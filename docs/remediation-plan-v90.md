# Remediation Plan v90 — the re-run cycle's next-oldest candidate (the v84-era mobile 390 twins' fourth re-run) + the axe watch + the stat-tile interior census pin (PIN-ONLY)

The formal narrative: `docs/session_216.md` (the v89 cycle's own narrative)
and `docs/session_217.md` (its transcript). The queue: the v89 plan's v90
suggestion — **the ledger-verified target** (the v89 docs' suggestion
AGREEING with the rotation ledger: the v84-era MOBILE 390 TWINS — the
/networth + the dashboard FULL-PAGE pair at 390x844 — last re-shot v84,
now the oldest remaining [v84 < v85 < v86 < v87 < v88 < v89]; the pair's
FOURTH re-run [v62/v63 → v69 → v78 → v84 → v90] — the THIRTEENTH
consecutive queue/ledger agreement), plus the axe-core watch at its
re-check point and the 84th standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 293.**

## The queue-correction note (the pre-execution ledger verification)

The v89-era docs' v90 queue phrasing — "the login + dashboard mobile
views, last re-shot v84" and "the twins' FIFTH re-run [v69 → v74 → v78 →
v84 → v90]" — carries TWO transcription errors, corrected here by
reading the v84 probe series itself (the ledger authority is the probe
lineage, not the prose):

1. **The SURFACE-NAME error**: the v84 cycle re-shot the **NETWORTH +
   the DASHBOARD** mobile 390 full-page twins — verified by reading
   `scripts/parity-probes/vlm-shots-v84.sh` ("(1) the /NETWORTH view …
   and (2) the DASHBOARD") and the v84 plan itself ("the mobile 390
   twins [the networth + dashboard FULL-PAGE pair at 390x844]"). The
   login mobile twin belongs to the v73 NEW-pair program (not in the
   re-run rotation).
2. **The RE-RUN-COUNT error**: v74 was the v58-era SAVINGS **desktop**
   pair's second re-run — not a mobile-twin shot. The twins' true
   history: **v62/v63 (original) → v69 (1st) → v78 (2nd) → v84 (3rd) →
   v90 (the FOURTH re-run)**.

The TARGET is unaffected: the v84-era mobile 390 twins, the oldest
remaining by last-re-shot date [v84 < v85 < v86 < v87 < v88 < v89].

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered) · **292 e2e ✓** (121 + 114 + 59 chunk executions
across three chunk splits of the 23 files = 294 total = 292 unique tests
[291 chromium + 1 setup, the setup re-run per chunk as the project
dependency] — the exact documented v89 state) · 35/35 smoke ✓. The
workspace REBUILT (the fresh-clone path, the v86/v88 precedent): `git
clone` at main @ 0f8bec4, the tree clean; the environment re-provisioned
(npm ci 354 packages; `.env` written [DATABASE_URL="file:../db/custom.db"],
`db/` at the repo root, db:generate + db:push + db:seed; chromium-1243
installed; the paramiko ssh shim deployed outside the repo at
/home/z/my-project/bin/ssh); the seedcheck exact (7 items / rent 1850 /
expenses 2235 / 0 line items / 3 assets / 2 liabilities) before any flow
ran, no orphaned servers.

The codebase audit clean: the v89 commit (f2040a3) re-verified PIN-ONLY
as documented (19 files, +1748/-4, ZERO src/ changes); the two commits
since session-log-only (session_216.md + session_217.md); the production
seams re-audited (auth scrypt/HMAC, the db-path contract, the SEO pair
[robots.ts + sitemap.ts — both prerendered by the build], the Tailwind v4
mitigations [`@variant hover (&:hover)` + the toast pointer-events fix +
the inline-rgba color discipline], the three test tiers); the repo's
skills/ folder excluded from checking/testing/compilation throughout
(eslint ignores + tsconfig exclude, verified live).

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next
prereleases beyond — no stable 4.14.1, no 5.x exists); npm-latest
`axe-core` 4.14.0; the lockfile holding the v68 dedupe state (the wrapper
4.14.0, no nested engine dir under `node_modules/@axe-core/playwright/`);
the engine-contract pin GREEN standalone (2 passed).

### F2 — the 84th standing checks: ALL GREEN (version-bumped from v83 — version-bump-only diffs verified)

