# Remediation Plan v2 — Deep Parity Audit (Session 3)

Date: 2026-10-07
Scope: findings from the session-3 deep parity audit against the live reference
(`https://zero-balance-4885a8f3.base44.app/`) — evidence gathered from BOTH the
live DOM (computed styles, real clicks, real hover states) and the reference's
minified JS bundle (`assets/index-DZ3RKTz_.js`, 1.05 MB, template extraction).
Every finding below cites its evidence source. This plan supersedes the visual
sections of `remediation-plan.md` (v1), which remains valid for the
infra/Tailwind/mobile-nav findings that are already shipped.

The v1 audit concluded "zero new gaps" based on a structural walk; the v3 audit
went deeper (money formatting templates, conditional states, per-view gradients,
badge color maps, drill-down interactions) and found **14 real gap groups**.
All are in scope for this remediation.

---

## Findings ledger

### F1. Money format split (plain `toFixed(2)` vs grouped)

Evidence — bundle: `children:["$",x.toFixed(2)]` (calculator),
`["$"+t.toFixed(2)]` style templates on dashboard/items/donut;
networth cards: `o.toLocaleString(void 0,{minimumFractionDigits:2,maximumFractionDigits:2})`.
Evidence — live DOM: dashboard hero `$3475.00`, stat cards `$5000.00`, breakdown
`- $1000.00`, legend `$6025.00`; networth summary `$25,000.00`, asset card `$25,000.00`.

| Surface | Reference format | Clone today |
|---|---|---|
| Dashboard (hero/breakdown/stat/donut legend) | `$5000.00` — no grouping | `$5,000.00` |
| Items views (header subtitle, card amounts) | `$5000.00` | `$5,000.00` |
| Calculator (total, line-item amounts) | `$25.00` | `$25.00` (< $1,000 identical) |
| Networth (summary, cards, tab short) | `$25,000.00` grouped; `$25,000` short | grouped ✓ |

Fix: `formatMoney`/`formatSignedMoney` become plain (`$` + `toFixed(2)`); new
`formatMoneyGrouped` for networth surfaces. Unit tests updated first (TDD).

### F2. Net-worth ratio rendering

Evidence — bundle: `children:[t>0?(e/t).toFixed(2):"∞",":1"]`.
Evidence — live: `∞:1` (debt-free account).

Reference: `0.21:1` (2 decimals, no spaces) / `∞:1`. Clone: `0.2 : 1` (1 decimal,
spaces). Fix `formatRatio` → `.toFixed(2)` and render `{ratio}:1` with no spaces.

### F3. Breakdown card is a 3-level expandable drill-down

Evidence — live clicks on the reference: clicking "Total Income" expands in place
(no navigation); "Salary" expands subcategory + item rows. Full DOM captured at
every level. Bundle: `isExpanded`/`categories`/`onToggleCategory` props,
`P.notes?P.notes.substring(0,30)+(P.notes.length>30?"...":""):"Item"`.

Structure (all captured verbatim):
- Level 1 (section buttons): icon chip `w-8 h-8 rounded-lg` tint 0.125, label
  `text-sm font-medium` gray, chevron-down `w-3.5` wrapped in `div.ml-1`, amount
  `font-semibold` section color, `- ` prefix on savings/expenses.
- Level 2 (category): container `ml-10 mt-2 space-y-2 pb-2` inside
  `overflow-hidden` (animated height/opacity); rows are buttons
  `py-1.5 px-3 rounded-lg hover:bg-gray-100` bg `rgb(249,250,251)`; dot `w-1.5`
  section color; name/amount `text-xs font-medium` forestDark; chevron-down
  `w-3`; footer row `py-1.5 px-3 border-t`: `N category`/`N categories`
  (`text-xs font-semibold` gray) + total (`text-xs font-bold` section color).
- Level 3 (subcategory): container `ml-4 mt-1 space-y-1`; rows
  `py-1 px-2 rounded` bg `rgb(250,250,250)`; dot `w-1` @ 0.6 opacity; name
  `text-xs` gray; amount `text-xs font-medium` gray.
- Level 4 (items): container `ml-4 space-y-0.5 mt-0.5`; rows `py-1 px-2 text-xs`
  color `rgb(156,163,175)`; dot `w-0.5` @ 0.4 opacity; label = notes truncated
  to 30 chars (`...` suffix) or literal `Item`; amount `font-medium`.
- Net Balance row: plain div in `border-t pt-3 mt-3`; label
  `text-sm font-semibold` gray; amount `text-lg font-bold`; color conditional:
  zero → `#8fbc3f`, positive → `#f5a962`, negative → `#3b7ea1`; matching icon
  chip (trending-up for ≥0, trending-down for negative).

