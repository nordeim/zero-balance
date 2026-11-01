#!/usr/bin/env python3
"""align-probereadme-v139.py — D6 of the v139 docs alignment: insert the
v139 cycle section + the v140 queue into scripts/parity-probes/README.md,
immediately after the v139 queue paragraph (the v138 cycle's own section
form) and before the v137 section. D0 discipline: the insert anchor
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
    print(f"ANCHOR MISS (the v139 queue tail): {n} hits")
    sys.exit(1)

SECTION = """## The v139 cycle (the v133-era ITEMS pair's THIRTEENTH re-run — Session 174)

The re-run cadence's next-oldest candidate: the v133-era ITEMS pair —
the ITEMS view (INCOME + EXPENSES) at desktop 1280x800 FULL-PAGE (the
v57-era items pair's surface family), last re-shot v133 — now the
oldest remaining [v133 < v134 < v135 < v136 < v137 < v138]; the pair's
THIRTEENTH re-run bracket [v57 -> v64 -> v70 -> v79 -> v85 -> v91 ->
v97 -> v103 -> v109 -> v115 -> v121 -> v127 -> v133 -> v139]; the
SIXTY-SECOND consecutive queue/ledger agreement — the surface names
verified against the v133 lineage's own records BEFORE the derivation
(the v133 plan's own header: the TWELFTH ordinal on its 13-entry
bracket [v57 the original, one entry — 13 entries − the original = 12
re-runs, no off-by-one this lineage]; the v133 shots header carries the
FULL bracket form — the documented verification source). THE v127–v132
ROTATION POOL EXHAUSTED — the cadence enters the SECOND PASS (the
v133–v138 pool), the v133-era pair its first entry. **A PIN-ONLY cycle
for src/ — zero production-code changes (the ninth PIN-ONLY cycle in
the last ten) + one e2e pin (341 -> 342)**; the cycle's standing items:
the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified), the
npm-audit watch at its thirtieth re-check (0 vulnerabilities
--omit=dev — the v110 bump holds [next 16.4.3 + zod 4.6.7]; the 16
moderate the accepted dev-only ESLint braces chain), the 133rd standing
checks (ALL GREEN — the reference's four bugs live; the data census
clean on the FIRST reads; the clone's mobile menu VERIFIED WORKING the
133rd consecutive time; zero overflow at 390 on all five views; the
seedcheck exact after the clone half).

The baseline GREEN ON THE FIRST CHAIN (the SAME-PERSISTED workspace —
the v138 environment held through the session boundary: node_modules 354
entries intact, BOTH chromium pairs [1200 + 1243] in the cache, the .env
[DATABASE_URL="file:../db/custom.db"] + db/ at the repo root intact with
the v138-cycle seed, the repo pulled to main @ 69a48d9; the seedcheck
EXACT 7/1850/2235/0/3/2 before any gate — under the env -u discipline,
the sandbox DATABASE_URL pollution live as documented; lint, typecheck,
108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e [344
executions = 341 unique, ZERO flakes], 35/35 smoke; the production-seam
audit clean; skills/ excluded).

The probe series derived from the v133 lineage (derive-v139-series.py —
the generic swaps incl. the FOUR explicit session-token families
[refvlm/clonevlm + refarbit/clonearbit — the tokens carry '133' without
the 'v' prefix] + FOUR history-correction fragments [the era marker
last-re-shot v127->v133 + the later-pairs list v128..v132->v134..v138;
the ordinal TWELFTH->THIRTEENTH + the bracket extended in all four
files], all applied on the FIRST run, zero residual, line counts
preserved 56/48/49/284 == the v133 lineage exactly; bash -n + node
--check clean) + the two-half builder (derive-build-twohalf-v139.py —
the session-token bump clonearbit133->clonearbit139 FIRST [the v121
stale-session-fix precedent] + the lesson-range bump v92..v132->v92..v138
[the BARE range token] + the lineage-note fixup LAST) + the comparator
(derive-compare-v139.py — the generic swap + the provenance citations
re-pointed at the v133 measurement) + the verify script
(derive-verify-twohalf-v139.py — the lineage-citation chain extended
v103/v109/v115/v121/v127->+v133; the digest UNCHANGED). The halves
built + the ONE-block md5 contract verified by the direct THREE-WAY
python extraction (verify-twohalf-v139.py — CENSUS_JS 193 lines md5
b55dcd29, byte-identical across arbit-v139.sh + ref-arbit-v139.sh +
clone-arbit-v139.sh — the v103/v109/v115/v121/v127/v133 lineage value
VERBATIM, carried byte-identical through the version-swap derivation).

