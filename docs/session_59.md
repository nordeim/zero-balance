# Session 59 — Parity iteration v29 (session-57 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_57.md` / `docs/remediation-plan-v28.md`
/ `worklog.md` / `docs/session_58.md`. Full autonomy granted on the open
questions, so I worked the whole chain directly.

**Step 1 — workspace refresh.** The sandbox had been RESET — the repo
re-cloned fresh (`zero-balance` at `34b4970` = the v28 parity commit
`d622f2e` + the session-58 transcript doc; `scandihaven` re-cloned as
the standing pattern reference); the environment rebuilt and re-verified:
`.env` from the accurate `.env.example`
(`DATABASE_URL="file:../db/custom.db"`), `db/` re-pushed + re-seeded at
the repo root (7 budget items, 3 assets, 2 liabilities for
`demo@zerobalance.app`), node_modules reinstalled, Vitest/Playwright
configs intact, robots.txt + sitemap.xml prerendering in the build. The
five project docs + four session docs re-read; the codebase validated
against them — the v28 changeset in place (the
`item-details-dialog.tsx` component + the store's `details` slot + the
card's guarded onClick + the app-shell mount + the `.zb-badge-hover`
pin + the four badge strings + the two button strings, all verified).

**Step 2 — the audit.** The baseline chain green: lint ✓ · typecheck ✓
· 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · **158/158
e2e** ✓ (one transient not-found-spec flake on the first two runs under
fresh-sandbox load — the isolated re-run and the third full run both
green; the flake is a transient `/api/auth/me` failure under load that
flips the boot gate to the login redirect — environmental, pre-existing,
unrelated to any change this session) · 35/35 smoke ✓. Audit Phase 2
clean: the same 5 dev-only ESLint `braces` advisories (no patched
release — accepted), the secret-pattern scan matching only the
documented files.

**Step 3 — the two-site sweep** (agent-browser on the ONE shared tab +
the :3200 parity server; the fresh-open + settle + parked-pointer +
real-click/real-hover disciplines throughout):

- **Mobile navigation (the task focus) R1–R4 all re-verified live on
  BOTH sites — the 23rd consecutive check.** R1: the reference's two
  `fixed top-0 z-[100]` toast containers still intercept the burger's
  center hit at (38,30) (`pe:auto`, 390×32, z-100; scrollWidth 395 on
  `/`), while the clone's burger hit is DIRECT on the svg with the
  viewport `pe:none` and 390 fit on every route. R2: the reference's
  sheet still traps after nav; the clone's closes (superset fix #2).
  R3: the reference marks nothing active on `/` and has no `<nav>`
  landmark; the clone highlights Dashboard + has the landmark (the
  documented superset). R4: the reference overflows 395 on
  `/`+`/dashboard` and 464 on `/networth`; the clone fits 390 on all
  six routes. **The Tailwind v4 pins hold — the clone's mobile menu
  works as expected.**
- **Data drift clean (23rd — the reference only read this session, no
  probe items created)**: allocation 30.5%, Balance `$3475.00`, income
  `$5000.00`/1, savings `$1000.00`/1, expenses `$525.00`/4.
- **SEO pair ✓**: both sites serve robots.txt (allow-all + the sitemap
  link) and sitemap.xml.
