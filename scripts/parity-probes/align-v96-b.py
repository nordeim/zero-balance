#!/usr/bin/env python3
"""align-v96-b.py — D4-D6 docs alignment for the v96 cycle:
D4 zero-balance_SKILL.md (Session 131 audit row + the state line),
D5 the PAD's v1.1.53 revision block, D6 the probe README's v96 section
(+ the v97 queue). Idempotent."""

SKILL_ROW = ("| 2026-10-20 | Session 131 — parity iteration v96 (`docs/remediation-plan-v96.md`) | "
"**The re-run cycle's next-oldest candidate (the v90-era MOBILE 390 twins' fifth re-run "
"[v62/v63 → v69 → v78 → v84 → v90 → v96] — the /networth + the dashboard FULL-PAGE pair at 390x844, "
"last re-shot v90; the nineteenth consecutive queue/ledger agreement) + the axe watch (NO DRIFT) + the "
"summary-card head-row typography + figure-fit census pin at 390 (PIN-ONLY — no production-code change; "
"+1 e2e = 299)**: BOTH verdicts DIFFERENT (the pair's documented verdict class — same as v84/v90) with "
"every flag DOM-arbitrated to a documented class — including the NEW clipped-figure flag "
"(\"-$245,950.00 clipped on the left\") arbitrated as a VLM MISREAD by the supplemental figclip one-shot "
"census (the textRect flush at the content-left [zero overhang] and 115px inside the content-right, "
"figureScrolls false — the figure fully in-bounds; the FLUSH-LEFT FIGURE PERCEPTION CLASS new this "
"cycle); the two-half census (BUILT two-half from the start — the NW/DASH census blocks md5-identical "
"across the halves) reproducing v90 exactly (zero drift on every axis; the stat-tile stacking the v41 "
"class; the subtitle wrap the v62 class; the spendingCard finder reading the same fallback string on "
"both sides — the heading is a div on both sites); the +1 pin the HEAD-ROW typography + FIGURE-FIT "
"family at 390 (the figure's fw 700 + color white [pinned at 640/1280 only before — the family-extension "
"pattern] + the label {14px/400/rgba(255,255,255,0.8)/mb 8/h 20} + the in-bounds fit contract [the "
"flush-left start, the in-bounds right, the no-scroll state] — never pinned at ANY viewport), the pin's "
"own axes first measured byte-identical on both sides by the supplemental two-half census (both sides "
"read-only); the mutation font-bold → font-bold max-sm:font-extrabold at net-worth-view.tsx:348 (only "
"the v96 pin red — the figure fw axis alone, cascade-free by construction; the max-sm dodge keeps the "
"640/1280-tier pins green); 15/16 screenshots byte-identical + 1/16 the DATE class (the 07-add-item-modal's "
"day digits rolled across the UTC midnight — the pixel-diff arbitration localizing the 32×22px delta to "
"the two day digits, the v75 form); the lessons: the standing-script timing artifact + the flush-left "
"figure perception class + the derivation miss-report discipline |** 108/299/35 green |\n")

