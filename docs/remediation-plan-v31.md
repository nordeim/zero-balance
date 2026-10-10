# Remediation Plan v31 — Session-61 Parity Iteration

Date: 2026-10-10 · Scope: fresh two-site re-audit after the v30 baseline
(`d851d38` + the session-log commits through `f9a9637` on `main`; this
session's re-run of the whole chain green on the FIRST full run: lint ✓ ·
typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**161/161 e2e ✓** · 35/35 smoke ✓). The workspace had been RESET — the repo
re-cloned, the environment rebuilt (node_modules, `.env` with
`DATABASE_URL="file:../db/custom.db"`, `db/` re-pushed + re-seeded,
scandihaven re-cloned). Probes: the standing disciplines — one-shot
`agent-browser eval` (base64 via run-probe.sh for `$`-bearing probes), the
:3200 parity server inside ONE `with-server.sh` invocation, REAL CDP hovers
via `mouse move`, parked-pointer settles, full computed strings, and
full-settle re-reads (the 6s /networth re-measure caught this session's one
timing artifact — a 2.5s settle read a still-loading page as 390; the true
464 matches every prior session).

## The sweep — method and results

The pass swept the three session-61 suggested surfaces — the **dashboard
donut's keyboard semantics** (recharts' own keyboard behavior), the **filter
selects' open-state arrow semantics**, and the **form dialogs' full Tab
order** — plus the standing re-verification set (mobile-nav R1–R4 on BOTH
sites, data drift, the SEO pair, the VLM pairwise) and the code audit
(`npm audit` = the same 5 dev-only ESLint `braces`/eslint-config-next
advisories — accepted, unchanged, dev-only; the secret-pattern scan matching
only the documented files; `.env.example` verified current).

