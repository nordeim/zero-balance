# Remediation Plan v16 — Session-31 Parity Iteration

Date: 2026-10-08 · Scope: fresh two-site re-audit after the v15 baseline
(`a141322` / code `286e6c9`) re-verified green (lint · typecheck · 96/96
unit · build · 123/123 e2e — one known login-parity 409 flake, clean in
isolation · 30/30 smoke). Probes: one-shot `agent-browser eval` scripts,
sessions `ref17`/`clone17` desktop 1280×800 + `ref17m`/`clone17m` 390×844,
the standalone parity server on :3200 booted per command through
`scripts/with-server.sh`.

This pass swept the surface class the last session flagged as the natural
sibling of the loading-state work — **the error/network-failure states
during fetches** — plus the standing task-focus re-verification (mobile
navigation R1–R4 + reference data-drift check).

The audit measured, for the first time, what each site does when the DATA
API fails while the page shell loads:

- **The reference renders a SILENT ZERO-STATE.** With its entity API
  (`app.base44.com/api/apps/<id>/entities/*`) aborted during a full-page
  load, the app stays on its route, mounts the FULL shell, and renders
  every figure zeroed — hero `Budget Allocation 0.0%`, `Balance $0.00`,
  status `✓ NET ZERO`, breakdown totals `$0.00`, and the items views show
  `0 items · $0.00` with their STANDARD empty states. No error toast, no
  banner, no retry UI — a transient network failure is visually
  indistinguishable from an empty budget (a data-integrity illusion).
- **The clone BUMPS to `/login`.** `store.boot()`'s single `catch` sets
  `user: null` regardless of WHICH stage failed — a successful session
  probe followed by a failed `refresh()` lands in the same catch as a
  logged-out visitor, `RequireSession` sees `booted && !user`, and the
  user is redirected to the login page. The reference keeps the user in
  the app.

Also swept first-time this pass: the reference's MUTATION-failure surface
(its Save with a dead API is a silent no-op — the dialog stays open with
zero feedback; the clone already keeps the dialog open AND toasts the
error — the superset is in place, verified live), the reference's
mid-session client-nav behavior under a dead API (no refetch — in-memory
data renders, matching the clone's v15-pinned behavior), the reference's
session-probe failure (aborting its `auth/login` POST changes nothing —
its platform cookie session carries the load), and the clone's toast
duration (4000ms — the reference shows no toasts at all, v10, so there is
no parity target).

The mobile-navigation stack (the task focus) was re-verified end-to-end
first (R1/R2/R3/R4 all still live on the reference; all six clone superset
fixes intact), and the reference data-drift check ran clean (unchanged
since session 19: allocation 30.5%, income `$5000.00`/1 item, savings
`$1000.00`/1 item, expenses `$525.00`/4 items, Net Balance `+$3475.00` —
tenth consecutive clean check). The code audit re-ran clean: `npm audit` =
5 high, all the dev-only ESLint `braces` chain (GHSA-vfj7-8cjw-p6xm, no
patched release — accepted, documented); secret-pattern scan clean (0 hits
in src/scripts/tests/prisma).

The audit found **1 clone-side finding group**; no new reference bugs
(the reference's silent zero-state IS the parity target's behavior — the
clone adds honest error feedback on top, the established superset class).

---

## Findings ledger

### G1. [MED] boot() conflates data-fetch failure with logged-out — the clone bumps to /login when the DATA fails

Measured live on the reference (abort `**/entities/**` during a full-page
load of `/` and `/income`): the app STAYS on its route with the full shell
and zeroed figures (hero `0.0%` / `$0.00` / `✓ NET ZERO`; items views
`0 items · $0.00` + their standard empty states; no error surface at all).

Measured live on the clone (abort `**/api/budget-items` during a
full-page load of `/` with a VALID session cookie): the URL ends at
`/login` — `boot()`'s catch sets `user: null` even though `/api/auth/me`
SUCCEEDED, `RequireSession` fires, and the authenticated user is dumped
at the sign-in card.

Drift on two axes:

1. **Stay-in-app parity**: the reference renders its zero-state; the clone
   redirects. An authenticated user with a transient network failure
   should stay in the app (the reference's observable behavior), not be
   treated as logged out.
2. **Honest error (superset)**: the reference's zero-state is a
   data-integrity illusion — a network failure renders as an empty budget
   with no signal. The clone's established superset class (error toasts on
   mutation failures, e.g. "Could not save the item") extends naturally:
   surface a boot-data error toast. The zero-state surfaces themselves
   match the reference (the empty figures/empty states are exactly what
   the reference renders with dead data).

Fix (2 parts):

- `store.ts`: `boot()` distinguishes the session probe from the data
  fetch — nested `try`: when `/api/auth/me` resolves with a user but
  `refresh()` throws, keep the user, set a new `bootError: true` flag,
  and flip `booted: true` (the shell mounts; views render the zero-state
  like the reference). A failed/401 session probe keeps the CURRENT
  behavior (`user: null` → RequireSession redirect — the auth parity
  pinned by the login/redirect specs).
- `app-shell.tsx`: a one-shot effect fires the honest error toast when
  `booted && bootError` — title "Could not load your data", description
  "Network error — check your connection and try again", `variant:
  "error"` (the same error-toast chrome the dialogs use; AppShell is
  inside the root-layout ToastProvider). One-shot: clear the flag when
  fired (a later `refresh()` succeeding must not re-toast; a full reload
  re-runs boot naturally).

Fix files: `src/components/budget/store.ts`,
`src/components/budget/app-shell.tsx`.

### Observations (documented, no action)

- **The reference's mutation failure is a silent no-op**: its Save button
  with a dead entity API leaves the dialog open with NO toast, NO error
  text, NO banner (measured live on the Add Income dialog). The clone
  already keeps the dialog open AND toasts "Could not save the item /
  Network error — check your connection and try again" (verified live in
  this audit) — the superset fix is in place; nothing to change.
