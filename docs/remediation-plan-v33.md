# Remediation Plan v33 — Session-65 Parity Iteration

Date: 2026-10-10 · Scope: fresh two-site re-audit after the v32 baseline
(`f7e08b6` + the session-log commit `3818922` on `main`; this session's
re-run of the whole chain green on the FIRST full run: lint ✓ ·
typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**165/165 e2e ✓** · 35/35 smoke ✓). The workspace survived intact from v32
(node_modules, `.env` with `DATABASE_URL="file:../db/custom.db"`, the
`db/` seed at the repo root); `scandihaven` was re-cloned (the reference
repo only — never compiled). Probes: the standing disciplines — one-shot
`agent-browser eval` (base64 via run-probe.sh for `$`-bearing probes),
the :3200 parity server inside ONE `with-server.sh` invocation, REAL key
presses for every focus-chrome claim, parked-pointer settles, FULL
computed strings, and full-settle re-reads.

## The sweep — method and results

The pass swept the four session-67 suggested surfaces — the **line-item
sub-dialog's focus traversal**, the **register/verify-email focus-ring
families**, the **toast's focus semantics**, and the **performance/
bundle-size pass** — plus the standing re-verification set (mobile-nav
R1–R4 on BOTH sites, data drift, the SEO pair, two VLM pairs) and the
code audit (`npm audit` = the same 5 dev-only ESLint
`braces`/eslint-config-next advisories — accepted, unchanged, dev-only;
the secret-pattern scan matching only the documented files;
`.env.example` verified current).

- **Mobile navigation (the task focus) R1–R4 all re-verified live on BOTH
  sites — the 27th consecutive check.** R1: the reference's `fixed
  top-0 z-[100]` toast containers still intercept the burger's center hit
  (hit `DIV.fixed.top-0.z-[100]`, scrollWidth 395), while the clone's
  burger hit is DIRECT on the svg with 390 fit on every route. R2: the
  reference's sheet still traps after nav (structure detector on
  `/income`: sheet open, body locked, 3 dark overlays); the clone's
  closes (superset fix #2). R3: the reference marks nothing active on `/`
  and has no `<nav>` landmark; the clone highlights Dashboard + has the
  landmark. R4: the reference overflows 395 on `/`+`/dashboard` and 464
  on `/networth`; the clone fits 390 on all six routes. **The Tailwind v4
  pins hold — the clone's mobile menu works as expected.**
- **Data drift clean (27th)**: allocation 30.5%, Balance `$3475.00`,
  income `$5000.00`/1 (Salary), savings `$1000.00`/1 (Emergency Fund),
  expenses `$525.00`/4 — the reference read-only throughout (the
  throwaway register probe + the item-edit save-with-same-values probe
  never moved the census; verified before and after).
- **SEO pair ✓** (live, both sites): robots.txt + sitemap.xml live on
  both; the full head-metadata census byte-identical (description /
  og:title / og:description / og:type / twitter:card / twitter:title /
  twitter:description / apple-mobile-web-app-title / title); canonical +
  og:image keyed off `NEXT_PUBLIC_SITE_URL`. Known non-pinned deltas:
  Next's `User-Agent` capitalization + `1` vs `1.0` priority
  serialization + the lowercase-route choice (all documented, valid).
  The reference's `/manifest.json` 302s empty; the clone's
  `manifest.webmanifest` serves the full v7-pinned document — a superset.
- **Suggestion #1 — the line-item sub-dialog's focus traversal: NO
  finding, byte-identical at every axis.** Both sites' "Add Line Item"
  sub-dialog renders exactly THIRTEEN focusable stops in the same order —
  X (36px) → Item Name → Amount (number) → Frequency (trigger) →
  Provider → Policy → Start date → End date → Payment Method → Status
  (trigger) → Notes (textarea) → Cancel → Save Item — all tabindex 0,
  same geometry per field. A REAL Tab walk reproduces the same sequence
  on both, INCLUDING the native date segments: each `<input type="date">`
  is a 4-STOP Tab walk (8 consecutive date-segment stops for the two
  dates — browser-native, identical on both sites since both use native
  date inputs). The deltas are the two documented Radix supersets: the
  reference's sub-dialog does NOT auto-focus anything on mouse-open
  (focus stays on the "Add First Item" trigger; its dialogs are plain
  divs) while the clone's Radix focuses the X; and after the last stop
  the reference EXITS to the page while the clone WRAPS (the dialogs-wide
  trap superset). The reference's plain-div dialogs also IGNORE Escape
  (measured: two Escape presses left the sub-dialog open — re-verified
  before trusting any "closed" state).
- **Suggestion #1 extension — the sub-dialog's select triggers' focus
  chrome: NO finding (a probe lesson, not a drift).** The clone's
  Frequency/Status SelectTriggers under REAL keyboard focus resolve
  `--tw-ring-color: #0a0a0a` + `--tw-ring-shadow: 0 0 0 calc(1px + 0px)
  #0a0a0a` — the 1px ring IS present, as the FOURTH layer of v4's
  composed box-shadow (three transparent placeholder layers precede it).
  The first 85-character read looked like "no ring at all" — v4's
  composition buries the visible ring behind three zero-width layers;
  **always read the FULL box-shadow string (and the --tw-ring-*
  custom properties) before claiming a missing ring.** The reference's
  triggers render the same visible 1px ring (its lead layer is
  white-on-zero-width vs v4's transparent-on-zero-width — invisible
  either way; the documented lead-layer family).
