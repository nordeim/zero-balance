#!/usr/bin/env python3
"""D6 — the probe README alignment for the v144 cycle: insert the v144
section (Session 179) between the v144 queue's end and '## The v138 cycle'
(each cycle section ends with the NEXT cycle's queue — the v143 section's
tail IS the v144 queue; the new v144 section carries the v145 queue)."""
import io
import sys

PATH = "scripts/parity-probes/README.md"

SECTION = """## The v144 cycle (the v138-era MOBILE-TWINS pair's THIRTEENTH re-run — Session 179)

The re-run cadence's second-pass next-oldest candidate: the v138-era
MOBILE-TWINS pair — the /NETWORTH view + the DASHBOARD, both FULL-PAGE
at mobile 390x844 (the v62/v63-era twins' surface family), last
re-shot v138 — now the oldest remaining [v138] — the LAST entry of the
second-pass pool; the pair's THIRTEENTH re-run bracket [v62/v63 -> v69
-> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120 -> v126 ->
v132 -> v138 -> v144]; the SIXTY-SEVENTH consecutive queue/ledger
agreement — the surface names verified against the v138 lineage's own
records BEFORE the derivation (the v138 plan's own header: the TWELFTH
ordinal on its 13-entry bracket [v62/v63 the original pair, one entry —
13 entries − the original = 12 re-runs, no off-by-one this lineage];
the v138 shots header carries the FULL bracket form, the verification
source). **A PIN-ONLY cycle for src/ — zero production-code changes
(the fourteenth PIN-ONLY cycle in the last fifteen) + one e2e pin
(346 -> 347)**; the cycle's standing items: the axe watch (NO DRIFT —
4.14.0 holds, the v68 dedupe verified), the npm-audit watch at its
thirty-fifth re-check (0 vulnerabilities --omit=dev — the v110 bump
holds [next 16.4.3 + zod 4.6.7]; the 16 moderate the accepted dev-only
ESLint braces chain), the 138th standing checks (ALL GREEN — the
reference's four bugs live; the data census clean on the FIRST reads;
the clone's mobile menu VERIFIED WORKING the 138th consecutive time;
zero overflow at 390 on all five views; the seedcheck exact after the
clone half).

The baseline GREEN ON THE FIRST CHAIN after the environment repair
(the RESET workspace — the sandbox recycled at the session boundary:
node_modules, BOTH chromium pairs, .env and db/ all absent — rebuilt
live: npm install [494 packages, 354 node_modules entries], npx
playwright install chromium [the 1243 pair restored alongside the
persisted 1200 pair], cp .env.example .env [DATABASE_URL="file:../db/
custom.db"], db:push + db:seed [db/ recreated at the repo root],
db:generate; the seedcheck EXACT 7/1850/2235/0/3/2 before any gate —
under the env -u discipline, the sandbox DATABASE_URL pollution live
as documented; the first e2e chunk initially 94-failed on the missing
chromium_headless_shell-1243 — the environment repair, then GREEN; the
db's rendered dates re-aligned to the canonical persisted-seed state
[align-seed-dates-v144.ts — the fresh re-seed stamped Nov 1, the
canonical seed Oct 31; the displayed date fields shifted back one day,
the amounts untouched]: lint, typecheck, 108/108 unit, build [robots +
sitemap prerendered], the 4-chunk e2e [349 executions = 346 unique,
ZERO flakes], 35/35 smoke; the production-seam audit clean; skills/
excluded).

The probe series derived from the v138 lineage (derive-v144-series.py
— the generic swaps incl. the FOUR explicit session-token families
[refvlm/clonevlm + the LONG-FORM refarbit/clonearbit — the
mobile-twins lineage's own token form, the tokens carrying '138'
without the 'v' prefix] + the history-correction fragments [the era
marker last re-shot v132->v138 + the oldest-remaining list
[v132]->[v138] + the ordinal TWELFTH->THIRTEENTH + the bracket
extended in all three corrected files + the verdicts window
v108/v132->v108/v138 + the arbit census-axes provenance re-pointed at
the v138 measurement + the plan pointer the v137 plan's->the v143
plan's], all applied on the FIRST run, zero residual, line counts
preserved 60/47/68/219 == the v138 lineage exactly; bash -n + node
--check clean; the pre-derivation sweep re-confirmed the standing
finding — all era tokens confined to the file headers, the clone file
carrying zero) + the two-half builder (derive-build-twohalf-v144.py —
the session-token bump clonearbit138->clonearbit144 FIRST + the
generic swap + the lesson-range bump v92..v137->v92..v143 [the BARE
range token] + the lineage-note fixup "build-twohalf-v132.py"->
"build-twohalf-v138.py" LAST) + the comparator (derive-compare-v144.py
— the generic swap incl. the EXPLICIT /tmp/vlm138->/tmp/vlm144
log-path swap + the provenance citations re-pointed at the v138
measurement [the lineage ordinal TWELFTH->THIRTEENTH; the records
chain v132->v138]) + the verify script (derive-verify-twohalf-v144.py
— the generic swap + the lineage-citation extension "…v126/v132
lineage contracts"->"…v126/v132/v138 lineage contracts"; the digests
themselves UNCHANGED) + the 138th standing pair (derive-standing-
v144.py — derived from the v137 pair, three token families [the
ordinal 137th->138th th->th plain replace, the bare session names
ref137/clone137->ref138/clone138, the version v137->v138; the citation
extended with v143's 136th->137th], normalize-back diff clean, zero
old tokens, line counts preserved 119/74). The halves built + the md5
contract verified by the direct THREE-WAY python extraction
(verify-twohalf-v144.py — NW_CENSUS 42 lines md5 82cf8a43 +
DASH_CENSUS 87 lines md5 85e4ec7e, byte-identical across
arbit-v144.sh + ref-arbit-v144.sh + clone-arbit-v144.sh — **the
documented v102/v108/v114/v120/v126/v132/v138 lineage contracts
VERBATIM: the mobile-twins census JS blocks carry no version tokens,
the digests cycle-invariant**).

The resource discipline applied between every half (the browser
daemons reaped BEFORE every half; both halves + both shot series
executed with first-attempt logins; the full logs captured by the
runner redirection — /tmp/vlm144/{ref,clone}-arbit.log, the
comparator's documented input paths).

The VLM pairwise run TWICE with full log capture
(/tmp/vlm144/vlm-pass{1,2}.log): pass 1 BOTH PAIRS DIFFERENT / pass 2
BOTH PAIRS DIFFERENT — **the consistent-verdict form, the pair's
DOCUMENTED VERDICT CLASS (the v84/v90/v96/v102/v108/v114/v120/v126/
v132/v138 re-runs' own verdict family)**. Every flag DOM-arbitrated to
a documented class: the summary-card 2-col-vs-1-col layout + the
clipped "$25,000.0..." amount (the v41 MOBILE-SUPERSET class —
census-verified: docSW 464/390, statGrid.cols "175.828px
175.844px"/"294px", tiles 176/294, card 432x333/358x421,
medallion.clipsViewport true/false); the sub-header text wrapping (the
RANGE-WALK line-bucketing class — census-verified: the two line texts
bucket differently at the 5px width difference, the line TOPS 123/147
identical — no vertical shift); the progress-bar + donut proportions/
labels + every figure/count/name/date (the PCT/SEED-DATA classes —
each site's own data); the pass-2 trend-icon claim (the
PERCEPTION-ARTIFACT class — the census axes medallion 64x64 +
trendIcon 32x32 byte-identical both sides); the avatar (the
USER-IDENTITY data class); and the FAB claims (BOTH surfaces — the
networth + the dashboard — flagged in BOTH passes: the
PLATFORM-CHROME class, **DISPROVEN LIVE by base44-fab-arbit-v144.sh**
[the v142 two-surface standing form adapted to the pair's own 390
viewport]: fabCount 0 + bodyHasBase44 false on BOTH sides, BOTH
flagged surfaces, 390x844, logged-in — the standing v97/v103/v108/
v109/v115/v120/v123/v127/v129/v135/v141/v142/v143 disproof form
re-confirmed).

The both-sides census compared axis-by-axis (compare-v144-census.py):
**55 axes — 37 identical + 18 documented-class deltas, ZERO new —
REPRODUCING the v138 census values EXACTLY** (the same 55/37/18 split,
zero drift on every axis: the 18 documented = the v41 mobile-superset
NETWORTH family x10 [docSW 464/390, card.w 432/358, card.h 333/421,
card.right 448/374, statGrid.cols/w, tiles[0/1].w 176/294,
medallion.right 416/342, medallion.clipsViewport true/false] + the
DASH width-guard family x8 [docSW 395/390, subtitle.rect.w/blockW
363/358, the two Range-walk line texts, breakdownCard.rect.w 363/358,
children[0/1].w 313/308]). The seedcheck exact after the clone half
(7/1850/2235/0/3/2). NO NEW CLONE GAP on the census axes.

THE PIN — the NETWORTH ADD ASSET button's FOCUS-VISIBLE LADDER at
mobile 390 on /networth (PIN-ONLY — src/ ZERO changes, the fourteenth
PIN-ONLY cycle in the last fifteen; +1 e2e = 347): the candidate
survey (the twins' surfaces' interaction families swept against the
specs' own assertions — the SPEC-ALIAS lesson) found every family HELD
— the /networth twin's summary card + stat tiles + medallion + trend
icon (v41 F3, v63 F3, v96 F4), the tablist triggers (v53 F1 at-rest +
v30 G2 roving + v138 F4 the own-hover ladder — the last twins cycle's
own pin), the asset-card family (v46, v47 F2, the badge own-hover
v132 F4, the kebab ladders v124/v130/v136 at 1280), the liability-card
census (v120 F4), the page-header + junctions + ratio-footer (v69/
v102/v84), the section-header row + the Add Asset at-rest chrome at
1280 (v94 F4); the DASHBOARD twin's mobile censuses (v50, v49, v51,
v78, v126, v114, v62) + the interaction families pinned at 1280 (the
QA hover v125 + the QA focus-visible v143 — the last cycle's own pin;
the stat-card hover v131/v137; the drill-down rows v142) — **the
networth Add Asset button's FOCUSED state held by NO spec at ANY
viewport** (the suite-wide survey: rg 'Add Asset' across
tests/e2e/*.spec.ts — zero hover/focus/ladder matches; the v35 S2
focus pin the DIFFERENT-ELEMENT dashboard header Add Item button at
1280, the single-rung form; the button a real BUTTON on BOTH sites —
the v94 cycle measured the reference's own Add Asset button live).
THE CONSTRUCT — the globals.css v11 G2c COMPOSITE: the .zb-btn-add
family (net-worth-view.tsx:427 — the section-header button, the FIRST
in DOM order; the empty-state twin renders only when
assets.length === 0, NOT the case on either site), the focused
end-state outline 2px TRANSPARENT + offset 2px (v3's outline-none
form) + the FOUR-layer box-shadow (the white zero-spread lead + the
shadcn 1px #0a0a0a ring + the gradient family's two ambient layers)
with the GRADIENT + opacity UNCHANGED under focus (the v11 G4
no-hover-fade family: focus != hover). The both-sides one-shot census
addfocus-arbit-v144.sh (the v143 focusqa form adapted to the twins'
own surface: the STRUCTURAL finder [the button whose trimmed text
starts with "Add Asset" — the v94 census's own finder family], the
REAL Chromium focus({focusVisible:true}) engagement [the v35 S2
idiom], the (5,5)-parked pointer, READ-ONLY — focus() dispatches no
click, the button NEVER clicked [it opens the Add Asset dialog, out
of bounds under the v46 rule], the scrollIntoView + the 300ms settle,
the blur restore) measured the ladder on BOTH sides **CLEAN, NO GAP —
the FOCUSED rung BYTE-IDENTICAL** (the at-rest rung: {focused false,
fv false, outlineStyle "none", outlineWidth "3px", outlineOffset
"0px", opacity "1", the gradient} — IDENTICAL both sides, the at-rest
boxShadow VISIBLE layers identical [the sole delta the INVISIBLE
lead-layer construct — REF the v3 four-slot form with two zero-alpha
leads vs CLONE the v11 G2a two-layer form, the v66 class, never
pinned]; the FOCUSED rung: {focused true, fv true, outlineStyle
"solid", outlineColor "rgba(0, 0, 0, 0)", outlineWidth "2px",
outlineOffset "2px" — the v3 outline-none form + the FOUR-layer
composite boxShadow BYTE-IDENTICAL both sides + opacity "1" UNCHANGED
+ the gradient UNCHANGED — the focus != hover family}; the BLURRED
rung: the at-rest contract re-established on every axis; the sole
non-construct delta the at-rest outlineColor computed form [REF
rgba(10, 10, 10, 0.5) vs CLONE lab(2.74175 0 0.00000596046 / 0.5) —
the v4 color computed-form family, never pinned per the v95
discipline]). The pin appended (append-pin-v144.py — the at-rest rung
-> the FOCUSED rung {focused true + fv true + outlineStyle "solid" +
outlineColor "rgba(0, 0, 0, 0)" + outlineWidth "2px" + outlineOffset
"2px" — THE v3 outline-none form + the FOUR-layer composite, each
layer asserted [the v35 S2 toContain form] + opacity "1" UNCHANGED +
the gradient UNCHANGED — the focus != hover family} -> the blurred
rung (the at-rest contract re-established); the V95/V66-COLLISION-
safe axis set [the at-rest outlineColor computed form + the at-rest
lead-layer count deliberately NOT pinned]; the ROLE finder
[getByRole button name /^Add Asset$/]; the button NEVER clicked; GREEN
on the first run; the authoritative --list: 347 in 24 files).

THE PIN-SANITY MUTATION — the COMPOSITE-REMOVAL form: the
.zb-btn-add:focus-visible block disabled in globals.css (the single
construct; the block serves EVERY zb-btn-add instance — the dialog
Save buttons, the dashboard header Add Item, the calculator Add Item,
the empty-state buttons — the WIDER blast radius NOTED: pins in OTHER
files would also fail if run; the sole-failure criterion verified on
the FULL NETWORTH SWEEP ALONE) — **the exact CSS-cleanup drift class
the pin exists to guard** (the "consolidation" that kills the keyboard
composite — an a11y regression invisible to every at-rest census):
the at-rest rung UNCHANGED (the block is :focus-visible-scoped —
every at-rest census [v5, v94, the v11 G2a family] stays GREEN), but
the FOCUSED rung loses the composite (the outline falls back to the
UA-default ring family + the boxShadow loses the white lead + the
1px #0a0a0a ring). **The SOLE FAILURE verified live — 1 failed [the
pin alone] + 41 passed in the FULL networth sweep**, the failure diff
EXACTLY the predicted focused-rung composite axes (outlineStyle/
outlineColor/outlineWidth/outlineOffset — the focused/fv/opacity axes
preserved); restored (git diff src/ = 0 lines) + the FULL REBUILD +
the post-restore regression **42 passed** (the full networth sweep —
the v144 pin + all 41 prior networth pins' same-file immunity
verified live).

The ship chain: **347 e2e zero flakes** (95+95+78+82 = 350 executions
= 347 unique — the +1 landing in ch3 [networth]; both closed watches
green through the chain); 35/35 smoke; the screenshots **16/16
captured — ALL byte-identical** (the same-seed law: the db re-aligned
to the canonical persisted-seed state [align-seed-dates-v144.ts — the
fresh re-seed's Nov 1 stamps shifted back to the canonical Oct 31
state], every date-bearing surface rendering identically); the dev
evidence 4/4 byte-identical + VLM-verified (the menu proof
{"url":"/income","docSW":390,"navLandmark":true}; the dev-shots
scripts derived v143 -> v144 with the version-swap-only verification
on both).

The v145 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence's next-oldest candidate —
**the v139-era ITEMS pair** (the ITEMS view [INCOME + EXPENSES] at
desktop 1280x800 FULL-PAGE [the v57-era items pair's surface family],
last re-shot v139 — now the oldest remaining [v139]; the pair's
FOURTEENTH re-run bracket [v57 -> v64 -> v70 -> v79 -> v85 -> v91 ->
v97 -> v103 -> v109 -> v115 -> v121 -> v127 -> v133 -> v139 -> v145]
to be verified against the v139 lineage's own records before the
derivation — the v139 plan's own header records the THIRTEENTH
ordinal on its 14-entry bracket [v57 the original, one entry — 14
entries − the original = 13 re-runs], consistent, no off-by-one this
lineage; the v139 shots header carries the FULL bracket form, the
verification source), (2) the axe-core watch at its next re-check point
(only a 5.x wrapper changes the calculus), (3) the npm-audit watch at
its re-check point (only a new advisory in the next/zod ranges changes
the calculus), (4) the deferred reference-write censuses (unchanged —
out of bounds under the v46 read-only rule), (5) the residual-class
watch (both flake classes CLOSED by the v136 dual-stack/localhost fix —
the watch continues in the standing form for any NEW class).

"""

text = io.open(PATH, encoding="utf-8").read()
if "## The v144 cycle" in text:
    print("SKIP: the v144 section already present")
    sys.exit(0)

anchor = "the standing form for any NEW class).\n\n## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)"
n = text.count(anchor)
if n != 1:
    print(f"FAIL: the insert anchor {n}x")
    sys.exit(1)

text = text.replace(anchor, "the standing form for any NEW class).\n\n" + SECTION + "## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)")
io.open(PATH, "w", encoding="utf-8").write(text)
print("OK: the v144 section + the v145 queue inserted (D6)")
