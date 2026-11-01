#!/usr/bin/env python3
"""align-probereadme-v138.py — D6 of the v138 docs alignment: insert the
v138 cycle section + the v139 queue into scripts/parity-probes/README.md,
immediately after the v138 queue paragraph (the v137 cycle's own section
form) and before the v121 section. D0 discipline: the insert anchor
verified 1-hit BEFORE any write; the script refuses on any miss."""
import io
import sys

PR = "scripts/parity-probes/README.md"
text = io.open(PR, encoding="utf-8").read()

anchor = (
    "CLOSED by the v136 dual-stack/localhost fix — the watch continues in\n"
    "the standing form for any NEW class).\n"
    "\n"
)
n = text.count(anchor)
if n != 1:
    print(f"ANCHOR MISS (the v138 queue tail): {n} hits")
    sys.exit(1)

SECTION = """## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)

The re-run cadence's next-oldest candidate: the v132-era MOBILE-TWINS
pair — the /NETWORTH view + the DASHBOARD, both FULL-PAGE at mobile
390x844 (the v62/v63-era twins' surface family), last re-shot v132 —
now the oldest remaining [v132] — the LAST entry of the v127–v132
rotation pool; the pair's TWELFTH re-run bracket [v62/v63 -> v69 -> v78
-> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120 -> v126 -> v132 ->
v138]; the SIXTY-FIRST consecutive queue/ledger agreement — the surface
names verified against the v132 lineage's own records BEFORE the
derivation (the v132 plan's own header: the ELEVENTH ordinal on its
12-entry bracket [v62/v63 the original pair, one entry — no off-by-one
this lineage]; the v132 shots header carries the FULL bracket form —
the documented verification source). **A PIN-ONLY cycle for src/ — zero
production-code changes (the eighth PIN-ONLY cycle in the last nine) +
one e2e pin (340 -> 341)**; the cycle's standing items: the axe watch
(NO DRIFT — 4.14.0 holds, the v68 dedupe verified), the npm-audit watch
at its twenty-ninth re-check (0 vulnerabilities --omit=dev — the v110
bump holds [next 16.4.3 + zod 4.6.7]; the 16 moderate the accepted
dev-only ESLint braces chain), the 132nd standing checks (ALL GREEN —
the reference's four bugs live; the data census clean on the FIRST
reads; the clone's mobile menu VERIFIED WORKING the 132nd consecutive
time; zero overflow at 390 on all five views; the seedcheck exact after
the clone half).

The baseline GREEN ON THE FIRST CHAIN (the SAME-PERSISTED workspace —
the v137 environment held through the session boundary: node_modules 354
entries intact, BOTH chromium pairs [1200 + 1243] in the cache, the .env
[DATABASE_URL="file:../db/custom.db"] + db/ at the repo root intact with
the v137-cycle seed, the repo pulled to main @ 22fa2ba; the seedcheck
EXACT 7/1850/2235/0/3/2 before any gate — under the env -u discipline,
the sandbox DATABASE_URL pollution live as documented; lint, typecheck,
108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e [343
executions = 340 unique, ZERO flakes], 35/35 smoke; the production-seam
audit clean; skills/ excluded).

The probe series derived from the v132 lineage (derive-v138-series.py —
the generic swaps incl. the FOUR explicit session-token families
[refvlm/clonevlm + refarbit/clonearbit arbit — the tokens carry '132'
without the 'v' prefix] + SIX history-correction fragments [the plan
pointer "the v131 plan's own suggestion" -> "the v137 plan's"; the era
marker last re-shot v126 -> v132 + the oldest-remaining list [v126 <
... < v131] -> [v132]; the ordinal ELEVENTH -> TWELFTH + the bracket
extended [-> v120 -> v126 -> v138] -> [-> v120 -> v126 -> v132 -> v138]
in the three corrected files; the verdicts window "the v84/v90/v96/v102/
v108/v126 re-runs" -> "...v108/v132 re-runs"; the arbit census-axes
provenance "The v126 census axes" -> "The v132 census axes"], all applied
on the FIRST run, zero residual, line counts preserved 60/47/68/219 ==
the v132 lineage exactly; bash -n + node --check clean; the clone file
verified zero era tokens — no corrections needed, the v132 derivation's
own finding). The two-half builder derived (derive-build-twohalf-v138.py
— the session-token bump clonearbit132 -> clonearbit138 FIRST [the v121
stale-session-fix precedent: the built clone half's session namespace
AGREES with the combined arbit-v138.sh's own token] + the generic swap +
the lesson-range bump v92..v131 -> v92..v137 as the BARE range token +
the lineage-note fixup "build-twohalf-v126.py" -> "build-twohalf-v132.py"
LAST [the v110 swap-order rule]). The comparator derived
(derive-compare-v138.py — the explicit /tmp/vlm132 -> /tmp/vlm138
log-path swap + the provenance citations re-pointed at the v132
measurement; the v132 derivation's latent 'textax' typo fixed in this
derivation's residual loop — the correct text[max(0, ...)] slice form).
The verify script derived (derive-verify-twohalf-v138.py — the lineage-
citation chain extended v102/v108/v114/v120/v126 -> +v132; the digests
UNCHANGED — the census JS blocks carry no version tokens). The halves
built + the TWO-block md5 contract verified by the direct THREE-WAY
python extraction (verify-twohalf-v138.py — NW_CENSUS 42 lines md5
82cf8a43 + DASH_CENSUS 87 lines md5 85e4ec7e, byte-identical across
arbit-v138.sh + ref-arbit-v138.sh + clone-arbit-v138.sh — **the
v102/v108/v114/v120/v126/v132 lineage values VERBATIM, carried
byte-identical through the version-swap derivation**).

The VLM pairwise run TWICE with full log capture
(/tmp/vlm138/vlm-pass{1,2}.log): pass 1 BOTH PAIRS DIFFERENT / pass 2
BOTH PAIRS DIFFERENT — **the consistent-verdict form, the pair's
DOCUMENTED VERDICT CLASS** (the same verdict family as the v84/v90/v96/
v102/v108/v114/v120/v126/v132 re-runs). Every flag in both passes in the
documented classes, arbitration-free: the summary-card tiles
side-by-side-vs-stacked the v41 MOBILE-SUPERSET class (the reference's
own 464px overflow + fixed 2-col tiles vs the clone's fitting 1-col
stack); the trend-icon claims the PERCEPTION-ARTIFACT class (the
contradictory descriptions across the passes — pass 1 "solid white
circle vs semi-transparent light green" / pass 2 "smaller and less
prominent" — while the census axes medallion 64x64 + trendIcon 32x32 are
BYTE-IDENTICAL both sides, the v120/v126/v132 arbitration's own disproof
form); the "Edit with Base44" tooltip/FAB claims the PLATFORM-CHROME
class (BOTH passes, BOTH pairs); the hero allocation pct + balance + the
progress-bar length + the donut proportions + the stat amounts/counts
the PCT/seed-data classes; the subtitle wrap the RANGE-WALK
line-bucketing class (the v62 family); the pass-2 tab-bar spacing claim
the v53-documented WIDTH family (the reference's own 432-wide list
inside its 464-overflow page vs the clone's fitting 358 — the internal
chrome byte-parity pinned green by the v53 F1 census in this cycle's
baseline). The both-sides census compared axis-by-axis
(compare-v138-census.py): **55 axes — 37 identical + 18
documented-class deltas, ZERO new — REPRODUCING the v132 census values
EXACTLY** (the same 55/37/18 split, zero drift on every axis; the 18
documented = the v41 mobile-superset family [docSW 464/390, the
card/statGrid/tiles/medallion width+stacking consequences] + the DASH
width-guard family [docSW 395/390, the subtitle/breakdownCard 5px width
consequences + the Range-walk line bucketing]). The seedcheck exact
after the clone half (7/1850/2235/0/3/2).

THE PIN (the NETWORTH TABLIST TRIGGER's OWN-HOVER LADDER at mobile 390 —
PIN-ONLY, +1 e2e = 341): the candidate survey found the tablist
trigger's own-hover path entirely unpinned (the v5 G3 pin the at-rest
2-col grid + the active green state; the v30 G2 the ROVING keyboard; the
v50 F2 the full chrome at 640; the v53 F1 the full chrome at 390 — every
tab census AT-REST; the trigger's own-hover END-STATE held by NO spec at
ANY viewport; both triggers reachable at 390 on BOTH sides — the Assets
center REF (126,472) / CLONE (108,422), the Liabilities center REF
(284,472) / CLONE (283,422), both inside the 390 viewport despite the
reference's 464 page overflow). THE CONSTRUCT UNDER TEST: the trigger
carries NO hover: utility (tabs.tsx:24-38 — the focus-visible +
data-[state=active] classes alone), so the own-hover end-state is the
INERT-HOVER contract — the at-rest chrome persisting under each
trigger's own hover. The both-sides one-shot census tabhover-arbit-v138.sh
(the v132 badgehover form adapted to the tablist axes: the ROLE-BASED
finders [button[role=tab] + aria-selected — the v53 form], the
(5,5)-parked ladder, the live-read centers, the two-arg mouse move,
READ-ONLY per the v46 rule — the Radix tabs activate on pointerdown
[the v120 lesson] and a mouse MOVE dispatches no pointerdown, so the
census can never flip the tab) measured the ladder on BOTH triggers —
the ACTIVE and the INACTIVE — CLEAN — NO GAP: the at-rest rung -> the
ACTIVE-HOVERED rung {hoverMatch true + the at-rest chrome UNCHANGED —
the inert-hover contract} -> the INACTIVE-HOVERED rung {hoverMatch true
+ the muted at-rest chrome UNCHANGED} -> the restored rung — IDENTICAL
both sides at every rung; the deltas the documented construct classes
alone (the trigger WIDTH family [REF 212 / CLONE 175 — the reference's
own 432-wide list inside its 464-overflow page, the v53-documented
class] + the shadow LEAD-LAYER count [the v66 invisible class — the
VISIBLE pair byte-identical] + the 0px border token [the
engine-preflight default, renders nothing — deliberately unpinned, the
v89 metadata form]). The pin appended (append-pin-v138.py — the at-rest
rung -> the ACTIVE-HOVERED rung -> the INACTIVE-HOVERED rung -> the
restored rung; the V94-COLLISION-safe axis set; the triggers never
clicked) GREEN on the first run; the authoritative --list: 341 in 24
files.

THE PIN-SANITY MUTATION — the HOVER-TINT form: hover:bg-[#f5f5f5]
prepended to the TabsTrigger's className at tabs.tsx:34 (the single
className line; the component used ONLY by net-worth-view.tsx —
verified: zero other importers) — cascade-free BY CONSTRUCTION
(hover-scoped: the at-rest rungs + the v53 F1 at-rest census + the v30
G2 roving pin [keyboard-driven] + the v124/v130/v132/v136 pins [other
elements] + the panel-switching specs [dialog-buttons/empty-states
click the tab but assert no tab chrome] all untouched) AND it simulates
the exact drift the pin exists to guard (a hover tint appearing on the
trigger — the clone diverging from the reference's inert-hover chrome).
The SOLE FAILURE verified live — 1 failed [the pin alone] + 40 passed
in the FULL networth sweep, the failure diff EXACTLY the predicted
hovered-rung axis (the INACTIVE twin's bg "rgb(245, 245, 245)" — the
mutation's tint — received vs the persisted at-rest "rgba(0, 0, 0, 0)"
expected, hoverMatch true preserved, the color axis untouched; NOTE the
ACTIVE twin's hovered rung stayed GREEN under the mutation — the
data-[state=active]:bg-[#dcfce7] rule holds the same-specificity
cascade, so the mutation's tint surfaces only on the muted twin — the
pin still catches the drift at its first failing rung; the at-rest +
restored rungs GREEN under the mutation); restored (git diff src/ = 0
lines) + the FULL REBUILD + the post-restore regression 143 passed
(networth 40 + dashboard 51 + items 51 + the setup — the v137/v136/v134
pins' different-file immunity verified live).

The ship chain: **341 e2e zero flakes** (93+93+76+82 = 344 executions =
341 unique — the +1 landing in ch3 [networth]; both closed watches
green through the chain); 35/35 smoke; the screenshots **16/16 captured
— 15 byte-identical + 07-add-item-modal the DETERMINISTIC CROSS-DAY
DATE-CLASS refresh** (the first cross-day capture since v131's own: the
modal's todayIso() default shifted Oct 31 -> Nov 1 UTC; the DB-derived
surfaces unchanged — the persisted seed's fixed dates render
identically); the dev evidence 4/4 byte-identical + VLM-verified (the
menu proof: the sheet closed, the heading "Income", the top bar +
toggle + brand; the dev-shots scripts derived v137 -> v138 with the
version-swap-only verification on both).

The v139 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence rotates to the next-oldest
candidate after the v132-era MOBILE-TWINS pair — **the v127–v132
rotation pool now EXHAUSTED; the cadence enters the SECOND PASS (the
v133–v138 pool)** — the oldest remaining the v133-era ITEMS pair (the
ITEMS view [income + expenses] at desktop 1280x800 FULL-PAGE, the
v57-era items pair's surface family, last re-shot v133 — now the oldest
remaining [v133 < v134 < v135 < v136 < v137 < v138]; the pair's
THIRTEENTH re-run bracket [v57 -> v64 -> v70 -> v79 -> v85 -> v91 ->
v97 -> v103 -> v109 -> v115 -> v121 -> v127 -> v133 -> v139] to be
verified against the v133 lineage's own records before the derivation —
the v133 plan's own header records the TWELFTH ordinal on its 13-entry
bracket [v57 the original, one entry — 13 entries − the original = 12
re-runs], consistent, no off-by-one this lineage; the v133 shots header
carries the FULL bracket form, the verification source), (2) the axe-core
watch at its next re-check point (only a 5.x wrapper changes the
calculus), (3) the npm-audit watch at its re-check point (only a new
advisory in the next/zod ranges changes the calculus), (4) the deferred
reference-write censuses (unchanged — out of bounds under the v46
read-only rule), (5) the residual-class watch (both flake classes CLOSED
by the v136 dual-stack/localhost fix — the watch continues in the
standing form for any NEW class).

"""
text = text.replace(anchor, anchor + SECTION)
io.open(PR, "w", encoding="utf-8").write(text)
print("D6 probe README: the v138 section + the v139 queue inserted")
