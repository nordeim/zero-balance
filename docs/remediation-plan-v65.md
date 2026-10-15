# Remediation Plan v65 — the OLDEST remaining desktop pair's fresh
# standing sweep (the v58-era savings pair re-run) + the axe-core 5.x
# wrapper watch (NO DRIFT) + the savings page-header row computed census
# pin

Date: 2026-10-15 · Scope: the session-155 v65 queue — "the v58-era
savings pair's fresh sweep (the queue's other OLDEST candidate — the v64
pass covered the v57-era items pair)" and "the axe-core 5.x wrapper
watch (unchanged next re-check point)" — plus the 59th standing checks.
All READ-ONLY on the reference (the v46 rule). Measured live on BOTH
sites via the v65 family: `vlm-shots-v65.sh` + `clone-vlmshots-v65.sh` +
`vlm-compare-v65.mjs` (the pair), `arbit-v65.sh` + `arbit-v65b.sh` (the
DOM arbitration census), `ref-standing-v59.sh` + `standing-checks-v59.sh`
(the 59th round, version-bumped from v58), and the npm/lockfile version
audit (F1).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · 266 e2e ✓ (91 + 95 + 82 chunk
runs = 265 chromium + 1 setup per chunk, zero failures — the `:3100`
orphan check clean before the runs) · 35/35 smoke ✓ — the codebase
matches the documented v64 state exactly (the v64 pin verified present
at items.spec.ts "the income filter-card computed census at 1280"). The
dev DB at the exact seed state (7 budget items / 3 assets / 2
liabilities — seeded fresh this sandbox, dates anchor to the seed-run
day).

## The v65 sweep — what the measurement found

### The 59th standing checks — ALL GREEN

