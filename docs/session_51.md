# Session 51 — Parity iteration v25 (session-49 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_49.md` / `docs/remediation-plan-v24.md`
/ `worklog.md` / `docs/session_50.md`. Full autonomy granted on the open
questions, so I worked the whole chain directly.

**Step 1 — workspace refresh.** `git pull` fast-forwarded to `e7109fd`
(bringing in `docs/session_50.md`); the environment survived the session
boundary intact (`.env` with `DATABASE_URL="file:../db/custom.db"`, `db/`
at the repo root, node_modules, Vitest/Playwright configs, sitemap/robots
prerendering, `.env.example` — all re-verified). The five project docs +
four session docs re-read; the codebase validated against them (scandihaven
unchanged at `d4789c3`, patterns already reflected).

**Step 2 — the audit.** The baseline chain green on the first run: lint ✓
· typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**150/150 e2e** ✓ · 35/35 smoke ✓. Audit Phase 2 clean: the same 5
dev-only ESLint `braces` advisories (no patched release — accepted),
the secret scan matching only the documented prompt-history/placeholder
files, and the v24 changeset (`4badb7b`) re-reviewed — clean, commented,
test-pinned. One false alarm during the audit — a suspected syntax error
in login-card.tsx was the DISPLAY pipeline stripping the literal
bracket+m sequence from rendered text (lesson 44; tsc + build were green
the whole time; verified byte-level with charCodeAt).

**Step 3 — the two-site sweep** (agent-browser on the ONE shared tab +
the :3200 parity server; the fresh open+settle discipline throughout):

- **Mobile navigation (the task focus) R1–R4 all re-verified live — the
  19th consecutive check.** R1: the reference's two `fixed top-0 z-[100]`
  toast containers still intercept the burger's center hit (pe:auto,
  390×32, z-100; scrollWidth 395 on `/`), while the clone's burger hit is
  DIRECT on the svg with the viewport `pe:none` and 390 fit on every
  route. R2: the reference's sheet still traps after nav
  (`sheetStillOpen: true`); the clone's closes (superset fix #2) — sheet
  288px + Income link (20,185) 247×32 identical. R3: the reference marks
  nothing active on `/` (rgb(63,63,70)/400, no nav landmark); the clone
  highlights Dashboard (superset #3). R4: the reference overflows 395 on
  `/`+`/dashboard` and 464 on `/networth`; the clone fits 390 on all six
  routes. **The Tailwind v4 pins hold — the clone's mobile menu works as
  expected.**
- **Data drift clean (19th)**: the reference unchanged (allocation 30.5%,
  Balance $3475.00, income $5000/1, savings $1000/1, expenses $525/4).
- **SEO pair ✓**: both sites serve robots.txt (allow-all + sitemap link)
  and sitemap.xml (five URLs, `/login` excluded).
- **v24 G1+G2 re-verified live**: the auth census re-run on both sites at
  390×844 — the clone renders the reference's exact three-family table
  (signin 44/16, signup 40/14, forgot 40/16, gaps 10, relMt 6).
- **The sm breakpoint (session-48 suggestion 1, first measurement)**: the
  census at 672×800 on both sites — EXACT match on every axis, including
  the sign-up font's 16px middle step. The v24 ladder verified at the
  third viewport. No finding.
- **The keyboard focus-ring sweep (session-48 suggestion 2, first
  measurement — three REAL findings)**: a REAL-Tab walk over every
  focusable on both sites' login pages found the reference runs DISTINCT
  ring families per component: the auth SUBMIT renders
  `focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2`
  with `--ring` = **zinc-950 #09090b** (the clone had the INPUTS'
  slate-400 #94a3b8 on it — G1); the 404 "Go Home" button runs plain
  `focus:` with **slate-500 #64748b** (the clone had keyboard-gated
  slate-400 — G2); and the reference's `<body>` styles NO background
  (the browser's white canvas, the warm #fafaf8 paper painted on the
  app-shell wrapper) where the clone painted the paper on the body
  (G3 — computed-style level; visually invisible, every page covers the
  body; the regenerated screenshots are byte-identical). The Google +
  swap buttons' browser-default outlines match; the reference's seventh
  focus stop is the Base44 PLATFORM edit badge, not app chrome. The VLM
  pair returned IDENTICAL — correct on the background (the identical
  full-viewport gradient covers it) and blind on the rings
  (keyboard-focus chrome is unphotographable in rest-state shots).

