#!/usr/bin/env python3
"""Align the docs for the v126 cycle (Session 161).

D1  AGENTS.md     — the v126 paragraph appended after the v125 paragraph
                    (the v125 paragraph is the file's last content; the
                    anchor carries the v125-unique tokens [main @ ca35ae3,
                    session_305.md] — the generic tail string appears in
                    BOTH the v124 and v125 paragraphs)
D2  CLAUDE.md     — the E2E count 328 -> 329 + the v126 clause
D3  README.md     — the count strings 328 -> 329 (two places) + the v126
                    plan row appended after the v125 row
D4  SKILL.md      — project_state 328 -> 329 + the Session 161 row appended
                    after the Session 160 row
D5  PAD           — the [UI] v1.1.83 revision block (inserted newest-first,
                    before the v1.1.82 block)
D6  probe README  — the v126 section (between the v126 queue and the v121
                    cycle section) + the v127 queue   [align-probereadme-v126.py]
D7  session_308.md + the worklog Session 161 entry (separate steps)

D0 checked clean: every insert anchor below verified 1-hit before any write
(the AGENTS anchor disambiguated by the v125-unique git-pull tokens).
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
V126_AGENTS = """

Reference surfaces pinned by the v126 iteration (`docs/remediation-plan-v126.md`) — **the re-run cycle's next-oldest candidate (the v120-era MOBILE 390x844 full-page TWINS pair — BOTH mobile twins: (1) the /NETWORTH view [the v63-era pair's surface] + (2) the DASHBOARD [the v62-era mobile twin's surface], the pair's TENTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126], the FORTY-NINTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly: the ordinal derived from vlm-shots-v120.sh's own header [the NINTH on its 10-entry bracket, v62/v63 the originals] — v126 = the TENTH, no prose/header conflict)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only the canary 4.14.0-canary.6b52b84 prerelease beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds — one node_modules/axe-core entry verified live; the engine-contract pin green) + the npm-audit watch at its seventeenth re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 120th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 120th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). **The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs this cycle** (lint · typecheck · 108 unit · build · 328 e2e zero flakes [331 executions in 4 chunks] · 35/35 smoke; the post-push commits 50a06eb + f018ede audited session-log-only [docs/session_307.md alone, 136 insertions]; the production-seam audit clean). **The verdict BOTH PAIRS DIFFERENT ×2 — the consistent form, the pair's DOCUMENTED VERDICT CLASS** (the same verdict family as the v84/v90/v96/v102/v108/v114/v120 re-runs) — every flag in the documented classes, arbitration-free: the "Edit with Base44" tooltip the platform-chrome class; the summary-card tiles side-by-side-vs-stacked + the card height the v41 MOBILE-SUPERSET class (the reference's own 464px overflow + fixed 2-col tiles vs the clone's fitting 1-col stack); the trend-icon circle the PERCEPTION-ARTIFACT class (the contradictory descriptions across the passes — the census axis trendIcon 32×32 byte-identical both sides, the v120 arbitration's own disproof form); the hero allocation % + balance the PCT/seed-data class; the donut sector proportions + the stat-card item counts the EACH-SITE'S-DATA/seed-data classes. The both-sides census (the TWO blocks of the v120 lineage — NW_CENSUS + DASH_CENSUS, the md5 contracts 82cf8a43/85e4ec7e verified by direct THREE-WAY python extraction [verify-twohalf-v126.py — the source + both halves], the v102/v108/v114/v120 lineage values VERBATIM; built by build-twohalf-v126.py derived from build-twohalf-v120.py with the lesson-range bump v92..v125 + the lineage-note fixup) compared AXIS-BY-AXIS by the persisted compare-v126-census.py (**55 axes: 37 identical + 18 documented-class deltas, ZERO new** — REPRODUCING the v120 census values EXACTLY, the same 55/37/18 split, zero drift on every axis). **THE PIN — the Spending Breakdown DONUT'S GEOMETRY census at 390 (PIN-ONLY — the never-pinned family on the mobile twin #2's own surface, +1 e2e = 329)**: the donut's RENDERED GEOMETRY held by NO spec at ANY viewport (the v9/v14 pins the DATA order + the hover tooltip's sector FILL; the v31 pin the keyboard semantics; the v44 F3 + v49 pins the LEGEND at 1280/390; the v76 pin the LABEL CHROME at 1280 [count/fs/lineCount — never the geometry]; the v101 pin the CARD BOX + header at 1280 — the 390 header twin rejected as the collision; the v42 F2 the 640 scrollHeight — the reason the mutation must be height-neutral). The BOTH-SIDES census (`donut-arbit-v126.sh` — READ-ONLY on both sides per the v46 rule, login + passive navigation only; the finders TAG-AGNOSTIC [the "Spending Breakdown" title a plain div on both sites — the v42 idiom; the card by the v78 radius/white walk]; the pie circle measured as the UNION BBOX of the sector paths; measured cleanly on the FIRST run): **the pie circle 200×200 / r 100 byte-identical both sides** (the outerRadius 100 rendered diameter — the reference's recharts 2.15 and the clone's 3.10 agreeing byte-for-byte) + the donut wrapper {h 300, relative} + the svg {h 300} + the card {h 656} identical + sectorCount 3 + labelCount 4 + labelLineCount 0 identical — the WIDTH family alone the documented DASH width-guard class (the reference's own 395px overflow vs the clone's fitting 390: docSW 395/390, card.w 363/358, wrap.w + svg.w 313/308, pieCircle.cx 197/195 — the centering consequence). **THE PIN-SANITY MUTATION — the HEIGHT-NEUTRAL form (designed against the collision map)**: `outerRadius={100}` → `{90}` at dashboard-view.tsx:730 (the only outerRadius line) — height-neutral by design (the v42 F2 scrollHeight 3029 guard: the circle shrinks WITHIN the fixed 300px wrapper, the wrapper/svg/card heights + the page scrollHeight structurally immune); the immunity map verified live (the v76 label chrome, the v49 legend, the v14/v31/v9 donut pins, the v78/v44 breakdown pins) — **the SOLE FAILURE verified live: the pin ALONE red, the deep-equality diff EXACTLY the predicted 3 lines (w/h 200→180, r 100→90; the cxInSvg/cyInSvg centering axes UNAFFECTED — the shrunken circle stays centered), the full dashboard file's 48 others green, the mobile-layout 390-side file 6/6 green**; restored + the full rebuild + the 55/55 post-restore regression. The pin's card-walk typing hardened to the v78 HTMLElement-null union form after the build's TypeScript step caught the first form (the standalone rebuild then the run — the pin GREEN on the first run after the fix). The ship chain 329 e2e zero flakes (90+86+74+82 = 332 executions = 329 unique); 35/35 smoke; **the screenshots 16/16 byte-identical (the same-day law — no refresh needed this cycle)**; the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the dev-shots scripts derived v125→v126 with the version-swap-only verification; the stale :3000 HUNG-SERVER LOCK reaped — the SIGTERM-surviving next-server with its listening socket already dead, the SIGKILL + the .next/dev/lock removal the fix, the v124 lesson's second instance). The workspace the CARRIED-OVER class (the v125 environment persisted between the cycles — the repo refreshed via git pull to main @ f018ede, the operator's session_307.md tail; NO re-provisioning needed: the zod extraction verified intact [840/840], BOTH v1243 playwright pairs verified in the cache directly, the `.env` + `db/` in place, the seedcheck exact before any gate)."""
AGENTS_TAIL = "the repo refreshed via git pull to main @ ca35ae3, the operator's session_305.md tail; NO re-provisioning needed: the zod extraction verified intact [840/840], BOTH v1243 playwright pairs verified in the cache directly, the `.env` + `db/` in place, the seedcheck exact before any gate)."
ok = ok and insert_after("AGENTS.md", AGENTS_TAIL, V126_AGENTS,
             "Reference surfaces pinned by the v126 iteration")

# ---------------- D2: CLAUDE.md ----------------
ok = ok and replace1("CLAUDE.md",
    "- **E2E (Playwright, 328)**:",
    "- **E2E (Playwright, 329)**:")
ok = ok and insert_after("CLAUDE.md",
    "the 48 others + the mobile-layout file green)",
    "; the v126 pin — the Spending Breakdown DONUT'S GEOMETRY census at 390: the never-pinned family at ANY viewport (the v9/v14 pins the data order + the tooltip fill, the v31 the keyboard semantics, the v44 F3/v49 the legend, the v76 the label chrome at 1280, the v101 the card box at 1280 — the rendered geometry [the svg's w/h, the pie circle's bbox/center/radius] held by NO spec); the both-sides census byte-identical on the circle (200×200/r 100) with the width family the documented width-guard class alone; the pin-sanity HEIGHT-NEUTRAL mutation (outerRadius 100→90 at dashboard-view.tsx:730 — the v42 F2 scrollHeight guard the design constraint) sole-failure verified live — the 3-line deep-equality diff exactly as designed [w/h/r alone, the centering axes unaffected], the 48 others + the mobile-layout file green)",
    "the v126 pin — the Spending Breakdown DONUT'S GEOMETRY census")

# ---------------- D3: README.md ----------------
ok = ok and replace1("README.md",
    "│   └── 📂 e2e/                    # Playwright specs (328 tests) + global setup",
    "│   └── 📂 e2e/                    # Playwright specs (329 tests) + global setup")
ok = ok and replace1("README.md",
    "npm run test:e2e    # Playwright e2e (328 tests) — needs `npm run build` first",
    "npm run test:e2e    # Playwright e2e (329 tests) — needs `npm run build` first")
V126_ROW = """
| [`docs/remediation-plan-v126.md`](docs/remediation-plan-v126.md) | **The re-run cycle's next-oldest candidate (the v120-era MOBILE 390x844 full-page TWINS pair's TENTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126] — the /networth view + the DASHBOARD, both full-page at mobile 390x844; the FORTY-NINTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly)** + the axe watch (NO DRIFT — 4.14.0 holds) + the npm-audit watch (0 vulnerabilities, seventeenth re-check) + the 120th standing checks (ALL GREEN — the mobile menu the 120th consecutive pass) + the Spending Breakdown DONUT'S GEOMETRY census pin at 390 (PIN-ONLY — +1 e2e = 329; the never-pinned family at ANY viewport — the pie circle 200×200/r 100 byte-identical both sides, the width family the documented width-guard class alone; the HEIGHT-NEUTRAL mutation sole-failure verified live — the 3-line diff exactly as designed) + the baseline fully green on the first chain (the CARRIED-OVER workspace — no re-provisioning) + the VLM pair BOTH PAIRS DIFFERENT ×2 (the pair's documented verdict class — every flag in the documented classes, arbitration-free) + the census 55 axes — 37 identical + 18 documented, ZERO new (the v120 values reproduced EXACTLY) + the screenshots 16/16 byte-identical (the same-day law). |"""
ok = ok and insert_after("README.md",
    "+ the screenshots 16/16 byte-identical (the same-day law). |",
    V126_ROW,
    "docs/remediation-plan-v126.md")

# ---------------- D4: zero-balance_SKILL.md ----------------
ok = ok and replace1("zero-balance_SKILL.md",
    "project_state: 108 unit tests / 328 e2e tests / 35 smoke steps — all green",
    "project_state: 108 unit tests / 329 e2e tests / 35 smoke steps — all green")
S161_ROW = """| 2026-10-27 | Session 161 — parity iteration v126 (`docs/remediation-plan-v126.md`) | **The re-run cycle's next-oldest candidate (the v120-era MOBILE 390x844 full-page TWINS pair's TENTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126] — the /networth view + the DASHBOARD, both full-page at mobile 390x844; the FORTY-NINTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly)** + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — seventeenth re-check) + the 120th standing checks (ALL GREEN — the reference's four bugs live, the mobile menu the 120th consecutive pass, zero overflow at 390) + the VLM pair (BOTH PAIRS DIFFERENT ×2 — the pair's documented verdict class, every flag in the documented classes, arbitration-free) + the two-half census (55 axes — 37 identical + 18 documented, ZERO new — the v120 values reproduced EXACTLY, the two-block md5 lineage verified three-way) + the Spending Breakdown DONUT'S GEOMETRY census pin at 390 (PIN-ONLY — the never-pinned family at ANY viewport; the both-sides census byte-identical on the pie circle 200×200/r 100; the HEIGHT-NEUTRAL mutation sole-failure verified live — the 3-line diff exactly as designed; +1 e2e = 329) + the ship chain fully green (329 e2e zero flakes [332 executions], 35/35 smoke, the screenshots 16/16 byte-identical [the same-day law], the dev evidence 4/4 byte-identical + VLM-verified) |** 108/329/35 green — the workspace the CARRIED-OVER class (git pull, no re-provisioning) |
"""
ok = ok and insert_after("zero-balance_SKILL.md",
    "108/328/35 green — the workspace the CARRIED-OVER class (git pull, no re-provisioning) |",
    "\n" + S161_ROW,
    "Session 161 — parity iteration v126")

# ---------------- D5: Project_Architecture_Document.md ----------------
V1183_BLOCK = """#### Revision Block — v1.1.83 (Tracked Changes)
- `[UI]` v1.1.83 (2026-10-27) — the v126 parity iteration (**PIN-ONLY — zero production-code changes** + one e2e pin; no dependency change): the counts 108 unit / **329 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v120-era MOBILE 390x844 full-page TWINS pair's TENTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126] — the /networth view + the DASHBOARD, both full-page at mobile 390x844; the FORTY-NINTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly)**; the baseline fully green on the first chain (the CARRIED-OVER workspace — no re-provisioning); the VLM pair **BOTH PAIRS DIFFERENT ×2 — the pair's documented verdict class** (every flag in the documented classes, arbitration-free: the platform chrome, the v41 mobile-superset stacking, the trend-icon perception class, the PCT/seed-data, the each-site's-data); the two-half census (the TWO-block v120 lineage, md5 82cf8a43/85e4ec7e verified three-way) **55 axes — 37 identical + 18 documented-class deltas, ZERO new** (the v120 values reproduced EXACTLY); **THE PIN — the Spending Breakdown DONUT'S GEOMETRY census at 390** (the never-pinned family at ANY viewport: the v9/v14 pins the data order + the tooltip fill, the v31 the keyboard semantics, the v44 F3/v49 the legend, the v76 the label chrome at 1280, the v101 the card box at 1280; the both-sides census: **the pie circle 200×200 / r 100 byte-identical both sides** — the reference's recharts 2.15 and the clone's 3.10 agreeing byte-for-byte — with the width family alone the documented width-guard class [the reference's own 395px overflow]; the pin holds the card/wrap/svg boxes + the pie circle's bbox/center-in-svg/radius + the sector settle guard; **the HEIGHT-NEUTRAL mutation [outerRadius 100→90 at dashboard-view.tsx:730 — the v42 F2 scrollHeight guard the design constraint] sole-failure verified live — the 3-line deep-equality diff exactly as designed, the centering axes unaffected, the 48 others + the mobile-layout file green**); the ship chain 329 e2e zero flakes (332 executions in 4 chunks) + 35/35 smoke + the screenshots 16/16 byte-identical (the same-day law) + the dev evidence 4/4 (the menu proof: /income, docSW 390, navLandmark true; the stale :3000 hung-server lock reaped — the SIGKILL + lock-removal form).
"""
if True:
    t = open("Project_Architecture_Document.md", encoding="utf-8").read()
    if "#### Revision Block — v1.1.83" not in t:
        old = "#### Revision Block — v1.1.82 (Tracked Changes)"
        n = t.count(old)
        if n != 1:
            print(f"D5 AMBIGUOUS: {n} hits")
            ok = False
        else:
            open("Project_Architecture_Document.md", "w", encoding="utf-8").write(
                t.replace(old, V1183_BLOCK + old))
            print("D5: v1.1.83 block inserted (newest-first)")
    else:
        print("D5: v1.1.83 block already present")

print("ALIGN RESULT:", "OK" if ok else "FAIL")
sys.exit(0 if ok else 1)
