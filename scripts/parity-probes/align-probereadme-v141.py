#!/usr/bin/env python3
"""align-probereadme-v141.py — D6 of the v141 docs alignment: insert the
v141 cycle section + the v142 queue into scripts/parity-probes/README.md,
immediately after the v141 queue paragraph (the v140 cycle's own section
tail) and before the v138 section. D0 discipline: the insert anchor
verified 1-hit BEFORE any write; the script refuses on any miss."""
import io
import sys

PR = "scripts/parity-probes/README.md"
text = io.open(PR, encoding="utf-8").read()

# the unique anchor: the v141 queue's own tail (the v135-lineage-specific
# wording) + the section break before the v138 cycle header
anchor = (
    "the FULL bracket form, the verification source), (2) the axe-core watch\n"
    "at its next re-check point (only a 5.x wrapper changes the calculus),\n"
    "(3) the npm-audit watch at its re-check point (only a new advisory in\n"
    "the next/zod ranges changes the calculus), (4) the deferred\n"
    "reference-write censuses (unchanged — out of bounds under the v46\n"
    "read-only rule), (5) the residual-class watch (both flake classes\n"
    "CLOSED by the v136 dual-stack/localhost fix — the watch continues in\n"
    "the standing form for any NEW class).\n"
    "\n"
)
n = text.count(anchor)
if n != 1:
    print(f"ANCHOR MISS (the v141 queue tail): {n} hits")
    sys.exit(1)

