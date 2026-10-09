# Remediation Plan v30 — Session-59 Parity Iteration

Date: 2026-10-10 · Scope: fresh two-site re-audit after the v29 baseline
(`368712d` + the session-60 transcript doc through `ece66b5` on `main`, all
green per this session's re-run: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · **158/158 e2e ✓ (first run)** ·
35/35 smoke ✓). The workspace survived this time (node_modules, `.env` with
`DATABASE_URL="file:../db/custom.db"`, seeded `db/`, scandihaven all intact).
Probes: the standing disciplines — one-shot `agent-browser eval` (base64 via
run-probe.sh for regex-bearing probes), the :3200 parity server inside ONE
`with-server.sh` invocation, REAL CDP hovers via `mouse move`, parked-pointer
settles, full computed strings.

## The sweep — method and results

The pass swept the session-59 log's four suggested surfaces — the
**dashboard's guideline-row hovers + quick-action card-button hovers** (pinned
in the v2/v4 era, never REAL-hover-diffed), the **savings view's card family**
(a census pass), the **net-worth tablist's arrow-key semantics** (never
measured), and the **details sheet's keyboard semantics at MOBILE** (the
focus-trap geometry at the bottom-sheet breakpoint) — plus the standing
re-verification set (mobile-nav R1–R4 on BOTH sites, data drift, the SEO pair,
the v29 fix in place) and the code audit (`npm audit` = the same 5 dev-only
ESLint `braces` advisories — accepted, unchanged; the secret-pattern scan
matching only the documented files; the v29 changeset re-verified: both
net-worth label strings carrying the hex pins + `zb-badge-hover`).

- **Mobile navigation (the task focus) R1–R4 all re-verified live on BOTH
  sites — the 24th consecutive check.** R1: the reference's two `fixed top-0
  z-[100]` toast containers still intercept the burger's center hit
  (`hitIsBurgerSvg: false`, scrollWidth 395 on `/`), while the clone's burger
  hit is DIRECT on the svg with 390 fit on every route. R2: the reference's
  sheet still traps after nav; the clone's closes (superset fix #2). R3: the
  reference marks nothing active on `/` and has no `<nav>` landmark; the
  clone highlights Dashboard + has the landmark. R4: the reference overflows
  395 on `/`+`/dashboard` and 464 on `/networth`; the clone fits 390 on all
  six routes. **The Tailwind v4 pins hold — the clone's mobile menu works as
  expected.**
- **Data drift clean (24th — the reference only read this session, no probe
  items created)**: allocation 30.5%, Balance `$3475.00`, income
  `$5000.00`/1 (Salary), savings `$1000.00`/1 (Emergency Fund), expenses
  `$525.00`/4 (Miscellaneous, Investments, Netflix, Rent).
- **SEO pair ✓ (the brief's standing ask, deepened this session)**: both
  sites serve `/robots.txt` (allow-all + the sitemap link) and `/sitemap.xml`.
  The full head-metadata census ran for the first time since v7:
  description / og:title / og:description / og:type / twitter:card /
  twitter:title / twitter:description / apple-mobile-web-app-title / title
  all **byte-identical strings**; canonical + og:image keyed off
  `NEXT_PUBLIC_SITE_URL` (the env var's contract); charset + viewport both
  present. The reference's `/manifest.json` endpoint serves **empty** (its
  manifest link is broken); the clone's `manifest.webmanifest` serves the
  full v7-pinned document — a superset.
- **The dashboard guideline rows (suggestion #1a) — NO finding**: the
  reference's rows are `p-4 rounded-lg` divs with inline backgroundColor
  `rgb(255,247,245)` + border `1px solid rgb(252,221,213)` (Needs), radius
  8px, pad 16px, cursor auto, transition-duration 0s — and a REAL CDP hover
  leaves the row UNCHANGED (no hover family; the `group` class on the card
  container never applies to the row). The clone's GUIDELINE_ROWS render the
  identical class string + inline styles with the identical constants
  (`#fff7f5`/`#fcddd5`/`#e07a3b` …), and its REAL hover is equally inert.
  Rest + hover: **byte-identical**.
