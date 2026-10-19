# Remediation Plan v94 — the re-run cycle's next-oldest candidate (the v88-era networth + drill-down pair's fifth re-run) + the axe watch + the networth section-header row census pin (PIN-ONLY)

The formal narrative: `docs/session_224.md` (the v93 cycle's own narrative
log; the raw continuation log `docs/session_225.md`). The queue: the v93
plan's v94 suggestion — **the ledger-verified target** (the v93-era docs'
suggestion AGREEING with the rotation ledger: the v88-era NETWORTH +
DRILL-DOWN pair [the NETWORTH view + the DASHBOARD's drill-down EXPANDED
state, both desktop 1280x800 full-page] — last re-shot v88, the oldest
remaining [v88 < v89 < v90 < v91 < v92 < v93]; the pair's FIFTH re-run
[v60 → v67 → v76 → v82 → v88 → v94] — the SEVENTEENTH consecutive
queue/ledger agreement), plus the axe-core watch at its re-check point
and the 88th standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 297.**

## The pre-execution ledger verification (the queue-prose verification lesson, applied)

The rotation ledger's authority is the PROBE LINEAGE, never the prose
queue phrasing. Verified against `scripts/parity-probes/vlm-shots-v88.sh`
before the derivation: its own header reads "a fresh re-run of the
v60-era pair (… the oldest remaining standing pair … the v60-era pair
last re-shot v82 …): the desktop 1280x800 FULL-PAGE state of (1) the
NETWORTH view and (2) the DASHBOARD's drill-down EXPANDED state. The
pair's FOURTH re-run [v60 → v67 → v76 → v82 → v88]" — the NETWORTH view
+ the DASHBOARD's drill-down EXPANDED state at desktop 1280x800,
matching the queue's phrasing exactly this cycle (no transcription
error to correct). The re-run bracket verified against the same
scripts' header — v94 is the FIFTH re-run. The standing-checks pair
(ref-standing-v88.sh + standing-checks-v88.sh) derived from v87 across
the three token families (v87→v88, 87th→88th, ref87→ref88/
clone87→clone88), version-bump-only verified by normalizing back and
diffing clean (zero old tokens remaining).

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered) · **296 e2e ✓** (111 + 105 + 82 chunk executions
across three chunk splits of the 23 files = 298 total = 296 unique tests
[295 chromium + 1 setup, the setup re-run per chunk as the project
dependency] — the exact documented v93 state, zero flakes on the first
run) · 35/35 smoke ✓. The workspace: the SAME environment provisioned
for the v93 cycle earlier this calendar day (npm ci 355 packages at the
identical lockfile — unchanged through the two commits since; `.env`
[DATABASE_URL="file:../db/custom.db"], `db/` at the repo root, the
e2e.db scratch, chromium-1243, the paramiko ssh shim outside the repo at
/home/z/my-project/bin/ssh), pulled to main @ 13e1445 (the docs-only
session-log commit — ZERO src/ deltas since the v93 push 1a2ecb5); the
seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items
/ 3 assets / 2 liabilities) before any flow ran, no orphaned servers.

The codebase audit clean: the v93 commit (1a2ecb5) verified PIN-ONLY as
documented (23 files, +2568/−6, ZERO src/ changes); the one commit since
(13e1445) session-log-only (docs/session_225.md — the skills/ folder
excluded from checking/testing/compilation throughout, verified live by
the eslint ignores + the tsconfig exclude); the production seams
re-audited (auth scrypt/HMAC, the db-path contract, the SEO pair
[robots.ts + sitemap.ts — both prerendered by the build], the Tailwind v4
mitigations [`@variant hover (&:hover)` + the toast pointer-events fix +
the space-y v3-semantics restore + the inline-rgba color discipline],
the three test tiers).

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 sha prereleases
beyond — no stable 4.14.1, no 5.x exists); the installed wrapper 4.14.0
+ the engine 4.14.0; the lockfile holding the v68 dedupe state (no
nested engine dir under node_modules/@axe-core/playwright/); the
engine-contract pin GREEN standalone (2 passed).