SECTION = """## The v141 cycle (the v135-era LOGIN + CALCULATOR pair's THIRTEENTH re-run — Session 176)

The re-run cadence's second-pass next-oldest candidate: the v135-era
LOGIN + CALCULATOR pair — the LOGIN view + the CALCULATOR dialog at
desktop 1280x800 (the v129-era LOGIN + CALCULATOR pair's surface family,
the v59-era original), last re-shot v135 — now the oldest remaining
[v135 < v136 < v137 < v138]; the pair's THIRTEENTH re-run bracket
[v59 -> v66 -> v75 -> v81 -> v87 -> v93 -> v99 -> v105 -> v111 -> v117
-> v123 -> v129 -> v135 -> v141]; the SIXTY-FOURTH consecutive
queue/ledger agreement — the surface names verified against the v135
lineage's own records BEFORE the derivation (the v135 plan's own header:
the TWELFTH ordinal on its 13-entry bracket [v59 the original, one
entry — 13 entries − the original = 12 re-runs, no off-by-one this
lineage]; the v135 shots header carries the FULL bracket form, the
verification source; the surface-family name "the v129-era LOGIN +
CALCULATOR pair" preserved — the lineage's own designation, the
v139/v140 preservation precedent). **A PIN-ONLY cycle for src/ — zero
production-code changes (the eleventh PIN-ONLY cycle in the last
twelve) + one e2e pin (343 -> 344)**; the cycle's standing items: the
axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified), the
npm-audit watch at its thirty-second re-check (0 vulnerabilities
--omit=dev — the v110 bump holds [next 16.4.3 + zod 4.6.7]; the 16
moderate the accepted dev-only ESLint braces chain), the 135th standing
checks (ALL GREEN — the reference's four bugs live; the data census
clean on the FIRST reads; the clone's mobile menu VERIFIED WORKING the
135th consecutive time; zero overflow at 390 on all five views; the
seedcheck exact after the clone half).

The baseline GREEN ON THE FIRST CHAIN (the SAME-PERSISTED workspace —
the v140 environment held through the session boundary: node_modules 354
entries intact, BOTH chromium pairs [1200 + 1243] in the cache, the .env
[DATABASE_URL="file:../db/custom.db"] + db/ at the repo root intact with
the v140-cycle seed, the repo pulled to main @ 69f91be [the session-log
commit, +1 file docs/session_349.md]; the seedcheck EXACT
7/1850/2235/0/3/2 before any gate — under the env -u discipline, the
sandbox DATABASE_URL pollution live as documented; lint, typecheck,
108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e [346
executions = 343 unique, ZERO flakes], 35/35 smoke; the production-seam
audit clean; skills/ excluded).

The probe series derived from the v135 lineage (derive-v141-series.py —
the generic swaps incl. the SIX explicit session-token families
[refvlm/clonevlm + refcalc/clonecalc + reflogin/clonelogin arbit — the
tokens carry '135' without the 'v' prefix] + the history-correction
fragments [the era marker last-re-shot v129->v135 + the oldest-remaining
list v129..v132->v135..v138 + the queue source the v134 plan->the v140
plan + the agreement counter FIFTY-EIGHTH->SIXTY-FOURTH; the ordinal
TWELFTH->THIRTEENTH + the bracket extended in all four files], all
applied on the FIRST run, zero residual, line counts preserved
102/166/65/355 == the v135 lineage exactly; bash -n + node --check
clean) + the login-shots sub-series (derive-loginshots-v141.py — 30/30
preserved; both sides' login censuses byte-equal) + the two-half builder
(derive-build-twohalf-v141.py — the generic swap + the lesson-range bump
v92..v134->v92..v140 [the BARE range token] + the lineage-note fixup
"build-twohalf-v129.py"->"build-twohalf-v135.py" LAST) + the comparator
(derive-compare-v141.py — the generic swap incl. the EXPLICIT
/tmp/vlm135->/tmp/vlm141 log-path swap [the path token carries no 'v135'
substring — the derivation's own first-run miss, caught by the residual
check and fixed before any execution] + the provenance citations
re-pointed at the v135 measurement [the lineage ordinal TWELFTH->
THIRTEENTH; the records chain extended v105/v111/v117/v123/v129 ->
+v135]) + the verify script (derive-verify-twohalf-v141.py — the
lineage-citation chain extended v124..v134->v124..v140; the digests
UNCHANGED). The halves built + the TWO-block md5 contract verified by
the direct THREE-WAY python extraction (verify-twohalf-v141.py —
CALC_CENSUS_JS 61 lines md5 e1092d12d06677a4 + LOGIN_CENSUS_JS 36 lines
md5 9e5a52d2ab0f2ab9, byte-identical across arbit-v141.sh +
ref-arbit-v141.sh + clone-arbit-v141.sh — the v123/v129/v135 lineage
values VERBATIM, carried byte-identical through the version-swap
derivation).

The resource discipline applied between every half (the browser daemons
reaped BEFORE every half; both halves + both shot series executed with
first-attempt logins; the full logs captured by the runner redirection —
/tmp/vlm141/{ref,clone}-arbit-full.log, the comparator's documented
input paths).

The VLM pairwise run TWICE with full log capture (/tmp/vlm141/
vlm-pass{1,2}.log): pass 1 CALCULATOR DIFFERENT / LOGIN IDENTICAL; pass
2 CALCULATOR DIFFERENT / LOGIN IDENTICAL — the pair's documented
verdict-VARIATION family (the login verdict has varied
IDENTICAL/DIFFERENT across re-runs — v105/v129 IDENTICAL, v135 pass 2
DIFFERENT-with-the-sole-disproven-flag; here IDENTICAL in both passes).
The login passes' sole note the reference's own "Edit with Base44" FAB
(the PLATFORM-CHROME class) — DISPROVEN LIVE by base44-fab-arbit-v141.sh
(derived from the v135 form, swap-only verified: fabCount 0 +
bodyHasBase44 false on BOTH sides at 1280 /login — the standing
v97/v103/v108/v109/v115/v120/v123/v127/v129/v135 disproof form
re-confirmed). Every calculator flag in both passes in the documented
classes, arbitration-free (every flag's class already DOM-confirmed by
the census's own axes): the line-item row hover action buttons
"missing" on the clone the POINTER-POSITION/HOVER-STATE screenshot
artifact (the census actionsAtRest {opacity 0, btnCount 2} IDENTICAL
both sides — the reference's shot carries its hover-revealed buttons,
the clone's its at-rest hidden ones; the v129/v135 documented class);
the "Will update category total" note the SEED-DATA class (ref false vs
clone true — totalCard.hasWillUpdateSpan; the reference's Rent $25.00
equals its calculated total so the note hides; the clone's Rent $1850
vs the recalculated $25.00 shows it; the total-card layout flag its
consequence).

The both-sides census compared axis-by-axis (compare-v141-census.py):
106 axes — 97 identical + 9 documented-class deltas, ZERO new —
REPRODUCING the v135 census values EXACTLY (the same 106/97/9 split,
zero drift on every axis: the 9 documented = login card.border [the
zero-width computed-color artifact] + login card.shadow + calc
panel.shadow [the v3/v4 construct zero-layer-lead-count class] + the 5
close.* axes [the v99 finder artifact — clone-only present, the
asymmetry direction HOLDS] + calc totalCard.hasWillUpdateSpan [the
seed-data class]). The seedcheck exact after the clone half
(7/1850/2235/0/3/2). NO NEW CLONE GAP on the census axes.

THE PIN — the LOGIN SIGN-IN SUBMIT's OWN-HOVER LADDER at 1280 on /login
(PIN-ONLY — src/ ZERO changes, the eleventh PIN-ONLY cycle in the last
twelve; +1 e2e = 344): the candidate survey (the login + calculator
surfaces' interaction families swept against the specs' own assertions
— the SPEC-ALIAS lesson) found the calculator dialog's families ALL
HELD (the X's at-rest chrome by the v87 pin, the X's own-hover tint by
the v129 pin, the X's focus-visible ring by the v135 pin, the row
actions' focus-visible family by the v32 pin, the row actions'
own-hover tints by the v129 pin, the row's hover shadow + the actions'
reveal by the v45 pin, the panel/totalCard/row chrome by the v45
F2a/v59/v66 pins, the scrim by the v73 pin; the Add Item button INERT
by design [the v11 G4 record]) and the login view's submit own-hover
path entirely unpinned (the v7 pin the REST chrome [bg #0f172a, color
white, h 48]; the v9 pin the per-state geometry; the v25 pin the
focus-visible ring; the v45 F4 pin the REST shadow-sm; the v135 survey
the own-hover tint measured live [rgb(15,23,42)->rgb(30,41,59)] and the
clone's class confirmed — every submit census AT-REST or FOCUS; the
submit's own-hover END-STATE held by NO spec at ANY viewport; the
submit reachable at 1280 on BOTH sides — the center (640,677),
IDENTICAL coordinates both sides). THE CONSTRUCT: the TINTED contract
(the v129 active-hover form) — the submit carries hover:bg-[#1e293b]
(login-card.tsx:357), so the own-hover end-state is the bg transitioning
rgb(15,23,42)->rgb(30,41,59) under the submit's own hover with the
color/shadow family unchanged. The both-sides one-shot census
submithover-arbit-v141.sh (the v140 searchhover form adapted to the
submit axis: the STRUCTURAL finder [button[type=submit] with the "Sign
in" text — the form shared by both sites, the text cross-checked], the
(5,5)-parked ladder, the live-read center, READ-ONLY — a mouse MOVE on
a button dispatches no click and the logged-out surface holds no
session; the submit NEVER clicked — a click would submit the form)
measured the ladder CLEAN, NO GAP (the TINTED contract IDENTICAL both
sides at every rung; the deltas the documented construct classes alone:
the shadow LEAD-LAYER count [the v37 O1 note — the v3 three-slot vs the
TW v4 five-slot construct, every lead a 0px-spread shadow invisible by
construction; the VISIBLE pair byte-identical] + the borderColor
zero-width computed-color artifact [the card.border class — border-width
0px both sides, nothing renders]; the transition metadata IDENTICAL both
sides [all / 0.2s]). The pin appended (append-pin-v141.py — the at-rest
rung -> the SUBMIT-HOVERED rung {hoverMatch true + bg rgb(30,41,59) —
THE TINT + the UNCHANGED color/shadow family} -> the restored rung; the
V94-COLLISION-safe axis set; the STRUCTURAL finder; the submit never
clicked) GREEN on the first run; the authoritative --list: 344 in 24
files.

THE PIN-SANITY MUTATION — the HOVER-TINT-REMOVAL form:
hover:bg-[#1e293b] removed from the submit's className at
login-card.tsx:357 (the single className line; the component serves
EVERY auth mode's submit — the WIDER-FILE blast radius noted, the
sole-failure criterion verified on the FULL LOGIN-PARITY SWEEP ALONE) —
cascade-checked BY CONSTRUCTION (hover-scoped: the at-rest rung + the v7
rest-chrome pin + the v25 focus-visible pin + the v45 F4 REST
shadow-sm pin untouched [focus engages no hover utility; the pointer
parked away]) AND it simulates the exact drift the pin exists to guard
(the hover tint disappearing from the submit — the clone diverging from
the reference's tinted hover chrome). The SOLE FAILURE verified live —
1 failed [the pin alone] + 32 passed in the FULL login-parity sweep,
the failure diff EXACTLY the predicted hovered-rung axis (the untinted
bg "rgb(15, 23, 42)" received vs the pinned tinted "rgb(30, 41, 59)"
expected, hoverMatch true preserved, the color/txt axes untouched);
restored (git diff src/ = 0 lines) + the FULL REBUILD + the
post-restore regression 107 passed (login-parity 33 + calculator 20 +
items 54 — the v140/v135/v129 pins' different-file immunity verified
live).

The ship chain: **344 e2e zero flakes** (95+93+77+82 = 347 executions =
344 unique — the +1 landing in ch3 [login-parity]; both closed watches
green through the chain); 35/35 smoke; the screenshots **16/16 captured
— ALL byte-identical** (the same-day law: both this cycle and v140
captured Nov 1 UTC, every date-bearing surface rendering identically
under the persisted seed); the dev evidence 4/4 byte-identical +
VLM-verified (the menu proof {"url":"/income","docSW":390,
"navLandmark":true}; the dev-shots scripts derived v140 -> v141 with
the version-swap-only verification on both).

The v142 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence's SECOND-PASS next-oldest
candidate — **the v136-era NETWORTH + drill-down-DASHBOARD pair** (the
NETWORTH view + the DASHBOARD's drill-down EXPANDED state at desktop
1280x800, the v60-era networth+drill-down pair's surface family, last
re-shot v136 — now the oldest remaining [v136 < v137 < v138]; the
pair's THIRTEENTH re-run bracket [v60 -> v67 -> v76 -> v82 -> v88 ->
v94 -> v100 -> v106 -> v112 -> v118 -> v124 -> v130 -> v136 -> v142] to
be verified against the v136 lineage's own records before the
derivation — the v136 plan's own header records the TWELFTH ordinal on
its 13-entry bracket [v60 the original, one entry — 13 entries − the
original = 12 re-runs], consistent, no off-by-one this lineage; the
v136 shots header carries the FULL bracket form, the verification
source), (2) the axe-core watch at its next re-check point (only a 5.x
wrapper changes the calculus), (3) the npm-audit watch at its re-check
point (only a new advisory in the next/zod ranges changes the
calculus), (4) the deferred reference-write censuses (unchanged — out
of bounds under the v46 read-only rule), (5) the residual-class watch
(both flake classes CLOSED by the v136 dual-stack/localhost fix — the
watch continues in the standing form for any NEW class).

"""

text = text.replace(anchor, anchor + SECTION, 1)
io.open(PR, "w", encoding="utf-8").write(text)
print("D6 probe README: the v141 cycle section + the v142 queue inserted after the v141 queue tail")
