# Session 3 — Deep Parity Audit & Remediation v2

**Date:** 2026-10-07 · **Scope:** visual/functional parity superset pass against the live reference · **Outcome:** 14 finding groups fixed, full chain green, pushed to `main`.

## Where this session started

Session 2 re-verified the v1 remediation and concluded the clone was a
verified superset with "zero new gaps" — based on a structural walk. This
session went DEEPER: money formatting templates, conditional UI states,
per-view gradients, badge color maps, and the breakdown's interaction model,
using two evidence sources the earlier sessions had not fully mined:

1. **The live reference DOM** — computed styles, real clicks, real hover
   states (the reference account now carries live user data: $5,000 income /
   $1,000 savings / $525 expenses → +$3,475, "Under Budget" 30.5%).
2. **The reference's minified JS bundle** (`assets/index-DZ3RKTz_.js`,
   1.05 MB) — template extraction for conditional states that cannot be
   triggered without mutating the user's live data (over-budget hero,
   "✓ NET ZERO", allocation fill gradients, badge maps `b1e`/`x1e`,
   line-item row, drill-down grouping).

## What the audit found (14 finding groups)

The full ledger with verbatim evidence lives in
[`remediation-plan-v2.md`](remediation-plan-v2.md). Headlines:

1. **Money format split** — the reference renders plain `"$"+toFixed(2)`
   (NO commas: `$5000.00`) on dashboard/items/calculator; `toLocaleString`
   grouping only on net worth. The clone used commas everywhere.
2. **Ratio** — `0.21:1` (toFixed(2), no spaces) / `∞:1`, not `0.2 : 1`.
3. **The breakdown is a 3-level accordion drill-down** (section → category →
   subcategory → item + "N categories" footer), NOT navigation rows. Item
   labels = notes truncated to 30 chars or the literal "Item"; null
   subcategories group under "Other"; Net Balance is sign-conditional
   (zero lime / positive #f5a962 / negative #3b7ea1).
4. **Donut order + legend icons** — sectors [Savings, Want, Need];
   piggy-bank / heart / circle-alert legend icons.
5. **Calculator card** — orange-tinted bordered card, label-left /
   amount-right in #e07a3b, "Based on N item(s)" + conditional
   "• Will update category total" in text-orange-600; header carries an
   orange-gradient chip + Close X; line-item rows use gray rounded-full
   pills, `#policy` lines, hover-revealed ghost buttons, no "From date".
6. **Stat cards** — `text-3xl` forestDark amounts (not type-colored
   text-2xl), chevron-right, count row with `h-px` flex-1 divider.
7. **Hero** — balance is `Math.abs` (sign lives in the chip), "✓ NET ZERO"
   literal chip, over-budget = BLUE #3b7ea1 (clone had orange), allocation
   fill gradient status-conditional (lime/orange/blue).
8. **Per-view add-button gradients** — dashboard forest→lime, income
   lime→limeLight, savings blueDark→blue, expenses orange→orangeLight,
   asset forest→lime, liability + calculator orange→orangeLight. The clone
   had one solid-lime button class.
9. **Quick actions are card-buttons** (p-6 rounded-2xl, tinted chip with
   hover scale-110, plus icon ml-auto), not a row of small buttons.
10. **Item-card badge maps** — per-classification colors/borders/ICONS
    (need circle-alert/red, want heart/blue, savings piggy-bank/green),
    per-frequency colors (weekly blue, quarterly indigo, annually pink…),
    capitalized green "Recurring" badge between frequency and status, status
    ALWAYS slate.
11. **Expense cards** carry hover-revealed absolute Edit/Calculate buttons
    (pen icon, "Edit Category"/"Open Calculator" titles) and NO ellipsis
    menu; income/savings cards keep the ellipsis.
12. **Networth lists are grouped by type** (capitalize h3 headers —
    forestMedium for assets, orangeDark for liabilities) and cards use
    dot + name + gray type badge (no icon chips), stacked footers with a
    liability-only "{rate}% interest" line.
13. **Icon corrections** — lucide-receipt (not receipt-text) on expense
    surfaces; lucide-pen on the expense Edit button; chevron-right on stat
    cards.
14. **Items-view headers** — gradient chips with white icons; the subtitle
    is ALWAYS plural ("1 items").

## Superset decisions

- The reference has NO delete affordance on expense cards (verified: 0/3
  cards have an ellipsis; income cards' menu is Edit/Delete). The clone keeps
  card chrome identical and adds a red Delete button in the EDIT DIALOG —
  the superset delete path (pinned by `items.spec.ts`).
- The drill-down accordion behavior was verified LIVE (expanding a second
  section collapses the first — bundle `i(r===E?null:E)`), then pinned by
  `breakdown.spec.ts`.

## TDD execution

Tests first, then implementation, per finding group:

- `tests/money.test.ts` rewritten (20 tests) for the two-formatter contract.
- `tests/constants.test.ts` extended (15 tests) pinning the badge maps,
  gradients and guideline rows extracted from the reference.
- `tests/dashboard-math.test.ts` — donut slice order [Savings, Want, Need].
- New `tests/e2e/breakdown.spec.ts` (5 tests): drill-down expansion,
  categories/subcategories/item labels, accordion semantics, Net Balance
  color.
- `dashboard/items/networth/calculator.spec.ts` rewritten against the new
  surfaces (money formats, gradients, badge classes, hover-revealed
  buttons, type grouping, ratio).
- Implementation: `money.ts`, `constants.ts`, `dashboard.ts`,
  `dashboard-view.tsx` (full rewrite incl. the drill-down), `items-view.tsx`,
  `item-card.tsx`, `calculator-dialog.tsx` (full rewrite),
  `net-worth-view.tsx` (full rewrite), `budget-item-dialog.tsx` (superset
  delete), `globals.css` (`.zb-btn-add` gradient chrome).

## Verification

- typecheck ✓ · lint ✓ · **95/95 unit** ✓ · build ✓ · **39/39 e2e**
  (incl. 7 mobile-nav specs + 5 new breakdown specs) ✓ · **30/30 smoke** ✓
- Live clone-vs-reference parity probes on the remediated build: hero
  (|balance|, orange under-budget fill), plain money on every dashboard
  surface, [Savings, Want, Need] sectors + iconed legend, guidelines tints,
  Net Balance orangeLight, drill-down structure, expenses badges order
  (need → monthly → Recurring → active), hover Edit/Calculate with titles,
  calculator chrome (#fff7f5/#fcddd5 card, orange gradient chip), networth
  grouping + "0.21:1" — all matching.
- Both reference mobile-nav bugs confirmed STILL LIVE on the reference
  (toaster hit-test block + stuck sheet) — the clone's fixes remain pinned
  by the mobile-navigation specs.
- Screenshots regenerated (11 files, incl. the new
  `11-breakdown-drilldown.png`).

## Docs alignment

README (features table, money paragraph, test counts, engineering
references), PAD (ADR-004 two-formatter decision, seed figures), SKILL
(project state, seed arithmetic, money examples), this session log, the
repo-root `worklog.md`, and `remediation-plan-v2.md` itself.