- **Mobile navigation (the task focus) R1–R4 all re-verified live on BOTH
  sites — the 25th consecutive check.** R1: the reference's two `fixed
  top-0 z-[100]` toast containers still intercept the burger's center hit
  (hit `DIV.fixed.top-0.z-[100]`, scrollWidth 395), while the clone's burger
  hit is DIRECT on the svg (`hitIsBurgerSvg: true`) with 390 fit. R2: the
  reference's sheet still traps after nav (overlay + `body overflow: hidden`
  measured on `/income` after the nav click); the clone's closes
  (superset fix #2 — re-verified with the Radix `[role=dialog]` detector:
  sheet opened → link click → sheet closed). R3: the reference marks nothing
  active on `/` (all five rail links `rgb(63,63,70)`, no gradient) and has no
  `<nav>` landmark; the clone highlights Dashboard (gradient + white text) +
  the landmark. R4: the reference overflows 395 on `/`+`/dashboard` and 464
  on `/networth`; the clone fits 390 on all six routes. **The Tailwind v4
  pins hold — the clone's mobile menu works as expected.**
- **Data drift clean (25th — the reference only read this session)**:
  allocation 30.5%, Balance `$3475.00`, income `$5000.00`/1 (Salary),
  savings `$1000.00`/1 (Emergency Fund), expenses `$525.00`/4; the donut's
  Need slice `$6025.00`.
- **SEO pair ✓** (live, both sites): robots.txt (allow-all + sitemap link) +
  sitemap.xml (5 URLs, weekly, 1.0/0.8) + the full head-metadata census —
  description / og:title / og:description / og:type / twitter:card /
  twitter:title / twitter:description / apple-mobile-web-app-title / title
  all **byte-identical**; canonical + og:image keyed off
  `NEXT_PUBLIC_SITE_URL` (the env contract); charset + viewport present on
  both. The reference's `/manifest.json` endpoint 302s to nothing (its
  manifest link is broken); the clone's `manifest.webmanifest` serves the
  full v7-pinned document — a superset. (theme-color and apple-touch-icon
  differ — the reference's own values the clone deliberately does not carry;
  known, non-pinned fields.)
- **The filter selects' open-state arrow semantics (suggestion #2) — NO
  finding, byte-identical behavior**: both sites' category filter is Radix
  (`role=combobox` trigger, `role=listbox` popup, `role=option` items with
  `data-highlighted`). Open → "All Categories" highlighted + activeElement
  on the option DIV; ArrowDown → next option highlighted; ArrowDown at the
  end → stays (no wrap); ArrowUp → back. Identical roving on both sites
  (the reference's option list is its live data — 2 options vs the clone's
  seeded 3 — a data difference, not a semantics difference).
- **The form dialogs' full Tab order (suggestion #3) — ONE finding (G2
  below), otherwise byte-identical**: the strict focusable census (tabindex
  property, aria-hidden excluded, 1×1 hidden excluded) on the Add Income
  dialog reads the SAME 14-field sequence on both sites — X close → Type
  combobox → Amount → classification radiogroup → Category → Subcategory →
  Frequency combobox → Date → Payment Method → Status combobox → Recurring
  switch → Notes → Cancel → Save Item. The reference's native `<select>`
  shadows (1×1, `tabindex=-1`, `aria-hidden`) are correctly NOT Tab stops on
  either site. The ONLY census delta: the reference's classification field
  contributes TWO stops (the radiogroup container AND the checked tile's
  radio BUTTON), the clone's one (container only) — G2.
- **The dashboard donut's keyboard semantics (suggestion #1) — THREE
  recharts-3-vs-2.15 drifts (G1 below)**, measured at the computed + live
  behavior level on both sites: the chart surface, the tooltip's live-region
  semantics, and the sector arrow-roving.
- **The VLM pairwise (two fresh pairs)**: the dashboard — DIFFERENT flags,
  all DOM-explained (the clone's Dashboard-active rail = superset #3; the
  allocation bar length + the avatar initial = seeded-data differences); the
  Add Income dialog — DIFFERENT flag, DOM-explained (the clone's X renders
  its v27-pinned 1px `ring-1` on open because Radix focuses it — the
  documented v29 superset; computed arbitration: both X's byte-identical at
  rest — 36×36, border 0, radius 6, transparent bg, no outline, #0a0a0a).
- Probe-methodology notes: a 2.5s post-navigation settle can read a
  still-loading route as non-overflowing (the /networth 390-vs-464 artifact
  — re-measure with a 6s settle before declaring drift); the dialog X finder
  must scope to the topmost fixed overlay (a page-wide 36×36+svg filter
  matches the card action buttons underneath); SVG elements without a
  `tabindex` attribute read `.tabIndex === -1` (property) — distinguish
  "attribute absent" from "attribute -1" before claiming parity.

## Findings

### G1. [MED] The donut's keyboard semantics — the recharts-3 a11y defaults drift from the reference (recharts 2.15)

Three sub-drifts, all measured live on both sites:

**(a) The chart surface is an extra Tab stop.** The clone's
`svg.recharts-surface` renders `tabIndex="0"` + `role="application"`
(recharts 3's `accessibilityLayer` defaults ON — `useAccessibilityLayer()`
reads `?? true`), and when focused it renders an **unpinned 5px
`outline: auto` focus ring** (the browser default — not any of the project's
pinned ring families). The reference's surface has **NO tabindex attribute
and no role** — it is inert (recharts 2.15 only sets surface attrs when
`accessibilityLayer` is explicitly true, which the reference does not set).
Keyboard users get one extra Tab stop on the clone, and screen readers get a
spurious `application` role.

**(b) The tooltip renders live-region semantics.** The clone's
`.recharts-default-tooltip` div carries `role="status"` +
`aria-live="assertive"` (recharts 3's DefaultTooltipContent when the a11y
layer is on). The reference's tooltip renders NEITHER attribute (measured on
its hovered tooltip: wrapper `tabindex=-1`, inner div no attrs).

**(c) The pie's arrow-key sector roving is MISSING.** The reference
(recharts 2.15.3) attaches `pieRef.onkeydown` in `componentDidMount`
(`attachKeyboardHandlers`) with an idiosyncratic contract:
- `ArrowLeft` → `sectorToFocus = ++n % len` → focus that sector g (forward,
  wraps);
- `ArrowRight` → `sectorToFocus = --n` (if `< 0` → `len-1`) → focus that
  sector (BACKWARD, wraps — so the FIRST ArrowRight from a fresh pie focuses
  the LAST sector in DOM order);
- `Escape` → the tracked sector `.blur()`s (focus resets to BODY) and the
  index resets to 0;
- `ArrowDown`/`ArrowUp`/`Enter`/etc: nothing; `altKey`-modified arrows:
  nothing; no `preventDefault` (arrows keep scrolling the page — the
  reference does not suppress it).

The sectors themselves are `tabIndex="-1"` on BOTH sites (focusable only
programmatically), and the pie layer `g.recharts-pie` is `tabIndex="0"` on
BOTH sites (recharts' `rootTabIndex: 0` in 2.15 AND 3.10 — parity holds
there). Live behavior measured on the reference: layer.focus() holds →
ArrowRight → `g.recharts-pie-sector[tb=-1]` focused (no tooltip appears) →
Escape → BODY. The clone (recharts 3.10.1): the layer focuses, the arrows do
nothing (recharts 3 removed the pie keyboard handlers entirely — the
sector-Shape code has no key handling and the a11y manager only covers
cartesian axes).

**Fix (executed — `src/components/budget/dashboard-view.tsx`):**
1. `<PieChart accessibilityLayer={false}>` — the explicit prop overrides the
   `?? true` default: the surface loses its tabindex + role (RootSurface's
   `hasAccessibilityLayer ? 0 : undefined` / `? 'application' : undefined`),
   and the tooltip's DefaultTooltipContent loses `role=status` +
   `aria-live=assertive`. Both sub-drifts (a) and (b) die with one prop.
2. A `usePieKeyboardParity` effect on the donut wrapper replicates (c) —
   the reference's exact `attachKeyboardHandlers` contract (ArrowLeft ++
   wrap / ArrowRight -- wrap / Escape blur+reset / altKey-ignored /
   no preventDefault), attached as an `onkeydown` DOM property on the
   wrapper (event delegation: the layer's keydowns bubble there — avoids the
   ResponsiveContainer mount race that a direct `.recharts-pie` attachment
   would hit; the wrapper handler fires for exactly the focus states the
   reference's layer handler can, since the layer is the only focusable
   chart element on both sites).

### G2. [MED] The classification tiles' fresh roving state — the checked radio is not a Tab stop

The reference's fresh dialog renders the classification field with TWO Tab
stops: the radiogroup container (`tabIndex=0` — the Radix RovingFocusGroup
entry-focus pattern, identical on both sites) AND the CHECKED tile's radio
BUTTON (`tabIndex=0`; the unchecked tiles are `-1`). The clone's fresh state
renders ALL three radios at `-1` (one stop: the container only). The
reference's older Radix ties the fresh roving tabindex to the checked state
— its fresh DOM census (`container 0, checked 0, unchecked -1`, re-verified
on a fresh Escape + reopen with zero prior interactions) proves it.

The keyboard BEHAVIOR already matches (measured live on both sites: Tab into
the container → ArrowDown → focus lands on the checked tile; ArrowRight →
focus + check move together with the roving tabindex following — automatic
activation, identical). The delta is the FRESH static DOM: on the reference
a keyboard user Tabs container → checked radio → Category (two stops in
the field); on the clone container → Category (one stop). Since checking
always follows focus (automatic activation), a checked-based static
tabindex is equal to the reference's roving tabindex in every reachable
state.

**Fix (executed — `src/components/budget/budget-item-dialog.tsx`):**
`<RadioGroupItem value={c} tabIndex={selected ? 0 : -1} />` — the explicit
prop flows through RovingFocusGroup.Item's `...itemProps` spread and
overrides the computed `isCurrentTabStop` value, rendering checked → 0 /
unchecked → -1 in the fresh state AND tracking every later check change
(the `selected` prop re-renders with the form state).

## Validation of this plan against the codebase

- G1 scope: `src/components/budget/dashboard-view.tsx` — the
  `SpendingBreakdownCard` renders `<PieChart>` (line ~558) with no
  `accessibilityLayer` prop today; recharts 3.10.1's RootSurface
  (`node_modules/recharts/es6/container/RootSurface.js`) documents the
  override order — an explicit `tabIndex`/`role` wins, else the a11y layer
  default. The tooltip pins (formatter/contentStyle/itemStyle, v14) are
  untouched — `accessibilityLayer` does not affect them. No existing spec
  asserts the surface's tabindex/role or any donut keyboard behavior
  (`rg 'recharts-surface|accessibilityLayer' tests/` → no hits), so no
  pinned contract regresses.
- G1(c) implementation surface: the donut wrapper `div` (height 300)
  already exists around the ResponsiveContainer; the effect is DOM-only
  (no setState — the react-hooks v6 `set-state-in-effect` rule is not
  engaged). The `SectorsWithAnimation` path is inert
  (`isAnimationActive={false}` — the sector DOM is stable from mount).
- G2 scope: `src/components/budget/budget-item-dialog.tsx` — the tiles map
  (line ~196-228) already computes `selected = form.classification === c`;
  the RadioGroupItem is the only RadioGroup in the app
  (`rg 'RadioGroup' src/` → budget-item-dialog + the ui primitive). No
  existing spec asserts the tiles' tabindex
  (`rg 'tabindex' tests/e2e/dialog-buttons.spec.ts` → no hits); the v20
  tile-visual specs (16px icons) are untouched.
- The suite count goes **161 → 164** (G1 adds TWO tests — the surface/
  tooltip a11y census + the arrow-roving contract; G2 adds ONE — the tiles'
  fresh roving census + Tab order). No new page flows, no new fixtures, no
  fixture restore needed (all three tests are read-only; the dialog closes
  itself on Escape/Cancel).
- Existing Tab-walk specs (`mobile-navigation`, `item-details`) walk the
  nav sheet and the details sheet — surfaces unaffected by either fix (the
  dialog Tab order gains a stop in the middle of the form, not before it).

## Execution order (TDD)

1. **RED (G1)**: write the two donut keyboard tests in
   `tests/e2e/dashboard.spec.ts` with the current (drifted) expectations
   inverted — surface `tabindex="0"`/`role="application"` present, no
   roving — to prove the harness sees today's behavior → FAIL against the
   reference-derived expectations → flip to the real assertions.
2. **GREEN (G1)**: `accessibilityLayer={false}` + the keyboard-parity
   effect → the tests pass.
3. **RED (G2)**: the tiles' fresh census test (assert the checked radio
   `tabIndex === 0`) → FAIL today (reads -1).
4. **GREEN (G2)**: the `tabIndex={selected ? 0 : -1}` prop → pass.
5. **Pin-sanity mutations**: remove the a11y prop (surface regains
   tabindex/role → test 1 fails); drop the Escape clause (test 2 fails);
   flip the tile prop to `{-1}` (test 3 fails) → restore → GREEN.
6. Full clean-check chain: `npm run lint && npm run typecheck && npm test &&
   npm run build && npm run test:e2e` + `bash scripts/smoke-test.sh`
   (**164 e2e expected**).
7. Live re-verification on the :3200 parity server: the surface census, the
   tooltip attrs, the ArrowRight→LAST-sector roving, the Escape reset, and
   the tiles' fresh census — against the reference measurements above.
8. Regenerate the screenshots (`node scripts/capture-screenshots.mjs`) —
   zero visual change expected (both fixes are keyboard/DOM-attribute
   level). Align README/CLAUDE/AGENTS/SKILL/session log/worklog + the
   probe README (the v31 catalog + this session's lessons).

## Risk notes

- Both fixes are keyboard-semantics-level: zero visual surfaces change
  (the donut renders identically; the tiles render identically). The
  regression surface is the e2e count (161 → 164) and the two production
  files touched.
- The G1(c) replicator must NOT preventDefault (the reference doesn't —
  arrows keep their page-scroll default on both sites) and must ignore
  alt-modified arrows (the reference's `if (!e.altKey)` guard).
- The G2 tabIndex prop rides `...itemProps` AFTER RovingFocusGroup's
  computed tabIndex in the Primitive spread — verified in the installed
  Radix (1.4.8) source; if the spread order ever flips on a Radix bump,
  the pin-sanity mutation catches it.
- The donut roving test asserts the LAST-sector-first quirk
  (`--0 → len-1`) — this is the reference's measured contract, not a
  convention choice; do not "fix" it to forward-first.
