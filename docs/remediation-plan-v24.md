# Remediation Plan v24 — Session-47 Parity Iteration

Date: 2026-10-09 · Scope: fresh two-site re-audit after the v23 baseline
(`1420e55` + the session-47 log doc at `dd49681` on `main`, all green per
this session's re-run: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
**145/145 e2e** ✓ · 35/35 smoke ✓). Environment survived the session
boundary intact (`.env` with `DATABASE_URL="file:../db/custom.db"`
verified, `db/` at the repo root with the seeded demo workspace,
node_modules installed, Vitest/Playwright configs intact, robots.txt +
sitemap.xml prerendered in the build). Probes: one-shot
`agent-browser eval` scripts on the shared parity browser (the
"sessions" resolve to ONE browser tab — the discipline is ALWAYS
`open <target-url>` + settle before every eval; this session's OWN
false-read: two "reference" class dumps read the CLONE's forgot page
left in the shared tab after a `with-server.sh` invocation — the census
probe (`probe-v24-auth-census.mjs`) was written to read all three states
in one eval right after a fresh open, which is the reliable form), the
standalone parity server on :3200 per `scripts/with-server.sh`, and the
VLM visual sweep (`z-ai vision` pairs — every flag DOM-verified before
it becomes a finding).

## The sweep — method and results

The pass swept the session-46 log's two measurable suggested surfaces —
the register SIGN-UP state's mobile VLM+DOM pair (its desktop chrome
was v13-pinned; the pre-submit mobile rendering was never visually
paired) and the mobile sheet's ARROW-key semantics (Tab + Escape were
swept in v23; arrows never) — plus a bonus first-time pairing of the
FORGOT-password state (never measured in any session), the
fresh-verification of the newest change (v23 G1's sheet keyboard
semantics, live on both sites), the standing task-focus re-verification
(mobile navigation R1–R4 + reference data-drift check), the standing
SEO check, and the code audit (`skills/code-review-and-audit`
native-CLI fallback: lint/tsc/tests green; `npm audit` = the same 5
dev-only ESLint `braces` advisories, no patched release — accepted,
unchanged; secret-pattern scan clean — matches only in the documented
runbook, the redacted wrapper placeholder, and the repo's own prompt
history; scandihaven current at `d4789c3`, patterns already reflected;
the v23 changeset `1420e55` re-reviewed — clean, commented, pinned).

- **Mobile navigation (task focus) R1–R4 re-confirmed, all four live
  (18th consecutive)**: R1 (the reference's TWO `fixed top-0 z-[100]`
  toast containers still intercept the burger's center hit at (38,30),
  `pe:auto`, 390×32 each; the clone's hit is DIRECT on the svg, viewport
  `pe:none`; burger 28×28 at (24,16) both), R2 (the reference's sheet
  still traps after nav — `sheetStillOpen: true`; the clone's closes;
  sheet 288px + Income link (20,185) 247×32 identical), R3 (nothing
  active on `/` on the reference at the desktop rail — all five links
  `rgb(63,63,70)`/400, no `<nav>` landmark; the clone highlights
  Dashboard white/500 + has the landmark), R4 (the reference overflows
  395px on `/`+`/dashboard`, 464px on `/networth`; the clone fits 390
  on all six routes). The Tailwind v4 pins hold — the clone's mobile
  menu works as expected.
- **v23 G1 re-verified live (the newest change)**: the sheet's keyboard
  sweep re-run on both sites — initial focus lands on a sheet container
  on both; REAL Tab presses cycle the five links at IDENTICAL positions
  (Dashboard (20,145) → Income (20,185) → Expenses (20,225) → Savings
  (20,265) → Net Worth (20,305)) and WRAP back to Dashboard (a focus
  loop on both); the sheet traps through the loop on both; Escape
  closes both. The v23 G1 spec pin (145/145 green this session) covers
  the visible blue #3b82f6 ring layer.
- **Data drift clean (18th consecutive check)**: the reference
  unchanged since session 19 (allocation 30.5%, Balance `$3475.00`,
  income `$5000.00`/1 item, savings `$1000.00`/1 item, expenses
  `$525.00`/4 items, guidelines 30.5/92.3/4.6).
