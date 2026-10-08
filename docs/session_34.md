# Session 34 — Fresh verification & parity iteration v17

> Continuation note: `docs/session_33.md` holds the incoming session-31
> conversation summary (the record this session was briefed to review),
> so this work session's formal log lives here. Work-session numbering
> continues the odd convention: 15 → 17 → 19 → 21 → 23 → 25 → 27 → 29 →
> 31 → 33 (this session), iteration v16 → **v17**.

Date: 2026-10-08 · Baseline: `7c45de1` (v16 code `13b0088`, all green) ·
Plan: `docs/remediation-plan-v17.md` · Outcome: **1 finding group fixed
TDD-first (the calculator's line-item LOAD failure — caught + the honest
error toast, rendering unchanged) + the previously-unpinned
mutation-failure catch blocks now guarded by 2 regression-pin specs;
96 unit · 129 e2e · 30 smoke all green (first full run, no flakes); live
parity re-verified; all 15 screenshots regenerated with ZERO pixel
changes (the fix is behavior-only).**

## What happened

1. **Workspace rebuilt from scratch (the sandbox had been reset).** The
   repo was re-cloned at `7c45de1`, `npm install` (493 packages, the
   Prisma postinstall re-run through `db:generate`), `.env` re-created
   from `.env.example` (`DATABASE_URL="file:../db/custom.db"`, a fresh
   `AUTH_SECRET`, `NEXT_PUBLIC_SITE_URL`), `db/custom.db` re-created at
   the repo root via `db:push` + `db:seed`. The standing brief
   requirements all re-verified: the `db/` folder at the repo root, the
   three env vars, Vitest + Playwright configs in place. Full doc chain
   re-read (AGENTS, CLAUDE, README, PAD, SKILL, session_32/33,
   remediation-plan-v16, worklog); the scandihaven pattern repo
   re-cloned and reviewed (its integer-money / Radix / CSS-first-token /
   honest-copy patterns already reflected in this codebase).

2. **Baseline chain at `7c45de1` fully green**: lint ✓ · typecheck ✓ ·
   96/96 unit ✓ · build ✓ · 126/126 e2e ✓ (first full run, no flakes) ·
   30/30 smoke ✓.

3. **Code audit (skills: code-review-and-audit, native CLI
   fallback).** Phase 1/4 green; Phase 2: `npm audit` = 5 high, all the
   dev-only ESLint `braces` chain (GHSA-vfj7-8cjw-p6xm, no patched
   release — accepted, unchanged advisory); secret scan clean (only the
   documented demo seed password + the probe DOM selectors). Phase 3:
   the v16 changeset re-reviewed clean (evidence-commented, test-covered
   — the nested-try boot fix + the 3-spec boot-failure file + probes).

4. **Audit infrastructure rebuilt**: four agent-browser sessions
   (`ref18`/`clone18` desktop 1280×800, `ref18m`/`clone18m` 390×844),
   both sites logged in (the reference's mobile login needed a
   textContent-matched programmatic burger/login retry — the first
   `fill` left the React state empty), the :3200 parity server booted
   per command through `scripts/with-server.sh`.

5. **Data drift check clean (eleventh consecutive)**: reference
   unchanged since session 19 (allocation 30.5%, income `$5000.00`/1
   item, savings `$1000.00`/1 item, expenses `$525.00`/4 items, Net
   Balance `+$3475.00`); clone seed arithmetic intact.

