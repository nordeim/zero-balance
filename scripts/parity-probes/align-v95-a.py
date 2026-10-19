#!/usr/bin/env python3
"""align-v95-a.py — D1-D3 docs alignment for the v95 cycle:
D1 AGENTS.md (the v95 paragraph), D2 CLAUDE.md (297->298 + the v95 clause
at the E2E line's tail), D3 README.md (the counts + the v95 plan-table row
inserted before the v94 row). Idempotent."""

AGENTS_PARA = """

The v95 parity iteration (2026-10-19/20, PIN-ONLY for src/ — no production-code change; +1 e2e = 298; the plan `docs/remediation-plan-v95.md`, the narrative `docs/session_228.md`, the worklog Session 130 entry): the re-run cycle's next-oldest candidate — the v89-era DASHBOARD pair (the BUDGET GUIDELINES card + the QUICK-ACTION card row, both below-the-fold surfaces of the dashboard FULL-PAGE at desktop 1280x800, last re-shot v89, now the oldest remaining [v89 < v90 < v91 < v92 < v93 < v94]; the pair's FIFTH re-run [v61 → v68 → v77 → v83 → v89 → v95] — the EIGHTEENTH consecutive queue/ledger agreement, the surface names verified against vlm-shots-v89.sh's own header before the derivation) + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only canary prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds; the engine-contract pin 2 passed standalone) + the 89th standing checks (ALL GREEN — the mobile menu VERIFIED WORKING the 89th consecutive time; the reference's four bugs all live; the data census the 89th clean drift check; the SEO pair live both sides) + the quick-action transition-timing family census pin at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 298). The baseline chain FULLY GREEN on a FRESH-CLONE workspace (npm install at the identical lockfile; `.env` with DATABASE_URL="file:../db/custom.db", `db/` at the repo root pushed + seeded, chromium-1243 installed; the seedcheck exact before any flow ran; lint → typecheck → 108 unit → npm run build [robots + sitemap prerendered] → 297 e2e chunk executions [106+98+95 = 299 = 297 unique, zero flakes] → 35/35 smoke). The codebase audit clean (the v94 commit ca38efa re-verified PIN-ONLY as documented [24 files, +2500/−6, ZERO src/ changes]; the one commit since [e0f99f2] session-log-only; the production seams re-audited — auth, db-path, the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout). The v95 cycle's findings: the VLM verdict IDENTICAL — zero style flags on the pair's own target surfaces (the THIRD consecutive IDENTICAL verdict for this pair [v83 → v89 → v95]); every VLM flag the documented standing classes (the seed-data figures; the root-URL active-nav highlight the v56 SUPERSET class; the "Edit with Base44" FAB the platform-chrome class; the avatar "U" vs "D" the user-identity class). The both-sides census — executed in the TWO-HALF controlled form, BUILT TWO-HALF FROM THE START (ref-arbit-v95.sh + clone-arbit-v95.sh via build-twohalf-v95.py, the THREE census blocks [ARBIT_G/ARBIT_Q/ARBIT_X] extracted once and embedded byte-identically across the halves — the md5 line-block contract [b500dd29 / da04e995 / 7a381755]) — REPRODUCES the v89 census values EXACTLY: zero drift on every axis (PART G the guidelines card 468×348/the header/the body/the three tiles with the label/pct/desc chrome — the shadow's transparent lead-layer count the v66 computed-form INVISIBLE class; PART Q the quick-action grid 304px×3/gap 24/w 960/the three cards 304×90 with the full chrome — the grid mt the v77 mechanism class [ref 0px vs clone 32px, the rendered gap 340 byte-identical], the label finder's wrapper catch the v61 label lesson [the clone's LEAF span identical, pinned green by the v61 F3 pin]; PART X cardBottom 1122/gridTop 1462/gap 340 byte-identical). NO NEW CLONE GAP — the v95 iteration PIN-ONLY. The +1 e2e pin: the quick-action TRANSITION-TIMING family census at 1280 (tests/e2e/dashboard.spec.ts — never pinned at ANY viewport: the three cards' transitionTimingFunction {cubic-bezier(0.4, 0, 0.2, 1)} + transitionDelay {0s} [the v89 pin holds the duration/property only] + the three tinted tiles' transition-transform family {dur 0.2s, timing cubic-bezier(0.4, 0, 0.2, 1)} + the three plus icons' transition-opacity family {prop opacity, dur 0.15s, timing, delay 0s} + the docSW 1280 guard; the tiles' transitionProperty asserted in the CONTAINS form — the v95 TAILWIND v4 COMPUTED-FORM class NEW this cycle [the reference's v3 "transform" vs the clone's v4 "transform, translate, scale, rotate" superset, the rendered behavior identical]; the pin's own axes first measured byte-identical on both sides by the supplemental two-half census [qa-timing-arbit-v95.sh + qa-timing-clone-v95.sh via build-qa-timing-v95.py, the census JS byte-identical by the md5 line-block diff ba296202; both sides read-only, the seedcheck exact after the run]). The pin-sanity mutation (the executed form — the viewport-scoped transition-all duration-200 → transition-all duration-200 lg:ease-linear at dashboard-view.tsx:885, by LINE NUMBER; AT-lg because the pin runs at 1280; the line-scoping keeps the file's OTHER transition-all duration-200 instance [line 578] untouched): the failure diff reads as the cardTiming axis ALONE ("cubic-bezier(0.4, 0, 0.2, 1)" → "linear"); the full dashboard.spec.ts under the mutation reads ONLY the v95 pin red (41 green) — cascade-free BY CONSTRUCTION (a timing-function flip affects no geometry and no computed style any other pin asserts; lg:ease-linear appears NOWHERE in src/) — then restored (git diff src/ = 0 lines; the standalone REBUILD via the FULL npm run build; the post-restore full run 42/42 green). The F5 full chain re-run GREEN: lint → typecheck → 108 unit → build → 298 e2e (107+98+95 = 300 chunk executions = 298 unique tests, zero flakes) → 35/35 smoke; the screenshots 16/16 BYTE-IDENTICAL (the same-day-seed byte-identity law — the seed planted and the shots taken on the same calendar day, byte-for-byte reproduction, ZERO arbitration needed — the third consecutive pure-form cycle); the final seedcheck exact. The operational lessons (the probe README's D6 section): the template-brace generator bug (the build-qa-timing-v95.py generator was written with .format()-style doubled braces but applied with .replace() — the generated LOGIN_JS kept literal {{ }} which made agent-browser eval return EMPTY on every attempt [the empty-eval signature matching the v89 resource-exhaustion class but the cause the generator; the discipline: bash -n + a spot grep for doubled braces after ANY generator run, and a manual open+snapshot diagnosis to separate site-down from script-broken]), the two-half form as the default (the v92/v93/v94 lesson applied clean — zero resource-exhaustion symptoms), and the v4 transition-property computed-form class (Tailwind v4's transition-transform computes the expanded property list — the pin form for such axes: CONTAINS, never exact). The docs alignment: D1 AGENTS.md (the v95 paragraph), D2 CLAUDE.md (297 → 298 + the v95 clause at the E2E line's tail), D3 README.md (the counts + the v95 plan-table row), D4 zero-balance_SKILL.md (Session 130 audit row + the state line), D5 the PAD's v1.1.52 revision block, D6 the probe README's v95 section (+ the v96 queue — the v90-era MOBILE 390 twins [v62/v63 → v69 → v78 → v84 → v90 → v96], to be verified against vlm-shots-v90.sh's own header next cycle), D7 session_228.md + the worklog Session 130 entry; docs/remediation-plan-v95.md saved (the validated plan — the pre-execution validation section recording the measured values, the mutation target line verified by reading the source, the coverage-map grep, the disproven-in-advance candidates)."""

