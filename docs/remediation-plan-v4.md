# Remediation Plan v4 — Session-7 Parity Iteration

Date: 2026-10-07 · Scope: fresh two-site re-audit of every surface against
the live reference (`https://zero-balance-4885a8f3.base44.app/`) at desktop
1280×800 and mobile 390×844, after the v3 remediation baseline
(`a037acc`) re-verified green (typecheck · lint · 96/96 unit · build ·
46/46 e2e · 30/30 smoke). Probe sources: `scripts/parity-probes/*-v4.mjs`
(passed to `agent-browser eval` via base64 to survive shell quoting).

Status after the v3 remediation: dashboard (hero/badge/allocation fill,
stat cards, donut sectors + labels + legend, breakdown drill-down, quick
actions), items views (headers, filter cards, cards, badges, footers,
hover buttons), dialogs (budget-item fields + classification tiles,
line-item fields + status enum, calculator), net worth (tabs, type
groups, cards), mobile chrome (layout geometry, hamburger, sheet) — all
re-verified matching. This pass found **6 clone-side finding groups**
plus **2 new reference mobile bugs** for the superset ledger.

---

## Findings ledger

### G1. [MED] Sidebar nav links are 40px tall (reference: 32px)

Reference link class (measured on `/dashboard`): shadcn
`SidebarMenuButton` base + custom overrides — the load-bearing tail is
`h-8 text-sm rounded-lg mb-1 transition-all duration-200 … flex
items-center gap-3 px-3 py-2.5`. Computed: **height 32px** (h-8 wins over
the py-2.5 padding), padding 10px 12px, gap 12px, radius 8px, icon 16px,
line-height 20px.

Clone today (`sidebar.tsx` NavList): `flex w-full items-center gap-3
rounded-lg px-3 py-2.5 text-sm transition-all duration-200 mb-1 …` — no
`h-8`, so py-2.5 × 2 + 20px line = **40px**. Everything else matches
(padding, gap, radius, colors, mb-1).

Fix: add `h-8` to the shared link classes (rail + sheet share NavList).

### G2. [MED] Inactive nav hover tint is `sidebar-accent` (reference: green-50)

Reference inactive hover: `hover:bg-green-50` (#f0fdf4 — a green tint),
plus the shadcn base `hover:text-sidebar-accent-foreground`. Clone uses
`hover:bg-sidebar-accent` → `--color-sidebar-accent` = **#f0f2ee** (a
warm gray-green) — a visibly different hover tint.

Fix: inactive links `hover:bg-green-50` (keep
`hover:text-sidebar-accent-foreground`).

### G3. [LOW] Active nav link dims on hover (reference: no hover change)

Reference active link keeps its inline gradient on hover (the inline
style outranks the class-level hover utilities — no visual change).
Clone active link carries `hover:opacity-90`, dimming the gradient to
90% on hover.

Fix: drop `hover:opacity-90` from the active variant.

### G4. [MED] Net-worth summary card: 3-col ratio grid vs the reference's 2-col grid + ratio footer row

Reference summary card (measured leaf-by-leaf):

- grid: `grid grid-cols-2 gap-4` with exactly **two** cards —
  Total Assets and Total Liabilities (`rounded-xl p-4`,
  `background-color: rgba(255,255,255,0.1)`, **`backdrop-filter:
  blur(10px)`**)
- card labels: `text-xs` `text-white/70` `mb-1` (12px, 70% white)
- card amounts: `text-2xl font-bold text-white` (**24px**)
- ratio: NOT a card — a footer row `mt-6 pt-6 border-t border-white/20`
  → `flex items-center justify-between` with label `text-sm
  text-white/80` (span) and value `text-lg font-bold text-white`
  (**18px** span)
- H2 net figure: `text-5xl font-bold` (48px) + label `text-sm
  text-white/80 mb-2`

Clone today: `grid grid-cols-1 gap-4 sm:grid-cols-3` with **three**
cards (the ratio is the third), labels `text-sm text-white/80`,
amounts `text-xl font-bold` (20px), no backdrop blur, no footer row.

Fix: restructure to the reference layout (2-col grid at ≥sm, ratio in
the border-t footer row, reference type sizes, backdrop blur). The
mobile stacking (`grid-cols-1`) stays — see G5.

### G5. [MED — clone bug, superset] Mobile net-worth page overflows horizontally by 38px

Clone at 390×844 on `/networth`: `document.documentElement.scrollWidth`
= **428** (38px sideways scroll). Isolation (hide-one-by-one): the
summary card's `flex items-center justify-between mb-8` header row —
the `text-4xl` (36px) H2 "−$245,950.00" (min-content ≈ 250px) + the
64px icon circle exceed the 294px mobile content box, and the flex
row's automatic minimum size drags `main` (flex-1, min-width:auto) to
428px.

