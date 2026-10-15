# Remediation Plan v64 — the OLDEST desktop pair's fresh standing sweep
# (the v57-era items pair re-run) + the axe-core 5.x wrapper watch (NO
# DRIFT) + the income filter-card computed census pin

Date: 2026-10-15 · Scope: the session-153 v64 queue — "the re-run cadence
on the OLDEST desktop pairs (v57's items pair and v58's savings pair
predate the v61 dashboard fix and the v62/v63 mobile twins — a fresh
standing sweep of one of them)" and "the axe-core 5.x wrapper watch (F1's
documented next re-check point)" — plus the 58th standing checks. All
READ-ONLY on the reference (the v46 rule). Measured live on BOTH sites
via the v64 family: `vlm-shots-v64.sh` + `clone-vlmshots-v64.sh` +
`vlm-compare-v64.mjs` (the pair), `arbit-v64.sh` (the DOM arbitration
census), `ref-standing-v58.sh` + `standing-checks-v58.sh` (the 58th
round, version-bumped from v57), and the npm/lockfile version audit (F1).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · 265 e2e ✓ (91 + 94 + 82 chunk
runs = 264 chromium + 1 setup, zero failures — the `:3100` orphan check
clean before the runs) · 35/35 smoke ✓ — the codebase matches the
documented v63 state exactly (the v63 pin verified present at
networth.spec.ts:868 "the stat-tile family census at 390"). The dev DB
at the exact seed state (7 budget items / 3 assets / 2 liabilities —
seeded fresh this sandbox, dates anchor to the seed-run day).

## The v64 sweep — what the measurement found

### The 58th standing checks — ALL GREEN

