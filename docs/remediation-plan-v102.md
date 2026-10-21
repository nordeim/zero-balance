# Remediation Plan v102 — the re-run cycle's next-oldest candidate (the v96-era MOBILE 390 twins pair's sixth re-run) + the axe watch + the networth mobile junctions census pin (PIN-ONLY)

The formal narrative: `docs/session_247.md` (the v101 cycle's own narrative
log). The queue: the v101 plan's v102 suggestion — **the ledger-verified
target** (the v101-era docs' suggestion AGREEING with the rotation ledger:
the v96-era MOBILE 390 twins pair [BOTH mobile 390x844 full-page twins —
(1) the /NETWORTH view (the v63-era pair's surface) and (2) the DASHBOARD
(the v62-era mobile twin's surface)], last re-shot v96 — now the oldest
remaining [v96 < v97 < v98 < v99 < v100 < v101]; the pair's SIXTH re-run
[v62/v63 → v69 → v78 → v84 → v90 → v96 → v102] — the TWENTY-FIFTH
consecutive queue/ledger agreement), plus the axe-core watch at its
re-check point and the 96th standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 305.**

## The pre-execution ledger verification (the queue-prose verification lesson, applied)

The rotation ledger's authority is the PROBE LINEAGE, never the prose
queue phrasing. Verified against `scripts/parity-probes/vlm-shots-v96.sh`
before the derivation: its own header reads "the v96 queue (the v95
plan's own suggestion, now confirmed by the rotation ledger: the twins
last re-shot v90 = the oldest remaining [v90 < v91 < v92 < v93 < v94 <
v95]; the pair's FIFTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96])"
— matching the queue's phrasing (the v96-era surface names confirmed:
BOTH mobile 390x844 full-page twins — the /NETWORTH view + the DASHBOARD;
the two v62/v63-era surfaces). The SIXTH re-run bracket [v62/v63 → v69 →
v78 → v84 → v90 → v96 → v102] constructed from the same header's FIFTH
bracket. The standing-checks pair (ref-standing-v96.sh +
standing-checks-v96.sh) derived from v95 across the THREE token families
(v95→v96, 95th→96th, ref95→ref96/clone95→clone96), version-bump-only
verified by normalizing back and diffing clean (zero old tokens remaining
— the persisted derive-standing-v102.py, both halves bash -n clean).

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items
/ 3 assets / 2 liabilities) before any flow ran (the `env -u DATABASE_URL`
discipline — the sandbox's polluted parent DATABASE_URL re-confirmed live
this cycle); lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓
(robots + sitemap prerendered) · **304 e2e ✓** (116 + 93 + 97 chunk
executions across three disjoint file splits of the 24 spec files + the
setup project = 306 total = 304 unique tests — the exact documented v101
state [303 spec + the v101 pin + 1 setup], the count first derived
authoritatively via `playwright test --list`; zero flakes on the FIRST
run) · 35/35 smoke ✓. The workspace: the CARRIED-OVER class (the v99
precedent — the v101 cycle's own fresh-clone environment carries over
unchanged, no re-provisioning: the two commits since the v101 push
[eb3ad12 + de127ed] audited session-log-only [docs/session_246.md +
docs/session_247.md — ZERO src/ or lockfile deltas]; node_modules,
chromium-1243, the tool-results dir, `.env` [DATABASE_URL=
"file:../db/custom.db"], and db/custom.db all verified live).

The codebase audit clean: the production seams re-audited — auth
(scrypt/HMAC + timingSafeEqual), the db-path contract (db-path.ts + its
unit test), the SEO pair (robots.ts allow-all + sitemap.ts 5-URL
structure — both prerendered by the build), the Tailwind v4 mitigations
(`@variant hover (&:hover)` + `@variant group-hover` + the toast
pointer-events fix), the three test tiers; skills/ excluded throughout
(the eslint ignores + the tsconfig exclude verified live).

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (dist-tags: rc/next sha
prereleases only beyond — no stable 4.14.1, no 5.x exists); the
installed wrapper 4.14.0 + the engine 4.14.0; the lockfile holding the
v68 dedupe state (exactly one `node_modules/axe-core` entry); the
engine-contract pin GREEN standalone (2 passed).

### F2 — the 96th standing checks: ALL GREEN (version-bumped from v95 — version-bump-only diffs verified)

ref-standing-v96.sh + standing-checks-v96.sh (version-bumped from v95
via the persisted derive-standing-v102.py across the THREE token
families [v95→v96, 95th→96th, AND the bare session names ref95→ref96/
clone95→clone96]; after normalizing back the files are version-bump-only:
diffed clean, zero old tokens remaining). Reference side: the four bugs
ALL live [toast-blocker `hitIsBurgerChild:false`; sheet-trap
`overlayCount:1` after nav; no-landmark `navLandmark:false`; the 464px
/networth overflow at 390 measured docSW 464 directly]; the data census
UNCHANGED on the FIRST read (networth "1 items · $25,000" / income "1
items · $5000.00" / expenses "4 items · $525.00" — no render-race this
cycle); the SEO pair live. Clone side: R1–R4 ALL GREEN — **the mobile
menu VERIFIED WORKING the 96th consecutive time**
(`hitIsBurgerChild: true`, the sheet opens, closes on nav, the nav
landmark present — the Tailwind v4 mitigation holds), zero overflow at
390 on all five views, the SEO pair live.

### F3 — the re-run pair (the v96-lineage derivation, the two-half census form)

The probe series derived from the v96 lineage (derive-v102-series.py,
persisted): vlm-shots-v102.sh + clone-vlmshots-v102.sh +
vlm-compare-v102.mjs + arbit-v102.sh — the generic swaps
(refvlm96→refvlm102, clonevlm96→clonevlm102, refarbit96→refarbit102,
clonearbit96→clonearbit102, /tmp/vlm96→/tmp/vlm102, v96→v102) followed
by the exact-fragment history corrections (the queue source "the v95
plan"→"the v101 plan", last-re-shot v90→v96, FIFTH→SIXTH, the re-run
bracket extension, the oldest-remaining bracket [v96 < v97 < v98 < v99 <
v100 < v101], the re-runs' verdict note v84/v90→v84/v90/v96, the
census-axes provenance "The v90 census axes"→"The v96 census axes") —
every correction verified applied (the derive script reports each
hit/miss; zero misses this cycle; the line-count-preservation check
green on all four files — the two-half builder inherits the v96 line
boundaries). bash -n + node --check clean on all four; zero residual
old tokens (the legitimate v41/v45/v44/v46/v51/v53/v61/v62/v63/v68/v73/
v75/v84/v90 pin-provenance tokens whitelisted by context). The census
BUILT two-half from the start (build-twohalf-v102.py — ref-arbit-v102.sh
+ clone-arbit-v102.sh, the TWO census JS blocks [NW_CENSUS 42 lines +
DASH_CENSUS 87 lines] byte-identical across the halves — the md5
line-block contract [82cf8a43 / 85e4ec7e — the v96 census blocks
verbatim]). The reaping budget applied as the standing step between
halves (the v89/v91/v100/v102-documented symptom class — the clone
half's FIRST run this cycle hit the fork-retry exhaustion + read EMPTY,
reaped, then clean on the retry).

**The verdict: BOTH DIFFERENT — the pair's documented verdict class (the
same flag-set classes as the v84/v90/v96 re-runs) with every flag
DOM-arbitrated to a documented class:**

