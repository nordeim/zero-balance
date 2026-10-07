# Remediation Plan v6 — Session-11 Parity Iteration

> **Status: COMPLETE** — all 14 finding groups fixed TDD-first (8 new e2e
> specs, RED→GREEN); full chain green at 96 unit / 73 e2e / 30 smoke; live
> parity re-verified surface-by-surface; R7 + D-9/D-10 documented. See
> `docs/session_11.md`.

Date: 2026-10-07 · Scope: fresh two-site re-audit after the v5 baseline
(`db757a2` + `bd2e4be`) re-verified green (typecheck · lint · 96/96 unit ·
build · 65/65 e2e · 30/30 smoke). Probes: `scripts/parity-probes/probe-v6-*.mjs`
via `run-probe.sh`; the clone's standalone parity server on `:3200` is now
booted per-command through `with-server.sh` (this sandbox reaps every
background process at command exit — see D-9 below).

This pass audited surfaces v2–v5 had NOT covered: the net-worth asset /
liability CARDS (chrome, action buttons, menus), the EDIT variants of every
dialog (prefill, disabled fields, grid spans), the calculator's populated
line-item rows, every EMPTY STATE on both sites (including filtered-to-zero),
wide-viewport content geometry (1440/1920), the sidebar bottom area, the
reference's toast container, and overlay/Escape/outside-click dismissal. It
found **14 clone-side finding groups** plus **one new reference bug (R7)**.

A note on the reference's data: its live dataset has changed since the
session-1 recon (income $5000 / savings $1000 / expenses $525 — 1/1/3 items,
expenses now Investments/Netflix/Rent, assets just Savings Account $25,000,
no liabilities). The clone's seed keeps its own recon-time story (income
5550 / savings 1250 / expenses 2235 — pinned by the unit + e2e suites); the
parity convention remains structure + chrome with each side's own data.
Reference data touched during this audit (a test line item and one asset)
was fully restored; verified live.

---

## Findings ledger

### G1. [MED] Dropdown menu items must NOT carry icons
The reference's card action menus (income/savings item cards AND net-worth
asset/liability cards) render Edit/Delete as **plain text** — zero SVGs, text
starting at the item's left padding. The clone renders a PencilIcon before
Edit and a Trash2Icon before Delete (svg: 1 on every item), shifting the text
~20px right. Files: `item-card.tsx` (income/savings menu),
`net-worth-view.tsx` (asset + liability menus).

### G2. [LOW] Net-worth menu Delete: named-class lab drift
`net-worth-view.tsx` uses `text-red-600 focus:text-red-600` → v4 computes
`lab(48.4493 …)`. The reference renders `rgb(220,38,38)`. Same fix as v5's
G9 pin: arbitrary hex `text-[#dc2626] focus:text-[#dc2626]` (item-card.tsx
already does this).

### G3. [MED] Every dialog Save button is missing the lucide Save icon
Measured on the reference's Add/Edit budget-item, line-item and asset
dialogs: the gradient Save buttons all carry the lucide **Save** icon
(`M15.2 3a2 2 0 0 1 1.4.6l3.8 3.8…`, 16px) before the label. The clone's
four Save buttons (asset `Save Asset`, budget-item `Save Item`, liability
`Save Liability`, line-item `Save Item`) have svgCount 0. Files:
`asset-dialog.tsx:208`, `budget-item-dialog.tsx:362`,
`liability-dialog.tsx:248`, `line-item-dialog.tsx:242`.

### G4. [MED] Asset dialog grid: Name and Last Updated must span full width
Reference grid (2×304px + 16px gap): Type(disabled on edit) | Amount, then
**Name `md:col-span-2` (624px)**, Institution | Account/Reference Number,
**Last Updated `md:col-span-2` (624px)**. The clone packs Name/Institution
and Account/Last-Updated into half-width cells. The budget-item dialog's
Classification row already renders full-width correctly (geometry matches —
only its DOM wrapper differs, invisible). File: `asset-dialog.tsx` (mirror
the same span pattern on the liability dialog's equivalent full-width rows
if its grid has any — verify against the ref at implementation time; the ref
has no liabilities so the asset pattern is the source of truth).

### G5. [MED] Asset/liability Type select must be DISABLED in edit mode
The reference disables the Asset Type combobox when editing (measured
`disabled: true`; enabled on create). The clone's budget-item dialog already
disables Type on edit (verified matching); the ASSET dialog does not. File:
`asset-dialog.tsx` (+ liability dialog for consistency with the same edit
pattern).

