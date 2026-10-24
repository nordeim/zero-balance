#!/usr/bin/env python3
"""D1-D3 docs alignment for the v110 cycle (Session 145).

D1 AGENTS.md  — append the v110 paragraph at the file end.
D2 CLAUDE.md  — E2E count 312 -> 313 + the v110 pin clause after the v109 clause.
D3 README.md  — the two count spots + the v110 plan-table row after the v109 row.
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


V110_AGENTS = (
    "\nReference surfaces pinned by the v110 iteration (`docs/remediation-plan-v110.md`) — "
    "**the re-run cycle's next-oldest candidate (the v104-era SAVINGS pair's EIGHTH re-run "
    "[v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98 -> v104 -> v110] — the SAVINGS view at "
    "desktop 1280x800 FULL-PAGE, the v58-era savings pair's surface, last re-shot v104; the "
    "THIRTY-THIRD consecutive queue/ledger agreement, the surface names verified against "
    "vlm-shots-v104.sh's own header before the derivation) + THE SECURITY BUMP (the cycle's "
    "FIX item — the first production-dependency change since the v68 axe-core bump: npm "
    "audit added to the F0b audit for the first time surfaced next 16.4.0 CRITICAL [three "
    "advisories published 2026-10-22: the Image-Optimization SVG RCE, the Server-Actions "
    "DoS, the use-cache RCE — ALL THREE PATHS UNEXPOSED in this codebase: no next/image, "
    "no 'use cache', no Server Actions] + zod 4.6.5 HIGH [the oversized-collection memory "
    "exhaustion — the one real, bounded exposure: zod validates the PUBLIC register/login "
    "inputs, rate-limited 10/IP/15min]; the fix `npm audit fix` -> next 16.4.3 + zod 4.6.7, "
    "BOTH within the existing caret ranges so package.json is UNTOUCHED and only the "
    "lockfile's 43 version pins moved [the 9 @next/swc platform binaries + @next/env in "
    "lockstep]; npm audit: found 0 vulnerabilities; the re-verification: quick gates green "
    "on the bumped tree + the 104th standing checks ran against the BUMPED standalone "
    "build + the full 313-e2e ship chain + the screenshots byte-compare [10/16 "
    "byte-identical — the bump produced ZERO visual drift; the six deltas all the "
    "documented fresh-seed date-roll + scrim classes]) + the axe watch (NO DRIFT — 4.14.0 "
    "holds, only rc/next sha prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe "
    "verified) + the 104th standing checks (ALL GREEN — the mobile menu VERIFIED WORKING "
    "the 104th consecutive time; the reference's four bugs all live [the 464px /networth "
    "overflow measured docSW 464 directly]; the data census clean on the FIRST read; the "
    "SEO pair live both sides) + the rail nav-block interior census pin at 1280 (PIN-ONLY "
    "for src/ — no production-code change)**. The verdict SAVINGS DIFFERENT (the pair's "
    "documented flag-set class — v104/v98 read DIFFERENT) with every flag DOM-arbitrated: "
    "the card-footer payment chips the v57 DATA-CONDITIONAL class (the census: ref footer "
    "childCount 1 [date-only] vs clone 2 with the 'Brokerage' chip — the reference RENDERS "
    "payment chips when data carries them; its savings item simply ships none); the card "
    "grid 1-vs-2 the seed-count class; the header stats + card contents the seed-data "
    "classes; the avatar the user-identity class; NO FAB flag raised (the disproof not "
    "required — the standing disproof form stays documented from v97/v103/v108/v109). The "
    "two-half census (SV_CENSUS_JS 153 lines, md5 891ab9b6 — the v98/v104 census block "
    "verbatim, the builder-form md5 verified against the EXISTING v104 halves) reproduces "
    "the v104 values EXACTLY on every axis (the brand h1; the grid + card + titleRow + "
    "amount + footer + badge families; the card h 200-vs-230 the v57/v70b Recurring-wrap "
    "class [the badgeRow h 22 vs 52]; the docSW 1280 guards) — NO NEW CLONE GAP. The +1 "
    "e2e pin (tests/e2e/nav-geometry.spec.ts): the rail's NAV-BLOCK INTERIOR family at "
    "1280 on /savings — the block BETWEEN the v104-pinned brand-block and the "
    "v103-pinned user-footer, never pinned at ANY viewport in ANY spec (the session-5 "
    "pins hold the link BOX on links[0] only; the v8 G2a pin the inactive color; the v36 "
    "S3 bands the y positions; the glyph-parity spec the icons' PATH data only): the "
    "'Navigation' section label {h 32, fs 12px, fw 600, uppercase, letterSpacing 0.6px, "
    "rgb(45, 90, 74), pad 8px 12px, radius 6px, flex/center} + the UL {flex/column/gap "
    "4px/w 215/childCount 5} + the LI {relative/mb 0/h 36} + the link box {h 32/pad 10px "
    "12px/columnGap 12px/fs 14px/fw 400/radius 8px} + the nav ICON {w 16, h 16} + the "
    "label SPAN's truncate family {14px/hidden/ellipsis/nowrap} + the ACTIVE link {the "
    "135deg forest-medium-to-lime gradient, white, fw 500, h 32} + the counts {5 links, "
    "5 icons} + the docSW 1280 guard — measured byte-identical both sides via the one-shot "
    "nav-arbit-v110.sh; the reference-side finder STRUCTURAL (the reference renders NO nav "
    "landmark — its documented no-landmark bug — so the ul is found by its 5-anchor shape "
    "and the label by the wrapper-sibling walk); the mutation h-4 w-4 -> h-4 w-5 at "
    "sidebar.tsx:96 line-scoped (the ONLY h-4 w-4 line in the file; the burger toggle's "
    "icon uses the [&_svg]:size-4 arbitrary-variant form — untouched) fails ONLY the v110 "
    "pin at the icon.w axis ALONE ('w': 16 -> 20) after the standalone REBUILD — "
    "cascade-free BY CONSTRUCTION (zero specs assert the nav icons' computed w/h; the "
    "v36 S3 y-bands + the session-5 box + the v8 G2a color + the v103/v104 rail pins all "
    "stay green under the mutation); restored (git diff src/ = 0), rebuilt, post-restore "
    "11/11 green. The ship chain: 313 e2e zero flakes (81+81+78+76 = 316 chunk executions "
    "across the auditable FOUR-chunk split — the per-file counts derived authoritatively "
    "via playwright --list BEFORE any chunk ran); 35/35 smoke; the screenshots 10/16 "
    "BYTE-IDENTICAL + SIX fresh-seed deltas ALL ARBITRATED (the four item-view card "
    "date-footers + the details sheet's own Date FactRow: the +1-day roll, VLM-read "
    "glyph-confirmed ['Oct 18' -> 'Oct 19', 'Oct 13' -> 'Oct 14', 'October 14, 2026' -> "
    "'October 15, 2026']; the 08-calculator + the 16-item-details y817-900 bands: the "
    "v105-documented backdrop-blur scrim rounding drift [maxDelta 1-2, zero glyphs — the "
    "GPU blur compositing's capture-session variance]; ZERO structural bands; the "
    "updated set committed); the dev-server evidence set re-captured + VLM-verified (the "
    "menu proof: /income, docSW 390, navLandmark true). THE PHANTOM-GLITCH DISPEL (the "
    "cycle's tooling lesson): the v107-era 'save glitch' never existed — od-hexdump "
    "verifies ALL committed dev scripts (v107/v108/v109) carry the byte-correct "
    "a[href*='income']:visible locator on disk; the perceived '[h' loss is a DISPLAY-"
    "layer artifact (the tool-output pipeline eats the [h sequence — escape-sequence "
    "filtering), never a file defect; any output showing a bracket-h sequence must be "
    "od-verified, never trusted from grep/console display.\n"
)

# ---------------- D1: AGENTS.md ----------------
t = open("AGENTS.md", encoding="utf-8").read()
open("AGENTS.md", "w", encoding="utf-8").write(t + V110_AGENTS)
print("aligned AGENTS.md (v110 paragraph appended)")

# ---------------- D2: CLAUDE.md ----------------
edit(
    "CLAUDE.md",
    [
        ("**E2E (Playwright, 312)**", "**E2E (Playwright, 313)**"),
    ],
)
edit(
    "CLAUDE.md",
    [
        (
            "would cascade the v65 savings + v52 mobile pins])\n- **Smoke (bash, 35 steps)**",
            "would cascade the v65 savings + v52 mobile pins]), and the v110 pin: the rail's "
            "nav-block interior census at 1280 on /savings (nav-geometry.spec.ts — the "
            "'Navigation' label {32px/12px/600/uppercase/0.6px letter-spacing/rgb(45,90,74)/"
            "8px 12px pad/6px radius} + the UL {flex column/gap 4px/5 links} + the LI "
            "{relative/36px} + the nav ICON {16×16 — never pinned at ANY viewport; the "
            "glyph-parity spec holds the icons' path data only} + the label SPAN's truncate "
            "family + the desktop ACTIVE link's computed chrome {the 135deg gradient/white/"
            "500 — the v10 pin holds the mobile sheet variant only} — the block between the "
            "v104 brand-block pin and the v103 user-footer pin, measured byte-identical both "
            "sides via the one-shot nav-arbit-v110.sh; the mutation h-4 w-4 → h-4 w-5 at "
            "sidebar.tsx:96 line-scoped — only the v110 pin red at the icon.w axis alone "
            "[16 → 20], single-axis AND cascade-free BY CONSTRUCTION [zero specs assert the "
            "nav icons' computed w/h; the v36 S3 y-bands stay green]); the v110 security bump "
            "(the first production-dependency change since v68: npm audit fix → next 16.4.3 "
            "+ zod 4.6.7 — the 2026-10-22 next CRITICAL advisories [all three paths unexposed: "
            "no next/image, no use cache, no Server Actions] + the zod HIGH [the public-input "
            "memory-exhaustion, rate-limit-bounded] cleared within the existing caret ranges — "
            "package.json untouched, 43 lockfile pins moved, npm audit 0 vulnerabilities, the "
            "full 313 chain + the 104th standing checks + the 10/16 byte-identical screenshots "
            "re-verifying the bumped tree)\n- **Smoke (bash, 35 steps)**",
        ),
    ],
)

# ---------------- D3: README.md ----------------
edit(
    "README.md",
    [
        (
            "📂 e2e/                    # Playwright specs (312 tests) + global setup",
            "📂 e2e/                    # Playwright specs (313 tests) + global setup",
        ),
        (
            "npm run test:e2e    # Playwright e2e (312 tests) — needs `npm run build` first",
            "npm run test:e2e    # Playwright e2e (313 tests) — needs `npm run build` first",
        ),
    ],
)

V110_README_ROW = (
    "| [`docs/remediation-plan-v110.md`](docs/remediation-plan-v110.md) | **The re-run cycle's next-oldest "
    "candidate (the v104-era SAVINGS pair's EIGHTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → "
    "v104 → v110] — the SAVINGS view at desktop 1280×800 FULL-PAGE, the v58-era savings pair's "
    "surface, last re-shot v104 — now the oldest remaining [v104 < v105 < v106 < v107 < v108 < "
    "v109]; the THIRTY-THIRD consecutive queue/ledger agreement) + THE SECURITY BUMP (the cycle's "
    "FIX item: `npm audit` added to the F0b audit surfaced next 16.4.0 CRITICAL [three 2026-10-22 "
    "advisories — all three paths UNEXPOSED in this codebase] + zod 4.6.5 HIGH [the public-input "
    "memory exhaustion]; `npm audit fix` → next 16.4.3 + zod 4.6.7 within the existing caret "
    "ranges — package.json untouched, 43 lockfile pins moved, 0 vulnerabilities, the full chain "
    "re-verified on the bumped tree) + the axe watch (NO DRIFT) + the 104th standing checks + "
    "the rail nav-block interior census pin (PIN-ONLY)**. The verdict SAVINGS DIFFERENT (the "
    "pair's documented flag-set class) with every flag DOM-arbitrated — the payment-chip footer "
    "the v57 DATA-CONDITIONAL class (ref childCount 1 date-only vs clone 2 with the 'Brokerage' "
    "chip), the grid 1-vs-2 the seed-count class, the header stats + card contents the seed-data "
    "classes, the avatar the user-identity class, NO FAB flag (no disproof required); the "
    "two-half census (SV_CENSUS_JS 153 lines, md5 891ab9b6 — the v98/v104 census block verbatim) "
    "reproduces the v104 values exactly on every axis (the card h 200-vs-230 the v57/v70b "
    "Recurring-wrap class [badgeRow 22 vs 52]) — NO NEW CLONE GAP; the +1 e2e pins the "
    "never-pinned rail NAV-BLOCK INTERIOR at 1280 on /savings (the 'Navigation' label {32px/"
    "12px/600/uppercase/0.6px/rgb(45,90,74)} + the UL {flex column/gap 4/5 links} + the LI "
    "{relative/36} + the link box controls + the nav ICON {16×16} + the span truncate family + "
    "the ACTIVE link {the 135deg gradient/white/500} — the block between the v104 brand-block "
    "pin and the v103 user-footer pin; 313 e2e total), measured byte-identical both sides via "
    "the one-shot nav-arbit-v110.sh (the reference-side finder STRUCTURAL — its documented "
    "no-landmark bug means no nav element), mutation-verified single-axis AND cascade-free "
    "(h-4 w-4 → h-4 w-5 at sidebar.tsx:96 line-scoped — the ONLY h-4 w-4 in the file; zero "
    "specs assert the nav icons' computed w/h). The ship: 313 e2e zero flakes across the "
    "auditable four-chunk split (81+81+78+76 = 316 executions = 313 unique); the screenshots "
    "10/16 byte-identical + SIX fresh-seed deltas ALL arbitrated (the +1-day date rolls on the "
    "four item views + the details sheet's Date FactRow — VLM glyph-read; the 08/16 y817-900 "
    "bands the v105-documented backdrop-blur scrim rounding drift [maxDelta 1-2, zero "
    "glyphs] — zero structural bands, the updated set committed); the dev evidence "
    "re-captured + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); the "
    "PHANTOM-GLITCH DISPEL (the v107-era 'save glitch' never existed — od-verified: all "
    "committed dev scripts byte-correct on disk; the '[h' loss a display-layer artifact). |\n"
)
t = open("README.md", encoding="utf-8").read()
anchor = "the vitest.config.ts stale sibling-seams comment cleaned (the LOW item flagged since v106 — comment-only). |\n"
i = t.find(anchor)
assert i >= 0, "README v109 row anchor not found"
assert t.find(anchor, i + 1) == -1, "README v109 row anchor not unique"
t = t[: i + len(anchor)] + V110_README_ROW + t[i + len(anchor) :]
open("README.md", "w", encoding="utf-8").write(t)
print("aligned README.md (v110 row inserted)")

print("D1-D3 aligned")
