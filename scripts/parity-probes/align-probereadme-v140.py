#!/usr/bin/env python3
"""align-probereadme-v140.py — D6 of the v140 docs alignment: insert the
v140 cycle section + the v141 queue into scripts/parity-probes/README.md,
immediately after the v140 queue paragraph (the v139 cycle's own section
tail) and before the v138 section. D0 discipline: the insert anchor
verified 1-hit BEFORE any write; the script refuses on any miss."""
import io
import sys

PR = "scripts/parity-probes/README.md"
text = io.open(PR, encoding="utf-8").read()

# the unique anchor: the v140 queue's own tail (the v134-lineage-specific
# wording) + the section break before the v138 cycle header
anchor = (
    "the v134\n"
    "shots header carries the FULL bracket form, the verification source),\n"
    "(2) the axe-core watch at its next re-check point (only a 5.x wrapper\n"
    "changes the calculus), (3) the npm-audit watch at its re-check point\n"
    "(only a new advisory in the next/zod ranges changes the calculus), (4)\n"
    "the deferred reference-write censuses (unchanged — out of bounds under\n"
    "the v46 read-only rule), (5) the residual-class watch (both flake\n"
    "classes CLOSED by the v136 dual-stack/localhost fix — the watch\n"
    "continues in the standing form for any NEW class).\n"
    "\n"
)
n = text.count(anchor)
if n != 1:
    print(f"ANCHOR MISS (the v140 queue tail): {n} hits")
    sys.exit(1)

