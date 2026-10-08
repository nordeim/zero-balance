# Remediation Plan v11 — Session-21 Parity Iteration

Date: 2026-10-08 · Scope: fresh two-site re-audit after the v10 baseline
(`061a16f`) re-verified green (lint · typecheck · 96/96 unit · build ·
104/104 e2e · 30/30 smoke). Probes: `scripts/parity-probes/probe-v11-*.mjs`
via `run-probe.sh`, agent-browser sessions (`ref11`/`clone11` desktop
1280×800 + `ref11m`/`clone11m` 390×844), the standalone parity server on
:3200 booted per command through `with-server.sh` (the sandbox still reaps
background processes; the agent-browser daemon persists).

This pass swept the state dimensions no earlier pass had measured at
computed-style depth: **intermediate/tablet breakpoints** (767/768/1024 —
the md boundary where rail and mobile chrome switch), the **desktop rail
hover state**, the **hero status badge** (Under Budget, the live state on
both sites), the **filter card's live behavior** (search-to-zero → the
FILTERED empty state, plus the item-card badge census), the **dialog
overlay + panel + sheet box-shadows** (read in full — see Observations),
the **gradient Add/Save button family** (`.zb-btn-add`: rest ambient
shadow, focus-visible ring, Plus-icon size, hover state), the **calculator
sm/outline button variants**, the **stat-card shadows**, and the **logout
affordance** (none on either site). The mobile-navigation stack (the task
focus) was re-verified end-to-end first. It found **4 clone-side finding
groups**; no new reference bugs (R1–R7 all re-confirmed live; reference
data unchanged since session 19: allocation 30.5%, expenses $525.00 with
the documented $0.00 "Miscellaneous" residual).

---

## Findings ledger

### G1. [MED] Empty-state heading renders 18px; the reference renders 20px

Measured live on the reference's FILTERED empty state (income page, search
`zzz` → "No income items yet"): the heading computes `font-size: 20px`
(`text-xl`), fw 600, `#1a3a2e`, mb 8px, line-height 28px. The same 20px
was measured on its net-worth Liabilities empty state (reachable live
because the reference account has zero liabilities — "No liabilities yet",
20px/600 inside the carded variant). The calculator's empty state has NO
heading (verified — text-only, matches the clone).

The clone renders the same three headings at `text-lg` (18px) —
`items-view.tsx:237` + `net-worth-view.tsx:373,436`. The v6 iteration
pinned the empty-state structure (bare block, 64px icon at opacity 0.2,
heading mb-2, `text-base` description) but never the heading's font size —
the one unpinned token in the family. Line-height stays 28px on both
sides either way (v3 `text-xl` lh 28 = v4 `text-lg` lh 28 = v4 `text-xl`
lh 28), so block heights do not shift (both sites measured the block at
960×328 / 960×330).

Fix: `text-lg` → `text-xl` on the three headings.

Fix files: `src/components/budget/items-view.tsx`,
`src/components/budget/net-worth-view.tsx`.

### G2. [MED] `.zb-btn-add` family: ambient shadow one notch too light, and no focus-visible ring

Measured live on the reference (Add Income topbar button, Save Item in
the budget dialog, Add Item in the dashboard breakdown header, Add Item
in the calculator — every gradient button):

- **Rest box-shadow** = v3's **bare `shadow`** utility:
  `rgba(0,0,0,0.1) 0px 1px 3px 0px, rgba(0,0,0,0.1) 0px 1px 2px -1px`
  (two layers, 0.1 alpha) — the same geometry at every size (the 32px
  calculator sm variant included).
- **Focus-visible** (programmatic `focus({focusVisible:true})`, confirmed
  by the box-shadow change): `rgb(255,255,255) 0px 0px 0px 0px` (the
  shadcn white zero-spread inner layer) + `rgb(10,10,10) 0px 0px 0px 1px`
  (the 1px `--ring` ring) + the button's own ambient, plus Tailwind v3's
  `outline-none`: `outline: 2px solid transparent; outline-offset: 2px`.
- **Outline variant** (the calculator empty state's "Add First Item"):
  rest shadow = v3's `shadow-sm` (`rgba(0,0,0,0.05) 0px 1px 2px 0px`,
  single layer — the LIGHTER slot, same as the reference's Cancel
  buttons), and the same focus-visible composition with the lighter
  ambient.

The clone's `.zb-btn-add` rest shadow is `var(--shadow-sm)` — the token
pinned by the session-12 trap-5 fix for the NAVBAR surface
(`0 1px 2px 0 rgb(0 0 0/0.05)`) — one notch lighter than the reference's
buttons. The outline variant renders `box-shadow: none`. And on
focus-visible the whole family falls through to the **browser default
`outline: auto`** (measured `auto/1px` with a lab() color) instead of the
reference's ring — no `:focus-visible` rule exists.