- **The details sheet's KEYBOARD semantics (session-57 suggestion #1)
  — measured for the first time; NO parity gap, the clone is the
  documented a11y superset**: the reference's sheet opens with NO
  initial focus (activeElement stays BODY), carries no
  role/aria-modal, and a REAL Tab walk tours the ENTIRE underlying
  page (stops 1–14 measured: the five sidebar links, Add Expense, the
  three filter triggers, then every card's Edit/Calculate buttons) —
  the sheet never traps; its single focusable (the X) is reachable
  only after the whole document. The clone (Radix): initial focus ON
  the X — and Chrome applies `:focus-visible` to the programmatic
  focus, so the pinned 1px `#0a0a0a` ring RENDERS in the open state
  (the superset's visible signature) — full Tab containment, Escape
  close. No change.
- **The VLM pairwise of the details sheet (suggestion #2)**: DIFFERENT
  with two flags, both DOM-explained — the clone's X "box" is the
  Radix initial-focus ring above (the reference renders the identical
  v27-pinned ring when its X is actually keyboard-focused), and the
  fact-row count/height difference is data-driven (the two captures'
  items differ in Notes/Payment Method presence; both panels are the
  measured `max-h-[85vh] overflow-y-auto` contract). No class-level
  drift — no change.
- **The edit-dialog entry-point consistency (suggestion #3) — NO
  finding**: the reference's income-card ellipsis menu (Edit/Delete,
  opened with a real ref click — synthetic clicks don't open it) and
  the expense card's hover-revealed footer Edit both open the SAME
  "Edit Budget Item" dialog (the identical 14-label field set,
  pre-filled per item). The clone's single shared `BudgetItemDialog`
  already does exactly this.
- **The net-worth view interactive-family census (suggestion #4 — the
  bulk of the session; never class-diffed)**: the tab triggers
  (computed byte-identical: active `rgb(220,252,231)`/`rgb(20,83,45)`,
  the clone's hex-pin superset), the tablist (448px, muted
  `rgb(245,245,245)`, 2-col grid), the Add Asset/Liability gradient
  buttons (`zb-btn-add` + the pinned gradients), the card containers
  (identical classes + the pinned inline border/shadow; cursor `auto`
  on BOTH sites — the reference's asset-card click opens NOTHING,
  unlike its budget items' details sheet), and the action dropdown
  menus (panel + items byte-identical: border `1px
  rgb(229,229,229)`, radius 6, min-w 128, 32px items, Edit
  `rgb(10,10,10)` / Delete `rgb(220,38,38)`) — ALL clean. **THE
  FINDING (G1)**: the reference's asset-card TYPE label is a
  Badge-base DIV — rest bg `rgb(243,244,246)` / text `rgb(55,65,81)`
  + on a REAL CDP hover the tint `rgba(245,245,245,0.8)` over 150ms
  (the exact v28 G1 family on a surface never diffed); the clone's
  static spans computed TW4 oklab (`lab(96.1596 …)` / `lab(27.1134
  …)`) with no hover family.
- **The net-worth mobile VLM pair (the regenerated capture)**: the
  desktop pair IDENTICAL; the mobile pair's three flags all
  DOM-arbitrated as NO CHANGE — (1) the summary grid 2-col vs 1-col:
  a LIVE DOM experiment flipping the clone to the reference's 2-col
  measured the seeded values "$65,300.00"/"$311,250.00" needing
  152px/169px vs the 107px content boxes (glyphs overlap the neighbor
  column; the reference's own "$25,000.00" already micro-overflows
  152/144 and its "$0.00" never exercises the case) — the v4-era
  stacking stands as the data-fit superset; (2) the trend icon inset
  is 48px on BOTH sites (measured with the same gradient-card finder;
  the earlier 16px reading was a wrapper artifact); (3) the tab icons
  are the v14-pinned 16px circle-arrow pair (the VLM misread them at
  16px).
- **The dashboard's breakdown-row hover — checked, NO finding**: the
  reference's nested rows carry the same inline
  `background-color: rgb(249,250,251)` + `hover:bg-gray-100` the
  clone has, and a REAL CDP hover leaves BOTH at `rgb(249,250,251)` —
  the inline style overrides the hover class on both sites (the class
  is inert on both; rendered parity).
- Probe-methodology lessons (persisted in the probe README): the
  reference's tab TRIGGERS ignore synthetic `element.click()` (real
  ref clicks only — the v28 real-click lesson extends to tabs); VLM
  glyph/icon claims at 16–24px are unreliable (every mobile flag was
  a false positive or data-driven — computed geometry is the
  arbiter); the clone's dialog X is found by its sr-only "Close"
  textContent (no aria-label); and the reference's `/networth` 464px
  mobile overflow involves both its sidebar wrapper and its content
  column (hide-either isolation → 390; the decorative circle is
  clipped by its card's `overflow-hidden`).

**Step 4 — the plan + TDD.** `docs/remediation-plan-v29.md` written and
validated against the codebase (grep-verified scopes: exactly two
`bg-gray-100 text-gray-700` label sites, the existing `.zb-badge-hover`
pin, the networth spec's badge assertions, no other spec touching the
labels). TDD: the spec's badge assertions updated RED first (the pinned
classes + the computed rgb values + the hover family — both cards'
labels; a locator scoped to the label span because the seeded home
loan's NAME is also "Home Loan") → RED confirmed on both tests → the
two class-string fixes in `net-worth-view.tsx` (`bg-[#f3f4f6]`
`text-[#374151]` + `transition-colors zb-badge-hover`) → GREEN (14/14)
→ pin-sanity mutations (a wrong hover class + a flipped rgb) FAIL →
restored.

**Step 5 — the chain.** **FULL CHAIN GREEN: 108 unit · 158 e2e · 35
smoke** + lint + typecheck + build (the one not-found flake
re-verified environmental: the isolated re-run + the full re-run both
green). Live re-verification on the :3200 parity server: the label's
rest bg computes `rgb(243,244,246)` / text `rgb(55,65,81)` / the 150ms
transition, and a REAL CDP hover tints it to `rgba(245,245,245,0.8)` —
byte-identical to the reference's measured values on both axes. The
screenshots regenerated — 14 byte-identical + the two net-worth
captures sub-pixel-different (the oklab→hex shift changes
anti-aliasing minutely; the desktop VLM pair: IDENTICAL).

**Step 6 — docs + ship.** The probe README (the v29 catalog + the
lessons), README (the v29 row), CLAUDE.md (the e2e description),
AGENTS.md (the v29 pin paragraph), the SKILL doc (the session row +
the state), this session log, the worklog.

## What this session did

- **Workspace re-cloned + environment rebuilt** (the sandbox reset);
  all standing requirements re-verified in place; the baseline green
  on the first full run (one environmental e2e flake, investigated
  and classified)
- **Standing checks all clean**: mobile-nav R1–R4 (23rd — Tailwind v4
  pins hold, both sites), data drift (23rd — reference read-only),
  the SEO pair
- **ONE fix** (`docs/remediation-plan-v29.md`): the net-worth
  asset/liability card type labels' rest colors + hover family —
  hex-pinned (`bg-[#f3f4f6] text-[#374151]`) + the `.zb-badge-hover`
  reuse, live-verified byte-identical on both axes (the oklab drift
  and the missing hover family were both real, on a surface the v4-era
  work never diffed)
- **The session-57 suggested surfaces all resolved**: the details
  sheet's keyboard semantics (the reference's weakest surface — no
  focus/trap/role/Escape; the clone's Radix superset now measured and
  documented, including the rendered X ring on open), the VLM details
  pair (both flags DOM-explained), the edit entry-point consistency
  (the SAME 14-field dialog — no finding), and the net-worth
  interactive-family census (the finding above; everything else
  byte-identical)
- **The net-worth mobile VLM pair's three flags all DOM-arbitrated
  no-change** — including a live 2-col DOM experiment re-proving the
  v4 data-fit stacking superset (152/169px glyphs vs 107px cells)
- Full chain **108/158/35 green**; docs/screenshots/worklog aligned;
  committed and pushed to main via the SSH wrapper

**Suggested next steps**: the net-worth census pattern extends to the
DASHBOARD's interactive families (the guideline rows' hover states and
the quick-action card-buttons were pinned in the v2/v4 era but never
REAL-hover-diffed), the savings view's card family (same structure as
income/expenses — a quick census pass), and a keyboard-semantics sweep
of the net-worth tab pair (the reference's tablist arrow-key behavior
was never measured); alternatively re-run the details-sheet keyboard
comparison after opening the sheet at MOBILE (the focus-trap geometry
at the bottom-sheet breakpoint). Just re-issue the brief referencing
`docs/session_59.md` / `docs/remediation-plan-v29.md` and I'll pick it
up from there.
