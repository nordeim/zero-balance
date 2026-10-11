# Remediation Plan v41 — The Net-Worth Summary Card's Viewport Census + the Vertical-Rhythm Fix (the Savings-Class Viewports Queue)

Date: 2026-10-11 · Scope: fresh two-site re-audit after the v40 baseline
(`fc781d0` + the session-log commits `5b0a6f3`/`009453c` on `main`; the
workspace survived the session break — `git pull` fast-forwarded to
`009453c`, the environment intact: node_modules, `.env`
(`DATABASE_URL="file:../db/custom.db"`), `db/custom.db` + `db/e2e.db` at
the repo root, playwright chromium). Baseline chain on the re-run: lint ✓
· typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**196/196 e2e ✓ (4.5m, the first run, zero flakes)**; npm audit = the same
5 dev-only ESLint `braces` advisories — accepted, unchanged, dev-only; the
secret-pattern scan clean (src/tests/scripts); `.env` verified
byte-identical to `.env.example`.

The sweep — method and results: the session-86/87 queue's headline surface
(the net-worth summary card's gradient chip at the savings-class viewports
— the unmeasured MID viewport class), plus the standing re-verification
set (mobile-nav R1–R4 on BOTH sites, data drift, the SEO pair) and the
code audit. One process note: this sandbox reaps background processes
between tool calls — every long job (the e2e suite, the parity server)
runs inside a single invocation via `scripts/with-server.sh`.

- **Mobile navigation (the standing task focus) R1–R4 all re-verified
  live on BOTH sites — the 35th consecutive check.** R1: the reference's
  toast containers still intercept the burger's center hit
  (`DIV.fixed.top-0.z-[100]`, scrollWidth 395); the clone's hit DIRECT on
  the svg, fits 390. R2: the reference's sheet still traps after nav
  (sheet open, body locked on /income); the clone's closes. R3: the
  reference marks nothing active on `/` and has no `<nav>`; the clone has
  the landmark. R4: the reference overflows 395 on `/`+`/dashboard`;
  the clone fits 390 on all routes. **The Tailwind v4 pins hold — the
  mobile menu works as expected.**
- **Data drift clean (35th)**: the reference's census re-verified BEFORE
  and AFTER all probes (allocation 30.5%, income `$5000.00`, savings
  `$1000.00`, expenses `$525.00` — unchanged; read-only throughout). The
  clone's seed census unchanged (62.8% / 5550 / 1250 / 2235).
- **SEO pair ✓** (live, both sites): robots.txt (allow-all + the sitemap
  line) + sitemap.xml live on both.
