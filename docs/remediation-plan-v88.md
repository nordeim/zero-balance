# Remediation Plan v88 — the re-run cycle's next-oldest candidate (the v82-era networth + drill-down pair's fourth re-run) + the axe watch + the stat-card count-row divider census pin (PIN-ONLY)

The formal narrative: `docs/session_211.md`. The queue: the v87 plan's v88
suggestion — **the ledger-verified target** (the v87 plan's suggestion
AGREEING with the rotation ledger: the v82-era NETWORTH + DRILL-DOWN pair
[the networth view + the dashboard drill-down EXPANDED at desktop
1280x800], last re-shot v82, is the oldest remaining candidate [v82 < v83
< v84 < v85 < v86 < v87]; the pair's FOURTH re-run [v60 → v67 → v76 →
v82 → v88] — the ELEVENTH consecutive queue/ledger agreement), plus the
axe-core watch at its re-check point and the 82nd standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 291.**

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered) · **292 e2e chunk executions ✓** (103 + 129 + 60
across three chunk splits of the 23 files = 290 unique tests — the same
unique count as the documented v87 state's 292 = 290) · 35/35 smoke ✓.
The workspace REBUILT (the fresh-clone path, the v86 precedent): `git
clone` at main @ 154ac6a, the tree clean; the environment re-provisioned
(npm ci 354 packages with the four approved install scripts [the
allowScripts block recorded in package.json by npm itself]; `.env`
written [DATABASE_URL="file:../db/custom.db"], `db/` at the repo root,
db:generate + db:push + db:seed; chromium-1243 installed; the paramiko
ssh shim deployed outside the repo at /home/z/my-project/bin/ssh); the
seedcheck exact (7 items / rent 1850 / expenses 2235 / 0 line items / 3
assets / 2 liabilities) before any flow ran, no orphaned servers.

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next
prereleases beyond — no stable 4.14.1, no 5.x exists), npm-latest
`axe-core` 4.14.0; the lockfile holding the v68 dedupe state (the
wrapper 4.14.0 + ONE hoisted axe-core 4.14.0 — no nested engine dir
under `node_modules/@axe-core/playwright/`); the engine-contract pin
GREEN standalone (2 passed).

### F2 — the 82nd standing checks: ALL GREEN (version-bumped from v81 — version-bump-only diffs verified)

ref-standing-v82.sh + standing-checks-v82.sh (version-bumped from v81
— after normalizing the THREE token families [v81→v82, 81st→82nd, AND
the bare-number session names ref81→ref82 / clone81→clone82] the files
are version-bump-only: verified by normalizing back and diffing clean).
Reference side: the four bugs ALL live [toast-blocker
`hitIsBurgerChild:false`; sheet-trap `overlayCount:1`; no-landmark
`navLandmark:false`; the 464px /networth overflow at 390]; the data
census UNCHANGED (the 82nd clean drift check: networth "1 items ·
$25,000" / income "1 items · $5000.00" / expenses "4 items · $525.00");
the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation
menu VERIFIED WORKING (the **82nd consecutive time**:
`hitIsBurgerChild:true`, the sheet opens, closes on nav, the nav
landmark present), zero overflow at 390 on all five views (docSW 390
everywhere), the SEO pair live.

### F3 — the re-run pair (the v82-era networth + drill-down pair: the networth view + the dashboard drill-down EXPANDED at desktop 1280x800)

**The NETWORTH pair: VERDICT IDENTICAL, zero style flags** (matching
the v82 re-run's own IDENTICAL verdict — zero drift on the VLM layer;
the VLM's only note the reference's "Edit with Base44" FAB, the
platform-chrome class; every other delta the seed classes — the
figures, the 1-asset vs 3-asset groups, the ratio). The PART B census
(arbit-v88.sh) **reproducing the v82 census values EXACTLY — zero drift
since v82 on every axis**: the card 960×333/32px pad/16px radius/the
forest-to-lime gradient/the rgba(26,58,46,0.3) 0px 20px 60px shadow;
the headRow h 76/mb 32px/flex/center; the label 14px/
rgba(255,255,255,0.8)/mb 8px/h 20; the figure 48px/700/white/lh 48/h
48; the medallion 64×64/rgba(255,255,255,0.2)/icon 32×32; the statGrid
440px 440px/84px/16px/896; the statTile 440×84/16px/12px/
rgba(255,255,255,0.1)/blur(10px)/label 12px-16-4px/amt 24px-700-32; the
ratioFooter 24px/24px/1px rgba(255,255,255,0.2)/h 53/label 14px/val
18px-700 — the labelBlock's WIDTH the ONE delta (ref 304 vs clone 357 —
the v82 DATA-CONDITIONAL width class: the 48px figure's text length
"$25,000.00" vs "-$245,950.00"; the heights byte-identical).

