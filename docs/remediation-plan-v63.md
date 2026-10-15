# Remediation Plan v63 — the /networth mobile 390 full-page pair (the
# standing-pair matrix COMPLETED) + the networth summary card's stat-tile
# family census pin + the axe-core version-drift re-check (NO DRIFT)

Date: 2026-10-15 · Scope: the session-149/151 v63 queue — "the
standing-pair program's remaining minor surface: a /networth 390
full-page pair (the last un-paired viewport × view combination)" and "a
re-check of the reference's axe-core VERSION drift (the 4.13 family set
held this round; a major bump could shift rule coverage)" — plus the
57th standing checks. All READ-ONLY on the reference (the v46 rule).
Measured live on BOTH sites via the v63 family: `vlm-shots-v63.sh` +
`clone-vlmshots-v63.sh` + `vlm-compare-v63.mjs` (the pair),
`arbit-v63.sh` (the three-flag DOM arbitration census),
`ref-standing-v57.sh` + `standing-checks-v57.sh` (the 57th round,
version-bumped from v56), and the npm-lockfile version audit (F1).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · 264 e2e ✓ (97 + 91 + 78 chunk
runs = 263 chromium + 1 setup, zero failures) · 35/35 smoke ✓ — the
codebase matches the documented v62 state exactly. The v62 pin verified
present (dashboard.spec.ts: the "mobile header-subtitle block census at
390" describe). The dev DB at the exact seed state (7 budget items /
3 assets / 2 liabilities — seeded this sandbox, dates anchor to the
seed-run day).

## The v63 sweep — what the measurement found

### The 57th standing checks — ALL GREEN

