# Remediation Plan v89 — the re-run cycle's next-oldest candidate (the v83-era dashboard pair's fourth re-run) + the axe watch + the quick-action transition + plus-viewBox + guidelines-body-display census pin (PIN-ONLY)

The formal narrative: `docs/session_214.md`. The queue: the v88 plan's v89
suggestion — **the ledger-verified target** (the v88 plan's suggestion
AGREEING with the rotation ledger: the v83-era DASHBOARD pair [the dashboard
FULL-PAGE at desktop 1280x800 — the below-the-fold Budget Guidelines card +
the quick-action row], last re-shot v83, is the oldest remaining candidate
[v83 < v84 < v85 < v86 < v87 < v88]; the pair's FOURTH re-run [v61 → v68 →
v77 → v83 → v89] — the TWELFTH consecutive queue/ledger agreement), plus the
axe-core watch at its re-check point and the 83rd standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 292.**

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered) · **291 e2e ✓** (120 + 113 + 60 chunk executions
across three chunk splits of the 23 files = 293 total = 291 unique tests
[288 chromium + 1 setup, the setup re-run per chunk as the project
dependency; the chunk boundaries split differently than v88's 104 + 129 +
60 but the unique total is identical] — the exact documented v88 state) ·
35/35 smoke ✓. The workspace PRESERVED (the v87 precedent — no reset: git
pull fast-forward 0cae166..ef681c0, the session_214 transcript only, the
tree clean; the environment verified in place — .env
[DATABASE_URL="file:../db/custom.db", db/ at the repo root with custom.db
+ e2e.db], node_modules 354 packages, chromium-1243, the paramiko ssh shim
at /home/z/my-project/bin/ssh); the seedcheck exact (7 items / rent 1850 /
expenses 2235 / 0 line items / 3 assets / 2 liabilities) before any flow
ran, no orphaned servers.

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next prereleases
beyond — no stable 4.14.1, no 5.x exists); the lockfile holding the v68
dedupe state (the wrapper 4.14.0, no nested engine dir under
`node_modules/@axe-core/playwright/`); the engine-contract pin GREEN
standalone (2 passed).

### F2 — the 83rd standing checks: ALL GREEN (version-bumped from v82 — version-bump-only diffs verified)

ref-standing-v83.sh + standing-checks-v83.sh (version-bumped from v82 —
after normalizing the THREE token families [v82→v83, 82nd→83rd, AND the
bare-number session names ref82→ref83/clone82→clone83] the files are
version-bump-only: verified by normalizing back and diffing clean).
Reference side: the four bugs ALL live [toast-blocker
`hitIsBurgerChild:false`; sheet-trap `overlayCount:1`; no-landmark
`navLandmark:false`; the 464px /networth overflow at 390]; the data census
UNCHANGED (the 83rd clean drift check: networth "1 items · $25,000" /
income "1 items · $5000.00" / expenses "4 items · $525.00"); the SEO pair
live. Clone side: R1–R4 ALL GREEN — the mobile navigation menu VERIFIED
WORKING (the **83rd consecutive time**: `hitIsBurgerChild:true`, the sheet
opens, closes on nav, the nav landmark present), zero overflow at 390 on
all five views (docSW 390 everywhere), the SEO pair live.

### F3 — the re-run pair (the v83-era dashboard pair: the dashboard FULL-PAGE at desktop 1280x800 — the below-the-fold Budget Guidelines card + the quick-action row)

**The verdict: IDENTICAL — zero style flags** (the pair's SECOND
consecutive IDENTICAL verdict [v83 → v89], matching v83's own verdict;
the VLM's only flags the expected DATA classes — the allocation bar
30.5%-vs-62.8%, the balance $3475-vs-$2065, the stat figures, the donut
proportions — every one the documented seed-data class).

The both-sides census (arbit-v89.sh — the v75 convention: the census runs
regardless of the verdict; executed in the controlled two-half form
[ref-arbit-v89.sh + clone-arbit-v89.sh] after the sandbox's chromium
resource exhaustion [66 zombie processes reaped] aborted the combined
run — see the operational lessons) **reproducing the v83 census values
EXACTLY — zero drift since v83 on every axis**:

1. PART G (the guidelines card) — the card 468×348/radius 12px/border
   rgb(229,231,227) 1px/white/the visible shadow layers
   `rgba(0,0,0,0.1) 0 1px 3px, rgba(0,0,0,0.1) 0 1px 2px -1px`; the
   header pad 24px/fs 16px/fw 600/rgb(26,58,46)/lh 16px/tracking
   -0.4px; the body pad 0px 24px 24px/display block; all three tiles
   418×78/radius 8px/pad 16px with the Needs/Wants/Savings tint families
   and the label 16px/500/pct 14px/400/desc 12px/lh 16px chrome — the
   ONLY census delta the card shadow's transparent lead-layer count (the
   clone's 6-layer computed form vs the reference's 4 — the v66
   computed-form INVISIBLE class, the visible layers byte-identical);
