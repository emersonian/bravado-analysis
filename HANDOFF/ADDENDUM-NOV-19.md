# Addendum: discoveries and events of November 18–19, 2026

This file records what was learned after the handoff package was assembled. It supplements `START-HERE.md` and the review memo. Same standing rules apply (no characterization of conduct; "document A shows X; document B shows Y").

## 1. Events

- **Nov 18, 2026 meeting.** Hugh Nguyen met Jeremiah Tallerine and Mark Clark. Blake Benthall / Comatri was not present or invited. Hugh handed over a questionnaire (16 items) and "the financial analysis."
- **Hugh's recap (Nov 19, emailed to all members).** No numbers or dates. Recorded commitments: Jer to estimate an in-house production kitchen; Jer to propose a repayment plan for the Nguyen note; Jer "confirmed" the Tallerine family loan "was forgiven" and should be removed from reporting; James Nelson's balance and "associated credit card charges" to be "removed from future reporting where appropriate"; Mark to "review and reconcile" the amount due from Jer "including any necessary reclassifications"; Comatri investment "mislabeled as Coinbase" to be relabelled Comatri, Inc.; Mark to prepare "Version 2" of the 2026 P&L and balance sheet; tax returns explained as cash basis vs accrual drafts; Mark to consult the outside accountant on the S-corporation termination date; Jer to address Blake's Finaloop access "directly with Blake"; Jer to produce a succession/continuity plan and a 2027 growth plan. Hugh reported that Jer said he "focused on bravado all the time, and he spent all of his time doing bravado stuff."
- **Blake's reply-all (Nov 19, 12:54 PM).** Ten numbered items: cash/13-week view; true balance due from Jer; 2026 payments and support for $31,312; Version 2 change list and preservation of ledgers; who is responsible for the books; tax status and Comatri (Finaloop shows "Capital - Blake Benthall" $54,610 incl. $4,600 not contributed; agreements effective Jul 22 and Nov 26, 2024; no K-1 ever; Comatri "not in a position to agree to any change in how its interest is held or dated"); restore Finaloop access; Jer's time and succession; why Comatri was excluded from the meeting; the 7,500 USDC. Proposed dates Nov 25 / Dec 4 / Dec 11.
- **Mark Clark's reply (Nov 19).** Key statements, quoted:
  - "I have not worked with the company for over a year so do not have all the answers. Going forward, I am happy to help out at no charge, but only to the extent it doesn't interfere with my regular work."
  - "QB was used to 12/31/25 with the services of Strata ... Finaloop thereafter." "THERE IS ONLY ONE SET OF BOOKS, CURRENTLY ON FINALOOP. QB TERMINATED AT 12/31/25."
  - "Through mid 2025, I reviewed financials monthly with Strata ... That hasn't happened since; hence the need for adjustments now. For what it's worth, the company owes me about $25k in unpaid fees currently included in payables."
  - "My DRAFT financials are based on a spreadsheet I kept through 2025 plus the numbers from Finaloop for 2026, unadjusted."
  - "Inventory at 9/30/26 is incorrect."
  - "The Due from James asset likely needs to be written off. Awaiting word from Jer's tax guy as to the best way to do that."
  - "The Due from Jeremiah asset needs to be viewed in conjunction with the Accrued Wages Jeremiah liability acct. As a practical matter they should be netted, but there are reasons to keep them separate for financial presentation."
  - "These statements include no expense for Jeremiah's compensation. That will need to be added to the Accrued Wages and to comp expense." And on the balance due from Jer: "I'LL PREPARE AN ANALYSIS ONCE I HAVE JER'S 2026 COMP ACCRUED."
  - "Retained earnings doesn't roll correctly. I need to research why."
  - "Interest needs to be accrued on the Nguyens note."
  - "Unallocated reimbursements represent reimbursement to Jer for company expenses he paid personally. This balance will be reclassified to appropriate expense line items once Jer provides me with a summary."
  - "Tax returns are prepared on a cash basis, books on accrual. They will not match."
  - "JER IS RESPONSIBLE [for the books] BUT I WILL HELP OUT TO THE EXTENT I CAN." "IT LOOKS TO ME LIKE THE COMATRI BALANCE IS $50,010."
  - No dates accepted. No response on bank balances, 13-week forecast, tax date, or outside CPA review.
