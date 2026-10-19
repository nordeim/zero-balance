# Remediation Plan v92 — the re-run cycle's next-oldest candidate (the v86-era savings pair's fifth re-run) + the axe watch + the savings filter-interior + search-icon census pin (PIN-ONLY)

The formal narrative: `docs/session_221.md` (the v91 cycle's own narrative
log). The queue: the v91 plan's v92 suggestion — **the ledger-verified
target** (the v91-era docs' suggestion AGREEING with the rotation ledger:
the v86-era SAVINGS pair [the SAVINGS view at desktop 1280x800,
FULL-PAGE] — last re-shot v86, the oldest remaining
[v86 < v87 < v88 < v89 < v90 < v91]; the pair's FIFTH re-run
[v58 → v65 → v74 → v80 → v86 → v92] — the FIFTEENTH consecutive
queue/ledger agreement), plus the axe-core watch at its re-check point
and the 86th standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 295.**

## The pre-execution ledger verification (the queue-prose verification lesson, applied)

The rotation ledger's authority is the PROBE LINEAGE, never the prose
queue phrasing. Verified against `scripts/parity-probes/vlm-shots-v86.sh`
before the derivation: its own surface list reads "the SAVINGS view at
desktop 1280x800, FULL-PAGE — the fresh sweep of the re-run cycle's
OLDEST candidate (the v80-era savings pair, last re-shot v80 ...)" —
the SAVINGS view at desktop 1280x800 full-page, matching the queue's
phrasing exactly this cycle (no transcription error to correct). The
re-run bracket verified against the same scripts' header ("the pair's
FOURTH re-run [v58 → v65 → v74 → v80 → v86]") — v92 is the FIFTH
re-run. The standing-checks pair (ref-standing-v86.sh +
standing-checks-v86.sh) derived from v85 across the three token
families (v85→v86, 85th→86th, ref85→ref86/clone85→clone86),
version-bump-only verified by normalizing back and diffing clean (zero
old tokens remaining).

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered) · **294 e2e ✓** (132 + 108 + 56 chunk executions
across three chunk splits of the 23 files = 296 total = 294 unique tests
[293 chromium + 1 setup, the setup re-run per chunk as the project
dependency] — the exact documented v91 state, zero flakes on the first
run) · 35/35 smoke ✓. The workspace REBUILT (the fresh-clone path, the
v86/v88/v90/v91 precedent): `git clone` at main @ e520a61, the tree
clean; the environment re-provisioned (npm ci 354 packages; `.env`
written [DATABASE_URL="file:../db/custom.db"], `db/` at the repo root,
db:generate + db:push + db:seed; chromium-1243 installed; the paramiko
ssh shim deployed outside the repo at /home/z/my-project/bin/ssh); the
seedcheck exact (7 items / rent 1850 / 0 line items / 3 assets /
2 liabilities) before any flow ran, no orphaned servers.

The codebase audit clean: the v91 commit (c794a7c) re-verified PIN-ONLY
as documented (21 files, +2161/-6, ZERO src/ changes); the one commit
since (e520a61) session-log + skills-folder-only (docs/session_221.md +
skills/ additions — the skills/ folder excluded from
checking/testing/compilation throughout, verified live by the eslint
ignores + the tsconfig exclude); the production seams re-audited (auth
scrypt/HMAC, the db-path contract, the SEO pair [robots.ts +
sitemap.ts — both prerendered by the build], the Tailwind v4
mitigations [`@variant hover (&:hover)` + the toast pointer-events fix +
the space-y v3-semantics restore + the inline-rgba color discipline],
the three test tiers).

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next
prereleases beyond — no stable 4.14.1, no 5.x exists); the installed
wrapper 4.14.0 + the engine 4.14.0; the lockfile holding the v68 dedupe
state (no nested engine dir under node_modules/@axe-core/playwright/);
the engine-contract pin GREEN standalone (2 passed).

### F2 — the 86th standing checks: ALL GREEN (version-bumped from v85 — version-bump-only diffs verified)

