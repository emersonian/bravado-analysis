# Bravado Spice — The Comatri Investment Window (Oct 2 – Nov 26, 2024)

**Prepared:** August 25, 2026
**Question:** In the materials Comatri received before signing the Nov 26, 2024 investment agreement ($35,000 for 700 shares), was anything misrepresented — about purchase orders or otherwise?
**Sources:** the Oct 2, 2024 email + four attachments in `Jer to Investors/2024-10-02 - To Blake Only/`, the signed agreement in `Comatri Investment Agreements/`, QuickBooks P&L/GL/audit logs. Companion to the two prior ANALYSIS files.

**Short answer:** The historical numbers and the purchase-order/factoring claims were essentially true. What was misrepresented is the *trajectory*: the workbook was six weeks stale when sent — August's collapse to $34K (half the number shown) was already in the books — the "turnaround" month anchoring the margin-correction story was inflated by a one-time $23K write-off taken on Jer's own say-so, and by the day Comatri signed, the Q4 plan underpinning the whole package was visibly failing with no correction on record.

---

## 1. What the email claimed, line by line

The Oct 2, 2024 email ("Bravado's Fin Docs") made these representations:

| # | Claim | Books | Verdict |
|---|---|---|---|
| 1 | 2024 Budget "has actuals to date and projections" | Actuals stop at **June**. See §2. | **Misleading** — "to date" was Oct 2; Jul/Aug actuals existed and were far below the sheet |
| 2 | "2025 Budget and conservative sales projections" | Forecast $1,495,000 at 42% GM; actual 2025: $464,997 at 32.4% | **Not conservative** by any measure; see §4 |
| 3 | Income-statement comparison "historical healthy margin, margin fall off, margin correction" | 2022–2023 history accurate; the 2024 "correction" leaned on a one-time write-off. See §3 | **Half true** |
| 6 | "All product for open POs are being produced and shipped with a 5% factoring fee from our co-packer" | October shipments were the year's best month ($98,753); the SBG 5% factor fee is real (GL bill BSC177, 12/01/2024, "5% Factor Fee," $7,532.56) | **Substantially true** (near-term) |
| 7 | "Potential SBA disaster loan for 65k–100k in the works"; ERC "to pay out this month or november" | SBA was real: $25,000 landed Dec 27, 2024 (then $226,200 Jan 3, 2025 and $100,000 Jul 26, 2025 — $351K total, 3.5× the range floated). ERC first paid **Jan 31, 2025** ($10,196 + $7,053), bulk May–Jun 2025 | SBA: **true, understated in size**. ERC timing: optimistic, framed as "potential" |
| 8 | "Current balances: Checking $(8,000), Savings $4,400, Total $(3,600)" | GL running balances at Oct 2: checking **−$7,302.72**, savings **$4,440.58** | **Accurate** — and candidly bleak |

The purchase-order claim specifically — the thing you asked about — holds up: the KeHE invoices in flight at the time (rebooked Oct 8 at $13,078 and Oct 31 at $31,990 after chargeback true-downs) correspond to product that did ship, and October 2024 was the biggest revenue month of the year. There is no sign of fictitious POs.

## 2. The stale workbook: August's collapse was known and not shown

The 2024 budget worksheet is labeled "**Actual**" for Jan–Jun and "**Budget**" for Jul–Dec, built around a Sept 1 investment assumption. The Jan–Jun actual sales match QuickBooks **to the dollar** ($451,261 H1) — the history was honest. But:

| Month | Shown in workbook | QuickBooks actual | Known by Oct 2? |
|---|---|---|---|
| Jul 2024 | $68,888 (budget) | **$62,030** | Yes — closed |
| Aug 2024 | $70,000 (budget) | **$34,126** | Yes — closed (the audit log shows August transactions being processed in real time, e.g. the KeHE invoice work on Aug 20) |
| Sep 2024 | $70,000 (budget) | $80,969 | Substantially |

August was the worst month since the 2023 collapse — **less than half** the figure in the sheet — and the email presented the package as containing "actuals to date" without flagging it. September's beat ($80,969) doesn't cure this: a reader of the workbook believed the company was tracking a $1,080,150 year; the July+August shortfall alone (−$42.7K vs. the sheet) said otherwise, and Jer had those numbers.

## 3. The "margin correction" month was inflated by a one-time write-off

