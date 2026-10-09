# Remediation Plan v27 — Session-53 Parity Iteration

Date: 2026-10-09 · Scope: fresh two-site re-audit after the v26 baseline
(`2879cb0` + the session-52/53/54 log docs through `d7d92f7` on `main`, all
green per this session's re-run: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **155/155 e2e** ✓ · 35/35 smoke ✓). Environment survived the
session boundary intact (`.env` with `DATABASE_URL="file:../db/custom.db"`
verified, `db/` at the repo root with the seeded demo workspace,
node_modules installed, Vitest/Playwright configs intact, robots.txt +
sitemap.xml prerendered in the build, `.env.example` present and
accurate). Probes: one-shot `agent-browser eval` scripts on the ONE
shared parity tab (the default browser session — ALWAYS `open
<target-url>` + settle before every eval), the standalone parity server
on :3200 per `scripts/with-server.sh`, real Tab presses via
`agent-browser press Tab` (the v25 discipline: programmatic `focus()`
never engages `:focus`/`:focus-visible` on either site — for the X button
a keydown-dispatched Tab walk inside one eval was needed because the
clone's Radix dialog TRAPS focus while the reference's plain-div dialogs
do not, so the two sites' walk-to-X stop counts differ), and the
class-attribute read as the reliable arbiter (the v26 lesson — the
empty-submit click moves focus to the first invalid input via native
validation on both sites, so behavior-only probes are ambiguous).

## The sweep — method and results

The pass swept the session-53 log's three suggested surfaces — the
**prefers-reduced-motion audit** (sheet slide-in + spinner), the
**print/overscroll rendering check** of the now-white body canvas, and
the **scrollbar styling comparison** at the dialog's `overflow-y-auto`
surfaces — plus a fresh extension into three more never-measured
families (the dark-mode rendering, the app-surface keyboard focus rings
on REAL Tab, and the dialog X-close button's own focus/hover family),
and the standing re-verification set (mobile-nav R1–R4, data drift, the
SEO pair, the v26 fixes live), and the code audit (lint/tsc/tests green;
`npm audit` = the same 5 dev-only ESLint `braces` advisories, no patched
release — accepted, unchanged; secret-pattern scan clean — matches only
in the documented prompt history, the redacted wrapper placeholder, and
the runbook; the v26 changeset `2879cb0` re-reviewed — clean, commented,
pinned).

- **Mobile navigation (task focus) R1–R4 all re-verified live — the 21st
  consecutive check.** R1: the reference's two `fixed top-0 z-[100]`
  toast containers still intercept the burger's center hit at (38,30)
  (`pe:auto`, 390×32, z-100; scrollWidth 395 on `/`), while the clone's
  burger hit is DIRECT on the svg with the viewport `pe:none` and 390
  fit on every route. R2: the reference's sheet still traps after nav
  (`sheetStillOpen: true`); the clone's closes (superset fix #2) — sheet
  288px + Income link (20,185) 247×32 identical. R3: the reference marks
  nothing active on `/` (all five rail links `rgb(63,63,70)`/400, no
  `<nav>` landmark); the clone highlights Dashboard (white/500 + the
  landmark). R4: the reference overflows 395 on `/`+`/dashboard` and 464
  on `/networth`; the clone fits 390 on all six routes. **The Tailwind
  v4 pins hold — the clone's mobile menu works as expected.**
- **Data drift clean (21st consecutive check)**: the reference unchanged
  (allocation 30.5%, Balance `$3475.00`, income `$5000.00`/1 item,
  savings `$1000.00`/1 item, expenses `$525.00`/4 items).
- **SEO check (the brief's standing ask) PASSES**: both sites serve
  `/robots.txt` (allow-all + the sitemap link) and `/sitemap.xml`
  (five URLs, `/login` excluded; origin-keyed fields correctly differ
  via `NEXT_PUBLIC_SITE_URL`).
- **v26 fixes re-verified live (the newest changeset)**: the reference's
  body is still classless (`className ""` on /login and /,
  `-webkit-font-smoothing: auto`; `<html>` classless too) and the
  clone's matches (`""` + `auto` on the parity server); the v26 G2
  autocomplete distribution is green in the 155-test e2e run.
- **Suggestion 1 — prefers-reduced-motion audit (first measurement on
  either site — NO FINDING)**: with `matchMedia('(prefers-reduced-motion:
  reduce)')` armed via the browser's media emulation, the reference's
  mobile sheet STILL runs its full 500ms slide-in (position sampled at
  33ms intervals: −288 → −111 @235ms → −7 @434ms → 0 @634ms; computed
  `transition: 0.5s …transform…`) and the clone's matches on the same
  sampling (−285 → 0 over the same window, `transition: 0.5s`). Both
  sites' CSSOMs contain ZERO `prefers-reduced-motion` rules (a full
  stylesheet walk, nested rules included). The full-page spinner: an
  `animate-spin` probe element on both sites reads
  `animationName: "spin"`, `animationDuration: "1s"`,
  `animationPlayState: "running"` with its transform actually rotating
  under reduce (two reads 500ms apart differ) — neither site gates the
  keyframe. Both sites behave identically: reduced motion is requested
  and ignored on both — parity holds with no action.
- **Suggestion 2 — print/overscroll of the now-white body canvas (first
  measurement — NO FINDING)**: both sites render `body background-color
  rgb(255,255,255)` (the v25/v26 white canvas holds), `overscroll-behavior
  auto` on BOTH body and html, `overflow: visible`, `margin: 0px`, and
  ZERO print media rules in either CSSOM (the full `@media print` walk).
  The two sites print and overscroll byte-identically from the
  computed-style level.
- **Suggestion 3 — scrollbar styling at the dialog `overflow-y-auto`
  surfaces (first measurement — NO FINDING)**: with a dialog open at a
  600px-tall viewport (forcing the scrollable state), the reference's
  panel computes `maxHeight 540px` (90vh), `overflow-y: auto`,
  `scrollHeight 843 > clientHeight 540` — ACTIVELY scrolling — with
  `scrollbar-width: auto`, `scrollbar-color: auto` and ZERO
  `::-webkit-scrollbar`/`scrollbar-*` rules in its CSSOM; the clone's
  panel (`.zb-modal-panel`) computes the identical family (`maxHeight
  540px`, `overflow-y: auto`, `scrollHeight 859 > 540`,
  `scrollbar-width auto`, `scrollbar-color auto`, zero rules). Both
  sites ship completely unstyled NATIVE scrollbars on the dialog
  surface — parity holds with no action.
- **Extension 1 — dark-mode rendering (never measured — NO FINDING)**:
  with `prefers-color-scheme: dark` armed, the reference still renders
  its light theme (body `rgb(255,255,255)`, text `rgb(10,10,10)`, cards
  `rgb(255,255,255)`, classless html, NO `color-scheme`/`theme-color`
  meta, ZERO `prefers-color-scheme` rules in the CSSOM) and the clone
  reads identically on every axis. Neither site ships a dark theme.
- **Extension 2 — the app-surface keyboard focus rings on REAL Tab
  (the v25 sweep covered only the auth + 404 surfaces — NO FINDING)**:
  a real-Tab walk from the parked pointer (5,5) across the dashboard:
  the rail links (stops 1–5) render the reference's blue sidebar-ring
  family (`rgb(59,130,246) 0 0 0 2px` visible layer + a white 0px
  offset — `focus-visible:ring-2`) and the clone's visible layer
  matches (the clone's string carries the v23-documented extra
  transparent lead layers); the Add Item button (stop 6) renders the
  reference's `rgb(255,255,255) 0 0 0 0, rgb(10,10,10) 0 0 0 1px` +
  the v3 ambient on BOTH sites byte-identically; the stat-card toggle
  buttons (stop 7) render NO focus ring on either site
  (`boxShadow: none` both). Three distinct families, all matching.
- **Extension 3 — the items-view filter surfaces (byte-identical)**:
  the "All Categories"/"All Frequencies" Select triggers carry the
  byte-identical class list on both sites (`focus:outline-none
  focus:ring-1 focus:ring-ring` — the plain-focus 1px family, 216×36);
  the search inputs' class prefixes and placeholders match
  ("Search income items...").
- **The dialog X-close button's keyboard-focus + hover family
  (surfaced by extension 2's discipline — REAL FINDING G1)**: measured
  live on both sites (Add Income dialog open, pointer parked, class
  lists read in full, REAL Tab walks to the X on both sides):
  - The reference's X (36×36, 16px lucide-x, rest color
    `rgb(10,10,10)` — the v9 pins) carries the shadcn **ghost-icon
    button base**: `focus-visible:outline-none focus-visible:ring-1
    focus-visible:ring-ring … hover:bg-accent
    hover:text-accent-foreground h-9 w-9`. On a REAL Tab press (18-stop
    walk — the reference's plain-div dialog does NOT trap focus, so
    the X is reached through the page's natural tab order) its
    rendered ring is `rgb(255,255,255) 0 0 0 0, rgb(10,10,10) 0 0 0
    1px, rgba(0,0,0,0) 0 0 0 0` — the **1px** #0a0a0a family with NO
    ambient layers.
  - The clone's X (the `DialogCloseButton` in
    `src/components/ui/dialog.tsx`) carries `focus:outline-none
    focus-visible:ring-2 focus-visible:ring-ring … hover:bg-accent` —
    the **2px** ring and NO hover text color. On a REAL Tab press
    (keydown-dispatched walk inside one eval — the clone's Radix trap
    cycles the dialog's own focusables, so the X lands on the first
    dispatched Tab) its rendered ring is `rgb(10,10,10) 0 0 0 2px`
    (after transparent lead layers) — **2px**, double the reference's.
  - Hover family: the reference runs `hover:bg-accent
    hover:text-accent-foreground` (the icon's currentColor shifts
    `#0a0a0a` → `#171717` on hover); the clone runs `hover:bg-accent`
    only (the icon stays `#0a0a0a`). The hover BG matches; the hover
    TEXT family drifts.
  - Context: this is the SAME class of finding as v25's ring-family
    sweep (distinct families per component — the reference's X runs
    the standard shadcn button base, i.e. the SAME family as the
    dialog Cancel/Save buttons that v26 verified byte-identical to
    the clone's `button.tsx`; the clone's X drifted to a 2px variant
    because `DialogCloseButton` was hand-written in v9 with its own
    class string, before the family discipline existed).
- One measurement-infrastructure observation (not a gap): the
  `with-server.sh` one-invocation pattern kills the server after each
  command, so a page `open`ed in one invocation boots against a server
  that dies mid-data-flight — the clone then renders its v16
  stay-in-app zero-state (the honest, reference-matching behavior for
  a dead API). Focus-ring probes are data-independent so the sweep was
  unaffected; the data-dependent checks (login census) ran inside ONE
  invocation per the established discipline. The API + `db/custom.db`
  were independently verified healthy (login + budget-items round-trip
  against a fresh server).

### G1. [app fix] The dialog X-close button's focus/hover family — align to the reference's shadcn ghost-icon base

Measured live on both sites (REAL Tab walks + full class reads): the
reference's X-close runs `focus-visible:outline-none
focus-visible:ring-1 focus-visible:ring-ring` (a 1px #0a0a0a ring on
keyboard focus — the same family as the dialog Cancel/Save buttons) and
`hover:bg-accent hover:text-accent-foreground` (the icon's currentColor
shifts #0a0a0a → #171717 on hover). The clone's `DialogCloseButton`
runs `focus:outline-none focus-visible:ring-2` (a 2px ring — double the
reference's) and no hover text family.

**Fix (`src/components/ui/dialog.tsx` DialogCloseButton, the one class
string at ~line 63):** `focus:outline-none focus-visible:ring-2` →
`focus-visible:outline-none focus-visible:ring-1`, and add
`hover:text-accent-foreground` after the existing `hover:bg-accent`.
The rest-state pins are untouched (36×36 `h-9 w-9`, 16px lucide-x,
`rounded-md`, `text-[#0a0a0a]`, the hover bg, the sr-only "Close"
superset label). All four dialog consumers (budget-item, line-item,
asset, liability) render the bare `<DialogCloseButton />` with no
className overrides — the single fix covers every dialog.

## Validation of this plan against the codebase

- `rg 'DialogCloseButton' src/` returns exactly 5 hits — the definition
  in `src/components/ui/dialog.tsx` + 4 bare usages
  (`budget-item-dialog.tsx:154`, `line-item-dialog.tsx:124`,
  `asset-dialog.tsx:117`, `liability-dialog.tsx:132`), none passing a
  `className` prop — the fix's single target is the one class string.
- No other surface uses the drifting family: `rg 'focus-visible:ring-2'
  src/` shows the sidebar rail links (the blue sidebar-ring 2px —
  verified matching on real Tab this session), the login submits (the
  v25 #09090b pin), the switch (the v19 pin), the tabs (the v14 pin),
  and the 404 button (the v25 plain-focus pin) — all pinned, verified
  families that must NOT change. The X-close is the only unpinned
  ring-2.
- No existing test asserts the X's focus or hover classes: the v9
  dialog-chrome test pins the geometry (36×36, 16px icon, 6px radius,
  rest color) and the v11 ambient test pins the Save/Add buttons'
  focus-visible family — `rg 'ring-1|ring-2' tests/e2e/dialog-buttons.spec.ts`
  shows no X-class assertions. The new pin is additive.
- The e2e cost: extending the EXISTING v9 "X-close is a 36×36
  in-header button" test with class assertions adds no page flows, no
  logins, and no new fixtures — the suite stays at 155 tests (1
  extended).
- The clone's own `src/components/ui/button.tsx` base already carries
  the target family (`focus-visible:outline-none focus-visible:ring-1
  focus-visible:ring-ring`) — v26 verified it byte-identical to the
  reference's dialog Cancel/Save buttons, so the fix moves the X onto
  the family the codebase itself already standardizes on.

## Execution order (TDD)

1. **RED**: extend the v9 X-close test in
   `tests/e2e/dialog-buttons.spec.ts` to also assert the X's class
   family — `focus-visible:outline-none`, `focus-visible:ring-1` (NOT
   ring-2), and `hover:text-accent-foreground` present, `focus:outline-none`
   (the plain-focus variant) ABSENT. Run → RED (the current app renders
   `focus:outline-none focus-visible:ring-2` and no hover-text class).
2. **G1 fix**: the two edits in `src/components/ui/dialog.tsx`. Run →
   GREEN.
3. **Pin-sanity (the load-bearing check)**: mutate the expected
   `ring-1` to `ring-2` and drop the hover-text expectation in a
   scratch run → FAIL → restore.
4. Full clean-check chain: `npm run lint && npm run typecheck && npm
   test && npm run build && npm run test:e2e` + `bash
   scripts/smoke-test.sh` (155 e2e expected: no new tests, one
   extended).
5. Live re-verification on the :3200 parity server: the X's class list
   + a real-Tab ring read (1px #0a0a0a) + the hover color family.
6. Regenerate the screenshots (`node scripts/capture-screenshots.mjs`
   — the X at rest is unchanged, so byte-identical captures expected);
   align README/CLAUDE/AGENTS/SKILL/session log/worklog + the probe
   README (the v27 catalog).

## Risk notes

- The fix touches ONE class string on a component with four usages and
  five existing e2e pins (the v9 geometry, the v22 third-family, the
  Escape-close superset, the Save-icon, the recurring-row layout) —
  none read the focus/hover classes; the geometry and rest-state are
  untouched.
- The `hover:text-accent-foreground` addition shifts the hovered icon
  color from #0a0a0a to #171717 (the reference's own behavior,
  measured) — invisible at rest, a 13/255 lightness step on hover.
- The X's sr-only "Close" label and the Radix close semantics (the
  Enter/Space activation, the aria) are untouched supersets.
- No API, store, or data changes — a pure presentational parity fix
  (one class string), measured on both sites with the fresh-open +
  settle + parked-pointer + real-Tab disciplines.
