# Session 36 — Fresh verification & parity iteration v18

> Continuation note: `docs/session_35.md` holds the incoming session-33
> conversation summary (the record this session was briefed to review),
> so this work session's formal log lives here. Work-session numbering
> continues the odd convention: 15 → 17 → 19 → 21 → 23 → 25 → 27 → 29 →
> 31 → 33 → 35 (this session), iteration v17 → **v18**.

Date: 2026-10-09 · Baseline: `eec5427` (v17 code `786f961`, all green) ·
Plan: `docs/remediation-plan-v18.md` · Outcome: **1 finding group fixed
TDD-first across THREE files (the card-inline-confirm delete failures —
the net-worth asset/liability twins plus the item-card site the
post-fix grep sweep surfaced: caught confirm bars + the honest error
toasts, rendering unchanged) + the save-failure catch blocks pinned by
2 regression specs + G2: the register-spec flake root-caused (Next.js's
route announcer racing the banner) and hardened; 96 unit · 134 e2e · 30
smoke all green; live parity re-verified; all 15 screenshots regenerated
with ZERO pixel changes (the fix is behavior-only).**

## What happened

1. **Workspace rebuilt from scratch (the sandbox had been reset).** The
   repo was re-cloned at `eec5427`, `npm install` (493 packages, the
   Prisma client re-generated through `db:generate`), `.env` re-created
   from `.env.example` (`DATABASE_URL="file:../db/custom.db"`, a fresh
   `AUTH_SECRET`, `NEXT_PUBLIC_SITE_URL`), `db/custom.db` re-created at
   the repo root via `db:push` + `db:seed`. The standing brief
   requirements all re-verified: the `db/` folder at the repo root, the
   three env vars, Vitest + Playwright configs in place. Full doc chain
   re-read (AGENTS, CLAUDE, README, PAD, SKILL, session_34/35,
   remediation-plan-v17, worklog); the scandihaven pattern repo
   re-cloned and reviewed (its integer-money / Radix / CSS-first-token /
   honest-copy patterns already reflected in this codebase).

2. **Baseline chain at `eec5427` fully green**: lint ✓ · typecheck ✓ ·
   96/96 unit ✓ · build ✓ · 129/129 e2e ✓ (after one register-spec
   flake — root-caused and fixed as G2 this session, see §9) · 30/30
   smoke ✓.

3. **Code audit (skills: code-review-and-audit, native CLI fallback).**
   Phase 1/4 green; Phase 2: `npm audit` = 5 high, all the dev-only
   ESLint `braces` chain (GHSA-vfj7-8cjw-p6xm, no patched release —
   accepted, unchanged advisory); secret scan clean. Phase 3: the v17
   changeset re-reviewed clean (the caught calculator mount effect +
   the 3-spec calculator-error file + docs alignment).

4. **Audit infrastructure rebuilt**: four agent-browser sessions
   (`ref20`/`clone20` desktop 1280×800, `ref20m`/`clone20m` 390×844),
   both sites logged in, the :3200 parity server booted per command
   through `scripts/with-server.sh`.

5. **Data drift check clean (twelfth consecutive)**: reference
   unchanged since session 19 (allocation 30.5%, income `$5000.00`/1
   item, savings `$1000.00`/1 item, expenses `$525.00`/4 items, Balance
   `$3475.00`); clone seed arithmetic intact (net worth
   `-$245,950.00`). New observation: the reference's net worth holds 1
   asset ("Savings Account" `$25,000.00`) and 0 liabilities.

