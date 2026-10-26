#!/usr/bin/env python3
"""Align the docs for the v123 cycle (Session 158).

D1  AGENTS.md     — the v123 paragraph appended after the v122 paragraph
D2  CLAUDE.md     — the E2E count 325 -> 326 + the v123 clause
D3  README.md     — the count strings 325 -> 326 (two places) + the v123
                    plan row appended after the v122 row
D4  SKILL.md      — project_state 325 -> 326 + the Session 158 row appended
                    after the Session 157 row
D5  PAD           — the [UI] v1.1.80 revision block (inserted newest-first,
                    before the v1.1.79 block)
D6  probe README  — the v123 section (after the v122 section) + the v124 queue
D7  session_302.md + the worklog Session 158 entry (separate steps)

No D0 this cycle: the v122 paragraph's tail verified clean (the anchor
fragment '075df6d' appears exactly ONCE — no duplication, the
v119-defect class checked and absent).
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
V123_AGENTS = """

Reference surfaces pinned by the v123 iteration (`docs/remediation-plan-v123.md`) — **the re-run cycle's next-oldest candidate (the v117-era LOGIN + CALCULATOR pair — the LOGIN view + the CALCULATOR dialog at desktop 1280x800, the v59-era pair's surface family, the pair's TENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123], the FORTY-SIXTH consecutive queue/ledger agreement — the v117 header's own NINTH ordinal CONSISTENT with its 10-entry bracket [v59 the original], no off-by-one this lineage)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only the canary 4.14.0-canary.6b52b84 prerelease beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds — one node_modules/axe-core entry verified live; the engine-contract pin green) + the npm-audit watch at its fourteenth re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 117th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads [1 items USD 25,000 / 1 items USD 5000.00 / 4 items USD 525.00]; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 117th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). **The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs this cycle** (the v122 date-axis repair verified holding on the new day: the v120 liability-card pin green with its computed seedDay form; lint · typecheck · 108 unit · build · 325 e2e zero flakes [328 executions in 4 chunks] · 35/35 smoke; the production-seam audit clean — auth, db-path, the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded as always). **The verdict CALCULATOR DIFFERENT ×2 / LOGIN IDENTICAL ×2 (the consistent form — no variation this cycle)** — every CALCULATOR flag DOM-arbitrated: the row action buttons "missing in the clone" + the "significantly shorter row" the POINTER-POSITION/HOVER-STATE screenshot artifact + the VLM MISREAD (the census: `actionsAtRest {opacity "0", btnCount 2}` IDENTICAL both sides, `row.h 102` byte-identical — the artifact's mechanism: the REFERENCE shots script captures BEFORE parking its pointer [still at the Calculate button, INSIDE the opened dialog — the hover-revealed actions caught mid-shot] while the CLONE script parks at (5,5) BEFORE its capture; the shots scripts' own structure, inherited verbatim from the v59 lineage); the "Will update category total" note the SEED-DATA class (the reference's OWN Rent $25.00 EQUALS its calculated total so the note hides; the clone's $1850-vs-$25.00 recalc shows it — DATA-CONDITIONAL, the totalCard box byte-identical); the login "Edit with Base44" badge the PLATFORM-CHROME class disproven live (`base44-fab-arbit-v123.sh`: fabCount 0 + bodyHasBase44 false BOTH sides). The both-sides census (the TWO blocks — CALC_CENSUS_JS 61 lines + LOGIN_CENSUS_JS 36 lines — byte-identical across the halves, the md5 line-block contract verified by direct python extraction [the sed-based extraction reads different boundaries]; built two-half by build-twohalf-v123.py, derived from build-twohalf-v117.py with the lesson-range bump v92..v122 + the lineage-note fixup) compared AXIS-BY-AXIS by the persisted compare-v123-census.py (**106 axes: 97 identical + 9 documented-class deltas, ZERO new** — the login card.border zero-width artifact, the card.shadow + panel.shadow construct lead-counts, the 5 close.* finder-artifact axes [clone-only present], the totalCard.hasWillUpdateSpan seed-data class). **THE PIN — the CALCULATOR line-item DELETE-CONFIRM BAR census at 1280 (PIN-ONLY — the never-pinned FOURTH member of the confirm-bar family, +1 e2e = 326)**: the family's four members — the ITEM-CARD bar (pinned v121), the ASSET + LIABILITY bars (held BY CONSTRUCTION via the identical class strings net-worth-view.tsx:123/234), and the CALCULATOR's bar (`calculator-dialog.tsx:279`, "Delete this line item?") — held by NO spec (the behavioral tests assert the text + the click flow only; the v45/v66 row censuses read the row at REST; the bar renders only while `confirmingId === li.id`). The CLONE-ONLY form (the v121 F3 adapted precedent): the reference's calculator row delete destroys IMMEDIATELY (its R6 bug) — no confirm bar exists on the reference, and a reference-side measurement would require a DESTRUCTIVE click (the v46 read-only rule); the family chrome = the v121 pinned contract BY CONSTRUCTION + **the calculator-specific axis: mt-3 (12px — the family's other members carry mt-4 16px; the token `mt-3 flex items-center justify-between rounded-lg p-3` appears EXACTLY ONCE in src/)**. The one-shot census (`confirmbar-arbit-v123.sh` — the CONFIRM-LADDER form: the twin state seeded through the real UI [the "Contents Insurance" $25 line item, the v66 form] → the at-rest 102 → the bar census → the Cancel path → the destructive Delete + restoreRent + the seedcheck exact; the census script's own first-run bug fixed live: the agent-browser `mouse move` takes x y as TWO args — the single-arg "x,y" form moves nowhere) measured: the bar {mt "12px" / flex / center / space-between / radius "8px" / pad "12px" / w 686 / h 48} + the label {"Delete this line item?" 14px/400} + the pills {4px 12px / 6px / 12px/500 / h 24} + the shadow-sm VISIBLE layer (`rgba(0,0,0,0.05) 0px 1px 2px 0px`, toContain — the accepted-leads convention) + **THE BAR-OPEN DELTA +60 (the row card 102 → 162 = the bar's 48 + the mt-3's 12)** + the Cancel path returning the row to 102. The pin's two live-red discoveries documented in the spec: the items-view subtitle's formatMoney NO-GROUPING form ("$2235.00" not "$2,235.00") + the census shadow key split to a sibling (cancelShadow) so the toEqual matches exactly. The pin-sanity mutation (`calculator-dialog.tsx:279` line-scoped p-3→p-4, the net-worth/item-card mt-4 twins untouched by the file+line scoping): the SOLE FAILURE verified live — the pin ALONE red at the pad ("12px"→"16px") + h (48→56) axes, the full calculator file's 19 others green (the v45/v66/v49/v53/v59/v73/v81/v87/v93/v111 pins + the behavioral tests all immune); restored + the full rebuild + the 20/20 post-restore regression + the items file 48/48 green (the v121/v122 pins' different-file immunity verified live). The ship chain 326 e2e zero flakes (87+86+74+82 = 329 executions = 326 unique); 35/35 smoke; **the screenshots 16/16 byte-identical (the same-day-seed law — the committed set is same-day with the Oct 26 seed, today's re-capture same-day too: no day-rollover refresh needed this cycle)**; the dev evidence 4/4 captured + VLM-verified (byte-identical; the menu proof: /income, docSW 390, navLandmark true — the dev-shots scripts derived v122→v123 with the version-swap-only verification). The workspace the RESET class (the v122 environment did not persist between the cycles — the repo re-cloned from main @ cbc38e9; the v108 FRESH-CLONE provisioning end-to-end: npm ci in the foreground [354 entries, the zod extraction verified intact 840/840], BOTH v1243 playwright pairs installed with INSTALLATION_COMPLETE verified [the fresh cache held only the old chromium-1200 pair], the explicit-env-prefix Prisma discipline, the seedcheck exact before any gate)."""
ok = ok and insert_after("AGENTS.md",
             "the repo re-cloned from main @ 075df6d; the v108 FRESH-CLONE provisioning end-to-end: npm ci in the foreground, the zod extraction verified intact, BOTH v1243 playwright pairs installed with INSTALLATION_COMPLETE verified, the explicit-env-prefix Prisma discipline, the seedcheck exact before any gate).",
             V123_AGENTS,
             "Reference surfaces pinned by the v123 iteration")

# ---------------- D2: CLAUDE.md ----------------
ok = ok and replace1("CLAUDE.md",
    "- **E2E (Playwright, 325)**:",
    "- **E2E (Playwright, 326)**:")
ok = ok and insert_after("CLAUDE.md",
    "the Radix tab-switch pointer-sequence lesson encoded in the spec form)",
    "; the v123 pin — the calculator line-item DELETE-CONFIRM BAR census at 1280: the never-pinned FOURTH member of the confirm-bar family (the v121 item-card bar's twin by identical class strings; the calculator-specific mt-3 12px axis + the +60 bar-open delta [the row 102 → 162] + the shadow-sm visible layer by toContain — the census shadow split to a sibling key so the toEqual matches; the pin-sanity p-3→p-4 line-scoped mutation sole-failure verified live, the 19 others green)",
    "the v123 pin — the calculator line-item DELETE-CONFIRM BAR census")

# ---------------- D3: README.md ----------------
ok = ok and replace1("README.md",
    "Playwright specs (325 tests) + global setup",
    "Playwright specs (326 tests) + global setup")
ok = ok and replace1("README.md",
    "Playwright e2e (325 tests) — needs `npm run build` first",
    "Playwright e2e (326 tests) — needs `npm run build` first")
V123_ROW = """| [`docs/remediation-plan-v123.md`](docs/remediation-plan-v123.md) | **The re-run cycle's next-oldest candidate (the v117-era LOGIN + CALCULATOR pair's TENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123] — the LOGIN view + the CALCULATOR dialog at desktop 1280x800; the FORTY-SIXTH consecutive queue/ledger agreement)** + the axe watch (NO DRIFT — 4.14.0 holds) + the npm-audit watch (0 vulnerabilities, fourteenth re-check) + the 117th standing checks (ALL GREEN — the mobile menu the 117th consecutive pass) + the calculator line-item DELETE-CONFIRM BAR census pin at 1280 (PIN-ONLY — +1 e2e = 326; the never-pinned FOURTH member of the confirm-bar family, the mt-3 calculator-specific axis + the +60 bar-open delta; the sole-failure mutation verified live) + the baseline fully green on the first chain (the v122 date-axis repair holding). |
"""
ok = ok and insert_after("README.md",
    "(re-cloned from main @ 075df6d, the v108 fresh-clone provisioning end-to-end). |",
    "\n" + V123_ROW,
    "docs/remediation-plan-v123.md")

# ---------------- D4: zero-balance_SKILL.md ----------------
ok = ok and replace1("zero-balance_SKILL.md",
    "project_state: 108 unit tests / 325 e2e tests / 35 smoke steps — all green",
    "project_state: 108 unit tests / 326 e2e tests / 35 smoke steps — all green")
S158_ROW = """| 2026-10-26 | Session 158 — parity iteration v123 (`docs/remediation-plan-v123.md`) | **The re-run cycle's next-oldest candidate (the v117-era LOGIN + CALCULATOR pair's TENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123] — the LOGIN view + the CALCULATOR dialog at 1280x800; the FORTY-SIXTH consecutive queue/ledger agreement)** + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — fourteenth re-check) + the 117th standing checks (ALL GREEN — the reference's four bugs live, the mobile menu the 117th consecutive pass, zero overflow at 390) + the VLM pair (CALCULATOR DIFFERENT ×2 / LOGIN IDENTICAL ×2 — every flag DOM-arbitrated: the pointer-position/hover-state shot artifact + the VLM row misread, the seed-data note, the platform-chrome FAB disproven live) + the two-half census (106 axes — 97 identical + 9 documented, ZERO new) + the calculator line-item DELETE-CONFIRM BAR census pin at 1280 (PIN-ONLY — the never-pinned FOURTH member of the confirm-bar family; the mt-3 axis + the +60 bar-open delta; the p-3→p-4 sole-failure mutation verified live; +1 e2e = 326) + the ship chain fully green (326 e2e zero flakes [329 executions], 35/35 smoke, the screenshots 16/16 byte-identical — the same-day-seed law, no day-rollover this cycle, the dev evidence 4/4 byte-identical + VLM-verified) |** 108/326/35 green — the workspace the RESET class (re-cloned from main @ cbc38e9) |
"""
ok = ok and insert_after("zero-balance_SKILL.md",
    "+ 1 date-only); the workspace the RESET class (re-cloned from main @ 075df6d) |** 108/325/35 green |",
    "\n" + S158_ROW,
    "Session 158 — parity iteration v123")

# ---------------- D5: Project_Architecture_Document.md ----------------
V1180_BLOCK = """#### Revision Block — v1.1.80 (Tracked Changes)
- `[UI]` v1.1.80 (2026-10-26) — the v123 parity iteration (**PIN-ONLY — zero production-code changes** + one e2e pin; no dependency change): the counts 108 unit / **326 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v117-era LOGIN + CALCULATOR pair's TENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123] — the LOGIN view + the CALCULATOR dialog at desktop 1280x800; the FORTY-SIXTH consecutive queue/ledger agreement; the v117 header's own NINTH ordinal consistent with its 10-entry bracket)**; the baseline fully green on the first chain (the v122 date-axis repair verified holding); the VLM pair CALCULATOR DIFFERENT ×2 / LOGIN IDENTICAL ×2 (every flag DOM-arbitrated — the pointer-position/hover-state screenshot artifact [the reference shots script captures before parking its pointer; the census actionsAtRest identical both sides], the VLM row misread [row.h 102 byte-identical], the seed-data note, the platform-chrome FAB disproven live); the two-half census **106 axes — 97 identical + 9 documented-class deltas, ZERO new** (the login card.border zero-width artifact, the card.shadow + panel.shadow construct lead-counts, the 5 close.* finder-artifact axes, the totalCard.hasWillUpdateSpan seed-data class); **THE PIN — the calculator line-item DELETE-CONFIRM BAR census at 1280** (the never-pinned FOURTH member of the confirm-bar family: the bar {mt-3 12px / flex / center / space-between / radius 8px / pad 12px / w 686 / h 48} + the label 14px/400 + the Cancel/Delete pills {4px 12px / 6px / 12px/500 / h 24} + the shadow-sm visible layer + **the +60 bar-open delta [the row card 102 → 162]** + the Cancel path; the clone-only form — the reference's row delete destroys immediately, its R6 bug; the pin-sanity p-3→p-4 line-scoped mutation sole-failure verified live); the ship chain 326 e2e zero flakes (329 executions in 4 chunks) + 35/35 smoke + the screenshots 16/16 byte-identical (the same-day-seed law) + the dev evidence 4/4 (the menu proof: /income, docSW 390, navLandmark true).
"""
if True:
    t = open("Project_Architecture_Document.md", encoding="utf-8").read()
    if "#### Revision Block — v1.1.80" not in t:
        old = "#### Revision Block — v1.1.79 (Tracked Changes)"
        n = t.count(old)
        if n != 1:
            print(f"D5 AMBIGUOUS: {n} hits")
            ok = False
        else:
            open("Project_Architecture_Document.md", "w", encoding="utf-8").write(
                t.replace(old, V1180_BLOCK + old))
            print("D5: v1.1.80 block inserted (newest-first)")
    else:
        print("D5: v1.1.80 block already present")

print("ALIGN RESULT:", "OK" if ok else "FAIL")
sys.exit(0 if ok else 1)
