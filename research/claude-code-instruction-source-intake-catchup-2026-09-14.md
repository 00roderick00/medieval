<!--
Filed: 2026-09-14
Origin: Claude (Cowork), at Roderick's request ("I've added a lot in
recently so it needs to catch up. Understand what's been added and add
it all into the project"). Thirty-one files arrived in corpus/retrieved/
after the STEP 0 inventory of 13 September. This instruction takes them
from files on disk to entries in the provenance chain.
-->

# Claude Code instruction — Source-intake catch-up run (arrivals of 14 September)

Read CLAUDE.md, spine.md, research/claude-code-instruction-source-intake-template.md, research/claude-code-instruction-source-intake-discovery.md, and research/assessments-2026-09-13/00-READERS-BRIEF.md before starting. This run does for the 14 September arrivals what the 13 September runs did for the forty-nine works before them: inventory, text-extraction, reading and assessment against the manuscript, then integration into sources.md, memo Revisions, critiques.md and the ledgers. The assessed-then-integrated pattern is the one to follow, with the assessment files written first (into research/assessments-2026-09-14/) and the integration written from them.

## Boundaries

Drafts are frozen: do not edit any draft.md, spine.md, CLAUDE.md, brief.md or outline.md. Corrections and register changes go into memo Revisions (PENDING HUMAN REVIEW) and critiques.md, and any new register decision is appended as a new row to research/rulings-sheet-2026-09-13.md (continuing its lettering after (t)). Every entry cites the work at its pin, having opened the text at that pin; the assessment files are your map, never your authority. Omission over invention. Commit after each unit; message states files and change; never force-push; push is Roderick's.

## STEP 0 — Inventory and extraction

0.1 List every file in corpus/retrieved/ with a modification time after 2026-09-13 18:00 (Pacific). Expected: Suleyman, *The Coming Wave*; the nine contemporary primaries (DMA, DSA, AI Act, eIDAS 2.0, EDIP proposal COM(2024) 150, CHIPS and Science Act, GENIUS Act, NDAA FY2026 enrolled text, the NATO Hague Declaration as .md); Miller *Chip War* EPUB; Farrell & Newman article (two copies) and *Underground Empire* EPUB; Ruggie 1993 (two copies); Scott, *Seeing Like a State*; Wu, *The Master Switch* EPUB; Schmitt, *Nomos of the Earth*; Krasner; Ertman; Stasavage EPUB; Commynes (Calmette ed.); Cheung; Chastellain *Œuvres* vols 1, 9, 11, 15; Glete. Record each in retrieval-master.md under a new dated section, flipping its row to IN REPO with the date, and classing it per the discovery instruction: (a) on ledger, now arrived; (c) unlisted arrival — Suleyman is one, create its row; (d) unreadable as found.

0.2 Duplicates: keep one copy each of the Farrell & Newman article and Ruggie; move the other to archive/ with a note. Miller *Chip War* is already IN REPO and assessed as a PDF; record the EPUB as a second copy and use it only if its pagination is better — do not re-assess.

0.3 Identify what the multi-volume and edition files actually are before anything else: which tome(s) of Calmette's Commynes the PDF contains (the ledger wants vol. II, 1474–83, for Louis XI's later reign and the revenue figure); which books of Chastellain fall in vols 1, 9, 11 and 15 of Kervyn de Lettenhove and whether they cover 1449–53 and the Burgundian court; whether the Glete file (156 MB) has a text layer. Record findings in the ledger; if the Commynes is the wrong tome or the Chastellain volumes miss 1449–53, leave the row OPEN with the exact volume wanted, as was done for Nicholson.

0.4 Text-extract everything into corpus/retrieved/source-library/text-2026-09-14/ (gitignored): pdftotext for PDFs with text layers; for EPUBs unzip and strip HTML (pandoc if present); OCR (pdftoppm 200 dpi grey then tesseract, serial) only where a PDF has no text layer — Chastellain and Glete are the likely cases; check with pdffonts first. Record the page-offset rule (PDF page = printed page + n) for each file at the head of its sidecar.

## STEP 1 — Assess (books and articles)

