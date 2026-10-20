# Remediation Plan v96 — the re-run cycle's next-oldest candidate (the v90-era MOBILE 390 twins' fifth re-run) + the axe watch + the head-row typography/figure-fit census pin (PIN-ONLY)

The formal narrative: `docs/session_229.md` (the v95 cycle's own narrative
log). The queue: the v95 plan's v96 suggestion — **the ledger-verified
target** (the v95-era docs' suggestion AGREEING with the rotation ledger:
the v90-era MOBILE 390 twins [the /NETWORTH view + the DASHBOARD
FULL-PAGE pair at 390x844] — last re-shot v90, the oldest remaining
[v90 < v91 < v92 < v93 < v94 < v95]; the pair's FIFTH re-run
[v62/v63 → v69 → v78 → v84 → v90 → v96] — the NINETEENTH consecutive
queue/ledger agreement), plus the axe-core watch at its re-check point
and the 90th standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 299.**

## The pre-execution ledger verification (the queue-prose verification lesson, applied)

The rotation ledger's authority is the PROBE LINEAGE, never the prose
queue phrasing. Verified against `scripts/parity-probes/vlm-shots-v90.sh`
before the derivation: its own header reads "BOTH mobile 390x844
full-page twins — (1) the /NETWORTH view (the v63-era pair's surface)
and (2) the DASHBOARD (the v62-era mobile twin's surface). The v90 queue
(... the twins last re-shot v84 = the oldest remaining ...; the pair's
FOURTH re-run [v62/v63 → v69 → v78 → v84 → v90])" — matching the
queue's phrasing exactly (no transcription error). The re-run bracket
verified against the same script's header — v96 is the FIFTH re-run
[v62/v63 → v69 → v78 → v84 → v90 → v96]. The standing-checks pair
(ref-standing-v90.sh + standing-checks-v90.sh) derived from v89 across
the three token families (v89→v90, 89th→90th, ref89→ref90/
clone89→clone90), version-bump-only verified by normalizing back and
diffing clean (zero old tokens remaining — the derive-standing-v96.py
persisted derivation, both halves bash -n clean).

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered) · **298 e2e ✓** (139 + 100 + 61 chunk executions
across three chunk splits of the 23 files = 300 total = 298 unique tests
[297 chromium + 1 setup, the setup re-run per chunk as the project
dependency] — the exact documented v95 state, zero flakes on the first
run) · 35/35 smoke ✓. The workspace: the CARRIED-OVER environment (the
session-log-only commit class — pulled to main @ 2b0bb52, the docs-only
session-log commit [docs/session_229.md, 99 insertions], ZERO src/ or
lockfile deltas since the v95 push 7a1ce9a, so the v95 cycle's own
fresh-clone environment carries over unchanged, no re-provisioning; the
`.env` [DATABASE_URL="file:../db/custom.db"], `db/` at the repo root,
chromium-1243, node_modules all intact); the seedcheck exact (7 items /
rent 1850 / expensesTotal 2235 / 0 line items / 3 assets / 2 liabilities)
before any flow ran, no orphaned servers.

The codebase audit clean: the v95 commit (7a1ce9a) verified PIN-ONLY as
documented (25 files, +2361/−5, ZERO src/ changes); the one commit since
(2b0bb52) session-log-only; the production seams re-audited (auth
scrypt/HMAC, the db-path contract [db-path.ts + its unit test], the SEO
pair [robots.ts + sitemap.ts — both prerendered by the build], the
Tailwind v4 mitigations [`@variant hover (&:hover)` + the toast
pointer-events fix + the space-y v3-semantics restore + the
inline-rgba color discipline], the three test tiers); skills/ excluded
throughout (the eslint ignores + the tsconfig exclude verified live).

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only sha prereleases beyond
[4.14.1-55245d5.0.sha-55245d5, 4.14.1-556d23c.0.sha-556d23c,
4.14.1-d1531a9.0.sha-d1531a9] — no stable 4.14.1, no 5.x exists); the
installed wrapper 4.14.0 + the engine 4.14.0; the lockfile holding the
v68 dedupe state (exactly one `node_modules/axe-core` entry); the
engine-contract pin GREEN standalone (2 passed).

### F2 — the 90th standing checks: ALL GREEN (version-bumped from v89 — version-bump-only diffs verified)

