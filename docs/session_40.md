# Session 40 — Fresh verification & parity iteration v20

> Continuation note: `docs/session_39.md` holds the incoming session-37
> conversation summary (the record this session was briefed to review),
> so this work session's formal log lives here. Work-session numbering
> continues the odd convention: 15 → 17 → 19 → 21 → 23 → 25 → 27 → 29 →
> 31 → 33 → 35 → 37 → 39 (this session), iteration v19 → **v20**.

Date: 2026-10-09 · Baseline: `365f2a4` (v19 code `d3528fd`, all green) ·
Plan: `docs/remediation-plan-v20.md` · Outcome: **2 finding groups fixed
TDD-first — (G1) the items-view header row's mobile geometry (the base
`items-start` that keeps the Add button auto-width at 390px + the `mb-8`
32px header→filter gap at both viewports) and (G2) the budget-item
dialog's classification tiles' 16px lucide icons (circle-alert / heart /
piggy-bank in the per-classification accents); 2 new e2e specs, RED →
GREEN both; the pass's fresh verification layer — the MOBILE-APP-VIEW +
POPULATED-EDIT-DIALOG VLM sweep (the session-38 log's two top
suggestions) + the breakdown drill-down; 96 unit · 137 e2e · 30 smoke
all green; live parity re-verified (all G1/G2 measurements match
exactly; the post-fix mobile income pair passes the VLM comparison
IDENTICAL); 5 of 15 screenshots changed (the three items-view shots +
the two dialog shots — exactly the fix scope).**

## What happened

1. **Workspace rebuilt from scratch (the sandbox had been reset):** the
   repo re-cloned at `365f2a4` (`git clone https://github.com/nordeim/
   zero-balance.git`), `npm install` run, `.env` re-created with
   `DATABASE_URL="file:../db/custom.db"`, `db/` at the repo root via
   `npm run db:push` + `npm run db:seed` (demo workspace: 7 budget
   items, 3 assets, 2 liabilities). All standing brief requirements
   re-verified: the Vitest + Playwright configs intact in the repo
   (96 unit / 135 e2e / 30 smoke baseline), the DB at the repo-root
   `db/` folder, the `.env.example` current. Full doc chain re-read
   (AGENTS, CLAUDE, README, PAD, SKILL, session_38/39,
   remediation-plan-v19, worklog); the scandihaven pattern repo
   re-cloned and re-checked (current at `d4789c3`; its integer-money /
   Radix / CSS-first-token / honest-copy patterns already reflected in
   this codebase).

2. **Baseline chain at `365f2a4` fully green, first full run, no
   flakes**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ · 135/135 e2e
   ✓ · 30/30 smoke ✓.

3. **Code audit (skills: code-review-and-audit, native CLI fallback).**
   Phase 1/4 green; Phase 2: `npm audit` = 5 high, all the dev-only
   ESLint `braces` chain (GHSA-vfj7-8cjw-p6xm, no patched release —
   accepted, unchanged advisory); secret-pattern scan clean (only the
   documented demo seed password). Phase 3: the pulled v19 changeset
   re-verified in the code before the audit work began (the fixed
   recurring row in `budget-item-dialog.tsx` + the v19 pin spec).

4. **Audit infrastructure**: agent-browser sessions `ref22`/`clone22`
   (desktop 1280×800, resized to 390×844 per check), both sites logged
   in (the reference with the brief's credentials; the clone with the
   seeded demo user inside one `with-server.sh` invocation), the :3200
   parity server booted per command through `scripts/with-server.sh`.

