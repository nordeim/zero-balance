# Session 89 — Parity iteration v41 (session-87/88 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_87.md` /
`docs/remediation-plan-v40.md` / `worklog.md` / `docs/session_88.md`.
Full autonomy granted on the open questions, so I worked the whole
chain directly.

**Step 1 — workspace refresh.** The local workspace SURVIVED the
session break: `git pull origin main` fast-forwarded `5b0a6f3` →
`009453c` (the session_88 transcript commit). The environment verified
intact in place: node_modules, `.env`
(`DATABASE_URL="file:../db/custom.db"` — the db/ folder at the repo
root, exactly as the brief specifies, `db/custom.db` + `db/e2e.db`
present), playwright chromium. The latest docs confirmed in place:
session_87.md, session_88.md, remediation-plan-v40.md, worklog.md.

**Step 2 — docs review.** The five project docs (AGENTS, CLAUDE,
README, PAD, SKILL) re-read; the v40 changeset verified in place (the
dashboard Tab-order census test + the interactive stat-card superset
pins + the probe-README lessons). The session_87/88 transcripts
reviewed — the v40 state: 108/196/35 green, the queue for this
session: **the net-worth summary card's gradient chip at the
savings-class viewports**, or the a11y gate's sheet-open scan
extension to the remaining five routes. The skills/ catalog consulted
(clone-app-pat-pro, agent-browser, tdd, the Tailwind v4 skills) —
skills/ excluded from code checking, testing and compilation
throughout, as the brief specifies.

**Step 3 — baseline chain.** Lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · **196/196 e2e ✓ (4.5m, the
FIRST run, zero flakes)**. npm audit: the same 5 dev-only ESLint
`braces` advisories — accepted, unchanged. The secret-pattern scan
clean. `.env` verified byte-identical to `.env.example`.

**Step 4 — the two-site sweep.** The reference standing checks (35th,
`ref-v40.sh`): R1 — the toast-blocker still intercepts the burger's
center hit (DIV.fixed.top-0.z-[100], scrollWidth 395); R2 — the sheet
still traps after nav (sheet open, body locked on /income); R3 — no
nav landmark on `/`, no active highlight; R4 — the 395px overflows on
`/`+`/dashboard`. The census before AND after all probes unchanged
(allocation 30.5%, income $5000.00, savings $1000.00, expenses
$525.00 — read-only held). The SEO pair live (robots allow-all + the
sitemap). The reference's mobile sheet re-measured: still the plain
fixed div (no role, no labelledby, no nav, no title). The clone side
(`clone-v40.sh` inside `with-server.sh`): R1 the DIRECT svg hit 390 ✓,
R2 the sheet closes after nav ✓, R3 the nav landmark ✓, R4 zero
overflows ✓, the census unchanged (62.8% / 5550 / 1250 / 2235), the
SEO pair live, the sheet-open structure re-proven (role=dialog +
labelledby → sr-only "Navigation" + nav aria-label="Primary" + the
five links + the named burger). **The Tailwind v4 pins hold — the
mobile menu works on both sites.**

**One process discovery this session**: this sandbox REAPS background
processes between tool calls — the first two e2e/standing-check
background attempts died mid-run (the logs frozen at test 2). Every
long job (the e2e suite, the parity server) ran inside a SINGLE
invocation afterward (`with-server.sh`); the agent-browser daemon and
its logged-in sessions survive between calls.

**Step 5 — the v41 surface.** The queue's savings-class viewports
item, interpreted as the unmeasured MID viewport class (640×960 — the
`sm:` breakpoint where the summary card's `sm:text-5xl` and
`sm:grid-cols-2` activate; the existing pins cover 390 and 1280 only).
The probe battery written and run on BOTH sites at 390×844, 640×960
AND 1280×800 (`nw-summary-v41.mjs` + `nw-yoffset-v41.mjs` +
`nw-below-v41.mjs`):

- **At 640: FULL geometry parity** — the 608×333 card (p-8, radius 16,
  the forest→lime gradient, the `rgba(26,58,46,0.3) 0 20 60` shadow),
  the 48px/700 figure, the 64×64 white/20% gradient chip at x=528
  (9999px radius, the 32px icon), the 264×2 stats grid (16px gap, 84px
  cells), the 18px ratio, the 48@x=16 header chip, the 256/0.1
  overlay, the 448×36 tabs, the 144px tabs→grid gap, sw=vw on both.
- **THE v41 PARITY GAP (the first production-code change since v38)**:
  the net-worth page's section rhythm runs `mb-6` (24px) where the
  reference runs `mb-8` (32px) at BOTH gaps — the header row→card
  (`net-worth-view.tsx:292`) and the card→tablist (`:308`) — 8px
  offsets at every viewport (card y: 124 vs 116 at 1280, 169 vs 161 at
  640). The y-offset probe attributed the delta in ONE run: the stack
  above (the 61px mobile header, the 60px chipRow, the 36px h1 at
  30px, the 24px subtitle) and below (the 448×36 tabs, the 144 gap)
  match byte-for-byte — only the two margins disagree. The
  items-view control probe (`items-rhythm-v41.mjs` on /income) proved
  the net-worth was the ONE outlier: the items-view rhythm is
  identical on both sites (the v20 G1 mb-8 + the reference's own
  filter-card mb-6).