Clone today: rows navigate to `/income` etc. and Net Balance is always lime.
Fix: implement the full drill-down; keep navigation OUT (parity), sections
independently expandable, one expanded section at a time is NOT required
(reference allows multiple open — verified: Income + Savings + Expenses all
open simultaneously).

### F4. Donut card structure, order and legend icons

Evidence — live DOM: sector fills `['#8fbc3f','#3b7ea1','#e07a3b']` =
[Savings, Want, Need]; legend rows carry `lucide-piggy-bank` (Savings),
`lucide-heart` (Want), `lucide-circle-alert` (Need); title is a shadcn CardTitle
div; card is `rounded-xl border bg-card shadow` with header `p-6` +
content `p-6 pt-0`; legend container `flex flex-col gap-3 mt-6`.

Fix: reorder data to [Savings, Want, Need], add icons + `w-4 h-4` swatch,
adopt shadcn card shell, plain money in legend amounts, slice labels stay
`{pct}%` (1 decimal — already matching).

### F5. Stat cards

Evidence — live DOM: amount `text-3xl font-bold mb-4` color `rgb(26,58,46)`
(forestDark, NOT type color); chevron is `lucide-chevron-right w-5 h-5`
(opacity-0 → group-hover); count row `flex items-center gap-2 text-sm` =
"N item/items" gray + `flex-1 h-px` divider (`rgb(229,231,227)`) +
`lucide-trending-up w-4 h-4` in type color; icons wallet / piggy-bank /
**receipt** (clone uses receipt-text).

### F6. Hero conditional states

Evidence — bundle:
`children:["$",Math.abs(r).toFixed(2)]`;
`i?m.jsx("div",{className:"px-4 py-2 rounded-lg font-semibold text-sm",style:{backgroundColor:"#8fbc3f",color:"white"},children:"✓ NET ZERO"})`
`:o? trending-up #f5a962 + "Under Budget" : trending-down #3b7ea1 + "Over Budget"`;
fill `i?"linear-gradient(90deg, #8fbc3f 0%, #b8d87e 100%)":o?"...#e07a3b...#f5a962...":"linear-gradient(90deg, #2c5f7c 0%, #3b7ea1 100%)"`.

Fix: balance = `$` + `Math.abs(balance).toFixed(2)`; literal `✓ NET ZERO` chip
(no icon); over-budget = blue `#3b7ea1` (clone wrongly orange); allocation fill
gradient conditional on status (net-zero → lime, under → orange, over → blue).
Under-budget visuals verified live and already match otherwise.

### F7. Add-button per-view gradients (135deg)

Evidence — computed styles on live reference:

| Button | Gradient |
|---|---|
| Dashboard "Add Item" | `#2d5a4a → #8fbc3f` (forest → lime) |
| Income "Add Income" | `#8fbc3f → #b8d87e` (lime → lime-light) |
| Savings "Add Savings" | `#2c5f7c → #3b7ea1` (blue-dark → blue) |
| Expenses "Add Expense" | `#e07a3b → #f5a962` (orange → orange-light) |
| Networth "Add Asset" | `#2d5a4a → #8fbc3f` |
| Networth "Add Liability" | `#e07a3b → #f5a962` |
| Calculator "Add Item" | `#e07a3b → #f5a962` (bundle) |
| Calculator empty "Add First Item" | outline variant (bundle) |

Clone today: solid lime `.zb-btn-primary` everywhere. Fix: per-view gradient
class (`.zb-btn-gradient` accepting the pair), plus icon `w-5 h-5 mr-2`.

### F8. Dashboard quick actions are card-buttons

Evidence — live DOM: `grid md:grid-cols-3 gap-6` of `<button class="p-6
rounded-2xl text-left transition-all duration-200 hover:shadow-lg group">` with
white bg + border; inner `flex items-center gap-3`: tinted icon chip `w-10 h-10
rounded-xl group-hover:scale-110 transition-transform` + label `font-medium`
forestDark + plus `w-4 h-4 ml-auto opacity-50 group-hover:opacity-100` type
color. Icons: wallet (lime) / piggy-bank (blue) / receipt (orange).
Clone today: three small solid-lime buttons in a flex row. Fix: card-button grid.

### F9. Items-view headers

Evidence — live DOM: icon chip `w-12 h-12 rounded-xl` with GRADIENT bg
(income `#8fbc3f→#b8d87e`, savings `#2c5f7c→#3b7ea1`, expenses `#e07a3b→#f5a962`)
and icon `w-6 h-6 text-white`; subtitle **always** `1 items · $5000.00`
(no singular form); h1 `text-3xl font-bold`. Dashboard h1 is
`text-3xl md:text-4xl font-bold mb-2`. Clone: tinted chip w-10 + colored icon,
singular/plural switch. Fix accordingly.

