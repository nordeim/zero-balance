# Remediation Plan v26 — Session-51 Parity Iteration

Date: 2026-10-09 · Scope: fresh two-site re-audit after the v25 baseline
(`c60cb9e` + the session-51/52 log docs through `6b46804` on `main`, all
green per this session's re-run: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **154/154 e2e** ✓ · 35/35 smoke ✓). Environment survived the
session boundary intact (`.env` with `DATABASE_URL="file:../db/custom.db"`
verified, `db/` at the repo root with the seeded demo workspace,
node_modules installed, Vitest/Playwright configs intact, robots.txt +
sitemap.xml prerendered in the build, `.env.example` present and
accurate). Probes: one-shot `agent-browser eval` scripts on the ONE
shared parity tab (the default browser session — ALWAYS `open
<target-url>` + settle before every eval), the standalone parity server
on :3200 per `scripts/with-server.sh`, and the VLM visual sweep
(`z-ai vision` pairs — every flag DOM-verified before it becomes a
finding).

## The sweep — method and results

The pass swept the session-51 log's two measurable suggested surfaces —
the **dialog buttons' mouse-focus behavior** (the v19 family was
measured with `focusVisible:true` probes; a live Tab-vs-click pair
settles whether the reference gates its ring behind `:focus-visible`
like the clone) and the **verify-email state's inputs as an
aria/landmark/focus surface** (never swept) — plus the standing
re-verification set (mobile-nav R1–R4, data drift, the SEO pair, the
v24 auth census, the v25 fixes live), and the code audit (lint/tsc/
tests green; `npm audit` = the same 5 dev-only ESLint `braces`
advisories, no patched release — accepted, unchanged; secret-pattern
scan clean — matches only in the documented prompt history, the
redacted wrapper placeholder, and the runbook; the v25 changeset
`c60cb9e` re-reviewed — clean, commented, pinned).

- **Mobile navigation (task focus) R1–R4 re-confirmed, all four live
  (20th consecutive)**: R1 (the reference's TWO `fixed top-0 z-[100]`
  toast containers still intercept the burger's center hit at (38,30),
  `pe:auto`, 390×32 each, scrollWidth 395 on `/`; the clone's hit is
  DIRECT on the svg, viewport `pe:none`, 390 fit), R2 (the reference's
  sheet still traps after nav — `sheetStillOpen: true`; the clone's
  closes; sheet 288px + Income link (20,185) 247×32 identical), R3
  (nothing active on `/` on the reference's desktop rail — all five
  links `rgb(63,63,70)`/400, no `<nav>` landmark; the clone highlights
  Dashboard white/500 + has the landmark), R4 (the reference overflows
  395 on `/`+`/dashboard`, 464 on `/networth`; the clone fits 390 on
  all six routes). **The Tailwind v4 pins hold — the clone's mobile
  menu works as expected.**
- **Data drift clean (20th consecutive check)**: the reference
  unchanged (allocation 30.5%, Balance `$3475.00`, income `$5000.00`/1
  item, savings `$1000.00`/1 item, expenses `$525.00`/4 items).
