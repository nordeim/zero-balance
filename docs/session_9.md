# Session 9 — Fresh Verification & Parity Iteration v5

**Date:** 2026-10-07 · **Scope:** workspace refresh (`git pull` → `e23d854`, session-8 = session-7's narrative record), docs re-validation, full-chain re-verification, a deeper two-site parity audit (desktop 1280×800 + intermediate widths 640/768/820/1024 + mobile 390×844) and remediation v5 · **Outcome:** 10 finding groups fixed TDD-first (13 new e2e specs), full chain green (96 unit / 65 e2e / 30 smoke), live parity re-verified surface-by-surface, pushed to `main`.

## Where this session started

Session 7 had completed remediation v4 and pushed `28ad5fc`; `e23d854`
added its raw narrative (`docs/session_8.md`). This session treated that
as the baseline: docs review (AGENTS / CLAUDE / README / PAD / SKILL /
session_7 / session_8 / remediation-plan-v4 / worklog), a codebase
validation (13 route files / 21 handlers, `.env` → `file:../db/custom.db`,
db at repo root, the v4 fixes live in `sidebar.tsx` / `net-worth-view.tsx`
/ `app-shell.tsx` / `items-view.tsx`), and the full chain from scratch —
**typecheck ✓ · lint ✓ · 96/96 unit ✓ · build ✓ · 52/52 e2e ✓ · 30/30
smoke ✓** — before touching anything.

## The fresh audit — deeper than geometry

Probe scripts: `scripts/parity-probes/probe-v5-*.mjs` (+ the shared
`run-probe.sh` runner; sources passed via `eval(atob(...))`). This pass
went past the previous geometry/leaf audits to the reference's OWN token
layer: reading its `:root` CSS variables directly, sweeping for
inherited-color text nodes, comparing dialog action buttons, dropdown and
select item states, focus rings, hover-variant semantics, and the full
responsive chrome map (640 → 1280).

Confirmed matching (no action): page title; nav geometry, resting text,
rail divider; guidelines card + leaves; donut sectors/labels/legend;
quick actions; breakdown buttons; stat cards; money formats; dialog
panels/inputs/tiles; calculator banner/headings; add-button gradients;
responsive chrome at every width; mobile sheet geometry + all superset
fixes; both prior reference mobile-nav bugs and both overflow bugs
re-confirmed live (R1–R4).

## Ten finding groups — `docs/remediation-plan-v5.md`

1. **G1 [MED]** Neutral foreground family: the clone used zinc-ish
   `#3f3f3f` where the reference's own `:root` ships shadcn neutrals —
   foreground `#0a0a0a`, accent-foreground/secondary-foreground
   `#171717`, sidebar-foreground `#3f3f46`. Rendered on select-trigger
   text, dialog labels, menu items, select options (all measured
   `rgb(10,10,10)` on the reference vs `rgb(63,63,63)` on the clone).
2. **G2 [MED]** Form-control borders: reference `--input` = `#e5e5e5`
   on every trigger/input/menu/select-content border; the clone routed
   them through `#e5e7e3` (which is ONLY the reference's CARD border —
   kept as `--color-border` on purpose).
3. **G3 [MED]** Net-worth tabs: the reference renders a
   `grid w-full max-w-md grid-cols-2` list (448px, 220px triggers) with
   a green active state (`#dcfce7` bg, `#14532d` text); the clone had a
   168px inline-flex pill with `bg-white text-foreground` active and a
   margin-collapsed 16px gap (reference: 24px via content `mt-6`).
4. **G4 [MED]** Dialog action buttons: reference Cancel = shadcn
   OUTLINE (white, 1px `#e5e5e5`, `#0a0a0a` text, 6px, 500); Save Item /
   Save Asset = the forest→lime gradient; Save Liability and the
   LINE-ITEM dialog's Save Item = the ORANGE gradient; "Add First Item"
   = outline. The clone rendered ghost Cancellations and solid-lime
   `.zb-btn-primary` Saves everywhere (removed the primitive).
5. **G5 [MED]** Accent pair: reference accent = `#f5f5f5` with
   accent-foreground `#171717` (menu hover, select highlight); the clone
   had `#f0f2ee` + forest.
6. **G6 [MED]** Nav hover text: reference zinc-900 `#18181b`
   (sidebar-accent-foreground) vs clone forest — same class, different
   token.
7. **G7 [MED]** Tailwind v4 media-gates `hover:` variants behind
   `@media (hover: hover)` — on `hover: none` devices the reference
   (v3 engine) still shows its tints while the clone showed none
   (measured transparent). Fixed with the `@variant hover (&:hover)`
   pin — v3 semantics on every device.
8. **G8 [LOW]** muted/secondary `#f4f4f5` → `#f5f5f5` (TabsList bg).
9. **G9 [LOW]** v4 emits named palette utilities as `lab()`/`oklab()` —
   menu Delete (`#dc2626`), calculator hint (`#ea580c`), and the
   white-alpha hero/net-worth labels (`rgba(255,255,255,.6/.7/.8)`)
   now pinned with arbitrary hex classes / inline rgba.
10. **G10 [LOW]** Focus rings: reference ring `#0a0a0a` (inputs) and
    sidebar-ring `#3b82f6` (nav) vs the clone's forest on both.

**Two new reference bugs documented (superset ledger):**
- **R5** — the reference's dialogs do NOT close on Escape (plain fixed
  overlays, no `data-state`, no keyboard dismissal; verified with focus
  inside on the budget-item and line-item dialogs). The clone's Radix
  dialogs close on Escape — now PINNED by a spec.
