# AGENTS.md

ZeroBalance — a Next.js 16 + React 19 budget planner (self-hosted superset clone of the ZeroBudget reference app). Single app, no monorepo.

## Commands

| Task | Command |
|------|---------|
| Dev server | `npm run dev` → http://localhost:3000 (logs tee'd to `dev.log`) |
| Production build | `npm run build` (standalone output) |
| Prod server | `npm start` |
| Typecheck | `npm run typecheck` |
| Lint | `npm run lint` |
| Unit tests | `npm test` (Vitest, one file: `npx vitest run tests/money.test.ts`) |
| E2E tests | `npm run test:e2e` (Playwright — **requires `npm run build` first**) |
| API smoke test | `bash scripts/smoke-test.sh` (boots its own server on :3210) |
| Schema push | `npm run db:push` (never bare `prisma db push` — see gotchas) |
| Seed | `npm run db:seed` (idempotent; demo@zerobalance.app / Demo1234!) |
| Screenshots | `node scripts/capture-screenshots.mjs` (after `npm run build`) |

**Clean-check order:** `npm run lint && npm run typecheck && npm test && npm run build && npm run test:e2e`. There is no hosted CI — the local gate is the only gate.

## Database location — read this before touching DATABASE_URL

`DATABASE_URL="file:../db/custom.db"` resolves **relative to `prisma/schema.prisma`**, NOT the CWD (implemented by `src/lib/db-path.ts`, pinned by `tests/db-path.test.ts`).

- Prisma CLI resolves a **shell-inherited** relative URL against the CWD, but a **`.env`-loaded** value against the schema dir. The npm scripts pin `DATABASE_URL` for the runtime and use `env -u DATABASE_URL` for CLI commands so both agree — don't bypass them.
- This sandbox (and some CI shells) export an absolute `DATABASE_URL` from a parent workspace; it pollutes child processes. The `env -u` discipline in the scripts is load-bearing.
- Production: use an absolute `file:` URL (see `docs/DEPLOYMENT.md`).

## Architecture in one minute