### G6. [MED] Net-worth empty states: bare icon, no tinted circle, mb-2, text-base
Reference (measured on both tabs — the assets state captured via a
delete/restore dance): inside the white `rounded-2xl` bordered card
(`text-center py-16 bg-white rounded-2xl`), the icon is a **bare lucide
icon** `w-16 h-16 mx-auto mb-4 opacity-20` inheriting near-black
`rgb(10,10,10)` — **circle-arrow-up** for assets, **circle-arrow-down** for
liabilities (NOT TrendingUp/CreditCard, and NOT inside a 64px tinted
circle). Heading `mb-2` (8px), description **16px** (`text-base`) gray-500
`rgb(107,114,128)`, gradient Add button with Plus icon (clone already
matches the button). Files: `net-worth-view.tsx` (both empty states).

### G7. [LOW] Calculator empty-state icon color
Reference: `lucide-calculator w-12 h-12 mx-auto mb-3 opacity-20` inheriting
near-black `rgb(10,10,10)`. The clone pins `color: rgb.forestDark`
(`#1a3a2e`). Size/mb/opacity already match. File:
`calculator-dialog.tsx:167`.

### G8. [LOW] Line-item dialog placeholders
Reference (measured on its Add Line Item dialog): Payment Method placeholder
= **"e.g., Direct Debit, Credit Card"** (clone: "e.g., Bank Account"); Notes
placeholder = **"Additional details about this item..."** (clone:
"Additional details..."). File: `line-item-dialog.tsx`.

### G9. [MED] Calculator line-item row actions must be ALWAYS visible
Reference (measured on a live row): the edit (near-black) and delete (red)
icon buttons render at `opacity: 1` at rest — 32×32 (`h-8 w-8`), no
aria-label, 16px icons. The clone wraps them in
`opacity-0 group-hover:opacity-100` (hidden until row hover). File:
`calculator-dialog.tsx:199`.

### G10. [LOW] Row action icon size + edit icon color
Reference row buttons: 16px icons (pencil near-black `rgb(10,10,10)`, trash
red `rgb(220,38,38)`). Clone: `h-3.5 w-3.5` (14px), edit icon
`color: rgb.gray` (gray-500). File: `calculator-dialog.tsx:200-215`.

### G11. [LOW] statusPill named-class drift
`bg-green-50 text-green-700` / `bg-yellow-50 text-yellow-700` /
`bg-gray-50 text-gray-700` compute as oklab in v4. Reference active pill
measured `rgb(240,253,244)` bg + `rgb(21,128,61)` text. Pin all three pairs
with arbitrary hex (green `#f0fdf4`/`#15803d`, yellow `#fefce0`/`#a16207`,
gray `#f9fafb`/`#374151`). File: `calculator-dialog.tsx:44-48`.

### G12. [MED] Items-view empty states must be BARE (no card, no circle)
Reference (measured via filter-to-zero on all three views): the empty state
is **not carded** — a bare `text-center py-16` block directly on the warm
page bg: bare lucide type icon (`w-16 h-16 mx-auto mb-4 opacity-20`,
near-black — **wallet / piggy-bank / receipt** by view), heading `mb-2`,
description **16px** gray-500, gradient Add button. The clone wraps it in a
white bordered rounded-2xl card with a 64px tinted circle. File:
`items-view.tsx` (the `filtered.length === 0` branch).

### G13. [MED] Content column: padding must sit OUTSIDE max-w-7xl
Reference page structure: `main > … > div.min-h-screen.p-4.md:p-8 >
div.max-w-7xl.mx-auto > content` — the 32px padding is OUTSIDE the 1280px
cap, so the content column = `min(vw − 256 − 64, 1280)`. The clone renders
`mx-auto w-full max-w-7xl p-4 md:p-8` (padding INSIDE the cap): at ≤1440px
the geometry is identical, but at ≥1568px viewports the clone's column is
**64px narrower** (measured at 1920: ref cards 1280 @ x=448 vs clone 1216 @
x=480). Fix all three views (dashboard/items/net-worth): outer
`min-h-screen p-4 md:p-8` wrapper + inner `mx-auto w-full max-w-7xl`.

