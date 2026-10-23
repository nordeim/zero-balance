#!/usr/bin/env python3
"""D1-D7 docs alignment for the v108 cycle (Session 143).

D1 AGENTS.md  — append the v108 paragraph at the file end.
D2 CLAUDE.md  — E2E count 310 -> 311 + the v108 pin clause after the v107 clause.
D3 README.md  — the two count spots + the v108 plan-table row after the v107 row.
D4 zero-balance_SKILL.md — the project_state line + the Session 143 review row
               above Session 142's.
D5 PAD        — the v1.1.65 revision block above v1.1.64's.
D6 probe README — the v108 section (lineage + lessons) + the v109 queue
               replacing the v108 queue.
Every edit is assert-applied; a miss fails the run.
"""
import sys


def edit(path, pairs, must=True):
    t = open(path, encoding="utf-8").read()
    for old, new in pairs:
        if old not in t:
            print(f"MISS in {path}: {old[:70]!r}")
            if must:
                sys.exit(1)
        t = t.replace(old, new, 1)
    open(path, "w", encoding="utf-8").write(t)
    print(f"aligned {path} ({len(pairs)} edits)")


V108_AGENTS = (
    "\nReference surfaces pinned by the v108 iteration (`docs/remediation-plan-v108.md`) — "
    "**the re-run cycle's next-oldest candidate (the v102-era MOBILE TWINS pair's SEVENTH re-run "
    "[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108] — BOTH mobile 390x844 full-page "
    "twins: (1) the /NETWORTH view (the v63-era pair's surface) and (2) the DASHBOARD (the "
    "v62-era mobile twin's surface), last re-shot v102; the THIRTY-FIRST consecutive "
    "queue/ledger agreement, the surface names verified against vlm-shots-v102.sh's own header "
    "before the derivation) + the axe watch (NO DRIFT — 4.14.0 holds, only rc/next sha "
    "prereleases beyond [4.14.1-d1531a9.0.sha-d1531a9 + 4.14.1-55245d5.0.sha-55245d5], no "
    "stable 4.14.1, no 5.x; the v68 dedupe re-verified after the npm ci reinstall) + the 102nd "
    "standing checks (ALL GREEN — the mobile menu VERIFIED WORKING the 102nd consecutive time; "
    "the reference's four bugs all live [the 464px /networth overflow measured docSW 464 "
    "directly]; the data census clean on the FIRST read; the SEO pair live both sides) + the "
    "mobile topbar interior junction census pin at 390 (PIN-ONLY for src/ — no "
    "production-code change; +1 e2e = 311)**. The verdicts BOTH DIFFERENT — the pair's "
    "documented verdict class (the same flag-set classes as the v84/v90/v96/v102 re-runs) — "
    "with every flag DOM-arbitrated: the stat-tile side-by-side-vs-stacked the v41 "
    "mobile-superset class (the statGrid cols ref 2-col vs clone 1-col, the gap 16px "
    "IDENTICAL, the tiles' h 84 byte-identical — the documented superset fix for the "
    "reference's own 464px overflow); the summary-card height the same class's width "
    "consequence (ref 432x333 vs clone 358x421); the trend-circle claim the VLM MISREAD class "
    "(the medallion 64x64 + the trendIcon 32x32 byte-identical both sides); the 'Edit with "
    "Base44' overlay the platform-chrome class DISPROVEN live (the one-shot both-sides census "
    "base44-fab-arbit-v108.sh: fabCount 0 + bodyHasBase44 false on BOTH sides — the FAB lives "
    "in the reference's platform iframe chrome, outside the app DOM; the v97/v103 standing "
    "disproof form re-confirmed); the 'hamburger menu icon missing in Image 2' flag (the first "
    "VLM run only) the VLM MISREAD class DISPROVEN live BYTE-IDENTICAL (BOTH sides render the "
    "toggle at rect {x 24, y 16, 28x28}, accessibleName 'Toggle Sidebar', svgClass 'lucide "
    "lucide-panel-left', the 16x16 glyph, pathD 'M9 3v18', stroke rgb(10,10,10) — there is NO "
    "3-line hamburger on EITHER side; remediation-plan-v3/v7 document the reference's own "
    "toggle as the 28x28 panel-left button — the glyph-recognition misread, its "
    "non-determinism the second form of the class); the subtitle wrap-point the v62 "
    "width-delta class (the chrome byte-identical [fs 16px/fw 400/rgb(107,114,128)/lh 24px, "
    "blockH 92, exactly 2 DOM lines both sides] — the reference's own 395px overflow shifts "
    "its wrap); the data figures the seed-data classes. The two-half census (NW_CENSUS 42 + "
    "DASH_CENSUS 87 lines, md5 82cf8a43/85e4ec7e — the v102 census blocks verbatim) reproduces "
    "the v102 values EXACTLY on every axis (the NETWORTH summary card + statGrid + tiles + "
    "medallion + trendIcon; the DASHBOARD subtitle + breakdownCard [h 324, svgCount 7, the "
    "16/14 alternation] + the spendingCard finder's SAME fallback string both sides; the docSW "
    "guards ref 464/395 vs clone 390/390 — the superset invariant) — NO NEW CLONE GAP. The "
    "+1 e2e pin (tests/e2e/mobile-layout.spec.ts): the MOBILE TOPBAR's interior junction "
    "family at 390 — never pinned at ANY viewport in ANY spec (the v7 G5 pin holds the "
    "burger's box + icon color; the session-5 pins the topbar's box GEOMETRY + the hamburger "
    "radius/icon CLASS + the brand CLASS — the header's own chrome [pad 24/16, border-b 1px "
    "rgb(229,231,227), bg white, h 61], the row's flex chrome [flex/center/gap 16px/h 28], "
    "the burger's POSITION [the px-6/py-4 rhythm], and the brand's COMPUTED chrome [fs "
    "20px/fw 700/lh 28px/rgb(26,58,46)] never asserted): measured byte-identical both sides "
    "via the one-shot topbar-arbit-v108.sh; the mutation gap-4 -> gap-5 at sidebar.tsx:224 "
    "line-scoped (the ONLY flex items-center gap-4 line in the file) fails ONLY the v108 pin "
    "at the row's gap axis alone ('16px' -> '20px') after the standalone REBUILD; restored "
    "(git diff src/ = 0), rebuilt, post-restore 6/6 green. THE FRESH-CLONE PROVISIONING "
    "LESSON: the first npm install produced an INCOMPLETE zod extraction (59/840 files, the "
    "v4/ subdirectory absent) which crashed both fast gates at startup — the registry tarball "
    "verified intact, the defect LOCAL; the disciplined fix npm ci (the clean lockfile-exact "
    "reinstall, integrity re-verified, both gates green on the first re-run). The ship chain: "
    "311 e2e zero flakes (77+78+78+81 = 314 chunk executions across the auditable FOUR-chunk "
    "split — the per-file counts derived authoritatively via playwright --list BEFORE any "
    "chunk ran); 35/35 smoke; the screenshots 16/16 BYTE-IDENTICAL (the same-day-seed law — "
    "zero arbitration needed); the dev-server evidence set re-captured + VLM-verified (the "
    "menu proof: /income, docSW 390, navLandmark true — the menu flow proven through the "
    "captures); the v107 dev-script's income-link selector save glitch (`aref*=` — the `[h` "
    "lost) noted LOW and corrected in the v108 script.\n"
)

