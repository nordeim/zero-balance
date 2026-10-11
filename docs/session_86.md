# Session 86 — Parity iteration v40 (session-84/85 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_84.md` /
`docs/remediation-plan-v39.md` / `worklog.md` / `docs/session_85.md`.
Full autonomy granted on the open questions, so I worked the whole
chain directly.

**Step 1 — workspace refresh.** The local workspace SURVIVED the
session break: `git pull origin main` fast-forwarded `6e75f2b` →
`8a7a3b4` (the session_85 transcript commit). The environment verified
intact in place: node_modules, `.env`
(`DATABASE_URL="file:../db/custom.db"` — the db/ folder at the repo
root, exactly as the brief specifies, `db/custom.db` + `db/e2e.db`
present), playwright chromium. The latest docs confirmed in place:
session_84.md, session_85.md, remediation-plan-v39.md, worklog.md.

**Step 2 — docs review.** The five project docs (AGENTS, CLAUDE,
README, PAD, SKILL) re-read; the v39 changeset verified in place (the
8-test mobile a11y gate + the sheet-open structural pins + the
probe-README lessons). The session_84/85 transcripts reviewed — the
v39 state: 108/195/35 green, the queue for this session: **the
dashboard quick-action Add Item's focus walk** (the session-78
queue's LAST unmeasured surface), the net-worth summary card's
gradient chip at the savings-class viewports, or the a11y gate's
sheet-open scan extension. The skills/ catalog consulted
(clone-app-pat-pro, agent-browser, tdd, the Tailwind v4 skills) —
skills/ excluded from code checking, testing and compilation
throughout, as the brief specifies.

**Step 3 — baseline chain.** Lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · **195/195 e2e ✓ (4.5m, the
FIRST run, zero flakes)** · 35/35 smoke ✓. npm audit: the same 5
dev-only ESLint `braces` advisories — accepted, unchanged. The
secret-pattern scan clean. `.env` verified byte-identical to
`.env.example`.

**Step 4 — the two-site sweep.** The reference standing checks (34th,
`ref-v39.sh`): R1 — the toast-blocker still intercepts the burger's
center hit (DIV.fixed.top-0.z-[100], scrollWidth 395); R2 — the sheet
still traps after nav (sheet open, body locked on /income); R3 — no
nav landmark on `/`, no active highlight; R4 — the 395px overflows on
`/`+`/dashboard`. The census before AND after all probes unchanged
(allocation 30.5%, income $5000.00, savings $1000.00, expenses
$525.00 — read-only held). The SEO pair live (robots allow-all + the
sitemap; the reference's capitalized /Income /Savings URLs still
documented). The clone-side standing checks (34th, `clone-v39.sh`
inside with-server.sh): R1 direct svg hit 390; R2 the sheet closes
after nav (superset #2); R3 the nav landmark; R4 zero overflows; the
census 62.8% / 5550 / 1250 / 2235 (the seed unchanged); the mobile
sheet structure re-proven (role=dialog + the sr-only Navigation title
+ nav aria-label="Primary" + the named burger). **The Tailwind v4
pins hold — the mobile menu works as expected on both sites.**

**Step 5 — the v40 surface (the dashboard's Tab-order focus walk —
the session-78 queue's last unmeasured surface), measured live on
BOTH sites** (`tabwalk-v36.sh` — the REAL-Tab walk, 22 presses, both
sites + `focus-census-v40.mjs` — the clean DOM-order focusable
census + `stat-card-chain-v40.mjs` — the text-ancestor chains +
`donut-focused-dump-v40.mjs` — the donut stop's structure):

- The REFERENCE's cycle (14 focusable stops, doc order): the five
  nav links → the Add Item header button → the three
  NetZero-breakdown stat-row buttons (real `button` elements at
  x=961, w=254) → the donut's `g.recharts-pie` (tabindex=0, its
  textContent carrying the sector labels "92.3%4.6%3.1%") → the
  three quick-action card buttons → the Base44 "Close badge"
  (platform chrome) → wrap.
- The CLONE's cycle (16 stops): the SAME walk — nav(5) → Add Item →
  the three stat-row buttons → **PLUS the three interactive stat
  cards** (`div[role="button"][tabindex="0"]` at [288/616/944,
  304×210]) → the donut's `g.recharts-pie` tabindex=0 (empty
  textContent — recharts 3 renders the labels in a separate layer;
  the visible chrome identical, VLM-clean) → the three quick-action
  cards → wrap to the body. The platform badge correctly absent.
- THE HEADLINE SUPERSET: the reference's BIG stat cards (the 304×210
  row, visually identical to the clone's) are **INERT divs** — no
  role, no tabindex, no handler (the stat-card-chain probe bottoms
  out at a plain grid div). The clone's are `div[role=button]` +
  `tabIndex=0` + Enter/Space handlers routing to the type view —
  the same dead-UI-fixed superset class as the kebab focus reveal
  (#7): the reference shows interactive-LOOKING cards (hover shadow
  + cursor) that do nothing.
- The donut stop matches structurally on both sites: the pie layer
  g carries tabindex=0 on both, the sector paths
  (path.recharts-sector, name=Need/Savings/Want) carry tabindex=-1
  (the v31 roving), the svg surface is inert on both — the v31
  replication confirmed at the walk level. The clone's svg adds
  recharts-3's zIndex-layer groups (library internals, invisible).
- The geometry bands: the nav links, Add Item, the stat-row buttons'
  x=961/w=254, the stat cards' 304×210, and the quick actions'
  304×90 all sit at the reference's positions within a 13px vertical
  band drift that starts at the reference's third stat-row button —
  the reference's own column gaps are inconsistent (25px then 12px)
  while the clone's are a consistent 25px (a reference quirk, both
  surfaces VLM-clean).
