# Citation Index — figure, source, derivation

Paths are relative to the repository root. "QB GL" = `Financials/Quickbooks/BRAVADO SPICE LLC_General Ledger - full.csv`. "Finaloop" = `Financials/Finaloop/Bravado - General_Ledger_2026_YTD Finaloop - Unlocked.numbers`. "Hugh pack" = `Jer to Investors/2026-11-18 - From Hugh (tax returns and Clark draft)/`. Return pages are cited by PDF page; rendered images are in `HANDOFF/process/return-page-images/`.

## Founder balances

| Figure | Source | Derivation |
|---|---|---|
| Due from Jer $75,440.62 (Dec 31, 2024 and 2025) | QB GL, account "Due from Jer" | 22,237.89 + 4,728.43 + 26,324.27 + 835.00 + 18,068.71 + 3,246.32 |
| 33500 Due to Jeremiah −$88,082.47 (Dec 31, 2025) | QB GL, account "33500 Due to Jeremiah" | Sum of 2025 entries; no year-end sweep made |
| Jer's Draw −$5,330.80 (2025) | QB GL, "53000 Jer's Draw" | 330.80 + 2,500 + 2,500 |
| Wages Due to Jeremiah $176,913.70 | QB GL, "Wages Due to Jeremiah" | 68,750.22 + 74,774.77 + 69,033.00 − 35,644.29 |
| AJE-547 $69,033.00 | QB GL, num AJE-547, dated 12/31/2025; audit log 2026 (created Feb 26, 2026; edited by Mark Clark Mar 31 and Apr 8, 2026) | Debit 73902 Salaries & Wages, credit Wages Due |
| Finaloop owner receivable opening $237,886.89 | Finaloop, account "Due to/from owner - non-interest balance - Jeremiah Tallerine", rows dated 2025-12-31 | 75,440.62 + 157,115.47 + 5,330.80 |
| $157,115.47 = $88,082.47 + $69,033.00 | Finaloop opening row; QB balances above | Arithmetic match to the cent |
| Finaloop receivable $226,743.59 (Jul 22, 2026) | Finaloop, same account | Opening + 923.50 personal charges − 2 × 6,033.40 |
| Finaloop Payroll payable $176,913.70 | Finaloop, "Payroll payable", description "Wages Due to Jeremiah, OB (based on BS)" | Opening; unchanged net of Gusto runs |
| Mark's Due from Jeremiah $163,523 / $208,100 | Hugh pack, `(Mark_DRAFT BS).pdf` | As printed (12/31/2025; 9/30/2026) |
| Loans to shareholders $294,256 (and $131,809; $100,231; $43,295) | 2025 Form 1120 p.6 Schedule L line 7; 2024 Form 1120-S p.4; 2023 Form 1120-S p.4 | 2025: 237,886.89 + 56,368.76 (Due from James) |
| Gap $74,363.80 | Above | 69,033.00 + 5,330.80 |

## Cash paid to the founder

| Figure | Source | Derivation |
|---|---|---|
| Annual gross cash 2020–2025: 73,104 / 21,358 / 41,712 / 77,017 / 87,509 / 118,128 | QB GL: bank and card lines whose split is one of the four founder accounts, plus direct-expensed personal-card payments, Expensify bills paid to vendor "Jeremiah Tallerine", 2020 Gusto owner's-draw runs | Method and exclusions in `ANALYSIS - Cash Paid to the Founder (Rebuilt).md` §1 |
| 2026 (Jan 1–Jul 22) $49,191.55 | Finaloop: Distributions, Reimbursements to owners, personal charges on the owner account, Citi payments in "Unidentified payouts & transfers" and "Miscellaneous expenses", July transfers in "Money-out"/"Money in transit", check 7588 | 24,328.83 cards + 23,689.22 transfers to checking 5820 + 923.50 + 250.00; excludes check 7590 ($3,250) |
| Check #7590 $3,250, payee and memo | QB GL, Chase 8733, Jan 27, 2026 (payee Seth Beacher, memo "2D Deposit"); Finaloop Distributions | — |
| Itemized reimbursements 2022–2025: 17,792 / 41,334 / 26,126 / 22,112 | QB GL: journal entries and bills crediting 33500 or Jer's Draw with expense or A/P splits | Listed in the rebuilt cash memo §6 |
| Charged to accrued wages $35,644.29 (2024) | QB GL, "Wages Due to Jeremiah", bank-split debits | 29 transfers to CHK …0002 |
| 2025 personal-card payments $44,384.47; Apple Card $10,890.90 (Jan 30, 2025); Bank of America $10,103.60 (Jan 31, 2025) | QB GL, bank lines | — |
| Monthly series Jan 2023–Jul 2026 | Same sources | Appendix of the rebuilt cash memo; January 2026 reduced by 3,250 |

## Results and liabilities

