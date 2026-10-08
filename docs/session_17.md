# Session 17 — Fresh Verification & Parity Iteration v9

**Date:** 2026-10-08 · **Baseline:** `92e837e` (session-16 = session-15's
narrative record) · **Outcome:** 7 finding groups fixed TDD-first —
**96/96 unit · 102/102 e2e · 30/30 smoke**, live parity re-verified.

## Baseline re-verification

The workspace survived from session 15 (repo at `3d66178`, clean tree);
`git pull` fast-forwarded to `92e837e` (only `docs/session_16.md` — the
session-15 narration). Environment intact (`.env`
`DATABASE_URL="file:../db/custom.db"`, `db/custom.db`, node_modules). Doc
chain re-read (AGENTS → CLAUDE → README → PAD → SKILL → session_15 →
plan-v8 → worklog → session_16), structure spot-checked, then the full
chain at HEAD: **lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ · 92/92 e2e
✓ · 30/30 smoke ✓** — the v8 baseline confirmed intact. The detached
standalone parity server booted on :3200 (survives across tool calls);
agent-browser sessions `ref9`/`clone9` (desktop 1280×800) logged into both
sites (ref landed on `/` as documented; clone via demo@zerobalance.app).

## The v9 audit — the donut convention, dialog chrome, and primitive tokens

Fresh angles this pass (surfaces the earlier passes had not measured at
computed-style depth): the **donut's data-order convention**, every form
dialog's **X-close geometry + sticky-header height**, the **form-label
line box**, the **classification-tile text line-height**, the
**shadcn primitive tokens** (radio/switch), the **Tailwind v4
`rounded-full` computed radius**, and the **login card's per-state control
geometry** — plus the standard mobile-nav re-verification (the task focus)
and the reference data-drift check (unchanged: +$3475.00, 30.5%).

**Mobile nav verification (task focus):** R1 re-confirmed live — the ref's
toast container (`fixed top-0 z-[100]`, h32, w390, `pointer-events: auto`)
still intercepts its hamburger's center hit; the clone's hit is DIRECT with
a `pe: none` viewport. R2 re-confirmed — tapping Income in the ref's sheet
navigated but left `sheetStillOpen: true`; the clone's closed. R4
re-confirmed — the ref scrolls to 395px on `/` at 390px; the clone fits
390. Toggle 28×28 at (24,16), sheet 288×844 `#fafafa` + 1px `#e5e5e5` +
`rgba(0,0,0,0.8)` overlay — identical both sides.

**Findings ledger (7 groups, `docs/remediation-plan-v9.md`):**

- **G1 [MED] donut**: the reference renders its donut data **sorted by
  value DESC** — today `[Need $6025, Savings $300, Want $200]` in both the
  pie sector DOM and the legend, biggest slice anchored at recharts'
  3-o'clock start. The v2-era "[S, W, N]" pin was the SAME convention
  wearing that era's data (the $6025 slice was Savings-classified then —
  reference data drifts, its code doesn't). The clone used a fixed
  [S, W, N] order. ALSO: the ref renders NO percentage-label connector
  lines; the clone rendered 3 recharts label lines. Fixed: value-desc sort
  in `SpendingBreakdownCard` (pie + legend share the sorted array —
  the aggregation function keeps its domain order) + `labelLine={false}`.
- **G2 [MED] dialog X + header**: the ref's dialogs render a **36×36
  X-close as a flex child of the sticky header** (16px lucide-x, `rounded-md`,
  `#0a0a0a`) → header **69px**; measured on both its budget and calculator
  dialogs. The clone's form dialogs used `DialogContent`'s default absolute
  20×20 (svg 20, radius 4, outside the header) → header 61px; its
  calculator X was 36×36 but with a 20px icon. Fixed: new
  `DialogCloseButton` primitive wired into all four form dialogs' headers;
  the default absolute X and `hideClose` prop removed; calculator icon →
  16px.
- **G3 [MED] form-label line box**: the ref's labels are the plain
  shadcn-v1 form (`text-sm font-medium leading-none`, **inline**) — the
  inline glyph box (rect h 16) produces a **12px label→input rect gap**
  under the same `space-y-2` wrapper. The clone's v4-shadcn
  `flex items-center gap-2` label rendered h 14 / gap 8. **Mid-flight
  discovery**: after restoring the inline label, the gap COLLAPSED to 4 —
  v4 rewrote `space-y-*` from v3's margin-top-on-following-sibling to
  margin-block-end on `:not(:last-child)`, and vertical margins on INLINE
  boxes are ignored by layout. Fixed: the Label base class → the ref's
  form, PLUS a v3-semantics restoration for `.space-y-2` pinned in
  `globals.css` (trap 4b; all 43 usages audited safe — block children are
  equivalent under sibling collapse).
- **G4 [LOW-MED] tile line-height**: the ref's tile text computes lh 14 →
  tile h **52**; the clone's `text-sm` paired with v4's lh 20 → 56. Fixed:
  `leading-none` on the tile span.
