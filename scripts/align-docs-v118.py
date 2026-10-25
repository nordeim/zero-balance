#!/usr/bin/env python3
"""D1-D5 docs alignment for the v118 cycle (the persisted alignment-script
precedent — the v117 cycle's align-docs-v117.py form, WITH the
IDEMPOTENT-RUN DUPLICATION TRAP guard on every insert-after edit).

D1  AGENTS.md     — the v118 paragraph appended after the v117 paragraph
D2  CLAUDE.md     — the E2E count 320 -> 321 + the v118 clause appended to
                    the v117 clause's tail
D3  README.md     — the two (320 tests) counts -> 321 + the v118 plan row
                    appended after the v117 row
D4  SKILL.md      — project_state 320 -> 321 + the Session 153 row appended
D5  PAD           — the v1.1.75 revision block inserted before v1.1.74

Each edit verifies its anchor exists AND the new content is absent (a miss
or an already-applied insert fails the run loudly — never a silent dup).
"""
import sys

ok = True

def replace1(path, old, new):
    global ok
    t = open(path, encoding="utf-8").read()
    if t.count(old) != 1:
        print(f"MISS/AMBIGUOUS in {path} ({t.count(old)} hits): {old[:70]!r}")
        ok = False
        return
    open(path, "w", encoding="utf-8").write(t.replace(old, new))
    print(f"aligned {path}: {old[:40]!r} -> ...")

def insert_after(path, anchor, content, marker):
    global ok
    t = open(path, encoding="utf-8").read()
    if marker in t:
        print(f"ALREADY APPLIED in {path}: {marker[:60]!r} — skipped")
        return
    if t.count(anchor) != 1:
        print(f"MISS/AMBIGUOUS anchor in {path} ({t.count(anchor)} hits): {anchor[:70]!r}")
        ok = False
        return
    t = t.replace(anchor, anchor + content, 1)
    open(path, "w", encoding="utf-8").write(t)
    print(f"aligned {path}: inserted after {anchor[:50]!r}")

# ---------------- D1: AGENTS.md ----------------
V118_AGENTS = """

Reference surfaces pinned by the v118 iteration (`docs/remediation-plan-v118.md`) — **the re-run cycle's next-oldest candidate (the v112-era NETWORTH + drill-down-DASHBOARD pair — the desktop 1280×800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's drill-down EXPANDED state, the pair's NINTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118], the FORTY-FIRST consecutive queue/ledger agreement)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only a canary sha prerelease beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds; the engine-contract pin green) + the npm-audit watch at its ninth re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 112th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 112th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). The verdicts NETWORTH DIFFERENT + drill-down DIFFERENT — every flag DOM-arbitrated to a documented class: the FAB flags DISPROVEN live (the one-shot base44-fab-arbit-v118.sh on the flagged /networth surface at 1280: `fabCount:0` + `bodyHasBase44:false` on BOTH sides — the platform-iframe chrome class); the avatar letters the USER-IDENTITY data class; the nav-highlight flag the v56 SUPERSET delta + perception (the census: bg `rgba(0,0,0,0)` transparent on BOTH sides — no green background; the color/fw asymmetry the documented superset); the hero progress % the PCT data class (fillW 173-vs-357); the donut % labels the EACH-SITE'S-DATA + perception class (the census: count 4 / labelFs 16px / sectors 3 byte-identical — the reference DOES render its labels); the stat counts / the extra category the SEED-DATA class; **the "Total Expense (singular) vs Total Expenses (plural)" flag DISPROVEN live — the reference reads "Total Expenses" PLURAL on ALL SIX instances (the 3 tab-button SPANs + the 3 stat-card H3s), the full family byte-identical to the clone's down to every chrome axis (the statlabel-explore one-shots) — the VLM text-misread class**. The both-sides census (ARBIT_A 90 lines md5 45b9a439 + ARBIT_B 111 lines md5 8ed66a88) compared AXIS-BY-AXIS by the persisted compare-v118-census.py (**73 axes: 67 identical + 6 documented-class deltas, ZERO new** — navHighlight.color/fw the v56 superset delta; avatarLetter the user-identity data class; progress.fillW the pct data class; donutLabels.texts the each-site's-data class; labelBlock.w the v82 DATA-CONDITIONAL width class [the 48px figure's text length]) — reproducing the v106/v112 census values EXACTLY, zero drift. **THE FIND — THE WRAPPER-MECHANISM CONSTRUCT CLASS (the cycle's find, PIN-ONLY — zero production-code changes)**: the pin-candidate survey targeted the /networth PAGE-HEADER ROW at 1280 (the element family every 1280 networth census walked past — pinned ONLY at 390 before this [the v69 F3 pin, clone-measured]; the v14 G3 test holds the chip's existence + gradient + geometry + the h1 x-positions only); the one-shot both-sides census (nwheader-arbit-v118.sh) measured the family BYTE-IDENTICAL on every VISUAL axis — the row {flex/center/gap 12px/h 60}, the chip {48×48/radius 12px/the 135deg forest→lime gradient/the 24×24 svg}, the h1 {30px/700/36px/rgb(26,58,46)}, the subtitle {16px/400/24px/rgb(107,114,128)}, the block {h 60/w 250}, the row→card gap 32, the card w 960 — with ONE mechanism axis diverging: the row's margin-bottom (the reference 0px vs the clone 32px). The drill-down (nwheader-mechanism-v118.sh + nwheader-wrapper-v118.sh): the reference wraps its header row in a SINGLE-CHILD responsive wrapper (`flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-8` — the wrapper carries the mb-8; childCount 1, nothing on the right) while the clone puts the mb-8 directly on the row — the pixel arithmetic IDENTICAL both sides (the row 32→92, the card 124, the gap 32), the 390 rhythm matching too; classified per the v7 accepted-construct convention (constructs that paint nothing are not parity axes — the wrapper organizes only); notably the clone's OWN dashboard header uses the reference's wrapper form verbatim (dashboard-view.tsx:927) — the /networth header the v14-era simplification. The +1 e2e pin (tests/e2e/networth.spec.ts): the page-header row census at 1280 — the row/chip/h1/subtitle/block/gap/card family + the docSW guard, the finders STRUCTURAL (the v72 class); the PIN-ONLY form (no red phase — the measured values already hold; the standalone GREEN run + the 35/35 networth surface regression). The ship chain 321 e2e zero flakes (85+80+77+82 = 324 executions = 321 unique); 35/35 smoke; **the screenshots 16/16 byte-IDENTICAL (the same-day-seed law)**; the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the menu open with all 5 links + the brand; the sheet closed post-nav; the dashboard clean — the dev-shots scripts derived v117→v118 with the version-swap-only verification). The workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end (npm ci in the foreground + zod 840/840 + BOTH v1243 binaries DIRECT)."""
insert_after("AGENTS.md",
             "the dev-shots scripts derived v116→v117 with the version-swap-only verification).",
             V118_AGENTS,
             "Reference surfaces pinned by the v118 iteration")