Root cause note: the reference's buttons are shadcn-v1 Buttons — the
default/gradient variant carries v3's bare `shadow` while the outline
variant carries v3's `shadow-sm`. The session-12 trap-5 pin correctly
fixed the navbar but the button family was never re-measured (shadows
weren't in any earlier probe — the box-shadow strings were only read
sliced, which hid the trailing visible layer; see Observations).

Fix: pin the two ambient shadows + a `:focus-visible` rule reproducing
the reference's composition (the Button primitive's Cancel already
matches — its `ring-1 ring-ring` renders the same visible ring + shadow-sm
ambient, verified live).

Fix files: `src/app/globals.css` (`.zb-btn-add`, `.zb-btn-add-outline`,
new `:focus-visible` rules; keep source order so the focus rules win).

### G3. [LOW] Plus icon 20px on the Add buttons; the reference renders 16px

Measured live on the reference: the topbar "Add Income" button is 147×36
with a **16px** Plus icon (mr 8px, gap 8px, 14px/500 text); the empty-state
"Add Income" (top 462): 147×36, 16px; the net-worth "Add Asset": 134×36,
16px; the dashboard breakdown "Add Item": 127×36, 16px. The calculator's
"Add Item"/"Add First Item" and every dialog Save button also carry 16px
icons.

The clone renders `PlusIcon className="mr-2 h-5 w-5"` (20px) on the
page-level / empty-state / net-worth / dashboard Add buttons — 4px wider
buttons (151 vs 147, 138 vs 134, 131 vs 127). The calculator's PlusIcons
and the dialog Save icons are already `h-4 w-4` (16px — correct).

Fix: `h-5 w-5` → `h-4 w-4` on the 7 sites (the section-row PlusIcon at
`dashboard-view.tsx:711` and the QuickActionCard trailing Plus are already
16px and match — leave them).

Fix files: `src/components/budget/items-view.tsx` (×2),
`src/components/budget/net-worth-view.tsx` (×4),
`src/components/budget/dashboard-view.tsx` (×1).

### G4. [LOW] Gradient buttons fade to 0.9 opacity on hover; the reference has no hover change

Measured live on the reference (native hover, `matches(":hover")`
confirmed): "Add Income" (topbar), "Add Item" (dashboard) and "Save Item"
(dialog) all keep `opacity: 1` on hover with unchanged box-shadow — no
visible hover state at all on the gradient buttons.

The clone's `.zb-btn-add:hover { opacity: 0.9 }` dates to the session-1
build (`703ea74`), never measured — the same class of unmeasured
assumption as v10's G1 (`highlightActive={false}`). The outline variant's
hover (`bg #f5f5f5`) IS pinned (v5, matches — keep it).

