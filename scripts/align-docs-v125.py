#!/usr/bin/env python3
"""Align the docs for the v125 cycle (Session 160).

D1  AGENTS.md     — the v125 paragraph appended after the v124 paragraph
                    (the v124 paragraph is the file's last content)
D2  CLAUDE.md     — the E2E count 327 -> 328 + the v125 clause
D3  README.md     — the count strings 327 -> 328 (two places) + the v125
                    plan row appended after the v124 row
D4  SKILL.md      — project_state 327 -> 328 + the Session 160 row appended
                    after the Session 159 row
D5  PAD           — the [UI] v1.1.82 revision block (inserted newest-first,
                    before the v1.1.81 block)
D6  probe README  — the v125 section (between the v125 queue and the v121
                    cycle section) + the v126 queue   [align-probereadme-v125.py]
D7  session_306.md + the worklog Session 160 entry (separate steps)

D0 checked clean: the v124 paragraph's tail anchor ('BOTH v1243 playwright
pairs verified in the cache directly, the `.env` + `db/` in place, the
seedcheck exact before any gate).' at the AGENTS.md file end) verified
appearing exactly ONCE — no duplication, the v119-defect class checked and
absent; every insert anchor below verified 1-hit before any write.
"""
import sys

def replace1(path, old, new):
    t = open(path, encoding="utf-8").read()
    n = t.count(old)
    if n != 1:
        print(f"AMBIGUOUS/MISS in {path}: {n} hits for {old[:60]!r}")
        return False
    open(path, "w", encoding="utf-8").write(t.replace(old, new))
    return True

def insert_after(path, anchor, content, marker):
    t = open(path, encoding="utf-8").read()
    if marker in t:
        print(f"ALREADY APPLIED: {path} — {marker[:40]!r}")
        return True
    n = t.count(anchor)
    if n != 1:
        print(f"AMBIGUOUS/MISS in {path}: {n} hits for anchor {anchor[:60]!r}")
        return False
    open(path, "w", encoding="utf-8").write(t.replace(anchor, anchor + content))
    return True

ok = True

