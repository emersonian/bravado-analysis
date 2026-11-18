# Bravado Spice LLC — Handoff Package for a Follow-on Agent

**Assembled:** November 18, 2026. **Repository:** `emersonian/bravado-analysis`, branch `claude/research-facts-dishonesty-qzpyqo`. This file is the entry point. Read it fully before opening anything else.

## 1. The assignment so far

The client is **Blake Benthall**, who controls **Comatri, Inc.** (a Delaware C corporation). Comatri is a minority member (about 9.35%) of **Bravado Spice LLC**, a Houston hot-sauce company managed by its majority member and founder, **Jeremiah "Jer" Tallerine**. Co-investors **Hugh and Christy Nguyen** hold about 18.7% and lent $100,000. **Mark Clark** is a member and the company's former fractional CFO. The work is a documents-only comparison of what management told investors against the company's own ledgers and tax filings, in preparation for members' meetings, a written records request, and engaging counsel.

## 2. Standing rules (the client set these; keep them)

1. **Never characterize conduct.** No "fraud," "theft," "concealment," "lied." Say: "document A shows X; document B shows Y." The agreed phrase is "written statements of existing fact that his own books contradict."
2. **No hype and no claims.** The audience is a careful accountant or lawyer. State figures and sources.
3. **Health.** Refer to health-related merchants and to the founder's health only as "healthcare." Do not repeat anything about treatment.
4. **Mark Clark** is held in high regard by Hugh. Do not disparage him. Do not share the analysis of Mark, legal strategy, or draft documents with him.
5. **Do not attack** the margin math or the October 2024 purchase-order history; both were checked and are accurate.
6. **Jeremiah's personal card statements are not company records.** They can only be requested voluntarily.
7. **The records request must be reviewed by counsel before it is sent.**
8. Blake signs as an officer of Comatri, Inc.; the member is Comatri, not Blake. Bravado is an LLC: "members," not "shareholders."
9. Nothing in this package is legal or tax advice. Tax points (S-election termination, cancellation-of-debt income, related-party accruals) are flagged for a specialist.

## 3. What is established, what is inference, what is open

**Read `../ANALYSIS - Independent Review of Nov 18 (results and corrections).md` first.** It is the most recent and most carefully verified statement of the numbers and it governs over every earlier memo. Each earlier memo that it corrects carries a banner saying so.

Established to the dollar from the ledgers and return pages (each re-derived by two independent passes):
- The founder's receivable/payable position under four versions of the books (review memo §1).
- 2025 Schedule L loans to shareholders $294,256 = Finaloop opening $237,886.89 + James $56,368.76; the $74,363.80 gap to QuickBooks = $69,033.00 + $5,330.80.
- 2025 Form 1120 line 13 ($62,919) = Gusto wages $131,952.09 − $69,033.00.
- Cash paid to the founder or his personal creditors by year, 2020–2025 (`../ANALYSIS - Cash Paid to the Founder (Rebuilt).md`, as corrected) and $49,191.55 for Jan 1–Jul 22, 2026.
- The S-termination statement's date (January 1, 2025) against the agreement dates, the deposit dates, and the 2024 return's paid-in capital and share counts.
- 2025 other income composition; 2024 and 2025 card balances written off to income.

Inference (state it as such):
- That Finaloop's $157,115.47 opening line "contains" AJE-547. It is an exact arithmetic match, not a label.
- That the $4,600 received May 1, 2026 is part of Blake's 7,500 USDC loan.
- That Mark's September 30, 2026 column is a Finaloop export.
- That $3,320 of written-off accruals was interest on the Nguyen note.
- That the card accounts paid from company funds are personal cards.

Open (see review memo §8): Mark's $208,100, payables, inventory and "Other" notes at September 30; the six 2024 shareholders; what Mark edited in AJE-547; filing status of the returns; anything after July 23, 2026.

Testimony, not documents (review memo §6): what Jeremiah said to Blake in April, on July 21 and on August 24, 2026; that neither Blake nor Comatri received a K-1 or sent $4,600 as capital.

## 4. Map of the repository