### G14. [LOW] Card action trigger: ref ships `hover:text-accent-foreground`
The reference's 36px ellipsis triggers include `hover:bg-accent
hover:text-accent-foreground`; the clone has `hover:bg-accent` only (icon
color never changes on hover). Add the token-routed class (no hex needed —
both route through tokens aligned in v5). Files: `item-card.tsx:120`,
`net-worth-view.tsx:79` (+ the liability twin).

### R7. [DOC] New reference bug: dialogs ignore outside-click too
With the ref's Edit Budget Item dialog open, a real mouse click on the
overlay corner (20,20) does NOT close it — only X/Cancel do. Combined with
R5 (no Escape), the reference's dialogs are ONLY closable via their buttons.
The clone's Radix dialogs close on Escape (pinned) AND overlay click — both
superset behaviors, kept and documented.

Re-confirmed live this pass: R1 (the toast container still covers the
mobile hamburger — `fixed top-0 z-[100] w-full … pointer-events: auto`,
empty inner list), R5 (Escape ignored), R6 (Delete destroys immediately —
extended: the calculator's row Delete is also instant, no confirmation).
The clone's fixes for all of them re-verified via the existing specs.

### Verified matching this pass (no action)
Net-worth card chrome (`bg-white rounded-xl p-5 … hover:shadow-lg`, 1px
#e5e7e3 border, 12px radius, `0 2px 8px` shadow); action trigger geometry
(36px, 16px icon, group-hover reveal); menu chrome (border #e5e5e5, 6px,
p-1, min-w 128px, item 14px/400, Edit near-black); item-card edit dialog
(title "Edit Budget Item", Type disabled, field order, Classification
full-width 624px, Recurring switch copy + 36×20 geometry, Status row);
calculator banner/headings/gradients; "Add Item" orange-gradient header
button + "Add First Item" outline button; line-item row card chrome
(`rounded-xl p-4 hover:shadow-md`), frequency pill `#f3f4f6`/gray-500,
amount 20px/700 orangeDark, "Based on N item(s)" singular/plural;
**1920px chrome** (content caps at 1280 after the G13 fix); no logout UI on
either side; sidebar bottom area; items-view "0 items · $0.00"
filter-aware counts; empty-state Add buttons carry each surface's gradient.

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | Menu items without icons (G1) + net-worth Delete hex (G2) + trigger hover text (G14) | extend `tokens.spec.ts`: menu items have 0 svgs + net-worth menu Delete `rgb(220,38,38)`; extend `networth.spec.ts` or tokens: trigger `hover:text-accent-foreground` class present | `item-card.tsx`, `net-worth-view.tsx` |
| 2 | Save icon on all four dialogs (G3) | extend `dialog-buttons.spec.ts`: each Save button contains exactly 1 svg | 4 dialog files |
| 3 | Asset dialog: col-span-2 on Name + Last Updated (G4), Type disabled on edit (G5) | extend `networth.spec.ts`: open Add Asset → Name/Last-Updated wrappers 624px wide; open Edit via menu → Type trigger `disabled` | `asset-dialog.tsx` (+ liability mirror) |
| 4 | Calculator: row buttons always visible 16px near-black/red (G9/G10), statusPill hex (G11), empty icon color (G7) | extend `calculator.spec.ts`: create a line item via UI, assert row buttons opacity 1 + icon 16px + colors; status pill computed `rgb(240,253,244)`/`rgb(21,128,61)`; empty icon `rgb(10,10,10)` | `calculator-dialog.tsx` |
| 5 | Line-item placeholders (G8) | extend `calculator.spec.ts` (or dialog-buttons): placeholder attributes match the reference strings | `line-item-dialog.tsx` |
| 6 | Net-worth empty states (G6): bare icons (circle-arrow-up/down), mb-2, text-base | NEW `empty-states.spec.ts`: API-delete liabilities → assert bare icon (opacity-20, near-black, 64px), heading margin 8px, desc 16px, card wrapper → API-restore fixtures | `net-worth-view.tsx` |
| 7 | Items-view empty states (G12): bare block, no card/circle, wallet icon | same spec: search gibberish on /income → assert no bordered card, bare icon near-black 64px, desc 16px, heading mb 8px | `items-view.tsx` |
| 8 | Wide content column (G13): padding outside max-w-7xl | same spec (or `mobile-layout.spec.ts`): viewport 1920 → first content card width 1280 on /dashboard, /income, /networth | `dashboard-view.tsx`, `items-view.tsx`, `net-worth-view.tsx` |
| 9 | Docs: R7 + D-9 sandbox note + data-story note; session_11 log; worklog; README/CLAUDE/AGENTS/SKILL alignment | — | docs |
| 10 | Regression: full chain + live parity re-check of every fixed surface + screenshots | — | — |

## Regression pin map (must NOT change)

- All six superset fixes (hamburger hit, sheet close-on-nav, root-URL nav
  highlight, no mobile overflow, Escape close, delete confirmations)
- Money two-formatter contract, breakdown drill-down, donut order/icons,
  stat cards, hero states, per-surface add gradients, badge maps, type
  grouping, ratio format, calculator server-side recalc, seed arithmetic
- The v5 token block, `@variant hover` pin, tab grid, outline Cancellations,
  gradient Saves (this plan only ADDS the Save icon), popover borders
- e2e fixture discipline: every spec restores what it mutates (the new
  empty-state spec deletes + re-creates the two seeded liabilities via API
  with identical field values)
