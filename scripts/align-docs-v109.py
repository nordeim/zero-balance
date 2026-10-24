#!/usr/bin/env python3
"""D1-D7 docs alignment for the v109 cycle (Session 144).

D1 AGENTS.md  — append the v109 paragraph at the file end.
D2 CLAUDE.md  — E2E count 311 -> 312 + the v109 pin clause after the v108 clause.
D3 README.md  — the two count spots + the v109 plan-table row after the v108 row.
D4 zero-balance_SKILL.md — the project_state line + the Session 144 review row
               above Session 143's.
D5 PAD        — the v1.1.66 revision block above v1.1.65's.
D6 probe README — the v109 section (lineage + lessons) + the v110 queue
               replacing the v109 queue.
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


V109_AGENTS = (
    "\nReference surfaces pinned by the v109 iteration (`docs/remediation-plan-v109.md`) — "
    "**the re-run cycle's next-oldest candidate (the v103-era ITEMS pair's EIGHTH re-run "
    "[v57 -> v64 -> v70 -> v79 -> v85 -> v91 -> v97 -> v103 -> v109] — the INCOME + EXPENSES "
    "view pair at desktop 1280x800 FULL-PAGE, the v57-era items pair's surfaces, last re-shot "
    "v103; the THIRTY-SECOND consecutive queue/ledger agreement, the surface names verified "
    "against vlm-shots-v103.sh's own header before the derivation) + the axe watch (NO DRIFT "
    "— 4.14.0 holds, only rc/next sha prereleases beyond, no stable 4.14.1, no 5.x; the v68 "
    "dedupe verified) + the 103rd standing checks (ALL GREEN — the mobile menu VERIFIED "
    "WORKING the 103rd consecutive time; the reference's four bugs all live [the 464px "
    "/networth overflow measured docSW 464 directly]; the data census clean on the FIRST "
    "read; the SEO pair live both sides) + the items-view page-header row interior census "
    "pin at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 312; one "
    "documented config-comment exception: the vitest.config.ts stale sibling-seams header "
    "cleaned [the LOW item flagged since v106 — comment-only, zero functional impact])**. "
    "The verdicts INCOME IDENTICAL + EXPENSES DIFFERENT (the pair's flag-set within its "
    "documented verdict classes — v103 read BOTH DIFFERENT; the income side's documented "
    "flags were all-data classes, so the IDENTICAL verdict is the cleaner outcome on the "
    "same chrome — the verdict-variation form, the v105 LOGIN-IDENTICAL precedent) with "
    "every flag DOM-arbitrated: the expenses payment-chip footer the v57 DATA-CONDITIONAL "
    "class CENSUS-PROVEN live (the reference's OWN income card footer reads childCount 2 "
    "with the 'Bank Account' chip + icon — the reference RENDERS payment chips when data "
    "carries them; its expense items simply ship none — footer childCount 1 — while the "
    "clone's carry them); the badge-arrangement wrap the v57 wrap/classification-VALUE "
    "classes (the expenses badgeRow h ref 22 vs clone 52, badgeCount 3 vs 4 — the clone's "
    "Recurring superset chip + the wrap; the chip chrome byte-identical); the 'Edit with "
    "Base44' FAB the platform-chrome class DISPROVEN live (the one-shot both-sides census "
    "base44-fab-arbit-v109.sh: fabCount 0 + bodyHasBase44 false on BOTH sides at 1280 on "
    "/expenses — the FAB lives in the reference's platform iframe chrome, outside the app "
    "DOM; the v97/v103/v108 standing disproof form re-confirmed); the avatar the "
    "user-identity class (the chrome byte-identical); the data figures the seed-data "
    "classes. The two-half census (CENSUS_JS 193 lines, md5 b55dcd29 — the v97/v103 census "
    "block verbatim) reproduces the v103/v97 values EXACTLY on every axis (the avatar "
    "chrome; the grid + card + titleRow + amount + footer + badge + filterCard families on "
    "both variants; the docSW 1280 guards) — NO NEW CLONE GAP. The +1 e2e pin "
    "(tests/e2e/items.spec.ts): the ITEMS views' DESKTOP 1280 page-header row INTERIOR "
    "family on BOTH variants — never pinned at ANY viewport in ANY spec (the v65 pin holds "
    "the family on the SAVINGS variant only; the v52 pin the 390 stacked state; the tokens "
    "G2 pin the Add icon's w + shadow layers — the header row's computed chrome on the "
    "INCOME/EXPENSES variants at 1280 AND the LEFT BLOCK's interior [the chip-to-title "
    "junction row: flex/center/gap 12px] never asserted anywhere): the row {flex/"
    "space-between/center/gap 16px/mb 32px/h 60} + the left block {flex/center/gap 12px/h "
    "60/childCount 2} + the chip {48x48/radius 12px/the per-type gradient} + the chip icon "
    "{24x24/white} + the h1 {30px/700/lh 36px/rgb(26,58,46)} + the subtitle {16px/400/"
    "rgb(107,114,128)} + the Add button {147x36 income / 155x36 expenses, radius 6px, pad "
    "8px 16px, 14px/500, white, the per-type gradient} + the plus icon {16x16/mr 8px} + "
    "the docSW 1280 guard — measured byte-identical both sides both variants via the "
    "one-shot header-arbit-v109.sh; the mutation gap-3 -> gap-4 at items-view.tsx:132 "
    "line-scoped (the ONLY flex items-center gap-3 line in the file — the shared "
    "component's left-block row) fails ONLY the v109 pin at the left.gap axis ALONE "
    "('12px' -> '16px') after the standalone REBUILD — the SINGLE-AXIS CASCADE RULE "
    "APPLIED: the row's own gap-4/mb-8 rejected as mutation targets BECAUSE the shared "
    "component would cascade the v65 savings + v52 mobile pins (multi-spec failures); "
    "restored (git diff src/ = 0), rebuilt, post-restore 44/44 green. The ship chain: 312 "
    "e2e zero flakes (80+79+81+75 = 315 chunk executions across the auditable FOUR-chunk "
    "split — the per-file counts derived authoritatively via playwright --list BEFORE any "
    "chunk ran); 35/35 smoke; the screenshots 15/16 BYTE-IDENTICAL + ONE fresh-seed delta "
    "ARBITRATED (the 07-add-item-modal's single 22-row band, maxD 245 — the band-crop + "
    "VLM read: '10/23/2026' -> '10/24/2026', the modal's default-date field rolling with "
    "the UTC day — the documented date-roll class [the v104/v105 precedent], the updated "
    "set committed); the dev-server evidence set re-captured + VLM-verified (the menu "
    "proof: /income, docSW 390, navLandmark true).\n"
)

# ---------------- D1: AGENTS.md ----------------
t = open("AGENTS.md", encoding="utf-8").read()
open("AGENTS.md", "w", encoding="utf-8").write(t + V109_AGENTS)
print("aligned AGENTS.md (v109 paragraph appended)")

# ---------------- D2: CLAUDE.md ----------------
edit(
    "CLAUDE.md",
    [
        ("**E2E (Playwright, 311)**", "**E2E (Playwright, 312)**"),
    ],
)
edit(
    "CLAUDE.md",
    [
        (
            'single-axis BY CONSTRUCTION)\n- **Smoke (bash, 35 steps)**',
            'single-axis BY CONSTRUCTION), and the v109 pin: the items views\' page-header row '
            "interior census at 1280 on BOTH variants (items.spec.ts — the row {flex/space-between/"
            "center/gap 16px/mb 32px/h 60} + the LEFT BLOCK {flex/center/gap 12px/h 60/childCount 2 — "
            "the chip-to-title junction, never pinned on ANY variant at ANY viewport} + the chip "
            "{48×48/radius 12px/the per-type gradient} + the chip icon {24×24/white} + the h1 "
            "{30px/700/lh 36px/rgb(26,58,46)} + the subtitle {16px/400/rgb(107,114,128)} + the Add "
            "button {147×36 income/155×36 expenses, radius 6px, pad 8px 16px, 14px/500, white, the "
            "per-type gradient} + the plus icon {16×16/mr 8px} — the family the v65 pin holds on the "
            "SAVINGS variant only [the v92 family-extension pattern inverted]; measured byte-identical "
            "both sides both variants via the one-shot header-arbit-v109.sh; the left block's width + "
            "the h1's x-position stay census-documented but UNPINNED — the v107/v108 xInRow lesson; "
            "the mutation gap-3 → gap-4 at items-view.tsx:132 line-scoped — only the v109 pin red at "
            "the left.gap axis alone [\"12px\" → \"16px\"], single-axis AND cascade-free BY "
            'CONSTRUCTION [the shared-component rule: the row\'s own gap-4/mb-8 rejected — they '
            'would cascade the v65 savings + v52 mobile pins])\n- **Smoke (bash, 35 steps)**',
        ),
    ],
)

# ---------------- D3: README.md ----------------
edit(
    "README.md",
    [
        (
            "📂 e2e/                    # Playwright specs (311 tests) + global setup",
            "📂 e2e/                    # Playwright specs (312 tests) + global setup",
        ),
        (
            "npm run test:e2e    # Playwright e2e (311 tests) — needs `npm run build` first",
            "npm run test:e2e    # Playwright e2e (312 tests) — needs `npm run build` first",
        ),
    ],
)

V109_README_ROW = (
    "| [`docs/remediation-plan-v109.md`](docs/remediation-plan-v109.md) | **The re-run cycle's next-oldest "
    "candidate (the v103-era ITEMS pair's EIGHTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → "
    "v103 → v109] — the INCOME + EXPENSES view pair at desktop 1280×800 FULL-PAGE, the v57-era items "
    "pair's surfaces, last re-shot v103 — now the oldest remaining [v103 < v104 < v105 < v106 < v107 "
    "< v108]; the THIRTY-SECOND consecutive queue/ledger agreement — the surface names verified "
    "against vlm-shots-v103.sh's own header before the derivation) + the axe watch (NO DRIFT) + the "
    "103rd standing checks + the items-view page-header row interior census pin (PIN-ONLY)**. The "
    "baseline on the FRESH-CLONE workspace (the sandbox reset: re-provisioned from scratch — the zod "
    "extraction INTACT this cycle [840/840, no npm ci needed]; the two post-push commits audited "
    "session-log-only — zero src/ or lockfile deltas); the verdicts INCOME IDENTICAL + EXPENSES "
    "DIFFERENT (the pair's flag-set within its documented classes — the verdict-variation form, the "
    "v105 LOGIN-IDENTICAL precedent) with every flag DOM-arbitrated — the payment-chip footer the v57 "
    "DATA-CONDITIONAL class census-proven live (the reference's OWN income card renders the 'Bank "
    "Account' chip — footer childCount 2 — its expense items simply ship no payment method), the "
    "badge wrap the v57 wrap/classification-VALUE classes (badgeRow h 22 vs 52, badgeCount 3 vs 4 — "
    "the clone's Recurring superset chip), the 'Edit with Base44' FAB the platform-chrome class "
    "DISPROVEN live (fabCount 0 + bodyHasBase44 false both sides at 1280), the avatar the "
    "user-identity class, the data figures the seed classes; the two-half census (CENSUS_JS 193 "
    "lines, md5 b55dcd29 — the v97/v103 census block verbatim) reproduces the v103/v97 values "
    "exactly on every axis — NO NEW CLONE GAP; the +1 e2e pins the never-census'd ITEMS VIEWS' "
    "PAGE-HEADER ROW INTERIOR at 1280 on BOTH variants (the row {flex/space-between/center/gap "
    "16px/mb 32px/h 60} + the LEFT BLOCK {flex/center/gap 12px/h 60} — the chip-to-title junction "
    "never pinned on ANY variant + the chip {48×48/12px/per-type gradient} + the icon {24×24/white} "
    "+ the h1 {30px/700/36px/forestDark} + the subtitle {16px/400/gray} + the Add button "
    "{147×36/155×36, 6px, 8px 16px, 14px/500, white, per-type gradient} + the plus {16×16/mr 8px} — "
    "the v65 pin holds the SAVINGS variant only; 312 e2e total), measured byte-identical both sides "
    "both variants via the one-shot header-arbit-v109.sh, mutation-verified single-axis AND "
    "cascade-free (gap-3 → gap-4 at items-view.tsx:132 line-scoped — the shared-component rule "
    "applied: the row's own gap-4/mb-8 rejected as mutation targets because they would cascade the "
    "v65 savings + v52 mobile pins). The ship: 312 e2e zero flakes across the auditable four-chunk "
    "split (80+79+81+75 = 315 executions = 312 unique); the screenshots 15/16 byte-identical + ONE "
    "fresh-seed delta arbitrated (the 07-add-item-modal's single 22-row band = the default-date "
    "roll '10/23/2026' → '10/24/2026' — the documented date-roll class, the updated set committed); "
    "the dev evidence re-captured + VLM-verified (the menu proof: /income, docSW 390, navLandmark "
    "true); the vitest.config.ts stale sibling-seams comment cleaned (the LOW item flagged since "
    "v106 — comment-only). |\n"
)
t = open("README.md", encoding="utf-8").read()
anchor = "(77+78+78+81 = 314 executions = 311 unique); the screenshots 16/16 BYTE-IDENTICAL (the same-day regeneration — zero arbitration needed); the dev evidence re-captured + VLM-verified (the menu proof: /income, docSW 390, navLandmark true). |\n"
i = t.find(anchor)
assert i >= 0, "README v108 row anchor not found"
assert t.find(anchor, i + 1) == -1, "README v108 row anchor not unique"
t = t[: i + len(anchor)] + V109_README_ROW + t[i + len(anchor) :]
open("README.md", "w", encoding="utf-8").write(t)
print("aligned README.md (v109 row inserted)")

print("D1-D3 aligned")
