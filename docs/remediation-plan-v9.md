# Remediation Plan v9 — Session-17 Parity Iteration

> **Status: COMPLETE** — all 7 finding groups fixed TDD-first (10 new e2e
> tests + 4 updated pins, RED → GREEN); full chain green at 96 unit / 102
> e2e / 30 smoke; live parity re-verified surface-by-surface. Mid-flight
> discovery: v4's `space-y-*` emits margin-block-end on the first child —
> with the reference's INLINE labels that margin is ignored by layout (the
> v3 build applies margin-top to the following sibling) — pinned in
> `globals.css`. See `docs/session_17.md`.

Date: 2026-10-08 · Scope: fresh two-site re-audit after the v8 baseline
(`3d66178` + `92e837e`) re-verified green (lint · typecheck · 96/96 unit ·
build · 92/92 e2e · 30/30 smoke). Probes: `scripts/parity-probes/probe-v9-*.mjs`
via `run-probe.sh`, agent-browser sessions (`ref9`/`clone9` desktop 1280×800 +
390×844, `reflog9`/`clonelog9` fresh unauthenticated login sessions), the
detached standalone parity server on :3200.

This pass re-verified the entire mobile-navigation stack end-to-end (the task
focus) and then swept surfaces the earlier passes had not measured at
computed-style depth: the **donut chart's data-order convention**, every form
dialog's **X-close geometry + header height**, the **form-label line box**,
the **classification-tile text line-height**, the **shadcn primitive tokens
(radio/switch)**, the **Tailwind v4 `rounded-full` infinity drift**, and the
**login card's per-state control geometry**. It found **7 clone-side finding
groups**; no new reference bugs (R1–R7 all re-confirmed live — R1 toast-block,
R2 sheet-trap, R4 395px overflow, R5 no Escape/outside-click, R6 unconfirmed
deletes; reference data unchanged since session 11: income 5000 / savings 1000
/ expenses 525 → `+$3475.00`, 30.5%).

---

## Findings ledger

### G1. [MED] Donut chart: data order + label connector lines

