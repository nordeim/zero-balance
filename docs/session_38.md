# Session 38 — Fresh verification & parity iteration v19

> Continuation note: `docs/session_37.md` holds the incoming session-35
> conversation summary (the record this session was briefed to review),
> so this work session's formal log lives here. Work-session numbering
> continues the odd convention: 15 → 17 → 19 → 21 → 23 → 25 → 27 → 29 →
> 31 → 33 → 35 → 37 (this session), iteration v18 → **v19**.

Date: 2026-10-09 · Baseline: `7576e56` (v18 code `cf322f6`, all green) ·
Plan: `docs/remediation-plan-v19.md` · Outcome: **1 finding group fixed
TDD-first (the item dialog's recurring-toggle row — the switch moved to
the reference's LEFT-first arrangement, the calendar icon and border
removed, the green-tinted rgb(245,248,245) surface restored; 1 new e2e
spec, RED → GREEN); the pass's fresh verification layer — the VLM
VISUAL SWEEP — ran 12 auth-state pairs + 5 app views + 3 dialogs (the
auth surfaces and app views all IDENTICAL/LAYOUT_IDENTICAL, the one
dialog drift found AND two VLM hallucinations DOM-refuted); 96 unit ·
135 e2e · 30 smoke all green; live parity re-verified (all 8 recurring-row
measurements match exactly); 1 of 15 screenshots changed (the item
dialog shot — the fix is dialog-internal).**

## What happened

1. **Workspace refreshed (no reset this time):** `git pull` fast-forwarded
   `cf322f6..7576e56` (the session_37.md narrative log). The environment
   was intact from the prior session's build (`.env` with
   `DATABASE_URL="file:../db/custom.db"`, `db/custom.db` + `db/e2e.db` at
   the repo root, node_modules, Vitest + Playwright configs) — the
   standing brief requirements all re-verified. Full doc chain re-read
   (AGENTS, CLAUDE, README, PAD, SKILL, session_36/37,
   remediation-plan-v18, worklog); the scandihaven pattern repo re-checked
   (current at `d4789c3`; its integer-money / Radix / CSS-first-token /
   honest-copy patterns already reflected in this codebase).

2. **Baseline chain at `7576e56` fully green, first full run, no
   flakes**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ · 134/134 e2e
   ✓ · 30/30 smoke ✓.

3. **Code audit (skills: code-review-and-audit, native CLI fallback).**
   Phase 1/4 green; Phase 2: `npm audit` = 5 high, all the dev-only
   ESLint `braces` chain (GHSA-vfj7-8cjw-p6xm, no patched release —
   accepted, unchanged advisory); secret-pattern scan clean. Phase 3: the
   pulled v18 changeset re-verified in the code (the caught confirm-bar
   handlers + the route-announcer-hardened register spec + the
   networth-error spec file) before the audit work began.

4. **Audit infrastructure**: four agent-browser sessions
   (`ref21`/`clone21` desktop 1280×800, `ref21m`/`clone21m` 390×844),
   both sites logged in (the reference's mobile login needed the
   keyboard-typing pattern for its React-state fill quirk), the :3200
   parity server booted per command through `scripts/with-server.sh`;
   two more logged-out sessions (`refauth`/`cloneauth`) for the auth
   surface.

5. **Data drift check clean (thirteenth consecutive)**: reference
   unchanged since session 19 (allocation 30.5%, income `$5000.00`/1
   item, savings `$1000.00`/1 item, expenses `$525.00`/4 items, Balance
   `$3475.00`); the census probe needed a fix mid-pass (the literal "·"
   separator in "N items · $X").

6. **Mobile navigation (task focus) re-verified end-to-end**: R1
   re-confirmed live (the ref's TWO toast containers intercept the
   burger's center hit at (38,30) — agent-browser's own actionability
   check REFUSED the click, the bug manifesting live; the synthetic-event
   dispatch was needed to drive the reference's own burger. The clone's
   hit is DIRECT on the svg; burger 28×28 at (24,16) both). R2
   re-confirmed (tapping Income in the ref's sheet navigated to `/income`
   with `sheetStillOpen: true` + overlay 1; the clone's sheet CLOSED +
   390px fit + `/income`). R3 re-confirmed (no ref link active on `/` —
   all five rail links `rgb(63,63,70)`/400, no `<nav>` landmark; the
   clone highlights Dashboard — white + gradient + 500 + landmark). R4
   re-confirmed (ref scrollWidth 395 on `/` + `/dashboard`, 464 on
   `/networth` full-page load; clone 390 on ALL six routes). The Tailwind
   v4 pins hold.

