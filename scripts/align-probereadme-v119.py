#!/usr/bin/env python3
"""D6 docs alignment for the v119 cycle — the probe README's v119 section
(inserted newest-first, before the v118 section) carrying the v120 queue.
Insert-after WITH the idempotency guard (the v113 lesson)."""
import sys

README = "scripts/parity-probes/README.md"
t = open(README, encoding="utf-8").read()

SECTION = """## The v119 cycle (the v113-era DASHBOARD pair's NINTH re-run — Session 154)

The re-run cadence's next-oldest candidate: the v113-era DASHBOARD pair
(the DASHBOARD at desktop 1280x800 FULL-PAGE, both v61 target surfaces
below the fold on the same view: (1) the BUDGET GUIDELINES card (the
tinted, bordered 50/30/20 rows) and (2) the QUICK-ACTION card row (the
three Add Income / Add Savings / Add Expense card buttons), last re-shot
v113 — now the oldest remaining [v113 < v114 < v115 < v116 < v117 <
v118]; the pair's NINTH re-run bracket [v61 -> v68 -> v77 -> v83 -> v89
-> v95 -> v101 -> v107 -> v113 -> v119]; the FORTY-SECOND consecutive
queue/ledger agreement — the surface names verified against
vlm-shots-v113.sh's own header BEFORE the derivation, with the v113
header's own SEVENTH-vs-bracket off-by-one identified BEFORE the
derivation and the NINTH ordinal fixed IN it [the consistent v112-lineage
convention: EIGHTH for 9 entries, NINTH for 10 — v61 the original in
every bracket; the BRACKET is the authority per the queue-prose
verification lesson]). **A PIN-ONLY cycle for src/ — zero
production-code changes** + one e2e pin; the cycle's standing items: the
axe watch (NO DRIFT — 4.14.0 holds, only a canary sha prerelease beyond,
the v68 dedupe verified), the npm-audit watch at its tenth re-check (0
vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]), the
113th standing checks (ALL GREEN — the mobile menu the 113th consecutive
green; the reference's four bugs all live; the data census clean on the
FIRST reads, no render-race hit this cycle).

**F0 baseline FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace**
(the RESET class — the v118 environment did not persist; the repo
re-cloned from main @ ec146b5). The v108 FRESH-CLONE lesson applied
END-TO-END: npm ci (354 entries; the first BACKGROUND attempt died
SILENTLY with an empty log — the v114 silent-death lesson's exact
symptom — the run redone in the FOREGROUND) with the zod extraction
verified INTACT [840/840 files by the total-file count, the src/v4
subdirectory present, one package-lock zod entry — the v68 dedupe];
BOTH v1243 playwright binaries verified DIRECTLY (the fresh cache held
only the OLD chromium-1200 pair; the v1243 layout the
chrome-linux64/chrome + chrome-headless-shell-linux64/chrome-headless-shell
pair, INSTALLATION_COMPLETE markers + direct binary reads). **The
fresh-workspace discovery**: the sandbox's workspace root carries its
own /home/z/my-project/.env with an ABSOLUTE
DATABASE_URL=file:/home/z/my-project/db/custom.db — the Prisma CLI
walks PARENT directories for .env files and the parent's absolute URL
WON over the repo's file:../db/custom.db (the first db push wrote
OUTSIDE the repo). THE FIX (the discipline for every fresh workspace):
the EXPLICIT env prefix on every Prisma CLI call
(DATABASE_URL="file:../db/custom.db" npx prisma db push / ... npm run
db:seed) — the explicit shell env beats any .env file; the app itself
unaffected (Next.js loads the repo .env only + db-path.ts anchors the
relative URL against the repo root regardless of CWD). The db verified
at <repo>/db/custom.db + the seed (7 items / 3 assets / 2 liabilities);
the seedcheck exact (7/1850/2235/0/3/2). The gates: lint · typecheck ·
108/108 unit · build (robots + sitemap prerendered) · **321 e2e ZERO
FLAKES** (85+80+77+82 = 324 executions = 321 unique) · 35/35 smoke.
NOTE the a11y-filename grep lesson re-hit: a `[a-z-]+\\.spec\\.ts` grep
pattern truncated "a11y.spec.ts" to "y.spec.ts" (the digit class
missing) — the first chunk-4 run executed 60 of 82 before the filename
check caught it; the re-run with the REAL filename green (the v111
lesson: verify the filename list against `--list` before running). The
post-push commits since the v118 parity push (d14d56f) audited
session-log-only [d48fabd adds docs/session_287.md + ec146b5 adds
docs/session_288.md — ZERO src/, tests/, prisma/ or lockfile deltas].

**F3**: the series derived from the v113 lineage (derive-v119-series.py
— the generic swaps + the EIGHT exact-fragment history corrections
[the era re-pointed v107-era -> v113-era, last-re-shot v107 -> v113,
the oldest-remaining list re-pointed, the ordinal off-by-one FIXED
SEVENTH/EIGHTH -> NINTH + the bracket extension -> v113 -> v119, the
agreement THIRTY-SIXTH -> FORTY-SECOND, the re-proves window
v101-v107 -> v101-v113, the verdict reference "The v107" -> "The v113",
the drift-re-check "since v107" -> "since v113", and the compare PAIR
banner], 8/8 applied on the second run — the first run's single MISS
the arbit header fragment written from the line-START where the file
carries it MID-LINE after "# 1280x800 (the..."; line counts preserved
[58/43/46/259]). The census BUILT two-half from the start
(build-twohalf-v119.py via derive-build-twohalf-v119.py with the
swap-order rule [generic swap FIRST, the lesson-range bump
v92..v112 -> v92..v118 — the BARE-RANGE form: the v113 builder's
TWOHALF_NOTE carries the range SPLIT ACROSS TWO LINES and the
v118-template phrase-form swap missed it, the bare-range swap catches
both occurrences; the lineage-note fixup "build-twohalf-v107.py" ->
"build-twohalf-v113.py" LAST]; the THREE census JS blocks [ARBIT_G 61
lines + ARBIT_Q 58 lines + ARBIT_X 25 lines] byte-identical across the
halves — the md5 line-block contracts [b500dd29 / da04e995 / 7a381755 —
the v101/v107/v113 census blocks VERBATIM, verified by marker-based
extraction across the source + both halves]). Both halves executed
cleanly (the reaping budget between halves; the parked pointer at
(5,5); read-only — the v46 rule holds; login on the first attempt both
sides).

**The verdict: IDENTICAL — the SEVENTH consecutive IDENTICAL verdict
for this pair [v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119]** —
run TWICE with the full log captured; the only flags the documented
classes: the nav highlight the v56 SUPERSET delta (the clone highlights
its ACTIVE nav item; the reference's own shortcoming); the avatar
letters the USER-IDENTITY data class; the figures the SEED-DATA classes
(each site's own data). No FAB flag raised this cycle (the v103
standing class: either form without surprise — no disproof needed when
no flag is raised). The both-sides census compared AXIS-BY-AXIS by the
persisted compare-v119-census.py (**154 axes: 144 identical + 10
documented-class deltas, ZERO new** — Gcard.shadow the v66 INVISIBLE
shadow-lead class; Qcards[i].label.color/.fw the v61 label-wrapper
lesson [the census finder catches the clone's WRAPPER 400/rgb(10,10,10)
while the ref's is the leaf — the clone's LEAF span byte-identical
16px/500/rgb(26,58,46), pinned green by the v61 F3 pin + the v107 F4
label-leaf census]; Qgrid.mt + XgridMt the v77 mechanism class
[explicit mt-8 on the clone vs structural spacing on the ref]; XgridCls
the site-source class) — reproducing the v113 census values EXACTLY
(the same 154/144/10 split), zero drift on every axis, the rendered
geometry HARD-ASSERTED byte-identical (cardBottom 1122 / gridTop 1462 /
gap 340 / gridParentMt 0px on BOTH sides).

**F4 [PIN] — the /dashboard PAGE-HEADER-ROW census at 1280 (the
never-pinned family, PIN-ONLY — the cleanest form)**: the pin-candidate
survey found the pair's own below-the-fold surfaces among the
most-pinned in the codebase (the guidelines card: v61 F2 + v77 F4 + v89
F4 + v101 F4 + v113 F4; the quick-action row: v61 F3 + v45 F3b + v83 F4
+ v89 F4 + v95 F4 + v107 F4 — every PART G/Q/X census axis family
pinned), so the candidate went to the SAME VIEW's never-pinned family
per the v118 precedent: **the DASHBOARD PAGE-HEADER ROW at 1280** — the
family pinned ONLY at 390 before this (the v114 F4 pin: the row's flex
chrome + the block->button junction + the Add Item button's box chrome;
the v62 F2 pin: the subtitle block's interior) and at 1280 only
POSITION-pinned (the v40 F1 Tab-order census: the Add Item button's
band [x 1121, w 127, h 36]; the session-5 gradient; the v35 S2 focus
shadow; the G3 Plus-icon geometry). The one-shot both-sides census
(drow-arbit-v119.sh — the census JS defined ONCE and eval'd on BOTH
sides, byte-identical by construction): **the family BYTE-IDENTICAL on
EVERY axis — not even a mechanism axis diverged** (the reference's and
the clone's census JSON lines the IDENTICAL string): the row {display
flex / flexDirection row / align center / justify space-between / gap
16px / mb 32px / h 72 / w 960}, the h1 {fs 36px — the md:text-4xl tier,
the 390 twin's text-3xl 30px the OTHER breakpoint / fw 700 / lh 40px /
color rgb(26,58,46) / h 40 / mb 8px}, the subtitle {fs 16px / fw 400 /
lh 24px / color rgb(107,114,128) / h 24}, the block {h 72 / w 498 /
right 786}, the addBtn {left 1121 / top 50 / h 36 / w 127 / pad 8px
16px / radius 6px / fs 14px / fw 500 / color white / bg the 135deg
forest->lime gradient / icon 16x16}, the junction {hGap 335 — the
justify-between SPREAD, the row's gap-4 16px the computed minimum}, the
nextGap {gap 32 — the mb-8 rendered, the next sibling the
lg:grid-cols-3 stat grid}, the docSW 1280 — the Add Item button's band
CROSS-VALIDATED against the v40 F1 pin's own [1121, 127, 36] exactly.

**THE CLASSIFICATION — PIN-ONLY (the cleanest form)**: no construct
question even arises this cycle (unlike the v118 wrapper find) — the
family is byte-identical on every axis INCLUDING the positions. The pin
locks the never-pinned 1280 family's computed chrome as the desktop
twin of the v114 390 pin.

The pin (tests/e2e/dashboard.spec.ts, the v119 describe block —
appended by the persisted append-pin-v119.py): the /dashboard
page-header row census at 1280x800 — the row {display flex /
flexDirection row / align center / justify space-between / gap 16px /
mb 32px} + the h1 {fs 36px / fw 700 / lh 40px / mb 8px — the
md:text-4xl tier} + the subtitle {fs 16px / fw 400 / lh 24px} + the
block {h 72 / w 498 — the TEXT BLOCK governs the row height, the
v65/v69/v118 lesson} + the addBtn BOX chrome {h 36 / w 127 / pad 8px
16px / radius 6px / fs 14px / fw 500 / color white / bg the 135deg
gradient / icon 16x16 — the v114 390 pin's desktop twin, the band
cross-validating the v40 F1 pin} + the horizontal junction (the block's
right -> the button's left, the justify-between spread — data-stable
via the fixed strings) + the row->stat-grid rhythm (the nextGap 32) +
the docSW 1280 guard; the finders STRUCTURAL (the h1 by its childless
exact text "Budget Dashboard"; the block as its parent; the row as the
block's parent; the button by its /Add Item/ text within the row; the
next sibling as the row's nextElementSibling). The PIN-ONLY form (the
v116/v118 precedent): the pin written asserting the measured clone
values -> the standalone GREEN run (no red phase — nothing to fix, the
values already hold) -> the 48/48 dashboard surface regression -> the
full-suite ship chain.

**F5 the ship chain**: lint · typecheck · 108 unit · 0 vulnerabilities ·
**322 e2e zero flakes** (86+80+77+82 = 325 executions = 322 unique) ·
35/35 smoke. **The screenshots 16/16 byte-IDENTICAL (the same-day-seed
law — the seed and the capture ran the same day, the relative dates
matching)**; the dev evidence 4/4 byte-identical + VLM-verified (the
menu proof: /income, docSW 390, navLandmark true; the menu open with
all 5 links + the brand; the sheet closed post-nav; the dashboard
clean — the dev-shots scripts derived v118->v119 with the
version-swap-only verification).

The v120 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v113-era DASHBOARD pair (the v114-era MOBILE TWINS pair —
BOTH mobile 390x844 full-page twins: (1) the /NETWORTH view (the
v63-era pair's surface) and (2) the DASHBOARD (the v62-era mobile
twin's surface), last re-shot v114 — now the oldest remaining [v114 <
v115 < v116 < v117 < v118 < v119]; the pair's next re-run bracket
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 ->
v120] to be verified against vlm-shots-v114.sh's own header before the
derivation — the v114 header's own EIGHTH ordinal is consistent with
its 9-entry bracket [v62/v63 the original pair], so v120 = the NINTH
re-run by the same convention), (2) the axe-core watch at its next
re-check point (only a 5.x wrapper changes the calculus), (3) the
npm-audit watch at its re-check point (only a new advisory in the
next/zod ranges changes the calculus), (4) the deferred reference-write
censuses (unchanged — out of bounds under the v46 read-only rule).

"""

if "## The v119 cycle" in t:
    print("ALREADY APPLIED: the v119 section — skipped")
    sys.exit(0)
anchor = "## The v118 cycle (the v112-era NETWORTH + drill-down-DASHBOARD pair's NINTH re-run — Session 153)"
if t.count(anchor) != 1:
    print(f"AMBIGUOUS/MISS anchor ({t.count(anchor)} hits)")
    sys.exit(1)
t = t.replace(anchor, SECTION + anchor, 1)
open(README, "w", encoding="utf-8").write(t)
print("aligned scripts/parity-probes/README.md (the v119 section + the v120 queue)")
