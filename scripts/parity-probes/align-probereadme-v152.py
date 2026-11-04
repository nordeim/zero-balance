#!/usr/bin/env python3
"""D6 — the probe README alignment for the v152 cycle: insert the v152
section (Session 187) between the v152 queue's end and '## The v138 cycle'
(each cycle section ends with the NEXT cycle's queue — the v151 section's
tail IS the v152 queue; the new v152 section carries the v153 queue)."""
import io
import sys

PATH = "scripts/parity-probes/README.md"

SECTION = """## The v152 cycle (the v146-era SAVINGS pair's FIFTEENTH re-run — Session 187)

The re-run cadence's third-pass next-oldest candidate: the v146-era
SAVINGS pair — the SAVINGS view at desktop 1280x800 FULL-PAGE (the
v58-era pair's surface family), last re-shot v146 — now the oldest
remaining [v146 < v147 < v148 < v149 < v150 < v151]; the pair's
FIFTEENTH re-run bracket [v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98
-> v104 -> v110 -> v116 -> v122 -> v128 -> v134 -> v140 -> v146 ->
v152]; the SEVENTY-FIFTH consecutive queue/ledger agreement — the
surface names verified against the v146 lineage's own records BEFORE
the derivation (the v146 plan's own header: the FOURTEENTH ordinal on
its 15-entry bracket [v58 the original, one entry — 15 entries − the
original = 14 re-runs, no off-by-one this lineage]; the v146 shots
header carries the FULL bracket form, the verification source). **A
PIN-ONLY cycle — src/ ZERO production-code changes + one e2e pin
(355 -> 356): the SAVINGS FILTER-CARD FREQUENCY SELECT TRIGGER's
FOCUS-VISIBLE LADDER at 1280 — the never-pinned keyboard path of the
pinned filter-card Select family's FREQUENCY sibling (the v37 S1 pin
closed the CATEGORY sibling at 1280 on /income; the v139 pin holds
both triggers' own-hover only — the sibling-completion form, the
v149/v150/v151 precedent)**; the cycle's standing items: the axe watch
(NO DRIFT — 4.14.0 holds, the v68 dedupe verified), the npm-audit
watch at its forty-third re-check (0 vulnerabilities --omit=dev — the
v110 bump holds [next 16.4.3 + zod 4.6.7]; no new advisories in the
watched ranges), the 146th standing checks (ALL GREEN — the
reference's four bugs live; the data census clean on the FIRST reads;
the clone's mobile menu VERIFIED WORKING the 146th consecutive time;
zero overflow at 390 on all five views; the seedcheck exact after the
clone half).

The baseline GREEN on the FIRST run (the REBUILT workspace — the
sandbox recycled between sessions: the repo re-cloned at main @
43834c1 [the v151 cycle's ship state + the operator's session_393],
npm ci [494 packages], the .env + db/ at the repo root + the seed
re-aligned to the canonical Oct 31 stamps via
scripts/align-seed-dates-v152.ts [the fresh Nov 4 seed shifted -4d on
every DISPLAYED date field — the items 2026-10-21..29 + the
assets'/liabilities' lastUpdated 2026-10-31, amounts untouched], BOTH
chromium pairs [1200 + 1243] available — the fresh-sandbox checklist
rule applied: BOTH chromium-1243 AND chromium_headless_shell-1243
verified in the cache before the first e2e run; the seedcheck EXACT
7/1850/2235/0/3/2 before any gate — under the env -u discipline, the
sandbox DATABASE_URL pollution live as documented): lint, typecheck,
108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e
[358 executions = 355 unique, ZERO flakes], 35/35 smoke; the
production-seam audit clean; skills/ excluded.

The probe series derived from the v146 lineage (derive-v152-series.py
— the generic swaps incl. the FOUR explicit session-token families
[refvlm/clonevlm + refarbit/clonearbit] + the history-correction
fragments [the era marker last re-shot v140->v146 + the
oldest-remaining list v141..v145->v147..v151 + the plan citation
v145->v151 + the agreement ordinal SIXTY-NINTH->SEVENTY-FIFTH + the
re-run ordinal FOURTEENTH->FIFTEENTH + the bracket extended in all
four corrected files], all applied on the FIRST run, zero residual,
line counts preserved 50/42/39/262) + the two-half builder
(derive-build-twohalf-v152.py — the session-token bump
refarbit146->refarbit152 FIRST + the lesson-range bump
v92..v145->v92..v151 + the lineage-note fixup LAST — the v110
swap-order rule) + the comparator (derive-compare-v152.py — the
provenance citations re-pointed at the v146 measurement) + the verify
script (derive-verify-twohalf-v152.py) + the 146th standing pair
derived (derive-standing-v152.py — the ordinal 145th->146th th->th
plain replace, ref145/clone145->ref146/clone146, v145->v146;
normalize-back diff clean, line counts preserved 119/74). The halves
built + the ONE-block md5 contract verified by the direct THREE-WAY
python extraction (verify-twohalf-v152.py — SV_CENSUS_JS [the
savings census JS] 153 lines md5 891ab9b6, byte-identical across
arbit-v152.sh + ref-arbit-v152.sh + clone-arbit-v152.sh — the
documented v122/v128/v134/v140/v146 lineage contract VERBATIM: the
savings census JS block carries no version tokens, so the digest is
cycle-invariant).

The VLM pairwise run TWICE (the full logs at /tmp/vlm152/): pass 1
SAVINGS DIFFERENT (data-only — layout/style essentially matches) /
pass 2 SAVINGS DIFFERENT (the data list + three style-flag variants) —
the v146-era stable-different form. Every flag in both passes in the
documented classes: the avatar the USER-IDENTITY class; the subtitle
counts/totals + the card names/amounts/badges/dates the
SEED-COUNT/SEED-DATA classes; the pass-2 style-flag variants each
DOM-arbitrated — the badge treatment [the green icon-bearing
savings/Recurring pills vs the red need pill] the classification-VALUE
badge-axis classes (census-documented: badges[0] "need" red vs
"savings" green + badges[2] "active" slate vs "Recurring" green
icon-bearing — value-dependent axes); the card footer account field
[Brokerage/Bank Account] the v57 DATA-CONDITIONAL class
(census-documented: footer childCount 1 vs 2 — the reference RENDERS
payment chips when its data carries them); the category-dot color
claim [teal vs blue] DISPROVEN (the census's dot axes byte-identical —
dotBg rgb(59, 126, 161) BOTH sides — and the dot color is TYPE-based
[item-card.tsx:69, TYPE_COLORS[item.type]]: every savings item on BOTH
sites renders the same savings-type dot; the VLM color-perception
misread class); NO FAB claim raised in either pass this cycle — the
standing platform-chrome guard re-confirmed LIVE anyway by
base44-fab-arbit-v152.sh (the single-surface form at the pair's own
1280 viewport: fabCount 0 + bodyHasBase44 false on BOTH sides, the
/savings surface, 1280x800, logged-in — the standing
v97/v103/v108/v109/v115/v120/v123/v127/v129/v135/v141/v142/v143/v144/
v148/v149/v150/v151 disproof form re-confirmed). The both-sides census
compared axis-by-axis (compare-v152-census.py): 120 axes — 80
identical + 40 documented-class deltas, ZERO new — REPRODUCING the
v146 census values EXACTLY (the same 120/80/40 split, zero drift on
every axis); the seedcheck exact after the clone half.

F4 -> the pin: the SAVINGS FILTER-CARD FREQUENCY SELECT TRIGGER's
FOCUS-VISIBLE LADDER at 1280 — NO GAP (PIN-ONLY). The candidate
survey: the savings-pair surfaces' interaction families ALL HELD
except the frequency Select trigger's focused state — never pinned at
ANY viewport (the suite-wide survey: rg 'frequency' across
tests/e2e/*.spec.ts — 19 matches, ZERO focus/ladder matches — one
badge-color comment + the v139 hover pin; the v37 S1 pin is the
CATEGORY sibling only, closed at 1280 on /income) — the
sibling-completion form (the v149/v150/v151 precedent). The discovery
census freqfocus-discovery-v152.sh (both sides' ladders at 1280 on
/savings — the STRUCTURAL finder the v139 text-based convention [the
reference's triggers carry NO aria-labels, located by their text 'All
Categories'/'All Frequencies'; the clone's carry them — the a11y
superset; the first run's aria-label finder form REJECTED for the
reference side — the discovery corrected to the text-based standing
finder], the REAL focusVisible idiom, the (5,5)-parked pointer,
READ-ONLY) measured both sides' ladders CLEAN — NO GAP: the focused
rung's visible ring composite [fv true + the 1px #0a0a0a ring layered
over the ambient shadow-sm + the untinted border rgb(229,229,229) +
the 216x36 geometry] byte-identical both sides, the blur restore
clean; the sole deltas the documented invisible constructs (the
focused outline construct — REF the v3 ENGAGED-but-TRANSPARENT form
[solid 2px rgba(0,0,0,0) + offset 2px] vs CLONE the v4 none form — the
v148 tablist-trigger class; the boxShadow lead-layer construct — REF
the white zero-spread lead vs CLONE the four transparent leads — the
v37 O1/v148 class; the at-rest outlineColor computed form [REF
rgba(10,10,10,0.5) vs CLONE lab(2.74175 0 0.00000596046 / 0.5)] — the
v95 class; all invisible by construction, never pinned). THE PLAN
WRITTEN BEFORE THE PIN (docs/remediation-plan-v152.md). THE PIN
(append-pin-v152.py — ONE test: the sibling-completion form adapting
the v146/v151 ladder pin's measurement idiom — the /savings view, the
settle line '2 items · $1250.00', the role finder getByRole("combobox",
{ name: "Filter by frequency" }), the at-rest -> focused -> blurred
ladder at 1280, the (5,5)-parked pointer, the REAL
focus({focusVisible:true}) idiom, the 450ms settles; the
outline-family axes deliberately NOT asserted — the v148 discipline) —
green on the current build on the FIRST invocation (the PIN-ONLY form;
no RED step: there is no repair); the authoritative --list: 356 in 24
files.

THE PIN-SANITY MUTATION — the RING-REMOVAL form (the
`focus:ring-1 focus:ring-ring` construct disabled from select.tsx —
the exact construct-cleanup drift class the pin exists to guard; the
WIDER blast radius noted [the construct serves EVERY SelectTrigger
instance — the v37 S1 pin (the category trigger on /income) lives on
the same construct in the SAME family]): the FULL ITEMS SWEEP read 2
failed [EXACTLY the v37 S1 pin + the v152 pin — the shared-construct
class, both filter-card Select focus pins together] + 56 passed, the
failure diff EXACTLY the predicted ring axis (the focused boxShadow's
rgb(10, 10, 10) 0px 0px 0px 1px ring layer gone — the mutated
construct leaves only the transparent leads + the ambient — while the
fv/border/geometry axes were preserved, the failure landing at the
ring toContain alone); restored (git diff src/ = 0 lines) + the FULL
REBUILD + the post-restore regression 58 passed (the full items sweep
— the v139 hover pin's + the v145/v146/v151 Add-button pins'
same-file immunity verified live).

The ship chain: 356 e2e ZERO flakes (99+96+82+82 = 359 executions =
356 unique — the +1 landing in ch1 [items]; both closed watches green
through the chain); 35/35 smoke; the screenshots 16/16 captured — 16
byte-identical (the same-day law: the capture day Nov 4 UTC == the
committed v151 captures' day — the 07-add-item-modal wall-clock
surface matching byte-for-byte [11/04/2026]; every seed-stamped
surface byte-identical under the canonical Oct 31 stamps — the
same-seed law intact, zero arbitration); the dev evidence 4/4
byte-identical + VLM-verified (the menu proof {"url":"/income",
"docSW":390,"navLandmark":true}; the dev-shots scripts derived
v151->v152 with the version-swap-only verification on both; the menu
OPEN [all 5 links + the brand] + the post-nav /income [the sheet
closed] + the dashboard [clean] all confirmed — the dashboard
fold/sign-prefix notes DISPROVEN by byte-identity to the committed
v151-verified set [the VLM pass-variation class, the v150/v151
documented form]).

The v153 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence's next-oldest candidate —
**the v147-era LOGIN + CALCULATOR pair** (the LOGIN view + the
CALCULATOR dialog at desktop 1280x800 [the v59-era pair's surface
family], last re-shot v147 — now the oldest remaining [v147 < v148 <
v149 < v150 < v151 < v152]; the pair's FIFTEENTH re-run bracket [v59
-> v66 -> v75 -> v81 -> v87 -> v93 -> v99 -> v105 -> v111 -> v117 ->
v123 -> v129 -> v135 -> v141 -> v147 -> v153] to be verified against
the v147 lineage's own records before the derivation — the v147 plan's
own header records the FOURTEENTH ordinal on its 15-entry bracket
[v59 the original, one entry — 15 entries − the original = 14 re-runs],
consistent, no off-by-one this lineage; the v147 shots header carries
the FULL bracket form, the verification source),
(2) the axe-core watch at its next re-check point (only a 5.x wrapper
changes the calculus), (3) the npm-audit watch at its re-check point
(only a new advisory in the next/zod ranges changes the calculus),
(4) the deferred reference-write censuses (unchanged — out of bounds
under the v46 read-only rule), (5) the residual-class watch (both
flake classes CLOSED by the v136 dual-stack/localhost fix — the
watch continues in the standing form for any NEW class).

"""

text = io.open(PATH, encoding="utf-8").read()
if "## The v152 cycle" in text:
    print("SKIP: the v152 section already present")
    sys.exit(0)

anchor = "the standing form for any NEW class).\n\n## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)"
n = text.count(anchor)
if n != 1:
    print(f"FAIL: the insert anchor {n}x")
    sys.exit(1)

text = text.replace(anchor, "the standing form for any NEW class).\n\n" + SECTION + "## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)")
io.open(PATH, "w", encoding="utf-8").write(text)
print("OK: the v152 section + the v153 queue inserted (D6)")
