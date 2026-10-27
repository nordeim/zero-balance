#!/usr/bin/env python3
"""Align the docs for the v127 cycle (Session 162).

D1  AGENTS.md     — the v127 paragraph appended after the v126 paragraph
                    (the v126 paragraph is the file's last content; the
                    anchor carries the v126-unique tokens f018ede /
                    session_307.md])
D2  CLAUDE.md     — the E2E count 329 -> 330 + the v127 clause
D3  README.md     — the count strings 329 -> 330 (two places) + the v127
                    plan row appended after the v126 row (the anchor
                    disambiguated by the v126-unique "v120 values
                    reproduced EXACTLY" tokens)
D4  SKILL.md      — project_state 329 -> 330 + the Session 162 row appended
                    after the Session 161 row
D5  PAD           — the [UI] v1.1.84 revision block (inserted newest-first,
                    before the v1.1.83 block)
D6  probe README  — the v127 section + the v128 queue   [align-probereadme-v127.py]
D7  session_310.md + the worklog Session 162 entry (separate steps)

D0 checked clean: every insert anchor below verified 1-hit before any write
(the AGENTS anchor by the v126-unique git-pull tokens; the README anchor by
the v126-unique census tokens; the CLAUDE anchor by the v126-unique
3-line/w-h/r tokens).
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

ok = True

# ---------------- D1: AGENTS.md ----------------
V127_AGENTS = """