| Figure | Source | Derivation |
|---|---|---|
| Net income 2014–2025 (e.g. 2023 −564,654; 2024 −294,663; 2025 −115,190) | `Financials/Quickbooks/…Profit and Loss by Month - YYYY.xlsx` | Official exports; reproduce from QB GL |
| 2025 operating loss ($271,832) | Same | 115,190 + 156,642 other income |
| 2025 other income $156,640.86 | QB GL, "80001 Other Misc Income" | Treasury receipts 101,289.51; AJE-455 7,661.73; AJE-456 43,743.70; AJE-496 3,034.90; AJE-422 911.02 |
| 2024 write-off $23,217.12 | QB GL, AJE-229, June 30, 2024, memo "per Jer this is not part of Bravado Spice's debt" | — |
| Total liabilities by year-end (45,728 … 805,512) | `…Balance Sheet - Quickbooks.xlsx` | Official export |
| Finaloop 2026 result ($51,407.62) through Jul 22; ($52,373.23) through export | Finaloop profit-and-loss accounts | Income accounts less contra and expense accounts; export imbalance 5,872.88 |
| January–June 2026 operating loss ($57,295) vs "(−$21,974)" stated | Finaloop; July 22, 2026 "State of the Business" v4 | `ANALYSIS - Claims vs Books.md` |
| Nguyen note: 100,000 → 88,767; payments Jul 7, Jul 28, Sep 2, 2025 | QB GL, "Loan From Nguyen"; Finaloop "Related party loan payable - Hugh & Christy Nguyen" | 3 × 4,707; principal 11,233; interest 2,888 |
| Tallerine line $69,440.20 | QB GL "33100 Anthony Tallerine LOC" (60,000 on Sep 13, 2023 + 9,440.20 AJE-92); Finaloop; 2025 Form 1120 Statement #11 | — |
| SBA payments 2026: $1,705 (Mar 3), $1,705 (May 20) | Finaloop, "Long-term loan payable - Small Business Administration" | — |

## Tax returns and ownership

| Figure | Source |
|---|---|
| 2023: 2 shareholders; gross receipts 1,868,988; loss per books (76,644); "Debt to Equity 129,000" | 2023 Form 1120-S pp. 1, 4, 5, Statement #22 |
| 2024: 6 shareholders; cash method; ordinary loss (67,869); loss per books (49,879); APIC 189,010; wages 140,131 + 3,694 | 2024 Form 1120-S pp. 1, 2, 4, 5 |
| 2025: Form 1120; salaries 62,919; taxable loss (47,893); other current liabilities 87,313 (credit cards 17,873; Tallerine 69,440) | 2025 Form 1120 pp. 1, 6, Statement #11 |
| Jeremiah 65.421% | 2025 Form 1120, Schedule G (= 7,000 / 10,700) |
| S-termination statement: "effective January 1, 2025"; "Date of Transfer/Acquisition: January 1, 2025"; signed 10/10/2026 | 2025 Form 1120 PDF, last page |
| Hugh: 1,000 shares; corporation 10,000 → 10,700; allocation 9.93744%; change dates 07-22-2024, 11-20-2024, 11-26-2024 | `2024 Schedule K-1 Hugh Nguyen.pdf` pp. 1 and 4 (worksheet marked "not filed with the return") |
| "Each of the shareholders was a U.S. citizen, resident alien, or certain domestic trust" | Same PDF p. 6 (standard K-3 notice) |
| Comatri agreement 1: $15,000 for 3%, effective July 22, 2024; Exhibit 2 lists Jeremiah 72% | `Jer to Investors/2024-07-21 - Comatri Agreement 1/COMATRI_INC_INVESTMENT_AGREEMENT.pdf` |
| Comatri agreement 2: $35,000 for 700 shares, effective 11/26/2024 "or the day $35,000 is paid"; access clause; Exhibit 2: 7,000 / 2,000 / 500 / 1,000, "TOTAL COMPANY SHARES: 10,700" | `Comatri Investment Agreements/2024-11-26 - Comatri__Inc_2nd_investment_agreement..pdf` |
| Comatri deposits $15,010 (Jul 22, 2024), $35,000 (Dec 2, 2024) | QB GL, "Member Equity - Coinbase" |
| Operating agreement §5.1 "commensurate with the value of such services"; §1.9; §4.1; §4.6 | Exhibit A to either Comatri agreement |

## Statements by management

| Statement | Source |
|---|---|
| "Took multiple outside jobs to put more money into Bravado and to make skipping my own paychecks possible" | July 22, 2026 "State of the Business" v4, `Jer to Investors/2026-07-22 - All Investors/` |
| "The plan does not depend on new borrowing" | Same; and the eight-page version shared with Blake July 21 |
| Tallerine line of credit "Forgiven" | Both July 2026 versions (see `ANALYSIS - Forgiven Loan and Comatri Retitle.md`) |
| "The $75K I have drawn" | Eight-page version only |
| New $10,000 family loan, July 28, 2026 | `Jer to Investors/2026-08-24 - All Investors/` briefing and cash plan |
| "let's not make any discretionary cash payments until sales get back in line" (Mark Clark, Jan 16, 2025) | `Jer to Investors/2025-01-27 - To Blake and Mark/Fwd_ 2025 Budget attached.eml` |
| Mark's text on S-corporation status | `Correspondence/2026-08-25 - Mark Clark text to Hugh re S corp.jpg` (date from file name) |
| "Would you consider a 7500 usdc transfer for a 8500 return in a month?" | `Correspondence/2026-04-29 - Jer text to Blake …png` and the Signal thread image |