- **Mark Clark's email to Blake, Aug 25, 2026:** "Blake, to clarify, i have not been the company's fractional CFO for quite some time. I am available to help Jer informally as needed but at this point my only relationship with the company is as an investor."
- **Jer had not responded** to any item as of this writing.
- **Blake engaged a lawyer on Nov 19, 2026** (not yet briefed). A draft overview for counsel is in the repo root.

## 2. Arithmetic of the proposed netting

Mark's draft, Sept 30, 2026: due from Jeremiah $208,100; accrued wages – Jeremiah $177,063. If 2026 compensation is accrued at the prior $75,000/yr rate for nine months (+$56,250; rate not stated by management), accrued wages become $233,313 and netting yields about **$25,200 owed by the company to Jer**. The nine-month loss would rise from $63,482 to about $119,700. Payroll (Gusto) stopped after the March 9–24, 2026 pay period; the July 2026 update planned "$5K/month" from September.

After the adjustments Mark lists (netting Jer, writing off James $56,369, correcting inventory $59,829), the draft's total assets of $329,016 fall to roughly $65,000 or less, against about $933,000 of liabilities before netting.

## 3. QuickBooks audit log: when the salary accruals were entered

All entries keyed by user "Strata Cloud Accountants" (outside accountants). Each batch is dated back to the month-ends it covers.

| Entered | Entries | Periods | Amount | Attachment added same day |
|---|---|---|---|---|
| Dec 14, 2023, 12:03–1:35 pm | AJE-76 … AJE-86 (11) | Jan–Nov 2023 | $68,750.22 | "CC Reimburstment Jer.xlsx" |
| May 23, 2024, 3:45–4:01 pm | AJE-202 … AJE-206 (5) | Jan–May 2024 | $25,000.08 | "2024 CC Reimburstment Jer.xlsx" |
| Jan 22, 2025, 3:55–4:51 pm | AJE-326 … AJE-333 (7) | May–Dec 2024 | $46,875.15 | "Part 2 - 2024 CC Reimburstment Jer.xlsx" |
| Feb 26, 2026, 8:20 am | AJE-547 (1) | all of 2025 | $69,033.00 | "Jer Wages Accrual - $69033.pdf" |

