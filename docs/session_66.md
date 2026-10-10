# Session 66 — Parity iteration v32 (session-63 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_64.md` / `docs/remediation-plan-v31.md`
/ `worklog.md` / `docs/session_65.md`. Full autonomy granted on the open
questions, so I worked the whole chain directly.

**Step 1 — workspace refresh.** The workspace had been RESET — the repo
re-cloned (`zero-balance` at `0c91904`), `scandihaven` re-cloned, and the
environment rebuilt and re-verified: node_modules, `.env`
(`DATABASE_URL="file:../db/custom.db"`), the `db/` folder re-pushed +
re-seeded at the repo root. The five project docs + the four session docs
re-read; the codebase validated against them — the v31 changeset in place
(the 164-test suite, the donut keyboard pins, the tiles' roving pin),
verified by the full chain below.

**Step 2 — the audit.** The baseline chain green on the FIRST full run:
lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap
prerendered) · **164/164 e2e ✓** · 35/35 smoke ✓. Audit Phase 2 clean: the
same 5 dev-only ESLint `braces`/eslint-config-next advisories (no patched
release — accepted, dev-only), the secret-pattern scan matching only the
documented files, `.env.example` verified current.

**Step 3 — the two-site sweep** (agent-browser on the ref32/clone32
sessions + the :3200 parity server; the fresh-open + settle +
parked-pointer + real-click/real-hover/real-Tab disciplines throughout):

