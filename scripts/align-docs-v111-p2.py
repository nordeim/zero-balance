#!/usr/bin/env python3
"""D6 + D7b alignment for the v111 cycle.

D6  probe README — the v111 cycle section (the record + THE PROVISIONING
    LESSON + the v112 queue) appended after the v111 queue
D7b worklog.md   — the ledger tail v110→v111 + the Session 146 entry
                    inserted above Session 145
"""
import sys

ok = True

# ---------------- D6: the probe README ----------------
t = open("scripts/parity-probes/README.md", encoding="utf-8").read()
tail_anchor = "(4) the deferred reference-write censuses\n(unchanged — out of bounds under the v46 read-only rule)."
if tail_anchor not in t:
    print("MISS: probe README tail anchor")
    ok = False
else:
    v111_section = """

## The v111 cycle (the v105-era LOGIN + CALCULATOR pair's EIGHTH re-run — Session 146)

The re-run cadence's next-oldest candidate: the v105-era LOGIN +
CALCULATOR pair (the LOGIN view + the CALCULATOR dialog at desktop
1280x800, last re-shot v105 — now the oldest remaining [v105 < v106 <
v107 < v108 < v109 < v110]; the pair's EIGHTH re-run bracket [v59 -> v66
-> v75 -> v81 -> v87 -> v93 -> v99 -> v105 -> v111]; the THIRTY-FOURTH
consecutive queue/ledger agreement — the surface names verified against
vlm-shots-v105.sh's own header before the derivation). PIN-ONLY for
src/; the cycle's standing items: the axe watch (NO DRIFT — 4.14.0
holds, the v68 dedupe verified), the npm-audit watch at its second
re-check (0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod
4.6.7]), the 105th standing checks (ALL GREEN — the mobile menu the
105th consecutive green; the reference's four bugs all live; the census
clean on the first read). The verdicts: CALCULATOR DIFFERENT (every
flag DOM-arbitrated to a documented class — the "Will update category
total" note the SEED-DATA class [ref hasWillUpdateSpan false: its own
Rent $25.00 equals its calculated total]; the hover-action row the
RESTING-STATE parity class [actionsAtRest {opacity 0, btnCount 2}
identical both sides]; the row-height flag their consequence) + LOGIN
IDENTICAL (the v105 precedent — the verdict-variation form). The
two-half census (CALC_CENSUS_JS 61 lines md5 e1092d12 + LOGIN_CENSUS_JS
36 lines md5 9e5a52d2 — the v99/v105 census blocks VERBATIM,
source-to-source verified) reproduces the v105 values exactly — NO NEW
CLONE GAP. The +1 pin (tests/e2e/calculator.spec.ts): the calculator's
LINE-ITEMS SECTION HEADER ROW at 1280 — the row {flex/center/
space-between/mb 16px/mt 0px/h 32/w 720/childCount 2} + the "Line
Items" h3 {16px/600/rgb(26,58,46)/lh 24px/h 24/margin 0px} + the
junction (h3CenterY === rowCenterY) + the addBtn context {110x32} —
never pinned at ANY viewport in ANY spec (zero "Line Items"
assertions across all 24 specs; the v81 addBtn pin + the v66 height
family + the v93 totalCard census all live on DIFFERENT elements),
measured byte-identical both sides via the one-shot
sectionrow-arbit-v111.sh, mutation-verified single-axis AND
cascade-free (font-semibold -> font-bold at calculator-dialog.tsx:171
line-scoped — the ONLY bare font-semibold line in the file; the
nameH4's mb-1 font-semibold at line 210 untouched; only the v111 pin
red at sectionH3.fw alone [600 -> 700] after the standalone REBUILD).
The ship chain: 314 e2e zero flakes (76+80+79+82 = 317 executions =
314 unique); 35/35 smoke; the screenshots 16/16 byte-identical (the
same-day-seed law); the dev evidence re-captured + VLM-verified.

- THE PROVISIONING LESSON (a fresh-workspace note): a fresh sandbox's
  playwright browser cache can hold only an OLDER pin's binaries
  (chromium-1200 + chromium_headless_shell-1200 here) while
  `npx playwright install chromium --dry-run` happily REPORTS the
  current pin's install location — the dry-run is a location report,
  NEVER an existence proof. The first chunk failed 74/75 with
  "Executable doesn't exist at .../chromium_headless_shell-124"3
  (the headless suite runs the headless-SHELL binary, not the full
  chromium). THE CHECKLIST RULE: verify the cache DIRECTLY
  (`ls /home/z/.cache/ms-playwright/` for BOTH `chromium-<pin>` AND
  `chromium_headless_shell-<pin>`) before the first e2e run; the
  full `npx playwright install chromium` downloads BOTH binaries.
- THE ONE-SHOT CENSUS COMMAND FORM (a census-note addendum): opening
  a hover-revealed control needs the vlm-shots form — mouse-move to
  the button center FIRST (the hover state holds), then mouse-down +
  mouse-up; the bare `agent-browser click` command can drop the
  hover-revealed button before the press lands (the first
  sectionrow-arbit run read "no panel" on exactly this), and a census
  passed into `with-server.sh bash -s` must travel as an ENV VARIABLE
  (the quoted heredoc never expands the parent's shell variables).

The v112 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v105-era LOGIN + CALCULATOR pair (the v106-era NETWORTH +
drill-down-DASHBOARD pair — the desktop 1280x800 FULL-PAGE NETWORTH
view + the DASHBOARD's drill-down EXPANDED state, last re-shot v106 —
now the oldest remaining [v106 < v107 < v108 < v109 < v110 < v111]; the
pair's EIGHTH re-run bracket [v60 -> v67 -> v76 -> v82 -> v88 -> v94 ->
v100 -> v106 -> v112] to be verified against vlm-shots-v106.sh's own
header before the derivation), (2) the axe-core watch at its next
re-check point (only a 5.x wrapper changes the calculus), (3) the
npm-audit watch at its re-check point (only a new advisory in the
next/zod ranges changes the calculus), (4) the deferred reference-write
censuses (unchanged — out of bounds under the v46 read-only rule)."""
    t = t.replace(tail_anchor, tail_anchor + v111_section, 1)
    open("scripts/parity-probes/README.md", "w", encoding="utf-8").write(t)
    print("aligned the probe README (the v111 section + the v112 queue)")

