# Remediation Plan v40 — The Dashboard's Tab-Order Focus Walk (the Last Unmeasured Session-78 Surface)

Date: 2026-10-11 · Scope: fresh two-site re-audit after the v39 baseline
(`a886a79` + the session-log commits `6e75f2b`/`8a7a3b4` on `main`; the
workspace survived the session break — `git pull` fast-forwarded to
`8a7a3b4`, the environment intact: node_modules, `.env`
(`DATABASE_URL="file:../db/custom.db"`), `db/custom.db` + `db/e2e.db` at
the repo root, playwright chromium). Baseline chain on the re-run: lint ✓
· typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**195/195 e2e ✓ (4.5m, first run, zero flakes)** · 35/35 smoke ✓; npm
audit = the same 5 dev-only ESLint `braces` advisories — accepted,
unchanged, dev-only; the secret-pattern scan clean (src/tests/scripts);
`.env` verified byte-identical to `.env.example`.

The sweep — method and results: the v39-queue headline surface (the
dashboard quick-action focus walk — the session-78 queue's LAST
unmeasured surface), plus the standing re-verification set (mobile-nav
R1–R4 on BOTH sites, data drift, the SEO pair, one VLM pair) and the
code audit.

- **Mobile navigation (the standing task focus) R1–R4 all re-verified
  live on BOTH sites — the 34th consecutive check.** R1: the reference's
  toast containers still intercept the burger's center hit
  (`DIV.fixed.top-0.z-[100]`, scrollWidth 395); the clone's hit DIRECT on
  the svg, fits 390. R2: the reference's sheet still traps after nav
  (sheet open, body locked on /income); the clone's closes. R3: the
  reference marks nothing active on `/` and has no `<nav>`; the clone has
  the landmark. R4: the reference overflows 395 on `/`+`/dashboard`;
  the clone fits 390 on all routes. **The Tailwind v4 pins hold — the
  mobile menu works as expected.**
- **Data drift clean (34th)**: the reference's census re-verified BEFORE
  and AFTER all probes (allocation 30.5%, income `$5000.00`, savings
  `$1000.00`, expenses `$525.00` — unchanged; read-only throughout: the
  focus walk presses Tab only, the probes read + focus, the VLM pair
  captures). The clone's seed census unchanged (62.8% / 5550 / 1250 /
  2235).
- **SEO pair ✓** (live, both sites): robots.txt (allow-all + the sitemap
  line) + sitemap.xml (five URLs, priority 1.0/0.8, weekly) live on both;
  the reference's sitemap still capitalizes its app-route URLs
  (`/Income`, `/Savings`) while the clone mirrors its own lowercase
  routes (the documented v21 decision).

## The v40 surface — the dashboard's Tab-order focus walk (first-time measured live on BOTH sites)

Measured with `tabwalk-v36.sh` (the REAL-Tab walk, 22 presses) +
`focus-census-v40.mjs` (the clean DOM-order focusable census, no
Tab-scroll artifacts) + `stat-card-chain-v40.mjs` (the text-ancestor
chains) + `donut-focused-dump-v40.mjs` (the donut stop's structure):

- **The reference's cycle (14 focusable stops, doc order)**: the five
  sidebar nav links (`a`, x=20, w=215, h=32, the 40px rail pitch) → the
  Add Item header button `[1121,50,127,36]` → the three NetZero-breakdown
  stat-row buttons (`button.w-full` at x=961, w=254, h=56/64) → the
  donut's `g.recharts-layer.recharts-pie` **tabindex=0** (its
  textContent carries the sector labels "92.3%4.6%3.1%" — recharts 2
  renders the labels inside the pie g) → the three quick-action card
  buttons (`[288/616/944, y≈1462, 304×90]`) → the Base44 "Close badge"
  (platform chrome, not app UI) → wrap.