# ---------------- D1: AGENTS.md ----------------
t = open("AGENTS.md", encoding="utf-8").read()
open("AGENTS.md", "w", encoding="utf-8").write(t + V108_AGENTS)
print("aligned AGENTS.md (v108 paragraph appended)")

# ---------------- D2: CLAUDE.md ----------------
edit(
    "CLAUDE.md",
    [
        ("**E2E (Playwright, 310)**", "**E2E (Playwright, 311)**"),
    ],
)
edit(
    "CLAUDE.md",
    [
        (
            'single-axis BY CONSTRUCTION)\n- **Smoke (bash, 35 steps)**',
            'single-axis BY CONSTRUCTION), and the v108 pin: the mobile topbar interior junction '
            "census at 390 (mobile-layout.spec.ts — the header {h 61, padX 24px, padY 16px, "
            "border-b 1px rgb(229,231,227), bg white} + the row {flex/center/gap 16px/h 28/"
            "childCount 2} + the burger {x 24, y 16, 28×28, radius 8px — the px-6/py-4 junction "
            "arithmetic} + the icon {16×16, rgb(10,10,10)} + the brand {ZeroBalance, fs 20px, "
            "fw 700, lh 28px, rgb(26,58,46)} — the never-pinned family [the v7 G5 pin holds "
            "the burger's box + icon color; the session-5 pins the topbar's box GEOMETRY + the "
            "hamburger radius/icon CLASS + the brand CLASS — the header's own chrome, the "
            "row's flex/gap, the burger's position, and the brand's computed chrome never "
            "asserted at ANY viewport], measured byte-identical both sides via the one-shot "
            "topbar-arbit-v108.sh; the header's w + the brand's x-position stay "
            "census-documented but UNPINNED — the v107 xInRow lesson; the mutation gap-4 → "
            "gap-5 at sidebar.tsx:224 line-scoped — only the v108 pin red at the row's gap "
            'axis alone ["16px" → "20px"], single-axis BY CONSTRUCTION)\n- **Smoke (bash, 35 steps)**',
        ),
    ],
)