2. PART Q (the quick-action row) — the grid `304px 304px 304px`/gap
   24px/w 960; the three cards 304×90/radius 16px/pad 24px/white/the
   border/the 40×40 radius-12 tinted tiles/the 20px icons/the labels/the
   16px 0.5-opacity pluses/transition 0.2s — the TWO census deltas both
   documented classes: the grid `mt` (ref 0px vs clone 32px — the
   rendered gap IDENTICAL at 340, the v77 mechanism class) and the label
   finder's wrapper catch (ref leaf 500/rgb(26,58,46) vs clone wrapper
   400/rgb(10,10,10) — the v61 label lesson re-confirmed: the clone's
   LEAF span carries the identical 500/rgb(26,58,46), pinned green by
   the v61 F3 pin's leaf-span finder);
3. PART X (the cross-row gap) — cardBottom 1122/gridTop 1462/gap 340
   on BOTH sides, byte-identical.

**NO NEW CLONE GAP — the v89 iteration is PIN-ONLY.**

### F4 [PIN] — the quick-action transition + plus-viewBox + guidelines-body-display census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 292)

The never-pinned axes (the existing pins cover around them: the v61 F2
pin holds the guidelines card's box chrome + the body's PAD + the FIRST
tile + the STRETCH contract — never the body's DISPLAY; the v61 F3 pin
holds the quick-action grid + the three cards' full chrome
{text/w/h/radius/pad/bg/border/shadow/textAlign/tile/icon/label/plus} —
never the cards' TRANSITION family; the v77 pin holds the guidelines
interior-text family + the ICONS' viewBox [the first svg] — never the
PLUS icons' own viewBox; the v83 pin holds the cross-row vertical rhythm;
grep-verified: no dashboard.spec.ts spec asserts the quick-action card's
transitionDuration/transitionProperty at ANY viewport, no spec asserts
the plus svg's viewBox, and no spec asserts the guidelines body's display
— the items.spec.ts transitionDur pins are the ITEM card's own family, a
different component):

- **The three cards' TRANSITION family at 1280** (dashboard-view.tsx:885
  — the `transition-all duration-200` button): per card
  {transitionDuration "0.2s", transitionProperty "all"};
- **The three PLUS icons' viewBox** (the v77 icon-viewBox family's plus
  twin): "0 0 24 24" per card;
- **The GUIDELINES BODY's display** (the v61 F2 pad family's own
  companion axis): {display "block"} — the pad "0px 24px 24px"
  re-affirming the v61 F2 pin;
- the docSW 1280 guard.

Every pinned axis STATIC chrome (the transition classes, the viewBox
constant, and the body's display unconditional — no data, no viewport
conditionals); the pin rides the plain authenticated dashboard view at
1280 on the e2e seed (read-only — no fixture writes, no hover state), in
tests/e2e/dashboard.spec.ts (the v61/v77/v83/v88 pins' own file).

**The pin's own axes first measured byte-identical on both sides by the
supplemental census** (qa-transition-arbit-v89.sh — the v87/v88 one-shot
precedent): the cards {transitionDuration "0.2s", transitionProperty
"all", plusViewBox "0 0 24 24", plusW 16} on all three; the
guidelinesBody {display "block", pad "0px 24px 24px"}; the docSW 1280 —
all byte-identical on both sides' dashboards at 1280x800.

**The pin-sanity mutation (the executed form — the viewport-scoped
responsive-variant dodge, the v80/v86/v87/v88 pattern)**: the card's
`duration-200` → `duration-200 lg:duration-300` (dashboard-view.tsx:885,
applied by LINE NUMBER) — flips EXACTLY the pin's card.transitionDuration
axis ("0.2s" → "0.3s") and nothing else: the responsive variant is inert
below 1024px; transitionDuration never affects geometry (no width/height/
layout axis reads it — every geometry pin green by construction); the
v45 F3b hover-shadow pin asserts the shadow's SETTLED computed layers
(Playwright's expect polls past the 300ms completion — the final state
identical); the v61 F3 pin's resting shadow "none" unaffected (no
transition runs at rest); no other spec asserts the quick-action card's
transitionDuration at any viewport (grep-verified) — **cascade-free BY
CONSTRUCTION** (the expected failure diff reads as the
card.transitionDuration axis alone), then restored (the standalone
REBUILD as a SEPARATE command; `git diff src/` = 0 lines; the
post-restore full run green).

