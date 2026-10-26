#!/usr/bin/env python3
"""D6: the probe README's v123 section + the v124 queue; D7: the worklog
Session 158 entry. (session_302.md is written separately — the narrative
record.)"""

def replace1(path, old, new):
    t = open(path, encoding="utf-8").read()
    n = t.count(old)
    if n != 1:
        print(f"AMBIGUOUS/MISS in {path}: {n} hits for {old[:70]!r}")
        return False
    open(path, "w", encoding="utf-8").write(t.replace(old, new))
    return True

ok = True

# ---------------- D6: scripts/parity-probes/README.md ----------------
# The v123 section inserted after the v122 section's tail (the v123 queue),
# before the "## The v121 cycle" heading — the newest-first recent block.
V123_SECTION = """
## The v123 cycle (the v117-era LOGIN + CALCULATOR pair's TENTH re-run — Session 158)

The re-run cadence's next-oldest candidate: the v117-era LOGIN +
CALCULATOR pair — the LOGIN view + the CALCULATOR dialog at desktop
1280x800, the v59-era pair's surface family, last re-shot v117 — now the
oldest remaining [v117 < v118 < v119 < v120 < v121 < v122]; the pair's
TENTH re-run bracket [v59 -> v66 -> v75 -> v81 -> v87 -> v93 -> v99 ->
v105 -> v111 -> v117 -> v123]; the FORTY-SIXTH consecutive queue/ledger
agreement — the surface names verified against vlm-shots-v117.sh's own
header BEFORE the derivation (the v117 header's own NINTH ordinal
CONSISTENT with its 10-entry bracket [v59 the original — no off-by-one
this lineage]). **A PIN-ONLY cycle for src/ — zero production-code
changes** + one e2e pin; the cycle's standing items: the axe watch (NO
DRIFT — 4.14.0 holds, only the canary sha prerelease beyond, the v68
dedupe verified), the npm-audit watch at its fourteenth re-check (0
vulnerabilities — the v110 bump holds), the 117th standing checks (ALL
GREEN — the reference's four bugs live; the data census clean on the
FIRST reads; the clone's mobile menu VERIFIED WORKING the 117th
consecutive time; zero overflow at 390 on all five views; the seedcheck
exact after the clone half).

The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs this cycle
(the v122 date-axis repair verified holding on the new day: the v120
liability-card pin green with its computed seedDay form). The verdict:
**CALCULATOR DIFFERENT ×2 / LOGIN IDENTICAL ×2** (the consistent form —
no variation this cycle) — every flag DOM-arbitrated: the row action
buttons + the "shorter row" the POINTER-POSITION/HOVER-STATE screenshot
artifact + the VLM MISREAD (the census `actionsAtRest {opacity "0",
btnCount 2}` IDENTICAL both sides + `row.h 102` byte-identical; the
mechanism: the REFERENCE shots script captures BEFORE parking its
pointer — still at the Calculate button, INSIDE the opened dialog —
while the CLONE script parks at (5,5) BEFORE its capture; the shots
scripts' own structure, inherited verbatim from the v59 lineage); the
"Will update category total" note the SEED-DATA class; the login
"Edit with Base44" badge the PLATFORM-CHROME class disproven live
(base44-fab-arbit-v123.sh: fabCount 0 + bodyHasBase44 false BOTH
sides). The two-half census (build-twohalf-v123.py from the v117
builder — the TWO blocks CALC_CENSUS_JS 61 lines + LOGIN_CENSUS_JS 36
lines byte-identical across the halves, the md5 line-block contract
verified by direct python extraction; compare-v123-census.py with the
census-era corrections + the /tmp/vlm-path explicit swap [the bare
v117 swap cannot touch 'vlm117' — no 'v117' substring]): **106 axes —
97 identical + 9 documented-class deltas, ZERO new**.

The pin: the CALCULATOR line-item DELETE-CONFIRM BAR census at 1280
(confirmbar-arbit-v123.sh — the one-shot CONFIRM-LADDER census; the
never-pinned FOURTH member of the confirm-bar family: the v121 pin
holds the item-card bar, the net-worth twins are held BY CONSTRUCTION
via the identical class strings, the calculator's mt-3 variant held by
NO spec; the CLONE-ONLY form — the reference's row delete destroys
immediately, its R6 bug, and a reference-side measurement would need a
DESTRUCTIVE click under the v46 read-only rule): the bar {mt "12px" /
flex / center / space-between / radius "8px" / pad "12px" / w 686 /
h 48} + the label 14px/400 + the pills {4px 12px / 6px / 12px/500 /
h 24} + the shadow-sm VISIBLE layer + **the +60 bar-open delta (the
row card 102 -> 162)** + the Cancel path. The pin-sanity mutation
(p-3 -> p-4 at calculator-dialog.tsx:279, line-scoped, the mt-4 family
twins untouched): the SOLE FAILURE verified live — the pin ALONE red at
the pad + h axes, the full calculator file's 19 others green. The
census script's own first-run bug fixed live: the agent-browser
`mouse move` takes x y as TWO args — the single-arg "x,y" form moves
nowhere. The ship: 326 e2e zero flakes (87+86+74+82 = 329 executions =
326 unique); 35/35 smoke; the screenshots 16/16 byte-identical (the
same-day-seed law — no day-rollover this cycle); the dev evidence 4/4
byte-identical + VLM-verified (the menu proof: /income, docSW 390,
navLandmark true; the dev-shots scripts derived v122 -> v123 with the
version-swap-only verification).

The v124 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v117-era LOGIN + CALCULATOR pair (the v118-era NETWORTH +
drill-down-DASHBOARD pair — the /networth view + the dashboard
drill-down at desktop 1280x800, the v60-era pair's surface family,
last re-shot v118 — now the oldest remaining [v118 < v119 < v120 <
v121 < v122 < v123]; the pair's ELEVENTH re-run bracket [v60 -> v67 ->
v76 -> v82 -> v88 -> v94 -> v100 -> v106 -> v112 -> v118 -> v124] to be
verified against vlm-shots-v118.sh's own header before the derivation —
the v118 header's own TENTH ordinal should be consistent with its
11-entry bracket [v60 the original], so v124 = the ELEVENTH re-run by
the same convention), (2) the axe-core watch at its next re-check point
(only a 5.x wrapper changes the calculus), (3) the npm-audit watch at
its re-check point (only a new advisory in the next/zod ranges changes
the calculus), (4) the deferred reference-write censuses (unchanged —
out of bounds under the v46 read-only rule).
"""

