#!/usr/bin/env python3
"""D0-D5 docs alignment for the v120 cycle (the persisted alignment-script
precedent — the v119 cycle's align-docs-v119.py form, WITH the
IDEMPOTENT-RUN DUPLICATION TRAP guard on every insert-after edit).

D0  AGENTS.md     — the v119-RESIDUAL DUPLICATION FIX (the v119 paragraph's
                    tail carries the workspace-class sentence 3 EXTRA times
                    — a latent v119-cycle defect; the duplicates removed,
                    the paragraph restored to its script-authored ending)
D1  AGENTS.md     — the v120 paragraph appended after the FIXED v119 tail
D2  CLAUDE.md     — the E2E count 322 -> 323 + the v120 clause appended to
                    the v119 clause's tail
D3  README.md     — the two (322 tests) counts -> 323 + the v120 plan row
                    appended after the v119 row
D4  SKILL.md      — project_state 322 -> 323 + the Session 155 row appended
D5  PAD           — the v1.1.77 revision block inserted before v1.1.76

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

# ---------------- D0: AGENTS.md — the v119-residual duplication fix ----------------
DUP = " The workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end (npm ci in the foreground + zod 840/840 + BOTH v1243 binaries DIRECT)."
t = open("AGENTS.md", encoding="utf-8").read()
dup_count = t.count(DUP)
if dup_count == 0:
    print("D0: no duplication found (already fixed) — skipped")
elif dup_count != 3:
    print(f"AMBIGUOUS: expected the 3 duplicate sentences, found {dup_count}")
    ok = False
else:
    # remove ALL 3 duplicates, then re-append exactly ONE (the v119
    # paragraph's authored ending carries the workspace-class note once —
    # verified against align-docs-v119.py's own V119_AGENTS content: the
    # script's block ends at 'and corrected).' and the FILE's paragraph =
    # the script's content + 3 copies; the authored form carries NO copy)
    t = t.replace(DUP, "")
    open("AGENTS.md", "w", encoding="utf-8").write(t)
    print(f"aligned AGENTS.md: removed the {dup_count} duplicated workspace-class sentences (the v119-residual defect)")

# ---------------- D1: AGENTS.md ----------------
V120_AGENTS = """