- **SEO check (the brief's standing ask) PASSES**: the clone serves
  `/robots.txt` (allow-all + the sitemap link; `User-Agent` casing per
  RFC 9309) and `/sitemap.xml` (five URLs, weekly, priorities 1/0.8,
  `/login` excluded) — verified live on :3200 against the reference's
  files (origin-keyed fields correctly differ, `NEXT_PUBLIC_SITE_URL`).
- **Register SIGN-UP state at MOBILE (session-46 suggestion 1 — VLM +
  DOM pair, 390×844)**: the VLM pair returned IDENTICAL (the 6th
  consecutive form-scale VLM blind spot — the real deltas are below
  DOM-measured resolution), BUT the DOM pair found two REAL findings —
  the plan's G1 and G2 (below). Everything else matches: h2
  "Create your account" 20px/700 #0f172a centered (the responsive
  `text-xl sm:text-2xl`), placeholders ("you@example.com" / "Min. 8
  characters" / "Re-enter password"), input width 294, radius 12,
  border `1px solid #e2e8f0`, bg `rgba(248,250,252,0.5)`, the Back
  link 127×20 14px/500 #64748b, the submit gap 12px, the h2→first-label
  gap 20px, no overflow (scrollWidth 390 both).
- **Mobile sheet ARROW-key sweep (session-46 suggestion 2)**: full
  parity — ArrowDown/ArrowUp/ArrowRight/ArrowLeft are INERT on both
  sites (focus stays on the sheet container, no sheet scroll, sheet
  stays open, URL unchanged). The sheet's nav list is a plain list on
  both; the reference implements no arrow-key roving. No findings.
- **FORGOT-password state (fresh surface, first-time pair, desktop +
  mobile)**: DESKTOP is identical (h2 "Reset your password" 24px/700
  #0f172a, email input 368×44 fs 14, Send reset link 368×44 #0f172a
  radius 12, Back 127×20, form `space-y-4 sm:space-y-5`). MOBILE
  carries the same two findings as the sign-up state (G1 + G2 below) —
  the reference's forgot input renders the `h-10 sm:h-11` family (40px
  at mobile) with `text-base md:text-sm` (16px — fs matches the clone
  at mobile), and the 10px label gap.
- **Dialog label→input gap re-verified live (the v9 pin holds)**: the
  budget-item dialog's first field gap measures 12px on BOTH sites
  (inline `leading-none` labels, space-y-2 with the globals.css v3
  pin — `.space-y-2 > * + * { margin-block-start: 0.5rem }`, plan v9
  G3). The v9 pin's scope stops at space-y-2; the login-card's
  `space-y-1.5` wrappers were never covered — that omission is G2.
- The session-46 log's third suggestion (the reference's
  5-attempts-exhausted lockout) remains unmeasurable without burning a
  reference account's five verification attempts — the standing note.

### G1. [app fix] The sign-UP and FORGOT forms render 44px controls at mobile — the reference runs the 40px `h-10 sm:h-11` family

Measured live (fresh-open + settled census, `probe-v24-auth-census.mjs`,
390×844 AND 1280×800, both sites): the reference runs THREE distinct
responsive families across its auth forms —

| state | input height | input font | submit height |
|-------|-------------|-----------|---------------|
| sign-in | `h-11 sm:h-12` (44/48) | `text-base md:text-sm` (16/14) | `h-11 sm:h-12` (44/48) |
| sign-up | `h-10 sm:h-11` (40/44) | `text-sm sm:text-base md:text-sm` (14/16/14) | `h-10 sm:h-11` (40/44) |
| forgot | `h-10 sm:h-11` (40/44) | `text-base md:text-sm` (16/14) | `h-10 sm:h-11` (40/44) |

