#!/usr/bin/env python3
"""align-docs-v139.py — D1-D5 of the v139 docs alignment (the D0 anchor
discipline: every insert/replace anchor verified 1-hit BEFORE any write;
the script refuses and exits non-zero on any anchor miss or multi-hit).
  D1 AGENTS.md — the v139 paragraph appended after the v138 paragraph
  D2 CLAUDE.md — the e2e count 341 -> 342 + the v139 clause appended to
     the e2e enumeration line's end (after the v138 clause)
  D3 README.md — the two test-count lines 341 -> 342 + the v139 plan row
     inserted after the v138 row
  D4 zero-balance_SKILL.md — the project_state line 341 -> 342 + the
     Session 174 row inserted after the Session 173 row
  D5 Project_Architecture_Document.md — the v1.1.96 revision block
     inserted before the v1.1.95 block
"""
import io
import sys

ok = True


def one_hit(text: str, anchor: str, label: str) -> bool:
    global ok
    n = text.count(anchor)
    if n != 1:
        print(f"ANCHOR MISS ({label}): {n} hits for {anchor[:60]!r}")
        ok = False
        return False
    return True


# ---------- D1: AGENTS.md ----------
AG = "AGENTS.md"
text = io.open(AG, encoding="utf-8").read()
anchor = "the dev-shots scripts derived v137→v138 with the version-swap-only verification).\n\n"
if one_hit(text, anchor, "AGENTS v138-paragraph tail"):
    v139 = (
        "Reference surfaces pinned by the v139 iteration (`docs/remediation-plan-v139.md`) — "
        "**the re-run cycle's next-oldest candidate (the v133-era ITEMS pair — the ITEMS view [INCOME + EXPENSES] at desktop 1280x800 FULL-PAGE, the pair's THIRTEENTH re-run "
        "[v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139], the SIXTY-SECOND consecutive queue/ledger agreement "
        "— the corrected entries-minus-one convention applied cleanly: the TWELFTH ordinal recorded in the v133 plan's own header on its 13-entry bracket [v57 the original, one entry] → v139 = the THIRTEENTH, no prose/header conflict; "
        "the v133 shots header carries the FULL bracket form — the documented verification source; THE v127–v132 ROTATION POOL EXHAUSTED — the cadence enters the SECOND PASS [the v133–v138 pool], the v133-era pair the oldest remaining)** "
        "+ the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, the v68 dedupe holds — one node_modules/axe-core entry verified live) "
        "+ the npm-audit watch at its thirtieth re-check (0 VULNERABILITIES --omit=dev — the v110 bump holds: next 16.4.3 + zod 4.6.7; the 16 moderate the accepted dev-only ESLint braces chain) "
        "+ the 133rd standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, "
        "the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; "
        "the clone's mobile menu VERIFIED WORKING the 133rd consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). "
        "**The baseline GREEN ON THE FIRST CHAIN** (the SAME-PERSISTED workspace — the v138 environment held through the session boundary: node_modules 354 entries intact, BOTH chromium pairs [1200 + 1243] in the cache, "
        "the .env [DATABASE_URL=\"file:../db/custom.db\"] + db/ at the repo root intact with the v138-cycle seed, the repo pulled to main @ 69a48d9; the seedcheck EXACT 7/1850/2235/0/3/2 before any gate [under the env -u discipline, "
        "the sandbox DATABASE_URL pollution live as documented]): lint, typecheck, 108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e [344 executions = 341 unique, ZERO flakes], 35/35 smoke; "
        "the production-seam audit clean; skills/ excluded). "
        "The probe series derived from the v133 lineage (derive-v139-series.py — FOUR explicit session-token families [refvlm/clonevlm + refarbit/clonearbit — the tokens carry '133' without the 'v' prefix] "
        "+ FOUR history-correction fragments [the era marker last-re-shot v127→v133 + the later-pairs list v128..v132→v134..v138; the ordinal TWELFTH→THIRTEENTH + the bracket extended in all four files], "
        "all applied on the FIRST run, zero residual, line counts preserved 56/48/49/284 == the v133 lineage exactly) "
        "+ the two-half builder (derive-build-twohalf-v139.py — the session-token bump clonearbit133→clonearbit139 FIRST [the v121 stale-session-fix precedent] + the lesson-range bump v92..v132→v92..v138 "
        "[the BARE range token] + the lineage-note fixup LAST) + the comparator (derive-compare-v139.py — the generic swap + the provenance citations re-pointed at the v133 measurement) "
        "+ the ONE-block two-half contract verified three-way (verify-twohalf-v139.py — CENSUS_JS 193 lines md5 b55dcd29 — **the v103/v109/v115/v121/v127/v133 lineage digest, carried byte-identical through the version-swap derivation**). "
        "**The VLM verdict — BOTH PAIRS DIFFERENT ×2, the pair's DOCUMENTED VERDICT CLASS** (the same verdict family as the v133 re-run; every flag in both passes in the documented classes: the avatar letter the USER-IDENTITY class; "
        "the \"Edit with Base44\" FAB claim the PLATFORM-CHROME/PERCEPTION-ARTIFACT class — claimed in BOTH directions across the passes and DISPROVEN LIVE by base44-fab-arbit-v139.sh [fabCount 0 + bodyHasBase44 false on BOTH sides, "
        "the flagged /income surface, 1280, logged-in — the v97..v136 standing disproof form]; the header stats + card names/amounts/dates the SEED-DATA classes; the expense footer payment-method labels the v57 DATA-CONDITIONAL class; "
        "the badge wrap the v57 wrap/classification-VALUE classes; the grid count the SEED-COUNT class); "
        "the both-sides census **187 axes — 163 identical + 24 documented-class deltas, ZERO new — REPRODUCING the v133 census values EXACTLY** (the same 187/163/24 split, zero drift on every axis). "
        "**A PIN-ONLY cycle for src/ — zero production-code changes (the ninth PIN-ONLY cycle in the last ten) + one e2e pin (341 → 342): the FILTER-CARD SELECT TRIGGER's OWN-HOVER LADDER at desktop 1280 on /income** "
        "(the never-pinned hover path of the pinned filter family: the v37 S1 pin the CLOSED category trigger's focus-visible family, the v64/v70 censuses BOTH triggers' at-rest geometry, the v50/v53 forms the mobile/640 chrome — "
        "every select census AT-REST; THE CONSTRUCT: the trigger carries NO hover: utility [select.tsx:20-27 — the focus + data-[placeholder] + disabled classes alone], "
        "so the own-hover end-state is the INERT-HOVER contract — the at-rest chrome persisting under each trigger's own hover); "
        "the both-sides one-shot census selecthover-arbit-v139.sh (the v138 tabhover form adapted to the select axes: the POSITION-BASED finders [button[role=combobox] first/second — the reference's triggers carry NO aria-label, "
        "identified by their text; the position form the ONLY form shared by both Radix sites], the (5,5)-parked ladder, the live-read centers [the category center REF (884,167) / CLONE (884,167), the frequency center REF (1115,167) / CLONE (1115,167)], "
        "READ-ONLY per the v46 rule — the Radix Select opens on pointerdown [the v120 lesson] and a mouse MOVE dispatches no pointerdown, so the census can never open the dropdown) measured the ladder on BOTH triggers — "
        "the CATEGORY and the FREQUENCY — **CLEAN, NO GAP** (the inert-hover contract IDENTICAL both sides at every rung; the deltas the documented construct classes alone: the shadow LEAD-LAYER count [the v37 S1's own O1 note — "
        "the v3 three-slot vs the TW v4 five-slot construct, every lead a 0px-spread shadow invisible by construction; the VISIBLE pair byte-identical] + the transition metadata identical); "
        "the pin appended (append-pin-v139.py — the at-rest rung → the CATEGORY-HOVERED rung {hoverMatch true + the UNCHANGED at-rest chrome} → the FREQUENCY-HOVERED rung → the restored rung {toEqual the first rung}; the V94-COLLISION-safe axis set; "
        "the POSITION-BASED finders; the triggers never clicked; GREEN on the first run; the authoritative --list: 342 in 24 files); "
        "the pin-sanity mutation — the HOVER-TINT form (hover:bg-[#f5f5f5] prepended to the SelectTrigger's className at select.tsx:25 — cascade-checked BY CONSTRUCTION: hover-scoped; the WIDER-FILE blast radius noted [select.tsx serves every Select in the app], "
        "the sole-failure criterion verified on the FULL ITEMS SWEEP ALONE) sole-failure verified live [1 failed + 52 passed in the FULL items sweep — the failure diff EXACTLY the predicted hovered-rung axis: "
        "the category trigger's bg rgb(245,245,245) — the mutation's tint — vs the persisted at-rest rgba(0,0,0,0) expected, hoverMatch true preserved, the border/color axes untouched]; "
        "restored (git diff src/ = 0 lines) + the FULL REBUILD + the post-restore regression 146 passed (items 53 + networth 41 + dashboard 52 — the v138/v137/v133 pins' different-file immunity verified live). "
        "The ship chain **342 e2e zero flakes** (94+93+76+82 = 345 executions = 342 unique — the +1 landing in ch1 [items]; both closed watches green through the chain); 35/35 smoke; "
        "**the screenshots 16/16 captured — ALL byte-identical (the same-day law: both this cycle and v138 captured Nov 1 UTC, every date-bearing surface rendering identically under the persisted seed)**; "
        "the dev evidence 4/4 byte-identical + VLM-verified (the menu proof {\"url\":\"/income\",\"docSW\":390,\"navLandmark\":true}; the dev-shots scripts derived v138→v139 with the version-swap-only verification).\n\n"
    )
    text = text.replace(anchor, anchor + v139)
    io.open(AG, "w", encoding="utf-8").write(text)
    print("D1 AGENTS.md: the v139 paragraph appended")

