#!/usr/bin/env python3
"""Align the docs for the v131 cycle (Session 166).

D1  AGENTS.md     — the v131 paragraph appended after the v130 paragraph
                    (the v130 paragraph is the file's last line; the anchor
                    carries the v130-unique dev-shots-derivation tokens)
D2  CLAUDE.md     — the E2E count 333 -> 334 + the v131 clause
D3  README.md     — the count strings 333 -> 334 (two places) + the v131
                    plan row appended after the v130 row (the anchor
                    disambiguated by the v130-unique alpha-modifier tokens)
D4  SKILL.md      — project_state 333 -> 334 + the Session 166 row appended
                    after the Session 165 row
D5  PAD           — the [UI] v1.1.88 revision block (inserted newest-first,
                    BEFORE the v1.1.87 block)
D6  probe README  — the v131 section + the v132 queue   [align-probereadme-v131.py]
D7  session_318.md + the worklog Session 166 entry (separate steps)

D0 checked clean: every insert anchor below verified 1-hit before any write
(the AGENTS anchor by the v130-unique dev-shots tokens; the README anchor
by the v130-unique alpha-modifier tokens; the CLAUDE anchor by the v130-unique
post-restore-regression tokens; the SKILL anchor by the S165-unique
resource-discipline tokens).
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
V131_AGENTS = """