The clone matches the sign-in family exactly but renders the sign-UP and
FORGOT forms on the FLAT `h-11` (44px at mobile) with the sign-in font
family (`text-base md:text-sm` — 16px at mobile where the sign-up wants
14px). At desktop every value coincides (44/14) — which is why the v9
per-state geometry tests and every prior desktop measurement passed; the
drift is mobile-only: the clone's sign-up inputs are 4px taller with a
2px-larger font, its Create account/Send-reset-link buttons 4px taller,
and the same for the forgot form. The reference's own
`h-10 sm:h-11` classes were read off its live DOM (the tie-breaker
discipline; the shared-tab false-read is documented above).

**Fix (`src/components/budget/login-card.tsx`):** split the single
`INPUT_CLS` height/font family into per-mode classes —
`signin`: `h-11 sm:h-12` + `text-base md:text-sm` (unchanged);
`signup`: `h-10 sm:h-11` + `text-sm sm:text-base md:text-sm`;
`forgot`: `h-10 sm:h-11` + `text-base md:text-sm`. The submit button
(line ~323) gets the same per-mode heights — `h-11 sm:h-12` for
sign-in, `h-10 sm:h-11` for sign-up/forgot. The shared base (radius,
border, bg, padding, focus ring, placeholder color) stays in
`INPUT_CLS`; only the height/font tokens move into the mode branches.
Desktop rendering is untouched (all families coincide at ≥768: 44/14
inputs, 44/40 submit — wait, 44; the v9 pins stay green by
construction).

### G2. [app fix] The auth forms' label→input gap renders 4px — the reference renders 10px (the v4 `space-y-1.5` trap, the v9 pin's blind spot)

Measured live on both sites, both viewports, all three states: the
reference's label→input gap is 10px (rect-based: an inline
`text-sm font-medium` label with line-height 20 whose glyph rect is 16
+ a 6px margin below the line box). The reference's v3-compiled
`space-y-1.5` puts `margin-top: 6px` on the input's `relative` wrapper
(measured `relMt: 6px`); the clone's v4 `space-y-1.5` puts
`margin-bottom: 6px` on the INLINE label instead (measured
`labelMb: 6px`, `relMt: 0`) — and vertical margins on inline boxes are
absorbed by the line box, so the margin renders nothing: the clone's
gap is 4px (just the leading). This is the EXACT trap the v9 fix
pinned for `space-y-2` (the dialogs' field wrappers — trap 4b, plan v9
G3: "v4 rewrote `space-y-*` to margin-block-end on `:not(:last-child)`
… with an INLINE first child, vertical margins on inline boxes are
IGNORED by layout"), but the v9 pin's selector scope stopped at
`.space-y-2` — the login-card's three `space-y-1.5` field wrappers
(lines ~223/243/265) were never covered. The dialogs re-measured clean
this session (12px both — the v9 pin works); the auth forms are the
only `space-y-1.5`-with-inline-first-child surfaces in the app (the
dashboard's two `space-y-1.5` wrappers hold block children —
layout-equivalent under either semantics).

**Fix (`src/app/globals.css`):** extend the v9 pin to cover
`space-y-1.5` with the same v3 form —
`.space-y-1.5 > :not(:last-child) { margin-block-end: 0; }` +
`.space-y-1.5 > * + * { margin-block-start: 0.375rem; }` (6px — v3's
space-y-1.5), in the same `@layer utilities` block. This restores the
6px margin onto the `relative` wrapper (a block) where it renders —
the label gap becomes 10px on every auth field at every viewport. The
dashboard's block-child wrappers are unaffected (v3/v4 are equivalent
for blocks).

## Validation of this plan against the codebase

- G1: `src/components/budget/login-card.tsx` line 190 holds `INPUT_CLS`
  (flat `h-11 … text-base … md:text-sm`) and line 216 derives
  `inputCls = p.mode === "signin" ? `${INPUT_CLS} sm:h-12` : INPUT_CLS`
  — the sign-up/forgot branches render the flat family (grep-verified;
  the census probe measured the rendered result). The submit button's
  class (line ~323) carries `h-11` + the sign-in-only `sm:h-12`. The
  verify-email state's code inputs (line ~137, `h-11 w-10`) are a
  SEPARATE family measured 44px at mobile on BOTH sites (v23 G2) —
  untouched by this change. The v9 per-state geometry tests
  (login-parity.spec.ts lines 147–205) pin the DESKTOP values
  (48/44/44) — all three reference families coincide at ≥640 (44px
  inputs, 44/48 submit), so the pins stay green by construction.
