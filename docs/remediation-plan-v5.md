# Remediation Plan v5 — Session-8 Parity Iteration

Date: 2026-10-07 · Scope: fresh two-site re-audit of every surface against
the live reference (`https://zero-balance-4885a8f3.base44.app/`) at desktop
1280×800, intermediate widths (640/768/820/1024) and mobile 390×844, after
the v4 baseline (`e23d854`) re-verified green (typecheck · lint · 96/96
unit · build · 52/52 e2e · 30/30 smoke). Probe sources:
`scripts/parity-probes/probe-v5-*.mjs` + the shared `run-probe.sh` runner
(base64 → `eval(atob(...))`).

Status after the v4 remediation: nav geometry (32px `h-8`), the net-worth
summary card (2-col grid + ratio footer), mobile fit (`min-w-0` + responsive
figure), filter-aware header counts, hero/stat/donut/breakdown/quick-action
chrome, item cards/badges/footers, dialog panels/inputs/tiles, calculator
banner + gradients, mobile chrome + sheet + all four superset fixes — all
re-verified matching this pass. This iteration went DEEPER: it read the
reference's own `:root` tokens, leaf-audited text colors on every form
control, compared dialog action buttons, dropdown/select item states, focus
rings, hover-variant semantics and the responsive chrome map. It found
**10 clone-side finding groups** plus **2 new reference bugs** (R5/R6).

A note on method: several differences below are invisible or
near-invisible in isolation (1-3 sRGB units), but they are SYSTEMATIC —
the clone's neutral scale was built from zinc-ish hexes while the reference
uses shadcn's neutral scale, and Tailwind v4 emits some utilities in
`lab()`/`oklab()` where the reference emits plain rgb. The project's pinned
convention is engine-independent, computed-style parity — so they are fixed
at the token level, once, for every surface.

---

## Findings ledger

### G1. [MED] Neutral foreground token family is zinc-ish, reference is near-black

Measured on the reference's `:root` (its own CSS vars): `--foreground:
0 0% 3.9%` = **#0a0a0a**, `--accent-foreground` / `--secondary-foreground` /
`--card-foreground` / `--popover-foreground`: `0 0% 9%` = **#171717**,
`--sidebar-foreground: 240 5.3% 26.1%` = **#3f3f46** (zinc-700).

Clone tokens: `--color-foreground/-card-foreground/-popover-foreground/
-secondary-foreground/-sidebar-foreground: #3f3f3f`, `--color-accent-
foreground: #1a3a2e`.

Where it renders (measured live): select-trigger value text (ref
`rgb(10,10,10)` vs clone `rgb(63,63,63)`), dialog form labels (same),
dropdown menu item resting text (same), select options (same), and every
text node that inherits the body base. A systematic inherited-text sweep
(`probe-v5-inherited`) confirmed the reference NEVER renders its body base
color while the clone renders it on the select triggers and net-worth tabs.

Fix: `--color-foreground: #0a0a0a`; `--color-card-foreground /
--color-popover-foreground / --color-secondary-foreground: #171717`;
`--color-accent-foreground: #171717` (see G5); `--color-sidebar-foreground:
#3f3f46`.

### G2. [MED] Form-control border token is warm gray, reference is neutral

Reference `--input`/`--border`: `0 0% 89.8%` = **#e5e5e5**. Measured live on
the reference: select-trigger borders, dialog inputs, search inputs, the
dropdown-menu content border and the select-dropdown content border are all
`1px rgb(229,229,229)`. Its CARD borders are a different, custom warm gray
`#e5e7e3` — which the clone already matches via `--color-border`.

Clone: `--color-input: #e5e7e3` (and the popover contents route through
`--color-border`) — so every form control and dropdown is 2 units greener
than the reference.

Fix: `--color-input: #e5e5e5`; point the dropdown-menu and select content
borders at the input token. Keep `--color-border: #e5e7e3` (cards match).

### G3. [MED] Net-worth tab list: compact pill vs the reference's 2-col grid + green active state

