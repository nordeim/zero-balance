#!/usr/bin/env python3
"""align-v96-a.py — D1-D3 docs alignment for the v96 cycle:
D1 AGENTS.md (the v96 paragraph), D2 CLAUDE.md (298->299 + the v96 clause
at the E2E line's tail), D3 README.md (the counts + the v96 plan-table row
inserted before the v95 row). Idempotent."""

AGENTS_PARA = """

The v96 parity iteration (2026-10-20, PIN-ONLY for src/ — no production-code change; +1 e2e = 299; the plan `docs/remediation-plan-v96.md`, the narrative `docs/session_230.md`, the worklog Session 131 entry): the re-run cycle's next-oldest candidate — the v90-era MOBILE 390 twins (the /NETWORTH view + the DASHBOARD FULL-PAGE pair at 390x844, last re-shot v90, now the oldest remaining [v90 < v91 < v92 < v93 < v94 < v95]; the pair's FIFTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96] — the NINETEENTH consecutive queue/ledger agreement, the surface names verified against vlm-shots-v90.sh's own header before the derivation) + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only sha prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds; the engine-contract pin 2 passed standalone) + the 90th standing checks (ALL GREEN — the mobile menu VERIFIED WORKING the 90th consecutive time; the reference's four bugs all live [the 464px /networth overflow re-verified with the settle-wait after the standing script's sleep-3 raced the reference's client-side boot — the timing-artifact lesson]; the data census the 90th clean drift check; the SEO pair live both sides) + the summary-card head-row typography + figure-fit census pin at 390 (PIN-ONLY for src/ — no production-code change; +1 e2e = 299). The baseline chain FULLY GREEN on the CARRIED-OVER workspace (the session-log-only commit class: pulled to main @ 2b0bb52 — the docs-only session-log commit [docs/session_229.md, 99 insertions], ZERO src/ or lockfile deltas since the v95 push 7a1ce9a, so the v95 cycle's own fresh-clone environment carries over unchanged, no re-provisioning; the seedcheck exact before any flow ran; lint → typecheck → 108 unit → npm run build [robots + sitemap prerendered] → 298 e2e chunk executions [139+100+61 = 300 = 298 unique, zero flakes on the first run] → 35/35 smoke). The codebase audit clean (the v95 commit 7a1ce9a re-verified PIN-ONLY as documented [25 files, +2361/−5, ZERO src/ changes]; the one commit since session-log-only; the production seams re-audited — auth, db-path, the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout). The v96 cycle's findings: BOTH VLM verdicts DIFFERENT (the pair's documented verdict class — same as v84/v90) with every flag DOM-arbitrated to a documented class (the stat-tile stacking the v41 mobile-superset class; the subtitle wrap-point the v62 width-delta class; the FAB the platform-chrome class; the figures/counts/donut the seed-data classes) — INCLUDING the NEW clipped-figure flag ("-$245,950.00 clipped on the left") DOM-arbitrated as a VLM MISREAD by the supplemental figclip one-shot census (figclip-clone-v96.sh: the figure H2 at x=48 w=179 h=32, the textRect flush at the content-left [textLeftOfContent 0 — zero overhang] and 115px inside the content-right, figureScrolls false, docSW 390 — the figure fully in-bounds on every axis; the flag rides the VLM's perception of the flush-left negative figure against the gradient — the FLUSH-LEFT FIGURE PERCEPTION CLASS new this cycle). The both-sides census — executed in the TWO-HALF controlled form, BUILT TWO-HALF FROM THE START (ref-arbit-v96.sh + clone-arbit-v96.sh via build-twohalf-v96.py, the TWO census blocks [NW_CENSUS 42 lines + DASH_CENSUS 87 lines] extracted once and embedded byte-identically across the halves — the md5 line-block contract [82cf8a43 / 85e4ec7e]) — REPRODUCES the v90 census values EXACTLY: zero drift on every axis (the summary card/statGrid/tiles/medallion/trendIcon families; the subtitle chrome; the breakdown card's svg family [svgCount 7, the 16/14 alternation, rechartsWrappers 0, pieSectors 0] + the children heights; the spendingCard finder reading the SAME fallback string on both sides — the heading is a div, not an h1-h4, on both sites). NO NEW CLONE GAP — the v96 iteration PIN-ONLY. The +1 e2e pin: the summary-card HEAD-ROW typography + FIGURE-FIT census at 390 (tests/e2e/networth.spec.ts — the FAMILY-EXTENSION pattern: the figure's fw + color pinned at 640/1280 but NEVER at 390 [the v41 F3 pin holds figureFont fs only]; the label's family pinned at 1280 only; the figure's FIT contract never pinned at ANY viewport: the flush-left start [textLeftOverhang 0], the in-bounds right [textRightMargin ≥ 0], the no-scroll state; + the figure {fs 24px, fw 700, color white, lh 32px} + the label {fs 14px, fw 400, color rgba(255,255,255,0.8), mb 8px, h 20} + the card box re-affirm + the docSW 390 guard; the pin's own axes first measured byte-identical on both sides by the supplemental two-half census [headrow-arbit-v96.sh + headrow-clone-v96.sh via build-headrow-v96.py, the census JS byte-identical by the md5 line-block diff 519ef222; both sides read-only; the seedcheck exact after the run]). The pin-sanity mutation (the executed form — the viewport-scoped break-words text-2xl font-bold text-white sm:text-5xl → + max-sm:font-extrabold at net-worth-view.tsx:348, by LINE NUMBER; AT-max-sm because the pin runs at 390 and the variant is INERT at ≥640 — the v90 LESSON APPLIED: the bare font-bold swap would cascade to the 640-tier v41 F2 fw pin and the 1280-tier v60 F1 figure pin; the line-scoping keeps the stat-tile VALUE's identical class string at line 372 untouched): the failure diff reads as the figure fw axis ALONE ("700" → "800" below 640px); the full networth.spec.ts under the mutation reads ONLY the v96 pin red (30 green) — cascade-free BY CONSTRUCTION (font-weight never changes line-height — the figure's lh stays 32px, the h 32 and the card-height arithmetic [421, the v63 F3 pin] unchanged; font-weight never affects color; max-sm: appears NOWHERE in src/) — then restored (git diff src/ = 0 lines; the standalone REBUILD via the FULL npm run build; the post-restore full run 31/31 green). The F5 full chain re-run GREEN: lint → typecheck → 108 unit → build → 299 e2e (140+100+61 = 301 chunk executions = 299 unique tests, zero flakes) → 35/35 smoke; the screenshots 15/16 BYTE-IDENTICAL + 1/16 the DATE class (the 07-add-item-modal's day digits "19"→"20" rolled across the UTC midnight boundary — the v96 cycle crosses it [the seed + the baseline shots Oct 19 22:41 UTC, the regeneration Oct 20 00:1x UTC]; the budget-item-dialog's render-time default date todayIso() [line 83] the mechanism; the pixel-diff-v96.py arbitration localizing the delta to a 32×22px region at x1535 — exactly the two day digits, the v75 arbitration form [width ≤ 48, height ≤ 40, x > 1000] — everything else byte-stable); the final seedcheck exact. The operational lessons (the probe README's D6 section): the standing-script timing artifact (the reference-side R-bug-4 read docSW 390/390 on the script's sleep-3 — the eval raced the client-side boot and measured the PRE-RENDER document; the 8s+2s settle re-read measured the true 464; the discipline: when a standing bug check reads CLEAN against its own documented-live history, re-measure with an explicit settle-wait before recording any state change), the flush-left figure perception class (the VLM flags a "clipped" negative currency figure when the text starts flush at the content-box left edge — the arbitration is the Range-walk textRect vs the padding-aware content box, NOT the element rect alone), the two-half form as the default (applied clean again — zero resource-exhaustion symptoms), and the derivation miss-report discipline (the derive script reports every correction's hit/miss — the one first-run MISS [the lowercase 'the' in the verdict-note fragment] was caught by the report itself and fixed before any probe executed). The docs alignment: D1 AGENTS.md (the v96 paragraph), D2 CLAUDE.md (298 → 299 + the v96 clause at the E2E line's tail), D3 README.md (the counts + the v96 plan-table row), D4 zero-balance_SKILL.md (Session 131 audit row + the state line), D5 the PAD's v1.1.53 revision block, D6 the probe README's v96 section (+ the v97 queue — the v91-era ITEMS pair [v57 → v64 → v70 → v79 → v85 → v91 → v97], to be verified against vlm-shots-v91.sh's own header next cycle), D7 session_230.md + the worklog Session 131 entry; docs/remediation-plan-v96.md saved (the validated plan — the pre-execution validation section recording the measured values, the mutation target line verified by reading the source, the coverage-map grep, the disproven-in-advance candidates)."""

