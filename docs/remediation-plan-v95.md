# Remediation Plan v95 — the re-run cycle's next-oldest candidate (the v89-era dashboard pair's fifth re-run) + the axe watch + the quick-action transition-timing census pin (PIN-ONLY)

The formal narrative: `docs/session_227.md` (the v94 cycle's own narrative
log). The queue: the v94 plan's v95 suggestion — **the ledger-verified
target** (the v94-era docs' suggestion AGREEING with the rotation ledger:
the v89-era DASHBOARD pair [the BUDGET GUIDELINES card + the QUICK-ACTION
card row — both below-the-fold surfaces of the dashboard FULL-PAGE at
desktop 1280x800] — last re-shot v89, the oldest remaining
[v89 < v90 < v91 < v92 < v93 < v94]; the pair's FIFTH re-run
[v61 → v68 → v77 → v83 → v89 → v95] — the EIGHTEENTH consecutive
queue/ledger agreement), plus the axe-core watch at its re-check point
and the 89th standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 298.**

## The pre-execution ledger verification (the queue-prose verification lesson, applied)

The rotation ledger's authority is the PROBE LINEAGE, never the prose
queue phrasing. Verified against `scripts/parity-probes/vlm-shots-v89.sh`
before the derivation: its own header reads "a fresh re-run of the
v61-era pair (… the oldest remaining standing pair: the DASHBOARD at
desktop 1280x800, FULL-PAGE …): Both v61 target surfaces live below the
fold on the same view: (1) the BUDGET GUIDELINES card — the tinted,
bordered 50/30/20 rows … — and (2) the QUICK-ACTION card row — the three
Add Income / Add Savings / Add Expense card buttons" — matching the
queue's phrasing exactly (no transcription error this cycle). The re-run
bracket verified against the same script's header — v95 is the FIFTH
re-run [v61 → v68 → v77 → v83 → v89 → v95]. The standing-checks pair
(ref-standing-v89.sh + standing-checks-v89.sh) derived from v88 across
the three token families (v88→v89, 88th→89th, ref88→ref89/
clone88→clone89), version-bump-only verified by normalizing back and
diffing clean (zero old tokens remaining).

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered) · **297 e2e ✓** (106 + 98 + 95 chunk executions
across three chunk splits of the 23 files = 299 total = 297 unique tests
[296 chromium + 1 setup, the setup re-run per chunk as the project
dependency] — the exact documented v94 state, zero flakes on the first
run) · 35/35 smoke ✓. The workspace: a FRESH CLONE provisioned this
session (npm install at the identical lockfile; `.env`
[DATABASE_URL="file:../db/custom.db"], `db/` at the repo root with
custom.db pushed + seeded, chromium-1243 installed) at main @ e0f99f2
(the session-log-only commit — ZERO src/ or lockfile deltas since the
v94 push ca38efa); the seedcheck exact (7 items / rent 1850 /
expensesTotal 2235 / 0 line items / 3 assets / 2 liabilities) before any
flow ran, no orphaned servers.

The codebase audit clean: the v94 commit (ca38efa) verified PIN-ONLY as
documented (24 files, +2500/−5, ZERO src/ changes); the one commit since
(e0f99f2) session-log-only (docs/session_227.md + skills/ additions —
the skills/ folder excluded from checking/testing/compilation
throughout, verified live by the eslint ignores + the tsconfig exclude);
the production seams re-audited (auth scrypt/HMAC, the db-path contract
[db-path.ts + its unit test], the SEO pair [robots.ts + sitemap.ts —
both prerendered by the build], the Tailwind v4 mitigations
[`@variant hover (&:hover)` + the toast pointer-events fix + the space-y
v3-semantics restore + the inline-rgba color discipline], the three test
tiers).

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only canary prereleases beyond
— no stable 4.14.1, no 5.x exists); the installed wrapper 4.14.0 + the
engine 4.14.0; the lockfile holding the v68 dedupe state (the
eslint-plugin-jsx-a11y engine deduped); the engine-contract pin GREEN
standalone (2 passed).

### F2 — the 89th standing checks: ALL GREEN (version-bumped from v88 — version-bump-only diffs verified)