The resource discipline applied between every half (the browser daemons
reaped BEFORE every half; both halves + both shot series executed with
first-attempt logins; the full logs captured by the runner redirection —
/tmp/vlm139/{ref-arbit,clone-arbit}.log).

The VLM pairwise run TWICE with full log capture (/tmp/vlm139/
vlm-pass{1,2}.log): pass 1 BOTH PAIRS DIFFERENT / pass 2 BOTH PAIRS
DIFFERENT — the consistent-verdict form, the pair's DOCUMENTED VERDICT
CLASS (the same verdict family as the v133 re-run). Every flag in both
passes in the documented classes: the avatar letter the USER-IDENTITY
class (both passes, both pairs); the "Edit with Base44" FAB claim the
PLATFORM-CHROME/PERCEPTION-ARTIFACT class — claimed in BOTH directions
across the passes (pass 1: present in the clone; pass 2: present in the
reference) and DISPROVEN LIVE by base44-fab-arbit-v139.sh (fabCount 0 +
bodyHasBase44 false on BOTH sides, the flagged /income surface, 1280,
logged-in — the v97..v136 standing disproof form: the FAB never renders
in the app DOM on either side, it lives in the reference's platform
iframe chrome outside the queryable body DOM); the header stats + the
card names/amounts/dates the SEED-DATA classes; the expense footer
payment-method labels the v57 DATA-CONDITIONAL class; the badge
wrap/stacking the v57 wrap/classification-VALUE classes; the grid
item-count the SEED-COUNT class.

The both-sides census compared axis-by-axis (compare-v139-census.py):
187 axes — 163 identical + 24 documented-class deltas, ZERO new —
REPRODUCING the v133 census values EXACTLY (the same 187/163/24 split,
zero drift on every axis: the avatar chrome, the grid + card chrome
[the 3-col 309.328px family], the titleRow, the amount leaf, the footer
+ badge chrome, the filter card on BOTH variants [the search
spanning/not-spanning contract], the page-header family, the docSW 1280
guards). The seedcheck exact after the clone half (7/1850/2235/0/3/2).
NO NEW CLONE GAP on the census axes.

THE PIN — the FILTER-CARD SELECT TRIGGER's OWN-HOVER LADDER at 1280 on
/income (PIN-ONLY — src/ ZERO changes, the ninth PIN-ONLY cycle in the
last ten; +1 e2e = 342): the candidate survey (the ITEMS-pair surfaces'
interaction families swept against the specs' own assertions — the
SPEC-ALIAS lesson) found the filter-card Select trigger's own-hover
path entirely unpinned (the v37 S1 pin the CLOSED category trigger's
focus-visible family; the v64/v70 censuses BOTH triggers' at-rest
geometry; the v50/v53 forms the mobile/640 chrome — every select census
AT-REST; the trigger's own-hover END-STATE held by NO spec at ANY
viewport; both triggers reachable at 1280 on BOTH sides — the category
center (884,167) + the frequency center (1115,167), IDENTICAL
coordinates both sides). THE CONSTRUCT: the trigger carries NO hover:
utility (select.tsx:20-27 — the focus + data-[placeholder] + disabled
classes alone), so the own-hover end-state is the INERT-HOVER contract
— the at-rest chrome persisting under each trigger's own hover. The
both-sides one-shot census selecthover-arbit-v139.sh (the v138 tabhover
form adapted to the select axes: the POSITION-BASED finders
[button[role=combobox] first/second — the reference's triggers carry NO
aria-label, identified by their text "All Categories"/"All Frequencies";
the position form the ONLY form shared by both Radix sites], the
(5,5)-parked ladder, the live-read centers, READ-ONLY per the v46 rule
— the Radix Select opens on pointerdown [the v120 lesson] and a mouse
MOVE dispatches no pointerdown, so the census can never open the
dropdown) measured the ladder on BOTH triggers — the CATEGORY and the
FREQUENCY — CLEAN, NO GAP (the inert-hover contract IDENTICAL both
sides at every rung; the deltas the documented construct classes alone:
the shadow LEAD-LAYER count [the v37 S1's own O1 note — the v3
three-slot vs the TW v4 five-slot construct, every lead a 0px-spread
shadow invisible by construction; the VISIBLE pair byte-identical] +
the transition metadata identical [all/0s both sides — no delta at all
this family]). The pin appended (append-pin-v139.py — the at-rest rung
-> the CATEGORY-HOVERED rung {hoverMatch true + the unchanged at-rest
chrome} -> the FREQUENCY-HOVERED rung -> the restored rung; the
V94-COLLISION-safe axis set; the POSITION-BASED finders; the triggers
never clicked) GREEN on the first run; the authoritative --list: 342 in
24 files.

