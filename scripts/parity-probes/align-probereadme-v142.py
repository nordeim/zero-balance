#!/usr/bin/env python3
"""align-probereadme-v142.py — D6 of the v142 docs alignment: insert the
v142 cycle section + the v143 queue into scripts/parity-probes/README.md,
immediately after the v142 queue paragraph (the v141 cycle's own section
tail) and before the v138 section. D0 discipline: the insert anchor
verified 1-hit BEFORE any write; the script refuses on any miss."""
import io
import sys

PR = "scripts/parity-probes/README.md"
text = io.open(PR, encoding="utf-8").read()

# the unique anchor: the v142 queue's own tail (the v136-lineage-specific
# wrapping) + the section break before the v138 cycle header
anchor = (
    "calculus), (4) the deferred reference-write censuses (unchanged — out\n"
    "of bounds under the v46 read-only rule), (5) the residual-class watch\n"
    "(both flake classes CLOSED by the v136 dual-stack/localhost fix — the\n"
    "watch continues in the standing form for any NEW class).\n"
    "\n"
    "## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)"
)
n = text.count(anchor)
if n != 1:
    print(f"ANCHOR MISS (the v142 queue tail): {n} hits")
    sys.exit(1)

SECTION = """## The v142 cycle (the v136-era NETWORTH + drill-down-DASHBOARD pair's THIRTEENTH re-run — Session 177)

The re-run cadence's second-pass next-oldest candidate: the v136-era
NETWORTH + drill-down-DASHBOARD pair — the NETWORTH view + the
DASHBOARD's drill-down EXPANDED state at desktop 1280x800 (the v60-era
networth+drill-down pair's surface family), last re-shot v136 — now the
oldest remaining [v136 < v137 < v138]; the pair's THIRTEENTH re-run
bracket [v60 -> v67 -> v76 -> v82 -> v88 -> v94 -> v100 -> v106 -> v112
-> v118 -> v124 -> v130 -> v136 -> v142]; the SIXTY-FIFTH consecutive
queue/ledger agreement — the surface names verified against the v136
lineage's own records BEFORE the derivation (the v136 plan's own header:
the TWELFTH ordinal on its 13-entry bracket [v60 the original, one
entry — 13 entries − the original = 12 re-runs, no off-by-one this
lineage]; the v136 shots header carries the FULL bracket form, the
verification source). **A PIN-ONLY cycle for src/ — zero
production-code changes (the twelfth PIN-ONLY cycle in the last
thirteen) + one e2e pin (344 -> 345)**; the cycle's standing items: the
axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified), the
npm-audit watch at its thirty-third re-check (0 vulnerabilities
--omit=dev — the v110 bump holds [next 16.4.3 + zod 4.6.7]; the 16
moderate the accepted dev-only ESLint braces chain), the 136th standing
checks (ALL GREEN — the reference's four bugs live; the data census
clean on the FIRST reads; the clone's mobile menu VERIFIED WORKING the
136th consecutive time; zero overflow at 390 on all five views; the
seedcheck exact after the clone half).

The baseline GREEN ON THE FIRST CHAIN (the SAME-PERSISTED workspace —
the v141 environment held through the session boundary: node_modules 354
entries intact, BOTH chromium pairs [1200 + 1243] in the cache, the .env
[DATABASE_URL="file:../db/custom.db"] + db/ at the repo root intact with
the v141-cycle seed, the repo pulled to main @ eb1fc47 [the session-log
commit, +1 file docs/session_353.md]; the seedcheck EXACT
7/1850/2235/0/3/2 before any gate — under the env -u discipline, the
sandbox DATABASE_URL pollution live as documented; lint, typecheck,
108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e [347
executions = 344 unique, ZERO flakes], 35/35 smoke; the production-seam
audit clean; skills/ excluded).

The probe series derived from the v136 lineage (derive-v142-series.py —
the generic swaps incl. the FOUR explicit session-token families
[refvlm/clonevlm + refar/clonear arbit — the tokens carry '136' without
the 'v' prefix] + the history-correction fragments [the era marker
last-re-shot v130->v136 + the oldest-remaining list v130..v132->
v136..v138 + the ordinal TWELFTH->THIRTEENTH + the bracket extended in
all four files + the agreement ordinal FIFTY-NINTH->SIXTY-FIFTH + the
arbit census provenance "the v130 census axes"->"the v136 census axes"],
all applied on the FIRST run, zero residual, line counts preserved
84/71/65/328 == the v136 lineage exactly; bash -n + node --check clean;
the pre-derivation sweep re-confirmed the v136 derivation's own finding
— all era tokens confined to the file headers, lines 2..8) + the
two-half builder (derive-build-twohalf-v142.py — the generic swap + the
lesson-range bump v92..v135->v92..v141 [the BARE range token] + the
lineage-note fixup "the v130-lineage derivation"->"the v136-lineage
derivation" LAST) + the comparator (derive-compare-v142.py — the generic
swap incl. the EXPLICIT /tmp/vlm136->/tmp/vlm142 log-path swap [the path
token carries no 'v136' substring] + the provenance citations re-pointed
at the v136 measurement [the lineage ordinal TWELFTH->THIRTEENTH; the
records chain v124/v130->v130/v136]) + the verify script
(derive-verify-twohalf-v142.py — the lineage-citation chain extended
v124/v125/v126/v127/v128/v129->+v130/v136) + the 136th standing pair
(derive-standing-v142.py — derived from the v135 pair, three token
families [the ordinal 135th->136th th->th plain replace, the bare
session names ref135/clone135->ref136/clone136, the version v135->v136;
the citation extended with v141's 134th->135th], normalize-back diff
clean, zero old tokens, line counts preserved 119/74 — the derivation's
own first-run pairing miss [the 134th sources] caught and fixed BEFORE
any execution). The halves built + the TWO-block md5 contract verified
by the direct THREE-WAY python extraction (verify-twohalf-v142.py —
ARBIT_A 90 lines md5 17d18f15c9145155afd28f7f1ca6efde + ARBIT_B 111
lines md5 9d4b50ad1f8c22dfe207ea9aa61470be, byte-identical across
arbit-v142.sh + ref-arbit-v142.sh + clone-arbit-v142.sh — **the
within-cycle contract form: the view-label tokens carry the version
['drill-arbit-1280-v142' / 'nw-height-1280-v142'], so the digests differ
from the v136 cycle's by construction**).

The resource discipline applied between every half (the browser daemons
reaped BEFORE every half; both halves + both shot series executed with
first-attempt logins; the full logs captured by the runner redirection —
/tmp/vlm142/{ref,clone}-census.log, the comparator's documented input
paths).

The VLM pairwise run TWICE with full log capture
(/tmp/vlm142/vlm-pass{1,2}.log): pass 1 NETWORTH IDENTICAL /
DRILL-DOWN DIFFERENT; pass 2 NETWORTH IDENTICAL / DRILL-DOWN DIFFERENT
— **the stable-identical-networth form (the v105/v121/v136 precedent
class: the identical side's outcome holds while its data differences
stay folded in the expected-and-reported data classes)**. The
drill-down flags across both passes, all in the documented classes: the
nav-highlight (the v56 SUPERSET class — the census navHighlight.color
rgb(63,63,70) vs rgb(255,255,255) + .fw 400 vs 500), the avatar letter
(the USER-IDENTITY class — the pass-2 form read the clone's 'D'
correctly; the pass-1 networth-side claim of a lime 'P' the
LETTER-MISREAD class [the census's own avatarLetter axis measured 'D'
directly — the v136 "Total Expense[s]" misread precedent's own family]),
the progress fill (the PCT data class — 173px vs 357px, the seed
percentages), the donut labels (the v60 PERCEPTION class — the
reference's concatenated stacked labels vs the clone's separate labels;
the census donutLabels count/labelFs/labelFill byte-identical), the
extra Freelance category + the "1 category"/"2 categories" footer (the
SEED-DATA classes), the "Total Expense vs Total Expenses" title claim
(a pass-1 MISREAD — both sides' third card title measured "Total
Expenses" in the v136 statfooter census, the same misread class as the
v136 cycle's own pass-2 claim), and the FAB claims (the PLATFORM-CHROME
class — claimed in BOTH directions across the two passes [pass 1:
ref-side on the networth; pass 2: clone-side on the networth + ref-side
on the drill-down stat-card tooltip], **DISPROVEN LIVE by
base44-fab-arbit-v142.sh**: fabCount 0 + bodyHasBase44 false on BOTH
sides, BOTH flagged surfaces [the dashboard / + the networth /networth],
1280, logged-in — the standing v97/v103/v108/v109/v115/v120/v123/v127/
v129/v135/v141 disproof form re-confirmed). The networth side:
IDENTICAL both passes (its data differences — the figures, the
asset/liability counts, the ratio — all in the expected-and-reported
data classes).

The both-sides census compared axis-by-axis
(compare-v142-census.py): **73 axes — 67 identical + 6 documented-class
deltas, ZERO new — REPRODUCING the v136 census values EXACTLY** (the
same 73/67/6 split, zero drift on every axis: the 6 documented =
navHighlight.color + navHighlight.fw [the v56 superset delta] +
avatarLetter [the user-identity data class] + progress.fillW [the pct
data class] + donutLabels.texts [the each-site's-data class] +
labelBlock.w [the v82 DATA-CONDITIONAL width class: the 48px figure's
text length "$25,000.00" 304px vs "-$245,950.00" 357px]). The seedcheck
exact after the clone half (7/1850/2235/0/3/2). NO NEW CLONE GAP on the
census axes.

THE PIN — the DASHBOARD DRILL-DOWN ROWS' OWN-HOVER LADDERS at 1280 on
/dashboard (PIN-ONLY — src/ ZERO changes, the twelfth PIN-ONLY cycle in
the last thirteen; +1 e2e = 345): the candidate survey (the networth +
drill-down surfaces' interaction families swept against the specs' own
assertions — the SPEC-ALIAS lesson) found the networth half's families
ALL HELD (the kebab twins' reveal family pinned on every path [the v46
F2 pin the at-rest census + the card-hover REVEAL + the card's own
REAL-hover INERT shadow; the v124 pin the OPEN+parked state; the v130
pin the OWN-HOVER tint ladder; the v132 pin the BADGE own-hover at 390;
the v136 pin the FOCUS-VISIBLE ladder]; the tablist pinned at three
viewports [the v50/v53 chrome censuses at 640/390 + the v60 F1 census
at 1280 + the v138 own-hover ladder at 390]; the summary-card family
pinned at three viewports [the v41/v60/v67/v82/v90/v96/v100/v102
censuses]; the section row + the Add Asset chrome by the v94 pin [the
Add Asset button INERT by design — the v11 G4 record]) and the
drill-down half's families: the stat cards' own-hover by the v131 pin
[the radial-circle + chevron reveals] + the v137 pin [the
INLINE-PERSISTENCE shadow ladder]; the quick actions by the v125 pin;
the donut by the v126 pin + the keyboard by the v31 pin; the hero by
the v35 S2/v56/v60/v67 pins; the expansion animation by the v44 F1 pin;
the chevron glyph contract by the v43 F1/v44 F4 pins; the section row's
hovered bg axis by the v43 F2 pin (the arbitrary-hex repair's own
regression axis — the hovered bg + cursor alone, never the ladder); the
rows' at-rest chrome by the v43/v44/v50/v53 censuses (the category
row's inline bg pinned at four states) — **the CATEGORY row's own-hover
INERT contract held by NO spec at ANY viewport, and the LADDER FORM
(the at-rest rung -> the hovered rung -> the restored rung, the
hoverMatch axes) never pinned on EITHER row** (the suite-wide survey:
breakdown.spec.ts — the drill-down's own spec — carries ZERO hover
coverage; dashboard.spec.ts's hover pins cover only the stat cards +
the quick actions) — the strongest form: never-pinned at ANY viewport,
both-sides measurable, on the PAIR'S OWN SURFACE (the drill-down
EXPANDED state — the pair's second half), at the pair's own 1280
viewport, the view's primary interactive rows. THE CONSTRUCT — the
two-contract form, the reference's own asymmetry: the clone's SECTION
row carries hover:bg-[#f9fafb] with NO inline bg (dashboard-view.tsx:309
— the v43 F2 arbitrary-hex repair), so its expected own-hover end-state
is the TINTED contract (the bg transitioning rgba(0,0,0,0)->
rgb(249,250,251) under the row's own hover with the color/radius/
geometry family unchanged); the clone's CATEGORY row carries
hover:bg-gray-100 BUT ALSO an inline backgroundColor "rgb(249, 250,
251)" (dashboard-view.tsx:365 — the inline beats the utility, the v29
class), so its expected own-hover end-state is the INERT-HOVER contract
(the at-rest inline bg persisting unchanged under the row's own hover).
The both-sides one-shot census drillhover-arbit-v142.sh (the v141
submithover form adapted to the drill-down rows' axis pair: the
STRUCTURAL finders [the breakdown card by its "Net Zero Breakdown"
title leaf -> its closest rounded-2xl ancestor — the form shared by
both sites; the section row = the card's button whose text carries
"Total Income"; the category row = the card's first button whose
trimmed text starts with "Salary" — both sites' first Income category,
the seed names cross-checked in the census output], the ONE-TIME
view-state expansion click on the section row [allowed under the v46
incident rule — the drill-down rows mutate no data; the rows NEVER
clicked past the one expansion — the accordion toggles on click, out of
bounds], the (5,5)-parked ladder, the live-read centers [the section
(1088,225) + the category (1116,275) — IDENTICAL coordinates both
sides], READ-ONLY — a mouse MOVE on a button dispatches no click and
the expansion state is never toggled by a move) measured the ladder on
BOTH rows and found **NO GAP** (the AT-REST rung: {section: hoverMatch
false, bg rgba(0,0,0,0), color rgb(10,10,10), radius 8px,
transitionDuration 0.15s, w 254, h 56; category: hoverMatch false, bg
rgb(249,250,251) [the inline], color rgb(10,10,10), radius 8px, w 214,
h 28} — IDENTICAL both sides; the SECTION-HOVERED rung: {hoverMatch
true + bg rgb(249,250,251) — THE TINTED CONTRACT, the color/radius/
geometry family UNCHANGED} — IDENTICAL both sides; the CATEGORY-HOVERED
rung: {hoverMatch true + bg rgb(249,250,251) UNCHANGED — THE
INERT-HOVER CONTRACT} — IDENTICAL both sides; the RESTORED rung: both
rows' at-rest contracts re-established — IDENTICAL both sides; the
deltas the documented construct classes alone: the transitionProperty
metadata [REF the v3 six-prop list vs CLONE the v4 gradient-var compile
with outline-color + the --tw-gradient tokens — the v95 family, never
pinned; the transitionDuration 0.15s IDENTICAL both sides] + the
category row's txt [the SEED-DATA class: the reference's
"Salary$5000.00" vs the clone's "Salary$5200.00"]). The pin appended
(append-pin-v142.py — the at-rest rung -> the SECTION-HOVERED rung
{hoverMatch true + bg rgb(249,250,251) — THE TINTED CONTRACT + the
UNCHANGED color/geometry family} -> the CATEGORY-HOVERED rung
{hoverMatch true + bg rgb(249,250,251) UNCHANGED — THE INERT CONTRACT}
-> the restored rung; the V94-COLLISION-safe axis set [the transition
metadata deliberately NOT pinned — the v95 family's own form]; the
shared section-hovered-bg axis with the v43 F2 pin noted [a
section-tint removal fails both — CORRECT drift behavior, both pins
guarding the same repair; the sole-failure criterion runs on the
CATEGORY-axis mutation]; GREEN on the first run; the authoritative
--list: 345 in 24 files).

THE PIN-SANITY MUTATION — the INLINE→CLASS SWAP form: the category
row's inline style={{ backgroundColor: "rgb(249, 250, 251)" }} replaced
with the bg-[#f9fafb] utility class at dashboard-view.tsx:364-365 (the
single construct; the component serves EVERY breakdown section's
category rows on the dashboard — the WIDER-FILE blast radius noted, the
sole-failure criterion verified on the FULL DASHBOARD SWEEP ALONE) —
**the exact Tailwind-v4-refactor drift class the pin exists to guard**:
the at-rest computed bg stays IDENTICAL (bg-[#f9fafb] computes the same
rgb(249,250,251), so the v43/v44/v50/v53 at-rest censuses stay GREEN),
but the hover utility hover:bg-gray-100 now WINS under hover (the
:hover pseudo-class outweighs the plain utility) — the hovered bg
computes the v4 named palette's lab() value (the v43 F2 record's own
trap), the INERT contract BROKEN. **The SOLE FAILURE verified live — 1
failed [the pin alone] + 52 passed in the FULL dashboard sweep**, the
failure diff EXACTLY the predicted category-hovered-rung bg axis (the
lab() value "lab(96.1596 -0.0823438 -1.13575)" [the v4 gray-100]
received vs the pinned inert "rgb(249, 250, 251)" expected, hoverMatch
true preserved); the v43 F2 section-row pin GREEN (the section row
untouched by the mutation); restored (git diff src/ = 0 lines) + the
FULL REBUILD + the post-restore regression **93 passed** (dashboard 53
+ networth 40 — the v137/v131/v125 dashboard pins + the v136 networth
pin's different-file immunity verified live).

The ship chain: **345 e2e zero flakes** (95+94+77+82 = 348 executions =
345 unique — the +1 landing in ch2 [dashboard]; both closed watches
green through the chain); 35/35 smoke; the screenshots **16/16 captured
— ALL byte-identical** (the same-day law: both this cycle and v141
captured Nov 1 UTC, every date-bearing surface rendering identically
under the persisted seed); the dev evidence 4/4 byte-identical +
VLM-verified (the menu proof {"url":"/income","docSW":390,
"navLandmark":true}; the dev-shots scripts derived v141 -> v142 with
the version-swap-only verification on both).

The v143 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence's SECOND-PASS next-oldest
candidate — **the v137-era DASHBOARD pair** (the DASHBOARD at desktop
1280x800 FULL-PAGE [the Budget Guidelines card + the Quick-Action row
below the fold], the v125-era pair's surface family, last re-shot v137
— now the oldest remaining [v137 < v138]; the pair's THIRTEENTH re-run
bracket [v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113
-> v119 -> v125 -> v131 -> v137 -> v143] to be verified against the
v137 lineage's own records before the derivation — the v137 plan's own
header records the TWELFTH ordinal on its 13-entry bracket [v61 the
original, one entry — 13 entries − the original = 12 re-runs],
consistent, no off-by-one this lineage; the v137 shots header carries
the FULL bracket form, the verification source), (2) the axe-core watch
at its next re-check point (only a 5.x wrapper changes the calculus),
(3) the npm-audit watch at its re-check point (only a new advisory in
the next/zod ranges changes the calculus), (4) the deferred
reference-write censuses (unchanged — out of bounds under the v46
read-only rule), (5) the residual-class watch (both flake classes
CLOSED by the v136 dual-stack/localhost fix — the watch continues in
the standing form for any NEW class).

"""

text = text.replace(anchor, SECTION + "## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)", 1)
io.open(PR, "w", encoding="utf-8").write(text)
print("D6 probe README: the v142 section + the v143 queue inserted before the v138 section")