# ---------------- D3: README.md ----------------
edit(
    "README.md",
    [
        (
            "📂 e2e/                    # Playwright specs (310 tests) + global setup",
            "📂 e2e/                    # Playwright specs (311 tests) + global setup",
        ),
        (
            "npm run test:e2e    # Playwright e2e (310 tests) — needs `npm run build` first",
            "npm run test:e2e    # Playwright e2e (311 tests) — needs `npm run build` first",
        ),
    ],
)

V108_README_ROW = (
    "| [`docs/remediation-plan-v108.md`](docs/remediation-plan-v108.md) | **The re-run cycle's next-oldest "
    "candidate (the v102-era MOBILE TWINS pair's SEVENTH re-run [v62/v63 → v69 → v78 → v84 → "
    "v90 → v96 → v102 → v108] — BOTH mobile 390x844 full-page twins: (1) the /NETWORTH view "
    "(the v63-era pair's surface) and (2) the DASHBOARD (the v62-era mobile twin's surface), "
    "last re-shot v102 — now the oldest remaining [v102 < v103 < v104 < v105 < v106 < v107]; "
    "the THIRTY-FIRST consecutive queue/ledger agreement — the surface names verified against "
    "vlm-shots-v102.sh's own header before the derivation) + the axe watch (NO DRIFT) + the "
    "102nd standing checks + the mobile topbar interior junction census pin (PIN-ONLY)**. The "
    "baseline on the FRESH-CLONE workspace (the sandbox reset: re-provisioned from scratch — "
    "the npm ci provisioning lesson: the first install's INCOMPLETE zod extraction [59/840 "
    "files] crashed both fast gates, the registry tarball verified intact, npm ci restored "
    "840/840 and both gates green; the one post-push commit audited session-log/skills-only "
    "— zero src/ or lockfile deltas); the verdicts BOTH DIFFERENT (the pair's documented "
    "class) with every flag DOM-arbitrated — the stat-tile stacking the v41 mobile-superset "
    "class, the summary height its width consequence, the trend circle the VLM misread "
    "(medallion 64×64 byte-identical), the 'Edit with Base44' overlay the platform-chrome "
    "class DISPROVEN live (fabCount 0 + bodyHasBase44 false both sides), the 'hamburger "
    "missing' flag the VLM MISREAD class DISPROVEN live byte-identical (both sides the "
    "panel-left toggle {24,16,28×28} — 'Toggle Sidebar', lucide-panel-left 16×16, pathD 'M9 "
    "3v18', rgb(10,10,10); the v3/v7-documented glyph — no 3-line hamburger exists on either "
    "side), the subtitle wrap the v62 width-delta class, the data figures the seed classes; "
    "the two-half census (NW_CENSUS 42 + DASH_CENSUS 87 lines, md5 82cf8a43/85e4ec7e — the "
    "v102 census blocks verbatim) reproduces the v102 values exactly (the summary card "
    "432×333/358×421 + statGrid 2-col/1-col [gap 16 identical, tiles h 84] + medallion 64×64 "
    "+ trendIcon 32×32 + docSW 464/390; the subtitle chrome + exactly 2 DOM lines + "
    "breakdownCard h 324/svgCount 7 + the spendingCard finder's same fallback both sides + "
    "docSW 395/390) — NO NEW CLONE GAP; the +1 e2e pins the never-census'd MOBILE TOPBAR "
    "interior family at 390 (the header {h 61, pad 24/16, border-b 1px rgb(229,231,227), bg "
    "white} + the row {flex/center/gap 16/h 28/childCount 2} + the burger {24/16/28×28/8px} "
    "+ the icon {16×16/rgb(10,10,10)} + the brand {ZeroBalance, 20px/700/28px/rgb(26,58,46)} "
    "— the v7 G5 pin holds the burger box+icon only; 311 e2e total), measured byte-identical "
    "both sides via the one-shot topbar-arbit-v108.sh, mutation-verified single-axis (gap-4 → "
    "gap-5 at sidebar.tsx:224, line-scoped — the row's gap axis alone) after the rebuild "
    "discipline. The ship: 311 e2e zero flakes across the auditable four-chunk split "
    "(77+78+78+81 = 314 executions = 311 unique); the screenshots 16/16 BYTE-IDENTICAL (the "
    "same-day regeneration — zero arbitration needed); the dev evidence re-captured + "
    "VLM-verified (the menu proof: /income, docSW 390, navLandmark true). |\n"
)
t = open("README.md", encoding="utf-8").read()
anchor = "(123+89+61+40 = 313 executions = 310 unique); the screenshots 16/16 BYTE-IDENTICAL (the same-day regeneration — zero arbitration needed). |\n"
i = t.find(anchor)
assert i >= 0, "README v107 row anchor not found"
assert t.find(anchor, i + 1) == -1, "README v107 row anchor not unique"
t = t[: i + len(anchor)] + V108_README_ROW + t[i + len(anchor) :]
open("README.md", "w", encoding="utf-8").write(t)
print("aligned README.md (v108 row inserted)")

