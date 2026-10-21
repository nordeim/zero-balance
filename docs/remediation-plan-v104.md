# Remediation Plan v104 — the re-run cycle's next-oldest candidate (the v98-era SAVINGS pair's seventh re-run) + the axe watch + the 98th standing checks + the rail brand-block subtitle/row census pin (PIN-ONLY)

The formal narrative: `docs/session_252.md` (the v103 cycle's own narrative
log). The queue: the v103 plan's v104 suggestion — **the ledger-verified
target** (the v103-era docs' suggestion AGREEING with the rotation ledger:
the v98-era SAVINGS pair [the SAVINGS view at desktop 1280x800], last
re-shot v98 — now the oldest remaining [v98 < v99 < v100 < v101 < v102 <
v103]; the pair's SEVENTH re-run bracket [v58 → v65 → v74 → v80 → v86 →
v92 → v98 → v104] — the TWENTY-SEVENTH consecutive queue/ledger
agreement), plus the axe-core watch at its re-check point and the 98th
standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 307.**

## The pre-execution ledger verification (the queue-prose verification lesson, applied)

The rotation ledger's authority is the PROBE LINEAGE, never the prose
queue phrasing. Verified against `scripts/parity-probes/vlm-shots-v98.sh`
before the derivation: its own header reads "the fresh sweep of the
re-run cycle's OLDEST candidate (the v92-era savings pair, last re-shot
v92, now the oldest remaining [v92 < v93 < v94 < v95 < v96 < v97]; the
pair's SIXTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98]" —
matching the queue's phrasing (the v98-era surface names confirmed: the
SAVINGS view at desktop 1280x800, FULL-PAGE; the goal-card grid). The
SEVENTH re-run bracket [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104]
constructed from the same header's SIXTH bracket. The standing-checks
pair (ref-standing-v98.sh + standing-checks-v98.sh) derived from v97
across the THREE token families (v97→v98, 97th→98th,
ref97→ref98/clone97→clone98), version-bump-only verified by normalizing
back and diffing clean (zero old tokens remaining — the persisted
derive-standing-v104.py, both halves bash -n clean).

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items
/ 3 assets / 2 liabilities) before any flow ran (the `env -u DATABASE_URL`
discipline); lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓
(robots + sitemap prerendered) · **306 e2e ✓** (126 + 89 + 57 + 37 chunk
executions across four disjoint file splits of the 23 spec files + the
setup project = 309 total = 306 unique tests — the exact documented v103
state [305 spec + the v103 pin + 1 setup], the count first derived
authoritatively via `playwright test --list` and the per-file counts
summed against the authoritative total before any chunk ran — the v103
chunk-split self-audit lesson applied; zero flakes on the FIRST run) ·
35/35 smoke ✓. The workspace: the FRESH-CLONE class (the sandbox reset —
the v86/v88/v90/v91/v92/v98/v100/v101/v103 precedent): the environment
re-provisioned from scratch (npm install; `.env` written
[DATABASE_URL="file:../db/custom.db"]; `db/` at the repo root +
db:generate + db:push + db:seed; chromium-1243 installed for the pinned
@playwright/test 1.63.0; the tool-results dir re-created for
with-server.sh). The two commits since the v103 parity push (f6b5ccf +
bb7e02e) audited session-log-only [docs/session_252.md +
docs/session_253.md — ZERO src/ or lockfile deltas].

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

### F2 — the 98th standing checks: ALL GREEN (version-bumped from v97 — version-bump-only diffs verified)

ref-standing-v98.sh + standing-checks-v98.sh (version-bumped from v97
via the persisted derive-standing-v104.py across the THREE token
families [v97→v98, 97th→98th, AND the bare session names ref97→ref98/
clone97→clone98]; after normalizing back the files are version-bump-only:
diffed clean, zero old tokens remaining). Reference side: the four bugs
ALL live [toast-blocker `hitIsBurgerChild:false`; sheet-trap
`overlayCount:1` after nav; no-landmark `navLandmark:false`; the 464px
/networth overflow at 390 measured docSW 464 directly]; the data census
UNCHANGED on the FIRST read (networth "1 items · $25,000" / income "1
items · $5000.00" / expenses "4 items · $525.00" — no render-race this
cycle); the SEO pair live. Clone side: R1–R4 ALL GREEN — **the mobile
menu VERIFIED WORKING the 98th consecutive time**
(`hitIsBurgerChild: true`, the sheet opens, closes on nav, the nav
landmark present — the Tailwind v4 mitigation holds), zero overflow at
390 on all five views, the SEO pair live. The seedcheck exact after the
clone half (the reaping budget between the halves).

