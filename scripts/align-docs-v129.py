#!/usr/bin/env python3
"""Align the docs for the v129 cycle (Session 164).

D1  AGENTS.md     — the v129 paragraph appended after the v128 paragraph
                    (the v128 paragraph is the file's last line; the anchor
                    carries the v128-unique dev-shots-derivation tokens)
D2  CLAUDE.md     — the E2E count 331 -> 332 + the v129 clause
D3  README.md     — the count strings 331 -> 332 (two places) + the v129
                    plan row appended after the v128 row (the anchor
                    disambiguated by the v128-unique census tokens)
D4  SKILL.md      — project_state 331 -> 332 + the Session 164 row appended
                    after the Session 163 row
D5  PAD           — the [UI] v1.1.86 revision block (inserted newest-first,
                    BEFORE the v1.1.85 block)
D6  probe README  — the v129 section + the v130 queue   [align-probereadme-v129.py]
D7  session_314.md + the worklog Session 164 entry (separate steps)

D0 checked clean: every insert anchor below verified 1-hit before any write
(the AGENTS anchor by the v128-unique dev-shots tokens; the README anchor
by the v128-unique census tokens; the CLAUDE anchor by the v128-unique
49-others/immunity tokens).
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
V129_AGENTS = """

Reference surfaces pinned by the v129 iteration (`docs/remediation-plan-v129.md`) — **the re-run cycle's next-oldest candidate (the v123-era LOGIN + CALCULATOR pair — the LOGIN view + the CALCULATOR dialog at desktop 1280x800, the v59-era pair's surface family, the pair's ELEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129], the FIFTY-SECOND consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly: the TENTH ordinal stated in vlm-shots-v123.sh's own header on its 11-entry bracket [v59 the original] → v129 = the ELEVENTH, no prose/header conflict)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only the canary 4.14.0-canary.6b52b84 prerelease beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds — one node_modules/axe-core entry verified live; the engine-contract pin green) + the npm-audit watch at its twentieth re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 123rd standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 123rd consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). **The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs before F4** (the RE-PROVISIONED workspace — the v127 cycle's own form: the fresh clone from main @ 2cf6429, the v108 lesson end-to-end [npm ci in the foreground, the zod extraction intact 840/840, BOTH chromium pairs — the fresh cache held only the OLD 1200 pair, the 1243 pair installed, the .env + db/ provisioned, db:push + db:seed, the seedcheck exact before any gate]; lint · typecheck · 108 unit · build [robots + sitemap prerendered] · 331 e2e zero flakes [334 executions in 4 chunks] · 35/35 smoke; the production-seam audit clean). **THE v129 RESOURCE DISCIPLINE — the daemon-exhaustion hang, reaped between the halves**: the first clone-arbit run hung (300s, zero output — the accumulated agent-browser sessions [four chrome contexts] + the freshly-booted server exhausting the spawn budget; the v128 lesson's fresh-sandbox form — the pkill between halves [agent-browser-linux-x64 + chrome-155] the fix, the clone half then first-attempt; the discipline now applied BEFORE every clone half). The probe series derived from the v123 lineage (derive-v129-series.py — SIX explicit session-token families [refvlm/clonevlm + refcalc/clonecalc + reflogin/clonelogin arbit — the login pair's tokens carry '123' without the 'v' prefix, missed on the first pass, caught by the residual sweep] + FOUR history-correction families, zero residual, line counts preserved) + the login-shots sub-series derived (derive-loginshots-v129.py — the v105/v111/v117/v123 family; both sides' login censuses byte-equal) + the TWO-block two-half contract verified three-way (verify-twohalf-v129.py — CALC_CENSUS_JS 61 lines md5 e1092d12d06677a4 + LOGIN_CENSUS_JS 36 lines md5 9e5a52d2ab0f2ab9). **The VLM verdict — the v123 consistent form BOTH PASSES: CALCULATOR DIFFERENT / LOGIN IDENTICAL** (every calculator flag in the documented classes: the hover-actions "missing" the POINTER-POSITION/HOVER-STATE screenshot artifact [the census actionsAtRest {opacity 0, btnCount 2} identical both sides; pass 2 self-identifying the mechanism], the "Will update category total" note the SEED-DATA class, the row-height flag the VLM misread [row.h 102 byte-identical]; the login pair IDENTICAL with the reference's own "Edit with Base44" badge the PLATFORM-CHROME class — DISPROVEN LIVE by base44-fab-arbit-v129.sh: fabCount 0 + bodyHasBase44 false on BOTH sides at 1280 /login). The both-sides census compared AXIS-BY-AXIS by the persisted compare-v129-census.py (**106 axes: 97 identical + 9 documented-class deltas, ZERO new** — REPRODUCING the v123 census values EXACTLY: the same 106/97/9 split, zero drift on every axis). **THE REPAIR — the CALCULATOR GHOST-HOVER FAMILY (the first src/ change since v46 — the eighteen-cycle PIN-ONLY run ends)**: the both-sides X-hover census (xhover-arbit-v129.sh — the F4 candidate survey's one-shot measurement, the panel finder DUAL [the reference's dialog is a PLAIN FIXED DIV, no role=dialog — the v99 finder-artifact lesson], the dialog opened via the REAL pointer press, the X found by the v87 geometric form) measured the TINT axis IDENTICAL (the hovered bg rgb(245,245,245) both sides) but **THE COLOR AXIS A NEW CLONE GAP: the reference's X under hover computes rgb(23,23,23) [accent-foreground] while the clone's stayed rgb(10,10,10)** — the reference's ghost-icon family carries `hover:text-accent-foreground`, the clone's calculator X did not; the family scope measured live (rowaction-hover-ref-v129.sh — the reference's ROW ACTIONS carry the full family too: the edit AND the trash both go rgb(23,23,23) under hover, the red trash included); **the repair: `hover:text-accent-foreground` added at calculator-dialog.tsx:138/239/247 (3 insertions, 3 deletions — the v27 G1 precedent's own fix form; the at-rest colors unchanged, every at-rest pin structurally immune; the a11y gate immune [≈15.6:1]; the screenshots unaffected [all at-rest]; the mobile views unaffected [hover:none])**. **THE PIN — the calculator ghost-hover family's own-hover ladders at 1280 (+1 e2e = 332)**: the X ladder (the at-rest rung {transparent bg, rgb(10,10,10), 36×36, radius 6px} → the OWN-HOVERED rung {bg rgb(245,245,245) + color rgb(23,23,23) — THE repaired axes} → the restored rung) + the row-action ladders (the fixture form — the "Contents Insurance" twin state: the row hover's revealed-at-rest colors {edit rgb(10,10,10), trash rgb(220,38,38) — the trash KEEPS its red at rest} → the edit's own-hovered {tint + rgb(23,23,23)} → the trash's own-hovered {tint + rgb(23,23,23)} → the fixture restore through the confirm bar + restoreRent). **THE TDD ORDER — the RED run verified live** (the pin alone failed against the unrepaired build at the X's hovered-color toEqual [rgb(10,10,10) received vs rgb(23,23,23) expected — exactly the predicted axis]) **then the repair + the REBUILD + the GREEN run** (first attempt) **+ the post-repair census re-run (the OWN-HOVERED state byte-identical both sides — the ladders identical, the only surviving delta the documented v3/v4 transitionProperty computed-form class)**. **THE PIN-SANITY MUTATION — the line-138-scoped revert (the X alone)**: the SOLE FAILURE verified live — 1 failed [the pin] + 20 passed in the full calculator file, the diff EXACTLY the predicted hovered-color line (rgb(23,23,23)→rgb(10,10,10); bg + hoverMatch + radius + w/h preserved); restored (git diff src/ = the 3-line repair only) + the REBUILD + the 86/86 post-restore regression (calculator 20 + dialog-buttons 17 + items 49 — the v123/v128 pins' different-file immunity verified live). The ship chain 332 e2e zero flakes (90+69+21+74+82 = 336 executions = 332 unique); 35/35 smoke; **the screenshots 16/16 byte-identical (the hover-only repair — no at-rest surface touched)**; the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the dev-shots scripts derived v128→v129 with the version-swap-only verification)."""
AGENTS_TAIL = "the dev-shots scripts derived v127→v128 with the version-swap-only verification)."
ok = ok and insert_after("AGENTS.md", AGENTS_TAIL, V129_AGENTS,
             "Reference surfaces pinned by the v129 iteration")

# ---------------- D2: CLAUDE.md ----------------
ok = ok and replace1("CLAUDE.md",
    "- **E2E (Playwright, 331)**:",
    "- **E2E (Playwright, 332)**:")
ok = ok and insert_after("CLAUDE.md",
    "the items file's 49 others + the networth immunity file green)",
    "; the v129 pin — the CALCULATOR GHOST-HOVER FAMILY's own-hover ladders at 1280 (THE REPAIR CYCLE — the first src/ change since v46: the both-sides X-hover census measured the tint identical but the COLOR axis a clone gap — the reference's ghost family carries hover:text-accent-foreground [the hovered rgb(23,23,23)], the clone's calculator X + row actions [calculator-dialog.tsx:138/239/247] carried hover:bg-accent alone; the family scope measured live — the reference's edit AND trash both go accent-foreground under hover; the repair: hover:text-accent-foreground added to all three, the v27 G1 precedent's own fix form; the TDD RED run verified live before the repair; the pin holds the X ladder + the row-action ladders + the fixture restore; the line-138-scoped revert mutation sole-failure verified live [1 failed + 20 passed, the diff exactly the predicted hovered-color line]; the post-repair census: the OWN-HOVERED state byte-identical both sides)",
    "the v129 pin — the CALCULATOR GHOST-HOVER FAMILY's own-hover ladders")

# ---------------- D3: README.md ----------------
ok = ok and replace1("README.md",
    "│   └── 📂 e2e/                    # Playwright specs (331 tests) + global setup",
    "│   └── 📂 e2e/                    # Playwright specs (332 tests) + global setup")
ok = ok and replace1("README.md",
    "npm run test:e2e    # Playwright e2e (331 tests) — needs `npm run build` first",
    "npm run test:e2e    # Playwright e2e (332 tests) — needs `npm run build` first")
V129_ROW = "\n| [`docs/remediation-plan-v129.md`](docs/remediation-plan-v129.md) | **The re-run cycle's next-oldest candidate (the v123-era LOGIN + CALCULATOR pair's ELEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129] — the LOGIN view + the CALCULATOR dialog at desktop 1280x800; the FIFTY-SECOND consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly, the TENTH ordinal stated in vlm-shots-v123.sh's own header)** + the axe watch (NO DRIFT — 4.14.0 holds) + the npm-audit watch (0 vulnerabilities, twentieth re-check) + the 123rd standing checks (ALL GREEN — the mobile menu the 123rd consecutive pass) + **THE REPAIR — the CALCULATOR GHOST-HOVER FAMILY (the first src/ change since v46: the both-sides X-hover census measured the hovered-color axis a clone gap — the reference's ghost family carries hover:text-accent-foreground, the clone's X + row actions did not; the repair at calculator-dialog.tsx:138/239/247 — the v27 G1 precedent's own fix form; the TDD RED→GREEN chain verified live)** + the ghost-hover family's own-hover ladders pin at 1280 (+1 e2e = 332; the X ladder + the row-action ladders + the fixture restore; the line-138-scoped revert mutation sole-failure verified live) + the daemon-exhaustion hang reaped between the halves (the v128 lesson's fresh-sandbox form) + the VLM pair the v123 consistent form (CALC DIFFERENT / LOGIN IDENTICAL both passes; every flag in the documented classes; the FAB disproven live) + the census 106 axes — 97 identical + 9 documented, ZERO new (the v123 values reproduced EXACTLY) + the screenshots 16/16 byte-identical (the hover-only repair). |"
README_ANCHOR = "the census 120 axes — 80 identical + 40 documented, ZERO new (the v122 values reproduced EXACTLY) + the screenshots 16/16 byte-identical (the same-day law). |"
ok = ok and insert_after("README.md", README_ANCHOR, V129_ROW,
             "remediation-plan-v129.md")

# ---------------- D4: SKILL.md ----------------
ok = ok and replace1("zero-balance_SKILL.md",
    "project_state: 108 unit tests / 331 e2e tests / 35 smoke steps — all green",
    "project_state: 108 unit tests / 332 e2e tests / 35 smoke steps — all green")
S164_ROW = "\n| 2026-10-27 | Session 164 — parity iteration v129 (`docs/remediation-plan-v129.md`) | **The re-run cycle's next-oldest candidate (the v123-era LOGIN + CALCULATOR pair's ELEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129] — the LOGIN view + the CALCULATOR dialog at desktop 1280x800; the FIFTY-SECOND consecutive queue/ledger agreement)** + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — twentieth re-check) + the 123rd standing checks (ALL GREEN — the reference's four bugs live, the mobile menu the 123rd consecutive pass, zero overflow at 390) + the VLM pair (the v123 consistent form — CALC DIFFERENT / LOGIN IDENTICAL both passes; every flag in the documented classes: the pointer-position/hover-state shot artifact, the seed-data note, the VLM row misread; the FAB disproven live — fabCount 0 + bodyHasBase44 false both sides) + the two-half census (106 axes — 97 identical + 9 documented, ZERO new — the v123 values reproduced EXACTLY, the TWO-block md5 e1092d12d06677a4/9e5a52d2ab0f2ab9 lineage verified three-way) + **THE REPAIR — the CALCULATOR GHOST-HOVER FAMILY (the first src/ change since v46: the X-hover census discovered the hovered-COLOR gap — the reference's ghost family carries hover:text-accent-foreground [rgb(23,23,23) under hover], the clone's X + row actions [calculator-dialog.tsx:138/239/247] did not; the family scope measured live — the reference's edit AND trash both go accent-foreground under hover; the repair: hover:text-accent-foreground on all three — the v27 G1 precedent's own fix form)** + the ghost-hover family's own-hover ladders pin at 1280 (the X ladder + the row-action ladders + the fixture restore; the TDD RED run verified live before the repair; the line-138-scoped revert mutation sole-failure verified live — 1 failed + 20 passed; +1 e2e = 332) + the ship chain fully green (332 e2e zero flakes [336 executions], 35/35 smoke, the screenshots 16/16 byte-identical [the hover-only repair], the dev evidence 4/4 + VLM-verified) |** 108/332/35 green — the workspace the RE-PROVISIONED class (the daemon-reap discipline between the halves) |"
SKILL_ANCHOR = "|** 108/331/35 green — the workspace the CARRIED-OVER class (the browser-daemon reap lesson) |"
ok = ok and insert_after("zero-balance_SKILL.md", SKILL_ANCHOR, S164_ROW,
             "Session 164 — parity iteration v129")

# ---------------- D5: PAD ----------------
PAD_V186 = """#### Revision Block — v1.1.86 (Tracked Changes)
- `[UI]` v1.1.86 (2026-10-27) — the v129 parity iteration (**THE REPAIR CYCLE — the first src/ change since v46** + one e2e pin; no dependency change): the counts 108 unit / **332 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v123-era LOGIN + CALCULATOR pair's ELEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129] — the LOGIN view + the CALCULATOR dialog at desktop 1280x800; the FIFTY-SECOND consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly)**; the baseline fully green on the first chain (the RE-PROVISIONED workspace — the fresh-clone class, the v108 lesson end-to-end: npm ci, zod 840/840, both chromium pairs, .env + db/ provisioned; the daemon-exhaustion hang reaped between the halves — the v128 lesson's fresh-sandbox form); the VLM pair **the v123 consistent form — CALCULATOR DIFFERENT / LOGIN IDENTICAL both passes** (every flag in the documented classes: the pointer-position/hover-state shot artifact, the seed-data note, the VLM row misread; the FAB disproven live — fabCount 0 + bodyHasBase44 false both sides); the two-half census (the TWO-block v123 lineage, md5 e1092d12d06677a4/9e5a52d2ab0f2ab9 verified three-way) **106 axes — 97 identical + 9 documented-class deltas, ZERO new** (the v123 values reproduced EXACTLY); **THE REPAIR — the CALCULATOR GHOST-HOVER FAMILY (the first production-code change since v46 — the eighteen-cycle PIN-ONLY run ends)**: the both-sides X-hover census (xhover-arbit-v129.sh — the dual panel finder [the reference's dialog is a plain fixed div], the real-pointer dialog open, the v87 geometric X finder) measured the tint identical but **the hovered-COLOR axis a clone gap — the reference's ghost family carries hover:text-accent-foreground [rgb(23,23,23) under hover], the clone's calculator X + row actions [calculator-dialog.tsx:138/239/247] carried hover:bg-accent alone**; the family scope measured live (rowaction-hover-ref-v129.sh — the reference's edit AND trash both go accent-foreground under hover, the red trash included); the repair: hover:text-accent-foreground on all three (the v27 G1 precedent's own fix form; every at-rest pin structurally immune; the a11y gate immune [≈15.6:1]); **the ghost-hover family's own-hover ladders pin at 1280** (the X ladder at-rest → hovered {bg rgb(245,245,245) + color rgb(23,23,23)} → restored + the row-action ladders {the trash KEEPS its red at rest — rgb(220,38,38) — the hover-only transition} + the fixture restore; the TDD RED run verified live before the repair; **the line-138-scoped revert mutation sole-failure verified live — 1 failed + 20 passed, the diff exactly the predicted hovered-color line**; the post-repair census: the OWN-HOVERED state byte-identical both sides); the ship chain 332 e2e zero flakes (336 executions in 5 runs) + 35/35 smoke + the screenshots 16/16 byte-identical (the hover-only repair — no at-rest surface touched) + the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true).
"""
ok = ok and insert_before("Project_Architecture_Document.md",
    "#### Revision Block — v1.1.85 (Tracked Changes)",
    PAD_V186,
    "Revision Block — v1.1.86")

print("D1-D5:", "ALL ALIGNED" if ok else "FAILED")
sys.exit(0 if ok else 1)
