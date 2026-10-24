#!/usr/bin/env python3
"""D1-D5 docs alignment for the v113 cycle (the persisted alignment-script
precedent — the v112 cycle's align-docs-v112.py form).

D1  AGENTS.md     — the v113 paragraph appended after the v112 paragraph
D2  CLAUDE.md     — the E2E count 315 -> 316 + the v113 clause appended to
                    the E2E bullet's tail (after the v112 clause)
D3  README.md     — the two (315 tests) counts -> 316 + the v113 plan row
                    appended after the v112 row
D4  SKILL.md      — project_state 315 -> 316 + the Session 148 row appended
D5  PAD           — the v1.1.70 revision block inserted before v1.1.69

Each edit verifies its anchor exists (a miss fails the run loudly).
"""
import sys

ok = True

def edit(path, pairs, mode="replace"):
    global ok
    t = open(path, encoding="utf-8").read()
    for old, new in pairs:
        if mode == "replace":
            if old not in t:
                print(f"MISS in {path}: {old[:80]!r}")
                ok = False
                continue
            if t.count(old) != 1:
                print(f"AMBIGUOUS in {path} ({t.count(old)} hits): {old[:80]!r}")
                ok = False
                continue
            t = t.replace(old, new)
        else:  # insert-after
            if old not in t:
                print(f"MISS in {path}: {old[:80]!r}")
                ok = False
                continue
            t = t.replace(old, old + new, 1)
    open(path, "w", encoding="utf-8").write(t)
    print(f"aligned {path}")

# ---------------- D1: AGENTS.md ----------------
V113_AGENTS = """

Reference surfaces pinned by the v113 iteration (`docs/remediation-plan-v113.md`) — **the re-run cycle's next-oldest candidate (the v107-era BUDGET GUIDELINES + QUICK-ACTION pair — both v61 target surfaces below the fold on the DASHBOARD at desktop 1280x800 FULL-PAGE, last re-shot v107; the pair's EIGHTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113]; the THIRTY-SIXTH consecutive queue/ledger agreement) + the axe watch (NO DRIFT) + the npm-audit watch (the standing step's fourth cycle: 0 vulnerabilities — the v110 bump holds) + the 107th standing checks + the guidelines tile label-row census pin (PIN-ONLY; +1 e2e = 316)**: the verdict IDENTICAL — ZERO layout/style flags on the pair's own target surfaces (the SIXTH consecutive IDENTICAL verdict for this pair [v83 → v89 → v95 → v101 → v107 → v113]; the only flags the documented seed-data classes; no FAB flag raised — the v103 standing class); the two-half census (ARBIT_G 61 lines md5 b500dd29 + ARBIT_Q 58 lines md5 da04e995 + ARBIT_X 25 lines md5 7a381755 — the version-free v101/v107 census blocks carried over VERBATIM), compared axis-by-axis by the persisted compare-v113-census.py (154 axes: 144 identical + 10 deltas, every delta a documented class — the shadow lead-layer count the v66 INVISIBLE class; the quick-action label census delta the v61 label lesson [the finder's wrapper catch; the clone's LEAF carries the identical chrome — the v61 F3 + v107 F4 pins]; the grid mt the v77 mechanism class [the rendered gap byte-identical at 340]; the gridCls strings the site-source class), reproduces the v107 values exactly — the PART X hard axes cardBottom 1122/gridTop 1462/gap 340/gridParentMt 0px byte-identical — NO NEW CLONE GAP. The +1 pin (tests/e2e/dashboard.spec.ts): the Budget Guidelines card's TILE LABEL-ROW family + the tile stack rhythm at 1280 — the row {flex/center/space-between/mb 4px/h 24/w 384/childCount 2} + the tile rhythm {gap1 12/gap2 12} — never pinned at ANY viewport before (the v51 pin the mobile twin at 390 only; the v61 F2 pin the card box + first tile + STRETCH; the v77 pin the header typography + the tiles' TEXT chrome; the v83 pin the card bottom/grid top/gap; the v89 pin the body display); the label/pct x-position axes stay census-documented but UNPINNED (the v107 xInRow discipline); measured byte-identical both sides via the one-shot glrow-arbit-v113.sh (the finders structural: the childless-exact-text heading + the shadow/radius/p card walk-up + the flex-ancestor-of-the-label-that-contains-the-pct row walk); the mutation justify-between → justify-start at dashboard-view.tsx:847 line-scoped (the ONLY mb-1 flex items-center justify-between line in the file) — only the v113 pin red at the row.justify axis alone (space-between → flex-start) after the standalone REBUILD (zero layout boxes moved — the v61/v77/v83/v89/v101/v107/v112 pins green under the mutation); restored, rebuilt, post-restore 46/46 green. The cycle's standing notes: the 107th standing checks' data census clean on the FIRST reads (no render-race hit this cycle); the retained workspace needed NO provisioning repair."""
t = open("AGENTS.md", encoding="utf-8").read()
anchor = "Reference surfaces pinned by the v112 iteration"
if anchor not in t:
    print("MISS: AGENTS.md v112 paragraph anchor")
    ok = False