### F10. Item-card badges and action buttons

Evidence — live DOM + bundle maps:
- Classification badge (map `x1e`): need `bg-red-50 text-red-700 border-red-200`
  + circle-alert icon; want `bg-blue-50 text-blue-700 border-blue-200` + heart;
  savings `bg-green-50 text-green-700 border-green-200` + piggy-bank.
- Frequency badge (map `b1e`): one-time `bg-gray-100 text-gray-700`; weekly &
  bi-weekly `bg-blue-50 text-blue-700`; monthly `bg-purple-50 text-purple-700`;
  quarterly `bg-indigo-50 text-indigo-700`; annually `bg-pink-50 text-pink-700`.
- Recurring badge (conditional, order: classification → frequency → Recurring →
  status): `bg-green-50 text-green-700`, repeat icon `w-3 h-3 mr-1`, text
  **"Recurring"** capitalized.
- Status badge: ALWAYS `bg-slate-50 text-slate-700` (bundle:
  `className:"bg-slate-50 text-slate-700",children:e.status`).
- Expense cards: `relative` card + absolute hover-revealed button row
  (`absolute top-3 right-3 flex gap-2 opacity-0 group-hover:opacity-100
  transition-opacity z-10`): Edit (white, shadow-md, `border-input`,
  `hover:bg-gray-50`, `lucide-pen` w-3.5, `title="Edit Category"`) and Calculate
  (white, `text-orange-600`, `hover:bg-orange-50`, `border-orange-200`,
  `lucide-calculator` w-3.5, `title="Open Calculator"`); header block gets
  `pr-24`; **no ellipsis menu on expense cards** (verified: 0/3 expense cards
  have one; income card ellipsis → Edit/Delete confirmed by real click).
- Income/savings cards: hover-revealed ellipsis → Edit/Delete (clone already ✓).

Superset decision: the reference has NO delete affordance for expense items.
To stay a functional superset without deviating visually, the item dialog gains
a red "Delete" button in edit mode (dialog-only affordance, invisible on cards).

### F11. Calculator dialog

Evidence — live DOM (opened on reference "Investments" card) + bundle:
- Panel: `max-w-3xl`, overlay `rgba(26,58,46,0.5)` + `blur(8px)`.
- Header: `border-b px-6 py-4 flex items-center justify-between` with icon chip
  `w-10 h-10 rounded-xl` orange gradient (`#e07a3b→#f5a962`, hardcoded) +
  white calculator icon; h2 `text-lg font-bold` forestDark; desc `text-sm` gray;
  Close X `h-9 w-9`.
- Total card: `mb-6 p-4 rounded-xl` bg `#fff7f5` border `#fcddd5`;
  row 1 (`mb-2`): "Total Calculated" `text-sm font-medium` gray LEFT + amount
  `text-2xl font-bold` `#e07a3b` RIGHT (`$` + `toFixed(2)`); row 2 (`text-xs`
  gray): "Based on N item/items" + conditional `text-orange-600`
  "• Will update category total" shown when `total !== item.amount`.
- "Line Items" h3 + Add Item button (size sm, orange gradient).
- Empty state: `text-center py-12`; calculator icon `w-12 h-12 mx-auto mb-3
  opacity-20`; "No line items yet. Start by adding individual items that make
  up this category." `text-sm mb-4`; "Add First Item" outline sm button.
- Line-item row (bundle `O1e`): `bg-white rounded-xl p-4 group hover:shadow-md
  transition-all` border; h4 `font-semibold mb-1` name; provider `text-sm` gray;
  hover-revealed ghost icon buttons (pen `w-3.5`; trash `w-3.5 text-red-600`);
  bottom `flex items-end justify-between` — LEFT `space-y-1`: frequency pill
  `px-2 py-0.5 rounded-full` bg `#f3f4f6` + conditional status pill
  (active `bg-green-50 text-green-700`; pending `bg-yellow-50 text-yellow-700`;
  else `bg-gray-50 text-gray-700`) + `#{policy_number}` line `text-xs #9ca3af`;
  RIGHT amount `text-xl font-bold` `#e07a3b`. **No "From date" line.**

Clone today: shadcn DialogHeader (no chip), cardTint banner with icon chip,
always-purple frequency badges, slate status, "From date" row, always-visible
edit/delete. Fix to the reference structure.

### F12. Networth type-grouped lists + card restructure

Evidence — live DOM + bundle (`Object.entries(...)` grouping, card `U$`):
- Lists grouped by type: section `h3 text-lg font-semibold mb-3 capitalize`
  — assets color `#2d5a4a`, liabilities `#e07a3b`; label = raw type key with
  underscores → spaces (CSS `capitalize` does the visual casing); grid
  `md:grid-cols-2 lg:grid-cols-3 gap-4`.
