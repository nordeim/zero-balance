#!/usr/bin/env python3
"""Align the docs for the v128 cycle (Session 163).

D1  AGENTS.md     — the v128 paragraph appended after the v127 paragraph
                    (the v127 paragraph is the file's last content; the
                    anchor carries the v127-unique fresh-clone tokens
                    [the 1243-pair install / the seedcheck-before-gate])
D2  CLAUDE.md     — the E2E count 330 -> 331 + the v128 clause
D3  README.md     — the count strings 330 -> 331 (two places) + the v128
                    plan row appended after the v127 row (the anchor
                    disambiguated by the v127-unique census/screenshot tokens)
D4  SKILL.md      — project_state 330 -> 331 + the Session 163 row appended
                    after the Session 162 row
D5  PAD           — the [UI] v1.1.85 revision block (inserted newest-first,
                    BEFORE the v1.1.84 block)
D6  probe README  — the v128 section + the v129 queue   [align-probereadme-v128.py]
D7  session_312.md + the worklog Session 163 entry (separate steps)

D0 checked clean: every insert anchor below verified 1-hit before any write
(the AGENTS anchor by the v127-unique fresh-clone tokens; the README anchor
by the v127-unique census/screenshot tokens; the CLAUDE anchor by the
v127-unique 48-others/immunity tokens).
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
V128_AGENTS = """