# ---------------- D4: zero-balance_SKILL.md ----------------
edit(
    "zero-balance_SKILL.md",
    [
        (
            "project_state: 108 unit tests / 310 e2e tests / 35 smoke steps — all green",
            "project_state: 108 unit tests / 311 e2e tests / 35 smoke steps — all green",
        ),
    ],
)
V108_SKILL_ROW = (
    "| 2026-10-24 | Session 143 — parity iteration v108 (`docs/remediation-plan-v108.md`) | **The re-run "
    "cycle's next-oldest candidate (the v102-era MOBILE TWINS pair's SEVENTH re-run [v62/v63 → v69 → "
    "v78 → v84 → v90 → v96 → v102 → v108] — BOTH mobile 390x844 full-page twins: (1) the /NETWORTH "
    "view (the v63-era pair's surface) and (2) the DASHBOARD (the v62-era mobile twin's surface), "
    "last re-shot v102, now the oldest remaining [v102 < v103 < v104 < v105 < v106 < v107]; the "
    "THIRTY-FIRST consecutive queue/ledger agreement — the surface names verified against "
    "vlm-shots-v102.sh's own header before the derivation) + the axe watch (NO DRIFT — 4.14.0 "
    "holds) + the 102nd standing checks (ALL GREEN — the mobile menu working the 102nd "
    "consecutive time; the census clean on the first read; the reference's four bugs all live) + "
    "the mobile topbar interior junction census pin at 390 (PIN-ONLY; +1 e2e = 311)**: the "
    "verdicts BOTH DIFFERENT (the pair's documented class) with every flag DOM-arbitrated (the "
    "stat-tile stacking the v41 mobile-superset class; the summary height its width consequence; "
    "the trend circle the VLM misread — the medallion 64×64 byte-identical; the 'Edit with "
    "Base44' overlay the platform-chrome class DISPROVEN live [fabCount 0 + bodyHasBase44 false "
    "both sides]; the 'hamburger missing' flag the VLM MISREAD class DISPROVEN live "
    "byte-identical — BOTH sides the panel-left toggle {24,16,28×28}, 'Toggle Sidebar', "
    "lucide-panel-left 16×16, pathD 'M9 3v18', rgb(10,10,10), the v3/v7-documented glyph, no "
    "3-line hamburger exists on either side; the subtitle wrap the v62 width-delta class; the "
    "data figures the seed classes); the two-half census (NW_CENSUS 42 + DASH_CENSUS 87 lines, "
    "md5 82cf8a43/85e4ec7e — the v102 census blocks verbatim) reproduces the v102 values exactly "
    "(the summary card 432×333/358×421, the statGrid 2-col/1-col with gap 16 identical + tiles "
    "h 84, the medallion 64×64 + trendIcon 32×32, docSW 464/390; the subtitle chrome + 2 DOM "
    "lines, the breakdownCard h 324 + svgCount 7 + the 16/14 alternation, the spendingCard "
    "finder's same fallback both sides, docSW 395/390) — NO NEW CLONE GAP; the +1 pin the "
    "MOBILE TOPBAR's interior junction family (the header {h 61, pad 24/16, border-b 1px "
    "rgb(229,231,227), bg white} + the row {flex/center/gap 16px/h 28/childCount 2} + the "
    "burger {x 24, y 16, 28×28, radius 8px} + the icon {16×16, rgb(10,10,10)} + the brand "
    "{ZeroBalance, 20px/700/28px/rgb(26,58,46)} — never pinned at ANY viewport [the v7 G5 pin "
    "holds the burger box + icon color; the session-5 pins the box geometry + classes only]; "
    "measured byte-identical both sides via the one-shot topbar-arbit-v108.sh [the header's w + "
    "the brand's x-position census-documented but unpinned — the v107 xInRow lesson]), "
    "mutation-verified single-axis (gap-4 → gap-5 at sidebar.tsx:224 line-scoped — the row's "
    "gap axis alone ['16px' → '20px'], the ONLY flex items-center gap-4 line in the file); the "
    "fresh-clone provisioning lesson (the first npm install's INCOMPLETE zod extraction "
    "[59/840 files] crashed both fast gates — the registry tarball intact, npm ci the "
    "disciplined fix); the ship 311 e2e zero flakes (77+78+78+81 = 314 chunk executions across "
    "the four-chunk split — the per-file counts derived authoritatively before any chunk ran); "
    "35/35 smoke; the screenshots 16/16 byte-identical (the same-day regeneration — zero "
    "arbitration needed); the dev evidence re-captured + VLM-verified (the menu proof: /income, "
    "docSW 390, navLandmark true) |** 108/311/35 green |\n"
)
t = open("zero-balance_SKILL.md", encoding="utf-8").read()
anchor = "| 2026-10-23 | Session 142 — parity iteration v107"
i = t.find(anchor)
assert i >= 0, "SKILL Session 142 row not found"
t = t[:i] + V108_SKILL_ROW + t[i:]
open("zero-balance_SKILL.md", "w", encoding="utf-8").write(t)
print("aligned zero-balance_SKILL.md (Session 143 row inserted)")

