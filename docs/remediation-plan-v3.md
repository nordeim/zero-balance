# Remediation Plan v3 — Session-5 Parity Iteration

Date: 2026-10-07 · Scope: fresh re-audit of every surface against the live
reference (`https://zero-balance-4885a8f3.base44.app/`), desktop 1280×800 +
mobile 390×844, with DOM/computed-style probes on BOTH sites (probe sources
under `scripts/parity-probes/`, `probe-*-v3.mjs` / `probe-view-dump.mjs` /
`probe-donut-nav.mjs`).

Status after the v2 remediation: dashboard (hero/stat cards/donut order +
labels/icons/guidelines/quick actions/breakdown drill-down/Net Balance),
item cards (badge maps, hover buttons), calculator (total card, rows, empty
state), net worth (ratio, type grouping, cards), and both reference mobile-nav
bugs re-confirmed still live — all verified matching. This pass found
**6 new finding groups**, including one critical clone-side mobile layout bug
present since session 1 but invisible to the interaction-focused e2e suite.

---

## Findings ledger

### F1. [CRITICAL — clone bug] Mobile top bar breaks the mobile layout

Evidence (clone, 390×844): `document.documentElement.scrollWidth` = **480**
(90px horizontal overflow); `header` rect `[0,0,222,3466]` — a 222px-wide,
full-page-height column; `main` rect `[222,0,214,3466]` — squeezed to 214px.

Root cause: `AppSidebar` renders the mobile top bar (`<header
class="md:hidden">`) as a React fragment child of `div.flex.min-h-svh.w-full`
(app-shell.tsx). Fragments don't create DOM nodes, so at mobile widths the
`display:block` header becomes a **row-flex item** beside `main`, stretching
to full height (align-items default) and stealing 222px of width.

Reference evidence (390×844): the header lives **inside** `main`
(`main.flex-1.flex.flex-col` → `header` + content), full-width 394px, 61px
tall; `main` takes the full viewport width.

Reference header details (all measured):
- inner row: `flex items-center gap-4` (clone: gap-3)
- toggle button: `h-7 w-7 p-2 rounded-lg hover:bg-green-50 transition-colors
  duration-200` (28×28) with **`lucide-panel-left`** icon at 16px
  (`[&_svg]:size-4`) and an sr-only "Toggle Sidebar" text node (clone: h-9
  w-9 rounded-md hover:bg-accent, lucide-menu icon, aria-label only)
- brand: `<h1 class="text-xl font-bold">` forestDark (clone: text-lg)
- total height 61px = py-4 (32) + 28px button + 1px border

Fix: hoist the sheet-open state to `AppShell`; render the mobile top bar
INSIDE `main` (first child) with the reference's classes/geometry. The
desktop `md:pl-(--sidebar-width)` padding on main is unaffected.

### F2. [HIGH] Items-view filter container is not the reference's card

Evidence (ref, all three items views): search + selects sit inside
`bg-white rounded-2xl p-6 mb-6` + inline `border: 1px solid rgb(229,231,227)`:

- income/savings: `grid md:grid-cols-4 gap-4`, search wrapper
  `md:col-span-2 relative`, 2 selects
- expenses: `grid md:grid-cols-2 lg:grid-cols-4 gap-4`, search + 3 selects
  (All Categories / All Frequencies / All Payment Methods)
- search icon: `absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5` (20px),
  input `pl-10`

Clone today: bare `mb-6 flex flex-col gap-3 md:flex-row`, fixed-width
`md:w-[160px]` selects in their own grid, icon `h-4 w-4`, input `pl-9`.

### F3. [MED] Add/Edit Budget Item — classification tile chrome

Evidence (ref dialog, live clicks through all three tiles):
- group: `flex gap-4` (each tile `flex-1`)
- tile: `flex items-center space-x-2 flex-1 p-4 rounded-lg border-2
  transition-all cursor-pointer` + per-tile hover `hover:border-red-300`
  (need) / `hover:border-blue-300` (want) / `hover:border-green-300` (savings)
- selected tile: border + tinted bg per classification —
  need `#e07a3b`/`#fff7f5`, want `#3b7ea1`/`#f0f7fb`, savings
  `#8fbc3f`/`#f5f9f0`; unselected: default border `rgb(229,231,227)`, white bg
- labels "Need"/"Want"/"Savings" (`text-sm font-medium`)

Clone today: `grid grid-cols-3 gap-3`, tiles `gap-2 rounded-lg border p-3
hover:bg-accent`, selected always forestMedium border + generic cardTint.
(Tints match the GUIDELINE_ROWS values already in constants.ts.)