# ---------- D2: CLAUDE.md ----------
CL = "CLAUDE.md"
text = io.open(CL, encoding="utf-8").read()
if one_hit(text, "E2E (Playwright, 341)", "CLAUDE e2e count"):
    text = text.replace("E2E (Playwright, 341)", "E2E (Playwright, 342)")
    io.open(CL, "w", encoding="utf-8").write(text)
    print("D2a CLAUDE.md: 341 -> 342")
text = io.open(CL, encoding="utf-8").read()
anchor = "the post-restore regression 143/143 [networth 40 + dashboard 51 + items 51 — the v137/v136/v134 pins' different-file immunity verified live])"
if one_hit(text, anchor, "CLAUDE v138 clause tail"):
    v139clause = (
        "; the v139 pin — the FILTER-CARD SELECT TRIGGERS' OWN-HOVER LADDER at 1280 (the PIN-ONLY form — src/ ZERO changes, the ninth PIN-ONLY cycle in the last ten: "
        "the never-pinned hover path of the pinned filter family [every select census AT-REST — the v37 S1 focus-visible family, the v64/v70 at-rest geometry, the v50/v53 mobile/640 chrome]; "
        "THE CONSTRUCT: the trigger carries NO hover: utility [select.tsx:20-27], so the own-hover end-state is the INERT-HOVER contract — the at-rest chrome persisting under each trigger's own hover; "
        "the both-sides census selecthover-arbit-v139.sh measured the ladder on BOTH triggers CLEAN — the inert-hover contract IDENTICAL both sides at every rung [the category center (884,167) + the frequency center (1115,167), "
        "IDENTICAL coordinates both sides], the construct delta [the v37 O1 shadow lead-layer construct — the VISIBLE pair byte-identical] the documented class — NO GAP, NO REPAIR; "
        "the pin: the at-rest rung → the CATEGORY-HOVERED rung → the FREQUENCY-HOVERED rung → the restored rung, GREEN on the first run, --list 342 in 24 files; "
        "the pin-sanity mutation the HOVER-TINT form hover:bg-[#f5f5f5] prepended to the SelectTrigger's className — hover-scoped by construction, the wider-file blast radius noted, "
        "the sole failure verified on the FULL items sweep: 1 failed + 52 passed, the failure diff the predicted hovered-rung bg axis; the post-restore regression 146/146 [items 53 + networth 41 + dashboard 52 — "
        "the v138/v137/v133 pins' different-file immunity verified live])"
    )
    text = text.replace(anchor, anchor + v139clause)
    io.open(CL, "w", encoding="utf-8").write(text)
    print("D2b CLAUDE.md: the v139 clause appended")