Reference surfaces pinned by the v127 iteration (`docs/remediation-plan-v127.md`) — **the re-run cycle's next-oldest candidate (the v121-era ITEMS pair — the ITEMS view [INCOME + EXPENSES] at desktop 1280x800 FULL-PAGE, the v57-era items pair's surface family, the pair's ELEVENTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127], the FIFTIETH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly: the ordinal derived from vlm-shots-v121.sh's own header [the TENTH on its 11-entry bracket, v57 the original] — v127 = the ELEVENTH, no prose/header conflict)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only the canary 4.14.0-canary.6b52b84 prerelease beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds — one node_modules/axe-core entry verified live; the engine-contract pin green) + the npm-audit watch at its eighteenth re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 121st standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 121st consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). **The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs this cycle** (lint · typecheck · 108 unit · build · 329 e2e zero flakes [332 executions in 4 chunks] · 35/35 smoke; the post-push commit 9e40655 audited session-log-only [docs/session_309.md alone, 120 insertions]; the production-seam audit clean). **The verdict the VLM-VARIATION form — pass 1 INCOME IDENTICAL + EXPENSES DIFFERENT / pass 2 BOTH PAIRS DIFFERENT — the pair's documented verdict-variation family** (the v105 LOGIN-IDENTICAL / v121 split precedent: v121 itself read the inverse split; the income side's flags all-data/identity classes, so the verdict flips across passes on the same chrome) — every flag in the documented classes: the expenses card-footer payment chips the v57 DATA-CONDITIONAL class; the badge-arrangement wrap the v57 wrap/classification-VALUE classes (badgeRow h 22 vs 52, badgeCount 3 vs 4 — the clone's Recurring superset chip + the wrap; the chip chrome byte-identical); the avatar letters the USER-IDENTITY class; the card counts/figures/dates the SEED-DATA classes; the pass-2 income grid-layout flag the SEED-COUNT class; the "Edit with Base44" FAB claim (an exploratory pass) the PLATFORM-CHROME class DISPROVEN LIVE (base44-fab-arbit-v127.sh: fabCount 0 + bodyHasBase44 false on BOTH sides at 1280 /expenses — the v97/v103/v108/v109/v115/v120 standing disproof form re-confirmed live). The both-sides census (the ONE-block v121 lineage — CENSUS_JS, the md5 contract b55dcd29 verified by direct THREE-WAY python extraction [verify-twohalf-v127.py — the source + both halves], the v103/v109/v115/v121 lineage values VERBATIM; built by build-twohalf-v127.py derived from build-twohalf-v121.py with the EXPLICIT session-token swap clonearbit121→clonearbit127 [the token carries no 'v121' substring — the v121-cycle stale-session-fix precedent applied at the derivation stage] + the lesson-range bump v92..v126 + the lineage-note fixup) compared AXIS-BY-AXIS by the persisted compare-v127-census.py (**187 axes: 163 identical + 24 documented-class deltas, ZERO new** — REPRODUCING the v121 census values EXACTLY, the same 187/163/24 split, zero drift on every axis). **THE PIN — the item-card BADGE's HOVER END-STATE census at 1280 (PIN-ONLY — the never-pinned hover path of the pinned badge family, +1 e2e = 330)**: the hovered tint — globals.css:421 `.zb-badge-hover:hover { background-color: rgba(245,245,245,0.8) }` — held by NO spec at ANY viewport (the v57 pin the badge ROW + badge0's AT-REST chrome; the v1-era + v28 G1/v29 G1 pins the zb-badge-hover CLASS TOKEN + the at-rest computed bg; every zb-badge-hover assertion in the suite a class-token check or an at-rest read — the hovered value appears only in comments). The BOTH-SIDES census (`badgehover-arbit-v127.sh` — the hover-ladder form, READ-ONLY per the v46 rule [login + passive navigation + a REAL pointer hover only — the v125 QA-hover precedent]; the finder TAG-AGNOSTIC [the "active" text leaf in the grid's first card]; the ladder parks at (5,5), reads the at-rest state, moves the REAL pointer to the badge's OWN live-read center, reads the end-state, parks back, verifies the restore; the reference login on the re-run after one transient first-run failure): **the hovered bg rgba(245,245,245,0.8) IDENTICAL both sides** + the at-rest bg rgb(248,250,252) → hovered → restored ladder IDENTICAL + the color rgb(51,65,85) + w 63 / h 22 + transitionDuration 0.15s IDENTICAL; the transitionProperty computed form the documented v3/v4 class (the reference's TW v3 shorter list vs the clone's v4 extended list — the v95 transition-property documented family). **THE PIN-SANITY MUTATION — the VALUE-ONLY form (designed against the collision map)**: `rgba(245, 245, 245, 0.8)` → `0.4` at globals.css:421 (the VALUE alone — the selector + the class token untouched, every class-token pin structurally immune BY CONSTRUCTION; the at-rest v57/v29 pins immune [the utility class's own value]; the a11y contrast gate immune [the mutated tint composites to ≈7:1 contrast — passing, so no new flagged node]) — **the SOLE FAILURE verified live: the pin ALONE red [1 failed + 48 green in the items file], the deep-equality diff EXACTLY the predicted line (bg 0.8→0.4 on the hovered rung alone; the at-rest + restored rungs UNAFFECTED), the networth immunity file 37/37 green [the OTHER zb-badge-hover site]**; restored + the full rebuild + the 85/85 post-restore regression. The ship chain 330 e2e zero flakes (90+87+74+82 = 333 executions = 330 unique); 35/35 smoke; **the screenshots 10 byte-identical + 6 refreshed (the seed-relative-date class — the fresh re-seed's isoDate(-N) dates shifting the date-bearing shots; the same-day law's refresh form, the v124 day-rollover precedent — the refreshed set committed)**; the dev evidence 3 byte-identical + 1 refreshed (the same date class) + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the dev-shots scripts derived v126→v127 with the version-swap-only verification). The workspace the RE-PROVISIONED class (the v121 cycle's own form — the sandbox workspace reset, the repo re-cloned from main @ 9e40655 [the operator's session_309.md tail]; the v108 FRESH-CLONE lesson applied end-to-end: npm ci in the foreground, the zod extraction verified intact [840/840, the v4 subdirectory at the package root], BOTH playwright chromium pairs verified directly in the cache [the fresh cache held only the OLD 1200 pair — the 1243 pair installed], the `.env` + `db/` provisioned at the repo root, db:push + db:seed, the seedcheck exact before any gate)."""
AGENTS_TAIL = "the repo refreshed via git pull to main @ f018ede, the operator's session_307.md tail; NO re-provisioning needed: the zod extraction verified intact [840/840], BOTH v1243 playwright pairs verified in the cache directly, the `.env` + `db/` in place, the seedcheck exact before any gate)."
ok = ok and insert_after("AGENTS.md", AGENTS_TAIL, V127_AGENTS,
             "Reference surfaces pinned by the v127 iteration")

# ---------------- D2: CLAUDE.md ----------------
ok = ok and replace1("CLAUDE.md",
    "- **E2E (Playwright, 329)**:",
    "- **E2E (Playwright, 330)**:")
ok = ok and insert_after("CLAUDE.md",
    "the 3-line deep-equality diff exactly as designed [w/h/r alone, the centering axes unaffected], the 48 others + the mobile-layout file green)",
    "; the v127 pin — the item-card BADGE's HOVER END-STATE census at 1280: the never-pinned hover path of the pinned badge family (the v57 pin the badge row + badge0 at-rest; the v1-era/v28 G1/v29 G1 pins the zb-badge-hover CLASS TOKEN + the at-rest bg — the hovered tint rgba(245,245,245,0.8) [globals.css:421] held by NO spec at ANY viewport); the both-sides census byte-identical on the ladder (at-rest rgb(248,250,252) → hovered rgba(245,245,245,0.8) → restored, the hoverMatch false→true→false); the pin-sanity VALUE-ONLY mutation (rgba 0.8→0.4 at globals.css:421 — the selector + class token untouched, every class-token pin immune by construction) sole-failure verified live — the 1-line deep-equality diff exactly as designed [the hovered bg alone; the at-rest + restored rungs unaffected], the items file's 48 others + the networth immunity file green)",
    "the v127 pin — the item-card BADGE's HOVER END-STATE census")

# ---------------- D3: README.md ----------------
ok = ok and replace1("README.md",
    "│   └── 📂 e2e/                    # Playwright specs (329 tests) + global setup",
    "│   └── 📂 e2e/                    # Playwright specs (330 tests) + global setup")
ok = ok and replace1("README.md",
    "npm run test:e2e    # Playwright e2e (329 tests) — needs `npm run build` first",
    "npm run test:e2e    # Playwright e2e (330 tests) — needs `npm run build` first")
V127_ROW = """
| [`docs/remediation-plan-v127.md`](docs/remediation-plan-v127.md) | **The re-run cycle's next-oldest candidate (the v121-era ITEMS pair's ELEVENTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127] — the ITEMS view [income + expenses] at desktop 1280x800 full-page; the FIFTIETH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly)** + the axe watch (NO DRIFT — 4.14.0 holds) + the npm-audit watch (0 vulnerabilities, eighteenth re-check) + the 121st standing checks (ALL GREEN — the mobile menu the 121st consecutive pass) + the item-card BADGE's HOVER END-STATE census pin at 1280 (PIN-ONLY — +1 e2e = 330; the never-pinned hover path of the pinned badge family — the hovered tint rgba(245,245,245,0.8) byte-identical both sides; the VALUE-ONLY mutation sole-failure verified live — the 1-line diff exactly as designed) + the baseline fully green on the first chain (the RE-PROVISIONED workspace — the fresh-clone class, the v108 lesson end-to-end) + the VLM pair the verdict-VARIATION form (pass 1 INCOME IDENTICAL + EXPENSES DIFFERENT / pass 2 BOTH PAIRS DIFFERENT — the documented v105/v121 family; every flag in the documented classes, the FAB claim disproven live) + the census 187 axes — 163 identical + 24 documented, ZERO new (the v121 values reproduced EXACTLY) + the screenshots 10 byte-identical + 6 refreshed (the seed-relative-date class). |"""
ok = ok and insert_after("README.md",
    "(the v120 values reproduced EXACTLY) + the screenshots 16/16 byte-identical (the same-day law). |",
    V127_ROW,
    "docs/remediation-plan-v127.md")

