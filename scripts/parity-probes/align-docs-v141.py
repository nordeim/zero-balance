#!/usr/bin/env python3
"""align-docs-v141.py — D1-D5 of the v141 docs alignment (the D0 anchor
discipline: every insert/replace anchor verified 1-hit BEFORE any write;
the script refuses and exits non-zero on any anchor miss or multi-hit).
  D1 AGENTS.md — the v141 paragraph appended after the v140 paragraph
  D2 CLAUDE.md — the e2e count 343 -> 344 + the v141 clause appended to
     the e2e enumeration line's end (after the v140 clause)
  D3 README.md — the two test-count lines 343 -> 344 + the v141 plan row
     inserted after the v140 row
  D4 zero-balance_SKILL.md — the project_state line 343 -> 344 + the
     Session 176 row inserted after the Session 175 row
  D5 Project_Architecture_Document.md — the v1.1.98 revision block
     inserted before the v1.1.97 block
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
anchor = "the dev-shots scripts derived v139→v140 with the version-swap-only verification).\n\n"
if one_hit(text, anchor, "AGENTS v140-paragraph tail"):
    v141 = (
        "Reference surfaces pinned by the v141 iteration (`docs/remediation-plan-v141.md`) — "
        "**the re-run cycle's second-pass next-oldest candidate (the v135-era LOGIN + CALCULATOR pair — the LOGIN view + the CALCULATOR dialog at desktop 1280x800, the pair's THIRTEENTH re-run "
        "[v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141], the SIXTY-FOURTH consecutive queue/ledger agreement "
        "— the corrected entries-minus-one convention applied cleanly: the TWELFTH ordinal recorded in the v135 plan's own header on its 13-entry bracket [v59 the original, one entry] → v141 = the THIRTEENTH; "
        "the surface-family name 'the v129-era LOGIN + CALCULATOR pair' preserved — the lineage's own designation, the v139/v140 preservation precedent) "
        "+ the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, the v68 dedupe holds — one node_modules/axe-core entry verified live) "
        "+ the npm-audit watch at its thirty-second re-check (0 VULNERABILITIES --omit=dev — the v110 bump holds: next 16.4.3 + zod 4.6.7; the 16 moderate the accepted dev-only ESLint braces chain) "
        "+ the 135th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, "
        "the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; "
        "the clone's mobile menu VERIFIED WORKING the 135th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). "
        "**The baseline GREEN ON THE FIRST CHAIN** (the SAME-PERSISTED workspace — the v140 environment held through the session boundary: node_modules 354 entries intact, BOTH chromium pairs [1200 + 1243], "
        "the .env [DATABASE_URL=\"file:../db/custom.db\"] + db/ at the repo root intact with the v140-cycle seed, the repo pulled to main @ 69f91be [the session-log commit, +1 file docs/session_349.md]; the seedcheck EXACT 7/1850/2235/0/3/2 before any gate; "
        "the sandbox DATABASE_URL pollution live as documented]): lint, typecheck, 108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e [346 executions = 343 unique, ZERO flakes], 35/35 smoke, "
        "the production-seam audit clean; skills/ excluded). "
        "The probe series derived from the v135 lineage (derive-v141-series.py — SIX explicit session-token families [refvlm/clonevlm + refcalc/clonecalc + reflogin/clonelogin arbit — the tokens carry '135' without the 'v' prefix, so the bare version swap cannot touch them] "
        "+ the history-correction fragments [the era marker last-re-shot v129→v135 + the oldest-remaining list v129..v132→v135..v138 + the queue source the v134 plan→the v140 plan + the agreement counter FIFTY-EIGHTH→SIXTY-FOURTH; the ordinal TWELFTH→THIRTEENTH + the bracket extended in all four files], "
        "all applied on the FIRST run, zero residual, line counts preserved 102/166/65/355 == the v135 lineage exactly) "
        "+ the login-shots sub-series (derive-loginshots-v141.py — 30/30 preserved) "
        "+ the two-half builder (derive-build-twohalf-v141.py — the generic swap + the lesson-range bump v92..v134→v92..v140 [the BARE range token] + the lineage-note fixup LAST) "
        "+ the comparator (derive-compare-v141.py — the generic swap incl. the EXPLICIT /tmp/vlm135→/tmp/vlm141 log-path swap [the path token carries no 'v135' substring — the derivation's own first-run miss, caught by the residual check and fixed before any execution] + the provenance citations re-pointed at the v135 measurement [the records chain extended +v135]) "
        "+ the TWO-block two-half contract verified three-way (verify-twohalf-v141.py — CALC_CENSUS_JS 61 lines md5 e1092d12d06677a4 + LOGIN_CENSUS_JS 36 lines md5 9e5a52d2ab0f2ab9 — **the v123/v129/v135 lineage digests, carried byte-identical through the version-swap derivation**). "
        "**The VLM verdict — CALCULATOR DIFFERENT ×2 / LOGIN IDENTICAL ×2, the pair's documented verdict-VARIATION family** (the login verdict has varied IDENTICAL/DIFFERENT across re-runs — v105/v129 IDENTICAL, v135 pass 2 DIFFERENT-with-the-sole-disproven-flag; here IDENTICAL both passes with the sole FAB note "
        "**DISPROVEN LIVE by base44-fab-arbit-v141.sh** [fabCount 0 + bodyHasBase44 false on BOTH sides at 1280 /login — the standing v97..v135 disproof form re-confirmed]; every calculator flag in both passes in the documented classes: the hover action buttons the POINTER-POSITION/HOVER-STATE screenshot artifact [the census actionsAtRest {opacity 0, btnCount 2} IDENTICAL both sides], "
        "the 'Will update category total' note the SEED-DATA class [ref false vs clone true — totalCard.hasWillUpdateSpan]); "
        "the both-sides census **106 axes — 97 identical + 9 documented-class deltas, ZERO new — REPRODUCING the v135 census values EXACTLY** (the same 106/97/9 split, zero drift on every axis; the close-key asymmetry direction HOLDS). "
        "**A PIN-ONLY cycle for src/ — zero production-code changes (the eleventh PIN-ONLY cycle in the last twelve) + one e2e pin (343 → 344): the LOGIN SIGN-IN SUBMIT's OWN-HOVER LADDER at desktop 1280x800 on /login** "
        "(the never-pinned hover path of the pinned submit family: the v7 pin the REST chrome, the v9 pin the per-state geometry, the v25 pin the focus-visible ring, the v45 F4 pin the REST shadow-sm, the v135 survey the own-hover tint measured live — every submit census AT-REST or FOCUS; "
        "THE CONSTRUCT: the TINTED contract [the v129 active-hover form] — the bg transitioning rgb(15,23,42)→rgb(30,41,59) under the submit's own hover with the color/shadow family unchanged); "
        "the both-sides one-shot census submithover-arbit-v141.sh (the v140 searchhover form adapted to the submit axis: the STRUCTURAL finder [button[type=submit] with the 'Sign in' text — shared by both sites; the text cross-checked], the (5,5)-parked ladder, the live-read center [REF (640,677) / CLONE (640,677) — IDENTICAL coordinates], "
        "READ-ONLY — a mouse MOVE on a button dispatches no click and the logged-out surface holds no session; the submit NEVER clicked) measured the ladder **CLEAN, NO GAP** (the TINTED contract IDENTICAL both sides at every rung; the deltas the documented construct classes alone: the shadow LEAD-LAYER count [the v37 O1 note — the v3 three-slot vs the TW v4 five-slot construct, every lead a 0px-spread shadow invisible by construction; the VISIBLE pair byte-identical] + the borderColor zero-width computed-color artifact [the card.border class — border-width 0px both sides, nothing renders; the transition metadata IDENTICAL both sides: all / 0.2s]); "
        "the pin appended (append-pin-v141.py — the at-rest rung → the SUBMIT-HOVERED rung {hoverMatch true + bg rgb(30,41,59) — THE TINT + the UNCHANGED color/shadow family} → the restored rung; "
        "the STRUCTURAL finder; the submit never clicked; GREEN on the first run; the authoritative --list: 344 in 24 files); "
        "the pin-sanity mutation — the HOVER-TINT-REMOVAL form (hover:bg-[#1e293b] removed from the submit's className at login-card.tsx:357 — cascade-checked BY CONSTRUCTION: hover-scoped; the WIDER-FILE blast radius noted [the component serves EVERY auth mode's submit], "
        "the sole-failure criterion verified on the FULL LOGIN-PARITY SWEEP ALONE) sole-failure verified live [1 failed + 32 passed in the FULL login-parity sweep — the failure diff EXACTLY the predicted hovered-rung axis: the untinted bg rgb(15,23,42) received vs the pinned tinted rgb(30,41,59) expected, hoverMatch true preserved, the color/txt axes untouched]; "
        "restored (git diff src/ = 0 lines) + the FULL REBUILD + the post-restore regression 107 passed (login-parity 33 + calculator 20 + items 54 — the v140/v135/v129 pins' different-file immunity verified live). "
        "The ship chain **344 e2e zero flakes** (95+93+77+82 = 347 executions = 344 unique — the +1 landing in ch3 [login-parity]; both closed watches green through the chain); 35/35 smoke; "
        "**the screenshots 16/16 captured — ALL byte-identical (the same-day law: both this cycle and v140 captured Nov 1 UTC, every date-bearing surface rendering identically under the persisted seed)**; "
        "the dev evidence 4/4 byte-identical + VLM-verified (the menu proof {\"url\":\"/income\",\"docSW\":390,\"navLandmark\":true}; the dev-shots scripts derived v140→v141 with the version-swap-only verification)."
    )
    text = text.replace(anchor, anchor + v141 + "\n\n")
    io.open(AG, "w", encoding="utf-8").write(text)
    print("D1 AGENTS.md: the v141 paragraph appended")

# ---------- D2: CLAUDE.md ----------
CM = "CLAUDE.md"
text = io.open(CM, encoding="utf-8").read()
if one_hit(text, "- **E2E (Playwright, 343)**:", "CLAUDE e2e count"):
    text = text.replace("- **E2E (Playwright, 343)**:", "- **E2E (Playwright, 344)**:")
tail = "the post-restore regression 145/145 [items 54 + networth 40 + dashboard 52 — the v139/v138/v134 pins' different-file immunity verified live])"
if one_hit(text, tail, "CLAUDE v140-clause tail"):
    clause = (
        ", and the login sign-in submit's own-hover ladder at 1280 (v141 — the cycle's own login-pair surface: the never-pinned hover path of the pinned submit family "
        "[the v7 pin the REST chrome, the v9 pin the per-state geometry, the v25 pin the focus-visible ring, the v45 F4 pin the REST shadow-sm — every submit census AT-REST or FOCUS]; "
        "the submit carries hover:bg-[#1e293b] [login-card.tsx:357], so the own-hover end-state is the TINTED contract — bg rgb(15,23,42)→rgb(30,41,59) under the submit's own hover with the color/shadow family unchanged, "
        "measured byte-identical both sides by submithover-arbit-v141.sh — NO GAP, the PIN-ONLY form; the pin-sanity mutation the hover-tint REMOVAL on the submit className — "
        "hover-scoped by construction, the wider-file blast radius noted [the component serves every auth mode's submit], the sole failure verified on the FULL login-parity sweep: 1 failed + 32 passed, "
        "the failure diff the predicted hovered-rung bg axis [the untinted rgb(15,23,42) received vs the pinned tinted rgb(30,41,59) expected]; the post-restore regression 107/107 [login-parity 33 + calculator 20 + items 54 — the v140/v135/v129 pins' different-file immunity verified live])"
    )
    text = text.replace(tail, tail + clause)
    io.open(CM, "w", encoding="utf-8").write(text)
    print("D2 CLAUDE.md: 343 -> 344 + the v141 clause appended")

# ---------- D3: README.md ----------
RM = "README.md"
text = io.open(RM, encoding="utf-8").read()
n = text.count("(343 tests)")
if n == 2:
    text = text.replace("(343 tests)", "(344 tests)")
    print("D3 README.md: both test-count lines 343 -> 344")
else:
    print(f"ANCHOR MISS (README counts): {n} hits for '(343 tests)'")
    ok = False
row_anchor = "docs/remediation-plan-v140.md"
if one_hit(text, f"[`{row_anchor}`]", "README v140 row link"):
    idx = text.index(f"[`{row_anchor}`]")
    line_end = text.index("\n", idx)
    v141_row = (
        "\n| [`docs/remediation-plan-v141.md`](docs/remediation-plan-v141.md) | **The re-run cycle's second-pass next-oldest candidate (the v135-era LOGIN + CALCULATOR pair's THIRTEENTH re-run — the LOGIN view + the CALCULATOR dialog at desktop 1280x800, the SIXTY-FOURTH consecutive queue/ledger agreement; the login sign-in submit's own-hover ladder pin at 1280 — the never-pinned hover path of the pinned submit family, the TINTED contract measured byte-identical both sides; PIN-ONLY: src/ zero changes, 344 e2e)** |"
    )
    text = text[: line_end] + v141_row + text[line_end:]
    io.open(RM, "w", encoding="utf-8").write(text)
    print("D3 README.md: the v141 plan row inserted after the v140 row")

# ---------- D4: zero-balance_SKILL.md ----------
SK = "zero-balance_SKILL.md"
text = io.open(SK, encoding="utf-8").read()
if one_hit(text, "project_state: 108 unit tests / 343 e2e tests / 35 smoke steps — all green", "SKILL state line"):
    text = text.replace(
        "project_state: 108 unit tests / 343 e2e tests / 35 smoke steps — all green",
        "project_state: 108 unit tests / 344 e2e tests / 35 smoke steps — all green",
    )
row = "| 2026-11-01 | Session 175 — parity iteration v140 (`docs/remediation-plan-v140.md`)"
if one_hit(text, row, "SKILL Session 175 row head"):
    idx = text.index(row)
    line_end = text.index("\n", idx)
    v141_row = (
        "\n| 2026-11-01 | Session 176 — parity iteration v141 (`docs/remediation-plan-v141.md`) | **The re-run cycle's second-pass next-oldest candidate (the v135-era LOGIN + CALCULATOR pair's THIRTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141], the SIXTY-FOURTH consecutive queue/ledger agreement; the VLM verdict CALCULATOR DIFFERENT ×2 / LOGIN IDENTICAL ×2 — the pair's documented verdict-VARIATION family, the sole login FAB note disproven live [fabCount 0 + bodyHasBase44 false both sides]; the census 106 axes — 97 identical + 9 documented, ZERO new — the v135 values reproduced EXACTLY; the TWO-block md5 contract e1092d12d06677a4 + 9e5a52d2ab0f2ab9 held; PIN-ONLY for src/ + one e2e pin [344]: the LOGIN SIGN-IN SUBMIT's OWN-HOVER LADDER at 1280 — the never-pinned hover path of the pinned submit family, the TINTED contract measured byte-identical both sides [center (640,677) IDENTICAL]; the pin-sanity mutation sole-failure verified live [1 failed + 32 passed — the failure diff the predicted hovered-rung bg axis]; the post-restore regression 107/107; the ship chain 344 e2e zero flakes + 35/35 smoke; the screenshots 16/16 byte-identical [the same-day law]; the dev evidence 4/4 + VLM-verified; the 135th standing checks ALL GREEN — the mobile menu VERIFIED WORKING the 135th consecutive time)** |"
    )
    text = text[: line_end] + v141_row + text[line_end:]
    io.open(SK, "w", encoding="utf-8").write(text)
    print("D4 SKILL: state line 343 -> 344 + the Session 176 row inserted")

# ---------- D5: Project_Architecture_Document.md ----------
PAD = "Project_Architecture_Document.md"
text = io.open(PAD, encoding="utf-8").read()
if one_hit(text, "#### Revision Block — v1.1.97 (Tracked Changes)", "PAD v1.1.97 head"):
    block = (
        "#### Revision Block — v1.1.98 (Tracked Changes)\n"
        "- `[UI]` v1.1.98 (2026-11-01) — the v141 parity iteration (**PIN-ONLY for src/ — zero production-code changes, the eleventh PIN-ONLY cycle in the last twelve** + one e2e pin; no config change, no dependency change): the counts 108 unit / **344 e2e** (+1) / 35 smoke; **the re-run cycle's second-pass next-oldest candidate (the v135-era LOGIN + CALCULATOR pair's THIRTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141], the SIXTY-FOURTH consecutive queue/ledger agreement; the surface-family name 'the v129-era LOGIN + CALCULATOR pair' preserved — the lineage's own designation)**; the VLM verdict CALCULATOR DIFFERENT ×2 / LOGIN IDENTICAL ×2 (the pair's documented verdict-VARIATION family; the sole login FAB note DISPROVEN LIVE by base44-fab-arbit-v141.sh [fabCount 0 + bodyHasBase44 false both sides]; every calculator flag in the documented classes: the hover action buttons the POINTER-POSITION screenshot artifact [actionsAtRest identical both sides], the 'Will update category total' note the SEED-DATA class); the census 106 axes — 97 identical + 9 documented-class deltas, ZERO new (the v135 values reproduced EXACTLY); the TWO-block two-half md5 contract held (CALC_CENSUS_JS e1092d12d06677a4 + LOGIN_CENSUS_JS 9e5a52d2ab0f2ab9 — the v123/v129/v135 lineage digests carried byte-identical); **the pin — the LOGIN SIGN-IN SUBMIT's OWN-HOVER LADDER at 1280** (the never-pinned hover path of the pinned submit family; THE CONSTRUCT: the TINTED contract [the v129 active-hover form] — bg rgb(15,23,42)→rgb(30,41,59) under the submit's own hover with the color/shadow family unchanged; the both-sides census submithover-arbit-v141.sh measured the ladder CLEAN — NO GAP [the center REF (640,677) / CLONE (640,677), IDENTICAL coordinates]; the deltas the documented v37 O1 lead-layer construct + the borderColor zero-width artifact alone, the VISIBLE pair byte-identical, the transition metadata identical [all / 0.2s]); the pin-sanity mutation the HOVER-TINT-REMOVAL form (hover:bg-[#1e293b] removed from the submit's className at login-card.tsx:357 — the WIDER-FILE blast radius noted: the component serves every auth mode's submit; the sole-failure criterion verified on the FULL LOGIN-PARITY SWEEP ALONE) sole-failure verified live [1 failed + 32 passed — the failure diff the predicted hovered-rung bg axis: the untinted rgb(15,23,42) received vs the pinned tinted rgb(30,41,59) expected, hoverMatch true preserved]; the post-restore regression 107/107 (login-parity 33 + calculator 20 + items 54); the ship chain 344 e2e zero flakes (95+93+77+82 = 347 executions) + 35/35 smoke; the screenshots 16/16 byte-identical (the same-day law); the dev evidence 4/4 byte-identical + VLM-verified; the 135th standing checks ALL GREEN (the mobile menu VERIFIED WORKING the 135th consecutive time); the watches green (npm-audit 0 vulnerabilities — the thirty-second re-check; axe-core NO DRIFT 4.14.0); the workspace the SAME-PERSISTED class (the v140 environment held, the seedcheck EXACT before any gate).\n\n"
    )
    text = text.replace("#### Revision Block — v1.1.97 (Tracked Changes)", block + "#### Revision Block — v1.1.97 (Tracked Changes)", 1)
    io.open(PAD, "w", encoding="utf-8").write(text)
    print("D5 PAD: the v1.1.98 revision block inserted")

sys.exit(0 if ok else 1)