- The VLM pairwise (one fresh pair, 1280×800): the desktop
  dashboard — VERDICT DIFFERENT with ALL THREE flags explained: (1)
  the clone's Dashboard link carries the active highlight (superset
  fix #3 — the reference marks nothing active on `/`, its R3 bug);
  (2) the Budget Allocation progress bar length (the different demo
  data: 62.8% vs 30.5%); (3) the avatar letter D vs U (the different
  demo users). Zero unexplained visual drift.

**Step 6 — the remediation plan.**
`docs/remediation-plan-v40.md` written and pre-validated against the
codebase (the insertion point after the donut keyboard contract, the
mutation targets in dashboard-view.tsx, the seed arithmetic, the
readStop idiom) before any execution: F1 the Tab-order census (1
test), S1 two pin-sanity mutations, T2 the probes + the README
section.

**Step 7 — TDD execution.** The census test appended to
`tests/e2e/dashboard.spec.ts` (the 16 REAL-Tab stops with tag + role
+ accessible name + tabindex, the nav geometry bands, the per-class
  x/w/h bands, the wrap, and the superset activation pair — Enter on
the focused Total Income card routes to /income, Space on Total
Savings routes to /savings). **GREEN on the first run (9.6s).**
Mutation (a) — the StatCard's `role="button"` + `tabIndex={0}`
stripped + rebuild: the census FAILED exactly at the stat-card stops
(the Tab skipped straight to the donut g — the divs dropped out of
the walk). Restored → GREEN. Mutation (b) — the StatCard's
Enter/Space handler removed + rebuild: the activation pin FAILED
(Enter no longer routes — **the mutation literally reproduces the
reference's dead-UI behavior and the test catches it**). Restored →
GREEN. `git diff --stat src/` — ZERO production-code changes (both
mutations restored byte-identically). Lint clean (the one warning in
my unused draft probe's dead expression — the draft deleted, the
used probes clean).

**Step 8 — the full chain re-run.** 108/108 unit ✓ · lint ✓ ·
typecheck ✓ · build ✓ · **196/196 e2e ✓** (195 → 196: the census
test) · 35/35 smoke ✓.

**Step 9 — the probe README + screenshots.** The v40 section appended
(5 lessons: the [tabindex]=-1 + zero-rect filter for recharts'
hidden zIndex layers; the text-ancestor chain as the only
inert-vs-interactive verdict; the `header button` query matching the
display:none burger first; the tabwalk's scroll artifacts — assert
x/w/h bands only; the reference's own inconsistent stat-row gaps).
The v40 standing-check scripts persisted (`ref-v40.sh` /
`clone-v40.sh`). The 16 screenshots regenerated via `node
scripts/capture-screenshots.mjs`. Probe lessons folded into
AGENTS.md/the SKILL doc too.

**Step 10 — docs aligned + shipped.** README (the 196 counts + the
v40 table row), CLAUDE.md (the counts + the census e2e entry),
AGENTS.md (the v40 paragraph), the SKILL doc (the state line + the
Session 75 row), this formal log, the repo worklog (Session 74,
newest-first), the workspace worklog. Commit + push to `main` via
the SSH wrapper runbook (`docs/ssh_git_wrapper_v3.py`, the key
materialized to ~/.ssh/, fingerprint verified, the wrapper dry-run
then the real push, the key shredded after).

**What this session delivered:**

- **The dashboard's Tab-order focus walk shipped (the session-78
  queue's LAST unmeasured surface)** — the 16 REAL-Tab stops pinned
  with tag + role + name + tabindex, the geometry bands, the wrap,
  and the interactive stat-card superset activation (1 new e2e)
- **The headline functional superset measured + pinned**: the
  reference's big stat cards are inert dead UI (no role, no
  tabindex, no handler); the clone's are keyboard-focusable and
  Enter/Space-activated navigation cards
- **The donut stop's structural parity confirmed at the walk
  level** — the v31 replication (the pie layer tabindex=0, the
  sector roving, the inert surface) holds on both sites
- **Standing checks clean (34th consecutive)** — mobile-nav R1–R4 on
  both sites (**Tailwind v4 pins hold, the mobile menu works**),
  data drift (reference read-only, before + after), the SEO pair,
  one VLM pair (the desktop dashboard — all three flags explained)
- **108/196/35 green** (1 new e2e, zero production-code changes,
  TDD with both pin-sanity mutations verified to FAIL)

**Suggested next steps**: re-issue the brief referencing
`docs/session_86.md` / `docs/remediation-plan-v40.md` — the queue
holds the net-worth summary card's gradient chip at the savings-class
viewports, the a11y gate's sheet-open scan extension to the remaining
five routes, or a fresh surface of your choosing.
