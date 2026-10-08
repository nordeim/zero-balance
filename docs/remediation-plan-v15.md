# Remediation Plan v15 — Session-29 Parity Iteration

Date: 2026-10-08 · Scope: fresh two-site re-audit after the v14 baseline
(`04e6b4e` / code `8fb03dd`) re-verified green (lint · typecheck · 96/96
unit · build · 119/119 e2e — one known login-parity 409 flake, clean in
isolation and on the full re-run · 30/30 smoke). Probes: one-shot
`agent-browser eval` scripts, sessions `ref16`/`clone16` desktop 1280×800 +
`ref16m`/`clone16m` 390×844, the standalone parity server on :3200 booted
per command through `scripts/with-server.sh`.

This pass swept the surface class the last session flagged as the final
unmeasured one — **the loading/spinner states during data fetches** — plus
the Select/listbox KEYBOARD flows, a three-page VLM screenshot sweep
(income / savings / mobile dashboard), and the standing task-focus
re-verification (mobile navigation R1–R4 + reference data-drift check).

**The loading-state audit found the session's one real drift** (G1 below):
the reference renders a full-screen, DOM-replacing spinner while its data
loads, and the clone's boot spinner drifts from it on three axes — chrome
(border width, colors, and orientation), container/DOM (inline-in-main vs
fixed full-screen, shell vs no shell), and TIMING (the clone's `booted`
flag flips after the session probe, before the data fetch lands — the
views render empty and the data pops in).

Also swept first-time this pass: the filter-card Select keyboard flow
(ArrowDown-open → Enter-select, live on both sites — the reference is
internally INCONSISTENT: its filter selects highlight the option AFTER the
current value on open while its dialog selects highlight the current value;
the clone's Radix highlights the current value everywhere, matching the
reference's dialog pattern and the a11y-correct standard — documented
observation, no action), the calculator's line-item dialog select (the
same highlight-current pattern both sides), the frequency option census
(One-time / Weekly / Bi-weekly / Monthly / Quarterly / Annually —
identical), and a VLM three-page comparison whose flagged diffs were each
DOM-verified (all data-driven: seed recurring flags + payment-method
footers + item counts; the card grid measures 309.3px 3-col gap 16px on
both sides; the mobile dashboard compared MATCH).

The mobile-navigation stack (the task focus) was re-verified end-to-end
first (R1/R2/R3/R4 all still live on the reference; all six clone superset
fixes intact), and the reference data-drift check ran clean (unchanged
since session 19: allocation 30.5%, income `$5000.00`/1 item, savings
`$1000.00`/1 item, expenses `$525.00`/4 items, Net Balance `+$3475.00`;
clone seed arithmetic intact at `+$2,065.00`). The code audit re-ran clean:
`npm audit` = 5 high, all the dev-only ESLint `braces` chain
(GHSA-vfj7-8cjw-p6xm, no patched release — accepted, documented);
secret-pattern scan clean (0 hits in src/scripts/tests/prisma).

The audit found **1 clone-side finding group**; no new reference bugs.

---

## Findings ledger

### G1. [MED] The boot loading state drifts from the reference on chrome, DOM, and timing

Measured live on the reference (full-page loads of `/`, `/income`,
`/networth`, desktop AND mobile): while data loads, the app renders ONLY a
full-screen centered spinner — `#root` contains exactly two children (the
spinner overlay + the toast viewport), NO rail, NO header, NO main
(`textLen: 0`), and the body behind is plain white. The overlay:

```
<div class="fixed inset-0 flex items-center justify-center">   ← transparent, z auto
  <div class="w-8 h-8 border-4 border-slate-200 border-t-slate-800
              rounded-full animate-spin"></div>
</div>
```

Spinner chrome (computed): 32×32 border-box (`w-8 h-8`), 4px borders —
slate-200 `rgb(226,232,240)` on three sides + slate-800 `rgb(30,41,59)` on
TOP (the visible "spoke"), radius 9999px, `spin 1s linear infinite`. The
spinner centers at the viewport midpoint (620,380 at 1280×800; the mobile
overlay measures 390×844). Trigger: FULL-PAGE LOADS only — client-side
navigations show no spinner on either site (data already in memory), and
`/login` shows none either.

