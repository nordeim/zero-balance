# Remediation Plan v84 — the re-run cycle's next-oldest candidate (the mobile 390 twins' third re-run) + the axe watch + the ratio-footer divider census pin (PIN-ONLY)

The formal narrative: `docs/session_200.md`. The queue: the session-199
continuation of the v83 plan's v84 suggestion — **the ledger-verified
target** (the v83 plan's suggestion AGREEING with the rotation ledger:
the mobile 390 twins [the networth + dashboard FULL-PAGE pair at
390x844], last re-shot v78, is the oldest remaining candidate [v78 <
v79 < v80 < v81 < v82 < v83]; the pair's THIRD re-run [v62/v63 → v69 →
v78 → v84] — the SEVENTH consecutive queue/ledger agreement), plus the
axe-core watch at its re-check point and the 78th standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 287.**

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered) · **286 e2e ✓** (102 + 108 + 78 chunk executions =
288 total = 286 unique tests in 23 files — the exact documented v83
state) · 35/35 smoke ✓. The workspace PRESERVED (no reset): `git pull`
landed at `main @ 2b2ba34` (v83 shipped + the session_199 transcript),
the tree clean; node_modules in place (354 packages), chromium-1243 in
place, `.env` verified (DATABASE_URL="file:../db/custom.db", db/ at the
repo root), the seedcheck exact (7 items / rent 1850 / expenses 2235 /
0 line items / 3 assets / 2 liabilities) before any flow ran, no
orphaned servers.

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next
prereleases beyond — no 5.x exists), npm-latest `axe-core` 4.14.0; the
lockfile holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted
axe-core 4.14.0); the engine-contract pin GREEN standalone (2 passed).

### F2 — the 78th standing checks: ALL GREEN (version-bumped from v77 — version-bump-only diffs verified)

The mobile menu VERIFIED WORKING (the 78th consecutive time —
`hitIsBurgerChild:true`, the sheet opens + closes on nav, the nav
landmark present); the reference's four bugs ALL live [toast-blocker
`hitIsBurgerChild:false`, sheet-trap `overlayCount:1`, no-landmark
`navLandmark:false`, the 464px /networth overflow]; the data census
UNCHANGED (the 78th clean drift check: networth "1 items · $25,000" /
income "1 items · $5000.00" / expenses "4 items · $525.00"); the SEO
pair live on both sides; zero overflow at 390 on all five clone views.

### F3 — the re-run pair (the mobile 390 twins: networth + dashboard FULL-PAGE at 390x844)

**Both verdicts DIFFERENT, every flag DOM-arbitrated to a documented
class — NO NEW GAP:**

1. **PAIR 1 (NETWORTH at 390)**: the stat tiles side-by-side (ref) vs
   stacked (clone) — the v41 mobile-superset class; the totals/ratio/
   asset figures + groups — the seed-data class; the "Edit with Base44"
   overlay — the platform-chrome class; **the "divider missing in the
   clone" flag — a VLM MISREAD, disproven by the dedicated one-shot
   both-sides arbitration (ratio-divider-arbit-v84.sh): the divider
   renders on BOTH sides with byte-identical computed chrome** (see the
   census below).

2. **PAIR 2 (DASHBOARD at 390)**: the subtitle wrap point — the v62
   width-delta class (the reference's own 395px docSW overflow shifts
   its wrap by one word; the chrome byte-identical); the black tooltip
   over the breakdown rows — the Base44 platform-chrome class; the
   progress-bar length — the pct data class; the donut proportions —
   the seed-data class. **Matching the v78 re-run's own flag-set
   classes exactly.**

**The both-sides census (arbit-v84.sh — the v78 census axes
re-measured): the v78 census values REPRODUCED EXACTLY — zero drift
since v78 on every axis:**

- **NETWORTH**: the medallion 64×64 + the trend icon 32×32 + the tiles
  h 84 + the grid gap 16px — BYTE-IDENTICAL on both sides; the deltas
  all the v41 mobile-superset class (the reference's card 432/docSW
  464/fixed 2-col tiles 176×84/medallion clipping at right 416 vs the
  clone's card 358/docSW 390/1-col tiles 294×84/medallion right 342
  fully visible).