Reference (measured): `TabsList` = `h-9 items-center justify-center
rounded-lg bg-muted p-1 text-muted-foreground grid w-full max-w-md
grid-cols-2` → a **448px-wide 2-column grid**, each trigger **220px**;
active trigger = `data-[state=active]:shadow data-[state=active]:
bg-green-100 data-[state=active]:text-green-900` → **#dcfce7 bg, #14532d
text**; inactive text `#737373`. TabsList bg = `#f5f5f5` (neutral-100).
Trigger base has NO `gap-1.5` and NO `[&_svg]` rules.

Clone: `inline-flex … mb-4` → a **168px pill** (triggers 70/90px); active =
`bg-white text-foreground` (white pill + gray text); base adds `gap-1.5`
+ `[&_svg]:size-4 [&_svg]:shrink-0`. The rendered vertical gap below the
list (24px) matches the reference, so `mb-4` stays.

Fix: `tabs.tsx` trigger → the reference's exact class set with pinned hex
(`data-[state=active]:bg-[#dcfce7] data-[state=active]:text-[#14532d]` —
arbitrary values, dodging the v4 oklch drift on green-100/900);
`net-worth-view.tsx` list → `grid w-full max-w-md grid-cols-2` (keep
`mb-4`); `--color-muted: #f5f5f5` (G8).

### G4. [MED] Dialog action buttons: ghost Cancel + solid-lime Save vs the reference's outline Cancel + per-dialog gradient Save

Reference (measured on Add/Edit budget-item, line-item and asset dialogs):

- **Cancel** (all): shadcn outline — white bg, `1px #e5e5e5` border,
  `#0a0a0a` text, `rounded-md` (6px), 500, h-36.
- **Save Item** (budget-item add+edit), **Save Asset** (and Liability):
  `linear-gradient(135deg, rgb(45,90,74), rgb(143,188,63))` — the
  forest→lime gradient, white text, 6px, 500, h-36.
- **Save Item** (line-item/calculator dialog): `linear-gradient(135deg,
  rgb(224,122,59), rgb(245,169,98))` — the ORANGE gradient.
- **Add First Item** (calculator empty state): outline — white bg, `1px
  #e5e5e5`, `#0a0a0a` text, 6px.

Clone: Cancel = ghost (transparent bg, gray-500 text, NO border,
`rounded-lg` 8px); every Save = `.zb-btn-primary` solid lime, 8px, 600;
`.zb-btn-add-outline` colors `rgb(31,41,55)` on `var(--color-border)`.

Fix: new `.zb-btn-outline` primitive (the reference's Cancel/outline
chrome, hover `#f5f5f5`); Save buttons move to the `.zb-btn-add` shape
(6px/500/h-9 — already the reference geometry) with the surface's gradient
via inline `background` (forest→lime for budget/asset/liability, orange for
line-item — both strings already in `ADD_BUTTON_GRADIENTS`); outline
variant's text → `#0a0a0a`, border → `#e5e5e5`. `.zb-btn-primary` becomes
unused and is removed.

### G5. [MED] Accent token: warm gray vs the reference's neutral-100 (menu hover, select highlight)

