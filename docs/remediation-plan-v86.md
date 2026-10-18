# Remediation Plan v86 — the re-run cycle's next-oldest candidate (the v80-era savings pair's fourth re-run) + the axe watch + the savings goal-card's subtitle-P + header-row + wrapper-third-leg census pin (PIN-ONLY)

The formal narrative: `docs/session_206.md`. The queue: the v85 plan's v86
suggestion — **the ledger-verified target** (the v85 plan's suggestion
AGREEING with the rotation ledger: the v80-era SAVINGS pair [the savings
view at desktop 1280x800], last re-shot v80, is the oldest remaining
candidate [v80 < v81 < v82 < v83 < v84 < v85]; the pair's FOURTH re-run
[v58 → v65 → v74 → v80 → v86] — the NINTH consecutive queue/ledger
agreement), plus the axe-core watch at its re-check point and the 80th
standing checks. **PIN-ONLY for src/ — no production-code change; +1 e2e
= 289.**

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered) · **290 e2e chunk executions ✓** (102 + 109 + 79
across three chunk splits of the 23 files = 288 unique tests — the same
unique count as the documented v85 state's 290 = 288) · 35/35 smoke ✓.
The workspace RESET (the fresh-clone path — exercised once before, in
v80): `git clone https://github.com/nordeim/zero-balance.git` landed at
`main @ 0d20198` (v85 shipped + the session_204/205 transcripts), the
tree clean; the environment re-provisioned (npm ci + the four approved
install scripts [prisma engines + client generated], `.env` written
[DATABASE_URL="file:../db/custom.db", NEXT_PUBLIC_SITE_URL,
AUTH_SECRET generated], db/ at the repo root, `db:push` in-sync +
`db:seed` [7 budget items, 3 assets, 2 liabilities], chromium-1243
installed [the playwright 1.63 expected revision]); the seedcheck exact
(7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2
liabilities) before any flow ran, no orphaned servers.

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next
prereleases beyond — no stable 4.14.1, no 5.x exists), npm-latest
`axe-core` 4.14.0; the lockfile holding the v68 dedupe state (the
wrapper 4.14.0 + ONE hoisted axe-core 4.14.0 — no nested engine dir
under `node_modules/@axe-core/playwright/`); the engine-contract pin
GREEN standalone (2 passed).

### F2 — the 80th standing checks: ALL GREEN (version-bumped from v79 — version-bump-only diffs verified)

ref-standing-v80.sh + standing-checks-v80.sh (version-bumped from v79
— after normalizing the version tokens [v79→v80, 79th→80th, AND the
bare-number session names ref79→ref80 / clone79→clone80 — the v84
substitution-gap lesson's third token family] the files are
byte-identical: only the header comment, the AGENT_BROWSER_SESSION
names, and the done echo differ). Reference side: the four bugs ALL
live [toast-blocker `hitIsBurgerChild:false`; sheet-trap
`overlayCount:1`; no-landmark `navLandmark:false`; the 464px /networth
overflow at 390]; the data census UNCHANGED (the 80th clean drift
check: networth "1 items · $25,000" / income "1 items · $5000.00" /
expenses "4 items · $525.00"); the SEO pair live. Clone side: R1–R4
ALL GREEN — the mobile navigation menu VERIFIED WORKING (the **80th
consecutive time**: `hitIsBurgerChild:true`, the sheet opens, closes on
nav, the nav landmark present), zero overflow at 390 on all five views
(docSW 390 everywhere), the SEO pair live.

### F3 — the re-run pair (the v80-era savings pair: the savings view at desktop 1280x800, full-page)

**The verdict IDENTICAL — the pair's FIRST non-DIFFERENT verdict in its
five-shot history (v58 → v65 → v74 → v80 → v86), with the VLM's own
flag list confined to the expected data/identity classes (the subtitle
counts "1 items · $1000.00" vs "2 items · $1250.00"; the card
figures/names/badges; the avatar "U" vs "D") — zero LAYOUT/STYLE flags
to arbitrate.**

**The both-sides census (arbit-v86.sh — the v75 convention: the census
runs regardless of the verdict; the v80 census axes re-measured): the
v80 census values REPRODUCED EXACTLY — zero drift since v80 on every
axis:**

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
  flex/space-between/12px/rgb(107,114,128)/h 16 with the icon
  children flex/gap 4px/12×12; the badgeRow flex/wrap/8px gap/mb 12px;
  every badge radius 6px/pad 2px 10px/fs 12px/fw 600/h 22); the footer
  childCount (1 vs 2) the v58 DATA-CONDITIONAL class; the badgeRow h
  (22 vs 52) + the classification texts the v57 wrap/VALUE classes.
- The docSW 1280 guard on both sides.

**NO NEW GAP — the v86 iteration is PIN-ONLY.**

### F4 [PIN] — the savings goal-card's subtitle-P + header-row arithmetic + the wrapper's savings third-leg census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 289)

