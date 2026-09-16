<!--
Filed: 2026-09-16 by Claude Code at the close of Part A of
research/claude-code-instruction-phase5-renovation-2026-09-16.md.
Interim report: Part B (ch09, ch12, the Coda, Appendix C, the
Introduction's wager, Appendix B) waits on the catch-up run's STEP 3
(research/intake-catchup-report-2026-09-14.md, absent at this
writing). Reflective document — outside the provenance chain; nothing
here may be cited.
-->

# Phase 5 renovation — Part A interim report (2026-09-16)

## What this run was

The first pass to edit draft.md files since the 3 September assembly.
It applied the rulings of 14 and 16 September (spine §8(g)/(h);
research/rulings-sheet-2026-09-13.md rows (a)–(cc) and R1–R9) to the
medieval chapters and ran the register pass across every draft. It
added no new works: every pin entered was already in the chapter's
sources.md, or is a POINTER to another chapter's master entry for a
work already in corpus (Vale 1974, Fortescue, Hall, Strayer, Johns,
Paston-Gairdner, Escouchy tome II — each pointer names the master).
Every edit is recorded in the chapter's memo under a dated Phase 5
entry with the old sentence, the new, and the pin; every such entry
is PENDING HUMAN REVIEW. Commits: one per chapter, in the
instruction's order where the forks allowed it (ch04 → ch08 → ch02 →
ch01 → ch11 → ch10 → ch07 → ch06 → register pass + assembly + this
report). Nothing pushed.

Part B is NOT run: research/intake-catchup-report-2026-09-14.md does
not exist. On Roderick's instruction of this session the catch-up
(sessions 2–3, STEP 3, STEP 4) is resumed next, and Part B follows
when that report exists.

## Assembly

tools/assemble.py at close: **80,169 words** (from 66,961 on 13
September), **265 endnotes** (from 224), **flags 117** (from 111): GAP
51 (from 55), BRIDGE 17 (from 16 — the one [BRIDGE — PROPOSED] in
ch11), RE-CHECK AT PRESS 15 (from 11), TRANS. CLAUDE 34 (from 29).
manuscript.md and research/master-status.md regenerated.

## Word counts and flags per chapter (draft.md, footer included)

| Chapter | Before | After | Δ | GAP | BRIDGE (of which PROPOSED) | RE-CHECK | TRANS. CLAUDE | OUTLINE CONFLICT |
|---|---|---|---|---|---|---|---|---|
| ch00-intro | 3,331 | 3,339 | +8 | 4 | 1 | 0 | 0 | — |
| ch01 | 4,578 | 5,147 | +569 | 7 | 2 | 0 | 0 | — |
| ch02 | 3,328 | 4,226 | +898 | 4 | 0 | 0 | 0 | — |
| ch03 | 2,859 | 2,859 | 0 | 7 | 0 | 4 | 1 | — |
| ch04 | 3,570 | 4,293 | +723 | 9 | 0 | 0 | 0 | — |
| ch05 | 5,937 | 5,937 | 0 | 6 | 5 | 0 | 1 | — |
| ch06 | 13,734 | 16,611 | +2,877 | 9 | 7 | 7 | 22 | — |
| ch07 | 5,015 | 7,266 | +2,251 | 8 | 3 | 0 | 0 | — |
| ch08 | 4,398 | 5,687 | +1,289 | 5 | 4 | 0 | 1 | — |
| ch09 | 3,316 | 3,316 | 0 | 4 | 0 | 0 | 0 | — (Part B) |
| ch10 | 8,559 | 11,280 | +2,721 | 13 | 7 | 3 | 15 | — |
| ch11 | 4,667 | 8,234 | +3,567 | 4 | 8 (1) | 3 | 0 | 1 (memo) |
| ch12 | 6,678 | 6,763 | +85 | 3 | 1 | 6 | 0 | — (Part B) |
| coda | 2,263 | 2,266 | +3 | 0 | 1 | 0 | 0 | — (Part B) |

The growth is ruled matter throughout (rewritten sections grew to
what the rulings needed); the ch07 fork notes its §VII inventory
paragraph as the candidate cut if Roderick judges the growth
excessive; the ch11 growth is the price of re-dating England,
rewriting the Ottoman section to end in devolution, and itemising
the barons' losses. The ch06 footer's word-count line still reads
"~11,000" from July and is superseded by the memo.

## Rulings applied, by chapter (old → new, summarised; full record in each memo)