The clone (current) drifts on three axes:

1. **Chrome**: `h-8 w-8 animate-spin rounded-[9999px] border-2` with
   `border-color: var(--lime-green)` + `border-t-color: transparent` — a
   2px brand-green ring with a transparent spoke, vs the reference's 4px
   slate ring with the slate-800 spoke.
2. **Container/DOM**: the spinner renders INSIDE `main`
   (`flex flex-1 items-center justify-center p-8`) with the sidebar and
   mobile top bar already mounted around it — vs the reference's
   DOM-replacing `fixed inset-0` overlay with NO shell mounted.
3. **Timing**: `store.boot()` sets `booted: true` right after
   `/api/auth/me` resolves and only THEN awaits `refresh()` — the spinner
   hides when the session probe lands while the data is still in flight,
   and the views render empty before the data pops in. The reference's
   spinner covers the data fetch (dataLoaded stays false until the figures
   render).

Fix (3 parts):

- `app-shell.tsx`: when `!booted`, return ONLY the overlay —
  `fixed inset-0 flex items-center justify-center` with an inline white
  `background` (the reference's observable loading state is white behind
  the transparent overlay — its body has no warm bg until the app mounts;
  the clone's body is `#fafaf8`, so the overlay paints the white itself) —
  wrapping the spinner rebuilt to the reference's chrome:
  `h-8 w-8 animate-spin rounded-[9999px] border-4 border-[#e2e8f0]
  border-t-[#1e293b]` (hex pins per the v8 named-palette lesson — the
  reference's slates compute as plain rgb in its v3 build; 9999px per the
  v9 radius lesson). KEEP `role="status"` + `aria-label="Loading"` (the
  documented a11y-superset class — the reference has no aria).
- `store.ts`: in `boot()`, flip `booted` AFTER `refresh()` resolves for an
  authed user (anonymous/no-session visitors keep the immediate flip —
  RequireSession redirects either way).
- The prerendered HTML now ships the spinner INSTEAD of the shell with the
  empty-store header — the "header AND empty-state Add-buttons coexist in
  static HTML" hydration race documented in AGENTS.md/CLAUDE.md
  DISAPPEARS (the empty state only renders after boot, post-data). The
  docs' settle-pattern notes get updated accordingly (the wait-for-heading
  discipline still applies — it is just no longer load-bearing against a
  strict-mode double match).

Fix files: `src/components/budget/app-shell.tsx`, `src/components/budget/store.ts`.

### Observations (documented, no action)

- **The reference's Select components are internally inconsistent**: its
  filter-card selects highlight the option AFTER the current value when
  opened via ArrowDown (measured: "All Categories" trigger → "Salary"
  highlighted), while its dialog selects (the line-item dialog's Frequency)
  highlight the CURRENT value — the standard Radix behavior the clone uses
  everywhere. The reference's filter triggers also omit `aria-haspopup`
  and don't mark the current value `aria-selected`. The clone's uniform
  Radix semantics match the reference's DIALOG pattern (the a11y-correct
  one) — same documented-superset class as the dialog focus trap. The ref's
  filter-select quirk is its own inconsistency, in the same bucket as the
  v13 trapped-sheet link-color finding.
- **VLM sweep (income / savings / mobile dashboard)**: the mobile
  dashboard compared MATCH; the income/savings flags were all refuted in
  the DOM as data-driven — the clone's seed carries recurring flags
  (the conditional Recurring badge, v8 pin) and payment methods (the
  footer row, v14 observation), and has 2 income / 2 savings items vs the
  reference's 1/1. The card grid measures `309.3px 309.3px 309.3px` with
  16px gap on BOTH sites; the clone's income card is 30px taller purely
  from the badge wrap.
- **The reference's data state is unchanged since session 19** (30.5%,
  +$3475.00, the 1/1/4 item census) — ninth consecutive clean drift check.
- **`/login` shows no loading state on either site** (no data fetch — the
  login card renders directly).

### Verified matching this pass (no action)

