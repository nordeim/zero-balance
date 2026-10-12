# Session 116 — Parity iteration v50: the auth states' panel heights (THE FIX — the second production-code change since v46) + the networth tablist's 640 chrome + the dashboard hero's 390 reflow (2026-10-12)

**Goal:** the session-115 v50 queue's three candidates — the auth
states' full 390 census (the surface that found ONE REAL DRIFT), the
networth tablist's chrome at 640, and the dashboard hero's mobile
reflow at 390. TDD-first, docs aligned, commit + push via the SSH
wrapper. (The workspace was RESET this session — a fresh `git clone`
of https://github.com/nordeim/zero-balance.git at 3f0202e; the
environment rebuilt from scratch: `npm install`, `.env` from
`.env.example`, `db:push` + `db:seed`, and `npx playwright install
chromium` — the fresh-sandbox chromium_headless_shell-1243 download
the v49 log did not need.)

## What was done

**Step 0 — the workspace.** The local workspace had been reset (no
zero-balance/ directory) — a fresh clone at 3f0202e ("update session
log" — session_115.md, the v49 session's final log commit; the parity
commit 27df57b below it). The five core docs (AGENTS / CLAUDE / README
/ PAD / SKILL) + the four session docs (session_114 /
remediation-plan-v49 / the repo worklog / session_115) reviewed; the
v49 state verified in code (the F1 spacer in login-card.tsx:724, the
v49 pins in login-parity/dashboard/calculator specs, the 232 count,
the sitemap/robots pair, .env.example matching the .env contract).

**Step 1 — the environment + the baseline chain.** npm install ✓ ·
.env copied from .env.example (DATABASE_URL `file:../db/custom.db`,
the db/ folder at the repo root, db:push + db:seed — the demo
workspace: 7 budget items, 3 assets, 2 liabilities) · `npx playwright
install chromium` ✓. Then the chain: lint ✓ · typecheck ✓ · 108/108
unit ✓ · build ✓ (robots + sitemap prerendered) · **232/232 e2e ✓
(5.4m)** · 35/35 smoke ✓. The audit: npm audit = the same 5 dev-only
ESLint-chain advisories (`--omit=dev` = 0); the secret-pattern scan
clean (the parity-probe reference credentials are the by-design probe
inputs); `.env` ≡ `.env.example`.

