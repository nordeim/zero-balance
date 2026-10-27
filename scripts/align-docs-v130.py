#!/usr/bin/env python3
"""Align the docs for the v130 cycle (Session 165).

D1  AGENTS.md     — the v130 paragraph appended after the v129 paragraph
                    (the v129 paragraph is the file's last line; the anchor
                    carries the v129-unique dev-shots-derivation tokens)
D2  CLAUDE.md     — the E2E count 332 -> 333 + the v130 clause
D3  README.md     — the count strings 332 -> 333 (two places) + the v130
                    plan row appended after the v129 row (the anchor
                    disambiguated by the v129-unique census tokens)
D4  SKILL.md      — project_state 332 -> 333 + the Session 165 row appended
                    after the Session 164 row
D5  PAD           — the [UI] v1.1.87 revision block (inserted newest-first,
                    BEFORE the v1.1.86 block)
D6  probe README  — the v130 section + the v131 queue   [align-probereadme-v130.py]
D7  session_316.md + the worklog Session 165 entry (separate steps)

D0 checked clean: every insert anchor below verified 1-hit before any write
(the AGENTS anchor by the v129-unique dev-shots tokens; the README anchor
by the v129-unique census tokens; the CLAUDE anchor by the v129-unique
post-repair-census tokens; the SKILL anchor by the S164-unique daemon-reap
tokens).
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
V130_AGENTS = """