Reference surfaces pinned by the v128 iteration (`docs/remediation-plan-v128.md`) — **the re-run cycle's next-oldest candidate (the v122-era SAVINGS pair — the SAVINGS view at desktop 1280x800 FULL-PAGE, the v58-era savings pair's surface family, the pair's ELEVENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128], the FIFTY-FIRST consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly: the era chain traced through the lineage headers [v122←v116←v110←v104←v98←v92←v86←v80←v58 = 11 entries, the TENTH ordinal stated in the v122 plan's own title, v58 the original] — v128 = the ELEVENTH, no prose/header conflict)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only the canary 4.14.0-canary.6b52b84 prerelease beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds — one node_modules/axe-core entry verified live; the engine-contract pin green) + the npm-audit watch at its nineteenth re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 122nd standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 122nd consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). **The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs this cycle** (lint · typecheck · 108 unit · build · 330 e2e zero flakes [333 executions in 4 chunks] · 35/35 smoke; the post-pull commit 597709a audited session-log-only [docs/session_311.md alone, 108 insertions]; the production-seam audit clean; the workspace the CARRIED-OVER class — the v127 environment persisted, the repo refreshed via git pull, NO re-provisioning needed, the seedcheck exact before any gate). **THE v128 ENVIRONMENT INCIDENT — the carried-over workspace's browser-daemon exhaustion, reaped**: the clone-half shots' login eval read "no inputs" twice, the VLM flagging the login-page shot live; the direct diagnosis — `agent-browser eval` failing with "OS can't spawn worker thread: Resource temporarily unavailable (os error 11)": the CARRIED-OVER sandbox inherited the v127 cycle's STALE AGENT-BROWSER DAEMON TREES (two full chrome-155 trees) + the stale :3000 next-server, together exhausting the 4GB sandbox; the reap (pkill agent-browser + chrome-155 + SIGKILL on the SIGTERM-surviving next-server [the v126 lesson's form] + the .next/dev/lock removal [the v124 lesson]) recovered the memory (1155→2545MB available), the clone half then first-attempt — **the v128 lesson: a carried-over workspace inherits the prior cycle's browser daemons; reap them before the probe series**. **The verdict BOTH PASSES DIFFERENT — every flag in the documented classes** (the savings pair's consistent form): the card-grid layout the SEED-COUNT class (ref 1 card vs clone 2); the card-footer payment chips the v57 DATA-CONDITIONAL class (the reference RENDERS payment chips when its data carries them; its savings item ships none); the badge styling the classification-VALUE + the v57 wrap/superset-chip classes; the sidebar avatar the USER-IDENTITY class; the header stats + card names/amounts/dates the SEED-DATA classes; no FAB claim in either pass — no disproof needed. The both-sides census (the ONE-block v122 lineage — SV_CENSUS_JS, the md5 contract 891ab9b6 verified by direct THREE-WAY python extraction [verify-twohalf-v128.py — the source + both halves]; built by build-twohalf-v128.py derived from build-twohalf-v122.py with the EXPLICIT session-token swap refarbit122→refarbit128 [the v121-cycle stale-session-fix precedent applied at the derivation stage] + the lesson-range bump v92..v127 + the lineage-note fixup) compared AXIS-BY-AXIS by the persisted compare-v128-census.py (**120 axes: 80 identical + 40 documented-class deltas, ZERO new** — REPRODUCING the v122 census values EXACTLY, the same 120/80/40 split, zero drift on every axis). **THE PIN — the savings goal-card KEBAB-TRIGGER's OWN-HOVER END-STATE census at 1280 (PIN-ONLY — the never-pinned TINT PATH of the pinned reveal family, +1 e2e = 331)**: the trigger's own hover end-state — the `hover:bg-accent` TINT (item-card.tsx:139, the file's sole occurrence) + the `hover:text-accent-foreground` COLOR + the simultaneous group-hover reveal — held by NO spec at ANY viewport (the reveal family's OPACITY paths fully held: v45 F1a the at-rest w/h/opacity, v116 the at-rest chrome + the CARD-hover reveal, v36 the keyboard path, v122 the OPEN+parked state, v98 the menu panel; the dialog-buttons v27 G1 pin holds the hover:bg-accent CLASS TOKEN on the DIALOG X — a different element in a different file). The BOTH-SIDES census (`kebabhover-arbit-v128.sh` — the hover-ladder form, READ-ONLY per the v46 rule [the menu opens on CLICK, the hover alone never opens it — the v125 QA-hover / v127 badge-hover precedent]; the finder TAG-AGNOSTIC + STRUCTURAL [the v116 form]; the ladder parks at (5,5) FIRST — BEFORE the finder — so the opacity-0 finder reads a clean at-rest trigger): **the OWN-HOVERED state {opacity 1 + bg rgb(245,245,245) [the accent tint] + color rgb(23,23,23) [accent-foreground] + hoverMatch true + cardHover true} IDENTICAL both sides** + the at-rest → hovered → restored ladder IDENTICAL + the w 36 / h 36 / radius 6px + the transition metadata identical (both sites' transition-opacity compiles to the single-property list — no v3/v4 computed-form difference on this element). **THE PIN-SANITY MUTATION — the ALPHA-MODIFIER VALUE-ONLY form (designed against the collision map)**: `hover:bg-accent` → `hover:bg-accent/50` at item-card.tsx:139 (the file's SOLE occurrence — line-scoped; every at-rest/card-hover/open axis structurally untouched; the a11y contrast gate immune [the mutated 0.5-alpha tint composites to ≈15:1 contrast — passing, no new flagged node]; the networth kebab twins untouched [the same class string in a different file]) — **the SOLE FAILURE verified live: the pin ALONE red [1 failed + 49 green in the full items file], the deep-equality diff EXACTLY the predicted line (bg rgb(245,245,245)→the mutated lab(...0.5) alpha form on the hovered rung alone; hoverMatch true + opacity 1 + color preserved, the at-rest + restored rungs UNAFFECTED), the networth immunity file 37/37 green [the same class string in a different file]**; restored + the full rebuild + the 86/86 post-restore regression. The ship chain 331 e2e zero flakes (90+88+74+82 = 334 executions = 331 unique); 35/35 smoke; **the screenshots 16/16 byte-identical (the same-day law — no refresh needed this cycle)**; the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the dev-shots scripts derived v127→v128 with the version-swap-only verification)."""
AGENTS_TAIL = "BOTH playwright chromium pairs verified directly in the cache [the fresh cache held only the OLD 1200 pair — the 1243 pair installed], the `.env` + `db/` provisioned at the repo root, db:push + db:seed, the seedcheck exact before any gate)."
ok = ok and insert_after("AGENTS.md", AGENTS_TAIL, V128_AGENTS,
             "Reference surfaces pinned by the v128 iteration")

# ---------------- D2: CLAUDE.md ----------------
ok = ok and replace1("CLAUDE.md",
    "- **E2E (Playwright, 330)**:",
    "- **E2E (Playwright, 331)**:")
ok = ok and insert_after("CLAUDE.md",
    "the items file's 48 others + the networth immunity file green)",
    "; the v128 pin — the savings goal-card KEBAB-TRIGGER's OWN-HOVER END-STATE census at 1280: the never-pinned TINT PATH of the pinned reveal family (the v45/v36/v116/v122/v98 pins hold the reveal family's OPACITY paths + the at-rest/open chrome; the trigger's own-hover tint [hover:bg-accent, item-card.tsx:139 — the file's sole occurrence] + color [hover:text-accent-foreground] held by NO spec at ANY viewport); the both-sides census byte-identical on the ladder (at-rest {opacity 0, bg transparent, color rgb(10,10,10)} → own-hovered {opacity 1, bg rgb(245,245,245), color rgb(23,23,23)} → restored, the hoverMatch + cardHover ladders false→true→false); the pin-sanity ALPHA-MODIFIER VALUE-ONLY mutation (hover:bg-accent→hover:bg-accent/50 — line-scoped, every other reveal-path pin structurally immune) sole-failure verified live — the 1-line deep-equality diff exactly as designed [the hovered bg alone; hoverMatch true + opacity 1 + color preserved, the at-rest + restored rungs unaffected], the items file's 49 others + the networth immunity file green)",
    "the v128 pin — the savings goal-card KEBAB-TRIGGER's OWN-HOVER END-STATE census")

# ---------------- D3: README.md ----------------
ok = ok and replace1("README.md",
    "│   └── 📂 e2e/                    # Playwright specs (330 tests) + global setup",
    "│   └── 📂 e2e/                    # Playwright specs (331 tests) + global setup")
ok = ok and replace1("README.md",
    "npm run test:e2e    # Playwright e2e (330 tests) — needs `npm run build` first",
    "npm run test:e2e    # Playwright e2e (331 tests) — needs `npm run build` first")
V128_ROW = "\n| [`docs/remediation-plan-v128.md`](docs/remediation-plan-v128.md) | **The re-run cycle's next-oldest candidate (the v122-era SAVINGS pair's ELEVENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128] — the SAVINGS view at desktop 1280x800 full-page; the FIFTY-FIRST consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly, the era chain traced through the lineage headers)** + the axe watch (NO DRIFT — 4.14.0 holds) + the npm-audit watch (0 vulnerabilities, nineteenth re-check) + the 122nd standing checks (ALL GREEN — the mobile menu the 122nd consecutive pass) + the savings goal-card KEBAB-TRIGGER's OWN-HOVER END-STATE census pin at 1280 (PIN-ONLY — +1 e2e = 331; the never-pinned tint path of the pinned reveal family — the hovered accent tint rgb(245,245,245) + the accent-foreground color byte-identical both sides; the ALPHA-MODIFIER VALUE-ONLY mutation sole-failure verified live — the 1-line diff exactly as designed) + the baseline fully green on the first chain (the CARRIED-OVER workspace — the v127 environment persisted, the repo refreshed via git pull) + the browser-daemon exhaustion incident reaped (the stale v127 agent-browser trees + the stale :3000 server — the v128 lesson) + the VLM pair both passes DIFFERENT (every flag in the documented classes; no FAB claim) + the census 120 axes — 80 identical + 40 documented, ZERO new (the v122 values reproduced EXACTLY) + the screenshots 16/16 byte-identical (the same-day law). |"
README_ANCHOR = "the census 187 axes — 163 identical + 24 documented, ZERO new (the v121 values reproduced EXACTLY) + the screenshots 10 byte-identical + 6 refreshed (the seed-relative-date class). |"
ok = ok and insert_after("README.md", README_ANCHOR, V128_ROW,
             "remediation-plan-v128.md")

# ---------------- D4: SKILL.md ----------------
ok = ok and replace1("zero-balance_SKILL.md",
    "project_state: 108 unit tests / 330 e2e tests / 35 smoke steps — all green",
    "project_state: 108 unit tests / 331 e2e tests / 35 smoke steps — all green")
S163_ROW = "\n| 2026-10-27 | Session 163 — parity iteration v128 (`docs/remediation-plan-v128.md`) | **The re-run cycle's next-oldest candidate (the v122-era SAVINGS pair's ELEVENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128] — the SAVINGS view at desktop 1280x800 full-page; the FIFTY-FIRST consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly, the era chain traced through the lineage headers)** + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — nineteenth re-check) + the 122nd standing checks (ALL GREEN — the reference's four bugs live, the mobile menu the 122nd consecutive pass, zero overflow at 390) + the VLM pair (both passes DIFFERENT — every flag in the documented classes: seed-count, the v57 data-conditional payment chips, classification-value badges, user-identity avatar, seed-data; no FAB claim) + the two-half census (120 axes — 80 identical + 40 documented, ZERO new — the v122 values reproduced EXACTLY, the single-block md5 891ab9b6 lineage verified three-way) + the savings goal-card KEBAB-TRIGGER's OWN-HOVER END-STATE census pin at 1280 (PIN-ONLY — the never-pinned tint path of the pinned reveal family; the both-sides census byte-identical on the ladder — the hovered accent tint rgb(245,245,245) + the accent-foreground color rgb(23,23,23); the ALPHA-MODIFIER VALUE-ONLY mutation sole-failure verified live — the 1-line diff exactly as designed; +1 e2e = 331) + the ship chain fully green (331 e2e zero flakes [334 executions], 35/35 smoke, the screenshots 16/16 byte-identical [the same-day law], the dev evidence 4/4 + VLM-verified) |** 108/331/35 green — the workspace the CARRIED-OVER class (the browser-daemon reap lesson) |"
SKILL_ANCHOR = "|** 108/330/35 green — the workspace the RE-PROVISIONED class (fresh clone, the v108 lesson end-to-end) |"
ok = ok and insert_after("zero-balance_SKILL.md", SKILL_ANCHOR, S163_ROW,
             "Session 163 — parity iteration v128")

# ---------------- D5: PAD ----------------
PAD_V185 = """#### Revision Block — v1.1.85 (Tracked Changes)
- `[UI]` v1.1.85 (2026-10-27) — the v128 parity iteration (**PIN-ONLY — zero production-code changes** + one e2e pin; no dependency change): the counts 108 unit / **331 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v122-era SAVINGS pair's ELEVENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128] — the SAVINGS view at desktop 1280x800 full-page; the FIFTY-FIRST consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly, the era chain traced through the lineage headers)**; the baseline fully green on the first chain (the CARRIED-OVER workspace — the v127 environment persisted, the repo refreshed via git pull; the browser-daemon exhaustion incident reaped — the stale v127 agent-browser trees + the stale :3000 server SIGKILLed, the memory recovered 1155→2545MB available — the v128 lesson: a carried-over workspace inherits the prior cycle's browser daemons, reap them before the probe series); the VLM pair **both passes DIFFERENT — every flag in the documented classes** (seed-count, the v57 data-conditional payment chips, classification-value badges, user-identity avatar, seed-data; no FAB claim — no disproof needed); the two-half census (the single-block v122 lineage, md5 891ab9b6 verified three-way) **120 axes — 80 identical + 40 documented-class deltas, ZERO new** (the v122 values reproduced EXACTLY); **THE PIN — the savings goal-card KEBAB-TRIGGER's OWN-HOVER END-STATE census at 1280** (the never-pinned TINT PATH of the pinned reveal family: the v45/v36/v116/v122/v98 pins hold the reveal family's OPACITY paths + the at-rest/open chrome; the trigger's own-hover tint [hover:bg-accent, item-card.tsx:139 — the file's sole occurrence] + color [hover:text-accent-foreground] held by NO spec at ANY viewport; the both-sides census: **the own-hovered state {opacity 1 + bg rgb(245,245,245) + color rgb(23,23,23) + hoverMatch + cardHover} byte-identical both sides** — the ladder at-rest → hovered → restored identical; **the ALPHA-MODIFIER VALUE-ONLY mutation [hover:bg-accent→hover:bg-accent/50 at item-card.tsx:139 — line-scoped, every other reveal-path pin structurally immune, the a11y gate immune, the networth twins untouched] sole-failure verified live — the 1-line deep-equality diff exactly as designed, the items file's 49 others + the networth immunity file green**); the ship chain 331 e2e zero flakes (334 executions in 4 chunks) + 35/35 smoke + the screenshots 16/16 byte-identical (the same-day law — no refresh) + the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true).
"""
ok = ok and insert_before("Project_Architecture_Document.md",
    "#### Revision Block — v1.1.84 (Tracked Changes)",
    PAD_V185,
    "Revision Block — v1.1.85")

print("D1-D5:", "ALL ALIGNED" if ok else "FAILURES PRESENT")
sys.exit(0 if ok else 1)
