# Remediation Plan v70 — the OLDEST re-run candidate's fresh standing
# sweep (the v57-era items pair — income + expenses at 1280 full-page,
# last re-shot by v64 itself) + the axe-core watch at its re-check point
# + the expenses view's filter-card computed census pin

Date: 2026-10-16 · Scope: the session-167/168 v70 queue — item #1 "the
re-run cadence returns to the DESKTOP pairs (the OLDEST re-run candidate:
the v57-era items pair, last re-shot by v64 — every other desktop pair
re-ran later [savings v65, calculator+login v66, networth+drill-down
v67, dashboard v68] and BOTH mobile twins re-ran at v69; the alternative
NEW-pair program [the below-the-fold 390 surfaces, the items views'
mobile twins never individually shot] stays the v71+ candidate)" and
item #2 "the axe-core watch continues at its next re-check point (only a
5.x wrapper changes the calculus — the engine-contract pin guards the
gate's toolchain)" and item #3 "the deferred reference-write censuses
(unchanged, blocked by the v46 read-only rule)" — plus the 64th standing
checks. Measured live via the v70 family: `vlm-shots-v70.sh` +
`clone-vlmshots-v70.sh` + `vlm-compare-v70.mjs` (both items pairs) +
`arbit-v70.sh` + `arbit-v70b.sh` (the five flags + the card-internals
decomposition) + `ref-standing-v64.sh` + `standing-checks-v64.sh` (the
64th round, version-bumped from v63).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · 271 e2e ✓ (93 + 94 + 86 chunk
runs = 270 chromium + 3 setups, 271 by the --list convention — the exact
documented v69 state) · 35/35 smoke ✓. **No F0 finding this run** — the
committed v69 tree passes the full gate chain as-shipped (the v68
tail-phase miss lesson holding: every file the v69 ship created was
linted before the commit).

## The v70 sweep — what the measurement found

### F1 [WATCH] — the axe-core watch at its re-check point: NO DRIFT

The registry state: npm-latest `@axe-core/playwright` = **4.14.0** (the
dist-tags carry only 4.14.1 rc/next prereleases — no stable 4.14.1, no
4.15); npm-latest `axe-core` = **4.14.0** (no 5.x engine exists). The
lockfile holds the v68 dedupe state: the wrapper 4.14.0 + ONE hoisted
axe-core@4.14.0 (no nested dir — verified live via the wrapper's own
`require.resolve('axe-core')` → `node_modules/axe-core/axe.js`). The
engine-contract pin (the v68 a11y.spec.ts tail) executed GREEN in the
baseline chain — re-verified standalone this session (2 passed). **NO
DRIFT — the 4.x story stays closed; only a 5.x wrapper (or a
nested-engine change) changes the calculus. The next re-check point
unchanged.**

### F2 [STANDING] — the 64th standing checks: ALL GREEN

- **Reference side** (`ref-standing-v64.sh`): the four bugs ALL still
  live — the toast-blocker (`hitIsBurgerChild:false`, the burger's
  center hit intercepted by `DIV.fixed top-0 z-[100]`), the sheet-trap
  (the overlay remains after the nav click, `overlayCount:1`), the
  no-landmark (`navLandmark:false`), the 464px `/networth` overflow at
  390. The data census UNCHANGED (the 64th consecutive clean drift
  check: "1 items · $25,000" networth / "1 items · $5000.00" income /
  "4 items · $525.00" expenses). The SEO pair live.
- **Clone side** (`standing-checks-v64.sh`): R1 the burger hit-test TRUE
  + the sheet opens · R2 the sheet CLOSES + navigates
  (`sheetGone:true, overlayGone:true` on /income) · R3 the nav landmark
  present · R4 ZERO overflow at 390 on all five views (docSW 390 each) ·
  the SEO pair live. **The mobile navigation menu VERIFIED WORKING —
  the 64th consecutive time.**

### F3 [PAIR] — the items pair re-run (income + expenses @1280): CLEAN

The OLDEST re-run candidate re-shot (the v57-era pair, v64's own
re-shot, six iterations stale — the re-run cadence's first completed
cycle: v64→v70). Both sides captured via `vlm-shots-v70.sh` +
`clone-vlmshots-v70.sh` (login on the first attempt both sides, the
parked pointer at (5,5)), compared via `vlm-compare-v70.mjs`.

