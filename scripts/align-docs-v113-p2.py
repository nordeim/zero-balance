#!/usr/bin/env python3
"""D6/D7 docs alignment for the v113 cycle (the align-docs-v112-p2.py form).

D6  probe README — the v113 section inserted BEFORE the v112 section
                    header + the v113 queue block REPLACED by the v114
                    queue block
D7  worklog.md    — the Session 148 entry inserted BEFORE the Session 147
                    entry

Each edit verifies its anchor exists (a miss fails the run loudly).
"""
import sys

ok = True

# ---------------- D6: the probe README ----------------
V113_SECTION = """## The v113 cycle (the v107-era BUDGET GUIDELINES + QUICK-ACTION pair's EIGHTH re-run — Session 148)

The re-run cadence's next-oldest candidate: the v107-era BUDGET
GUIDELINES + QUICK-ACTION pair (both v61 target surfaces below the fold
on the DASHBOARD at desktop 1280x800 FULL-PAGE, last re-shot v107 — now
the oldest remaining [v107 < v108 < v109 < v110 < v111 < v112]; the
pair's EIGHTH re-run bracket [v61 -> v68 -> v77 -> v83 -> v89 -> v95 ->
v101 -> v107 -> v113]; the THIRTY-SIXTH consecutive queue/ledger
agreement — the surface names verified against vlm-shots-v107.sh's own
header before the derivation). PIN-ONLY for src/; the cycle's standing
items: the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe
verified), the npm-audit watch at its fourth re-check (0
vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]), the
107th standing checks (ALL GREEN — the mobile menu the 107th
consecutive green; the reference's four bugs all live; the data census
clean on the FIRST reads, no render-race hit this cycle). The verdict:
IDENTICAL — ZERO layout/style flags on the pair's own target surfaces
(the SIXTH consecutive IDENTICAL verdict for this pair [v83 -> v89 ->
v95 -> v101 -> v107 -> v113]; the only flags the documented seed-data
classes; no FAB flag raised — the v103 standing class). The two-half
census (ARBIT_G 61 lines md5 b500dd29 + ARBIT_Q 58 lines md5 da04e995 +
ARBIT_X 25 lines md5 7a381755 — the version-free v101/v107 census
blocks carried over VERBATIM), compared axis-by-axis by the persisted
compare-v113-census.py (154 axes: 144 identical + 10 deltas, every
delta a documented class — the shadow lead-layer count the v66
INVISIBLE class; the quick-action label census delta the v61 label
lesson [the finder's wrapper catch; the clone's LEAF carries the
identical chrome — the v61 F3 + v107 F4 pins]; the grid mt the v77
mechanism class [the rendered gap byte-identical at 340]; the gridCls
strings the site-source class), reproduces the v107 values exactly —
the PART X hard axes cardBottom 1122/gridTop 1462/gap 340 byte-
identical — NO NEW CLONE GAP. The +1 pin (tests/e2e/dashboard.spec.ts):
the Budget Guidelines card's TILE LABEL-ROW family + the tile stack
rhythm at 1280 — the row {flex/center/space-between/mb 4px/h 24/w 384/
childCount 2} + the rhythm {gap1 12/gap2 12} — never pinned at ANY
viewport in ANY spec (the label/pct x-position axes stay
census-documented but UNPINNED — the v107 xInRow discipline), measured
byte-identical both sides via the one-shot glrow-arbit-v113.sh (the
finders structural: the childless-exact-text heading + the
shadow/radius/p card walk-up + the flex-ancestor-of-the-label-that-
contains-the-pct row walk), mutation-verified single-axis AND
cascade-free (justify-between -> justify-start at dashboard-view.tsx:847
line-scoped — the ONLY mb-1 flex items-center justify-between line in
the file; only the v113 pin red at the row.justify axis alone
[space-between -> flex-start] after the standalone REBUILD; the v61/
v77/v83/v89/v101/v107/v112 pins green under the mutation). The ship
chain: 316 e2e zero flakes (83+77+75+84 = 319 executions = 316 unique);
35/35 smoke; the screenshots 16/16 byte-identical (the same-day-seed
law); the dev evidence re-captured + VLM-verified.

- THE IDEMPOTENT-RUN DUPLICATION TRAP (an alignment-scripting lesson):
  the align-docs re-run after a mid-script MISS duplicated every
  insert-after edit (the anchor text SURVIVES the insertion, so the
  second run inserts a SECOND copy) — grep -c undercounts (it counts
  LINES, not occurrences, and the docs carry one paragraph per line);
  the repair the persisted dedup-align-v113.py (grep -o | wc -l is the
  occurrence counter; the alignment scripts' insert-after edits are
  NOT idempotent — rerunning requires a dedup pass or an
  already-applied guard).

"""

