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
- **Tailwind v4**: CSS-first config in `src/app/globals.css`; v4-native `w-(--var)` syntax; `h-svh` (not `h-full`) for full-height fixed chrome; colors via inline styles + CSS vars for parity surfaces; `@variant hover (&:hover)` pins v3 hover semantics (v4 media-gates hover utilities behind `@media (hover: hover)` — the reference applies `:hover` on every device) and `@variant group-hover (.group:hover &)` does the same for the GROUP family (the calculator's hover-revealed row actions — v21; without the pin the actions would stay invisible on hover:none devices); the shadow SCALE shifted in v4 (its `shadow-sm` = v3's bare `shadow`) — the `.zb-btn-add` family pins the reference's v3 geometry directly in `globals.css` (v11) while `--shadow-sm` stays pinned for the navbar surface it was measured on; computed `box-shadow` strings are multi-layer and must be compared in FULL (the visible layer may trail transparent lead layers); a color-only `ring-[…]` utility emits NO box-shadow without a width class — pin focus rings as arbitrary shadows (`focus:shadow-[0_0_0_2px_#fff,0_0_0_4px_#94a3b8]`, the v13 login-input pattern); the reference runs DISTINCT ring families per component (login inputs two-layer #94a3b8, auth submits zinc-950 #09090b, dialog buttons 1px #0a0a0a, the 404 button plain-`focus:` slate-500 #64748b — v25) — never copy one family's color onto another; the app's warm #fafaf8 paper lives on the app-shell wrapper (the body renders the browser's white canvas — v25); Per-route tab titles: use route-segment `layout.tsx` metadata + the root template — NEVER a client `document.title` effect (React Float re-emits the static `<title>` from the RSC payload after hydration and silently resets it); recharts 3's default TOOLTIP drifts from the reference's recharts-2 chrome on four axes (value format, `#cccccc` border, no radius/shadow, sector-colored item text) — pin `formatter` + `contentStyle` + `itemStyle` (the v14 donut pattern); a mouse-following tooltip makes Playwright `.hover()` loop forever — dispatch the sector's pointer events synthetically.
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
- **Unit (Vitest, 108)**: money math, dashboard aggregations, zod schemas (incl. the verify-email/resend schemas — v21), rate limiter, serializers, SQLite URL resolution, the email-verification seam (code format, 5-attempt countdown, the reference's exact messages — v21)
- **E2E (Playwright, 187)**: auth (incl. the `?from_url` deep-link redirect — login lands on the param route — v35), dashboard (incl. the donut hover tooltip — value format + full default-tooltip chrome, v14, and the quick-action Add Item's focus-visible four-layer composite — v35), items CRUD (incl. the card delete failure: the inline confirm's caught rejection + toast — v18), net worth (incl. the header gradient chip at both viewports + the tab icons with currentColor — v14, and the asset/liability error tier: save/delete failures under route-aborted APIs — v18), calculator (+ the line-item error tier: load/create/delete under route-aborted APIs — v17, and the sub-dialog's third family: the 85vh panel cap + 20px form gaps — v22, and the line-item row actions' focus-visible ring family: the 1px #0a0a0a ring + v3's transparent outline form, pinned via the globals.css zb-row-action class — v32, and the toast's announcer: Radix's hidden role=status/aria-live=assertive portal read inside its 1-second mount window — v33), mobile navigation + layout geometry (incl. the sheet's active-route highlighting, the items-view Add button's mobile auto-width + the 32px header gap — v20, and the sheet's keyboard semantics: the Tab focus loop through the five links + the blue #3b82f6 sidebar-ring focus layer — v23), nav geometry (+ per-route tab titles), neutral-token + primitive chrome (radio/switch/9999px radii), dialog action buttons + chrome (X-close/header/labels/tiles, the X's focus-visible ring-1 + hover:text-accent-foreground family — v27, the recurring row's switch-left tinted layout — v19, the classification tiles' 16px lucide icons — v20, the line-item sub-dialog's 85vh/space-y-5 family split — v22) + the gradient-button family (ambient shadows, focus ring, 16px Plus icons, no hover fade — v11), badge computed colors, empty states + content column, login-surface computed chrome + per-state geometry + the error banner/confirmation state/landmark (v12), the register-flow error text + sign-up placeholders + input focus ring (v13), the auth forms' MOBILE responsive families — sign-in 44px vs sign-up/forgot 40px controls + the 10px label→input gap, the v4 space-y-1.5 inline-label trap pinned in globals.css (v24), the auth submit's zinc-950 #09090b keyboard ring + the login body's white canvas + its classless `<body>` (v25/v26), the full-page loading state (the DOM-replacing spinner overlay: chrome, data-flight timing, client-nav inverse, mobile overlay — v15), the boot data-failure state (stay-in-app zero-state + the one-shot error toast + the 401-probe redirect pin — v16), custom 404 + head metadata (+ the sitemap/robots MetadataRoute files: allow-all robots, the five-URL/priority sitemap — v21, and the Go Home button's plain-`focus:` slate-500 #64748b ring — v25), the register verify-email gate (the reference's state chrome + 6-input geometry, the wrong-code countdown, the correct-code dashboard landing, the unverified-login banner, resend — v21, and the state's MOBILE chrome: the 56px circle / 28px icon / 20px h2 responsive scale + the 294×44 button — v23, and the code inputs' autocomplete distribution — one-time-code on the first box, off on the rest — v26, and the code inputs' focus family: the reference's 2px zinc-950 ring + untinted border + the first-box auto-focus, pinned via the explicit arbitrary-shadow idiom — v33, and the forgot-state focus-walk contract: the 3-stop census + no-auto-focus + the v13 slate input family + the v25 zinc submit family + the raw back button — v34, and the frequency Select's listbox keyboard contract: the fresh-open selected-option accent highlight (:focus-driven), the arrow roving CLAMPED at both ends, Home/End, Escape closing the popup only (focus → trigger, the dialog stays), and Enter selecting — v34, and the action-menu keyboard contract + the focused Delete family: the click-open container / Enter-open first-item focus landing, the arrow roving with ArrowUp-from-container landing on the LAST item, Home/End, the Tab trap, Escape → trigger, the focused Delete's accent-foreground (not red — the reference's cascade), and the trigger's 1px #0a0a0a focus-visible ring — v35, and the action-menu HOVER-highlight family: the REAL-hover pointer-driven roving (focus moves to the hovered item — the accent tint, the hovered Delete NOT red; the pointer-off reset to the container + rest colors; the menu survives the leave) — v36, and the filter Selects' listbox keyboard contract at the /income instances: the fresh-open selected-option accent highlight via click AND Enter, the clamped arrow roving, Home/End, Escape closing the popup only (focus → trigger, page unaffected), Enter selecting + the trigger text update — v36, and the items-view Tab-order census: the page-level stop sequence (the five nav links → the Add button → the search input → the two filter comboboxes → the card kebabs) + the kebab's focus-visible opacity REVEAL (superset #7 — the reference's trigger stays invisible when keyboard-focused) — v36, and the filter Select TRIGGERS' focus-visible family: the REAL-Tab 1px #0a0a0a ring + ambient over the untinted border (216×36; the v3/v4 lead-layer construct difference documented — invisible by construction) — v37, and the search input's focus + typing contract: the same ring family + the REAL-key match/no-match/empty-state/cleared outcome — v37, and the /expenses payment-method filter's full contract: the dynamically derived options + the Credit Card round-trip + the reset — v37, and the Budget Item Details sheet: the card-body-click surface with the bottom-sheet/centered geometry, the type/classification pill badges, the icon-led fact rows + conditional Notes, and the action-button independence — v28, and the net-worth card type labels' pinned rest colors + hover family — v29, and the details sheet's keyboard semantics (initial focus X + Tab trap + Escape, desktop AND mobile with the bottom-sheet geometry) + the net-worth tablist's roving arrow-key contract — v30, and the donut's keyboard semantics: the INERT surface (no tabindex/role — recharts 3's a11y defaults pinned off via accessibilityLayer={false}), the tooltip's attribute-free default content, and the recharts-2.15 sector roving replicated (ArrowLeft ++wrap / ArrowRight --wrap / Escape blur+reset — v31, and the classification tiles' fresh roving state: the checked radio is a real tab stop (tabIndex={selected ? 0 : -1}) with the REAL Tab landing on it via the container's entry focus — v31, and the breakdown rows' aria-expanded accurate-state superset (section + category levels — v32), and the axe-core A11Y GATE (v38 — `tests/e2e/a11y.spec.ts`, the session-72 tooling pass: @axe-core/playwright scans of the 6 authed routes + the 404 + the login under TWO gates — GATE 1 structural: no axe rule other than color-contrast may fire [the reference fails button-name + svg-img-alt there; the clone passes both — the aria-label superset + the v31 inert donut], GATE 2 provenance: every contrast-flagged color must be one of the reference's own 7 measured palette colors [its lime/blue/orange type accents, its hero status color, its stat-card sublabel gray, its 404 slate, its zinc inactive tab] — a new low-contrast color fails even though the rule id is allow-listed; the login page asserts ZERO violations, in its own storageState-opt-out describe) — against the production standalone build
- **Smoke (bash, 35 steps)**: full API surface including rate limiting, session invalidation, and the register verify-email gate (201+code, 403 unverified login, 400 wrong code, 200 verify + authed session — v21)

### Test Commands

```bash
npm test                                  # all unit
npx vitest run tests/money.test.ts        # one file
npm run build && npm run test:e2e         # e2e (needs the build)
npx playwright test tests/e2e/items.spec.ts -g "round-trip"   # one spec
```

**E2E contract**: `db/e2e.db` is wiped and re-seeded every run; specs assert the seed's exact arithmetic and **must restore their fixtures** — in the ORIGINAL relative order when the fixture's display order depends on `createdAt` (the net-worth tabs order by `createdAt` DESC; the empty-states spec re-creates its deleted liabilities in reverse capture order); one worker, one shared database; a single storageState login (the auth endpoints are rate-limited — never add per-test logins). Since v15 the item-view pages prerender the full-screen loading overlay (the reference's DOM-replacing spinner; `booted` starts false): the old header + empty-state double-match race in static HTML is gone — wait for a seeded card heading before interacting (the settle pattern holds); to test the loading state itself, intercept the API routes with a delay and `unrouteAll({ behavior: "ignoreErrors" })` before the spec ends (the loading-state spec's pattern). Since v16 the boot data-failure specs abort the data routes (`route.abort("failed")` — read-only) with `/api/auth/me` left live, so the session probe succeeds exactly like the measured reference scenario; a toast-text `getByText` needs `{ exact: true }` — Radix mirrors the toast into a `role=status` live region whose concatenated text double-matches the loose locator (the boot-failure spec's strict-mode lesson). Since v17 the calculator-error specs pin the line-item tier (load/create/delete) under aborted `**/api/line-items**` routes; a NESTED Radix dialog aria-hides the parent — calculator-content assertions must wait until the sub-dialog closes (assert the sub-dialog first, then Cancel, then the calculator text). Since v18 the networth-error specs pin the asset/liability tier (save + the caught deletes) under aborted `**/api/assets**`/`**/api/liabilities**` routes and the items spec pins the budget-item CARD delete failure under aborted `**/api/budget-items**` — the delete specs need NO fixture restore (the aborted DELETE never reaches the server; the card survives by construction). Next.js App Router's ROUTE ANNOUNCER also renders `role="alert"` (empty, dynamic mount) — never wait on a bare `[role=alert]` in specs; filter the locator by the expected banner TEXT (the register flake, plan v18 G2). Since v21 the verify-email spec registers throwaway accounts per test (≤5 register-class calls + the login-parity 409 = under the 10/IP/15min register bucket); a throwaway email must be well-formed — native `type=email` validation silently blocks the submit on a malformed value (the live-audit lesson, probe-v21). Since v22 the verify-email spec parks the pointer at (5,5) + settles 350ms after the state swap — a clicked submit leaves the mouse where the swapped-in button lands, and its 200ms hover transition reads mid-flight otherwise (the parked-pointer race, plan v22 G1; the same discipline as the v11/v13 transition settles — and since v23 it applies to LIVE PROBES too: a probe eval without a parked pointer reads the swapped-in button's hover color). Since v23 the verify-email spec holds FIVE register-class calls (4 desktop + 1 mobile) — still under the 10/IP/15min register bucket with login-parity's 409. The sheet-focus ring fades in over ~200ms — a 60ms post-Tab read catches it at ~65% opacity/width (the v23 G1 settle).

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
`/api/auth/{login,logout,register,me,verify-email,resend}`, `/api/budget-items[/id]`, `/api/line-items[/id]`, `/api/assets[/id]`, `/api/liabilities[/id]`, `/api/health`. Envelope `{ ok, data | error }`; all mutations zod-validated; line-item mutations return `{ lineItem, parentAmount }` (the recalculated parent); register does NOT open a session — it returns `{ email, devCode }` (the honest no-mail delivery) and the session opens at `/api/auth/verify-email` (v21); login rejects unverified accounts with 403 + the reference's banner text.

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
