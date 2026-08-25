# Bravado Spice — Continuity-Memo Review & New Verified Findings

**Prepared:** August 25, 2026
**Purpose:** Cross-check of the ChatGPT master continuity memo (`Bravado_Comatri_Master_Research_Continuity_20260824.md`) against this repository's primary records, plus new findings from the leads it flagged as unanalyzed. Companion to the three prior ANALYSIS files. Where this file and the earlier ones differ, this one is the more current calibration.

---

## 1. Verdict on the other agent's memo

The memo is well-calibrated and its guardrails are sound. Repo evidence **confirms** its major leads (§2 below), **sharpens** several into findings, and **corrects** nothing material. Two calibration notes flow back onto my own earlier reports:

- **Owner-balance netting (errata to `ANALYSIS - Claims vs Books.md` §3.3–3.4).** The Finaloop $157,115.47 opening adjustment equals $88,082.47 + $69,033.00 exactly, so the $69,033 wage accrual may be counted in *both* the owner receivable and payroll payable. Depending on whether that is deliberate migration logic or a double-count, the net founder position at mid-2026 ranges from **Jer owes the company ~$50K** to **the company owes Jer ~$8–19K net**. Either endpoint remains far from the "~$101K net owed to Jer" that (per the memo) the longer July document claimed by netting only the $75,440 "Due from Jer" and ignoring the $88,082 overdrawn account and $5,331 draws. The core finding survives at both endpoints: the sacrifice narrative omits roughly $93K of owner debit balances. (Note: the longer 8-page July document quoted in the memo is **not in this repo** — only v4 is. Obtain it; its "$75K I have drawn" sentence is a directly testable representation.)
- **The "$107" claim (errata/refinement to §3.5 of the first report).** New provenance found: the August workbook's Assumptions sheet says "RE-BASELINED: **Found Primary $232.64 as of Jul 11**... (Was **$96.32 Jul 7**...)" — so $107-ish figures existed as a *Found "Primary pocket"* or unreconciled-feed balance. But the same August workbook's `Timeline!C2` sets **Starting Bank (Jul 7) = $2,379.30**, annotated "Reconciled to Found Bank on Aug 20," matching the Finaloop ledger (~$2,304–2,380). So: plausibly an honest pocket-view error in July — **but management's own August model corrected it by a factor of ~22×, and no correction of the dramatic "$107" anchor was ever communicated to investors.** The fair statement is "materially false when made, known-corrected by Aug 20, never retracted."

---

## 2. New findings verified against the repo (this session)

### 2.1 The "tempered assumptions" claim is contradicted by the model's own assumptions sheet — both months, both workbooks

The July 22 deck told investors: *"November–December: Holiday season on tempered assumptions."* The cash-plan workbooks' Assumptions sheet records the tempering decision explicitly:

> "Amazon Growth C **TEMPERED 7/11: Nov/Dec now ~$8–11K** (2–3x verified baseline) **instead of $20K/$23.6K** (6x)."

Yet the operative ROLLUP forecasts — which produce the year-end cash figures shown to investors — use the **untempered** numbers in both files: July plan Amazon Nov **$21,090** / Dec **$23,602**; August revision Nov **$21,952.50** / Dec **$24,597**. The August briefing's raised $40,018 year-end forecast (headlined "IMPROVING") therefore rests on Amazon holiday numbers the model's own notes say were rejected on July 11. Substituting the stated $8–11K assumption removes roughly **$27K** of the year-end cash. This is the cleanest known-at-the-time contradiction found so far: the tempering language went to investors; the untempered numbers went into the forecast.

### 2.2 The $10K family loan sits inside the Wholesale sales data (memo §20.1 — confirmed, with one exoneration)

`Daily_Sales` row for Jul 28, 2026: **Wholesale Actual = $10,000**, note "Anthony (Dad) loan $10K wire from Veronica M Tallerine," followed by compensating entries (+$9,983 forecast, −$10,000 forecast, −$1,216.85 actual) over the next two days. Summing the workbook's actual columns for Jul 22–Aug 20 gives Wholesale $10,949.67 — i.e., loan included. **However**, the August *briefing* de-contaminated this correctly: it shows Wholesale direct $950, operating receipts $18,664, and the $10,000 as a separate financing line. So this is model-hygiene risk (any future channel analytics from this sheet will overstate wholesale), not investor-facing misstatement — the memo's framing is right.

