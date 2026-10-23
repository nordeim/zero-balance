#!/usr/bin/env python3
"""D1-D7 docs alignment for the v106 cycle (Session 141).

D1 AGENTS.md  — append the v106 paragraph at the file end.
D2 CLAUDE.md  — E2E count 308 -> 309 + the v106 pin clause after the v105 clause.
D3 README.md  — the two count spots + the v106 plan-table row after the v105 row.
D4 zero-balance_SKILL.md — the project_state line + the Session 141 review row
               above Session 140's.
D5 PAD        — the v1.1.63 revision block above v1.1.62's.
D6 probe README — the v106 section (lineage + lessons) + the v107 queue
               replacing the v106 queue.
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


V106_AGENTS = (
    "\nReference surfaces pinned by the v106 iteration (`docs/remediation-plan-v106.md`) — "
    "**the re-run cycle's next-oldest candidate (the v100-era NETWORTH + DRILL-DOWN pair's SEVENTH re-run "
    "[v60 -> v67 -> v76 -> v82 -> v88 -> v94 -> v100 -> v106] — the NETWORTH view + the DASHBOARD's drill-down "
    "EXPANDED state at desktop 1280x800 full-page, last re-shot v100; the TWENTY-NINTH consecutive queue/ledger "
    "agreement, the surface names verified against vlm-shots-v100.sh's own header before the derivation — the "
    "queue-prose verification lesson applied: session_258.md's \"the v100-era DASHBOARD pair\" naming the pair by "
    "its drill-down surface, the probe lineage the authority) + the axe watch (NO DRIFT — 4.14.0 holds, only "
    "rc/next sha prereleases beyond, the v68 dedupe holds) + the 100th standing checks (ALL GREEN — the mobile "
    "menu VERIFIED WORKING the 100th consecutive time; the reference's four bugs all live [the 464px /networth "
    "overflow measured docSW 464 directly]; the data census the 100th clean drift check — clean on the FIRST read; "
    "the SEO pair live both sides) + the networth asset-card facts-row interior census pin at 1280 (PIN-ONLY for "
    "src/ — no production-code change; +1 e2e = 309)**. The verdicts: the NETWORTH pair IDENTICAL (zero "
    "layout/style flags — only the expected data classes + the platform-chrome FAB form); the DRILL-DOWN pair "
    "DIFFERENT (the pair's documented re-run class) with every flag DOM-arbitrated to a documented class: the "
    "nav-highlight the v56 SUPERSET class (the reference's root-route bug — it marks NOTHING active at `/`; the "
    "clone's Dashboard highlight superset fix #3), the avatar the user-identity class (the VLM's \"P\" a misread of "
    "the clone's \"D\"), the progress fill the pct DATA class (trackW 568 byte-identical, fillW 173-vs-357 each "
    "site's own percentage), the donut labels the v60 perception class (the census: count 4 + labelLineCount 0 + "
    "labelFs 16px + labelFill black + sectors 3 BYTE-IDENTICAL — the reference's own labels render OVERLAPPING "
    "under its seed and are illegible to the VLM), the \"Total Expense vs Total Expenses\" flag a NEW VLM "
    "text-misread sub-form DISPROVEN by the direct live DOM read (the reference's own `/` statTitles read \"Total "
    "Expenses\" — PLURAL, byte-identical to the clone's pinned family), the Freelance category + the footer count "
    "the seed-data class, the \"Edit with Base44\" tooltip the platform-chrome class. The two-half census (ARBIT_A "
    "90 + ARBIT_B 111 lines, md5 457438e8/0b895e19 — the v100 census blocks verbatim) reproduces the v100 values "
    "EXACTLY on every axis (the PART A drill-down family + the PART B summary-card family; the labelBlock WIDTH "
    "304-vs-357 the ONE documented delta — the v82 DATA-CONDITIONAL width class, the 48px figure's text length) — "
    "NO NEW CLONE GAP. The +1 e2e pin (tests/e2e/networth.spec.ts): the networth ASSET CARD's FACTS-ROW INTERIOR "
    "family — never pinned at ANY viewport in ANY spec (the v46 F2 pin holds the facts WRAPPER's font/color + the "
    "value->facts gap; the rows' own flex chrome, the 12x12 icon family, the row heights, and the space-y-2 rhythm "
    "were unpinned): the wrapper {display block, fs 12px, color rgb(107, 114, 128), h 40, rowCount 2} + both rows "
    "{flex, center, gap 8px, h 16} + the Updated row's mt 8px (the v3 space-y-2 margin-top semantics restored by "
    "globals.css — the trap-log family holding on a networth surface) + the icons {12x12, currentColor "
    "rgb(107, 114, 128), viewBox 0 0 24 24} — measured byte-identical on BOTH sides via the one-shot census "
    "nw-facts-arbit-v106.sh (the reference's own \"Savings Account\" card vs the clone's \"Share Portfolio\"; "
    "every axis DATA-INDEPENDENT). The pin GREEN on first run (34/34 in networth.spec.ts); the pin-sanity "
    "mutation (net-worth-view.tsx:118 h-3 w-3 -> h-3 w-3.5, LINE-NUMBER-SCOPED — the institution row's line 113 + "
    "the liability card's lines 218/224/229 untouched) fails ONLY the v106 pin (33 green) at the Updated row's "
    "iconW axis ALONE (\"12\" -> \"14\" — the single-dimension icon form, the row h staying 16: the 16px text line "
    "box wins over the 14px icon) after the standalone REBUILD; restored (git diff src/ = 0), rebuilt, "
    "post-restore 34/34 green. The ship chain: 309 e2e zero flakes (117+94+59+42 = 312 chunk executions across "
    "the auditable FOUR-chunk split — the per-file counts derived authoritatively via playwright --list BEFORE any "
    "chunk ran, the v103 lesson applied); 35/35 smoke; the screenshots 16/16 BYTE-IDENTICAL (the same-day-seed "
    "law — the v105-set regeneration's own seed day, zero arbitration needed this cycle).\n"
)

# ---------------- D1: AGENTS.md ----------------
t = open("AGENTS.md", encoding="utf-8").read()
open("AGENTS.md", "w", encoding="utf-8").write(t + V106_AGENTS)
print("aligned AGENTS.md (v106 paragraph appended)")

# ---------------- D2: CLAUDE.md ----------------
edit(
    "CLAUDE.md",
    [
        ("**E2E (Playwright, 308)**", "**E2E (Playwright, 309)**"),
        (
            "the fw-on-a-leaf-span form single-axis BY CONSTRUCTION)",
            "the fw-on-a-leaf-span form single-axis BY CONSTRUCTION), and the v106 pin: the networth "
            "asset-card facts-row interior census at 1280 (networth.spec.ts — the facts wrapper {block, 12px, "
            "rgb(107, 114, 128), h 40, rowCount 2} + both rows {flex/center/8px/h 16} + the Updated row's mt 8px "
            "[the v3 space-y-2 margin-top semantics restored by globals.css] + the 12×12 icon family {currentColor "
            "gray, viewBox 0 0 24 24} — the never-pinned family [the v46 pin holds the wrapper's font/color only; "
            "the rows' own interiors never asserted at ANY viewport], measured byte-identical both sides via the "
            "one-shot nw-facts-arbit-v106.sh; the mutation h-3 w-3 → h-3 w-3.5 at net-worth-view.tsx:118 "
            "line-scoped — the institution row's line 113 + the liability card's lines 218/224/229 untouched — only "
            "the v106 pin red at the Updated row's iconW axis alone, the single-dimension icon form single-axis BY "
            "CONSTRUCTION)",
        ),
    ],
)

# ---------------- D3: README.md ----------------
edit(
    "README.md",
    [
        (
            "📂 e2e/                    # Playwright specs (308 tests) + global setup",
            "📂 e2e/                    # Playwright specs (309 tests) + global setup",
        ),
        (
            "npm run test:e2e    # Playwright e2e (308 tests) — needs `npm run build` first",
            "npm run test:e2e    # Playwright e2e (309 tests) — needs `npm run build` first",
        ),
    ],
)

V106_README_ROW = (
    "| [`docs/remediation-plan-v106.md`](docs/remediation-plan-v106.md) | **The re-run cycle's next-oldest "
    "candidate (the v100-era NETWORTH + DRILL-DOWN pair's SEVENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → "
    "v100 → v106] — the NETWORTH view + the DASHBOARD's drill-down EXPANDED state at desktop 1280x800 full-page, "
    "last re-shot v100 — now the oldest remaining [v100 < v101 < v102 < v103 < v104 < v105]; the TWENTY-NINTH "
    "consecutive queue/ledger agreement — the probe-lineage authority applied over the session_258 prose) + the "
    "axe watch (NO DRIFT) + the 100th standing checks + the networth asset-card facts-row interior census pin "
    "(PIN-ONLY)**. The baseline on the FRESH-CLONE workspace (the sandbox reset: re-provisioned from scratch, the "
    "two post-push commits audited session-log/skills-sync-only — zero src/ or lockfile deltas); the verdicts "
    "NETWORTH IDENTICAL + DRILL-DOWN DIFFERENT (the pair's documented classes) with every drill-down flag "
    "DOM-arbitrated — the nav-highlight the v56 SUPERSET class, the avatar the user-identity class, the progress "
    "fill the pct DATA class, the donut labels the v60 perception class, the \"Total Expense vs Total Expenses\" "
    "flag a NEW VLM text-misread sub-form DISPROVEN by the direct live DOM read (the reference's own statTitles "
    "read \"Total Expenses\" — plural, byte-identical to the clone), the Freelance category + footer the "
    "seed-data class, the FAB the platform-chrome class; the two-half census (ARBIT_A 90 + ARBIT_B 111 lines, "
    "md5 457438e8/0b895e19 — the v100 census blocks verbatim) reproduces the v100 values exactly (the labelBlock "
    "WIDTH the ONE documented v82 DATA-CONDITIONAL delta) — NO NEW CLONE GAP; the +1 e2e pins the "
    "never-census'd facts-ROW interiors at 1280 (the wrapper {block/12px/gray/h 40/rowCount 2} + both rows "
    "{flex/center/8px/h 16} + the mt 8px v3 rhythm + the 12×12 icon family — the v46 pin holds the wrapper's "
    "font/color only; 309 e2e total), mutation-verified single-axis (h-3 w-3 → h-3 w-3.5 at "
    "net-worth-view.tsx:118, line-scoped — the Updated row's iconW axis alone, the 16px line box winning the row "
    "height) after the rebuild discipline. The ship: 309 e2e zero flakes across the auditable four-chunk split "
    "(117+94+59+42 = 312 executions = 309 unique); the screenshots 16/16 BYTE-IDENTICAL (the same-day "
    "regeneration — zero arbitration needed). |\n"
)
t = open("README.md", encoding="utf-8").read()
anchor = "the max-per-pixel-delta decomposition: glyph rolls d 400-700, rounding d ≤ 3). |\n"
i = t.find(anchor)
assert i >= 0, "README v105 row anchor not found"
t = t[: i + len(anchor)] + V106_README_ROW + t[i + len(anchor) :]
open("README.md", "w", encoding="utf-8").write(t)
print("aligned README.md (v106 row inserted)")

# ---------------- D4: zero-balance_SKILL.md ----------------
edit(
    "zero-balance_SKILL.md",
    [
        (
            "project_state: 108 unit tests / 308 e2e tests / 35 smoke steps — all green",
            "project_state: 108 unit tests / 309 e2e tests / 35 smoke steps — all green",
        ),
    ],
)
V106_SKILL_ROW = (
    "| 2026-10-23 | Session 141 — parity iteration v106 (`docs/remediation-plan-v106.md`) | **The re-run "
    "cycle's next-oldest candidate (the v100-era NETWORTH + DRILL-DOWN pair's SEVENTH re-run [v60 → v67 → v76 → "
    "v82 → v88 → v94 → v100 → v106] — the NETWORTH view + the DASHBOARD's drill-down EXPANDED state at desktop "
    "1280x800 full-page, last re-shot v100, now the oldest remaining [v100 < v101 < v102 < v103 < v104 < v105]; "
    "the TWENTY-NINTH consecutive queue/ledger agreement — the probe-lineage authority applied over the "
    "session_258 prose; the queue-prose verification lesson) + the axe watch (NO DRIFT — 4.14.0 holds) + the "
    "100th standing checks (ALL GREEN — the mobile menu working the 100th consecutive time; the census clean on "
    "the first read; the reference's four bugs all live) + the networth asset-card facts-row interior census pin "
    "at 1280 (PIN-ONLY; +1 e2e = 309)**: the verdicts NETWORTH IDENTICAL + DRILL-DOWN DIFFERENT (the pair's "
    "documented classes) with every drill-down flag DOM-arbitrated (the nav-highlight the v56 SUPERSET class; "
    "the avatar the user-identity class; the progress fill the pct DATA class [trackW 568 byte-identical, fillW "
    "the seed percentage]; the donut labels the v60 perception class [count 4 + labelLineCount 0 + labelFs 16px + "
    "labelFill black + sectors 3 byte-identical — the reference's own labels overlap under its seed]; the \"Total "
    "Expense vs Total Expenses\" flag a NEW VLM text-misread sub-form DISPROVEN by the direct live DOM read [the "
    "reference's own statTitles read \"Total Expenses\" plural — byte-identical to the clone's pinned family]; "
    "the Freelance category + footer count the seed-data class; the FAB the platform-chrome class); the "
    "two-half census (ARBIT_A 90 + ARBIT_B 111 lines, md5 457438e8/0b895e19 — the v100 census blocks verbatim) "
    "reproduces the v100 values exactly (the labelBlock WIDTH 304-vs-357 the ONE documented v82 "
    "DATA-CONDITIONAL delta) — NO NEW CLONE GAP; the +1 pin the networth ASSET CARD's FACTS-ROW interior family "
    "(the wrapper {block, 12px, rgb(107, 114, 128), h 40, rowCount 2} + both rows {flex/center/gap 8px/h 16} + "
    "the Updated row's mt 8px [the v3 space-y-2 margin-top semantics restored by globals.css] + the 12×12 icon "
    "family {currentColor gray, viewBox 0 0 24 24} — never pinned at ANY viewport [the v46 pin holds the "
    "wrapper's font/color only]; measured byte-identical both sides via the one-shot nw-facts-arbit-v106.sh), "
    "mutation-verified single-axis (h-3 w-3 → h-3 w-3.5 at net-worth-view.tsx:118 line-scoped — the Updated "
    "row's iconW axis alone, the 16px text line box winning the row height, the institution row's line 113 + "
    "the liability card's lines 218/224/229 untouched); the ship 309 e2e zero flakes (117+94+59+42 = 312 chunk "
    "executions across the four-chunk split — the per-file counts derived authoritatively before any chunk "
    "ran); 35/35 smoke; the screenshots 16/16 byte-identical (the same-day regeneration — zero arbitration "
    "needed) |** 108/309/35 green |\n"
)
t = open("zero-balance_SKILL.md", encoding="utf-8").read()
anchor = "| 2026-10-23 | Session 140 — parity iteration v105"
i = t.find(anchor)
assert i >= 0, "SKILL Session 140 row not found"
t = t[:i] + V106_SKILL_ROW + t[i:]
open("zero-balance_SKILL.md", "w", encoding="utf-8").write(t)
print("aligned zero-balance_SKILL.md (Session 141 row inserted)")

# ---------------- D5: PAD v1.1.63 block ----------------
V106_PAD = (
    "#### Revision Block — v1.1.63 (Tracked Changes)\n"
    "- `[UI]` v1.1.63 (2026-10-23) — the v106 parity iteration (PIN-ONLY — no production-code change): the "
    "counts 108 unit / **309 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v100-era "
    "NETWORTH + DRILL-DOWN pair's SEVENTH re-run [v60 -> v67 -> v76 -> v82 -> v88 -> v94 -> v100 -> v106] — the "
    "NETWORTH view + the DASHBOARD's drill-down EXPANDED state at desktop 1280x800 full-page, last re-shot "
    "v100; the TWENTY-NINTH consecutive queue/ledger agreement — the probe-lineage authority applied over the "
    "session_258 prose) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe intact) + the 100th standing "
    "checks (ALL GREEN — the mobile menu working the 100th consecutive time; the reference's four bugs all "
    "live; the census clean on the first read) + the networth asset-card facts-row interior census pin at 1280 "
    "(PIN-ONLY; +1 e2e = 309)**: the verdicts NETWORTH IDENTICAL + DRILL-DOWN DIFFERENT (the pair's documented "
    "classes) with every drill-down flag DOM-arbitrated to a documented class (the nav-highlight the v56 "
    "SUPERSET class; the avatar the user-identity class; the progress fill the pct DATA class; the donut labels "
    "the v60 perception class; the \"Total Expense vs Total Expenses\" flag a NEW VLM text-misread sub-form "
    "DISPROVEN by the direct live DOM read — the reference's own statTitles read \"Total Expenses\" plural, "
    "byte-identical to the clone's pinned family; the Freelance category + footer the seed-data class; the FAB "
    "the platform-chrome class); the two-half census (ARBIT_A 90 + ARBIT_B 111 lines, md5 "
    "457438e8/0b895e19 — the v100 census blocks verbatim) reproduces the v100 values exactly on every axis "
    "(the labelBlock WIDTH the ONE documented v82 DATA-CONDITIONAL delta) — NO NEW CLONE GAP; the +1 pin "
    "(tests/e2e/networth.spec.ts) the facts-ROW interior family — the wrapper "
    "{block/12px/rgb(107, 114, 128)/h 40/rowCount 2} + both rows {flex/center/8px/h 16} + the Updated row's "
    "mt 8px (the v3 space-y-2 rhythm restored by globals.css) + the 12x12 icon family — measured "
    "byte-identical both sides via the one-shot nw-facts-arbit-v106.sh; the mutation h-3 w-3 -> h-3 w-3.5 at "
    "net-worth-view.tsx:118 line-scoped — only the v106 pin red at the iconW axis alone after the rebuild; "
    "restored, rebuilt, post-restore green; the ship chain 309 e2e zero flakes (117+94+59+42 = 312 executions "
    "across four chunks), 35/35 smoke, the screenshots 16/16 byte-identical (the same-day regeneration); the "
    "queue-prose verification lesson re-applied (session_258.md's \"the v100-era DASHBOARD pair\" read through "
    "vlm-shots-v100.sh's own header — the NETWORTH + drill-down surfaces confirmed).\n"
)
t = open("Project_Architecture_Document.md", encoding="utf-8").read()
anchor = "#### Revision Block — v1.1.62 (Tracked Changes)"
i = t.find(anchor)
assert i >= 0, "PAD v1.1.62 block not found"
t = t[:i] + V106_PAD + t[i:]
open("Project_Architecture_Document.md", "w", encoding="utf-8").write(t)
print("aligned Project_Architecture_Document.md (v1.1.63 block inserted)")

# ---------------- D6: probe README ----------------
V106_PROBE_SECTION = (
    "### The v106 cycle (Session 141) — the v100-lineage derivation\n\n"
    "- `derive-v106-series.py` (persisted) — the v106 series derived from the\n"
    "  v100 lineage: vlm-shots-v106.sh + clone-vlmshots-v106.sh +\n"
    "  vlm-compare-v106.mjs + arbit-v106.sh; the generic swaps + the\n"
    "  exact-fragment history corrections (era v94-era->v100-era, last-re-shot\n"
    "  v94->v100, SIXTH->SEVENTH, the bracket extension ...v100 -> v106, the\n"
    "  TWENTY-THIRD->TWENTY-NINTH agreement ordinal, the census-axes reference)\n"
    "  — zero misses, zero residuals, line-count-preserving on all four.\n"
    "- `build-twohalf-v106.py` — the two-half builder (ARBIT_A 90 + ARBIT_B 111\n"
    "  lines, md5 457438e8/0b895e19): ref-arbit-v106.sh + clone-arbit-v106.sh,\n"
    "  the census JS byte-identical across the halves.\n"
    "- `derive-standing-v106.py` — the 100th standing pair (ref-standing-v100.sh\n"
    "  + standing-checks-v100.sh) from the v99 pair, the THREE token families,\n"
    "  normalize-back verified version-bump-only.\n"
    "- `nw-facts-arbit-v106.sh` — the ONE-SHOT both-sides census of the networth\n"
    "  ASSET CARD's FACTS-ROW interior family (the v106 pin's own axes measured\n"
    "  byte-identical on both sides before the pin). Finder lessons: the\n"
    "  \"Updated\" text is a BARE TEXT NODE beside the svg — no element leaf\n"
    "  carries it alone, so anchor the row finder on the row div whose\n"
    "  textContent STARTS WITH \"Updated\" (a /Updated/ substring match returns\n"
    "  the space-y-2 WRAPPER first — pre-order traversal); the facts wrapper is\n"
    "  the Updated row's parentElement, never a walk-up loop (a 12px+svg\n"
    "  predicate overshoots to the card body).\n\n"
    "### D6 — the operational lessons this cycle (v106)\n\n"
    "- THE TEXT-LAYER MISREAD CLASS (a VLM-arbitration note): the VLM can\n"
    "  misread a word's inflection (\"Total Expense\" vs the DOM's \"Total\n"
    "  Expenses\") — a flag class the v43 rule now covers at the TEXT layer:\n"
    "  when a VLM flag claims a WORD-level difference, read the reference's\n"
    "  live DOM for the exact string before counting the flag; the DOM is the\n"
    "  authority at every layer, glyph-level AND word-level.\n"
    "- THE QUEUE-PROSE VS LINEAGE NAMING (a rotation-ledger note): session\n"
    "  prose may name the re-run pair by ONE of its surfaces (\"the v100-era\n"
    "  DASHBOARD pair\" for the pair whose second surface IS the dashboard's\n"
    "  drill-down EXPANDED state); the probe lineage's own header (which\n"
    "  surfaces, which bracket) remains the authority — derive from the\n"
    "  header, note the prose in the plan.\n"
    "- THE SINGLE-DIMENSION ICON MUTATION FORM (a pin-design note): the\n"
    "  cleanest icon-family mutation changes ONE dimension only\n"
    "  (h-3 w-3 -> h-3 w-3.5: the W axis alone); the row height stays at the\n"
    "  text line box (max(16, 14) = 16) so no row-height axis cascades —\n"
    "  single-axis BY CONSTRUCTION, the v92 W-only form's sibling.\n\n"
    "The v107 queue (suggestions — verify against the rotation ledger before\n"
    "executing): (1) the re-run cadence rotates to the next-oldest candidate\n"
    "after the NETWORTH + DRILL-DOWN pair (the v101-era DASHBOARD pair — the\n"
    "BUDGET GUIDELINES card + the QUICK-ACTION row at desktop 1280x800\n"
    "full-page, last re-shot v101 — now the oldest remaining\n"
    "[v101 < v102 < v103 < v104 < v105 < v106]; the pair's re-run bracket to\n"
    "be verified against vlm-shots-v101.sh's own header before the\n"
    "derivation), (2) the axe-core watch at its next re-check point (only a\n"
    "5.x wrapper changes the calculus), (3) the deferred reference-write\n"
    "censuses (unchanged — out of bounds under the v46 read-only rule).\n"
)
t = open("scripts/parity-probes/README.md", encoding="utf-8").read()
i = t.find("The v106 queue (suggestions")
assert i >= 0, "v106 queue anchor not found"
t = t[:i] + V106_PROBE_SECTION
open("scripts/parity-probes/README.md", "w", encoding="utf-8").write(t)
print("aligned scripts/parity-probes/README.md (v106 section + v107 queue)")
print("D1-D6 aligned")