- Account "Wages Due to Jeremiah" was **created Feb 29, 2024, 1:10 pm**; all eleven 2023 entries were edited that same minute (their original credit account is not shown by the log).
- The same journal entries carry both business-expense reimbursements credited to "33500 Due to Jeremiah" and the "Skipped Paychecks" lines credited to "Wages Due to Jeremiah." Memos name specific Gusto pay periods (e.g., "Jan 9 - Jan 24 Gusto Skipped Paychecks - Jer"); rate is a constant $3,125.01 per half-month.
- AJE-547 was edited by Mark Clark on Mar 31 (2:12 pm) and Apr 8, 2026 (12:16, 12:19 pm). $69,033 is not a multiple of $3,125.01 (22 = $68,750.22; 24 = $75,000.24).
- Jer was signed in to QuickBooks on Dec 14, 2023, May 23, 2024 and Jan 22, 2025. Mark Clark was signed in May 23, 2024.
- Timing: first batch is 15 days before the Nguyens' $200,000 wire (Dec 29, 2023). Of the Jan 22, 2025 batch, $34,375 is dated before Comatri's Nov 26, 2024 agreement ($40,625 through Nov 30).
- Tax returns show "compensation of officers" of $10,039 (2023) and $3,694 (2024). Gusto ledger lines do not name employees.
- 2023–2025 totals: salary accrued about $209,658; cash to Jer not itemized $155,090; payments recorded against wages $37,992 ($35,644.29 in 28 transfers in 2024, plus one $2,347.34 item on Sep 18, 2024 whose bank memo names another employee's payroll). Corrected Nov 21: earlier text said $153,090 and $39,992, which counted AJE-345 ($2,000, 2025, a journal entry against accounts payable) as a payment.

## 4. The 2024 Comatri investment

- **Both agreements** (signed for the company by Jer; July 21/22, 2024 and Nov 26, 2024) contain §2: (a) duly registered Texas LLC; (b) "Pursuant to the Company's Operating Agreement, all approvals have been acquired to proceed with the issuance of this membership agreement"; (c) no legal action pending; (d) **"The Company is current in all tax filings and there are no outstanding assessments or other liabilities."** §4 Texas law. §5 entire agreement: "All negotiations and understandings have been included in this agreement and only the written terms of this agreement will bind the parties."
- Agreement 1: $15,000 for 3%, right to invest $35,000 more for 7% by Oct 2, 2024 "at this same valuation"; its Exhibit 2 lists Jer 72%, Nguyens 20%, Clark 5%, Comatri 3%. Agreement 2: $35,000 for 700 shares and "access to the Company's financial records from 11/20/2024 until either Jeremiah Tallerine is no longer a majority stack holder in the Company or in the event the Investor divests."
- **QuickBooks balance sheet (as it stands today):**

| | Jul 2024 | Nov 2024 |
|---|---|---|
| Total liabilities | $660,797 | $680,816 |
| Accounts payable | $198,812 | $254,626 |
| Credit cards | $99,352 | $98,721 |
| Loan from Nguyen | $100,000 | $100,000 |
| Tallerine LOC | $69,440 | $69,440 |
| Wages due to Jeremiah | $93,925 | $106,357 |
| Funding Circle / Forward Financing (Nov) | | $35,633 / $11,825 |
| Deferred Social Security tax ("34310") (Nov) | | $6,441 |
| Due from Jer + Due from James | $110,198 | $110,198 |
| Total equity | ($404,527) | ($462,055) |

- **Oct 2, 2024 email from Jer ("Bravado's Fin Docs")** attached a 2024 budget ("has actuals to date"), a 2025 budget ("conservative sales projections"), an income-statement trend, and two pricing sheets. No balance sheet. It disclosed: "This assumes $100k of funding from somewhere"; open POs shipping with a 5% factoring fee; "Potential SBA disaster loan for 65k-100k in the works"; bank balances checking $(8,000), savings $4,400. The income statements show interest expense ($64,336 for 2023).
- 2023 Form 1120-S preparer date Apr 23, 2024; 2024 Form 1120-S preparer date May 8, 2025.
- No large payment to Jer followed either Comatri deposit (about $5,100 and $8,400 to his accounts in the surrounding weeks).
- Nothing in the repository predates July 21, 2024 for Comatri; Blake's own messages with Jer from that period have not been collected.
- Blake reports (not documents): Comatri has never received a K-1; he was asked to retitle the interest into his own name; his Finaloop access was removed; he was given QuickBooks read access in January 2025.

## 5. Operating Agreement provisions relied on (adopted June 1, 2023)

1.9 admission of additional members requires prior unanimous written consent; 4.1 managers elected by members holding a majority of capital interests; Exhibit 1: managers serve "until they are removed for any reason by a majority vote of the Members"; 4.2 non-manager members take no part in management; 4.3 manager powers (borrowing, compromise of claims); 4.6 members may inspect and copy all books and records; 4.7 exculpation for acts "done in good faith to promote the best interests of the Company"; 4.8 indemnification; 4.9 records to be kept; 5.1 manager compensation "commensurate with the value of such services"; 5.2 reimbursement of "direct out-of-pocket expenses"; 6.1 managers maintain complete and accurate books; 6.3 annual statement to each member of distributive share; no amendment provision.

## 6. Other

- Blake's April 2026 loan: Jer's text Apr 29, 2026: "I have a lock on the next 300k from SBA but I need to bring my SBA account balance to zero. Would you consider a 7500 usdc transfer for a 8500 return in a month?" Sent to a Solana wallet supplied by Jer. Not recorded as a loan in Finaloop. $4,600 from a Capital One account on May 1, 2026 booked to "Capital - Blake Benthall" (link to the loan is inference).
- Miguel Vaquero (operations) moved off Gusto payroll in April 2026; paid by direct transfer since.
- Only draws/distributions since 2024 in either ledger: Jer's ($5,331 draws in 2025; $21,752 "Distributions - Jeremiah Tallerine" in 2026).
- QuickBooks contains 2026-dated entries through March 27, 2026; Strata logged 1,111 events in Jan 2026, 198 in Feb, 6 in March.

## 7. Written objection and reply (added after the multi-reviewer pass)

- **Comatri's objection, sent by Blake to the members (date sent: on or shortly after Nov 19, 2026; exact timestamp to be taken from his sent mail):** "For the record, Comatri does not agree to any compensation being accrued for Jer for 2026, or to any netting of accrued wages against the balance he owes the company, until the members have seen the basis for the rate and the periods, the payroll tax treatment, and have agreed to it in writing."
- **Mark Clark's reply (quoted by Blake):** "Not sure you understand. He has taken draws which are effectively his compensation. The accounting adjustment simply reclassifies those draws to what they are. When i have the amount i'll provide the analysis then we'll have a basis for discussion."

Points to carry forward (documents-only):
- The person preparing the statements now describes the cash taken as "effectively his compensation." The books recorded the same cash as amounts owed by the manager (a receivable), the 2025 Form 1120 reports $294,256 as "loans to shareholders," the returns show officer compensation of $10,039 (2023) and $3,694 (2024), and the July 2026 update says he "skipped my own paychecks."
- Mark's two emails describe two different adjustments. Nov 19 (first): "These statements include no expense for Jeremiah's compensation. That will need to be added to the Accrued Wages and to comp expense" and the balances "should be netted." Reply: the adjustment "simply reclassifies those draws to what they are." On Finaloop the 2026 payments ($49,192 through Jul 22) are already booked as distributions ($21,752) and reimbursements ($27,640), not added to the receivable. Reclassifying what was drawn leaves the manager owing roughly $31,000 on Mark's Sept 30 figures ($208,100 less $177,063); accruing nine months at $75,000 a year first and then netting produces about $25,200 owed to him. The difference is about $56,000. Which of the two is intended is not stated.
- The reply says the analysis will come first and then "we'll have a basis for discussion"; it does not say whether anything will be booked before members agree.

## Mark Clark's reply on netting (pasted by Blake Nov 21, 2026; exact send date and the email it answers to be confirmed)

Full text as pasted:

> The reason the due from Jer and accrued wages are not netted on the financials relates directly to your point. Most of the due to Jer balance are draws that i would prefer to have been run through payroll. A smaller amount is reimbursements for company expenses paid by Jer personally. Here is the accounting process.
>
> Draws: Debit Due from Jer / Credit Cash
> Compensation: Debit Comp expense / Credit Accrued wages
> Co expenses paid by Jer personally: Debit appropriate expense accts / Credit Due from Jer
> Reimbursement: Debit Due from Jer / Credit cash
>
> The last two should wash when all is current. By handling "comp" this way, the wages are recorded on an accrual basis for financial presentation, but not on a cash basis which would be the basis for payroll reporting.
>
> Again, i'd prefer the draws be run through payroll, but given they haven't, this accounting process has been discussed with the tax CPA.

What the document states: (1) the two balances are not netted on the financials; (2) most of the balance the manager owes is cash draws, with a smaller part reimbursements that "should wash"; (3) wages are accrued for presentation but not treated as paid for payroll reporting; (4) the process has been discussed with the tax CPA. ("due to Jer" in his second sentence reads as "due from Jer" in context.)

Not stated: whether a note, interest or repayment schedule exists for the balance; what the tax CPA concluded; whether any netting or reclassification is still planned for Version 2.
