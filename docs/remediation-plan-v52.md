# Remediation Plan v52 — The Details Sheet's Missing Subcategory Line
# (THE FIX — the fourth production-code change since v46) + the /income
# and /expenses 390 Pins + the Details-Sheet Internals Pin

Date: 2026-10-12 · Scope: the session-121 v52 queue's read-only members
(the /income and /expenses mobile censuses at 390 — the item-card family
beyond the v51 savings pin; the item-details sheet's internals at 390 —
the v28 geometry pins walked the panel chrome only, never the summary's
content sequence) + the session-121 probe-infra finding (the standing
script's stale burger selector). Measured live on BOTH sites via the
agent-browser evals (the v52 family: `ref-v52.sh` + `clone-v52.sh`,
READ-ONLY on the reference — no form submits, no data mutations, no
auth state writes; the v46 incident rule).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **241/241 e2e ✓ (5.5m — clean on the FIRST run, no flakes)**
· 35/35 smoke ✓. The 46th standing checks all clean (mobile-nav R1–R4
both sites — the clone's mobile menu VERIFIED WORKING via the eval-flow
this session: the burger opens the 5-link sheet, the Income nav closes
the sheet AND navigates, the Escape key closes it; the reference's four
bugs ALL live — the toast-blocker, the sheet-trap via the overlayCount,
the no-landmark, the 464 /networth overflow; the data census read-only
and intact — "1 items · $25,000" networth / "1 items · $5000.00"
income; the SEO pair live on both sites). npm audit = 0 production
vulnerabilities (the same 5 dev-only ESLint-chain advisories, accepted,
unchanged); `.env` ≡ `.env.example` (modulo the dev AUTH_SECRET value).
The trap-log scan CLEAN: only two `-mb-` utilities live in src/ — both
the auth back buttons, both inside their converted `zb-auth-mode`
containers (the v50 + v51 fixes; no un-converted trap site remains).

## The v52 sweep — what the measurement found

- **THE ITEM-DETAILS SHEET'S SUMMARY (the session-121 queue's
  item-details 390 reflow, resolved read-only): ONE REAL GAP — the
  summary block is missing the SUBCATEGORY line.** Measured live on
  BOTH sites (the reference's Rent sheet on /expenses + Salary sheet
  on /income, opened via the card-body click at 390×844):
  - The reference's summary block (`div.text-center.pb-6.border-b`)
    renders FIVE elements: the chip row (`flex items-center
    justify-center gap-2 mb-3` — the EXPENSE/INCOME type chip + the
    classification chip, both `inline-flex px-3 py-1 rounded-full
    text-xs font-medium` 12/500 in the type color) → the **H3 name
    (`text-2xl font-bold mb-2`, 24/700/rgb(26,58,46))** → **the
    SUBCATEGORY P (`text-lg`, 18/400/rgb(107,114,128))** → the amount
    P (`text-4xl font-bold mt-4`, 36/700 in the type color) — the
    values: Rent → "Apartment", Salary → "Main Job".
  - The clone's summary renders FOUR: the chip row ✓ → the H3 ✓ →
    the amount P ✓ — **the subcategory P between the H3 and the
    amount does not exist** (`item-details-dialog.tsx:173-177`: the
    H3 at 173, the amount at 176 — nothing between).
  - The data is ALIGNED: the clone's Item model carries `subcategory`
    (prisma/schema.prisma, the seeded Rent → "Apartment" / Salary →
    "Main Job" — byte-identical values to the reference's renders).
    The field simply was never wired into the details dialog — the
    CARD renders it (`item-card.tsx:125`, the `P.text-sm` under the
    dot+H4 row, byte-identical to the reference's card), the EDIT
    dialog edits it (`budget-item-dialog.tsx:256`), but the DETAILS
    view skips it.
  - POST-FIX geometry: the P adds ~27px to the scrollable BODY's
    height (768 → 795 at 390) — the PANEL's height stays pinned at
    its 85vh cap (717.4 at 844; the body was ALREADY over the cap at
    768) and the panel's `overflow-y: auto` scrolls — NO existing
    panel-geometry pin is affected (the v28 mobile geometry test's
    y 127 / w 390 / maxH 717.4 and the v48 shadow census's h 680 at
    800 stay green; both ride the cap).
  - Reference-side measurement: LIVE this session (the card-body
    click flow — no writes; the sheet opens read-only on click).
- **THE /INCOME VIEW AT 390 (the session-121 queue's mobile census):
  BYTE-PARITY on every visible axis — PIN-ONLY.** Measured on the
  view's full chrome, live on both sites, at 390×844:
  - The header row: 358×112, `flex flex-col` / gap 16px / mb 32px /
    align-start (the mobile reflow of the v20 G1 row) — IDENTICAL.
  - The gradient chip: 48×48 / radius 12px / the lime gradient
    `linear-gradient(135deg, rgb(143,188,63), rgb(184,216,126))` —
    IDENTICAL.
  - The H1 "Income": 30/700/rgb(26,58,46); the count sub: 16/400/
    rgb(107,114,128) (the "2 items · $5550.00" vs "1 items ·
    $5000.00" — the richer seed's data class) — IDENTICAL.
  - The Add button: 147×36 / radius 6px / the same lime gradient /
    white 14/500 / pad 8px 16px — IDENTICAL.
  - The filter card: 358 wide / radius 16px / pad 24px / white /
    border 1px solid rgb(229,231,227) / mb 24px — IDENTICAL.
  - The inner grid at 390: `grid md:grid-cols-4 gap-4` → 1 column
    (308px), gap 16, 3 children — the search wrapper (308×36 @ y
    246), the category trigger (308×36 @ y 298), the frequency
    trigger (308×36 @ y 350) — the y rhythm IDENTICAL.
  - The search input: 308×36 / radius 6px / pad 4px 12px 4px 40px /
    the same placeholder — IDENTICAL.
  - The item grid: grid / 1 column (358px) / gap 16px — IDENTICAL.
  - The first card: 358×230 / radius 12px / pad 20px / border /
    white / shadow rgba(0,0,0,0.04) 0px 2px 8px 0px (the reference's
    200 — the seed's 4-badge wrap, the v51 F3's documented data
    class); the H4 16/600/rgb(26,58,46); the amount 16/400/
    rgb(10,10,10); the badge 12/600 — IDENTICAL.
  - docSW 390 on both sites.
- **THE /EXPENSES VIEW AT 390 (the session-121 queue's mobile census):
  BYTE-PARITY on every visible axis — PIN-ONLY.** The same family:
  the H1 30/700/forest; the count sub 16/rgb(107,114,128) ("3 items
  · $2235.00" vs "4 items · $525.00" — data); the Add button 155×36 /
  the orange gradient `linear-gradient(135deg, rgb(224,122,59),
  rgb(245,169,98))`; the filter card 358 / radius 16 / pad 24; the
  inner grid 1 column (308px) / gap 16 / **4 children** (the search +
  the category + frequency + payment-method selects) / 3 combobox
  triggers; the first card's chrome (358×230 / radius 12 / pad 20 /
  border / white / the 0.04 2px 8px shadow); docSW 390 — IDENTICAL.
- **THE DETAILS SHEET'S INTERNALS AT 390 (beyond the v28/v48 pins):
  BYTE-PARITY on every chrome axis — PIN-ONLY (the subcategory P
  excepted, the F1 fix above).** Measured live on both sites:
  - The panel: 390×717 @ y 127 / radius 24px 24px 0px 0px / maxH
    717.4px (the 85vh cap) / white / overflow-y auto; the shadow's
    VISIBLE 2xl layer rgba(0,0,0,0.25) 0px 25px 50px -12px (the
    reference: 2 transparent leads + the layer = 3; the clone: 4
    leads + the layer = 5 — the accepted lead-divergence class,
    v10/v25/v45/v48) — IDENTICAL.
  - The sticky header: h 69 / pad 16px 24px / position sticky / top 0
    / border-b 1px solid rgb(229,231,227) / bg white (the clone's
    z-10 vs the reference's z auto — both above the body, invisible)
    — IDENTICAL.
  - The title: 18/700/rgb(26,58,46); the close button: 36×36 (the v9
    X family) — IDENTICAL.
  - The body: `space-y-6 p-6` (pad 24px) — IDENTICAL.
  - The classification block: `rounded-xl p-4` + the 20px icon + the
    label font-semibold in the cls color + the desc text-sm gray —
    IDENTICAL.
  - The facts: `space-y-4` / the rows `flex items-center gap-3 py-2`
    (gap 12 / pad 8px 0px) / the 20px gray icons / the label 12px
    gray / the value font-medium forest — IDENTICAL (the clone's
    richer seed adds the Notes row — the documented data class).
  - The meta footer: `border-t pt-4` + the `grid grid-cols-2 gap-4`
    + the labels 12/gray + the values font-medium/forest — IDENTICAL.
- **THE STANDING SCRIPT'S STALE BURGER SELECTOR (the probe-infra
  finding, a scripts/ fix — NOT production): `clone-stand47.sh`'s R1
  clicks `button[aria-label="Open menu"]` — the REFERENCE's DOM
  idiom. The clone's burger carries NO aria-label (its accessible
  name rides the sr-only span "Toggle Sidebar" — the v7 idiom).** The
  selector fails silently on the clone (`|| true` masks the error)
  and R1 reports `sheetLinks: 0` — a FALSE RED on a WORKING surface
  (the mobile nav itself is green: the 7 mobile-navigation e2e tests
  pass, and this session's eval-flow verified the sheet opens 5 links
  / navigates / closes / Escape-closes). The fix: replace the
  selector-based click with the text-walk eval (the verified flow:
  find the button whose textContent includes "Toggle Sidebar", click,
  then census the 5 nav links).

## Findings

### F1. [FIX] the details sheet's missing subcategory P (the summary's
### fifth element)

One production change:

1. `src/components/budget/item-details-dialog.tsx` — insert between
   the H3 (line 173) and the amount P (line 176):
   `{item.subcategory ? (<p className="text-lg" style={{ color: rgb.gray }}>{item.subcategory}</p>) : null}`.
   Conditional on the non-empty subcategory (the dialog's own
   established idiom for optional fields — `item.paymentMethod ? … :
   null`; the reference's template renders the P unconditionally, but
   every reference item carries a subcategory so both forms produce
   identical DOM on real data; the v46 read-only rule bars measuring
   the reference's empty-subcategory edge — the conditional is the
   honest clone-side choice). NO other change: the chip row, the H3,
   the amount, and the panel geometry are already at parity.

One e2e test (`tests/e2e/item-details.spec.ts`, a new
`test.describe("details summary subcategory census (v52 — plan F1)")`
inside the authenticated project, 390×844 viewport): open the Salary
sheet via the card-body click → the subcategory P is visible with the
text "Main Job", fs 18px / fw 400 / color rgb(107,114,128), the class
list containing `text-lg`, and its DOM position BETWEEN the H3
"Salary" and the amount "$5200.00" (the elementAfter/elementBefore
sequence). RED against the current build (the P does not exist) →
the one-insert fix → GREEN.

### F2. [PIN] the /income view's census at 390

One e2e test (`tests/e2e/items.spec.ts` — a 390×844 describe, the
income family): the header row (358×112, flex-col, gap 16, mb 32,
align-start); the chip (48×48, radius 12, the lime gradient); the H1
(30/700/rgb(26,58,46)); the sub (16/400/rgb(107,114,128)); the Add
button (147×36, radius 6, the lime gradient, white, 14/500, pad
8px 16px); the filter card (358, radius 16, pad 24, white, border,
mb 24); the inner grid (1 col 308, gap 16, 3 children at the y rhythm
246/298/350 — the authenticated seed's stable y's); the search
(308×36, radius 6, pad 4px 12px 4px 40px); the item grid (1 col, gap
16); the first card (358 wide, radius 12, pad 20, border, white, the
0.04 2px 8px shadow — the HEIGHT is data-dependent, never pinned);
the H4 (16/600/forest); the amount (16/400/rgb(10,10,10)); docSW 390.

### F3. [PIN] the /expenses view's census at 390

One e2e test (the same describe family): the H1 (30/700/forest); the
sub (16/rgb(107,114,128)); the Add button (155×36, the orange
gradient); the filter card (358, radius 16, pad 24); the inner grid
(1 col 308, gap 16, 4 children, 3 combobox triggers); the first
card's chrome (radius 12, pad 20, border, white, the shadow); docSW
390.

### F4. [PIN] the details sheet's internals at 390

One e2e test (`tests/e2e/item-details.spec.ts` — the v52 describe):
the panel (390 wide @ x 0, radius 24px 24px 0px 0px, maxH 717.4px,
white, overflow-y auto, the shadow's visible 2xl layer + the
construction count); the sticky header (h 69, pad 16px 24px, sticky,
top 0, border-b rgb(229,231,227)); the title (18/700/forest); the
close (36×36); the body (space-y-6 p-6); the summary's chip row
(gap 12, mb 12, the chips 12/500 rounded-full px-3 py-1 in the type
color); the classification block (rounded-xl p-4); the facts rows
(flex gap 12, pad 8px 0px, the icons 20px); the meta footer
(border-t, pt 16, grid-cols-2 gap 16, the labels 12 gray, the values
font-medium forest).

### S1. [MUTATION-SANITY] the pins bite

(a) the subcategory P removed → the F1 pin fails (the TDD RED run —
the pre-fix proof);
(b) the income chip's inline gradient removed → the F2 pin fails
(the chip bg mismatch);
(c) the filter card's `p-6` → `p-4` → the F2/F3 pins fail (the pad
24 → 16);
(d) the details header's `py-4` → `py-2` → the F4 pin fails (the
header 69 → 53);
(e) the items H1's `text-3xl` → `text-2xl` → the F2/F3 pins fail
(the fs 30 → 24).
All restored → GREEN. **Each mutation needs the standalone REBUILD
before the run bites** (the v47–v51 execution lesson — the e2e suite
runs against the BUILD, not the source tree).

### P1. [PROBE-INFRA] the standing script's burger selector

`scripts/parity-probes/clone-stand47.sh` — the R1 step's
`agent-browser click 'button[aria-label="Open menu"]'` (the
reference's DOM idiom, silently failing on the clone since the
sr-only "Toggle Sidebar" burger carries no aria-label) replaced with
the verified text-walk eval: find the button whose textContent
includes "Toggle Sidebar", click it, then the same 5-link census. A
scripts/ change only — zero production impact.

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v52 paragraph. D2: CLAUDE.md — the v52 entry +
the counts. D3: README — the v52 row + the counts. D4: the SKILL doc
— the Session 87 row, the count sites, the state line. D5: the PAD —
a v1.1.9 revision block. D6: the probe README — the v52 section (the
drivers + the lessons). D7: session_122.md (the formal log) +
session_123.md (the raw transcript) + the repo worklog Session 86 +
the ledger list. D8: the workspace worklog
(/home/z/my-project/worklog.md).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1 — the RED pin first (the pre-fix run must FAIL: the subcategory P absent), then the one-insert item-details-dialog.tsx fix (between the H3 at 173 and the amount at 176), then GREEN (TDD — the fourth production change since v46) | fix+test | `src/components/budget/item-details-dialog.tsx` + `tests/e2e/item-details.spec.ts` |
| 2 | F2 + F3 written (pin-only — GREEN immediately against the unchanged build, the TDD pin discipline: the pin proves the parity, the mutations prove the pin) | test | `tests/e2e/items.spec.ts` |
| 3 | F4 written (pin-only — the details sheet's internals) | test | `tests/e2e/item-details.spec.ts` |
| 4 | P1 — the standing script's R1 burger selector fixed (the text-walk eval) | scripts | `scripts/parity-probes/clone-stand47.sh` |
| 5 | The probe scripts persisted + the probe README's v52 section | docs | `scripts/parity-probes/` |
| 6 | S1(a)–(e): the five pin-sanity mutations, each verified to FAIL then restored (each preceded by `npm run build`) | verify | `src/components/budget/item-details-dialog.tsx` + `items-view.tsx` |
| 7 | The full chain re-run (108 unit · **245** e2e · 35 smoke + lint + typecheck + build) — all green; the standing VLM pair on a fresh surface (the /expenses view at 390 — THE F3 SURFACE) | verify | — |
| 8 | The 16 screenshots regenerated (the capture script) | docs | `docs/screenshots/` |
| 9 | D1–D8 + the formal session log (session_122.md) + the raw transcript (session_123.md) + the repo worklog Session 86 + the SKILL doc Session 87 row | docs | repo root + `docs/` |
| 10 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/item-details-dialog.tsx:173-177` — the H3
  (mb-2 text-2xl font-bold, the forest color via COLORS.forestDark)
  followed directly by the amount P (mt-4 text-4xl font-bold, the
  typeColor) — the insertion point for the subcategory P. `rgb` is
  already imported (the facts + footer use `rgb.gray`/`rgb.border`);
  `item.subcategory` is on the store's Item type (the card + the edit
  dialog already read it). NO import or type change needed.
- The existing pins are SAFE: the v28 summary assertions walk the
  H3's role (`heading level 3`) + the amount's class/text (the new P
  adds a text node "Main Job" — `getByRole("heading", { name:
  "Salary", level: 3 })` and the amount locators are unaffected); the
  v28 mobile geometry test pins the PANEL (x 0 / w 390 / maxH 717.4 /
  overflowY auto — all cap- or class-driven, unaffected by the body's
  +27px); the v48 shadow census pins h 680 at 800 (the 85vh cap — the
  content was already over the cap at 768, stays over at 795); the
  v28 income test's "Net monthly salary" Notes fact is unaffected
  (the subcategory P renders in the SUMMARY, not the facts).
- `src/components/budget/items-view.tsx:129` — the header row
  (`mb-8 flex flex-col justify-between items-start gap-4 md:flex-row
  md:items-center`); `:131-137` — the chip (`flex h-12 w-12 …
  rounded-xl` + HEADER_CHIP_GRADIENTS[type]); `:139-143` — the H1
  (`text-3xl font-bold` + rgb.forestDark) + the count sub; `:147-153`
  — the Add button (`zb-btn-add shrink-0` + ADD_BUTTON_GRADIENTS —
  the v8/v11 pinned gradients); `:167` — the filter card (`mb-6
  rounded-2xl bg-white p-6`); `:169-175` — the inner grid (`grid
  gap-4 md:grid-cols-4` / the expense variant `md:grid-cols-2
  lg:grid-cols-4`); the search `pl-10` (the 40px left pad) — the F2/
  F3 targets, byte-verified against the reference census.
- The e2e contract: the items + item-details specs run AUTHENTICATED
  via the setup project's storageState (the deterministic seed — the
  y-position pins 246/298/350 ride the stable filter rhythm; the
  global-setup re-seeds db/e2e.db fresh every run). The Salary item's
  subcategory "Main Job" + amount $5200.00 are seed-stable.
- The chain gate: lint → typecheck → 108 unit → build → 241 e2e
  (**245** after: +4 — F1, F2, F3, F4) → 35 smoke.
- Execution notes: `pkill -f agent-browser` + a stale-session-file
  sweep (`rm -f ~/.agent-browser/<session>.*`) before every
  agent-browser run (the v50/v51 lesson — a killed run leaves the
  .engine pair that HANGS the next open); a rebuild swaps
  .next/standalone UNDER a running parity server — reboot the :3200
  server after every build (with-server.sh boots fresh per command);
  the reference session EXPIRES between long eval gaps — re-login
  via the same eval before any follow-up census (this session's
  lesson); `agent-browser set viewport` state DOES NOT survive a
  session restart — re-apply before any 390 census after a re-login
  (this session's "215.5px desktop" false reading).
- The VLM pair: the /expenses view at 390 (THE F3 SURFACE — the
  filter + card family, a data-divergent surface; the expected flags:
  the reference's own Base44 FAB + the seed-data classes, the v47/v48
  precedents).
- DEFERRED queue (unchanged, both need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side verify
  -email panel census (a registration) and the reference-side
  forgot-confirm state census (a reset-link submit).