- **The clone's cycle (16 stops)**: the SAME walk — nav(5) → Add Item →
  the three stat-row buttons → **PLUS the three interactive stat cards**
  (`div[role="button"][tabindex="0"]` at [288/616/944, y≈545, 304×210])
  → the donut's `g.recharts-pie` tabindex=0 (empty textContent —
  recharts 3 renders the labels in a separate layer; the visible chrome
  is identical, VLM-clean) → the three quick-action cards → wrap to the
  body. **The platform badge is correctly absent** (the v36 census
  treatment).
- **THE HEADLINE SUPERSET**: the reference's BIG stat cards (the
  304×210 row at y≈532 — visually identical to the clone's) are **INERT
  divs** — `div.relative.overflow-hidden.rounded-2xl.p-6` with NO role,
  NO tabindex, NO handler (measured by stat-card-chain-v40.mjs: the
  Total Income text chain bottoms out at the plain grid div). The
  clone's are `div[role=button]` + `tabIndex=0` + Enter/Space handlers
  that route to the type view — the same dead-UI-fixed superset class
  as the kebab focus reveal (#7): the reference shows an interactive-
  LOOKING card (hover shadow + cursor) that does nothing.
- **The donut stop matches structurally (F2 — the v31 replication
  confirmed at the walk level)**: `g.recharts-pie` tabindex=0 on BOTH
  sites, the sector paths (`path.recharts-sector` name=Need/Savings/Want)
  tabindex=-1 roving on both, the svg surface inert (no role/tabindex)
  on both. The clone's svg additionally carries recharts-3's
  `recharts-zIndex-layer_*` groups (library internals, invisible).
- **Geometry bands (F3)**: the nav links, Add Item, the stat-row
  buttons' x=961/w=254, the stat cards' 304×210, and the quick actions'
  304×90 all sit at the reference's positions within a **13px vertical
  band drift** that starts at the reference's THIRD stat-row button: the
  reference's own column gaps are inconsistent (25px then 12px) while
  the clone's are a consistent 25px — a reference layout quirk, both
  surfaces VLM-clean (the pair below flags zero geometry issues).
- **The VLM pairwise (one fresh pair, 1280×800)**: the desktop
  dashboard — VERDICT DIFFERENT with ALL THREE flags explained: (1) the
  clone's Dashboard link carries the active highlight (superset fix #3
  — the reference marks nothing active on `/`, its R3 bug); (2) the
  Budget Allocation progress bar length (the different demo data: 62.8%
  vs 30.5%); (3) the avatar letter D vs U (the different demo users).
  Zero unexplained visual drift.

## Findings

### F1. [SUPERSET — pin] the dashboard's Tab-order census + the interactive stat cards

