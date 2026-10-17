# Remediation Plan v82 — the re-run cycle's next-oldest candidate (the v60-era networth + drill-down pair's third re-run) + the axe watch + the summary card's completion-family pin (PIN-ONLY)

The formal narrative: `docs/session_194.md`. The queue: the session-193
continuation of the v81 plan's v82 suggestion — **the ledger-verified
target** (the v81 plan's suggestion AGREEING with the rotation ledger:
the v60-era networth + drill-down pair [the networth view + the
dashboard drill-down EXPANDED at desktop 1280], last re-shot v76, is the
oldest remaining candidate [v76 < v77 < v78 < v79 < v80 < v81]; the
pair's THIRD re-run [v60 → v67 → v76 → v82] — the FIFTH consecutive
queue/ledger agreement), plus the axe-core watch at its re-check point
and the 76th standing checks. **PIN-ONLY for src/ — no
production-code change; +1 e2e = 285.**

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered; the standalone static + public copies verified) ·
**284 e2e ✓** (104 + 104 + 78 chunk executions = 286 total = 284 unique
tests in 24 files [283 chromium + 1 setup, the setup re-run per chunk as
the project dependency] — the exact documented v81 state) · 35/35 smoke
✓. The workspace REBUILT (the reset path — the second consecutive
reset-boundary): `git clone` landed at `main @ edb4707` (v81 shipped +
the session_193 transcript), the tree clean; node_modules reinstalled
(354 packages), chromium-1243 reinstalled, `.env` rewritten
(DATABASE_URL="file:../db/custom.db", db/ at the repo root),
`prisma generate` + `npm run db:push` + `npm run db:seed` re-run (the
polluting shell DATABASE_URL handled via the documented `env -u`
discipline), no orphaned servers, the seedcheck confirming the exact
seed (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets /
2 liabilities) before any flow ran.

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next
prereleases; no 5.x exists), npm-latest `axe-core` 4.14.0; the lockfile
holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted
axe-core 4.14.0, no nested engine dir); the engine-contract pin GREEN
standalone (2 passed).

### F2 — the 76th standing checks: ALL GREEN (version-bumped from v75 — version-bump-only diffs verified)

The mobile menu VERIFIED WORKING (the 76th consecutive time —
`hitIsBurgerChild:true`, the sheet opens + closes on nav, the nav
landmark present); the reference's four bugs ALL live [toast-blocker,
sheet-trap `overlayCount:1`, no-landmark, the 464px /networth
overflow]; the data census UNCHANGED (the 76th clean drift check:
networth "1 items · $25,000" / income "1 items · $5000.00" /
expenses "4 items · $525.00"); the SEO pair live; zero overflow at 390
on all five clone views.

### F3 — the re-run pair (the networth view + the dashboard drill-down EXPANDED at desktop 1280x800)

**The NETWORTH pair: VERDICT IDENTICAL** — the only LAYOUT/STYLE flag
the reference's "Edit with Base44" overlay (the platform-chrome
class); every other reported delta DATA (the seed classes: the
figures, the 1-asset vs 3-asset groups, the ratio ∞:1 vs 0.21:1) —
matching the v76 re-run's own networth verdict classes. The
both-sides census (arbit-v82.sh PART B — the v76 census axes
re-measured) BYTE-IDENTICAL on every chrome axis: the card
960×333/32px/16px/the 135deg forest→lime gradient/the 26-58-46
shadow; the head row 76/mb 32px/flex/center; the label 14px/
rgba(255,255,255,0.8)/mb 8px/h 20; the figure 48px/700/white/lh
48px/h 48; the medallion 64×64/white-20%/icon 32×32; the stat grid
440px 440px/rows 84px/gap 16px/896×84; the stat tile 440×84/16px/
12px/white-10%/blur(10px)/label 12px-h16-mb4/amount 24px-700-h32;
the ratio footer mt 24/pt 24/1px rgba(255,255,255,0.2)/h 53/label
14px/value 18px-700. The ONE width delta — the labelBlock w ref 304
vs clone 357 — the DATA-CONDITIONAL width class (the figure text
"$25,000.00" [10 chars] vs "-$245,950.00" [12 chars] at the same
48px/700 — the block wraps the longer negative figure; the same
v76-era mechanism, the heights byte-identical).

**The DRILL-DOWN pair: VERDICT DIFFERENT with EIGHT flags, every one
DOM-arbitrated to a documented class** (matching the v76 re-run's own
flag-set classes):

1. the "Dashboard nav highlighted in the clone" — the v56 SUPERSET
   class (AGENTS.md rule 3; the census: the reference's link INERT
   {color rgb(63,63,270), fw 400} vs the clone's ACTIVE {color
   rgb(255,255,255), fw 500});
