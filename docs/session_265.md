The workspace was reset — the repo needed a fresh clone. Cloning at main
@ 84cfafd (v107 shipped + the session log), re-establishing the full
context from docs/session_263.md (the prior session's transcript — the
v107 cycle delivered and pushed at f018c3b) + docs/session_262.md +
docs/remediation-plan-v107.md + the worklog Session 142 entry.

The queue is clear: **v108 targets the v102-era MOBILE TWINS pair** (the
probe README's v108 queue agreeing with the rotation ledger — BOTH
mobile 390x844 full-page twins: the /NETWORTH view + the DASHBOARD, the
pair's SEVENTH re-run). The v102 probe header verified before anything
derived (the queue-prose verification lesson). Kicking off the long-pole
environment provisioning while studying the derivation patterns.

npm install completed — but the first attempt died silently in the
background (the sandbox reaps background process groups). Foregrounded.

**The provisioning incident**: lint crashed at startup
(`Cannot find module '.../node_modules/zod/v4/index.cjs'` via
eslint-plugin-react-hooks 7.1.1's unconditional `require('zod/v4')`) and
typecheck followed. Diagnosis: the installed zod 4.6.5 had only 59 of
the published tarball's 840 files — the `v4/` subdirectory absent even
though zod's own exports map references it. The registry tarball
verified intact (`npm pack zod@4.6.5` → 840 files including package/v4/)
— the LOCAL extraction was corrupt, not the lockfile. The disciplined
fix: **`npm ci`** — 840/840 restored, both gates green on the first
re-run, the axe-core dedupe re-verified. THE NPM-CI PROVISIONING LESSON
documented for the lineage.

`.env` written from the example (DATABASE_URL="file:../db/custom.db"),
db/ seeded (the `env -u DATABASE_URL` discipline — the sandbox parent
env carries an out-of-repo path), **seedcheck EXACT** (7 / 1850 / 2235 /
0 / 3 / 2). chromium-1243 installed for the pinned @playwright/test
1.63.0. The post-push commit audit clean (84cfafd session-log/skills-
only, zero src/ deltas).

**F0 baseline FULLY GREEN** — lint · typecheck · 108/108 unit · build
(robots + sitemap prerendered) · **310 e2e** (77+78+78+80 = 313
executions across FOUR disjoint chunks, zero flakes on the FIRST run —
the per-file counts derived authoritatively via --list and summed
[76+77+77+79 = 309 spec] BEFORE any chunk ran) · 35/35 smoke.

**F1: NO DRIFT** — npm-latest 4.14.0 (only rc/next sha prereleases
beyond: 4.14.1-d1531a9.0.sha-d1531a9 + 4.14.1-55245d5.0.sha-55245d5),
wrapper + engine both 4.14.0, dedupe holds post-npm-ci.

**F2: the 102nd standing checks ALL GREEN** — derive-standing-v108.py
(the v101 pair → the 102nd, the THREE token families, normalize-back
clean); reference half: the four bugs ALL live (the 464px /networth
overflow measured docSW 464 directly) + the data census clean on the
FIRST read + the SEO pair live; clone half: **the mobile menu VERIFIED
WORKING the 102nd consecutive time**, zero overflow at 390 on all five
views, the SEO pair live.

**F3**: derive-v108-series.py — the generic swaps + the EIGHT
exact-fragment history corrections (the oldest-remaining bracket
corrected as TWO single-line halves — the v102 compare header wraps it
across lines 4-5), **8/8 on the FIRST run**, zero residual,
line-count-preserving (60/47/68/219). build-twohalf-v108.py — **md5
contracts reproduce the v102 values exactly (82cf8a43 / 85e4ec7e — the
v102 census blocks verbatim)**. The VLM pairwise: **BOTH DIFFERENT**
(the pair's documented class). Flag arbitration: the stat-tile stacking
the v41 mobile-superset class; the summary height its width consequence;
the trend circle the VLM misread; **the "Edit with Base44" overlay
DISPROVEN live** (base44-fab-arbit-v108.sh: fabCount 0 +
bodyHasBase44 false on BOTH sides — a FAB flag WAS raised, so the
v103-form disproof ran); **the "hamburger menu icon missing in Image 2"
flag (the first VLM run only) DISPROVEN live, byte-identical** — BOTH
sides render the toggle at {24,16,28×28} "Toggle Sidebar"
lucide-panel-left 16×16 pathD "M9 3v18" rgb(10,10,10): the reference's
OWN toggle is the panel-left button documented since v3/v7 — no 3-line
hamburger exists on either side (the NEW glyph-misread sub-form, the
svg-fingerprint arbitration); the subtitle wrap the v62 width-delta
class. The two-half census **reproduces the v102 values EXACTLY** —
every axis, the docSW guards ref 464/395 vs clone 390/390. **NO NEW
CLONE GAP.**

**F4**: the family-extension survey — the MOBILE TOPBAR's interior
junction family (the coverage map: the v7 G5 pin holds the burger box +
icon color; the session-5 pins the box GEOMETRY + classes only; the
header's own chrome, the row's flex/gap, the burger's POSITION, and the
brand's COMPUTED chrome never pinned at ANY viewport). The one-shot
topbar-arbit-v108.sh: **byte-identical across sides on every chrome
axis** (header {h 61, pad 24/16, border-b 1px rgb(229,231,227), bg
white} + row {flex/center/gap 16/h 28/childCount 2} + burger {24/16/
28×28/8px} + icon {16×16, rgb(10,10,10)} + brand {ZeroBalance, 20px/
700/28px/rgb(26,58,46)}). The plan written + validated
(docs/remediation-plan-v108.md) BEFORE the pin's execution.

The v108 pin appended to tests/e2e/mobile-layout.spec.ts (typecheck
clean). **Pin GREEN on the first run** (6 passed). The pin-sanity
mutation (sidebar.tsx:224 gap-4 → gap-5, line-scoped — the ONLY `flex
items-center gap-4` line in the file): after the standalone REBUILD,
**ONLY the v108 pin red (5 green), the failure diff reading as the
row's gap axis ALONE** ("16px" → "20px" at the row.gap assertion; every
header axis green before it). Restored (git diff src/ = 0), rebuilt,
**post-restore 6/6 green**.

**F5 the ship chain**: lint · 108 unit · **311 e2e zero flakes**
(77+78+78+81 = 314 executions = 311 unique) · 35/35 smoke · the
screenshots **16/16 BYTE-IDENTICAL** (zero arbitration needed — the
same-day-seed law) · the dev-server evidence set re-captured +
VLM-verified (the menu proof: /income, docSW 390, navLandmark true;
the v107 dev-script's income-link selector save glitch [`aref*=` — the
`[h` lost] noted LOW and corrected in the v108 script; the "1 Insight"
toast the superset feature's transient layering, the below-the-fold
surfaces absent from the viewport-only capture — both non-defects).

**D1–D7 aligned** (align-docs-v108.py: AGENTS v108 paragraph · CLAUDE
311 + the v108 clause · README counts + the v108 plan row · the SKILL
Session 143 row + state · PAD v1.1.65 · the probe README's v108 section
+ the three new lessons + the v109 queue; insert-worklog-v108.py: the
worklog Session 143 entry + the plan-ledger tail) + session_264.md (the
delivery record).

**The ship**: the pre-ship checks clean (src/ untouched — PIN-ONLY
confirmed; .env.example matching; 27 files). Commit **d2970db** via the
message file (the v107 display-corruption lesson). The push: the
runbook re-read, the operator key materialized outside the repo at 0600
— **the fingerprint verified: SHA256:3ddaNlFhMz1JXiGEDgVEaRsUzI4Ev0Ip-
GEEB7NnU4PU** (matching the documented key). paramiko 5.1.0 installed,
the Appendix A shim extracted from the runbook into the workspace bin.

**The wrong-remote catch**: the first dry-run REJECTED with a
non-fast-forward — the wrapper's DEFAULT remote is the sibling
`nordeim/task-management.git` (the wrapper's own lineage), not
zero-balance. The rejection was the safe outcome (the sibling repo's
unrelated history refusing the clobber). The correct invocation adds
`--remote git@github.com:nordeim/zero-balance.git`: **dry-run green
(84cfafd..d2970db, fast-forward, auth verified)** → the real push →
**remote main @ d2970db == local HEAD, the tracking ref synced, the
wrapper's temp key shredded**. The operator key shredded. **Push
DOUBLE-VERIFIED** (the SSH wrapper + the independent HTTPS ls-remote:
d2970db0a502f5a23de993b34d3d7d5dbe23a4f0 both reads). The tree clean.

The v108 cycle is complete and shipped. Here's the summary:

## ✅ v108 Cycle Delivered & Pushed — `main @ d2970db` (double-verified, key shredded)

**The cycle (PIN-ONLY, +1 e2e = 311):**
- **Baseline all green** on the fresh-clone workspace — seedcheck exact ·
  108 unit · 310→311 e2e (four chunks, zero flakes) · 35/35 smoke · build
  with the SEO pair prerendered; **the npm ci provisioning lesson** (the
  corrupt zod extraction diagnosed + fixed without touching the lockfile)
- **The v102-era MOBILE TWINS pair's 7th re-run** — verdicts **BOTH
  DIFFERENT** (the pair's documented class); every flag DOM-arbitrated
  (the stat-tile stacking the v41 superset class; the FAB disproven live;
  the **NEW "hamburger missing" glyph-misread flag disproven
  byte-identical** — both sides render the same panel-left toggle; the
  subtitle wrap the v62 class); the census reproduced the v102 values
  exactly — **no new clone gap**
- **Mobile menu verified working the 102nd consecutive time**; the
  reference's four bugs all still live
- **New pin**: the MOBILE TOPBAR's interior junction family at 390 (never
  pinned at any viewport; byte-identical both sides; mutation-verified
  single-axis `gap-4→gap-5`)
- **Docs aligned D1–D7** — remediation-plan-v108, session_264, worklog
  Session 143, probe README v109 queue; the dev evidence re-captured +
  VLM-verified

**Next:** say "continue v109" to run the next cycle (the v103-era
**ITEMS pair** — the INCOME + EXPENSES views at desktop 1280×800
full-page, the pair's EIGHTH re-run), or ask for any adjustment — e.g.
finally cleaning the low-severity stale comment in `vitest.config.ts`
flagged across cycles, or the v107 dev-script selector glitch now
corrected in the v108 script.