**A1 — ch06** (memo Revisions 28; commit 87c957e). (aa) §I and §VII:
"controlled comparisons" and "as near a controlled experiment" gone;
the proof restated as an organised system — guns, powder, gunners'
pay, carriage, siege pay, on permanent taxation — making resistance
unaffordable whatever a garrison's circumstances, with Burgundy,
Venice and the Ottomans named as the mechanism's test. (a)
establishment/entry/standing cost throughout; "no subject could pay"
→ "no subject could sustain it as a standing, provincial-scale
instrument at campaign tempo"; "No baron had this. No city had this"
narrowed to the establishment, with Ghent's two hundred carts (1382)
and Nuremberg's calibres (1462) conceded (Hall pp. 49, 95); the 1442
figure carried as "more than twice" (Rogers ed. p. 74). Barker's
distinction entered in §IV: guns documented on the wall (Argentan's
cart-sized hole p. 389; Caen's mined tower p. 397; Bayeux "to rubble"
p. 396; Avranches with both durations p. 396) against purchase and
hunger (Cherbourg sold pp. 399, 401; the Grey Tower starved p. 383;
Château Gaillard p. 394); the English ledger (Dieppe's two hundred
guns p. 302; Somerset's train at Avranches p. 312; Kyriell's train p.
394) as the losing side's proof that the object was the institution.
(d) §V: Fortescue as the longbow theorist in person — the defeated
saw the fiscal apparatus, called it tyranny, did not see what it
bought (Plummer pp. 114–17, 137). (y) §VI: Talbot recast as the
expert whose system stopped supplying the means; his competence left
mixed and unresolved in Roderick's terms (lost battles, famously the
last; "vaillant chevallier et sage en armes" in Escouchy ii. 64; the
Shakespearean afterlife via Pollard ch. 1); the Caen plot (Vale p.
138) as proof the train was an intelligible target, not of his
intention. (r) Belloc cited by name with B. T. B. (p. 41) for the
syndrome, paired with Talbot; "prophets of the knock-out blow"
detached to Freedman (pp. 55–57) and Holman (retrieval). (s) DeVries
defused at first citation (XVIII 470; Hale at XVI 128–29). R2: the
invented Howard sentence removed and its removal stated; the dissent
restaged on Howard pp. 30–31, DeVries X 348 / XVI 132–33, Hall pp.
117, 131; Basin's temerity recorded as a stock verdict (Samaran i.
76, 92, 176–78) with the Quicherat/Samaran [RE-CHECK]. R4: the twelve
thousand cut. R7: RESOLVED AT THE SOURCES — Escouchy tome II read at
pp. 64–67: the town stormed Wednesday 19 September (the weekday
checks), the castle composed, Benauges' capitulation 27 September in
Beaucourt's note (matching Hall's date); Vale's 17 September left
unreconciled and flagged; the superlative narrowed to the town.
Corrections of fact: Formigny (Kyriell 2,500 + 1,800; the culverins
carrying both readings; 3,774 in fourteen grave pits), Fougères as
London policy, 50,000 saluts, Fauconberg, the trebuchet's high arc,
corned powder "kept and burned better," iron shot 1453, Bureau mayor
from 1451, Rogers restaged on what he refuses (a single hinge; p.
56). (i) the people's weapon re-pointed from the longbow to the pike,
crossbow and hand-gun (Hall pp. 20, 38). [GAP]s closed: English
Heritage (Hall p. 14), the tipping point (Rogers ed. pp. 67–73, Hall
p. 58, DeVries XI 122–23), Rouen 1418–19, Howard, Freedman/Belloc,
Cadillac.