- **Suggestion #2 — the register/verify-email focus families: ONE drift
  (G1 below), everything else byte-identical.** The register inputs:
  the reference's focused email field renders the v13-pinned slate
  family (`rgb(255,255,255) 0 0 0 2px, rgb(148,163,184) 0 0 0 4px` +
  `focus:border-[#94a3b8]`) — the clone matches (pinned). The verify
  submit: the v25-pinned white-2px + zinc-4px family — byte-identical.
  The Resend + "Back to sign in" buttons: browser-default
  `outline: auto` (raw, no focus classes) on BOTH sites — matched. The
  code inputs: the drift (G1) — the reference's focused code input
  renders the 2px zinc-950 ring with NO border tint, and the reference
  AUTO-FOCUSES the first code input on landing in the verify state.
- **Suggestion #3 — the toast's focus semantics: NO finding; the clone
  is the documented a11y superset at every layer.** The reference's
  toast VIEWPORTS are two plain `fixed top-0 z-[100]` divs with NO
  role/aria-live/aria-label, `pointer-events: auto` (the standing R1
  burger-blocker root cause), and its live toasts never fired on
  item-edit-save, line-item save, or line-item delete (measured this
  session — the reference's toasts are rare-path only). The clone's
  viewport: `role="region" aria-label="Notifications (F8)" tabindex=-1
  pointer-events: none` (the R1 fix). The clone's live toast: an
  `li tabindex=0` (Radix's pause-on-focus affordance) PLUS Radix's
  hidden ANNOUNCER — measured inside its 1-second window:
  `<span role="status" aria-live="assertive">Notification Line item
  added</span>` portaled to the body (the foreground-type default) —
  the screen-reader announcement the reference lacks entirely. Pin: S1.
- **Suggestion #4 — the performance/bundle pass: NO finding
  (documented numbers).** The clone's dashboard route ships 12 chunks /
  1,104KB raw / **338KB gzipped** + 147KB raw CSS, with nav 66ms and
  DOMContentLoaded 26ms on the parity server. The reference ships one
  mega-bundle 1,060KB raw / **317KB gzipped** + 68KB CSS + a 214KB
  dev-only `badge.js` (the "Edit with base44" chrome). Wire-weight
  parity (338 vs 317KB gz) while the clone serves a route-split superset
  (per-route lazy chunks, no dev badge). No Lighthouse CLI in this
  environment — the resource-timing + curl census substitutes.
- **The VLM pairwise (two fresh pairs, viewport-verified)**: the
  dashboard — IDENTICAL layout, one flag DOM-explained (the clone's
  Dashboard-active rail = superset #3); the verify-email state — one
  flag DOM-explained (the clone's dev-code hint box = the documented
  honest no-mail dev variant). **Probe lesson: verify the VIEWPORT
  before pairing** — the first dashboard pair this session compared a
  desktop reference against a mobile clone shot (the default
  agent-browser session had a stale 390×844 viewport) and produced a
  phantom full-page layout drift verdict.
- Probe-methodology notes: (a) v4's ring composition puts the visible
  ring in the FOURTH box-shadow layer behind three transparent
  placeholders — a truncated read fabricates a missing-ring finding;
  (b) persistent agent-browser sessions keep their LAST viewport —
  re-assert `set viewport` before VLM pair capture; (c) the clone's
  Radix DialogContent is NOT inside a `div.fixed` — the overlay and the
  content are SIBLINGS in the portal, so probes must anchor with
  `closest('[data-state=open],[role=dialog]')` (two silent probe
  failures this session); (d) the reference's plain-div dialogs ignore
  Escape — never assume a dialog closed; verify the DOM state; (e) the
  reference's register form is a STATE on `/login` (the `/register`
  route 404s) — reach it via the "Need an account? Sign up" link.

## Findings

### G1. [MED] The verify-email code inputs lack the reference's focus family (ring + auto-focus)

The only production-code drift this session. Measured on the live
reference (REAL Tab + settle, the verify state reached via a throwaway
register):

- the reference's focused code input renders `outline: solid 2px
  rgba(0,0,0,0)` (invisible v3 form) + `box-shadow: rgb(255,255,255)
  0px 0px 0px 0px, rgb(9,9,11) 0px 0px 0px 2px, rgba(0,0,0,0) 0px 0px
  0px 0px` — the VISIBLE 2px zinc-950 (`#09090b`) ring with the
  0-width white lead layer;
- the border does NOT tint on focus (stays `rgb(228,228,231)` =
  the resting `#e4e4e7`) — the ring alone signals focus;
- the FIRST code input is auto-focused when the verify state lands
  (measured: `document.activeElement` = the first 40×44 box immediately
  after the register submit) — the user can type the code without
  clicking.

The clone's code inputs (`src/components/budget/login-card.tsx`, the
CodeInputs component) render `focus:border-[#94a3b8]
focus:outline-none`: a slate-400 border TINT the reference never shows,
and NO ring; and there is no `autoFocus`. The v21 session pinned the
verify state's geometry/chrome/autocomplete but never measured the
focus family — this session closes that gap. Note the reference's own
inconsistency: its REGISTER inputs carry the slate-2px/4px family (v13,
pinned) while its CODE inputs carry the zinc-2px family — each surface
is measured and pinned separately (the never-copy-one-family's-color-
onto-another rule).

**Fix (TDD):** replace the focus classes on the six code inputs with
the reference's measured family — `focus:shadow-[0_0_0_0_#fff,0_0_0_
2px_#09090b] focus:outline-none` (the register-input precedent idiom:
the explicit arbitrary shadow, byte-exact to the reference's visible
layers; the trailing zero-width transparent layer is omitted — the
established convention) — and add `autoFocus={i === 0}` to the first
box. No rest-state change (the family is focus-only; the border keeps
`#e4e4e7` at rest AND on focus, matching the reference's untinted
behavior).

