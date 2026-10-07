# Session 15 — Fresh Verification & Parity Iteration v8

**Date:** 2026-10-08 · **Baseline:** `c6d40fa` (session-14 = session-13's
narrative record + the session prompt) · **Outcome:** 2 finding groups +
1 hygiene item fixed TDD-first — **96/96 unit · 92/92 e2e · 30/30 smoke**,
live parity re-verified.

## Baseline re-verification

Workspace was RESET this session — re-cloned `nordeim/zero-balance` fresh
into `/home/z/my-project/zero-balance`, re-created `.env`
(`DATABASE_URL="file:../db/custom.db"`), `db/` at the repo root, `db:push` +
`db:seed` (the sandbox still exports its polluting absolute `DATABASE_URL` —
the npm scripts' `env -u` discipline handled it untouched; the earlier
sessions' `with-server.sh` boot-per-command workaround turned out
unnecessary this time: a detached `(bun server.js &)` subshell survives
across tool calls, so ONE parity server on :3200 served the whole audit).
Read the full doc chain (AGENTS → CLAUDE → README → PAD → SKILL →
session_13 → plan v7 → worklog → session_14), spot-checked the structure
against the docs (7 routes, 14 budget components, 15 lib seams, 8 unit
files, 15 e2e specs, probe infrastructure), then ran the whole chain at
HEAD: **lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ · 83/83 e2e ✓ ·
30/30 smoke ✓** — the v7 baseline confirmed intact.

## The v8 audit — dialog footers + the badge family at computed-style depth

Two agent-browser sessions (`ref8` = live reference, `clone8` = the
standalone parity server on :3200). Fresh angles: the mobile-navigation
stack re-verified end-to-end (the task focus), then the surfaces v7 had not
measured at computed-value depth — every form dialog's **footer-button
geometry** and the item-card **badge family's computed colors**.

**Mobile nav verification (task focus):** R1 re-confirmed live — the ref's
toast container (`fixed top-0 z-[100] w-full`, h=32, `pointer-events:auto`)
still BLOCKS its hamburger's center point (the hit-test returns the
container, not the button); the clone's hit-test is DIRECT and its viewport
is `pointer-events: none`. R2 re-confirmed — tapping Income in the ref's
sheet changed the URL but left `sheetOpen: true` behind the overlay; the
clone's sheet closed. R4 re-confirmed — the ref scrolls to 395px on `/` and
464px on `/networth` at 390px; the clone fits exactly on all five routes.
Toggle/tbar/sheet chrome identical to the v7 pins (28×28 toggle, 16px
`rgb(10,10,10)` icon with shrink-0, 61px topbar, 288×844 sheet
`#fafafa` + 1px `#e5e5e5` + `rgba(0,0,0,0.8)` overlay).

**Findings ledger (2 groups + hygiene, `docs/remediation-plan-v8.md`):**

- **G1 [MED] dialog footers**: the reference renders every form dialog's
  footer as `flex gap-3 pt-4` with BOTH buttons at `flex-1` — Cancel ≈ 307px
  (left half of the 624px content row) + Save ≈ 305px (right half), h=36 —
  measured on its budget add/edit, asset, and line-item dialogs. The clone
  ran a right-aligned row of content-sized buttons (Cancel 81px / Save 127px,
  no pt-4). The dialog shells themselves matched exactly (672px, sticky 69px
  header, scrolling `p-6 space-y-6` form — the ref's edit form is 774px tall
  inside a 720px card, i.e. internally scrolled, same cap on the clone).
- **G2 [MED] remaining lab() drifts**: a computed-color sweep found the last
  named-palette classes on parity surfaces — `text-zinc-700` on the inactive
  nav links (ref `rgb(63,63,70)`), the full badge map family in
  `constants.ts` (frequency gray/blue/purple/indigo/pink, classification
  red/blue/green — all values verified identical to the ref's, e.g. monthly
  purple `rgb(250,245,255)/rgb(126,34,206)`, need red
  `rgb(254,242,242)/rgb(185,28,28)/rgb(254,202,202)`), the Recurring badge,
  the status badge, and the Calculate button (`rgb(234,88,12)` /
  `rgb(254,215,170)`). All hex-pinned.
