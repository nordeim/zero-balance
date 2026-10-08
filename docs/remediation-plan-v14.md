# Remediation Plan v14 — Session-27 Parity Iteration

Date: 2026-10-08 · Scope: fresh two-site re-audit after the v13 baseline
(`931bfcd` / code `8b634fe`) re-verified green (lint · typecheck · 96/96
unit · build · 115/115 e2e — one known not-found navigation flake, clean
in isolation · 30/30 smoke). Probes: one-shot `agent-browser eval` scripts,
sessions `ref15`/`clone15` desktop 1280×800 + `ref15m`/`clone15m` 390×844,
the standalone parity server on :3200 booted per command through
`scripts/with-server.sh` (recreated this session; the sandbox still reaps
background processes between tool calls while the agent-browser daemon
persists).

This pass swept dimensions no earlier pass had measured, led by a
**three-page VLM screenshot comparison** (dashboard / expenses / networth)
whose flagged diffs were each verified in the DOM — most were refuted
(data-driven badge wrap + payment-method footers, the intentional
`--color-border` token, VLM misreads of the identical active-tab tint and
ratio icon), but three surfaced as real clone-side gaps: the **donut hover
tooltip's value format** (never hovered before), the **net-worth tab
icons** (the v5 tab pin measured text/geometry/colors but never icon
presence), and the **net-worth page header's gradient icon chip** (the
items-view chips were pinned in v4; the net-worth header was never
measured). Also swept first-time: the net-worth **tablist keyboard flow**
(roles, aria-selected, ArrowRight/ArrowLeft activation — identical), the
**dialog initial-focus position** (the ref leaves focus on the trigger
button — an a11y gap the clone's Radix focus trap deliberately supersedes),
**field-level validation on invalid input** (negative amount → silent
rejection, both sides, no error text either), **guideline-row + accordion
section-button hover states** (none on either side), a **user-select
sweep** (auto everywhere), and the **dialog input census + payment-method
footer behavior** (identical; the ref's items simply carry no payment
methods in data).

The mobile-navigation stack (the task focus) was re-verified end-to-end
first (R1/R2/R3/R4 all still live on the reference; all six clone superset
fixes intact), and the reference data-drift check ran clean (unchanged
since session 19: allocation 30.5%, income `$5000.00`/1 item, savings
`$1000.00`, expenses `$525.00`; clone seed arithmetic intact at
`+$2065.00` / 62.8%). The code audit re-ran clean: `npm audit` = 5 high,
all the dev-only ESLint `braces` chain (GHSA-vfj7-8cjw-p6xm, no patched
release — accepted, documented); secret-pattern scan clean.

The audit found **3 clone-side finding groups**; no new reference bugs.

---

## Findings ledger

### G1. [MED] Donut hover tooltip: raw value AND default chrome drift from the reference

Measured live on the reference (dispatching pointer events on the first
`.recharts-pie-sector`): the recharts DEFAULT tooltip renders
`recharts-default-tooltip` whose item row reads **"Need : $6025.00"** —
label, " : " separator, and a value formatted with the dollar sign and two
decimals. The full chrome: padding 10, bg white, border 1px
rgb(229,231,227) (#e5e7e3 — the reference's CARD token), radius 8, shadow
`rgba(0,0,0,0.1) 0 4px 12px`, item row BLACK (#000) 16px/400 (the
recharts-2 default item color).

The clone (recharts 3) drifted on FOUR axes: the value rendered the raw
number ("7370" — no `<Tooltip />` formatter); the border defaulted to
`#cccccc`; there was NO radius and NO shadow; and the item row rendered in
the SECTOR's fill color (orange) instead of black (recharts 3 changed the
default item color to the series fill).

Fix: pin all four —
`formatter={(v) => \`$${Number(v).toFixed(2)}\`}` (the dashboard's plain
money convention — no thousands separator, measured "$6025.00"),
`contentStyle={{ borderRadius: 8, borderColor: "#e5e7e3", boxShadow:
"rgba(0,0,0,0.1) 0px 4px 12px" }}`, and `itemStyle={{ color: "#000000" }}`.

Fix files: `src/components/budget/dashboard-view.tsx` (line ~591).

### G2. [LOW-MED] Net-worth tab triggers render text-only; the reference renders 16px lucide icons

Measured live on the reference (`[role="tab"]` on `/networth`): the
Assets trigger contains `<svg class="lucide lucide-circle-arrow-up w-4
h-4 mr-2">` and the Liabilities trigger `lucide-circle-arrow-down`, both
16×16, `stroke="currentColor" stroke-width="2"`, margin-right 8px — the
icons inherit the tab's text color (active green-900 `rgb(20,83,45)`,
inactive `rgb(115,115,115)`). The clone's `TabsTrigger`s render the bare
text (`net-worth-view.tsx` lines 340-341) — the icons were never measured
in the v5 tab pin (geometry/colors only).

