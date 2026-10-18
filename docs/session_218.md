# Session 218 — the v90 cycle (the mobile 390 twins' fourth re-run)

The audit → align → remediate → push workflow, continued from the v89
state (main @ 0f8bec4 — the v89 parity commit f2040a3 + the two
session-log commits). The task chain: refresh the workspace, review the
core docs + the latest session docs, audit the codebase, run the parity
iteration against the reference, PIN the verified chrome, re-run the
full chain, align the docs, and push to main via the SSH wrapper.

## The workspace + the audit

The workspace RESET (the sandbox wiped since session 217) — the
fresh-clone path (the v86/v88 precedent): `git clone
https://github.com/nordeim/zero-balance.git` at main @ 0f8bec4, the
tree clean. The environment re-provisioned end-to-end: npm ci (354
packages), `.env` written (DATABASE_URL="file:../db/custom.db"), db/
at the repo root (db:generate + db:push + db:seed — 7 items / rent
1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities, the
seedcheck exact), chromium-1243 installed, the paramiko ssh shim
deployed outside the repo at /home/z/my-project/bin/ssh.

The core docs reviewed (AGENTS.md, CLAUDE.md, README.md, the PAD
v1.1.46, zero-balance_SKILL.md) + the latest session docs
(session_216.md, remediation-plan-v89.md, the worklog's Session 124
entry, session_217.md) — the v89 state confirmed: 292 e2e / 108 unit /
35 smoke / PAD v1.1.46 / Session 124. The v89 plan's v90 queue
suggestion: the v84-era MOBILE 390 TWINS — **with the surface-name
transcription error caught and corrected during the pre-execution
ledger verification**: the v89-era docs' prose said "the login +
dashboard mobile views" and "the twins' FIFTH re-run [v69 → v74 → v78 →
v84 → v90]", but the v84 probe scripts themselves (vlm-shots-v84.sh)
and the v84 plan both say the twins are **the /networth + the
dashboard FULL-PAGE pair at 390x844**, and v74 was the savings DESKTOP
pair — the true history [v62/v63 → v69 → v78 → v84 → v90] = the FOURTH
re-run. The correction documented in the v90 plan (the queue-prose
verification lesson: the ledger's authority is the probe lineage, never
the prose).

The codebase audit clean: the v89 commit (f2040a3) re-verified
PIN-ONLY as documented (19 files, +1748/-4, ZERO src/ changes); the two
commits since session-log-only; the production seams re-audited (auth
scrypt/HMAC, the db-path contract, the SEO pair [robots.ts +
sitemap.ts — both prerendered by the build], the Tailwind v4
mitigations [`@variant hover (&:hover)` + the toast pointer-events fix
+ the inline-rgba discipline], the three test tiers); the repo's
skills/ folder excluded from checking/testing/compilation throughout
(eslint ignores + tsconfig exclude, verified live).

## F0 — the baseline chain: FULLY GREEN as-shipped

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered) · **292 e2e ✓** (121 + 114 + 59 chunk executions
= 294 total = 292 unique tests — the exact documented v89 state) ·
35/35 smoke ✓ — all on the first run after the fresh-clone
reprovisioning, zero flakes.

## F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next
prereleases beyond — no stable 4.14.1, no 5.x exists); npm-latest
`axe-core` 4.14.0; the lockfile holding the v68 dedupe state (the
wrapper 4.14.0, no nested engine dir); the engine-contract pin GREEN
standalone (2 passed).

## F2 — the 84th standing checks: ALL GREEN

ref-standing-v84.sh + standing-checks-v84.sh (version-bumped from v83
across the THREE token families [v83→v84, 83rd→84th, AND the bare
session names ref83→ref84/clone83→clone84] — version-bump-only diffs
verified by normalizing back and diffing clean, zero old tokens
remaining). Reference side: the four bugs ALL live [toast-blocker
`hitIsBurgerChild:false`; sheet-trap `overlayCount:1`; no-landmark
`navLandmark:false`; the 464px /networth overflow at 390]; the data
census UNCHANGED (the 84th clean drift check); the SEO pair live.
Clone side: R1–R4 ALL GREEN — **the mobile navigation menu VERIFIED
WORKING (the 84th consecutive time)**: `hitIsBurgerChild:true`, the
sheet opens, closes on nav, the nav landmark present; zero overflow at
390 on all five views; the SEO pair live.

## F3 — the re-run pair (the mobile 390 twins' FOURTH re-run)

The v90 probe series sed-derived from the v84 lineage (vlm-shots-v90.sh
+ clone-vlmshots-v90.sh + vlm-compare-v90.mjs + arbit-v90.sh — the
version + session-name + tmp-dir token substitutions; the headers
history-corrected to the fourth re-run; the functional bodies verified
version-bump-only by the normalize-back diff; login on the first
attempt both sides; the parked pointer at (5,5); read-only on the
reference — the v46 rule holds).

**Both verdicts DIFFERENT, every flag DOM-arbitrated to the v84 re-run's
own documented classes** — the networth pair: the tiles side-by-side
(ref) vs stacked (clone) [the v41 mobile-superset class], the
medallion "larger circle" [a VLM perception misread — the 64×64 +
32×32 chrome byte-identical], the tab-bar alignment [a misread under
the v53 pin], the data classes, the Base44 overlay [platform-chrome];
the dashboard pair: the subtitle wrap [the v62 width-delta class], the
black tooltip [platform-chrome], the progress/donut [seed-data].

