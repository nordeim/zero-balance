#!/usr/bin/env python3
"""worklog-insert-s170.py — D7 of the v135 docs alignment: insert the
Session 170 entry at the top of worklog.md's session log (newest first),
immediately before the Session 169 entry. D0 discipline: the anchor
verified 1-hit BEFORE any write."""
import io
import sys

WL = "worklog.md"
text = io.open(WL, encoding="utf-8").read()

anchor = "## Session 169 — Parity iteration v134"
n = text.count(anchor)
if n != 1:
    print(f"ANCHOR MISS (the Session 169 header): {n} hits")
    sys.exit(1)

ENTRY = """## Session 170 — Parity iteration v135: the re-run cycle's next-oldest candidate (the v129-era LOGIN + CALCULATOR pair's TWELFTH re-run — the corrected entries-minus-one convention applied cleanly) + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — the standing step's twenty-sixth cycle) + the 129th standing checks + the calculator X's focus-visible family repair + pin at 1280 (the REPAIR + PIN form — the first src/ change since v129) (2026-10-30)

The v129-era LOGIN + CALCULATOR pair (the LOGIN view + the CALCULATOR
dialog at desktop 1280x800, the v59-era pair's surface family, last
re-shot v129 — now the oldest remaining [v129 < v130 < v131 < v132]; the
pair's TWELFTH re-run bracket [v59 -> v66 -> v75 -> v81 -> v87 -> v93 ->
v99 -> v105 -> v111 -> v117 -> v123 -> v129 -> v135]; the FIFTY-EIGHTH
consecutive queue/ledger agreement — the corrected entries-minus-one
convention applied cleanly, the ELEVENTH ordinal recorded in the v129
plan's own F3 record on its 12-entry bracket [v59 the original, one
entry] with no prose/header conflict; the v129 shots header carries the
FULL bracket form — the documented verification source).

**A REPAIR + PIN cycle for src/ — the first src/ change since v129 (the
five-cycle PIN-ONLY run v130..v134 ends at v134)** + one e2e pin
(337 -> 338) + a test-config change (the IPv4-literal BASE_URL pin) + a
spec diagnostic guard (the empty-states G6 fixture).

The baseline GREEN with **THE FLAKE EPISODE escalated — BOTH
intermittents captured for the first time** (the CONTINUING workspace —
the v134 cycle's own sandbox workspace persisted, the seedcheck exact
before any gate; lint, typecheck, 108/108 unit, build, 337 e2e [341
executions in 4 chunks = 336 spec + 1 setup: 93/91/74/82], 35/35 smoke;
the production-seam audit clean + the v134 pin verified in place). The
not-found:111 recurrence — the full error capture
`page.goto: net::ERR_CONNECTION_REFUSED at http://localhost:3100/` (the
test died at the NAVIGATION; the v134 "transient error head" hypothesis
DISPROVEN); the asymmetry verified live (the standalone server binds
0.0.0.0 IPv4-only: 127.0.0.1:3100 -> 200, [::1]:3100 -> REFUSED) — the
localhost resolution racing ::1-first the mechanism; **the fix: BASE_URL
pinned to the IPv4 literal in playwright.config.ts** (a test-config
change, src/ untouched), the full 337 re-verified green under the fix.
The empty-states:85 recurrence — the cookie-less apiRequestContext GET ->
401 {"error"} -> the cryptic data.map TypeError, captured WITH the
retained trace (the network entry: NO Cookie header; the storageState
verified healthy); the diagnostic guard added so a recurrence reads as a
precise expect-ok failure (the 2nd occurrence read exactly that:
"Expected: true / Received: false"). Both watches continue.

The standing items: the npm-audit watch 0 vulnerabilities (the
twenty-sixth re-check — the v110 bump holds), the axe-core watch NO DRIFT
(4.14.0, the v68 dedupe holds), **the 129th standing checks ALL GREEN**
(the reference's four bugs live; the data census clean on the FIRST
reads; the clone's mobile menu VERIFIED WORKING the 129th consecutive
time, zero overflow at 390 on all five views; the seedcheck exact after
the clone half).

The probe series derived from the v129 lineage (derive-v135-series.py —
SIX explicit session-token families + FOUR history-correction fragments,
zero residual, line counts preserved 102/166/65/355) + the login-shots
sub-series (30/30) + the builder (the lesson-range bump v92..v128 ->
v92..v134) + the comparator (the /tmp/vlm129 -> /tmp/vlm135 log-path
swap; the provenance citations re-pointed at the v129 measurement) + the
TWO-block md5 contract verified three-way (verify-twohalf-v135.py —
CALC_CENSUS_JS 61 lines e1092d12d06677a4 + LOGIN_CENSUS_JS 36 lines
9e5a52d2ab0f2ab9, the v123/v129 lineage values VERBATIM). **The VLM
verdict — CALCULATOR DIFFERENT x2 + LOGIN IDENTICAL (pass 1) / DIFFERENT
(pass 2 — the sole flag the "Edit with Base44" FAB, the PLATFORM-CHROME
class, DISPROVEN LIVE by base44-fab-arbit-v135.sh: fabCount 0 +
bodyHasBase44 false on BOTH sides; the pair's documented verdict-VARIATION
family)**; every calculator flag in the documented classes. The both-sides
census **106 axes — 97 identical + 9 documented-class deltas, ZERO new**
— REPRODUCING the v129 census values EXACTLY — **but the census never
measured focus end-states, and the F4 candidate survey found one**.

THE REPAIR + PIN — the CALCULATOR X's FOCUS-VISIBLE LADDER at 1280: the
candidate survey (the login view's three hover families measured live on
the reference — the submit's #0f172a -> #1e293b, the Google's
#f8fafc/#cbd5e1 + shadow-sm, the mode links' #64748b -> #334155 — every
one matching the clone's existing classes, both-sides-matching,
documented; the calculator X's keyboard path entirely unpinned); the
both-sides one-shot census focusx-arbit-v135.sh (the walk FINDER-BOUNDED
and REQUIRING :focus-visible — the clone's Radix auto-focus is
programmatic and must not satisfy the landing check) measured **THE GAP**:
the reference's focused rung carries the 1px #0a0a0a ring + the
transparent-outline form [solid 2px, offset 2px] — the shadcn focus base —
while the clone's carried the UA default `auto 1px` with NO ring. **The
repair: the zb-row-action class + focus-visible:ring-1
focus-visible:ring-ring added at calculator-dialog.tsx:138** (the file's
own sibling family — the row actions at :239/:247 carry the identical
tokens, the v32-pinned family; a 1-line edit). **THE TDD ORDER — the RED
run verified live** (the pin alone failed against the unrepaired build at
the ring toContain: "none" received vs the ring expected — exactly the
predicted axis) **then the repair + the REBUILD + the GREEN run (first
attempt) + the post-repair census re-run (the focused rung
byte-identical both sides)**. THE PIN-SANITY MUTATION — the line-138
scoped revert of the focus tokens: the SOLE FAILURE verified live —
1 failed [the pin] + 21 passed in the FULL calculator sweep; restored +
the FULL REBUILD + the 89/89 post-restore regression (calculator 21 +
dialog-buttons 17 + items 51).

The ship chain 338 e2e (93+92+74+82 = 341 executions = 338 unique — ONE
documented intermittent: the empty-states:85 fixture GET, the 2nd
occurrence, precisely diagnosed by the guard, unreproduced in the isolated
re-run; the not-found:111 watch green under the IPv4 fix); 35/35 smoke;
the screenshots 16/16 — 15 byte-identical + 07 the DETERMINISTIC
CROSS-DAY DATE-CLASS refresh (the todayIso default shifted Oct 29 -> 30
UTC; every seeded-date surface byte-identical — the CONTINUING
workspace's unchanged seed); the dev evidence 4/4 byte-identical +
VLM-verified (the menu proof: /income, docSW 390, navLandmark true). The
docs D1-D7 aligned; `.env.example` verified untouched.

---

"""
text = text.replace(anchor, ENTRY + anchor, 1)
io.open(WL, "w", encoding="utf-8").write(text)
print("D7 worklog: the Session 170 entry inserted (anchor 1-hit verified)")