- **The reference's mid-session client-nav does not refetch**: with the
  entity API dead, a rail click to Income renders the in-memory data
  ("1 items · $5000.00"). The clone matches (v15 pinned the same
  no-refetch-on-client-nav behavior). No auto-retry is added to the clone
  either — parity; a manual full reload retries on both.
- **The reference's session-probe failure is unobservable**: aborting its
  `auth/login` POST during a page load changes nothing (its platform
  cookie session carries the load — data still renders). The clone's
  `/api/auth/me` network failure keeps the login redirect (the session is
  genuinely unknown from the app's perspective; a 401 probe MUST keep it
  — pinned by spec 3 below).
- **Toast duration**: the clone's ToastProvider pins `duration={4000}`.
  The reference shows no toasts anywhere (v10 documented) — no parity
  target; 4s stays.
- **`/login` under a dead API**: the login card renders on both sites
  (no data fetch — v15 observation, re-verified this pass).
- **The reference's data state is unchanged since session 19** (30.5%,
  +$3475.00, the 1/1/4 item census) — tenth consecutive clean drift
  check.

### Verified matching this pass (no action)

Mobile navigation (task focus, both sites 390×844): R1 re-confirmed live
(the ref's TWO toast containers — both `fixed top-0 z-[100]` 390×32
`pe:auto` — intercept the burger's center hit at (38,30); the clone's hit
is DIRECT on the svg; burger 28×28 at (24,16) both, 16px svg both). R2
re-confirmed (tapping Income in the ref's sheet navigated to `/income`
with `sheetStillOpen: true` + overlay count 2; the clone's sheet CLOSED +
390px fit + `/income`). R3 re-confirmed (no ref link active on `/` — all
five rail links `rgb(63,63,70)`/400; the clone highlights Dashboard —
white + gradient + 500). R4 re-confirmed (ref scrollWidth 395 on `/` +
`/dashboard`, 464 on `/networth` full-page load; clone 390 on ALL six
routes). Sheet link geometry identical (Income at (20,185), 247×32,
both).

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | G1: data-fetch failure at boot stays in-app with the reference's zero-state (no login bump) | `tests/e2e/boot-failure.spec.ts` NEW "data-fetch failure at boot stays in-app (v16)" — route-abort `**/api/budget-items` + `**/api/assets` + `**/api/liabilities` (leave `/api/auth/me` live), `page.goto("/")`, assert: URL stays `/` (no `?from_url=` redirect), the shell renders (the seeded user chip + the hero heading "NET ZERO GOAL"), the zero-state figures render (Budget Allocation `0.0%`, Balance `$0.00`), the items-empty state pattern if navigated; unroute with `unrouteAll({ behavior: "ignoreErrors" })` before spec end | `store.ts` |
| 2 | G1: the honest error toast (superset) — fired once when the data fails at boot | same spec, NEW "boot data-failure shows the error toast once (v16)" — same interception, assert the toast's title "Could not load your data" + description "Network error — check your connection and try again" is visible (role status region), and stays one-shot (no duplicate toasts after the settle) | `app-shell.tsx` |
| 3 | G1 regression pin: a FAILED session probe still redirects (the auth parity must not regress) | same spec, NEW "session-probe 401 still redirects to login (v16 pin)" — route `/api/auth/me` to a 401 `{ ok: false }` envelope, goto `/`, assert the URL becomes `/login?from_url=%2F` and the login card renders | — (pins current behavior) |
| 4 | Docs: session log (`docs/session_32.md` — the session_31.md slot holds the incoming session-29 conversation summary), worklog, README/AGENTS/CLAUDE/SKILL alignment (the v16 pin paragraph + the boot-failure surface), probe README v16 rows | — | docs |
| 5 | Regression: full chain + live parity re-check (route-aborted clone session reproduces the reference's stay-in-app zero-state + the toast; a clean reload recovers the seed figures) + screenshot refresh (no visible change expected — the 15 static shots wait for content) | — | — |

## Regression pin map (must NOT change)

- All six superset fixes (hamburger hit, sheet close-on-nav, root-URL nav
  highlight — rail AND sheet, no mobile overflow, Escape close, delete
  confirmations) and the v9–v15 pins (donut geometry + tooltip, tab icons
  + header chip, banner chrome, titles, placeholders, focus rings, the
  full-page loading state + its data-flight timing)
- The v15 loading-state timing: `booted` still flips only after the data
  resolves for an authed user — the G1 fix adds a SECOND failure branch
  inside the same flow (refresh throwing), it must not alter the success
  path (the loading-state specs re-run green)
- The auth parity: a 401 session probe → login redirect (spec 3 pins it);
  post-logout API 401s (smoke step 28); the login-lands-on-root behavior
- The mutation-failure superset (dialog stays open + error toast) — the
  dialogs' catch blocks are untouched
- e2e fixture discipline: the new specs only abort/delay routes — they
  never write; the aborted handlers are unhooked by the specs' own scope