ref-standing-v86.sh + standing-checks-v86.sh (version-bumped from v85 —
after normalizing the THREE token families [v85→v86, 85th→86th, AND the
bare session names ref85→ref86/clone85→clone86] the files are
version-bump-only: verified by normalizing back and diffing clean, zero
old tokens remaining). Reference side: the four bugs ALL live
[toast-blocker `hitIsBurgerChild:false`; sheet-trap
`overlayCount:1` after nav; no-landmark `navLandmark:false`; the 464px
/networth overflow at 390]; the data census UNCHANGED (the 86th clean
drift check: networth "1 items · $25,000" / income "1 items · $5000.00"
/ expenses "4 items · $525.00"); the SEO pair live. Clone side: R1–R4
ALL GREEN — the mobile navigation menu VERIFIED WORKING (the **86th
consecutive time**: `hitIsBurgerChild:true`, the sheet opens, closes on
nav, the nav landmark present), zero overflow at 390 on all five views
(docSW 390 everywhere), the SEO pair live.

### F3 — the re-run pair (the v86-era savings pair: the savings view at desktop 1280x800, full-page — the pair's FIFTH re-run)

The probe series derived from the v86 lineage (vlm-shots-v92.sh +
clone-vlmshots-v92.sh + vlm-compare-v92.mjs + arbit-v92.sh — the sed
derivation with the version + session-name + tmp-dir substitutions
[vlm86→vlm92, refarbit86→refarbit92, clonearbit86→clonearbit92,
v86→v92; the shots' session names refvlm86→refvlm92/
clonevlm86→clonevlm92 riding the vlm86→vlm92 family]; the headers
history-corrected to the FIFTH re-run [v58 → v65 → v74 → v80 → v86 →
v92] + "last re-shot v86" + the oldest-remaining bracket [v86 < v87 <
v88 < v89 < v90 < v91] + the queue agreement ordinal NINTH → FIFTEENTH
+ the suggesting plan v85 → v91; the functional bodies verified
version-bump-only by the normalize-back diff — only the intentional
history-correction comment lines differ; the residual "86"/"80" tokens
all legitimate history references [the v74/v80 census axes, the v80
titleRow geometry, the v86 pin candidate]; login on the first attempt
both sides; the parked pointer at (5,5); read-only on the reference —
the v46 rule holds).

**The verdict DIFFERENT, every flag DOM-arbitrated to a documented
class — the SAME flag-set classes as the v86 re-run itself:**

