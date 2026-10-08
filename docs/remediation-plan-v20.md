# Remediation Plan v20 — Session-39 Parity Iteration

Date: 2026-10-09 · Scope: fresh two-site re-audit after the v19 baseline
(`365f2a4` / v19 code `d3528fd`, all green) — the workspace was RESET this
session (fresh `git clone`, `.env` + `db/` + node_modules rebuilt, the
standing brief requirements re-verified: `DATABASE_URL="file:../db/custom.db"`
with `db/` at the repo root, `db:push` + `db:seed` run, the Vitest +
Playwright configs intact in the repo). Baseline chain at `365f2a4` fully
green BEFORE any work: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ ·
135/135 e2e ✓ (first full run, no flakes) · 30/30 smoke ✓. Probes: one-shot
`agent-browser eval` scripts, sessions `ref22`/`clone22` desktop 1280×800 +
390×844 (resized per check), the standalone parity server on :3200 booted
per command through `scripts/with-server.sh`, and the **VLM visual sweep**
(`z-ai vision` pairs + a mechanical pixel-diff layer, per the v19
methodology).

This pass swept the surface classes the session-38 log flagged as the next
tier — the **MOBILE APP VIEWS** at 390×844 (the v19 sweep covered auth
only at mobile) and the **POPULATED EDIT DIALOGS** (the v19 sweep compared
the EMPTY add dialogs) — plus the breakdown drill-down expanded rows (the
third suggestion), the standing task-focus re-verification (mobile
navigation R1–R4 + reference data-drift check), and the code audit
(`skills/code-review-and-audit` native-CLI fallback: lint/tsc/tests green;
`npm audit` = the same 5 dev-only ESLint `braces` advisories, no patched
release — accepted, unchanged; secret-pattern scan clean; the pulled v19
changeset re-verified in the code first).

## The sweep — method and results

Ten mobile screenshots (5 views × 2 sites: dashboard, income, expenses,
savings, net worth at 390×844), one populated-edit-dialog pair (the
reference's Netflix item vs the clone's first seeded expense, both at
1280×800), and one breakdown drill-down pair (Income section + Salary
category expanded, both sites), compared pairwise through `z-ai vision`
with layout-focused prompts (data differences excluded by instruction).

- **Mobile dashboard: IDENTICAL.** The clone's header row (chip + Add Item
  button at 127×36, `items-start` + `mb-8` — the CORRECT reference pattern)
  and the stacked 1-col quick-action grid (363/358×90 — the 5px difference
  is the reference's own 395px overflow) both match.
- **Mobile items views (income/expenses/savings): ONE REAL DRIFT (G1).**
  The VLM flagged the Add button as full-width on the clone vs
  left-aligned-narrow on the reference — DOM-verified on all three views:
  the reference's header row runs `flex flex-col md:flex-row
  justify-between items-start md:items-center gap-4 mb-8` while the clone's
  runs `mb-6 flex flex-col gap-4 md:flex-row md:items-center
  md:justify-between` — the missing base `items-start` lets the flex-col
  cross-axis STRETCH the button to 358px (the reference's auto-width:
  147 "Add Income" / 155 "Add Expense" / 150 "Add Savings"), and the
  `mb-6`-vs-`mb-8` margin drifts the header→filter-card gap 24 vs 32px —
  at BOTH viewports (desktop nextTop 116 vs the reference's 124). The
  clone's own DASHBOARD header row already carries the correct pattern
  (`mb-8 … items-start`), so this is an items-view-local drift, never
  caught because no spec ever pinned the mobile stacking of that row (the
  v4-era pins measured the button chrome, not its width; the desktop
  flex-row renders both sites' buttons at the same 147×36).
- **Mobile net worth: all five VLM flags are the DOCUMENTED superset fix
  #4 manifestations** (the reference's own 464px overflow: its fixed
  `text-5xl` 48px net figure, its 2-col Assets/Liabilities summary grid,
  its Add Asset button pushed to x=314 → half off-screen) plus one
  hallucination refuted in the DOM (the "pronounced green" Assets tab —
  both sides compute the identical `rgb(220, 252, 231)` active tint).
  No action: the clone intentionally trades the reference's broken 464px
  layout for the 390px fit (superset fix #4, test-pinned).
- **Populated edit dialogs: ONE REAL DRIFT (G2).** The VLM flagged the
  classification radios as "icons inside the radio buttons (circle, heart,
  leaf)" on the reference — DOM-verified: the reference's classification
  tile LABELS carry 16px lucide icons between the radio and the text —
  need → `lucide-circle-alert` colored `rgb(224, 122, 59)` (#e07a3b, the
  expense accent), want → `lucide-heart` `rgb(59, 126, 161)` (#3b7ea1),
  savings → `lucide-piggy-bank` `rgb(143, 188, 63)` (#8fbc3f) — the same
  icon family the donut legend already renders. Present in BOTH the Add
  (empty) and Edit (populated) dialog states — the v19 empty-dialog sweep
  simply missed them (full-page pairs at dialog scale; the fresh
  populated-state pair caught what the empty pair didn't). The clone's
  tiles render [radio + span] with no icon. The VLM's other two flags were
  refuted in the DOM (the X-close "boxed" claim — both sides measure the
  identical 36×36, 0px border, transparent bg, 16px `#0a0a0a` lucide-x;
  the subcategory-subtitle and payment-method card claims — data-driven,
  the reference's own Netflix card renders its "Streaming" subcategory
  line identically and its items carry no payment-method values).
