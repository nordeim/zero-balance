# Remediation Plan v19 — Session-37 Parity Iteration

Date: 2026-10-09 · Scope: fresh two-site re-audit after the v18 baseline
(`7576e56` / v18 code `cf322f6`, all green) re-verified green (lint ·
typecheck · 96/96 unit · build · 134/134 e2e, first full run, no flakes ·
30/30 smoke). Probes: one-shot `agent-browser eval` scripts, sessions
`ref21`/`clone21` desktop 1280×800 + `ref21m`/`clone21m` 390×844 (the
standing checks) + `refauth`/`cloneauth` for the auth surface, the
standalone parity server on :3200 booted per command through
`scripts/with-server.sh`, and — new this pass — **the VLM visual sweep**
(full-page screenshot pairs compared through `z-ai vision`, plus a
mechanical pixel-diff layer and MD5 asset hashing).

This pass swept the surface class the session-36 log flagged as the next
tier — **the VLM visual sweep of the auth surfaces** ("the auth surface
got text-level pins in v12/v13 but no full-page visual diff") — then
extended the same method to the five app views and three dialogs (a
verification layer the project had never applied: every prior surface was
pinned by computed-style probes, never by full-page visual AI comparison),
plus the standing task-focus re-verification (mobile navigation R1–R4 +
reference data-drift check) and the secondary fresh angle (the tablet
breakpoints 767/768/1024 re-measured post-v11).

## The VLM visual sweep — method and results

Twelve auth-state screenshots (six states × two sites: login default,
sign-up, forgot-password, forgot-confirmation, login error, mobile
default), five app views (dashboard, income, expenses, savings, net worth)
and three dialogs (Add Item, calculator, Add Asset) captured at
1280×800 (the app views) / 390×844 (mobile login) and compared pairwise
through `z-ai vision` with layout-focused prompts (data differences
excluded by instruction — the two sites hold different demo data by
design).

- **Auth surfaces: IDENTICAL ×6.** The v12/v13 text-level pins held under
  full-page visual diffing. The mechanical pixel-diff layer (4–20% pixel
  deltas) decomposed into font anti-aliasing noise (uniform glyph-edge
  differences — two different Chrome instances) and the reference's
  "Edit with Base44" floating platform badge (a platform chrome element
  at bottom-right, not app design — the clone correctly has none).
  Asset fidelity verified beyond the VLM: the reference's logo PNG and
  the clone's `public/zerobalance-logo.png` are **byte-identical (same
  MD5 `835c3687f0e66f9e22be716e5919bd8b`)**, both rendered 80×80 from a
  480×480 natural image; the sign-in button measures 294×44 on both.
