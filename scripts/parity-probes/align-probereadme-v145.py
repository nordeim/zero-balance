#!/usr/bin/env python3
"""D6 — the probe README alignment for the v145 cycle: insert the v145
section (Session 180) between the v145 queue's end and '## The v138 cycle'
(each cycle section ends with the NEXT cycle's queue — the v144 section's
tail IS the v145 queue; the new v145 section carries the v146 queue)."""
import io
import sys

PATH = "scripts/parity-probes/README.md"

SECTION = """## The v145 cycle (the v139-era ITEMS pair's FOURTEENTH re-run — Session 180)

The re-run cadence's third-pass oldest-remaining candidate: the v139-era
ITEMS pair — the ITEMS view [INCOME + EXPENSES] at desktop 1280x800
FULL-PAGE (the v57-era items pair's surface family), last re-shot v139
— now the oldest remaining [v139] — the FIRST entry of the third-pass
pool (the v133–v138 second-pass pool EXHAUSTED at v144); the pair's
FOURTEENTH re-run bracket [v57 -> v64 -> v70 -> v79 -> v85 -> v91 ->
v97 -> v103 -> v109 -> v115 -> v121 -> v127 -> v133 -> v139 -> v145];
the SIXTY-EIGHTH consecutive queue/ledger agreement — the surface
names verified against the v139 lineage's own records BEFORE the
derivation (the v139 plan's own header: the THIRTEENTH ordinal on its
14-entry bracket [v57 the original, one entry — 14 entries − the
original = 13 re-runs, no off-by-one this lineage]; the v139 shots
header carries the FULL bracket form, the verification source). **A
PIN-ONLY cycle for src/ — zero production-code changes + ONE TOOLING
REPAIR [scripts/align-seed-dates-v144.ts — the v144 cycle's own
committed script carrying a typecheck defect: the ExpenseLineItem
block referenced a nonexistent `date` field; caught by THIS cycle's
F0 baseline on its FIRST typecheck run and fixed to the model's real
`startDate`/`endDate` fields] + one e2e pin (347 -> 348)**; the
cycle's standing items: the axe watch (NO DRIFT — 4.14.0 holds, the
v68 dedupe verified), the npm-audit watch at its thirty-sixth
re-check (0 vulnerabilities --omit=dev — the v110 bump holds [next
16.4.3 + zod 4.6.7]; no new advisories in the watched ranges), the
139th standing checks (ALL GREEN — the reference's four bugs live;
the data census clean on the FIRST reads; the clone's mobile menu
VERIFIED WORKING the 139th consecutive time; zero overflow at 390 on
all five views; the seedcheck exact after the clone half).

The baseline carried THE TOOLING REPAIR then GREEN (the
SAME-PERSISTED workspace — the v144 environment held: node_modules
354 entries, BOTH chromium pairs [1200 + 1243], .env + db/ at the
repo root with the canonical Oct 31 seed stamps [the idempotent seed
re-run PRESERVED them, verified live: the items' date fields
2026-10-21..29 + the assets'/liabilities' lastUpdated 2026-10-31];
the seedcheck EXACT 7/1850/2235/0/3/2 before any gate — under the
env -u discipline, the sandbox DATABASE_URL pollution live as
documented): `npm run typecheck` FAILED on the FIRST run —
scripts/align-seed-dates-v144.ts(33): the ExpenseLineItem block
referenced a nonexistent `date` field [the model carries
`startDate`/`endDate`] — ROOT CAUSE: the v144 cycle committed that
script AFTER its typecheck gate had already run (the process-slip
class the F0 baseline exists to catch); FIXED: the block now shifts
the model's real `startDate`/`endDate` fields, each when present
(the seedcheck contract untouched — lineItems = 0 under the canonical
seed, the loop body never executes on the canonical state); then:
lint, typecheck, 108/108 unit, build [robots + sitemap prerendered],
the 4-chunk e2e [350 executions = 347 unique, ZERO flakes], 35/35
smoke; the production-seam audit clean; skills/ excluded).

The probe series derived from the v139 lineage (derive-v145-series.py
— the generic swaps incl. the FOUR explicit session-token families
[refvlm/clonevlm + refarbit/clonearbit] + the history-correction
fragments [the era marker last re-shot v133->v139 + the later-pairs
list v134..v138->v140..v144 + the ordinal THIRTEENTH->FOURTEENTH +
the bracket extended in all four files], all applied on the FIRST
run, zero residual, line counts preserved 57/49/50/285; bash -n +
node --check clean; the pre-derivation sweep re-confirmed the
standing finding — all era tokens confined to the file headers, the
clone file carrying zero) + the two-half builder (derive-build-
twohalf-v145.py — the session-token bump clonearbit139->clonearbit145
FIRST [the v121 stale-session-fix precedent] + the generic swap + the
lesson-range bump v92..v138->v92..v144 [the BARE range token] + the
lineage-note fixup "build-twohalf-v133.py"->"build-twohalf-v139.py"
LAST [the v110 swap-order rule]) + the comparator (derive-compare-
v145.py — the generic swap + the provenance citations re-pointed at
the v139 measurement [the v139-documented standing classes; the v145
census must reproduce the v139 values EXACTLY]) + the verify script
(derive-verify-twohalf-v145.py — the generic swap + the
lineage-citation chain extended v103/v109/v115/v121/v127/v133->+v139;
the digest itself UNCHANGED) + the 139th standing pair (derive-
standing-v145.py — derived from the v138 pair, three token families
[the ordinal 138th->139th th->th plain replace, the bare session
names ref138/clone138->ref139/clone139, the version v138->v139; the
citation extended with v144's 137th->138th], normalize-back diff
clean, zero old tokens, line counts preserved 119/74). The halves
built + the md5 contract verified by the direct THREE-WAY python
extraction (verify-twohalf-v145.py — CENSUS_JS 193 lines md5
b55dcd29, byte-identical across arbit-v145.sh + ref-arbit-v145.sh +
clone-arbit-v145.sh — **the documented v103/v109/v115/v121/v127/
v133/v139 lineage contract VERBATIM: the items census JS block
carries no version tokens, the digest cycle-invariant**).

The resource discipline applied between every half (the browser
daemons reaped BEFORE every half; both halves + both shot series
executed with first-attempt logins; the full logs captured by the
runner redirection — /tmp/vlm145/{ref,clone}-arbit.log, the
comparator's documented input paths).

The VLM pairwise run TWICE with full log capture
(/tmp/vlm145/vlm-pass{1,2}.log): pass 1 BOTH PAIRS DIFFERENT / pass 2
BOTH PAIRS DIFFERENT — **the consistent-verdict form, the pair's
DOCUMENTED VERDICT CLASS (the same verdict family as the v139 re-run
and the lineage's prior re-runs)**. Every flag DOM-arbitrated to a
documented class: the avatar letter (the USER-IDENTITY class — "D"
vs "U", both passes, both pairs); the grid layout/arrangement (the
SEED-COUNT class — census-verified: income grid childCount 1 vs 2 +
expenses 4 vs 3, the template columns byte-identical
309.328px-family); the header stats + the card names/amounts/dates/
badges (the SEED-DATA classes — each site's own data); the expense
footer payment-method chips (the v57 DATA-CONDITIONAL class — the
reference's expense items ship no payment methods, its footer
childCount 1 vs the clone's 2; the clone RENDERS the chip when its
data carries it); the badge wrap/stacking (the v57 wrap/
classification-VALUE classes — the expenses badgeRow h 22 vs 52 +
badgeCount 3 vs 4, the census-whitelisted clone's Recurring superset
chip + the wrap consequence). **NO FAB/platform-chrome claims in
EITHER pass this cycle** (the standing flag class absent from both
passes' output — no live disproof required; the v97..v144 standing
disproof form [base44-fab-arbit] remains available should any future
pass claim it).

The both-sides census compared axis-by-axis (compare-v145-census.py):
**187 axes — 163 identical + 24 documented-class deltas, ZERO new —
REPRODUCING the v139 census values EXACTLY** (the same 187/163/24
split, zero drift on every axis: the avatar chrome [36x36 / radius
9999px / 14px-600 / white / rgb(143,188,63) — the identity text the
sole delta], the grid + card chrome [the 3-col 309.328px family],
the titleRow, the amount leaf [text-2xl font-bold], the footer +
badge chrome, the filter card on BOTH variants [the search
spanning/not-spanning contract], the page-header family, the docSW
1280 guards). The seedcheck exact after the clone half
(7/1850/2235/0/3/2). NO NEW CLONE GAP on the census axes.

THE PIN — the ITEMS VIEW PAGE-HEADER ADD INCOME button's
FOCUS-VISIBLE LADDER at desktop 1280 on /income (PIN-ONLY for src/ —
zero production-code changes; +1 e2e = 348): the candidate survey
(the items-pair surfaces' interaction families swept against the
specs' own assertions — the SPEC-ALIAS lesson) found every family
HELD — the nav links' hover family (nav-geometry/tokens), the search
input's focus-visible + typing (the v37 S2 pin) + the savings search
input's own-hover (the v140 pin, the same-component family), the
filter-card Select triggers' own-hover ladders (THE v139 PIN — the
pair's own surface), the item-card badge hover (the v127 pin), the
card-hover reveal + the inert card shadow (the v45 F1b/v29 pins),
the page-header row + the Add buttons' AT-REST chrome (the v109 pin
— the income "Add Income" 147x36 lime->limeLight gradient + the
expenses "Add Expense" 155x36 orange gradient), the header Add
Income button's HOVER no-fade (the tokens v11 G4 pin,
tokens.spec.ts:546), the md-band state at 800 (the v115 pin), the
mobile censuses at 390 (the v52 pins) — **the income header Add
Income button's FOCUSED state held by NO spec at ANY viewport** (the
suite-wide survey: rg 'Add Income' across tests/e2e/*.spec.ts — 63
matches, ZERO focus/ladder matches; the v35 S2 focus pin the
DIFFERENT-ELEMENT dashboard header "Add Item" button at 1280, the
single-rung form; the dashboard.spec.ts:5321 pin the DIFFERENT-
ELEMENT dashboard quick-action "Add Income" CARD [the UA-default
ring family, NOT the composite]; the v144 pin the networth "Add
Asset" button at 390; the button a real BUTTON on BOTH sites — the
v109 cycle measured the reference's own header Add Income button
live at 1280). THE CONSTRUCT — the globals.css v11 G2c COMPOSITE:
the .zb-btn-add family (items-view.tsx:154 — the page-header button,
className="zb-btn-add shrink-0" with the inline lime->limeLight
gradient), the focused end-state outline 2px TRANSPARENT + offset
2px (v3's outline-none form) + the FOUR-layer box-shadow (the white
zero-spread lead + the shadcn 1px #0a0a0a ring + the gradient
family's two ambient layers) with the GRADIENT + opacity UNCHANGED
under focus (the v11 G4 no-hover-fade family: focus != hover). The
both-sides one-shot census addfocus-arbit-v145.sh (the v144 focusqa
form adapted to the items pair's own surface: the STRUCTURAL finder
[the v109 census's own finder family — main button, trimmed text
startsWith "Add", top < 200 — the page-header Add Income button],
the REAL Chromium focus({focusVisible:true}) engagement [the v35 S2
idiom], the (5,5)-parked pointer, READ-ONLY — focus() dispatches no
click, the button NEVER clicked [it opens the Add Item dialog, out
of bounds under the v46 rule], the scrollIntoView + the 300ms
settle, the blur restore) measured the ladder on BOTH sides **CLEAN,
NO GAP — the FOCUSED rung BYTE-IDENTICAL** (the at-rest rung:
{focused false, fv false, outlineStyle "none", outlineWidth "3px",
outlineOffset "0px", opacity "1", the gradient} — IDENTICAL both
sides, the at-rest boxShadow VISIBLE layers identical [the sole
delta the INVISIBLE lead-layer construct — REF the v3 four-slot form
with two zero-alpha leads vs CLONE the v11 G2a two-layer form, the
v66 class, never pinned]; the FOCUSED rung: {focused true, fv true,
outlineStyle "solid", outlineColor "rgba(0, 0, 0, 0)",
outlineWidth "2px", outlineOffset "2px" — the v3 outline-none form +
the FOUR-layer composite boxShadow BYTE-IDENTICAL both sides +
opacity "1" UNCHANGED + the gradient UNCHANGED — the focus != hover
family}; the BLURRED rung: the at-rest contract re-established on
every axis; the sole non-construct delta the at-rest outlineColor
computed form [REF rgba(10, 10, 10, 0.5) vs CLONE lab(2.74175 0
0.00000596046 / 0.5) — the v4 color computed-form family, never
pinned per the v95 discipline]). The pin appended (append-pin-
v145.py — the at-rest rung -> the FOCUSED rung {focused true + fv
true + outlineStyle "solid" + outlineColor "rgba(0, 0, 0, 0)" +
outlineWidth "2px" + outlineOffset "2px" — THE v3 outline-none form
+ the FOUR-layer composite, each layer asserted [the v35 S2
toContain form] + opacity "1" UNCHANGED + the gradient UNCHANGED —
the focus != hover family} -> the blurred rung (the at-rest contract
re-established); the V95/V66/V109-COLLISION-safe axis set [the
at-rest outlineColor computed form + the at-rest lead-layer count +
the v109-pinned shared at-rest axes deliberately NOT pinned]; the
ROLE finder [getByRole button name /^Add Income$/]; the button
NEVER clicked; GREEN on the first run; the authoritative --list:
348 in 24 files).

THE PIN-SANITY MUTATION — the COMPOSITE-REMOVAL form: the
.zb-btn-add:focus-visible block disabled in globals.css (the single
construct; the block serves EVERY zb-btn-add instance — the dialog
Save buttons, the dashboard header Add Item, the calculator Add
Item, the empty-state buttons, the networth Add Asset — the WIDER
blast radius NOTED: pins in OTHER files [dialog-buttons, dashboard's
v35 S2, calculator, empty-states, networth's v144] would also fail
if run; the sole-failure criterion verified on the FULL ITEMS SWEEP
ALONE) — **the exact CSS-cleanup drift class the pin exists to
guard** (the "consolidation" that kills the keyboard composite — an
a11y regression invisible to every at-rest census): the at-rest rung
UNCHANGED (the block is :focus-visible-scoped — every at-rest census
[v109, the session-5 gradient pins, the v11 G2a family] stays
GREEN), but the FOCUSED rung loses the composite (the outline falls
back to the UA-default ring family + the boxShadow loses the white
lead + the 1px #0a0a0a ring). **The SOLE FAILURE verified live — 1
failed [the pin alone] + 54 passed in the FULL items sweep**, the
failure diff EXACTLY the predicted focused-rung composite axes
(outlineStyle/outlineColor/outlineWidth/outlineOffset — the
focused/fv/opacity axes preserved); restored (git diff src/ = 0
lines) + the FULL REBUILD + the post-restore regression **55
passed** (the full items sweep — the v145 pin + all 54 prior items
pins' same-file immunity verified live).

The ship chain: **348 e2e zero flakes** (96+95+78+82 = 351
executions = 348 unique — the +1 landing in ch1 [items]; both closed
watches green through the chain); 35/35 smoke; the screenshots
**16/16 captured — 15/16 byte-identical + 1 the documented
WALL-CLOCK class** (07-add-item-modal.png — the dialog's todayIso()
date default crossed midnight [11/01/2026 -> 11/02/2026, VLM-
confirmed on the pixel-diff crop {the pixel-diff: 154 pixels, one
digit-wide bbox}; the same re-commit convention as v117/v122/v124/
v131/v133/v135/v136/v138; the same-seed law otherwise intact — the
canonical persisted-seed state [the Oct 31 stamps verified live:
the idempotent seed re-run preserved them]); the dev evidence 4/4
byte-identical + VLM-verified (the menu proof
{"url":"/income","docSW":390,"navLandmark":true}; the dev-shots
scripts derived v144 -> v145 with the version-swap-only verification
on both).

The v146 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence's next-oldest candidate —
**the v140-era SAVINGS pair** (the SAVINGS view at desktop 1280x800
FULL-PAGE [the v58-era savings pair's surface family], last re-shot
v140 — now the oldest remaining [v140]; the pair's FOURTEENTH re-run
bracket [v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98 -> v104 ->
v110 -> v116 -> v122 -> v128 -> v134 -> v140 -> v146] to be verified
against the v140 lineage's own records before the derivation — the
v140 plan's own header records the THIRTEENTH ordinal on its 14-entry
bracket [v58 the original, one entry — 14 entries − the original =
13 re-runs], consistent, no off-by-one this lineage; the v140 shots
header carries the FULL bracket form, the verification source), (2)
the axe-core watch at its next re-check point (only a 5.x wrapper
changes the calculus), (3) the npm-audit watch at its re-check point
(only a new advisory in the next/zod ranges changes the calculus),
(4) the deferred reference-write censuses (unchanged — out of bounds
under the v46 read-only rule), (5) the residual-class watch (both
flake classes CLOSED by the v136 dual-stack/localhost fix — the
watch continues in the standing form for any NEW class).

"""

text = io.open(PATH, encoding="utf-8").read()
if "## The v145 cycle" in text:
    print("SKIP: the v145 section already present")
    sys.exit(0)

anchor = "the standing form for any NEW class).\n\n## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)"
n = text.count(anchor)
if n != 1:
    print(f"FAIL: the insert anchor {n}x")
    sys.exit(1)

text = text.replace(anchor, "the standing form for any NEW class).\n\n" + SECTION + "## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)")
io.open(PATH, "w", encoding="utf-8").write(text)
print("OK: the v145 section + the v146 queue inserted (D6)")