PAD_BLOCK = """#### Revision Block — v1.1.53 (Tracked Changes)
- `[UI]` v1.1.53 (2026-10-20) — the v96 parity iteration (PIN-ONLY — no production-code change): the counts 108 unit / **299 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v90-era MOBILE 390 twins' FIFTH re-run [v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96] — the /NETWORTH view + the DASHBOARD FULL-PAGE pair at 390x844, last re-shot v90; the nineteenth consecutive queue/ledger agreement, the surface names verified against vlm-shots-v90.sh's own header before the derivation) + the axe watch (NO DRIFT — 4.14.0 npm-latest, only sha prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds; the engine-contract pin 2 passed standalone) + the 90th standing checks (the mobile menu verified the 90th consecutive time; the reference's four bugs all live [the 464px /networth overflow re-verified with the settle-wait after the standing script's sleep-3 raced the reference's client-side boot — the timing-artifact lesson]; the data census the 90th clean drift check)**: BOTH verdicts DIFFERENT (the pair's documented verdict class — same as v84/v90) with every flag DOM-arbitrated to a documented class (the stat-tile stacking the v41 mobile-superset class; the subtitle wrap-point the v62 width-delta class; the FAB the platform-chrome class; the figures/counts/donut the seed-data classes) — including the NEW clipped-figure flag ("-$245,950.00 clipped on the left") DOM-arbitrated as a VLM MISREAD by the supplemental figclip one-shot census (figclip-clone-v96.sh: the figure H2 at x=48 w=179 h=32, the textRect flush at the content-left [textLeftOfContent 0 — zero overhang] and 115px inside the content-right, figureScrolls false, docSW 390 — the figure fully in-bounds on every axis; the FLUSH-LEFT FIGURE PERCEPTION CLASS new this cycle); the both-sides census — executed in the TWO-HALF controlled form BUILT two-half from the start (ref-arbit-v96.sh + clone-arbit-v96.sh via build-twohalf-v96.py, the TWO census blocks [NW_CENSUS/DASH_CENSUS] byte-identical across the halves by the md5 line-block contract [82cf8a43 / 85e4ec7e]) — REPRODUCING the v90 census values EXACTLY (the summary card/statGrid/tiles/medallion/trendIcon families; the subtitle chrome; the breakdown card's svg family; the children heights; the spendingCard finder reading the SAME fallback string on both sides — the heading is a div, not an h1-h4, on both sites); NO NEW CLONE GAP; the +1 e2e pin the summary-card HEAD-ROW typography + FIGURE-FIT census at 390 (tests/e2e/networth.spec.ts — the FAMILY-EXTENSION pattern: the figure's fw + color pinned at 640/1280 but NEVER at 390; the label's family pinned at 1280 only; the figure's FIT contract never pinned at ANY viewport [the flush-left start, the in-bounds right, the no-scroll state]; the pin's own axes first measured byte-identical on both sides by the supplemental two-half census [headrow-arbit-v96.sh + headrow-clone-v96.sh via build-headrow-v96.py, the census JS byte-identical by the md5 line-block diff 519ef222]); the pin-sanity mutation font-bold -> font-bold max-sm:font-extrabold at net-worth-view.tsx:348 (by LINE NUMBER, AT-max-sm because the pin runs at 390 and the variant is INERT at >=640 — the v90 LESSON APPLIED; the line-scoping keeps the stat-tile VALUE's identical class string at line 372 untouched): ONLY the v96 pin red (30 green under the mutation), the failure diff reads as the figure fw axis ALONE ("700" -> "800") — cascade-free BY CONSTRUCTION (font-weight never changes line-height — the figure's lh stays 32px, the h 32 and the card-height arithmetic [421, the v63 F3 pin] unchanged; font-weight never affects color; max-sm: appears NOWHERE in src/), then restored (git diff src/ = 0; the standalone REBUILD; the post-restore full run 31/31 green); the F5 chain 140+100+61 = 301 chunk executions = 299 unique tests, zero flakes; the screenshots **15/16 BYTE-IDENTICAL + 1/16 the DATE class** (the 07-add-item-modal's day digits "19"->"20" rolled across the UTC midnight boundary — the budget-item-dialog's render-time default date todayIso() [line 83] the mechanism; the pixel-diff-v96.py arbitration localizing the delta to a 32x22px region at x1535 — exactly the two day digits, the v75 arbitration form [width <= 48, height <= 40, x > 1000]); the operational lessons: the standing-script timing artifact (the reference-side R-bug-4 read docSW 390/390 on the sleep-3 — the eval raced the client-side boot and measured the PRE-RENDER document; the 8s+2s settle re-read measured the true 464; the discipline: when a standing bug check reads CLEAN against its own documented-live history, re-measure with an explicit settle-wait before recording any state change), the flush-left figure perception class (the VLM flags a "clipped" negative currency figure when the text starts flush at the content-box left edge — the arbitration is the Range-walk textRect vs the padding-aware content box, NOT the element rect alone), the two-half form as the default (zero resource-exhaustion symptoms), and the derivation miss-report discipline (the derive script reports every correction's hit/miss — the one first-run MISS caught by the report itself and fixed before any probe executed).
"""

