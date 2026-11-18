#!/usr/bin/env python3
"""Build the source appendix PDF: every document and ledger extract cited in the summary for Hugh.

Usage: python3.13 build_source_appendix.py <repo> <data-dir with qb_gl.csv / finaloop_gl.csv> <work-dir> <output.pdf>
Needs: pandas, openpyxl, pypdf, reportlab; node + playwright (render_many.js); soffice for the .docx.
"""
import sys, os, re, html, csv, json, subprocess, io
import pandas as pd, openpyxl
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

REPO, DATA, WORK, OUT = sys.argv[1:5]
HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(WORK, exist_ok=True)
HUGH = os.path.join(REPO, "Jer to Investors", "2026-11-18 - From Hugh (tax returns and Clark draft)")
QBDIR = os.path.join(REPO, "Financials", "Quickbooks")

CSS = """
@page{ size:Letter; margin:0.55in 0.55in 0.75in 0.55in; }
*{box-sizing:border-box}
body{margin:0;font:400 9.4pt/1.42 "Inter","Liberation Sans",Arial,sans-serif;color:#0b0b0b;font-variant-numeric:tabular-nums}
h1{font-size:20pt;font-weight:650;margin:0 0 6pt;letter-spacing:-.01em;line-height:1.15}
h2{font-size:12.5pt;font-weight:650;margin:16pt 0 3pt;break-after:avoid}
h3{font-size:10.2pt;font-weight:650;margin:12pt 0 2pt;break-after:avoid}
p{margin:0 0 6pt;color:#3f3e3a}
p.note{font-size:8.2pt;color:#7c7a73;margin:2pt 0 6pt}
table{border-collapse:collapse;width:100%;font-size:7.3pt;line-height:1.3;margin:2pt 0 8pt}
th{text-align:left;font-weight:600;border-bottom:1px solid #8f8d85;padding:2.5pt 4pt 2.5pt 0;font-size:7pt;color:#3f3e3a}
td{padding:2pt 4pt 2pt 0;border-bottom:1px solid #e4e3dc;vertical-align:top;word-break:break-word}
td.n,th.n{text-align:right;white-space:nowrap;padding-right:0}
th.n{white-space:normal;padding-left:8pt;vertical-align:bottom}
td.d{white-space:nowrap}
tr{break-inside:avoid}
tr.tot td{font-weight:650;border-top:1px solid #8f8d85;border-bottom:none}
tr.tot + tr.tot td{border-top:none}
table.big{font-size:9pt} table.big th{font-size:8.4pt} table.big td{padding:3.5pt 6pt 3.5pt 0}
.page{break-after:page}
.div{height:8.6in;display:flex;flex-direction:column;justify-content:center}
.div .letter{font-size:11pt;letter-spacing:.14em;color:#7c7a73;text-transform:uppercase}
.div h1{font-size:26pt;margin:6pt 0 12pt}
.div p{font-size:11pt;max-width:6in}
.div .meta{font-size:9.2pt;color:#7c7a73;margin-top:14pt}
"""

def esc(x):
    return html.escape("" if x is None else str(x))

def money(v):
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return ""
    return ("-" if v < 0 else "") + "{:,.2f}".format(abs(v))

def page(title, body):
    return "<!doctype html><html><head><meta charset='utf-8'><title>%s</title><style>%s</style></head><body>%s</body></html>" % (esc(title), CSS, body)

def table(rows, cols, numcols=(), datecols=(), cls="", total=None):
    out = ["<table class='%s'><thead><tr>" % cls]
    for key, label in cols:
        out.append("<th class='%s'>%s</th>" % ("n" if key in numcols else "", esc(label)))
    out.append("</tr></thead><tbody>")
    for r in rows:
        out.append("<tr>")
        for key, _ in cols:
            v = r.get(key, "")
            if key in numcols:
                out.append("<td class='n'>%s</td>" % (money(v) if isinstance(v, (int, float)) else esc(v)))
            else:
                out.append("<td class='%s'>%s</td>" % ("d" if key in datecols else "", esc(v)))
        out.append("</tr>")
    for tot in ([] if total is None else total if isinstance(total, list) else [total]):
        out.append("<tr class='tot'>")
        for key, _ in cols:
            out.append("<td class='%s'>%s</td>" % ("n" if key in numcols else "", money(tot[key]) if key in tot and isinstance(tot[key], (int, float)) else esc(tot.get(key, ""))))
        out.append("</tr>")
    out.append("</tbody></table>")
    return "".join(out)

HEALTH = re.compile(r"TALKIAT|THERAPY|PHARMACY", re.I)
def clean_memo(s, n=150):
    s = "" if s is None or (isinstance(s, float) and pd.isna(s)) else str(s)
    if HEALTH.search(s):
        return "[healthcare provider]"
    s = re.sub(r"ORIG CO NAME:|ORIG ID:\S+|DESC DATE:\d*|CO ENTRY DESCR:|SEC:\w+|TRACE#:\S+|EED:\d+|IND ID:\S+|TRN: ?\S+ ?TC|transaction ?#: ?\S+|reference#: ?\S+|WEB ID: ?\S+", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:n] + ("…" if len(s) > n else "")

# ------------------------------------------------------------------ ledgers
qb = pd.read_csv(os.path.join(DATA, "qb_gl.csv")).fillna("")
qb["amount"] = qb["amount"].astype(float)
qb["year"] = qb["date"].str[:4].astype(int)
fl = pd.read_csv(os.path.join(DATA, "finaloop_gl.csv")).fillna("")
fl["amount"] = fl["amount"].astype(float)
fl["date"] = fl["datetime_utc"].str[:10]

