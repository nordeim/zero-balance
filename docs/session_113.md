# Session 113 — Parity iteration v49: the login panel's mobile-only &nbsp; spacer (THE FIX — the first production-code change since v46) + the donut legend's mobile reflow + the calculator dialog's 640 chrome (2026-10-12)

**Goal:** the session-111 v49 queue's three candidates — the login
panel's mobile 390 census (the surface that found ONE REAL DRIFT), the
donut legend's mobile reflow at 390, and the calculator dialog's 640
chrome. TDD-first, docs aligned, commit + push via the SSH wrapper.
(The workspace was INTACT this session — `git pull` 3f00e47 → 0bf89ce
brought in session_112; the environment (node_modules / .env / db /
the chromium-1243 build) survived from the v48 session — the first
no-rebuild session since the workspace resets began.)

## What was done

**Step 0 — the workspace.** `git pull` fast-forwarded c02dd1b →
0bf89ce (session_112.md, 110 lines — the v48 session's final log
commit). The five core docs (AGENTS / CLAUDE / README / PAD / SKILL)
+ the four session docs (session_111 / remediation-plan-v48 / the
repo worklog / session_112) reviewed; the v48 state verified in code
(the item-details 10 / dialog-buttons 17 / empty-states 8 spec files,
the 229 count, the sitemap/robots pair, .env ≡ .env.example, the db/
folder at the repo root with custom.db + e2e.db).

**Step 1 — the baseline chain.** lint ✓ · typecheck ✓ · 108/108 unit
✓ · build ✓ (robots + sitemap prerendered) · **229/229 e2e ✓ (5.3m)**
· 35/35 smoke ✓. The audit: npm audit = the same 5 dev-only
ESLint-chain advisories (`--omit=dev` = 0); the secret-pattern scan
clean; `.env` ≡ `.env.example`; the v48 diff = ZERO src/ changes
since 3f00e47 (the pin-only contract held).

**Step 2 — the 43rd standing checks.** Reference side
(`ref-standing-v49.sh`): all four bugs live — the toast-blocker via
elementFromPoint at the burger's center (hit `DIV.fixed top-0
z-[100]`, hitIsBurgerChild false), the sheet-trap re-verified with the
PRECISE overlay census (the z-50 rgba(0,0,0,0.8) scrim still open on
/income after the nav click — an early heuristic detector keying on
overlay TEXT missed it; the empty-text overlay needs the
z-index+geometry census), no nav landmark, the /networth 464 overflow;
the data census read-only ("1 items · $25,000" networth / "1 items ·
$5000.00" income); the SEO pair live. Clone side
(`standing-checks-v49.sh` via with-server): R1 the burger hit-test
direct + the sheet opens, R2 the sheet closes on nav, R3 the nav
landmark, R4 docSW 390 on all five routes, the SEO pair — all pass.

**Step 3 — the v49 sweep (three surfaces, both sites — ref-v49.sh +
clone-v49.sh, READ-ONLY on the reference).**
- **The login panel at 390 (queue #1): ONE REAL DRIFT.** The
  reference's `w-full max-w-md` wrapper carries TWO children — the
  panel (w 358 / h 682 / y 57 / radius 16 / bg rgba(255,255,255,0.95)
  / the 2xl visible layer / contentPad 32 / heading 24-700 — all
  byte-identical) **and a mobile-only spacer** `<div class="mt-8
  text-center text-xs text-slate-400 sm:hidden"><p>&nbsp;</p></div>`
  (h 16, mt 32, rgb(148,163,184), ta center, empty content). The
  spacer makes the wrapper 730 (682+32+16) and centers the STACK at y
  57 — 24px above the geometric center. The clone's wrapper carried
  the panel ALONE (682, y 81) — the whole login card rendered 24px
  lower at mobile. Verified on the reference's sign-in AND sign-up
  states (the spacer is a panel sibling — every auth state carries
  it); the 640 contract re-verified live (display none, the panel
  re-centers to y 111). The v12/v13 login pins were desktop-measured
  (sm:hidden hides the spacer there); the v24 auth-forms mobile
  census walked the controls, never the panel's position —
  first-time measurement at 390 caught it.
