export const meta = {
  name: 'bravado-ledger-review',
  description: 'Independent re-derivation and adversarial check of the Bravado founder balances, Clark draft, tax returns and the draft questions',
  phases: [
    { title: 'Investigate', detail: 'four independent investigators over the ledgers, draft financials, returns and the draft reply' },
    { title: 'Verify', detail: 'each investigator finding re-computed by a skeptic' },
    { title: 'Anticipate', detail: 'likely explanations and the document that settles each' },
  ],
}

const PACK = '/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/README_FOR_AGENTS.md'
const COMMON = `You are reviewing the books of a small Texas LLC (Bravado Spice LLC) for a minority member who meets management tonight. Accuracy matters more than volume: a wrong number said in the room is worse than no number. FIRST read ${PACK} in full — it lists every data file, the sign conventions, the people and the house rules. Work from the raw ledgers by writing and running small pandas scripts; do not trust figures in prior memos until you have reproduced them. Your final message is consumed by a program, not a person: return only the structured result.`

const FINDINGS = {
  type: 'object',
  properties: {
    summary: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          statement: { type: 'string', description: 'One or two sentences, exact figures, document-vs-document, no characterization' },
          how_computed: { type: 'string', description: 'Accounts, filters and arithmetic so a second person can re-run it' },
          confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
          corrects_prior_memo: { type: 'string', description: 'If this contradicts a prior memo or the draft reply, quote what was wrong; otherwise empty' },
          question_for_meeting: { type: 'string', description: 'A plain question management could be asked, or empty' },
        },
        required: ['id', 'statement', 'how_computed', 'confidence'],
      },
    },
    could_not_tie_out: { type: 'array', items: { type: 'string' } },
  },
  required: ['summary', 'findings'],
}

const VERDICTS = {
  type: 'object',
  properties: {
    verdicts: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          verdict: { type: 'string', enum: ['confirmed', 'confirmed_with_correction', 'refuted', 'could_not_verify'] },
          corrected_statement: { type: 'string' },
          note: { type: 'string' },
        },
        required: ['id', 'verdict'],
      },
    },
  },
  required: ['verdicts'],
}