QCOLS = [("date", "Date"), ("type", "Type"), ("num", "No."), ("name", "Name"), ("memo", "Memo"), ("split", "Offset account"), ("amount", "Amount")]
def qrows(df):
    rows = []
    for _, r in df.iterrows():
        rows.append(dict(date=r["date"], type=r["type"], num=r["num"], name=str(r["name"])[:28], memo=clean_memo(r["memo"]), split=str(r["split"])[:34], amount=float(r["amount"])))
    return rows
def qtable(df, with_total=True):
    rows = qrows(df)
    tot = dict(memo="Net of the entries shown", amount=round(float(df["amount"].sum()), 2)) if with_total else None
    return table(rows, QCOLS, numcols=("amount",), datecols=("date", "type", "num"), total=tot)
BB = {r[0]: float(r[1]) for r in csv.reader(open(os.path.join(DATA, "qb_beginning_balances.csv"))) if r[0] and r[1] and r[1].replace("-", "").replace(".", "").isdigit()}
def acct(name):
    d = qb[qb["account"] == name]
    opening = BB.get(name, 0.0)
    rows = qrows(d)
    if opening:
        rows.insert(0, dict(date="2020-01-01", type="", num="", name="", memo="Balance brought forward at January 1, 2020", split="", amount=opening))
    tots = [dict(memo="Balance at December 31, 2025", amount=round(opening + float(d[d["date"] <= "2025-12-31"]["amount"].sum()), 2))]
    if (d["date"] > "2025-12-31").any():
        tots.append(dict(memo="Balance at March 27, 2026, the end of the export", amount=round(opening + float(d["amount"].sum()), 2)))
    return table(rows, QCOLS, numcols=("amount",), datecols=("date", "type", "num"), total=tots)
def qacct(name, where=None):
    d = qb[qb["account"] == name]
    if where is not None:
        d = d[where(d)]
    return d
def journal(num, date=None):
    d = qb[(qb["num"] == num) & (qb["type"] == "Journal Entry")]
    if date:
        d = d[d["date"] == date]
    rows = []
    for _, r in d.iterrows():
        rows.append(dict(date=r["date"], num=r["num"], account=r["account"], memo=clean_memo(r["memo"], 170), amount=float(r["amount"])))
    return table(rows, [("date", "Date"), ("num", "No."), ("account", "Account"), ("memo", "Memo"), ("amount", "Amount")], numcols=("amount",), datecols=("date", "num"))

SIGNS_QB = "<p class='note'>Extracted without alteration from the QuickBooks general ledger export covering January 1, 2020 to March 27, 2026 (file: BRAVADO SPICE LLC_General Ledger - full.csv). Amounts carry the sign QuickBooks gives each account: in a liability or equity account a positive amount increases what the company owes; in an asset account a positive amount increases what is owed to the company; in a bank account a negative amount is money leaving. Bank descriptors are shortened by removing routing and trace codes. Journal entries with several lines show a blank offset account.</p>"

k = ["<h1>Exhibit K. QuickBooks general ledger extracts</h1>", SIGNS_QB]
k.append("<h2>K-1. Account \"Wages Due to Jeremiah\" (all entries)</h2><p>Salary recorded as owed to Jeremiah Tallerine and not paid. Positive amounts add to what the company owes him; negative amounts are payments charged against it.</p>")
k.append(acct("Wages Due to Jeremiah"))
k.append("<h2>K-2. Account \"Due from Jer\" (all entries)</h2><p>Amounts recorded as owed to the company by Jeremiah Tallerine.</p>")
k.append(acct("Due from Jer"))
k.append("<h2>K-3. Account \"33500 Due to Jeremiah\" (all entries)</h2><p>The running account between the company and Jeremiah Tallerine. Positive entries record expenses he paid for the company or year-end transfers; negative entries are company money paid to him or to card accounts in his name. A negative balance means he has received more than was recorded as owed to him.</p>")
k.append(acct("33500 Due to Jeremiah"))
k.append("<h2>K-4. Account \"53000 Jer's Draw\" (all entries)</h2>")
k.append(acct("53000 Jer's Draw"))
k.append("<h2>K-5. Journal entries cited, with every line</h2>")
for num, date, label in [("AJE-547", None, "Accrual of unpaid wages for 2025"), ("AJE-345", None, "January 2025 tie-out entry"), ("AJE-387", None, "Reclassification, January 2025"), ("AJE-388", None, "Reclassification, February 2025"),
                         ("AJE-39", None, "Year-end 2022 transfer to Due from Jer"), ("AJE-172", None, "July 2023 transfer"), ("AJE-177", None, "Year-end 2023 transfer"), ("CPA AJE 1 - 2024", None, "Year-end 2024 consolidation"), ("AJE-397", None, "Year-end 2024 transfer"),
                         ("AJE-307", None, "Sale of the Chevrolet"), ("AJE-229", None, "Card balance written off, June 2024"), ("AJE-455", None, "Card balance written off, June 2025"), ("AJE-456", None, "Card balance written off, June 2025"), ("AJE-292", None, "Payroll check of September 18, 2024")]:
    k.append("<h3>%s — %s</h3>" % (esc(num), esc(label)))
    k.append(journal(num, date))
k.append("<h2>K-6. Account \"Loan From Nguyen\" (all entries)</h2>")
k.append(acct("Loan From Nguyen"))
pay = qb[(qb["name"].str.contains("Nguyen", case=False)) & (qb["account"].str.contains("Chase|Found")) & (qb["year"] >= 2025)]
if len(pay):
    k.append("<h3>Bank payments naming Nguyen, 2025 onward</h3>")
    k.append(qtable(pay))