- **Mobile navigation (the task focus) R1–R4 all re-verified live on BOTH
  sites — the 26th consecutive check.** R1: the reference's two `fixed
  top-0 z-[100]` toast containers still intercept the burger's center hit
  (hit `DIV.fixed.top-0.z-[100]`, scrollWidth 395), while the clone's
  burger hit is DIRECT on the svg with 390 fit on every route. R2: the
  reference's sheet still traps after nav (re-verified with a ROBUST
  detector — a fixed panel carrying ≥4 nav links + body locked + 3 dark
  overlays, measured on `/income` after the nav click; the v31 probe's
  white-bg matcher missed the sheet this session — a probe lesson); the
  clone's closes (superset fix #2). R3: the reference marks nothing active
  on `/` and has no `<nav>` landmark; the clone highlights Dashboard + has
  the landmark. R4: the reference overflows 395 on `/`+`/dashboard` and
  464 on `/networth`; the clone fits 390 on all six routes. **The Tailwind
  v4 pins hold — the clone's mobile menu works as expected.**
- **Data drift clean (26th — the reference only read)**: allocation 30.5%,
  Balance `$3475.00`, income `$5000.00`/1 (Salary), savings `$1000.00`/1
  (Emergency Fund), expenses `$525.00`/4 — verified BEFORE and AFTER the
  calculator probe cycles (the reference's Miscellaneous parent returned
  to `$0.00` after the add/delete restore; the census never moved).
- **SEO pair ✓ (the full head-metadata census)**: robots.txt + sitemap.xml
  live on both; description / og:title / og:description / og:type /
  twitter:card / twitter:title / twitter:description /
  apple-mobile-web-app-title / title byte-identical; canonical + og:image
  keyed off `NEXT_PUBLIC_SITE_URL`; charset + viewport present. The
  reference's `/manifest.json` endpoint 302s empty (broken); the clone's
  `manifest.webmanifest` serves the full v7-pinned document — a superset.
- **The net-worth dropdown menus' keyboard contract (session-63
  suggestion #1) — NO finding, byte-identical at every axis**: click-open
  → focus on the menu container (role=menu, tabindex −1, items −1, no
  highlight); Enter-open (keyboard) → the first item focused +
  data-highlighted; ArrowDown → Edit (tabindex 0) → Delete; ArrowUp
  reverse; no wrap at either end (CLAMPED); Home/End work; NO typeahead
  (typing `d` from Edit stays on Edit on both); Escape → menu closed +
  focus returned to the trigger. The clone's aria-labeled "Actions for X"
  triggers are the documented v29 naming superset.
- **The calculator line-item row actions' Tab order (suggestion #2) — the
  census and Tab walk byte-identical; ONE ring-family drift (G1)**: both
  sites' populated calculator renders exactly FOUR focusable stops in the
  same order — X (36px) → Add Item (110px) → Edit (32px) → Delete (32px),
  all tabindex 0, the row actions `opacity 1` inside their `opacity-0`
  hover-reveal container (focusable-while-invisible on BOTH — the reveal
  is hover-only, never focus). A REAL Tab walk reproduces the same
  sequence on both; after the last stop the reference EXITS to the page
  (no trap) while the clone WRAPS to the X (the documented Radix-trap
  superset). The drift: the reference's row actions carry the shadcn
  focus family (`focus-visible:outline-none focus-visible:ring-1
  focus-visible:ring-ring`) — REAL-Tab-measured, the focused Edit renders
  `outline: solid 2px rgba(0,0,0,0)` + the 1px #0a0a0a ring shadow with
  the white lead layer — while the clone's raw buttons rendered the
  browser-default `outline: auto 1px lab(…)` and `box-shadow: none`.
- **The breakdown accordion's arrow semantics (suggestion #3) — NO
  functional finding**: the section rows are full buttons on both sites
  (tabindex 0, the same class token set, computed chrome identical:
  radius 8px, transparent bg, 0.15s transition); arrows and Home/End are
  INERT on both; Enter EXPANDS on both; Escape does NOT collapse on
  either. One DOM delta kept and documented as a superset (S1): the
  clone's section AND category rows carry `aria-expanded` (accurate
  state); the reference's carry none.
- **The reference's row delete is IMMEDIATE** (no confirm — measured:
  click Delete → item gone, no confirm text, no red buttons). The clone's
  inline "Delete this line item?" confirm is the documented "unconfirmed
  deletes fixed" superset.
- **The VLM pairwise (two fresh pairs)**: the dashboard — flag
  DOM-explained (the clone's Dashboard-active rail = superset #3); the
  calculator — flag DOM-explained (the clone's X renders its v27-pinned
  ring on open because Radix focuses it — the documented v29 superset).
- Probe-methodology lessons (persisted in the probe README): the
  transition-colors/outline-color settle (v4's property list includes
  outline-color — settle ≥350ms before reading focus chrome, or the read
  catches the transparent settle mid-flight in oklab form); form fill
  finders anchor on LABEL text or DOM order, never `placeholder*=name`
  (the reference's Provider placeholder "Insurance Company Name" swallowed
  an Item Name fill); a calculator add/delete probe cycle recalculates the
  parent amount (restore the dev db afterward — the seed's natural-key
  upsert does NOT); the reference's sheet detector should match STRUCTURE
  (fixed panel + nav links + body lock), not background color.

**Step 4 — the plan + TDD.** `docs/remediation-plan-v32.md` written and
validated against the codebase (grep-verified: no focus assertions in the
calculator spec, `focus-visible` absent from calculator-dialog.tsx, the
item-card precedent uses exactly the family string, `--color-ring:
#0a0a0a` is the token, no aria-expanded assertions in the breakdown
spec). TDD: the G1 test written → RED (the shadow lacks the ring) →
`focus-visible:ring-1 focus-visible:ring-ring` inline → the ring GREEN
but the outline still wrong → root-caused to v4's `outline-none` utility
(emits `outline-style: none` ONLY) → the `.zb-row-action:focus-visible`
globals.css pin (v3's `outline: 2px solid transparent; outline-offset:
2px`) → the immediate-read trap (transition-colors interpolates
outline-color) → the 350ms settle in the test → **GREEN**. The S1 pin
assertions added to the breakdown spec → GREEN. **Pin-sanity mutations**
(the ring utilities removed → the ring assertions FAIL; the globals pin
removed → the outline assertion FAILS reading `auto/1px/lab(…)`; the
aria-expanded attribute removed → the S1 pin FAILS) → all restored →
GREEN again.

**Step 5 — the chain.** **FULL CHAIN GREEN: 108 unit · 165 e2e · 35
smoke** + lint + typecheck + build (the suite went 164 → 165). Live
re-verification on the :3200 parity server: the REAL-Tab focused Edit
reads `outline: solid 2px rgba(0, 0, 0, 0)` + the 1px #0a0a0a ring
shadow (byte-identical to the reference's measurement, modulo v4's
transparent lead layers), contOp 0 (still no reveal-on-focus — matching).
The mobile-nav R1/R4 spot check clean (direct svg hit, 390 fit). The 16
screenshots regenerated (2 PNGs byte-noise only — the fix is
keyboard-level, zero visual change).

**Step 6 — docs + ship.** The probe README (the v32 catalog + the five
lessons), README (the v32 row + the 165 counts), CLAUDE.md (the e2e
description + counts), AGENTS.md (the v32 verification paragraph), the
SKILL doc (the session row + the 165-test state), this session log, the
worklog.

## What this session did

- **Workspace re-cloned (the sandbox reset) + environment rebuilt and
  re-verified**; the baseline chain green on the first full run
- **Standing checks all clean (26th consecutive)**: mobile-nav R1–R4 on
  both sites — **Tailwind v4 pins hold, the mobile menu works**; data
  drift clean (reference read-only, verified before + after the probe
  cycles); the SEO pair live (full head census byte-identical)
- **The session-63 suggested surfaces resolved with first-time keyboard
  measurements**: the net-worth dropdown menus' keyboard contract (NO
  finding — byte-identical), the calculator row actions' Tab order (one
  finding: the focus-visible ring family), and the breakdown accordion's
  arrow semantics (NO functional finding; the aria-expanded superset
  documented + pinned)
- **TWO changes** (`docs/remediation-plan-v32.md`): the
  `focus-visible:ring-1 focus-visible:ring-ring` utilities + the
  `.zb-row-action:focus-visible` globals.css pin on the calculator's row
  actions (a THIRD Tailwind v4 class-name-parity trap documented — the
  outline-none form), and the breakdown rows' aria-expanded kept + pinned
  as a deliberate a11y superset — TDD with pin-sanity mutations, the fix
  live-re-verified byte-identical
- Full chain **108/165/35 green**; docs/screenshots/worklog aligned;
  committed and pushed to main via the SSH wrapper

**Suggested next steps**: the keyboard sweep still has unmeasured
families — the line-item sub-dialog's own focus walk (the 85vh panel's
internal Tab order), the register/verify-email surfaces' focus-ring
families, and the toast's focus semantics; or the
performance/correctness pass (Lighthouse, bundle sizes, API error tiers).
Just re-issue the brief referencing `docs/session_66.md` /
`docs/remediation-plan-v32.md` and I'll pick it up from there.
