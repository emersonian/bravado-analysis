# Bravado Spice — QuickBooks Audit-Log Forensics

**Prepared:** August 25, 2026
**Source:** 18 QuickBooks audit-log exports in `Financials/Quickbooks/` — 143,199 raw events (116,554 after deduplication; the "Other" file overlaps 2025–2026), continuous coverage Jan 1 2020 → Aug 24 2026 by change date. Companion to `ANALYSIS - Claims vs Books.md`.

Method: every event was parsed (timestamp, user, action, document type, dollar amount where present) and analyzed for deletions/voids, journal-entry activity, user/access changes, chart-of-accounts changes, and clustering around investor milestones (Oct 2 2024 pitch, Nov 26 2024 Comatri signing, Jul 22 2026 meeting, Aug 24 2026 briefing).

---

## 1. Findings that corroborate the misrepresentation case

### 1.1 The $69,033 wage accrual was deliberate, CFO-reviewed — and then left out of the investor deck

- **Feb 26, 2026** — Strata Cloud Accountants *added* Journal Entry **AJE-547** ("Accrue Unpaid Wages Due to Jeremiah," $69,033, dated 12/31/2025) and edited it the same morning.
- **Mar 31 and Apr 8, 2026** — **Mark Clark** (the fractional CFO, himself an investor) edited AJE-547 three times.
- **Jul 19, 2026, 2:30–3:35 pm** — Jeremiah signed into QuickBooks (his only session between mid-May and the meeting), three days before presenting the July 22 deck. The deck's 2024 figures match QuickBooks to the dollar; its 2025 figures match QuickBooks *minus exactly this entry*.

So the accrual was not an obscure bookkeeping artifact: it was created and revised over six weeks by the accountants and the CFO, and the books containing it were open on Jer's screen the week of the meeting. The deck presented 2025 without it.

### 1.2 The business-partner timeline in the narrative doesn't match the books

The July 2026 deck's arc says: *"2024: The year the wheels came off. My business partner's health crisis surfaced hidden, unvetted contracts… I had to ask him to step down."*

The audit log: **James Nelson's last activity in QuickBooks is September 2023**, and **Jeremiah inactivated his user on October 13, 2023** (alongside Vince Blasco, the sales lead). The CPA's member-equity restructure creating "Member Equity - Nelson" followed in April 2024. A $16,500 deposit from Nelson was booked September 2023 (visible in the 2023 P&L as September other income).

The separation was underway by fall 2023 — which places the company's worst year, **2023 (net loss $564,654, omitted entirely from the "three-year arc")**, at the end of the partnership period, and means the narrative shifted the partner rupture a year later, onto the year the arc begins.

### 1.3 The 2025 cash context the investor documents never assemble

From the ledgers and audit log together, calendar 2025 received roughly **$480K of non-operating cash**:

- SBA disaster loan disbursements: **$25,000 (Dec 27 2024) + $226,200 (Jan 3 2025) + $100,000 (Jul 26 2025) = $351,300** ("SBAD TREAS 310" deposits in the GL);
- ERC / U.S. Treasury refunds totaling **$156,642** booked to 2025 other income (deposits of $10,196, $7,053, $7,329, $62,268, $14,443, and others logged Jan–Dec 2025).

Despite ~$480K of borrowings and refunds landing in a single year, 2025 ended with **$3,146** in the bank — while (per the GL analysis in the companion report) **~$93K net moved to Jeremiah or his personal creditors** during that same year. The July deck says the ERC "went to debt, inventory, and survival."

---

## 2. Patterns worth knowing about (ambiguous — not provable fraud from the log alone)

### 2.1 Heavy founder-level deletion activity, mostly explainable as cleanup

Jeremiah personally deleted **133 transactions in 2024 (gross $596K)** and 51 in 2025 ($116K). On inspection the bulk is:

- **Duplicate AR from integration syncs**: runs of identical-amount invoices (five × $26,586 and seven × $10,634.40 "for ULINE" — a *vendor*, not a customer — plus Link Logistics, etc., invoice numbers 9578–9793) deleted Jan–Apr 2024. These look like Katana/Faire sync artifacts; deleting them *reduced* recorded revenue, the opposite of inflation.
- **KeHE remittance reconciliation, Sep–Oct 2024**: on Sep 3–5, 2024 he deleted ~$97K of KeHE invoices (largest: No. 2631832 at $44,392), then **recreated the major ones at lower amounts** — 2631832 → $31,990 (Oct 31), 2612072 → $13,685 → $11,644, 2559438 → $10,593 → $7,899. Net effect ≈ −$17K of revenue/AR, consistent with absorbing KeHE chargebacks, and again *against* his own interest in the books. This happened in the weeks around the Oct 2 pitch to Blake, i.e., the AR was being trued *down* right before showing the financials.