# ---------------- D5: PAD v1.1.65 block ----------------
V108_PAD = (
    "#### Revision Block — v1.1.65 (Tracked Changes)\n"
    "- `[UI]` v1.1.65 (2026-10-24) — the v108 parity iteration (PIN-ONLY — no production-code "
    "change): the counts 108 unit / **311 e2e** (+1) / 35 smoke; **the re-run cycle's "
    "next-oldest candidate (the v102-era MOBILE TWINS pair's SEVENTH re-run [v62/v63 -> v69 -> "
    "v78 -> v84 -> v90 -> v96 -> v102 -> v108] — BOTH mobile 390x844 full-page twins: (1) the "
    "/NETWORTH view (the v63-era pair's surface) and (2) the DASHBOARD (the v62-era mobile "
    "twin's surface), last re-shot v102; the THIRTY-FIRST consecutive queue/ledger agreement — "
    "the surface names verified against vlm-shots-v102.sh's own header before the derivation) "
    "+ the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe re-verified post-npm-ci) + the "
    "102nd standing checks (ALL GREEN — the mobile menu working the 102nd consecutive time; "
    "the reference's four bugs all live; the census clean on the first read) + the mobile "
    "topbar interior junction census pin at 390 (PIN-ONLY; +1 e2e = 311)**: the verdicts BOTH "
    "DIFFERENT (the pair's documented class) with every flag DOM-arbitrated to a documented "
    "class (the stat-tile stacking the v41 mobile-superset class; the summary height its width "
    "consequence; the trend circle the VLM misread; the 'Edit with Base44' overlay the "
    "platform-chrome class DISPROVEN live [fabCount 0 + bodyHasBase44 false on both sides]; "
    "the 'hamburger missing' flag the VLM MISREAD class DISPROVEN live byte-identical [both "
    "sides the panel-left toggle {24,16,28x28}, 'Toggle Sidebar', lucide-panel-left 16x16, "
    "pathD 'M9 3v18', rgb(10,10,10) — the v3/v7-documented glyph]; the subtitle wrap the v62 "
    "width-delta class; the data figures the seed-data classes); the two-half census "
    "(NW_CENSUS 42 + DASH_CENSUS 87 lines, md5 82cf8a43/85e4ec7e — the v102 census blocks "
    "verbatim) reproduces the v102 values exactly on every axis — NO NEW CLONE GAP; the +1 "
    "pin (tests/e2e/mobile-layout.spec.ts) the MOBILE TOPBAR's interior junction family — the "
    "header {h 61, padX 24px, padY 16px, border-b 1px rgb(229,231,227), bg white} + the row "
    "{flex/center/gap 16px/h 28/childCount 2} + the burger {x 24, y 16, 28x28, radius 8px} + "
    "the icon {16x16, rgb(10,10,10)} + the brand {ZeroBalance, fs 20px, fw 700, lh 28px, "
    "rgb(26,58,46)} — measured byte-identical both sides via the one-shot topbar-arbit-v108.sh "
    "(THE FRESH-CLONE PROVISIONING LESSON: the first npm install's INCOMPLETE zod extraction "
    "[59/840 files, the v4/ subdirectory absent] crashed both fast gates — the registry "
    "tarball verified intact, the defect LOCAL; npm ci the disciplined fix, 840/840 restored); "
    "the mutation gap-4 -> gap-5 at sidebar.tsx:224 line-scoped — only the v108 pin red at "
    "the row's gap axis alone after the rebuild; restored, rebuilt, post-restore green; the "
    "ship chain 311 e2e zero flakes (77+78+78+81 = 314 executions across four chunks), 35/35 "
    "smoke, the screenshots 16/16 byte-identical (the same-day regeneration).\n"
)
t = open("Project_Architecture_Document.md", encoding="utf-8").read()
anchor = "#### Revision Block — v1.1.64 (Tracked Changes)"
i = t.find(anchor)
assert i >= 0, "PAD v1.1.64 block not found"
t = t[:i] + V108_PAD + t[i:]
open("Project_Architecture_Document.md", "w", encoding="utf-8").write(t)
print("aligned Project_Architecture_Document.md (v1.1.65 block inserted)")