PROBE_SECTION = """
## The v96 cycle (executed 2026-10-20 — the v90-era MOBILE 390 twins' fifth re-run)

The queue's own paragraph above was EXECUTED this cycle. The probe series
derived from the v90 lineage by derive-v96-series.py (the PERSISTED
derivation script — the generic swaps [vlm90->vlm96, v90->v96, the
session names, the /tmp dir] followed by the exact-fragment history
corrections [the queue source "the v95 plan's own suggestion", the
oldest-remaining list, the FIFTH re-run bracket, FOURTH->FIFTH, the
census-axes provenance, the verdict note], every correction verified
applied — the DERIVATION MISS-REPORT DISCIPLINE: the script reports each
correction's hit/miss and the one first-run MISS [the lowercase 'the' in
the verdict-note fragment] was caught by the report itself and fixed
before any probe executed; zero residual old tokens across all four
files; bash -n + node --check clean). The new probes this cycle:
vlm-shots-v96.sh + clone-vlmshots-v96.sh + vlm-compare-v96.mjs +
arbit-v96.sh (the intermediate combined form, header-corrected) +
build-twohalf-v96.py (the two-half builder — the TWO census blocks
[NW_CENSUS 42 lines / DASH_CENSUS 87 lines] extracted once, embedded
byte-identically across the halves by the md5 line-block contract
[82cf8a43 / 85e4ec7e]) + ref-arbit-v96.sh + clone-arbit-v96.sh +
derive-standing-v96.py (the persisted standing derivation — the 90th
pair, version-bump-only verified by the normalize-back diff) +
ref-standing-v90.sh + standing-checks-v90.sh + figclip-clone-v96.sh (the
NEW clipped-figure flag's one-shot arbitration) + build-headrow-v96.py +
headrow-arbit-v96.sh + headrow-clone-v96.sh (the supplemental two-half
census for the v96 pin's own axes — the census JS byte-identical by the
md5 line-block diff [519ef222]; the doubled-brace spot grep clean, the
v95 template-brace lesson pre-applied) + pixel-diff-v96.py (the
07-add-item-modal DATE-class arbitration).

The verdicts: BOTH DIFFERENT (the pair's documented verdict class — the
same flag-set classes as the v84/v90 re-runs) with every flag
DOM-arbitrated: the stat-tile side-by-side-vs-stacked the v41
mobile-superset class (the census: the statGrid cols ref
"175.828px 175.844px" 2-col vs clone "294px" 1-col, the gap 16px
IDENTICAL, the tiles ref 176x84 vs clone 294x84 — the h 84
byte-identical); the clipped negative figure the NEW flag —
DOM-arbitrated as a VLM MISREAD by the figclip one-shot census (the
figure H2 at x=48 w=179 h=32, the textRect x=48 w=179 — the text starts
EXACTLY at the content-left edge [textLeftOfContent 0, zero overhang]
and ends 115px INSIDE the content-right; figureScrolls false; docSW 390
— the figure fully in-bounds on every axis, no clipping exists; THE
FLUSH-LEFT FIGURE PERCEPTION CLASS: the VLM flags a "clipped" negative
currency figure when the text starts flush at the content-box left edge
— the arbitration is the Range-walk textRect vs the padding-aware
content box, NOT the element rect alone); the subtitle wrap-point the
v62 width-delta class (the census: the chrome byte-identical [fs
16px/fw 400/rgb(107,114,128)/lh 24px, the P h 48, the block h 92], BOTH
sides 2 DOM lines; the reference's own 395px overflow shifts its wrap);
the FAB the platform-chrome class; the figures/counts/donut the
seed-data classes. The two-half census REPRODUCES the v90 values
EXACTLY — zero drift on every axis (the summary
card/statGrid/tiles/medallion/trendIcon families; the subtitle chrome;
the breakdown card's svg family [svgCount 7, the 16/14 alternation];
the children heights; the spendingCard finder reading the SAME fallback
string on BOTH sides — the heading is a div, not an h1-h4, on both
sites, the parity-correct rendering). NO NEW CLONE GAP.

The standing-script timing artifact (NEW this cycle): the
reference-side standing check's R-bug-4 (/networth overflow) read docSW
390/390 on the script's sleep-3 — the eval raced the reference's
client-side boot and measured the PRE-RENDER document; the 8s+2s settle
re-read measured the true 464. THE DISCIPLINE: when a standing bug
check reads CLEAN against its own documented-live history (the bug live
89 consecutive checks), re-measure with an explicit settle-wait before
recording any state change — a bug that has been live for 89
consecutive checks does not vanish on the 90th without a DOM-visible
cause.

The DATE-class screenshot arbitration (the v96 form): the cycle crosses
the UTC midnight boundary (the seed + the baseline shots Oct 19 22:41
UTC; the regeneration Oct 20 00:1x UTC) — the Add Item form's default
date (budget-item-dialog.tsx:83, todayIso(), computed at RENDER time)
rolls "2026-10-19" -> "2026-10-20" and the 07-add-item-modal shot
differs by exactly the two day digits: the pixel-diff-v96.py
arbitration localizes the delta to a 32x22px region at x1535 (the
v75 acceptance form: width <= 48, height <= 40, x > 1000 — the date
field in the dialog's form column right-of-center at the 2x DPR shot);
the other 15 shots byte-identical; the committed set updated with the
new 07 shot (the date-class delta documented, never a regression).

The v97 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the twins (the v91-era ITEMS pair [the INCOME + EXPENSES view
pair at desktop 1280x800], last re-shot v91 — now the oldest remaining
[v91 < v92 < v93 < v94 < v95 < v96]; the pair's SIXTH re-run
[v57 -> v64 -> v70 -> v79 -> v85 -> v91 -> v97] — verify the surface
names against vlm-shots-v91.sh's own header before the derivation),
(2) the axe-core watch at its next re-check point (only a 5.x wrapper
changes the calculus), (3) the deferred reference-write censuses
(unchanged — out of bounds under the v46 read-only rule).
"""