- The stat-tile side-by-side-vs-stacked → the v41 mobile-superset class
  (the census: the statGrid cols ref "175.828px 175.844px" 2-col vs
  clone "294px" 1-col, the gap 16px IDENTICAL, the tiles ref 176×84 vs
  clone 294×84 — the h 84 byte-identical — the documented superset fix
  for the reference's own 464px overflow).
- The subtitle wrap-point + the claimed "third line" → the VLM MISREAD
  class (the census is the authority: the clone's subtitle P h 48 =
  exactly 2 DOM lines, the Range-walk line buckets at tops 123/147, the
  chrome byte-identical [fs 16px/fw 400/rgb(107,114,128)/lh 24px,
  blockH 92]; the wrap-point delta itself the v62 width-delta class —
  the reference's own 395px overflow shifts its wrap).
- The top header spacing → the VLM MISREAD class (arbitrated by the
  supplemental headgap-arbit-v102.sh one-shot census: the topbar {h 28,
  bottom 44, static} + the h1 {h 36, top 77, fs 30px, fw 700, lh 36px} +
  gapTopbarToH1 33 + gapH1ToCard 56 — BYTE-IDENTICAL across sides; the
  flag an artifact of comparing the reference's 464-wide full-page image
  against the clone's 390-wide image).
- The tab-bar alignment → the v47/v53 divergence class (the reference's
  own 432-wide list inside its 464-overflow page vs the clone's 358-wide
  in-bounds list with the identical "175px 175px" grid — pinned green by
  the v53 F1 pin).
- The total-figure alignment + the trend-icon appearance → the seed-data
  classes (each site's own figures drive the text length [the v82
  DATA-CONDITIONAL width class] and the trend direction; the figure
  chrome pinned by the v96 F4 pin, the medallion + trendIcon chrome
  byte-identical per the census [64×64 + 32×32]).
- The "Edit with Base44" FAB → the platform-chrome class (the
  v97-documented fabCount 0 + bodyHasBase44 false on BOTH sides — the
  FAB never renders in the app DOM).
- The progress-bar length + the donut proportions → the seed-data
  classes (each site's own data).

The both-sides census (the two-half controlled form) **REPRODUCES the
v96 census values EXACTLY — zero drift on every axis:**

- **NETWORTH (the NW_CENSUS axes)**: the summary card {ref 432×333 /
  clone 358×421 — the documented v41 mobile-superset + width classes},
  the statGrid {cols ref "175.828px 175.844px" vs clone "294px", gap
  16px IDENTICAL, children 2}, the tiles {ref 176×84 ×2 vs clone 294×84
  ×2 — the h 84 byte-identical}, the medallion {64×64, clipsViewport ref
  true / clone false — the R-bug-4 consequence}, the trendIcon {32×32},
  docSW {ref 464 / clone 390 — the superset invariant}.
- **DASHBOARD (the DASH_CENSUS axes)**: the subtitle {text identical,
  rect {ref 363×48 / clone 358×48}, computed {fs 16px, fw 400,
  rgb(107,114,128), lh 24px} IDENTICAL, blockH 92 IDENTICAL, 2 DOM lines
  both sides}, the breakdownCard {h 324 byte-identical, svgCount 7, the
  16/14 svg alternation, children {H3 h 20 + DIV h 238} identical}, the
  spendingCard finder reading the SAME fallback string on BOTH sides
  ("no Spending Breakdown heading" — the heading is a div, not an
  h1-h4, on both sites, the parity-correct rendering), docSW {ref 395 /
  clone 390}.

**NO NEW CLONE GAP — the v102 iteration PIN-ONLY.**

### F4 [PIN] — the networth view's MOBILE junctions census at 390: the card→tablist gap + the assets tablist→section gap + the LIABILITIES panel's own tablist→section junction (PIN-ONLY for src/ — no production-code change; +1 e2e = 305)

The never-pinned family (the FAMILY-EXTENSION pattern — the v100
junction-walk lesson applied to the MOBILE viewport + the SECOND panel's
own junction): the v69 F3 pin (390) walks the header row→card gap only
(rowToCardGap 32); the v41 F2 pin (640) walks the UPPER rhythm
(headerToCard 32 + cardToTablist 32 — at 640); the v53 F1 pin (390) the
tablist's own chrome; the v94 F4 pin (1280) the section row's chrome +
the row-to-group rhythm; the v100 F4 pin (1280) the ASSETS tablist→
section junction — but **the MOBILE junctions at 390 (the card→tablist
gap + the tablist→section gap) and the LIABILITIES panel's own junction
(its own mt-6, at ANY viewport) are NEVER pinned in ANY spec** (the
coverage-map grep across all 24 specs: the only cardToTablist assertion
in the suite the v41 F2 pin's own at 640; the only tablist-to-section
junction assertion the v100 pin's own at 1280 — on the ASSETS tab; zero
specs assert ANY TabsContent margin at 390; zero specs assert the
liabilities panel's junction at any viewport; the only mt-6 assertions
near the liabilities content the summary card's ratio footer — a
different element).

**The pin's own axes first measured byte-identical on BOTH sides** by
the supplemental two-half census (mobjunction-arbit-v102.sh +
mobjunction-clone-v102.sh — BUILT two-half from the start via
build-mobjunction-v102.py, the census JS byte-identical by the md5
line-block contract [83a04c0e — 52 lines]; both halves READ-ONLY login +
passive navigation — the v46 rule holds; the Liabilities tab switched by
the FULL pointer-event sequence — the reference's Radix-style trigger
ignores a bare DOM click, the pointerdown family load-bearing on the
reference side; the seedcheck exact after the clone half):

- The CARD: {w 358 (clone) / 432 (ref — the documented overflow width
  class), bottom 590 / 502} — the anchors.
- The TABLIST: {w 358 / 432 (the width class), h 36 byte-identical,
  template "175px 175px" (clone) / "211.828px 211.844px" (ref — the
  v53-documented width family), pad "4px" byte-identical}.
- The JUNCTION 1 (card→tablist): {gap 32} — **byte-identical across
  sides** (the summary card's mb-8).
- The ASSETS JUNCTION 2 (tablist→section): {gap 24} — **byte-identical
  across sides** (the assets TabsContent's mt-6, re-anchored at the
  mobile viewport).
- The LIABILITIES JUNCTION 3 (tablist→section on the SECOND panel):
  {gap 24} — **byte-identical across sides** (the liabilities
  TabsContent's own mt-6 — the never-pinned axis).
- The LIABILITIES SECTION ROW: {h 56 byte-identical, display flex,
  justify space-between, w 358 / 432 (the width class)}.
- The docSW 390 guard on the clone side (the superset invariant — the
  reference reads 464, its own documented overflow bug).

Every axis is DATA-INDEPENDENT (the structural chrome — the margins
[mb-8/mt-6/mt-6], the tablist's h/pad, the section rows' flex chrome and
h 56, the docSW guard; no seed data touches any axis — the count text
lengths cannot wrap at the 358 column) — the v98 data-independent-panel
strength class: the pin asserts the cross-side-verified values directly.

**The pin** (tests/e2e/networth.spec.ts, appended as the v102 describe
block): navigate to /networth at 390×844 → the assets-side junction walk
(the gradient summary card finder → the tablist → the Assets h2 → block
→ row — the v94/v100 finders) → assert the cardToTablist gap 32 + the
assets tablistToSection gap 24 + the tablist h 36/pad 4px anchors →
switch to the Liabilities tab (the Playwright locator click — the full
pointer event family natively) → the liabilities section row visible →
assert the liabJunction gap 24 + the liabSectionRow {h 56, flex,
space-between} + the docSW 390 guard.

**The pin-sanity mutation (the planned form)**: the LIABILITIES
TabsContent's `mt-6` → `mt-8` (src/components/budget/net-worth-view.tsx:
479, by LINE NUMBER — the line carries EXACTLY ONE mt-6, grep-count
verified; the line-scoping keeps the ASSETS TabsContent's own mt-6 at
line 415 AND the ratio footer's "mt-6 pt-6" at line 385 untouched).
Expected: the pin FAILS at exactly the LIABILITIES junction axis alone
(liabJunction.gap 24 → 32); cascade-free BY CONSTRUCTION (a vertical
margin never changes any width/height/chrome axis; the v100 pin's assets
junction [line 415] and the v41 F2 pin's cardToTablist [the card's mb-8
at line 325] are untouched by the line-scoped mutation — the v100
mutation's own line-scoping precedent, mirrored); no other spec asserts
the liabilities TabsContent's junction — this pin is the first. NOTE the
v98 mutation-rebuild discipline: the mutation only bites after the
standalone REBUILD (the e2e runs the PREBUILT .next/standalone server).
Then restored (git diff src/ = 0 lines; the standalone REBUILD via the
FULL npm run build; the post-restore full file run green).

**The disproven-in-advance candidates (documented without execution):**
the summary card's mb-8 → mb-6 mutation (cardToTablist 32→24 at BOTH 640
and 390 — fails the v41 F2 pin at 640 TOO: NOT cascade-free within the
same file); the ASSETS TabsContent's mt-6 → mt-8 mutation (line 415 —
tablistToSection 24→32 at BOTH 1280 and 390: fails the v100 pin TOO:
NOT cascade-free); the section row's inter-child rhythm mutations (the
row h 56 is pinned by the v94 F4 pin at 1280 — any row-height mutation
cascades; the v101 cumulative-pin-coupling lesson re-applied).

## The ToDo list

| # | Step | Status |
|---|------|--------|
| 1 | F0 baseline chain on the carried-over workspace (seedcheck exact; lint/typecheck/108 unit/build ✓; 304 e2e zero flakes on the first run; 35/35 smoke) | DONE — all green |
| 2 | F1 axe-core watch | DONE — NO DRIFT |
| 3 | F2 96th standing checks (derived v95→v96, version-bump-only verified) | DONE — ALL GREEN (census clean on the first read) |
| 4 | F3 the v96-lineage probe derivation (generic swaps + exact-fragment history corrections + residual checks + line-count preservation; zero misses) | DONE |
| 5 | F3 two-half census builder (build-twohalf-v102.py, md5 contract) + both halves executed (the reaping budget between halves) | DONE |
| 6 | F3 the VLM pairwise + the flag arbitration (the headgap one-shot census) | DONE — BOTH DIFFERENT, every flag DOM-arbitrated (NO NEW GAP) |
| 7 | F4 the supplemental mobile-junction two-half census (the pin's own axes measured byte-identical, including the liabilities pass) | DONE |
| 8 | F4 THIS PLAN written + validated BEFORE the pin's execution | DONE |
| 9 | F4 append the v102 pin to tests/e2e/networth.spec.ts | PENDING |
| 10 | F4 pin first run (GREEN expected) | PENDING |
| 11 | F4 pin-sanity mutation (net-worth-view.tsx:479, line-number-scoped) → single-axis failure after the REBUILD → restore (git diff src/ = 0) → standalone REBUILD → post-restore full file run | PENDING |
| 12 | F5 full chain re-run (lint/typecheck/108 unit/build/305 e2e/35 smoke) + the screenshots regeneration + byte-compare | PENDING |
| 13 | D1–D7 docs alignment + session_248.md + the worklog Session 137 entry | PENDING |
| 14 | ship: the full chain re-run + commit + SSH-wrapper push | PENDING |

## The pre-execution validation section (the measured evidence)

- The pin's measured values (the mobile-junction two-half census, this
  session): cardToTablist {gap 32} byte-identical; tablistToSection
  (assets) {gap 24} byte-identical; **liabJunction {gap 24}
  byte-identical**; liabSectionRow {h 56, display flex, justify
  space-between} byte-identical (the w family the documented
  ref-overflow class: clone 358 / ref 432); tablist {h 36, pad "4px"}
  byte-identical (the template the v53 width class: clone "175px 175px"
  / ref "211.828px 211.844px"); docSW clone 390 / ref 464 (the
  superset invariant); the seedcheck exact after the clone half.
- The mutation target line verified by reading the source:
  src/components/budget/net-worth-view.tsx:479 — the LIABILITIES
  TabsContent's opening tag carries EXACTLY ONE `mt-6` (grep-count 1 on
  the line); the ASSETS TabsContent's own `mt-6` at line 415 and the
  ratio footer's `mt-6 pt-6` at line 385 — untouched by the
  line-number scoping.
- The coverage-map grep (run across ALL 24 specs): the only
  cardToTablist assertion the v41 F2 pin's own at 640; the only
  tablist→section junction assertion the v100 pin's own at 1280 (the
  ASSETS tab); zero specs assert ANY junction at 390; zero specs assert
  the liabilities panel's junction at ANY viewport; the only mt-6
  assertion near the liabilities content the ratio footer's — a
  different element — this pin is the FIRST on the liabilities-junction
  family.