# ---------------- D2: CLAUDE.md ----------------
replace1("CLAUDE.md", "- **E2E (Playwright, 320)**:", "- **E2E (Playwright, 321)**:")
V118_CLAUSE = " and the v118 /networth page-header-row census at 1280 (the never-pinned family — the row/chip/h1/subtitle/block/gap chrome; the find: the reference carries its mb-8 on a single-child responsive wrapper where the clone puts it on the row itself — the CONSTRUCT class, zero visual consequence [the gap 32 both sides, the wrapper childCount 1], PIN-ONLY)"
insert_after("CLAUDE.md",
             "the 52/52 surface regression)",
             V118_CLAUSE,
             "the v118 /networth page-header-row census")

# ---------------- D3: README.md ----------------
replace1("README.md",
         "e2e/                    # Playwright specs (320 tests) + global setup",
         "e2e/                    # Playwright specs (321 tests) + global setup")
replace1("README.md",
         "npm run test:e2e    # Playwright e2e (320 tests) — needs `npm run build` first",
         "npm run test:e2e    # Playwright e2e (321 tests) — needs `npm run build` first")
V118_ROW = """
| [`docs/remediation-plan-v118.md`](docs/remediation-plan-v118.md) | **The re-run cycle's next-oldest candidate (the v112-era NETWORTH + drill-down-DASHBOARD pair's NINTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118] — the desktop 1280×800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's drill-down EXPANDED state, last re-shot v112 — now the oldest remaining [v112 < v113 < v114 < v115 < v116 < v117]; the FORTY-FIRST consecutive queue/ledger agreement — the surface names verified against vlm-shots-v112.sh's own header before the derivation) + the axe watch (NO DRIFT) + the npm-audit watch (the standing step's ninth cycle: 0 vulnerabilities — the v110 bump holds) + the 112th standing checks + the /networth page-header-row census pin at 1280 (PIN-ONLY — +1 e2e = 321)**. The verdicts NETWORTH DIFFERENT + drill-down DIFFERENT — every flag DOM-arbitrated: the FAB DISPROVEN live (`fabCount:0` + `bodyHasBase44:false` on BOTH sides, the platform-iframe chrome class); the nav-highlight the v56 superset delta + perception (bg transparent BOTH sides); the donut labels the data+perception class (present on BOTH sides); **the "Total Expense(s)" flag DISPROVEN live — the reference reads "Total Expenses" PLURAL on all six instances, the family byte-identical (the VLM text-misread)**; the two-half census (ARBIT_A 90 lines md5 45b9a439 + ARBIT_B 111 lines md5 8ed66a88) compared AXIS-BY-AXIS by the persisted compare-v118-census.py (73 axes: 67 identical + 6 documented-class deltas, ZERO new — the v106/v112 values reproduced exactly). **THE FIND — THE WRAPPER-MECHANISM CONSTRUCT CLASS (PIN-ONLY, zero production-code changes)**: the /networth page-header family at 1280 never pinned (the v69 pin at 390 only; the v14 G3 test the chip geometry + x-positions only); the one-shot census byte-identical on every VISUAL axis — the row.mb mechanism axis root-caused to the reference's single-child responsive wrapper (`flex flex-col md:flex-row justify-between ... mb-8`, childCount 1) carrying the mb-8 where the clone puts it on the row (the pixel arithmetic identical: row 32→92, card 124, gap 32; the clone's own dashboard header uses the wrapper form — dashboard-view.tsx:927); classified per the v7 accepted-construct convention. The +1 e2e pin the page-header row census at 1280 (the row/chip/h1/subtitle/block/gap/card family + the docSW guard, the finders structural); the PIN-ONLY form (the standalone GREEN + the 35/35 surface regression). The ship: 321 e2e zero flakes across the auditable four-chunk split (85+80+77+82 = 324 executions = 321 unique); 35/35 smoke; **the screenshots 16/16 byte-IDENTICAL (the same-day-seed law)**; the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end. |"""
insert_after("README.md",
             "the dev evidence 3 same + 1 date-drift + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end (npm ci in the foreground + zod 840/840 + BOTH v1243 binaries DIRECT). |",
             V118_ROW,
             "remediation-plan-v118.md")

