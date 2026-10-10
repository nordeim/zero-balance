---
name: zero-balance
description: >
  ZeroBalance — self-hosted budget planner (Next.js 16 + React 19 + Prisma/SQLite
  + Zustand + Tailwind CSS v4). Superset clone of the ZeroBudget reference app
  with cookie-session auth, integer-cents money math, and a three-tier test
  suite. This skill captures every design decision, anti-pattern, debugging
  procedure, and lesson needed to extend, debug, or replicate the codebase.
version: 1.0.0
last_updated: 2026-10-10

project_state: 108 unit tests / 168 e2e tests / 35 smoke steps — all green
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
| `playwright.config.ts` | desktop + mobile(390×844) projects, authenticated via `storageState`, `db/e2e.db`, webServer = standalone build on :3333 |
| `postcss.config.mjs` | `@tailwindcss/postcss` |
| `prisma/schema.prisma` | 5 models, provider sqlite |

**Verification that bootstrap worked:** `npm run typecheck && npm test` (87
tests), then `npm run build && npm run test:e2e` (34 tests), then
`bash scripts/smoke-test.sh` (30 steps on :3210).

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
npm test                 # 87/87
npm run build            # standalone build must succeed
npm run test:e2e         # 34/34 (build first!)
bash scripts/smoke-test.sh   # 30/30 on :3210
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
| 7 | Three-tier tests: Vitest unit (87) / Playwright e2e (34, desktop+mobile) / bash API smoke (30) | Each tier catches what the previous can't (see §12 L1, L8) |

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
| E2E specs | `tests/e2e/*.spec.ts` (7 files, 34 tests) |
| Smoke script | `scripts/smoke-test.sh` (30 steps, port 3210) |
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
| Tailwind trap log | `docs/Tailwind-V4-Validation-Report.md` |

**Commands:** `npm run dev` · `npm run build` · `npm start` ·
`npm run typecheck` · `npm run lint` · `npm test` · `npm run test:e2e` ·
`npm run db:push` · `npm run db:seed` · `bash scripts/smoke-test.sh`



