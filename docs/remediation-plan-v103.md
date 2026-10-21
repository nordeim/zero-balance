# Remediation Plan v103 — the re-run cycle's next-oldest candidate (the v97-era ITEMS pair's seventh re-run) + the axe watch + the 97th standing checks + the rail user-footer tile census pin (PIN-ONLY)

The formal narrative: `docs/session_250.md` (the v102 cycle's own narrative
log). The queue: the v102 plan's v103 suggestion — **the ledger-verified
target** (the v102-era docs' suggestion AGREEING with the rotation ledger:
the v97-era ITEMS pair [the INCOME + EXPENSES view pair at desktop
1280x800], last re-shot v97 — now the oldest remaining [v97 < v98 < v99 <
v100 < v101 < v102]; the pair's SEVENTH re-run bracket [v57 → v64 → v70 →
v79 → v85 → v91 → v97 → v103] — the TWENTY-SIXTH consecutive
queue/ledger agreement), plus the axe-core watch at its re-check point and
the 97th standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 306.**

## The pre-execution ledger verification (the queue-prose verification lesson, applied)

The rotation ledger's authority is the PROBE LINEAGE, never the prose
queue phrasing. Verified against `scripts/parity-probes/vlm-shots-v97.sh`
before the derivation: its own header reads "the fresh re-run of the
OLDEST re-run candidate (the v57-era items pair, last re-shot v91 — the
SIXTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v97]" —
matching the queue's phrasing (the v97-era surface names confirmed: the
ITEMS view [income + expenses] at desktop 1280x800, FULL-PAGE; the two
v57-era surfaces). The SEVENTH re-run bracket [v57 → v64 → v70 → v79 →
v85 → v91 → v97 → v103] constructed from the same header's SIXTH bracket.
The standing-checks pair (ref-standing-v97.sh + standing-checks-v97.sh)
derived from v96 across the THREE token families (v96→v97, 96th→97th,
ref96→ref97/clone96→clone97), version-bump-only verified by normalizing
back and diffing clean (zero old tokens remaining — the persisted
derive-standing-v103.py, both halves bash -n clean).

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items
/ 3 assets / 2 liabilities) before any flow ran (the `env -u DATABASE_URL`
discipline); lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓
(robots + sitemap prerendered) · **305 e2e ✓** (117 + 96 + 85 + 10 chunk
executions across four disjoint file splits of the 23 spec files + the
setup project = 308 total = 305 unique tests — the exact documented v102
state [304 spec + the v102 pin + 1 setup], the count first derived
authoritatively via `playwright test --list`; zero flakes on the FIRST
run) · 35/35 smoke ✓. The workspace: the FRESH-CLONE class (the sandbox
reset — the v86/v88/v90/v91/v92/v98/v100/v101 precedent): the environment
re-provisioned from scratch (npm install; `.env` written
[DATABASE_URL="file:../db/custom.db"]; `db/` at the repo root +
db:generate + db:push + db:seed; chromium-1243 installed for the pinned
@playwright/test 1.63.0; the tool-results dir re-created for
with-server.sh). The two commits since the v102 parity push (ef1148c +
0291a6e) audited session-log-only [docs/session_249.md +
docs/session_250.md — ZERO src/ or lockfile deltas].

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

### F2 — the 97th standing checks: ALL GREEN (version-bumped from v96 — version-bump-only diffs verified)

ref-standing-v97.sh + standing-checks-v97.sh (version-bumped from v96
via the persisted derive-standing-v103.py across the THREE token
families [v96→v97, 96th→97th, AND the bare session names ref96→ref97/
clone96→clone97]; after normalizing back the files are version-bump-only:
diffed clean, zero old tokens remaining). Reference side: the four bugs
ALL live [toast-blocker `hitIsBurgerChild:false`; sheet-trap
`overlayCount:1` after nav; no-landmark `navLandmark:false`; the 464px
/networth overflow at 390 measured docSW 464 directly]; the data census
UNCHANGED on the FIRST read (networth "1 items · $25,000" / income "1
items · $5000.00" / expenses "4 items · $525.00" — no render-race this
cycle); the SEO pair live. Clone side: R1–R4 ALL GREEN — **the mobile
menu VERIFIED WORKING the 97th consecutive time**
(`hitIsBurgerChild: true`, the sheet opens, closes on nav, the nav
landmark present — the Tailwind v4 mitigation holds), zero overflow at
390 on all five views, the SEO pair live.

### F3 — the re-run pair (the v97-lineage derivation, the two-half census form)