- **Reference side**: the four bugs ALL still live — the toast-blocker
  (`hitIsBurgerChild:false`, the burger's center hit intercepted by
  `DIV.fixed top-0 z-[100]`), the sheet-trap (the overlay remains after
  the nav click, `overlayCount:1`), the no-landmark
  (`navLandmark:false`), the 464px `/networth` overflow at 390. The
  data census UNCHANGED (the 59th consecutive clean drift check: "1
  items · $25,000" networth / "1 items · $5000.00" income / "4 items ·
  $525.00" expenses). The SEO pair live.
- **Clone side**: R1 the burger hit-test TRUE + the sheet opens · R2 the
  sheet CLOSES + navigates (`sheetGone:true, overlayGone:true` on
  /income) · R3 the nav landmark present · R4 ZERO overflow at 390 on
  all five views (docSW 390 each) · the SEO pair live. **The mobile
  navigation menu VERIFIED WORKING — the 59th consecutive time.**

### F1 [AUDIT] — the axe-core 5.x wrapper watch: NO DRIFT

The v64 F1's documented next re-check point ("a 5.x wrapper release or
an engine bump inside the wrapper's nested dep"): **neither has
happened**. The npm-latest `@axe-core/playwright` is STILL 4.13.0 (no
5.x release exists), the lockfile resolves the wrapper to 4.13.0, and
the engine that actually executes the AxeBuilder scans — the wrapper's
NESTED `axe-core@4.13.0` (`node_modules/@axe-core/playwright/
node_modules/axe-core`) — is byte-identical to the v38/v62/v63/v64
audits. The top-level `axe-core@4.14.0` in the tree still belongs to
`eslint-plugin-jsx-a11y@6.10.2` (via eslint-config-next) — a LINT-TIME
static-analysis consumer that never scans pages (the v63 documented
preempt). The a11y.spec.ts contract remains valid as pinned; no
re-scan required. The next re-check point: unchanged (a 5.x wrapper
release or an engine bump inside the wrapper's nested dep).

### F2 [PAIR] — the OLDEST remaining desktop pair's fresh sweep: the v58-era savings pair re-run

The session-155 v65 queue's first item — a fresh VLM standing sweep of
the savings view at 1280×800 FULL-PAGE (the v58 shots of the savings
view predate the v61 dashboard fix and the v62/v63 mobile twins; the
v64 pass covered the OTHER oldest pair, the v57-era items pair). Shot
FULL-PAGE both sides (`vlm-shots-v65.sh` + `clone-vlmshots-v65.sh`),
compared via `vlm-compare-v65.mjs`, every flag DOM-arbitrated via
`arbit-v65.sh` + `arbit-v65b.sh` (the computed census on both sides at
1280×800) per the v43 rule.

**VERDICT DIFFERENT with 2 style flags + data classes, every one
arbitrated to a documented class:**

1. "The avatar circle is green (ref) vs lime/yellow-green (clone), the
   initial U vs D" — DOM-arbitrated to the user-identity class, with a
   NEW perception lesson: the avatar chrome is BYTE-IDENTICAL (36×36,
   radius 9999px, 14px/600, white text, **bg rgb(143, 188, 63) on BOTH
   sides** — the same lime). Only the INITIAL differs: the reference
   renders "U" for its nameless account; the clone's demo user "Demo
   User" renders "D" (the documented name-derived-initial contract,
   sidebar.tsx:110-112). The VLM's "green vs lime" color claim was a
   PERCEPTION ARTIFACT — identical computed colors read as different
   hues.
2. "The reference displays a single card; the clone displays two cards
   side-by-side" — the seed-count data class, re-measured live: the
   grid axes BYTE-IDENTICAL (w 960, gap 16px, 3 tracks); the reference's
   1 savings item vs the clone's 2-item seed. NOTE: the reference's
   template reads "309.328px 309.328px 309.328px" at ONE child while
   the clone's reads "309.328px 309.328px 309.344px" at TWO — the
   fractional last-track distribution is CONTENT-COUNT-CONDITIONAL (the
   browser's subpixel remainder collapses differently with fewer
   in-flow children; the v64 census measured the SAME 309.344 last
   track on both sides at 4-vs-3 children). The axes — width, gap,
   track count — are the contract; the subpixel tail is a rendering
   artifact of the data class.
3. The data classes — the goal-card footer (the v57 DATA-CONDITIONAL
   class re-measured live: the footer chrome BYTE-IDENTICAL [flex
   justify-between 12px rgb(107,114,128) h 16; every child span flex
   gap 4px with the 12×12 gray icon]; the reference's 1 savings item
   carries no paymentMethod so its footer renders ONE child [the date
   alone]; the clone's carry it and render TWO), the badge arrangement
   (the badge chrome BYTE-IDENTICAL [flex/6px radius/2px 10px pad/
   12px-600/h 22; the row flex wrap 8px gap mb 12px]; the clone's
   Recurring superset badge wraps the row to h 52 = 22+8+22 vs the
   reference's 3-badge h 22), the card heights (200 vs 230 = the
   badge-wrap arithmetic data class), and the header subtitle/amount
   texts ("1 items · $1000.00" vs "2 items · $1250.00" — the seed).
4. The Add button's computed box-shadow — the reference renders
   `rgba(0,0,0,0) 0 0 0 0, rgba(0,0,0,0) 0 0 0 0, rgba(0,0,0,0.1) 0 1px
   3px 0, rgba(0,0,0,0.1) 0 1px 2px -1px` (two LEADING zero-alpha
   layers — the Tailwind v4 computed-form class, the documented
   multi-layer rule) while the clone's `.zb-btn-add` (the v11 pin)
   renders the VISIBLE layers alone: `rgba(0,0,0,0.1) 0 1px 3px 0,
   rgba(0,0,0,0.1) 0 1px 2px -1px` — the visible geometry BYTE-IDENTICAL
   (the documented v11 class; the eye renders them the same).

**The pair is CLEAN: every flag arbitrates to a documented class. No
production-code parity gap** (`git diff src/` empty at ship — the
pin-only line continues).

**A DOM-structure discovery (documented, not a gap):** the reference's
savings page carries a HIDDEN zero-size `h1` "ZeroBalance" FIRST in its
DOM (x:0, y:0, w:0, h:0 — its own SEO pattern; an 18px/700 `h2`
"ZeroBalance" logo sits in its sidebar) before the VISIBLE 30px/700 h1
"Savings" at x:348. The clone renders the visible h1 alone (30px/700/
lh36/forestDark — BYTE-IDENTICAL to the reference's visible h1). The
hidden h1 is invisible to every standing VLM pair (correctly never
flagged); the visible h1 chrome is the parity contract.

### F3 [PIN] — the savings view's page-header row computed census at 1280

The F2 arbitration census measured a never-census'd family: the DESKTOP
1280 page-header row of the items views — the v42 census pinned the MID-640
STACKED state only (headerRowMb 32px/dir column across all five routes);
the v63 pin the mobile 390 networth header block; the early-era tests pin
CLASS STRINGS (the chip h-12, the Add-button gradients) but never the
computed geometry of the 1280 row. The census, measured BYTE-IDENTICAL on
both sides (the savings instance):

- **The header row**: flex, justify space-between, align center, gap
  16px, mb 32px, h 60 (the chip 48 + the row's center alignment).
- **The gradient chip**: 48×48, radius 12px (rounded-xl), the savings
  blue gradient `linear-gradient(135deg, rgb(44, 95, 124), rgb(59, 126,
  161))` (HEADER_CHIP_GRADIENTS.savings).
- **The chip icon**: 24×24 (h-6 w-6), white.
- **The h1**: fontSize 30px (text-3xl), weight 700, lineHeight 36px,
  color rgb(26, 58, 46) (forestDark).
- **The count subtitle**: 16px/400/rgb(107, 114, 128) (the "N items ·
  $X" line — the TEXT is the data class, the chrome the pin).
- **The Add button**: "Add Savings" 150×36, radius 6px, pad 8px 16px,
  fontSize 14px, weight 500, color white, the savings blue gradient
  (ADD_BUTTON_GRADIENTS.savings), the `.zb-btn-add` visible shadow
  layers `rgba(0,0,0,0.1) 0 1px 3px 0, rgba(0,0,0,0.1) 0 1px 2px -1px`;
  the plus icon 16×16 (h-4 w-4).

The F3 pin adds the census to `tests/e2e/items.spec.ts` (PIN-ONLY — the
surface is already correct; GREEN first run expected), inside the
savings describe right after the v38 S2 filter-card test, at the pair
viewport (1280×800 explicit).

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F3 pin: the savings page-header row computed census at 1280 (GREEN first) | tests/e2e/items.spec.ts |
| 2 | sanity | S1 mutation A: the header row `mb-8`→`mb-4` must FAIL the pin (mb 32→16); standalone rebuild; restore | src/components/budget/items-view.tsx |
| 3 | sanity | S2 mutation B: the chip `h-12 w-12`→`h-10 w-10` must FAIL the pin (48→40 + the row h 60→52); standalone rebuild; restore | src/components/budget/items-view.tsx |
| 4 | sanity | S3 mutation C: the h1 `text-3xl`→`text-2xl` must FAIL the pin (30px→24px + lh 36→32); standalone rebuild; restore | src/components/budget/items-view.tsx |
| 5 | verify | the 16 screenshots regenerated + byte-compared (expect the SEED-DATE class at most — no production change) | docs/screenshots/ |
| 6 | docs | D1: AGENTS.md v65 paragraph | AGENTS.md |
| 7 | docs | D2: CLAUDE.md count/state bump | CLAUDE.md |
| 8 | docs | D3: README state + the v65 row | README.md |
| 9 | docs | D4: SKILL doc Session 100 row + the state line | zero-balance_SKILL.md |
| 10 | docs | D5: PAD revision block v1.1.22 | Project_Architecture_Document.md |
| 11 | docs | D6: the probe README's v65 section | scripts/parity-probes/README.md |
| 12 | docs | D7: session_158.md + the repo worklog Session 99 entry | docs/session_158.md + worklog.md |
| 13 | ship | the full chain re-run (lint → typecheck → 108 unit → build → 267 e2e → 35 smoke) + commit + SSH-wrapper push | — |

## Pre-execution validation (done before the plan's execution)

- The F3 pin's finders: the Add button by role name "Add Savings"
  (the early-era test's own finder), then the DOM walk UP to the
  container that also holds the visible h1 (the v65 arbitration's own
  row finder — the reference's hidden zero-size h1 "ZeroBalance"
  motivated the VISIBLE-h1 filter on the reference side; the clone
  renders a single visible h1 so `page.locator("h1")` is unambiguous
  there). The chip via `div.h-12` inside the row; the chip icon via the
  chip's `svg`; the subtitle via the h1's parent-element `p`; the
  button icon via the button's `svg`. All axes scroll-independent (the
  header sits at the top of the page at 1280×800).
- The mutation targets: `mb-8` at items-view.tsx:131 (the header row's
  own class — the mb axis), `h-12 w-12` at :136 (the chip's size
  class — the chip + the row-height axes in one mutation), `text-3xl`
  at :144 (the h1's font class — the h1 font-size + line-height axes).
  Each mutation needs the STANDALONE REBUILD as a SEPARATE command (the
  v53 lesson) before the pin run can bite.
- The chain gate: lint → typecheck → 108 unit → build → 266 e2e
  (**267** after: +1 — the F3 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every agent-browser
  run; the with-server boots fresh per command; the reference session
  EXPIRES between long eval gaps — re-login; the e2e chunks pass FULL
  file paths; `ss -tlnp | grep :3100` + kill before every full-chain
  run (the v53 orphaned-webServer lesson); the census JS must carry NO
  `$` sequences inside the unquoted heredoc (the v65 first-pass
  "X: unbound variable" lesson — the v64 rule re-learned).
- The deferred queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side verify-email
  panel census, the forgot-confirm state census, the calculator
  EMPTY-state reference census, the line-items dialog glyphs.
- The v66 queue (suggestions): (1) the re-run cadence rotates to the
  v59-era pair (the dashboard full-page at 1280 — the v61-fix-era
  shots, the oldest remaining after v64/v65 covered the v57/v58 pairs),
  (2) the axe-core 5.x wrapper watch (unchanged next re-check point),
  (3) the deferred reference-write censuses (unchanged).
