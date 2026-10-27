#!/usr/bin/env python3
"""D6: the probe README's v124 section + the v125 queue; D7: the worklog
Session 159 entry. (session_304.md is written separately — the narrative
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
# The v124 section inserted after the v123 section's tail (the v124 queue),
# before the "## The v121 cycle" heading — the newest-first recent block.
V124_SECTION = """
## The v124 cycle (the v118-era NETWORTH + drill-down-DASHBOARD pair's TENTH re-run — Session 159)

The re-run cadence's next-oldest candidate: the v118-era NETWORTH +
drill-down-DASHBOARD pair — the /networth view + the dashboard drill-down
EXPANDED state at desktop 1280x800, the v60-era pair's surface family,
last re-shot v118 — now the oldest remaining [v118 < v119 < v120 < v121 <
v122 < v123]; the pair's TENTH re-run bracket [v60 -> v67 -> v76 -> v82 ->
v88 -> v94 -> v100 -> v106 -> v112 -> v118 -> v124]; the FORTY-SEVENTH
consecutive queue/ledger agreement — the surface names verified against
vlm-shots-v118.sh's own header BEFORE the derivation. **THE CYCLE'S FIND —
THE QUEUE PROSE'S ORDINAL OFF-BY-ONE, caught by the header verification**
(the queue-prose verification lesson working as designed): the v123-era
docs' v124 queue named "the pair's ELEVENTH re-run bracket" and expected
"the v118 header's own TENTH ordinal... consistent with its 11-entry
bracket" — but vlm-shots-v118.sh's own header reads "The pair's NINTH
re-run [v60 -> v67 -> v76 -> v82 -> v88 -> v94 -> v100 -> v106 -> v112 ->
v118]" — a 10-ENTRY bracket; the ordinal chain verified BACKWARDS before
the derivation (v106 SEVENTH -> v112 EIGHTH -> v118 NINTH — the lineage
internally consistent, no off-by-one there); the off-by-one lives in the
QUEUE PROSE (the v123 cycle's own phrasing counted the 11-entry v124
bracket as ELEVENTH, breaking the convention by which v123's own 11-entry
bracket was the TENTH, from v117's NINTH/10-entry form). The resolution:
v124 = the TENTH re-run, the surface unaffected — and the D6 v125 queue
now carries the CORRECTED CONVENTION (the ordinal ALWAYS derived from the
from-header's own bracket [entries − 1, the original not a re-run], never
the prose). **A PIN-ONLY cycle for src/ — zero production-code changes**
(the thirteenth since v46) + one e2e pin; the cycle's standing items: the
axe watch (NO DRIFT — 4.14.0 holds, only the canary sha prerelease beyond,
the v68 dedupe verified), the npm-audit watch at its fifteenth re-check (0
vulnerabilities — the v110 bump holds), the 118th standing checks (ALL
GREEN — the reference's four bugs live; the data census clean on the
FIRST reads; the clone's mobile menu VERIFIED WORKING the 118th
consecutive time; zero overflow at 390 on all five views; the seedcheck
exact after the clone half).

The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs this cycle
(the workspace the CARRIED-OVER class — the v123 environment persisted,
the repo refreshed via git pull, NO re-provisioning: the zod extraction
verified intact 840/840, BOTH v1243 playwright pairs verified in the
cache directly, the seedcheck exact before any gate). The verdict:
**NETWORTH IDENTICAL ×2 / DRILL-DOWN DIFFERENT ×2** (the consistent form)
— every flag DOM-arbitrated: the "Dashboard nav highlighted (green
background) in the clone" the v56 SUPERSET delta + perception (the census
navHighlight bg rgba(0,0,0,0) transparent on BOTH sides — no green
anywhere; the color/fw asymmetry the documented superset delta); the
avatar U-vs-D the USER-IDENTITY class; the progress 30.5%-vs-62.8% the
PCT data class (fillW 173-vs-357); the donut labels "missing in the
reference" the EACH-SITE'S-DATA + perception class (count 4 / labelFs
16px / sectors 3 byte-identical BOTH sides — the reference DOES render
its 92.3/4.6/3.1 labels); the stat-card trend icons "different stroke
paths" the v67 PATH-SIGNATURE misread (the glyphSig polyline byte-
identical both sides); the networth groups the SEED-DATA class. The
two-half census (build-twohalf-v124.py from the v118 builder — the TWO
blocks ARBIT_A 90 lines + ARBIT_B 111 lines byte-identical across the
halves, the md5 contracts b4ba7fe7/dfb1a1df verified by direct python
extraction [verify-twohalf-v124.py]; compare-v124-census.py with the
census-era corrections + the /tmp/vlm-path explicit swap [the bare v118
swap cannot touch 'vlm118']): **73 axes — 67 identical + 6
documented-class deltas, ZERO new** — REPRODUCING the v106/v112/v118
census values EXACTLY (the same 73/67/6 split).

