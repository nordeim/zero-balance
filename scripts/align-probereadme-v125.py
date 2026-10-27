#!/usr/bin/env python3
"""align-probereadme-v125.py — D6 for the v125 cycle: insert the v125
section (with the v126 queue at its end) into scripts/parity-probes/README.md,
between the v125 queue (the v124 section's tail) and the v121 cycle section.
The v126 queue target derived from vlm-shots-v120.sh's own header (the
corrected entries-minus-one convention): the v120-era MOBILE 390x844
full-page twins — the /networth view (the v63-era surface) + the DASHBOARD
(the v62-era mobile twin), last re-shot v120, the pair's TENTH re-run
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 ->
v120 -> v126]."""
import sys

SECTION = """
## The v125 cycle (the v119-era DASHBOARD pair's TENTH re-run — Session 160)

The re-run cadence's next-oldest candidate: the v119-era DASHBOARD pair —
the BUDGET GUIDELINES card + the QUICK-ACTION card row, both below the fold
on the dashboard at desktop 1280x800 FULL-PAGE, the v61-era pair's surface
family, last re-shot v119 — now the oldest remaining [v119 < v120 < v121 <
v122 < v123 < v124]; the pair's TENTH re-run bracket [v61 -> v68 -> v77 ->
v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119 -> v125]; the FORTY-EIGHTH
consecutive queue/ledger agreement — the surface names verified against
vlm-shots-v119.sh's own header BEFORE the derivation, **THE CORRECTED
ENTRIES-MINUS-ONE CONVENTION APPLIED CLEANLY** (the v124 cycle's own
off-by-one find codified and working as designed: the v119 header's own
NINTH ordinal on its 10-entry bracket [v61 the original] → v125 = the TENTH
— no prose/header conflict this cycle, the first cycle fully under the
corrected convention). **A PIN-ONLY cycle for src/ — zero production-code
changes** (the fourteenth since v46) + one e2e pin; the cycle's standing
items: the axe watch (NO DRIFT — 4.14.0 holds, only the canary sha
prerelease beyond, the v68 dedupe verified), the npm-audit watch at its
sixteenth re-check (0 vulnerabilities — the v110 bump holds), the 119th
standing checks (ALL GREEN — the reference's four bugs live; the data
census clean on the FIRST reads; the clone's mobile menu VERIFIED WORKING
the 119th consecutive time; zero overflow at 390 on all five views; the
seedcheck exact after the clone half).

The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs this cycle (the
workspace the CARRIED-OVER class — the v124 environment persisted, the repo
refreshed via git pull to main @ ca35ae3 [the operator's session_305.md
tail], NO re-provisioning: the zod extraction verified intact 840/840, BOTH
v1243 playwright pairs verified in the cache directly, the seedcheck exact
before any gate; the e2e :3100 isolation verified against the stale :3000
dev server, reaped later at the dev-evidence phase). The verdict: **IDENTICAL
×2 — THE CLEANEST PAIR FORM IN THE LINEAGE** (zero layout/style flags both
passes, NO DOM arbitration needed this cycle; only the expected DATA classes
flagged: the hero allocation % [30.5% vs 62.8%] + balance [$3475.00 vs
$2065.00] the PCT/seed-data class, the donut sector percentages + the
drill-down amounts the EACH-SITE'S-DATA class). The two-half census
(derive-v125-series.py from the v119 lineage — the generic swaps + SEVEN
history-correction families all applied on the FIRST run, zero residual,
line counts preserved 57/224/223/108; build-twohalf-v125.py from the v119
builder — the THREE blocks of the v119 lineage [the guidelines PART G + the
quick-action PART Q + the cross-row PART X], the md5 contracts
b500dd29/da04e995/7a381755 verified by direct python extraction
[verify-twohalf-v125.py], the v101/v107/v113/v119 lineage values VERBATIM;
compare-v125-census.py with the /tmp/vlm-path explicit swap): **154 axes —
144 identical + 10 documented-class deltas, ZERO new** — REPRODUCING the
v119 census values EXACTLY (the same 154/144/10 split, zero drift on every
axis; the rendered geometry byte-identical: cardBottom 1122 / gridTop 1462 /
the cross-row gap 340; the ten documented classes — Gcard.shadow the v4
composed-shadow zero-layer superset, Qcards[0..2].label.color/.fw ×6 the
wrapper-vs-leaf finder asymmetry [the v61 label lesson's own class], Qgrid.mt
+ XgridMt + XgridCls the v83 cross-row family's mt-8 rhythm + responsive
class-string superset classes).

The pin: the QUICK-ACTION card's HOVER END-STATE census at 1280
(qahover-arbit-v125.sh — the ONE-SHOT both-sides HOVER-LADDER census,
READ-ONLY on both sites per the v46 rule [login + passive navigation + a
REAL pointer hover only — the hover reveals chrome, it clicks nothing, the
v45 F3b precedent's own surface]; the never-pinned HOVER paths of the
MOST-pinned family on the dashboard: the v45 F3b holds the CARD's
hover:shadow-lg layers only — the sole QA .hover() in the entire suite; the
v61 F3 + v107 pins the AT-REST chrome; the v95 pin the TRANSITION TIMING
metadata — the tile's group-hover:scale-110 [dashboard-view.tsx:890] + the
plus's group-hover:opacity-100 [:899] held by NO spec, verified across all
24 spec files): the ladder — the pointer parked at (5,5), the at-rest
{shadow none / tile {transform none, scale none, 40×40} / plus {0.5, 16}}
byte-identical both sides → the REAL pointer at the live-read card center
(440,723 — identical both sides, never guessed): **the rendered parity
contract IDENTICAL both sides — the tile 40→44×44, the plus 0.5→1,
cardHover true, the shadow's two visible layers byte-identical** — with the
COMPUTED FORM the documented class (the reference's Tailwind v3
transform:matrix(1.1,0,0,1.1,0,0) vs the clone's v4 scale:"1.1" — the v95
transition-property class's hover-state twin) → the pointer re-parked, the
restored rung back to at-rest exactly; the seedcheck exact after the clone
half. **The pin-sanity mutation — the CONDITIONAL form designed-in from the
start (the v124 lesson applied at the design stage)**: group-hover:scale-110
-> group-hover:scale-105 at :890 AND group-hover:opacity-100 ->
group-hover:opacity-90 at :899, both by LINE NUMBER (the identical opacity
token at :602 — the guidelines copy affordance — untouched); the
conditionality preserved so the at-rest holders (v61 F3, v107) are
structurally immune — the SOLE FAILURE verified live: the pin ALONE red at
the hovered axes (the deep-equality diff EXACTLY the predicted 4 lines:
tile w/h 44→42 + scale 1.1→1.05 + plus opacity 1→0.9), the file's 48 others
green, the mobile-layout 390-side file 6/6 green; restored + the full
rebuild + the 54/54 post-restore regression. The ship: 328 e2e zero flakes
(89+86+74+82 = 331 executions = 328 unique); 35/35 smoke; **the screenshots
16/16 byte-identical (the same-day law — even 07-add-item-modal.png, the
v124 day-rollover refresh committed same-day, no refresh needed this
cycle)**; the dev evidence 4/4 byte-identical + VLM-verified (the menu
proof: /income, docSW 390, navLandmark true; the dev-shots scripts derived
v124 -> v125 with the version-swap-only verification; the stale :3000 dev
server reaped as planned at the dev-evidence phase).

The v126 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from the
from-header's own bracket [entries − 1, the original not a re-run], never
the prose): (1) the re-run cadence rotates to the next-oldest candidate
after the v119-era DASHBOARD pair (the v120-era MOBILE 390x844 full-page
TWINS — the /networth view [the v63-era pair's surface] + the DASHBOARD
[the v62-era mobile twin's surface], both FULL-PAGE at mobile 390x844,
last re-shot v120 — now the oldest remaining [v120 < v121 < v122 < v123 <
v124 < v125]; the pair's TENTH re-run bracket [v62/v63 -> v69 -> v78 ->
v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120 -> v126] to be verified
against vlm-shots-v120.sh's own header before the derivation — the v120
header's own NINTH ordinal on its 10-entry bracket [v62/v63 the originals],
so v126 = the TENTH re-run by the entries-minus-one convention), (2) the
axe-core watch at its next re-check point (only a 5.x wrapper changes the
calculus), (3) the npm-audit watch at its re-check point (only a new
advisory in the next/zod ranges changes the calculus), (4) the deferred
reference-write censuses (unchanged — out of bounds under the v46
read-only rule).
"""

path = "scripts/parity-probes/README.md"
text = open(path, encoding="utf-8").read()
if "## The v125 cycle" in text:
    print("ALREADY APPLIED: the v125 section present")
    sys.exit(0)

anchor = "## The v121 cycle (the v115-era ITEMS pair's TENTH re-run — Session 156)"
n = text.count(anchor)
if n != 1:
    print(f"AMBIGUOUS/MISS: {n} hits for the v121-cycle anchor")
    sys.exit(1)

# sanity: the v125 queue (the v124 section's tail) must sit immediately
# before the anchor — the corrected-convention queue prose present
pre = text[: text.index(anchor)]
if "so v125 = the TENTH re-run by the same entries-minus-one" not in pre[-2500:]:
    print("FAIL: the v125 queue not found directly before the anchor")
    sys.exit(1)

open(path, "w", encoding="utf-8").write(text.replace(anchor, SECTION + "\n" + anchor))
print("OK: the v125 section + the v126 queue inserted before the v121 cycle section")