Reference: `--accent: 0 0% 96.1%` = **#f5f5f5**. Measured live: dropdown-menu
item hover bg `rgb(245,245,245)`; select highlighted item bg `rgb(245,245,245)`
with text `rgb(23,23,23)` (#171717 — their accent-foreground). Clone:
`--color-accent: #f0f2ee` (a warm gray-green) → menu hover and select
highlight render `#f0f2ee`; the select-highlighted text is forest.

Fix: `--color-accent: #f5f5f5` (+ `--color-accent-foreground: #171717`,
G1). The select/menu item classes route through the tokens, so no
component change needed.

### G6. [MED] Nav hover text: forest vs the reference's zinc-900

Reference inactive nav hover: bg `#f0fdf4` (green-50 — already matched) +
text `rgb(24,24,27)` = **#18181b** (their `--sidebar-accent-foreground:
240 5.9% 10%`). The class is the same on both sides
(`hover:text-sidebar-accent-foreground`); the clone's token is
`--color-sidebar-accent-foreground: #1a3a2e` (forest) — a visible hover-text
difference (dark green vs near-black). Resting text matches (both zinc-700;
the clone's renders from v4's lab form, same sRGB `rgb(63,63,70)`).

Fix: `--color-sidebar-accent-foreground: #18181b`. (Only the nav hover text
reads this token — verified by grep.)

### G7. [MED] Tailwind v4 media-gates hover variants — the reference (v3) does not

The built CSS wraps every `hover:` utility in `@media (hover: hover)`. The
reference's v3-era engine emits plain `:hover` — so on any `hover: none`
device (touch laptops, phones with stylus, accessibility settings) the
reference still shows hover tints while the clone shows none. Measured in
a `hover: none` session: the clone's nav hover computes transparent while
the reference computes green-50.

Fix: pin the v3 semantics in `globals.css` right after the imports:
`@variant hover (&:hover);` — every hover utility then applies regardless
of device capability, exactly like the reference engine. (Also makes
headless parity probes consistent.) Pinned by a spec that emulates an
iPhone (hover: none) and asserts the nav tint still applies.

### G8. [LOW] muted/secondary tokens: zinc-100 vs neutral-100

Reference `--muted`/`--secondary`/`--accent`: `0 0% 96.1%` = **#f5f5f5**.
Clone: `#f4f4f5` (zinc-100). Renders on the net-worth TabsList (G3) and
wherever `bg-secondary` appears. Fix both tokens to `#f5f5f5`.

### G9. [LOW] lab()/oklab computed drift on three colored-text families

- Dropdown-menu **Delete** item: reference `rgb(220,38,38)` (**#dc2626**);
  clone emits a v4 `text-red-600` class → computes `lab(48.4 …)`.
- Calculator **"• Will update category total"**: reference
  `rgb(234,88,12)` (**#ea580c**); clone's orange class computes `lab(57.1 …)`.
- **White-alpha labels** (hero "Budget Allocation"/"Balance", net-worth
  card labels/footers): reference `rgba(255,255,255,.6/.7/.8)`; clone's
  `text-white/NN` classes compute `oklab(0.999994 …)`. Invisible (sub-1/255
  drift) but violates the computed-parity convention.

Fix per the project convention (inline styles for parity colors): inline
hex/rgba on those exact nodes.

### G10. [LOW] Focus-ring tokens: forest vs the reference's near-black (inputs) and blue-500 (sidebar)

Measured live: the reference's search-input focus ring = `rgb(10,10,10)
0 0 0 1px` + shadow-sm (their `--ring: 0 0% 3.9%`); the clone's = `rgb(26,
58,46) 0 0 0 1px` + shadow-sm (same geometry, forest color). The reference's
nav-link focus ring = `rgb(59,130,246)` (**#3b82f6** — their
`--sidebar-ring: 217.2 91.2% 59.8%`); the clone's = forest.

Fix: `--color-ring: #0a0a0a`; `--color-sidebar-ring: #3b82f6`; the nav link
switches `focus-visible:ring-ring` → `focus-visible:ring-sidebar-ring`.

### Reference bugs newly documented (no clone change; superset ledger)

- **R5.** The reference's dialogs do NOT close on Escape — the overlay is a
  plain `fixed inset-0` div with no `data-state` and no keyboard dismissal
  (verified with focus inside the dialog on both the budget-item and
  line-item dialogs; only the X / Cancel buttons close it). The clone's
  Radix dialogs close on Escape — pinned by a NEW spec (desktop dialogs;
  the sheet's Escape was already pinned).
- **R6.** The reference's card menu **Delete** destroys the item
  IMMEDIATELY — no confirmation (verified: the Salary item vanished on
  click; restored afterwards with identical data). The clone's delete path
  has a confirm step (edit-dialog confirm row / alert dialog) — a superset
  safety feature, kept and documented.

Prior reference bugs re-confirmed live today: R1 toast-viewport hamburger
block (hit-test top element = the empty container), R2 sheet-stuck-open
after nav (overlay + 288px sheet persist after the route change), R3
dashboard 395px overflow, R4 net-worth 464px overflow. The clone's fixes
for all four re-verified end-to-end on the same probes.

### Verified matching this pass (no action)

Page title (`ZeroBudget`); nav geometry (32px/`h-8`, padding, gap, radius,
rects), resting nav text (zinc-700 both), rail divider (`rgb(229,231,227)`
right 1px, 256px rails); guidelines card chrome + all leaf colors (type
labels, `~%`, gray descriptions); donut sectors, slice labels, legend rows
+ amounts + icons; quick-action cards (borders, gradients, 16px/24px
geometry); breakdown section buttons (`hover:bg-gray-50` chrome, sign
prefixes); stat cards (30px/700 forest amounts, singular counts,
separators); hero leaf colors + sizes; money formats (plain vs grouped);
dialog panel (672px, 16px radius, `0 25px 50px -12px` shadow, no border);
dialog inputs (36px, 6px radius, transparent bg); classification tiles;
calculator banner (tinted card, orange amount, gray captions), headings,
Add-Item gradients (orange→orangeLight, both sides identical); Add-Asset
card gradient; responsive chrome map at 640 (mobile top bar "Toggle
Sidebar" + ZeroBalance heading), 768/820/1024/1280 (256px rail, no burger,
no overflow); mobile sheet geometry (288px, link rows, overlay) and both
superset interaction fixes; select dropdown content geometry (white, 6px,
min-w 128px equivalents, item padding `6px 32px 6px 8px`).

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | Token alignment (G1/G2/G5/G6/G8/G10): foreground family, input, accent pair, sidebar-accent-foreground, muted/secondary, ring pair | NEW `tests/e2e/tokens.spec.ts` (~6 specs: trigger text+border, menu hover+Delete color, select highlight pair, nav hover text, input/nav focus rings) | `src/app/globals.css` |
| 2 | Net-worth tabs (G3): grid list + green active + reference trigger base | `networth.spec.ts` +1 spec (list grid geometry + active/inactive colors) | `src/components/ui/tabs.tsx`, `net-worth-view.tsx` |
| 3 | Dialog action buttons (G4): outline Cancel, gradient Saves (forest vs orange per dialog), outline Add-First-Item; remove `.zb-btn-primary` | NEW `tests/e2e/dialog-buttons.spec.ts` (4 specs: budget dialog pair, line-item orange Save, asset dialog pair, calculator empty-state button) | `globals.css`, `budget-item-dialog.tsx`, `line-item-dialog.tsx`, `asset-dialog.tsx`, `liability-dialog.tsx`, `calculator-dialog.tsx` |
| 4 | Hover-variant pin (G7): `@variant hover (&:hover)` | +1 spec in `mobile-navigation.spec.ts` (iPhone emulation, hover:none → nav tint still applies) | `globals.css` |
| 5 | lab/oklab drift pins (G9): menu Delete `#dc2626`, Will-update `#ea580c`, white-alpha rgba on hero + net-worth labels | folded into tokens.spec + `calculator.spec.ts` + `networth.spec.ts` assertions | `item-card.tsx`, `calculator-dialog.tsx`, `dashboard-view.tsx`, `net-worth-view.tsx` |
| 6 | Superset pin (R5): desktop dialog closes on Escape | +1 spec in `dialog-buttons.spec.ts` | — |
| 7 | Regression: full chain + live parity re-check of every fixed surface | — | — |
| 8 | Docs: session_9 log, worklog, README (R5/R6 + superset list), SKILL (project_state, D-6 row: hover-variant media gate), plan v5 | — | docs |

## Regression pin map (must NOT change)

- Mobile-nav superset fixes #1/#2 + mobile-layout geometry + no-overflow
  (min-w-0 + responsive net-worth figure) — all re-verified this pass
- Money two-formatter contract, breakdown drill-down, badge maps,
  per-surface add-button gradients, calculator/line-item dialog fields,
  net-worth ratio format (`0.21:1` / `∞:1`), type grouping, API contracts,
  seed arithmetic, dialog panel/inputs/tiles, responsive chrome map
- The net-worth summary card's GRADIENT, shadow, decorative circle, H2
  text and grouped comma money stay as-is
