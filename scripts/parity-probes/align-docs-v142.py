#!/usr/bin/env python3
"""align-docs-v142.py — D1-D5 of the v142 docs alignment (the D0 anchor
discipline: every insert/replace anchor verified 1-hit BEFORE any write;
the script refuses and exits non-zero on any anchor miss or multi-hit).
  D1 AGENTS.md — the v142 paragraph appended after the v141 paragraph
  D2 CLAUDE.md — the e2e count 344 -> 345 + the v142 clause appended to
     the e2e enumeration line's end (after the v141 clause)
  D3 README.md — the two test-count lines 344 -> 345 + the v142 plan row
     inserted after the v141 row
  D4 zero-balance_SKILL.md — the project_state line 344 -> 345 + the
     Session 177 row inserted after the Session 176 row
  D5 Project_Architecture_Document.md — the v1.1.99 revision block
     inserted before the v1.1.98 block
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
anchor = "the dev-shots scripts derived v140→v141 with the version-swap-only verification).\n\n"
if one_hit(text, anchor, "AGENTS v141-paragraph tail"):
    v142 = (
        "Reference surfaces pinned by the v142 iteration (`docs/remediation-plan-v142.md`) — "
        "**the re-run cycle's second-pass next-oldest candidate (the v136-era NETWORTH + drill-down-DASHBOARD pair — the NETWORTH view + the DASHBOARD's drill-down EXPANDED state at desktop 1280x800, the pair's THIRTEENTH re-run "
        "[v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142], the SIXTY-FIFTH consecutive queue/ledger agreement "
        "— the corrected entries-minus-one convention applied cleanly: the TWELFTH ordinal recorded in the v136 plan's own header on its 13-entry bracket [v60 the original, one entry] → v142 = the THIRTEENTH; "
        "the v60-era networth+drill-down pair's surface family name preserved) "
        "+ the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, the v68 dedupe holds — one node_modules/axe-core entry verified live) "
        "+ the npm-audit watch at its thirty-third re-check (0 VULNERABILITIES --omit=dev — the v110 bump holds: next 16.4.3 + zod 4.6.7; the 16 moderate the accepted dev-only ESLint braces chain) "
        "+ the 136th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, "
        "the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; "
        "the clone's mobile menu VERIFIED WORKING the 136th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). "
        "**The baseline GREEN ON THE FIRST CHAIN** (the SAME-PERSISTED workspace — the v141 environment held through the session boundary: node_modules 354 entries intact, BOTH chromium pairs [1200 + 1243], "
        "the .env [DATABASE_URL=\"file:../db/custom.db\"] + db/ at the repo root intact with the v141-cycle seed, the repo pulled to main @ eb1fc47 [the session-log commit, +1 file docs/session_353.md]; the seedcheck EXACT 7/1850/2235/0/3/2 before any gate; "
        "the sandbox DATABASE_URL pollution live as documented]: lint, typecheck, 108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e [347 executions = 344 unique, ZERO flakes], 35/35 smoke, "
        "the production-seam audit clean; skills/ excluded). "
        "The probe series derived from the v136 lineage (derive-v142-series.py — the generic swaps incl. the FOUR explicit session-token families [refvlm/clonevlm + refar/clonear arbit — the tokens carry '136' without the 'v' prefix] "
        "+ the history-correction fragments [the era marker last-re-shot v130→v136 + the oldest-remaining list v130..v132→v136..v138 + the ordinal TWELFTH→THIRTEENTH + the bracket extended in all four files "
        "+ the agreement ordinal FIFTY-NINTH→SIXTY-FIFTH + the arbit census provenance \"the v130 census axes\"→\"the v136 census axes\"], all applied on the FIRST run, zero residual, line counts preserved 84/71/65/328 == the v136 lineage exactly) "
        "+ the two-half builder (derive-build-twohalf-v142.py — the generic swap + the lesson-range bump v92..v135→v92..v141 [the BARE range token] + the lineage-note fixup \"the v130-lineage derivation\"→\"the v136-lineage derivation\" LAST) "
        "+ the comparator (derive-compare-v142.py — the generic swap incl. the EXPLICIT /tmp/vlm136→/tmp/vlm142 log-path swap [the path token carries no 'v136' substring] + the provenance citations re-pointed at the v136 measurement "
        "[the lineage ordinal TWELFTH→THIRTEENTH; the records chain v124/v130→v130/v136]) "
        "+ the verify script (derive-verify-twohalf-v142.py — the lineage-citation chain extended v124/v125/v126/v127/v128/v129→+v130/v136) "
        "+ the 136th standing pair derived (derive-standing-v142.py — from the v135 pair, three token families [the ordinal 135th→136th th→th plain replace, the bare session names ref135/clone135→ref136/clone136, the version v135→v136; "
        "the citation extended with v141's 134th→135th], normalize-back diff clean, zero old tokens, line counts preserved 119/74 — the derivation's own first-run pairing miss [the 134th sources] caught and fixed BEFORE any execution). "
        "The halves built + the TWO-block md5 contract verified by the direct THREE-WAY python extraction (verify-twohalf-v142.py — ARBIT_A 90 lines md5 17d18f15c9145155afd28f7f1ca6efde + ARBIT_B 111 lines md5 9d4b50ad1f8c22dfe207ea9aa61470be, "
        "byte-identical across arbit-v142.sh + ref-arbit-v142.sh + clone-arbit-v142.sh — **the within-cycle contract form: the view-label tokens carry the version ['drill-arbit-1280-v142' / 'nw-height-1280-v142'], so the digests differ from the v136 cycle's by construction**). "
        "**The VLM verdict — NETWORTH IDENTICAL ×2 / DRILL-DOWN DIFFERENT ×2, the stable-identical-networth form (the v105/v121/v136 precedent class: the identical side's outcome holds while its data differences stay folded in the expected-and-reported data classes)** "
        "(the FAB claims — claimed in BOTH directions across the two passes, both flagged surfaces [the dashboard / + the networth /networth] — **DISPROVEN LIVE by base44-fab-arbit-v142.sh**: fabCount 0 + bodyHasBase44 false on BOTH sides, BOTH surfaces, 1280, logged-in — "
        "the standing v97/v103/v108/v109/v115/v120/v123/v127/v129/v135/v141 disproof form re-confirmed; the pass-1 avatar 'P' claim the LETTER-MISREAD class [the census's own avatarLetter axis measured 'D' directly — the v136 \"Total Expense[s]\" misread precedent's own family]; "
        "every drill-down flag in both passes in the documented classes: the nav-highlight the v56 SUPERSET class, the progress fill the PCT data class, the donut labels the v60 PERCEPTION class [the census donutLabels count/labelFs/labelFill byte-identical], "
        "the extra Freelance category + the \"1 category\"/\"2 categories\" footer the SEED-DATA classes, the \"Total Expense vs Total Expenses\" title claim a pass-1 MISREAD [both sides' third card title measured \"Total Expenses\" in the v136 statfooter census]). "
        "The both-sides census **73 axes — 67 identical + 6 documented-class deltas, ZERO new — REPRODUCING the v136 census values EXACTLY** (the same 73/67/6 split, zero drift on every axis: navHighlight.color + navHighlight.fw [the v56 superset delta] "
        "+ avatarLetter [the user-identity data class] + progress.fillW [the pct data class] + donutLabels.texts [the each-site's-data class] + labelBlock.w [the v82 DATA-CONDITIONAL width class: \"$25,000.00\" 304px vs \"-$245,950.00\" 357px]). "
        "**A PIN-ONLY cycle for src/ — zero production-code changes (the twelfth PIN-ONLY cycle in the last thirteen) + one e2e pin (344 → 345): the DASHBOARD DRILL-DOWN ROWS' OWN-HOVER LADDERS at desktop 1280x800 on /dashboard** "
        "(the never-pinned hover paths of the pinned drill-down family: the v43 F2 pin holds the SECTION row's hovered bg axis alone [the arbitrary-hex repair's own regression axis]; the v43/v44/v50/v53 censuses hold the rows' AT-REST chrome "
        "[the category row's inline bg pinned at four states]; the v44 F1 pin the expansion animation; the v31 pin the drill-down keyboard path; the v60 F2 pin the sub/item STRUCTURE — "
        "**the CATEGORY row's own-hover INERT contract held by NO spec at ANY viewport** [the suite-wide survey: breakdown.spec.ts carries zero hover coverage; dashboard.spec.ts's hover pins cover only the stat cards + the quick actions], "
        "and the ladder FORM itself never pinned on either row); THE CONSTRUCT — the two-contract form, the reference's own asymmetry: the SECTION row's **TINTED contract** [hover:bg-[#f9fafb] with NO inline bg, dashboard-view.tsx:309 — the v43 F2 arbitrary-hex repair — "
        "the bg transitioning rgba(0,0,0,0)→rgb(249,250,251) under the row's own hover with the color/radius/geometry family unchanged] + the CATEGORY row's **INERT-HOVER contract** [hover:bg-gray-100 BUT ALSO an inline backgroundColor rgb(249,250,251), dashboard-view.tsx:365 — "
        "the inline beats the utility, the v29 class — the at-rest inline bg persisting unchanged under the row's own hover]; the both-sides one-shot census drillhover-arbit-v142.sh (the v141 submithover form adapted to the drill-down rows' axis pair: "
        "the STRUCTURAL finders [the breakdown card by its \"Net Zero Breakdown\" title leaf → its closest rounded-2xl ancestor — the form shared by both sites; the section row = the card's button whose text carries \"Total Income\"; "
        "the category row = the card's first button whose trimmed text starts with \"Salary\" — both sites' first Income category, the seed names cross-checked], the ONE-TIME view-state expansion click on the section row [allowed under the v46 incident rule — "
        "the drill-down rows mutate no data; the rows NEVER clicked past the one expansion — the accordion toggles on click, out of bounds], the (5,5)-parked ladder, the live-read centers [the section (1088,225) + the category (1116,275) — IDENTICAL coordinates both sides], "
        "READ-ONLY — a mouse MOVE on a button dispatches no click) measured BOTH ladders **CLEAN, NO GAP** (both contracts IDENTICAL both sides at every rung: the at-rest rung, the section-hovered rung, the category-hovered rung, the restored rung; "
        "the deltas the documented construct classes alone: the transitionProperty metadata [REF the v3 six-prop list vs CLONE the v4 gradient-var compile — **the v95 family, never pinned**; the transitionDuration 0.15s IDENTICAL both sides] + the category row's txt [the SEED-DATA class]); "
        "the pin appended (append-pin-v142.py — the at-rest rung → the SECTION-HOVERED rung {hoverMatch true + bg rgb(249,250,251) — THE TINTED CONTRACT + the UNCHANGED color/geometry family} → the CATEGORY-HOVERED rung {hoverMatch true + bg rgb(249,250,251) UNCHANGED — THE INERT CONTRACT} → the restored rung; "
        "the V94-COLLISION-safe axis set [the transition metadata deliberately NOT pinned — the v95 family's own form]; the shared section-hovered-bg axis with the v43 F2 pin noted [a section-tint removal fails both — CORRECT drift behavior, both pins guarding the same repair]; "
        "GREEN on the first run; the authoritative --list: 345 in 24 files); "
        "the pin-sanity mutation — the INLINE→CLASS SWAP form (the category row's inline backgroundColor replaced with the bg-[#f9fafb] class at dashboard-view.tsx:364-365 — **the exact Tailwind-v4-refactor drift class the pin exists to guard**: the at-rest computed bg stays IDENTICAL [bg-[#f9fafb] computes the same rgb(249,250,251), so the v43/v44/v50/v53 at-rest censuses stay GREEN] "
        "but the hover utility hover:bg-gray-100 now WINS under hover [the :hover pseudo-class outweighs the plain utility] — the hovered bg computes the v4 named palette's lab() value [the v43 F2 record's own trap], the INERT contract BROKEN; the WIDER-FILE blast radius noted [the component serves every breakdown section's category rows], "
        "the sole-failure criterion verified on the FULL DASHBOARD SWEEP ALONE) sole-failure verified live [1 failed + 52 passed — the failure diff EXACTLY the predicted category-hovered-rung bg axis: the lab() value lab(96.1596 -0.0823438 -1.13575) [the v4 gray-100] received vs the pinned inert rgb(249,250,251) expected, hoverMatch true preserved; "
        "the v43 F2 section-row pin GREEN — the section row untouched by the mutation]; restored (git diff src/ = 0 lines) + the FULL REBUILD + the post-restore regression 93 passed (dashboard 53 + networth 40 — the v137/v131/v125 dashboard pins + the v136 networth pin's different-file immunity verified live). "
        "The ship chain **345 e2e zero flakes** (95+94+77+82 = 348 executions = 345 unique — the +1 landing in ch2 [dashboard]; both closed watches green through the chain); 35/35 smoke; "
        "**the screenshots 16/16 captured — ALL byte-identical (the same-day law: both this cycle and v141 captured Nov 1 UTC, every date-bearing surface rendering identically under the persisted seed)**; "
        "the dev evidence 4/4 byte-identical + VLM-verified (the menu proof {\"url\":\"/income\",\"docSW\":390,\"navLandmark\":true}; the dev-shots scripts derived v141→v142 with the version-swap-only verification on both)."
    )
    text = text.replace(anchor, anchor + v142 + "\n\n")
    io.open(AG, "w", encoding="utf-8").write(text)
    print("D1 AGENTS.md: the v142 paragraph appended")

# ---------- D2: CLAUDE.md ----------
CM = "CLAUDE.md"
text = io.open(CM, encoding="utf-8").read()
if one_hit(text, "- **E2E (Playwright, 344)**:", "CLAUDE e2e count"):
    text = text.replace("- **E2E (Playwright, 344)**:", "- **E2E (Playwright, 345)**:")
tail = "the post-restore regression 107/107 [login-parity 33 + calculator 20 + items 54 — the v140/v135/v129 pins' different-file immunity verified live])"
if one_hit(text, tail, "CLAUDE v141-clause tail"):
    clause = (
        ", and the dashboard drill-down rows' own-hover ladders at 1280 (v142 — the cycle's own drill-down-pair surface: the never-pinned hover paths of the pinned drill-down family "
        "[the v43 F2 pin the SECTION row's hovered bg axis alone; the v43/v44/v50/v53 censuses the rows' AT-REST chrome; the v44 F1 pin the expansion animation; the v31 pin the keyboard path; the v60 F2 pin the sub/item STRUCTURE — "
        "the CATEGORY row's own-hover INERT contract + the ladder form held by NO spec at ANY viewport]; the two-contract form, the reference's own asymmetry — the section row's TINTED contract "
        "[bg rgba(0,0,0,0)→rgb(249,250,251) under hover, hover:bg-[#f9fafb] at dashboard-view.tsx:309] + the category row's INERT-HOVER contract [the inline backgroundColor rgb(249,250,251) persisting unchanged under hover — the inline beats the hover:bg-gray-100 utility, the v29 class, dashboard-view.tsx:365], "
        "measured byte-identical both sides at every rung by drillhover-arbit-v142.sh — NO GAP, the PIN-ONLY form [the one-time view-state expansion click allowed under the v46 rule; the rows never clicked past it]; "
        "the pin-sanity mutation the INLINE→CLASS SWAP on the category row's backgroundColor at dashboard-view.tsx:364-365 — the exact TW-v4-refactor drift class [at-rest identical, the hover utility live under hover — the hovered bg computes the v4 lab() value], "
        "the sole failure verified on the FULL dashboard sweep: 1 failed + 52 passed, the failure diff the predicted category-hovered-rung bg axis [the lab() value lab(96.1596 -0.0823438 -1.13575) received vs the pinned inert rgb(249,250,251) expected, hoverMatch true preserved]; "
        "the post-restore regression 93/93 [dashboard 53 + networth 40 — the v137/v131/v125/v136 pins' different-file immunity verified live])"
    )
    text = text.replace(tail, tail + clause)
    io.open(CM, "w", encoding="utf-8").write(text)
    print("D2 CLAUDE.md: 344 -> 345 + the v142 clause appended")

# ---------- D3: README.md ----------
RM = "README.md"
text = io.open(RM, encoding="utf-8").read()
n = text.count("(344 tests)")
if n == 2:
    text = text.replace("(344 tests)", "(345 tests)")
    print("D3 README.md: both test-count lines 344 -> 345")
else:
    print(f"ANCHOR MISS (README counts): {n} hits for '(344 tests)'")
    ok = False
row_anchor = "docs/remediation-plan-v141.md"
if one_hit(text, f"[`{row_anchor}`]", "README v141 row link"):
    idx = text.index(f"[`{row_anchor}`]")
    line_end = text.index("\n", idx)
    v142_row = (
        "\n| [`docs/remediation-plan-v142.md`](docs/remediation-plan-v142.md) | **The re-run cycle's second-pass next-oldest candidate (the v136-era NETWORTH + drill-down-DASHBOARD pair's THIRTEENTH re-run — the NETWORTH view + the DASHBOARD's drill-down EXPANDED state at desktop 1280x800, the SIXTY-FIFTH consecutive queue/ledger agreement; the dashboard drill-down rows' own-hover ladder pins at 1280 — the never-pinned hover paths of the pinned drill-down family, the two-contract form [the section row's TINTED + the category row's INERT] measured byte-identical both sides; PIN-ONLY: src/ zero changes, 345 e2e)** |"
    )
    text = text[: line_end] + v142_row + text[line_end:]
    io.open(RM, "w", encoding="utf-8").write(text)
    print("D3 README.md: the v142 plan row inserted after the v141 row")

# ---------- D4: zero-balance_SKILL.md ----------
SK = "zero-balance_SKILL.md"
text = io.open(SK, encoding="utf-8").read()
if one_hit(text, "project_state: 108 unit tests / 344 e2e tests / 35 smoke steps — all green", "SKILL state line"):
    text = text.replace(
        "project_state: 108 unit tests / 344 e2e tests / 35 smoke steps — all green",
        "project_state: 108 unit tests / 345 e2e tests / 35 smoke steps — all green",
    )
row = "| 2026-11-01 | Session 176 — parity iteration v141 (`docs/remediation-plan-v141.md`)"
if one_hit(text, row, "SKILL Session 176 row head"):
    idx = text.index(row)
    line_end = text.index("\n", idx)
    v142_row = (
        "\n| 2026-11-01 | Session 177 — parity iteration v142 (`docs/remediation-plan-v142.md`) | **The re-run cycle's second-pass next-oldest candidate (the v136-era NETWORTH + drill-down-DASHBOARD pair's THIRTEENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142], the SIXTY-FIFTH consecutive queue/ledger agreement; the VLM verdict NETWORTH IDENTICAL ×2 / DRILL-DOWN DIFFERENT ×2 — the stable-identical-networth form, the FAB claims [both directions, both surfaces] disproven live [fabCount 0 + bodyHasBase44 false both sides]; the census 73 axes — 67 identical + 6 documented, ZERO new — the v136 values reproduced EXACTLY; the TWO-block md5 contract 17d18f15 + 9d4b50ad held [the within-cycle form]; PIN-ONLY for src/ + one e2e pin [345]: the DASHBOARD DRILL-DOWN ROWS' OWN-HOVER LADDERS at 1280 — the never-pinned hover paths of the pinned drill-down family, the two-contract form [the section row's TINTED + the category row's INERT] measured byte-identical both sides [centers (1088,225) + (1116,275) IDENTICAL]; the pin-sanity mutation [the INLINE→CLASS SWAP — the exact TW-v4-refactor drift class] sole-failure verified live [1 failed + 52 passed — the failure diff the predicted category-hovered-rung bg axis, the v4 lab() value received]; the post-restore regression 93/93; the ship chain 345 e2e zero flakes + 35/35 smoke; the screenshots 16/16 byte-identical [the same-day law]; the dev evidence 4/4 + VLM-verified; the 136th standing checks ALL GREEN — the mobile menu VERIFIED WORKING the 136th consecutive time)** |"
    )
    text = text[: line_end] + v142_row + text[line_end:]
    io.open(SK, "w", encoding="utf-8").write(text)
    print("D4 SKILL: state line 344 -> 345 + the Session 177 row inserted")

# ---------- D5: Project_Architecture_Document.md ----------
PAD = "Project_Architecture_Document.md"
text = io.open(PAD, encoding="utf-8").read()
if one_hit(text, "#### Revision Block — v1.1.98 (Tracked Changes)", "PAD v1.1.98 head"):
    block = (
        "#### Revision Block — v1.1.99 (Tracked Changes)\n"
        "- `[UI]` v1.1.99 (2026-11-01) — the v142 parity iteration (**PIN-ONLY for src/ — zero production-code changes, the twelfth PIN-ONLY cycle in the last thirteen** + one e2e pin; no config change, no dependency change): the counts 108 unit / **345 e2e** (+1) / 35 smoke; **the re-run cycle's second-pass next-oldest candidate (the v136-era NETWORTH + drill-down-DASHBOARD pair's THIRTEENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142], the SIXTY-FIFTH consecutive queue/ledger agreement; the v60-era networth+drill-down pair's surface family name preserved)**; the VLM verdict NETWORTH IDENTICAL ×2 / DRILL-DOWN DIFFERENT ×2 (the stable-identical-networth form — the v105/v121/v136 precedent class; the FAB claims — both directions across the passes, both flagged surfaces — DISPROVEN LIVE by base44-fab-arbit-v142.sh [fabCount 0 + bodyHasBase44 false both sides]; every drill-down flag in the documented classes: the nav-highlight the v56 SUPERSET class, the avatar letter the user-identity class [the pass-1 'P' claim a LETTER-MISREAD — the census measured 'D' directly], the progress fill the PCT data class, the donut labels the v60 PERCEPTION class, the extra Freelance category + the footer count the SEED-DATA classes); the census 73 axes — 67 identical + 6 documented-class deltas, ZERO new (the v136 values reproduced EXACTLY: navHighlight.color/.fw + avatarLetter + progress.fillW + donutLabels.texts + labelBlock.w [the v82 DATA-CONDITIONAL width class]); the TWO-block two-half md5 contract held (ARBIT_A 90 lines 17d18f15c9145155afd28f7f1ca6efde + ARBIT_B 111 lines 9d4b50ad1f8c22dfe207ea9aa61470be — the within-cycle contract form, the view-label tokens carrying the version); **the pin — the DASHBOARD DRILL-DOWN ROWS' OWN-HOVER LADDERS at 1280** (the never-pinned hover paths of the pinned drill-down family; THE CONSTRUCT — the two-contract form, the reference's own asymmetry: the section row's TINTED contract [bg rgba(0,0,0,0)→rgb(249,250,251) under hover] + the category row's INERT-HOVER contract [the inline bg rgb(249,250,251) persisting unchanged under hover]; the both-sides census drillhover-arbit-v142.sh measured BOTH ladders CLEAN — NO GAP [the centers (1088,225) + (1116,275), IDENTICAL coordinates both sides]; the deltas the documented v95 transitionProperty construct + the seed-data texts alone, the transitionDuration 0.15s IDENTICAL); the pin-sanity mutation the INLINE→CLASS SWAP form (the category row's inline backgroundColor replaced with the bg-[#f9fafb] class at dashboard-view.tsx:364-365 — the exact Tailwind-v4-refactor drift class: the at-rest computed bg IDENTICAL [the at-rest censuses stay green] but the hover utility now live under hover [the hovered bg computes the v4 lab() value, the INERT contract broken]; the WIDER-FILE blast radius noted: the component serves every breakdown section's category rows; the sole-failure criterion verified on the FULL DASHBOARD SWEEP ALONE) sole-failure verified live [1 failed + 52 passed — the failure diff the predicted category-hovered-rung bg axis: the lab() value lab(96.1596 -0.0823438 -1.13575) received vs the pinned inert rgb(249,250,251) expected, hoverMatch true preserved]; the post-restore regression 93/93 (dashboard 53 + networth 40); the ship chain 345 e2e zero flakes (95+94+77+82 = 348 executions) + 35/35 smoke; the screenshots 16/16 byte-identical (the same-day law); the dev evidence 4/4 byte-identical + VLM-verified; the 136th standing checks ALL GREEN (the mobile menu VERIFIED WORKING the 136th consecutive time); the watches green (npm-audit 0 vulnerabilities — the thirty-third re-check; axe-core NO DRIFT 4.14.0); the workspace the SAME-PERSISTED class (the v141 environment held, the seedcheck EXACT before any gate).\n\n"
    )
    text = text.replace("#### Revision Block — v1.1.98 (Tracked Changes)", block + "#### Revision Block — v1.1.98 (Tracked Changes)", 1)
    io.open(PAD, "w", encoding="utf-8").write(text)
    print("D5 PAD: the v1.1.99 revision block inserted")

sys.exit(0 if ok else 1)
