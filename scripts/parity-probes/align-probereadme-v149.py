#!/usr/bin/env python3
"""D6 — the probe README alignment for the v149 cycle: insert the v149
section (Session 184) between the v149 queue's end and '## The v138 cycle'
(each cycle section ends with the NEXT cycle's queue — the v148 section's
tail IS the v149 queue; the new v149 section carries the v150 queue)."""
import io
import sys

PATH = "scripts/parity-probes/README.md"

SECTION = """## The v149 cycle (the v143-era DASHBOARD pair's FOURTEENTH re-run — Session 184)

The re-run cadence's third-pass next-oldest candidate: the v143-era
DASHBOARD pair — the DASHBOARD at desktop 1280x800 FULL-PAGE (the
v61-era pair's surface family), last re-shot v143 — now the oldest
remaining [v143 < v144]; the pair's FOURTEENTH re-run bracket
[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 ->
v119 -> v125 -> v131 -> v137 -> v143 -> v149]; the SEVENTY-SECOND
consecutive queue/ledger agreement — the surface names verified
against the v143 lineage's own records BEFORE the derivation (the
v143 plan's own header: the THIRTEENTH ordinal on its 14-entry
bracket [v61 the original, one entry — 14 entries − the original =
13 re-runs, no off-by-one this lineage]; the v143 shots header
carries the FULL bracket form, the verification source). **A PIN-ONLY
cycle — src/ ZERO production-code changes + one e2e pin (352 ->
353): the quick-action SIBLING cards' [Add Savings + Add Expense]
focus-visible ladders at 1280 — the never-pinned keyboard paths of
the v143-pinned family's remaining two cards**; the cycle's standing
items: the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe
verified), the npm-audit watch at its fortieth re-check (0
vulnerabilities --omit=dev — the v110 bump holds [next 16.4.3 + zod
4.6.7]; no new advisories in the watched ranges), the 143rd standing
checks (ALL GREEN — the reference's four bugs live; the data census
clean on the FIRST reads; the clone's mobile menu VERIFIED WORKING
the 143rd consecutive time; zero overflow at 390 on all five views;
the seedcheck exact after the clone half).

The baseline GREEN on the FIRST run (the REBUILT workspace — the
sandbox recycled between sessions: the repo re-cloned at main @
49c7003, npm ci [494 packages], the .env + db/ at the repo root +
the seed re-aligned to the canonical Oct 31 stamps via
scripts/align-seed-dates-v149.ts [the fresh Nov 3 seed shifted -3d
on every DISPLAYED date field — the items 2026-10-21..29 + the
assets'/liabilities' lastUpdated 2026-10-31, amounts untouched],
BOTH chromium pairs [1200 + 1243] available; the seedcheck EXACT
7/1850/2235/0/3/2 before any gate — under the env -u discipline,
the sandbox DATABASE_URL pollution live as documented): lint,
typecheck, 108/108 unit, build [robots + sitemap prerendered], the
4-chunk e2e [355 executions = 352 unique, ZERO flakes], 35/35 smoke;
the production-seam audit clean; skills/ excluded.

The probe series derived from the v143 lineage (derive-v149-series.py
— the generic swaps incl. the FOUR explicit session-token families
[refvlm/clonevlm + refar/clonear arbit — the tokens carry '143'
without the 'v' prefix] + the history-correction fragments [the era
marker last re-shot v137->v143 + the oldest-remaining list
[v137 < v138]->[v143 < v144] + the re-run ordinal
THIRTEENTH->FOURTEENTH + the bracket extended + the agreement
ordinal SIXTY-SIXTH->SEVENTY-SECOND + the re-proves-after windows
v101-v137->v101-v143 + the arbit census provenance "a drift
re-check since v137"->"since v143" + "The v137 verdict"->"The v143
verdict" + the compare banner's ordinal/era], all applied on the
FIRST run, zero residual, line counts preserved 57/42/45/258) + the
two-half builder (derive-build-twohalf-v149.py — the lesson-range
bump v92..v142->v92..v148 + the lineage-note fixup LAST) + the
comparator (derive-compare-v149.py — the provenance citations
re-pointed at the v143 measurement) + the verify script
(derive-verify-twohalf-v149.py) + the 143rd standing pair
(derive-standing-v149.py — the ordinal 142nd->143rd nd->rd plain
replace; normalize-back diff clean, line counts preserved 119/74).
The halves built + the THREE-block md5 contract verified by the
direct THREE-WAY python extraction (verify-twohalf-v149.py — ARBIT_G
[the guidelines census] 61 lines md5 b500dd299e5e9a94eaf07b29facc69db
+ ARBIT_Q [the quick-action census] 58 lines md5
da04e9954976eb58d9aff2b95d2dcfc6 + ARBIT_X [the cross-row gap
census] 25 lines md5 7a381755a22ce55c62f70a053f826852, byte-identical
across arbit-v149.sh + ref-arbit-v149.sh + clone-arbit-v149.sh — the
digests differ from the v143 cycle's by construction [the census JS
blocks' view-label tokens carry the version]).

The VLM verdict IDENTICAL x2 (the cleanest pair form reproduced —
NO style flags, NO FAB claims raised, the first
zero-platform-chrome-claim cycle; the FAB disproof re-run as the
standing re-confirmation per the v43 rule: base44-fab-arbit-v149.sh,
derived from the v143 form with the updated header — fabCount 0 +
bodyHasBase44 false on BOTH sides at 1280 on the dashboard surface,
the v97..v148 standing disproof form re-confirmed). The both-sides
census compared axis-by-axis (compare-v149-census.py): 154 axes —
144 identical + 10 documented-class deltas, ZERO new — REPRODUCING
the v143 census values EXACTLY (the same 154/144/10 split, zero
drift on every axis; the seedcheck exact after the clone half).

The candidate survey found the never-pinned SIBLING keyboard paths
(the Add Savings + Add Expense quick-action cards' FOCUS-VISIBLE
ladders — ZERO focus-visible/ring matches on these two cards across
all 24 spec files; the v143 pin measured the Add Income card only;
the items.spec v146 pin covers the savings-view header button — a
different element on a different view). The discovery census
tabqa2-discovery-v149.sh (both sibling cards' ladders at 1280 on
BOTH sides — the structural finder, the (5,5)-parked pointer, the
REAL focusVisible idiom, the outline family INCLUDING outlineColor,
READ-ONLY) measured the ladders CLEAN — NO GAP: the UA-default ring
contract [outlineStyle auto / width 1px / offset 0px] byte-identical
at the focused rung, the card chrome UNCHANGED under focus (focus !=
hover: boxShadow none, tileScale none, plusOpacity 0.5), the blur
restore clean, the sole delta the documented outlineColor computed
form (REF rgba(10,10,10,0.5) vs CLONE lab(2.74175 0 0.00000596046 /
0.5) — the v43-F2 construct class, the same rendered
near-black-at-50%, never pinned per the v95 discipline). THE PIN
(append-pin-v149.py — the sibling-completion form adapting the v143
pin's measurement idiom: BOTH cards' at-rest -> focused -> blurred
ladders at 1280 + the SIBLING NON-INTERFERENCE cross-check at each
focused rung; the outlineColor axes deliberately NOT asserted) —
green on the current build on the FIRST invocation (the PIN-ONLY
form; no RED step: there is no repair); the authoritative --list:
353 in 24 files.

The pin-sanity mutation — the RING-REMOVAL form
(focus-visible:outline-none added to the QuickActionCard's className
at dashboard-view.tsx:885 — the exact TW-v4-refactor drift class the
pin exists to guard, the same mutation form as the v143 sanity; the
WIDER-FILE blast radius noted [the component serves all three
cards]): the FULL DASHBOARD SWEEP read 2 failed [EXACTLY the v143
Add Income pin + the v149 sibling pin — the shared-construct class]
+ 53 passed, the failure diff EXACTLY the predicted focused-rung
outline axis (outlineStyle "none" received vs "auto" expected — the
fv/focused/boxShadow/width/offset axes preserved); restored (git
diff src/ = 0 lines) + the FULL REBUILD + the post-restore
regression 98 passed (the full dashboard + networth sweeps).

The ship chain: lint, typecheck, 108/108 unit, 0-vuln audit, 353
e2e ZERO flakes (97+96+81+82 = 356 executions = 353 unique — the +1
landing in ch2 [dashboard]), 35/35 smoke, the screenshots 16/16
captured — 16 byte-identical (the same-day law: the capture day Nov
3 UTC == the committed v148 captures' day, the 07-add-item-modal
wall-clock form matching byte-for-byte; every seed-stamped surface
byte-identical under the canonical Oct 31 stamps), the dev evidence
4/4 byte-identical + VLM-verified (the menu proof
{"url":"/income","docSW":390,"navLandmark":true}; the dev-shots
scripts derived v148->v149 with the version-swap-only verification
on both).

The v150 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence's next-oldest candidate —
**the v144-era MOBILE-TWINS pair** (the /networth view + the DASHBOARD,
both FULL-PAGE at mobile 390x844 [the v62/v63-era twins' surface
family], last re-shot v144 — now the oldest remaining [v144]; the
pair's FOURTEENTH re-run bracket [v62/v63 -> v69 -> v78 -> v84 -> v90
-> v96 -> v102 -> v108 -> v114 -> v120 -> v126 -> v132 -> v138 -> v144
-> v150] to be verified against the v144 lineage's own records before
the derivation — the v144 plan's own header records the THIRTEENTH
ordinal on its 14-entry bracket [v62/v63 the original pair, one entry
— 14 entries − the original = 13 re-runs], consistent, no off-by-one
this lineage; the v144 shots header carries the FULL bracket form, the
verification source),
(2) the axe-core watch at its next re-check point (only a 5.x wrapper
changes the calculus), (3) the npm-audit watch at its re-check point
(only a new advisory in the next/zod ranges changes the calculus),
(4) the deferred reference-write censuses (unchanged — out of bounds
under the v46 read-only rule), (5) the residual-class watch (both
flake classes CLOSED by the v136 dual-stack/localhost fix — the
watch continues in the standing form for any NEW class).

"""

text = io.open(PATH, encoding="utf-8").read()
if "## The v149 cycle" in text:
    print("SKIP: the v149 section already present")
    sys.exit(0)

anchor = "the standing form for any NEW class).\n\n## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)"
n = text.count(anchor)
if n != 1:
    print(f"FAIL: the insert anchor {n}x")
    sys.exit(1)

text = text.replace(anchor, "the standing form for any NEW class).\n\n" + SECTION + "## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)")
io.open(PATH, "w", encoding="utf-8").write(text)
print("OK: the v149 section + the v150 queue inserted (D6)")
