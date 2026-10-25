#!/usr/bin/env python3
"""D1-D5 docs alignment for the v117 cycle (the persisted alignment-script
precedent — the v116 cycle's align-docs-v116.py form, WITH the
IDEMPOTENT-RUN DUPLICATION TRAP guard on every insert-after edit).

D1  AGENTS.md     — the v117 paragraph appended after the v116 paragraph
D2  CLAUDE.md     — the E2E count 319 -> 320 + the v117 clause appended to
                    the v116 clause's tail
D3  README.md     — the two (319 tests) counts -> 320 + the v117 plan row
                    appended after the v116 row
D4  SKILL.md      — project_state 319 -> 320 + the Session 152 row appended
D5  PAD           — the v1.1.74 revision block inserted before v1.1.73

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
V117_AGENTS = """

Reference surfaces pinned by the v117 iteration (`docs/remediation-plan-v117.md`) — **the re-run cycle's next-oldest candidate (the v111-era LOGIN + CALCULATOR pair — the LOGIN view + the CALCULATOR dialog at desktop 1280×800, the pair's NINTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117], the FORTIETH consecutive queue/ledger agreement)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only a canary sha prerelease beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds; the engine-contract pin green) + the npm-audit watch at its eighth re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 111th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 111th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). The verdicts CALCULATOR DIFFERENT (the pair's documented verdict class — the will-update note the SEED-DATA class [ref `hasWillUpdateSpan:false`, its own Rent $25.00 equals its calculated total]; the hover-action row the RESTING-STATE parity class [`actionsAtRest` {opacity 0, btnCount 2} identical both sides]; the row-height flag their consequence) + LOGIN DIFFERENT (the FAB flag alone — DISPROVEN live by the one-shot base44-fab-arbit-v117.sh: `fabCount:0` + `bodyHasBase44:false` on BOTH sides at 1280 on /login — the platform-iframe chrome class). The both-sides census (CALC_CENSUS_JS 61 lines md5 e1092d12 + LOGIN_CENSUS_JS 36 lines md5 9e5a52d2 — the version-free v99/v105/v111 census blocks carried over VERBATIM) compared AXIS-BY-AXIS by the persisted compare-v117-census.py (**106 axes: 97 identical + 9 documented-class deltas, ZERO new** — the card.shadow/panel.shadow zero-layer lead counts the v3/v4 construct class [the visible layer the contract, held by the v45 F4 pin]; the card.border zero-width computed-color artifact [border-width 0 both sides, nothing renders — the v3 base default gray-200 vs the app's measured --color-border token]; the close-key family the v99 finder artifact [the v87 pin the authority]; hasWillUpdateSpan the SEED-DATA class) — the strip census's `bottom` axis divergence (ref 742 vs clone 738) root-caused by the cardheight drill-down to **THE SM:TIER FREEZE — the cycle's production-code FIX (the sixth since v46)**: the login h1 block ships the reference's own verbatim `space-y-2 sm:space-y-3` classes (login-card.tsx:574, the ONLY sm-paired tier in the codebase), but the v9 G3 mitigation's class-specificity base restore FROZE OUT v4's zero-specificity `:where(.sm\\:space-y-3)` media variant — the subtitle's gap computed at the base 8px forever (block 104 / card 742) where the reference's v3 engine lets the sm: tier win at >=640 (12px / 108 / 746). THE FIX: the sm:-variant restore in globals.css's `@layer utilities` (the v50 zb-sm6 precedent's form — `@media (min-width: 640px) { .sm\\:space-y-3 > * + * { margin-block-start: 0.75rem } }`), cascade-verified surgical (exactly ONE element carries the class; the v99/v105/v7/v25/v45/v55/v51 pins all structurally immune — element-local or relative axes). The +1 e2e pin (tests/e2e/login-parity.spec.ts): the login card's TOP-ACCENT-STRIP + H1-BLOCK census at 1280 — the strip's never-pinned geometry {tag DIV/position absolute/top 0px/right 0px/left 0px/h 4/w 448/bgImage the full 3-stop slate gradient} + the FIXED family {subtitle mt "12px"/block h 108} + the card context {w 448/h 746} + the docSW guard; TDD-verified (the pre-fix RED run failed at the sm:TIER axes alone [subMt "8px" vs "12px"], the post-fix GREEN run, the 52/52 surface regression check). The ship chain 320 e2e zero flakes (84+80+77+82 = 323 executions = 320 unique); 35/35 smoke; the screenshots regenerated with 9 byte-diffs ARBITRATED (2 fix-effects [01-login + 14-login-error — the +4px card shift] + 7 date-drifts [the relative-seed dates rolled a day: 03/04/05/06/07/08/16, the footer-band bboxes]; 15-forgot-reset byte-IDENTICAL — the surgical-fix confirmation); the dev evidence 3 same + 1 date-drift + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the menu open with all 5 links + the brand; the sheet closed post-nav; the dashboard clean — the dev-shots scripts derived v116→v117 with the version-swap-only verification). The workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end (npm ci in the foreground + zod 840/840 + BOTH v1243 binaries DIRECT)."""
insert_after("AGENTS.md",
             "the dev-shots scripts derived v115→v116 with the version-swap-only verification).",
             V117_AGENTS,
             "Reference surfaces pinned by the v117 iteration")

# ---------------- D2: CLAUDE.md ----------------
replace1("CLAUDE.md", "- **E2E (Playwright, 319)**:", "- **E2E (Playwright, 320)**:")
V117_CLAUSE = " and the v117 login strip + h1-block census at 1280 (the card's top-accent-strip geometry + THE SM:TIER FIX's axes — the login h1 block's `space-y-2 sm:space-y-3` subtitle gap was FROZEN at the base 8px by the v9 G3 mitigation's class-specificity base restore beating v4's zero-specificity `:where(.sm\\:space-y-3)` media variant; the fix: the sm:-variant restore in globals.css's @layer utilities [the v50 zb-sm6 precedent's form] — the subtitle mt 12px / the block 108 / the card 746, the reference's own values; the pre-fix RED run failed at the sm:TIER axes alone, the post-fix GREEN + the 52/52 surface regression)"
insert_after("CLAUDE.md",
             "the v45 pin structurally immune)",
             V117_CLAUSE,
             "the v117 login strip + h1-block census")

# ---------------- D3: README.md ----------------
replace1("README.md",
         "e2e/                    # Playwright specs (319 tests) + global setup",
         "e2e/                    # Playwright specs (320 tests) + global setup")
replace1("README.md",
         "npm run test:e2e    # Playwright e2e (319 tests) — needs `npm run build` first",
         "npm run test:e2e    # Playwright e2e (320 tests) — needs `npm run build` first")
V117_ROW = """
| [`docs/remediation-plan-v117.md`](docs/remediation-plan-v117.md) | **The re-run cycle's next-oldest candidate (the v111-era LOGIN + CALCULATOR pair's NINTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117] — the LOGIN view + the CALCULATOR dialog at desktop 1280×800, last re-shot v111 — now the oldest remaining [v111 < v112 < v113 < v114 < v115 < v116]; the FORTIETH consecutive queue/ledger agreement — the surface names verified against vlm-shots-v111.sh's own header before the derivation) + the axe watch (NO DRIFT) + the npm-audit watch (the standing step's eighth cycle: 0 vulnerabilities — the v110 bump holds) + the 111th standing checks + the login h1-block SM:TIER space-y restore (THE FIX — the sixth production-code change since v46) + the login strip + h1-block census pin at 1280 (+1 e2e = 320)**. The verdicts CALCULATOR DIFFERENT (the pair's documented class — the will-update note the SEED-DATA class, the hover-action row the RESTING-STATE parity class, the row-height flag their consequence) + LOGIN DIFFERENT (the FAB flag alone — DISPROVEN live: `fabCount:0` + `bodyHasBase44:false` on BOTH sides, the platform-iframe chrome class); the two-half census (CALC_CENSUS_JS 61 lines md5 e1092d12 + LOGIN_CENSUS_JS 36 lines md5 9e5a52d2 — the v99/v105/v111 blocks carried over VERBATIM) compared AXIS-BY-AXIS by the persisted compare-v117-census.py (106 axes: 97 identical + 9 documented-class deltas, ZERO new — the shadow lead counts the v3/v4 construct class, the card.border zero-width computed-color artifact, the close-key family the v99 finder artifact, hasWillUpdateSpan the SEED-DATA class). **THE FIX — THE SM:TIER FREEZE**: the strip census's `bottom` axis divergence root-caused to the login h1 block's `space-y-2 sm:space-y-3` (the ONLY sm-paired tier in the codebase) — the v9 G3 mitigation's class-specificity base restore FROZE OUT v4's zero-specificity `:where(.sm\\:space-y-3)` media variant (the subtitle gap 8px forever vs the reference's 12px at >=640, the block 104 vs 108, the card 742 vs 746); the fix the sm:-variant restore in globals.css's `@layer utilities` (the v50 zb-sm6 precedent's form), cascade-verified surgical (one element, zero existing pins redden — the v99 rhythm axis RELATIVE, the v105/v7/v25/v45/v55/v51 axes element-local or other-mode). The +1 e2e pin the login card's TOP-ACCENT-STRIP (the never-pinned geometry {position absolute/top 0px/right 0px/left 0px/h 4/w 448/bgImage the full 3-stop slate gradient} — the v7 G2 pin holds the gradient colors only) + the FIXED family {subtitle mt "12px"/block h 108} + the card context {w 448/h 746}; TDD-verified (the pre-fix RED at the sm:TIER axes alone [subMt "8px" vs "12px"] → the fix → the post-fix GREEN → the 52/52 surface regression check). The ship: 320 e2e zero flakes across the auditable four-chunk split (84+80+77+82 = 323 executions = 320 unique); 35/35 smoke; the screenshots regenerated with 9 byte-diffs ARBITRATED (2 fix-effects + 7 date-drifts; 15-forgot-reset byte-identical — the surgical confirmation); the dev evidence 3 same + 1 date-drift + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end (npm ci in the foreground + zod 840/840 + BOTH v1243 binaries DIRECT). |"""
insert_after("README.md",
             "the auditable four-chunk split (84+79+77+82 = 322 executions = 319 unique); the screenshots 20/20 byte-identical (the same-day-seed law); the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); the workspace the RESET class",
             V117_ROW,
             "remediation-plan-v117.md")

# ---------------- D4: SKILL.md ----------------
replace1("zero-balance_SKILL.md",
         "project_state: 108 unit tests / 319 e2e tests / 35 smoke steps — all green",
         "project_state: 108 unit tests / 320 e2e tests / 35 smoke steps — all green")
V152_ROW = """| 2026-10-25 | Session 152 — parity iteration v117 (`docs/remediation-plan-v117.md`) | **The re-run cycle's next-oldest candidate (the v111-era LOGIN + CALCULATOR pair's NINTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117] — the LOGIN view + the CALCULATOR dialog at desktop 1280×800; the FORTIETH consecutive queue/ledger agreement) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's eighth cycle: 0 vulnerabilities — the v110 bump holds) + the 111th standing checks (ALL GREEN — the mobile menu working the 111th consecutive time) + THE SM:TIER FREEZE FIX (the sixth production-code change since v46) + the login strip + h1-block census pin at 1280 (+1 e2e = 320)**: the verdicts CALCULATOR DIFFERENT (the pair's documented class — the will-update note the SEED-DATA class, the hover-action row the RESTING-STATE parity class) + LOGIN DIFFERENT (the FAB flag alone — DISPROVEN live: fabCount 0 + bodyHasBase44 false on BOTH sides, the platform-iframe chrome class); the two-half census (CALC 61 lines md5 e1092d12 + LOGIN 36 lines md5 9e5a52d2 — the v99/v105/v111 blocks VERBATIM) compared axis-by-axis by the persisted compare-v117-census.py (106 axes: 97 identical + 9 documented-class deltas, ZERO new) — the strip census's `bottom` divergence root-caused to **THE SM:TIER FREEZE**: the login h1 block's `space-y-2 sm:space-y-3` (the ONLY sm-paired tier in the codebase) had its sm: tier FROZEN OUT by the v9 G3 mitigation's class-specificity base restore beating v4's zero-specificity `:where(.sm\\:space-y-3)` media variant (the subtitle gap 8px vs the reference's 12px at >=640, the block 104 vs 108, the card 742 vs 746); THE FIX the sm:-variant restore in globals.css's @layer utilities (the v50 zb-sm6 precedent's form), cascade-verified surgical (one element; the v99 rhythm axis relative, the v105/v7/v25/v45/v55/v51 axes element-local or other-mode — zero existing pins redden); the +1 pin the login card's TOP-ACCENT-STRIP geometry (never pinned at any viewport — the v7 G2 pin holds the gradient colors only) + the FIXED family {subtitle mt 12px/block 108} + the card context {448/746}; TDD-verified (the pre-fix RED at the sm:TIER axes alone [subMt "8px" vs "12px"] → the fix → the post-fix GREEN → the 52/52 surface regression); the ship chain 320 e2e zero flakes (84+80+77+82 = 323 executions), 35/35 smoke, the screenshots regenerated with 9 byte-diffs ARBITRATED (2 fix-effects + 7 date-drifts; 15-forgot-reset byte-identical — the surgical confirmation), the dev evidence 3 same + 1 date-drift + VLM-verified; the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end |** 108/320/35 green |"""
insert_after("zero-balance_SKILL.md",
             "|** 108/319/35 green |",
             "\n" + V152_ROW.strip(),
             "Session 152 — parity iteration v117")

# ---------------- D5: PAD ----------------
V1174_BLOCK = """#### Revision Block — v1.1.74 (Tracked Changes)
- `[UI]` v1.1.74 (2026-10-25) — the v117 parity iteration (**THE FIX — the sixth production-code change since v46** + one e2e pin; no dependency change): the counts 108 unit / **320 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v111-era LOGIN + CALCULATOR pair's NINTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117] — the LOGIN view + the CALCULATOR dialog at desktop 1280×800, last re-shot v111; the FORTIETH consecutive queue/ledger agreement) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's eighth cycle: 0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 111th standing checks (ALL GREEN — the mobile menu working the 111th consecutive time; the reference's four bugs all live; the data census clean on the FIRST reads) + the login h1-block SM:TIER space-y restore + the login strip + h1-block census pin at 1280 (+1 e2e = 320)**: the verdicts CALCULATOR DIFFERENT (the pair's documented class — the will-update note the SEED-DATA class [ref `hasWillUpdateSpan:false`], the hover-action row the RESTING-STATE parity class [`actionsAtRest` identical], the row-height flag their consequence) + LOGIN DIFFERENT (the FAB flag alone — DISPROVEN live by base44-fab-arbit-v117.sh: `fabCount:0` + `bodyHasBase44:false` on BOTH sides at 1280 on /login); the two-half census (CALC_CENSUS_JS 61 lines md5 e1092d12 + LOGIN_CENSUS_JS 36 lines md5 9e5a52d2 — the v99/v105/v111 blocks carried over VERBATIM) compared AXIS-BY-AXIS by the persisted compare-v117-census.py (**106 axes: 97 identical + 9 documented-class deltas, ZERO new**) — the strip census's `bottom` axis divergence (ref 742 vs clone 738) root-caused by the cardheight drill-down (the padding 48/40/40, the form blocks 172+80, the h1 72, the subtitle 24 all IDENTICAL; the delta isolated to the h1 block's internal gap) to **THE SM:TIER FREEZE**: the login h1 block ships the reference's own verbatim `space-y-2 sm:space-y-3` classes (login-card.tsx:574, the ONLY sm-paired tier in the codebase), but the v9 G3 mitigation's class-specificity base restore (`.space-y-2 > * + * { margin-block-start: 0.5rem }`, 0-1-2) FROZE OUT v4's zero-specificity `:where(.sm\\:space-y-3 > :not(:last-child))` media variant — the subtitle's gap computed at the base 8px forever (the block 104px / the card 742px) where the reference's v3 engine lets the sm: tier win at >=640 (12px / 108 / 746). THE FIX: the sm:-variant restore in globals.css's `@layer utilities` (`@media (min-width: 640px) { .sm\\:space-y-3 > * + * { margin-block-start: 0.75rem } }` — the v50 zb-sm6 precedent's form; source order after the base restore decides the same-specificity tie), cascade-verified surgical (exactly ONE element in the codebase carries `sm:space-y-3`; the v99 social-row pin's rhythm axis is RELATIVE, the v105/v7/v25/v45/v55/v51 pins element-local or other-mode — zero existing pins redden, verified live 52/52). The +1 e2e pin (tests/e2e/login-parity.spec.ts) the login card's TOP-ACCENT-STRIP + H1-BLOCK census at 1280 — the strip's never-pinned geometry {tag DIV/position absolute/top 0px/right 0px/left 0px/h 4/w 448/bgImage the full 3-stop slate gradient — the v7 G2 pin holds the gradient COLORS via toContain only} + the FIXED family {subtitle mt "12px"/block h 108} + the card context {w 448/h 746} + the docSW guard; TDD-verified (the pre-fix RED run failed at the sm:TIER axes alone [subMt "8px" vs "12px" — the fix load-bearing], the standalone REBUILD, the post-fix GREEN, the 52/52 surface regression). The ship chain 320 e2e zero flakes (84+80+77+82 = 323 executions across four chunks), 35/35 smoke, the screenshots regenerated with 9 byte-diffs ARBITRATED (2 fix-effects [01-login + 14-login-error, the +4px card shift] + 7 date-drifts [the relative-seed dates rolled a day — 03/04/05/06/07/08/16, the footer-band bboxes]; 15-forgot-reset byte-IDENTICAL — the surgical-fix confirmation), the dev evidence 3 same + 1 date-drift + VLM-verified; the workspace the RESET class — the v108 FRESH-CLONE provisioning lesson applied end-to-end.
"""
t = open("Project_Architecture_Document.md", encoding="utf-8").read()
if "#### Revision Block — v1.1.74" in t:
    print("ALREADY APPLIED: PAD v1.1.74 block — skipped")
elif t.count("#### Revision Block — v1.1.73 (Tracked Changes)") != 1:
    print(f"AMBIGUOUS/MISS: PAD v1.1.73 anchor")
    ok = False
else:
    t = t.replace("#### Revision Block — v1.1.73 (Tracked Changes)",
                  V1174_BLOCK + "#### Revision Block — v1.1.73 (Tracked Changes)", 1)
    open("Project_Architecture_Document.md", "w", encoding="utf-8").write(t)
    print("aligned Project_Architecture_Document.md (the v1.1.74 block)")

sys.exit(0 if ok else 1)