CLAUDE_TAIL_OLD = "lg:font-black at net-worth-view.tsx:418 only the v94 pin red — the h2's fw axis alone, cascade-free)"
CLAUDE_TAIL_NEW = ("lg:font-black at net-worth-view.tsx:418 only the v94 pin red — the h2's fw axis alone, cascade-free); "
"the v95 quick-action transition-timing family census pin (the three cards' timing function + delay + the tiles' "
"transition-transform family + the pluses' transition-opacity family at 1280 — never pinned at ANY viewport; the tile's "
"transitionProperty asserted in the CONTAINS form [the v95 v4 computed-form class: the clone's \"transform, translate, "
"scale, rotate\" superset vs the reference's \"transform\"]; the mutation transition-all duration-200 -> transition-all "
"duration-200 lg:ease-linear at dashboard-view.tsx:885 only the v95 pin red — the cardTiming axis alone, cascade-free)")

README_ROW = ("| [`docs/remediation-plan-v95.md`](docs/remediation-plan-v95.md) | **The re-run cycle's next-oldest candidate "
"(the v89-era dashboard pair's fifth re-run [v61 → v68 → v77 → v83 → v89 → v95] — the BUDGET GUIDELINES card + the "
"QUICK-ACTION card row, both below-the-fold surfaces of the dashboard FULL-PAGE at desktop 1280x800, last re-shot v89; "
"the eighteenth consecutive queue/ledger agreement, the surface names verified against the v89 probe scripts) + the axe "
"watch (NO DRIFT) + the quick-action transition-timing family census pin at 1280 (PIN-ONLY — no production-code change; "
"+1 e2e = 298)**: the verdict IDENTICAL — zero style flags on the pair's own target surfaces (the third consecutive "
"IDENTICAL for this pair [v83 → v89 → v95]); every flag the documented standing classes (the seed-data figures; the v56 "
"SUPERSET root-URL nav highlight; the FAB platform-chrome class; the avatar user-identity class); the census — executed "
"in the two-half controlled form BUILT two-half from the start (the ARBIT_G/Q/X blocks md5-identical across the halves) "
"— reproducing the v89 values exactly (zero drift on every axis; the shadow lead-layer the v66 invisible class; the grid "
"mt the v77 mechanism class [rendered gap 340 byte-identical]; the label wrapper-catch the v61 lesson); the +1 pin the "
"TRANSITION-TIMING family {the cards' timing cubic-bezier(0.4, 0, 0.2, 1) + delay 0s + the tiles' transition-transform "
"{dur 0.2s, timing} + the pluses' transition-opacity {prop/dur 0.15s/timing/delay}} — never pinned at ANY viewport (the "
"v89 pin holds the cards' duration/property only), the tile's transitionProperty asserted in the CONTAINS form (the v95 "
"v4 computed-form class: the clone's \"transform, translate, scale, rotate\" superset vs the reference's \"transform\"), "
"the pin's own axes first measured byte-identical on both sides by the supplemental two-half census (both sides "
"read-only); the pin-sanity mutation transition-all duration-200 → transition-all duration-200 lg:ease-linear at "
"dashboard-view.tsx:885 (only the v95 pin red, the failure diff reads as the cardTiming axis alone — cascade-free); the "
"screenshots 16/16 byte-identical (the same-day-seed law — the third consecutive pure-form cycle, zero arbitration "
"needed); the lessons: the template-brace generator bug + the two-half form as the default + the v4 transition-property "
"computed-form class |\n")