- **Breakdown drill-down (expanded): clean.** The only VLM flags are the
  known Dashboard active-nav highlight (superset #3) and the avatar letter
  (data) — the expanded rows themselves layout-identical.
- **Badge-wrap mechanism: identical** (both sites `flex flex-wrap gap-2
  mb-3`, wrap + 8px gap; the clone's screenshots wrap only because its
  seed items carry 4 badges vs the reference's 2 — data-driven).

The mobile-navigation stack (the task focus) was re-verified end-to-end
first: R1 (the reference's TWO toast containers still intercept the
burger's center hit at (38,30) — the synthetic-event dispatch needed to
drive the reference's own burger; the clone's hit is DIRECT on the svg;
burger 28×28 at (24,16) both), R2 (tapping Income in the reference's sheet
navigated to `/income` with `sheetStillOpen: true` + overlay 1 — the trap
bug live; the clone's sheet CLOSED + 390px fit; sheet 288px + link
geometry (20,185) 247×32 identical), R3 (no reference link active on `/` —
all five rail links `rgb(63,63,70)`/400, no `<nav>` landmark; the clone
highlights Dashboard — white + gradient + 500 + landmark), R4 (reference
scrollWidth 395 on `/` + `/dashboard`, 464 on `/networth`; clone 390 on
ALL six routes). The Tailwind v4 pins hold. Data drift clean — FOURTEENTH
consecutive check (allocation 30.5%, income `$5000.00`/1 item, savings
`$1000.00`/1 item, expenses `$525.00`/4 items, Balance `$3475.00`; the
census needed an ASCII-safe rewrite this pass — the v19 probe's literal
"·" separator gets mangled by the base64→atob→eval transport into two
Latin-1 chars and never matched; `probe-census-v20.mjs` builds it from
`String.fromCharCode(0xb7)`).

The audit found **2 clone-side finding groups** (G1, G2); no new reference
bugs (the reference's silent failures ARE the parity target's behavior —
the clone keeps the surfaces and adds honest feedback, the established
superset class).

---

## Findings ledger

### G1. [MED] the items-view header row drifts from the reference on two measured axes (Add-button width at mobile, header→filter margin at both viewports)

Found by the mobile VLM sweep ("the Add button is full-width on the
clone"), then DOM-verified on all three items views (income/expenses/
savings at 390×844 + income at 1280×800):

| Property | Reference | Clone (pre-fix) |
|----------|-----------|-----------------|
| Row class | `flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-8` | `mb-6 flex flex-col gap-4 md:flex-row md:items-center md:justify-between` |
| Add button @390 | **147 / 155 / 150 px** (auto-width — `items-start` blocks the cross-axis stretch) | **358 px** (full-width stretch) |
| Add button @1280 | 147×36 at (1101,44) — identical both | 147×36 at (1101,44) ✓ |
| Button height/position | 36px, y=153 @390 / y=44 @1280 | identical ✓ |
| Header→filter gap | **32 px** (`mb-8`) — both viewports (nextTop 124 @1280, 221 @390) | **24 px** (`mb-6`) — (nextTop 116 @1280, 213 @390) |
| Heading block + count | x=16 both, same fonts | identical ✓ |

Why every prior probe missed it: the v4-era header pins measured the
DESKTOP flex-row (where both sites render the button at the same
147×36) and the v11 pins measured the BUTTON's own chrome (shadow/icon/
focus ring) — no spec ever pinned the row's mobile stacking (the
cross-axis stretch) or its bottom margin. The clone's DASHBOARD header
row (measured in the v3/v4 era) already carries the correct pattern
(`mb-8 … items-start`), so the fix is a one-line class alignment on the
items views' row.

Fix (one file, `src/components/budget/items-view.tsx`):

