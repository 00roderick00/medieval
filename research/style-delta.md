# Style Delta — Current Drafts vs research/style-standard.md
## For a single scripted conformance sweep at assembly, after Roderick's rewrite

*Generated 2026-08-04. Counts are from a scripted sweep of the fourteen
draft files (Introduction, chs. 1–12, Coda); patterns are approximate
where noted. NO restyling has been performed — per instruction, this
list exists so the conformance pass can run once, scripted, after the
rewrite. One example per conflict class.*

| # | Conflict class | Count | Example | Note for the sweep |
|---|---|---|---|---|
| D1 | **Citation system**: author–date parentheticals in text vs Section II notes (first-full/short-title) | ~188 parenthetical author-date cites (plus bare page-pin cites) | `(Bull [1977] 2012: 245)` (Intro §V) | BY DESIGN — the drafting format doctrine preserves for traceability; the assembly converter (tools/assemble.py) already lifts parentheticals to notes; it must additionally expand FIRST references to the full Section II form and shorten the rest. Requires a works-register keyed to each chapter's sources.md. |
| D2 | **Double quotation marks** vs single inverted commas (doubles only within quotes) | ~374 double-quoted spans | `"a line of 250 guns of all calibres massed wheel to wheel"` (Intro §I) | Scripted swap with nesting inversion; French/Latin quotations keep guillemet-free doubles? — originals' conventions are retained per §5 of the standard, so verbatim source-quotes need case-by-case handling where the original edition used « » or " ". |
| D3 | **Serial comma** absent | ~50 `, x and y` patterns | `fiscal, administrative and legibility` (Intro §II) | Scripted-with-review (some hits are true pairs, not lists); note voice.md's own examples lack the serial comma — the standard overrides, per the adoption instruction. |
| D4 | **Numbers under 100 in figures** where prose form is required | ~310 (rough; unit-, percent-, page- and money-attached numerals excluded) | `fifty or sixty killed or taken` coexists with `30 guns`-type figures | Judgment sweep, not blind script: the standard's mixture rule (all-figures where a passage mixes >100 and <100) legitimises many instances — especially chs. 10–12's statistical passages. |
| D5 | **Elliptical day-ordinals** (`fell on the 10th`) vs the date form (10 May) | 3 (ch06 §VII bridge) | `Paris fell on 14 June` ✓ but `opened on the 10th` | Trivial; expand at sweep. |
| D6 | **Journal cites carrying both issue and month/neither consistently** in sources.md apparatus | unscoped | `*EHR* 79/311 (1964)` (volume/issue form) | Section II: volume mandatory, issue OR month, never both; normalise at bibliography build. |
| D7 | **Bibliography does not yet exist** in Section II form | n/a | — | The per-chapter sources.md files are graded working lists, not the bibliography; the assembly must generate the three-section, surname-inverted, hanging-indent bibliography (manuscript sources by place–library–shelfmark, the medievalists' convention adopted). |
| D8 | **Ibid.** unused | 0 (nothing to fix) | — | Becomes available at note-conversion; the converter should apply it only under the standard's no-confusion rule. |

## Adopted-reading decisions (recorded, not conflicts)

- **Endnotes, not footnotes:** Section I.D compels footnotes for
  coursework; under the adopted reading Section I is ignored as
  mechanics, and the book's endnote apparatus (project doctrine)
  stands, carrying Section II's *content and forms*.
- **Word-count, presentation, submission rules (I.A–B):** ignored.
- **Foreign-language quotation duplication (I.C.5/A.4.e):** the
  project's original-plus-[TRANS. CLAUDE] practice is compatible; at
  press, original in text with translation in the notes (or vice
  versa), per the standard.

## Conformities worth recording (no action)

Possessive 's on names in -s (Rogers's, Watts's — 0 violations found);
decades without apostrophe (1440s); centuries written out in prose;
the date form (17 July 1453); British spelling and logical punctuation
throughout; abbreviation/contraction pointing (ed. / edn) already
matches.

## Silences carried from the standard

Block-quote threshold; dash conventions; ellipsis style — flagged in
style-standard.md §9 for Roderick's ruling at the sweep.