- **The items-view rhythm re-audited for the drift class** (items-rhythm
  -v41.mjs on /income, both sites): IDENTICAL — the header row's mb-8
  (the 32px header→filter gap, the v20 G1 pin), the filter card's mb-6
  (the reference's own 24px filter→grid gap), the 86px filter card, the
  grid at y=234. The net-worth page is the only rhythm outlier.

## The v41 surface — the net-worth summary card measured live on BOTH sites at 390×844, 640×960 and 1280×800 (first time at the MID viewport)

Measured with `nw-summary-v41.mjs` (the card/figure/chip/grid/footer
census) + `nw-yoffset-v41.mjs` (the vertical stack attribution) +
`nw-below-v41.mjs` (the below-card gaps):

- **At the MID viewport (640×960 — the "savings-class" unmeasured
  class): FULL geometry parity.** The card 608×333, p-8 (32px), radius
  16px, the forest→lime gradient, the `rgba(26,58,46,0.3) 0 20 60`
  shadow, overflow hidden; the figure 48px/700/white (the `sm:text-5xl`);
  the 64×64 white/20% gradient chip at x=528, radius 9999px, the 32px
  icon; the stats grid 264×264 gap 16, cells at x=48/328, h=84; the
  ratio value 18px; the header chip 48@x=16; the overlay 256/0.1; the
  tabs 448×36; the tabs→grid gap 144; sw=vw (no overflow on either
  site). The chipRow stack (header 61px mobile → +16 → the 60px chip row
  → the 36px h1 at 30px font → the 24px subtitle) matches byte-for-byte.
- **THE PARITY GAP (the first production-code change since v38): the
  net-worth page's vertical rhythm runs 24px where the reference runs
  32px — at BOTH viewports.** (1) the header row→summary-card gap: ref
  32 (`mb-8`) vs clone 24 (`mb-6` — net-worth-view.tsx:292); (2) the
  summary card→tablist gap: ref 32 vs clone 24 (`mb-6` —
  net-worth-view.tsx:308, confirmed by the computed `marginBottom: 24px`
  vs the reference's card-bottom→tablist 32). The 8px offsets show at
  every viewport (card y: 124 vs 116 at 1280; 169 vs 161 at 640). The
  items-view pages already carry `mb-8` (the v20 G1 pin) — the
  net-worth view is the one page that kept the pre-v20 `mb-6` rhythm.
- **The MOBILE superset pair (390×844, re-measured at the card level)**:
  the reference's card is **432px wide at the 390 viewport** (74px page
  overflow, sw=464) — its figure fixed at 48px, its 2-col stats grid
  fixed (176px cells, the second cell's right edge 416), its 64×64 chip
  at x=352 (26px past the viewport). The clone's card is 358 (fits:
  p-4's 16px margins), the figure 24px (`text-2xl` — the superset fix
  #6), the 1-col grid (294px track), the chip fully visible at x=278,
  sw=390. The card chrome (gradient, radius, padding, shadow, the
  64×64/9999px/white-20% chip, the 84px cells, the 18px ratio, the
  256/0.1 overlay) is IDENTICAL — the superset class, not a visual
  divergence.
- **The reference's demo data on /networth**: net `$25,000.00`, ratio
  `∞:1` (debt-free) — vs the clone's seed `-$245,950.00` / `0.21:1`.
  The documented demo-dataset difference (the VLM pairs' standing
  data-flag class).

## Findings

### F1. [PARITY — fix] the net-worth page's 32px vertical rhythm

Two `mb-6` → `mb-8` changes in `src/components/budget/net-worth-view.tsx`
(the header row at line 292 and the summary card at line 308) — matching
the reference's measured 32px gaps at both viewports and joining the
items-view's v20 G1 rhythm (the reference's page-level section rhythm is
uniformly `mb-8`; the in-card and filter-card `mb-6`s stay — they match
the reference's own).

### F2. [PARITY — pin] the summary card's geometry census at the mid viewport (640×960)

One e2e test (a new describe in `tests/e2e/networth.spec.ts`, the
`test.use({ viewport: 640×960 })` pattern): the full band census — the
card's 608 width (p-4 margins), 32px pad, 16px radius, the gradient, the
shadow; the figure's 48px/700; the chip's 64×64 + x=528 + 9999px +
white/0.2 + 32px icon; the grid's 264×2 tracks, 16px gap, the 84px cells;
the 18px ratio; the header chip 48@x=16; the overlay 256/0.1; **the two
rhythm pins: `card.y − chipRow.bottom === 32` and `tablist.y −
card.bottom === 32`** (the F1 fix's pins — relative, scroll-independent);
sw=vw.

### F3. [SUPERSET — pin] the summary card's mobile census (390×844)

One e2e test (the same describe family): the card 358 wide (fits), the
figure 24px (the `text-2xl` superset fix #6 — the reference's fixed 48px
overflows its own 390 viewport by 74px, sw=464), the 1-col grid (the
reference's fixed 2-col overflows), the chip 64×64 fully inside (x+64 ≤
374; the reference's chip hangs 26px offscreen), the sw=390 no-overflow
pin, the card chrome (the gradient/radius/shadow — identical to the
reference's).

### F4. [SUPERSET — pin] the a11y sheet-open structure on the remaining five routes (the second queue item)

The v39 sheet-open test pins the structure on `/` only. Extend the
STRUCTURAL pins (role=dialog, the aria-labelledby → the sr-only
"Navigation" title, the nav landmark with aria-label="Primary", the five
links, the real-burger click, the Escape close) to `/dashboard`,
`/income`, `/expenses`, `/savings`, `/networth` — the v39 `for (const
[route, marker] of authed)` loop pattern in `tests/e2e/a11y.spec.ts`.
The full axe scan stays on `/` only: the sheet's DOM contribution is
route-independent (the global app-shell component) and each route's
page baseline is already scanned sheet-CLOSED by the v39 mobile gate.

### S1. [MUTATION-SANITY] the rhythm, the figure scale, the grid stacking, the sheet title

Four mutations verify the pins bite:
(a) revert the header row's `mb-8` → `mb-6` → the 640 census's
`card.y − chipRow.bottom` pin FAILS (24 ≠ 32);
(b) strip the figure's `sm:text-5xl` → the 640 census's 48px pin FAILS;
(c) strip the grid's `grid-cols-1 sm:grid-cols-2` → the 390 census's
1-col pin FAILS;
(d) strip the sheet's DialogTitle → the route-extension's aria-labelledby
pin FAILS on all five routes.
All restored → GREEN.

### T2. [TOOLING] the v41 probes persisted + the README section

`nw-summary-v41.mjs` (the card census, both sites), `nw-yoffset-v41.mjs`
(the vertical-stack attribution — the 8px delta isolated to the two
margins), `nw-below-v41.mjs` (the below-card gaps), `items-rhythm-v41.mjs`
(the items-view's rhythm — the no-drift control), plus the probe README's
v41 section.

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1: the two `mb-6` → `mb-8` rhythm fixes | fix | `src/components/budget/net-worth-view.tsx` |
| 2 | F2: the 640×960 geometry census e2e (the bands + the two rhythm pins + no overflow) | test | `tests/e2e/networth.spec.ts` |
| 3 | F3: the 390×844 mobile census e2e (the superset pair: 24px figure, 1-col grid, the chip inside, sw=390) | test | `tests/e2e/networth.spec.ts` |
| 4 | F4: the a11y sheet-open structural extension to the remaining five routes (5 tests) | test | `tests/e2e/a11y.spec.ts` |
| 5 | S1(a)–(d): the four pin-sanity mutations, each verified to FAIL then restored | verify | the two files above |
| 6 | The full chain re-run (108 unit · 203 e2e · 35 smoke + lint + typecheck + build) | verify | — |
| 7 | The 16 screenshots regenerated | docs | `docs/screenshots/` |
| 8 | The v41 probes persisted + the probe README's v41 section | docs | `scripts/parity-probes/` |
| 9 | Docs aligned (README v41 row + counts, CLAUDE.md the census entry, AGENTS.md the v41 paragraph, the SKILL state line + session row, session_89.md the formal log, session_90.md the raw transcript, the repo worklog Session 75, the workspace worklog) | docs | repo root + `docs/` |
| 10 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/net-worth-view.tsx` line 292: `<div className="mb-6
  flex items-center gap-3">` (the header row) and line 308: `className=
  "relative mb-6 overflow-hidden rounded-2xl p-8"` (the summary card) —
  the two F1 targets; the mb-6s INSIDE the card (the figure row's mb-8
  at line 323, the cell sublabels) and the filter-card's mb-6 stay (the
  measured matches).
- The 640 census test ports the `test.use({ viewport: ... })` pattern from
  the "net worth mobile header chip (v14)" describe (networth.spec.ts:574)
  — the same `page.evaluate` census idiom (query by the text markers, not
  the class names that shift with the build).
- The figure's seed value: `-$245,950.00` (the grouped format — the spec
  header's arithmetic); the ratio `0.21:1` — both already pinned by the
  desktop tests; the census adds the GEOMETRY only.
- The rhythm pins evaluate the card/chipRow/tablist rects INSIDE one
  `page.evaluate` (scroll-independent relative gaps — the v40 lesson).
- The a11y route extension ports the v39 describe's `authed` loop +
  the sheet-open test's structure-evaluate block verbatim (the sheet
  locator `[data-state='open'][role='dialog']`, the REAL burger click by
  the accessible name "Toggle Sidebar", the 1200ms settle, the Escape
  close assert); marker texts per route from the v39 loop
  (["Total Income", "Total Income", "Salary", "Rent", "Emergency Fund",
  "Assets"]).
- The chain gate: lint → typecheck → 108 unit → build → 196 e2e (203
  after: +2 networth +5 a11y) → 35 smoke. The two census tests add ~8s;
  the five sheet-open routes add ~20s.
