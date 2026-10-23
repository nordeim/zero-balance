The v105 cycle shipped in one continuous session on the FRESH-CLONE
workspace (the sandbox reset — the v86/v88/v90/v91/v92/v98/v100/v101/
v103/v104 precedent: git clone at main @ 50423c0; the environment
re-provisioned from scratch — npm install, `.env` written
[DATABASE_URL="file:../db/custom.db"], db/ re-seeded with the seedcheck
exact, chromium-1243 for the pinned @playwright/test 1.63.0, the
tool-results dir re-created). The full narrative of the cycle's F0–F5 +
D1–D7 work: `docs/session_257.md`; the validated plan:
`docs/remediation-plan-v105.md`; the worklog Session 140 entry: the
repo root `worklog.md`.

The ship: the pre-commit gates re-run green (lint; the staged diff
ZERO src/ changes — PIN-ONLY confirmed; `.env.example` verified tracked
+ codebase-matched [DATABASE_URL="file:../db/custom.db"]; `.env` +
`db/*.db` correctly gitignored; the staleness sweep clean — zero stale
current-state 307 count references; the file modes 644 consistent with
the convention). The commit `449f22d` created (36 files, +2741/−10 —
15 modified [AGENTS.md, CLAUDE.md, the PAD, README.md, the seven
fresh-seed screenshots, the probe README, tests/e2e/login-parity.spec.ts,
worklog.md, zero-balance_SKILL.md] + 21 new [docs/remediation-plan-v105.md,
docs/session_257.md, the 15 v105/v99 probe scripts: the series sextet
vlm-shots-v105.sh + login-shots-v105.sh + clone-vlmshots-v105.sh +
clone-login-shots-v105.sh + vlm-compare-v105.mjs + arbit-v105.sh, the
builder build-twohalf-v105.py, the halves ref-arbit-v105.sh +
clone-arbit-v105.sh, the standing trio derive-standing-v105.py +
ref-standing-v99.sh + standing-checks-v99.sh, the one-shot action-row
arbitration moderow-arbit-v105.sh, the screenshot-arbitration quartet
diff-shots-v105.mjs + diff-shots-v105-bands.mjs + diff-shots-v105-rows.mjs
+ crop-diff-v105.mjs, the VLM crop reader vlm-read-crops-v105.mjs, and
the persisted derivation script derive-v105-series.py]).

The push: the environment re-provisioned (the workspace reset took the
v104 push environment with it — paramiko 5.1.0 re-installed in
/home/z/my-project/ssh-venv, the paramiko ssh shim re-deployed at
/home/z/my-project/bin/ssh, extracted verbatim from the runbook's
Appendix A). The operator key materialized at /tmp/zb-v105-deploy.key
(0600, outside the repo); the fingerprint
SHA256:3ddaNlFhMz1JXiGEDgVEaRsUzI4Ev0IpGEEB7NnU4PU — **matching the
documented fingerprint from session_240.md/session_243.md/
session_246.md/session_249.md/session_252.md/session_255.md** (the
v99/v100/v101/v102/v103/v104 pushes' own verification records — the
same operator key). The dry-run clean (fast-forward 50423c0..449f22d,
the --remote override per the v97/v98 lesson — the wrapper's default
remote is task-management); the real push executed: **remote verified
refs/heads/main @ 449f22d == local HEAD**, the tracking ref synced; the
operator key shredded (randomized + removed, zero residue); the
independent HTTPS re-check confirms remote main @
449f22d2bb59a1fc6044a3fbb9ea1b3572902d12; the tree clean.

**The v105 parity cycle (Session 140) is complete and pushed to
`main @ 449f22d`** — remote verified via the wrapper's post-push
assertion AND the independent HTTPS re-check, tree clean, keys
shredded with zero residue.

**What shipped (PIN-ONLY, zero src/ changes, +1 e2e = 308):**
- **Baseline all green** on the fresh-clone workspace (306 e2e zero
  flakes on the first run across the auditable FOUR-chunk split
  [126+90+57+37 = 310 executions = 306 unique]; 35/35 smoke; seedcheck
  exact)
- **The v99-era LOGIN + CALCULATOR pair's SEVENTH re-run**: the
  verdicts CALCULATOR DIFFERENT + LOGIN IDENTICAL (the pair's
  documented classes) with every calculator flag DOM-arbitrated — the
  "Will update category total" line the SEED-DATA class
  (hasWillUpdateSpan false-vs-true — the reference's own Rent $25.00
  equals its calculated total), the hover-state flag the RESTING-STATE
  parity class (actionsAtRest identical), the FAB the unflagged
  platform-chrome third form; the two-half census (CALC 61 + LOGIN 36
  lines, md5 e1092d12/9e5a52d2 — the v99 blocks verbatim) zero-drift —
  **no new clone gap**
- **New pin**: the login's AUTH-MODE ACTION ROW census at 1280 (the
  flex row + the forgot context + the signup-side button + the "Sign
  up" emphasis span — the v7 G2 pin held only the forgot axes; the
  signup button clicked 8+ times but never chrome-asserted; measured
  byte-identical both sides, mutation-verified single-axis [the
  span.fw axis alone — the fw-on-a-leaf-span form, single-axis BY
  CONSTRUCTION] after the rebuild discipline; the finder lesson: the
  mode switchers are BUTTONS on both sides, never a[href])
- The ship chain 308 e2e zero flakes (311 chunk executions); the
  screenshots **9/16 byte-identical + SEVEN fresh-seed deltas
  arbitrated** (the +2-day roll: five crisp glyph rolls + the "Date:
  October 12 → October 14" FactRow roll + the two ±1-3 RGB
  blur-rounding drift regions — **zero structural bands**; the new
  arbitration discipline: the max-per-pixel-delta decomposition —
  glyph rolls read d 400-700, rounding drift reads d ≤ 3); the docs
  aligned D1–D7; `remediation-plan-v105.md` + `session_257.md` saved

**Next:** per the rotation ledger, v106 targets the v100-era DASHBOARD
pair (now the oldest remaining [v100 < v101 < v102 < v103 < v104 <
v105]) — say "continue v106" to proceed, or request adjustments.
