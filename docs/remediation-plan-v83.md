# Remediation Plan v83 — the re-run cycle's next-oldest candidate (the v61-era dashboard pair's third re-run) + the axe watch + the cross-row vertical-rhythm census pin (PIN-ONLY)

The formal narrative: `docs/session_197.md`. The queue: the session-195
continuation of the v82 plan's v83 suggestion — **the ledger-verified
target** (the v82 plan's suggestion AGREEING with the rotation ledger:
the v61-era dashboard pair [the dashboard FULL-PAGE at desktop 1280 —
the below-the-fold Budget Guidelines card + the quick-action row], last
re-shot v77, is the oldest remaining candidate [v77 < v78 < v79 < v80 <
v81 < v82]; the pair's THIRD re-run [v61 → v68 → v77 → v83] — the SIXTH
consecutive queue/ledger agreement), plus the axe-core watch at its
re-check point and the 77th standing checks. **PIN-ONLY for src/ — no
production-code change; +1 e2e = 286.**

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered; the standalone static + public copies verified) ·
**285 e2e ✓** (101 + 108 + 78 chunk executions = 287 total = 285 unique
tests in 23 files [283 chromium + 1 setup, the setup re-run per chunk as
the project dependency] — the exact documented v82 state) · 35/35 smoke
✓. The workspace REBUILT (the reset path — the third consecutive
reset-boundary): `git clone` landed at `main @ 7b28990` (v82 shipped +
the session_195 transcript), the tree clean; node_modules reinstalled
(354 packages), chromium-1243 reinstalled, `.env` rewritten
(DATABASE_URL="file:../db/custom.db", db/ at the repo root), `prisma
generate` + `npm run db:push` + `npm run db:seed` re-run (the polluting
shell DATABASE_URL — an absolute parent-workspace path — handled via the
documented `env -u` discipline; every DB-touching command ran through
the npm scripts), no orphaned servers, the seedcheck confirming the
exact seed (7 items / rent 1850 / expenses 2235 / 0 line items / 3
assets / 2 liabilities) before any flow ran.

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (no 5.x exists), npm-latest
`axe-core` 4.14.0; the lockfile holding the v68 dedupe state (the
wrapper 4.14.0 + ONE hoisted axe-core 4.14.0); the engine-contract pin
GREEN standalone (2 passed).

### F2 — the 77th standing checks: ALL GREEN (version-bumped from v76 — version-bump-only diffs verified)

The mobile menu VERIFIED WORKING (the 77th consecutive time —
`hitIsBurgerChild:true`, the sheet opens + closes on nav, the nav
landmark present); the reference's four bugs ALL live [toast-blocker
`hitIsBurgerChild:false`, sheet-trap `overlayCount:1`, no-landmark
`navLandmark:false`, the 464px /networth overflow]; the data census
UNCHANGED (the 77th clean drift check: networth "1 items · $25,000" /
income "1 items · $5000.00" / expenses "4 items · $525.00"); the SEO
pair live on both sides; zero overflow at 390 on all five clone views.

### F3 — the re-run pair (the dashboard FULL-PAGE at desktop 1280x800)

**The DASHBOARD pair: VERDICT IDENTICAL** — the only reported deltas
DATA (the seed classes: the hero figures 30.5%/62.8% allocation,
$3475/$2065 balance, the stat amounts and counts, the donut proportions
and drill-down amounts) + the documented non-chrome classes (the
root-URL nav state the v56 SUPERSET class — the reference's Dashboard
link INERT vs the clone's ACTIVE; the avatar the user-identity class
"U" vs "D"; the "Edit with Base44" overlay the platform-chrome class).
The two v61-era TARGET SURFACES — the Budget Guidelines card and the
quick-action row — IDENTICAL on every reported chrome axis (geometry,
radius, padding, borders, tints, icon tiles, typography, plus icons).

**The both-sides census (arbit-v83.sh — the v77 census axes
re-measured): the v77 census values REPRODUCED EXACTLY — zero drift
since v77 on every axis:**