Measured live on the reference dashboard (1280×800): its donut renders the
data **sorted by value DESCENDING** — today `[Need $6025.00 (92.3%), Savings
$300.00 (4.6%), Want $200.00 (3.1%)]` — identically in the pie sector DOM and
the legend rows, with the biggest slice anchored at the recharts default
start point (3-o'clock, counterclockwise sweep). The v2-era pin "[Savings,
Want, Need] sector fills" is the SAME convention with then-different data
(the $6025 slice was Savings-classified at v2 time; the reference's items
were re-classified since — its data drifts, its code doesn't). The clone
renders the fixed `[Savings, Want, Need]` order from
`spendingBreakdown()` (`src/lib/dashboard.ts:59`) in both the pie
(`dashboard-view.tsx:541`) and the legend — with the seed's data
(S 1250 / W 415 / N 7370) the two layouts are visually different: the
reference anchors its biggest (Need) slice at 3-o'clock with the small
slices just below it; the clone anchors Savings (13.8%) there.

Additionally the reference renders **no percentage-label connector lines**
(`labelLineCount: 0`) while the clone renders 3 recharts
`.recharts-pie-label-line` elements (one per labeled sector).

Fix: sort the slices by `amount` DESC in `SpendingBreakdownCard` (one sorted
array feeding BOTH the pie `data` and the legend rows — the aggregation
function's order stays the domain model) and pass `labelLine={false}` to the
`<Pie>`. Label style itself already matches (16px/400, sector fill,
`.toFixed(1)%`).

### G2. [MED] Dialog X-close geometry + sticky-header height (all dialogs)

Measured live on the reference's Add Budget Item AND calculator dialogs:
the X-close is a **36×36 button rendered as a flex child of the sticky
header** (`flex items-center justify-between border-b px-6 py-4`), svg 16px,
radius 6px, color `rgb(10,10,10)`, transparent bg — making the form-dialog
header **69px** (16 + 36 + 16 + 1). The clone's four form dialogs
(budget-item, line-item, asset, liability) render `DialogContent`'s default
**absolute 20×20** close (`svg h-5 w-5`, radius 4, outside the header) →
header **61px**. The calculator dialog already renders the 36×36 in-header X
(v6) but with a **20px icon** (reference: 16px).

Fix: new `DialogCloseButton` primitive in `ui/dialog.tsx` (36×36
`rounded-md`, `XIcon h-4 w-4`, `#0a0a0a`, `hover:bg-accent`,
`DialogPrimitive.Close`) rendered inside each form dialog's `DialogHeader`;
remove `DialogContent`'s default absolute X (+ the `hideClose` prop — the
calculator's own X stays, its icon → `h-4 w-4`).

### G3. [MED] Form-label line box → 12px label→control gap

The reference's field labels are the plain shadcn-v1 form:
`text-sm font-medium leading-none` on an **inline** element — computed rect
h 16 (14px text, inline glyph box), label-bottom → input-top **12px** with
the same `space-y-2` wrapper the clone uses. The clone's `Label` base adds
`flex items-center gap-2` (the v4-shadcn form) — display flex with
`leading-none` → rect h 14, gap **8px**. Visible in every field of every
form dialog. Fix: drop `flex items-center gap-2` from the `Label` base class
(the classification-tile Label already re-adds its own flex layout; no other
Label nests icons — grep-verified).

### G4. [LOW-MED] Classification-tile text line-height (56px vs 52px tiles)

The reference's tile text label computes **lh 14** (leading-none on the
14px text) inside its `p-4 border-2` flex tile → tile h **52**. The clone's
tile span is `text-sm font-medium` — v4's `text-sm` pairs with lh 20 → tile
h **56**. Fix: add `leading-none` to the tile span
(`budget-item-dialog.tsx:201`).

### G5. [MED] shadcn primitive tokens: radio + switch (the #171717 family)

- **Radio circle border**: reference `border-primary` computes
  `rgb(23,23,23)` (its `--primary` is the shadcn near-black #171717); the
  clone's `--color-primary` is deliberately the brand forest `#1a3a2e`
  (globals.css:51) → its radio circles render forest. Fix: hex-pin the
  radio (`border-[#171717] text-[#171717]`, `ring-1` focus — the reference
  uses `focus-visible:ring-1`, the clone `ring-2`).
- **Switch checked track**: reference `data-[state=checked]` bg = **
  rgb(23,23,23)** (flipped its own Recurring switch live, measured, then
  restored); the clone renders `bg-primary` forest. Fix:
  `data-[state=checked]:bg-[#171717]`.
- **Switch thumb**: reference `bg-background` → **#ffffff** (its
  `--background` is white) + `ring-0`; the clone's `--background` is the
  warm paper `#fafaf8` and it adds `ring-1 ring-border`. Fix: thumb →
  `bg-white` + `ring-0`.

### G6. [LOW-MED] Tailwind v4 `rounded-full` infinity drift (systematic)

Computed-radius census on both dashboards: the reference renders **9
elements at `9999px`** (avatar, hero progress track+fill, decorative
circles, tile dots); the clone renders the **same 8-9 surfaces at
`33554432px`** — v4's `rounded-full` emits `calc(infinity * 1px)` while the
reference's build emits `9999px`. Visually identical, but this is the exact
computed-style-drift class the v8 iteration eliminated for colors (lab()
→ hex pins); the doctrine is "computed styles are ground truth". Fix:
`rounded-full` → `rounded-[9999px]` across the 24 source sites (10 files:
app-shell, calculator-dialog, dashboard-view, item-card, login-card,
net-worth-view, sidebar, radio-group, switch).

### G7. [MED] Login card: primary-button font-size + per-state control heights

Measured live on the reference (fresh unauthenticated sessions, all three
card states):

| Surface | Reference | Clone |
|---|---|---|
| Primary button font-size (all states) | **14px/500** | 16px/500 |
| Sign-in button height (≥640px) | 48px ✓ | 48px ✓ |
| Sign-in inputs height (≥640px) | 48px ✓ | 48px ✓ |
| **Sign-up** button + inputs height | **44px** | 48px |
| **Forgot** button + input height | **44px** | 48px |

The reference's sign-in state uses taller controls (48) than its sign-up and
forgot states (44) — a real per-state geometry the clone flattens to 48
everywhere. The Google button (h54/fs16), heading family, links, and input
chrome already match (v7 pins). Withdrawn during validation: the card
border-color difference (`#e5e7eb` vs `#e5e7e3`) — BOTH cards render
`border-width: 0` (the color never paints; not a visual gap).

Fix: primary button gains `text-sm`; button + input heights become
mode-dependent (signin keeps `h-11 sm:h-12`; signup/forgot pin `h-11`).

### Verified matching this pass (no action)

Mobile navigation (task focus, both sites 390×844): toggle 28×28 at (24,16)
identical; **R1 re-confirmed live** — the ref's toast container (`fixed
top-0 z-[100]`, h32, w390, `pointer-events: auto`) still intercepts its
hamburger's center hit (elementFromPoint returns the container), the clone's
hit is DIRECT and its viewport `pe: none`; **R2 re-confirmed** — tapping
Income in the ref's sheet navigated but left the sheet+overlay trapping
(sheetStillOpen true), the clone's closed; **R4 re-confirmed** — the ref
scrolls to 395px on `/` at 390px, the clone fits 390; sheet chrome identical
(288×844 `#fafafa`, 1px `#e5e5e5`, `rgba(0,0,0,0.8)` overlay). Hero card
(632×316, 135deg forest gradient, 16px radius, p-32, full label family incl.
Under Budget `rgb(245,169,98)` 16px/600, allocation bar 12px h, 90deg orange
gradient, width ∝ allocation %). Stat cards identical (304×210, white,
`#e5e7e3` border, 16px radius, p-24, shadow `0 4px 20px rgba(0,0,0,0.06)`,
amounts 30px/700/`#1a3a2e`, chevrons 20px `#6b7280`). Budget Guidelines text
identical. Net-worth structure identical (summary/tabs/type groups/ratios).
Donut sector colors/stroke (`#fff` 1px)/size (200px r) + label style
identical. Dialog shells (672×720, sticky header, `p-6 space-y-6` form),
footers (v8 flex-1 split intact: Cancel 307 + Save 305), text/select/date
inputs (h36/w304/14px/`#e5e5e5`/r6), textarea (624×78), Select triggers,
recurring description (12px `#6b7280`), tile borders (2px, selected
`#e07a3b` + `#fff7f5` tint), switch geometry (36×20, thumb 16, translate 16).
Login: signin heading (30px/700/`#0f172a`/-0.75), card bg
`rgba(255,255,255,0.95)`, Google button (h54/368/16px), links (14px
`#64748b`), input chrome (`#e2e8f0` / `rgba(248,250,252,0.5)` / r12).
Reference data state unchanged (no drift).

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | G1 donut: value-desc sort + `labelLine={false}` | `dashboard.spec.ts`: fills → `[orange, lime, blue]`; legend rows → Need/Savings/Want with amounts+percentages; NEW: label-line count = 0 | `dashboard-view.tsx` |
| 2 | G2 dialog X + header: `DialogCloseButton` in 4 form headers, remove default absolute X, calculator icon 16px | `dialog-buttons.spec.ts`: NEW header h 69 + X 36×36/svg16 pins on the budget dialog; calculator X icon 16 | `ui/dialog.tsx`, 4 form dialogs, `calculator-dialog.tsx` |
| 3 | G3 Label line box | `dialog-buttons.spec.ts`: NEW label→input gap 12px pin (rect-based) | `ui/label.tsx` |
| 4 | G4 tile lh | `dialog-buttons.spec.ts`: NEW tile height 52 pin | `budget-item-dialog.tsx` |
| 5 | G5 radio/switch tokens | `tokens.spec.ts`: NEW radio border `rgb(23,23,23)`, switch checked bg + thumb `rgb(255,255,255)` pins | `ui/radio-group.tsx`, `ui/switch.tsx` |
| 6 | G6 rounded-[9999px] | `tokens.spec.ts`: NEW hero-bar + avatar radius `9999px` pins | 10 files (24 sites) |
| 7 | G7 login geometry | `login-parity.spec.ts`: NEW submit fs 14px; signup/forgot button+input h44 pins | `login-card.tsx` |
| 8 | Docs: session_17 log, worklog, README/AGENTS/CLAUDE/SKILL alignment + probe README v9 row | — | docs |
| 9 | Regression: full chain + live parity re-check of every fixed surface + screenshot refresh | — | — |

## Regression pin map (must NOT change)

- All six superset fixes (hamburger hit, sheet close-on-nav, root-URL nav
  highlight, no mobile overflow, Escape close, delete confirmations) — all
  re-verified live this pass on both sites
- v8 footer geometry (flex gap-3 pt-4, Cancel/Save ≥ 300px), the hex-pinned
  badge/nav/Calculate colors, dialog shells, field geometry incl. 624px
  full-row spans, outline-Cancel/gradient-Save colors + Save icons
- Money two-formatter contract, breakdown drill-down, donut sector
  colors/icons/label style, stat cards, hero states, per-surface add
  gradients, calculator server-side recalc, seed arithmetic, empty-state
  pattern, login v7 pin set (heading/card/google/links/input chrome)
- The v5 token block, `@variant hover` pin, tab grid, mobile toggle/sheet
  pins, custom 404, head metadata
- e2e fixture discipline: every spec restores what it mutates