**The disproven-in-advance candidates (documented without execution —
the design-probe analysis)**: (1) a plus-viewBox mutation — refuted by
the SHARED-COMPONENT cascade (the PlusIcon svg's viewBox feeds every
plus-bearing surface — the item-card rows, the dialog add rows — a flip
cascades beyond the quick-action row into unpinned-but-parity-relevant
surfaces); (2) a guidelines-body display mutation — refuted by the
shared-card-interior cascade (the body element's display flip cascades
into every card family pinned at 1280 [the v42 F2 breakdown card, the
v44 drill-down census, the networth summary card]); (3) an fs-axis
mutation on the guidelines body — REFUTED by the v86 RATIO-LINE-HEIGHT
TRAP lesson (any font-size override scales the line-height and cascades
every height-governed pin [the v61 F2 STRETCH contract cardH 348, the
v77 tile heights 78]).

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → `npm run build` → **292 e2e** in chunks
(+1) → 35 smoke; the 16 standing screenshots regenerated + byte-
compared (the same-DB discipline; the seedcheck under
`env -u DATABASE_URL`). EXPECTED: the same-day seed + same-day shots
reproduce the committed set byte-for-byte (the v82/v88 same-day-seed
byte-identity law — the seed planted and the shots taken on the same
calendar day 2026-10-18); any DATE-class diff pixel-arbitrated per the
v66/v75/v80/v86 discipline, never a full-page VLM verdict; any
rasterization-noise class re-classified per pixel if it recurs.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the quick-action transition + plus-viewBox + guidelines-body-display census at 1280 (the three cards' {transitionDuration/transitionProperty} + the three plus viewBoxes + the body display + the docSW guard), riding the plain authenticated dashboard view | tests/e2e/dashboard.spec.ts |
| 2 | sanity | the pin-sanity mutation (the EXECUTED form): the card's `duration-200` → `duration-200 lg:duration-300` (dashboard-view.tsx:885, by LINE NUMBER) → the pin FAILS at exactly the card.transitionDuration axis ("0.2s" → "0.3s"; the property/viewBox/body/docSW axes stay green); the full dashboard.spec.ts under the mutation: only the v89 pin red; restored → the standalone REBUILD → the post-restore full run green | src/components/budget/dashboard-view.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 292 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v89 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (291→292 + the v89 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v89 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 124 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.46 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v89 section (the new probes + the chromium resource-exhaustion lesson + the two-half controlled census form) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_215.md + the repo worklog Session 124 entry | docs/session_215.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the qa-transition-arbit-v89.sh census's
  own measured values, byte-identical on both sides' dashboards at
  1280x800 (the supplemental census ran BEFORE this plan's execution —
  the values above are its verbatim output).
- The mutation target line verified by reading the source:
  dashboard-view.tsx:885 is the quick-action card button's className
  (`group rounded-2xl border p-6 text-left transition-all duration-200
  hover:shadow-lg`) — the ONLY duration-200 on that line; the other
  duration-200 occurrences (lines 578, 602, 890) belong to the stat
  card, the stat hover glyph, and the qa TILE; the qa PLUS (line 899)
  runs `transition-opacity` with its own default duration — all
  untouched by the line-number-scoped mutation.
- The grep verification: `grep -rn "transitionDuration" tests/e2e/`
  finds the calculator/items/networth specs' own families (different
  components) and NO dashboard.spec.ts assertion; no spec asserts the
  plus svg's viewBox; no spec asserts the guidelines body's display.
- The rotation ledger verified: v83 is the oldest remaining re-shot
  candidate [v83 < v84 < v85 < v86 < v87 < v88] — the v88 plan's v89
  suggestion agreeing with the ledger, the TWELFTH consecutive
  agreement.

## Operational lessons this cycle (the probe README's D6 section)

- THE CHROMIUM RESOURCE-EXHAUSTION LESSON: the sandbox's agent-browser
  chromium processes can accumulate across long probe sessions (66
  zombie processes observed mid-cycle) until fork/pthread_create fails
  (`Resource temporarily unavailable`) — the fix is `pkill -f
  agent-browser` + a fresh session name; the symptom is EMPTY eval
  results (not an error surface).
- THE TWO-HALF CONTROLLED CENSUS FORM: when the combined arbit script
  fails mid-run (the resource exhaustion or a transient with-server
  boot abort), the census's reference half and clone half can run as
  SEPARATE scripts (ref-arbit-v89.sh + clone-arbit-v89.sh) with the
  IDENTICAL census JS (the functional-body diff vs the v83 derivation
  verified version-bump-only) — the both-sides census contract is the
  JS identity, not the single-script form.
- The transient with-server boot abort (the standalone server
  "Aborted" once with an empty log, then booted clean on the manual
  retry) — the retry-first discipline before any investigation.
