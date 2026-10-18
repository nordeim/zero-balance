# Remediation Plan v85 — the re-run cycle's next-oldest candidate (the v79-era items pair's fourth re-run) + the axe watch + the expense-card content-wrapper + orange-dot titleRow census pin (PIN-ONLY)

The formal narrative: `docs/session_203.md`. The queue: the session-202
continuation of the v84 plan's v85 suggestion — **the ledger-verified
target** (the v84 plan's suggestion AGREEING with the rotation ledger:
the v79-era ITEMS pair [the income + expenses view pair at desktop
1280x800], last re-shot v79, is the oldest remaining candidate [v79 <
v80 < v81 < v82 < v83 < v84]; the pair's FOURTH re-run [v57 → v64 →
v70 → v79 → v85] — the EIGHTH consecutive queue/ledger agreement), plus
the axe-core watch at its re-check point and the 79th standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 288.**

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered) · **289 e2e chunk executions ✓** (102 + 104 + 83
across three chunk splits of the 23 files — the same total execution
count as the documented v84 state's 102+108+79 = 289 = 287 unique
tests) · 35/35 smoke ✓. The workspace PRESERVED (no reset): `git pull`
landed at `main @ 3f92b87` (v84 shipped + the session_202 transcript),
the tree clean; node_modules in place (355 top dirs), chromium-1243 in
place, `.env` verified (DATABASE_URL="file:../db/custom.db", db/ at the
repo root), the seedcheck exact (7 items / rent 1850 / expenses 2235 /
0 line items / 3 assets / 2 liabilities) before any flow ran, no
orphaned servers.

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next
prereleases beyond — no stable 4.14.1, no 5.x exists), npm-latest
`axe-core` 4.14.0; the lockfile holding the v68 dedupe state (the
wrapper 4.14.0 + ONE hoisted axe-core 4.14.0 — no nested engine dir
under `node_modules/@axe-core/playwright/`); the engine-contract pin
GREEN standalone (2 passed).

### F2 — the 79th standing checks: ALL GREEN (version-bumped from v78 — version-bump-only diffs verified)