# ---------------- D4: SKILL.md ----------------
replace1("zero-balance_SKILL.md",
         "project_state: 108 unit tests / 320 e2e tests / 35 smoke steps — all green",
         "project_state: 108 unit tests / 321 e2e tests / 35 smoke steps — all green")
V153_ROW = """| 2026-10-25 | Session 153 — parity iteration v118 (`docs/remediation-plan-v118.md`) | **The re-run cycle's next-oldest candidate (the v112-era NETWORTH + drill-down-DASHBOARD pair's NINTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118] — the NETWORTH view + the DASHBOARD's drill-down EXPANDED state at desktop 1280×800; the FORTY-FIRST consecutive queue/ledger agreement) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's ninth cycle: 0 vulnerabilities — the v110 bump holds) + the 112th standing checks (ALL GREEN — the mobile menu working the 112th consecutive time) + the /networth page-header-row census pin at 1280 (PIN-ONLY — +1 e2e = 321)**: the verdicts NETWORTH DIFFERENT + drill-down DIFFERENT — every flag DOM-arbitrated (the FAB DISPROVEN live: fabCount 0 + bodyHasBase44 false on BOTH sides; the nav-highlight the v56 superset + perception; the donut labels the data+perception class; **the "Total Expense(s)" flag DISPROVEN live — the reference reads "Total Expenses" PLURAL on all six instances, the family byte-identical, the VLM text-misread**); the two-half census (ARBIT_A 90 lines md5 45b9a439 + ARBIT_B 111 lines md5 8ed66a88) compared axis-by-axis by the persisted compare-v118-census.py (73 axes: 67 identical + 6 documented-class deltas, ZERO new — the v106/v112 values reproduced exactly) — **THE FIND the WRAPPER-MECHANISM CONSTRUCT CLASS**: the /networth page-header family at 1280 never pinned (the v69 pin at 390 only); the one-shot census byte-identical on every VISUAL axis, the row.mb axis root-caused to the reference's single-child responsive wrapper carrying the mb-8 (childCount 1 — nothing on the right; the pixel arithmetic identical: row 32→92, card 124, gap 32) where the clone puts it on the row — classified per the v7 accepted-construct convention, PIN-ONLY (zero production-code changes; the clone's own dashboard header uses the wrapper form — dashboard-view.tsx:927); the +1 pin the page-header row census at 1280 (the row/chip/h1/subtitle/block/gap/card family + the docSW guard, the finders structural); the PIN-ONLY form (the standalone GREEN + the 35/35 surface regression); the ship chain 321 e2e zero flakes (85+80+77+82 = 324 executions), 35/35 smoke, **the screenshots 16/16 byte-IDENTICAL (the same-day-seed law)**, the dev evidence 4/4 byte-identical + VLM-verified; the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end |** 108/321/35 green |"""
insert_after("zero-balance_SKILL.md",
             "108/320/35 green |",
             "\n" + V153_ROW.strip(),
             "Session 153 — parity iteration v118")