The both-sides census (arbit-v90.sh — the combined script ran clean
this cycle, no resource exhaustion, no two-half split needed)
**REPRODUCES the v84 census values EXACTLY — zero drift on every
axis**: the summary card {ref 432×333 on its 464 docSW vs clone
358×421 on its fitting 390 — the v41 class}, the statGrid {gap 16px
identical, cols 2-col-vs-1-col the v41 class}, the tiles {h 84
byte-identical}, the medallion {64×64 both} + the trendIcon {32×32
both}, the subtitle chrome {fs 16px/fw 400/rgb(107,114,128)/lh 24px,
P h 48, block h 92, 2 lines — byte-identical}, the breakdown card {h
324 byte-identical, svgCount 7, the [16,14] family, rechartsWrappers
0, pieSectors 0, the H3/DIV heights identical}. **NO NEW CLONE GAP —
the iteration PIN-ONLY.**

## F4 — the v90 pin: the stat-tile INTERIOR census at 390 (+1 e2e = 293)

The never-pinned axes mapped (the v41 F3 = the card box/figure/chip;
the v63 F3 = the tile BOX family; the v84 F4 = the ratio-footer; the
v60 F1 = the tile value's amtFw at 1280 — a coverage discovered by the
mutation, see below): **the two tiles' INTERIOR families** — the label
{P/fs 12px/color rgba(255,255,255,0.7)/mb 4px/h 16} + the value
{P/fs 24px/fw 700/white} — plus the tile-box/grid re-affirm + the
docSW guard. The pin's own axes first measured byte-identical on both
sides by the supplemental census (tile-interior-arbit-v90.sh — the
v87/v88/v89 one-shot precedent): the ONLY deltas the tile width (ref
176 on its overflowing 2-col vs clone 294 on its fitting 1-col — the
v41 class) and the docSW (464 vs 390).

The pin appended to tests/e2e/networth.spec.ts (the v41/v63/v84 pins'
own file, the v63 F3 finder verbatim) — typechecked, then **GREEN on
first run** (the setup + the pin = 2 passed standalone).

**THE MUTATION-AS-COVERAGE-AUDIT CATCH**: the pin-sanity mutation's
first executed form — the bare class swap `font-bold` →
`font-extrabold` at net-worth-view.tsx:371 (by LINE NUMBER) — DID
cascade: the full networth.spec.ts under it read TWO red (the v90 pin
AND the v60 F1 pin at 1280, failing at its statTile.amtFw axis
"700" → "800"). The root cause: the plan's grep verification had
searched the `fw:` assertion token and MISSED the v60 pin's `amtFw`
shorthand — the tile value's fw was already pinned at 1280 all along.
The catch is the mutation discipline working as designed (the mutation
is the coverage-map audit, not just the pin's sensitivity check). The
corrected form — the viewport-scoped dodge `font-bold` → `font-bold
max-lg:font-extrabold` (the max-lg variant INERT at ≥1024px, active
below) — confines the flip to the pin's own viewport family: under it
the full networth.spec.ts read **only the v90 pin red (28 green, the
v60 pin green)**, the failure diff reading as the fw axis alone
("700" → "800"); restored (the standalone REBUILD as a SEPARATE
command; `git diff src/` = 0 lines; the post-restore full run 29/29
green). The plan's coverage map and grep-verification text corrected
accordingly (the shorthand-token grep lesson).

## F5 — the full chain re-run + the screenshots

lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **293 e2e** (122 + 114 +
59 chunk executions = 295 total = 293 unique tests, zero flakes) ·
35/35 smoke ✓. The 16 standing screenshots regenerated + byte-compared:
**16/16 BYTE-IDENTICAL** (the same-day-seed byte-identity law — the
fresh-clone seed planted and the shots taken on the same calendar day
reproduce the committed set byte-for-byte; no pixel arbitration
needed). The final seedcheck exact.

## D1–D7 — the docs alignment

D1 AGENTS.md (the v90 paragraph), D2 CLAUDE.md (293 + the v90 pin
clause), D3 README.md (the counts + the v90 plan-table row), D4
zero-balance_SKILL.md (Session 125 audit row + the state lines), D5
the PAD's v1.1.47 revision block, D6 the probe README's v90 section
(the new probes + the queue-prose verification lesson + the
shorthand-token grep lesson + the fresh-clone reprovisioning note +
the v91 queue), D7 this session_218.md + the worklog Session 125 entry.

## The ship

The pre-ship gate: lint ✓ · typecheck ✓ · PIN-ONLY ✓ (`git diff src/`
= 0) · test-results cleaned · no orphaned servers · .env.example
tracked (unchanged, still matching the codebase). The parity commit
(the v90 pin + the probes + the plan + the docs), then the session-log
commit (session_218.md + the worklog entry). The SSH infrastructure:
the operator key written (0600), the fingerprint verified, the dry-run
push via the wrapper (the shim on PATH, the explicit --remote flag —
the v81 lesson), then the real push — remote verified `main @ <sha>
== local HEAD`, the operator key shredded.