ref-standing-v90.sh + standing-checks-v90.sh (version-bumped from v89
via the persisted derive-standing-v96.py across the THREE token families
[v89→v90, 89th→90th, AND the bare session names ref89→ref90/
clone89→clone90]; after normalizing back the files are version-bump-only:
diffed clean, zero old tokens remaining). Reference side: the four bugs
ALL live [toast-blocker `hitIsBurgerChild:false`; sheet-trap
`overlayCount:1` after nav; no-landmark `navLandmark:false`; the 464px
/networth overflow at 390 — re-measured with the settle-wait after the
first read timed at 390/390 pre-render (the timing-artifact lesson: the
standing script's sleep-3 raced the reference's client-side boot; the
8s+2s settle re-read measured docSW 464 exactly)]; the data census
UNCHANGED (the 90th clean drift check: networth "1 items · $25,000" /
income "1 items · $5000.00" / expenses "4 items · $525.00"); the SEO pair
live (robots.txt allow-all + its sitemap link; sitemap.xml its origin at
1.0 + the app routes at 0.8). Clone side: R1–R4 ALL GREEN — **the mobile
menu VERIFIED WORKING the 90th consecutive time** (`hitIsBurgerChild:
true`, the sheet opens, closes on nav, the nav landmark present — the
Tailwind v4 mitigation holds), zero overflow at 390 on all five views
(docSW 390 on /, /income, /savings, /expenses, /networth), the SEO pair
live.

### F3 — the re-run pair (the v90-lineage derivation, the two-half census form)

The probe series derived from the v90 lineage (derive-v96-series.py,
persisted): vlm-shots-v96.sh + clone-vlmshots-v96.sh + vlm-compare-v96.mjs
+ arbit-v96.sh — the generic swaps (v90→v96, refvlm90→refvlm96,
clonevlm90→clonevlm96, refarbit90→refarbit96, clonearbit90→clonearbit96,
/tmp/vlm90→/tmp/vlm96) followed by the exact-fragment history corrections
(the queue source "the v95 plan's own suggestion", the oldest-remaining
list [v90 < v91 < v92 < v93 < v94 < v95], the FIFTH re-run bracket
[v62/v63 → v69 → v78 → v84 → v90 → v96], FOURTH→FIFTH, the census-axes
provenance "The v90 census axes", the verdict note "the v84/v90 re-runs'
own verdicts") — every correction verified applied (the derive script
reports each hit; one first-run MISS [the verdict-note fragment's
lowercase 'the'] fixed and re-run clean); bash -n + node --check clean on
all four; zero residual old tokens. The census BUILT two-half from the
start (build-twohalf-v96.py — ref-arbit-v96.sh + clone-arbit-v96.sh, the
TWO census JS blocks [NW_CENSUS 42 lines + DASH_CENSUS 87 lines]
extracted once and embedded byte-identically across the halves — the md5
line-block contract [82cf8a43 / 85e4ec7e]; the doubled-brace spot grep
clean — the v95 template-brace lesson pre-applied). The reaping budget
applied as the standing step between every half. Login on the first
attempt both sides; the parked pointer at (5,5); read-only — the v46
rule holds.

**Both verdicts DIFFERENT, every flag DOM-arbitrated to a documented
class:**

1. **PAIR 1 (NETWORTH at 390)**: the stat tiles side-by-side (ref) vs
   stacked (clone) — the **v41 mobile-superset class** (the census
   confirms: the statGrid cols ref "175.828px 175.844px" 2-col vs clone
   "294px" 1-col, the gap 16px IDENTICAL, the tiles ref 176×84 ×2 vs
   clone 294×84 ×2 — the h 84 byte-identical, the w the v41 class; the
   medallion ref right 416 CLIPPING vs clone right 342 visible — the v41
   class; the trendIcon 32×32 byte-identical); **the clipped negative
   figure "-$245,950.00" — the NEW flag this cycle, DOM-arbitrated as a
   VLM MISREAD** (figclip-clone-v96.sh, the supplemental one-shot census:
   the figure H2 at x=48 w=179 h=32, the textRect x=48 w=179 — the text
   starts EXACTLY at the content-left edge [textLeftOfContent 0 — zero
   overhang] and ends 115px INSIDE the content-right [textRightOfContent
   −115]; figureScrolls false; docSW 390 — the figure is fully in-bounds
   on every axis, no clipping exists; the flag rides the VLM's
   perception of the flush-left negative figure against the gradient);
   the "Edit with Base44" overlay — the platform-chrome class; the
   figures/counts/groups — the seed-data classes.