**A2 — ch11** (memo Revisions 9; commit bb470ca). (k) England
re-dated to the 1530s, the dissolution its fisc ("contains a
universalist power" carried as the book's argument, [BOOK'S
ARGUMENT]); Henry VII the pre-settlement case — Lander's tallies and
the cancellations of 1509–10, Grummitt's chamber (a reserve of
deposit treasuries, spent on the Cornish rising of 1497; not a
Yorkist continuation; not a personal ledger); "retained, to the
letter, his father's machine" gone; Bergavenny corrected to Lander
(the 1390 rank rule; two-thirds of a year's revenue; probably paid
once). (g)/(m) §IV rewritten as administrative-state-before-artillery,
artillery locking it, ending in devolution (Ágoston pp. 121–23);
Çandarlı re-dated to late summer, ulema-origin; the kul system
completed not created; the janissary growth stated; §V exempts the
Ottomans by name. (h)/(n) Castile the consolidated core of a
composite; the DEFEND-tier claim narrowed to sustaining decisive
force; all four consolidators stated as composites, subordinating the
core's intermediaries and ruling the rest aeque principaliter
(Solórzano verified at Elliott 1992 p. 53); the Habsburgs inherited.
(p) print: the harness the canon and the register; "chartered a guild
that took enforcement, and much else, into its own hands" (Atkyns's
"Petit State"); fifty-three houses, sixty-two by 1705, 1695 "never
again restored"; the disanalogy stated as one the mechanism survives;
the quo warranto held for ch12 by pointer; one [BRIDGE — PROPOSED]
(steam, not Gutenberg). (v) §VII itemises the five discretions lost
with Fortescue's instruments, Lander's Bergavenny and Lane's Colleoni;
[GAP — Part B: Chastellain t. III, Alençon]. R8 cut. [OUTLINE
CONFLICT] flagged in the memo: the outline's ch11 brief casts Henry
VII as "the technician of consolidation" (window 1470–1530) and the
devşirme as the century's most successful answer to the over-mighty
subject; the rulings contradict both; the draft follows the rulings.

**A3 — ch10** (memo Revisions 30; commit f0722fc). §I Louppy stated
as Cosneau's pièce LXXXIV is — a commission of 26 May 1445 billeting
190 lances in Poitou, the sum blank, under a lost general act earlier
than 20 April; the 1,500 lances re-based on Basin, Escouchy and
Contamine; the spelling per Cosneau; the trois voyes (pièce LXXXVI)
matched to Contamine's tariff; pièce LXXXII's "en maniére que la force
et auctorité nous demeure" entered. (j) the 1360s as the first
permanence, reversed 1380; 1439–46 the second; Strayer's
defence-of-the-realm override; Hoffman p. 140 as the assumption his
own case disproves. The Praguerie corrected per Vale (Montferrand,
May 1440; the aides; the banishments; Dunois; the 1439 ordonnance a
dead letter until 1445); the revenue arc re-pinned to Commynes via
Vale. (l) the two-variable reading marked as the book's inference
from Depreter; "intact" and "guns" out; the fisc failure stated (the
charroi levy, Menostey, the emptied arsenals); Venice the fourth
counter-case with both disanalogies (Lombard war not cannon; men not
capital). (a)/(aa) Hoffman engaged by name and answered with
establishment cost and the 1380 reversal. (x) command, dependence and
capture introduced in §VIII's historical half (the Stationers'
quo warranto 1684–88; Venice's crews) with [PART B — (x) platform
application pending]; the terms not claimed as a coinage pending the
Farrell & Newman check. R6 Hussites re-sourced to Hall. (s) DeVries
use-note. (b) "subordinating … not eliminating" with Tilly p. 25.

**A4 — ch08** (memo Revisions 8; commit 6e4c679). (o) "outspent" →
sequence, not payment: the settlement bought enforcement, not law;
Payling's pardon as the failure point ("evenhanded in its
negligence"; the crown unwilling not weak; Stourton 1557); Baker's
absorption by procedure (assumpsit, writ of error, 1477;
incorporation unfinished in 1700); Dean's c. 1300 criminalisation;
the England line carried as the book's inference "plausible on the
dates and unproven on the documents"; the closing line recut. Every
Paston citation re-pinned to Gairdner 1872 vol. I by letter number
and page; the Osbern wording conformed; Margaret's hand-gun letter,
the Nowell forslet and Norfolk's proclamation added.

**A5 — ch07** (memo Revisions 4 of 2026-09-16; commit fc45d1e). R1
the pardon-roll tally cut, Griffiths staged as the dissent in his own
words, Bohna as carrier, [GAP: Harvey 1991] ×2. R9 the five thousand
cut ("this chapter carries no number"). Griffiths's corrections:
Blackheath by 11 June; the three manifestos distinguished (with the
finding that the Wikisource text is Gairdner's composite); Moleyns
killed by his own captain. The Praguerie per Vale and Basin. (t) the
Bundschuh programme restored ("no lord but God and the Emperor");
1525 as annihilation; the Speyer recess carried; the forty-seven
cannon captured-not-cast; the editors' caution against "unrestrained
control." (bb) the commons' consequences for the settlement itemised
with fifteenth-century instances. Payn's letter (Gairdner 1872: I,
no. 99, pp. 132–33) added.