### F3 — the re-run pair (the v98-lineage derivation, the two-half census form)

The probe series derived from the v98 lineage (derive-v104-series.py,
persisted): vlm-shots-v104.sh + clone-vlmshots-v104.sh +
vlm-compare-v104.mjs + arbit-v104.sh — the generic swaps
(refvlm98→refvlm104, clonevlm98→clonevlm104, refarbit98→refarbit104,
clonearbit98→clonearbit104, /tmp/vlm98→/tmp/vlm104, v98→v104) followed
by the exact-fragment history corrections (last-re-shot v92→v98, the era
marker v92-era→v98-era, SIXTH→SEVENTH, the re-run bracket extension
[v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104], the oldest-remaining
list bumped to the current era [v98 < v99 < v100 < v101 < v102 < v103],
the plan attribution v97→v103, the agreement count TWENTY-FIRST→
TWENTY-SEVENTH, and the v98-era pin-candidate provenance note kept
historical) — every correction verified applied (the derive script
reports each hit/miss; zero misses this cycle; the line-count-preservation
check green on all four files — the two-half builder inherits the v98
line boundaries). bash -n + node --check clean on all four; zero
residual old tokens (the legitimate v58/v57/v74/v80/v64/v73/v51/v54/
v43/v46/v22 lineage/axes-provenance tokens whitelisted by context). The
census BUILT two-half from the start (build-twohalf-v104.py —
ref-arbit-v104.sh + clone-arbit-v104.sh, the ONE census JS block
[SV_CENSUS_JS 153 lines] byte-identical across the halves — the md5
line-block contract [891ab9b6]; the doubled-brace spot check clean). The
reaping budget applied as the standing step between halves. Login on the
first attempt both sides; the parked pointer at (5,5); read-only — the
v46 rule holds; the seedcheck exact after the clone half.

The VLM pairwise verdict: **DIFFERENT** (the pair's documented verdict
class) with every flag DOM-arbitrated to a documented class: the "Card
Footer Layout" flag the v57 DATA-CONDITIONAL class (the footer
childCount 1-vs-2 — the clone's "Brokerage" chip; the census proving
the reference RENDERS payment chips when data carries them per the
v97 income-card evidence); the "Card Grid" flag the seed-count class
(grid childCount 1 vs 2); the header-subtitle + card-contents flags the
seed-data classes (the reference's 1 savings item vs the clone's 2-item
dev seed); the avatar flag the user-identity class. The "Edit with
Base44" FAB NOT flagged this cycle (the VLM's report omitted the
platform chrome entirely — the v103 standing-class lesson: EITHER form
expected without surprise; no arbitration needed for an unflagged
family).

The both-sides census **REPRODUCES the v98 census values EXACTLY — zero
drift on every axis**:

- The HEADER {h1 "ZeroBalance" fs 20px / fw 700 / rgb(26, 58, 46)} —
  byte-identical (the hidden-SEO-h1 family).