- **Reference side**: the four bugs ALL still live — the toast-blocker
  (`hitIsBurgerChild:false`, the burger's center hit intercepted by
  `DIV.fixed top-0 z-[100]`), the sheet-trap (the overlay remains after
  the nav click, `overlayCount:1`), the no-landmark
  (`navLandmark:false`), the 464px `/networth` overflow at 390. The
  data census UNCHANGED (the 58th consecutive clean drift check: "1
  items · $25,000" networth / "1 items · $5000.00" income / "4 items ·
  $525.00" expenses). The SEO pair live.
- **Clone side**: R1 the burger hit-test TRUE + the sheet opens · R2 the
  sheet CLOSES + navigates (`sheetGone:true, overlayGone:true` on
  /income) · R3 the nav landmark present · R4 ZERO overflow at 390 on
  all five views (docSW 390 each) · the SEO pair live. **The mobile
  navigation menu VERIFIED WORKING — the 58th consecutive time.**

### F1 [AUDIT] — the axe-core 5.x wrapper watch: NO DRIFT

The v63 F1's documented next re-check point ("a 5.x wrapper release or
an engine bump inside the wrapper's nested dep"): **neither has
happened**. The npm-latest `@axe-core/playwright` is STILL 4.13.0 (no
5.x release exists), the lockfile resolves the wrapper to 4.13.0, and
the engine that actually executes the AxeBuilder scans — the wrapper's
NESTED `axe-core@4.13.0` (`node_modules/@axe-core/playwright/
node_modules/axe-core`) — is byte-identical to the v38/v62/v63 audits.
The top-level `axe-core@4.14.0` in the tree still belongs to
`eslint-plugin-jsx-a11y@6.10.2` (via eslint-config-next) — a LINT-TIME
static-analysis consumer that never scans pages (the v63 documented
preempt). The a11y.spec.ts contract remains valid as pinned; no
re-scan required. The next re-check point: unchanged (a 5.x wrapper
release or an engine bump inside the wrapper's nested dep).

### F2 [PAIR] — the OLDEST desktop pair's fresh sweep: the v57-era items pair re-run

The session-153 v64 queue's first item — a fresh VLM standing sweep of
the OLDEST desktop pair (the v57 shots of the income + expenses views at
1280×800 predate the v61 dashboard fix and the v62/v63 mobile twins).
Shot FULL-PAGE both sides (`vlm-shots-v64.sh` +
`clone-vlmshots-v64.sh`), compared via `vlm-compare-v64.mjs`, every flag
DOM-arbitrated via `arbit-v64.sh` (the computed census on both sides at
1280×800) per the v43 rule.

**PAIR 1 (income): VERDICT DIFFERENT with 2 style flags + data classes,
every one arbitrated to a documented class:**
1. "The avatar letter D vs U" — the user-identity class (the
   reference's account vs the clone's demo user).
2. "The clone is missing the Base44 FAB" — the platform-chrome class
   (the reference's own "Edit with Base44" floating badge; the VLM
   contradicted itself between the two pairs — pair 2 attributed it to
   the clone — either way platform chrome, excluded from comparisons by
   the v36 rule).
3. The data classes (1 income item "$5000.00" vs the clone's 2-item
   seed "$5550.00") — the expected seed-data family.

**PAIR 2 (expenses): VERDICT DIFFERENT with 3 style flags + data
classes, every one arbitrated to a documented class:**
1. "The card footer content: the payment-method label with icon" — the
   v57 DATA-CONDITIONAL class, re-measured live: the footer chrome
   BYTE-IDENTICAL both sides (`flex justify-between 12px
   rgb(107,114,128) h 16`; every child span `flex gap 4px` with the
   12×12 gray icon); the reference's expense items carry no
   paymentMethod values so their footers render ONE child (the date
   alone), the clone's carry them and render the SAME two-child
   structure the reference's OWN income card renders (measured live:
   "Oct 7, 2026" + "Bank Account").
2. "The badge arrangement: the extra Recurring badge wrap" — the v57
   wrap data class, re-measured live: the badge chrome BYTE-IDENTICAL
   (the row `flex wrap 8px gap mb 12px`; every badge `flex`/6px
   radius/2px 10px pad/12px-600/h 22); the clone's Recurring superset
   badge wraps the row to h 52 (the 22 + 8 + 22 arithmetic; the
   reference's 3-badge rows stay h 22).
3. "The grid population: a 3-item row + a 1-item row vs a single row of
   3" — the seed-count data class, re-measured live: the grid axes
   BYTE-IDENTICAL (w 960, gap 16px, the template
   "309.328px 309.328px 309.344px" — the SAME fractional last track on
   both sides); the reference's 4 expense cards vs the clone's seed's 3.
4. The card heights (200 vs 230) — the badge-wrap arithmetic data class
   (the clone's wrapped 52px badge row adds exactly the 30px; the card
   HEIGHT is documented as a data class, never pinned).
5. The data classes (the header counts "4 items · $525.00" vs "3 items
   · $2235.00"; the avatar; the FAB misattribution).

**The pair is CLEAN: every flag arbitrates to a documented class. No
production-code parity gap** (`git diff src/` empty at ship — the
pin-only line continues).

### F3 [PIN] — the income view's filter-card computed census at 1280

The F2 arbitration census measured a never-census'd family: the INCOME
view's filter card at desktop 1280 — the never-census'd sibling of the
v38 S2 savings pin (v37/v38 measured the /expenses trigger chrome + the
/savings instance; the v52 F2 pin covered the income card's MOBILE 390
state only; the early-era income test pins CLASS STRINGS
(`rounded-2xl`, `md:grid-cols-4`, `md:col-span-2`, `pl-10`) but never
the computed geometry). The census, measured BYTE-IDENTICAL on both
sides:

- **The card**: 960 wide × 86 tall (24 pad + 36 control + 24 pad + the
  2px borders), pad 24px, radius 16px, bg rgb(255,255,255), border
  rgb(229,231,227), mb 24px.
- **The search input**: 447×36 (the 2-col span: 215.5 + 16 + 215.5),
  computed pad "4px 12px 4px 40px" (the asymmetric 40px left pad —
  the search icon's room, pl-10), radius 6px, border rgb(229,229,229).
- **The inner grid**: display grid, 4 tracks "215.5px" each, gap 16px,
  3 children (the search wrapper spanning 2 + the two comboboxes).
- **The comboboxes**: 216×36 each, fontSize 14px, the rest texts "All
  Categories" / "All Frequencies".

The F3 pin adds the census to `tests/e2e/items.spec.ts` (PIN-ONLY —
the surface is already correct; GREEN first run expected), inside the
income describe right after the early-era class-string filter-card
test, at the pair viewport (1280×800 explicit).

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F3 pin: the income filter-card computed census at 1280 (GREEN first) | tests/e2e/items.spec.ts |
| 2 | sanity | S1 mutation A: the card `p-6`→`p-4` must FAIL the pin (pad 24→16 + card h 86→70); standalone rebuild; restore | src/components/budget/items-view.tsx |
| 3 | sanity | S2 mutation B: the search wrapper `md:col-span-2` removed must FAIL the pin (search w 447→215.5 — the span arithmetic); standalone rebuild; restore | src/components/budget/items-view.tsx |
| 4 | sanity | S3 mutation C: the grid `gap-4`→`gap-2` must FAIL the pin (gap 16→8 + the tracks recompute 215.5→221.5); standalone rebuild; restore | src/components/budget/items-view.tsx |
| 5 | verify | the 16 screenshots regenerated + byte-compared (expect the SEED-DATE class at most — no production change) | docs/screenshots/ |
| 6 | docs | D1: AGENTS.md v64 paragraph | AGENTS.md |
| 7 | docs | D2: CLAUDE.md count/state bump | CLAUDE.md |
| 8 | docs | D3: README state + the v64 row | README.md |
| 9 | docs | D4: SKILL doc Session 99 row + the state line | zero-balance_SKILL.md |
| 10 | docs | D5: PAD revision block v1.1.21 | Project_Architecture_Document.md |
| 11 | docs | D6: the probe README's v64 section | scripts/parity-probes/README.md |
| 12 | docs | D7: session_155.md + the repo worklog Session 98 entry | docs/session_155.md + worklog.md |
| 13 | ship | the full chain re-run (lint → typecheck → 108 unit → build → 266 e2e → 35 smoke) + commit + SSH-wrapper push | — |

## Pre-execution validation (done before the plan's execution)

- The F3 pin's finders: the search input by the placeholder
  `input[placeholder^='Search income']` (the early-era test's own
  finder), then `closest('div.rounded-2xl')` for the card (the
  first rounded-2xl on the page is the filter card — the item cards are
  rounded-xl; the savings pin's own locator pattern), the card's grid
  child via the `display === 'grid'` walk (the v64 arbitration's own
  finder, re-used), the comboboxes via `[role='combobox']` inside the
  grid. All axes scroll-independent (the card sits above the fold at
  1280×800).
- The mutation targets: `p-6` at items-view.tsx:169 (the filter card's
  own class — the pad axis + the card-height axis in one mutation),
  `md:col-span-2` at :179 (the search wrapper's span class — the 447
  span arithmetic axis), `gap-4` at :176 (the inner grid's gap class —
  the gap + track-recompute axis). Each mutation needs the STANDALONE
  REBUILD as a SEPARATE command (the v53 lesson) before the pin run
  can bite.
- The chain gate: lint → typecheck → 108 unit → build → 265 e2e
  (**266** after: +1 — the F3 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every agent-browser
  run; the with-server boots fresh per command; the reference session
  EXPIRES between long eval gaps — re-login; the e2e chunks pass FULL
  file paths; `ss -tlnp | grep :3100` + kill before every full-chain
  run (the v53 orphaned-webServer lesson).
- The deferred queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side verify-email
  panel census, the forgot-confirm state census, the calculator
  EMPTY-state reference census, the line-items dialog glyphs.
- The v65 queue (suggestions): (1) the v58-era savings pair's fresh
  sweep (the queue's other OLDEST candidate — the v64 pass covered the
  v57-era items pair), (2) the axe-core 5.x wrapper watch (unchanged
  next re-check point), (3) the deferred reference-write censuses
  (unchanged).