const INVESTIGATORS = [
  {
    key: 'owner-balances',
    prompt: `${COMMON}

YOUR TASK — what the founder (Jeremiah Tallerine) owes the company and what it owes him, under every version of the books.
1. From qb_gl.csv compute the Dec 31 balance for each year 2019-2025 of: 33500 Due to Jeremiah, Due from Jer, 53000 Jer's Draw, Wages Due to Jeremiah, Member Equity - Tallerine, Due from James, 54000 James' Draw. Show the year-end sweep journal entries that moved amounts between them.
2. Build a full bridge from the QuickBooks Dec 31 2025 balance sheet (every balance-sheet account, computed from the GL) to Finaloop's opening balances (rows dated 2025-12-31 in finaloop_gl.csv). List every account where the two differ, the amount, and Finaloop's description of the opening entry. In particular decompose Finaloop's "Due to/from owner - non-interest balance - Jeremiah Tallerine" opening lines (75,440.62; 157,115.47; 5,330.80) into QuickBooks balances to the cent, and find what the offsetting side of the 157,115.47 was (which Finaloop account absorbed the 69,033 so that the opening balance sheet still balances — check "Payroll payable", "Retained earnings", "Prior year adjustment", capital accounts). Does Finaloop's opening balance sheet balance?
3. List every 2026 Finaloop entry touching the founder: Due to/from owner, Distributions, Reimbursements to owners, Capital - Jeremiah Tallerine, Payroll payable, plus any bank-side payment to his personal accounts/cards classified elsewhere. Explain the two "Manual Clearing Adjustment" entries of -6,033.40 on 2026-04-07 (find their counter-entries and descriptions).
4. State, for Dec 31 2025 and for the latest date available, the founder's gross receivable, the accrued-wage payable, and the net, under (a) QuickBooks, (b) Finaloop, (c) Mark Clark's draft (mark_draft_BS.txt), (d) the 2025 tax return Schedule L (returns_extract.md). Reconcile each pair of versions to the dollar or say what is unexplained.
5. Mark's draft shows "Due from Jeremiah" 208,100 at 9/30/2026 vs 163,523 at 12/31/2025 (+44,577) and Jeremiah equity 173,528 vs 192,849. Using Finaloop through Jul 22 2026, test hypotheses for how 208,100 could be built (e.g. 163,523 + distributions + reimbursements-to-owners + personal charges - contributions +/- clearing adjustments) and report which combination comes closest and the residual.
6. Check the member-related items too: "Related party loan payable - Hugh & Christy Nguyen" movements in 2025 (QuickBooks) and 2026 (Finaloop); "Line of credit - Anthony Tallerine"; "Capital - Blake Benthall" (a 4,600 deposit on 2026-05-01 from a "CAPITAL ONE - TRANSFER" — compare its bank descriptor with other inbound Capital One transfers and how those were classified); whether any loan from Blake Benthall (7,500 sent as USDC about Apr 30 2026 to a wallet the founder supplied) appears anywhere; SBA loan payments in 2026 (dates/amounts).`,
  },
  {
    key: 'clark-draft',
    prompt: `${COMMON}

YOUR TASK — test Mark Clark's draft financials (mark_draft_PL.txt, mark_draft_BS.txt) line by line.
1. For the 12/31/2024 and 12/31/2025 balance-sheet columns and the 2024 and 2025 income-statement columns, reproduce EVERY line from qb_gl.csv (group QuickBooks accounts as needed) and report the lines that tie, the lines that do not and by how much. Cross-check net income against the official exports in /home/user/bravado-analysis/Financials/Quickbooks/ (Profit and Loss by Month 2024 and 2025 xlsx). The draft shows 2024 net loss (301,103) against an official (294,663): find the exact cause.
2. Determine which ledger the 9/30/2026 column is built from. QuickBooks stops Mar 27 2026; Finaloop runs to Jul 23 2026 only. Compare each 9-month line with Finaloop's Jan 1-Jul 22 totals (finaloop_Profit_and_Loss_Index.csv and the GL) and report, per line, Finaloop-through-July vs draft-through-September and whether the gap is plausible for ~10 more weeks. Flag lines that are LOWER in the 9-month draft than in Finaloop's 7 months, or that have no Finaloop counterpart ("Unallocated reimbursements" 31,312 vs Finaloop "Reimbursements to owners"; "Bad debts" 17,587; "Compensation & benefits" 74,377; "Travel & auto").
3. Balance sheet 9/30/2026: for each line compare with Finaloop at Jul 22 (Balance Sheet Index). Explain if you can: Due from Jeremiah 208,100; Accts payable 204,880 (Finaloop "Inventory vendors - bills" + "Operational vendors - bills"); Notes payable "Other" 19,391 (candidates: Finaloop "Loan payable - American Express", "Loan payable - Ondeck Capital"); Tallerine 79,440; SBA 349,204; credit cards 7,085; Jeremiah equity 173,528.
4. Equity roll-forward: retained earnings (974,507) at 12/31/2025 -> (966,646) at 9/30/2026 while the 9-month net loss is (63,482). Quantify the unexplained movement and test whether it equals a reversal of the 69,033 accrual, Finaloop's "Prior year adjustment" account, or something else. Also check that each column of the draft balance sheet actually balances and that 2025 retained earnings roll forward from 2024 by the 2025 loss.
5. Gross margin: draft shows 52.8% for 2026 vs 32.4% (2025) and 28.5% (2024). Using the ledgers, say what changed in how cost of sales is recorded (e.g. which QuickBooks cost accounts existed in 2024-2025 that have no Finaloop equivalent, inventory movements, channel mix).
6. Report anything else in the draft a careful accountant would query (lines that are blank in one year, misspellings aside).`,
  },
  {
    key: 'tax-returns',
    prompt: `${COMMON}

YOUR TASK — test the three federal returns (returns_extract.md; verify key figures against the page images) against the QuickBooks ledger.
1. For each of 2023, 2024, 2025 try to reproduce from qb_gl.csv: gross receipts, cost of goods sold, officer compensation + salaries, rents, interest, the itemized "other deductions", other income, and the net loss per books. The returns are cash-method; say for each line whether it matches the accrual ledger exactly, a cash-adjusted figure, or neither.
2. Wages specifically. A prior memo claims: 2023 deduction 394,912 = entire account "73902 Salaries & Wages" including 68,750.22 accrued to the founder; 2024 deduction 143,825 = account total 182,956.27 - accruals 74,774.77 + 35,644.29 of transfers charged to "Wages Due to Jeremiah"; 2025 deduction 62,919 = Gusto wages 131,952.09 - 69,033.09. Re-derive each independently and say whether there is any OTHER combination of ledger amounts that also produces 62,919 (for example contractor reclassifications, employment-credit reductions, cost-of-labor in COGS) — i.e. is the 69,033 link the only exact fit?
3. Schedule L. Reproduce "Loans to shareholders" for each year-end 2022-2025 (43,295; 100,231; 131,809; 294,256) from the Due from Jer / Due from James / 33500 / Jer's Draw balances in QuickBooks and Finaloop's opening balances. Reproduce other current liabilities, notes payable, loans from shareholders, APIC (189,010) and retained earnings as far as possible. What liabilities that are on the QuickBooks balance sheet are absent from Schedule L each year, and how much?
4. Other income 2025 (156,641): identify its components in the ledger (account 80001 Other Misc Income, ERC refunds, write-offs). Mark Clark's draft splits it "ERC/PPA 131,781" + "Other income 24,316": test that split. Were any liabilities written off to income in 2024 or 2025 (e.g. AJE-229, AJE-253 "per Jer this is not part of Bravado Spice's debt")? Amounts and dates.
5. 2024: the return shows "other gross rental income 17,990" and Form 4797 gain 15,735; find them in the ledger. The Chevrolet sale proceeds 12,135 are recorded in AJE-307 as "received check amount directly to Jer": confirm how that was booked.
6. Ownership arithmetic: Hugh Nguyen's 2024 allocation 9.93744% from the worksheet periods (204, 121, 6, 35 days of 366; 1,000 shares of 10,000 then 10,700) — recompute. Schedule G 65.421% = 7,000/10,700? Which share counts sum to 10,700?
7. List any other internal inconsistency between the three returns (e.g. ending balances of one year vs beginning balances of the next; shareholder loan vs K-1 item).`,
  },
  {
    key: 'fact-check',
    prompt: `${COMMON}

YOUR TASK — adversarial fact-check. The member is about to send the text file "/home/user/bravado-analysis/DRAFT - Reply to Hugh (Nov 18 meeting questions).txt" to a co-investor, backed by "/home/user/bravado-analysis/ANALYSIS - Tax Returns and Clark Draft Financials.md". Read both. Extract EVERY factual assertion in the reply (each dollar figure, date, percentage, share count, quotation, and each "X equals Y" or "X is in neither ledger" claim) and test it against primary sources: the ledgers in the data pack, mark_draft_*.txt, returns_extract.md and the page images, the investor documents under "/home/user/bravado-analysis/Jer to Investors/" (use pdftotext for PDFs; .eml/.md/.txt directly), the agreements under "/home/user/bravado-analysis/Comatri Investment Agreements/" and "Jer to Investors/2024-07-21 - Comatri Agreement 1/", and "/home/user/bravado-analysis/NOTES - Bravado Timeline.md" for the member's own recollections (those are testimony, not documents — mark them as such, do not "refute" them).
Report one finding per assertion that is WRONG, OVERSTATED, UNSUPPORTED BY ANY DOCUMENT YOU CAN FIND, or materially imprecise — put the faulty wording in corrects_prior_memo and the accurate wording in statement. Also report (briefly, confidence high) the ten most important assertions you were able to confirm exactly, so the member knows which are solid. Specifically test: the quotation "took multiple outside jobs"; "the plan does not depend on new borrowing" and its date relative to the July 28 2026 $10,000 loan; the $52,422 Jan 1-Jul 22 2026 total and its split 24,329 / 26,919 / ~1,200; $44,384 of personal card bills in 2025 and the 10,891 and 10,104 January 2025 payments; "$22,112 itemized in 2025"; the accrued-salary figures 68,750 / 74,775 / 69,033; "$69,033 less than the wages actually run through Gusto ($131,952)"; "$294,256 equals Finaloop's opening balance for Jer plus James to the dollar"; "Your $74,364 difference is exactly $69,033 plus $5,331"; book losses 565K/295K/115K vs 77K/50K/48K; the Nguyen note balances; "7,000 of 10,700"; the operating-agreement quotations ("the value of such services"; "access to the Company's financial records"); and whether the claim that payroll "ended in March" and "no wages have been accrued this year" holds in Finaloop.`,
  },
]