| Path | What it is |
|---|---|
| `Financials/Quickbooks/` | General ledger export (Jan 1, 2020 – Mar 27, 2026), official P&L-by-month exports 2014–2026, balance sheet, audit logs 2020–2026, invoices and payments |
| `Financials/Finaloop/` | Finaloop general ledger, Dec 31, 2025 opening – Jul 23, 2026 (Apple Numbers file) |
| `Jer to Investors/` | Everything management sent investors, by date: Oct 2024 pitch materials, Jan 2025 budget workbook (contains Mark's "Jer Accts" tab), July 2026 "State of the Business" (two versions), cash plans, Aug 24, 2026 briefing, and `2026-11-18 - From Hugh/` (three tax returns, two K-1s, Mark's draft P&L and balance sheet, Hugh's question sheet) |
| `Comatri Investment Agreements/`, `Jer to Investors/2024-07-21 - Comatri Agreement 1/` | The two signed agreements with the operating agreement attached |
| `Correspondence/` | Mark's text to Hugh; the April 29, 2026 loan texts |
| `ANALYSIS - *.md` | Memos, one topic each. Start with the Nov 18 review memo, then the rebuilt cash memo, then the tax-returns memo |
| `BRIEF - *.md`, `NOTES - *.md` | Meeting briefs, the timeline, counsel shortlist, QuickBooks export checklist |
| `DRAFT - *` | Reply to Hugh (final as of Nov 18), email to prospective counsel, the joint records request (v4, needs counsel review) |
| `ARTIFACT - *.html` | Source of the two published pages (financial analysis; Mark Clark ledger access record) |
| `HANDOFF/` | This package: `CITATION-INDEX.md`, `CORRECTIONS-LOG.md`, and `process/` |

`HANDOFF/process/`:
- `scripts/export_ledgers.py` — turns both ledgers into flat CSV. Run: `python3.13 export_ledgers.py <repo> <outdir>` (needs `pandas`, `numbers-parser`).
- `derived-data/` — its output, gzipped, plus Finaloop's two index tables and a text transcription of Mark's draft.
- `return-page-images/` — the scanned returns rendered to PNG (`pdftoppm -r 110 -png`). The PDFs have no text layer and no OCR engine was available; figures were read from these images.
- `workflow/` — the Nov 18 multi-agent review: the briefing given to agents (`README_FOR_AGENTS.md`, `returns_extract.md`), the orchestration script, the full structured result (`workflow_result.json`), one readable file per reviewer with verdicts, and the journal.
- `scripts/agent-scripts/` — the pandas scripts each agent wrote. Uncurated working files; useful for re-running a specific tie-out.
- `scripts/hugh_summary_v2.html` + `scripts/make_pdf.js` — source and renderer for `Bravado Spice - Summary for Hugh (2026-11-18).pdf` (six questions, each with background and numbered sources). Run: `node make_pdf.js <html> <pdf>`. `hugh_summary.html` is the earlier three-page version.
- `scripts/build_source_appendix.py` + `scripts/render_many.js` — builds `Bravado Spice - Source Appendix (2026-11-18).pdf` (137 pages): Exhibits A to J are the cited documents in full; K to N are line-by-line ledger and report extracts; O is the founder-cash computation. Its index maps the summary's source numbers 1 to 32 to exhibits. Run: `python3.13 build_source_appendix.py <repo> <dir with unzipped derived-data> <work dir> <out.pdf>` (needs `pandas`, `openpyxl`, `pypdf`, `reportlab`, node with Playwright, and LibreOffice for the one .docx). Choices made in the appendix: healthcare merchant names are replaced with "[healthcare provider]"; the audit-log extract shows only the February 26, 2026 creation events for AJE-547 (later edits are in the full log, and the extract says so); the private loan texts, the privately shared July version and the analysis memos are not included; a by-vendor accounts-payable table from QuickBooks was dropped because it did not tie to the Finaloop opening balances without further work.

## 5. Traps in the data

- **Signs are account-natural** in both ledgers: asset debit +, liability credit +, expense +, bank outflow −. In QuickBooks, `33500 Due to Jeremiah` with a negative (debit) balance means he was paid more than was documented.
- **QuickBooks multi-line journal entries** show a blank or "-Split-" offset. Find the other legs by `num` + `date`.
- **QuickBooks stops March 27, 2026** (ledger); the audit log continues. The 2026 audit-log file omits the year in its timestamps. Deleted users retain only sign-out events.
- **Finaloop has no user or actor field.** Who made an entry cannot be determined. Its export is out of balance by $5,872.88 (April 7 and April 15, 2026).
- **Finaloop's P&L signs:** income accounts positive; discounts, refunds and all expenses also positive. Classify before summing.
- **"Credit card (9532)" is James Nelson's card**, not the founder's. Check 2418 (Sept 2020, $14,078) was James's tax, though first booked to the founder's draw. Check #7590 (Jan 2026, $3,250) went to a third party though Finaloop books it as the founder's distribution.
- **Mark's draft mixes ledgers:** 2024 column = QuickBooks before the CPA's April 2025 entries; 2025 column = QuickBooks final; September 2026 column = Finaloop-based.
- **The returns are cash-method** (2023, 2024 marked; 2025's page 4 is missing). "Purchases" is a balancing figure. Book-versus-return differences are mostly method, not error; the exceptions are documented in the review memo §3.
- **Founder W-2 pay for 2021–2022** is inside lump Gusto entries and cannot be separated by person.

## 6. Suggested next steps

1. Record what was said at the November 18 meeting against each question in `../DRAFT - Reply to Hugh (Nov 18 meeting questions).txt`, and test each answer with the "document that settles it" column in the review memo §7.
2. Obtain: all six 2024 K-1s; the 2025 Form 1120 page 4 and e-file acknowledgements; the Finaloop export behind Mark's September column; A/P aging and inventory count at September 30, 2026; the Gusto register by employee; the AJE-547 attachment; the Finaloop onboarding correspondence.
3. Tax specialist: effective date of the S-election termination and whether 2024 must be refiled; treatment of shareholder loans in a C corporation; the written-off card balances.
4. Counsel review of the records request before delivery.
5. If new ledgers arrive, re-run `export_ledgers.py` and extend the founder-cash series past July 22, 2026.

## 7. Published pages

- Financial analysis: https://claude.ai/code/artifact/8385ef27-3b75-4f68-8c0e-633a848cc44a (source: `../ARTIFACT - Bravado by the Books.html`; last revised Nov 18, 2026).
- Mark Clark ledger access record: https://claude.ai/code/artifact/32cb5ded-4dc1-45c1-aa36-80411e1579a9.

The full conversation transcript is deliberately not included: it contains private messages and legal strategy. `CORRECTIONS-LOG.md` records the reasoning that matters.