# ---------------- D1: AGENTS.md ----------------
V125_AGENTS = """

Reference surfaces pinned by the v125 iteration (`docs/remediation-plan-v125.md`) — **the re-run cycle's next-oldest candidate (the v119-era DASHBOARD pair — the BUDGET GUIDELINES card + the QUICK-ACTION card row, both below the fold on the dashboard at desktop 1280x800 FULL-PAGE, the v61-era pair's surface family, the pair's TENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125], the FORTY-EIGHTH consecutive queue/ledger agreement — THE CORRECTED ENTRIES-MINUS-ONE CONVENTION APPLIED CLEANLY: the v124 cycle's own off-by-one find codified, the ordinal derived from vlm-shots-v119.sh's own header [the NINTH on its 10-entry bracket, v61 the original] — v125 = the TENTH, no prose/prose conflict this cycle)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only the canary 4.14.0-canary.6b52b84 prerelease beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds — one node_modules/axe-core entry verified live; the engine-contract pin green) + the npm-audit watch at its sixteenth re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 119th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 119th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). **The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs this cycle** (lint · typecheck · 108 unit · build · 327 e2e zero flakes [330 executions in 4 chunks] · 35/35 smoke; the post-push commit ca35ae3 audited session-log-only; the production-seam audit clean). **The verdict IDENTICAL ×2 — THE CLEANEST PAIR FORM IN THE LINEAGE: zero layout/style flags both passes, no DOM arbitration needed this cycle** (only the expected DATA classes flagged: the hero allocation % [30.5% vs 62.8%] + balance [$3475.00 vs $2065.00] the PCT/seed-data class; the donut sector percentages + the drill-down amounts the EACH-SITE'S-DATA class). The both-sides census (the THREE blocks of the v119 lineage — the guidelines PART G + the quick-action PART Q + the cross-row PART X, the md5 contracts b500dd29/da04e995/7a381755 verified by direct python extraction [verify-twohalf-v125.py], the v101/v107/v113/v119 lineage values VERBATIM; built by build-twohalf-v125.py derived from build-twohalf-v119.py) compared AXIS-BY-AXIS by the persisted compare-v125-census.py (**154 axes: 144 identical + 10 documented-class deltas, ZERO new** — REPRODUCING the v119 census values EXACTLY, the same 154/144/10 split, zero drift on every axis; the rendered geometry byte-identical: cardBottom 1122 / gridTop 1462 / the cross-row gap 340; the ten documented classes — Gcard.shadow the v4 composed-shadow zero-layer superset [the visible layers byte-identical], Qcards[0..2].label.color/.fw ×6 the wrapper-vs-leaf finder asymmetry [the v61 label lesson's own class; the rendered LEAF chrome byte-identical per the v61 F3 + v107 pins], Qgrid.mt + XgridMt + XgridCls the v83 cross-row family's mt-8 rhythm + responsive class-string superset classes). **THE PIN — the QUICK-ACTION card's HOVER END-STATE census at 1280 (PIN-ONLY — the never-pinned hover paths of the MOST-pinned family on the dashboard, +1 e2e = 328)**: the quick-action family held by FOUR pins (the v45 F3b the CARD's hover:shadow-lg layers — the sole QA `.hover()` in the entire suite; the v61 F3 the AT-REST chrome [the grid 960/3×304/gap 24, the tile 40×40/radius 12, the plus 16/0.5]; the v95 the TRANSITION TIMING metadata; the v107 the interior flex-row at rest) — **the hover END-STATES (the tile's `group-hover:scale-110` at dashboard-view.tsx:890 + the plus's `group-hover:opacity-100` at :899) held by NO spec** (verified across all 24 spec files). The BOTH-SIDES census (`qahover-arbit-v125.sh` — the hover ladder, READ-ONLY on both sites per the v46 rule, the REAL pointer at the live-read card center [440,723 identical both sides], measured cleanly and RE-RUN POST-CYCLE reproducing the values exactly): the at-rest {shadow none / tile {transform none, scale none, 40×40} / plus 0.5} byte-identical → the hovered **rendered parity contract IDENTICAL both sides (the tile 40→44×44, the plus 0.5→1, cardHover true, the shadow's two visible layers byte-identical)** with the COMPUTED FORM the documented class (the reference's Tailwind v3 `transform: matrix(1.1, 0, 0, 1.1, 0, 0)` vs the clone's v4 `scale: "1.1"` — the v95 transition-property class's hover-state twin) → the restored rung back to at-rest exactly. **THE PIN-SANITY MUTATION — the CONDITIONAL form designed-in from the start (the v124 lesson applied at the design stage)**: `group-hover:scale-110` → `group-hover:scale-105` at :890 AND `group-hover:opacity-100` → `group-hover:opacity-90` at :899, both by LINE NUMBER (the identical opacity token at :602 — the guidelines copy affordance — untouched); the conditionality preserved so the at-rest holders (v61 F3, v107) are structurally immune — **the SOLE FAILURE verified live: the pin ALONE red at the hovered axes (the deep-equality diff EXACTLY the predicted 4 lines: tile w/h 44→42 + scale 1.1→1.05 + plus opacity 1→0.9), the file's 48 others green, the mobile-layout 390-side file 6/6 green (the immunity evidence)**; restored + the full rebuild + the 54/54 post-restore regression. The ship chain 328 e2e zero flakes (89+86+74+82 = 331 executions = 328 unique); 35/35 smoke; **the screenshots 16/16 byte-identical (the same-day law — even 07-add-item-modal.png, the v124 day-rollover refresh committed same-day, no refresh needed this cycle)**; the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the dev-shots scripts derived v124→v125 with the version-swap-only verification; the stale :3000 dev server reaped at the dev-evidence phase as planned, the e2e :3100 isolation verified before the gates). The workspace the CARRIED-OVER class (the v124 environment persisted between the cycles — the repo refreshed via git pull to main @ ca35ae3, the operator's session_305.md tail; NO re-provisioning needed: the zod extraction verified intact [840/840], BOTH v1243 playwright pairs verified in the cache directly, the `.env` + `db/` in place, the seedcheck exact before any gate)."""
AGENTS_TAIL = "BOTH v1243 playwright pairs verified in the cache directly, the `.env` + `db/` in place, the seedcheck exact before any gate)."
ok = ok and insert_after("AGENTS.md", AGENTS_TAIL, V125_AGENTS,
             "Reference surfaces pinned by the v125 iteration")

