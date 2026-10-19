# Remediation Plan v93 — the re-run cycle's next-oldest candidate (the v87-era login + calculator pair's fifth re-run) + the axe watch + the totalCard inner-text census pin (PIN-ONLY)

The formal narrative: `docs/session_222.md` (the v92 cycle's own narrative
log; the raw continuation log `docs/session_223.md`). The queue: the v92
plan's v93 suggestion — **the ledger-verified target** (the v92-era docs'
suggestion AGREEING with the rotation ledger: the v87-era LOGIN +
CALCULATOR pair [the CALCULATOR dialog at desktop 1280x800, full-pair] —
last re-shot v87, the oldest remaining
[v87 < v88 < v89 < v90 < v91 < v92]; the pair's FIFTH re-run
[v59 → v66 → v75 → v81 → v87 → v93] — the SIXTEENTH consecutive
queue/ledger agreement), plus the axe-core watch at its re-check point
and the 87th standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 296.**

## The pre-execution ledger verification (the queue-prose verification lesson, applied)

The rotation ledger's authority is the PROBE LINEAGE, never the prose
queue phrasing. Verified against `scripts/parity-probes/vlm-shots-v87.sh`
before the derivation: its own header reads "a fresh standing sweep of
the CALCULATOR dialog at desktop 1280x800 — the re-run cycle's
next-oldest candidate (the v81-era LOGIN + CALCULATOR pair, last re-shot
v81 ...)" — the CALCULATOR dialog at desktop 1280x800 + the LOGIN view
(vlm-compare-v87.mjs's own pair list), matching the queue's phrasing
exactly this cycle (no transcription error to correct). The re-run
bracket verified against the same scripts' header ("the pair's FOURTH
re-run [v59 → v66 → v75 → v81 → v87]") — v93 is the FIFTH re-run. The
standing-checks pair (ref-standing-v87.sh + standing-checks-v87.sh)
derived from v86 across the three token families (v86→v87, 86th→87th,
ref86→ref87/clone86→clone87), version-bump-only verified by normalizing
back and diffing clean (zero old tokens remaining).

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered) · **295 e2e ✓** (105 + 112 + 80 chunk executions
across three chunk splits of the 23 files = 297 total = 295 unique tests
[294 chromium + 1 setup, the setup re-run per chunk as the project
dependency] — the exact documented v92 state, zero flakes on the first
run) · 35/35 smoke ✓. The workspace: the SAME environment provisioned
for the v92 cycle earlier this calendar day (npm ci 354 packages at the
identical lockfile — unchanged through the two commits since; `.env`
[DATABASE_URL="file:../db/custom.db"], `db/` at the repo root, the
e2e.db scratch, chromium-1243, the paramiko ssh shim outside the repo at
/home/z/my-project/bin/ssh), pulled to main @ 926f193 (the docs-only
session-log commit — ZERO src/ deltas since the v92 push 6567512); the
seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items
/ 3 assets / 2 liabilities) before any flow ran, no orphaned servers.