- **DASHBOARD**: the subtitle chrome BYTE-IDENTICAL (fs 16px/fw 400/
  rgb(107,114,128)/lh 24px, the P h 48, the block h 92, 2 lines) — the
  wrap-point delta (ref "...expenses to / achieve net zero" vs clone
  "...expenses / to achieve net zero") the v62 width-delta class; the
  breakdown card svg family + chart-absence BYTE-IDENTICAL (svgCount 7,
  the [16,14,16,14,...] size family, rechartsWrappers 0/pieSectors 0)
  — the width deltas (363/313 ref vs 358/308 clone) the v62 page-width
  class, the heights byte-identical (card h 324, H3 h 20, DIV h 238).
- **The ratio-divider one-shot arbitration (ratio-divider-arbit-v84.sh,
  BOTH sides at 390)**: the footer's border-t family BYTE-IDENTICAL —
  borderTop 1px solid rgba(255,255,255,0.2), marginTop 24px,
  paddingTop 24px, the footer h 53, the label fs 14px/fw 400, the label
  box 156×20 — the only deltas the footer w (368 ref vs 294 clone — the
  v41 width class) and the footer top (417 vs 505 — the stacked-tile
  card arithmetic, the v41 class).

**NO NEW GAP — the v84 iteration is PIN-ONLY.**

### F4 [PIN] — the networth summary card's ratio-footer census at 390 (PIN-ONLY for src/ — no production-code change; +1 e2e = 287)