# ---------------- D2: CLAUDE.md ----------------
ok = ok and replace1("CLAUDE.md",
    "- **E2E (Playwright, 327)**:",
    "- **E2E (Playwright, 328)**:")
ok = ok and insert_after("CLAUDE.md",
    "the Tailwind utilities-cascade lesson; the 36 others green)",
    "; the v125 pin — the quick-action card's HOVER END-STATE census at 1280: the never-pinned hover paths of the most-pinned family (the tile's group-hover:scale-110 + the plus's group-hover:opacity-100 — the v45 F3b holds the card's shadow only, the v61 F3/v107 the at-rest chrome, the v95 the timing metadata; the hover ladder: the at-rest rung → the REAL-hover end-states [tile 44×44 scale 1.1, plus opacity 1] → the restore rung; the pin-sanity CONDITIONAL mutations at dashboard-view.tsx:890/:899 sole-failure verified live — the 4-line deep-equality diff exactly as designed, the 48 others + the mobile-layout file green)",
    "the v125 pin — the quick-action card's HOVER END-STATE census")

# ---------------- D3: README.md ----------------
ok = ok and replace1("README.md",
    "│   └── 📂 e2e/                    # Playwright specs (327 tests) + global setup",
    "│   └── 📂 e2e/                    # Playwright specs (328 tests) + global setup")
ok = ok and replace1("README.md",
    "npm run test:e2e    # Playwright e2e (327 tests) — needs `npm run build` first",
    "npm run test:e2e    # Playwright e2e (328 tests) — needs `npm run build` first")
V125_ROW = """
| [`docs/remediation-plan-v125.md`](docs/remediation-plan-v125.md) | **The re-run cycle's next-oldest candidate (the v119-era DASHBOARD pair's TENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125] — the BUDGET GUIDELINES + QUICK-ACTION below-the-fold surfaces at desktop 1280x800; the FORTY-EIGHTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly)** + the axe watch (NO DRIFT — 4.14.0 holds) + the npm-audit watch (0 vulnerabilities, sixteenth re-check) + the 119th standing checks (ALL GREEN — the mobile menu the 119th consecutive pass) + the quick-action card's HOVER END-STATE census pin at 1280 (PIN-ONLY — +1 e2e = 328; the never-pinned hover paths of the most-pinned family — the tile's group-hover:scale-110 + the plus's group-hover:opacity-100; the both-sides census rendered-identical with the computed form the documented v3-matrix/v4-scale class; the CONDITIONAL-form mutations sole-failure verified live) + the baseline fully green on the first chain (the CARRIED-OVER workspace — no re-provisioning) + the VLM pair IDENTICAL ×2 (zero layout/style flags — the cleanest pair form in the lineage) + the census 154 axes — 144 identical + 10 documented, ZERO new + the screenshots 16/16 byte-identical (the same-day law). |"""
ok = ok and insert_after("README.md",
    "the add-item modal's capture-day date input, VLM-verified date-only). |",
    V125_ROW,
    "docs/remediation-plan-v125.md")

# ---------------- D4: zero-balance_SKILL.md ----------------
ok = ok and replace1("zero-balance_SKILL.md",
    "project_state: 108 unit tests / 327 e2e tests / 35 smoke steps — all green",
    "project_state: 108 unit tests / 328 e2e tests / 35 smoke steps — all green")