- G2: `src/app/globals.css` lines 19–36 hold the v9 pin scoped to
  `.space-y-2` only (grep-verified: `space-y-1.5` appears nowhere in
  globals.css). `rg 'space-y-1\.5' src/` returns exactly five hits: the
  login-card's three field wrappers (the target) and the dashboard's
  two block-child wrappers (layout-equivalent). The Label component
  (`src/components/ui/label.tsx`) documents the dialogs' 12px
  leading-none family — a different, already-pinned pattern.
- Test placement: `tests/e2e/login-parity.spec.ts` already opts out of
  storageState (logged-out surface) and holds the per-state geometry
  describes; a new v24 describe with a 390×844 `test.use` (the
  verify-email spec's mobile describe is the precedent) plus one
  desktop-viewport label-gap test pins both groups. No register-class
  API calls are added (the sign-up/forgot states are pure client swaps
  — no rate-limit budget impact).

## Execution order (TDD)

1. **G1 RED**: write the mobile-viewport tests first — the sign-up
   state's three inputs + Create account button at 40px height, the
   sign-up email input's 14px font; the forgot state's input + Send
   reset link button at 40px; the sign-in state re-pinned at 44 (the
   family that already matches — the guard against over-drift). Run →
   RED (the current app renders 44/44/44/16 at mobile).
2. **G2 RED**: write the desktop label-gap test (the reference's 10px
   rect gap on the sign-in form's first field). Run → RED (the current
   app renders 4px).
3. **G1 fix**: the per-mode `inputCls` + submit-button height branches
   in `login-card.tsx`. Run the G1 tests → GREEN.
4. **G2 fix**: the `space-y-1.5` pin in `globals.css` (the v9 form).
   Run the G2 test → GREEN.
5. **Pin-sanity (the load-bearing check)**: mutate the expected mobile
   height 40→44 and the label gap 10→4 in scratch runs → both tests
   FAIL → restore via unique-context edits (the v23 lesson: the
   `expect(...).toBe(N)` pattern exists in several files — never blind
   replace).
6. Full clean-check chain: `npm run lint && npm run typecheck && npm
   run test && npm run build && npm run test:e2e` + `bash
   scripts/smoke-test.sh` (150 e2e expected: 145 + 5 new — the G1 mobile-family describe [the sign-in guard + sign-up/forgot fixes] + the G2 label-gap pair).
7. Live re-verification on the :3200 parity server: re-run
   `probe-v24-auth-census.mjs` on the clone at mobile — expect the
   reference's exact census (40/40/44 mobile, labelGap 10, relMt 6).
8. Regenerate the docs screenshots if the login pages changed visually
   (the login screenshots at 1280×800 are desktop — unchanged; check
   the capture script's viewport list); align README/CLAUDE/AGENTS/
   SKILL/session log/worklog + the probe README (the v24 catalog).

## Risk notes

- The `h-10 sm:h-11` family only changes rendering below 640px; the v9
  desktop pins (48/44/44) and the v12/v13 banner/placeholder/ring pins
  are desktop-or-viewport-invariant — none read mobile input heights
  today (grep-verified; the only mobile auth pins are the verify-email
  state's, a separate component).
- The `space-y-1.5` pin is a GLOBAL stylesheet change: the dashboard's
  two block-child `space-y-1.5` wrappers render identically under v3
  and v4 semantics (block-child layout equivalence, the v9 comment's
  own analysis) — but the full e2e suite is the guard; if any
  dashboard assertion moved, the tokens/dialog specs would catch it.
- The sign-up input's font family `text-sm sm:text-base md:text-sm`
  renders 16px in the 640–768 band (the reference's own behavior — its
  class list, read live); the clone previously rendered 16px there too
  (text-base), so the sm band is unchanged on both axes.
- No API, store, or data changes — the two groups are pure presentational
  parity fixes on the auth card, both measured on both sites with the
  fresh-open census (the shared-tab false-read lesson encoded in the
  probe README).
