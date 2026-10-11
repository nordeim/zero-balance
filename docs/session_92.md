# Session 92 — Parity iteration v42 (session-90/91 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_90.md` /
`docs/remediation-plan-v41.md` / `worklog.md` / `docs/session_91.md`.
Full autonomy granted on the open questions, so I worked the whole
chain directly.

**Step 1 — workspace refresh.** The local workspace SURVIVED the
session break: `git pull origin main` fast-forwarded `3f89e53` →
`d5068c8` (the session_91 log commit). The environment verified
intact in place: node_modules, `.env`
(`DATABASE_URL="file:../db/custom.db"` — the db/ folder at the repo
root, exactly as the brief specifies, `db/custom.db` + `db/e2e.db`
present), playwright chromium. The latest docs confirmed in place:
session_90.md, session_91.md, remediation-plan-v41.md, worklog.md.

**Step 2 — docs review.** The five project docs (AGENTS, CLAUDE,
README, PAD, SKILL) re-read via a review pass; the v41 changeset
verified in place (the two `mb-8` rhythm fixes + the two census
describes + the a11y route extension — the git diff re-audited: exactly
the documented 3-file changeset, nothing else). The session_90/91
transcripts reviewed — the v41 state: 108/203/35 green, the queue for
this session: **the mid-viewport (640) census of the OTHER five
routes** (the v41 lesson: an unmeasured viewport class is as dangerous
as an unmeasured surface), the summary card's hover/interaction
states, or a fresh surface of choice. The skills/ catalog consulted
(clone-app-pat-pro, agent-browser, tdd, tailwind-patterns,
nextjs16-tailwind4, evidence-driven-testing) — skills/ excluded from
code checking, testing and compilation throughout, as the brief
specifies.

**Step 3 — baseline chain.** Lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · **203/203 e2e ✓ (4.7m, the
FIRST run, zero flakes)**. The audit: npm audit = the same 5 dev-only
ESLint `braces` advisories (accepted, unchanged, dev-only), the
secret-pattern scan clean, `.env` byte-identical to `.env.example`
(the SQLite `DATABASE_URL="file:../db/custom.db"` resolving against
prisma/schema.prisma, the db/ folder at the repo root — verified
against `src/lib/db-path.ts` + `tests/db-path.test.ts`).

**Step 4 — the 36th standing checks.** The reference side
(ref-v40.sh, one foreground invocation): R1 the toast-blocker still
intercepts the burger's center hit (scrollW 395); R2 the sheet still
traps after nav; R3 no landmark + no active highlight on /; R4 the 395
overflows on / + /dashboard; the census before AND after unchanged
(30.5% / 5000 / 1000 / 525 — read-only held); the SEO pair live; the
mobile sheet still the plain fixed div. The clone side
(clone-v40.sh inside with-server.sh): R1 the direct svg hit 390, R2
the sheet closes, R3 the nav landmark, R4 zero overflows, the census
unchanged (62.8% / 5550 / 1250 / 2235), the SEO pair live, the
sheet-open structure re-proven (role=dialog + labelledby → the sr-only
"Navigation" + nav aria-label="Primary" + the five links + the named
burger). **The Tailwind v4 pins hold — the mobile menu works on both
sites.**

**Step 5 — the v42 surface (the queue item).** The five non-networth
routes (/, /dashboard, /income, /expenses, /savings) measured live on
BOTH sites at 640×960 (mid-census-v42.mjs, the v41 census idiom
ported): **the 32px rhythm HOLDS on all five routes** (gapRowToFirst
=== 32 everywhere — the page-header row's mb-8, the v20 G1 pin's class
extended to the mid viewport), the header 61px, the h1 30px/36, the
cap 608 (640 − 2×16), sw 640 (no overflow on either site), the
items-view routes fully matching (the filter card y=221 h=190/242
mb-24 block, the item grid 1-col 16px gap). **THE FINDING: the
dashboard's firstSection (the hero grid) ran 677 vs the reference's
664 (+13).** The attribution (hero-attrib-v42.mjs): the goalCard
byte-identical (316, the bands 48/48/108, the donut 558×300), the
drift isolated to the breakdownCard (324 vs 337) — then
bd-attrib-v42.mjs band-by-band: **the clone rendered TWO Dividers
(Income|Savings AND Savings|Expenses), the reference ONE (Income|
Savings only)** — the extra 12+1px band = the +13. The same delta at
1280 (377 vs 364, the rows 56/64/64 wrapping identically on both
sites — width-driven, not data-driven). The tail-v42.mjs control: the
lastBand mb=0 on both sites (no trailing-margin class), scrollH 3029
vs 3042 — **exactly the +13, the divider alone**. The reference's
structure reads as the app's ONE rule grouped: [Income] | [Savings,
Expenses] | border-t | [Net Balance].