2. **PAIR 2 (DASHBOARD at 390)**: the "Edit with Base44" tooltip over
   the breakdown rows — the Base44 platform-chrome class; the subtitle
   wrap-point (ref wraps after "to" / clone after "expenses") — the
   **v62 width-delta class** (the census confirms the chrome
   byte-identical [fs 16px/fw 400/rgb(107,114,128)/lh 24px, the P h 48,
   the block h 92] and BOTH sides render 2 DOM lines; the reference's
   own 395px docSW overflow shifts its wrap by one word); the donut
   4-segments-vs-3 + the proportions + the stat figures — the seed-data
   classes.

The both-sides census (the two-half controlled form) **REPRODUCES the
v90 census values EXACTLY — zero drift on every axis**:

- **NETWORTH**: the summary card {ref 432×333 right 448 on its 464
  docSW vs clone 358×421 right 374 on its fitting 390 — the v41 class};
  the statGrid {cols ref "175.828px 175.844px" vs clone "294px", the gap
  16px IDENTICAL, 2 children both}; the tiles {ref 176×84 ×2 vs clone
  294×84 ×2 — the h 84 byte-identical, the w the v41 class}; the
  medallion {64×64 both, ref right 416 clipping vs clone right 342
  visible — the v41 class}; the trendIcon {32×32 both,
  byte-identical}.
- **DASHBOARD**: the subtitle {fs 16px/fw 400/rgb(107,114,128)/lh 24px,
  the P h 48, the block h 92, 2 lines — BYTE-IDENTICAL; the wrap-point
  delta the v62 width-delta class}; the breakdown card {358×324 vs ref
  363×324 — the w the v62 page-width class, the h byte-identical}; the
  svg family {svgCount 7, the [16,14,16,14] size family,
  rechartsWrappers 0, pieSectors 0 — BYTE-IDENTICAL}; the children {the
  H3 h 20 + the DIV h 238 byte-identical, the w 308-vs-313 the
  page-width class}; the spendingCard finder {the same fallback string
  "no Spending Breakdown heading" on BOTH sides — the heading is a div,
  not an h1-h4, on both sites (the parity-correct rendering)}.

**NO NEW CLONE GAP — the v96 iteration PIN-ONLY.**

### F4 [PIN] — the summary-card HEAD-ROW typography + the FIGURE-FIT census at 390 (PIN-ONLY for src/ — no production-code change; +1 e2e = 299)

The never-pinned family (the FAMILY-EXTENSION pattern — the v93
label-first lesson): the networth summary card's HEAD-ROW text chrome at
mobile 390. The figure's typography family is pinned at 640 (the v41 F2
pin: font 48px + weight 700 — fs/fw, NO color) and at 1280 (the v60 F1
pin: {48px, 700, white} full family) — but at 390 the v41 F3 pin holds
the figureFont fs 24px ONLY; **the figure's fw + color are NEVER pinned
at 390**. The label's family {fs, color} is pinned at 1280 only (the
v60-era census.label) — **never at 390**. The figure's FIT contract
(the figclip arbitration's own axes — the flush-left start, the
in-bounds right, the no-scroll state) is never pinned at ANY viewport.
The dashboard's hero figure at dashboard.spec.ts:1896 is a DIFFERENT
element (the Net Zero Goal card's 30px figure — untouched by this pin's
scope).

**The pin's own axes first measured byte-identical on BOTH sides** by
the supplemental two-half census (headrow-arbit-v96.sh +
headrow-clone-v96.sh — BUILT two-half from the start via
build-headrow-v96.py, the census JS byte-identical by the md5
line-block diff [519ef222 — 48 lines]; both sides read-only; the
seedcheck exact after the run; the doubled-brace spot grep clean):

- The label ("Total Net Worth" leaf): {fs `14px`, fw `400`, color
  `rgba(255, 255, 255, 0.8)`, mb `8px`, h 20} — **FULL byte-identity
  across sides** (the text-sm family, viewport-independent).
- The figure's fw `700` + color `rgb(255, 255, 255)` — byte-identical
  (the font-bold text-white family at the 24px tier).
- The flush-left start: the figure el x=48 = textRect x=48 = contentL 48
  on BOTH sides (textLeftOverhang 0) — byte-identical.
- The no-scroll state: figureScrolls `false` on both sides —
  byte-identical.
- The pad arithmetic: padL/padR 32 on both sides — byte-identical.
- The documented-class deltas (NOT pin axes): the card w {ref 432 vs
  clone 358 — the v41 class}; the figure fs {ref 48px vs clone 24px —
  the v41 superset fix} + its lh corollary {48 vs 32}; the figure text +
  el w + textRect w + textRightMargin {ref "$25,000.00" w 304 margin 64
  vs clone "-$245,950.00" w 179 margin 116 — the seed-data class}; the
  docSW {ref 464 vs clone 390 — the R-bug-4 class vs the superset
  zero-overflow}.

