#!/usr/bin/env python3
"""D6 — the probe README alignment for the v150 cycle: insert the v150
section (Session 185) between the v150 queue's end and '## The v138 cycle'
(each cycle section ends with the NEXT cycle's queue — the v149 section's
tail IS the v150 queue; the new v150 section carries the v151 queue)."""
import io
import sys

PATH = "scripts/parity-probes/README.md"

SECTION = """## The v150 cycle (the v144-era MOBILE-TWINS pair's FOURTEENTH re-run — Session 185)

The re-run cadence's third-pass next-oldest candidate: the v144-era
MOBILE-TWINS pair — the /networth view + the DASHBOARD, both FULL-PAGE
at mobile 390x844 (the v62/v63-era twins' surface family), last re-shot
v144 — now the oldest remaining [v144]; the pair's FOURTEENTH re-run
bracket [v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 ->
v114 -> v120 -> v126 -> v132 -> v138 -> v144 -> v150]; the
SEVENTY-THIRD consecutive queue/ledger agreement — the surface names
verified against the v144 lineage's own records BEFORE the derivation
(the v144 plan's own header: the THIRTEENTH ordinal on its 14-entry
bracket [v62/v63 the original pair, one entry — 14 entries − the
original = 13 re-runs, no off-by-one this lineage]; the v144 shots
header carries the FULL bracket form, the verification source). **A
PIN-ONLY cycle — src/ ZERO production-code changes + one e2e pin
(353 -> 354): the networth ADD LIABILITY button's FOCUS-VISIBLE LADDER
at 390 — the never-pinned keyboard path of the Add-button family's
LIABILITY sibling (the v144 pin closed the ASSET sibling at 390 — the
sibling-completion form, the v149 precedent)**; the cycle's standing
items: the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe
verified), the npm-audit watch at its forty-first re-check (0
vulnerabilities --omit=dev — the v110 bump holds [next 16.4.3 + zod
4.6.7]; no new advisories in the watched ranges), the 144th standing
checks (ALL GREEN — the reference's four bugs live; the data census
clean on the FIRST reads; the clone's mobile menu VERIFIED WORKING the
144th consecutive time; zero overflow at 390 on all five views; the
seedcheck exact after the clone half).

The baseline GREEN on the FIRST run (the REBUILT workspace — the
sandbox recycled between sessions: the repo re-cloned at main @
a94b0f1, npm ci [494 packages], the .env + db/ at the repo root + the
seed re-aligned to the canonical Oct 31 stamps via
scripts/align-seed-dates-v150.ts [the fresh Nov 3 seed shifted -3d on
every DISPLAYED date field — the items 2026-10-21..29 + the
assets'/liabilities' lastUpdated 2026-10-31, amounts untouched], BOTH
chromium pairs [1200 + 1243] available — the fresh-sandbox checklist
rule applied: BOTH chromium-1243 AND chromium_headless_shell-1243
verified in the cache before the first e2e run; the seedcheck EXACT
7/1850/2235/0/3/2 before any gate — under the env -u discipline, the
sandbox DATABASE_URL pollution live as documented): lint, typecheck,
108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e
[356 executions = 353 unique, ZERO flakes], 35/35 smoke; the
production-seam audit clean; skills/ excluded.

The probe series derived from the v144 lineage (derive-v150-series.py
— the generic swaps incl. the FOUR explicit session-token families
[refvlm/clonevlm + the LONG-FORM refarbit/clonearbit — the
mobile-twins lineage's own token form, the tokens carrying '144'
without the 'v' prefix] + the history-correction fragments [the plan
pointer the v143 plan's->the v149 plan's + the era marker last re-shot
v138->v144 + the oldest-remaining list [v138]->[v144] + the re-run
ordinal THIRTEENTH->FOURTEENTH + the bracket extended + the verdicts
window v108/v138->v108/v144 + the arbit census provenance "The v138
census axes"->"The v144 census axes"], all applied on the FIRST run,
zero residual, line counts preserved 60/47/68/219) + the two-half
builder (derive-build-twohalf-v150.py — the session-token bump
clonearbit144->clonearbit150 FIRST + the lesson-range bump
v92..v143->v92..v149 + the lineage-note fixup LAST) + the comparator
(derive-compare-v150.py — the /tmp/vlm144->/tmp/vlm150 log-path swap +
the provenance citations re-pointed at the v144 measurement) + the
verify script (derive-verify-twohalf-v150.py — the lineage-citation
extension ...+v144; the digests themselves UNCHANGED) + the 144th
standing pair (derive-standing-v150.py — the ordinal 143rd->144th
rd->th plain replace; normalize-back diff clean, line counts preserved
119/74).

The halves built + the TWO-block md5 contract verified by the direct
THREE-WAY python extraction (verify-twohalf-v150.py — NW_CENSUS [the
networth census] 42 lines md5 82cf8a43 + DASH_CENSUS [the dashboard
census] 87 lines md5 85e4ec7e, byte-identical across arbit-v150.sh +
ref-arbit-v150.sh + clone-arbit-v150.sh — the documented
v102/v108/v114/v120/v126/v132/v138/v144 lineage contracts VERBATIM:
the mobile-twins census JS blocks carry no version tokens, so the
digests are cycle-invariant).

The VLM verdict NETWORTH IDENTICAL x2 + DASHBOARD DIFFERENT->IDENTICAL
(the verdict-variation form; every pass-1 flag DOM-arbitrated to a
documented class — the dashboard subtitle wrap the RANGE-WALK
line-bucketing class [census-verified: the line TOPS 123/147
identical], the figures/proportions the PCT/SEED-DATA classes, the
avatar the USER-IDENTITY class; the FAB claims [the networth pass-1
note + the dashboard passes' flags — the PLATFORM-CHROME class]
DISPROVEN LIVE by base44-fab-arbit-v150.sh — the v144 two-surface
standing form at the pair's own 390 viewport: fabCount 0 +
bodyHasBase44 false on BOTH sides, BOTH flagged surfaces, logged-in).
The both-sides census compared axis-by-axis (compare-v150-census.py):
55 axes — 37 identical + 18 documented-class deltas, ZERO new —
REPRODUCING the v144 census values EXACTLY (the same 55/37/18 split,
zero drift on every axis; the seedcheck exact after the clone half).

The candidate survey found the never-pinned sibling keyboard path (the
networth ADD LIABILITY button's FOCUS-VISIBLE LADDER at 390 — ZERO
focus-visible/ring matches on 'Add Liability' across all 24 spec
files; the v144 pin closed the ASSET sibling at 390 — the
sibling-completion form, the v149 precedent; the mobile-390 kebab +
dashboard Add Item forms the weaker new-viewport extensions). THE
TAB-ACTIVATION PREREQUISITE (the structural finding): the button
renders inside the Radix TabsContent value="liabilities" panel — NOT
in the DOM while the Assets tab is active (the default on both
sites); the discovery activates the Liabilities tab FIRST (the v120 /
v148-follow-up full pointer-event sequence — VIEW-STATE only). The
discovery census addliabfocus-discovery-v150.sh (both sides' ladders
at 390 — the structural finder, the (5,5)-parked pointer, the REAL
focusVisible idiom, the outline family INCLUDING outlineColor,
READ-ONLY) measured the ladder CLEAN — NO GAP: the focused rung's v11
G2c composite [outline 2px solid transparent + offset 2px + the
FOUR-layer box-shadow: the white zero-spread lead + the 1px #0a0a0a
ring + the two ambient layers] byte-identical both sides, the ORANGE
gradient + opacity UNCHANGED under focus (focus != hover), the blur
restore clean, the sole deltas the documented classes (the at-rest
outlineColor computed form [REF rgba(10,10,10,0.5) vs CLONE
lab(2.74175 0 0.00000596046 / 0.5) — the v43-F2 construct class,
never pinned per the v95 discipline] + the at-rest invisible
lead-layer construct [the v66 class, never pinned]). THE PIN
(append-pin-v150.py — the sibling-completion form adapting the v144
pin's measurement idiom: the Liabilities tab activated FIRST [the v6
locator click], the Add Liability button's at-rest -> focused ->
blurred ladder at 390; the outlineColor axes deliberately NOT
asserted) — green on the current build on the FIRST invocation (the
PIN-ONLY form; no RED step: there is no repair); the authoritative
--list: 354 in 24 files.

The pin-sanity mutation — the COMPOSITE-REMOVAL form (the
.zb-btn-add:focus-visible block disabled from globals.css — the exact
CSS-cleanup drift class the pin exists to guard, the same mutation
family as the v144 sanity; the WIDER blast radius noted [the family
serves every zb-btn-add instance — the v145/v146 items pins + the v35
S2 dashboard pin live on the same composite in other files]): the
FULL NETWORTH SWEEP read 2 failed [EXACTLY the v144 Add Asset pin +
the v150 Add Liability pin — the shared-family class] + 43 passed,
the failure diff EXACTLY the predicted focused-rung composite axes
(the 4-axis outline family diff — outlineStyle/outlineColor/
outlineWidth/outlineOffset — while the focused/fv/opacity axes were
preserved); restored (git diff src/ = 0 lines) + the FULL REBUILD +
the post-restore regression 45 passed (the full networth sweep).

The ship chain: lint, typecheck, 108/108 unit, 0-vuln audit, 354 e2e
ZERO flakes (97+96+82+82 = 357 executions = 354 unique — the +1
landing in ch3 [networth]), 35/35 smoke, the screenshots 16/16
captured — 16 byte-identical (the same-day law: the capture day Nov 3
UTC == the committed v149 captures' day, the 07-add-item-modal
wall-clock form matching byte-for-byte; every seed-stamped surface
byte-identical under the canonical Oct 31 stamps), the dev evidence
4/4 byte-identical + VLM-verified (the menu proof
{"url":"/income","docSW":390,"navLandmark":true}; the dev-shots
scripts derived v149->v150 with the version-swap-only verification on
both).

The v151 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence's next-oldest candidate —
**the v145-era ITEMS pair** (the ITEMS view [INCOME + EXPENSES] at
desktop 1280x800 FULL-PAGE [the v57-era pair's surface family], last
re-shot v145 — now the oldest remaining [v145 < v146 < v147 < v148 <
v149 < v150]; the pair's FIFTEENTH re-run bracket [v57 -> v64 -> v70
-> v79 -> v85 -> v91 -> v97 -> v103 -> v109 -> v115 -> v121 -> v127 ->
v133 -> v139 -> v145 -> v151] to be verified against the v145 lineage's
own records before the derivation — the v145 plan's own header records
the FOURTEENTH ordinal on its 15-entry bracket [v57 the original, one
entry — 15 entries − the original = 14 re-runs], consistent, no
off-by-one this lineage; the v145 shots header carries the FULL bracket
form, the verification source),
(2) the axe-core watch at its next re-check point (only a 5.x wrapper
changes the calculus), (3) the npm-audit watch at its re-check point
(only a new advisory in the next/zod ranges changes the calculus),
(4) the deferred reference-write censuses (unchanged — out of bounds
under the v46 read-only rule), (5) the residual-class watch (both
flake classes CLOSED by the v136 dual-stack/localhost fix — the
watch continues in the standing form for any NEW class).

"""

text = io.open(PATH, encoding="utf-8").read()
if "## The v150 cycle" in text:
    print("SKIP: the v150 section already present")
    sys.exit(0)

anchor = "the standing form for any NEW class).\n\n## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)"
n = text.count(anchor)
if n != 1:
    print(f"FAIL: the insert anchor {n}x")
    sys.exit(1)

text = text.replace(anchor, "the standing form for any NEW class).\n\n" + SECTION + "## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)")
io.open(PATH, "w", encoding="utf-8").write(text)
print("OK: the v150 section + the v151 queue inserted (D6)")