### F2 — the 88th standing checks: ALL GREEN (version-bumped from v87 — version-bump-only diffs verified)

ref-standing-v88.sh + standing-checks-v88.sh (version-bumped from v87 —
after normalizing the THREE token families [v87→v88, 87th→88th, AND the
bare session names ref87→ref88/clone87→clone88] the files are
version-bump-only: verified by normalizing back and diffing clean, zero
old tokens remaining). Reference side: the four bugs ALL live
[toast-blocker `hitIsBurgerChild:false`; sheet-trap `overlayCount:1`
after nav; no-landmark `navLandmark:false`; the 464px /networth overflow
at 390]; the data census UNCHANGED (the 88th clean drift check: networth
"1 items · $25,000" / income "1 items · $5000.00" / expenses "4 items ·
$525.00"); the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile
navigation menu VERIFIED WORKING (the **88th consecutive time**:
`hitIsBurgerChild:true`, the sheet opens, closes on nav, the nav
landmark present), zero overflow at 390 on all five views (docSW 390
everywhere), the SEO pair live.

### F3 — the re-run pair (the v88-era networth + drill-down pair: the networth view + the dashboard drill-down EXPANDED at desktop 1280x800 — the pair's FIFTH re-run)

The probe series derived from the v88 lineage (vlm-shots-v94.sh +
clone-vlmshots-v94.sh + vlm-compare-v94.mjs + arbit-v94.sh — the sed
derivation with the version + session-name + tmp-dir substitutions
[vlm88→vlm94, v88→v94, FOURTH→FIFTH, ELEVENTH→SEVENTEENTH; the shots'
session names refvlm88→refvlm94/clonevlm88→clonevlm94 riding the
families; the arbit session names refar88→refar94/clonear88→clonear94
corrected by the explicit second sed pass — the v94 derivation's own
small addition]; the headers history-corrected to the FIFTH re-run
[v60 → v67 → v76 → v82 → v88 → v94] + "last re-shot v88" + the
oldest-remaining bracket [v88 < v89 < v90 < v91 < v92 < v93] + the
queue agreement ordinal ELEVENTH → SEVENTEENTH + the
v88-era-pair-not-v60-era correction; the functional bodies verified
version-bump-only by the normalize-back diff — only the intentional
history-correction comment lines differ; the residual "88" tokens all
legitimate history references [the v88-era lineage, the FIFTH re-run
bracket]; login on the first attempt both sides; the parked pointer at
(5,5); read-only on the reference — the v46 rule holds). **The reaping
budget applied BETWEEN the halves from the start** (the v93 lesson as a
standing step: the pre-run reap + the between-halves reap on every
probe; zero resource-exhaustion symptoms this cycle — 70-zombie-class
absent throughout).

**The NETWORTH pair: VERDICT DIFFERENT with flags, every one
DOM-arbitrated to a documented class — the same mechanism classes as
the v82/v88 re-runs (zero drift in the mechanism classes):**

1. the avatar "U" vs "P" — the user-identity class (the reference's
   account initial vs the clone's demo account; the census axis
   `avatarLetter` measuring exactly the documented values);
2. the "Edit with Base44" FAB — the platform-chrome class, RE-ARBITRATED
   LIVE (base44-fab-arbit-v91.sh re-run: `fabCount 0 + bodyHasBase44
   false` on BOTH sides — the FAB lives in the reference's platform
   iframe chrome, outside the queryable DOM — the v85/v91-documented
   class);
3. the data figures (the net-worth totals, the 1-asset vs 3-asset
   groups, the ∞:1 vs 0.21:1 ratio) — the seed-data classes.

**The DRILL-DOWN pair: VERDICT DIFFERENT with flags, every one
DOM-arbitrated to a documented class — the same mechanism classes as
the v82/v88 re-runs:**

1. the "Dashboard link highlighted in the clone" — the v56 SUPERSET
   class (the reference's link INERT rgb(63,63,70)/400 vs the clone's
   ACTIVE white/500 — the superset fix #3, pinned by the mobile
   navigation spec family);
2. the avatar — the user-identity class (as above);
3. the "progress bar significantly longer in the clone" — the pct × 568
   DATA class (fillW ref 173 vs clone 357 on the byte-identical 568×12
   track — **the v82/v88 arbitration's own values REPRODUCED EXACTLY,
   six re-runs later** — the census-arithmetic reproduction lesson's
   standing case);
4. the "donut percentage labels absent in the ref" — the v60 PERCEPTION
   class re-arbitrated live by the census (the reference DOES render its
   labels: count 4 [1 group + 3 labels], labelLineCount 0, 16px, black,
   3 sectors — the chrome byte-identical, the texts each site's own data
   [92.3%/4.6%/3.1% vs 81.6%/13.8%/4.6%]);
5. the "'Total Expense' vs 'Total Expenses'" — the v82 VLM MISREAD
   class, re-arbitrated live (the stat-divider-arbit-v88.sh both-sides
   census re-run: the reference's statTitles measured VERBATIM "Total
   Income"/"Total Savings"/"Total Expenses" [plural, on every card] —
   the titles BYTE-IDENTICAL to the clone's own plural family);
6. the "divider lines present in the clone but missing in the ref" —
   the v88 VLM MISREAD class, re-arbitrated live (the same one-shot
   census: the divider {DIV, h 1, bg rgb(229,231,227), flexGrow 1} on
   EVERY card on BOTH sides — byte-identical; the width 177-vs-170 the
   flex-1 data-conditional remainder [the "1 item" vs "2 items" text
   width]; the count row h 20/w 254/flex/gap 8px/center/14px/
   rgb(10,10,10) with rowChildTags [SPAN, DIV, svg] byte-identical);
7. the expanded-content + counts + proportions + legend deltas — the
   seed-data classes (the clone's 2 income categories vs the reference's
   1, the donut proportions, the stat values).

The both-sides census — **executed in the TWO-HALF CONTROLLED FORM,
BUILT TWO-HALF FROM THE START** (ref-arbit-v94.sh + clone-arbit-v94.sh,
built by build-twohalf-v94.py with the TWO census JS blocks [ARBIT_A 90
lines + ARBIT_B 111 lines] extracted once and embedded byte-identically
across the halves — the identity verified by the md5 line-block
contract [a9cdcc96 / baa22974]) — **REPRODUCES the v88 census values
EXACTLY — zero drift since v88 on every axis:**

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
  length "$25,000.00" vs "-$245,950.00"; the heights byte-identical);
  the docSW 1280 guard.

**NO NEW CLONE GAP — the v94 iteration is PIN-ONLY.**

### F4 [PIN] — the networth view's section-header row census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 297)

The never-pinned axes (the existing pins cover around them — the v60 F1
pin holds the summary card + the tablist + the type-group header + the
card grid at 1280; the v67 F3 pin the summary-card HEIGHT family at
1280; the v82 F4 pin the completion family at 1280; the v84 F4 pin the
ratio footer at 390; the v90 F4 pin the stat-tile interior at 390; the
v69 F3 pin the PAGE-header row at 390 [the chip + the h1 "Net Worth" +
the subtitle — a DIFFERENT row from the section header]; the v46 F2 pin
the asset CARD family at 1280; the tokens.spec G2/G3 pins the Add
buttons' 16px Plus icon + the bare-shadow ambient at the DEFAULT
viewport; the networth.spec:166 test the group-header TEXT + the
forestMedium COLOR at the default viewport): **the SECTION-HEADER row
family — the tab panel's "Assets" header row — is never pinned at ANY
viewport** (only text-visibility assertions elsewhere: the h2 "Assets"
`getByRole("heading", level: 2)` toBeVisible; the count "3 items ·
$65,300" toBeVisible; the a11y spec's "Assets" references are the TAB
role, not the h2):

- **The section header ROW's chrome at 1280**: {display "flex",
  alignItems "center", justifyContent "space-between", h 56, w 960} —
  never pinned at any viewport (the row's own flex contract);
- **The "Assets" h2's typography at 1280**: {fs "24px", fw "700", lh
  "32px", color "rgb(26, 58, 46)", mb "0px", h 32} — never pinned at
  ANY viewport (the genuinely-new family member: the text-2xl
  font-bold + forestDark inline triple);
