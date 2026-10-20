# Remediation Plan v100 — the re-run cycle's next-oldest candidate (the v94-era NETWORTH + DRILL-DOWN pair's sixth re-run) + the axe watch + the networth tablist→section-row junction census pin (PIN-ONLY)

The formal narrative: `docs/session_239.md` (the v99 cycle's own narrative
log). The queue: the v99 plan's v100 suggestion — **the ledger-verified
target** (the v99-era docs' suggestion AGREEING with the rotation ledger:
the v94-era NETWORTH + DRILL-DOWN pair [the networth view + the dashboard
drill-down EXPANDED state, both desktop 1280x800 full-page], last re-shot
v94 — now the oldest remaining [v94 < v95 < v96 < v97 < v98 < v99]; the
pair's SIXTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100] — the
TWENTY-THIRD consecutive queue/ledger agreement), plus the axe-core watch
at its re-check point and the 94th standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 303.**

## The pre-execution ledger verification (the queue-prose verification lesson, applied)

The rotation ledger's authority is the PROBE LINEAGE, never the prose
queue phrasing. Verified against `scripts/parity-probes/vlm-shots-v94.sh`
before the derivation: its own header reads "a fresh re-run of the v88-era
pair … the desktop 1280x800 FULL-PAGE state of (1) the NETWORTH view and
(2) the DASHBOARD's drill-down EXPANDED state. The pair's FIFTH re-run
[v60 → v67 → v76 → v82 → v88 → v94] — the SEVENTEENTH consecutive
queue/ledger agreement" — matching the queue's phrasing exactly (no
transcription error; the v94-era surface names confirmed: the NETWORTH
view + the dashboard drill-down EXPANDED state at desktop 1280x800). The
SIXTH re-run bracket [v60 → v67 → v76 → v82 → v88 → v94 → v100]
constructed from the same header's FIFTH bracket. The
standing-checks pair (ref-standing-v94.sh + standing-checks-v94.sh)
derived from v93 across the THREE token families (v93→v94, 93rd→94th,
ref93→ref94/clone93→clone94), version-bump-only verified by normalizing
back and diffing clean (zero old tokens remaining — the persisted
derive-standing-v100.py, both halves bash -n clean).

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items
/ 3 assets / 2 liabilities) before any flow ran; lint ✓ · typecheck ✓ ·
108/108 unit ✓ · `npm run build` ✓ (robots + sitemap prerendered) ·
**302 e2e ✓** (108 + 116 + 83 chunk executions across three chunk splits
of the 23 spec files + the setup project = 307 total = 302 unique tests —
the exact documented v99 state; zero flakes on the FIRST run) · 35/35
smoke ✓. The workspace: the FRESH-CLONE class (the sandbox reset — the
v86/v88/v90/v91/v92/v98 precedent: git clone at main @ fd06b78; npm
install; `.env` written [DATABASE_URL="file:../db/custom.db"]; db/
re-seeded [the seedcheck exact]; chromium-1243 installed for the pinned
@playwright/test 1.63.0 — the cache's 1200 build belongs to a different
playwright generation; the tool-results dir re-created for
with-server.sh). The two commits since the v99 push (b43db6f + fd06b78)
audited session-log-only (docs/session_240.md + docs/session_241.md —
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
engine-contract pin GREEN standalone (a11y.spec.ts 23/23).

### F2 — the 94th standing checks: ALL GREEN (version-bumped from v93 — version-bump-only diffs verified)

ref-standing-v94.sh + standing-checks-v94.sh (version-bumped from v93
via the persisted derive-standing-v100.py across the THREE token
families [v93→v94, 93rd→94th, AND the bare session names ref93→ref94/
clone93→clone94]; after normalizing back the files are version-bump-only:
diffed clean, zero old tokens remaining). Reference side: the four bugs
ALL live [toast-blocker `hitIsBurgerChild:false`; sheet-trap
`overlayCount:1` after nav; no-landmark `navLandmark:false`; the 464px
/networth overflow at 390 measured docSW 464 directly]; the data census
UNCHANGED on the FIRST read (networth "1 items · $25,000" / income "1
items · $5000.00" / expenses "4 items · $525.00" — no render-race this
cycle); the SEO pair live. Clone side: R1–R4 ALL GREEN — **the mobile
menu VERIFIED WORKING the 94th consecutive time**
(`hitIsBurgerChild: true`, the sheet opens, closes on nav, the nav
landmark present — the Tailwind v4 mitigation holds), zero overflow at
390 on all five views, the SEO pair live.

### F3 — the re-run pair (the v94-lineage derivation, the two-half census form)

The probe series derived from the v94 lineage (derive-v100-series.py,
persisted): vlm-shots-v100.sh + clone-vlmshots-v100.sh +
vlm-compare-v100.mjs + arbit-v100.sh — the generic swaps
(refvlm94→refvlm100, clonevlm94→clonevlm100, refar94→refar100,
clonear94→clonear100, /tmp/vlm94→/tmp/vlm100, v94→v100) followed by the
exact-fragment history corrections (last-re-shot v88→v94, FIFTH→SIXTH,
the re-run bracket extension, the oldest-remaining bracket [v94 < v95 <
v96 < v97 < v98 < v99], the agreement ordinal SEVENTEENTH→TWENTY-THIRD,
the census-axes reference v88→v94) — every correction verified applied
(the derive script reports each hit/miss; zero misses this cycle). bash
-n + node --check clean on all four; zero residual old tokens (the
legitimate v60-era/v67/v75/v82 pin-provenance tokens whitelisted by
context). The census BUILT two-half from the start (build-twohalf-v100.py
— ref-arbit-v100.sh + clone-arbit-v100.sh, the TWO census JS blocks
[ARBIT_A 90 lines + ARBIT_B 111 lines] extracted once and embedded
byte-identically across the halves — the md5 line-block contract
[50e0cbf2 / cb3afbfc]). The reaping budget applied as the standing step
between every half (the clone half's first run read EMPTY census output —
65 stale chromium processes from the reference half reaped, then clean;
the v89/v91-documented symptom class). Login on the first attempt both
sides; the parked pointer at (5,5); read-only — the v46 rule holds.

**The verdicts: the NETWORTH pair IDENTICAL — zero layout/style flags
(only the expected data classes + the platform-chrome FAB); the
DRILL-DOWN pair DIFFERENT (the documented re-run class) — every flag
DOM-arbitrated to a documented class:**

1. The "Dashboard nav item highlighted in the clone, not the reference"
   — the **v56 SUPERSET class** (the reference's root-route bug: it marks
   NO nav item active at `/`; the clone's Dashboard highlight is
   superset fix #3, pinned by mobile-navigation.spec.ts. The census:
   navHighlight INERT rgb(63,63,70)/fw 400 on the reference vs ACTIVE
   rgb(255,255,255)/fw 500 on the clone, radius 8px identical — the
   deliberate superset delta, NOT a drift).
2. The "avatar U vs P" — the **user-identity class** (the census's
   avatarLetter U-vs-D — each site's own logged-in user; the VLM's "P"
   misread of the clone's "D" the v43 perception rule applied).
3. The "Edit with Base44 FAB present in the reference, absent in the
   clone" — the **platform-chrome class** (the reference's Base44
   platform iframe chrome — the v97-documented fabCount 0 +
   bodyHasBase44 false on BOTH sides: the FAB never renders in the app
   DOM).
4. The "donut percentage labels absent on the reference, present on the
   clone (81.6/13.8/4.6%)" — the **v60 perception class** (the census
   proving the reference's own labels ARE in its DOM: donutLabels count
   4, texts ["92.3%4.6%3.1%", "92.3%", "4.6%", "3.1%"], labelLineCount
   0, labelFs 16px, labelFill rgb(0,0,0), sectors 3 — the chrome
   byte-identical to the clone's [count 4, labelLineCount 0, labelFs
   16px, labelFill rgb(0,0,0), sectors 3]; the reference's own seed data
   renders its three labels OVERLAPPING (the merged first text) and
   illegible to the VLM, the clone's well-separated. The v76 F4 pin
   holds the chrome).
