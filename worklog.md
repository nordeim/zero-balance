# ZeroBalance — Project Worklog

Rolling log of the engineering sessions on this repo, newest first. Each
session's detailed narrative lives in `docs/session_<n>.md`; findings ledgers
live in `docs/remediation-plan.md` (v1), `docs/remediation-plan-v2.md`,
`docs/remediation-plan-v3.md`, `docs/remediation-plan-v4.md`, and
`docs/remediation-plan-v5.md`.

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