- **The mobile superset pair re-measured at the card level (390)**:
  the reference's card is 432px wide at the 390 viewport — 74px page
  overflow (sw=464), its figure a fixed 48px, its stats grid a fixed
  2-col (the second cell's right edge 416), its 64×64 chip at x=352
  (26px past the viewport). The clone's fits: the 358 card (sw=390),
  the 24px figure (`text-2xl` — superset fix #6), the 1-col grid, the
  chip fully inside (x=278) — with byte-identical card chrome (the
  gradient, the radius, the padding, the shadow, the chip specs, the
  84px cells, the 18px ratio, the overlay).
- **The reference's demo data on /networth**: net $25,000.00, ratio
  ∞:1 (debt-free) vs the clone's seed −$245,950.00 / 0.21:1 — the
  documented demo-dataset difference.

**Step 6 — the remediation plan.** `docs/remediation-plan-v41.md`
written and pre-validated against the codebase (the two mb-6 targets,
the v14 mobile-chip describe's `test.use` pattern as the census-port
source, the v39 sheet-open structure-evaluate as the route-extension
source, the seed arithmetic for the figure/ratio pins, the
scroll-independent relative-gap rhythm pins).

**Step 7 — TDD execution.** The 640 census test written FIRST and run
RED against the unfixed build (the rhythm pin failed at exactly
`headerToCard` 24 ≠ 32). The F1 fix applied (the two `mb-6` → `mb-8`
in `net-worth-view.tsx`, with the measured-evidence comments) →
rebuilt → **GREEN** (the 640 census + the 390 superset census, both
first-run). The F4 a11y route extension written (5 tests: the
sheet-open structural pins + the Escape close on /dashboard, /income,
/expenses, /savings, /networth) → **GREEN** (all 5 first-run). Four
pin-sanity mutations verified to FAIL: (a) the reverted `mb-8` → the
rhythm pin fails; (b) the stripped `sm:text-5xl` → the 48px pin
fails; (c) the fixed `grid-cols-2` → the 390 1-col pin fails; (d) the
stripped DialogTitle → all five route tests fail. All restored →
GREEN. The final src diff: the 2-line production fix + the comments.

**Step 8 — the full chain re-run.** Lint ✓ · typecheck ✓ · 108/108
unit ✓ · build ✓ · **203/203 e2e ✓ (4.7m — 196 → 203: +2 networth
census, +5 a11y route extension)** · 35/35 smoke ✓. The 16
screenshots regenerated (the mb-8 rhythm visible in 06-networth.png
and 12-mobile-networth.png).

**Step 9 — docs aligned.** The probe README's v41 section (4 lessons);
README (the 203 counts + the v41 table row); CLAUDE.md (the counts +
the net-worth census entry + the a11y route-extension entry);
AGENTS.md (the v41 paragraph, newest-first); the SKILL doc (the
project_state 203 + the Session 76 row); this formal log; the repo
worklog (Session 75, newest-first); the workspace worklog.

**Step 10 — commit + push.** The changeset committed to main and
pushed via the SSH wrapper runbook (`docs/ssh_git_wrapper_v3.py`, the
`docs/how-to-git-push-using-ssh-wrapper_SKILL.md` instructions — the
key materialized to a 600-mode file, the fingerprint verified, the
dry-run, the real push, the remote verified, the key shredded).

## What this session delivered

- **The net-worth summary card's viewport census shipped** (the
  savings-class viewports queue item): the first MID-viewport (640)
  measurement of the project — FULL geometry parity found and pinned
- **THE VERTICAL-RHYTHM FIX (the first production-code change since
  v38)**: the net-worth page's two 24px section gaps corrected to the
  reference's 32px (`mb-6` → `mb-8` at the header row and the summary
  card), pinned by the two rhythm pins in the 640 census
- **The mobile superset pair pinned at the card level**: the
  reference's 432px card (74px overflow, the offscreen chip, the fixed
  2-col grid) vs the clone's fitting 358px card — the superset class
  with byte-identical chrome
- **The a11y sheet-open structural pins extended to the remaining
  five routes** (the second queue item — the v39 `/`-only test now
  covers every authed route)
- **7 new e2e (196 → 203), four pin-sanity mutations verified to
  FAIL** — 108/203/35 green
- Standing checks clean (35th): mobile-nav R1–R4 both sites (Tailwind
  v4 pins hold, the mobile menu works), data drift (reference
  read-only, before + after), the SEO pair

**Suggested next steps**: re-issue the brief referencing
`docs/session_89.md` / `docs/remediation-plan-v41.md` — the queue
holds the mid-viewport (640) census of the OTHER five routes (the
items-views and the dashboard — the v41 lesson: an unmeasured viewport
class is as dangerous as an unmeasured surface), the summary card's
hover/interaction states, or a fresh surface of your choosing.
