# Remediation Plan v23 — Session-45 Parity Iteration

Date: 2026-10-09 · Scope: fresh two-site re-audit after the v22 baseline
(`38def33` on `main` + the session-45 log doc at `93e3b70`, all green per
this session's re-run: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
**143/143 e2e** ✓ · 35/35 smoke ✓ — the v22 G1 spec fix holds
deterministically). Environment survived the session boundary intact
(`.env` with `DATABASE_URL="file:../db/custom.db"` verified, `db/` at the
repo root with the seeded demo workspace, node_modules installed,
Vitest/Playwright configs intact). Probes: one-shot `agent-browser eval`
scripts on the shared parity browser (sessions created via
`agent-browser session new` — NOTE: `session use` prints `default` and both
"sessions" resolve to ONE browser tab; the active site is whatever the last
`open` pointed at — the probe discipline this session is ALWAYS
`open <target-url>` + settle before every eval; see the sweep lessons), the
standalone parity server on :3200 booted per command through
`scripts/with-server.sh`, and the VLM visual sweep (`z-ai vision` pairs,
the v19–v22 methodology — every flag DOM-verified before it becomes a
finding).

## The sweep — method and results

The pass swept the session-44 log's two measurable suggested surfaces —
the budget-item dialog's MOBILE state (VLM + DOM pair; its 90vh cap was
DOM-measured in v22 but never visually paired) and the mobile sheet's
KEYBOARD semantics (the sheet's focus trap was never swept; the desktop
rail was in v22) — plus two fresh never-measured-at-mobile surfaces
(the register VERIFY-EMAIL state and the custom 404), the standing
task-focus re-verification (mobile navigation R1–R4 + reference
data-drift check), the standing SEO check, and the code audit
(`skills/code-review-and-audit` native-CLI fallback: lint/tsc/tests green;
`npm audit` = the same 5 dev-only ESLint `braces` advisories, no patched
release — accepted, unchanged; secret-pattern scan clean; scandihaven
current at `d4789c3`, patterns already reflected; the v22 changeset
`38def33` re-reviewed — clean, commented, pinned).

- **Mobile navigation (task focus) R1–R4 re-confirmed, all four live
  (17th consecutive)**: R1 (the reference's TWO `fixed top-0 z-[100]` toast
  containers still intercept the burger's center hit at (38,30), `pe:auto`,
  390×32 each; the clone's hit is DIRECT on the svg, viewport `pe:none`;
  burger 28×28 at (24,16) both), R2 (the reference's sheet still traps
  after nav — `sheetStillOpen: true`; the clone's closes; sheet 288px +
  Income link (20,185) 247×32 identical), R3 (nothing active on `/` on the
  reference — all five rail links `rgb(63,63,70)`/400, no `<nav>` landmark;
  the clone highlights Dashboard white/500 + has the landmark), R4 (the
  reference overflows 395px on `/`+`/dashboard`, 464px on `/networth`; the
  clone fits 390 on all six routes). The Tailwind v4 pins hold — the
  clone's mobile menu works as expected.
- **Data drift clean (17th consecutive check)**: reference unchanged since
  session 19 (allocation 30.5%, income `$5000.00`/1 item, savings
  `$1000.00`/1, expenses `$525.00`/4 items, Balance `$3475.00`, guidelines
  30.5/92.3/4.6). One false alarm during the pass: a drift probe read
  62.8%/`$2065` — the CLONE's seed numbers — because the eval ran against
  the page the previous navigation had left (the shared-browser lesson
  above); three re-probes + the per-view census confirm the reference's
  data is unchanged.