ref-standing-v89.sh + standing-checks-v89.sh (version-bumped from v88 —
after normalizing the THREE token families [v88→v89, 88th→89th, AND the
bare session names ref88→ref89/clone88→clone89] the files are
version-bump-only: verified by normalizing back and diffing clean, zero
old tokens remaining). Reference side: the four bugs ALL live
[toast-blocker `hitIsBurgerChild:false`; sheet-trap `overlayCount:1`
after nav; no-landmark `navLandmark:false`; the 464px /networth overflow
at 390]; the data census UNCHANGED (the 89th clean drift check: networth
"1 items · $25,000" / income "1 items · $5000.00" / expenses
"4 items · $525.00"); the SEO pair live (robots.txt + sitemap.xml). Clone
side: R1–R4 ALL GREEN — **the mobile menu VERIFIED WORKING the 89th
consecutive time** (`hitIsBurgerChild:true`, the sheet opens, closes on
nav, the nav landmark present — the Tailwind v4 mitigation holds), zero
overflow at 390 on all five views, the SEO pair live.

### F3 — the re-run pair: the verdict IDENTICAL — zero style flags on the pair's own surfaces (the THIRD consecutive IDENTICAL [v83 → v89 → v95])

The probe series (the v89 lineage, sed-derived with the version +
session-name + tmp-dir substitutions [vlm89→vlm95, v89→v95,
FOURTH→FIFTH, TWELFTH→EIGHTEENTH, refar89→refar95, clonear89→clonear95
— the bare-number families caught by the grep verification, the v94
second-pass lesson]; the headers history-corrected to the FIFTH re-run
[v61 → v68 → v77 → v83 → v89 → v95] + "last re-shot v89" + the
oldest-remaining bracket [v89 < v90 < v91 < v92 < v93 < v94] + the
v89-era-pair correction; the functional bodies verified
version-bump-only by the normalize-back diff — only the intentional
history-correction comment lines differ):

- vlm-shots-v95.sh — the REFERENCE side (login on the first attempt;
  the parked pointer at (5,5); read-only — the v46 rule).
- clone-vlmshots-v95.sh — the CLONE side (the with-server :3200 parity
  server; no fixture writes).
- vlm-compare-v95.mjs — the VLM pairwise.
- arbit-v95.sh — the both-sides census (the v89 PART G/Q/X axes
  re-measured; the census runs regardless of the verdict — the v75
  convention). Executed in the CONTROLLED TWO-HALF FORM BUILT TWO-HALF
  FROM THE START (build-twohalf-v95.py — the ARBIT_G/ARBIT_Q/ARBIT_X
  census blocks extracted once and embedded byte-identically across the
  halves, the md5 line-block contract [b500dd29 / da04e995 / 7a381755]):
  ref-arbit-v95.sh + clone-arbit-v95.sh.
- build-qa-timing-v95.py → qa-timing-arbit-v95.sh +
  qa-timing-clone-v95.sh — the supplemental one-shot census for the
  v95 pin's own axes (the v87..v94 supplemental precedent, BUILT
  two-half from the start; the census JS byte-identical by the md5
  line-block diff [ba296202]).

**The VLM verdict: IDENTICAL.** Zero style flags on the pair's own
target surfaces (the Budget Guidelines card + the Quick Action cards
both "visually identical"). The only flags the documented standing
classes: the DATA differences (the seed-data classes — the allocation
bar 30.5%-vs-62.8%, the balance $3475-vs-$2065, the stat figures, the
donut proportions), the root-URL active-nav highlight (the v56 SUPERSET
class — the reference's link INERT vs the clone's ACTIVE), the "Edit
with Base44" FAB (the platform-chrome class — the reference's platform
iframe chrome, fabCount 0 + bodyHasBase44 false on both sides per the
v85/v91/v94 live re-arbitrations), and the avatar "U" vs "D" (the
user-identity class).

**The both-sides census REPRODUCES the v89 census values EXACTLY —
zero drift on every axis:**

1. PART G (the guidelines card): 468×348 / radius 12px / border
   rgb(229,231,227) / bg white / the header pad 24px, fs 16px, fw 600,
   rgb(26,58,46), lh 16px, tracking −0.4px / the body pad 0px 24px 24px,
   display block / the three tiles 418×78, radius 8px, pad 16px, the
   Needs/Wants/Savings tints, the label 16px/500, the pct 14px/400, the
   desc 12px/lh 16px — the ONLY delta the card shadow's transparent
   lead-layer count (the v66 computed-form INVISIBLE class, the visible
   layers byte-identical).