# ---------------- D6: probe README ----------------
V108_PROBE_SECTION = (
    "### The v108 cycle (Session 143) — the v102-lineage derivation\n\n"
    "- `derive-v108-series.py` (persisted) — the v108 series derived from the\n"
    "  v102 lineage: vlm-shots-v108.sh + clone-vlmshots-v108.sh +\n"
    "  vlm-compare-v108.mjs + arbit-v108.sh; the generic swaps + the EIGHT\n"
    "  exact-fragment history corrections (the queue source v101-plan ->\n"
    "  v107-plan, last-re-shot v96->v102, the oldest-remaining bracket\n"
    "  bumped as TWO single-line halves [the v102 compare header wraps it\n"
    "  across lines 4-5], SIXTH->SEVENTH, the bracket extension v96->v102\n"
    "  ->v108, the re-runs' verdict note v84/v90/v96->v84/v90/v96/v102, the\n"
    "  census-axes provenance v96->v102) — 8/8 on the FIRST run, zero\n"
    "  residuals, line-count-preserving on all four (60/47/68/219).\n"
    "- `build-twohalf-v108.py` — the two-half builder (NW_CENSUS 42 +\n"
    "  DASH_CENSUS 87 lines, md5 82cf8a43/85e4ec7e — the v102 census blocks\n"
    "  VERBATIM, the blocks themselves version-free): ref-arbit-v108.sh +\n"
    "  clone-arbit-v108.sh, the census JS byte-identical across the halves.\n"
    "- `derive-standing-v108.py` — the 102nd standing pair\n"
    "  (ref-standing-v102.sh + standing-checks-v102.sh) from the v101 pair,\n"
    "  the THREE token families (the ordinal token's suffix flip\n"
    "  101st->102nd), normalize-back verified version-bump-only.\n"
    "- `base44-fab-arbit-v108.sh` — the ONE-SHOT both-sides arbitration for\n"
    "  the cycle's TWO disproven claims: the FAB census (fabCount 0 +\n"
    "  bodyHasBase44 false on both sides — the v97/v103 standing disproof\n"
    "  form, run because a FAB flag WAS raised) EXTENDED with the burger\n"
    "  glyph census (rect + accessibleName + svgClass + pathD + stroke) —\n"
    "  BOTH sides byte-identical {24,16,28x28} panel-left 'Toggle Sidebar'.\n"
    "- `topbar-arbit-v108.sh` — the ONE-SHOT both-sides census of the\n"
    "  MOBILE TOPBAR's interior junction family (the v108 pin's own axes\n"
    "  measured byte-identical on both sides before the pin): the header\n"
    "  {h 61, pad 24/16, border-b 1px rgb(229,231,227), bg white} + the row\n"
    "  {flex/center/gap 16/h 28/childCount 2} + the burger {24/16/28x28/\n"
    "  8px} + the icon {16x16, rgb(10,10,10)} + the brand {ZeroBalance,\n"
    "  20px/700/28px/rgb(26,58,46)}.\n\n"
    "### D6 — the operational lessons this cycle (v108)\n\n"
    "- THE NPM-CI PROVISIONING RULE (a fresh-clone note): a startup\n"
    "  module-resolution crash on a LOCKFILE-PINNED package (eslint's\n"
    "  `Cannot find module '.../zod/v4/index.cjs'` — 59 of 840 files\n"
    "  installed, the v4/ subdirectory absent while zod 4.6.5's own exports\n"
    "  map references it) means the LOCAL extraction is corrupt, NOT the\n"
    "  lockfile: verify the installed file count against the registry\n"
    "  tarball (`npm pack zod@4.6.5` -> 840 files) and fix with `npm ci`\n"
    "  (the clean lockfile-exact reinstall, integrity re-verified on every\n"
    "  package) — never a version change.\n"
    "- THE GLYPH-MISREAD ARBITRATION (a VLM-flag note): a VLM presence/\n"
    "  absence claim about an ICON is arbitrated by the svg FINGERPRINT\n"
    "  (class + pathD + stroke + rect + accessibleName), not by re-asking\n"
    "  the VLM — the v108 'hamburger missing in Image 2' claim died on the\n"
    "  byte-identical panel-left fingerprints (the reference's OWN toggle\n"
    "  is the 28x28 panel-left button documented since v3/v7; no 3-line\n"
    "  hamburger exists on either side). The VLM's second run did not even\n"
    "  raise the flag — the non-determinism itself the second form of the\n"
    "  class.\n"
    "- THE WRAPPED-BRACKET CORRECTION FORM (a derive-script note): when a\n"
    "  probe header wraps the oldest-remaining bracket across lines (the\n"
    "  v102 compare's `[v96 < v97 <` + `v98 < v99 < v100 < v101]`), correct\n"
    "  it as TWO single-line fragments rather than one multi-line fragment\n"
    "  — each half gets its own per-file hit count, keeping the\n"
    "  single-line-safe discipline (the v107 lesson's applied form).\n\n"
    "The v109 queue (suggestions — verify against the rotation ledger before\n"
    "executing): (1) the re-run cadence rotates to the next-oldest candidate\n"
    "after the v102-era MOBILE TWINS pair (the v103-era ITEMS pair — the\n"
    "INCOME + EXPENSES view pair at desktop 1280x800 FULL-PAGE, the\n"
    "v57-era items pair's surfaces, last re-shot v103 — now the oldest\n"
    "remaining [v103 < v104 < v105 < v106 < v107 < v108]; the pair's\n"
    "EIGHTH re-run bracket [v57 -> v64 -> v70 -> v79 -> v85 -> v91 -> v97 ->\n"
    "v103 -> v109] to be verified against vlm-shots-v103.sh's own header\n"
    "before the derivation), (2) the axe-core watch at its next re-check\n"
    "point (only a 5.x wrapper changes the calculus), (3) the deferred\n"
    "reference-write censuses (unchanged — out of bounds under the v46\n"
    "read-only rule).\n"
)
t = open("scripts/parity-probes/README.md", encoding="utf-8").read()
i = t.find("The v108 queue (suggestions")
assert i >= 0, "v108 queue anchor not found"
t = t[:i] + V108_PROBE_SECTION
open("scripts/parity-probes/README.md", "w", encoding="utf-8").write(t)
print("aligned scripts/parity-probes/README.md (v108 section + v109 queue)")
print("D1-D6 aligned")