SECTION = """## The v140 cycle (the v134-era SAVINGS pair's THIRTEENTH re-run — Session 175)

The re-run cadence's second-pass next-oldest candidate: the v134-era
SAVINGS pair — the SAVINGS view at desktop 1280x800 FULL-PAGE (the
v128-era savings pair's surface family, the v58-era original), last
re-shot v134 — now the oldest remaining [v134 < v135 < v136 < v137 <
v138]; the pair's THIRTEENTH re-run bracket [v58 -> v65 -> v74 -> v80 ->
v86 -> v92 -> v98 -> v104 -> v110 -> v116 -> v122 -> v128 -> v134 ->
v140]; the SIXTY-THIRD consecutive queue/ledger agreement — the surface
names verified against the v134 lineage's own records BEFORE the
derivation (the v134 plan's own header: the TWELFTH ordinal on its
13-entry bracket [v58 the original, one entry — 13 entries − the
original = 12 re-runs, no off-by-one this lineage]; the surface-family
name "the v128-era savings pair" preserved — the lineage's own
designation). **A PIN-ONLY cycle for src/ — zero production-code
changes (the tenth PIN-ONLY cycle in the last eleven) + one e2e pin
(342 -> 343)**; the cycle's standing items: the axe watch (NO DRIFT —
4.14.0 holds, the v68 dedupe verified), the npm-audit watch at its
thirty-first re-check (0 vulnerabilities --omit=dev — the v110 bump
holds [next 16.4.3 + zod 4.6.7]; the 16 moderate the accepted dev-only
ESLint braces chain), the 134th standing checks (ALL GREEN — the
reference's four bugs live; the data census clean on the FIRST reads;
the clone's mobile menu VERIFIED WORKING the 134th consecutive time;
zero overflow at 390 on all five views; the seedcheck exact after the
clone half).

The baseline GREEN ON THE FIRST CHAIN (the SAME-PERSISTED workspace —
the v139 environment held through the session boundary: node_modules 354
entries intact, BOTH chromium pairs [1200 + 1243] in the cache, the .env
[DATABASE_URL="file:../db/custom.db"] + db/ at the repo root intact with
the v139-cycle seed, the repo pulled to main @ a1abcdc [the session-log
commit, +1 file docs/session_346.md]; the seedcheck EXACT
7/1850/2235/0/3/2 before any gate — under the env -u discipline, the
sandbox DATABASE_URL pollution live as documented; lint, typecheck,
108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e [345
executions = 342 unique, ZERO flakes], 35/35 smoke; the production-seam
audit clean; skills/ excluded).

The probe series derived from the v134 lineage (derive-v140-series.py —
the generic swaps incl. the FOUR explicit session-token families
[refvlm/clonevlm + refarbit/clonearbit — the tokens carry '134' without
the 'v' prefix] + FOUR history-correction fragments [the era marker
last-re-shot v128->v134 + the oldest-remaining list v128..v132->
v134..v138 + the queue source the v133 plan->the v139 plan + the
agreement counter FIFTY-SEVENTH->SIXTY-THIRD; the ordinal
TWELFTH->THIRTEENTH + the bracket extended in all four files], all
applied on the FIRST run, zero residual, line counts preserved
50/42/39/262 == the v134 lineage exactly; bash -n + node --check clean)
+ the two-half builder (derive-build-twohalf-v140.py — the builder's
ref_exec ASSERTION's stale refarbit134 bumped to refarbit140 FIRST [the
no-'v'-prefix token, untouched by the generic swap — the v121
stale-session precedent in this lineage's assertion form] + the
lesson-range bump v92..v133->v92..v139 [the BARE range token] + the
lineage-note fixup "build-twohalf-v128.py"->"build-twohalf-v134.py"
LAST) + the comparator (derive-compare-v140.py — the generic swap + the
provenance citations re-pointed at the v134 measurement) + the verify
script (derive-verify-twohalf-v140.py — the lineage-citation chain
extended v122/v128->+v134; the digest UNCHANGED). The halves built +
the ONE-block md5 contract verified by the direct THREE-WAY python
extraction (verify-twohalf-v140.py — SV_CENSUS_JS 153 lines md5
891ab9b6, byte-identical across arbit-v140.sh + ref-arbit-v140.sh +
clone-arbit-v140.sh — the v122/v128/v134 lineage value VERBATIM,
carried byte-identical through the version-swap derivation).

The resource discipline applied between every half (the browser daemons
reaped BEFORE every half; both halves + both shot series executed with
first-attempt logins; the full logs captured by the runner redirection —
/tmp/vlm140/{ref-arbit,clone-arbit}.log, mirrored to the comparator's
/tmp/{ref,clone}-arbit-v140.log paths).

The VLM pairwise run TWICE with full log capture (/tmp/vlm140/
vlm-pass{1,2}.log): pass 1 DIFFERENT / pass 2 DIFFERENT — the savings
pair's CONSISTENT FORM (the same verdict family as the v122/v128/v134
re-runs). Every flag in both passes in the documented classes,
arbitration-free this cycle (every flag's class already DOM-confirmed by
the census's own whitelisted quads): the card-grid layout the SEED-COUNT
class (the reference's 1-item savings seed vs the clone's 2-item dev
seed — the grid template census byte-identical 309.328px x3); the
card-footer payment chips ("Brokerage"/"Bank Account" absent on the
reference) the v57 DATA-CONDITIONAL class (its savings item ships no
paymentMethod — its footer childCount 1 vs the clone's 2); the badge
family (the red "need" vs the green "savings" + the clone's extra
"Recurring") the classification-VALUE + v57 wrap classes; the header
stats + the card contents the seed-data classes; the avatar letter the
USER-IDENTITY class. NO FAB/platform-chrome claim raised in either pass
this cycle — no arbitration script needed.

The both-sides census compared axis-by-axis (compare-v140-census.py):
120 axes — 80 identical + 40 documented-class deltas, ZERO new —
REPRODUCING the v134 census values EXACTLY (the same 120/80/40 split,
zero drift on every axis: the avatar chrome, the grid + card chrome [the
3-col 309.328px family], the titleRow, the amount leaf, the footer +
badge chrome [the 40 documented-class quads — the seed-count, the
DATA-CONDITIONAL footer chips, the classification-VALUE badge colors,
the Recurring superset chip, the wrap consequence], the page-header
family, the docSW 1280 guards). The seedcheck exact after the clone
half (7/1850/2235/0/3/2). NO NEW CLONE GAP on the census axes.

THE PIN — the SAVINGS FILTER-CARD SEARCH INPUT's OWN-HOVER LADDER at
1280 on /savings (PIN-ONLY — src/ ZERO changes, the tenth PIN-ONLY
cycle in the last eleven; +1 e2e = 343): the candidate survey (the
savings-pair surfaces' interaction families swept against the specs' own
assertions — the SPEC-ALIAS lesson) found the filter-card search input's
own-hover path entirely unpinned (the v37 S2 pin the input's
focus-visible family + the REAL-key typing contract [on /income, the
shared filter card]; the v64 census the /income at-rest geometry; the
v38 S2 pin the /savings class-level chrome; the v134 survey the /savings
at-rest + FOCUS ring — every search census AT-REST or FOCUS; the
input's own-hover END-STATE held by NO spec at ANY viewport; the input
reachable at 1280 on BOTH sides — the center (537,167), IDENTICAL
coordinates both sides). THE CONSTRUCT: the input carries NO hover:
utility (input.tsx:10 — the focus-visible + disabled + placeholder
classes alone), so the own-hover end-state is the INERT-HOVER contract
— the at-rest chrome persisting under the input's own hover. The
both-sides one-shot census searchhover-arbit-v140.sh (the v139
selecthover form adapted to the search-input axis: the STRUCTURAL finder
[the rounded-2xl white card containing an input -> its ONLY input —
tag-agnostic per the v107 lesson, shared by both sites; the placeholder
"Search savings items..." cross-checked — IDENTICAL both sides], the
(5,5)-parked ladder, the live-read center, READ-ONLY — a mouse MOVE on
an input dispatches no click and the input opens nothing on hover, the
census cannot mutate state) measured the ladder CLEAN, NO GAP (the
inert-hover contract IDENTICAL both sides at every rung; the deltas the
documented construct classes alone: the shadow LEAD-LAYER count [the
v37 S1's own O1 note — the v3 three-slot vs the TW v4 five-slot
construct, every lead a 0px-spread shadow invisible by construction; the
VISIBLE pair byte-identical] + the transitionProperty metadata [the v3
6-prop list vs the v4 gradient-var compile — the v95 family, never
pinned; the duration 0.15s IDENTICAL both sides]). The pin appended
(append-pin-v140.py — the at-rest rung -> the SEARCH-HOVERED rung
{hoverMatch true + the unchanged at-rest chrome} -> the restored rung;
the V94-COLLISION-safe axis set; the STRUCTURAL finder; the input never
clicked) GREEN on the first run; the authoritative --list: 343 in 24
files.

THE PIN-SANITY MUTATION — the HOVER-TINT form: hover:bg-[#f5f5f5]
prepended to the Input's className at input.tsx:10 (the single className
line; the component serves EVERY Input in the app — the WIDER-FILE
blast radius noted, the sole-failure criterion verified on the FULL
ITEMS SWEEP ALONE) — cascade-checked BY CONSTRUCTION (hover-scoped: the
at-rest rung + the v37 S2 focus-visible pin + the v64 at-rest geometry
census + the v47 dialog-input focus composites untouched [focus engages
no hover utility]) AND it simulates the exact drift the pin exists to
guard (a hover tint appearing on the search input — the clone diverging
from the reference's inert-hover chrome). The SOLE FAILURE verified
live — 1 failed [the pin alone] + 53 passed in the FULL items sweep,
the failure diff EXACTLY the predicted hovered-rung axis (the input's
bg "rgb(245, 245, 245)" — the mutation's tint — received vs the
persisted at-rest "rgba(0, 0, 0, 0)" expected, hoverMatch true
preserved, the border/color axes untouched); restored (git diff src/ =
0 lines) + the FULL REBUILD + the post-restore regression 145 passed
(items 54 + networth 40 + dashboard 52 — the v139/v138/v134 pins'
different-file immunity verified live).

The ship chain: **343 e2e zero flakes** (95+93+76+82 = 346 executions =
343 unique — the +1 landing in ch1 [items]; both closed watches green
through the chain); 35/35 smoke; the screenshots **16/16 captured — ALL
byte-identical** (the same-day law: both this cycle and v139 captured
Nov 1 UTC, every date-bearing surface rendering identically under the
persisted seed); the dev evidence 4/4 byte-identical + VLM-verified
(the menu proof {"url":"/income","docSW":390,"navLandmark":true}; the
dev-shots scripts derived v139 -> v140 with the version-swap-only
verification on both).

The v141 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence's SECOND-PASS next-oldest
candidate — **the v135-era LOGIN + CALCULATOR pair** (the LOGIN view +
the CALCULATOR dialog at desktop 1280x800, the v59-era login+calculator
pair's surface family, last re-shot v135 — now the oldest remaining
[v135 < v136 < v137 < v138]; the pair's THIRTEENTH re-run bracket
[v59 -> v66 -> v75 -> v81 -> v87 -> v93 -> v99 -> v105 -> v111 -> v117
-> v123 -> v129 -> v135 -> v141] to be verified against the v135
lineage's own records before the derivation — the v135 plan's own
header records the TWELFTH ordinal on its 13-entry bracket [v59 the
original, one entry — 13 entries − the original = 12 re-runs],
consistent, no off-by-one this lineage; the v135 shots header carries
the FULL bracket form, the verification source), (2) the axe-core watch
at its next re-check point (only a 5.x wrapper changes the calculus),
(3) the npm-audit watch at its re-check point (only a new advisory in
the next/zod ranges changes the calculus), (4) the deferred
reference-write censuses (unchanged — out of bounds under the v46
read-only rule), (5) the residual-class watch (both flake classes
CLOSED by the v136 dual-stack/localhost fix — the watch continues in
the standing form for any NEW class).

"""

text = text.replace(anchor, anchor + SECTION, 1)
io.open(PR, "w", encoding="utf-8").write(text)
print("D6 probe README: the v140 cycle section + the v141 queue inserted")
