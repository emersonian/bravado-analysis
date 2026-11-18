# fact-check

SUMMARY: Fact-check of "DRAFT - Reply to Hugh (Nov 18 meeting questions).txt" against the QuickBooks and Finaloop ledgers, the return and K-1 page images, Mark Clark's draft, both Comatri agreements, the July and August 2026 investor documents and the archived texts. The user's note that the loan was "7500 for 8500" matches the archived text and the draft.

The core reconciliations hold to the dollar: 294,256 = 237,886.89 + 56,368.76; 74,364 = 69,033 + 5,331; 62,919 = 131,952.09 - 69,033.09; the Nguyen note balances; 65.421% = 7,000/10,700; and every quotation tested. Payroll ending in March and no 2026 wage accrual both hold in Finaloop.

Fourteen assertions need rewording before the reply is sent (W01-W14), and W15 lists the statements that rest only on the member's recollection. The ones most likely to be challenged in the room:
- W01: the "$26,919 of transfers to his personal checking" includes a $3,250 check to a third party; transfers to account 5820 are $23,664.
- W02: the $52,422 is gross; $3,830 came back in from Capital One transfers booked as his capital, and the total reproduces at $52,416.55.
- W05: the 2024 accrual entries total $71,875.23, not $74,775, and "full-time" is not in the ledger.
- W07: the $22,112 itemized in 2025 is measured against $118,128 of total cash to him, not against the $44,384 of card payments.
- W08/W09: $77K/$50K/$48K are the Schedule M-1 "per books" lines (page-1 losses are $72,663 / $67,869 / $47,893); no copy shows filing; the 2025 accounting-method page is not in the PDF.
- W10: the K-1 "Changes in Ownership" page is marked "not filed with the return" and names no holder.
- W11: Mark's text itself already states the C-corp problem, so "said S corp" understates it.

C01-C10 are the ten assertions confirmed exactly. Scripts and rendered pages are in /tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/agents/factcheck/.

## W01 [high] VERDICT: -
Finaloop bank lines for Jan 1-Jul 22, 2026 show $23,664.22 transferred to Capital One personal checking 5820, not $26,919. The other $3,250 is check #7590 (Jan 27, 2026): QuickBooks records payee "Seth Beacher", memo "2D Deposit", Uncategorized Expense; Finaloop books it to "Distributions - Jeremiah Tallerine"; a $3,250 "CAPITAL ONE TRANSFER" came in on Jan 23, 2026.
CORRECTS: Draft Q3: "$26,919 of transfers to his personal checking". Same figure in ANALYSIS - Cash Paid to the Founder (Rebuilt).md, 2026 row, "Transfers to personal bank 26,919".
Q: What was check #7590 for $3,250 to Seth Beacher on January 27, 2026 (memo "2D Deposit"), and why is it booked as a distribution to Jeremiah?
HOW: finaloop_gl.csv, the four Checking/Savings accounts, dt < 2026-07-23. Description matching "Transfer to Capital One Personal Checking 5820" or starting "Transfer to 360 Checking": 36 lines, -23,689.22 (Chase 8733 -16,826.42; Found 1862 -6,855.30; Savings 3580 -7.50). One $25 transfer on 2026-07-02 is classified "Failed transfer" with a same-day $25 "FEE REVERSAL", leaving 23,664.22. Check 7590: qb_gl.csv num=7590, 2026-01-27, name Seth Beacher, memo "2D Deposit", -3,250; Finaloop "Distributions - Jeremiah Tallerine" -3,250 "CHECK # 7590". Inflow: Finaloop Chase 8733 +3,250 on 2026-01-23, booked to "Capital - Jeremiah Tallerine" (QuickBooks: 67000 Uncategorized Income). 23,664.22 + 3,250 = 26,914.22, $5 from the memo's 26,919.

