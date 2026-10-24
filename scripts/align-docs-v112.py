#!/usr/bin/env python3
"""D1-D5 docs alignment for the v112 cycle (the persisted alignment-script
precedent — the v111 cycle's align-docs-v111.py form).

D1  AGENTS.md     — the v112 paragraph appended after the v111 paragraph
D2  CLAUDE.md     — the E2E count 314 -> 315 + the v112 clause appended to
                    the E2E bullet's tail (before the Smoke bullet)
D3  README.md     — the two (314 tests) counts -> 315 + the v112 plan row
                    appended after the v111 row
D4  SKILL.md      — project_state 314 -> 315 + the Session 147 row appended
D5  PAD           — the v1.1.69 revision block inserted before v1.1.68

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
V112_AGENTS = """

Reference surfaces pinned by the v112 iteration (`docs/remediation-plan-v112.md`) — **the re-run cycle's next-oldest candidate (the v106-era NETWORTH + drill-down-DASHBOARD pair — the desktop 1280x800 FULL-PAGE NETWORTH view + the DASHBOARD's drill-down EXPANDED state, last re-shot v106; the pair's EIGHTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112]; the THIRTY-FIFTH consecutive queue/ledger agreement) + the axe watch (NO DRIFT) + the npm-audit watch (the standing step's third cycle: 0 vulnerabilities — the v110 bump holds) + the 106th standing checks + the drill-down card's Net-Balance footer-row census pin (PIN-ONLY; +1 e2e = 315)**: the verdicts BOTH PAIRS DIFFERENT (the pair's documented verdict class) with every flag DOM-arbitrated to a documented class (the "Edit with Base44" FAB the platform-chrome class DISPROVEN live [fabCount 0 + bodyHasBase44 false on BOTH sides — the one-shot statfooter-arbit-v112.sh]; the nav-highlight delta the v56 SUPERSET class [the reference's root-route bug: it marks NO nav item active; the clone's Dashboard highlight the superset fix]; the avatar the user-identity class; the progress fill the pct DATA class over the byte-identical 568px track; the donut labels the v60 perception class [the reference's own labels ARE in its DOM — count 4, labelFs 16px, labelFill black, sectors 3 byte-identical; its seed renders them overlapping]; the stat-card footer "dashed line" a NEW VLM perception-flag form DISPROVEN live [the leader reads borderTopStyle SOLID + h 1 + bg rgb(229,231,227) on BOTH sides, byte-identical — the v88 pin's family]; the "Total Expense" singular the v106-documented VLM text-misread sub-form re-disproven [statTitles PLURAL on BOTH sides]; the data figures the seed-data classes); the two-half census (ARBIT_A 90 lines md5 6fda636c + ARBIT_B 111 lines md5 9a4e73cc — the block deltas verified version-bump-only [exactly the two census view-label tokens]) reproduces the v106 values exactly on every axis — NO NEW CLONE GAP. The +1 pin (tests/e2e/dashboard.spec.ts): the Net Zero Breakdown card's NET-BALANCE FOOTER ROW interior — the border-t wrapper {mt 12px/pt 12px/1px rgb(229,231,227)} + the row {flex/center/space-between/h 32} + the left block {flex/center/gap 8px/h 32} + the chip {32×32/radius 8px/rgba(245,169,98,0.125)} + the chip icon {16×16/the twin-polyline trending-up glyphSig/0 0 24 24} + the label {"Net Balance"/14px/600/rgb(107,114,128)/h 20} + the value {18px/700/rgb(245,169,98)/h 28} + the junction (chipCy === rowCy === labelCy) — never pinned at ANY viewport before (the v5-era test pins the amount color + the icon's existence only; the v42/v43/v44/v60/v76/v82 censuses live on different elements); measured byte-identical both sides via the one-shot netrow-arbit-v112.sh (the value finder the String.fromCharCode(36) regex form — the v64 rule; the row finder the flex-ancestor-that-contains-the-value walk — never by class alone); the mutation font-semibold → font-bold at dashboard-view.tsx:532 line-scoped — only the v112 pin red at the label.fw axis alone (600→700) after the standalone REBUILD (the line-135 text-sm font-semibold untouched); restored, rebuilt, post-restore 45/45 green. The cycle's standing notes: the 106th standing checks hit the documented render-race/session-expiry class ONCE on the reference's expenses census ("no match" — the cold re-login re-read "4 items · $525.00" EXACT, the v75 login-retry convention's class, NOT a reference data change); the retained workspace needed NO provisioning repair (the playwright cache verified holding BOTH v1243 binaries directly)."""
t = open("AGENTS.md", encoding="utf-8").read()
anchor = "Reference surfaces pinned by the v111 iteration"
if anchor not in t:
    print("MISS: AGENTS.md v111 paragraph anchor")
    ok = False
else:
    t = t.rstrip("\n") + "\n" + V112_AGENTS.strip() + "\n"
    open("AGENTS.md", "w", encoding="utf-8").write(t)
    print("aligned AGENTS.md (the v112 paragraph appended)")

# ---------------- D2: CLAUDE.md ----------------
V112_CLAUDE_CLAUSE = """ and the v112 net-balance footer-row census (the Net Zero Breakdown card's net row interior: the border-t wrapper {mt 12px/pt 12px/1px rgb(229,231,227)} + the row {flex/center/space-between/h 32} + the left block {flex/gap 8px/h 32} + the 32×32 rounded-lg chip on the 12.5% orangeLight tint + the 16×16 twin-polyline trending-up glyph + the 14px/600 gray label + the 18px/700 value — never pinned at ANY viewport; the v5-era test pins the amount color + the icon's existence only; measured byte-identical both sides by the one-shot netrow-arbit-v112.sh; the mutation font-semibold → font-bold at dashboard-view.tsx:532 line-scoped — single-axis label.fw 600→700 alone, the line-135 occurrence untouched)"""
edit("CLAUDE.md", [
    ("- **E2E (Playwright, 314)**", "- **E2E (Playwright, 315)**"),
    ("the v66 nameH4 pin untouched)", "the v66 nameH4 pin untouched)" + V112_CLAUDE_CLAUSE),
])

# ---------------- D3: README.md ----------------
V112_README_ROW = """| [`docs/remediation-plan-v112.md`](docs/remediation-plan-v112.md) | **The re-run cycle's next-oldest candidate (the v106-era NETWORTH + drill-down-DASHBOARD pair's EIGHTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112] — the desktop 1280×800 FULL-PAGE NETWORTH view + the DASHBOARD's drill-down EXPANDED state, the v60-era pair's surfaces, last re-shot v106 — now the oldest remaining [v106 < v107 < v108 < v109 < v110 < v111]; the THIRTY-FIFTH consecutive queue/ledger agreement) + the axe watch (NO DRIFT) + the npm-audit watch (the standing step's third cycle: 0 vulnerabilities — the v110 bump holds, next 16.4.3 + zod 4.6.7) + the 106th standing checks + the drill-down card's Net-Balance footer-row census pin (PIN-ONLY)**. The verdicts BOTH PAIRS DIFFERENT (the pair's documented verdict class) with every flag DOM-arbitrated — the FAB the platform-chrome class DISPROVEN live (fabCount 0 + bodyHasBase44 false on BOTH sides), the nav-highlight delta the v56 SUPERSET class, the avatar the user-identity class, the progress fill the pct DATA class, the donut labels the v60 perception class, the stat-card footer "dashed line" a new VLM perception-flag DISPROVEN live (the leader SOLID + byte-identical both sides — the v88 pin's family), the "Total Expense" singular the v106-documented text-misread re-disproven (statTitles PLURAL both sides); the two-half census (ARBIT_A 90 lines md5 6fda636c + ARBIT_B 111 lines md5 9a4e73cc — the block deltas version-bump-only) reproduces the v106 values exactly — NO NEW CLONE GAP; the +1 e2e pins the never-pinned NET-BALANCE FOOTER ROW interior at 1280 (the border-t wrapper + the row + the left block + the 32×32 chip + the trending-up glyph + the 14px/600 label + the 18px/700 value + the junction; 315 e2e total), measured byte-identical both sides via the one-shot netrow-arbit-v112.sh, mutation-verified single-axis (font-semibold → font-bold at dashboard-view.tsx:532 line-scoped — label.fw 600→700 alone; the line-135 occurrence untouched). The ship: 315 e2e zero flakes across the auditable four-chunk split (82+80+72+84 = 318 executions = 315 unique); the screenshots 16/16 byte-identical (the same-day-seed law — zero arbitration); the dev evidence re-captured + VLM-verified; the 106th standing checks' expenses census hit the documented render-race class once (the cold re-login re-read EXACT — the v75 convention, NOT a data change). |
"""
edit("README.md", [
    ("Playwright specs (314 tests)", "Playwright specs (315 tests)"),
    ("Playwright e2e (314 tests)", "Playwright e2e (315 tests)"),
], mode="replace")
# append the v112 row after the v111 row
t = open("README.md", encoding="utf-8").read()
v111_row_tail = "verify the cache DIRECTLY — the dry-run is a location report, never an existence proof). |\n"
if v111_row_tail not in t:
    print("MISS: README v111 row tail anchor")
    ok = False
else:
    t = t.replace(v111_row_tail, v111_row_tail + V112_README_ROW, 1)
    open("README.md", "w", encoding="utf-8").write(t)
    print("aligned README.md (the v112 plan row appended)")

# ---------------- D4: SKILL.md ----------------
V112_SKILL_ROW = """| 2026-10-24 | Session 147 — parity iteration v112 (`docs/remediation-plan-v112.md`) | **The re-run cycle's next-oldest candidate (the v106-era NETWORTH + drill-down-DASHBOARD pair's EIGHTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112] — the desktop 1280×800 FULL-PAGE NETWORTH view + the DASHBOARD's drill-down EXPANDED state, the v60-era pair's surfaces, last re-shot v106, now the oldest remaining [v106 < v107 < v108 < v109 < v110 < v111]; the THIRTY-FIFTH consecutive queue/ledger agreement — the surface names verified against vlm-shots-v106.sh's own header before the derivation) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's third cycle: 0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 106th standing checks (ALL GREEN — the mobile menu working the 106th consecutive time; the reference's four bugs all live; the expenses census hit the documented render-race class once — the cold re-login re-read EXACT) + the drill-down card's Net-Balance footer-row census pin at 1280 (PIN-ONLY; +1 e2e = 315)**: the verdicts BOTH PAIRS DIFFERENT (the pair's documented class) with every flag DOM-arbitrated to a documented class (the 'Edit with Base44' FAB the platform-chrome class DISPROVEN live by the one-shot statfooter-arbit-v112.sh [fabCount 0 + bodyHasBase44 false on BOTH sides]; the nav-highlight delta the v56 SUPERSET class; the avatar the user-identity class; the progress fill the pct DATA class over the byte-identical 568px track; the donut labels the v60 perception class; the stat-card footer 'dashed line' a NEW VLM perception-flag form DISPROVEN live [the leader SOLID + h 1 + bg rgb(229,231,227) byte-identical both sides — the v88 pin's family]; the 'Total Expense' singular the v106-documented VLM text-misread sub-form re-disproven [statTitles PLURAL on BOTH sides]; the data figures the seed-data classes); the two-half census (ARBIT_A 90 lines md5 6fda636c + ARBIT_B 111 lines md5 9a4e73cc — the block deltas verified version-bump-only [exactly the two census view-label tokens]) reproduces the v106 values exactly on every axis — NO NEW CLONE GAP; the +1 pin (tests/e2e/dashboard.spec.ts) the Net Zero Breakdown card's NET-BALANCE FOOTER ROW interior at 1280 — the border-t wrapper {mt 12px/pt 12px/1px rgb(229,231,227)} + the row {flex/center/space-between/h 32} + the left block {flex/center/gap 8px/h 32} + the chip {32×32/radius 8px/rgba(245,169,98,0.125)} + the chip icon {16×16/the twin-polyline trending-up glyphSig/0 0 24 24} + the label {'Net Balance'/14px/600/rgb(107,114,128)/h 20} + the value {18px/700/rgb(245,169,98)/h 28} + the junction (chipCy === rowCy === labelCy) — never pinned at ANY viewport in ANY spec, measured byte-identical both sides via the one-shot netrow-arbit-v112.sh (the value finder the String.fromCharCode(36) regex form — the v64 rule; the row finder the flex-ancestor-that-contains-the-value walk — never by class alone), mutation-verified single-axis AND cascade-free (font-semibold → font-bold at dashboard-view.tsx:532 line-scoped — the line-135 text-sm font-semibold untouched; only the v112 pin red at the label.fw axis alone [600 → 700] after the standalone REBUILD; the v42/v43/v44/v60/v76/v88 pins green under the mutation); restored, rebuilt, post-restore 45/45 green; the ship 315 e2e zero flakes (82+80+72+84 = 318 executions = 315 unique); 35/35 smoke; the screenshots 16/16 byte-identical (the same-day-seed law); the dev evidence re-captured + VLM-verified (the menu proof: /income, docSW 390, navLandmark true) |** 108/315/35 green |
"""
edit("zero-balance_SKILL.md", [
    ("project_state: 108 unit tests / 314 e2e tests / 35 smoke steps — all green",
     "project_state: 108 unit tests / 315 e2e tests / 35 smoke steps — all green"),
], mode="replace")
t = open("zero-balance_SKILL.md", encoding="utf-8").read()
s146_anchor = "| 2026-10-24 | Session 146 — parity iteration v111"
if s146_anchor not in t:
    print("MISS: SKILL Session 146 row anchor")
    ok = False
else:
    t = t.replace(s146_anchor, V112_SKILL_ROW + s146_anchor, 1)
    open("zero-balance_SKILL.md", "w", encoding="utf-8").write(t)
    print("aligned zero-balance_SKILL.md (the Session 147 row inserted)")

# ---------------- D5: PAD ----------------
V112_PAD = """#### Revision Block — v1.1.69 (Tracked Changes)
- `[UI]` v1.1.69 (2026-10-24) — the v112 parity iteration (PIN-ONLY for src/ — no production-code change; no dependency change): the counts 108 unit / **315 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v106-era NETWORTH + drill-down-DASHBOARD pair's EIGHTH re-run [v60 -> v67 -> v76 -> v82 -> v88 -> v94 -> v100 -> v106 -> v112] — the desktop 1280x800 FULL-PAGE NETWORTH view + the DASHBOARD's drill-down EXPANDED state, the v60-era pair's surfaces, last re-shot v106; the THIRTY-FIFTH consecutive queue/ledger agreement) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's third cycle: 0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 106th standing checks (ALL GREEN — the mobile menu working the 106th consecutive time; the reference's four bugs all live; the expenses census hit the documented render-race class once — the cold re-login re-read EXACT, the v75 convention) + the drill-down card's Net-Balance footer-row census pin at 1280 (PIN-ONLY; +1 e2e = 315)**: the verdicts BOTH PAIRS DIFFERENT (the pair's documented verdict class) with every flag DOM-arbitrated to a documented class (the 'Edit with Base44' FAB the platform-chrome class DISPROVEN live [fabCount 0 + bodyHasBase44 false on BOTH sides — the one-shot statfooter-arbit-v112.sh]; the nav-highlight delta the v56 SUPERSET class; the avatar the user-identity class; the progress fill the pct DATA class over the byte-identical 568px track; the donut labels the v60 perception class [the reference's own labels ARE in its DOM — count 4/labelFs 16px/labelFill black/sectors 3 byte-identical; its seed renders them overlapping]; the stat-card footer 'dashed line' a NEW VLM perception-flag form DISPROVEN live [the leader borderTopStyle SOLID + h 1 + bg rgb(229,231,227) byte-identical both sides — the v88 pin's family]; the 'Total Expense' singular the v106-documented VLM text-misread sub-form re-disproven [statTitles PLURAL on BOTH sides]; the data figures the seed-data classes); the two-half census (ARBIT_A 90 lines md5 6fda636c + ARBIT_B 111 lines md5 9a4e73cc — the block deltas verified version-bump-only) reproduces the v106 values exactly — NO NEW CLONE GAP; the +1 pin (tests/e2e/dashboard.spec.ts) the Net Zero Breakdown card's NET-BALANCE FOOTER ROW interior at 1280 — the border-t wrapper {mt 12px/pt 12px/1px rgb(229,231,227)} + the row {flex/center/space-between/h 32} + the left block {flex/center/gap 8px/h 32} + the chip {32x32/radius 8px/rgba(245,169,98,0.125)} + the chip icon {16x16/the twin-polyline trending-up glyphSig/0 0 24 24} + the label {'Net Balance'/14px/600/rgb(107,114,128)/h 20} + the value {18px/700/rgb(245,169,98)/h 28} + the junction centers — never pinned at ANY viewport in ANY spec, measured byte-identical both sides via the one-shot netrow-arbit-v112.sh (the value finder the String.fromCharCode(36) regex form; the row finder the flex-ancestor-that-contains-the-value walk), mutation-verified single-axis AND cascade-free (font-semibold -> font-bold at dashboard-view.tsx:532 line-scoped — the line-135 occurrence untouched; only the v112 pin red at label.fw alone [600 -> 700] after the standalone REBUILD); restored, rebuilt, post-restore 45/45 green; the ship chain 315 e2e zero flakes (82+80+72+84 = 318 executions across four chunks), 35/35 smoke, the screenshots 16/16 byte-identical (the same-day-seed law), the dev evidence re-captured + VLM-verified.

"""
t = open("Project_Architecture_Document.md", encoding="utf-8").read()
pad_anchor = "#### Revision Block — v1.1.68 (Tracked Changes)"
if pad_anchor not in t:
    print("MISS: PAD v1.1.68 anchor")
    ok = False
else:
    t = t.replace(pad_anchor, V112_PAD + pad_anchor, 1)
    open("Project_Architecture_Document.md", "w", encoding="utf-8").write(t)
    print("aligned Project_Architecture_Document.md (the v1.1.69 block inserted)")

sys.exit(0 if ok else 1)