function verifyPrompt(result, inv) {
  return `${COMMON}

YOUR TASK — you are a skeptic. Another analyst ("${inv.key}") produced the findings below from the same data pack. For EACH finding, independently recompute it from the raw files (write your own script; do not reuse theirs) and try to REFUTE it: look for double counting, sign errors, wrong year boundaries, accounts left out, coincidental matches, and alternative explanations a competent bookkeeper would offer. Verdict "confirmed" only if your own numbers match to the dollar (or the stated precision). If a figure is off, give the corrected statement. If the finding is an inference rather than arithmetic, say what is fact and what is inference. Prioritize findings with a non-empty question_for_meeting and those that correct a prior memo.

FINDINGS TO TEST (JSON):
${JSON.stringify(result.findings, null, 1)}`
}

phase('Investigate')
const steelmanP = agent(`${COMMON}

YOUR TASK — prepare the member for the answers they will hear. Read "/home/user/bravado-analysis/DRAFT - Reply to Hugh (Nov 18 meeting questions).txt" and "/home/user/bravado-analysis/ANALYSIS - Tax Returns and Clark Draft Financials.md" and "/home/user/bravado-analysis/ANALYSIS - Cash Paid to the Founder (Rebuilt).md". For each of the ten numbered questions in the reply, and additionally for the question "the latest books show the founder owes the company over $200,000 — does he agree, on what terms, and when will it be repaid?", write: (a) the most plausible good-faith explanation management or their CPA would give (be genuinely fair — cash vs accrual, software migration artifacts, a CPA's simplification, reimbursements for real business costs, accountable-plan mechanics, shareholder-loan conventions in S and C corporations); (b) whether the ledgers in the data pack are consistent with that explanation — test it with a quick calculation where you can; (c) the single follow-up question that separates the good-faith explanation from the alternative; (d) the one existing document that would settle it. Put each as one finding (id = q1..q11), with (a)-(d) in the statement and your test in how_computed. Do not characterize anyone's conduct.`, { label: 'anticipate:answers', phase: 'Anticipate', schema: FINDINGS })

const reviewed = await pipeline(
  INVESTIGATORS,
  inv => agent(inv.prompt, { label: `investigate:${inv.key}`, phase: 'Investigate', schema: FINDINGS }),
  (result, inv) => {
    if (!result) return null
    if (inv.key === 'fact-check') return { key: inv.key, result, verdicts: null }
    return agent(verifyPrompt(result, inv), { label: `verify:${inv.key}`, phase: 'Verify', schema: VERDICTS })
      .then(v => ({ key: inv.key, result, verdicts: v ? v.verdicts : null }))
  },
)
const steelman = await steelmanP
return { reviewed: reviewed.filter(Boolean), steelman }