- **G3 [LOW] hygiene**: `prisma/db/custom.db` was a session-1 stray tracked
  in git at the wrong path (nothing references it; the contract is
  `<repo>/db/custom.db`, gitignored) — untracked with `git rm --cached`.

**The instructive non-finding**: the clone renders a green "Recurring" card
badge its items showed and the reference's didn't — but flipping the
reference's own "Recurring Item" switch (in its edit dialog) made the same
green badge appear on its card (`rgb(21,128,61)`), and restoring the switch
removed it. The badge is CONDITIONAL on the item's recurring flag on both
sides; the difference was pure data (the reference's live items now ship
recurring=false — they rendered badges when the v2 recon measured the maps).
Render logic already matched; no code change (SKILL lesson 12.18).

Also verified MATCHING (no action): reference data state (unchanged since
session 11: 5000/1000/525 → +$3475.00, 30.5%), the full v7 login/404/head
pin set, calculator buttons (110/141px content-sized both sides), rail brand
+ geometry, active nav gradient, and the card chrome.

## TDD execution

13 spec assertions across 12 tests RED first: NEW `badge-colors.spec.ts`
(8 — computed values for need/want/savings/monthly/weekly/Recurring/active
badges + the Calculate button), +1 `nav-geometry` (inactive-link
`rgb(63,63,70)`), +3 extended `dialog-buttons` (footer container flex/gap
12px/pt 16px + Cancel/Save ≥ 300px on the budget, line-item, and asset
dialogs). Implementation across `budget-item-dialog.tsx`,
`line-item-dialog.tsx`, `asset-dialog.tsx`, `liability-dialog.tsx` (footer
→ `flex gap-3 pt-4` + `flex-1` on both buttons; the superset Delete link
keeps `mr-auto`), `constants.ts` (both badge maps hex-pinned),
`item-card.tsx` (Recurring/status badges + Edit/Calculate hovers),
`sidebar.tsx` (`text-[#3f3f46]`).

Mid-flight corrections: a JSX comment inside a ternary's parens is a parse
error (moved to `//` form); the items/constants specs pinned the old named
class STRINGS — updated to the hex forms with the computed-value pins now
carried by the new badge spec (stronger than class-name matching).

**92/92 e2e green** (83 + 9 net-new).

## Verification & docs

Full chain: lint · typecheck · **96/96 unit** · build · **92/92 e2e** ·
**30/30 smoke**. Live parity re-verified surface-by-surface on :3200 — the
budget dialog's footer now measures `flex`/gap 12px/pt 16px with **Cancel
307px + Save 305px** (the reference's exact numbers), the nav links compute
`rgb(63,63,70)` plain rgb, every badge computes the reference's exact rgb
values (need `rgb(254,242,242)/rgb(185,28,28)/rgb(254,202,202)` etc.), and
the Calculate button reads `rgb(234,88,12)` + `rgb(254,215,170)`. The mobile
stack re-verified end-to-end on the fixed build (toggle hit DIRECT, sheet
closes on nav, 390px fit on every route).

Screenshots: db re-seeded, full 13-shot catalog regenerated (5 shots carry
the new footer/badge rendering). `.env.example` verified to match the
codebase (3 vars — DATABASE_URL relative contract, NEXT_PUBLIC_SITE_URL,
AUTH_SECRET).

Docs aligned: README (counts 92, plan-v8 row), CLAUDE.md (counts), AGENTS.md
(v8 pin paragraph), SKILL (state 96/92/30, lessons 12.16–12.18, Appendix B
row), probe README (v8 catalog), this session log, and `worklog.md`.