- **G5 [MED] radio/switch primitive tokens**: the ref's `--primary` is
  shadcn's `#171717` — its radio borders, checked radio dot, and CHECKED
  switch track all measure `rgb(23,23,23)` (flipped its own Recurring
  switch live, measured, restored); its switch thumb is pure white with
  `ring-0`. The clone's `--color-primary` is deliberately brand forest
  `#1a3a2e`, so `border-primary`/`bg-primary` primitives rendered forest;
  its thumb was the warm paper `#fafaf8` with `ring-1`. Fixed: hex-pins on
  the primitives (radio border/dot/ring-1, switch checked track + white
  ring-0 thumb) instead of routing through the brand token.
- **G6 [LOW-MED] rounded-full infinity drift**: a computed-radius census
  found the SAME surfaces (avatar, hero progress track+fill, decorative
  circles, tile dots) rendering **9999px** on the ref and **33554432px**
  (`calc(infinity * 1px)`) on the clone — the v8 lab() doctrine in the
  radius dimension. Fixed: `rounded-full` → `rounded-[9999px]` across all
  24 source sites.
- **G7 [MED] login per-state geometry**: the ref's primary button text is
  **14px** in every state (the Google button is the 16px one), and its
  **sign-in** controls are 48px at ≥640px while its **sign-up/forgot**
  controls are **44px** (h-11) — a per-state geometry the clone flattened
  to 48. Fixed: `text-sm` + mode-dependent `sm:h-12` on the button and
  inputs. Withdrawn during validation: the login-card border-color
  difference (`#e5e7eb` vs `#e5e7e3`) — BOTH cards render `border-width: 0`
  (the color never paints).

Also verified MATCHING (no action): hero card + full label family +
allocation bar (width ∝ allocation %), stat cards (304×210 incl. shadow),
Budget Guidelines, net-worth structure, donut sector colors/stroke/size +
label style, dialog shells/footers (v8 flex-1 split intact:
Cancel 307 + Save 305)/text/select/date inputs/textarea/recurring row, tile
borders/tints, dialog descriptions, login v7 pin set (heading, card bg,
Google button, links, input chrome), reference data state.

## TDD execution

10 new e2e tests + 4 updated pins, RED first: the dashboard donut spec
rewritten (fills `[orange, lime, blue]`, legend `[Need, Savings, Want]`,
label-line count 0), four new `dialog chrome (v9)` tests (header 69 + X
36×36/svg16/r6, label gap 12 + inline display, tiles 52×197 with lh 14,
calculator X 36/16), three new `primitive chrome (v9)` token tests (radio
`#171717` + 9999px radius, the switch checked/unchecked/thumb with
`expect.poll` — an immediate `getComputedStyle` read races the
`transition-colors` animation and returns the pre-flip value, lesson 21 —
and the hero-bar/avatar 9999px radii), three new login geometry tests
(signin 48/14 regression + signup/forgot 44/14). Two pre-existing specs
that pinned the old `rounded-full` class strings (auth logo chip, the
empty-states icon circles) were updated to the `rounded-[9999px]` form.

**102/102 e2e green** (92 + 10 net-new). One environment hiccup: four live
agent-browser sessions + Playwright's own Chromium crashed the first full
run ("Target crashed") — closing the fresh login sessions freed it.

## Verification & docs

Full chain: lint · typecheck · **96/96 unit** · build · **102/102 e2e** ·
**30/30 smoke**. Live parity re-verified on the fixed build surface by
surface: the donut renders `[orange, lime, blue]` with the biggest slice
anchored at 3-o'clock and **0 label lines** (was 3); the budget dialog's
header measures **69px** with the X at **36×36/svg 16/radius 6/#0a0a0a**
in the header; the Amount label sits **12px** above its input (inline
display, mb 0); tiles are **52×197**; the switch's checked track computes
**rgb(23,23,23)** with a **white** ring-0 thumb and 9999px track radius;
the radio border is `rgb(23,23,23)`; the legend order is
`[Need $7370.00, Savings $1250.00, Want $415.00]`; the avatar + hero bar
compute **9999px** with **zero** infinity-radius elements left on the
page; the login card computes **14px** button text with **48/48** signin
and **44/44** signup/forgot controls. Mobile stack re-verified end-to-end
on the fixed build (toggle hit DIRECT, sheet closes on nav, 390px fit).

Screenshots: db re-seeded, all 13 shots regenerated on the fixed build.
`.env.example` verified to match the codebase (3 vars — DATABASE_URL
relative contract, NEXT_PUBLIC_SITE_URL, AUTH_SECRET).

Docs aligned: README (counts 102 + plan-v9 row), CLAUDE.md (counts),
AGENTS.md (v9 pin paragraph), SKILL (state 96/102/30, lessons 12.19–12.23,
Appendix B row), probe README (v9 catalog), this session log, and
`worklog.md`.