ref-standing-v84.sh + standing-checks-v84.sh (version-bumped from v83 —
after normalizing the THREE token families [v83→v84, 83rd→84th, AND the
bare session names ref83→ref84/clone83→clone84] the files are
version-bump-only: verified by normalizing back and diffing clean, zero
old tokens remaining). Reference side: the four bugs ALL live
[toast-blocker `hitIsBurgerChild:false`; sheet-trap `overlayCount:1`;
no-landmark `navLandmark:false`; the 464px /networth overflow at 390];
the data census UNCHANGED (the 84th clean drift check: networth "1 items
· $25,000" / income "1 items · $5000.00" / expenses "4 items · $525.00");
the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation
menu VERIFIED WORKING (the **84th consecutive time**:
`hitIsBurgerChild:true`, the sheet opens, closes on nav, the nav landmark
present), zero overflow at 390 on all five views (docSW 390 everywhere),
the SEO pair live.

### F3 — the re-run pair (the v84-era mobile 390 twins: the /networth + the dashboard FULL-PAGE at 390x844 — the pair's FOURTH re-run)

The probe series derived from the v84 lineage (vlm-shots-v90.sh +
clone-vlmshots-v90.sh + vlm-compare-v90.mjs + arbit-v90.sh — the sed
derivation with the version + session-name + tmp-dir substitutions
[vlm84→vlm90, refarbit84→refarbit90, clonearbit84→clonearbit90,
ref84→ref90/clone84→clone90]; the headers history-corrected to the FOURTH
re-run [v62/v63 → v69 → v78 → v84 → v90]; the functional bodies verified
version-bump-only by the normalize-back diff — only the intentional
history-correction comment lines differ; login on the first attempt both
sides; the parked pointer at (5,5); read-only on the reference — the v46
rule holds).

**Both verdicts DIFFERENT, every flag DOM-arbitrated to a documented
class — the SAME flag-set classes as the v84 re-run itself:**

1. **PAIR 1 (NETWORTH at 390)**: the stat tiles side-by-side (ref) vs
   stacked (clone) — the **v41 mobile-superset class** (the clone's
   deliberate fix for the reference's 464px overflow; the census below
   confirms the tile chrome byte-identical, only the grid track differs);
   the trend-icon circle "larger and more opaque" — a VLM MISREAD (the
   medallion 64×64 + the trend icon 32×32 measured BYTE-IDENTICAL; the
   perception artifact rides the reference's medallion CLIPPING at its
   viewport edge [right 416 on a 390 viewport] vs the clone's fully
   visible one [right 342]); the tab-bar alignment — a VLM misread (the
   v53 tablist-390 pin holds the chrome byte-identical); the
   figures/ratio/groups — the seed-data classes; the "Edit with Base44"
   overlay — the platform-chrome class.
2. **PAIR 2 (DASHBOARD at 390)**: the subtitle wrap point (ref 3 lines
   perceived vs clone 2) — the **v62 width-delta class** (the reference's
   own 395px docSW overflow shifts its wrap by one word; the census
   confirms the subtitle chrome byte-identical and BOTH sides render 2
   DOM lines); the black tooltip over the breakdown rows — the Base44
   platform-chrome class; the progress-bar length + the donut
   proportions — the seed-data classes.

The both-sides census (arbit-v90.sh — the v75 convention: the census runs
regardless of the verdict) **REPRODUCES the v84 census values EXACTLY —
zero drift since v84 on every axis**:

- **NETWORTH**: the summary card {ref 432×333 on its 464 docSW vs clone
  358×421 on its fitting 390 — the v41 class}; the statGrid {cols ref
  "175.828px 175.844px" 2-col vs clone "294px" 1-col, the gap 16px
  IDENTICAL, 2 children both}; the tiles {ref 176×84 ×2 vs clone 294×84
  ×2 — the h 84 byte-identical, the w the v41 class}; the medallion
  {64×64 both, ref right 416 clipping vs clone right 342 visible — the
  v41 class}; the trendIcon {32×32 both, byte-identical}.
- **DASHBOARD**: the subtitle {fs 16px/fw 400/rgb(107,114,128)/lh 24px,
  the P h 48, the block h 92, 2 lines — BYTE-IDENTICAL; the wrap-point
  delta the v62 width-delta class}; the breakdown card {358×324 vs ref
  363×324 — the w the v62 page-width class, the h byte-identical};
  the svg family {svgCount 7, the [16,14,16,14] size family,
  rechartsWrappers 0, pieSectors 0 — BYTE-IDENTICAL}; the children {the
  H3 h 20 + the DIV h 238 byte-identical, the w the page-width class}.

**NO NEW CLONE GAP — the v90 iteration is PIN-ONLY.**

### F4 [PIN] — the stat-tile INTERIOR census at 390 (PIN-ONLY for src/ — no production-code change; +1 e2e = 293)

The never-pinned axes (the existing pins cover around them — the v41 F3
pin holds the card box/figure font/chip/gridCols at 390; the v63 F3 pin
the stat-tile BOX family {w/h/bg/blur/radius/pad} + the grid + the card
h 421 + the medallion svg at 390; the v84 F4 pin the ratio-footer family
at 390; the v60 F1 pin the tile box + the VALUE's fs/fw at 1280 [the
amtFw axis — the coverage the first mutation attempt caught, originally
missed by the `fw:`-token grep]; the v67 F3/v82 F4 pins the card's
geometry/typography at 1280; the LABEL family {fs/color/mb} and the
interior typography AT 390 are the never-pinned axes — the only
tile-interior-adjacent assertions elsewhere are the v46-era asset-card
value fs 24px [a different component] and the ratio-footer label family
[a different row]):