- **SEO check (the brief's standing ask) PASSES**: both sites serve
  `/robots.txt` (allow-all + the sitemap link) and `/sitemap.xml`
  (five URLs, `/login` excluded; origin-keyed fields correctly differ
  via `NEXT_PUBLIC_SITE_URL`).
- **v24 auth census re-run on the reference (the full ladder holds)**:
  the three-family table byte-identical (sign-in `h-11 sm:h-12` 48/16 +
  `text-sm` submit; sign-up `h-10 sm:h-11` 44/14; forgot 44/16 + 44;
  widths 368, label gaps 10, `relMt 6px`) — no platform drift in the
  auth forms.
- **v25 fixes re-verified live (the newest change)**: the reference's
  submit ring still `rgb(9,9,11) 0 0 0 4px` + white offset (REAL Tab
  walk, stop #4), its inputs' ring still `rgb(148,163,184)`, its 404
  "Go Home" still plain-`focus:` `rgb(100,116,139)`, its body bg still
  `rgb(255,255,255)`; the clone's v25 pins all green in the e2e run.
- **Dialog-button mouse-focus pair (session-51 suggestion 1, first
  behavioral measurement — NO FINDING)**: the reference's dialog
  Cancel/Save buttons (class list read live, both buttons) carry
  `focus-visible:outline-none focus-visible:ring-1
  focus-visible:ring-ring` — the same keyboard-gating as the clone's
  `src/components/ui/button.tsx` base (byte-identical class prefix), so
  a mouse click shows NO ring on either site (Chromium's
  `:focus-visible` heuristic: clicks on buttons don't match) and a REAL
  Tab press renders the identical visible layers on both (`rgb(10,10,10)
  0 0 0 1px` + `rgba(0,0,0,0.05) 0 1px 2px` — the clone's string
  carries the documented transparent lead layers, read in full). The
  v19 `focusVisible:true` probe methodology captured the correct
  family. (One measurement subtlety: clicking Save on an EMPTY form
  moves focus to the first invalid input via native validation on both
  sites — the empty-submit path cannot hold focus on the button, which
  is why the class-attribute read is the reliable arbiter.)
- **The verify-email state's inputs as an aria/landmark/focus surface
  (session-51 suggestion 2, first measurement — REAL FINDING G2)**:
  measured live on the reference (fresh registration) and the clone:
  - Structure identical: the `<main>` landmark wraps the state; H2
    "Verify your email"; the "We've sent a 6-digit code to {email}"
    paragraph; a `<form>` holding the six inputs + the hint + the
    "Verify email" submit; the Resend row; the only extra focusable is
    the Base44 PLATFORM badge close button (18×18 at (1233,756) —
    platform chrome, correctly absent).
  - Geometry + behavior identical: 40×44 inputs, gap 6, inputmode
    `numeric`, type `text`; auto-advance on digit entry, backspace on
    empty clears the previous digit and retreats, pasting a 6-digit
    code distributes all six and focuses the last input.
  - **autocomplete drift (G2)**: the reference runs
    `autocomplete="one-time-code"` on the FIRST input ONLY and
    `autocomplete="off"` on inputs 2–6 (the standard OTP convention —
    the browser's one-time-code offer targets the first box); the clone
    carries `one-time-code` on ALL SIX. A DOM-attribute drift with
    browser-facing behavior (WebOTP/autofill offers): G2 below.
  - **Documented supersets (KEEP, no action)**: the clone's
    `aria-label="Digit 1..6"` (the reference's inputs are UNNAMED — the
    same a11y-superset class as the focus trap and the spinner's
    `role="status"`) and the clone's ArrowLeft/ArrowRight focus
    navigation between the boxes (the reference's arrows are INERT —
    measured live: ArrowRight from box 1 stays, ArrowLeft from box 3
    stays; the clone's arrows move — an invisible keyboard-UX
    enhancement that cannot affect rest-state parity).
- **The body's `antialiased` class (a reference-side drift surfaced by
  the standing v25 re-verification — REAL FINDING G1)**: the v25
  session measured the reference's `<body>` as "class `antialiased`
  only"; TODAY the reference's body class is EMPTY (`""` on /login, /,
  and the 404 — three fresh opens each) with
  `-webkit-font-smoothing: auto` (and `<html>` classless, `lang="en"`).
  The reference (or its Base44 shell) REMOVED the antialiased class —
  the same reference-drift class as v19's recurring row and v21's
  row-actions. The clone still renders `<body className="antialiased">`
  (`src/app/layout.tsx:58`) → `-webkit-font-smoothing: antialiased`.
  VISUAL IMPACT on this platform: NONE — an A/B pixel test (the class
  removed via eval, re-shot, PIL-compared) produced byte-identical
  diff counts (37656/22156/19920/12438/9056 px at the >1/>8/>20/>40/>80
  thresholds with AND without the class; Linux Chromium ignores
  font-smoothing) — the 6.62% pair delta is the historical
  two-instance AA noise. On macOS the property IS user-visible
  (grayscale vs subpixel text), so matching the reference's classless
  body is the correct parity move either way. G1 below.
- **VLM pair on the login pages (desktop, both sites)**: VERDICT
  IDENTICAL — correct (the antialiased difference is unphotographable
  on this platform, confirmed by the pixel A/B above).
- **Register-endpoint observation (limits future probes, not a gap)**:
  the reference's `/api/auth/register` started answering
  `400 {"message":"Security verification is required"}` after ~2
  synthetic registrations this session (the first landed the verify
  state normally — the measurements above are from it). A platform-
  side anti-automation defense; future live verify-state probes on the
  reference may be rate-capped. The clone's honest devCode flow is
  unaffected.
- The session-51 log's third suggestion (the reference's
  5-attempts-exhausted lockout) remains unmeasurable without burning a
  reference account's five verification attempts — the standing note
  (now doubly blocked by the register security gate).

### G1. [app fix] The body's `antialiased` class — the reference's body is now classless

Measured live on both sites (three page families, fresh opens):
the reference's `<body>` carries NO class (`className === ""`,
`-webkit-font-smoothing: auto`) — the `antialiased` class it carried
when v25 measured the white-canvas body is gone (a reference-side
change; v25's G3 background measurement is unaffected — the body bg is
still the browser's white canvas on both sites). The clone renders
`<body className="antialiased">` →
`-webkit-font-smoothing: antialiased`. On this Linux Chromium the
rendered result is byte-identical (the A/B pixel test above), and on
macOS the reference's subpixel rendering is the target — so the clone
drops the class to match the reference's classless body exactly.

**Fix (`src/app/layout.tsx` line ~58):** `<body
className="antialiased">` → `<body>` (a classless body, byte-parity
with the reference). The stale references to "class `antialiased`
only" in the comments at `src/app/globals.css:85` and
`tests/e2e/login-parity.spec.ts:597` are updated to the current
measurement (classless body; v25 measured `antialiased`, the reference
dropped it after).

### G2. [app fix] The verify-email code inputs' autocomplete — the reference runs `one-time-code` on the FIRST box only

Measured live on both sites (fresh registrations): the reference's six
verify inputs carry `autocomplete="one-time-code"` on input #1 and
`autocomplete="off"` on inputs #2–6 — the standard OTP convention (the
browser's one-time-code/WebOTP offer targets the first box; the rest
opt out). The clone carries `one-time-code` on all six
(`src/components/budget/login-card.tsx` CodeInputs ~line 105) — every
box is an autofill target, so a browser OTP offer can appear on any
focused box (a behavioral drift the DOM exposes directly).

