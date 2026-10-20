# Remediation Plan v101 — the re-run cycle's next-oldest candidate (the v95-era DASHBOARD pair's sixth re-run) + the axe watch + the spending+guidelines 2-col row grid / spending-card box census pin (PIN-ONLY)

The formal narrative: `docs/session_244.md` (the v100 cycle's own narrative
log). The queue: the v100 plan's v101 suggestion — **the ledger-verified
target** (the v100-era docs' suggestion AGREEING with the rotation ledger:
the v95-era DASHBOARD pair [the dashboard FULL-PAGE's below-the-fold
surfaces — the BUDGET GUIDELINES card + the QUICK-ACTION row, both desktop
1280x800 full-page], last re-shot v95 — now the oldest remaining [v95 <
v96 < v97 < v98 < v99 < v100]; the pair's SIXTH re-run [v61 → v68 → v77 →
v83 → v89 → v95 → v101] — the TWENTY-FOURTH consecutive queue/ledger
agreement), plus the axe-core watch at its re-check point and the 95th
standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 304.**

## The pre-execution ledger verification (the queue-prose verification lesson, applied)

The rotation ledger's authority is the PROBE LINEAGE, never the prose
queue phrasing. Verified against `scripts/parity-probes/vlm-shots-v95.sh`
before the derivation: its own header reads "a fresh re-run of the
v89-era pair … the DASHBOARD at desktop 1280x800, FULL-PAGE, last re-shot
v89 — now the oldest remaining [v89 < v90 < v91 < v92 < v93 < v94]; the
pair's FIFTH re-run [v61 → v68 → v77 → v83 → v89 → v95] — the EIGHTEENTH
consecutive queue/ledger agreement" — matching the queue's phrasing (the
v95-era surface names confirmed: the DASHBOARD FULL-PAGE at desktop
1280x800; the two v61-era below-the-fold target surfaces: the BUDGET
GUIDELINES card + the QUICK-ACTION row). The SIXTH re-run bracket
[v61 → v68 → v77 → v83 → v89 → v95 → v101] constructed from the same
header's FIFTH bracket. The standing-checks pair (ref-standing-v95.sh +
standing-checks-v95.sh) derived from v94 across the THREE token families
(v94→v95, 94th→95th, ref94→ref95/clone94→clone95), version-bump-only
verified by normalizing back and diffing clean (zero old tokens remaining
— the persisted derive-standing-v101.py, both halves bash -n clean).

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items
/ 3 assets / 2 liabilities) before any flow ran; lint ✓ · typecheck ✓ ·
108/108 unit ✓ · `npm run build` ✓ (robots + sitemap prerendered) ·
**303 e2e ✓** (115 + 92 + 98 chunk executions across three disjoint file
splits of the 24 spec files + the setup project = 305 total = 303 unique
tests — the exact documented v100 state [302 spec + the v100 pin +
1 setup], the count first derived authoritatively via
`playwright test --list`; zero flakes on the FIRST run) · 35/35 smoke ✓.
The workspace: the FRESH-CLONE class (the sandbox reset — the
v86/v88/v90/v91/v92/v98/v100 precedent: git clone at main @ 840e25c; npm
install; `.env` written [DATABASE_URL="file:../db/custom.db"]; db/
re-seeded [the seedcheck exact]; chromium-1243 installed for the pinned
@playwright/test 1.63.0; the tool-results dir re-created for
with-server.sh). The two commits since the v100 push (1a5c5bb + 840e25c)
audited session-log-only (docs/session_243.md + docs/session_244.md —
ZERO src/ or lockfile deltas).

The codebase audit clean: the production seams re-audited — auth
(scrypt/HMAC + timingSafeEqual), the db-path contract (db-path.ts + its
unit test), the SEO pair (robots.ts allow-all + sitemap.ts 5-URL
structure — both prerendered by the build), the Tailwind v4 mitigations
(`@variant hover (&:hover)` + `@variant group-hover` + the toast
pointer-events fix), the three test tiers; skills/ excluded throughout
(the eslint ignores + the tsconfig exclude verified live).

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (dist-tags: rc/next sha
prereleases only beyond — no stable 4.14.1, no 5.x exists); the
installed wrapper 4.14.0 + the engine 4.14.0; the lockfile holding the
v68 dedupe state (exactly one `node_modules/axe-core` entry); the
engine-contract pin GREEN standalone (2 passed).

