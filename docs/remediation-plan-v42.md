# Remediation Plan v42 — The Mid-Viewport Census of the Five Routes + the
# Breakdown Card's Single-Divider Fix (the session-90/91 queue)

Date: 2026-10-11 · Scope: fresh two-site re-audit after the v41 baseline
(`9978987` + the session-log commits `3f89e53`/`d5068c8` on `main`; the
workspace survived the session break — `git pull` fast-forwarded to
`d5068c8`, the environment intact: node_modules, `.env`
(`DATABASE_URL="file:../db/custom.db"`), `db/custom.db` + `db/e2e.db` at
the repo root, playwright chromium). Baseline chain on the re-run: lint ✓
· typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**203/203 e2e ✓ (4.7m, the first run, zero flakes)**; npm audit = the same
5 dev-only ESLint `braces` advisories — accepted, unchanged, dev-only; the
secret-pattern scan clean (src/tests/scripts); `.env` verified
byte-identical to `.env.example`. The v41 src diff re-audited (the two
mb-8 rhythm fixes + the two census describes — exactly the documented
changeset, nothing else).

The sweep — method and results: the session-90/91 queue's headline surface
(the MID viewport 640×960 census of the five non-networth routes — the v41
lesson applied: "an unmeasured VIEWPORT CLASS is as dangerous as an
unmeasured surface"), plus the standing re-verification set (mobile-nav
R1–R4 on BOTH sites, data drift, the SEO pair) and the code audit. One
process note (carried from v41): this sandbox reaps background processes
between tool calls — every long job (the e2e suite, the parity server)
runs inside a single invocation via `scripts/with-server.sh`.

- **Mobile navigation (the standing task focus) R1–R4 all re-verified
  live on BOTH sites — the 36th consecutive check.** R1: the reference's
  toast containers still intercept the burger's center hit
  (`DIV.fixed.top-0.z-[100]`, scrollWidth 395); the clone's hit DIRECT on
  the svg, fits 390. R2: the reference's sheet still traps after nav
  (sheet open, body locked on /income); the clone's closes. R3: the
  reference marks nothing active on `/` and has no `<nav>`; the clone has
  the landmark. R4: the reference overflows 395 on `/`+`/dashboard`; the
  clone fits 390 on all routes. **The Tailwind v4 pins hold — the mobile
  menu works as expected.**
- **Data drift clean (36th)**: the reference's census re-verified BEFORE
  and AFTER all probes (allocation 30.5%, income `$5000.00`, savings
  `$1000.00`, expenses `$525.00` — unchanged; read-only throughout). The
  clone's seed census unchanged (62.8% / 5550 / 1250 / 2235).
- **SEO pair ✓** (live, both sites): robots.txt (allow-all + the sitemap
  line) + sitemap.xml live on both.

## The v42 surface — the five routes measured live on BOTH sites at 640×960 (mid-census-v42.mjs)

- **The 32px rhythm HOLDS on all five routes** — `gapRowToFirst === 32`
  everywhere (the page-header row's mb-8, the v20 G1 pin's class extended
  to the mid viewport). The header (61px), main (pad 0 — the padding lives
  on the view wrapper), h1 (30px font, 36px high), the content cap
  (`capW 608` = 640 − 2×16), `sw 640` (no overflow on either site) — all
  byte-identical.
- **The items-view routes (/income, /expenses, /savings) fully match**:
  the headerRow (y=77, h=112, mb=32, column), the filter card (y=221,
  h=190/190/242 by route, mb=24, display block), the item grid (1-col,
  16px gap). The only height deltas are the seed's item counts (data, not
  parity).
- **THE PARITY GAP (the first production-code change since v41): the
  dashboard's NetZeroBreakdownCard runs +13px taller than the reference —
  at BOTH viewports** (640: 337 vs 324; 1280: 377 vs 364). Attribution
  (hero-attrib-v42.mjs + bd-attrib-v42.mjs): the goalCard is byte-identical
  (316 at both sites, the bands 48/48/108, the donut 558×300/418×300);
  the row heights are identical (56/64/64 at 1280 — the wrap behavior
  included); **the delta is ONE EXTRA DIVIDER BAND: the clone renders TWO
  `Divider`s (Income|Savings AND Savings|Expenses); the reference renders
  ONE (Income|Savings only)**. The extra 12+1px band carries into every
  band below the hero at 640 (secondBand y 938 vs 925; thirdBand y 1648 vs
  1635; `scrollH 3042 vs 3029` — the tail-v42.mjs check: exactly +13, the
  lastBand mb=0 on both sites, no trailing-margin class).
- The reference's structure reads as the app's ONE rule rendered as
  groups: **[Income] | divider | [Savings, Expenses] | border-t | [Net
  Balance]** — the source separated from the allocation pair, the Net
  Balance footer carrying its own border-t (mt-3). The clone's uniform
  `i > 0` divider was a build-time assumption, never measured.

## Findings

### F1. [PARITY — fix] the breakdown card's single-divider structure

One condition change in `src/components/budget/dashboard-view.tsx` line
410: `{i > 0 && <Divider />}` → `{i === 1 && <Divider />}` — the Divider
renders only between the first and second sections (Income|Savings),
joining the reference's `[Income] | [Savings, Expenses] | [Net]`
grouping. The 12+1px band removed; the card's height joins the reference
at both viewports (324 at 640, 364 at 1280) and every band below the
hero shifts back 13px at 640 (secondBand 925, thirdBand 1635, scrollH
3029).