June 2024 is the pivot of the pitch narrative: 51.4% gross margin and the only positive "Cash from Operations" month (+$26,026) in the actuals — proof the correction was working. The GL shows journal entry **AJE-229, dated 6/30/2024: "To write off the balance — per Jer this is not payable," $23,217.12** of income (the disputed Credit Card 9532 balance, $29,283 at Dec 2023, zeroed during 2024).

- QuickBooks classifies this as **Other Income**, below operating income (QB June operating income was −$9,484).
- The pitch worksheet instead nets it into SG&A as "Miscellaneous **(23,152)**" — inside operations — which is what turns June's operating cash positive.

So the one "proof point" month shown to Comatri was operating-positive only because a one-time, self-declared liability write-off was presented as an operating item. Without it, June was roughly break-even (+$2.9K) at best. (A similar $2,167 write-off was booked in July and reversed in August — AJE-253/AJE-270.)

## 4. By the signing date, the plan was visibly failing — and the record shows no correction

Comatri signed **Nov 26, 2024** (sent for signature Nov 20). By then the books showed:

| Month | Workbook budget | Actual | Status at Nov 26 |
|---|---|---|---|
| Oct 2024 | $120,000 | $98,753 | Closed — 18% miss |
| Nov 2024 | $150,000 | $43,206 | 26 days in — tracking at ~29% of budget |
| Dec 2024 | $150,000 | $35,399 | (came in at 24% of budget) |

Q4 delivered **$177,358 against a $420,000 budget**; the year closed at **$805,744 against the $1,080,150** shown in the pitch. The 2025 "conservative" forecast ($1.495M, 42% GM, +$136K operating cash) was built on that Q4 run-rate, which had already broken before the ink dried. This repository contains **no communication between Oct 2 and the Nov 26 signing** updating these numbers (caveat: an update could exist outside this repo — worth checking your own records). December then closed with a −$21,169 gross-profit month (year-end inventory write-offs) and a −$56,916 net loss.

## 5. The agreement's own representations

- **§2(d): "The Company is current in all tax filings and there are no outstanding assessments or other liabilities."** At signing, the books carried ~**$699K of liabilities** (Dec 2024: $243,571 A/P, much of it past due — the company paid $9,168 of late-penalty fees in 2024 — plus $163K of loans/LOC, $98K credit cards, $107,881 accrued wages to Jer). On a plain reading, the "no other liabilities" representation was false; even on the narrow tax-only reading it is unverifiable from this repo (a Texas Comptroller payable appears in 2025).
- **§2(b): "all approvals have been acquired to proceed"** — the attached Operating Agreement §1.9 requires **prior unanimous written consent of the Members** to admit a new member. No Nguyen/Clark consent documents exist in this repo. A question to ask, not a finding.
- **§2(c): no legal action pending** — nothing in the books contradicts it; the Unishippers/Leviton dispute surfaces later (2025).
- The agreement's records-access clause (§1a) is what entitles Comatri to everything analyzed here.

## 6. What was honest — for fairness

- Jan–Jun 2024 actuals: exact to QuickBooks. 2023 history in the trend sheet: exact ($1,754,718.90 total income; GM $515,917). The disastrous 2023 (−$582K cash from ops) and 2022's negative ops were **openly shown** in the Oct 2024 package — notably more candid than the July 2026 deck, which starts its "arc" at 2024.
- The negative bank balance was volunteered, accurately.
- The 5% co-packer factoring arrangement was real, and open POs did ship (October was the year's best month).
- The SBA loan materialized as promised (bigger than floated — more cash, but also more debt than Comatri was told to expect: $351,300 vs. "65k–100k").

## 7. Bottom line

Nothing about **purchase orders** was misrepresented — orders existed, shipped, and the factoring fee was real. The misrepresentation in the Comatri window is subtler and chronological: **a package whose history was accurate but whose present was six weeks old and materially worse than shown (August = $34K vs. $70K displayed), whose turnaround proof-month rested on an undisclosed one-time $23K write-off taken "per Jer," and whose Q4 plan — the basis of the "conservative" 2025 forecast — was already missing by 70%+ when the agreement was signed, with no correction communicated in this record.** Combined with the §2(d) representation about liabilities, the picture at signing was materially rosier than the books Jer was looking at.
