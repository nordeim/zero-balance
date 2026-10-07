---
name: zero-balance
description: >
  ZeroBalance — self-hosted budget planner (Next.js 16 + React 19 + Prisma/SQLite
  + Zustand + Tailwind CSS v4). Superset clone of the ZeroBudget reference app
  with cookie-session auth, integer-cents money math, and a three-tier test
  suite. This skill captures every design decision, anti-pattern, debugging
  procedure, and lesson needed to extend, debug, or replicate the codebase.
version: 1.0.0
last_updated: 2026-10-07
project_state: 96 unit tests / 46 e2e tests / 30 smoke steps — all green
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
   plus two reference mobile-navigation bugs deliberately fixed (§9 D-1/D-2,
   `docs/remediation-plan.md`).

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
| Tailwind trap log | `docs/Tailwind-V4-Validation-Report.md` |

**Commands:** `npm run dev` · `npm run build` · `npm start` ·
`npm run typecheck` · `npm run lint` · `npm test` · `npm run test:e2e` ·
`npm run db:push` · `npm run db:seed` · `bash scripts/smoke-test.sh`