**PAIR 1 (income): VERDICT DIFFERENT with two style flags + the data
notes, every one DOM-arbitrated via `arbit-v70.sh` + `arbit-v70b.sh`:**
(1) the sidebar avatar "U" vs "D" — the chrome BYTE-IDENTICAL (36×36 /
radius 9999px / 14px / 600 / white / bg rgb(143,188,63), the fixed
v65b finder re-used after the first pass caught the clone's brand block
— the clone's avatar uses `rounded-[9999px]`, not `rounded-full`) = the
**user-identity class**; (2) the card grid "1 card vs 2 side-by-side" —
the AXES byte-identical (w 960 / gap 16px / the 3-track template, the
same fractional 309.344px last track class as v64) = the **seed-count
class**; the card heights (ref 200 vs clone 230) decompose
arithmetic-wise via the v70b card-internals census — the clone's Salary
card carries the 4th **Recurring** superset badge → the wrap h 52
(22+8+22) → +30px, AND the sibling Freelance card (natural 200)
stretches to 230 with it = **the v57 badge-wrap class + the grid
STRETCH-GOVERNED class** (the v67 lesson: the row = the taller sibling,
both cards in one row); the amounts/dates/"Main Job." punctuation = the
data classes.

**PAIR 2 (expenses): VERDICT DIFFERENT with three style flags, every
one arbitrated:** (1) the card footer "payment-method label + icon
altering the bottom section" — the footer CHROME byte-identical
(flex/space-between/12px/rgb(107,114,128)/h 16); the childCount 1 vs 2
is the reference's own data (its expense items carry no paymentMethod
values → date-only footers) = the **v57 DATA-CONDITIONAL class**;
(2) the badge arrangement "the Recurring badge changes the vertical
height and line-break behavior" — the badge CHROME byte-identical
(flex/wrap/gap 8px/mb 12px/2px 10px/12px/600/h 22); the count 3 vs 4
and the wrap h 52 = **the v57 wrap class re-confirmed live** (the v70b
census: every clone expense card 4 badges → h 52; every reference card
3 badges → h 22; the card-height delta 200→230 the same wrap
arithmetic); (3) the avatar = the **user-identity class** (again).

**Both pairs CLEAN — every flag arbitrates to a documented class.** The
re-run re-proves the v57/v64 contracts live six iterations later (the
first cadence cycle complete).

### F4 [PIN] — the expenses view's FILTER-CARD computed census at 1280

The iteration's pin: the last never-census'd filter-card variant — the
v38 S2 pin covered the /savings instance, the v64 pin the /income
variant, the v52 F3 pin the expenses card's MOBILE 390 state only; the
expenses DESKTOP variant (the `lg:grid-cols-4` grid with the search NOT
spanning, the 4 children incl. the 3rd payment-method combobox) was
never censused at any viewport. Measured BYTE-IDENTICAL on BOTH sides
via `arbit-v70.sh` (the expenses half of the census): the card
960×86 (pad 24px/radius 16px/bg rgb(255,255,255)/border
rgb(229,231,227)/mb 24px), the search 216×36 (the 1-col span; the
asymmetric pad "4px 12px 4px 40px", radius 6px, border rgb(229,229,229)),
the inner grid 4 tracks × 215.5px (gap 16px, 4 children), the three
comboboxes 216×36 at 14px ("All Categories" / "All Frequencies" / "All
Payment Methods").

The pin adds ONE test to `tests/e2e/items.spec.ts` (a new describe at
the file tail, after the v58 savings goal-card census), +1 → **272
e2e**. PIN-ONLY — no production-code change (the pin-only line
continues; src/ untouched this iteration — the mutations below were
verified then reverted, `git diff src/` = 0 lines).

### F5 [VERIFY] — the screenshots + the full chain re-run

The 16 screenshots regenerated against the SAME-day seed and
byte-compared against the committed set (any DATE-class diff
pixel-arbitrated via the v66 PIL-diff method). The full gate chain
re-run on the clean tree: lint → typecheck → 108 unit → build → 272
e2e in 3 chunks → 35 smoke.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the expenses filter-card computed census at 1280 (GREEN first run) | tests/e2e/items.spec.ts |
| 2 | sanity | S1 mutation: the expense grid `gap-4`→`gap-2` (the inner gap 16→8) must FAIL the pin; restore | src/components/budget/items-view.tsx |
| 3 | sanity | S2 mutation: the card `p-6`→`p-4` (pad 24→16 + card h 86→70) must FAIL the pin; restore | src/components/budget/items-view.tsx |
| 4 | sanity | S3 mutation: the search `pl-10`→`pl-4` (the asymmetric 40→16 left pad) must FAIL the pin; restore | src/components/budget/items-view.tsx |
| 5 | verify | the full chain re-run (lint → typecheck → 108 unit → build → 272 e2e in chunks → 35 smoke) | — |
| 6 | verify | the 16 screenshots regenerated + byte-compared | docs/screenshots/ |
| 7 | docs | D1: AGENTS.md v70 paragraph | AGENTS.md |
| 8 | docs | D2: CLAUDE.md state bump (the E2E count 271→272 + the v70 pin entry) | CLAUDE.md |
| 9 | docs | D3: README state + the v70 plan-table row | README.md |
| 10 | docs | D4: SKILL doc Session 105 audit row + the state line | zero-balance_SKILL.md |
| 11 | docs | D5: PAD revision block v1.1.27 | Project_Architecture_Document.md |
| 12 | docs | D6: the probe README's v70 section (the 5 new/changed probes + the v70 lessons) | scripts/parity-probes/README.md |
| 13 | docs | D7: session_169.md + the repo worklog Session 104 entry | docs/session_169.md + worklog.md |
| 14 | ship | the full chain re-run + commit + SSH-wrapper push | — |

## Pre-execution validation (done before the plan's execution)

- The F4 pin's mechanism verified live: `arbit-v70.sh` ran the exact
  census the pin's page.evaluate carries (the search → the closest
  `div.rounded-2xl` → the inner grid → the comboboxes) on BOTH sides —
  every asserted value is a measured value, not a derived guess (the
  deterministic arithmetic documented: card w 960 = the rail 256 + the
  content column 1024 − the p-8 64; card h 86 = 24 pad + 36 control +
  24 pad + the 2px borders; search w 216 = the 1-col 215.5px track
  rounded by offsetWidth; the combobox w 216 the same track).