2. PART Q (the quick-action row): the grid 304px×3 / gap 24px / w 960;
   the three cards 304×90 / radius 16px / pad 24px / white / border /
   the 40×40 radius-12 tinted tiles / the 20px icons / the 0.5-opacity
   pluses / transition 0.2s — the TWO census deltas both documented
   classes: the grid mt (ref 0px vs clone 32px — the rendered gap
   IDENTICAL at 340, the v77 mechanism class) and the label finder's
   wrapper catch (ref leaf 500/rgb(26,58,46) vs clone wrapper
   400/rgb(10,10,10) — the v61 label lesson re-confirmed: the clone's
   LEAF span carries the identical 500/rgb(26,58,46), pinned green by
   the v61 F3 pin's leaf-span finder).
3. PART X (the cross-row gap): cardBottom 1122 / gridTop 1462 / gap 340
   on BOTH sides, byte-identical.

**NO NEW CLONE GAP — the v95 iteration is PIN-ONLY.**

### F4 [PIN] — the quick-action TRANSITION-TIMING family census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 298)

The never-pinned family: the quick-action row's TRANSITION-TIMING
chrome. The v89 pin holds the cards' transitionDuration
("0.2s") + transitionProperty ("all") ONLY — never the timing function,
never the delay. The three tinted tiles' transition-transform family
(`transition-transform duration-200 group-hover:scale-110`) and the
three plus icons' transition-opacity family (`transition-opacity
group-hover:opacity-100`) are never pinned at ANY viewport (the v61 F3
pin holds the tile's GEOMETRY + the plus's resting opacity/color; the
v77 pin the icons' viewBox; grep-verified: zero spec matches for
transitionTimingFunction/transitionDelay/cubic-bezier on the dashboard
surfaces, zero for transition-transform/scale-110 anywhere).

**The pin's own axes first measured byte-identical on BOTH sides** by
the supplemental two-half census (qa-timing-arbit-v95.sh +
qa-timing-clone-v95.sh — BUILT two-half from the start via
build-qa-timing-v95.py, the census JS byte-identical by the md5
line-block diff [ba296202]; BOTH sides read-only; the seedcheck exact
after the run):

- The three cards' transitionTimingFunction: `cubic-bezier(0.4, 0, 0.2, 1)`
  — byte-identical (Tailwind's default timing, both sides).
- The three cards' transitionDelay: `0s` — byte-identical.
- The three tiles' transitionDuration `0.2s` + transitionTimingFunction
  `cubic-bezier(0.4, 0, 0.2, 1)` — byte-identical; the tiles'
  transitionProperty the ONE delta — **the v95 TAILWIND v4
  COMPUTED-FORM class (NEW this cycle, now documented)**: the reference
  (v3) computes `transform` while the clone (v4) computes
  `transform, translate, scale, rotate` (the v4 utility's expanded
  property list; the rendered behavior identical — the tile's only
  animated property `scale` covered by BOTH lists). The property axis
  pinned in the CONTAINS form (`toContain("transform")`), never exact.
- The three pluses' transitionProperty `opacity` + transitionDuration
  `0.15s` + transitionTimingFunction `cubic-bezier(0.4, 0, 0.2, 1)` +
  transitionDelay `0s` — byte-identical on all four axes.
- The docSW 1280 guard.

**The pin-sanity mutation (the planned form)**: the card's
`transition-all duration-200` → `transition-all duration-200
lg:ease-linear` (dashboard-view.tsx:885, by LINE NUMBER — the
line-scoping keeps the file's OTHER `transition-all duration-200`
instance [line 578, the breakdown category card] untouched; AT-lg
because the pin runs at 1280). Expected: the pin FAILS at exactly the
cardTiming axis alone (`cubic-bezier(0.4, 0, 0.2, 1)` → `linear` at
≥1024px); cascade-free BY CONSTRUCTION (a timing-function flip affects
no geometry and no computed style any other pin asserts — the v89
transition-pin precedent's own argument; `lg:ease-linear` appears
NOWHERE in src/ [verified: only the un-prefixed `ease-in-out` in
dialog.tsx, a different element]; no spec asserts the quick-action
card's transitionTimingFunction — this pin is the first).

## The ToDo list

| # | Step | Status |
|---|------|--------|
| 1 | F0 baseline chain (lint/typecheck/unit/build/e2e/smoke) on the fresh-clone workspace | DONE — all green |
| 2 | F1 axe-core watch | DONE — NO DRIFT |
| 3 | F2 89th standing checks (derived v88→v89, version-bump-only verified) | DONE — ALL GREEN |
| 4 | F3 the v89-lineage probe derivation (sed families + second-pass session names + header history corrections + normalize-back verification) | DONE |
| 5 | F3 two-half census builder (build-twohalf-v95.py, md5 contract) + both halves executed | DONE |
| 6 | F3 the VLM pairwise | DONE — verdict IDENTICAL |
| 7 | F4 the supplemental qa-timing two-half census (the pin's own axes measured byte-identical) | DONE |
| 8 | F4 THIS PLAN written + validated BEFORE the pin's execution | DONE |
| 9 | F4 append the v95 pin to tests/e2e/dashboard.spec.ts | PENDING |
| 10 | F4 pin first run (GREEN expected) | PENDING |
| 11 | F4 pin-sanity mutation (dashboard-view.tsx:885, line-number-scoped) → single-axis failure → restore (git diff src/ = 0) → standalone REBUILD → post-restore full file run | PENDING |
| 12 | F5 full chain re-run (lint/typecheck/108 unit/build/298 e2e/35 smoke) + the screenshots regeneration + byte-compare | PENDING |
| 13 | D1–D7 docs alignment + session_228.md + the worklog Session 130 entry | PENDING |
| 14 | ship: the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | PENDING |

## The pre-execution validation section (the measured evidence)

- The pin's measured values (the qa-timing two-half census, this
  session): cardTiming `cubic-bezier(0.4, 0, 0.2, 1)` ×3; cardDelay
  `0s` ×3; tileTransition {prop contains "transform", dur `0.2s`,
  timing `cubic-bezier(0.4, 0, 0.2, 1)`} ×3; plusTransition {prop
  `opacity`, dur `0.15s`, timing `cubic-bezier(0.4, 0, 0.2, 1)`, delay
  `0s`} ×3; docSW 1280 — byte-identical on both sides except the tile's
  transitionProperty computed-form class (documented above).
- The mutation target line verified by reading the source:
  dashboard-view.tsx:885 — `className="group rounded-2xl border p-6
  text-left transition-all duration-200 hover:shadow-lg"` (the
  quick-action card button; the file's other `transition-all
  duration-200` at line 578 untouched by the line-number scoping).
- The coverage-map grep (run across ALL specs): NO spec asserts the
  quick-action card's transitionTimingFunction or transitionDelay at
  any viewport; NO spec asserts the tiles' transition-transform family
  or the pluses' transition-opacity family anywhere; the only
  cubic-bezier assertion is networth.spec.ts:1287 (the NETWORTH card's
  composite transition string, a different surface); the items.spec.ts
  transitionDur pins are the ITEM card's own family; `lg:ease-linear`
  appears nowhere in src/.
- The rotation ledger verified: the dashboard pair last re-shot v89 =
  the oldest remaining [v89 < v90 < v91 < v92 < v93 < v94] — the
  v94-era docs' v95 suggestion agreeing with the ledger (the
  EIGHTEENTH consecutive agreement), the surface names verified against
  vlm-shots-v89.sh's own header before the derivation.
- The pin's finder: the census's own finder verbatim (the exact-text
  regex on the button trio — the v61 F3/v89 finder; the tile's
  radius-12 bounding-box finder — the v61 F3 finder; the LAST-svg
  plus finder — the v61 F3/v89 finder) — proven stable across the
  v61/v83/v89/v95 censuses.

## Operational lessons this cycle (the probe README's D6 section)

- THE TEMPLATE-BRACE GENERATOR BUG (NEW): the two-half generator script
  (build-qa-timing-v95.py) was written with .format()-style doubled
  braces but applied with .replace() — the generated LOGIN_JS kept
  literal `{{`/`}}`, a JS syntax error that made agent-browser eval
  return EMPTY on every attempt (the empty-eval signature). The symptom
  matched the v89 resource-exhaustion class but the cause was the
  generator. The discipline: bash -n + a spot grep for doubled braces
  after ANY generator run, before executing the probe; a manual
  open+snapshot diagnosis separates site-down from script-broken.
- THE TWO-HALF FORM AS THE DEFAULT (the v92/v93/v94 lesson, applied
  clean): the v95 census was BUILT two-half from the start (the builder
  extracts the census blocks once, the md5 line-block contract) — zero
  resource-exhaustion symptoms, no mid-run splits needed.
- THE v4 TRANSITION-PROPERTY COMPUTED-FORM CLASS (NEW): Tailwind v4's
  `transition-transform` computes `transform, translate, scale, rotate`
  where v3 computed `transform` — a property-LIST superset with
  identical rendered behavior. The pin form for such axes: CONTAINS,
  never exact (the v66 shadow lead-layer / v82 labelBlock width /
  v94 margin-attribution family's newest member).

## The next queue (the v96 suggestion — verify against the rotation ledger before executing)

(1) the re-run cadence rotates to the next-oldest candidate after this
pair (the v90-era MOBILE 390 twins [the /networth + the dashboard
FULL-PAGE pair at 390x844], last re-shot v90 — now the oldest remaining
[v90 < v91 < v92 < v93 < v94 < v95]; the pair's FIFTH re-run
[v62/v63 → v69 → v78 → v84 → v90 → v96] — verify against
vlm-shots-v90.sh's own header before the derivation), (2) the axe-core
watch at its next re-check point (only a 5.x wrapper changes the
calculus), (3) the deferred reference-write censuses (unchanged — out
of bounds under the v46 read-only rule).
