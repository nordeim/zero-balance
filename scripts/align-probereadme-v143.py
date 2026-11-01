#!/usr/bin/env python3
"""D6 — the probe README alignment for the v143 cycle: insert the v143
section (Session 178) between the v143 queue's end and '## The v138 cycle'
(each cycle section ends with the NEXT cycle's queue — the v142 section's
tail IS the v143 queue; the new v143 section carries the v144 queue)."""
import io
import sys

PATH = "scripts/parity-probes/README.md"

SECTION = """## The v143 cycle (the v137-era DASHBOARD pair's THIRTEENTH re-run — Session 178)

The re-run cadence's second-pass next-oldest candidate: the v137-era
DASHBOARD pair — the DASHBOARD at desktop 1280x800 FULL-PAGE (the Budget
Guidelines card + the Quick-Action row below the fold — the v125-era
dashboard pair's surface family), last re-shot v137 — now the oldest
remaining [v137 < v138]; the pair's THIRTEENTH re-run bracket [v61 ->
v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119 -> v125
-> v131 -> v137 -> v143]; the SIXTY-SIXTH consecutive queue/ledger
agreement — the surface names verified against the v137 lineage's own
records BEFORE the derivation (the v137 plan's own header: the TWELFTH
ordinal on its 13-entry bracket [v61 the original, one entry — 13
entries − the original = 12 re-runs, no off-by-one this lineage]; the
v137 shots header carries the FULL bracket form, the verification
source). **A PIN-ONLY cycle for src/ — zero production-code changes
(the thirteenth PIN-ONLY cycle in the last fourteen) + one e2e pin
(345 -> 346)**; the cycle's standing items: the axe watch (NO DRIFT —
4.14.0 holds, the v68 dedupe verified), the npm-audit watch at its
thirty-fourth re-check (0 vulnerabilities --omit=dev — the v110 bump
holds [next 16.4.3 + zod 4.6.7]; the 16 moderate the accepted dev-only
ESLint braces chain), the 137th standing checks (ALL GREEN — the
reference's four bugs live; the data census clean on the FIRST reads;
the clone's mobile menu VERIFIED WORKING the 137th consecutive time;
zero overflow at 390 on all five views; the seedcheck exact after the
clone half).

The baseline GREEN ON THE FIRST CHAIN (the SAME-PERSISTED workspace —
the v142 environment held through the session boundary: node_modules 354
entries intact, BOTH chromium pairs [1200 + 1243] in the cache, the .env
[DATABASE_URL="file:../db/custom.db"] + db/ at the repo root intact with
the v142-cycle seed, the repo pulled to main @ a999f9b [the session-log
commit, +1 file docs/session_357.md]; the seedcheck EXACT
7/1850/2235/0/3/2 before any gate — under the env -u discipline, the
sandbox DATABASE_URL pollution live as documented; lint, typecheck,
108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e [348
executions = 345 unique, ZERO flakes], 35/35 smoke; the production-seam
audit clean; skills/ excluded).

The probe series derived from the v137 lineage (derive-v143-series.py —
the generic swaps incl. the FOUR explicit session-token families
[refvlm/clonevlm + refar/clonear arbit — the tokens carry '137' without
the 'v' prefix] + the history-correction fragments [the era marker
v131-era->v137-era + last re-shot v131->v137 + the oldest-remaining list
[v131 < v132]->[v137 < v138] + the ordinal TWELFTH->THIRTEENTH + the
bracket extended in all four files + the agreement ordinal
SIXTIETH->SIXTY-SIXTH + the re-proves chain v101-v131->v101-v137 + the
arbit verdict/census provenance re-pointed at the v137 measurement], all
applied on the FIRST run, zero residual, line counts preserved
57/42/45/258 == the v137 lineage exactly; bash -n + node --check clean;
the pre-derivation sweep re-confirmed the v137 derivation's own finding
— all era tokens confined to the file headers, the sole in-body
exception the compare script's own PAIR console.log line, corrected) +
the two-half builder (derive-build-twohalf-v143.py — the generic swap +
the lesson-range bump v92..v136->v92..v142 [the BARE range token] + the
lineage-note fixup "verbatim from build-twohalf-v131.py"->"verbatim from
build-twohalf-v137.py" LAST) + the comparator (derive-compare-v143.py —
the generic swap incl. the EXPLICIT /tmp/vlm137->/tmp/vlm143 log-path
swap [the path token carries no 'v137' substring] + the provenance
citations re-pointed at the v137 measurement [the lineage ordinal
TWELFTH->THIRTEENTH; the records chain v131->v137]) + the verify script
(derive-verify-twohalf-v143.py — the generic swap only, the v137 form
carrying no citation chain) + the 137th standing pair
(derive-standing-v143.py — derived from the v136 pair, three token
families [the ordinal 136th->137th th->th plain replace, the bare
session names ref136/clone136->ref137/clone137, the version
v136->v137; the citation extended with v142's 135th->136th],
normalize-back diff clean, zero old tokens, line counts preserved
119/74). The halves built + the THREE-block md5 contract verified by the
direct THREE-WAY python extraction (verify-twohalf-v143.py — ARBIT_G 61
lines md5 b500dd299e5e9a94eaf07b29facc69db + ARBIT_Q 58 lines md5
da04e9954976eb58d9aff2b95d2dcfc6 + ARBIT_X 25 lines md5
7a381755a22ce55c62f70a053f826852, byte-identical across arbit-v143.sh +
ref-arbit-v143.sh + clone-arbit-v143.sh — **the within-cycle contract
form: the census JS blocks' view-label tokens carry the version, so the
digests differ from the v137 cycle's by construction**).

The resource discipline applied between every half (the browser daemons
reaped BEFORE every half; both halves + both shot series executed with
first-attempt logins; the full logs captured by the runner redirection —
/tmp/vlm143/{ref,clone}-arbit.log, the comparator's documented input
paths).

The VLM pairwise run TWICE with full log capture
(/tmp/vlm143/vlm-pass{1,2}.log): pass 1 IDENTICAL / pass 2 IDENTICAL —
**the CLEANEST PAIR FORM (the v131/v125/v137 precedent class — the
pair's documented stable-identical verdict family; pass 2 zero style
flags: "No visual differences found in the Budget Guidelines or Quick
Actions sections... identical between the reference and the clone")**.
The pass-1 flags, all in the documented classes: the data differences
(the SEED-DATA classes — the Net Zero Goal allocation %/balance, the
Breakdown totals, the stat cards' amounts/counts, the donut
proportions), the nav-highlight (the v56 SUPERSET class — "Dashboard"
highlighted green in the clone), the avatar letter U vs D (the
USER-IDENTITY data class), and the FAB claim ("The 'Edit with Base44'
floating action button/widget present in the top-right of the reference
image is completely absent from the clone" — the PLATFORM-CHROME class,
**DISPROVEN LIVE by base44-fab-arbit-v143.sh**: fabCount 0 +
bodyHasBase44 false on BOTH sides, the flagged dashboard surface, 1280,
logged-in — the standing v97/v103/v108/v109/v115/v120/v123/v127/v129/
v135/v141/v142 disproof form re-confirmed).

The both-sides census compared axis-by-axis (compare-v143-census.py):
**154 axes — 144 identical + 10 documented-class deltas, ZERO new —
REPRODUCING the v137 census values EXACTLY** (the same 154/144/10
split, zero drift on every axis: the 10 documented = the v66 INVISIBLE
shadow lead-layer count class [Gcard.shadow — the clone's transparent
leads + the v4 5-slot construct vs the reference's 2-slot form, the
VISIBLE layers identical] + the v61 label-lesson ×6 [Qcards[*].label.
color + fw — the census finder catches the clone's WRAPPER
(400/rgb(10,10,10)) while the ref's is the leaf itself (500/
rgb(26,58,46)) — the clone's LEAF span carries the identical chrome,
pinned green by the v61 F3 pin + the v107 F4 label-leaf pin] + the v77
mechanism class ×2 [Qgrid.mt + XgridMt — explicit mt-8 on the clone vs
structural spacing on the ref, rendered geometry byte-identical] + the
gridCls site-source class [the class string itself, never pinned]); the
rendered-geometry hard assertions green (cardBottom 1122 + gridTop 1462
+ gap 340 + gridParentMt 0px — byte-identical both sides). The seedcheck
exact after the clone half (7/1850/2235/0/3/2). NO NEW CLONE GAP on the
census axes.

THE PIN — the DASHBOARD QUICK-ACTION CARDS' FOCUS-VISIBLE LADDER at
1280 on /dashboard (PIN-ONLY — src/ ZERO changes, the thirteenth
PIN-ONLY cycle in the last fourteen; +1 e2e = 346): the candidate survey
(the dashboard full-page pair's interaction families swept against the
specs' own assertions — the SPEC-ALIAS lesson) found the
Guidelines-card half's families ALL HELD (the card box + header + the
FIRST tile + the STRETCH contract by the v61 F2 pin; the interior TEXT
family + the tiles 2/3 chrome + the icons' viewBox by the v77 pin; the
row's own grid + the Spending card's box/header by the v101 pin; the
tiles' 390 mobile twin by the v51 F4 pin; the cross-row gap by the v83
F4 pin) and the Quick-Action half's families: the at-rest geometry by
the v61 F3 pin; the glyphs by the v107 pin; the transition TIMING
metadata by the v95 pin; the hover:shadow-lg layers by the v45 F3b pin;
the HOVER end-state ladder (the tile scale + the plus opacity + the
restore) by the v125 pin — **the FOCUS-VISIBLE family held by NO spec
at ANY viewport** (the suite-wide survey: dashboard.spec.ts's focus
pins cover the header Add Item button's four-layer composite (v35 S2) +
the Tab-order structural walk's tag/role/name/tabindex axes (v40 F1) —
no spec asserts the QA cards' ring; the stat cards' focus path is
SUPERSET-only [the reference's 304×210 stat cards are INERT divs — the
v40 F1 census records the clone's div[role=button]+tabIndex=0 superset],
not a both-sides axis; the QA cards are real BUTTONS on BOTH sites [the
v40 F1 walk: the three quick-action cards are Tab stops on both sides])
— the strongest form: never-pinned at ANY viewport, both-sides
measurable (real buttons on both sites), on the PAIR'S OWN SURFACE (the
Quick-Action row below the fold), at the pair's own 1280 viewport, the
pair's primary interactive elements (the guidelines tiles are static
divs). THE CONSTRUCT — the UA-DEFAULT RING contract: the clone's
QuickActionCard carries NO focus classes (dashboard-view.tsx:885 —
group rounded-2xl border p-6 text-left transition-all duration-200
hover:shadow-lg), so its expected focused end-state is the engine's own
ring (outlineStyle none->auto + outlineWidth medium->1px +
outlineOffset 0px) with the card chrome UNCHANGED under focus (the
shadow-lg is :hover-only — focus != hover; the tile scale + the plus
opacity are group-hover-only — both stay at-rest under focus); the
reference's cards MEASURED by the census (the same contract — its cards
likewise classless-on-focus buttons). The both-sides one-shot census
focusqa-arbit-v143.sh (the v142 drillhover form adapted to the focus
ladder: the STRUCTURAL finder [the button whose trimmed text starts
with "Add Income" — both sites' first QA card, the v125 pin's own finder
family], the REAL Chromium focus({focusVisible:true}) engagement [the
v35 S2 idiom — the REAL FocusOptions member; the v25 plain-focus lesson
does not apply to the focusVisible form], the (5,5)-parked pointer,
READ-ONLY — focus() dispatches no click; the cards NEVER clicked [they
open the Add Item dialog, OUT OF BOUNDS under the v46 rule], the blur
restore, the tile/plus state read alongside the ring axes) measured the
ladder on BOTH sides and found **NO GAP** (the AT-REST rung:
{focused false, fv false, outlineStyle "none", outlineWidth "3px" [the
CSS-wide medium], outlineOffset "0px", boxShadow "none", tileScale
"none", plusOpacity "0.5"} — IDENTICAL both sides; the FOCUSED rung:
{focused true, fv true, outlineStyle "auto", outlineWidth "1px",
outlineOffset "0px", boxShadow "none" UNCHANGED — focus != hover, the
shadow-lg NOT engaged, tileScale "none" + plusOpacity "0.5" UNCHANGED —
the group-hover reveals NOT engaged} — IDENTICAL both sides; the BLURRED
rung: the at-rest contract re-established on every axis — IDENTICAL
both sides; the sole delta the outlineColor computed form [REF
rgba(10, 10, 10, 0.5) vs CLONE lab(2.74175 0 0.00000596046 / 0.5) — the
SAME rendered near-black-at-50% foreground, the v4 color computed-form
family, never pinned per the v95 discipline; under outline-style:auto
the engine draws its own ring]). The pin appended (append-pin-v143.py —
the at-rest rung -> the FOCUSED rung {focused true + fv true +
outlineStyle "auto" + outlineWidth "1px" + outlineOffset "0px" — THE
UA-DEFAULT RING CONTRACT + boxShadow "none" + tileScale "none" +
plusOpacity "0.5" UNCHANGED — the focus != hover family} -> the blurred
rung (the at-rest contract re-established); the V95-COLLISION-safe axis
set [the outlineColor computed form deliberately NOT pinned — the v4
lab() family's own form]; the V125-COLLISION-safe family [the tile/plus
axes asserted at their AT-REST values only]; the STRUCTURAL finder; the
card NEVER clicked; GREEN on the first run; the authoritative --list:
346 in 24 files).

THE PIN-SANITY MUTATION — the RING-REMOVAL form: focus-visible:
outline-none added to the QuickActionCard's className at
dashboard-view.tsx:885 (the single construct; the component serves ALL
THREE quick-action cards — the WIDER-FILE blast radius noted, the
sole-failure criterion verified on the FULL DASHBOARD SWEEP ALONE) —
**the exact Tailwind-v4-refactor drift class the pin exists to guard**
(the "cleanup" that kills the keyboard ring — an a11y regression
invisible to every at-rest census): the at-rest rung UNCHANGED (the
utility is focus-visible-scoped — the v61 F3/v107/v95/v125 at-rest
censuses stay GREEN), but the FOCUSED rung's ring goes NONE (the TW v4
outline-none computes outline-style: none — the ring never renders).
**The SOLE FAILURE verified live — 1 failed [the pin alone] + 53 passed
in the FULL dashboard sweep**, the failure diff EXACTLY the predicted
focused-rung ring axis (outlineStyle "none" received vs the pinned
"auto" expected — the width/offset + the focus != hover axes
preserved); the v45 F3b + v125 hover pins GREEN (the hover pseudo-class
untouched by a focus-visible-scoped mutation); restored (git diff src/ =
0 lines) + the FULL REBUILD + the post-restore regression **94 passed**
(dashboard 53 + networth 40 + setup — the v125/v131/v137/v142 dashboard
pins' same-file immunity verified live).

The ship chain: **346 e2e zero flakes** (95+95+77+82 = 349 executions =
346 unique — the +1 landing in ch2 [dashboard]; both closed watches
green through the chain); 35/35 smoke; the screenshots **16/16 captured
— ALL byte-identical** (the same-day law: both this cycle and v142
captured Nov 1 UTC, every date-bearing surface rendering identically
under the persisted seed); the dev evidence 4/4 byte-identical +
VLM-verified (the menu proof {"url":"/income","docSW":390,
"navLandmark":true}; the dev-shots scripts derived v142 -> v143 with
the version-swap-only verification on both).

The v144 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence's SECOND-PASS next-oldest
candidate — **the v138-era MOBILE-TWINS pair** (the /networth view +
the DASHBOARD, both FULL-PAGE at mobile 390x844 [the v62/v63-era
twins' surface family], last re-shot v138 — now the oldest remaining
[v138]; the pair's THIRTEENTH re-run bracket [v62/v63 -> v69 -> v78 ->
v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120 -> v126 -> v132 ->
v138 -> v144] to be verified against the v138 lineage's own records
before the derivation — the v138 plan's own header records the TWELFTH
ordinal on its 13-entry bracket [v62/v63 the original pair, one entry —
13 entries − the original = 12 re-runs], consistent, no off-by-one this
lineage; the v138 shots header carries the FULL bracket form, the
verification source), (2) the axe-core watch at its next re-check point
(only a 5.x wrapper changes the calculus), (3) the npm-audit watch at
its re-check point (only a new advisory in the next/zod ranges changes
the calculus), (4) the deferred reference-write censuses (unchanged —
out of bounds under the v46 read-only rule), (5) the residual-class
watch (both flake classes CLOSED by the v136 dual-stack/localhost fix —
the watch continues in the standing form for any NEW class).

"""

text = io.open(PATH, encoding="utf-8").read()
if "## The v143 cycle" in text:
    print("SKIP: the v143 section already present")
    sys.exit(0)

anchor = "the standing form for any NEW class).\n\n## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)"
n = text.count(anchor)
if n != 1:
    print(f"FAIL: the insert anchor {n}x")
    sys.exit(1)

text = text.replace(anchor, "the standing form for any NEW class).\n\n" + SECTION + "## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)")
io.open(PATH, "w", encoding="utf-8").write(text)
print("OK: the v143 section + the v144 queue inserted (D6)")
