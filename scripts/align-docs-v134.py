#!/usr/bin/env python3
"""Align the docs for the v134 cycle (Session 169).

D1  AGENTS.md     — the v134 paragraph appended after the v133 paragraph
                    (the anchor carries the v133-unique dev-shots-derivation
                    tokens "derived v132→v133")
D2  CLAUDE.md     — the E2E count 336 -> 337 + the v134 clause
D3  README.md     — the count strings 336 -> 337 (two places) + the v134
                    plan row appended after the v133 row (the anchor
                    disambiguated by the v133-unique date-class tokens)
D4  SKILL.md      — project_state 336 -> 337 + the Session 169 row appended
                    after the Session 168 row
D5  PAD           — the [UI] v1.1.91 revision block (inserted newest-first,
                    BEFORE the v1.1.90 block)
D6  probe README  — the v134 section + the v135 queue   [align-probereadme-v134.py]
D7  session_327.md + the worklog Session 169 entry (separate steps)

D0 checked clean: every insert anchor below verified 1-hit before any write
(the AGENTS anchor by the v133-unique dev-shots tokens; the README anchor
by the v133-unique date-class tokens; the CLAUDE anchor by the v133-unique
post-restore-regression tokens; the SKILL anchor by the S168-unique
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
V134_AGENTS = """

