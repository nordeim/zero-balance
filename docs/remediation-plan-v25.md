# Remediation Plan v25 — Session-49 Parity Iteration

Date: 2026-10-09 · Scope: fresh two-site re-audit after the v24 baseline
(`4badb7b` + the session-48/49/50 log docs through `e7109fd` on `main`, all
green per this session's re-run: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **150/150 e2e** ✓ · 35/35 smoke ✓). Environment survived the
session boundary intact (`.env` with `DATABASE_URL="file:../db/custom.db"`
verified, `db/` at the repo root with the seeded demo workspace,
node_modules installed, Vitest/Playwright configs intact, robots.txt +
sitemap.xml prerendered in the build, `.env.example` present and
accurate). Probes: one-shot `agent-browser eval` scripts on the ONE
shared parity tab (the default browser session — this session opened a
stray second session once, caught immediately by the blank-page read;
the discipline is ALWAYS `open <target-url>` + settle before every
eval), the standalone parity server on :3200 per
`scripts/with-server.sh`, and the VLM visual sweep (`z-ai vision` pairs
— every flag DOM-verified before it becomes a finding).

## The sweep — method and results

The pass swept the session-48/50 log's two measurable suggested
surfaces — the auth forms at the **sm breakpoint (640–768)** (the
sign-up font's 16px middle step, VLM + DOM pair) and the **auth submit
buttons' focus-visible ring** (never swept in any session; the INPUTS'
focus ring was v13 G3) — plus a bonus first-time sweep of the 404
page's "Go Home" button ring (the 404's geometry was v21-pinned, its
focus chrome never), the login page's FULL keyboard focus walk (every
focusable: Google button, inputs, submit, both swap buttons), the
fresh-verification of the newest change (v24 G1+G2, live on both
sites), the standing task-focus re-verification (mobile navigation
R1–R4 + reference data-drift check), the standing SEO check, and the
code audit (lint/tsc/tests green; `npm audit` = the same 5 dev-only
ESlint `braces` advisories, no patched release — accepted, unchanged;
secret-pattern scan clean — matches only in the documented prompt
history, the redacted wrapper placeholder, and the runbook; the v24
changeset `4badb7b` re-reviewed — clean, commented, pinned).

- **Mobile navigation (task focus) R1–R4 re-confirmed, all four live
  (19th consecutive)**: R1 (the reference's TWO `fixed top-0 z-[100]`
  toast containers still intercept the burger's center hit at (38,30),
  `pe:auto`, 390×32 each; the clone's hit is DIRECT on the svg, viewport
  `pe:none`; burger 28×28 at (24,16) both), R2 (the reference's sheet
  still traps after nav — `sheetStillOpen: true`; the clone's closes;
  sheet 288px + Income link (20,185) 247×32 identical), R3 (nothing
  active on `/` on the reference at the desktop rail — all five links
  `rgb(63,63,70)`/400, no `<nav>` landmark; the clone highlights
  Dashboard white/500 + has the landmark), R4 (the reference overflows
  395px on `/`+`/dashboard`, 464px on `/networth`; the clone fits 390
  on all six routes). **The Tailwind v4 pins hold — the clone's mobile
  menu works as expected.**
- **Data drift clean (19th consecutive check)**: the reference
  unchanged since session 19 (allocation 30.5%, Balance `$3475.00`,
  income `$5000.00`/1 item, savings `$1000.00`/1 item, expenses
  `$525.00`/4 items).
- **SEO check (the brief's standing ask) PASSES**: both sites serve
  `/robots.txt` (allow-all + the sitemap link) and `/sitemap.xml`
  (five URLs, `/login` excluded; origin-keyed fields correctly differ
  via `NEXT_PUBLIC_SITE_URL`).
- **v24 G1+G2 re-verified live (the newest change)**: the auth census
  (`probe-v24-auth-census.mjs`) re-run on BOTH sites at 390×844 — the
  clone now renders the reference's exact three-family table (sign-in
  44/16, sign-up 40/14, forgot 40/16, every label gap 10px, `relMt 6`).