THE PIN-SANITY MUTATION — the HOVER-TINT form: hover:bg-[#f5f5f5]
prepended to the SelectTrigger's className at select.tsx:25 (the single
className line; the component serves EVERY Select in the app — the
WIDER-FILE blast radius noted, the sole-failure criterion verified on
the FULL ITEMS SWEEP ALONE) — cascade-checked BY CONSTRUCTION
(hover-scoped: the at-rest rungs + the v37 S1/v64/v70 at-rest +
focus-visible pins untouched [focus engages no hover utility]) AND it
simulates the exact drift the pin exists to guard (a hover tint
appearing on the filter trigger — the clone diverging from the
reference's inert-hover chrome). The SOLE FAILURE verified live —
1 failed [the pin alone] + 52 passed in the FULL items sweep, the
failure diff EXACTLY the predicted hovered-rung axis (the category
trigger's bg "rgb(245, 245, 245)" — the mutation's tint — received vs
the persisted at-rest "rgba(0, 0, 0, 0)" expected, hoverMatch true
preserved, the border/color axes untouched); restored (git diff src/ =
0 lines) + the FULL REBUILD + the post-restore regression 146 passed
(items 53 + networth 41 + dashboard 52 — the v138/v137/v133 pins'
different-file immunity verified live).

The ship chain: **342 e2e zero flakes** (94+93+76+82 = 345 executions =
342 unique — the +1 landing in ch1 [items]; both closed watches green
through the chain); 35/35 smoke; the screenshots **16/16 captured — ALL
byte-identical** (the same-day law: both this cycle and v138 captured
Nov 1 UTC, every date-bearing surface rendering identically under the
persisted seed); the dev evidence 4/4 byte-identical + VLM-verified
(the menu proof {"url":"/income","docSW":390,"navLandmark":true}; the
dev-shots scripts derived v138 -> v139 with the version-swap-only
verification on both).

The v140 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence's SECOND-PASS next-oldest
candidate — **the v134-era SAVINGS pair** (the SAVINGS view at desktop
1280x800 FULL-PAGE, the v58-era savings pair's surface family, last
re-shot v134 — now the oldest remaining [v134 < v135 < v136 < v137 <
v138]; the pair's THIRTEENTH re-run bracket [v58 -> v65 -> v74 -> v80 ->
v86 -> v92 -> v98 -> v104 -> v110 -> v116 -> v122 -> v128 -> v134 ->
v140] to be verified against the v134 lineage's own records before the
derivation — the v134 plan's own header records the TWELFTH ordinal on
its 13-entry bracket [v58 the original, one entry — 13 entries − the
original = 12 re-runs], consistent, no off-by-one this lineage; the v134
shots header carries the FULL bracket form, the verification source),
(2) the axe-core watch at its next re-check point (only a 5.x wrapper
changes the calculus), (3) the npm-audit watch at its re-check point
(only a new advisory in the next/zod ranges changes the calculus), (4)
the deferred reference-write censuses (unchanged — out of bounds under
the v46 read-only rule), (5) the residual-class watch (both flake
classes CLOSED by the v136 dual-stack/localhost fix — the watch
continues in the standing form for any NEW class).

"""

text = text.replace(anchor, anchor + SECTION)
io.open(PR, "w", encoding="utf-8").write(text)
print("D6 probe README: the v139 section + the v140 queue inserted")
