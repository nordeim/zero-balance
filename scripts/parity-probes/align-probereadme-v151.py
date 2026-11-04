#!/usr/bin/env python3
"""D6 — the probe README alignment for the v151 cycle: insert the v151
section (Session 186) between the v151 queue's end and '## The v138 cycle'
(each cycle section ends with the NEXT cycle's queue — the v150 section's
tail IS the v151 queue; the new v151 section carries the v152 queue)."""
import io
import sys

PATH = "scripts/parity-probes/README.md"

SECTION = """## The v151 cycle (the v145-era ITEMS pair's FIFTEENTH re-run — Session 186)

The re-run cadence's third-pass next-oldest candidate: the v145-era
ITEMS pair — the ITEMS view [INCOME + EXPENSES] at desktop 1280x800
FULL-PAGE (the v57-era pair's surface family), last re-shot v145 — now
the oldest remaining [v145 < v146 < v147 < v148 < v149 < v150]; the
pair's FIFTEENTH re-run bracket [v57 -> v64 -> v70 -> v79 -> v85 -> v91
-> v97 -> v103 -> v109 -> v115 -> v121 -> v127 -> v133 -> v139 -> v145
-> v151]; the SEVENTY-FOURTH consecutive queue/ledger agreement — the
surface names verified against the v145 lineage's own records BEFORE
the derivation (the v145 plan's own header: the FOURTEENTH ordinal on
its 15-entry bracket [v57 the original, one entry — 15 entries − the
original = 14 re-runs, no off-by-one this lineage]; the v145 shots
header carries the FULL bracket form, the verification source). **A
PIN-ONLY cycle — src/ ZERO production-code changes + one e2e pin
(354 -> 355): the EXPENSES PAGE-HEADER ADD EXPENSE button's
FOCUS-VISIBLE LADDER at 1280 — the never-pinned keyboard path of the
Add-button family's EXPENSE sibling (the v145 pin closed the INCOME
sibling at 1280 — the sibling-completion form, the v149/v150
precedent)**; the cycle's standing items: the axe watch (NO DRIFT —
4.14.0 holds, the v68 dedupe verified), the npm-audit watch at its
forty-second re-check (0 vulnerabilities --omit=dev — the v110 bump
holds [next 16.4.3 + zod 4.6.7]; no new advisories in the watched
ranges), the 145th standing checks (ALL GREEN — the reference's four
bugs live; the data census clean on the FIRST reads; the clone's
mobile menu VERIFIED WORKING the 145th consecutive time; zero overflow
at 390 on all five views; the seedcheck exact after the clone half).

The baseline GREEN on the FIRST run (the REBUILT workspace — the
sandbox recycled between sessions: the repo re-cloned at main @
1356203, npm ci [494 packages], the .env + db/ at the repo root + the
seed re-aligned to the canonical Oct 31 stamps via
scripts/align-seed-dates-v151.ts [the fresh Nov 3 seed shifted -3d on
every DISPLAYED date field — the items 2026-10-21..29 + the
assets'/liabilities' lastUpdated 2026-10-31, amounts untouched], BOTH
chromium pairs [1200 + 1243] available — the fresh-sandbox checklist
rule applied: BOTH chromium-1243 AND chromium_headless_shell-1243
verified in the cache before the first e2e run; the seedcheck EXACT
7/1850/2235/0/3/2 before any gate — under the env -u discipline, the
sandbox DATABASE_URL pollution live as documented): lint, typecheck,
108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e
[357 executions = 354 unique, ZERO flakes], 35/35 smoke; the
production-seam audit clean; skills/ excluded.

The probe series derived from the v145 lineage (derive-v151-series.py
— the generic swaps incl. the FOUR explicit session-token families
[refvlm/clonevlm + refarbit/clonearbit] + the history-correction
fragments [the era marker last re-shot v139->v145 + the later-pairs
list v140..v144->v146..v150 [savings v146, login+calculator v147,
networth+drill-down v148, dashboard v149, mobile twins v150] + the
re-run ordinal FOURTEENTH->FIFTEENTH + the bracket extended in all
four corrected files], all applied on the FIRST run, zero residual,
line counts preserved 57/49/50/285) + the two-half builder
(derive-build-twohalf-v151.py — the session-token bump
clonearbit145->clonearbit151 FIRST + the lesson-range bump
v92..v144->v92..v150 + the lineage-note fixup LAST — the v110
swap-order rule) + the comparator (derive-compare-v151.py — the
provenance citations re-pointed at the v145 measurement) + the verify
script (derive-verify-twohalf-v151.py) + the 145th standing pair
derived (derive-standing-v151.py — the ordinal 144th->145th th->th
plain replace, ref144/clone144->ref145/clone145, v144->v145;
normalize-back diff clean, line counts preserved 119/74). The halves
built + the ONE-block md5 contract verified by the direct THREE-WAY
python extraction (verify-twohalf-v151.py — CENSUS_JS [the items
census JS] 193 lines md5 b55dcd29, byte-identical across
arbit-v151.sh + ref-arbit-v151.sh + clone-arbit-v151.sh — the
documented v103/v109/v115/v121/v127/v133/v139/v145 lineage contract
VERBATIM: the items census JS block carries no version tokens, so the
digest is cycle-invariant).

The VLM pairwise run TWICE (the full logs at /tmp/vlm151/): pass 1
INCOME IDENTICAL + EXPENSES DIFFERENT (data-only) / pass 2 INCOME
DIFFERENT (data-only) + EXPENSES DIFFERENT (data-only) — the
verdict-variation form (the expenses pair STABLE-DIFFERENT-data-only
x2; the income pair's verdict varies, the v111-era form). Every flag
in both passes in the documented classes: the avatar the
USER-IDENTITY class; the grid layout/arrangement + count/total the
SEED-COUNT class (census-verified: income grid childCount 1 vs 2 +
expenses 4 vs 3, the template columns byte-identical); the header
stats + the card names/amounts/dates/badges/subtitles the SEED-DATA
classes; the badge wrap the v57 wrap/classification-VALUE classes
(census-whitelisted: the expenses badgeRow h 22 vs 52 + badgeCount 3
vs 4); the expense footer payment-method chips the v57
DATA-CONDITIONAL class; the FAB claims (the expenses pass-1 note +
the income pass-2 layout flag + the expenses pass-2 layout flag — the
PLATFORM-CHROME class) DISPROVEN LIVE by base44-fab-arbit-v151.sh
(the standing two-surface form at the pair's own 1280 viewport:
fabCount 0 + bodyHasBase44 false on BOTH sides, BOTH flagged surfaces
[/income + /expenses], 1280x800, logged-in — the
v97/v103/v108/v109/v115/v120/v123/v127/v129/v135/v141/v142/v143/v144/
v148/v149/v150 standing disproof form re-confirmed). The both-sides
census compared axis-by-axis (compare-v151-census.py): 187 axes —
163 identical + 24 documented-class deltas, ZERO new — REPRODUCING
the v145 census values EXACTLY (the same 187/163/24 split, zero drift
on every axis); the seedcheck exact after the clone half.

F4 -> the pin: the EXPENSES PAGE-HEADER ADD EXPENSE button's
FOCUS-VISIBLE LADDER at 1280 — NO GAP (PIN-ONLY). The candidate
survey: the items-pair surfaces' interaction families ALL HELD except
the expenses header Add Expense button's focused state — never pinned
at ANY viewport (the suite-wide survey: rg 'Add Expense' across
tests/e2e/*.spec.ts — 17 matches, ZERO focus/ladder matches on the
header button; the dashboard.spec.ts:5452 pin is the
DIFFERENT-ELEMENT quick-action card, the UA-default ring family; the
v145 pin closed the INCOME sibling at 1280) — the sibling-completion
form (the v149/v150 precedent). The discovery census
addexpfocus-discovery-v151.sh (both sides' ladders at 1280 on
/expenses — the structural finder [the v109 census's own finder
family — main button, trimmed text startsWith 'Add', top < 200 — the
page-header Add Expense button], the REAL focusVisible idiom, the
(5,5)-parked pointer, READ-ONLY) measured both sides' ladders CLEAN —
NO GAP: the focused rung's v11 G2c composite [outline 2px solid
transparent + offset 2px + the FOUR-layer box-shadow — the white
zero-spread lead + the 1px #0a0a0a ring + the two ambient layers]
byte-identical both sides, the ORANGE gradient + opacity UNCHANGED
under focus (focus != hover), the blur restore clean; the sole deltas
the documented classes (the at-rest outlineColor computed form [REF
rgba(10,10,10,0.5) vs CLONE lab(2.74175 0 0.00000596046 / 0.5) — the
v43-F2 class, never pinned per the v95 discipline] + the at-rest
invisible lead-layer construct [the v66 class, never pinned]). THE
PLAN WRITTEN BEFORE THE PIN (docs/remediation-plan-v151.md). THE PIN
(append-pin-v151.py — 144 lines, ONE test: the sibling-completion
form adapting the v145 pin's measurement idiom — the /expenses view,
the settle line '3 items · $2235.00', the structural role finder
/^Add Expense$/, the at-rest -> focused -> blurred ladder at 1280, the
(5,5)-parked pointer, the REAL focus({focusVisible:true}) idiom, the
450ms settles; the outlineColor axes deliberately NOT asserted) —
green on the current build on the FIRST invocation (the PIN-ONLY
form; no RED step: there is no repair); the authoritative --list: 355
in 24 files.

THE PIN-SANITY MUTATION — the COMPOSITE-REMOVAL form (the
.zb-btn-add:focus-visible block disabled from globals.css — the exact
CSS-cleanup drift class the pin exists to guard, the same mutation
family as the v144/v145/v150 sanity; the WIDER blast radius noted
[the family serves every zb-btn-add instance — the v144/v145/v146/
v150 items pins + the v35 S2 dashboard pin live on the same composite
in other files]): the FULL ITEMS SWEEP read 3 failed [EXACTLY the
v145 Add Income pin + the v146 Add Savings pin + the v151 Add Expense
pin — the shared-family class, all three items-file Add-button ladder
pins together] + 54 passed, the failure diff EXACTLY the predicted
focused-rung composite axes (the 4-axis outline family diff —
outlineStyle/outlineColor/outlineWidth/outlineOffset — while the
focused/fv/opacity axes were preserved, the focus != hover family
intact); restored (git diff src/ = 0 lines) + the FULL REBUILD + the
post-restore regression 57 passed (the full items sweep — the
v145/v146 pins' same-file immunity verified live).

The ship chain: 355 e2e ZERO flakes (98+96+82+82 = 358 executions =
355 unique — the +1 landing in ch1 [items]; both closed watches green
through the chain); 35/35 smoke; the screenshots 16/16 captured — 15
byte-identical + 1 the documented WALL-CLOCK class (the capture day
Nov 4 UTC — the 07-add-item-modal surface's todayIso() date default
crossed UTC midnight [11/03/2026 -> 11/04/2026], VLM-confirmed on the
pixel-diff crop: the sole diff a 16x22px region, 232 pixels, the date
field alone — the same re-commit convention as
v117/v122/v124/v131/v133/v135/v136/v138/v145; every seed-stamped
surface byte-identical under the canonical Oct 31 stamps — the
same-seed law intact); the dev evidence 4/4 byte-identical +
VLM-verified (the menu proof {"url":"/income","docSW":390,
"navLandmark":true}; the dev-shots scripts derived v150->v151 with
the version-swap-only verification on both; the menu OPEN [all 5
links + the brand] + the post-nav /income [the sheet closed] + the
dashboard [clean] all confirmed — the one pass-2 avatar-overlap note
on the menu capture DISPROVEN by the byte-identity to the committed
v150-verified set + the DOM census [exactly ONE avatar circle in the
sheet footer — the user-initial glyph, no second circle] — the VLM
glyph-misread class).

The v152 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence's next-oldest candidate —
**the v146-era SAVINGS pair** (the SAVINGS view at desktop 1280x800
FULL-PAGE [the v58-era pair's surface family], last re-shot v146 — now
the oldest remaining [v146 < v147 < v148 < v149 < v150 < v151]; the
pair's FIFTEENTH re-run bracket [v58 -> v65 -> v74 -> v80 -> v86 -> v92
-> v98 -> v104 -> v110 -> v116 -> v122 -> v128 -> v134 -> v140 -> v146
-> v152] to be verified against the v146 lineage's own records before
the derivation — the v146 plan's own header records the FOURTEENTH
ordinal on its 15-entry bracket [v58 the original, one entry — 15
entries − the original = 14 re-runs], consistent, no off-by-one this
lineage; the v146 shots header carries the FULL bracket form, the
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
if "## The v151 cycle" in text:
    print("SKIP: the v151 section already present")
    sys.exit(0)

anchor = "the standing form for any NEW class).\n\n## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)"
n = text.count(anchor)
if n != 1:
    print(f"FAIL: the insert anchor {n}x")
    sys.exit(1)

text = text.replace(anchor, "the standing form for any NEW class).\n\n" + SECTION + "## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)")
io.open(PATH, "w", encoding="utf-8").write(text)
print("OK: the v151 section + the v152 queue inserted (D6)")
