---
IMPORTANT: File is read fresh for every conversation. Be brief and practical.
---

# ZeroBalance

## Core Identity & Purpose

ZeroBalance is a self-hosted budget-planner web app built around the net-zero rule (Income = Savings + Expenses). It is a production-grade, **superset** clone of the ZeroBudget reference app (`zero-balance-4885a8f3.base44.app`): visual parity with the reference, plus its two mobile-navigation bugs, its mobile horizontal overflow, its dialogs that ignore Escape/outside-click and its unconfirmed deletes fixed. Maintained as a single Next.js application (no monorepo) with cookie-session auth, a Prisma/SQLite store, and a three-tier test suite (Vitest unit, Playwright e2e, bash API smoke).

## Foundational Principles

### Meticulous Approach (Six-Phase Workflow)

Follow this six-phase workflow for all implementation tasks:

1. **ANALYZE** — Mine the requirement: explicit asks, implicit needs, ambiguities. For parity work, check the measured design tokens (`src/lib/constants.ts`) before guessing colors/sizes.
2. **PLAN** — A short ordered plan; for UI work include which view/dialog and which tests pin it.
3. **VALIDATE** — Confirm the approach against the codebase contracts below before writing code.
4. **IMPLEMENT** — Modular, typed, tested changes. Persist scripts; never long inline commands.
5. **VERIFY** — Run the clean-check gate: `npm run lint && npm run typecheck && npm test && npm run build && npm run test:e2e`. New behavior needs a new test.
6. **DELIVER** — Conventional Commit; push via the SSH wrapper runbook.

### Project-Specific Principles

- **Parity first, superset always**: match the reference's computed styles; fix its bugs and pin the fix with a test.
- **Integer-cent arithmetic**: every money aggregation goes through `src/lib/money.ts` — no float sums.
- **Validate at the boundary**: every API input is zod-parsed (`src/lib/validation.ts`); unknown input never reaches Prisma.
- **One client store**: Zustand (`src/components/budget/store.ts`) — no React Context, no prop drilling for server data.

## Implementation Standards

### General Coding Practices
- Early returns over nested conditionals
- Composition over inheritance
- Self-documenting names; comments explain *why*
- Strict TypeScript; `any` only at genuine boundaries with a justification comment