Reference surfaces pinned by the v130 iteration (`docs/remediation-plan-v130.md`) — **the re-run cycle's next-oldest candidate (the v124-era NETWORTH + drill-down pair — the /networth view + the DASHBOARD's drill-down EXPANDED state at desktop 1280x800, the v60-era pair's surface family, the pair's ELEVENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130], the FIFTY-THIRD consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly: the TENTH ordinal stated in vlm-shots-v124.sh's own header on its 11-entry bracket [v60 the original] → v130 = the ELEVENTH, no prose/header conflict)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only canary prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds — one node_modules/axe-core entry verified live) + the npm-audit watch at its twenty-first re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 124th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 124th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). **The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs (the PIN-ONLY form, the v128 class)** (the RE-PROVISIONED workspace — the v127/v129 cycle's own form: the fresh clone from main @ f25870b, the v108 lesson end-to-end [npm ci in the foreground, the zod extraction intact 840/840, BOTH chromium pairs — the fresh cache held only the OLD 1200 pair, the 1243 pair installed, the .env + db/ provisioned, db:push + db:seed, the seedcheck exact before any gate]; lint · typecheck · 108 unit · build [robots + sitemap prerendered] · 332 e2e zero flakes [335 executions in 4 chunks = 331 spec + 1 setup] · 35/35 smoke; the production-seam audit clean + the v129 repair verified in place). The probe series derived from the v124 lineage (derive-v130-series.py — FOUR explicit session-token families [refvlm/clonevlm + refar/clonear arbit — the arbit tokens carry '124' without the 'v' prefix] + FOUR history-correction families [the era marker, the bracket extension, the ordinal TENTH→ELEVENTH, the agreement ordinal FORTY-SEVENTH→FIFTY-THIRD, the census provenance], zero residual, line counts preserved 84/71/65/328) + the TWO-block two-half contract verified three-way (verify-twohalf-v130.py — ARBIT_A 90 lines md5 5033e36aaf3ad596b90ba083aaf27a6a + ARBIT_B 111 lines md5 fb8fec538507d17a6f5707fdfae40be8) + the comparator derived (the /tmp/vlm124→/tmp/vlm130 explicit log-path swap + the provenance citations re-pointed at the v124 measurement). **The VLM verdict — the INVERSE-SPLIT verdict-variation family (the v121/v127 precedent form)**: pass 1 **NETWORTH IDENTICAL + DRILL-DOWN DIFFERENT** / pass 2 **NETWORTH DIFFERENT + DRILL-DOWN IDENTICAL** — every flag in both passes in the documented classes: the nav-highlight the v56 SUPERSET class, the avatar letter the USER-IDENTITY class, the "Edit with Base44" FAB claims (BOTH directions across the passes) the PLATFORM-CHROME class **DISPROVEN LIVE by base44-fab-arbit-v130.sh — fabCount 0 + bodyHasBase44 false on BOTH sides, BOTH flagged surfaces [the dashboard / + the networth /networth], 1280, logged-in**, the pass-2 "Budget Pro profile card shifted vertically" claim **a VLM MISREAD, adjudicated live by profilecard-arbit-v130.sh — the block's geometry BYTE-IDENTICAL both sides {x:16, y:724, w:223, h:60, bottomFromVH:16}, the fixed inset-y-0 rail pinning it identically, the docH 895-vs-1411 the SEED-COUNT class [ref 1 asset card vs clone 3 cards in 3 groups]**, the data differences the SEED-DATA classes. The both-sides census compared AXIS-BY-AXIS by the persisted compare-v130-census.py (**73 axes: 67 identical + 6 documented-class deltas, ZERO new** — REPRODUCING the v124 census values EXACTLY: the same 73/67/6 split, zero drift on every axis). **THE PIN — the NETWORTH ASSET-CARD KEBAB-TRIGGER's OWN-HOVER LADDER at 1280 (+1 e2e = 333; PIN-ONLY — src/ zero changes)**: the candidate survey found the reveal family fully held at REST + CARD-hover [v46 F2] + keyboard [v36] + OPEN [v124 — the open state's full box chrome] on the networth file, the v128 pin holding the SAME ladder on the SAVINGS item-card [a different file]; the both-sides one-shot census kebabhover-arbit-v130.sh (the v46 grid finder, the tag-agnostic computed-shape trigger finder, the (5,5)-parked ladder, the live-read center, READ-ONLY per the v46 rule) measured the ladder **BYTE-IDENTICAL both sides** — at-rest {opacity 0, bg transparent, color rgb(10,10,10)} → OWN-HOVERED {opacity 1, bg rgb(245,245,245), color rgb(23,23,23)} → restored, the box chrome 36×36/r6px + transition opacity 0.15s identical — **no gap, no repair; the networth twins already carry the full ghost family**; the pin (append-pin-v130.py — the Share Portfolio card, the V94-COLLISION-safe axis set [the w/h/radius held by the v124 open-state pin, deliberately not re-pinned]) GREEN on the first run; **THE PIN-SANITY MUTATION — the line-82-scoped value-only alpha-modifier form (hover:bg-accent → hover:bg-accent/50, the ASSET twin alone, the liability twin :192 untouched)**: the SOLE FAILURE verified live — 1 failed [the pin] + 37 passed in the full networth file, the deep-equality diff EXACTLY the predicted hovered-bg line [rgb(245,245,245) → the mutated lab(96.5375 0 0 / 0.5) alpha form; cardHover/color/hoverMatch/opacity preserved]; restored (git diff src/ = 0 lines) + the FULL REBUILD + the 107/107 post-restore regression (networth 37 + items 49 + calculator 20 — the v128/v129 pins' different-file immunity verified live). The ship chain 333 e2e zero flakes (91+89+74+82 = 336 executions = 333 unique); 35/35 smoke; **the screenshots 16/16 byte-identical (the pin-only cycle — no src/ surface touched; the same-day law)**; the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the dev-shots scripts derived v129→v130 with the version-swap-only verification)."""
AGENTS_TAIL = "the dev-shots scripts derived v128→v129 with the version-swap-only verification)."
ok = ok and insert_after("AGENTS.md", AGENTS_TAIL, V130_AGENTS,
             "Reference surfaces pinned by the v130 iteration")

# ---------------- D2: CLAUDE.md ----------------
ok = ok and replace1("CLAUDE.md",
    "- **E2E (Playwright, 332)**:",
    "- **E2E (Playwright, 333)**:")
ok = ok and insert_after("CLAUDE.md",
    "the post-repair census: the OWN-HOVERED state byte-identical both sides)",
    "; the v130 pin — the NETWORTH ASSET-CARD KEBAB-TRIGGER's own-hover ladder at 1280 (PIN-ONLY — src/ zero changes: the both-sides census kebabhover-arbit-v130.sh measured the ladder byte-identical — at-rest {opacity 0, transparent, rgb(10,10,10)} → own-hovered {opacity 1, rgb(245,245,245), rgb(23,23,23)} → restored; the networth twins [net-worth-view.tsx:82/192] already carry the full ghost family; the pin holds the V94-COLLISION-safe axis set; the line-82-scoped alpha-modifier mutation sole-failure verified live [1 failed + 37 passed, the diff exactly the predicted hovered-bg line]; the post-restore regression 107/107)",
    "the v130 pin — the NETWORTH ASSET-CARD KEBAB-TRIGGER's own-hover ladder")

# ---------------- D3: README.md ----------------
ok = ok and replace1("README.md",
    "│   └── 📂 e2e/                    # Playwright specs (332 tests) + global setup",
    "│   └── 📂 e2e/                    # Playwright specs (333 tests) + global setup")
ok = ok and replace1("README.md",
    "npm run test:e2e    # Playwright e2e (332 tests) — needs `npm run build` first",
    "npm run test:e2e    # Playwright e2e (333 tests) — needs `npm run build` first")
V130_ROW = "\n| [`docs/remediation-plan-v130.md`](docs/remediation-plan-v130.md) | **The re-run cycle's next-oldest candidate (the v124-era NETWORTH + drill-down pair's ELEVENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130] — the /networth view + the DASHBOARD's drill-down EXPANDED state at desktop 1280x800; the FIFTY-THIRD consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly, the TENTH ordinal stated in vlm-shots-v124.sh's own header)** + the axe watch (NO DRIFT — 4.14.0 holds) + the npm-audit watch (0 vulnerabilities, twenty-first re-check) + the 124th standing checks (ALL GREEN — the mobile menu the 124th consecutive pass) + the VLM pair **the INVERSE-SPLIT verdict-variation family** (pass 1 NETWORTH IDENTICAL + DRILL-DOWN DIFFERENT / pass 2 the flip — the v121/v127 precedent form; every flag in the documented classes; the FAB disproven live on BOTH flagged surfaces both sides; the profile-card claim adjudicated a VLM misread — the geometry byte-identical, the docH the seed-count class) + the census 73 axes — 67 identical + 6 documented, ZERO new (the v124 values reproduced EXACTLY) + **the networth kebab own-hover ladder pin at 1280 (+1 e2e = 333; PIN-ONLY — the both-sides census measured the ladder byte-identical, no repair; the line-82-scoped alpha-modifier mutation sole-failure verified live)** + the screenshots 16/16 byte-identical (the same-day law). |"
README_ANCHOR = "+ the screenshots 16/16 byte-identical (the hover-only repair). |"
ok = ok and insert_after("README.md", README_ANCHOR, V130_ROW,
             "remediation-plan-v130.md")

# ---------------- D4: SKILL.md ----------------
ok = ok and replace1("zero-balance_SKILL.md",
    "project_state: 108 unit tests / 332 e2e tests / 35 smoke steps — all green",
    "project_state: 108 unit tests / 333 e2e tests / 35 smoke steps — all green")
S165_ROW = "\n| 2026-10-28 | Session 165 — parity iteration v130 (`docs/remediation-plan-v130.md`) | **The re-run cycle's next-oldest candidate (the v124-era NETWORTH + drill-down pair's ELEVENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130] — the /networth view + the DASHBOARD's drill-down EXPANDED state at desktop 1280x800; the FIFTY-THIRD consecutive queue/ledger agreement)** + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — twenty-first re-check) + the 124th standing checks (ALL GREEN — the reference's four bugs live, the mobile menu the 124th consecutive pass, zero overflow at 390) + the VLM pair **the INVERSE-SPLIT verdict-variation family** (pass 1 NETWORTH IDENTICAL + DRILL-DOWN DIFFERENT / pass 2 the flip — the v121/v127 precedent form; every flag in the documented classes: the nav-highlight v56 superset, the avatar user-identity, the FAB platform-chrome disproven live on BOTH flagged surfaces both sides, the profile-card claim a VLM misread adjudicated live [the geometry byte-identical, the docH the seed-count class]) + the two-half census (73 axes — 67 identical + 6 documented, ZERO new — the v124 values reproduced EXACTLY, the TWO-block md5 5033e36aaf3ad596b90ba083aaf27a6a/fb8fec538507d17a6f5707fdfae40be8 lineage verified three-way) + **the networth kebab own-hover ladder pin at 1280 (PIN-ONLY — src/ zero changes: the both-sides census kebabhover-arbit-v130.sh measured the ladder byte-identical [at-rest {opacity 0, transparent, rgb(10,10,10)} → own-hovered {opacity 1, rgb(245,245,245), rgb(23,23,23)} → restored; the networth twins already carry the full ghost family]; the V94-COLLISION-safe axis set; the line-82-scoped alpha-modifier mutation sole-failure verified live — 1 failed + 37 passed, the diff exactly the predicted hovered-bg line; the post-restore regression 107/107; +1 e2e = 333)** + the ship chain fully green (333 e2e zero flakes [336 executions], 35/35 smoke, the screenshots 16/16 byte-identical [the same-day law], the dev evidence 4/4 + VLM-verified) |** 108/333/35 green — the workspace the RE-PROVISIONED class (the resource discipline between the halves) |"
SKILL_ANCHOR = "|** 108/332/35 green — the workspace the RE-PROVISIONED class (the daemon-reap discipline between the halves) |"
ok = ok and insert_after("zero-balance_SKILL.md", SKILL_ANCHOR, S165_ROW,
             "Session 165 — parity iteration v130")

# ---------------- D5: PAD ----------------
PAD_V187 = """#### Revision Block — v1.1.87 (Tracked Changes)
- `[UI]` v1.1.87 (2026-10-28) — the v130 parity iteration (**PIN-ONLY — src/ zero changes** + one e2e pin; no dependency change): the counts 108 unit / **333 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v124-era NETWORTH + drill-down pair's ELEVENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130] — the /networth view + the DASHBOARD's drill-down EXPANDED state at desktop 1280x800; the FIFTY-THIRD consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly)**; the baseline fully green on the first chain (the RE-PROVISIONED workspace — the fresh-clone class, the v108 lesson end-to-end: npm ci, zod 840/840, both chromium pairs, .env + db/ provisioned; the resource discipline between the halves); the VLM pair **the INVERSE-SPLIT verdict-variation family** (pass 1 NETWORTH IDENTICAL + DRILL-DOWN DIFFERENT / pass 2 the flip — the v121/v127 precedent form; every flag in the documented classes; the FAB disproven live on BOTH flagged surfaces both sides [fabCount 0 + bodyHasBase44 false, the dashboard + the networth surfaces, 1280, logged-in]; the pass-2 profile-card claim a VLM misread adjudicated live — the block geometry byte-identical {x:16, y:724, 223×60, bottomFromVH 16}, the fixed rail pinning it identically, the docH 895-vs-1411 the seed-count class); the two-half census (the TWO-block v124 lineage, md5 5033e36aaf3ad596b90ba083aaf27a6a/fb8fec538507d17a6f5707fdfae40be8 verified three-way) **73 axes — 67 identical + 6 documented-class deltas, ZERO new** (the v124 values reproduced EXACTLY); **the networth asset-card kebab own-hover ladder pin at 1280**: the candidate survey (the reveal family held at rest + card-hover [v46] + keyboard [v36] + open [v124] on the networth file; the v128 pin the same ladder on the different-file savings item-card) + the both-sides census **byte-identical** (no gap, no repair — the networth twins net-worth-view.tsx:82/192 already carry the full ghost family `hover:bg-accent hover:text-accent-foreground`) + the pin (the V94-COLLISION-safe axis set — the w/h/radius held by the v124 open-state pin) + **the line-82-scoped value-only alpha-modifier mutation sole-failure verified live — 1 failed + 37 passed, the diff exactly the predicted hovered-bg line [rgb(245,245,245) → lab(96.5375 0 0 / 0.5)]** + restored + the 107/107 post-restore regression; the ship chain 333 e2e zero flakes (336 executions in 4 chunks) + 35/35 smoke + the screenshots 16/16 byte-identical (the same-day law) + the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true).
"""
ok = ok and insert_before("Project_Architecture_Document.md",
    "#### Revision Block — v1.1.86 (Tracked Changes)",
    PAD_V187,
    "Revision Block — v1.1.87")

print("D1-D5:", "ALL ALIGNED" if ok else "FAILED")
sys.exit(0 if ok else 1)