t = open("scripts/parity-probes/README.md", encoding="utf-8").read()
sec_anchor = "## The v112 cycle (the v106-era NETWORTH + drill-down-DASHBOARD pair's EIGHTH re-run — Session 147)"
if sec_anchor not in t:
    print("MISS: probe README v112 section anchor")
    ok = False
else:
    t = t.replace(sec_anchor, V113_SECTION + sec_anchor, 1)
    print("probe README: the v113 section inserted")

# the v113 queue block -> the v114 queue block
V113_QUEUE = """The v113 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v106-era NETWORTH + drill-down-DASHBOARD pair (the v107-era
BUDGET GUIDELINES + QUICK-ACTION pair — both v61 target surfaces live
below the fold on the DASHBOARD at desktop 1280x800 FULL-PAGE, last
re-shot v107 — now the oldest remaining [v107 < v108 < v109 < v110 <
v111 < v112]; the pair's EIGHTH re-run bracket [v61 -> v68 -> v77 ->
v83 -> v89 -> v95 -> v101 -> v107 -> v113] to be verified against
vlm-shots-v107.sh's own header before the derivation), (2) the axe-core
watch at its next re-check point (only a 5.x wrapper changes the
calculus), (3) the npm-audit watch at its re-check point (only a new
advisory in the next/zod ranges changes the calculus), (4) the deferred
reference-write censuses (unchanged — out of bounds under the v46
read-only rule)."""

V114_QUEUE = """The v114 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v107-era BUDGET GUIDELINES + QUICK-ACTION pair (the v108-era
MOBILE TWINS pair — BOTH mobile 390x844 full-page twins: the /NETWORTH
view [the v63-era pair's surface] and the DASHBOARD [the v62-era mobile
twin's surface], last re-shot v108 — now the oldest remaining [v108 <
v109 < v110 < v111 < v112 < v113]; the pair's EIGHTH re-run bracket
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114] to
be verified against vlm-shots-v108.sh's own header before the
derivation), (2) the axe-core watch at its next re-check point (only a
5.x wrapper changes the calculus), (3) the npm-audit watch at its
re-check point (only a new advisory in the next/zod ranges changes the
calculus), (4) the deferred reference-write censuses (unchanged — out
of bounds under the v46 read-only rule)."""

if V113_QUEUE not in t:
    print("MISS: probe README v113 queue block")
    ok = False
else:
    t = t.replace(V113_QUEUE, V114_QUEUE, 1)
    print("probe README: the v114 queue installed")

open("scripts/parity-probes/README.md", "w", encoding="utf-8").write(t)

