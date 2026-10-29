#!/usr/bin/env python3
"""Align the docs for the v133 cycle (Session 168).

D1  AGENTS.md     — the v133 paragraph appended after the v132 paragraph
                    (the anchor carries the v132-unique dev-shots-derivation
                    tokens "derived v131→v132")
D2  CLAUDE.md     — the E2E count 335 -> 336 + the v133 clause
D3  README.md     — the count strings 335 -> 336 (two places) + the v133
                    plan row appended after the v132 row (the anchor
                    disambiguated by the v132-unique date-class tokens)
D4  SKILL.md      — project_state 335 -> 336 + the Session 168 row appended
                    after the Session 167 row
D5  PAD           — the [UI] v1.1.90 revision block (inserted newest-first,
                    BEFORE the v1.1.89 block)
D6  probe README  — the v133 section + the v134 queue   [align-probereadme-v133.py]
D7  session_323.md + the worklog Session 168 entry (separate steps)

D0 checked clean: every insert anchor below verified 1-hit before any write
(the AGENTS anchor by the v132-unique dev-shots tokens; the README anchor
by the v132-unique date-class tokens; the CLAUDE anchor by the v132-unique
post-restore-regression tokens; the SKILL anchor by the S167-unique
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
V133_AGENTS = """

Reference surfaces pinned by the v133 iteration (`docs/remediation-plan-v133.md`) — **the re-run cycle's next-oldest candidate (the v127-era ITEMS pair — the ITEMS view [INCOME + EXPENSES] at desktop 1280x800 FULL-PAGE, the v57-era items pair's surface family, the pair's TWELFTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133], the FIFTY-SIXTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly: the ELEVENTH ordinal stated in vlm-shots-v127.sh's own header on its 12-entry bracket [v57 the original, one entry] → v133 = the TWELFTH, no prose/header conflict)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only canary prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds — one node_modules/axe-core entry verified live) + the npm-audit watch at its twenty-fourth re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 127th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 127th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). **The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs (the PIN-ONLY form, the v128/v129/v130/v131/v132 class — the FIFTH consecutive PIN-ONLY cycle)** (the CONTINUING workspace — the v132 cycle's own sandbox workspace persisted: the working tree clean at dd3bdc5, the pull fast-forwarding one doc file [session_322.md]; the v132 provisioning intact [node_modules, BOTH chromium pairs, the .env + db/ at the root], the seedcheck exact before any gate 7/1850/2235/0/3/2; lint · typecheck · 108 unit [the count derived via vitest list] · build [robots + sitemap prerendered] · 335 e2e zero flakes [338 executions in 4 chunks = 334 spec + 1 setup — the count derived authoritatively via --list before any chunk ran: 93/89/74/82] · 35/35 smoke; the production-seam audit clean + the v132 pin verified in place). The probe series derived from the v127 lineage (derive-v133-series.py — FOUR explicit session-token families [refvlm/clonevlm + refarbit/clonearbit arbit — the arbit tokens carry '127' without the 'v' prefix] + FOUR history-correction fragments [the era marker last-re-shot v121→v127, the ordinal ELEVENTH→TWELFTH + the bracket extension in all four files, the later-pairs list re-pointed at the CURRENT later re-runs {savings v128, login+calculator v129, networth+drill-down v130, budget-guidelines+quick-action v131, mobile twins v132}], zero residual, line counts preserved 57/49/50/285) + the ONE-block two-half contract verified three-way (verify-twohalf-v133.py — CENSUS_JS 193 lines md5 b55dcd29, the v103/v109/v115/v121/v127 lineage value VERBATIM; the builder's embedded clone_login stale `clonearbit127` session token bumped to `clonearbit133` — the v121 stale-session-fix precedent, the v132 form applied to the items lineage) + the comparator derived (the generic swap + the two provenance citations re-pointed at the v127 measurement; residual clean, line-count preserved 136). **The VLM verdict — BOTH PAIRS DIFFERENT ×2, THE CONSISTENT FORM** (within the pair's documented verdict-VARIATION family [the v105/v121/v127 precedent]; every flag in the documented classes, arbitration-free: the avatar letter the USER-IDENTITY class, the card-grid childCount + the header stats + the item texts/amounts/dates/badges the SEED-COUNT/seed-data classes, the expenses footer payment-method chips the v57 DATA-CONDITIONAL class, the badge multi-line wrap + the card height the v57 wrap/classification-VALUE + v70b-decomposed classes — no layout/style flag beyond the documented classes in either pass). The both-sides census compared AXIS-BY-AXIS by the persisted compare-v133-census.py (**187 axes: 163 identical + 24 documented-class deltas, ZERO new** — REPRODUCING the v127 census values EXACTLY: the same 187/163/24 split, zero drift on every axis). **THE PIN — the ITEM-CARD ACTION BUTTONS' OWN-HOVER LADDERS at 1280 (+1 e2e = 336; PIN-ONLY — src/ zero changes)**: the candidate survey (the action-button family's coverage map — the v45 F1b pin holds the at-rest chrome + the row reveal + the buttons' at-rest shadow-md, the v28 G2 pin the Edit's hover:text CLASS TOKEN + the focus families, the v36 S3 the Tab walk, the v127 pin the badge's hover path [a different element in the same card]; the hovered computed end-states held by NO spec on THIS file at ANY viewport; the live survey probes finding the reference's first expense card carries exactly TWO action buttons [Edit 77×32 + Calculate 110×32 — NO kebab; the kebab is the clone's superset #7 on non-expense cards only] with the row's own group-hover reveal [opacity 0 at rest → 1 on card hover], and the reference's own-hover values: Edit → bg rgb(249,250,251) + color rgb(23,23,23), Calculate → bg rgb(255,247,237) — the clone's utilities map exactly [--color-accent-foreground: #171717 = rgb(23,23,23)]); the both-sides one-shot census itemhover-arbit-v133.sh (the v132 badgehover form's own shape adapted to the TWO-button ladder — TAG-AGNOSTIC finders [button/[role=button] by text + the state-independent radius-6px/fs-12px guards], the first expense card's grid-cols-3 first child on BOTH sides, the (5,5)-parked ladder, the live-read centers, READ-ONLY per the v46 rule — the buttons OPEN dialogs on click, never clicked) measured the ladders **BYTE-IDENTICAL both sides** — at-rest {both white, rowOpacity 0} → EDIT OWN-HOVERED {bg rgb(249,250,251) + color rgb(23,23,23), rowOpacity 1} → CALC OWN-HOVERED {bg rgb(255,247,237), the orange color unchanged, rowOpacity 1} → restored, the transitionDuration 0.15s identical, the w pair the label-dependent 2px delta family (deliberately not pinned) — **no gap, no repair**; the pin (append-pin-v133.py — the first expense card's Edit + Calculate ladders at 1280×800, the V94-COLLISION-safe axis set [the end-states alone, the transition metadata + the label-dependent w deliberately not pinned]) GREEN on the first run; **THE PIN-SANITY MUTATION — the line-100-scoped value-only form (hover:bg-[#f9fafb] → hover:bg-[#f9fafc], the Edit button's hover-bg utility alone; the dashboard-view.tsx:309 twin untouched by the file+line scoping; the v28 G2 class assertions immune — hover:text-accent-foreground untouched)**: the SOLE FAILURE verified live — 1 failed [the pin] + 2 passed in the family grep + 1 failed + 50 passed in the FULL items sweep, the deep-equality diff EXACTLY the predicted hovered-bg line [rgb(249,250,251) → rgb(249,250,252); hoverMatch true + the color axis preserved, the at-rest + restored rungs + the calc ladder UNAFFECTED]; restored (git diff src/ = 0 lines) + the FULL REBUILD + the 159/159 post-restore regression (items 50 + dashboard 50 + networth 38 + calculator 20 — the v130/v131/v132 pins' different-file immunity verified live). The ship chain 336 e2e zero flakes (93+90+74+82 = 339 executions = 336 unique); 35/35 smoke; **the screenshots 16/16 — 15 byte-identical + 07 the DETERMINISTIC CROSS-DAY DATE-CLASS refresh (the add-item modal's todayIso() default, Oct 28 → Oct 29 — the sole live-today-bearing captured surface; the db the CONTINUING workspace's unchanged seed, so the seeded-date surfaces byte-identical; the calculator capture carries no live-today surface in view — byte-identical)**; the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the dev-shots scripts derived v132→v133 with the version-swap-only verification)."""
AGENTS_TAIL = "the dev-shots scripts derived v131→v132 with the version-swap-only verification)."
ok = ok and insert_after("AGENTS.md", AGENTS_TAIL, V133_AGENTS,
             "Reference surfaces pinned by the v133 iteration")

# ---------------- D2: CLAUDE.md ----------------
ok = ok and replace1("CLAUDE.md",
    "- **E2E (Playwright, 335)**:",
    "- **E2E (Playwright, 336)**:")
ok = ok and insert_after("CLAUDE.md",
    "the post-restore regression 158/158)",
    "; the v133 pin — the ITEM-CARD ACTION BUTTONS' own-hover ladders at 1280 (PIN-ONLY — src/ zero changes: the both-sides census itemhover-arbit-v133.sh measured the two-button ladder byte-identical — at-rest {both white, row 0} → the Edit own-hovered {bg rgb(249,250,251) + color rgb(23,23,23)} → the Calculate own-hovered {bg rgb(255,247,237)} → restored; the reference's card carries the same two buttons + the same group-hover reveal — a both-sides parity axis; the line-100-scoped value-only mutation [hover:bg-[#f9fafb] → hover:bg-[#f9fafc]] sole-failure verified live [1 failed + 50 passed in the full items sweep, the diff exactly the predicted hovered-bg line]; the post-restore regression 159/159)",
    "the v133 pin — the ITEM-CARD ACTION BUTTONS' own-hover ladders")

# ---------------- D3: README.md ----------------
ok = ok and replace1("README.md",
    "│   └── 📂 e2e/                    # Playwright specs (335 tests) + global setup",
    "│   └── 📂 e2e/                    # Playwright specs (336 tests) + global setup")
ok = ok and replace1("README.md",
    "npm run test:e2e    # Playwright e2e (335 tests) — needs `npm run build` first",
    "npm run test:e2e    # Playwright e2e (336 tests) — needs `npm run build` first")
V133_ROW = "\n| [`docs/remediation-plan-v133.md`](docs/remediation-plan-v133.md) | **The re-run cycle's next-oldest candidate (the v127-era ITEMS pair's TWELFTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133] — the ITEMS view [income + expenses] at desktop 1280x800 FULL-PAGE; the FIFTY-SIXTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly, the ELEVENTH ordinal stated in vlm-shots-v127.sh's own header)** + the axe watch (NO DRIFT — 4.14.0 holds) + the npm-audit watch (0 vulnerabilities, twenty-fourth re-check) + the 127th standing checks (ALL GREEN — the mobile menu the 127th consecutive pass) + the VLM pair **BOTH PAIRS DIFFERENT ×2 — the consistent form, within the pair's documented verdict-VARIATION family** (every flag in the documented classes, arbitration-free) + the census 187 axes — 163 identical + 24 documented, ZERO new (the v127 values reproduced EXACTLY) + **the item-card action buttons' own-hover ladders pin at 1280 (+1 e2e = 336; PIN-ONLY — the both-sides census measured the ladders byte-identical, no repair; the line-100-scoped value-only mutation sole-failure verified live)** + the screenshots 16/16 — 15 byte-identical + 07 the deterministic cross-day date-class refresh (the modal's todayIso default — the sole live-today-bearing surface). |"
README_ANCHOR = "no date-class refresh this cycle). |"
ok = ok and insert_after("README.md", README_ANCHOR, V133_ROW,
             "remediation-plan-v133.md")

# ---------------- D4: SKILL.md ----------------
ok = ok and replace1("zero-balance_SKILL.md",
    "project_state: 108 unit tests / 335 e2e tests / 35 smoke steps — all green",
    "project_state: 108 unit tests / 336 e2e tests / 35 smoke steps — all green")
S168_ROW = "\n| 2026-10-29 | Session 168 — parity iteration v133 (`docs/remediation-plan-v133.md`) | **The re-run cycle's next-oldest candidate (the v127-era ITEMS pair's TWELFTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133] — the ITEMS view [income + expenses] at desktop 1280x800 FULL-PAGE; the FIFTY-SIXTH consecutive queue/ledger agreement)** + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — twenty-fourth re-check) + the 127th standing checks (ALL GREEN — the reference's four bugs live, the mobile menu the 127th consecutive pass, zero overflow at 390) + the VLM pair **BOTH PAIRS DIFFERENT ×2 — the consistent form, within the pair's documented verdict-VARIATION family** (every flag in the documented classes, arbitration-free: the user-identity avatar, the seed-count/seed-data grid + stats + texts, the v57 data-conditional payment chips, the v57 wrap + v70b card-height classes) + the two-half census (187 axes — 163 identical + 24 documented, ZERO new — the v127 values reproduced EXACTLY, the ONE-block md5 b55dcd29 lineage verified three-way; the builder's stale clonearbit127 session token bumped to clonearbit133) + **the item-card action buttons' own-hover ladders pin at 1280 (PIN-ONLY — src/ zero changes: the candidate survey found the hovered computed end-states held by no spec on this file at any viewport — the v28 G2 pin holds the class token only; the live survey probes found the reference's card carries exactly two action buttons, no kebab; the both-sides census itemhover-arbit-v133.sh measured the ladders byte-identical [at-rest → the Edit own-hovered {bg rgb(249,250,251) + color rgb(23,23,23)} → the Calculate own-hovered {bg rgb(255,247,237)} → restored; the row 0→1→1→0]; the line-100-scoped value-only mutation sole-failure verified live — 1 failed + 50 passed in the full items sweep, the diff exactly the predicted hovered-bg line; the post-restore regression 159/159; +1 e2e = 336)** + the ship chain fully green (336 e2e zero flakes [339 executions], 35/35 smoke, the screenshots 16/16 [15 byte-identical + 07 the deterministic cross-day date-class refresh], the dev evidence 4/4 + VLM-verified) |** 108/336/35 green — the workspace the CONTINUING class (the resource discipline between the halves) |"
SKILL_ANCHOR = "|** 108/335/35 green — the workspace the RE-PROVISIONED class (the resource discipline between the halves) |"
ok = ok and insert_after("zero-balance_SKILL.md", SKILL_ANCHOR, S168_ROW,
             "Session 168 — parity iteration v133")

# ---------------- D5: PAD ----------------
PAD_V190 = """#### Revision Block — v1.1.90 (Tracked Changes)
- `[UI]` v1.1.90 (2026-10-29) — the v133 parity iteration (**PIN-ONLY — src/ zero changes** + one e2e pin; no dependency change): the counts 108 unit / **336 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v127-era ITEMS pair's TWELFTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133] — the ITEMS view [income + expenses] at desktop 1280x800 FULL-PAGE; the FIFTY-SIXTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly)**; the baseline fully green on the first chain (the CONTINUING workspace — the v132 cycle's own workspace persisted, the pull fast-forwarding one doc file; the seedcheck exact before any gate; the resource discipline between the halves); the VLM pair **BOTH PAIRS DIFFERENT ×2 — the consistent form, within the pair's documented verdict-VARIATION family** (every flag in the documented classes, arbitration-free); the two-half census (the ONE-block v127 lineage, md5 b55dcd29 verified three-way; the builder's stale clonearbit127 session token bumped to clonearbit133) **187 axes — 163 identical + 24 documented-class deltas, ZERO new** (the v127 values reproduced EXACTLY); **the item-card action buttons' own-hover ladders pin at 1280**: the candidate survey (the action-button family's coverage map — the hovered computed end-states held by no spec on this file at any viewport; the live survey probes finding the reference's card carries exactly two action buttons + the same group-hover reveal — a both-sides parity axis) + the both-sides census **byte-identical** (no gap, no repair) + the pin (the V94-COLLISION-safe axis set — the end-states alone) + **the line-100-scoped value-only mutation sole-failure verified live — 1 failed + 50 passed in the full items sweep [the v28 G2 class assertions immune, the dashboard twin untouched by the file+line scoping], the diff exactly the predicted hovered-bg line [rgb(249,250,251) → rgb(249,250,252)]** + restored + the 159/159 post-restore regression; the ship chain 336 e2e zero flakes (339 executions in 4 chunks) + 35/35 smoke + the screenshots 16/16 (15 byte-identical + 07 the deterministic cross-day date-class refresh — the modal's todayIso default, the sole live-today-bearing surface) + the dev evidence 4/4 + VLM-verified (the menu proof: /income, docSW 390, navLandmark true).
"""
ok = ok and insert_before("Project_Architecture_Document.md",
    "#### Revision Block — v1.1.89 (Tracked Changes)",
    PAD_V190,
    "Revision Block — v1.1.90")

print("D1-D5:", "ALL ALIGNED" if ok else "FAILED")
sys.exit(0 if ok else 1)