k.append("<h2>K-7. Account \"33100 Anthony Tallerine LOC\" (all entries)</h2>")
k.append(acct("33100 Anthony Tallerine LOC"))
k.append("<h2>K-8. Account \"Member Equity - Coinbase\" (all entries)</h2><p>The account in which Comatri, Inc.'s two payments were recorded.</p>")
k.append(acct("Member Equity - Coinbase"))
k.append("<h2>K-9. Account \"80001 Other Misc Income\", 2024 and 2025</h2>")
k.append(qtable(qacct("80001 Other Misc Income", lambda d: d["year"].isin([2024, 2025]))))
open(os.path.join(WORK, "exK.html"), "w").write(page("Exhibit K", "".join(k)))

# ------------------------------------------------------------------ Finaloop
FCOLS = [("date", "Date"), ("src", "Source"), ("desc", "Description"), ("cls", "Classification"), ("amount", "Amount")]
def ftable(d, with_total=True):
    rows = []
    for _, r in d.sort_values("datetime_utc").iterrows():
        rows.append(dict(date=r["date"], src=str(r["Source"])[:44], desc=clean_memo(r["Description"], 150), cls=str(r["Transaction Classification"])[:30], amount=float(r["amount"])))
    tot = dict(desc="Net of the entries shown", amount=round(float(d["amount"].sum()), 2)) if with_total else None
    return table(rows, FCOLS, numcols=("amount",), datecols=("date",), total=tot)
def facct(prefix):
    return fl[fl["account"].str.startswith(prefix)]

L = ["<h1>Exhibit L. Finaloop general ledger extracts</h1>",
     "<p class='note'>Extracted from the Finaloop general ledger exported July 23, 2026 (file: Bravado - General_Ledger_2026_YTD Finaloop - Unlocked.numbers). Entries dated December 31, 2025 are Finaloop's opening balances. Amounts carry the sign Finaloop gives each account. Finaloop records no user name against any entry. Names of healthcare providers in descriptions are replaced with \"[healthcare provider]\"; nothing else is altered.</p>"]
L.append("<h2>L-1. Account \"Due to/from owner - non-interest balance - Jeremiah Tallerine\" (all entries)</h2><p>A positive balance is owed to the company by Jeremiah Tallerine.</p>")
L.append(ftable(facct("Due to/from owner")))
L.append("<h2>L-2. Account \"Distributions - Jeremiah Tallerine\" (all entries)</h2>")
L.append(ftable(facct("Distributions - Jeremiah")))
L.append("<h2>L-3. Account \"Reimbursements to owners\" (all entries)</h2><p>An expense account.</p>")
L.append(ftable(fl[fl["account"] == "Reimbursements to owners"]))
L.append("<h2>L-4. Owner capital accounts (all entries)</h2>")
for a in ["Capital - Jeremiah Tallerine", "Capital - Blake Benthall", "Capital - Hugh & Christy Nguyen", "Capital - Mark Clark"]:
    L.append("<h3>%s</h3>" % esc(a))
    L.append(ftable(fl[fl["account"] == a]))
L.append("<h2>L-5. Account \"Payroll payable\"</h2><p>Opening entries and the net of all payroll activity in 2026.</p>")
pp = fl[fl["account"] == "Payroll payable"]
L.append(ftable(pp[pp["date"] <= "2025-12-31"], with_total=False))
L.append(table([dict(a="Opening entries, December 31, 2025", v=round(float(pp[pp["date"] <= "2025-12-31"]["amount"].sum()), 2)),
                dict(a="Gusto payroll entries, January 1 to July 23, 2026 (net)", v=round(float(pp[pp["date"] > "2025-12-31"]["amount"].sum()), 2)),
                dict(a="Balance at July 23, 2026", v=round(float(pp["amount"].sum()), 2)),
                dict(a="Last payroll entry date", v=str(pp["date"].max()))], [("a", ""), ("v", "Amount")], numcols=("v",), cls="big"))
L.append("<h2>L-6. All entries of $6,033.40, April 7, 2026</h2>")
L.append(ftable(fl[(fl["amount"].abs().round(2) == 6033.40)].assign(Source=lambda d: d["account"].str[:44]), with_total=False))
L.append("<p class='note'>In this table the \"Source\" column shows the account each line was posted to.</p>")
L.append("<h2>L-7. Loans: Nguyen, Tallerine and SBA (all entries)</h2>")
for a in ["Related party loan payable - Hugh & Christy Nguyen", "Line of credit - Anthony Tallerine", "Long-term loan payable - Small Business Administration"]:
    L.append("<h3>%s</h3>" % esc(a))
    L.append(ftable(fl[fl["account"] == a]))
L.append("<h2>L-8. Unpaid vendor bills</h2>")
vb = fl[fl["account"].isin(["Inventory vendors - bills", "Operational vendors - bills"])]
L.append("<h3>Opening entries, December 31, 2025</h3>")
L.append(ftable(vb[vb["date"] <= "2025-12-31"].assign(Source=lambda d: d["account"])))
L.append(table([dict(a=a, v=round(float(vb[(vb["account"] == a) & (vb["date"] <= "2026-07-22")]["amount"].sum()), 2)) for a in ["Inventory vendors - bills", "Operational vendors - bills"]] +
               [dict(a="Total unpaid vendor bills at July 22, 2026", v=round(float(vb[vb["date"] <= "2026-07-22"]["amount"].sum()), 2))], [("a", "Account"), ("v", "Balance at July 22, 2026")], numcols=("v",), cls="big"))