### 2.2 Vendor-bill deletions in mid-2025, including creditors later shown on the debt schedule

Jul 7 – Aug 25, 2025, Jeremiah deleted: SBG bills of $10,412, $6,929, $5,401 (plus $14,479 in March); John Henry's PO bills totaling ~$11.4K; six Unishippers bills totaling $2,706; a Berlin Packaging bill of $1,022; later an HTS Texas invoice ($3,000, Nov 2025) and a **$2,500 bill to Mark Clark** (Sep 18, 2025, along with its attachment "Bravado Invoice 40901.doc"). Deleting bills removes recorded liabilities. Plausible innocent reading: duplicates of PO-tracked obligations (SBG debt continued to be acknowledged in investor docs). The Unishippers deletions are consistent with the disclosed "disputed for cause" position. Not resolvable to intent from the log — but this is the mechanism by which QuickBooks A/P could drift below true payables.

### 2.3 Deleted supporting documents

Attachments deleted in fall 2025: "Unishippers - The Shipping Company That Works For You.pdf" (Aug 19), "Bravado.pdf" (Sep 19), "48841 supporting.pdf" (Oct 2), "Invoice_50209_from_Western_Crating.pdf" (Dec 8). Small in number, but deleting source documents for disputed/derecognized liabilities is a records-hygiene red flag.

### 2.4 Family repaid while trade creditors stretched

The Nguyens received loan repayments in 2025 (balance $100,000 → $88,767, including a $4,707 payment Jer entered and paid on Aug 30, 2025), and Mark Clark's $5,000 loan went to zero — while SBG, rent, Uline, and Berlin Packaging went past due into 2026. Balances disclosed to investors are accurate; the *ordering* of who got paid is the notable fact. (Blake Benthall's personal $7,500 bridge loan — repayable as $8,500 within one month, per Blake — was never booked on either balance sheet and could not have been "scheduled" by the books at all.)

---

## 3. Exculpatory findings (fairness requires stating these)

1. **Jer gave Blake direct books access early.** On **Jan 27, 2025, 6:36–6:41 pm** he cleaned up stale users (inactivated Ryan Harcourt, John Tallerine) and **added user "Blake Benthal"** — four minutes before emailing Blake the 2025 budget. Blake's sign-ins on Aug 24, 2026 (pulling these very exports) confirm access was never revoked. Someone systematically cooking QuickBooks does not usually hand an investor a live login 18 months in advance.
2. **No retroactive tampering before investor reports.** The Aug 24 briefing's "plan" column reproduces the locked July file exactly; there is no burst of edits to closed periods before the Oct 2024, Jul 2026, or Aug 2026 communications; QuickBooks was essentially dormant (sign-ins only) from April 2026 on.
3. **Professionals did the sensitive accounting.** The Nguyen/Clark debt-to-equity restructure (Apr 2024) was performed by William S. Annon, CPA; the wage accruals and reclasses (AJE-345/387/388/547) were entered by Strata Cloud Accountants; the same CPA was signing in through Jul 21, 2026. The $200,000 Nguyen deposit (Jan 2024) and both Comatri deposits ($15,010 Jul–Aug 2024, booked to equity under the bank feed's mislabel "Coinbase"; $35,000 Nov 2024) were booked by the accountants.
4. **Journal-entry deletions are routine.** The 57 deleted JEs are overwhelmingly accountant reversal-pair cycles (AJE-…R patterns) and Gusto re-syncs, spread across all years and mostly not performed by Jer.
5. **The revenue-side deletions cut against him.** As noted in §2.1, the large 2024 deletions lowered recorded revenue/AR to match reality. There is no instance in the log of revenue being conjured or liabilities of record being silently shrunk *immediately before* an investor communication.

---

## 4. Bottom line

The audit log does **not** show classic books-cooking (backdated revenue, pre-report edit bursts, reconciliation manipulation). What it does show, powerfully, is that **the numbers withheld from investors were known, deliberate, and professionally reviewed**: the $69,033 wage accrual was a six-week, CFO-edited process completed in April 2026, and Jer was in QuickBooks days before presenting 2025 figures that exclude it. It also shows the partner-departure story was moved forward a year, burying 2023 — the worst year in company history — outside the narrative window. The dishonesty documented in the companion report lives in the *presentation layer* (decks and briefings), not in fabricated ledger entries; the audit log is what proves the gap between the two was knowing rather than sloppy.

Items worth asking about directly: the deleted SBG/John Henry's/Unishippers bills and their attachments (§2.2–2.3), the deleted $2,500 Mark Clark bill, and why the $7,500 Benthall loan was never booked.