- The GRID + CARD chrome {grid w 960 / gap 16px / the 3-col 309.328px
  template family; card w 309 / pad 20px / radius 12px / border 1px
  rgb(229, 231, 227) / bg white} — byte-identical; the childCount (1 vs
  2) the seed-count class; the card h (200 vs 230) the v57/v70b
  Recurring-wrap class (+30px: the badgeRow h 22 vs 52); the clone
  template's last-column sub-pixel (.328/.328/.344 vs .328 ×3) the
  column-distribution rounding noise WITHIN the documented 309.328px
  family (the reference's own expenses template reads .328/.328/.344 —
  byte-identical to the clone's form).
- The TITLE ROW chrome {gap 8px / dot 8×8 / dotBg rgb(59, 126, 161) /
  font 16px / weight 600 / lh 24px} — byte-identical.
- The AMOUNT leaf chrome {fs 24px / fw 700 / lh 32px / color
  rgb(59, 126, 161)} — byte-identical.
- The FOOTER + BADGE chrome {footer flex/space-between/12px/
  rgb(107,114,128)/h 16; badge row flex/wrap/8px gap/mb 12px; badge
  radius 6px/pad 2px 10px/fs 12px/fw 600/h 22} — byte-identical; the
  footer childCount (1 vs 2) the v57 DATA-CONDITIONAL class; the
  badgeRow h (22 vs 52) + texts the wrap/classification-VALUE classes;
  the "monthly" (purple rgb(126, 34, 206)) + "active" (slate
  rgb(51, 65, 85)) badges byte-identical in full chrome.
- The docSW 1280 guard on both sides.

**NO NEW CLONE GAP — the v104 iteration PIN-ONLY.**

### F4 [PIN] — the rail's TOP brand-block subtitle + row census at 1280: the flex row + the h2 color/lh + the "Budget Planner" subtitle chrome (PIN-ONLY for src/ — no production-code change; +1 e2e = 307)

The never-pinned family (the FAMILY-EXTENSION pattern — the rail's TOP
block, never census'd as a whole): the v7 G4 pin holds the brand TILE
(40×40/12px/gradient) + the ICON (24×24 white) + the H2's size/weight
(18px/700) ONLY; the mobile sheet asserts only the TEXTS' visibility
("Budget Planner" — mobile-navigation.spec:127, the sheet variant); the
v36 S3 bands assert the nav links' y positions — **the H2's COLOR +
LINE-HEIGHT, the subtitle P's computed chrome (the 12px/400/
forest-medium "Budget Planner"), and the brand ROW's flex chrome
(display/align/gap) are NEVER pinned in ANY spec at ANY viewport** (the
coverage-map grep across all 23 spec files: zero "Budget Planner"
assertions outside the sheet's one visibility check; zero brand-subtitle
computed-style assertions; the only h2 assertions the v7 G4 size/weight
pair; the rgb(45,90,74) color assertions elsewhere are the networth
chip + mobile-sheet GRADIENTS — different elements).

**The pin's own axes first measured byte-identical on BOTH sides** by
the one-shot both-sides DOM census (brand-arbit-v104.sh — the
base44-fab/userfooter one-shot pattern applied to the family; the census
JS defined ONCE and eval'd on both sides, byte-identical by construction;
both sides READ-ONLY login + passive navigation — the v46 rule holds;
the parked pointer at (5,5); the reference's rail is a DIV not an aside
— the finder carries the v103 rail fallback chain, a live discovery
this cycle):

- The ROW: {display flex, align center, gap 12px} — **byte-identical
  across sides**.
- The H2: {fs 18px, fw 700, lh 28px, color rgb(26, 58, 46)} —
  **byte-identical across sides** (the lh + color the NEW axes; the
  fs/fw the v7 G4 controls re-asserted in the walk).
- The SUBTITLE: {text "Budget Planner", fs 12px, fw 400, color
  rgb(45, 90, 74)} — **byte-identical across sides** (the static copy —
  the reference's own brand block carries the same subtitle).
- The TEXT COLUMN: {display block} + The TILE {w 40, h 40, radius 12px}
  + The ICON {w 24px, h 24px} — the v7 G4 controls re-walked as the
  geometry context.

Every axis is DATA-INDEPENDENT (the structural chrome + the static copy
texts — no seed data touches any axis; the v98 data-independent-panel
strength class: the pin asserts the cross-side-verified values
directly).

**The pin** (tests/e2e/nav-geometry.spec.ts, appended as the v104
describe block): navigate to /savings at 1280×800 → the rail walk (the
aside → the h2 with text "ZeroBalance" → the text column → the tile
[column's previousElementSibling] → the row [column's parent] → the
subtitle P [column's p]) → assert the row {flex, center, gap 12px} +
the h2 {fs 18px, fw 700, lh 28px, color rgb(26,58,46)} + the subtitle
{text "Budget Planner", fs 12px, fw 400, color rgb(45,90,74)} + the
context controls (tile 40×40/12px, icon 24×24, column block).

**The pin-sanity mutation (the planned form)**: the subtitle's
`text-xs` → `text-sm` (src/components/budget/sidebar.tsx:48, by LINE
NUMBER — the line carries EXACTLY ONE text-xs, grep-count verified; the
line-scoping keeps the section label's own text-xs at line 61 AND the
user-footer subtitle's own text-xs at line 129 untouched — the v103
pin's sub axis and the mobile sheet's visibility ride those lines).
Expected: the pin FAILS at exactly the subtitle fs axis alone
(subtitle.fs "12px" → "14px"; the pin deliberately does NOT assert the
subtitle's line-height — text-sm moves fs AND lh, a two-axis failure
diff — the single-axis discipline). Cascade-free: no other spec asserts
the brand subtitle's computed chrome — this pin is the first; the
sheet's visibility check survives a 12→14px change trivially (the
element remains visible); the v7 G4 brand test asserts the h2's
size/weight + the tile + the icon — all untouched by the p's font-size.
The one INDIRECT coupling — the v36 S3 nav-pitch band (navY[0] within
140–150, measured 145 this cycle): the mutation grows the text column
lh 16→20 (+4px IF the column drives the row height) → navY[0] ≤ 149 <
150 — the band survives BY MEASUREMENT (the headroom computed from the
live 145 reading; documented as the disproven-in-advance candidate).
NOTE the v98 mutation-rebuild discipline: the mutation only bites after
the standalone REBUILD (the e2e runs the PREBUILT .next/standalone
server). Then restored (git diff src/ = 0 lines; the standalone REBUILD
via the FULL npm run build; the post-restore full file run green).

**The disproven-in-advance candidates (documented without execution):**
the subtitle's inline color mutation (`var(--forest-medium)` →
`var(--forest-dark)` — single-axis [color] but weaker than the
structural fs form: the fs mutation exercises the typography axis AND
the layout headroom analysis); the h2's `text-lg` → `text-xl` mutation
(fs 18→22 — bites the v7 G4 pin's OWN logo-size axis [18px] — a
cascade, NOT cascade-free); the row's `gap-3` → `gap-4` mutation (row
gap 12→16 — shifts the tile/icon junction AND the column x — two-axis);
the subtitle's text content mutation (breaks the mobile sheet's
visibility text — a cross-file cascade).

