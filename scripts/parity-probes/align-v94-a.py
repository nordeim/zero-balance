#!/usr/bin/env python3
"""align-v94-a.py — D1-D3 docs alignment for the v94 cycle:
D1 AGENTS.md (the v94 paragraph), D2 CLAUDE.md (296->297 + the v94 clause
at the E2E line's tail), D3 README.md (the counts + the v94 plan-table row
inserted before the v93 row). Idempotent."""

AGENTS_PARA = """

The v94 parity iteration (2026-10-19, PIN-ONLY for src/ — no production-code change; +1 e2e = 297; the plan `docs/remediation-plan-v94.md`, the narrative `docs/session_226.md`, the worklog Session 129 entry): the re-run cycle's next-oldest candidate — the v88-era NETWORTH + DRILL-DOWN pair (the NETWORTH view + the DASHBOARD's drill-down EXPANDED state at desktop 1280x800, full-pair, last re-shot v88, now the oldest remaining [v88 < v89 < v90 < v91 < v92 < v93]; the pair's FIFTH re-run [v60 → v67 → v76 → v82 → v88 → v94] — the SEVENTEENTH consecutive queue/ledger agreement, the surface names verified against vlm-shots-v88.sh's own header before the derivation) + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only sha prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds; the engine-contract pin 2 passed standalone) + the 88th standing checks (ALL GREEN — the mobile menu VERIFIED WORKING the 88th consecutive time; the reference's four bugs all live; the data census the 88th clean drift check; the SEO pair live both sides) + the networth section-header row census pin at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 297). The baseline chain FULLY GREEN as-shipped on the carried-over workspace (the session-log-only commit class: pulled to main @ 13e1445 — the docs-only session-log commit, ZERO src/ or lockfile deltas since the v93 push 1a2ecb5 — so the v93 cycle's own environment carries over unchanged, no re-provisioning; the seedcheck exact before any flow ran; lint → typecheck → 108 unit → npm run build → 296 e2e chunk executions [111+105+82 = 298 = 296 unique = the documented v93 state, zero flakes on the first run] → 35/35 smoke). The codebase audit clean (the v93 commit 1a2ecb5 re-verified PIN-ONLY as documented [23 files, +2568/−6, ZERO src/ changes]; the one commit since session-log-only; the production seams re-audited — auth, db-path, the SEO pair [robots.ts + sitemap.ts, both prerendered by the build], the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout). The v94 cycle's findings: the NETWORTH pair VERDICT DIFFERENT with every flag DOM-arbitrated to the v82/v88 re-runs' own documented classes (the avatar user-identity class; the "Edit with Base44" FAB the platform-chrome class RE-ARBITRATED LIVE [fabCount 0 + bodyHasBase44 false on BOTH sides]; the seed-data figures — the 1-asset vs 3-asset groups, the ∞:1 vs 0.21:1 ratio); the DRILL-DOWN pair VERDICT DIFFERENT with every flag DOM-arbitrated to the v82/v88 re-runs' own documented classes (the v56 SUPERSET nav-highlight class [the reference's link INERT rgb(63,63,70)/400 vs the clone's ACTIVE white/500]; the avatar; the pct × 568 DATA class [fillW ref 173 vs clone 357 on the byte-identical 568×12 track — the v82/v88 values REPRODUCED EXACTLY six re-runs later]; the v60 PERCEPTION donut-labels class [count 4, labelLineCount 0, 16px, black, 3 sectors — chrome byte-identical]; the v82 VLM-MISREAD stat-title class RE-ARBITRATED LIVE [both sides' titles "Total Income"/"Total Savings"/"Total Expenses" plural, byte-identical]; the v88 VLM-MISREAD divider class RE-ARBITRATED LIVE [the divider {DIV, h 1, bg rgb(229,231,227), flexGrow 1} byte-identical on every card; the count row h 20/w 254/flex/gap 8px byte-identical]; the seed-data classes). The both-sides census — executed in the TWO-HALF controlled form, BUILT TWO-HALF FROM THE START (ref-arbit-v94.sh + clone-arbit-v94.sh via build-twohalf-v94.py, the TWO census JS blocks [ARBIT_A 90 lines + ARBIT_B 111 lines] extracted once and embedded byte-identically across the halves — the md5 line-block contract [a9cdcc96 / baa22974]) — REPRODUCES the v88 census values EXACTLY: zero drift on every axis (the drill-down census: navHighlight/avatarLetter/progress/donutLabels/statTrendIcons/heroTrendGlyphs; the networth summary-card census: the card 960×333/32px/16px/the gradient/the shadow, the headRow 76/32, the label/figure/medallion/statGrid/statTile/ratioFooter families — the labelBlock's width the v82 DATA-CONDITIONAL class [304 vs 357]). NO NEW CLONE GAP — the v94 iteration PIN-ONLY. The +1 e2e pin: the networth SECTION-HEADER row census at 1280 (tests/e2e/networth.spec.ts — the tab panel's "Assets" header row, never pinned at ANY viewport: the row's flex chrome {flex/center/space-between/h 56/w 960} + the h2 "Assets" typography {24px/700/lh 32px/rgb(26,58,46)/mb 0/h 32} + the count subtitle P {16px/400/lh 24px/rgb(107,114,128)} + the left block's h 56 + the Add Asset button's chrome on this row {36×134/8px 16px/6px/14px/500/white/the forest→lime gradient} + the 16px Plus + the row→group rhythm delta 24 + the first type-group header's re-affirm {18px/600/lh 28px/mb 12} + the docSW 1280 guard; the block's width + the countText EXCLUDED [the data-coupled width class — the v82 labelBlock convention], the group wrapper's margin-TOP form EXCLUDED [the v3/v4 space-y margin-attribution computed class — the rendered delta 24 the parity contract]; the pin's own axes first measured byte-identical on both sides by the supplemental two-half census [nwsection-arbit-v94.sh + nwsection-clone-v94.sh — BUILT two-half from the start, the census JS byte-identical by the md5 line-block diff f8b3cabf; both sides read-only, the seedcheck exact after the run]). The pin-sanity mutation (the executed form — the viewport-scoped text-2xl font-bold → text-2xl font-bold lg:font-black at net-worth-view.tsx:418, by LINE NUMBER; AT-lg because the pin runs at 1280; the line-scoping keeps the file's OTHER text-2xl font-bold instances [107/212/348/371/378/482] untouched): the failure diff reads as the h2.fw axis ALONE ("700" → "900" at ≥1024px); the full networth.spec.ts under the mutation reads ONLY the v94 pin red (29 green) — cascade-free BY CONSTRUCTION (the h2's lh 32px bound by text-2xl's line-height — a font-weight flip does not scale it; the block's h 56, the row, the countP, the addBtn, the rhythm, and the docSW all unchanged; no spec asserts the "Assets" section h2's computed styles at ANY viewport — the getByRole heading + the a11y TAB-role references text-matching, green under a weight flip; lg:font-black appears NOWHERE in src/) — then restored (git diff src/ = 0 lines; the standalone REBUILD via the FULL npm run build; the post-restore full run 30/30 green). The F5 full chain re-run GREEN: lint → typecheck → 108 unit → build → 297 e2e (111+106+82 = 299 chunk executions = 297 unique tests, zero flakes) → 35/35 smoke; the screenshots 16/16 BYTE-IDENTICAL (the same-day-seed byte-identity law — the seed planted and the shots taken on the same calendar day 2026-10-19, byte-for-byte reproduction, ZERO arbitration needed — the second consecutive pure-form cycle); the final seedcheck exact. The operational lessons (the probe README's D6 section): the reaping budget as a standing step applied clean (the pre-run + between-halves reaps on every probe — zero resource-exhaustion symptoms this cycle), the second-pass session-name sed (the arbit lineage's refar88/clonear88 session names ride the "ar" token family, NOT the "v88" family — the explicit second sed pass caught them before any execution), and the misread-class live re-arbitration (a re-flagged documented MISREAD class is re-arbitrated by RE-RUNNING the existing one-shot census live, not re-derived). The docs alignment: D1 AGENTS.md (the v94 paragraph), D2 CLAUDE.md (296 → 297 + the v94 clause at the E2E line's tail), D3 README.md (the counts + the v94 plan-table row), D4 zero-balance_SKILL.md (Session 129 audit row + the state line), D5 the PAD's v1.1.51 revision block, D6 the probe README's v94 section (+ the v95 queue — the v89-era DASHBOARD pair [v61 → v68 → v77 → v83 → v89 → v95], verified against vlm-shots-v89.sh's own header), D7 session_226.md + the worklog Session 129 entry; docs/remediation-plan-v94.md saved (the validated plan — the pre-execution validation section recording the measured values, the mutation target line verified by reading the source, the coverage-map grep, the disproven-in-advance candidates)."""

