#!/usr/bin/env python3
"""D1-D5 docs alignment for the v119 cycle (the persisted alignment-script
precedent — the v118 cycle's align-docs-v118.py form, WITH the
IDEMPOTENT-RUN DUPLICATION TRAP guard on every insert-after edit).

D1  AGENTS.md     — the v119 paragraph appended after the v118 paragraph
D2  CLAUDE.md     — the E2E count 321 -> 322 + the v119 clause appended to
                    the v118 clause's tail
D3  README.md     — the two (321 tests) counts -> 322 + the v119 plan row
                    appended after the v118 row
D4  SKILL.md      — project_state 321 -> 322 + the Session 154 row appended
D5  PAD           — the v1.1.76 revision block inserted before v1.1.75

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
V119_AGENTS = """

Reference surfaces pinned by the v119 iteration (`docs/remediation-plan-v119.md`) — **the re-run cycle's next-oldest candidate (the v113-era DASHBOARD pair — the DASHBOARD at desktop 1280×800 FULL-PAGE, both v61 target surfaces below the fold on the same view: (1) the BUDGET GUIDELINES card (the tinted, bordered 50/30/20 rows) and (2) the QUICK-ACTION card row (the three Add Income / Add Savings / Add Expense card buttons), the pair's NINTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119], the FORTY-SECOND consecutive queue/ledger agreement — the v113 header's own SEVENTH-vs-bracket off-by-one identified before the derivation and the NINTH ordinal fixed IN the derivation per the consistent v112-lineage convention)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only a canary sha prerelease beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds; the engine-contract pin green) + the npm-audit watch at its tenth re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 113th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 113th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). **The verdict IDENTICAL — the SEVENTH consecutive IDENTICAL verdict for this pair [v83 → v89 → v95 → v101 → v107 → v113 → v119]** — the only flags the documented classes: the nav highlight the v56 SUPERSET delta; the avatar letters the USER-IDENTITY data class; the figures the SEED-DATA classes; no FAB flag raised (the v103 standing class). The both-sides census (ARBIT_G 61 lines md5 b500dd29 + ARBIT_Q 58 lines md5 da04e995 + ARBIT_X 25 lines md5 7a381755 — the v101/v107/v113 census blocks VERBATIM) compared AXIS-BY-AXIS by the persisted compare-v119-census.py (**154 axes: 144 identical + 10 documented-class deltas, ZERO new** — the v66 INVISIBLE shadow-lead class; the v61 label-wrapper lesson [the clone's LEAF span byte-identical: 16px/500/rgb(26,58,46)]; the v77 grid-mt mechanism class [the rendered geometry HARD-ASSERTED byte-identical: cardBottom 1122 / gridTop 1462 / gap 340]; the gridCls site-source class) — reproducing the v113 census values EXACTLY (the same 154/144/10 split), zero drift on every axis. **THE PIN — the /dashboard PAGE-HEADER-ROW census at 1280 (the never-pinned family, PIN-ONLY — zero production-code changes)**: the pair's own below-the-fold surfaces are among the most-pinned in the codebase (v61/v77/v83/v89/v95/v101/v107/v113 — every PART G/Q/X census axis family pinned), so the candidate went to the SAME VIEW's never-pinned family per the v118 precedent: the dashboard page-header row — pinned ONLY at 390 before this (the v114 F4 pin: the row's flex chrome + the block→button junction + the Add Item box chrome; the v62 F2 pin: the subtitle block's interior) and at 1280 only POSITION-pinned (the v40 F1 Tab-order band [x 1121, w 127, h 36]; the session-5 gradient; the v35 S2 focus shadow; the G3 Plus-icon geometry). The one-shot both-sides census (drow-arbit-v119.sh — the census JS defined ONCE and eval'd on BOTH sides): **the family BYTE-IDENTICAL on EVERY axis — not even a mechanism axis diverged** (the reference's and the clone's census JSON lines the IDENTICAL string): the row {flex / row / center / space-between / gap 16px / mb 32px / h 72 / w 960}, the h1 {36px md:text-4xl / 700 / lh 40px / mb 8px}, the subtitle {16px / 400 / lh 24px}, the block {h 72 / w 498}, the addBtn {left 1121 / h 36 / w 127 / pad 8px 16px / radius 6px / 14px/500/white / the 135deg forest→lime gradient / icon 16×16 — the band CROSS-VALIDATED against the v40 F1 pin exactly}, the junction {hGap 335 — the justify-between spread}, the nextGap {32 — the mb-8 rendered, the next sibling the lg:grid-cols-3 stat grid}, the docSW 1280. The +1 e2e pin (tests/e2e/dashboard.spec.ts): the page-header row census at 1280 — the row/h1/subtitle/block/addBtn/junction/nextGap family + the docSW guard, the finders STRUCTURAL (the v72 class); the PIN-ONLY form (no red phase — the measured values already hold; the standalone GREEN run + the 48/48 dashboard surface regression). The ship chain 322 e2e zero flakes (86+80+77+82 = 325 executions = 322 unique); 35/35 smoke; **the screenshots 16/16 byte-IDENTICAL (the same-day-seed law)**; the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the menu open with all 5 links + the brand; the sheet closed post-nav; the dashboard clean — the dev-shots scripts derived v118→v119 with the version-swap-only verification). The workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end (npm ci in the foreground after the silent background death + zod 840/840 + BOTH v1243 binaries DIRECT; the fresh-workspace discovery: the sandbox's workspace-root .env carries an ABSOLUTE DATABASE_URL that the Prisma CLI prefers over the repo's — every CLI call now carries the EXPLICIT env prefix; the a11y-filename grep lesson re-hit [a `[a-z-]+` pattern truncated a11y.spec.ts to y.spec.ts] and corrected)."""
insert_after("AGENTS.md",
             "the dev-shots scripts derived v117→v118 with the version-swap-only verification).",
             V119_AGENTS,
             "Reference surfaces pinned by the v119 iteration")

# ---------------- D2: CLAUDE.md ----------------
replace1("CLAUDE.md", "- **E2E (Playwright, 321)**:", "- **E2E (Playwright, 322)**:")
V119_CLAUSE = " and the v119 /dashboard page-header-row census at 1280 (the never-pinned family — the v114 390 pin's desktop twin: the row flex-row/center/gap-4/mb-8 + the h1 md:text-4xl 36px + the subtitle + the block 498×72 + the Add Item box chrome + the junction + the row→grid rhythm 32; measured BYTE-IDENTICAL on both sides — not even a mechanism axis, the cleanest PIN-ONLY form)"
insert_after("CLAUDE.md",
             "the v118 /networth page-header-row census at 1280 (the never-pinned family — the row/chip/h1/subtitle/block/gap chrome; the find: the reference carries its mb-8 on a single-child responsive wrapper where the clone puts it on the row itself — the CONSTRUCT class, zero visual consequence [the gap 32 both sides, the wrapper childCount 1], PIN-ONLY)",
             V119_CLAUSE,
             "the v119 /dashboard page-header-row census")

# ---------------- D3: README.md ----------------
replace1("README.md",
         "e2e/                    # Playwright specs (321 tests) + global setup",
         "e2e/                    # Playwright specs (322 tests) + global setup")
replace1("README.md",
         "npm run test:e2e    # Playwright e2e (321 tests) — needs `npm run build` first",
         "npm run test:e2e    # Playwright e2e (322 tests) — needs `npm run build` first")
V119_ROW = """
| [`docs/remediation-plan-v119.md`](docs/remediation-plan-v119.md) | **The re-run cycle's next-oldest candidate (the v113-era DASHBOARD pair's NINTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119] — the DASHBOARD at desktop 1280×800 FULL-PAGE, both v61 target surfaces below the fold: (1) the BUDGET GUIDELINES card + (2) the QUICK-ACTION card row, last re-shot v113 — now the oldest remaining [v113 < v114 < v115 < v116 < v117 < v118]; the FORTY-SECOND consecutive queue/ledger agreement — the surfaces verified against vlm-shots-v113.sh's own header, the v113 header's SEVENTH-vs-bracket off-by-one identified and the NINTH ordinal fixed in the derivation) + the axe watch (NO DRIFT) + the npm-audit watch (the standing step's tenth cycle: 0 vulnerabilities — the v110 bump holds) + the 113th standing checks + the /dashboard page-header-row census pin at 1280 (PIN-ONLY — +1 e2e = 322)**. **The verdict IDENTICAL — the SEVENTH consecutive IDENTICAL for this pair [v83 → … → v113 → v119]** — the only flags the documented classes (the nav highlight the v56 superset delta; the avatar the user-identity class; the figures the seed-data classes; no FAB flag raised). The two-half census (ARBIT_G 61 lines md5 b500dd29 + ARBIT_Q 58 lines md5 da04e995 + ARBIT_X 25 lines md5 7a381755) compared AXIS-BY-AXIS by the persisted compare-v119-census.py (**154 axes: 144 identical + 10 documented-class deltas, ZERO new** — the v113 values reproduced EXACTLY [the same 154/144/10 split]; the rendered geometry HARD-ASSERTED: cardBottom 1122 / gridTop 1462 / gap 340). **THE PIN — the /dashboard page-header-row census at 1280 (PIN-ONLY, zero production-code changes)**: the pair's own surfaces fully pinned by v61/v77/v83/v89/v95/v101/v107/v113 — the candidate the SAME VIEW's never-pinned 1280 family (the v114 390 pin's desktop twin; at 1280 only the v40 F1 position band existed); the one-shot both-sides census (drow-arbit-v119.sh) measured the family **BYTE-IDENTICAL on EVERY axis — not even a mechanism axis diverged**: the row {flex/row/center/space-between/gap 16px/mb 32px/h 72/w 960}, the h1 {36px md:text-4xl/700/lh 40px/mb 8px}, the subtitle {16px/400/lh 24px}, the block {h 72/w 498}, the addBtn {1121/36/127/pad 8px 16px/radius 6px/14px/500/white/the 135deg gradient/icon 16×16 — cross-validated against the v40 F1 band}, the junction {hGap 335}, the nextGap {32}; the +1 pin the family census + the docSW guard (the finders structural); the PIN-ONLY form (the standalone GREEN + the 48/48 surface regression). The ship: 322 e2e zero flakes across the auditable four-chunk split (86+80+77+82 = 325 executions = 322 unique); 35/35 smoke; **the screenshots 16/16 byte-IDENTICAL (the same-day-seed law)**; the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end + the fresh-workspace discovery (the sandbox workspace-root .env's ABSOLUTE DATABASE_URL preferred by the Prisma CLI over the repo's — the explicit-env-prefix fix on every CLI call). |"""
insert_after("README.md",
             "the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end (npm ci in the foreground + zod 840/840 + BOTH v1243 binaries DIRECT). |",
             V119_ROW,
             "remediation-plan-v119.md")

# ---------------- D4: SKILL.md ----------------
replace1("zero-balance_SKILL.md",
         "project_state: 108 unit tests / 321 e2e tests / 35 smoke steps — all green",
         "project_state: 108 unit tests / 322 e2e tests / 35 smoke steps — all green")
V154_ROW = """| 2026-10-25 | Session 154 — parity iteration v119 (`docs/remediation-plan-v119.md`) | **The re-run cycle's next-oldest candidate (the v113-era DASHBOARD pair's NINTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119] — the BUDGET GUIDELINES card + the QUICK-ACTION card row at desktop 1280×800; the FORTY-SECOND consecutive queue/ledger agreement; the v113 header's SEVENTH-vs-bracket off-by-one fixed in the derivation) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's tenth cycle: 0 vulnerabilities — the v110 bump holds) + the 113th standing checks (ALL GREEN — the mobile menu working the 113th consecutive time) + the /dashboard page-header-row census pin at 1280 (PIN-ONLY — +1 e2e = 322)**: **the verdict IDENTICAL — the SEVENTH consecutive IDENTICAL for this pair [v83 → … → v113 → v119]** — the only flags the documented classes (the nav highlight the v56 superset; the avatar the user-identity class; the figures the seed-data classes; no FAB flag raised); the two-half census (ARBIT_G 61 lines md5 b500dd29 + ARBIT_Q 58 lines md5 da04e995 + ARBIT_X 25 lines md5 7a381755) compared axis-by-axis by the persisted compare-v119-census.py (**154 axes: 144 identical + 10 documented-class deltas, ZERO new** — the v113 values reproduced EXACTLY; the rendered geometry hard-asserted byte-identical); **THE PIN the /dashboard page-header-row census at 1280** (the pair's own surfaces fully pinned by v61/v77/v83/v89/v95/v101/v107/v113 — the candidate the SAME VIEW's never-pinned 1280 family, the v114 390 pin's desktop twin; the one-shot both-sides census drow-arbit-v119.sh measured the family BYTE-IDENTICAL on EVERY axis — not even a mechanism axis diverged: the row {flex/row/center/space-between/gap 16/mb 32/h 72}, the h1 {36px/700/lh 40px/mb 8px}, the subtitle {16px/400/lh 24px}, the block {h 72/w 498}, the addBtn {1121/36/127/the 135deg gradient/icon 16×16 — cross-validated against the v40 F1 band}, the junction {hGap 335}, the nextGap {32}); the +1 pin the family census + the docSW guard (the finders structural); the PIN-ONLY form (the standalone GREEN + the 48/48 surface regression); the ship chain 322 e2e zero flakes (86+80+77+82 = 325 executions), 35/35 smoke, **the screenshots 16/16 byte-IDENTICAL (the same-day-seed law)**, the dev evidence 4/4 byte-identical + VLM-verified; the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end + the workspace-root .env DATABASE_URL discovery (the explicit-env-prefix fix) |** 108/322/35 green |"""
insert_after("zero-balance_SKILL.md",
             "108/321/35 green |",
             "\n" + V154_ROW.strip(),
             "Session 154 — parity iteration v119")

# ---------------- D5: PAD ----------------
V1176_BLOCK = """#### Revision Block — v1.1.76 (Tracked Changes)
- `[UI]` v1.1.76 (2026-10-25) — the v119 parity iteration (**PIN-ONLY — zero production-code changes** + one e2e pin; no dependency change): the counts 108 unit / **322 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v113-era DASHBOARD pair's NINTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119] — the DASHBOARD at desktop 1280×800 FULL-PAGE, both v61 target surfaces below the fold: (1) the BUDGET GUIDELINES card + (2) the QUICK-ACTION card row, last re-shot v113; the FORTY-SECOND consecutive queue/ledger agreement; the v113 header's SEVENTH-vs-bracket off-by-one identified before the derivation and the NINTH ordinal fixed IN it) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's tenth cycle: 0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 113th standing checks (ALL GREEN — the mobile menu working the 113th consecutive time; the reference's four bugs all live; the data census clean on the FIRST reads) + the /dashboard page-header-row census pin at 1280 (+1 e2e = 322)**: **the verdict IDENTICAL — the SEVENTH consecutive IDENTICAL for this pair [v83 → v89 → v95 → v101 → v107 → v113 → v119]** — the only flags the documented classes (the nav highlight the v56 superset delta; the avatar the user-identity data class; the figures the seed-data classes; no FAB flag raised — the v103 standing class); the two-half census (ARBIT_G 61 lines md5 b500dd29 + ARBIT_Q 58 lines md5 da04e995 + ARBIT_X 25 lines md5 7a381755 — the v101/v107/v113 census blocks VERBATIM) compared AXIS-BY-AXIS by the persisted compare-v119-census.py (**154 axes: 144 identical + 10 documented-class deltas, ZERO new** — the v66 INVISIBLE shadow-lead class; the v61 label-wrapper lesson [the clone's LEAF span byte-identical]; the v77 grid-mt mechanism class [the rendered geometry HARD-ASSERTED: cardBottom 1122 / gridTop 1462 / gap 340 / gridParentMt 0px]; the gridCls site-source class) — reproducing the v113 census values exactly (the same 154/144/10 split). **THE PIN — the /dashboard PAGE-HEADER-ROW census at 1280 (the never-pinned family, PIN-ONLY)**: the pair's own below-the-fold surfaces among the most-pinned in the codebase (v61/v77/v83/v89/v95/v101/v107/v113), the candidate the SAME VIEW's never-pinned 1280 family per the v118 precedent — the dashboard page-header row (pinned ONLY at 390 before this [the v114 F4 pin + the v62 F2 pin]; at 1280 only the v40 F1 Tab-order position band [x 1121, w 127, h 36]); the one-shot both-sides census (drow-arbit-v119.sh) measured the family **BYTE-IDENTICAL on EVERY axis — not even a mechanism axis diverged**: the row {flex/row/center/space-between/gap 16px/mb 32px/h 72/w 960}, the h1 {36px md:text-4xl/700/lh 40px/mb 8px}, the subtitle {16px/400/lh 24px}, the block {h 72/w 498}, the addBtn {left 1121/h 36/w 127/pad 8px 16px/radius 6px/fs 14px/fw 500/white/the 135deg forest→lime gradient/icon 16×16 — the band CROSS-VALIDATED against the v40 F1 pin exactly}, the junction {hGap 335 — the justify-between spread}, the nextGap {32 — the mb-8 rendered, the next sibling the lg:grid-cols-3 stat grid}, the docSW 1280. The +1 e2e pin (tests/e2e/dashboard.spec.ts) the page-header row census at 1280 — the row/h1/subtitle/block/addBtn/junction/nextGap family + the docSW guard, the finders STRUCTURAL (the v72 class); the PIN-ONLY form (the standalone GREEN + the 48/48 dashboard surface regression). The ship chain 322 e2e zero flakes (86+80+77+82 = 325 executions across four chunks), 35/35 smoke, **the screenshots 16/16 byte-IDENTICAL (the same-day-seed law)**, the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end + the fresh-workspace discovery (the sandbox workspace-root .env carries an ABSOLUTE DATABASE_URL that the Prisma CLI prefers over the repo's relative URL — every Prisma CLI call now carries the EXPLICIT `DATABASE_URL="file:../db/custom.db"` env prefix; the app itself unaffected [Next.js loads the repo .env only + db-path.ts anchors the relative URL against the repo root]).
"""
t = open("Project_Architecture_Document.md", encoding="utf-8").read()
if "#### Revision Block — v1.1.76" in t:
    print("ALREADY APPLIED: PAD v1.1.76 block — skipped")
elif t.count("#### Revision Block — v1.1.75 (Tracked Changes)") != 1:
    print(f"AMBIGUOUS/MISS: PAD v1.1.75 anchor")
    ok = False
else:
    t = t.replace("#### Revision Block — v1.1.75 (Tracked Changes)",
                  V1176_BLOCK + "#### Revision Block — v1.1.75 (Tracked Changes)", 1)
    open("Project_Architecture_Document.md", "w", encoding="utf-8").write(t)
    print("aligned Project_Architecture_Document.md (the v1.1.76 block)")

sys.exit(0 if ok else 1)