The codebase audit clean: the v92 commit (6567512) verified PIN-ONLY as
documented (34 files, +2476/−6, ZERO src/ changes); the one commit since
(926f193) session-log-only (docs/session_223.md — the skills/ folder
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

### F2 — the 87th standing checks: ALL GREEN (version-bumped from v86 — version-bump-only diffs verified)

ref-standing-v87.sh + standing-checks-v87.sh (version-bumped from v86 —
after normalizing the THREE token families [v86→v87, 86th→87th, AND the
bare session names ref86→ref87/clone86→clone87] the files are
version-bump-only: verified by normalizing back and diffing clean, zero
old tokens remaining). Reference side: the four bugs ALL live
[toast-blocker `hitIsBurgerChild:false`; sheet-trap `overlayCount:1`
after nav; no-landmark `navLandmark:false`; the 464px /networth overflow
at 390]; the data census UNCHANGED (the 87th clean drift check: networth
"1 items · $25,000" / income "1 items · $5000.00" / expenses "4 items ·
$525.00"); the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile
navigation menu VERIFIED WORKING (the **87th consecutive time**:
`hitIsBurgerChild:true`, the sheet opens, closes on nav, the nav
landmark present), zero overflow at 390 on all five views (docSW 390
everywhere), the SEO pair live.

### F3 — the re-run pair (the v87-era login + calculator pair: the login view + the calculator dialog at desktop 1280x800 — the pair's FIFTH re-run)

The probe series derived from the v87 lineage (vlm-shots-v93.sh +
login-shots-v93.sh + clone-vlmshots-v93.sh + clone-login-shots-v93.sh +
vlm-compare-v93.mjs + arbit-v93.sh — the sed derivation with the version
+ session-name + tmp-dir substitutions [vlm87→vlm93, login87→login93,
calc87→calc93, v87→v93; the shots' session names refvlm87→refvlm93/
clonevlm87→clonevlm93/reflogin87→reflogin93/clonelogin87→clonelogin93
riding the families]; the headers history-corrected to the FIFTH re-run
[v59 → v66 → v75 → v81 → v87 → v93] + "last re-shot v87" + the
oldest-remaining bracket [v87 < v88 < v89 < v90 < v91 < v92] + the
queue agreement ordinal TENTH → SIXTEENTH + the suggesting plan v86 →
v92; the functional bodies verified version-bump-only by the
normalize-back diff — only the intentional history-correction comment
lines differ; the residual "87" tokens all legitimate history
references [the v87-era lineage, the FIFTH re-run bracket, the v87
close-button pin reference]; login on the first attempt both sides; the
parked pointer at (5,5); read-only on the reference — the v46 rule
holds). **The v89/v92 reaping lesson applied mid-cycle**: the clone-side
shots' first run hit the chromium resource-exhaustion symptom class
(70 zombie processes observed; the EMPTY-eval symptom, no error
surface) — `pkill -f agent-browser` + the session-file sweep +
a reaping step budgeted BETWEEN the reference and clone halves of every
long probe from then on; all clone-side runs clean after the reaping.

**The LOGIN pair: VERDICT IDENTICAL, zero style flags** (matching the
v75/v81/v87 re-runs' own IDENTICAL verdicts — zero drift since v75 on
the VLM layer; the VLM's note-free report covering the card geometry,
logo, fonts, colors, input chrome, button chrome, spacing, shadows).
The both-sides census byte-identical on every axis: the card
448/0px-pad/16px/rgba(255,255,255,0.95); the h1 30px/700/lh 36px/
rgb(15,23,42); the subtitle 16px/rgb(100,116,139); the logo 96×96; the
inputs 48/12px/14px/1px rgb(226,232,240); the Sign in
368×48/12px/14px/500/rgb(15,23,42); the Google + OR blocks both
present; the docSW 1280 guard. The card's 0px-width border
computed-color (ref slate-200 form vs the clone's border token) and the
shadow's transparent lead-layer count are the v66 computed-form
INVISIBLE class — both surfaces render identically.

**The CALCULATOR pair: VERDICT DIFFERENT with flags, every one
DOM-arbitrated to a documented class — the SAME flag-set classes as the
v75/v81/v87 re-runs (zero drift in the mechanism classes):**

1. the "extra will-update line" + its derived "Total Calculated card
   height" note — the v66 DATA-CONDITIONAL class (`hasWillUpdateSpan`
   ref FALSE [its Rent natively $25.00 === its line-item total] vs
   clone TRUE [opened-at $1850 ≠ the recalculated $25.00]; the
   totalCard box itself measures 720×90 BYTE-IDENTICAL on both sides);
2. the "hover action buttons missing in the clone" — the v75/v81/v87
   POINTER-POSITION perception class (the reference's shot taken with
   the pointer still inside the dialog after the Calculate click, the
   clone's after the parked-pointer move — the DOM census:
   `actionsAtRest {opacity: 0, btnCount: 2}` BYTE-IDENTICAL on both
   sides);
3. the data figures — the seed-data classes (the reference's Rent
   $25.00 seed vs the clone's Rent $1850 dev seed; both dialogs carry
   ONE "Contents Insurance" $25.00 monthly-active row for the pair).

No FAB flag this cycle (the reference's platform iframe chrome outside
the queryable DOM — the v85/v91-documented class, absent from this
verdict's flag set).

The both-sides census — **executed in the TWO-HALF CONTROLLED FORM,
BUILT TWO-HALF FROM THE START** (ref-arbit-v93.sh + clone-arbit-v93.sh,
built by build-twohalf-v93.py with the TWO census JS blocks
[CALC_CENSUS_JS 61 lines + LOGIN_CENSUS_JS 36 lines] extracted once and
embedded byte-identically across the halves — the identity verified by
the md5 line-block diff [e1092d12 / 9e5a52d2]) — **REPRODUCES the v87
census values EXACTLY — zero drift since v87 on every axis:**

- **The LOGIN census BYTE-IDENTICAL** (the card
  448/0px/16px/rgba(255,255,255,0.95) with the shadow's
  transparent-lead-layer count the v66 computed-form INVISIBLE class;
  the h1 30px/700/36px/rgb(15,23,42); the subtitle 16px/
  rgb(100,116,139); the logo 96×96; the inputs 48/12px/14px/1px
  rgb(226,232,240); the Sign in 368×48/12px/14px/500/rgb(15,23,42);
  the Google + OR blocks both present; the docSW 1280 guard).
- **The CALCULATOR census BYTE-IDENTICAL** (the panel 768×393/16px/
  white/maxW 768px with the shadow's transparent-lead-layer count the
  v66 computed-form class [the visible layer
  rgba(0,0,0,0.25) 0px 25px 50px −12px byte-identical]; the scrim
  rgba(26,58,46,0.5)/blur(8px)/1280×800; the title
  18px/700/lh 28px/rgb(26,58,46); the desc 14px/lh 20px/
  rgb(107,114,128); the totalCard 720×90/16px/12px/1px solid
  rgb(252,221,213); the nameH4 16/600/h 24/mb 4px; the row
  720×102/16px/12px/1px solid rgb(229,231,227); the pillRow
  flex/8px/12px/h 20; the pill1 20/65/2px 8px/9999px/12px/400; the
  amountP 20px/700/rgb(224,122,59)/h 28; the addBtn
  110×32/radius 6px/12px/500/white); the hasWillUpdateSpan (ref FALSE
  vs clone TRUE) the v66 DATA-CONDITIONAL class; the docSW 1280 guard.
- **The CLOSE button census axis**: absent on the reference side (the
  reference's calculator close button LOST its accessible name — the
  v87-documented reference-side observation; the finder's aria-label/
  ×-text clause misses it) while the clone's close census reads
  {36×36/6px/transparent/0px} — the v87 pin's own values; the clone is
  the SUPERSET (the accessible name retained).

**NO NEW CLONE GAP — the v93 iteration is PIN-ONLY.**

### F4 [PIN] — the totalCard inner-text census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 296)

The never-pinned axes (the existing pins cover around them — the v59 F1
pin holds the totalCard BOX chrome {720×90/pad/radius/border} at 1280;
the v66 F3 pin the row/name/pill/amount HEIGHT family at 1280; the v73
F4 pin the summary-text family {amount/basedOn/willUpdate} at 390 ONLY;
the v81 pin the title/desc/addBtn/scrim at 1280; the v87 pin the close
button's chrome at 1280; the v2-era G-test the amount's COLOR at the
default viewport; **the totalCard's inner-text family is never pinned
at 1280 — the v73 390 family's desktop twin — and the "Total
Calculated" LABEL leaf's chrome {fs/fw/lh/color} is never pinned at ANY
viewport** (only toBeVisible elsewhere; the labelFinder/locator filters
never read its computed styles):

- **The "Total Calculated" LABEL leaf's typography at 1280**: {fs
  "14px", fw "500", lh "20px", color "rgb(107, 114, 128)"} —
  never pinned at ANY viewport (the genuinely-new axis);
- **The summary AMOUNT leaf's typography at 1280** (the v73 390
  family's desktop twin): {fs "24px", fw "700", lh "32px", color
  "rgb(224, 122, 59)"};
- **The "Based on 1 item" leaf at 1280** (the v73 family's desktop
  twin): {fs "12px", lh "16px", color "rgb(107, 114, 128)"};
- **The will-update span at 1280** (the v73 family's desktop twin; the
  data-conditional span present in the pin's fixture state): {fs
  "12px", fw "400", color "rgb(234, 88, 12)"};
- **The two summary ROWS' chrome at 1280** (never pinned at any
  viewport): the top row {display "flex", justify "space-between",
  align "center", mb "8px"} + the bottom row {display "flex", justify
  "space-between", fs "12px", color "rgb(107, 114, 128)"};
- **The totalCard box chrome re-affirm** {w 720, h 90, pad "16px",
  radius "12px", border "1px solid rgb(252, 221, 213)"} (the v59
  contract at the pin's own viewport);
- The docSW 1280 guard.

Every pinned axis is STATIC chrome (the label/amount/basedOn/rows'
classes are unconditional — text-sm/font-medium/text-2xl/font-bold/
text-xs carry no responsive prefixes; the will-update span's EXISTENCE
is the only data-conditional, its classes unconditional); the pin rides
the calculator dialog at 1280×800 in the 1-row fixture state (the
v45/v66/v73 discipline — Add Item "Contents Insurance" $25 through the
real UI on the e2e scratch db; the global setup re-seeds per run, no
manual restore needed), in tests/e2e/calculator.spec.ts (the
v45/v49/v53/v59/v66/v73/v81/v87 pins' own file), reusing the census's
own leaf finders verbatim (the totalCard bg rgb(255,247,245) finder →
the leaf() text matchers).

**The pin's own axes first measured byte-identical on both sides by the
supplemental census** (totalcard-arbit-v93.sh + totalcard-clone-v93.sh
— the v87/v88/v89/v90/v91/v92 one-shot precedent, BUILT two-half from
the start; the census JS verified byte-identical across the halves by
the md5 line-block diff [49aa5547]): on BOTH sides' calculator dialog
at 1280×800 with the paired 1-row state (the reference's NATIVE
"Contents Insurance" $25 row — read-only on the reference; the clone's
added-then-fully-restored twin — the seedcheck exact after the run),
the label reads {14px/500/20px/rgb(107,114,128)}, the amount reads
{24px/700/32px/rgb(224,122,59)}, the basedOn reads {12px/16px/
rgb(107,114,128)}, the topRow reads {flex/space-between/center/8px},
the bottomRow reads {flex/space-between/12px/rgb(107,114,128)}, the
totalCard reads {720×90/16px/12px/1px solid rgb(252,221,213)}, and the
docSW reads 1280 — ZERO deltas on any axis (the willUpdate span the
documented v66 DATA-CONDITIONAL class: absent on the reference [its
Rent natively $25.00 === its line-item total], present on the clone at
{12px/400/rgb(234,88,12)} — matching the v73 390 pin's own values, the
family viewport-independent).

**The pin-sanity mutation (the executed form — the viewport-scoped
responsive-variant dodge, the v80/v86/v87/v88/v89/v90/v91/v92 pattern,
scoped AT-lg this cycle because the pin runs at 1280)**: the label's
`text-sm font-medium` → `text-sm font-medium lg:font-semibold`
(calculator-dialog.tsx:153, applied by LINE NUMBER — the "Total
Calculated" label span's own className, the one instance in the file)
— flips EXACTLY the pin's label.fw axis at the pin's OWN viewport
("500" → "600" at ≥1024px, where the pin runs at 1280) and nothing
else: the `lg:` variant is INERT below 1024px (every 390/640 pin green
by construction — the v73 390 family's own axes untouched); the label
is an INLINE SPAN inside the justify-between topRow (the row's height
driven by the amount's text-2xl lh 32px — the label's lh 20px bound
unchanged by a font-weight flip; the totalCard box 720×90, the rows'
chrome, the amount/basedOn/willUpdate axes, and the docSW all
unchanged); the label's fs/lh/color axes green (only the weight class
flips); **no spec asserts the "Total Calculated" label's computed
styles at ANY viewport** — the coverage-map grep run across ALL specs:
the label's only assertions elsewhere are the locator filters +
toBeVisible checks (calculator.spec.ts:43/46/793/806/1324,
calculator-error.spec.ts:54 — text-matching, green under a weight
flip); the dashboard's label assertions (dashboard.spec.ts:790-826)
are the DONUT's category labels — different elements entirely;
`lg:font-semibold` appears NOWHERE in src/ (no pre-existing variant to
collide with); no unit test asserts the component's classNames —
**cascade-free BY CONSTRUCTION** (the expected failure diff reads as
the label.fw axis alone; the fs/lh/color axes, the amount/basedOn/
willUpdate families, the rows' chrome, the totalCard box, and the
docSW guard all green), then restored (the standalone REBUILD as a
SEPARATE command — the FULL `npm run build`, never a bare `next
build`; `git diff src/` = 0 lines; the post-restore full run green).

**The disproven-in-advance candidates (documented without execution —
the design-probe analysis)**: (1) the amount's fw mutation — viable
single-axis BUT the label is the genuinely-never-pinned family member
(the amount's color already held at the default viewport by the v2-era
G-test, its full family at 390 by v73 — the family-rotation precedent
prefers the never-pinned axis); (2) the bottomRow's fs mutation
(text-xs → lg:text-sm) — flips the bottomRow.fs + basedOn.fs +
willUpdate.fs axes TOGETHER (the row carries the fs — a three-axis
failure diff); (3) the label's fs mutation (text-sm → lg:text-base) —
the v86 ratio-line-height trap (fs 14→16 scales lh 20→24, a two-axis
failure); (4) the label's color mutation — the inline `style={{ color:
rgb.gray }}` token is the app's global gray family (the v81 pin holds
desc.color, the v93 pin holds basedOn/bottomRow.color — a multi-pin
cascade); (5) the topRow's mb mutation (mb-2 → lg:mb-4) — flips
topRow.mb AND the totalCard h (the box grows — the v59/v66 pins hold
the h; a cross-pin cascade); (6) the addBtn/title/desc/scrim/close
axes — all v81/v87-pinned (a direct cross-pin cascade); (7) the
amount's color — the inline COLORS.orangeDark token shared with the
row's amountP.color (the v66 pin — a cascade). The `lg:font-semibold`
dodge on the label is the ONLY single-axis, cascade-free,
coverage-verified flip on the pin's own surface.

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → `npm run build` → **296 e2e** in chunks
(+1) → 35 smoke; the 16 standing screenshots regenerated + byte-
compared (the same-DB discipline; the seedcheck under
`env -u DATABASE_URL`). EXPECTED: the seed planted and the shots taken
on the same calendar day reproduce the committed set byte-for-byte
(the v82/v88/v90/v91 same-day-seed byte-identity law — the v92 cycle's
own 9/16 byte-identical + 7/16 DATE-TEXT/noise-arbitrated precedent on
the cross-day re-seed); any DATE-class diff pixel-arbitrated per the
v66/v75/v80/v86/v92 discipline, never a full-page VLM verdict; any
rasterization-noise class re-classified per pixel if it recurs.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the totalCard inner-text census at 1280 (the label's typography {fs/fw/lh/color} + the amount family {fs/fw/lh/color} + the basedOn {fs/lh/color} + the willUpdate {fs/fw/color} + the two rows' chrome + the totalCard box re-affirm + the docSW guard), riding the 1-row fixture state (Add Item "Contents Insurance" $25) | tests/e2e/calculator.spec.ts |
| 2 | sanity | the pin-sanity mutation (the EXECUTED form): the label's `text-sm font-medium` → `text-sm font-medium lg:font-semibold` (calculator-dialog.tsx:153, by LINE NUMBER) → the pin FAILS at exactly the label.fw axis ("500" → "600" at ≥1024px; the fs/lh/color axes, the amount/basedOn/willUpdate families, the rows' chrome, the totalCard box, and the docSW guard stay green; every below-1024 pin green — the lg variant inert there); the full calculator.spec.ts under the mutation: only the v93 pin red; restored → the standalone REBUILD → the post-restore full run green | src/components/budget/calculator-dialog.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 296 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v93 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (295→296 + the v93 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v93 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 128 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.50 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v93 section (the new probes + the reaping-budget-between-halves lesson + the v94 queue) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_224.md + the repo worklog Session 128 entry | docs/session_224.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the totalcard census's own measured
  values, byte-identical on both sides' calculator dialog at 1280×800
  with the paired 1-row state (the supplemental census ran BEFORE this
  plan's execution — the values above are its verbatim output; the
  census JS verified byte-identical across the two halves by the md5
  line-block diff [49aa5547]).
- The mutation target line verified by reading the source:
  calculator-dialog.tsx:153 is the label span's own className
  (`className="text-sm font-medium"` — the "Total Calculated" label,
  the ONE instance of the class pair in the file); the amount span
  (line 156), the bottomRow (line 162), and the will-update span (line
  167) carry their own classNames, untouched by the line-number-scoped
  mutation.
- The grep verification (run across ALL specs, BOTH the computed-style
  assertions AND the locator/text families): NO spec asserts the
  "Total Calculated" label's computed styles at any viewport; the only
  label assertions elsewhere are the locator filters + toBeVisible
  checks (green under a weight flip); the v73 pin holds the
  amount/basedOn/willUpdate families at 390 ONLY (the lg: variant inert
  below 1024px — green by construction); the dashboard's label
  assertions are the donut's category labels (different elements).
- The rotation ledger verified: the login + calculator pair last
  re-shot v87 = the oldest remaining [v87 < v88 < v89 < v90 < v91 <
  v92] — the v92-era docs' v93 suggestion agreeing with the ledger (the
  SIXTEENTH consecutive agreement), the surface names verified against
  vlm-shots-v87.sh's own header before the derivation.
- The pin's finder: the census's own finder verbatim (the totalCard
  bg rgb(255,247,245) finder + the leaf() text matchers) — proven
  stable across the v59/v66/v73/v87/v93 censuses.

## Operational lessons this cycle (the probe README's D6 section)

- THE REAPING BUDGET, BETWEEN THE HALVES, FROM THE START: the
  clone-side shots' first run hit the chromium resource-exhaustion
  symptom (70 zombie processes; the EMPTY-eval signature) — the fix
  (`pkill -f agent-browser` + the session-file sweep) is now budgeted
  as a STANDING STEP between the reference and clone halves of EVERY
  long probe, not just the recovery; the two-half census forms and the
  supplemental one-shots are all built two-half from the start (the
  v92 lesson holding, applied one step earlier).
- THE SESSION-LOG-ONLY COMMIT CLASS: the pulled 926f193 (docs/
  session_223.md, docs-only) requires ZERO re-provisioning — the npm ci
  state, the db, the chromium, and the shim all carry over when the
  delta touches no src/ or lockfile path; the baseline chain re-run on
  the carried-over environment IS the shipped-state verification (the
  tree clean at the pulled HEAD).
- THE LABEL-FIRST FAMILY EXTENSION: when a pin family extends to a new
  viewport (the v73 390 → v93 1280 twin), the mutation axis should
  target the family member never pinned at ANY viewport (the label) —
  the viewport-twin axes (amount/basedOn/willUpdate) are held by the
  390 pin whose lg:-scoped inertness keeps it green, but the label's
  never-pinned-anywhere status makes its flip the cleanest
  single-axis proof that the NEW pin bites.