2. the "progress bar significantly longer" — the pct × 568 DATA class
   (the v60 arbitration's own values REPRODUCED EXACTLY: fillW ref
   173 vs clone 357 on the byte-identical 568×12
   rgba(255,255,255,0.1) track — zero drift since v60);
3. the "additional expanded category (Freelance) + footer 2 vs 1" —
   the seed-data class (the clone's income carries 2 categories
   [Salary + Freelance] vs the reference's 1 — the drill-down's
   row-count/footer-count arithmetic follows the data);
4. the "donut proportions differ" — the seed-data class (92.3/4.6/3.1
   vs 81.6/13.8/4.6);
5. the "percentage labels present in the clone, absent in the
   reference" — the v60 PERCEPTION class, re-arbitrated live both
   sides: the reference DOES render its labels (the census's own
   texts "92.3%"/"4.6%"/"3.1%", count 4 [1 group + 3 labels — the
   reference's g carries the texts INSIDE, the clone's recharts-3
   layer renders them separately, the v40 dump], labelLineCount 0,
   16px, fill black, sectors 3 — the chrome BYTE-IDENTICAL, the texts
   each site's own data);
6. the "'Total Expense' vs 'Total Expenses'" — a VLM MISREAD (the v43
   misattribution lesson's live case: the reference's statTitles
   measured VERBATIM — "Total Income"/"Total Savings"/"Total
   Expenses" [SPAN + H3 both, 14px/500/rgb(107,114,128)],
   hasSingular:false, hasPlural:true — the clone's source renders the
   same plural "Total Expenses" [dashboard-view.tsx:481], the v40
   Tab-census pin holding the clone's "Total Expenses- $2235.00"
   accessble name — the titles BYTE-IDENTICAL);
7. the "avatar differs" — the user-identity class ("U" vs "D");
8. the "Base44 overlay/widget" — the platform-chrome class.

**NO NEW GAP — the v82 iteration is PIN-ONLY.**

### F4 [PIN] — the networth summary card's completion-family census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 285)

The never-pinned axes (the existing pins cover around them — the v60
F1 pin holds the card's w/pad/radius/gradient/shadow + the figure/
label typography + the medallion w/bg/iconW + the grid template/gap +
the tile w/pad/radius/bg/blur/amount typography + the ratio VALUE
18px/700 + the tablist/groupHeader/grid/card0/docSW; the v67 F3 pin
holds the HEIGHT family [card/headRow/figure/grid-rows/tile/footer]
+ the headRow mb/display + the label mb/h + the figure lh + the tile
labelH/labelMb/amtH; the v4-era structure test holds the tile label
12px + the footer border 1px solid rgba(255,255,255,0.2) at the
default 1280×720; the G9 test holds the ratio label's COLOR):

- **The HEAD ROW's ALIGNMENT at 1280**: alignItems "center" — the v80
  titleRow.alignItems pattern's networth twin (the v67 pin holds the
  row's h/mb/display, never its items axis).
- **The LABEL BLOCK's HEIGHT at 1280**: h 76 (the min-w-0 wrapper's
  own height — the label 20 + mb 8 + the figure 48 stack; the v67 pin
  holds the PARENT row's h 76, never the block's own).
- **The STAT GRID's content-box WIDTH at 1280**: w 896 (the 960 card
  − the 2×32 pad arithmetic twin; v60 holds the template/gap, v67 the
  rows/h — never the bounding width).
- **The RATIO LABEL's TYPOGRAPHY at 1280**: fs "14px" (text-sm — G9
  holds the label's color, the structure test the VALUE's 18px/700,
  v67 the footer's mt/pt/borderW/h — never the label's own
  font-size).

