#!/usr/bin/env python3
"""D1-D5 docs alignment for the v116 cycle (the persisted alignment-script
precedent — the v115 cycle's align-docs-v115.py + p2 forms merged, WITH
the IDEMPOTENT-RUN DUPLICATION TRAP guard on every insert-after edit).

D1  AGENTS.md     — the v116 paragraph appended after the v115 paragraph
D2  CLAUDE.md     — the E2E count 318 -> 319 + the v116 clause appended to
                    the v115 clause's tail
D3  README.md     — the two (318 tests) counts -> 319 + the v116 plan row
                    appended after the v115 row
D4  SKILL.md      — project_state 318 -> 319 + the Session 151 row appended
D5  PAD           — the v1.1.73 revision block inserted before v1.1.72

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

# ---------------- D1: AGENTS.md ----------------
V116_AGENTS = """

Reference surfaces pinned by the v116 iteration (`docs/remediation-plan-v116.md`) — **the re-run cycle's next-oldest candidate (the v110-era SAVINGS pair — the SAVINGS view at desktop 1280×800 FULL-PAGE, the pair's NINTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116], the THIRTY-NINTH consecutive queue/ledger agreement)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, canary-only prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds; the engine-contract pin green) + the npm-audit watch at its seventh re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 110th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads [1 items USD 25,000 / 1 items USD 5000.00 / 4 items USD 525.00 — no render-race hit this cycle]; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 110th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). The verdict SAVINGS DIFFERENT — the pair's documented flag-set class (v104/v98/v110 read DIFFERENT; NO FAB flag raised this cycle — the disproof not required, the v103 standing class) — every flag DOM-arbitrated to a documented class: the card-footer payment chips the v57 DATA-CONDITIONAL class (the reference's savings item ships no paymentMethod — its footer renders the date-only DIV; the clone's carry them and render the SPAN pair the reference's own income card renders); the card grid the seed-count class (1 vs 2); the header stats + card contents the seed-data classes (the classification-VALUE badge colors locked by badge-colors.spec); the avatar the user-identity class. The both-sides census (SV_CENSUS_JS 153 lines, md5 891ab9b6 — the version-free v104/v110 census block carried over VERBATIM) compared AXIS-BY-AXIS by the persisted compare-v116-census.py (120 axes: 80 identical + 40 documented-class deltas, ZERO new — the avatar/h1/grid/card/titleRow/amount/footer/badges/badgeRow chrome all byte-identical) — NO NEW CLONE GAP. The +1 e2e pin (tests/e2e/items.spec.ts): the savings goal-card's KEBAB TRIGGER census at 1280 — the hover-revealed action element on the pair's OWN target surface, never pinned at ANY viewport in ANY spec (the tab-walk pin holds only the focus-path reveal; the v98 pin only the menu panel — the trigger's downstream; the v54/v51 pins only the 390 mobile census) — the at-rest unheld chrome {tag BUTTON/display flex/radius 6px/bg transparent/color rgb(10,10,10)/cardTop 21/cardRight 21} + the HOVER-path group-hover reveal {opacity "1"}; measured byte-identical both sides via the one-shot hover-arbit-v116.sh (the at-rest read with the pointer parked at (5,5), the hover read at the card's OWN center); mutation-verified single-axis (rounded-md → rounded-lg at item-card.tsx:139 line-scoped — only the v116 pin red at the radius family axis alone ["6px" → "8px"]; the v45 F1a pin — which holds the trigger's w/h/at-rest opacity on /income, the shared component — GREEN under the mutation); restored, rebuilt, post-restore 46/46 green. The cycle's TWO survey lessons: THE SPEC-ALIAS COVERAGE LESSON (the first mutation attempt [the h axis] failed the sole-failure test with TWO reds — the v45 F1a pin holds the trigger's w/h/at-rest opacity on /income, a hold the coverage map missed because it grepped the SOURCE tokens instead of the specs' own "kebab" alias; an axis held in ANY view is held for EVERY view of a shared component; the pin re-scoped to the unheld axes, the first mutation's two-red run kept as the collision evidence) and THE STATIC-HOVER-COORDINATE TRAP (the first hover read's static 640,300 missed the reference's ONLY card — its 1-item seed renders in grid COLUMN 1, x 288–597, and x=640 lands on the column-gap whitespace; the repair reads the card's own bounding rect and moves the pointer to the card's OWN center — both sides then byte-identical). The ship chain 319 e2e zero flakes (84+79+77+82 = 322 executions = 319 unique); 35/35 smoke; the screenshots 20/20 byte-identical (the same-day-seed law); the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the dev-shots scripts derived v115→v116 with the version-swap-only verification). The workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end (npm ci in the foreground + zod 840/840 + BOTH v1243 binaries DIRECT)."""
insert_after("AGENTS.md",
             "the dev-shots scripts derived v114→v115 with the version-swap-only verification).",
             V116_AGENTS,
             "Reference surfaces pinned by the v116 iteration")

# ---------------- D2: CLAUDE.md ----------------
replace1("CLAUDE.md", "- **E2E (Playwright, 318)**:", "- **E2E (Playwright, 319)**:")
V116_CLAUSE = " and the v116 savings goal-card kebab-trigger census at 1280 (the hover-revealed action element on the savings pair's own surface — the at-rest unheld chrome {tag/display/radius/bg/color/cardTop/cardRight} + the hover-path group-hover reveal {opacity \"1\", settled past the 150ms transition window}; the v45-held w/h/at-rest-opacity axes left OUT of the census return per the V94-COLLISION criterion — THE SPEC-ALIAS COVERAGE LESSON: the coverage map must grep the specs' own \"kebab\" alias, not just the source class tokens; the mutation rounded-md → rounded-lg at item-card.tsx:139 line-scoped — the radius family axis alone, the v45 pin structurally immune)"
insert_after("CLAUDE.md",
             "the 390/640 and ≥1024 states structurally immune)",
             V116_CLAUSE,
             "the v116 savings goal-card kebab-trigger census")

# ---------------- D3: README.md ----------------
replace1("README.md",
         "e2e/                    # Playwright specs (318 tests) + global setup",
         "e2e/                    # Playwright specs (319 tests) + global setup")
replace1("README.md",
         "npm run test:e2e    # Playwright e2e (318 tests) — needs `npm run build` first",
         "npm run test:e2e    # Playwright e2e (319 tests) — needs `npm run build` first")
V116_ROW = """
| [`docs/remediation-plan-v116.md`](docs/remediation-plan-v116.md) | **The re-run cycle's next-oldest candidate (the v110-era SAVINGS pair's NINTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116] — the SAVINGS view at desktop 1280×800 FULL-PAGE, last re-shot v110 — now the oldest remaining [v110 < v111 < v112 < v113 < v114 < v115]; the THIRTY-NINTH consecutive queue/ledger agreement — the surface names verified against vlm-shots-v110.sh's own header before the derivation) + the axe watch (NO DRIFT) + the npm-audit watch (the standing step's seventh cycle: 0 vulnerabilities — the v110 bump holds) + the 110th standing checks + the savings goal-card kebab-trigger census pin at 1280 (PIN-ONLY)**. The verdict SAVINGS DIFFERENT — the pair's documented flag-set class (v104/v98/v110 read DIFFERENT; no FAB flag raised — the disproof not required) — with every flag DOM-arbitrated to a documented class (the card-footer chips the v57 DATA-CONDITIONAL class [the reference's savings item ships no paymentMethod — footer childCount 1, the date-only DIV; the clone's render the SPAN pair, footer childCount 2]; the card grid the seed-count class; the header stats + card contents the seed-data classes; the avatar the user-identity class); the two-half census (SV_CENSUS_JS 153 lines, md5 891ab9b6 — the v104/v110 census block carried over VERBATIM) compared AXIS-BY-AXIS by the persisted compare-v116-census.py (120 axes: 80 identical + 40 documented-class deltas, ZERO new) — NO NEW CLONE GAP; the +1 e2e pin the never-pinned savings goal-card KEBAB TRIGGER at 1280 (the at-rest unheld chrome {tag BUTTON/display flex/radius 6px/bg transparent/color rgb(10,10,10)/cardTop 21/cardRight 21} + the hover-path group-hover reveal {opacity "1"} — the v45 F1a pin already holds the trigger's w/h/at-rest opacity on /income, the shared component, so those axes stay out of the census return per the V94-COLLISION criterion; measured byte-identical both sides via the one-shot hover-arbit-v116.sh with the static-hover-coordinate trap repaired [the card's OWN center, not a static 640,300]); mutation-verified single-axis (rounded-md → rounded-lg at item-card.tsx:139 line-scoped — only the v116 pin red at the radius axis alone ["6px" → "8px"], the v45/tab-walk/v98/v80 pins structurally immune; the FIRST h-axis attempt's two-red run the V94-collision evidence — THE SPEC-ALIAS COVERAGE LESSON); restored, rebuilt, post-restore 46/46 green; 319 e2e total. The cycle's derivation lessons: THE BARE-FRAGMENT LINE-WRAP FORM (the plan-attribution correction must target the line-internal bare "v109 plan's" — the with-article form spans the v110 headers' line break) + the builder's bare-session swap (refarbit110→refarbit116 — a no-'v'-prefix token the generic swap cannot touch). The ship: 319 e2e zero flakes across the auditable four-chunk split (84+79+77+82 = 322 executions = 319 unique); the screenshots 20/20 byte-identical (the same-day-seed law); the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end (npm ci in the foreground + zod 840/840 + BOTH v1243 binaries DIRECT). |"""
insert_after("README.md",
             "class — the v108 FRESH-CLONE provisioning lesson applied end-to-end (npm ci in the foreground + zod 840/840 + BOTH v1243 binaries DIRECT). |",
             V116_ROW,
             "remediation-plan-v116.md")

# ---------------- D4: SKILL.md ----------------
replace1("zero-balance_SKILL.md",
         "project_state: 108 unit tests / 318 e2e tests / 35 smoke steps — all green",
         "project_state: 108 unit tests / 319 e2e tests / 35 smoke steps — all green")
V151_ROW = """| 2026-10-25 | Session 151 — parity iteration v116 (`docs/remediation-plan-v116.md`) | **The re-run cycle's next-oldest candidate (the v110-era SAVINGS pair's NINTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116] — the SAVINGS view at desktop 1280×800 FULL-PAGE; the THIRTY-NINTH consecutive queue/ledger agreement) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's seventh cycle: 0 vulnerabilities — the v110 bump holds) + the 110th standing checks (ALL GREEN — the mobile menu working the 110th consecutive time) + the savings goal-card kebab-trigger census pin at 1280 (PIN-ONLY; +1 e2e = 319)**: the verdict SAVINGS DIFFERENT — the pair's documented flag-set class — every flag DOM-arbitrated to a documented class (the payment chips the v57 DATA-CONDITIONAL class [the reference's savings item ships no paymentMethod — footer childCount 1, the date-only DIV; the clone's render the SPAN pair]; the seed-count/seed-data classes; the user-identity avatar; NO FAB flag — the disproof not required); the two-half census (SV_CENSUS_JS 153 lines, md5 891ab9b6 — the v104/v110 block VERBATIM) compared axis-by-axis by the persisted compare-v116-census.py (120 axes: 80 identical + 40 documented-class deltas, ZERO new) — NO NEW CLONE GAP; the +1 pin the savings goal-card's KEBAB TRIGGER at 1280 — the at-rest unheld chrome + the hover-path reveal, the v45-held w/h/at-rest-opacity axes left out per the V94-COLLISION criterion — measured byte-identical both sides via the one-shot hover-arbit-v116.sh, mutation-verified single-axis (rounded-md → rounded-lg at item-card.tsx:139 line-scoped — only the v116 pin red at the radius axis alone; the first h-axis attempt's two-red run the collision evidence — THE SPEC-ALIAS COVERAGE LESSON: grep the specs' own "kebab" alias, not just the source tokens; an axis held in ANY view is held for EVERY view of a shared component); THE STATIC-HOVER-COORDINATE TRAP (the first read's static 640,300 missed the reference's column-1 card — hover at the card's OWN center); restored, rebuilt, post-restore 46/46 green; the ship chain 319 e2e zero flakes (84+79+77+82 = 322 executions), 35/35 smoke, the screenshots 20/20 byte-identical, the dev evidence 4/4 byte-identical + VLM-verified; the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end |** 108/319/35 green |"""
insert_after("zero-balance_SKILL.md",
             "|** 108/318/35 green |",
             "\n" + V151_ROW.strip(),
             "Session 151 — parity iteration v116")

# ---------------- D5: PAD ----------------
V1173_BLOCK = """#### Revision Block — v1.1.73 (Tracked Changes)
- `[UI]` v1.1.73 (2026-10-25) — the v116 parity iteration (PIN-ONLY for src/ — no production-code change; no dependency change): the counts 108 unit / **319 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v110-era SAVINGS pair's NINTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116] — the SAVINGS view at desktop 1280×800 FULL-PAGE, last re-shot v110; the THIRTY-NINTH consecutive queue/ledger agreement) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's seventh cycle: 0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 110th standing checks (ALL GREEN — the mobile menu working the 110th consecutive time; the reference's four bugs all live; the data census clean on the FIRST reads) + the savings goal-card kebab-trigger census pin at 1280 (PIN-ONLY; +1 e2e = 319)**: the verdict SAVINGS DIFFERENT — the pair's documented flag-set class (v104/v98/v110 read DIFFERENT; no FAB flag raised — the disproof not required) — with every flag DOM-arbitrated to a documented class (the card-footer payment chips the v57 DATA-CONDITIONAL class [the reference's savings item ships no paymentMethod — its footer renders the date-only DIV, childCount 1; the clone's items carry paymentMethods and render the SPAN pair the reference's own income card renders, childCount 2]; the card grid the seed-count class [1 vs 2]; the header stats + card contents the seed-data classes [the classification-VALUE badge colors locked by badge-colors.spec]; the avatar the user-identity class); the two-half census (SV_CENSUS_JS 153 lines, md5 891ab9b6 — the version-free v104/v110 census block carried over VERBATIM), compared AXIS-BY-AXIS by the persisted compare-v116-census.py (120 axes: 80 identical + 40 documented-class deltas, ZERO new) — NO NEW CLONE GAP; the +1 pin (tests/e2e/items.spec.ts) the savings goal-card's KEBAB TRIGGER at 1280 — the hover-revealed action element on the pair's OWN target surface, never pinned at ANY viewport in ANY spec — the at-rest unheld chrome {tag BUTTON / display flex / radius 6px / bg transparent / color rgb(10,10,10) / cardTop 21 / cardRight 21} + the HOVER-path group-hover reveal {opacity "1", settled past the 150ms transition window}; measured byte-identical both sides via the one-shot hover-arbit-v116.sh (the static-hover-coordinate trap repaired: the hover reads the card's OWN center — the reference's 1-item seed renders its card in grid column 1, x 288–597, where the static 640,300 landed on the column-gap whitespace); mutation-verified single-axis (rounded-md → rounded-lg at item-card.tsx:139 line-scoped — only the v116 pin red at the radius family axis alone ["6px" → "8px"]; the v45 F1a pin — which holds the trigger's w 36/h 36/at-rest opacity "0" on /income, the shared component — GREEN under the mutation); restored, rebuilt, post-restore 46/46 green. The cycle's survey lesson: THE SPEC-ALIAS COVERAGE LESSON (the first mutation attempt — the h axis — failed the sole-failure test with TWO reds: the v45 F1a pin holds the trigger's w/h/at-rest opacity under the specs' own "kebab" alias, a hold the coverage map missed grepping only the source class tokens; an axis held in ANY view is held for EVERY view of a shared component; the pin re-scoped to the unheld axes with the held axes left out of the census return itself, the first mutation's two-red run kept as the collision evidence); the derivation lessons: THE BARE-FRAGMENT LINE-WRAP FORM (the plan-attribution correction targets the line-internal bare "v109 plan's" — the with-article form spans the v110 headers' line break, the v107 line-break lesson's bare-form instance) + the builder's bare-session swap (refarbit110→refarbit116 — a no-'v'-prefix token the generic swap cannot touch, closed this cycle after the v115 builder's clonearbit109 leftover). The ship chain 319 e2e zero flakes (84+79+77+82 = 322 executions across four chunks), 35/35 smoke, the screenshots 20/20 byte-identical (the same-day-seed law), the dev evidence 4/4 byte-identical + re-captured + VLM-verified; the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end.
"""
t = open("Project_Architecture_Document.md", encoding="utf-8").read()
if "#### Revision Block — v1.1.73" in t:
    print("ALREADY APPLIED: PAD v1.1.73 block — skipped")
elif t.count("#### Revision Block — v1.1.72 (Tracked Changes)") != 1:
    print(f"AMBIGUOUS/MISS: PAD v1.1.72 anchor")
    ok = False
else:
    t = t.replace("#### Revision Block — v1.1.72 (Tracked Changes)",
                  V1173_BLOCK + "#### Revision Block — v1.1.72 (Tracked Changes)", 1)
    open("Project_Architecture_Document.md", "w", encoding="utf-8").write(t)
    print("aligned Project_Architecture_Document.md (the v1.1.73 block)")

sys.exit(0 if ok else 1)
