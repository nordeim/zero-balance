# Session 32 — Fresh verification & parity iteration v16

> Continuation note: `docs/session_31.md` holds the incoming session-29
> conversation summary (the record this session was briefed to review),
> so this work session's formal log lives here. Work-session numbering
> continues the odd convention: 15 → 17 → 19 → 21 → 23 → 25 → 27 → 29 →
> 31 (this session), iteration v15 → **v16**.

Date: 2026-10-08 · Baseline: `a141322` (v15 code `286e6c9`, all green) ·
Plan: `docs/remediation-plan-v16.md` · Outcome: **1 finding group fixed
TDD-first (the boot data-failure state — stay-in-app zero-state parity +
the one-shot honest error toast); 96 unit · 126 e2e · 30 smoke all green
(first full run, no flakes); live parity re-verified; all 15 screenshots
regenerated with ZERO pixel changes (the fix is behavior-only).**

## What happened

1. **Workspace synced (no reset this time).** `git pull` brought in
   `docs/session_31.md` (the incoming session-29 conversation summary)
   at `a141322`. The environment from session 29 survived intact
   (`node_modules`, `.env` with `DATABASE_URL="file:../db/custom.db"`,
   the seeded `db/custom.db` at the repo root, the standalone build).
   Full doc chain re-read (AGENTS, CLAUDE, README, PAD, SKILL,
   session_30/31, remediation-plan-v15, worklog). The standing brief
   requirements all re-verified: `.env.example` matches the codebase's
   three env vars, Vitest + Playwright configs in place, the `db/`
   folder at the repo root.

2. **Baseline chain at `a141322` fully green**: lint ✓ · typecheck ✓ ·
   96/96 unit ✓ · build ✓ · 123/123 e2e ✓ (one login-parity 409 flake
   on the first run — the known class, clean in isolation) · 30/30
   smoke ✓.

3. **Code audit (skills: code-review-and-audit, native CLI
   fallback).** Phase 1/4 green; Phase 2: `npm audit` = 5 high, all the
   dev-only ESLint `braces` chain (GHSA-vfj7-8cjw-p6xm, no patched
   release — accepted, unchanged advisory); secret scan clean. Phase 3:
   the v15 changeset re-reviewed clean (evidence-commented, test-covered
   — the app-shell/store loading-state fix + the 4-spec file + probes).

4. **Audit infrastructure rebuilt**: four agent-browser sessions
   (`ref17`/`clone17` desktop 1280×800, `ref17m`/`clone17m` 390×844),
   both sites logged in, the :3200 parity server booted per command
   through `scripts/with-server.sh`.

5. **Data drift check clean (tenth consecutive)**: reference unchanged
   since session 19 (allocation 30.5%, income `$5000.00`/1 item, savings
   `$1000.00`/1 item, expenses `$525.00`/4 items, Net Balance
   `+$3475.00`); clone seed arithmetic intact (`+$2065.00`).

