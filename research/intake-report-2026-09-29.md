<!--
Filed 2026-09-28 by Claude Code, closing the intake of Jill Lepore,
*The Rise and Fall of the Artificial State*, per the instruction of this
date. Reflective document — outside the provenance chain; nothing here
may be cited. Every chapter entry it reports is PENDING HUMAN REVIEW.
(Filed under the instruction's filename, which dates the arrival
2026-09-29; the repository clock read 2026-09-28 throughout the run.)
-->

# Intake report — Jill Lepore, *The Rise and Fall of the Artificial State*

## Identification (STEP 0)

**The book is Lepore's, and the standing row is closed — but not from the
title page.** The capture (`corpus/retrieved/The Rise and Fall of the
Artificial State.pdf`, 306 pages, 160 MB, Adobe Scan for iOS 26.08.31)
contains **no title page and no copyright page**: it runs jacket flap,
epigraphs, contents, preface. The instruction's caution against assuming
the Lepore row was therefore the right caution, and it had to be
satisfied another way.

Authorship is conclusive from the book's own **About the Author page at
PDF 204** — out of sequence, because jacket material is interleaved with
the text: "JILL LEPORE is the David Woods Kemper … Professor of American
history at Harvard University, professor of law at Harvard Law School,
and a staff writer at The New Yorker. Her many books include the New York
Times bestsellers *These Truths* and *We the People*." Corroborated from
inside the text: the book's core is "the 2026 Tanner Lectures on Human
Values at Yale"; she names the Priestley Lectures at Toronto and the
Hegel Lecture at the Freie Universität Berlin, "classes I have taught at
Harvard", a BBC radio series, and the New Yorker essay on disruptive
innovation whose publication drew Marc Andreessen's tweet; the notes
self-cite *If Then*, "The Disruption Machine", "We, the Robots" and "The
World According to Elon Musk's Grandfather". The jacket flap reads
"PULITZER PRIZE-winning author of WE THE PEOPLE".

**Not established, and now an open row: publisher, place, edition and
year.** The copyright page was never photographed. No entry anywhere may
give an imprint or a date, and none does. Internal evidence puts the book
in 2026 or later.

## The OCR decision (STEP 0)

**The embedded Adobe layer was rejected as not citation-grade**, on the
instructed twenty-page sample. Two findings decided it: alternating pages
are unreadable (PDF 5, 6 and 8 are noise, PDF 8 being a garbled duplicate
of PDF 7's text), and **PDF pages 201–306 carry no text at all** — the
entire endnote apparatus, which is where provenance lives, was absent.

Re-OCR'd this session, serially, `pdftoppm -r 200 -gray -png` plus
`tesseract --psm 3`, all 306 pages, into the gitignored sidecar
**`corpus/retrieved/source-library/text-2026-09-29/ArtificialState-ocr.txt`**
(103,890 words; every page prefixed `[[PDF p. N]]`).

**The page-offset rule is that there is no usable rule.** Measured from
running heads, printed ≈ PDF − 10 to − 12 through the main text (drifting)
and printed = PDF − 18 to − 19 in the notes, with jacket material
interleaved out of sequence. **No pin may be computed from an offset:
every printed page must be read off the running head on its own page**,
and every entry carries both printed and PDF page. **All pins are
provisional** — a phone scan, OCR'd by us — and must be re-verified
against a printed copy before press. Recorded at each sources.md entry.

Structure, corrected at integration: Part Two's opener at printed pp.
117–130; the Epilogue at 225–228; **the main text ends at printed p. 228 /
PDF 246**; endnotes 229–287, the last captured page. The index was not
captured.

## What the five questions returned (STEP 1)

**Tier: T3** for the contemporary chapters — the ones the project needs —
because they are interpretive essay built from journalism, public
statements and manifestos rather than archival or peer-reviewed work, and
because no imprint can be given. Two carve-outs: her historical chapters
(the census and statistics, Technocracy Inc., Simulmatics) rest on her own
archival research and carry T2-strength narrative fact; and her endnotes
let almost every claim be re-pinned one step to its own primary. Standing
use-note entered: **take the sentence from her, the citation from her
note, cite the primary**; she is never sole support for a structural
claim.

**1. "The artificial state" is not this book's object; it is its
inverse.** Her definition is by negation — "less a state than a dream of
being without one, the dream of the severing of humans not only from the
natural world but also from one another, every umbilical cord cut"
(printed p. xv) — and expansively, "the rule of humans by machines
manufactured by corporations". Greps of the whole main text return **zero**
for foundry, TSMC, CHIPS, chip, export control, Anduril, Starlink,
Starshield, Pentagon, procurement and licensing: her Artificial State
contains no decisive force, its military limb being one sentence about
firms making technologies "available to the military". Her direction of
travel is the reverse of the book's: "Democracy and the liberal
nation-state had to be abolished to free corporations from the restraining
force of any government" (printed p. 205). **A title collision, not an
agreement**, and the discipline is entered as a use-note: she may never be
cited as a synonym for, or as support for, the artillery state or the
consolidated state.

**2. The second-reader's question comes back a clean negative — and that
is a finding, not a gap.** She gives no account of public authority
expanding over private technology in a democracy. Her causal claim is
abdication: it "played out the way it did because of the failure of liberal
democracy to limit corporate power over politics and government" (printed
p. 69). Every instrument she names is one of withdrawal — the Office of
Technology Assessment closed, the 1996 Telecommunications Act, an AI
Action Plan relieving AI infrastructure of environmental review. In AI.GOV
the state adopts the industry's prose, not its discretion ("The nation is
in Silicon Valley's hands", printed p. 222), and the countercurrents she
frames as capture. Her only expansion cases are authoritarian, where
expansion plainly destroys consent. **The question the book was retrieved
to answer remains the book's own.**