ok = ok and replace1(
    "scripts/parity-probes/README.md",
    "v46 read-only rule).\n\n## The v121 cycle (the v115-era ITEMS pair's TENTH re-run — Session 156)",
    "v46 read-only rule).\n" + V123_SECTION + "\n## The v121 cycle (the v115-era ITEMS pair's TENTH re-run — Session 156)")

# ---------------- D7: worklog.md — the Session 158 entry ----------------
W158 = """## Session 158 — Parity iteration v123: the re-run cycle's next-oldest candidate (the v117-era LOGIN + CALCULATOR pair's TENTH re-run) + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — the standing step's fourteenth cycle) + the 117th standing checks + the calculator line-item DELETE-CONFIRM BAR census pin at 1280 (PIN-ONLY — the never-pinned FOURTH member of the confirm-bar family) (2026-10-26)

The v117-era LOGIN + CALCULATOR pair (the LOGIN view + the CALCULATOR
dialog at desktop 1280x800, the v59-era family, the TENTH re-run
[v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123];
the FORTY-SIXTH consecutive queue/ledger agreement — verified against
vlm-shots-v117.sh's own header before the derivation). PIN-ONLY for
src/ (zero production-code changes, the twelfth cycle since v46 without
one). The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs (the
v122 date-axis repair verified holding; lint · typecheck · 108 unit ·
build · 325 e2e zero flakes [328 executions in 4 chunks] · 35/35 smoke;
the production-seam audit clean; the post-push commits audited
session-log-only). The watches: axe NO DRIFT (4.14.0, only the canary
beyond, the v68 dedupe holds); npm audit 0 vulnerabilities (the v110
bump holds — fourteenth re-check). The 117th standing checks ALL GREEN
(the reference's four bugs live; the data census clean on the FIRST
reads; the clone's mobile menu VERIFIED WORKING the 117th consecutive
time; zero overflow at 390 on all five views; the seedcheck exact after
the clone half). The VLM pair: CALCULATOR DIFFERENT ×2 / LOGIN
IDENTICAL ×2 — every flag DOM-arbitrated (the pointer-position/
hover-state screenshot artifact [the reference shots script captures
before parking its pointer — the census actionsAtRest identical both
sides], the VLM row misread [row.h 102 byte-identical], the seed-data
note, the platform-chrome FAB disproven live). The two-half census: 106
axes — 97 identical + 9 documented-class deltas, ZERO new. THE PIN: the
calculator line-item DELETE-CONFIRM BAR census at 1280 (+1 e2e = 326) —
the never-pinned FOURTH member of the confirm-bar family (the v121
item-card pin's twin by identical class strings; the calculator-specific
mt-3 12px axis + the +60 bar-open delta [the row 102 → 162] + the
shadow-sm visible layer); the clone-only form (the reference's row
delete destroys immediately — its R6 bug); the pin-sanity p-3→p-4
line-scoped mutation sole-failure verified live (the pin alone red at
the pad + h axes; the 19 others green; the items file 48/48 post-restore
— the v121/v122 pins' different-file immunity). The census script's own
first-run bug fixed live: the agent-browser `mouse move` takes x y as
TWO args — the single-arg "x,y" form moves nowhere. The ship: 326 e2e
zero flakes (329 executions); 35/35 smoke; the screenshots 16/16
byte-identical (the same-day-seed law — no day-rollover this cycle);
the dev evidence 4/4 byte-identical + VLM-verified (the menu proof:
/income, docSW 390, navLandmark true). Docs D1–D7 aligned (AGENTS the
v123 paragraph [D0 checked clean — the anchor fragment unique]; CLAUDE
326 + the v123 clause; README counts + the v123 plan row; the SKILL
Session 158 row + the state line; PAD v1.1.80; the probe README's v123
section + the v124 queue [the v118-era NETWORTH + drill-down pair]; the
derived probe series v123 + the standing pair 117 + the dev-shots v123
+ the one-shot confirmbar-arbit-v123.sh + append-pin-v123.py +
align-docs-v123.py + derive-v123-series.py + derive-build-twohalf-v123.py
+ derive-compare-v123.py + derive-standing-v123.py + build-twohalf-v123.py
+ compare-v123-census.py all persisted). The workspace the RESET class
(re-cloned from main @ cbc38e9; the v108 fresh-clone provisioning
end-to-end). Delivery record: `docs/session_302.md`.

"""
ok = ok and replace1(
    "worklog.md",
    "## Session 157 — Parity iteration v122:",
    W158 + "## Session 157 — Parity iteration v122:")

print("D6+D7 RESULT:", "OK" if ok else "FAIL")
import sys
sys.exit(0 if ok else 1)