CLAUDE_TAIL_OLD = "the failure diff reads as the label's fw axis alone)"
CLAUDE_TAIL_NEW = ("the failure diff reads as the label's fw axis alone); the v94 networth section-header row census pin "
"(the tab panel's \"Assets\" header row at 1280 — the row's flex chrome + the h2 typography + the count P + the Add Asset "
"chrome + the row-to-group rhythm, never pinned at ANY viewport; the mutation text-2xl font-bold -> text-2xl font-bold "
"lg:font-black at net-worth-view.tsx:418 only the v94 pin red — the h2's fw axis alone, cascade-free)")

README_ROW = ("| [`docs/remediation-plan-v94.md`](docs/remediation-plan-v94.md) | **The re-run cycle's next-oldest candidate "
"(the v88-era networth + drill-down pair's fifth re-run [v60 → v67 → v76 → v82 → v88 → v94] — the NETWORTH view + the "
"DASHBOARD's drill-down EXPANDED state at desktop 1280x800, last re-shot v88; the seventeenth consecutive queue/ledger "
"agreement, the surface names verified against the v88 probe scripts) + the axe watch (NO DRIFT) + the networth "
"section-header row census pin at 1280 (PIN-ONLY — no production-code change; +1 e2e = 297)**: both verdicts DIFFERENT "
"with every flag DOM-arbitrated to the v82/v88 re-runs' own documented classes (the avatar user-identity class; the FAB "
"the platform-chrome class re-arbitrated live [fabCount 0 + bodyHasBase44 false on both sides]; the v56 SUPERSET "
"nav-highlight; the pct × 568 data class [fillW 173-vs-357 on the byte-identical 568×12 track]; the v60 perception "
"donut-labels class; the v82 stat-title misread re-arbitrated live [both sides plural, byte-identical]; the v88 divider "
"misread re-arbitrated live [the divider byte-identical on every card]; the seed-data classes); the census — executed in "
"the two-half controlled form BUILT two-half from the start — reproducing the v88 values exactly (zero drift on every "
"axis; the labelBlock width the v82 data-conditional class); the +1 pin the SECTION-HEADER row family {the row's flex "
"chrome {flex/center/space-between/56/960} + the h2 \"Assets\" typography {24px/700/lh 32px/rgb(26,58,46)} + the count "
"subtitle P {16px/400/lh 24px/rgb(107,114,128)} + the block h 56 + the Add Asset chrome {36×134/8px 16px/6px/14px/500/"
"white/gradient} + the 16px Plus + the row→group delta 24 + the groupH3 re-affirm} — never pinned at ANY viewport, the "
"pin's own axes first measured byte-identical on both sides by the supplemental two-half census (both sides read-only); "
"the pin-sanity mutation text-2xl font-bold → text-2xl font-bold lg:font-black at net-worth-view.tsx:418 (only the v94 "
"pin red, the failure diff reads as the h2's fw axis alone — cascade-free); the screenshots 16/16 byte-identical (the "
"same-day-seed law — the second consecutive pure-form cycle, zero arbitration needed); the lessons: the reaping budget "
"as a standing step applied clean + the second-pass session-name sed + the misread-class live re-arbitration |\n")