- Align the header row's class to the reference's: add base
  `items-start` (kills the mobile stretch; `md:items-center` already
  overrides at md) and change `mb-6` → `mb-8` (the 32px gap, both
  viewports). Keep `justify-between`/`gap-4` (the reference carries both;
  base `justify-between` is harmless in the flex-col stacking and matches
  the reference's own class list).

Pinned by a NEW test in `tests/e2e/mobile-layout.spec.ts` (the
mobile-geometry home): open `/income` at 390×844, assert the Add button's
computed width is auto-width (< 200px — the stretched state measures 358)
and the header row's computed `margin-bottom` is 32px — RED at the
pre-fix state, GREEN after. A desktop companion assertion (the gap at
1280) joins the same test's evaluate to pin both viewports.

### G2. [MED] the budget-item dialog's classification tiles lack the reference's 16px lucide icons

Found by the populated-edit-dialog VLM sweep ("icons inside the radio
buttons — circle, heart, leaf"), then DOM-verified in BOTH dialog states
on the reference (the Add Income dialog and the Edit Budget Item dialog):

| Tile | Reference icon | Color (computed) |
|------|----------------|------------------|
| Need | `lucide-circle-alert` w-4 h-4 (16px) | `rgb(224, 122, 59)` = #e07a3b |
| Want | `lucide-heart` w-4 h-4 (16px) | `rgb(59, 126, 161)` = #3b7ea1 |
| Savings | `lucide-piggy-bank` w-4 h-4 (16px) | `rgb(143, 188, 63)` = #8fbc3f |

The icons sit INSIDE the tile's label between the radio and the text
(the reference's label: `svg + span`), colored by the per-classification
accent — exactly the tile accents the clone already ships in
`CLASSIFICATION_TILES` and the same icon family the dashboard's donut
legend renders (`LEGEND_ICONS`: piggy-bank/heart/circle-alert,
`dashboard-view.tsx`). The clone's tiles render `[RadioGroupItem +
span]` with no icon.

Why every prior probe missed it: the v9 tile pins measured the tile
GEOMETRY (52px, `leading-none`) and the v6 pins measured the selected
border/tint — no spec ever asserted the tile's child inventory. The v19
VLM empty-dialog sweep compared full-page pairs at dialog scale and
missed the icons (a screening-layer miss the populated-state pass
caught — the exact class of gap the session-38 "populated EDIT dialogs"
suggestion predicted).

Fix (one file, `src/components/budget/budget-item-dialog.tsx`):

- Import `CircleAlertIcon`, `HeartIcon`, `PiggyBankIcon` from
  `lucide-react` (the same imports the dashboard view uses).
- Add a local `CLASSIFICATION_ICONS` map (need → CircleAlertIcon,
  want → HeartIcon, savings → PiggyBankIcon).
- Render the icon between the `RadioGroupItem` and the label span at
  `h-4 w-4` with an inline `color` style from the tile accent
  (`CLASSIFICATION_TILES[c].accent` — #e07a3b/#3b7ea1/#8fbc3f, the
  measured values; inline rgb per the v4 lab-drift doctrine: never a
  named palette class on a parity surface).

Pinned by a NEW test in `tests/e2e/dialog-buttons.spec.ts` (the dialog
chrome home, beside the existing 52px-tile test): open the Add Item
dialog, assert each tile label contains exactly one svg whose class
carries the measured lucide name and whose computed color matches the
per-classification accent — RED at the pre-fix state, GREEN after.

### Observations (documented, no action)

- **The mobile VLM sweep's networth flags are all superset fix #4** —
  the reference's own 464px overflow manifests as its fixed 48px
  `text-5xl` net figure, its 2-col summary grid (the clone's responsive
  `text-2xl`/1-col stack is the documented no-overflow superset), its
  tablist stretched to 212px-per-tab (the clone's 175), and its Add
  Asset button half off-screen (x=314 + w=134 > 390). Not drift — the
  intended superset behavior, test-pinned since v4.
- **One VLM hallucination refuted by measurement** (the "pronounced
  solid light-green" Assets tab: both sides compute `rgb(220, 252,
  231)`) — the lesson-37 discipline (the VLM is a screening layer;
  computed styles are ground truth) holds for the mobile sweep too.
- **The reference's Netflix card renders its subcategory line**
  ("Netflix / Streaming / $200.00") exactly like the clone's cards; its
  items carry no payment-method values, so its cards show no
  payment-method label — the clone's "Credit Card" labels are
  data-driven, mechanism-identical.
- **The X-close button is identical on both sides** (36×36, 0px border,
  transparent bg, 16px svg in `rgb(10, 10, 10)`) — the VLM's "boxed X"
  flag refuted.
- **The census probe's transport bug**: the v19 file's literal "·"
  (U+00B7, UTF-8 C2 B7) becomes TWO Latin-1 characters through the
  base64→`atob`→`eval` transport, so its regex never matched the DOM
  text (empty counts — also explains why the v19 session needed a
  "mid-pass fix"). `probe-census-v20.mjs` builds the separator from
  `String.fromCharCode(0xb7)` (ASCII-only source — transport-proof).
  The drift data itself was unaffected: the 13 prior checks used the
  manual probe path.
- **The reference data state remains unchanged since session 19**
  (fourteenth consecutive clean drift check).

### Verified matching this pass (no action)

Mobile navigation R1–R4 (both sites, the task focus — details above);
the mobile dashboard view (chip + header row + quick-action grid); the
breakdown drill-down expanded rows (Income + Salary levels); the badge
wrap mechanism (`flex flex-wrap gap-2 mb-3`); the classification tile
geometry (197×52, border-2, per-type hover borders, selected accent +
tint); the dialog X-close chrome; the networth tab header row
(`flex justify-between items-center`, gap 24, Add Asset 134×36).

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | G1: pin the reference's header-row geometry — RED spec first | `tests/e2e/mobile-layout.spec.ts` NEW "the items-view Add button is auto-width and the header gap is 32px (v20 G1)" — open `/income` at 390×844, read the Add button's computed width + the header row's margin-bottom (and the filter card's offset): assert width < 200 (the stretched state measures 358) and margin-bottom 32; run RED at the pre-fix state (both assertions fail) | — |
| 2 | G1: fix the row (base `items-start` + `mb-8`) — GREEN | the RED spec flips green; the desktop geometry re-pinned by the same test's 1280×800 evaluate (gap 32 at both viewports) | `src/components/budget/items-view.tsx` (row class) |
| 3 | G2: pin the reference's tile icons — RED spec first | `tests/e2e/dialog-buttons.spec.ts` NEW "classification tiles carry the reference's 16px lucide icons (v20 G2)" — open the Add Item dialog, per tile: assert one svg with the measured lucide class fragment (circle-alert/heart/piggy-bank) and the computed color per accent (#e07a3b/#3b7ea1/#8fbc3f); run RED (svg count 0) | — |
| 4 | G2: render the icons (map + inline accent colors) — GREEN | the RED spec flips green; the existing 52px-tile and v9 radio pins re-run untouched (the icons add height-neutral inline children) | `src/components/budget/budget-item-dialog.tsx` (icon imports + map + tile children) |
| 5 | Regression: full chain + live parity re-check (both fixed surfaces re-measured against the reference side-by-side; the mobile app-view + populated-edit-dialog screenshot pairs regenerated and re-compared through the VLM) + screenshot refresh (the mobile items-view shots + the dialog shots will change; the other shots should be pixel-stable) | — | — |
| 6 | Docs: session log (`docs/session_40.md` — the session_39.md slot holds the incoming session-37 conversation summary), worklog, README/CLAUDE/AGENTS/SKILL alignment (counts, the v20 pin paragraphs, the mobile-sweep + populated-dialog methodology note, the census transport lesson), probe README v20 rows | — | docs |

## Regression pin map (must NOT change)

- All six superset fixes (hamburger hit, sheet close-on-nav, root-URL nav
  highlight — rail AND sheet, no mobile overflow — the networth
  responsive summary stays, Escape close, delete confirmations) and the
  v9–v19 pins (donut geometry + tooltip, tab icons + header chip, banner
  chrome, titles, placeholders, focus rings, the full-page loading state,
  the boot data-failure tier, the calculator error tier, the net-worth +
  item-card delete error tier, the route-announcer spec discipline, the
  recurring row's switch-left tinted layout)
- The Add-button chrome pins (v11: 16px Plus icons, v3 bare-shadow
  ambient, no hover fade; the `.zb-btn-add` family) — the G1 fix changes
  only the ROW class, never the button's own
- The tile geometry pins (52px `leading-none` tiles, per-type hover
  borders, selected accent + tint, the v9 radio primitive #171717
  family) — the G2 fix inserts a height-neutral icon child; the tile's
  flex row absorbs it without a height change (16px icon < 14px-text +
  radio row height; the reference's tiles measure 52 both)
- The dialog's other rows (Payment Method, Status, Notes — untouched);
  the recurring row (v19 — untouched); the footer geometry (flex-1
  Cancel/Save); the X-close chrome
- e2e fixture discipline: both new specs only READ (open the view /
  dialog, compute styles, Escape to close) — no fixture restore needed
