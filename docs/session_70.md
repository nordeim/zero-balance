# Session 70 — Parity iteration v34 (session-69 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_68.md` /
`docs/remediation-plan-v33.md` / `worklog.md` / `docs/session_69.md`.
Full autonomy granted on the open questions, so I worked the whole chain
directly.

**Step 1 — workspace refresh.** `git pull` brought in the session-log
commit `3ff3d7c` (the session_69 transcript — the first pull ran before
the user pushed it; a re-pull after the user's nudge retrieved it). The
workspace otherwise survived intact from v33 — node_modules, `.env` with
`DATABASE_URL="file:../db/custom.db"`, the `db/` seed at the repo root
all re-verified; `scandihaven` (the reference-only repo) re-verified
present. The five project docs + the four session docs re-read; the
codebase validated against them — the v33 changeset in place (the
166-test suite, the code-input focus family + autoFocus, the announcer
pin), verified by the full chain below.

**Step 2 — the audit.** The baseline chain green on the FIRST full run:
lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap
prerendered) · **166/166 e2e ✓** · 35/35 smoke ✓. Audit Phase 2 clean:
the same 5 dev-only ESLint `braces`/eslint-config-next advisories (no
patched release — accepted, dev-only), the secret-pattern scan matching
only the documented files, `.env.example` verified current.

**Step 3 — the two-site sweep** (agent-browser on the ref34/clone
sessions + the :3200 parity server; the fresh-open + settle +
parked-pointer + real-click/real-hover/real-Tab disciplines throughout,
plus a NEW `document.hasFocus()` gate before every `:focus`-computed
read — lesson L1 below):

- **Mobile navigation (the task focus) R1–R4 all re-verified live on BOTH
  sites — the 28th consecutive check.** R1: the reference's `fixed
  top-0 z-[100]` toast containers still intercept the burger's center
  hit (scrollWidth 395), while the clone's burger hit is DIRECT on the
  svg with 390 fit on every route. R2: the reference's sheet still traps
  after nav (structure detector on `/income`: sheet open, body locked);
  the clone's closes (superset fix #2). R3: the reference marks nothing
  active on `/` and has no `<nav>` landmark; the clone highlights
  Dashboard (white/500 text + the rail) + has the landmark. R4: the
  reference overflows 395 on `/`+`/dashboard` and 464 on `/networth`;
  the clone fits 390 on all six routes. **The Tailwind v4 pins hold —
  the clone's mobile menu works as expected.**
- **Data drift clean (28th — the reference only read)**: allocation
  30.5%, Balance `$3475.00`, income `$5000.00`/1 (Salary), savings
  `$1000.00`/1 (Emergency Fund), expenses `$525.00`/4 — verified before
  and after the probe cycles (the forgot-reset probe used a throwaway
  address; the calculator/listbox probe cycles were all cancelled before
  save; the dev DB census clean at 7 items / 0 line items / 0 probe
  users).
- **SEO pair ✓** (live, both sites): robots.txt + sitemap.xml live on
  both; the full head-metadata census byte-identical; canonical +
  og:image keyed off `NEXT_PUBLIC_SITE_URL`; the reference's
  `/manifest.json` still 302s empty (broken) while the clone's
  `manifest.webmanifest` serves the v7-pinned document — a superset.
- **The forgot-password state's focus walk (session-69 suggestion #1) —
  NO finding (first-time measurement; S1 pin).** The reference's state
  (a STATE on `/login`): 368×44 controls, radius 12px, NO auto-focus on
  landing, exactly THREE app stops (Back to sign in → Email → Send
  reset link), then the exit to the page. The focus families,
  REAL-Tab-measured on both sites: the email input = the v13 SLATE
  family (white 2px + slate 4px + the tinted `#94a3b8` border), the
  submit = the v25 ZINC family (white 2px + zinc 4px + ambient), the
  Back button = the browser-default `outline: auto` (raw) — every
  family byte-identical. The post-submit state: the reference's "Check
  your email" confirmation vs the clone's honest no-mail variant (the
  documented v12 G4 superset, already pinned).
