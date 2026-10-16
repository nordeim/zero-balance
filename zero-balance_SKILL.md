---
name: zero-balance
description: >
  ZeroBalance — self-hosted budget planner (Next.js 16 + React 19 + Prisma/SQLite
  + Zustand + Tailwind CSS v4). Superset clone of the ZeroBudget reference app
  with cookie-session auth, integer-cents money math, and a three-tier test
  suite. This skill captures every design decision, anti-pattern, debugging
  procedure, and lesson needed to extend, debug, or replicate the codebase.
version: 1.0.0
last_updated: 2026-10-16

project_state: 108 unit tests / 271 e2e tests / 35 smoke steps — all green
---

# ZeroBalance — Engineering Skill

> **How to use this document:** Read §1–§5 before making any change — they
> define the identity, stack, and layering rules that every contribution must
> respect. When something breaks, start at §10 (Debugging Guide). Before
> shipping, run §11 (Pre-Ship Checklist). Every claim below is verifiable
> against a specific file, command, or test in the repo at
> `github.com/nordeim/zero-balance`.

## Table of Contents

1. [Project Identity & Design Philosophy](#1-project-identity--design-philosophy)
2. [Tech Stack & Environment](#2-tech-stack--environment)
3. [Bootstrapping & Configuration](#3-bootstrapping--configuration)
4. [The Design System (Code-First)](#4-the-design-system-code-first)
5. [Component Architecture & Patterns](#5-component-architecture--patterns)
6. [State Management Deep Dive (Zustand)](#6-state-management-deep-dive-zustand)
7. [Domain Data, Enums & Seed](#7-domain-data-enums--seed)
8. [Accessibility Implementation](#8-accessibility-implementation)
9. [Anti-Patterns & Common Bugs](#9-anti-patterns--common-bugs)
10. [Debugging Guide](#10-debugging-guide)
11. [Pre-Ship Checklist](#11-pre-ship-checklist)
12. [Lessons Learnt & How to Avoid Them](#12-lessons-learnt--how-to-avoid-them)
13. [Pitfalls to Avoid](#13-pitfalls-to-avoid)
14. [Best Practices](#14-best-practices)
15. [Coding Patterns](#15-coding-patterns)
16. [Coding Anti-Patterns](#16-coding-anti-patterns)
17. [Responsive Breakpoint Reference](#17-responsive-breakpoint-reference)
18. [Z-Index Layer Map](#18-z-index-layer-map)
19. [Color Reference (Complete)](#19-color-reference-complete)
20. [The Complete TypeScript Interface Reference](#20-the-complete-typescript-interface-reference)
- [Appendix A: Architecture Decision Records](#appendix-a-adrs)
- [Appendix B: Audit & Session History](#appendix-b-audit--session-history)
- [Appendix C: Live-Site Validation Methodology](#appendix-c-live-site-validation-methodology)
- [Quick Reference Card](#quick-reference-card)

---

## 1. Project Identity & Design Philosophy

**One sentence:** ZeroBalance is a self-hosted personal budget planner built
around the net-zero rule — `Income = Savings + Expenses` — where every budget
item, asset, and liability is tracked in integer cents, aggregated into a
dashboard, and decomposable into line items through a server-recalculating
calculator.

**Two identities in one codebase:**

1. **A real product** — cookie-session auth, per-IP login rate limiting, a
   Prisma/SQLite store, and zod-validated JSON APIs.
2. **A parity superset clone** of the hosted ZeroBudget reference app
   (`zero-balance-4885a8f3.base44.app`): pixel-level visual parity by design,
   plus four reference bugs deliberately fixed — the two mobile-navigation
   bugs (§9 D-1/D-2), the root-URL active-nav gap, and the reference's own
   mobile horizontal overflow (§9 D-5, `docs/remediation-plan-v4.md`).

**Design thesis — "organic fintech calm":** deep forest greens with a lime
accent, warm off-white paper (`#fafaf8`), 135° forest gradient surfaces for
the hero/summary cards, soft 12px-corner cards, and a 256px fixed desktop
rail. The brand reads grounded and botanical, never neon or corporate-blue.

**Non-negotiable design rules:**

- Brand colors come **only** from the `:root` CSS variables / `@theme inline`
  literal hexes (§19). Never a Tailwind default-palette class for brand color.
- Gradient surfaces always use explicit inline
  `linear-gradient(135deg, var(--forest-dark), var(--forest-medium))` styles —
  never `bg-gradient-to-*` utilities (Tailwind v4 oklab trap, §4).
- Money is **integer cents** end-to-end; floats exist only at the format
  boundary (`src/lib/money.ts`).
- Parity decisions are **evidence-based**: computed styles and live hit-tests
  on the reference are the ground truth, never screenshots alone.

**The anti-generic mandate:** no glassmorphism, no purple/indigo gradients, no
rounded-2xl-everything, no drop shadows on drop shadows, no dark mode (the
reference has none — the `dark` custom variant exists only for shadcn
compatibility, §4).

**CTA hierarchy:** primary actions are forest-solid buttons (Add Item, Save,
Sign in); destructive actions are `#bd3228`; tertiary actions are ghost/outline
(plain `Edit` / `Calculate` inline buttons on expense cards).

---

## 2. Tech Stack & Environment

Exact installed versions (`npm list --depth=0`, 2026-10-07):

| Layer | Technology | Version | Critical note |
|-------|------------|---------|---------------|
| Framework | `next` | 16.4.0 | App Router only; standalone output (`next.config.ts`) |
| UI runtime | `react` / `react-dom` | 19.3.0 | `useSyncExternalStore` semantics matter for store selectors (§6) |
| Language | `typescript` | 5.9.3 | `strict: true`, no `ignoreBuildErrors` |
| Styling | `tailwindcss` | 4.3.3 | v4 — five known traps, all mitigated (§4, §9) |
| PostCSS | `@tailwindcss/postcss` | 4.x | via `postcss.config.mjs` |
| ORM | `prisma` / `@prisma/client` | 6.11.1 | relative `file:` URL anchoring rules (§3) |
| Database | SQLite | — | `db/custom.db` at repo root; `db/e2e.db` for e2e |
| Client state | `zustand` | 5.0.15 | v5 — derived-array selectors MUST use `useShallow` (§9 E-1) |
| Validation | `zod` | 4.6.5 | at every API boundary (`src/lib/validation.ts`) |
| Charts | `recharts` | 3.10.1 | donut fills pinned by e2e assertions |
| Icons | `lucide-react` | 0.525.0 | Income=`Receipt`, Net Worth=`TrendingUp` (parity-verified) |
| Dialog/menu primitives | `@radix-ui/react-dialog` etc. | 1.2.0 / 2.3.8 / 1.1.22 / 1.2.24 | shadcn-style wrappers in `src/components/ui/` |
| Unit tests | `vitest` | 5.0.3 | 3 projects: node contract, api (node env), browser api-contract |
| E2E tests | `@playwright/test` | 1.63.0 | desktop + mobile projects; storageState auth sharing |
| Runtime | Node ≥ 20 / bun 1.3.x | — | `bun` runs the standalone prod server in scripts |

**Environment variables** (all three in `.env.example`, count = 3):

| Variable | Purpose | Default behavior |
|----------|---------|-------------------|
| `DATABASE_URL` | SQLite location, `"file:../db/custom.db"` → `<repo>/db/custom.db` | **No default** — must be set |
| `NEXT_PUBLIC_SITE_URL` | Canonical origin for metadata | Falls back to `http://localhost:3000` (`src/app/layout.tsx`) |
| `AUTH_SECRET` | HMAC-SHA256 session signing key | Falls back to an insecure dev constant with a console warning (`src/lib/auth.ts`) — set in production |

**There is no** Tailwind config file (v4 is CSS-first via `globals.css`),
no `tailwind.config.ts`, no `middleware.ts` (auth is enforced per-route by
`require-session` + per-handler `verifySession`), no i18n, no dark mode toggle.

---

## 3. Bootstrapping & Configuration

```bash
git clone https://github.com/nordeim/zero-balance.git && cd zero-balance
npm install
cp .env.example .env          # DATABASE_URL="file:../db/custom.db"
npm run db:push               # prisma db push (env -u discipline, see below)
npm run db:seed               # demo@zerobalance.app / Demo1234!
npm run dev                   # http://localhost:3000 (logs tee'd to dev.log)
```

**The database path discipline (critical):** `db/` lives at the **repo root**.
A relative `file:` URL resolves differently depending on who reads it:

| Reader | Anchor |
|--------|--------|
| Prisma CLI reading `.env` | `prisma/schema.prisma` dir → `<repo>/db/custom.db` ✅ |
| Prisma CLI reading a **shell-inherited** `DATABASE_URL` | process CWD (unpredictable) ⚠️ |
| Runtime server via `src/lib/db-path.ts` | always schema-dir anchored ✅ |

Therefore `package.json` scripts pin the value explicitly:

- Runtime scripts inline it: `DATABASE_URL=file:../db/custom.db next dev …`
- Prisma CLI scripts strip the environment first: `env -u DATABASE_URL prisma db push …`

so a polluted parent shell can never redirect the database. The contract is
pinned by `tests/db-path.test.ts` (15 tests). Never run a bare `prisma db push`
in a shell whose `DATABASE_URL` may be inherited.

**Key configuration files:**

| File | Role |
|------|------|
| `next.config.ts` | `output: "standalone"`, `allowedDevOrigins` fix, no rewrites, no ignoreBuildErrors |
| `tsconfig.json` | strict TS, `@/*` → `src/*` path alias |
| `eslint.config.mjs` | eslint 9 flat config + eslint-config-next (react-hooks v6 rules active — see §9 G-6) |
| `vitest.config.ts` | 3 projects (node / api node-env / browser api-contract) |
| `playwright.config.ts` | desktop + mobile(390×844) projects, authenticated via `storageState`, `db/e2e.db`, webServer = standalone build on :3100 |
| `postcss.config.mjs` | `@tailwindcss/postcss` |
| `prisma/schema.prisma` | 5 models, provider sqlite |

**Verification that bootstrap worked:** `npm run typecheck && npm test` (108
tests), then `npm run build && npm run test:e2e` (271 tests), then
`bash scripts/smoke-test.sh` (35 steps on :3210).

---

## 4. The Design System (Code-First)

All tokens live in `src/app/globals.css`. The `@theme inline` block uses
**literal hex values only** — under Tailwind v4 a bare HSL triplet like
`0 0% 100%` silently resolves to transparent (trap 1), and v4's default
palette is oklch, which drifts 1–3 sRGB units per channel from the reference
hexes (trap 2).

**Brand palette** (`:root` variables — the source of truth):

| Token | Hex | Usage |
|-------|-----|-------|
| `--forest-dark` | `#1a3a2e` | primary buttons, active nav, hero gradient start, `--color-primary` |
| `--forest-medium` | `#2d5a4a` | hero gradient end, summary-card gradient end |
| `--lime-green` | `#8fbc3f` | savings accent, donut Savings fill, net-zero highlights |
| `--lime-light` | `#b8d87e` | lime tint (active-nav gradient end, hover states) |
| `--orange-dark` | `#e07a3b` | donut Need fill, warning/over-budget accents |
| `--orange-light` | `#f5a962` | orange tint |
| `--blue-dark` | `#2c5f7c` | deep blue accent |
| `--blue-medium` | `#3b7ea1` | donut Want fill, savings-view accent |
| `--neutral-warm` | `#fafaf8` | app background (`--color-background`) |

**Semantic tokens** (`@theme inline`, all literal hex): background
`#fafaf8`, foreground `#3f3f3f`, card/popover `#ffffff`, primary `#1a3a2e`,
secondary/muted `#f4f4f5`, muted-foreground `#737373`, accent `#f0f2ee`,
destructive `#bd3228`, border/input `#e5e7e3`, ring `#1a3a2e`, sidebar
`#fafafa`. Full table in §19.

**Typography:** the system stack — `ui-sans-serif, system-ui, sans-serif,
"Apple Color Emoji", …` (parity: the reference uses no webfont). Weights:
400 body, 500/600 headings and emphasis; hero money figures ~30px semibold;
uppercase + tracking-wide eyebrow labels ("NET ZERO GOAL", "NAVIGATION").

**Radius:** `--radius` base with `calc()` offsets — `--radius-sm: -4px`,
`--radius-md: -2px`, `--radius-lg: base`, `--radius-xl: +4px`. Cards are
`rounded-lg` family; the login logo chip is `rounded-full`.

**Shadows:** `--shadow-sm` is **pinned to the reference geometry** — v4 moved
the scale one notch heavier (trap 5), so the pin restores reference elevation.

**Gradients:** always inline style, e.g. the hero card:
`style={{ background: "linear-gradient(135deg, var(--forest-dark), var(--forest-medium))" }}`
— oklab interpolation in v4 gradient utilities visibly shifts brand blends (trap 3).

**Spacing discipline:** no `mt-*`/`mb-*` on children of `space-y-*`
containers (v4 rewrote the `space-y` selector, trap 4) — apply spacing on the
child's own margin or restructure.

**Sidebar geometry:** `--sidebar-width: 16rem` (256px desktop rail),
`--sidebar-width-icon: 3rem`; the **mobile sheet is 18rem (288px)** and
left-anchored — measured on the reference, pinned by e2e.

---

## 5. Component Architecture & Patterns

**Layer model** (imports flow downward only):

```
src/app/**            routes: thin pages, each wrapping views in <AppShell> (client)
src/app/api/**        route handlers: verifySession → zod → service → JSON envelope
src/components/budget feature components + the Zustand store (client)
src/components/ui     shadcn-style primitives (Radix wrappers, client)
src/lib               pure domain + infra (money, dashboard math, validation, auth, db)
prisma/               schema + seed
```

**Counts** (2026-10-07): 61 TS/TSX files under `src/`; 28 files carry
`"use client"`; `src/components/budget/` = 14 files; `src/components/ui/` =
12 files; `src/lib/` = 14 files; API = 13 `route.ts` files (21 handler
functions — collection + item routes for 5 resources + auth×4 + health).

**Client/server split rule:** every page (`/`, `/dashboard`, `/income`,
`/expenses`, `/savings`, `/networth`, `/login`) is a **server component**
that renders `<AppShell>` (client) → `RequireSession` gates the session
server-side via `/api/auth/me` + children only when authenticated; views
hydrate from the store's `boot()`. No route fetches domain data at the RSC
layer — data flows through the client store over the JSON API (Base44
reference parity).

**The dialog mount pattern (lazy initializers).** `ModalHost` inside
`AppShell` conditionally mounts dialogs from `modal` state. Because a
conditional mount means `useState(initializer)` runs **after** the modal key
is already set, every dialog initializes its form lazily and resets on
modal-identity change during render:

```tsx
// budget-item-dialog.tsx (pattern; all four dialogs share it)
const [form, setForm] = useState(() => initialForm(modal));
const [prevKey, setPrevKey] = useState(modalKey(modal));
if (prevKey !== modalKey(modal)) {          // adjust-during-render (React idiom)
  setPrevKey(modalKey(modal));
  setForm(initialForm(modal));
}
```

This replaced an effect-based reset (eslint react-hooks v6
`set-state-in-effect` violation, and racy in production hydration).

**The queries boundary:** the browser never calls `fetch` directly —
`src/lib/api.ts` wraps every endpoint, throws `ApiError` with the server's
message, and the store maps it to toasts.

**Icons (parity-pinned):** sidebar = `LayoutDashboardIcon` (Dashboard),
`WalletIcon` (Income), `ReceiptIcon` (Expenses — **not** ReceiptText),
`PigBankIcon` (Savings), `TrendingUpIcon` (Net Worth); avatar fallback is the
letter "U" for the demo user. Do not change without re-verifying the live
reference.

---

## 6. State Management Deep Dive (Zustand)

One store: `src/components/budget/store.ts` — `useBudgetStore` (created with
`create<BudgetStore>`). It caches the session user, all budget items, assets,
liabilities, line items keyed by parent, and the modal state machine.

**Lifecycle:**

- `boot()` — called once by `AppShell` on mount: fetches `/api/auth/me`,
  items, assets, liabilities in parallel; sets `booted: true`.
- `refresh()` — re-fetches items/assets/liabilities after mutations.
- `login/register/logout` — auth flows; login also boots.

**The selector rule (the single most important perf invariant in the repo):**

```tsx
// ❌ FORBIDDEN — new array every snapshot → infinite re-render (React #185)
const items = useBudgetStore((s) => s.items.filter((i) => i.type === "expense"));

// ✅ REQUIRED — shallow-compares the derived array
import { useShallow } from "zustand/react/shallow";
const items = useBudgetStore(useShallow((s) => s.items.filter((i) => i.type === "expense")));

// ✅ Also fine — stable slice references (no derivation)
const items = useBudgetStore((s) => s.items);
```

With zustand v5 + React 19's `useSyncExternalStore`, a selector returning a
fresh object/array every call fails snapshot equality forever → Maximum update
depth exceeded. This crashed all three item views in production while looking
fine on the dev server (§9 E-1). `tests/e2e/items.spec.ts` pins the fix by
running against the production build.

**The modal state machine** (`ModalState`): five slots — `item`, `calculator`,
`lineItem`, `asset`, `liability` — each a discriminated union of
create/edit/null. One `closeModals()` clears everything **except** the scoped
`closeLineItemModal()`, which clears only `modal.lineItem`. Rationale
(reference behavior): saving a line item must keep the calculator open showing
the server-recalculated total banner. Deleting that scoped close regresses
`tests/e2e/calculator.spec.ts`.

**Mutation flow:** every CRUD action calls `src/lib/api.ts`, then refreshes
the affected slice (items reload on item mutations; line-item mutations
reload that parent's line items **and** the parent item, because the server
recalculates the parent's amount — see §7).

---

## 7. Domain Data, Enums & Seed

**Enums** (`src/lib/constants.ts`, all `as const` arrays with derived union
types — the single source for dropdowns, badges, and validation):

| Constant | Values |
|----------|--------|
| `ITEM_TYPES` | `income`, `savings`, `expense` |
| `CLASSIFICATIONS` | `need`, `want`, `savings` |
| `FREQUENCIES` | `one-time`, `weekly`, `bi-weekly`, `monthly`, `quarterly`, `annually` |
| `ITEM_STATUSES` | `planned`, `active`, `completed` (budget items) |
| `LINE_ITEM_STATUSES` | `active`, `pending`, `cancelled` (calculator line items — their OWN enum, per the reference's Add Line Item form) |
| `ASSET_TYPES` / `ASSET_LABELS` | `bank_account`, `superannuation`, `property`, `investment`, `vehicle`, `other` → "Bank Account", "Superannuation", … |
| `LIABILITY_TYPES` / `LIABILITY_LABELS` | `home_loan`, `personal_loan`, `credit_card`, `car_loan`, `student_loan`, `other` → "Home Loan", … |
| `COLORS` | the measured reference palette (§19) |

Adding a value: touch `constants.ts` (array + label map) → the dropdowns,
badges, and zod schemas pick it up automatically (validation imports the same
arrays). That's the whole procedure — do not fork enum copies into components.

**Prisma models** (`prisma/schema.prisma`):

- `User` — id, email (unique), name?, passwordHash; relations to everything.
- `BudgetItem` — userId, type (ItemType), name, description?, amount (Int,
  cents), category, classification, frequency, status, paymentMethod?, dueDay?,
  nextDueDate?; `@@index([userId, type])`, `@@index([userId, createdAt])`.
- `ExpenseLineItem` — budgetItemId + userId, name, amount (cents), frequency,
  provider?, policyNumber?, startDate?/endDate?; `@@index` on both FKs.
- `Asset` / `Liability` — userId, name, type, amount (cents), institution?,
  notes?; `@@index([userId])`.

**The calculator contract (core domain rule):** expense categories decompose
into line items, and **every line-item mutation triggers a server-side
recalculation of the parent BudgetItem's amount** (sum of line items, integer
cents) inside `src/lib/line-item-service.ts` — there is no Save button; the
calculator banner shows "Total Calculated $X / Based on N items · Will update
category total" and mutations persist immediately. Pinned by
`tests/e2e/calculator.spec.ts` and `tests/line-item-service.test.ts`.

**Seed** (`prisma/seed.ts`): demo user `demo@zerobalance.app` / `Demo1234!`;
income $5,550 (2 items), expenses $2,235 (3), savings $1,250 (2) — dashboard
shows 62.8% allocation, `+$2,065.00` net; assets $65,300 / liabilities
$311,250 → net −$245,950.00, ratio "0.21:1". These figures are load-bearing:
`tests/e2e/dashboard.spec.ts` and `networth.spec.ts` assert them, so changing
the seed means updating those specs in the same commit.

---

## 8. Accessibility Implementation

- **Radix primitives everywhere** (`src/components/ui/`): dialogs expose
  `role="dialog"` + `aria-modal`, selects expose `role="combobox"` with
  `role="option"` children, tabs/dropdown/radio-group keep their native ARIA
  trees. E2E locators rely on these roles — removing them breaks the suite
  before it breaks users.
- **Labeling conventions (parity + a11y):** hamburger → `aria-label="Toggle
  Sidebar"`; card action menus → `aria-label="Actions for {name}"`;
  `aria-label="Delete {name}"` for line-item delete rows. Inline Edit/
  Calculate buttons intentionally have **no** aria-label — the reference
  exposes their visible text as the accessible name.
- **Forms:** every input has a `<Label>` (`src/components/ui/label.tsx`);
  validation errors render as text below fields and as toasts.
- **Focus:** ring token `--color-ring: #1a3a2e`; dialogs trap focus (Radix),
  return it on close, and close on Escape + overlay tap.
- **Keyboard paths (tested):** Escape closes the mobile sheet and dialogs;
  Enter submits dialog forms (native `<form>` submit buttons); all controls
  are real buttons/inputs — no click-divs.
- **Motion:** animations are short slide/fade transitions; exit animations
  ~200–300ms — UI **stays in the DOM** during exit. Any automation asserting
  "closed" must settle-wait first (§12 L7).

---

## 9. Anti-Patterns & Common Bugs

Historical bugs — each fixed and pinned. Severity = recurrence blast radius.

| ID | Anti-pattern | Symptom | Root cause | Fix (file) | Pinned by | Severity |
|----|--------------|---------|------------|------------|-----------|----------|
| E-1 | Derived store selector without `useShallow` | Production crash "Maximum update depth exceeded" (React #185) on /income /expenses /savings | Fresh array per snapshot never passes `useSyncExternalStore` equality | `useShallow` wrap (`items-view.tsx`) | items e2e vs prod build | Critical |
| E-2 | Modal panel without positioning | Dialog visible but every click swallowed by the overlay | Static panel under a `z-50` fixed overlay | Fixed + centered `.zb-modal-panel` (`globals.css`, `dialog.tsx`) | every dialog e2e | Critical |
| E-3 | Sticky dialog header over the Close button | Close (×) unclickable | Header `z-10` stacks over `z-auto` close | Close raised to `z-20` (`dialog.tsx`) | calculator e2e | High |
| E-4 | `isoDate().optional()` for optional date inputs | Save returns 400; dialog stuck open | HTML forms submit `""`; `Date.parse` rolls over impossible dates | `optionalIsoDate` preprocessor (`""`→undefined) + components round-trip check (`validation.ts`) | `tests/validation.test.ts` | High |
| E-5 | One `closeModals()` for nested dialogs | Saving a line item closes the calculator | Shared close clears all modal slots | Scoped `closeLineItemModal` (`store.ts`) | calculator e2e | Medium |
| E-6 | Effect-based form reset in conditionally-mounted dialogs | Quick-action preselect (type=income) lost | Reset ran before mount / never on identity change | Lazy initializers + adjust-during-render reset (all 4 dialogs) | dashboard e2e | Medium |
| D-1 | Toast viewport with `pointer-events: auto` (reference bug) | Hamburger hit-test fails on mobile | Empty fixed container overlays the button | Viewport `pointer-events: none`; toasts restore it (`globals.css` §toast, `toast.tsx`) | mobile-nav e2e #2 | High |
| D-2 | Mobile sheet stays open after nav (reference bug) | User taps a link, page changes behind the stuck sheet | Sheet close never wired to link clicks | Nav links call `onNavOpenChange(false)`; pathname change closes too (`sidebar.tsx`) | mobile-nav e2e #4 | High |
| D-3 | Sheet `h-full` under mobile emulation | Sheet measures 1044px on a 844px viewport | `%` height resolves against the *layout* viewport (collapsed-URL bars) | `h-svh` (`dialog.tsx`, matches reference rail) | mobile-nav e2e #3 | Medium |
| D-4 | Mobile top bar rendered as a row-flex SIBLING of `<main>` (session-1..4 bug, found session 5) | 390px viewport: 222px column squeezes main to 214px; `scrollWidth` 480 | React fragment child of `div.flex` becomes a flex item; `md:hidden` only hides it ≥768px | Top bar lives INSIDE `<main>` (reference structure), state hoisted to `AppShell` (`app-shell.tsx`/`sidebar.tsx`) | mobile-layout e2e | Critical |
| D-5 | `flex-1` item's automatic minimum size (min-width:auto) stretches the page past the viewport (reference bug R3/R4: its own dashboard scrolls 5px, net-worth 74px; the clone had a 38px net-worth case) | `document.documentElement.scrollWidth` > `clientWidth` on mobile; hiding an inner row shrinks it back | An unbreakable string (long currency figure) inside a flex row sets the min-content width of every block ancestor up to the flex item | `min-w-0` on `<main>` (`app-shell.tsx`) + responsive figures (`text-2xl sm:text-5xl`, `break-words`, `min-w-0` on the text block — `net-worth-view.tsx`). NOTE: `overflow-wrap: break-word` does NOT reduce min-content (only `anywhere` does) | networth e2e (mobile overflow spec) | High |
| D-6 | Tailwind v4 media-gates `hover:` variants behind `@media (hover: hover)` — hover tints vanish on `hover: none` devices (the reference's v3 engine applies `:hover` everywhere) | Nav hover computes `rgba(0,0,0,0)` in a `hover: none` session while the reference shows its tint | v4 compiles `hover:` utilities inside a media query; v3 emitted plain `:hover` | `@variant hover (&:hover);` right after the `@import`s (`globals.css`) — restores v3 semantics | mobile-nav e2e (hover:none emulation spec) | Medium |
| D-7 | Prerendered item-view pages carry the empty-store state: the header AND empty-state "Add …" buttons coexist until hydration + boot fetch | `getByRole('button', { name: 'Add Income' })` strict-mode violation resolving 2 elements on a freshly-seeded run | Static prerender happens at build time with `items: []`; the fetched state replaces the empty state only after hydration | Wait for a seeded card heading before clicking "Add …" by role (the dialog-buttons spec settle pattern) | dialog-buttons e2e | Medium |
| D-8 | v4 named palette utilities emit `lab()`/`oklab()` computed colors (text-red-600, bg-green-50, text-white/70…) while the reference emits plain rgb/rgba | Computed-style probes show `lab(...)` where the reference shows `rgb(...)` — visually identical, computed-different | v4 stores the default palette in oklch/Lab; named utilities reference it | Arbitrary hex classes (`text-[#dc2626]`, `hover:bg-[#f0fdf4]`) or inline rgba on parity surfaces | tokens e2e + dialog-buttons e2e | Low |
| D-9 | The agent sandbox REAPS every background process at command exit (setsid/nohup/disown all die); the standalone server also CRASHES under `node` on the first API request in this environment | A detached `:3200` parity server is gone by the next command; `node .next/standalone/server.js` boots then dies on login POST (no log output) | Process-tree kill between shell invocations; Prisma engine vs node runtime mismatch | Boot per-command via `scripts/parity-probes/with-server.sh` (bun + health wait + teardown); pure DOM probes need no server once the page is loaded | with-server.sh + parity probes | Medium |
| D-10 | e2e fixture restores that re-create rows via the API flip the display order when a view orders by `createdAt` DESC | Re-created liabilities re-appear in reversed type-group order; downstream specs asserting the order fail (they pass in isolation) | POST re-stamps `createdAt` at restore time; GET orders DESC so the newest-first capture order inverts | Re-create in REVERSE capture order (empty-states spec), or assert order-agnostically | empty-states e2e | Medium |
| G-1 | Shared e2e DB without reset | Seed-dependent assertions fail after any earlier failure | Failed runs leave mutated rows | `global-setup.ts` resets `db/e2e.db` every run; specs clean up | consecutive full-suite runs | High |
| G-4 | Smoke test on a shared port | Requests served by a stale dev server | Orphan process holds :3000 | Dedicated port 3210 + orphan kill (`smoke-test.sh`) | smoke run | Medium |

**Framework gotchas seen here:** React #185 (above); Radix exit animations keep
nodes mounted; Playwright strict mode fails on duplicate text (scope locators
to the dialog/card); recharts normalizes hex fills to `rgb()` in computed
style (assert accordingly).

---

## 10. Debugging Guide

| Symptom / error | Cause | Fix |
|-----------------|-------|-----|
| `Maximum update depth exceeded` (React #185) | Derived array/object from a zustand selector (E-1) | `useShallow` the selector; audit any `s => s.x.filter/map({...})` |
| Prisma `Error code 14` (can't open db) / db created in the wrong folder | Relative `file:` URL anchored to CWD by a shell-inherited `DATABASE_URL` | Use npm scripts (pinned/`env -u`); never bare `prisma` commands from a polluted shell (§3) |
| Dialog opens but is dead (no clicks register) | Panel under the overlay (E-2) or another layer over the target (E-3) | Check `.zb-modal-panel` positioning + close button `z-20`; use `document.elementFromPoint` in devtools |
| Line-item save → 400, dialog stays open | Empty-string optional dates (E-4) | `optionalIsoDate` preprocessor; check zod error in the response body |
| Calculator disappears after adding a line item | Shared modal close (E-5) | Use `closeLineItemModal` |
| e2e passes alone, fails in the full run | DB pollution from an earlier spec (G-1/G-2) | Global setup resets e2e.db; your spec must clean up its fixtures |
| e2e "element is not visible/clickable" right after close | Radix exit animation still mounted | `await page.waitForTimeout(300)` or assert disappearance with auto-waiting locator |
| Login suddenly 429 in tests/scripts | Rate limiter (10 / 15 min / IP) counted earlier attempts (G-5) | Count your attempts; share auth via `storageState`; restart the server process to clear the in-memory bucket |
| Radix Select "click does nothing" in a test | Re-render race right after another interaction (G-6) | Settle-wait ~150ms between radio check and select open |
| Sheet measures taller than the viewport under emulation | `100%` height vs layout viewport (D-3) | `h-svh` |
| Donut fill assertion fails though colors look right | Computed style returns `rgb(224, 122, 59)` not `#e07a3b` | Assert the `rgb()` form or compare via `element.getAttribute('fill')` |
| Tailwind class renders transparent/invisible | Bare HSL triplet in `@theme` (trap 1) | Use literal hex tokens (§4) |
| Color subtly off vs reference | oklch default palette drift (trap 2) or oklab gradient (trap 3) | Pin hexes; inline-style gradients |
| `tsc` passes but a component misbehaves in prod only | Prod build exercises hydration paths dev skips (e.g. E-1) | Always run `npm run build && npm run test:e2e` before shipping |

---

## 11. Pre-Ship Checklist

```bash
npm run typecheck        # 0 errors
npm run lint             # 0 errors (eslint 9 + react-hooks v6)
npm test                 # 108/108
npm run build            # standalone build must succeed
npm run test:e2e         # 265/265 (build first!)
bash scripts/smoke-test.sh   # 35/35 on :3210
```

Then the manual/visual pass:

- [ ] Desktop: sidebar 256px fixed; hero gradient `linear-gradient(135deg,
      rgb(26,58,46), rgb(45,90,74))`; donut fills orange/blue/lime.
- [ ] Mobile 390×844: hamburger hit-test passes with the toast container
      present; sheet 288px @ x=0; nav tap navigates **and** closes; Escape
      and overlay tap close.
- [ ] Dialogs: open each of the five; every field editable; Close (×), Save,
      Escape all work; inline delete confirms inline.
- [ ] Calculator: add + delete a line item → parent card amount updates
      server-side with no Save button.
- [ ] Auth: wrong password shows "Invalid email or password"; logout blocks
      the API (401); 11th login attempt in 15 min → 429.
- [ ] No stray `console.log`, no `any`, no TODO/FIXME left in the diff.

---

## 12. Lessons Learnt & How to Avoid Them

Numbered institutional lessons. Each traces to a concrete fix in
`docs/remediation-plan.md`.

1. **The dev server lies about production hydration.** E-1 crashed only in
   the standalone build. → Always gate shipping on `npm run build && npm run
   test:e2e`, never dev-server eyeballing alone.
2. **A zustand selector that allocates is an infinite loop waiting to
   happen.** Any `filter/map/({...})` in a selector must be `useShallow`-wrapped
   (§6). Grep for `useBudgetStore((` and audit on every review.
3. **Prisma's relative `file:` URL has two personalities.** `.env`-sourced →
   schema-dir anchored; shell-inherited → CWD anchored. Scripts pin or strip
   the variable (§3). This cost a whole debugging session to isolate —
   the tests in `db-path.test.ts` now encode the answer.
4. **The environment can poison you.** An absolute `DATABASE_URL` exported by
   a parent shell silently redirected every CLI invocation. When tooling
   behaves nonsensically, dump `env | grep DATABASE` before touching code.
5. **The reference has bugs too — verify before you copy.** Both reference
   mobile-nav bugs (D-1, D-2) would have been faithfully cloned by a naive
   parity pass. Clone *measured geometry and content*, not *broken behavior*;
   document every deliberate divergence as a superset fix.
6. **Computed styles are the ground truth for parity.** Screenshots deceive
   (color profiles, scaling); `getComputedStyle` + `getBoundingClientRect` +
   `elementFromPoint` hit-tests don't. The e2e suite asserts computed values
   (`rgb()` forms, pixel widths) instead of pixels-in-screenshots.
7. **Radix exit animations keep nodes mounted ~300ms.** Assertions made
   immediately after a close see a "still open" DOM. Settle-wait or use
   auto-waiting disappearance locators (§10).
8. **Shared mutable e2e state is a time bomb.** One failing calculator spec
   poisoned every later seed-dependent assertion until the global setup began
   resetting `db/e2e.db` per run and specs learned to clean up (G-1/G-2).
9. **Rate limiters count *your* tests.** 10 attempts / 15 min / IP is generous
   for humans and starvation for scripts. The setup project authenticates
   once and shares `storageState`; the smoke script accounts for its own
   attempts (G-5).
10. **Inline-style gradients are engine-independent; utility gradients are
    not.** v4's oklab interpolation changed brand blends; the literal
    `linear-gradient(135deg, …)` style survives any engine (trap 3).
11. **zod `.optional()` does not mean "accepts empty string."** HTML forms
    submit `""` for untouched inputs — preprocess optional fields at the
    boundary (E-4), and round-trip calendar dates to reject rollovers like
    2026-02-30.
12. **Conditional mount defeats effect-based resets.** When `ModalHost`
    mounts a dialog only when needed, a `useEffect` reset runs after the
    initial render you wanted to intercept. Lazy initializers +
    adjust-during-render (§5) are the React-idiomatic fix and satisfy
    react-hooks v6.
13. **Never slice a computed `boxShadow`/`backgroundImage` when probing.**
    A 60-char `.slice()` read the transparent ring-offset layers of the
    login logo's shadow and filed a "missing ring" finding that was really
    a truncation artifact (plan v7 G3's correction). Always dump the FULL
    computed string (or assert with `toContain`) before declaring a drift.
14. **An inline `boxShadow` overrides every shadow utility on the element.**
    To add a ring WITHOUT losing `shadow-lg`/`group-hover:shadow-xl`, put
    the ring on a sibling layer (`.zb-logo-ring`) — inline style always
    wins the cascade against utility classes.
15. **Flex-squeeze: a fixed-height padded button shrinks its svg.** A 28px
    `h-7 w-7 p-2` toggle box leaves 12px of content width; a 16px icon
    silently compresses unless it carries `shrink-0` (the reference ships
    `[&_svg]:size-4 [&_svg]:shrink-0` for exactly this — plan v7 G5).
16. **A visual match is not a computed-style match — and the drift is
    systematic.** The v4 named palette (zinc/slate/purple/red/green/orange…)
    computes EVERY entry in Lab space: `lab(97.16 3 -4.13)` renders the same
    pixels as `rgb(250,245,255)` in modern Chromium but drifts on
    non-color-managed engines and breaks entirely on browsers without Lab
    support. The v5/v7/v8 passes each found a new family of these; the rule
    is absolute: NO named palette class on a parity surface — arbitrary hex
    only (`text-[#3f3f46]`, `bg-[#faf5ff]`).
17. **Content-sized dialog buttons vs flex-1: the footer is part of the
    dialog's visual identity.** Every reference form dialog splits its
    footer as `flex gap-3 pt-4` with both buttons at `flex-1` (~306px each,
    halves of the 624px content row). A `justify-end` row of content-sized
    buttons reads instantly as "almost right"; measure button WIDTHS, not
    just colors/heights, when auditing dialogs.
18. **Reference data changes under you — re-measure conditional chrome.**
    The Recurring card badge looked like a clone-only extra until the
    reference's own items turned out to ship `recurring: false` (its live
    data changed since the v2 recon measured badge maps). Flip the
    reference's own switch, observe its conditional render, restore the
    mutation, THEN classify the difference as data vs structure.
19. **Reference data changes under you — re-derive the RENDER CONVENTION
    too.** The v2-era "[Savings, Want, Need] sector order" pin was really
    the reference's value-DESC sort wearing that era's data (its $6025
    slice was Savings-classified then, Need now). When a pinned ORDER
    depends on data magnitudes, re-measure with fresh data and derive the
    underlying convention (sort? anchor?) before re-pinning (plan v9 G1).
20. **v4 rewrote `space-y-*` semantics — the margin MOVED.** v3 put
    margin-top on following siblings; v4 puts margin-block-end on
    `:not(:last-child)`. Equivalent for block children (sibling collapse),
    but with an INLINE first child (the reference's shadcn-v1 labels) the
    v4 margin is layout-IGNORED (vertical margins on inline boxes don't
    affect flow) and the gap collapses. Pin the v3 selector in
    `globals.css` when parity depends on it (plan v9 G3).
21. **Transitions race computed-style reads.** A `transition-colors` switch
    flips `aria-checked` instantly but ANIMATES its background — an
    immediate `getComputedStyle` returns the pre-flip value. Poll
    (`expect.poll`) or settle-wait before asserting transitioned values
    (plan v9's switch spec).
22. **`rounded-full` computes as `calc(infinity * 1px)` in v4.** The
    reference's v3 build emits a plain `9999px` — visually identical,
    computed-style different, exactly the lab() color story in one
    dimension over. The same doctrine applies: pin `rounded-[9999px]` on
    parity surfaces (plan v9 G6).
23. **The shadcn `--primary` token is app-brand in this codebase but
    shadcn-neutral in the reference.** The clone's `--color-primary` is
    deliberately forest `#1a3a2e`; the reference's is shadcn's `#171717`.
    Primitives that ride `border-primary`/`bg-primary` (radio circles,
    switch tracks) therefore drift forest-vs-black — hex-pin the primitive
    chrome instead of routing it through the brand token (plan v9 G5).
24. **Never suppress a parity surface on an unmeasured assumption.** The
    mobile sheet shipped `highlightActive={false}` from session 1 — a
    guess that the reference's sheet didn't highlight — and survived eight
    audit passes because none of them measured the sheet's ACTIVE state
    (only its geometry, links, chrome, and close behavior). Measured live
    at `/income`: the reference's sheet renders the current route in the
    FULL active style (135deg forest gradient + white + 500), identical to
    its rail. The fix was one prop; the lesson is to sweep EVERY state
    dimension of a task-focus surface — active/inactive included — before
    assuming a component-level divergence (plan v10 G1).
25. **Computed multi-layer strings hide their payload at the END.** The
    reference's dialog panel reads `rgba(0,0,0,0) 0 0 0 0, rgba(0,0,0,0)
    0 0 0 0, rgba(0,0,0,0.25) 0 25px 50px -12px` — two transparent lead
    layers with the visible shadow LAST. A probe that `.slice()`d the
    computed `box-shadow` at 70 chars reported "shadowless panel" and
    nearly shipped a bogus fix; reading the string in full showed the
    clone was byte-identical. The same trailing-transparent pattern
    appears on focus rings (shadcn's white zero-spread inner layer) and
    the sheet's shadow-lg. Never truncate computed `box-shadow`,
    `transition`, or `outline` strings when diffing two sites — compare
    them whole (plan v11 observations).
26. **A "detail" nobody measured is still drift.** Three v11 findings were
    session-1 defaults that no later pass questioned: the empty-state
    heading's font size (`text-lg` vs the reference's 20px — v6 pinned
    mb/desc/icon but not the size), the gradient buttons' hover fade
    (`opacity: 0.9` vs the reference's no-change — hover state was never
    measured on ANY button until v11), and the Plus icon 20px on Add
    buttons (16px on the reference — every button GEOMETRY was pinned
    but never the icon inside). The audit checklist now sweeps per-
    component: rest state, hover state, focus-visible state, icon
    sizes, ambient shadows, AND every state dimension of the surface's
    children — not just the container (plan v11 G1–G4).
27. **A client-side `document.title` effect LOSES to React Float.** The
    v12 route-title fix was first attempted as a `usePathname()`-driven
    `document.title` effect in the AppShell — it ran (260ms, title set)
    and was silently reset 24ms later when React's Float layer
    re-emitted the static `<title>` from the RSC flight payload during
    hydration recovery. The failing artifact: an e2e title assertion
    that passed on one route and failed on the next (the reset landed
    between the two samples). The correct Next.js mechanism for ANY
    per-route head value is route-segment metadata — a server
    `layout.tsx` exporting `title` + the root layout's template — the
    value ships in the prerendered HTML and the Float re-emission is
    idempotent. Diagnosed with an in-page 20ms `setInterval` title
    poller installed via `addInitScript` (MutationObserver wiring
    never attached — init scripts run before the parser builds
    `<head>`) (plan v12 G2).
28. **Error states are parity surfaces too.** The v12 login audit found
    the clone rendering auth errors as bare red text while the
    reference renders a bordered red-tinted banner (the shadcn
    FormMessage pattern) — the THIRD surface family (after rest and
    open states) that audits must sweep: the ERROR/edge state of every
    form (wrong password, validation mismatch, network failure) and
    the POST-SUBMIT state (the forgot flow's confirmation view —
    layout reproduced, honest copy kept). The clone's honest-copy
    decision pattern: match the reference's LAYOUT geometry exactly,
    diverge only on TEXT where lying to the user would be required
    (plan v12 G1/G4).
29. **A color-only `ring-[…]` utility emits NO box-shadow in v4.** The
    v13 login audit found the clone's inputs carrying
    `focus:ring-[#94a3b8]` with no ring-width class — v4 renders
    nothing (the color var is set, but no shadow layer references it),
    so the inputs swapped border color on focus and had NO ring while
    the reference rendered the two-layer shadcn v1 ring (white 2px
    offset + slate-400 4px) on plain `:focus`. Pin focus rings as
    arbitrary box-shadows (`focus:shadow-[0_0_0_2px_#fff,0_0_0_4px_#94a3b8]`)
    — engine-independent, byte-comparable. And read transitioned
    computed styles only after a settle (the border color animates
    through `transition-colors`; the shadow does not) (plan v13 G3).
30. **Error TEXT and the reachable STATE are parity surfaces.** The
    v13 audit read the reference's register 409 banner and found a
    one-word drift ("A user with this email already exists" vs the
    clone's "An account with…") — API error STRINGS must match the
    reference exactly unless honesty forces a divergence. Same pass:
    the reference's trapped mobile sheet re-renders its active link
    with dark `#18181b` text while its fresh-opened sheet renders the
    pinned white — always determine WHICH of the reference's internal
    states the clone can actually reach before pinning the style (the
    clone's sheet closes on nav, so the trapped state is unreachable
    by design) (plan v13 G1 + the trapped-sheet observation).
31. **Library MAJOR-VERSION defaults are parity surfaces.** The v14
    audit hovered the donut and found recharts 3's default tooltip
    drifting from the reference's recharts-2 chrome on FOUR axes at
    once (raw value, `#cccccc` border, no radius/shadow, sector-colored
    item text) — a surface both sides render "by default" but with
    different defaults. When the reference ships a library default,
    pin it explicitly (`formatter` + `contentStyle` + `itemStyle`)
    — never assume "default == default" across a major version. And
    test the HOVER/interaction states of chart primitives, not just
    their painted geometry (plan v14 G1).
32. **A mouse-following tooltip breaks Playwright's `.hover()`** — the
    tooltip appears under the cursor, re-triggers pointer events, and
    the actionability loop never settles (45s timeout). Dispatch the
    sector's `mouseover`/`mousemove` synthetically via `evaluate`
    instead (the dashboard G1 spec pattern). Same pass:
    `transition-all` on the net-worth tabs animates the icon-color
    swap — read post-click computed colors only after a ~400ms settle
    (the documented transition-settle rule applies to icon currentColor
    too, not just nav links) (plan v14 G1/G2).

33. **A "fast" surface still has a loading state — measure it by slowing
    the network.** The v15 audit found the boot spinner drifting on three
    axes nobody had seen because localhost resolves the data fetch in
    ~5ms: the window only opens under real network latency. Reproduce it
    deterministically in e2e with `page.route()` + `route.continue()`-after-
    `waitForTimeout` delays (the loading-state spec's `delayRoutes`), and
    unhook with `page.unrouteAll({ behavior: "ignoreErrors" })` before the
    spec ends — in-flight route callbacks outliving the test FAIL it with
    `"page.waitForTimeout: Test ended."`. Two more measurement rules from
    the same pass: a rotating element's `getBoundingClientRect()` measures
    the ROTATED bounding box (the 32×32 spinner measured 38–40px at
    various angles — use `offsetWidth/offsetHeight` for the true box),
    and Playwright's `devices["Desktop Chrome"]` is 1280×**720**, not
    800 — read `window.innerWidth/innerHeight` live instead of
    hard-coding viewport math (plan v15 G1).

34. **Radix mirrors toast text into a `role=status` live region — loose
    `getByText` double-matches it.** The v16 boot-failure spec's toast
    assertion tripped strict mode: "Network error — check your connection
    and try again" resolved to 2 elements — the description div AND the
    live-region span Radix renders for screen readers, whose text is the
    title+description CONCATENATION ("Notification Could not load your
    dataNetwork error…"). Fix: `getByText(text, { exact: true })` — the
    exact match hits only the element whose own text equals the string,
    never the mirrored live region. Same pass: a boot-time
    `catch { user: null }` conflates "data failed" with "logged out" —
    nest the try so a failed `refresh()` after a successful session probe
    keeps the user (the reference's silent zero-state stays in-app; the
    login bump was an auth failure the error wasn't) (plan v16 G1).

35. **`void promise` swallows failures AND hides them from you.** The v17
    calculator audit found the line-items load failing into a `void
    loadLineItems(item.id)` — an unhandled rejection with no toast, no
    log, and no test (the reference renders the same scenario as its
    SILENT empty-state, so the clone's silence looked like parity). The
    doctrine: every fire-and-forget fetch needs an explicit `.catch`
    that either surfaces the honest error (the superset class — a dead
    API must never render as "empty data") or documents why silence is
    the parity decision. Same pass: a NESTED Radix dialog sets
    `aria-hidden` on the parent — `getByRole` locators scoped to the
    parent dialog find NOTHING while the sub-dialog is open; assert the
    sub-dialog, close it, THEN assert the parent's content (the v17
    calculator-error spec pattern) (plan v17 G1).

36. **Next.js's route announcer is a second `role="alert"` on every
    page — never wait on a bare `[role=alert]` in specs.** The register
    duplicate-email spec flaked in 2 of 4 full-suite runs (never in file
    isolation): its `waitForSelector("[role='alert']")` matched
    Next.js App Router's ROUTE ANNOUNCER (`__next-route-announcer__`,
    aria-live, dynamically mounted with EMPTY text), passing before the
    409 banner rendered — then the one-shot evaluate read `null` in the
    latency gap under full-suite load. Fix: filter the locator by the
    expected banner TEXT and assert with a retrying
    `toBeVisible`/`toHaveText`. Same pass: the v18 audit found the v17
    `void promise` doctrine still un-applied in the net-worth view —
    the asset/liability confirm bars called `void deleteAsset()` /
    `void deleteLiability()` (silent unhandled rejections, no honest
    toast). The tier-by-tier sweep is now COMPLETE: boot (v16),
    budget-item mutations (v16), line-item load/create/delete (v17),
    and asset/liability save/delete (v18) all catch and toast. The
    v18 post-fix grep sweep (`grep -rn 'void (delete|create|update|load|refresh)' src/`)
    is the closing discipline — it caught item-card's `void
    deleteItem()` AFTER the net-worth fix looked "complete". The
    clone's toast texts per tier: "Could not save the item" /
    "Could not delete the item" / "Could not save the line item" /
    "Could not remove the line item" / "Could not load the line items" /
    "Could not save the asset" / "Could not delete the asset" /
    "Could not save the liability" / "Could not delete the liability"
    (plan v18 G1/G2).

37. **The VLM screenshot sweep is a SCREENING layer — every flagged
    diff must be DOM/measurement-verified before it becomes a
    finding.** The v19 sweep (full-page screenshot pairs through the
    z-ai vision CLI — the first visual-AI comparison layer, extending
    computed-style probes) compared 12 auth-state pairs + 5 app views +
    3 dialogs. It found ONE real drift (the item dialog's
    recurring-toggle row: the reference runs the switch LEFT as the
    row's first child with the label right, NO calendar icon, NO
    border, on a green-tinted `rgb(245,248,245)` surface; the clone ran
    icon+label left, switch right, 1px border, transparent — h 74 vs
    72). It ALSO hallucinated twice: a "faded smaller logo" (the two
    PNG assets are MD5-identical and both render 80×80 from 480×480)
    and a "taller wider sign-in button" (294×44 on both). The
    discipline: VLM verdict → DOM measurement → pin spec asserting the
    MEASURED values (never the VLM's words). The companion pixel-diff
    layer's 4–20% deltas decompose into font anti-aliasing noise (two
    Chrome instances rasterizing the same fonts) plus the reference's
    "Edit with Base44" floating platform badge (platform chrome, not
    app design) — decompose before concluding drift. The same sweep
    also DOM-verified the calculator's "• Will update category total"
    as a matching data-conditional (the reference shows it on a
    non-zero item; hidden when total === amount) (plan v19 G1).

38. **The base64→`atob`→`eval` probe transport mangles multi-byte
    UTF-8 — keep probe sources ASCII-only.** The v19 census probe's
    literal "·" (U+00B7, UTF-8 C2 B7) decoded through `atob` as TWO
    Latin-1 characters, so its regex never matched the DOM text (empty
    counts on every run — also the root cause behind the v19 session's
    "mid-pass fix"). The v20 fix builds the separator from
    `String.fromCharCode(0xb7)` (pure-ASCII source, transport-proof).
    Generalize: any probe that travels through base64 must avoid
    non-ASCII literals — escape them, or build them from char codes.
    Same pass, second lesson: the mobile VLM sweep re-proved that
    superset-fix manifestations read as "differences" (the reference's
    own 464px networth overflow: its fixed 48px `text-5xl` figure, its
    2-col summary grid, its off-screen Add button) — decompose every
    mobile-view flag into superset-fix vs data vs real drift before
    filing (plan v20, Observations).

39. **The reference site itself drifts — re-measure pinned chrome on every
    pass.** v21's calculator row-actions finding: the v6 pin said the
    reference renders its line-item row actions always-visible (measured
    at rest, session 11) — but the LIVE reference now wraps them in
    `opacity-0 group-hover:opacity-100`. A pinned "always" claim is only
    as fresh as its last measurement; when a VLM flag contradicts a pin,
    re-measure BOTH sides before refuting the flag (the flag was right,
    the pin had aged). Same family as v19's recurring-row drift.
    Same pass, second lesson: a "silent" form submit usually means native
    validation — a malformed test email (`a@b@c.com`) fails `type=email`
    constraint validation with NO visible error and NO network call
    (the live register flow "did nothing"); check
    `form.checkValidity()` + the invalid inputs' `validationMessage`
    before suspecting React state (plan v21, the probe-v21 live-audit
    lesson).

40. **A clicked submit parks the pointer on the next state's button — and
    screenshots inherit the pointer too.** v22's verify-email spec flake:
    Playwright's mouse stays at the "Create account" click point; the
    card swaps to the verify state and the "Verify email" button renders
    UNDER the parked pointer; its 200ms hover transition (`#0f172a` →
    `#1e293b`) was mid-flight when the chrome read landed
    (`rgb(19,27,46)` — a "wrong color" that was really a wrong TIME).
    The app was correct; the fix is procedural: `page.mouse.move(5, 5)` +
    a 350ms settle after any state swap that re-renders a button under
    the click point (the same discipline as the v11/v13 transition
    settles, now encoded in `registerFreshAccount`). The same pass's
    screenshot corollary: a VLM pair shot captured with the pointer
    parked from an earlier real click showed the reference's
    hover-revealed row actions VISIBLE while the clone's (pointer
    elsewhere) stayed hidden — a false "missing actions" diff. Park the
    pointer away on BOTH sides before every comparison capture (plan
    v22 G1 + the mobile-calculator triage).


41. **The probe tooling itself carries state — park, settle, re-measure, and
    know which browser you are actually driving.** v23's three probe lessons,
    all from ONE pass: (a) the agent-browser "sessions" (`session new
    ref25` / `clone25`) resolve to ONE shared browser tab — `session use`
    prints `default` and the active site is whatever the last `open`
    pointed at; a drift probe that skipped the open read the CLONE's
    dashboard on the "reference" session and produced a false
    data-drift alarm (the clone's seed numbers on the "reference"). The
    discipline: ALWAYS `open <target-url>` + settle before every eval.
    (b) The v22 parked-pointer lesson extends to LIVE PROBES: a probe
    eval on a just-swapped state reads the swapped-in button's hover
    color until the pointer is parked (the clone's Verify button read
    `#1e293b` until `mouse.move(5,5)`). (c) A transient FIRST geometry
    read after a state swap (the reference's Verify button read h=40
    once; two re-measures + the `h-11` class attribute refute it) —
    after a state swap, re-measure and use the class attribute as the
    tie-breaker before declaring a finding (plan v23, the
    verify-mobile probe trio).

42. **When two probe reads disagree, distrust the one that ran LAST
    without a fresh open — and arbitrate with the class attribute.** The
    v24 pass re-learned lesson 41a the hard way: two "reference" class
    dumps read the CLONE's forgot page left in the shared browser tab by
    an intervening `with-server.sh` invocation (they showed `h-11` flat
    where a fresh-open census showed the reference's `h-10 sm:h-11`
    family). The reliable probe form for MULTI-STATE surfaces: one eval
    that walks every state (open → click → settle → read → click → …)
    immediately after the fresh open — the auth-census pattern
    (`scripts/parity-probes/probe-v24-auth-census.mjs`); per-state probes
    that re-query after other commands have crossed the tab invite the
    false read. When two geometry reads disagree, the CLASS ATTRIBUTE is
    the tie-breaker (it is rendered HTML, not a layout snapshot — it
    cannot be transient). And the form-scale VLM blind spot is now SIX
    consecutive: the sign-up mobile pair returned IDENTICAL while the DOM
    found a 4px input-height, 2px font, and 6px label-gap delta — sub-6px
    differences are below the VLM's resolution; DOM-decompose before
    believing a clean VLM verdict on form chrome (plan v24 G1/G2).

---

## 13. Pitfalls to Avoid

**Architecture**

- Don't fetch domain data in RSC pages — the client store owns data flow
  (reference parity, §5).
- Don't put Prisma imports in `src/components/**`; only `src/lib/**` and
  `src/app/api/**` touch the database.
- Don't add `middleware.ts` for auth — sessions are verified per-handler
  (`verifySession`) and per-page (`RequireSession`).

**TypeScript**

- No `any` (there are zero `any`s in `src/` — keep it that way); use
  `unknown` + narrowing or the exported domain types.
- Don't fork enum copies — import from `src/lib/constants.ts`.

**Money**

- Never `parseFloat`/arithmetic on dollar floats — `toCents` on input,
  integer math, `fromCents`/`formatMoney` on output (§15).
- Don't store floats in Prisma — amounts are `Int` (cents) on every model.

**Tailwind v4**

- Don't add HSL triplets to `@theme` (transparent trap); only literal hex.
- Don't use `bg-gradient-to-*` for brand gradients (oklab drift).
- Don't put `mt-*`/`mb-*` inside `space-y-*` children (selector rewrite).
- Don't use the v3 arbitrary syntax `[--var]`; v4 native is `w-(--var)`.

**Testing**

- Don't assert seed data without ensuring the e2e db was reset (global setup
  owns that; your spec owns its own cleanup).
- Don't write specs that depend on execution order.
- Don't assert `#hex` computed fills — browsers return `rgb()`.
- Don't measure animated geometry mid-animation.

**Security**

- Don't read `process.env.AUTH_SECRET` inline in more than one place —
  `authSecret()` centralizes the fallback warning.
- Don't bypass `api-helpers.ts` envelopes when adding endpoints.
- Don't weaken `ignoreBuildErrors` back into `next.config.ts` — it hid
  nothing and shipped bugs.

---

## 14. Best Practices

- **Types at the boundaries:** zod schemas validate every request body
  (`src/lib/validation.ts`); inferred types flow inward. UI form types come
  from the same schemas (`z.infer`).
- **Pure domain modules:** `money.ts`, `dashboard.ts`, `rate-limit.ts`,
  `line-item-service.ts` import no framework — they run in node and browser
  test projects alike (that's why `vitest.config.ts` has a browser-mode
  api-contract project).
- **Serializers at the API edge** (`src/lib/serializers.ts`): Prisma rows →
  JSON DTOs with dates as ISO strings; never `JSON.stringify` a Prisma row
  raw.
- **Envelope responses** (`src/lib/api-helpers.ts`): `{ ok, data }` /
  `{ ok: false, error }` everywhere; the client `ApiError` surfaces
  `error.message` in toasts.
- **One constant source:** enums + labels + palette in `constants.ts`.
- **Comments explain *why*, not what** — the codebase comments trap numbers,
  parity decisions, and reference bug fixes; grep "reference" for the trail.
- **Commit discipline:** every bug fix lands with the test that pins it in
  the same commit (TDD).

---

## 15. Coding Patterns

**API route (collection)** — `src/app/api/budget-items/route.ts` shape:

```ts
export async function GET() {
  const session = await verifySession();          // 401 envelope when absent
  if (!session) return unauthorized();
  const rows = await prisma.budgetItem.findMany({ where: { userId: session.id } });
  return ok(rows.map(serializeBudgetItem));       // { ok: true, data }
}

export async function POST(request: Request) {
  const session = await verifySession();
  if (!session) return unauthorized();
  const body = createBudgetItemSchema.safeParse(await request.json()); // zod
  if (!body.success) return invalid(body.error);                      // 400
  const created = await prisma.budgetItem.create({ data: { ...body.data, userId: session.id } });
  return ok(serializeBudgetItem(created), 201);
}
```

**Line-item mutation (server-side recalc)** — the calculator contract:

```ts
// inside src/app/api/line-items/*/route.ts via line-item-service.ts
const lineItem = await prisma.expenseLineItem.create({ data: { ...input } });
const { amount, count } = await recalcParent(prisma, lineItem.budgetItemId);
// amount = integer-cents sum of the parent's line items; the parent
// BudgetItem is updated in the same transaction, so the item card and the
// dashboard totals move without any Save button.
```

**Money handling** — `src/lib/money.ts`:

```ts
toCents(1500.5)            // 150050  — input boundary
sumAmounts([150050, -500]) // 149550  — integer math only
formatMoney(1495.5)      // "$1495.50" — PLAIN, no grouping (dashboard/items/calculator)
formatSignedMoney(2065)  // "+$2065.00" (breakdown Net Balance)
formatMoneyGrouped(25000) // "$25,000.00" — net worth ONLY
formatMoneyShort(80300)   // "$80,300" (networth tab counts)
formatRatio(0.21)          // "0.21" (toFixed(2); caller appends ":1"); null → "∞"
```

**Store action** (client) — `src/components/budget/store.ts` shape:

```ts
createItem: async (data) => {
  try {
    const item = await api.createBudgetItem(data);   // src/lib/api.ts
    set((s) => ({ items: [...s.items, item] }));     // stable-state update
    toast.success("Budget item created");
  } catch (error) {
    toast.error(messageOf(error));                   // ApiError message
  }
},
```

**Dialog skeleton** (all five dialogs follow this) — sticky header with
`z-10`, Close at `z-20`, lazy form state (§5), footer with
`type="submit"` + outline Cancel, native `<form onSubmit>`.

---

## 16. Coding Anti-Patterns

| ❌ Don't | ✅ Do instead |
|----------|--------------|
| `useBudgetStore((s) => s.items.filter(f))` | `useBudgetStore(useShallow((s) => s.items.filter(f)))` |
| `(a * 100).toFixed(2)` money math | `toCents` → int math → `formatMoney` |
| `bg-gradient-to-br from-forest to-lime` | inline `linear-gradient(135deg, var(--forest-dark), var(--forest-medium))` |
| `@theme { --color-x: 210 40% 20%; }` | `@theme inline { --color-x: #1a3a2e; }` |
| `w-[--sidebar-width]` (v3 syntax) | `w-(--sidebar-width)` (v4 native) |
| `space-y-2` child with `mt-4` | remove `space-y`, give children explicit margins |
| `<div onClick>` controls | real `<button>`/Radix primitives (a11y + e2e roles) |
| `any` / `as any` | `unknown` + narrowing, or the domain type |
| raw `fetch` in components | `src/lib/api.ts` wrapper (`ApiError` → toast) |
| `useEffect(() => setForm(...), [modal])` reset | lazy initializer + adjust-during-render (§5) |
| one `closeModals()` from the line-item dialog | `closeLineItemModal()` (keeps calculator open) |
| bare `prisma db push` from any shell | `npm run db:push` (env discipline, §3) |
| `TODO` / placeholder text in committed code | finish it or file it in `docs/remediation-plan.md` |

---

## 17. Responsive Breakpoint Reference

Default Tailwind breakpoints only (no custom config): `sm 640`, `md 768`,
`lg 1024`, `xl 1280`, `2xl 1536`.

| Concern | < 768px (mobile) | ≥ 768px (desktop) |
|---------|------------------|--------------------|
| Navigation | sticky top header (hamburger + brand title, left-aligned) + slide-in sheet **288px** (`--sheet-width: 18rem`), left-anchored, `h-svh` | fixed left rail **256px** (`w-(--sidebar-width)`, `--sidebar-width: 16rem`), `h-svh`, mobile chrome hidden |
| Breakdown rows | stacked | responsive grid |
| Dialogs | full-bleed-ish centered panel | centered panel, max-width per dialog |
| Testing target | Playwright mobile project **390×844** (iPhone-14-class) | Playwright desktop project (1280×720 default) |

The one breakpoint that matters is **md (768px)** — the sidebar/mobile-header
swap. Everything else is single-column fluid.

## 18. Z-Index Layer Map

| Layer | Value | Element / location |
|-------|-------|--------------------|
| Sticky card/dialog headers | `z-10` (5 uses) | `sidebar.tsx` rail, dialog sticky headers, dashboard hero header |
| Dialog Close (×) | `z-20` (1 use) | `dialog.tsx` — must stay above the sticky header (E-3) |
| Modal overlay + panel | `z-50` (5 uses) | `dialog.tsx` overlay, `.zb-modal-panel`, dropdown-menu content |
| Toast viewport | *no z-index war* — pointer-events strategy | viewport `pointer-events: none` so an empty container can never block the hamburger (D-1); toasts restore `auto` (`globals.css` §toast) |

Conflict rules: raise the *innermost interactive chrome* (Close) above its own
sticky header; keep portals at `z-50`; never blanket `z-[100]` fixed
full-width containers — that is exactly the reference bug D-1.

## 19. Color Reference (Complete)

**Brand (`:root` in `globals.css`):**

| Token | Hex | RGB | Tailwind path | Primary usage |
|-------|-----|-----|---------------|---------------|
| `--forest-dark` | `#1a3a2e` | 26,58,46 | `--color-primary` | buttons, active nav, gradient start |
| `--forest-medium` | `#2d5a4a` | 45,90,74 | — | gradient end (hero/summary) |
| `--lime-green` | `#8fbc3f` | 143,188,63 | — | Savings donut, savings accents |
| `--lime-light` | `#b8d87e` | 184,216,126 | — | active-nav gradient end |
| `--orange-dark` | `#e07a3b` | 224,122,59 | — | Need donut, warning accents |
| `--orange-light` | `#f5a962` | 245,169,98 | — | orange tints |
| `--blue-dark` | `#2c5f7c` | 44,95,124 | — | deep blue accent |
| `--blue-medium` | `#3b7ea1` | 59,126,161 | — | Want donut, savings view |
| `--neutral-warm` | `#fafaf8` | 250,250,248 | `--color-background` | app background |

**Semantic (`@theme inline`):** background `#fafaf8`, foreground `#3f3f3f`,
card & popover `#ffffff`, primary `#1a3a2e` (+ white foreground), secondary
`#f4f4f5`, muted `#f4f4f5`, muted-foreground `#737373`, accent `#f0f2ee`
(foreground `#1a3a2e`), destructive `#bd3228` (white foreground),
border/input `#e5e7e3`, ring `#1a3a2e`, sidebar `#fafafa`.

**Chart palette (donut, measured on the reference, pinned by e2e):**
Need `#e07a3b`, Want `#3b7ea1`, Savings `#8fbc3f`. Also in
`src/lib/constants.ts` → `COLORS`.

**Forbidden:** Tailwind default-palette classes for brand color (`green-600`,
`blue-500`…), any oklch default, purple/indigo, and any hex not in this table.
The one exception: pure white `#ffffff` card surfaces (a semantic token, listed
above). Computed styles return `rgb()` forms — e2e asserts
`rgb(26, 58, 46)` etc.

## 20. The Complete TypeScript Interface Reference

All shapes live in `src/components/budget/store.ts`, `src/lib/types.ts`,
`src/lib/money.ts`, `src/lib/rate-limit.ts`, `src/lib/constants.ts` (type
unions), and `prisma/schema.prisma` (model types). Key contracts:

```ts
// store.ts — modal state machine
export interface ModalState {
  item: { mode: "create"; type: BudgetItem["type"] } | { mode: "edit"; item: BudgetItem } | null;
  calculator: { item: BudgetItem } | null;
  lineItem: { mode: "create"; budgetItemId: string } | { mode: "edit"; lineItem: ExpenseLineItem } | null;
  asset: { mode: "create" } | { mode: "edit"; asset: Asset } | null;
  liability: { mode: "create" } | { mode: "edit"; liability: Liability } | null;
}

interface BudgetStore {
  user: SessionUser | null; booted: boolean;
  items: BudgetItem[]; assets: Asset[]; liabilities: Liability[];
  lineItems: Record<string, ExpenseLineItem[]>;
  modal: ModalState;
  boot(): Promise<void>; refresh(): Promise<void>;
  login(email, password): Promise<void>;
  register(email, password, name?): Promise<void>;
  logout(): Promise<void>;
  createItem(data: BudgetItemFormData): Promise<BudgetItem>;
  updateItem(id, data: Partial<BudgetItemFormData>): Promise<BudgetItem>;
  deleteItem(id): Promise<void>;
  loadLineItems(budgetItemId): Promise<ExpenseLineItem[]>;
  createLineItem(data: LineItemFormData & { budgetItemId: string }): Promise<void>;
  updateLineItem(id, data: Partial<LineItemFormData>): Promise<void>;
  deleteLineItem(id): Promise<void>;
  createAsset(data: AssetFormData): Promise<void>;          // + update/delete
  createLiability(data: LiabilityPayload): Promise<void>;   // + update/delete
  openItemModal(m): void; openCalculator(item): void; openLineItemModal(m): void;
  openAssetModal(m): void; openLiabilityModal(m): void;
  closeModals(): void; closeLineItemModal(): void;          // scoped (E-5)
}

// money.ts — the money boundary
toCents(amount: number): number;            fromCents(cents: number): number;
sumAmounts(amounts: number[]): number;
formatMoney(amount: number): string;        formatSignedMoney(amount: number): string;
formatMoneyGrouped(amount: number): string; // net worth surfaces
formatNetWorth(amount: number): string;     formatMoneyShort(amount: number): string;
formatRatio(ratio: number | null): string;  formatPercent(part: number, whole: number): string;
percentValue(part: number, whole: number): number;

// rate-limit.ts
export interface RateLimiterConfig { limit: number; windowMs: number; }
export interface RateLimitDecision { allowed: boolean; remaining: number; retryAfterSeconds: number; }
export const AUTH_RATE_LIMIT: RateLimiterConfig;   // { limit: 10, windowMs: 15 * 60 * 1000 }
export class RateLimiter { check(key: string, now?: number): RateLimitDecision; }

// constants.ts — union types
type ItemType = "income" | "savings" | "expense";
type Classification = "need" | "want" | "savings";
type Frequency = "one-time" | "weekly" | "bi-weekly" | "monthly" | "quarterly" | "annually";
type ItemStatus = "planned" | "active" | "completed";
type LineItemStatus = "active" | "pending" | "cancelled";
type AssetType = "bank_account" | "superannuation" | "property" | "investment" | "vehicle" | "other";
type LiabilityType = "home_loan" | "personal_loan" | "credit_card" | "car_loan" | "student_loan" | "other";

// auth.ts — constants
const SESSION_COOKIE = "zb_session";        // httpOnly, sameSite=lax, secure in prod
const SESSION_TTL_MS = 30 * 24 * 60 * 60 * 1000;   // 30 days
const SCRYPT_KEYLEN = 64;
```

zod schemas (`src/lib/validation.ts`): `emailSchema`, `passwordSchema`,
`registerSchema`, `loginSchema`, `create/updateBudgetItemSchema`,
`create/updateLineItemSchema`, `create/updateAssetSchema`,
`create/updateLiabilitySchema` — all request bodies flow through these.

---

## Appendix A: ADRs

| ADR | Decision | Rationale |
|-----|----------|-----------|
| 1 | Single Next.js app (no monorepo) | One deployable, one test chain; matches repo scaffolding and reference shape |
| 2 | Prisma + SQLite, `db/` at repo root | Zero-config self-hosting; path discipline in §3 makes relative URLs safe |
| 3 | scrypt + HMAC-signed cookie sessions (`zb_session`, 30d) | No external auth dependency; parity with reference's platform auth behavior |
| 4 | Zustand client store owns domain data (no RSC fetching) | Mirrors reference SPA data flow; keeps one cache, one toast path |
| 5 | Integer cents end-to-end | Eliminates float money bugs class-wide; pinned by `tests/money.test.ts` |
| 6 | Tailwind v4 with literal-hex `@theme inline` + inline gradients | Survives all five documented v4 traps (§4) with engine-independent output |
| 7 | Three-tier tests: Vitest unit (108) / Playwright e2e (265, desktop+mobile) / bash API smoke (35) | Each tier catches what the previous can't (see §12 L1, L8) |

Full reasoning: `Project_Architecture_Document.md` (7 ADRs expanded).

## Appendix B: Audit & Session History

| Date | Session | Outcome |
|------|---------|---------|
| Session 1 | Recon → build → test-driven remediation → first push (`703ea74`) | All findings A/B/C/D/E/F/G identified and fixed; see `docs/session_1.md` + `docs/remediation-plan.md` |
| Session 1 (cont.) | Docs + screenshots + final push (`6efc1ce`) | 4 root docs, 10 VLM-verified screenshots |
| 2026-10-07 | Re-verification (this document) | Full chain re-run green (87/34/30 + tsc + eslint); live reference re-checked — both mobile-nav bugs still present on the reference, both fixes verified on the clone; `zero-balance_SKILL.md` distilled |
| Sessions 3–11 | Parity iterations v2–v6 (`docs/remediation-plan-v2..v6.md`) | Money formats, drill-down, badges, mobile chrome, tokens, dialog buttons, plain-text menus, empty states, wide column — 96/73/30 green at `42f50da` |
| 2026-10-07 | Session 13 — parity iteration v7 (`docs/remediation-plan-v7.md`) | Login-surface slate pins + text-sm, logo halo layer, 24px brand target + text-lg, 16px toggle icon, sheet border/overlay pins, custom 404, head metadata, post-login root redirect — 96/83/30 green |
| 2026-10-08 | Session 15 — parity iteration v8 (`docs/remediation-plan-v8.md`) | Dialog footers rebuilt as the reference's flex-1 full-row split (Cancel ≈ 307px + Save ≈ 305px), all remaining badge/nav/Calculate named classes hex-pinned (plain rgb computed styles), stray `prisma/db/custom.db` untracked; every mobile-nav superset fix + v7 pin re-verified live — 96/92/30 green |
| 2026-10-08 | Session 17 — parity iteration v9 (`docs/remediation-plan-v9.md`) | Donut re-sorted to the reference's value-DESC convention + `labelLine={false}`; dialog X-close rebuilt as the 36×36 in-header button (sticky header 69px); form labels restored to the inline shadcn-v1 line box (12px gap — v4's space-y margin-block-end is layout-ignored on inline first children, pinned in globals.css); 52px classification tiles; radio/switch #171717 primitive family (checked track, borders, dot, white ring-0 thumb); `rounded-full` → `rounded-[9999px]` ×24 sites (v4 emits calc(infinity)); login per-state control geometry (14px button text, 44px sign-up/forgot vs 48px sign-in) — 96/102/30 green |
| 2026-10-08 | Session 19 — parity iteration v10 (`docs/remediation-plan-v10.md`) | Mobile sheet active-nav highlighting restored (the reference's sheet renders the current route in the full active style — white + the 135deg forest-medium→lime gradient + fw 500, same as its rail; the clone had suppressed it since session 1) — pinned by 2 new mobile-navigation specs; the pass also swept the Select popover OPEN state, card action-menu OPEN state, drill-down EXPANDED rows, guidelines leaves, live focus-visible rings, dialog scroll mechanics, date inputs, and empty-submit — all verified identical; reference's no-toast-on-save documented (clone toasts = superset UX) — 96/104/30 green |
| 2026-10-08 | Session 21 — parity iteration v11 (`docs/remediation-plan-v11.md`) | Empty-state headings → 20px `text-xl` (items + net-worth); the `.zb-btn-add` family re-pinned — v3 bare-shadow ambient (gradient buttons, every size), v3 shadow-sm (outline variant), the shadcn focus-visible ring (white inner + 1px #0a0a0a + transparent 2px outline) replacing the browser-default outline; Plus icons 20→16px on the 7 Add-button sites; the session-1 hover opacity-0.9 fade removed (reference has no hover change) — pinned by 3 new/extended specs; the pass also swept the tablet breakpoints (767/768/1024), rail hover, hero status badge, filter card live behavior, item-badge census, dialog/sheet/stat-card shadows (full strings), and the no-logout parity — all verified identical — 96/107/30 green |
| 2026-10-08 | Session 23 — parity iteration v12 (`docs/remediation-plan-v12.md`) | Login ERROR state rebuilt as the reference's red-tinted bordered banner (red-50/70%, red-200 border, radius 12, pad 16, centered red-700 14px/400 — the same slot serves 401s and sign-up mismatches); per-route tab titles restored ("Income \| ZeroBudget" etc., one-word "Networth") via route-segment `layout.tsx` metadata + the root pipe template — the first client-effect attempt was reverted after discovering React Float's post-hydration `<title>` re-emission (lesson 27); login root promoted to a `<main>` landmark; forgot-password rebuilt as the reference's confirmation-state layout with honest copy (no mail transport) — pinned by 5 new/extended specs; the pass also swept the payment-method filter + listbox, the a11y landmark/h1 structure, and the reference's sheet-closes-on-Escape behavior (matching) — 96/112/30 green |
| 2026-10-08 | Session 25 — parity iteration v13 (`docs/remediation-plan-v13.md`) | Register duplicate-email 409 text matched to the reference ("A user with this email already exists"); sign-up password placeholders restored ("Min. 8 characters" / "Re-enter password"); login inputs' FOCUS ring pinned as the reference's two-layer shadcn ring (white 2px + slate-400 4px — v4's color-only ring utility emits no shadow) — pinned by 3 new specs; the pass also swept the register banner chrome, login 401 text, item-card date formats, hero progress-bar chrome, the OR divider, Google button chrome + OAuth divergence, cursor styles, authed /login, and the code audit (npm audit = dev-only unpatchable braces advisory; secret scan clean) — 96/115/30 green |
| 2026-10-08 | Session 27 — parity iteration v14 (`docs/remediation-plan-v14.md`) | Donut hover TOOLTIP pinned to the reference (value "$X.XX" + full recharts-2 chrome — border #e5e7e3, radius 8, 0 4px 12px shadow, black item row; recharts 3 drifts on all four axes); net-worth tab icons restored (16px lucide circle-arrow-up/down, mr-2, currentColor — active green-900/inactive gray); net-worth page header's 48×48 gradient icon chip added (forest→lime, radius 12, 24px white trending-up, BOTH viewports — the items-view chip family extended to the page the v4 pin missed) — found via a VLM screenshot sweep with DOM verification of every flag; the pass also swept the net-worth tablist keyboard flow, dialog initial focus (ref: no move — clone's Radix trap is the superset), invalid-input validation (silent both), guideline/accordion hovers, user-select, and the full mobile-nav stack — 96/119/30 green |
| 2026-10-08 | Session 29 — parity iteration v15 (`docs/remediation-plan-v15.md`) | The full-page LOADING STATE rebuilt to the reference (the last unmeasured surface class): DOM-replacing `fixed inset-0` white-backed overlay + the slate spinner (32×32, 4px, #e2e8f0 track + #1e293b top spoke, 9999px, spin 1s), no shell mounted while loading, and `boot()` flipping `booted` only after the data lands (route-delayed e2e pins: chrome, DOM replacement, data-flight timing, client-nav inverse, 390×844) — the old 2px lime/transparent-top inline spinner hid at the session probe while data popped into empty views; also swept the Select keyboard flows (ref internally inconsistent — filter selects advance, dialog selects don't; the clone's Radix matches the dialog/a11y pattern), a VLM income/savings/mobile sweep (all flags data-driven), and mobile-nav R1–R4 + data drift (clean, ninth check) — 96/123/30 green |
| 2026-10-08 | Session 31 — parity iteration v16 (`docs/remediation-plan-v16.md`) | The boot DATA-FAILURE state measured for the first time (route-aborted entity API): the reference STAYS in-app rendering its SILENT ZERO-STATE (full shell, 0.0% / $0.00 / ✓ NET ZERO, items views "0 items · $0.00" + standard empty states, NO error surface) while the clone's single `catch` bumped the authenticated user to `/login`; fixed with a nested try in `boot()` (user stays, `bootError` flag) + the one-shot honest error toast in AppShell; the reference's mutation failure measured too (SILENT no-op — dialog stays open, no feedback; the clone's dialog + error-toast superset verified live) and its client-nav under a dead API (no refetch — in-memory); mobile-nav R1–R4 re-verified + data drift clean (tenth check) — 96/126/30 green |
| 2026-10-08 | Session 33 — parity iteration v17 (`docs/remediation-plan-v17.md`) | The CALCULATOR LINE-ITEM ERROR TIER measured for the first time (the parent-recalc family the session-32 log flagged next): the reference is SILENT on every path with its entity API dead (calculator load → the empty-state "$0.00 / 0 items / No line items yet"; create → sub-dialog open, no feedback, no optimistic update; delete → row stays, no feedback); the clone's mutation-failure superset verified live and PINNED (create: "Could not save the line item"; delete: "Could not remove the line item"), while its calculator LOAD failure was swallowed as an unhandled rejection (`void loadLineItems(item.id)`) — fixed with a caught mount effect + the "Could not load the line items" toast (per-open semantics, rendering unchanged — the reference's empty-state parity via `?? []`); 3 new e2e specs (load/create/delete under route-aborted `**/api/line-items**`); lesson 35 documents the void-swallow + the nested-dialog aria-hidden trap; mobile-nav R1–R4 re-verified + data drift clean (eleventh check) — 96/129/30 green |
| 2026-10-09 | Session 35 — parity iteration v18 (`docs/remediation-plan-v18.md`) | The NET-WORTH ASSET/LIABILITY ERROR TIER measured for the first time (the last unpinned dialog family, per the session-34 suggestion): the reference is SILENT on both paths with its entity API dead (asset delete → no confirmation, card stays, zero feedback; asset save → dialog stays open, no feedback); the clone's save-failure superset verified live and PINNED ("Could not save the asset" / "Could not save the liability"), while BOTH delete paths swallowed the rejection (`void deleteAsset()` / `void deleteLiability()` — the v17 void accident in its last hiding place) — fixed with caught confirm-bar handlers + the "Could not delete the asset/liability" toasts (per-click semantics, surfaces unchanged) — and the post-fix grep sweep surfaced a THIRD site (`void deleteItem()` in item-card.tsx, the card-menu path the v16 dialog audit missed), fixed identically with "Could not delete the item"; 5 new e2e specs (asset/liability save/delete under route-aborted APIs + the item-card delete); G2: the register duplicate-email flake root-caused as Next.js's route announcer rendering a second empty `role=alert` — the spec's bare waitForSelector matched it and raced the banner; hardened with a text-filtered retrying locator (lesson 36); mobile-nav R1–R4 re-verified + data drift clean (twelfth check) — 96/134/30 green |
| 2026-10-09 | Session 37 — parity iteration v19 (`docs/remediation-plan-v19.md`) | The **VLM VISUAL SWEEP** — the first full-page visual-AI comparison layer (the session-36 log's top suggestion): 12 auth-state pairs + 5 app views + 3 dialogs compared through the z-ai vision CLI with a mechanical pixel-diff layer + MD5 asset hashing. Results: the auth surfaces IDENTICAL ×6 (the v12/v13 text pins held under full-page diffing; the logo PNGs byte-identical by MD5, both 80×80), the app views LAYOUT_IDENTICAL ×5 (the dashboard's three flags are known supersets/data), the dialogs clean except ONE real drift: the item dialog's RECURRING-TOGGLE ROW (the reference runs the switch LEFT — the row's first child, 12px gap to the label block — with NO calendar icon, NO border, and a green-tinted rgb(245,248,245) inline background, h 72; the clone ran icon+label left, switch right (justify-between), 1px border, transparent bg, h 74) — DOM-verified on four axes, fixed to the reference's arrangement, pinned by the dialog-buttons spec's new recurring-row test; two VLM hallucinations DOM-refuted (the "faded logo", the "taller button" — lesson 37: the VLM is a screening layer, every flag needs measurement); the calculator's "extra line" refuted as a matching data-conditional; tablet breakpoints 767/768/1024 re-measured (rail switch at 768 both, heading x=288 both); mobile-nav R1–R4 re-verified + data drift clean (thirteenth check) — 96/135/30 green |
| 2026-10-09 | Session 39 — parity iteration v20 (`docs/remediation-plan-v20.md`) | The **mobile-app-view + populated-edit-dialog VLM sweep** (the session-38 log's two top suggestions): 5 mobile views at 390×844 + the populated Edit dialog + the breakdown drill-down, compared pairwise through z-ai vision. Results: the mobile dashboard IDENTICAL; the networth flags all decomposed into the documented superset fix #4 (the reference's own 464px overflow: 48px `text-5xl` figure, 2-col grid, off-screen Add button) plus one refuted tab-tint hallucination (identical rgb(220,252,231)); the badge-wrap mechanism verified identical (data-driven wrap); the drill-down clean. TWO real drifts found, DOM-verified, fixed TDD-first, live-re-measured exact, and pinned: (G1) the ITEMS-VIEW HEADER ROW — base `items-start` missing so the Add button stretched full-width 358px on mobile (the reference's auto-width 147/155/150) and `mb-6` vs `mb-8` (a 24 vs 32px header→filter gap at BOTH viewports; the dashboard's row already carried the correct pattern); (G2) the CLASSIFICATION TILES — the reference's tile labels carry 16px lucide icons (circle-alert #e07a3b / heart #3b7ea1 / piggy-bank #8fbc3f) between the radio and the text in both Add and Edit states, missed by the v19 empty-dialog sweep. Also: the census probe's base64→atob UTF-8 mangling root-caused and fixed transport-safe (lesson 38); mobile-nav R1–R4 re-verified + data drift clean (fourteenth check) — 96/137/30 green |
| 2026-10-09 | Session 41 — parity iteration v21 (`docs/remediation-plan-v21.md`) | **SEO + the register verification gate.** Three finding groups: (G1) the sitemap.xml/robots.txt the reference serves, added via Next.js MetadataRoute routes (`src/app/robots.ts` + `src/app/sitemap.ts`) — the reference's five-URL/priority/weekly structure mirrored with the clone's routes, `/login` excluded like the reference, Next's canonicalizations documented as protocol-equivalent; (G2) the calculator's line-item row actions re-measured HOVER-REVEALED on the live reference (`opacity-0 group-hover:opacity-100` — the v6-era always-visible pin had aged with the reference's chrome change) — matched with the `@variant group-hover (.group:hover &)` pin in globals.css keeping the reveal alive on hover:none devices; (G3) the REGISTER POST-SUCCESS LANDING measured live for the first time: the reference gates registration behind a "Verify your email" state (6-digit code inputs 40×44, a 5-attempt countdown, resend semantics, unverified-login rejection) — rebuilt as the honest superset: the full state chrome + `/api/auth/verify-email` + `/api/auth/resend` + the register re-issue path + a 403 unverified-login rejection with the reference's exact banner + the honest dev-code delivery (no mail transport; the v12 forgot-password precedent) + the seeded demo user pre-verified. Swept clean: the mobile sheet-open VLM pair, the net-worth populated edit-asset pair (X-close thrice-refuted), the login keyboard-focus spot check (the v13 ring holds once settled + read in full); mobile-nav R1–R4 + data drift (fifteenth check) clean — 108/142/35 green |
| 2026-10-09 | Session 43 — parity iteration v22 (`docs/remediation-plan-v22.md`) | **The line-item sub-dialog's third dialog family.** Two finding groups: (G1) the verify-email spec's parked-pointer race root-caused — the Create-account click leaves Playwright's mouse where the swapped-in Verify button renders, and the 200ms hover transition reads mid-flight (a deterministic flake on a correct app; fixed with the park + settle discipline in `registerFreshAccount`); (G2) the line-item sub-dialog measured live for the first time at both viewports — the reference caps its panel at 85vh (desktop 672×680, mobile 358×717) with `space-y-5` form gaps (20px), while the clone rode the generic budget-item family (90vh + 24px gaps) — fixed with the inline `maxHeight: "85vh"` + `p-6 space-y-5` form, pinned by the dialog-buttons spec's third-family test (which also pins the budget dialog's 90vh so the family split can't regress). Swept clean: the mobile calculator VLM pair (the row-action "missing" flag = a screenshot pointer artifact — DOM-identical at rest AND under hover; the X-close claim refuted a FOURTH time), keyboard Tab sweeps on the dashboard + income views (order + focus chrome identical; the clone's computed rings carry invisible transparent lead layers), the SEO pair live on both sites, mobile-nav R1–R4 + data drift (sixteenth check) clean — 108/143/35 green |
| 2026-10-09 | Session 45 — parity iteration v23 (`docs/remediation-plan-v23.md`) | **A clean verification pass — the pins ARE the deliverable.** Two finding groups, both TEST-PINS of newly measured surfaces (the app matched the reference on every axis): (G1) the mobile sheet's KEYBOARD semantics measured live for the first time — initial focus lands on a sheet container, real Tab presses cycle the five links at identical positions and WRAP in a focus loop, the visible indicator is the blue #3b82f6 2px sidebar-ring layer (read in FULL — v4's transparent lead layers), Escape closes; pinned by the mobile-navigation spec's new test (the ring fades in ~200ms — settle 350ms before reading); (G2) the register verify-email state's MOBILE chrome measured for the first time at 390×844 — the responsive scale (circle 56/icon 28/h2 20px vs desktop 64/32/24; inputs 6×40×44 gap 6; button 294×44 #0f172a); pinned by the verify-email spec's new mobile describe (register budget 5→6 calls). Swept clean: the budget-item dialog's mobile pair (the VLM radio claim DOM-refuted — the 5th dialog-scale misread), the 404 at mobile, the v22 sub-dialog fix re-verified at both viewports, mobile-nav R1–R4 + SEO + data drift (17th check — the false alarm was the shared-browser lesson, lesson 41a) — 108/145/35 green (2 new e2e) |
| 2026-10-09 | Session 47 — parity iteration v24 (`docs/remediation-plan-v24.md`) | **Two REAL app fixes behind a clean VLM verdict — the DOM found what the VLM could not.** Pairing the register SIGN-UP state at mobile (390×844, first time) surfaced: (G1) the reference runs THREE responsive families across its auth forms — sign-in `h-11 sm:h-12`/`text-base md:text-sm`, sign-up `h-10 sm:h-11`/`text-sm sm:text-base md:text-sm` (40px/14px mobile), forgot `h-10 sm:h-11`/`text-base md:text-sm` (40px/16px) — the clone rendered the flat 44px sign-in family everywhere (desktop coincides on every axis, which is why the v9 pins and all prior desktop measurements passed; the drift was mobile-only: 4px taller inputs/buttons + 2px larger sign-up font); fixed with per-mode height/font branches (`login-card.tsx` — `INPUT_CLS` now carries only the invariant chrome). (G2) the v4 `space-y-1.5` inline-label trap — the v9 globals.css v3-pin stopped at `space-y-2` (the dialogs): v4's margin-block-end on the INLINE auth label is absorbed by the line box, collapsing the label→input gap to 4px where the reference renders 10px at every viewport (v3's margin-top sits on the input's `relative` wrapper); the pin extended to `space-y-1.5`. Swept clean: the sheet's ARROW keys (inert both), the forgot state's desktop chrome (identical), the v23 sheet-keyboard fix re-verified live, the v9 dialog label gap (12px both), mobile-nav R1–R4 + SEO + data drift (18th) — 108/150/35 green (5 new e2e; lesson 42 — the shared-tab false read struck again, arbitrated by the class attribute) |

## Appendix C: Live-Site Validation Methodology

Parity claims are validated against the live reference with `agent-browser`:

1. **Computed styles over screenshots** — `getComputedStyle` for fills,
   backgrounds, radii; `getBoundingClientRect` for widths/anchors.
2. **Hit-tests for clickability** — `document.elementFromPoint(cx, cy)` must
   return the target (or a descendant). This is how D-1 was found: the empty
   Toaster DIV intercepted the hamburger's center point.
3. **Real clicks for flows** — open sheet → measure 288px → click nav link →
   assert navigation + dialog disappearance (D-2).
4. **Login-verified sessions** — reference creds in the task brief; clone
   uses the seeded demo user.
5. Anything measured is then **pinned as an e2e assertion** so parity can't
   silently drift (dashboard gradient, donut fills, sheet geometry).

## Quick Reference Card

| Need | Path |
|------|------|
| Brand tokens | `src/app/globals.css` (`:root` + `@theme inline`) |
| Enums & labels | `src/lib/constants.ts` |
| Money math | `src/lib/money.ts` |
| Dashboard aggregation | `src/lib/dashboard.ts` |
| Validation schemas | `src/lib/validation.ts` |
| Auth (scrypt/HMAC/cookie) | `src/lib/auth.ts` |
| Rate limiter | `src/lib/rate-limit.ts` |
| DB path resolution | `src/lib/db-path.ts` (+ `tests/db-path.test.ts`) |
| Line-item recalc | `src/lib/line-item-service.ts` |
| Client store | `src/components/budget/store.ts` |
| Shell / sidebar / sheet | `src/components/budget/app-shell.tsx`, `sidebar.tsx` |
| Dialogs | `src/components/budget/*-dialog.tsx` (5) |
| UI primitives | `src/components/ui/` (12) |
| E2E specs | `tests/e2e/*.spec.ts` (24 files, 271 tests) |
| Smoke script | `scripts/smoke-test.sh` (35 steps, port 3210) |
| Screenshot capture | `scripts/capture-screenshots.mjs` (port 3100) |
| Remediation record | `docs/remediation-plan.md` |
| 2026-10-09 | Session 49 — parity iteration v25 (`docs/remediation-plan-v25.md`) | **Three DOM-verified fixes from the FIRST keyboard-focus-ring sweep of the auth + 404 surfaces** (REAL Tab presses, pointer parked, 350ms settle): (G1) the auth SUBMIT buttons' focus-visible ring — the reference renders zinc-950 `#09090b` (its shadcn `ring-ring`: white 2px offset + the v3 ambient) where the clone had copied the INPUTS' slate-400 `#94a3b8` — the reference runs DISTINCT ring families per component (inputs two-layer #94a3b8 v13, submits #09090b, dialog buttons 1px #0a0a0a v19, the 404 button plain-focus slate-500 #64748b); fixed on both submit lines in `login-card.tsx`. (G2) the 404 Go Home button — plain `focus:` (ANY focus, not keyboard-only) + `#64748b`; the clone had the keyboard-gated slate-400; fixed verbatim in `not-found.tsx`. (G3) the BODY BACKGROUND layer — the reference styles NO body bg (the browser's white canvas; class `antialiased` only) and paints its warm `#fafaf8` paper on the app-shell wrapper; the clone had the paper on the body (the v7-era MANIFEST read — a PWA splash color): visually invisible (the login gradient, the shell, and the 404 root cover the body everywhere — regenerated screenshots byte-identical, PIL-verified) but a computed-style + layer-structure drift, corrected (`--color-background: #ffffff` + the shell's `bg-(--neutral-warm)`). Swept clean: the auth forms at the sm band 672×800 (the sign-up font's 16px middle step — exact match, the v24 ladder at the third viewport), the login full focus walk (Google/swap buttons' browser-default outlines match; the reference's 7th stop is the Base44 PLATFORM badge, not app chrome), the v24 fixes re-verified live, mobile-nav R1–R4 + SEO + data drift (19th) — 108/154/35 green (4 new e2e; lesson 43 — agent-browser eval programmatic focus() never engages :focus/:focus-visible on either site, REAL Tab presses are the only reliable focus-chrome probe; lesson 44 — the tool-result display pipeline strips the literal left-bracket+m sequence from rendered text, so a bracketed destructure line displays corrupted: verify with charCodeAt before fixing) |
| 2026-10-09 | Session 51 — parity iteration v26 (`docs/remediation-plan-v26.md`) | **Two DOM-verified fixes behind the session-51 log's suggested surfaces**: (G1) the body's `antialiased` class — the reference REMOVED it after v25 (its body is now fully classless across /login, /, and the 404, `-webkit-font-smoothing: auto`; the same reference-drift class as v19's recurring row); the clone drops the class (rendering byte-identical on Linux Chromium — the A/B pixel test proved the class is render-inert here; on macOS the reference's subpixel text is the target). (G2) the verify-email code inputs' `autocomplete` — the reference runs `one-time-code` on the FIRST box only and `off` on the other five (the standard OTP convention); the clone had it on all six. The dialog-button Tab-vs-click pair (suggestion 1) found NO drift — both sites' dialog buttons carry the byte-identical `focus-visible:ring-1 ring-ring` family, no ring on mouse clicks, the same visible layers on real Tab (the v19 `focusVisible:true` methodology was correct; a click on an empty-form Save moves focus to the first invalid input via native validation on BOTH sites — the class attribute is the reliable behavioral arbiter). The verify-email inputs audit (suggestion 2): structure/geometry/behavior all match (main/h2/form, 40×44 gap-6, inputmode numeric, auto-advance, backspace-retreat, paste-distribute-to-last); the clone's aria-label boxes + arrow-key navigation stay as documented supersets (the reference's inputs are unnamed and arrow-inert). Swept clean: mobile-nav R1–R4 (20th — Tailwind v4 pins hold), data drift (20th), the SEO pair, the v24 auth census (the three-family table), the v25 fixes re-verified live (submit ring #09090b, 404 ring #64748b, body white), the VLM login pair (IDENTICAL) — 108/155/35 green (1 new e2e + 1 extended; observation: the reference's register endpoint started demanding "Security verification" after ~2 synthetic registrations — a platform anti-automation gate that may rate-cap future live verify-state probes) |
| 2026-10-09 | Session 53 — parity iteration v27 (`docs/remediation-plan-v27.md`) | **One DOM-verified fix from the dialog X-close button's first keyboard/hover-family measurement**: the reference's X runs the shadcn ghost-icon base (`focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring` — a 1px #0a0a0a ring on REAL Tab, the same family as the dialog Cancel/Save buttons) + `hover:bg-accent hover:text-accent-foreground` (the icon shifts #0a0a0a → #171717 on hover); the clone's hand-written `DialogCloseButton` had drifted to `focus:outline-none focus-visible:ring-2` (2px) with no hover text — one class string in `dialog.tsx` covers all four dialogs, pinned by the extended v9 X-close spec (class-attribute assertions). The session-53 suggested surfaces ALL swept clean on first measurement: prefers-reduced-motion (both sites animate the full 500ms sheet slide-in + 1s spinner under `reduce` — zero reduced-motion rules in either CSSOM), print/overscroll (white body, `auto` overscroll, zero print rules), scrollbar styling at the dialog overflow (native `auto` scrollbars on both). Extensions also clean: dark mode (both stay light), the app-surface real-Tab focus rings (three families all matching), the filter triggers + search inputs (byte-identical). Probe lessons: the clone's Radix dialog TRAPS focus (the reference's plain-div dialogs do not) so the walk-to-X stop counts differ — dispatch a keydown Tab inside one eval to reach the clone's X; the with-server one-invocation pattern boots pages against a dying server (the v16 zero-state renders honestly — data probes need one invocation). Swept clean: mobile-nav R1–R4 (21st — Tailwind v4 pins hold), data drift (21st), the SEO pair, the v26 fixes re-verified live — 108/155/35 green (1 e2e extended) |
| 2026-10-09 | Session 55 — parity iteration v28 (`docs/remediation-plan-v28.md`) | **THREE fixes, headlined by a whole missing surface (G3)**: the reference's card-body click opens a read-only **Budget Item Details sheet** — measured across all three types + both viewports (overlay `fixed inset-0 z-50` forest 50% + blur(8px); panel bottom-anchored full-width `rounded-t-3xl` max-h-85vh at mobile / centered `max-w-lg` 512px `md:rounded-2xl` at desktop; sticky header + the X-close family; centered summary with type/classification pill badges — type color at 12.5% alpha, `text-2xl` name, `text-4xl` type-colored amount; the tinted classification block with a SEPARATE details-copy map — need 'Essential expenses like rent, utilities, and groceries', want 'Discretionary spending like entertainment and dining out', savings 'Savings, investments, and future planning'; icon-led fact rows calendar/refresh-cw/tag/credit-card?/dollar-sign + the taller Notes? variant with file-text; the Created/Last Updated grid footer) — built as `item-details-dialog.tsx` + the store's `details` modal slot + the card's guarded onClick (clicks inside buttons/menus skip the sheet — the reference behaves the same). (G1) the card badges' hover family: the reference's badges tint to rgba(245,245,245,0.8) on a REAL CDP hover (`hover:bg-secondary/80` + 150ms transition) — the clone pins the exact computed rgba via `.zb-badge-hover` in globals.css because the direct TW4 utility computes as oklab `lab(96.5375 0 0 / 0.8)` (the v7 G6 drift class). (G2) the expense-card footer Edit/Calculate buttons' keyboard family: `focus-visible:ring-1` + the Edit's `hover:text-accent-foreground` (the clone's hand-written strings had NONE — the UA default outline rendered on REAL Tab). Swept clean (session-55 suggestions): the one-pass button census, the avatar chip (non-interactive on both), the toast close buttons (the reference renders NO toasts on add-success — viewport heights [32,32] at 200ms/900ms/3.4s), mobile-nav R1–R4 (22nd — Tailwind v4 pins hold), data drift (22nd — after an add-then-delete probe cycle restored the census), the SEO pair — 108/158/35 green (3 new e2e; NEW `16-item-details.png` screenshot; probe lessons: synthetic mouseenter NEVER engages :hover — REAL `agent-browser mouse move` does; the reference's dialogs do NOT close on Escape; its number-input keeps an EMPTY value, '0.00' is the placeholder) |
| 2026-10-10 | Session 57 — parity iteration v29 (`docs/remediation-plan-v29.md`) | **One DOM-verified fix from the net-worth view's FIRST interactive-family census** (the session-57 suggested surface): the asset/liability card TYPE labels — the reference's are Badge-base DIVs (rest bg `rgb(243,244,246)` / text `rgb(55,65,81)`, REAL-hover tint `rgba(245,245,245,0.8)` over 150ms — the v28 G1 family on a surface never diffed); the clone's static spans computed TW4 oklab (`lab(96.1596 …)`/`lab(27.1134 …)`) with no hover family — fixed on both label strings in `net-worth-view.tsx` via the hex pins `bg-[#f3f4f6] text-[#374151]` + the existing `.zb-badge-hover` class. The census also swept clean: tab triggers + tablist (computed byte-identical), the Add gradient buttons, card containers (cursor auto on both — the reference's asset-card click opens NOTHING), the action dropdown menus (byte-identical), the breakdown-row hover (INERT on both — each site's inline background-color overrides its own hover class). The OTHER session-57 suggestions verified: the details sheet's keyboard semantics (the reference: NO focus/trap/role/Escape — its Tab walk tours the whole page; the clone's Radix initial-focus→X + trap + Escape is the documented superset — Chrome renders the pinned X ring on open, the superset's visible signature); the VLM details pair (both flags DOM-explained); the ellipsis-Edit vs footer-Edit (the SAME 14-field dialog — no finding). The mobile net-worth VLM pair's three flags all DOM-arbitrated no-change: the 1-col stacking = the v4 data-fit superset RE-VERIFIED by a live 2-col DOM experiment (the seeded $65,300/$311,250 glyphs need 152/169px vs the 107px cells; the reference's own $25,000 already micro-overflows 152/144), the trend icon inset 48px on BOTH, the tab icons the v14 circle-arrow pair. Mobile-nav R1–R4 (23rd — Tailwind v4 pins hold), data drift (23rd — reference read-only), the SEO pair — 108/158/35 green (the networth spec's label assertions extended; lessons: the reference's tab triggers ignore synthetic clicks — real ref clicks only; VLM glyph claims at 16–24px are unreliable — arbitrate with computed geometry; find the clone's dialog X by its sr-only Close textContent) |
| 2026-10-10 | Session 59 — parity iteration v30 (`docs/remediation-plan-v30.md`) | **Zero production-code drift — the iteration PINS the newly-measured semantics** (3 new e2e). Every session-59 suggested surface swept clean with first-time REAL-hover/keyboard measurements: the dashboard guideline rows (rest byte-identical; NO hover family on either site — the inline tints are static), the quick-action card buttons (rendered parity: v4's `scale: 1.1` property vs the reference's `transform: matrix(1.1,…)` both render 40→44px; `hover:shadow-lg`'s visible layer pair byte-identical behind v4's extra TRANSPARENT lead layers; the Plus fade 0.5→1 identical), the savings card family (byte-identical; the details sheet opens on savings-card click — cursor pointer on both), the net-worth tablist's arrow-key semantics (the reference IS Radix: the identical RovingFocusGroup attribute set — container tabIndex=0, both triggers -1 fresh, `data-radix-collection-item`; ArrowRight → focus move + automatic activation + roving-tabindex update, identical on both), the details sheet's keyboard semantics at MOBILE (geometry byte-identical x=0/w=390/max-h 717.4px; the reference's no-trap bug confirmed at the bottom-sheet breakpoint — its mobile Tab walk tours the underlying page's Edit/Calculate buttons; the clone's Radix trap holds). SEO DEEPENED: the full head-metadata census — description/OG/Twitter byte-identical, the reference's `/manifest.json` endpoint serves EMPTY (the clone's webmanifest is the superset). Pins added: G1 the details sheet's keyboard semantics (initial focus X + Tab containment + Escape, desktop AND mobile + the mobile geometry) and G2 the tablist's roving arrow-key contract (focus/aria-selected/roving-tabindex/panel switch) — TDD with pin-sanity mutations. Mobile-nav R1–R4 (24th — Tailwind v4 pins hold), data drift (24th — read-only), VLM pairs (dashboard + mobile details: both IDENTICAL) — 108/161/35 green; lessons: bash mangles template-literal probes inline (persist `$`-bearing probes as files); a static both-triggers-`tabIndex=-1` + container `tabIndex=0` is the CORRECT Radix fresh state (measure the behavior, not the old active=0 pattern); read v4's scale via `.scale` + the rendered rect, `.transform` reads `none` |
| 2026-10-10 | Session 61 — parity iteration v31 (`docs/remediation-plan-v31.md`) | **The donut's keyboard semantics + the classification tiles' fresh roving state** (3 new e2e, both DOM-verified on the two live sites, TDD with pin-sanity mutations). G1 — the recharts 3↔2.15 drift trio: (a) the chart surface stamped `tabIndex=0` + `role="application"` (recharts 3's `accessibilityLayer` defaults ON, `?? true`) while the reference's surface is INERT (no attribute, no role) — an extra tab stop rendering the browser's unpinned 5px auto ring; (b) the tooltip's default content carrying `role="status"` + `aria-live="assertive"` (the reference's renders neither); (c) recharts 3 REMOVED 2.15's `attachKeyboardHandlers` pie roving — the reference's layer g (tabIndex=0 on BOTH versions, `rootTabIndex: 0`) roves sector focus: ArrowLeft `++n % len` forward, ArrowRight `--n < 0 → len-1` BACKWARD (the first ArrowRight from a fresh pie focuses the LAST sector — the reference's quirk), Escape blurs + resets, alt-arrows ignored, no preventDefault. Fixed: `<PieChart accessibilityLayer={false}>` + `usePieKeyboardParity` (an onkeydown DOM property on the donut wrapper — delegation via bubbling, immune to the ResponsiveContainer mount race). G2 — the reference's older Radix ties the fresh roving tabindex to the CHECKED state (container 0 + checked radio 0 = two stops; Radix 1.4.8's fresh state renders all radios −1) — fixed with `tabIndex={selected ? 0 : -1}` on the tiles' RadioGroupItem (equal to the roving tabindex in every reachable state: checking always follows focus). NO findings: the filter selects' open-state arrow semantics (identical Radix listbox roving, no wrap) and the form dialogs' full Tab order (the 14-field census byte-identical; the reference's 1×1 native-select shadows are not stops on either site). Measured lesson: a REAL Tab into a Radix roving group lands on the CHECKED item (the container's entry focus forwards instantly — activeElement never reads the container). Mobile-nav R1–R4 (25th — Tailwind v4 pins hold, both sites), data drift (25th — reference read-only), the SEO pair (full head census byte-identical + the superset webmanifest), the VLM dashboard + add-dialog pairs (all flags DOM-explained) — 108/164/35 green; lessons: a 2.5s post-nav settle can read a still-loading route as non-overflowing (the /networth 390-vs-464 artifact — re-measure at 6s); the dialog X finder must scope to the topmost fixed overlay; SVG elements without a tabindex attribute read `.tabIndex === -1` — distinguish attribute-absent from attribute -1 |
| 2026-10-10 | Session 63 — parity iteration v32 (`docs/remediation-plan-v32.md`) | **The calculator row actions' focus-visible ring family + the breakdown rows' aria-expanded superset pinned** (1 new e2e + the S1 pins, DOM-verified on the two live sites, TDD with pin-sanity mutations). G1 — the reference's 32px calculator line-item row actions (Edit/Delete) carry the shadcn focus family (REAL-Tab-measured: the 1px #0a0a0a ring shadow with the white lead layer + v3's outline-none form `solid 2px rgba(0,0,0,0)` + offset 2) while the clone's raw `h-8 w-8 … hover:bg-accent` buttons rendered the browser-default `outline: auto` — fixed with `focus-visible:ring-1 focus-visible:ring-ring` inline + a NEW globals.css pin `.zb-row-action:focus-visible` (Tailwind v4's `outline-none` utility emits `outline-style: none` ONLY — v3's `outline: 2px solid transparent; outline-offset: 2px` form must be pinned in CSS; the same trap family as the shadow-scale shift and the hover media-gate). The populated-calculator Tab census is byte-identical on both sites (4 stops: X 36 / Add Item 110 / Edit 32 / Delete 32; the row actions are Tab stops inside their opacity-0 hover-reveal container — the reveal is hover-ONLY, never focus; the reference's dialog EXITS to the page after the last stop vs the clone's Radix wrap = the documented trap superset). S1 — the breakdown rows' `aria-expanded` (accurate state; the reference's have none) measured, KEPT as a deliberate a11y superset (the aria-label family), and pinned so a future sweep doesn't 'fix' it away. NO findings: the net-worth dropdown menus' keyboard contract (byte-identical: click-open container focus / Enter-open first item / arrow roving with data-highlighted / CLAMPED at the ends / Home-End / NO typeahead / Escape returns focus to the trigger) and the breakdown accordion's arrow semantics (inert on both, Enter expands both, Escape collapses on neither). Documented: the reference's calculator row delete is IMMEDIATE — the clone's inline confirm is the "unconfirmed deletes fixed" superset. Mobile-nav R1–R4 (26th — Tailwind v4 pins hold, both sites), data drift (26th — reference read-only, verified before + after the probe cycles), the SEO pair (head census byte-identical), the VLM dashboard + calculator pairs (both flags DOM-explained: superset #3, the Radix X-focus ring) — 108/165/35 green; lessons: transition-colors' v4 property list includes outline-color — settle ≥350ms before reading focus chrome (an immediate read catches the transparent settle mid-flight in oklab form); form fill finders anchor on LABEL text or DOM order, never `placeholder*=name`; a calculator add/delete probe cycle recalculates the parent amount (restore the dev db afterward — the seed's natural-key upsert does NOT); the reference's sheet detector matches STRUCTURE (fixed panel + nav links + body lock), not background color |
| 2026-10-10 | Session 65 — parity iteration v33 (`docs/remediation-plan-v33.md`) | **The verify-email code inputs' focus family + the toast announcer pinned** (1 new e2e + the S1 pin, DOM-verified on the two live sites, TDD with pin-sanity mutations). G1 — the reference's focused 40x44 code inputs render the 2px zinc-950 ring (`box-shadow: rgb(255,255,255) 0 0 0 0, rgb(9,9,11) 0 0 0 2px`) with NO border tint (the border stays #e4e4e7 — the ring alone signals focus) and the reference AUTO-FOCUSES the first box when the verify state lands, while the clone rendered an invented slate-400 border tint, no ring, and no auto-focus — fixed with the register-input precedent idiom `focus:shadow-[0_0_0_0_#fff,0_0_0_2px_#09090b] focus:outline-none` + `autoFocus={i === 0}` (the reference's own register inputs carry the SLATE family — its code inputs carry the ZINC family; each surface measured separately). S1 — the toast's announcement semantics measured and pinned: the clone's live toast announces via Radix's hidden `role="status" aria-live="assertive"` portal (`Notification Line item added`) within its 1-second mount window, while the reference's toast viewports are semantic-less `pointer-events: auto` divs (the standing R1 burger-blocker root cause) and its live toasts never fire on item/line-item saves or deletes (measured). NO findings: the line-item sub-dialog's focus traversal (13-stop census + REAL-Tab walk byte-identical INCLUDING the native date segments — each `<input type="date">` is a 4-stop walk; the two deltas are the documented Radix supersets), the sub-dialog's select triggers' focus chrome (the 1px ring IS present as the FOURTH box-shadow layer — v4's composition buries it behind three transparent placeholders; a truncated read fabricated a missing-ring finding), the register inputs + verify submit + Resend + Back (all pinned or raw-default-matched), the bundle pass (the clone's dashboard: 12 chunks 1,104KB raw/338KB gz vs the reference's 1,060KB/317KB one-bundle + a 214KB dev-only badge.js — wire-weight parity with a route-split superset). Mobile-nav R1-R4 (27th — Tailwind v4 pins hold, both sites), data drift (27th), the SEO pair, the VLM dashboard + verify pairs (both flags DOM-explained: superset #3, the dev-code hint box) — 108/166/35 green; lessons: v4's ring composition puts the visible ring in the FOURTH box-shadow layer behind three transparent placeholders — a truncated read fabricates a missing-ring finding; persistent agent-browser sessions keep their LAST viewport (re-assert before VLM pairing); the clone's Radix DialogContent is NOT inside a div.fixed (overlay and content are portal SIBLINGS — anchor with closest('[data-state=open],[role=dialog]')); the reference's plain-div dialogs IGNORE Escape; the reference's register form is a STATE on /login (/register 404s) |
| 2026-10-10 | Session 67 — parity iteration v34 (`docs/remediation-plan-v34.md`) | **Zero production-code drift — the session-69 suggested surfaces measured for the first time and PINNED** (2 new e2e, TDD with pin-sanity mutations). S1 — the forgot-password state's focus walk: exactly THREE app stops in order (Back to sign in → Email → Send reset link), NO auto-focus on landing (focus stays on the body — unlike the verify state's first-box auto-focus), the email input's focused chrome = the v13 slate family, the submit = the v25 zinc family (focus-VISIBLE-gated — programmatic focus never engages it; programmatic-focus-then-real-Tab is the working probe pattern), the Back button raw (browser-default outline) — all byte-identical on both sites, pinned by login-parity. S2 — the calculator frequency Select's listbox keyboard contract: the same Radix combobox family (role=combobox + aria-controls + the same 6 options in the same order), fresh-open focuses the SELECTED option rendering the accent highlight (rgb(245,245,245) — :focus-driven via SelectItem's focus:bg-accent), arrows rove CLAMPED at both ends (no wrap), Home/End jump, NO typeahead (both sites), Escape closes the POPUP ONLY (focus → trigger, the sub-dialog stays), Enter selects — pinned by the calculator spec with Playwright's real page focus. D1 — the README's structure/commands sections still said 165 e2e after v33's 166 (fixed to 168). S3 — the API error-tier audit clean (401/400/404/429/403/409 consistent, the client layered network → non-JSON → envelope, every Prisma query userId-scoped). **The big probe lesson: the UNFOCUSED-HEADLESS-WINDOW :focus artifact** — an eval that DOM-clicks a Select trigger open reads document.activeElement = the selected option while element.matches(':focus') is FALSE and document.querySelector(':focus') returns NOTHING (the headless page's OS-level window focus was lost after a navigation without real key presses); the first fresh-open comparison fabricated a 'missing highlight' finding — GATE every :focus-computed read on document.hasFocus() (a real 'press Shift' re-focuses the page); Playwright is immune (its pages hold real focus). Also: [tabindex=-1] is an INVALID unquoted CSS selector (an identifier cannot start with '-' then a digit — quote it), and the tool-result display pipeline eats [h] and [m] sequences (lesson 44's family) — DISPLAY-ONLY (command transport and file contents are never touched; a repr read fabricated a 'file mangled' conclusion mid-session — arbitrate with char codes). Mobile-nav R1-R4 (28th — Tailwind v4 pins hold, both sites), data drift (28th — reference read-only), the SEO pair, the VLM dashboard + forgot pairs (dashboard one flag DOM-explained = superset #3; forgot IDENTICAL, zero flags) — 108/168/35 green |
| 2026-10-10 | Session 70 — parity iteration v35 (`docs/remediation-plan-v35.md`) | **The item-card action menus' open-state focus chrome — TWO drifts found and fixed + three pins** (3 new e2e, TDD with pin-sanity mutations, all first-time REAL-key measurements on the two live sites). G1 — the action-menu DELETE item's FOCUSED text color: the reference's `focus:text-accent-foreground` outspecifies its `text-red-600` when focused (the highlighted Delete renders rgb(23,23,23) dark text over the accent bg — red only at REST), while the clone's v5-era `focus:text-[#dc2626]` hex migration kept it RED when focused; fixed by removing the override on all three Delete items (income/savings card + both net-worth cards — the base DropdownMenuItem cascade then matches the reference exactly). G2 — the menu TRIGGERS (the 36×36 hover-revealed kebabs) lacked the reference's shadcn `focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring` family entirely (REAL-Tab into them rendered box-shadow: none vs the reference's 1px #0a0a0a three-layer ring) — the clone's DropdownMenuTrigger is the RAW Radix primitive, not the shadcn Button; fixed by adding the ring family inline on all three triggers. The rest of the menu contract byte-identical: fresh-open click → the menu CONTAINER / Enter → the FIRST item; arrows rove with the accent highlight; ArrowUp-from-container lands on the LAST item (the Radix convention); Home/End jump; Tab trapped; Escape → trigger; items 118×32; the trigger's rest opacity-0 hover-reveal on both. S2 — the dashboard quick-action Add Item's focus-visible FOUR-layer composite (white 0px lead + 1px #0a0a0a ring + the gradient family's two ambient layers) byte-identical on both sites, first-time measured, pinned at the dashboard instance. S3 — the `?from_url` deep-link redirect: the reference's login HONORS the param (measured live: /login?from_url=/income lands on /income), the clone byte-matches, pinned (+1 e2e); the 404's Go Home link-vs-button documented as a SUPERSET (the reference's is a button that client-navigates; the clone's is a real Link — crawler-followable, click-identical; the title derivation byte-identical). Probe lessons: compare the SAME open path across sites (click-open vs Enter-open land focus differently on BOTH — a cross-path comparison fabricated a phantom landing difference); the genuine ArrowUp-from-container contract is LAST-item (an Enter-open-then-ArrowUp reads a clamped first-item and contaminated the first S1 draft — the TDD RED caught it); a wide sed on a class substring strips MORE than intended (the mutation-B strip also removed the expense-card buttons' ring family — caught by the full-chain re-run and restored; verify changesets with git diff before shipping); a bare .click() does NOT open Radix's DropdownMenuTrigger (dispatch pointerdown first); a 'rest' style read after a REAL-Tab sequence is still a FOCUSED read — blur first. Mobile-nav R1–R4 (29th — Tailwind v4 pins hold, both sites), data drift (29th — reference read-only), the SEO pair, the VLM dashboard + menu-open pairs (dashboard flags DOM-explained = superset #3 + demo data; menu-open IDENTICAL, zero flags — the G1 red-vs-dark text is below VLM resolution, the DOM measurement is the authority) — 108/171/35 green |
| 2026-10-10 | Session 71 — parity iteration v36 (`docs/remediation-plan-v36.md`) | **The session-72 suggested-surface sweep — ZERO production-code drift, three surfaces measured for the first time and pinned** (3 new e2e, TDD with pin-sanity mutations — every pin verified to FAIL under its mutation). Surface A — the action-menu HOVER-highlight family (REAL `agent-browser hover`, both sites): hovering a menu item moves DOM focus to it (Radix's pointer-driven roving — SYNTHETIC mousemove/mouseenter events do NOT trigger it; the first probe fabricated 'the reference ignores hover' until the real-hover retry) and renders the SAME accent family as keyboard focus (bg rgb(245,245,245) + text rgb(23,23,23) — the hovered Delete NOT red, the v35 G1 cascade extended to the hover path); pointer-off → focus returns to the CONTAINER, both items to rest (Delete red again), the menu survives; pinned (S1, tokens.spec). Surface B — the filter Selects' listbox keyboard contract (the /income instances; v34 covered the calculator sub-dialog only): fresh-open via click AND Enter both land focus on the SELECTED option with the accent highlight; arrows rove CLAMPED at both ends; Home/End jump; Escape closes the popup ONLY (focus → the trigger, the page unaffected); Enter selects + updates the trigger text; pinned (S2, items.spec) with the fixture-restore discipline. Surface C — the items-view Tab-order census (first-time PAGE-level walk; v33 covered the sub-dialog): the sequence is exactly the five nav links → Add Income → the search input → the category combobox → the frequency combobox → the card kebabs (one per card, DOM order) — the same sequence the reference walks MINUS its Base44 platform badge (#base44-edit-badge 'Edit with Base44' + its 18×18 Close button, fixed bottom-right z-index 999999 — PLATFORM chrome, not app UI; exclude from tab-order and VLM comparisons); pinned (S3, items.spec). **Superset #7 documented + pinned from the walk: the kebab trigger's keyboard reveal** — the reference's 36×36 trigger stays INVISIBLE (opacity 0) when keyboard-focused AND when its menu is keyboard-opened (:focus-visible matches, the ring computes, but the element renders nothing — a keyboard user loses the visual focus at that stop); the clone's day-one `focus-visible:opacity-100` + `data-[state=open]:opacity-100` keep it visible. Also documented: the clone's filter comboboxes/search input carry invisible aria-labels (day-one a11y supersets — the reference's controls are value-named only); the reference's CLOSED Select trigger persists aria-controls (a Radix-minor-version detail — both carry the matching attribute while OPEN; the id format differs by React useId generation, cosmetic). Probe lessons: a blur does NOT reset the sequential focus navigation position (Chromium resumes from the last focus — walk past the wrap); Radix Select's post-open focus landing is ASYNC — a racing key press hits the trigger instead of the option (the S2 fixture-restore failed exactly there; interleave a toBeFocused() between presses). Mobile-nav R1–R4 (30th — Tailwind v4 pins hold, the mobile menu works, both sites), data drift (30th — reference read-only, verified before + after), the SEO pair, the VLM dashboard + filter-open pairs (all flags DOM-explained: superset #3 + demo data + the platform badge) — 108/174/35 green |
| 2026-10-11 | Session 72 — parity iteration v37 (`docs/remediation-plan-v37.md`) | **The session-76 suggested-surface sweep — ZERO production-code drift, three surfaces measured for the first time and pinned** (3 new e2e, TDD with pin-sanity mutations — every pin verified to FAIL under its mutation). Surface A — the filter Select TRIGGERS' focus-visible family (the CLOSED trigger's keyboard chrome — the v36 census walked PAST the stops without asserting them): a REAL Tab onto the closed category-filter trigger engages :focus-visible and renders the 1px #0a0a0a ring layered over the ambient rgba(0,0,0,0.05) shadow — the border stays UNTINTED rgb(229,229,229), the geometry unchanged (216×36); pinned (S1, items.spec) with the mutation sanity (stripping the SelectTrigger's focus:ring-1 focus:ring-ring FAILS the pin). **O1 documented (not drift)**: the full box-shadow STRINGS differ in their invisible lead layers — the reference's v3 three-slot construct (a white ring-offset lead) vs the clone's v4 five-slot construct (four transparent leads); every lead is a 0px-spread shadow, invisible by construction, the VISIBLE layers byte-identical (the v11 shadow-scale precedent — the pins assert the visible layers, never the lead count). Surface B — the search input's focus + typing contract: the REAL-Tab focus family (the same ring + ambient, border untinted, 447×36, transparent bg) + the REAL-key behavior — an exact-name match narrows the card list + recomputes the header ('Income 1 items · $5200.00'), a no-match string swaps to the EMPTY state (the h3 'No income items yet' — the reference's card titles are h4), clearing restores the full list; pinned (S2, items.spec) with the mutation sanity (stripping the Input's focus-visible:ring-1 focus-visible:ring-ring FAILS the pin). Surface C — the /expenses payment-method filter (the third Select, first-time live measurement): the trigger chrome (216×36, 'All Payment Methods') + its DYNAMIC option derivation (the reference's own list carries only its All option — its demo items hold no paymentMethod values, a data-level difference; its edit dialog carries the 'payment method' field, verified read-only — the model matches, the clone's conditional item.paymentMethod chip is the same model) + the Credit Card round-trip (the trigger text updates, the cards narrow to Entertainment+Groceries, the header recomputes '2 items · $385.00') + the reset (3 cards, '3 items · $2235.00'); pinned (S3, items.spec) with the mutation sanity (emptying the paymentMethods derivation FAILS the pin). Also re-verified on the reference: the expense cards' action family is the INLINE hover-revealed Edit (77×32) + Calculate (110×32) buttons (the v8-pinned family; the kebab lives on the income/savings cards). Probe lessons: the reference's card titles are h4 and its empty-state heading an h3 (an h3-only card census fabricated 'no cards' readings until the h4 selector caught them — query the title tag the view renders); agent-browser keyboard press Backspace does NOT register in the reference's focused search input (six presses, the value unchanged) and the CLI's fill '' dispatches no input event — clear React-controlled inputs in probes via the native value setter + a bubbled input Event (Playwright's fill('') is unaffected — it drives proper input events). Mobile-nav R1–R4 (31st — Tailwind v4 pins hold, the mobile menu works, both sites), data drift (31st — reference read-only, verified before + after; the PM probe Escape-closed without selecting, the edit-dialog probe opened + Escape-closed without saving), the SEO pair (robots + sitemap + the head census; the reference's sitemap capitalizes its app-route URLs /Income /Savings — measured live, documented; the clone mirrors its own lowercase routes, the v21 decision), one VLM pair (/expenses + the PM filter open — all five flags data-explained: the card count, the extra tags + footer chips + the two extra dropdown options = the clone's seed carrying paymentMethod values, the avatar letter) — 108/177/35 green |
| 2026-10-11 | Session 78 — parity iteration v43 (`docs/remediation-plan-v43.md`) | **The drill-down EXPANDED-state census + the static-chevron and hover-rgb fixes — THE FIRST PRODUCTION-CODE CHANGE SINCE v42** (3 new e2e, TDD with three pin-sanity mutations). The surface (the session-92/93 queue's two items): the drill-down's expanded bands measured live on BOTH sites at 640×960 (exp-census-v43.mjs + exp-detail-v43.mjs + exp-rotate-v43.mjs + hover-v43.mjs) — the per-row chrome BYTE-IDENTICAL at every level (the section 48/8px/-8px/8px radius/14px chevron, the category 28/"6px 12px"/inline rgb(249,250,251)/6×6 dot/12px-500-forestDark, the sub 24/"4px 8px"/rgb(250,250,250)/12px-400-gray/4×4 dot at 0.6, the item 24/"4px 8px"/12px rgb(156,163,175)/2×2 dot at 0.4/120px truncate, the footer 29/"6px 12px"/border-t) with the expansion arithmetic 324→441→495 and sw 640 fully expanded; the heights differ only by DATA (the seed's 2 categories vs the reference's 1). TWO PARITY FIXES: (F1) the chevrons — the clone's v4 rotate-180 rendered `rotate: 180deg` (0.15s) while the reference's are STATIC (rotate: none, transition "all" 0s at BOTH levels — Tailwind v4's rotate-* emits the `rotate` PROPERTY, not `transform`; a transform: none reading is meaningless on v4) — both chevrons stripped of rotate-180 + transition-transform, the aria-expanded a11y superset KEPT; (F2) the section-row hover — the v4 named palette (hover:bg-gray-50) computed lab(98.2596 -0.247031 -0.706708) where the reference's engaged v3 gray-50 computes rgb(249,250,251) — the named-palette trap LIVE in a hover state (the section button carries no inline bg) — fixed hover:bg-[#f9fafb]. The category rows' hover is inert on BOTH sites (the inline bg overrides — v29, DOM-identical). The queue's summary-card item RESOLVED: static on both (the same gradient, the same rgba(26,58,46,0.3) 0 20 60 shadow, cursor auto — no interaction states exist). THREE PIN-SANITY MUTATIONS VERIFIED TO FAIL: the restored rotate-180 → the rotate pin fails ("180deg" ≠ "none"); the reverted hover hex → the rgb pin fails (lab ≠ rgb); the sub-row py-1→py-2 → the census pin fails (503 ≠ 495). Probe lessons: read the CSS `rotate` PROPERTY for v4 rotations (transform never shows rotate-*); a saved DOM node goes stale across a React re-render (computed styles of detached nodes return empty/none — re-query after every state change); the named-palette lab() trap lives in HOVER states too; VLM image-order attribution is unreliable (the reference's own Base44 badge was flagged as "on the clone" — DOM-verified before it counts). Mobile-nav R1–R4 (37th — Tailwind v4 pins hold, the mobile menu works, both sites), data drift (37th — reference read-only, verified before + after), the SEO pair, one VLM pair (the EXPANDED drill-down post-fix — all three flags in the known classes: the active-highlight superset #3, the avatar letter, the reference's Base44 badge misattributed) — 108/209/35 green |
| 2026-10-11 | Session 79 — parity iteration v44 (`docs/remediation-plan-v44.md`) | **The drill-down expansion ANIMATION + the chevron GLYPH swap — the first production-code change since v43** (5 new e2e, TDD with five pin-sanity mutations). The surface (the session-95/96/97 queue): the drill-down's expanded state at the REMAINING viewports (390/1280) + the donut legend's geometry/interaction, measured live on BOTH sites (exp-vp-v44.mjs + legend-v44.mjs + collapse-ref-v44.mjs + band-mount-v44.mjs + chev-glyph-v44.mjs). TWO PARITY FIXES: (F1) **the expansion ANIMATES on the reference** — its card ramps ~200ms in BOTH directions (324→346→364→387→398→405 on the expand; 459→429→384→359→339→324 on the collapse), mid-collapse its band reads INLINE height: 25.5455px (a per-frame JS tween, not a CSS transition) with the end state height:auto/opacity:1, and the section band UNMOUNTS after the collapse animation — while the clone mounted/unmounted instantly (324→441 at the first sample, zero in-flight frames); fixed with the Collapse wrapper (the grid 0fr↔1f technique + @starting-style for the entry + the onTransitionEnd delayed unmount — the collapsed DOM returns to exactly the pre-fix node tree, the accordion count-0 pins hold; the render-phase mount flip uses the adjust-state-during-render pattern, the unmount is a React event handler — no setState-in-effect); (F4) **the chevrons SWAP GLYPHS** — lucide-chevron-down collapsed ↔ lucide-chevron-up expanded at BOTH levels (section 14px w-3.5, category 12px w-3), rotate: none at EVERY state — the v43 "static" finding was correct-but-incomplete: the flip is the ICON, not the transform, and **a computed-style census cannot see a glyph swap — read the svg's class** (the standing VLM pair flagged it, the DOM verified it — the opposite of v43's misattributed Base44 badge). PINS: the 390 census (the chrome byte-identical, the mobile indentation ml 40/mt 8, the clone's sw 390 fully expanded — the superset; the reference reads 395, its own overflow), the 1280 census (the 304px narrow column, the section label's 2-line WRAP — labelH 40 on BOTH sites, the v42 56px row explained: width-driven), the donut legend census (h 64/pad 12/radius 8/label 16-500/amount 16-700-classcolor/pct 12-gray/dot 16×16-r4/icon 16/gap 12/mt 24 — and the hover INERT on both sites: the queue's legend-interaction item RESOLVED, no interaction states exist). FIVE PIN-SANITY MUTATIONS VERIFIED TO FAIL: the zeroed duration → the in-flight sample pin fails; the removed @starting-style → the entry pin fails; the legend p-3→p-4 → the census pin fails (64→72); the sub-row py-1→py-2 → the 390 census pin fails; the reverted glyph swap → the glyph pin fails. Probe lessons: a height-curve census catches what the end-state census cannot (sample DURING the transition, both directions); the grid 0fr→1f technique + @starting-style animates height 0↔auto with NO JS frame games; a computed-style census is blind to GLYPH swaps — read the svg class list; the VLM pair catches glyph-level flags the geometry census misses (DOM-verify before counting). Mobile-nav R1→R4 (38th — Tailwind v4 pins hold, the mobile menu works, both sites), data drift (38th — reference read-only, verified before + after), the SEO pair, the VLM pair (one REAL flag — the F4 glyph swap) — 108/214/35 green |
| 2026-10-11 | Session 80 — parity iteration v45 (`docs/remediation-plan-v45.md`) | **The shadow-scale sweep + the items-view card grid census + the calculator row hover — a PIN-ONLY iteration** (7 new e2e, TDD with five pin-sanity mutations; NO production-code change — the measured chrome was already at parity, the pins lock it). The surface (the session-99/100 queue): the items-view card grid at 1280, the calculator row's hover, the category-level animation — measured live on BOTH sites (items-card-v45.mjs + calc-row-v45.mjs + the tag/hover driver steps). THE V45 DISCOVERY: a SYSTEMIC v3↔v4 divergence in the computed box-shadow composition — every live `shadow-*` utility's VISIBLE layers match on both sites (the `--shadow-sm` theme pin is load-bearing: v4 RENAMED the scale, its native shadow-sm = v3's "shadow"; the pin restores `0 1px 2px 0 rgb(0 0 0 / 0.05)` — measured matching) while the LEAD layers diverge by construction (v4's 5-slot composition emits 4 transparent leads vs v3's 2 — invisible, the accepted v10/v25 class: "v4's transparent lead layers paint nothing"); the md/lg/xl/2xl values were NOT renamed and were UNPINNED — v45 pins the md/lg/sm/2xl sites (the calculator row's hover shadow-md, the quick-action card's hover shadow-lg, the action buttons' rest shadow-md, the slate/Google buttons' shadow-sm, the login panel's shadow-2xl) as the regression net against a future Tailwind upgrade changing the scale. PINS: the items-view card census at 1280 (the grid 960 = the rail 256 + the content column 1024 − the p-8 64 — the SAME arithmetic on both sites, 3 cols × 309.328, gap 16; the card 309/pad 20/radius 12/border/rest shadow rgba(0,0,0,0.04) 0px 2px 8px 0px/transition all 0.2s; the title row gap 8/dot 8×8/16-600; the income kebab 36×36/opacity 0; the expense action row top 12/right 12/gap 8/btn 32/padX 12/12px; **the card's REAL hover INERT on BOTH sites** — the inline boxShadow beats the hover:shadow-lg utility, the v29 inline-beats-class family — while the action row REVEALS), the calculator row census + REAL hover (the panel 768@1280/608@640, the row 720/560, pad 16/radius 12/border/rest-shadow none/transition all 0.15s; under a REAL hover the shadow-md's visible layers + the action reveal on both sites — the row carries NO inline shadow, its hover is LIVE, unlike the cards; the reference's RENT calculator is the only one of its four expense cards with line items), the category-level band animation at the NESTED level (the v44 F1 extension: in-flight frames both directions, 441→495→441). FIVE PIN-SANITY MUTATIONS VERIFIED TO FAIL: the card inline 0.04→0.08 → F1a fails; the grid gap-4→gap-6 → F1a+F1b fail; the row hover:shadow-md removed → F2a fails; the quick-action hover:shadow-lg removed → F3b fails; the slate shadow-sm removed → F4 fails. Probe lessons: the v3↔v4 shadow LEAD-layer divergence is systemic but invisible — census the VISIBLE layers with toContain and pin them as the regression net; a REAL `.hover()` (Playwright/agent-browser) is the ONLY way to engage CSS `:hover` (synthetic dispatchEvent cannot); the calculator rule sets the parent to the line-items SUM — a probe that creates + deletes a row must PATCH the parent back (deleting alone recalcs to 0). Mobile-nav R1→R4 (39th — Tailwind v4 pins hold, the mobile menu works, both sites), data drift (39th — reference read-only, verified before + after), the SEO pair, the VLM pair (**IDENTICAL, zero flags** — the first fully-clean screening) — 108/221/35 green |
| 2026-10-11 | Session 81 — parity iteration v46 (`docs/remediation-plan-v46.md`) | **The net-worth card census + THE VALUE→FACTS SPACING FIX + the confirm-bar white-pill regression pin** (2 new e2e, TDD with four pin-sanity mutations; the session-101 queue's first and third candidates). The surface: the net-worth ASSET/LIABILITY cards at 1280, measured live on BOTH sites (nw-card-v46.mjs + confirm-pill-v46.mjs + the REAL-hover driver steps) — the grid `md:grid-cols-2 lg:grid-cols-3 gap-4` 960 wide / 3 cols × 309.328 / gap 16 (the SAME family on both sites; the summary card's inner `sm:grid-cols-2` is the v4 G4 stat-blocks design — a probe finder lesson), the card chrome byte-identical (309/pad 20/radius 12/border 1px rgb(229,231,227)/rest shadow rgba(0,0,0,0.04) 0px 2px 8px 0px/transition all 0.2s; the title row gap 8/dot 8×8 rgb(143,188,63)/16-600; the type badge bg rgb(243,244,246)/pad 2px 10px/radius 6/12-600; the facts 12px rgb(107,114,128); the kebab 36×36 opacity 0), **the card's REAL hover INERT on BOTH sites** (the inline boxShadow beats the hover:shadow-lg utility, the v29 family) while the kebab REVEALS. **THE v46 PARITY FIX: the value→facts spacing** — the reference wraps its value in `mb-4` (16px) while the clone's bare `mb-2` P rendered 8px (the card h 186 vs the reference's 194; the item-card's own mb-4 wrap the in-repo precedent — the net-worth cards were the one oversight, no census had sampled the 1280 card's internal rhythm): the fix is `mb-2`→`mb-4` on both cards' value P (net-worth-view.tsx). **The confirm-bar white-pill pin** (the clone's superset chrome — the reference's net-worth DELETE is DIRECT, no confirm bars, the v18 superset-fix-#6 family re-confirmed live): the bar (mt 16/radius 8/pad 12/rgb(254,242,242)) + the Cancel pill's shadow-sm VISIBLE layer rgba(0, 0, 0, 0.05) 0px 1px 2px 0px (the `--shadow-sm` theme pin's regression net, the five-site family). FOUR PIN-SANITY MUTATIONS VERIFIED TO FAIL: the reverted mb-4 → the F2 census fails (the value mb + the card h); the pill's shadow-sm removed → the F3 pin fails; the card inline 0.04→0.08 → the F2 rest-shadow pin fails; the kebab's group-hover reveal removed → the F2 hover step fails. Probe lessons: **the reference's net-worth kebab flow is NEVER safe to probe past the menu open** (the menu's Delete click IS the delete — the reference's only asset was deleted and restored via its Add Asset form this session: name 'Savings Account', type bank account, value 25000, institution 'Commonwealth Bank', date 2026-10-07, the panel census re-reading '1 items · $25,000' byte-identical to the before state); a Radix dropdown ignores synthetic `el.click()` — only a NATIVE Playwright/agent-browser click opens it; the reference's dialogs are plain `fixed inset-0` divs with NO `[role=dialog]` (find them by the Save-button text); the reference's tabs ALSO need native clicks; the confirm-bar pill/text colors compute as `lab(...)` strings (Tailwind v4's oklab emission) — ACCEPTED for superset-only surfaces (no reference counterpart to byte-match), the shadow VISIBLE layer is the pin that matters. Mobile-nav R1→R4 (40th — Tailwind v4 pins hold, the mobile menu works, both sites), data drift (40th — reference read-only, verified before + after, the incident fully restored), the SEO pair, the VLM pair on the /networth surface at 1280 (**IDENTICAL, zero flags** — the second fully-clean screening) — 108/223/35 green |
| 2026-10-11 | Session 82 — parity iteration v47 (`docs/remediation-plan-v47.md`) | **The dialog-input focus composite + the net-worth card MOBILE census + the mobile sheet's shadow-lg — a PIN-ONLY iteration** (3 new e2e, TDD with four pin-sanity mutations; NO production-code change — the measured chrome was already at parity on every VISIBLE layer, the pins lock it; the v45-family's third pin-only iteration). The surface: the session-101 queue's second item (the dialog inputs' focus-state shadow composition) + the v46 follow-up (the net-worth card's MOBILE census at 390, the post-fix internal rhythm) + the session-104 queue's sheet item (the mobile sheet's shadow-lg). MEASURED LIVE ON BOTH SITES: the dialog input under REAL focus (`focus({ focusVisible: true })`, the v35 idiom) — the reference composes a white zero-spread lead + the 1px #0a0a0a RING + the shadow-sm visible layer (3 layers, v3's slot count) while the clone's shadcn stack (shadow-sm + focus-visible:ring-1 ring-ring) composes the SAME two VISIBLE layers with 4/3 transparent leads (v4's 5-slot construction — the accepted v10/v25/v45 class); the input chrome identical (h 36/radius 6/pad 4px 12px/border 1px rgb(229,229,229)/bg transparent), the border UNCHANGED under focus on both sites (the ring does the work). The net-worth card at 390: the reference's card h 194 (inside its 432-wide OVERFLOWING grid — its documented superset-fix-#4 bug, docSW 464) vs the clone's 358×194 (the page FITS, docSW 390) — the card heights match EXACTLY, the v46 fix's rhythm survives the mobile reflow (the value mb 16, the facts 12px rgb(107,114,128), the measured gap 16). The mobile sheet: 288×844/x 0/bg rgb(250,250,250) + the shadow-lg VISIBLE pair (rgba(0,0,0,0.1) 0px 10px 15px -3px + 0px 4px 6px -4px) — the shadow-scale regression net's SIXTH site (the lg end on the mobile surface); the overlay rgba(0,0,0,0.8) z 50. FOUR PIN-SANITY MUTATIONS VERIFIED TO FAIL: the input's ring-1 removed → the F1 pin fails; the input's shadow-sm removed → the F1 pin fails; the value mb-4 reverted → the F2 census fails (mb 16→8 AND h 194→186); the sheet's shadow-lg removed → the F3 pin fails — **each mutation needs the standalone REBUILD before the run bites (the e2e-tests-run-against-the-build lesson: a src/ mutation is invisible to the suite until `npm run build`)**. Probe lessons: the reference's /income at 390 is overflow-free (docSW 390 — a comparable VLM mobile surface); the VLM's 3 flags on the mobile /income pair all DOM-verified as data/platform classes (the clone's richer seed carries a 4th Recurring badge that wraps in the byte-identical flex flex-wrap gap-2 container — the reference has no second card to compare; the 'Edit with Base44' FAB is the reference's own platform chrome) — the v43 misattribution lesson re-applied; the reference's net-worth value wrap is div.mb-4 while the clone carries mb-4 ON the P — the computed geometry is the contract, the DOM shape is not (the v45 lesson, re-measured at 390). Mobile-nav R1→R4 (41st — Tailwind v4 pins hold, the mobile menu works, both sites), data drift (41st — reference read-only, verified before + after), the SEO pair (robots + sitemap live on both), the VLM pair on the mobile /income surface at 390 (3 flags, all DOM-verified data/platform classes — no chrome gaps) — 108/226/35 green |
| 2026-10-12 | Session 84 — parity iteration v49 (`docs/remediation-plan-v49.md`) | **The login panel's mobile-only &nbsp; spacer (THE FIX — the first production-code change since v46) + the donut legend's mobile reflow + the calculator dialog's 640 chrome (two PIN-ONLY surfaces)** (3 new e2e, TDD with six pin-sanity mutations; the session-111 v49 queue's three candidates). THE v49 FIX (F1, `tests/e2e/login-parity.spec.ts`): the reference's login wrapper carries a SECOND child at mobile — `<div class="mt-8 text-center text-xs text-slate-400 sm:hidden"><p>&nbsp;</p></div>` (h 16, mt 32, color rgb(148,163,184)) below the panel — lifting its card stack 24px above the geometric center at 390 (the reference's panel y 57 / wrapper 730; the pre-fix clone centered the panel ALONE at y 81 / wrapper 682). The v12/v13 login pins were desktop-measured where `sm:hidden` hides the spacer — invisible there, never measured; the v24 auth-forms mobile census walked the controls, never the panel's position; first-time measurement at 390 caught it (verified on the reference's sign-in AND sign-up states — the spacer is a panel SIBLING, every auth state carries it; the 640 contract re-verified live: display none, the panel re-centers to y 111 = (960−422)/2 on the sign-up state). The fix (`src/components/budget/login-card.tsx`): the spacer added as the w-full max-w-md wrapper's second child, the color pinned as the `text-[#94a3b8]` hex (Tailwind v4's named slate computes as oklab() — the v7 login-family rule; the &nbsp; content never renders it, the census pins it byte-exact anyway); the pin asserts the wrapper 730, the panel y 57/h 682/w 358, the spacer census (h 16/mt 32/fs 12/color/ta center/display block/text  ) + the 640 re-check (display none, the re-centering). F2 (`tests/e2e/dashboard.spec.ts`) — the donut legend's MOBILE reflow at 390 (the v44 F3 measured BOTH viewports but pinned only 1280; the v49 pin locks the mobile reflow): the container display flex/flex-direction column/gap 12px/mt 24px/w 308, the row w 308/h 64/radius 8px/pad 12px/bg rgb(245,248,245), the dot 16×16/radius 4px/bg rgb(224,122,59), the leaves (the label fs 16/fw 500/rgb(26,58,46) 'Need'; the amount fs 16/fw 700/rgb(224,122,59); the pct fs 12/fw 400/rgb(107,114,128)), the right block ta right, the svg icon w 16/color rgb(224,122,59), sw 390 — byte-identical (the reference's row w 313 rides its own 395 docSW overflow — the documented superset-fix-#4; the clone's 308 fits). The row's INHERITED color (rgb(10,10,10) vs rgb(23,23,23) — the neutral vs accent foreground) never renders: every text leaf carries an explicit color — an invisible divergence, documented. F3 (`tests/e2e/calculator.spec.ts`) — the calculator panel's CHROME census at 640 (the read-only open flow: hover the Rent card → Calculate → census → Close; the v45 F2b pinned only the WIDTHS at 640 after a line-item add): w 608/x 16/radius 16px/maxW 768px (max-w-3xl)/maxH 816px (85vh of 960)/bg rgb(255,255,255)/overflow hidden, the boxShadow toContain the 2xl VISIBLE layer `rgba(0, 0, 0, 0.25) 0px 25px 50px -12px` (the reference's 2 transparent leads vs the clone's `.zb-modal-panel` direct emission — the accepted lead-divergence class, the shadow-scale net's EIGHTH site), the close button 36×36, the header border-b 1px solid rgb(229,231,227), the CENTERING invariant (y == round((960−h)/2) — the height is data-dependent, the pin never asserts it), sw 640. SIX PIN-SANITY MUTATIONS VERIFIED TO FAIL: the spacer removed → the F1 pin fails (the TDD RED run — the pre-fix state); the spacer's mt-8→mt-4 → the F1 pin fails (the wrapper 730→722, the panel y 57→69); the spacer's sm:hidden removed → the F1 640 sub-check fails (the spacer display block at 640, the panel drifts off-center); the legend row's p-3→p-2 → the F2 pin fails (pad 12→8, h 64→56); the `.zb-modal-panel` box-shadow removed → the F3 pin fails (no 2xl layer); the calculator's inline maxHeight 85vh→90vh → the F3 pin fails (maxH 816→864) — each with the standalone REBUILD (the v47/v48 lesson). Probe lessons: the reference's login-page vertical layout at 390 is a THREE-element stack (main p-4 → the w-full max-w-md wrapper → panel + spacer) — census the WRAPPER's children, not just the panel (a panel-only census reads the card as centered when the reference's stack is not); agent-browser's screenshot syntax is `screenshot [selector] [path]` — `screenshot <path> full` mis-fires (the path parsed as a selector, 'full' as the path); the reference's donut legend row w 313 vs the clone's 308 IS the reference's own 5px /dashboard overflow (docSW 395) — the row-width diff rides the overflow, not a chrome gap (the v46/v47 lesson family). Mobile-nav R1→R4 (43rd — Tailwind v4 pins hold, the mobile menu works, both sites; the sheet-trap re-verified with the precise overlay census — the z-50 rgba(0,0,0,0.8) scrim still open on /income after the nav click; the earlier heuristic detector missed it — an empty-text overlay needs the z-index+geometry census), data drift (43rd — reference read-only, verified before + after: '1 items · $25,000' networth / '1 items · $5000.00' income), the SEO pair (robots + sitemap live on both), the VLM pair on the LOGIN page at 390 (THE FIXED SURFACE — a data-free static form): **IDENTICAL, zero app flags** (the only flag the reference's own 'Edit with Base44' FAB platform chrome) — the F1 fix's visual verification. — 108/232/35 green (3 new e2e, 1 production fix, TDD) |
| 2026-10-12 | Session 87 — parity iteration v52 (`docs/remediation-plan-v52.md`) | **The details sheet's missing subcategory line (THE FIX — the fourth production-code change since v46) + the /income and /expenses 390 pins + the details-sheet internals pin (ALL PIN-ONLY) + the standing script's burger-selector probe-infra fix** (4 new e2e, TDD with five pin-sanity mutations; the session-121 v52 queue's read-only members: the /income and /expenses mobile censuses + the item-details 390 reflow). THE v52 FIX (F1, `tests/e2e/item-details.spec.ts`): the reference's details-sheet summary renders FIVE elements — the chip row → the H3 name (text-2xl font-bold mb-2, 24/700/forest) → **the SUBCATEGORY P (`text-lg`, 18/400/rgb(107,114,128))** → the amount P (text-4xl font-bold mt-4, 36/700/type-color) — measured live on the reference's Rent AND Salary sheets ("Apartment" / "Main Job", via the read-only card-body click) — while the clone rendered FOUR (the H3 → the amount directly): the `subcategory` field was always on the model (the card renders it at item-card.tsx:125, the edit dialog edits it at budget-item-dialog.tsx:256) but the details view never wired it. The one-insert fix (`item-details-dialog.tsx` between the H3 and the amount, conditional on the non-empty value — the dialog's own optional-field idiom, e.g. paymentMethod; every reference item carries a subcategory so both forms produce identical DOM on real data): adds ~27px to the scrollable body; the panel stays capped at its 85vh max-height (the body was ALREADY over the cap at 768) — NO existing geometry pin affected (the v28 mobile geometry test's y 127/w 390/maxH 717.4 and the v48 shadow census's h 680 at 800 both ride the cap). F2 (`tests/e2e/items.spec.ts`) — the /INCOME view at 390: byte-parity (the header row 358×112 flex-col/gap 16/mb 32/align-start — the mobile reflow of the v20 G1 row; the 48×48 radius-12 lime-gradient chip; the H1 30/700/forest; the count sub 16/400/gray; the Add button 147×36/radius 6/lime gradient/white 14/500/pad 8 16; the filter card 358/radius 16/pad 24/white/border/mb 24; the inner grid 1-col 308/gap 16/3 children at the y rhythm 246/298/350; the search 308×36/radius 6/pad 4 12 4 40; the item grid 1-col 358/gap 16; the first card radius 12/pad 20/border/white/the rgba(0,0,0,0.04) 0px 2px 8px shadow; the H4 16/600/forest; the amount 16/400/rgb(10,10,10); docSW 390 — the card height and the count/amount texts are the seed's data class, never pinned). F3 (`tests/e2e/items.spec.ts`) — the /EXPENSES view at 390: byte-parity (the same family + the 155×36 orange-gradient Add button + the filter's 4-children/3-combobox-triggers inner grid — the payment-method family; the first card's chrome; docSW 390). F4 (`tests/e2e/item-details.spec.ts`) — the DETAILS SHEET's INTERNALS at 390 (beyond the v28/v48 panel pins — those walked the panel chrome + the bottom-sheet geometry; the internals were never pinned): byte-parity (the panel 390×717 @ y 127/radius 24 24 0 0/maxH 717.4/white/overflow-y auto + the 2xl visible layer with the accepted 4-vs-2 lead divergence; the sticky header h 69/pad 16 24/position sticky/top 0/border-b rgb(229,231,227)/white; the title 18/700/forest; the 36×36 close; the body space-y-6 p-6; the summary's chip row gap 8 (gap-2)/mb 12/centered with the 12/500 type-color rounded-full px-3 py-1 chips — the rounded-full COMPUTED radius diverges 9999px (v3) vs 3.35544e+07px (v4), both fully-round pills, the CLASS is the pinned contract; the classification block radius 12/pad 16; the fact rows flex/gap 12/pad 8 0; the meta footer border-t/pt 16/grid-cols-2 with the 12px gray labels + font-medium forest values). FIVE PIN-SANITY MUTATIONS VERIFIED TO FAIL: the subcategory P removed (the TDD RED run — the pre-fix proof); the income chip's inline gradient removed (F2); the filter card's p-6→p-4 (F2 AND F3); the details header's py-4→py-2 (F4 — the header 69→53); the H1's text-3xl→text-2xl (F2 AND F3 — the fs 30→24) — each with the standalone REBUILD first. P1 (probe-infra, a scripts/ fix — NOT production): the standing script clone-stand47.sh's R1 step clicked `button[aria-label="Open menu"]` — the REFERENCE's DOM idiom; the clone's burger carries NO aria-label (its accessible name rides the sr-only span "Toggle Sidebar" — the v7 idiom) so the click failed SILENTLY (the `|| true` masked it) and R1 read sheetLinks:0 — a FALSE RED on a WORKING surface (the 7 mobile-navigation e2e tests pass; the session's eval-flow verified the sheet opens 5 links/navigates/closes/Escape-closes); the fixed text-walk eval reads sheetLinks:5. Standing checks all clean (46th): mobile-nav R1–R4 both sites, the reference's four bugs ALL live (the toast-blocker; the sheet-trap via overlayCount — the z-50 scrim remains on /income after the nav click; the no-landmark; the 464 /networth overflow), the data census read-only and intact, the SEO pair live on both. The trap-log scan CLEAN (only two -mb- utilities live in src/ — both the auth back buttons, both inside their converted zb-auth-mode containers). The VLM pair on the /expenses view at 390 (THE F3 SURFACE): 4 flagged diffs, ALL DOM-verified as the documented seed-data/platform classes (the count/total; the card contents — the richer seed; the Base44 FAB — the reference's own platform chrome, the VLM mislabeled which image carries it; the layout length). Probe lessons: the reference session EXPIRES between long eval gaps — re-login via the same eval before any follow-up census; `agent-browser set viewport` state does NOT survive a session restart — re-apply before any 390 census after a re-login (the "215.5px desktop" false reading); the reference's details sheet has NO [role=dialog] (the no-landmark family — find the sheet via the `fixed inset-0 z-50` overlay class census); the reference's summary name is an H3 with the subcategory as a SEPARATE P (the two-level title structure — walk the full subtree, a leaf-only census misses siblings); the rounded-full computed radius diverges v3/v4 — pin the class, not the computed value. Full chain: lint + typecheck + 108 unit + build + 245/245 e2e (+4, 5.5m — clean on the FIRST run, no flakes) + 35/35 smoke green. The 16 screenshots regenerated (ONE byte-diff: 16-item-details.png — the F1 fix's visual effect); the docs aligned (AGENTS/CLAUDE/README/SKILL Session 87 row + the 245 state/PAD v1.1.9/the probe README's v52 section/session_122 + session_123/the repo worklog Session 86 + the ledger list). Four new e2e, 241 to 245, 108/245/35 green |
| 2026-10-12 | Session 88 — parity iteration v53 (`docs/remediation-plan-v53.md`) | **The /networth tablist's mobile pin + the calculator dialog's mobile pin (PIN-ONLY — the second consecutive pin-only iteration; no production-code change)** (2 new e2e, TDD with five pin-sanity mutations; the session-124 v53 queue's read-only members: the /networth mobile tablist census + the calculator dialog 390 reflow). F1 (`tests/e2e/networth.spec.ts`) — the TABLIST at 390: byte-parity on every chrome axis (the list h 36/grid/bg #f5f5f5/radius 8/pad 4/maxW 448; the ACTIVE trigger 175×28/radius 6/14/500/#14532d on #dcfce7 + the shadow-sm VISIBLE pair + the 16×16 currentColor icon at mr 8; the INACTIVE 175×28/#737373/transparent/shadow none) — the WIDTH family rides the reference's own documented 464-overflow bug (its list renders 432 wide with fractional 211.8px tracks inside the overflowing page, overhanging the 390 viewport; the clone's superset fix keeps the page in-bounds at 358 with 175px tracks/pageSW 390 — the v47 net-worth-card mobile-census divergence class). F2 (`tests/e2e/calculator.spec.ts`) — the CALCULATOR DIALOG at 390 (the v45 F2b add-then-cleanup flow; the reference's own data carries 1 row, the clone's dev seed none): byte-parity (the panel 358 @ x 16 = 390 − 2×16 overlay pad/radius 16/maxW 768/maxH 717.4 = 85vh/white/overflow hidden/flex + the 2xl VISIBLE layer + the CENTERING invariant; the header h 101/pad 16 24/border-b; the chip 32×40 + the close 29×36 — the IDENTICAL flex-shrink squish at 390 on BOTH sites; the h2 18/700/forest; the desc 14/gray; the total card 310/#fff7f5/radius 12/pad 16; the row 310/pad 16/white/border-t/radius 12; the Add Item button 110×32/12/500/the orange gradient/white; docSW 390 — the panel h 413 with 1 row on BOTH sites is data-dependent, never pinned). FIVE PIN-SANITY MUTATIONS VERIFIED TO FAIL (the TabsList grid-cols-2→grid-cols-1; the active bg-[#dcfce7] removed; the header py-4→py-2 [101→69]; the panel maxWidth 48rem→40rem [768→640]; the total card p-4→p-2 [16→8]) — each with the standalone REBUILD first. EXECUTION LESSONS (the big ones): (1) a timed-out playwright run leaves an ORPHANED webServer on :3100 that the next run REUSES via reuseExistingServer — with a stale db handle after the next global-setup re-seed, poisoning every data-driven assertion (the 10.5s expect-timeout cascade; `ss -tlnp | grep :3100` + kill before every full-chain run); (2) every calculator add/delete e2e MUST end with restoreRent(page) — the line-item mutations recalculate the parent's amount server-side, a missing restore poisons every later spec's dashboard arithmetic (+$2065.00); (3) the rebuild and the test run must be SEPARATE commands (the combined one-liner raced the .next/standalone swap twice); (4) the eval string's closing `()` — an un-invoked async function expression submits NOTHING (the login silently no-ops, the "no card" cascade). Standing checks all clean (47th): mobile-nav R1–R4 both sites (the v52-fixed text-walk selector reads sheetLinks:5), the reference's four bugs ALL live, the data census intact, the SEO pair live. The VLM pair on the calculator at 390 (THE F2 SURFACE): 5 flagged diffs ALL DOM-verified (the close-button "boxed X" = the probe's synthetic-click focus artifact — outline:auto renders only under :focus-visible, the keyboard-a11y superset; the reference's close is never focused on open and its outline-style is none, its own a11y regression; no ring in real mouse flows — the desktop 08-calculator.png proves it; the rest = the reference's own data class + the Base44 FAB platform chrome). Full chain: lint + typecheck + 108 unit + build + 246/246 chromium e2e (+2, run as two ordered chunks 140+108 after the orphan-server diagnosis; both exit 0, zero failures) + 35/35 smoke green. The 16 screenshots regenerated (ZERO byte-diffs — the pin-only invariant); the docs aligned (AGENTS/CLAUDE/README/SKILL Session 88 row + the 247 state/PAD v1.1.10/the probe README's v53 section/session_125 + session_126/the repo worklog Session 87 + the ledger list). Two new e2e, 245 to 247, 108/247/35 green |
| 2026-10-13 | Session 90 — parity iteration v55 (`docs/remediation-plan-v55.md`) | **The ICON-GLYPH swap (THE FIX — the fifth production-code change since v46, breaking the v53/v54 pin-only streak)** (6 new e2e, TDD RED-first with five pin-sanity mutations; the session-128 v55 queue's goal-card classification-icon glyph census, extended to a FULL icon-glyph audit — `glyph-audit-v55.sh` + `glyph-diff-v55.mjs`, 24 lucide glyphs across the five views + the login page, measured live on BOTH sites): 19 of 24 shared glyphs byte-identical, 4 DRIFTED — lucide-react 0.525 redesigned piggy-bank / trending-up / search / mail since the reference's lucide version (the v44 chevron-swap class: parity is the SHAPE DATA — a computed-style census cannot see a glyph swap, read the svg's shape children). F1 — `src/components/ui/legacy-icons.tsx` (the reference's EXACT svg: base attrs + path/polyline/rect/circle children byte-identical to the live reference DOM, the `lucide lucide-<name>` class prefix kept for the svg.lucide-* selectors, aria-hidden mirroring lucide's own no-a11y-prop rule) + the eight import swaps (item-card / items-view / dashboard-view / item-details-dialog / budget-item-dialog / sidebar / net-worth-view / login-card). The reference renders the piggy's OLD 3-path glyph on EVERY surface (piggy-sweep-v55.sh: the nav rail's Savings link, the Total-Savings stat row, the donut legend, the quick actions, the savings hero, the classification chips) and the trending-up as TWO POLYLINES (`points='22 7 13.5 15.5 8.5 10.5 2 17'` + `'16 7 22 7 22 13'` — the redesign turned it into paths). The e2e pin (`tests/e2e/glyph-parity.spec.ts`): the goal card's piggy (12×12, mr 4, the chip's own color) / calendar (3 paths + the 18×18 rx-2 rect — already byte-parity, pin-locked) / repeat (the clone-only Recurring badge) at 390, EVERY dashboard + networth piggy + trending, the search handle (`m21 21-4.3-4.3`, not the 4.34 redesign), the login mail flap (`a1.94 1.94`, not the `a2 2` redesign) + lock, and the /expenses heart + circle-alert same-glyph control (the reference's Netflix/Investments cards vs the clone's Entertainment/Groceries/Rent — the same glyphs, byte-identical). SIX pin-sanity mutations verified to FAIL (the piggy body path; the trending polyline points; the search handle 4.3→4.34; the mail flap a1.94→a2; ONE usage-site revert to the lucide import — each with the standalone REBUILD as a SEPARATE command). Standing checks clean (49th): mobile-nav R1–R4 both sites (the mobile menu verified working), the reference's four bugs ALL live, the data census intact, the SEO pair live. The VLM pair (the calculator dialog's with-row — the v53 F2 surface, the session-128 standing-check suggestion + the savings goal card post-swap): CLEAN per the v43 rule — the X-close 29×36 transparent/radius 6/lucide-x 16×16 byte-identical on both sites (the 'square-outlined X' a screenshot-perception artifact), the amounts 24px/700 on both sites' every card (the 'smaller font' a digits-count misread); the state/content differences are the documented seed-data classes (the reference's calculator carries its own Contents Insurance row; the clone's dev seed's Rent has none) + the Base44 FAB. PROBE LESSONS: (1) a path-only glyph census reads ZERO paths on circle-alert — the glyphs render circle/rect/polyline children; walk every shape tag and read `points` (not x1/y1) for polylines; (2) the glyph audit's login can RACE the page mount ('no inputs' is the RETRY signal, not auth state) and the auth state needs an explicit post-login check — the first sweep censused the LOGIN PAGE six times; (3) agent-browser eval output is a JSON-encoded string — unwrap it (twice if doubly-encoded) before parsing dictionaries. Full chain: lint + typecheck + 108 unit + build + 254 e2e (run as two ordered chunks 122+133, both exit 0, zero failures) + 35/35 smoke green. The 16 screenshots regenerated (14 byte-diffs — the production-change invariant, the first non-pin-only regeneration since v49); the docs aligned (AGENTS/CLAUDE/README/SKILL Session 90 row + the 254 state/PAD v1.1.12/the probe README's v55 section/session_131 + session_132/the repo worklog Session 89 + the ledger list). Six new e2e, 248 to 254, 108/254/35 green |
| 2026-10-13 | Session 91 — parity iteration v56 (`docs/remediation-plan-v56.md`) | **The 1280 desktop VLM standing pair + the glyph-swap HOLD re-audit (PIN-ONLY — no production-code change, the v53/v54 line's return to pin-only after the v55 FIX)** (1 new e2e + three pin-sanity mutations; the session-131 v56 queue's own suggestion — a fresh VLM pair on the v55 F1 surfaces' desktop 1280 state). The glyph re-audit (`glyph-audit-v56.sh`, the polyline/rect-rx capture fix applied): 24 shared glyph names, 0 DIFFS among the shared set, 1 one-side-only (repeat) — **the v55 legacy-icon swap HOLDS byte-identical; no new drift**. The desktop 1280x800 pair (`vlm-shots-v56.sh` + `clone-vlmshots-v56.sh` + `vlm-compare-v56.mjs`): PAIR 2 (the networth view — the trending-up swap surfaces) VERDICT IDENTICAL; PAIR 1 (the dashboard) flagged 4, every one DOM-arbitrated clean (`vlm-arbit-v56.sh` + `clone-arbit-v56.sh`, the v43 rule) — the nav "Dashboard" highlight is the documented root-URL active-nav gap (a reference bug the clone deliberately fixes; the non-root control at /networth renders the byte-identical 135deg forest-gradient active style on BOTH sites), the progress-bar length is data-driven (the track byte-identical 568x12 rgba(255,255,255,0.1) on both sites; the fill's width is pct x 568 per each site's own data — the reference 173 = 30.5% x 568, the clone 357 = 62.8% x 568), the avatar is the user-identity class, the FAB the Base44 platform chrome. The v56 pin (`tests/e2e/dashboard.spec.ts`, the "hero desktop 1280 census" describe, +1 → 255): the hero-desk-v56.sh measurement (byte-identical on both sites) — the hero grid's 304px triple-column template + 24px gap + the [632x364, 304x364] children at y 136, the goal card 632x316/radius 16/pad 32/the 135deg forest gradient + the 26-58-46/0.3 shadow, the 568x12 track, the fill's 90deg status-gradient family + its pct-proportional width arithmetic (±2px), the three 48px stat tiles' 24x24 svgs (the v55 glyph-swap chrome). THREE pin-sanity mutations verified to FAIL then restored (the track h-3→h-2, the card p-8→p-6, the grid gap-6→gap-4 — each with the standalone REBUILD as a SEPARATE command). Standing checks clean (50th): mobile-nav R1–R4 both sites (the mobile menu verified working), the reference's four bugs ALL live, the data census intact, the SEO pair live. PROBE LESSONS: (1) the v55 census's polyline capture read `points` as empty via x1/y1 — branch the shape dump per tag; (2) the reference has no <nav> landmark (its own documented bug) — nav probes must scan ALL anchors, not nav-scoped selectors; (3) the combined clone-side shot script can exceed the 240s Bash timeout when the agent-browser daemon was reset between steps — split into per-view invocations. Full chain: lint + typecheck + 108 unit + build + 255 e2e (two ordered chunks 105+151, both exit 0, zero failures) + 35/35 smoke green. The 16 screenshots regenerated (7 trivial timing diffs ≤0.005% pixels — the pin-only invariant; no production change, `git diff src/` empty). The docs aligned (AGENTS/CLAUDE/README/SKILL Session 91 row + the 255 state/PAD v1.1.13/the probe README's v56 section/session_134 + session_135/the repo worklog Session 90 + the ledger list). One new e2e, 254 to 255, 108/255/35 green |
| 2026-10-13 | Session 92 — parity iteration v57 (`docs/remediation-plan-v57.md`) | **The items-view desktop 1280 VLM standing pair + the item-card footer + badge-row census (PIN-ONLY — no production-code change, the pin-only line's continuation) + the not-found G7 flake fix (TEST-ONLY)** (2 new e2e + three pin-sanity mutations; the session-134 v57 queue's own suggestion — a fresh VLM pair on the ITEMS view's desktop 1280 state, the v56 pair having covered the dashboard + networth). The pair (`vlm-shots-v57.sh` + `clone-vlmshots-v57.sh` + `vlm-compare-v57.mjs`): the income + expenses views, every flag DOM-arbitrated to the documented data classes (`vlm-arbit-v57.sh` + the badge-census pair, the v43 rule) — the avatar (the user-identity class); the seed data; the payment-method chips (DATA-CONDITIONAL: the footer row's chrome byte-identical on both sites [flex justify-between 12px rgb(107,114,128) h 16; each span flex gap 4px with the 12×12 gray icon] — the reference's own income card renders the SAME two-child structure [the date + "Bank Account"] while its expense items carry no payment methods); the badge wrap (the row's chrome byte-identical [flex wrap 8px mb 12px; every badge flex center / 6px / 2px 10px / 12px/600 / h 22 / 12×12 icons], the clone's Recurring superset badge wraps the row to h 52 = 22+8+22). The v57 pin (`tests/e2e/items.spec.ts`, the "items card footer + badge census at 1280" describe, +2 → 257): F1a the /income card's footer two-children conditional render (the date span + the PayPal chip) + the badge chrome (flex/center/6px/2px 10px/12px/600/h 22, the [want, monthly, active] texts); F1b the /expenses grid census (960/3 children/16px gap/the 3-col template) + the wrapped 4-badge row (h 52, [want, monthly, Recurring, active]). THREE pin-sanity mutations verified to FAIL then restored (the footer text-xs→text-sm, the badge-row gap-2→gap-4, the badge px-2.5→px-2 — each with the standalone REBUILD as a SEPARATE command). F3 (TEST-ONLY): the not-found G7 "Go Home" flake fix — the file-wide logged-out opt-out raced the /login redirect's ~50-180ms transient dashboard render (a genuine ~1-in-8 failure by --repeat-each, NOT load; three chunk-run failures in one session triggered the root-cause probe); the test now carries its own describe-scoped storageState (`tests/e2e/.auth/user.json`, the same AUTH_STATE the chromium project uses) — verified 21/21 by --repeat-each=10. Standing checks clean (51st): mobile-nav R1–R4 both sites (the mobile menu verified working), the reference's four bugs ALL live, the data census intact, the SEO pair live. PROBE LESSONS: (1) the badge-row finder walks the card's DIRECT children (the row is a direct child, not nested); (2) the clone-side with-server heredoc must be QUOTED (<<'EOF') when it carries a $-expanded census variable; (3) the reference's expenses items carry no payment methods — the conditional footer is the parity contract, not a drift. Full chain: lint + typecheck + 108 unit + build + 257 e2e (two ordered chunks 115+143, both exit 0, zero failures) + 35/35 smoke green. The 16 screenshots regenerated ALL BYTE-IDENTICAL (the pin-only invariant; `git diff src/` empty). The docs aligned (AGENTS/CLAUDE/README/SKILL Session 92 row + the 257 state/PAD v1.1.14/the probe README's v57 section/session_137/the repo worklog Session 91 + the ledger list). Two new e2e, 255 to 257, 108/257/35 green |
| 2026-10-13 | Session 93 — parity iteration v58 (`docs/remediation-plan-v58.md`) | **The savings-view desktop 1280 VLM standing pair + the savings goal-card's footer + badge-row census (PIN-ONLY — no production-code change; the eighth iteration since v46, the pin-only line's continuation)** (1 new e2e + three pin-sanity mutations; the session-137 v58 queue's own first suggestion — the items family's remaining view, the v57 pair having covered income + expenses; the savings goal-card's 1280 state was unpinned at the pair viewport, its internals pinned at 390 only [v54 F1]). The pair (`vlm-shots-v58.sh` + `clone-vlmshots-v58.sh` + `vlm-compare-v58.mjs`): the savings view at desktop 1280x800, every flag DOM-arbitrated to the documented data classes (`savings-census-ref-v58.sh` + `savings-census-clone-v58.sh`, the v43 rule) — the seed data (the reference's own 1-item savings view ["1 items · $1000.00", "Emergency Fund" $1000] vs the clone's dev seed ["2 items · $1250.00", Investments $450 + Emergency Fund $800]); the savings card's footer content (DATA-CONDITIONAL: the footer row's chrome byte-identical on both sites [flex justify-between 12px rgb(107,114,128) h 16; each span flex gap 4px with the 12×12 gray icon] — the reference's own savings item carries NO paymentMethod so its footer renders ONE child [the date alone], the clone's items carry them and render the SAME two-child structure the reference's own income card renders [the date + "Brokerage"] — the v57 conditional-footer contract measured on the third view); the badge family (DATA-CONDITIONAL: the badge-row chrome byte-identical [flex wrap 8px mb 12px; every badge flex center / 6px / 2px 10px / 12px/600 / h 22 / the 12×12 icons] — the reference's savings item is classified "need" [the red family] while the clone's are "savings" [the green family]: the classification VALUE is the data class, the color maps stay locked by badge-colors.spec.ts; the monthly purple-50 + active slate-50 badges byte-identical both sides; the clone's Recurring superset badge wraps the row to h 52 = 22+8+22); the grid (960/16px gap/the 3-col template each ≈309.33px; the card chrome 309/20px/12px/1px solid rgb(229,231,227)/white — the v45 F1a pin's own values). The v58 pin (`tests/e2e/items.spec.ts`, the "the savings goal-card census at 1280" describe, +1 → 258): the /savings grid (960/2 children/16px gap/the 3-col template) + the Investments card's two-children conditional footer (the date span + the "Brokerage" chip) + the wrapped 4-badge row (h 52, [savings, monthly, Recurring, active]) + every badge's geometry. THREE pin-sanity mutations verified to FAIL then restored (the footer text-xs→text-sm; the badge-row gap-2→gap-4; the classification badge py-0.5→py-1 — the fresh VERTICAL-pad axis proving the wrap arithmetic 22+8+22, each with the standalone REBUILD as a SEPARATE command). Standing checks clean (52nd): mobile-nav R1–R4 both sites (the mobile menu verified working), the reference's four bugs ALL live, the data census intact, the SEO pair live. PROBE LESSONS: (1) a comment apostrophe inside a single-quoted shell census variable terminates the quote (bash -n before every run); (2) the reference's savings item is classified NEED — the classification VALUE is the data class, the color maps stay locked by badge-colors.spec.ts; (3) the e2e-chunk filter regex: the file alternation must match the FULL filename stem (an `auth\.spec` stem plus the shared `\.spec\.ts` suffix double-matches and silently drops auth.spec.ts / calculator-error.spec.ts / networth-error.spec.ts). Full chain: lint + typecheck + 108 unit + build + 258 e2e (78 + 38 + 144, three ordered chunks this session, both exit 0, zero failures) + 35/35 smoke green. The 16 screenshots regenerated ALL BYTE-IDENTICAL (the pin-only invariant; `git diff src/` empty). The docs aligned (AGENTS/CLAUDE/README/SKILL Session 93 row + the 258 state/PAD v1.1.15/the probe README's v58 section/session_139/the repo worklog Session 92 + the ledger list). One new e2e, 257 to 258, 108/258/35 green |
| 2026-10-15 | Session 94 — parity iteration v59 (`docs/remediation-plan-v59.md`) | **The calculator-view desktop 1280 VLM standing pair + the calculator panel/total-card census (PIN-ONLY — no production-code change; the ninth iteration since v46, the pin-only line's continuation)** (1 new e2e + three pin-sanity mutations; the session-139 v59 queue's first TWO items — the CALCULATOR dialog's desktop 1280x800 pair [the panel + row surfaces; the v45 F2a pin covered the panelW + row census at 1280, the v49 F3 panel chrome at 640 only] and the LOGIN view's 1280 pair [the v55 glyph pin's surface, no pair at 1280 yet]). The calculator pair (`vlm-shots-v59.sh` + `clone-vlmshots-v59.sh` + `vlm-compare-v59.mjs`): both VLM flags DOM-arbitrated (`calc-census-ref-v59.sh` + `calc-census-clone-v59.sh`, the v43 rule) — the total card's "Will update category total" span (DATA-CONDITIONAL: the lineTotal-vs-parentAmount-at-open contract — the reference's own Rent $25 === its line-item sum so hidden, the clone's $1850 parent showed it; the clone-side pair state built by adding the SAME "Contents Insurance" $25 line item through the real UI then FULLY restored [delete + the $1850 edit-flow restore + the $2235.00 page total verified]) and the row's hover-action pair (POINTER-POSITION artifact: both sites gate it at opacity 0 at rest, the reference's shot merely caught it mid-hover); the census byte-identical on every axis (the panel 768/393 @ 256,204 — the centering invariant round((800−393)/2) / radius 16 / maxW 768px / maxH 680px [85vh of 800] / bg white / overflow hidden / the 2xl VISIBLE layer rgba(0,0,0,0.25) 0px 25px 50px -12px / the total card 720×90 #fff7f5 radius 12 pad 16 border 1px solid rgb(252,221,213) / the close 36×36 / the header border-b 1px solid rgb(229,231,227) / the row 720 pad 16 radius 12 border 1px solid rgb(229,231,227) transition all 0.15s — the v45 F2a values re-confirmed live on both sides). The login pair (`login-shots-v59.sh` + `clone-login-shots-v59.sh`): IDENTICAL — the only flag the reference's Base44 platform badge; the census matches exactly (title/h1/inputs/the Sign-in button 368×48). The v59 pin (`tests/e2e/calculator.spec.ts`, the "calculator panel census at 1280" describe, +1 → 259): the read-only open state — the panel chrome + the centering invariant + the 36×36 close + the header border-b + the total card (720/#fff7f5/radius 12/pad 16/border — the v53 F2 chrome at the 1280 viewport) + the panelW 768 control. THREE pin-sanity mutations verified to FAIL then restored (the total card bg #fff7f5→#fff8f0; the panel maxWidth 48rem→42rem; the total card p-4→p-5 — each with the standalone REBUILD as a SEPARATE command). Standing checks clean (53rd): mobile-nav R1–R4 both sites (the mobile menu verified working — the 53rd time), the reference's four bugs ALL live, the data census intact (the /expenses census "4 items · $525.00" now documented: Miscellaneous $0 / Investments $300 / Netflix $200 / Rent $25 — its Rent carries ONE "Contents Insurance" line item), the SEO pair live. PROBE LESSONS: (1) `agent-browser mouse click` DOES NOT EXIST in 0.39.0 — the low-level pair is `mouse down` + `mouse up` after a `mouse move` (a swallowed subcommand failure leaves the pointer on the card body and the down/up opens the ITEM DETAILS dialog — a false-failure signature); (2) the eval output is a JSON-encoded STRING — strip the quotes before `cut` (`POS=${POS//\"/}`) or `mouse move` silently breaks; (3) the reference's dialogs are PLAIN fixed divs (no role=dialog) — find its panels by geometry (maxWidth 768px), never by [role=dialog]; (4) the reference's session EXPIRES between long eval gaps — re-login before any follow-up census. The 16 screenshots: 9 byte-identical + 7 diff the SEED-DATE class (isoDate(-N) anchors to the seed-run date; the fresh checkout seeded a day after v58's capture — VLM-arbitrated DATE-TEXT-only, zero layout diffs; the e2e DB re-seeds every run so the suite is date-independent). Full chain: lint + typecheck + 108 unit + build + 259 e2e (90 + 94 + 76, three ordered chunks, zero failures) + 35/35 smoke green. The docs aligned (AGENTS/CLAUDE/README/SKILL Session 94 row + the 259 state/PAD v1.1.16/the probe README's v59 section/session_141/the repo worklog Session 93 + the ledger list). One new e2e, 258 to 259, 108/259/35 green |
| 2026-10-15 | Session 95 — parity iteration v60 (`docs/remediation-plan-v60.md`) | **The networth-view desktop 1280 VLM standing pair + the dashboard drill-down EXPANDED-state pair (PIN-ONLY — no production-code change; the tenth iteration since v46, the pin-only line's continuation)** (2 new e2e + three pin-sanity mutations; the session-141 v60 queue's first TWO items — the NETWORTH view's dedicated desktop 1280x800 pair [the standing-pair program's remaining major view — the v56 PAIR 2 was the glyph-swap audit pass; the v52-era pins cover the 390/640 chrome] and the DASHBOARD's drill-down EXPANDED surfaces at 1280 [the v43 F3 family pinned the sub/item rows at 640 only; the v44 F2b 1280 pin walked the section/category/footer heights] — both FULL-PAGE shots, the below-the-fold surfaces) + the 54th standing checks (the expenses census now IN the standing script). The networth pair (`vlm-shots-v60.sh` + `clone-vlmshots-v60.sh` + `vlm-compare-v60.mjs`): **VERDICT IDENTICAL** — zero layout/style flags, every difference the expected data class (the figures, the groups, the ratio "∞:1" vs "0.21:1" — the pinned formatRatio contract); the census (`nw-census-ref-v60.sh` + `nw-census-clone-v60.sh`) byte-identical on every axis — the summary card 960/32px/16px/the 135deg forest→lime gradient/the rgba(26,58,46,0.3) 0px 20px 60px shadow; the figure 48px/700/white; the medallion 64×64 white-20% + the 32px icon; the stat grid 440px 440px gap 16; the stat tile 16px/12px/white-10%/blur(10px)/the amount 24px-700; the ratio value 18px/700; the tablist 448/36/"220px 220px" (the v50 F2 values at the pair viewport); the group header 18px/600/rgb(45,90,74)/mb 12/capitalize; the card grid 960/3×309.328/gap 16 + the card 309/20px/12px (the v46 F2 values re-confirmed live); the divergences both documented classes — the summary mb (the reference computes 0, its 32px GAP lives on another element; the GEOMETRY is the contract, the DOM shape is not [the v45 lesson]) + the clone's break-words guard (the D-5 superset). The drill-down pair: FIVE flags, every one DOM-arbitrated (`drill-arbit-ref-v60.sh` + `drill-arbit-clone-v60.sh`, the v43 rule) — the nav highlight (the root-URL active-nav gap, superset contrast #3), the avatar (user-identity), the Base44 tooltip (platform chrome), the hero progress fill 30.5% vs 62.8% (the pct × 568 data class — the track byte-identical 568×12), and the donut percentage labels (a PERCEPTION ARTIFACT — the reference DOES render them: 3 texts/labelLineCount 0/16px/black, the v9 G1b measurement re-confirmed live both sides); the drill census (`drill-census-ref-v60.sh` + `drill-census-clone-v60.sh`) byte-identical on every axis — the card 304; collapsed 364 BOTH; the section {56, 8px, labelH 40}; the category {28, "6px 12px", rgb(249,250,251)}; the sub {24, "4px 8px", rgb(250,250,250), 12px/400/rgb(107,114,128)}; the item {24, "4px 8px", 12px, rgb(156,163,175), maxW 120px + ellipsis}; the footer {29, 1px}; the heights 364→445→499 (reference) vs 364→481→535 (clone) = the DATA class (its one Salary category vs the seed's two); one census-axis false alarm arbitrated by `drill-itemdump-ref-v60.sh` — the reference-side rows[last] caught the item row's INNER label-group div (h 16, pad 0), the REAL item row byte-identical. The v60 pins (+2 → 261): the networth summary-card + tablist census at 1280 (`tests/e2e/networth.spec.ts`, the "net worth view census at 1280" describe — the v41 F2/F3 pattern at the pair viewport, the v46 F2 grid/card controls re-asserted) and the drill-down sub/item-row census at 1280 (`tests/e2e/dashboard.spec.ts`, the "drill-down sub/item-row census at 1280" describe — the finder pins the REAL rows by their chrome [justify-between + pad "4px 8px"], never rows[last]: the itemdump lesson). THREE pin-sanity mutations verified to FAIL then restored (the summary card p-8→p-10 [32px→40px]; the tablist max-w-md→max-w-lg [448→512]; the item label max-w-[120px]→max-w-[140px] — each with the standalone REBUILD as a SEPARATE command). Standing checks clean (54th): mobile-nav R1–R4 both sites (the mobile menu verified working — the 54th time), the reference's four bugs ALL live, the data census intact, the SEO pair live. PROBE LESSONS: (1) a single-quoted bash CENSUS string must contain NO single quotes — the JS selectors like '[role="tablist"]' TERMINATE the bash string and the eval silently returns empty (use escaped double-quoted JS strings inside the single-quoted wrapper, or a quoted heredoc; the failure signature: an empty line between the === markers); (2) the FULL-PAGE screenshot (--full) is the pair-shot mode for views taller than the 800 viewport; (3) the drill-down expansion clicks are VIEW-STATE toggles (safe under the v46 read-only rule); (4) the recharts label census must filter the individual <text> labels from the group wrapper (count 4 = 1 group + 3 labels); (5) census row-finders must pin rows by their chrome (pad/justify-between), never by array position — the reference's sub-area carries the rows' INNER label-group divs. The 16 screenshots: 15 byte-identical + 1 diff the DATE class (07-add-item-modal: the modal's Date input defaults to the CAPTURE-run day 10/14→10/15 — VLM-arbitrated DATE-TEXT-only, zero layout diffs; the seed-date family's dialog-default extension). Full chain: lint + typecheck + 108 unit + build + 261 e2e (91 + 94 + 78, three ordered chunks, zero failures) + 35/35 smoke green. The docs aligned (AGENTS/CLAUDE/README/SKILL Session 95 row + the 261 state/PAD v1.1.17/the probe README's v60 section/session_144/the repo worklog Session 94 + the ledger list). Two new e2e, 259 to 261, 108/261/35 green |
| 2026-10-15 | Session 96 — parity iteration v61 (`docs/remediation-plan-v61.md`) | **The Budget Guidelines card's STRETCH fix (the FIRST production-code change since v55 — the pin-only line broken after six consecutive iterations) + the quick-action row + the Budget Guidelines card's 1280 census pins** (2 new e2e + three pin-sanity mutations; the session-144 v61 queue's first TWO items — the dashboard's below-the-fold FULL-PAGE 1280x800 pair + the DOM census both sides). The VLM pair (`vlm-shots-v61.sh` + `clone-vlmshots-v61.sh` + `vlm-compare-v61.mjs`): **VERDICT IDENTICAL** — but the DOM census caught what the VLM missed: the reference's Budget Guidelines card sits at NATURAL height (348) inside a stretched `space-y-4` wrapper (the grid child; the row 656 under the seed; the card ends at y 1122 right after the Savings tile, the remaining ~308px of the column PAGE BACKGROUND) — the pre-v61 clone's card ITSELF stretched to 656 (the grid child directly) with ~308px of empty white card body + border + shadow below the last tile. Arbitrated three ways — the DOM census both sides, the REGION-CROP VLM re-arbitration (`vlm-glcol-v61.mjs`, the x 770-1258 / y 764-1472 column crops: pre-fix VERDICT DIFFERENT [the reference's card body "ends immediately after the Savings row", the clone's "extends further down"], post-fix VERDICT SAME), and the reference's own row DOM measured live (the `space-y-4` wrapper + the `grid lg:grid-cols-2 gap-6 mb-8` row). **The fix mirrors the reference's DOM** — the guidelines card wrapped in `<div className="space-y-4">` at the row's right column (`dashboard-view.tsx`); TDD: the F2 pin RED (cardH Expected 348, Received 656) → the fix → GREEN (the ±1 subpixel tolerance on the card-bottom-minus-last-tile axis). The quick-action census (`qa-census-ref-v61.sh` + `qa-census-clone-v61.sh`): byte-identical on every axis — the row grid 960/"304px 304px 304px"/gap 24 (the content column 1280 − 256 sidebar − 64 p-8); the cards 304×90/radius 16px/pad 24px/border rgb(229,231,227)/shadow none at rest/transition 0.2s; the icon tile 40×40/radius 12px/the type tints rgba(...,0.125) (a DIV on the reference, a SPAN on the clone — the chrome the contract); the icon 20px/the type colors; the label 16px/500/rgb(26,58,46) via the LEAF-SPAN finder (the v61 label lesson: a bare textContent match catches the clone's row WRAPPER span — fw 400/rgb(10,10,10) — the reference's row is a DIV so the first census pass read it correctly by accident; the finder must pin the exact-text + zero-children span); the plus 16×16/opacity 0.5. The guidelines chrome census: the card 468/radius 12px/border/bg white + the shadow's VISIBLE layers rgba(0,0,0,0.1) 0px 1px 3px 0px + 0px 1px 2px -1px (the reference computes 2 leading zero-alpha layers, the clone 4 — the Tailwind v4 computed-form class, the visible layers the contract); the header pad 24px + 16px/600/rgb(26,58,46); the body "0px 24px 24px"; the three tiles 418×78/radius 8px/pad 16px with the GUIDELINE_ROWS tints/labels/percents/descriptions byte-identical (the constant content — no data dependency, the natural height fully deterministic). The DOM-shape classes documented (no action): the reference's `mb-8` row margins vs the clone's `mt-8` (identical geometry — the quick grid top 1462 BOTH sides); the tile/row tag differences; the shadow's leading-layer count. The v61 pins (+2 → 263): the "Budget Guidelines card census at 1280" describe (`tests/e2e/dashboard.spec.ts` — the card chrome + the NO-STRETCH contract [cardH 348 + the card bottom one body-pad below the last tile + the row 656 − card 308]) and the "quick-action card row census at 1280" describe (the grid + the three cards' full chrome trio + the leaf-span label). THREE pin-sanity mutations verified to FAIL then restored (the wrapper removal → cardH 656 again; the card p-6→p-8 → h 106 vs 90; the tile rounded-xl→rounded-2xl → the radius-12 chrome finder nulls the tile). Standing checks clean (55th): mobile-nav R1–R4 both sites (the mobile menu verified working — the 55th time), the reference's four bugs ALL live, the data census intact, the SEO pair live. PROBE LESSONS: (1) the heading leaf is a DIV so `.closest("div")` returns the heading ITSELF — use `.parentElement` for the wrapper; (2) census finders pin the LEAF span (exact text + zero element children) — never a bare textContent match; (3) the icon tile is a DIV on the reference but a SPAN on the clone — match BOTH tags by chrome; (4) the REGION-CROP arbitration pattern — when a full-page VLM pair calls a surface IDENTICAL but the DOM census diverges, crop BOTH screenshots to the surface's region and re-arbitrate; (5) a grid-child STRETCH divergence can hide inside an IDENTICAL full-page VLM verdict — the DOM census (geometry: card height vs row height) is the authority. The 16 screenshots byte-identical (the fix's visual effect lives below every viewport shot's fold at 1440×900/390×844 — the pinned census + the crop arbitration carry the verification). Full chain: lint + typecheck + 108 unit + build + 263 e2e (93 + 94 + 78, three ordered chunks, zero failures) + 35/35 smoke green. The docs aligned (AGENTS/CLAUDE/README/SKILL Session 96 row + the 263 state/PAD v1.1.18/the probe README's v61 section/session_147/the repo worklog Session 95 + the ledger list). Two new e2e, 261 to 263, 108/263/35 green |
| 2026-10-15 | Session 97 — parity iteration v62 (`docs/remediation-plan-v62.md`) | **The reference-side a11y surface re-audit (NO DRIFT since v38) + the mobile header-subtitle 390 census pin + the SKILL doc count-line sweep (PIN-ONLY — no production-code change; the pin-only line resumes after the v61 fix)** (1 new e2e + one pin-sanity mutation; the session-147 v62 queue first TWO items — the reference axe-tree re-audit deferred from v61, and the four stale SKILL count lines flagged by the v61 doc digest). The a11y re-audit (`axe-detail-ref-v62.mjs`, the full a11y.spec.ts surface: six authed routes at 1280 + the 404 + the logged-out login + the mobile 390 sheet-open state, axe-core 4.13): **NO DRIFT** — the logged-out login still ZERO-violation; the structural families still exactly `button-name` (10 nodes: the unlabeled Select triggers + card kebabs) + `svg-img-alt` (6 nodes: the recharts donut sectors) — the two families the clone deliberately fixes (GATE 1 superset contrast); the contrast palette still EXACTLY the v38 7-color set (lime/blue/orange/orangeLight/gray-500/#cbd5e1/zinc-500) — no new low-contrast color entered the reference design, the clone GATE 2 allow-list unchanged; the mobile sheet-open tree color-contrast only. The TWO-pair VLM program (`vlm-shots-v62.sh` + `clone-vlmshots-v62.sh` + `vlm-compare-v62.mjs` — the desktop 1280 full-page pair + the NEW mobile 390x844 full-page twin): the desktop pair five flags ALL arbitrated (nav-highlight root-URL gap / avatar / progress-bar data class / donut-labels PERCEPTION ARTIFACT [the reference renders its three 92.3-4.6-3.1, DOM-verified] / Base44 FAB); the mobile pair two flags both arbitrated (Base44 tooltip; "the clone subtitle wraps to a third line" — a PERCEPTION ARTIFACT, DOM-arbitrated via `arbit2-v62.sh`: the leaf-text census measured the subtitle P BOTH sides byte-identical [h 48, 2 lines, 16px/400/rgb(107,114,128), lh 24px, block h 92, top 121; the 5px width delta the reference own 395px docSW overflow] — the v61 meta-lesson INVERSE: the DOM census ACQUITTED what the VLM convicted). The v62 pin (+1 → 264): the mobile header-subtitle block census at 390 (`tests/e2e/dashboard.spec.ts`) — the P {h 48, top 121, 16px/400/gray-500, lh 24px, 2 lines} + the lineRhythm contract (the delta between the two line tops = exactly the 24px line-height — the glyph rects are ~19px font metrics, NOT pinned) + the block {h 92 = h1 36 + mb-2 8 + p 48, top 77} + the h1 {36/30px/700/mb 8px}; the WIDTH axis deliberately not pinned (the WRAP OUTCOME is the contract). ONE pin-sanity mutation verified to FAIL then restored (inline lineHeight 24→28px → h 48→56 + lineRhythm 24→28 + lh 28px, three axes; standalone REBUILD separate). F3: the SKILL doc four stale current-state count lines corrected (214→263 bootstrap / 223/223→263/263 gate / 223→263 decisions / 22 files-214→23 files-263 inventory — all 264 after the pin; historical rows stay era-correct). The 56th standing checks (the mobile menu verified working — the 56th time; the reference four bugs ALL live; the data census intact; the SEO pair live). The 16 screenshots: 10 byte-identical + 6 VLM-arbitrated (5 SEED-DATE [the item-view footers + details date row + networth Updated stamp, each +1 day, the dev DB re-seeded] + 1 sub-perceptual AA-timing [08-calculator, 1596px in a 57x73 bbox, full-shot + 3x-crop VLM both IDENTICAL]). PROBE LESSONS: the fresh-sandbox caveat (install Playwright browsers first); the text-range getClientRects() heights are GLYPH boxes (~19px for 16px font), NOT line boxes — the wrap rhythm lives in the line-top delta (= lh) + the element height; a pin expected geometry must come from the PROBE measured values, never derived arithmetic (the block-top 68-vs-77 miss: block top = P top − 36 − 8); the mobile full-page pair joins the standing VLM program. Full chain: lint + typecheck + 108 unit + build + 264 e2e (95 + 93 + 75, three ordered chunks) + 35/35 smoke green. The docs aligned (AGENTS/CLAUDE/README/SKILL Session 97 row + the 264 state/PAD v1.1.19/the probe README v62 section/session_151/the repo worklog Session 96). One new e2e, 263 to 264, 108/264/35 green |
| 2026-10-15 | Session 98 — parity iteration v63 (`docs/remediation-plan-v63.md`) | **The /networth mobile 390 full-page pair (the standing-pair matrix COMPLETED) + the networth summary card's stat-tile family census pin + the axe-core version-drift re-check (PIN-ONLY — no production-code change; the pin-only line continues)** (1 new e2e + three pin-sanity mutations; the session-149/151 v63 queue's two items — the standing-pair program's remaining minor surface [a /networth 390 full-page pair, the LAST un-paired viewport × view combination] and the axe-core version-drift re-check). **The pair matrix is now COMPLETE**: {dashboard, items (income/expenses), savings, calculator, networth} × {1280 desktop, 390 mobile} all paired (v56–v62 for the rest; the v63 pair closes it). The /networth 390 pair (`vlm-shots-v63.sh` + `clone-vlmshots-v63.sh` + `vlm-compare-v63.mjs`): VERDICT DIFFERENT with THREE flags, ALL DOM-arbitrated via `arbit-v63.sh` to documented classes — (1) "stat tiles side-by-side (ref) vs stacked (clone)" = the v41 mobile-superset class re-measured live (the reference's card 432-wide inside its own 464 docSW overflow renders its fixed 2-col grid [cols "175.828px 175.844px", tiles 176×84]; the clone's 358-fit card stacks 1-col [cols "294px", tiles 294×84] — the v4 data-fit superset); (2) "the clone's summary card is taller" = the direct arithmetic of (1) (the reference's h 333 + the second 84px tile row + the 16px gap = the clone's 421); (3) "the trend-icon circle appears larger in the clone" = a PERCEPTION ARTIFACT of the v54 clipping class (the medallion BYTE-IDENTICAL 64×64 + the trending-up icon BYTE-IDENTICAL 32×32 on both sides — the reference's medallion sits at right 416 in its 464-overflowing page, 26px PAST the 390 viewport edge [clipsViewport:true, partially rendered]; the clone's sits fully in-bounds at right 342 — the VLM read the reference's clipped medallion as "smaller"). The data differences the expected classes (1 asset vs the 3+2 seed; "∞:1" vs "0.21:1" — the pinned formatRatio contract; the Base44 tooltip — platform chrome). The axe-core version-drift re-check: **NO DRIFT** — the pinned `@axe-core/playwright@^4.13.0` resolves to 4.13.0 which is STILL npm-latest, and the engine that actually executes the AxeBuilder scans is the wrapper's NESTED `axe-core@4.13.0` (byte-identical to the v38/v62 audits); the top-level `axe-core@4.14.0` belongs to `eslint-plugin-jsx-a11y` (lint-time static analysis, never scans pages); the next re-check point is a 5.x wrapper release or an engine bump inside the wrapper's nested dep. The v63 pin (+1 → 265): the networth summary card's STAT-TILE family census at 390 (`tests/e2e/networth.spec.ts`, extending the v41 F3 describe — the stat grid {cols "294px", gap "16px", w 294, 2 children}, the tiles {294×84 each; bg rgba(255,255,255,0.1), backdrop blur(10px), radius 12px, pad 16px}, the card HEIGHT 421 [the 1-col stacking arithmetic], the medallion's inner icon 32×32). THREE pin-sanity mutations verified to FAIL then restored (the stat grid gap-4→gap-2 [gap 16→8 + card h 421→413]; the tile p-4→p-2 [tile h 84→68]; the medallion svg h-8 w-8→h-6 w-6 [icon 32→24] — each with the standalone REBUILD as a SEPARATE command). The 57th standing checks (the mobile menu verified working — the 57th consecutive time; the reference's four bugs ALL live; the data census intact — the 57th clean drift check; the SEO pair live). The 16 screenshots BYTE-IDENTICAL (no re-seed this session). PROBE LESSONS: the VLM's size judgments on CLIPPED elements are unreliable — a byte-identical element partially cut off by its own page's overflow reads "smaller" (always read the bounding rect AND the viewport-clipping boolean before believing a "larger/smaller" flag); the pair-matrix completion rule — the last un-paired viewport × view combination is never "minor" (its three flags needed three separate documented classes to arbitrate). Full chain: lint + typecheck + 108 unit + build + 265 e2e + 35/35 smoke green. The docs aligned (AGENTS/CLAUDE/README/SKILL Session 98 row + the 265 state/PAD v1.1.20/the probe README's v63 section/session_153/the repo worklog Session 97). One new e2e, 264 to 265, 108/265/35 green |
| 2026-10-15 | Session 99 — parity iteration v64 (`docs/remediation-plan-v64.md`) | **The OLDEST desktop pair's fresh standing sweep (the v57-era items pair re-run) + the axe-core 5.x wrapper watch (NO DRIFT) + the income filter-card computed census pin (PIN-ONLY — no production-code change; the pin-only line continues)** (1 new e2e + three pin-sanity mutations; the session-153 v64 queue's first two items — the re-run cadence on the OLDEST desktop pairs ["v57's items pair and v58's savings pair predate the v61 dashboard fix and the v62/v63 mobile twins — a fresh standing sweep of one of them"] and the axe-core 5.x wrapper watch [F1's documented next re-check point]) plus the 58th standing checks. The fresh items pair (`vlm-shots-v64.sh` + `clone-vlmshots-v64.sh` + `vlm-compare-v64.mjs`, FULL-PAGE both views at 1280×800): PAIR 1 (income) VERDICT DIFFERENT with the avatar (the user-identity class) + the Base44 FAB (the platform-chrome class — the VLM CONTRADICTED ITSELF between the two pairs, attributing the FAB to the clone in pair 2; either way platform chrome, excluded by rule) + the seed data (its 1 income item vs the clone's 2-item seed); PAIR 2 (expenses) VERDICT DIFFERENT with THREE style flags, ALL DOM-arbitrated via `arbit-v64.sh` (the computed census on both sides) to documented classes — the card footer content (the v57 DATA-CONDITIONAL class re-measured live: the footer chrome BYTE-IDENTICAL [flex justify-between 12px rgb(107,114,128) h 16; every child span flex gap 4px with the 12×12 gray icon]; the reference's expense items carry no paymentMethod values so their footers render ONE child [the date alone], the clone's carry them and render the SAME two-child structure the reference's OWN income card renders [measured live: "Oct 7, 2026" + "Bank Account"]), the badge arrangement (the v57 wrap data class re-measured: the badge chrome BYTE-IDENTICAL [flex/6px radius/2px 10px pad/12px-600/h 22; the row flex wrap 8px gap mb 12px]; the clone's Recurring superset badge wraps the row to h 52 = 22+8+22), and the grid population (the seed-count data class: the grid axes BYTE-IDENTICAL [w 960, gap 16px, the template "309.328px 309.328px 309.344px" — the SAME fractional last track both sides]; the reference's 4 cards vs the clone's seed's 3) — plus the card heights (200 vs 230 = the badge-wrap arithmetic data class, the documented never-pinned family). **The pair is CLEAN: every flag arbitrates to a documented class.** The axe-core 5.x wrapper watch: **NO DRIFT** — the npm-latest `@axe-core/playwright` is STILL 4.13.0 (no 5.x release exists), the wrapper's NESTED engine `axe-core@4.13.0` (what AxeBuilder actually executes) byte-identical to the v38/v62/v63 audits, the top-level 4.14.0 still eslint-plugin-jsx-a11y's (lint-time only); the next re-check point unchanged. The v64 pin (+1 → 266): the INCOME view's filter-card COMPUTED census at 1280 (`tests/e2e/items.spec.ts`, inside the income describe right after the early-era class-string filter-card test) — the never-census'd sibling of the v38 S2 savings pin (v37/v38 measured the /expenses triggers + the /savings instance; the v52 F2 pin covered this card's MOBILE 390 state; the early-era test pins CLASS STRINGS only): the card 960×86 (pad 24px/radius 16px/white/border rgb(229,231,227)/mb 24px — the 24+36+24+2 height arithmetic), the search 447×36 (the 2-col span 215.5+16+215.5; the asymmetric 40px left pad — the icon's room, pl-10; radius 6px/border rgb(229,229,229)), the inner grid 4 tracks "215.5px"/16px gap/3 children, the comboboxes 216×36 at 14px ("All Categories"/"All Frequencies"). THREE pin-sanity mutations verified to FAIL then restored (the card p-6→p-4 [pad 24→16 + h 86→70]; the search wrapper md:col-span-2 removed [search w 447→215.5]; the grid gap-4→gap-2 [gap 16→8 + the tracks recompute 215.5→221.5] — each with the standalone REBUILD as a SEPARATE command). The 58th standing checks (the mobile menu verified working — the 58th consecutive time; the reference's four bugs ALL live; the data census intact — the 58th clean drift check; the SEO pair live). The 16 screenshots BYTE-IDENTICAL. PROBE LESSONS: a VLM can contradict itself on the SAME platform-chrome element between two pairs in one comparison run (the Base44 FAB "missing from the clone" in pair 1 vs "present in the clone" in pair 2) — platform chrome is excluded from comparisons by rule, never arbitrated; the re-run cadence on an OLD pair re-proves the documented data classes live (the v57 conditional-footer + wrap contracts re-measured byte-identical five iterations later); a never-census'd sibling can hide behind an early-era CLASS-STRING pin (the income filter card looked pinned — the class strings were, the computed geometry was not). Full chain: lint + typecheck + 108 unit + build + 266 e2e + 35/35 smoke green. The docs aligned (AGENTS/CLAUDE/README/SKILL Session 99 row + the 266 state/PAD v1.1.21/the probe README's v64 section/session_155/the repo worklog Session 98). One new e2e, 265 to 266, 108/266/35 green |
| 2026-10-15 | Session 100 — parity iteration v65 (`docs/remediation-plan-v65.md`) | **The OLDEST remaining desktop pair's fresh standing sweep (the v58-era savings pair re-run) + the axe-core 5.x wrapper watch (NO DRIFT) + the savings page-header row computed census pin (PIN-ONLY)** — the session-155 v65 queue's two items + the 59th standing checks. The fresh savings pair (FULL-PAGE 1280×800): every flag DOM-arbitrated to documented classes — the avatar (the user-identity class with a NEW perception lesson: the chrome BYTE-IDENTICAL [36×36/9999px/14px-600/white/bg rgb(143,188,63) BOTH sides]; only the initial differs ["U" vs "D"]; the VLM's "green vs lime" a PERCEPTION ARTIFACT — identical computed colors read as different hues), the grid (the seed-count class; the axes BYTE-IDENTICAL; the fractional last-track CONTENT-COUNT-CONDITIONAL — the axes are the contract, never the subpixel tail), the footer/badges/card-heights (the v57 DATA-CONDITIONAL + wrap classes re-measured byte-identical), and the Add button's shadow (the v4 lead-layer form over the .zb-btn-add visible layers — the v11 class). **The pair CLEAN.** DOM discovery: the reference's hidden zero-size h1 "ZeroBalance" (its SEO pattern) precedes its VISIBLE 30px/700 h1 — filter h1s by non-zero geometry. The axe watch NO DRIFT (still 4.13.0, no 5.x; the nested engine byte-identical). The v65 pin (+1 → 267): the savings PAGE-HEADER ROW computed census at 1280 — the never-census'd family (v42 pinned the MID-640 stacked state; v63 the 390 networth block; the early-era tests pin class strings): the row flex space-between/center/16px/32px/h 60 + the chip 48×48/12px/blue gradient + the white 24×24 icon + the h1 30/700/36/forestDark + the subtitle 16/400/gray-500 + the Add button 150×36/6px/8px 16px/14px-500/white + the 16×16 plus. THREE mutations verified to FAIL (mb-8→mb-4; h-12 w-12→h-10 w-10; text-3xl→text-2xl [the row h 60→56 — the text block governs]). The 59th standing checks: the mobile menu verified working (59th time), the reference's four bugs ALL live, the data census intact. The 16 screenshots BYTE-IDENTICAL. — 108/267/35 green |
| 2026-10-16 | Session 101 — parity iteration v66 (`docs/remediation-plan-v66.md`) | **The v59-era pair's fresh standing sweep (the calculator dialog + login view re-run at 1280) + the axe-core 5.x wrapper watch (an upstream 4.14.0 appears — local NO DRIFT) + the calculator dialog's HEIGHT-family computed census pin (PIN-ONLY — no production-code change; the pin-only line continues)** — the session-159/160 v66 queue's two items + the 60th standing checks. The fresh calculator pair (the clone half adds the matching "Contents Insurance" $25 line item through the real UI then FULLY restores the fixture): VERDICT DIFFERENT with 2 style flags, BOTH DOM-arbitrated via `arbit-v66.sh` + `arbit-v66b.sh` (the computed census on both sides, the row-HEIGHT family added) to documented classes — the row actions (the POINTER-POSITION class: the actions rest at opacity 0 on BOTH sides [btnCount 2 each]; the reference's screenshot caught the pair mid-reveal — the pointer had rested inside the dialog at shot time, a capture-timing artifact) and the "• Will update category total" span (the DATA-CONDITIONAL class: renders while total !== item.amount; the reference's OWN Rent is natively $25.00 and its single line item sums to $25.00 → HIDDEN; the clone's modal snapshot carries the opened-at parent $1850 against the recalculated $25.00 → SHOWN — the conditional itself the pinned contract); plus the panel's computed box-shadow censused (the reference's two LEADING zero-alpha layers — the Tailwind v4 computed-form class — over the clone's .zb-modal-panel visible layer: the documented accepted lead-divergence class). The fresh login pair: **VERDICT IDENTICAL** — only the reference's "Edit with Base44" FAB (platform chrome, excluded by rule); the census byte-for-byte (title "ZeroBudget", h1 "Welcome to ZeroBudget", the same placeholders, Sign in 368×48, no `<a>` either side). **The pair CLEAN.** The v66 census's own discovery — the never-pinned HEIGHT family (the v45 F2a pin covered width/pad/radius/border + hover reveal, the v53 pin the 390 reflow, the v59 pin the panel + totalCard w/bg/radius/pad/border — NEVER the heights), measured BYTE-IDENTICAL both sides: the row **720×102** (the deterministic arithmetic: the 32px top-actions row + the h4's 4px mb + the 28px amount block + the 32px p-4 + the 2px border), the name h4 (16px/600/rgb(26,58,46)/h 24/mb 4px), the badge pill row (flex/gap 8px/12px/h 20), the first pill (h 20/w 65/pad 2px 8px/radius 9999px/12px/400), the amount P (20px/700/rgb(224,122,59)/h 28), the totalCard **h 90** (32+8+16+32+2 — the height arithmetic of the v59-pinned chrome). The axe watch: **local NO DRIFT** (the lockfile resolves 4.13.0; the nested engine byte-identical to v38/v62/v63/v64/v65; the top-level 4.14.0 still eslint-plugin-jsx-a11y's — lint-time only) — **BUT the npm registry now carries `@axe-core/playwright@4.14.0`** (a MINOR bump inside 4.x, NOT the guarded 5.x; the pinned ^4.13.0 would admit it on an unconstrained fresh install but the lockfile holds the tree) — recorded as the candidate for a future DEDICATED upgrade iteration (bump deliberately + re-run the a11y gate + re-audit rule coverage — never a side-effect drift); the next re-check point unchanged. The v66 pin (+1 → 268): the calculator dialog's HEIGHT-family computed census at 1280 (`tests/e2e/calculator.spec.ts`, a new describe after the v59 panel-census block, riding the add-then-restoreRent fixture flow): the row 720×102/pad 16/radius 12/border rgb(229,231,227)/bg white, the name h4 16/600/forestDark/h 24/mb 4, the pill row flex/gap 8/12px/h 20, the first pill 20/65/2px 8px/9999px/12px/400, the amount P 20/700/orangeDark/h 28, the totalCard 720×90. THREE mutations verified to FAIL then restored (the row p-4→p-2 [pad 16→8 + h 102→70 — caught by the v66 pin AND the v45/v49/v53/v59 pins, 6 failures]; the h4 mb-1→mb-2 [the nameH4 mb axis 4→8]; the totalCard p-4→p-2 [h 90→58] — each with the standalone REBUILD as a SEPARATE command). The 60th standing checks (`ref-standing-v60.sh` + `standing-checks-v60.sh`, version-bumped from the v59 family): the mobile menu verified working (the 60th consecutive time), the reference's four bugs ALL live, the data census intact (the 60th clean drift check), the SEO pair live. The 16 screenshots: 15 byte-identical + 1 (07-add-item-modal) the documented dialog-default DATE class re-arbitrated with a STRONGER method — a programmatic pixel-diff localized the change to a 16×22 px region at (1552,931)–(1568,953), exactly the date input's day digits "15"→"16" (the calendar rolled past midnight); everything else byte-stable — a pixel diff beats a VLM verdict for a single-region change. PROBE LESSONS: the VLM's "shorter row" was a perception artifact (the row 720×102 BOTH sides — always measure the computed heights before believing a proportion claim); the fresh-login first fetch can exceed the wait window (retry the finder on a warm session — the reference's /expenses rendered "0 items" transiently before the data landed); the height arithmetic is deterministic (32+4+28+32+2 = 102 — a pin on the parts makes the whole predictable). Full chain: lint + typecheck + 108 unit + build + 268 e2e + 35/35 smoke green. The docs aligned (AGENTS/CLAUDE/README/SKILL Session 101 row + the 268 state/PAD v1.1.23/the probe README's v66 section/session_161/the repo worklog Session 100). One new e2e, 267 to 268, 108/268/35 green |
| 2026-10-16 | Session 102 — parity iteration v67 (`docs/remediation-plan-v67.md`) | **The v60-era pair's fresh standing sweep (the networth view + the dashboard drill-down EXPANDED re-run at 1280) + the axe-core 5.x wrapper watch (local NO DRIFT — the upgrade DECISION: v68 = the dedicated upgrade iteration) + the networth summary card's HEIGHT-family computed census pin (PIN-ONLY — no production-code change; the pin-only line continues)** — the session-161/162 v67 queue's two items + the 61st standing checks. The v60-era re-run covers BOTH of that era's pairs (the v66 precedent: the v59-era re-run covered the calculator + login set). The fresh networth pair (FULL-PAGE 1280×800): **VERDICT IDENTICAL** — the VLM found ZERO layout/style differences ("pixel-perfect matches" on the nav rail, the page header, the summary card geometry/gradient, the tab bar, the card layouts, the typography, the spacing); every difference the expected DATA class (the figures, the counts, the group headers, the ratio "∞:1" vs "0.21:1", the avatar letter) + the "Edit with Base44" FAB (platform chrome, excluded by rule). The fresh drill-down EXPANDED pair: VERDICT DIFFERENT with 5 style flags, every one DOM-arbitrated via `arbit-v67.sh` + `arbit-v67b.sh` (the two-part computed census on both sides — the five flags + the networth summary-card HEIGHT family) to documented classes — the Dashboard nav highlight (the root-URL active-nav gap, re-confirmed live: the reference transparent/zinc-700/400 vs the clone transparent/white/500 — the superset contrast #3), the avatar ("U" vs "D" — the user-identity class), the hero progress-bar fill (the pct × 568 data class re-measured live: the track 568×12 rgba(255,255,255,0.1) BYTE-IDENTICAL both sides, the fills 173/357 = each site's own allocation pct), the donut percentage labels (the PERCEPTION ARTIFACT re-confirmed live: both sides render count 4 [1 group + 3 labels]/labelLineCount 0/16px/black/3 sectors — the v9 G1b contract holds; the values each site's own data), and the stat cards' footer TREND ICONS (a NEW flag variant — "different paths/angles" — DOM-arbitrated to a PERCEPTION ARTIFACT via a GLYPH census: the icons are BYTE-IDENTICAL, 16×16/rgb(143,188,63)/viewBox "0 0 24 24" with the same two-polyline Heroicons-v1 outline trending-up — POLYLINE-based, no `<path>` element, which is why the census needs the innerHTML glyph signature; plus the hero-glyph census: the same 7 svgs in the same order on both sides, every path signature byte-identical). **The pair CLEAN: every flag arbitrates to a documented class or a measured perception artifact.** The arbitration's own discovery — the never-pinned HEIGHT family (the v60 F1 pin covered the card's width/pad/radius/gradient/shadow + the fonts + the grid template/gap, the v63 F3 pin the stat-tile heights at 390 — NEVER the 1280 heights), measured BYTE-IDENTICAL both sides: the card **960×333** (the deterministic arithmetic 32 + 76 + 32 + 84 + 24 + 24 + 1 + 28 + 32), the head row **h 76** (the label h 20 + mb 8 + the figure h 48 govern; the 64px medallion rides), the figure **h 48** (lh 48px), the stat grid **rows "84px"/h 84** (ONE row at 1280 — the 390 twin's two-row 184 is the v63 class), the stat tile **440×84** (pad 16 + the label 16 + mb 4 + the amount 32 + pad 16), the ratio footer **mt/pt 24/24 + border 1px + h 53** (the pt 24 + the border 1 + the ratio row 28 — text-lg's 28px lh). The axe watch: **local NO DRIFT** — the registry state unchanged from v66 (npm-latest 4.14.0, its declared nested engine `axe-core ~4.14.0` verified by packing the tarball), the lockfile resolves 4.13.0, the NESTED engine `axe-core@4.13.0` byte-identical to the v38–v66 audits, the top-level 4.14.0 still eslint-plugin-jsx-a11y's (lint-time only) — **and the upgrade DECISION (the queue's item #2): the 4.14.0 upgrade is DEFERRED TO A DEDICATED v68 ITERATION** (never a drift, never a rider: the upgrade changes the toolchain the a11y.spec.ts contract executes under and deserves an iteration whose center of gravity is the toolchain change with its full re-verification chain — the pin bump `^4.13.0`→`^4.14.0` + the lockfile regeneration + the nested-engine verify + the full a11y gate re-run + the rule-coverage re-audit [diff the activated rule sets axe-core 4.13.0 vs 4.14.0, arbitrate any new violations: a real markup issue → fix + pin; a rule-behavior change → pin accordingly] — the complete specification carried in the v67 plan's v68 queue); the watch's next re-check point unchanged. The v67 pin (+1 → 269): the networth summary card's HEIGHT-family computed census at 1280 (`tests/e2e/networth.spec.ts`, a new describe after the v60 F1 block, the read-only logged-in state — no fixture flow needed): the card 960×333, the head row h 76/mb 32px, the label mb 8px/h 20, the figure lh 48px/h 48, the medallion h 64/iconH 32, the stat grid rows "84px"/h 84, the stat tile h 84/labelH 16/labelMb 4px/amtH 32, the ratio footer mt 24px/pt 24px/borderTopW 1px/h 53. THREE pin-sanity mutations verified to FAIL then restored (the head row mb-8→mb-4 [mb 32→16 + card h 333→317]; BOTH stat tiles p-4→p-2 [pad 16→8 + tile h 84→68 + grid rows "84px"→"68px" + card h 333→317 — the shared-class regression; a FIRST-tile-only mutation does NOT move the axis: the tile height is STRETCH-GOVERNED, the grid row follows the taller p-4 sibling and stretches the p-2 tile back to 84, measured live — pad 8px + h 84 on the mutated tile beside its p-4 sibling]; the ratio footer mt-6 pt-6→mt-3 pt-3 [mt/pt 24→12 + footer h 53→29 + card h 333→309] — each with the standalone REBUILD as a SEPARATE command). The 61st standing checks (`ref-standing-v61.sh` + `standing-checks-v61.sh`, version-bumped from the v60 family): the mobile menu verified working (the 61st consecutive time), the reference's four bugs ALL live, the data census intact (the 61st clean drift check), the SEO pair live. The 16 screenshots BYTE-IDENTICAL (no production-code change; the capture date matching the committed set's). PROBE LESSONS: the single-quote-selector rule bites BOTH ways (the v60 lesson #1 applies inside the quoted-heredoc clone script too — the eval argument is itself a single-quoted bash string; use double-quoted attribute-value selectors like closest("[class*=grid]")); a `const` census variable assigned in a walk-up loop throws "Assignment to constant variable" and, with stderr discarded, the ONLY signature is the EMPTY eval line between the === markers (debug with stderr visible); a childless-div finder fails on container tracks (the hero progress TRACK carries the fill as a child — drop the !children.length requirement); the reference's Heroicons-v1 trend glyph is POLYLINE-based (no `<path>` — a glyph census needs the innerHTML signature, a path `d` signature returns null); the stat tile's height at 1280 is STRETCH-GOVERNED (the grid row = the taller sibling; both tiles stretch to it — a single-tile pad mutation leaves the pinned axis untouched, the mutation must be the shared-class regression, and the stretch explains the arithmetic's stability: both tiles share the content structure so the row = either tile's natural height). Full chain: lint + typecheck + 108 unit + build + 269 e2e + 35/35 smoke green. The docs aligned (AGENTS/CLAUDE/README/SKILL Session 102 row + the 269 state/PAD v1.1.24/the probe README's v67 section/session_163/the repo worklog Session 101). One new e2e, 268 to 269, 108/269/35 green |
| 2026-10-16 | Session 103 — parity iteration v68 (`docs/remediation-plan-v68.md`) | **The DEDICATED axe-core wrapper upgrade (the deliberate ^4.13.0→^4.14.0 pin bump + the lockfile regeneration [the nested engine dissolves — npm dedupe; ONE axe-core in the tree] + the engine verify 4.14.0 + the full a11y gate re-run green [the v38 contract holds] + the rule-coverage re-audit [69 of 105 rules activated on BOTH engines — the sets byte-identical, zero added/removed]) + the v61-era pair re-run (the dashboard full-page 1280 — VERDICT IDENTICAL, zero style flags) + the ENGINE-CONTRACT pin (+1 = 270: testEngine.version asserted at 4.14.x on a real scan — "never a drift" made executable; the toolchain-downgrade sanity mutation proven to fail) + the 62nd standing checks (the mobile menu working, the 62nd consecutive time; the reference's four bugs all live)**. |
| 2026-10-16 | Session 104 — parity iteration v69 (`docs/remediation-plan-v69.md`) | **The mobile 390 pair re-run (the networth full-page twin — the documented queue item — PLUS the dashboard mobile twin, the other never-re-run mobile pair, both in one two-pair iteration) + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only 4.14.1 rc/next prereleases, no 5.x; the lockfile holding the v68 dedupe state; the engine-contract pin green) + the networth view's PAGE-HEADER ROW computed census pin (PIN-ONLY for src/, +1 = 271) + the F0 lint-gate repair (the v68 ship's own miss — the seedcheck .cjs, the repo's only CommonJS file, was committed after v68's final lint run and tripped @typescript-eslint/no-require-imports; repaired with a single-file eslint-disable, the gate staying strict for the rest of scripts/)**. Both mobile pairs CLEAN, every flag DOM-arbitrated via `arbit-v69.sh`: the networth re-run's three flags = the v63-era classes re-confirmed live with the EXACT v63 numbers (the stat-tile stacking [the v41 mobile-superset class: the reference's 2-col 176×84 in its 432 card inside its own 464 overflow vs the clone's 1-col 294×84 in its fitting 358 card]; the trend icon [the v54 clipping perception artifact — the medallion 64×64 + the icon 32×32 BYTE-IDENTICAL both sides, the reference's clipping at right 416, the clone's fitting at 342]; the Base44 overlay [platform chrome]); the dashboard re-run's flags = the Base44 tooltip [platform chrome] + the subtitle wrap [the documented v62 class — the chrome BYTE-IDENTICAL (the subtitle P h 48, top 121, 16px/400/gray, lh 24px, block h 92 — the exact v62 pin values), the reference's own docSW 395 overflow giving its block 363 vs the clone's 358, the 5px shifting its wrap point by one word] + a NEW flag variant DOM-DISPROVEN ("the reference's Net Zero Breakdown card contains a donut" — ZERO donut on EITHER side: rechartsWrappers 0, pieSectors 0 both; the card h 324 both sides [the v42 census value]; the 7 svgs the BYTE-IDENTICAL 16×16/14×14 row icons — a perception artifact, the DOM census the ground truth per the v43 rule). The v69 pin (`tests/e2e/networth.spec.ts`, a new describe at the file tail, the logged-in read-only state, measured live via `nw-header-v69.sh`): the row flex/center/gap-3 12px/mb-8 32px/w 358/h 60 — the TEXT BLOCK governs the row height (the h1 36 + the subtitle 24), not the 48px chip (the v65 lesson); the chip 48×48/rounded-xl 12px/the forest-medium→lime 135deg gradient rgb(45,90,74)→rgb(143,188,63) + the 24×24 white TrendingUp; the h1 30px/700/lh 36px/forestDark rgb(26,58,46)/h 36/x 76; the block w 250 (the subtitle's max-content governs)/h 60; the subtitle 16px/400/gray-500 rgb(107,114,128)/lh 24px ONE line; the row→card gap 32 (the v41 rhythm); docSW 390 (the superset — the reference overflows to 464, its R-bug-4). GREEN on first run; THREE pin-sanity mutations verified to FAIL then restored (the row mb-8→mb-4 [mb 32→16 + the gap 32→16]; the chip h-12 w-12→h-10 w-10 [48→40 + the h1 x shift]; the h1 text-3xl→text-2xl [fs 30→24 + lh 36→32 + block h 60→56 + row h 60→56] — each with the standalone REBUILD as a SEPARATE command). The 63rd standing checks clean (the mobile menu verified working — the 63rd consecutive time; the reference's four bugs all live; the data census intact — the 63rd clean drift check; the SEO pair live). The 16 screenshots 16/16 BYTE-IDENTICAL (the first fully-identical set since v65 — the v68 re-seed and the v69 capture share the 2026-10-16 calendar day). Probe lessons: one-shot Prisma scripts need `env -u DATABASE_URL` (the sandbox's inherited parent-workspace URL broke the seedcheck's first run — the documented pollution applies beyond the npm scripts); the VLM can invent a chart inside a card that carries none on either side — a chart-presence claim needs the recharts-wrapper/sector census, not a screenshot read; a wrap-point difference with byte-identical chrome is a width-delta class — measure the block width + docSW before believing a typography flag. — 108/271/35 green |

| 2026-10-12 | Session 89 — parity iteration v54 (`docs/remediation-plan-v54.md`) | **The savings goal-card's badge-row + footer internals at 390 (PIN-ONLY — the third consecutive pin-only iteration; no production-code change)** (1 new e2e, TDD with five pin-sanity mutations; the session-125 v54 queue's first read-only member: the goal-card internals BEYOND the v51 F3 chrome pin). F1 (`tests/e2e/items.spec.ts`) — the GOAL-CARD INTERNALS at 390: byte-parity on every chrome axis (the header row flex/gap 8/mb 4/center; the dot 8×8/9999/rgb(59,126,161) — the savings TYPE accent on BOTH sites, the reference colors its dot by TYPE not classification, its need-classified goal still carries the teal savings dot; the BADGE ROW flex/wrap/gap 8/mb 12; every CHIP h 22/radius 6/pad 2px 10px/12/600 with the 12×12 icons at mr 4 — the "monthly" chip w 78 and the "active" chip w 63 on BOTH sites, the byte-parity width proof, the same text at the same chrome renders the same width; the FOOTER flex/space-between/12/rgb(107,114,128)/h 16 + the date span flex/gap 4/12 with the 12×12 calendar icon at gray) — the chip COUNT (the reference's 3 vs the seed's 4 — the Recurring chip), the row HEIGHT (22 vs 52, the wrap), and the payment span (the reference's goal carries none) are the documented DATA classes. FIVE PIN-SANITY MUTATIONS VERIFIED TO FAIL (the badge row's gap-2→gap-4 [8→16]; the chip's px-2.5→px-1.5 [pad 2px 10px→2px 6px]; the chip's text-xs→text-sm [h 22→26]; the footer's text-xs→text-sm; the date span's gap-1→gap-2 [4→8]) — each with the standalone REBUILD as a SEPARATE command (the v53 lesson). Standing checks all clean (48th): mobile-nav R1–R4 both sites (the mobile menu verified working: R1 burger hit-test true + the 5-link sheet, the Income nav closes AND navigates, Escape closes; the reference's four bugs ALL live — the toast-blocker [the fixed z-[100] toast viewport eats the burger's center hit], the sheet-trap [overlayCount 1 after nav], the no-landmark, the 464 /networth overflow), the data census intact, the SEO pair live on both. The VLM pair on BOTH the /networth tablist (the v53 F1 surface — the session-125 standing-check suggestion) AND the savings goal card (THE F1 surface): every flag DOM-verified (the active tab bg byte-identical rgb(220,252,231) — a screenshot-perception artifact; the Add button's full "Add Asset" text on both sites, scrollW 134 = clientW 134, no truncation — a small-text misread; the trend icon = the documented 464-overflow width class — the reference's 32×32 trending-up clips at its page's right edge, the clone's sits fully in-bounds; the rest = the seed-data/platform classes) — the pair CLEAN per the v43 rule. PROBE LESSONS: (1) a generic justify-between + svg footer finder matches the card's HEADER row first (the header also carries justify-between + the kebab svg — the first census read the header's 16px/48px geometry as the "footer" and an empty kebab as the "payment span"; the fs-16/h-48 signature is the tell-tale) — the footer locator is "the LAST justify-between direct child WITHOUT an h4"; (2) the chips' inline-flex SOURCE class computes to "flex" as flex items (CSS blockification — an `inline-flex` child of a flex container is blockified) — a census finder checking display === "inline-flex" finds nothing; (3) the fresh-clone environment needs `npx playwright install chromium` (the headless-shell binary is per-Playwright-version — 1243 this session; the first a11y run failed 21-wide on browserType.launch). Full chain: lint + typecheck + 108 unit + build + 248 e2e (+1, run as two ordered chunks 141+108; both exit 0, zero failures) + 35/35 smoke green. The 16 screenshots regenerated (ZERO byte-diffs — the pin-only invariant); the docs aligned (AGENTS/CLAUDE/README/SKILL Session 89 row + the 248 state/PAD v1.1.11/the probe README's v54 section/session_128 + session_129/the repo worklog Session 88 + the ledger list). One new e2e, 247 to 248, 108/248/35 green |
| 2026-10-12 | Session 86 — parity iteration v51 (`docs/remediation-plan-v51.md`) | **The verify-email mode container's missing `.zb-auth-mode` conversion (THE FIX — the third production-code change since v46, completing the v50 F1's CLAIMED-but-never-applied third site) + four 390 pin surfaces (the stats row, the savings goal card, the Budget Guidelines card, the quick-actions row — ALL PIN-ONLY)** (5 new e2e, TDD with five pin-sanity mutations; the session-118 v51 queue's read-only members + two sibling sweep surfaces). THE v51 FIX (F1, `tests/e2e/verify-email.spec.ts`): the v50 plan (§F1), the v50 commit message, and all five docs stated "the verify-email branch's same-idiom container converted" — the v50 diff landed the DESCRIBING COMMENT at login-card.tsx:605-607 but the line-608 class swap itself never shipped; the verify branch still read `space-y-4`. Measured via a fresh CLONE-side registration (the reference stays read-only — the v46 rule): the verify panel 358×492 @ y 152 (16px SHORT vs the v3-stacking 508), the wrapper 540 (vs 556), the y 152 (vs 144), and the junction netGap −8 — the centered inner stack's top (196) sat 8px ABOVE the back button's bottom (204): the button's own `-mb-2` (−8) OVERRIDES v4's zero-specificity `:where(& > :not(:last-child))` margin-block-end (16) where the reference's v3 build STACKS them (the collapsed 16 + (−8) = the 8px NET gap) — the SAME drift the v50 F1 fixed for sign-up/forgot. The fix: the one-class swap the v50 plan specified (NO `.zb-sm6` — the reference's verify container carries no sm tier, the v21-measured structure; the existing globals.css `.zb-auth-mode` rules carry it). THE PIN (a NEW discipline finding): the verify panel's height is EMAIL-LENGTH-DEPENDENT — the "We've sent a 6-digit code to {email}" block wraps per the address length (a 38-char address wraps one extra line, +20px: the first GREEN attempt measured 528 not 508) — the pin uses a FIXED 21-char email (the global-setup re-seeds db/e2e.db every run, so the address is reusable). F2 (`tests/e2e/dashboard.spec.ts`) — the STATS ROW at 390: byte-parity (the 1-col/24px-gap grid; the three cards 358×210 @ y 949/1183/1417 — the rhythm byte-identical on both sites; the radius 16/pad 24/border/white + the rgba(0,0,0,0.06) 0px 4px 20px shadow; the 48px icon circle radius 12/rgba(143,188,63,0.125); the 24px icon; the title 14/500/gray/mb 4; the amount 30/700/forestDark/mb 16; the count row 14/gap 8; the 16px trend icon — the reference's 363-wide cards ride its own 395 docSW overflow, the clone's 358 fit). F3 (`tests/e2e/items.spec.ts`) — the SAVINGS view at 390: byte-parity (the goal card radius 12/pad 20/border/white + the rgba(0,0,0,0.04) 0px 2px 8px shadow; the H4 16/600/forest; the subtitle 14/400/gray; the amount 24/700/rgb(59,126,161); the 8×8 dot radius 9999px; the 1-col/16px-gap grid; the H1 30/700/forest; the sub 16/gray; the filter card 358/radius 16/pad 24; the search 308×36; docSW 390 — the card HEIGHT is a data class, NEVER pinned: the clone's richer seed renders 4 chips that wrap to 2 rows (the badges row 52px) where the reference's 3 chips fit 1 row (22px) — the 230-vs-200 diff fully accounted for by the seed). F4 (`tests/e2e/dashboard.spec.ts`) — the BUDGET GUIDELINES card at 390: byte-parity (the card 358×380/radius 12/border/white + the shadow-sm VISIBLE pair rgba(0,0,0,0.1) 0px 1px 3px / rgba(0,0,0,0.1) 0px 1px 2px -1px — the reference's FULL string re-measured UNSLICED: 2 transparent leads + the pair = 4 layers, the clone 4 leads + the pair = 6, the accepted lead-divergence class v10/v25/v45/v49/v50; the tiles container display BLOCK (the space-y-3 stack); the three tiles radius 8/pad 16/h 94/94/78 with the byte-identical tinted pairs — Needs rgb(255,247,245)/rgb(252,221,213)/rgb(224,122,59), Wants rgb(240,247,251)/rgb(212,233,245)/rgb(59,126,161), Savings rgb(245,249,240)/rgb(223,236,208)/rgb(143,188,63)). F5 (`tests/e2e/dashboard.spec.ts`) — the QUICK-ACTIONS row at 390: byte-parity (the 1-col/24px-gap grid with mt 32; the three cards 358×90 @ y 2751/2865/2979 — the 114px rhythm, the full-page vertical rhythm byte-identical through the whole dashboard on both sites; the radius 16/pad 24/border/white/shadow-none rest state; the 40×40 icon circle `w-10 h-10 rounded-xl` + rgba(143,188,63,0.125) + the group-hover:scale-110 transition-transform idiom; the 20×20 icon; the label 16/500/rgb(26,58,46); the trailing plus 16×16 at opacity 0.5 in the accent color — the reference's own `ml-auto opacity-50 group-hover:opacity-100 transition-opacity` class string read DIRECTLY from its DOM; the wrapper tag diverges — a DIV on the reference vs a SPAN on the clone, both `flex items-center gap-3`, tag-agnostic). FIVE PIN-SANITY MUTATIONS VERIFIED TO FAIL: the zb-auth-mode removed (the TDD RED run — the pre-fix proof, modeCls/panel/junction all bite); the stat card's rounded-2xl→rounded-xl (the F2 radius 16→12); the goal card's inline shadow removed (F3); the Needs tile's inline bg removed (F4 — also bites the 1280 tinted-cards pin); the quick-action circle's w-10 h-10→w-8 h-8 (F5 — the circle finder misses at 32) — each with the standalone REBUILD first (the v47–v50 lesson, pre-applied). Standing checks all clean (45th): mobile-nav R1–R4 both sites (Tailwind v4 pins hold, the mobile menu works; the reference's sheet-trap re-verified via the overlayCount census — the z-50 scrim remains on /income after the nav click; the toast-blocker via elementFromPoint; the no-landmark; the 464 /networth overflow), data drift (reference read-only, verified before + after: '1 items · $25,000' networth / '1 items · $5000.00' income), the SEO pair live on both sites. The VLM pair on the /savings view at 390 (THE F3 SURFACE): 3 flagged diffs, ALL DOM-verified as the documented seed-data classes (the count subtitle '1 items' vs '2 items'; the card contents — the reference's 1 Emergency Fund card vs the clone's 2 richer-seed cards; the extra-card layout length — the v48 precedent's second application, the chrome byte-pinned by F3). Probe lessons: the verify panel's height is email-length-dependent (a fixed-length address keeps the absolute pins deterministic); Playwright does NOT typecheck (the `c.querySelector &&` TS2774 always-defined check passed at runtime but fails `next build`'s tsc — a new test file needs a build before the chain gate); the with-server heredoc KILLS its server at the end — every follow-up eval needs a fresh invocation (the mid-flow "Network error"); the sign-up form carries THREE inputs (email + password + Confirm Password — a probe that fills only the first two never submits); the reference's savings goal card title is an H4 but the page also carries a hidden desktop-sidebar H2 brand (the `h1, h2` finder hits the hidden 18px H2 first — the probe artifact, the visible top-bar brand is the 20px H1). Full chain: lint + typecheck + 108 unit + build + 241/241 e2e (+5, 5.6m; the not-found spec's flake family — a different test each full run, 7/7 standalone twice, clean on the third run) + 35/35 smoke green. The 16 screenshots regenerated; the docs aligned (AGENTS/CLAUDE/README/SKILL Session 86 row + the 241 state/PAD v1.1.8/the probe README's v51 section/session_119 + session_120/the repo worklog Session 85 + the ledger list). Five new e2e, 236 to 241, 108/241/35 green |
| 2026-10-12 | Session 85 — parity iteration v50 (`docs/remediation-plan-v50.md`) | **The auth states' panel heights (THE FIX — the second production-code change since v46) + the networth tablist's 640 chrome + the dashboard hero's 390 reflow (two PIN-ONLY surfaces)** (4 new e2e, TDD with five pin-sanity mutations; the session-115 v50 queue's three candidates). THE v50 FIX (F1, `tests/e2e/login-parity.spec.ts`): the clone's sign-up and forgot panels were 16px SHORT at every viewport (406 vs the reference's 422 / 294 vs 310, the wrapper 454/342 vs 470/358, the panel y 195/251 vs 187/243) — the v4 space-y trap-log rule 4 violation: the back button's OWN `-mb-2` (the reference's idiom) OVERRIDES v4's zero-specificity `:where(& > :not(:last-child))` margin-block-end where the reference's v3 build STACKS them (the collapsed 16 + (-8) = the 8px net gap; the pre-fix clone's heading overlapped the button by 8px AND the container lost 16px — the form heights were IDENTICAL, 286/126, isolating the drift to the button→heading junction). The fix (`src/app/globals.css` + `src/components/budget/login-card.tsx`): the scoped `.zb-auth-mode` restore (the SPACE-Y V3 SEMANTICS family's third member — v9 G3 / v24 G2) with the container DROPPING the space-y class entirely (unlike the v9/v24 restores which keep it and neutralize: a `> :not(:last-child) { margin-block-end: 0 }` zero at 0-2-0 specificity BEATS the button's own -mb-2 utility at 0-1-0 and kills the 8px collapse — the first fix attempt's measured 430, caught by the pin before it shipped) + the forgot's `.zb-sm6` modifier (the reference's own DOM class `space-y-4 sm:space-y-6` — 24px gaps at >=640, absent from the clone) + the verify-email branch's same-idiom container converted (the v21-inherited measurement; a fresh reference registration is a WRITE, out of bounds under the v46 read-only rule). The pins: the sign-up panel 422/wrapper 470/y 187 + the junction (the button h 20 mb -8 at y 0 / the H2 h 28 at y 28 — the net gap 8 / the form at y 72) + the forgot panel 310/wrapper 358/y 243 (the heading block 76 at y 28 / the form at y 120) + the 640 sub-check (the forgot container's heading mt 24px — the sm tier; the sign-up's stays 16). F2 (`tests/e2e/networth.spec.ts`) — the tablist's CHROME census at 640 (the v14 G2 pinned the icons + the existing 1280 test the grid/green pair; the v50 pin adds the mid-viewport + the full chrome): the list 448/36/display grid/cols "220px 220px"/bg rgb(245,245,245)/radius 8/pad 4/x 16; the active trigger 220×28/radius 6/fs 14/fw 500/color rgb(20,83,45)/bg rgb(220,252,231) + the shadow-sm VISIBLE pair `rgba(0,0,0,0.1) 0px 1px 3px 0px` / `rgba(0,0,0,0.1) 0px 1px 2px -1px` (the reference's FULL string: 2 transparent leads + the visible pair = 4 layers; the clone: 4 leads + the pair = 6 — the documented accepted lead-divergence class, v10/v25/v45/v49; the visible layers byte-identical); the inactive 220×28/#737373/transparent/shadow none; the 16×16 currentColor icons on both. F3 (`tests/e2e/dashboard.spec.ts`) — the hero's MOBILE reflow census at 390 (the v42 F2 pinned 640 only): the grid display grid/1 col (358px)/gap 24px/2 children; the goal card 358×316@y 253/radius 16/pad 32/the 135deg forest gradient/the shadow rgba(26,58,46,0.3) 0px 20px 60px; the breakdown card 358×324@y 593 (the 24px rhythm 253+316+24); the internals (the icon circle 48×48/rgba(143,188,63,0.2)/the 24px target icon at rgb(143,188,63); the H3 18/700/white/lh 28; the sublabel 14/rgba(255,255,255,0.6); the allocation label 14/rgba(255,255,255,0.8); the pct 18/600/white; the track h 12/rgba(255,255,255,0.1)/9999px; the fill's 90deg rgb(224,122,59)→rgb(245,169,98) under-budget gradient/9999px — the fill WIDTH and the figure TEXT data-dependent, never pinned; the balance box radius 12/pad 24/bg rgba(255,255,255,0.05)/blur(10px); the Balance label 14/0.6; the figure 30/700/white; the chip: the flex gap-8 center row + the span "Under Budget" 16/600 rgb(245,169,98) + the svg color rgb(245,169,98) — BOTH sites' `w-5 h-5` svgs SQUISH to 12px computed under the row's flex-shrink (the width-pressure artifact is byte-SHARED: the left figure block 158 + the chip 93 on both) — a data-pressure class, the pin locks the family; the reference's card w 363 rides its own 395 docSW overflow, the clone's 358 fits (docSW 390, the superset fix #4). FIVE PIN-SANITY MUTATIONS VERIFIED TO FAIL: the zb-auth-mode removed (both F1 tests — the TDD RED run); the -mb-2 removed (the net gap 8→16, the wrapper 470→478); the zb-sm6 removed (the 640 sub-check: the heading mt 24→16); the active-tab bg removed (F2); the hero track's h-3→h-2 (F3) — each with the standalone REBUILD. Probe lessons: a stale agent-browser session (a killed run leaves the `.config`/`.engine` pair) HANGS the next `open` on that session name — `pkill -f agent-browser` + a session-file sweep before every run; a rebuild swaps `.next/standalone` UNDER a running parity server (page loads die with the browser's "This page couldn't load" interstitial) — reboot the :3200 server after every build; the smoke script's cleanup kills ALL standalone servers (reboot after smoke); the VLM's 4 flagged diffs on the sign-up pair were ALL DOM-verified as noise (the panel y 187/h 422/the button 294@x 48 IDENTICAL — the v43 misattribution lesson's fifth application). Mobile-nav R1→R4 (44th — Tailwind v4 pins hold, the mobile menu works, both sites; the reference's sheet-trap re-verified with the precise overlay census — the z-50 rgba(0,0,0,0.8) 390×844 scrim still open on /income after the nav click), data drift (44th — reference read-only, verified before + after: '1 items · $25,000' networth / '1 items · $5000.00' income), the SEO pair (robots + sitemap live on both). — 108/236/35 green (4 new e2e, 1 production fix, TDD) |
| 2026-10-12 | Session 83 — parity iteration v48 (`docs/remediation-plan-v48.md`) | **The item-details sheet's shadow-2xl + the dialog-input focus composite at 390 + the empty-state full census — a PIN-ONLY iteration** (3 new e2e, TDD with four pin-sanity mutations; NO production-code change — the measured chrome was already at parity on every VISIBLE layer, the three pins lock it; the v45-family's FOURTH pin-only iteration). The surface (the session-108 queue #1 + #4 + #3): the item-details sheet's panel shadow census at 1280 (`tests/e2e/item-details.spec.ts`) — the panel 512×680 (the 85vh cap at an 800 viewport)/radius 16/max-w-lg/bg white with the v3 shadow-2xl VISIBLE layer `rgba(0, 0, 0, 0.25) 0px 25px 50px -12px` (the reference's 3-slot construction vs the clone's 5-slot — the accepted v10/v25/v45 lead-divergence class, at the 2xl end on the details surface — the shadow-scale regression net's SEVENTH site, joining the v45 login-panel 2xl), the overlay the v7 G6 forest scrim `rgba(26, 58, 46, 0.5)` + z 50 + blur(8px), the close button the v9 36×36 transparent X (its accessible name 'Close' via the sr-only span — the finder idiom); the dialog input's focus composite at 390 (`tests/e2e/dialog-buttons.spec.ts`) — the v47 F1's MOBILE follow-up: the input w 310 on BOTH sites (the mobile dialog's content width) with the same visible layers (the rest shadow-sm layer + under a REAL focus the 1px rgb(10,10,10) ring with the rest shadow persisting beneath it, the border unchanged, the 5-slot counts) — the focus family is viewport-independent on both sites; the empty-state FULL census via filter-to-zero at 390 (`tests/e2e/empty-states.spec.ts`) — the bare block at BYTE-PARITY: the container `py-16 text-center` 358×328/pad 64px 0px/transparent/no border, the icon 64×64/opacity 0.2/rgb(10,10,10)/mb 16, the H3 fs 20/fw 600/rgb(26,58,46)/mb 8, the P 16px/rgb(107,114,128)/mb 24, the Add button h 36/w 147/the 135deg gradient/pad 8px 16px/radius 6/fw 500 + v3's BARE shadow (the `.zb-btn-add` v11 G2a family). FOUR PIN-SANITY MUTATIONS VERIFIED TO FAIL: the panel's shadow-2xl removed → the F1 pin fails; the input's ring-1 removed → the F2 pin fails (shared class — also v47's F1); the icon mb-4 reverted to mb-2 → the F3 census fails (the container h 328→320); the `.zb-btn-add` shadow removed → the F3 pin fails — each mutation needs the standalone REBUILD before the run bites. Probe lessons: the reference's toast is RARE-PATH only (empty-form saves never toast — the clone's toasts are the documented superset UX, the v10 note; the queue's toast item resolved as superset-only); the reference's frequency Select carries non-matching options (One-time vs its monthly items — the read-only filter-to-zero trigger); the reference's empty-state Add button carries the gradient + v3 bare-shadow family (NOT the --shadow-sm navbar pin — the two shadow scales coexist by surface). Mobile-nav R1→R4 (42nd — Tailwind v4 pins hold, the mobile menu works, both sites), data drift (42nd — reference read-only, verified before + after: '1 items · $25,000' networth / '1 items · $5,000.00' income, the frequency filter reset verified), the SEO pair (robots + sitemap live on both), the VLM pair on the /savings view at 1280 (4 flags, all DOM-verified as data classes — the richer seed's 2-card grid, the Recurring/payment-method rows, the avatar initial; the badge chrome byte-identical: need's red chip = the clone's same map) — 108/229/35 green |
| 2026-10-11 | Session 77 — parity iteration v42 (`docs/remediation-plan-v42.md`) | **The mid-viewport census of the five routes + the breakdown card's single-divider fix — THE FIRST PRODUCTION-CODE CHANGE SINCE v41** (3 new e2e, TDD with three pin-sanity mutations). The surface (the session-90/91 queue — the v41 lesson applied to the remaining route set): the five non-networth routes (/, /dashboard, /income, /expenses, /savings) measured live on BOTH sites at 640×960 (mid-census-v42.mjs) — THE 32px RHYTHM HOLDS ON ALL FIVE ROUTES (gapRowToFirst === 32 everywhere, capW 608, sw 640, the items-view structure identical — the v20 G1 pin's class extended to the mid viewport). THE v42 PARITY FIX (F1): the NetZeroBreakdownCard ran +13px taller than the reference at BOTH viewports (640: 337 vs 324; 1280: 377 vs 364) — attributed band-by-band (hero-attrib-v42.mjs + bd-attrib-v42.mjs): the goalCard byte-identical (316, the bands 48/48/108, the donut 558×300), the row heights identical (56/64/64 at 1280 — the wrap is width-driven, not data-driven) — THE DELTA WAS ONE EXTRA DIVIDER: the clone rendered TWO (Income|Savings AND Savings|Expenses), the reference ONE (Income|Savings only — the app's ONE rule grouped: [Income] | [Savings, Expenses] | border-t | [Net Balance]). The fix is one condition: `{i === 1 && <Divider />}` (dashboard-view.tsx); every band below the hero shifts back 13px at 640 (secondBand 925, thirdBand 1635, scrollH 3029 — the tail-v42.mjs check proved the delta was the divider alone, the lastBand mb=0 on both sites). F2: the breakdown census e2e at 1280 (the 5-band stack [56, 1, 64, 64, 45], the single divider, the 364px card) + the hero grid census at 640 (goalCard 316, breakdownCard 324@y=569, hero 664, secondBand y=925, thirdBand y=1635, scrollH 3029); F3: the five-route mid-viewport census e2e (the common rhythm + the route-class branches: the dashboard's 1-col 24px-gap hero grid, the items' block mb-24 filter + 1-col 16px-gap grid). THREE PIN-SANITY MUTATIONS VERIFIED TO FAIL: the reverted divider condition → the band-count pin fails (6 ≠ 5); the items-view mb-8 → mb-6 → the /income rhythm pin fails (24 ≠ 32); the dashboard mb-8 → mb-6 → the / rhythm pin fails. Probe lessons: a height drift attributes FASTER BAND-BY-BAND than card-by-card; a DOM-structure census (child COUNT) catches what the geometry census misses (+13px was visible in the height, but the root cause was a 6-vs-5 child count — census BOTH); the uniform-symmetric-chrome assumption class is exactly where asymmetric reference design hides. Mobile-nav R1–R4 (36th — Tailwind v4 pins hold, the mobile menu works, both sites), data drift (36th — reference read-only, verified before + after), the SEO pair (robots + sitemap live on both), one VLM pair (the desktop dashboard post-fix — all three flags in the known classes: the active-highlight superset #3, the allocation-bar length = demo data, the avatar letter) — 108/209/35 green |
| 2026-10-11 | Session 76 — parity iteration v41 (`docs/remediation-plan-v41.md`) | **The net-worth summary card's viewport census + the vertical-rhythm fix — THE FIRST PRODUCTION-CODE CHANGE SINCE v38** (7 new e2e, TDD with four pin-sanity mutations). The surface (the session-86/87 queue's savings-class viewports item — the unmeasured MID viewport class): the summary card measured live on BOTH sites at 390×844, 640×960 AND 1280×800 (nw-summary-v41.mjs + nw-yoffset-v41.mjs + nw-below-v41.mjs). AT THE MID VIEWPORT (640): FULL geometry parity — the 608×333 card (p-8, radius 16, the forest→lime gradient, the rgba(26,58,46,0.3) 0 20 60 shadow), the 48px/700 figure (sm:text-5xl), the 64×64 white/20% gradient chip at x=528 (9999px, the 32px icon), the 264×2 stats grid (16px gap, 84px cells), the 18px ratio, the 48@x=16 header chip, the 256/0.1 overlay. THE v41 PARITY FIX (F1): the net-worth page's section rhythm ran mb-6 (24px) where the reference runs mb-8 (32px) at BOTH gaps — the header row→card and the card→tablist (8px offsets at every viewport; the y-offset probe isolated the two margins — everything above/below matches byte-for-byte; the items-view control on /income proved the net-worth was the one outlier). THE MOBILE SUPERSET PAIR (390): the reference's card is 432px wide at the 390 viewport (74px page overflow, sw=464, its chip 26px offscreen at x=352, its stats grid a fixed 2-col, its figure a fixed 48px); the clone's fits (358 card, the 24px text-2xl figure — superset fix #6, the 1-col grid, the chip fully inside, sw=390) with byte-identical card chrome. F2/F3: the 640 census e2e (the full band census + the two rhythm pins — card.y − chipRow.bottom === 32, tablist.y − card.bottom === 32) + the 390 superset census e2e (networth.spec.ts). F4: the a11y sheet-open structural pins EXTENDED to the remaining five routes (a11y.spec.ts — /dashboard /income /expenses /savings /networth; the v39 test covered / only; the same dialog-role/labelledby/nav-landmark/five-links/Escape-close contract; the full axe scan stays on / since the sheet's DOM contribution is route-independent). FOUR PIN-SANITY MUTATIONS VERIFIED TO FAIL: the reverted mb-8 → the rhythm pin fails (24 ≠ 32); the stripped sm:text-5xl → the 48px pin fails; the fixed 2-col grid → the 1-col pin fails; the stripped DialogTitle → all five route tests fail. Probe lessons: an unmeasured VIEWPORT CLASS is as dangerous as an unmeasured surface — the rhythm bug survived 40 iterations of desktop/mobile pins because the mid viewport was never census'd; an 8px y-drift is attributable in ONE probe by measuring the full vertical stack; the reference's page-level section rhythm is uniformly mb-8 — audit the CLASS when one page's gap disagrees; this sandbox reaps background processes between tool calls (long jobs run inside ONE invocation via with-server.sh; the agent-browser daemon survives). Mobile-nav R1–R4 (35th — Tailwind v4 pins hold, the mobile menu works, both sites), data drift (35th — reference read-only, verified before + after), the SEO pair (robots + sitemap live on both) — 108/203/35 green |
| 2026-10-11 | Session 75 — parity iteration v40 (`docs/remediation-plan-v40.md`) | **The dashboard's Tab-order focus walk — the session-78 queue's LAST unmeasured surface — ZERO production-code changes** (1 new e2e, TDD with two pin-sanity mutations). The census (tests/e2e/dashboard.spec.ts): the 16 REAL-Tab stops with tag + role + accessible name + tabindex — the five nav links → the Add Item header button → the three NetZero-breakdown stat-row buttons → the three interactive stat cards → the donut's g.recharts-pie (tabindex=0) stop → the three quick-action cards → the body wrap — plus the geometry bands (nav x=20 w=215 pitch 40; the stat-row buttons x=961 w=254; the stat cards [288/616/944, 304×210]) and the interactive stat-card SUPERSET activation (Enter on the focused Total Income card routes to /income; Space on Total Savings routes to /savings). THE MEASUREMENT (tabwalk-v36.sh + focus-census-v40.mjs + stat-card-chain-v40.mjs + donut-focused-dump-v40.mjs, BOTH sites): the reference's 14-stop cycle is the same walk MINUS the three stat-card stops PLUS its Base44 "Close badge" (platform chrome) — **its big 304×210 stat cards are INERT divs** (no role, no tabindex, no handler — dead UI; the text-ancestor chain probe is what separates them from the stat rows, which ARE real buttons on both sites). The donut stop matches structurally on both sites (g.recharts-pie tabindex=0, the sector paths tabindex=-1 roving, the inert svg surface — the v31 replication confirmed at the walk level; the reference's g carries its label texts inside, the clone's render them in a separate recharts-3 layer — library internals, VLM-clean). BOTH PIN-SANITY MUTATIONS VERIFIED TO FAIL: (a) the stripped role+tabIndex drops the stat-card stops out of the walk (the Tab skips straight to the donut g); (b) the removed Enter/Space handler fails the activation pin — the mutation literally reproduces the reference's dead-UI behavior and the test catches it. Probe lessons: the clean focusable census must filter [tabindex]=-1 AND zero-rect elements or recharts' hidden zIndex layers pollute the count; the reference's stat-card inertness is only visible via the TEXT-ANCESTOR CHAIN (the census alone shows both sites' stat ROWS as buttons); document.querySelector('header button') matches the display:none MobileTopbar burger first — query by text when the target has no semantic landmark; the tabwalk's 450ms settles leave the page scrolled — assert only scroll-independent bands (x/w/h); the reference's own stat-row column gaps are inconsistent (25px then 12px) while the clone's are a consistent 25px — a 13px band drift below that point, VLM-clean. Mobile-nav R1–R4 (34th — Tailwind v4 pins hold, the mobile menu works, both sites), data drift (34th — reference read-only, verified before + after), the SEO pair (robots + sitemap live on both), one VLM pair (the desktop dashboard — VERDICT DIFFERENT with ALL THREE flags explained: the clone's Dashboard active highlight = superset fix #3, the allocation-bar length = the different demo data, the avatar letter = the different demo users) — 108/196/35 green |
| 2026-10-11 | Session 74 — parity iteration v39 (`docs/remediation-plan-v39.md`) | **The a11y gate's MOBILE extension — the 390×844 sheet-state scan — ZERO production-code changes** (8 new e2e, TDD with two pin-sanity mutations). The v38 desktop gate extended to the mobile viewport (a new test.describe with test.use({viewport: {width: 390, height: 844}, hasTouch: true, isMobile: true}) — the mobile-navigation.spec.ts emulation): the six authed routes scanned sheet-closed under the SAME two gates (GATE 1 structural + GATE 2 the 7-color palette provenance, the shared assertParityClean helper), the sheet-OPEN state on / (a REAL click on the named burger, then the structural pins: role=dialog, the aria-labelledby resolving to the sr-only "Navigation" DialogTitle, the <nav aria-label="Primary"> with the five links, Escape closing the sheet), and the logged-out mobile login (its own storageState-opt-out describe, ZERO violations). The measurement behind it (a11y-scan-v39.mjs + axe-detail-v39.mjs / axe-detail-ref-v39.mjs, both sites): the reference at mobile fails button-name (critical) on the four item views (its unlabeled Select triggers + kebabs) and svg-img-alt on the two dashboard routes — the same families as desktop — while the clone passes both everywhere; the clone's only mobile failures are color-contrast, every flagged color enumerated in the reference's own 7-color palette (the mobile node counts differ from desktop only by the demo card counts: 2 income cards, 3 expense cards, 3 assets + the inactive tab). THE HEADLINE STRUCTURAL SUPERSET: the reference's mobile sheet is a plain fixed div — NO dialog role, NO aria-labelledby, NO <nav> landmark, NO accessible title — while the clone's is role=dialog + aria-labelledby → the sr-only "Navigation" DialogTitle + nav aria-label="Primary" + the five links + the named burger (sr-only "Toggle Sidebar"). THE STRIPPED-BURGER MUTATION IS THE EXTENSION'S RAISON D'ÊTRE: removing the sr-only span fires button-name on ALL SIX mobile routes while every desktop scan stays green — the burger is md:hidden at desktop, so a desktop-only gate can never catch a nameless burger (mutation verified to FAIL, restored → GREEN); the removed-DialogTitle mutation breaks the aria-labelledby pin exactly as designed. Probe lessons: the agent-browser daemon can WEDGE after a killed parity server (pkill agent-browser restarts it cleanly; sessions are disposable); the clone's burger is named by its sr-only SPAN, not an aria-label; document.querySelector('nav') on mobile finds the display:none desktop rail first — query the sheet element for its own nav (the sheet's portal is at the end of body); the reference's burger is hit-test blocked by its toast viewport (R1) — mobile sheet probes must JS-click it (el.click()); playwright test -g '…' with parens in the title breaks the grep regex. Mobile-nav R1–R4 (33rd — Tailwind v4 pins hold, the mobile menu works, both sites), data drift (33rd — reference read-only, verified before + after), the SEO pair (robots + sitemap live on both), one VLM pair (the mobile sheet-open state — VERDICT DIFFERENT with BOTH flags explained: the clone's Dashboard active highlight = superset fix #3 [the reference marks nothing active on /], the avatar letter = the different demo users) — 108/195/35 green |
| 2026-10-11 | Session 73 — parity iteration v38 (`docs/remediation-plan-v38.md`) | **The a11y tooling pass (open since session 72) shipped as a permanent gate + two first-time surfaces pinned — ZERO production-code changes** (10 new e2e, TDD with pin-sanity mutations). THE A11Y GATE (`tests/e2e/a11y.spec.ts`, @axe-core/playwright 4.13): every app route (6 authed + the 404 + the logged-out login in its own opt-out describe) scanned with the wcag2a/2aa/21a/21aa tags under TWO gates — GATE 1 (structural): no violation id other than color-contrast may fire; GATE 2 (provenance): every contrast-flagged color must be one of the reference's own 7 measured palette colors. The measurement behind it (both sites, axe-core live): the reference FAILS button-name (critical — its unlabeled Select triggers + card kebabs) and svg-img-alt (its recharts donut sectors path[name=…]) while the clone PASSES both (the aria-label superset + the v31 inert donut); the clone's ONLY failures are the reference's own parity-pinned contrast colors — the 1:1 node enumeration matched both sites color-for-color (the 3 breakdown section rows, the hero status label, the 50/30/20 guideline amounts, the stat-card rows, the item-card amounts, the net-worth inactive tab + asset amounts, the 404 h1 — 7 colors: rgb(143,188,63)/rgb(59,126,161)/rgb(224,122,59)/rgb(245,169,98)/rgb(107,114,128)/rgb(203,213,225)/rgb(115,115,115)). The tooling pass's other half: scripts/parity-probes/hasfocus-gate.sh — the v34 document.hasFocus() discipline as a shared fail-loud probe helper (a REAL press Shift re-focuses a page the sandbox unfocused; source it + focus_gate <session> before any :focus-computed read). SURFACE A — the /expenses frequency filter (first-time live): the second Select's option list is the STATIC 7-option list BYTE-IDENTICAL to the reference's (All Frequencies + One-time/Weekly/Bi-weekly/Monthly/Quarterly/Annually — the same static list the v34 pin covered in the sub-dialog instance); the round-trip: the reference 'One-time' → 0 cards + '0 items · $0.00' (its demo expenses are all recurring — data-level), the clone 'Weekly' → Groceries + '1 items · $320.00' + the reset (3 cards, '3 items · $2235.00'); pinned (S1, items.spec) with the mutation sanity (removing the Weekly SelectItem FAILS the census). SURFACE B — the /savings filter-card instance (the third items-view, first-time live): the white rounded-2xl card (bg rgb(255,255,255), radius 16px, border rgb(229,231,227), pad 24px), the 447×36 search ('Search savings items...', the aria-label superset — the reference's input carries NO label), the two 216×36 comboboxes, the 4-column grid — byte-identical to the reference's; the category round-trip (Emergency Fund → 1 card + '1 items · $800.00' → the reset, 2 cards + '2 items · $1250.00'; the reference's own list carries only its All + Emergency Fund — its demo savings has ONE item, data-level); pinned (S2, items.spec) with the mutation sanity (changing the savings searchPlaceholder FAILS the placeholder/aria-label assertions). Probe lessons: getByRole('option', {name:'Weekly'}) collides with 'Bi-weekly' (substring matching — use exact:true in census loops); AxeBuilder.analyze() requires a page from browser.newContext() (a bare browser.newPage() throws); test.use({storageState…}) is HOISTED per describe — logged-out tests need their own describe; the axe node.target selector chains (escaped classes included) resolve cleanly through document.querySelector for the color-provenance reads. Mobile-nav R1–R4 (32nd — Tailwind v4 pins hold, the mobile menu works, both sites), data drift (32nd — reference read-only, verified before + after; the frequency + category probes reset to All), the SEO pair (robots + sitemap live on both; the reference's capitalized app-route URLs still documented), one VLM pair (/savings — all four flags data-explained: the card count, the classification tags, the payment-method footer chips, the avatar letter) — 108/187/35 green |

| Tailwind trap log | `docs/Tailwind-V4-Validation-Report.md` |

**Commands:** `npm run dev` · `npm run build` · `npm start` ·
`npm run typecheck` · `npm run lint` · `npm test` · `npm run test:e2e` ·
`npm run db:push` · `npm run db:seed` · `bash scripts/smoke-test.sh`



