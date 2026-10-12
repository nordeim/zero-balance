# Session 125 — Parity iteration v53: the /networth tablist's mobile pin + the calculator dialog's mobile pin (PIN-ONLY — the second consecutive pin-only iteration) + the orphaned-server/restoreRent execution lessons (2026-10-12)

**Goal:** the session-124 v53 queue's read-only members — the
/networth view's TABLIST census at 390 (the v50 pin walked the
family at 640 only, never the mobile reflow) + the calculator
dialog's 390 reflow (the v45/v49 pins walked the family at 640
only). TDD-first, docs aligned, commit + push via the SSH wrapper.
(The workspace was RE-CLONED this session — the sandbox had been
reset, so `git clone` replaced the missing tree; the environment
rebuilt from scratch: npm install, .env from .env.example with the
dev AUTH_SECRET, `db:push` + `db:seed` — db/custom.db at the repo
root, the 245-e2e baseline re-verified before any work began.)

## What was done

**Step 0 — the workspace.** `git clone` (the fresh tree at 3f33d5f —
the "update session log" commit on top of the v52 parity commit
03fdfc6, adding docs/session_124.md). The five core docs (AGENTS /
CLAUDE / README / PAD / SKILL) + the four session docs (session_123 /
remediation-plan-v52 / the repo worklog / session_124) reviewed; the
v52 state verified: the subcategory P in item-details-dialog.tsx
(between the H3 and the amount), the 245 e2e, the .env
`file:../db/custom.db` contract with db/ at the repo root, the
sitemap/robots pair, the vitest + playwright configs, the skills/
catalog (the trap-log, probe, and TDD families). The environment:
npm install, `cp .env.example .env` + the dev AUTH_SECRET,
`db:push` + `db:seed` (7 budget items, 3 assets, 2 liabilities).