# ---------------- D4: zero-balance_SKILL.md ----------------
ok = ok and replace1("zero-balance_SKILL.md",
    "project_state: 108 unit tests / 329 e2e tests / 35 smoke steps — all green",
    "project_state: 108 unit tests / 330 e2e tests / 35 smoke steps — all green")
V127_SKILL_ROW = """
| 2026-10-27 | Session 162 — parity iteration v127 (`docs/remediation-plan-v127.md`) | **The re-run cycle's next-oldest candidate (the v121-era ITEMS pair's ELEVENTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127] — the ITEMS view [income + expenses] at desktop 1280x800 full-page; the FIFTIETH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly)** + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — eighteenth re-check) + the 121st standing checks (ALL GREEN — the reference's four bugs live, the mobile menu the 121st consecutive pass, zero overflow at 390) + the VLM pair (the verdict-VARIATION form — pass 1 INCOME IDENTICAL + EXPENSES DIFFERENT / pass 2 BOTH PAIRS DIFFERENT, the documented v105/v121 family; every flag in the documented classes, the FAB claim disproven live) + the two-half census (187 axes — 163 identical + 24 documented, ZERO new — the v121 values reproduced EXACTLY, the single-block md5 b55dcd29 lineage verified three-way) + the item-card BADGE's HOVER END-STATE census pin at 1280 (PIN-ONLY — the never-pinned hover path of the pinned badge family; the both-sides census byte-identical on the ladder — the hovered tint rgba(245,245,245,0.8); the VALUE-ONLY mutation sole-failure verified live — the 1-line diff exactly as designed; +1 e2e = 330) + the ship chain fully green (330 e2e zero flakes [333 executions], 35/35 smoke, the screenshots 10 byte-identical + 6 refreshed [the seed-relative-date class], the dev evidence 3+1 + VLM-verified) |** 108/330/35 green — the workspace the RE-PROVISIONED class (fresh clone, the v108 lesson end-to-end) |"""
ok = ok and insert_after("zero-balance_SKILL.md",
    "|** 108/329/35 green — the workspace the CARRIED-OVER class (git pull, no re-provisioning) |",
    V127_SKILL_ROW,
    "Session 162 — parity iteration v127")