- Asset/liability card: NO icon chip — dot `w-2 h-2` (asset `#8fbc3f` /
  liability `#e07a3b`) + name h4 `font-semibold` forestDark; type badge
  `bg-gray-100 text-gray-700 text-xs` (title-cased, e.g. "Bank Account");
  hover-revealed ellipsis → Edit/Delete; amount `text-2xl font-bold` type color
  (grouped format); footer `space-y-2 text-xs` gray, stacked lines:
  institution (building2 `w-3`), liabilities only `{rate}% interest`
  (percent icon), "Updated {MMM d, yyyy}" (calendar `w-3`).
- Section h2 `text-2xl font-bold` (clone: text-xl); tab panel `space-y-6 mt-2`.

Clone today: flat grid, icon-chip cards, h3 type + h4 name, interest appended
to the Updated line. Fix to the reference structure.

### F13. Icon inventory corrections

- Expenses stat card / breakdown row / items-view chip / quick action:
  `lucide-receipt` (clone: receipt-text).
- Item-card Edit (expense): `lucide-pen` (clone: pencil — same glyph family,
  align to pen); classification icons per F10.
- Stat card chevron: `lucide-chevron-right` (clone: rotated chevron-down).

### F14. Header/search chrome

- Dashboard h1 `text-3xl md:text-4xl font-bold mb-2` (clone: text-3xl only).
- Search placeholder + filter labels verified identical (no change).
- Items subtitle always plural (F9).

---

## ToDo (execution order — TDD)

| # | Task | Test first | Files |
|---|---|---|---|
| 1 | `money.ts`: plain `formatMoney`/`formatSignedMoney`, new `formatMoneyGrouped`, `formatRatio` → 2-decimals | `tests/unit/money.test.ts` rewrite | `src/lib/money.ts` |
| 2 | Constants: `ADD_GRADIENTS`, `HEADER_CHIP_GRADIENTS`, `FREQUENCY_BADGES`, `CLASSIFICATION_BADGES` (icons+border), guidelines data | `tests/unit/constants.test.ts` extend | `src/lib/constants.ts` |
| 3 | Dashboard: hero states (F6), stat cards (F5), donut (F4), guidelines (F11 rows), quick actions (F8), gradients (F7), header (F14) | e2e `dashboard.spec.ts` rewrite + new `breakdown.spec.ts` | `dashboard-view.tsx` |
| 4 | Breakdown drill-down (F3) incl. conditional Net Balance colors | `breakdown.spec.ts` (new) | `dashboard-view.tsx` |
| 5 | Items view: header chip gradient + white icon, always-items subtitle, per-view Add gradient (F7/F9) | `items.spec.ts` updates | `items-view.tsx` |
| 6 | Item card: badge maps, Recurring green capitalized, status slate, expense hover buttons, pen/receipt icons (F10/F13) | `items.spec.ts` updates | `item-card.tsx` |
| 7 | Superset: Delete button in item dialog edit mode (F10) | `items.spec.ts` new case | `budget-item-dialog.tsx` |
| 8 | Calculator: header chip + Close X, total card, line-item rows, empty state (F11) | `calculator.spec.ts` rewrite | `calculator-dialog.tsx`, `globals.css` |
| 9 | Networth: ratio, type grouping, cards, h2 size, interest line (F2/F12) | `networth.spec.ts` updates | `net-worth-view.tsx` |
| 10 | e2e regression sweep: update every money assertion (commas → plain on dashboard/items; grouped on networth) | all specs | `tests/e2e/*` |
| 11 | Full chain: typecheck, lint, vitest, build, playwright, smoke | — | — |
| 12 | Live parity re-verification (clone vs reference, desktop + mobile 390×844) | — | — |
| 13 | Screenshots refresh `docs/screenshots/` | — | `scripts/capture-screenshots.mjs` |
| 14 | Docs: README/PAD/SKILL alignment, `worklog.md` (repo root), `docs/session_3.md` | — | docs |

## Regression pin map (what must NOT change)

- Mobile nav superset fixes (toast viewport pointer-events, sheet close-on-nav)
  — pinned by `mobile-navigation.spec.ts` (7 specs).
- Login/auth flows, rate limiting, db-path discipline, API contracts (21 handlers).
- `.zb-modal-*` overlay/panel stacking; dialog Escape/overlay close behavior.
- Seed data (`demo@zerobalance.app`) and e2e storage-state setup.

## Verification commands

```bash
npm run typecheck && npm run lint && npm run test:unit
npm run build
DATABASE_URL="file:../db/e2e.db" npx playwright test   # via package scripts
bash scripts/smoke-test.sh
```
