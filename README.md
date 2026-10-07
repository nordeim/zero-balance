# ZeroBalance — Budget Planner

![Next.js](https://img.shields.io/badge/Next.js-16-black?logo=next.js)
![React](https://img.shields.io/badge/React-19-61dafb?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5-3178c6?logo=typescript)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4-38bdf8?logo=tailwindcss)
![Prisma](https://img.shields.io/badge/Prisma-6-2d3748?logo=prisma)
![SQLite](https://img.shields.io/badge/DB-SQLite-003b57?logo=sqlite)

A production-grade budget planner built around one rule — **Income = Savings + Expenses** — and a self-hosted, superset clone of the reference ZeroBudget app (`zero-balance-4885a8f3.base44.app`), rebuilt as a single Next.js application with cookie-session auth, a Prisma/SQLite store, and a full three-tier test suite.

## Overview

ZeroBalance tracks income, savings, and expenses as budget items, computes your net position against the net-zero goal in real time, and breaks your balance sheet into assets and liabilities for net-worth tracking. The dashboard aggregates everything into allocation percentages, a needs/wants/savings donut, and 50/30/20 guideline rows; every expense category can be decomposed into line items through a built-in calculator that recalculates the category total server-side on every change. The clone keeps pixel-level visual parity with the reference while fixing its two mobile navigation bugs (see [Superset fixes](#superset-fixes-over-the-reference)).

## Key Features

| Feature | Description |
|---------|-------------|
| 🎯 **Net Zero Goal hero** | Forest-gradient dashboard card computing `Income − Savings − Expenses`, allocation %, and Under Budget / NET ZERO / Over Budget status |
| 📊 **Net Zero Breakdown** | A 3-level expandable drill-down (section → category → subcategory → item, accordion-style) with sign-prefixed rows (`$5,550.00` → plain format `- $1250.00`) and a sign-conditional Net Balance (lime/orange/blue) |
| 📈 **Spending Breakdown donut** | recharts pie in the reference's sector order [Savings, Want, Need] (`#8fbc3f` / `#3b7ea1` / `#e07a3b`) with piggy-bank / heart / circle-alert legend icons |
| 🧮 **Category Calculator** | Break any expense category into line items (name, amount, frequency, provider, policy #); each mutation recalculates and persists the parent item's amount server-side, with category-adaptive chrome ("Rent Calculator / Break down your rent…") |
| 💰 **Net Worth tracker** | Assets vs liabilities tabs grouped **by type** under capitalize headers, gradient summary card with the `0.21:1` / `∞:1` asset-to-liability ratio |
| 🔍 **Filterable item views** | Search + category + frequency (+ payment method on expenses) filters; per-classification/per-frequency badge maps, capitalized green Recurring badge; hover-revealed Edit/Calculate buttons on expense cards (plus a superset delete in the edit dialog) |
| 📱 **Working mobile navigation** | Hamburger + slide-in sheet at 288px — with both reference bugs fixed (below) |
| 🔐 **Cookie-session auth** | scrypt password hashing + HMAC-signed sessions, per-IP rate limiting (10 attempts / 15 min), zod-validated API, three-state login card (sign-in / sign-up / forgot) |

### Superset fixes over the reference

The live reference app has quirks and bugs, measured against the clone:

1. **Hamburger click-block** — the reference's empty toast container (`pointer-events: auto`, full-width, top 32px, z-100) covers the top half of the mobile hamburger button. The clone's toast viewport is `pointer-events: none` (the sonner pattern); toasts re-enable pointer events individually. Pinned by `tests/e2e/mobile-navigation.spec.ts`.
2. **Menu stays open after nav** — tapping a nav link in the reference's sheet changes the route but leaves the sheet + overlay trapping the user. The clone closes the sheet on every navigation. Pinned by the same spec.
3. **Root URL nav highlight** — the reference marks NO nav item active when you sit on `/` after login (its active check compares the pathname to `/dashboard`). The clone highlights Dashboard on the root route — the page you are actually viewing.
4. **Mobile horizontal overflow** — the reference's own pages scroll sideways on a 390px phone: the dashboard measures 395px and the net-worth page 464px (its fixed `text-5xl` net figure + fixed 2-col summary grid stretch `main` past the viewport). The clone fits exactly (390px) via `min-w-0` on `main` plus a responsive summary card (`text-2xl` on phones, `sm:grid-cols-2`). Pinned by `tests/e2e/mobile-layout.spec.ts` + the net-worth mobile spec.
5. **Dialogs ignore Escape AND outside-click** — the reference's modal overlays are plain `fixed` divs with no keyboard dismissal and no overlay-click dismissal (verified on its budget-item and line-item dialogs: Escape with focus inside and real clicks on the overlay corner both leave it up; only X/Cancel close it). The clone's Radix dialogs close on Escape and overlay click. Pinned by `tests/e2e/dialog-buttons.spec.ts`.
6. **Delete without confirmation** — the reference's card menu Delete destroys the item immediately (verified live — the same for its calculator line-item rows). The clone's delete paths confirm first (the edit dialog's inline confirm / the alert dialog).

The mobile layout itself (top bar stacked inside `main` at the reference's 61px geometry, no horizontal overflow) is pinned by `tests/e2e/mobile-layout.spec.ts`.

## Architecture

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| Web framework | Next.js (App Router) | ^16.1.1 | Routes, static prerender + standalone build |
| UI runtime | React | ^19.0.0 | Client components, hydrated static pages |
| Language | TypeScript (strict) | ^5 | End-to-end typing, `noEmit` typecheck gate |
| Styling | Tailwind CSS | 4 | CSS-first `@theme`, utility classes + inline CSS-var colors |
| Charts | recharts | ^3.10.1 | Spending Breakdown donut |
| State | Zustand | ^5.0.6 | Single client store (server data + modals), `useShallow` selectors |
| ORM | Prisma | 6.11.1 | Schema, migrations, typed client |
| Database | SQLite | — | `db/custom.db` at the repo root (zero-config) |
| Validation | zod | ^4.6.5 | Every API input, field-level 400s |
| Unit tests | Vitest | ^5.0.1 | Pure domain seams (money, dashboard math, validators) |
| E2E tests | Playwright | ^1.63.0 | Production standalone server, real Chromium |

```mermaid
flowchart TB
    subgraph Client["Browser"]
        UI["App Router pages<br/>(login · dashboard · income ·<br/>expenses · savings · networth)"]
        Store["Zustand store<br/>items · assets · liabilities ·<br/>lineItems · modals"]
    end
    subgraph Server["Next.js (standalone)"]
        API["JSON API routes<br/>/api/auth/* · /api/budget-items<br/>/api/line-items · /api/assets<br/>/api/liabilities"]
        Val["zod validation"]
        Auth["scrypt + HMAC<br/>cookie sessions"]
    end
    DB[("SQLite<br/>db/custom.db")]
    UI --> Store --> API --> Val --> Auth --> DB
```

## File Hierarchy

```
📂 zero-balance/
├── 📂 prisma/
│   └── 📄 schema.prisma           # User, BudgetItem, ExpenseLineItem, Asset, Liability
│   └── 📄 seed.ts                 # Idempotent demo seed (demo@zerobalance.app / Demo1234!)
├── 📂 src/
│   ├── 📂 app/                    # App Router: 7 routes + 21 API handlers (13 files)
│   │   ├── 📄 login/page.tsx      # Three-state auth card
│   │   └── 📄 [dashboard·income·expenses·savings·networth]/page.tsx
│   ├── 📂 components/
│   │   ├── 📂 budget/             # Views, dialogs, sidebar, store (the app)
│   │   └── 📂 ui/                 # shadcn-style primitives (dialog, select, toast…)
│   └── 📂 lib/                    # Domain seams: money, dashboard, validation,
│                                  #   auth, rate-limit, serializers, db-path
├── 📂 tests/
│   ├── 📄 *.test.ts               # Vitest unit suites (96 tests)
│   └── 📂 e2e/                    # Playwright specs (92 tests) + global setup
├── 📂 scripts/
│   ├── 📄 smoke-test.sh           # 30-step production API smoke test
│   └── 📄 capture-screenshots.mjs # docs/screenshots generator
├── 📄 docs/                       # Tailwind v4 report, SSH push runbook, DEPLOYMENT.md, remediation plan, session log
└── 📄 db/custom.db                # SQLite database (gitignored)
```

## Quick Start

Requires **Node.js ≥ 20** (or bun ≥ 1.2) and npm.

```bash
# 1. install
npm install

# 2. database (SQLite file at db/custom.db — created by the push)
npm run db:push

# 3. seed the demo workspace
npm run db:seed

# 4. dev server → http://localhost:3000
npm run dev
```

**Verify setup**

```bash
curl -s http://localhost:3000/api/health          # {"ok":true,...}
# then log in with the seeded demo account:
#   email: demo@zerobalance.app    password: Demo1234!
```

**Production build**

```bash
npm run build        # standalone output (pins DATABASE_URL for the build)
npm start            # boots .next/standalone/server.js
```

## Environment Variables

`.env` (see `.env.example`; `.env` is gitignored):

| Variable | Required | Description |
|----------|----------|-------------|
| `DATABASE_URL` | yes | `file:../db/custom.db` — **relative to `prisma/schema.prisma`**, not the CWD. `src/lib/db-path.ts` anchors the same rule at runtime so CLI and server agree. |
| `NEXT_PUBLIC_SITE_URL` | no | Canonical public origin for metadata (default `http://localhost:3000`). |
| `AUTH_SECRET` | prod | HMAC key for session cookies. Generate with `openssl rand -hex 32`. Falls back to an insecure dev constant when unset. |

> **Database-location gotcha:** Prisma resolves a relative `file:` URL from a shell-inherited `DATABASE_URL` against the **CWD**, but from a `.env`-loaded value against the **schema dir**. The npm scripts pin `DATABASE_URL` (runtime) and use `env -u` (Prisma CLI) so both always land at `<repo>/db/custom.db`. Don't run bare `prisma db push` from an arbitrary directory.

## Testing

```bash
npm test            # Vitest unit suite (96 tests) — pure domain seams
npm run test:e2e    # Playwright e2e (92 tests) — needs `npm run build` first
bash scripts/smoke-test.sh   # 30-step production API smoke (own server, port 3210)
npm run typecheck   # tsc --noEmit
npm run lint        # eslint (react-hooks v6 rules enforced)
```

- The e2e suite boots the **production standalone server** on `:3100` with its own `db/e2e.db`, deleted and re-seeded **every run** — specs assert the seed's exact arithmetic (e.g. `+$2065.00` net balance) and restore their fixtures after themselves.
- One worker: the specs share a single seeded SQLite file (`playwright.config.ts`).
- Auth is signed in once by the `setup` project and replayed via storageState — the auth endpoints are rate-limited (10/IP/15 min), so per-test logins would trip the limiter.
- Unit tests cover the money arithmetic (integer-cent sums — no IEEE-754 drift), dashboard aggregations, every zod schema (including empty-string optional dates and impossible calendar dates), the rate limiter, and the SQLite URL resolution contract.

## Design System

Measured from the reference's `:root` (computed styles as ground truth):

| Token | Hex | Usage |
|-------|-----|-------|
| `--forest-dark` | `#1a3a2e` | Headings, active nav text, hero gradient start |
| `--forest-medium` | `#2d5a4a` | Secondary green, active nav gradient start |
| `--lime-green` | `#8fbc3f` | Income accent, primary buttons, avatar |
| `--orange-dark` | `#e07a3b` | Expense accent, "Need" donut slice |
| `--blue-medium` | `#3b7ea1` | Savings accent, "Want" donut slice |
| `--neutral-warm` | `#fafaf8` | Page background |

- **Typography**: the system font stack (`ui-sans-serif, system-ui, …`) — no webfonts.
- **Money — two formatters (measured in the reference bundle)**: plain `"$" + toFixed(2)` without thousands separators on the dashboard / items views / calculator (`$5550.00`); `toLocaleString` grouping on net worth only (`$25,000.00`). Savings/expenses breakdown rows carry `- ` prefixes, Net Balance `+`. Add buttons carry per-surface 135deg gradients (forest→lime, lime→limeLight, blue→blue, orange→orangeLight).
- **Motion**: sheet slide-in 500ms / slide-out 300ms; `data-[state]`-driven; no reduced-motion needs beyond Radix defaults.
- Tailwind v4 specifics (bare-HSL theme, oklch drift, shadow scale) are pinned in `src/app/globals.css` — the full trap report is [`docs/Tailwind-V4-Validation-Report.md`](docs/Tailwind-V4-Validation-Report.md).

## Engineering References

| Document | Purpose |
|----------|---------|
| [`zero-balance_SKILL.md`](zero-balance_SKILL.md) | Distilled engineering skill — design system, architecture, anti-patterns, debugging guide, pre-ship checklist |
| [`docs/remediation-plan.md`](docs/remediation-plan.md) | Session-1/2 findings ledger (reference bugs, Tailwind v4 traps, app bugs) with fixes and regression pins |
| [`docs/remediation-plan-v2.md`](docs/remediation-plan-v2.md) | Session-3 deep parity audit — money format split, drill-down, badge maps, gradients, networth grouping (14 finding groups) |
| [`docs/remediation-plan-v3.md`](docs/remediation-plan-v3.md) | Session-5 parity iteration — mobile top-bar layout bug, filter card, classification tiles, line-item status enum, login states (6 finding groups) |
| [`docs/remediation-plan-v4.md`](docs/remediation-plan-v4.md) | Session-7 parity iteration — nav-link geometry, net-worth summary card + mobile overflow, filter-aware header counts (6 finding groups, 2 new reference bugs) |
| [`docs/remediation-plan-v5.md`](docs/remediation-plan-v5.md) | Session-9 parity iteration — reference-token alignment (neutrals, accent, input, rings), net-worth tab grid + green active state, dialog action buttons (outline Cancel + per-dialog gradient Saves), hover-variant v3 semantics (10 finding groups, 2 new reference bugs R5/R6) |
| [`docs/remediation-plan-v6.md`](docs/remediation-plan-v6.md) | Session-11 parity iteration — plain-text action menus, Save-button icons, asset/liability dialog grid spans + edit-disabled type, reference empty-state pattern (bare icons, no circles), always-visible calculator row actions, padding-outside-max-w content column (14 finding groups + reference bug R7) |
| [`docs/remediation-plan-v7.md`](docs/remediation-plan-v7.md) | Session-13 parity iteration — post-login root redirect, login-surface slate hex pins (lab/oklab drift) + text-sm footer links, logo-ring halo layer, 24px lucide-target + text-lg sidebar brand, 16px near-black mobile toggle icon with shrink-0, sheet border/overlay pins, the custom 404 page, and full head metadata (description/OG/Twitter/canonical/manifest/apple) (8 finding groups) |
| [`docs/remediation-plan-v8.md`](docs/remediation-plan-v8.md) | Session-15 parity iteration — dialog footers rebuilt as the reference's `flex gap-3 pt-4` full-row split (Cancel/Save at flex-1 ≈ 306px each), every remaining badge/nav/Calculate named-palette class hex-pinned (frequency purple/gray/blue/indigo/pink, classification red/blue/green, Recurring green, status slate, zinc-700 nav, orange Calculate) so computed styles render plain rgb instead of v4 lab(), and the stray session-1 `prisma/db/custom.db` binary untracked (2 finding groups + hygiene; Recurring-badge conditional verified live both sides) |
| [`docs/session_1.md`](docs/session_1.md) · [`docs/session_2.md`](docs/session_2.md) · [`docs/session_3.md`](docs/session_3.md) | Narrative logs of the build + re-verification sessions |
| [`worklog.md`](worklog.md) | Rolling project worklog (all sessions, latest first) |
| [`Project_Architecture_Document.md`](Project_Architecture_Document.md) | 7 ADRs, topology, ER diagram, security model |

## Deployment

`next build` emits a **standalone** server (`docs/DEPLOYMENT.md` has the full runbook):

```bash
npm run build
DATABASE_URL="file:/absolute/path/to/custom.db" AUTH_SECRET="$(openssl rand -hex 32)" \
  node .next/standalone/server.js
```

Use an **absolute** `file:` URL in production — a relative URL resolves against the standalone build's own location.

## Screenshots

| | |
|---|---|
| ![Dashboard](docs/screenshots/02-dashboard.png) | ![Mobile menu](docs/screenshots/10-mobile-menu.png) |
| *Dashboard — NET ZERO GOAL, breakdown, donut* | *Mobile nav sheet (288px, closes on nav)* |
| ![Net Worth](docs/screenshots/06-networth.png) | ![Mobile net worth](docs/screenshots/12-mobile-networth.png) |
| *Net Worth — gradient summary, type-grouped tabs* | *Mobile net worth (fits 390px — superset fix #4)* |

Full 13-shot set in [`docs/screenshots/`](docs/screenshots/) — regenerate with `node scripts/capture-screenshots.mjs`.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `P2003` / `Error code 14` opening the database | A shell-exported absolute `DATABASE_URL` overrides `.env`. Run `npm run db:push` (which strips it) or export `DATABASE_URL="file:../db/custom.db"`. |
| e2e fails with wrong dashboard totals | A previous failed run left fixtures in `db/e2e.db`? The global setup resets it — but specs also restore their own fixtures; if one crashed mid-flow, just re-run. |
| Playwright `--dry-run`/push: `no ssh binary on PATH` | That's the SSH wrapper, not Playwright — see [`docs/how-to-git-push-using-ssh-wrapper_SKILL.md`](docs/how-to-git-push-using-ssh-wrapper_SKILL.md). |
| Login returns 429 in dev | The per-IP rate limiter (10/15 min) persists in the server process. Restart the dev server or wait out the window. |

## License

Private project — all rights reserved.