CLAUDE_TAIL_OLD = "lg:ease-linear at dashboard-view.tsx:885 only the v95 pin red — the cardTiming axis alone, cascade-free)"
CLAUDE_TAIL_NEW = ("lg:ease-linear at dashboard-view.tsx:885 only the v95 pin red — the cardTiming axis alone, cascade-free); "
"the v96 summary-card head-row typography + figure-fit census pin at 390 (the figure's fw/color family — pinned at 640/1280 "
"only before — + the label family + the in-bounds fit contract [the v96 figclip arbitration's own axes: the flush-left "
"start, the in-bounds right, the no-scroll state]; the mutation font-bold -> font-bold max-sm:font-extrabold at "
"net-worth-view.tsx:348 only the v96 pin red — the figure fw axis alone, cascade-free; the max-sm dodge keeps the "
"640/1280-tier pins green)")

README_ROW = ("| [`docs/remediation-plan-v96.md`](docs/remediation-plan-v96.md) | **The re-run cycle's next-oldest candidate "
"(the v90-era MOBILE 390 twins' fifth re-run [v62/v63 → v69 → v78 → v84 → v90 → v96] — the /networth + the dashboard "
"FULL-PAGE pair at 390x844, last re-shot v90; the nineteenth consecutive queue/ledger agreement, the surface names "
"verified against the v90 probe scripts) + the axe watch (NO DRIFT) + the summary-card head-row typography + figure-fit "
"census pin at 390 (PIN-ONLY — no production-code change; +1 e2e = 299)**: BOTH verdicts DIFFERENT (the pair's documented "
"verdict class — same as v84/v90) with every flag DOM-arbitrated to a documented class — including the NEW clipped-figure "
"flag (\"-$245,950.00 clipped on the left\") arbitrated as a VLM MISREAD by the supplemental figclip one-shot census (the "
"textRect flush at the content-left [zero overhang] and 115px inside the content-right, figureScrolls false — the figure "
"fully in-bounds; the FLUSH-LEFT FIGURE PERCEPTION CLASS new this cycle); the census — executed in the two-half "
"controlled form BUILT two-half from the start (the NW/DASH census blocks md5-identical across the halves) — reproducing "
"the v90 values exactly (zero drift on every axis; the stat-tile stacking the v41 class; the subtitle wrap the v62 class; "
"the spendingCard finder reading the same fallback string on both sides — the heading is a div on both sites); the +1 pin "
"the HEAD-ROW typography + FIGURE-FIT family {the figure's fw 700 + color white [pinned at 640/1280 only before] + the "
"label {14px/400/rgba(255,255,255,0.8)/mb 8/h 20} + the in-bounds fit contract [the flush-left start, the in-bounds "
"right, the no-scroll state] — never pinned at ANY viewport}, the pin's own axes first measured byte-identical on both "
"sides by the supplemental two-half census (both sides read-only); the pin-sanity mutation font-bold → font-bold "
"max-sm:font-extrabold at net-worth-view.tsx:348 (only the v96 pin red, the failure diff reads as the figure fw axis "
"alone — cascade-free; the max-sm dodge keeps the 640/1280-tier pins green); the screenshots 15/16 byte-identical + 1/16 "
"the DATE class (the 07-add-item-modal's day digits rolled across the UTC midnight — the pixel-diff arbitration "
"localizing the 32×22px delta to the two day digits, the v75 form); the lessons: the standing-script timing artifact + "
"the flush-left figure perception class + the derivation miss-report discipline |\n")