**Fix (`src/components/budget/login-card.tsx` CodeInputs):** the
input's `autoComplete="one-time-code"` → `autoComplete={i === 0 ?
"one-time-code" : "off"}`. The `inputMode="numeric"`, type, and the
`aria-label` superset stay (the reference's inputs are unnamed — the
labels are the documented a11y superset, invisible to rest-state
parity).

## Validation of this plan against the codebase

- G1: `rg 'antialiased' src/` returns exactly two hits —
  `src/app/layout.tsx:58` (the body class, the fix's only target) and
  the comment in `src/app/globals.css:85` (updated for accuracy). No
  other surface uses the class (the switch thumb/others use Tailwind
  color utilities, not `antialiased`). No spec asserts the body's
  className (grep `className` on body in tests/: only the v25 G3
  background-color pin, which reads `backgroundColor` — unaffected);
  the new pin is additive. Screenshot impact: NONE (the A/B pixel test
  proved the class renders identically on this platform; the
  regenerated captures are byte-identical).
- G2: the CodeInputs component's props are `digits`/`onSetDigit`/
  `disabled`; the autocomplete attribute is a static JSX prop (one
  line). The e2e budget: extending the EXISTING "lands on the verify
  state" test (verify-email.spec.ts:59) with the autocomplete read
  costs NO new register-class call (the suite stays at 5 register
  calls + login-parity's 409 — under the 10/IP/15min bucket). The
  clone's own register endpoint has no security gate (the honest
  devCode flow). No existing assertion reads the inputs' autocomplete
  (grep `one-time-code` in tests/: only login-parity's placeholder
  checks on the auth inputs, a different surface) — the new pin is
  additive.
- The reference's own verify-state inputs are UNNAMED (no aria-label)
  and arrow-INERT; the clone's `aria-label` + arrow navigation are
  documented supersets in the KEEP class — this plan does NOT remove
  them (the same class as the dialog focus trap, the toast viewport's
  aria, and the spinner's role=status).

## Execution order (TDD)

1. **RED**: write the two tests first — (a) login-parity: extend the
   v25 G3 body-canvas test (or add a sibling in the same describe) to
   pin `document.body.className === ""` +
   `getComputedStyle(document.body).webkitFontSmoothing === "auto"`;
   (b) verify-email: extend the "lands on the verify state" chrome
   test to read all six inputs' `autocomplete` attribute — expect
   `["one-time-code", "off", "off", "off", "off", "off"]`. Run → RED
   (the current app renders `antialiased` + six × `one-time-code`).
2. **G1 fix**: `<body>` in layout.tsx. Run (a) → GREEN.
3. **G2 fix**: the conditional autoComplete in CodeInputs. Run (b) →
   GREEN.
4. **Pin-sanity (the load-bearing check)**: mutate (a)'s expected
   className to `"antialiased"` and (b)'s expected first value to
   `"off"` in scratch runs → all FAIL → restore.
5. Full clean-check chain: `npm run lint && npm run typecheck && npm
   test && npm run build && npm run test:e2e` + `bash
   scripts/smoke-test.sh` (154 e2e expected: no new tests, two
   extended).
6. Live re-verification on the :3200 parity server: the clone's body
   class + font-smoothing; the clone's verify-state input attributes
   (fresh throwaway registration — the clone's endpoint has no gate).
7. Regenerate the screenshots (`node scripts/capture-screenshots.mjs`
   — expected byte-identical); align README/CLAUDE/AGENTS/SKILL/
   session log/worklog + the probe README (the v26 catalog).

## Risk notes

- G1 touches the root layout's body — the only consumers of
  font-smoothing are the browser's text rasterizer (invisible on this
  platform, verified) and any future macOS rendering (the reference's
  own behavior — the point of the fix). The `<html lang="en">` tag is
  untouched (identical on both sites).
- G2 is a one-prop attribute change on a surface with five existing
  e2e pins (chrome, wrong-code countdown, mobile geometry, resend,
  unverified-login banner) — none read autocomplete; the auto-advance/
  backspace/paste handlers are untouched (measured identical on both
  sites this session).
- No API, store, or data changes — both fixes are pure presentational
  parity (a class removal + an attribute distribution), measured on
  both sites with the fresh-open + settle discipline.