- The rotation ledger verified: the twins pair last re-shot v96 = the
  oldest remaining [v96 < v97 < v98 < v99 < v100 < v101] — the
  v101-era docs' v102 suggestion agreeing with the ledger (the
  TWENTY-FIFTH consecutive agreement), the surface names verified
  against vlm-shots-v96.sh's own header before the derivation.
- The pin's finders: the gradient summary card finder (the NW_CENSUS
  pattern — proven on both sides this cycle), the `[role="tablist"]`
  locator (labelled on BOTH sides — the v99 finder rule), the Assets/
  Liabilities h2 → block → row walk (the v94 finder — proven at 1280
  and re-proven at 390 this cycle on both sides), and the Liabilities
  trigger by accessible name (the Playwright locator click — the full
  pointer-event family natively, the reference-side pointerdown lesson
  learned this cycle).

## Operational lessons this cycle (the probe README's D6 section)

- THE REFERENCE TAB-SWITCH INTERACTION CLASS (a census-finder note): the
  reference's Radix-style TabsTrigger ignores a bare DOM `.click()` —
  the aria-selected state never flips and the panel never swaps; the
  FULL pointer-event sequence (pointerdown + mousedown + pointerup +
  mouseup + click) is load-bearing on the reference side (the clone
  responds to both). Future censuses that switch tabs on the reference
  must dispatch the full sequence — or use the Playwright locator click
  in the pin itself (which dispatches the full family natively).
