# ZeroBalance — Remediation Plan & Record

**Version:** 1.1.0 (post-remediation re-verification)
**Date:** 2026-10-07
**Scope:** Full audit of the zero-balance codebase against the live reference
(`https://zero-balance-4885a8f3.base44.app/`) — visual parity, functional
superset, database placement, Tailwind CSS v4 correctness, and test coverage.
**Method:** Recon-driven (agent-browser + computed-style ground truth), then
TDD — every fix below is pinned by a regression test or a scripted check.
**Status:** **All items remediated and verified.** This document is kept as the
authoritative record for future reference and regression hunting.

---

## 1. Verification Snapshot (2026-10-07 re-run)

| Gate | Command | Result |
|------|---------|--------|
| Typecheck | `npm run typecheck` | ✅ clean |
| Lint | `npm run lint` (eslint 9 + react-hooks v6) | ✅ clean |
| Unit tests | `npm test` (Vitest, 8 files) | ✅ **87/87** |
| E2E tests | `npm run test:e2e` (Playwright, 7 specs, desktop + mobile) | ✅ **34/34** |
| API smoke | `bash scripts/smoke-test.sh` (30 steps, prod standalone server) | ✅ **30/30** |
| Live parity | agent-browser, reference vs clone (desktop + mobile) | ✅ parity, superset confirmed |

Live-reference re-check (2026-10-07): **both reference mobile-navigation bugs
are still present on the production reference site** — (1) the empty Toaster
container (`fixed top-0 z-[100] … pointer-events: auto`) still fails the
hamburger hit-test, and (2) the mobile sheet still stays open after a nav-link
tap (`sheetStillOpen: true` after navigating to `/income`). The clone measures
geometrically identical (sheet 288 px, left-anchored, `fixed`, full height,
same 5 nav links) while fixing both behaviors.

---

## 2. Findings & Remediations

### A. Scaffolding / previous-iteration (ORBITAL) residue

| # | Finding | Severity | Remediation | Status |
|---|---------|----------|-------------|--------|
| A-1 | E2E specs (goals/workspace/v25–v30-parity, 8 files) tested the previous ORBITAL app, not ZeroBalance | Critical | Deleted; replaced by 7 ZeroBalance specs (auth, dashboard, items, networth, calculator, mobile-navigation + setup) | ✅ Done |
| A-2 | `scripts/` held 12 ORBITAL-era probe/capture scripts referencing non-existent paths | Medium | Deleted; replaced by `scripts/smoke-test.sh` (30-step API smoke) and `scripts/capture-screenshots.mjs` (10-shot catalog) | ✅ Done |
| A-3 | Root docs (README/AGENTS/CLAUDE/PAD) described the ORBITAL app | High | All four rewritten per their repo skills for ZeroBalance | ✅ Done |
| A-4 | `next.config.ts` had ORBITAL rewrites + `ignoreBuildErrors` guardrail weakening | High | Removed rewrites; removed `ignoreBuildErrors`/`ignoreDuringBuilds`; added `allowedDevOrigins` fix | ✅ Done |
| A-5 | `.env.example` header still said "ORBITAL" | Low | Header corrected to ZeroBalance (this pass) | ✅ Done |

### B. Database placement & path resolution

**User requirement:** `DATABASE_URL="file:../db/custom.db"` with `db/` at the
**repo root**.

Empirically established resolution rules (Prisma 6.11.1):

| Source of `DATABASE_URL` | Anchor for a relative `file:` URL |
|--------------------------|-----------------------------------|
| `.env` file (loaded by Prisma CLI) | `prisma/schema.prisma` directory → `<repo>/db/custom.db` ✅ |
| Shell-inherited env var | Process CWD (varies!) ⚠️ |
| Inline npm-script assignment | Process CWD = repo root → `file:../db/custom.db` → `<repo>/db/custom.db` ✅ |
| Runtime (`src/lib/db-path.ts`) | Always schema-dir anchored ✅ |

