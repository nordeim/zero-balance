#!/usr/bin/env python3
"""Align the docs for the v132 cycle (Session 167).

D1  AGENTS.md     — the v132 paragraph appended after the v131 paragraph
                    (the v131 paragraph is the file's last line; the anchor
                    carries the v131-unique dev-shots-derivation tokens)
D2  CLAUDE.md     — the E2E count 334 -> 335 + the v132 clause
D3  README.md     — the count strings 334 -> 335 (two places) + the v132
                    plan row appended after the v131 row (the anchor
                    disambiguated by the v131-unique date-class tokens)
D4  SKILL.md      — project_state 334 -> 335 + the Session 167 row appended
                    after the Session 166 row
D5  PAD           — the [UI] v1.1.89 revision block (inserted newest-first,
                    BEFORE the v1.1.88 block)
D6  probe README  — the v132 section + the v133 queue   [align-probereadme-v132.py]
D7  session_320.md + the worklog Session 167 entry (separate steps)

D0 checked clean: every insert anchor below verified 1-hit before any write
(the AGENTS anchor by the v131-unique dev-shots tokens; the README anchor
by the v131-unique date-class tokens; the CLAUDE anchor by the v131-unique
post-restore-regression tokens; the SKILL anchor by the S166-unique
state-line tokens).
"""
import sys

def replace1(path, old, new):
    t = open(path, encoding="utf-8").read()
    n = t.count(old)
    if n != 1:
        print(f"AMBIGUOUS/MISS in {path}: {n} hits for {old[:60]!r}")
        return False
    open(path, "w", encoding="utf-8").write(t.replace(old, new))
    return True

def insert_after(path, anchor, content, marker):
    t = open(path, encoding="utf-8").read()
    if marker in t:
        print(f"ALREADY APPLIED: {path} — {marker[:40]!r}")
        return True
    n = t.count(anchor)
    if n != 1:
        print(f"AMBIGUOUS/MISS in {path}: {n} hits for anchor {anchor[:60]!r}")
        return False
    open(path, "w", encoding="utf-8").write(t.replace(anchor, anchor + content))
    return True

def insert_before(path, anchor, content, marker):
    t = open(path, encoding="utf-8").read()
    if marker in t:
        print(f"ALREADY APPLIED: {path} — {marker[:40]!r}")
        return True
    n = t.count(anchor)
    if n != 1:
        print(f"AMBIGUOUS/MISS in {path}: {n} hits for anchor {anchor[:60]!r}")
        return False
    open(path, "w", encoding="utf-8").write(t.replace(anchor, content + anchor))
    return True

ok = True