# ---------- D3: README.md ----------
RD = "README.md"
text = io.open(RD, encoding="utf-8").read()
if one_hit(text, "Playwright e2e (341 tests)", "README e2e count line"):
    text = text.replace("Playwright e2e (341 tests)", "Playwright e2e (342 tests)")
    io.open(RD, "w", encoding="utf-8").write(text)
    print("D3a README.md: the test command count 341 -> 342")
text = io.open(RD, encoding="utf-8").read()
if one_hit(text, "Playwright specs (341 tests) + global setup", "README hierarchy count line"):
    text = text.replace(
        "Playwright specs (341 tests) + global setup",
        "Playwright specs (342 tests) + global setup",
    )
    io.open(RD, "w", encoding="utf-8").write(text)
    print("D3b README.md: the hierarchy count 341 -> 342")
text = io.open(RD, encoding="utf-8").read()
anchor = "the first cross-day capture since v131), the dev evidence 4/4 + VLM-verified). |\n"
if one_hit(text, anchor, "README v138 plan row tail"):
    v139row = (
        "| [`docs/remediation-plan-v139.md`](docs/remediation-plan-v139.md) | **The re-run cycle's next-oldest candidate (the v133-era ITEMS pair's THIRTEENTH re-run — the ITEMS view [income + expenses] at desktop 1280x800 FULL-PAGE, the SIXTY-SECOND consecutive queue/ledger agreement; "
        "the v127–v132 rotation pool exhausted — the cadence's SECOND PASS [the v133–v138 pool], the v133-era pair the oldest remaining) + the filter-card Select trigger own-hover ladder pin at 1280 (PIN-ONLY — src/ zero changes, the ninth PIN-ONLY cycle in the last ten; "
        "the census measured the ladder CLEAN on BOTH triggers — the INERT-HOVER contract, the at-rest chrome persisting under each trigger's own hover, IDENTICAL both sides at every rung; the FAB claim disproven live [fabCount 0 both sides]; "
        "the pin-sanity mutation the HOVER-TINT form on the SelectTrigger className — hover-scoped, the sole failure verified on the full items sweep: 1 failed + 52 passed; the post-restore regression 146/146) — "
        "the 133rd standing checks ALL GREEN (the mobile menu the 133rd consecutive; the four reference bugs live; the census clean on the FIRST reads), the watches green (0 vulnerabilities --omit=dev — the thirtieth; axe-core NO DRIFT), "
        "the VLM BOTH PAIRS DIFFERENT ×2 (the pair's documented verdict class — every flag DOM-arbitrated to a documented class), the census 187 axes — 163 identical + 24 documented, ZERO new (the v133 values reproduced EXACTLY), "
        "the ship chain 342 e2e zero flakes (345 executions) + 35/35 smoke, the screenshots 16/16 byte-identical (the same-day law), the dev evidence 4/4 + VLM-verified). |\n"
    )
    text = text.replace(anchor, anchor + v139row)
    io.open(RD, "w", encoding="utf-8").write(text)
    print("D3c README.md: the v139 plan row inserted")