Fix: render the icons inside the triggers —
`<TabsTrigger value="assets"><CircleArrowUpIcon className="h-4 w-4
mr-2" />Assets</TabsTrigger>` and the circle-arrow-down twin for
liabilities (both already imported in the file). Lucide's `currentColor`
default keeps the ref's color inheritance — no class changes needed on
the trigger.

Fix files: `src/components/budget/net-worth-view.tsx`.

### G3. [MED] Net-worth page header missing the 48×48 gradient icon chip

Measured live on the reference at BOTH viewports (desktop 1280×800,
mobile 390×844): the `/networth` page header is a `flex items-center
gap-3` row (310×60 at desktop) containing the 48×48 icon chip
(`linear-gradient(135deg, rgb(45,90,74), rgb(143,188,63))` —
forest-medium→lime, radius 12, flex-centered `lucide-trending-up` 24×24
`text-white`, stroke-width 2) followed by the h1+p block. The clone's
`net-worth-view.tsx` renders the h1+p bare — the header-icon family was
pinned for the ITEM views in v4 (`items-view.tsx`'s
`HEADER_CHIP_GRADIENTS[type]` chip) but the net-worth page's chip was
never measured. The reference renders NO chip on `/` (dashboard) — both
sides match there.

Fix: restructure the header block to the items-view pattern —
`mb-6 flex items-center gap-3` row → chip div
(`flex h-12 w-12 items-center justify-center rounded-xl`,
`background: linear-gradient(135deg, #2d5a4a, #8fbc3f)`) wrapping
`<TrendingUpIcon className="h-6 w-6 text-white" />` (already imported) →
div with the existing h1 + p.

Fix files: `src/components/budget/net-worth-view.tsx` (lines ~255-260).

### Observations (documented, no action)

- **Dialog initial focus (a11y superset, invisible)**: the reference's
  Add-Item dialog leaves `document.activeElement` on the "Add Income"
  TRIGGER button (no focus move, no trap — consistent with its
  no-Escape/no-overlay-click behavior, R5/R6). The clone's Radix dialog
  moves focus onto the 36×36 in-header Close button. Same class as the
  `aside` rail landmark and the autoComplete hints — the clone's behavior
  is the a11y superset; documented so a future pass doesn't "fix" it
  backwards.
- **Invalid input = silent rejection on both sides**: submitting the
  Add-Item dialog with amount `-50` keeps the dialog open with NO error
  text or toast on either site (v10's empty-submit finding extended to
  invalid values). The clone's zod rejects server-side with a field-level
  400 the dialog silently swallows — matching UX. No fixture residue
  (verified: no "Probe Negative" card on either side).
- **Net-worth summary-card chrome re-verified**: the ratio row's
  white divider (border-top 1px rgba(255,255,255,0.2)) exists on BOTH
  sides; the 32×32 `lucide-trending-up` corner icon is byte-identical.
  (The VLM flagged both as differing; DOM measurement refutes both.)
- **Expenses badge wrap + payment-method footers**: the clone's expense
  cards show 4 badges (wrapping to two rows) and payment-method footers
  because the SEED data carries recurring flags + payment methods; the
  reference's items don't. The ref renders payment methods too when
  present (its income card footer shows "Bank Account"). Data-driven, no
  action.
- **Tab border token**: the tab triggers' 0px border color computes
  rgb(229,229,229) (ref) vs rgb(229,231,227) (clone) — the documented
  intentional `--color-border` divergence; 0px width paints nothing.

### Verified matching this pass (no action)