- **R6** — the reference's card-menu Delete destroys the item
  IMMEDIATELY (verified live — the Salary item vanished on click and was
  restored with identical data). The clone confirms first.

## TDD execution

New/extended specs, all verified RED before implementing (13 total):

- NEW `tests/e2e/tokens.spec.ts` (6): trigger text+border, menu
  hover+Delete red+content border, select highlight pair, nav hover
  tint+text, focus rings (input near-black + nav blue), hero
  white-alpha computed forms.
- NEW `tests/e2e/dialog-buttons.spec.ts` (4): budget dialog pair
  (outline Cancel + forest gradient Save), calculator empty state +
  orange hint + orange-gradient line-item Save, asset dialog pair,
  dialogs-close-on-Escape (the R5 superset pin).
- `tests/e2e/networth.spec.ts` +2: the tab list grid geometry + green
  active state; summary-label computed rgba.
- `tests/e2e/mobile-navigation.spec.ts` +1: the nav hover tint applies
  under `hover: none` emulation (the G7 pin).
- Updated `nav-geometry.spec.ts` (the hover class is now the
  arbitrary-hex form) and `calculator.spec.ts` (the hint asserts the
  computed color).

Implementation: the token block in `globals.css` (one comment-documented
`@theme inline` rewrite + `@variant hover` + popover-foreground note),
`tabs.tsx` + `net-worth-view.tsx` (the reference tab structure with
pinned hex + the 24px gap via `mt-6`), the four dialog footers (Button
`variant="outline"` Cancellations; `.zb-btn-add` Saves with the
surface's `ADD_BUTTON_GRADIENTS` inline — `.zb-btn-primary` removed),
`button.tsx` outline bg → white (the reference's `--background` token is
white; the clone's doubles as the warm page bg), popover content borders
→ `border-input`, `sidebar.tsx` (arbitrary-hex hover tint +
`focus-visible:ring-sidebar-ring`), `item-card.tsx` /
`calculator-dialog.tsx` (arbitrary-hex red/orange), and the white-alpha
labels in `dashboard-view.tsx` / `net-worth-view.tsx` (inline rgba).

Three infra gotchas re-learned (now in AGENTS.md / the SKILL D-table):
(D-7) the item-view pages are prerendered with an empty store — the
header AND empty-state "Add …" buttons coexist until hydration, so
role-based clicks need a seeded-card settle first (a latent race the
existing items.spec round-trip also carried — hardened); (D-6) the
hover-variant media gate; (D-8) the lab/oklab computed drift. And the
`:3200` parity server restart must kill by the `ss` PID — `lsof` never
lists the next-server LISTEN socket, so a "kill by port" via lsof
silently misses it and the new server dies on EADDRINUSE.

## Verification

- Full chain: typecheck ✓ · lint ✓ · **96/96 unit** ✓ · build ✓ ·
  **65/65 e2e** (52 prior + 13 new) ✓ · **30/30 smoke** ✓.
- Live parity re-verified on the remediated build, side by side:
  select trigger `rgb(10,10,10)`/`rgb(229,229,229)`; nav hover
  `rgb(240,253,244)` + `rgb(24,24,27)`; net-worth tabs 448px grid,
  220px triggers, 24px gap, active `rgb(20,83,45)` on `rgb(220,252,231)`;
  dialog Cancellations outline + all four Save gradients exact; menu
  hover `rgb(245,245,245)`/`rgb(23,23,23)` + Delete `rgb(220,38,38)`;
  select highlight pair; search-input ring `rgb(10,10,10)`; calculator
  hint `rgb(234,88,12)`; hero/net-worth labels plain rgba; the nav tint
  applies under `hover: none`; all mobile superset fixes re-verified
  (hamburger hit, sheet close-on-nav, 390px fit on every view).
- Screenshot catalog regenerated (12 shots) on the remediated build.

## Docs alignment

README (superset list → six entries + R5/R6, test counts 96/65, v5 plan
row), CLAUDE.md (counts, prerender-race contract, hover pin),
AGENTS.md (six pinned supersets, the neutral-token map, the two new
v4 traps, the prerender/settle conventions), SKILL (project_state
96/65, D-6/D-7/D-8 rows), `remediation-plan-v5.md`, this session log,
and `worklog.md`.