1. **"Card Grid & Footer Alignment"** — the clone's 2-card grid + the
   footer split into two groups (left/right) vs the reference's single
   card footer grouped left: the seed-count class (the reference's
   1-item savings seed vs the clone's 2-item dev seed) + the **v58
   DATA-CONDITIONAL footer class** (the reference's own savings item
   carries NO paymentMethod so its footer renders ONE child — the date
   alone — while the clone's carry paymentMethods, the same two-child
   structure the reference's own income card renders; the v57
   conditional-footer contract).
2. **"Card Internal Spacing"** — the derived consequence of the footer
   layout difference (the same v58 class).
3. **The header stats / card counts / contents / badges** — the
   seed-data classes (the amounts, the badge sets, the subtexts, the
   dates — the reference's need/monthly/active vs the clone's
   savings/monthly/Recurring/active).
4. **The avatar "U" vs "D"** — the user-identity class.

No FAB flag this cycle (the reference's platform iframe chrome outside
the queryable DOM — the v85/v91-documented class, absent from this
verdict's flag set).

The both-sides census (arbit-v92.sh — **executed in the TWO-HALF
CONTROLLED FORM** [ref-arbit-v92.sh + clone-arbit-v92.sh, the census JS
byte-identical across the halves — the lines-1-153 identity verified by
the md5 line-block diff] after the combined script's clone half
aborted in the sandbox's chromium resource exhaustion — the
v89/v91-documented symptom class; the v91 lesson applied: the two-half
form is the recovery) — **REPRODUCES the v86 census values EXACTLY —
zero drift since v86 on every axis:**

- **The HEADER BYTE-IDENTICAL** (the h1 20px/700/rgb(26,58,46)).
- **The GRID + CARD chrome BYTE-IDENTICAL** (grid w 960 / gap 16px /
  the 3-col ~309px template; card w 309 / pad 20px / radius 12px /
  border 1px solid rgb(229,231,227) / bg rgb(255,255,255)); the
  childCount (1 vs 2) the seed-count class; the card h (ref 200 vs
  clone 230) the v70b-decomposed class (the Recurring superset badge's
  wrap h 52 [22+8+22] → +30px, and the 1-row grid STRETCHES the shorter
  sibling).
- **The TITLE ROW BYTE-IDENTICAL** (flex/center/8px/h 24 + the dot
  8×8/9999px in the savings blue rgb(59,126,161) + the h4
  16px/600/lh 24px/rgb(26,58,46)).
- **The AMOUNT leaf BYTE-IDENTICAL** (fs 24px / fw 700 / lh 32px / the
  savings blue rgb(59,126,161)).
- **The FOOTER + BADGE chrome BYTE-IDENTICAL** (the footer
  flex/space-between/12px/rgb(107,114,128)/h 16 with the icon children
  flex/gap 4px/12×12/rgb(107,114,128); the badgeRow flex/wrap/8px
  gap/mb 12px; every badge radius 6px/pad 2px 10px/fs 12px/fw 600/h
  22); the footer childCount (1 vs 2) the v58 DATA-CONDITIONAL class;
  the badgeRow h (22 vs 52) + the classification texts the v57
  wrap/VALUE classes.
- The docSW 1280 guard on both sides.

**NO NEW CLONE GAP — the v92 iteration is PIN-ONLY.**

### F4 [PIN] — the savings filter-interior + search-icon census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 295)

The never-pinned axes (the existing pins cover around them — the v38 S2
pin holds the savings filter card's CHROME {bg/radius/border/pad} + the
search's {447×36} GEOMETRY + the comboboxes' {216×36} + the placeholder
+ the aria-label superset, at the default viewport; the v91 pin holds
the interactive INTERIORS at 1280 on the INCOME and EXPENSES variants
only — {the search's typography + every trigger's resting chrome + the
chevrons}; the v65 F3 pin the page-header row at 1280 on /savings; the
v45/v57/v74/v79/v80/v85/v86 pins the card/titleRow/amount/footer/badge/
subtitle families; **the SAVINGS variant's interactive interiors are
never pinned at ANY viewport, and the SEARCH ICON's computed chrome
{w/h/color/position/left} is never pinned at ANY viewport on ANY view**
— the glyph-parity spec holds the icon's PATH data only, the
class-string test the w-5 SUBSTRING only):

- **The SEARCH input's full census at 1280 on /savings** (the v91
  family's third variant): {tag "INPUT", type "text", w 447, h 36, fs
  "14px", fw "400", lh "20px", color "rgb(10, 10, 10)", placeholder
  "Search savings items...", pad "4px 12px 4px 40px", radius "6px"};
- **The SEARCH ICON's computed chrome at 1280** (the filter card's last
  never-pinned element — the magnifier svg in the search's relative
  wrapper): {tag "svg", w 20, h 20, color "rgb(107, 114, 128)",
  position "absolute", left "12px"};
- **Every combobox TRIGGERS' RESTING chrome at 1280** (both triggers on
  the savings view): {tag "BUTTON", w 216, h 36, pad "8px 12px",
  justify "space-between", align "center", bg "rgba(0, 0, 0, 0)",
  radius "6px", borderW "1px", borderC "rgb(229, 229, 229)", fs "14px",
  fw "400", color "rgb(10, 10, 10)", chev {w 16, h 16, color
  "rgb(10, 10, 10)"}} + the trigger texts ("All Categories" / "All
  Frequencies");
- **The FILTER CARD's own chrome re-affirm** {w 960, h 86, pad "24px",
  radius "16px", bg "rgb(255, 255, 255)", borderC "rgb(229, 231, 227)"}
  (the v38 S2 contract at the pin's own viewport);
- The docSW 1280 guard.

Every pinned axis is STATIC chrome (the filter card's default resting
state — the placeholder and trigger texts are view-constants, no data
conditionals); the pin rides the plain authenticated /savings view at
1280×800 on the e2e seed (read-only — no fixture writes), in
tests/e2e/items.spec.ts (the v38/v57/v64/v70/v85/v86/v91 pins' own
file), reusing the census's own finder verbatim (the wide input > 100 →
the closest div.rounded-2xl → the search wrapper's first svg + the
inner grid → the [role=combobox] children + the svg inside each).

