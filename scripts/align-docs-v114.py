#!/usr/bin/env python3
"""D1-D5 docs alignment for the v114 cycle (the persisted alignment-script
precedent — the v113 cycle's align-docs-v113.py form, WITH the
IDEMPOTENT-RUN DUPLICATION TRAP guard: every insert-after edit first checks
the inserted content is ABSENT — the anchor text SURVIVES the insertion, so
a re-run would duplicate; the guard makes the re-run a no-op instead).

D1  AGENTS.md     — the v114 paragraph appended after the v113 paragraph
D2  CLAUDE.md     — the E2E count 316 -> 317 + the v114 clause appended to
                    the E2E bullet's tail (after the v113 clause)
D3  README.md     — the two (316 tests) counts -> 317 + the v114 plan row
                    appended after the v113 row
D4  SKILL.md      — project_state 316 -> 317 + the Session 149 row appended
D5  PAD           — the v1.1.71 revision block inserted before v1.1.70

Each edit verifies its anchor exists AND the new content is absent (a miss
or an already-applied insert fails the run loudly — never a silent dup).
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
        else:  # insert-after WITH the idempotency guard
            if new.strip() and new.strip() in t:
                print(f"ALREADY APPLIED in {path}: {new[:80]!r}")
                ok = False
                continue
            if old not in t:
                print(f"MISS in {path}: {old[:80]!r}")
                ok = False
                continue
            t = t.replace(old, old + new, 1)
    open(path, "w", encoding="utf-8").write(t)
    print(f"aligned {path}")

# ---------------- D1: AGENTS.md ----------------
V114_AGENTS = """

