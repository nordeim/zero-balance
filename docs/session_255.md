The v104 cycle shipped in one continuous session on the FRESH-CLONE
workspace (the sandbox reset — the v86/v88/v90/v91/v92/v98/v100/v101/
v103 precedent: git clone at main @ bb7e02e; the environment
re-provisioned from scratch — npm install, `.env` written
[DATABASE_URL="file:../db/custom.db"], db/ re-seeded with the seedcheck
exact, chromium-1243 for the pinned @playwright/test 1.63.0, the
tool-results dir re-created). The full narrative of the cycle's F0–F5 +
D1–D7 work: `docs/session_254.md`; the validated plan:
`docs/remediation-plan-v104.md`; the worklog Session 139 entry: the
repo root `worklog.md`.

The ship: the pre-commit gates re-run green (lint; the staged diff
ZERO src/ changes — PIN-ONLY confirmed; `.env.example` verified tracked
+ codebase-matched [DATABASE_URL="file:../db/custom.db"]; `.env` +
`db/*.db` correctly gitignored; the staleness sweep clean — zero stale
current-state 306 count references; the file modes consistent with the
v103 convention — the historical 755 probe scripts untouched). The
commit `6589c35` created (22 files, +2139/−5 — 8 modified [AGENTS.md,
CLAUDE.md, the PAD, README.md, the probe README,
tests/e2e/nav-geometry.spec.ts, worklog.md, zero-balance_SKILL.md] +
14 new [docs/remediation-plan-v104.md, docs/session_254.md, the 12
v104/v98 probe scripts: the series quartet vlm-shots-v104.sh +
clone-vlmshots-v104.sh + vlm-compare-v104.mjs + arbit-v104.sh, the
builder build-twohalf-v104.py, the halves ref-arbit-v104.sh +
clone-arbit-v104.sh, the standing trio derive-standing-v104.py +
ref-standing-v98.sh + standing-checks-v98.sh, the one-shot brand
arbitration brand-arbit-v104.sh, and the persisted derivation script
derive-v104-series.py]).

The push: the environment re-provisioned (the workspace reset took the
v103 push environment with it — paramiko re-installed in
/home/z/my-project/ssh-venv, the paramiko ssh shim re-deployed at
/home/z/my-project/bin/ssh). The operator key materialized at
/tmp/zb-v104-deploy.key (0600, outside the repo); the fingerprint
SHA256:3ddaNlFhMz1JXiGEDgVEaRsUzI4Ev0IpGEEB7NnU4PU — **matching the
documented fingerprint from session_240.md/session_243.md/
session_246.md/session_249.md/session_252.md** (the v99/v100/v101/
v102/v103 pushes' own verification records — the same operator key).
The dry-run clean (fast-forward bb7e02e..6589c35, the --remote override
per the v97/v98 lesson — the wrapper's default remote is
task-management); the real push executed: **remote verified
refs/heads/main @ 6589c35 == local HEAD**, the tracking ref synced; the
operator key shredded (randomized + removed, zero residue); the
independent HTTPS re-check confirms remote main @
6589c35ee4dfd75a03d10e08d5696653c21917cc; the tree clean.

**The v104 parity cycle (Session 139) is complete and pushed to
`main @ 6589c35`** — remote verified via the wrapper's post-push
assertion AND the independent HTTPS re-check, tree clean, keys
shredded with zero residue.

**What shipped (PIN-ONLY, zero src/ changes, +1 e2e = 307):**
- **Baseline all green** on the fresh-clone workspace (306 e2e zero
  flakes on the first run across the auditable FOUR-chunk split
  [126+90+57+37 = 310 executions = 306 unique — the per-chunk file
  lists derived from ls + the per-file --list counts summed against
  the authoritative total BEFORE any chunk ran]; 35/35 smoke; seedcheck
  exact)
- **The v98-era SAVINGS pair's SEVENTH re-run**: the verdict DIFFERENT
  (the pair's documented verdict class) with every flag DOM-arbitrated
  — the card-footer the v57 DATA-CONDITIONAL class (the clone's
  "Brokerage" chip, childCount 1-vs-2), the card grid the seed-count
  class, the rest the seed-data/user-identity classes, and the "Edit
  with Base44" FAB the THIRD documented form (UNFLAGGED platform
  chrome — no arbitration needed); the two-half census (SV_CENSUS_JS
  153 lines, md5 891ab9b6) zero-drift — **no new clone gap**
- **New pin**: the rail's TOP brand-block subtitle/row census at 1280
  (the flex row + the h2 color/lh + the "Budget Planner" subtitle
  chrome — the family never pinned beyond the v7 G4 tile/icon/h2-size
  axes; measured byte-identical both sides, mutation-verified
  single-axis [the subtitle.fs alone] after the rebuild discipline;
  the live discovery: the reference's rail is a DIV not an aside — the
  fallback-chain finder lesson)
- The ship chain 307 e2e zero flakes (310 chunk executions); the
  screenshots **16/16 BYTE-IDENTICAL** (the same-day regeneration —
  the v97 precedent, NO DATE-class deltas this cycle); the docs
  aligned D1–D7; `remediation-plan-v104.md` + `session_254.md` saved

**Next:** per the rotation ledger, v105 targets the v99-era LOGIN +
CALCULATOR pair (now the oldest remaining [v99 < v100 < v101 < v102 <
v103 < v104]) — say "continue v105" to proceed, or request
adjustments.
