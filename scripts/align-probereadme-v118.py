#!/usr/bin/env python3
"""D6 docs alignment for the v118 cycle — the probe README's v118 section
(inserted newest-first, before the v117 section) carrying THE
WRAPPER-MECHANISM CONSTRUCT CLASS lesson and the v119 queue. Insert-after
WITH the idempotency guard (the v113 lesson)."""
import sys

README = "scripts/parity-probes/README.md"
t = open(README, encoding="utf-8").read()

SECTION = """## The v118 cycle (the v112-era NETWORTH + drill-down-DASHBOARD pair's NINTH re-run — Session 153)

The re-run cadence's next-oldest candidate: the v112-era NETWORTH +
drill-down-DASHBOARD pair (the desktop 1280x800 FULL-PAGE state of
(1) the NETWORTH view and (2) the DASHBOARD's drill-down EXPANDED
state, last re-shot v112 — now the oldest remaining [v112 < v113 <
v114 < v115 < v116 < v117]; the pair's NINTH re-run bracket [v60 -> v67
-> v76 -> v82 -> v88 -> v94 -> v100 -> v106 -> v112 -> v118]; the
FORTY-FIRST consecutive queue/ledger agreement — the surface names
verified against vlm-shots-v112.sh's own header BEFORE the derivation).
**A PIN-ONLY cycle for src/ — zero production-code changes** + one e2e
pin; the cycle's standing items: the axe watch (NO DRIFT — 4.14.0
holds, only a canary sha prerelease beyond, the v68 dedupe verified),
the npm-audit watch at its ninth re-check (0 vulnerabilities — the
v110 bump holds [next 16.4.3 + zod 4.6.7]), the 112th standing checks
(ALL GREEN — the mobile menu the 112th consecutive green; the
reference's four bugs all live; the data census clean on the FIRST
reads, no render-race hit this cycle).

**F0 baseline FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace**
(the RESET class — the v117 environment did not persist; the repo
re-cloned from main @ dba644d). The v108 FRESH-CLONE lesson applied
END-TO-END: npm ci (run in the foreground — the v114 silent-death
lesson; 354 entries) with the zod extraction verified INTACT [840/840
files by the total-file count, the src/v4 subdirectory present,
verified BEFORE any gate; one package-lock zod entry — the v68
dedupe]; .env [DATABASE_URL="file:../db/custom.db"] + db/ at the repo
root; db:push + db:seed (7 items / 3 assets / 2 liabilities); BOTH
v1243 playwright binaries verified DIRECTLY (the fresh cache held only
the OLD chromium-1200 pair). The gates: seedcheck exact
(7/1850/2235/0/3/2) · lint · typecheck · 108/108 unit · build (robots +
sitemap prerendered) · **320 e2e ZERO FLAKES** (84+80+77+82 = 323
executions = 320 unique — every chunk green on its FIRST run) · 35/35
smoke. The post-push commit since the v117 parity push (0f657e9)
audited session-log-only [dba644d adds docs/session_285.md — ZERO
src/, tests/, prisma/ or lockfile deltas].

**F3**: the series derived from the v112 lineage (derive-v118-series.py
— the generic swaps + the FOUR exact-fragment history corrections, 4/4
applied on the FIRST run; line counts preserved [84/71/65/328]). The
census BUILT two-half from the start (build-twohalf-v118.py via
derive-build-twohalf-v118.py with the swap-order rule [generic swap
FIRST, the lesson-range bump v92..v111 -> v92..v117, the lineage-note
fixup "the v106-lineage derivation" -> "the v112-lineage derivation"
LAST]; ZERO builder repairs needed this cycle; the TWO census JS
blocks [ARBIT_A 90 lines + ARBIT_B 111 lines] byte-identical across
the halves — the md5 line-block contracts [45b9a439 / 8ed66a88,
verified by marker-based extraction across the source + both halves]).
Both halves executed cleanly (the reaping budget between halves; the
parked pointer at (5,5); read-only — the v46 rule holds; the
drill-down expansion clicks mutate no data; login on the first attempt
both sides).

**The verdicts: NETWORTH DIFFERENT + drill-down DIFFERENT — every flag
DOM-arbitrated to a documented class**: the FAB flags (raised on BOTH
pairs) DISPROVEN live (base44-fab-arbit-v118.sh on the flagged
/networth surface at 1280: fabCount 0 + bodyHasBase44 false on BOTH
sides — the platform-iframe chrome class, the standing disproof form
re-confirmed); the avatar letters the USER-IDENTITY data class; the
nav-highlight flag the v56 SUPERSET delta + perception (the census: bg
rgba(0,0,0,0) transparent on BOTH sides — no green background; the
color/fw asymmetry the documented superset); the hero progress % the
PCT data class (fillW 173-vs-357); the donut % labels the
EACH-SITE'S-DATA + perception class (count 4 / labelFs 16px / sectors
3 byte-identical — the reference DOES render its labels); the stat
counts / the extra category the SEED-DATA class; **the "Total Expense
(singular) vs Total Expenses (plural)" flag DISPROVEN live — the
reference reads "Total Expenses" PLURAL on ALL SIX instances (the 3
tab-button SPANs + the 3 stat-card H3s), the full family byte-identical
to the clone's down to every chrome axis (statlabel-explore-v118.sh +
statlabel-explore-clone-v118.sh) — the VLM TEXT-MISREAD class**. The
both-sides census compared AXIS-BY-AXIS by the persisted
compare-v118-census.py (**73 axes: 67 identical + 6 documented-class
deltas, ZERO new** — navHighlight.color/fw the v56 superset delta;
avatarLetter the user-identity data class; progress.fillW the pct data
class; donutLabels.texts the each-site's-data class; labelBlock.w the
v82 DATA-CONDITIONAL width class [the 48px figure's text length]) —
reproducing the v106/v112 census values EXACTLY, zero drift on every
axis. NOTE: the census lines are DOUBLE-ESCAPED in the halves' logs
(agent-browser prints the JSON object itself serialized as a quoted
string — structural quotes escaped once, nested quotes inside values
like glyphSig twice); the recovery is a DOUBLE json.loads (the
compare-v118-census.py parser form).

**F4 [PIN] — THE WRAPPER-MECHANISM CONSTRUCT CLASS (the cycle's find,
PIN-ONLY)**: the pin-candidate survey targeted the /networth PAGE-HEADER
ROW at 1280 (the element family every 1280 networth census walked past:
the v60 view census jumps straight to the summary card's label; the
v67/v82 pins the card interior; the v94 the GROUP headers; the v100 the
tablist junction; the v106 the asset cards — the PAGE header row pinned
ONLY at 390 before this [the v69 F3 pin, measured on the CLONE only];
the v14 G3 test pins the chip's existence + gradient + geometry + the
h1 x-positions only). The one-shot both-sides census
(nwheader-arbit-v118.sh) measured the family BYTE-IDENTICAL on every
VISUAL axis — the row {flex/center/gap 12px/h 60}, the chip {48x48 /
radius 12px / the 135deg forest->lime gradient / the 24x24 svg}, the h1
{30px/700/36px/rgb(26,58,46)}, the subtitle {16px/400/24px/
rgb(107,114,128)}, the block {h 60 / w 250}, the row->card gap 32, the
card w 960 — with ONE mechanism axis diverging: the row's margin-bottom
(the reference 0px vs the clone 32px). The drill-down
(nwheader-mechanism-v118.sh + nwheader-wrapper-v118.sh, both sides):
**the reference wraps its header row in a SINGLE-CHILD responsive
wrapper** (`flex flex-col md:flex-row justify-between items-start
md:items-center gap-4 mb-8` — the wrapper carries the mb-8 = 32px; the
row itself bare) while the clone puts the mb-8 directly on the row (no
wrapper). The wrapper's census: childCount 1 — the chip+title row alone
(w 310, right 682, NOTHING on the right); justify-between has no second
child to spread. ZERO visual consequence: the pixel arithmetic
identical both sides (the row top 32 / bottom 92, the card top 124, the
gap 32), the 390 rhythm matching too (the v69 pin's gap 32 = the
reference's wrapper mb 32). Notably the clone's OWN dashboard header
uses the reference's wrapper form verbatim (dashboard-view.tsx:927) —
the /networth header is the v14-era simplification, predating the
wrapper's discovery. **THE CLASSIFICATION — the CONSTRUCT class per the
v7 accepted-construct convention (constructs that paint nothing are not
parity axes)**: the single-child wrapper paints nothing, organizes
only — its computed effect is exactly {mb 32}, which the clone achieves
on the row itself; the DOM-tree shape is not the contract (the v72
structural-finder principle). The production-code changes remain
reserved for REAL visual deltas (the six since v46 — all visual).

**THE LESSON (formalized): a STRUCTURAL-layer difference with zero
computed-style consequence on every visible axis is a CONSTRUCT class,
not a parity gap — measure the MECHANISM (which element carries the
margin/gap) before flagging it, and pin the VISUAL contract (the
geometry the user sees), not the mechanism axis. The corollary: when a
census axis diverges, first compute whether ANY pixel the user can see
differs (the position arithmetic: tops/bottoms/gaps of the elements
AROUND the axis); if the arithmetic is identical, the axis is a
mechanism axis — document the class, do not touch src/.**

The pin (tests/e2e/networth.spec.ts, the v118 describe block —
appended by the persisted append-pin-v118.py): the /networth
page-header row census at 1280x800 — the row {display flex / alignItems
center / gap 12px / mb 32px — the clone's own rhythm, the reference's
living on its wrapper: the construct class documented in the pin's
comment} + the chip {48x48 / radius 12px / the 135deg gradient} + the
h1 {30px/700/lh 36px} + the subtitle {16px/400/lh 24px} + the block {h
60 / w 250 — the TEXT BLOCK governs the row height, the v65/v69
lesson} + the row->card gap 32 + the card w 960 context + the docSW
1280 guard; the finders STRUCTURAL (the h1 by its text; the block as
its parent; the row as the block's parent; the chip as the row's
svg-carrying child; the card via the "Total Net Worth" label walk-up —
the v60 finder). The PIN-ONLY form (the v116 precedent): the pin
written asserting the measured clone values -> the standalone GREEN run
(no red phase — nothing to fix, the values already hold) -> the 35/35
networth surface regression -> the full-suite ship chain.

**F5 the ship chain**: lint · typecheck · 108 unit · 0 vulnerabilities ·
**321 e2e zero flakes** (85+80+77+82 = 324 executions = 321 unique) ·
35/35 smoke. **The screenshots 16/16 byte-IDENTICAL (the same-day-seed
law — the seed and the capture ran the same day, the relative dates
matching)**; the dev evidence 4/4 byte-identical + VLM-verified (the
menu proof: /income, docSW 390, navLandmark true; the menu open with
all 5 links + the brand; the sheet closed post-nav; the dashboard
clean — the dev-shots scripts derived v117->v118 with the
version-swap-only verification).

The v119 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v112-era NETWORTH + drill-down-DASHBOARD pair (the v113-era
DASHBOARD pair — the DASHBOARD at desktop 1280x800 FULL-PAGE, both v61
target surfaces below the fold on the same view: (1) the BUDGET
GUIDELINES card (the tinted, bordered 50/30/20 rows) and (2) the
QUICK-ACTION card row (the three Add Income / Add Savings / Add
Expense card buttons), last re-shot v113 — now the oldest remaining
[v113 < v114 < v115 < v116 < v117 < v118]; the pair's next re-run
bracket [v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113
-> v119] to be verified against vlm-shots-v113.sh's own header before
the derivation — NOTE the v113 header's own ordinal reads SEVENTH for a
9-entry bracket, an off-by-one vs the v112-lineage convention (EIGHTH
for 9 entries); the BRACKET is the authority per the queue-prose
verification lesson, so v119 = the NINTH re-run by the consistent
convention), (2) the axe-core watch at its next re-check point (only a
5.x wrapper changes the calculus), (3) the npm-audit watch at its
re-check point (only a new advisory in the next/zod ranges changes the
calculus), (4) the deferred reference-write censuses (unchanged — out
of bounds under the v46 read-only rule).

"""

if "## The v118 cycle" in t:
    print("ALREADY APPLIED: the v118 section — skipped")
    sys.exit(0)
anchor = "## The v117 cycle (the v111-era LOGIN + CALCULATOR pair's NINTH re-run — Session 152)"
if t.count(anchor) != 1:
    print(f"AMBIGUOUS/MISS anchor ({t.count(anchor)} hits)")
    sys.exit(1)
t = t.replace(anchor, SECTION + anchor, 1)
open(README, "w", encoding="utf-8").write(t)
print("aligned scripts/parity-probes/README.md (the v118 section + the v119 queue)")
