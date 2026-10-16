# Remediation Plan v67 — the v60-era pair's fresh standing sweep (the
# networth + drill-down re-run at 1280) + the axe-core wrapper watch (the
# upgrade DECISION: v68 = the dedicated upgrade iteration) + the networth
# summary card's HEIGHT-family computed census pin

Date: 2026-10-16 · Scope: the session-161/162 v67 queue — "the re-run
cadence rotates to the v60-era pair (the networth-view desktop 1280
standing pair — the oldest remaining after v64/v65/v66 covered the
v57/v58/v59 pairs)" and "the axe-core wrapper upgrade decision (the
upstream 4.14.0 — a dedicated upgrade iteration, never a drift)" — plus
the 61st standing checks. The v60-era pair re-run covers BOTH of that
era's pairs (the v66 precedent: the v59-era re-run covered the
calculator + login set): (1) the NETWORTH view's FULL-PAGE 1280×800
pair and (2) the DASHBOARD's drill-down EXPANDED 1280×800 pair. All
READ-ONLY on the reference (the v46 rule — the drill-down expansion
clicks are VIEW-STATE toggles that mutate no data). Measured live on
BOTH sites via the v67 family: `vlm-shots-v67.sh` +
`clone-vlmshots-v67.sh` + `vlm-compare-v67.mjs` (the pair),
`arbit-v67.sh` + `arbit-v67b.sh` (the two-part DOM arbitration census —
the five PAIR 2 flags + the networth summary-card HEIGHT family),
`ref-standing-v61.sh` + `standing-checks-v61.sh` (the 61st round,
version-bumped from v60), and the npm/lockfile version audit (F1).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · 268 e2e ✓ (the --list count —
267 chromium + 1 setup; the chunk runs 97 + 96 + 77 = 267 chromium + 3
setups, zero failures — the `:3100`/`:3200` orphan checks clean before
the runs) · 35/35 smoke ✓ — the codebase matches the documented v66
state exactly (the v66 pin verified present at calculator.spec.ts "the
calculator dialog's HEIGHT-family computed census at 1280"). The dev DB
at the exact seed state (7 budget items / 3 assets / 2 liabilities).

## The v67 sweep — what the measurement found

### The 61st standing checks — ALL GREEN

- **Reference side**: the four bugs ALL still live — the toast-blocker
  (`hitIsBurgerChild:false`, the burger's center hit intercepted by
  `DIV.fixed top-0 z-[100]`), the sheet-trap (the overlay remains after
  the nav click, `overlayCount:1`), the no-landmark
  (`navLandmark:false`), the 464px `/networth` overflow at 390. The
  data census UNCHANGED (the 61st consecutive clean drift check: "1
  items · $25,000" networth / "1 items · $5000.00" income / "4 items ·
  $525.00" expenses). The SEO pair live.
- **Clone side**: R1 the burger hit-test TRUE + the sheet opens · R2 the
  sheet CLOSES + navigates (`sheetGone:true, overlayGone:true` on
  /income) · R3 the nav landmark present · R4 ZERO overflow at 390 on
  all five views (docSW 390 each) · the SEO pair live. **The mobile
  navigation menu VERIFIED WORKING — the 61st consecutive time.**

### F1 [AUDIT] — the axe-core 5.x wrapper watch: local NO DRIFT + the upgrade DECISION

The registry state is UNCHANGED from the v66 watch: npm-latest
`@axe-core/playwright` = **4.14.0** (dist-tags: latest 4.14.0 +
4.14.1-rc/next; its declared nested engine `axe-core ~4.14.0` —
verified by packing the tarball). **The local tree has NO DRIFT**: the
lockfile resolves `@axe-core/playwright` to 4.13.0, and the engine that
actually executes the AxeBuilder scans — the wrapper's NESTED
`axe-core@4.13.0` (`node_modules/@axe-core/playwright/
node_modules/axe-core`) — is byte-identical to the v38–v66 audits. The
top-level `axe-core@4.14.0` in the tree still belongs to
`eslint-plugin-jsx-a11y@6.10.2` (via eslint-config-next) — a LINT-TIME
static-analysis consumer that never scans pages. The a11y.spec.ts
contract remains valid as pinned; no re-scan required.

**The upgrade DECISION (the queue's item #2): the 4.14.0 upgrade is
DEFERRED TO A DEDICATED v68 ITERATION — never a drift, never a rider.**
Rationale: (1) the v66 plan's own constraint — "a future DEDICATED
upgrade iteration (bump the pin deliberately + re-run the full a11y
gate + re-audit the rule coverage — never a side-effect lockfile
drift)" — the upgrade changes the toolchain the a11y.spec.ts contract
executes under, and that deserves an iteration whose center of gravity
is the toolchain change with its full re-verification chain, not a
rider on a pair-re-run iteration; (2) v67's cadence item (the
v60-era pair — the oldest remaining standing pair) continues the
unbroken four-iteration rotation (v64 items → v65 savings → v66
calculator/login → v67 networth+drill-down) and slipping it would
disorder the cadence; (3) there is no urgency — the lockfile holds the
tree, no 5.x wrapper exists, and the watch's re-check point is
unchanged (a 5.x wrapper release or an engine bump inside the
wrapper's nested dep in the local tree). The v68 queue carries the
complete upgrade specification (below) so v68 executes it mechanically.

### F2 [PAIR] — the v60-era pair's fresh sweep: the networth view + the drill-down at 1280

The session-161/162 v67 queue's first item — a fresh VLM standing
sweep of the two surfaces the v60 pair first shot (the v60-era shots
predate the v61 dashboard fix, the v62/v63 mobile twins, and the v66
height-family pin; the v64/v65/v66 passes covered the v57/v58/v59-era
pairs). Shot both sides (`vlm-shots-v67.sh` + `clone-vlmshots-v67.sh` —
login on the first attempt both sides, the drill-down expansion clicks
"section clicked" + "category clicked" both sides), compared via
`vlm-compare-v67.mjs`, every flag DOM-arbitrated via `arbit-v67.sh` +
`arbit-v67b.sh` (the two-part computed census on both sides at
1280×800) per the v43 rule.

**PAIR 1 (networth) VERDICT IDENTICAL** — the VLM found ZERO
layout/style differences ("pixel-perfect matches" on the nav rail, the
page header, the summary card geometry/gradient, the tab bar, the
section headers, the Add Asset button, the card layouts, the
typography, the spacing); every difference it listed was the expected
DATA class (the figures, the counts, the group headers, the ratio
"∞:1" vs "0.21:1", the avatar letter) + the "Edit with Base44" FAB
(platform chrome, excluded from comparisons by rule). The pair CLEAN
with zero flags to arbitrate.

**PAIR 2 (drill-down) VERDICT DIFFERENT with 5 style flags, every one
DOM-arbitrated to a documented class (the v60 re-run re-proving its own
arbitration classes live):**

1. "The Dashboard nav item is highlighted in the clone but not the
   reference" — DOM-arbitrated to the documented **root-URL active-nav
   gap**: the reference shows none at `/` (measured bg transparent /
   color rgb(63,63,70) / fw 400) while the clone highlights (bg
   transparent / color rgb(255,255,255) / fw 500) — the superset
   contrast #3, documented since v56, re-confirmed live both sides.
2. "The avatar shows U vs D" — the **user-identity class** (each
   site's own logged-in user).
3. "The progress bar fill length differs (30.5% vs 62.8%)" —
   DOM-arbitrated to the **pct × 568 data class** (the v56
   arbitration, re-measured live): the track is byte-identical on both
   sides (568×12, bg rgba(255,255,255,0.1), radius 9999px, the fill
   gradient linear-gradient(90deg, rgb(224,122,59) 0%…)); the fill's
   width is each site's own allocation pct — the reference 173, the
   clone 357.
4. "Percentage labels are visible on the chart in the clone but absent
   in the reference" — DOM-arbitrated to a **PERCEPTION ARTIFACT** (the
   v60 precedent, re-confirmed live): the reference DOES render its
   donut labels (count 4 = 1 group wrapper + 3 individual texts
   "92.3%"/"4.6%"/"3.1%", labelLineCount 0, 16px, fill rgb(0,0,0), 3
   sectors) and the clone renders the same chrome (count 4, "81.6%"/
   "13.8%"/"4.6%", labelLineCount 0, 16px, black, 3 sectors) — the
   values each site's own data (the v9 G1b contract holds on both
   sides).
5. "The trend line icons at the bottom-right of the stat cards show
   different paths/angles" — **a NEW flag variant (not in the v60
   run)**, DOM-arbitrated to a **PERCEPTION ARTIFACT** via a GLYPH
   census: the stat cards' footer trend icons are BYTE-IDENTICAL on
   both sides — 16×16, color rgb(143,188,63) (the lime income type
   color), viewBox "0 0 24 24", and the same two-polyline glyph
   `<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"></polyline>
   <polyline points="16 7 22 7 22 13"></polyline>` (the Heroicons v1
   outline trending-up — POLYLINE-based, carrying no `<path>` element,
   which is why the census needs the innerHTML glyph signature, not a
   path `d` signature). Plus the hero-glyph census: the same 7 svgs in
   the same order on both sides (the sign-conditional TrendingUp at
   orangeLight, 3 chevron-rights at gray, the piggy at lime + blue,
   the receipt at orangeDark — every path signature byte-identical).
   No glyph difference exists; the VLM read the same shapes at
   different raster positions as "different paths".

**The pair is CLEAN: every flag arbitrates to a documented class or a
measured perception artifact. No production-code parity gap** (`git
diff src/` empty at ship — the pin-only line continues).

**The arbitration's own discovery — the never-pinned HEIGHT family.**
The v67 census added the summary card's computed HEIGHT axes to the
arbitration (never measured before v67 at this viewport): the v60 F1
pin covers the summary card's width/pad/radius/gradient/shadow + the
figure/label/medallion/stat-tile FONTS + the stat grid template/gap +
the ratio value's text axes, and the v63 F3 pin the stat-tile family's
heights at 390 — but NEVER the 1280 heights. The v67 census measured
the family BYTE-IDENTICAL on both sides (the reference's values, the
clone's identical):

- **The summary card**: 960×**333** (pad 32px, radius 16px, the 135deg
  forest→lime gradient, the 26-58-46 shadow) — the deterministic
  arithmetic 32 (pad-top) + 76 (head row) + 32 (the head row's mb-8) +
  84 (the stat grid) + 24 (the footer's mt-6) + 24 (the footer's pt-6)
  + 1 (the border-top) + 28 (the ratio row — text-lg's 28px
  line-height) + 32 (pad-bottom) = 333.
- **The head row**: h **76** (flex items-center, mb 32px) — governed by
  the label block (the label h 20 + mb 8 + the figure h 48 = 76), the
  64×64 medallion along for the ride.
- **The figure**: fs 48px / fw 700 / white, lineHeight 48px, h **48**.
- **The stat grid**: template "440px 440px", rows **"84px"**, gap 16px,
  h **84** (one row at 1280 — the 390 twin's two-row 184 is the v63
  class).
- **The stat tile**: 440×**84** (pad 16px, radius 12px, bg
  rgba(255,255,255,0.1), blur(10px)) — the label h 16 + mb 4 + the
  amount h 32 + the 32px padding; the label 12px, the amount 24px/700.
- **The ratio footer**: mt **24px** / pt **24px** / borderTop 1px
  rgba(255,255,255,0.2), h **53** (the pt 24 + the border 1 + the ratio
  row 28); the label 14px, the value 18px/700.

### F3 [PIN] — the networth summary card's HEIGHT-family computed census at 1280

The F2 arbitration census measured a never-pinned family: the computed
HEIGHTS of the networth view's summary card at the 1280 pair viewport —
the v60 F1 pin covers the card's width/pad/radius/gradient/shadow class
strings + the fonts, the v63 F3 pin the stat-tile heights at 390, but
NEVER the 1280 heights (the card h 333, the head row h 76, the figure
h 48, the stat grid rows, the tile h 84, the ratio footer's mt/pt/
border/h). The census, measured BYTE-IDENTICAL on both sides:

- **The card**: 960×333 (the w/pad/radius/bg/shadow re-asserted as
  controls — the v60 F1 axes).
- **The head row**: h 76, mb 32px (flex items-center).
- **The label**: fs 14px, mb 8px, h 20 (the color pinned by v60 F1).
- **The figure**: lh 48px, h 48 (the fs/fw/color pinned by v60 F1).
- **The medallion**: iconH 32 (the 64×64 + iconW 32 pinned by v60 F1).
- **The stat grid**: gridTemplateRows "84px", h 84 (the template/gap
  pinned by v60 F1).
- **The stat tile**: h 84, the label h 16 + mb 4px, the amount h 32
  (the pad/radius/bg/blur/amtFs/amtFw pinned by v60 F1).
- **The ratio footer**: mt 24px, pt 24px, borderTopWidth 1px, h 53
  (the label/value font axes pinned by v60 F1).

The F3 pin adds the census to `tests/e2e/networth.spec.ts` (PIN-ONLY —
the surface is already correct; GREEN first run expected), a new
describe after the v60 F1 block, at the pair viewport (1280×800), in
the read-only logged-in state (the v60-F1 pattern — no fixture flow
needed; the summary card renders from the e2e seed's own 3-asset /
2-liability data on every run).

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F3 pin: the networth summary card's height-family computed census at 1280 (GREEN first) | tests/e2e/networth.spec.ts |
| 2 | sanity | S1 mutation A: the head row's `mb-8`→`mb-4` must FAIL the pin (mb 32→16 + card h 333→317); standalone rebuild; restore | src/components/budget/net-worth-view.tsx:340 |
| 3 | sanity | S2 mutation B: BOTH stat tiles' `p-4`→`p-2` must FAIL the pin (pad 16→8 + tile h 84→68 + grid rows "84px"→"68px" + card h 333→317 — the shared-class regression; a FIRST-tile-only mutation does NOT move the axis: the tile height is STRETCH-GOVERNED — the grid row follows the taller p-4 sibling and stretches the p-2 tile back to 84, measured live); standalone rebuild; restore | src/components/budget/net-worth-view.tsx:367+374 |
| 4 | sanity | S3 mutation C: the ratio footer's `mt-6 pt-6`→`mt-3 pt-3` must FAIL the pin (mt/pt 24→12 + footer h 53→29 + card h 333→309); standalone rebuild; restore | src/components/budget/net-worth-view.tsx:385 |
| 5 | verify | the 16 screenshots regenerated + byte-compared (expect NO change — no production-code change) | docs/screenshots/ |
| 6 | docs | D1: AGENTS.md v67 paragraph | AGENTS.md |
| 7 | docs | D2: CLAUDE.md count/state bump | CLAUDE.md |
| 8 | docs | D3: README state + the v67 row | README.md |
| 9 | docs | D4: SKILL doc Session 102 row + the state line | zero-balance_SKILL.md |
| 10 | docs | D5: PAD revision block v1.1.24 | Project_Architecture_Document.md |
| 11 | docs | D6: the probe README's v67 section | scripts/parity-probes/README.md |
| 12 | docs | D7: session_163.md + the repo worklog Session 101 entry | docs/session_163.md + worklog.md |
| 13 | ship | the full chain re-run (lint → typecheck → 108 unit → build → 269 e2e → 35 smoke) + commit + SSH-wrapper push | — |

## Pre-execution validation (done before the plan's execution)

- The F3 pin's finders: modeled on the v60 F1 pin's own census (proven
  live in the v67 arbitration on BOTH sites) — the label by its exact
  "Total Net Worth" leaf text, the card by the walk-up to the
  div.rounded-2xl, the head row as the label block's parent (the flex
  justify-between), the figure by the `$`-prefixed amount inside the
  card, the medallion by its 9999px radius + svg, the stat grid by the
  "Total Assets" label's [class*=grid] walk-up, the tile by the
  label's [class*=rounded] walk-up, the ratio footer by the walk-UP
  from the "Asset to Liability Ratio" leaf to the border-t element.
  All axes scroll-independent (the card sits at the top of /networth
  at 1280×800).
- The mutation targets: the head row's `mb-8` at
  net-worth-view.tsx:340 (the headRow mb + card h axes), the first
  tile's `p-4` at :367 (the tile h + grid rows + card h axes), the
  ratio footer's `mt-6 pt-6` at :385 (the footer mt/pt/h + card h
  axes). Each mutation needs the STANDALONE REBUILD as a SEPARATE
  command (the v53 lesson) before the pin run can bite.
- The e2e contract: the pin runs AUTHENTICATED via the setup project's
  storageState; the deterministic e2e seed (prisma/seed.ts, re-seeded
  into db/e2e.db every run by global-setup) puts the same networth
  data (3 assets / 2 liabilities → the "0.21:1" ratio, the figure
  "-$245,950.00") on every run — the pin's expected values are the
  live-measured clone census values (db/custom.db carries the same
  seed). The figure's DIGIT COUNT is data-conditional (the labelBlock
  width is NOT pinned — only the heights, which are figure-FONT
  driven, not digit driven: lh 48 × one line = h 48 whatever the
  digits).