- **The count subtitle P's typography at 1280**: {fs "16px", fw "400",
  lh "24px", color "rgb(107, 114, 128)"} — never pinned at any viewport
  (the bare P with the inline gray);
- **The left block's height** {h 56} (the h2 lh 32 + the countP lh 24 —
  the block-governed arithmetic; the block's WIDTH excluded — the
  countText length's DATA-CONDITIONAL width class, the v82 labelBlock
  convention);
- **The Add Asset button's chrome ON THIS ROW at 1280**: {h 36, w 134,
  pad "8px 16px", radius "6px", fs "14px", fw "500", color
  "rgb(255, 255, 255)", bg the 135deg forest→lime gradient} + the Plus
  icon {16×16} — the zb-btn-add family's GEOMETRY never census'd on
  this row (the tokens.spec G3 pin holds the icon + the shadow at the
  default viewport; the networth.spec:219 test the backgroundImage
  string at the default viewport; the full chrome on the section row at
  the pair viewport unpinned until v94);
- **The row → first-group rhythm**: the rendered gap delta 24 (the
  space-y-6 rhythm; the group wrapper's margin-TOP form excluded — the
  v3-vs-v4 space-y margin-attribution class, the rendered geometry the
  parity contract);
- **The first type-group header's re-affirm at 1280**: {fs "18px", fw
  "600", lh "28px", mb "12px"} (the v60 F1 pin's own family, the
  position-adjacent member re-asserted inside the row's rhythm
  context);