else:
    # append after the v112 paragraph's LAST line (the file's final paragraph)
    tail_anchor = "the retained workspace needed NO provisioning repair (the playwright cache verified holding BOTH v1243 binaries directly)."
    if tail_anchor not in t:
        print("MISS: AGENTS.md v112 paragraph tail anchor")
        ok = False
    else:
        t = t.replace(tail_anchor, tail_anchor + V113_AGENTS, 1)
        open("AGENTS.md", "w", encoding="utf-8").write(t)
        print("aligned AGENTS.md (the v113 paragraph)")

# ---------------- D2: CLAUDE.md ----------------
V113_CLAUSE = " and the v113 guidelines label-row census (the Budget Guidelines card's tile label-row + the tile stack rhythm at 1280: the row {flex/center/space-between/mb 4px/h 24/w 384/childCount 2} + the rhythm {12/12} — never pinned at ANY viewport; the label/pct x-positions stay unpinned per the v107 xInRow discipline; measured byte-identical both sides by the one-shot glrow-arbit-v113.sh; the mutation justify-between → justify-start at dashboard-view.tsx:847 line-scoped — single-axis row.justify alone, zero layout boxes moved)"
edit("CLAUDE.md", [
    ("- **E2E (Playwright, 315)**:", "- **E2E (Playwright, 316)**:"),
    ("the mutation font-semibold → font-bold at dashboard-view.tsx:532 line-scoped — single-axis label.fw 600→700 alone, the line-135 occurrence untouched)",
     "the mutation font-semibold → font-bold at dashboard-view.tsx:532 line-scoped — single-axis label.fw 600→700 alone, the line-135 occurrence untouched)" + V113_CLAUSE),
])

# ---------------- D3: README.md ----------------
V113_ROW = """
| [`docs/remediation-plan-v113.md`](docs/remediation-plan-v113.md) | **The re-run cycle's next-oldest candidate (the v107-era BUDGET GUIDELINES + QUICK-ACTION pair's EIGHTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113] — both v61 target surfaces below the fold on the DASHBOARD at desktop 1280×800 FULL-PAGE, last re-shot v107 — now the oldest remaining [v107 < v108 < v109 < v110 < v111 < v112]; the THIRTY-SIXTH consecutive queue/ledger agreement — the surface names verified against vlm-shots-v107.sh's own header before the derivation) + the axe watch (NO DRIFT) + the npm-audit watch (the standing step's fourth cycle: 0 vulnerabilities — the v110 bump holds, next 16.4.3 + zod 4.6.7) + the 107th standing checks + the guidelines tile label-row census pin (PIN-ONLY)**. The verdict IDENTICAL — ZERO layout/style flags on the pair's own target surfaces (the SIXTH consecutive IDENTICAL verdict for this pair; no FAB flag raised — the v103 standing class); the two-half census (ARBIT_G 61 + ARBIT_Q 58 + ARBIT_X 25 lines, md5 b500dd29/da04e995/7a381755 — the version-free v101/v107 blocks carried over VERBATIM), compared axis-by-axis by the persisted compare-v113-census.py (154 axes: 144 identical + 10 deltas, all documented classes — the shadow lead-layer count the v66 INVISIBLE class; the label census delta the v61 label lesson [the clone's LEAF identical — the v61 F3 + v107 F4 pins]; the grid mt the v77 mechanism class [the rendered gap byte-identical at 340]; the gridCls the site-source class), reproduces the v107 values exactly — the PART X hard axes byte-identical — NO NEW CLONE GAP; the +1 e2e pins the never-pinned GUIDELINES TILE LABEL-ROW family + the tile stack rhythm at 1280 (the row {flex/center/space-between/mb 4px/h 24/w 384/childCount 2} + the rhythm {gap1 12/gap2 12}; the label/pct x-positions unpinned per the v107 xInRow discipline; 316 e2e total), measured byte-identical both sides via the one-shot glrow-arbit-v113.sh, mutation-verified single-axis AND cascade-free (justify-between → justify-start at dashboard-view.tsx:847 line-scoped — the ONLY mb-1 flex items-center justify-between line; row.justify alone, zero layout boxes moved — the v61/v77/v83/v89/v101/v107/v112 pins green under the mutation). The ship: 316 e2e zero flakes across the auditable four-chunk split (83+77+75+84 = 319 executions = 316 unique); the screenshots 16/16 byte-identical (the same-day-seed law — zero arbitration); the dev evidence re-captured + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); the 107th standing checks' data census clean on the FIRST reads (no render-race hit this cycle). |"""
edit("README.md", [
    ("e2e/                    # Playwright specs (315 tests) + global setup",
     "e2e/                    # Playwright specs (316 tests) + global setup"),
    ("npm run test:e2e    # Playwright e2e (315 tests) — needs `npm run build` first",
     "npm run test:e2e    # Playwright e2e (316 tests) — needs `npm run build` first"),
])
t = open("README.md", encoding="utf-8").read()
row_anchor = "the cold re-login re-read EXACT — the v75 convention, NOT a data change). |"
if row_anchor not in t:
    print("MISS: README v112 row tail anchor")
    ok = False
