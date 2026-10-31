#!/usr/bin/env python3
"""align-probereadme-v137.py — D6 of the v137 docs alignment: insert the
v137 cycle section + the v138 queue into scripts/parity-probes/README.md,
immediately after the v137 queue paragraph (the v136 cycle's own section
form) and before the v121 section. D0 discipline: the insert anchor
verified 1-hit BEFORE any write; the script refuses on any miss."""
import io
import sys

PR = "scripts/parity-probes/README.md"
text = io.open(PR, encoding="utf-8").read()

anchor = (
    "CLOSED by the v136 dual-stack/localhost fix — the watch continues in\n"
    "the standing form for any NEW class).\n"
    "\n"
)
n = text.count(anchor)
if n != 1:
    print(f"ANCHOR MISS (the v137 queue tail): {n} hits")
    sys.exit(1)

SECTION = """## The v137 cycle (the v131-era DASHBOARD pair's TWELFTH re-run — Session 172)

The re-run cadence's next-oldest candidate: the v131-era DASHBOARD pair —
the DASHBOARD at desktop 1280x800 FULL-PAGE (the Budget Guidelines card +
the Quick-Action row below the fold), the v125-era pair's surface family,
last re-shot v131 — now the oldest remaining [v131 < v132]; the pair's
TWELFTH re-run bracket [v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101
-> v107 -> v113 -> v119 -> v125 -> v131 -> v137]; the SIXTIETH
consecutive queue/ledger agreement — the surface names verified against
the v131 lineage's own records BEFORE the derivation (the v131 plan's own
header: the ELEVENTH ordinal on its 12-entry bracket [v61 the original,
one entry — no off-by-one this lineage]; the v131 shots header carries
the FULL bracket form — the documented verification source). **A PIN-ONLY
cycle for src/ — zero production-code changes (the seventh PIN-ONLY cycle
in the last eight) + one e2e pin (339 -> 340)**; the cycle's standing
items: the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified),
the npm-audit watch at its twenty-eighth re-check (0 vulnerabilities
--omit=dev — the v110 bump holds [next 16.4.3 + zod 4.6.7]; the 16
moderate the accepted dev-only ESLint braces chain), the 131st standing
checks (ALL GREEN — the reference's four bugs live; the data census
clean on the FIRST reads; the clone's mobile menu VERIFIED WORKING the
131st consecutive time; zero overflow at 390 on all five views; the
seedcheck exact after the clone half).

The baseline GREEN ON THE FIRST CHAIN (the RE-PROVISIONED workspace —
the repo re-cloned from main @ 907b9ed, the v108 FRESH-CLONE provisioning
end-to-end [npm ci 354 entries, the zod 4.6.7 extraction intact, BOTH
chromium pairs 1200 + 1243 installed — the fresh cache held only the OLD
1200 pair, the dry-run-is-a-location-report lesson re-verified, the .env
[DATABASE_URL="file:../db/custom.db"] + db/ at the repo root + db:push +
db:seed, the seedcheck EXACT 7/1850/2235/0/3/2 before any gate]; lint,
typecheck, 108/108 unit, build [robots + sitemap prerendered], the
4-chunk e2e [342 executions = 339 unique, ZERO flakes — both v136-closed
watch classes green through the chain: the empty-states G6 fixture
attaching its Secure cookie under the dual-stack/localhost config, the
not-found resolver race dead], 35/35 smoke; the production-seam audit
clean; skills/ excluded).

The probe series derived from the v131 lineage (derive-v137-series.py —
the generic swaps incl. the FOUR explicit session-token families [refvlm/
clonevlm + refar/clonear arbit] + NINE history-correction fragments [the
era marker v125-era -> v131-era + last re-shot v125 -> v131 + the
oldest-remaining list [v125 < ... < v130] -> [v131 < v132]; the ordinal
ELEVENTH -> TWELFTH + the bracket extended [-> v125 -> v137] -> [-> v125
-> v131 -> v137]; the agreement ordinal FIFTY-FOURTH -> SIXTIETH; the
re-proves chain v101-v125 -> v101-v131; the arbit verdict/census
provenance re-pointed at the v131 measurement], all applied on the FIRST
run, zero residual, line counts preserved 57/42/45/258 == the v131
lineage exactly; bash -n + node --check clean). The two-half builder
derived (derive-build-twohalf-v137.py — the lesson-range bump
v92..v130 -> v92..v136 as the BARE range token [the v131 lineage's
TWOHALF_NOTE wraps the phrase across two lines, the within-line-edit
form] + the lineage-note fixup LAST [the source pointer re-pointed at
build-twohalf-v131.py]). The comparator derived (derive-compare-v137.py
— the explicit /tmp/vlm131 -> /tmp/vlm137 log-path swap + the
provenance citations re-pointed at the v131 measurement). The halves
built + the THREE-block md5 contract verified by the direct THREE-WAY
python extraction (verify-twohalf-v137.py — ARBIT_G 61 lines md5
b500dd299e5e9a94eaf07b29facc69db + ARBIT_Q 58 lines md5
da04e9954976eb58d9aff2b95d2dcfc6 + ARBIT_X 25 lines md5
7a381755a22ce55c62f70a053f826852, byte-identical across arbit-v137.sh +
ref-arbit-v137.sh + clone-arbit-v137.sh — **the v131 lineage's own
recorded digests, carried byte-identical through the version-swap
derivation**).

The VLM pairwise run TWICE with full log capture (/tmp/vlm137/vlm-pass{1,2}.log):
pass 1 IDENTICAL / pass 2 IDENTICAL — **the CLEANEST PAIR FORM** (the
v131/v125 verdict form re-confirmed: zero layout/style flags BOTH
passes, NO DOM arbitration needed this cycle). Every flag in both passes
in the documented classes: the PCT/seed-data classes (the hero
allocation pct + balance, the stat amounts/counts, the donut proportions
+ legend) + the pass-2 nav-highlight (the v56 SUPERSET class) + the
avatar letter (the USER-IDENTITY class) — exactly the v131 cycle's own
flag set. The both-sides census compared axis-by-axis
(compare-v137-census.py): **154 axes — 144 identical + 10
documented-class deltas, ZERO new — REPRODUCING the v131 census values
EXACTLY** (the same 154/144/10 split, zero drift on every axis; the 10
documented = the v66 INVISIBLE shadow lead-layer count + the v61
label-lesson x6 [the finder catches the clone's WRAPPER (400/rgb(10,10,
10)) while the ref's is the leaf itself (500/rgb(26,58,46)); the clone's
LEAF span identical, pinned green by the v61 F3 + v107 F4 pins] + the
v77 mechanism class x3 [grid mt 0px-vs-32px with the rendered gap
byte-identical — cardBottom/gridTop/gap 340 all matching; the
class-string itself differs by construction]). The seedcheck exact
after the clone half (7/1850/2235/0/3/2).

THE PIN (the INTERACTIVE STAT CARD's OWN-HOVER SHADOW LADDER at 1280 —
PIN-ONLY, +1 e2e = 340): the candidate survey found the stat card's
shadow path entirely unpinned (the v131 pin the own-hover REVEAL ladder
[the radial + the chevron opacity]; the v45 F3b pin the QUICK-ACTION
TWIN's LIVE hover:shadow-lg layers [that card carries NO inline
boxShadow, so the utility engages]; the v51 F2 pin the AT-REST card
chrome at 390 incl. the inline rest shadow; the stat card's hovered
shadow held by NO spec at ANY viewport). THE CONSTRUCT UNDER TEST: the
stat card carries BOTH the hover:shadow-lg utility AND the INLINE
boxShadow rgba(0, 0, 0, 0.06) 0px 4px 20px — the inline style beats the
utility in the cascade (the v43 category-row precedent), so the expected
hovered end-state is the INLINE PERSISTENCE (the shadow unchanged across
the ladder's rungs, the hover:shadow-lg inert) — the exact opposite of
the v45 F3b quick-action twin. The both-sides one-shot census
stathovershadow-arbit-v137.sh (the v131 stathover form adapted to the
shadow axes: the v131 structural card finder, the (5,5)-parked ladder,
the live-read center [both sides (440,400)], the two-arg mouse move,
READ-ONLY per the v46 rule, the full computed boxShadow string never
truncated) measured the ladder CLEAN — NO GAP: the at-rest rung
{cardHover false, boxShadow rgba(0, 0, 0, 0.06) 0px 4px 20px 0px} ->
the hovered rung {cardHover true, boxShadow UNCHANGED — the inline
persistence axis} -> the restored rung — IDENTICAL both sides at every
rung; the deltas the documented construct classes alone (the class token
[REF false / CLONE true — never a pin axis, the XgridCls precedent] +
the transition metadata [REF all 0s / CLONE all 0.2s — the v89 family's
own form]). The pin appended (append-pin-v137.py — the at-rest rung ->
the REAL-hover rung {cardHover true + the unchanged inline boxShadow} ->
the restored rung; the V94-COLLISION-safe axis set; the structural
finder; the card NEVER clicked) GREEN on the first run; the
authoritative --list: 340 in 24 files.

THE PIN-SANITY MUTATION — the MUTATION-FAMILY ROTATION (the v116 lesson
re-applied): the first-chosen INLINE-VALUE form (rgba(0, 0, 0, 0.06) ->
rgba(0, 0, 0, 0.07) at dashboard-view.tsx:581) was run first and
REJECTED as a cascade — the full dashboard sweep read 2 failed (the
v137 pin red at the boxShadow axis, exactly the predicted line, AND the
v51 F2 pin red at the same shared-VALUE axis: the mobile 390 at-rest
census asserts the same inline rest shadow at dashboard.spec.ts:2057 —
the two pins read the SAME rendered axis of the SAME element at
different viewports, no line-scoping can separate them; the
sole-failure discipline demands a cascade-free form). THE ROTATED FORM:
the IMPORTANT-MODIFIER mutation (hover:shadow-lg -> hover:shadow-lg! at
dashboard-view.tsx:578 — the Tailwind v4 important suffix, making the
utility BEAT the inline style under hover): cascade-free BY CONSTRUCTION
(hover-scoped — the at-rest rungs + the v51 F2 390 at-rest census + the
v131 radial/chevron axes + the v45 F3b/v125/v107 quick-action elements
all untouched) AND it simulates the exact drift the pin exists to guard
(the utility going LIVE under hover — the clone diverging from the
reference's inline-persistence chrome). The SOLE FAILURE verified live —
1 failed [the pin alone] + 51 passed in the FULL dashboard sweep, the
failure diff EXACTLY the predicted hovered-rung axis (the TW v4 LIVE
shadow-lg construct — the 4 transparent lead slots + the visible
rgba(0, 0, 0, 0.1) 0px 10px 15px -3px pair — received vs the inline
persistence expected, cardHover true preserved, the at-rest + restored
rungs GREEN under the mutation); restored (git diff src/ = 0 lines) +
the FULL REBUILD + the post-restore regression 142 passed (dashboard 52
+ networth 39 + items 51 — the v136/v134 pins' different-file immunity
verified live).

The ship chain: **340 e2e zero flakes** (93+93+75+82 = 343 executions =
340 unique — the count derived authoritatively via --list before any
chunk ran; both closed watches green through the chain); 35/35 smoke;
the screenshots **16/16 BYTE-IDENTICAL** (the same-day-seed law — this
workspace and the v136 cycle both seeded Oct 31 UTC, every date-bearing
surface rendering identically); the dev evidence 4/4 byte-identical +
VLM-verified (the menu proof: the sheet closed, the heading "Income",
the top bar + toggle + brand; the dev-shots scripts derived v136 -> v137
with the version-swap-only verification on both).

THE DOCS REPAIR (this cycle's own finding): the SKILL's project_state
line was left STALE at 338 by the v136 cycle's D4a — its anchor
("108/338/35") missed the project_state line's own format ("338 e2e
tests") and instead bumped the Session 170 row's historical status cell
(338 -> 339); this cycle's D4 repairs both (the state line to the
current 340, a two-count jump through the v136 pin; the Session 170 row
restored to the v135 cycle's own shipped 338).

The v138 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence rotates to the next-oldest
candidate after the v131-era DASHBOARD pair (the v132-era MOBILE-TWINS
pair — the /NETWORTH view + the DASHBOARD, both FULL-PAGE at mobile
390x844, last re-shot v132 — now the oldest remaining [v132]; the pair's
TWELFTH re-run bracket [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 →
v108 → v114 → v120 → v126 → v132 → v138] to be verified against the
v132 lineage's own records before the derivation — the v132 plan's own
header records the ELEVENTH ordinal on its 12-entry bracket [v62/v63 the
original pair, one entry], consistent, no off-by-one this lineage; the
v132 shots header carries the FULL bracket form, the verification
source), (2) the axe-core watch at its next re-check point (only a 5.x
wrapper changes the calculus), (3) the npm-audit watch at its re-check
point (only a new advisory in the next/zod ranges changes the calculus),
(4) the deferred reference-write censuses (unchanged — out of bounds
under the v46 read-only rule), (5) the residual-class watch (both flake
classes CLOSED by the v136 dual-stack/localhost fix — the watch continues
in the standing form for any NEW class).

"""
text = text.replace(anchor, anchor + SECTION)
io.open(PR, "w", encoding="utf-8").write(text)
print("D6 probe README: the v137 section + the v138 queue inserted")
