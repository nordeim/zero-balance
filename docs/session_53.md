# Session 53 — Parity iteration v26 (session-51 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_51.md` / `docs/remediation-plan-v25.md`
/ `worklog.md` / `docs/session_52.md`. Full autonomy granted on the open
questions, so I worked the whole chain directly.

**Step 1 — workspace refresh.** `git pull` fast-forwarded to `6b46804`
(bringing in `docs/session_52.md`); the environment survived the session
boundary intact (`.env` with `DATABASE_URL="file:../db/custom.db"`, `db/`
at the repo root, node_modules, Vitest/Playwright configs, sitemap/robots
prerendering, `.env.example` — all re-verified). The five project docs +
four session docs re-read; the codebase validated against them
(scandihaven unchanged at `d4789c3`, patterns already reflected; the v25
changeset `c60cb9e` in place — the `ring-[#09090b]` submits, the 404's
plain-`focus:` family, the white body token + the shell's warm paper).

**Step 2 — the audit.** The baseline chain green on the first run: lint ✓
· typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**154/154 e2e** ✓ · 35/35 smoke ✓. Audit Phase 2 clean: the same 5
dev-only ESLint `braces` advisories (no patched release — accepted), the
secret scan matching only the documented files, and the v25 changeset
re-reviewed — clean, commented, test-pinned.

**Step 3 — the two-site sweep** (agent-browser on the ONE shared tab +
the :3200 parity server; the fresh open+settle discipline throughout):

- **Mobile navigation (the task focus) R1–R4 all re-verified live — the
  20th consecutive check.** R1: the reference's two `fixed top-0 z-[100]`
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
- **Data drift clean (20th)**: the reference unchanged (allocation 30.5%,
  Balance $3475.00, income $5000/1, savings $1000/1, expenses $525/4).
- **SEO pair ✓**: both sites serve robots.txt (allow-all + sitemap link)
  and sitemap.xml (five URLs, `/login` excluded).
- **v25 fixes re-verified live**: the reference's submit ring still
  `rgb(9,9,11) 0 0 0 4px` (REAL Tab walk, stop #4), its inputs still
  `rgb(148,163,184)`, its 404 still plain-`focus:` `rgb(100,116,139)`,
  its body bg still white; the v24 auth census re-run — the three-family
  table byte-identical (no platform drift in the auth forms).
- **The dialog-button mouse-focus pair (session-51 suggestion 1, first
  behavioral measurement — NO FINDING)**: the reference's dialog
  Cancel/Save buttons carry `focus-visible:ring-1 focus-visible:ring-ring`
  (class list read live, both buttons) — byte-identical to the clone's
  `button.tsx` base, so a mouse click shows NO ring on either site and a
  REAL Tab press renders the identical visible layers (`rgb(10,10,10)
  0 0 0 1px` + the v3 ambient). The v19 `focusVisible:true` probe
  methodology captured the correct family. (Clicking Save on an EMPTY
  form moves focus to the first invalid input via native validation on
  both sites — the empty-submit path cannot hold focus on the button;
  the class attribute is the reliable arbiter.)
- **The verify-email state's inputs audit (session-51 suggestion 2,
  first measurement — REAL FINDING G2)**: structure, geometry, and
  behavior all match (main/h2/form landmarks; 40×44 gap-6
  inputmode-numeric boxes; auto-advance; backspace clears-and-retreats;
  paste distributes to the last box) — but the reference runs
  `autocomplete="one-time-code"` on the FIRST box only and `off` on the
  other five (the standard OTP convention) while the clone carried it on
  all six. The clone's `aria-label` boxes + arrow-key navigation stay as
  documented supersets (the reference's inputs are unnamed and
  arrow-inert — measured live with real Arrow key presses).
- **The body's `antialiased` class (surfaced by the v25 re-verification —
  REAL FINDING G1)**: the reference's body class is now EMPTY ("" on
  /login, /, and the 404 — three fresh opens each,
  `-webkit-font-smoothing: auto`); the `antialiased` class v25 measured
  is GONE from the reference. The clone still rendered
  `className="antialiased"`. An A/B pixel test (the class removed via
  eval, re-shot, PIL-compared) produced byte-identical diff counts on
  this Linux Chromium — the fix is computed-style-level here (on macOS
  the reference's subpixel text is the target). The VLM login pair:
  IDENTICAL (correct — the difference is unphotographable on this
  platform).
- **Register-gate observation**: the reference's `/api/auth/register`
  started answering `400 "Security verification is required"` after ~2
  synthetic registrations this session (the first landed the verify
  state normally — the audit data above is from it). A platform
  anti-automation gate; the clone's honest devCode flow is unaffected.

**Step 4 — the plan + TDD.** `docs/remediation-plan-v26.md` written and
validated against the codebase (grep-verified scopes: `antialiased`'s
two hits, the CodeInputs' static autoComplete prop, no existing pins on
either surface). The classless-body test written RED first + the
autocomplete-distribution read extended into the verify-email chrome
test (no new register-class call — the budget stays at 5 + the
login-parity 409) → both RED as expected → the two fixes (the classless
`<body>` in layout.tsx; the conditional `autoComplete` in CodeInputs) →
GREEN → pin-sanity mutations (the old class name + the old
first-box value) both RED → restored → GREEN. (One measurement stumble:
the first mutation run's `tail -2` truncation hid the failure summaries —
the rerun with full output confirmed both mutations FAIL as required.)

**Step 5 — the chain.** **FULL CHAIN GREEN: 108 unit · 155 e2e (1 new,
1 extended) · 35 smoke** + lint + typecheck + build. The screenshots
regenerated — byte-identical (git-clean; both fixes are
computed-style/attribute-level, exactly as the A/B pixel test predicted).

**Step 6 — docs + ship.** README (counts + the v26 row), CLAUDE.md (the
E2E list + counts), AGENTS.md (the v26 pin paragraph), the SKILL (state +
the session row), the probe README (the v26 catalog +
`probe-v26-verify-inputs.mjs`), this session log, the worklog. Committed
and pushed to `main` through the SSH wrapper.

## What this session did

- **Workspace refreshed** (`6b46804`), full doc chain re-read, all
  standing brief requirements re-verified in place
- **Baseline fully green on the first run** — 108/154/35; the audit clean
  (the same 5 dev-only advisories, no secrets, the v25 changeset clean)
- **Standing checks all clean**: mobile-nav R1–R4 (20th — Tailwind v4
  pins hold), data drift (20th), the SEO pair, the v24 auth census, the
  v25 fixes re-verified live
- **Two REAL fixes** (`docs/remediation-plan-v26.md`): the body's
  `antialiased` class removed to match the reference's now-classless
  body (G1 — computed-style parity, byte-identical screenshots), and the
  verify-email code inputs' autocomplete distribution (G2 —
  `one-time-code` on the first box only, `off` on the rest, the
  reference's measured OTP convention)
- **Suggestion 1 resolved with NO drift**: the dialog buttons' mouse-focus
  pair — both sites run the identical `focus-visible:` family; the v19
  methodology vindicated
- Full chain now **108/155/35 green**; docs/screenshots/worklog aligned;
  committed and pushed to main via the SSH wrapper

**Suggested next steps**: the reference's register "Security
verification" gate now blocks fresh verify-state probes on the reference
(the 5-attempts-exhausted lockout remains unmeasurable behind it);
candidate surfaces for the next sweep: a `prefers-reduced-motion` audit
of the sheet slide-in + spinner (never measured on either site), a
print/overscroll rendering check of the now-white body canvas (the G3/G1
layer fixes make those states deterministic), or a compositor-level
scrollbar styling comparison at the dialog's `overflow-y-auto` surfaces.