- **The calculator frequency Select's listbox keyboard contract
  (suggestion #2) — NO finding (first-time measurement; S2 pin).** Both
  sites' Frequency control is the same Radix combobox family:
  `role=combobox` + `aria-controls` → the listbox, the same 6 options
  in the same order (One-time, Weekly, Bi-weekly, Monthly, Quarterly,
  Annually). The contract: fresh-open focuses the SELECTED option which
  renders the accent highlight (`rgb(245,245,245)` bg + `rgb(23,23,23)`
  text — `:focus`-driven; the reference's older Radix also stamps
  `data-highlighted` on open, the clone's 2.3.8 after the first
  interaction — invisible either way); ArrowDown/Up rove; CLAMPED at
  both ends (no wrap); Home/End jump; NO typeahead on either site;
  Escape closes the POPUP ONLY (focus → trigger; the sub-dialog stays
  open); Enter selects (the trigger updates). The first fresh-open
  comparison FABRICATED a "the clone's selected option renders no
  highlight" finding — the **unfocused-headless-window `:focus`
  artifact** (L1): the reference read had run after REAL key presses
  (page focused), the clone read after JS clicks alone (the headless
  page's OS-level window focus was lost; `:focus` matches nothing while
  `document.activeElement` retains its value). Re-measured with a
  `document.hasFocus()` gate (a real `press Shift` re-focuses the page):
  **byte-identical**.
- **The API error-tier audit (suggestion #3) — NO finding.** The 15
  route files' tiers consistent (401 session / 400 validation + JSON
  parse / 404 scoped not-found / 429 login rate-limit / 403 unverified
  / 409 duplicate register); the client layered (network → non-JSON
  "Unexpected response" → envelope); every Prisma query `userId`-scoped
  (the unscoped findUniques are the pre-auth email lookups — correct);
  the money-math edge cases pinned (the 0.1+0.2 proof, the cent
  boundary, the three formatters, the ∞ ratio).
- **The VLM pairwise (two fresh pairs, viewport-asserted 1280×800)**:
  the dashboard — VERDICT IDENTICAL, one flag DOM-explained (the
  Dashboard-active rail = superset #3); the forgot state — VERDICT
  IDENTICAL, zero flags.
- Probe-methodology lessons: (L1) the unfocused-headless-window
  `:focus` artifact — gate every `:focus`-computed read on
  `document.hasFocus()`; (L2) `[tabindex=-1]` is an INVALID unquoted
  CSS selector (an identifier cannot start with `-` then a digit —
  quote it); (L3) the tool-result display pipeline eats `[h` and `[m`
  sequences (lesson 44's family) — DISPLAY-ONLY: command transport and
  file contents are never touched (a python `repr()` output of a file
  read displayed mangled mid-session and fabricated a "the file got
  mangled" conclusion; byte-level reads proved every file intact);
  (L4) the reference's burger has no aria-label (the sr-only
  "Toggle Sidebar" span names it) and its mobile sheet closes via the
  burger TOGGLE (no X); (L5) a REAL Tab into a `focus-visible:` ring
  needs the source focused first (programmatic focus + one real Tab);
  back-to-back test presses can outrace Radix's roving (interleave
  `toBeFocused()` assertions); (L6) the 6-route × 6s overflow eval
  exceeds the agent-browser CDP timeout (3 routes per eval is the
  ceiling); (L7) a two-probe sequence that clicks an already-open
  Select trigger toggles it closed — read the fresh open in ONE
  self-contained probe.

**Step 4 — the plan + TDD.** `docs/remediation-plan-v34.md` written and
validated against the codebase (grep-verified: the forgot families in
place, no forgot-FOCUS test in login-parity.spec.ts, the frequency
combobox addressable via aria-label, SelectItem's `focus:bg-accent`,
the compiled `.focus\:bg-accent:focus{background-color:#f5f5f5}` rule,
the README's three stale 165 spots, zero new register-class calls in
the plan's tests). TDD: the S1 test (the forgot focus-walk contract)
written → census mapping fixed (the `type` attribute took precedence
over text) → the submit's focus-VISIBLE gate hit (programmatic focus
never engages it — restructured to programmatic-focus-then-REAL-Tab) →
**GREEN**; pin-sanity: the INPUT_CLS shadow family removed → FAILED;
the submit ring removed → FAILED; restored → GREEN. The S2 test (the
listbox keyboard contract) written → the re-open Enter step raced
Radix's roving with back-to-back presses (the trigger stayed Monthly) —
interleaved `toBeFocused()` assertions (implicit settle) → **GREEN**;
pin-sanity: SelectItem's `focus:bg-accent` removed → the highlight
assertions FAILED; restored → GREEN. D1 fixed (the README's
structure/commands sections 165 → 168 — the v33 miss).

**Step 5 — the chain.** **FULL CHAIN GREEN: 108 unit · 168 e2e (166 →
168) · 35 smoke** + lint + typecheck + build. The dev DB census clean
(7 items / 0 line items / 0 probe users — every probe cycle was
cancelled before save). The 16 screenshots regenerated.

**Step 6 — docs + ship.** The probe README (the v34 catalog + the
L1–L7 lessons), README (the v34 row + the 168 counts), CLAUDE.md (the
e2e description + the two v34 surface entries + the 168 count),
AGENTS.md (the v34 verification paragraph), the SKILL doc (the state
line + the Session-67 row), this session log, the repo worklog (the
Session 67 entry), the workspace worklog.

## What this session did

- **Workspace refreshed** (`git pull` — the session_69 transcript
  commit `3ff3d7c`) + the environment re-verified; the baseline chain
  green on the first full run
- **Standing checks all clean (28th consecutive)**: mobile-nav R1–R4 on
  both sites — **Tailwind v4 pins hold, the mobile menu works**; data
  drift clean (reference read-only, verified before + after the probe
  cycles); the SEO pair live (full head census byte-identical)
- **The session-69 suggested surfaces resolved with first-time
  measurements — ALL clean**: the forgot-password focus walk (NO
  finding — the 3-stop census + the slate/zinc/raw families
  byte-identical), the frequency Select's listbox keyboard contract (NO
  finding — the full Radix combobox contract identical once the
  `:focus` artifact was gated), the API error-tier audit (NO finding —
  the tiers, the client layering, and the query scoping all verified)
- **TWO pins + one doc fix** (`docs/remediation-plan-v34.md`): the
  forgot-state focus-walk contract (login-parity) and the frequency
  listbox keyboard contract (calculator) — TDD with pin-sanity
  mutations; the README's stale 165→168 count spots fixed
- **The big probe lesson banked**: the unfocused-headless-window
  `:focus` artifact (the `document.hasFocus()` gate) + the
  display-only `[h`/`[m` mangling arbitrated byte-level (both
  demonstrated live this session — each fabricated a phantom finding
  before the gate/arbitration caught it)
- Full chain **108/168/35 green**; docs/screenshots/worklog aligned;
  committed and pushed to main via the SSH wrapper

**Suggested next steps**: the unmeasured families keep shrinking — the
item-card action menus' open-state focus chrome (the dropdown menu
items' focus families — v29 measured the containers, not the item
focus), the dashboard quick-action buttons' focus-visible family, or
the deep-link/URL contract (the `?from_url` redirect family, the 404
route's link semantics); or the tooling pass (a `document.hasFocus()`
assertion helper baked into the probe README's standing scripts, a
Playwright a11y audit CI step). Just re-issue the brief referencing
`docs/session_70.md` / `docs/remediation-plan-v34.md` and I'll pick it
up from there.
