# ZeroBalance — Project Worklog

Rolling log of the engineering sessions on this repo, newest first. Each
session's detailed narrative lives in `docs/session_<n>.md`; findings ledgers
live in `docs/remediation-plan.md` (v1), `docs/remediation-plan-v2.md`,
`docs/remediation-plan-v3.md`, `docs/remediation-plan-v4.md`,
`docs/remediation-plan-v5.md`, `docs/remediation-plan-v6.md`,
`docs/remediation-plan-v7.md`, `docs/remediation-plan-v8.md`, and
`docs/remediation-plan-v9.md`.

---

## Session 17 — Fresh verification & parity iteration v9 (2026-10-08)

**Goal:** `git pull` to `92e837e` (session-16 record), re-verify the v8
baseline, then a fresh two-site parity audit at computed-style depth of the
surfaces no earlier pass had measured that way: the donut's data-order
convention, every form dialog's X-close geometry + sticky-header height,
the form-label line box, the classification-tile text line-height, the
shadcn radio/switch primitive tokens, the v4 `rounded-full` computed
radius, and the login card's per-state control geometry. Explicit
mobile-navigation re-verification (the task focus) + reference data-drift
check.

- Baseline chain at `92e837e` fully green (96/92/30 + lint/typecheck/build);
  detached :3200 parity server + `ref9`/`clone9` (desktop) and
  `reflog9`/`clonelog9` (fresh login) browser sessions.
- Mobile stack re-verified end-to-end: R1/R2/R4 all still live on the
  reference (toast-block hit-test, sheet-trap after nav, 395px overflow);
  all clone superset fixes intact (DIRECT hit, sheet closes, 390px fit).
- 7 finding groups (`docs/remediation-plan-v9.md`): the donut re-sorted to
  the reference's value-DESC convention (biggest slice anchored at
  recharts' 3-o'clock start — the v2-era [S,W,N] pin was the same sort
  wearing that era's data) + `labelLine={false}`; the dialog X-close
  rebuilt as the 36×36 in-header `DialogCloseButton` (sticky header
  69px, default absolute X removed); the form Label restored to the
  inline shadcn-v1 line box (12px label→input gap); 52px classification
  tiles; the radio/switch `#171717` primitive family (checked switch
  track, radio borders/dot, white ring-0 thumb — hex-pinned off the brand
  forest `--primary`); `rounded-full` → `rounded-[9999px]` across 24 sites
  (v4 computes calc(infinity) → 33554432px); login per-state geometry
  (14px primary-button text; 44px sign-up/forgot controls vs 48px
  sign-in). Withdrawn: the login-card border-color difference (both cards
  render border-width 0).