- **Auth forms at the sm breakpoint (640–768 — session-48 suggestion
  1, first measurement in any session)**: the census re-run at
  672×800 on BOTH sites — EXACT match on every axis (sign-in 48/16
  input + 48 submit; sign-up 44/16 input — **the 16px middle step
  renders** (`text-sm sm:text-base md:text-sm`) — + 44 submit; forgot
  44/16 + 44; all widths 368, all label gaps 10, `relMt 6`). The v24
  fix's full responsive ladder is verified at the third viewport. No
  finding.
- **The auth submit buttons' focus-visible ring (session-48
  suggestion 2, first measurement in any session — REAL FINDING
  G1)**: a REAL-Tab keyboard walk (`kb-auth-ring-v25.sh` +
  `kb-login-walk-v25.sh`, pointer parked, CDP Tab presses) over every
  focusable on the reference's login page found:
  - Stop #1 "Continue with Google": browser-default `auto 1px`
    outline, NO custom ring — the clone matches (no finding).
  - Stops #2/#3 (inputs): the v13-pinned two-layer #94a3b8 family —
    the clone matches (no finding).
  - **Stop #4 "Sign in" (the submit): the reference renders
    `rgb(255,255,255) 0 0 0 2px, rgb(9,9,11) 0 0 0 4px, rgba(0,0,0,0.05)
    0 1px 2px` — a white 2px offset + a 2px **zinc-950 `#09090b`** ring
    (its class: `focus-visible:ring-2 focus-visible:ring-ring
    focus-visible:ring-offset-2`, its `--ring` = zinc-950) + the v3
    ambient. The clone renders the SAME composition but with the ring
    colored **`#94a3b8`** (slate-400) — its hardcoded
    `focus-visible:ring-[#94a3b8]`. G1 below.**
  - Stops #5/#6 (the "Forgot password?" / "Need an account? Sign up"
    swap buttons): browser-default `auto 1px` outlines, NO custom
    ring — the clone matches (no finding).
  - Stop #7: the Base44 PLATFORM's floating edit badge
    (`#base44-edit-badge #badge-close`) — platform chrome, not app
    design; correctly absent from the clone (documented, not a gap).
