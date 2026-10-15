# Remediation Plan v61 — the Budget Guidelines card's STRETCH fix (the
# first production-code change since v55) + the quick-action row + the
# Budget Guidelines card's 1280 census pins

Date: 2026-10-15 · Scope: the session-144 v61 queue's first TWO items —
"the QUICK-ACTION card surfaces' 1280 pair (the v45 F3 hover-shadow pin
is at 640; the quick-action row at 1280 unpaired)" and "the BUDGET
GUIDELINES card's 1280 pair (the v51 F4 mobile census's desktop twin
unpinned)" — plus the 55th standing checks. Measured live on BOTH sites
via the v61 family (vlm-shots-v61.sh + clone-vlmshots-v61.sh +
vlm-compare-v61.mjs — the FULL-PAGE 1280x800 pair of the dashboard (both
v61 surfaces live below the fold); qa-census-ref-v61.sh +
qa-census-clone-v61.sh — the guidelines + quick-action DOM census, both
sides; vlm-glcol-v61.mjs — the guidelines-column crop arbitration).
All READ-ONLY on the reference (the v46 rule).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · 261 e2e ✓ (91 + 94 + 78, three
ordered chunks, zero failures) · 35/35 smoke ✓. The 55th standing
checks all clean (the reference's four bugs ALL live [toast-blocker
hitIsBurgerChild:false, the sheet-trap overlayCount:1, the no-landmark
navLandmark:false, the 464 /networth overflow], the clone's mobile menu
VERIFIED WORKING — the 55th time, the data census intact ["1 items ·
$25,000" networth / "1 items · $5000.00" income / "4 items · $525.00"
expenses], the SEO pair live on both sites).

## The v61 sweep — what the measurement found

- **THE DASHBOARD FULL-PAGE 1280x800 VLM PAIR: VERDICT IDENTICAL** —
  every difference the expected DATA class (the allocation pct × 568,
  the balance figures, the stat amounts, the donut percentages). BUT
  the DOM census found ONE real divergence the VLM missed — the
  **BUDGET GUIDELINES CARD'S STRETCH**:
  - the REFERENCE: the right column of the `grid lg:grid-cols-2 gap-6
    mb-8` row is a `space-y-4` WRAPPER (a grid child, stretched to the
    row height 656) containing the compact guidelines card (h 348,
    natural height, top-aligned) — the card ends at y 1122 right after
    the Savings tile, and the remaining ~308px of the column below it
    are PAGE BACKGROUND, not card;
  - the CLONE: the guidelines card itself is the grid child — it
    STRETCHES to the full row height (h 656) — the card's white body +
    border + shadow extend down to y 1430 with ~308px of EMPTY WHITE
    SPACE below the last tile;
  - the quick grid starts at y 1462 on BOTH sides (the row→grid spacing
    32px — the reference's `mb-8` on the row vs the clone's `mt-8` on
    the grid: the GEOMETRY is the contract, the DOM shape is not — the
    v45 lesson);
  - **ARBITRATED VISUALLY** (vlm-glcol-v61.mjs, the x 770-1258 /
    y 764-1472 column crops): the VLM confirms — the reference's white
    card body "ends immediately after the Savings row", the clone's
    "extends further down with a significant amount of extra empty
    white space" — VERDICT DIFFERENT. **A REAL production parity gap**
    — the first since v55 (six consecutive pin-only iterations).
- **THE QUICK-ACTION CENSUS (both sides): byte-identical on every
  axis** — the row grid { display grid, template "304px 304px 304px",
  gap 24px, w 960 } (the content column 1280 − 256 sidebar − 64 p-8);
  each of the three cards { w 304, h 90, radius 16px, pad 24px, bg
  rgb(255,255,255), border rgb(229,231,227) 1px, shadow none at rest,
  textAlign left, transition 0.2s }; the icon tile { 40×40, radius
  12px, bg rgba(143,188,63,0.125) / rgba(59,126,161,0.125) /
  rgba(224,122,59,0.125) }; the icon { 20×20, the type color }; the
  label { 16px/500/rgb(26,58,46) — measured via the LEAF-SPAN finder;
  the first census pass caught the clone's row WRAPPER span (fw 400,
  rgb(10,10,10)) — a FINDER ARTIFACT, the v60 itemdump lesson: the
  reference's row is a DIV so the span query skipped it; the finder
  must pin the leaf span }; the plus { 16×16, opacity 0.5, the type
  color }. The resting shadow `none` + the hover:shadow-lg layers are
  already pinned (v45 F3b).