The probe series derived from the v97 lineage (derive-v103-series.py,
persisted): vlm-shots-v103.sh + clone-vlmshots-v103.sh +
vlm-compare-v103.mjs + arbit-v103.sh — the generic swaps
(refvlm97→refvlm103, clonevlm97→clonevlm103, refarbit97→refarbit103,
clonearbit97→clonearbit103, /tmp/vlm97→/tmp/vlm103, v97→v103) followed
by the exact-fragment history corrections (last-re-shot v91→v97, SIXTH→
SEVENTH, the re-run bracket extension, the other-pairs list bumped to
the current era [savings v98, login+calculator v99, networth+drill-down
v100, dashboard v101, mobile twins v102]) — every correction verified
applied (the derive script reports each hit/miss; zero misses this
cycle; the line-count-preservation check green on all four files — the
two-half builder inherits the v97 line boundaries). bash -n + node
--check clean on all four; zero residual old tokens (the legitimate
v57/v64/v65/v70/v70b/v75/v79/v22/v43/v46/v56 pin-provenance tokens
whitelisted by context). The census BUILT two-half from the start
(build-twohalf-v103.py — ref-arbit-v103.sh + clone-arbit-v103.sh, the
ONE census JS block [CENSUS_JS 193 lines] byte-identical across the
halves — the md5 line-block contract [b55dcd29 — the v97 census block
verbatim]; the doubled-brace spot check clean). The reaping budget
applied as the standing step between halves. Login on the first attempt
both sides; the parked pointer at (5,5); read-only — the v46 rule holds;
the seedcheck exact after the clone half.

**The verdict: BOTH DIFFERENT — the pair's documented verdict class (the
same flag-set classes as the v91/v97 re-runs) with every flag
DOM-arbitrated to a documented class:**

- PAIR 1 (INCOME): the avatar "U" vs "D" → the user-identity class (the
  chrome byte-identical: 36×36 / 9999px / 14px / 600 / white /
  rgb(143,188,63)); the "Edit with Base44" FAB attributed to the CLONE
  (image 2) → the platform-chrome class with the INVERTED attribution
  form (the v85/v91-documented class — re-arbitrated live by the
  one-shot both-sides DOM census base44-fab-arbit-v103.sh: **fabCount 0
  + bodyHasBase44 false on BOTH sides** — the FAB renders in the
  reference's platform iframe chrome, outside the queryable body DOM;
  the v97 re-run saw the non-inverted form — both forms documented);
  the header stats "1 items · $5000.00" vs "2 items · $5550.00" + the
  1-card vs 2-card grid + the card contents (amounts/dates/badges) →
  the seed-data classes; the "Recurring" 4th badge → the
  DATA-CONDITIONAL class (the reference's own income item ships
  recurring=false).