- **The 404 page's "Go Home" button ring (bonus first-time sweep —
  REAL FINDING G2)**: the reference's button (full class read live)
  carries `focus:outline-none focus:ring-2 focus:ring-offset-2
  focus:ring-slate-500` — a plain **`focus:`** (engages on ANY focus,
  not keyboard-only) with a **slate-500 `#64748b`** ring; measured
  `rgb(255,255,255) 0 0 0 2px, rgb(100,116,139) 0 0 0 4px`. The clone
  renders `focus-visible:ring-[#94a3b8]` (slate-400,
  keyboard-focus-only). G2 below. Every OTHER 404 value already
  matches (border #e2e8f0, text #334155, hover #f8fafc/#cbd5e1, the
  w-4 h-4 mr-2 HomeIcon, the #f8fafc page root — v21 pins).
- **The login page's background (surfaced by the focus walk's outline
  drift — REAL FINDING G3, computed-style level)**: the reference's
  `<body>` carries ONLY `antialiased` — it styles NO background (the
  browser's default white canvas; `bodyBg: rgb(255,255,255)`), and its
  warm `#fafaf8` paper is painted by its APP-SHELL wrapper
  (`min-h-screen flex w-full` → `rgb(250,250,248)`, measured up the DOM
  chain), while its 404 page paints its own `#f8fafc` root (v21 pin).
  The clone paints `#fafaf8` on the BODY (`--color-background:
  #fafaf8` + `body { @apply bg-background }` — the value came from the
  v7-era MANIFEST read: the PWA `background_color` splash color, not a
  rendered surface). VISUAL IMPACT: none — the login page's full-viewport
  gradient (the main's `linear-gradient(to right bottom, rgb(248,250,252),
  rgb(241,245,249))` — identical on both sites, re-verified live this
  session) covers the body on /login, the app shell covers it on every
  app page, and the 404's #f8fafc root covers it there (the regenerated
  screenshots are byte-identical — confirmed with PIL pixel reads). The
  reference's browser-default focus-outline serialization difference
  (rgb(16,16,16) vs a 50%-alpha lab() color on the UNSTYLED swap
  buttons) persists post-fix — a Chromium-internal serialization detail
  on UA-default outlines, out of app scope. G3 is a spec-level parity
  fix: the clone's computed body style + its layer structure now match
  the reference exactly (white canvas + shell-painted paper).
- **VLM pair on the login pages (desktop, both sites)**: VERDICT
  IDENTICAL, "none" — CORRECT on the background (the body's tint is
  covered by the identical full-viewport gradient, G3 above) and
  blind on the rings only because keyboard-focus chrome is
  unphotographable in rest-state screenshots. The VLM remains a
  coarse filter; the DOM (and REAL Tab presses) is ground truth.
- The session-48 log's third suggestion (the reference's
  5-attempts-exhausted lockout) remains unmeasurable without burning
  a reference account's five verification attempts — the standing
  note. (The verify-email state's SUBMIT ring is the same unmeasured
  family; it shares the clone's G1 class line and is fixed with it —
  the reference's submit is the same shadcn dark-button family, class
  read on its login submit this session.)

### G1. [app fix] The auth submit buttons' focus-visible ring renders slate-400 — the reference renders zinc-950 `#09090b`

Measured live (REAL Tab presses, pointer parked, 350ms settle — the
200ms transition family) on both sites: the reference's auth submit
(Sign in / Create account / Send reset link — one button component
across the three modes) renders `box-shadow: #fff 0 0 0 2px, #09090b
0 0 0 4px, rgba(0,0,0,0.05) 0 1px 2px` on keyboard focus — the shadcn
`focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2`
family with its `--ring` = zinc-950. The clone renders the identical
composition (offset, width, ambient, outline-none) but colors the ring
`#94a3b8` — the value was copied from the INPUT focus family (v13 G3,
where `#94a3b8` IS correct) onto the button, where the reference runs
its `--ring` token instead. A 4px 2px-wide ring around a dark button:
slate-400 reads as a light gray-blue halo, zinc-950 reads as a
near-black ring — visibly different keyboard-focus chrome.

The reference's OTHER ring families (all previously pinned, all
already matching — this fix touches NONE of them): the login INPUTS'
two-layer #94a3b8 ring (v13 G3), the dialog buttons' 1px #0a0a0a ring
(v11 G2/v19 — the clone matches via `--color-ring: #0a0a0a`), the
search input's 1px currentColor #0a0a0a ring (v5 G10), the sheet's
blue #3b82f6 sidebar ring (v23 G1), the 404's slate-500 ring (G2
below). The auth submit is the ONLY surface where the clone hardcodes
#94a3b8 on a BUTTON.

**Fix (`src/components/budget/login-card.tsx`):** two class strings —
the AuthForm submit (line ~338) and the verify-email state's submit
(line ~624) — change `focus-visible:ring-[#94a3b8]` →
`focus-visible:ring-[#09090b]`. The width (`ring-2`), offset
(`ring-offset-2`), ambient (`shadow-sm`), and `outline-none` stay.

### G2. [app fix] The 404 "Go Home" button's ring renders slate-400 on `focus-visible:` — the reference renders slate-500 `#64748b` on plain `focus:`