| # | Finding | Severity | Remediation | Status |
|---|---------|----------|-------------|--------|
| B-1 | The sandbox exports a polluting absolute `DATABASE_URL` that redirects Prisma CLI to a parent-workspace `db/` | Critical | npm scripts discipline: runtime scripts pin `DATABASE_URL=file:../db/custom.db` inline; Prisma CLI scripts use `env -u DATABASE_URL` so only `.env` is honored | ✅ Done |
| B-2 | Relative `file:` URL semantics differ between CLI and runtime | High | `src/lib/db-path.ts` implements schema-dir anchoring for the runtime; 15 contract tests in `tests/db-path.test.ts` pin the behavior | ✅ Done |
| B-3 | `db/` must live at repo root, git-ignored | Medium | `.gitignore` covers `db/*.db`; seed writes `<repo>/db/custom.db`; e2e uses isolated `db/e2e.db` reset per run by `tests/e2e/global-setup.ts` | ✅ Done |

### C. Tailwind CSS v4 traps (all five, per docs/Tailwind-V4-Validation-Report.md)

| # | Trap | Risk | Remediation (in `src/app/globals.css` unless noted) | Status |
|---|------|------|-----------------------------------------------------|--------|
| C-1 | Bare-HSL triplets in `@theme` resolve to **transparent** | Invisible surfaces | `@theme inline` uses **literal hex values** for every token | ✅ Done |
| C-2 | v4 default palette is oklch → 1–3 sRGB units/channel drift | Color mismatch vs reference | Neutral + brand scales pinned to reference-era hexes | ✅ Done |
| C-3 | `bg-gradient-to-*` utilities interpolate in oklab → visible gradient shift | Hero/summary cards off-brand | Gradient surfaces use explicit `linear-gradient(135deg, var(--forest-dark), var(--forest-medium))` inline styles (engine-independent) | ✅ Done |
| C-4 | `space-y-*` selector rewrite interacts with child `mt-*`/`mb-*` | Mobile nav CTA spacing blowups | No margin utilities on children of `space-y-*` containers | ✅ Done |
| C-5 | Shadow scale shifted one notch heavier in v4 | Card elevation mismatch | `--shadow-sm` pinned to the reference geometry | ✅ Done |
| C-6 | v3-era arbitrary-value syntax `[--var]` for CSS vars | Broken sidebar width | v4-native `w-(--sidebar-width)` syntax | ✅ Done |

### D. Reference-site mobile navigation bugs (superset fixes)

Both bugs verified **live on the reference** during recon (session 1) and
re-verified 2026-10-07.

| # | Reference bug | Evidence on reference | Clone fix | Pinned by |
|---|---------------|------------------------|-----------|-----------|
| D-1 | Empty Toaster container (`fixed top-0 z-[100] w-full p-4`, `pointer-events: auto`) overlays the top half of the hamburger — the button fails `elementFromPoint` hit-tests | `hitTestPasses: false`, blocker = Toaster DIV, `pointer-events: auto` (2026-10-07) | Toast **viewport** is `pointer-events: none` (`src/app/globals.css` §toast, `src/components/ui/toast.tsx`); individual toasts restore `pointer-events: auto` via the open-group variant | `tests/e2e/mobile-navigation.spec.ts` — "the empty toast viewport never blocks the hamburger" (asserts computed `pointer-events` + real click) |
| D-2 | Mobile sheet does **not** close after tapping a nav link | `sheetStillOpen: true` after link → `/income` (2026-10-07) | Nav links in the mobile sheet call `closeModals()` on click (`src/components/budget/sidebar.tsx`) | Same spec — "tapping a nav link navigates AND closes the sheet" |
| D-3 | (related) Sheet height `100%` resolves against the layout viewport (1044 px under 390×844 emulation) instead of the visual viewport | Measured 1044 px sheet vs 844 viewport | Sheet uses `h-svh` like the reference's own desktop rail (`src/components/ui/dialog.tsx`) | Same spec — sheet geometry assertions (288 px, x=0, full height) |

### E. Application bugs found by the new test suites (TDD)