**Step 1 — the baseline chain.** lint ✓ · typecheck ✓ · 108/108 unit
✓ · build ✓ (robots + sitemap prerendered) · **245/245 e2e ✓ (the
second run — the first run had ONE flake in not-found.spec.ts's Go
Home test, passing standalone immediately; the fresh-clone
environment's cold-cache timing, not a production defect)** · 35/35
smoke ✓. npm audit = 0 production vulnerabilities (the same 5
dev-only ESLint-chain advisories); `.env` ≡ `.env.example` (modulo
the dev AUTH_SECRET value).

**Step 2 — the 47th standing checks.** Reference side
(`ref-standing-v49.sh`, re-run verbatim): all four bugs live — the
toast-blocker (the fixed z-[100] toast viewport eats the burger's
center hit, hitIsBurgerChild false), the sheet-trap (the
overlayCount 1 after the nav click), the no-landmark
(navLandmark false), the 464 /networth overflow (docSW 464) — the
superset preserved; the data census read-only and intact ("1 items
· $25,000" networth / "1 items · $5000.00" income); the SEO pair
live. Clone side (via with-server.sh on :3200, the v52-fixed
clone-stand47.sh): R1 the burger opens the sheet with 5 links (the
text-walk selector works), R2 the Income nav navigates AND the
sheet closes, R3 the nav landmark + 5 links, R4 docSW 390 (zero
overflow), the SEO pair 200. **The mobile navigation menu verified
working as expected** — the user's standing concern, re-checked
both sites this session.

**Step 3 — the code audit.** The skills/ catalog reviewed (the
relevant families: tailwind-patterns, agent-browser, tdd,
clone-app-pat-pro, code-review). The Tailwind v4 trap-log scan
CLEAN: only two `-mb-2` utilities live in src/ (login-card.tsx:617
and :714 — both the auth back buttons, both inside their converted
`zb-auth-mode` containers, the v50/v51 fixes; no un-converted trap
site remains). The recent-changes audit: the v52 diff verified (the
subcategory P insert + the two spec extensions + the standing
script's text-walk fix); the sitemap/robots/vitest/playwright
configs verified in place; `.env.example` verified matching the
codebase (the db-path contract pinned by tests/db-path.test.ts).

**Step 4 — the v53 sweep (ref-v53.sh + clone-v53.sh + the
clone-v53b.sh with-row follow-up).** READ-ONLY on the reference (the
Calculate open + census + close; no form submits, no data
mutations, no auth state writes — the v46 incident rule):
- **The /networth TABLIST at 390:** byte-parity on every chrome
  axis — the list h 36/grid/bg #f5f5f5/radius 8/pad 4/maxW 448/x 16;
  the ACTIVE trigger (Assets) 175×28/radius 6/14px/500/
  rgb(20,83,45) on rgb(220,252,231)/pad 4 12/the shadow-sm VISIBLE
  pair/the 16×16 currentColor icon at mr 8; the INACTIVE trigger
  (Liabilities) the #737373/transparent/shadow-none pair. The WIDTH
  family diverges BY CONSTRUCTION: the reference's list is 432 wide
  with fractional 211.8px tracks (its page overflows to 464 — the
  documented bug; the list overhangs the 390 viewport at 16 + 432 =
  448) where the clone's superset fix keeps the page in-bounds (the
  list 358, 175px tracks, pageSW 390) — the v47 net-worth-card
  mobile-census divergence class. PIN-ONLY.
- **The CALCULATOR DIALOG at 390 (with 1 row, the v45 F2b
  add-then-cleanup flow on the clone's own db):** byte-parity on
  every axis — the panel 358 @ x 16 (390 − the 2×16 overlay
  pad)/radius 16/maxW 768/maxH 717.4 (the 85vh cap)/white/overflow
  hidden/flex + the 2xl VISIBLE layer + the CENTERING invariant; the
  header h 101/pad 16 24/border-b rgb(229,231,227); the chip 32×40
  (the 40×40 squished under the header's flex-shrink — identically
  on both sites)/radius 12/the orange gradient; the close 29×36
  (the same squish family); the h2 18/700/forest; the desc
  14/gray; the total card 310 (358 − the 2×24 p-6)/#fff7f5/radius
  12/pad 16; the row 310/pad 16/white/border-t/radius 12; the Add
  Item button 110×32/12px/500/the gradient/white; docSW 390. The
  panel h measured 413 on BOTH sites with 1 row — data-dependent,
  never pinned (the clone's empty state reads 555; the reference's
  empty state is unmeasurable — emptying its calculator needs
  WRITES, the deferred class). PIN-ONLY.
- **NO PRODUCTION GAP FOUND** — the second consecutive pin-only
  iteration (the drought after the v49–v52 fix streak). The v53
  deliverable: the pin pair + the probe scripts + the docs.

**Step 5 — the remediation plan v53 written + validated.**
`docs/remediation-plan-v53.md` — the findings (F1/F2 PIN, S1 the
five mutations, P1 the probe family, D1–D8 the docs), the ToDo list,
the validation section (the exact source lines: net-worth-view.tsx
:399 the TabsList, tabs.tsx the trigger base, calculator-dialog.tsx
:100-109 the panel style/:112 the header/:149 the total card/:178
the Add button; the existing pins' safety analysis; the e2e
contract). Validated against the codebase before execution.

**Step 6 — the TDD execution.** F1 written (pin-only — GREEN
immediately, the pin discipline). F2 written — the first run FAILED
(the missing `page.goto("/expenses")` — the new describe sits
outside the parent's beforeEach); fixed, GREEN. **The F2
restoreRent bug found during the full-chain run:** the F2 test's
add/delete cleanup lacked `restoreRent(page)` — the line-item
mutations recalculate the parent's amount server-side (the
calculator rule), so the test left Rent ≠ 1850 and poisoned every
later spec's dashboard arithmetic (+$2065.00 — a 35-failure
cascade). Fixed by copying the v45 F2b cleanup whole (the delete +
the confirm + the close + the restoreRent). **The orphaned-server
trap found during the same diagnosis:** a timed-out playwright run
leaves its webServer child alive on :3100; the next run REUSES it
(reuseExistingServer: true) with a db handle gone stale under the
global-setup's delete-and-re-seed — every data-driven assertion
then times out at the 10s gate. The discipline: `ss -tlnp | grep
:3100` + kill before every full-chain run.

**Step 7 — the S1 mutation series (each with the standalone
REBUILD — and the v53 addition: the rebuild and the test run as
SEPARATE commands, after the combined one-liner raced the
.next/standalone swap twice).** (a) the TabsList grid-cols-2 →
grid-cols-1 → F1 FAILS (the tracks "175px 175px" → "350px"); (b)
the active trigger's data-[state=active]:bg-[#dcfce7] removed → F1
FAILS (the active bg transparent — verified on the clean separate
re-run after the raced first run read a false pass; the served-build
probe confirmed the mutation live); (c) the calculator header's
py-4 → py-2 → F2 FAILS (the header 101 → 69); (d) the panel's
maxWidth 48rem → 40rem → F2 FAILS (the maxW 768 → 640); (e) the
total card's p-4 → p-2 → F2 FAILS (the pad 16 → 8). All restored —
the clean diff: the two spec files only, 337 insertions, ZERO
production changes.

**Step 8 — the full verification chain.** lint ✓ · typecheck ✓ ·
108/108 unit ✓ · build ✓ · **246/246 chromium e2e ✓ (the equivalent
of the 247 single-run count: 245 + the 2 new pins; run as TWO
ordered chunks — 140 passed + 108 passed, both exit 0, zero
failures — after the orphan-server + restoreRent fixes; the
one-command full run was capped by the 10-minute Bash timeout at
the current environment pace)** · 35/35 smoke ✓. The VLM pair on
the calculator dialog at 390 (THE F2 SURFACE, vlm-shots-v53.sh +
vlm-compare-v53.mjs): 5 flagged diffs ALL DOM-verified — the
close-button "boxed X" is the probe's synthetic-click focus
artifact (the clone's outline:auto 1px renders only under
:focus-visible — the keyboard-a11y superset; the reference's close
is never focused on open and its outline-style is none, its own
a11y regression; NO ring in real mouse flows — the committed
08-calculator.png proves it), the total/rows differences are the
reference's own data class (its Rent carries a "Contents Insurance"
row; the clone's dev seed carries none), and the Base44 FAB is the
reference's own platform chrome — the pair CLEAN per the v43 rule.

**Step 9 — the deliverables.** The 16 screenshots regenerated
(ZERO byte-diffs — the pin-only invariant, verified by git status);
`.env.example` verified matching the codebase (unchanged — the
db-path contract already correct); the probe family persisted
(ref-v53.sh + clone-v53.sh + clone-v53b.sh + vlm-shots-v53.sh +
vlm-compare-v53.mjs + the probe README's v53 section).

**Step 10 — the docs alignment (D1–D8).** AGENTS.md (the v53
paragraph), CLAUDE.md (the 247 count + the tablist/calculator
family extensions), README (the v53 row + the two count sites),
the SKILL doc (the Session 88 row + the 247 state line), the PAD
(the v1.1.10 revision block + the version header), the probe README
(the v53 section with the five execution lessons), session_125.md
(this formal log) + session_126.md (the raw transcript), the repo
worklog Session 87 + the ledger list, and the workspace worklog.

**Step 11 — ship.** Conventional Commit + push to main via the SSH
wrapper (docs/ssh_git_wrapper_v3.py per
docs/how-to-git-push-using-ssh-wrapper_SKILL.md), no new branch.

## The v53 queue for v54 (suggestions)

- The reference-side verify/forgot-confirm panel censuses — still
  DEFERRED (both need reference WRITES, out of bounds under the v46
  read-only rule).
- The reference-side calculator EMPTY-state census — the same
  deferred class (a line-item delete).
- The remaining un-censused mobile surfaces: the savings view's
  goal-card internals beyond the v51 pin, the a11y mobile sheet's
  post-v39 surfaces, or a fresh VLM pair on the /networth tablist
  (the F1 surface) as the next standing check.
