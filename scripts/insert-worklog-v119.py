#!/usr/bin/env python3
"""Insert the Session 154 (v119) entry into worklog.md — newest-first,
inserted before the Session 153 entry. Also updates the header plan-list
line (through v118/Session 153 -> v119/Session 154). Idempotent (the
marker check fails loudly)."""
import sys

ENTRY = """## Session 154 — Parity iteration v119: the re-run cycle's next-oldest candidate (the v113-era DASHBOARD pair's NINTH re-run) + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — the standing step's tenth cycle) + the 113th standing checks + the /dashboard page-header-row census pin at 1280 (PIN-ONLY — the byte-identical desktop twin of the v114 390 pin) (2026-10-25)

**The cycle** (`docs/remediation-plan-v119.md` — the plan validated against the codebase before execution; the delivery record: `docs/session_289.md`): the re-run cadence's next-oldest candidate — the v113-era DASHBOARD pair (the DASHBOARD at desktop 1280x800 FULL-PAGE, both v61 target surfaces below the fold on the same view: (1) the BUDGET GUIDELINES card + (2) the QUICK-ACTION card row, last re-shot v113 — now the oldest remaining [v113 < v114 < v115 < v116 < v117 < v118]; the pair's NINTH re-run bracket [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119]; the FORTY-SECOND consecutive queue/ledger agreement — the surface names verified against vlm-shots-v113.sh's own header BEFORE the derivation, with the v113 header's own SEVENTH-vs-bracket off-by-one identified BEFORE the derivation and the NINTH ordinal fixed IN it per the consistent v112-lineage convention).

- **The verdict IDENTICAL — the SEVENTH consecutive IDENTICAL verdict for this pair [v83 → v89 → v95 → v101 → v107 → v113 → v119]** (run TWICE with the full log captured) — the only flags the documented classes: the nav highlight the v56 SUPERSET delta (the clone highlights its ACTIVE nav item; the reference's own shortcoming); the avatar letters the USER-IDENTITY data class; the figures the SEED-DATA classes (each site's own data). No FAB flag raised this cycle (the v103 standing class — no disproof needed when no flag is raised).
- **The both-sides census** (ARBIT_G 61 lines md5 b500dd29 + ARBIT_Q 58 lines md5 da04e995 + ARBIT_X 25 lines md5 7a381755 — the v101/v107/v113 census blocks VERBATIM, byte-identical across the halves, verified by marker-based extraction) **compared AXIS-BY-AXIS by the persisted compare-v119-census.py — 154 axes: 144 identical + 10 documented-class deltas, ZERO new** (Gcard.shadow the v66 INVISIBLE shadow-lead class; Qcards[i].label.color/.fw the v61 label-wrapper lesson [the clone's LEAF span byte-identical: 16px/500/rgb(26,58,46)]; Qgrid.mt + XgridMt the v77 mechanism class [the rendered geometry byte-identical]; XgridCls the site-source class) — reproducing the v113 census values EXACTLY (the same 154/144/10 split), zero drift on every axis, the rendered geometry HARD-ASSERTED byte-identical (cardBottom 1122 / gridTop 1462 / gap 340 / gridParentMt 0px on BOTH sides).
- **THE PIN — the /dashboard PAGE-HEADER-ROW census at 1280 (the never-pinned family, PIN-ONLY — the cleanest form)**: the pin-candidate survey found the pair's own below-the-fold surfaces among the most-pinned in the codebase (the guidelines card: v61 F2 + v77 F4 + v89 F4 + v101 F4 + v113 F4; the quick-action row: v61 F3 + v45 F3b + v83 F4 + v89 F4 + v95 F4 + v107 F4 — every PART G/Q/X census axis family pinned), so the candidate went to the SAME VIEW's never-pinned family per the v118 precedent: the dashboard page-header row — pinned ONLY at 390 before this (the v114 F4 pin + the v62 F2 pin) and at 1280 only POSITION-pinned (the v40 F1 Tab-order band [x 1121, w 127, h 36]). The one-shot both-sides census (drow-arbit-v119.sh — the census JS defined ONCE and eval'd on BOTH sides): **the family BYTE-IDENTICAL on EVERY axis — not even a mechanism axis diverged** (the reference's and the clone's census JSON lines the IDENTICAL string): the row {flex/row/center/space-between/gap 16px/mb 32px/h 72/w 960}, the h1 {36px md:text-4xl/700/lh 40px/mb 8px}, the subtitle {16px/400/lh 24px}, the block {h 72/w 498}, the addBtn {left 1121/h 36/w 127/pad 8px 16px/radius 6px/14px/500/white/the 135deg forest→lime gradient/icon 16×16}, the junction {hGap 335 — the justify-between spread}, the nextGap {32 — the mb-8 rendered}, the docSW 1280 — the Add Item band CROSS-VALIDATED against the v40 F1 pin's own [1121, 127, 36] exactly. **THE CLASSIFICATION — PIN-ONLY (the cleanest form)**: no construct question even arises (unlike the v118 wrapper find) — the family byte-identical on every axis INCLUDING the positions; the pin locks the never-pinned 1280 family's computed chrome as the desktop twin of the v114 390 pin.
- **The +1 pin** (tests/e2e/dashboard.spec.ts, appended by the persisted append-pin-v119.py): the page-header row census at 1280 — the row/h1/subtitle/block/addBtn/junction/nextGap family + the docSW guard; the finders STRUCTURAL (the v72 class). **The PIN-ONLY form** (the v116/v118 precedent): the standalone GREEN run (no red phase — the measured values already hold) + the 48/48 dashboard surface regression + the full-suite ship chain.
- **The derivation**: the series from the v113 lineage (derive-v119-series.py — 8/8 corrections applied on the second run [the first run's single MISS the arbit header fragment written from the line-START where the file carries it MID-LINE]; line counts preserved [58/43/46/259]) + the two-half builder (derive-build-twohalf-v119.py → build-twohalf-v119.py — the lesson-range bump v92..v112→v92..v118 in the BARE-RANGE form [the v113 builder's TWOHALF_NOTE carries the range SPLIT ACROSS TWO LINES; the v118-template phrase-form swap missed it], the lineage-note fixup "build-twohalf-v107.py"→"build-twohalf-v113.py" LAST; ZERO builder repairs; the md5 contracts b500dd29/da04e995/7a381755) + the 113th standing pair (derive-standing-v119.py, three token families, normalize-back clean).
- **The baseline chain FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace, ZERO flakes** (the RESET class — the v118 environment did not persist; the repo re-cloned from main @ ec146b5; the v108 FRESH-CLONE lesson applied end-to-end: npm ci in the foreground after the silent BACKGROUND death [the v114 lesson's exact symptom] with the zod extraction verified 840/840 + src/v4 present BEFORE any gate, BOTH v1243 playwright binaries verified DIRECTLY [the v1243 layout the chrome-linux64 + chrome-headless-shell-linux64 pair], .env + db/ at the repo root + db:push + db:seed [7 items / 3 assets / 2 liabilities]; **the fresh-workspace discovery: the sandbox workspace-root .env carries an ABSOLUTE DATABASE_URL that the Prisma CLI prefers over the repo's — the EXPLICIT-env-prefix fix on every Prisma CLI call [the app itself unaffected: Next.js loads the repo .env only + db-path.ts anchors the relative URL]**; the seedcheck exact [the env -u DATABASE_URL discipline, the canonical db-seedcheck-v68.cjs]; lint; typecheck; 108 unit; build [robots + sitemap prerendered]; 321 e2e [85+80+77+82 = 324 executions, every chunk green on its FIRST correct run — the a11y-filename grep lesson re-hit: a `[a-z-]+` pattern truncated a11y.spec.ts to y.spec.ts, the first chunk-4 run 60 of 82, the re-run green]; 35/35 smoke; the post-push commits audited session-log-only [d48fabd + ec146b5 — session docs only]).
- **The ship chain**: 322 e2e zero flakes (86+80+77+82 = 325 executions = 322 unique); 35/35 smoke; **the screenshots 16/16 byte-IDENTICAL (the same-day-seed law — the seed and the capture ran the same day)**; the dev evidence re-captured + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the menu open with all 5 links + the brand; the sheet closed post-nav; the dashboard clean — the byte-compare 4/4 identical; the dev-shots scripts derived v118→v119 with the version-swap-only verification).
- **The 113th standing checks ALL GREEN** — the mobile menu VERIFIED WORKING the 113th consecutive time; the reference's four bugs all live; the data census clean on the FIRST reads (no render-race hit this cycle); the SEO pair live both sides.
- The docs aligned D1–D7 (AGENTS the v119 paragraph; CLAUDE 322 + the v119 clause; README counts + the v119 plan row; the SKILL Session 154 row + the state line; PAD v1.1.76; the probe README's v119 section + the v120 queue [the v114-era MOBILE TWINS pair — BOTH mobile 390×844 full-page twins, the bracket [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120]]; this Session 154 entry); `docs/session_289.md` saved. `.env.example` verified matching the codebase (untouched this cycle).

---

"""

path = "worklog.md"
t = open(path, encoding="utf-8").read()

if "## Session 154 — Parity iteration v119" in t:
    print("ALREADY APPLIED: the Session 154 entry")
    sys.exit(0)

# the header plan-list line: v118/Session 153 -> v119/Session 154
old_hdr = "`docs/remediation-plan-v118.md` (the v118 cycle — Session 153)."
new_hdr = "`docs/remediation-plan-v119.md` (the v119 cycle — Session 154)."
if old_hdr in t:
    t = t.replace(old_hdr, new_hdr, 1)
    print("aligned worklog.md header (the plan list -> v119/Session 154)")
elif new_hdr in t:
    print("header already v119 — skipped")
else:
    print("WARN: the header plan-list line not found in either state — inspect")

anchor = "## Session 153 — Parity iteration v118"
if t.count(anchor) != 1:
    print(f"AMBIGUOUS/MISS anchor ({t.count(anchor)} hits)")
    sys.exit(1)

t = t.replace(anchor, ENTRY + anchor, 1)
open(path, "w", encoding="utf-8").write(t)
print("aligned worklog.md (the Session 154 entry)")