5. The "donut slice proportions differ" — the **seed-data class** (each
   site's own data drives the sector angles; the fills + order pinned by
   the early dashboard spec).

The both-sides census (the two-half controlled form) **REPRODUCES the
v88/v94 census values EXACTLY — zero drift on every axis:**

- **The DRILL-DOWN census (PART A)**: the navHighlight (the reference
  INERT rgb(63,63,70)/400 vs the clone ACTIVE white/500 — the v56
  SUPERSET class); the avatarLetter (U vs D — the user-identity class);
  the progress (trackW 568/trackH 12/trackBg rgba(255,255,255,0.1)
  byte-identical, fillW 173-vs-357 the pct DATA class, the fill gradient
  family byte-identical); the donutLabels (count 4, labelLineCount 0,
  labelFs 16px, labelFill black, sectors 3 — byte-identical chrome; the
  texts each site's own data); the statTrendIcons (16×16, the per-type
  color, the polyline glyphSig, viewBox 0 0 24 24 — byte-identical);
  statCardCount 3 both sides; the heroTrendGlyphs (the full 7-glyph
  family byte-identical); the docSW 1280 guard.
- **The NETWORTH summary-card census (PART B)**: the card 960×333/
  32px/16px/the 135deg forest→lime gradient/the rgba(26,58,46,0.3)
  0px 20px 60px shadow; the headRow h 76/mb 32px/flex/center; the label
  14px/rgba(255,255,255,0.8)/mb 8px/h 20; the figure 48px/700/white/
  lh 48px/h 48; the medallion 64×64/rgba(255,255,255,0.2)/icon 32×32;
  the statGrid 440px 440px/84px/16px/896; the statTile 440×84/16px/
  12px/rgba(255,255,255,0.1)/blur(10px)/label 12px-16-4px/amt 24px-700-32;
  the ratioFooter 24px/24px/1px rgba(255,255,255,0.2)/h 53/label 14px/
  val 18px-700 — the labelBlock's WIDTH the ONE delta (ref 304 vs clone
  357 — the v82 DATA-CONDITIONAL width class: the 48px figure's text
  length); the docSW 1280 guard.