- **Reference side**: the four bugs ALL still live — the toast-blocker
  (`hitIsBurgerChild:false`, the burger's center hit intercepted by
  `DIV.fixed top-0 z-[100]`), the sheet-trap (the overlay remains after
  the nav click, `overlayCount:1`), the no-landmark
  (`navLandmark:false`), the 464px `/networth` overflow at 390. The
  data census UNCHANGED (the 57th consecutive clean drift check: "1
  items · $25,000" networth / "1 items · $5000.00" income / "4 items ·
  $525.00" expenses). The SEO pair live.
- **Clone side**: R1 the burger hit-test TRUE + the sheet opens · R2 the
  sheet CLOSES + navigates (`sheetGone:true, overlayGone:true` on
  /income) · R3 the nav landmark present · R4 ZERO overflow at 390 on
  all five views (docSW 390 each) · the SEO pair live. **The mobile
  navigation menu VERIFIED WORKING — the 57th consecutive time.**

### F1 [AUDIT] — the axe-core version-drift re-check: NO DRIFT

The queue's question: has the axe toolchain drifted since the v38/v62
contracts were pinned, in a way that could shift rule coverage?

- **The page-scan toolchain is BYTE-IDENTICAL**: the pinned
  `@axe-core/playwright@^4.13.0` resolves to 4.13.0 — which is STILL
  the npm-latest release of the wrapper — and the engine that actually
  executes the `AxeBuilder` scans is the wrapper's NESTED
  `axe-core@4.13.0` (`node_modules/@axe-core/playwright/node_modules/
  axe-core`, hoisted per the `~4.13.0` range). The v38 and v62 audits
  ran this exact pairing; the "axe-core 4.13" in the spec's contract
  header names it. No version drift → the family set (`button-name` +
  `svg-img-alt` + the 7-color palette) trivially holds; no re-scan
  required.
- **The top-level `axe-core@4.14.0`** in the tree belongs to
  `eslint-plugin-jsx-a11y` (its `^4.10.0` range) — a LINT-TIME static
  analysis consumer that never scans pages. It has no bearing on the
  e2e a11y gates. (Documented to preempt the next session's "why is
  4.14 in the lockfile" question.)
- **Verdict**: the a11y.spec.ts contract remains valid as pinned; no
  code change. The next re-check point: a 5.x wrapper release or an
  engine bump inside the wrapper's nested dep.

### F2 [PAIR] — the /networth 390 full-page VLM pair: the matrix COMPLETED

The standing-pair program's last un-paired viewport × view combination
— the /networth view at mobile 390x844, full-page
(`vlm-shots-v63.sh` + `clone-vlmshots-v63.sh` +
`vlm-compare-v63.mjs`). With it, the matrix is complete: {dashboard,
items (income/expenses), savings, calculator, networth} × {1280 desktop,
390 mobile} all paired (v56–v62 for the rest; this pair closes it).

**VERDICT: DIFFERENT with three flags, ALL arbitrated to documented
classes** (`arbit-v63.sh`, the DOM census on both sides):

1. **"Stat tiles side-by-side (ref) vs stacked (clone)"** — the
   DOCUMENTED v41 mobile-superset class, re-measured live: the
   reference's summary card renders 432px wide at 390 (its own
   documented 464px docSW overflow, R-bug-4), giving its stat grid room
   for its fixed 2-col layout (cols "175.828px 175.844px", tiles
   176×84); the clone's card fits (358 = 390 − 2×16, docSW 390) and
   stacks 1-col (cols "294px", tiles 294×84) — the v4 data-fit
   superset (v29's live 2-col DOM experiment: the seeded
   $65,300/$311,250 figures need 152/169px vs the ~107px half-width
   cells), pinned by the v41 F3 census.
2. **"The clone's summary card is taller"** — the direct arithmetic of
   flag 1: the reference's card h 333 (one 84px tile row) vs the
   clone's h 421 (two tile rows + the 16px gap: 333 + 88 = 421). The
   same documented class; every chrome axis byte-identical (pad 32px,
   radius 16px, the 135deg forest→lime gradient, the
   rgba(26,58,46,0.3) 0px 20px 60px shadow).
3. **"The trend-icon circle appears larger/more prominent in the
   clone"** — a PERCEPTION ARTIFACT of the documented v54 clipping
   class: the medallion is BYTE-IDENTICAL 64×64 on both sides and the
   trending-up icon BYTE-IDENTICAL 32×32 — but the reference's
   medallion sits at right 416 in its 464-overflowing page, 26px PAST
   the 390 viewport edge (`clipsViewport:true` — partially rendered,
   visually smaller), while the clone's sits fully in-bounds at right
   342. The VLM read the reference's clipped medallion as "smaller".

The data differences are the expected classes (the reference's 1 asset
"1 items · $25,000" vs the clone's 3+2 seed; the "∞:1" vs "0.21:1"
ratio — the pinned formatRatio contract; the Base44 tooltip — platform
chrome). **The pair is CLEAN: every flag arbitrates to a documented
class. No production-code parity gap** (`git diff src/` empty at ship).

### F3 [PIN] — the networth summary card's stat-tile family census at 390

The F2 arbitration measured a never-pinned family: the summary card's
stat tiles at 390 (the v41 F3 pin covers the card w/pad/radius/bg/
shadow, the 24px figure, the gridCols "294px", and the chip's 64px w +
bounds — but NOT the tile geometry, the tile chrome, the grid gap, the
card HEIGHT arithmetic, or the medallion's inner icon). The census,
identical on both sides where the reference fits (and superset-class
where it overflows):

- **The stat grid**: `grid grid-cols-1 gap-4 sm:grid-cols-2` → at 390:
  cols "294px", gap "16px", w 294, 2 children.
- **The tiles**: 294×84 each (the 1-col full width; the h 84 = p-4 16
  + label 16 + mb-1 4 + text-2xl amount 32 + p-4 16 — deterministic
  under the fixed seed), chrome: bg rgba(255,255,255,0.1),
  backdrop-filter blur(10px), radius 12px, pad 16px.
- **The card height**: 421 — the 1-col stacking arithmetic (the
  reference's own 333 + the second 84px tile row + the 16px gap), the
  flag-1/flag-2 contract locked.
- **The medallion's inner icon**: 32×32 (h-8 w-8) inside the 64×64
  circle — the flag-3 byte-parity axis.

The F3 pin adds the family to `tests/e2e/networth.spec.ts` (PIN-ONLY —
the surface is already correct; GREEN first run expected), extending
the v41 F3 describe's census shape.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F3 pin: the stat-tile family census at 390 (GREEN first) | tests/e2e/networth.spec.ts |
| 2 | sanity | S1 mutation A: the stat grid `gap-4`→`gap-2` must FAIL the pin (gap 16→8 + card h 421→413); standalone rebuild; restore | src/components/budget/net-worth-view.tsx |
| 3 | sanity | S2 mutation B: the tile `p-4`→`p-2` must FAIL the pin (tile h 84→68 + pad 16→8 + card h); standalone rebuild; restore | src/components/budget/net-worth-view.tsx |
| 4 | sanity | S3 mutation C: the medallion svg `h-8 w-8`→`h-6 w-6` must FAIL the pin (icon 32→24); standalone rebuild; restore | src/components/budget/net-worth-view.tsx |
| 5 | verify | the 16 screenshots regenerated + byte-compared (expect the SEED-DATE class only — no production change) | docs/screenshots/ |
| 6 | docs | D1: AGENTS.md v63 paragraph | AGENTS.md |
| 7 | docs | D2: CLAUDE.md count/state bump | CLAUDE.md |
| 8 | docs | D3: README state + the v63 row | README.md |
| 9 | docs | D4: SKILL doc Session 98 row + the state line | zero-balance_SKILL.md |
| 10 | docs | D5: PAD revision block v1.1.20 | Project_Architecture_Document.md |
| 11 | docs | D6: the probe README's v63 section | scripts/parity-probes/README.md |
| 12 | docs | D7: session_153.md + the repo worklog Session 97 entry | docs/session_153.md + worklog.md |
| 13 | ship | the full chain re-run (lint → typecheck → 108 unit → build → 265 e2e → 35 smoke) + commit + SSH-wrapper push | — |

## Pre-execution validation (done before the plan's execution)

- The F3 pin's finder: reuse the v41 F3 census shape (the
  "Total Net Worth" leaf label → `closest("div.rounded-2xl")`), then
  the "Total Assets" leaf label → its `closest('[class*="grid"]')`
  parent (the stat grid, NOT the card grid — the v46 F2 lesson), then
  the grid's children (the two tiles) and each tile's computed chrome;
  the medallion svg via the chip finder's `querySelector("svg")`. The
  card-height axis reads the card's bounding rect h. All axes
  scroll-independent (the card sits at the page top).
- The mutation targets: `gap-4` at net-worth-view.tsx:365 (the stat
  grid's own class — the tile row-gap axis + the card-height axis in
  one mutation), `p-4` at :367/:374 (both tiles — one class string,
  two sites; the mutation edits BOTH), `h-8 w-8` at :356 (the
  medallion's TrendingUpIcon). Each mutation needs the STANDALONE
  REBUILD as a SEPARATE command (the v53 lesson) before the pin run
  can bite.
- The chain gate: lint → typecheck → 108 unit → build → 264 e2e
  (**265** after: +1 — the F3 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every agent-browser
  run; the with-server boots fresh per command; the reference session
  EXPIRES between long eval gaps — re-login; the e2e chunks pass FULL
  file paths; `ss -tlnp | grep :3100` + kill before every full-chain
  run (the v53 orphaned-webServer lesson).
- The deferred queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census, the line-items dialog
  glyphs. The reference's trending-down glyph stays data-conditional
  (its net is positive — the 57th data census confirms).
- The v64 queue (suggestions): the pair matrix being complete, the
  next natural surfaces are (1) the re-run cadence on the OLDEST
  desktop pairs (v57's items pair and v58's savings pair predate the
  v61 dashboard fix and the v62/v63 mobile twins — a fresh standing
  sweep of one of them), (2) the axe-core 5.x wrapper watch (F1's
  documented next re-check point), (3) the deferred reference-write
  censuses (unchanged).