Every pinned axis STATIC chrome (none depends on the figures — the
labelBlock's WIDTH is the data-conditional axis and is EXCLUDED); the
pin rides the plain authenticated /networth view (no dialogs, no
fixture writes — the simplest read-only state).

**The pin-sanity mutation**: the ratio label's `text-sm` → `text-sm
lg:text-base` (net-worth-view.tsx:389) — flips EXACTLY the
ratioLabel.fs axis at 1280 ("14px" → "16px") and nothing else (the
mutation is viewport-scoped: below 1024px the lg: variant is inert —
the 390/640 families untouched; at 1280 the ratio row's height stays
value-governed [text-lg's 28px lh > any label line-box up to 24px] —
the v67 footer h 53 and the v60 value axes stay GREEN; the G9 color
pin and the v4-era structure test's ratioSize [the VALUE span] stay
GREEN; the v82 pin's other three axes [headRow.items, labelBlock.h,
statGrid.w] are mutation-inert) — cascade-free by construction, then
restored (the standalone REBUILD as a SEPARATE command; `git diff
src/` = 0 lines).

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → `npm run build` → **285 e2e** in chunks
(+1) → 35 smoke; the 16 standing screenshots regenerated + byte-
compared (the same-DB discipline; the seedcheck under
`env -u DATABASE_URL`). EXPECTED: the FRESH-SEED DATE-class diffs
(the re-clone's db:seed planted 2026-10-18 vs the v81 set's
2026-10-17 — a +1-day shift on the date-bearing text bands per the
v80 lesson) pixel-arbitrated per the v66/v75/v80 discipline, never a
full-page VLM verdict.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the summary card's headRow.items + labelBlock.h + statGrid.w + ratioLabel.fs census at 1280 | tests/e2e/networth.spec.ts |
| 2 | sanity | the pin-sanity mutation: the ratio label's `text-sm` → `text-sm lg:text-base` (net-worth-view.tsx:389) → the pin FAILS at exactly the ratioLabel.fs axis ("14px" → "16px"); restored → GREEN (the standalone REBUILD as a SEPARATE command) | src/components/budget/net-worth-view.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 285 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v82 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (284→285 + the v82 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v82 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 117 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.39 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v82 section (the new probes + the ledger-verified queue note) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_194.md + the repo worklog Session 117 entry | docs/session_194.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the arbit-v82.sh PART B census's own
  measured values, byte-identical on both sides' summary cards at
  1280x800: the headRow `{items: "center"}`; the labelBlock
  `{h: 76}`; the statGrid `{w: 896}`; the ratioLabel `{fs: "14px"}`.
- The source confirms the values: the head row
  `mb-8 flex items-center justify-between gap-4`
  (net-worth-view.tsx:342); the label block `min-w-0` wrapping the
  label mb-2 text-sm (h 20) + the figure sm:text-5xl (h 48) = 76; the
  stat grid `grid grid-cols-1 gap-4 sm:grid-cols-2` inside the 32px
  card pad (960 − 64 = 896); the ratio label `text-sm` (line 389).
- The pin-sanity target: the ratio label's `text-sm` flips ONLY the
  ratioLabel.fs axis at 1280 ("14px" → "16px") — the v82 pin's own
  completion axis; viewport-scoped so the 390/640 families (v41/v47/
  v53/v63) are untouched; the ratio row's height stays value-governed
  (the 28px text-lg line-box > the 24px text-base line-box) so the
  v67 footer h 53 stays GREEN; grep-verified: the ratio LABEL's
  font-size is asserted NOWHERE (the G9 test holds its color; the
  v4-era structure test holds the VALUE's 18px via
  span:last-child; the v60/v67 pins hold the value/spacing axes).
- The existing pins are SAFE: the v67 pin's height family (disjoint
  from the four completion axes — the pin adds, never duplicates);
  the v60 pin's chrome family (a superset on other axes); the G9
  color pin and the structure test's 12px/18px/border-color axes
  (unaffected by an lg:-scoped label mutation).
- The blast radius: ZERO production-code change (every census delta a
  documented class — the pin-only line holds); the pin-sanity
  mutation touches `src/components/budget/net-worth-view.tsx:389`
  (the ratio label's className) REVERTED before ship (`git diff
  src/` = 0 lines at commit).
- The chain gate: lint → typecheck → 108 unit → `npm run build` →
  284 e2e (**285** after: +1 — the F4 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every
  agent-browser run; the with-server boots fresh per command; the
  reference session EXPIRES between long eval gaps — the login-retry
  loop handles it; the e2e chunks pass FULL file paths;
  `ss -tlnp | grep :3100` + kill before every full-chain run (the
  v53 orphaned-webServer lesson); one-shot Prisma scripts need
  `env -u DATABASE_URL`; no dollar sequences in census JS inside
  double-quoted bash strings (the v64 rule); no attribute-value
  selectors in the census (the v78 rule — geometry + text-content
  filters only); the QUOTED heredoc with the env-injected census
  (the v73 lesson); the mutations need the standalone REBUILD as a
  SEPARATE command (the v53 lesson); the clean-check gate re-runs
  AFTER every new file lands (the v69 lesson); the build step is
  `npm run build` (the v76 F0 lesson); the screenshot DATE-class
  diffs after a fresh seed are pixel-arbitrated, never full-page
  VLM-verdicted (the v80 lesson).
- The deferred queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census, the line-items dialog
  glyphs.
- The v83 queue (suggestions): (1) the re-run cadence rotates to the
  next-oldest candidate after this pair (the v61-era dashboard pair
  [the dashboard FULL-PAGE at desktop 1280], last re-shot v77 — now
  the oldest remaining [v77 < v78 < v79 < v80 < v81 < v82]), (2) the
  axe-core watch at its next re-check point (only a 5.x wrapper
  changes the calculus), (3) the deferred reference-write censuses
  (unchanged).