def main():
    # D1 — AGENTS.md: append the v94 paragraph (idempotent).
    t = open("AGENTS.md").read()
    if "The v94 parity iteration" not in t:
        if not t.endswith("\n"):
            t += "\n"
        t += AGENTS_PARA + "\n"
        open("AGENTS.md", "w").write(t)
        print("D1 AGENTS.md: v94 paragraph appended")
    else:
        print("D1 AGENTS.md: already present")

    # D2 — CLAUDE.md: 296 -> 297 + the v94 clause at the E2E line's tail.
    t = open("CLAUDE.md").read()
    changed = 0
    if "**E2E (Playwright, 296)**" in t:
        t = t.replace("**E2E (Playwright, 296)**", "**E2E (Playwright, 297)**", 1)
        changed += 1
    if CLAUDE_TAIL_OLD in t and "lg:font-black at net-worth-view.tsx:418" not in t:
        t = t.replace(CLAUDE_TAIL_OLD, CLAUDE_TAIL_NEW, 1)
        changed += 1
    open("CLAUDE.md", "w").write(t)
    print(f"D2 CLAUDE.md: {changed} edits applied")

    # D3 — README.md: the counts (two places) + the v94 row before the v93 row.
    t = open("README.md").read()
    changed = 0
    if "Playwright specs (296 tests)" in t:
        t = t.replace("Playwright specs (296 tests)", "Playwright specs (297 tests)", 1)
        changed += 1
    if "Playwright e2e (296 tests)" in t:
        t = t.replace("Playwright e2e (296 tests)", "Playwright e2e (297 tests)", 1)
        changed += 1
    anchor = "| [`docs/remediation-plan-v93.md`](docs/remediation-plan-v93.md)"
    if anchor in t and "remediation-plan-v94.md" not in t:
        t = t.replace(anchor, README_ROW + anchor, 1)
        changed += 1
    open("README.md", "w").write(t)
    print(f"D3 README.md: {changed} edits applied")

if __name__ == "__main__":
    main()