L.append("<h2>L-9. Other payments to card accounts or a personal account in his name, recorded outside L-1 to L-3</h2>")
other = pd.concat([
    fl[(fl["account"] == "Unidentified payouts & transfers") & fl["Description"].str.contains("CITI CARD")],
    fl[(fl["account"] == "Miscellaneous expenses") & fl["Description"].str.contains("CITI AUTOPAY")],
    fl[(fl["account"] == "Money-out") & fl["Description"].str.contains("5820") & (fl["date"] >= "2026-07-04") & (fl["Transaction Classification"] == "") & (fl["amount"] > 0) & ~fl["Description"].str.contains("fee", case=False)],
    fl[(fl["account"] == "Money in transit") & fl["Description"].str.contains("5820") & (fl["amount"].abs().round(2) == 25.00)].head(1),
    fl[(fl["account"] == "Other operations expenses") & fl["Description"].str.contains("7588")],
])
L.append(ftable(other.assign(Source=lambda d: d["account"].str[:44])))
L.append("<p class='note'>In this table the \"Source\" column shows the account each line was posted to. Check #7588 is recorded in QuickBooks as paid to Finnacle Managing Co LLC with the memo \"Tallerine/ Whitenton Lease App.\"</p>")
bs = pd.read_csv(os.path.join(DATA, "finaloop_Balance_Sheet_Index.csv")).fillna("")
plx = pd.read_csv(os.path.join(DATA, "finaloop_Profit_and_Loss_Index.csv")).fillna("")
def idx_table(df, labels):
    cols = list(df.columns)
    rows = []
    for _, r in df.iterrows():
        d = dict(a=r[cols[0]])
        for i, c in enumerate(cols[1:]):
            try:
                d["v%d" % i] = float(r[c])
            except Exception:
                d["v%d" % i] = r[c]
        rows.append(d)
    return table(rows, [("a", "Account")] + [("v%d" % i, labels[i]) for i in range(len(cols) - 1)], numcols=tuple("v%d" % i for i in range(len(cols) - 1)))
L.append("<h2>L-10. Finaloop's own balance sheet totals at the July 23, 2026 export</h2>")
L.append(idx_table(bs, ["Starting balance", "Ending balance"]))
L.append("<h2>L-11. Finaloop's own profit-and-loss totals, 2026 to the July 23 export</h2><p class='note'>Finaloop shows income, discounts, refunds and expenses all as positive numbers.</p>")
L.append(idx_table(plx, ["Year total"]))
open(os.path.join(WORK, "exL.html"), "w").write(page("Exhibit L", "".join(L)))

# ------------------------------------------------------------------ QuickBooks reports
M = ["<style>table.big td{padding:2.4pt 6pt 2.4pt 0} h2{margin-top:12pt}</style><h1>Exhibit M. QuickBooks official reports: key lines</h1>",
     "<p class='note'>Figures read from the official QuickBooks exports in the company's files (\"Profit and Loss by Month\" for each year, and \"Balance Sheet\", all dates). The full reports are spreadsheets and are not reproduced.</p>",
     "<h2>M-1. Profit and loss by year</h2>"]
rows = []
for y in range(2020, 2026):
    wb = openpyxl.load_workbook(os.path.join(QBDIR, "BRAVADO SPICE LLC_Profit and Loss by Month - %d.xlsx" % y), data_only=True)
    ws = wb.active
    d = dict(year=str(y))
    for r in ws.iter_rows(values_only=True):
        lab = str(r[0] or "").strip().lower()
        nums = [c for c in r[1:] if isinstance(c, (int, float))]
        if not nums:
            continue
        for key, pref in [("inc", ("total for income", "total income")), ("cogs", ("total for cost of goods sold", "total cost of goods sold")), ("noi", ("net operating income",)), ("oth", ("net other income",)), ("net", ("net income",))]:
            if lab.startswith(pref) and key not in d:
                d[key] = round(float(nums[-1]), 2)
    rows.append(d)
M.append(table(rows, [("year", "Year"), ("inc", "Total income (sales)"), ("cogs", "Cost of goods sold"), ("noi", "Net operating income"), ("oth", "Net other income"), ("net", "Net income")], numcols=("inc", "cogs", "noi", "oth", "net"), cls="big"))
M.append("<h2>M-2. Balance sheet lines at each December 31</h2>")
wb = openpyxl.load_workbook(os.path.join(QBDIR, "BRAVADO SPICE LLC_Balance Sheet - Quickbooks.xlsx"), data_only=True)
ws = wb.active
allrows = list(ws.iter_rows(values_only=True))
hdr = next(r for r in allrows if any(isinstance(c, str) and c.strip() == "Dec 2025" for c in r))
colidx = {lab: i for i, lab in enumerate(hdr) if isinstance(lab, str)}
want = ["Dec 2022", "Dec 2023", "Dec 2024", "Dec 2025"]
keys = ["Total for Bank Accounts", "Total Bank Accounts", "Due from James", "Due from Jer", "Total for Assets", "Total for Accounts Payable", "Total Accounts Payable", "33500 Due to Jeremiah", "Accrued Expense", "Wages Due to Jeremiah", "Loan From Nguyen", "33100 Anthony Tallerine LOC", "Total for Liabilities", "Member Equity - Coinbase", "Total for Equity", "Total Equity"]
rows = []
seen = set()
for r in allrows:
    lab = str(r[0] or "").strip()
    if any(lab == kx or lab.endswith(kx) for kx in keys) and lab not in seen:
        seen.add(lab)
        d = dict(a=lab)
        for i, w in enumerate(want):
            v = r[colidx[w]] if w in colidx else None
            d["v%d" % i] = round(float(v), 2) if isinstance(v, (int, float)) else ""
        rows.append(d)