### S1. [PIN] The toast's announcement semantics (the Radix announcer)

The session-67 surface #3's measurable contract, now measured and
pinned: the clone's live toast announces via Radix's hidden
`role="status" aria-live="assertive"` portal ("Notification Line item
added") within its 1-second mount window. No production change — a new
e2e assertion in the calculator's line-item-add test (the toast's mount
is synchronous with the save; the read lands ~200ms in, squarely inside
the window) so a future toast-system rewrite (e.g. a sonner swap)
cannot silently drop the announcement. This is the counterpart to the
existing exact:true lesson comments (the announcer double-matches loose
text locators) — the pin makes the announcer itself a first-class
assertion.

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | G1 RED: the code-input focus-family e2e test (auto-focus + the REAL-Tab ring + the untinted border — fails on the drifted build) | test | `tests/e2e/verify-email.spec.ts` |
| 2 | G1 GREEN: the `focus:shadow-[0_0_0_0_#fff,0_0_0_2px_#09090b] focus:outline-none` family + `autoFocus={i === 0}` on the code inputs | fix | `src/components/budget/login-card.tsx` |
| 3 | G1 pin-sanity: remove the shadow family → the test fails; remove the autoFocus → the test fails; restore | verify | same |
| 4 | S1 pin: the announcer assertion in the line-item-add test (role=status + aria-live + the toast text, inside the 1s window) | test | `tests/e2e/calculator.spec.ts` |
| 5 | S1 pin-sanity: stub the announcer out → the pin fails → restore | verify | — |
| 6 | Live re-verification on the :3200 parity server (the REAL-Tab focused code input's shadow byte-compare vs the reference's measurement + the announcer census + the mobile-nav R1/R4 spot check) | verify | — |
| 7 | The 16 screenshots regenerated | docs | `docs/screenshots/` |
| 8 | The v33 probes persisted + the probe README updated (the five lessons) | docs | `scripts/parity-probes/` |
| 9 | Docs aligned (README, CLAUDE, AGENTS, SKILL, session_68, the narrative, worklog) | docs | repo root + `docs/` |
| 10 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `login-card.tsx` CodeInputs (line ~144): the className carries
  `focus:border-[#94a3b8] focus:outline-none` — confirmed the ring is
  absent today (grep: no `focus:shadow` in the code-input class; the
  register inputs at line 202 carry the `focus:shadow-[...]` precedent
  idiom this plan follows). No `autoFocus` anywhere in the file (grep:
  zero matches).
- The register-input precedent (line 202) uses the same arbitrary-shadow
  form — `focus:shadow-[0_0_0_2px_#fff,0_0_0_4px_#94a3b8]
  focus:outline-none` — pinned green since v13; the code-input fix
  follows the identical pattern with the zinc-2px layers.
- `verify-email.spec.ts`: five tests, none touch focus state or the
  code inputs' chrome (grep: `focus` matches nothing in the file); the
  register-class rate-limit budget: 5 existing + 1 new = 6 register
  calls + login-parity's 409 = 7 — under the 10/IP/15min cap (the file
  header's documented budget).
- `calculator.spec.ts` line 112 ("add a line item → parent amount
  recalculates immediately"): the save + `expect(lineDialog).toBeHidden()`
  sequence is the injection point for the S1 announcer assertion — the
  toast mounts with the dialog close, ~200ms before the read; no
  existing assertion queries `[role=status]` in this flow (grep clean
  — the spinner's role=status lives on the loading route only).
- The chain gate: lint → typecheck → 108 unit → build → 165 e2e (166
  after the G1 test; the S1 assertion extends an existing test) → 35
  smoke.
