# Remediation Plan v45 — The Shadow-Scale Sweep + the Items-View Card
# Grid Census + the Calculator Row Hover (the session-99/100 queue)

Date: 2026-10-11 · Scope: the three queued surfaces — the items-view card
grid at 1280 (unmeasured: the 3-col grid pitch, the card chrome, the
card's hover state), the calculator line-item row's hover at 640/1280
(unmeasured: the row's `hover:shadow-md` under a REAL pointer), and the
category-level expansion animation (implemented in v44, pinned only at
the SECTION level) — PLUS the shadow-scale sweep the calculator probe
opened: a SYSTEMIC v3↔v4 divergence in the computed box-shadow
composition. Measured live on BOTH sites via `items-card-v45.mjs` +
`calc-row-v45.mjs` (drivers: `ref-v45.sh` / `clone-v45.sh`) and direct
agent-browser evals (the real-hover steps).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **214/214 e2e ✓ (4.9m)** · 35/35 smoke ✓. The 39th standing
checks all clean (mobile-nav R1–R4 both sites — Tailwind v4 pins hold,
the mobile menu works; the reference's toast-blocker, sheet-trap,
no-landmark, 395 overflows all still live; the data census read-only
before + after; the SEO pair live). npm audit = the same 5 dev-only
ESLint-chain advisories (accepted, unchanged); the secret-pattern scan
clean; `.env` byte-identical to `.env.example`; the workspace
fast-forwarded (31b275d → e327b57, the session_100.md log).

## The v45 sweep — what the measurement found

- **THE SHADOW-SCALE DISCOVERY (a SYSTEMIC class, VERIFIED-NO-GAP):**
  every live `shadow-*` utility on the clone computes its VISIBLE layers
  byte-identically to the reference's, but the LEAD (transparent)
  layers diverge by construction — Tailwind v4's shadow utilities emit a
  5-slot composition (`--tw-inset-shadow, --tw-inset-ring-shadow,
  --tw-ring-offset-shadow, --tw-ring-shadow, --tw-shadow` → 4 transparent
  leads) where v3 emits 3 slots (2 transparent leads). Example (the
  calculator row under a REAL hover): the reference
  `rgba(0,0,0,0) 0 0 0 0, rgba(0,0,0,0) 0 0 0 0, rgba(0,0,0,0.1) 0 4px
  6px -1px, rgba(0,0,0,0.1) 0 2px 4px -2px` (4 layers) vs the clone's
  6 layers (the same 2 visible + 4 leads). This is the ACCEPTED v10/v25
  class ("v4's transparent lead layers paint nothing — the v10 lesson"),
  now census'd across the FULL scale: shadow-sm (the Google-button
  hover, the slate submit buttons at rest, the dialog inputs, the five
  white pills), shadow-md (the calculator row hover, the expense-card
  action buttons at rest), shadow-lg (the quick-action card hover, the
  mobile sheet), shadow-2xl (the login panel, the details sheet), and
  shadow-xl (the login logo's group-hover). **The `--shadow-sm` theme
  pin (globals.css, the v11 trap-5) is load-bearing for the small end**
  (v4 renamed the scale: v4's native shadow-sm = v3's "shadow"; the pin
  restores v3's `0 1px 2px 0 rgb(0 0 0 / 0.05)` — measured matching on
  both sites). The md/lg/xl/2xl values were NOT renamed (v4 kept v3's
  numerics — measured matching), and are UNPINNED — a future Tailwind
  upgrade that changes the scale would drift silently. **v45 pins the
  visible layers of every size (the regression net).**
- **The items-view card census at 1280: BYTE-IDENTICAL** (the v42
  mid-viewport census's 640 rhythm extends cleanly to the desktop grid):
  the grid 960 wide (the rail 256 + the content column 1024 − the p-8
  64 — the same arithmetic on BOTH sites), 3 columns × 309.328px, gap
  16; the card 309 wide, pad 20, radius 12, border 1px
  rgb(229,231,227), the rest shadow `rgba(0, 0, 0, 0.04) 0px 2px 8px
  0px` (computed 4-value — Chrome normalizes the clone's 3-value inline
  and the reference's inline to the SAME string), bg white, cursor
  pointer, transition all 0.2s; the title row gap 8 / dot 8×8 / title
  16px-600; the income cards' kebab 36×36 opacity 0; the expense cards'
  hover-revealed action row top 12 right 12 / gap 8 / btn h 32 / padX 12
  / fontSize 12. **The card's REAL hover is INERT on BOTH sites** (the
  inline boxShadow beats the `hover:shadow-lg` utility — the v29
  inline-beats-class family; translateY none) and the expense cards'
  action row REVEALS (opacity 0→1) on both. The card heights differ
  (230 vs 200) — DATA (the clone's seed cards carry notes rows), the
  same class as v43's +36. sw 1280 on both.
- **The calculator row census + REAL hover: BYTE-IDENTICAL.** The
  dialog panel 768 wide at 1280 / 608 at 640 (w-full max-w-3xl inside
  the p-4 overlay); the row 720/560 wide, pad 16, radius 12, border 1px
  rgb(229,231,227), boxShadow none at rest, bg white, transition all
  0.15s (v4's default 150ms = v3's — matching); the rest action pair
  opacity 0 / 32px buttons. Under a REAL pointer hover: the row's
  `hover:shadow-md` engages on BOTH sites with the IDENTICAL visible
  layers (`rgba(0,0,0,0.1) 0 4px 6px -1px, rgba(0,0,0,0.1) 0 2px 4px
  -2px`) and the action pair reveals (opacity 1). The row heights
  differ (118 vs 102) — DATA (the probe's provider row). The reference
  measurements required the RENT calculator (the only one of its four
  expense cards with line items — "Contents Insurance"); the clone's
  row was created via the API and restored after (delete + PATCH the
  parent amount back — the calculator rule sets the parent to the
  line-items SUM, so the delete alone recalcs to 0).
- **The category-level (nested) band ANIMATION works on the clone**
  (the v44 Collapse wrapper at the second level): the card ramps
  441→453→463→479→484→491→493→495 on the category expand and
  495→491→483→464→457→448→445→442→441 on the collapse — in-flight frames
  both directions, ~200ms. The v44 F1 e2e pins only the SECTION level;
  the category level is unpinned (the pin candidate).

## Findings

### F1. [PARITY — pin] the items-view card grid census at 1280

Two e2e tests (`tests/e2e/items.spec.ts`, `page.setViewportSize(1280)`,
the items-card-v45 probe ported to the spec's page.evaluate idiom):
- **The income route**: the grid 960 wide / 3 columns × 309.328 / gap 16
  / 2 children; the first card 309 wide / pad 20 / radius 12 / border
  1px rgb(229,231,227) / the rest shadow `rgba(0, 0, 0, 0.04) 0px 2px
  8px 0px` / bg white / cursor pointer / transition all 0.2s; the title
  row gap 8 / dot 8×8 rgb(143,188,63) / title 16px-600; the kebab
  36×36 / opacity 0; a REAL `.hover()` leaves the boxShadow UNCHANGED
  (the inert pin — the inline beats the utility on both sites).
- **The expenses route**: the same grid + card chrome; the action row
  top 12 / right 12 / gap 8 / btn h 32 / padX 12 / fontSize 12; a REAL
  `.hover()` keeps the card's shadow inert AND reveals the action row
  (opacity 0→1) + the action buttons' REST shadow-md visible layers
  (`rgba(0, 0, 0, 0.1) 0px 4px 6px -1px` + `rgba(0, 0, 0, 0.1) 0px 2px
  4px -2px` — the shadow-scale regression pin).

### F2. [PARITY — pin] the calculator row census + the REAL-hover shadow

Two e2e tests (`tests/e2e/calculator.spec.ts`): the existing
create-line-item flow (the spec's seeded fixture + restore), then the
census —
- **At 1280**: the panel 768 wide; the row 720 wide / pad 16 / radius 12
  / border 1px rgb(229,231,227) / boxShadow none at rest / bg white /
  transition all 0.15s; the action pair opacity 0 / 32px buttons; a
  REAL `.hover()` engages the row's shadow-md with the exact VISIBLE
  layers (`rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px
  2px 4px -2px` — the toContain idiom, the accepted-leads convention)
  and reveals the action pair (opacity 1).
- **At 640**: the panel 608 / the row 560 / sw 640 (the mid-viewport
  dialog contract — unmeasured before v45).

### F3. [PARITY — pin] the category-level band animation

One e2e test (`tests/e2e/dashboard.spec.ts`, the v44 F1 idiom extended
to the nested level): expand the Total Income section (settle 600ms),
click the first category row, sample the card height every ~25ms —
in-flight samples strictly between 441 and 495 on the way up AND on the
way down (the v44 F1's curve-agnostic assertion style), the end states
441/495/441. Plus the quick-action card's hover-shadow-lg pin (the
REAL `.hover()`, the visible layers `rgba(0,0,0,0.1) 0px 10px 15px
-3px` + `rgba(0,0,0,0.1) 0px 4px 6px -4px` — the shadow-scale
regression pin for the lg size).

### F4. [PARITY — pin] the shadow-scale regression pins (login)

One e2e test (`tests/e2e/login-parity.spec.ts`): the slate submit
button's REST shadow-sm visible layer (`rgba(0, 0, 0, 0.05) 0px 1px 2px
0px` — guards the `--shadow-sm` theme pin against a Tailwind upgrade),
the login panel's shadow-2xl visible layer (`rgba(0, 0, 0, 0.25) 0px
25px 50px -12px`), and the Google button's REAL-hover shadow-sm
(the same visible layer as the slate button — the --shadow-sm pin is
load-bearing in hover states too).

### S1. [MUTATION-SANITY] the five pins bite

(a) the item-card's inline boxShadow 0.04→0.08 → the F1 rest-shadow pin
fails (the computed string drifts);
(b) the items grid `gap-4`→`gap-6` → the F1 grid pin fails (960/3×309
arithmetic breaks);
(c) the calculator row's `hover:shadow-md` removed → the F2 hover pin
fails (no shadow layers);
(d) the QuickActionCard's `hover:shadow-lg` removed → the F3 lg pin
fails;
(e) the slate button's `shadow-sm` removed → the F4 sm pin fails.
All restored → GREEN.

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v45 paragraph + the 214→220 e2e count. D2:
CLAUDE.md — the v45 entry + the counts. D3: README — the v45 row + the
counts. D4: the SKILL doc — the Session 80 row, the count sites, the
state line. D5: the PAD — a v1.1.2 revision block. D6: the probe
README — the v45 section (the two probes + the drivers + the
shadow-sweep lessons). D7: session_101.md (the formal log) +
session_102.md (the raw transcript) + the repo worklog Session 79 + the
ledger list. D8: the workspace worklog (/home/z/my-project/worklog.md).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1/F2/F3/F4: the SEVEN e2e tests written FIRST (TDD — pin-only: the F2 pair needed its describe-level beforeEach navigation, the one RED-to-fix in the test layer itself; the pins lock the measured contracts) | test | `tests/e2e/items.spec.ts` + `tests/e2e/calculator.spec.ts` + `tests/e2e/dashboard.spec.ts` + `tests/e2e/login-parity.spec.ts` |
| 2 | The probe scripts persisted + the probe README's v45 section | docs | `scripts/parity-probes/` |
| 3 | S1(a)–(e): the five pin-sanity mutations, each verified to FAIL then restored — (a) the card inline 0.04→0.08 → F1a fails; (b) the grid gap-4→gap-6 → F1a+F1b fail; (c) the row hover:shadow-md removed → F2a fails; (d) the quick-action hover:shadow-lg removed → F3b fails; (e) the slate shadow-sm removed → F4 fails | verify | `item-card.tsx` + `items-view.tsx` + `calculator-dialog.tsx` + `dashboard-view.tsx` + `login-card.tsx` |
| 4 | The full chain re-run (108 unit · **221** e2e · 35 smoke + lint + typecheck + build) — all green; the standing VLM pair on the new surface: **IDENTICAL, zero flags** | verify | — |
| 5 | The 16 screenshots regenerated (the capture script) | docs | `docs/screenshots/` |
| 6 | D1–D8 + the formal session log (session_101.md) + the raw transcript (session_102.md) + the repo worklog Session 79 + the SKILL doc Session 80 row | docs | repo root + `docs/` |
| 7 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/items-view.tsx:260` — the grid
  `grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3` (the F1
  target; the reference's DOM carries the identical utility family).
- `src/components/budget/item-card.tsx:74-76` — the card wrapper
  `group cursor-pointer rounded-xl bg-white p-5 transition-all
  duration-200 hover:shadow-lg` + the inline
  `border: 1px solid rgb.border` + `boxShadow: rgba(0, 0, 0, 0.04) 0px
  2px 8px` (the inline beats the hover utility — the F1 inert pin's
  mechanism, the v29 family).
- `src/components/budget/item-card.tsx:98,107` — the action buttons'
  `shadow-md` at rest (the F1 shadow-scale pin).
- `src/components/budget/calculator-dialog.tsx:205` — the row `group
  rounded-xl border bg-white p-4 transition-all hover:shadow-md` + the
  inline borderColor (the F2 target; the reference's class list is the
  same family).
- `src/components/budget/dashboard-view.tsx` — the QuickActionCard
  `hover:shadow-lg` (the F3 lg pin) and the v44 `Collapse` component
  (the F3 category-level sampling: the nested band is the second
  `Collapse` at the category rows).
- `src/components/budget/login-card.tsx:354,640,169` + `:557` — the
  slate buttons' `shadow-sm`, the Google button's `hover:shadow-sm`,
  and the panel's `shadow-2xl` (the F4 pins; the `--shadow-sm` theme
  pin at globals.css:133 is load-bearing for the sm sites).
- The e2e contract: the calculator spec's existing create/delete flow
  restores its fixture (the parent amount recalcs — the spec's own
  discipline); the F2 tests reuse that flow and restore after (the
  parent PATCH back to the seeded amount, matching the probe's
  restore). The REAL `.hover()` idiom is the v43/v44 precedent (the
  synthetic dispatchEvent cannot engage `:hover`). The pins use
  `toContain` on the visible layers — the accepted-leads convention
  (the v10 lesson, restated in login-parity.spec.ts:671's comment).
- The chain gate: lint → typecheck → 108 unit → build → 214 e2e (**221**
  after: +7 — F1a/F1b, F2a/F2b, F3a/F3b, F4) → 35 smoke. The seven
  tests add ~22s. A pin-only iteration: NO production-code change (the
  measured chrome was already at parity — the pins lock it; the five
  S1 mutations prove the pins bite).
- Execution notes: the F2 pair's first run failed on a missing
  describe-level `beforeEach` (no `page.goto("/expenses")` — the rent
  locator timed out; the fix is test-layer only). The build's typecheck
  caught a TS union in the F3a evaluate's early return (the
  `{ sectionExpandedH, catFound: false }` branch vs the full shape —
  fixed by widening the early return; `next build` typechecks the spec
  files too). The VLM pair on the /income 1280 surface: **IDENTICAL,
  zero flags** — the first fully-clean screening since the pair began.
