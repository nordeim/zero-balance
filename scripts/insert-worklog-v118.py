#!/usr/bin/env python3
"""Insert the Session 153 (v118) entry into worklog.md — newest-first,
inserted before the Session 152 entry. Also updates the header plan-list
line (through v117/Session 152 -> v118/Session 153). Idempotent (the
marker check fails loudly)."""
import sys

ENTRY = """## Session 153 — Parity iteration v118: the re-run cycle's next-oldest candidate (the v112-era NETWORTH + drill-down-DASHBOARD pair's ninth re-run) + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — the standing step's ninth cycle) + the 112th standing checks + the /networth page-header-row census pin at 1280 (PIN-ONLY — the wrapper-mechanism construct class) (2026-10-25)

**The cycle** (`docs/remediation-plan-v118.md` — the plan validated against the codebase before execution; the delivery record: `docs/session_286.md`): the re-run cadence's next-oldest candidate — the v112-era NETWORTH + drill-down-DASHBOARD pair (the desktop 1280x800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's drill-down EXPANDED state, last re-shot v112 — now the oldest remaining [v112 < v113 < v114 < v115 < v116 < v117]; the pair's NINTH re-run bracket [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118]; the FORTY-FIRST consecutive queue/ledger agreement — the surface names verified against vlm-shots-v112.sh's own header BEFORE the derivation).

- **The verdicts NETWORTH DIFFERENT + drill-down DIFFERENT — every flag DOM-arbitrated to a documented class**: the FAB flags (raised on BOTH pairs) DISPROVEN live (the one-shot base44-fab-arbit-v118.sh on the flagged /networth surface at 1280: `fabCount:0` + `bodyHasBase44:false` on BOTH sides — the platform-iframe chrome class, the v97/v103/v108/v109/v115/v117 standing disproof form re-confirmed); the avatar letters the USER-IDENTITY data class; the nav-highlight flag the v56 SUPERSET delta + perception (the census: navHighlight bg `rgba(0,0,0,0)` transparent on BOTH sides — no green background; the color/fw asymmetry the documented superset); the hero progress % the PCT data class (fillW 173-vs-357); the donut % labels the EACH-SITE'S-DATA + perception class (count 4 / labelFs 16px / sectors 3 byte-identical — the reference DOES render its labels); the stat counts / the extra "Freelance" category the SEED-DATA class; **the "Total Expense (singular) vs Total Expenses (plural)" flag DISPROVEN live — the reference reads "Total Expenses" PLURAL on ALL SIX instances (the 3 tab-button SPANs + the 3 stat-card H3s), the full family byte-identical to the clone's down to every chrome axis (statlabel-explore-v118.sh + statlabel-explore-clone-v118.sh) — the VLM TEXT-MISREAD class**.
- **The both-sides census** (ARBIT_A 90 lines md5 45b9a439 + ARBIT_B 111 lines md5 8ed66a88 — byte-identical across the halves, verified by marker-based extraction) **compared AXIS-BY-AXIS by the persisted compare-v118-census.py — 73 axes: 67 identical + 6 documented-class deltas, ZERO new** (navHighlight.color/fw the v56 superset delta; avatarLetter the user-identity data class; progress.fillW the pct data class; donutLabels.texts the each-site's-data class; labelBlock.w the v82 DATA-CONDITIONAL width class [the 48px figure's text length]) — reproducing the v106/v112 census values EXACTLY, zero drift on every axis. NOTE: the census lines are DOUBLE-ESCAPED in the halves' logs (agent-browser prints the JSON object itself serialized as a quoted string); the recovery a DOUBLE json.loads (the compare-v118-census.py parser form).
- **THE FIND — THE WRAPPER-MECHANISM CONSTRUCT CLASS (PIN-ONLY, zero production-code changes)**: the pin-candidate survey targeted the /networth PAGE-HEADER ROW at 1280 (the element family every 1280 networth census walked past — pinned ONLY at 390 before this [the v69 F3 pin, clone-measured]; the v14 G3 test the chip's existence + gradient + geometry + the h1 x-positions only). The one-shot both-sides census (nwheader-arbit-v118.sh) measured the family BYTE-IDENTICAL on every VISUAL axis — the row {flex/center/gap 12px/h 60}, the chip {48×48/radius 12px/the 135deg forest→lime gradient/the 24×24 svg}, the h1 {30px/700/36px/rgb(26,58,46)}, the subtitle {16px/400/24px/rgb(107,114,128)}, the block {h 60/w 250}, the row→card gap 32, the card w 960 — ONE mechanism axis diverging: the row's margin-bottom (the reference 0px vs the clone 32px). The drill-down (nwheader-mechanism-v118.sh + nwheader-wrapper-v118.sh): **the reference wraps its header row in a SINGLE-CHILD responsive wrapper** (`flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-8` — the wrapper carries the mb-8; childCount 1, nothing on the right) while the clone puts the mb-8 directly on the row; the pixel arithmetic IDENTICAL both sides (the row 32→92, the card 124, the gap 32), the 390 rhythm matching too; the clone's OWN dashboard header uses the reference's wrapper form verbatim (dashboard-view.tsx:927) — the /networth header the v14-era simplification. **THE CLASSIFICATION — the CONSTRUCT class per the v7 accepted-construct convention** (constructs that paint nothing are not parity axes; the DOM-tree shape is not the contract — the v72 structural-finder principle; the production-code changes reserved for REAL visual deltas). **THE RULE**: a structural-layer difference with zero computed-style consequence on every visible axis is a CONSTRUCT class, not a parity gap — measure the MECHANISM + the position arithmetic before flagging; pin the VISUAL contract, not the mechanism axis.
- **The +1 pin** (tests/e2e/networth.spec.ts, appended by the persisted append-pin-v118.py): the /networth page-header row census at 1280 — the row {flex/center/gap 12px/mb 32px} + the chip {48×48/radius 12px/the gradient} + the h1 {30px/700/lh 36px} + the subtitle {16px/400/lh 24px} + the block {h 60/w 250 — the TEXT BLOCK governs the row height, the v65/v69 lesson} + the row→card gap 32 + the card w 960 + the docSW 1280 guard; the finders STRUCTURAL (the v72 class). **The PIN-ONLY form** (the v116 precedent): the standalone GREEN run (no red phase — the measured values already hold) + the 35/35 networth surface regression + the full-suite ship chain.
- **The derivation**: the series from the v112 lineage (derive-v118-series.py — 4/4 corrections applied on the FIRST run; line counts preserved [84/71/65/328]) + the two-half builder (derive-build-twohalf-v118.py → build-twohalf-v118.py, the lesson-range bump v92..v111→v92..v117, the lineage-note fixup LAST; ZERO builder repairs needed; the md5 contracts 45b9a439/8ed66a88) + the 112th standing pair (derive-standing-v118.py, three token families, normalize-back clean).
- **The baseline chain FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace, ZERO flakes** (the RESET class — the v117 environment did not persist; the repo re-cloned from main @ dba644d; the v108 FRESH-CLONE lesson applied end-to-end: npm ci in the foreground with the zod extraction verified 840/840 + src/v4 present BEFORE any gate, BOTH v1243 playwright binaries verified DIRECTLY, .env + db/ at the repo root + db:push + db:seed [7 items / 3 assets / 2 liabilities]; the seedcheck exact [the env -u DATABASE_URL discipline, the canonical db-seedcheck-v68.cjs]; lint; typecheck; 108 unit; build [robots + sitemap prerendered]; 320 e2e [84+80+77+82 = 323 executions, every chunk green on its FIRST run]; 35/35 smoke; the post-push commit audited session-log-only [dba644d adds docs/session_285.md]).
- **The ship chain**: 321 e2e zero flakes (85+80+77+82 = 324 executions = 321 unique); 35/35 smoke; **the screenshots 16/16 byte-IDENTICAL (the same-day-seed law — the seed and the capture ran the same day)**; the dev evidence re-captured + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the menu open with all 5 links + the brand; the sheet closed post-nav; the dashboard clean — the byte-compare 4/4 identical; the dev-shots scripts derived v117→v118 with the version-swap-only verification).
- **The 112th standing checks ALL GREEN** — the mobile menu VERIFIED WORKING the 112th consecutive time; the reference's four bugs all live; the data census clean on the FIRST reads (no render-race hit this cycle); the SEO pair live both sides.
- The docs aligned D1–D7 (AGENTS the v118 paragraph; CLAUDE 321 + the v118 clause; README counts + the v118 plan row; the SKILL Session 153 row + the state line; PAD v1.1.75; the probe README's v118 section + THE WRAPPER-MECHANISM CONSTRUCT CLASS lesson + the v119 queue [the v113-era DASHBOARD pair — the Budget Guidelines + Quick-Action surfaces, the bracket [v61 → … → v113 → v119], with the v113 header's own SEVENTH-vs-bracket off-by-one flagged for the v119 verification]; this Session 153 entry); `docs/session_286.md` saved. `.env.example` verified matching the codebase (untouched this cycle).

---

"""

path = "worklog.md"
t = open(path, encoding="utf-8").read()

if "## Session 153 — Parity iteration v118" in t:
    print("ALREADY APPLIED: the Session 153 entry")
    sys.exit(0)

# the header plan-list line: v117/Session 152 -> v118/Session 153
old_hdr = "`docs/remediation-plan-v117.md` (the v117 cycle — Session 152)."
new_hdr = "`docs/remediation-plan-v118.md` (the v118 cycle — Session 153)."
if old_hdr in t:
    t = t.replace(old_hdr, new_hdr, 1)
    print("aligned worklog.md header (the plan list -> v118/Session 153)")
elif new_hdr in t:
    print("header already v118 — skipped")
else:
    print("WARN: the header plan-list line not found in either state — inspect")

anchor = "## Session 152 — Parity iteration v117"
if t.count(anchor) != 1:
    print(f"AMBIGUOUS/MISS anchor ({t.count(anchor)} hits)")
    sys.exit(1)

t = t.replace(anchor, ENTRY + anchor, 1)
open(path, "w", encoding="utf-8").write(t)
print("aligned worklog.md (the Session 153 entry)")