Pin the measured walk as one e2e test (`tests/e2e/dashboard.spec.ts`,
after the donut keyboard contract): the 16 REAL-Tab stops with tag +
role + accessible name + the focusability attrs, the nav geometry bands
(x=20, w=215, the 40px pitch), the per-class x/w/h bands, the wrap, and
the superset activation pair — Enter on the focused Total Income stat
card routes to /income, Space on the Total Savings card routes to
/savings (the reference's inert cards do NOTHING on either key).

### S1. [MUTATION-SANITY] the stat card's role/tabindex and its Enter handler

Two mutations verify the new pins bite:
(a) strip the StatCard's `role="button"` + `tabIndex={0}` + rebuild →
the census FAILS at the stat-card stops (the divs drop out of the walk —
the Tab skips to the donut g).
(b) remove the StatCard's Enter/Space key handler + rebuild → the
activation pin FAILS (Enter on the focused card no longer routes).
Both restored → GREEN. Zero production-code changes ship.

### T2. [TOOLING] the v40 probes persisted + the README section

`focus-census-v40.mjs` (the clean DOM-order focusable census, both
sites), `stat-card-chain-v40.mjs` (the text-ancestor chains — the
inert-vs-interactive verdict), `donut-focused-dump-v40.mjs` (the donut
stop's structure), `vlm-compare-v40.mjs` (the desktop dashboard pair),
`ref-v40.sh` / `clone-v40.sh` (the 34th standing checks) — plus the
probe README's v40 section (the lessons: the clean census must filter
`[tabindex]=-1` AND zero-rect elements or recharts' hidden zIndex layers
pollute the count; the reference's stat-card inertness is only visible
via the text-ancestor chain — the census alone shows both sites' stat
ROWS as buttons).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | The dashboard Tab-order census e2e: the 16 REAL-Tab stops (tag + role + name + tabindex) + the geometry bands + the wrap + the superset activation pair (Enter → /income, Space → /savings) | test | `tests/e2e/dashboard.spec.ts` |
| 2 | S1(a) pin-sanity: strip the StatCard's role+tabIndex → the census FAILS at the stat-card stops; restore → GREEN | verify | `src/components/budget/dashboard-view.tsx` |
| 3 | S1(b) pin-sanity: remove the StatCard's key handler → the activation pin FAILS; restore → GREEN | verify | `src/components/budget/dashboard-view.tsx` |
| 4 | The full chain re-run (108 unit · 196 e2e · 35 smoke + lint + typecheck + build) | verify | — |
| 5 | The 16 screenshots regenerated (the deliverable brief's capture pass) | docs | `docs/screenshots/` |
| 6 | The v40 probes persisted (the 5 scripts above) + the probe README's v40 section | docs | `scripts/parity-probes/` |
| 7 | Docs aligned (README v40 row + counts, CLAUDE.md the census entry, AGENTS.md the v40 paragraph, SKILL state line + session row, session_86.md the formal log, session_87.md the raw transcript, the repo worklog Session 74, the workspace worklog) | docs | repo root + `docs/` |
| 8 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `tests/e2e/dashboard.spec.ts` (348 lines): the insertion point is the
  file's end (after the "arrow keys rove sector focus" test, inside the
  top-level describe). The v36 items-view census idiom ports directly:
  the `readStop` evaluate (tag/role/name/rect/opacity), the pre-walk
  blur, the REAL Tab presses with 450ms settles, the per-stop tag+name
  asserts, the nav-pitch evaluate, the wrap assert.
- The expected stop names come from the seed's exact arithmetic (the
  same numbers the stat-cards test already pins): "Total
  Income$5550.002 items", "Total Savings$1250.002 items", "Total
  Expenses$2235.003 items" — the div textContent concatenation, sliced
  at 30 chars in `readStop` ("Total Income$5550.002 items" = 27, "Total
  Expenses$2235.003 items" = 29 — both fit).
- The stat-row BUTTON names carry the minus prefix for the two negative
  rows: "Total Savings- $1250.00", "Total Expenses- $2235.00" (the
  reference's own format, measured both sites).
- `src/components/budget/dashboard-view.tsx` lines 450–530: the
  StatCard renders `div[role="button"][tabIndex={0}]` with the
  `onKeyDown` Enter/Space handler routing via `router.push(href)` —
  the S1(a) mutation strips the role+tabIndex attributes; the S1(b)
  mutation removes the onKeyDown handler. The click navigation is
  already pinned by the existing "stat cards show forestDark amounts,
  counts and navigate" test (v-prior) — the v40 test adds the KEYBOARD
  half only.
- The donut stop assert: `tag: "g"` + `name: ""` (the clone's pie g
  carries no text — recharts 3 renders the labels in a separate layer;
  the reference's g textContent is "92.3%4.6%3.1%", a library-internal
  placement difference, VLM-clean, documented — NOT a regression).
- The walk settles: 450ms per stop (the v36 sheet-ring fade discipline);
  the page auto-scrolls as Tab moves focus (assert only the
  scroll-independent bands: x, w, h — the y values drift with the
  scroll).
- The activation sub-assert re-focuses the card directly (the
  `div[role='button']` locator filtered by hasText) rather than walking
  back — the focusability itself is already proven by the walk's stops
  10–12.
- The chain gate: lint → typecheck → 108 unit → build → 195 e2e (196
  after the v40 test) → 35 smoke. The census test adds ~25s (16 stops ×
  450ms + the two activation routes).
