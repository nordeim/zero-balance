#!/usr/bin/env python3
"""D6 + D7 alignment for the v112 cycle.

D6  probe README — the v112 cycle section (the record + the two lessons
    + the v113 queue) appended after the v112 queue
D7  worklog.md   — the ledger tail v111→v112 + the Session 147 entry
                    inserted above Session 146
Plus: docs/session_275.md (the v112 delivery record)
"""
import sys

ok = True

# ---------------- D6: the probe README ----------------
t = open("scripts/parity-probes/README.md", encoding="utf-8").read()
tail_anchor = "(4) the deferred reference-write censuses\n(unchanged — out of bounds under the v46 read-only rule)."
if tail_anchor not in t:
    print("MISS: probe README tail anchor")
    ok = False
else:
    v112_section = """

## The v112 cycle (the v106-era NETWORTH + drill-down-DASHBOARD pair's EIGHTH re-run — Session 147)

The re-run cadence's next-oldest candidate: the v106-era NETWORTH +
drill-down-DASHBOARD pair (the desktop 1280x800 FULL-PAGE NETWORTH view
+ the DASHBOARD's drill-down EXPANDED state, the v60-era pair's
surfaces, last re-shot v106 — now the oldest remaining [v106 < v107 <
v108 < v109 < v110 < v111]; the pair's EIGHTH re-run bracket [v60 ->
v67 -> v76 -> v82 -> v88 -> v94 -> v100 -> v106 -> v112]; the
THIRTY-FIFTH consecutive queue/ledger agreement — the surface names
verified against vlm-shots-v106.sh's own header before the derivation).
PIN-ONLY for src/; the cycle's standing items: the axe watch (NO DRIFT
— 4.14.0 holds, the v68 dedupe verified), the npm-audit watch at its
third re-check (0 vulnerabilities — the v110 bump holds [next 16.4.3 +
zod 4.6.7]), the 106th standing checks (ALL GREEN — the mobile menu the
106th consecutive green; the reference's four bugs all live). The
verdicts: BOTH PAIRS DIFFERENT (the pair's documented verdict class)
with every flag DOM-arbitrated to a documented class (the FAB the
platform-chrome class DISPROVEN live [fabCount 0 + bodyHasBase44 false
on BOTH sides]; the nav-highlight delta the v56 SUPERSET class; the
avatar the user-identity class; the progress fill the pct DATA class
over the byte-identical 568px track; the donut labels the v60
perception class; the stat-card footer "dashed line" a NEW VLM
perception-flag form DISPROVEN live [the leader SOLID + byte-identical
both sides — the v88 pin's family]; the "Total Expense" singular the
v106-documented text-misread re-disproven [statTitles PLURAL on BOTH
sides]; the data figures the seed-data classes). The two-half census
(ARBIT_A 90 lines md5 6fda636c + ARBIT_B 111 lines md5 9a4e73cc — the
block deltas verified version-bump-only, exactly the two census
view-label tokens) reproduces the v106 values exactly — NO NEW CLONE
GAP. The +1 pin (tests/e2e/dashboard.spec.ts): the drill-down card's
NET-BALANCE FOOTER ROW interior at 1280 — the border-t wrapper {mt 12px
/ pt 12px / 1px rgb(229,231,227)} + the row {flex/center/
space-between/h 32} + the left block {flex/center/gap 8px/h 32} + the
chip {32x32/radius 8px/rgba(245,169,98,0.125)} + the chip icon {16x16,
the twin-polyline trending-up glyphSig, 0 0 24 24} + the label
{"Net Balance"/14px/600/rgb(107,114,128)/h 20} + the value {18px/700/
rgb(245,169,98)/h 28} + the junction (chipCy === rowCy === labelCy) —
never pinned at ANY viewport in ANY spec, measured byte-identical both
sides via the one-shot netrow-arbit-v112.sh, mutation-verified
single-axis AND cascade-free (font-semibold -> font-bold at
dashboard-view.tsx:532 line-scoped — the line-135 occurrence
untouched; only the v112 pin red at label.fw alone [600 -> 700] after
the standalone REBUILD). The ship chain: 315 e2e zero flakes (82+80+
72+84 = 318 executions = 315 unique); 35/35 smoke; the screenshots
16/16 byte-identical (the same-day-seed law); the dev evidence
re-captured + VLM-verified.

- THE REGEXP-DOLLAR RULE (a one-shot-census addendum — the v64 rule's
  sharpest form yet): a `new RegExp('^[-+]' + D + '...')` built from
  String.fromCharCode(36) inserts a RAW dollar into the pattern — where
  it is the regex END-ANCHOR, so the money-leaf finder silently matches
  NOTHING ("no value leaf" on both sides, zero errors). The literal
  dollar in a RegExp pattern needs the ESCAPED form: build the
  pattern as '^[-+]\\\\' + D + '[\\\\d,]+...' so the regex receives
  "\\$". Symptom class: a census that returns a finder-miss string on
  BOTH sides with no JS error — check the escape chain BEFORE blaming
  the DOM or the seed.
- THE RENDER-RACE RE-READ (a standing-checks note, the v75 convention
  applied): the reference's data census can read "no match" on ONE
  view after a long eval gap (the session EXPIRES between the R-bug
  checks and the census; the page re-renders the login flash before
  the view hydrates) — the disciplined response is the cold re-login
  re-read, which returned "4 items · $525.00" EXACT this cycle. It is
  the documented session-expiry class, NEVER a reference data change;
  do not re-document the census values off the racy read.

The v113 queue (suggestions — verify against the rotation ledger before
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
    t = t.replace(tail_anchor, tail_anchor + v112_section, 1)
    open("scripts/parity-probes/README.md", "w", encoding="utf-8").write(t)
    print("aligned scripts/parity-probes/README.md (the v112 section + the v113 queue)")

# ---------------- D7: worklog.md ----------------
t = open("worklog.md", encoding="utf-8").read()
ledger_anchor = "`docs/remediation-plan-v111.md` (the v111 cycle — Session 146)."
if ledger_anchor not in t:
    print("MISS: worklog ledger anchor")
    ok = False
else:
    t = t.replace(
        ledger_anchor,
        "`docs/remediation-plan-v112.md` (the v112 cycle — Session 147).",
        1,
    )
    open("worklog.md", "w", encoding="utf-8").write(t)
    print("aligned worklog.md (the ledger tail v111 -> v112)")

V112_WORKLOG = """## Session 147 — Parity iteration v112: the re-run cycle's next-oldest candidate (the v106-era NETWORTH + drill-down-DASHBOARD pair's eighth re-run) + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — the standing step's third cycle) + the 106th standing checks + the drill-down card's Net-Balance footer-row census pin (PIN-ONLY) (2026-10-24)