5. **Data drift check clean (fourteenth consecutive)**: reference
   unchanged since session 19 (allocation 30.5%, income `$5000.00`/1
   item, savings `$1000.00`/1 item, expenses `$525.00`/4 items, Balance
   `$3475.00`). The census probe needed a rewrite this pass: the v19
   file's literal "·" separator is mangled by the base64→`atob`→`eval`
   transport (C2 B7 decodes as two Latin-1 chars, so the regex never
   matched — the v19 session's "mid-pass fix" root-caused);
   `probe-census-v20.mjs` builds the separator from
   `String.fromCharCode(0xb7)` (ASCII-only source, transport-proof).

6. **Mobile navigation (task focus) re-verified end-to-end**: R1
   re-confirmed live (the ref's TWO toast containers intercept the
   burger's center hit at (38,30) — the bug manifesting live; the
   synthetic-event dispatch needed to drive the reference's own burger.
   The clone's hit is DIRECT on the svg; burger 28×28 at (24,16) both).
   R2 re-confirmed via the new one-eval probe (tapping Income in the
   ref's sheet navigated to `/income` with `sheetStillOpen: true` +
   overlay 1; the clone's sheet CLOSED + 390px fit + `/income`; sheet
   288px + Income link (20,185) 247×32 identical). R3 re-confirmed (no
   ref link active on `/` — all five rail links `rgb(63,63,70)`/400, no
   `<nav>` landmark; the clone highlights Dashboard — white + gradient
   + 500 + landmark). R4 re-confirmed (ref scrollWidth 395 on `/` +
   `/dashboard`, 464 on `/networth`; clone 390 on ALL six routes). The
   Tailwind v4 pins hold — the clone's mobile menu works as expected.

7. **Fresh surfaces — the mobile-app-view + populated-edit-dialog VLM
   sweep** (the session-38 log's two top suggestions, run through
   `z-ai vision` with the established layout-focused prompt +
   DOM-verification of every flag):
   - **Mobile views (5 × 2 sites at 390×844):** the dashboard IDENTICAL
     (its header row already carries the reference pattern). The three
     items views flagged the Add button — **REAL DRIFT (G1)**,
     DOM-verified: the reference's header row runs base `items-start`
     (the Add button stays auto-width: 147/155/150px) + `mb-8` (a 32px
     header→filter gap); the clone's bare `flex-col` stretched the
     button to 358px full-width and its `mb-6` rendered a 24px gap — at
     BOTH viewports (desktop nextTop 116 vs 124). The networth flags
     all decomposed into the documented superset fix #4 (the
     reference's own 464px overflow: its fixed 48px `text-5xl` figure,
     its 2-col summary grid, its Add button half off-screen) plus ONE
     hallucination refuted by measurement (the "pronounced green" tab
     tint — identical `rgb(220,252,231)` both).
   - **Populated edit dialogs (both sites at 1280×800):** the VLM
     flagged the classification radios as carrying icons — **REAL DRIFT
     (G2)**, DOM-verified in BOTH the reference's Add and Edit dialog
     states: the tile labels carry 16px lucide icons between the radio
     and the text, colored by the per-classification accent (need →
     circle-alert `rgb(224,122,59)`, want → heart `rgb(59,126,161)`,
     savings → piggy-bank `rgb(143,188,63)` — the same family the
     donut legend renders; the v19 empty-dialog sweep missed them at
     full-page scale). The VLM's other flags refuted in the DOM (the
     X-close "boxed" — identical 36×36/0px/transparent/16px svg both;
     the subcategory-subtitle and payment-method card claims —
     data-driven: the reference's own Netflix card renders its
     "Streaming" subcategory identically and its items carry no
     payment-method values).
   - **Breakdown drill-down (expanded Income + Salary): clean** — the
     only flags are the known superset #3 active-nav + the avatar
     letter (data). The badge-wrap mechanism verified identical
     (`flex flex-wrap gap-2 mb-3` both sides; the clone's wrap is
     data-driven — its seed carries 4 badges vs the reference's 2).

8. **2 finding groups** (`docs/remediation-plan-v20.md` G1, G2) — the
   plan written, validated against the codebase, then executed.

9. **TDD RED → GREEN (G1)**: 1 new e2e test in
   `tests/e2e/mobile-layout.spec.ts` ("the items-view Add button is
   auto-width and the header gap is 32px (v20 G1)") — RED confirmed at
   the exact unfixed state (btnW 358 vs < 200), GREEN after the
   one-line fix (`items-view.tsx`: the row's class aligned to the
   reference's — base `items-start` + `mb-8`, `justify-between` +
   `gap-4` kept).

10. **TDD RED → GREEN (G2)**: 1 new e2e test in
    `tests/e2e/dialog-buttons.spec.ts` ("classification tiles carry the
    reference's 16px lucide icons (v20 G2)") — RED confirmed (svg count
    0), GREEN after the fix (`budget-item-dialog.tsx`: the
    `CLASSIFICATION_ICONS` map + the icon rendered between the
    RadioGroupItem and the label span at `h-4 w-4` with the inline tile
    accent color). The v9 tile-geometry pins re-ran green untouched
    (the icon is height-neutral: 16px = the radio's height; the tiles
    stay 197×52).

11. **Full chain**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ ·
    **137/137 e2e** ✓ (135 + 2 new, first full run, no flakes) · 30/30
    smoke ✓.

12. **Live parity re-verification**: fresh paired measurements of both
    fixed surfaces on both sites — G1: the clone's button now 147×36 at
    (16,153) with the 32px gap (rowBottom 189 → nextTop 221 — every
    value identical to the reference's); G2: the icons now
    circle-alert/heart/piggy-bank at 16px in the exact measured colors
    (rgb(224,122,59)/rgb(59,126,161)/rgb(143,188,63)), the tile
    geometry preserved. The post-fix mobile income screenshot pair
    passes the VLM comparison IDENTICAL; the post-fix edit-dialog
    pair's remaining flags are data states (different items being
    edited: radio/switch positions) + the twice-DOM-refuted X-close
    misread.

13. **Screenshots**: all 15 regenerated — **five changed** (03-income,
    04-expenses, 05-savings — the G1 gap/button; 07-add-item-modal +
    08-calculator — the G2 icons and the shifted expenses page behind
    it; every other shot pixel-stable, including the dashboard whose
    header row already matched).

14. **Docs aligned**: README (counts 137, plan-v20 row), CLAUDE.md
    (counts + the two v20 pins in the e2e pyramid), AGENTS.md (the v20
    pin paragraph + the probe-transport lesson), SKILL (state
    96/137/30, lesson 38 — the base64→atob UTF-8 mangling + the
    superset-decomposition lesson, Appendix B row), the probe README
    (v20 catalog: the census transport fix, the R2 one-eval probe, the
    header/gap/nw/badge/drilldown probes, the VLM wrapper), this log,
    and the worklog.

## Suggested next steps

- The VLM sweep now covers auth (v19), app views desktop + mobile
  (v19/v20), the empty + populated dialogs (v19/v20), and the
  drill-down (v20). Good next surfaces: the CALCULATOR's populated
  state (multiple line items + the nested line-item dialog), the
  MOBILE sheet's open state under the VLM (its geometry is pinned but
  never visually diffed), and the net-worth EDIT dialogs (populated
  asset/liability forms — this pass only read their empty states).
- The register POST-SUCCESS landing and the logout headless path —
  the two remaining unmeasured auth flows (session-38's "new surface
  class" candidates).
- A keyboard-navigation sweep (Tab order + focus visibility across the
  main surfaces) — the a11y-superset class this project has never
  systematically swept.