## The ToDo list

| # | Step | Status |
|---|------|--------|
| 1 | F0 baseline chain on the fresh-clone workspace (seedcheck exact; lint/typecheck/108 unit/build ✓; 306 e2e zero flakes on the first run; 35/35 smoke) | DONE — all green |
| 2 | F1 axe-core watch | DONE — NO DRIFT |
| 3 | F2 98th standing checks (derived v97→v98, version-bump-only verified) | DONE — ALL GREEN (census clean on the first read) |
| 4 | F3 the v98-lineage probe derivation (generic swaps + exact-fragment history corrections + residual checks + line-count preservation; zero misses) | DONE |
| 5 | F3 two-half census builder (build-twohalf-v104.py, md5 contract) + both halves executed (the reaping budget between halves) | DONE |
| 6 | F3 the VLM pairwise + the flag arbitration | DONE — DIFFERENT, every flag DOM-arbitrated (NO NEW GAP) |
| 7 | F4 the supplemental brand-block one-shot census (the pin's own axes measured byte-identical) | DONE |
| 8 | F4 THIS PLAN written + validated BEFORE the pin's execution | DONE |
| 9 | F4 append the v104 pin to tests/e2e/nav-geometry.spec.ts | DONE — appended (typecheck clean) |
| 10 | F4 pin first run (GREEN expected) | DONE — GREEN on the first run (10/10 in nav-geometry.spec.ts) |
| 11 | F4 pin-sanity mutation (sidebar.tsx:48, line-number-scoped) → single-axis failure after the REBUILD → restore (git diff src/ = 0) → standalone REBUILD → post-restore full file run | DONE — ONLY the v104 pin red (9 green), the failure diff reads as subtitle.fs "12px"→"14px" ALONE; restored (git diff src/ = 0); rebuilt; post-restore 10/10 green |
| 12 | F5 full chain re-run (lint/typecheck/108 unit/build/307 e2e/35 smoke) + the screenshots regeneration + byte-compare | DONE — all green; 307 e2e in four chunks (126+90+57+37 = 310 executions = 307 unique, zero flakes); the screenshots 16/16 BYTE-IDENTICAL (the same-day regeneration — the v97 precedent, NO DATE-class deltas this cycle) |
| 13 | D1–D7 docs alignment + session_254.md + the worklog Session 139 entry | DONE |
| 14 | ship: the full chain re-run + commit + SSH-wrapper push | PENDING |

## The pre-execution validation section (the measured evidence)

- The pin's measured values (the brand-block one-shot census, this
  session): the row {display flex, align center, gap 12px}
  byte-identical; the h2 {fs 18px, fw 700, lh 28px, color
  rgb(26,58,46)} byte-identical; the subtitle {text "Budget Planner",
  fs 12px, fw 400, color rgb(45,90,74)} byte-identical; the column
  {display block} byte-identical; the tile {w 40, h 40, radius 12px}
  byte-identical; the icon {w 24px, h 24px} byte-identical — on BOTH
  sides at 1280.