**The cycle** (`docs/remediation-plan-v112.md` — the plan validated against the codebase before execution; the delivery record: `docs/session_275.md`): the re-run cadence's next-oldest candidate — the v106-era NETWORTH + drill-down-DASHBOARD pair (the desktop 1280x800 FULL-PAGE NETWORTH view + the DASHBOARD's drill-down EXPANDED state, the v60-era pair's surfaces, last re-shot v106 — now the oldest remaining [v106 < v107 < v108 < v109 < v110 < v111]; the pair's EIGHTH re-run bracket [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112]; the THIRTY-FIFTH consecutive queue/ledger agreement — the surface names verified against vlm-shots-v106.sh's own header before the derivation) + the axe watch (NO DRIFT — 4.14.0 holds; the v68 dedupe verified) + the npm-audit watch at its third cycle (0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 106th standing checks + the drill-down card's Net-Balance footer-row census pin at 1280 (PIN-ONLY; +1 e2e = 315).

- **The verdicts BOTH PAIRS DIFFERENT** (the pair's documented verdict class) with every flag DOM-arbitrated to a documented class: the FAB the platform-chrome class DISPROVEN live (the one-shot statfooter-arbit-v112.sh: fabCount 0 + bodyHasBase44 false on BOTH sides); the nav-highlight delta the v56 SUPERSET class; the avatar the user-identity class; the progress fill the pct DATA class over the byte-identical 568px track; the donut labels the v60 perception class; the stat-card footer "dashed line" a NEW VLM perception-flag form DISPROVEN live (the leader borderTopStyle SOLID + byte-identical both sides — the v88 pin's family); the "Total Expense" singular the v106-documented VLM text-misread sub-form re-disproven (statTitles PLURAL on BOTH sides); the data figures the seed-data classes.
- **The two-half census** (ARBIT_A 90 lines md5 6fda636c + ARBIT_B 111 lines md5 9a4e73cc — the block deltas verified version-bump-only, exactly the two census view-label tokens) **reproduces the v106 values exactly on every axis — NO NEW CLONE GAP**.
- **The +1 pin** (tests/e2e/dashboard.spec.ts): the Net Zero Breakdown card's NET-BALANCE FOOTER ROW interior at 1280 — the border-t wrapper {mt 12px/pt 12px/1px rgb(229,231,227)} + the row {flex/center/space-between/h 32} + the left block {flex/center/gap 8px/h 32} + the chip {32×32/radius 8px/rgba(245,169,98,0.125)} + the chip icon {16×16/the twin-polyline trending-up glyphSig/0 0 24 24} + the label {"Net Balance"/14px/600/rgb(107,114,128)/h 20} + the value {18px/700/rgb(245,169,98)/h 28} + the junction (chipCy === rowCy === labelCy) — never pinned at ANY viewport in ANY spec; measured byte-identical both sides via the one-shot netrow-arbit-v112.sh (the value finder the String.fromCharCode(36) escaped-form regex — the v64 rule; the row finder the flex-ancestor-that-contains-the-value walk); mutation-verified single-axis AND cascade-free (font-semibold → font-bold at dashboard-view.tsx:532 line-scoped — the line-135 occurrence untouched; only the v112 pin red at label.fw alone [600 → 700] after the standalone REBUILD); restored, rebuilt, post-restore 45/45 green.
- **The baseline chain FULLY GREEN on the RETAINED workspace** (no reset, no provisioning repair — the playwright cache verified holding BOTH v1243 binaries directly): seedcheck exact (7/1850/2235/0/3/2); lint; typecheck; 108 unit; build (robots + sitemap prerendered); 314 e2e zero flakes across the four-chunk split (81+80+72+84 = 317 executions — the a11y file kept INSIDE chunk 4, the v111 filename-parsing lesson applied); 35/35 smoke; npm audit 0 vulnerabilities; the three post-push commits audited session-log-only.
- **The ship chain**: 315 e2e zero flakes (82+80+72+84 = 318 executions = 315 unique); 35/35 smoke; the screenshots 16/16 byte-identical (the same-day-seed law — zero arbitration); the dev evidence re-captured + VLM-verified (the menu proof: /income, docSW 390, navLandmark true).
- **The 106th standing checks ALL GREEN** — the mobile menu VERIFIED WORKING the 106th consecutive time; the reference's four bugs all live; the expenses census hit the documented render-race/session-expiry class once (the cold re-login re-read "4 items · $525.00" EXACT — the v75 login-retry convention's class, NOT a reference data change); the SEO pair live both sides.
- **The cycle's tooling findings**: THE REGEXP-DOLLAR RULE (the String.fromCharCode(36) census regex needed the escaped `\\$` form — a raw dollar in a RegExp pattern is the END-ANCHOR, silently matching nothing; symptom: a finder-miss on BOTH sides with zero JS errors) + the standing render-race re-read documented.
- The docs aligned D1–D7 (AGENTS the v112 paragraph; CLAUDE 315 + the v112 clause; README counts + the v112 plan row; the SKILL Session 147 row + the state line; PAD v1.1.69; the probe README's v112 section + the two lessons + the v113 queue; this Session 147 entry + the ledger tail); `docs/session_275.md` saved. `.env.example` verified matching the codebase.

---

"""
t = open("worklog.md", encoding="utf-8").read()
s146 = "## Session 146 — Parity iteration v111"
if s146 not in t:
    print("MISS: worklog Session 146 anchor")
    ok = False
else:
    t = t.replace(s146, V112_WORKLOG + s146, 1)
    open("worklog.md", "w", encoding="utf-8").write(t)
    print("aligned worklog.md (the Session 147 entry inserted)")

sys.exit(0 if ok else 1)