def main():
    # D1 — AGENTS.md: append the v96 paragraph (idempotent).
    t = open("AGENTS.md").read()
    if "The v96 parity iteration" not in t:
        if not t.endswith("\n"):
            t += "\n"
        t += AGENTS_PARA + "\n"
        open("AGENTS.md", "w").write(t)
        print("D1 AGENTS.md: v96 paragraph appended")
    else:
        print("D1 AGENTS.md: already aligned")

    # D2 — CLAUDE.md: 298 -> 299 in the E2E line + the v96 clause at its tail.
    c = open("CLAUDE.md").read()
    changed = 0
    if "**E2E (Playwright, 298)**" in c and "the v96 summary-card head-row typography" not in c:
        c = c.replace("**E2E (Playwright, 298)**", "**E2E (Playwright, 299)**", 1)
        changed += 1
    if CLAUDE_TAIL_OLD in c and "the v96 summary-card head-row typography" not in c:
        c = c.replace(CLAUDE_TAIL_OLD, CLAUDE_TAIL_NEW, 1)
        changed += 1
    open("CLAUDE.md", "w").write(c)
    print(f"D2 CLAUDE.md: {changed} edits applied")

    # D3 — README.md: the counts (298 -> 299) + the v96 plan-table row before the v95 row.
    r = open("README.md").read()
    changed = 0
    if "Playwright specs (298 tests)" in r and "remediation-plan-v96.md" not in r:
        r = r.replace("Playwright specs (298 tests)", "Playwright specs (299 tests)", 1)
        changed += 1
    if "Playwright e2e (298 tests)" in r and "remediation-plan-v96.md" not in r:
        r = r.replace("Playwright e2e (298 tests)", "Playwright e2e (299 tests)", 1)
        changed += 1
    anchor = "| [`docs/remediation-plan-v95.md`](docs/remediation-plan-v95.md)"
    if anchor in r and "remediation-plan-v96.md" not in r:
        r = r.replace(anchor, README_ROW + anchor, 1)
        changed += 1
    open("README.md", "w").write(r)
    print(f"D3 README.md: {changed} edits applied")

if __name__ == "__main__":
    main()