6. **Mobile navigation (task focus) re-verified end-to-end**: R1
   re-confirmed live (the ref's TWO toast containers — both `fixed
   top-0 z-[100]` 390×32 `pe:auto` — intercept the burger's center hit
   at (38,30); the clone's hit is DIRECT on the svg; burger 28×28 at
   (24,16) both). R2 re-confirmed (tapping Income in the ref's sheet
   navigated to `/income` with `sheetStillOpen: true` + overlay count
   1; the clone's sheet CLOSED + 390px fit + `/income`). R3
   re-confirmed (no ref link active on `/` — all five rail links
   `rgb(63,63,70)`/400 and no `<nav>` landmark; the clone highlights
   Dashboard — white + gradient + 500 + landmark). R4 re-confirmed
   (ref scrollWidth 395 on `/` + `/dashboard`, 464 on `/networth`
   full-page load; clone 390 on ALL six routes). Sheet link geometry
   identical (Income at (20,185), 247×32, both). The Tailwind v4 pins
   hold — the clone's mobile menu works on every axis the reference's
   fails.

7. **Fresh angles swept (first-ever measurements)** — the surface class
   the session-34 log suggested: **the net-worth asset/liability error
   tier** (the last dialog family the error-state audit had not
   measured). The reference's entity API was aborted via
   `agent-browser network route --abort`: its asset-card Delete fires
   with NO confirmation and the failed delete leaves the card with
   zero feedback (the DELETE XHR verified fired-and-failed in the
   network log); its failed Edit Asset Save leaves the dialog open
   (its dialogs are plain `fixed` divs — no `[role=dialog]`) with no
   feedback. The clone's save-failure superset was verified live (the
   edit dialog open + "Could not save the asset / Network error — …",
   after one probe iteration — the first probe used a
   `[data-sonner-toast]` selector and missed the toast; the clone's
   toasts are Radix `.zb-toast`) — but BOTH delete paths were swallowed
   as unhandled rejections: `net-worth-view.tsx`'s confirm bars called
   `void deleteAsset(asset.id)` / `void deleteLiability(liability.id)`
   — silent, untested, the same `void` accident as v17's calculator
   load. And the whole net-worth error tier had ZERO e2e coverage.

8. **2 finding groups** (`docs/remediation-plan-v18.md`): G1 the
   net-worth delete-failure catches + toasts (with the save pins as the
   test tier of the same group); G2 the register duplicate-email spec
   flake (see §9).

9. **TDD RED → GREEN (G1)**: 4 new e2e specs
   (`tests/e2e/networth-error.spec.ts`: asset delete card-stays +
   toast, liability delete card-stays + toast, asset save dialog-open +
   toast, liability save dialog-open + toast) — RED confirmed at the
   exact unfixed state (both delete specs failed on the missing toast;
   both save pins passed, proving the existing superset live), then
   GREEN after the 1-file fix (the caught confirm-bar handlers in
   `net-worth-view.tsx`). The grep-swept third site then got its own
   RED → GREEN cycle: a fifth spec in `tests/e2e/items.spec.ts` (the
   item-card delete failure — card stays + confirm bar stays + the
   "Could not delete the item" toast) failed on the missing toast,
   passed after the `item-card.tsx` catch. **G2 flake root-cause mid-flight**: the first
   full-suite regression failed the register duplicate-email spec
   (2 of 4 full runs this session, never in isolation); hardening it
   with a bare `getByRole("alert")` exposed the mechanism via a
   strict-mode violation — **Next.js App Router's route announcer also
   renders `role="alert"`** (`__next-route-announcer__`, empty,
   dynamically mounted): the old `waitForSelector("[role='alert']")`
   matched the ANNOUNCER (a no-op wait), then the one-shot evaluate
   raced the 409's arrival → null. Fixed with a text-filtered retrying
   locator (lesson 36).

10. **Full chain**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ ·
    **134/134 e2e** ✓ (129 + 5 new; the flake's fix verified in file
    isolation AND the full run) · 30/30 smoke ✓.

11. **Live parity re-verification**: a fresh `verify18` session with the
    assets API aborted opens the Share Portfolio card's menu → Delete
    → the confirm bar's Delete: the card STAYS, the confirm bar STAYS
    (the reference's surfaces), and the error toast fires live ("Could
    not delete the asset / Network error — check your connection and
    try again"); with the API live, a clean reload shows the normal
    state with NO toast (3 cards, `-$245,950.00`, seed intact — no
    mutations ever landed; the aborted probes are read-only).

12. **Screenshots**: all 15 regenerated — **zero pixel changes** (the
    fix is behavior-only: the failure branch never renders in the
    content-waiting shots; `git status` on `docs/screenshots/` is
    empty).

13. **Docs aligned**: README (counts 134, plan-v18 row), CLAUDE.md
    (counts, the net-worth + item-card error tiers in the e2e pyramid,
    the v18 e2e-contract note — the route-announcer lesson), AGENTS.md
    (the v18 pin paragraph, the third site), SKILL (state 96/134/30,
    lesson 36 — including the closing grep-sweep discipline, Appendix B
    row), the probe README (v18 catalog + the toast-selector + tab +
    announcer lessons), this log, and the worklogs.

## Suggested next steps

- The error-state audit is now COMPLETE across every entity family:
  boot (v16), budget-item mutations (v16 — plus the card path this
  pass), line-item load/create/delete (v17), and asset/liability
  save/delete (v18) — every tier catches, toasts, and is pinned by
  specs. The closing grep sweep (`grep -rn "void
  (delete|create|update|load|refresh)" src/`) now returns only
  comments and the caught handlers — the discipline worth repeating at
  the end of every future tier sweep (it caught the third site AFTER
  the net-worth fix looked complete).
- The remaining fresh-angle candidates are visual, not error-state: a
  VLM screenshot sweep of the login/register states (the auth surface
  got text-level pins in v12/v13 but no full-page visual diff), or the
  reference's tablet breakpoints (767/768) re-measured post-v11.
- The remaining honest-copy divergences (Google OAuth unavailable,
  forgot-password no-mail) are documented features, not drift —
  converting them into real integrations is a product decision, not a
  parity task.