**NO NEW CLONE GAP — the v100 iteration PIN-ONLY.**

### F4 [PIN] — the networth TABLIST→SECTION-ROW junction census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 303)

The never-pinned family (the FAMILY-EXTENSION pattern — the v94
missing-middle lesson applied to the networth view's INTER-BLOCK RHYTHM):
the junction between the tablist and the Assets section row — the
TabsContent's `mt-6` gap. The v41 F2 pin (640) walks the UPPER rhythm
only (headerToCard 32 + cardToTablist 32 — the two mb-8 gaps above the
tablist); the v60 F1 pin (1280) walks the summary card + tablist
interiors (w/h/template/maxW/pad — no rhythm axes); the v94 F4 pin (1280)
walks the section row's own chrome + the row-to-group rhythm (the
space-y-6 INSIDE the TabsContent) — **the JUNCTION between them (the
tablist bottom → section row top gap) is NEVER pinned at ANY viewport in
ANY spec** (the coverage-map grep across all 24 specs: zero specs assert
any TabsContent margin; zero specs assert any tablist-to-section gap;
the only mt-6 assertions in the suite are the summary card's ratio
footer — a different element).

**The pin's own axes first measured byte-identical on BOTH sides** by
the supplemental two-half census (nwjunction-arbit-v100.sh +
nwjunction-clone-v100.sh — BUILT two-half from the start via
build-nwjunction-v100.py, the census JS byte-identical by the md5
line-block contract [5f124436 — 26 lines]; both sides READ-ONLY login +
passive navigation — the v46 rule holds; the seedcheck exact after the
clone half):

- The TABLIST: {w 448, h 36, bottom 525, template "220px 220px", maxW
  "448px", pad "4px"} — byte-identical across sides (the v60 F1 family
  re-anchored in the junction context).
- The SECTION ROW: {top 549, h 56, w 960, display flex, justify
  space-between} — byte-identical across sides (the v94 F4 family
  re-anchored).