**Step 4 — the plan + TDD.** `docs/remediation-plan-v25.md` written and
validated against the codebase (grep-verified scopes: the `ring-[#94a3b8]`
family's three hits, `--color-background`'s single consumer, the
`--neutral-warm` token's dead status, no existing ring/body pins). Four
tests written RED first (the submit ring in both auth states, the login
body's white canvas, the 404 ring after plain focus, the shell's warm
paper over a white body) → all four RED as expected → the three fixes
(the two `ring-[#09090b]` submit lines; the 404's `focus:` family
verbatim; `--color-background: #ffffff` + the shell's
`bg-(--neutral-warm)`) → GREEN 4/4 → pin-sanity mutations (the ring
colors and the body white mutated to the old values) all RED → restored
→ GREEN. The e2e flaked once mid-chain (the 404 navigation test, passing
in isolation and on both full re-runs — a one-off; the final full-chain
run is clean).

**Step 5 — the chain.** **FULL CHAIN GREEN: 108 unit · 154 e2e (4 new) ·
35 smoke** + lint + typecheck + build. The screenshots regenerated —
byte-identical (PIL pixel-verified: the body's fix is covered by the
identical login gradient on every page, exactly as measured). The G3
narrative in the plan/specs amended for that accuracy (computed-style
fix, zero visual change).

**Step 6 — docs + ship.** README (counts + the v25 row), CLAUDE.md (the
E2E list + the Tailwind ring-family lesson), AGENTS.md (the v25 pin
paragraph), the SKILL (state + the session row + lessons 43/44), the
probe README (the v25 catalog), this session log, the worklog. Committed
and pushed to `main` through the SSH wrapper.

## What this session did

- **Workspace refreshed** (`e7109fd`), full doc chain re-read, all
  standing brief requirements re-verified in place
- **Baseline fully green on the first run** — 108/150/35; the audit clean
  (the same 5 dev-only advisories, no secrets, the v24 changeset clean)
- **Standing checks all clean**: mobile-nav R1–R4 (19th — Tailwind v4
  pins hold), data drift (19th), the SEO pair, the v24 fixes re-verified
  live at mobile + the sm band (the sign-up font's 16px middle step)
- **Three REAL fixes from the first keyboard-focus-ring sweep** (TDD,
  pin-sanity-mutated, live re-verified with REAL Tab presses): the auth
  submits' zinc-950 ring (G1), the 404's plain-focus slate-500 ring (G2),
  and the body's white-canvas/shell-paper layering (G3 — computed-style
  parity, byte-identical screenshots)
- **Two probe lessons**: programmatic `focus()` in agent-browser evals
  never engages `:focus`/`:focus-visible` (REAL Tab presses are the only
  reliable mechanism — lesson 43); the tool-result display pipeline
  strips the literal bracket+m sequence from rendered text (lesson 44 —
  verify suspected source corruption with charCodeAt first)
- Full chain now **108/154/35 green**; docs/screenshots/worklog aligned;
  committed and pushed to main via the SSH wrapper

**Suggested next steps**: the reference's 5-attempts-exhausted lockout
remains the standing unmeasurable (burning the account's verification
attempts); otherwise a mouse-focus (`focus:` vs `focus-visible:`)
behavioral sweep of the app's DIALOG buttons (the v19 family is
focus-visible-gated in the clone — the reference's dialog buttons were
measured via `focusVisible:true` probes, so their click-focus behavior
may warrant a live Tab-vs-click pair), or an aria/landmark audit of the
verify-email state's inputs (never swept as a focus surface).