else:
    t = t.replace(row_anchor, row_anchor + V113_ROW, 1)
    open("README.md", "w", encoding="utf-8").write(t)
    print("aligned README.md (the v113 plan row)")

# ---------------- D4: zero-balance_SKILL.md ----------------
V113_SKILL_ROW = """| 2026-10-24 | Session 148 — parity iteration v113 (`docs/remediation-plan-v113.md`) | **The re-run cycle's next-oldest candidate (the v107-era BUDGET GUIDELINES + QUICK-ACTION pair's EIGHTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113] — both v61 target surfaces below the fold on the DASHBOARD at desktop 1280×800 FULL-PAGE, last re-shot v107, now the oldest remaining [v107 < v108 < v109 < v110 < v111 < v112]; the THIRTY-SIXTH consecutive queue/ledger agreement — the surface names verified against vlm-shots-v107.sh's own header before the derivation) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's fourth cycle: 0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 107th standing checks (ALL GREEN — the mobile menu working the 107th consecutive time; the reference's four bugs all live; the data census clean on the FIRST reads — no render-race hit this cycle) + the guidelines tile label-row census pin at 1280 (PIN-ONLY; +1 e2e = 316)**: the verdict IDENTICAL — ZERO layout/style flags on the pair's own target surfaces (the SIXTH consecutive IDENTICAL verdict for this pair [v83 → v89 → v95 → v101 → v107 → v113]; the only flags the documented seed-data classes; no FAB flag raised — the v103 standing class); the two-half census (ARBIT_G 61 lines md5 b500dd29 + ARBIT_Q 58 lines md5 da04e995 + ARBIT_X 25 lines md5 7a381755 — the version-free v101/v107 census blocks carried over VERBATIM), compared axis-by-axis by the persisted compare-v113-census.py (154 axes: 144 identical + 10 deltas, every delta a documented class — the shadow lead-layer count the v66 INVISIBLE class; the quick-action label census delta the v61 label lesson [the finder's wrapper catch; the clone's LEAF carries the identical chrome — the v61 F3 + v107 F4 pins]; the grid mt the v77 mechanism class [the rendered gap byte-identical at 340]; the gridCls strings the site-source class), reproduces the v107 values exactly on every axis — the PART X hard axes cardBottom 1122/gridTop 1462/gap 340 byte-identical — NO NEW CLONE GAP; the +1 pin (tests/e2e/dashboard.spec.ts) the Budget Guidelines card's TILE LABEL-ROW family + the tile stack rhythm at 1280 — the row {flex/center/space-between/mb 4px/h 24/w 384/childCount 2} + the rhythm {gap1 12/gap2 12} — never pinned at ANY viewport in ANY spec (the label/pct x-position axes stay census-documented but UNPINNED — the v107 xInRow discipline), measured byte-identical both sides via the one-shot glrow-arbit-v113.sh (the finders structural: the childless-exact-text heading + the shadow/radius/p card walk-up + the flex-ancestor-of-the-label-that-contains-the-pct row walk), mutation-verified single-axis AND cascade-free (justify-between → justify-start at dashboard-view.tsx:847 line-scoped — the ONLY mb-1 flex items-center justify-between line in the file; only the v113 pin red at the row.justify axis alone [space-between → flex-start] after the standalone REBUILD; the v61/v77/v83/v89/v101/v107/v112 pins green under the mutation); restored, rebuilt, post-restore 46/46 green; the ship 316 e2e zero flakes (83+77+75+84 = 319 executions = 316 unique); 35/35 smoke; the screenshots 16/16 byte-identical (the same-day-seed law); the dev evidence re-captured + VLM-verified (the menu proof: /income, docSW 390, navLandmark true) |** 108/316/35 green |"""
edit("zero-balance_SKILL.md", [
    ("project_state: 108 unit tests / 315 e2e tests / 35 smoke steps — all green",
     "project_state: 108 unit tests / 316 e2e tests / 35 smoke steps — all green"),
])
t = open("zero-balance_SKILL.md", encoding="utf-8").read()
skill_anchor = "|** 108/315/35 green |"
if skill_anchor not in t:
    print("MISS: SKILL Session 147 row tail anchor")
    ok = False