7. **Fresh surface — the VLM VISUAL SWEEP** (the session-36 log's top
   suggestion: "a VLM screenshot sweep of the login/register states —
   the auth surface got text-level pins in v12/v13 but no full-page
   visual diff"), then extended to the app views and dialogs (the layer
   the project had never applied — every prior surface was pinned by
   computed-style probes, never full-page visual AI comparison):
   - **Auth (6 states × 2 sites): IDENTICAL ×6** — login default,
     sign-up, forgot-password, forgot-confirmation
     (IDENTICAL_LAYOUT with the documented honest-copy divergence),
     login error, mobile default. A mechanical pixel-diff layer
     (4–20% deltas) was added as the verification backstop and
     decomposed: font anti-aliasing noise (uniform glyph edges across
     all text — two Chrome instances) + the reference's "Edit with
     Base44" floating platform badge (bottom-right platform chrome,
     not app design). Asset fidelity beyond the VLM: the reference's
     served logo PNG and the clone's `public/zerobalance-logo.png`
     are **byte-identical (MD5 `835c3687…`)**, both 80×80 from 480×480.
   - **App views (5 × 2): LAYOUT_IDENTICAL ×5** — dashboard (its three
     flagged deltas are the documented superset #3 active-nav, the
     avatar letter, and the allocation figure — different demo data),
     income, expenses, savings, net worth.
   - **Dialogs (3 × 2): ONE REAL DRIFT.** The Add Asset dialog
     LAYOUT_IDENTICAL; the calculator's flagged "extra line" DOM-refuted
     as a MATCHING data-conditional (the reference shows the identical
     "• Will update category total" on its Investments $300 calculator
     — hidden on its $0.00 item, exactly the clone's `total !== amount`
     conditional); the **Add Item dialog's recurring-toggle row
     drifted on four axes** — the reference runs the SWITCH LEFT (the
     row's first child at x=16, 12px gap to the label block), NO
     calendar icon, NO border, on a green-tinted `rgb(245,248,245)`
     surface (h 72); the clone ran icon+label left, switch RIGHT
     (`justify-between`), a 1px border, transparent bg (h 74). Found by
     the VLM, then DOM-verified with paired probes before filing.
   - **Two VLM hallucinations DOM-refuted** (the methodology lesson):
     a "faded, smaller, desaturated logo" (MD5-identical assets, 80×80
     both) and a "taller, wider sign-in button" (294×44 both). The
     discipline codified as lesson 37: the VLM is a SCREENING layer;
     every flag needs DOM/measurement verification, and pin specs
     assert measured values, never VLM verdicts.
   - **Tablet breakpoints (767/768/1024, the secondary suggestion)
     re-measured**: the rail↔mobile-chrome switch lands at 768 on both
     (767: mobile header 61px + full-width main both; 768/1024: rail
     flex 256px + header hidden both), no overflow anywhere; the
     first heading sits at x=288 on both at 768 and 1280 — the clone's
     full-width `main` + `md:ml-64` wrapper is a structural DOM
     difference with an identical visual result.

8. **1 finding group** (`docs/remediation-plan-v19.md` G1): the
   recurring-row drift (four axes: arrangement, icon, border,
   background).

9. **TDD RED → GREEN (G1)**: 1 new e2e spec in
   `tests/e2e/dialog-buttons.spec.ts` ("the recurring row renders the
   reference's switch-left tinted layout (v19)") — RED confirmed at the
   exact unfixed state (the swIdx/arrangement assertions failed), GREEN
   after the one-file fix (`budget-item-dialog.tsx`: the Switch moved to
   the row's first child, the `CalendarIcon` and its import removed, the
   border dropped, the `rgb(245,248,245)` inline background added; the
   row's height follows at 72 automatically). The v9 switch-primitive
   pins re-ran green untouched (the tokens spec queries
   `[role="switch"]` position-independently).

10. **Full chain**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ ·
    **135/135 e2e** ✓ (134 + 1 new, first full run, no flakes) · 30/30
    smoke ✓.

11. **Live parity re-verification**: a fresh paired measurement of the
    fixed row on both sites — all EIGHT values match exactly (swIdx 0,
    swX 16, labelX 64, h 72, border 0px, bg `rgb(245,248,245)`, svg 0,
    gap 12px), and the post-fix dialog screenshot pair passes the VLM
    comparison (IDENTICAL).

12. **Screenshots**: all 15 regenerated — **exactly one changed**
    (`07-add-item-modal.png`, the dialog shot carrying the recurring
    row; every other shot pixel-stable — the fix is dialog-internal).

13. **Docs aligned**: README (counts 135, plan-v19 row), CLAUDE.md
    (counts, the recurring-row pin in the e2e pyramid), AGENTS.md (the
    v19 pin paragraph + the VLM-sweep methodology), SKILL (state
    96/135/30, lesson 37 — the VLM screening discipline, Appendix B
    row), the probe README (v19 catalog: the sweep/pixel-diff/MD5
    techniques + the tablet-breakpoint heading-x lesson + the census
    "·" separator), this log, and the worklog.

## Suggested next steps

- The VLM sweep is now the third standing instrument (computed-style
  probes + e2e pin specs + the visual sweep). Good next surfaces for
  it: the MOBILE app views at 390×844 (this pass swept them for auth
  only), the EDIT dialogs' populated states (this pass compared the
  empty add dialogs), and the breakdown drill-down expanded rows.
- The recurring-row family: audit whether any OTHER form row in the
  item dialog (Payment Method, Status, Notes) carries a similar
  arrangement drift under the VLM layer at closer crops — the full-page
  pairs can miss intra-dialog row orderings that crop-pairs catch.
- The remaining fresh-angle candidates from session 36 are now
  exhausted (error-state audit complete through v18, auth visual sweep
  + tablet breakpoints done this pass) — new directions need a new
  surface class: the register POST-SUCCESS landing, the logout
  headless path's live behavior, or a keyboard-navigation sweep.