Mobile navigation (task focus, both sites 390×844): R1 re-confirmed live
(the ref's TWO toast containers — both `fixed top-0 z-[100]` 390×32
`pe:auto` — intercept the burger's center hit at (38,30); the clone's hit
is DIRECT on the svg; burger 28×28 at (24,16) both, 16px svg both). R2
re-confirmed (tapping Income in the ref's sheet navigated to `/income`
with `sheetStillOpen: true`; the clone's sheet CLOSED + 390px fit). R3
re-confirmed (no ref link active on `/` — all five rail links
`rgb(63,63,70)`/400; the clone highlights Dashboard — white + gradient +
500). R4 re-confirmed (ref scrollWidth 395 on `/` + `/dashboard`, 464 on
`/networth`; clone 390 on ALL six routes). Sheet link geometry identical
(Income at (20,185), 247×32, both).

Select/listbox keyboard flows: the dialog Frequency select opens on
ArrowDown with the current value highlighted (both), Enter selects and
closes (both — verified end-to-end on the reference's filter select: the
list re-filtered to "1 items · $5000.00" after selecting Salary; the
clone's flow matches on the dialog pattern). Frequency option census:
One-time / Weekly / Bi-weekly / Monthly / Quarterly / Annually — identical
to the clone's `FREQUENCY_LABELS`.

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | G1: full-page loading state → the reference's DOM-replacing fixed overlay + slate spinner chrome | `tests/e2e/loading-state.spec.ts` NEW "full-page loading state renders the reference's spinner overlay (v15)" — route-intercept the four API endpoints with a delay, `page.goto("/")`, assert: the overlay (`fixed inset-0`, flex centered, background #ffffff) is the app's only shell (no `aside`/`header`/`main` in the DOM), the spinner's offsetWidth/Height 32, borderTop 4px `rgb(30,41,59)`, other sides `rgb(226,232,240)`, borderRadius 9999px, `spin` 1s linear infinite, `role="status"` | `app-shell.tsx`, `store.ts` |
| 2 | G1: the spinner covers the data fetch (not just the session probe) | same spec, NEW "the spinner persists while the data is in flight (v15)" — delay ONLY `/api/budget-items` (+ assets/liabilities) ~1200ms, leave `/api/auth/me` instant; goto, wait 400ms, assert the overlay is STILL mounted and no money figure is painted; then wait for the overlay's disappearance and assert the seeded hero figure (`+$2,065.00`) IS rendered | `store.ts` |
| 3 | G1 mobile: the overlay covers the 390×844 viewport | same spec, NEW "mobile loading overlay covers the viewport (v15)" — `test.use` 390×844, delayed routes, goto, assert overlay 390 wide ≥844 tall + the same spinner chrome + no shell | `app-shell.tsx` |
| 4 | Docs: session log (`docs/session_30.md` — the session_29 slot holds the incoming session-27 conversation summary), worklog, README/AGENTS/CLAUDE/SKILL alignment (the v15 pin paragraph + the OBSOLETE prerendered-empty-state notes in the e2e contract), probe README v15 rows | — | docs |
| 5 | Regression: full chain + live parity re-check of the fixed loading state (fresh clone session, delayed-network window reproduced via route interception is Playwright-only — live check verifies the overlay chrome + the post-data disappearance) + screenshot refresh (no visible change expected in the 15 static shots — the spinner is transient; the shots wait for content) | — | — |

## Regression pin map (must NOT change)

- All six superset fixes (hamburger hit, sheet close-on-nav, root-URL nav
  highlight — rail AND sheet, no mobile overflow, Escape close, delete
  confirmations) and the v9–v14 pins (donut geometry + tooltip, tab
  icons + header chip, banner chrome, titles, placeholders, focus rings)
- The client-side-navigation behavior: NO spinner on SPA route changes
  (the store persists across mounts — `booted` stays true) — pinned by
  the "persists while data in flight" spec's inverse (the overlay must
  NOT reappear on a client-side nav; assert in spec 3)
- The `/login` surface: no spinner (the login page never mounts AppShell)
  — the login-parity specs already pin the card's direct render
- e2e fixture discipline: all three new specs only read (route delays
  never write) — no fixture impact; the delayed routes are unhooked by
  the specs' own scope
- The toast viewport stays `pointer-events: none` (R1 pin) — the overlay
  is a different, transient surface; when it unmounts, the toast viewport
  (mounted by the shell) returns with the shell