- **The two tiles' LABEL family at 390** (net-worth-view.tsx:370/375 —
  the `mb-1 text-xs` P with the inline color): per tile {tag "P",
  fs "12px", color "rgba(255, 255, 255, 0.7)", mb "4px", h 16};
- **The two tiles' VALUE family at 390** (net-worth-view.tsx:371/376 —
  the `text-2xl font-bold text-white` P): per tile {tag "P", fs "24px",
  fw "700", color "rgb(255, 255, 255)"};
- The tile box + grid re-affirm (the v63 F3 contract: the tile 294×84,
  the grid cols "294px") + the docSW 390 guard.

Every pinned axis is STATIC chrome (the tile interiors are unconditional
— no data, no viewport conditionals in the markup); the pin rides the
plain authenticated /networth view at 390 on the e2e seed (read-only —
no fixture writes), in tests/e2e/networth.spec.ts (the v41/v63/v84 pins'
own file), reusing the v63 F3 finder verbatim (the "Total Net Worth"
leaf → the rounded-2xl card → the "Total Assets" leaf → the grid
ancestor).

**The pin's own axes first measured byte-identical on both sides by the
supplemental census** (tile-interior-arbit-v90.sh — the v87/v88/v89
one-shot precedent, executed in the two-half controlled form): on BOTH
sides' /networth at 390x844, both tiles read {label: P/fs 12px/
rgba(255,255,255,0.7)/mb 4px/h 16; value: P/fs 24px/fw 700/
rgb(255,255,255)} — the ONLY deltas the tile width (ref 176 on its
overflowing 2-col vs clone 294 on its fitting 1-col — the v41 class)
and the docSW (464 vs 390 — the reference's own overflow bug).

**The pin-sanity mutation (the executed form — the viewport-scoped
responsive-variant dodge, the v80/v86/v87/v88/v89 pattern, CORRECTED
after the first attempt's cascade catch)**: the assets tile's value
`font-bold` → `font-bold max-lg:font-extrabold` (net-worth-view.tsx:371,
applied by LINE NUMBER — the line scoped to the ASSETS tile alone; the
liabilities twin [line 376], the card figure [line 348], and the ratio
value [line 392] untouched) — flips EXACTLY the pin's first tile's
value.fw axis at the pin's OWN viewport ("700" → "800" below 1024px,
where the pin runs at 390) and nothing else: the `max-lg:` variant is
INERT at ≥1024px — the v60 F1 pin's OWN amtFw axis (the tile value's fw
at 1280, line 1692-1695) stays green; font-weight never changes
line-height (the value P's line box stays text-2xl's 32px — the tile
h 84 arithmetic [16 pad + 16 label + 4 mb + 32 value + 16 pad]
unchanged, the v63 F3 tile-h/card-h pins green); font-weight never
affects color (the v41/v63/v84 chrome axes green); no other spec
asserts the tile value's fw below 1024px — **cascade-free BY
CONSTRUCTION** (the expected failure diff reads as the first tile's
value.fw axis alone; the label axes, the fs/color axes, the second
tile, the box/grid/docSW axes all green), then restored (the standalone
REBUILD as a SEPARATE command; `git diff src/` = 0 lines; the
post-restore full run green).

**THE FIRST-ATTEMPT CASCADE CATCH (the honest record, the lesson)**: the
first executed mutation form — the bare class swap `font-bold` →
`font-extrabold` — DID cascade: the full networth.spec.ts under it read
TWO red (the v90 pin AND the v60 F1 pin at 1280, failing at its
statTile.amtFw axis "700" → "800"). The root cause: the plan's original
grep verification searched for the `fw:` assertion token and MISSED the
v60 pin's `amtFw` shorthand — the tile value's fw was ALREADY pinned at
1280 all along. The catch is the mutation discipline working as
designed (the mutation is the coverage-map audit, not just the pin's
sensitivity check); the corrected form (the max-lg dodge) confines the
flip to below-lg where the v90 pin is the ONLY fw assertion, and the
plan's coverage map is corrected accordingly (the F4 coverage paragraph
and the pre-execution validation below).