- The docSW 1280 guard.

Every pinned axis is STATIC chrome (the row's flex classes, the h2's
text-2xl font-bold, the countP's bare P + inline gray, the button's
zb-btn-add family, the space-y-6 rhythm — all unconditional, no
responsive prefixes); the pin rides the plain authenticated /networth
view on the e2e seed (3 assets → "3 items · $65,300" — read-only, no
fixture writes, no tab interactions needed — the Assets tab is the
default panel), in tests/e2e/networth.spec.ts (the v60/v67/v82/v84/v90
pins' own file), reusing the census's own finders verbatim (the h2
text-match finder → the parent block → the row; the Add Asset
text-match button finder; the nextElementSibling group wrapper).

**The pin's own axes first measured byte-identical on both sides by the
supplemental census** (nwsection-arbit-v94.sh + nwsection-clone-v94.sh
— the v87/v88/v89/v90/v91/v92/v93 one-shot precedent, BUILT two-half
from the start; the census JS verified byte-identical across the halves
by the md5 line-block diff [f8b3cabf]): on BOTH sides' /networth view
at 1280×800 (the reference's populated Assets panel "1 items ·
$25,000" — read-only on the reference; the clone's seeded panel "3
items · $65,300" — read-only, the seedcheck exact after the run), the
row reads {flex/center/space-between/56/960}, the h2 reads
{24px/700/32px/rgb(26,58,46)/mb 0/h 32}, the countP reads
{16px/400/24px/rgb(107,114,128)}, the block reads {h 56} (the w 141
byte-identical this seed but EXCLUDED as the data-coupled width
class), the addBtn reads {36/134/8px 16px/6px/14px/500/white/the
forest→lime gradient}, the addBtnIcon reads {16×16}, the groupGap
delta reads 24 (the mt form 24-vs-0 the v3/v4 margin-attribution
computed class — the RENDERED gap the parity contract), the groupH3
reads {18px/600/28px/mb 12px}, and the docSW reads 1280 — ZERO deltas
on any pinned axis.

**The pin-sanity mutation (the executed form — the viewport-scoped
responsive-variant dodge, the v80..v93 pattern, scoped AT-lg this
cycle because the pin runs at 1280)**: the h2's `text-2xl font-bold` →
`text-2xl font-bold lg:font-black` (net-worth-view.tsx:418, applied by
LINE NUMBER — the "Assets" section h2's own className, the ONE
instance at that line; the file's OTHER text-2xl font-bold instances
[lines 107/212/348/371/378/482] untouched by the line-scoping) —
flips EXACTLY the pin's h2.fw axis at the pin's OWN viewport ("700" →
"900" at ≥1024px, where the pin runs at 1280) and nothing else: the
`lg:` variant is INERT below 1024px (every 390/640 pin green by
construction); the h2's lh 32px is bound by text-2xl's line-height
(font-weight does not scale line-height — the h2's h 32 and the
block's h 56 unchanged); the row's h 56, the countP family, the
addBtn family, the groupGap delta, the groupH3 family, and the docSW
all unchanged; **no spec asserts the "Assets" section h2's computed
styles at ANY viewport** — the coverage-map grep run across ALL specs:
the h2's only assertions elsewhere are the getByRole("heading",
{ name: "Assets", level: 2 }) toBeVisible (networth.spec.ts:168) and
the a11y spec's TAB-role "Assets" references (a11y.spec.ts:85/148/240
— the Tabs trigger, a different element) — text-matching, green under
a weight flip; `lg:font-black` appears NOWHERE in src/ (no
pre-existing variant to collide with); no unit test asserts the
component's classNames — **cascade-free BY CONSTRUCTION** (the
expected failure diff reads as the h2.fw axis alone; the fs/lh/color/
mb/h axes, the row family, the countP family, the addBtn family, the
rhythm, and the docSW guard all green), then restored (the standalone
REBUILD as a SEPARATE command — the FULL `npm run build`, never a bare
`next build`; `git diff src/` = 0 lines; the post-restore full run
green).

