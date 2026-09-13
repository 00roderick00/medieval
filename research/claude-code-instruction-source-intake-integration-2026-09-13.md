<!--
Filed: 2026-09-13
Origin: Claude (Cowork), at Roderick's request ("what shall i tell claude
code to do?"), after the two-batch September intake was read and assessed
(research/corpus-intake-assessment-2026-09-13.md; research/assessments-
2026-09-13/). This is the Claude Code instruction for the INTEGRATION run:
it moves the assessments' findings into the provenance chain without
touching any draft.
-->

# Claude Code instruction — Source-intake integration run (September intake, both batches)

Read CLAUDE.md, spine.md and research/claude-code-instruction-source-intake-template.md before starting. This run replaces the second reading that the discovery-mode instruction would otherwise perform: the forty-nine works of the September intake have already been read and assessed, with page pins, in research/assessments-2026-09-13/ (thirty-nine assessment files, twelve of them prefixed 2026-09-13b-), and the synthesis is research/corpus-intake-assessment-2026-09-13.md. Your job is to carry those findings into the manuscript's provenance chain — sources.md, memo Revisions, critiques.md, the retrieval ledger — and to prepare the ruling sheet, without editing any draft.md, spine.md, CLAUDE.md, brief.md or outline.md.

## Boundaries for this run

Nothing in research/ is a manuscript source. The assessments are your map, not your authority: every sources.md entry, every memo Revision and every flag closure must cite the work itself, at the pin the assessment supplies, and you must open the corpus text at that pin before you write the entry. Where an assessment says a quotation must be re-verified against the page image, record the entry as PENDING VERIFICATION rather than closing the flag. Omission over invention throughout.

Drafts are frozen. Register changes listed in synthesis §5(a)–(t) are for Roderick's ruling; do not apply any of them to a draft, and do not apply corrections of fact (§4) to drafts either. Corrections go into the chapter memo under a Revisions entry and into critiques.md; the draft is corrected in the renovation pass after the rulings.

Commit after each chapter, message stating chapter, files, change; push to origin main is Roderick's. Never force-push.

## STEP 0 — Inventory

Confirm every work in corpus/retrieved/ that the synthesis §1 names is present as a text sidecar or PDF, and record in retrieval-master.md, with the intake date 2026-09-13, the status of each. Three special cases: the Nicholson file (*Love, War and the Grail*, Brill 2001) is the wrong book — move it to archive/ with a note, leave the retrieval row for Nicholson 1993 or Forey 1992 OPEN, and take nothing from it beyond the one ch01 dating correction the assessment records; the Eisenstein file is the Chinese translation — its rows are annotated "pins usable, quotations must be re-quoted from the English edition," and no Eisenstein quotation enters any sources.md; the Paston file is Gairdner 1872 vol. I, not the 1904 library edition — every existing Paston citation in ch08 given as "vol. II" or by 1904 letter number must be re-pinned to this edition's letter number and page, with Davis kept as citation of record when retrieved.

## STEP 1 — Chapter by chapter, from the assessments

Work the chapters in this order, because it is the order in which the batch bears on them: ch06, ch11, ch10, ch08, ch07, ch04, ch02, ch05, ch12, ch01, ch03, ch09, appendix-b, appendix-c, coda. For each chapter:

1.1 sources.md. Add every assessed work the assessment places in that chapter, at its tier (T1 for Cosneau's pièces, the Paston Letters, Belloc, Fortescue, Basin; T2 for the monographs and articles; T3 for Gairdner's Introduction and other trade material), with the pins the assessment gives and the assessment's placement note ("ally with the Colleoni correction," "rival on causation," "witness testifying against his own frame," and so on) as the entry's use-note. Record publication date and any later scholarship that supersedes the work, as CLAUDE.md §5 requires. Where the assessment names the two sides of a scholarly dispute (Rogers v. Parker; Dean v. Zorzi; Eisenstein v. Johns; Griffiths v. Harvey/Bohna on the Cade pardon roll; Wolffe v. Grummitt on the chamber; Hale/DeVries v. the technological-determinist reading), record the dispute in the entry.