# ---------------- D1: AGENTS.md ----------------
V132_AGENTS = """

Reference surfaces pinned by the v132 iteration (`docs/remediation-plan-v132.md`) — **the re-run cycle's next-oldest candidate (the v126-era MOBILE-TWINS pair — BOTH mobile 390x844 full-page twins: (1) the /NETWORTH view (the v63-era pair's surface) + (2) the DASHBOARD (the v62-era mobile twin's surface), the pair's ELEVENTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132], the FIFTY-FIFTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly: the TENTH ordinal stated in vlm-shots-v126.sh's own header on its 11-entry bracket [v62/v63 the original pair, one entry] → v132 = the ELEVENTH, no prose/header conflict)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only canary prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds — one node_modules/axe-core entry verified live) + the npm-audit watch at its twenty-third re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 126th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 126th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). **The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs (the PIN-ONLY form, the v128/v129/v130/v131 class — the FOURTH consecutive PIN-ONLY cycle)** (the RE-PROVISIONED workspace — the v127/v129/v130/v131 cycle's own form: the fresh clone from main @ ff17745, the v108 lesson end-to-end [npm ci in the foreground, the zod extraction intact 840/840, BOTH chromium pairs — the fresh cache held only the OLD 1200 pair, the 1243 pair installed, the .env + db/ provisioned, db:push + db:seed, the seedcheck exact before any gate]; lint · typecheck · 108 unit · build [robots + sitemap prerendered] · 334 e2e zero flakes [337 executions in 4 chunks = 333 spec + 1 setup] · 35/35 smoke; the production-seam audit clean + the v131 pin verified in place). The probe series derived from the v126 lineage (derive-v132-series.py — FOUR explicit session-token families [refvlm/clonevlm + refarbit/clonearbit arbit — the arbit tokens carry '126' without the 'v' prefix] + FIVE history-correction fragments [the plan pointer, the era marker + the oldest-remaining list, the ordinal TENTH→ELEVENTH + the bracket extension, the verdicts window, the arbit re-proves chain + the census-axes era], zero residual, line counts preserved 61/48/69/220) + the TWO-block two-half contract verified three-way (verify-twohalf-v132.py — NW_CENSUS 42 lines md5 82cf8a43 + DASH_CENSUS 87 lines md5 85e4ec7e, the v102/v108/v114/v120/v126 lineage values VERBATIM; the builder's embedded clone_login stale `clonearbit120` session token bumped to `clonearbit132` — the v121 stale-session-fix precedent) + the comparator derived (the /tmp/vlm126→/tmp/vlm132 explicit log-path swap + the provenance citations re-pointed at the v126 measurement; the v126 derivation's latent 'textax' residual-loop typo fixed to the correct text[max(0, …)] slice form). **The VLM verdict — BOTH PAIRS DIFFERENT ×2, THE CONSISTENT FORM** (the pair's DOCUMENTED VERDICT CLASS — the same verdict family as the v84/v90/v96/v102/v108/v114/v120/v126 re-runs; every flag in the documented classes, arbitration-free: the tiles side-by-side-vs-stacked + the page-length the v41 MOBILE-SUPERSET/seed-count classes, the trend-icon opacity the PERCEPTION-ARTIFACT class [the census axis trendIcon 32×32 byte-identical], the "Edit with Base44" tooltip the PLATFORM-CHROME class, the hero allocation % + balance + the donut proportions + the stat amounts the PCT/seed-data classes, the subtitle wrap the RANGE-WALK line-bucketing class). The both-sides census compared AXIS-BY-AXIS by the persisted compare-v132-census.py (**55 axes: 37 identical + 18 documented-class deltas, ZERO new** — REPRODUCING the v126 census values EXACTLY: the same 55/37/18 split, zero drift on every axis). **THE PIN — the NETWORTH ASSET-CARD TYPE BADGE's OWN-HOVER LADDER at 390 (+1 e2e = 335; PIN-ONLY — src/ zero changes)**: the candidate survey (the networth badge family's coverage map — the v29 G1 pins hold the class token + the at-rest bg/color, the v127 pin the ITEM-CARD badge's hover path [a different file, a different at-rest family], the v130 pin the same card's kebab; the hovered tint held by NO spec on THIS file at ANY viewport; a live survey probe finding the reference's badge is a Badge-base DIV carrying the SAME chrome family [at-rest rgb(243,244,246) / color rgb(55,65,81) / radius 6px / h 22 / 0.15s — the v28 G1 family]); the both-sides one-shot census badgehover-arbit-v132.sh (the v127 badgehover form's own shape — the TAG-AGNOSTIC finders [the reference's DIV vs the clone's SPAN], the "Bank Account" SAME-LABEL target [the w/h axes byte-comparable], the (5,5)-parked ladder, the live-read center, READ-ONLY per the v46 rule — the badge's only behavior is the tint, no click path exists on either site) measured the ladder **BYTE-IDENTICAL both sides** — at-rest {bg rgb(243,244,246)} → OWN-HOVERED {hoverMatch true, bg rgba(245,245,245,0.8)} → restored, the color rgb(55,65,81)/w 115/h 22/transitionDuration 0.15s identical, the transitionProperty list the v95 documented class — **no gap, no repair**; the pin (append-pin-v132.py — the first asset card's badge at 390×844, the V94-COLLISION-safe axis set [the end-states alone, the transition metadata + the label-dependent w/h deliberately not pinned]) GREEN on the first run; **THE PIN-SANITY MUTATION — the line-76-scoped class-token suffix-extension form (zb-badge-hover → zb-badge-hoverx, the asset twin alone; the liability twin at :186 untouched by line-scoping; the regex partial-match quirk keeps networth.spec.ts:196's toHaveClass(/zb-badge-hover/) green — the mutated class attribute still contains the substring; the v127 items pin different-file immune)**: the SOLE FAILURE verified live — 1 failed [the pin] + 7 passed in the family grep + the v127 pin 2 passed, the deep-equality diff EXACTLY the predicted hovered-bg line [rgba(245,245,245,0.8) → rgb(243,244,246); hoverMatch true preserved, the at-rest + restored rungs UNAFFECTED]; restored (git diff src/ = 0 lines) + the FULL REBUILD + the 158/158 post-restore regression (networth 38 + items 49 + dashboard 50 + calculator 20 — the v130/v131 pins' different-file immunity verified live). The ship chain 335 e2e zero flakes (93+89+74+82 = 338 executions = 335 unique); 35/35 smoke; **the screenshots 16/16 byte-identical (the SAME-UTC-DAY law — the seed ran on the same UTC day as the v131 seed, the relative isoDate(-N) dates unchanged, no date-class refresh this cycle)**; the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the dev-shots scripts derived v131→v132 with the version-swap-only verification)."""
AGENTS_TAIL = "the dev-shots scripts derived v130→v131 with the version-swap-only verification)."
ok = ok and insert_after("AGENTS.md", AGENTS_TAIL, V132_AGENTS,
             "Reference surfaces pinned by the v132 iteration")