Reference surfaces pinned by the v114 iteration (`docs/remediation-plan-v114.md`) — **the re-run cycle's next-oldest candidate (the v108-era MOBILE TWINS pair — BOTH mobile 390x844 full-page twins: the /NETWORTH view [the v63-era pair's surface] and the DASHBOARD [the v62-era mobile twin's surface], last re-shot v108; the pair's EIGHTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114]; the THIRTY-SEVENTH consecutive queue/ledger agreement) + the axe watch (NO DRIFT) + the npm-audit watch (the standing step's fifth cycle: 0 vulnerabilities — the v110 bump holds) + the 108th standing checks + the dashboard header-row census pin at 390 (PIN-ONLY; +1 e2e = 317)**: the verdicts BOTH PAIRS DIFFERENT — the pair's documented verdict class (the v84/v90/v96/v102/v108 re-run family) — with every flag DOM-arbitrated to a documented class (the stat-tile side-by-side-vs-stacked the v41 mobile-superset class [statGrid cols 2-col-vs-1-col, gap 16px identical, tiles h 84 byte-identical]; the summary-card height the same class's width consequence [432×333 vs 358×421]; the trend-circle claim the VLM MISREAD class [medallion 64×64 + trendIcon 32×32 byte-identical]; the NEW tab-bar alignment flag — the first time raised for this pair — the v41 width-consequence class with the centering claim DISPROVEN live [jc center + ai center byte-identical both sides; the w 432-vs-358 + the gridCols + the tabs' w the reference's own 464px overflow width class; every non-width axis byte-identical] by the one-shot fabtab-arbit-v114.sh; the 'Edit with Base44' overlay — flagged on BOTH pairs — the platform-chrome class DISPROVEN live [fabCount 0 + bodyHasBase44 false on BOTH sides at BOTH surfaces]; the subtitle wrap-point the v62 width-delta class [chrome byte-identical, blockH 92, exactly 2 DOM lines both sides, tops 123/147]; the progress-bar geometry the pct DATA class [the fill width each site's own allocation over the byte-identical track]; the data figures the seed-data classes); the two-half census (NW_CENSUS 42 lines md5 82cf8a43 + DASH_CENSUS 87 lines md5 85e4ec7e — the version-free v102/v108 census blocks carried over VERBATIM) reproduces the v108 values EXACTLY on every axis (the NW summary card 432×333/358×421 + statGrid + tiles + medallion [clipsViewport ref true/clone false — the R-bug-4 consequence] + trendIcon; the DASH subtitle 363×48/358×48 + computed identical + blockH 92 + 2 lines tops 123/147 + breakdownCard h 324/svgCount 7/the 16-14 alternation + the spendingCard finder's SAME fallback string both sides; the docSW guards ref 464/395 vs clone 390/390 — the superset invariant) — NO NEW CLONE GAP. The +1 pin (tests/e2e/dashboard.spec.ts): the DASHBOARD mobile twin's HEADER-ROW interior family at 390 — the row {flex/column/flex-start/space-between/gap 16px/mb 32px/h 144} + the block {h 92/bottom 169} + the junction {gap 16} + the Add Item button's BOX chrome {36×127/pad 8px 16px/radius 6px/14px/500/white/the 135deg gradient/icon 16×16} — never pinned at ANY viewport in ANY spec (the v62 pin walks the block's interior, never the row; the session-5 pin the gradient; the v35 S2 the focus shadow; the G3 the icon; the v52/v65/v109 pins the items-view headers — different elements); the block's/button's x positions + absolute y values stay census-documented but UNPINNED (the v107 position-arithmetic discipline); measured byte-identical both sides via the one-shot drow-arbit-v114.sh (the finders structural: the childless-exact-text h1 + the parentElement block walk [the v62 lesson] + the parentElement row walk + the row's button-with-text walk); the mutation items-start → items-center at dashboard-view.tsx:927 line-scoped (the ONLY mb-8 flex flex-col justify-between items-start gap-4 line in the file) — only the v114 pin red at the row.align axis alone (flex-start → center) after the standalone REBUILD (the cross-axis alignment moves only the unpinned x positions — the block/bottom, the button's top/h, the junction, the row's h, the goalCard.y 253 all green under the mutation; the >=768px rendering untouched by the md: override); restored, rebuilt, post-restore 47/47 green. The cycle's provisioning note: the RESET workspace class (the v113 environment did not persist) — the v108 FRESH-CLONE lesson applied end-to-end (npm ci + the zod extraction verified 840/840 with src/v4 present BEFORE any gate + BOTH v1243 playwright binaries verified DIRECTLY + .env + db push/seed); the 108th standing checks' data census clean on the FIRST reads (no render-race hit this cycle)."""
edit("AGENTS.md", [("the retained workspace needed NO provisioning repair.", "the retained workspace needed NO provisioning repair." + V114_AGENTS)], mode="insert-after")

# ---------------- D2: CLAUDE.md ----------------
V114_CLAUSE = " and the v114 dashboard header-row census (the mobile twin's header ROW at 390: the row {flex/column/flex-start/space-between/gap 16px/mb 32px/h 144} + the block→button junction {gap 16} + the Add Item button's box chrome {36×127/pad 8px 16px/radius 6px/14px/500/white/gradient/icon 16×16} — never pinned at ANY viewport; the x positions unpinned per the v107 discipline; measured byte-identical both sides by the one-shot drow-arbit-v114.sh; the mutation items-start → items-center at dashboard-view.tsx:927 line-scoped — single-axis row.align alone, the cross-axis move touches no vertical box)"
edit("CLAUDE.md", [
    ("- **E2E (Playwright, 316)**:", "- **E2E (Playwright, 317)**:"),
    ("single-axis row.justify alone, zero layout boxes moved)",
     "single-axis row.justify alone, zero layout boxes moved)" + V114_CLAUSE),
])

# ---------------- D3: README.md ----------------
V114_ROW = """
| [`docs/remediation-plan-v114.md`](docs/remediation-plan-v114.md) | **The re-run cycle's next-oldest candidate (the v108-era MOBILE TWINS pair's EIGHTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114] — BOTH mobile 390×844 full-page twins: the /NETWORTH view [the v63-era pair's surface] and the DASHBOARD [the v62-era mobile twin's surface], last re-shot v108 — now the oldest remaining [v108 < v109 < v110 < v111 < v112 < v113]; the THIRTY-SEVENTH consecutive queue/ledger agreement — the surface names verified against vlm-shots-v108.sh's own header before the derivation) + the axe watch (NO DRIFT) + the npm-audit watch (the standing step's fifth cycle: 0 vulnerabilities — the v110 bump holds, next 16.4.3 + zod 4.6.7) + the 108th standing checks + the dashboard header-row census pin at 390 (PIN-ONLY)**. The verdicts BOTH PAIRS DIFFERENT — the pair's documented verdict class — with every flag DOM-arbitrated to a documented class (the stat-tile stacking the v41 mobile-superset class; the summary-card height its width consequence; the trend-circle the VLM MISREAD class; the NEW tab-alignment flag the v41 width-consequence class with the centering DISPROVEN live [jc/ai center byte-identical both sides]; the 'Edit with Base44' overlay — flagged on BOTH pairs — the platform-chrome class DISPROVEN live [fabCount 0 + bodyHasBase44 false both sides both surfaces]; the subtitle wrap the v62 width-delta class; the progress bar the pct DATA class; the data figures the seed-data classes); the two-half census (NW_CENSUS 42 + DASH_CENSUS 87 lines, md5 82cf8a43/85e4ec7e — the version-free v102/v108 blocks carried over VERBATIM) reproduces the v108 values exactly on every axis (the docSW guards ref 464/395 vs clone 390/390 — the superset invariant) — NO NEW CLONE GAP; the +1 e2e pins the never-pinned DASHBOARD HEADER-ROW interior family at 390 (the row {flex/column/flex-start/space-between/gap 16px/mb 32px/h 144} + the block {h 92} + the junction {gap 16} + the Add Item button's box chrome {36×127/pad 8px 16px/radius 6px/14px/500/white/gradient/icon 16×16}; the x positions + absolute y unpinned per the v107 discipline; 317 e2e total), measured byte-identical both sides via the one-shot drow-arbit-v114.sh, mutation-verified single-axis AND cascade-free (items-start → items-center at dashboard-view.tsx:927 line-scoped — the ONLY mb-8 flex flex-col justify-between items-start gap-4 line; row.align alone — the cross-axis move touches no vertical box, the >=768px rendering untouched by the md: override — the v62/hero-reflow/v42-band/session-5/v35/G3 pins green under the mutation). The ship: 317 e2e zero flakes across the auditable four-chunk split (84+77+75+84 = 320 executions = 317 unique); the screenshots 16/16 byte-identical (the same-day-seed law — zero arbitration); the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end (npm ci + zod 840/840 + BOTH v1243 binaries DIRECT). |"""
edit("README.md", [
    ("e2e/                    # Playwright specs (316 tests) + global setup",
     "e2e/                    # Playwright specs (317 tests) + global setup"),
    ("npm run test:e2e    # Playwright e2e (316 tests) — needs `npm run build` first",
     "npm run test:e2e    # Playwright e2e (317 tests) — needs `npm run build` first"),
])
t = open("README.md", encoding="utf-8").read()
row_anchor = "the 107th standing checks' data census clean on the FIRST reads (no render-race hit this cycle). |"
if V114_ROW.strip() in t:
    print("ALREADY APPLIED: README.md v114 row")
    ok = False
elif row_anchor not in t:
    print("MISS: README.md v113 row tail anchor")
    ok = False
else:
    t = t.replace(row_anchor, row_anchor + V114_ROW, 1)
    open("README.md", "w", encoding="utf-8").write(t)
    print("aligned README.md (the v114 row)")

# ---------------- D4: SKILL.md ----------------
V149_ROW = """
| 2026-10-24 | Session 149 — parity iteration v114 (`docs/remediation-plan-v114.md`) | **The re-run cycle's next-oldest candidate (the v108-era MOBILE TWINS pair's EIGHTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114] — BOTH mobile 390×844 full-page twins: the /NETWORTH view [the v63-era pair's surface] and the DASHBOARD [the v62-era mobile twin's surface], last re-shot v108, now the oldest remaining [v108 < v109 < v110 < v111 < v112 < v113]; the THIRTY-SEVENTH consecutive queue/ledger agreement — the surface names verified against vlm-shots-v108.sh's own header before the derivation) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's fifth cycle: 0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 108th standing checks (ALL GREEN — the mobile menu working the 108th consecutive time; the reference's four bugs all live; the data census clean on the FIRST reads — no render-race hit this cycle) + the dashboard header-row census pin at 390 (PIN-ONLY; +1 e2e = 317)**: the verdicts BOTH PAIRS DIFFERENT — the pair's documented verdict class (the v84/v90/v96/v102/v108 re-run family) — with every flag DOM-arbitrated to a documented class (the stat-tile stacking the v41 mobile-superset class; the summary-card height the width consequence; the trend-circle the VLM MISREAD class [medallion 64×64 + trendIcon 32×32 byte-identical]; the NEW tab-bar alignment flag — the first time raised — the v41 width-consequence class with the centering DISPROVEN live [jc/ai center byte-identical both sides; the w/gridCols/tabs-w the reference's own 464px overflow class] by the one-shot fabtab-arbit-v114.sh; the 'Edit with Base44' overlay — flagged on BOTH pairs — the platform-chrome class DISPROVEN live [fabCount 0 + bodyHasBase44 false both sides both surfaces]; the subtitle wrap the v62 width-delta class; the progress bar the pct DATA class; the data figures the seed-data classes); the two-half census (NW_CENSUS 42 lines md5 82cf8a43 + DASH_CENSUS 87 lines md5 85e4ec7e — the version-free v102/v108 census blocks carried over VERBATIM) reproduces the v108 values exactly on every axis (the NW card 432×333/358×421 + statGrid cols/gap 16 + tiles 176×84/294×84 h-84-identical + medallion 64×64 clipsViewport ref-true/clone-false + trendIcon 32×32; the DASH subtitle 363×48/358×48 + computed identical + blockH 92 + 2 lines tops 123/147 + breakdownCard h 324/svgCount 7/16-14 alternation + the spendingCard SAME fallback string; docSW 464/395 vs 390/390) — NO NEW CLONE GAP; the +1 pin (tests/e2e/dashboard.spec.ts) the DASHBOARD mobile twin's HEADER-ROW interior family at 390 — the row {flex/column/flex-start/space-between/gap 16px/mb 32px/h 144} + the block {h 92/bottom 169} + the junction {gap 16} + the Add Item button's box chrome {36×127/pad 8px 16px/radius 6px/14px/500/white/gradient/icon 16×16} — never pinned at ANY viewport in ANY spec (the v62 pin the block interior; the session-5 the gradient; the v35 S2 the focus shadow; the G3 the icon; the v52/v65/v109 the items-view headers), measured byte-identical both sides via the one-shot drow-arbit-v114.sh (the finders structural: the childless-exact-text h1 + the parentElement block walk + the parentElement row walk + the button-with-text walk), mutation-verified single-axis AND cascade-free (items-start → items-center at dashboard-view.tsx:927 line-scoped — the ONLY mb-8 flex flex-col justify-between items-start gap-4 line; only the v114 pin red at row.align alone [flex-start → center] after the standalone REBUILD; the cross-axis move touches no vertical box — the v62 block pin/hero-reflow goalCard.y 253/v42 band census/session-5/v35/G3 green under the mutation; the >=768px rendering untouched by the md: override); restored, rebuilt, post-restore 47/47 green; the ship 317 e2e zero flakes (84+77+75+84 = 320 executions = 317 unique); 35/35 smoke; the screenshots 16/16 byte-identical (the same-day-seed law); the dev evidence 4/4 byte-identical + re-captured + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end (npm ci + the zod extraction 840/840 verified BEFORE any gate + BOTH v1243 playwright binaries verified DIRECTLY) |** 108/317/35 green |"""
edit("zero-balance_SKILL.md", [
    ("state: 108 unit tests / 316 e2e tests / 35 smoke steps — all green",
     "state: 108 unit tests / 317 e2e tests / 35 smoke steps — all green"),
])
t = open("zero-balance_SKILL.md", encoding="utf-8").read()
row_anchor = "|** 108/316/35 green |"
if V149_ROW.strip() in t:
    print("ALREADY APPLIED: SKILL.md Session 149 row")
    ok = False
elif row_anchor not in t:
    print("MISS: SKILL.md Session 148 row tail anchor")
    ok = False
else:
    t = t.replace(row_anchor, row_anchor + "\n" + V149_ROW.strip(), 1)
    open("zero-balance_SKILL.md", "w", encoding="utf-8").write(t)
    print("aligned zero-balance_SKILL.md (the Session 149 row)")

# ---------------- D5: PAD ----------------
V1171_BLOCK = """#### Revision Block — v1.1.71 (Tracked Changes)
- `[UI]` v1.1.71 (2026-10-24) — the v114 parity iteration (PIN-ONLY for src/ — no production-code change; no dependency change): the counts 108 unit / **317 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v108-era MOBILE TWINS pair's EIGHTH re-run [v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114] — BOTH mobile 390x844 full-page twins: the /NETWORTH view [the v63-era pair's surface] and the DASHBOARD [the v62-era mobile twin's surface], last re-shot v108; the THIRTY-SEVENTH consecutive queue/ledger agreement) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's fifth cycle: 0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 108th standing checks (ALL GREEN — the mobile menu working the 108th consecutive time; the reference's four bugs all live; the data census clean on the FIRST reads) + the dashboard header-row census pin at 390 (PIN-ONLY; +1 e2e = 317)**: the verdicts BOTH PAIRS DIFFERENT — the pair's documented verdict class — with every flag DOM-arbitrated to a documented class (the stat-tile stacking the v41 mobile-superset class; the summary-card height its width consequence; the trend-circle the VLM MISREAD class; the NEW tab-bar alignment flag the v41 width-consequence class with the centering DISPROVEN live [jc/ai center byte-identical both sides]; the 'Edit with Base44' overlay — flagged on BOTH pairs — the platform-chrome class DISPROVEN live [fabCount 0 + bodyHasBase44 false both sides both surfaces]; the subtitle wrap the v62 width-delta class; the progress bar the pct DATA class; the data figures the seed-data classes); the two-half census (NW_CENSUS 42 + DASH_CENSUS 87 lines, md5 82cf8a43/85e4ec7e — the version-free v102/v108 blocks carried over VERBATIM) reproduces the v108 values exactly — NO NEW CLONE GAP; the +1 pin (tests/e2e/dashboard.spec.ts) the DASHBOARD mobile twin's HEADER-ROW interior family at 390 — the row {flex/column/flex-start/space-between/gap 16px/mb 32px/h 144} + the block {h 92/bottom 169} + the junction {gap 16} + the Add Item button's box chrome {36x127/pad 8px 16px/radius 6px/14px/500/white/gradient/icon 16x16} — never pinned at ANY viewport in ANY spec, measured byte-identical both sides via the one-shot drow-arbit-v114.sh, mutation-verified single-axis and cascade-free (items-start -> items-center at dashboard-view.tsx:927 line-scoped — only the v114 pin red at row.align alone after the standalone REBUILD); restored, rebuilt, post-restore 47/47 green; the ship chain 317 e2e zero flakes (84+77+75+84 = 320 executions across four chunks), 35/35 smoke, the screenshots 16/16 byte-identical (the same-day-seed law), the dev evidence 4/4 byte-identical + re-captured + VLM-verified; the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end.

"""
t = open("Project_Architecture_Document.md", encoding="utf-8").read()
pad_anchor = "#### Revision Block — v1.1.70 (Tracked Changes)"
if "#### Revision Block — v1.1.71" in t:
    print("ALREADY APPLIED: PAD v1.1.71 block")
    ok = False
elif pad_anchor not in t:
    print("MISS: PAD v1.1.70 anchor")
    ok = False
else:
    t = t.replace(pad_anchor, V1171_BLOCK + pad_anchor, 1)
    open("Project_Architecture_Document.md", "w", encoding="utf-8").write(t)
    print("aligned Project_Architecture_Document.md (the v1.1.71 block)")

sys.exit(0 if ok else 1)