- **SEO check (the brief's standing ask) PASSES**: the clone serves
  `/robots.txt` (allow-all + the sitemap link; `User-Agent` casing per RFC
  9309) and `/sitemap.xml` (five URLs, weekly, priorities 1/0.8, `/login`
  excluded) — verified live on :3200 against the reference's files
  (origin-keyed fields correctly differ, `NEXT_PUBLIC_SITE_URL`; the
  reference's capitalized routes `/Income`… are its own paths, the clone's
  lowercase ones are the clone's).
- **Budget-item dialog MOBILE pair (session-44 suggestion 1 — VLM + DOM,
  390×844)**: DOM-identical — panel 358×760 at (16,42), `max-height
  759.6px` (= 90vh), `overflow-y auto`, radius 16, white bg, form row gaps
  24px (space-y-6) on BOTH sides. The VLM pair flagged the classification
  "Need" radio as "thicker border / more prominent" on the clone —
  DOM-REFUTED (5th consecutive dialog-scale VLM misread): both sides
  render 16×16, `1px solid rgb(23,23,23)` (#171717), radius 9999px. The
  other flag was the platform badge (non-finding). **Chrome parity holds.**
- **Mobile sheet KEYBOARD sweep (session-44 suggestion 2)**: initial focus
  lands inside the sheet on a container DIV on both sides; REAL Tab
  presses (CDP key events — synthetic dispatch does not move focus, the
  v22 lesson) cycle the five links at IDENTICAL positions (Dashboard
  (20,145) → Income (20,185) → Expenses (20,225) → Savings (20,265) → Net
  Worth (20,305)) and then WRAP back to Dashboard — a focus loop on both
  (the reference's own sheet traps; the clone's Radix trap matches); the
  focused link's VISIBLE focus indicator is the blue `rgb(59,130,246) 0px
  0px 0px 2px` sidebar-ring layer on BOTH (full-string reads; the clone's
  extra transparent lead layers are v4's ring implementation — invisible;
  the reference's transparent 2px outline vs the clone's `outline: none`
  are both invisible); Escape closes the sheet on both. **No findings.**
- **v22 G2 sub-dialog re-verification (the prior session's fix holds)**:
  the line-item sub-dialog re-measured live on both sites at BOTH
  viewports — desktop 672×680 (maxH 680px = 85vh, form gaps 20px), mobile
  358×717 (maxH 717.4px = 85vh, form gaps 20px) — exactly identical.
- **Verify-email state at MOBILE (fresh surface, measured for the first
  time at 390×844)**: DOM-identical — the icon circle 56px `rgb(241,245,249)`
  radius 9999px with a 28×28 `#334155` shield icon (the reference's mobile
  scale; desktop is 64/32), SIX 40×44 code inputs (x 60→290, gap 6, radius
  8, border `1px solid rgb(228,228,231)`, centered), the Verify button
  294×44 `#0f172a` radius 12 (class `h-11` on the reference — its mobile
  button is 44px too), the h2 20px/700 `#0f172a`, 6 inputs both. The VLM
  pair flagged ONLY the clone's dev-code box — the documented honest
  no-mail superset. **Parity holds** (two probe lessons surfaced: the
  parked-pointer hover artifact hit THIS session's own probe — the clone's
  bg read `#1e293b` until the pointer was parked at (5,5); and one
  transient first geometry read on the reference (button h "40") that two
  re-measures + the `h-11` class refute — settle AND re-measure after a
  state swap).
- **Custom 404 at MOBILE (fresh surface)**: identical — title
  "Nonexistent V23 Probe | ZeroBudget", the 72px/300 `rgb(203,213,225)`
  "404" h1, the quoted-path message, Go Home 123×38 white/`#334155`,
  scrollWidth 390 both. **No findings.**
- **The session-44 log's third suggestion** (the reference's
  5-attempts-exhausted lockout) remains unmeasurable without burning a
  reference account's five verification attempts — the standing note
  (the clone implements the documented resend/reset semantics).

### G1. [test-pin] The mobile sheet's keyboard semantics are measured but unpinned

The sweep above measured the sheet's focus behavior live on both sites
(the Tab loop through the five links, the wrap-around, the visible blue
sidebar-ring focus layer, the initial container focus). The
mobile-navigation spec pins R1–R4, the active-route highlighting, the
hover-under-hover:none semantics, and Escape/overlay dismissal — but
NOTHING pins the keyboard focus order or the focus-ring chrome. The sheet
is the highest-regression-risk surface (a Radix upgrade or a dialog
refactor could silently change the trap behavior, the focus target, or
the ring). Pin it.

**Fix (spec-only):** new test in `tests/e2e/mobile-navigation.spec.ts`
("the sheet's keyboard focus: Tab cycles the five links in a loop, the
blue sidebar-ring renders (v23 G1)"): open the sheet → 7 real Tab presses
with focus reads → assert the order `[Dashboard, Income, Expenses,
Savings, Net Worth, Dashboard, Income]` (the loop wraps) → assert the
focused link's full box-shadow contains `rgb(59, 130, 246) 0px 0px 0px
2px` (the visible blue layer). Pin-sanity (the load-bearing check): flip
one expected label in a scratch run and confirm the test FAILS, then
restore (the TDD-flavored RED for a pin whose app side is already
correct).

### G2. [test-pin] The verify-email state's mobile chrome is measured but unpinned

The v21 spec pins the state's DESKTOP chrome (64px circle, 32px icon,
44px button). This session measured the MOBILE chrome for the first time
(56px circle + 28px icon + 20px h2 — the responsive `h-14 w-14 sm:h-16` /
`h-7 w-7 sm:h-8` / `text-xl sm:text-2xl` scale; inputs 40×44 gap 6;
button 294×44 `#0f172a` radius 12). Nothing pins the mobile rendering —
a responsive-class regression (someone "simplifying" `h-14 sm:h-16` to
`h-16`) would pass the desktop spec and drift mobile. Pin it.

**Fix (spec-only):** new describe in `tests/e2e/verify-email.spec.ts`
("register verify-email gate at MOBILE (v23 — plan G2)") with
`test.use({ viewport: { width: 390, height: 844 } })`: register a
throwaway → assert the circle 56/`rgb(241,245,249)`, icon 28/`#334155`,
six inputs 40×44 radius 8 ta center + the row's gap 6, the button 294×44
`rgb(15,23,42)` radius 12, the h2 20px/700 `#0f172a`. One additional
register-class call per run (5 existing + 1 = 6 — under the 10/IP/15min
bucket; the in-memory limiter also resets on every server boot).

## Validation of this plan against the codebase

- G1: `tests/e2e/mobile-navigation.spec.ts` already runs in a
  390×844/touch context (`test.use` line 24) with real-click sheet opens
  (the "sheet opens at the reference geometry" test's pattern); no
  existing test reads `document.activeElement` or keyboard focus order in
  that file (grep-verified — the sweep's semantics are unpinned). The
  ring assertion's expected layer `rgb(59, 130, 246) 0px 0px 0px 2px` is
  the measured visible layer (the full clone string carries three
  transparent leads — the `toContain` form dodges the lead-layer trap).
- G2: `tests/e2e/verify-email.spec.ts` holds the desktop chrome test
  (circle 64 / icon 32 / button 44 assertions at the default 1280×720
  viewport); `login-card.tsx:580` renders the responsive circle
  (`h-14 w-14 sm:h-16`), line 581 the icon (`h-7 w-7 sm:h-8`), line 583
  the h2 (`text-xl sm:text-2xl`), line 137 the inputs (`w-10 h-11`), line
  607 the button (`h-11 w-full` — 294px at the mobile card's 326px
  content width). A describe-level `test.use({ viewport: ... })` re-pin
  composes with the file-level storageState pin (the mobile-navigation
  spec's desktop describe is the precedent). No mobile-viewport verify
  test exists (grep-verified).

## Execution order (TDD)

1. **G1**: write the keyboard-focus test → pin-sanity RED (mutate one
   expected label → the test fails) → restore → GREEN on the current app.
2. **G2**: write the mobile-chrome test → pin-sanity RED (mutate the
   circle expectation 56→64 → the test fails) → restore → GREEN.
3. Full clean-check chain: `npm run lint && npm run typecheck && npm test
   && npm run build && npm run test:e2e` + `bash scripts/smoke-test.sh`
   (144 e2e expected: 143 + G1 + G2 − wait, +2 = 145).
4. Regenerate the docs screenshots if any changed (none expected — no app
   change); align README/CLAUDE/AGENTS/SKILL/session log/worklog + the
   probe README (the v23 catalog).

## Risk notes

- G1's Tab-order assertion depends on the sheet's focusable set: if the
  sheet's footer or brand ever gains a focusable element BETWEEN the
  links, the order array changes — the test documents the reference's
  measured order (five links, wrap) and should be updated only with a
  fresh two-site measurement, never unilaterally.
- G1's ring read must use the FULL box-shadow string (the v11 truncation
  lesson) — `toContain("rgb(59, 130, 246) 0px 0px 0px 2px")` on the
  complete computed string, never a sliced prefix.
- G2 adds one register call per e2e run — the rate-limit budget note in
  the spec header must be updated (5 → 6 register-class calls) so the
  next session's audit doesn't miscount.
- No app-code change in this plan — the two groups are test-pins of
  measured parity (the app side already matches the reference on every
  axis this session measured). The plan's RED steps are pin-sanity
  mutations (proving the assertions are load-bearing), not app fixes.
