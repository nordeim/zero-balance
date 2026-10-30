#!/usr/bin/env python3
"""align-probereadme-v135.py — D6 of the v135 docs alignment: insert the
v135 cycle section + the v136 queue into scripts/parity-probes/README.md,
immediately after the v135 queue paragraph (the v134 cycle's own section
form) and before the v121 section. D0 discipline: the insert anchor
verified 1-hit BEFORE any write; the script refuses on any miss."""
import io
import sys

PR = "scripts/parity-probes/README.md"
text = io.open(PR, encoding="utf-8").read()

anchor = (
    "the not-found:111 flake watch (the v134-documented intermittent — if it\n"
    "recurs, the full error capture + trace escalation is the documented step).\n"
)
n = text.count(anchor)
if n != 1:
    print(f"ANCHOR MISS (the v135 queue tail): {n} hits")
    sys.exit(1)
# the section goes AFTER the queue's trailing blank line, before the v121 section
insert_after = anchor + "\n"

SECTION = """## The v135 cycle (the v129-era LOGIN + CALCULATOR pair's TWELFTH re-run — Session 170)

The re-run cadence's next-oldest candidate: the v129-era LOGIN + CALCULATOR
pair — the LOGIN view + the CALCULATOR dialog at desktop 1280x800, the
v59-era pair's surface family, last re-shot v129 — now the oldest remaining
[v129 < v130 < v131 < v132]; the pair's TWELFTH re-run bracket [v59 -> v66
-> v75 -> v81 -> v87 -> v93 -> v99 -> v105 -> v111 -> v117 -> v123 -> v129
-> v135]; the FIFTY-EIGHTH consecutive queue/ledger agreement — the surface
names verified against the v129 lineage's own records BEFORE the derivation
(the v129 plan's own F3 record: the ELEVENTH ordinal on its 12-entry
bracket [v59 the original, one entry — no off-by-one this lineage]; the
v129 shots header carries the FULL bracket form — the documented
verification source). **A REPAIR + PIN cycle for src/ — the first src/
change since v129 (the five-cycle PIN-ONLY run v130..v134 ends at v134)** +
one e2e pin; the cycle's standing items: the axe watch (NO DRIFT — 4.14.0
holds, the v68 dedupe verified), the npm-audit watch at its twenty-sixth
re-check (0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod
4.6.7]), the 129th standing checks (ALL GREEN — the reference's four bugs
live; the data census clean on the FIRST reads; the clone's mobile menu
VERIFIED WORKING the 129th consecutive time; zero overflow at 390 on all
five views; the seedcheck exact after the clone half).

The baseline GREEN — **THE FLAKE EPISODE escalated: BOTH intermittents
captured for the first time** (the CONTINUING workspace; lint, typecheck,
108/108 unit, build [robots + sitemap prerendered], 337 e2e [341
executions in 4 chunks = 336 spec + 1 setup — the count derived
authoritatively via --list before any chunk ran: 93/91/74/82], 35/35
smoke; the production-seam audit clean + the v134 pin verified in place).
**The not-found:111 recurrence** (the v134-documented intermittent — the
single-test transient form, 1 failed + 81 passed): the documented
escalation step executed — the isolated spec 7/7, the traced re-run 82/82,
a bounded capture loop 4 clean full-chunk runs, 3/3 instrumented runs
clean (the webServer command wrapped so the standalone server's output
lands in a log; no crash output exists to examine). **THE CAPTURE:
`page.goto: net::ERR_CONNECTION_REFUSED at http://localhost:3100/`** —
the test died at the NAVIGATION, not the head assertions; the v134
mechanism hypothesis ("a transient empty/error head") DISPROVEN. **THE
VERIFIED ASYMMETRY**: the standalone server binds 0.0.0.0 (IPv4-only;
measured live: 127.0.0.1:3100 -> 200, [::1]:3100 -> connection REFUSED) —
the "localhost" name resolution can race ::1-first and surface the RST as
ERR_CONNECTION_REFUSED (one goto refused, the next fine seconds later: a
resolver race, not a dead listener; the same run's `AggregateError:
apiRequestContext.get: connect ECONNREFUSED ::1:3100` independently
confirms the ::1 attempts). **THE FIX (a test-config change, not src/ —
playwright.config.ts: BASE_URL pinned to the IPv4 literal
http://127.0.0.1:${PORT})** — removing the class wholesale; the full 337
e2e re-verified green under the fix. **The empty-states:85 recurrence** (a
SECOND intermittent, captured WITH its full error detail — the
retained-on-failure trace survived): `TypeError: Cannot read properties of
undefined (reading 'map')` at the G6 fixture line — **the trace's network
entry shows the `GET /api/liabilities` went out with NO Cookie header ->
401 {"error"} -> data undefined**. The storageState verified healthy (1
cookie, domain 127.0.0.1, 30-day TTL); the trigger (why the
apiRequestContext dropped the context cookie on ONE call while 154
sibling tests stayed green) UNCONFIRMED — a one-off cookie-attachment
miss, unreproduced in the isolated rerun. **The diagnostic guard added**
(expect(list.ok(), "liabilities fixture GET must be authenticated (200)")
BEFORE the json destructure) — the 2nd occurrence read as a precise
"Expected: true / Received: false" instead of the cryptic TypeError. A
separate 17-failure terminal-block incident (the server dead from test 68
onward) occurred immediately after a tool-deadline kill of a loop run —
an infrastructure artifact of the escalation loop itself, NOT the flake;
documented, not counted. Both watches continue through the ship chain.

The probe series derived from the v129 lineage (derive-v135-series.py —
the generic swaps incl. SIX explicit session-token families
[refvlm/clonevlm + refcalc/clonecalc + reflogin/clonelogin arbit — the
tokens carry '129' without the 'v' prefix] + FOUR history-correction
fragments, all applied on the FIRST run, zero residual, line counts
preserved 102/166/65/355 == the v129 lineage exactly). The login-shots
sub-series derived (derive-loginshots-v135.py; both sides' login censuses
byte-equal; line counts preserved 30/30). The two-half builder derived
(derive-build-twohalf-v135.py -> build-twohalf-v135.py — the generic swap
+ the lesson-range bump v92..v128 -> v92..v134 + the lineage-note fixup
"build-twohalf-v123.py" -> "build-twohalf-v129.py" LAST; normalize-back
diff clean, zero residual; line-count preserved 82) + the comparator
derived (derive-compare-v135.py -> compare-v135-census.py — the generic
swap + the explicit /tmp/vlm129 -> /tmp/vlm135 log-path swap + the two
provenance citations re-pointed at the v129 measurement [the lineage
ordinal v123-era/ELEVENTH -> v129-era/TWELFTH; the records chain extended
v105/v111/v117/v123 -> +v129]; residual clean, line-count preserved 145)
+ the TWO-block md5 contract verified by the direct THREE-WAY python
extraction (verify-twohalf-v135.py — CALC_CENSUS_JS 61 lines md5
e1092d12d06677a4 + LOGIN_CENSUS_JS 36 lines md5 9e5a52d2ab0f2ab9,
byte-identical across arbit-v135.sh + ref-arbit-v135.sh +
clone-arbit-v135.sh — the v123/v129 lineage values VERBATIM).

The verdict: **CALCULATOR DIFFERENT x2 + LOGIN IDENTICAL (pass 1) /
DIFFERENT (pass 2 — the sole flag the reference's own "Edit with Base44"
FAB, the PLATFORM-CHROME class, DISPROVEN LIVE by base44-fab-arbit-v135.sh
[derived from the v129 form, swap-only verified]: fabCount 0 +
bodyHasBase44 false on BOTH sides at 1280 /login — the standing
v97/v103/v108/v109/v115/v120/v123/v127/v129 disproof form re-confirmed;
the pair's documented verdict-VARIATION family — the login verdict has
varied IDENTICAL/DIFFERENT across re-runs, the calculator verdict DIFFERENT
in every recorded re-run). Every calculator flag in both passes in the
documented classes: the hover action buttons "missing" the
POINTER-POSITION/HOVER-STATE screenshot artifact (the census actionsAtRest
{opacity 0, btnCount 2} IDENTICAL both sides), the "Will update category
total" note the SEED-DATA class, the total-card layout flag its
consequence. The both-sides census compared AXIS-BY-AXIS by the persisted
compare-v135-census.py: **106 axes — 97 identical + 9 documented-class
deltas, ZERO new — REPRODUCING the v129 census values EXACTLY** (the same
106/97/9 split, zero drift on every axis). NO NEW CLONE GAP on the census
axes — **but the census never measured focus end-states, and the F4
candidate survey found one** (the v129 cycle's own discovery pattern
repeated).

THE REPAIR + PIN — the CALCULATOR X's FOCUS-VISIBLE FAMILY (the first
src/ change since v129; +1 e2e = 338): the candidate was the calculator
X's keyboard focus end-state (the v129 hover repair's twin: the close
family fully held at REST [v59 F1 {w,h} at 1280 / v49 F3 {36,36} at 640 /
v53 F2 {29,36} at 390 / the v87 at-rest chrome]; the v129 pin the
OWN-HOVER tint ladder; the v32 pin the ROW ACTIONS' focus family — the X
itself carried NO focus class at any viewport; the computed focused
end-state held by NO spec). The BOTH-SIDES census (focusx-arbit-v135.sh —
the v129 xhover form adapted to the KEYBOARD ladder: the dialog opened via
the REAL pointer press on the expense card's Calculate button; the panel
finder DUAL [the clone's Radix [role=dialog] first, the reference's plain
maxWidth-768px div the fallback — the v99 lesson]; the X finder
TAG-AGNOSTIC + STRUCTURAL [the v87 geometric form — the reference's X
lost its accessible name]; the walk FINDER-BOUNDED and REQUIRING
:focus-visible to match [the clone's Radix auto-focus on dialog open is
PROGRAMMATIC — fv false — and must not satisfy the landing check; the
landing probe returns a PLAIN unquoted token — the v134 lesson]; NEVER
pressing Enter — the dialog opens on click/Enter, out of bounds;
READ-ONLY per the v46 rule) measured: the AT-REST + BLURRED rungs
IDENTICAL both sides — **but THE FOCUSED RUNG A NEW CLONE GAP: the
reference's X under keyboard focus carries the 1px #0a0a0a ring [the
white lead + rgb(10,10,10) 0px 0px 0px 1px + the transparent tail] + the
outline form [solid 2px rgba(0,0,0,0), offset 2px] — the shadcn focus
base — while the clone's X carried the UA default outline `auto 1px`
with NO ring**. **The repair: the zb-row-action class +
focus-visible:ring-1 focus-visible:ring-ring added at
calculator-dialog.tsx:138 (a 1-line edit — the file's own sibling family:
the row actions at :239/:247 carry the identical tokens, the v32-pinned
family; the at-rest chrome unchanged, the hover ladder unchanged, the
v87/v129 pins immune; the a11y gate immune [the ring is the shadcn family
the whole app carries]; the screenshots unaffected [all at-rest]; the
mobile views unaffected)**. THE TDD ORDER — **the RED run verified live**
(the pin alone failed against the unrepaired build at the X's ring
toContain [boxShadow "none" received vs rgb(10,10,10) 0px 0px 0px 1px
expected — exactly the predicted axis]) **then the repair + the REBUILD +
the GREEN run (first attempt) + the post-repair census re-run (the
FOCUSED state byte-identical both sides — the lead-slot count the
documented construct class, the visible ring layer identical)**. THE PIN
(tests/e2e/calculator.spec.ts, appended by the persisted
append-pin-v135.py): the X ladder (the at-rest rung -> the REAL-Tab
FOCUSED rung {fv true + THE ring via toContain + the outline form [solid
2px / transparent / offset 2px]} -> the blurred rung); the
V94-COLLISION-safe axis set (the end-states alone; the transition metadata
+ the lead-slot construct deliberately NOT pinned). THE PIN-SANITY
MUTATION — the line-138-scoped revert of the focus tokens (the
v129-revert form; the row-action lines 239/247 untouched): the SOLE
FAILURE verified live — 1 failed [the pin] + 21 passed in the full
calculator file; restored (git diff src/ = the repair only) + the REBUILD
+ the 89/89 post-restore regression (calculator 21 + dialog-buttons 17 +
items 51 — the v129/v133/v134 pins' different-file immunity verified
live).

The ship chain: lint, typecheck, 108 unit, 0-vuln audit, **338 e2e (93+92
+74+82 = 341 executions = 338 unique, the auditable split — ONE documented
intermittent: the empty-states:85 fixture GET, the 2nd occurrence,
precisely diagnosed by the guard, unreproduced in the isolated re-run; the
not-found:111 watch green under the IPv4 fix)**, 35/35 smoke, **the
screenshots 16/16 — 15 byte-identical + 07 the DETERMINISTIC CROSS-DAY
DATE-CLASS refresh (the todayIso default shifted Oct 29 -> 30 UTC; every
seeded-date surface byte-identical — the CONTINUING workspace's unchanged
seed)**, the dev evidence 4/4 byte-identical + VLM-verified (the menu
proof: /income, docSW 390, navLandmark true; the dev-shots scripts derived
v134->v135 with the version-swap-only verification). The docs D1-D7
aligned; `.env.example` verified untouched. The v135 probe lineage
persisted (derive-v135-series.py, derive-loginshots-v135.py,
derive-build-twohalf-v135.py, derive-compare-v135.py,
derive-standing-v135.py, build-twohalf-v135.py, verify-twohalf-v135.py,
compare-v135-census.py, focusx-arbit-v135.sh, survey-logincalc-v135.sh,
base44-fab-arbit-v135.sh, the v129-derived series [vlm-shots-v135.sh,
arbit-v135.sh, ref-arbit-v135.sh, clone-arbit-v135.sh,
clone-vlmshots-v135.sh, vlm-compare-v135.mjs], the login-shots pair
[login-shots-v135.sh, clone-login-shots-v135.sh], the 129th standing pair
[ref-standing-v129.sh, standing-checks-v129.sh], capture-dev-shots-v135.mjs,
verify-dev-shots-v135.mjs, append-pin-v135.py, align-docs-v135.py,
align-probereadme-v135.py, worklog-insert-s170.py). src/ ONE line changed
(the REPAIR form — the first src/ change since v129); tests/ +1 pin (338
total) + the empty-states diagnostic guard + the playwright-config IPv4
pin.

The v136 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from the
from-lineage's own bracket [entries − 1, the original not a re-run], never
the prose): (1) the re-run cadence rotates to the next-oldest candidate
after the v129-era LOGIN + CALCULATOR pair (the v130-era NETWORTH +
drill-down-DASHBOARD pair — the /networth view + the dashboard drill-down
at desktop 1280x800, last re-shot v130 — now the oldest remaining [v130 <
v131 < v132]; the pair's TWELFTH re-run bracket [v60 -> v67 -> v76 -> v82
-> v88 -> v94 -> v100 -> v106 -> v112 -> v118 -> v124 -> v130 -> v136] to
be verified against the v130 lineage's own records before the derivation —
the v130 plan's F3 records the ELEVENTH ordinal on its 12-entry bracket
[v60 the original], consistent, no off-by-one this lineage; the v130 shots
header carries the FULL bracket form, the verification source), (2) the
axe-core watch at its next re-check point (only a 5.x wrapper changes the
calculus), (3) the npm-audit watch at its re-check point (only a new
advisory in the next/zod ranges changes the calculus), (4) the deferred
reference-write censuses (unchanged — out of bounds under the v46
read-only rule), (5) the not-found:111 flake watch (the IPv4-pin fix in —
the watch continues for any residual class) + the empty-states:85 fixture
watch (the 2nd occurrence precisely diagnosed by the guard; if it recurs,
the trace capture + the cookie-attachment root-cause is the documented
step).

"""

text = text.replace(insert_after, insert_after + SECTION)
io.open(PR, "w", encoding="utf-8").write(text)
print("D6 probe README: the v135 section + the v136 queue inserted (anchor 1-hit verified)")
