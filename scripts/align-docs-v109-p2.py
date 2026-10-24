#!/usr/bin/env python3
"""D4-D6 docs alignment for the v109 cycle (Session 144) — part 2.

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


# ---------------- D4: zero-balance_SKILL.md ----------------
edit(
    "zero-balance_SKILL.md",
    [
        (
            "project_state: 108 unit tests / 311 e2e tests / 35 smoke steps — all green",
            "project_state: 108 unit tests / 312 e2e tests / 35 smoke steps — all green",
        ),
    ],
)
V109_SKILL_ROW = (
    "| 2026-10-24 | Session 144 — parity iteration v109 (`docs/remediation-plan-v109.md`) | **The re-run "
    "cycle's next-oldest candidate (the v103-era ITEMS pair's EIGHTH re-run [v57 → v64 → v70 → v79 → "
    "v85 → v91 → v97 → v103 → v109] — the INCOME + EXPENSES view pair at desktop 1280×800 FULL-PAGE, "
    "the v57-era items pair's surfaces, last re-shot v103, now the oldest remaining [v103 < v104 < "
    "v105 < v106 < v107 < v108]; the THIRTY-SECOND consecutive queue/ledger agreement — the surface "
    "names verified against vlm-shots-v103.sh's own header before the derivation) + the axe watch "
    "(NO DRIFT — 4.14.0 holds) + the 103rd standing checks (ALL GREEN — the mobile menu working the "
    "103rd consecutive time; the census clean on the first read; the reference's four bugs all live) "
    "+ the items-view page-header row interior census pin at 1280 (PIN-ONLY; +1 e2e = 312; one "
    "config-comment exception: the vitest.config.ts stale sibling-seams header cleaned — the LOW "
    "item flagged since v106)**: the verdicts INCOME IDENTICAL + EXPENSES DIFFERENT (the pair's "
    "flag-set within its documented classes — the verdict-variation form, the v105 LOGIN-IDENTICAL "
    "precedent) with every flag DOM-arbitrated (the payment-chip footer the v57 DATA-CONDITIONAL "
    "class census-proven live — the reference's OWN income card renders the 'Bank Account' chip, "
    "footer childCount 2, its expense items simply ship none; the badge wrap the v57 wrap/"
    "classification-VALUE classes [badgeRow h 22 vs 52, badgeCount 3 vs 4 — the clone's Recurring "
    "superset chip]; the 'Edit with Base44' FAB the platform-chrome class DISPROVEN live [fabCount "
    "0 + bodyHasBase44 false both sides at 1280 on /expenses]; the avatar the user-identity class; "
    "the data figures the seed classes); the two-half census (CENSUS_JS 193 lines, md5 b55dcd29 — "
    "the v97/v103 census block verbatim) reproduces the v103/v97 values exactly on every axis — "
    "NO NEW CLONE GAP; the +1 pin the ITEMS VIEWS' PAGE-HEADER ROW INTERIOR at 1280 on BOTH "
    "variants (the row {flex/space-between/center/gap 16px/mb 32px/h 60} + the LEFT BLOCK "
    "{flex/center/gap 12px/h 60/childCount 2 — the chip-to-title junction, never pinned on ANY "
    "variant at ANY viewport} + the chip {48×48/radius 12px/the per-type gradient} + the chip icon "
    "{24×24/white} + the h1 {30px/700/lh 36px/rgb(26,58,46)} + the subtitle {16px/400/"
    "rgb(107,114,128)} + the Add button {147×36 income/155×36 expenses, radius 6px, pad 8px 16px, "
    "14px/500, white, the per-type gradient} + the plus icon {16×16/mr 8px} — the v65 pin holds "
    "the SAVINGS variant only, the v92 family-extension pattern inverted; measured byte-identical "
    "both sides both variants via the one-shot header-arbit-v109.sh), mutation-verified "
    "single-axis AND cascade-free (gap-3 → gap-4 at items-view.tsx:132 line-scoped — the ONLY "
    "flex items-center gap-3 line in the file; the shared-component rule applied: the row's own "
    "gap-4/mb-8 rejected as mutation targets because they would cascade the v65 savings + v52 "
    "mobile pins); the ship 312 e2e zero flakes (80+79+81+75 = 315 chunk executions across the "
    "four-chunk split — the per-file counts derived authoritatively before any chunk ran); 35/35 "
    "smoke; the screenshots 15/16 byte-identical + ONE fresh-seed delta arbitrated (the "
    "07-add-item-modal's single 22-row band, maxD 245 — the band-crop + VLM read: '10/23/2026' → "
    "'10/24/2026', the modal's default-date field rolling with the UTC day — the documented "
    "date-roll class, the updated set committed); the dev evidence re-captured + VLM-verified "
    "(the menu proof: /income, docSW 390, navLandmark true) |** 108/312/35 green |\n"
)
t = open("zero-balance_SKILL.md", encoding="utf-8").read()
anchor = "| 2026-10-24 | Session 143 — parity iteration v108"
i = t.find(anchor)
assert i >= 0, "SKILL Session 143 row not found"
t = t[:i] + V109_SKILL_ROW + t[i:]
open("zero-balance_SKILL.md", "w", encoding="utf-8").write(t)
print("aligned zero-balance_SKILL.md (Session 144 row inserted)")

# ---------------- D5: PAD v1.1.66 block ----------------
V109_PAD = (
    "#### Revision Block — v1.1.66 (Tracked Changes)\n"
    "- `[UI]` v1.1.66 (2026-10-24) — the v109 parity iteration (PIN-ONLY — no production-code "
    "change; one config-comment exception: the vitest.config.ts stale sibling-seams header "
    "cleaned, the LOW item flagged since v106): the counts 108 unit / **312 e2e** (+1) / 35 "
    "smoke; **the re-run cycle's next-oldest candidate (the v103-era ITEMS pair's EIGHTH re-run "
    "[v57 -> v64 -> v70 -> v79 -> v85 -> v91 -> v97 -> v103 -> v109] — the INCOME + EXPENSES "
    "view pair at desktop 1280x800 FULL-PAGE, the v57-era items pair's surfaces, last re-shot "
    "v103; the THIRTY-SECOND consecutive queue/ledger agreement — the surface names verified "
    "against vlm-shots-v103.sh's own header before the derivation) + the axe watch (NO DRIFT — "
    "4.14.0 holds, the v68 dedupe verified) + the 103rd standing checks (ALL GREEN — the mobile "
    "menu working the 103rd consecutive time; the reference's four bugs all live; the census "
    "clean on the first read) + the items-view page-header row interior census pin at 1280 "
    "(PIN-ONLY; +1 e2e = 312)**: the verdicts INCOME IDENTICAL + EXPENSES DIFFERENT (the pair's "
    "flag-set within its documented classes — the verdict-variation form, the v105 "
    "LOGIN-IDENTICAL precedent) with every flag DOM-arbitrated to a documented class (the "
    "payment-chip footer the v57 DATA-CONDITIONAL class census-proven live — the reference's "
    "OWN income card renders the 'Bank Account' chip, footer childCount 2, its expense items "
    "simply ship none; the badge wrap the v57 wrap/classification-VALUE classes; the 'Edit with "
    "Base44' FAB the platform-chrome class DISPROVEN live [fabCount 0 + bodyHasBase44 false on "
    "both sides at 1280 on /expenses]; the avatar the user-identity class; the data figures the "
    "seed-data classes); the two-half census (CENSUS_JS 193 lines, md5 b55dcd29 — the v97/v103 "
    "census block verbatim) reproduces the v103/v97 values exactly on every axis — NO NEW "
    "CLONE GAP; the +1 pin (tests/e2e/items.spec.ts) the ITEMS VIEWS' PAGE-HEADER ROW INTERIOR "
    "family at 1280 on BOTH variants — the row {flex/space-between/center/gap 16px/mb 32px/h "
    "60} + the LEFT BLOCK {flex/center/gap 12px/h 60/childCount 2} + the chip {48x48/radius "
    "12px/the per-type gradient} + the chip icon {24x24/white} + the h1 {30px/700/lh 36px/"
    "rgb(26,58,46)} + the subtitle {16px/400/rgb(107,114,128)} + the Add button {147x36 "
    "income/155x36 expenses, radius 6px, pad 8px 16px, 14px/500, white, the per-type gradient} "
    "+ the plus icon {16x16/mr 8px} — measured byte-identical both sides both variants via the "
    "one-shot header-arbit-v109.sh; the mutation gap-3 -> gap-4 at items-view.tsx:132 "
    "line-scoped — only the v109 pin red at the left.gap axis alone after the rebuild (THE "
    "SINGLE-AXIS CASCADE RULE: the shared component's row gap-4/mb-8 rejected as mutation "
    "targets — they would cascade the v65 savings + v52 mobile pins); restored, rebuilt, "
    "post-restore 44/44 green; the ship chain 312 e2e zero flakes (80+79+81+75 = 315 "
    "executions across four chunks), 35/35 smoke, the screenshots 15/16 byte-identical + ONE "
    "fresh-seed delta arbitrated (the 07-add-item-modal's default-date roll '10/23/2026' -> "
    "'10/24/2026' — the documented date-roll class, the updated set committed).\n"
)
t = open("Project_Architecture_Document.md", encoding="utf-8").read()
anchor = "#### Revision Block — v1.1.65 (Tracked Changes)"
i = t.find(anchor)
assert i >= 0, "PAD v1.1.65 block not found"
t = t[:i] + V109_PAD + t[i:]
open("Project_Architecture_Document.md", "w", encoding="utf-8").write(t)
print("aligned Project_Architecture_Document.md (v1.1.66 block inserted)")

# ---------------- D6: probe README ----------------
V109_PROBE_SECTION = (
    "### The v109 cycle (Session 144) — the v103-lineage derivation\n\n"
    "- `derive-v109-series.py` (persisted) — the v109 series derived from the\n"
    "  v103 lineage: vlm-shots-v109.sh + clone-vlmshots-v109.sh +\n"
    "  vlm-compare-v109.mjs + arbit-v109.sh; the generic swaps + the FIVE\n"
    "  exact-fragment history corrections (last-re-shot v97->v103, SIXTH-\n"
    "  era SEVENTH->EIGHTH, the re-run bracket extension\n"
    "  v91->v97->v103->v109, the later-pairs list [savings v98...v102 ->\n"
    "  v104...v108] as TWO single-line halves) — 5/5 on the FIRST run (11\n"
    "  hit-checks), zero residuals, line-count-preserving on all four\n"
    "  (56/48/49/284).\n"
    "- `build-twohalf-v109.py` — the two-half builder (CENSUS_JS 193\n"
    "  lines, md5 b55dcd29 — the v97/v103 census block VERBATIM, the\n"
    "  block itself version-free but for the v70b finder provenance):\n"
    "  ref-arbit-v109.sh + clone-arbit-v109.sh, the census JS\n"
    "  byte-identical across the halves.\n"
    "- `derive-standing-v109.py` — the 103rd standing pair\n"
    "  (ref-standing-v103.sh + standing-checks-v103.sh) from the v102\n"
    "  pair, the THREE token families (the ordinal token's suffix flip\n"
    "  102nd->103rd), normalize-back verified version-bump-only.\n"
    "- `base44-fab-arbit-v109.sh` — the ONE-SHOT both-sides arbitration\n"
    "  for the cycle's FAB flag (fabCount 0 + bodyHasBase44 false on\n"
    "  BOTH sides at 1280 on /expenses — the v97/v103/v108 standing\n"
    "  disproof form, run because a FAB flag WAS raised).\n"
    "- `header-arbit-v109.sh` — the ONE-SHOT both-sides census of the\n"
    "  ITEMS VIEWS' PAGE-HEADER ROW INTERIOR family (the v109 pin's own\n"
    "  axes measured byte-identical on both sides on BOTH variants before\n"
    "  the pin): the row {flex/space-between/center/gap 16/mb 32/h 60} +\n"
    "  the left block {flex/center/gap 12/h 60/childCount 2} + the chip\n"
    "  {48x48/12px/the per-type gradient} + the icon {24x24/white} + the\n"
    "  h1 {30px/700/36px/forestDark} + the subtitle {16px/400/gray} + the\n"
    "  Add button {147x36 income/155x36 expenses, 6px, 8px 16px, 14px/500,\n"
    "  white, the per-type gradient} + the plus {16x16/mr 8px}.\n"
    "- `crop-07-v109.mjs` + `vlm-read-07-v109.mjs` — the screenshot\n"
    "  arbitration pair for the one fresh-seed delta: the band-crop + the\n"
    "  VLM read ('10/23/2026' -> '10/24/2026' — the modal's default-date\n"
    "  field rolling with the UTC day).\n\n"
    "### D6 — the operational lessons this cycle (v109)\n\n"
    "- THE SINGLE-AXIS CASCADE RULE (a mutation-selection note): when the\n"
    "  pin's family lives in a SHARED component (items-view.tsx serves\n"
    "  income + expenses + savings), the mutation target must be an axis NO\n"
    "  OTHER SPEC asserts in ANY variant — the left block's gap-3 (never\n"
    "  asserted anywhere) passes; the row's own gap-4/mb-8 would cascade\n"
    "  into the v65 savings + v52 mobile pins (multi-spec failures). The\n"
    "  mutation-selection discipline extends from single-axis to\n"
    "  single-axis AND single-spec-by-construction.\n"
    "- THE DATE-ROLL ARBITRATION (a screenshot note): a single-band\n"
    "  maxD-200+ pixel delta in a regenerated set decomposes via the\n"
    "  band-crop + VLM read — the 07-add-item-modal's one 22-row band read\n"
    "  as '10/23/2026' -> '10/24/2026' (the default-date field rolling\n"
    "  with the UTC day) — the documented fresh-seed date-roll class (the\n"
    "  v104/v105 precedent), the updated set committed.\n"
    "- THE VERDICT-VARIATION FORM (a VLM note): the pair's verdict may\n"
    "  vary across re-runs within the documented class set — v103 read\n"
    "  BOTH DIFFERENT, v109 read INCOME IDENTICAL + EXPENSES DIFFERENT; the\n"
    "  income side's documented flags were all-data classes, so the\n"
    "  IDENTICAL verdict is the cleaner outcome on the same chrome (the\n"
    "  v105 LOGIN-IDENTICAL precedent) — the CLASSES, not the verdict\n"
    "  string, are the contract.\n\n"
    "The v110 queue (suggestions — verify against the rotation ledger before\n"
    "executing): (1) the re-run cadence rotates to the next-oldest candidate\n"
    "after the v103-era ITEMS pair (the v104-era SAVINGS pair — the SAVINGS\n"
    "view at desktop 1280x800 FULL-PAGE, the v58-era savings pair's surface,\n"
    "last re-shot v104 — now the oldest remaining [v104 < v105 < v106 <\n"
    "v107 < v108 < v109]; the pair's EIGHTH re-run bracket [v58 -> v65 ->\n"
    "v74 -> v80 -> v86 -> v92 -> v98 -> v104 -> v110] to be verified against\n"
    "vlm-shots-v104.sh's own header before the derivation), (2) the axe-core\n"
    "watch at its next re-check point (only a 5.x wrapper changes the\n"
    "calculus), (3) the deferred reference-write censuses (unchanged — out\n"
    "of bounds under the v46 read-only rule).\n"
)
t = open("scripts/parity-probes/README.md", encoding="utf-8").read()
i = t.find("The v109 queue (suggestions")
assert i >= 0, "v109 queue anchor not found"
t = t[:i] + V109_PROBE_SECTION
open("scripts/parity-probes/README.md", "w", encoding="utf-8").write(t)
print("aligned scripts/parity-probes/README.md (v109 section + v110 queue)")
print("D4-D6 aligned")