- The existing pins are SAFE: the v60 F1 pin (1280), the v41 F2/F3
  pins (640/390), the v50 F2 (640) + v53 F1 (390) tablist pins, and
  the v46 F2 grid/card pin (1280) are all re-asserted as controls or
  untouched — the v67 pin asserts the HEIGHT family they never
  covered, at the same viewport, on the same finders. The networth
  add/delete round-trips and networth-error.spec.ts untouched (the
  v67 pin is read-only).
- The chain gate: lint → typecheck → 108 unit → build → 268 e2e
  (**269** after: +1 — the F3 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every
  agent-browser run; the with-server boots fresh per command; the
  reference session EXPIRES between long eval gaps — re-login; the
  fresh-login first fetch can exceed the wait window — retry the
  finder on a warm session (the v66 lesson); the e2e chunks pass FULL
  file paths; `ss -tlnp | grep :3100` + kill before every full-chain
  run (the v53 orphaned-webServer lesson); the census JS inside the
  heredoc avoids every dollar sequence (String.fromCharCode(36)) and
  every single quote — BOTH the unquoted-wrapped ARBIT string AND the
  single-quoted eval argument inside a quoted heredoc terminate on
  single quotes (the v60 lesson #1, re-learned on the clone side this
  iteration); a `const` census variable assigned in a walk-up loop
  throws "Assignment to constant variable" — with stderr discarded the
  only signature is the EMPTY eval line between the === markers
  (debug with stderr visible); a childless-div finder pattern FAILS on
  container tracks (the hero progress TRACK carries the fill as a
  child — drop the !children.length requirement); the reference's
  Heroicons-v1 trend glyph is POLYLINE-based (no `<path>` element) — a
  glyph census needs the innerHTML signature, a path `d` signature
  returns null; **the stat tile's height at 1280 is STRETCH-GOVERNED**
  — the grid row follows the TALLER sibling and stretch-fills both
  tiles to it (align-items: stretch, the default), so a FIRST-tile-only
  pad mutation leaves the pinned h axis untouched (measured live: pad
  8px + h 84 on the mutated tile beside its p-4 sibling — the S2
  non-bite, root-caused) — the pin-sanity mutation must be the
  SHARED-class regression (both tiles), which the corrected S2
  verified; the stretch also EXPLAINS the arithmetic's stability: both
  tiles share the content structure, so the row = either tile's
  natural height.
- The deferred queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side verify-email
  panel census, the forgot-confirm state census, the calculator
  EMPTY-state reference census, the line-items dialog glyphs.
- The v68 queue (suggestions): (1) **the DEDICATED axe-core wrapper
  upgrade iteration** — bump the devDependency pin
  `@axe-core/playwright` `^4.13.0`→`^4.14.0` deliberately, `npm
  install` to regenerate the lockfile entry, verify the nested engine
  resolves `axe-core@4.14.x`, re-run the full a11y gate
  (a11y.spec.ts) + the full e2e chain + smoke, and RE-AUDIT the rule
  coverage (diff the activated rule sets axe-core 4.13.0 vs 4.14.0 —
  arbitrate any new violations: a real markup issue → fix + pin; a
  rule-behavior change → pin accordingly; the upgrade is NEVER a
  side-effect lockfile drift), (2) the re-run cadence rotates to the
  v61-era pair (the dashboard full-page 1280 standing pair — the
  quick-action row + the Budget Guidelines card, the oldest remaining
  after v64/v65/v66/v67 covered the v57/v58/v59/v60 pairs), (3) the
  deferred reference-write censuses (unchanged).
