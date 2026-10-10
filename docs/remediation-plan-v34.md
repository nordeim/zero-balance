# Remediation Plan v34 — Session-67 Parity Iteration

Date: 2026-10-10 · Scope: fresh two-site re-audit after the v33 baseline
(`07d890c` + the session-log commit `3ff3d7c` on `main`; this session's
re-run of the whole chain green on the FIRST full run: lint ✓ ·
typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**166/166 e2e ✓** · 35/35 smoke ✓). The workspace survived intact from v33
(node_modules, `.env` with `DATABASE_URL="file:../db/custom.db"`, the
`db/` seed at the repo root); `scandihaven` re-verified (the reference
repo only — never compiled). Probes: the standing disciplines — one-shot
`agent-browser eval` (base64 via run-probe.sh for `$`-bearing probes),
the :3200 parity server inside ONE `with-server.sh` invocation, REAL key
presses for every focus-chrome claim, parked-pointer settles, FULL
computed strings, full-settle re-reads, and (new this session — L1
below) a `document.hasFocus()` gate before any `:focus`-computed read.

## The sweep — method and results

The pass swept the three session-69 suggested surfaces — the
**forgot-password/reset state's focus walk**, the **calculator
frequency Select's listbox keyboard contract**, and the **API
error-tier audit** — plus the standing re-verification set (mobile-nav
R1–R4 on BOTH sites, data drift, the SEO pair, two VLM pairs) and the
code audit (`npm audit` = the same 5 dev-only ESLint
`braces`/eslint-config-next advisories — accepted, unchanged, dev-only;
the secret-pattern scan matching only the documented files;
`.env.example` verified current).

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
- **Data drift clean (28th)**: allocation 30.5%, Balance `$3475.00`,
  income `$5000.00`/1 (Salary), savings `$1000.00`/1 (Emergency Fund),
  expenses `$525.00`/4 — the reference read-only throughout (the
  forgot-reset probe used a throwaway address; the calculator/listbox
  probe cycles were all cancelled before save; verified before and
  after).
- **SEO pair ✓** (live, both sites): robots.txt + sitemap.xml live on
  both; the full head-metadata census byte-identical (description /
  og:title / og:description / og:type / og:image / twitter:card /
  twitter:title / twitter:description / apple-mobile-web-app-title /
  title); canonical + og:image keyed off `NEXT_PUBLIC_SITE_URL`. The
  reference's `/manifest.json` still 302s empty (broken) while the
  clone's `manifest.webmanifest` serves the v7-pinned document — a
  superset.
- **Suggestion #1 — the forgot-password state's focus walk: NO finding
  (first-time measurement; the S1 pin below).** The reference's state
  (a STATE on `/login` — the "Forgot password?" button swap): a
  "Back to sign in" plain button, the h2 "Reset your password", the
  description, ONE email input (368×44 at desktop, radius 12px, bg
  `rgba(248,250,252,0.5)`), and a "Send reset link" submit (368×44,
  `#0f172a`). The walk: NO auto-focus on landing (focus stays on the
  body — unlike the verify state's first-box auto-focus), exactly THREE
  app stops in order (Back → Email → Send reset link), then the exit to
  the page (the reference tours its dev-badge button after; the clone
  has no badge). The focus families, REAL-Tab-measured on both sites:
  the email input renders the v13 SLATE family (`rgb(255,255,255) 0 0
  0 2px, rgb(148,163,184) 0 0 0 4px` + the tinted `#94a3b8` border) —
  the clone's `INPUT_CLS` byte-matches; the submit renders the v25 ZINC
  family (`rgb(255,255,255) 0 0 0 2px, rgb(9,9,11) 0 0 0 4px, rgba(0,
  0,0,0.05) 0 1px 2px 0px`) — the clone's submit classes byte-match;
  the Back button renders the browser-default `outline: auto` on both
  (raw buttons, no focus utilities). The post-submit state: the
  reference's "Check your email" confirmation (a real email flow) vs
  the clone's honest no-mail variant — the documented v12 G4 superset
  (a self-hosted instance has no SMTP), already pinned by the v12 spec.
- **Suggestion #2 — the calculator frequency Select's listbox keyboard
  contract: NO finding (first-time measurement; the S2 pin below).**
  Both sites' "Add Line Item" sub-dialog Frequency control is the same
  Radix combobox family: `role=combobox` trigger with `aria-controls`
  → the listbox, SIX options in the same order (One-time, Weekly,
  Bi-weekly, Monthly, Quarterly, Annually), popper-portal content. The
  contract, measured with REAL key presses on both sites: fresh-open
  focuses the SELECTED option (Monthly) which renders the accent
  highlight (`bg rgb(245,245,245)` + `color rgb(23,23,23)` — the
  `:focus`-driven shadcn family; the reference's older Radix ALSO
  stamps `data-highlighted`, the clone's 2.3.8 stamps it after the
  first interaction — invisible either way since both style via
  `:focus`); ArrowDown/ArrowUp rove the highlight (Monthly→Quarterly);
  the roving is CLAMPED at both ends (no wrap — verified at index 5
  staying 5 and index 0 staying 0); Home jumps to the first, End to
  the last; NO typeahead on either site (a focused-page 'w' keypress
  leaves the highlight on Monthly on both); Escape closes the POPUP
  ONLY (focus returns to the trigger; the sub-dialog stays open —
  re-verified, the reference's plain-div dialogs ignore Escape but its
  Radix popups do not); Enter selects the highlighted option (the
  trigger updates to the new value, the popup closes, focus lands on
  the trigger).
- **Suggestion #3 — the API error-tier audit: NO finding.** The 15
  route files' error tiers are consistent: 401 session (the
  `requireSession` guard), 400 validation (the zod `parseBody` seam,
  JSON-parse failures included), 404 not-found (the scoped findFirst
  guards), 429 login rate-limit, 403 unverified-login, 409 duplicate
  register. The client (`src/lib/api.ts`) layers its handling: network
  failure → ApiError(0), non-JSON (an unstructured 500) → the
  "Unexpected response from server" tier, envelope errors → the
  server's message — and the route-aborted UI surfaces are pinned by
  the v17/v18 e2e specs. Every Prisma query is `userId`-scoped (all
  findMany/findFirst/updates/deletes; the unscoped findUniques are the
  pre-auth email lookups in register/verify — correct by design). The
  money-math edge cases are pinned by the unit suite (the 0.1+0.2
  proof, the cent boundary, the three formatters, the ∞ ratio).