# ---------------- D5: Project_Architecture_Document.md ----------------
# newest-first: the v1.1.84 block goes BEFORE the v1.1.83 header — a
# direct replace (the v1.1.84 block + the v1.1.83 header re-attached).
V127_PAD = """#### Revision Block — v1.1.84 (Tracked Changes)
- `[UI]` v1.1.84 (2026-10-27) — the v127 parity iteration (**PIN-ONLY — zero production-code changes** + one e2e pin; no dependency change): the counts 108 unit / **330 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v121-era ITEMS pair's ELEVENTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127] — the ITEMS view [income + expenses] at desktop 1280x800 full-page; the FIFTIETH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly)**; the baseline fully green on the first chain (the RE-PROVISIONED workspace — the fresh-clone class, the v108 lesson end-to-end: npm ci, zod 840/840, both chromium pairs, .env + db/ provisioned); the VLM pair **the verdict-VARIATION form — pass 1 INCOME IDENTICAL + EXPENSES DIFFERENT / pass 2 BOTH PAIRS DIFFERENT — the pair's documented verdict-variation family** (the v105/v121 precedent; every flag in the documented classes; the FAB claim disproven live — fabCount 0 + bodyHasBase44 false both sides); the two-half census (the single-block v121 lineage, md5 b55dcd29 verified three-way) **187 axes — 163 identical + 24 documented-class deltas, ZERO new** (the v121 values reproduced EXACTLY); **THE PIN — the item-card BADGE's HOVER END-STATE census at 1280** (the never-pinned hover path of the pinned badge family: the v57 pin the badge row + badge0 at-rest, the v1-era/v28 G1/v29 G1 pins the class token + the at-rest bg — the hovered tint rgba(245,245,245,0.8) [globals.css:421] held by NO spec at ANY viewport; the both-sides census: **the hovered bg byte-identical both sides** — the ladder at-rest rgb(248,250,252) → hovered rgba(245,245,245,0.8) → restored identical, the color/w/h/duration identical; **the VALUE-ONLY mutation [rgba 0.8→0.4 at globals.css:421 — the selector + class token untouched, every class-token pin immune by construction] sole-failure verified live — the 1-line deep-equality diff exactly as designed, the at-rest + restored rungs unaffected, the items file's 48 others + the networth immunity file green**); the ship chain 330 e2e zero flakes (333 executions in 4 chunks) + 35/35 smoke + the screenshots 10 byte-identical + 6 refreshed (the seed-relative-date class — the fresh re-seed's isoDate(-N) dates; the same-day law's refresh form) + the dev evidence 3 byte-identical + 1 refreshed + VLM-verified (the menu proof: /income, docSW 390, navLandmark true).
"""
ok = ok and replace1("Project_Architecture_Document.md",
    "#### Revision Block — v1.1.83 (Tracked Changes)",
    V127_PAD + "#### Revision Block — v1.1.83 (Tracked Changes)")

if ok:
    print("D1-D5 aligned: AGENTS + CLAUDE + README + SKILL + PAD")
else:
    print("ALIGNMENT INCOMPLETE — see the AMBIGUOUS/MISS lines above")
    sys.exit(1)