- **THE BUDGET GUIDELINES CENSUS (both sides): byte-identical on every
  axis EXCEPT the stretch** — the card { w 468, radius 12px, border
  rgb(229,231,227) 1px, bg white, the shadow's VISIBLE layers
  rgba(0,0,0,0.1) 0px 1px 3px 0px + 0px 1px 2px -1px (the reference
  computes 2 leading zero-alpha layers, the clone 4 — the Tailwind v4
  computed-form stacking, the visible layers the contract) }; the
  header { pad 24px, the heading 16px/600/rgb(26,58,46)/lineHeight
  16px/tracking -0.4px }; the body { pad "0px 24px 24px", display
  block }; the three tiles byte-identical — Needs { 418×78, radius
  8px, pad 16px, bg rgb(255,247,245), border rgb(252,221,213), label
  16px/500/rgb(224,122,59), pct ~50% 14px/400/same, desc 12px/
  rgb(107,114,128)/lh 16px }, Wants { same chrome, bg
  rgb(240,247,251), border rgb(212,233,245), color rgb(59,126,161),
  ~30% }, Savings { same chrome, bg rgb(245,249,240), border
  rgb(223,236,208), color rgb(143,188,63), ~20% }. The GUIDELINE_ROWS
  content is a CONSTANT (no data dependency) — the card's natural
  height is fully deterministic: 348 at the 1280 content width.
- **The DOM-shape classes (documented, no action)**: (1) the
  reference's row/grid margins `mb-8` vs the clone's `mt-8` — identical
  geometry; (2) the reference's icon tile is a DIV, the clone's a SPAN
  — identical computed chrome; (3) the reference's inner row wrapper is
  a DIV, the clone's a SPAN; (4) the shadow's leading zero-alpha layer
  count (4 vs 2) — the v4 `shadow` variable chain's computed form, the
  visible layers identical.

## Findings

### F1. [FIX] the Budget Guidelines card must NOT stretch

`src/components/budget/dashboard-view.tsx:981-984` — the row:

  <div className="mt-8 grid grid-cols-1 gap-6 lg:grid-cols-2">
    <SpendingBreakdownCard />
    <BudgetGuidelinesCard />
  </div>

The fix mirrors the reference's DOM (measured live: the right column is
a `space-y-4` wrapper stretched by the grid, the card inside at natural
height):

  <div className="mt-8 grid grid-cols-1 gap-6 lg:grid-cols-2">
    <SpendingBreakdownCard />
    <div className="space-y-4">
      <BudgetGuidelinesCard />
    </div>
  </div>

At lg+ the wrapper stretches (h 656 under the seed), the card keeps its
natural 348 — matching the reference's compact card + background gap
below. Below lg (single column) the wrapper is a no-op (block, auto
height) — the mobile census (v51 F4 at 390) unaffected. The
SpendingBreakdownCard (the taller sibling that drives the row height)
stretches on BOTH sites — unchanged.

### F2. [PIN] the Budget Guidelines card's census at 1280