# ---------------- D7: worklog.md ----------------
V113_WORKLOG = """## Session 148 — Parity iteration v113: the re-run cycle's next-oldest candidate (the v107-era BUDGET GUIDELINES + QUICK-ACTION pair's eighth re-run) + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — the standing step's fourth cycle) + the 107th standing checks + the guidelines tile label-row census pin (PIN-ONLY) (2026-10-24)

**The cycle** (`docs/remediation-plan-v113.md` — the plan validated against the codebase before execution; the delivery record: `docs/session_277.md`): the re-run cadence's next-oldest candidate — the v107-era BUDGET GUIDELINES + QUICK-ACTION pair (both v61 target surfaces below the fold on the DASHBOARD at desktop 1280x800 FULL-PAGE, last re-shot v107 — now the oldest remaining [v107 < v108 < v109 < v110 < v111 < v112]; the pair's EIGHTH re-run bracket [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113]; the THIRTY-SIXTH consecutive queue/ledger agreement — the surface names verified against vlm-shots-v107.sh's own header before the derivation) + the axe watch (NO DRIFT — 4.14.0 holds; the v68 dedupe verified) + the npm-audit watch at its fourth cycle (0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 107th standing checks + the guidelines tile label-row census pin at 1280 (PIN-ONLY; +1 e2e = 316).

- **The verdict IDENTICAL** — ZERO layout/style flags on the pair's own target surfaces (the SIXTH consecutive IDENTICAL verdict for this pair [v83 → v89 → v95 → v101 → v107 → v113]; the only flags the documented seed-data classes — the allocation pct, the balance, the stat figures, the item counts, the donut proportions; no FAB flag raised — the v103 standing class).
- **The two-half census** (ARBIT_G 61 lines md5 b500dd29 + ARBIT_Q 58 lines md5 da04e995 + ARBIT_X 25 lines md5 7a381755 — the version-free v101/v107 census blocks carried over VERBATIM), compared axis-by-axis by the persisted compare-v113-census.py (154 axes: 144 identical + 10 deltas, every delta a documented class — the shadow lead-layer count the v66 INVISIBLE class; the quick-action label census delta the v61 label lesson [the finder's wrapper catch; the clone's LEAF carries the identical chrome — the v61 F3 + v107 F4 pins]; the grid mt the v77 mechanism class [the rendered gap byte-identical at 340]; the gridCls strings the site-source class) **reproduces the v107 values exactly on every axis — the PART X hard axes cardBottom 1122/gridTop 1462/gap 340/gridParentMt 0px byte-identical — NO NEW CLONE GAP**.
- **The +1 pin** (tests/e2e/dashboard.spec.ts): the Budget Guidelines card's TILE LABEL-ROW family + the tile stack rhythm at 1280 — the row {flex/center/space-between/mb 4px/h 24/w 384/childCount 2} + the rhythm {gap1 12/gap2 12} — never pinned at ANY viewport in ANY spec (the label/pct x-position axes stay census-documented but UNPINNED — the v107 xInRow discipline); measured byte-identical both sides via the one-shot glrow-arbit-v113.sh (the finders structural: the childless-exact-text heading + the shadow/radius/p card walk-up + the flex-ancestor-of-the-label-that-contains-the-pct row walk); mutation-verified single-axis AND cascade-free (justify-between → justify-start at dashboard-view.tsx:847 line-scoped — the ONLY mb-1 flex items-center justify-between line in the file; only the v113 pin red at the row.justify axis alone [space-between → flex-start] after the standalone REBUILD; the v61/v77/v83/v89/v101/v107/v112 pins green under the mutation); restored, rebuilt, post-restore 46/46 green.
- **The baseline chain FULLY GREEN on the RETAINED workspace** (no reset, no provisioning repair): seedcheck exact (7/1850/2235/0/3/2); lint; typecheck; 108 unit; build (robots + sitemap prerendered); 315 e2e zero flakes across the four-chunk split (82+77+75+84 = 318 executions — the a11y file kept INSIDE chunk 4); 35/35 smoke; npm audit 0 vulnerabilities; the two post-push commits audited session-log-only.
- **The ship chain**: 316 e2e zero flakes (83+77+75+84 = 319 executions = 316 unique); 35/35 smoke; the screenshots 16/16 byte-identical (the same-day-seed law — zero arbitration); the dev evidence re-captured + VLM-verified (the menu proof: /income, docSW 390, navLandmark true).
- **The 107th standing checks ALL GREEN** — the mobile menu VERIFIED WORKING the 107th consecutive time; the reference's four bugs all live; the data census clean on the FIRST reads (no render-race hit this cycle); the SEO pair live both sides.
- **The cycle's tooling finding**: THE IDEMPOTENT-RUN DUPLICATION TRAP (the align-docs re-run after a mid-script MISS duplicated every insert-after edit — the anchor text SURVIVES the insertion; grep -c undercounts because it counts LINES not occurrences and the docs carry one paragraph per line; the repair the persisted dedup-align-v113.py).
- The docs aligned D1–D7 (AGENTS the v113 paragraph; CLAUDE 316 + the v113 clause; README counts + the v113 plan row; the SKILL Session 148 row + the state line; PAD v1.1.70; the probe README's v113 section + the IDEMPOTENT-RUN lesson + the v114 queue; this Session 148 entry); `docs/session_277.md` saved. `.env.example` verified matching the codebase.

---

"""

t = open("worklog.md", encoding="utf-8").read()
wl_anchor = "## Session 147 — Parity iteration v112:"
if wl_anchor not in t:
    print("MISS: worklog Session 147 anchor")
    ok = False
else:
    t = t.replace(wl_anchor, V113_WORKLOG + wl_anchor, 1)
    open("worklog.md", "w", encoding="utf-8").write(t)
    print("worklog.md: the Session 148 entry inserted")

print("D6-D7 done" if ok else "D6-D7 INCOMPLETE — fix the misses")
sys.exit(0 if ok else 1)