- The mutation target line verified by reading the source:
  src/components/budget/sidebar.tsx:48 — the subtitle P's opening tag
  carries EXACTLY ONE `text-xs` (grep-count 1 on the line); the section
  label's own `text-xs` at line 61 and the user-footer subtitle's own
  at line 129 — untouched by the line-number scoping.
- The coverage-map grep (run across ALL 23 spec files): zero
  "Budget Planner" assertions outside mobile-navigation.spec:127 (the
  sheet's VISIBILITY check); zero brand-subtitle computed-style
  assertions; zero brand-row flex assertions; the only h2 assertions
  the v7 G4 size/weight pair — this pin is the FIRST on the subtitle/
  row/h2-color axes.
- The rotation ledger verified: the SAVINGS pair last re-shot v98 = the
  oldest remaining [v98 < v99 < v100 < v101 < v102 < v103] — the
  v103-era docs' v104 suggestion agreeing with the ledger (the
  TWENTY-SEVENTH consecutive agreement), the surface names verified
  against vlm-shots-v98.sh's own header before the derivation.
- The nav-pitch headroom measured live: navY[0] = 145 on the clone at
  1280 (the v36 S3 band 140–150); the mutation's worst-case +4px shift
  (the text column lh 16→20) lands at 149 < 150 — the band survives.

## Operational lessons this cycle (the probe README's D6 section)

- THE REFERENCE RAIL IS A DIV (a finder note): the brand one-shot's
  first run returned `{err: "no h2"}` on the reference — the
  `aside h2` finder assumed the reference's rail was an `<aside>` like
  the clone's; the reference's rail is a DIV. The v103 userfooter
  finder already carried the geometric fallback chain (aside OR the
  180–320px-wide 700px-tall left-anchored div) — the lesson: every
  cross-side rail finder must use the fallback chain form, never a
  bare `aside` selector.
- THE UNFLAGGED-FAB CYCLE (a VLM-arbitration note): the v104 pairwise
  report omitted the "Edit with Base44" FAB entirely — after ~15
  cycles of one-or-the-other attribution forms, the THIRD form (no
  flag at all) is now documented; future cycles expect any of the
  three forms without surprise, and an unflagged platform-chrome
  family needs no arbitration.
- THE SUBTITLE-LH EXCLUSION (a pin-design note): the pin deliberately
  omits the subtitle's line-height axis because the chosen mutation
  (`text-xs` → `text-sm`) moves fs AND lh together — asserting both
  would make the mutation's failure diff two-axis; the single-axis
  discipline prefers the fs axis alone (the lh implicitly covered by
  the row-height arithmetic in the headroom analysis).

## The next queue (the v105 suggestion — verify against the rotation ledger before executing)

(1) the re-run cadence rotates to the next-oldest candidate after the
savings pair (the v99-era LOGIN + CALCULATOR pair, last re-shot v99 —
now the oldest remaining [v99 < v100 < v101 < v102 < v103 < v104]; the
pair's re-run bracket to be verified against vlm-shots-v99.sh's own
header before the derivation), (2) the axe-core watch at its next
re-check point (only a 5.x wrapper changes the calculus), (3) the
deferred reference-write censuses (unchanged — out of bounds under the
v46 read-only rule).
