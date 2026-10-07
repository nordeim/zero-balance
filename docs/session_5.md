# Session 5 — Fresh Verification & Parity Iteration v3

**Date:** 2026-10-07 · **Scope:** workspace refresh, full-chain re-verification, a fresh two-site parity audit (desktop 1280×800 + mobile 390×844), and remediation v3 · **Outcome:** 6 finding groups fixed TDD-first, full chain green (96 unit / 46 e2e / 30 smoke), live parity re-verified, pushed to `main`.

## Where this session started

The workspace had been reset, so the session began with a fresh clone.
Session 4 (logged in `session_4.md`) had completed the interrupted
deep-audit remediation v2 and pushed `8b82e4c`; this session treated that
as the baseline and set out to (a) re-verify the whole chain from scratch,
(b) re-audit every surface against the live reference with fresh probes,
and (c) fix whatever the new pass found.

## Baseline verification (before any change)

- Docs review: AGENTS / CLAUDE / README / PAD / SKILL / session_3 /
  session_4 / remediation-plan-v2 — all claims validated against the
  codebase (13 route files / 21 handlers, 95 unit tests, 7 e2e spec files,
  `.env.example` aligned, db-path discipline).
- Full chain: typecheck ✓ · lint ✓ · 95/95 unit ✓ · build ✓ · 39/39 e2e ✓
  · 30/30 smoke ✓.

## The fresh audit (probe scripts under `scripts/parity-probes/`)

Two agent-browser sessions (clone on :3200, live reference), DOM +
computed-style probes on both, surfaces covered: dashboard (hero, stat
cards, donut sectors/labels/legend, guidelines, quick actions, breakdown
drill-down), items views (headers, filter area, cards, badges, hover
buttons), all five dialogs, net worth, login's three states, mobile chrome
(hamburger hit-test, sheet geometry, close-on-nav, layout measurements).

Confirmed matching (no action): donut slice labels (16px, sector fills),
hero structure, avatar, guidelines tints, badge maps, calculator card +
rows + empty state, net worth ratio/grouping/footers, breakdown
levels/footers, sheet geometry, and both reference mobile-nav bugs
**still live** (toast-viewport hamburger block + stuck sheet).

Six finding groups — `remediation-plan-v3.md`:

1. **F1 [CRITICAL — clone bug]** The mobile top bar rendered as a
   row-flex SIBLING of `<main>` (a React fragment child of the shell's
   `div.flex`), so at 390px it became a 222px full-height column: main
   squeezed to 214px, `scrollWidth` 480. Present since session 1 and
   invisible to the interaction-focused e2e suite. The reference nests the
   header INSIDE `main` (61px tall: py-4 + 28px panel-left toggle +
   border; `gap-4` row; `h1 text-xl` brand; toggle `hover:bg-green-50`
   with an sr-only "Toggle Sidebar").
2. **F2** Items views: the reference wraps search + selects in a white
   `rounded-2xl p-6` bordered card (`grid md:grid-cols-4`, search
   `md:col-span-2`, expenses `md:grid-cols-2 lg:grid-cols-4`; icon
   `w-5 h-5`, input `pl-10`) — the clone had a bare flex row with
   fixed-width selects.
3. **F3** Classification tiles: reference is a `flex gap-4` row of
   `flex-1 p-4 rounded-lg border-2` tiles with per-classification selected
   colors (need `#e07a3b`/`#fff7f5`, want `#3b7ea1`/`#f0f7fb`, savings
   `#8fbc3f`/`#f5f9f0`) and per-tile hover borders — the clone used a
   3-col grid of p-3 border-1 tiles, uniformly forest-tinted.
4. **F4** Line-item dialog: missing Payment Method field, "End Date" →
   "End / Expiry Date", field order, and — functionally — line items
   carry their OWN status enum (Active/Pending/Cancelled), not the
   budget-item planned/active/completed trio. New `LineItemStatus` type +
   `LINE_ITEM_STATUSES` constant, validation + calculator pill map
   updated.
5. **F5** Login card: the clone's "Continue as guest" link was dead
   (`/dashboard` bounces back to /login) AND absent from the reference —
   removed. Sign-up/forgot states restructured to the reference: a
   left-aligned "← Back to sign in" button at the TOP, an H2 heading, NO
   logo / Google / OR divider, and the reference's forgot-password
   wording.
6. **F6 [documented superset]** The reference marks NO nav item active on
   the root `/` route (its active check compares pathname to
   `/dashboard`). The clone highlights Dashboard there — kept as superset
   fix #3 and documented.

## TDD execution

- NEW `tests/e2e/mobile-layout.spec.ts` (3 specs): no horizontal overflow,
  header stacked inside full-width main at reference geometry, 28px
  panel-left button + text-xl brand.
- `items.spec.ts` +2 specs: the filter card (card/grid/pl-10/w-5/select
  counts) and the classification tiles (group/tile chrome, per-class
  colors, capitalized labels); expenses grid assertions added.
- `calculator.spec.ts` +1 spec: the line-item dialog's exact label order,
  the Payment Method field, and the Active/Pending/Cancelled options
  (planned/completed asserted absent).
- `auth.spec.ts` +1 spec: sign-up/forgot structure (back button first,
  left-aligned, arrow-left; H2; no logo/Google/OR; reference wording; no
  guest link in any state).
- `tests/validation.test.ts` +1: line items accept pending/cancelled and
  reject planned/completed (budget items keep them).
- Implementation: `app-shell.tsx` (sheet state hoisted; top bar inside
  main), `sidebar.tsx` (MobileTopbar extraction + reference chrome),
  `items-view.tsx` (filter card), `budget-item-dialog.tsx` (tiles),
  `line-item-dialog.tsx` (fields/order/enum), `calculator-dialog.tsx`
  (pill map), `login-card.tsx` (GoogleBlock/AuthForm extraction + state
  restructure), `constants.ts` (CLASSIFICATION_TILES +
  LINE_ITEM_STATUSES), `types.ts`, `validation.ts`.

One infra gotcha re-learned: a rebuilt standalone server must actually
replace the old `next-server` process (a stale PID on :3200 kept serving
the previous build's chunk manifest — kill by port/PID, then re-verify
the served markup).

## Verification

- Full chain: typecheck ✓ · lint ✓ · **96/96 unit** ✓ · build ✓ ·
  **46/46 e2e** (39 prior + 7 new) ✓ · **30/30 smoke** ✓.
- Live parity re-verified on the remediated build against the reference:
  mobile layout (header [0,0,390,61] inside main, `scrollWidth` 390),
  filter cards, classification tiles (byte-identical computed styles),
  line-item dialog (identical labels/order/defaults), sign-up state
  (arrow-left back button, H2, no Google/logo) — all matching.
- Both reference mobile-nav bugs re-confirmed still live; the clone's
  superset fixes re-verified end-to-end (hamburger hit-test passes,
  sheet closes on nav).
- All 11 screenshots regenerated (`01`–`10` updated with the new
  surfaces; `09-mobile-dashboard.png` now shows the corrected mobile
  layout).

## Docs alignment

README (test counts 96/46, superset list + mobile-layout pin,
remediation-plan-v3 reference), PAD (13/21 handler count fix), SKILL
(project_state, `LINE_ITEM_STATUSES`, `LineItemStatus`, D-2 wording, new
D-4 row), `worklog.md`, this session log, and `remediation-plan-v3.md`
itself.
