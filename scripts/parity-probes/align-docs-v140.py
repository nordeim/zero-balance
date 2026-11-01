#!/usr/bin/env python3
"""align-docs-v140.py — D1-D5 of the v140 docs alignment (the D0 anchor
discipline: every insert/replace anchor verified 1-hit BEFORE any write;
the script refuses and exits non-zero on any anchor miss or multi-hit).
  D1 AGENTS.md — the v140 paragraph appended after the v139 paragraph
  D2 CLAUDE.md — the e2e count 342 -> 343 + the v140 clause appended to
     the e2e enumeration line's end (after the v139 clause)
  D3 README.md — the two test-count lines 342 -> 343 + the v140 plan row
     inserted after the v139 row
  D4 zero-balance_SKILL.md — the project_state line 342 -> 343 + the
     Session 175 row inserted after the Session 174 row
  D5 Project_Architecture_Document.md — the v1.1.97 revision block
     inserted before the v1.1.96 block
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
anchor = "the dev-shots scripts derived v138→v139 with the version-swap-only verification).\n\n"
if one_hit(text, anchor, "AGENTS v139-paragraph tail"):
    v140 = (
        "Reference surfaces pinned by the v140 iteration (`docs/remediation-plan-v140.md`) — "
        "**the re-run cycle's second-pass next-oldest candidate (the v134-era SAVINGS pair — the SAVINGS view at desktop 1280x800 FULL-PAGE, the pair's THIRTEENTH re-run "
        "[v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128 → v134 → v140], the SIXTY-THIRD consecutive queue/ledger agreement "
        "— the corrected entries-minus-one convention applied cleanly: the TWELFTH ordinal recorded in the v134 plan's own header on its 13-entry bracket [v58 the original, one entry] → v140 = the THIRTEENTH; "
        "the surface-family name 'the v128-era savings pair' preserved — the lineage's own designation) "
        "+ the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, the v68 dedupe holds — one node_modules/axe-core entry verified live) "
        "+ the npm-audit watch at its thirty-first re-check (0 VULNERABILITIES --omit=dev — the v110 bump holds: next 16.4.3 + zod 4.6.7; the 16 moderate the accepted dev-only ESLint braces chain) "
        "+ the 134th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, "
        "the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; "
        "the clone's mobile menu VERIFIED WORKING the 134th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). "
        "**The baseline GREEN ON THE FIRST CHAIN** (the SAME-PERSISTED workspace — the v139 environment held through the session boundary: node_modules 354 entries intact, BOTH chromium pairs [1200 + 1243], "
        "the .env [DATABASE_URL=\"file:../db/custom.db\"] + db/ at the repo root intact with the v139-cycle seed, the repo pulled to main @ a1abcdc [the session-log commit, +1 file docs/session_346.md]; the seedcheck EXACT 7/1850/2235/0/3/2 before any gate; "
        "the sandbox DATABASE_URL pollution live as documented]): lint, typecheck, 108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e [345 executions = 342 unique, ZERO flakes], 35/35 smoke, "
        "the production-seam audit clean; skills/ excluded). "
        "The probe series derived from the v134 lineage (derive-v140-series.py — FOUR explicit session-token families [refvlm/clonevlm + refarbit/clonearbit — the tokens carry '134' without the 'v' prefix, so the bare version swap cannot touch them] "
        "+ FOUR history-correction fragments [the era marker last-re-shot v128→v134 + the oldest-remaining list v128..v132→v134..v138 + the queue source the v133 plan→the v139 plan + the agreement counter FIFTY-SEVENTH→SIXTY-THIRD; the ordinal TWELFTH→THIRTEENTH + the bracket extended in all four files], "
        "all applied on the FIRST run, zero residual, line counts preserved 50/42/39/262 == the v134 lineage exactly) "
        "+ the two-half builder (derive-build-twohalf-v140.py — the builder's ref_exec ASSERTION's stale refarbit134 bumped to refarbit140 FIRST [the no-'v'-prefix token — the v121 stale-session precedent, this lineage's assertion form] + the lesson-range bump v92..v133→v92..v139 [the BARE range token] + the lineage-note fixup LAST) "
        "+ the comparator (derive-compare-v140.py — the generic swap + the provenance citations re-pointed at the v134 measurement) "
        "+ the ONE-block two-half contract verified three-way (verify-twohalf-v140.py — SV_CENSUS_JS 153 lines md5 891ab9b6 — **the v122/v128/v134 lineage digest, carried byte-identical through the version-swap derivation**). "
        "**The VLM verdict — DIFFERENT ×2, the savings pair's CONSISTENT FORM** (the same verdict family as the v122/v128/v134 re-runs; every flag in both passes in the documented classes, arbitration-free this cycle — every flag's class already DOM-confirmed by the census's own whitelisted quads: the avatar letter USER-IDENTITY; "
        "the card-grid SEED-COUNT [the reference's 1-item savings seed vs the clone's 2-item dev seed — the grid template census byte-identical 309.328px ×3]; "
        "the card-footer payment chips the v57 DATA-CONDITIONAL class [the reference's savings item ships no paymentMethod — its footer childCount 1 vs the clone's 2]; "
        "the badge family the classification-VALUE + v57 wrap classes [badgeRow h 22 vs 52 + n 3 vs 4 — the Recurring superset chip + the wrap consequence]; "
        "the header stats + card contents the SEED-DATA classes; NO FAB/platform-chrome claim raised in either pass — no arbitration script needed); "
        "the both-sides census **120 axes — 80 identical + 40 documented-class deltas, ZERO new — REPRODUCING the v134 census values EXACTLY** (the same 120/80/40 split, zero drift on every axis). "
        "**A PIN-ONLY cycle for src/ — zero production-code changes (the tenth PIN-ONLY cycle in the last eleven) + one e2e pin (342 → 343): the SAVINGS FILTER-CARD SEARCH INPUT's OWN-HOVER LADDER at desktop 1280x800 on /savings** "
        "(the never-pinned hover path of the pinned search family: the v37 S2 pin the input's focus-visible family + the REAL-key typing contract, the v64 census the /income at-rest geometry, the v38 S2 pin the /savings class-level chrome, the v134 survey the /savings at-rest + FOCUS ring — every search census AT-REST or FOCUS; "
        "THE CONSTRUCT: the input carries NO hover: utility [input.tsx:10 — the focus-visible + disabled + placeholder classes alone], "
        "so the own-hover end-state is the INERT-HOVER contract — the at-rest chrome persisting under the input's own hover); "
        "the both-sides one-shot census searchhover-arbit-v140.sh (the v139 selecthover form adapted to the search-input axis: the STRUCTURAL finder [the rounded-2xl white card containing an input → its ONLY input — tag-agnostic, shared by both sites; the placeholder cross-checked], the (5,5)-parked ladder, the live-read center [REF (537,167) / CLONE (537,167) — IDENTICAL coordinates], "
        "READ-ONLY — a mouse MOVE on an input dispatches no click and the input opens nothing on hover) measured the ladder **CLEAN, NO GAP** (the inert-hover contract IDENTICAL both sides at every rung; the deltas the documented construct classes alone: the shadow LEAD-LAYER count [the v37 O1 note — the v3 three-slot vs the TW v4 five-slot construct, every lead a 0px-spread shadow invisible by construction; the VISIBLE pair byte-identical] + the transitionProperty metadata [the v3 6-prop list vs the v4 gradient-var compile — the v95 family, never pinned; the duration 0.15s identical]); "
        "the pin appended (append-pin-v140.py — the at-rest rung → the SEARCH-HOVERED rung {hoverMatch true + the UNCHANGED at-rest chrome} → the restored rung; "
        "the STRUCTURAL finder; the input never clicked; GREEN on the first run; the authoritative --list: 343 in 24 files); "
        "the pin-sanity mutation — the HOVER-TINT form (hover:bg-[#f5f5f5] prepended to the Input's className at input.tsx:10 — cascade-checked BY CONSTRUCTION: hover-scoped; the WIDER-FILE blast radius noted [input.tsx serves EVERY Input in the app], "
        "the sole-failure criterion verified on the FULL ITEMS SWEEP ALONE) sole-failure verified live [1 failed + 53 passed in the FULL items sweep — the failure diff EXACTLY the predicted hovered-rung axis: the input's bg rgb(245,245,245) — the mutation's tint — vs the persisted at-rest rgba(0,0,0,0) expected, hoverMatch true preserved, the border/color axes untouched]; "
        "restored (git diff src/ = 0 lines) + the FULL REBUILD + the post-restore regression 145 passed (items 54 + networth 40 + dashboard 52 — the v139/v138/v134 pins' different-file immunity verified live). "
        "The ship chain **343 e2e zero flakes** (95+93+76+82 = 346 executions = 343 unique — the +1 landing in ch1 [items]; both closed watches green through the chain); 35/35 smoke; "
        "**the screenshots 16/16 captured — ALL byte-identical (the same-day law: both this cycle and v139 captured Nov 1 UTC, every date-bearing surface rendering identically under the persisted seed)**; "
        "the dev evidence 4/4 byte-identical + VLM-verified (the menu proof {\"url\":\"/income\",\"docSW\":390,\"navLandmark\":true}; the dev-shots scripts derived v139→v140 with the version-swap-only verification)."
    )
    text = text.replace(anchor, anchor + v140 + "\n\n")
    io.open(AG, "w", encoding="utf-8").write(text)
    print("D1 AGENTS.md: the v140 paragraph appended")

# ---------- D2: CLAUDE.md ----------
CM = "CLAUDE.md"
text = io.open(CM, encoding="utf-8").read()
if one_hit(text, "- **E2E (Playwright, 342)**:", "CLAUDE e2e count"):
    text = text.replace("- **E2E (Playwright, 342)**:", "- **E2E (Playwright, 343)**:")
tail = "the post-restore regression 146/146 [items 53 + networth 41 + dashboard 52 — the v138/v137/v133 pins' different-file immunity verified live])"
if one_hit(text, tail, "CLAUDE v139-clause tail"):
    clause = (
        ", and the savings filter-card search input's own-hover ladder at 1280 (v140 — the cycle's own savings-pair surface: the never-pinned hover path of the pinned search family "
        "[the v37 S2 pin the focus-visible family, the v64 census the at-rest geometry, the v134 survey the at-rest + FOCUS ring — every search census AT-REST or FOCUS]; "
        "the input carries NO hover: utility [input.tsx:10], so the own-hover end-state is the INERT-HOVER contract — the at-rest chrome persisting under the input's own hover, "
        "measured byte-identical both sides by searchhover-arbit-v140.sh — NO GAP, the PIN-ONLY form; the pin-sanity mutation hover:bg-[#f5f5f5] on the Input className — "
        "hover-scoped by construction, the wider-file blast radius noted [input.tsx serves EVERY Input in the app], the sole failure verified on the FULL items sweep: 1 failed + 53 passed, "
        "the failure diff the predicted hovered-rung bg axis; the post-restore regression 145/145 [items 54 + networth 40 + dashboard 52 — the v139/v138/v134 pins' different-file immunity verified live])"
    )
    text = text.replace(tail, tail + clause)
    io.open(CM, "w", encoding="utf-8").write(text)
    print("D2 CLAUDE.md: 342 -> 343 + the v140 clause appended")

# ---------- D3: README.md ----------
RM = "README.md"
text = io.open(RM, encoding="utf-8").read()
n = text.count("(342 tests)")
if n == 2:
    text = text.replace("(342 tests)", "(343 tests)")
    print("D3 README.md: both test-count lines 342 -> 343")
else:
    print(f"ANCHOR MISS (README counts): {n} hits for '(342 tests)'")
    ok = False
row_anchor = "docs/remediation-plan-v139.md"
if one_hit(text, f"[`{row_anchor}`]", "README v139 row link"):
    idx = text.index(f"[`{row_anchor}`]")
    line_end = text.index("\n", idx)
    v140_row = (
        "\n| [`docs/remediation-plan-v140.md`](docs/remediation-plan-v140.md) | **The re-run cycle's second-pass next-oldest candidate (the v134-era SAVINGS pair's THIRTEENTH re-run — the SAVINGS view at desktop 1280x800 FULL-PAGE, the SIXTY-THIRD consecutive queue/ledger agreement; the savings filter-card search input's own-hover ladder pin at 1280 — the never-pinned hover path of the pinned search family, the INERT-HOVER contract measured byte-identical both sides; PIN-ONLY: src/ zero changes, 343 e2e)** |"
    )
    text = text[: line_end] + v140_row + text[line_end:]
    io.open(RM, "w", encoding="utf-8").write(text)
    print("D3 README.md: the v140 plan row inserted after the v139 row")

# ---------- D4: zero-balance_SKILL.md ----------
SK = "zero-balance_SKILL.md"
text = io.open(SK, encoding="utf-8").read()
if one_hit(text, "project_state: 108 unit tests / 342 e2e tests / 35 smoke steps — all green", "SKILL state line"):
    text = text.replace(
        "project_state: 108 unit tests / 342 e2e tests / 35 smoke steps — all green",
        "project_state: 108 unit tests / 343 e2e tests / 35 smoke steps — all green",
    )
row = "| 2026-11-01 | Session 174 — parity iteration v139 (`docs/remediation-plan-v139.md`)"
if one_hit(text, row, "SKILL Session 174 row head"):
    idx = text.index(row)
    line_end = text.index("\n", idx)
    v140_row = (
        "\n| 2026-11-01 | Session 175 — parity iteration v140 (`docs/remediation-plan-v140.md`) | **The re-run cycle's second-pass next-oldest candidate (the v134-era SAVINGS pair's THIRTEENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128 → v134 → v140], the SIXTY-THIRD consecutive queue/ledger agreement; the VLM verdict DIFFERENT ×2 — the savings pair's consistent form, every flag in the documented classes arbitration-free; the census 120 axes — 80 identical + 40 documented, ZERO new — the v134 values reproduced EXACTLY; the ONE-block md5 contract 891ab9b6 held; PIN-ONLY for src/ + one e2e pin [343]: the SAVINGS FILTER-CARD SEARCH INPUT's OWN-HOVER LADDER at 1280 — the never-pinned hover path of the pinned search family, the INERT-HOVER contract measured byte-identical both sides [center (537,167) IDENTICAL]; the pin-sanity mutation sole-failure verified live [1 failed + 53 passed — the failure diff the predicted hovered-rung bg axis]; the post-restore regression 145/145; the ship chain 343 e2e zero flakes + 35/35 smoke; the screenshots 16/16 byte-identical [the same-day law]; the dev evidence 4/4 + VLM-verified; the 134th standing checks ALL GREEN — the mobile menu VERIFIED WORKING the 134th consecutive time)** |"
    )
    text = text[: line_end] + v140_row + text[line_end:]
    io.open(SK, "w", encoding="utf-8").write(text)
    print("D4 SKILL: state line 342 -> 343 + the Session 175 row inserted")

# ---------- D5: Project_Architecture_Document.md ----------
PAD = "Project_Architecture_Document.md"
text = io.open(PAD, encoding="utf-8").read()
if one_hit(text, "#### Revision Block — v1.1.96 (Tracked Changes)", "PAD v1.1.96 head"):
    block = (
        "#### Revision Block — v1.1.97 (Tracked Changes)\n"
        "- `[UI]` v1.1.97 (2026-11-01) — the v140 parity iteration (**PIN-ONLY for src/ — zero production-code changes, the tenth PIN-ONLY cycle in the last eleven** + one e2e pin; no config change, no dependency change): the counts 108 unit / **343 e2e** (+1) / 35 smoke; **the re-run cycle's second-pass next-oldest candidate (the v134-era SAVINGS pair's THIRTEENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128 → v134 → v140], the SIXTY-THIRD consecutive queue/ledger agreement; the surface-family name 'the v128-era savings pair' preserved — the lineage's own designation)**; the VLM verdict DIFFERENT ×2 (the savings pair's consistent form — every flag in the documented classes, arbitration-free this cycle: every flag's class DOM-confirmed by the census's own whitelisted quads; NO FAB claim raised); the census 120 axes — 80 identical + 40 documented-class deltas, ZERO new (the v134 values reproduced EXACTLY); the ONE-block two-half md5 contract held (SV_CENSUS_JS 153 lines 891ab9b6 — the v122/v128/v134 lineage digest carried byte-identical); **the pin — the SAVINGS FILTER-CARD SEARCH INPUT's OWN-HOVER LADDER at 1280** (the never-pinned hover path of the pinned search family; THE CONSTRUCT: the input carries NO hover: utility [input.tsx:10], the own-hover end-state the INERT-HOVER contract — the at-rest chrome persisting under the input's own hover; the both-sides census searchhover-arbit-v140.sh measured the ladder CLEAN — NO GAP [the center REF (537,167) / CLONE (537,167), IDENTICAL coordinates]; the deltas the documented v37 O1 lead-layer construct + the transitionProperty metadata [the v95 family] alone, the VISIBLE pair byte-identical); the pin-sanity mutation the HOVER-TINT form (hover:bg-[#f5f5f5] on the Input className — the WIDER-FILE blast radius noted: input.tsx serves EVERY Input in the app; the sole-failure criterion verified on the FULL ITEMS SWEEP ALONE) sole-failure verified live [1 failed + 53 passed — the failure diff the predicted hovered-rung bg axis]; the post-restore regression 145/145 (items 54 + networth 40 + dashboard 52); the ship chain 343 e2e zero flakes (95+93+76+82 = 346 executions) + 35/35 smoke; the screenshots 16/16 byte-identical (the same-day law); the dev evidence 4/4 byte-identical + VLM-verified; the 134th standing checks ALL GREEN (the mobile menu VERIFIED WORKING the 134th consecutive time); the watches green (npm-audit 0 vulnerabilities — the thirty-first re-check; axe-core NO DRIFT 4.14.0); the workspace the SAME-PERSISTED class (the v139 environment held, the seedcheck EXACT before any gate).\n\n"
    )
    text = text.replace("#### Revision Block — v1.1.96 (Tracked Changes)", block + "#### Revision Block — v1.1.96 (Tracked Changes)", 1)
    io.open(PAD, "w", encoding="utf-8").write(text)
    print("D5 PAD: the v1.1.97 revision block inserted")

sys.exit(0 if ok else 1)