The pin: the NETWORTH asset-card kebab-trigger's OPEN-MENU reveal census
at 1280 (kebabopen-arbit-v124.sh — the one-shot REVEAL-LADDER census,
measured cleanly on the FIRST run; the reveal family's OPEN path on the
never-pinned networth file: the v46 census holds the networth kebab's
at-rest + hover rungs, the v36 S3 the keyboard, the v122 pin the open
path on the SAVINGS item-card only — a DIFFERENT FILE whose own v122
mutation left these networth twins green, the different-file immunity
evidence; the CLONE-ONLY form — the reference's trigger stays invisible
when its menu opens, its own superset-#7 bug, and the reference's
net-worth kebab flow is NEVER safe to probe past the menu open): the
open+parked {opacity "1" / dataState "open" / the unchanged 36×36 / 6px
/ transparent / rgb(10,10,10) / insets 21/21} with the pointer parked at
(5,5) — the data-[state=open] token alone holding the reveal. **The
pin-sanity mutation's CONDITIONAL-FORM DISCOVERY (the cycle's live-red
lesson)**: the v122 UNCONDITIONAL form (the token replaced outright with
opacity-90) reddens the v46 at-rest census TOO on this surface — the
unconditional token beats opacity-0 in the Tailwind utilities cascade
(same specificity, later in the property-group order), leaking the
at-rest state to 0.9; the v122 form worked only because the items file
holds NO at-rest assertion for the item-card kebab, while the networth
file DOES (the v46 census, networth.spec.ts:1084); the CORRECTED
CONDITIONAL form (data-[state=open]:opacity-100 -> data-[state=open]:
opacity-90, the conditionality preserved) isolates the open path alone —
the SOLE FAILURE verified live: the pin ALONE red at the open+parked
opacity axis ("1" -> "0.9", the deep-equality diff the single opacity
line), the full networth file's 36 others green, the items file 48/48
green. The ship: 327 e2e zero flakes (88+86+74+82 = 330 executions = 327
unique); 35/35 smoke; **the screenshots 15/16 byte-identical + 1
DAY-ROLLOVER REFRESH (07-add-item-modal.png — the CAPTURE-DAY-DEPENDENT
class: the dialog's date input defaults to todayIso(), the one surface
in the 16-shot catalog that follows the CAPTURE day rather than the seed
day; the pixel pre-analysis 234/5,184,000 pixels in a single 16×22 bbox
[the date digits alone] + the VLM verification [date-only, zero chrome
drift]; the refreshed shot committed)**; the dev evidence 4/4
byte-identical + VLM-verified (the menu proof: /income, docSW 390,
navLandmark true; the dev-shots scripts derived v123 -> v124 with the
version-swap-only verification; the stale dev-server LOCK reaped — a
hung next-server held .next/dev/lock with its socket already dead, the
port-scan reaper missed it, the PID-direct kill the fix).

The v125 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-header's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence rotates to the next-oldest
candidate after the v118-era NETWORTH + drill-down-DASHBOARD pair (the
v119-era DASHBOARD pair — the BUDGET GUIDELINES card + the QUICK-ACTION
card row, both below the fold on the dashboard at desktop 1280x800
FULL-PAGE, the v61-era pair's surface family, last re-shot v119 — now
the oldest remaining [v119 < v120 < v121 < v122 < v123 < v124]; the
pair's TENTH re-run bracket [v61 -> v68 -> v77 -> v83 -> v89 -> v95 ->
v101 -> v107 -> v113 -> v119 -> v125] to be verified against
vlm-shots-v119.sh's own header before the derivation — the v119 header's
own NINTH ordinal is consistent with its 10-entry bracket [v61 the
original], so v125 = the TENTH re-run by the same entries-minus-one
convention), (2) the axe-core watch at its next re-check point (only a
5.x wrapper changes the calculus), (3) the npm-audit watch at its
re-check point (only a new advisory in the next/zod ranges changes the
calculus), (4) the deferred reference-write censuses (unchanged — out of
bounds under the v46 read-only rule).
"""

ok = ok and replace1(
    "scripts/parity-probes/README.md",
    "v46 read-only rule).\n\n## The v121 cycle (the v115-era ITEMS pair's TENTH re-run — Session 156)",
    "v46 read-only rule).\n" + V124_SECTION + "\n## The v121 cycle (the v115-era ITEMS pair's TENTH re-run — Session 156)")

# ---------------- D7: worklog.md — the Session 159 entry ----------------
W159 = """## Session 159 — Parity iteration v124: the re-run cycle's next-oldest candidate (the v118-era NETWORTH + drill-down-DASHBOARD pair's TENTH re-run — the queue prose's ordinal off-by-one caught by the header verification) + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — the standing step's fifteenth cycle) + the 118th standing checks + the networth kebab-trigger OPEN-MENU reveal census pin at 1280 (PIN-ONLY — the reveal family's open path on the never-pinned networth file) (2026-10-27)