Reference surfaces pinned by the v120 iteration (`docs/remediation-plan-v120.md`) — **the re-run cycle's next-oldest candidate (the v114-era MOBILE TWINS pair — BOTH mobile 390×844 full-page twins: (1) the /NETWORTH view (the v63-era pair's surface) and (2) the DASHBOARD (the v62-era mobile twin's surface), the pair's NINTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120], the FORTY-THIRD consecutive queue/ledger agreement — the v114 header's own EIGHTH ordinal CONSISTENT with its 9-entry bracket [v62/v63 the original pair], no off-by-one this lineage)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only the canary 4.14.0-canary.6b52b84 prerelease beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds; the engine-contract pin green) + the npm-audit watch at its eleventh re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 114th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 114th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). **The verdict BOTH PAIRS DIFFERENT — the pair's documented verdict class (the same verdict family as the v84/v90/v96/v102/v108/v114 re-runs)** — every flag DOM-arbitrated: the NETWORTH stat-tiles stacking + card height + every width consequence the v41 mobile-superset class (census-confirmed: statGrid.cols 2-col-vs-1-col, tiles 176-vs-294, card 432×333-vs-358×421, medallion clipsViewport true-vs-false); the trend-icon circle the PERCEPTION-ARTIFACT class (the census axis trendIcon 32×32 BYTE-IDENTICAL both sides + the medallion 64×64 identical — the VLM's own contradictory descriptions across the two passes the disproof); the card grouping/figures the SEED-DATA classes; the Base44 overlay the PLATFORM-CHROME class DISPROVEN LIVE at BOTH flagged surfaces (base44-fab-arbit-v120.sh: fabCount 0 + bodyHasBase44 false on the reference at /networth AND / + on the clone at both — the overlay lives in the reference's platform iframe chrome); the progress bar/donut/labels the SEED-DATA classes; the subtitle wrap the RANGE-WALK line bucketing (the DASH width-guard class's documented consequence: the ref's 363px-vs-clone's 358px content width buckets the same text differently; the line TOPS identical 123/147, the computed chrome identical). The both-sides census (NW_CENSUS 42 lines md5 82cf8a43 + DASH_CENSUS 87 lines md5 85e4ec7e — the v102/v108/v114 census blocks VERBATIM, built two-half by build-twohalf-v120.py with the STALE clonearbit108 SESSION TOKEN FIXED to clonearbit120 — the v114 builder's clone_login carried the v108 token unbumped) compared AXIS-BY-AXIS by the persisted compare-v120-census.py (**55 axes: 37 identical + 18 documented-class deltas, ZERO new** — the v41 mobile-superset family [docSW 464/390, card.w/h/right, statGrid.cols/w, tiles w, medallion.right/clipsViewport]; the DASH width-guard family [docSW 395/390, subtitle.rect.w/blockW, breakdownCard.rect.w, the children w] + the Range-walk line texts) — reproducing the v114 census values EXACTLY (the same 55/37/18 split), zero drift on every axis. **THE PIN — the /networth LIABILITY-CARD census at 390 (the never-pinned family, PIN-ONLY — the FAMILY-CONSISTENCY form)**: the twins' own surfaces among the most-pinned in the codebase (the /networth: v108/v69/v41/v63/v84/v90/v96/v50/v53/v102/v46/v47; the dashboard: v114/v62/v50/v78/v44-F2a/v51-F2/F4/F5/v49), the rejected candidates documented with the collision evidence (the section-row/facts-row/spending-header 390 twins — the v94/v106/v101 1280 collisions, the v114 rejections standing; the 640-band form — dashboard-view carries ZERO sm: variants, the 640 rendering = the 390 rendering for every family, any 640 pin cascades; the empty-state — the clone seeds 2 liabilities), the candidate the /networth view's LIABILITY CARD family — NEVER pinned at ANY viewport (only the v29 G1 badge family-consistency pin + the interest-line TEXT existence + the group headers + the Add Liability gradient; the ASSET twin fully pinned v46/v47/v106). The FAMILY-CONSISTENCY form (the v29 G1 precedent): the reference's own liability data is EMPTY (0 liabilities — no cards to measure; the v46 read-only rule forbids writing reference data), the chrome family = the AssetCard's pinned contract BY CONSTRUCTION (net-worth-view.tsx:169 the identical class strings to :65; the v46 F1 liability-twin fix's own comment documents the shared mb-4 P + space-y-2 facts stack). The one-shot census (liabcard-arbit-v120.sh — the RADIX TAB-SWITCH LESSON baked in: the tabs activate on pointerdown, the bare el.click() leaves the tab inactive, the full PointerEvent/MouseEvent sequence the fix) measured: the card {358×218 — the asset's pinned 194 + the third facts row's 16 + the space-y-2's 8, THE ARITHMETIC EXACT / radius 12px / pad 20px / border 1px rgb(229,231,227) / shadow rgba(0,0,0,0.04) 0px 2px 8px / bg white / transition all 0.2s — every box axis the v47 contract}, the head row {mb 12 / flex / flex-start / space-between / h 52}, the dot {8×8 / 9999px / the LIABILITY_COLOR orange rgb(224,122,59)}, the h4 {16px/600/forestDark}, the badge {22/12px/600/the v29 G1 family}, the value P {24px/700/THE ORANGE/mb 16px — the v46 F1 liability twin}, the facts {12px/gray/rowGap 8px/rowCount 3 — the liability-ONLY axis: institution + interest + updated vs the asset's 2 rows}, the three rows {flex/center/gap 8px/h 16/icon 12×12}, the valueToFactsGap 16, the docSW 390 (the superset invariant holds on the liabilities panel). The +1 e2e pin (tests/e2e/networth.spec.ts, appended by the persisted append-pin-v120.py): the liability-card census at 390 — the full family + the docSW guard, the finders STRUCTURAL (the card by its class + the /Home Loan/ text; the tab by role), the tab switch by Playwright's locator click (the full pointer sequence — the census lesson encoded in the spec form); the PIN-ONLY form (no red phase — the measured values already hold; the standalone GREEN run + THE PIN-SANITY MUTATION [net-worth-view.tsx:223 the interest row's gap-2→gap-3, LINE-SCOPED — the pin FAILED at rows[1].gap ALONE, 8px→12px, every other axis green; the 6 other same-class lines untouched; restored + the full rebuild + the 36/36 post-restore networth regression]). The ship chain 323 e2e zero flakes (87+80+77+82 = 326 executions = 323 unique); 35/35 smoke; **the screenshots 16/16 byte-IDENTICAL (the same-day-seed law)**; the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true — the dev-shots scripts derived v119→v120 with the version-swap-only verification). The workspace the PERSISTED class (the v119 environment survived between the cycles — node_modules + the db + BOTH v1243 playwright pairs intact; only the git pull needed for the session_291.md handoff; the seedcheck exact before any gate). The v119-RESIDUAL AGENTS.md DUPLICATION FIXED this cycle (the v119 paragraph's tail carried the workspace-class sentence 3 EXTRA times — a latent v119-cycle defect, the duplicates removed in D0)."""
insert_after("AGENTS.md",
             "pattern truncated a11y.spec.ts to y.spec.ts] and corrected).",
             V120_AGENTS,
             "Reference surfaces pinned by the v120 iteration")

# ---------------- D2: CLAUDE.md ----------------
replace1("CLAUDE.md", "- **E2E (Playwright, 322)**:", "- **E2E (Playwright, 323)**:")
V120_CLAUSE = " and the v120 /networth liability-card census at 390 (the never-pinned family — the FAMILY-CONSISTENCY form: the reference's own liability data is EMPTY, the chrome family pinned via the AssetCard's identical class strings [the v29 G1 precedent] — the card 358×218 [the asset's 194 + the third row's 16 + the space-y-2's 8] + the orange dot/value + the 3-row facts stack with the interest row; the Radix tab-switch pointer-sequence lesson encoded in the spec form)"
insert_after("CLAUDE.md",
             "measured BYTE-IDENTICAL on both sides — not even a mechanism axis, the cleanest PIN-ONLY form)",
             V120_CLAUSE,
             "the v120 /networth liability-card census")

# ---------------- D3: README.md ----------------
replace1("README.md",
         "e2e/                    # Playwright specs (322 tests) + global setup",
         "e2e/                    # Playwright specs (323 tests) + global setup")
replace1("README.md",
         "npm run test:e2e    # Playwright e2e (322 tests) — needs `npm run build` first",
         "npm run test:e2e    # Playwright e2e (323 tests) — needs `npm run build` first")
V120_ROW = """
| [`docs/remediation-plan-v120.md`](docs/remediation-plan-v120.md) | **The re-run cycle's next-oldest candidate (the v114-era MOBILE TWINS pair's NINTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120] — BOTH mobile 390×844 full-page twins: (1) the /NETWORTH view (the v63-era pair's surface) + (2) the DASHBOARD (the v62-era mobile twin's surface), last re-shot v114 — now the oldest remaining [v114 < v115 < v116 < v117 < v118 < v119]; the FORTY-THIRD consecutive queue/ledger agreement — the surfaces verified against vlm-shots-v114.sh's own header, the EIGHTH ordinal CONSISTENT with the 9-entry bracket, no off-by-one this lineage) + the axe watch (NO DRIFT) + the npm-audit watch (the standing step's eleventh cycle: 0 vulnerabilities — the v110 bump holds) + the 114th standing checks + the /networth liability-card census pin at 390 (PIN-ONLY — +1 e2e = 323)**. **The verdict BOTH PAIRS DIFFERENT — the pair's documented verdict class (the same family as v84/v90/v96/v102/v108/v114)** — every flag DOM-arbitrated: the stat-tiles stacking the v41 mobile-superset class; the trend-icon circle the perception-artifact class (the census 32×32 byte-identical + the VLM's contradictory descriptions across the passes); the figures the seed-data classes; the Base44 overlay the platform-chrome class DISPROVEN LIVE at BOTH surfaces (fabCount 0 + bodyHasBase44 false both sides); the subtitle wrap the Range-walk line bucketing (the DASH width-guard class's documented consequence). The two-half census (NW_CENSUS 42 lines md5 82cf8a43 + DASH_CENSUS 87 lines md5 85e4ec7e — the stale clonearbit108 session token fixed to clonearbit120 in the builder lineage) compared AXIS-BY-AXIS by the persisted compare-v120-census.py (**55 axes: 37 identical + 18 documented-class deltas, ZERO new** — the v114 values reproduced EXACTLY [the same 55/37/18 split]). **THE PIN — the /networth LIABILITY-CARD census at 390 (PIN-ONLY, zero production-code changes — the FAMILY-CONSISTENCY form)**: the twins' own surfaces fully pinned (the rejected candidates documented with the collision evidence — the v94/v106/v101 1280 collisions + the 640-band viewport-invariant rejection); the candidate the /networth view's LIABILITY CARD family — never pinned at ANY viewport (only the v29 G1 badge + the interest-line text existence); the reference's own liability data EMPTY (the v46 read-only rule) — the chrome family = the AssetCard's pinned contract BY CONSTRUCTION (the identical class strings, the v46 F1 liability-twin fix's own comment); the one-shot census (liabcard-arbit-v120.sh — the Radix pointer-event tab-switch lesson) measured the family: the card {358×218 — the asset's 194 + the third row's 16 + the space-y-2's 8, the arithmetic exact}, the head row, the orange dot, the h4, the badge (the v29 G1 family), the orange value P (24px/700/mb 16), the 3-row facts stack (12px/gray/rowGap 8 — the liability-ONLY axis: institution + interest + updated), the rows' chrome, the valueToFactsGap 16; the +1 pin the family census + the docSW guard (the finders structural; the tab by Playwright's locator click — the full pointer sequence); the PIN-ONLY form (the standalone GREEN + the single-axis mutation sanity [net-worth-view.tsx:223 gap-2→gap-3 line-scoped — the pin failed at rows[1].gap ALONE] + the 36/36 post-restore regression). The ship: 323 e2e zero flakes across the auditable four-chunk split (87+80+77+82 = 326 executions = 323 unique); 35/35 smoke; **the screenshots 16/16 byte-IDENTICAL (the same-day-seed law)**; the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); the workspace the PERSISTED class (the v119 environment survived — only the git pull needed); the v119-residual AGENTS.md duplication fixed (the 3 trailing duplicate sentences removed). |"""
insert_after("README.md",
             "the fresh-workspace discovery (the sandbox workspace-root .env's ABSOLUTE DATABASE_URL preferred by the Prisma CLI over the repo's — the explicit-env-prefix fix on every CLI call). |",
             V120_ROW,
             "remediation-plan-v120.md")

# ---------------- D4: SKILL.md ----------------
replace1("zero-balance_SKILL.md",
         "project_state: 108 unit tests / 322 e2e tests / 35 smoke steps — all green",
         "project_state: 108 unit tests / 323 e2e tests / 35 smoke steps — all green")
V155_ROW = """| 2026-10-25 | Session 155 — parity iteration v120 (`docs/remediation-plan-v120.md`) | **The re-run cycle's next-oldest candidate (the v114-era MOBILE TWINS pair's NINTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120] — BOTH mobile 390×844 full-page twins: the /NETWORTH view + the DASHBOARD; the FORTY-THIRD consecutive queue/ledger agreement; the EIGHTH ordinal consistent with the 9-entry bracket) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's eleventh cycle: 0 vulnerabilities — the v110 bump holds) + the 114th standing checks (ALL GREEN — the mobile menu working the 114th consecutive time) + the /networth liability-card census pin at 390 (PIN-ONLY — +1 e2e = 323)**: **the verdict BOTH PAIRS DIFFERENT — the pair's documented verdict class [the same family as v84 → … → v114]** — every flag DOM-arbitrated (the stat-tiles stacking the v41 mobile-superset class; the trend-icon circle the perception-artifact class — the census 32×32 byte-identical + the VLM's contradictory descriptions; the figures the seed-data classes; the Base44 overlay the platform-chrome class DISPROVEN LIVE at BOTH surfaces; the subtitle wrap the Range-walk line bucketing); the two-half census (NW_CENSUS 42 lines md5 82cf8a43 + DASH_CENSUS 87 lines md5 85e4ec7e — the stale clonearbit108 session token fixed in the builder lineage) compared axis-by-axis by the persisted compare-v120-census.py (**55 axes: 37 identical + 18 documented-class deltas, ZERO new** — the v114 values reproduced EXACTLY); **THE PIN the /networth LIABILITY-CARD census at 390** (the never-pinned family — the FAMILY-CONSISTENCY form [the v29 G1 precedent]: the reference's liability data EMPTY + the v46 read-only rule, the chrome family = the AssetCard's pinned contract BY CONSTRUCTION; the one-shot census liabcard-arbit-v120.sh with the RADIX TAB-SWITCH LESSON [the tabs activate on pointerdown — the bare el.click() leaves the tab inactive] measured the family: the card 358×218 [the asset's 194 + the third row's 16 + the space-y-2's 8 — the arithmetic exact] + the orange dot/value + the badge + the 3-row facts stack with the interest row); the +1 pin the family census + the docSW guard (the finders structural; the tab by the locator click); the PIN-ONLY form (the standalone GREEN + the single-axis mutation sanity [net-worth-view.tsx:223 gap-2→gap-3 line-scoped — the pin failed at rows[1].gap ALONE] + the 36/36 post-restore regression); the ship chain 323 e2e zero flakes (87+80+77+82 = 326 executions), 35/35 smoke, **the screenshots 16/16 byte-IDENTICAL (the same-day-seed law)**, the dev evidence 4/4 byte-identical + VLM-verified; the workspace the PERSISTED class (the v119 environment survived); the v119-residual AGENTS.md duplication fixed |** 108/323/35 green |"""
insert_after("zero-balance_SKILL.md",
             "108/322/35 green |",
             "\n" + V155_ROW.strip(),
             "Session 155 — parity iteration v120")

# ---------------- D5: PAD ----------------
V1177_BLOCK = """#### Revision Block — v1.1.77 (Tracked Changes)
- `[UI]` v1.1.77 (2026-10-25) — the v120 parity iteration (**PIN-ONLY — zero production-code changes** + one e2e pin; no dependency change): the counts 108 unit / **323 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v114-era MOBILE TWINS pair's NINTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120] — BOTH mobile 390×844 full-page twins: (1) the /NETWORTH view (the v63-era pair's surface) + (2) the DASHBOARD (the v62-era mobile twin's surface), last re-shot v114; the FORTY-THIRD consecutive queue/ledger agreement; the EIGHTH ordinal CONSISTENT with the 9-entry bracket — no off-by-one this lineage) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's eleventh cycle: 0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 114th standing checks (ALL GREEN — the mobile menu working the 114th consecutive time; the reference's four bugs all live; the data census clean on the FIRST reads) + the /networth liability-card census pin at 390 (+1 e2e = 323)**: **the verdict BOTH PAIRS DIFFERENT — the pair's documented verdict class (the same family as the v84/v90/v96/v102/v108/v114 re-runs)** — every flag DOM-arbitrated (the stat-tiles stacking the v41 mobile-superset class; the trend-icon circle the perception-artifact class [the census axis byte-identical + the VLM's contradictory descriptions across the passes]; the figures the seed-data classes; the Base44 overlay the platform-chrome class DISPROVEN LIVE at BOTH surfaces [fabCount 0 + bodyHasBase44 false both sides]; the subtitle wrap the Range-walk line bucketing); the two-half census (NW_CENSUS 42 lines md5 82cf8a43 + DASH_CENSUS 87 lines md5 85e4ec7e — the v102/v108/v114 census blocks VERBATIM, the stale clonearbit108 session token fixed to clonearbit120 in the builder lineage) compared AXIS-BY-AXIS by the persisted compare-v120-census.py (**55 axes: 37 identical + 18 documented-class deltas, ZERO new** — the v41 mobile-superset family + the DASH width-guard family + the Range-walk line texts) — reproducing the v114 census values exactly (the same 55/37/18 split). **THE PIN — the /networth LIABILITY-CARD census at 390 (the never-pinned family, PIN-ONLY — the FAMILY-CONSISTENCY form)**: the twins' own surfaces among the most-pinned in the codebase, the rejected candidates documented with the collision evidence (the v94/v106/v101 1280 collisions; the 640-band viewport-invariant rejection [dashboard-view carries ZERO sm: variants]); the candidate the /networth view's LIABILITY CARD family — never pinned at ANY viewport; the reference's own liability data EMPTY (the v46 read-only rule) — the chrome family = the AssetCard's pinned contract BY CONSTRUCTION (net-worth-view.tsx:169 the identical class strings to :65); the one-shot census (liabcard-arbit-v120.sh — the RADIX TAB-SWITCH LESSON: the tabs activate on pointerdown, the bare el.click() leaves the tab inactive, the full pointer-event sequence the fix) measured the family: the card {358×218 — the asset's pinned 194 + the third facts row's 16 + the space-y-2's 8, the arithmetic exact / radius 12px / pad 20px / border / shadow / transition all the v47 contract}, the head row {mb 12 / flex / flex-start / space-between / h 52}, the dot {8×8 / 9999px / the LIABILITY_COLOR orange}, the h4 {16px/600/forestDark}, the badge {the v29 G1 family}, the value P {24px/700/the orange/mb 16px — the v46 F1 liability twin}, the facts {12px/gray/rowGap 8px/rowCount 3 — the liability-ONLY axis}, the three rows {flex/center/gap 8px/h 16/icon 12×12}, the valueToFactsGap 16, the docSW 390. The +1 e2e pin (tests/e2e/networth.spec.ts) the liability-card census at 390 — the full family + the docSW guard, the finders STRUCTURAL, the tab switch by Playwright's locator click (the full pointer sequence — the census lesson encoded in the spec form); the PIN-ONLY form (the standalone GREEN + THE PIN-SANITY MUTATION [net-worth-view.tsx:223 the interest row's gap-2→gap-3, LINE-SCOPED — the pin FAILED at rows[1].gap ALONE, every other axis green; restored + the full rebuild + the 36/36 post-restore regression]). The ship chain 323 e2e zero flakes (87+80+77+82 = 326 executions across four chunks), 35/35 smoke, **the screenshots 16/16 byte-IDENTICAL (the same-day-seed law)**, the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); the workspace the PERSISTED class (the v119 environment survived — only the git pull needed); the v119-residual AGENTS.md duplication fixed (the 3 trailing duplicate workspace-class sentences removed).
"""
t = open("Project_Architecture_Document.md", encoding="utf-8").read()
if "#### Revision Block — v1.1.77" in t:
    print("ALREADY APPLIED: PAD v1.1.77 block — skipped")
elif t.count("#### Revision Block — v1.1.76 (Tracked Changes)") != 1:
    print(f"AMBIGUOUS/MISS: PAD v1.1.76 anchor")
    ok = False
else:
    t = t.replace("#### Revision Block — v1.1.76 (Tracked Changes)",
                  V1177_BLOCK + "#### Revision Block — v1.1.76 (Tracked Changes)", 1)
    open("Project_Architecture_Document.md", "w", encoding="utf-8").write(t)
    print("aligned Project_Architecture_Document.md (the v1.1.77 block)")

sys.exit(0 if ok else 1)