**Step 2 — the 44th standing checks.** Reference side
(`ref-standing-v49.sh`, re-run verbatim): all four bugs live — the
toast-blocker (hit `DIV.fixed top-0 z-[100]`, hitIsBurgerChild
false), the sheet-trap re-verified with the PRECISE overlay census
(the z-50 rgba(0,0,0,0.8) 390×844 scrim still open on /income after
the nav click — the heuristic text-keyed detector read false again,
the known artifact), no nav landmark, the /networth 464 overflow; the
data census read-only ("1 items · $25,000" networth / "1 items ·
$5,000.00" income); the SEO pair live. Clone side
(`standing-checks-v49.sh` via with-server): R1 the burger hit-test
direct + the sheet opens, R2 the sheet closes on nav (sheetGone +
overlayGone), R3 the landmark, R4 docSW 390 on all five routes, the
SEO pair. **The 44th standing checks ALL CLEAN.**

**Step 3 — the v50 sweep (the three queue candidates, both sites —
ref-v50.sh + clone-v50.sh, READ-ONLY on the reference).**
- **The auth states at 390 (the queue #1): ONE REAL DRIFT — THE FIX
  (the second production-code change since v46).** The sign-in state
  is byte-identical (the v49 F1 contract re-verified: the wrapper 730
  / the panel 682 / y 57). The sign-up: the reference's wrapper 470 /
  panel 422 / y 187 vs the clone's 454/406/195; the forgot:
  358/310/243 vs 342/294/251 — the panels 16px SHORT at every
  viewport. The inner census isolated the drift to ONE junction: the
  reference (v3 space-y semantics — margin-top on `> * + *`) STACKS
  the back button's own `-mb-2` (-8) with the heading's mt 16 (the
  collapsed net gap 8) while the clone (v4's zero-specificity
  `:where(& > :not(:last-child))` margin-block-end) let the utility
  OVERRIDE the container gap — the heading overlapped the button by
  8px and the container lost 16px (the form heights IDENTICAL: 286 /
  126). A BONUS finding: the reference's forgot container carries
  `sm:space-y-6` (24px at >=640) — absent from the clone. The
  verify-email branch shares the same idiom (its container converted
  too — the reference measurement inherited from the v21 live
  session; a fresh reference registration is a write, out of bounds
  under the v46 read-only rule).
- **The networth tablist at 640 (the queue #2): BYTE-PARITY — PIN.**
  The list 448/36/grid "220px 220px"/#f5f5f5/8px/4px/x 16; the
  triggers 220×28/6px/14/500; the active green pair #14532d on
  #dcfce7 with the shadow's VISIBLE pair `rgba(0,0,0,0.1) 0px 1px
  3px 0px` / `rgba(0,0,0,0.1) 0px 1px 2px -1px` (the FULL reference
  string re-measured unsliced: 2 transparent leads + the pair = 4
  layers; the clone: 4 leads + the pair = 6 — the accepted
  lead-divergence class, the visible layers byte-identical); the
  inactive #737373 pair; the 16×16 currentColor icons.
- **The dashboard hero at 390 (the queue #3): BYTE-PARITY — PIN.**
  The grid 1-col/gap 24; the goal card 358×316@y 253 (the
  reference's 363 rides its own 395 docSW overflow — the
  superset-fix-#4 family; the clone's 358 fits, docSW 390); the
  breakdown 358×324@y 593 (the 24px rhythm); the full internals (the
  icon circle 48/rgba(143,188,63,0.2) + the 24px target icon; the H3
  18/700/white/lh 28; the sublabel/allocation/pct families; the track
  12px/0.1/9999px; the fill's 90deg orange status gradient; the
  balance box 12px/24px/0.05/blur(10px); the figure 30/700/white);
  the chip's flex gap-8 row with the 16/600 rgb(245,169,98) pair —
  BOTH sites' 20px svgs squish to 12px computed under the row's
  flex-shrink (a byte-shared width-pressure artifact: the left figure
  block 158 + the chip 93 on both).

**Step 4 — the remediation plan.** `docs/remediation-plan-v50.md`
written and validated against the codebase (the two container line
numbers, the existing pins' safety analysis — the v12/v13/v24/v49
pins walk the CONTROLS or the sign-in state, never the mode panels'
heights; the v21/v23/v33 verify-email pins walk the controls).

**Step 5 — the TDD execution.** F1 written RED first (both tests
failed against the pre-fix build: the wrapper 454/342, the panel
406/294). The fix applied: the `.zb-auth-mode` + `.zb-sm6` rules in
globals.css (the SPACE-Y V3 SEMANTICS block's third member) + the
class swaps in login-card.tsx (line 693 the shared signup/forgot
container, line 603 the verify branch's). The FIRST fix attempt
carried a `> :not(:last-child) { margin-block-end: 0 }` zeroing rule
(the v9/v24 idiom) — the pin caught it before it shipped (the
measured 430: the 0-2-0 zero beat the button's own -mb-2 utility at
0-1-0 and killed the 8px collapse); the second attempt DROPS the
space-y class entirely (no zeroing needed — v4's emission never
matches) → **GREEN** (the sign-up 422/470/187, the forgot
310/358/243, the 640 sm tier 24px). F2 + F3 written (pin-only —
GREEN immediately; the F2 shadow assertion corrected from the sliced
probe's 2-layer assumption to the unsliced 4-layer truth with the
visible pair pinned). **Four new e2e, 232 → 236.**

**Step 6 — the mutation sanity (S1, five mutations, each with the
standalone REBUILD).** (a) the zb-auth-mode class removed → both F1
tests FAIL (the panels back to 406/294); (b) the back button's -mb-2
removed → F1 FAILS (the net gap 8→16, the wrapper 470→478); (c) the
zb-sm6 modifier removed → the F1 640 sub-check FAILS (the heading mt
24→16); (d) the active tab's data-[state=active]:bg removed → F2
FAILS; (e) the hero track's h-3→h-2 → F3 FAILS. All restored — the
source diff: globals.css (+28) + login-card.tsx (±14).

**Step 7 — the full chain.** lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **236/236 e2e ✓ (5.4m — one flaky not-found metadata test
on the first run, clean on the re-run and standalone)** · 35/35 smoke
✓. The VLM pair on the login SIGN-UP state at 390 (THE FIXED
SURFACE): the VLM flagged 4 diffs (card position / button width /
spacing / shadow depth) — ALL DOM-verified as noise (the panel y 187
/ h 422 / the button 294@x 48 IDENTICAL on both sites; the
shadow-depth flag is the accepted lead-divergence class) — the v43
misattribution lesson's fifth application. The 16 screenshots
regenerated (7 byte-diffs — the auth states shifted by the fix).

**Step 8 — the docs + the ship.** D1–D8 (AGENTS / CLAUDE / README /
PAD v1.1.7 / the SKILL doc's Session 85 row / the probe README's v50
section / session_116 + session_117 / the repo worklog Session 84 /
the workspace worklog). Commit + push to main via the SSH wrapper
(the key materialized, the push verified, the key destroyed).

## Probe lessons (the v50 additions)

- **A stale agent-browser session hangs the next open** — a killed
  run leaves the `.config`/`.engine` pair in ~/.agent-browser and the
  next `agent-browser open` on that session name waits forever (the
  first clone-v50 run hung 600s): `pkill -f agent-browser` + a
  session-file sweep before every probe run.
- **A rebuild swaps `.next/standalone` UNDER a running parity
  server** — page loads die with the browser's own "This page
  couldn't load" interstitial (not an app error): reboot the :3200
  server after every build. The smoke script's step-0 pkill kills it
  too.
- **Slice-bounded censuses lie about multi-layer shadows** — the v49
  tablist probe sliced the reference's shadow at 50 chars (2 of 4
  layers); re-measure the FULL string before pinning layer counts.
- **The reference's sm: tiers are readable from its own DOM class
  list** — the forgot container's `sm:space-y-6` was visible without
  a second live measurement.
- **A specificity collision inside a fix is caught by the pin** —
  the first fix attempt's 0-2-0 zeroing rule vs the 0-1-0 utility:
  the RED→GREEN loop is the guard, the mutation series the proof.

## v51 queue suggestions

The verify-email state's full panel census (needs a reference
registration — a write; only under an explicit waiver), the forgot
CONFIRMATION state's 390 census (the "Password reset unavailable"
honest variant vs the reference's "Check your email"), the hero's
640→390 stat-card row reflow, the savings view's goal-card mobile
census — say the word.