**The DRILL-DOWN pair: VERDICT DIFFERENT with SEVEN flags, every one
DOM-arbitrated to a documented class — the same mechanism classes as
the v82 re-run (the stat-title misread excepted — not re-flagged this
cycle):**

1. the "Dashboard link highlighted in the clone" — the v56 SUPERSET
   class (the reference's link INERT rgb(63,63,70)/400 vs the clone's
   ACTIVE white/500 — the superset behavior);
2. the avatar "U" vs "D" — the user-identity class;
3. the "progress bar significantly longer in the clone" — the pct × 568
   DATA class (fillW ref 173 vs clone 357 on the byte-identical
   568×12 track — **the v60 arbitration's own values REPRODUCED
   EXACTLY, five re-runs later** — the v82 census-arithmetic
   reproduction lesson's standing case);
4. the "donut percentage labels absent in the ref" — the v60 PERCEPTION
   class re-arbitrated live (the reference DOES render its labels: the
   census's count 4 = 1 group + 3 labels, labelLineCount 0, 16px,
   black, 3 sectors — the chrome byte-identical, the texts each site's
   own data [92.3%/4.6%/3.1% vs 81.6%/13.8%/4.6%]);
5. the "stat card footer divider lines present in the clone but missing
   in the ref" — **THE CYCLE'S NEW FLAG — a VLM MISREAD, disproven by
   the dedicated one-shot both-sides census** (stat-divider-arbit-v88.sh,
   the v87 close-arbit precedent): **the divider renders BYTE-IDENTICALLY
   on BOTH sides** — the count row h 20/w 254/flex/gap 8px/center/
   14px/rgb(10,10,10) with the rowChildTags [SPAN, DIV, svg]; the
   divider {DIV, h 1, bg rgb(229,231,227), flexGrow 1} on every card
   (the width 177-vs-170 the flex-1 data-conditional remainder: the
   "1 item" vs "2 items" text width); the trend icons 16×16 with the
   per-type colors (lime/blue/orange — byte-identical). The VLM read
   the faint 1px rgb(229,231,227) line's visibility difference as
   presence/absence — the misread class;
6. the expanded-content + counts + proportions deltas — the seed-data
   classes (the clone's 2 income categories vs the reference's 1, the
   donut proportions, the stat values);
7. the "Edit with Base44" overlay — the platform-chrome class.

**NO NEW CLONE GAP — the v88 iteration is PIN-ONLY.**

### F4 [PIN] — the stat-card count-row + divider census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 291)

The never-pinned axes (the existing pins cover around them: the v51 F2
pin holds the stats row at **390 only** — the grid, the card chrome, the
icon circle, the title, the amount, the countRow's fs/gap/color, the
trend w — and never the divider; the v40 F1 pin holds the 1280 geometry
bands (the 304×210 cards) + the role/tabindex census — never the
count-row or divider chrome; grep-verified: no spec asserts the
stat-card divider's height/background/flexGrow at ANY viewport, and the
trend icon's per-type COLOR is never pinned on the stat cards):

- **The COUNT ROW at 1280** (dashboard-view.tsx:616 — the
  `flex items-center gap-2 text-sm` row): {h 20, display "flex", gap
  "8px", alignItems "center", fs "14px", color "rgb(10, 10, 10)"};
- **The DIVIDER** (dashboard-view.tsx:618 — the `h-px flex-1` line with
  the rgb.border inline background — the ONLY `h-px flex-1` in src,
  grep-verified): {tag DIV, h "1px", bg "rgb(229, 231, 227)", flexGrow
  "1"} — the divider's WIDTH EXCLUDED (the flex-1 data-conditional
  remainder axis — the v82 labelBlock-width convention);
- **The TREND ICON at 1280**: {w 16, h 16} + the per-type COLOR
  trilogy (income rgb(143, 188, 63) lime / savings rgb(59, 126, 161)
  blue / expenses rgb(224, 122, 59) orange — the v80/v85 per-type-dot
  trilogy's stat-card twin);
- the docSW 1280 guard.

Every pinned axis STATIC chrome (the count-row classes and the
divider's height/flex/background are unconditional — no data, no
viewport conditionals; the per-type colors are per-card constants); the
pin rides the plain authenticated dashboard view at 1280 on the e2e
seed (read-only — no fixture writes, no expansion clicks needed), in
tests/e2e/dashboard.spec.ts (the v40/v51/v83 pins' own file).

**The pin's own axes first measured byte-identical on both sides by the
supplemental census** (stat-divider-arbit-v88.sh — the v84/v85/v86/v87
one-shot precedent): the row {h 20/flex/8px/center/14px/
rgb(10,10,10)}, the divider {DIV/1px/rgb(229,231,227)/flexGrow 1}, the
trend {16×16 + the per-type colors} — all byte-identical on both sides'
dashboards at 1280x800.

**The pin-sanity mutation (the executed form — the viewport-scoped
responsive-variant dodge, the v80/v86/v87 pattern)**: the divider's
`h-px` → `h-px lg:h-0.5` (dashboard-view.tsx:618, applied by LINE
NUMBER) — flips EXACTLY the pin's divider.height axis ("1px" → "2px")
and nothing else: the responsive variant is inert below 1024px (the
v51 F2 390 pin untouched — it asserts no divider axis anyway); the row
is `flex items-center` so the 2px divider centers without growing the
row (the row height stays the text's 20px line box — the row.h axis
GREEN under the mutation); the card's height 210 unchanged (the v40 F1
geometry bands green); no other spec asserts the stat-card divider at
any viewport (the login-card OR divider, the dropdown/select separators
— different components, grep-verified) — **cascade-free BY
CONSTRUCTION** (the expected failure diff reads as the divider.height
axis alone), then restored (the standalone REBUILD as a SEPARATE
command; `git diff src/` = 0 lines; the post-restore full run green).

**The disproven-in-advance candidates (documented without execution —
the design-probe analysis)**: (1) a bg-axis mutation on the divider's
inline `backgroundColor` — the inline style is not a Tailwind class, so
the viewport-scoped responsive-variant dodge does not apply (a raw
style flip would fail the bg axis but is NOT inert below 1024px — it
would cascade into any future mobile divider pin; the h-axis mutation
alone demonstrates the failure semantics); (2) a trend-icon color
mutation (the per-type `color` prop) — refuted by the per-type trilogy
dependence (the same constant feeds the icon circle tint and the hover
radial gradient — `hexToRgba(color, 0.125)` + the gradient — cascading
the v51 F2 icon-circle bg and the hover-reveal chrome axes); (3) an
fs-axis mutation on the count row (text-sm → text-sm lg:text-base) —
REFUTED by the v86 RATIO-LINE-HEIGHT TRAP lesson (any font-size override
scales the row's line-height 20px → 22px, cascading the row.h axis AND
every card-height-governed pin [the v40 F1 304×210 bands, the v51 F2
210-height] — the row height is content-governed).

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → `npm run build` → **291 e2e** in chunks
(+1) → 35 smoke; the 16 standing screenshots regenerated + byte-
compared (the same-DB discipline; the seedcheck under
`env -u DATABASE_URL`). EXPECTED: the same-day seed + same-day shots
reproduce the committed set byte-for-byte (the v82 same-day-seed
byte-identity law — the seed planted and the shots taken on the same
calendar day 2026-10-18); any DATE-class diff pixel-arbitrated per the
v66/v75/v80/v86 discipline, never a full-page VLM verdict; any
rasterization-noise class re-classified per pixel if it recurs.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the stat-card count-row + divider census at 1280 (the row {h/display/gap/alignItems/fs/color} + the divider {tag/h/bg/flexGrow} + the trend icon {16×16} + the per-type color trilogy + the docSW guard), riding the plain authenticated dashboard view | tests/e2e/dashboard.spec.ts |
| 2 | sanity | the pin-sanity mutation (the EXECUTED form): the divider's `h-px` → `h-px lg:h-0.5` (dashboard-view.tsx:618, by LINE NUMBER) → the pin FAILS at exactly the divider.height axis ("1px" → "2px"; the row/trend/docSW axes stay green); the full dashboard.spec.ts under the mutation: only the v88 pin red; restored → GREEN (the standalone REBUILD as a SEPARATE command; the post-restore full run green) | src/components/budget/dashboard-view.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 291 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v88 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (290→291 + the v88 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v88 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 123 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.45 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v88 section (the new probes + the divider-misread lesson + the fresh-clone reprovisioning note) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_211.md + the repo worklog Session 123 entry | docs/session_211.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the stat-divider-arbit-v88.sh census's
  own measured values, byte-identical on both sides' dashboards at
  1280x800: the row `{h: 20, display: "flex", gap: "8px", alignItems:
  "center", fs: "14px", color: "rgb(10, 10, 10)"}`; the divider `{tag:
  "DIV", h: "1px", bg: "rgb(229, 231, 227)", flexGrow: "1"}`; the trend
  `{w: 16, h: 16, color: rgb(143, 188, 63) | rgb(59, 126, 161) |
  rgb(224, 122, 59) per type}`; the docSW 1280.
- The source confirms the values: dashboard-view.tsx:616 —
  `<div className="flex items-center gap-2 text-sm">` (flex/gap-2 =
  8px/center/text-sm = 14px; the row height = the text's 20px line box;
  the color rgb(10,10,10) inherited from the body text token);
  dashboard-view.tsx:618 — `<div className="h-px flex-1"
  style={{ backgroundColor: rgb.border }} aria-hidden="true" />`
  (h-px = 1px; flex-1 = flexGrow 1; rgb.border = rgb(229,231,227);
  the ONLY `h-px flex-1` in src, grep-verified); the trend icon —
  `<TrendingUpIcon className="h-4 w-4" style={{ color }} />` (16×16;
  the per-type color constant).
- The pin-sanity target (the executed form): `h-px` → `h-px lg:h-0.5`
  flips ONLY the divider's height at ≥1024px (1px → 2px) —
  grep-verified: no spec asserts the stat-card divider's height at any
  viewport; the row's height is the text's line box (a 2px centered
  divider never grows it); the card height 210 is content-governed and
  unchanged; the v51 F2 390 pin asserts no divider axis; the login-card
  OR divider and the dropdown/select separators are different
  components.
- The existing pins are SAFE: the v40 F1 1280 geometry bands (the
  304×210 cards) — the mutation preserves the card height; the v51 F2
  390 stats-row pin — below the lg: breakpoint the variant inert, and
  its countRow axes (fs/gap/color) height-independent; the v83
  cross-row rhythm pin — the row heights unchanged; the v60/v44
  drill-down pins — different surfaces (the breakdown card, not the
  stat cards); the stat-card interaction tests — the click/navigation
  behavior untouched.
- The blast radius: ZERO production-code change (the divider claim a
  VLM MISREAD disproven by the both-sides census — the pin-only line
  holds); the pin-sanity mutation touches
  `src/components/budget/dashboard-view.tsx:618` (the divider's
  className) REVERTED before ship (`git diff src/` = 0 lines at
  commit).
- The chain gate: lint → typecheck → 108 unit → `npm run build` →
  292+1 e2e chunk executions (**291 unique** after: +1 — the F4 pin)
  → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every
  agent-browser run; the with-server boots fresh per command; the
  reference session EXPIRES between long eval gaps — the login-retry
  loop handles it; the e2e chunks pass FULL file paths;
  `ss -tlnp | grep :3100` + kill before every full-chain run (the
  v53 orphaned-webServer lesson); one-shot Prisma scripts need
  `env -u DATABASE_URL`; no dollar sequences in census JS inside
  double-quoted bash strings (the v64 rule); no attribute-value
  selectors in the census (the v78 rule — geometry + text-content
  filters only); the UNQUOTED heredoc with the env-injected census
  (the v73 lesson); the mutations need the standalone REBUILD as a
  SEPARATE command (the v53 lesson); the clean-check gate re-runs
  AFTER every new file lands (the v69 lesson); the build step is
  `npm run build` (the v76 F0 lesson); the screenshot DATE-class diffs
  after a fresh seed are pixel-arbitrated, never full-page
  VLM-verdicted (the v80 lesson); the sed derivation of the standing
  checks needs the bare-number session-name token family TOO
  (ref81/clone81 — the v84 lesson, applied and diff-verified this
  session); the sed derivation of the probe series needs the
  BARE-NUMBER tmp-dir family TOO (/tmp/vlm82 → /tmp/vlm88 — the v84
  lesson's second face, caught and fixed this session); a VLM
  IDENTICAL verdict still gets the census (the v75 convention); the
  census finders must not depend on ACCESSIBLE NAMES for
  reference-side elements (the v87 lesson — geometry + position +
  text-content finders only); a NEW VLM flag gets a dedicated one-shot
  both-sides census BEFORE it counts as a gap (the v88 lesson — the
  divider misread).
- The deferred queue (all need reference WRITES — out of bounds under
  the v46 read-only rule — plus the login family): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census, the line-items dialog
  glyphs; the login card's pad family + logo radius pin (the
  pair-arbit-v87.sh census values recorded in the v87 plan's F4 — the
  login + calculator pair's FIFTH re-run).
- The v89 queue (suggestions): (1) the re-run cadence rotates to the
  next-oldest candidate after this pair (the v83-era DASHBOARD pair
  [the dashboard FULL-PAGE at desktop 1280 — the below-the-fold Budget
  Guidelines card + the quick-action row], last re-shot v83 — now the
  oldest remaining [v83 < v84 < v85 < v86 < v87 < v88]; the pair's
  FOURTH re-run [v61 → v68 → v77 → v83 → v89]), (2) the axe-core watch
  at its next re-check point (only a 5.x wrapper changes the
  calculus), (3) the deferred reference-write censuses (unchanged).