1. PART G (the guidelines card) — the card 468×348/radius 12px/border
   rgb(229,231,227) 1px/white/the visible shadow layers
   `rgba(0,0,0,0.1) 0 1px 3px, rgba(0,0,0,0.1) 0 1px 2px -1px`; the
   header pad 24px/fs 16px/fw 600/rgb(26,58,46)/lh 16px/tracking
   -0.4px; the body pad 0px 24px 24px; all three tiles 418×78/radius
   8px/pad 16px with the Needs/Wants/Savings tint families and the
   label 16px/500/pct 14px/400/desc 12px/lh 16px chrome — the ONLY
   census delta the card shadow's transparent lead-layer count (the
   clone's 6-layer computed form vs the reference's 4 — the v66
   computed-form INVISIBLE class, the visible layers byte-identical).
2. PART Q (the quick-action row) — the grid `304px 304px 304px`/gap
   24px/w 960; the three cards 304×90/radius 16px/pad 24px/white/the
   border/the 40×40 radius-12 tinted tiles/the 20px icons/the 16px
   labels/the 16px 0.5-opacity pluses — the TWO census deltas both
   documented classes: the grid `mt` (ref 0px vs clone 32px — the
   rendered gap IDENTICAL at 340, the v77 mechanism class) and the
   label finder's wrapper catch (ref leaf 500/rgb(26,58,46) vs clone
   wrapper 400/rgb(10,10,10) — the v61 label lesson re-confirmed: the
   clone's LEAF span carries the identical 500/rgb(26,58,46), pinned
   green by the v61 F3 pin's leaf-span finder).
3. PART X (the cross-row gap) — cardBottom 1122/gridTop 1462/gap 340
   on BOTH sides, byte-identical.

**NO NEW GAP — the v83 iteration is PIN-ONLY.**

### F4 [PIN] — the dashboard's cross-row vertical-rhythm census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 286)