- PAIR 2 (EXPENSES): the payment-method footer chips (the reference's
  expense cards date-only vs the clone's date + chip) → the v57
  DATA-CONDITIONAL class (the census proves the reference RENDERS
  payment chips when data carries them: its own income card's footer
  childCount 2 with the "Bank Account" chip + icon; its expense items
  simply ship no payment method — footer childCount 1 — while the
  clone's carry them); the card grid layout (the reference's 3+1 two-row
  vs the clone's 3 one-row) → the seed-count class (4 vs 3 items); the
  "Edit with Base44" FAB → the platform-chrome class (the non-inverted
  form this pair); the avatar → the user-identity class; the header
  stats + card contents → the seed-data classes.

The both-sides census (the two-half controlled form) **REPRODUCES the
v97 census values EXACTLY — zero drift on every axis:**

- The AVATAR chrome {36×36 / radius 9999px / fs 14px / fw 600 / color
  white / bg rgb(143,188,63)} — byte-identical; the identity text the
  only delta (the user-identity class).
- The GRID + CARD chrome {grid w 960 / gap 16px / the 3-col 309.328px
  template family; card w 309 / pad 20px / radius 12px / border
  rgb(229,231,227)} — byte-identical; the childCount (1 vs 2 income,
  4 vs 3 expenses) the seed-count class; the card h (200 vs 230) the
  v70b-decomposed class; the income template's last-column sub-pixel
  (ref .328 ×3 vs clone .328/.328/.344) the column-distribution
  rounding noise WITHIN the documented 309.328px family.
- The TITLE ROW chrome {gap 8px / dot 8×8 / dotBg per type
  [rgb(143,188,63) income / rgb(224,122,59) expenses] / font 16px /
  weight 600} — byte-identical.
- The AMOUNT leaf chrome {fs 24px / fw 700 / lh 32px / h 32; the
  per-type accents matching} — byte-identical; the texts the seed-data
  class.
- The FOOTER + BADGE chrome {footer flex/space-between/12px/
  rgb(107,114,128)/h 16 with the children flex gap 4px icons 12×12; the
  badge row flex/wrap/8px gap/mb 12px; badge0 radius 6px/pad 2px 10px/
  fs 12px/fw 600/h 22} — byte-identical; the expenses footer childCount
  (1 vs 2) the v57 DATA-CONDITIONAL class; the badgeRow h (22 vs 52) +
  texts the v57 wrap/classification-VALUE classes.
- The FILTER CARD on BOTH variants {the income variant: card 960×86/
  pad 24px/radius 16px/search 447×36 SPANNING/3 children/2 comboboxes
  216×36 at 14px; the expenses variant: search 216×36 NOT spanning/
  4 children/3 comboboxes} — byte-identical (the v64/v70 contract); the
  page header row + the docSW 1280 guard on both views.

**NO NEW CLONE GAP — the v103 iteration PIN-ONLY.**

### F4 [PIN] — the rail's bottom USER-FOOTER tile census at 1280: the border-t wrapper + the tinted tile + the name/subtitle chrome (PIN-ONLY for src/ — no production-code change; +1 e2e = 306)

The never-pinned family (the FAMILY-EXTENSION pattern — the rail's
bottom block, never census'd at ANY viewport): the v79 F4 pin covers the
AVATAR's own chrome (the round 1-2 char element INSIDE the tile —
36×36/9999px/14px/600/white/rgb(143,188,63), pinned at 1280 in
items.spec); the mobile sheet asserts only the TEXTS' visibility
("Budget Pro" / "Track your finances" — mobile-navigation.spec, the
sheet variant); the nav-geometry spec pins the nav LINKS + the brand
block — but **the TILE's own box (the rounded-lg p-3 tinted
rgb(245,248,245) card that carries the avatar), the name/subtitle
typography (the 14px/500/forest-dark "Budget Pro" + the 12px/400/
forest-medium "Track your finances" truncate pair), and the border-t
p-4 wrapper are NEVER pinned in ANY spec at ANY viewport** (the
coverage-map grep across all 23 spec files: zero "245, 248, 245"
assertions outside the dashboard's own rows + the dialog button row
[different elements]; zero user-footer/tile censuses; the only
"Budget Pro" assertions the sheet's two visibility checks).

**The pin's own axes first measured byte-identical on BOTH sides** by
the one-shot both-sides DOM census (userfooter-arbit-v103.sh — the
base44-fab one-shot pattern applied to the family; the census JS
defined ONCE and eval'd on both sides, byte-identical by construction;
both sides READ-ONLY login + passive navigation — the v46 rule holds;
the parked pointer at (5,5); the seedcheck exact after the clone half):

- The TILE: {w 223, h 60, radius 8px, pad 12px, bg rgb(245,248,245),
  display flex, align center, gap 12px} — **byte-identical across
  sides** (the h 60 = pad 12×2 + avatar 36; the w 223 the rail 256 −
  the wrapper pad 32 − the sub-pixel rounding).
- The WRAPPER: {borderTop "1px rgb(229,231,227)", pad 16px, gap 8px,
  display flex} — **byte-identical across sides**.
- The AVATAR: {w 36} — the v79 control re-asserted in the walk.
- The NAME: {text "Budget Pro", fs 14px, fw 500, color rgb(26,58,46),
  text-overflow ellipsis} — **byte-identical across sides** (the static
  copy — the reference's own demo user block carries the same texts).
- The SUBTITLE: {text "Track your finances", fs 12px, fw 400, color
  rgb(45,90,74), text-overflow ellipsis} — **byte-identical across
  sides**.

Every axis is DATA-INDEPENDENT (the structural chrome + the static
copy texts — the identity-dependent avatar TEXT is never asserted, only
its w 36 geometry control; the v98 data-independent-panel strength
class: the pin asserts the cross-side-verified values directly).

**The pin** (tests/e2e/nav-geometry.spec.ts, appended as the v103
describe block): navigate to /income at 1280×800 → the rail walk (the
aside → the v79 avatar finder [the round 1-2 char element] → the tile
[the nearest ancestor with a visible bg + radius] → the wrapper → the
tile's text leaves) → assert the tile {w 223, h 60, radius 8px, pad
12px, bg rgb(245,248,245), flex, center, gap 12px} + the wrapper
{borderTop 1px rgb(229,231,227), pad 16px, gap 8px} + the avatar w 36
control + the name {fs 14px, fw 500, color rgb(26,58,46), ellipsis} +
the subtitle {fs 12px, fw 400, color rgb(45,90,74), ellipsis}.

**The pin-sanity mutation (the planned form)**: the tile's
`rounded-lg` → `rounded-xl` (src/components/budget/sidebar.tsx:116, by
LINE NUMBER — the line carries EXACTLY ONE rounded-lg, grep-count
verified; the line-scoping keeps the NAV LINKS' own rounded-lg at line
79 AND the mobile burger's own rounded-lg at line 227 untouched — the
nav-geometry h-8 pins and the mobile-layout 28×28 pin ride those lines).
Expected: the pin FAILS at exactly the tile radius axis alone
(tile.radius "8px" → "12px"); cascade-free BY CONSTRUCTION
(border-radius never changes the layout box — the v99/v101 precedent);
no other spec asserts the user-footer tile's radius — this pin is the
first. NOTE the v98 mutation-rebuild discipline: the mutation only
bites after the standalone REBUILD (the e2e runs the PREBUILT
.next/standalone server). Then restored (git diff src/ = 0 lines; the
standalone REBUILD via the FULL npm run build; the post-restore full
file run green).

**The disproven-in-advance candidates (documented without execution):**
the tile's `p-3` → `p-2` mutation (pad 12→8 AND h 60→52 — a two-axis
failure diff, not the single-axis discipline); the name's
`text-sm` → `text-base` mutation (fs 14→16 — bites the SHEET variant's
name too, which mobile-navigation asserts only as visibility — single
axis but the radius form is cleaner); the wrapper's `p-4` → `p-2`
mutation (wrapper pad 16→8 AND tile w 223→239 — two axes); the
wrapper's `border-t` removal (borderTop AND the wrapper's own box —
plus it would change the rail's junction rhythm globally).

## The ToDo list

| # | Step | Status |
|---|------|--------|
| 1 | F0 baseline chain on the fresh-clone workspace (seedcheck exact; lint/typecheck/108 unit/build ✓; 305 e2e zero flakes on the first run; 35/35 smoke) | DONE — all green |
| 2 | F1 axe-core watch | DONE — NO DRIFT |
| 3 | F2 97th standing checks (derived v96→v97, version-bump-only verified) | DONE — ALL GREEN (census clean on the first read) |
| 4 | F3 the v97-lineage probe derivation (generic swaps + exact-fragment history corrections + residual checks + line-count preservation; zero misses) | DONE |
| 5 | F3 two-half census builder (build-twohalf-v103.py, md5 contract) + both halves executed (the reaping budget between halves) | DONE |
| 6 | F3 the VLM pairwise + the flag arbitration (the base44-fab one-shot census) | DONE — BOTH DIFFERENT, every flag DOM-arbitrated (NO NEW GAP) |
| 7 | F4 the supplemental user-footer one-shot census (the pin's own axes measured byte-identical) | DONE |
| 8 | F4 THIS PLAN written + validated BEFORE the pin's execution | DONE |
| 9 | F4 append the v103 pin to tests/e2e/nav-geometry.spec.ts | DONE — appended (typecheck clean) |
| 10 | F4 pin first run (GREEN expected) | DONE — GREEN on the first run (9/9 in nav-geometry.spec.ts) |
| 11 | F4 pin-sanity mutation (sidebar.tsx:116, line-number-scoped) → single-axis failure after the REBUILD → restore (git diff src/ = 0) → standalone REBUILD → post-restore full file run | DONE — ONLY the v103 pin red (8 green), the failure diff reads as tile.radius "8px"→"12px" ALONE; restored (git diff src/ = 0); rebuilt; post-restore 9/9 green |
| 12 | F5 full chain re-run (lint/typecheck/108 unit/build/306 e2e/35 smoke) + the screenshots regeneration + byte-compare | DONE — all green; 306 e2e in four chunks (117+96+86+10 = 309 executions = 306 unique, zero flakes); the screenshots 10/16 byte-identical + SIX DATE-class deltas pixel-arbitrated (the fresh-seed +1-day roll — the band decomposition: every delta a text-row band [h 19 glyph rows / the field regions], zero structural bands; the v86/v80/v92 fresh-seed precedent, the updated set committed) |
| 13 | D1–D7 docs alignment + session_251.md + the worklog Session 138 entry | PENDING |
| 14 | ship: the full chain re-run + commit + SSH-wrapper push | PENDING |

## The pre-execution validation section (the measured evidence)

- The pin's measured values (the user-footer one-shot census, this
  session): the tile {w 223, h 60, radius 8px, pad 12px, bg
  rgb(245,248,245), flex, center, gap 12px} byte-identical; the wrapper
  {borderTop "1px rgb(229,231,227)", pad 16px, gap 8px, flex}
  byte-identical; the avatar {w 36} byte-identical; the name {"Budget
  Pro", fs 14px, fw 500, color rgb(26,58,46), ellipsis} byte-identical;
  the subtitle {"Track your finances", fs 12px, fw 400, color
  rgb(45,90,74), ellipsis} byte-identical; the seedcheck exact after
  the clone half.
- The mutation target line verified by reading the source:
  src/components/budget/sidebar.tsx:116 — the tile's opening tag carries
  EXACTLY ONE `rounded-lg` (grep-count 1 on the line); the nav links'
  own `rounded-lg` at line 79 and the mobile burger's own at line 227 —
  untouched by the line-number scoping.
- The coverage-map grep (run across ALL 23 spec files): zero
  "245, 248, 245" assertions on any rail/sidebar element (the matches
  are the dashboard's own rows + the dialog button row — different
  elements); zero user-footer tile censuses; the only "Budget Pro"
  assertions the mobile sheet's two visibility checks; the avatar's
  chrome pinned by the v79 F4 pin (a DIFFERENT element inside the tile)
  — this pin is the FIRST on the user-footer tile family.
- The rotation ledger verified: the ITEMS pair last re-shot v97 = the
  oldest remaining [v97 < v98 < v99 < v100 < v101 < v102] — the
  v102-era docs' v103 suggestion agreeing with the ledger (the
  TWENTY-SIXTH consecutive agreement), the surface names verified
  against vlm-shots-v97.sh's own header before the derivation.
- The pin's finders: the `aside` locator (present on every authed route
  — the v79/a11y precedent), the v79 avatar finder (the round 1-2 char
  element, geometry + content filters only — proven on both sides this
  cycle and re-used by the v103 census itself), the tile walk (the
  nearest ancestor with a visible bg + radius — deterministic on both
  DOMs, proven by the one-shot census), and the text-leaf finder (the
  tile's childless p/span/div elements with >2 char text — the name +
  the subtitle, in DOM order).

## Operational lessons this cycle (the probe README's D6 section)

- THE CHUNK-SPLIT SELF-AUDIT (a baseline-chain note): the F0 e2e
  re-run's chunk filter "items.spec.ts dashboard.spec.ts
  networth.spec.ts" does NOT match item-details.spec.ts (the
  Playwright file filter is a path regex — "items.spec" ≠
  "item-details.spec"); the v102-era three-chunk record (116+93+97)
  silently rode a different split. The lesson: derive the per-chunk
  file lists from `ls tests/e2e/*.spec.ts` explicitly and SUM the
  per-file `--list` counts against the authoritative total before
  declaring the baseline green — the four-chunk form this cycle
  (117+96+85+10 = 308 executions = 305 unique) is the auditable split.
