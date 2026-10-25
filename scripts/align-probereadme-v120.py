#!/usr/bin/env python3
"""D6 docs alignment for the v120 cycle — the probe README's v120 section
(inserted newest-first, before the v119 section) carrying the v121 queue.
Insert-after WITH the idempotency guard (the v113 lesson)."""
import sys

README = "scripts/parity-probes/README.md"
t = open(README, encoding="utf-8").read()

SECTION = """## The v120 cycle (the v114-era MOBILE TWINS pair's NINTH re-run — Session 155)

The re-run cadence's next-oldest candidate: the v114-era MOBILE TWINS
pair — BOTH mobile 390x844 full-page twins: (1) the /NETWORTH view (the
v63-era pair's surface) and (2) the DASHBOARD (the v62-era mobile twin's
surface), last re-shot v114 — now the oldest remaining [v114 < v115 <
v116 < v117 < v118 < v119]; the pair's NINTH re-run bracket [v62/v63 ->
v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120]; the
FORTY-THIRD consecutive queue/ledger agreement — the surface names
verified against vlm-shots-v114.sh's own header BEFORE the derivation,
with the v114 header's own EIGHTH ordinal CONSISTENT with its 9-entry
bracket [v62/v63 the original pair — no off-by-one this lineage, unlike
the v113 lineage's SEVENTH-vs-bracket]. **A PIN-ONLY cycle for src/ —
zero production-code changes** + one e2e pin; the cycle's standing
items: the axe watch (NO DRIFT — 4.14.0 holds, only the canary sha
prerelease beyond, the v68 dedupe verified), the npm-audit watch at its
eleventh re-check (0 vulnerabilities — the v110 bump holds [next
16.4.3 + zod 4.6.7]), the 114th standing checks (ALL GREEN — the mobile
menu the 114th consecutive green; the reference's four bugs all live;
the data census clean on the FIRST reads, no render-race hit this
cycle).

**F0 baseline FULLY GREEN on the PERSISTED workspace** (the first
PERSISTED-class cycle in the recent ledger — the v119 environment
survived between the cycles: node_modules 354 entries, the db at
<repo>/db/custom.db, BOTH playwright v1243 binary pairs in the cache;
only the git pull needed for the session_291.md handoff [0455e0e ->
a060896, session-log-only]). The seedcheck exact (7/1850/2235/0/3/2)
before any gate; the gates: lint · typecheck · 108/108 unit · build
(robots + sitemap prerendered) · **322 e2e ZERO FLAKES** (86+80+77+82 =
325 executions = 322 unique, every chunk green on its FIRST run) ·
35/35 smoke. The post-push commits audited session-log-only.

**F2 the 114th standing checks ALL GREEN** (the pair derived from the
v113 pair via the persisted derive-standing-v120.py — three token
families, normalize-back diff clean, zero old tokens): the reference's
four bugs all live [toast-blocker hitIsBurgerChild:false; sheet-trap
overlayCount:1 after nav; no-landmark navLandmark:false; the 464px
/networth overflow measured docSW 464 directly]; the data census clean
on the FIRST reads; the SEO pair live both sides; the clone's mobile
menu VERIFIED WORKING the 114th consecutive time (zero overflow at 390
on all five views); the seedcheck exact after the clone half.

**F3 the re-run pair**: the probe series derived from the v114 lineage
(the persisted derive-v120-series.py — the generic swaps + FIVE
exact-fragment history corrections, 5/5 applied on the FIRST run, line
counts preserved 61/48/69/220); the census BUILT two-half from the
start (build-twohalf-v120.py — ref-arbit-v120.sh + clone-arbit-v120.sh,
the TWO census JS blocks [NW_CENSUS 42 + DASH_CENSUS 87 lines]
byte-identical across the halves, the md5 line-block contracts
[82cf8a43 / 85e4ec7e — the v102/v108/v114 census blocks VERBATIM]; the
STALE clonearbit108 SESSION TOKEN in the v114 builder's clone_login
FIXED to clonearbit120 in this lineage — the v114 derivation had
inherited the v108 token unbumped). **The verdict BOTH PAIRS DIFFERENT
— the pair's documented verdict class (the same verdict family as the
v84/v90/v96/v102/v108/v114 re-runs)** — every flag DOM-arbitrated: the
NETWORTH stat-tiles stacking + card height the v41 mobile-superset
class (census-confirmed: statGrid.cols 2-col-vs-1-col, tiles
176-vs-294, card 432x333-vs-358x421, medallion clipsViewport
true-vs-false); the trend-icon circle the PERCEPTION-ARTIFACT class
(the census axis trendIcon 32x32 BYTE-IDENTICAL both sides + the
medallion 64x64 identical — the VLM's own contradictory descriptions
across the two passes the disproof); the card grouping/figures the
SEED-DATA classes; the Base44 overlay the PLATFORM-CHROME class
DISPROVEN LIVE at BOTH flagged surfaces (base44-fab-arbit-v120.sh:
fabCount 0 + bodyHasBase44 false on BOTH sides at BOTH surfaces — the
overlay lives in the reference's platform iframe chrome); the progress
bar/donut/labels the SEED-DATA classes; the subtitle wrap the RANGE-
WALK line bucketing (the DASH width-guard class's documented
consequence: the ref's 363px-vs-clone's 358px content width buckets the
same text differently; the line TOPS identical 123/147, the computed
chrome identical). The census compared AXIS-BY-AXIS by the persisted
compare-v120-census.py: **55 axes — 37 identical + 18 documented-class
deltas, ZERO new** (the v41 mobile-superset family + the DASH
width-guard family + the Range-walk line texts) — reproducing the v114
census values EXACTLY (the same 55/37/18 split), zero drift on every
axis.

**F4 THE PIN — the /networth LIABILITY-CARD census at 390 (the
never-pinned family, PIN-ONLY — the FAMILY-CONSISTENCY form, the v29
G1 precedent)**: the twins' own surfaces among the most-pinned in the
codebase (the rejected candidates documented with the collision
evidence — the section-row/facts-row/spending-header 390 twins the
v94/v106/v101 1280 collisions [the v114 rejections standing]; the
640-band form REJECTED [dashboard-view carries ZERO sm: variants — the
640 rendering = the 390 rendering for every family, any 640 pin either
duplicates the 390 values cascading to the 390 pin or the aggregate
band state already pinned by the v42 F2/F3 censuses]; the empty-state
REJECTED [the clone seeds 2 liabilities]); the candidate the /networth
view's LIABILITY CARD family — NEVER pinned at ANY viewport (only the
v29 G1 badge family-consistency pin + the interest-line TEXT existence
+ the group headers + the Add Liability gradient; the ASSET twin fully
pinned v46/v47/v106). The FAMILY-CONSISTENCY form: the reference's own
liability data is EMPTY (0 liabilities — no cards to measure; the v46
read-only rule forbids writing reference data), the chrome family =
the AssetCard's pinned contract BY CONSTRUCTION (net-worth-view.tsx:169
the identical class strings to :65; the v46 F1 liability-twin fix's
own comment documents the shared mb-4 P + space-y-2 facts stack). The
one-shot census (liabcard-arbit-v120.sh — the RADIX TAB-SWITCH LESSON
baked in: the tabs activate on pointerdown, the bare el.click() leaves
the tab inactive, the full PointerEvent/MouseEvent sequence the fix)
measured the family: the card {358x218 — the asset's pinned 194 + the
third facts row's 16 + the space-y-2's 8, THE ARITHMETIC EXACT /
radius 12px / pad 20px / border / shadow / transition all the v47
contract}, the head row {mb 12 / flex / flex-start / space-between /
h 52}, the dot {8x8 / 9999px / the LIABILITY_COLOR orange
rgb(224,122,59)}, the h4 {16px/600/forestDark}, the badge {the v29 G1
family}, the value P {24px/700/the orange/mb 16px — the v46 F1
liability twin}, the facts {12px/gray/rowGap 8px/rowCount 3 — the
liability-ONLY axis: institution + interest + updated vs the asset's 2
rows}, the three rows {flex/center/gap 8px/h 16/icon 12x12}, the
valueToFactsGap 16, the docSW 390. The +1 e2e pin
(tests/e2e/networth.spec.ts, appended by the persisted
append-pin-v120.py): the family census + the docSW guard, the finders
STRUCTURAL, the tab switch by Playwright's locator click (the full
pointer sequence — the census lesson encoded in the spec form); the
PIN-ONLY form (the standalone GREEN run + THE PIN-SANITY MUTATION
[net-worth-view.tsx:223 the interest row's gap-2 -> gap-3, LINE-SCOPED
— the pin FAILED at rows[1].gap ALONE, 8px -> 12px, every other axis
green; the 6 other same-class lines untouched; restored + the full
rebuild + the 36/36 post-restore networth regression]).

**F5 the ship chain**: lint · typecheck · 108 unit · 0 vulnerabilities ·
**323 e2e zero flakes** (87+80+77+82 = 326 executions = 323 unique) ·
35/35 smoke. **The screenshots 16/16 byte-IDENTICAL (the same-day-seed
law — the seed and the capture ran the same day, the relative dates
matching)**; the dev evidence 4/4 byte-identical + VLM-verified (the
menu proof: /income, docSW 390, navLandmark true; the menu open with
all 5 links + the brand; the sheet closed post-nav; the dashboard
clean — the dev-shots scripts derived v119->v120 with the
version-swap-only verification). The v119-RESIDUAL AGENTS.md
DUPLICATION FIXED this cycle (the v119 paragraph's tail carried the
workspace-class sentence 3 EXTRA times — a latent v119-cycle defect,
the duplicates removed in the docs alignment D0).

The v121 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v114-era MOBILE TWINS pair (the v115-era ITEMS pair — the
ITEMS view (income + expenses) at desktop 1280x800 FULL-PAGE, the
v57-era items pair's surface family, last re-shot v115 — now the oldest
remaining [v115 < v116 < v117 < v118 < v119 < v120]; the pair's TENTH
re-run bracket [v57 -> v64 -> v70 -> v79 -> v85 -> v91 -> v97 -> v103
-> v109 -> v115 -> v121] to be verified against vlm-shots-v115.sh's own
header before the derivation — the v115 header's own NINTH ordinal is
consistent with its 10-entry bracket [v57 the original], so v121 = the
TENTH re-run by the same convention), (2) the axe-core watch at its next
re-check point (only a 5.x wrapper changes the calculus), (3) the
npm-audit watch at its re-check point (only a new advisory in the
next/zod ranges changes the calculus), (4) the deferred reference-write
censuses (unchanged — out of bounds under the v46 read-only rule).

"""

if "## The v120 cycle" in t:
    print("ALREADY APPLIED: the v120 section — skipped")
    sys.exit(0)
anchor = "## The v119 cycle (the v113-era DASHBOARD pair's NINTH re-run — Session 154)"
if t.count(anchor) != 1:
    print(f"AMBIGUOUS/MISS anchor ({t.count(anchor)} hits)")
    sys.exit(1)
t = t.replace(anchor, SECTION + anchor, 1)
open(README, "w", encoding="utf-8").write(t)
print("aligned scripts/parity-probes/README.md (the v120 section + the v121 queue)")
