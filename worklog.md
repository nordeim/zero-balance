# ZeroBalance — Project Worklog

Rolling log of the engineering sessions on this repo, newest first. Each
session's detailed narrative lives in `docs/session_<n>.md`; findings ledgers
live in `docs/remediation-plan.md` (v1), `docs/remediation-plan-v2.md`, and
`docs/remediation-plan-v3.md`.

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