The never-pinned axes (the existing pins cover around them — the v61
F2 pin holds the guidelines card's box chrome + the FIRST tile + the
STRETCH contract [cardH 348, cardBottom−lastTileBottom 24–25, rowH
656, rowH−cardH 308]; the v61 F3 pin holds the quick-action grid's
{display/template/gap/w} + the three cards' full chrome + the
tile/icon/label/plus families; the v77 pin holds the guidelines
interior-text family + the icons' viewBox; the v51 F5 pin holds the
grid's mt "32px" at 390 ONLY):

- **The GUIDELINES CARD's BOTTOM at 1280**: cardBottom 1122 — the
  cumulative upstream rhythm (the hero + breakdown + stat rows + the
  guidelines row's own 656 stretch), never pinned as an absolute.
- **The QUICK-ACTION GRID's TOP at 1280**: gridTop 1462.
- **The RENDERED CROSS-ROW GAP**: gap 340 (gridTop − cardBottom) — the
  byte-identical both-sides parity axis (the reference achieves the
  same 340 through its own wrapper structure; the clone through the
  wrapper stretch 308 + the grid's mt-8 32px).
- **The GRID's OWN mt at 1280**: mt "32px" — the v51 F5 390 axis's
  desktop twin (the clone's mechanism axis; the reference's own mt is
  the 0px mechanism class — the RENDERED gap is the parity axis).

Every pinned axis STATIC chrome (none depends on the seed figures);
the pin rides the plain authenticated /dashboard view (no dialogs, no
fixture writes — the simplest read-only state).

**The pin-sanity mutation**: the quick-action grid's `mt-8` → `mt-8
lg:mt-6` (dashboard-view.tsx:993 — the QUICK-ACTION grid only; the
stat row's identical class string at :954 untouched) — flips EXACTLY
the pin's own axes at 1280 (mt 32→24, gridTop 1462→1454, gap 340→332;
cardBottom 1122 unchanged) and nothing else (the mutation is
viewport-scoped: below 1024px the lg: variant is inert — the v51 F5
390 mt pin and the 390 card y-positions 2751/2865/2979 stay GREEN; the
v42 F2 640 scrollHeight 3029 stays GREEN; the v61 F3 grid
{display/template/gap/w} expectation carries no mt axis; the v61 F2
STRETCH contract is upstream of the mutation; the quick-action grid
is the LAST child of the dashboard view — no downstream cascade) —
cascade-free by construction, then restored (the standalone REBUILD as
a SEPARATE command; `git diff src/` = 0 lines).

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → `npm run build` → **286 e2e** in chunks
(+1) → 35 smoke; the 16 standing screenshots regenerated + byte-
compared (the same-DB discipline; the seedcheck under
`env -u DATABASE_URL`). EXPECTED: the same-day seed + same-day shots
reproduce the committed set byte-for-byte (the v82 same-day-seed
byte-identity law — the seed planted 2026-10-18, the committed set
shot 2026-10-18); any DATE-class diff pixel-arbitrated per the
v66/v75/v80 discipline, never a full-page VLM verdict.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the cross-row vertical-rhythm census at 1280 (cardBottom 1122 + gridTop 1462 + gap 340 + gridMt 32px) | tests/e2e/dashboard.spec.ts |
| 2 | sanity | the pin-sanity mutation: the quick-action grid's `mt-8` → `mt-8 lg:mt-6` (dashboard-view.tsx:993) → the pin FAILS at exactly its own axes (mt 32→24, gridTop 1462→1454, gap 340→332; cardBottom 1122 unchanged); restored → GREEN (the standalone REBUILD as a SEPARATE command) | src/components/budget/dashboard-view.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 286 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v83 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (285→286 + the v83 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v83 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 118 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.40 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v83 section (the new probes + the census-reproduction note) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_197.md + the repo worklog Session 118 entry | docs/session_197.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the arbit-v83.sh PART X census's own
  measured values, byte-identical on both sides' dashboards at
  1280x800: the cardBottom `{1122}`; the gridTop `{1462}`; the gap
  `{340}`; the gridMt `{"32px"}` (the clone's own mechanism axis).
- The source confirms the values: the quick-action grid
  `mt-8 grid grid-cols-1 gap-6 md:grid-cols-3`
  (dashboard-view.tsx:993) inside the page's `space-y-6` flow; the
  guidelines row's wrapper stretch (rowH 656 − cardH 348 = 308) + the
  grid's mt-8 (32px) = the rendered 340px gap (1122 + 308 + 32 =
  1462).
- The pin-sanity target: the `lg:mt-6` variant flips ONLY the 1280
  axes — grep-verified: no spec pins the quick-action grid's mt or
  y-positions at 1280 (the v51 F5 mt/y pins are the 390 family; the
  v42 F2 scrollHeight 3029 pin is the 640 family; the v61 F3 grid
  expectation is {display/template/gap/w} — no mt axis); the
  quick-action grid is the LAST child of the dashboard view
  (dashboard-view.tsx:993-1012) — no downstream element's position
  depends on it.
- The existing pins are SAFE: the v61 F2 STRETCH contract (upstream of
  the mutation — the wrapper and card geometry untouched); the v61 F3
  chrome family (no mt/position axes); the v77 interior-text family
  (typography only); the v51 F5 390 family (the lg: variant inert
  below 1024px).
- The blast radius: ZERO production-code change (every census delta a
  documented class — the pin-only line holds); the pin-sanity
  mutation touches `src/components/budget/dashboard-view.tsx:993`
  (the quick-action grid's className) REVERTED before ship (`git diff
  src/` = 0 lines at commit).
- The chain gate: lint → typecheck → 108 unit → `npm run build` →
  285 e2e (**286** after: +1 — the F4 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every
  agent-browser run; the with-server boots fresh per command; the
  reference session EXPIRES between long eval gaps — the login-retry
  loop handles it; the e2e chunks pass FULL file paths;
  `ss -tlnp | grep :3100` + kill before every full-chain run (the
  v53 orphaned-webServer lesson); one-shot Prisma scripts need
  `env -u DATABASE_URL`; no dollar sequences in census JS inside
  double-quoted bash strings (the v64 rule); no attribute-value
  selectors in the census (the v78 rule — geometry + text-content
  filters only); the QUOTED heredoc with the env-injected census
  (the v73 lesson); the mutations need the standalone REBUILD as a
  SEPARATE command (the v53 lesson); the clean-check gate re-runs
  AFTER every new file lands (the v69 lesson); the build step is
  `npm run build` (the v76 F0 lesson); the screenshot DATE-class
  diffs after a fresh seed are pixel-arbitrated, never full-page
  VLM-verdicted (the v80 lesson).
- The deferred queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census, the line-items dialog
  glyphs.
- The v84 queue (suggestions): (1) the re-run cadence rotates to the
  next-oldest candidate after this pair (the v78-era MOBILE pair
  [the networth + dashboard full-page twins at 390], last re-shot
  v78 — now the oldest remaining [v78 < v79 < v80 < v81 < v82 <
  v83]), (2) the axe-core watch at its next re-check point (only a
  5.x wrapper changes the calculus), (3) the deferred reference-write
  censuses (unchanged).
