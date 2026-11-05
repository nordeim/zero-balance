#!/usr/bin/env python3
"""D6 — the probe README alignment for the v155 cycle: insert the v155
section (Session 190) between the v155 queue's end and '## The v138 cycle'
(each cycle section ends with the NEXT cycle's queue — the v154 section's
tail IS the v155 queue; the new v155 section carries the v156 queue)."""
import io
import sys

PATH = "scripts/parity-probes/README.md"

SECTION = """## The v155 cycle (the v149-era DASHBOARD pair's FIFTEENTH re-run — Session 190)

The re-run cadence's third-pass next-oldest candidate: the v149-era
DASHBOARD pair — the DASHBOARD at desktop 1280x800 FULL-PAGE (the
v61-era pair's surface family: the BUDGET GUIDELINES card + the
QUICK-ACTION row below the fold), last re-shot v149 — now the oldest
remaining [v149 < v150 < v151 < v152 < v153]; the pair's FIFTEENTH
re-run bracket [v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107
-> v113 -> v119 -> v125 -> v131 -> v137 -> v143 -> v149 -> v155]; the
SEVENTY-EIGHTH consecutive queue/ledger agreement — the surface names
verified against the v149 lineage's own records BEFORE the derivation
(the v149 plan's own header: the FOURTEENTH ordinal on its 15-entry
bracket [v61 the original, one entry — 15 entries − the original = 14
re-runs, no off-by-one this lineage]; the v149 shots header carries
the FULL bracket form, the verification source). **A PIN-ONLY cycle
— src/ ZERO production-code changes + one e2e pin (358 -> 359): the
DASHBOARD QUICK-ACTION SIBLING CARDS' (Add Savings + Add Expense)
HOVER END-STATE LADDERS at 1280, BOTH cards in ONE test — the
never-pinned HOVER PATH of the SIBLING cards (the v125 pin closed the
FIRST card's hover end-states [the tile's scale-110 reveal + the
plus's opacity-100 reveal — the Add Income card only, the sole
.hover() on the QA surface in the entire suite]; the v149 pin the
siblings' KEYBOARD paths [the focus-visible ladders]; the at-rest
chrome by the v61 F3/v107 pins; the card's shadow-lg layers by the
v45 F3b pin; the transition timing by the v95 pin — the hover
family's sibling-completion form)**; the cycle's standing items: the
axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified), the
npm-audit watch at its forty-sixth re-check (0 vulnerabilities
--omit=dev — the v110 bump holds [next 16.4.3 + zod 4.6.7]; no new
advisories in the watched ranges), the 149th standing checks (ALL
GREEN — the reference's four bugs live; the data census clean on the
FIRST reads; the clone's mobile menu VERIFIED WORKING the 149th
consecutive time; zero overflow at 390 on all five views; the
seedcheck exact after the clone half).

The baseline GREEN on the FIRST run (the FRESH-CLONE rebuild — the
sandbox reset between sessions: the repo re-cloned from main @
577e2ac [the v154 push verified]; npm ci [494 packages] + .env from
.env.example + a fresh AUTH_SECRET + db:push + db:seed +
align-seed-dates-v155.ts [the observed Nov-5 seed day shifted -5d to
the canonical Oct-31 stamps — the items 2026-10-21..29 + the
assets'/liabilities' lastUpdated 2026-10-31] + the Playwright
chromium-1243 pair joining the cached 1200 pair; the seedcheck EXACT
before any gate [under the env -u discipline]): lint, typecheck,
108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e
[361 executions = 358 unique, ZERO flakes], 35/35 smoke, the
production-seam audit clean; skills/ excluded.

The probe series derived from the v149 lineage (derive-v155-series.py
— the FOUR explicit session-token families [refvlm/clonevlm +
refar/clonear] + the history-correction fragments [the era marker
last re-shot v143->v149 + the oldest-remaining list [v143 < v144]->
[v149 < v150 < v151 < v152 < v153] + the agreement ordinal
SEVENTY-SECOND->SEVENTY-EIGHTH + the re-run ordinal FOURTEENTH->
FIFTEENTH + the bracket extended + the re-proves windows
v101-v143->v101-v149 + the arbit census provenance since-v143->
since-v149 + the v143-verdict->v149-verdict citation + the compare
banner FOURTEENTH->FIFTEENTH], all applied on the FIRST run, zero
residual, line counts preserved 58/43/46/259) + the two-half builder
(derive-build-twohalf-v155.py — the lesson-range bump v92..v148->
v92..v154 + the lineage-note fixup LAST) + the comparator
(derive-compare-v155.py) + the verify script
(derive-verify-twohalf-v155.py) + the FAB arbit
(derive-base44fab-v155.py — the header narrative corrected from the
v149 no-claims standing form to the v155 claims form) + the 149th
standing pair derived (derive-standing-v155.py — the ordinal
148th->149th, ref148/clone148->ref149/clone149, v148->v149). The
halves built + the THREE-block md5 contract verified by the direct
THREE-WAY python extraction (ARBIT_G [the GUIDELINES census JS] 61
lines md5 b500dd299e5e9a94eaf07b29facc69db + ARBIT_Q [the
QUICK-ACTION census JS] 58 lines md5 da04e9954976eb58d9aff2b95d2dcfc6
+ ARBIT_X [the CROSS-ROW GAP census JS] 25 lines md5
7a381755a22ce55c62f70a053f826852, byte-identical across
arbit-v155.sh + ref-arbit-v155.sh + clone-arbit-v155.sh — the
digests EQUAL the v149 lineage values by construction: THIS lineage's
census JS carries no version-bearing tokens [verified live], the
cycle-invariant class).

The VLM pairwise run TWICE: pass 1 IDENTICAL / pass 2 IDENTICAL — the
v143/v149 cleanest pair form REPRODUCED (zero layout/style flags on
the pair's focus surfaces in either pass; the passes' only notes the
documented classes: the FAB note claimed in BOTH passes, ref-only —
DISPROVEN LIVE by base44-fab-arbit-v155.sh [fabCount 0 +
bodyHasBase44 false on BOTH sides at 1280 on the flagged surface,
logged-in]; the nav-highlight the v56 SUPERSET class; the avatar the
USER-IDENTITY class; the data differences the EACH-SITE'S-OWN-DATA
classes — the standing census axes). The both-sides census compared
axis-by-axis: 154 axes — 144 identical + 10 documented-class deltas,
ZERO new — REPRODUCING the v149 census values EXACTLY (the same
154/144/10 split; the seedcheck exact after the clone half).

The F4 candidate survey found the never-pinned hover-family sibling
path: the Add Savings + Add Expense dashboard quick-action cards'
HOVER END-STATES — held by NO spec at ANY viewport (the suite-wide
survey: ZERO hover/scale/opacity assertions on these two cards
across all 24 spec files; the items.spec v146/v151 pins cover the
SAVINGS/EXPENSES page-header BUTTONS — different elements on different
views). The both-sides one-shot census qasibhover-discovery-v155.sh
(the v125 qahover arbitration form adapted to the SIBLING cards: the
per-card STRUCTURAL finders [the button whose trimmed text is exactly
the card name; the tile finder TAG-AGNOSTIC — the radius-12px box in
the 30..60 band, the v107 DIV-vs-SPAN lesson, the state-read band
25..65 covering both rungs], the REAL pointer hover at the live-read
card center [the coords read after the scrollIntoView — never
guessed; the mouse move takes x y as TWO args — the v123 lesson], the
(5,5)-parked pointer [the v22 lesson], the SIBLING NON-INTERFERENCE
cross-check at the hovered rung [the v149 form], the seedcheck at the
end, READ-ONLY) measured BOTH SIDES' ladders on BOTH sibling cards
CLEAN — NO GAP: the tile's group-hover:scale-110 reveal (the rendered
40x40 -> 44x44 the parity contract; the computed form the documented
v125 class — the reference's Tailwind v3 transform matrix vs the
clone's v4 `scale` property, the same rendered rect) + the plus's
group-hover:opacity-100 reveal (0.5 -> 1) + the cardHover state + the
per-card tile tints (savings rgba(59,126,161,0.125) / expense
rgba(224,122,59,0.125)) identical both sides + the sibling
cross-checks clean + the restores clean; the sole deltas the
documented classes (the v125 computed form + the card's
hovered-shadow transparent lead layers [the v66 class — held by the
v45 F3b pin]). THE PLAN WRITTEN BEFORE THE PIN
(docs/remediation-plan-v155.md).

THE PIN (append-pin-v155.py — ONE test appended to dashboard.spec.ts:
the hover family's sibling-completion form adapting the v125 hover
pin's finder + ladder idioms to the sibling cards — the per-card
structural finder, the at-rest -> hovered -> restored ladder at 1280
with the REAL pointer hover [the locator .hover() — the v43/v45/v125
idiom] + the (5,5)-parked pointer, the scale-110 + opacity-100 reveal
assertions, the per-card tile-tint axis, the sibling
non-interference cross-checks) — green on the current build on the
FIRST invocation (the PIN-ONLY form; no RED step: there is no
repair); the authoritative --list: 359 in 24 files.

THE PIN-SANITY MUTATION — the SIBLING-HOVER-SUPPRESSION form (the
two group-hover reveal utilities removed from the QuickActionCard
component [dashboard-view.tsx:890 the tile's group-hover:scale-110 +
:899 the plus's group-hover:opacity-100] + the standalone REBUILD —
the exact CSS-cleanup drift class the pin exists to guard; the WIDER
blast radius noted [the construct serves the FIRST card too — the
v125 pin lives on the same reveals in the same file]): the FULL
DASHBOARD SWEEP read 2 failed [EXACTLY the hover-reveal family — the
v125 + v155 pins, the sole reveal-dependent pins in the file] + 55
passed (the 54 old non-reveal tests + the setup execution — the v149
focus pin's + every other dashboard test's same-file immunity
verified live), the v155 failure diff EXACTLY the predicted reveal
axes (the hovered rung's tile {scale 1.1->none, h 44->40} + the plus
{opacity 1->0.5} — while cardHover true, the bg tint, the transform
axis, the at-rest/restore rungs all preserved); restored (git diff
src/ = 0 lines) + the FULL REBUILD + the post-restore regression 57
passed (the full dashboard sweep).

The ship chain: 359 e2e ZERO flakes (99+98+82+83 = 362 executions =
359 unique — the +1 landing in ch2 [dashboard]; both closed watches
green through the chain); 35/35 smoke; the screenshots 16/16
captured — the day-change protocol applied, the documented v148
precedent form (15 byte-identical + the 07-add-item-modal the
wall-clock surface [the dialog-default date 11/05/2026 vs the
committed v154 captures' 11/04/2026] — the delta pixel-bounded to the
EXACT documented 16x22px region at (1552,931)-(1568,953) [the
v66/v75 bbox, everything else in the 2880x1800 frame byte-stable];
the new capture committed as the refreshed state — the same-seed law
intact, every seed-stamped surface byte-identical under the canonical
Oct 31 stamps, zero arbitration); the dev evidence 4/4
byte-identical + VLM-verified (the menu proof
{"url":"/income","docSW":390,"navLandmark":true}; the dev-shots
scripts derived v154->v155 via derive-devshots-v155.py with the
version-swap-only verification on both; the menu OPEN [all 5 links +
the NAVIGATION heading + the ZeroBalance / Budget Planner brand] +
the post-nav /income [the sheet closed] + the dashboard [clean] all
confirmed — the dashboard fold/minus-glyph notes DISPROVEN by
byte-identity to the committed v154-verified set [the VLM
pass-variation class, the v150/v151/v152/v153/v154-documented form]).

The v156 queue (suggestions — verify against the rotation ledger
before executing; THE CORRECTED CONVENTION — the ordinal ALWAYS
derived from the from-lineage's own bracket [entries − 1, the
original not a re-run], never the prose): (1) the re-run cadence's
next-oldest candidate — **the v150-era MOBILE-TWINS pair** (the
/NETWORTH view + the DASHBOARD, both FULL-PAGE at mobile 390x844 [the
v62/v63-era twins' surface family], last re-shot v150 — now the
oldest remaining [v150 < v151 < v152 < v153]; the pair's FIFTEENTH
re-run bracket [v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 ->
v108 -> v114 -> v120 -> v126 -> v132 -> v138 -> v144 -> v150 -> v156]
to be verified against the v150 lineage's own records before the
derivation — the v150 plan's own header records the FOURTEENTH
ordinal on its 15-entry bracket [v62/v63 the original pair, one entry
— 15 entries − the original = 14 re-runs], consistent, no off-by-one
this lineage; the v150 shots header carries the FULL bracket form,
the verification source), (2) the axe-core watch at its next
re-check point (only a 5.x wrapper changes the calculus), (3) the
npm-audit watch at its re-check point (only a new advisory in the
next/zod ranges changes the calculus), (4) the deferred
reference-write censuses (unchanged — out of bounds under the v46
read-only rule), (5) the residual-class watch (both flake classes
CLOSED by the v136 dual-stack/localhost fix — the watch continues in
the standing form for any NEW class).

"""

text = io.open(PATH, encoding="utf-8").read()
if "## The v155 cycle" in text:
    print("SKIP: the v155 section already present")
    sys.exit(0)

anchor = "the standing form for any NEW class).\n\n## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)"
n = text.count(anchor)
if n != 1:
    print(f"FAIL: the insert anchor {n}x")
    sys.exit(1)

text = text.replace(
    anchor,
    "the standing form for any NEW class).\n\n" + SECTION + "## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)",
)
io.open(PATH, "w", encoding="utf-8").write(text)
print("OK: the v155 section + the v156 queue inserted (D6)")