### F4. [MED] Line Item dialog — missing field, label, order, status enum

Evidence (ref "Add Line Item", opened via calculator → Add First Item,
z-[60] stacked overlay):
- fields: Item Name *, Amount *, Frequency, Provider / Company,
  Policy / Account Number, Start / Renewal Date, **End / Expiry Date**,
  **Payment Method**, Status, Notes (clone: no Payment Method, "End Date",
  Status ordered between Policy and the dates)
- **Status options: Active / Pending / Cancelled** — line items carry their
  OWN enum, distinct from BudgetItem's planned/active/completed (verified in
  the Add Budget Item dialog: Planned/Active/Completed there)
- calculator row pill (v2 bundle evidence): active → green, pending →
  yellow, else gray — "pending" is a real line-item status, not an alias for
  "planned"

Clone today: reuses `ItemStatus` (planned/active/completed) for line items.
The Prisma model already has `paymentMethod` (String?) and the zod schema
already validates it — only the dialog omits the field.

### F5. [MED] Login card — signup/forgot states + dead guest link

Evidence (ref, three states):
- signin: matches the clone (logo, H1 "Welcome to ZeroBudget", subtitle,
  Google, OR, Email/Password, Sign in, Forgot, Sign-up link)
- signup: **"Back to sign in" button at the TOP** (`flex items-center gap-2
  text-sm`), heading is an **H2 `text-xl sm:text-2xl font-bold`**, **no
  subtitle, no Google button, no OR divider**; form = Email / Password /
  Confirm Password / Create account
- forgot: "Back to sign in" at the TOP, heading "Reset your password", desc
  **"Enter your email and we'll send you a link to reset your password"**
  (clone: "…we'll send a reset link"), **no Google, no OR**
- NO guest affordance in any state

Clone today: "Continue as guest" link on every state — a **dead link**
(`/dashboard` is session-gated and bounces back to /login) that also deviates
visually; signup/forgot keep the Google+OR block and put "Back to sign in"
at the bottom.

### F6. [LOW — documented superset, no code change] Root-URL active nav

Reference: after login the URL is `/` and **no nav item renders active**
(its active-state check compares pathname to `/dashboard` and fails on the
root; the gradient DOES apply when the path is exactly `/dashboard` — both
measured today). Clone: renders the dashboard at `/` with Dashboard
highlighted (sensible behavior). KEEP the clone behavior; document as
superset fix #3.

Also re-verified today (no action): donut slice labels (16px, sector-color
fills, `recharts-pie-label-text`), hero overflow-hidden + decorative circle,
avatar, quick-action computed styles, stat-count rows, breakdown drill-down
levels/footers, networth ratio/grouping/footers, Add Asset dialog, sheet
geometry (288px), ref mobile bugs #1/#2 still live.

---

## ToDo (TDD — tests first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | Mobile layout: top bar inside main, reference geometry | NEW `tests/e2e/mobile-layout.spec.ts` | `app-shell.tsx`, `sidebar.tsx` |
| 2 | Items-view filter card (rounded-2xl p-6, grids, pl-10 search, w-5 icon) | `items.spec.ts` | `items-view.tsx` |
| 3 | Classification tiles (flex gap-4, border-2 p-4, per-class colors/tints, capitalized labels) | `items.spec.ts` | `budget-item-dialog.tsx`, `constants.ts` |
| 4 | Line item: Payment Method field, End / Expiry Date label, field order, `LineItemStatus` enum (active/pending/cancelled) + pill map | `calculator.spec.ts` rewrite of dialog assertions; `tests/validation.test.ts` enum cases | `line-item-dialog.tsx`, `calculator-dialog.tsx`, `types.ts`, `validation.ts` |
| 5 | Login card: remove guest link; signup/forgot restructure (back-link top, H2, no Google/OR, ref desc) | `auth.spec.ts` | `login-card.tsx` |
| 6 | Regression: full chain + mobile probes + live parity re-check | — | — |
| 7 | Docs: session_5 log, worklog, README/SKILL alignment; screenshots refresh | — | docs |

## Regression pin map (must NOT change)

- Mobile-nav superset fixes #1/#2 (toast viewport pointer-events, sheet
  close-on-nav) — `mobile-navigation.spec.ts` (7 specs)
- Money two-formatter contract, breakdown drill-down, badge maps, gradients,
  calculator/networth structure — v2 spec suite
- API contracts, seed data, e2e storage-state discipline