- **The quick-action card buttons (suggestion #1b) — NO finding (rendered
  parity, two v3↔v4 mechanism notes)**: both sites' buttons carry the exact
  class set `rounded-2xl p-6 text-left transition-all duration-200
  hover:shadow-lg group` (order differs, computes identical), bg white,
  border `1px solid rgb(229,231,227)`, radius 16px, pad 24px, transition
  `0.2s cubic-bezier(0.4, 0, 0.2, 1)`, cursor pointer; the inner icon box
  `w-10 h-10 rounded-xl … group-hover:scale-110 transition-transform
  duration-200`; the Plus `w-4 h-4 ml-auto opacity-50
  group-hover:opacity-100 transition-opacity` (0.15s). Under REAL CDP hover:
  (a) the reference scales its icon via `transform: matrix(1.1,…)` while the
  clone scales via the v4-native **`scale: 1.1` property** — both render the
  identical 40→44px box (the rendered-geometry bar, the v13 precedent);
  (b) the reference's `hover:shadow-lg` computes 4 layers (2 transparent
  lead + `rgba(0,0,0,0.1) 0px 10px 15px -3px, rgba(0,0,0,0.1) 0px 4px 6px
  -4px`) while the clone emits 2 extra TRANSPARENT lead layers ahead of the
  byte-identical visible pair — transparent layers cast nothing (the
  v13/v22 full-string lesson: compare the visible layers); (c) the Plus
  fades 0.5→1 on both. The `@variant hover` + `@variant group-hover` pins
  in globals.css hold (both hovers engage under the probe's real pointer).
- **The savings view's card family (suggestion #2) — NO finding, byte
  identical**: the Emergency Fund card computes the exact family of the
  income/expense cards — `bg-white rounded-xl p-5 cursor-pointer group
  transition-all duration-200 hover:shadow-lg` (border `rgb(229,231,227)`,
  radius 12, pad 20, shadow `rgba(0,0,0,0.04) 0px 2px 8px`, cursor
  **pointer** — the savings card IS clickable); the "monthly" frequency
  badge computes `rgb(250,245,255)`/`rgb(126,34,206)` and the "active"
  status badge `rgb(248,250,252)`/`rgb(51,65,85)` (the v28-pinned
  hex+`zb-badge-hover` family); the 36×36 hover-revealed footer trigger at
  opacity 0 (0.15s). The reference's savings card click opens the SAME
  "Budget Item Details" sheet (measured: the headings + body text flip;
  its reference-side geometry identical to the expense card's v28
  measurement). The clone's shared items-view does exactly this.
- **The net-worth tablist's arrow-key semantics (suggestion #3) — NO
  finding, byte-identical (the reference IS Radix)**: both tablists carry
  `role=tablist` + container `tabIndex=0` + both triggers `tabIndex=-1`
  (the RovingFocusGroup entry-focus pattern — NOT the old static
  "active=0" pattern; a static read showing both -1 is the correct fresh
  state on BOTH sites). The trigger attribute sets are identical down to
  `data-orientation`/`data-radix-collection-item` (only the Radix ID
  namespace differs: `radix-:r0:` vs `radix-_r_3_:`). Behavior measured
  live on BOTH: focus Assets → **ArrowRight** → focus moves to
  Liabilities, `aria-selected` flips, the roving tabindex updates
  (Liabilities `0`, Assets `-1`) — the automatic-activation roving
  contract, identical.
- **The details sheet's keyboard semantics at MOBILE (suggestion #4) — NO
  parity gap; the clone is the accessible superset (now measured at the
  bottom-sheet breakpoint)**: the reference's mobile sheet (its inner panel
  `bg-white rounded-t-3xl md:rounded-2xl shadow-2xl max-w-lg w-full
  max-h-[85vh] overflow-y-auto`) computes x=0, y=127, w=390, h=717
  (maxH 717.4px = 85vh of 844) — the clone's panel computes the
  **byte-identical rectangle** (its `fixed bottom-0 left-1/2
  -translate-x-1/2` self-positioning vs the reference's full-screen
  items-end flex wrapper render the same geometry; the v28
  rendered-parity precedent). Keyboard: the reference opens with NO
  initial focus (activeElement stays BODY), no role/aria-modal — and a
  REAL Tab walk at mobile tours the UNDERLYING page (stops 1–3 measured:
  the expense cards' Edit/Calculate buttons — `activeInSheet: false`;
  the sheet never traps). The clone (Radix): initial focus ON the X
  (Close), all Tab stops land **inside** the dialog (`inDialog: true`
  across the walk — the trap holds at mobile), Escape closes. Same
  verdict as the v29 desktop measurement, now pinned at both breakpoints.
