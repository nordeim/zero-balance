#!/usr/bin/env python3
"""D6 — the probe README alignment for the v153 cycle: insert the v153
section (Session 188) between the v153 queue's end and '## The v138 cycle'
(each cycle section ends with the NEXT cycle's queue — the v152 section's
tail IS the v153 queue; the new v153 section carries the v154 queue)."""
import io
import sys

PATH = "scripts/parity-probes/README.md"

SECTION = """## The v153 cycle (the v147-era LOGIN + CALCULATOR pair's FIFTEENTH re-run — Session 188)

The re-run cadence's third-pass next-oldest candidate: the v147-era
LOGIN + CALCULATOR pair — the LOGIN view + the CALCULATOR dialog at
desktop 1280x800 (the v59-era pair's surface family), last re-shot
v147 — now the oldest remaining [v147 < v148 < v149 < v150 < v151 <
v152]; the pair's FIFTEENTH re-run bracket [v59 -> v66 -> v75 -> v81
-> v87 -> v93 -> v99 -> v105 -> v111 -> v117 -> v123 -> v129 -> v135
-> v141 -> v147 -> v153]; the SEVENTY-SIXTH consecutive queue/ledger
agreement — the surface names verified against the v147 lineage's own
records BEFORE the derivation (the v147 plan's own header: the
FOURTEENTH ordinal on its 15-entry bracket [v59 the original, one
entry — 15 entries − the original = 14 re-runs, no off-by-one this
lineage]; the v147 shots header carries the FULL bracket form, the
verification source). **A PIN-ONLY cycle — src/ ZERO production-code
changes + one e2e pin (356 -> 357): the CALCULATOR DIALOG "Add Item"
BUTTON's FOCUS-VISIBLE LADDER at 1280 — the never-pinned keyboard path
of the pinned Add-button family's DIALOG INSTANCE (the family's focus
ladders closed on EVERY page-header sibling [v35 S2 dashboard @1280 ->
v144 networth @390 -> v145 income @1280 -> v146 savings @1280 ->
v150 networth-liability @390 -> v151 expenses @1280]; the v81 census
holds this button's at-rest chrome only; the v129 own-hover pin's
finder EXPLICITLY EXCLUDES it; the v135 focus pin is the dialog X only
— the sibling-completion form, the v149/v150/v151/v152 precedent)**;
the cycle's standing items: the axe watch (NO DRIFT — 4.14.0 holds,
the v68 dedupe verified), the npm-audit watch at its forty-fourth
re-check (0 vulnerabilities --omit=dev — the v110 bump holds [next
16.4.3 + zod 4.6.7]; no new advisories in the watched ranges), the
147th standing checks (ALL GREEN — the reference's four bugs live; the
data census clean on the FIRST reads; the clone's mobile menu VERIFIED
WORKING the 147th consecutive time; zero overflow at 390 on all five
views; the seedcheck exact after the clone half).

The baseline GREEN on the FIRST run (the SAME-PERSISTED workspace —
the v152 environment held: node_modules 354 entries + BOTH chromium
pairs [1200 + 1243] + the canonical Oct-31-stamped seed verified live
[the items 2026-10-21..29 + the assets'/liabilities' lastUpdated
2026-10-31]; the repo pulled clean to main @ a9a2d4c [adding
docs/session_397.md — the operator's preserved v152 transcript]; the
seedcheck EXACT 7/1850/2235/0/3/2 before any gate — under the env -u
discipline, the sandbox DATABASE_URL pollution live as documented):
lint, typecheck, 108/108 unit, build [robots + sitemap prerendered],
the 4-chunk e2e [359 executions = 356 unique, ZERO flakes], 35/35
smoke; the production-seam audit clean; skills/ excluded.

The probe series derived from the v147 lineage (derive-v153-series.py
— the generic swaps incl. the SIX explicit session-token families
[refvlm/clonevlm + refcalc/clonecalc + reflogin/clonelogin arbit] +
the history-correction fragments [the era marker last re-shot
v141->v147 + the oldest-remaining list v141..v144->v147..v152 + the
plan citation v146->v152 + the agreement ordinal SEVENTIETH->
SEVENTY-SIXTH + the re-run ordinal FOURTEENTH->FIFTEENTH + the
bracket extended in all four corrected files], all applied on the
FIRST run, zero residual, line counts preserved 102/166/65/355) + the
login-shots sub-series (derive-loginshots-v153.py — 30/30 preserved)
+ the two-half builder (derive-build-twohalf-v153.py — the
lesson-range bump v92..v146->v92..v152 + the lineage-note fixup LAST —
the v110 swap-order rule) + the comparator (derive-compare-v153.py —
the provenance citations re-pointed at the v147 measurement) + the
verify script (derive-verify-twohalf-v153.py) + the 147th standing
pair derived (derive-standing-v153.py — the ordinal 146th->147th
th->th plain replace, ref146/clone146->ref147/clone147, v146->v147
[the files carry the ORDINAL as their version token: the 146th pair
ran in cycle v152, the 147th pair runs in cycle v153]; normalize-back
diff clean, line counts preserved 119/74). The halves built + the
TWO-block md5 contract verified by the direct THREE-WAY python
extraction (verify-twohalf-v153.py — CALC_CENSUS_JS [the calculator
census JS] 61 lines md5 e1092d12d06677a4 + LOGIN_CENSUS_JS [the login
census JS] 36 lines md5 9e5a52d2ab0f2ab9, byte-identical across
arbit-v153.sh + ref-arbit-v153.sh + clone-arbit-v153.sh — the
documented v123/v129/v135/v141/v147 lineage values VERBATIM: the
census JS blocks carry no version tokens, so the digests are
cycle-invariant).

The VLM pairwise run TWICE (the full logs at /tmp/vlm153/): pass 1
CALCULATOR DIFFERENT / LOGIN IDENTICAL / pass 2 CALCULATOR DIFFERENT /
LOGIN DIFFERENT (by one element) — the pair's documented
verdict-VARIATION family (the login verdict has varied
IDENTICAL/DIFFERENT across re-runs — v105/v129 IDENTICAL, v135 pass 2
DIFFERENT-with-the-sole-disproven-flag, v141 IDENTICAL x2, v147
IDENTICAL x2; here pass 1 IDENTICAL, pass 2 DIFFERENT on the sole FAB
note). The login passes' sole note the reference's own "Edit with
Base44" FAB (the PLATFORM-CHROME class) — DISPROVEN LIVE by
base44-fab-arbit-v153.sh (the single-surface form at 1280 /login,
logged-out: fabCount 0 + bodyHasBase44 false on BOTH sides — the
standing v97..v147 disproof form re-confirmed). Every calculator flag
in both passes in the documented classes, arbitration-free (every
flag's class already DOM-confirmed by the census's own axes): the
line-item row hover action buttons "missing" on the clone the
POINTER-POSITION/HOVER-STATE screenshot artifact (the census
actionsAtRest {opacity 0, btnCount 2} IDENTICAL both sides — the
reference's shot carries its hover-revealed buttons, the clone's its
at-rest hidden ones; the v129/v135/v141/v147 documented class); the
"Will update category total" note the SEED-DATA class (ref false vs
clone true — totalCard.hasWillUpdateSpan; the reference's Rent $25.00
equals its calculated total so the note hides; the clone's Rent $1850
vs the recalculated $25.00 shows it — the totalCard box
byte-identical). The both-sides census compared axis-by-axis
(compare-v153-census.py): 106 axes — 97 identical + 9
documented-class deltas, ZERO new — REPRODUCING the v147 census values
EXACTLY (the same 106/97/9 split, zero drift on every axis); the
seedcheck exact after the clone half.

F4 -> the pin: the CALCULATOR DIALOG "Add Item" BUTTON's
FOCUS-VISIBLE LADDER at 1280 — NO GAP (PIN-ONLY). The candidate
survey: the LOGIN+CALC-pair surfaces' interaction families ALL HELD
except the calculator Add Item button's focused state — never pinned
at ANY viewport (the suite-wide survey: rg "Add Item" across
tests/e2e/*.spec.ts — the focus/ladder matches are the
DIFFERENT-ELEMENT dashboard quick-action card + the v145/v146/v151
OUT-OF-BOUNDS comments; the v81 census holds this button's at-rest
chrome only; the v129 own-hover pin's finder EXPLICITLY EXCLUDES it;
the v135 focus pin is the dialog X only) — the sibling-completion form
(the v149/v150/v151/v152 precedent): the Add-button family's focus
ladders closed on EVERY page-header sibling; this pin closes the
family's DIALOG member — the zb-btn-add-sm variant, in the same dialog
as the v135 X-focus pin, on the pair's own calculator surface at the
pair's own 1280 viewport. The discovery census
additemfocus-discovery-v153.sh (both sides' ladders at 1280 in the
Rent Calculator dialog — the standing read-only dialog-open path [the
real-mouse Rent-card hover + the Calculate click], the STRUCTURAL
finder [the unique button whose trimmed text is exactly "Add Item"
inside a fixed overlay container — works on BOTH sides: the clone's
Radix role=dialog + the reference's PLAIN fixed div, the documented
reference class], the REAL focusVisible idiom, the (5,5)-parked
pointer, READ-ONLY) measured both sides' ladders CLEAN — NO GAP: the
focused rung's v11 G2c four-layer composite [fv true + the white
zero-spread lead + the 1px #0a0a0a ring + the two ambient 0.1 layers]
+ the orange gradient UNCHANGED under focus [focus != hover] + the
110x32 geometry byte-identical both sides, the blur restore clean; the
sole deltas the documented invisible constructs (the at-rest
outlineColor computed form [REF rgba(10,10,10,0.5) vs CLONE
lab(2.74175 0 0.00000596046 / 0.5)] — the v95 class; the at-rest
lead-layer construct — the v3/v4 construct class; all invisible by
construction, never pinned). THE PLAN WRITTEN BEFORE THE PIN
(docs/remediation-plan-v153.md). THE PIN (append-pin-v153.py — ONE
test appended to calculator.spec.ts: the sibling-completion form
adapting the v145 ladder pin's measurement idiom to the pair's
calculator surface — the dialog-open path [the v135 form: the settle
line '3 items · $2235.00', the Rent-card hover + the Calculate click],
the role finder dialog.getByRole("button", { name: /^Add Item$/ }), the
at-rest -> focused -> blurred ladder at 1280, the (5,5)-parked
pointer, the REAL focus({focusVisible:true}) idiom, the 450ms settles;
the at-rest outlineColor axis deliberately NOT asserted — the v95
discipline) — green on the current build on the FIRST invocation (the
PIN-ONLY form; no RED step: there is no repair); the authoritative
--list: 357 in 24 files.

THE PIN-SANITY MUTATION — the COMPOSITE-REMOVAL form (the
`.zb-btn-add:focus-visible` block disabled from globals.css — the
exact CSS-cleanup drift class the pin exists to guard, the same
mutation family as the v144/v145/v146/v150/v151 sanity; the WIDER
blast radius noted [the construct serves EVERY zb-btn-add instance —
the v35 S2 dashboard pin + the v144/v145/v146/v150/v151 page-header
pins live on the same composite in other files]): the FULL CALCULATOR
SWEEP read 1 failed [EXACTLY the v153 pin — the family's dialog
member, the sole composite-dependent pin in this file] + 22 passed
(the 21 old tests + the setup execution — the v129 own-hover pin's +
the v135 X-focus pin's same-file immunity verified live), the failure
diff EXACTLY the predicted focused-rung composite axes (the 4-axis
outline family — outlineStyle solid->auto / outlineColor
rgba(0,0,0,0)->lab() / outlineWidth 2px->1px / outlineOffset 2px->0px —
while the focused/fv/opacity/geometry axes were preserved, the focus
!= hover family intact); restored (git diff src/ = 0 lines) + the
FULL REBUILD + the post-restore regression 23 passed (the full
calculator sweep — the v129/v135 pins' same-file immunity verified
live again).

The ship chain: 357 e2e ZERO flakes (99+96+82+83 = 360 executions =
357 unique — the +1 landing in ch4 [calculator]; both closed watches
green through the chain); 35/35 smoke; the screenshots 16/16 captured
— 16 byte-identical (the same-day law: the capture day Nov 4 UTC ==
the committed v152 captures' day — the 07-add-item-modal wall-clock
surface matching byte-for-byte [11/04/2026]; every seed-stamped
surface byte-identical under the canonical Oct 31 stamps — the
same-seed law intact, zero arbitration); the dev evidence 4/4
byte-identical + VLM-verified (the menu proof {"url":"/income",
"docSW":390,"navLandmark":true}; the dev-shots scripts derived
v152->v153 with the version-swap-only verification on both; the menu
OPEN [all 5 links + the brand] + the post-nav /income [the sheet
closed] + the dashboard [clean] all confirmed — the dashboard
fold/sidebar-glyph notes DISPROVEN by byte-identity to the committed
v152-verified set [the VLM pass-variation class, the
v150/v151/v152-documented form]).

The v154 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence's next-oldest candidate —
**the v148-era NETWORTH + drill-down-DASHBOARD pair** (the NETWORTH
view + the DASHBOARD's drill-down EXPANDED state at desktop 1280x800
[the v60-era pair's surface family], last re-shot v148 — now the
oldest remaining [v148 < v149 < v150 < v151 < v152]; the pair's
FIFTEENTH re-run bracket [v60 -> v67 -> v76 -> v82 -> v88 -> v94 ->
v100 -> v106 -> v112 -> v118 -> v124 -> v130 -> v136 -> v142 -> v148
-> v154] to be verified against the v148 lineage's own records before
the derivation — the v148 plan's own header records the FOURTEENTH
ordinal on its 15-entry bracket [v60 the original, one entry — 15
entries − the original = 14 re-runs], consistent, no off-by-one this
lineage; the v148 shots header carries the FULL bracket form, the
verification source),
(2) the axe-core watch at its next re-check point (only a 5.x wrapper
changes the calculus), (3) the npm-audit watch at its re-check point
(only a new advisory in the next/zod ranges changes the calculus),
(4) the deferred reference-write censuses (unchanged — out of bounds
under the v46 read-only rule), (5) the residual-class watch (both
flake classes CLOSED by the v136 dual-stack/localhost fix — the
watch continues in the standing form for any NEW class).

"""

text = io.open(PATH, encoding="utf-8").read()
if "## The v153 cycle" in text:
    print("SKIP: the v153 section already present")
    sys.exit(0)

anchor = "the standing form for any NEW class).\n\n## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)"
n = text.count(anchor)
if n != 1:
    print(f"FAIL: the insert anchor {n}x")
    sys.exit(1)

text = text.replace(anchor, "the standing form for any NEW class).\n\n" + SECTION + "## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)")
io.open(PATH, "w", encoding="utf-8").write(text)
print("OK: the v153 section + the v154 queue inserted (D6)")