S160_ROW = """| 2026-10-27 | Session 160 — parity iteration v125 (`docs/remediation-plan-v125.md`) | **The re-run cycle's next-oldest candidate (the v119-era DASHBOARD pair's TENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125] — the BUDGET GUIDELINES + QUICK-ACTION below-the-fold surfaces at 1280x800; the FORTY-EIGHTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly, no off-by-one this cycle)** + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — sixteenth re-check) + the 119th standing checks (ALL GREEN — the reference's four bugs live, the mobile menu the 119th consecutive pass, zero overflow at 390) + the VLM pair (IDENTICAL ×2 — zero layout/style flags both passes, no DOM arbitration needed, the cleanest pair form in the lineage) + the two-half census (154 axes — 144 identical + 10 documented, ZERO new — the v119 values reproduced EXACTLY, the three-block md5 lineage verified) + the quick-action card's HOVER END-STATE census pin at 1280 (PIN-ONLY — the tile's group-hover:scale-110 + the plus's group-hover:opacity-100, never-pinned by the v45/v61/v95/v107 family pins; the both-sides hover census rendered-identical; the CONDITIONAL-form mutations sole-failure verified live — the 4-line diff exactly as designed; +1 e2e = 328) + the ship chain fully green (328 e2e zero flakes [331 executions], 35/35 smoke, the screenshots 16/16 byte-identical [the same-day law], the dev evidence 4/4 byte-identical + VLM-verified) |** 108/328/35 green — the workspace the CARRIED-OVER class (git pull, no re-provisioning) |
"""
ok = ok and insert_after("zero-balance_SKILL.md",
    "108/327/35 green — the workspace the CARRIED-OVER class (git pull, no re-provisioning) |",
    "\n" + S160_ROW,
    "Session 160 — parity iteration v125")

# ---------------- D5: Project_Architecture_Document.md ----------------
V1182_BLOCK = """#### Revision Block — v1.1.82 (Tracked Changes)
- `[UI]` v1.1.82 (2026-10-27) — the v125 parity iteration (**PIN-ONLY — zero production-code changes** + one e2e pin; no dependency change): the counts 108 unit / **328 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v119-era DASHBOARD pair's TENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125] — the BUDGET GUIDELINES + QUICK-ACTION below-the-fold surfaces at desktop 1280x800; the FORTY-EIGHTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly)**; the baseline fully green on the first chain (the CARRIED-OVER workspace — no re-provisioning); the VLM pair **IDENTICAL ×2 — the cleanest pair form in the lineage: zero layout/style flags both passes, no DOM arbitration needed** (only the expected data classes: the hero allocation/balance pct, the donut sectors, the drill-down amounts); the two-half census (the THREE-block v119 lineage, md5 b500dd29/da04e995/7a381755 verified) **154 axes — 144 identical + 10 documented-class deltas, ZERO new** (the v119 values reproduced EXACTLY; the rendered geometry byte-identical: cardBottom 1122 / gridTop 1462 / gap 340); **THE PIN — the quick-action card's HOVER END-STATE census at 1280** (the never-pinned hover paths of the most-pinned family: the tile's `group-hover:scale-110` [dashboard-view.tsx:890] + the plus's `group-hover:opacity-100` [:899] — the v45 F3b holds the card's shadow only, the v61 F3/v107 the at-rest chrome, the v95 the timing metadata; the both-sides hover ladder census rendered-identical — the tile 40→44×44 + the plus 0.5→1 on BOTH sites, the computed form the documented v3-matrix/v4-scale class, the v95 class's hover-state twin; **the CONDITIONAL-form mutations sole-failure verified live — the 4-line deep-equality diff exactly as designed, the v124 cascade lesson applied at the design stage**); the ship chain 328 e2e zero flakes (331 executions in 4 chunks) + 35/35 smoke + the screenshots 16/16 byte-identical (the same-day law — the v124 day-rollover refresh committed same-day) + the dev evidence 4/4 (the menu proof: /income, docSW 390, navLandmark true).
"""
if True:
    t = open("Project_Architecture_Document.md", encoding="utf-8").read()
    if "#### Revision Block — v1.1.82" not in t:
        old = "#### Revision Block — v1.1.81 (Tracked Changes)"
        n = t.count(old)
        if n != 1:
            print(f"D5 AMBIGUOUS: {n} hits")
            ok = False
        else:
            open("Project_Architecture_Document.md", "w", encoding="utf-8").write(
                t.replace(old, V1182_BLOCK + old))
            print("D5: v1.1.82 block inserted (newest-first)")
    else:
        print("D5: v1.1.82 block already present")

print("ALIGN RESULT:", "OK" if ok else "FAIL")
sys.exit(0 if ok else 1)
