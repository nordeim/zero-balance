# Session 83 — Parity iteration v39 (session-81/82 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_81.md` /
`docs/remediation-plan-v38.md` / `worklog.md` / `docs/session_82.md`.
Full autonomy granted on the open questions, so I worked the whole
chain directly.

**Step 1 — workspace refresh.** The local workspace had been RESET
(only an empty stub remained), so I re-cloned
`https://github.com/nordeim/zero-balance.git` fresh at `a2d5381`
(the session-82 transcript commit). The environment rebuilt:
`npm install` (495 packages), `cp .env.example .env`
(`DATABASE_URL="file:../db/custom.db"` — the db/ folder at the repo
root, exactly as the brief specifies), `npm run db:push` +
`npm run db:seed` (the demo workspace: 7 budget items, 3 assets, 2
liabilities), `npx playwright install chromium` (the fresh
headless-shell 1243). The latest docs confirmed in place:
session_81.md, session_82.md, remediation-plan-v38.md, worklog.md.

**Step 2 — docs review.** The five project docs (AGENTS, CLAUDE,
README, PAD, SKILL) re-read; the v38 changeset verified in place (the
8-test a11y gate + the S1/S2 pins + the hasfocus-gate helper). The
session_81/82 transcripts reviewed — the v38 state: 108/187/35 green,
the queue for this session: **the a11y gate's MOBILE extension** (a
390×844 scan of the sheet-open state — the queue's third item), the
dashboard quick-action Add Item's focus walk, or the net-worth
summary chip's savings-class viewports. The skills/ catalog consulted
(clone-app-pat-pro, agent-browser, tdd re-read; the Tailwind v4
skills' mobile-navigation debugging sections re-checked) — skills/
excluded from code checking, testing and compilation throughout, as
the brief specifies.

**Step 3 — baseline chain.** Lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · e2e: the FIRST full run
flagged ONE flake — `not-found.spec.ts › Go Home navigates to the
dashboard` failed a `toBeVisible` at 11.1s — it passed in isolation
(7/7) AND in the full re-run (**187/187, 4.0m**): a first-run-after-
rebuild warm-up timing artifact, not a regression (the standing
checks + both mobile scans below ran against the same build with zero
drift). 35/35 smoke ✓. npm audit: the same 5 dev-only ESLint `braces`
advisories — accepted, unchanged. The secret-pattern scan clean.
`.env.example` verified current (keys matching `.env`).

**Step 4 — the two-site sweep.** The reference standing checks (33rd,
`ref-v39.sh`): R1 — the toast-blocker still intercepts the burger's
center hit (DIV.fixed.top-0.z-[100], scrollWidth 395); R2 — the sheet
still traps after nav (sheet open, body locked on /income); R3 — no
nav landmark on `/`, no active highlight; R4 — the 395px overflows on
`/`+`/dashboard`. The census before AND after all probes unchanged
(allocation 30.5%, income $5000.00, savings $1000.00, expenses
$525.00 — read-only held). The SEO pair live (robots allow-all + the
sitemap; the reference's capitalized /Income /Savings URLs still
documented). The clone-side standing checks (33rd, `clone-v39.sh`
inside with-server.sh): R1 direct svg hit 390; R2 the sheet closes
after nav (superset #2); R3 the nav landmark + the root-route
Dashboard highlight; R4 zero overflows; the census 62.8% / 5550 /
1250 / 2235 (the seed unchanged). **The Tailwind v4 pins hold — the
mobile menu works as expected on both sites.**

**Step 5 — the v39 surface (the a11y gate's mobile extension),
measured live on BOTH sites** (`a11y-scan-v39.mjs` — the v38 scanner
extended with the 390×844 isMobile+hasTouch emulation, plus
`axe-detail-v39.mjs` / `axe-detail-ref-v39.mjs` for the color
provenance):

- The REFERENCE at mobile: `button-name` (CRITICAL) fires on
  /income + /expenses + /savings + /networth (its unlabeled Select
  triggers + the card kebab) and `svg-img-alt` on `/`+`/dashboard`
  (its donut sectors) — the same families as desktop. The clone
  PASSES both on every mobile route; its only failures are
  color-contrast — every flagged color enumerated and in the
  reference's own 7-color palette (the mobile node counts differ
  from desktop only by the demo card counts: the clone's 2 income
  cards vs the reference's 1, its 3 expense cards vs 4, its 3 assets
  vs 1).
- THE HEADLINE: the sheet-OPEN structural census. The reference's
  mobile sheet is a plain `fixed` div — NO dialog role, NO
  aria-labelledby, NO `<nav>` landmark, NO accessible title. The
  clone's sheet is a Radix Dialog: `role="dialog"` +
  `aria-labelledby` → the sr-only "Navigation" DialogTitle +
  `<nav aria-label="Primary">` + the five links + the named burger
  (sr-only "Toggle Sidebar"). The sheet-open scan on the clone adds
  ZERO violations beyond the 14 color-contrast baseline nodes.
- The VLM pairwise (one fresh pair, 390×844): the mobile sheet-open
  state — VERDICT DIFFERENT with BOTH flags explained: (1) the
  clone's Dashboard link carries the active highlight (superset fix
  #3 — the reference marks nothing active on `/`, its R3 bug); (2)
  the avatar letter U vs D (the different demo users). Zero
  unexplained visual drift.

**Step 6 — the remediation plan.**
`docs/remediation-plan-v39.md` written and pre-validated against the
codebase (the insertion points, the mutation targets, the seed
arithmetic, the marker pairs) before any execution: F1 the mobile
a11y gate (8 tests), S1 two pin-sanity mutations, T2 the probes +
the README section.

**Step 7 — TDD execution.** The 8 mobile tests appended to
`tests/e2e/a11y.spec.ts` (a new
`test.use({viewport: 390×844, isMobile, hasTouch})` describe — the
six authed routes under the shared two-gate helper; the sheet-open
test with the REAL burger click + the structural pins + both gates +
the Escape close; the logged-out mobile login in its own opt-out
describe). **All 17 a11y tests GREEN on the first run (1.0m).**
Mutation (a) — the burger's sr-only span stripped + rebuild: the
mobile `/` scan's GATE 1 FAILED with `button-name` ("Buttons must
have discernible text", 1 node — the burger) on ALL SIX mobile routes
while the desktop scans stay green — **the extension's raison
d'être: a desktop-only gate can never catch a nameless burger
(it's md:hidden at desktop)**. Restored → GREEN. Mutation (b) — the
sheet's DialogTitle removed + rebuild: the sheet-open test FAILED
exactly at the `aria-labelledby` pin (Received: null). Restored →
GREEN. `git diff src/` — ZERO production-code changes (both
mutations restored byte-identically). Lint clean (the one warning in
my new probe script's dead expression fixed).

**Step 8 — the full chain re-run.** 108/108 unit ✓ · lint ✓ ·
typecheck ✓ · build ✓ · **195/195 e2e ✓** (187 → 195: the 8 mobile
a11y tests) · 35/35 smoke ✓.

**Step 9 — the probe README + screenshots.** The v39 section
appended (5 lessons: the wedged agent-browser daemon + the pkill
restart; the sr-only-named burger; the document-wide nav query trap
on mobile; the reference's toast-blocked burger needing the
JS-click; the playwright -g paren regex). The 16 screenshots
regenerated via `node scripts/capture-screenshots.mjs`. Probe
lessons folded into AGENTS.md/the SKILL doc too.

**Step 10 — docs aligned + shipped.** README (the 195 counts + the
v39 table row), CLAUDE.md (the counts + the mobile-gate e2e entry),
AGENTS.md (the v39 paragraph — the two gates at mobile + the
structural pins + the stripped-burger lesson), the SKILL doc (the
state line + the Session 74 row), this formal log, the repo worklog
(Session 73, newest-first), the workspace worklog. Commit + push to
`main` via the SSH wrapper runbook (`docs/ssh_git_wrapper_v3.py`,
the key materialized to ~/.ssh/, fingerprint verified, the wrapper
dry-run then the real push, the key shredded after).

**What this session delivered:**

- **The a11y gate's MOBILE extension shipped (the session-80/81
  queue item)** — the two-gate axe scan extended to the 390×844
  mobile viewport: the six authed routes sheet-closed, the sheet-OPEN
  state, and the logged-out mobile login (8 new e2e)
- **The headline structural superset measured + pinned**: the
  reference's mobile sheet is a plain div (no role, no labelledby, no
  nav, no title); the clone's is the fully accessible Radix Dialog
  (role=dialog + labelledby → the "Navigation" title + the
  `<nav aria-label="Primary">` + the named burger)
- **The stripped-burger mutation proves the extension's worth** —
  button-name fires on all six mobile routes while every desktop
  scan stays green (the burger is md:hidden at desktop)
- **Standing checks clean (33rd consecutive)** — mobile-nav R1–R4 on
  both sites (**Tailwind v4 pins hold, the mobile menu works**), data
  drift (reference read-only, verified before + after), the SEO pair,
  one VLM pair (the mobile sheet-open state — both flags explained)
- **108/195/35 green** (8 new e2e, zero production-code changes,
  TDD with both pin-sanity mutations verified to FAIL)

**Suggested next steps**: the dashboard quick-action Add Item's
focus walk (the last unmeasured surface from the session-78 queue);
or the net-worth summary card's gradient chip at the /savings-class
viewports; or re-issue the brief referencing `docs/session_83.md` /
`docs/remediation-plan-v39.md` and I'll pick from the queue.