- **The VLM pairwise (two fresh pairs)**: the dashboard
  (quick-actions+guidelines region) — **IDENTICAL** ("none" differences);
  the mobile details sheet — **IDENTICAL** ("none" differences).
- **The topbar avatar** (a census extension): the reference's rail avatar
  (36px `rounded-full`, "U" initial) is NOT clickable — no user menu
  exists; the clone's matches (static, the v4-era pin). No surface.
- Probe-methodology notes: the reference's details-sheet X is best found
  by its sticky-header position (no aria-label; sr-only text on the
  clone's X); a template-literal probe passed inline gets mangled by bash
  — persist regex/`$`-bearing probes as files (the run-probe.sh base64
  discipline); `getComputedStyle().transform` reads `none` for v4's
  `scale-110` (the individual `scale` property is the v4 mechanism —
  read `.scale` and the rendered rect for the rendered-parity verdict).

## Findings — the pin gaps (both are TEST additions; no production-code drift exists)

### G1. [MED] Pin the details sheet's keyboard semantics with an e2e test (desktop + mobile)

The v29 session MEASURED the keyboard semantics (the reference's no-focus /
no-trap / no-Escape family vs the clone's Radix initial-focus / trap /
Escape) but never PINNED them — the item-details spec (v28) covers geometry,
structure, and the action-button independence only. Nothing prevents a
regression of the superset's three guarantees. This session adds the pin:
initial focus lands on the X (Close), the Tab walk stays INSIDE the dialog
(the trap — at DESKTOP and at the MOBILE bottom-sheet breakpoint, where v23
pinned the nav-sheet's trap but not the details sheet's), and Escape closes.
The mobile variant also pins the bottom-sheet geometry numbers measured this
session (x=0, w=390, max-h 85vh) at the computed level.

**Fix (executed — `tests/e2e/item-details.spec.ts`, two new tests in the v28
describe):** (1) "the sheet's keyboard semantics: initial focus on X, Tab
traps, Escape closes" — open the Rent card's sheet, assert activeElement is
the dialog's Close button (sr-only text), press Tab ×3 and assert every stop
remains `inDialog`, press Escape and assert the dialog unmounts; (2) the same
contract at `setViewportSize(390, 844)` plus the computed bottom-sheet
rectangle (w=390, x=0, maxHeight `717.4px` — 85% of 844). Follows the v23
mobile-nav keyboard pattern (real keyboard.press, 60ms per-stop settle, the
350ms ring/transition settle where computed styles are read).

### G2. [MED] Pin the net-worth tablist's roving arrow-key semantics with an e2e test

The tablist's STATIC geometry/colors are pinned (networth.spec v5 G3) but the
**roving behavior** — the Radix contract measured live on BOTH sites this
session — is unpinned: arrow-key focus movement, automatic activation, the
roving tabindex update. A regression (a non-Radix tab rewrite, a
`tabIndex={0}` static override, a `activationMode` flip) would pass every
existing test. This session adds the pin: focus the Assets trigger, ArrowRight
→ the Liabilities trigger becomes focused + `aria-selected=true` + the panel
switches (the seeded liability cards render) + the roving tabindex flips
(Liabilities `0`, Assets `-1`).

**Fix (executed — `tests/e2e/networth.spec.ts`, one new test after the v5
tabs describe):** `page.evaluate` focuses the active trigger, one
`keyboard.press("ArrowRight")`, a settle, then assertions on
activeElement/text, both triggers' aria-selected + tabindex, and the
Liabilities panel's visible heading. The v5 describe's beforeEach (goto
/networth + heading wait) is reused.

## Validation of this plan against the codebase

- G1 scope: `tests/e2e/item-details.spec.ts` — the v28 describe exists with
  3 tests (lines 13/128/164); no keyboard-semantics test exists (`rg
  'keyboard|Escape|activeElement' tests/e2e/item-details.spec.ts` → only the
  X's focus-visible class assertion at line 60). The Rent card + "Budget
  Item Details" heading settle pattern is the file's own; the X exposes the
  sr-only "Close" text (the v29 probe lesson — `getByRole("button", {
  name: "Close" })`).
- G2 scope: `tests/e2e/networth.spec.ts` — the v5 tabs describe (line 375)
  covers the static tablist; no roving test exists (`rg 'ArrowRight' tests/`
  → no hits). The seeded liability cards ("Home Loan" + "Car Loan" per the
  e2e seed) render in the Liabilities panel — the panel-switch assertion is
  data-backed (the seed's `networth.spec` empty-state test names them).
- The suite count goes **158 → 161** (G1 adds TWO tests — desktop + mobile — and G2 adds ONE); no new page flows, no new fixtures, no
  fixture restore needed (both tests are read-only — no data mutations, the
  sheet closes itself on Escape).
- No production code changes this iteration: every measured surface is
  byte-identical, pinned, or the documented superset (the results above).

## Execution order (TDD)

1. **RED-check (G1)**: write the two keyboard tests with one deliberately
   wrong expectation first (e.g. activeElement NOT the Close button) →
   confirm the harness fails → correct it → GREEN.
2. **GREEN (G1)**: the real assertions against the current (correct)
   behavior — the v29/v30 measurements are the spec.
3. **RED-check + GREEN (G2)**: same discipline for the roving test.
4. **Pin-sanity (both)**: mutate one expectation per test (drop the trap
   assertion's dialog containment; flip the expected aria-selected) → FAIL
   → restore → GREEN.
5. Full clean-check chain: `npm run lint && npm run typecheck && npm test &&
   npm run build && npm run test:e2e` + `bash scripts/smoke-test.sh`
   (**161 e2e expected**).
6. Live re-verification on the :3200 parity server (the two probe scripts
   re-run: the mobile sheet trap + the tablist arrows).
7. Regenerate the screenshots (`node scripts/capture-screenshots.mjs`) —
   expected byte-identical (zero production-code change). Align
   README/CLAUDE/AGENTS/SKILL/session log/worklog + the probe README (the
   v30 catalog).

## Risk notes

- Both changes are test-file-only: zero API/store/schema impact, zero data
  risk, zero visual risk. The only regression surface is the suite count (158 → 161) cited in the docs.
- The mobile keyboard test must respect the parked-pointer discipline (the
  v22 G1 lesson) and the Radix sheet's ~200ms ring fade (the v23 settle) —
  the settles are baked into the test bodies.
- The tablist test relies on the e2e seed's Liabilities content (Home Loan /
  Car Loan) — the fixture is re-seeded every run (global-setup), so the
  assertion is stable; no restore needed (read-only test).
- No other surface in the sweep requires a change (all verified
  identical/pinned/superset — see the results above).