- Mid-flight root-cause: v4 rewrote `space-y-*` to margin-block-end on
  `:not(:last-child)` — layout-IGNORED for inline first children (the
  reference's labels), collapsing the gap to 4px. v3 semantics restored
  for `.space-y-2` in `globals.css` (trap 4b; all 43 usages audited safe).
- TDD: 10 new e2e + 4 updated pins RED → GREEN (donut order/lines, dialog
  chrome ×4, primitive tokens ×3 incl. an `expect.poll` for the
  `transition-colors` race, login geometry ×3; two old `rounded-full`
  class-string pins updated). Full chain: lint · typecheck · 96/96 unit ·
  build · **102/102 e2e** · 30/30 smoke.
- Live parity re-verified surface-by-surface on the fixed build (header
  69, X 36/16, gap 12, tiles 52, switch #171717 + white thumb, radio
  #171717, donut [orange, lime, blue] with 0 label lines, legend
  value-desc, 9999px radii with 0 infinity elements left, login 14px +
  48/44 per state); mobile re-checked; 13 screenshots regenerated;
  docs aligned (README/CLAUDE/AGENTS/SKILL/probe README/session_17 +
  this worklog).

---

## Session 15 — Fresh verification & parity iteration v8 (2026-10-08)

**Goal:** workspace was RESET — re-clone, re-provision the environment, then
a fresh two-site parity audit at computed-style depth of the surfaces v7 had
not covered that way (every form dialog's footer-button geometry, the
item-card badge family's computed colors); fix what it found. Explicit
mobile-navigation re-verification (the task focus).

- Re-cloned fresh; `.env` + `db/` re-provisioned (seed intact); full doc
  chain re-read; baseline chain green at `c6d40fa` (96 unit / 83 e2e /
  30 smoke). v7 fixes confirmed live. Notable environment change: a
  detached parity-server boot now survives across tool calls, so the audit
  ran both sites through persistent agent-browser sessions (`ref8`/`clone8`).
- Mobile nav re-verified live on both sites: R1 (toast container still
  swallows the ref's hamburger — hit-test returns the container), R2 (its
  sheet still traps after nav), R4 (395px/464px overflow) all still live on
  the reference; the clone's superset fixes verified end-to-end (DIRECT
  hit, close-on-nav, 390px fit on all five routes).
- Fresh probe audit → **2 finding groups + 1 hygiene item**
  (`docs/remediation-plan-v8.md`): every form dialog's footer is the
  reference's `flex gap-3 pt-4` full-row split with Cancel + Save at
  `flex-1` (≈ 306px each — the clone ran right-aligned 81px/127px buttons);
  the remaining named-palette classes on parity surfaces all compute as
  `lab()` in v4 (nav `text-zinc-700`, both badge maps, the Recurring/status
  badges, the Calculate button's orange) — values identical to the
  reference's plain rgb, so a full hex-pin pass; and `prisma/db/custom.db`
  (a session-1 stray tracked at the wrong path) untracked.
- The instructive non-finding: the "Recurring" card badge — flipping the
  reference's own Recurring Item switch made the same green badge appear on
  its card (then restored); the badge is CONDITIONAL on both sides and the
  difference was pure live-data drift (SKILL lesson 12.18).
- All fixes TDD-first (12 tests / 13 assertions RED → GREEN): NEW
  `badge-colors.spec.ts` (8), +1 nav-geometry, +3 dialog-buttons footer
  geometry; the unit constants pins and items.spec class pins updated to
  the hex forms (computed values now pinned by the new spec).
- Full chain: typecheck · lint · **96/96 unit** · build · **92/92 e2e**
  (83 + 9 net-new) · 30/30 smoke. Live parity re-verified
  surface-by-surface (footer Cancel 307px + Save 305px — the reference's
  exact numbers; every badge at the reference's exact rgb; nav links
  `rgb(63,63,70)`). 13 screenshots regenerated; seed arithmetic intact.
- Docs aligned (README/CLAUDE/AGENTS/SKILL/session_15 + plan v8 + probe
  README). SKILL gained lessons 12.16–12.18; AGENTS gained the v8 pin
  paragraph.

---

## Session 13 — Fresh verification & parity iteration v7 (2026-10-07)

**Goal:** workspace was RESET — re-clone, re-provision the environment, then
a fresh two-site parity audit of the surfaces no prior session had covered
(the login page's full computed chrome, the rail brand block, the mobile
topbar toggle, the sheet border/overlay colors, the 404 page, the document
head); fix what it found. Explicit mobile-navigation re-verification.

- Re-cloned fresh; `.env` + `db/` re-provisioned (seed intact); full doc
  chain re-read; baseline chain green at `7295906` (96 unit / 73 e2e /
  30 smoke). v6 fixes confirmed live.
- Mobile nav re-verified live on both sites: R1 (toast container still
  swallows the ref's hamburger click), R2 (its sheet still traps after
  nav — `sheetOpen: true` while the URL changed), R4 (395px overflow)
  all still live on the reference; the clone's superset fixes verified
  end-to-end (real-click hamburger, close-on-nav, 390 fit).
- Fresh probe audit → **8 finding groups**
  (`docs/remediation-plan-v7.md`): post-login redirect must land on `/`
  (not `/dashboard`); the login surface — the last one still on named slate
  classes — computed everything in lab()/oklab() AND its footer links were
  missing `text-sm` (16px vs the ref's 14px); the logo halo's ring color
  drifted to oklab (a first probe FALSE-POSITIVED "missing ring" by slicing
  boxShadow at 60 chars — corrected during plan validation); the rail brand
  needed a 24px white lucide-target + `text-lg` logo (the clone's 20px +
  `text-base` sat the whole rail 4px high); the mobile toggle's icon was
  flex-squeezed to 12px (no shrink-0) in the wrong color; the sheet border
  (#e5e7e3 vs the ref's neutral #e5e5e5) and overlay (oklab vs rgba)
  drifted; the clone shipped Next's default 404 (the ref has a branded
  one with the quoted path + Go Home); and the head lacked the ref's
  description/OG/Twitter/canonical/manifest/apple meta.
- All fixes TDD-first (13 specs RED → GREEN): login-card full slate hex
  pin pass + inline gradients + text-sm links + `.zb-logo-ring` sibling
  halo layer (an inline boxShadow on the span would kill its
  shadow-lg/hover), sidebar `TargetIcon h-6 w-6` + `text-lg` + the ref's
  `div.w-full.text-sm` ul wrapper, toggle `[&_svg]:size-4
  [&_svg]:shrink-0` in `#0a0a0a`, sheet border/overlay pins, NEW
  `src/app/not-found.tsx` (quoted-path message via window.location lazy
  init + suppressHydrationWarning, client-side "Page Name | ZeroBudget"
  title, Go Home → `/`), and `layout.tsx` metadata +
  `public/manifest.webmanifest`.
- Full chain: typecheck · lint · **96/96 unit** · build · **83/83 e2e**
  (73 + 10 net-new) · 30/30 smoke. Live parity re-verified
  surface-by-surface (login card identical to the ref on every pinned
  value; rail label/link y exact at 113/145; toggle 16px near-black;
  post-login URL `/`; head complete). 13 screenshots regenerated (new:
  13-not-found), seed arithmetic verified intact after the catalog run.
- Docs aligned (README/CLAUDE/AGENTS/SKILL/session_13 + plan v7 + probe
  README). SKILL gained lessons 12.13–12.15 (probe slicing, inline-shadow
  override, flex-squeeze); AGENTS gained the v7 pin paragraph.

---

## Session 11 — Fresh verification & parity iteration v6 (2026-10-07)

**Goal:** workspace refresh + a fresh two-site parity audit of the surfaces
v2–v5 had NOT covered (net-worth cards/menus, every dialog's EDIT variant,
the calculator's populated rows, ALL empty states, wide-viewport geometry,
overlay dismissal); fix what it found.

- Pulled to `bd2e4be` (session-10 = session-9's narrative record);
  re-validated all docs against the codebase; re-ran the full chain green
  (96 unit / 65 e2e / 30 smoke). v5 fixes confirmed live in code.
- New sandbox behavior (D-9): every background process is reaped at command
  exit and the standalone server crashes under `node` — built
  `scripts/parity-probes/with-server.sh` (per-command bun boot + health
  wait + teardown) and audited through it.
- Fresh probe audit of the un-audited surfaces → **14 finding groups**
  (`docs/remediation-plan-v6.md`): menu items must be plain text (no
  pencil/trash icons), all four Save buttons carry the lucide Save icon,
  asset/liability Name + Last Updated span 624px (`md:col-span-2`) with the
  Type select disabled on edit, the reference's bare-icon empty-state
  pattern (wallet/piggy-bank/receipt/circle-arrow-up/down, no tinted
  circles; items views render it card-less, net-worth carded), the
  calculator's always-visible row actions (32px/16px, near-black/red),
  placeholder strings, hex-pinned status pills, and the padding-outside-
  max-w-7xl content column (the clone was 64px narrow at ≥1568px).
- Measured **reference bug R7** (its dialogs ignore outside-click too) and
  discovered the reference's live DATA changed since the recon (seed
  unchanged — pinned by tests). R1/R5/R6 re-confirmed live; every reference
  mutation this session (test line item, one asset, one recalculated
  category) restored and verified.
- All fixes TDD-first (8 new/extended specs, all RED first): NEW
  `empty-states.spec.ts` (3, incl. an API delete/restore fixture dance that
  re-creates liabilities in reverse capture order to preserve `createdAt`
  ordering — D-10), +1 dialog-buttons (Save icons), +2 networth (dialog
  grid spans, disabled-on-edit type), +1 tokens (plain-text menus + red
  pins + trigger hover class), +1 calculator (row chrome + placeholders +
  pills + empty icon).
- Full chain: typecheck · lint · **96/96 unit** · build · **73/73 e2e** ·
  30/30 smoke. Live parity re-verified surface-by-surface; 12 screenshots
  regenerated.
- Docs aligned (README/CLAUDE/AGENTS/SKILL/session_11 + plan v6). SKILL
  gained D-9/D-10; AGENTS gained the v6 parity pin paragraph and the
  fixture-order restore rule.

---

## Session 9 — Fresh verification & parity iteration v5 (2026-10-07)

**Goal:** workspace refresh + a deeper two-site parity audit (the reference's
own token layer, dialog buttons, dropdown states, focus rings, hover
semantics, responsive chrome map); fix what it found.

- Pulled to `e23d854` (session-8 = session-7's narrative record);
  re-validated all docs against the codebase; re-ran the full chain green
  (96 unit / 52 e2e / 30 smoke). v4 fixes confirmed live in code and browser.
- Token-level audit (reading the reference's `:root` vars + an
  inherited-text sweep + `hover:none` emulation) → **10 finding groups**
  (`docs/remediation-plan-v5.md`): zinc-vs-neutral foreground family,
  input/popover borders, the net-worth tab grid + green active state,
  dialog action buttons (ghost Cancel + solid-lime Save vs outline +
  per-dialog gradients), the accent pair, nav hover text, v4's
  media-gated hover variants, muted, lab/oklab drift on three colored
  texts, and the focus-ring tokens.
- Measured **two new reference bugs**: R5 (its dialogs ignore Escape —
  plain fixed overlays, no keyboard dismissal) and R6 (its card-menu
  Delete destroys items immediately, no confirmation). R1–R4 re-confirmed
  live; all clone superset fixes re-verified end-to-end.
- All fixes TDD-first (13 new/extended specs, all RED first): the
  reference's neutral token block in `globals.css`, `@variant hover
  (&:hover)` (v3 hover semantics on every device), the reference tab
  structure (448px grid, `#dcfce7`/`#14532d` active, 24px gap),
  outline Cancellations + gradient Saves (forest for budget/asset,
  orange for line-item/liability — `.zb-btn-primary` removed),
  popover borders → input neutral, arbitrary-hex pins for the
  lab-drifted colors, inline rgba white-alpha labels, ring tokens
  (`#0a0a0a` / `#3b82f6`).
- Full chain: typecheck · lint · **96/96 unit** · build · **65/65 e2e** ·
  30/30 smoke. Live parity re-verified surface-by-surface (every fixed
  value now measures identical to the reference); 12 screenshots
  regenerated.
- Docs aligned (README/CLAUDE/AGENTS/SKILL/session_9 + plan v5). SKILL
  gained D-6/D-7/D-8 (hover media gate, prerender empty-store race,
  lab/oklab drift); AGENTS gained the prerender settle convention and
  the six-superset pin list.

---

## Session 8 — Audit narrative record (2026-10-07)

Session-7's fresh-verification + remediation-v4 narrative, committed as
`docs/session_8.md` (the raw work log of `28ad5fc`).

---

## Session 7 — Fresh verification & parity iteration v4 (2026-10-07)

**Goal:** workspace refresh + a fresh two-site parity audit of every
surface; fix what it found.

- Pulled to `4f9cb28` (session-6 = session-5's narrative record);
  re-validated all docs against the codebase; re-ran the full chain green
  (96 unit / 46 e2e / 30 smoke). Found CLAUDE.md carrying stale session-2
  test counts — fixed in the docs pass.
- Fresh probe-based audit (clone vs live reference, desktop 1280×800 +
  mobile 390×844) → **6 finding groups** (`docs/remediation-plan-v4.md`):
  nav-link height (40px vs the reference's `h-8` 32px), inactive hover
  tint (sidebar-accent vs green-50), active hover dim, the net-worth
  summary card's structure (3-col ratio grid vs the reference's 2-col
  grid + border-t ratio footer row), a 38px mobile net-worth overflow
  (unbreakable `text-4xl` figure stretching the flex-1 `main`), and the
  items-view header count ignoring active filters.
- Measured **two new reference mobile bugs**: its own `/dashboard` scrolls
  to 395px and `/networth` to 464px at 390px (R3/R4). Both prior reference
  mobile-nav bugs re-confirmed live; the clone's fixes re-verified.
- All fixes TDD-first: new `nav-geometry.spec.ts` (3), +2 networth specs,
  +1 items spec — all verified red before implementing. Key changes:
  `h-8` + `hover:bg-green-50` nav links, the reference's summary-card
  layout (2-col grid, xs/70 labels, 2xl amounts, blur, ratio footer row
  with an inline rgba border — dodging the v4 oklab drift), responsive
  `text-2xl sm:text-5xl` net figure, **`min-w-0` on `main`** (the
  structural superset fix for flex min-width:auto overflows), and
  `filtered.length` header counts.
- Full chain: typecheck · lint · **96/96 unit** · build · **52/52 e2e** ·
  30/30 smoke. Live parity re-verified (nav 32px, summary card
  leaf-identical at desktop, all mobile views exactly 390px).
- Screenshot catalog regenerated — now 12 shots (new
  `12-mobile-networth.png`). README/CLAUDE/AGENTS/SKILL/session_7
  aligned; SKILL gained the D-5 row (min-width:auto trap +
  `overflow-wrap: break-word` ≠ min-content).

---

## Session 5 — Fresh verification & parity iteration v3 (2026-10-07)

**Goal:** workspace refresh + a fresh two-site parity audit of every
surface; fix what it found.

- Re-cloned (workspace had been reset); validated all docs against the
  codebase; re-ran the full chain green (95 unit / 39 e2e / 30 smoke).
- Fresh probe-based audit (clone vs live reference, desktop + mobile
  390×844) → **6 finding groups** (`docs/remediation-plan-v3.md`),
  headlined by a CRITICAL clone-side mobile layout bug present since
  session 1: the mobile top bar rendered as a row-flex sibling of `<main>`
  (222px column, main squeezed to 214px, 90px overflow) — invisible to
  the interaction-only e2e suite. Also: the items-views filter card,
  classification tile chrome, the line-item dialog's Payment Method
  field / labels / OWN status enum (active/pending/cancelled), the login
  card's sign-up/forgot structure (+ removal of the dead guest link),
  and the reference's root-URL active-nav gap (documented superset #3).
- All fixes TDD-first: new `mobile-layout.spec.ts` (3), +2 items specs,
  +1 calculator spec, +1 auth spec, +1 validation test. Full chain:
  typecheck · lint · **96/96 unit** · build · **46/46 e2e** · 30/30
  smoke.
- Live parity re-verified on the remediated build (mobile geometry,
  filter card, tiles, line-item dialog, login states — all matching);
  both reference mobile-nav bugs confirmed still live.
- Screenshots regenerated (11); README/PAD/SKILL/session_5 aligned.

---

## Session 4 — Audit narrative record (2026-10-07)

Session-3's deep-audit + remediation-v2 narrative, committed as
`docs/session_4.md` (the raw work log of `8b82e4c`).

---

## Session 3 — Deep parity audit & remediation v2 (2026-10-07)

**Goal:** production-ready superset of `zero-balance-4885a8f3.base44.app` with
visual parity; fresh re-verification of every surface.

- Deep-audited the live reference DOM (computed styles, real clicks/hovers)
  AND its minified JS bundle (template extraction) → **14 finding groups**
  (`docs/remediation-plan-v2.md`): money format split (plain `toFixed(2)` vs
  networth-only grouping), `0.21:1` ratio, the 3-level accordion breakdown
  drill-down, donut order/icons, calculator card restructure, stat cards,
  hero conditional states (✓ NET ZERO / blue over-budget / Math.abs), per-view
  add-button gradients, quick-action card-buttons, badge color maps,
  expense-card hover buttons (no ellipsis), networth type grouping, icon
  corrections, always-plural "N items".
- Implemented all fixes TDD-first: money/constants/dashboard-math unit tests
  rewritten or extended; new `breakdown.spec.ts`; dashboard/items/networth/
  calculator specs rewritten. Superset: delete path for expense items via the
  edit dialog (the reference has none on expense cards).
- Full chain green: typecheck · lint · 95/95 unit · build · 39/39 e2e
  (incl. 7 mobile-nav + 5 breakdown) · 30/30 smoke.
- Live parity re-verified on the remediated build; both reference mobile-nav
  bugs confirmed still live (clone fixes both — pinned).
- Screenshots regenerated (11, incl. `11-breakdown-drilldown.png`); README /
  PAD / SKILL / session_3.md aligned.

---

## Session 2 — Re-verification + distillation (2026-10-07)

**Goal:** re-run the full verification chain, live parity check, and produce
the added deliverables (remediation plan record, SKILL doc, doc alignment).

- Re-validated docs against the codebase; re-ran the full chain (87 unit /
  34 e2e / 30 smoke, typecheck/lint clean).
- Live parity re-check (desktop + mobile 390×844): both reference mobile-nav
  bugs confirmed still live; clone superset verified (hamburger hit-test,
  sheet close-on-nav, Escape).
- Wrote `docs/remediation-plan.md` (session-1/2 findings ledger with the
  20-item ToDo record and regression pin map).
- Distilled `zero-balance_SKILL.md` (20 sections + ADRs + audit history +
  quick-reference card) per the distill-codebase / to-distill-project-into-skill
  method, with every claim verified against the codebase.
- Fixed doc drift (.env.example header, API handler count 13 route files /
  21 handlers). Pushed `6bf69a6`.

---

## Session 1 — Build (2026-10-07)

**Goal:** from scaffolding repo to production clone with test suites.

- Reconned the reference (all views, modals, mobile chrome, design tokens,
  entity schemas); found the two reference mobile-nav bugs (toast viewport
  click-block; sheet stays open after nav).
- Built the app: Next.js 16 App Router, Prisma/SQLite (`db/custom.db`),
  scrypt+HMAC cookie auth, Zustand store, Tailwind v4 with the five trap-log
  mitigations, recharts donut, shadcn-style primitives.
- 13 route files / 21 API handlers, zod validation, rate-limited login,
  server-side line-item recalculation contract.
- Replaced the ORBITAL-era tests with the ZeroBalance suites (87 unit + 34
  e2e incl. 7 mobile-nav specs) + a 30-step smoke test; fixed 7 real bugs the
  tests caught (zustand v5 loop, modal stacking, dialog states, date
  validation…).
- Rewrote the root docs (README, AGENTS, CLAUDE, PAD); screenshots; pushed
  `703ea74`, `6efc1ce`.