Reference surfaces pinned by the v131 iteration (`docs/remediation-plan-v131.md`) — **the re-run cycle's next-oldest candidate (the v125-era DASHBOARD pair — the DASHBOARD at desktop 1280x800 FULL-PAGE, the v61-era dashboard pair's surface family [the Budget Guidelines card + the Quick-Action row below the fold], the pair's ELEVENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131], the FIFTY-FOURTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly: the TENTH ordinal stated in vlm-shots-v125.sh's own header on its 11-entry bracket [v61 the original] → v131 = the ELEVENTH, no prose/header conflict)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only canary prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds — one node_modules/axe-core entry verified live) + the npm-audit watch at its twenty-second re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 125th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 125th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). **The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs (the PIN-ONLY form, the v128/v129/v130 class)** (the RE-PROVISIONED workspace — the v127/v129/v130 cycle's own form: the fresh clone from main @ 4818db7, the v108 lesson end-to-end [npm ci in the foreground, the zod extraction intact 840/840, BOTH chromium pairs — the fresh cache held only the OLD 1200 pair, the 1243 pair installed, the .env + db/ provisioned, db:push + db:seed, the seedcheck exact before any gate]; lint · typecheck · 108 unit · build [robots + sitemap prerendered] · 333 e2e zero flakes [336 executions in 4 chunks = 332 spec + 1 setup] · 35/35 smoke; the production-seam audit clean + the v130 pin verified in place). The probe series derived from the v125 lineage (derive-v131-series.py — FOUR explicit session-token families [refvlm/clonevlm + refar/clonear arbit — the arbit tokens carry '125' without the 'v' prefix] + SIX history-correction fragments [the era marker, the bracket extension, the ordinal TENTH→ELEVENTH, the agreement ordinal FORTY-EIGHTH→FIFTY-FOURTH, the re-proves chain, the arbit verdict/census provenance], zero residual, line counts preserved 58/43/46/259) + the THREE-block two-half contract verified three-way (verify-twohalf-v131.py — ARBIT_G 61 lines md5 b500dd299e5e9a94eaf07b29facc69db + ARBIT_Q 58 lines md5 da04e9954976eb58d9aff2b95d2dcfc6 + ARBIT_X 25 lines md5 7a381755a22ce55c62f70a053f826852) + the comparator derived (the /tmp/vlm125→/tmp/vlm131 explicit log-path swap + the provenance citations re-pointed at the v125 measurement). **The VLM verdict — IDENTICAL ×2, THE CLEANEST PAIR FORM** (the v125 cycle's own verdict form re-confirmed: zero layout/style flags BOTH passes, NO DOM arbitration needed; the flags all in the documented classes — the data differences the SEED-DATA/PCT classes, the pass-2 nav-highlight the v56 SUPERSET class, the avatar letter the USER-IDENTITY class). The both-sides census compared AXIS-BY-AXIS by the persisted compare-v131-census.py (**154 axes: 144 identical + 10 documented-class deltas, ZERO new** — REPRODUCING the v125 census values EXACTLY: the same 154/144/10 split, zero drift on every axis). **THE PIN — the INTERACTIVE STAT CARD's OWN-HOVER REVEAL LADDER at 1280 (+1 e2e = 334; PIN-ONLY — src/ zero changes)**: the candidate survey (the stat-card family's coverage map read across all 24 spec files — the v40 pin the tab stops + the geometry bands + the Enter/Space SUPERSET activation, the v42 the hero grid census, the v51 F2 the at-rest chrome, the v88 the count-row + the divider, the v125 pin the QUICK-ACTION twin [a different component family]; the stat card's hover end-states held by NO spec; a live survey probe finding the REFERENCE'S OWN INERT CARD CARRIES THE SAME REVEAL FAMILY — `absolute top-0 right-0 w-32 h-32 rounded-full opacity-0 group-hover:opacity-10` + `lucide-chevron-right w-5 h-5 opacity-0 group-hover:opacity-100` — the reveals the reference's own pure-CSS group-hover idiom, a BOTH-SIDES parity axis, NOT a superset axis; only the INTERACTIVITY is superset); the both-sides one-shot census stathover-arbit-v131.sh (the v51 F2 card finder, the state-independent finders [the radial by the absolute 9999px-radius shape, the chevron by the 19..21 width band — the v107 lesson: the at-rest opacity-0 chevron finder FAILED on the hovered rung in the first run, the opacity being the animated axis; the type icon 24px + the trend icon 16px outside the band], the (5,5)-parked ladder, the live-read center, READ-ONLY per the v46 rule — the clone's card CLICK NAVIGATES, never clicked) measured the ladder **BYTE-IDENTICAL both sides** — at-rest {radial opacity 0, chevron opacity 0} → OWN-HOVERED {radial opacity 0.1, chevron opacity 1, cardHover true} → restored, the transitions opacity 0.3s/0.2s identical — **no gap, no repair**; the pin (append-pin-v131.py — the Total Income card, the V94-COLLISION-safe axis set [the end-states alone, the transition metadata deliberately not pinned]) GREEN on the first run; **THE PIN-SANITY MUTATION — the line-587-scoped value-only form (group-hover:opacity-10 → group-hover:opacity-20, the radial alone; the -100 twins at :602/:899 carry the -10 substring, the line scope load-bearing)**: the SOLE FAILURE verified live — 1 failed [the pin] + 4 passed in the family grep, the deep-equality diff EXACTLY the predicted hovered-radial line [opacity 0.1 → 0.2; cardHover/chevron preserved, the at-rest + restored rungs UNAFFECTED]; restored (git diff src/ = 0 lines) + the FULL REBUILD + the 157/157 post-restore regression (dashboard 50 + networth 37 + items 49 + calculator 20 — the v128/v129/v130 pins' different-file immunity verified live). The ship chain 334 e2e zero flakes (92+89+74+82 = 337 executions = 334 unique); 35/35 smoke; **the screenshots 16/16 captured — 9 byte-identical + 7 the DETERMINISTIC CROSS-DAY DATE-CLASS refresh (the first cross-day capture since v127: the seed's relative isoDate(-N) dates + the dialogs' todayIso() default shifted one day; the changed set EXACTLY the date-bearing surfaces — 03/04/05/06 the item views + 07 the modal + 08 the calculator + 16 the details; the date-free 9 byte-identical)**; the dev evidence 4/4 (3 byte-identical + dev-mobile-income-390 the date-class twin) + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the dev-shots scripts derived v130→v131 with the version-swap-only verification)."""
AGENTS_TAIL = "the dev-shots scripts derived v129→v130 with the version-swap-only verification)."
ok = ok and insert_after("AGENTS.md", AGENTS_TAIL, V131_AGENTS,
             "Reference surfaces pinned by the v131 iteration")

# ---------------- D2: CLAUDE.md ----------------
ok = ok and replace1("CLAUDE.md",
    "- **E2E (Playwright, 333)**:",
    "- **E2E (Playwright, 334)**:")
ok = ok and insert_after("CLAUDE.md",
    "the post-restore regression 107/107)",
    "; the v131 pin — the INTERACTIVE STAT CARD's own-hover reveal ladder at 1280 (PIN-ONLY — src/ zero changes: the both-sides census stathover-arbit-v131.sh measured the ladder byte-identical — at-rest {radial 0, chevron 0} → own-hovered {radial 0.1, chevron 1} → restored; the REFERENCE'S OWN inert card carries the same reveal family — a both-sides parity axis, not a superset axis; the state-independent chevron finder's 19..21 width band; the line-587-scoped opacity-10→opacity-20 mutation sole-failure verified live [1 failed + 4 passed, the diff exactly the predicted hovered-radial line]; the post-restore regression 157/157)",
    "the v131 pin — the INTERACTIVE STAT CARD's own-hover reveal ladder")

# ---------------- D3: README.md ----------------
ok = ok and replace1("README.md",
    "│   └── 📂 e2e/                    # Playwright specs (333 tests) + global setup",
    "│   └── 📂 e2e/                    # Playwright specs (334 tests) + global setup")
ok = ok and replace1("README.md",
    "npm run test:e2e    # Playwright e2e (333 tests) — needs `npm run build` first",
    "npm run test:e2e    # Playwright e2e (334 tests) — needs `npm run build` first")
V131_ROW = "\n| [`docs/remediation-plan-v131.md`](docs/remediation-plan-v131.md) | **The re-run cycle's next-oldest candidate (the v125-era DASHBOARD pair's ELEVENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131] — the DASHBOARD at desktop 1280x800 FULL-PAGE [the Budget Guidelines card + the Quick-Action row]; the FIFTY-FOURTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly, the TENTH ordinal stated in vlm-shots-v125.sh's own header)** + the axe watch (NO DRIFT — 4.14.0 holds) + the npm-audit watch (0 vulnerabilities, twenty-second re-check) + the 125th standing checks (ALL GREEN — the mobile menu the 125th consecutive pass) + the VLM pair **IDENTICAL ×2 — the cleanest pair form** (zero style flags both passes, no DOM arbitration; every flag in the documented classes) + the census 154 axes — 144 identical + 10 documented, ZERO new (the v125 values reproduced EXACTLY) + **the stat-card own-hover reveal ladder pin at 1280 (+1 e2e = 334; PIN-ONLY — the reference's own inert card carries the same reveal family, the both-sides census measured the ladder byte-identical, no repair; the line-587-scoped opacity mutation sole-failure verified live)** + the screenshots 16/16 captured (9 byte-identical + 7 the deterministic cross-day date-class refresh — the seed's relative dates shifted one day, the changed set exactly the date-bearing surfaces). |"
README_ANCHOR = "the line-82-scoped alpha-modifier mutation sole-failure verified live)** + the screenshots 16/16 byte-identical (the same-day law). |"
ok = ok and insert_after("README.md", README_ANCHOR, V131_ROW,
             "remediation-plan-v131.md")

# ---------------- D4: SKILL.md ----------------
ok = ok and replace1("zero-balance_SKILL.md",
    "project_state: 108 unit tests / 333 e2e tests / 35 smoke steps — all green",
    "project_state: 108 unit tests / 334 e2e tests / 35 smoke steps — all green")
S166_ROW = "\n| 2026-10-28 | Session 166 — parity iteration v131 (`docs/remediation-plan-v131.md`) | **The re-run cycle's next-oldest candidate (the v125-era DASHBOARD pair's ELEVENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131] — the DASHBOARD at desktop 1280x800 FULL-PAGE; the FIFTY-FOURTH consecutive queue/ledger agreement)** + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — twenty-second re-check) + the 125th standing checks (ALL GREEN — the reference's four bugs live, the mobile menu the 125th consecutive pass, zero overflow at 390) + the VLM pair **IDENTICAL ×2 — the cleanest pair form** (zero style flags both passes, no DOM arbitration; every flag in the documented classes: the seed-data/pct classes, the nav-highlight v56 superset, the avatar user-identity) + the two-half census (154 axes — 144 identical + 10 documented, ZERO new — the v125 values reproduced EXACTLY, the THREE-block md5 b500dd299e5e9a94eaf07b29facc69db/da04e9954976eb58d9aff2b95d2dcfc6/7a381755a22ce55c62f70a053f826852 lineage verified three-way) + **the stat-card own-hover reveal ladder pin at 1280 (PIN-ONLY — src/ zero changes: the candidate survey found the reference's own inert card carries the same reveal family [a both-sides parity axis, not a superset axis]; the both-sides census stathover-arbit-v131.sh measured the ladder byte-identical [at-rest {radial 0, chevron 0} → own-hovered {radial 0.1, chevron 1, cardHover true} → restored]; the state-independent chevron finder's 19..21 width band; the line-587-scoped opacity-10→opacity-20 mutation sole-failure verified live — 1 failed + 4 passed, the diff exactly the predicted hovered-radial line; the post-restore regression 157/157; +1 e2e = 334)** + the ship chain fully green (334 e2e zero flakes [337 executions], 35/35 smoke, the screenshots 16/16 captured [9 byte-identical + 7 the deterministic cross-day date-class refresh], the dev evidence 4/4 + VLM-verified) |** 108/334/35 green — the workspace the RE-PROVISIONED class (the resource discipline between the halves) |"
SKILL_ANCHOR = "|** 108/333/35 green — the workspace the RE-PROVISIONED class (the resource discipline between the halves) |"
ok = ok and insert_after("zero-balance_SKILL.md", SKILL_ANCHOR, S166_ROW,
             "Session 166 — parity iteration v131")

# ---------------- D5: PAD ----------------
PAD_V188 = """#### Revision Block — v1.1.88 (Tracked Changes)
- `[UI]` v1.1.88 (2026-10-28) — the v131 parity iteration (**PIN-ONLY — src/ zero changes** + one e2e pin; no dependency change): the counts 108 unit / **334 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v125-era DASHBOARD pair's ELEVENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131] — the DASHBOARD at desktop 1280x800 FULL-PAGE; the FIFTY-FOURTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly)**; the baseline fully green on the first chain (the RE-PROVISIONED workspace — the fresh-clone class, the v108 lesson end-to-end: npm ci, zod 840/840, both chromium pairs, .env + db/ provisioned; the resource discipline between the halves); the VLM pair **IDENTICAL ×2 — the cleanest pair form** (zero style flags both passes, no DOM arbitration; every flag in the documented classes); the two-half census (the THREE-block v125 lineage, md5 b500dd299e5e9a94eaf07b29facc69db/da04e9954976eb58d9aff2b95d2dcfc6/7a381755a22ce55c62f70a053f826852 verified three-way) **154 axes — 144 identical + 10 documented-class deltas, ZERO new** (the v125 values reproduced EXACTLY); **the interactive stat-card own-hover reveal ladder pin at 1280**: the candidate survey (the stat-card family's coverage map — the hover end-states held by no spec; a live survey probe finding the reference's own inert card carries the same reveal family — the reveals the reference's own pure-CSS group-hover idiom, a BOTH-SIDES parity axis, not a superset axis) + the both-sides census **byte-identical** (no gap, no repair) + the pin (the V94-COLLISION-safe axis set — the end-states alone) + **the line-587-scoped value-only mutation sole-failure verified live — 1 failed + 4 passed, the diff exactly the predicted hovered-radial line [opacity 0.1 → 0.2]** + restored + the 157/157 post-restore regression; the ship chain 334 e2e zero flakes (337 executions in 4 chunks) + 35/35 smoke + the screenshots 16/16 captured (9 byte-identical + 7 the deterministic cross-day date-class refresh — the seed's relative isoDate(-N) dates + the dialogs' todayIso() default shifted one day, the changed set exactly the date-bearing surfaces) + the dev evidence 4/4 + VLM-verified (the menu proof: /income, docSW 390, navLandmark true).
"""
ok = ok and insert_before("Project_Architecture_Document.md",
    "#### Revision Block — v1.1.87 (Tracked Changes)",
    PAD_V188,
    "Revision Block — v1.1.88")

print("D1-D5:", "ALL ALIGNED" if ok else "FAILED")
sys.exit(0 if ok else 1)