M.append(table(rows, [("a", "Line")] + [("v%d" % i, w) for i, w in enumerate(want)], numcols=("v0", "v1", "v2", "v3"), cls="big"))
M.append("<p class='note'>QuickBooks shows \"33500 Due to Jeremiah\" within liabilities; a negative figure there is an amount he owes the company.</p>")
M.append("<h2>M-3. Salaries and wages recorded each year, compared with the tax returns</h2>")
sal = qb[qb["account"] == "73902 Salaries & Wages"]
wd = qb[qb["account"] == "Wages Due to Jeremiah"]
ret = {2023: 384873 + 10039, 2024: 140131 + 3694, 2025: 62919}
rows = []
for y in [2023, 2024, 2025]:
    s = sal[sal["year"] == y]
    rows.append(dict(y=str(y), tot=round(float(s["amount"].sum()), 2), gusto=round(float(s[s["num"] == "Gusto"]["amount"].sum()), 2), oth=round(float(s[s["num"] != "Gusto"]["amount"].sum()), 2),
                     wdchg=round(float(wd[wd["year"] == y]["amount"].sum()), 2), ret=float(ret[y])))
M.append(table(rows, [("y", "Year"), ("tot", "Account 73902 total"), ("gusto", "of which payroll (Gusto) entries"), ("oth", "of which other entries"), ("wdchg", "Net change in Wages Due to Jeremiah"), ("ret", "Wage lines on the tax return")], numcols=("tot", "gusto", "oth", "wdchg", "ret"), datecols=("y",), cls="big"))
M.append("<p class='note'>Tax-return wage lines: 2023 Form 1120-S lines 7 and 8 ($10,039 and $384,873); 2024 Form 1120-S lines 7 and 8 ($3,694 and $140,131); 2025 Form 1120 line 13 ($62,919). 2025: $131,952.09 of payroll entries less $62,919 equals $69,033.09.</p>")
open(os.path.join(WORK, "exM.html"), "w").write(page("Exhibit M", "".join(M)))

# ------------------------------------------------------------------ audit log
N = ["<h1>Exhibit N. QuickBooks audit log extracts, 2026</h1>",
     "<p class='note'>From the QuickBooks audit log export for 2026 (file: Audit Log - 2026.csv). The export shows the month, day and time of each event without the year; every event in this file is in 2026.</p>"]
alog = []
with open(os.path.join(QBDIR, "Audit Log - 2026.csv"), newline="") as f:
    rd = csv.reader(f)
    next(rd)
    for row in rd:
        if len(row) >= 3:
            alog.append(dict(when=row[0], user=row[1], event=row[2].strip()))
N.append("<h2>N-1. Creation of journal entry AJE-547</h2>")
N.append(table([a for a in alog if "AJE-547" in a["event"] and a["user"].startswith("Strata")][::-1], [("when", "Date and time"), ("user", "User"), ("event", "Event")], cls="big"))
N.append("<p class='note'>Shows the events on the day the entry was created. Later events on the same entry appear in the full log and are not reproduced here.</p>")
strata = [a for a in alog if a["user"].startswith("Strata")]
N.append("<h2>N-2. Strata Cloud Accountants: number of logged events by month, 2026</h2>")
cnt = {}
for a in strata:
    m = a["when"].split(" ")[0]
    cnt[m] = cnt.get(m, 0) + 1
