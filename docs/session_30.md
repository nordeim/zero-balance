# Session 30 — Fresh verification & parity iteration v15

> Continuation note: `docs/session_29.md` holds the incoming session-27
> conversation summary (the record this session was briefed to review),
> so this work session's formal log lives here. Work-session numbering
> continues the odd convention: 15 → 17 → 19 → 21 → 23 → 25 → 27 → 29
> (this session), iteration v14 → **v15**.

Date: 2026-10-08 · Baseline: `04e6b4e` (v14 code `8fb03dd`, all green) ·
Plan: `docs/remediation-plan-v15.md` · Outcome: **1 finding group fixed
TDD-first (the full-page loading state — chrome + DOM + timing); 96 unit
· 123 e2e · 30 smoke all green (first full run, no flakes); live parity
re-verified; 5 of 15 screenshots changed (seed date-text drift only —
the workspace was reset this session, so `db/custom.db` was re-seeded
and the seed's relative-day offsets moved; every pixel diff verified in
the date-text regions), the visual surfaces unchanged.**

## What happened

1. **Workspace rebuilt from scratch.** The sandbox had been reset —
   both repos re-cloned (`zero-balance` at `04e6b4e`, `scandihaven`
   for the pattern reference), `npm install`, `.env` recreated with
   `DATABASE_URL="file:../db/custom.db"`, `npm run db:push` +
   `db:seed` (the `db/` folder at the repo root, the standing brief
   requirements all re-verified: `.env.example` matches, Vitest +
   Playwright configs in place). Full doc chain re-read (AGENTS,
   CLAUDE, README, PAD, SKILL, session_28/29, remediation-plan-v14,
   worklog). The v14 pins spot-checked in the code first (donut tooltip
   formatter + contentStyle/itemStyle, net-worth tab icons, header
   chip).

2. **Baseline chain at `04e6b4e` fully green**: lint ✓ · typecheck ✓ ·
   96/96 unit ✓ · build ✓ · 119/119 e2e ✓ (one login-parity 409 flake
   on the first run — the known class, clean in isolation and on the
   full re-run) · 30/30 smoke ✓.

3. **Code audit (skills: code-review-and-audit, native CLI
   fallback).** Phase 1/4 green; Phase 2: `npm audit` = 5 high, all the
   dev-only ESLint `braces` chain (GHSA-vfj7-8cjw-p6xm, no patched
   release — accepted, unchanged advisory); secret scan clean (0 hits
   in src/scripts/tests/prisma). Phase 3: the v14 changeset re-reviewed
   clean (evidence-commented, all pins test-covered — 2 source files,
   2 spec files, 4 probes, the with-server wrapper).

4. **Audit infrastructure rebuilt**: four agent-browser sessions
   (`ref16`/`clone16` desktop 1280×800, `ref16m`/`clone16m` 390×844),
   both sites logged in, the :3200 parity server booted per command
   through `scripts/with-server.sh`.

5. **Data drift check clean (ninth consecutive)**: reference unchanged
   since session 19 (allocation 30.5%, income `$5000.00`/1 item, savings
   `$1000.00`/1 item, expenses `$525.00`/4 items, Net Balance
   `+$3475.00`); clone seed arithmetic intact (`+$2065.00`).