- **The donut legend at 390 (queue #2): BYTE-PARITY.** The container
  flex/column/gap 12/mt 24; the row h 64/radius 8/pad 12/bg
  rgb(245,248,245); the dot 16×16/radius 4/rgb(224,122,59); the leaves
  (label 16/500/rgb(26,58,46); amount 16/700/rgb(224,122,59); pct
  12/400/rgb(107,114,128)); the right-aligned values; the 16px icon —
  every axis IDENTICAL (a leaf-node census; the first probe's finder
  grabbed the amount+percent PARENT and read the wrapper's style —
  re-measured with leaf targeting). The reference's row w 313 vs the
  clone's 308 = the reference's own 5px /dashboard overflow (docSW
  395 — its documented superset-fix-#4 bug; the clone fits at 390).
  The v44 F3 measured both viewports but pinned only 1280.
- **The calculator dialog at 640 (queue #3): BYTE-PARITY.** The panel
  w 608/x 16/radius 16/maxW 768px (max-w-3xl)/maxH 816px (85vh of
  960)/bg white/overflow hidden; the shadow — the reference's 2
  transparent leads + the 2xl visible layer vs the clone's
  `.zb-modal-panel` direct emission of the SAME visible layer (the
  accepted lead-divergence class); the close 36×36; the header
  border-b 1px solid rgb(229,231,227); the centering (y 223 both —
  data-coincident h 515); sw 640. The v45 F2b pinned only the widths
  at 640 (after a line-item add); the v49 pin censuses the read-only
  open state's full chrome.

**Step 4 — the plan + the TDD execution.**
`docs/remediation-plan-v49.md` written + validated (the insertion
point login-card.tsx:555/723-724, the F2/F3 targets, the mutation
list, the chain gate). F1 written RED FIRST — the pre-fix run FAILED
(the spacer absent: `{ present: false }`, the wrapper 682, y 81), then
the production fix (the spacer added as the wrapper's second child,
the color pinned as the `text-[#94a3b8]` hex — the v4 named-slate
oklab trap, the v7 login-family rule), the rebuild, GREEN. F2 + F3
written pin-only — GREEN immediately. **3/3 v49 pins GREEN.**

**Step 5 — the mutation sanity (six, each with the standalone
REBUILD — the v47/v48 lesson).** (a) the spacer removed → F1 fails
(the TDD RED run itself — the pre-fix proof); (b) the spacer's mt-8 →
mt-4 → F1 fails (the wrapper 730→722); (c) the spacer's sm:hidden
removed → F1's 640 sub-check fails (the spacer display block at 640);
(d) the legend row's p-3 → p-2 → F2 fails (pad 12→8, h 64→56); (e)
the `.zb-modal-panel` box-shadow removed → F3 fails (no 2xl layer);
(f) the calculator's inline maxHeight 85vh → 90vh → F3 fails (maxH
816→864). All restored — `git diff --stat src/` shows ONE file
(login-card.tsx, +14 lines — the F1 fix).

**Step 6 — the full chain.** lint ✓ · typecheck ✓ · 108 unit ✓ ·
build ✓ · **232/232 e2e ✓ (5.3m — 229→232)** · 35/35 smoke ✓.

**Step 7 — the VLM pair + the screenshots.** The VLM pair on the
LOGIN page at 390 (THE FIXED SURFACE — a data-free static form):
**IDENTICAL, zero app flags** (the only flag the reference's own "Edit
with Base44" FAB platform chrome) — the F1 fix's visual verification.
The 16 screenshots regenerated (the capture script).

**Step 8 — the docs.** AGENTS (the v49 paragraph), CLAUDE (three v49
entries + the 232 count), README (the v49 row + the two count sites),
the SKILL doc (the Session 84 row + the state line), the PAD (the
v1.1.6 block), the probe README (the v49 section + the lessons),
session_113 (this log) + session_114 (the raw transcript), the repo
worklog Session 83 + the ledger list, the workspace worklog.

## Standing checks

- Mobile-nav R1–R4: **43rd consecutive pass** (both sites).
- Data drift: reference read-only throughout (the calculator opened +
  censused + closed; the login state swap is client-only).
- SEO: robots + sitemap live on both sites.
- npm audit: unchanged (5 dev-only; --omit=dev = 0).

## Outcome

Three new e2e (229 → 232), 108/232/35 green, ONE production fix (the
first since v46 — the login card's mobile position now byte-matches
the reference at 390), two pin-only surfaces locked (the donut
legend's mobile reflow, the calculator's 640 chrome). The VLM pair on
the fixed surface: IDENTICAL.
