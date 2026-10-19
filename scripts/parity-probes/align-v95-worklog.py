#!/usr/bin/env python3
"""align-v95-worklog.py — the worklog's v95 alignment: the doc-list tail
(remediation-plan-v95.md) + the Session 130 entry inserted newest-first
(before the Session 129 heading). Idempotent."""

SESSION_130 = """## Session 130 — Parity iteration v95: the re-run cycle's next-oldest candidate (the v89-era dashboard pair's fifth re-run) + the axe watch (NO DRIFT) + the quick-action transition-timing family census pin (PIN-ONLY) (2026-10-19/20)

**The cycle** (`docs/remediation-plan-v95.md` — the plan validated against the codebase before execution; the narrative: `docs/session_228.md`): the re-run cadence's next-oldest candidate — the v89-era DASHBOARD pair (the BUDGET GUIDELINES card + the QUICK-ACTION card row, both below-the-fold surfaces of the dashboard FULL-PAGE at desktop 1280x800, last re-shot v89 — now the oldest remaining [v89 < v90 < v91 < v92 < v93 < v94]; the pair's FIFTH re-run [v61 → v68 → v77 → v83 → v89 → v95]; the EIGHTEENTH consecutive queue/ledger agreement, the surface names verified against vlm-shots-v89.sh's own header before the derivation) + the axe-core watch at its re-check point + the 89th standing checks. PIN-ONLY for src/ — no production-code change; +1 e2e = 298.

**The baseline — a FRESH-CLONE workspace** (the sandbox reset between cycles): `git clone` to main @ e0f99f2 (the session-log-only commit — ZERO src/ or lockfile deltas since the v94 push ca38efa); the environment provisioned from scratch (npm install at the identical lockfile; `.env` with `DATABASE_URL="file:../db/custom.db"`; `db/` at the repo root pushed + seeded; chromium-1243 installed); the seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran; lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · **297 e2e ✓** (106+98+95 = 299 chunk executions = 297 unique, zero flakes on the first run) · 35/35 smoke ✓. The codebase audit clean (the v94 commit verified PIN-ONLY as documented; the production seams re-audited — auth, db-path, the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout).

**F1 the axe-core watch: NO DRIFT** — npm-latest 4.14.0 (only canary prereleases beyond — no stable, no 5.x); the installed wrapper + engine both 4.14.0; the v68 dedupe holds; the engine-contract pin 2 passed standalone.

**F2 the 89th standing checks: ALL GREEN** (ref-standing-v89.sh + standing-checks-v89.sh, version-bumped from the v88 pair across the three token families, version-bump-only verified by the normalize-back diff): the reference's four bugs ALL live (toast-blocker / sheet-trap / no-landmark / the 464px /networth overflow); the data census the 89th clean drift check; the SEO pair live both sides. Clone side: R1–R4 ALL GREEN — **the mobile menu VERIFIED WORKING the 89th consecutive time** (hitIsBurgerChild:true, the sheet opens, closes on nav, the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

**F3 the re-run pair** (vlm-shots-v95.sh + clone-vlmshots-v95.sh + vlm-compare-v95.mjs + arbit-v95.sh — the sed derivation from the v89 lineage with the version + ordinal + agreement-count + second-pass session-name substitutions, the headers history-corrected to the FIFTH re-run, the functional bodies verified version-bump-only by the normalize-back diff; the two-half census BUILT two-half from the start via build-twohalf-v95.py — the ARBIT_G/Q/X census blocks byte-identical across the halves by the md5 line-block contract [b500dd29 / da04e995 / 7a381755]; the reaping budget applied as the standing step; login on the first attempt both sides; the parked pointer at (5,5); read-only — the v46 rule holds): **the verdict IDENTICAL — zero style flags on the pair's own target surfaces** (the THIRD consecutive IDENTICAL for this pair [v83 → v89 → v95]); every VLM flag the documented standing classes (the seed-data figures; the v56 SUPERSET root-URL active-nav highlight; the "Edit with Base44" FAB the platform-chrome class; the avatar "U" vs "D" the user-identity class). The census **REPRODUCES the v89 census values EXACTLY: zero drift on every axis** (PART G the guidelines card + the three tiles — the shadow lead-layer the v66 invisible class; PART Q the quick-action grid + the three cards — the grid mt the v77 mechanism class [rendered gap 340 byte-identical], the label wrapper-catch the v61 lesson; PART X cardBottom 1122/gridTop 1462/gap 340 byte-identical). **NO NEW CLONE GAP.**

**F4 the +1 e2e pin (297 → 298): the quick-action TRANSITION-TIMING family census at 1280** (tests/e2e/dashboard.spec.ts — never pinned at ANY viewport: the three cards' transitionTimingFunction {cubic-bezier(0.4, 0, 0.2, 1)} + transitionDelay {0s} [the v89 pin holds the duration/property only] + the three tinted tiles' transition-transform family {dur 0.2s, timing} + the three plus icons' transition-opacity family {prop opacity, dur 0.15s, timing, delay 0s} + the docSW 1280 guard; the tiles' transitionProperty asserted in the CONTAINS form — **the v95 TAILWIND v4 COMPUTED-FORM class NEW this cycle** [the reference's v3 "transform" vs the clone's v4 "transform, translate, scale, rotate" superset, the rendered behavior identical, documented from live both-sides evidence]; the pin's own axes first measured byte-identical on BOTH sides by the supplemental two-half census [qa-timing-arbit-v95.sh + qa-timing-clone-v95.sh via build-qa-timing-v95.py, the census JS byte-identical by the md5 line-block diff ba296202; both sides read-only; the seedcheck exact after the run]) — GREEN on first run. **The pin-sanity mutation (the executed form)**: the card's `transition-all duration-200` → `transition-all duration-200 lg:ease-linear` (dashboard-view.tsx:885, by LINE NUMBER — the line-scoping keeps the file's OTHER transition-all duration-200 instance [line 578] untouched; AT-lg because the pin runs at 1280): ONLY the v95 pin red (41 green under the mutation), the failure diff reads as the cardTiming axis ALONE ("cubic-bezier(0.4, 0, 0.2, 1)" → "linear") — cascade-free BY CONSTRUCTION (a timing-function flip affects no geometry and no computed style any other pin asserts; lg:ease-linear appears NOWHERE in src/) — then restored (git diff src/ = 0 lines; the standalone REBUILD via the FULL npm run build; the post-restore full run 42/42 green).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **298 e2e** (107+98+95 = 300 chunk executions = 298 unique tests, zero flakes) · 35/35 smoke ✓; the screenshots **16/16 BYTE-IDENTICAL** (the same-day-seed byte-identity law — the third consecutive pure-form cycle, ZERO arbitration needed); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v95 paragraph), D2 CLAUDE.md (297 → 298 + the v95 clause at the E2E line's tail), D3 README.md (the counts + the v95 plan-table row), D4 zero-balance_SKILL.md (Session 130 audit row + the state line), D5 the PAD's v1.1.52 revision block, D6 the probe README's v95 section (the template-brace generator bug lesson + the two-half-form-as-default lesson + the v4 transition-property computed-form class lesson + the v96 queue), D7 session_228.md + this Session 130 entry.

**The next queue:** the v96 cycle — the v90-era MOBILE 390 twins (the /networth + the dashboard FULL-PAGE pair at 390x844, last re-shot v90 — now the oldest remaining [v90 < v91 < v92 < v93 < v94 < v95]; the pair's FIFTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96]); verify against the rotation ledger first, per protocol.

---

"""

def main():
    t = open("worklog.md").read()
    changed = 0
    # The doc-list tail: add remediation-plan-v95.md after v94.
    old_tail = "and `docs/remediation-plan-v94.md`.\n"
    new_tail = "and `docs/remediation-plan-v94.md`,\nand `docs/remediation-plan-v95.md`.\n"
    if old_tail in t and "remediation-plan-v95.md" not in t:
        t = t.replace(old_tail, new_tail, 1)
        changed += 1
    # The Session 130 entry inserted before the Session 129 heading.
    anchor = "## Session 129 — Parity iteration v94:"
    if anchor in t and "## Session 130 — Parity iteration v95:" not in t:
        t = t.replace(anchor, SESSION_130 + anchor, 1)
        changed += 1
    open("worklog.md", "w").write(t)
    print(f"worklog.md: {changed} edits applied")

if __name__ == "__main__":
    main()