### 2.3 The October 2024 "open POs" statement is now affirmatively corroborated (memo §8 — resolved)

From the previously unanalyzed `Invoices and Received Payments.xlsx` (19,279 transaction rows, 677 customers): invoicing ran **Sep 2024 $69,878** and **Oct 2024 $77,810** — the two best months of the year, dominated by KeHE ($25.9K + $44.8K, the rebooked chargeback-corrected invoices). Product for orders in hand at Oct 2 really was being produced, shipped, and invoiced, and the SBG 5% factoring fee is documented in the GL (bill BSC177). **The Q4 miss came from new order flow dying afterward** — Nov invoiced $29,219, Dec $19,487, against a $420K Q4 budget. The dishonesty exposure in the Comatri window stays where the earlier analysis put it: the stale August actuals, the AJE-229 write-off inside the June "turnaround" month, and the unamended forecast at signing — not the PO statement.

### 2.4 Hot Shots: the "historical $10–12K" basis is genuine (memo §17.3/§31.1 — partially resolved)

The invoices export shows a 10-year Hot Shots Distribution relationship with remarkably steady orders: $10.6K–$13.9K per order through 2021–2025, including 2025 orders of $12,941 (Feb), $12,957 (Jun), and $13,411 (Sep 8, 2025). Finaloop 2026 shows ~$10K of Distribution sales in H1 2026. So the August "probable $11,000 (historical $10–12K)" was well-founded, and a Sep 2026 reorder fits their cadence. The remaining question is narrower and still worth asking: what specifically justified the word **"confirmed Sep 15"** on July 22 that had degraded to "probable" by Aug 24. The customer is real and the amount plausible; only the certainty claim is at issue.

### 2.5 Third independent confirmation of the 2023 partner exit (strengthens Audit-Log Forensics §1.2)

GL account "Due from James": journal entry **AJE-173, dated 7/21/2023 — "to close member equity and draw upon member exit"** ($25,081.27), plus the Sep 2023 Ford Explorer exchange JE and the Dec 2023 transfer that brings the receivable to $56,072. Together with James Nelson's QB activity ending Sep 2023 and his user being inactivated Oct 13, 2023, the books now show the member exit was **executed in July 2023**. The July 2026 narrative places the partner rupture in 2024. The memo's caution ("do not assume identity without confirming") is now satisfiable: the GL member-exit entries are in James Nelson's name.

### 2.6 Mark Clark: full money map, including an undisclosed $25,000 payable (memo §25 — confirmed and quantified)

From the GL and Finaloop opening balances:

| Item | Amount |
|---|---|
| Professional fees paid: 2022 / 2023 / 2024 / 2025 | $7,500 / $25,000 / $30,000 / $20,000 (≈ $82.5K total) |
| Loans to company: 2023 $14,000; 2024 $5,000; repaid $5,000 in 2025 | net $0 outstanding loan |
| Equity: Member Equity – Clark $39,000 (incl. $29K debt-to-equity, Apr 2024) | 500 shares |
| **Finaloop opening A/P at 12/31/2025: "Mark Clark — Other professional services"** | **$25,000** |

Neither the July nor the August investor debt presentation names a $25K payable to Mark Clark (it can only be hiding inside the unnamed "trade A/P $29,919"), while a $344 Uline balance gets its own row. Combined with his role editing AJE-547 and preparing budgets, Clark is simultaneously member, paid consultant (~$20–30K/yr), creditor, and accounting participant — exactly the multi-hat conflict the memo flags. Also noted: a Feb 2025 $2,500 payment booked to *Jer's Draw* with the memo text "Is this payment to Mark Clark?//Un…" — the books themselves weren't sure who received it.

### 2.7 Marisa Whitenton: compensated role predates 2026 (memo §26/§1.5 — confirmed)

GL: 1099 payments 2020–2022 (small), **2024 W-2 wages $5,174.71** plus $2,500 via Amex, **2025 1099 compensation $8,800** (the ~$800/mo pattern) plus expense reimbursements. Her 2026 operational involvement was a continuation of a real paid role, per the memo's correction — a governance/related-party question, not an anomaly.

### 2.8 Unishippers: books carry more than the "documented amount"