# ---------- D4: zero-balance_SKILL.md ----------
SK = "zero-balance_SKILL.md"
text = io.open(SK, encoding="utf-8").read()
s_line = "project_state: 108 unit tests / 341 e2e tests / 35 smoke steps — all green"
if one_hit(text, s_line, "SKILL project_state line"):
    text = text.replace(
        s_line,
        "project_state: 108 unit tests / 342 e2e tests / 35 smoke steps — all green",
    )
    io.open(SK, "w", encoding="utf-8").write(text)
    print("D4a SKILL.md: the project_state line 341 -> 342")
text = io.open(SK, encoding="utf-8").read()
anchor = "the workspace the SAME-PERSISTED class (the v137 environment held through the session boundary, the seedcheck EXACT before any gate) |** 108/341/35 green |\n"
if one_hit(text, anchor, "SKILL Session 173 row tail"):
    s174 = (
        "| 2026-11-01 | Session 174 — parity iteration v139 (`docs/remediation-plan-v139.md`) | **The re-run cycle's next-oldest candidate (the v133-era ITEMS pair's THIRTEENTH re-run "
        "[v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139], the SIXTY-SECOND consecutive queue/ledger agreement; the v127–v132 rotation pool EXHAUSTED — the cadence's SECOND PASS [the v133–v138 pool], the v133-era pair the oldest remaining) "
        "+ the filter-card Select trigger own-hover ladder pin at 1280 (PIN-ONLY — src/ ZERO changes, the ninth PIN-ONLY cycle in the last ten: the never-pinned hover path of the pinned filter family — every select census AT-REST; "
        "the census measured the ladder CLEAN on BOTH triggers — the INERT-HOVER contract, the at-rest chrome persisting under each trigger's own hover, IDENTICAL both sides at every rung; "
        "the pin-sanity mutation the HOVER-TINT form over:bg-[#f5f5f5] on the SelectTrigger className — hover-scoped, the wider-file blast radius noted, the sole failure verified on the FULL items sweep: 1 failed + 52 passed] "
        "sole-failure verified; the post-restore regression 146/146) — the 133rd standing checks ALL GREEN (the mobile menu the 133rd consecutive; the four reference bugs live; the census clean on the FIRST reads), "
        "the watches green (0 vulnerabilities --omit=dev — the thirtieth; axe-core NO DRIFT), the VLM BOTH PAIRS DIFFERENT ×2 (the pair's documented verdict class — every flag DOM-arbitrated to a documented class; the FAB claim DISPROVEN LIVE [fabCount 0 both sides]), "
        "the census 187 axes — 163 identical + 24 documented, ZERO new (the v133 values reproduced EXACTLY), the ship chain 342 e2e zero flakes (345 executions) + 35/35 smoke, "
        "the screenshots 16/16 byte-identical (the same-day law), the dev evidence 4/4 + VLM-verified; "
        "the workspace the SAME-PERSISTED class (the v138 environment held through the session boundary, the seedcheck EXACT before any gate) |** 108/342/35 green |\n"
    )
    text = text.replace(anchor, anchor + s174)
    io.open(SK, "w", encoding="utf-8").write(text)
    print("D4b SKILL.md: the Session 174 row inserted")