**The disproven-in-advance candidates (documented without execution —
the design-probe analysis)**: (1) the h2's fs mutation (text-2xl →
lg:text-3xl) — the v86/v93 ratio-line-height trap (fs 24→30 scales lh
32→40, a two-axis failure diff); (2) the countP's color mutation —
the inline `style={{ color: rgb.gray }}` token is the app's global
gray family (the countP has NO className — the class-flip mutation
form does not apply; a style-value mutation is not the executed form);
(3) the row's justify mutation (justify-between → lg:justify-around)
— flips row.justify AND the addBtn's x-position (geometry-coupled
two-axis); (4) the addBtn's fs/radius/pad mutations — the zb-btn-add
CSS class family shared across EVERY view's Add buttons (the
tokens.spec G2/G3 pins + the items.spec v11 pins cascade); (5) the
addBtn's bg mutation — the ADD_BUTTON_GRADIENTS.asset constant shared
with the empty-state button (networth.spec:219's own gradient
assertion cascades); (6) the groupH3's fw — the v60 F1 pin's own
axis (a direct cross-pin cascade); (7) the groupGap's rhythm — the
TabsContent's space-y-6 wrapper class shared with the liabilities
panel (the v60 pin's tablist-context assertions ride the same
wrapper). The `lg:font-black` dodge on the h2 is the ONLY single-axis,
cascade-free, coverage-verified flip on the pin's own surface.

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → `npm run build` → **297 e2e** in chunks
(+1) → 35 smoke; the 16 standing screenshots regenerated + byte-
compared (the same-DB discipline; the seedcheck under
`env -u DATABASE_URL`). EXPECTED: the seed planted and the shots taken
on the same calendar day reproduce the committed set byte-for-byte
(the v82/v88/v90/v91/v93 same-day-seed byte-identity law — the v93
cycle's own 16/16 byte-identical precedent); any DATE-class diff
pixel-arbitrated per the v66/v75/v80/v86/v92 discipline, never a
full-page VLM verdict; any rasterization-noise class re-classified per
pixel if it recurs.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the networth section-header row census at 1280 (the row's flex chrome {display/align/justify/h/w} + the h2 "Assets" typography {fs/fw/lh/color/mb/h} + the countP typography {fs/fw/lh/color} + the block h 56 + the addBtn chrome {h/w/pad/radius/fs/fw/color/bg} + the addBtnIcon {16×16} + the groupGap delta 24 + the groupH3 re-affirm {fs/fw/lh/mb} + the docSW guard), riding the plain authenticated /networth view on the e2e seed (read-only) | tests/e2e/networth.spec.ts |
| 2 | sanity | the pin-sanity mutation (the EXECUTED form): the h2's `text-2xl font-bold` → `text-2xl font-bold lg:font-black` (net-worth-view.tsx:418, by LINE NUMBER) → the pin FAILS at exactly the h2.fw axis ("700" → "900" at ≥1024px; the fs/lh/color/mb/h axes, the row family, the countP family, the addBtn family, the rhythm, and the docSW guard stay green; every below-1024 pin green — the lg variant inert there); the full networth.spec.ts under the mutation: only the v94 pin red; restored → the standalone REBUILD → the post-restore full run green | src/components/budget/net-worth-view.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 297 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v94 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (296→297 + the v94 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v94 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 129 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.51 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v94 section (the new probes + the v95 queue) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_226.md + the repo worklog Session 129 entry | docs/session_226.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the nwsection census's own measured
  values, byte-identical on both sides' /networth view at 1280×800 (the
  supplemental census ran BEFORE this plan's execution — the values
  above are its verbatim output; the census JS verified byte-identical
  across the two halves by the md5 line-block diff [f8b3cabf]).
- The mutation target line verified by reading the source:
  net-worth-view.tsx:418 is the "Assets" section h2's own className
  (`className="text-2xl font-bold"` — the one instance at that line);
  the count P (line 421), the Add Asset buttons (lines 432/457), and
  the liabilities h2 (line 482) carry their own classNames, untouched
  by the line-number-scoped mutation.
- The grep verification (run across ALL specs, BOTH the computed-style
  assertions AND the locator/text families): NO spec asserts the
  "Assets" section h2's computed styles at any viewport; the only h2
  assertions elsewhere are the getByRole heading toBeVisible
  (networth.spec.ts:168) and the a11y spec's TAB-role references
  (a11y.spec.ts:85/148/240 — the Tabs trigger, a different element);
  `lg:font-black` appears nowhere in src/.
- The rotation ledger verified: the networth + drill-down pair last
  re-shot v88 = the oldest remaining [v88 < v89 < v90 < v91 < v92 <
  v93] — the v93-era docs' v94 suggestion agreeing with the ledger (the
  SEVENTEENTH consecutive agreement), the surface names verified
  against vlm-shots-v88.sh's own header before the derivation.