6. **Mobile navigation (task focus) re-verified end-to-end**: R1
   re-confirmed live (the ref's TWO toast containers — both `fixed
   top-0 z-[100]` 390×32 `pe:auto` — intercept the burger's center hit
   at (38,30); the clone's hit is DIRECT on the svg; burger 28×28 at
   (24,16) both). R2 re-confirmed (tapping Income in the ref's sheet
   navigated to `/income` with `sheetStillOpen: true` + overlay count 1;
   the clone's sheet CLOSED + 390px fit + `/income`). R3 re-confirmed
   (no ref link active on `/` — all five rail links `rgb(63,63,70)`/400
   and no `<nav>` landmark; the clone highlights Dashboard — white +
   gradient + 500). R4 re-confirmed (ref scrollWidth 395 on `/` +
   `/dashboard`, 464 on `/networth` full-page load; clone 390 on ALL six
   routes). Sheet link geometry identical (Income at (20,185), 247×32,
   both). The Tailwind v4 pins hold — the clone's mobile menu works on
   every axis the reference's fails.

7. **Fresh angles swept (first-ever measurements)** — the surface class
   the session-32 log flagged as the next tier: **the calculator's
   line-item error paths** (the parent-recalc response family). The
   reference's line-items API was aborted via `agent-browser network
   route --abort`: its calculator LOAD renders the SILENT EMPTY-STATE
   ("Total Calculated `$0.00` / Based on 0 items / • Will update
   category total / No line items yet. Start by adding individual items
   that make up this category. / Add First Item" — no error surface); its
   line-item CREATE failure leaves the Add Line Item sub-dialog open
   with NO toast, NO error text, and NO optimistic update (the
   calculator still reads "Based on 1 item" after the failed save); its
   DELETE failure leaves the row in place with zero feedback (its
   calculator deletes with no confirmation). The clone's
   mutation-failure superset was verified live (create: sub-dialog open
   + "Could not save the line item / Network error — …"; delete: row
   stays + "Could not remove the line item / Network error — …") — but
   its calculator LOAD failure was swallowed as an UNHANDLED promise
   rejection (`void loadLineItems(item.id)`), rendering the reference's
   empty-state byte-identically with no honest feedback, and the whole
   error tier had ZERO e2e coverage. Also re-measured: the calculator
   row-action geometry (32×32 buttons, 16×16 icons — the v6 pin holds on
   both sides).

8. **1 finding group** (`docs/remediation-plan-v17.md`): the G1
   calculator load-failure catch + toast, with the mutation pins as the
   test tier of the same group.

9. **TDD RED → GREEN**: 3 new e2e specs
   (`tests/e2e/calculator-error.spec.ts`: load empty-state + toast,
   create dialog-open + toast, delete row-stays + toast) — RED confirmed
   at the exact unfixed values (the load spec failed on the missing
   toast; the create/delete pins passed, proving the existing superset
   live), then GREEN after the 1-file fix (the caught mount effect in
   `calculator-dialog.tsx`). One test-bug fix mid-flight (documented as
   SKILL lesson 35): a NESTED Radix dialog aria-hides the parent — the
   "Based on 0 items" assertion moved after the sub-dialog's Cancel; and
   the first full-suite run flagged nothing else.

10. **Full chain**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ ·
    **129/129 e2e** ✓ (first full run, no flakes) · 30/30 smoke ✓.

11. **Live parity re-verification**: a fresh `clone19` session with the
    line-items API aborted opens the Rent calculator rendering the
    reference's empty-state ($0.00 / 0 items / "No line items yet") WITH
    the error toast caught live ("Could not load the line items /
    Network error — check your connection and try again"); with the API
    live, the calculator reopens showing the normal state with NO toast
    (the toast fires only on actual failures). The dev database was
    restored to its seed state after the mutation probes (the probe line
    item deleted; Rent's amount PATCHed back to `$1850.00`).

12. **Screenshots**: all 15 regenerated — **zero pixel changes** (the
    fix is behavior-only: the failure branch never renders in the
    content-waiting shots; `git status` on `docs/screenshots/` is
    empty).

13. **Docs aligned**: README (counts 129, plan-v17 row), CLAUDE.md
    (counts, the calculator error tier in the e2e pyramid, the v17
    e2e-contract note — the nested-dialog aria-hidden trap), AGENTS.md
    (the v17 pin paragraph), SKILL (state 96/129/30, lesson 35,
    Appendix B row), the probe README (v17 catalog + the
    calculator-error technique + the nested-dialog lesson), this log,
    and the worklogs.

## Suggested next steps

- The error-state audit has now covered the boot, the budget-item
  mutations, and the calculator's line-item tier (load/create/delete).
  The remaining unmeasured edge: the EDIT line-item failure on the
  REFERENCE (its edit flows through the same Save→PUT path as create —
  same-class by construction; the clone's shared catch is pinned by the
  create spec). Low value; skip unless a future audit surfaces drift.
- The net-worth asset/liability mutation failures share the
  dialog-catch pattern (already covered by the same class — the v16
  audit verified the budget-item dialog live; the net-worth dialogs'
  catches are the same code family). Consider one route-abort pin spec
  for an asset Save on the next pass if the tier feels under-pinned.
- The remaining honest-copy divergences (Google OAuth unavailable,
  forgot-password no-mail) are documented features, not drift —
  converting them into real integrations is a product decision, not a
  parity task.
