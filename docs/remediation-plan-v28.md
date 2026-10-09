# Remediation Plan v28 — Session-55 Parity Iteration

Date: 2026-10-09 · Scope: fresh two-site re-audit after the v27 baseline
(`eca1754` + the session-56 log doc through `8329114` on `main`, all green
per this session's re-run: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓
(robots + sitemap prerendered) · **155/155 e2e** ✓ · 35/35 smoke ✓). The
workspace was re-cloned fresh (the sandbox reset); the environment restored
and re-verified (`.env` with `DATABASE_URL="file:../db/custom.db"`, `db/`
at the repo root re-pushed + re-seeded, node_modules reinstalled, the
scandihaven pattern repo re-cloned at `d4789c3` — unchanged from the v27
session's verification). Probes: one-shot `agent-browser eval` scripts on
the ONE shared parity tab (always `open <target-url>` + settle before every
eval), the standalone parity server on :3200 per `scripts/with-server.sh`
(data-dependent probes inside ONE invocation), REAL Tab walks via
`agent-browser press Tab` (parked pointer at (5,5) first), REAL CDP hovers
via `agent-browser mouse move` (synthetic mouseenter never engages `:hover`
— measured this session), and the class-attribute read as the reliable
arbiter (the v26/v27 lesson).

## The sweep — method and results

The pass swept the session-55 log's three suggested surfaces — the
**card action-menu trigger family** (the "Active ▾" status button), the
**avatar/user chip**, and the **toast close buttons** — plus the suggested
**one-pass button-variant class census** (every `<button>` on the items
views diffed between the sites), and the standing re-verification set
(mobile-nav R1–R4 on BOTH sites, data drift, the SEO pair, the v27 fix in
place), and the code audit (lint/tsc/tests green; `npm audit` = the same 5
dev-only ESLint `braces` advisories, no patched release — accepted,
unchanged; secret-pattern scan matches only the documented files; the v27
changeset `eca1754` re-verified in the tree — the `dialog.tsx` class string
+ the extended v9 X-close spec, all pinned).

- **Mobile navigation (task focus) R1–R4 all re-verified live on BOTH sites
  — the 22nd consecutive check.** R1: the reference's two `fixed top-0
  z-[100]` toast containers still intercept the burger's center hit at
  (38,30) (`pe:auto`, 390×32, z-100; scrollWidth 395 on `/`), while the
  clone's burger hit is DIRECT on the svg with the viewport `pe:none` and
  390 fit on every route. R2: the reference's sheet still traps after nav
  (`sheetStillOpen: true`); the clone's closes (superset fix #2) — sheet
  288px + Income link (20,185) 247×32 identical. R3: the reference marks
  nothing active on `/` (all five rail links `rgb(63,63,70)`/400, no
  `<nav>` landmark); the clone highlights Dashboard (the documented
  superset). R4: the reference overflows 395 on `/`+`/dashboard` and 464 on
  `/networth`; the clone fits 390 on all six routes. **The Tailwind v4 pins
  hold — the clone's mobile menu works as expected.**
- **Data drift clean (22nd consecutive check, after an explicit
  add-then-delete probe cycle restored to census)**: the reference
  unchanged (allocation 30.5%, Balance `$3475.00`, income `$5000.00`/1
  item, savings `$1000.00`/1 item, expenses `$525.00`/4 items).
- **SEO check (the brief's standing ask) PASSES**: both sites serve
  `/robots.txt` (allow-all + the sitemap link) and `/sitemap.xml`
  (five URLs, `/login` excluded).
- **The one-pass button-variant census (the session-55 suggestion — every
  `<button>` on the items views, full class strings, both sites)**: the Add
  buttons (the clone's `zb-btn-add` gradient pin — the focus family
  verified byte-identical on real Tab in v27), the three Select triggers
  (byte-identical `focus:outline-none focus:ring-1 focus:ring-ring`),
  and the income card's hover-revealed 36×36 ghost-icon button
  (`focus-visible:ring-1` + `hover:bg-accent
  hover:text-accent-foreground` + `opacity-0 group-hover:opacity-100`) all
  match. TWO census surfaces drifted — the expense-card footer
  **Edit/Calculate buttons** (G2 below) and the **card badges** (G1 below).
- **The card action-menu trigger ("Active ▾" — session-55's suggestion)**:
  measured directly — the reference's status element is a plain DIV (not a
  button, no menu): clicking it opens NOTHING (no `[role=menu]`, no
  popper, no state change). Its `cursor: pointer` is INHERITED from the
  clickable card. But the read surfaced the real drift the suggestion was
  circling: the reference's card badges carry the full shadcn **Badge
  base** — `transition-colors focus:outline-none focus:ring-2
  focus:ring-ring focus:ring-offset-2 hover:bg-secondary/80` — and on a
  REAL CDP hover (`agent-browser mouse move` to the badge center) the
  status/classification badges' background computes **`rgba(245, 245, 245,
  0.8)`** (secondary `#f5f5f5` at 80% over the white card) with the 150ms
  color transition. The clone's badges are static spans with NO hover
  family (measured: bg stays `rgb(248,250,252)` under the same hover).
  The focus classes are inert on both sites (non-focusable DIVs/SPANs) —
  the rendered drift is the hover tint + transition → **G1**.
- **The avatar/user chip (session-55's suggestion)**: the reference's chip
  (the sidebar footer "U" circle + "Budget Pro" labels) is a NON-interactive
  DIV row (`flex items-center gap-3 p-3 rounded-lg`, 223×60, no role, no
  tabindex, no handler) and the clone's `UserFooter` matches the pinned
  structure — **NO keyboard family exists on either site — no finding**.
- **The toast close buttons (session-55's suggestion)**: the reference
  renders **NO toasts at all** — the add-success flow leaves both
  `fixed top-0 z-[100]` toast viewports at their empty 32px padding
  (heights sampled at 200ms / 900ms / 3.4s after the save — all [32,32]).
  The clone's toasts + close buttons remain the established superset
  (session-1 design, v18 text pins). **No reference surface to compare —
  no finding.**
- **The Budget Item Details dialog (surfaced while probing the card-click
  path — REAL FINDING, the headline)**: on the reference, clicking an item
  card body opens a read-only **"Budget Item Details"** sheet; the clone's
  card click does NOTHING (verified live: no overlay, no text change) —
  **G3 below**, fully measured on both the desktop and mobile layouts.
- Probe-methodology notes: synthetic `mouseenter`/`pointerover` events
  never engage CSS `:hover` (the reference's status badge measured
  unchanged under synthetic events, tinted under the real CDP
  `mouse move`); the reference's dialogs are plain divs that do NOT close
  on Escape (the clone's Radix Escape-close is the v22 superset — the
  close-path is the X button); and the reference's number-input finder must
  match `type="number"` (its "0.00" is the placeholder, the value stays
  empty — a v28 probe-script lesson).

### The reference's Budget Item Details dialog — the full measured contract

- **Trigger**: clicking the item card body (any type — income, expense,
  savings; desktop AND mobile). The reference's card carries
  `cursor-pointer group` (the clone already renders the same card chrome).
- **Overlay**: `fixed inset-0 z-50 flex items-end md:items-center
  justify-center p-0 md:p-4` — background `rgba(26, 58, 46, 0.5)`
  (forest-dark 50%) + `backdrop-filter: blur(8px)` (the SAME overlay family
  the clone's `.zb-modal-overlay` already pins for its edit dialogs);
  **bottom-sheet anchored at mobile** (`items-end`, `p-0`), centered with
  1rem padding at `md:`. Outside-click closes (measured).
- **Panel**: `bg-white rounded-t-3xl md:rounded-2xl shadow-2xl max-w-lg
  w-full max-h-[85vh] overflow-y-auto` — 512px max-width at desktop
  (`max-w-lg`, NOT the edit dialogs' 42rem), radius 24px top-only at
  mobile / 16px at desktop, `shadow-2xl` (`rgba(0,0,0,0.25) 0 25px 50px
  -12px`), 85vh max-height. Measured mobile: x=0, w=390 (full width),
  bottom-anchored.
- **Header**: `sticky top-0 bg-white border-b px-6 py-4 flex
  items-center justify-between rounded-t-3xl md:rounded-t-2xl` — H2
  "Budget Item Details" (`text-lg font-bold`, forest-dark) + the 36×36
  X close (the v27 ghost-icon family: `focus-visible:ring-1
  hover:bg-accent hover:text-accent-foreground` — the clone's
  `DialogCloseButton` already carries it exactly).
- **Body** (`p-6 space-y-6`):
  1. **Summary block** (`text-center pb-6 border-b`): a badge row
     (`flex items-center justify-center gap-2 mb-3`) with the TYPE badge
     (`inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs
     font-medium`, bg = type color at 12.5% alpha, text = type color) and
     the CLASSIFICATION badge (same base + `border`, bg = per-cls tint,
     text = per-cls color, a 12px cls icon); the name H3 (`text-2xl
     font-bold mb-2`, forest-dark `#1a3a2e`); the amount P (`text-4xl
     font-bold mt-4`, the TYPE color).
  2. **Classification block** (`p-4 rounded-xl`, bg = per-cls tint): a 20px
     cls icon + title (`font-semibold mb-1` text-[16px], per-cls color) +
     description (`text-sm`, gray-500 `#6b7280`).
  3. **Facts list** (`space-y-4`): rows `flex items-center gap-3 py-2` — a
     16px lucide icon (gray-500) + label (`text-xs` gray-500) + value
     (`font-medium` 16px forest-dark): Date (CalendarIcon, "October 9,
     2026" long-form), Frequency (RepeatIcon), Recurring (No/Yes — English
     word, not boolean), Status (capitalized), **Notes (CONDITIONAL — only
     when the item has notes)**.
  4. **Meta footer** (`pt-4 border-t` > `grid grid-cols-2 gap-4 text-xs`):
     Created + Last Updated — label (`mb-1` gray-500 12px) over value
     (`font-medium` forest-dark 12px, "Oct 9, 2026" short-form).
- **Type color map** (badge bg = color/12.5%, badge + amount text = color):
  income `#8fbc3f` (COLORS.limeGreen), expense `#e07a3b`
  (COLORS.orangeDark), savings `#3b7ea1` (COLORS.blueMedium) — the clone's
  existing `TYPE_COLORS` map is EXACTLY this.
- **Classification map** (block bg / title+badge color / icon): need
  `#fff7f5` / `#e07a3b` / circle-alert; want `#f0f7fb` / `#3b7ea1` /
  heart; savings `#f5f9f0` / `#8fbc3f` / piggy-bank — the same tint/color
  pairs as the clone's `GUIDELINE_ROWS` (which already carries these
  bgColors/colors); the DESCRIPTIONS are a separate copy map: need
  "Essential expenses like rent, utilities, and groceries" (note the
  ", and"), want "Discretionary spending like entertainment and dining
  out", savings "Savings, investments, and future planning" (≠ the
  guidelines' "Emergency fund, retirement, investments").
- The clone's data model already carries every field the sheet reads
  (`type`, `classification`, `category`, `amount`, `frequency`, `date`,
  `recurring`, `status`, `notes?`, `createdAt`, `updatedAt` —
  `src/lib/types.ts`).

### G1. [MED] The card badges' hover/transition family — add the reference's tint

All four card badge variants (classification, frequency, Recurring,
status) on the reference carry `transition-colors
hover:bg-secondary/80`; on a REAL CDP hover they tint to
`rgba(245,245,245,0.8)` over 150ms. The clone's badges were static.

**Fix (executed — `src/components/budget/item-card.tsx`, the four badge
class strings at ~lines 148–172 + one rule in `src/app/globals.css`):**
each badge gained `transition-colors zb-badge-hover`, where `.zb-badge-hover:hover`
pins `background-color: rgba(245, 245, 245, 0.8)` in globals.css. The
direct `hover:bg-secondary/80` utility was tried first and LIVE-verified
— it computes to **`lab(96.5375 0 0 / 0.8)`** on the clone (the Tailwind
v4 oklab drift, the v7 G6 lesson: the reference renders plain
`rgba(245, 245, 245, 0.8)`), so the computed value is pinned through the
custom class exactly like the overlay/border pins before it. The
clone's `--color-secondary: #f5f5f5` matches the reference's tint base.
The reference's inert focus classes (`focus:outline-none focus:ring-2
focus:ring-ring focus:ring-offset-2`) are NOT added — non-focusable
spans render nothing on both sites (the v13 tag-difference precedent:
rendered parity is the bar).

### G2. [LOW-MED] The expense-card footer Edit/Calculate buttons' keyboard family

The reference's Edit button carries the shadcn outline-variant base
(`focus-visible:outline-none focus-visible:ring-1
focus-visible:ring-ring` + `border border-input
hover:text-accent-foreground h-8 rounded-md px-3 text-xs bg-white
shadow-md hover:bg-gray-50`) and the Calculate carries the same focus
family (its own orange hover). On a REAL 12-stop Tab walk the reference's
buttons render `rgb(10,10,10) 0 0 0 1px` + the shadow-md ambient; the
clone's hand-written strings (v9-era, like the v27 X-close) carry NO
focus family at all — on the same walk the clone renders the **UA
default outline** (`outline: auto 1px lab(...)` — a different visible
indicator) with no ring layer.

**Fix (`src/components/budget/item-card.tsx`, the two class strings at
~lines 87 and 96):** add `focus-visible:outline-none
focus-visible:ring-1 focus-visible:ring-ring` to BOTH buttons and
`hover:text-accent-foreground` to the Edit (the reference's Calculate
keeps its orange text on hover — no hover-text class). The rest geometry
(77×32 vs the clone's 75×32 — 2px of text-metric slack, the hover bg
pins `#f9fafb`/`#fff7ed`, the orange border) is already pinned and
untouched.

### G3. [HIGH — the headline] The Budget Item Details dialog — build the missing surface

The reference's card click opens a read-only details sheet (the full
measured contract above); the clone's card click is dead. This is the
largest functional parity gap found since the v16 boot-state work — a
whole user-facing surface, not a class drift.

**Fix (three files, following the established modal pattern):**

1. `src/components/budget/store.ts` — add the modal slot:
   `details: { item: BudgetItem } | null` to `ModalState` +
   `openDetails`/`closeDetails` actions (the same shape as the
   calculator slot).
2. `src/components/budget/item-details-dialog.tsx` — NEW component: the
   overlay/panel geometry (bottom-sheet at mobile, centered 512px at
   desktop), the sticky header + `DialogCloseButton`, the summary /
   classification / facts / meta blocks per the measured contract,
   reusing `DialogCloseButton`, `TYPE_COLORS`, the classification
   tints/icons from `item-card.tsx`'s existing maps, and a NEW
   details-description copy map. Radix `DialogPrimitive` root/portal
   wired through the store's `modal.details` slot (Escape + overlay
   click close for free — the reference's outside-click measured closing;
   Escape is the standing clone superset).
3. `src/components/budget/item-card.tsx` — wire the card container's
   `onClick={() => openDetails(item)}` (the card already renders
   `cursor-pointer`; the inner action buttons stopPropagation so
   Edit/Calculate/ellipsis still work — the reference's same
   nesting: card-click → details, button-click → its own action).
4. `src/components/budget/app-shell.tsx` — mount
   `{modal.details && <ItemDetailsDialog key="details" />}`.

## Validation of this plan against the codebase

- The badge class strings: `rg 'inline-flex items-center rounded-md
  border' src/components/budget/item-card.tsx` returns exactly the four
  badge sites (lines ~148–172) — the classification chip, the frequency
  chip, the Recurring chip, the status chip. No other component renders
  these card-badge strings (the dashboard's guideline tiles use
  GUIDELINE_ROWS' own classes; the dialogs' badges are separate surfaces
  with their own pins).
- The Edit/Calculate class strings: `rg 'hover:bg-\[#f9fafb\]' src/`
  returns exactly one hit (the Edit); `rg 'hover:bg-\[#fff7ed\]' src/`
  exactly one (the Calculate). The buttons' rest-state pins
  (border-input, #fed7aa, text-[#ea580c], shadow-md, h-8 px-3 text-xs)
  are asserted by the existing items spec (`expense cards carry the
  hover-revealed Edit and Calculate buttons`) — the new assertions are
  additive.
- The modal pattern: `ModalState` has five slots, `app-shell.tsx` mounts
  five dialogs via the store — the details slot is the sixth, same shape
  (`{ item: BudgetItem } | null` mirrors `calculator`).
- The data model: `rg 'createdAt|updatedAt|notes' src/lib/types.ts` —
  every entity already carries all three; the Prisma schema timestamps
  exist (the API serializes them — the store's items carry them after
  refresh).
- The X close: `DialogCloseButton` (dialog.tsx) carries the v27-pinned
  family verbatim — reuse as-is (the reference's details X carries the
  identical base, measured this session).
- The overlay/panel: `.zb-modal-overlay` already pins the exact overlay
  color + blur; the DETAILS panel needs its own geometry (NOT
  `.zb-modal-panel` — 42rem centered always; the details is `max-w-lg`,
  85vh, bottom-sheet at mobile) — implemented as the reference's own
  class string on the Radix Content.
- No existing spec covers the card-click surface: `rg 'click.*card|card
  click|Details' tests/e2e/*.spec.ts` returns nothing for the item-card
  body click (the items specs interact via the buttons and dialogs).
- The e2e cost: G1+G2 extend the existing items spec (no new page flows);
  G3 adds ONE new spec file (one login, seeded fixtures, the
  open→assert→close round-trip) — the suite grows 155 → ~158.

## Execution order (TDD)

1. **RED (G1+G2)**: extend the items spec's expense-card tests with the
   class-attribute assertions — the badges carry `hover:bg-secondary/80`
   + `transition-colors`; the Edit/Calculate carry
   `focus-visible:ring-1` (NOT ring-2) and the Edit carries
   `hover:text-accent-foreground`. Run → RED (the current classes lack
   all of them).
2. **G1+G2 fixes**: the class-string edits in `item-card.tsx`. Run →
   GREEN.
3. **Pin-sanity (G1+G2)**: mutate one expectation each (drop
   `hover:bg-secondary/80`, flip ring-1 → ring-2) → FAIL → restore.
4. **RED (G3)**: new `tests/e2e/item-details.spec.ts` — the card click
   opens the sheet; the header/badges/name/amount/classification/facts/
   meta assertions (classes + computed colors); the X closes; the seeded
   Rent item's exact fact values. Run → RED (no dialog exists).
5. **G3 build**: the store slot, the component, the card onClick, the
   app-shell mount. Run → GREEN.
6. **Pin-sanity (G3)**: mutate the amount-color and one fact expectation
   → FAIL → restore.
7. Full clean-check chain: `npm run lint && npm run typecheck && npm
   test && npm run build && npm run test:e2e` + `bash
   scripts/smoke-test.sh` (~158 e2e expected).
8. Live re-verification on the :3200 parity server: the card click opens
   the details sheet on the clone; the badges tint under a real CDP
   hover; the Edit's real-Tab ring reads 1px #0a0a0a.
9. Regenerate the screenshots (`node scripts/capture-screenshots.mjs`) —
   the app-view captures are pixel-stable (the details sheet only opens
   on click; consider adding a details-sheet capture if the script's
   flow allows). Align README/CLAUDE/AGENTS/SKILL/session log/worklog +
   the probe README (the v28 catalog).

## Risk notes

- G1's hover tint applies to ALL item cards' badges (income, savings,
  expense) — the same measured family on every view (the reference's
  income and savings cards carry the identical base, verified).
- G2 touches two buttons with existing e2e pins (the rest-state classes
  are asserted — additive assertions only; the rest geometry is
  untouched).
- G3 adds ONE new interactive surface; the card's existing children
  (buttons, dropdown triggers) must stopPropagation to keep their own
  actions — the reference's nesting works the same way (measured: the
  card click opens details; the action buttons act). The details sheet
  is READ-ONLY (no form state, no API calls — zero data risk). The
  mobile bottom-sheet uses the reference's exact class family
  (`items-end md:items-center` on the overlay + `rounded-t-3xl
  md:rounded-2xl`), which coexists with the Radix portal (the sheet's
  mobile-nav sibling already proves the pattern).
- No API, store-data, or schema changes — G3 reads fields the store
  already holds; G1/G2 are pure class strings.