- **The VLM pairwise (two fresh pairs, viewport-asserted 1280×800
  before each capture — the v33 lesson)**: the dashboard — VERDICT
  IDENTICAL, one flag DOM-explained (the clone's Dashboard-active rail
  = superset #3); the forgot state — VERDICT IDENTICAL, zero flags
  (the honest-copy difference is text-content, explicitly excluded).
- **Probe-methodology lessons (L1–L3):**
  - **L1 — the unfocused-headless-window `:focus` artifact (the big
    one).** An `agent-browser eval` that DOM-clicks a Select trigger
    open reads `document.activeElement` = the selected option while
    `element.matches(':focus')` is FALSE and `document.querySelector(
    ':focus')` returns NOTHING — the headless page's OS-level window
    focus was lost (no real key press since the last navigation), so
    the `:focus` pseudo-class matches nothing while `activeElement`
    retains its value. The first fresh-open comparison this session
    fabricated a "the clone's selected option renders NO highlight"
    finding (bg transparent vs the reference's #f5f5f5) — the
    reference read had run after REAL key presses (page focused), the
    clone read after JS clicks alone (page unfocused). **Gate every
    `:focus`-computed read on `document.hasFocus()` (a real `press
    Shift` re-focuses the page); Playwright is immune (its pages hold
    real focus).**
  - **L2 — `[tabindex=-1]` is an invalid CSS selector.** An unquoted
    attribute value starting with `-` followed by a digit is not a CSS
    identifier: `querySelectorAll('[tabindex]:not([tabindex=-1])')
    THROWS. Quote it: `[tabindex="-1"]`. The thrown error's message
    also displays with `a[href]` mangled to `aref]` — the display
    pipeline eats a `[h` sequence (see L3) — which misdirected the
    debugging toward a transport bug that wasn't there (the base64
    transport was verified clean by char codes).
  - **L3 — the display-mangling family extends beyond `[m`.** The
    v44-documented tool-result display pipeline eats `[m`; this
    session it also ate `[h` (in `a[href]` → `aref]` inside a browser
    error message). Treat ANY bracket+letter sequence in displayed
    tool output as suspect; arbitrate with char codes or probe files,
    never by eye.

## Findings

### D1. [LOW — doc drift] README's structure/commands sections still say 165 e2e tests

The v33 iteration raised the suite 165→166 and updated the README's
remediation table row, CLAUDE.md, AGENTS.md, the SKILL doc, and the
worklog — but the README's project-structure tree (line ~91: "Playwright
specs (165 tests)") and the two commands-section spots (line ~148: "npm
run test:e2e # Playwright e2e (165 tests)"; plus the test-suite table
row) still carry the pre-v33 count. The repo's single source of truth
(`npm run test:e2e` → 166) and every other doc disagree with these three
spots. Fix: 165 → 166 in the README (three spots), keeping the v34
table row's count at the NEW total after this session's pins (166→168).

### S1. [PIN] The forgot-password state's focus-walk contract

The session-69 surface #1's measurable contract, now measured and
pinned: the state renders exactly THREE focusable app stops in order
(Back to sign in → Email input → Send reset link), NO auto-focus on
landing (focus stays on the body), the email input's focused chrome =
the v13 slate family (white 2px + slate 4px ring + the tinted #94a3b8
border), the submit's focused chrome = the v25 zinc family (white 2px +
zinc 4px + the ambient layer), and the Back button stays a raw button
(no focus utilities — the browser default). No production change — a
new e2e test in `tests/e2e/login-parity.spec.ts` (the v13 G3 test's
section) pins the families + the no-auto-focus + the census so a future
auth-card refactor cannot silently swap the families (the reference
itself runs distinct families per form — the v33 lesson) or add an
invented auto-focus.

### S2. [PIN] The calculator frequency Select's listbox keyboard contract

The session-69 surface #2's measurable contract, now measured and
pinned: fresh-open focuses the selected option which renders the accent
highlight (`rgb(245,245,245)` bg + `rgb(23,23,23)` text — the
`:focus`-driven family); ArrowDown/ArrowUp rove with the highlight
following; the roving CLAMPS at both ends (no wrap); Home/End jump to
the ends; Escape closes the popup only (focus returns to the trigger;
the sub-dialog stays open); Enter selects the highlighted option (the
trigger updates). No production change — a new e2e test in
`tests/e2e/calculator.spec.ts` pins the contract end-to-end. Playwright's
real page focus renders the `:focus` highlight (the L1 artifact cannot
strike there), so the bg assertions are honest.

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | S1 pin: the forgot-state focus-family test (the 3-stop census + no-auto-focus + the slate input family + the zinc submit family + the raw back button) | test | `tests/e2e/login-parity.spec.ts` |
| 2 | S1 pin-sanity: mutate the INPUT_CLS focus family → the test FAILS; mutate the submit ring → FAILs; restore | verify | `src/components/budget/login-card.tsx` |
| 3 | S2 pin: the frequency listbox keyboard contract test (fresh-open highlight + arrow roving + clamp + Home/End + Escape + Enter) | test | `tests/e2e/calculator.spec.ts` |
| 4 | S2 pin-sanity: remove `focus:bg-accent` from SelectItem → the highlight assertions FAIL; restore | verify | `src/components/ui/select.tsx` |
| 5 | D1: the README's three stale 165→166 count spots | docs | `README.md` |
| 6 | The full chain re-run (108 unit · 168 e2e · 35 smoke + lint + typecheck + build) | verify | — |
| 7 | The 16 screenshots regenerated | docs | `docs/screenshots/` |
| 8 | The v34 probes persisted + the probe README updated (the L1–L3 lessons) | docs | `scripts/parity-probes/` |
| 9 | Docs aligned (README v34 row + counts, CLAUDE, AGENTS, SKILL, session_70, the repo worklog Session 67, the workspace worklog) | docs | repo root + `docs/` |
| 10 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `login-card.tsx`: the AuthForm section renders the forgot state's
  three controls — the back button (`-mb-2 flex items-center gap-2
  text-sm font-medium text-[#64748b]…` — no focus utilities, raw), the
  shared `INPUT_CLS` (line ~213: `focus:border-[#94a3b8]
  focus:shadow-[0_0_0_2px_#fff,0_0_0_4px_#94a3b8] focus:outline-none`
  — the v13 slate family), and the submit (`focus-visible:ring-2
  focus-visible:ring-[#09090b] focus-visible:ring-offset-2` — the v25
  zinc family; the computed form measured byte-identical live this
  session). No `autoFocus` anywhere outside the v33 code inputs (grep:
  the CodeInputs' `autoFocus={i === 0}` only). The forgot state needs
  no API call (the honest submit transitions locally) — the new test
  adds ZERO register-class calls (the rate-limit budget unchanged).
- `login-parity.spec.ts`: the v13 G3 test (line ~424) is the
  established focus-family pattern (goto /login → state swap → focus →
  settle 350ms → computed reads); the v12 G4 test (line ~303) already
  covers the post-submit honest state; the file has no existing
  forgot-FOCUS test (grep: the forgot tests cover geometry + mobile +
  the confirmation state — the focus families are the gap this pin
  closes).
- `calculator.spec.ts`: the line-item dialog tests open the sub-dialog
  via `dialog.getByRole("button", { name: "Add Item" })` with lookups
  scoped by dialog name (the two-dialogs-open pattern); the frequency
  combobox is addressable as `lineDialog.getByRole("combobox", { name:
  "Frequency" })` (the `aria-label="Frequency"` on the trigger —
  line-item-dialog.tsx line ~154). The options are
  `page.getByRole("option", …)` (portal-level, outside the dialog
  scope — the v33 announcer pattern). The add/delete tests restore the
  seed state; the new test only CANCELS (nothing persisted — the
  established cancel-only pattern from the fields test).
- `select.tsx`: SelectItem carries `focus:bg-accent
  focus:text-accent-foreground` (line ~113) — the accent bg asserted by
  the pin resolves to `#f5f5f5`/`#171717` via the globals.css theme
  (`--color-accent`, line ~109). The pin-sanity mutation (removing
  `focus:bg-accent`) makes the fresh-open bg assertion fail — verified
  conceptually against the compiled rule `.focus\:bg-accent:focus{
  background-color:#f5f5f5}` (grepped in the standalone CSS this
  session).
- `README.md`: the three stale spots grepped at lines ~90-91, ~148 (the
  structure tree's "165 tests", the commands row's "165 tests", and the
  test-suite table) — no other 165 references outside the v32/v33
  remediation table rows (historical record, correct as-is).
- The chain gate: lint → typecheck → 108 unit → build → 166 e2e (168
  after S1+S2; both are new tests) → 35 smoke.