The never-pinned axes (the existing pins cover around them: the v51 F3
pin holds the savings subtitle's fs/color at 390 ONLY — never the lh,
never the box, never ANY 1280 state; the Rent-card subtitle test holds
the EXPENSES twin's {h, fs, lh, color} at 390 only; the v80 pin the
savings titleRow geometry + the card heights + the border/bg; the v74
pin the savings h4/amount/hiddenH1; the v58 F1 pin the grid/card/footer/
badge chrome; the v85 pin the expenses wrapper's pr-24 + the income
twin's paddingRight-0 — never the SAVINGS twin, the conditional's third
leg; grep-verified: no spec asserts a subtitle's lh anywhere, no spec
asserts the savings wrapper's paddingRight, no spec asserts the header
row's own geometry {display/justify/alignItems/h/mb} at any viewport):

- **The SUBTITLE P's full chrome at 1280** (item-card.tsx:131 — the
  `text-sm` P): {h 20, fs "14px", lh "20px", color
  "rgb(107, 114, 128)", mt "0px"} — the 1280 state of the v51 F3
  390-only family, byte-identical on both sides (the reference's
  Emergency Fund "Home Savings" vs the clone's Investments "Index
  Funds" — the TEXT the seed/user-data class, the CHROME the pin);
- **The with-subtitle ARITHMETIC at 1280**: the titleRow's mb "4px"
  (the mb-1 spacing between the dot+title row and the subtitle) + the
  HEADER ROW's own geometry {display "flex", justify
  "space-between", alignItems "flex-start", h 48, mb "12px"} — the
  48 = 24 titleRow + 4 mb-1 + 20 P twin of the 390 Rent-card family,
  never pinned at 1280;
- **The WRAPPER's savings THIRD LEG at 1280** (item-card.tsx:119 — the
  `cn("flex-1", item.type === "expense" && "pr-24")` column):
  {display "block", flexGrow "1", paddingRight "0px"} — completing the
  v85 conditional trilogy (expenses 96px / income 0px / savings 0px —
  the pr scoped to expenses ONLY, verified on all three types);
- the docSW 1280 guard.