def main():
    # D1 — AGENTS.md: append the v95 paragraph (idempotent).
    t = open("AGENTS.md").read()
    if "The v95 parity iteration" not in t:
        if not t.endswith("\n"):
            t += "\n"
        t += AGENTS_PARA + "\n"
        open("AGENTS.md", "w").write(t)
        print("D1 AGENTS.md: v95 paragraph appended")
    else:
        print("D1 AGENTS.md: already present")

    # D2 — CLAUDE.md: 297 -> 298 + the v95 clause at the E2E line's tail.
    t = open("CLAUDE.md").read()
    changed = 0
    if "**E2E (Playwright, 297)**" in t:
        t = t.replace("**E2E (Playwright, 297)**", "**E2E (Playwright, 298)**", 1)
        changed += 1
    if CLAUDE_TAIL_OLD in t and "lg:ease-linear at dashboard-view.tsx:885" not in t:
        t = t.replace(CLAUDE_TAIL_OLD, CLAUDE_TAIL_NEW, 1)
        changed += 1
    open("CLAUDE.md", "w").write(t)
    print(f"D2 CLAUDE.md: {changed} edits applied")

    # D3 — README.md: the counts (two places) + the v95 row before the v94 row.
    t = open("README.md").read()
    changed = 0
    if "Playwright specs (297 tests)" in t:
        t = t.replace("Playwright specs (297 tests)", "Playwright specs (298 tests)", 1)
        changed += 1
    if "Playwright e2e (297 tests)" in t:
        t = t.replace("Playwright e2e (297 tests)", "Playwright e2e (298 tests)", 1)
        changed += 1
    anchor = "| [`docs/remediation-plan-v94.md`](docs/remediation-plan-v94.md)"
    if anchor in t and "remediation-plan-v95.md" not in t:
        t = t.replace(anchor, README_ROW + anchor, 1)
        changed += 1
    open("README.md", "w").write(t)
    print(f"D3 README.md: {changed} edits applied")

if __name__ == "__main__":
    main()