| # | Bug | Symptom | Root cause | Fix | Pinned by |
|---|-----|---------|------------|-----|-----------|
| E-1 | Infinite re-render (React #185) on `/income`, `/expenses`, `/savings` in production build | Page crashes: "Maximum update depth exceeded" | `useBudgetStore((s) => s.items.filter(...))` returns a new array per snapshot → `useSyncExternalStore` loop | Derived-array selector wrapped in `useShallow` (`src/components/budget/items-view.tsx`) | e2e items suite |
| E-2 | Modals rendered but **unclickable** | Overlay swallows all clicks | `.zb-modal-panel` had no positioning; the fixed overlay (z-50) covered the static panel | Panel fixed + centered above the overlay (`src/app/globals.css`, `src/components/ui/dialog.tsx`) | every dialog e2e |
| E-3 | Dialog Close (×) unclickable | Click lands on the sticky header | Sticky header `z-10` stacked over the absolutely-positioned Close button | Close button raised to `z-20` (`src/components/ui/dialog.tsx`) | calculator e2e |
| E-4 | Saving a line item with empty optional dates → 400 | Dialog stays open, error toast | `isoDate().optional()` rejects `""` (HTML form initial value); `Date.parse` also rolls over impossible dates like `2026-02-30` | `optionalIsoDate` preprocessor (`""` → `undefined`) + components round-trip calendar check (`src/lib/validation.ts`) | `tests/validation.test.ts` |
| E-5 | Saving a line item closed the calculator too | Calculator vanishes after save | Shared `closeModals()` cleared all modal state | Scoped `closeLineItemModal` in the store (`src/components/budget/store.ts`) | calculator e2e |
| E-6 | Dialog forms opened empty via quick actions | "Add Income" preselect lost | `ModalHost` conditionally mounts dialogs; `useState(modalKey)` equaled the current key at mount so the reset never fired | Lazy `useState` initializers + identity-change reset in all 4 dialogs | dashboard e2e (quick actions) |

### F. Parity gaps found vs the live reference

| # | Gap | Resolution |
|---|-----|------------|
| F-1 | Mobile sheet showed an active-item highlight the reference doesn't have | `highlightActive={false}` for the sheet nav (reference parity) |
| F-2 | Sidebar icons: Income used `ReceiptText`, Net Worth used wrong glyph | `Receipt` (income) and `TrendingUp` (net worth) — verified against reference |
| F-3 | Avatar fallback text | "U" (first letter of the user email/name) |
| F-4 | Modal title assumed "Add Item" | Reference title is **"Add Budget Item"** — verified live, clone matches |
| F-5 | Calculator chrome assumed static | Reference is **category-adaptive**: "{Category} Calculator" / "Break down your {category} into individual items" — implemented |
| F-6 | Expense-card inline buttons had `aria-label="Edit Rent"` | Reference exposes plain "Edit"/"Calculate" — labels removed (names stay visible-text) |
| F-7 | Donut palette assumed | Measured live: Need `#e07a3b`, Want `#3b7ea1`, Savings `#8fbc3f` (pinned in `src/lib/constants.ts` + dashboard e2e fill assertions) |
| F-8 | Root route behavior | Reference renders the dashboard at `/` (no redirect) — clone matches (`toHaveURL(/\/$/)` e2e) |

### G. Test-infrastructure issues

| # | Issue | Fix |
|---|-------|-----|
| G-1 | Shared `db/e2e.db` polluted across failed runs → seed-dependent assertions poisoned | `tests/e2e/global-setup.ts` resets the e2e database every run; specs clean up their own fixtures |
| G-2 | Calculator e2e cleanup left Rent at $0 (broke later runs) | Cleanup restores seed amounts through the real edit flow |
| G-3 | Mobile geometry measured mid-slide-animation | Assertions wait for the sheet to settle |
| G-4 | Stale dev server on :3000 hijacked smoke-test requests | Smoke test uses dedicated port 3210 + kills orphans first |
| G-5 | Login API rate limit (10/15 min/IP) tripping suites | Setup project authenticates once and shares `storageState`; auth.spec opts out via file-level `test.use({ storageState: … })` |
| G-6 | Radix Select interaction races | Settle-wait between radio check and select click; `getByRole("combobox")` → `getByRole("option")` pattern |

---

## 3. ToDo Ledger

All items below are **completed**; each carries its regression pin so a future
regression can be traced to the exact guard.

- [x] **T1.** Replace ORBITAL e2e specs with ZeroBalance suites (A-1) — *guard: `tests/e2e/*.spec.ts` (34 tests)*
- [x] **T2.** Delete ORBITAL probe scripts; write ZeroBalance smoke + capture scripts (A-2) — *guard: `scripts/smoke-test.sh` 30/30*
- [x] **T3.** Rewrite the four root docs for ZeroBalance (A-3)
- [x] **T4.** Clean `next.config.ts` (A-4) — *guard: `npm run build` succeeds with no rewrites*
- [x] **T5.** Fix `.env.example` header (A-5)
- [x] **T6.** Enforce DB path discipline: `.env` → `file:../db/custom.db`, `db/` at repo root, npm-script pinning, `env -u` for CLI (B-1..B-3) — *guard: `tests/db-path.test.ts` 15/15*
- [x] **T7.** Apply all five Tailwind v4 trap mitigations in `globals.css` (C-1..C-5) — *guard: dashboard e2e computed-style assertions (gradient `rgb(26,58,46)`, sidebar `rgb(250,250,250)`)*
- [x] **T8.** Migrate CSS-var utilities to v4-native syntax (C-6)
- [x] **T9.** Fix toast viewport click-block (superset D-1) — *guard: mobile-navigation e2e #2*
- [x] **T10.** Close mobile sheet on nav (superset D-2) — *guard: mobile-navigation e2e #4*
- [x] **T11.** Pin sheet height to `svh` (D-3) — *guard: mobile-navigation e2e #3*
- [x] **T12.** `useShallow` for derived store selectors (E-1) — *guard: items e2e on production build*
- [x] **T13.** Position + center `.zb-modal-panel` (E-2) — *guard: all dialog e2e*
- [x] **T14.** Raise dialog Close to z-20 (E-3) — *guard: calculator e2e*
- [x] **T15.** `optionalIsoDate` + calendar round-trip validation (E-4) — *guard: `tests/validation.test.ts`*
- [x] **T16.** Scoped `closeLineItemModal` (E-5) — *guard: calculator e2e (server-side recalc without closing)*
- [x] **T17.** Lazy dialog initializers (E-6) — *guard: dashboard quick-action e2e*
- [x] **T18.** Close parity gaps F-1..F-8 — *guard: dashboard/networth/items e2e + live re-check 2026-10-07*
- [x] **T19.** E2E db reset + fixture cleanup discipline (G-1..G-2) — *guard: consecutive full-suite runs stay green*
- [x] **T20.** Smoke test isolation (port, orphan kill, limiter accounting) (G-4) — *guard: `scripts/smoke-test.sh`*

**Open items (deliberate, non-blocking):**

- [ ] *O-1.* The reference's "Continue with Google" button renders on the
  reference login card; the clone keeps the button for visual parity but
  (like any self-hosted deployment without an OAuth provider) it surfaces a
  "not configured" toast instead of wiring a real provider. Wiring a real
  provider is future work and requires deployment-specific credentials.
- [ ] *O-2.* No i18n currently — English only, matching the reference.

---

## 4. Regression Pin Map

| Invariant | Test / check |
|-----------|--------------|
| Toast viewport never blocks the hamburger | `mobile-navigation.spec.ts` → computed `pointer-events` + real click |
| Sheet = 288 px, left-anchored, fixed, full-height | `mobile-navigation.spec.ts` geometry block |
| Nav tap closes the sheet + navigates | `mobile-navigation.spec.ts` |
| Desktop rail = 256 px fixed, mobile chrome hidden ≥768 px | `mobile-navigation.spec.ts` desktop block |
| Hero gradient = `linear-gradient(135deg, rgb(26,58,46), rgb(45,90,74))` | `dashboard.spec.ts` hero assertions |
| Donut fills = `#e07a3b / #3b7ea1 / #8fbc3f` | `dashboard.spec.ts` `.recharts-sector` fill array |
| Calculator recalculates parent server-side, no Save button | `calculator.spec.ts` |
| Line-item mutation keeps calculator open | `calculator.spec.ts` |
| DB path resolution (CLI vs runtime) | `tests/db-path.test.ts` (15) |
| Empty/impossible dates accepted-or-rejected correctly | `tests/validation.test.ts` |
| Login rate limit 10/15 min | `smoke-test.sh` step 30 |
| Money math in integer cents | `tests/money.test.ts` |

---

## 5. How to Re-verify Everything

```bash
npm install
npm run db:push && npm run db:seed     # db/custom.db at repo root
npm run typecheck && npm run lint      # static gates
npm test                               # 87 unit tests
npm run build && npm run test:e2e      # 34 e2e (build is required first)
bash scripts/smoke-test.sh             # 30 API steps on :3210
```

Manual mobile-nav spot check (the user's special focus):

```bash
# boot prod server, then in agent-browser / devtools at 390×844:
#  1. document.elementFromPoint on the hamburger center → must be the button
#  2. click → sheet opens at exactly 288 px, x=0
#  3. tap "Income" → URL /income AND no [role=dialog] in the DOM
#  4. Escape / overlay tap → sheet closes
```
