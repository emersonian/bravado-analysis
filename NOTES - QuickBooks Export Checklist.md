# QuickBooks Export Checklist — What to Pull, in What Order

**Prepared:** August 26, 2026. You already hold: the full general ledger (2020–Aug 2026), monthly balance sheets (2014–Mar 2026), P&L by month (2014–2026), 18 audit-log exports, and an invoices/payments report. This lists what is **missing** and worth having.

---

## Read this first

**Your sign-ins are logged, and Jer can see them.** The audit log records "Blake Benthal — Signed In," which is how your August 24 session appears. Pulling a large batch of reports is visible activity. That is not a problem — you are a member with contractual and statutory inspection rights, and you were given this access deliberately in January 2025 — but it does mean:

- **Do Tier 1 in a single session, first.** Don't browse leisurely and come back next week for the important things.
- **Change nothing.** Any edit under your login appears in the audit log permanently and would be genuinely damaging. Read and export only.
- **Assume access could end.** It has not been revoked, but after the August 24 meeting you should not count on that continuing.

**Export both formats where offered.** PDF carries the company name, report basis, and a run date/time in the header — that is provenance, and it is harder to argue a PDF was manipulated. Excel is what makes the data analyzable. Take both; they cost nothing extra.

---

## TIER 1 — do these first, in one sitting

### 1. The AJE-547 audit history (highest value single item)
Open journal entry **AJE-547** (dated 12/31/2025, $69,033, "Accrue Unpaid Wages Due to Jeremiah"), then use **More → Audit History** on the transaction itself. This is *not* the same as the Audit Log you already have: the transaction-level audit history shows **field-by-field what changed on each edit** — which is exactly what the exported log does not.

That answers the open question about Mark Clark's three edits (Mar 31, Apr 8 ×2, 2026) definitively. Screenshot every screen, including the "show all" or expanded view.

**Do the same for:** AJE-345, AJE-387, AJE-388 (the 2025 wage reclasses), and AJE-229 ($23,217 "per Jer this is not payable").

### 2. Every attachment in the file
QuickBooks stores uploaded documents. The audit log confirms these exist:
- **"Jer Wages Accrual - $69033.pdf"** — the support for the wage accrual
- **"Mark Clark Investment Agreement_11.20.24.pdf"** — dated six days before your second agreement
- **"Bravado Invoice 40901.doc"** — the Clark invoice deleted Sep 18, 2025

Find them under the paperclip icon on individual transactions, or via any list view that shows attachments. Download all of them.

### 3. Journal report / adjusting journal entries, 2023–2026
A **Journal** report (Reports → For My Accountant → Journal) for each year, run with the **Created By / Last Modified By** columns turned on if available. This gives you every entry with its preparer — the thing the general ledger does not show.

### 4. A/P Aging Detail — as of several dates
Run **A/P Aging Detail** as of 12/31/2024, 12/31/2025, and today. This shows every vendor, invoice date, and how far past due — including the Mark Clark balance and the trade creditors. It is item 18 of the records request; pulling it yourself means you do not have to rely on him producing it.

### 5. Transaction List by Vendor — for the related parties
Run for: **Jeremiah Tallerine, Anthony Tallerine, Mark Clark, Hugh and Christy Nguyen, Marisa Whitenton, Veronica Tallerine.** All dates. This is the cleanest single view of related-party money movement.

---

## TIER 2 — completes the financial record

6. **Trial Balance** as of 12/31 for 2022, 2023, 2024, 2025 — the cleanest proof of what each account held at year-end.
7. **Balance Sheet Detail** (not summary) as of 12/31/2025 — shows the transactions composing each balance.
8. **Statement of Cash Flows** by year, 2023–2025 — you have P&L and balance sheet but not this.
9. **A/R Aging Detail** as of the same dates.
10. **Sales by Customer Summary** and **Sales by Customer Detail**, all dates — confirms the KeHE, Buc-ee's, Amazon and Faire mix independently.
11. **Sales by Product/Service Detail**, 2023–2026 — SKU-level revenue, which supports the KeHE assortment analysis.
12. **Reconciliation Reports** (Reports → Reconciliation Reports) for the operating accounts — these show reconciliation discrepancies and unreconciled items, which is where the "$107 vs $2,379" type of question lives.

---

## TIER 3 — useful, lower priority

13. **Vendor Contact List** and **Customer Contact List** — full detail, including any accounts you have not seen.
14. **Account List (chart of accounts)** — confirms every account and any that were made inactive.
15. **Recurring Transactions list** — shows standing automated entries.
16. **User list / Manage Users** screenshot — who currently has access and at what permission level.
17. **1099 Transaction Detail** for 2024 and 2025 — contractor payments as reported.
18. **A fresh Audit Log export** covering Aug 24, 2026 to today — closes the gap after your last pull.

---

## What you will not find in QuickBooks

- **2026 operating data.** The books moved to Finaloop in January 2026; QuickBooks is a partial shell for that year. Everything 2026 has to come from Finaloop, and Finaloop has **no user-level audit trail at all** — no user, actor, or author field anywhere in its export. That gap is permanent and is why the migration workpapers are in the records request.
- **KeHE product mix for 2026** — same reason. Finaloop records sales by channel, not SKU.
- **Payroll detail by person before April 2026** — Gusto posts as aggregate journal entries.

---

## A note on what this is and isn't

Exporting records you have been given access to, as a member exercising inspection rights, is ordinary and defensible. Copying, altering, or deleting anything is not. Keep the line bright: **read, export, screenshot — nothing else.** Save everything with its original filename and the date you pulled it, and do not edit the files themselves; work on copies.