- **THE JUNCTION: {gap 24}** — the tablist's bottom (525) to the
  section row's top (549) — byte-identical across sides (the
  TabsContent's mt-6; the never-pinned axis).
- The continuation: the groupH3 {fs 18px, fw 600, mb 12px} + the
  rowToGroup {gap 24} — byte-identical (the v94 families re-measured in
  the junction context).
- The docSW 1280 guard on both sides.

Every axis is DATA-INDEPENDENT (the structural chrome — the tablist
geometry, the section row's structure, the TabsContent's unconditional
mt-6 margin; no seed data touches any axis) — the v98
data-independent-panel strength class: the pin asserts the
cross-side-verified values directly.

**The pin** (tests/e2e/networth.spec.ts, appended as the v100 describe
block): navigate to /networth at 1280×800 → the junction census walk
(the tablist via [role="tablist"], the section row via the v94 "Assets"
h2 finder) → asserts the full junction family above + the docSW 1280
guard.

**The pin-sanity mutation (the planned form)**: the assets TabsContent's
`mt-6` → `mt-8` (src/components/budget/net-worth-view.tsx:415, by LINE
NUMBER — the line carries EXACTLY ONE mt-6, grep-count verified). 
Expected: the pin FAILS at exactly the junction gap axis alone (24 →
32); cascade-free BY CONSTRUCTION (a vertical margin never changes any
width/height/chrome axis; the v41 F2 rhythm axes sit ABOVE the tablist;
the v94 F4 row chrome is position-relative within the row's own
coordinate space; the v60 F1 tablist interior axes are untouched; no
other spec asserts any tablist-to-section gap or any absolute y-position
below the tablist — this pin is the first; the LINE-NUMBER scoping keeps
the liabilities TabsContent's own mt-6 at line 479 untouched). NOTE the
v98 mutation-rebuild discipline: the mutation only bites after the
standalone REBUILD (the e2e runs the PREBUILT .next/standalone server).
Then restored (git diff src/ = 0 lines; the standalone REBUILD via the
FULL npm run build; the post-restore full file run green).

**The disproven-in-advance candidates (documented without execution):**
the mt-6 → mt-4 mutation (gap 24→16 AND — none other: a single-axis
failure, but the WEAKER form — the planned mt-8 form reads the clearer
32px delta against the 24px pinned value); the space-y-6 → space-y-4
mutation on the same line (rowToGroup 24→16 AND junction untouched —
fails the WRONG axis, the v94 family); the h2 text-2xl → text-xl
mutation (the v94 h2 family: fs/fw/lh/h — four axes).

## The ToDo list

| # | Step | Status |
|---|------|--------|
| 1 | F0 baseline chain on the fresh-clone workspace (seedcheck exact; lint/typecheck/108 unit/build ✓; 302 e2e zero flakes on the first run; 35/35 smoke) | DONE — all green |
| 2 | F1 axe-core watch | DONE — NO DRIFT |
| 3 | F2 94th standing checks (derived v93→v94, version-bump-only verified) | DONE — ALL GREEN (census clean on the first read) |
| 4 | F3 the v94-lineage probe derivation (generic swaps + exact-fragment history corrections + residual checks; zero misses) | DONE |
| 5 | F3 two-half census builder (build-twohalf-v100.py, md5 contract) + both halves executed (the reaping budget between halves) | DONE |
| 6 | F3 the VLM pairwise | DONE — networth IDENTICAL, drill-down DIFFERENT (all flags arbitrated) |
| 7 | F4 the supplemental nwjunction two-half census (the pin's own axes measured byte-identical) | DONE |
| 8 | F4 THIS PLAN written + validated BEFORE the pin's execution | DONE |
| 9 | F4 append the v100 pin to tests/e2e/networth.spec.ts | PENDING |
| 10 | F4 pin first run (GREEN expected) | PENDING |
| 11 | F4 pin-sanity mutation (net-worth-view.tsx:415, line-number-scoped) → single-axis failure after the REBUILD → restore (git diff src/ = 0) → standalone REBUILD → post-restore full file run | PENDING |
| 12 | F5 full chain re-run (lint/typecheck/108 unit/build/303 e2e/35 smoke) + the screenshots regeneration + byte-compare | PENDING |
| 13 | D1–D7 docs alignment + session_242.md + the worklog Session 135 entry | PENDING |
| 14 | ship: the full chain re-run + commit + SSH-wrapper push | PENDING |

## The pre-execution validation section (the measured evidence)

- The pin's measured values (the nwjunction two-half census, this
  session): tablist {w 448, h 36, bottom 525, template "220px 220px",
  maxW "448px", pad "4px"} byte-identical; sectionRow {top 549, h 56,
  w 960, display flex, justify space-between} byte-identical; junction
  {gap 24} byte-identical; groupH3 {fs 18px, fw 600, mb 12px}
  byte-identical; rowToGroup {gap 24} byte-identical; docSW 1280 both
  sides; the seedcheck exact after the clone half.
- The mutation target line verified by reading the source:
  src/components/budget/net-worth-view.tsx:415 — the assets
  TabsContent's className carries EXACTLY ONE `mt-6` (grep-count 1 on
  the line); the liabilities TabsContent's own `mt-6 space-y-6` sits at
  line 479 — untouched by the line-number scoping.