**3. Assist against replace: administration against representation.** The
load-bearing sentence is at printed p. 38 / PDF 49 — Cold War computing
served military, intelligence and "government administration of everything
from welfare provision to national security. Only later would these tools
be applied, by private companies, as substitutes for the democratic
functions of representation, deliberation, and participation." It
**supports** ch12 §III's legibility paragraph and supplies the two-sided
formula the draft hedges ("The ability to count gave the state power; the
ability to be counted gave the people power", printed p. 94); it
**sharpens** §IV by supplying the criterion for claim 3(ii) — whether what
the state acquires is administrative capacity or the representative
function itself; and it **embarrasses** §IV's trust-busting sentence,
because her documented 2023–26 record is deregulation and the defeat of
antitrust reform.

**4. Her democratic resistance is cultural, local and individual, not
institutional — which is the answer Appendix C needed.** She names three
of the four falsifiers as *rights*: "everything destructive that they have
done can be undone by voters, elections, legislation, and judicial
enforcement" (printed p. 226). She names **none of the fourth** — no
public substitute for any supplier appears in the book — and gives no
instance of any of the three operating on a strategic commitment. Her live
resistance is "Grow tomatoes, not data centers" and "Unplug". One usable
anti-baseline for DC-2 (the abolition of the body that did technology
assessment) is entered **NEEDS PRIMARY FOR THE DATE**; her 2025 opinion
series are opinion, not control series, and are explicitly not scored.

**5. The coinage survives its third check.** ornament, ornamental,
façade, veneer, shell, hollow, husk, decorative, charade and sham as a
word: **all zero across 306 pages**. Near-hits reported honestly —
"trappings" of religion, "veneer" of Bostrom's prose, and one
"figurehead", which is Lepore's own sentence summarising Douglas Adams's
Zaphod Beeblebrox, "chosen not by voters but by the government to serve as
a diversion from its criminality" (printed p. 210). Her own terms are the
Artificial State, *automatocracy*, Masuda's *Automated State*, *digital
authoritarianism*, *datafication*; her note concedes *algocracy* as a
rival. Her nearest equivalent is **government without consent** — an input
concept where the book's is an output test. **Three predecessors, three
objects**: Crouch on egalitarian policy, Wolin on the regime, Lepore on
consent, the book on control of the state's strategic commitments.

## The two contradictions, and how they were graded

**It is not a state, and the direction is not consolidation.**
Corporations "began to subsume the state"; decisions are made by "a
handful of men"; "The nation is in Silicon Valley's hands". A working
historian reading the same 2025–26 record finds no licence, no procurement
lever, no export-control regime, no foundry and no munitions base worth a
paragraph. This reaches spine §6's DEFEND tier and the §8(b)/(c) ruling
that the American state will absorb the stack. The book's answer —
different objects; her own unturned hinges ("available to the military",
"sovereign AI", federally underwritten businesses); §7's compelled-not-
accomplished tense — is graded **adequate, no more**, and the reason is
recorded: it argues from her silences, and she has not tested the
absorption claim, so she is neither evidence against it nor for it.

**The three failures.** Found in her own material and sharper: the
National Data Center, OGAS and Cybersyn — three dated cases where a state
wanted the legibility stack, had the fiscal capacity, and failed, while
private firms built it. This reaches spine §8(g) item 4. Graded **good on
sequence, weak on the failures**, with the concession recommended in
terms: the mechanism predicts acquisition only where the capability is
decisive **and** the dependence inescapable.

## Entries added (STEP 2)

| File | What |
|---|---|
| ch12/sources.md | master block, ~45 pins each with printed and PDF page; tier and carve-outs; no-imprint citation form; offset and running-head rule; provisional-pin warning; four use-notes; both disputes; a NOT-TO-BE-USED list |
| ch12/memo.md | Revisions 31, with "The second-reader's question, answered", "Assist against replace", "The ledger, third check" |
| ch12/critiques.md | Revisions 21 (the file's last entry was 20, so the instruction's "22" would have left a gap — recorded), both objections steelmanned with grades attributed |
| ch09/sources.md, ch09/memo.md | POINTER entry naming ch12 as master; Revisions 13 — the figurehead subject, assist/replace as it bears on the efficient part migrating, and the statement that she gives ch09 nothing else |
| appendix-c/memo.md | Revisions against DC-1..6: three falsifiers as rights, the fourth absent, the resistance finding, the anti-baseline, the opinion-series exclusion |
| appendix-a/memo.md | full lineage entry; **the Lepore placeholder discharged** |
| research/rulings-sheet-2026-09-13.md | rows **(llll)–(tttt)** appended with blank RULING fields; ⚑SPINE on (oooo) §8(g)(6), (pppp) §8(g)(4) and (tttt) |

## Flags

**CLOSABLE AT RENOVATION:** only ch12 §III's `[ANALOGY-ONLY]`, and as a
**narrowing, not a closure** — printed pp. 38 and 94 supply a principled
stopping line (administration yes, representation no) but no mechanism for
episodic-to-continuous legibility. **Explicitly not closed:** §II's
Kantorowicz and Famiglietti/Autrand gaps (Blackstone narrows at one remove
only — RE-PIN OR OMIT); the Elton-debate gaps; §VIII's SpaceX
reported-only flag; the over-mighty-citizen ledger flag; ch09's
[OUTLINE CONFLICT]; the Wolin irreversibility concession. **RE-SOURCE OR
CUT:** none arising.

## Claimed but not found at the pin — eight items, all corrected

The integration pass audited the assessment against the sidecar and
corrected it. Recorded because the audit is the point:

1. **"Zero occurrences of CHIPS, chip, export control" is true of the main
   text only** — "Despite US export controls on advanced chips, China's AI
   firms have adapted" stands in an endnote, inside a quoted World Economic
   Forum piece, at printed p. 256 / PDF 274–275. Substance unaffected;
   the claim is now stated as "zero in the main text".
2. **The 1995 abolition date is not at the pin.** She gives 1972 for the
   formation and dates the closure only by Gingrich's arrival as Speaker.
   Entered as NEEDS PRIMARY FOR THE DATE; **1995 is asserted nowhere**.
3. The Musk descent was pinned to a badly sheared, unquotable page;
   re-pinned to printed p. 97 / PDF 110.
4. The Durov sentence's legible text exists only at PDF 99; printed p. 88
   confirmed from the damaged duplicate's head.
5. "Seven assessment questions" — there are **six** question-sentences at
   printed p. 227.
6. The *figurehead* sentence is **Lepore's**, summarising Adams; only the
   inner phrase is his. Corrected in all three files.
7. "*sham*: three hits" — the third is "shambles"; **sham as a word is
   zero**.
8. A probable note-carrier for her unnamed 2026 survey was found — Yotzov
   et al., "Firm Data on AI", NBER, February 2026 (printed p. 286) — but
   the note-sequence association is an inference in damaged OCR, so the
   datum stays **unscored** and the survey **NEEDS VERIFICATION**.

Also owed and now done: retrieval-master.md's structure note corrected
(main text ends printed 228, not "about 237"; Part Two's opener and the
Epilogue pinned; the grep claim qualified).

## Record hygiene, for Roderick — not touched

`appendix-c/memo.md` carries the 2026-09-16 Wolin/Crouch DC block **three
times**, with the running STATUS line likewise. Deprecation is not this
run's authority (CLAUDE.md §7: deprecate to /archive, never delete), so
nothing was merged or removed. Two untracked files in `research/` from 16
September (`_rows2.md`, `Rulings-Sheet-II-2026-09-16.docx`) are not this
run's and were left alone.

## Assembly (STEP 3)

tools/assemble.py at close: **97,443 words, 270 endnotes, 133 flags**
(GAP 52, BRIDGE 19, RE-CHECK AT PRESS 16, TRANS. CLAUDE 46) — **identical
to the figures the instruction specified. No draft.md, spine.md,
CLAUDE.md, brief.md or outline.md was touched.**

## Next

Roderick's review of rows (llll)–(tttt) and of the PENDING entries. The
two that reach doctrine are (oooo), the three-predecessor clause at
§8(g)(6), and (pppp), the decisive-and-inescapable concession at §8(g)(4).
Outstanding retrievals from this intake: the imprint and year; a printed
copy for the provisional pins; a primary for the technology-assessment
abolition date; the NBER paper behind the 2026 survey.