For each of the fourteen scholarly works (Suleyman, Farrell & Newman book and article, Ruggie, Scott, Wu, Schmitt, Krasner, Ertman, Stasavage, Commynes, Cheung, Chastellain, Glete), write research/assessments-2026-09-14/<Author>.md in the form of the 13 September assessments — the book in two paragraphs; what it confirms, corrects, adds and contradicts, each with verbatim quotation and pin (PDF page / printed page); placement by chapter and section; verdict — against spine.md, CLAUDE.md §§1–6 and the current assembled manuscript. Read the whole work where it is under 300 pages; otherwise read the parts that touch the project and say which. Six works per session at most; keep the ledger as memory between sessions. Particular questions each must answer:

Scott — where "legibility" (28 uses in the manuscript) departs from his sense; whether his account of resistance to legibility (mētis) supplies the interstitial-disorder argument of Part III. Wu — the cycle against ch12's twelve American cases; whether "the switch" as the book uses it is his or the book's, and the ledger check the voice rule requires. Farrell & Newman — whether weaponised interdependence is the mechanism's contemporary form or a rival to it; the panopticon/chokepoint distinction against the compute and payments stacks. Ruggie and Krasner — Appendix A lineage; what each concedes to Bull and denies. Schmitt — the *Grossraum* source for ch12's hemispherical reading; the disanalogy the book must state. Stasavage — city-state credit against Lane's Venice; whether his size argument bears on the bloc thesis. Ertman and Glete — where each sits against Tilly, Spruyt and Hoffman in ch10 §VII's critiques; Glete's naval/army distinction for the Tilly answer. Cheung — the Chinese bloc's stack as state project; baselines for Appendix C. Suleyman — a T3 witness; record what, if anything, a chapter could use, and note the containment thesis as a scoreable prediction. Commynes and Chastellain — T1; verify every existing Commynes and Burgundian-court citation in the drafts against the text, and list what the chapters do not yet use.

## STEP 2 — Verify (the nine contemporary primaries)

Primary documents are not assessed; they are checked. For each, find every place a draft or memo cites or paraphrases it (grep the chapter folders for DMA, DSA, AI Act, eIDAS, EDIP, CHIPS, GENIUS, NDAA, Hague), open the text at the article, section or paragraph relied on, and record in the chapter's sources.md a T1 entry with the exact citation form (Regulation number, article and paragraph; Public Law number and section; declaration paragraph) and a note MATCH / MISMATCH / NOT FOUND for each draft claim. Mismatches go into the memo Revisions as corrections, not into the draft. Where a draft cites the instrument for something it does not contain, say so plainly and mark RE-SOURCE OR CUT. For eIDAS 2.0 and EDIP, which the drafts do not yet cite, record in the ch12 and appendix-c memos what each instrument could carry (the European identity stack; the fiscal-military instrument's baseline) as ADDS, with article pins.

## STEP 3 — Integrate

Chapter by chapter, from the assessment files and the STEP 2 checks, exactly as the 13 September integration run did (research/claude-code-instruction-source-intake-integration-2026-09-13.md, STEP 1.1–1.4): sources.md entries at tier with pins and use-notes, memo Revisions entries, critiques.md objections steelmanned with graded answers, flags marked CLOSABLE AT RENOVATION or RE-SOURCE OR CUT — never edited in the draft. Order: ch12, appendix-a, appendix-c, ch01, ch10, ch11, ch04, ch05, ch03, ch08, coda. Appendix A's annotated bibliography memo gains Ruggie, Krasner, Goldsmith & Wu (when it arrives) and Farrell & Newman as lineage entries.

## STEP 4 — Ledgers, ruling sheet, assembly, report

Flip every row; note what is still OPEN from the 14 September additions (McNeill; Goldsmith & Wu; Tilly 1975 and 1985; Samaran tome II; the EUR-Lex EDIP regulation if adopted; anything STEP 0.3 found wanting). Append new register decisions to the rulings sheet with the same columns as (a)–(t). Run tools/assemble.py and confirm no draft changed (66,961 words; 111 flags). Write research/intake-catchup-report-2026-09-14.md: files inventoried and classed; sidecars made; assessments written; primaries verified with match/mismatch counts; entries added per chapter; flags marked; rows flipped and rows still open; anything an assessment claimed that could not be found at the pin. Commit.