# ---------------- D7b: worklog.md ----------------
t = open("worklog.md", encoding="utf-8").read()
ledger_old = "and every subsequent plan through\n`docs/remediation-plan-v110.md` (the v110 cycle — Session 145)."
ledger_new = "and every subsequent plan through\n`docs/remediation-plan-v111.md` (the v111 cycle — Session 146)."
if ledger_old not in t:
    print("MISS: worklog ledger tail")
    ok = False
else:
    t = t.replace(ledger_old, ledger_new, 1)

session_anchor = "## Session 145 — Parity iteration v110"
v111_entry = """## Session 146 — Parity iteration v111: the re-run cycle's next-oldest candidate (the v105-era LOGIN + CALCULATOR pair's eighth re-run) + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — the v110 bump holds) + the 105th standing checks + the calculator's Line-Items section-header row census pin (PIN-ONLY) (2026-10-24)

**The cycle** (`docs/remediation-plan-v111.md` — the plan validated against the codebase before execution; the delivery record: `docs/session_272.md`): the re-run cadence's next-oldest candidate — the v105-era LOGIN + CALCULATOR pair (the LOGIN view + the CALCULATOR dialog at desktop 1280x800, the v59-era pair's surfaces, last re-shot v105 — now the oldest remaining [v105 < v106 < v107 < v108 < v109 < v110]; the pair's EIGHTH re-run bracket [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111]; the v110-era docs' v111 queue suggestion AGREEING with the rotation ledger — the THIRTY-FOURTH consecutive agreement, the surface names verified against vlm-shots-v105.sh's own header before the derivation) + the axe-core watch at its re-check point + the npm-audit watch (the standing step's second cycle) + the 105th standing checks. **PIN-ONLY for src/ — zero production-code changes, zero dependency changes; +1 e2e = 314.**

**The baseline — the FRESH-CLONE workspace** (the v86..v110 precedent): git clone at main @ 9a78446, the tree clean; the environment re-provisioned from scratch (npm install in 15s — the zod extraction INTACT [840/840 files, the v4/ subdirectory present, no npm ci needed]; next 16.4.3 + zod 4.6.7 confirmed — **the v110 security bump holds**; `.env` [DATABASE_URL="file:../db/custom.db"]; db/ at the repo root, db:generate + db:push + db:seed; BOTH playwright binaries installed after the provisioning catch below); the two commits since the v110 parity push (fe528fa + 9a78446) audited session-log-only [docs/session_270.md + docs/session_271.md — ZERO src/, tests/, prisma/ or lockfile deltas]; the seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran; lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · **313 e2e ✓** (75+80+79+60+23 = 317 chunk executions = 313 unique, zero flakes — the a11y file split off after a filename-parsing artifact caught by the count check) · 35/35 smoke ✓. The codebase audit clean (the production seams re-audited — auth, db-path, the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout) + **npm audit: 0 vulnerabilities** (the v110 bump's end-state verified holding).

**THE PROVISIONING LESSON (the cycle's tooling finding):** the fresh sandbox's playwright cache held only v1200-era binaries; `npx playwright install chromium --dry-run` REPORTED the v1243 location without verifying existence, and the first e2e chunk failed 74/75 on the missing `chromium_headless_shell-1243` (the headless suite runs the headless-SHELL binary). The fix: the FULL install (BOTH binaries). THE CHECKLIST RULE: verify the cache DIRECTLY — the dry-run is a location report, never an existence proof.

**F1 the axe-core watch: NO DRIFT** — npm-latest 4.14.0 (only rc/next sha prereleases beyond; no stable 4.14.1, no 5.x); the installed wrapper + engine both 4.14.0; the v68 dedupe verified (exactly one node_modules/axe-core entry); the engine-contract pin GREEN inside the a11y chunk's 23.

**F2 the 105th standing checks: ALL GREEN** — derived v104→v105 (derive-standing-v111.py, three token families, normalize-back diff clean). Reference side: the four bugs ALL live (toast-blocker `hitIsBurgerChild:false`; sheet-trap `overlayCount:1`; no-landmark `navLandmark:false`; the 464px /networth overflow at 390) + the data census clean on the FIRST read (1 items · $25,000 / 1 items · $5000.00 / 4 items · $525.00) + the SEO pair live. Clone side: R1–R4 ALL GREEN — **the mobile menu VERIFIED WORKING the 105th consecutive time**, zero overflow at 390 on all five views, the SEO pair live; the seedcheck exact after the clone half; one zombie-browser cleanup between the halves.

**F3 the re-run pair (the v105-lineage derivation, the two-half census form)**: the series derived from the v105 lineage (derive-v111-series.py — the six generic swaps + the SIX exact-fragment history corrections, 6/6 on the FIRST run; line-count preservation 101/29/165/29/64/354; bash -n + node --check clean; zero residuals). The census BUILT two-half (build-twohalf-v111.py via derive-build-twohalf-v111.py — the swap-order rule; the first derive attempt failed on three builder-specific forms, corrected against the actual bytes): **md5 contracts e1092d12 (CALC_CENSUS_JS, 61 lines) + 9e5a52d2 (LOGIN_CENSUS_JS, 36 lines) source-to-source verified** — the v99/v105 census blocks VERBATIM. The VLM pairwise verdicts: **CALCULATOR DIFFERENT + LOGIN IDENTICAL** (the v105 precedent — the verdict-variation form) with every flag DOM-arbitrated — the "• Will update category total" note the SEED-DATA class (ref hasWillUpdateSpan false: its own Rent $25.00 EQUALS its calculated total; the totalCard chrome byte-identical), the hover-action row the RESTING-STATE parity class (actionsAtRest {opacity 0, btnCount 2} identical both sides; the reference's screenshot caught its row post-pointer), the row-height flag their consequence; the FAB unflagged (the standing disproof form); the close-key asymmetry the v99-documented finder artifact. **The census reproduces the v99/v105 values EXACTLY — NO NEW CLONE GAP.**

**F4 the calculator's Line-Items section-header row census pin at 1280 (PIN-ONLY; +1 e2e = 314)**: the never-pinned family (the dialog's section row between the v93-pinned totalCard and the items — zero "Line Items" assertions across ALL 24 specs; the v81 addBtn pin walked as CONTEXT ONLY). The one-shot both-sides census (sectionrow-arbit-v111.sh — two mid-build repairs: the vlm-shots mouse-move + down/up click form [the bare click dropped the hover-revealed Calculate button] and the env-var census pass-through [the quoted heredoc never expands the parent's variables]): **EVERY AXIS BYTE-IDENTICAL** — the row {flex/center/space-between/mb 16px/mt 0px/h 32/w 720/childCount 2} + the h3 {"Line Items"/H3/16px/600/rgb(26,58,46)/lh 24px/h 24/margin 0px} + the addBtn context {110×32} + the junction (h3CenterY === rowCenterY) + docSW 1280. The plan written + validated BEFORE the pin; the pin appended to tests/e2e/calculator.spec.ts — **GREEN on the first run** (19 passed; the count now **314**); **mutation verified single-axis AND cascade-free**: font-semibold → font-bold at calculator-dialog.tsx:171 line-scoped (the ONLY bare font-semibold in the file; the nameH4's line 210 untouched) — ONLY the v111 pin red (18 green), the failure diff reading as the sectionH3.fw axis ALONE ("600" → "700"; the v66/v81/v87/v93 pins green under the mutation); restored (git diff src/ = 0), rebuilt, post-restore 19/19 green.

**F5 the ship chain**: lint ✓ · typecheck ✓ · 108/108 unit ✓ · npm audit 0 vulnerabilities ✓ · **314 e2e zero flakes** (76+80+79+82 = 317 executions = 314 unique across FOUR chunks) · 35/35 smoke ✓ · the screenshots **16/16 BYTE-IDENTICAL** (the same-day-seed law — the v110 capture and this one share the UTC day; zero deltas, zero arbitration) · the dev-server evidence re-captured + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the dev-shots scripts derived v110→v111 by the version-swap protocol).

The docs aligned D1–D7 (AGENTS.md the v111 paragraph · CLAUDE.md 314 + the v111 clause · README.md counts + the v111 plan row · zero-balance_SKILL.md the Session 146 row + the state line · PAD v1.1.68 · the probe README's v111 section + THE PROVISIONING LESSON + the ONE-SHOT CENSUS COMMAND FORM note + the v112 queue); `docs/remediation-plan-v111.md` + `docs/session_272.md` saved; the worklog Session 146 entry + the ledger tail. The `.env.example` verified matching the codebase. The v111 probe series + the 105th standing pair + the two-half builder + the one-shot censuses persisted (derive-v111-series.py · derive-standing-v111.py · derive-build-twohalf-v111.py · build-twohalf-v111.py · sectionrow-arbit-v111.sh · ref-arbit-v111.sh + clone-arbit-v111.sh · ref-standing-v105.sh + standing-checks-v105.sh · vlm-shots-v111.sh + login-shots-v111.sh + clone-vlmshots-v111.sh + clone-login-shots-v111.sh + vlm-compare-v111.mjs + arbit-v111.sh · capture-dev-shots-v111.mjs + verify-dev-shots-v111.mjs).

---

"""
if session_anchor not in t:
    print("MISS: worklog Session 145 anchor")
    ok = False
else:
    t = t.replace(session_anchor, v111_entry + session_anchor, 1)
open("worklog.md", "w", encoding="utf-8").write(t)
print("aligned worklog.md (the Session 146 entry + the ledger tail)")

sys.exit(0 if ok else 1)