## W02 [high] VERDICT: -
The $52,422 is a gross figure and reproduces from Finaloop at $52,416.55. Over the same period $3,830 came in from Capital One transfers that Finaloop booked to "Capital - Jeremiah Tallerine" ($3,250 Jan 23, $180 Jan 27, $400 Apr 23), so the net is about $48,587 (the prior memo's own net is $48,592).
CORRECTS: Draft Q3: "From the ledger, $52,422 went to him or his personal creditors from January 1 through July 22" (stated without saying it is gross, or that $3,830 came back in).
HOW: Gross = card payments 24,328.83 + transfers to 5820 23,664.22 + check 7590 3,250.00 + check 7588 250.00 + personal transactions charged to the owner account 923.50 = 52,416.55 (52,441.55 if the failed $25 transfer is counted). Inflows: Finaloop account "Capital - Jeremiah Tallerine", 2026 lines 3,250 + 180 + 400 = 3,830. 52,416.55 - 3,830 = 48,586.55. Difference from 52,422 is $5.45, not tied.

## W03 [medium] VERDICT: -
The $24,329 reproduces ($24,328.83): Capital One card payments $22,959.89 (10), Citi $980.42 (4), Petal $388.52 (3). The ledger descriptors do not identify which card was paid; the "personal" label rests on the books charging them to owner accounts. The company's own Capital One Spark card 4964 was paid under the same descriptors until Mar 3, 2025 and was closed in QuickBooks on Jun 30, 2025.
CORRECTS: Draft Q3: "$24,329 of personal credit-card bills" (amount confirmed; the ledger alone does not show the cards are personal).
Q: Which Capital One, Citi and Petal card accounts received the $24,329 paid from company accounts between January and July 2026, and will the statements be provided?
HOW: finaloop_gl.csv bank accounts, dt < 2026-07-23: Description matching "CAPITAL ONE ... ONLINE PMT|MOBILE PMT" = -22,959.89; "CITI CARD|CITI AUTOPAY" = -980.42; "Petal Card" = -388.52. Finaloop classification: 18,759.89 + 388.52 in "Reimbursements to owners", 4,200 in "Distributions - Jeremiah Tallerine", Citi 955.42 in "Unidentified payouts & transfers" and 25 in "Miscellaneous expenses". QuickBooks booked the three January 2026 Capital One payments (1,900; 2,528; 971) to 33500 Due to Jeremiah. Spark card: qb_gl.csv account "32400 Spark Business Credit Card - 4964", payments with CAPITAL ONE ORIG ID ...4391/...4380 through 2025-03-03; journal entry 2025-06-30 "Closing this in book since it is not in portal anymore since March".

## W04 [high] VERDICT: -
The "about $1,200" is $1,173.50: $923.50 of personal transactions charged to his owner account in Finaloop (17 lines, of which $441.26 is healthcare, $300 a Chase card payment and $46.13 OneMain Financial) plus $250 check #7588 to Finnacle Managing Co LLC, memo "Tallerine/ Whitenton Lease App". Neither ledger says the lease application was in New York, and the company books the $250 as an expense (QuickBooks: Office Expenses; Finaloop: Other operations expenses).
CORRECTS: Draft Q3: "about $1,200 of personal charges and a New York lease-application check".
HOW: finaloop_gl.csv, account "Due to/from owner - non-interest balance - Jeremiah Tallerine", Source starting "Personal transaction", dt < 2026-07-23: 17 lines, 923.50. Check 7588: qb_gl.csv num=7588, 2026-01-14, -250, split "73200 Overhead Expenses (G&A):Office Expenses".

## W05 [high] VERDICT: -
The 2024 "skipped paycheck" accrual entries total $71,875.23 (23 paychecks of $3,125.01), not $74,775. The $74,774.77 figure is all 2024 credits to "Wages Due to Jeremiah" and includes $2,899.54 of Gusto pay-run lines dated Oct 28, 2024. The ledger shows a $3,125.01 semi-monthly rate ($75,000.24 a year) and never uses the term "full-time"; 2023 is 22 paychecks ($68,750.22, none for December) and 2025 is a single Dec 31 entry of $69,033.00.
CORRECTS: Draft Q2: "the books accrued a full-time $75,000 salary for him: $68,750 for 2023, $74,775 for 2024 and $69,033 for 2025". The same $74,775 is in ANALYSIS - Cash Paid to the Founder (Rebuilt).md section 3.
Q: How was the $69,033 for 2025 calculated, and what did Mark change in journal entry AJE-547 on March 31 and April 8, 2026?
HOW: qb_gl.csv, account "Wages Due to Jeremiah": positive lines 2023 = 68,750.22 (AJE-76..86); 2024 = 74,774.77, of which AJE-202..206 and AJE-326..333 = 71,875.23 and num "Gusto" 2024-10-28 (Debit net pay 1,924.22; Debit reimbursement 552.19; Debit tax 423.13) = 2,899.54; 2025 AJE-547 = 69,033.00. The same 71,875.23 appears in "73902 Salaries & Wages" as 2024 skipped-paycheck entries. QuickBooks audit log 2026: AJE-547 added Feb 26, 2026 by Strata Cloud Accountants; edited by Mark Clark on Mar 31 and Apr 8, 2026.

## W06 [high] VERDICT: -
The 2024 return's wage deduction ($140,131 + $3,694 = $143,825) equals the QuickBooks salary account ($182,956.27) less the net 2024 increase in "Wages Due to Jeremiah" ($39,130.48). In gross terms, $71,875.23 of accrual entries are excluded and $32,744.75 of transfers to his personal checking are included; the $35,644.29 is all 29 transfers charged to that account, $2,899.54 of which offset an Oct 28, 2024 Gusto pay run already in wages.
CORRECTS: Draft finding 3: "2024 left the accrual out but deducted $35,644 of transfers to his personal checking as wages." Analysis section 1a states the same.
Q: How did the CPA arrive at the 2024 wage deduction of $143,825, and was a W-2 issued to Jeremiah for the transfers included in it?
HOW: 182,956.27 - 39,130.48 = 143,825.79. Equivalent forms: 182,956.27 - 74,774.77 + 35,644.29, or 182,956.27 - 71,875.23 + 32,744.75. All 29 negative 2024 lines in "Wages Due to Jeremiah" carry "0002" memos and sum to -35,644.29. Return lines 7 and 8 read from image f1120s_2024-01.png. That the transfers were deducted "as wages" is an inference from this arithmetic; the return does not itemise line 8.

## W07 [high] VERDICT: -
The $22,112 ($22,111.99) is not a share of the $44,384 of card payments. It is 23 journal entries crediting his owner account during 2025, against total 2025 cash to him or his creditors of $118,128 gross. $12,393.88 of it is credit for vendor invoices recorded as paid by him (offset to Accounts Payable) and $9,718.11 is spread across expense categories; the ledger holds journal entries, not expense reports, and does not show when anything was submitted.
CORRECTS: Draft Q3: "In 2025 the company paid $44,384 of his personal card bills ... None of the 2026 amounts has an itemized expense report in the ledger. In 2025, $22,112 did; he does front real business costs and those were itemized when submitted."
HOW: qb_gl.csv, account "33500 Due to Jeremiah", year 2025, type Journal Entry, amount > 0: 23 entries, 22,111.99 (the AJE-387/388 reclass debits excluded). Other legs of those entries: 31000 Accounts Payable -12,393.88, remainder in expense and COGS accounts. Example memo in AJE-406: "payment for Invoice#79459 - waiting for invoice copy" 3,066.78. 2025 gross cash = card payments 44,384.47 + transfers 72,347.32 + Tickpick 396 + transfer 1,000 = 118,127.79.

## W08 [high] VERDICT: -
$77K, $50K and $48K are the returns' Schedule M-1 line 1 "net income (loss) per books": (76,644), (49,879), (47,893). The page-1 losses are (72,663) for 2023, (67,869) for 2024 and (47,893) for 2025; the 2024 figure of (49,879) is after $17,990 of other gross rental income. The QuickBooks losses of $564,654, $294,663 and $115,190 are confirmed.
CORRECTS: Draft finding 4: "The IRS has seen losses of $77K, $50K and $48K for 2023 to 2025."
HOW: Images f1120s_2023-01/-05, f1120s_2024-01/-05, f1120_2025-01/-05 (line 22 or 30, and Schedule M-1 line 1). QuickBooks: "Net Income" row of BRAVADO SPICE LLC_Profit and Loss by Month - 2023/2024/2025.xlsx = -564,653.80; -294,662.76; -115,190.10.

## W09 [high] VERDICT: -
The "Cash" accounting-method box is checked on the 2023 and 2024 Forms 1120-S (Schedule B line 1). The 2025 Form 1120 PDF has no page 4, where that box sits, so the 2025 method is not shown in the documents provided. None of the three copies shows a filing confirmation: 2023 is watermarked "Client Copy" and the officer signature lines are undated.
CORRECTS: Draft finding 4: "The returns are cash-basis." Draft finding 1: the statement "tells the IRS". Analysis table section 1 lists 2025 as "Cash".
Q: Can we see page 4 of the 2025 Form 1120 and the e-file acceptance for each of the three returns?
HOW: Images f1120s_2023-02.png and f1120s_2024-02.png (Schedule B line 1a). pdfinfo "Bravado Spice 2025 Form 1120.pdf" = 10 pages: form pages 1, 2, 3, 5, 6, Form 1125-A, Schedule G, two statement pages, termination statement. The 2025 Schedule L shows no receivables, inventory or accounts payable, which is consistent with cash method but is not the checkbox.

## W10 [high] VERDICT: -
The "Changes in Ownership" page is printed "This page is not filed with the return. It is for your records only" and names no holder other than Hugh. It lists change dates 07-22-2024, 11-20-2024 and 11-26-2024, with total shares 10,000 on each of those rows and 10,700 for the last 35 days of the year (Nov 27-Dec 31). What the filed forms show is 6 shareholders, 10,000 shares at the start of 2024 and 10,700 at the end; the K-3 notification's wording is "Each of the shareholders was a U.S. citizen, resident alien, or certain domestic trust".
CORRECTS: Draft finding 1: "shows total shares at 10,700 from November 26, 2024 ... So the 2024 return recorded Comatri's shares on the right dates but did not treat the holder as a corporation".
Q: Whose holdings changed on July 22, November 20 and November 26, 2024 in the CPA's ownership schedule, and who are the six 2024 shareholders?
HOW: Images k1_hugh-4.png (worksheet; Christy's page 4 is identical), k1_hugh-6.png (K-3 notification), k1_hugh-1.png item D (10,000 / 10,700), f1120s_2024-01.png item I (6). Day counts 204 + 121 + 6 + 35 = 366; 1000/10000 x 331/366 + 1000/10700 x 35/366 = 9.93744%. 11/20/2024 is also the date the second Comatri agreement was sent for signature and the start date of its records-access clause.

## W11 [high] VERDICT: -
Mark Clark's text reads: "Bravado is an S corp. However Blake's investment in Bravado was via his C corp which is not allowed under S corp rules. Absent amending the investment to be personal by Blake, the S election would be invalidated. I had thought this adjustment was made but apparently it wasn't." It ends "there would be no k1 for the shareholders for 2025." The screenshot carries no date; Aug 25, 2026 comes from the file name.
CORRECTS: Draft Q5: "When did Jer and Mark learn the corporate member was a problem, given Mark's August text to you said S corp?" (the same text already states the C-corporation issue).
Q: Mark, what was the "adjustment" to make Blake's investment personal that you thought had been made, who was to make it, and when?
HOW: Read /home/user/bravado-analysis/Correspondence/2026-08-25 - Mark Clark text to Hugh re S corp.jpg.

## W12 [high] VERDICT: -
No document provided shows in whose name the 2024 return placed the 1,000 shares, or whether a K-1 for them was prepared or sent. The 2024 Form 1120-S reports 6 shareholders and 10,700 year-end shares, and only Hugh's and Christy's K-1s are in the file. That neither Blake nor Comatri received a K-1 is the member's own statement.
CORRECTS: Draft Q5: "so the 2024 return put those shares in a name that was never sent the form."
Q: Was a 2024 K-1 prepared for Comatri, Inc. or for Blake Benthall, and where was it sent?
HOW: Reviewed all 11 pages of the 2024 Form 1120-S and both 6-page K-1 packages; no shareholder list or other K-1 is included. Non-receipt is recorded as Blake's confirmation in the Analysis memo section 2 (testimony).

## W13 [high] VERDICT: -
The texts show the request ("a 7500 usdc transfer for a 8500 return in a month") and Blake's agreement on Apr 29, 2026, and a 100 USDC test sent Apr 30; the screenshots do not show the remaining transfer. QuickBooks' last ledger transaction is Mar 27, 2026, before the loan, so it could not contain it. Finaloop through Jul 23, 2026 has no loan account or line naming Blake; the only company record is the cash plan, which lists "Blake Benthall $7,500" (added Jul 20, 2026).
CORRECTS: Draft Q9: "My personal loan of April 29 ($7,500, with $8,500 due in one month) has not been repaid and is in neither ledger".
Q: Is the $7,500 loan from Blake a company debt or Jeremiah's personal debt, and where is it recorded in the books?
HOW: Correspondence PNGs dated 2026-04-29 (SMS, Wed Apr 29 1:47 PM; Signal thread Apr 29-30). finaloop_gl.csv: no Description matching benthall|blake|usdc|coinbase|comatri; liability accounts are Tallerine line of credit, Amex, OnDeck, Shopify Capital, Nguyen and SBA only. qb_gl.csv max date 2026-03-27. Cash plan workbook 2026-07-22, sheet Audit_Log row dated 2026-07-20 and sheet Debt_Schedule_Ref.

## W14 [high] VERDICT: -
QuickBooks' last ledger transaction is dated Mar 27, 2026, but its audit log shows Mark Clark editing journal entry AJE-547 on Mar 31 and Apr 8, 2026. It also shows sign-ins after that by Jeremiah Tallerine (to Jul 19), Robert Vople (to Jun 3) and William S Annon, CPA (May 24 to Jul 21, 2026). Strata Cloud Accountants' last logged events are in March (6 events).
CORRECTS: Draft Q9: "QuickBooks, which the company stopped using in March".
HOW: qb_gl.csv max date. /home/user/bravado-analysis/Financials/Quickbooks/Audit Log - 2026.csv: rows grouped by month and user; rows 43-44 "Edited Journal Entry No. AJE-547" by Mark Clark, Apr 8; row 89 same, Mar 31; Strata counts Jan 1,111 / Feb 198 / Mar 6.

## W15 [high] VERDICT: -
These statements in the reply rest on the member's own recollection (NOTES - Bravado Timeline.md), not on a document: Jer said in April he would step down in January; he has lived in New York since early 2026; on July 21 he said he would be away about ten days with Marissa running things; neither Blake nor Comatri sent the $4,600; neither received a K-1; the loan is unrepaid; Blake has lost Finaloop access and can still log in to QuickBooks. Partial document support: the July 22 document says "I am medically burned out"; the ledger shows a lease-application check on Jan 14, 2026 and Brooklyn, NY card descriptors; QuickBooks spells the name "Marisa Whitenton".
HOW: NOTES - Bravado Timeline.md entries 2026-01/02, 2026-04-16, 2026-05-01, 2026-07-21. July v4 document section "What I am asking of you". finaloop_gl.csv owner-account descriptors (e.g. 2026-05-14 "BROOKLYN, NY"); qb_gl.csv check 7588 memo "Tallerine/ Whitenton Lease App"; Finaloop 2026-03-03 "Zelle payment to Marisa Whitenton". Not tested as documents and not refuted.

## C01 [high] VERDICT: -
Confirmed: Form 1120 Schedule L line 7, $294,256, equals Finaloop's Dec 31, 2025 opening balances for Jeremiah ($237,886.89) plus James Nelson ($56,368.76) = $294,255.65. Mark's $219,892 equals QuickBooks ($75,440.62 + $88,082.47 + $56,368.76 = $219,891.85), and the $74,364 difference is $69,033.00 + $5,330.80 exactly. One caveat: Finaloop labels the $157,115.47 component only "2026 opening balance adjustment"; that it contains the wage accrual is an exact arithmetic match ($157,115.47 - $88,082.47 = $69,033.00), not a label.
HOW: finaloop_gl.csv, "Due to/from owner ... Jeremiah Tallerine", lines dated 2025-12-31: 5,330.80 + 75,440.62 + 157,115.47 = 237,886.89; "Related party balance ... James Nelson" 56,368.76. qb_gl.csv balances at 2025-12-31: Due from Jer 75,440.62; 33500 Due to Jeremiah -88,082.47; Due from James 56,368.76; 53000 Jer's Draw -5,330.80 (three 2025 lines). Return figure from image f1120_2025-05.png.

## C02 [high] VERDICT: -
Confirmed: Form 1120 line 13, $62,919, is $69,033.09 less than the 2025 Gusto wages in QuickBooks, $131,952.09 (salary account $200,985.09 less AJE-547 $69,033.00).
HOW: qb_gl.csv, account "73902 Salaries & Wages", 2025: num "Gusto" lines 123,081.19 + 4,549.93 + 3,117.47 + 1,203.50 = 131,952.09; AJE-547 69,033.00. Line 13 from image f1120_2025-01.png. The return does not show how line 13 was derived.

## C03 [high] VERDICT: -
Confirmed: the 2023 return's wage deduction ($384,873 + $10,039 = $394,912) equals the entire 2023 salary account ($394,912.11), which includes the $68,750.22 accrued to Jeremiah. AJE-547 is $69,033.00, the accrued-wage balance is $176,913.70, and no accrued-wage liability appears on Schedule L or its statements in 2023, 2024 or 2025.
HOW: qb_gl.csv 73902 total for 2023; "Wages Due to Jeremiah" balances 68,750.22 / 107,880.70 / 176,913.70 at the three year-ends. Images f1120s_2023-01/-04, f1120s_2024-04/-10 (Statement #22), f1120_2025-05/-09 (Statement #11).

## C04 [high] VERDICT: -
Confirmed: the termination statement attached to the 2025 Form 1120 is signed "Jeremiah Tallerine, President", dated 10/10/2026, and gives "Date of Transfer/Acquisition: January 1, 2025" for Comatri Inc., 1,000 shares, 9.34579%. The first Comatri agreement is dated and effective July 22, 2024 ($15,010 received that day); the second is signed 11/26/2024 ($35,000 received Dec 2, 2024).
HOW: Image f1120_2025-10.png. pdftotext of both agreement PDFs. qb_gl.csv "Member Equity - Coinbase": 15,010 on 2024-07-22 and 35,000 on 2024-12-02.

## C05 [high] VERDICT: -
Confirmed quotations. July 22 v4 document: "Took multiple outside jobs to put more money into Bravado and to make skipping my own paychecks possible"; "The plan does not depend on new borrowing"; Tallerine line of credit $69,440 "Forgiven". Operating agreement 5.1: "compensation commensurate with the value of such services". Second agreement 1(a): "access to the Company's financial records from 11/20/2024 until either Jeremiah Tallerine is no longer a majority stack holder in the Company or in the event the Investor divests". The August 24 briefing dates the new $10,000 family loan Jul 28, six days after July 22.
HOW: pandoc text of 2026-07-22-Bravado-State-of-Business-v4.docx (the 8-page private version words it "took multiple jobs outside Bravado"); pdftotext of the 11/26/2024 agreement and its Exhibit A; 2026-08-24 briefing sections 2 and 4. Operating agreement 4.1 (majority of capital interests elects Managers) and 4.6 (each Member may inspect and copy all books and records) also read. The $10,000 is not in any ledger provided: Finaloop ends Jul 23.

## C06 [high] VERDICT: -
Confirmed: the Nguyen loan is $100,000.00 at Dec 31, 2024 and $88,767.00 at Dec 31, 2025 in QuickBooks, $88,767 on the 2025 return and in Finaloop's opening balance, and $88,767 at Sep 30, 2026 on Mark's draft. Finaloop shows no payment to the Nguyens from Jan 1 to Jul 23, 2026.
HOW: qb_gl.csv "Loan From Nguyen": principal reductions 3,707 (2025-07-07), 3,744 (2025-07-28), 3,782 (bill 2025-08-30, paid 2025-09-02); three $4,707 payments including $2,888 interest. finaloop_gl.csv: one opening line, 88,767; no Description matching nguyen|frost bank. mark_draft_BS.txt. Image f1120_2025-05.png line 19.

## C07 [high] VERDICT: -
Confirmed: Schedule G reports 65.421%, which is 7,000/10,700; the second agreement's Exhibit 2 lists Jeremiah 7,000, Nguyens 2,000, Clark 500, Comatri 1,000 (sum 10,500) under "TOTAL COMPANY SHARES: 10,700". Additional document fact: the first agreement's Exhibit 2 (July 22, 2024) lists Jeremiah at 72%, Nguyens 20%, Clark 5%, Comatri 3%, so the 200-share gap equals the drop in his listed holding from 7,200 to 7,000.
Q: Jeremiah was listed at 72% on July 22, 2024 and at 7,000 shares on November 26, 2024; who received the 200 shares, and is that the sixth shareholder on the 2024 return?
HOW: Image f1120_2025-07.png. pdftotext of both agreements, Exhibit 2. 7,000/10,700 = 65.4206%; 7,200/10,700 would be 67.290%. The K-1 worksheet shows a change on 11-20-2024 with total shares unchanged at 10,000, and the 2024 return counts 6 shareholders.

## C08 [high] VERDICT: -
Confirmed in Finaloop: the last Gusto pay period is 03/09/2026-03/24/2026 (Gusto wages $28,647.46, January to March only), and "Payroll payable" is $176,913.70 at both the opening and Jul 23, 2026, with no 2026 accrual to Jeremiah. Two related document facts: Mark's draft line "Accrued wages-Jeremiah" moves from $176,914 to $177,063 (+$149, equal to Finaloop's "Other payroll deductions payable" of $149.37), and the July 22 document says "September: Founder pay moves to sustainable $5K/month, conditional on revenue landing."
Q: Has Jeremiah been paid $5,000 a month since September as the July document planned, and through which account?
HOW: finaloop_gl.csv: "Salaries & wages (via Gusto)" by month 10,298.88 / 10,370.70 / 7,977.88; "Payroll payable" opening 176,913.70 ("Wages Due to Jeremiah, OB (based on BS)") plus 2,055.69 closing adjustment, Gusto movements net -2,055.69. Contractors account rises from April (direct payments to three individuals). Gusto entries are not split by employee, so whether Jeremiah was on the January-March payroll is not shown.

## C09 [high] VERDICT: -
Confirmed: 2025 payments to his card accounts total $44,384.47 ($44,281.94 charged to his owner accounts plus $102.53 booked to Bank Fees), including Apple Card $10,890.90 on Jan 30, 2025 and Bank of America $10,103.60 on Jan 31, 2025. Six further 2025 payments to Citi, Credit One and Bank of America ($1,906.22) were booked straight to Travel, Office and Shipping Supplies and are not in the figure. The bookkeeper's memo on the Apple Card line reads "reimbursement for jer's personal cc used for business expenses".
HOW: qb_gl.csv 2025, non-journal lines in 33500 Due to Jeremiah / 53000 Jer's Draw / Wages Due to Jeremiah whose memo names a card: Chase card 8965 7,768.29; Apple 10,890.90; Bank of America 11,816.60; Capital One 9,234.07; Citi 2,551.30; Credit One 555.52; Mastercard 1,465.26 = 44,281.94. Bank Fees: Mastercard payments 37.53 + 65.00. The Apple payment was first charged to Wages Due to Jeremiah and moved to 33500 by AJE-387.

## C10 [high] VERDICT: -
Confirmed from Mark's draft and the ledgers: cash $1,963 against accounts payable $204,880 at Sep 30, 2026; "Unallocated reimbursements" $31,312; Due from Jeremiah up $44,577 (163,523 to 208,100); Tallerine note $79,440 against $69,440 at Dec 31, 2025 (also $69,440 on the 2025 return, Statement #11). Bad debts $17,587 equals the Dec 31, 2025 receivable, written off in Finaloop on Jun 30, 2026 ($17,586.74); $115,190 - $46,157 = $69,033; $7,861 + $63,482 = $71,343, which is $2,310 above $69,033. Mark's draft shows Due from James at $56,072 for Dec 31, 2024 and $56,369 from Dec 31, 2025; QuickBooks reaches $56,368.76 by a $297 reclass dated Dec 31, 2024.
CORRECTS: Draft notes: "James has been static at $56,369 since 2024" (Mark's draft shows $56,072 at Dec 31, 2024).
HOW: mark_draft_BS.txt and mark_draft_PL.txt arithmetic. finaloop_gl.csv "Bad debt" line 2026-06-30 "Invoice Uncollectible". qb_gl.csv "Due from James" AJE-397. July v4 document net income 2025 ($46,157). Finaloop's "Reimbursements to owners" is $27,640.33 through Jul 23, 2026; it is not tied to Mark's $31,312, which runs to Sep 30.

- UNTIED: $52,422 total: reproduced at $52,416.55 from Finaloop bank lines, $5.45 short; the prior memo's $2,106 of "unclassified" items could not be rebuilt line for line.
- UNTIED: Whether the Capital One, Citi and Petal card accounts paid in 2026 ($24,328.83) are personal cards: no statements are in the records; descriptors show only the issuer and "IND NAME: Jeremiah Tallerine".
- UNTIED: Check #7590, $3,250 to Seth Beacher ("2D Deposit"): purpose not shown in either ledger; QuickBooks leaves it in Uncategorized Expense and Finaloop books it as a distribution.
- UNTIED: Source of the $4,600 "CAPITAL ONE - TRANSFER RT010850381BE61" on May 1, 2026 (booked to Capital - Blake Benthall): not identifiable from the ledger. Its descriptor has the same form as the Apr 23, 2026 $400 inflow that Finaloop booked to Capital - Jeremiah Tallerine.
- UNTIED: Mark's "Unallocated reimbursements" of $31,312 (9 months to Sep 30) against Finaloop's "Reimbursements to owners" of $27,640.33 (to Jul 23): different periods, $3,671.67 apart, no August-September ledger available.
- UNTIED: Mark's "Other" note of $19,391 at Sep 30, 2026: Finaloop at Jul 23 carries Loan payable - American Express $13,210.90 and Loan payable - Ondeck Capital $13,949.93 (a $19,000 OnDeck deposit arrived Feb 18, 2026), together $27,160.83; no combination tested equals $19,391, with or without Blake's $7,500.
- UNTIED: Mark's Due from Jeremiah increase of $44,577 against Finaloop, where the same account fell from $237,886.89 to $226,743.59 by Jul 23 (including two Apr 7, 2026 "Manual Clearing Adjustment" entries of -$6,033.40 each).
- UNTIED: 2025 accounting method: Form 1120 page 4 is absent from the 10-page PDF.
- UNTIED: Filing status of all three returns: no e-file acknowledgement or IRS transcript is in the documents.
- UNTIED: Officer compensation of $10,039 (2023) and $3,694 (2024) on the returns: not identified as a separate amount in the ledger; only the combined wage totals tie.
- UNTIED: The $10,000 Jul 28, 2026 family loan: not in any ledger provided (Finaloop ends Jul 23); sourced to the Aug 24 briefing ("Anthony, Jul 28") and the August cash plan (Timeline row: "wire from Veronica M Tallerine"). That $79,440 = $69,440 + $10,000 is arithmetic; Mark's draft gives no breakdown.
- UNTIED: Blake's loan: the screenshots show the request, the agreement and a 100 USDC test on Apr 30, 2026; the transfer of the balance and its date are not in the archived images.
- UNTIED: Date of Mark Clark's text to Hugh: not visible in the screenshot; Aug 25, 2026 is from the file name only.
- UNTIED: Date of the July v4 document: the text says "July 2026"; July 22 comes from the file name and from the Aug 24 briefing's reference to the "July 22 Plan"; file metadata is not preserved.
- UNTIED: What Mark Clark changed in AJE-547 on Mar 31 and Apr 8, 2026: the audit log records the edits but not their content.