The never-pinned axes (the existing pins cover around them — the v41 F3
pin holds the card box/figure/gridCols/chip at 390; the v63 F3 pin the
stat-tile family + the card h 421 + the medallion at 390; the v67 F3
pin the footer's {mt, pt, borderTopW, h} at 1280 ONLY; the v4-era
structure test the border style/color + the VALUE's 18px/700 at 1280;
the v82 pin the label's fs at 1280):

- **The FOOTER's border-t family at 390**: borderTopWidth "1px" /
  style "solid" / color "rgba(255, 255, 255, 0.2)" — the inline style,
  unconditional across viewports.
- **The FOOTER's rhythm + height at 390**: mt "24px" / pt "24px" /
  h 53 (the pt 24 + the border 1 + the value-governed 28px ratio row —
  text-lg's line box governs over any label line box).
- **The ratio LABEL's typography + box at 390**: fs "14px" / fw "400"
  (text-sm) + the 156×20 line box (the static "Asset to Liability
  Ratio" text).

Every pinned axis STATIC chrome (the label text is static; the value is
a single-line 28px line box regardless of the ratio string — "0.21:1"
and "∞:1" both single-line; the mt/pt/border unconditional); the pin
rides the plain authenticated /networth view at 390x844 (no dialogs, no
fixture writes — the simplest read-only state).

**The pin-sanity mutation**: the ratio label's `text-sm` → `text-xs
lg:text-sm` (net-worth-view.tsx:389 — the ONLY `className="text-sm"` in
the file, verified; applied by LINE NUMBER per the v83 lesson) — flips
EXACTLY the pin's label sub-family at 390 (fs 14→12, the label h 20→16,
the label w 156→~134) and nothing else: the mutation is
desktop-restored (at 1280 the lg: variant restores text-sm's 14px — the
v82 ratioLabel.fs pin, the v67 F3 footer arithmetic [the label's line
box never governs the footer h — the value's 28px does], and the
v4-era structure test all stay GREEN); at 390 the footer family stays
GREEN under the mutation (the row height stays value-governed — mt/pt/
border/h 53 untouched) while no other 390 pin asserts the ratio label
(the v41 F3/v63 F3 families stop at the stat grid/tiles/medallion/card
box; the v53 tablist + v69 page-header-row + v14 G3 chip pins are
disjoint surfaces) — cascade-free by construction, then restored (the
standalone REBUILD as a SEPARATE command; `git diff src/` = 0 lines).

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → `npm run build` → **287 e2e** in chunks
(+1) → 35 smoke; the 16 standing screenshots regenerated + byte-
compared (the same-DB discipline; the seedcheck under
`env -u DATABASE_URL`). EXPECTED: the same-day seed + same-day shots
reproduce the committed set byte-for-byte (the v82 same-day-seed
byte-identity law — the committed set was seeded AND shot the same
calendar day as this re-run); any DATE-class diff pixel-arbitrated per
the v66/v75/v80 discipline, never a full-page VLM verdict.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the ratio-footer census at 390 (the border-t family + mt/pt/h + the label typography/box) | tests/e2e/networth.spec.ts |
| 2 | sanity | the pin-sanity mutation: the ratio label's `text-sm` → `text-xs lg:text-sm` (net-worth-view.tsx:389, by LINE NUMBER) → the pin FAILS at exactly its label axes (fs 14→12, h 20→16, w 156→~134; the footer family stays green); restored → GREEN (the standalone REBUILD as a SEPARATE command) | src/components/budget/net-worth-view.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 287 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v84 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (286→287 + the v84 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v84 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 119 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.41 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v84 section (the new probes + the divider-misread lesson) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_200.md + the repo worklog Session 119 entry | docs/session_200.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the ratio-divider-arbit-v84.sh census's
  own measured values, byte-identical on both sides' /networth views at
  390x844: the footer `{borderTopWidth: "1px", borderTopStyle: "solid",
  borderTopColor: "rgba(255, 255, 255, 0.2)", marginTop: "24px",
  paddingTop: "24px", h: 53}`; the label `{fs: "14px", fw: "400",
  w: 156, h: 20}`.
- The source confirms the values: net-worth-view.tsx:385-389 — the
  footer div `className="mt-6 pt-6"` + the inline `borderTop: "1px
  solid rgba(255, 255, 255, 0.2)"` (unconditional across viewports),
  the label span `className="text-sm"` (the ONLY `className="text-sm"`
  in the file — grep-verified, the line-number mutation still applied
  per the v83 identical-string lesson); the ratio row's height stays
  value-governed (text-lg's 28px line box > any label line box to
  24px — the v82 mutation's own cascade argument, reused in the
  inverse direction).
- The pin-sanity target: the `lg:`-restored mutation flips ONLY the 390
  label axes — grep-verified: no spec pins the ratio label's fs/fw/box
  at 390 (the v41 F3/v63 F3/v53/v69/v14-G3 families are disjoint; the
  ratio-label pins at lines 31/271/673/1590/1789/2043 of
  networth.spec.ts all run at the 1280 default or assert visibility
  only); the footer family at 390 stays value-governed under the
  label mutation (mt/pt/border/h untouched).
- The existing pins are SAFE: the v67 F3 footer pin (1280 — the lg:
  variant restores text-sm); the v82 ratioLabel.fs pin (1280); the
  v4-era structure test (1280 — the border family + the VALUE's
  typography unconditional); the v41 F3 + v63 F3 390 families (card
  box/tiles/grid/medallion — the label's line box never enters the
  card-height stack: the v63 F3 pin's own arithmetic holds the 390 card
  h 421 = 333 + the second 84px tile row + the 16px gap, every term
  upstream of the footer's value-governed 28px ratio row — the label
  mutation cannot move the card h).
- The blast radius: ZERO production-code change (every census delta a
  documented class — the pin-only line holds); the pin-sanity
  mutation touches `src/components/budget/net-worth-view.tsx:389`
  (the ratio label's className) REVERTED before ship (`git diff src/`
  = 0 lines at commit).
- The chain gate: lint → typecheck → 108 unit → `npm run build` →
  286 e2e (**287** after: +1 — the F4 pin) → 35 smoke.
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
  VLM-verdicted (the v80 lesson); the sed derivation of the v84 probe
  series needs BOTH the version substitutions AND the
  session-name/tmp-dir substitutions (the vlm78→vlm84 miss caught in
  this session: "v78" as a substring does not match "vlm78" — always
  grep the derived script for the old version string before running).
- The deferred queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census, the line-items dialog
  glyphs.
- The v85 queue (suggestions): (1) the re-run cadence rotates to the
  next-oldest candidate after this pair (the v79-era ITEMS pair
  [the income + expenses view pair at desktop 1280], last re-shot
  v79 — now the oldest remaining [v79 < v80 < v81 < v82 < v83 <
  v84]), (2) the axe-core watch at its next re-check point (only a
  5.x wrapper changes the calculus), (3) the deferred reference-write
  censuses (unchanged).
