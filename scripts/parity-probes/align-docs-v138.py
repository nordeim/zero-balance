#!/usr/bin/env python3
"""align-docs-v138.py — D1-D5 of the v138 docs alignment (the D0 anchor
discipline: every insert/replace anchor verified 1-hit BEFORE any write;
the script refuses and exits non-zero on any anchor miss or multi-hit).
  D1 AGENTS.md — the v138 paragraph appended after the v137 paragraph
  D2 CLAUDE.md — the e2e count 340 -> 341 + the v138 clause appended to
     the e2e enumeration line's end (after the v137 clause)
  D3 README.md — the two test-count lines 340 -> 341 + the v138 plan row
     inserted after the v137 row
  D4 zero-balance_SKILL.md — the project_state line 340 -> 341 + the
     Session 173 row inserted after the Session 172 row
  D5 Project_Architecture_Document.md — the v1.1.95 revision block
     inserted before the v1.1.94 block
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
anchor = "restores the Session 170 row's cell to the v135 cycle's own shipped 338.\n\n"
if one_hit(text, anchor, "AGENTS v137-paragraph tail"):
    v138 = (
        "Reference surfaces pinned by the v138 iteration (`docs/remediation-plan-v138.md`) — "
        "**the re-run cycle's next-oldest candidate (the v132-era MOBILE-TWINS pair — the /networth view + the DASHBOARD, both FULL-PAGE at mobile 390x844, the pair's TWELFTH re-run "
        "[v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132 → v138], the SIXTY-FIRST consecutive queue/ledger agreement "
        "— the corrected entries-minus-one convention applied cleanly: the ELEVENTH ordinal recorded in the v132 plan's own header on its 12-entry bracket [v62/v63 the original pair, one entry] → v138 = the TWELFTH, no prose/header conflict; "
        "the v132 shots header carries the FULL bracket form — the documented verification source; the remaining pool {v132} — the last entry of the v127–v132 rotation)** "
        "+ the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, the v68 dedupe holds — one node_modules/axe-core entry verified live) "
        "+ the npm-audit watch at its twenty-ninth re-check (0 VULNERABILITIES --omit=dev — the v110 bump holds: next 16.4.3 + zod 4.6.7; the 16 moderate the accepted dev-only ESLint braces chain) "
        "+ the 132nd standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, "
        "the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; "
        "the clone's mobile menu VERIFIED WORKING the 132nd consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). "
        "**The baseline GREEN ON THE FIRST CHAIN** (the SAME-PERSISTED workspace — the v137 environment held through the session boundary: node_modules 354 entries intact, BOTH chromium pairs [1200 + 1243] in the cache, "
        "the .env [DATABASE_URL=\"file:../db/custom.db\"] + db/ at the repo root intact with the v137-cycle seed, the repo pulled to main @ 22fa2ba; the seedcheck EXACT 7/1850/2235/0/3/2 before any gate [under the env -u discipline, "
        "the sandbox DATABASE_URL pollution live as documented]): lint, typecheck, 108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e [343 executions = 340 unique, ZERO flakes], 35/35 smoke; "
        "the production-seam audit clean; skills/ excluded). "
        "The probe series derived from the v132 lineage (derive-v138-series.py — FOUR explicit session-token families [refvlm/clonevlm + refarbit/clonearbit — the tokens carry '132' without the 'v' prefix] "
        "+ SIX history-correction fragments [the plan pointer \"the v131 plan's own suggestion\"→\"the v137 plan's\"; the era marker last-re-shot v126→v132 + the oldest-remaining list [v126 < … < v131]→[v132]; "
        "the ordinal ELEVENTH→TWELFTH + the bracket extended [→ v120 → v126 → v138]→[→ v120 → v126 → v132 → v138]; the verdicts window \"the v84/v90/v96/v102/v108/v126 re-runs\"→\"…v108/v132 re-runs\"; "
        "the arbit census-axes provenance \"The v126 census axes\"→\"The v132 census axes\"], all applied on the FIRST run, zero residual, line counts preserved 60/47/68/219; the clone file verified zero era tokens — no corrections needed, "
        "the v132 derivation's own finding) + the two-half builder (derive-build-twohalf-v138.py — the session-token bump clonearbit132→clonearbit138 FIRST [the v121 stale-session-fix precedent] + the lesson-range bump v92..v131→v92..v137 "
        "[the BARE range token] + the lineage-note fixup LAST) + the comparator (derive-compare-v138.py — the explicit /tmp/vlm132→/tmp/vlm138 log-path swap + the provenance citations re-pointed at the v132 measurement; "
        "the v132 derivation's latent 'textax' typo fixed in this derivation's residual loop — the correct text[max(0, …)] slice form) "
        "+ the TWO-block two-half contract verified three-way (verify-twohalf-v138.py — NW_CENSUS 42 lines md5 82cf8a43 + DASH_CENSUS 87 lines md5 85e4ec7e — **the v102/v108/v114/v120/v126/v132 lineage digests, carried byte-identical through the version-swap derivation**). "
        "**The VLM verdict — BOTH PAIRS DIFFERENT ×2, the pair's DOCUMENTED VERDICT CLASS** (the same verdict family as the v84/v90/v96/v102/v108/v114/v120/v126/v132 re-runs; every flag in both passes in the documented classes, arbitration-free: "
        "the summary-card tiles side-by-side-vs-stacked the v41 MOBILE-SUPERSET class; the trend-icon claims the PERCEPTION-ARTIFACT class [the contradictory descriptions across the passes while the census axes medallion 64×64 + trendIcon 32×32 "
        "are BYTE-IDENTICAL both sides — the v120/v126/v132 disproof form]; the \"Edit with Base44\" tooltip/FAB the PLATFORM-CHROME class [both passes, both pairs]; the hero pct/balance + the progress-bar + the donut + the stat amounts "
        "the PCT/seed-data classes; the subtitle wrap the RANGE-WALK line-bucketing class; the pass-2 tab-bar spacing claim the v53-documented WIDTH family [the reference's own 432-wide list inside its 464-overflow page]); "
        "the both-sides census **55 axes — 37 identical + 18 documented-class deltas, ZERO new — REPRODUCING the v132 census values EXACTLY** (the same 55/37/18 split, zero drift on every axis: the 18 documented = the v41 mobile-superset family "
        "+ the DASH width-guard family). "
        "**A PIN-ONLY cycle for src/ — zero production-code changes (the eighth PIN-ONLY cycle in the last nine) + one e2e pin (340 → 341): the NETWORTH TABLIST TRIGGER's OWN-HOVER LADDER at mobile 390** "
        "(the never-pinned hover path of the pinned tablist family: the v5 G3 pin the at-rest 2-col grid + the active green state, the v30 G2 the ROVING keyboard, the v50 F2 the full chrome at 640, the v53 F1 the full chrome at 390 — "
        "every tab census AT-REST; the trigger's own-hover END-STATE held by NO spec at ANY viewport; THE CONSTRUCT: the trigger carries NO hover: utility [tabs.tsx:24-38 — the focus-visible + data-[state=active] classes alone], "
        "so the own-hover end-state is the INERT-HOVER contract — the at-rest chrome persisting under each trigger's own hover); "
        "the both-sides one-shot census tabhover-arbit-v138.sh (the v132 badgehover form adapted to the tablist axes: the ROLE-BASED finders [button[role=tab] + aria-selected — the v53 form], the (5,5)-parked ladder, the live-read centers "
        "[the Assets center REF (126,472) / CLONE (108,422), the Liabilities center REF (284,472) / CLONE (283,422)], READ-ONLY per the v46 rule — the Radix tabs activate on pointerdown [the v120 lesson] and a mouse MOVE dispatches no pointerdown, "
        "so the census can never flip the tab) measured the ladder on BOTH triggers — the ACTIVE and the INACTIVE — **CLEAN, NO GAP** (the inert-hover contract IDENTICAL both sides at every rung; the deltas the documented construct classes alone: "
        "the trigger WIDTH family [REF 212 / CLONE 175 — the reference's own 432-wide list inside its 464-overflow page, the v53-documented class] + the shadow LEAD-LAYER count [the v66 invisible class — the VISIBLE pair byte-identical] + "
        "the 0px border token [the engine-preflight default, renders nothing — deliberately unpinned, the v89 metadata form]); "
        "the pin appended (append-pin-v138.py — the at-rest rung → the ACTIVE-HOVERED rung {hoverMatch true + the UNCHANGED at-rest chrome} → the INACTIVE-HOVERED rung → the restored rung {toEqual the first rung}; the V94-COLLISION-safe axis set; "
        "the triggers never clicked; GREEN on the first run; the authoritative --list: 341 in 24 files); "
        "the pin-sanity mutation — the HOVER-TINT form (hover:bg-[#f5f5f5] prepended to the TabsTrigger's className at tabs.tsx:34 — cascade-free BY CONSTRUCTION [hover-scoped; the component used only by net-worth-view.tsx — verified: zero other importers]) "
        "sole-failure verified live [1 failed + 40 passed in the FULL networth sweep — the failure diff EXACTLY the predicted hovered-rung axis: the INACTIVE twin's bg rgb(245,245,245) — the mutation's tint — vs the persisted at-rest rgba(0,0,0,0) expected, "
        "hoverMatch true preserved; the ACTIVE twin's hovered rung stayed GREEN under the mutation — the data-[state=active]:bg-[#dcfce7] rule holds the same-specificity cascade, the tint surfacing only on the muted twin]; "
        "restored (git diff src/ = 0 lines) + the FULL REBUILD + the post-restore regression 143 passed (networth 40 + dashboard 51 + items 51 + the setup — the v137/v136/v134 pins' different-file immunity verified live). "
        "The ship chain **341 e2e zero flakes** (93+93+76+82 = 344 executions = 341 unique — the +1 landing in ch3 [networth]; both closed watches green through the chain); 35/35 smoke; "
        "**the screenshots 16/16 captured — 15 byte-identical + 07-add-item-modal the DETERMINISTIC CROSS-DAY DATE-CLASS refresh (the first cross-day capture since v131's own: the modal's todayIso() default shifted Oct 31 → Nov 1 UTC; "
        "the DB-derived surfaces unchanged — the persisted seed's fixed dates render identically)**; "
        "the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: the sheet closed, the heading \"Income\", the top bar + toggle + brand; the dev-shots scripts derived v137→v138 with the version-swap-only verification).\n\n"
    )
    text = text.replace(anchor, anchor + v138)
    io.open(AG, "w", encoding="utf-8").write(text)
    print("D1 AGENTS.md: the v138 paragraph appended")

# ---------- D2: CLAUDE.md ----------
CL = "CLAUDE.md"
text = io.open(CL, encoding="utf-8").read()
if one_hit(text, "E2E (Playwright, 340)", "CLAUDE e2e count"):
    text = text.replace("E2E (Playwright, 340)", "E2E (Playwright, 341)")
    io.open(CL, "w", encoding="utf-8").write(text)
    print("D2a CLAUDE.md: 340 -> 341")
text = io.open(CL, encoding="utf-8").read()
anchor = "the post-restore regression 142/142 [dashboard 52 + networth 39 + items 51 — the v136/v134 pins' different-file immunity verified live])\n"
if one_hit(text, anchor, "CLAUDE v137 clause tail"):
    v138clause = (
        "; the v138 pin — the NETWORTH TABLIST TRIGGER's OWN-HOVER LADDER at 390 (the PIN-ONLY form — src/ ZERO changes, the eighth PIN-ONLY cycle in the last nine: "
        "the never-pinned hover path of the pinned tablist family [every tab census AT-REST — the v5 G3 grid + active state, the v30 G2 roving keyboard, the v50 F2 chrome at 640, the v53 F1 chrome at 390]; "
        "THE CONSTRUCT: the trigger carries NO hover: utility [tabs.tsx:24-38], so the own-hover end-state is the INERT-HOVER contract — the at-rest chrome persisting under each trigger's own hover; "
        "the both-sides census tabhover-arbit-v138.sh measured the ladder on BOTH triggers CLEAN — the inert-hover contract IDENTICAL both sides at every rung [the Assets center REF (126,472) / CLONE (108,422)], "
        "the construct deltas [the trigger width family + the v66 shadow lead-layer class + the 0px border token] the documented classes — NO GAP, NO REPAIR; the pin: the at-rest rung → the ACTIVE-HOVERED rung → the INACTIVE-HOVERED rung → "
        "the restored rung, GREEN on the first run, --list 341 in 24 files; the pin-sanity mutation the HOVER-TINT form [hover:bg-[#f5f5f5] prepended to the TabsTrigger's className — cascade-free by construction, hover-scoped] "
        "sole-failure verified live [1 failed + 40 passed in the full networth sweep — the failure diff the INACTIVE twin's bg tint vs the persisted at-rest transparent, hoverMatch true preserved; the ACTIVE twin's hovered rung green under the mutation — "
        "the data-[state=active]:bg rule holds the same-specificity cascade]; the post-restore regression 143/143 [networth 40 + dashboard 51 + items 51 — the v137/v136/v134 pins' different-file immunity verified live])\n"
    )
    text = text.replace(anchor, anchor[:-1] + v138clause)
    io.open(CL, "w", encoding="utf-8").write(text)
    print("D2b CLAUDE.md: the v138 clause appended")

# ---------- D3: README.md ----------
RM = "README.md"
text = io.open(RM, encoding="utf-8").read()
if text.count("(340 tests)") == 2:
    text = text.replace("(340 tests)", "(341 tests)")
    io.open(RM, "w", encoding="utf-8").write(text)
    print("D3a README.md: the two count lines 340 -> 341")
text = io.open(RM, encoding="utf-8").read()
anchor = "the SKILL project_state line repaired (the v136 cycle left it stale at 338)). |\n"
if one_hit(text, anchor, "README v137 row tail"):
    v138row = (
        "| [`docs/remediation-plan-v138.md`](docs/remediation-plan-v138.md) | **The re-run cycle's next-oldest candidate (the v132-era MOBILE-TWINS pair's TWELFTH re-run — the /networth view + the DASHBOARD, both FULL-PAGE at mobile 390x844, "
        "the SIXTY-FIRST consecutive queue/ledger agreement; the remaining pool {v132} — the last entry of the v127–v132 rotation) + the tablist trigger own-hover ladder pin at 390 (PIN-ONLY — src/ zero changes, the eighth PIN-ONLY cycle in the last nine; "
        "the census measured the ladder CLEAN on BOTH triggers: the INERT-HOVER contract — the at-rest chrome persisting under each trigger's own hover — IDENTICAL both sides at every rung; "
        "the pin-sanity mutation the HOVER-TINT form [hover:bg-[#f5f5f5] on the TabsTrigger className — cascade-free by construction] sole-failure verified [1 failed + 40 passed]; "
        "the post-restore regression 143/143) — the 132nd standing checks ALL GREEN (the mobile menu the 132nd consecutive), the watches green (0 vulnerabilities --omit=dev, axe-core NO DRIFT), "
        "the VLM BOTH PAIRS DIFFERENT ×2 (the pair's documented verdict class — every flag DOM-arbitrated to a documented class: the v41 mobile-superset, the trend-icon perception-artifact [the census disproof], the Base44 platform chrome, "
        "the PCT/seed-data classes, the subtitle Range-walk, the tab-bar width family), the census 55/37/18 reproducing the v132 values EXACTLY, "
        "the ship chain 341 e2e zero flakes + 35/35 smoke, the screenshots 16/16 (15 byte-identical + the add-item modal the deterministic cross-day date-class refresh — the first cross-day capture since v131), the dev evidence 4/4 + VLM-verified). |\n"
    )
    text = text.replace(anchor, anchor + v138row)
    io.open(RM, "w", encoding="utf-8").write(text)
    print("D3b README.md: the v138 plan row inserted")

# ---------- D4: zero-balance_SKILL.md ----------
SK = "zero-balance_SKILL.md"
text = io.open(SK, encoding="utf-8").read()
s_line = "project_state: 108 unit tests / 340 e2e tests / 35 smoke steps — all green"
if one_hit(text, s_line, "SKILL project_state line"):
    text = text.replace(
        s_line,
        "project_state: 108 unit tests / 341 e2e tests / 35 smoke steps — all green",
    )
    io.open(SK, "w", encoding="utf-8").write(text)
    print("D4a SKILL.md: the project_state line 340 -> 341")
text = io.open(SK, encoding="utf-8").read()
anchor = "the docs repair: the project_state line recovered from the v136 cycle's stale 338 to the current 340 |** 108/340/35 green |\n"
if one_hit(text, anchor, "SKILL Session 172 row tail"):
    s173 = (
        "| 2026-11-01 | Session 173 — parity iteration v138 (`docs/remediation-plan-v138.md`) | **The re-run cycle's next-oldest candidate (the v132-era MOBILE-TWINS pair's TWELFTH re-run "
        "[v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132 → v138], the SIXTY-FIRST consecutive queue/ledger agreement; the remaining pool {v132} — the last entry of the v127–v132 rotation) "
        "+ the tablist trigger own-hover ladder pin at 390 (PIN-ONLY — src/ ZERO changes, the eighth PIN-ONLY cycle in the last nine: the never-pinned hover path of the pinned tablist family — every tab census AT-REST; "
        "the census measured the ladder CLEAN on BOTH triggers — the INERT-HOVER contract, the at-rest chrome persisting under each trigger's own hover, IDENTICAL both sides at every rung; "
        "the pin-sanity mutation the HOVER-TINT form [hover:bg-[#f5f5f5] on the TabsTrigger className — cascade-free by construction] sole-failure verified: 1 failed + 40 passed in the full networth sweep; "
        "the post-restore regression 143/143) — the 132nd standing checks ALL GREEN (the mobile menu the 132nd consecutive; the four reference bugs live; the census clean on the FIRST reads), "
        "the watches green (0 vulnerabilities --omit=dev — the twenty-ninth; axe-core NO DRIFT), the VLM BOTH PAIRS DIFFERENT ×2 (the pair's documented verdict class — every flag DOM-arbitrated to a documented class), "
        "the census 55 axes — 37 identical + 18 documented, ZERO new (the v132 values reproduced EXACTLY), the ship chain 341 e2e zero flakes (344 executions) + 35/35 smoke, "
        "the screenshots 16/16 (15 byte-identical + the add-item modal the deterministic cross-day date-class refresh — the first cross-day capture since v131), the dev evidence 4/4 + VLM-verified; "
        "the workspace the SAME-PERSISTED class (the v137 environment held through the session boundary, the seedcheck EXACT before any gate) |** 108/341/35 green |\n"
    )
    text = text.replace(anchor, anchor + s173)
    io.open(SK, "w", encoding="utf-8").write(text)
    print("D4b SKILL.md: the Session 173 row inserted")

# ---------- D5: Project_Architecture_Document.md ----------
PAD = "Project_Architecture_Document.md"
text = io.open(PAD, encoding="utf-8").read()
anchor = "#### Revision Block — v1.1.94 (Tracked Changes)"
if one_hit(text, anchor, "PAD v1.1.94 block heading"):
    v1195 = (
        "#### Revision Block — v1.1.95 (Tracked Changes)\n"
        "- `[UI]` v1.1.95 (2026-11-01) — the v138 parity iteration (**PIN-ONLY for src/ — zero production-code changes, the eighth PIN-ONLY cycle in the last nine** + one e2e pin; "
        "no config change, no dependency change): the counts 108 unit / **341 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v132-era MOBILE-TWINS pair's TWELFTH re-run "
        "[v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132 → v138], the SIXTY-FIRST consecutive queue/ledger agreement; the remaining pool {v132} — the last entry of the v127–v132 rotation)** "
        "+ the NETWORTH TABLIST TRIGGER's OWN-HOVER LADDER pin at mobile 390 (the never-pinned hover path of the pinned tablist family: the trigger carries NO hover: utility [tabs.tsx:24-38], so the own-hover end-state is "
        "the INERT-HOVER contract — the at-rest chrome persisting under each trigger's own hover, measured byte-identical both sides on BOTH triggers by the one-shot census tabhover-arbit-v138.sh — NO GAP, NO REPAIR; "
        "the pin-sanity mutation the HOVER-TINT form [hover:bg-[#f5f5f5] prepended to the TabsTrigger's className — cascade-free by construction: hover-scoped, the component used only by net-worth-view.tsx] sole-failure verified live "
        "[1 failed + 40 passed in the full networth sweep — the failure diff the INACTIVE twin's bg tint vs the persisted at-rest transparent]; the post-restore regression 143/143); "
        "the 132nd standing checks ALL GREEN (the mobile menu the 132nd consecutive); the VLM verdict BOTH PAIRS DIFFERENT ×2 (the pair's documented verdict class — every flag DOM-arbitrated to a documented class: the v41 mobile-superset, "
        "the trend-icon perception-artifact [the census disproof], the Base44 platform chrome, the PCT/seed-data classes, the subtitle Range-walk, the tab-bar width family); the both-sides census 55 axes — 37 identical + 18 documented-class deltas, "
        "ZERO new (the v132 values reproduced EXACTLY); the ship chain 341 e2e zero flakes (344 executions) + 35/35 smoke; the screenshots 16/16 (15 byte-identical + the add-item modal the deterministic cross-day date-class refresh — "
        "the first cross-day capture since v131: the modal's todayIso() default shifted Oct 31 → Nov 1 UTC, the DB-derived surfaces unchanged under the persisted seed); the dev evidence 4/4 + VLM-verified; "
        "the workspace the SAME-PERSISTED class (the v137 environment held through the session boundary).\n\n"
    )
    text = text.replace(anchor, v1195 + anchor)
    io.open(PAD, "w", encoding="utf-8").write(text)
    print("D5 PAD.md: the v1.1.95 revision block inserted")

print("DONE" if ok else "FAILED — anchor misses above")
sys.exit(0 if ok else 1)