- THE ONE-SHOT CENSUS FORM FOR SMALL FAMILIES (a probe-form note): the
  user-footer arbitration ran as a single both-sides script (the
  base44-fab pattern) rather than the two-half split — legitimate for
  SMALL censuses (one element family, one eval per side) where the
  chromium-exhaustion budget is not in play; the two-half form remains
  the default for the multi-view census series (the v92..v95 lesson).
- THE INVERTED-FAB ATTRIBUTION IS A STANDING CLASS (a VLM-arbitration
  note): the v103 PAIR 1 attributed the "Edit with Base44" FAB to the
  CLONE (image 2) — the opposite of PAIR 2's attribution in the SAME
  comparison run; both forms are documented (v85/v91 inverted, v97
  non-inverted) and both arbitrate identically (fabCount 0 +
  bodyHasBase44 false on BOTH sides — the FAB lives in the reference's
  platform iframe chrome, outside the queryable body DOM). Future
  cycles expect EITHER form without surprise.

## The next queue (the v104 suggestion — verify against the rotation ledger before executing)

(1) the re-run cadence rotates to the next-oldest candidate after the
items pair (the v98-era SAVINGS pair, last re-shot v98 — now the oldest
remaining [v98 < v99 < v100 < v101 < v102 < v103]; the pair's re-run
bracket to be verified against vlm-shots-v98.sh's own header before the
derivation), (2) the axe-core watch at its next re-check point (only a
5.x wrapper changes the calculus), (3) the deferred reference-write
censuses (unchanged — out of bounds under the v46 read-only rule).