Finaloop opening A/P includes **Unishippers $20,705.34** at 12/31/2025, while investor docs recognize only the "documented" **$14,174** (and QB audit logs show Jer deleted six Unishippers bills totaling $2,706 in Jul 2025 plus the vendor's PDF attachment). The company's own ledger concedes ~$6.5K more than investors were told is acknowledged. Also confirmed in the same itemization: Endorphin $89,297.61 (matches disclosure exactly) and Western Crating (landlord) $11,650, consistent with the $16,475 past-due-rent figure.

### 2.9 KeHE 3773648 got a third value inside the August workbook

The workbook's own milestone note (Aug 4): "KeHE PO 3773648 net cash **$8,494** = $10,601 gross − $2,212 chargebacks," and its assumptions call the $8,389 "CONFIRMED." Actual collected: **$4,736.72**. So the July $9,573 → pack "original" $8,389 → workbook $8,494 → actual $4,737 progression shows KeHE deduction risk was chronically understated even in the internal model, right up to collection.

### 2.10 Items checked and neutral

The Aug workbook's Audit_Log contains no entries dating the SBG decline or the Anthony-loan decision (it still carries stale July-era SBG production milestones — confirming the memo's §20.4 version-control point), so the "no new borrowing → $10K loan six days later" chronology still needs correspondence to resolve. No usable S-election evidence exists anywhere in the repo (keyword hits are invoice-number noise) — Form 2553/K-1s remain an external demand. The two identical −$6,033.40 Apr 7 owner-receivable adjustments cannot be resolved as duplicate-vs-deliberate from the export.

---

## 3. Where to dig deeper

### A. Requires documents from Bravado (ordered by expected yield)

1. **The December 2025 Finaloop management report and QB→Finaloop migration workpapers** — resolves in one stroke: the $69,033 exclusion basis, the $157,115.47 owner-receivable construction, and the $736K-vs-$891K liability bridge. This is the keystone document.
2. **The longer 8-page July 2026 "State of the Business"** (not in this repo) — contains the "$176,914 absorbs the $75K I have drawn" sentence, the "$736K/AP $150K" table, and the "every number is real" representation; each is directly testable against balances already established here.
3. **Form 2553, consents, CP261, 1120-S returns and all K-1s** — the Comatri-vs-S-election question is unanswerable from the books; also determines whether Comatri's interest was reported to the IRS at all (the Finaloop "Capital – Blake Benthall" naming heightens this).
4. **Hot Shots and SBG correspondence, July 10–28, 2026** — the two dated-knowledge questions: what made Hot Shots "confirmed" on Jul 22, and when SBG's decline made new borrowing necessary relative to the "no new borrowing" statement.
5. **Katana sales orders / POs / outsourced POs, 2024–present** — closes the remaining gap between "invoiced" (now verified) and "orders in hand" for both Oct 2024 and the 2026 KeHE placeholder POs.
6. **Found bank statements (all pockets) for Jul 2026** and founder personal-card statements behind the $27,640 of 2026 owner reimbursements — converts the reimbursement/distribution findings from ledger-level to source-level.
7. **Written creditor arrangements** claimed in the Aug briefing ("every creditor is now on a written, scheduled arrangement") — at minimum Nguyen and Blake rows contradict this on the briefing's own face ("deferral requested"), and the Anthony/Endorphin/SBG writings would test the rest.
8. **The May 1, 2026 $4,600 deposit** credited to "Capital – Blake Benthall" — Blake should check Comatri's own records first: if Comatri didn't send it, someone else's money was credited to Blake's capital account, which is a concrete books error with cap-table consequences.

### B. Extractable from this repo with more work (lower priority)

- Full KeHE invoice→remittance→chargeback mapping from the invoices export (would quantify historical KeHE deduction rates and show whether ~45% collection on 3773648 was foreseeable).
- A month-by-month reconstruction of the 2025 "Due to Jeremiah" gross flows (gross draws vs. reimbursement credits) to present the founder-cash story to a decimal.
- Cross-referencing the ~$596K of 2024 deleted transactions against re-created replacements to certify the "duplicate cleanup" reading item-by-item.

### C. Questions answered — no further digging needed

October 2024 PO fulfillment (§2.3), Hot Shots order history (§2.4), the 5% factoring fee, the partner-exit date (§2.5), the 59.4%/74% margin math (three independent reconstructions now agree), the Aug briefing's plan-column integrity, and the provenance of the "$107" figure (§1).