Measured live on the reference's 404 page (fresh open, programmatic
focus): `focus:outline-none focus:ring-2 focus:ring-offset-2
focus:ring-slate-500` → `rgb(255,255,255) 0 0 0 2px, rgb(100,116,139)
0 0 0 4px` — the ring engages on ANY focus (mouse click included), and
its color is slate-500, one step darker than slate-400. The clone
renders `focus-visible:ring-[#94a3b8]` — the wrong color AND the
keyboard-only gate (a mouse click on the clone's Go Home shows no
ring; the reference's shows one).

**Fix (`src/app/not-found.tsx` line ~60):** change
`focus-visible:ring-2 focus-visible:ring-[#94a3b8]
focus-visible:ring-offset-2 focus-visible:outline-none` →
`focus:outline-none focus:ring-2 focus:ring-offset-2
focus:ring-[#64748b]` (the reference's full family verbatim).

### G3. [app fix] The body's background token renders the app-shell's warm paper `#fafaf8` — the reference's body renders the plain white canvas

Measured live up the DOM chain on both sites, three page families:
the reference styles NO body background (body class `antialiased`
only, `bg: rgb(255,255,255)` — the browser canvas) and paints its
warm `#fafaf8` paper on the app-shell wrapper (`min-h-screen flex
w-full`); its 404 page paints its own `#f8fafc` root. The clone
paints `#fafaf8` on the body (`--color-background: #fafaf8`, the
manifest's PWA splash color) and nothing on the shell. The rendered
result is VISUALLY IDENTICAL on every page (the login gradient, the
app shell, and the 404 root each cover the body on both sites — the
regenerated screenshots are byte-identical, PIL-verified), so this
is a computed-style + layer-structure parity fix, not a visual one:
the clone's body now computes `rgb(255,255,255)` exactly like the
reference's, and the warm paper sits on the shell wrapper exactly
like the reference's — any future surface that exposes the body
(page transitions, print styles, overscroll rubber-banding) renders
identically on both sites.

**Fix:** `src/app/globals.css` — `--color-background: #fafaf8` →
`#ffffff` (the body's `@apply bg-background` then renders white; the
`--neutral-warm: #fafaf8` token stays for the shell). 
`src/components/budget/app-shell.tsx` line ~93 — the root wrapper
gains the warm paper: `flex min-h-svh w-full` → `flex min-h-svh w-full
bg-(--neutral-warm)` (the v4-native CSS-var syntax, the same family
as the existing `md:pl-(--sidebar-width)`). The v15 loading overlay
already paints its own `#ffffff` ("the body behind is white" — the v15
measurement was right; the body token was wrong), so the loading
state is unaffected — and MORE correct (white body + white overlay).

## Validation of this plan against the codebase

- G1: `rg 'ring-\[#94a3b8\]' src/` returns exactly three hits —
  login-card.tsx:338 (the AuthForm submit, all three modes), :624 (the
  verify submit), and not-found.tsx:60 (G2's target). The login
  INPUTS' ring is NOT a Tailwind ring utility at all (v13's arbitrary
  `focus:shadow-[0_0_0_2px_#fff,0_0_0_4px_#94a3b8]` — unaffected by
  this grep's family and untouched by the fix). The v13 G3 spec pins
  the INPUT family; no existing spec pins the SUBMIT ring (grep
  `ring` in login-parity.spec.ts: only the input-ring test + the v13
  banner notes) — the new pin is additive. The v24 mobile-family
  tests read heights/fonts, not shadows — unaffected.
- G2: not-found.spec.ts pins the 404's structure/title/meta/robots
  (4 tests) — none touch the button's focus chrome; the new pin is
  additive. The reference's `focus:` (not `focus-visible:`) family
  means the e2e test can use plain programmatic `focus()` (no
  `focusVisible` option needed — the v19 dialog-button test needed it
  only because the clone's dialog family is focus-visible-gated; the
  404 fix adopts the reference's plain `focus:`).
- G3: `--color-background` feeds exactly ONE consumer (the body's
  `@apply bg-background`, globals.css:156 — grep-verified, no other
  `bg-background` in src/). `--neutral-warm: #fafaf8` is defined in
  :root (globals.css:143, currently unconsumed) and mirrored by
  `COLORS.neutralWarm` in constants.ts:76 (unit-pinned, untouched).
  The switch thumb's #fafaf8 drift was ALREADY fixed in v9
  (`bg-white` + `ring-0`, switch.tsx:26-28 — the comment documents the
  reference's thumb as white). No spec pins the body's background
  (grep `fafaf8` in tests/: only constants.test.ts's neutralWarm) —
  the new pins are additive. The e2e suite's authed specs (tokens,
  dashboard, …) sample computed surfaces — all read the shell or
  cards, never the body — the warm-paper move is invisible to every
  existing assertion (grep-verified: no `backgroundColor` assertion on
  body exists).
- Test placement: `tests/e2e/login-parity.spec.ts` (logged-out
  surface, opts out of storageState) gets the v25 describe — the
  submit-ring test (sign-in + sign-up states via the client-side
  swap, `focus({focusVisible: true})` + 350ms settle — the v13/v19
  pattern) and the body-white pin; `tests/e2e/not-found.spec.ts` gets
  the Go Home ring pin (plain `focus()`); `tests/e2e/tokens.spec.ts`
  (authed) gets the shell-paper pin (the `flex min-h-svh w-full`
  wrapper's bg on /income + the body's white). No register-class API
  calls added (the sign-up state is a client-side swap — the
  rate-limit budget is untouched).
- Screenshot impact: NONE — the login page's full-viewport gradient, the
  app shell, and the 404 root each cover the body on both sites, so the
  regenerated captures are byte-identical (PIL pixel-verified; the
  catalog re-shoot documents the fact, not a change).

## Execution order (TDD)

1. **RED**: write the four tests first — (a) login-parity: the
   submit-ring test (sign-in's Sign in button + the sign-up state's
   Create account — both read `box-shadow` after `focus({focusVisible:
   true})` + 350ms settle, asserting the white 2px offset + the
   `rgb(9, 9, 11) 0px 0px 0px 4px` ring + the v3 ambient); (b)
   login-parity: the login page's `body` background `rgb(255, 255,
   255)`; (c) not-found: the Go Home link's ring after plain `focus()`
   (+350ms) — the white 2px offset + `rgb(100, 116, 139) 0px 0px 0px
   4px`; (d) tokens: on /income, the body is white AND the shell
   wrapper (`flex min-h-svh w-full`) is `rgb(250, 250, 248)`. Run →
   RED (the current app renders #94a3b8 / #94a3b8 / #fafaf8 body).
2. **G1 fix**: the two `ring-[#94a3b8]` → `ring-[#09090b]` edits in
   login-card.tsx. Run (a) → GREEN.
3. **G2 fix**: the `focus:`-family rewrite in not-found.tsx. Run (c) →
   GREEN.
4. **G3 fix**: `--color-background: #ffffff` in globals.css + the
   `bg-(--neutral-warm)` shell class in app-shell.tsx. Run (b)+(d) →
   GREEN.
5. **Pin-sanity (the load-bearing check)**: mutate (a)'s expected
   ring `rgb(9, 9, 11)` → `rgb(148, 163, 184)`, (c)'s `rgb(100, 116,
   139)` → `rgb(148, 163, 184)`, and (d)'s body `rgb(255, 255, 255)` →
   `rgb(250, 250, 248)` in scratch runs → all FAIL → restore.
6. Full clean-check chain: `npm run lint && npm run typecheck && npm
   test && npm run build && npm run test:e2e` + `bash
   scripts/smoke-test.sh` (154 e2e expected: 150 + 4 new).
7. Live re-verification on the :3200 parity server: re-run the focus
   walk (`kb-login-walk-v25.sh`) on the clone — expect the reference's
   stop-by-stop table (submit ring `rgb(9,9,11)`); re-read the login
   body bg (white) + the shell chain (`rgb(250,250,248)` on the
   wrapper); re-read the 404 ring (`rgb(100,116,139)`).
8. Regenerate the screenshots (`node scripts/capture-screenshots.mjs`
   — the auth-surface captures change); align README/CLAUDE/AGENTS/
   SKILL/session log/worklog + the probe README (the v25 catalog).

## Risk notes

- The submit-ring color is the ONLY axis that changes (width/offset/
  ambient/outline were already identical); the rest-state chrome
  (`box-shadow: shadow-sm` at rest, the hover family) is untouched —
  the v9/v11/v24 geometry pins are shadow-at-rest or height/font
  reads.
- The 404's `focus:` adoption changes the mouse-click behavior (a
  ring now shows on click — the reference's own behavior). No
  existing spec asserts the 404 button's focus-invisible behavior.
- The `--color-background` change is body-only (one consumer,
  grep-verified); the manifest's `background_color: #fafaf8` stays
  (the PWA splash color — the v7 measurement of the reference's
  manifest, a different surface). The `--neutral-warm` shell adoption
  renders the exact same rgb(250,250,248) the app pages rendered
  before (painted one layer up) — every existing computed-style
  assertion on app surfaces is unaffected.
- No API, store, or data changes — all three fixes are pure
  presentational parity on keyboard-focus chrome and the body's
  backdrop, all measured on both sites with the parked-pointer +
  settle discipline.