The v118-era NETWORTH + drill-down-DASHBOARD pair (the /networth view +
the dashboard drill-down EXPANDED state at desktop 1280x800, the v60-era
family, the TENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 →
v106 → v112 → v118 → v124]; the FORTY-SEVENTH consecutive queue/ledger
agreement — verified against vlm-shots-v118.sh's own header before the
derivation, **which REFUTED the queue prose's "ELEVENTH re-run" ordinal:
the v118 header's own NINTH/10-entry bracket makes v124 the TENTH by the
same convention that made v123 the TENTH from v117's NINTH; the chain
verified backwards v106 SEVENTH → v112 EIGHTH → v118 NINTH — the
off-by-one lived in the prose, not the lineage; the corrected convention
now carried in the v125 queue**). PIN-ONLY for src/ (zero
production-code changes, the thirteenth cycle since v46 without one).
The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs (lint ·
typecheck · 108 unit · build · 326 e2e zero flakes [329 executions in 4
chunks] · 35/35 smoke; the v122 date-axis repair verified holding; the
production-seam audit clean; the post-push commits audited
session-log-only). The watches: axe NO DRIFT (4.14.0, only the canary
beyond, the v68 dedupe holds); npm audit 0 vulnerabilities (the v110
bump holds — fifteenth re-check). The 118th standing checks ALL GREEN
(the reference's four bugs live; the data census clean on the FIRST
reads; the clone's mobile menu VERIFIED WORKING the 118th consecutive
time; zero overflow at 390 on all five views; the seedcheck exact after
the clone half). The VLM pair: NETWORTH IDENTICAL ×2 / DRILL-DOWN
DIFFERENT ×2 — every flag DOM-arbitrated (the nav-highlight v56 superset
+ perception [bg transparent both sides], the avatar user-identity, the
progress pct, the donut labels data+perception [count/fs/sectors
identical both sides], the trend-icons v67 path-signature misread
[glyphSig byte-identical], the networth groups seed-data). The two-half
census: 73 axes — 67 identical + 6 documented-class deltas, ZERO new
(the v106/v112/v118 values reproduced EXACTLY). THE PIN: the networth
asset-card kebab-trigger's OPEN-MENU reveal census at 1280 (+1 e2e =
327) — the reveal family's open path on the never-pinned networth file
(net-worth-view.tsx:82/192, the v122 pin's different-file twin by
identical class strings; the open+parked opacity-1 axis with the pointer
off the card + the unchanged 36×36 box chrome); the clone-only form (the
reference's trigger stays invisible when its menu opens — its own
superset-#7 bug; the reference's net-worth kebab flow never safe to
probe past the menu open). **The pin-sanity mutation's CONDITIONAL-FORM
discovery**: the v122 unconditional form (the token replaced outright
with opacity-90) reddens the v46 at-rest census TOO — the unconditional
token beats opacity-0 in the Tailwind utilities cascade, leaking the
at-rest state to 0.9 (the v122 form worked only because the items file
holds no at-rest assertion for the item-card kebab); the corrected
CONDITIONAL form (data-[state=open]:opacity-90) isolates the open path —
the SOLE FAILURE verified live (the pin alone red at the opacity axis,
the 36 others green, the items file 48/48 — the v122 pin's
different-file immunity re-verified). The ship: 327 e2e zero flakes (330
executions); 35/35 smoke; the screenshots 15/16 byte-identical + 1
day-rollover refresh (the add-item modal's capture-day date input —
234 pixels in a 16×22 bbox, VLM-verified date-only, zero chrome drift);
the dev evidence 4/4 byte-identical + VLM-verified (the menu proof:
/income, docSW 390, navLandmark true; the stale dev-server LOCK reaped —
the PID-direct kill after the port-scan reaper missed the hung process).
Docs D1–D7 aligned (AGENTS the v124 paragraph [D0 checked clean]; CLAUDE
327 + the v124 clause; README counts + the v124 plan row; the SKILL
Session 159 row + the state line; PAD v1.1.81; the probe README's v124
section + the v125 queue [the v119-era DASHBOARD pair — the BUDGET
GUIDELINES + QUICK-ACTION below-the-fold surfaces, the TENTH re-run by
the corrected entries-minus-one convention]; the derived probe series
v124 + the standing pair 118 + the dev-shots v124 + the one-shot
kebabopen-arbit-v124.sh + verify-twohalf-v124.py + verify-modal-shot-
v124.mjs + append-pin-v124.py + align-docs-v124.py +
align-probereadme-worklog-v124.py + insert-skillrow-v124.py +
derive-v124-series.py + derive-build-twohalf-v124.py +
derive-compare-v124.py + derive-standing-v124.py + build-twohalf-v124.py
+ compare-v124-census.py all persisted). The workspace the CARRIED-OVER
class (git pull from main @ 333c2cb — no re-provisioning needed: zod
840/840 intact, both v1243 playwright pairs verified, the seedcheck
exact). Delivery record: `docs/session_304.md`.

"""
ok = ok and replace1(
    "worklog.md",
    "## Session 158 — Parity iteration v123:",
    W159 + "## Session 158 — Parity iteration v123:")

print("D6+D7 RESULT:", "OK" if ok else "FAIL")
import sys
sys.exit(0 if ok else 1)