**A6 — ch04** (memo Revisions 8; commit 86800fd). Lane's corrections
(the Arsenal's sixty acres and 2,000–3,000 men; the hundred galleys of
1570; the 1262 debt at five per cent half-yearly on "the propertied";
the Ten undated; Carmagnola's formal hearing and public execution).
R3 the bocche di leone re-pointed to Chambers & Pullan and flagged
[GAP]. R5 Colleoni's bargain — contractual fidelity plus the licensed
Romagna adventure of 1467, sequestration and a statue; the
captaincy-for-life date dropped (no carrier). (l) "Venice became the
proto-state itself" cut; Venice restated as the polity that "built
the instruments and, by Lane's verdict, refused the form," handed to
ch10.

**A7 — ch02 and ch01** (commits bef3c07, 5ef8cae). ch02 (q): §II in
Morris's terms — the Dictatus undated and an emergency-powers
document, Worms partitioning symbols in Germany only, Canossa
Henry's coup, Innocent III casualiter, the apex Innocent IV; Ullmann
demoted to the superseded reading; the papal fisc entered as the
disanalogy (1,214 gold ounces; the Papal State "created on the
battlefields"); Morris p. 113 as the other universalism's ratchet,
the book's inference marked. ch01: the Teutonic Order re-dated
(1198; the Prussian state a project of the 1230s — Nicholson p. 26);
(c) "ended" → "locked shut" throughout, with Strayer's trellis and
confessed blank and Scheidel p. 193 quoted, the ratchet stated as the
book's; the Great Interregnum 1254–73.

**A8 — the register pass** (commit at close). Introduction §I "was
ended … at an identifiable price … above what any subject could pay"
→ "locked into consolidated units … at an identifiable cost … the
establishment cost … beyond what any subject could sustain"; §II
"suppression" → "subordination"; condition 4 → "consolidate a bloc's
decisive capability"; §IV "the ending of the first dispersal" → "the
locking of the first dispersal into states." Coda §I "suppressing" →
"subordinating," "price … pay" → "establishment cost … sustain"; §VI
"ended within two generations" → "became irreversible within two
generations." ch12 §IV oil passages per (e): "1911 severed the private
off-switch" → "broke the private command … the same men went on
running the successor companies informally for a decade (Chernow ch.
27). The public off-switch was not severed from the barons; it was
acquired when they could no longer hold it — … 'crawling to
Washington on their hands and knees' (Yergin ch. 13) — … and what it
acquires it keeps"; "severs the same thing" → "takes the same thing
into public keeping, and keeps it"; "title left, discretion severed"
→ "title left, discretion taken and kept" — NOTE: the old wording is
spine §8(c)(ii)'s own formula; conforming the spine is Roderick's.
Within the chapter forks: ch10 §I "suppressing" → "subordinating"
(Tilly p. 25); ch06 §VII's Rogers-cycle paraphrase "suppressed" →
"subordinated" (the quoted sentence untouched); ch01/ch02/ch04/ch07/
ch08 "ended" → "locked" where the plural order's fate is stated;
"severs"/Standard Oil occurs nowhere outside ch12. The "people's
weapon" re-pointing: ch06 §VII done; the Introduction carries no
longbow echo to re-point (condition 1's "cheap distributed systems"
already names the drone, not the bow).

## Flags closed and opened

Closed (14): ch06 ×6 (English Heritage; tipping point; Rouen
1418–19; Howard UNVERIFIED; Freedman/Belloc; Cadillac); ch11 ×3
(Chrimes; Lander tallies; İnalcık per-levy); ch10 ×1 (Hussites);
ch07 ×2 (Griffiths pp. 619–20; Contamine); ch02 ×1 (Ullmann); ch01
Interregnum dating (not a flag; a correction).

Opened: [BRIDGE — PROPOSED] ×1 (ch11 §VI, steam not Gutenberg).
[OUTLINE CONFLICT] ×1 (ch11 memo — Henry VII and the devşirme).
[GAP] re-pointed or new: ch04 Chambers & Pullan (bocche di leone);
ch07 Harvey 1991 ×2 and the Complaint collation; ch10 Wolfe (the
taille's own line); ch11 Youings/Hoyle (dissolution receipts), the
İnalcık vassal-prince page, [GAP — Part B: Chastellain t. III,
Alençon]; ch01 Innocent III (Morris not in ch01's sources — upgrade
pass). [PART B] marker ×1 (ch10 §VIII). [RE-CHECK AT PRESS] +4 in
ch06 (the 50,000 saluts against Stevenson; Honfleur/Harfleur against
Barker; Basin's Castillon pins against Samaran tome II; Vale's
Cadillac date), +3 in ch10 and ch11 per their memos. [BOOK'S
ARGUMENT] +1 (ch11, the dissolution as universalist power).

## What a ruling asked for that could not be done at the pin

- **ch06, Honfleur/Harfleur (Revisions 21's correction from Barker):
  NOT APPLIED.** Blondel's text (Stevenson 1863: 141–42, read at the
  page) names Honnofluctus/Honofluctum, distinguished from Harofluctum,
  and Stevenson's index makes Curson captain of Honfleur; Barker (T3)
  has Harfleur. T1 read at the page outranks T3; the draft keeps
  Honfleur, records Barker in the citation, and flags [RE-CHECK AT
  PRESS]. Roderick to rule if he prefers Barker.
- **ch06, Cadillac (R7):** resolved for mode and for two of the three
  dates; Vale's 17 September execution (payment record) is not
  reconciled with Escouchy's 19 September storm and stands flagged.
- **ch06, Fougères:** Barker cited alone; Griffiths is not in ch06's
  sources.md and was not added (no new works).
- **ch07, R1:** Harvey 1991 is a retrieval row, not in corpus; the
  gentry tally stays out until it arrives.
- **ch04, R5:** the Colleoni captaincy date has no carrier in ch04's
  sources (Mallett gated); dropped rather than re-pinned.
- **ch11, (n):** the Ottoman composite rests on İnalcık's
  vassal-prince passage without a resolvable page (sidecar mapping
  failed); flagged in text. No source in corpus carries the
  dissolution's receipts. The Hermandad/Granada finance clause was cut
  rather than re-sourced (Ladero not in corpus).
- **ch01, Innocent III [GAP]:** Morris is ch02's source, not ch01's;
  closing it needs a ch01 sources entry (upgrade pass). The §IV
  "Since 2022" denial-regime dating (Miller/Brands) is a 13 September
  correction not in the Phase 5 ch01 list; NOT applied; flagged in
  the ch01 memo for Roderick.
- **ch05:** the rulings sheet's (h) row lists ch05 §VII "Aragon
  expanding"; ch05 is not in Part A and was not touched. Owed to the
  next pass (with "weary of the throne" and the Bergavenny caveat,
  per the ch11 fork's note).
- **ch10:** the "27 December 1444" Gaspard date and "No baron had
  this" do not occur in ch10 (nothing to cut there; the latter was
  ch06's and is done). The $52.7bn CHIPS aggregate still wants a
  named secondary before press.
- **ch12, ruling (e):** "title left, discretion severed" is spine
  §8(c)(ii)'s wording; echoed as "taken and kept" in the draft; the
  spine's sentence is Roderick's to conform.
- **ch06, ruling (z):** the Blondel "walls and the minds" quotation
  stays at §IV as the citation at source; whether Roderick's "once, in
  the Introduction" means it leaves ch06 too is a Part B (B3)
  question, flagged in ch06 memo Revisions 28.
- **Ruling (z), (u), (v) Alençon, (x) platform half, (w), (cc), (bb),
  §8(g) items 1–6, Appendix B and C:** Part B, not attempted.

## Voice ledgers

No chapter claims a new coinage. ch06's aphorism count stays at two
(the cut Roderick's). ch08's recut close ("not argued out of
existence; nor … outspent. It was outranked") is a quotable line the
ledger now counts. ch10 flags one candidate image ("a polity that is
one life long"). ch11's footer lists three new quotable lines for the
ration. ch06's "Belloc syndrome" is a label for Belloc's own text and
is not claimed as a coinage; "the longbow theorist in person" is
Roderick's phrase from the synthesis.

## Next

Resume research/claude-code-instruction-source-intake-catchup-2026-09-14.md
from where the ledger says session 1 closed: sessions 2 and 3
(Ruggie, Krasner, Ertman, Stasavage, Glete, Cheung; Chastellain tome
III with the Alençon pp. 484–87 and Lombard-lender pp. 315–16 scenes
verified at the page, Suleyman, Tilly 1975), STEP 3 integration, STEP
4 ledgers, assembly and report; then Part B.