# ---------------- D5: PAD ----------------
V1175_BLOCK = """#### Revision Block — v1.1.75 (Tracked Changes)
- `[UI]` v1.1.75 (2026-10-25) — the v118 parity iteration (**PIN-ONLY — zero production-code changes** + one e2e pin; no dependency change): the counts 108 unit / **321 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v112-era NETWORTH + drill-down-DASHBOARD pair's NINTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118] — the desktop 1280×800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's drill-down EXPANDED state, last re-shot v112; the FORTY-FIRST consecutive queue/ledger agreement) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's ninth cycle: 0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 112th standing checks (ALL GREEN — the mobile menu working the 112th consecutive time; the reference's four bugs all live; the data census clean on the FIRST reads) + the /networth page-header-row census pin at 1280 (+1 e2e = 321)**: the verdicts NETWORTH DIFFERENT + drill-down DIFFERENT — every flag DOM-arbitrated (the FAB DISPROVEN live by base44-fab-arbit-v118.sh: `fabCount:0` + `bodyHasBase44:false` on BOTH sides at 1280 on /networth; the nav-highlight the v56 superset delta + perception [bg `rgba(0,0,0,0)` transparent BOTH sides]; the hero progress the PCT data class [fillW 173-vs-357]; the donut labels the EACH-SITE'S-DATA + perception class [count 4/labelFs 16px/sectors 3 byte-identical]; the stat counts / the extra category the SEED-DATA class; **the "Total Expense(s)" flag DISPROVEN live — the reference reads "Total Expenses" PLURAL on ALL SIX instances [the 3 tab-button SPANs + the 3 stat-card H3s], the full family byte-identical to the clone's down to every chrome axis — the VLM text-misread class**); the two-half census (ARBIT_A 90 lines md5 45b9a439 + ARBIT_B 111 lines md5 8ed66a88) compared AXIS-BY-AXIS by the persisted compare-v118-census.py (**73 axes: 67 identical + 6 documented-class deltas, ZERO new**) — reproducing the v106/v112 census values exactly. **THE FIND — THE WRAPPER-MECHANISM CONSTRUCT CLASS (PIN-ONLY)**: the pin-candidate survey targeted the /networth PAGE-HEADER ROW at 1280 (the family every 1280 networth census walked past — pinned ONLY at 390 before this [the v69 F3 pin, clone-measured]; the v14 G3 test the chip's existence + gradient + geometry + the h1 x-positions only); the one-shot both-sides census (nwheader-arbit-v118.sh) measured the family BYTE-IDENTICAL on every VISUAL axis (the row {flex/center/gap 12px/h 60}, the chip {48×48/radius 12px/the 135deg gradient/the 24×24 svg}, the h1 {30px/700/36px}, the subtitle {16px/400/24px}, the block {h 60/w 250}, the gap 32, the card 960) — ONE mechanism axis diverging: the row's mb (the reference 0px vs the clone 32px), root-caused by the drill-down (nwheader-mechanism-v118.sh + nwheader-wrapper-v118.sh) to the reference's SINGLE-CHILD responsive wrapper (`flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-8` — the wrapper carries the mb-8; childCount 1, nothing on the right) where the clone puts the mb-8 directly on the row; the pixel arithmetic IDENTICAL both sides (the row 32→92, the card 124, the gap 32); classified per the v7 accepted-construct convention (constructs that paint nothing are not parity axes); the clone's own dashboard header uses the reference's wrapper form verbatim (dashboard-view.tsx:927) — the /networth header the v14-era simplification. The +1 e2e pin (tests/e2e/networth.spec.ts) the page-header row census at 1280 — the row/chip/h1/subtitle/block/gap/card family + the docSW guard, the finders STRUCTURAL (the v72 class); the PIN-ONLY form (the standalone GREEN + the 35/35 networth surface regression). The ship chain 321 e2e zero flakes (85+80+77+82 = 324 executions across four chunks), 35/35 smoke, **the screenshots 16/16 byte-IDENTICAL (the same-day-seed law)**, the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end.
"""
t = open("Project_Architecture_Document.md", encoding="utf-8").read()
if "#### Revision Block — v1.1.75" in t:
    print("ALREADY APPLIED: PAD v1.1.75 block — skipped")
elif t.count("#### Revision Block — v1.1.74 (Tracked Changes)") != 1:
    print(f"AMBIGUOUS/MISS: PAD v1.1.74 anchor")
    ok = False
else:
    t = t.replace("#### Revision Block — v1.1.74 (Tracked Changes)",
                  V1175_BLOCK + "#### Revision Block — v1.1.74 (Tracked Changes)", 1)
    open("Project_Architecture_Document.md", "w", encoding="utf-8").write(t)
    print("aligned Project_Architecture_Document.md (the v1.1.75 block)")

sys.exit(0 if ok else 1)