### Language & Framework Guidelines
- **Next.js 16 App Router**: pages are thin `"use client"` compositions; API handlers under `src/app/api/**/route.ts` return the typed envelope from `src/lib/api-helpers.ts`.
- **React 19 / eslint react-hooks v6**: no `setState` in effects — use the adjust-state-during-render pattern for derived resets (see the dialogs' lazy form initializers). Components defined at module scope, never inside render.
- **Zustand v5**: selectors returning derived arrays/objects MUST use `useShallow` (a bare derived selector loops to React error #185 on hydrated static pages).
- **Tailwind v4**: CSS-first config in `src/app/globals.css`; v4-native `w-(--var)` syntax; `h-svh` (not `h-full`) for full-height fixed chrome; colors via inline styles + CSS vars for parity surfaces; `@variant hover (&:hover)` pins v3 hover semantics (v4 media-gates hover utilities behind `@media (hover: hover)` — the reference applies `:hover` on every device).
- **Prisma 6**: schema at `prisma/schema.prisma`; relative `file:` URLs anchor to the schema dir (both CLI — via the npm script wrappers — and runtime, via `src/lib/db-path.ts`).

## Development Workflow

### Environment Setup

```bash
npm install
npm run db:push     # create db/custom.db
npm run db:seed     # demo workspace (demo@zerobalance.app / Demo1234!)
npm run dev         # http://localhost:3000
```

### Build Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | Development server (tee'd to `dev.log`) |
| `npm run build` | Production standalone build |
| `npm start` | Boot the standalone server |
| `npm test` | Vitest unit suite |
| `npm run test:e2e` | Playwright e2e (build first) |
| `bash scripts/smoke-test.sh` | 30-step API smoke (own server, :3210) |
| `npm run typecheck` | `tsc --noEmit` |
| `npm run lint` | ESLint |
| `npm run db:push` / `db:seed` / `db:migrate` | Prisma CLI via wrapper scripts |

## Testing Strategy

### Test Pyramid
- **Unit (Vitest, 96)**: money math, dashboard aggregations, zod schemas, rate limiter, serializers, SQLite URL resolution
- **E2E (Playwright, 104)**: auth, dashboard, items CRUD, net worth, calculator, mobile navigation + layout geometry (incl. the sheet's active-route highlighting), nav geometry, neutral-token + primitive chrome (radio/switch/9999px radii), dialog action buttons + chrome (X-close/header/labels/tiles), badge computed colors, empty states + content column, login-surface computed chrome + per-state geometry, custom 404 + head metadata — against the production standalone build
- **Smoke (bash, 30 steps)**: full API surface including rate limiting and session invalidation

### Test Commands

```bash
npm test                                  # all unit
npx vitest run tests/money.test.ts        # one file
npm run build && npm run test:e2e         # e2e (needs the build)
npx playwright test tests/e2e/items.spec.ts -g "round-trip"   # one spec
```

**E2E contract**: `db/e2e.db` is wiped and re-seeded every run; specs assert the seed's exact arithmetic and **must restore their fixtures** — in the ORIGINAL relative order when the fixture's display order depends on `createdAt` (the net-worth tabs order by `createdAt` DESC; the empty-states spec re-creates its deleted liabilities in reverse capture order); one worker, one shared database; a single storageState login (the auth endpoints are rate-limited — never add per-test logins). The item-view pages are prerendered with an EMPTY store — until hydration + the boot fetch land, the header AND empty-state "Add …" buttons coexist in the DOM. Wait for a seeded card heading before clicking an "Add …" button by role, or the strict-mode locator resolves to two elements (the dialog-buttons spec shows the settle pattern).

## Code Quality Standards

```bash
npm run lint && npm run typecheck
```

- ESLint 9 + eslint-config-next with react-hooks v6 rules (`set-state-in-effect`, `static-components` are errors, not warnings).
- No `ignoreBuildErrors`/`ignoreDuringBuilds` escape hatches in `next.config.ts` — keep it that way.

## Git & Version Control

- `main` only; short-lived branches merged fast
- Conventional Commits; atomic commits (one logical change)
- Push through `docs/ssh_git_wrapper_v3.py` (see `docs/how-to-git-push-using-ssh-wrapper_SKILL.md`) — run the clean-check gate first; never commit secrets, `db/*.db`, `.env`, or the ssh shim

## Error Handling & Debugging

- API failures return `{ ok: false, error }` with a field-level zod message and a precise status (400/401/404/429/500) — never leak stack traces
- Client surfaces errors via toasts (`useToast`); the toast viewport is `pointer-events: none` (the reference's hamburger-blocker bug — do not regress; a Playwright test pins it)
- Auth rejects unknown-email and wrong-password identically (no account enumeration); the limiter answers 429 with `Retry-After`
- Debug a stuck e2e with the saved trace: `npx playwright show-trace test-results/<dir>/trace.zip`

## Communication & Documentation

- Comments and docs explain *why*, with the measured evidence (e.g. "reference exposes plain `Edit`/`Calculate` accessible names")
- Architecture decisions belong in `Project_Architecture_Document.md`; agent operating rules in `AGENTS.md`; keep README user-facing

## Project-Specific Standards

### Architecture
Client-heavy single app: App Router pages compose views; all server data flows through the Zustand store; store-driven modals mount in `ModalHost` (a dialog exists only while its modal is open — forms initialize via lazy `useState`, not effects).

### API Design
`/api/auth/{login,logout,register,me}`, `/api/budget-items[/id]`, `/api/line-items[/id]`, `/api/assets[/id]`, `/api/liabilities[/id]`, `/api/health`. Envelope `{ ok, data | error }`; all mutations zod-validated; line-item mutations return `{ lineItem, parentAmount }` (the recalculated parent).

### Database / Data Layer
SQLite at `db/custom.db`; Prisma models User, BudgetItem, ExpenseLineItem, Asset, Liability (all scoped by `userId`). Serializers (`src/lib/serializers.ts`) translate rows to API payloads (ISO dates, null → undefined elision, no `userId` leaks).

### Environment Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `DATABASE_URL` | SQLite location, relative to `prisma/schema.prisma` | `file:../db/custom.db` |
| `AUTH_SECRET` | Session HMAC key (required in prod) | `openssl rand -hex 32` |
| `NEXT_PUBLIC_SITE_URL` | Canonical origin for metadata (OG/Twitter/canonical/manifest) | `http://localhost:3000` |

## Anti-Patterns to Avoid

- **Bare derived Zustand selectors** — always `useShallow` (React #185 loop)
- **`h-full` on fixed full-height chrome** — use `h-svh` (mobile emulation measures 1044 against 844)
- **`setState` inside `useEffect`** — adjust during render or restructure
- **Float money arithmetic** — integer cents via `src/lib/money.ts`
- **Skipping fixture cleanup in e2e** — the next spec depends on the seed's exact numbers
- **Running bare `prisma` CLI commands** — a shell-exported absolute `DATABASE_URL` will write to the wrong file; use the npm wrapper scripts