ref-standing-v79.sh + standing-checks-v79.sh (version-bumped from v78
— after normalizing the version tokens the files are byte-identical:
only the header comment, the AGENT_BROWSER_SESSION name, and the done
echo differ). Reference side: the four bugs ALL live [toast-blocker
`hitIsBurgerChild:false`; sheet-trap `overlayCount:1`; no-landmark
`navLandmark:false`; the 464px /networth overflow at 390]; the data
census UNCHANGED (the 79th clean drift check: networth "1 items ·
$25,000" / income "1 items · $5000.00" / expenses "4 items · $525.00");
the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation
menu VERIFIED WORKING (the **79th consecutive time**: `hitIsBurgerChild:true`,
the sheet opens, closes on nav, the nav landmark present), zero overflow
at 390 on all five views (docSW 390 everywhere), the SEO pair live.

### F3 — the re-run pair (the v79-era items pair: income + expenses at desktop 1280x800, full-page)

**Both verdicts DIFFERENT, every flag DOM-arbitrated to a documented
class — NO NEW GAP:**

1. **PAIR 1 (INCOME at 1280)**: the avatar letter "U" vs "D" — the
   user-identity class; the 1-card vs 2-card grid + the card figures +
   the badge variations — the seed-data classes; **the "Edit with
   Base44" floating-button flag — a VLM IMAGE-ATTRIBUTION SWAP,
   disproven by the two-step one-shot arbitration
   (base44-fab-arbit-v85.sh + crop-fab-v85.mjs +
   vlm-arbit-fabcrop-v85.mjs)**: the DOM census finds ZERO Base44
   elements on EITHER side (the platform FAB renders outside the
   queryable body text — the platform's iframe chrome); the pixel
   census locates the dark FAB pixels in the REFERENCE shot's
   bottom-right corner ONLY (6585 dark px in the 340×100 crop vs 0 in
   the clone's — the FAB is black, ~150×40); the single-image VLM reads
   of the two crops confirm it: the reference crop shows the black
   "Edit with Base44" button (the orange icon + the x close), the clone
   crop is solid white. **The flag's true class: the Base44
   platform-chrome class (the reference's own platform chrome) — the
   VLM swapped which image carries it.**

2. **PAIR 2 (EXPENSES at 1280)**: the card footer's payment-method
   chips (ref: date only on its first card) — the v57 DATA-CONDITIONAL
   class; the badge arrangement/height (the wrap pushing the footer
   down, the taller cards) — the v57 Recurring superset wrap class; the
   avatar — the user-identity class; the figures/counts/categories —
   the seed-data classes. **Matching the v79 re-run's own flag-set
   classes exactly.**

**The both-sides census (arbit-v85.sh — the v75 convention: the census
runs regardless of the verdict; the v79 census axes re-measured): the
v79 census values REPRODUCED EXACTLY — zero drift since v79 on every
axis:**

- **The AVATAR chrome BYTE-IDENTICAL** (w 36 × h 36 / radius 9999px /
  fs 14px / fw 600 / color rgb(255,255,255) / bg rgb(143,188,63) — the
  identity text "U" vs "D" the only delta, the user-identity class).
- **The GRID + CARD chrome BYTE-IDENTICAL** (grid w 960 / gap 16px /
  the 3-col 309.328px template; card w 309 / pad 20px / radius 12px /
  border rgb(229,231,227)); the childCount (1 vs 2 income, 4 vs 3
  expenses) the seed-count class; the card h (ref 200 vs clone 230) the
  v70b-decomposed class — the Recurring superset badge's wrap h 52
  (22+8+22) → +30px, and the 1-row grid STRETCHES the shorter sibling.
- **The TITLE ROW chrome BYTE-IDENTICAL** (gap 8px / dot 8×8 / income
  dotBg rgb(143,188,63) + expenses dotBg rgb(224,122,59) on BOTH sides
  / font 16px / weight 600).
- **The AMOUNT leaf chrome BYTE-IDENTICAL** (fs 24px / fw 700 / lh 32px
  / h 32; the income accent rgb(143,188,63) + the expenses accent
  rgb(224,122,59) matching per type — the texts the seed-data class).
- **The FOOTER + BADGE chrome BYTE-IDENTICAL** (footer
  flex/space-between/12px/rgb(107,114,128)/h 16 with the children flex
  gap 4px icons 12×12; the badge row flex/wrap/8px gap/mb 12px; badge0
  radius 6px/pad 2px 10px/fs 12px/fw 600/h 22); the expenses footer
  childCount (1 vs 2) the v57 DATA-CONDITIONAL class; the badgeRow h
  (22 vs 52) + texts the v57 wrap/classification-VALUE classes.
- **The FILTER CARD BYTE-IDENTICAL on BOTH variants** (the income
  variant: card 960×86/pad 24px/radius 16px/search 447×36
  SPANNING/3 children/2 comboboxes 216×36 at 14px; the expenses
  variant: search 216×36 NOT spanning/4 children/3 comboboxes — the
  v64/v70 pins' own values, zero drift) + the docSW 1280 guard on both
  views.

**The wrapper-family supplemental census (wrapper-arbit-v85.sh — the
pin's own axes, measured on BOTH sides at 1280): the EXPENSE-ONLY
content wrapper BYTE-IDENTICAL** (display block / flexGrow 1 /
**paddingRight 96px** — the expenses-conditional `pr-24`, the room
reserved for the hover action row [item-card.tsx:119 — the ONLY pr-24
in src]; the income twin's paddingRight **0px** on BOTH sides — the
conditional control); **the expenses TITLE ROW's full geometry
BYTE-IDENTICAL** (flex/center/8px/h 24 + the dot 8×8/9999px in the
expenses orange rgb(224,122,59) + the h4 16px/600/rgb(26,58,46)); the
hover action row byte-identical (top 247/right 696/opacity 0/gap 8px —
the v45 F1b pin's own family); the subtitle null-vs-"Streaming" the
subtitle-CONDITIONAL class (the v71 F4 idiom — the reference's
Miscellaneous card carries no subcategory).

**NO NEW GAP — the v85 iteration is PIN-ONLY.**

### F4 [PIN] — the expense-card content-wrapper + the orange-dot titleRow census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 288)

The never-pinned axes (the existing pins cover around them: the v45 F1a
pin asserts the income titleRow's gap/dotW/dotBg/font/weight but never
its display/alignItems/h/dotH/dotRadius, never the h4's color, and
nothing on the expenses twin; the v80 pin the SAVINGS titleRow's full
geometry + heights — the per-type trilogy's blue twin only; the v45 F1b
pin the action row's own geometry; the v57 F1b pin the expenses
grid/card-box/footer/badge chrome — never the titleRow, never the
wrapper; the v79 pin the avatar + the amount accents + the income card
h; grep-verified: the expenses dot's orange rgb(224,122,59) appears in
NO spec's dot assertion, and NO spec asserts the wrapper's paddingRight
or the string pr-24):

- **The WRAPPER's pr family at 1280** (item-card.tsx:119): display
  "block" / flexGrow "1" / paddingRight "96px" — the expenses-conditional
  pr-24 (the hover action row's reserved room; a broken conditional —
  the pr leaking to income/savings, or dropping from expenses — flips
  this axis);
- **The TITLE ROW's full geometry at 1280** (item-card.tsx:120-124):
  display "flex" / alignItems "center" / gap "8px" / h 24 / the dot
  {W 8, H 8, radius "9999px", bg "rgb(224, 122, 59)"} — the orange
  twin's FIRST pin anywhere (TYPE_COLORS.expense on the dot — the v79
  pin holds the same color on the AMOUNT leaf; this pin holds it on the
  DOT) / the h4 {fs "16px", fw "600", color "rgb(26, 58, 46)" —
  rgb.forestDark, never pinned on any item-card title};
- **The INCOME twin's paddingRight control at 1280**: "0px" — the
  conditional's other leg (the pr scoped to expenses ONLY on both
  sides);
- the docSW 1280 guard on both views.

Every pinned axis STATIC chrome (the pr conditional on the item type —
not the data; the titleRow content-governed — the h4's single-line
line box; the dot fixed-size); the pin rides the plain authenticated
/expenses + /income views at 1280x800 on the e2e seed (the
Entertainment card first — the v57 F1b walk), no dialogs, no fixture
writes.

**The pin-sanity mutation**: the wrapper's `pr-24` → `pr-20`
(item-card.tsx:119, applied by LINE NUMBER — the ONLY `pr-24` in src,
grep-verified) — flips EXACTLY the pin's wrapper.paddingRight axis
("96px" → "80px") and nothing else: the titleRow's geometry is
content-governed (the h4 "Entertainment" is a single line at 16px ≈
110px ≪ the narrowed box's ~141px; the dot fixed 8×8; the row h 24 the
h4 line box); the amount/badge/footer rows are SIBLINGS of the wrapper
(card-level children — their wrap/heights untouched); the hover action
row is absolute (top-3 right-3 — the v45 F1b axes untouched); the
income/savings wrappers carry NO pr (the mutation's expense-scoped
condition — the v45 F1a income titleRow, the v80 savings titleRow +
heights, the v79 income cardH all stay GREEN); the 390 subtitle tests
stay GREEN (the "Apartment"/"Probe NoSub" texts are single-line at
both 96px and 80px paddings — the titleRowH 48/28 arithmetic
unaffected) — cascade-free by construction, then restored (the
standalone REBUILD as a SEPARATE command; `git diff src/` = 0 lines).

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → `npm run build` → **288 e2e** in chunks
(+1) → 35 smoke; the 16 standing screenshots regenerated + byte-
compared (the same-DB discipline; the seedcheck under
`env -u DATABASE_URL`). EXPECTED: the same-day seed + same-day shots
reproduce the committed set byte-for-byte (the v82 same-day-seed
byte-identity law); any DATE-class diff pixel-arbitrated per the
v66/v75/v80 discipline, never a full-page VLM verdict.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the wrapper's pr family + the titleRow's full geometry (the orange dot's first pin) + the income pr-0 control at 1280 | tests/e2e/items.spec.ts |
| 2 | sanity | the pin-sanity mutation: the wrapper's `pr-24` → `pr-20` (item-card.tsx:119, by LINE NUMBER) → the pin FAILS at exactly the wrapper.paddingRight axis ("96px" → "80px"; the titleRow family stays green); restored → GREEN (the standalone REBUILD as a SEPARATE command) | src/components/budget/item-card.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 288 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v85 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (287→288 + the v85 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v85 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 120 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.42 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v85 section (the new probes + the image-attribution-swap lesson) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_203.md + the repo worklog Session 120 entry | docs/session_203.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the wrapper-arbit-v85.sh census's own
  measured values, byte-identical on both sides' items views at
  1280x800: the wrapper `{display: "block", flexGrow: "1",
  paddingRight: "96px"}` (expenses) / `{paddingRight: "0px"}`
  (income control); the titleRow `{display: "flex", alignItems:
  "center", gap: "8px", h: 24, dotW: 8, dotH: 8, dotRadius: "9999px",
  dotBg: "rgb(224, 122, 59)", h4Fs: "16px", h4Fw: "600", h4Color:
  "rgb(26, 58, 46)"}`; the docSW 1280.
- The source confirms the values: item-card.tsx:119 — `cn("flex-1",
  item.type === "expense" && "pr-24")` (the ONLY pr-24 in src,
  grep-verified); :120 — `mb-1 flex items-center gap-2` (the row);
  :121 — `h-2 w-2 rounded-[9999px]` + `style={{ backgroundColor:
  accent }}` with `accent = TYPE_COLORS[item.type]` (:69) and
  `TYPE_COLORS = { income: COLORS.limeGreen, savings: COLORS.blueMedium,
  expense: COLORS.orangeDark }` (constants.ts:92-96 — orangeDark =
  rgb(224,122,59)); :122 — `font-semibold` + `style={{ color:
  rgb.forestDark }}` (constants.ts:80 — rgb(26,58,46)).
- The pin-sanity target: `pr-24` → `pr-20` flips ONLY the expenses
  wrapper's paddingRight (96 → 80) — grep-verified: no spec asserts the
  wrapper's paddingRight or pr-24 anywhere; the titleRow's axes are
  width-independent (content-governed row h, fixed-size dot, single-line
  h4 — "Entertainment" ≈ 110px ≪ 141px); the amount/badge/footer are
  card-level siblings of the wrapper (their wrap arithmetic untouched);
  the action row is absolute (top-3 right-3 — the v45 F1b family
  untouched); the income/savings wrappers carry no pr (the v45 F1a /
  v79 / v80 pins untouched); the 390 subtitle tests ("Apartment" /
  "Probe NoSub" single-line at both paddings — titleRowH 48/28
  arithmetic unaffected) untouched.
- The existing pins are SAFE: the v45 F1a income titleRow pin asserts
  gap/dotW/dotBg(lime)/font/weight — a DISJOINT axis set from the
  wrapper family, and the income twin's own paddingRight is the pin's
  CONTROL leg (0px, unaffected by the expense-scoped mutation); the
  v80 savings titleRow pin (full geometry) — the savings wrapper carries
  no pr; the v57 F1b expenses pin (grid/card-box/footer/badge) —
  card-level surfaces; the v45 F1b action-row pin — the absolute
  family; the v79 avatar/amount/cardH pins — the avatar is in the rail,
  the amount leaf and the card height are wrapper-external; the v74
  h4/amount chrome pins — the h4's fs/fw/lh are width-independent; the
  v52 F3 mobile pin — box-level axes (w/pad/radius/shadow); the
  empty-subtitle/Rent-subtitle 390 tests — single-line texts at both
  paddings.
- The blast radius: ZERO production-code change (every census delta a
  documented class — the pin-only line holds); the pin-sanity mutation
  touches `src/components/budget/item-card.tsx:119` (the wrapper's cn
  expression) REVERTED before ship (`git diff src/` = 0 lines at
  commit).
- The chain gate: lint → typecheck → 108 unit → `npm run build` →
  289 e2e chunk executions (**288 unique** after: +1 — the F4 pin) →
  35 smoke.
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
  (the v73 lesson — the clone-side heredoc stays UNQUOTED only for the
  census-variable injection); the mutations need the standalone REBUILD
  as a SEPARATE command (the v53 lesson); the clean-check gate re-runs
  AFTER every new file lands (the v69 lesson); the build step is
  `npm run build` (the v76 F0 lesson); the screenshot DATE-class
  diffs after a fresh seed are pixel-arbitrated, never full-page
  VLM-verdicted (the v80 lesson); the sed derivation of the v85 probe
  series needs BOTH the version substitutions AND the session-name/
  tmp-dir substitutions (the v84 lesson — applied and grep-verified
  clean this session); a VLM pairwise flag claiming an element's
  presence in one image is arbitrated by the DOM census + the pixel
  crop census + the SINGLE-IMAGE VLM read (the v85 image-attribution
  lesson — never the pairwise verdict alone).
- The deferred queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census, the line-items dialog
  glyphs.
- The v86 queue (suggestions): (1) the re-run cadence rotates to the
  next-oldest candidate after this pair (the v80-era SAVINGS pair
  [the savings view at desktop 1280], last re-shot v80 — now the
  oldest remaining [v80 < v81 < v82 < v83 < v84 < v85]), (2) the
  axe-core watch at its next re-check point (only a 5.x wrapper
  changes the calculus), (3) the deferred reference-write censuses
  (unchanged).