**The pin's own axes first measured byte-identical on both sides by the
supplemental census** (savings-filter-arbit-v92.sh +
savings-filter-clone-v92.sh — the v87/v88/v89/v90/v91 one-shot
precedent, BUILT TWO-HALF from the start after the cycle's first
exhaustion; the census JS verified byte-identical across the halves by
the md5 line-block diff): on BOTH sides' /savings at 1280×800, the
search reads {INPUT/text/447×36/14px/400/20px/rgb(10,10,10)/"Search
savings items..."/"4px 12px 4px 40px"/6px}, the search icon reads
{svg/20×20/rgb(107,114,128)/absolute/12px}, every trigger reads
{BUTTON, 216×36, pad "8px 12px", justify space-between, align center,
bg rgba(0,0,0,0), radius 6px, borderW 1px, borderC rgb(229,229,229), fs
14px, fw 400, color rgb(10,10,10), chev 16×16 rgb(10,10,10)}, and the
filter card reads {960×86/24px/16px/white/rgb(229,231,227)} — ZERO
deltas on any axis (the docSW 1280 both sides).

**The pin-sanity mutation (the executed form — the viewport-scoped
responsive-variant dodge, the v80/v86/v87/v88/v89/v90/v91 pattern,
scoped AT-lg this cycle because the pin runs at 1280)**: the search
icon's `h-5 w-5` → `h-5 w-5 lg:h-6` (items-view.tsx:181, applied by
LINE NUMBER — the SearchIcon's own className, the one instance shared
by all three items views) — flips EXACTLY the pin's searchIcon.h axis
at the pin's OWN viewport ("20" → "24" at ≥1024px, where the pin runs
at 1280) and nothing else: the `lg:` variant is INERT below 1024px
(every mobile/tablet pin green by construction); the icon is
ABSOLUTELY POSITIONED (out of flow — the wrapper's box, the input's
447×36 geometry, the grid columns, and the docSW all unchanged); the
icon's w/color/position/left axes green (only the height class flips);
**no spec asserts any search icon's computed w/h at ANY viewport** —
the coverage-map grep run across ALL specs: the icon-size assertions
found are on OTHER elements (the dashboard quick-action icons
{w 20/color accent}, the stat-tile icons, the item-details
classification icon {iconW 20}, the networth nav/medallion icons
{16×16/32}, the calculator row icons, the dialog tile icons, the
mobile burger's class-substring); the search icon's ONLY assertions
elsewhere are the class-SUBSTRING test (`iconCls` contains "w-5" —
green under the added lg:h-6, the w-5 substring intact) and the
glyph-parity PATH-data pins (green under a size flip) — **cascade-free
BY CONSTRUCTION** (the expected failure diff reads as the icon's h
axis alone; the w/color/position/left axes, the search's typography,
the trigger family, the filter card, and the docSW guard all green),
then restored (the standalone REBUILD as a SEPARATE command — the FULL
`npm run build`, never a bare `next build`; `git diff src/` = 0 lines;
the post-restore full run green).

**The disproven-in-advance candidates (documented without execution —
the design-probe analysis)**: (1) the search's fw mutation (the v91
form, pl-10 → pl-10 lg:font-medium) — REFUTED this cycle: the Input
instance is shared by ALL THREE views, so the flip cascades to the v91
pin's search.fw axis on /income and /expenses (TWO pins red — the
cascade the v92 pin must avoid); (2) the search's fs mutation
(text-sm → text-base) — the shared-Input cascade + the v86
ratio-line-height trap (fs 14→16 scales lh 20→24, a two-axis failure);
(3) the trigger's pad mutation — the SelectTrigger is the SHARED shadcn
component (every dialog select flips — the v89 shared-component-cascade
lesson); (4) the chevron's size — the lucide ChevronDown inside the
shared SelectTrigger (the same cascade); (5) the icon's color mutation
— the color rides the view's inline `style={{ color: rgb.gray }}`
token (every items view's icon flips, but the color axis is shared
with... no other spec — viable but REJECTED: the h axis is the cleaner
single-axis flip, the color token is the app's global gray family);
(6) the icon's position/left axes — geometry-coupled (a position flip
moves the icon box, a two-axis failure diff); (7) the docSW axis — a
page-level shared surface, never a mutation target. The `lg:h-6` dodge
is the ONLY single-axis, geometry-inert, coverage-verified flip on the
pin's own surface.

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → `npm run build` → **295 e2e** in chunks
(+1) → 35 smoke; the 16 standing screenshots regenerated + byte-
compared (the same-DB discipline; the seedcheck under
`env -u DATABASE_URL`). EXPECTED: the seed planted and the shots taken
on the same calendar day reproduce the committed set byte-for-byte
(the v82/v88/v90/v91 same-day-seed byte-identity law); any DATE-class
diff pixel-arbitrated per the v66/v75/v80/v86 discipline, never a
full-page VLM verdict; any rasterization-noise class re-classified per
pixel if it recurs.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the savings filter-interior + search-icon census at 1280 (the search's full census {tag/type/w/h/fs/fw/lh/color/placeholder/pad/radius} + the search icon's computed chrome {tag/w/h/color/position/left} + every trigger's resting chrome {tag/w/h/pad/justify/align/bg/radius/borderW/borderC/fs/fw/color/chev w/h/color + the texts} + the filter card's chrome re-affirm + the docSW guard), riding the plain authenticated /savings view | tests/e2e/items.spec.ts |
| 2 | sanity | the pin-sanity mutation (the EXECUTED form): the search icon's `h-5 w-5` → `h-5 w-5 lg:h-6` (items-view.tsx:181, by LINE NUMBER) → the pin FAILS at exactly the searchIcon.h axis ("20" → "24" at ≥1024px; the w/color/position/left axes, the search's typography, the trigger family, the filter card, and the docSW guard stay green; every below-1024 pin green — the lg variant inert there); the full items.spec.ts under the mutation: only the v92 pin red; restored → the standalone REBUILD → the post-restore full run green | src/components/budget/items-view.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 295 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v92 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (294→295 + the v92 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v92 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 127 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.49 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v92 section (the new probes + the two-half-from-the-start lesson + the v93 queue) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_222.md + the repo worklog Session 127 entry | docs/session_222.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the savings-filter census's own
  measured values, byte-identical on both sides' /savings at 1280×800
  (the supplemental census ran BEFORE this plan's execution — the
  values above are its verbatim output; the census JS verified
  byte-identical across the two halves by the md5 line-block diff).
- The mutation target line verified by reading the source:
  items-view.tsx:181 is the SearchIcon's own className
  (`className="absolute top-1/2 left-3 h-5 w-5 -translate-y-1/2"`) —
  the one instance rendered for all three items views; the login
  page's icons (login-card.tsx) and the dialogs' icons carry their own
  classNames in their own files, untouched by the line-number-scoped
  mutation.
- The grep verification (run across ALL specs, BOTH the computed-style
  assertions AND the class-string/glyph families): NO spec asserts any
  search icon's computed w/h at any viewport; the only search-icon
  assertions elsewhere are the class-substring (`toContain("w-5")` —
  green under the added lg:h-6) and the glyph-parity PATH-data pins
  (green under a size flip); the v91 pin holds NO icon axes (its
  census measured the search typography + the triggers + the chevrons
  only).
- The rotation ledger verified: the savings pair last re-shot v86 = the
  oldest remaining [v86 < v87 < v88 < v89 < v90 < v91] — the v91-era
  docs' v92 suggestion agreeing with the ledger (the FIFTEENTH
  consecutive agreement), the surface names verified against
  vlm-shots-v86.sh's own surface list before the derivation.