**Step 6 — the remediation plan v42** written and pre-validated
against the codebase (the `i > 0` target at dashboard-view.tsx:410,
the v41 census-test idiom as the pattern source, the a11y
route-extension for-loop for the five-route test, the measured pin
values from the probes) — saved as
`docs/remediation-plan-v42.md`.

**Step 7 — TDD.** RED first: the three census tests written and run
against the unfixed build — all three FAILED at exactly the expected
pins (the band-count 6 ≠ 5; the card 377 ≠ 364; the hero 677 ≠ 664;
the scrollH 3042 ≠ 3029; the rhythm pins on the loop routes). The F1
fix applied: `{i > 0 && <Divider />}` → `{i === 1 && <Divider />}`
(one condition + the measured-evidence comment). Rebuild → GREEN (all
three first-run).

**Step 8 — pin-sanity mutations.** Three mutations, each verified to
FAIL then restored: (a) the reverted divider condition → the
band-count pin fails (6 ≠ 5, card 377); (b) the items-view header row
`mb-8` → `mb-6` → the /income rhythm pin fails (24 ≠ 32); (c) the
dashboard header row `mb-8` → `mb-6` → the / rhythm pin fails. The
final src diff: the 1-line condition + the comment.

**Step 9 — the full chain.** Lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **206/206 e2e ✓ (4.7m — 203 → 206)** · 35/35 smoke ✓. The 16
screenshots regenerated. The standing VLM pair (the desktop dashboard
post-fix, vlm-compare-v42.mjs): all three flags in the known classes
(the Dashboard-highlight superset #3, the allocation-% seed data, the
avatar letter) — no new drift; the divider fix itself drew no flag.

**Step 10 — docs aligned.** The probe README's v42 section (the four
probes + the VLM script + the lessons), README (the 206 counts + the
v42 table row), CLAUDE.md (the counts + the census entry), AGENTS.md
(the v42 paragraph), the SKILL doc (the state line 206 + the Session
77 row), this formal log, the raw transcript (session_93.md, the
follow-up commit), the repo worklog (Session 76), the workspace
worklog.

**Step 11 — ship.** The commit staged and pushed to main via the SSH
wrapper (`docs/ssh_git_wrapper_v3.py` + the runbook), the operator key
shredded after the push.

## What this session delivered

- **The mid-viewport census of the five non-networth routes shipped**
  — the v41 lesson applied to the remaining route set; the 32px rhythm
  class verified holding on every route at 640×960
- **THE SINGLE-DIVIDER FIX — the first production-code change since
  v41**: the NetZeroBreakdownCard's extra Savings|Expenses divider
  removed (the +13px at both viewports; every band below the hero
  shifts back; scrollH joins the reference at 3029) — TDD with the
  RED-first census pins
- **3 new e2e (203 → 206), three pin-sanity mutations verified to
  FAIL** — 108/206/35 green
- Standing checks clean (36th): mobile-nav R1–R4 both sites (Tailwind
  v4 pins hold, the mobile menu works), data drift (reference
  read-only, before + after), the SEO pair, the VLM pair

**Suggested next steps**: re-issue the brief referencing
`docs/session_92.md` / `docs/remediation-plan-v42.md` — the queue
holds the summary card's hover/interaction states, the drill-down
EXPANDED-state census (the divider fix's collapsed-state pin now
exists; the expanded categories/subcategories bands are unmeasured at
the mid viewport), or a fresh surface of your choosing.