- The coverage-map grep (run across ALL 24 specs): zero specs assert
  any TabsContent margin (zero `TabsContent` matches in any spec file);
  zero specs assert any tablist-to-section gap; the only mt-6
  assertions in the suite are the summary card's ratio footer (a
  different element) — this pin is the FIRST on the family.
- The rotation ledger verified: the networth + drill-down pair last
  re-shot v94 = the oldest remaining [v94 < v95 < v96 < v97 < v98 <
  v99] — the v99-era docs' v100 suggestion agreeing with the ledger (the
  TWENTY-THIRD consecutive agreement), the surface names verified
  against vlm-shots-v94.sh's own header before the derivation.
- The pin's finder: the tablist via `[role="tablist"]` (labelled on BOTH
  sides — the v60 reference census's own finder); the section row via
  the v94 "Assets" h2 → block → row finder (proven stable across both
  census halves this cycle and the v94 nwsection census).

## Operational lessons this cycle (the probe README's D6 section)

- THE REAPING BUDGET AS THE STANDING STEP (the v89/v91 symptom class,
  re-confirmed): the clone census half's FIRST run read EMPTY output —
  65 stale chromium processes from the reference half's sessions; after
  the reap the identical script ran clean. The two-half form is
  necessary but not sufficient — the reaping BETWEEN halves is
  load-bearing on this sandbox.
- THE CLEAN-PARENTHETICAL DERIVATION (a derivation-quality note): the
  v94-era headers' "the v89-era pair covered by v90" parenthetical
  carried an internally-confused rotation framing (decoded this cycle
  via the v83/v88/v89 headers: "the vN-era pair covered by vM" = the
  pair re-shot at vM); the v100 headers use the clean form ("the
  v94-era pair last re-shot v94 — now the oldest remaining [v94 < v95 <
  …]") — future derivations should carry the clean form forward.
- THE JUNCTION-COMPLETE RHYTHM MAP (a coverage-map note): the networth
  view's inter-block rhythm is now FULLY pinned — headerToCard 32 +
  cardToTablist 32 (v41 F2, 640) + tablistToSection 24 (THIS pin, 1280)
  + rowToGroup 24 + groupToGrid 12 (v94 F4, 1280) — the
  family-extension survey should walk the JUNCTIONS between pinned
  blocks, not just the blocks' interiors.

## The next queue (the v101 suggestion — verify against the rotation ledger before executing)

(1) the re-run cadence rotates to the next-oldest candidate after the
networth + drill-down pair (the v95-era DASHBOARD pair [the dashboard
view + …, both desktop 1280x800 full-page], last re-shot v95 — now the
oldest remaining [v95 < v96 < v97 < v98 < v99 < v100]; the pair's SIXTH
re-run bracket to be verified against vlm-shots-v95.sh's own header
before the derivation), (2) the axe-core watch at its next re-check
point (only a 5.x wrapper changes the calculus), (3) the deferred
reference-write censuses (unchanged — out of bounds under the v46
read-only rule).