Fix: delete the `.zb-btn-add:hover { opacity: 0.9 }` rule (the outline
variant's own hover rule already sets `opacity: 1` and is unaffected).

Fix files: `src/app/globals.css`.

### Observations (documented, no action)

- **Computed box-shadow strings must be read IN FULL.** The reference's
  dialog panel renders `rgba(0,0,0,0) 0 0 0 0, rgba(0,0,0,0) 0 0 0 0,
  rgba(0,0,0,0.25) 0px 25px 50px -12px` — two transparent lead layers with
  the visible layer LAST. A `.slice(0, 70)` read produced a false
  "shadowless panel" finding this pass; the full string shows the clone's
  panel shadow (`0 25px 50px -12px 0.25`) is IDENTICAL. Same for the
  mobile sheet (shadow-lg visible layers identical both sides) and the
  Cancel button (the white zero-spread focus layer paints nothing).
  Probe hygiene: never truncate computed multi-layer strings.
- **No logout affordance on either site.** The reference's rail footer is
  a static block (no button, cursor auto); a full-DOM sweep found zero
  logout/signout elements. The clone matches visually while keeping its
  store-level `logout()` + `/api/auth/logout` (smoke-tested) — a headless
  superset. Adding logout UI would CREATE visual drift; not done.
- **The reference's rail/footer user block**: "U" avatar + "Budget Pro" +
  "Track your finances" — static, no interactions. Clone matches.

### Verified matching this pass (no action)

Mobile navigation (task focus, both sites 390×844): R1 re-confirmed live
(the ref's toast container `fixed top-0 z-[100]` 390×32 `pe:auto` still
intercepts its burger's center hit — elementFromPoint returns the
container; the clone's hit is DIRECT on the svg); R2 re-confirmed (tapping
Income in the ref's sheet navigated to `/income` with
`sheetStillOpen: true`; the clone's sheet closed and fits 390px); R4
re-confirmed (ref scrollWidth 395 at 390; clone 390 on `/` and `/income`);
the v10 sheet active-highlight re-verified (ref: Income active on
`/income` — white + the 135deg forest-medium→lime gradient + fw 500;
clone: Dashboard active on `/` — superset #3 — with sheet geometry
288×844 `#fafafa` identical); burger/topbar geometry identical (28×28 at
(24,16), "ZeroBalance" 20px/700 at (68,16)).

Tablet/intermediate breakpoints (NEW this pass): at 768×1024 and
1024×800 both sites render the 256px fixed rail with the burger present
but 0×0 (hidden); at 767 both switch to the mobile topbar (no rail,
burger 28×28 at (24,16), brand 20px/700 at (68,16), main x=0, no
overflow). At 768 the reference offsets `main` to x=256 while the clone
pads it (`md:pl-(--sidebar-width)`) — the visible content column is
IDENTICAL (NET ZERO GOAL card at 288/200/448 both sites; the DOM
approach differs, the pixels do not). No overflow at any width.

Desktop rail hover (NEW): Income link hovered — `rgb(24,24,27)` on
`rgb(240,253,244)`, fw 400 both sites (the v5 `@variant hover` pin
holding). Hero status badge (NEW): "Under Budget" label `#0a0a0a` 16px/400
+ value `rgb(245,169,98)` 16px/600, both sites (same live state). Filter
card (NEW): search 447×36 14px `#e5e5e5`-bordered radius 6; triggers
"All Categories"/"All Frequencies" 216×36 space-between — identical; live
filtering behavior identical ("sal" → 1 card, "zzz" → 0 cards + "0 items
· $0.00" header + the empty state). Item-card badge census (NEW): monthly
`#7e22ce`/`#faf5ff`, active `#334155`/`#f8fafc`, need `#b91c1c`/`#fef2f2`
— all 12px/600 radius 6 pad 2px 10px with the svg icon child, identical
both sides. Dialog overlay `rgba(26,58,46,0.5)` z-50 + panel 672×720 at
(304,40) white radius 16 — identical. Calculator: panel 768×515 radius 16
+ panel shadow identical; empty state identical (48px icon op 0.2 mb 12,
14px/400 text mb 16, no heading). Stat cards: 304×210 white radius 16
border `#e5e7e3` shadow `rgba(0,0,0,0.06) 0 4px 20px` — identical.
QuickActionCards: 304×90, chip icon 20px, trailing Plus 16px opacity
50→100 — identical. Cancel (Button primitive): rest ambient + focus ring
+ invisible outline — identical. Donut legends value-DESC both sides (v9
pin holding). Reference data state unchanged (no drift since session 19).

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | G1: empty-state headings → `text-xl` (20px) | `empty-states.spec.ts`: extend the items-view test (`fontSize` "20px" on the heading) + the net-worth liabilities test (heading 20px) | `items-view.tsx`, `net-worth-view.tsx` |
| 2 | G2: `.zb-btn-add` rest shadow → v3 bare-shadow; outline variant → v3 shadow-sm; `:focus-visible` ring (white inner + 1px `#0a0a0a` + variant ambient + transparent 2px outline, offset 2px) | `dialog-buttons.spec.ts`: NEW "button ambient shadows + focus ring (v11)" — the budget dialog's Save Item rest box-shadow + focused box-shadow/outline; the calculator's sm Add Item + outline Add First Item rest shadows (RED: current 0.05/none + auto outline) | `globals.css` |
| 3 | G3: Plus icon `h-5 w-5` → `h-4 w-4` on the 7 Add-button sites | `tokens.spec.ts`: NEW "gradient Add-button chrome (v11)" — the /income topbar Add Income button: svg 16px, rest shadow the v3 bare-shadow, hover opacity 1.0; the net-worth Add Asset svg 16px; the dashboard Add Item svg 16px | `items-view.tsx` (×2), `net-worth-view.tsx` (×4), `dashboard-view.tsx` (×1) |
| 4 | G4: remove `.zb-btn-add:hover { opacity: 0.9 }` | covered by the same tokens.spec test (hover opacity stays 1) | `globals.css` |
| 5 | Docs: session log, worklog, README/AGENTS/CLAUDE/SKILL alignment + probe README v11 rows | — | docs |
| 6 | Regression: full chain + live parity re-check of every fixed surface + screenshot refresh if visual deltas | — | — |

## Regression pin map (must NOT change)

- All six superset fixes (hamburger hit, sheet close-on-nav, root-URL nav
  highlight — rail AND sheet, no mobile overflow, Escape close, delete
  confirmations) and the v10 sheet-active pins
- The navbar's trap-5 `--shadow-sm` pin (`0 1px 2px 0 rgb(0 0 0/0.05)`) —
  the BUTTON family moves to the bare-shadow geometry; the navbar token
  stays as pinned (different reference surface, both measured)
- The Button primitive (Cancel): `ring-1 ring-ring` focus + shadow-sm
  ambient — already matching, untouched
- v5–v10 surface pins: token block, `@variant hover`, dialog X/footers/
  labels/tiles, radio/switch `#171717`, 9999px radii, donut value-DESC +
  `labelLine={false}`, login per-state geometry, badge hex pins,
  plain-text menus, empty-state structure (icon/desc/mb — only the
  heading SIZE changes), dialog panel + sheet + popover shadows (now
  verified identical in full)
- The QuickActionCard + section-row + calculator + Save-button icons
  (already 16px/20px correctly per surface)
- e2e fixture discipline: every spec restores what it mutates