One new test in `tests/e2e/dashboard.spec.ts` — its own describe "the
Budget Guidelines card census at 1280 (v61 — plan F2)": on /dashboard
at 1280×800 (the read-only logged-in state): (1) the card w 468 /
radius 12px / border rgb(229, 231, 227) 1px / bg rgb(255, 255, 255) /
the shadow's visible layers (toContain the two rgba(0,0,0,0.1)
layers); (2) the header pad 24px + the heading 16px/600/
rgb(26,58,46); (3) the body pad "0px 24px 24px"; (4) the three tiles
(each 418×78 / radius 8px / pad 16px / the byte-identical bg/border/
label/pct/desc chrome per GUIDELINE_ROWS); (5) **THE STRETCH CONTRACT**
(the F1 fix's pin): the card h 348 (the natural arithmetic) + the
card's bottom === the last tile's bottom + 24px (the body's bottom
pad — no empty card body below the tiles) + the row (the card's
ancestor grid) h 656 > the card h (the stretch lives on the WRAPPER,
never the card).

### F3. [PIN] the quick-action cards' census at 1280

One new test in `tests/e2e/dashboard.spec.ts` — its own describe "the
quick-action card row census at 1280 (v61 — plan F3)": on /dashboard at
1280×800: (1) the row grid { template "304px 304px 304px", gap 24px,
w 960 }; (2) each of the three cards { w 304, h 90, radius 16px, pad
24px, bg white, border rgb(229, 231, 227), shadow "none" at rest,
textAlign left }; (3) the icon tile per card { 40×40, radius 12px, the
type tint rgba(...,0.125) }; (4) the icon { 20×20, the type color };
(5) the label (the LEAF span — the finder pins the span with the exact
text AND no element children, never the row wrapper: the v61 label
lesson) { 16px/500/rgb(26, 58, 46) }; (6) the plus { 16×16, opacity
0.5, the type color }.

### S1. [MUTATION-SANITY] the pins bite

(a) REMOVE the F1 wrapper (`<BudgetGuidelinesCard />` unwrapped again)
→ the F2 stretch assertions FAIL (card h 656, the card bottom 308px
below the last tile);
(b) the quick-action card's `p-6` → `p-8` (dashboard-view.tsx:878) →
the F3 pad assertion FAILS (24px vs 32px);
(c) the tile's `rounded-xl` → `rounded-2xl` (dashboard-view.tsx:883) →
the F3 tile radius assertion FAILS (12px vs 16px).
All restored → GREEN. Each mutation preceded by `npm run build`, run
as a SEPARATE command (the v47–v60 execution lesson).

### P1. [PROBE-INFRA] the v61 probe family persisted

vlm-shots-v61.sh + clone-vlmshots-v61.sh + vlm-compare-v61.mjs (the
dashboard FULL-PAGE pair), qa-census-ref-v61.sh + qa-census-clone-v61.sh
(the guidelines + quick-action census, both sides, the cross-row gap),
vlm-glcol-v61.mjs (the guidelines-column crop arbitration — the
REGION-CROP pattern: when a full-page VLM pair calls a flagged-or-not
surface IDENTICAL but the DOM census diverges, crop BOTH screenshots
to the surface's region and re-arbitrate), ref-standing-v55.sh +
standing-checks-v55.sh (the 55th standing checks), plus the probe
README's v61 section. The v61 probe lessons: (1) the heading leaf is a
DIV so `.closest("div")` returns the heading ITSELF — use
`.parentElement` for the wrapper; (2) census finders must pin the LEAF
span (exact text + zero element children) — a bare textContent match
catches ancestor wrappers (the clone's row wrapper span read fw 400 /
rgb(10,10,10) before the fix); (3) the icon tile is a DIV on the
reference but a SPAN on the clone — match BOTH tags by chrome; (4) the
REGION-CROP arbitration pattern (above); (5) a grid child STRETCH
divergence can hide inside an IDENTICAL full-page VLM verdict — the
DOM census (geometry: card height vs row height) is the authority.

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v61 paragraph. D2: CLAUDE.md — the E2E count
261 → 263 + the v61 family entries (the guidelines + quick-action
censuses). D3: README — the counts + the v61 row. D4: the SKILL doc —
the Session 96 row + the state line (line 12). D5: the PAD — a
v1.1.18 revision block. D6: the probe README — the v61 section + the
lessons. D7: the formal session log (session_147.md) + the repo
worklog Session 95 + the ledger list. D8: the workspace worklog.

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F2's pin written FIRST → RED (the stretch assertions FAIL against the stretched clone — the TDD RED phase) | test | `tests/e2e/dashboard.spec.ts` |
| 2 | F1's fix (the space-y-4 wrapper) → the F2 pin GREEN (the TDD GREEN phase) | fix | `src/components/budget/dashboard-view.tsx` |
| 3 | F3's pin (the quick-action census) → GREEN (no production change — the surface already correct) | test | `tests/e2e/dashboard.spec.ts` |
| 4 | S1(a)–(c): the three pin-sanity mutations, each verified to FAIL then restored (each preceded by `npm run build`, run as a SEPARATE command) | verify | `dashboard-view.tsx` |
| 5 | The probe scripts persisted + the probe README's v61 section | docs | `scripts/parity-probes/` |
| 6 | The full chain re-run (108 unit · **263** e2e [+2: the v61 pins] · 35 smoke + lint + typecheck + build) — all green | verify | — |
| 7 | The 16 screenshots regenerated (expect byte-identical OR the seed-date class; the guidelines card region now matches the reference) | docs | `docs/screenshots/` |
| 8 | D1–D8 + the formal session log (session_147.md; the raw transcript lands as the follow-up commit per the session-141 pattern) + the repo worklog Session 95 | docs | repo root + `docs/` |
| 9 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/dashboard-view.tsx:981-984` — the row grid
  `mt-8 grid grid-cols-1 gap-6 lg:grid-cols-2` with the two cards as
  direct children (the F1 fix site); `:829-862` the BudgetGuidelinesCard
  (the card `rounded-xl border bg-card text-card-foreground shadow` at
  :832, the header `flex flex-col space-y-1.5 p-6`, the body
  `space-y-3 p-6 pt-0` at :840, the tile `rounded-lg p-4` at :844 with
  the inline GUIDELINE_ROWS tints); `:869-907` the QuickActionCard (the
  card `group rounded-2xl border p-6 text-left transition-all
  duration-200 hover:shadow-lg` at :877-878, the tile `flex h-10 w-10
  items-center justify-center rounded-xl` at :882-883, the label
  `font-medium` + forestDark at :891-893, the plus `ml-auto h-4 w-4
  opacity-50` at :895-896); `:986-1005` the quick-action row `mt-8
  grid grid-cols-1 gap-6 md:grid-cols-3` with the three cards.
- `src/lib/constants.ts:203-228` — the GUIDELINE_ROWS constant (the
  three rows' text/tint/border/color values — static content, no data
  dependency: the card's natural height is deterministic).
- The e2e contract: both v61 describes run AUTHENTICATED via the setup
  project's storageState; the deterministic e2e seed puts the same
  spending categories on every run (the breakdown card h 656 → the row
  h 656 under the seed — the F2 stretch controls' arithmetic); the
  quick-action surfaces are content-static (h 90).
- The existing pins are SAFE: the v51 F4 pin (the guidelines card at
  390) walks up from the heading to the card — the added wrapper does
  not affect the walk (it stops at the card); the v45 F3b hover pin
  (the shadow layers) is hover-state, orthogonal to the F3 resting
  census; the v44 F2b / v60 F2 drill-down pins walk the breakdown card
  (the LEFT column — untouched by the F1 fix).
- The chain gate: lint → typecheck → 108 unit → build → 261 e2e
  (**263** after: +2 — the v61 pins) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every
  agent-browser run; the with-server.sh boots fresh per command; the
  reference session EXPIRES between long eval gaps — re-login via the
  same eval before any follow-up census; the e2e-chunk file filter:
  pass FULL file paths (no regex alternation — the v58 lesson); each
  mutation's rebuild is a SEPARATE command (the v53 lesson).
- The v61 queue's third item (the reference-side a11y re-audit) is
  DEFERRED to the v62 queue — the F1 production fix + the two pin
  families are this session's core deliverable (the best-judgment
  call: a real parity fix outranks a drift re-audit).
- DEFERRED queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census (the reference's Rent
  carries a line item — an empty state would need a reference
  delete), the line-items dialog glyphs. The reference's
  trending-down glyph stays data-conditional (its net is positive —
  the 55th data census confirms "1 items · $25,000" unchanged).
- The v62 queue (suggestions): the reference-side a11y surface
  re-audit (has the reference's own axe tree drifted since v38?), the
  deferred reference-write censuses (unchanged), and a sweep of the
  SKILL doc's stale count lines (177, 474, 1191, 1255 — pre-existing
  doc drift flagged by the v61 doc digest; docs-only).