- THE FORK-RETRY EXHAUSTION RE-CONFIRMED (a reaping-budget note): the
  clone census half's first run this cycle hit `bash: fork: retry:
  Resource temporarily unavailable` and read EMPTY output even after a
  routine pkill — the THOROUGH reaping (pkill -9 on chromium AND chrome
  AND agent-browser AND the standalone server + a 5s settle) was needed
  before the clean retry; the two-half form remains necessary but not
  sufficient — the reaping must be thorough between halves on this
  sandbox.
- THE SECOND-PANEL COVERAGE RULE (a coverage-map note): a tabbed view's
  junction coverage is complete only when BOTH panels' junctions are
  pinned — the assets panel's junction (the v100 pin at 1280) and the
  liabilities panel's own (THIS pin at 390); the family-extension survey
  on a tabbed surface must walk EVERY panel's junction, not just the
  default tab's (the same both-columns lesson as the v101 2-col row).

## The next queue (the v103 suggestion — verify against the rotation ledger before executing)

(1) the re-run cadence rotates to the next-oldest candidate after the
mobile twins (the v97-era ITEMS pair [the INCOME + EXPENSES view pair at
desktop 1280x800], last re-shot v97 — now the oldest remaining [v97 <
v98 < v99 < v100 < v101 < v102]; the pair's SEVENTH re-run bracket
[v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103] to be verified against
vlm-shots-v97.sh's own header before the derivation), (2) the axe-core
watch at its next re-check point (only a 5.x wrapper changes the
calculus), (3) the deferred reference-write censuses (unchanged — out
of bounds under the v46 read-only rule).
