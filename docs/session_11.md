# Session 11 — Fresh Verification & Parity Iteration v6

**Date:** 2026-10-07 · **Scope:** workspace refresh (`git pull` → `bd2e4be`, session-10 = session-9's narrative record), docs re-validation, full-chain re-verification, a fresh two-site parity audit covering surfaces v2–v5 had NOT touched (net-worth CARDS + their action menus, every dialog's EDIT variant, the calculator's populated rows, ALL empty states, wide-viewport geometry, sidebar bottom, toast container, overlay dismissal) and remediation v6 · **Outcome:** 14 finding groups fixed TDD-first (8 new e2e specs), full chain green (96 unit / 73 e2e / 30 smoke), live parity re-verified surface-by-surface, pushed to `main`.

## Where this session started

Session 9 had shipped remediation v5 (`db757a2`); `bd2e4be` added its raw
narrative (`docs/session_10.md`). This session treated that as the baseline:
docs review (AGENTS / CLAUDE / README / PAD / SKILL / session_9 /
remediation-plan-v5 / worklog / session_10), codebase validation (the v5
token block, `.zb-btn-primary` removal, tab grid, outline Cancellations all
live; 13 route files / 21 handlers; `.env` → `file:../db/custom.db`; seed
canonical), and the full chain from scratch — **typecheck ✓ · lint ✓ · 96/96
unit ✓ · build ✓ · 65/65 e2e ✓ · 30/30 smoke ✓** — before touching anything.

## Environment shift — a new sandbox gotcha (D-9)

The parity server could no longer survive between shell commands: this
sandbox reaps EVERY background process at command exit (setsid, nohup and
disown all die with the command), and the standalone server additionally
CRASHES under `node` on the first API request (the e2e/smoke paths always
used `bun`). Fix: `scripts/parity-probes/with-server.sh` — boots
`bun .next/standalone/server.js` on :3200 (0.0.0.0), waits for
`/api/health`, runs the requested command, tears down. Read-only DOM probes
still work serverless once a page is loaded (the browser sessions persist).

## The fresh audit — surfaces v2–v5 never touched

Probe scripts: `scripts/parity-probes/probe-v6-*.mjs`. This pass audited the
net-worth individual asset/liability CARDS (chrome, hover actions, menus,
edit dialogs), the EDIT variants of every dialog (prefill, disabled fields,
grid spans), the calculator's POPULATED line-item rows, every EMPTY state on
both sites (including filter-to-zero and a delete/restore dance on the
reference's only asset), wide-viewport content geometry (1440/1920), the
sidebar bottom area, the reference's toast container, and
overlay/outside-click dismissal.

Also discovered: **the reference's live DATA has changed since the session-1
recon** (now income $5000 / savings $1000 / expenses $525 — 1/1/3 items,
expenses Investments/Netflix/Rent, one asset, no liabilities). The clone
keeps its own recon-time seed (pinned by the test suites); the parity
convention remains structure + chrome with each side's own data. All
reference data this session touched (a test line item, the Savings Account
asset, a recalculated Investments category) was restored and verified live.

## Fourteen finding groups — `docs/remediation-plan-v6.md`

1. **G1 [MED]** Card action menus carried Pencil/Trash icons; the reference
   renders PLAIN-TEXT Edit/Delete (zero SVGs, text at the item's left
   padding). Fixed in `item-card.tsx` + both `net-worth-view.tsx` menus.
2. **G2 [LOW]** Net-worth menu Delete used named `text-red-600` → `lab()`
   computed; pinned to `text-[#dc2626]` (the v5 convention).
3. **G3 [MED]** All four dialog Save buttons were missing the lucide Save
   icon the reference renders (16px, before the label). Added (the saving
   spinner replaces it while pending).
4. **G4 [MED]** Asset + liability dialogs: Name and Last Updated must span
   the full 624px row (`md:col-span-2`, measured on the reference's asset
   AND Add Liability dialogs); the clone packed them into half-width cells.
5. **G5 [MED]** The Asset/Liability Type select must be DISABLED while
   editing (reference behavior; enabled on create) — the budget-item dialog
   already did this, the asset/liability dialogs didn't.
6. **G6 [MED]** Net-worth empty states: the reference renders a BARE lucide
   icon (`w-16 h-16 mx-auto mb-4 opacity-20` in `#0a0a0a` —
   circle-arrow-up for assets, circle-arrow-down for liabilities) inside
   the `bg-white rounded-2xl` bordered card — NOT the clone's tinted circle
   + TrendingUp/CreditCard; heading `mb-2`; description `text-base`.
7. **G7 [LOW]** Calculator empty-state icon color: forestDark → `#0a0a0a`.
8. **G8 [LOW]** Line-item dialog placeholders: Payment Method → "e.g.,
   Direct Debit, Credit Card"; Notes → "Additional details about this
   item..." (measured on the reference).
9. **G9 [MED]** Calculator line-item row actions must be ALWAYS VISIBLE —
   the reference renders them at opacity 1 at rest; the clone hid them
   behind row hover.
10. **G10 [LOW]** Row action icons: 14px gray → 16px near-black (edit) /
    red (delete), matching the reference's measured geometry.
11. **G11 [LOW]** statusPill named classes → arbitrary hex pairs
    (green `#f0fdf4`/`#15803d`, yellow `#fefce0`/`#a16207`, gray
    `#f9fafb`/`#374151`).
12. **G12 [MED]** Items-view empty states must be BARE — no white card, no
    circle: `text-center py-16` directly on the page, bare wallet /
    piggy-bank / receipt icon (near-black, 64px, opacity-20), heading
    `mb-2`, 16px description (measured via filter-to-zero on all three
    views).
13. **G13 [MED]** Content column: the reference wraps `max-w-7xl mx-auto`
    INSIDE `min-h-screen p-4 md:p-8` (padding OUTSIDE the 1280px cap) — at
    ≥1568px viewports the clone's column was 64px narrower (1216 vs 1280,
    measured at 1920). Fixed in all three views.
14. **G14 [LOW]** The card action triggers were missing the reference's
    `hover:text-accent-foreground`.

**New reference bug documented (R7):** its dialogs ALSO ignore
outside-click — a real mouse click on the overlay corner leaves the dialog
open; only X/Cancel close it (consistent with R5's no-Escape). The clone's
Radix dialogs close on both — superset behaviors, kept. Re-confirmed live:
R1 (toast container still covers the mobile hamburger), R5, R6 (extended —
its calculator row Delete is also instant).

## TDD execution

New/extended specs, all verified RED before implementing (8 new tests):

- NEW `tests/e2e/empty-states.spec.ts` (3): the bare items-view empty state
  (filter-to-zero); the net-worth liabilities empty state via an API
  delete/restore fixture dance (re-created in reverse capture order to
  preserve `createdAt` ordering — D-10); the content column at 1920/1280.
- `tests/e2e/dialog-buttons.spec.ts` +1: every Save button carries the
  Save icon (all four dialogs in one flow).
- `tests/e2e/networth.spec.ts` +2: the asset + liability dialog grid spans
  (304/624px with col-span-2); the Type select disabled on edit +
  enabled on create.
- `tests/e2e/tokens.spec.ts` +1: plain-text menu items (0 svgs) on income
  AND net-worth menus, Delete `rgb(220,38,38)` on both, trigger
  `hover:text-accent-foreground`.
- `tests/e2e/calculator.spec.ts` +1: empty-icon color, the two placeholders,
  always-visible row actions (32px/16px/near-black/red), status-pill hex —
  through a real line-item create + delete round-trip.

Three spec-side corrections during the RED→GREEN loop (all
implementation-neutral): Tailwind preflight makes `border-style: solid` even
at 0px width (assert width, not style); the net-worth empty card carries
`bg-white rounded-2xl` on the SAME div as `py-16 text-center` (measured);
and the liabilities count lives inside its tab panel (click the tab after
reloading the restored fixture).

## Verification

- Full chain: typecheck ✓ · lint ✓ · **96/96 unit** ✓ · build ✓ ·
  **73/73 e2e** (65 prior + 8 new) ✓ · **30/30 smoke** ✓.
- Live parity re-verified on the remediated build, surface by surface:
  income + net-worth menus (0 svgs, Edit `rgb(10,10,10)`, Delete
  `rgb(220,38,38)`); trigger hover class; the asset edit dialog (Save icon
  with the reference's exact path, Type disabled, Name/Last-Updated 624px);
  the calculator empty icon (`rgb(10,10,10)`, 48px, 0.2, mb-3); the
  line-item placeholders; the populated row (buttons opacity 1, 32px,
  16px icons, near-black/red, pills `rgb(240,253,244)`/`rgb(21,128,61)`);
  the bare items-view empty state (wallet icon 64px near-black, mb-4,
  heading 8px, desc 16px); the 1280px content column at 1920 (live on
  /income; all three views pinned by spec). The 12-shot screenshot catalog
  regenerated on the remediated build.

## Docs alignment

README (superset #5/#6 wording, counts 96/73, plan-v6 row), CLAUDE.md
(counts, the fixture-order restore contract), AGENTS.md (the v6 parity
pin paragraph, the fixture-order rule, superset #5 wording), SKILL
(project_state 96/73, D-9/D-10 rows), `docs/remediation-plan-v6.md`,
this session log, and `worklog.md`.
