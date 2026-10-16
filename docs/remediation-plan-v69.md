# Remediation Plan v69 — the mobile 390 pair re-run (the networth
# full-page twin — the documented queue item — PLUS the dashboard mobile
# twin, the other never-re-run mobile pair) + the axe-core watch at its
# re-check point + the networth page-header row computed census pin
# + the F0 lint-gate repair (the v68 ship's own miss)

Date: 2026-10-16 · Scope: the session-165/166 v69 queue — item #1 "the
re-run cadence rotates to the v62-era pair (the networth mobile 390
full-page twin — the oldest remaining after v63's own pass and
v64/v65/v66/v67/v68 covered the v57/v58/v59/v60/v61 pairs)" and item #2
"the axe-core watch continues at its next re-check point (the 4.14.0
upgrade closes the 4.x story; only a 5.x wrapper changes the calculus —
the engine-contract pin now guards the gate's toolchain)" and item #3
"the deferred reference-write censuses (unchanged, blocked by the v46
read-only rule)" — plus the 63rd standing checks. Measured live via the
v69 family: `vlm-shots-v69.sh` + `clone-vlmshots-v69.sh` +
`vlm-compare-v69.mjs` (BOTH mobile pairs) + `arbit-v69.sh` (the four
flags) + `nw-header-v69.sh` (the pin's measurement probe) +
`ref-standing-v63.sh` + `standing-checks-v63.sh` (the 63rd round,
version-bumped from v62).

Baseline before the sweep: lint ✓ (after F0) · typecheck ✓ · 108/108
unit ✓ · build ✓ (robots + sitemap prerendered) · 270 e2e ✓ (the exact
documented v68 state — 97 + 98 + 77 chunks) · 35/35 smoke ✓. The dev DB
verified at the exact seed state (7 items / Rent $1850 / expenses $2235
/ 0 line items / 3 assets / 2 liabilities — via db-seedcheck-v68.cjs
under `env -u DATABASE_URL`; the sandbox's inherited parent-workspace
`DATABASE_URL=file:/home/z/my-project/db/custom.db` is the documented
pollution, and it broke the seedcheck's first run — the `env -u`
discipline applies to one-shot Prisma scripts too).

## The v69 sweep — what the measurement found

### F0 [REPAIR] — the lint gate: the v68 ship's own miss

The v68 changeset shipped `scripts/parity-probes/db-seedcheck-v68.cjs`
— the repo's ONLY `.cjs` file, created during the screenshot phase
(AFTER v68's final lint run) — and its CommonJS `require("@prisma/client")`
trips `@typescript-eslint/no-require-imports`: **the committed v68 tree
did not pass `npm run lint`** (the pre-ship clean-check gap — the file
was never linted before the ship). The v69 audit's first finding, caught
by the baseline chain itself. The repair: a single-file eslint-disable
directive at the top of the .cjs (the file keeps its name + logic — the
historical record intact; the gate stays strict for the rest of
scripts/ — the .mjs probe family lints clean). Scripts-only; src/
untouched. LESSON: the clean-check gate must re-run AFTER every new file
lands, not only before the ship summary — a file created in the
screenshots phase (the chain's tail) escapes a chain run from the
morning.

### F1 [WATCH] — the axe-core watch at its re-check point: NO DRIFT

The registry state: npm-latest `@axe-core/playwright` = **4.14.0** (the
dist-tags carry only 4.14.1 rc/next prereleases — no stable 4.14.1, no
4.15); npm-latest `axe-core` = **4.14.0** (no 5.x engine exists). The
lockfile holds the v68 state: the wrapper 4.14.0 + ONE hoisted
axe-core@4.14.0 (no nested dir — the v68 dedupe state verified live).
The engine-contract pin (the v68 a11y.spec.ts tail) executed GREEN in
the baseline chain — the toolchain that ACTUALLY runs the scans is
4.14.x, guarded. **NO DRIFT — the 4.x story stays closed; only a 5.x
wrapper (or a nested-engine change) changes the calculus. The next
re-check point unchanged.**

### F2 [STANDING] — the 63rd standing checks: ALL GREEN

- **Reference side** (`ref-standing-v63.sh`): the four bugs ALL still
  live — the toast-blocker (`hitIsBurgerChild:false`, the burger's
  center hit intercepted by `DIV.fixed top-0 z-[100]`), the sheet-trap
  (the overlay remains after the nav click, `overlayCount:1`), the
  no-landmark (`navLandmark:false`), the 464px `/networth` overflow at
  390. The data census UNCHANGED (the 63rd consecutive clean drift
  check: "1 items · $25,000" networth / "1 items · $5000.00" income /
  "4 items · $525.00" expenses). The SEO pair live.
- **Clone side** (`standing-checks-v63.sh`): R1 the burger hit-test TRUE
  + the sheet opens · R2 the sheet CLOSES + navigates
  (`sheetGone:true, overlayGone:true` on /income) · R3 the nav landmark
  present · R4 ZERO overflow at 390 on all five views (docSW 390 each) ·
  the SEO pair live. **The mobile navigation menu VERIFIED WORKING —
  the 63rd consecutive time.**

### F3 [PAIR] — BOTH mobile 390 full-page twins re-run: CLEAN

The documented queue item (the networth mobile 390 twin) PLUS the other
never-re-run mobile pair (the dashboard mobile 390 twin — v62's own
mobile addition; the desktop pairs were all re-run through v68, and the
v68 re-run of the v61-era dashboard desktop pair re-proved the desktop
half of v62's program — so the v69 sweep covers BOTH remaining mobile
twins in one two-pair iteration, the v62/v67 two-pair precedent). Both
sides captured via `vlm-shots-v69.sh` + `clone-vlmshots-v69.sh` (login
on the first attempt both sides, the parked pointer at (5,5)), compared
via `vlm-compare-v69.mjs` (two pairs).

**PAIR 1 — the networth mobile 390 re-run: VERDICT DIFFERENT with three
flags, every one DOM-arbitrated via `arbit-v69.sh` to a documented
class** (the v63-era classes, re-confirmed live with the EXACT v63
numbers): (1) the stat-tile layout — the reference's 2-col grid
(cols "175.828px 175.844px", tiles 176×84) inside its 432-wide card in
its own 464px overflow vs the clone's 1-col (cols "294px", tiles
294×84) inside its fitting 358-wide card = **the v41 mobile-superset
class** (the reference's own R-bug-4 overflow forces its fixed 2-col
grid; the clone's fit is the superset fix — pinned by the v63 stat-tile
census); (2) the trend icon "larger/more right" — the medallion 64×64 +
the icon 32×32 BYTE-IDENTICAL both sides; the reference's clips the
viewport at right 416, the clone's fits at 342 = **the v54
clipping-class PERCEPTION ARTIFACT**; (3) the "Edit with Base44"
overlay = **platform chrome, excluded by rule**.

**PAIR 2 — the dashboard mobile 390 re-run: VERDICT DIFFERENT with two
flags + one data note, every one arbitrated**: (1) the Base44 tooltip
overlay "partially clipping the Total Expenses row" = **platform
chrome, excluded by rule** (the documented v62 mobile flag); (2) the
subtitle "wraps differently" — the chrome BYTE-IDENTICAL (the subtitle
P h 48, top 121, 16px/400/rgb(107,114,128), lh 24px, block h 92 — the
EXACT v62 pin values re-measured on both sides); the reference's
subtitle block is 363 wide against the clone's 358 because **the
reference's own page overflows to docSW 395 at 390** (its documented
5px-wide overflow) — the extra 5px of line width shifts its wrap point
by one word ("to" rides the reference's first line), the clone's
fitting wrap the superset consequence = **the documented v62 class**;
(3) the NEW flag variant — "the reference's Net Zero Breakdown card
contains a donut chart (a faint circle behind the text), the clone's
does not" — DOM-DISPROVEN on both sides: the breakdown card carries
ZERO donut on EITHER site (rechartsWrappers 0, pieSectors 0 on both;
the card's 7 svgs are the BYTE-IDENTICAL 16×16/14×14 row icons; the
card h 324 both sides — the v42 census value; the H3+DIV structure
identical) = **a PERCEPTION ARTIFACT** (the VLM likely read the
reference's own Base44 tooltip overlay or the tinted row-icon tiles as
a "faint circle" — the DOM census is the ground truth, the v43 rule).

**Both pairs CLEAN — every flag arbitrates to a documented class.** The
re-run re-proves the mobile twins live after v63's stat-tile pin, the
v62 subtitle pin, and v64–v68's pins.

### F4 [PIN] — the networth view's PAGE-HEADER ROW computed census at 390

The iteration's pin: a never-census'd family on the re-run surface —
the v14 G3 chip test pins the chip/h1 x-positions only, and the v65 F3
savings page-header-row pin's sibling never existed for the networth
surface (at ANY viewport). Measured live on the clone via
`nw-header-v69.sh`: the row flex/align-center/gap-3 (12px) with the
mb-8 (32px) section rhythm (the v41 F1 rhythm re-measured), w 358 (the
390 column − 2×16 p-4), h 60 — the TEXT BLOCK governs (the h1 36 + the
subtitle 24), not the 48px chip (the v65 lesson); the chip 48×48
rounded-xl (12px) with the forest-medium→lime 135deg gradient
(rgb(45, 90, 74) → rgb(143, 188, 63)) wrapping the 24×24 white
TrendingUp; the h1 30px/700/lh 36px/forestDark rgb(26, 58, 46)/h 36/x
76; the block w 250 (the subtitle's max-content governs), h 60; the
subtitle 16px/400/gray-500 rgb(107, 114, 128)/lh 24px — ONE line (h
24); the row→card gap 32; the page FITS 390 (docSW 390 — the superset;
the reference's own page overflows to 464, its R-bug-4).

The pin adds ONE test to `tests/e2e/networth.spec.ts` (a new describe at
the file tail, after the v67 HEIGHT census), +1 → **271 e2e**. PIN-ONLY
— no production-code change (the pin-only line continues; src/
untouched this iteration — the mutations below were verified then
reverted, `git diff src/` = 0 lines).

### F5 [VERIFY] — the screenshots: 16/16 BYTE-IDENTICAL

The first fully-identical set since v65: the dev DB's seed was
re-anchored TODAY (2026-10-16) by the v68 session's re-seed, and the
v69 capture ran on the SAME calendar day — every rendered date digit
matches the committed set byte-for-byte (no DATE-class arbitration
needed this run; the login/404/forgot frames carry no seed dates).
`git diff src/` = 0 lines; `git status docs/screenshots/` empty.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | repair | F0: the single-file eslint-disable for the v68 seedcheck .cjs (the lint gate green again; scripts-only) | scripts/parity-probes/db-seedcheck-v68.cjs |
| 2 | test | F4 pin: the networth page-header row computed census at 390 (GREEN first run) | tests/e2e/networth.spec.ts |
| 3 | sanity | S1 mutation: the row mb-8→mb-4 (mb 32→16 + rowToCardGap 32→16) must FAIL the pin; restore | src/components/budget/net-worth-view.tsx |
| 4 | sanity | S2 mutation: the chip h-12 w-12→h-10 w-10 (48→40 + the h1 x shift) must FAIL the pin; restore | src/components/budget/net-worth-view.tsx |
| 5 | sanity | S3 mutation: the h1 text-3xl→text-2xl (fs 30→24 + lh 36→32 + block h 60→56 + row h 60→56) must FAIL the pin; restore | src/components/budget/net-worth-view.tsx |
| 6 | verify | the full chain re-run (lint → typecheck → 108 unit → build → 271 e2e in chunks [97 + 99 + 77] → 35 smoke) | — |
| 7 | verify | the 16 screenshots regenerated + byte-compared (16/16 byte-identical — the same-day seed) | docs/screenshots/ |
| 8 | docs | D1: AGENTS.md v69 paragraph | AGENTS.md |
| 9 | docs | D2: CLAUDE.md state bump (the E2E count 270→271 + the v69 pin entry) | CLAUDE.md |
| 10 | docs | D3: README state + the v69 plan-table row | README.md |
| 11 | docs | D4: SKILL doc Session 104 audit row + the state line | zero-balance_SKILL.md |
| 12 | docs | D5: PAD revision block v1.1.26 | Project_Architecture_Document.md |
| 13 | docs | D6: the probe README's v69 section (the 6 new/changed probes + the v69 lessons) | scripts/parity-probes/README.md |
| 14 | docs | D7: session_167.md + the repo worklog Session 103 entry | docs/session_167.md + worklog.md |
| 15 | ship | the full chain re-run + commit + SSH-wrapper push | — |

## Pre-execution validation (done before the plan's execution)

- The F4 pin's mechanism verified live: the measurement probe
  (nw-header-v69.sh) ran the exact census the pin's page.evaluate
  carries — every asserted value is a measured value, not a derived
  guess (the deterministic arithmetic documented: block h 60 = h1 36 +
  subtitle 24; row w 358 = 390 − 2×16; h1 x 76 = chip 48 at x 16 + gap
  12).
- The pin's read-only: it rides the logged-in storageState (the
  networth.spec.ts family), needs no fixture flow, no fixture restore.
- The S1/S2/S3 mutation mechanics: each is a src/ class-string edit
  (one line each) + a standalone REBUILD (the e2e server serves the
  standalone build — a SEPARATE command per the v63 lesson), the pin
  run FAILS on the mutated axes, then `git checkout --` restores and
  the final rebuild lands the clean tree.
- The existing pins are SAFE: the v14 chip test (x-positions), the v41
  F2/F3 censuses, the v63 stat-tile pin, the v53 tablist pin, the v60
  F1 census, and the v67 HEIGHT census are all untouched — the v69 pin
  asserts the HEADER family none of them cover (the v14 test's own
  gap: x-positions only, never the row/chip/h1/subtitle computed
  census).
- The chain gate: lint → typecheck → 108 unit → build → 270 e2e
  (**271** after: +1 — the F4 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every
  agent-browser run; the with-server boots fresh per command; the
  reference session EXPIRES between long eval gaps — the login-retry
  loop handles it; the e2e chunks pass FULL file paths;
  `ss -tlnp | grep :3100` + kill before every full-chain run (the v53
  orphaned-webServer lesson); one-shot Prisma scripts need
  `env -u DATABASE_URL` (the sandbox's inherited parent-workspace URL
  is the documented pollution — the v69 seedcheck lesson); no dollar
  sequences in census JS inside double-quoted bash strings (the v64
  rule); no attribute-value selectors in single-quoted eval strings
  (the v60/v67 rule — geometry + text-content filters instead).
- The deferred queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census, the line-items dialog
  glyphs.
- The v70 queue (suggestions): (1) the re-run cadence's mobile twins
  are now BOTH re-run (v69) — the oldest remaining re-run candidate
  returns to the DESKTOP pairs (the v62-era dashboard desktop full
  page, last re-shot by v68 itself — or a NEW-pair program: the
  below-the-fold surfaces at 390, the items views' mobile twins never
  individually shot), (2) the axe-core watch continues at its next
  re-check point (only a 5.x wrapper changes the calculus), (3) the
  deferred reference-write censuses (unchanged).
