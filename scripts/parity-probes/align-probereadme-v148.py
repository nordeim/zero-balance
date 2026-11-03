#!/usr/bin/env python3
"""D6 — the probe README alignment for the v148 cycle: insert the v148
section (Session 183) between the v148 queue's end and '## The v138 cycle'
(each cycle section ends with the NEXT cycle's queue — the v147 section's
tail IS the v148 queue; the new v148 section carries the v149 queue)."""
import io
import sys

PATH = "scripts/parity-probes/README.md"

SECTION = """## The v148 cycle (the v142-era NETWORTH + drill-down-DASHBOARD pair's FOURTEENTH re-run — Session 183)

The re-run cadence's third-pass next-oldest candidate: the v142-era
NETWORTH + drill-down-DASHBOARD pair — the NETWORTH view + the
DASHBOARD's drill-down EXPANDED state at desktop 1280x800 (the
v60-era networth+drill-down pair's surface family), last re-shot
v142 — now the oldest remaining [v142] — the fourth entry of the
third-pass pool (the v133–v138 second-pass pool EXHAUSTED at v144;
the v139-era ITEMS pair re-run at v145; the v140-era SAVINGS pair
re-run at v146; the v141-era LOGIN + CALCULATOR pair re-run at
v147); the pair's FOURTEENTH re-run bracket [v60 -> v67 -> v76 ->
v82 -> v88 -> v94 -> v100 -> v106 -> v112 -> v118 -> v124 -> v130 ->
v136 -> v142 -> v148]; the SEVENTY-FIRST consecutive
queue/ledger agreement — the surface names verified against the v142
lineage's own records BEFORE the derivation (the v142 plan's own
header: the THIRTEENTH ordinal on its 14-entry bracket [v60 the
original, one entry — 14 entries − the original = 13 re-runs, no
off-by-one this lineage]; the v142 shots header carries the FULL
bracket form, the verification source). **A REPAIR + PIN cycle —
src/ ONE production-code change (the networth Liabilities tab
trigger's ORANGE active pair) + two e2e pins (350 -> 352)**; the
cycle's standing items: the axe watch (NO DRIFT — 4.14.0 holds, the
v68 dedupe verified), the npm-audit watch at its thirty-ninth
re-check (0 vulnerabilities --omit=dev — the v110 bump holds [next
16.4.3 + zod 4.6.7]; no new advisories in the watched ranges), the
142nd standing checks (ALL GREEN — the reference's four bugs live;
the data census clean on the FIRST reads; the clone's mobile menu
VERIFIED WORKING the 142nd consecutive time; zero overflow at 390 on
all five views; the seedcheck exact after the clone half).

The baseline GREEN on the FIRST run (the REBUILT workspace — the
sandbox recycled between sessions: the repo re-cloned at main @
39de745, npm ci [494 packages -> 354 entries], the .env + db/ at the
repo root + the seed re-aligned to the canonical Oct 31 stamps via
scripts/align-seed-dates-v148.ts [the fresh Nov 3 seed shifted -3d
on every DISPLAYED date field — the items 2026-10-21..29 + the
assets'/liabilities' lastUpdated 2026-10-31, amounts untouched],
BOTH chromium pairs [1200 + 1243] installed; the seedcheck EXACT
7/1850/2235/0/3/2 before any gate — under the env -u discipline,
the sandbox DATABASE_URL pollution live as documented): lint,
typecheck, 108/108 unit, build [robots + sitemap prerendered], the
4-chunk e2e [353 executions = 350 unique, ZERO flakes], 35/35 smoke;
the production-seam audit clean; skills/ excluded.

The probe series derived from the v142 lineage (derive-v148-series.py
— the generic swaps incl. the FOUR explicit session-token families
[refvlm/clonevlm + refar/clonear arbit — the tokens carry '142'
without the 'v' prefix] + the history-correction fragments [the era
marker last re-shot v136->v142 + the oldest-remaining list
[v136 < v137 < v138]->[v142 < v143 < v144] + the re-run ordinal
THIRTEENTH->FOURTEENTH + the bracket extended in all four files +
the agreement ordinal SIXTY-FIFTH->SEVENTY-FIRST + the arbit census
provenance the v136->the v142 census], all applied on the FIRST run,
zero residual, line counts preserved 84/71/65/328; one
residual-check refinement: the corrected census-provenance line's
token pair spans the line wrap — the whitelist extended to the
"census axes re-measured" tail) + the two-half builder
(derive-build-twohalf-v148.py — the generic swap + the lesson-range
bump v92..v141->v92..v147 [the BARE range token] + the lineage-note
fixup "the v136-lineage derivation"->"the v142-lineage derivation"
LAST [the v110 swap-order rule]) + the comparator
(derive-compare-v148.py — the generic swap + the provenance
citations re-pointed at the v142 measurement [the lineage ordinal
THIRTEENTH->FOURTEENTH; the records chain extended v130/v136->
v136/v142]) + the verify script (derive-verify-twohalf-v148.py — the
generic swap + the lineage-citation chain extended +v142) + the
142nd standing pair (derive-standing-v148.py — derived from the
141st pair, three token families [the ordinal 141st->142nd st->nd
plain replace — the suffix following the number's English form, the
same plain-replace family as v122's 121st/v132's 131st/v147's
140th->141st; the bare session names ref141/clone141->ref142/
clone142, the version v141->v142], normalize-back diff clean, zero
old tokens, line counts preserved 119/74). The halves built + the
TWO-block md5 contract verified by the direct THREE-WAY python
extraction (verify-twohalf-v148.py — ARBIT_A [the drill-down
census] 90 lines md5 a060791bcd1a9455e117cec08e7dc832 + ARBIT_B
[the networth summary-card census] 111 lines md5
2cacaf7aa0a1f0dcb0211b1e19dfe24f, byte-identical across
arbit-v148.sh + ref-arbit-v148.sh + clone-arbit-v148.sh — the
digests differ from the v142 cycle's by construction [the census JS
blocks' view-label tokens carry the version: "drill-arbit-1280-
v148" / "nw-height-1280-v148"]).

The resource discipline applied between every half (the browser
daemons reaped BEFORE every half; both halves + both shot series
executed with first-attempt logins; the full logs captured by the
runner redirection — /tmp/vlm148/{ref,clone}-census.log, the
comparator's documented input paths). The VLM pairwise run TWICE
with full log capture (/tmp/vlm148/vlm-pass{1,2}.log): pass 1
NETWORTH IDENTICAL / DRILL-DOWN DIFFERENT; pass 2 NETWORTH
IDENTICAL / DRILL-DOWN DIFFERENT — the v142 stable-identical-networth
form reproduced. Every drill-down flag in the documented classes,
arbitration-free (every flag's class already DOM-confirmed by the
census's own axes): the nav-highlight the v56 SUPERSET class, the
avatar the USER-IDENTITY class, the hero progress fill the PCT data
class, the donut labels + slice proportions the seed-data class,
the stat-card counts the seed-data class. The three FAB notes (the
PLATFORM-CHROME class — pass-1 networth + pass-1 drill-down +
pass-2 networth "Edit with Base44" claims) — DISPROVEN LIVE by
base44-fab-arbit-v148.sh (derived from the v142 form, swap-only +
the updated header: fabCount 0 + bodyHasBase44 false on BOTH sides
at 1280 on BOTH flagged surfaces [/ + /networth] — the standing
v97/v103/v108/v109/v115/v120/v123/v127/v129/v135/v141/v142
disproof form re-confirmed). The stat-card-label watch (the
documented VLM text-misread sub-form — "Total Expense" singular,
disproven at v106/v112/v118/v136) re-confirmed by
statfooter-arbit-v148.sh: both sides' third stat card title reads
"Total Expenses" (plural), the footer chrome byte-identical, the
sole deltas the seed-count texts.

The both-sides census compared axis-by-axis (compare-v148-census.py):
73 axes — 67 identical + 6 documented-class deltas, ZERO new —
REPRODUCING the v142 census values EXACTLY (the same 73/67/6 split,
zero drift on every axis: the 6 documented = avatarLetter [the
user-identity class] + donutLabels.texts [the each-site's-data
class] + navHighlight.color + navHighlight.fw [the v56 superset
class] + progress.fillW [the pct data class] + labelBlock.w [the
v82 data-conditional width class]). The seedcheck exact after the
clone half (7/1850/2235/0/3/2). NO NEW CLONE GAP on the census
axes.

THE REPAIR + THE PIN — the tablist trigger's FOCUS-VISIBLE LADDER
at 390 (the never-pinned KEYBOARD PATH of the pinned tablist
family: the at-rest chrome pinned at 640/390 by v50/v53, the
own-hover INERT ladder at 390 by v138, the roving arrow-key flip
by v30 G2 — the focus-visible END-STATE held by NO spec at ANY
viewport [the suite-wide survey: ZERO focus-visible/ring matches
on the tablist across all 24 spec files]) + THE LIABILITIES-ACTIVE
TABLIST CHROME (the cycle's REPAIR): the discovery census
tablistfocus-discovery-v148.sh (both triggers' focus ladders at
390 on BOTH sides — the outline family INCLUDING outlineColor)
measured the ladder CLEAN — NO GAP (the visible ring composite
"rgb(255,255,255) 0px 0px 0px 2px, rgb(10,10,10) 0px 0px 0px 4px"
byte-identical both sides; the sole deltas the documented INVISIBLE
outline construct [REF the v3 transparent form solid/2px/2px
rgba(0,0,0,0) vs CLONE the v4 none form — both invisible, never
pinned] + the lead-layer/width/computed-form classes) — AND the
discovery's inactive-focused rung surfaced a REAL, previously-
undocumented VISUAL PARITY GAP: the LIABILITIES-ACTIVE tablist
chrome (the Radix automatic-activation onFocus handler [react-tabs
dist: onFocus -> onValueChange when !isSelected && automatic] flips
the tab on a bare focus of the inactive trigger on BOTH sites; the
follow-up census tablistfocus-followup-v148.sh [the deliberate full
pointer-event sequence, the v120 form] confirmed: REF
data-[state=active]:bg-orange-100 text-orange-900 = the computed
pair rgb(255,237,213)/rgb(124,45,18) — the per-tab POLARITY THEMING
matching the liability card's own orange family; CLONE the SAME
green pair as the Assets tab — the Liabilities half LOST in the
clone; never pinned/shot/asserted before [every tablist census
measured the Assets-active default; the VLM shots never showed the
Liabilities tab; the v30 flip test asserts selection + panel, not
chrome]). THE REPAIR — net-worth-view.tsx the Liabilities
TabsTrigger className "data-[state=active]:bg-[#ffedd5]
data-[state=active]:text-[#7c2d12]" (the arbitrary-hex form — the
v5 G3 oklch-drift lesson; the cn() last-occurrence rule resolves
the pair over the base's green; the inactive/at-rest states + the
Assets path untouched). THE PIN (append-pin-v148.py — TEST A the
focus-visible ladder at 390: the at-rest rung [the v53 contract
re-asserted] -> the FOCUSED rung [the REAL focus({focusVisible:
true}) — the v35 S2 idiom; the ACTIVE Assets trigger's focus
activates nothing under Radix's onFocus handler — the CLEAN
keyboard-entry state; the v4 outline-none form none/1px/0px + the
VISIBLE ring composite via toContain + the ambient pair + the
chrome UNCHANGED — focus != hover] -> the blurred rung; TEST B the
LIABILITIES-ACTIVE chrome — the repair's regression pin: the
Liabilities tab clicked [the v6 form] -> the ORANGE pair + the
ambient shadow + the muted Assets twin -> the Assets tab clicked
back -> the at-rest contract re-established) — THE TDD DISCIPLINE
APPLIED LIVE: the RED run first (TEST A GREEN + TEST B RED with the
EXACT predicted diff [bg rgb(220,252,231) received vs rgb(255,237,
213) expected; color rgb(20,83,45) received vs rgb(124,45,18)
expected]) -> the repair -> the FULL REBUILD -> the GREEN run (both
tests); the authoritative --list: 352 in 24 files.

THE PIN-SANITY MUTATION — the ORANGE-PAIR-REMOVAL form: the
className prop's orange pair removed from the Liabilities trigger
(+ the standalone REBUILD) — the exact CSS-cleanup drift class the
pin exists to guard (the "consolidation" that reverts the per-tab
polarity theming — a regression invisible to every at-rest census):
**TEST B alone fails** [the failure diff EXACTLY the predicted two
axes {bg, color}], TEST A green (the different-element/different-
state immunity verified live); restored (git diff src/ = the repair
alone) + the FULL REBUILD + the post-restore regression **44
passed** (the full networth sweep) — ONE prior-pin collision found +
corrected: the v14 G2 icons test's activated-Liabilities-icon
assertion (the v14-era green-900 inference encoding the clone's
then-green-for-both construct, corrected to the reference-verified
rgb(124,45,18) [the orange-900 the icon inherits via currentColor
from the trigger's own active pair], documented in the test's own
comment; the case-insensitive re-sweep: the v14 icon test the SOLE
collision).

The ship chain: **352 e2e zero flakes** (97+95+81+82 = 355
executions = 352 unique — the +2 landing in ch3 [networth]; both
closed watches green through the chain); 35/35 smoke; the
screenshots **16/16 captured — 15 byte-identical + ONE WALL-CLOCK
delta** (07-add-item-modal.png: the modal's date field defaults to
the wall clock [budget-item-dialog.tsx:54 `const d = new Date()`] —
Nov 3 vs the committed Nov 2, the same re-commit convention as
v117/v122/v124/v131/v133/v135/v136/v138/v145; every seed-stamped
surface byte-identical under the canonical Oct 31 stamps); the dev
evidence 4/4 byte-identical + VLM-verified (the menu proof
{"url":"/income","docSW":390,"navLandmark":true}; the dev-shots
scripts derived v147 -> v148 with the version-swap-only
verification on both).

The v149 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence's next-oldest candidate —
**the v143-era DASHBOARD pair** (the DASHBOARD at desktop 1280x800
FULL-PAGE [the v61-era pair's surface family], last re-shot v143 — now
the oldest remaining [v143 < v144]; the pair's FOURTEENTH re-run bracket
[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119
-> v125 -> v131 -> v137 -> v143 -> v149] to be verified against the v143
lineage's own records before the derivation — the v143 plan's own
header records the THIRTEENTH ordinal on its 14-entry bracket [v61 the
original, one entry — 14 entries − the original = 13 re-runs],
consistent, no off-by-one this lineage; the v143 shots header carries
the FULL bracket form, the verification source),
(2) the axe-core watch at its next re-check point (only a 5.x wrapper
changes the calculus), (3) the npm-audit watch at its re-check point
(only a new advisory in the next/zod ranges changes the calculus),
(4) the deferred reference-write censuses (unchanged — out of bounds
under the v46 read-only rule), (5) the residual-class watch (both
flake classes CLOSED by the v136 dual-stack/localhost fix — the
watch continues in the standing form for any NEW class).

"""

text = io.open(PATH, encoding="utf-8").read()
if "## The v148 cycle" in text:
    print("SKIP: the v148 section already present")
    sys.exit(0)

anchor = "the standing form for any NEW class).\n\n## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)"
n = text.count(anchor)
if n != 1:
    print(f"FAIL: the insert anchor {n}x")
    sys.exit(1)

text = text.replace(anchor, "the standing form for any NEW class).\n\n" + SECTION + "## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)")
io.open(PATH, "w", encoding="utf-8").write(text)
print("OK: the v148 section + the v149 queue inserted (D6)")