**The pin** (tests/e2e/networth.spec.ts, appended as the v96 describe
block): the census finder is the supplemental census's own finder
verbatim (the gradient-card finder + the label leaf + the largest-$-font
figure walk); asserts — the figure {fs `24px`, fw `700`, color
`rgb(255, 255, 255)`, lh `32px`} + the el {x 48, h 32} + the textRect
{x 48} at 390; the label {fs `14px`, fw `400`, color `rgba(255, 255,
255, 0.8)`, mb `8px`, h 20}; the FIT contract {textLeftOverhang 0,
textRightMargin ≥ 0, figureScrolls false}; the card {w 358, pad 32/32}
re-affirm (the v41 arithmetic); the docSW 390 guard. The right-margin
axis asserted as the IN-BOUNDS contract (≥ 0), never the exact value
(the margin is data-dependent — the figure string's length).

**The pin-sanity mutation (the planned form)**: the figure h2's
`break-words text-2xl font-bold text-white sm:text-5xl` → `break-words
text-2xl font-bold max-sm:font-extrabold text-white sm:text-5xl`
(net-worth-view.tsx:348, by LINE NUMBER — the line-scoping keeps the
stat-tile VALUE's `text-2xl font-bold text-white` at line 372 untouched
[the v90 pin's own surface]; AT-max-sm because the pin runs at 390 and
the variant is INERT at ≥640 — the 640-tier v41 F2 fw pin and the
1280-tier v60 F1 figure pin both stay green; the v90 LESSON APPLIED:
the bare font-bold swap cascades to the 640/1280 tiers, the
viewport-scoped dodge confines the flip). Expected: the pin FAILS at
exactly the figure fw axis alone (`700` → `800` below 640px);
cascade-free BY CONSTRUCTION (font-weight never changes line-height —
the figure's lh stays text-2xl's 32px, the h 32 and the card-height
arithmetic [421, the v63 F3 pin] unchanged; font-weight never affects
color; the in-bounds contract holds its 116px slack at fw 800;
`max-sm:` appears NOWHERE in src/ [verified]; no spec asserts the
figure's fw below 640 — this pin is the first). Then restored (git
diff src/ = 0 lines; the standalone REBUILD via the FULL npm run
build; the post-restore full networth.spec.ts run green).

**The disproven-in-advance candidates (documented without execution):**
the label fs mutation (text-sm → text-base: the label h 20 → 24 → the
head-row block height → the card-height arithmetic 421 → cascades to the
v63 F3 pin — the v86 ratio-line-height trap family); the label mb
mutation (mb-2 → mb-1: the head-row height −8 → the same cardH cascade);
the figure fs mutation (text-2xl → text-xl: the lh 32 → 28 → the figure
h → the cardH cascade); the figure color mutation (text-white →
text-slate-100: a clean single-axis candidate but the fw axis is the
sharper demonstration — the v90 precedent's own choice).

## The ToDo list

| # | Step | Status |
|---|------|--------|
| 1 | F0 baseline chain on the carried-over workspace | DONE — all green |
| 2 | F1 axe-core watch | DONE — NO DRIFT |
| 3 | F2 90th standing checks (derived v89→v90, version-bump-only verified) | DONE — ALL GREEN |
| 4 | F3 the v90-lineage probe derivation (generic swaps + exact-fragment history corrections + residual checks) | DONE |
| 5 | F3 two-half census builder (build-twohalf-v96.py, md5 contract) + both halves executed | DONE |
| 6 | F3 the VLM pairwise | DONE — both verdicts DIFFERENT, all flags arbitrated |
| 7 | F3 the figclip one-shot arbitration (the NEW clipped-figure flag) | DONE — VLM misread, in-bounds proven |
| 8 | F4 the supplemental headrow two-half census (the pin's own axes measured byte-identical) | DONE |
| 9 | F4 THIS PLAN written + validated BEFORE the pin's execution | DONE |
| 10 | F4 append the v96 pin to tests/e2e/networth.spec.ts | PENDING |
| 11 | F4 pin first run (GREEN expected) | PENDING |
| 12 | F4 pin-sanity mutation (net-worth-view.tsx:348, line-number-scoped, max-sm dodge) → single-axis failure → restore (git diff src/ = 0) → standalone REBUILD → post-restore full file run | PENDING |
| 13 | F5 full chain re-run (lint/typecheck/108 unit/build/299 e2e/35 smoke) + the screenshots regeneration + byte-compare | PENDING |
| 14 | D1–D7 docs alignment + session_230.md + the worklog Session 131 entry | PENDING |
| 15 | ship: the full chain re-run + commit + SSH-wrapper push | PENDING |

## The pre-execution validation section (the measured evidence)

- The pin's measured values (the headrow two-half census, this session):
  label {fs 14px, fw 400, color rgba(255,255,255,0.8), mb 8px, h 20}
  byte-identical; figure fw 700 + color rgb(255,255,255) byte-identical;
  the flush-left start (el x 48 = textRect x 48 = contentL 48,
  textLeftOverhang 0) byte-identical; figureScrolls false byte-identical;
  the clone's own axes — figure {fs 24px, lh 32px, el x48 w179 h32,
  textRect x48 w179}, the card {x 16, w 358, padL 32, padR 32,
  contentR 342}, the fit {textRightMargin 116, docSW 390}; the
  seedcheck exact after the run.
- The mutation target line verified by reading the source:
  net-worth-view.tsx:348 — `<h2 className="break-words text-2xl
  font-bold text-white sm:text-5xl">` (the figure; the stat-tile value's
  identical class string sits at line 372, untouched by the
  line-number scoping; the figure is the ONLY `break-words` carrier in
  the file — the grep-verified uniqueness anchor).
- The coverage-map grep (run across ALL specs): the figure's fw is
  asserted ONLY at networth.spec.ts:738 (the 640 tier) and
  networth.spec.ts:1683 (the 1280 tier) — no spec asserts it at 390;
  the dashboard.spec.ts:1896 figure is the HERO card's 30px figure (a
  different element in a different view); the label's computed style is
  asserted ONLY at networth.spec.ts:1684 (the 1280 tier); `max-sm:`
  appears nowhere in src/; no spec asserts the figure's
  textRect/fit axes at any viewport.
- The rotation ledger verified: the twins last re-shot v90 = the oldest
  remaining [v90 < v91 < v92 < v93 < v94 < v95] — the v95-era docs' v96
  suggestion agreeing with the ledger (the NINETEENTH consecutive
  agreement), the surface names verified against vlm-shots-v90.sh's own
  header before the derivation.
- The pin's finder: the supplemental census's own finder verbatim (the
  NW_CENSUS gradient-card finder + the label leaf finder [the v41 F3
  idiom] + the largest-$-font figure walk [the figclip finder]) — proven
  stable across this session's three independent runs (figclip +
  headrow-ref + headrow-clone).

## Operational lessons this cycle (the probe README's D6 section)

- THE STANDING-SCRIPT TIMING ARTIFACT (NEW): the reference-side
  standing check's R-bug-4 (/networth overflow) read docSW 390/390 on
  the script's sleep-3 — the eval raced the reference's client-side
  boot and measured the PRE-RENDER document; the 8s+2s settle re-read
  measured the true 464. The discipline: when a standing bug check
  reads CLEAN against its own documented-live history, re-measure with
  an explicit settle-wait before recording any state change — a bug
  that has been live for 89 consecutive checks does not vanish on the
  90th without a DOM-visible cause.
- THE FLUSH-LEFT FIGURE PERCEPTION CLASS (NEW): the VLM flags a
  "clipped" negative currency figure when the text starts flush at the
  content-box left edge (textLeftOverhang 0) — the arbitration is the
  Range-walk textRect vs the padding-aware content box (the figclip
  census form), NOT the element rect alone (the element rect equals the
  text rect here; only the content-box comparison proves in-bounds).
- THE TWO-HALF FORM AS THE DEFAULT (the v92..v95 lesson, applied clean
  again): every census this cycle (the pair census + the supplemental)
  BUILT two-half from the start — zero resource-exhaustion symptoms.
- THE DERIVATION MISS-REPORT DISCIPLINE (from the v95 second-pass
  lesson): the derive script reports every correction's hit/miss — the
  one first-run MISS (the lowercase 'the' in the verdict-note fragment)
  was caught by the report itself and fixed before any probe executed.

## The next queue (the v97 suggestion — verify against the rotation ledger before executing)

(1) the re-run cadence rotates to the next-oldest candidate after the
twins (the v91-era ITEMS pair [the INCOME + EXPENSES view pair at
desktop 1280x800], last re-shot v91 — now the oldest remaining
[v91 < v92 < v93 < v94 < v95 < v96]; the pair's SIXTH re-run
[v57 → v64 → v70 → v79 → v85 → v91 → v97] — verify against
vlm-shots-v91.sh's own header before the derivation), (2) the axe-core
watch at its next re-check point (only a 5.x wrapper changes the
calculus), (3) the deferred reference-write censuses (unchanged — out
of bounds under the v46 read-only rule).