# ---------- D5: Project_Architecture_Document.md ----------
PAD = "Project_Architecture_Document.md"
text = io.open(PAD, encoding="utf-8").read()
anchor = "#### Revision Block — v1.1.95 (Tracked Changes)\n"
if one_hit(text, anchor, "PAD v1.1.95 block head"):
    v1196 = (
        "#### Revision Block — v1.1.96 (Tracked Changes)\n"
        "- `[UI]` v1.1.96 (2026-11-01) — the v139 parity iteration (**PIN-ONLY for src/ — zero production-code changes, the ninth PIN-ONLY cycle in the last ten** + one e2e pin; no config change, no dependency change): "
        "the counts 108 unit / **342 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v133-era ITEMS pair's THIRTEENTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139], "
        "the SIXTY-SECOND consecutive queue/ledger agreement; the v127–v132 rotation pool EXHAUSTED — the cadence enters the SECOND PASS [the v133–v138 pool], the v133-era pair the oldest remaining)**; "
        "the FAB VLM claim DISPROVEN LIVE (base44-fab-arbit-v139.sh — fabCount 0 + bodyHasBase44 false on BOTH sides, the flagged /income surface at 1280); the census 187 axes — 163 identical + 24 documented-class deltas, ZERO new (the v133 values reproduced EXACTLY); "
        "the ONE-block two-half md5 contract held (CENSUS_JS 193 lines b55dcd29 — the v103/v109/v115/v121/v127/v133 lineage digest carried byte-identical); **the pin — the FILTER-CARD SELECT TRIGGER's OWN-HOVER LADDER at 1280** "
        "(the never-pinned hover path of the pinned filter family; THE CONSTRUCT: the trigger carries NO hover: utility [select.tsx:20-27], the own-hover end-state the INERT-HOVER contract — the at-rest chrome persisting under each trigger's own hover; "
        "the both-sides census selecthover-arbit-v139.sh measured the ladder on BOTH triggers CLEAN — NO GAP; the deltas the documented v37 O1 lead-layer construct alone, the VISIBLE pair byte-identical); "
        "the pin-sanity mutation the HOVER-TINT form (hover:bg-[#f5f5f5] on the SelectTrigger className) sole-failure verified live [1 failed + 52 passed in the FULL items sweep — the failure diff the predicted hovered-rung bg axis]; "
        "the post-restore regression 146/146 (items 53 + networth 41 + dashboard 52); the ship chain 342 e2e zero flakes (94+93+76+82 = 345 executions) + 35/35 smoke; the screenshots 16/16 byte-identical (the same-day law); the dev evidence 4/4 byte-identical + VLM-verified; "
        "the 133rd standing checks ALL GREEN (the mobile menu VERIFIED WORKING the 133rd consecutive time); the watches green (npm-audit 0 vulnerabilities — the thirtieth re-check; axe-core NO DRIFT 4.14.0); "
        "the workspace the SAME-PERSISTED class (the v138 environment held, the seedcheck EXACT before any gate).\n"
    )
    text = text.replace(anchor, v1196 + anchor)
    io.open(PAD, "w", encoding="utf-8").write(text)
    print("D5 PAD.md: the v1.1.96 revision block inserted")

print("ALIGN:", "OK" if ok else "FAILED")
sys.exit(0 if ok else 1)