6. **Mobile navigation (task focus) re-verified end-to-end**: R1
   re-confirmed live (the ref's TWO toast containers — both `fixed
   top-0 z-[100]` 390×32 `pe:auto` — intercept the burger's center hit
   at (38,30); the clone's hit is DIRECT on the svg; burger 28×28 at
   (24,16) both, 16px svg both). R2 re-confirmed (tapping Income in the
   ref's sheet navigated to `/income` with `sheetStillOpen: true` +
   overlay still present; the clone's sheet CLOSED + 390px fit). R3
   re-confirmed (no ref link active on `/` — all five rail links
   `rgb(63,63,70)`/400; the clone highlights Dashboard — white +
   gradient + 500). R4 re-confirmed (ref scrollWidth 395 on `/` +
   `/dashboard`, 464 on `/networth`; clone 390 on ALL SIX routes). Sheet
   link geometry identical (Income at (20,185), 247×32, both).

7. **Fresh angles swept (first-ever measurements)** — the surface class
   the last session flagged as final: **the loading/spinner states**.
   The reference renders a DOM-replacing full-screen spinner on every
   full-page load (desktop AND mobile): `#root` holds ONLY the
   `fixed inset-0 flex items-center justify-center` overlay + the toast
   viewport (no rail, no header, no main, body WHITE behind), the
   spinner is `w-8 h-8 border-4 border-slate-200 border-t-slate-800
   rounded-full animate-spin` (32×32 border-box, 4px borders —
   slate-200 track + slate-800 top spoke, radius 9999px, `spin 1s
   linear infinite`), and it stays up until the DATA renders. The clone
   drifted on three axes: a 2px lime-green/transparent-top spinner
   inside `main` (shell mounted around it), and `booted` flipping after
   the session probe — the views rendered empty while the data popped
   in. Client-side navigations show NO spinner on either site; `/login`
   shows none on either. Also swept: the filter-card Select KEYBOARD
   flow (ArrowDown-open/Enter-select live on both — the ref is
   internally inconsistent: its filter selects highlight the option
   AFTER the current value, its dialog selects highlight the current
   value; the clone's uniform Radix matches the dialog/a11y pattern —
   documented observation), the calculator's line-item dialog Frequency
   select (highlight-current both), the frequency option census
   (identical), and a **three-page VLM screenshot comparison**
   (income/savings/mobile-dashboard) whose flagged diffs were each
   DOM-verified — ALL refuted as data-driven (seed recurring flags +
   payment-method footers + item counts; the card grids measure
   309.3px 3-col gap 16px on both sides; the mobile dashboard compared
   MATCH).

8. **1 finding group** (`docs/remediation-plan-v15.md`): the G1
   loading-state rebuild (chrome + container/DOM + timing).

9. **TDD RED → GREEN**: 4 new e2e specs (`tests/e2e/loading-state.spec.ts`:
   the overlay chrome + DOM replacement, the data-flight timing, the
   client-nav inverse, the 390×844 mobile overlay) — RED confirmed at
   the exact unfixed values (`div.fixed.inset-0` not found; the timing
   spec's overlay count 0 at t+400ms), then GREEN after the 2-file fix
   (`app-shell.tsx` + `store.ts`). Three test-bug fixes mid-flight
   (documented as SKILL lesson 33): the route callbacks must be
   unhooked with `unrouteAll({behavior:'ignoreErrors'})` before spec
   end; Playwright's Desktop Chrome is 1280×720 (read the viewport
   live, don't hard-code 800); and the hero-figure locator needed the
   house's no-comma plain format (`+$2065.00`).

10. **Full chain**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ ·
    **123/123 e2e** ✓ (first full run — the new route-delay specs
    included) · 30/30 smoke ✓.

11. **Live parity re-verification**: the prerendered HTML now ships
    exactly the reference's loading DOM (`fixed inset-0` white-backed
    overlay + the slate spinner + the toast region — ZERO
    aside/header/main elements, verified via curl); the spinner caught
    live on a real reload (`spin` + `rgb(30,41,59)` top spoke); the
    post-boot shell + full seed arithmetic verified on a fresh
    `clone17` session.

12. **Screenshots**: all 15 regenerated — 5 changed (`03-income`,
    `04-expenses`, `05-savings`, `06-networth`, `08-calculator`), every
    diff verified as seed date-text drift (the reset workspace's
    re-seeded DB shifted the seed's relative-day offsets; pixel-diffed
    21–134 sampled pixels, all inside the date-text regions; VLM-read
    of the crops confirms "Sep 30, 2026" → "Oct 1, 2026" class
    changes) — the loading spinner is transient and invisible in the
    content-waiting shots, exactly as predicted.

13. **Docs aligned**: README (counts 123, plan-v15 row), CLAUDE.md
    (counts, the loading-state surface, the v15 e2e-contract note —
    the prerendered-empty-store note rewritten for the spinner
    prerender), AGENTS.md (the v15 pin paragraph + the updated
    prerender note), SKILL (state 96/123/30, lesson 33, Appendix B
    row), the probe README (v15 catalog + the route-delay technique +
    the rotated-bounding-box lesson), this log, and the worklogs.