def main():
    # D4 — zero-balance_SKILL.md: the state line + the Session 131 row.
    t = open("zero-balance_SKILL.md").read()
    changed = 0
    if "108 unit tests / 298 e2e tests / 35 smoke steps" in t:
        t = t.replace("108 unit tests / 298 e2e tests / 35 smoke steps",
                      "108 unit tests / 299 e2e tests / 35 smoke steps", 1)
        changed += 1
    if "last_updated: 2026-10-19" in t:
        t = t.replace("last_updated: 2026-10-19", "last_updated: 2026-10-20", 1)
        changed += 1
    anchor = "| 2026-10-19 | Session 130 — parity iteration v95"
    if anchor in t and "Session 131 — parity iteration v96" not in t:
        idx = t.index(anchor)
        line_end = t.index("\n", idx) + 1
        t = t[:line_end] + SKILL_ROW + t[line_end:]
        changed += 1
    open("zero-balance_SKILL.md", "w").write(t)
    print(f"D4 zero-balance_SKILL.md: {changed} edits applied")

    # D5 — PAD: the v1.1.53 revision block before v1.1.52.
    t = open("Project_Architecture_Document.md").read()
    anchor = "#### Revision Block — v1.1.52 (Tracked Changes)"
    if anchor in t and "Revision Block — v1.1.53" not in t:
        t = t.replace(anchor, PAD_BLOCK + anchor, 1)
        open("Project_Architecture_Document.md", "w").write(t)
        print("D5 PAD: v1.1.53 revision block inserted")
    else:
        print("D5 PAD: already present")

    # D6 — the probe README: the v96 section + the v97 queue appended.
    t = open("scripts/parity-probes/README.md").read()
    if "## The v96 cycle (executed" not in t:
        if not t.endswith("\n"):
            t += "\n"
        t += PROBE_SECTION
        open("scripts/parity-probes/README.md", "w").write(t)
        print("D6 probe README: v96 section + v97 queue appended")
    else:
        print("D6 probe README: already present")

if __name__ == "__main__":
    main()