- **App views: LAYOUT_IDENTICAL ×5.** The dashboard comparison's three
  flagged deltas are all known documented items: the Dashboard active-nav
  highlight (superset fix #3), the avatar letter (different user emails),
  the Budget Allocation progress fill (different demo data — the
  reference's 30.5% vs the clone seed's 63%, both correct arithmetic).
- **Dialogs: ONE REAL FINDING (G1 below).** The calculator's flagged
  "extra line" ("• Will update category total") is a data-state artifact,
  not drift: the reference shows the identical conditional hint on a
  non-zero item (verified live on its Investments $300 calculator —
  "Total Calculated $0.00 / Based on 0 items / • Will update category
  total"), exactly matching the clone's `total !== item.amount`
  conditional. The Add Asset dialog is LAYOUT_IDENTICAL. The **Add Item
  dialog's recurring-toggle row drifts** — found by the VLM, then
  verified in the DOM (the VLM-only layer would not have been enough:
  the same sweep ALSO produced two disproven hallucinations, see
  Observations).
- **Tablet breakpoints (767/768/1024, the secondary fresh angle): visual
  parity holds.** The rail↔mobile-chrome switch lands at 768 on both
  (767: mobile header 61px + full-width main both; 768/1024: rail flex
  256px + header hidden both), no overflow at any width on either side.
  The reference offsets its `<main>` itself (x=256) while the clone keeps
  `main` full-width and offsets the content wrapper (`md:ml-64`) — a
  structural DOM difference, not a visual one: the first heading sits at
  x=288 on both at 768 and 1280.

The mobile-navigation stack (the task focus) was re-verified end-to-end
first (R1/R2/R3/R4 all still live on the reference; all six clone
superset fixes intact — the Tailwind v4 pins hold), and the reference
data-drift check ran clean (unchanged since session 19: allocation 30.5%,
income `$5000.00`/1 item, savings `$1000.00`/1 item, expenses
`$525.00`/4 items, Balance `$3475.00` — thirteenth consecutive clean
check). The code audit re-ran clean: `npm audit` = 5 high, all the
dev-only ESLint `braces` chain (GHSA-vfj7-8cjw-p6xm, no patched release —
accepted, documented); secret-pattern scan clean.

The audit found **1 clone-side finding group** (G1); no new reference
bugs (the reference's silent failures ARE the parity target's behavior —
the clone keeps the surfaces and adds honest feedback, the established
superset class).

---

## Findings ledger

### G1. [MED] the item dialog's recurring-toggle row drifts from the reference on four measured axes (switch side, icon, border, background)

Found by the VLM dialog sweep ("toggle switch on the left with label to
its right, no icons" vs "toggle on the right, calendar icon on the far
left"), then verified in the DOM on both sites (the Add Income dialog,
row width 624 on both):

| Property | Reference | Clone (pre-fix) |
|----------|-----------|-----------------|
| Switch position | **LEFT** — button at x=16 (row-relative), the FIRST child | RIGHT — button at x=571, `justify-between` |
| Label + description | to the switch's RIGHT (x=64, w=251) | LEFT group (x=17, w=283) |
| Gap switch↔text | 12px (`gap: 12px` computed) | 12px inside the label group (icon↔text) |
| Calendar icon | **none** (row svg count 0) | `lucide-calendar h-5 w-5` (row svg count 1) |
| Border | **none** (border 0px) | `1px solid rgb(229, 231, 227)` |
| Background | **`rgb(245, 248, 245)`** (a green-tinted surface) | transparent |
| Row height | 72 | 74 (the +2 = the border) |
| Radius / padding | 8px / 16px | 8px / 16px ✓ |

Text metrics already match (label 14px/500 `#0a0a0a`, description 12px
`rgb(107,114,128)`, text block 40px tall on both) — the drift is purely
the row's arrangement and chrome. The switch PRIMITIVE is untouched
(v9's pins — 36×20 track, `#171717` checked, white thumb — hold; the
existing tokens.spec queries `[role="switch"]` position-independently).

Why every prior probe missed it: the v9 primitive-chrome pins measured
the switch's OWN computed styles; no spec ever pinned the ROW's
child order, border, or background. The VLM full-page layer caught it
because it compares the composed image.

Fix (one file, `src/components/budget/budget-item-dialog.tsx`):

- Rearrange the row to the reference's structure: the `Switch` becomes
  the first child, the label+description `div` second, the row becomes
  `flex items-center gap-3` (no `justify-between`, no inner group).
- Remove the `CalendarIcon` (and its import — it has no other use in
  the file).
- Drop the `border` class + `borderColor` style; set the row's
  background inline — `style={{ backgroundColor: "rgb(245, 248, 245)" }}`
  (the Tailwind v4 lab-drift doctrine: inline rgb for parity colors).
- The row height follows automatically (74 − 2px border = 72).

Pinned by a NEW spec in `tests/e2e/dialog-buttons.spec.ts`: the
recurring row's computed arrangement (switch first + left, label after,
border 0px, background `rgb(245, 248, 245)`, height 72, no svg in the
row) — RED at the pre-fix state, GREEN after the fix.

### Observations (documented, no action)

- **The VLM hallucinates — every finding must be DOM-verified.** This
  sweep produced two disproven VLM claims: (1) the mobile login "logo is
  smaller, faded, desaturated" (the crop-pair analysis) — the DOM
  measures the logo at exactly 80×80/480×480 on both sites and the two
  PNG assets are BYTE-IDENTICAL by MD5; (2) the sign-in button "taller
  and wider" on the clone — measured 294×44 on both. The recurring-row
  finding, by contrast, DOM-verified on all four axes. Lesson: the VLM
  sweep is a SCREENING layer; computed-style measurement remains the
  ground truth. Pin specs assert measured values, never VLM verdicts.
- **The reference's calculator shows the same conditional total hint**
  ("• Will update category total" on its Investments $300 calculator
  with 0 line items; hidden on its Miscellaneous $0.00 item where
  total === amount) — the clone's conditional matches exactly; the VLM
  flagged it only because the screenshot pair sat at different data
  states.
- **The reference's "Edit with Base44" badge is platform chrome** —
  a floating bottom-right platform affordance (with its own close
  button), present in every reference screenshot, absent on the clone
  by design (it is not part of the app's design language).
- **The pixel-diff layer's 4–20% deltas decompose** into font
  anti-aliasing noise (uniform glyph edges — two separate Chrome
  instances rasterizing the same fonts) plus the platform badge; no
  structural diff survives decomposition. The mobile pair's 19.6% is
  the badge + the denser text column.
- **The clone's `<main>` spans full width with the content wrapper
  carrying `md:ml-64`**, while the reference offsets `<main>` itself
  (x=256 at ≥768) — a structural DOM difference with identical visual
  result (first heading x=288 both, at 768 and 1280).
- **The reference data state remains unchanged since session 19**
  (thirteenth consecutive clean drift check).

### Verified matching this pass (no action)

Mobile navigation (task focus, both sites 390×844): R1 re-confirmed live
(the ref's TWO toast containers — both `fixed top-0 z-[100]` 390×32
`pe:auto` — intercept the burger's center hit at (38,30); the clone's
hit is DIRECT on the svg; burger 28×28 at (24,16) both). R2 re-confirmed
(tapping Income in the ref's sheet navigated to `/income` with
`sheetStillOpen: true` + overlay count 1; the clone's sheet CLOSED +
390 fit + `/income`). R3 re-confirmed (no ref link active on `/` — all
five rail links `rgb(63,63,70)`/400 and no `<nav>` landmark; the clone
highlights Dashboard — white + gradient + 500 + landmark). R4
re-confirmed (ref scrollWidth 395 on `/` + `/dashboard`, 464 on
`/networth` full-page load; clone 390 on ALL six routes). Sheet link
geometry identical (Income at (20,185), 247×32, both).

Auth surfaces (the sweep's primary target): all six state pairs
IDENTICAL — the login card's slate hex family, gradients, footer links,
logo halo (v7), the error banner chrome (v12), the register
duplicate-email text (v13), the sign-up placeholders (v13), the
confirmation-state layout (v12), the mobile login card — all verified
as full-page compositions for the first time.

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | G1: pin the reference's recurring-row arrangement — RED spec first | `tests/e2e/dialog-buttons.spec.ts` NEW "the recurring row renders the reference's switch-left tinted layout (v19)" — open the Add Income dialog, read the row's computed arrangement: the switch is the row's FIRST element child and sits LEFT of the label block (x-order assertion), the row carries border 0px + background `rgb(245, 248, 245)` + height 72, and NO svg renders inside the row; run RED at the pre-fix state (the arrangement assertions fail) | — |
| 2 | G1: fix the row (switch first + left, no calendar icon, no border, tinted background) — GREEN | the RED spec flips green | `src/components/budget/budget-item-dialog.tsx` (row rearrange + `CalendarIcon` import removal) |
| 3 | Docs: session log (`docs/session_38.md` — the session_37.md slot holds the incoming session-35 conversation summary), worklog, README/CLAUDE/AGENTS/SKILL alignment (the v19 pin paragraph + the VLM-sweep methodology + the hallucination-verification lesson), probe README v19 rows, and the sweep's method note (the VLM layer joins computed-style probes as the second audit instrument) | — | docs |
| 4 | Regression: full chain + live parity re-check (the fixed recurring row re-measured against the reference side-by-side; the row screenshot pair regenerated) + screenshot refresh (the dialog shots will change — the row is visible in the item-dialog capture; the app-view shots should be pixel-stable) | — | — |

## Regression pin map (must NOT change)

- All six superset fixes (hamburger hit, sheet close-on-nav, root-URL nav
  highlight — rail AND sheet, no mobile overflow, Escape close, delete
  confirmations) and the v9–v18 pins (donut geometry + tooltip, tab icons
  + header chip, banner chrome, titles, placeholders, focus rings, the
  full-page loading state, the boot data-failure tier, the calculator
  error tier, the net-worth + item-card delete error tier, the
  route-announcer spec discipline)
- The v9 switch PRIMITIVE pins (36×20 track, `#171717` checked track,
  white thumb, `#e5e5e5` unchecked, 9999px radii) — the row rearrangement
  must not touch the primitive
- The recurring switch's FUNCTION (form.recurring round-trip, the
  Recurring card badge conditional on the flag — items.spec's coverage)
- The dialog's other rows (Payment Method, Status, Notes — untouched);
  the footer geometry (flex-1 Cancel/Save); the X-close chrome
- e2e fixture discipline: the new spec only READS (opens the dialog,
  computes styles, Escape to close) — no fixture restore needed