- **All state client-side**: one Zustand store (`src/components/budget/store.ts`) holds session user, items/assets/liabilities/lineItems, and the modal stack. Pages are thin; views read the store.
- **Modals are store-driven** and mounted by `ModalHost` in `src/components/budget/app-shell.tsx` — a dialog only mounts while its modal is open, so form state initializes from the modal via lazy `useState` initializers. Don't add effects to reset forms.
- **Zustand v5 footgun**: any selector that derives a new array/object (`s.items.filter(...)`) must be wrapped in `useShallow` — a bare derived selector re-renders forever (React error #185) on hydrated static pages. Precedent: `items-view.tsx`.
- **Money**: amounts are plain JSON numbers at the API boundary, but **every aggregation converts to integer cents first** (`src/lib/money.ts`). Never sum floats directly.
- **Calculator rule**: creating/editing/deleting a line item recalculates and persists the parent BudgetItem's amount **server-side immediately** (`src/lib/line-item-service.ts`) — there is no client-side recalc step.
- **API envelope**: `{ ok: true, data } | { ok: false, error }` (`src/lib/api-helpers.ts`). All input validated by zod (`src/lib/validation.ts`) — nothing reaches Prisma unvalidated.
- **Auth**: scrypt + HMAC cookie sessions (`src/lib/auth.ts`), per-IP rate limiting (10/15 min) on login/register. Login API returns 401 with the same message for unknown email and wrong password (no enumeration).

## Testing conventions

- Vitest matches `*.test.ts` only; Playwright specs are `*.spec.ts` — never picked up twice.
- E2E runs against the **production standalone build** on :3100 with `db/e2e.db`, **deleted and re-seeded every run** by `tests/e2e/global-setup.ts`. Specs assert the seed's exact numbers (income 5550 / savings 1250 / expenses 2235 → net `+$2,065.00`) and **must restore their fixtures** (delete created items, restore edited amounts) — the suite runs in one worker sharing one database.
- The auth setup project signs in once; storageState replays the session. Total real login attempts per run must stay well under the rate-limit budget (10/IP/15 min) — don't add per-test logins.
- Known interaction race: after a state-changing click inside a dialog (e.g. a radio check), wait one beat before clicking a Radix Select trigger — clicking mid-re-render can land on a stale node and the dropdown never opens (see `tests/e2e/items.spec.ts` for the settle-wait precedent).
- The item-view pages are **prerendered with an empty store**: until hydration + the boot fetch land, the header AND empty-state "Add …" buttons coexist in the static HTML. Wait for a seeded card heading before clicking an "Add …" button by role — otherwise the strict-mode locator resolves two elements (see the dialog-buttons spec's settle pattern). Transitions (`transition-all 200ms` on nav links, ring fade-ins) also need a ~300ms settle before reading computed styles.

## Tailwind CSS v4 — known traps

`docs/Tailwind-V4-Validation-Report.md` documents five measured v4 traps; mitigations live in `src/app/globals.css`. The ones that bite most often:

- **Hover variants are media-gated in v4** — every `hover:` utility compiles inside `@media (hover: hover)`, so the tints vanish on `hover: none` devices. `globals.css` pins the reference's v3 semantics with `@variant hover (&:hover)` — never remove it (pinned by the mobile-navigation spec under `hover: none` emulation).
- **Named palette colors emit `lab()`/`oklab()`** — v4 computes `text-red-600`, `text-orange-600`, `bg-green-50`, `text-white/70` etc. in Lab color space while the reference emits plain rgb/rgba. For computed-style parity use arbitrary hex (`text-[#dc2626]`, `hover:bg-[#f0fdf4]`) or inline rgba — never the named classes on parity surfaces.
- CSS variable arbitrary values use the **v4-native** `w-(--var)` syntax, not the v3 `[--var]` bracket form.
- `h-full` on a fixed element resolves against the **large** layout viewport under mobile emulation (844 visual → 1044 measured) — use `h-svh` for full-height fixed chrome (the sheet does; the reference's rail does too).
- Colors: the app mixes Tailwind utilities for layout with **inline styles + CSS vars for colors** — engine-independent parity with the reference. Keep that pattern for new surfaces.
- The toast viewport is `pointer-events: none` with toasts opting back in (`src/components/ui/toast.tsx`) — never set `pointer-events: auto` on the container; that is the reference's hamburger-blocking bug, and there is a Playwright test pinning the fix.

## Reference-parity rules

The target is a **superset**: visual parity with the reference site plus fixed bugs. When in doubt about a visual detail, the extracted design tokens are in `src/lib/constants.ts` (measured `:root` vars + per-type accents) and the recon notes live in the repo history. Six superset fixes are pinned by tests and must not regress:

1. Mobile hamburger always clickable (toast viewport `pointer-events: none`).
2. Mobile nav sheet closes after tapping a nav link.
3. Dashboard highlighted on the root `/` route (the reference marks nothing active there).
4. No mobile horizontal overflow — `min-w-0` on `main` + the responsive net-worth summary card (the reference scrolls to 395px on `/dashboard` and 464px on `/networth` at 390px).
5. Dialogs close on Escape (the reference's modal overlays have no keyboard dismissal at all — only X/Cancel close them).
6. Deletes confirm first (the reference's card menu deletes immediately, no confirmation).

The neutral tokens are the reference's shadcn NEUTRAL scale, measured live on its `:root` (see the token comment in `globals.css`): foreground `#0a0a0a`, accent/muted `#f5f5f5`, accent-foreground `#171717`, input `#e5e5e5`, sidebar-accent-foreground `#18181b`, ring `#0a0a0a`, sidebar-ring `#3b82f6`. Only `--color-border` (`#e5e7e3`, the reference's CARD border) intentionally differs from `--color-input`.

## Git

- `main` only; push via the SSH wrapper (`docs/ssh_git_wrapper_v3.py`) per `docs/how-to-git-push-using-ssh-wrapper_SKILL.md` — never commit keys or the paramiko ssh shim (`bin/ssh` stays outside the repo).
- Conventional Commits; run the clean-check gate before every push.
- Never commit: `.env`, `db/*.db`, `test-results/`, `tests/e2e/.auth/` (all gitignored — keep it that way).
