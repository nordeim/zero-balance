#!/usr/bin/env python3
"""D1-D5 docs alignment for the v115 cycle (the persisted alignment-script
precedent — the v114 cycle's align-docs-v114.py form, WITH the
IDEMPOTENT-RUN DUPLICATION TRAP guard: every insert-after edit first checks
the inserted content is ABSENT — the anchor text SURVIVES the insertion, so
a re-run would duplicate; the guard makes the re-run a no-op instead).

D1  AGENTS.md     — the v115 paragraph appended after the v114 paragraph
D2  CLAUDE.md     — the E2E count 317 -> 318 + the v115 clause appended to
                    the E2E bullet's tail (after the v114 clause)
D3  README.md     — the two (317 tests) counts -> 318 + the v115 plan row
                    appended after the v114 row
D4  SKILL.md      — project_state 317 -> 318 + the Session 150 row appended
D5  PAD           — the v1.1.72 revision block inserted before v1.1.71

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
V115_AGENTS = """

Reference surfaces pinned by the v115 iteration (`docs/remediation-plan-v115.md`) — **the re-run cycle's next-oldest candidate (the v109-era ITEMS pair — the ITEMS view [INCOME + EXPENSES] at desktop 1280x800 FULL-PAGE, last re-shot v109; the pair's NINTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115]; the THIRTY-EIGHTH consecutive queue/ledger agreement) + the axe watch (NO DRIFT) + the npm-audit watch (the standing step's sixth cycle: 0 vulnerabilities — the v110 bump holds) + the 109th standing checks + the items md-band state census pin at 800×600 (PIN-ONLY; +1 e2e = 318)**: the verdicts INCOME IDENTICAL + EXPENSES DIFFERENT — the pair's documented verdict split (the same split as v109; the income side's documented flags all-data classes, the IDENTICAL verdict the cleaner outcome on the same chrome — the VLM-verdict variation form, the v105 LOGIN-IDENTICAL precedent) — with every flag DOM-arbitrated to a documented class (the expenses payment chips the v57 DATA-CONDITIONAL class census-proven live [the reference's OWN income card footer childCount 2 with the "Bank Account" chip — the reference RENDERS payment chips when data carries them; its expense items simply ship none]; the badge-arrangement wrap the v57 wrap/classification-VALUE classes [badgeRow h ref 22 vs clone 52, badgeCount 3 vs 4 — the clone's Recurring superset chip + the wrap, the chip chrome byte-identical]; the 'Edit with Base44' FAB the platform-chrome class DISPROVEN live [fabCount 0 + bodyHasBase44 false on BOTH sides at 1280 on /expenses — the base44-fab-arbit-v115.sh standing disproof form]; the avatar the user-identity class; the header stats + card contents the seed-data classes); the two-half census (CENSUS_JS 193 lines, md5 b55dcd29 — the version-free v97/v103/v109 census block carried over VERBATIM; the builder derived via derive-build-twohalf-v115.py with the swap-order rule) compared AXIS-BY-AXIS by the persisted compare-v115-census.py (187 axes: 163 identical + 24 documented-class deltas, ZERO new deltas — the avatar chrome, the grid/card/titleRow/amount/footer/badge0 chrome, the filter card on both variants, the page header row, the docSW 1280 guard all byte-identical) — NO NEW CLONE GAP. The +1 pin (tests/e2e/items.spec.ts): the ITEMS view's MD-BAND STATE at 800×600 — the viewport band (768 ≤ w < 1024) NO spec pins on the items views (the coverage map: pinned ONLY at 390 [v52] and 1280 [v45/v64/v91/v92/v109]; the v42 five-route census sits at 640 — BELOW md, the 1-col state) — the item grid's md state {the 2-col template `232px 232px`, gap 16px} + the page header row's md state {flex/row/space-between/center/gap 16px/mb 32px/h 60/childCount 2} + the filter card's inner grid md state {4 tracks `95.5px ×4`, gap 16px, childCount 3} + the card box at the 2-col width {w 232/pad 20px/radius 12px/border rgb(229,231,227)/bg white} + the docSW 800 guard; the grid childCount (the seed count) + the card h (the v70b wrap consequence) stay UNPINNED — data axes (the v107 position-arithmetic discipline); measured byte-identical both sides via the one-shot mdband-arbit-v115.sh (the finders structural: the card-like-children grid walk [radius 12px + pad 20px], the Add-button→row walk [the v109 finder], the search→card→inner-grid walk); the mutation md:grid-cols-2 → md:grid-cols-1 at items-view.tsx:262 line-scoped (the ONLY `grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3` line in the file; the expenses filter card's own md:grid-cols-2 on line 175 a DIFFERENT line — untouched by the full-string scoping) — only the v115 pin red (44 green) with the failure diff reading as the grid-template family axis ALONE (`232px 232px` → `480px`) after the standalone REBUILD (the 390/640 states structurally immune [grid-cols-1 base]; the ≥1024 states structurally immune [lg:grid-cols-3 overrides md — the v45 1280 pin green under the mutation]; the header row's md:flex-row + the filter card's md:grid-cols-4 separate tokens — untouched); restored (git diff src/ = 0), rebuilt, post-restore 45/45 green. The cycle's derivation lesson: THE POST-SWAP-FRAGMENT RULE (the bracket-extension correction must be written against the POST-generic-swap state [→ v97 → v103 → v115], not the pre-swap form — the generic swap consumes the version token first; the first run's pre-swap fragment missed silently, caught by reading the derived header before proceeding — the v114 derivation's own precedent, now formalized). The baseline chain FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace (the RESET class — the v114 environment did not persist; the repo re-cloned from main @ 735f612; the v108 FRESH-CLONE lesson applied end-to-end: npm ci [run in the foreground — the v114 silent-death lesson] with the zod extraction verified INTACT [840/840, src/v4 present] BEFORE any gate, BOTH v1243 playwright binaries verified DIRECTLY, .env + db push/seed; the seedcheck exact [the env -u DATABASE_URL discipline, the canonical db-seedcheck-v68.cjs]; lint; typecheck; 108 unit; build [robots + sitemap prerendered]; 317 e2e zero flakes [84+77+77+82 = 320 executions = 317 unique — the a11y file kept INSIDE chunk 4]; 35/35 smoke). The ship chain 318 e2e zero flakes (84+78+77+82 = 321 executions = 318 unique); 35/35 smoke; the screenshots 16/16 BYTE-IDENTICAL (the same-day-seed law) + the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the menu open with all 5 links + the brand; the sheet closed post-nav; the dashboard clean — the dev-shots scripts derived v114→v115 with the version-swap-only verification)."""
edit("AGENTS.md", [("the 108th standing checks' data census clean on the FIRST reads (no render-race hit this cycle).", "the 108th standing checks' data census clean on the FIRST reads (no render-race hit this cycle)." + V115_AGENTS)], mode="insert-after")

# ---------------- D2: CLAUDE.md ----------------
V115_CLAUSE = " and the v115 items md-band state census (the ITEMS view at 800×600 — the viewport band [768 ≤ w < 1024] no spec pins on the items views: the 2-col item grid template `232px 232px` + the flex-row header reflow + the 4-track filter grid `95.5px ×4` + the card box at the 2-col width + the docSW 800 guard; the seed-count and wrap-height data axes unpinned per the v107 discipline; measured byte-identical both sides by the one-shot mdband-arbit-v115.sh; the mutation md:grid-cols-2 → md:grid-cols-1 at items-view.tsx:262 line-scoped — the grid-template family axis alone [`232px 232px` → `480px`], the 390/640 and ≥1024 states structurally immune)"
edit("CLAUDE.md", [
    ("- **E2E (Playwright, 317)**:", "- **E2E (Playwright, 318)**:"),
    ("single-axis row.align alone, the cross-axis move touches no vertical box)",
     "single-axis row.align alone, the cross-axis move touches no vertical box)" + V115_CLAUSE),
])

# ---------------- D3: README.md ----------------
edit("README.md", [
    ("e2e/                    # Playwright specs (317 tests) + global setup",
     "e2e/                    # Playwright specs (318 tests) + global setup"),
    ("npm run test:e2e    # Playwright e2e (317 tests) — needs `npm run build` first",
     "npm run test:e2e    # Playwright e2e (318 tests) — needs `npm run build` first"),
])

# ---------------- D4: SKILL.md ----------------
edit("zero-balance_SKILL.md", [
    ("state: 108 unit tests / 317 e2e tests / 35 smoke steps — all green",
     "state: 108 unit tests / 318 e2e tests / 35 smoke steps — all green"),
])

sys.exit(0 if ok else 1)