### F2. [PARITY — pin] the breakdown card's census at 1280 + the hero grid at 640

Two e2e tests (a new describe in `tests/e2e/dashboard.spec.ts`, the
`page.evaluate` census idiom): (1) the breakdown card's band census at
1280 — the 5-band stack [56, 1, 64, 64, 45], the single divider, the card
h=364, pad 24px / radius 16px / border 1px, the Net Balance footer (the
border-t row); (2) the dashboard hero grid at 640 — the goalCard 316, the
breakdownCard y=569 h=324, the 24px inter-card gap, the hero total 664,
secondBand y=925, thirdBand y=1635, scrollH 3029 (the F1 fix's pins at
both viewports).

### F3. [PARITY — pin] the MID viewport (640×960) band census of the five routes

One e2e test (the same describe): the five-route loop (`/`, `/dashboard`,
`/income`, `/expenses`, `/savings` — the a11y route-extension for-loop
pattern) pinning the common census — `gapRowToFirst === 32`, `capW 608`,
`sw 640`, the h1 30px/36, the headerRow mb=32 dir=column — plus the
route-class branches: the dashboard routes assert the hero grid (display
grid, 1 col, 24px gap, h=664 post-fix); the items routes assert the
filter card (display block, mb=24px) and the item grid (1 col, 16px gap).
The v41 lesson pinned for the remaining routes.

### S1. [MUTATION-SANITY] the divider, the two rhythms

Three mutations verify the pins bite:
(a) revert the divider condition to `i > 0` → the band-count pin fails
(6 ≠ 5), the card-height pin fails (377 ≠ 364), the scrollH pin fails;
(b) the items-view header row's `mb-8` → `mb-6` → the /income route's
`gapRowToFirst` pin fails (24 ≠ 32);
(c) the dashboard header row's `mb-8` → `mb-6` → the / route's pin fails.
All restored → GREEN.

### T2. [TOOLING] the v42 probes persisted + the README section

`mid-census-v42.mjs` (the five-route mid-viewport census, both sites),
`hero-attrib-v42.mjs` (the hero grid attribution), `bd-attrib-v42.mjs`
(the breakdown card's internals — the band-by-band census that isolated
the second Divider), `tail-v42.mjs` (the last-band margin + scrollHeight
check), plus the probe README's v42 section.

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F2/F3: the three census e2e tests written FIRST (TDD red: the band-count 6≠5, the heights 677/377, the scrollH 3042 — all should FAIL against the current build) | test | `tests/e2e/dashboard.spec.ts` |
| 2 | F1: the divider condition fix `{i === 1 && <Divider />}` | fix | `src/components/budget/dashboard-view.tsx` |
| 3 | Rebuild → green phase (the three census tests first-run) | verify | — |
| 4 | S1(a)–(c): the three pin-sanity mutations, each verified to FAIL then restored | verify | the two files above |
| 5 | The full chain re-run (108 unit · 206 e2e · 35 smoke + lint + typecheck + build) | verify | — |
| 6 | The 16 screenshots regenerated | docs | `docs/screenshots/` |
| 7 | The v42 probes persisted + the probe README's v42 section | docs | `scripts/parity-probes/` |
| 8 | The standing VLM pair (screening — the desktop dashboard post-fix; every flagged diff DOM-verified) | verify | `scripts/parity-probes/` |
| 9 | Docs aligned (README v42 row + counts, CLAUDE.md the census entry, AGENTS.md the v42 paragraph, the SKILL state line + session row, session_92.md the formal log, session_93.md the raw transcript, the repo worklog Session 76) | docs | repo root + `docs/` |
| 10 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/dashboard-view.tsx:410`:
  `{i > 0 && <Divider />}` inside the `sections.map` — the F1 target;
  the `Divider` (line 369) is `my-3 border-t` (12+1+12 collapsed against
  the space-y-3 margins — the measured extra band: 13px).
- The `sections` array (line ~390): income / savings / expense — the
  divider indices: `i === 1` renders between sections[0] (Income) and
  sections[1] (Savings) only.
- The census tests port the v41 `networth.spec.ts` idiom (the
  `page.setViewportSize({ width: 640, height: 960 })` + `page.evaluate`
  census; query by the text markers, never the class names). The
  five-route loop ports the a11y spec's `for (const route of authed)`
  pattern.
- The measured pin values (the clone's seed): the dashboard at 640 —
  goalCard 316, breakdownCard 324@y=569 (post-fix; 337 pre-fix), hero 664
  (post-fix; 677 pre-fix), secondBand y=925 (post-fix; 938 pre-fix),
  scrollH 3029 (post-fix; 3042 pre-fix); the breakdown at 1280 — the
  bands [56, 1, 64, 64, 45] (the wrap behavior data-robust: the reference
  renders the same heights with its own amounts), card 364 (post-fix;
  377 pre-fix). The items routes at 640 — filter h 190/190/242 by route,
  mb 24, grid 1-col gap 16.
- The chain gate: lint → typecheck → 108 unit → build → 203 e2e (206
  after: +3 census) → 35 smoke. The three census tests add ~10s.