**The disproven-in-advance candidates (documented without execution —
the design-probe analysis)**: (1) the label's fs mutation (text-xs →
text-sm) — REFUTED by the v86 RATIO-LINE-HEIGHT TRAP (the label's line
box 16→20 scales the tile h 84→88, cascading the v63 F3 tile-h and
card-h-421 pins); (2) the label's mb mutation (mb-1 → mb-1.5) — refuted
by the same height arithmetic (the tile h 84→86); (3) the value's fs
mutation (text-2xl → text-xl) — refuted by the same (the value line box
32→28, the tile h 84→80, the card h 421→413); (4) the docSW/gridCols
axes — page-level shared surfaces, never mutation targets.

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → `npm run build` → **293 e2e** in chunks
(+1) → 35 smoke; the 16 standing screenshots regenerated + byte-
compared (the same-DB discipline; the seedcheck under
`env -u DATABASE_URL`). EXPECTED: the seed planted and the shots taken
on the same calendar day reproduce the committed set byte-for-byte
(the v82/v88 same-day-seed byte-identity law); any DATE-class diff
pixel-arbitrated per the v66/v75/v80/v86 discipline, never a full-page
VLM verdict; any rasterization-noise class re-classified per pixel if
it recurs.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the stat-tile INTERIOR census at 390 (both tiles' label {tag/fs/color/mb/h} + value {tag/fs/fw/color} families + the tile box/grid re-affirm + the docSW guard), riding the plain authenticated /networth view | tests/e2e/networth.spec.ts |
| 2 | sanity | the pin-sanity mutation (the EXECUTED form): the assets tile's value `font-bold` → `font-bold max-lg:font-extrabold` (net-worth-view.tsx:371, by LINE NUMBER) → the pin FAILS at exactly the first tile's value.fw axis ("700" → "800" below 1024px; the label/fs/color/second-tile/box/grid/docSW axes stay green; the v60 F1 amtFw at 1280 stays green — the max-lg variant inert there); the full networth.spec.ts under the mutation: only the v90 pin red; restored → the standalone REBUILD → the post-restore full run green | src/components/budget/net-worth-view.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 293 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v90 paragraph (+ the queue-correction note) | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (292→293 + the v90 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v90 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 125 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.47 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v90 section (the new probes + the queue-correction lesson + the fresh-clone reprovisioning note) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_218.md + the repo worklog Session 125 entry | docs/session_218.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the tile-interior-arbit-v90.sh census's
  own measured values, byte-identical on both sides' /networth at
  390x844 (the supplemental census ran BEFORE this plan's execution —
  the values above are its verbatim output).
- The mutation target line verified by reading the source:
  net-worth-view.tsx:371 is the assets tile's value P
  (`text-2xl font-bold text-white`) — the ONLY font-bold on that line;
  the other font-bold text-white occurrences (lines 348 [the card
  figure, its fw pinned at 1280 by the v4-era structure test], 376 [the
  liabilities twin], 392 [the ratio value, its fw pinned at 1280]) are
  untouched by the line-number-scoped mutation.
- The grep verification (CORRECTED after the first-attempt cascade
  catch): the v60 F1 pin DOES assert the tile value's fw at 1280 — via
  the `amtFw` shorthand (networth.spec.ts:1692-1695), which the
  original `fw:`-token grep missed; no OTHER spec asserts the tile
  value's fw at any viewport (the tile assertions in the v63 F3 pin are
  the BOX axes: w/h/bg/blur/radius/pad; the only fs-24px value pin
  besides the v60/v90 pair is the v46-era ASSET-CARD value [a different
  component, a different view region]). The corrected mutation (the
  max-lg dodge) is inert at the v60 pin's 1280 viewport by construction.
- The rotation ledger verified: the mobile 390 twins last re-shot v84 =
  the oldest remaining [v84 < v85 < v86 < v87 < v88 < v89] — the v89
  plan's v90 suggestion agreeing with the ledger once the surface-name
  transcription error is corrected (the THIRTEENTH consecutive
  agreement).
- The pin's finder: the v63 F3 finder verbatim (the "Total Net Worth"
  leaf → the rounded-2xl card → the "Total Assets" leaf → the grid
  ancestor → the tile children's P pair) — proven stable across four
  prior pins.

## Operational lessons this cycle (the probe README's D6 section)

- THE QUEUE-PROSE VERIFICATION LESSON: the rotation ledger's authority
  is the PROBE LINEAGE (the shot scripts' own surface lists), never the
  prose queue phrasing — the v89-era docs' "login + dashboard" v90
  phrasing was a transcription error caught by reading vlm-shots-v84.sh
  before deriving the v90 series. Verify the surface names against the
  probe scripts before every derivation; correct the record in the plan.
- The fresh-clone reprovisioning checklist (the v86/v88 precedent,
  re-verified): npm ci → .env → db:generate/push/seed → chromium-1243 →
  the paramiko shim outside the repo → the seedcheck exact — the full
  chain then lands on the documented state with zero flakes on the
  first run.