Mobile navigation (task focus, both sites 390×844): R1 re-confirmed live
(the ref's TWO toast containers — both `fixed top-0 z-[100]` 390×32
`pe:auto` — intercept the burger's center hit at (38,30); the clone's hit
is DIRECT on the svg; burger 28×28 at (24,16) both). R2 re-confirmed
(tapping Income in the ref's sheet navigated to `/income` with
`sheetStillOpen: true`; the clone's sheet CLOSED + 390px fit). R3
re-confirmed (no ref link active on `/` — all five rail links
`rgb(63,63,70)`/400/none; the clone highlights Dashboard — white +
gradient + 500). R4 re-confirmed (ref scrollWidth 395; clone 390 on `/`
and `/income`). Sheet link geometry identical (Income at (20,185),
247×32, both).

Net-worth tablist (both sites): `[role="tablist"]` container, tab roles,
aria-selected true/false, tabIndex -1, 220×28 triggers at the same
offsets, active `rgb(20,83,45)` on `rgb(220,252,231)` fw 500 — and the
KEYBOARD flow identical (ArrowRight moves focus Assets→Liabilities AND
activates; ArrowLeft returns). Dashboard data state: reference unchanged
since session 19; clone seed intact. Dialog input census (10 inputs,
number-first, same placeholders). Donut sector fills (the pinned token
trio, 3 real sectors). Guideline/legend rows (tinted rgb(245,248,245),
no hover either side). Accordion section buttons (254×56, pointer,
#0a0a0a/400, 16px chevron, no hover). user-select auto everywhere.
Cursor sweep pointer/auto.

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | G1: donut tooltip value → "$X.XX" via the formatter | `dashboard.spec.ts`: NEW "donut hover tooltip formats the value (v14)" — dispatch pointermove/mouseover on the first `.recharts-pie-sector`, assert `.recharts-tooltip-item-value` reads `$7370.00` (the seed's Need slice) and the tooltip chrome (padding/border/radius) stays the recharts default | `dashboard-view.tsx` |
| 2 | G2: net-worth tab icons | `networth.spec.ts`: NEW "tabs render the reference's 16px icons (v14)" — each trigger contains its `lucide-circle-arrow-up`/`lucide-circle-arrow-down` svg at 16×16, `margin-right 8px`, stroke currentColor; the INACTIVE icon inherits rgb(115,115,115), the ACTIVE (after click) rgb(20,83,45) | `net-worth-view.tsx` |
| 3 | G3: net-worth header icon chip | `networth.spec.ts`: NEW "header renders the gradient icon chip (v14)" — the header row is `flex items-center gap-3`; the 48×48 chip (radius 12, `linear-gradient(135deg, rgb(45,90,74), rgb(143,188,63))`) wraps `svg.lucide-trending-up` at 24×24 white; the h1 sits 12px right of the chip; ALSO pin mobile 390px (chip 48×48 present, h1 to its right, no horizontal overflow) | `net-worth-view.tsx` |
| 4 | Docs: session log (`docs/session_28.md`), worklog, README/AGENTS/CLAUDE/SKILL alignment + probe README v14 rows + `scripts/with-server.sh` committed (the per-command parity-server wrapper, referenced by the probe README since v10) | — | docs, scripts |
| 5 | Regression: full chain + live parity re-check of the three fixed surfaces + screenshot refresh (expect the networth screenshots to change — the chip + tab icons are visible; dashboard/login shots byte-identical since the tooltip is hover-only) | — | — |

## Regression pin map (must NOT change)

- All six superset fixes (hamburger hit, sheet close-on-nav, root-URL nav
  highlight — rail AND sheet, no mobile overflow, Escape close, delete
  confirmations) and the v10–v13 sheet/banner/title/placeholder/focus-ring
  pins
- The v9 donut pins: sector fills + value-DESC order + `labelLine={false}`
  + the percentage labels — the G1 formatter only touches the tooltip
  VALUE, not sectors/labels
- The v5 tab pins: 220×28 trigger geometry, `grid w-full max-w-md
  grid-cols-2` list, active `#dcfce7`/`#14532d`, inactive
  muted-foreground — the icons are additive children inside the triggers
- The net-worth summary card family (gradient, ratio, divider, corner
  icon), the type-grouped tab content, and the mobile no-overflow pin
  (the chip adds 60px of header height, not width — the row wraps inside
  the content column)
- The items-view header chips (`HEADER_CHIP_GRADIENTS`) — untouched; the
  G3 chip reuses the same visual pattern with the summary gradient
- e2e fixture discipline: the G1 spec only hovers (no writes); G2/G3 are
  pure DOM reads — no fixture impact