Every pinned axis STATIC chrome (the subtitle conditional on the
non-empty subcategory — v71 F4; the typography lh-governed; the wrapper
conditional on the item type); the pin rides the plain authenticated
/savings view at 1280x800 on the e2e seed (the Investments card — the
v58/v74/v80 pins' own walk), no dialogs, no fixture writes.

**The pin-sanity mutation (the executed form — the viewport-scoped
responsive-variant dodge, the v80 pattern on the sibling row)**: the
header row's `items-start` → `items-start lg:items-center`
(item-card.tsx:118, applied by LINE NUMBER) — flips EXACTLY the pin's
headerRow.alignItems axis ("flex-start" → "center") and nothing else:
the responsive variant is inert at 390 (the Rent subtitle pin, the v51
F3 sub pin, the v54 F1 families all GREEN); at 1280 the centering
changes NO height (the row h stays max[48, 36] = 48 — the wrapper's
content stack untouched, the kebab merely centers) → every
height-governed pin (v80 [230,230], v79 income 230) GREEN; no other
spec asserts the header row's own alignItems — cascade-free by
construction (the full items.spec.ts run under the mutation: **38
green, only the v86 pin red**), then restored (the standalone REBUILD
as a SEPARATE command; `git diff src/` = 0 lines; the post-restore
full run 39/39 green).

**The two DISPROVEN mutation candidates (the design-probe lessons,
kept for the record)**: (1) the subtitle P's `text-sm` → `text-sm
lg:text-[15px]` (the naive fs-axis flip) — REFUTED by the **Tailwind
v4 RATIO-LINE-HEIGHT TRAP**: `text-sm` computes `line-height:
var(--tw-leading, var(--text-sm--line-height))` where
`--text-sm--line-height` is stored as the UNITLESS RATIO
calc(1.25 / 0.875) ≈ 1.42857 — any font-size override (even a pure
`lg:[font-size:15px]` arbitrary property) proportionally scales the
line-height (20px → 21.43px) and the P's box (20 → 21), cascading
into every height-governed pin (the v80 heights measured 254 under
the sibling candidate — the verified cascade); a font-size axis
CANNOT be isolated via Tailwind classes. (2) the type-scoped
conditional extension (`item.type === "expense"` → `item.type !==
"income"` — the v85 pattern, flipping the savings wrapper's
paddingRight 0→96) — REFUTED by the **NARROWED-CONTENT WRAP CASCADE**:
the pr-96 narrows the wrapper's content box to 137px, the seeded
Emergency Fund h4 (~125px at 16px/600) wraps to two lines (+24), and
the 1-row grid STRETCHES both cards to 254 — the v80 heights pin
cascades; the pr-narrowing family is only safe when every text stays
single-line at the narrowed width.

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → `npm run build` → **289 e2e** in chunks
(+1) → 35 smoke; the 16 standing screenshots regenerated + byte-
compared (the same-DB discipline; the seedcheck under
`env -u DATABASE_URL`). EXPECTED: the same-day seed + same-day shots
reproduce the committed set byte-for-byte (the v82 same-day-seed
byte-identity law — the committed set was shot 2026-10-18, the v86 seed
re-created the same calendar day); any DATE-class diff pixel-arbitrated
per the v66/v75/v80 discipline, never a full-page VLM verdict.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the subtitle P's full chrome + the titleRow mb + the headerRow's geometry + the wrapper's savings pr-0 third leg at 1280 | tests/e2e/items.spec.ts |
| 2 | sanity | the pin-sanity mutation (the EXECUTED form): the header row's `items-start` → `items-start lg:items-center` (item-card.tsx:118, by LINE NUMBER) → the pin FAILS at exactly the headerRow.alignItems axis ("flex-start" → "center"; the h/mb/display/justify + the subtitle + the wrapper axes stay green); the full items.spec.ts under the mutation: 38 green, only the v86 pin red; restored → GREEN (the standalone REBUILD as a SEPARATE command; the post-restore full run 39/39) | src/components/budget/item-card.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 289 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v86 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (288→289 + the v86 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v86 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 121 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.43 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v86 section (the new probes + the IDENTICAL-verdict + third-token-family lessons) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_206.md + the repo worklog Session 121 entry | docs/session_206.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the wrapper-arbit-v86.sh census's own
  measured values, byte-identical on both sides' savings views at
  1280x800: the wrapper `{display: "block", flexGrow: "1",
  paddingRight: "0px", w: 231, h: 48}`; the subtitle `{h: 20, fs:
  "14px", lh: "20px", color: "rgb(107, 114, 128)", mt: "0px"}` (the
  texts "Home Savings" vs "Index Funds" the data class); the titleRow
  mb "4px"; the headerRow `{display: "flex", justify: "space-between",
  alignItems: "flex-start", h: 48, mb: "12px"}`; the cardH (ref 200 vs
  clone 230) the v70b class; the docSW 1280.
- The source confirms the values: item-card.tsx:118 — `mb-3 flex
  items-start justify-between` (the header row); :119 —
  `cn("flex-1", item.type === "expense" && "pr-24")` (the wrapper —
  savings carries NO pr, the third leg); :120 — `mb-1 flex
  items-center gap-2` (the titleRow, its mb-1 = the 4px); :131 —
  `<p className="text-sm" style={{ color: rgb.gray }}>` (the subtitle
  P — text-sm = fs 14px + lh 20px; rgb.gray = rgb(107,114,128) per
  constants.ts).
- The pin-sanity target (the executed form): `items-start` → `items-start
  lg:items-center` flips ONLY the header row's alignItems at ≥1024px
  (inert at 390 — the v80 responsive-variant dodge pattern) —
  grep-verified: no spec asserts the header row's alignItems at any
  viewport; the row's height is max-governed (48 vs the kebab's 36) —
  the centering changes no height; the two DISPROVEN candidates (the
  fs-axis text-sm mutation [the v4 ratio-line-height trap] and the
  type-scoped conditional extension [the Emergency-Fund wrap cascade])
  documented above with their measured refutations.
- The existing pins are SAFE: the v51 F3 sub pin (390, fs+color) —
  disjoint viewport; the Rent subtitle test (390, expenses) — disjoint
  viewport + type; the v80 savings pin (heights + titleRow + border/bg)
  — the mutation's lh-preservation keeps the heights arithmetic
  intact; the v58 F1 savings pin (grid/card/footer/badge) —
  card-level surfaces; the v74 pin (h4/amount/hiddenH1) — other
  elements; the v85 pin (expenses wrapper + income pr-0 control) —
  the savings leg is the NEW third leg, disjoint from both.
- The blast radius: ZERO production-code change (every census delta a
  documented class — the pin-only line holds); the pin-sanity mutation
  touches `src/components/budget/item-card.tsx:131` (the subtitle P's
  className) REVERTED before ship (`git diff src/` = 0 lines at
  commit).
- The chain gate: lint → typecheck → 108 unit → `npm run build` →
  290+1 e2e chunk executions (**289 unique** after: +1 — the F4 pin)
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
  (the v73 lesson — the clone-side heredoc stays unquoted ONLY for the
  census-variable injection); the mutations need the standalone REBUILD
  as a SEPARATE command (the v53 lesson); the clean-check gate re-runs
  AFTER every new file lands (the v69 lesson); the build step is
  `npm run build` (the v76 F0 lesson); the screenshot DATE-class diffs
  after a fresh seed are pixel-arbitrated, never full-page
  VLM-verdicted (the v80 lesson); the sed derivation of the standing
  checks needs the bare-number session-name token family TOO
  (ref79/clone79 — the v84 lesson's third family, applied and
  diff-verified this session); a VLM IDENTICAL verdict still gets the
  census (the v75 convention — the census is the authority, the
  verdict is a signal).
- The deferred queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census, the line-items dialog
  glyphs.
- The v87 queue (suggestions): (1) the re-run cadence rotates to the
  next-oldest candidate after this pair (the v81-era LOGIN +
  CALCULATOR pair [the login view + the calculator dialog at desktop
  1280], last re-shot v81 — now the oldest remaining [v81 < v82 <
  v83 < v84 < v85 < v86]), (2) the axe-core watch at its next
  re-check point (only a 5.x wrapper changes the calculus), (3) the
  deferred reference-write censuses (unchanged).