1.2 memo.md. Under the Revisions heading, one dated entry per work or pair of works, PENDING HUMAN REVIEW, in three parts: what the work confirms (with pins), what it corrects (with the manuscript's current wording quoted and the correction stated — but not applied to the draft), what it adds and where. Keep the assessment's distinction between scholarly consensus, contested interpretation and the book's own argument. The five findings in synthesis §3 and the five in §3b each get their own entry in the chapter they touch.

1.3 critiques.md. Enter every "What it CONTRADICTS" section that reaches argument level as a named objection, steelmanned at the strength the assessment gives it, with the assessment's "best answer" as the chapter's answer and the assessment's grading of that answer (good / adequate / plausible-unproven) preserved. The ones that must not be missed: Lane on "proto-state" and on a fisc driven by war not cannon (ch04, ch10); Depreter on the incomplete Burgundian fisc (ch10); Ágoston with Kafadar and İnalcık on Ottoman devolution (ch11); Elliott 1992 on the durable composite (ch11, ch12); Payling and Baker on "outspent" (ch08); Johns and Eisenstein on print as not capital-intensive and on the crown losing the medium (ch11, ch12); Barker's deflationary reading of the Normandy sieges (ch06); DeVries's Hale frame and "ratchet" collision (ch06, ch10); Lander on England without a fisc (ch11); Morris on jurisdiction not sovereignty (ch02); Hoffman's price series, Tilly's direct-rule sentence, Strayer's trellis, Scheidel's episode, Spruyt's starting gun, Parrott's contractor-state, Sharman's company sovereigns, Zielonka's fiscless bloc, Varoufakis's co-rentier, Freedman's "decisive" (from the first batch, where not already entered).

1.4 Flags. For every [GAP], [VERIFY] or [SOURCE] flag in the chapter's draft that an assessment closes, record the closure in the memo Revision with the pin, and mark it CLOSABLE AT RENOVATION; do not edit the flag in the draft. Where an assessment closes a flag negatively (the Cade pardon roll; the Howard sentence; the bocche di leone; the twelve thousand of Rouen; the Colleoni captaincy; the Hussite material in DeVries), record it as RE-SOURCE OR CUT with the assessment's recommendation.

## STEP 2 — Cross-chapter ledgers

2.1 research/outstanding-sources.md and retrieval-master.md: add the rows in synthesis §8 (both paragraphs) with the reason each is wanted and the chapter that is blocked on it; flip IN REPO for all forty-nine intake works; note the three special cases from STEP 0.

2.2 appendix-b: enter the Venetian row from Lane's c. 1500 budget and Lane and Mueller's 1469 breakdown, the papal fisc from Morris, and the Ottoman "conversion failed" cell pinned to Ágoston pp. 121–23 — in the appendix's memo as Revisions, not in its draft.

2.3 appendix-c: enter, in the memo, the candidate indicators the synthesis names (Hoffman's falsifier; Scheidel's capstone sub-wager; Andrade's breakable-defence condition; Johns's steam threshold as the capital-intensity test for a medium) with their sources, and mark each NEEDS BASELINE where no dated baseline is yet sourced; generate no indicator without one.

## STEP 3 — The ruling sheet

Write research/rulings-sheet-2026-09-13.md: one row per register decision in synthesis §5(a)–(t), giving the decision in one sentence, the draft sentences it would change (chapter, section, quoted), the works that carry it (with pins), whether it touches spine.md or CLAUDE.md (mark those: (b), (d), (k), (n)), and a blank RULING field for Roderick. Add a final row for each RE-SOURCE OR CUT item from STEP 1.4. Do not recommend; state.

## STEP 4 — Assembly and report

Run tools/assemble.py, confirm no draft changed (word count and flag count unchanged from the last assembly), update research/master-status.md, and write a closing report to research/intake-integration-report-2026-09-13.md: chapters processed, entries added per file, flags marked closable, flags marked re-source-or-cut, rows added to the retrieval ledgers, anything the assessments claimed that you could not find at the pin (list these; do not resolve them yourself). Commit.

The next run, after Roderick fills the ruling sheet, is the renovation pass: rulings into spine.md by Roderick, then the draft corrections and register changes applied chapter by chapter, with ch06 and ch11 first.