# ---------------- D2: CLAUDE.md ----------------
ok = ok and replace1("CLAUDE.md",
    "- **E2E (Playwright, 334)**:",
    "- **E2E (Playwright, 335)**:")
ok = ok and insert_after("CLAUDE.md",
    "the post-restore regression 157/157)",
    "; the v132 pin — the NETWORTH asset-card type badge's own-hover ladder at 390 (PIN-ONLY — src/ zero changes: the both-sides census badgehover-arbit-v132.sh measured the ladder byte-identical on the same-label 'Bank Account' target — at-rest {bg rgb(243,244,246)} → own-hovered {bg rgba(245,245,245,0.8)} → restored; the reference's Badge-base DIV carries the same chrome family — a both-sides parity axis; the line-76-scoped class-token suffix mutation sole-failure verified live [1 failed + 7 passed in the family grep, the v127 pin different-file immune]; the post-restore regression 158/158)",
    "the v132 pin — the NETWORTH asset-card type badge's own-hover ladder")

# ---------------- D3: README.md ----------------
ok = ok and replace1("README.md",
    "│   └── 📂 e2e/                    # Playwright specs (334 tests) + global setup",
    "│   └── 📂 e2e/                    # Playwright specs (335 tests) + global setup")
ok = ok and replace1("README.md",
    "npm run test:e2e    # Playwright e2e (334 tests) — needs `npm run build` first",
    "npm run test:e2e    # Playwright e2e (335 tests) — needs `npm run build` first")
V132_ROW = "\n| [`docs/remediation-plan-v132.md`](docs/remediation-plan-v132.md) | **The re-run cycle's next-oldest candidate (the v126-era MOBILE-TWINS pair's ELEVENTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132] — the /networth view + the DASHBOARD, both FULL-PAGE at mobile 390x844; the FIFTY-FIFTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly, the TENTH ordinal stated in vlm-shots-v126.sh's own header)** + the axe watch (NO DRIFT — 4.14.0 holds) + the npm-audit watch (0 vulnerabilities, twenty-third re-check) + the 126th standing checks (ALL GREEN — the mobile menu the 126th consecutive pass) + the VLM pair **BOTH PAIRS DIFFERENT ×2 — the consistent form, the pair's documented verdict class** (every flag in the documented classes, arbitration-free) + the census 55 axes — 37 identical + 18 documented, ZERO new (the v126 values reproduced EXACTLY) + **the networth badge own-hover ladder pin at 390 (+1 e2e = 335; PIN-ONLY — the both-sides same-label census measured the ladder byte-identical, no repair; the line-76-scoped class-token suffix mutation sole-failure verified live)** + the screenshots 16/16 byte-identical (the same-UTC-day law — no date-class refresh this cycle). |"
README_ANCHOR = "the changed set exactly the date-bearing surfaces). |"
ok = ok and insert_after("README.md", README_ANCHOR, V132_ROW,
             "remediation-plan-v132.md")

# ---------------- D4: SKILL.md ----------------
ok = ok and replace1("zero-balance_SKILL.md",
    "project_state: 108 unit tests / 334 e2e tests / 35 smoke steps — all green",
    "project_state: 108 unit tests / 335 e2e tests / 35 smoke steps — all green")