N.append(table([dict(m=m, c=str(cnt[m])) for m in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"] if m in cnt], [("m", "Month"), ("c", "Events")], cls="big"))
N.append("<h2>N-3. Strata Cloud Accountants: last ten logged events</h2>")
N.append(table(strata[:10], [("when", "Date and time"), ("user", "User"), ("event", "Event")], cls="big"))
open(os.path.join(WORK, "exN.html"), "w").write(page("Exhibit N", "".join(N)))

# ------------------------------------------------------------------ computation
O = ["<h1>Exhibit O. Computation: cash paid to Jeremiah Tallerine by year</h1>",
     "<p>This exhibit is a computation, not a company document. It shows how the yearly totals in the summary were derived from the ledger entries reproduced in Exhibits K and L.</p>",
     "<h2>O-1. What is counted</h2>",
     "<p>Every line in a company bank or company credit-card account whose offsetting account is one of his four QuickBooks accounts (33500 Due to Jeremiah, Due from Jer, 53000 Jer's Draw, Wages Due to Jeremiah); payments of card accounts in his name and transfers to his personal accounts that the bookkeepers recorded directly as an expense; and, for 2026, the Finaloop entries in Exhibit L-1, L-2, L-3 and L-9. Journal entries that move balances between accounts are not cash and are not counted.</p>",
     "<p>Not counted: check 2418 of September 2020 ($14,078), which the CPA reclassified as James Nelson's 2019 income tax; charges on the credit card ending 9532, which is in James Nelson's name; check #7590 of January 27, 2026 ($3,250), which QuickBooks records as paid to a third party, together with the $3,250 he transferred in four days earlier; and his payroll salary for 2021 and 2022, which the payroll entries do not separate by employee.</p>",
     "<h2>O-2. Cash paid, by year and by how the bookkeepers recorded it</h2>"]
comp = [("2022", 41712, 1459, 17792, 0, 23920), ("2023", 77017, 6204, 41334, 0, 35683), ("2024", 87509, 3829, 26126, 37992, 23391), ("2025", 118128, 500, 22112, 2000, 94016), ("2026, Jan 1 to Jul 22", 49192, 580, 0, 0, 49192)]
O.append(table([dict(y=c[0], g=float(c[1]), r=float(c[2]), i=float(c[3]), w=float(c[4]), u=float(c[5])) for c in comp],
               [("y", "Year"), ("g", "Paid (gross)"), ("r", "Returned by him"), ("i", "Matched by itemized entries"), ("w", "Recorded as payment of unpaid salary"), ("u", "No itemization in the ledger")], numcols=("g", "r", "i", "w", "u"), datecols=("y",), cls="big"))
O.append("<p class='note'>\"Matched by itemized entries\" is the total of journal entries and vendor bills that credit his account with business-expense detail (Exhibit K-3 and K-4). \"Recorded as payment of unpaid salary\" is the $35,644.29 of 2024 transfers charged to Wages Due to Jeremiah, one $2,347.34 payroll check in 2024, and $2,000 in 2025 (Exhibit K-1). \"No itemization\" is the remainder: for 2022 to 2024 it corresponds to the balances the accountants moved to Due from Jer at each year-end plus payments recorded directly as expenses; for 2025 it is the $88,082.47 left in account 33500 plus $5,330.80 of draws and $603 recorded as expenses; for 2026 it is every payment.</p>")
O.append("<h2>O-3. 2026 detail (Finaloop, January 1 to July 22)</h2>")
O.append(table([dict(a="Payments to card accounts in his name (Capital One $22,959.89; Citi $980.42; Petal $388.52)", v=24328.83), dict(a="Transfers to Capital One personal checking 5820 (36 transfers)", v=23689.22),
                dict(a="Personal charges posted to his owner account", v=923.50), dict(a="Check #7588, lease application", v=250.00), dict(a="Total", v=49191.55)], [("a", "Item"), ("v", "Amount")], numcols=("v",), cls="big"))
open(os.path.join(WORK, "exO.html"), "w").write(page("Exhibit O", "".join(O)))

# ------------------------------------------------------------------ image exhibit
img = os.path.join(REPO, "Correspondence", "2026-08-25 - Mark Clark text to Hugh re S corp.jpg")
open(os.path.join(WORK, "exJ.html"), "w").write(page("Exhibit J", "<div style='text-align:center'><img src='file://%s' style='max-width:100%%;max-height:8.9in'></div>" % img))

# ------------------------------------------------------------------ exhibits
subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", WORK, os.path.join(REPO, "Jer to Investors", "2026-07-22 - All Investors", "2026-07-22-Bravado-State-of-Business-v4.docx")], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
EX = [
    dict(L="A", t="Mark Clark's draft financial statements", d="Draft income statement and balance sheet for 2024, 2025 and the nine months to September 30, 2026. Received from Hugh Nguyen on November 18, 2026.", f=["(Mark_DRAFT PL).pdf", "(Mark_DRAFT BS).pdf"], parts=[os.path.join(HUGH, "(Mark_DRAFT PL).pdf"), os.path.join(HUGH, "(Mark_DRAFT BS).pdf")]),
    dict(L="B", t="2025 Form 1120, U.S. Corporation Income Tax Return", d="As provided to the members, with the Statement of Termination of S Corporation Election as its last page. Page 4 of the form was not in the copy received.", f=["Bravado Spice 2025 Form 1120.pdf"], parts=[os.path.join(HUGH, "Bravado Spice 2025 Form 1120.pdf")]),
    dict(L="C", t="2024 Form 1120-S, U.S. Income Tax Return for an S Corporation", d="As provided to the members.", f=["Bravado Spice 2024 Form 1120-S.pdf"], parts=[os.path.join(HUGH, "Bravado Spice 2024 Form 1120-S.pdf")]),
    dict(L="D", t="2023 Form 1120-S, U.S. Income Tax Return for an S Corporation", d="Client copy, as provided to the members.", f=["Bravado Spice 2023 Form 1120-S.pdf"], parts=[os.path.join(HUGH, "Bravado Spice 2023 Form 1120-S.pdf")]),
    dict(L="E", t="2024 Schedules K-1, Hugh Nguyen and Christy Nguyen", d="Each package includes the K-1, its supplemental statements, the loans-from-shareholder statement and the \"Changes in Ownership\" worksheet.", f=["2024 Schedule K-1 Hugh Nguyen.pdf", "2024 Schedule K-1 Christy Nguyen.pdf"], parts=[os.path.join(HUGH, "2024 Schedule K-1 Hugh Nguyen.pdf"), os.path.join(HUGH, "2024 Schedule K-1 Christy Nguyen.pdf")]),
    dict(L="F", t="Comatri, Inc. Investment Agreement, July 2024", d="Signed July 21 and 22, 2024, with the Operating Agreement of Bravado Spice LLC attached as its exhibit.", f=["COMATRI_INC_INVESTMENT_AGREEMENT.pdf"], parts=[os.path.join(REPO, "Jer to Investors", "2024-07-21 - Comatri Agreement 1", "COMATRI_INC_INVESTMENT_AGREEMENT.pdf")]),
    dict(L="G", t="Comatri, Inc. Investment Agreement 2, November 2024", d="Signed November 26, 2024, with the Operating Agreement and the listing of members attached.", f=["2024-11-26 - Comatri__Inc_2nd_investment_agreement..pdf"], parts=[os.path.join(REPO, "Comatri Investment Agreements", "2024-11-26 - Comatri__Inc_2nd_investment_agreement..pdf")]),
    dict(L="H", t="\"State of the Business,\" July 2026", d="The version circulated to all investors on July 22, 2026. Converted from the Word file received; page breaks may differ from the original.", f=["2026-07-22-Bravado-State-of-Business-v4.docx"], parts=[os.path.join(WORK, "2026-07-22-Bravado-State-of-Business-v4.pdf")]),
    dict(L="I", t="Investor briefing, August 24, 2026", d="As circulated to all investors.", f=["2026-08-24-State-of-Bravado-Investor-Briefing.pdf"], parts=[os.path.join(REPO, "Jer to Investors", "2026-08-24 - All Investors", "2026-08-24-State-of-Bravado-Investor-Briefing.pdf")]),
    dict(L="J", t="Mark Clark's text message to Hugh Nguyen, August 2026", d="Screenshot supplied by Hugh Nguyen. The image shows no date; August 25, 2026 is the date under which it was saved.", f=["2026-08-25 - Mark Clark text to Hugh re S corp.jpg"], parts=[os.path.join(WORK, "exJ.pdf")]),
    dict(L="K", t="QuickBooks general ledger extracts", d="The accounts and journal entries cited in the summary, reproduced line by line from the general ledger export.", f=["BRAVADO SPICE LLC_General Ledger - full.csv"], parts=[os.path.join(WORK, "exK.pdf")]),
    dict(L="L", t="Finaloop general ledger extracts", d="The accounts cited in the summary, reproduced line by line from the Finaloop export of July 23, 2026, with Finaloop's own account totals.", f=["Bravado - General_Ledger_2026_YTD Finaloop - Unlocked.numbers"], parts=[os.path.join(WORK, "exL.pdf")]),
    dict(L="M", t="QuickBooks official reports: key lines", d="Yearly profit-and-loss totals, year-end balance sheet lines, and a comparison of recorded wages with the tax returns.", f=["BRAVADO SPICE LLC_Profit and Loss by Month - 2020 to 2025.xlsx", "BRAVADO SPICE LLC_Balance Sheet - Quickbooks.xlsx"], parts=[os.path.join(WORK, "exM.pdf")]),
    dict(L="N", t="QuickBooks audit log extracts, 2026", d="The creation of journal entry AJE-547 and the last recorded activity of the outside accounting firm.", f=["Audit Log - 2026.csv"], parts=[os.path.join(WORK, "exN.pdf")]),
    dict(L="O", t="Computation: cash paid to Jeremiah Tallerine by year", d="How the yearly totals in the summary were derived from the ledger entries in Exhibits K and L. A computation, not a company document.", f=[], parts=[os.path.join(WORK, "exO.pdf")]),
]
INDEX = [
    (1, "Mark Clark's draft statements", "A"), (2, "Nguyen note: payments and balance", "K-6; L-7"), (3, "Outside accounting firm's last activity", "N-2, N-3"), (4, "Sales and net result by year", "M-1; L-11"),
    (5, "Other income and card balances written off", "K-9; K-5 (AJE-455, AJE-456, AJE-229)"), (6, "Unpaid vendor bills at July 22, 2026", "L-8"), (7, "Older payables within the total", "L-8 (opening entries); H (debt table); M-2"),
    (8, "July 2026 \"State of the Business\"", "H"), (9, "Salary recorded as owed to Jer", "K-1"), (10, "Date AJE-547 was created", "N-1; K-5"), (11, "Operating Agreement, Article 5.1", "F or G (the attached Operating Agreement)"),
    (12, "Year-end transfers to \"Due from Jer\"", "K-2, K-3, K-4, K-5"), (13, "The $74,364 difference", "K-2, K-3, K-4; L-1; M-2"), (14, "Loans to shareholders, 2025 return", "B (Schedule L and Statement #11)"),
    (15, "Chevrolet sale proceeds", "K-5 (AJE-307); C (Form 4797)"), (16, "Finaloop owner account and payroll payable", "L-1; L-5"), (17, "End of payroll", "L-5"), (18, "2026 payments to Jer", "L-1, L-2, L-3, L-9; O-3"),
    (19, "Itemized reimbursement entries", "K-3; L-3"), (20, "Payments recorded against unpaid salary", "K-1; K-5 (AJE-292)"), (21, "Cash paid by year", "O; K-1 to K-4"), (22, "Retained earnings in Mark's draft and Finaloop", "A; L-10"),
    (23, "April 7, 2026 entries", "L-6"), (24, "Mark Clark's text message", "J"), (25, "Statement of termination of S election", "B (last page)"), (26, "Comatri's agreements and deposits", "F; G; K-8"),
    (27, "2024 return: shareholders and paid-in capital", "C (page 1 and Schedule L)"), (28, "Hugh Nguyen's 2024 K-1", "E"), (29, "Accounting method and loss per books on the returns", "B; C; D (Schedule B and Schedule M-1)"),
    (30, "Liabilities not on the 2025 return's balance sheet", "M-2; B (Schedule L)"), (31, "Tallerine family loan", "H; I; B (Statement #11); A; K-7"), (32, "Share counts", "B (Schedule G); G (Exhibit 2 to the agreement)"),
]
json.dump([dict(html=os.path.join(WORK, "ex%s.html" % x), pdf=os.path.join(WORK, "ex%s.pdf" % x)) for x in "JKLMNO"], open(os.path.join(WORK, "render1.json"), "w"))
subprocess.run(["node", os.path.join(HERE, "render_many.js"), os.path.join(WORK, "render1.json")], check=True)

def npages(p):
    return len(PdfReader(p).pages)
for e in EX:
    e["n"] = sum(npages(p) for p in e["parts"])

# dividers
dv = []
for e in EX:
    dv.append("<div class='page'><div class='div'><div class='letter'>Exhibit %s</div><h1>%s</h1><p>%s</p><p class='meta'>%s<br>%d page%s follow this one.</p></div></div>" % (
        e["L"], esc(e["t"]), esc(e["d"]), ("Source file%s: " % ("s" if len(e["f"]) > 1 else "") + esc("; ".join(e["f"]))) if e["f"] else "Prepared from Exhibits K and L.", e["n"], "" if e["n"] == 1 else "s"))
open(os.path.join(WORK, "dividers.html"), "w").write(page("Dividers", "".join(dv)))

def front(starts, total):
    b = ["<div class='page'><div class='div' style='height:8.4in'><div class='letter'>Reference document</div><h1>Bravado Spice LLC: source appendix</h1>",
         "<p>The documents and ledger extracts behind \"Bravado Spice LLC: questions for the members' meeting,\" dated November 18, 2026.</p>",
         "<p style='font-size:10pt'>Exhibits A to J are company and investor documents, reproduced in full as received. Exhibits K to N are extracts from the company's own ledgers and reports, reproduced line by line. Exhibit O is a computation. Taxpayer identification numbers were already blacked out in the copies received. In the ledger extracts, names of healthcare providers are replaced with \"[healthcare provider]\"; nothing else is altered.</p>",
         "<p style='font-size:10pt'>Every page carries its exhibit letter and its page number in this appendix at the foot. The index on the following pages lists each numbered source in the summary and where to find it.</p>",
         "<p class='meta'>%d pages. Compiled November 18, 2026. Not legal or tax advice.</p></div></div>" % total]
    b.append("<h2 style='margin-top:0'>Contents</h2>")
    b.append(table([dict(l="Exhibit " + e["L"], t=e["t"], p="%d to %d" % (starts[e["L"]], starts[e["L"]] + e["n"])) for e in EX], [("l", "Exhibit"), ("t", "Document"), ("p", "Appendix pages")], cls="big"))
    b.append("<h2>Index of sources cited in the summary</h2><p class='note'>The number is the source number printed in the summary. Sections such as \"K-3\" are headings inside the exhibit.</p>")
    b.append(table([dict(n=str(n), s=s, w=w) for n, s, w in INDEX], [("n", "No."), ("s", "Source"), ("w", "Where in this appendix")], cls="big"))
    return page("Source appendix", "".join(b))

def render(pairs):
    json.dump(pairs, open(os.path.join(WORK, "render2.json"), "w"))
    subprocess.run(["node", os.path.join(HERE, "render_many.js"), os.path.join(WORK, "render2.json")], check=True)

open(os.path.join(WORK, "front.html"), "w").write(front({e["L"]: 0 for e in EX}, 0))
render([dict(html=os.path.join(WORK, "front.html"), pdf=os.path.join(WORK, "front.pdf")), dict(html=os.path.join(WORK, "dividers.html"), pdf=os.path.join(WORK, "dividers.pdf"))])
nf = npages(os.path.join(WORK, "front.pdf"))
starts, cur = {}, nf
for e in EX:
    starts[e["L"]] = cur + 1
    cur += 1 + e["n"]
total = cur
open(os.path.join(WORK, "front.html"), "w").write(front(starts, total))
render([dict(html=os.path.join(WORK, "front.html"), pdf=os.path.join(WORK, "front.pdf"))])
assert npages(os.path.join(WORK, "front.pdf")) == nf

# ------------------------------------------------------------------ merge and stamp
w = PdfWriter()
labels = []
for p in PdfReader(os.path.join(WORK, "front.pdf")).pages:
    w.add_page(p); labels.append("")
divs = PdfReader(os.path.join(WORK, "dividers.pdf")).pages
outline = []
for i, e in enumerate(EX):
    outline.append(("Exhibit %s. %s" % (e["L"], e["t"]), len(w.pages)))
    w.add_page(divs[i]); labels.append("Exhibit " + e["L"])
    for part in e["parts"]:
        for p in PdfReader(part).pages:
            w.add_page(p); labels.append("Exhibit " + e["L"])
assert len(w.pages) == total, (len(w.pages), total)
for i, pg in enumerate(w.pages):
    pg.transfer_rotation_to_content()
    wd, ht = float(pg.mediabox.width), float(pg.mediabox.height)
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(wd, ht))
    txt = "Bravado Spice source appendix   ·   %s   ·   page %d of %d" % (labels[i], i + 1, total) if labels[i] else "Bravado Spice source appendix   ·   page %d of %d" % (i + 1, total)
    c.setFont("Helvetica", 7)
    tw = c.stringWidth(txt, "Helvetica", 7)
    c.setFillColorRGB(1, 1, 1); c.rect(wd / 2 - tw / 2 - 6, 9, tw + 12, 11, stroke=0, fill=1)
    c.setFillColorRGB(0.35, 0.35, 0.33); c.drawString(wd / 2 - tw / 2, 12, txt)
    c.save(); buf.seek(0)
    pg.merge_page(PdfReader(buf).pages[0])
w.add_outline_item("Contents and index of sources", 0)
for title, idx in outline:
    w.add_outline_item(title, idx)
w.add_metadata({"/Title": "Bravado Spice LLC: source appendix", "/Subject": "Documents and ledger extracts cited in the summary of November 18, 2026"})
with open(OUT, "wb") as f:
    w.write(f)
print("pages", total, "front", nf, {e["L"]: (starts[e["L"]], e["n"]) for e in EX})