### F2 — the 95th standing checks: ALL GREEN (version-bumped from v94 — version-bump-only diffs verified)

ref-standing-v95.sh + standing-checks-v95.sh (version-bumped from v94
via the persisted derive-standing-v101.py across the THREE token
families [v94→v95, 94th→95th, AND the bare session names ref94→ref95/
clone94→clone95]; after normalizing back the files are version-bump-only:
diffed clean, zero old tokens remaining). Reference side: the four bugs
ALL live [toast-blocker `hitIsBurgerChild:false`; sheet-trap
`overlayCount:1` after nav; no-landmark `navLandmark:false`; the 464px
/networth overflow at 390 measured docSW 464 directly]; the data census
UNCHANGED on the FIRST read (networth "1 items · $25,000" / income "1
items · $5000.00" / expenses "4 items · $525.00" — no render-race this
cycle); the SEO pair live. Clone side: R1–R4 ALL GREEN — **the mobile
menu VERIFIED WORKING the 95th consecutive time**
(`hitIsBurgerChild: true`, the sheet opens, closes on nav, the nav
landmark present — the Tailwind v4 mitigation holds), zero overflow at
390 on all five views, the SEO pair live.

### F3 — the re-run pair (the v95-lineage derivation, the two-half census form)

The probe series derived from the v95 lineage (derive-v101-series.py,
persisted): vlm-shots-v101.sh + clone-vlmshots-v101.sh +
vlm-compare-v101.mjs + arbit-v101.sh — the generic swaps
(refvlm95→refvlm101, clonevlm95→clonevlm101, refar95→refar101,
clonear95→clonear101, /tmp/vlm95→/tmp/vlm101, v95→v101) followed by the
exact-fragment history corrections (last-re-shot v89→v95, FIFTH→SIXTH,
the re-run bracket extension, the oldest-remaining bracket [v95 < v96 <
v97 < v98 < v99 < v100], the agreement ordinal EIGHTEENTH→TWENTY-FOURTH,
the previous-verdict reference v89→v95, the "after v89-v94"→"after
v95-v100", the census-axes drift-check baseline→v95) — every correction
verified applied (the derive script reports each hit/miss; zero misses
this cycle; the line-count-preservation check green on all four files —
the two-half builder inherits the v95 line boundaries). bash -n + node
--check clean on all four; zero residual old tokens (the legitimate
v45/v46/v51/v60/v61/v64/v66/v68/v73/v75/v83 pin-provenance tokens
whitelisted by context). The census BUILT two-half from the start
(build-twohalf-v101.py — ref-arbit-v101.sh + clone-arbit-v101.sh, the
THREE census JS blocks [ARBIT_G 61 lines + ARBIT_Q 58 lines + ARBIT_X 25
lines] byte-identical across the halves — the md5 line-block contract
[b500dd29 / da04e995 / 7a381755 — the v95 census blocks verbatim]). The
reaping budget applied as the standing step between every half (the
v89/v91/v100-documented symptom class). Login on the first attempt both
sides; the parked pointer at (5,5); read-only — the v46 rule holds.

**The verdict: IDENTICAL — ZERO layout/style flags on the pair's own
target surfaces (the FOURTH consecutive IDENTICAL verdict for this pair
[v83 → v89 → v95 → v101]).** The only flags the documented standing
classes: the root-URL active-nav highlight (the v56 SUPERSET class — the
reference's root-route bug marks NO nav item active at /), the avatar
U-vs-D (the user-identity class), and the seed-data figures (the
allocation bar, the balance, the stat figures, the donut proportions —
each site's own data).

The both-sides census (the two-half controlled form) **REPRODUCES the
v89/v95 census values EXACTLY — zero drift on every axis:**

- **PART G (the guidelines card)**: the card 468×348/radius 12px/border
  rgb(229,231,227)/bg white/the header pad 24px/fs 16px/fw 600/
  rgb(26,58,46)/lh 16px/tracking -0.4px/the body pad 0px 24px 24px/the
  three tiles 418×78 with the Needs/Wants/Savings tints and the full
  label/pct/desc chrome — the only delta the shadow's transparent
  lead-layer count (the v66 computed-form INVISIBLE class).
- **PART Q (the quick-action row)**: the grid 304px x3/gap 24px/w 960/
  the three cards 304×90/radius 16px/pad 24px/white/border/the 40×40
  tinted tiles/the 20px icons/the labels/the 0.5-opacity pluses/
  transition 0.2s — the TWO census deltas both documented classes (the
  grid mt [ref 0px vs clone 32px — the rendered gap IDENTICAL at 340,
  the v77 mechanism class] and the label finder's wrapper catch [ref
  leaf 500/rgb(26,58,46) vs clone wrapper 400/rgb(10,10,10) — the v61
  label lesson: the clone's LEAF span carries the identical chrome,
  pinned green by the v61 F3 pin]).
- **PART X (the cross-row gap)**: cardBottom 1122/gridTop 1462/gap 340
  on BOTH sides, byte-identical.

**NO NEW CLONE GAP — the v101 iteration PIN-ONLY.**

### F4 [PIN] — the spending+guidelines 2-col row's grid + the Spending Breakdown card's own box/header census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 304)

The never-pinned family (the FAMILY-EXTENSION pattern — the v100
junction-walk lesson applied to the 2-col row: walk what the existing
pins do NOT hold): the v61 F2 pin walks the row ONLY for rowH 656 (the
stretch contract) + the guidelines card's own box; the v77 pin the
guidelines card's interior text; the v83 F4 pin the card-level cross-row
gap (cardBottom 1122/gridTop 1462/gap 340) — but **the ROW'S OWN GRID
CHROME (the lg:grid-cols-2 template "468px 468px", the 24px column gap,
the 960 width, the two children's 468 widths) and the SPENDING CARD'S
OWN BOX + HEADER (the card radius/border/bg/shadow, the title's
typography, the subtitle's chrome, the title→subtitle rhythm, the
body's pt-0 contract) are NEVER pinned at ANY viewport in ANY spec**
(the coverage-map grep across all 24 specs: zero "468px 468px" matches;
zero spending-card radius/border/shadow assertions; the subtitle "Needs
vs Wants vs Savings" only visibility-asserted [dashboard.spec.ts:106];
the only columnGap census the v61 F3 quick-action grid's own).

**The pin's own axes first measured byte-identical on BOTH sides** by
the supplemental two-half census (spending-arbit-v101.sh +
spending-clone-v101.sh — BUILT two-half from the start via
build-spending-v101.py, the census JS byte-identical by the md5
line-block contract [7e6a13c3 — 48 lines]; both sides READ-ONLY login +
passive navigation — the v46 rule holds; the seedcheck exact after the
clone half):

- The ROW: {display "grid", template "468px 468px", colGap "24px",
  w 960} — byte-identical across sides.
- The TWO CHILDREN: [{w 468, display block}, {w 468, display block}] —
  the spending card + the stretched guidelines wrapper, byte-identical.
- The SPENDING CARD: {w 468, radius "12px", border rgb(229,231,227),
  bg rgb(255,255,255)} + the shadow's VISIBLE pair (the clone's 4
  transparent leads vs the reference's 2 — the v66 computed-form
  INVISIBLE class) — byte-identical.
- The HEADER: {pad "24px"} + the title {fs 16px, fw 600, color
  rgb(26,58,46), lh 16px, tracking -0.4px} + the subtitle {text "Needs
  vs Wants vs Savings", fs 14px, fw 400, color rgb(107,114,128), lh
  20px, top 6 (the space-y-1.5 rhythm)} — byte-identical.
- The BODY: {pad "0px 24px 24px"} — the pt-0 contract (the header's own
  p-6 bottom provides the separation), byte-identical.
- The docSW 1280 guard on both sides.

Every axis is DATA-INDEPENDENT (the structural chrome — the row's
lg:grid-cols-2/gap-6 classes and the 960 cap arithmetic, the card's box
classes, the fixed header texts "Spending Breakdown" / "Needs vs Wants
vs Savings" — no seed data touches any axis; the data-locked heights
[h 656] stay with the v61 F2 pin's own rowH contract) — the v98
data-independent-panel strength class: the pin asserts the
cross-side-verified values directly.

**The pin** (tests/e2e/dashboard.spec.ts, appended as the v101 describe
block): navigate to /dashboard at 1280×800 → the spending-row census
walk (the "Spending Breakdown" leaf title → the bordered card walk [the
v61 F2 pattern: shadow + radius + a <p> descendant] → the ancestor
2-col grid walk [the v61 F2 pattern: grid-cols-2 + children 2]) →
asserts the full family above + the docSW 1280 guard.

**The pin-sanity mutation (the planned form)**: the SpendingBreakdownCard's
card `rounded-xl` → `rounded-2xl` (src/components/budget/
dashboard-view.tsx:695, by LINE NUMBER — the line carries EXACTLY ONE
rounded-xl, grep-count verified; the line-scoping keeps the
BudgetGuidelinesCard's own rounded-xl at line 832 untouched).
Expected: the pin FAILS at exactly the card radius axis alone
("12px" → "16px"); cascade-free BY CONSTRUCTION (border-radius never
changes the layout box — the v99 precedent: the login Google button's
rounded-xl → rounded-lg mutation bit the google radius axis ALONE);
no other spec asserts the spending card's radius — this pin is the
first. NOTE the v98 mutation-rebuild discipline: the mutation only bites
after the standalone REBUILD (the e2e runs the PREBUILT .next/standalone
server). Then restored (git diff src/ = 0 lines; the standalone REBUILD
via the FULL npm run build; the post-restore full file run green).

**The disproven-in-advance candidates (documented without execution):**
the subtitle text-sm → text-base mutation (the subtitle fs axis
14px→16px AND the header height +4 → the card h 656→660 → rowH 660 —
fails the v61 F2 pin's rowH 656 too: NOT cascade-free, the WRONG form);
the row's gap-6 → gap-8 mutation (colGap 24→32 AND the children's
widths 468→456 — two axes of THIS pin, and the guidelines card w 468
pinned by the v61 F2 pin → NOT cascade-free); the title's font-semibold
→ font-normal (fw 600→400 — single-axis on the title family but the
WEAKER form; the planned radius form reads the clearer 12px→16px delta
against a never-pinned axis).

## The ToDo list

| # | Step | Status |
|---|------|--------|
| 1 | F0 baseline chain on the fresh-clone workspace (seedcheck exact; lint/typecheck/108 unit/build ✓; 303 e2e zero flakes on the first run; 35/35 smoke) | DONE — all green |
| 2 | F1 axe-core watch | DONE — NO DRIFT |
| 3 | F2 95th standing checks (derived v94→v95, version-bump-only verified) | DONE — ALL GREEN (census clean on the first read) |
| 4 | F3 the v95-lineage probe derivation (generic swaps + exact-fragment history corrections + residual checks + line-count preservation; zero misses) | DONE |
| 5 | F3 two-half census builder (build-twohalf-v101.py, md5 contract) + both halves executed (the reaping budget between halves) | DONE |
| 6 | F3 the VLM pairwise | DONE — IDENTICAL (the fourth consecutive IDENTICAL verdict for this pair; all flags the documented classes) |
| 7 | F4 the supplemental spending two-half census (the pin's own axes measured byte-identical) | DONE |
| 8 | F4 THIS PLAN written + validated BEFORE the pin's execution | DONE |
| 9 | F4 append the v101 pin to tests/e2e/dashboard.spec.ts | PENDING |
| 10 | F4 pin first run (GREEN expected) | PENDING |
| 11 | F4 pin-sanity mutation (dashboard-view.tsx:695, line-number-scoped) → single-axis failure after the REBUILD → restore (git diff src/ = 0) → standalone REBUILD → post-restore full file run | PENDING |
| 12 | F5 full chain re-run (lint/typecheck/108 unit/build/304 e2e/35 smoke) + the screenshots regeneration + byte-compare | PENDING |
| 13 | D1–D7 docs alignment + session_245.md + the worklog Session 136 entry | PENDING |
| 14 | ship: the full chain re-run + commit + SSH-wrapper push | PENDING |

## The pre-execution validation section (the measured evidence)

- The pin's measured values (the spending two-half census, this
  session): row {display "grid", template "468px 468px", colGap "24px",
  w 960} byte-identical; children [{w 468, block}, {w 468, block}]
  byte-identical; card {w 468, radius "12px", border rgb(229,231,227),
  bg white} + the visible shadow pair byte-identical (the lead-layer
  count the v66 INVISIBLE class); header pad "24px"; title {fs "16px",
  fw "600", color rgb(26,58,46), lh "16px", tracking "-0.4px"};
  subtitle {text "Needs vs Wants vs Savings", fs "14px", fw "400",
  color rgb(107,114,128), lh "20px", top 6}; body pad "0px 24px 24px";
  docSW 1280 both sides; the seedcheck exact after the clone half.
- The mutation target line verified by reading the source:
  src/components/budget/dashboard-view.tsx:695 — the
  SpendingBreakdownCard's card div className carries EXACTLY ONE
  `rounded-xl` (grep-count 1 on the line); the BudgetGuidelinesCard's
  own `rounded-xl border bg-card text-card-foreground shadow` sits at
  line 832 — untouched by the line-number scoping.
- The coverage-map grep (run across ALL 24 specs): zero specs assert
  the row's "468px 468px" template or its column gap; zero specs assert
  the spending card's radius/border/bg/shadow; the subtitle only
  visibility-asserted (dashboard.spec.ts:106); the only columnGap
  census the v61 F3 quick-action grid's own — this pin is the FIRST on
  the family.
- The rotation ledger verified: the dashboard pair last re-shot v95 =
  the oldest remaining [v95 < v96 < v97 < v98 < v99 < v100] — the
  v100-era docs' v101 suggestion agreeing with the ledger (the
  TWENTY-FOURTH consecutive agreement), the surface names verified
  against vlm-shots-v95.sh's own header before the derivation.
- The pin's finder: the "Spending Breakdown" leaf title (labelled on
  BOTH sides — the v61/v77 guidelines finder's own pattern) → the
  bordered card walk (shadow + radius + a <p> descendant — proven
  stable across both census halves this cycle) → the ancestor 2-col
  grid walk (grid-cols-2 + children 2 — the v61 F2 row finder, proven
  on both sides).

## Operational lessons this cycle (the probe README's D6 section)

- THE RESIDUAL-CHECK ASYMMETRY (a derivation-quality note): the v101
  residual whitelist must tolerate the NEW-era v95 tokens the history
  corrections introduce ("the v95-era" / "re-shot v95" / "since v95" /
  "after v95-v100") while still flagging the OLD v89-era/FIFTH/
  EIGHTEENTH tokens — the whitelist is era-asymmetric by construction
  and must be re-derived per cycle, never copied blindly.
- THE CUMULATIVE-PIN COUPLING (a mutation-selection note): the
  dashboard's cumulative y-position pins (the v83 F4 cardBottom 1122 /
  gridTop 1462; the v56 F1 hero children y 136) make ANY inter-row
  margin mutation NON-cascade-free — the mutation-selection for
  dashboard-surface pins must target box-chrome axes (radius/border/
  typography), never the inter-row rhythm, unless the cumulative pins
  are re-baselined in the same change.
- THE LEFT-COLUMN COMPLETION (a coverage-map note): the 2-col row's
  coverage is now COMPLETE — the row's own grid chrome + BOTH columns'
  cards (the guidelines card by v61 F2/v77, the spending card by THIS
  pin) + the cross-row junction by v83 F4 — the family-extension survey
  on a two-column row must walk BOTH columns' boxes, not just the
  arbitrarily-chosen first.

## The next queue (the v102 suggestion — verify against the rotation ledger before executing)

(1) the re-run cadence rotates to the next-oldest candidate after the
dashboard pair (the v96-era MOBILE 390 twins pair [the five views'
mobile surfaces at 390x844], last re-shot v96 — now the oldest remaining
[v96 < v97 < v98 < v99 < v100 < v101]; the pair's SIXTH re-run bracket
to be verified against vlm-shots-v96.sh's own header before the
derivation), (2) the axe-core watch at its next re-check point (only a
5.x wrapper changes the calculus), (3) the deferred reference-write
censuses (unchanged — out of bounds under the v46 read-only rule).