else:
    t = t.replace(skill_anchor, skill_anchor + "\n" + V113_SKILL_ROW, 1)
    open("zero-balance_SKILL.md", "w", encoding="utf-8").write(t)
    print("aligned zero-balance_SKILL.md (the Session 148 row)")

# ---------------- D5: Project_Architecture_Document.md ----------------
V113_PAD = """#### Revision Block — v1.1.70 (Tracked Changes)
- `[UI]` v1.1.70 (2026-10-24) — the v113 parity iteration (PIN-ONLY for src/ — no production-code change; no dependency change): the counts 108 unit / **316 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v107-era BUDGET GUIDELINES + QUICK-ACTION pair's EIGHTH re-run [v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113] — both v61 target surfaces below the fold on the DASHBOARD at desktop 1280x800 FULL-PAGE, last re-shot v107; the THIRTY-SIXTH consecutive queue/ledger agreement) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's fourth cycle: 0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 107th standing checks (ALL GREEN — the mobile menu working the 107th consecutive time; the reference's four bugs all live; the data census clean on the FIRST reads) + the guidelines tile label-row census pin at 1280 (PIN-ONLY; +1 e2e = 316)**: the verdict IDENTICAL — ZERO layout/style flags on the pair's own target surfaces (the SIXTH consecutive IDENTICAL verdict for this pair; no FAB flag raised — the v103 standing class); the two-half census (ARBIT_G 61 + ARBIT_Q 58 + ARBIT_X 25 lines, md5 b500dd29/da04e995/7a381755 — the version-free v101/v107 blocks carried over VERBATIM), compared axis-by-axis by the persisted compare-v113-census.py (154 axes: 144 identical + 10 deltas, all documented classes — the v66 INVISIBLE shadow class; the v61 label-lesson wrapper catch; the v77 mechanism grid-mt class; the site-source gridCls), reproduces the v107 values exactly — NO NEW CLONE GAP; the +1 pin (tests/e2e/dashboard.spec.ts) the Budget Guidelines card's TILE LABEL-ROW family + the tile stack rhythm at 1280 — the row {flex/center/space-between/mb 4px/h 24/w 384/childCount 2} + the rhythm {gap1 12/gap2 12} — never pinned at ANY viewport in ANY spec (the label/pct x-positions unpinned — the v107 xInRow discipline), measured byte-identical both sides via the one-shot glrow-arbit-v113.sh, mutation-verified single-axis AND cascade-free (justify-between -> justify-start at dashboard-view.tsx:847 line-scoped — only the v113 pin red at row.justify alone after the standalone REBUILD; the v61/v77/v83/v89/v101/v107/v112 pins green under the mutation); restored, rebuilt, post-restore 46/46 green; the ship chain 316 e2e zero flakes (83+77+75+84 = 319 executions across four chunks), 35/35 smoke, the screenshots 16/16 byte-identical (the same-day-seed law), the dev evidence re-captured + VLM-verified.

"""
t = open("Project_Architecture_Document.md", encoding="utf-8").read()
pad_anchor = "#### Revision Block — v1.1.69 (Tracked Changes)"
if pad_anchor not in t:
    print("MISS: PAD v1.1.69 anchor")
    ok = False
else:
    t = t.replace(pad_anchor, V113_PAD + pad_anchor, 1)
    open("Project_Architecture_Document.md", "w", encoding="utf-8").write(t)
    print("aligned Project_Architecture_Document.md (v1.1.70)")

print("D1-D5 done" if ok else "D1-D5 INCOMPLETE — fix the misses")
sys.exit(0 if ok else 1)