S167_ROW = "\n| 2026-10-29 | Session 167 — parity iteration v132 (`docs/remediation-plan-v132.md`) | **The re-run cycle's next-oldest candidate (the v126-era MOBILE-TWINS pair's ELEVENTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132] — the /networth view + the DASHBOARD, both FULL-PAGE at mobile 390x844; the FIFTY-FIFTH consecutive queue/ledger agreement)** + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — twenty-third re-check) + the 126th standing checks (ALL GREEN — the reference's four bugs live, the mobile menu the 126th consecutive pass, zero overflow at 390) + the VLM pair **BOTH PAIRS DIFFERENT ×2 — the consistent form, the pair's documented verdict class** (every flag in the documented classes, arbitration-free: the v41 mobile-superset/seed-count tiles + page-length, the perception-artifact trend icon, the platform-chrome Base44 tooltip, the pct/seed-data classes, the range-walk subtitle bucketing) + the two-half census (55 axes — 37 identical + 18 documented, ZERO new — the v126 values reproduced EXACTLY, the TWO-block md5 82cf8a43/85e4ec7e lineage verified three-way; the builder's stale clonearbit120 session token bumped to clonearbit132) + **the networth asset-card badge own-hover ladder pin at 390 (PIN-ONLY — src/ zero changes: the candidate survey found the hovered tint held by no spec on this file at any viewport; the both-sides census badgehover-arbit-v132.sh measured the ladder byte-identical on the same-label target [at-rest {bg rgb(243,244,246)} → own-hovered {bg rgba(245,245,245,0.8), hoverMatch true} → restored; the w/h 115×22 identical]; the line-76-scoped class-token suffix mutation sole-failure verified live — 1 failed + 7 passed in the family grep, the v127 pin different-file immune, the diff exactly the predicted hovered-bg line; the post-restore regression 158/158; +1 e2e = 335)** + the ship chain fully green (335 e2e zero flakes [338 executions], 35/35 smoke, the screenshots 16/16 byte-identical [the same-UTC-day law], the dev evidence 4/4 + VLM-verified) |** 108/335/35 green — the workspace the RE-PROVISIONED class (the resource discipline between the halves) |"
SKILL_ANCHOR = "|** 108/334/35 green — the workspace the RE-PROVISIONED class (the resource discipline between the halves) |"
ok = ok and insert_after("zero-balance_SKILL.md", SKILL_ANCHOR, S167_ROW,
             "Session 167 — parity iteration v132")

# ---------------- D5: PAD ----------------
PAD_V189 = """#### Revision Block — v1.1.89 (Tracked Changes)
- `[UI]` v1.1.89 (2026-10-29) — the v132 parity iteration (**PIN-ONLY — src/ zero changes** + one e2e pin; no dependency change): the counts 108 unit / **335 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v126-era MOBILE-TWINS pair's ELEVENTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132] — the /networth view + the DASHBOARD, both FULL-PAGE at mobile 390x844; the FIFTY-FIFTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly)**; the baseline fully green on the first chain (the RE-PROVISIONED workspace — the fresh-clone class, the v108 lesson end-to-end: npm ci, zod 840/840, both chromium pairs, .env + db/ provisioned; the resource discipline between the halves); the VLM pair **BOTH PAIRS DIFFERENT ×2 — the consistent form, the pair's documented verdict class** (every flag in the documented classes, arbitration-free); the two-half census (the TWO-block v126 lineage, md5 82cf8a43/85e4ec7e verified three-way; the builder's stale clonearbit120 session token bumped to clonearbit132) **55 axes — 37 identical + 18 documented-class deltas, ZERO new** (the v126 values reproduced EXACTLY); **the networth asset-card type badge own-hover ladder pin at 390**: the candidate survey (the networth badge family's coverage map — the hovered tint held by no spec on this file at any viewport; a live survey probe finding the reference's Badge-base DIV carries the same chrome family — the v28 G1 family) + the both-sides census **byte-identical** on the same-label target (no gap, no repair) + the pin (the V94-COLLISION-safe axis set — the end-states alone) + **the line-76-scoped class-token suffix-extension mutation sole-failure verified live — 1 failed + 7 passed in the family grep [the v127 pin different-file immune], the diff exactly the predicted hovered-bg line [rgba(245,245,245,0.8) → rgb(243,244,246)]** + restored + the 158/158 post-restore regression; the ship chain 335 e2e zero flakes (338 executions in 4 chunks) + 35/35 smoke + the screenshots 16/16 byte-identical (the same-UTC-day law — no date-class refresh this cycle) + the dev evidence 4/4 + VLM-verified (the menu proof: /income, docSW 390, navLandmark true).
"""
ok = ok and insert_before("Project_Architecture_Document.md",
    "#### Revision Block — v1.1.88 (Tracked Changes)",
    PAD_V189,
    "Revision Block — v1.1.89")

print("D1-D5:", "ALL ALIGNED" if ok else "FAILED")
sys.exit(0 if ok else 1)