- The pin's finder: the census's own finder verbatim (the h2 text-match
  finder → the parent block → the row; the Add Asset text-match button
  finder; the nextElementSibling group wrapper) — proven stable across
  the v60/v67/v82/v84/v90/v94 censuses.

## Operational lessons this cycle (the probe README's D6 section)

- THE REAPING BUDGET AS A STANDING STEP, APPLIED CLEAN: the v93
  lesson (the between-halves reap budgeted from the start) applied as
  a pre-run + between-halves step on EVERY probe this cycle — zero
  resource-exhaustion symptoms throughout (the 70-zombie class absent;
  the self-matching pkill caution respected via the `agent[-]browser`
  character-class form).
- THE SECOND-PASS SESSION-NAME SED: the arbit lineage's session names
  (refar88/clonear88) ride the "ar" token family, NOT the "v88" family
  — the first sed pass missed them; the explicit second pass
  (refar88→refar94/clonear88→clonear94) corrected the derivation
  before any execution. Future derivations: sweep for residual old
  tokens by SESSION-NAME pattern, not just the version family.
- THE MISREAD-CLASS LIVE RE-ARBITRATION: when a re-run cycle's VLM
  verdict re-flags a documented MISREAD class (the v82 stat-title, the
  v88 divider), the existing one-shot census is RE-RUN live rather
  than re-derived — the disproven-in-advance form (the flag's class
  already documented, the re-run the fresh evidence).