Reference surfaces pinned by the v134 iteration (`docs/remediation-plan-v134.md`) — **the re-run cycle's next-oldest candidate (the v128-era SAVINGS pair — the SAVINGS view at desktop 1280x800 FULL-PAGE, the v58-era savings pair's surface family, the pair's TWELFTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128 → v134], the FIFTY-SEVENTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly: the ELEVENTH ordinal recorded in the v128 plan's own F3 record on its 12-entry bracket [v58 the original, one entry] → v134 = the TWELFTH, no prose/header conflict; the v128 shots header carries the SHORT form — the documented verification source)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only canary prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds — one node_modules/axe-core entry verified live, the eslint-plugin-jsx-a11y dependency deduped to the same copy) + the npm-audit watch at its twenty-fifth re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 128th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 128th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). **The baseline GREEN (one unreproduced intermittent, documented — the not-found:111 head-parity test failed 2 of the first 4 chunk-4 executions of the freshly-provisioned workspace, unreproduced in 13+ subsequent runs incl. --trace on; every asserted axis a root-layout static; the watch entered — the flake stayed green through the v134 ship chain) (the PIN-ONLY form, the v128/v129/v130/v131/v132/v133 class — the SIXTH consecutive PIN-ONLY cycle)** (the RE-PROVISIONED workspace — the fresh clone from main @ a739c50, the v108 lesson end-to-end: npm ci in the foreground, the zod extraction intact, BOTH chromium pairs [the fresh cache held only the OLD 1200 pair — the 1243 pair installed], the .env + db/ provisioned, db:push + db:seed, the seedcheck exact before any gate; lint · typecheck · 108 unit · build [robots + sitemap prerendered] · 336 e2e [339 executions in 4 chunks = 335 spec + 1 setup — the count derived authoritatively via --list before any chunk ran: 93/90/74/82] · 35/35 smoke; the production-seam audit clean + the v133 pin verified in place). The probe series derived from the v128 lineage (derive-v134-series.py — FOUR explicit session-token families [refvlm/clonevlm + refarbit/clonearbit arbit — the arbit tokens carry '128' without the 'v' prefix] + FOUR history-correction fragments [the era marker last-re-shot v122→v128 + the oldest-remaining list, the plan pointer + the agreement ordinal FIFTY-FIRST→FIFTY-SEVENTH in the SHORT-form shots header, the ordinal ELEVENTH→TWELFTH + the bracket extension in the three bracket-carrying files], zero residual, line counts preserved 50/42/39/262) + the ONE-block two-half contract verified three-way (verify-twohalf-v134.py — SV_CENSUS_JS 153 lines md5 891ab9b6, the v122/v128 lineage value VERBATIM; the builder derivation's own residual gate caught the bare refarbit128 token on the first run — the EXPLICIT session-family swap added, the no-'v'-prefix lesson re-confirmed; the v128-lineage builder extracts ALL blocks from the source arbit file — no embedded clone_login, no stale-session fix needed) + the comparator derived (the two provenance citations re-pointed at the v128 measurement; residual clean, line-count preserved 143). **The VLM verdict — DIFFERENT ×2, THE SAVINGS PAIR's CONSISTENT FORM** (the same verdict family as the v122/v128 re-runs; every flag in the documented classes, arbitration-free: the card-grid layout the SEED-COUNT class, the footer payment chips the v57 DATA-CONDITIONAL class, the badge family the classification-VALUE + v57 wrap classes, the header stats the seed-data classes, the avatar the USER-IDENTITY class). The both-sides census compared AXIS-BY-AXIS by the persisted compare-v134-census.py (**120 axes: 80 identical + 40 documented-class deltas, ZERO new** — REPRODUCING the v128 census values EXACTLY: the same 120/80/40 split, zero drift on every axis). **THE PIN — the SAVINGS GOAL-CARD KEBAB-TRIGGER's FOCUS-VISIBLE LADDER at 1280 (+1 e2e = 337; PIN-ONLY — src/ zero changes)**: the candidate survey (the savings surface's interaction families swept — the Add button INERT by design [the v11 G4 record], the combobox own-hover INERT both sides [measured live], the search-focus savings twin REJECTED on the shared-component mutation collision [the v37 S2 income pin — the sole-failure discipline unsatisfiable], the kebab's focus ring held by NO spec at ANY viewport [the v36 S3 pin holds {fv, opacity} only on /income; the v45/v116/v122/v128 pins hold the at-rest/card-hover/own-hover/open states] and the savings keyboard path entirely unpinned); the both-sides one-shot census focusladder-arbit-v134.sh (the v133 itemhover form adapted to the KEYBOARD ladder — the SAME-LABEL Emergency Fund target, the STRUCTURAL tag-agnostic finder [the reference's trigger is unlabelled — the v98 record], the FINDER-BOUNDED REAL Tab walk [never a hardcoded count; the sites' stop orders differ — REF 10 stops / CLONE 11; NEVER pressing Enter — the menu opens on click/Enter, both out of bounds], the landing probe returning a PLAIN unquoted token — immune to the bash-quoted-JSON escaping that defeated the first run's grep, the fix verified live, READ-ONLY per the v46 rule) measured the ladder **clean on both sides** — at-rest {opacity 0, boxShadow none} IDENTICAL → FOCUSED: REF {fv true, opacity "0" [the v36 S3 superset class], the ring computed-present [the white lead + rgb(10,10,10) 0px 0px 0px 1px, visually masked]} vs CLONE {fv true, opacity "1" [the keyboard-reveal superset], bg transparent [focus ≠ hover], the SAME VISIBLE ring layer rgb(10,10,10) 0px 0px 0px 1px} — the lead-slot count differs by construction (the v3 3-slot vs the TW v4 5-slot, the v37 S1/v95 documented class) → blurred restored IDENTICAL — **no gap, no repair**; the pin (append-pin-v134.py — the REAL Playwright Tab walk to the Emergency Fund trigger, the V94-COLLISION-safe axis set [the end-states alone; the transition metadata + the lead-slot construct deliberately not pinned]; the typecheck Element→HTMLElement narrowing fix applied in-passing [the as-HTMLElement cast], the persisted append script synced) GREEN on the first run; **THE PIN-SANITY MUTATION — the line-139-scoped value-only form (focus-visible:ring-1 → focus-visible:ring-2, the kebab trigger's ring width alone; the :100/:109 Edit/Calculate twins untouched by line-scoping — the v28 G2 class assertions immune; the v36 S3 pin immune by construction [it asserts {fv, opacity} only, never the ring])**: the SOLE FAILURE verified live — 1 failed [the pin] + 3 passed in the family grep [the v36 S3 + v128 kebab + v133 action-button pins immune] + 1 failed + 51 passed in the FULL items sweep, the diff EXACTLY the predicted ring-width line [rgb(10,10,10) 0px 0px 0px 1px → 2px; fv + opacity 1 + bg transparent preserved, the at-rest + blurred rungs UNAFFECTED]; restored (git diff src/ = 0 lines) + the FULL REBUILD + the 160/160 post-restore regression (items 51 + dashboard 50 + networth 38 + calculator 20 — the v130/v131/v132/v133 pins' different-file immunity verified live). The ship chain 337 e2e zero flakes (93+91+74+82 = 340 executions = 337 unique — the not-found flake-watch test green); 35/35 smoke; **the screenshots 16/16 — 10 byte-identical + 6 the DETERMINISTIC CROSS-DAY SEED refresh (the fresh re-provisioning re-seeded Oct 29 vs v133's Oct 28 seed — every relative isoDate(-N) shifted +1 day; the changed set EXACTLY the date-bearing surfaces 03/04/05/06 the item views + 08 the calculator + 16 the details; 07 byte-identical — the same-UTC-day capture law holds, the modal's todayIso default unchanged)**; the dev evidence 4/4 (3 byte-identical + dev-mobile-income-390 the date-class twin) + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the dev-shots scripts derived v133→v134 with the version-swap-only verification)."""
AGENTS_TAIL = "the dev-shots scripts derived v132→v133 with the version-swap-only verification)."
ok = ok and insert_after("AGENTS.md", AGENTS_TAIL, V134_AGENTS,
             "Reference surfaces pinned by the v134 iteration")

# ---------------- D2: CLAUDE.md ----------------
ok = ok and replace1("CLAUDE.md",
    "- **E2E (Playwright, 336)**:",
    "- **E2E (Playwright, 337)**:")
ok = ok and insert_after("CLAUDE.md",
    "the post-restore regression 159/159)",
    "; the v134 pin — the SAVINGS goal-card kebab's focus-visible ladder at 1280 (PIN-ONLY — src/ zero changes: the both-sides census focusladder-arbit-v134.sh measured the keyboard ladder clean — the ring layer rgb(10,10,10) 0px 0px 0px 1px computed-parity both sides, the reveal the v36 S3 superset class [REF opacity 0 / CLONE opacity 1], the outer rungs identical; the line-139-scoped ring-width mutation sole-failure verified live [1 failed + 51 passed in the full items sweep, the diff exactly the predicted ring-width line]; the post-restore regression 160/160)",
    "the v134 pin — the SAVINGS goal-card kebab's focus-visible ladder")

# ---------------- D3: README.md ----------------
ok = ok and replace1("README.md",
    "│   └── 📂 e2e/                    # Playwright specs (336 tests) + global setup",
    "│   └── 📂 e2e/                    # Playwright specs (337 tests) + global setup")
ok = ok and replace1("README.md",
    "npm run test:e2e    # Playwright e2e (336 tests) — needs `npm run build` first",
    "npm run test:e2e    # Playwright e2e (337 tests) — needs `npm run build` first")
V134_ROW = "\n| [`docs/remediation-plan-v134.md`](docs/remediation-plan-v134.md) | **The re-run cycle's next-oldest candidate (the v128-era SAVINGS pair's TWELFTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128 → v134] — the SAVINGS view at desktop 1280x800 FULL-PAGE; the FIFTY-SEVENTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly, the ELEVENTH ordinal recorded in the v128 plan's own F3 record [the shots header carries the SHORT form])** + the axe watch (NO DRIFT — 4.14.0 holds) + the npm-audit watch (0 vulnerabilities, twenty-fifth re-check) + the 128th standing checks (ALL GREEN — the mobile menu the 128th consecutive pass) + the VLM pair **DIFFERENT ×2 — the savings pair's consistent form** (every flag in the documented classes, arbitration-free) + the census 120 axes — 80 identical + 40 documented, ZERO new (the v128 values reproduced EXACTLY) + **the savings goal-card kebab's focus-visible ladder pin at 1280 (+1 e2e = 337; PIN-ONLY — the both-sides census measured the keyboard ladder clean [the ring layer computed-parity, the reveal the v36 S3 superset class]; the line-139-scoped ring-width mutation sole-failure verified live)** + THE FLAKE NOTE (the not-found:111 intermittent — 2 early failures post-provisioning, unreproducible in 13+ runs, the watch entered, green through the ship chain) + the screenshots 16/16 — 10 byte-identical + 6 the deterministic cross-day seed refresh (the re-seed's isoDate(-N) shift; 07 byte-identical — the same-UTC-day capture law). |"
README_ANCHOR = "the sole live-today-bearing surface). |"
ok = ok and insert_after("README.md", README_ANCHOR, V134_ROW,
             "remediation-plan-v134.md")

# ---------------- D4: SKILL.md ----------------
ok = ok and replace1("zero-balance_SKILL.md",
    "project_state: 108 unit tests / 336 e2e tests / 35 smoke steps — all green",
    "project_state: 108 unit tests / 337 e2e tests / 35 smoke steps — all green")
S169_ROW = "\n| 2026-10-29 | Session 169 — parity iteration v134 (`docs/remediation-plan-v134.md`) | **The re-run cycle's next-oldest candidate (the v128-era SAVINGS pair's TWELFTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128 → v134] — the SAVINGS view at desktop 1280x800 FULL-PAGE; the FIFTY-SEVENTH consecutive queue/ledger agreement)** + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — twenty-fifth re-check) + the 128th standing checks (ALL GREEN — the reference's four bugs live, the mobile menu the 128th consecutive pass, zero overflow at 390) + the VLM pair **DIFFERENT ×2 — the savings pair's consistent form** (every flag in the documented classes, arbitration-free: the seed-count card grid, the v57 data-conditional payment chips, the classification-value + wrap badge classes, the user-identity avatar) + the two-half census (120 axes — 80 identical + 40 documented, ZERO new — the v128 values reproduced EXACTLY, the ONE-block md5 891ab9b6 lineage verified three-way) + **the savings goal-card kebab's focus-visible ladder pin at 1280 (PIN-ONLY — src/ zero changes: the candidate survey found the focus ring held by no spec at any viewport [the v36 S3 pin holds {fv, opacity} only] and the savings keyboard path unpinned; the both-sides census focusladder-arbit-v134.sh measured the ladder clean [the ring layer rgb(10,10,10) 0px 0px 0px 1px computed-parity both sides, the reveal the v36 S3 superset class (REF opacity 0 / CLONE opacity 1), the at-rest + blurred rungs identical]; the finder-bounded REAL Tab walk [REF 10 stops / CLONE 11, never Enter]; the line-139-scoped ring-width mutation sole-failure verified live — 1 failed + 51 passed in the full items sweep, the diff exactly the predicted ring-width line; the post-restore regression 160/160; +1 e2e = 337)** + the ship chain fully green (337 e2e zero flakes [340 executions] — the not-found flake-watch green, 35/35 smoke, the screenshots 16/16 [10 byte-identical + 6 the deterministic cross-day seed refresh], the dev evidence 4/4 + VLM-verified) |** 108/337/35 green — the workspace the RE-PROVISIONED class (the resource discipline between the halves; the not-found:111 flake documented, the watch entered) |"
SKILL_ANCHOR = "|** 108/336/35 green — the workspace the CONTINUING class (the resource discipline between the halves) |"
ok = ok and insert_after("zero-balance_SKILL.md", SKILL_ANCHOR, S169_ROW,
             "Session 169 — parity iteration v134")

# ---------------- D5: PAD ----------------
PAD_V191 = """#### Revision Block — v1.1.91 (Tracked Changes)
- `[UI]` v1.1.91 (2026-10-29) — the v134 parity iteration (**PIN-ONLY — src/ zero changes** + one e2e pin; no dependency change): the counts 108 unit / **337 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v128-era SAVINGS pair's TWELFTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128 → v134] — the SAVINGS view at desktop 1280x800 FULL-PAGE; the FIFTY-SEVENTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly)**; the baseline green (the RE-PROVISIONED workspace — the fresh-clone class, the v108 lesson end-to-end; ONE unreproduced intermittent documented [the not-found:111 head-parity test — 2 early failures post-provisioning, unreproducible in 13+ subsequent runs incl. --trace on, every asserted axis a root-layout static; the watch entered, green through the ship chain]); the VLM pair **DIFFERENT ×2 — the savings pair's consistent form** (every flag in the documented classes, arbitration-free); the two-half census (the ONE-block v128 lineage, md5 891ab9b6 verified three-way) **120 axes — 80 identical + 40 documented-class deltas, ZERO new** (the v128 values reproduced EXACTLY); **the savings goal-card kebab's focus-visible ladder pin at 1280**: the candidate survey (the savings surface's interaction families swept — the Add button INERT by design, the combobox own-hover INERT both sides, the search-focus twin rejected on the shared-component mutation collision; the kebab's focus ring held by no spec at any viewport) + the both-sides census **clean** (the ring layer computed-parity — rgb(10,10,10) 0px 0px 0px 1px both sides; the reveal the v36 S3 superset class; the outer rungs identical; no gap, no repair) + the pin (the REAL Tab walk, the V94-COLLISION-safe axis set) + **the line-139-scoped ring-width mutation sole-failure verified live — 1 failed + 51 passed in the full items sweep [the v36 S3 + v28 G2 + v128 pins immune], the diff exactly the predicted ring-width line [rgb(10,10,10) 0px 0px 0px 1px → 2px]** + restored + the 160/160 post-restore regression; the ship chain 337 e2e zero flakes (340 executions in 4 chunks) + 35/35 smoke + the screenshots 16/16 (10 byte-identical + 6 the deterministic cross-day seed refresh — the re-seed's isoDate(-N) shift, 07 byte-identical per the same-UTC-day capture law) + the dev evidence 4/4 + VLM-verified (the menu proof: /income, docSW 390, navLandmark true).
"""
ok = ok and insert_before("Project_Architecture_Document.md",
    "#### Revision Block — v1.1.90 (Tracked Changes)",
    PAD_V191,
    "Revision Block — v1.1.91")

print("D1-D5:", "ALL ALIGNED" if ok else "FAILED")
sys.exit(0 if ok else 1)
