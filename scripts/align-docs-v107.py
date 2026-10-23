#!/usr/bin/env python3
"""D1-D7 docs alignment for the v107 cycle (Session 142).

D1 AGENTS.md  — append the v107 paragraph at the file end.
D2 CLAUDE.md  — E2E count 309 -> 310 + the v107 pin clause after the v106 clause.
D3 README.md  — the two count spots + the v107 plan-table row after the v106 row.
D4 zero-balance_SKILL.md — the project_state line + the Session 142 review row
               above Session 141's.
D5 PAD        — the v1.1.64 revision block above v1.1.63's.
D6 probe README — the v107 section (lineage + lessons) + the v108 queue
               replacing the v107 queue.
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


V107_AGENTS = (
    "\nReference surfaces pinned by the v107 iteration (`docs/remediation-plan-v107.md`) — "
    "**the re-run cycle's next-oldest candidate (the v101-era DASHBOARD pair's SEVENTH re-run "
    "[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107] — the BUDGET GUIDELINES card + the "
    "QUICK-ACTION row, the two v61-era below-the-fold surfaces on the DASHBOARD at desktop "
    "1280x800 full-page, last re-shot v101; the THIRTIETH consecutive queue/ledger agreement, the "
    "surface names verified against vlm-shots-v101.sh's own header before the derivation) + the "
    "axe watch (NO DRIFT — 4.14.0 holds, only rc/next sha prereleases beyond, the v68 dedupe "
    "holds) + the 101st standing checks (ALL GREEN — the mobile menu VERIFIED WORKING the 101st "
    "consecutive time; the reference's four bugs all live [the 464px /networth overflow measured "
    "docSW 464 directly]; the data census the 101st clean drift check — clean on the FIRST read; "
    "the SEO pair live both sides) + the quick-action card interior flex-row census pin at 1280 "
    "(PIN-ONLY for src/ — no production-code change; +1 e2e = 310)**. The verdict: the pair "
    "IDENTICAL — ZERO layout/style flags on the pair's own target surfaces (the FIFTH consecutive "
    "IDENTICAL verdict for this pair [v83 -> v89 -> v95 -> v101 -> v107]) — the only flags the "
    "documented standing classes: the nav-highlight the v56 SUPERSET class (the reference's "
    "root-route bug), the avatar the user-identity class, the seed-data figures each site's own "
    "data; NO FAB flag raised this cycle (the v103 standing class — either form without "
    "surprise). The two-half census (ARBIT_G 61 + ARBIT_Q 58 + ARBIT_X 25 lines, md5 "
    "b500dd29/da04e995/7a381755 — the v101 census blocks verbatim) reproduces the v101 values "
    "EXACTLY on every axis (the PART G guidelines card: 468x348/radius 12px/the header + the "
    "three 418x78 tinted tiles — the shadow's transparent lead-layer count the ONE v66 INVISIBLE "
    "class delta; the PART Q quick-action row: the grid 304px x3/gap 24/w 960 + the three "
    "304x90 cards — the grid mt [ref 0px vs clone 32px] the v77 mechanism class, the label "
    "finder's wrapper catch the v61 label lesson; the PART X cross-row gap: cardBottom "
    "1122/gridTop 1462/gap 340 byte-identical) — NO NEW CLONE GAP. The +1 e2e pin "
    "(tests/e2e/dashboard.spec.ts): the quick-action card's INTERIOR FLEX-ROW family — never "
    "pinned at ANY viewport in ANY spec (the v61 F3 pin holds the card/tile/icon/label/plus BOX "
    "chrome; the v45 F3b pin the hover shadow; the row's own flex/gap-12 centering, the tile's "
    "flex centering, and the icon's (40-20)/2 centering offsets were unpinned): the row {flex, "
    "center, gap 12px, h 40, childCount 3} + the tile {flex, center, center, 40x40, radius 12px} "
    "+ the icon {20x20, offX 10, offY 10} + the label leaf {16px/500/rgb(26, 58, 46)} + the plus "
    "{16/16/0.5} — measured byte-identical on BOTH sides via the one-shot census "
    "qarow-arbit-v107.sh (THE STRUCTURAL-FINDER LESSON: the reference's row/tile are DIVs while "
    "the clone's are SPANs — identical computed chrome, different tags — so the finders walk "
    "POSITIONALLY [firstElementChild children order], never by tag, and the label leaf finder is "
    "the v61 leaf lesson generalized TAG-AGNOSTIC; every axis DATA-INDEPENDENT — the three labels "
    "fixed strings). The pin GREEN on first run (44/44 in dashboard.spec.ts); the pin-sanity "
    "mutation (dashboard-view.tsx:888 gap-3 -> gap-4, LINE-NUMBER-SCOPED — the line carries "
    "EXACTLY ONE flex items-center gap-3, the QuickActionCard's own row; the page header's line "
    "97 + the legend slice row's line 781 untouched) fails ONLY the v107 pin (43 green) at the "
    "row's gap axis ALONE (\"12px\" -> \"16px\") after the standalone REBUILD; restored (git "
    "diff src/ = 0), rebuilt, post-restore 44/44 green. The ship chain: 310 e2e zero flakes "
    "(123+89+61+40 = 313 chunk executions across the auditable FOUR-chunk split — the per-file "
    "counts derived authoritatively via playwright --list BEFORE any chunk ran, the v103 lesson "
    "applied); 35/35 smoke; the screenshots 16/16 BYTE-IDENTICAL (the same-day-seed law — zero "
    "arbitration needed this cycle).\n"
)

# ---------------- D1: AGENTS.md ----------------
t = open("AGENTS.md", encoding="utf-8").read()
open("AGENTS.md", "w", encoding="utf-8").write(t + V107_AGENTS)
print("aligned AGENTS.md (v107 paragraph appended)")

# ---------------- D2: CLAUDE.md ----------------
edit(
    "CLAUDE.md",
    [
        ("**E2E (Playwright, 309)**", "**E2E (Playwright, 310)**"),
        (
            "the single-dimension icon form single-axis BY CONSTRUCTION)",
            "the single-dimension icon form single-axis BY CONSTRUCTION), and the v107 pin: the "
            "quick-action card interior flex-row census at 1280 (dashboard.spec.ts — the row "
            "{flex/center/gap 12px/h 40/childCount 3} + the tile {flex/center/center/40×40/"
            "radius 12px} + the icon {20×20, offX 10, offY 10 — the (40−20)/2 centering "
            "arithmetic} + the label leaf {16px/500/forestDark} + the plus {16/16/0.5} — the "
            "never-pinned family [the v61 F3 pin holds the card/tile/icon/label/plus BOX chrome "
            "only; the row's own flex/gap centering + the tile's flex centering + the icon's "
            "centering offsets never asserted at ANY viewport], measured byte-identical both "
            "sides via the one-shot qarow-arbit-v107.sh with STRUCTURAL finders — the "
            "reference's row/tile are DIVs, the clone's SPANs, identical computed chrome, so "
            "the finders walk POSITIONALLY [firstElementChild], never by tag, and the label "
            "leaf finder is the v61 leaf lesson generalized tag-agnostic; the mutation gap-3 → "
            "gap-4 at dashboard-view.tsx:888 line-scoped — the page header's line 97 + the "
            "legend slice row's line 781 untouched — only the v107 pin red at the row's gap "
            "axis alone [\"12px\" → \"16px\"], single-axis BY CONSTRUCTION)",
        ),
    ],
)

# ---------------- D3: README.md ----------------
edit(
    "README.md",
    [
        (
            "📂 e2e/                    # Playwright specs (309 tests) + global setup",
            "📂 e2e/                    # Playwright specs (310 tests) + global setup",
        ),
        (
            "npm run test:e2e    # Playwright e2e (309 tests) — needs `npm run build` first",
            "npm run test:e2e    # Playwright e2e (310 tests) — needs `npm run build` first",
        ),
    ],
)

V107_README_ROW = (
    "| [`docs/remediation-plan-v107.md`](docs/remediation-plan-v107.md) | **The re-run cycle's next-oldest "
    "candidate (the v101-era DASHBOARD pair's SEVENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → "
    "v101 → v107] — the BUDGET GUIDELINES card + the QUICK-ACTION row, the two v61-era "
    "below-the-fold surfaces on the DASHBOARD at desktop 1280x800 full-page, last re-shot v101 — "
    "now the oldest remaining [v101 < v102 < v103 < v104 < v105 < v106]; the THIRTIETH "
    "consecutive queue/ledger agreement — the surface names verified against vlm-shots-v101.sh's "
    "own header before the derivation) + the axe watch (NO DRIFT) + the 101st standing checks + "
    "the quick-action card interior flex-row census pin (PIN-ONLY)**. The baseline on the "
    "FRESH-CLONE workspace (the sandbox reset: re-provisioned from scratch, the two post-push "
    "commits audited session-log/skills-sync-only — zero src/ or lockfile deltas); the verdict "
    "IDENTICAL — ZERO layout/style flags on the pair's own target surfaces (the FIFTH consecutive "
    "IDENTICAL verdict for this pair [v83 → v89 → v95 → v101 → v107]) with the only flags the "
    "documented standing classes — the nav-highlight the v56 SUPERSET class, the avatar the "
    "user-identity class, the seed-data figures each site's own data; no FAB flag raised this "
    "cycle; the two-half census (ARBIT_G 61 + ARBIT_Q 58 + ARBIT_X 25 lines, md5 "
    "b500dd29/da04e995/7a381755 — the v101 census blocks verbatim) reproduces the v101 values "
    "exactly (the shadow lead-layers the v66 INVISIBLE class; the grid mt the v77 mechanism "
    "class; the label wrapper the v61 label lesson; the PART X gap 340 byte-identical) — NO NEW "
    "CLONE GAP; the +1 e2e pins the never-census'd interior flex-row family at 1280 (the row "
    "{flex/center/gap 12px/h 40/childCount 3} + the tile {flex/center/center/40×40/radius 12px} "
    "+ the icon {20×20, offsets 10/10} + the label leaf {16px/500/forestDark} + the plus "
    "{16/16/0.5} — the v61 F3 pin holds the BOX chrome only; 310 e2e total), measured "
    "byte-identical both sides via the one-shot qarow-arbit-v107.sh with STRUCTURAL finders (the "
    "reference's row/tile DIVs vs the clone's SPANs — identical computed chrome, positional "
    "walk), mutation-verified single-axis (gap-3 → gap-4 at dashboard-view.tsx:888, line-scoped "
    "— the row's gap axis alone) after the rebuild discipline. The ship: 310 e2e zero flakes "
    "across the auditable four-chunk split (123+89+61+40 = 313 executions = 310 unique); the "
    "screenshots 16/16 BYTE-IDENTICAL (the same-day regeneration — zero arbitration needed). |\n"
)
t = open("README.md", encoding="utf-8").read()
anchor = "zero arbitration needed). |\n"
i = t.find(anchor)
assert i >= 0, "README v106 row anchor not found"
assert t.find(anchor, i + 1) == -1, "README v106 row anchor not unique"
t = t[: i + len(anchor)] + V107_README_ROW + t[i + len(anchor) :]
open("README.md", "w", encoding="utf-8").write(t)
print("aligned README.md (v107 row inserted)")

# ---------------- D4: zero-balance_SKILL.md ----------------
edit(
    "zero-balance_SKILL.md",
    [
        (
            "project_state: 108 unit tests / 309 e2e tests / 35 smoke steps — all green",
            "project_state: 108 unit tests / 310 e2e tests / 35 smoke steps — all green",
        ),
    ],
)
V107_SKILL_ROW = (
    "| 2026-10-23 | Session 142 — parity iteration v107 (`docs/remediation-plan-v107.md`) | **The re-run "
    "cycle's next-oldest candidate (the v101-era DASHBOARD pair's SEVENTH re-run [v61 → v68 → "
    "v77 → v83 → v89 → v95 → v101 → v107] — the BUDGET GUIDELINES card + the QUICK-ACTION row, "
    "the two v61-era below-the-fold surfaces on the DASHBOARD at desktop 1280x800 full-page, "
    "last re-shot v101, now the oldest remaining [v101 < v102 < v103 < v104 < v105 < v106]; the "
    "THIRTIETH consecutive queue/ledger agreement — the surface names verified against "
    "vlm-shots-v101.sh's own header before the derivation) + the axe watch (NO DRIFT — 4.14.0 "
    "holds) + the 101st standing checks (ALL GREEN — the mobile menu working the 101st "
    "consecutive time; the census clean on the first read; the reference's four bugs all live) + "
    "the quick-action card interior flex-row census pin at 1280 (PIN-ONLY; +1 e2e = 310)**: the "
    "verdict IDENTICAL — zero layout/style flags on the pair's own target surfaces (the FIFTH "
    "consecutive IDENTICAL verdict for this pair [v83 → v89 → v95 → v101 → v107]) with the only "
    "flags the documented standing classes (the nav-highlight the v56 SUPERSET class; the avatar "
    "the user-identity class; the seed-data figures each site's own data; no FAB flag this "
    "cycle — the v103 standing class); the two-half census (ARBIT_G 61 + ARBIT_Q 58 + ARBIT_X 25 "
    "lines, md5 b500dd29/da04e995/7a381755 — the v101 census blocks verbatim) reproduces the "
    "v101 values exactly (the shadow lead-layers the v66 INVISIBLE class; the grid mt the v77 "
    "mechanism class; the label wrapper the v61 label lesson; the PART X gap 340 "
    "byte-identical) — NO NEW CLONE GAP; the +1 pin the quick-action card's INTERIOR FLEX-ROW "
    "family (the row {flex/center/gap 12px/h 40/childCount 3} + the tile {flex/center/center/"
    "40×40/radius 12px} + the icon {20×20, offX 10, offY 10 — the (40−20)/2 centering "
    "arithmetic} + the label leaf {16px/500/forestDark} + the plus {16/16/0.5} — never pinned at "
    "ANY viewport [the v61 F3 pin holds the BOX chrome only]; measured byte-identical both sides "
    "via the one-shot qarow-arbit-v107.sh with STRUCTURAL finders [the reference's row/tile DIVs "
    "vs the clone's SPANs — identical computed chrome, the positional firstElementChild walk, "
    "the tag-agnostic leaf finder]), mutation-verified single-axis (gap-3 → gap-4 at "
    "dashboard-view.tsx:888 line-scoped — the row's gap axis alone [\"12px\" → \"16px\"], the "
    "page header's line 97 + the legend slice row's line 781 untouched); the ship 310 e2e zero "
    "flakes (123+89+61+40 = 313 chunk executions across the four-chunk split — the per-file "
    "counts derived authoritatively before any chunk ran); 35/35 smoke; the screenshots 16/16 "
    "byte-identical (the same-day regeneration — zero arbitration needed) |** 108/310/35 green |\n"
)
t = open("zero-balance_SKILL.md", encoding="utf-8").read()
anchor = "| 2026-10-23 | Session 141 — parity iteration v106"
i = t.find(anchor)
assert i >= 0, "SKILL Session 141 row not found"
t = t[:i] + V107_SKILL_ROW + t[i:]
open("zero-balance_SKILL.md", "w", encoding="utf-8").write(t)
print("aligned zero-balance_SKILL.md (Session 142 row inserted)")

# ---------------- D5: PAD v1.1.64 block ----------------
V107_PAD = (
    "#### Revision Block — v1.1.64 (Tracked Changes)\n"
    "- `[UI]` v1.1.64 (2026-10-23) — the v107 parity iteration (PIN-ONLY — no production-code "
    "change): the counts 108 unit / **310 e2e** (+1) / 35 smoke; **the re-run cycle's "
    "next-oldest candidate (the v101-era DASHBOARD pair's SEVENTH re-run [v61 -> v68 -> v77 -> "
    "v83 -> v89 -> v95 -> v101 -> v107] — the BUDGET GUIDELINES card + the QUICK-ACTION row, the "
    "two v61-era below-the-fold surfaces on the DASHBOARD at desktop 1280x800 full-page, last "
    "re-shot v101; the THIRTIETH consecutive queue/ledger agreement — the surface names verified "
    "against vlm-shots-v101.sh's own header before the derivation) + the axe watch (NO DRIFT — "
    "4.14.0 holds, the v68 dedupe intact) + the 101st standing checks (ALL GREEN — the mobile "
    "menu working the 101st consecutive time; the reference's four bugs all live; the census "
    "clean on the first read) + the quick-action card interior flex-row census pin at 1280 "
    "(PIN-ONLY; +1 e2e = 310)**: the verdict IDENTICAL — zero layout/style flags on the pair's "
    "own target surfaces (the FIFTH consecutive IDENTICAL verdict for this pair [v83 -> v89 -> "
    "v95 -> v101 -> v107]) with the only flags the documented standing classes (the nav-highlight "
    "the v56 SUPERSET class; the avatar the user-identity class; the seed-data figures each "
    "site's own data; no FAB flag raised this cycle — the v103 standing class); the two-half "
    "census (ARBIT_G 61 + ARBIT_Q 58 + ARBIT_X 25 lines, md5 b500dd29/da04e995/7a381755 — the "
    "v101 census blocks verbatim) reproduces the v101 values exactly on every axis (the shadow "
    "lead-layers the v66 INVISIBLE class; the grid mt the v77 mechanism class; the label wrapper "
    "the v61 label lesson; the PART X gap 340 byte-identical) — NO NEW CLONE GAP; the +1 pin "
    "(tests/e2e/dashboard.spec.ts) the interior flex-row family — the row {flex/center/gap "
    "12px/h 40/childCount 3} + the tile {flex/center/center/40x40/radius 12px} + the icon "
    "{20x20, offX 10, offY 10} + the label leaf {16px/500/rgb(26, 58, 46)} + the plus {16/16/"
    "0.5} — measured byte-identical both sides via the one-shot qarow-arbit-v107.sh (THE "
    "STRUCTURAL-FINDER LESSON: the reference's row/tile are DIVs, the clone's SPANs — identical "
    "computed chrome, different tags — the finders walk POSITIONALLY [firstElementChild], never "
    "by tag; the label leaf finder the v61 leaf lesson generalized tag-agnostic); the mutation "
    "gap-3 -> gap-4 at dashboard-view.tsx:888 line-scoped — only the v107 pin red at the row's "
    "gap axis alone after the rebuild; restored, rebuilt, post-restore green; the ship chain 310 "
    "e2e zero flakes (123+89+61+40 = 313 executions across four chunks), 35/35 smoke, the "
    "screenshots 16/16 byte-identical (the same-day regeneration).\n"
)
t = open("Project_Architecture_Document.md", encoding="utf-8").read()
anchor = "#### Revision Block — v1.1.63 (Tracked Changes)"
i = t.find(anchor)
assert i >= 0, "PAD v1.1.63 block not found"
t = t[:i] + V107_PAD + t[i:]
open("Project_Architecture_Document.md", "w", encoding="utf-8").write(t)
print("aligned Project_Architecture_Document.md (v1.1.64 block inserted)")

# ---------------- D6: probe README ----------------
V107_PROBE_SECTION = (
    "### The v107 cycle (Session 142) — the v101-lineage derivation\n\n"
    "- `derive-v107-series.py` (persisted) — the v107 series derived from the\n"
    "  v101 lineage: vlm-shots-v107.sh + clone-vlmshots-v107.sh +\n"
    "  vlm-compare-v107.mjs + arbit-v107.sh; the generic swaps + the NINE\n"
    "  exact-fragment history corrections (era v95-era->v101-era, last-re-shot\n"
    "  v95->v101, SIXTH->SEVENTH, the bracket extension ...v101 -> v107, the\n"
    "  oldest-remaining list bumped to the current era, the TWENTY-FOURTH->\n"
    "  THIRTIETH agreement ordinal, the re-proves window v95-v100->v101-v106,\n"
    "  the arbit verdict reference v95->v101, the drift-re-check v95->v101)\n"
    "  — 9/9 on the FIRST run, zero residuals, line-count-preserving on all\n"
    "  four (57/42/45/258).\n"
    "- `build-twohalf-v107.py` — the two-half builder (ARBIT_G 61 + ARBIT_Q 58\n"
    "  + ARBIT_X 25 lines, md5 b500dd29/da04e995/7a381755 — the v101 census\n"
    "  blocks VERBATIM, the blocks themselves version-free): ref-arbit-v107.sh\n"
    "  + clone-arbit-v107.sh, the census JS byte-identical across the halves.\n"
    "- `derive-standing-v107.py` — the 101st standing pair (ref-standing-v101.sh\n"
    "  + standing-checks-v101.sh) from the v100 pair, the THREE token families\n"
    "  (note the ordinal token's suffix flip 100th->101st), normalize-back\n"
    "  verified version-bump-only.\n"
    "- `qarow-arbit-v107.sh` — the ONE-SHOT both-sides census of the\n"
    "  quick-action card's INTERIOR FLEX-ROW family (the v107 pin's own axes\n"
    "  measured byte-identical on both sides before the pin). THE\n"
    "  STRUCTURAL-FINDER LESSON: the reference's row/tile are DIVs while the\n"
    "  clone's are SPANs — identical computed chrome, different tags — so the\n"
    "  finders walk POSITIONALLY (the row = the button's firstElementChild;\n"
    "  the tile = the row's firstElementChild; the icon = the row's first\n"
    "  svg; the plus = the row's last svg), NEVER by tag; the label leaf\n"
    "  finder is the v61 leaf lesson generalized TAG-AGNOSTIC (the exact\n"
    "  text + zero element children, any tag — a div on the reference, a\n"
    "  span on the clone).\n\n"
    "### D6 — the operational lessons this cycle (v107)\n\n"
    "- THE STRUCTURAL-FINDER RULE (a census-finder note): when a family's DOM\n"
    "  tags differ across sites (DIV vs SPAN — the computed-chrome class),\n"
    "  walk POSITIONALLY (firstElementChild children order), never by tag;\n"
    "  generalize leaf finders tag-agnostically (exact text + zero element\n"
    "  children, any tag) — the v61 leaf lesson's next form. A tag-matched\n"
    "  finder silently returns null on one side and manufactures a false\n"
    "  gap.\n"
    "- THE LINE-BREAK FRAGMENT HAZARD (a derive-script note): history-\n"
    "  correction fragments must be SINGLE-LINE-SAFE — probe headers wrap at\n"
    "  ~78 chars, so a fragment spanning a line break (\"the\\n# v95-era pair\",\n"
    "  \"SIXTH\\n# re-run\", \"after\\n# v95-v100\", \"The v95\\n# verdict\") never\n"
    "  matches; cut each correction fragment to the unbroken span (\"v95-era\n"
    "  pair\", \"SIXTH\", \"v95-v100\", \"The v95\") and verify per-file hit counts\n"
    "  so a miss fails the derivation rather than shipping a stale header.\n"
    "- THE UNPINNED POSITION-ARITHMETIC AXES (a pin-design note): the census\n"
    "  may measure position arithmetic byte-identical (the label's 40+12\n"
    "  junction x = 52; the plus's right-edge anchor = 238), but the PIN\n"
    "  holds the STRUCTURAL chrome only — position axes co-move with\n"
    "  unrelated mutations (gap-3 -> gap-4 moves the label's x too), so\n"
    "  pinning them would break the single-axis mutation discipline; keep\n"
    "  them census-documented, pin-unasserted.\n\n"
    "The v108 queue (suggestions — verify against the rotation ledger before\n"
    "executing): (1) the re-run cadence rotates to the next-oldest candidate\n"
    "after the v101-era DASHBOARD pair (the v102-era MOBILE TWINS pair — BOTH\n"
    "mobile 390x844 full-page twins: (1) the /NETWORTH view (the v63-era\n"
    "pair's surface) and (2) the DASHBOARD (the v62-era mobile twin's\n"
    "surface), last re-shot v102 — now the oldest remaining\n"
    "[v102 < v103 < v104 < v105 < v106 < v107]; the pair's SEVENTH re-run\n"
    "bracket [v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108] to\n"
    "be verified against vlm-shots-v102.sh's own header before the\n"
    "derivation), (2) the axe-core watch at its next re-check point (only a\n"
    "5.x wrapper changes the calculus), (3) the deferred reference-write\n"
    "censuses (unchanged — out of bounds under the v46 read-only rule).\n"
)
t = open("scripts/parity-probes/README.md", encoding="utf-8").read()
i = t.find("The v107 queue (suggestions")
assert i >= 0, "v107 queue anchor not found"
t = t[:i] + V107_PROBE_SECTION
open("scripts/parity-probes/README.md", "w", encoding="utf-8").write(t)
print("aligned scripts/parity-probes/README.md (v107 section + v108 queue)")
print("D1-D6 aligned")