- The pin's read-only: it rides the logged-in storageState (the
  items.spec.ts family), needs no fixture flow, no fixture restore —
  the filter card's geometry is seed-independent (the "All ..." trigger
  defaults, not the derived option lists).
- The S1/S2/S3 mutation mechanics: each is a src/ class-string edit
  (one line each) + a standalone REBUILD (the e2e server serves the
  standalone build — a SEPARATE command per the v63 lesson), the pin
  run FAILS on the mutated axes, then `git checkout --` restores and
  the final rebuild lands the clean tree. S1 mutates the EXPENSE branch
  only (`"grid gap-4 md:grid-cols-2 lg:grid-cols-4"` → gap-2) so the
  v64 income pin stays green; S2 (the card p-6→p-4) and S3 (the
  search pl-10→pl-4) are shared-class regressions — they also fail the
  v64 income pin and the v38 savings chrome assertions, the documented
  shared-class mutation precedent (the v67 stat-tile lesson).
- The existing pins are SAFE: the v64 income filter-card pin (the
  income variant's axes), the v38 S2 savings card assertions, the v52
  F3 expenses mobile census, the v57 F1 footer + badge pin, the v45
  grid census — none asserts the expenses card's DESKTOP 1280 filter
  family (the v37 S3 payment-trigger pin asserts the trigger's
  216×36 only, never the card/grid/search census).
- The chain gate: lint → typecheck → 108 unit → build → 271 e2e
  (**272** after: +1 — the F4 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every
  agent-browser run; the with-server boots fresh per command; the
  reference session EXPIRES between long eval gaps — the login-retry
  loop handles it; the e2e chunks pass FULL file paths;
  `ss -tlnp | grep :3100` + kill before every full-chain run (the v53
  orphaned-webServer lesson); one-shot Prisma scripts need
  `env -u DATABASE_URL` (the sandbox's inherited parent-workspace URL
  is the documented pollution); no dollar sequences in census JS
  inside double-quoted bash strings (the v64 rule); no
  attribute-value selectors in single-quoted eval strings (the v60/v67
  rule — geometry + text-content filters instead); the clone-side
  avatar finder must accept `rounded-[9999px]` (the v65b rule).
- The deferred queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census, the line-items dialog
  glyphs.
- The v71 queue (suggestions): (1) the NEW-pair program opens (the
  below-the-fold 390 surfaces — the items views' mobile twins never
  individually shot, the v62/v63 precedent extending the standing-pair
  matrix to the remaining views) or the re-run cadence's second cycle
  (the v58-era savings pair, last re-shot v65), (2) the axe-core watch
  continues at its next re-check point (only a 5.x wrapper changes the
  calculus), (3) the deferred reference-write censuses (unchanged).