The **reference has the same bug, worse**: its net-worth page scrolls to
**464px** at 390 (its H2 is `text-5xl` at all widths and its summary
grid is a fixed `grid-cols-2`), and its dashboard also scrolls 5px
(395px). Reference mobile overflow bugs are documented below (R3/R4);
the clone fixes them.

Fix (visual parity at desktop, no overflow at mobile — superset):
- H2: `text-3xl sm:text-5xl` (30px on phones — 13-char seed amount fits
  with ~19px slack; 48px from sm up = reference parity) + `break-words`
  for pathological amounts
- text block gets `min-w-0` so the H2 can shrink inside the flex row
- summary grid: `grid-cols-1 gap-4 sm:grid-cols-2` (stacks the two
  cards on phones instead of the reference's clipped 2-col crush)

### G6. [MED — functional] Items-view header count ignores the active filters

Reference: the "N items · $X" subtitle recomputes BOTH the count and
the total from the FILTERED list. Measured: search "zzzzqqq" →
"Income **0 items** · $0.00"; search "Sal" → "Income **1 items** ·
$5000.00".

Clone today (`items-view.tsx`): the total uses `sumAmounts(filtered)`
but the count renders `items.length` (the UNFILTERED total) — search
"zzzzqqq" shows the inconsistent "Income **2 items** · $0.00".

Fix: render `filtered.length`. (The reference's always-plural "items"
wording is already correct.)

### Reference mobile bugs newly documented (no clone change; superset ledger)

- **R3.** Reference dashboard at 390×844 scrolls horizontally 5px
  (`scrollWidth` 395): its `main` (flex-1, `min-width:auto`) renders
  395px wide inside the 390px `SidebarProvider` wrapper. The clone's
  dashboard measures exactly 390.
- **R4.** Reference net-worth page at 390×844 scrolls horizontally
  **74px** (`scrollWidth` 464) — `text-5xl` H2 + `grid-cols-2` summary
  (see G5). The clone fixes this class of bug (G5) as superset item #6.

Prior reference bugs re-confirmed live today: the toast-viewport
hamburger block (hit-test top element = the empty toast container,
`isButtonOrChild: false`) and the sheet-stays-open-after-nav trap
(overlay `[data-state=open]` persists after the route changes). The
clone's fixes for both re-verified end-to-end on the same probes.

### Verified matching this pass (no action)

Hero card gradient/label/status badge (`Under Budget` rgb(245,169,98)
`font-semibold`)/allocation fill (orange 90deg gradient), stat cards
(30px/700/forest-dark amounts, no-comma money, `1 item` singular count
row + 1px separator), donut sector order + fills + slice labels + legend
(piggy-bank/heart/circle-alert icons, gray last spans, card chrome),
breakdown sections/footers (`Net Balance+$2065.00`), brand block
(40px gradient tile + `text-xl font-bold`), rail geometry (256px,
`hidden`→`md:flex`), avatar footer (36px lime circle), items-view
headers (`text-3xl font-bold`, `N items · $X`), filter cards
(`bg-white rounded-2xl p-6 mb-6`, 20px icon, `pl-10`), item cards
(dot + h4 + subtitle, `text-2xl` typed amounts, badge maps incl. the
purple frequency + green Recurring + slate status, hover
Edit/Calculate buttons, calendar footers), the Add Budget Item dialog
(field set, defaults, tile chrome, 358px panel at 390), net-worth
tabs/type groups/asset cards/Add-Asset gradient, savings Add gradient,
login states (v3), mobile top bar + hamburger + sheet superset fixes.

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | Nav links: `h-8` + `hover:bg-green-50` inactive + no active hover dim | NEW `tests/e2e/nav-geometry.spec.ts` (3 specs) | `sidebar.tsx` |
| 2 | Net-worth summary card restructure (G4: 2-col grid, xs/70 labels, 2xl amounts, blur, ratio footer row text-lg) + mobile fit (G5: `text-3xl sm:text-5xl`, `min-w-0`, `break-words`, `grid-cols-1 sm:grid-cols-2`) | `networth.spec.ts` (+2 specs: card structure at desktop, mobile no-overflow at 390×844) | `net-worth-view.tsx` |
| 3 | Items-view header count follows filters (G6) | `items.spec.ts` (+1 spec: search garbage → "0 items", partial search → filtered count, clear → restored) | `items-view.tsx` |
| 4 | Regression: full chain + live parity re-check of the fixed surfaces | — | — |
| 5 | Docs: session_7 log, worklog, README superset list (+R3/R4, count 48+), CLAUDE test-count fix, SKILL project_state | — | docs |

## Regression pin map (must NOT change)

- Mobile-nav superset fixes #1/#2 + mobile-layout geometry (7 + 3 specs)
- Money two-formatter contract, breakdown drill-down, badge maps,
  gradients, calculator/line-item dialogs, net-worth ratio format
  (`0.21:1` / `∞:1`), type grouping, API contracts, seed arithmetic
- The net-worth summary card's GRADIENT, shadow, decorative circle,
  `-$245,950.00` H2 text, and grouped comma money stay as-is