- The pin's finder: the census's own finder verbatim (the wide input
  > 100 → the closest div.rounded-2xl → the search wrapper's first svg
  + the inner grid → the [role=combobox] children) — proven stable
  across the v38/v64/v70/v91 censuses.

## Operational lessons this cycle (the probe README's D6 section)

- THE TWO-HALF CENSUS, FROM THE START, AGAIN: the combined
  arbit-v92.sh's clone half aborted in the chromium resource exhaustion
  (the v89/v91-documented symptom class) — the two-half form (the
  census JS byte-identity as the contract, verified by the md5
  line-block diff) is the recovery, and the SUPPLEMENTAL one-shot
  censuses are again BUILT two-half from the start after the cycle's
  first exhaustion (the v91 lesson holding).
- THE MUTATION-FAMILY ROTATION: the v91 mutation form (the search's
  fw axis via the view-local className) is NOT reusable on the same
  component once its axes are pinned on the sibling views — the
  Input instance is shared by all three items views, so an fw flip at
  ≥1024px cascades to the v91 pin (TWO pins red). The v92 mutation
  rotates to a DIFFERENT element on the same surface — the search
  ICON's height — whose computed chrome is asserted by NO other spec
  at any viewport. The lesson: when the pin family extends across the
  sibling variants of a shared component, the mutation axis must move
  to an element whose axes the earlier variants' pins do not hold.