6. **Mobile navigation (task focus) re-verified end-to-end**: R1
   re-confirmed live (the ref's TWO toast containers — both `fixed
   top-0 z-[100]` 390×32 `pe:auto` — intercept the burger's center hit
   at (38,30); the clone's hit is DIRECT on the svg; burger 28×28 at
   (24,16) both). R2 re-confirmed (tapping Income in the ref's sheet
   navigated to `/income` with `sheetStillOpen: true` + overlay count 2;
   the clone's sheet CLOSED + 390px fit). R3 re-confirmed (no ref link
   active on `/` — all five rail links `rgb(63,63,70)`/400; the clone
   highlights Dashboard — white + gradient + 500). R4 re-confirmed (ref
   scrollWidth 395 on `/`+`/dashboard`, 464 on `/networth` full-page
   load; clone 390 on ALL six routes). Sheet link geometry identical
   (Income at (20,185), 247×32, both).

7. **Fresh angles swept (first-ever measurements)** — the surface class
   the last session flagged as the natural sibling of the loading-state
   work: **the error/network-failure states during fetches**. The
   reference's entity API (`app.base44.com/api/apps/<id>/entities/*`)
   was aborted during full-page loads: it STAYS on its route rendering
   a SILENT ZERO-STATE — full shell, hero `0.0%` / `$0.00` / `✓ NET
   ZERO`, breakdown totals `$0.00`, items views `0 items · $0.00` with
   their STANDARD empty states, NO error surface at all (a transient
   network failure is visually indistinguishable from an empty budget).
   The clone BUMPED to `/login` — `boot()`'s single `catch` set
   `user: null` regardless of which stage failed, so an authenticated
   user with a dead data API was treated as logged out. Also measured:
   the reference's MUTATION failure (its Save with a dead API is a
   silent no-op — the dialog stays open with no toast/banner/error
   text; the clone's dialog + error-toast superset verified live: "Could
   not save the item / Network error — check your connection and try
   again"), its mid-session client-nav under a dead API (NO refetch —
   in-memory data renders, matching the clone's v15-pinned behavior),
   its session-probe failure (aborting its `auth/login` POST changes
   nothing — the platform cookie session carries the load), and the
   clone's toast duration (4000ms; the reference shows no toasts
   anywhere, v10 — no parity target).

8. **1 finding group** (`docs/remediation-plan-v16.md`): the G1
   boot data-failure rebuild (stay-in-app parity + the honest error
   toast).

9. **TDD RED → GREEN**: 3 new e2e specs
   (`tests/e2e/boot-failure.spec.ts`: stay-in-app + zero-state + URL,
   the one-shot error toast, the 401-probe redirect pin) — RED confirmed
   at the exact unfixed values (the login redirect fires after the URL
   assertions, so no "NET ZERO GOAL" renders; no toast exists), then
   GREEN after the 2-file fix (`store.ts` nested try + `bootError`
   flag/clear action, `app-shell.tsx` one-shot toast effect). One
   test-bug fix mid-flight (documented as SKILL lesson 34): Radix
   mirrors the toast text into a `role=status` live region whose
   concatenated text double-matches a loose `getByText` — the assertions
   need `{ exact: true }`.

10. **Full chain**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ ·
    **126/126 e2e** ✓ (first full run, no flakes) · 30/30 smoke ✓.

11. **Live parity re-verification**: a route-aborted reload on a fresh
    `clone18` session stays on `/` rendering the reference's zero-state
    (0.0% / $0.00 / ✓ NET ZERO) with the error toast caught live
    ("Could not load your data / Network error — check your connection
    and try again"); after unrouting, a clean reload recovers the seeded
    hero figure (`+$2065.00`).

12. **Screenshots**: all 15 regenerated — **zero pixel changes** (the
    fix is behavior-only: the failure branch never renders in the
    content-waiting shots; `git status` on `docs/screenshots/` is
    empty).

13. **Docs aligned**: README (counts 126, plan-v16 row), CLAUDE.md
    (counts, the boot-failure surface in the e2e pyramid, the v16
    e2e-contract note — the route-abort pattern + the live-region
    lesson), AGENTS.md (the v16 pin paragraph), SKILL (state 96/126/30,
    lesson 34, Appendix B row), the probe README (v16 catalog + the
    route-abort technique + the nested-quoting lesson), this log, and
    the worklogs.

## Suggested next steps

- The toast VISIBILITY model: the reference never toasts (v10); the
  clone's superset toasts are 4s-fixed — consider duration/stacking
  polish ONLY if a future audit surfaces drift in the surfaces around
  them (no parity target exists).
- The remaining honest-copy divergences (Google OAuth unavailable,
  forgot-password no-mail) are documented features, not drift —
  converting them into real integrations is a product decision, not a
  parity task.
- The error-state audit covered boot + mutations; a THIRD tier exists in
  the calculator's line-item flows (the parent recalculation response
  `{ lineItem, parentAmount }`) — same dialog-catch superset applies,
  low risk, verify on the next pass.
