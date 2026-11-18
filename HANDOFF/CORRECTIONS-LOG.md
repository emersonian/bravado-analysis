# Corrections Log — what was got wrong along the way, and how it was caught

Kept so a follow-on agent can see where this analysis has been fragile. Newest last.

| When | What was wrong | How it was caught | Fix |
|---|---|---|---|
| Aug 2026 | Edits to AJE-547 attributed to Hugh | Audit-log actor field | They were Mark Clark's (Mar 31 and Apr 8, 2026) |
| Aug 2026 | Strata Cloud Accountants' last activity placed in 2025 | Audit log | March 27, 2026 |
| Aug 2026 | Comatri's first $15,010 described as pre-agreement | Signed agreement dated July 21–22, 2024 | Corrected |
| Aug 2026 | Clark's $5,000 loan described as offset | Bank register | Repaid in cash May 16, 2025 |
| Aug 2026 | Language too dramatic ("smoking gun") | Client feedback | Standing rule: no characterization, no claims |
| Sep 1, 2026 | 2022 founder cash $46,200 included Endorphin Farms charges on James Nelson's card | Rebuild from raw GL after Mark Clark challenged the chart | $41,712 |
| Sep 1, 2026 | 2023 founder cash $30,300 omitted the draw account | Same rebuild; monthly chart and annual table disagreed by $39K | $77,017 |
| Sep 1, 2026 | 2024 "documented" $80,691 counted the CPA's $18,069 sweep as documentation | Same rebuild | $26,126 itemized + $37,992 as wages |
| Nov 18, 2026 | "Accrued wages never deducted on a return" | Reproduced each year's wage line from account 73902 | 2023 wage lines include the accrual |
| Nov 18, 2026 | …then "2023 deducted the accrual" | Independent returns tie-out: purchases are lower by the same amount | No net deduction in 2023 |
| Nov 18, 2026 | "$95,000 of founder-related outflows" in Mark's nine-month draft (sum of three lines) | Self-review, then independent review: the columns are on different ledgers | Withdrawn; verified figure is $49,192 through July 22 |
| Nov 18, 2026 | S-termination inference from the allocation percentage (33 days) | Found the K-1 "Changes in Ownership" worksheet (35 days from 11-26-2024) | Replaced; then led with paid-in capital on the filed Schedule L, because the worksheet is not filed and names no holder |
| Nov 18, 2026 | 2026 founder cash $52,422 and "transfers $26,919" | Fact-check: check #7590 went to a third party | $49,192; transfers $23,689 |
| Nov 18, 2026 | 2026 net result ($57,300) "through July 22" | Two agents summed Finaloop's P&L accounts | ($51,408); ($57,295) is the Jan–Jun operating loss |
| Nov 18, 2026 | 2025 other income described as "the $157K ERC" | Composition of account 80001 | $101,290 Treasury receipts + $51,405 card write-offs |
| Nov 18, 2026 | "The 2025 return uses Finaloop's opening balances" | Schedule L line-by-line | Only loans to shareholders does |
| Nov 18, 2026 | Accrued-wage arithmetic "less $37,992 plus $2,000" | Account roll-forward | $212,558 − $35,644 = $176,914 |
| Nov 18, 2026 | "Mark's August text said S corp" | Read the screenshot in full | The text itself raises the C-corporation problem |

## Recurring causes

1. **Adding figures across documents that are on different bases** (two ledgers, two dates, cash versus accrual). Check the basis of each column before subtracting.
2. **Treating a ledger classification as a fact about the world** (a card is "personal," a check is "to the founder"). The ledger shows how something was booked, not what it was.
3. **Stating an exact arithmetic match as a causal link.** Say "equals" and stop.
4. **Carrying a figure forward from an earlier memo** instead of recomputing it.

## Method that worked

Rebuild from the raw general ledger; reproduce an official report to the dollar before trusting the parse; have an independent pass recompute every figure that will be said aloud; ask a separate pass for the good-faith explanation of each finding and the single document that would settle it.
