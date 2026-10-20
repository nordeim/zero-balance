#!/usr/bin/env python3
"""align-v96-worklog.py — the worklog's v96 alignment: the doc-list tail
(remediation-plan-v96.md) + the Session 131 entry inserted newest-first
(before the Session 130 heading). Idempotent."""

SESSION_131 = """## Session 131 — Parity iteration v96: the re-run cycle's next-oldest candidate (the v90-era MOBILE 390 twins' fifth re-run) + the axe watch (NO DRIFT) + the head-row typography/figure-fit census pin (PIN-ONLY) (2026-10-20)

**The cycle** (`docs/remediation-plan-v96.md` — the plan validated against the codebase before execution; the narrative: `docs/session_230.md`): the re-run cadence's next-oldest candidate — the v90-era MOBILE 390 twins (the /NETWORTH view + the DASHBOARD FULL-PAGE pair at 390x844, last re-shot v90 — now the oldest remaining [v90 < v91 < v92 < v93 < v94 < v95]; the pair's FIFTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96]; the NINETEENTH consecutive queue/ledger agreement, the surface names verified against vlm-shots-v90.sh's own header before the derivation) + the axe-core watch at its re-check point + the 90th standing checks. PIN-ONLY for src/ — no production-code change; +1 e2e = 299.

**The baseline — the CARRIED-OVER workspace** (the session-log-only commit class): `git pull` to main @ 2b0bb52 (the docs-only session-log commit [docs/session_229.md, 99 insertions] — ZERO src/ or lockfile deltas since the v95 push 7a1ce9a, so the v95 cycle's own fresh-clone environment carries over unchanged, no re-provisioning); the seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran; lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · **298 e2e ✓** (139+100+61 = 300 chunk executions = 298 unique, zero flakes on the first run) · 35/35 smoke ✓. The codebase audit clean (the v95 commit verified PIN-ONLY as documented; the production seams re-audited — auth, db-path, the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout).

**F1 the axe-core watch: NO DRIFT** — npm-latest 4.14.0 (only sha prereleases beyond — no stable, no 5.x); the installed wrapper + engine both 4.14.0; the v68 dedupe holds; the engine-contract pin 2 passed standalone.

**F2 the 90th standing checks: ALL GREEN** (ref-standing-v90.sh + standing-checks-v90.sh, derived from the v89 pair via the PERSISTED derive-standing-v96.py across the three token families, version-bump-only verified by the normalize-back diff): the reference's four bugs ALL live (toast-blocker / sheet-trap / no-landmark / the 464px /networth overflow — **the overflow re-verified with the settle-wait after the script's sleep-3 raced the reference's client-side boot and read the PRE-RENDER document [390/390]; the 8s+2s re-read measured the true 464 — the standing-script timing artifact lesson**); the data census the 90th clean drift check; the SEO pair live both sides. Clone side: R1–R4 ALL GREEN — **the mobile menu VERIFIED WORKING the 90th consecutive time** (hitIsBurgerChild:true, the sheet opens, closes on nav, the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

**F3 the re-run pair** (vlm-shots-v96.sh + clone-vlmshots-v96.sh + vlm-compare-v96.mjs + arbit-v96.sh — the derivation from the v90 lineage via the PERSISTED derive-v96-series.py: the generic swaps + the exact-fragment history corrections, every correction's hit/miss REPORTED by the script itself [the derivation miss-report discipline — the one first-run MISS caught and fixed before any probe executed]; the two-half census BUILT two-half from the start via build-twohalf-v96.py — the NW/DASH census blocks byte-identical across the halves by the md5 line-block contract [82cf8a43 / 85e4ec7e]; the reaping budget applied as the standing step; login on the first attempt both sides; the parked pointer at (5,5); read-only — the v46 rule holds): **BOTH verdicts DIFFERENT (the pair's documented verdict class — same as v84/v90), every flag DOM-arbitrated to a documented class** — the stat-tile stacking the v41 mobile-superset class; the subtitle wrap-point the v62 width-delta class; the FAB the platform-chrome class; the figures/donut the seed-data classes; **the NEW clipped-figure flag ("-$245,950.00 clipped on the left") DOM-arbitrated as a VLM MISREAD** (figclip-clone-v96.sh: the textRect flush at the content-left [textLeftOfContent 0 — zero overhang] and 115px inside the content-right, figureScrolls false, docSW 390 — the figure fully in-bounds; the FLUSH-LEFT FIGURE PERCEPTION CLASS new this cycle). The census **REPRODUCES the v90 census values EXACTLY: zero drift on every axis** (the summary card/statGrid/tiles/medallion/trendIcon families; the subtitle chrome; the breakdown card's svg family; the children heights; the spendingCard finder reading the SAME fallback string on both sides — the heading is a div on both sites). **NO NEW CLONE GAP.**

**F4 the +1 e2e pin (298 → 299): the summary-card HEAD-ROW typography + FIGURE-FIT census at 390** (tests/e2e/networth.spec.ts — the FAMILY-EXTENSION pattern: the figure's fw + color pinned at 640/1280 but NEVER at 390 [the v41 F3 pin holds the fs only]; the label's family pinned at 1280 only; the figure's FIT contract never pinned at ANY viewport — the flush-left start, the in-bounds right, the no-scroll state; + the figure {fs 24px, fw 700, color white, lh 32px} + the label {fs 14px, fw 400, color rgba(255,255,255,0.8), mb 8px, h 20} + the card box re-affirm + the docSW 390 guard; the pin's own axes first measured byte-identical on BOTH sides by the supplemental two-half census [headrow-arbit-v96.sh + headrow-clone-v96.sh via build-headrow-v96.py, the census JS byte-identical by the md5 line-block diff 519ef222; both sides read-only; the seedcheck exact after the run]) — GREEN on first run. **The pin-sanity mutation (the executed form)**: the figure's `font-bold` → `font-bold max-sm:font-extrabold` (net-worth-view.tsx:348, by LINE NUMBER — the line-scoping keeps the stat-tile VALUE's identical class string at line 372 untouched; AT-max-sm because the pin runs at 390 and the variant is INERT at ≥640 — the v90 LESSON APPLIED, the 640/1280-tier pins stay green): ONLY the v96 pin red (30 green under the mutation), the failure diff reads as the figure fw axis ALONE ("700" → "800") — cascade-free BY CONSTRUCTION (font-weight never changes line-height — the card-height arithmetic [421, the v63 F3 pin] unchanged; font-weight never affects color; max-sm: appears NOWHERE in src/) — then restored (git diff src/ = 0 lines; the standalone REBUILD via the FULL npm run build; the post-restore full run 31/31 green).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **299 e2e** (140+100+61 = 301 chunk executions = 299 unique tests, zero flakes) · 35/35 smoke ✓; the screenshots **15/16 BYTE-IDENTICAL + 1/16 the DATE class** (the cycle crosses the UTC midnight boundary — the 07-add-item-modal's day digits "19"→"20" rolled [the budget-item-dialog's render-time default date todayIso(), line 83, the mechanism]; the pixel-diff-v96.py arbitration localizing the delta to a 32×22px region at x1535 — exactly the two day digits, the v75 acceptance form; everything else byte-stable); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v96 paragraph), D2 CLAUDE.md (298 → 299 + the v96 clause at the E2E line's tail), D3 README.md (the counts + the v96 plan-table row), D4 zero-balance_SKILL.md (Session 131 audit row + the state line + the last_updated date), D5 the PAD's v1.1.53 revision block, D6 the probe README's v96 section (the standing-script timing artifact lesson + the flush-left figure perception class + the derivation miss-report discipline + the DATE-class arbitration record + the v97 queue), D7 session_230.md + this Session 131 entry.

**The next queue:** the v97 cycle — the v91-era ITEMS pair (the INCOME + EXPENSES view pair at desktop 1280x800, last re-shot v91 — now the oldest remaining [v91 < v92 < v93 < v94 < v95 < v96]; the pair's SIXTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97]); verify against the rotation ledger first, per protocol.

---

"""

def main():
    t = open("worklog.md").read()
    changed = 0
    # The doc-list tail: add remediation-plan-v96.md after v95.
    old_tail = "and `docs/remediation-plan-v95.md`.\n"
    new_tail = "and `docs/remediation-plan-v95.md`,\nand `docs/remediation-plan-v96.md`.\n"
    if old_tail in t and "remediation-plan-v96.md" not in t:
        t = t.replace(old_tail, new_tail, 1)
        changed += 1
    # The Session 131 entry inserted before the Session 130 heading.
    anchor = "## Session 130 — Parity iteration v95:"
    if anchor in t and "## Session 131 — Parity iteration v96:" not in t:
        t = t.replace(anchor, SESSION_131 + anchor, 1)
        changed += 1
    open("worklog.md", "w").write(t)
    print(f"worklog.md: {changed} edits applied")

if __name__ == "__main__":
    main()
