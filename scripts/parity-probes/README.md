# Parity probes (session-3 audit tooling)

One-shot browser probes (run via `agent-browser eval "$(cat <file>.mjs)"`)
used during the deep parity audit against the live reference and the
remediated clone — see `docs/remediation-plan-v2.md` and
`docs/session_3.md`. Kept for future re-audits: each file is
self-contained (no imports) and targets one surface.

- `probe-ref-dashboard.mjs` — hero/stat/breakdown/legend/guidelines/add-button evidence
- `probe-ref-html*.mjs` — raw HTML dumps (hero, quick actions, donut, guidelines, breakdown)
- `probe-ref-bd.mjs` — full breakdown card dump
- `probe-ref-live2.mjs` — legend/guidelines/quick-action/stat-card live DOM
- `probe-clone-parity.mjs` — the same dashboard evidence on the clone (side-by-side)

Session-5 additions (remediation-plan-v3 audit):

- `probe-structural-v3.mjs` — h1/quick-action/stat-count/breakdown/avatar/nav/guidelines/legend computed styles
- `probe-followup-v3.mjs` — avatar fills, donut label DOM, visible nav links, breakdown expansion
- `probe-donut-nav.mjs` — standalone percentage-label location + Dashboard-link active states
- `probe-items-v3.mjs` / `probe-view-dump.mjs` — items-view header/card/badge dumps (ref markup uses div badges; the clone's span badges render identically)

Session-7 additions (remediation-plan-v4 audit) — run via
`agent-browser eval "eval(atob('$(base64 -w0 <file>)'))"` (raw `$(cat …)`
quoting mangles `$` inside regexes):

- `probe-dashboard-v4.mjs` / `probe-followup-v4.mjs` / `probe-legend-v4.mjs` —
  hero/stat/donut/legend/guidelines/quick-action/nav/avatar evidence
- `probe-nav-v4.mjs` / `probe-navlink-detail-v4.mjs` / `probe-nav-hover-v4.mjs` —
  nav-link geometry + classes (found the 40px-vs-32px h-8 gap) + hover states
- `probe-items-v4.mjs` / `probe-item-card-v4.mjs` / `probe-badges-v4.mjs` /
  `probe-footers-v4.mjs` — items-view structure scoped to `main`
- `probe-networth{,2,3,4}-v4.mjs` / `probe-nw-panel-v4.mjs` — net-worth
  summary card leaf dump (found the 3-col-vs-2-col + footer-row gap),
  ratio element, tab-panel cards
- `probe-outline-v4.mjs` / `probe-desktop-chrome-v4.mjs` — page outlines and
  desktop header/rail/padding geometry
- `probe-mobile-v4.mjs` / `probe-hamburger-v4.mjs` — mobile layout geometry +
  the toast-viewport hit-test (reference bug #1)
- `probe-overflow-v4.mjs` — per-view scrollWidth check (found the reference's
  395px/464px mobile overflows and the clone's 428px net-worth case)
- `probe-nw-overflow-v4.mjs` / `probe-shell-chain-v4.mjs` / `probe-isolate-v4.mjs` —
  overflow culprit isolation (hide-one-by-one binary search)
- `probe-dialog{,2,3}-v4.mjs` — dialog panel geometry + classification-tile
  markup (the ref has no `role="dialog"`; climb from the heading)
- `probe-savings-v4.mjs` / `probe-empty-type.mjs` — savings add-button
  gradient + the filtered empty-state check

Session-13 additions (remediation-plan-v7 audit) — head/brand/login/mobile
surfaces, same run-probe.sh pattern:

- `probe-v7-refdata.mjs` / `probe-v7-dash-sweep.mjs` — reference data state +
  dashboard broad-sweep (hero/stat/legend/gradient hashes)
- `probe-v7-headings.mjs` / `probe-v7-sidebar-head.mjs` / `probe-v7-brandfull.mjs`
  / `probe-v7-iconbg.mjs` / `probe-v7-railgeom.mjs` / `probe-v7-asidehtml.mjs`
  / `probe-v7-navstruct.mjs` — the rail brand block (found the 20px-vs-24px
  target + text-base-vs-text-lg logo), label/link geometry, ul wrapper
- `probe-v7-mobile-topbar.mjs` / `probe-v7-sheet.mjs` / `probe-v7-sheet2.mjs`
  / `probe-v7-closebtn.mjs` / `probe-v7-mobile-items.mjs` — mobile chrome
  (found the 12px-squeezed toggle icon + the sheet border/overlay drifts)
- `probe-v7-login.mjs` / `probe-v7-login2.mjs` / `probe-v7-login3.mjs`
  / `probe-v7-login-flow.mjs` — the login card's full computed slate map
  (found the lab/oklab drifts + the missing text-sm) + a form-submit probe
- `probe-v7-404.mjs` / `probe-v7-head.mjs` — the reference's custom 404
  structure + its head metadata (description, OG/Twitter, canonical,
  manifest, apple meta)
- LESSON (SKILL §12.13): `probe-v7-iconbg.mjs`'s 60-char shadow slice caused
  a false "missing ring" finding — always dump FULL computed strings.

Session-15 additions (remediation-plan-v8 audit) — the parity server booted
detached this session (`(bun .next/standalone/server.js … &)` survives across
tool calls), so agent-browser sessions `ref8`/`clone8` drove both sites
directly:

- `probe-v8-data.mjs` — reference data state (hero figure/allocation,
  stats, legend) for drift detection against the session-13 snapshot
- `probe-v8-mobile-nav.mjs` / `probe-v8-mobile-nav2.mjs` /
  `probe-v8-hamburger.mjs` — the mobile topbar/toggle/toast-viewport
  audit (R1 hit-test, R2 sheet-trap, R4 overflow, toggle geometry)
- `probe-v8-sheet.mjs` — sheet + overlay geometry with the sheet open
- `probe-v8-rail.mjs` / `probe-v8-rail-ref.mjs` — desktop rail audit (the
  ref's rail is NOT an `<aside>` — find it by geometry; found the
  `text-zinc-700` → `lab()` inactive-link drift)
- `probe-v8-page.mjs` — per-page mobile sweep (overflow + h1 + card
  headings on all five routes)
- Footer/badge findings came from inline `agent-browser eval` probes (the
  ref's dialogs have no `[role=dialog]` — climb from the Save button; its
  badges are DIVs, the clone's are SPANs — match by text)

Session-17 additions (remediation-plan-v9 audit) — same detached :3200
parity server + `ref9`/`clone9` desktop sessions and `reflog9`/`clonelog9`
fresh unauthenticated login sessions:

- `probe-v9-data.mjs` — reference data-state drift check (hero figure +
  allocation) — unchanged since session 11
- `probe-v9-dash.mjs` / `probe-v9-stat-cards.mjs` — hero/stat-card/guideline
  sweep at computed depth (found the hero bar's 9999px vs 33554432px radius)
- `probe-v9-donut-labels.mjs` / `probe-v9-donut-angles.mjs` /
  `probe-v9-donut-bbox.mjs` / `probe-v9-donut-hit.mjs` — the donut deep
  dive: sector path d-attribute angular math + label fills/positions +
  bounding boxes (found the value-DESC data-order convention and the
  clone-only label connector lines)
- `probe-v9-mobile.mjs` — the mobile stack re-verification (R1/R2/R4 +
  toggle hit-test; scroll to top before hit-testing — the topbar scrolls
  off during audits)
- `probe-v9-dialog-form.mjs` / `probe-v9-dialog-detail.mjs` — form-dialog
  internals at computed depth (labels/inputs/selects/radios/switch/
  textarea/footer; the ref's dialogs have no `[role=dialog]` — find the
  panel via its `fixed inset-0 z-50` overlay, then the first white card
  child; found the X-close/header-height/label-line-box/tile-line-height
  and switch/radio token drifts)
- `probe-v9-login-states.mjs` — the login card's three states at computed
  depth from fresh sessions (found the 14px button text + the per-state
  44/48px control geometry; withdrawn: the card border-color difference —
  both cards render border-width 0)

Session-19 additions (remediation-plan-v10 audit) — this session's sandbox
returned to reaping background processes (session-11 behavior D-9), so the
parity server booted PER COMMAND through `with-server.sh` (the agent-browser
daemon still persists across tool calls — sessions survive, the server
doesn't; do the navigate + settle + probe inside one with-server
invocation):

- `probe-v10-data.mjs` / `probe-v10-hero.mjs` / `probe-v10-hero2.mjs` —
  reference data-state drift check (hero2 is the precise body-text-regex
  form; the hero variant's smallest-div heuristic truncates the card) —
  unchanged since session 11 (+$3475.00, 30.5%)
- `probe-v10-mobile-nav.mjs` / `probe-v10-mobile-nav2.mjs` /
  `probe-v10-mobile-nav3.mjs` — the mobile stack re-verification (R1
  toast-block hit-test — agent-browser's own actionability check REFUSES
  the ref's burger click, which is itself live confirmation of R1 — plus
  burger/topbar/brand geometry; nav3 finds the burger by TEXT content
  ("Toggle Sidebar"), not aria-label — the ref's accessible name comes
  from its text node)
- `probe-v10-select-open.mjs` — the Select popover OPEN state (trigger
  click + follow-up eval for the listbox/options; identical both sides)
- `probe-v10-dialog-scroll.mjs` — tall-dialog scroll mechanics (panel
  max-height/overflow, sticky header, static footer, scrollable form;
  identical — note the clone's panel needs `[role=dialog]`, the ref's
  needs the overlay-climb)
- `probe-v10-drilldown.mjs` + inline row evals — the breakdown drill-down
  EXPANDED state (collapsed row 254×64; subcategory rows 28px with the
  #f9fafb tint — identical)
- `probe-v10-guidelines.mjs` + leaf evals — the Budget Guidelines leaf
  typography (per-type colored percentages; text-only card, no bars —
  identical; the card finder must strip whitespace, "Savings ~20%" spans
  two text nodes)
- `probe-v10-sheet-internals.mjs` — the mobile sheet's brand block/nav
  rows/avatar/user-footer at mobile depth (identical; run on the REF with
  its R2-trapped sheet, on the CLONE after a JS burger click)
- `probe-v10-verify-fix.mjs` — the post-fix live verification driver
  (opens the sheet on the fixed build; the measure probe then asserts the
  active-link gradient/white/500 exactly matches the reference's)

Session-21 additions (remediation-plan-v11 audit) — same with-server.sh
per-command pattern; sessions `ref11`/`clone11` (desktop 1280×800) +
`ref11m`/`clone11m` (390×844), then fresh `ref12`/`clone12` for the
post-fix verification:

- `probe-v11-viewport.mjs` / `probe-v11-viewport2.mjs` — the tablet /
  intermediate breakpoints (767/768/1024): rail-vs-mobile-chrome switch,
  burger hidden state, main offset, content column position — identical
  (at 768 the ref offsets main to x=256 while the clone PADS it — the
  visible column is identical; the DOM approach differs, the pixels
  don't)
- `probe-v11-rail-hover.mjs` — the desktop rail's inactive-link hover
  (synthetic mouseover does NOT trigger CSS :hover — use agent-browser's
  native `hover` with an `a[href]` selector; measured `rgb(24,24,27)` on
  `rgb(240,253,244)` — identical)
- `probe-v11-hero-status.mjs` — the NET ZERO GOAL status badge (label +
  value colors for the live Under Budget state — identical; the regex
  must exclude the "NET ZERO GOAL" heading to find the badge)
- `probe-v11-filter.mjs` / `probe-v11-filter-fn.mjs` — the filter card
  geometry + live search behavior (React-controlled input needs the
  native value setter + input event; "zzz" reaches the FILTERED empty
  state on both sites)
- `probe-v11-filtered-empty.mjs` — the filtered empty state (found G1:
  the ref's heading is 20px, the clone's was 18px)
- `probe-v11-card-badges.mjs` — the income item-card badge census (any-tag
  leaf scan; the ref's badges are DIVs with svg children, the clone's
  SPANs — visually identical; the card finder must anchor on the item
  name + amount, not on buttons)
- `probe-v11-dialog-overlay.mjs` — the dialog overlay + panel (forest
  0.5 scrim, 672×720 panel — identical)
- `probe-v11-btn-focus.mjs` / `probe-v11-btn-shadows.mjs` — the button
  focus-visible + ambient-shadow census (found G2: the ref's gradient
  buttons carry v3's BARE shadow + the shadcn ring on focus; the clone
  fell through to the browser default; programmatic
  `focus({focusVisible:true})` works in Chromium — TS's DOM lib lags the
  option)
- `probe-v11-clone-calc.mjs` — the calculator's sm + outline button
  variants (panel 768×515 identical; found the outline variant's missing
  shadow-sm)
- `probe-v11-verify-fix.mjs` … `probe-v11-verify-fix4.mjs` — the post-fix
  live verification (Add button 147 = 147 / icon 16 / bare-shadow /
  opacity 1; empty heading 20px both sides; the Save focus ring
  byte-identical; the calculator variants matched)
- **Full-string hygiene (lesson 25):** computed `box-shadow` strings are
  multi-layer with the visible layer often LAST behind transparent lead
  layers — never `.slice()` them when diffing (a truncated read nearly
  produced a false "shadowless panel" finding this pass)

Session-23 additions (remediation-plan-v12 audit) — same with-server.sh
per-command pattern; sessions `ref12`/`clone12` (desktop 1280×800) +
`ref12m`/`clone12m` (390×844), then fresh `ref13`/`clone13` (+ `ref13m`)
for the post-fix verification. This pass's probes were one-shot
`agent-browser eval` scripts (kept as /tmp snippets; the reusable
lessons are the patterns):

- **login error state** (found G1): submit a wrong password on both
  sites and measure the `[role=alert]` slot — the ref renders a DIV
  banner (bg `rgba(254,242,242,0.7)`, border `rgb(254,202,202)`, radius
  12, pad 16, box 368×54) with a centered `#b91c1c` 14px/400 inner div
  (the shadcn FormMessage pattern; find it via the computed bg color,
  not class names). The same banner renders the sign-up mismatch error
  — reach that state with mismatched confirm passwords (pure
  client-side, no auth API budget).
- **per-route document.title** (found G2): `agent-browser eval
  "document.title"` after each `open` — one shot per route; the ref's
  titles land client-side after SPA navigation (give it ~2.5s), the
  clone's now ship statically in the prerendered HTML.
- **forgot-password confirmation state** (found G4): click "Forgot
  password?" → fill → submit, then measure the replaced card state (H2
  24px/700, descriptions 16px `#475569`/`#09090b`, back 14px/500
  `#64748b` — all centered). The ref PRETENDS the mail was sent
  ("Check your email"); the probe records the layout, the honest-copy
  decision lives in the clone.
- **a11y sweep** (no drift): `document.querySelector('main'/'aside'/
  'h1')` + `document.documentElement.lang` + accessible button names
  on both sites — found the login root landmark gap (G3) and confirmed
  the clone's desktop `aside` rail is an a11y superset over the ref's
  div rail.
- **payment-method filter + listbox OPEN state** (no drift): the three
  216×36 triggers + the 218px listbox with 32px options — identical;
  the option COUNT differs only by data (the ref's items carry no
  payment methods).
- **sheet Escape behavior** (observation): the ref's mobile SHEET
  closes on Escape (unlike its dialogs, R5) — `agent-browser press
  Escape` after opening; the clone's Radix sheet matches.
- **title-race diagnosis (lesson 27):** to watch `document.title`
  fight React Float, install an in-page 20ms `setInterval` poller via
  Playwright `addInitScript` (a MutationObserver never attaches — init
  scripts run before the parser builds `<head>`). Observed: title set
  at 260ms, reset at 284ms by the Float re-emission — the fix is
  route-segment metadata, never a client effect.
- **agent-browser daemon pressure:** `close --all` can hang under
  memory pressure (CDP `Connection refused` on new sessions) — close
  sessions one at a time with `timeout 25` wrappers and retry; the
  daemon recovers without a restart.

Session-25 additions (remediation-plan-v13 audit):

- `probe-v13-ref-mobile.mjs` — the task-focus re-verification on the
  reference (R4 overflow + toast-container census + burger geometry;
  the R1 hit-test needs the label-free finder — see below).
- `probe-v13-register-err.mjs` — the register duplicate-email 409
  banner (text + chrome) on either site; sign-up state, existing
  account email + matching valid passwords → 409 before any write.
- `probe-v13-input-focus.mjs` — the login inputs' :focus ring (email +
  password): border #94a3b8 + the two-layer shadow; settle 350ms
  (transition-colors animates the border, not the shadow).
- **burger finder gotcha:** `button[aria-label*='enu']` is
  case-SENSITIVE and the ref's burger has NO aria-label — find it by
  text content (`textContent.includes('Toggle Sidebar')`, an sr-only
  span) and open the ref's sheet by mouse-clicking the burger's
  EXPOSED BOTTOM half (y≈40 at 390px — the toast container covers
  y<32); agent-browser's actionability check refuses the covered
  center click.
- **trapped-sheet observation (lesson 30):** the ref's sheet-active
  text color is STATE-dependent — fresh-open renders the pinned white,
  the post-nav trapped re-render renders dark #18181b
  (`sidebar-accent-foreground`). Measure BOTH states before pinning
  sheet styles; the clone only ever has the fresh-open state.
- **register/Google probes:** the ref's "Continue with Google"
  redirects the whole tab to accounts.google.com (Base44 OAuth) —
  navigate BACK afterwards (`open <app>/login`); the authed `/login`
  visit renders the card on both sites (no redirect).
- **zombie sessions:** a dead CDP session can refuse `close` forever —
  work around it (new sessions still work); `close --all` may also
  leave one behind.

Session-27 additions (remediation-plan-v14 audit) — same with-server.sh
discipline (the wrapper is now committed at `scripts/with-server.sh`;
boot the standalone build on :3200 per command, login inside ONE
invocation, `agent-browser set viewport <w> <h>` for geometry):

- `probe-v14-data-drift.mjs` — the dashboard data-state drift check on
  either site (allocation %, totals, item counts, sign conventions).
- `probe-v14-ref-burger.mjs` — the R1 hit-test via the sr-only
  "Toggle Sidebar" text finder (the v13 gotcha, formalized): center hit
  intercepted by the toast container, bottom-half hit direct.
- `probe-v14-nw-tabs.mjs` — net-worth tablist semantics (roles,
  aria-selected, geometry, active tint) + keyboard flow via
  `press ArrowRight/ArrowLeft` (focus + activation both sites).
- `probe-v14-dialog-focus2.mjs` — dialog initial focus: finds the panel
  via the "Add Budget Item" heading's fixed ancestor (the ref has no
  role=dialog — plain fixed divs) and reports `document.activeElement`
  (ref: the TRIGGER button stays focused — no focus move; clone: Radix
  focuses the 36×36 Close button).
- `probe-v14-donut-hover.mjs` — dispatches pointer/mouse events on the
  first `.recharts-pie-sector path` and captures the
  `recharts-default-tooltip` value/chrome (found G1: raw value, wrong
  border/radius/shadow, sector-colored item text).
- `probe-v14-guideline-hover.mjs` / `probe-v14-accordion-hover.mjs` —
  guideline rows + breakdown section buttons: rest vs hover computed
  styles (no hover state on either side) + a user-select sweep.
- `probe-v14-nw-visual.mjs` — verifies the VLM-flagged net-worth diffs
  in the DOM (found G2 tab icons + G3 header chip; refuted the
  divider/ratio-icon/active-tint flags — computed styles are ground
  truth over VLM impressions).
- **VLM sweep discipline:** a three-page screenshot comparison
  (ref vs clone, `z-ai vision -i ref.png -i clone.png`) surfaced the
  G2/G3 candidates in minutes — but EVERY flagged diff must be
  DOM-verified before it becomes a finding (this pass: 3 real, 4
  refuted as VLM misreads or data-driven).
- **session-cookie note:** `agent-browser close` wipes session cookies
  on restart (the e2e-run discipline) — re-login after closing
  sessions mid-audit.

Session-29 additions (remediation-plan-v15 audit) — sessions
`ref16`/`clone16` desktop + `ref16m`/`clone16m` mobile, the :3200 parity
server per `scripts/with-server.sh`:

- `probe-v15-refdata.mjs` / `probe-v15-refdata2.mjs` — the reference
  data-drift check (allocation %, Net Balance, stat-card totals, donut
  legend — unchanged since session 19: 30.5%, +$3475.00).
- `probe-v15-burger.mjs` — the R1 hit-test formalized as a reusable
  probe: burger geometry + the full `elementsFromPoint` hit stack + the
  toast-container census (`toastContainers: 2` on the ref, 0 on the
  clone; `svgDirectHit` is the assertion).
- `probe-v15-loading.mjs` — the LOADING-state census (never measured
  before v15): busy indicators (aria-busy/progressbar/skeleton
  classes/spin animations), "Loading" text, main content count, and
  `dataLoaded` — run immediately after `open` to land inside the fetch
  window (found G1: the ref renders a spinner; the clone had none
  visible at that moment).
- `probe-v15-loading2.mjs` / `probe-v15-loading3.mjs` /
  `probe-v15-loading4.mjs` — the spinner's full chrome + container
  chain (`fixed inset-0 flex items-center justify-center`, transparent,
  the toast viewport as the only sibling), and the under-overlay DOM
  census (the ref's #root holds ONLY the overlay + toast viewport — no
  rail/header/main; body bg WHITE). LESSON: a rotating element's
  `getBoundingClientRect()` measures the ROTATED box (the 32×32
  spinner measured 38–40px) — use `offsetWidth/offsetHeight`.
- `probe-v15-select-kb.mjs` + real `press ArrowDown/Enter` — the
  filter-select KEYBOARD flow (found the ref's internal inconsistency:
  its filter selects highlight the option AFTER the current value on
  open, its dialog selects highlight the current value — the clone's
  uniform Radix matches the dialog/a11y pattern; documented, no action).
- `probe-v15-sheet-close.mjs` — the R2 clone-side sheet close-on-nav
  check ( Income link geometry + post-nav sheet/overlay/scrollWidth).
- **route-delay technique (e2e only):** the loading window is ~5ms on
  localhost — reproduce it deterministically with Playwright
  `page.route()` + `waitForTimeout` before `route.continue()`, and
  `page.unrouteAll({ behavior: "ignoreErrors" })` before the spec ends
  (in-flight route callbacks outliving the test fail it).

Session-31 additions (remediation-plan-v16 audit) — the error/network-
failure surface class, same run-probe.sh pattern:

- `probe-v16-refdata.mjs` — the tenth data-drift check on the reference
  (hero figure + stat totals; unchanged since session 19).
- `probe-v16-burger.mjs` — the R1 burger hit-test (v16 re-verification;
  the find-by-regex fix for the querySelector quoting trap).
- `probe-v16-sheet-close.mjs` — the R2 clone-side sheet close-on-nav
  check (clicks the Income link via `el.click()` — the sheet link
  geometry + the post-nav trap/scrollWidth read).
- `probe-v16-rail.mjs` — the R3 root-route rail-link computed styles
  (the ref marks nothing active on `/`; the clone highlights Dashboard).
- `probe-v16-overflow.mjs` — the R4 six-route scrollWidth sweep (SPA-nav
  variant; the ref's `/networth` 464px case needs a full-page load).
- **route-abort technique:** the failure window is reproduced by
  `agent-browser network route <pattern> --abort` (the ref's entity API
  is `app.base44.com/api/apps/<id>/entities/*`); the reference's
  observable state = the SILENT ZERO-STATE (0.0% / $0.00 / ✓ NET ZERO,
  items views "0 items · $0.00" + their standard empty states, NO error
  surface); its mutation failure = a silent no-op (dialog stays open).
  LESSON: nested shell quoting mangles backtick template literals in
  `agent-browser eval` — always go through run-probe.sh (base64).

Session-33 additions (remediation-plan-v17 audit) — the calculator
line-item error tier (the parent-recalc response family), same
run-probe.sh pattern:

- `probe-v17-refdata.mjs` — the eleventh data-drift check on the
  reference (allocation/balance/status figures).
- `probe-v17-census.mjs` / `probe-v17-headdump.mjs` — the items-view
  census (the "N items · $X" header; the middle-dot in the header text
  defeats a naive `·` regex — dump the raw text instead).
- `verify-v17.sh` — the clone-side live verification script (login +
  route-aborted calculator open: empty-state parity + the error toast;
  run INSIDE one with-server.sh invocation — the nested-quoting lesson
  applies to ref extraction too, hence the script file).
- **calculator error-tier technique:** abort `**/api/line-items**`
  (clone) / `**/entities/**` (ref) AFTER the expenses view loads, then
  open the calculator — the reference renders its SILENT empty-state
  ($0.00 / 0 items / "No line items yet"); the clone (v17) renders the
  same surfaces PLUS the "Could not load the line items" toast. The
  reference's calculator total derives from the FETCHED line-items sum,
  not the parent figure. Its mutation failures (create/delete) are
  silent no-ops with no optimistic update.
- LESSON: a NESTED Radix dialog aria-hides the parent — page-level
  `getByRole`/computed-style reads scoped to the parent dialog return
  nothing while the sub-dialog is open (assert the sub-dialog, close
  it, then read the parent).

Session-35 additions (remediation-plan-v18 audit) — the net-worth
asset/liability error tier (the last unpinned dialog family), same
run-probe.sh / one-invocation patterns:

- **net-worth error-tier technique:** abort `**/api/assets/**` or
  `**/api/liabilities/**` (clone) / `**/entities/**` (ref) with the
  net-worth view live, then drive the card menu → Delete (the
  reference's Delete fires IMMEDIATELY — no confirmation; the clone's
  inline confirm bar is the superset #6 chrome) and the Edit dialog →
  Save. The reference is SILENT on both paths (card stays with zero
  feedback; dialog stays open with zero feedback — its dialogs are
  plain `fixed` divs, no `[role=dialog]`, so probe with the h2
  heading's visibility instead of a dialog role query). The clone (v18)
  keeps the surfaces and toasts: "Could not delete the asset" /
  "Could not delete the liability" (the caught confirm bars) and
  "Could not save the asset" / "Could not save the liability" (the
  dialog catches).
- **toast selector:** the clone's toasts are Radix, NOT sonner — select
  `.zb-toast` (a `[data-sonner-toast]` probe returns empty and misses
  live toasts; the v18 audit's first save-failure probe hit exactly
  that trap).
- **reference tab quirk:** its Assets/Liabilities Radix tabs need REAL
  pointer clicks (snapshot refs) — a programmatic `.click()` on the tab
  element leaves the selection unchanged (the same React-state class
  as the mobile-login fill quirk).
- LESSON (e2e): Next.js App Router's ROUTE ANNOUNCER renders a second
  EMPTY `role="alert"` (`__next-route-announcer__`) that mounts
  dynamically — never `waitForSelector("[role='alert']")` in specs;
  filter by the expected banner text (the register-spec flake, plan
  v18 G2).
- The reference's net worth holds 1 asset ("Savings Account" $25,000)
  and 0 liabilities — its Liabilities tab renders "No liabilities
  yet"; the clone's seed (3 assets, 2 liabilities) is a superset by
  design.

Session-37 additions (remediation-plan-v19 audit) — the VLM visual
sweep (the first full-page visual-AI comparison layer) + the tablet
breakpoint re-measurement, plus the standing drift/nav probes:

- `probe-drift-v19.mjs` / `probe-census-v19.mjs` — the standing
  data-drift pair (hero allocation/balance + the per-view "N items ·
  $X" census; the census's regex needs the literal "·" separator).
- `probe-r1-v19.mjs` — the R1 burger hit test (elementFromPoint at the
  center + the fixed top-0 container census with pointer-events).
- `probe-r3-v19.mjs` — the R3 root-route nav-highlight probe (rail link
  colors/weights + the nav landmark).
- `probe-tablet-v19.mjs` — the 767/768/1024 breakpoint probe (rail
  display/geometry, mobile header, main offset, scrollWidth). NOTE: the
  clone's `<main>` spans full width with the content wrapper carrying
  `md:ml-64` — compare the first HEADING's x (288 on both), not
  main.x, or the structural difference reads as drift.
- **VLM sweep technique:** capture full-page screenshot PAIRS (same
  viewport, same state) on both sites, then `z-ai vision -p "<layout
  prompt that IGNORES data differences>" -i ref.png -i clone.png`.
  The VLM is a SCREENING layer: this pass it found one real drift (the
  recurring-row) and hallucinated two (the "faded logo" — MD5-identical
  assets; the "taller button" — 294×44 both). ALWAYS DOM-verify every
  flag before filing it; pin specs assert MEASURED values.
- **pixel-diff decomposition:** the mechanical layer (PIL
  ImageChops.difference) reads 4–20% differing pixels even on
  identical pages — font anti-aliasing noise (two Chrome instances)
  + the reference's "Edit with Base44" platform badge. Decompose
  (row/col profiles + region crops + VLM on the CROPS) before
  concluding drift.
- **MD5 asset hashing:** `md5sum` the reference's served logo against
  the local `public/` copy settles asset-fidelity flags in one command
  (the v19 sweep's logo was byte-identical).
- The reference's dialogs need their X button to close (no Escape —
  superset fix #5); find it via `[...dlg.querySelectorAll('button')]`
  + `svg.lucide-x`.
- The reference's calculator shows "• Will update category total" ONLY
  when total ≠ item.amount (hidden on its $0.00 Miscellaneous item,
  shown on its $300 Investments item) — the clone's conditional
  matches; don't read an "extra line" on one side as drift without
  checking the other side's data state.

Session-39 additions (remediation-plan-v20 audit) — sessions
`ref22`/`clone22` (resized 1280×800 ↔ 390×844 per check), the :3200
parity server per `scripts/with-server.sh`, the v20 surfaces: the
MOBILE app views + the populated EDIT dialogs + the drill-down:

- `probe-census-v20.mjs` — the items-view census, ASCII-only (the
  separator built from `String.fromCharCode(0xb7)`). ROOT CAUSE of the
  v19 file's empty counts: the base64→`atob`→`eval` transport decodes
  C2 B7 as TWO Latin-1 chars, so the v19 regex's literal "·" never
  matched the DOM's U+00B7. Any probe traveling through base64 must
  avoid non-ASCII literals — build them from char codes.
- `probe-r2-v20.mjs` — the R2 sheet-trap test as ONE async eval: the
  synthetic pointer/mouse event sequence on the burger (the reference's
  toast containers block the programmatic hit — its own R1 bug), wait
  700ms for the slide-in, tap Income the same way, wait 1.2s, then read
  the sheet/overlay state (ref: `sheetStillOpen: true`; clone: closed +
  390 fit). The sheet + link geometry come free (288px sheet, Income at
  (20,185) 247×32 both).
- `probe-r4-route-v20.mjs` — the per-route scrollWidth probe (R4 at
  390×844): ref 395/395/390/390/390/464, clone 390 ×6.
- `probe-v20-mobile-header.mjs` — the items-view header probe that
  found G1: the Add button's width/position + the parent row's class
  (the missing base `items-start` = the 358px mobile stretch; the
  reference's 147/155/150 auto-widths).
- `probe-v20-header-gap.mjs` — the header→filter-card gap (ref 32 =
  `mb-8`, clone 24 = `mb-6` — at BOTH viewports; the G1 second axis).
- `probe-v20-nw-summary.mjs` — the networth mobile summary card (the
  VLM flags decomposer): ref 48px `text-5xl` figure + 2-col grid + the
  off-screen Add button (x=314 + 134 > 390) = the documented superset
  fix #4 (its own 464px overflow); clone 24px + 1-col = the fix; the
  tab tint IDENTICAL rgb(220,252,231) both (the VLM "pronounced green"
  hallucination refuted).
- `probe-v20-badge-rows.mjs` — the card badge-cluster mechanism probe
  (both sides `flex flex-wrap gap-2 mb-3` — the wrap flags are
  data-driven: the clone's seed carries 4 badges, the ref's data 2).
  NOTE: the ref's badges are DIVs, the clone's SPANs — match on the
  PARENT's computed styles, not the tag.
- `probe-v20-drilldown.mjs` — the breakdown drill-down expander (the
  section button by its "Total Income" prefix, then the category by its
  "Salary" prefix).
- `vlm-compare-v20.sh` — the reusable VLM pair-comparison wrapper
  (layout-focused prompt, data differences excluded by instruction,
  verdict extracted from the JSON output). The v20 sweep's flags:
  5 mobile views (dashboard IDENTICAL; 3 items views = G1; networth =
  superset #4 + 1 refuted hallucination), the populated edit dialog
  (the icons = G2; the radio/switch "differences" = data states —
  different items being edited; the X-close "bordered" = the same
  hallucination twice, DOM-identical), the drill-down (clean).

Session-41 additions (remediation-plan-v21 audit) — sessions
`ref23`/`clone23` (desktop 1280×800 + 390×844), the :3200 parity server
per `scripts/with-server.sh`, the v21 surfaces:

- `vlm-compare-v21.sh` — the VLM wrapper, v21 edition (same
  layout-focused prompt; `/tmp/vlm21/` pairs). The v21 sweep's flags:
  the calculator POPULATED pair (the row-actions visibility = G2, a
  real reference chrome change; the "Will update category total" line =
  data-driven — the reference's Rent parent equals its line-item sum),
  the mobile SHEET-OPEN pair (both flags = the documented superset #3
  root-route highlight + the avatar letter), the net-worth populated
  EDIT-ASSET pair (the X-close claim = the same thrice-DOM-refuted
  misread), and the verify-email state pair (IDENTICAL — the clone's
  dev-code box excluded by instruction as the documented superset).
- `probe-v21-verify-flow.mjs` — completes the clone's verify-email flow
  through the DOM (reads the dev code from the honest box, sets the six
  inputs via the native value setter + input events, clicks Verify) —
  the live counterpart of the e2e spec. The live-audit lesson it
  encoded: a malformed throwaway email (`a@b@c.com`) fails native
  `type=email` validation SILENTLY (no submit, no error, no request) —
  check `form.checkValidity()` before suspecting React state.

Session-43 additions (remediation-plan-v22 audit) — sessions
`ref24`/`clone24` (desktop 1280×800 + 390×844), the :3200 parity server
per `scripts/with-server.sh`, the v22 surfaces:

- `vlm-compare-v21.sh` (reused — same wrapper, `/tmp/vlm21/` pairs): the
  v22 sweep's pairs — the MOBILE calculator (the first pair's row-action
  "missing" flag was a SCREENSHOT POINTER ARTIFACT: the reference's shot
  caught its row under the mouse parked from an earlier real click
  [opacity 1] while the clone's pointer sat at its Save button
  [opacity 0]; re-taken with the pointer parked away on both sides: only
  the X-close claim remained, DOM-refuted for the FOURTH time) and the
  line-item EDIT SUB-DIALOG pair (only the same X-close misread —
  DOM-refuted; the real finding, the panel cap + form gaps, came from the
  DOM decomposition below, not the VLM).
- `probe-v22-row-actions.mjs` — measures the calculator row-action
  container's computed opacity/classes/geometry at rest and under a
  parked mouse (the triage probe that separated the hover state from the
  artifact; verified identical classes + 32px/16px/colors both sites).
- `probe-v22-li-edit.mjs` — opens the line-item Edit sub-dialog through
  the DOM and dumps its panel + inputs + buttons (the first measurement
  of the nested dialog's populated state — found the 90vh-vs-85vh cap).
- `probe-v22-sub-decomp.mjs` — decomposes the sub-dialog's vertical
  structure (header / form / form children with classes + heights) —
  isolated the `space-y-6` vs the reference's `space-y-5` form gap.
- `probe-v22-kb-sweep.mjs` + `probe-v22-focus-now.mjs` — the app-view
  keyboard sweep: real Tab presses (agent-browser `press Tab`) with a
  per-press focus read (tag/label/position/ring/outline). The synthetic
  keydown variant does NOT move focus — only real key presses do.
- `probe-v22-xclose.mjs` — the X-close chrome dump (the 4th refutation
  probe: identical 29×36 mobile / 36×36 desktop, 0px border,
  transparent bg, 16px svg `#0a0a0a`, radius 6 both sites).

Session-45 additions (remediation-plan-v23 audit) — the shared parity
browser (NOTE: `agent-browser session new ref25/clone25` prints `default`
and BOTH "sessions" resolve to ONE browser tab — the active site is
whatever the last `open` pointed at; the discipline is ALWAYS
`open <target-url>` + settle before every eval. A drift probe that
skipped the open read the CLONE's dashboard left over from the previous
navigation and produced a false "data drift" alarm this pass), the :3200
parity server per `scripts/with-server.sh`, the v23 surfaces:

- `vlm-compare-v23.sh` — the v23 VLM pair wrapper (`/tmp/vlm23/`): the
  budget-item dialog's MOBILE pair (the session-44 suggestion — only the
  classification-radio "thicker border" claim + the platform badge;
  DOM-refuted: 16×16 / 1px #171717 / 9999px radius both) and the
  verify-email state's MOBILE pair (only the dev-code box — the
  documented superset).
- `kb-sheet-sweep-v23.sh` — the mobile sheet's KEYBOARD sweep (the
  session-44 suggestion 2): opens the sheet (synthetic burger click),
  then REAL Tab presses with per-press focus reads, then Escape. Found:
  initial focus → a sheet container, the five links cycle at identical
  positions and WRAP (a focus loop on both sites), the visible ring is
  the blue #3b82f6 2px layer on both, Escape closes both. Pinned by the
  mobile-navigation spec's new v23 G1 test.
- `probe-v23-sheet-focus.mjs` + `probe-v23-focus-read.mjs` — the
  sheet-open + focused-element full-shadow reads (the ring pair: the
  reference's white 0-spread lead + blue layer vs the clone's three
  transparent leads + the same blue layer — visible chrome identical).
- `probe-v23-verify-mobile.mjs` — the verify-email state's chrome at
  390×844 (first mobile measurement: circle 56 / icon 28 / six 40×44
  inputs gap 6 / button 294×44 #0f172a / h2 20px 700). Pinned by the
  verify-email spec's new v23 G2 mobile describe. Its lessons: park the
  pointer BEFORE the eval (the probe itself read the swapped-in button's
  hover #1e293b until parked — the v22 G1 lesson now applies to PROBES
  too), and re-measure after a state swap (one transient first read of
  the reference's button height [40] that two re-measures + the h-11
  class refute).
- `probe-v23-drift-census.mjs` — the per-view data census (income/
  expenses/savings innerText dumps) backing the 17th consecutive clean
  drift check.
- `probe-v23-subdialog-family.mjs` — one-shot re-verification of the
  line-item sub-dialog's third-family geometry at the CURRENT viewport
  (the v22 G2 fix re-verified at both: 672×680/85vh/20px desktop,
  358×717/85vh/20px mobile — identical to the reference).

Session-47 additions (remediation-plan-v24 audit) — the shared parity
browser (the open+settle discipline; this session's OWN false-read: two
"reference" class dumps read the CLONE's forgot page left in the tab by
an intervening with-server.sh invocation — lesson 42: read ALL states
of a multi-state surface in ONE eval right after the fresh open, and
arbitrate disagreements with the CLASS ATTRIBUTE), the :3200 parity
server per `scripts/with-server.sh`, the v24 surfaces:

- `probe-v24-signup-rows.mjs` — the sign-up form's per-row
  decomposition (label y/h, input y/h, label→input gap, row→row gap,
  submit gap) — the first measurement that isolated the 4px vs 10px
  label gap and the 40 vs 44 input heights at mobile.
- `probe-v24-auth-census.mjs` — the reliable multi-state form: ONE eval
  that walks signin → signup → back → forgot right after a fresh open,
  reading each state's input/submit height + font + height/fs class
  list + label gap + rel-wrapper margin-top. This census produced the
  three-family table (v24 G1) and re-verified the fix live (40/40/44
  mobile, gap 10, relMt 6 — identical to the reference).
- `kb-sheet-arrows-v24.sh` — the mobile sheet's ARROW-key sweep (the
  session-46 suggestion): opens the sheet, presses each arrow key with
  per-press focus/scroll/sheet-state reads. Verdict: arrows are INERT
  on both sites (no roving focus, no scroll, sheet stays open).
- The VLM pair wrapper reused at `/tmp/vlm24/` (ref/clone
  signup-mobile screenshots): the pair returned IDENTICAL while the DOM
  found two real deltas — the 6th consecutive form-scale VLM blind
  spot; sub-6px differences are below its resolution.

Session-49 additions (remediation-plan-v25 audit) — the keyboard-focus-ring
sweep (the session-48 log's suggestion 2) + the sm-band auth census (its
suggestion 1), the :3200 parity server per `scripts/with-server.sh`:

- `kb-auth-ring-v25.sh` — the auth submit's focus ring via REAL Tab
  presses (CDP key events move focus): opens /login fresh, parks the
  pointer, Tabs until the submit button is focused, reads its FULL
  computed box-shadow + class list (plus the first input's ring for
  context). This produced the G1 finding (the reference's
  `ring-ring` = zinc-950 rgb(9,9,11) vs the clone's #94a3b8) and
  re-verified the fix live (identical composition). Its LESSON:
  programmatic `focus()` inside agent-browser evals sets
  document.activeElement but never matches `:focus`/`:focus-visible`
  on either site (Playwright's page.evaluate DOES) — REAL Tab presses
  are the only reliable focus-chrome probe.
- `kb-login-walk-v25.sh` + `probe-v25-focus-stop.mjs` — the login
  page's FULL focus walk: one Tab press per stop, a focus-chrome read
  after each (tag/label/boxShadow/outline/color/bg). The reference's
  table: Google → browser-default outline; inputs → the v13 #94a3b8
  family; submit → G1's #09090b; the two swap buttons →
  browser-default outlines; the 7th stop is the Base44 PLATFORM edit
  badge (not app chrome, correctly absent from the clone).
- `vlm-compare-v25.sh` — the v25 VLM pair wrapper (`/tmp/vlm25/`):
  the login-page pair returned IDENTICAL "none" (correct on the
  background — the body's tint is covered by the identical
  full-viewport gradient; blind on the rings only because
  keyboard-focus chrome is unphotographable in rest-state shots).
- The v24 census probe was REUSED for the sm-band sweep (672×800 —
  the sign-up font's 16px middle step): exact match on every axis on
  both sites (signin 48/16 + 48 submit, signup 44/16 + 44, forgot
  44/16 + 44, widths 368, gaps 10, relMt 6) — the v24 responsive
  ladder verified at the third viewport.
- Display-pipeline lesson (44): the tool-result text pipeline strips
  the literal two-character sequence left-bracket+m from RENDERED
  text — a `[mode, setMode]` destructure line DISPLAYS as if
  corrupted. Verify suspected source corruption with charCodeAt
  before "fixing" it (this session's false alarm: tsc + build were
  green the whole time).

Session-51 additions (remediation-plan-v26 audit) — the dialog-button
mouse-focus pair + the verify-email state's inputs audit (the
session-51 log's two suggestions), the :3200 parity server per
`scripts/with-server.sh`:

- `probe-v26-verify-inputs.mjs` — the verify-email state's six code
  inputs as an aria/landmark/focus surface (first sweep): attributes
  (autocomplete distribution, inputmode, aria-label, pattern,
  maxlength), geometry, and the state's landmark counts. This
  produced the G2 finding (the reference runs `one-time-code` on the
  FIRST box only and `off` on the rest — the standard OTP convention —
  while the clone had it on all six) and documented the two KEPT
  supersets (the clone's `aria-label="Digit N"` boxes; the reference's
  inputs are unnamed — and the clone's arrow-key navigation; the
  reference's arrows are inert, measured live with REAL Arrow key
  presses on both sites).
- The dialog-button mouse-focus pair needed NO new probe: the class
  ATTRIBUTE read settled it (lesson 42's tie-breaker discipline) —
  both sites' dialog Cancel/Save carry the byte-identical
  `focus-visible:ring-1 ring-ring` family, so a mouse click shows no
  ring on either site; the REAL-Tab re-verification (the v23 sheet
  pattern) confirmed the identical visible ring layers. Behavioral
  probe lesson: clicking Save on an EMPTY form moves focus to the
  first invalid input via native validation on both sites — the
  empty-submit path cannot hold focus on the button.
- The antialiased A/B pixel test (G1): the clone's login shot with
  `document.body.classList.remove("antialiased")` applied via eval —
  byte-identical diff counts against the reference pair at every
  threshold (Linux Chromium ignores font-smoothing) — proving the
  class removal is a computed-style-only fix on this platform.
- Register-gate observation (limits future reference probes, not a
  gap): the reference's `/api/auth/register` started answering
  `400 "Security verification is required"` after ~2 synthetic
  registrations this session — a platform anti-automation gate.

Session-53 additions (remediation-plan-v27 audit) — the suggested-surface
sweep (reduced-motion, print/overscroll, scrollbars) ran as inline evals
(no dedicated files needed — each was a one-shot CSSOM + computed-style
walk); the finding surfaces got persisted probes:

- `probe-v27-x-tabwalk.mjs` — the dialog X-close button's REAL-Tab focus
  walk (the G1 evidence): dispatches keydown Tab events inside ONE eval
  until the 36px X (svg + .sr-only) is focused, then reads its FULL
  focused box-shadow + outline. Needed because the clone's Radix dialog
  TRAPS focus while the reference's plain-div dialogs do not — the two
  sites' Tab-walk-to-X stop counts differ (the reference reached the X
  at walk stop 18; the clone's trap lands it on the first dispatched
  Tab). Run with the dialog open (the Add Income button clicked first).
- `probe-v27-x-hover.mjs` — the X's HOVER family read (bg + currentColor
  + the hover: class list) with the dialog open; produced the second G1
  axis (the reference runs `hover:bg-accent
  hover:text-accent-foreground`, the clone only `hover:bg-accent`).
- `probe-v27-x-focus-read.mjs` — the active element's full focused
  shadow (a generic stop-sampler for the Tab walk).
- `probe-v27-filter-triggers.mjs` — the items-view filter Select
  triggers ("All Categories"/"All Frequencies") class + geometry read
  (byte-identical on both sites — the `focus:ring-1 focus:ring-ring`
  plain-focus family).
- The reduced-motion sheet measurement: `agent-browser set media light
  reduced-motion` + a synthetic-click sheet open sampled at 33ms
  intervals (both sites animate the full 500ms slide-in; the spinner
  probed via an injected `animate-spin` element — `animationName: spin`,
  `1s`, `running`, transform rotating on both).
- Probe-infrastructure note: the `with-server.sh` one-invocation pattern
  kills the server after each command, so a page `open`ed in one
  invocation boots against a dying server — the clone correctly renders
  its v16 stay-in-app zero-state (data-dependent probes must run inside
  ONE invocation; focus-ring probes are data-independent).

Session-55 additions (remediation-plan-v28 audit) — the details-sheet
discovery + the badge-hover discipline:

- `probe-v28-btn-census.mjs` — the ONE-PASS button-variant census (every
  `<button>` on the items views with full class strings; found G2 and the
  badge-hover lead).
- `probe-v28-card-dump.mjs` / `probe-v28-badge-hover.mjs` — the expense
  card's interactive structure + all badge classes + the synthetic-hover
  probe (NOTE: synthetic mouseenter never engages `:hover` — the REAL
  CDP `agent-browser mouse move` to the badge center is the arbiter).
- `probe-v28-details-*.mjs` — the Budget Item Details sheet contract:
  `-leaves.mjs` (fact-row/classification/summary styles), `-expense.mjs` /
  `-savings.mjs` (type variants), `-clsvar.mjs` (want/savings
  classification variants), `-overlay.mjs` (overlay + outside-click),
  `-esc.mjs` (Escape + mobile geometry).
- `probe-v28-toast.mjs` / `probe-v28-toast2.mjs` / `probe-v28-toast3.mjs`
  — the reference's toast-render timing check (viewport heights at
  200ms/900ms/3.4s after a save: [32,32] — the reference renders NO
  toasts; the number-input finder must match `input[type=number]`, its
  value stays EMPTY, "0.00" is the placeholder).
- `probe-v28-focus-stop.mjs` — the real-Tab walk stop reader (full
  box-shadow + outline per stop).
- `clone-sweep-v28.sh` / `clone-tabwalk-v28.sh` / `clone-tabwalk-full-v28.sh`
  / `clone-edit-focus-v28.sh` / `clone-mobile-nav-v28.sh` /
  `clone-cardclick-v28.sh` / `clone-verify-v28.sh` — the clone-side
  login-in-one-invocation patterns: the census, the real-Tab walks to the
  Edit/Calculate buttons, the R1–R4 mobile-nav standing check, the dead
  card-click verification, and the post-fix live re-verification.

Session-57 additions (remediation-plan-v29 audit) — the net-worth census
+ the details-sheet keyboard semantics + the VLM-flag arbitration
discipline:

- `probe-v29-refdata.mjs` — the standing five-metric reference census
  (allocation/Balance/per-view totals; the 23rd drift check).
- `clone-nw-census-v29.sh` / `clone-nwmenu-v29.sh` — the clone-side
  net-worth census (tab triggers, tablist, the asset card + label) and
  the asset-card dropdown menu class diff (panel/items/computed — all
  byte-identical; the trigger snapshot pattern: the aria-labeled
  "Actions for X" buttons).
- `clone-sweep-v29.sh` / `clone-sweep2-v29.sh` / `clone-bdhover-v29.sh`
  — the clone-side details-sheet keyboard-semantics check (initial
  focus → the X, the Radix trap, Escape close — the superset), the
  asset-label hover probe, and the breakdown nested-row hover (inert on
  BOTH sites — the inline `background-color` style overrides the
  `hover:bg-gray-100` class everywhere).
- `clone-xchrome-v29.sh` — the details X's computed chrome in the OPEN
  state (Chrome applies `:focus-visible` to Radix's programmatic focus —
  the pinned 1px ring RENDERS on open; the reference's BODY-focus leaves
  its X ringless — the superset's visible signature; find the X by its
  sr-only "Close" textContent, there is no aria-label).
- `clone-details-shot-v29.sh` / `vlm-compare-v29.sh` — the details-sheet
  VLM pair (capture + verdict; the two DIFFERENT flags were both
  DOM-explained: the X ring = the Radix superset, the fact-row count =
  data).
- `clone-gridtest-v29.sh` — the live DOM experiment that flipped the
  clone's mobile summary grid to the reference's 2-col and measured the
  seeded values' glyph overflow (152/169px vs the 107px box — the v4
  stacking superset re-verified; scrollWidth stayed 390).
- `clone-trendicon-v29.sh` — the trend-icon inset arbitration (48px on
  both sites — the VLM's "overlapping the border" was a false positive;
  measure with the gradient-card finder, not a text-wrapper finder).
- `clone-verify-v29.sh` / `clone-mobgrid-v29.sh` — the post-fix live
  re-verification (rest rgb + the REAL CDP hover tint) and the mobile
  summary-grid measurement.
- LESSONS: the reference's tab TRIGGERS do not respond to synthetic
  `element.click()` (real ref clicks only — the v28 real-click lesson
  now extends to tabs); VLM glyph/icon claims at 16–24px are unreliable
  (all three mobile flags were false positives or data-driven — always
  arbitrate with computed geometry); the reference's /networth 464px
  overflow culprit is its SIDEBAR WRAPPER (hide rootChild0 → 390), not
  the summary grid; and the details-sheet keyboard family is the
  reference's weakest surface (no focus, no trap, no role, no Escape —
  the clone's Radix behavior is the documented superset).

Session-31 additions (remediation-plan-v30 audit — the session-59 brief):

- `clone-sweep-v30.sh` — the clone-side standing sweep (login + mobile-nav
  R1-R4, 24th) plus the guideline rows' rest/hover and the quick-action
  buttons' rest/hover (REAL CDP hover; the v4 `scale: 1.1` property reads
  `transform: none` — read `.scale` + the rendered rect; the hover shadow's
  2 extra TRANSPARENT v4 lead layers precede the byte-identical visible
  pair).
- `ref-guidelines-v30.mjs` — the reference's guideline-row finder (the rows
  are `p-4 rounded-lg` divs with inline tints BELOW the donut's "Needs vs
  Wants vs Savings" card — found by description text, not by a "guideline"
  heading, which does not exist).
- `probe-head-v30.mjs` — the full head-metadata census (SEO deep check:
  description/OG/Twitter/apple-title byte-identical; the reference's
  /manifest.json endpoint serves EMPTY while the clone's webmanifest serves
  the full document — a superset).
- `vlm-compare-v30.sh` — the dashboard (quick-actions + guidelines region)
  and mobile details-sheet VLM pairs (both IDENTICAL, "none" differences).
- LESSONS: bash mangles template literals with `$`-bearing selectors passed
  inline — persist regex/`$` probes as files (the run-probe.sh base64
  discipline); a static `tabIndex=-1` on BOTH tab triggers with the
  tablist container at `tabIndex=0` is the correct Radix RovingFocusGroup
  fresh state (not a broken roving pattern — the reference renders the
  identical attribute set); and the arrow-key roving contract (focus move +
  automatic activation + the roving tabindex update) is now pinned by the
  v30 e2e tests.

Session-33 additions (remediation-plan-v31 audit — the session-61 brief):

- `probe-drift-v31.mjs` / `probe-r1-v31.mjs` / `probe-r2-ref-v31.mjs` /
  `probe-r2-trapped-v31.mjs` / `probe-r2-clone-v31.mjs` / `probe-r3-v31.mjs`
  — the 25th standing sweep (data census, the burger hit-test, the
  reference's sheet trap + the clone's close-on-nav with the Radix
  `[role=dialog]` detector, the root-URL active-nav census).
- `probe-select-open-v31.mjs` / `probe-select-arrows-v31.mjs` — the filter
  selects' open-state arrow semantics (suggestion #2 — NO finding: both
  sites are Radix listbox/option roving with `data-highlighted`, no wrap at
  the ends, identical).
- `probe-dialog-structure-v31.mjs` / `probe-dialog-taborder-v31.mjs` /
  `probe-tiles-v31.mjs` / `probe-tile-arrows-v31.mjs` /
  `probe-realtab-v31.mjs` — the form dialogs' full Tab order (suggestion
  #3): the strict focusable census (tabindex property; the reference's
  1×1 native select shadows are NOT stops), the classification tile
  structure + arrow behavior, and the REAL Tab landing (the entry-focus
  pass-through). Found G2 (the checked radio's fresh tabindex).
- `probe-donut-census-v31.mjs` / `probe-donut-tip-v31.mjs` /
  `probe-donut-kb-v31.mjs` / `probe-donut-rings-v31.mjs` — the donut's
  keyboard semantics (suggestion #1): the surface/layer/sector tabindex
  census, the tooltip's attribute set, the full arrow-key walk, and the
  focus-ring rendering. Found G1 (the recharts-3 a11y defaults + the
  missing 2.15 roving).
- `probe-x-chrome-v31.mjs` — the VLM dialog-flag arbitration (the X's
  computed chrome at rest — byte-identical; the open-state ring = the
  documented v29 superset).
- `vlm-compare-v31.sh` — the dashboard + add-dialog VLM pairs (all flags
  DOM-explained: the Dashboard-active rail = superset #3, the allocation
  bar + avatar = seeded data, the X box = the Radix focus superset).
- LESSONS: a 2.5s post-navigation settle can read a still-loading route as
  non-overflowing (the /networth 390-vs-464 artifact — re-measure with a
  6s settle before declaring drift); the dialog X finder must scope to the
  topmost fixed overlay (a page-wide 36×36+svg filter matches the card
  action buttons underneath); SVG elements without a `tabindex` attribute
  read `.tabIndex === -1` — distinguish "attribute absent" from
  "attribute -1" before claiming parity; a REAL Tab into a Radix
  RovingFocusGroup lands on the CHECKED ITEM (the container's entry-focus
  forwards immediately — activeElement never reads the container); and
  recharts' pie-layer roving is version-specific (2.15's
  `attachKeyboardHandlers` ArrowLeft=++wrap / ArrowRight=--wrap / Escape
  blur+reset was REMOVED in 3.x — the clone replicates it in
  `usePieKeyboardParity`, dashboard-view.tsx).

Session-35 additions (remediation-plan-v32 audit — the session-63 brief):

- `probe-nw-menu-v32.mjs` + `kb-nw-menu-v32.sh` — the net-worth dropdown
  menus' keyboard contract (suggestion #1 — NO finding): the census +
  the REAL-key walk (click-open container focus / Enter-open first item /
  ArrowDown-Up roving with data-highlighted / CLAMPED at the ends — no
  wrap / Home-End work / NO typeahead / Escape closes + returns focus to
  the trigger). Byte-identical on both sites; the clone's aria-labeled
  "Actions for X" triggers are the documented v29 naming superset.
- `probe-calc-row-v32.mjs` + `kb-calc-rowactions-v32.sh` — the
  calculator line-item row actions' Tab order (suggestion #2 — G1): the
  strict focusable census (4 stops on both sites: X 36 / Add Item 110 /
  Edit 32 / Delete 32, the row actions focusable inside their opacity-0
  container — the reveal is hover-ONLY, never focus) + the REAL-Tab walk
  with the SETTLED focused-chrome read (the G1 evidence: the reference's
  buttons carry focus-visible:outline-none ring-1 ring-ring; the clone's
  raw buttons rendered the browser-default auto outline — fixed in
  calculator-dialog.tsx + the globals.css zb-row-action pin).
- `probe-bd-rows-v32.mjs` — the breakdown accordion's arrow semantics
  (suggestion #3 — NO functional finding): plain buttons on both sites,
  arrows/Home/End inert, Enter expands, Escape does NOT collapse on
  either; the clone's aria-expanded is the kept + pinned S1 superset.
- `probe-r2-ref-v32.mjs` — the ROBUST R2 sheet detector (structure +
  body-lock + overlay census — the v31 white-bg matcher missed the
  reference's sheet this session; prefer structure over background-color
  matching).
- `vlm-compare-v32.sh` — the dashboard + calculator VLM pairs (both
  DIFFERENT flags DOM-explained: the Dashboard-active rail = superset
  #3; the X's open-state box = the v29 Radix focus superset).
- LESSONS: (a) Tailwind v4's `outline-none` utility emits
  `outline-style: none` ONLY — v3's `outline: 2px solid transparent;
  outline-offset: 2px` form must be pinned in globals.css (the
  zb-row-action pattern, the same trap family as the shadow-scale shift
  and the hover media-gate); (b) `transition-colors`' v4 property list
  INCLUDES outline-color — an immediate post-focus read catches the
  transparent settle mid-flight in oklab-interpolated form (settle
  ≥350ms before reading focus chrome; the v23 G1 lesson generalized);
  (c) a form fill finder must anchor on LABEL text or DOM order, never
  `placeholder*=name` (the reference's Provider placeholder "Insurance
  Company Name" swallowed an Item Name fill); (d) a calculator
  add/delete probe cycle recalculates the parent amount to the line-item
  sum — the dev custom.db needs the amount restored afterward (the
  seed's natural-key upsert does NOT restore it); (e) the reference's
  calculator row delete is IMMEDIATE (no confirm) — the clone's inline
  confirm is the documented "unconfirmed deletes fixed" superset.

Session-37 additions (remediation-plan-v33 audit — the session-67 brief):

- `probe-data-v33.mjs` — the 27th data-drift census (read-only; the
  standing fields: allocation 30.5%, Balance $3475.00, income
  $5000.00/1, savings $1000.00/1, expenses $525.00/4).
- `probe-r4-v33.mjs` — the per-route mobile overflow walk (superseded
  by the CLI loop — kept for the route list; the 6s settle discipline
  lives in the shell loop).
- `clone-mobile-nav-v33.sh` — the clone-side standing R1–R4 (27th):
  the burger hit DIRECT on the svg (390 fit), the sheet opens
  (structure detector) and CLOSES after nav (superset fix #2), the
  nav landmark present, all six routes fit 390.
- `probe-lisub-census-v33.mjs` + `kb-lisub-v33.sh` — the line-item
  sub-dialog's focusable census + REAL-Tab walk (suggestion #1 — NO
  finding): 13 stops on both sites in the same order (X 36 / name /
  amount / frequency / provider / policy / 2 native dates / payment /
  status / notes 90px / cancel / save), the walk byte-identical
  INCLUDING the native date segments (each `<input type="date">` is a
  FOUR-STOP walk — 8 consecutive date stops on both sites); the
  reference keeps focus on its trigger on mouse-open and EXITS after
  the last stop (the clone's Radix auto-focus-X + trap = the
  documented supersets).
- `clone-lisub-v33.sh` — the clone-side twin of the sub-dialog walk
  (same census + 18 REAL Tabs — the identical sequence, `inDlg:false`
  is a probe artifact: `querySelector('[role=dialog]')` finds the
  CALCULATOR dialog beneath, not the sub-dialog).
- `clone-seltrigger-v33.sh` + `clone-seltrigger-deep-v33.sh` — the
  select triggers' focus chrome (NO finding — the probe LESSON): the
  first 85-char box-shadow read looked like "no ring"; the deep probe
  reads `--tw-ring-color: #0a0a0a` + `--tw-ring-shadow: 0 0 0
  calc(1px + 0px) #0a0a0a` and the FULL composed shadow — the 1px
  ring IS present as the FOURTH layer behind v4's three transparent
  placeholders.
- `probe-toast-ref-v33.mjs` — the reference's toast-viewport census:
  two plain `fixed top-0 z-[100]` divs, NO role/aria-live/aria-label,
  `pointer-events: auto` (the standing R1 burger-blocker root cause).
- `clone-toast-v33.sh` — the clone's live toast semantics (the save
  toast via the calculator's add flow): the li (tabindex 0, no
  role/live BY DESIGN) + Radix's hidden ANNOUNCER portal —
  `<span role="status" aria-live="assertive">Notification Line item
  added</span>` measured inside its 1-second mount window (the
  +1.2s read misses it — read within ~0.5s).
- `clone-perf-v33.sh` — the bundle/page-weight census (suggestion #4):
  the clone's dashboard = 12 chunks 1,104KB raw / 338KB gz + 147KB
  CSS, nav 66ms / DCL 26ms; the reference = one 1,060KB raw / 317KB
  gz bundle + 68KB CSS + a 214KB dev-only badge.js.
- `clone-vlmshots-v33.sh` + `vlm-compare-v33.sh` — the VLM pairs (the
  dashboard + the verify-email state): both flags DOM-explained
  (superset #3, the dev-code hint box). **Re-assert `set viewport`
  before pairing** — the first dashboard pair compared a desktop
  reference against a mobile clone shot (the stale default-session
  viewport) and produced a phantom full-page drift verdict.
- `clone-reverify-v33.sh` — the post-fix live re-verification: the
  register lands with Digit 1 focused; the REAL-Tab-focused Digit 2
  renders the 2px zinc ring + the untinted border (byte-matching the
  reference modulo v4's invisible lead layers); the R1/R4 spot check.
- LESSONS: (a) v4's ring composition puts the visible ring in the
  FOURTH box-shadow layer behind three zero-width transparent
  placeholders — a truncated read fabricates a missing-ring finding;
  read the FULL string + the `--tw-ring-*` properties; (b) persistent
  agent-browser sessions keep their LAST viewport — re-assert `set
  viewport` before any screenshot pairing; (c) the clone's Radix
  DialogContent is NOT inside a `div.fixed` (the overlay and the
  content are portal SIBLINGS) — anchor probes with
  `closest('[data-state=open],[role=dialog]')`, not
  `closest('div.fixed')` (two silent probe failures this session);
  (d) the reference's plain-div dialogs IGNORE Escape — verify the
  DOM state, never assume closed; (e) the reference's register form
  is a STATE on `/login` (the `/register` route 404s — enter via the
  "Need an account? Sign up" link); (f) the empty-required-field save
  is blocked by NATIVE form validation (no submit event, no toast —
  drive the toast probes through a real fill); (g) the calculator
  add/delete probe cycle under the DEMO user needs the line-item
  cleanup + the parent restore (the probe users cascade-delete but
  the demo user's fixtures do not).

Session-67 additions (remediation-plan-v34 audit — the session-69
suggested surfaces: the forgot-password focus walk, the calculator
frequency Select's listbox keyboard contract, the API error-tier audit):

- `probe-drift-v34.mjs` / `probe-seo-v34.mjs` — the standing data-drift
  census + the head-metadata census (28th consecutive — clean).
- `probe-r1-v34.mjs` — the burger hit test (fixed: the reference's
  burger has NO aria-label — its accessible name comes from the sr-only
  "Toggle Sidebar" span; find it by textContent or the finder silently
  skips the click).
- `probe-r2-open-v34.mjs` + `probe-r2-nav-v34.mjs` +
  `probe-sheet-toggle-v34.mjs` — the sheet open/nav/trap check (the
  structure detector: fixed panel + nav links + body lock) and the
  close via the burger TOGGLE (the sheet has no X on the reference —
  the snapshot's dialog carries no close button).
- `probe-r3-v34.mjs` + `probe-r3-active-v34.mjs` — the nav landmark +
  active-state check (the clone's active rail is TEXT-COLOR based —
  a bg-color-based active filter false-negatives; check computed
  color/weight per link).
- `probe-r4a-v34.mjs` + `probe-r4b-v34.mjs` — the per-route overflow
  census split in halves (the 6-route × 6s single eval exceeds the
  agent-browser CDP timeout — 3 routes per eval is the ceiling).
- `probe-forgot-census-v34.mjs` + `probe-focus-read-v34.mjs` +
  `probe-forgot-submit-v34.mjs` — the forgot-password state's census
  (3 stops: Back → Email → Send reset link; 368×44 controls; no
  auto-focus), the REAL-Tab focus-chrome reader, and the post-submit
  state (the reference's "Check your email" vs the clone's honest
  no-mail variant — the v12 G4 superset).
- `probe-calc-open-v34.mjs` + `probe-lisub-open-v34.mjs` — the
  REFERENCE-side calculator + sub-dialog openers (the reference's
  dialogs are plain `fixed z-50/z-[60]` divs — the fixed-class
  detector works THERE but NOT on the clone; see the Radix-aware
  counterpart below).
- `probe-freq-census-v34.mjs` + `probe-freq-state-v34.mjs` +
  `probe-freq-reopen-v34.mjs` — the frequency listbox's structure
  census (role=combobox + aria-controls + 6 same-order options), the
  roving-state reader (data-highlighted index + activeElement), and
  the re-open state (post-Escape: the selected option re-focuses).
- `probe-clone-lisub-freq-v34.mjs` — the CLONE-side Radix-aware chain
  (calculator → sub-dialog → listbox) — anchored via
  `[role=dialog]`/`h2` textContent, NOT the fixed-class detector
  (the v33 lesson (c): the clone's Radix DialogContent is NOT inside
  a `div.fixed`).
- `probe-freq-fresh-v34.mjs` — the self-contained fresh-open visual
  census (single-click path — clicking an ALREADY-OPEN trigger
  toggles it CLOSED; a two-probe sequence double-clicks and reads a
  collapsing popup — a measurement artifact this session hit).
- `probe-freq-focuscheck-v34.mjs` + `probe-freq-wherefocus-v34.mjs` —
  THE L1 EVIDENCE: the `:focus`-computed read gated on
  `document.hasFocus()`. See LESSONS (a) below — the unfocused
  headless window fabricates a missing-highlight finding.
- `clone-mobile-nav-v34.sh` + `clone-surfaces-v34.sh` — the clone-side
  standing checks (R1–R4 + drift at 390×844) and the surfaces (the
  forgot walk + the listbox) against the :3200 parity server inside
  ONE `with-server.sh` invocation.
- `vlm-compare-v34.sh` — the VLM pairs (the dashboard + the
  forgot state): dashboard one flag DOM-explained (superset #3);
  forgot VERDICT IDENTICAL, zero flags.
- LESSONS: (a) **THE UNFOCUSED-HEADLESS-WINDOW `:focus` ARTIFACT** —
  an eval that DOM-clicks a Select trigger open reads
  `document.activeElement` = the selected option while
  `element.matches(':focus')` is FALSE and
  `document.querySelector(':focus')` returns NOTHING: the headless
  page's OS-level window focus was lost (no real key press since the
  last navigation), so the `:focus` pseudo-class matches nothing
  while `activeElement` retains its value. The first fresh-open
  comparison fabricated "the clone's selected option renders NO
  highlight" (bg transparent vs the reference's #f5f5f5) — the
  reference read had run after REAL key presses (page focused), the
  clone read after JS clicks alone. **Gate every `:focus`-computed
  read on `document.hasFocus()` (a real `press Shift` re-focuses the
  page); Playwright is immune (its pages hold real focus).**
  (b) `[tabindex=-1]` is an INVALID CSS selector unquoted (an
  identifier cannot start with `-` followed by a digit) —
  `querySelectorAll('[tabindex]:not([tabindex=-1])')` THROWS; quote
  it: `[tabindex="-1"]`. (c) The display pipeline eats `[h` too (in
  `a[href]` → `aref]` inside a displayed browser error message — the
  lesson-44 `[m` family extension); arbitrate with char codes or
  probe files, never by eye — INCLUDING python `repr()` outputs of file
  reads (a repr output displayed mangled mid-session and fabricated a
  "the command transport mangled the file" conclusion; byte-level reads
  proved every file intact — command transport and file contents are
  NEVER touched, only the DISPLAYED result text). (d) A REAL Tab into a `focus-visible:`
  ring still needs the source focused first (programmatic focus +
  real Tab is the working pattern; programmatic focus alone never
  engages `:focus-visible`). (e) Back-to-back keyboard presses in a
  test can outrace Radix's roving — interleave an
  `expect(...).toBeFocused()` between presses (implicit settle).
  (f) The reference's burger has no aria-label (sr-only span names
  it); the reference's mobile sheet closes via the burger TOGGLE (no
  X button).


Session-68 additions (remediation-plan-v35 audit — the session-70
suggested surfaces: the item-card action menus' open-state focus chrome,
the dashboard quick-action buttons' focus-visible family, the
deep-link/URL contract):

- `census-v35.mjs` — the standing data-drift census (29th — clean; the
  reference's own live numbers re-verified unchanged before + after).
- `clone-mobile-nav-v35.sh` — the clone-side standing checks (R1–R4 +
  the census) against the :3200 parity server; reuses the v34 probe
  files (R1/R2/R3/R4 are date-stable standing checks).
- `probe-menu-census-v35.mjs` / `probe-menu-full-v35.mjs` — the action
  menu's OPEN-STATE structure census: the portal wrapper
  (`data-radix-popper-content-wrapper`), the role=menu container, the
  two menuitems, the full class strings, and the initial focus. NOTE
  the full-open probe dispatches pointerdown + mousedown + click (a
  bare `.click()` does NOT open Radix's DropdownMenuTrigger — it opens
  on pointerdown).
- `probe-menu-itemfocus-v35.mjs` — the REAL-key item-focus reader: the
  active item's `:focus` match + the accent bg + the text color of
  BOTH items (the focused + the resting — the Delete renders red at
  rest but accent-foreground #171717 when FOCUSED on the reference;
  the clone's invented `focus:text-[#dc2626]` was the v35 G1 drift).
- `probe-menu-cls-v35.mjs` — the full menu + item class strings (the
  reference's Delete carries `text-red-600` appended — a plain
  single-class utility that its base `focus:text-accent-foreground`
  OUTSPECIFIES when focused; the cascade IS the contract).
- `probe-focus-add-v35.mjs` / `probe-read-add-fv-v35.mjs` — the
  quick-action Add Item button's focus-visible reader (programmatic
  focus + REAL Tab out-and-back — the `:focus-visible` engagement
  pattern) and the computed four-layer box-shadow composite reader.
- `probe-trig-fv-v35.mjs` — the menu TRIGGER's focus-visible reader
  (REAL Tab landing; the shadcn 1px #0a0a0a ring family — the clone's
  raw Radix triggers lacked it entirely, the v35 G2 fix).
- `clone-surfaceA-v35.sh` / `clone-surfaceA-clean-v35.sh` / `
  clone-surfaceBC-v35.sh` — the clone-side surface probes (the menu
  contract, the quick-action family, the from_url deep link, the 404
  link semantics) against the :3200 parity server.
- `vlm-compare` (ad-hoc, /tmp/vlm35) — the VLM pairs: the dashboard
  (one flag DOM-explained = superset #3 + the demo-data letter/fill)
  and the menu-OPEN state with Delete highlighted (VERDICT IDENTICAL,
  zero flags — the G1 red-vs-dark text is below VLM resolution; the
  DOM-level measurement is the authority).
- LESSONS: (a) **COMPARE THE SAME OPEN PATH** — click-open and
  Enter-open land focus DIFFERENTLY on BOTH sites (click → the menu
  CONTAINER; Enter → the FIRST item); the first cross-path comparison
  (reference click-open vs clone Enter-open) fabricated a phantom
  "the clone lands on an item" finding — measure the FULL matrix (2
  open paths × 2 sites) before claiming a landing difference.
  (b) The genuine reference contract: ArrowUp from the click-open
  CONTAINER lands on the LAST item (the standard Radix convention) —
  an Enter-open-then-ArrowUp sequence reads a CLAMP at index 0 and
  looks like "both arrows land on the first item" (the contamination
  this session's first S1 draft encoded — caught when the test went
  RED on the wrong assertion). (c) The persistent eval scope strikes
  EVERY session — wrap probe bodies in IIFEs via run-probe.sh (the
  `Identifier already declared` family). (d) A "rest" style read
  AFTER a REAL-Tab focus sequence is still a FOCUSED read — blur
  first (the Add Item rest-shadow probe initially read the focused
  composite; the reference's two transparent lead slots are the v3
  compiled-output artifact, the visible pixels identical). (e) A sed
  regex chokes on Tailwind class strings containing `[state=open]`
  (a character-class, not a literal) — use the Edit tool for class
  strings; and a wide sed on a shared substring can strip MORE
  classes than intended (the v35 mutation-B strip also removed the
  expense-card buttons' ring family — caught by the full-chain
  re-run, restored, and the final changeset re-verified against
  `git diff` before shipping).

Session-70 additions (remediation-plan-v36 audit — the session-72
suggested surfaces: the item-card menu's hover-highlight family, the
filter selects' listbox keyboard contract, the items-view Tab-order
census):

- `probe-menu-hover-v36.mjs` — the action menu's HOVER path (synthetic
  mouse events dispatch + read; the LESSON below: they do NOT move the
  Radix highlight — use this file only to open the menu and read the
  pre-hover state; the REAL hover runs via `agent-browser hover`).
- `probe-menu-openonly-v36.mjs` — opens the card action menu via the
  pointerdown family and reads the fresh-open container-focus state
  (the pre-hover baseline for the hover measurement).
- `probe-filter-open-v36.mjs` — the FILTER-card Select's fresh-open
  census (the v34 listbox contract at the /income instances the v34
  pass never measured): the trigger geometry/aria + the selected
  option's accent highlight, `data-highlighted`, `aria-selected`,
  `:focus` match, per-option colors.
- `probe-tabwalk-v36.mjs` — the Tab-stop READER (one stop per call —
  the walk itself needs REAL Tab presses, driven by `tabwalk-v36.sh`).
- `tabwalk-v36.sh` — the REAL-Tab walk driver: blurs, then alternates
  `agent-browser press Tab` with the reader eval (450ms settles).
  Found the reference's Base44 platform badge in its tab order AND the
  kebab's focus-reveal superset (the clone's opacity reads 1 at the
  stop, the reference's 0).
- `probe-head-seo-v36.mjs` — the head-metadata census (title, desc,
  canonical, OG/Twitter, apple title, manifest) — the standing SEO
  pair's reader.
- `clone-surfaceA-v36.sh` / `clone-surfaceB-v36.sh` /
  `clone-surfaceC-v36.sh` — the clone-side surface sweeps (login +
  census, the hover family, the filter listbox contract, the Tab walk)
  against the :3200 parity server.
- `clone-mobile-nav-v36.sh` — the clone-side standing checks (R1–R4 +
  the census, the 30th).
- `clone-vlm-v36.sh` + `vlm-compare-v36.mjs` — the VLM pair captures
  (dashboard + the /income filter-open state) and the pairwise
  comparison via `zai.chat.completions.createVision` (the plain
  `create` endpoint REJECTS image content — error 1210).
- LESSONS: (a) **SYNTHETIC MOUSE EVENTS DO NOT MOVE RADIX'S HOVER
  HIGHLIGHT** — `dispatchEvent(mousemove/mouseenter)` leaves the
  menu's highlight untouched; only a REAL pointer move
  (`agent-browser hover` / Playwright `.hover()`) triggers Radix's
  pointer-driven focus move (the first probe fabricated "the reference
  ignores hover" until the real-hover retry). (b) A blur does NOT
  reset the sequential focus navigation position — Chromium resumes
  the Tab walk from the last focus position; walk the cycle past the
  wrap to read the document-order sequence. (c) The reference's Tab
  order includes the Base44 PLATFORM badge (`#base44-edit-badge` +
  its 18×18 "Close badge" button, fixed bottom-right z-index 999999)
  — platform chrome, NOT app UI; exclude it from tab-order
  comparisons (the VLM pair flags it too). (d) The reference's kebab
  trigger stays INVISIBLE (opacity 0) when keyboard-focused and when
  keyboard-opened — the clone's `focus-visible:opacity-100` +
  `data-[state=open]:opacity-100` (day-one) are the superset #7.
  (e) Radix Select's post-open focus landing is ASYNC — a key press
  racing it hits the trigger instead of the option (the S2 spec's
  fixture-restore initially failed exactly there; interleave a
  `toBeFocused()` between presses — the AGENTS.md e2e-race lesson).

Session-71 additions (remediation-plan-v37 audit — the session-76
suggested surfaces: the filter Select TRIGGERS' focus-visible family,
the search input's focus + typing contract, the /expenses payment-method
filter):

- `clone-v37.sh` — the clone-side standing checks (the 31st: R1–R4 +
  the census) + all three v37 surfaces against the :3200 parity
  server (the trigger ring walk, the search typing contract, the
  payment-method round-trip with the fixture restore).
- `vlm-compare-v37.mjs` — the VLM pair for the /expenses view with the
  payment-method filter open (all five flags data-explained: the card
  count, the extra tags + footer chips + the two extra dropdown
  options = the clone's seed carrying paymentMethod values, the
  avatar letter).
- LESSONS: (a) **The reference's CARD titles are `h4` and its
  EMPTY-state heading an `h3`** — an h3-only card census fabricated
  "the reference's search shows no cards" readings until the h4
  selector caught them; card probes must query the title tag the view
  actually renders (or both). (b) `agent-browser keyboard press
  Backspace` does NOT register in the reference's focused search
  input (six presses, the value unchanged) and the CLI's `fill ""`
  dispatches no input event either — clear a React-controlled input
  in probes via the native value setter + a bubbled `input` Event
  (the React onChange path). Playwright's own `fill("")` is
  unaffected (it drives proper input events). (c) The v3/v4 ring
  CONSTRUCT difference (O1): the reference's focus box-shadow carries
  the v3 three-slot construct (a white ring-offset lead) while the
  clone compiles v4's five-slot construct — every lead is a 0px-spread
  shadow, invisible by construction; assert the VISIBLE layers (the
  1px #0a0a0a ring + the ambient), never the lead count. (d) The
  reference's payment-method filter list carries ONLY its All option
  (its demo items hold no paymentMethod values; its edit dialog
  carries the "payment method" field — read-only open + Escape).

Session-72 additions (remediation-plan-v38 audit — the session-78
suggested-surface queue: the a11y tooling pass, the /expenses frequency
filter, the /savings filter-card instance):

- `ref-v38.sh` / `clone-v38.sh` — the reference + clone standing checks
  (the 32nd: R1–R4 + the census + the SEO pair) and both new surfaces:
  the frequency-filter option census + round-trip (A) and the /savings
  filter-card instance + the category round-trip (B), plus the a11y
  structural census (C: landmarks, unlabeled controls, headings).
- `a11y-scan-v38.mjs` — the axe-core 4.13 deep scan (BOTH sites; the
  wcag2a/2aa/21a/21aa tags, desktop 1280×800, the booted state) that
  drives the permanent `tests/e2e/a11y.spec.ts` gate. Use
  `node a11y-scan-v38.mjs clone|ref` (clone runs INSIDE with-server.sh).
  THE HEADLINE MEASUREMENT: the reference FAILS `button-name` (critical
  — its unlabeled Select triggers + card kebabs) and `svg-img-alt` (its
  recharts donut sectors `path[name=…]`) while the clone PASSES both
  (the aria-label superset + the v31 inert donut); the clone's ONLY
  failures are color-contrast — every flagged node 1:1 with the
  reference's own failure at a byte-identical color (7-color palette).
- `axe-detail-v38.mjs` / `axe-detail-ref-v38.mjs` — the per-node
  enumeration with computed colors (the palette provenance evidence for
  the spec's GATE 2; also the scripts that validated reading computed
  colors off axe node.target selector chains).
- `vlm-shots-v38.sh` + `vlm-compare-v38.mjs` — the VLM pair for the
  /savings view (all four flags data-explained: the card count, the
  classification tags, the payment-method footer chips, the avatar
  letter).
- `hasfocus-gate.sh` — **the v34 discipline formalized as a shared
  helper** (the session-72 tooling pass's first half): `source` it and
  call `focus_gate <session>` before ANY :focus-computed read — it
  asserts `document.hasFocus()`, re-focuses with a REAL `press Shift`
  when the sandbox dropped focus, re-asserts, and fails loud otherwise.
  Bake it into every v39+ standing script that reads focus chrome.
- LESSONS: (a) **`getByRole("option", { name: "Weekly" })` collides with
  "Bi-weekly"** — accessible-name matching is substring-based; use
  `exact: true` in option census loops (the S1 spec's first run hit the
  strict-mode violation). (b) `AxeBuilder.analyze()` requires a page
  from `browser.newContext()` (a bare `browser.newPage()` throws
  "Please use browser.newContext()"). (c) `test.use({ storageState … })`
  is HOISTED per describe — a logged-out test must live in its own
  describe or the opt-out leaks to every test in the block. (d) The axe
  node.target selector chains (escaped classes included) resolve cleanly
  through `document.querySelector` — the color-provenance gate reads
  computed colors off them directly.

Session-73 additions (remediation-plan-v39 audit — the session-80/81
suggested queue's third item: the a11y gate's MOBILE extension):

- `a11y-scan-v39.mjs` — the MOBILE extension of the v38 scanner (390×844,
  isMobile + hasTouch — the mobile-navigation.spec.ts emulation, both
  sites): every authed route sheet-closed + the sheet-OPEN state on /.
  THE MEASUREMENT: the reference at mobile fails button-name (critical)
  on the four item views + svg-img-alt on / + /dashboard — the same
  families as desktop — while the clone passes both everywhere; its only
  failures are color-contrast (the reference's own 7-color palette; the
  mobile node counts differ from desktop only by the demo card counts).
  The sheet-OPEN structural census: the reference's sheet is a plain
  fixed div (no role, no labelledby, no nav, no title); the clone's is
  role=dialog + aria-labelledby → sr-only "Navigation" + nav
  aria-label="Primary" + the named burger.
- `axe-detail-v39.mjs` / `axe-detail-ref-v39.mjs` — the MOBILE
  color-provenance enumeration (the v39 GATE 2 evidence: every
  color-contrast node's computed color on both sites' mobile routes).
- `ref-v39.sh` / `clone-v39.sh` — the 33rd standing checks (R1–R4 + the
  census + the SEO pair) + the mobile sheet-structure probes (the
  ref/clone structural comparison above).
- `vlm-compare-v39.mjs` — the VLM pair for the mobile sheet-open state
  (VERDICT DIFFERENT, both flags explained: the clone's Dashboard active
  highlight = superset fix #3 [the reference marks nothing active on /],
  the avatar letter = the different demo users).
- LESSONS: (a) **the agent-browser daemon can WEDGE after a killed
  parity server** — a hung `agent-browser status` (30s+ timeout) means
  the daemon is stuck; `pkill agent-browser` restarts it cleanly (the
  fresh daemon answers immediately; sessions are disposable). (b) The
  clone's burger is named by its sr-only SPAN, not an aria-label —
  probes must find it via `querySelector('span.sr-only')` or the
  accessible-name role query; `getAttribute('aria-label')` returns null.
  (c) `document.querySelector('nav')` on mobile finds the DISPLAY:NONE
  desktop rail first (DOM order) — the sheet's own nav lives in the
  portal at the END of body; query the sheet element for its nav
  (`sheet.querySelector('nav')`), never the document-wide first match.
  (d) The reference's burger is hit-test BLOCKED by its toast viewport
  (R1) — the mobile sheet probes must JS-click it (el.click()), like
  R2's open probe; a Playwright click works only on the clone (the
  pointer-events fix). (e) `playwright test -g "…"` with `(`/`)` in the
  test title breaks the grep regex — quote-safe patterns or run the
  whole spec.

Session-74 additions (remediation-plan-v40 audit — the session-84/85
suggested queue's first item: the dashboard quick-action focus walk, the
session-78 queue's LAST unmeasured surface):

- `focus-census-v40.mjs` — the clean DOM-order focusable census (a[href] /
  button / input / [tabindex], zero-rect + tabindex=-1 filtered, doc
  coordinates, no Tab-scroll artifacts). THE MEASUREMENT: the reference's
  dashboard cycle is 14 app stops (nav 5 → Add Item → the three
  NetZero-breakdown stat-row buttons → the donut's g.recharts-pie
  tabindex=0 → the three quick-action cards → the Base44 "Close badge"
  [platform chrome]) — the clone's is the SAME walk minus the badge PLUS
  the three interactive stat cards (div[role=button] tabindex=0, stops
  10–12; the reference's big 304×210 stat cards are INERT divs — no
  role, no tabindex, no handler).
- `stat-card-chain-v40.mjs` — the text-ancestor chains ("Total Income" →
  its card-level ancestor): the inert-vs-interactive verdict. The
  reference's chain bottoms out at a plain grid div (no role/ti); the
  clone's at div[role=button]. The census ALONE is misleading here —
  both sites' stat ROWS are real buttons; only this probe separates the
  big-card surfaces.
- `donut-focused-dump-v40.mjs` — the donut tab stop's structure (run
  after the Nth Tab press, N=10 ref / 13 clone): g.recharts-pie
  tabindex=0 on BOTH sites, the sector paths tabindex=-1 (the v31
  roving), the svg surface inert on both. The reference's g carries the
  label texts INSIDE (textContent "92.3%4.6%3.1%"); the clone's renders
  them in a separate recharts-3 layer (g textContent "" — the visible
  chrome is identical, VLM-clean).
- `ref-v40.sh` / `clone-v40.sh` — the 34th standing checks (R1–R4 + the
  census + the SEO pair + the v39 sheet-structure census).
- `vlm-compare-v40.mjs` — the VLM pair for the desktop dashboard
  (VERDICT DIFFERENT, all three flags explained: the clone's Dashboard
  active highlight = superset fix #3, the allocation-bar length = the
  different demo data, the avatar letter = the different demo users).
- LESSONS: (a) the clean census must filter `[tabindex]="-1"` AND
  zero-rect elements or recharts' hidden zIndex layers pollute the count
  (the clone's svg carries ~17 tabindex=-1 groups). (b) The
  reference's stat-card inertness is only visible via the TEXT-ANCESTOR
  CHAIN — the focusable census shows both sites' stat rows as buttons,
  and the tabwalk's 450ms settles can leave the page scrolled (assert
  only scroll-independent bands: x/w/h; y drifts with the auto-scroll).
  (c) `document.querySelector('header button')` matches the MobileTopbar
  burger FIRST (it is display:none at desktop but still in the DOM) —
  query by text content when the target lives outside a semantic
  landmark. (d) The reference's own stat-row column gaps are
  inconsistent (25px then 12px at the third row) while the clone's are a
  consistent 25px — a 13px band drift below that point; both surfaces
  VLM-clean, documented in plan v40 F3.

Session-75 additions (remediation-plan-v41 audit — the session-86/87
suggested queue's first item: the net-worth summary card's gradient chip
at the savings-class viewports — the unmeasured MID viewport class):

- `nw-summary-v41.mjs` — the summary card's full census (card box /
  figure / the 64×64 gradient chip / stats grid / ratio footer / header
  chip / overlay), run at 390×844, 640×960 AND 1280×800 on BOTH sites.
  THE MEASUREMENT: at the MID viewport (640) FULL geometry parity
  (608×333 card, 48px figure, chip 64×64@x=528, 264×2 grid, 18px ratio);
  at MOBILE the reference's card is 432px wide (74px page overflow,
  sw=464, its chip 26px offscreen at x=352, its stats grid a fixed
  2-col) while the clone's fits (358 card, 24px figure, 1-col grid) —
  the superset pair with byte-identical card chrome.
- `nw-yoffset-v41.mjs` — the vertical stack ABOVE the card (the mobile
  top bar, the chipRow, the h1, the subtitle, the card's y). THE FINDER:
  the stack matches byte-for-byte EXCEPT the header row→card gap —
  ref 32 (`mb-8`) vs clone 24 (`mb-6`) — the v41 F1 production fix (the
  first since v38).
- `nw-below-v41.mjs` — the gaps BELOW the card (card→tablist: ref 32 vs
  clone 24 — the second F1 fix; tabs 448×36 and the 144px tabs→grid gap
  match).
- `items-rhythm-v41.mjs` — the items-view's rhythm on /income (the
  no-drift CONTROL): header mb-8 (32, the v20 G1 pin), filter mb-6 (the
  reference's own 24), grid at y=234 — IDENTICAL on both sites; the
  net-worth page was the one rhythm outlier.
- `ref-v40.sh` / `clone-v40.sh` re-run as the 35th standing checks.
- LESSONS: (a) an unmeasured VIEWPORT CLASS is as dangerous as an
  unmeasured surface — the mb-6 rhythm bug survived 40 iterations of
  desktop/mobile pins because the mid viewport was never census'd; a
  two-viewport pin strategy leaves the BETWEEN class dark. (b) An 8px
  y-drift is attributable in ONE probe by measuring the full vertical
  stack (the margins isolate themselves — everything else matched
  byte-for-byte). (c) The reference's page-level section rhythm is
  uniformly `mb-8` — when ONE page's gap disagrees, audit the CLASS (all
  pages' same-role gaps), not just the surface (the items-view control
  proved the net-worth was the outlier in one run). (d) This sandbox
  reaps background processes between tool calls — long jobs (e2e, the
  parity server) must run inside ONE invocation (`with-server.sh`); the
  agent-browser DAEMON and its logged-in sessions survive.

Session-76 additions (remediation-plan-v42 audit — the session-90/91
suggested queue: the MID viewport 640×960 census of the five non-networth
routes — the v41 lesson applied to the remaining route set):

- `mid-census-v42.mjs` — the five-route (/, /dashboard, /income,
  /expenses, /savings) mid-viewport census: the vertical stack (header →
  main → the page-header row → the first section), the section rhythm
  (`gapRowToFirst`), the cap width, the band structure (display/cols/gap
  per band), the overflow. Run on BOTH sites — THE FINDING: the rhythm
  HOLDS on all five routes (32px everywhere, capW 608, sw 640, the
  items-view structure identical) EXCEPT the dashboard's firstSection
  height: ref 664 vs clone 677 (+13).
- `hero-attrib-v42.mjs` — the dashboard hero grid's attribution: the
  goalCard byte-identical (316, bands 48/48/108, donut 558×300), the
  drift isolated to the breakdownCard (324 vs 337).
- `bd-attrib-v42.mjs` — the breakdown card's band-by-band internals —
  THE ROOT CAUSE: the clone rendered TWO `Divider`s (Income|Savings AND
  Savings|Expenses) vs the reference's ONE (Income|Savings only); the
  extra 12+1px band = the +13. The v42 F1 production fix
  (`{i === 1 && <Divider />}`); the row heights wrap identically on both
  sites at 1280 (56/64/64 — width-driven, not data-driven).
- `tail-v42.mjs` — the last-band margin + the total scrollHeight (the
  trailing-space class check): lastBand mb=0 on BOTH sites (no
  trailing-margin class), scrollH 3029 vs 3042 — exactly the +13
  divider band, nothing else.
- `vlm-compare-v42.mjs` + the /tmp/vlm42 pair — the standing VLM
  screening (the desktop dashboard post-fix): all three flags in the
  known classes (the Dashboard-highlight superset #3, the allocation-%
  seed data, the avatar letter) — no new drift.
- `ref-v40.sh` / `clone-v40.sh` re-run as the 36th standing checks.
- LESSONS: (a) a height drift ATTRIBUTES FASTER BAND-BY-BAND than
  card-by-card — the bd-attrib probe isolated the divider in one run by
  listing every stack child with its height/margins. (b) The
  DOM-structure census (child COUNT) catches what the geometry census
  misses: the +13px was visible in firstSection.h, but the root cause
  was a 6-vs-5 child count — census BOTH. (c) The reference's divider
  structure encodes the app's ONE rule ([Income] | [Savings, Expenses] |
  border-t | [Net]) — uniform `i > 0` dividers were a build-time
  assumption, never measured; the assumption class (uniform symmetric
  chrome) is exactly where asymmetric reference design hides. (d) VLM
  screening flags stay in the known classes (superset pins + seed data)
  — the divider fix itself drew no flag, the heights now matching.

Session-77 additions (remediation-plan-v43 audit — the session-92/93
suggested queue: the drill-down EXPANDED-state census + the summary
card's hover/interaction states):

- `exp-census-v43.mjs` — the drill-down expanded-state census (both
  sites, 640×960): expands the Total Income section + its first
  category, reads every band's chrome (the section/category/sub/item
  rows + the footer) and the card's expansion heights. The chrome is
  BYTE-IDENTICAL at every level (section 48/8px/-8px/8px radius;
  category 28/"6px 12px"/inline rgb(249,250,251)/6×6 dot; sub
  24/"4px 8px"/rgb(250,250,250)/4×4 dot at 0.6; item 24/"4px
  8px"/12px/rgb(156,163,175)/2×2 dot at 0.4/120px truncate; footer
  29/border-t); the heights differ only by DATA (the seed's 2 categories
  vs the reference's 1 → +36).
- `exp-detail-v43.mjs` — the label-span fonts + the fresh-query chevron
  (the saved node goes STALE on React re-render — computed styles of
  detached nodes read ""/none; always re-query after the click).
- `exp-rotate-v43.mjs` — THE definitive rotation probe: reads the CSS
  `rotate` property. Tailwind v4's rotate-* utilities emit the modern
  `rotate` property, NOT `transform` — a `transform: none` reading on
  BOTH sites is MEANINGLESS (the v4 property trap). FINDINGS: the
  reference's chevrons are STATIC at BOTH levels (rotate: none,
  transform: none, transition "all" 0s); the clone's pre-fix
  rotate-180 rendered rotate: 180deg (0.15s). The v43 F1 production fix
  (the two chevrons stripped of rotate-180 + transition-transform).
- `hover-v43.mjs` — the REAL-pointer hover census: the section row's
  engaged hover (the reference rgb(249,250,251) vs the clone's pre-fix
  lab(98.2596 -0.247031 -0.706708) — the v4 named-palette trap, LIVE on
  this surface; the v43 F2 fix hover:bg-[#f9fafb]); the category rows'
  hover inert on BOTH (the inline bg overrides — v29); the net-worth
  summary card STATIC on both (the queue item resolved: same gradient,
  same shadow rgba(26,58,46,0.3) 0 20 60, cursor auto — no interaction
  states exist to match).
- `vlm-compare-v43.mjs` + the /tmp/vlm43 pair — the standing VLM
  screening (the EXPANDED drill-down post-fix): all three flags in the
  known classes (the Dashboard-highlight superset #3, the avatar letter
  data, and the reference's own Base44 dev badge misattributed to the
  clone — DOM-verified: the fixed z-999999 div lives on the REFERENCE).
- `ref-v40.sh` / `clone-v40.sh` re-run as the 37th standing checks.
- LESSONS: (a) read the CSS `rotate` PROPERTY for v4 rotation states —
  `transform` never shows Tailwind v4's rotate-* (the mirror image of
  the shadow/space-y traps: v4 maps familiar class names to NEW
  properties). (b) A saved DOM node goes stale across a React
  re-render — computed styles of detached nodes return empty/none;
  re-query after every state change. (c) The named-palette lab() trap
  lives in HOVER states too — hover:bg-gray-50 computes lab() in v4;
  the arbitrary-hex fix (hover:bg-[#f9fafb]) works because the hover
  selector carries no inline-style override. (d) The "inert hover" class
  (inline bg beating the hover class) is DOM-identical on both sites —
  parity holds without a fix when the reference has the same inert
  class. (e) VLM image-order attribution is unreliable — a fixed
  overlay flag must be DOM-verified before it counts.

Session-79 additions (remediation-plan-v44 — the session-95/96/97
suggested queue: the drill-down's EXPANDED-state census at the OTHER
viewports + the donut legend's interaction):

- `exp-vp-v44.mjs` — the drill-down expanded-state census at the
  REMAINING viewports (390×844 and 1280×800, run via
  `vp-census-v44.sh`): the chrome byte-identical at every level on BOTH
  sites (the section 48/8px at 390 and 56/labelH-40 at 1280 — the
  2-line WRAP on both sites, the v42 collapsed census's 56px row
  explained: width-driven); the mobile indentation arithmetic (the inner
  ml 40px/mt 8px — no responsive indent exists); the clone's sw 390
  fully expanded (the superset — the reference reads 395, its own
  overflow); the expansion-height SAMPLES at 25ms intervals — the
  reference ramps ~200ms in both directions, the pre-fix clone jumped
  instantly (the v44 F1 gap).
- `legend-v44.mjs` — the donut legend census: the rows' geometry
  (h 64/pad 12/radius 8/bg 245,248,245; the label 16px/500/forestDark;
  the amount 16px/700 in the classification color; the pct 12px/gray;
  the dot 16×16/r4; the icon 16×16; the gap 12; the container mt 24)
  — byte-identical on both sites at both viewports, and the REAL hover
  INERT on both (no interaction states exist — the queue's
  legend-interaction item resolved). Structure-agnostic lesson: the
  reference's textContent concatenates WITHOUT spaces, so text-matching
  the ROW fails — match the exact-text LABEL span, then climb.
- `collapse-ref-v44.mjs` + `band-mount-v44.mjs` — the reference's
  collapse-direction + mount-semantics decode: the collapse ALSO
  animates (~200ms, the height ramp + the opacity ease — computed
  0.314 at 110ms into a collapse), the section band UNMOUNTS after the
  collapse animation (the collapsed root = the button alone), and
  mid-collapse the band's INLINE style reads `height: 25.5455px` — a
  per-frame JS tween writing fractional heights, NOT a CSS transition
  (the end state `height: auto; opacity: 1`). THE v44 F1 contract.
- `chev-glyph-v44.mjs` — the chevron GLYPH-swap verification (the
  standing VLM pair flagged "the chevron points UP on the reference" —
  DOM-verified REAL): lucide-chevron-down collapsed ↔
  lucide-chevron-up expanded at BOTH levels (section 14px, category
  12px), rotate: none at every state. **A computed-style census CANNOT
  see a glyph swap — read the svg's class list.** The v43 "static"
  finding was correct-but-incomplete: the flip is the ICON, not the
  transform.
- `vp-census-v44.sh` / `clone-v44.sh` — the multi-viewport drivers (run
  both probes at 390 + 1280 on a logged-in session; the clone driver
  wraps the login + runs inside with-server.sh).
- `vlm-compare-v44.mjs` + the /tmp/vlm44 pair — the standing VLM
  screening (the expanded drill-down post-fix): the glyph-direction
  flag was REAL (the F4 fix) — the VLM screening earns its keep; the
  other flags (the icon outline-vs-solid, the bold labels) were
  screenshot-scale misreads, DOM-refuted (the lucide classes and the
  font-weight 500 identical).
- The v44 F1 fix: the `Collapse` wrapper (the grid 0fr↔1fr technique +
  `@starting-style` for the entry + the onTransitionEnd delayed
  unmount) — see `src/components/budget/dashboard-view.tsx` + the
  `.zb-collapse` class pair in `src/app/globals.css`.
- LESSONS: (a) a height-curve census catches what the end-state census
  cannot — sample DURING the transition, both directions (the pre-fix
  clone's end states were byte-identical; only the in-flight samples
  exposed the animation gap). (b) The grid 0fr↔1fr technique +
  @starting-style animates height 0↔auto with NO JS frame games — and
  the delayed unmount (onTransitionEnd) returns the collapsed DOM to
  exactly the conditional-mount tree (the accordion count-0 pins hold).
  (c) A computed-style census is BLIND to glyph swaps — read the svg
  class list (rotate/transform read "none" while the icon flips). (d)
  The VLM pair catches glyph-level flags the geometry census misses —
  DOM-verify before counting (v43's badge was a misattribution; v44's
  glyph flag was real). (e) The reference's textContent concatenates
  without spaces — match exact-text leaf spans and climb, never
  text-match container rows.

## v45 — the shadow-scale sweep + the items-view card grid + the calculator row hover (session-100/101)

- `items-card-v45.mjs` — the items-view CARD census (the grid located by
  its grid-cols-3 class, the card chrome, the title row, the kebab, the
  hover-revealed action row; tags the first card for the driver's REAL
  hover step).
- `calc-row-v45.mjs` — the calculator LINE-ITEM ROW census (the row
  located via its h4 climb to the p-4 bordered block; the rest action
  pair; a synthetic-event hover — which does NOT engage CSS :hover, see
  the lessons).
- `ref-v45.sh` / `clone-v45.sh` — the drivers (login → the /income +
  /expenses censuses at 1280 → the REAL `agent-browser hover` steps →
  the calculator: the reference's RENT card — the ONLY one of its four
  expense cards with line items — the clone's API-created row + the
  delete + PATCH restore).
- `vlm-compare-v45.mjs` + the /tmp/vlm45 pair — the standing VLM
  screening (the /income items-view at 1280): **IDENTICAL, zero flags —
  the first fully-clean screening since the pair began.**
- THE V45 DISCOVERY — the shadow-scale sweep: every live `shadow-*`
  utility's VISIBLE layers match on both sites, but the LEAD layers
  diverge by construction (v4's 5-slot composition emits 4 transparent
  leads vs v3's 2 — e.g. the calculator row's hover: the reference reads
  4 layers, the clone 6, the same 2 visible). The accepted v10/v25
  class, now census'd across the full scale (sm/md/lg/xl/2xl) and PINNED
  as the regression net (a future Tailwind upgrade that changes the
  scale numerics fails the suite).
- LESSONS: (a) a REAL `.hover()` (Playwright's locator.hover() or
  `agent-browser hover`) is the ONLY way to engage CSS `:hover` — a
  synthetic `dispatchEvent(new MouseEvent('mouseover'))` fires the
  listeners but never sets the pseudo-class (the first calc-row draft
  read "inert" for BOTH sites on a live hover). (b) The reference's RENT
  calculator is the only one of its four expense cards with line items —
  probe the card with data, not the first one. (c) The calculator rule
  sets the parent's amount to the line-items SUM — a probe that creates
  + deletes a row must PATCH the parent back (deleting alone recalcs to
  0; the seed's 1850 does not come back). (d) Chrome normalizes a
  3-value inline box-shadow to the 4-value computed form — the clone's
  `rgba(0,0,0,0.04) 0px 2px 8px` and the reference's inline compute the
  IDENTICAL string. (e) The reference's dialog is an
  overlay-wrapping-panel while the clone's is a Radix [role=dialog]
  portal — a shared probe needs both finders (the v44 sheet lesson,
  generalized). (f) `next build` typechecks the spec files too — an
  evaluate's early return with a narrower object shape fails the build,
  not the test run.

## v46 — the net-worth card census + the value→facts fix + the white-pill pin (session-101/102)

- `nw-card-v46.mjs` — the net-worth ASSET/LIABILITY CARD census at 1280
  (the grid located by `lg:grid-cols-3` — NOT the summary card's inner
  `sm:grid-cols-2` stat-blocks grid, the v4 G4 design; the first draft's
  finder caught the wrong grid and read "no grid"): the grid 960 /
  3×309.328 / gap 16, the card chrome (pad 20/radius 12/border
  rgb(229,231,227)/the inline rest shadow), the title row, the type
  badge, the value figure, the facts, the kebab (36×36 opacity 0,
  tagged for the driver's click step).
- `confirm-pill-v46.mjs` — the delete-confirm BAR census (the red bar +
  the Cancel white-pill + the red Delete): the pill's shadow-sm VISIBLE
  layer `rgba(0, 0, 0, 0.05) 0px 1px 2px 0px` — the `--shadow-sm` theme
  pin's regression net (the five-site family: item-card, budget-item
  dialog, calculator dialog, net-worth asset + liability).
- `ref-v46.sh` / `clone-v46.sh` — the drivers (login → /networth at
  1280 → the census → the REAL hover → the kebab → Delete → the bar
  census → Cancel).
- `vlm-compare-v46.mjs` + the /tmp/vlm46 pair — the standing VLM
  screening (the /networth view at 1280): **IDENTICAL, zero flags — the
  second fully-clean screening.**
- THE V46 FINDING — the value→facts spacing: the reference wraps its
  card value in `mb-4` (16px) while the clone's bare `mb-2` P rendered
  8px (the card h 186 vs 194; the item-card's own `mb-4` wrap the
  in-repo precedent — the net-worth cards were the one oversight). The
  fix: `mb-2`→`mb-4` on both cards' value P.
- LESSONS: (a) **THE INCIDENT — the reference's net-worth kebab flow is
  NEVER safe to probe past the menu open**: the menu's Delete click IS
  the delete attempt (no confirm bar on the reference — the v18
  superset-fix-#6 family); this session's probe deleted the reference's
  only asset and had to restore it via its Add Asset form (name
  "Savings Account", type bank account, value 25000, institution
  "Commonwealth Bank", date 2026-10-07 — the panel census re-read "1
  items · $25,000" byte-identical to the before state). (b) A Radix
  dropdown (and the reference's tab triggers) ignore synthetic
  `el.click()` — only a NATIVE Playwright/agent-browser click engages
  them (the v45 :hover lesson generalizes to pointer-driven widgets).
  (c) The reference's dialogs are plain `fixed inset-0` divs with NO
  `[role=dialog]` — find them by the Save-button text (the v45 lesson,
  re-applied to the Add Asset form). (d) The confirm-bar's pill/text
  colors compute as `lab(...)` strings (Tailwind v4's oklab emission
  for the named palette) — ACCEPTED for superset-only surfaces (no
  reference counterpart to byte-match); the shadow VISIBLE layer is the
  pin that matters. (e) The agent-browser daemon's Chrome instances
  survive across tool calls — kill them (`pkill -f agent-browser`)
  before a Playwright run or the browser contexts crash on
  pthread_create resource exhaustion.

## v47 — the dialog-input focus composite + the net-worth mobile census + the sheet's shadow-lg (the session-101 queue #2 + the v46 follow-up)

- `dlg-focus-v47.mjs` — the dialog input's FOCUS-state shadow composition
  census (the Add-Item/Add-Income dialog's first input, the clone's
  [role=dialog] finder): the rest census (the shadow-sm visible layer +
  the v4 5-slot layer count) + the REAL focus (`focus({ focusVisible:
  true })`, the v35 idiom) census (the ring + the persisting rest
  shadow + the unchanged border + the outline style).
- `nw-mobcard-v47.mjs` — the net-worth ASSET card's MOBILE census at
  390 (the wrap-aware value gap: the clone's P-carried mb-4 vs the
  reference's div.mb-4 wrap — the computed geometry is the contract).
  Works on BOTH sites (the reference's grid has no `grid-cols-1` in
  its class string — the structural finder keys on md:lg: classes).
- `sheet-chrome-v47.mjs` — the MOBILE SHEET chrome census at 390 (the
  structural finder: fixed + 250–330 wide + contains links — covers
  both the clone's [data-state=open] sheet and the reference's plain
  fixed div; the overlay = the fixed dim layer without links): the
  sheet's bg/geometry/shadow-lg visible pair + the layer count + the
  overlay bg/z.
- `ref-v47.sh` / `clone-v47.sh` — the drivers (READ-ONLY on the
  reference: the dialog opens + Cancels, the sheet opens + closes, NO
  Delete clicks — the v46 incident rule).
- `vlm-compare-v47.mjs` + the /tmp/vlm47 pair — the standing VLM
  screening (the MOBILE /income view at 390 — a fresh surface; the
  reference's /income is overflow-free at 390, docSW verified live):
  3 flags, all DOM-verified as data/platform classes (the clone's
  richer seed carries a 4th Recurring badge that wraps in the
  byte-identical `flex flex-wrap gap-2` container — the reference has
  no second card; the "Edit with Base44" FAB is the reference's own
  platform chrome) — no chrome gaps.
- THE v47 FINDING — everything at parity on the VISIBLE layers, the
  third pin-only iteration (v45-family): the dialog input's focus
  composite (the reference's 3-layer v3 composition vs the clone's
  5-layer v4 construction — the SAME ring + shadow-sm visible layers);
  the net-worth card's mobile rhythm (h 194 both sites, the value mb
  16 both sites — the v46 fix survives the mobile reflow); the mobile
  sheet (the shadow-lg visible pair + the geometry/bg/overlay).
- LESSONS: (a) **a src/ mutation is INVISIBLE to the e2e suite until
  `npm run build` runs** — the tests run against the standalone build,
  not the source tree; the first ring-1 mutation "passed" until the
  rebuild, then bit. (b) The reference's net-worth grid class string
  has no `grid-cols-1` (its mobile column count comes from the md/lg
  responsive classes alone) — a structural finder keyed on grid-cols-1
  finds only the clone; key on the md:/lg: pair for a shared probe.
  (c) The reference's badge rows: the badge texts are leaf DIVs (not
  spans) — find them by text with a children<=1 filter. (d) The
  clone's /income seed carries a second card with the conditional
  green Recurring badge (4 badges) — at 390 the 4th wraps; the
  reference's single-card data never shows this; the wrap is the
  byte-identical flex-wrap behavior, not a chrome gap (VLM flags need
  the DOM verification — the v43 lesson, third application).

## v48 — the item-details shadow-2xl + the dialog-input 390 composite + the empty-state census (session-108/109 queue #1 + #4 + #3)

- `ref-v48.sh` — the reference-side driver (READ-ONLY: the card-click
  + details census + close; the dialog-open + input-focus + cancel;
  the frequency filter-to-zero + the reset-verified restore — no
  Delete clicks anywhere, the v46 incident rule).
- `clone-v48.sh` — the clone-side driver (the same three surfaces via
  with-server on :3200; the search filter-to-zero is the e2e idiom —
  the live probe used the reference's frequency-Select route).
- `standing-checks-v48.sh` — the 42nd standing check, clone side
  (R1–R4 + the SEO pair, one script).
- `vlm-compare-v48.mjs` + the /tmp/vlm48 pair — the standing VLM
  screening (the /savings view at 1280 — the fresh DESKTOP surface):
  4 flags, all DOM-verified as data classes (the richer seed's 2-card
  grid, the Recurring + payment-method rows, the avatar initial; the
  badge chrome byte-identical — the reference's need chip
  rgb(254,242,242)/rgb(185,28,28) = the clone's need map exactly).
- THE v48 FINDING — everything at parity on the VISIBLE layers, the
  FOURTH pin-only iteration (v45-family): the details panel's
  shadow-2xl (the net's seventh site — `rgba(0,0,0,0.25) 0px 25px 50px
  -12px` on both sites, the reference's 3-slot vs the clone's 5-slot);
  the dialog input's focus composite at 390 (the input w 310 on BOTH
  sites — the mobile content width; the same rest + focus visible
  layers, the family viewport-independent); the empty-state block at
  BYTE-PARITY (the whole 358×328 census incl. the Add button's v3
  bare-shadow pair).
- LESSONS: (a) **the reference's toast is RARE-PATH only** —
  empty-form saves never toast (measured live twice this session, on
  /income and /networth); the clone's toasts are the documented
  superset UX (the v10 note). A toast census needs a REAL save (data
  mutation) — defer to a queue where mutation is sanctioned. (b) The
  reference's frequency Select carries non-matching options
  (One-time/Weekly/… vs its monthly items) — the read-only
  filter-to-zero trigger for empty-state probes (reset verified by
  the after-census). (c) The reference's empty-state Add button
  carries the GRADIENT + v3 BARE-shadow family (NOT the --shadow-sm
  navbar pin) — the two shadow scales coexist by surface; a naive
  "all shadow-sm" sweep would mis-pin. (d) The clone's details close
  button is found by its accessible name "Close" (the sr-only span) —
  an empty-text finder misses it (the first F1 draft's TypeError). (e)
  The VLM's badge-color flag on /savings decomposes into the
  classification VALUE difference (need=red vs savings=green) — the
  CHIP chrome is identical per value; DOM-verify the color map before
  counting a badge flag (the v43 lesson, fourth application).

## v49 — the login spacer fix + the donut legend mobile reflow + the calculator 640 chrome (session-111 v49 queue #1 + #2 + #3)

- `ref-v49.sh` — the reference-side driver (READ-ONLY: the logged-out
  login-panel census at 390; the login for the donut-legend leaf
  census at 390; the calculator open via its Calculate click + census
  + X close at 640 — no saves, no deletes, the v46 incident rule).
- `clone-v49.sh` — the clone-side driver (the same three surfaces via
  with-server on :3200).
- `ref-standing-v49.sh` — the 43rd standing check, REFERENCE side
  (login + the four reference bugs + the read-only data census + the
  SEO pair).
- `standing-checks-v49.sh` — the 43rd standing check, clone side
  (R1–R4 + the SEO pair, one script — generated from the v48 family).
- `vlm-compare-v49.mjs` + the /tmp/vlm49 pair — the standing VLM
  screening (the LOGIN page at 390 — THE FIXED SURFACE, a data-free
  static form): **IDENTICAL, zero app flags** (the only flag the
  reference's own "Edit with Base44" FAB platform chrome) — the F1
  fix's visual verification.
- THE v49 FINDING — ONE REAL DRIFT (the first production-code change
  since v46) + two pin-only surfaces: (1) the reference's login
  wrapper carries a mobile-only SECOND child — `<div class="mt-8
  text-center text-xs text-slate-400 sm:hidden"><p>&nbsp;</p></div>`
  (h 16, mt 32, rgb(148,163,184)) below the panel — lifting its card
  stack 24px above the geometric center at 390 (the panel y 57 /
  wrapper 730; the clone pre-fix centered the panel ALONE at y 81 /
  wrapper 682). Verified on the reference's sign-in AND sign-up
  states; at 640 the spacer is display none (sm:hidden) and the panel
  re-centers — the desktop pins were always safe, the drift was
  mobile-only and first-measured this session. (2) The donut legend at
  390: byte-identical chrome (the v44 F3 measured both viewports but
  pinned only 1280 — the v49 pin locks the mobile reflow; the
  reference's row w 313 rides its own 395 docSW overflow, the clone's
  308 fits — the superset-fix-#4 family). (3) The calculator panel at
  640: byte-identical chrome (the v45 F2b pinned only the widths after
  a line-item add; the v49 pin censuses the read-only open state's
  panel + close + header border + the centering invariant).
- LESSONS: (a) **Census the WRAPPER's children, not just the panel** —
  the reference's login-page vertical layout at 390 is a three-element
  stack (main p-4 → the w-full max-w-md wrapper → panel + spacer); a
  panel-only census reads the card as "centered" when the reference's
  stack is not — the y-offset drift hides one level above the card.
  (b) **agent-browser's screenshot syntax is `screenshot [selector]
  [path]`** — `screenshot <path> full` mis-fires (the path parses as a
  SELECTOR, the word "full" as the path; the file never lands). (c)
  The reference's donut-legend row w 313 vs the clone's 308 IS the
  reference's own 5px /dashboard overflow (docSW 395) — the row-width
  diff rides the overflow, not a chrome gap (the v46/v47 lesson
  family). (d) The reference's sheet-trap needs the PRECISE overlay
  census (z-50 + rgba(0,0,0,0.8) + geometry) — a heuristic detector
  keying on overlay TEXT misses it (the overlay div itself is
  empty-texted; the sheet's content is a sibling). (e) The calculator
  panel's absolute height is data-dependent — pin the CENTERING
  invariant (y == round((vh − h)/2)) + the chrome, never the height.

- `ref-v50.sh` + `clone-v50.sh` — the v50 surface drivers: the auth
  states' FULL 390 census (the sign-in baseline + the sign-up and
  forgot client-state swaps — the v49 precedent), the networth
  tablist's chrome at 640, the dashboard hero's mobile reflow at 390
  (the goal-card walk + the internals + the chip census).
- THE v50 FINDING — ONE REAL DRIFT (the second production-code change
  since v46) + two pin-only surfaces: (1) the clone's sign-up and
  forgot panels were 16px SHORT at every viewport (406 vs 422 / 294 vs
  310) — the v4 space-y × `-mb-2` override: the reference's v3 build
  STACKS the back button's own -mb-2 with the heading's mt (the
  collapsed 16 + (-8) = the 8px net gap) while v4's zero-specificity
  `:where(& > :not(:last-child))` margin-block-end lets the utility
  OVERRIDE the container gap (the heading overlapped the button by 8px
  AND the container lost 16px — the form heights were IDENTICAL,
  isolating the drift to the one junction). The fix: the scoped
  `.zb-auth-mode` restore (the container DROPS the space-y class —
  no zeroing rule: a 0-2-0 `> :not(:last-child)` zero beats the
  0-1-0 -mb-2 utility and kills the collapse — the first attempt's
  measured 430) + the forgot's `.zb-sm6` sm tier (the reference's own
  DOM class `space-y-4 sm:space-y-6` — 24px at >=640). (2) The
  networth tablist at 640: byte-parity (the full reference shadow
  string re-measured UNSLICED: 2 transparent leads + the shadow-sm
  VISIBLE pair; the clone: 4 leads + the pair — the accepted
  lead-divergence class, the visible layers byte-identical). (3) The
  dashboard hero at 390: byte-parity (the goal card, the internals,
  the chip — both sites' 20px svgs squish IDENTICALLY to 12px under
  the chip row's flex-shrink, a byte-shared width-pressure artifact).
- LESSONS: (a) **A stale agent-browser session hangs the next open** —
  a killed run leaves the `.config`/`.engine` pair in
  ~/.agent-browser and the next `agent-browser open` on that session
  name waits forever (the first clone-v50 run hung 600s): `pkill -f
  agent-browser` + a session-file sweep (`rm -f
  ~/.agent-browser/<session>.*`) before every probe run. (b) **A
  rebuild swaps `.next/standalone` UNDER a running parity server** —
  page loads die with the browser's own "This page couldn't load"
  interstitial (not an app error): reboot the :3200 server after
  every build. (c) The smoke script's step-0 `pkill -f
  standalone/server.js` kills the parity server too — reboot after
  smoke. (d) **Slice-bounded censuses lie about multi-layer
  shadows** — the v49 tablist probe sliced the reference's shadow at
  50 chars (2 of 4 layers); re-measure the FULL string before pinning
  layer counts. (e) The reference's `sm:space-y-6` tier is readable
  from its own DOM class list — a viewport-tier divergence visible
  without a second live measurement.
- `vlm-compare-v50.mjs` + the /tmp/vlm50 pair — the standing VLM
  screening (the login SIGN-UP state at 390 — THE FIXED SURFACE): the
  VLM flagged 4 diffs (card position / button width / spacing /
  shadow depth) — ALL DOM-verified as noise (the panel y 187 / h 422
  / the button 294@x 48 IDENTICAL on both sites; the shadow-depth
  flag is the accepted lead-divergence class) — the v43
  misattribution lesson's fifth application.

- `ref-v51.sh` + `clone-v51.sh` — the v51 surface drivers: the
  dashboard's STATS ROW at 390 (the three StatCards' grid/rhythm/
  chrome/internals), the SAVINGS view at 390 (the goal-card census +
  the view chrome), the BUDGET GUIDELINES card at 390 (the card + the
  tiles container + the three tinted tiles), and the follow-up
  censuses (the goal card's internals, the quick-actions row, the
  unsliced guidelines shadow — run as inline with-server evals).
- THE v51 FINDING — ONE REAL GAP (the third production-code change
  since v46) + four pin-only surfaces: (1) the v50 F1's THIRD-site
  conversion was CLAIMED but NEVER APPLIED — the v50 plan (§F1), the
  commit message, and all five docs stated "the verify-email branch's
  same-idiom container converted," the v50 diff landed the describing
  comment at login-card.tsx:605-607, but the line-608 class swap
  itself never shipped: the verify branch still read `space-y-4`.
  Measured via a fresh CLONE-side registration (the reference stays
  read-only): the verify panel 492 (16px short), the junction netGap
  −8 (the centered inner stack overlapping the back button by 8px).
  The fix: the one-class swap (`zb-auth-mode`, no `zb-sm6` — the
  verify container carries no sm tier). (2–5) The stats row, the
  savings view, the Budget Guidelines card, and the quick-actions row
  at 390: ALL byte-parity (the full-page vertical rhythm identical —
  the stats cards @ 949/1183/1417 and the quick-actions @
  2751/2865/2979 on BOTH sites; the savings card height is a data
  class — the richer seed's 4-chip badge wrap, never pinned).
- LESSONS: (a) **The verify panel's height is EMAIL-LENGTH-DEPENDENT**
  — the "We've sent a 6-digit code to {email}" block wraps per the
  address's length (a 38-char address wraps one extra line, +20px:
  the first GREEN attempt measured 528, not 508) — pin with a FIXED
  21-char email (the global-setup re-seeds db/e2e.db every run, so
  the address is reusable). (b) **Playwright does NOT typecheck** —
  the `c.querySelector &&` TS2774 always-defined check runs green at
  runtime but fails `next build`'s tsc (a new spec file needs a build
  before the chain gate, not just a test run). (c) **The with-server
  heredoc kills its server at the end** — every follow-up eval needs
  a fresh invocation (the mid-flow "Network error"). (d) The sign-up
  form carries THREE inputs (email + password + Confirm Password) —
  a probe that fills only the first two never submits (native
  validation blocks it silently). (e) The savings page carries a
  hidden desktop-sidebar H2 brand — an `h1, h2` finder hits the
  hidden 18px H2 first (the probe artifact; the VISIBLE top-bar brand
  is the 20px H1, both sites). (f) The reference's quick-action card
  internals are readable from its own DOM (the button's class string
  `p-6 rounded-2xl text-left transition-all …` + the wrapper div +
  the 40×40 circle + the trailing plus's `ml-auto opacity-50
  group-hover:opacity-100 transition-opacity` — the class-attribute
  census, not a computed-style guess).
- `vlm-compare-v51.mjs` + the /tmp/vlm51 pair — the standing VLM
  screening (the /savings view at 390 — THE F3 SURFACE): the VLM
  flagged 3 diffs (the count subtitle / the card contents / the
  extra-card layout length) — ALL DOM-verified as the documented
  seed-data classes (the reference's 1 Emergency Fund card vs the
  clone's 2 richer-seed cards with the 4-chip badge rows; the chrome
  byte-pinned by the F3 test) — the v48 precedent's second
  application.

## v52 — the details sheet's subcategory + the /income and /expenses mobile censuses (session-121/122)

- `ref-v52.sh` + `clone-v52.sh` — the v52 surface drivers: the
  /income view at 390 (the header row's mobile reflow + the filter
  card + the item-card grid), the /expenses view at 390 (the same
  family + the 4-child filter grid), and the item-details sheet's
  internals at 390 (opened via the read-only card-body click).
- THE v52 FINDING — ONE REAL GAP (the fourth production-code change
  since v46): the details sheet's summary was missing the SUBCATEGORY
  P. The reference renders FIVE summary elements (the chip row → the
  H3 name → the P.text-lg subcategory 18/400/rgb(107,114,128) → the
  amount) — Rent → "Apartment", Salary → "Main Job" — while the clone
  rendered four (the H3 → the amount directly). The field was always
  on the clone's model (the card renders it, the edit dialog edits
  it); the details view simply never wired it. The one-insert fix
  lands between the H3 and the amount.
- The /income and /expenses 390 censuses: BYTE-PARITY on every
  visible axis (the header row 358×112 flex-col/gap 16/mb 32; the
  48×48 gradient chip; the H1 30/700; the per-type-gradient Add
  buttons 147/155×36; the filter card 358/radius 16/pad 24; the inner
  grid 1-col 308/gap 16 with the 3- and 4-child variants; the search
  308×36/pad 4 12 4 40; the item grid + the first card's chrome;
  docSW 390).
- The details sheet's internals: byte-parity (the sticky header h 69,
  the title 18/700, the 36×36 close, the body space-y-6 p-6, the chip
  row gap 8/mb 12, the classification block radius 12/pad 16, the
  fact rows gap 12/pad 8 0, the meta footer grid-cols-2) — plus the
  accepted 4-vs-2 shadow-lead divergence (the 2xl layer's visible
  pair byte-identical).
- `vlm-compare-v52.mjs` + the /tmp/vlm52 pair — the standing VLM
  screening (the /expenses view at 390 — THE F3 SURFACE): the VLM
  flagged 4 diffs (the header count/total; the card contents; the
  Base44 FAB [mislabeled as the clone's — the FAB is the reference's
  own platform chrome]; the layout length) — ALL DOM-verified as the
  documented seed-data/platform classes (the v47/v48 precedents).
- P1 — the standing script's burger selector: `clone-stand47.sh`'s R1
  step clicked `button[aria-label="Open menu"]` — the REFERENCE's DOM
  idiom; the clone's burger carries no aria-label (its accessible
  name rides the sr-only "Toggle Sidebar" span) so the click failed
  SILENTLY (`|| true` masked it) and R1 read sheetLinks:0 — a false
  red on a working surface. The fixed text-walk eval reads
  sheetLinks:5 (the 46th standing check re-verified with it).
- Probe lessons: (a) the reference session EXPIRES between long eval
  gaps — re-login via the same eval before any follow-up census. (b)
  `agent-browser set viewport` state does NOT survive a session
  restart — re-apply the 390 viewport before any mobile census after
  a re-login (a post-restart census read the desktop 4-col filter
  grid at "215.5px" tracks — the false reading). (c) The reference's
  details sheet carries NO [role=dialog] (the no-landmark family) —
  find it via the `fixed inset-0 z-50` overlay class census instead.
  (d) The reference's summary is a TWO-LEVEL title structure (the H3
  name + the P subcategory) — walk the FULL subtree; a leaf-only
  census misses the siblings between the levels. (e) The rounded-full
  computed radius diverges v3 (9999px) vs v4 (3.35544e+07px) — both
  fully-round pills clamped at h/2; pin the CLASS, not the computed
  value.

## v53 — the /networth tablist + the calculator dialog mobile censuses (session-124/125)

- `ref-v53.sh` + `clone-v53.sh` + `clone-v53b.sh` — the v53 surface
  drivers (the session-124 queue's read-only members): the /networth
  view's TABLIST at 390 (the list + the active/inactive trigger pair
  + the 16px currentColor icons — the v50 pin walked this family at
  640 only) and the CALCULATOR DIALOG at 390 (the panel + the header
  + the chip + the close + the total card + the line-item rows + the
  Add button — the v45/v49 pins walked the family at 640 only;
  clone-v53b is the with-row follow-up: add one line item → census →
  delete → close, on the clone's OWN db).
- THE v53 FINDING — NO PRODUCTION GAP: both surfaces are already at
  byte-parity. The deliverable is the pin pair (F1 networth.spec.ts,
  F2 calculator.spec.ts) + the probe scripts + the docs.
- The TABLIST at 390: byte-parity on every chrome axis — the list
  h 36/grid/#f5f5f5/radius 8/pad 4/maxW 448, the active trigger the
  green pair (#14532d on #dcfce7, the shadow-sm VISIBLE pair), the
  inactive the #737373 pair, the 16×16 currentColor icons at mr 8.
  The WIDTH family diverges BY CONSTRUCTION: the reference's list is
  432 wide with fractional 211.8px tracks (its /networth page
  overflows to 464 — the documented bug; the list overhangs the 390
  viewport) where the clone's superset fix keeps the page in-bounds
  (the list 358, 175px tracks, pageSW 390) — the same documented
  divergence class as the v47 net-worth-card mobile census.
- The CALCULATOR at 390 (with 1 row): byte-parity on every axis —
  the panel 358 @ x 16/radius 16/maxW 768/maxH 717.4 (85vh)/white/
  overflow hidden/flex + the 2xl VISIBLE layer + the CENTERING
  invariant; the header h 101/pad 16 24/border-b; the chip 32×40 and
  the close 29×36 — the IDENTICAL flex-shrink squish at 390 on BOTH
  sites (the 40×40 chip and the 36×36 close squeeze under the
  header's flex row — byte-shared behavior, pin the squished values);
  the total card 310/#fff7f5/radius 12/pad 16; the row 310/pad 16/
  white/border-t/radius 12; the Add Item button 110×32/12px/500/the
  orange gradient/white; docSW 390. The panel h measured 413 on BOTH
  sites with 1 row — data-dependent, never pinned (the empty state
  reads 555 on the clone; the reference's empty state is unmeasurable
  — emptying its calculator needs WRITES, the deferred class).
- `vlm-shots-v53.sh` + `vlm-compare-v53.mjs` + the /tmp/vlm53 pair —
  the standing VLM screening (the calculator dialog at 390 — THE F2
  SURFACE): the VLM flagged 5 diffs — the close button "boxed X" (the
  probe's synthetic-click focus artifact: the clone's outline:auto
  1px renders only under :focus-visible — the keyboard a11y superset;
  the reference's close is never focused on open and its
  outline-style is none, its own a11y regression; NO ring in real
  mouse flows — the committed 08-calculator.png proves it), the total
  $25.00-vs-$0.00 + the "Based on 1 item"-vs-0 + the row-vs-empty-
  state (the reference's own data class — its Rent carries a
  "Contents Insurance" row; the clone's dev seed carries none), and
  the Base44 FAB (the reference's own platform chrome) — ALL
  DOM-verified, the pair CLEAN per the v43 rule.
- THE v53 EXECUTION LESSONS (the big ones):
  1. **The orphaned :3100 webServer** — a timed-out/killed playwright
     run leaves its `bun .next/standalone/server.js` child ALIVE on
     :3100; the next run REUSES it (`reuseExistingServer: true`) with
     a db handle that went stale under the next global-setup's
     delete-and-re-seed of db/e2e.db — every data-driven assertion
     then times out at the 10s expect gate (the 45-failure cascade).
     The discipline: `ss -tlnp | grep ":3100 "` + kill the pid BEFORE
     every full-chain run, and again after any killed run.
  2. **restoreRent after every calculator add/delete e2e** — the
     line-item mutations recalculate the parent item's amount
     SERVER-SIDE (the calculator rule); a test that adds + deletes a
     row without `restoreRent(page)` leaves Rent ≠ 1850 and poisons
     every later spec's dashboard arithmetic (+$2065.00). The v45 F2b
     test has always done this; a new test must copy the whole
     cleanup, not just the delete.
  3. **The rebuild and the test run as SEPARATE commands** — the
     combined `npm run build … && npx playwright test …` one-liner
     RACED the .next/standalone swap twice this session (two mutation
     runs read "1 passed" against a not-yet-swapped build). When a
     mutation unexpectedly does not bite, probe the SERVED build
     directly (the live-computed-style check) before doubting the
     pin.
  4. **The eval string's closing `()`** — an un-invoked async
     function expression (`})"` instead of `})()"`) submits NOTHING:
     the login silently no-ops and every downstream census reads "no
     card". Grep the driver for `})()"` before running it.
  5. `pkill -f agent-browser` inside a bash -c whose command string
     contains "agent-browser" kills the PARENT script (the -f match
     hits the command line) — use fresh session names instead.

## v54 — the savings goal-card's badge-row + footer internals census (session-128)

The first iteration of the session-125 v54 queue: the savings view's
GOAL-CARD INTERNALS at 390 — the badge chip row + the date/payment
footer — the internals BEYOND the v51 F3 chrome pin. Drivers:
`ref-v54.sh` (READ-ONLY on the reference) + `clone-v54.sh` + the VLM
pair `vlm-shots-v54.sh` + `clone-vlmshots-v54.sh` +
`vlm-compare-v54.mjs`.

**Result: byte-parity on every chrome axis — PIN-ONLY (the third
consecutive pin-only iteration).** The reference's own Emergency Fund
goal (need-classified, 3 chips, no payment method) vs the clone's dev
seed's Emergency Fund (savings-classified, 4 chips incl. Recurring,
Bank Account payment) — the chip COUNT, the row HEIGHT (22 vs 52, the
wrap), and the payment span are DATA classes; the chip + footer CHROME
is byte-identical, with the "monthly" chip measuring w 78 and the
"active" chip w 63 on BOTH sites (the same text at the same chrome
renders the same width — the strongest byte-parity signal a census can
produce).

The v54 lessons:

1. **A generic justify-between + svg footer finder matches the card's
   HEADER row first** — the header row (`flex items-start
   justify-between mb-3`) also carries justify-between and its own
   kebab svg. The first census run read the header's 16px/48px
   geometry as the "footer" and the empty kebab button as the
   "payment span" (the fs-16/h-48 signature is the tell-tale of the
   wrong row). The correct locator: **the LAST justify-between direct
   child WITHOUT an h4**.
2. **The chips' `inline-flex` SOURCE class computes to "flex"** — the
   chips are children of the flex badge row, and flex items are
   blockified per the CSS spec (`inline-flex` → `flex`). A census
   finder checking `display === "inline-flex"` finds nothing; accept
   "flex" (the probe's OR-clause existed for exactly this reason).
3. **The fresh-clone environment needs `npx playwright install
   chromium`** — the headless-shell binary is per-Playwright-version
   (1243 this session; the cache carried 1200/1248 from other
   Playwright installs). The first a11y run failed 21-wide on
   `browserType.launch: Executable doesn't exist` before the install.
4. **The reference session EXPIRES between long eval gaps** — the
   mid-verification census landed on the login page ("Welcome to
   ZeroBudge" + docSW 390 at a logged-in route is the signature);
   re-login via the same eval before any follow-up census.

## v55 — the goal-card icon-glyph census + the FULL glyph audit + the legacy-icon swap (session-131)

The session-128 v55 queue's read-only member (the goal-card's
classification-icon glyph census — the v44 glyph-swap family's
badge-row application), extended to a FULL icon-glyph audit that found
the fifth production-code change since v46. The drivers:

- `ref-v55.sh` + `clone-v55.sh` — the goal-card glyph census at 390
  (the classification chip's icon svg: class/viewBox/stroke
  family/shape children/12×12/mr 4/the chip color) + the
  `/expenses` same-glyph CONTROL census (every card's classification
  chip matched by text — the reference's Investments/Netflix/Rent vs
  the clone's Entertainment/Groceries/Rent).
- `piggy-sweep-v55.sh` — the reference's EVERY piggy-bank svg across
  the five views (the scope sweep that found all six surfaces: the
  nav rail link, the quick-action tile, the stat row, the donut
  legend, the savings hero, the classification chip — all carrying
  the OLD 3-path glyph).
- `glyph-audit-v55.sh` — the FULL per-view lucide glyph dictionary
  (every `svg[class*=lucide-]` on the five views + the login page;
  the name → shape-dump map, one entry per glyph). Accepts
  BASE/SESSION/SIDE args (the ref side logs in with the reference
  credentials, the clone side with the demo seed's).
- `glyph-exact-v55.sh` — the exact-svg-markup capture (the
  outerHTML of the four drifted glyphs — the byte source for
  `src/components/ui/legacy-icons.tsx`).
- `glyph-diff-v55.mjs` — the dictionary diff (IDENTICAL / DRIFTED /
  ONE-SIDE-ONLY per glyph, the shapes normalized by segment sort).
- The VLM trio: `vlm-shots-v55.sh` + `clone-vlmshots-v55.sh` +
  `vlm-compare-v55.mjs` (the calculator dialog's with-row state —
  the v53 F2 surface — + the savings goal card post-swap) +
  `vlm-arbit-v55.sh` (the DOM arbitration of the VLM's flags).

The verdict: 24 shared glyphs — 19 byte-identical, 4 DRIFTED
(piggy-bank, trending-up, search, mail — lucide-react 0.525
redesigned them since the reference's lucide version), 1 clone-only
(repeat — the Recurring superset badge). The fix:
`src/components/ui/legacy-icons.tsx` + the eight import swaps, pinned
by `tests/e2e/glyph-parity.spec.ts` (the shape-data census).

**The v55 probe lessons:**

1. **A path-only glyph census reads ZERO paths on circle-alert** —
   the lucide glyphs render `<circle>` (circle-alert's ring),
   `<rect>` (the calendar's box, the mail's envelope), and
   `<polyline>` (the reference's trending-up) children, not just
   paths. The shape dump must walk EVERY shape tag
   (path/circle/rect/line/polyline/polygon) and read `points` (not
   x1/y1, which polylines don't carry) for polyline/polygon.
2. **The glyph audit's login can RACE the page mount** — "no
   inputs" is the RETRY signal (a fresh profile's /login can still
   be mounting at 3s), NOT auth state; and the auth state needs an
   explicit post-login check before the census loop (the first
   sweep censused the LOGIN PAGE six times — every view's
   dictionary was mail+lock because the unauthenticated visits all
   redirect to /login).
3. **agent-browser eval output is a JSON-encoded string** — the
   eval's return value arrives quoted and escaped; unwrap it
   (twice if doubly-encoded) before parsing dictionaries.
4. **The reference's calculator X-close finder differs per site** —
   the reference's dialog layer matches `fixed inset-0` + "Total
   Calculated", the clone's is a Radix `[role=dialog]` containing
   it; the VLM arbitration probe takes the site into account.

## v56 — the desktop 1280 VLM pair + the glyph-swap hold re-audit + the hero-desk census (session-134)

The session-131 v56 queue's own standing-check suggestion — a fresh
VLM pair on the v55 F1 surfaces' desktop 1280 state — extended with
the full glyph re-audit (does the v55 swap still hold?) and the 50th
standing checks. PIN-ONLY iteration: no production-code change, the
v56 deliverable is the hero-card DESKTOP 1280 census pin.

- `glyph-audit-v56.sh` — the full per-view lucide glyph dictionary
  re-census (both sites; the v55 audit's shape dump with the
  polyline/rect-rx capture fix applied). Verdict: 24 shared glyph
  names, 0 DIFFS among the shared set — the v55 legacy-icon swap
  HOLDS byte-identical; no new drift.
- `vlm-shots-v56.sh` + `clone-vlmshots-v56.sh` +
  `vlm-compare-v56.mjs` — the desktop 1280x800 VLM pair: PAIR 1 the
  dashboard (the stat rows + donut + legend post-swap), PAIR 2 the
  networth view (the trending-up hero/summary). PAIR 2 VERDICT
  IDENTICAL; PAIR 1 flagged 4.
- `vlm-arbit-v56.sh` + `clone-arbit-v56.sh` — the PAIR 1 flags'
  DOM arbitration (the v43 rule): the nav highlight = the
  documented root-URL active-nav gap (the reference shows no
  highlight at `/` — computed transparent/none/zinc-700/400 — while
  the clone highlights; the NON-ROOT control at /networth renders
  the byte-identical 135deg forest-gradient active style on BOTH
  sites); the progress bar = the track byte-identical 568x12
  rgba(255,255,255,0.1) on both sites with the fill's width =
  pct x 568 per each site's own data (the reference 173 = 30.5% x
  568; the clone 357 = 62.8% x 568); the avatar the user-identity
  class; the FAB the Base44 platform chrome. The pair CLEAN.
- `hero-desk-v56.sh` — the hero-card census at 1280x800 on both
  sites (the v56 pin's measurement source, byte-identical): the
  hero grid `304px 304px 304px` + 24px gap + the [632x364, 304x364]
  children at y 136; the goal card 632x316/radius 16/pad 32/135deg
  forest gradient + the 26-58-46/0.3 shadow; the 568x12 track; the
  fill's 90deg orange status gradient + radius 9999px; the 48px
  stat tiles' 24x24 svgs.
- `standing-checks-v50.sh` + `ref-standing-v50.sh` — the 50th
  standing checks (the v49 scripts with fresh session names): the
  reference's four bugs all live, the clone's mobile nav verified
  working (R1 burger hit + sheet, R2 close-on-nav, R3 landmark, R4
  zero overflow at 390 on all five views), the data census intact,
  the SEO pair live.

### v56 probe lessons

1. **Branch the glyph census's shape dump per tag** — the v55
   audit's generic fallback read polylines via x1/y1 (empty) and
   dropped the rects' rx; glyph-audit-v56.sh branches
   path/circle/rect(rx)/polyline(points)/polygon(points) per tag
   (the v55 lesson applied at the source).
2. **The reference has no `<nav>` landmark** (its own documented
   bug) — nav probes must scan ALL anchors
   (`document.querySelectorAll("a")`), not nav-scoped selectors;
   a nav-scoped probe reads "no link" on every view.
3. **Split long clone-side shot scripts into per-view
   invocations** — the combined login+2-shots script can exceed the
   240s Bash timeout when the agent-browser daemon was reset
   between steps (the with-server boot + the fresh session open
   serialize); login+shot, then the second shot, runs in well
   under half.
4. **The sed mutation discipline: match the SOURCE's exact
   formatting** — a mutation pattern written from a display
   rendering (spaces in `rgba(255, 255, 255, 0.1)`) can silently
   no-op against the source's own spacing
   (`rgba(255,255,255,0.1)`); always re-read the line post-sed
   before rebuilding, and prefer line-addressed class-token
   mutations over full-attribute patterns.

## v57 — the items-view desktop 1280 VLM pair + the item-card footer/badge census + the G7 flake fix (session-134/136)

The session-134 v57 queue's own standing-check suggestion — a fresh VLM
pair on the ITEMS view's desktop 1280 state (the v56 pair covered the
dashboard + networth; the items views remained). The pair CLEAN (every
flag DOM-arbitrated to the documented data classes); the v57 deliverable
is the item-card footer + badge-row census pin (+2 e2e) and the
not-found G7 flake fix (test-only).

- `vlm-shots-v57.sh` + `clone-vlmshots-v57.sh` +
  `vlm-compare-v57.mjs` — the desktop 1280x800 VLM pair: PAIR 1 the
  income view (the v55 search-glyph surface + the item-card grid),
  PAIR 2 the expenses view. Every flag data-class (the avatar, the
  seed data, the payment chips, the badge wrap).
- `vlm-arbit-v57.sh` — the DOM arbitration + the reference-side
  census (the grid template 309.328px ×3 / 16px gap / 960 wide; the
  footer chrome byte-identical; the card chrome byte-identical) on
  both views.
- `badge-census-ref-v57.sh` + `badge-census-clone-v57.sh` — the
  badge-row chrome census (flex/wrap/8px/mb 12px; every badge
  flex/center/6px/2px 10px/12px/600/h 22/12×12 icons — byte-identical
  on both sites; the Recurring superset chip's wrap is the data class).
- `ref-standing-v51.sh` + `standing-checks-v51.sh` — the 51st standing
  checks (the mobile-nav R1–R4 + the data census + the SEO pair, both
  sides).

### v57 probe lessons

1. The badge-row finder walks the card's DIRECT children (the row is
   a direct child of the card, class flex flex-wrap gap-2 mb-3 — a
   nested querySelectorAll filter can miss it or match the wrong row).
2. The clone-side with-server heredoc must be QUOTED (<<'EOF') when
   the inner script references a $-expanded census variable — an
   unquoted heredoc re-parses the JS's double quotes through the
   inner bash and strips them (badge-census-clone-v57.sh's census
   lines came back empty; the debug variant
   badge-census-clone-v57-debug.sh carries the fix).
3. The reference's expenses items carry NO payment methods — its
   expense-card footers render one child (the date alone) while its
   income card carries two (the date + "Bank Account"): the
   conditional render is the parity contract, not a drift.

## v58 — the savings-view desktop 1280 VLM pair + the savings goal-card census (session-137)

The session-137 v58 queue's own first suggestion — the items family's
remaining view (the v57 pair covered income + expenses; the savings
goal-card's 1280 state was unpinned at the pair viewport, its internals
pinned at 390 only [v54 F1]). The pair came back CLEAN after DOM
arbitration (every flag a documented data class — the seed data, the
conditional payment footer, the classification VALUE + the badge count)
— the v58 deliverable is the PIN (`tests/e2e/items.spec.ts`, +1 → 258).

- `vlm-shots-v58.sh` + `clone-vlmshots-v58.sh` +
  `vlm-compare-v58.mjs` — the savings view's desktop 1280x800 VLM pair
  (the reference's login-retry loop + the clone's with-server boot).
- `savings-census-ref-v58.sh` + `savings-census-clone-v58.sh` — the
  DOM arbitration + the full census (the grid template + the card
  chrome + the footer's two-children conditional render + the badge
  row + every badge's geometry), both sides — the clone script
  carries the P1.2 quoted-heredoc fix by construction (the census
  variable is EXPORTED, the with-server heredoc is QUOTED).
- `ref-standing-v52.sh` + `standing-checks-v52.sh` — the 52nd standing
  checks (the mobile-nav R1–R4 + the data census + the SEO pair, both
  sides).

### v58 probe lessons

1. A comment apostrophe inside a single-quoted shell census variable
   terminates the quote — `bash -n` before every run
   (savings-census-ref-v58.sh's first run failed with "DIRECT:
   command not found" from the comment `the card's DIRECT child`).
2. The reference's savings item is classified NEED (the red family:
   bg rgb(254,242,242) + the 1px rgb(254,202,202) border) while the
   clone's are SAVINGS (green) — the classification VALUE is the data
   class; the color maps stay locked by badge-colors.spec.ts. Its
   savings footer renders the ONE-child date-only form (its item
   carries no paymentMethod) — the v57 conditional-footer contract
   measured on the third view.
3. The e2e-chunk filter regex lesson (a test-infra trap, not a probe):
   the Playwright file-filter alternation must match the FULL filename
   stem — an `auth\.spec` stem plus the shared `\.spec\.ts` suffix
   outside the group double-matches (`auth.spec.spec.ts`) and silently
   drops auth.spec.ts / calculator-error.spec.ts / networth-error.spec
   .ts from the run; stems-only alternations (`badge` for
   badge-colors) fail the same way on the suffix side.

## v59 — the calculator-view desktop 1280 VLM pair + the panel/total-card census + the login 1280 pair (session-141)

The session-139 v59 queue's first TWO items: the CALCULATOR dialog's
desktop 1280x800 pair (the panel + row surfaces — the v45 F2a pin
covered the panelW + row census at 1280, the v49 F3 panel chrome at 640
only, the total card at 390 only [v53 F2]) and the LOGIN view's 1280
pair (the v55 glyph pin's surface, no pair at 1280 yet) — plus the 53rd
standing checks.

**The calculator pair** (`vlm-shots-v59.sh` + `clone-vlmshots-v59.sh` +
`vlm-compare-v59.mjs`): the reference's own Rent calculator (its Rent
$25.00 carries ONE "Contents Insurance" $25.00 monthly-active line
item — its own data) vs the clone's (the SAME line item added through
the real UI for the pair, then FULLY restored: delete + the $1850
edit-flow restore + the "3 items · $2235.00" page total verified).
Both VLM flags DOM-arbitrated (`calc-census-ref-v59.sh` +
`calc-census-clone-v59.sh`, the v43 rule):

1. the total card's "• Will update category total" span —
   DATA-CONDITIONAL: the lineTotal-vs-parentAmount-at-open contract
   (the reference's $25 === $25 → hidden; the clone's $25 !== $1850 →
   shown; the conditional itself is the pinned contract);
2. the row's hover-action pair — POINTER-POSITION artifact: both sites
   gate the pair at opacity 0 at rest (the census: opacity 0 / 2
   buttons / btnW 32, both sides); the reference's shot caught them
   mid-hover (its pointer rested inside the dialog after the click).

The census, byte-identical on every axis: the panel 768×393 @ (256,
204) — the centering invariant round((800−393)/2) — radius 16 / maxW
768px / maxH 680px (85vh of the 800 viewport; the v49 F3's 816px was
the 960 viewport's) / bg white / overflow hidden / the 2xl VISIBLE
layer; the total card 720×90 / #fff7f5 / radius 12 / pad 16 / border
1px solid rgb(252,221,213); the close 36×36; the header border-b 1px
solid rgb(229,231,227); the row 720 / pad 16 / radius 12 / border /
transition all 0.15s (the v45 F2a values).

**The login pair** (`login-shots-v59.sh` + `clone-login-shots-v59.sh`):
IDENTICAL — the only flag the reference's "Edit with Base44" platform
badge. The census matches exactly: title "ZeroBudget" / h1 "Welcome to
ZeroBudget" / the email+password inputs (the same placeholders) / the
Sign-in button 368×48.

**The pin** (`tests/e2e/calculator.spec.ts`, the "calculator panel
census at 1280" describe, +1 → 259): the read-only open state — the
panel chrome + the centering invariant + the 36×36 close + the header
border-b + the total card (the v53 F2 chrome at the 1280 viewport) +
the panelW 768 control. THREE pin-sanity mutations verified to FAIL
then restored: the total card bg #fff7f5→#fff8f0, the panel maxWidth
48rem→42rem (768→672), the total card p-4→p-5 (16px→20px).

### v59 probe lessons

1. `agent-browser mouse click` DOES NOT EXIST in 0.39.0 — the low-level
   pair is `mouse down` + `mouse up` after a `mouse move` (valid mouse
   subcommands: move, down, up, wheel). The failure mode of using the
   nonexistent subcommand (its error swallowed by >/dev/null): the
   pointer stays wherever it was — over the CARD BODY — and the
   down/up click OPENS THE ITEM DETAILS dialog instead of the
   calculator: a false-failure signature to recognize on sight.
2. The eval output is a JSON-encoded STRING — `"443,550"` — and
   `cut -d,` on it yields `"443` (a leading quote) which silently
   breaks `mouse move`. Strip the quotes FIRST with bash parameter
   expansion: `POS=${POS//\"/}`.
3. The reference's dialogs are PLAIN fixed divs (no role=dialog — the
   documented reference class): the reference-side dialog census must
   find the panel by GEOMETRY (e.g. `getComputedStyle(d).maxWidth ===
   '768px'` or the fixed-overlay width filter), never by
   `[role=dialog]`. The clone's Radix dialogs DO carry the role.
4. The reference's session EXPIRES between long eval gaps (the carried
   v58 lesson, re-confirmed twice): re-login via the same eval before
   any follow-up census, or the eval reads the /login redirect.
5. The reference's /expenses data census (documented for future
   calculator pairs): "4 items · $525.00" — Miscellaneous $0.00 (need)
   / Investments $300.00 (savings) / Netflix $200.00 (want, Streaming)
   / Rent $25.00 (need, Apartment); its Rent carries ONE line item
   ("Contents Insurance" $25.00 monthly active).
6. The screenshot SEED-DATE class (a capture-infra lesson): the seed's
   `isoDate(-N)` anchors the item dates to the SEED-RUN date, so a
   fresh checkout seeded N days after the last capture regenerates
   date-bearing screenshots with drifted date text (7 of 16 diffed;
   VLM-arbitrated DATE-TEXT-only, zero layout diffs). The e2e DB
   re-seeds EVERY RUN (global-setup) so the suite is date-independent;
   only docs/screenshots carry the class. Future pin-only sessions
   that re-seed on a later date should expect the 7-file diff, not
   byte-identity, and arbitrate it as this class.

## v60 — the networth-view desktop 1280 VLM pair + the dashboard drill-down EXPANDED-state pair (session-144)

The session-141 v60 queue's first TWO items — the NETWORTH view's
DEDICATED desktop 1280x800 standing pair (the standing-pair program's
remaining major view; the v56 PAIR 2 was the glyph-swap audit pass, not
a dedicated pair) and the DASHBOARD's drill-down EXPANDED surfaces at
1280 (the first VLM pair over the expanded drill-down; the v43 F3
family pinned the sub/item rows at 640, the v44 F2b the section/
category/footer heights at 1280) — plus the 54th standing checks (the
expenses census now IN the standing script). PIN-ONLY iteration: no
production-code change, the v60 deliverables are the TWO pins (+2 →
261).

- `vlm-shots-v60.sh` + `clone-vlmshots-v60.sh` +
  `vlm-compare-v60.mjs` — the FULL-PAGE (--full) desktop 1280x800
  pairs: PAIR 1 the networth view (the below-the-fold card grids
  captured whole), PAIR 2 the dashboard with the drill-down EXPANDED
  (the Total Income section + its first category — VIEW-STATE clicks
  only, no data mutation). PAIR 1 VERDICT IDENTICAL (zero layout/style
  flags; every difference the expected data class — the figures, the
  groups, the ratio "∞:1" vs "0.21:1"); PAIR 2 flagged FIVE.
- `drill-arbit-ref-v60.sh` + `drill-arbit-clone-v60.sh` — the PAIR 2
  flags' DOM arbitration (the v43 rule): the nav highlight = the
  documented root-URL active-nav gap (the reference transparent/
  zinc-700/400 at `/`, the clone white/500 + the gradient — superset
  contrast #3); the avatar = the user-identity class ("U" vs "D"); the
  Base44 tooltip = the platform-chrome class; the hero progress fill
  30.5% vs 62.8% = the pct × 568 data class (the track byte-identical
  568×12 rgba(255,255,255,0.1), the fill each site's own pct — the
  v56 arbitration); the donut percentage labels = a PERCEPTION
  ARTIFACT — the reference DOES render them (count 3 individual
  texts "92.3%"/"4.6%"/"3.1%", labelLineCount 0, 16px, fill black —
  the v9 G1b measurement re-confirmed live; the clone byte-identical
  chrome: "81.6%"/"13.8%"/"4.6%", labelLineCount 0, 16px, black).
  The pair CLEAN.
- `nw-census-ref-v60.sh` + `nw-census-clone-v60.sh` — the networth DOM
  arbitration + the F1 pin's measurement source (both sides):
  byte-identical on every axis — the summary card 960/32px/16px/the
  135deg forest→lime gradient/the rgba(26,58,46,0.3) 0px 20px 60px
  shadow; the figure 48px/700/white; the label 14px/0.8-white; the
  medallion 64×64 white-20% + the 32px svg; the stat grid 440px
  440px gap 16; the tile 440/16px/12px/white-10%/blur(10px)/the
  amount 24px-700; the ratio value 18px/700 (the text the data
  class: "∞:1" vs "0.21:1"); the tablist 448/36/"220px 220px" (the
  v50 F2 values at the pair viewport); the group header
  18px/600/rgb(45,90,74)/mb 12/capitalize; the grid 960/3×309.328/
  gap 16; the card 309/20px/12px/1px solid rgb(229,231,227)/the
  rgba(0,0,0,0.04) 0px 2px 8px rest shadow/the dot 8×
  rgb(143,188,63). The divergences both documented classes: the
  summary mb (the reference computes 0 — its 32px card→tablist GAP
  lives on another element; the GEOMETRY is the contract, the DOM
  shape is not [the v45 lesson]) + the clone's break-words figure
  guard (the D-5 superset).
- `drill-census-ref-v60.sh` + `drill-census-clone-v60.sh` — the
  drill-down EXPANDED census (both sides): byte-identical on every
  axis — the card 304; collapsed 364 BOTH (the v44 F2b start); the
  section {56, 8px, -8px, 8px, pointer, labelH 40}; the category
  {28, "6px 12px", 8px, rgb(249,250,251), 12px/500/rgb(26,58,46)};
  the sub {24, "4px 8px", rgb(250,250,250), 12px/400/
  rgb(107,114,128)}; the item {24, "4px 8px", 12px,
  rgb(156,163,175), maxW 120px, ellipsis}; the footer {29, "6px
  12px", 1px, 12px/600}; the heights 364→445→499 (reference, its one
  Salary category) vs 364→481→535 (clone, the seed's two categories)
  = the DATA class.
- `drill-itemdump-ref-v60.sh` — the ONE census-axis false alarm's
  evidence: the reference-side census's rows[last] caught the item
  row's INNER label-group div (flex items-center gap-1.5, h 16, pad
  0, also carrying a maxW-120/ellipsis span) — the reference's REAL
  item row (flex items-center justify-between py-1 px-2, h 24, pad
  "4px 8px") is byte-identical to the clone's. The v60 pin's finder
  pins the REAL rows by their chrome (justify-between + pad
  "4px 8px"), never by array position.
- `ref-standing-v54.sh` + `standing-checks-v54.sh` — the 54th
  standing checks (the v53 scripts + the expenses census added to the
  reference side): the four bugs ALL live (toast-blocker
  hitIsBurgerChild:false, the sheet-trap overlayCount:1, the
  no-landmark, the 464 /networth overflow), the data census intact
  ("1 items · $25,000" / "1 items · $5000.00" / "4 items · $525.00"),
  the SEO pair live; the clone R1-R4 all green (the mobile menu
  VERIFIED WORKING — the 54th time).
- `vlm-shotsdiff-v60.mjs` — the v60 screenshot-regeneration
  arbitration: 15 of 16 byte-identical + ONE diff
  (07-add-item-modal.png) arbitrated as the DATE class — the modal's
  Date input defaults to the CAPTURE-run day (10/14/2026 →
  10/15/2026), DATE-TEXT-only, zero layout diffs. The seed-date
  family's dialog-default extension: the seed's item dates anchor to
  the SEED-run date (v59 lesson 6) while a dialog's default-today
  input anchors to the CAPTURE-run date — an un-re-seeded db can
  still produce ONE date-class screenshot diff.

### v60 probe lessons

1. **A single-quoted bash CENSUS string must contain NO single
   quotes.** The JS selectors like `'[role="tablist"]'` TERMINATE the
   bash string mid-assignment — the script's eval then silently
   returns EMPTY (the failure signature: a blank line between the
   === markers; `bash -n` does NOT catch it because the mangled
   assignment is still valid bash). Use escaped double-quoted JS
   strings inside the single-quoted wrapper
   (`"[role=\"tablist\"]"`) or a quoted heredoc. The same trap bites
   the clone-side single-quoted eval inside a `<<'EOF'` heredoc.
2. **The FULL-PAGE screenshot (`agent-browser screenshot --full`) is
   the pair-shot mode for views taller than the 800 viewport** — the
   networth view's card grids and the dashboard's expanded drill-down
   extend below the fold; the v56-v59 pairs were viewport shots of
   surfaces that fit. The parked-pointer discipline applies the same
   way (`mouse move 5 5` before the shot).
3. **The drill-down expansion clicks are VIEW-STATE toggles** — safe
   under the v46 read-only rule (no data mutation; the reference's
   own Salary category expanded and collapsed cleanly).
4. **The recharts label census must filter the individual `<text>`
   labels from the group wrapper** — the `[class*=recharts-pie-label]`
   selector matches the group g (whose textContent concatenates all
   labels) plus the individual texts (count 4 = 1 group + 3 labels);
   the arbitration axes are the individual count, the labelLineCount
   (0 — the v9 G1b contract), the fontSize and the fill.
5. **Census row-finders must pin rows by their CHROME (pad /
   justify-between), never by array position** — the reference's
   drill-down sub-area contains the rows' INNER label-group divs
   (flex gap-1.5, h 16, pad 0, carrying maxW-120 spans) that a
   rows[last] finder catches instead of the REAL item row. The
   dump-then-pin pattern (drill-itemdump) is the arbitration
   instrument.

## v61 — the Budget Guidelines STRETCH fix + the quick-action row + the
## guidelines chrome 1280 censuses (session 96)

The family: `vlm-shots-v61.sh` + `clone-vlmshots-v61.sh` +
`vlm-compare-v61.mjs` (the dashboard FULL-PAGE 1280x800 pair — both v61
surfaces live below the fold), `qa-census-ref-v61.sh` +
`qa-census-clone-v61.sh` (the guidelines + quick-action DOM census, both
sides, the cross-row gap included), `vlm-glcol-v61.mjs` (the
guidelines-column REGION-CROP arbitration),
`ref-standing-v55.sh` + `standing-checks-v55.sh` (the 55th standing
checks).

The session's finding: the VLM pair called the dashboard IDENTICAL, but
the DOM census caught the **Budget Guidelines card's STRETCH divergence**
— the reference's card sits at NATURAL height (348) inside a stretched
`space-y-4` wrapper (the grid child; the row 656 under the seed), while
the pre-v61 clone's card itself stretched to 656 with ~308px of empty
white card body below the Savings tile. Arbitrated three ways (the
census both sides; the region-crop re-arbitration — DIFFERENT pre-fix /
SAME post-fix; the reference's own row DOM). The fix mirrors the
reference's DOM; TDD: the pin RED (cardH 656) → the fix → GREEN.

Lessons (v61):

1. **The heading leaf is a DIV — `.closest("div")` returns the heading
   ITSELF** (closest checks self first). Use `.parentElement` for the
   wrapper. The failure mode: the census reads the heading's own padding
   (0px) as the header wrapper's, then the body lookup walks off the
   card and `getComputedStyle(null)` throws — the empty-eval signature.
2. **Census finders must pin the LEAF span (the exact text + zero
   element children)** — a bare textContent match catches ancestor
   wrappers: the clone's quick-action row wrapper SPAN carries the
   label's textContent (fw 400 / rgb(10,10,10) — the inherited body
   chrome) and sorts before the label in document order; the reference's
   row is a DIV so the first census pass read the label correctly by
   accident. The tag asymmetry is itself the DOM-shape class (the
   GEOMETRY is the contract, the DOM shape is not).
3. **The icon tile is a DIV on the reference but a SPAN on the clone** —
   match BOTH tags by chrome (radius + the 30-60px box), never by tag.
4. **The REGION-CROP arbitration pattern** — when a full-page VLM pair
   calls a flagged-or-not surface IDENTICAL but the DOM census diverges,
   crop BOTH screenshots to the surface's region (sharp extract) and
   re-arbitrate the crops with the VLM. The full-page scale hides
   below-the-fold geometry; the crop isolates it.
5. **A grid-child STRETCH divergence can hide inside an IDENTICAL
   full-page VLM verdict** — the stretched card differs from the compact
   card only by empty space BELOW the content (the tiles all
   byte-identical), a low-salience difference at page scale. The DOM
   census (the card height vs the row height) is the authority; the VLM
   is a screening layer (lesson 37).
6. **The content column at 1280 is 960** (1280 − 256 sidebar − 64 p-8
   padding) — the max-w-7xl cap never bites on this stack; the grid
   templates derive from it (3×304 + 2×24 gaps = 960; 2×468 + 24 =
   960).

## v62 — the reference-side a11y re-audit + the TWO-pair VLM program
(desktop + the NEW mobile 390 twin) + the mobile header-subtitle pin
(session-150)

The session-147 v62 queue's first TWO items (the a11y re-audit deferred
from v61 + the SKILL doc's stale count lines), the 56th standing
checks, and the standing VLM program's mobile extension.

1. **axe-detail-ref-v62.mjs** — the reference-side a11y re-audit, the
   full a11y.spec.ts surface (six authed routes at 1280 + the 404 + the
   logged-out login + the mobile 390 sheet-open state). VERDICT: **NO
   DRIFT since v38** — the login zero-violation, the structural
   families still exactly `button-name` (10) + `svg-img-alt` (6), the
   contrast palette still exactly the 7-color v38 set. The clone's
   a11y.spec.ts contract stays valid as pinned; no code change.
2. **vlm-shots-v62.sh / clone-vlmshots-v62.sh / vlm-compare-v62.mjs** —
   the TWO-pair VLM program: the dashboard full-page at 1280x800 (the
   standing pair) AND at 390x844 (the NEW mobile twin — the standing
   checks verify mobile functionally; this pair adds the visual
   confirmation). Every flag on both pairs DOM-arbitrated to documented
   classes — the desktop pair: nav-highlight gap / avatar / allocation
   data / donut-labels perception artifact / Base44 FAB; the mobile
   pair: Base44 tooltip + the "subtitle third line" PERCEPTION
   ARTIFACT.
3. **arbit-v62.sh / arbit2-v62.sh** — the two unclassified flags'
   arbitrations: the donut labels (the reference renders its three:
   92.3 / 4.6 / 3.1 — the clone its own 81.6 / 13.8 / 4.6) and the
   mobile subtitle (the leaf-text census, both sides byte-identical:
   h 48, 2 lines, 16px/400/rgb(107,114,128), lh 24px, block h 92, top
   121 — the 5px width delta is the reference's own 395px docSW
   overflow).
4. **vlm-shotsdiff-v62.mjs + arbit-calc-v62.mjs** — the screenshot
   regeneration arbitration: 6 of 16 diff, 5 the SEED-DATE class (the
   dev DB re-seeded this session — each date +1 day) + 1 the
   sub-perceptual AA-timing class (08-calculator: 1,596px in a 57×73
   bbox; the full-shot AND the 3×-upscaled region crop both VLM
   IDENTICAL).
5. **ref-standing-v56.sh / standing-checks-v56.sh** — the 56th round
   (version bumps of the v55 scripts; the mobile menu verified working
   the 56th consecutive time; the reference's four bugs ALL live).

**The v62 lessons:**
1. The fresh-sandbox caveat — the Playwright browsers must be installed
   (`npx playwright install chromium`) before the first e2e run; a
   "browserType.launch: Executable doesn't exist" failure signature on
   EVERY test is this, not a code regression.
2. The text-range `getClientRects()` heights are GLYPH boxes (~19px
   for a 16px font — the font-metric content height), NOT the 24px
   line boxes: a wrap-rhythm pin must assert the DELTA between
   consecutive line tops (= the line-height) + the element's total
   height — never the individual rect heights.
3. A pin's expected geometry must come from the PROBE's measured
   values, never from derived arithmetic (the v62 block-top miss:
   block top = P top 121 − h1 36 − mb-2 8 = 77, not the assumed 68).
4. The v61 meta-lesson's INVERSE case: the DOM census can ACQUIT what
   the VLM convicts (the mobile pair's "third line" flag — the census
   showed both sides identical; the perception artifact class).
5. The mobile full-page pair (390x844) joins the standing VLM program
   — the desktop pair alone can miss mobile-only reflow divergences.

## v63 — the /networth mobile 390 full-page pair (the matrix COMPLETED) +
the stat-tile family pin + the axe-core version-drift re-check
(session-153)

The session-149/151 v63 queue's two items (the standing-pair program's
last un-paired viewport × view combination + the axe toolchain drift
watch) and the 57th standing checks.

1. **vlm-shots-v63.sh / clone-vlmshots-v63.sh / vlm-compare-v63.mjs** —
   the /networth view full-page at 390x844, the LAST un-paired
   viewport × view combination. With it the pair matrix is COMPLETE:
   {dashboard, items (income/expenses), savings, calculator, networth}
   × {1280 desktop, 390 mobile}. VERDICT: DIFFERENT with three flags,
   every one DOM-arbitrated to a documented class — the pair is CLEAN.
2. **arbit-v63.sh** — the three-flag DOM arbitration census (both
   sides, 390x844): the stat-tile stacking = the v41 mobile-superset
   class (the reference's 432-wide card in its own 464 overflow → its
   fixed 2-col grid, tiles 176×84; the clone's 358-fit card → 1-col,
   tiles 294×84); the card height = the arithmetic consequence
   (333 + 84 + 16 = 421); the trend-icon "larger" = a PERCEPTION
   ARTIFACT of the v54 clipping class (the medallion 64×64 + the icon
   32×32 BYTE-IDENTICAL both sides; the reference's medallion clips
   the 390 viewport at right 416 — `clipsViewport:true` — while the
   clone's fits at 342).
3. **The axe-core version-drift re-check** (the npm/lockfile audit, no
   script needed): **NO DRIFT** — @axe-core/playwright@4.13.0 is still
   npm-latest and its NESTED engine axe-core@4.13.0 is byte-identical
   to the v38/v62 audits; the top-level axe-core@4.14.0 belongs to
   eslint-plugin-jsx-a11y (lint-time static analysis — it never scans
   pages). The next re-check point: a 5.x wrapper release or an engine
   bump inside the wrapper's nested dep.
4. **ref-standing-v57.sh / standing-checks-v57.sh** — the 57th round
   (version bumps of the v56 scripts; the mobile menu verified working
   the 57th consecutive time; the reference's four bugs ALL live; the
   data census unchanged — the 57th clean drift check).
5. **The v63 pin** (tests/e2e/networth.spec.ts) — the stat-tile family
   census at 390: the stat grid {cols "294px", gap "16px", w 294}, the
   tiles 294×84 with the translucent-blur chrome, the card h 421
   stacking arithmetic, the medallion's inner 32×32 icon. Three
   pin-sanity mutations verified to FAIL (the grid gap-4→gap-2, the
   tile p-4→p-2, the medallion svg h-8→h-6).

**The v63 lessons:**
1. The VLM's size judgments on CLIPPED elements are unreliable — a
   byte-identical element partially cut off by its own page's overflow
   reads "smaller" (the trend-icon flag): always read the bounding
   rect AND the viewport-clipping boolean before believing a
   "larger/smaller" verdict.
2. The pair-matrix completion rule — the last un-paired viewport ×
   view combination is never "minor": its three flags needed three
   separate documented classes to arbitrate (the stacking superset,
   the height arithmetic, the clipping artifact).
3. The lockfile can hold TWO axe-core versions at once — the WRAPPER's
   nested engine (what AxeBuilder actually executes) is the one the
   a11y contract names; a top-level copy under a different consumer
   (eslint-plugin-jsx-a11y) never scans pages. Verify the nested dep,
   not `npm ls axe-core`'s first line.


## v64 — the OLDEST desktop pair's fresh standing sweep + the axe-core
5.x wrapper watch + the income filter-card pin (session-155)

The session-153 v64 queue's first two items (the re-run cadence on the
OLDEST desktop pairs — the v57-era items pair re-run — and the axe-core
5.x wrapper watch) and the 58th standing checks.

1. **vlm-shots-v64.sh / clone-vlmshots-v64.sh / vlm-compare-v64.mjs** —
   the items pair (income + expenses) at desktop 1280x800, FULL-PAGE
   both views, the fresh re-run of the OLDEST desktop pair (v57's shots
   predate the v61 dashboard fix and the v62/v63 mobile twins). PAIR 1
   (income): the avatar + the Base44 FAB + the seed data — all
   documented classes. PAIR 2 (expenses): THREE style flags, all
   DOM-arbitrated to documented classes — the footer content (the v57
   DATA-CONDITIONAL class: chrome byte-identical, the reference's
   expense items carry no paymentMethod values), the badge wrap (the
   v57 class: chrome byte-identical, the Recurring superset badge wraps
   h 52 = 22+8+22), the grid population (the seed-count class: the
   axes byte-identical incl. the SAME fractional 309.344px last track).
   **The pair is CLEAN.**
2. **arbit-v64.sh** — the DOM arbitration census (both sides, both
   views at 1280x800): the item grid + first-card chrome + footer
   (per-child spans + icons) + badge row + the FILTER CARD (the never
   -census'd income variant) + the header. The census that arbitrated
   every flag and measured the v64 pin's values.
3. **The axe-core 5.x wrapper watch** (the npm/lockfile audit, no
   script): **NO DRIFT** — @axe-core/playwright@4.13.0 is still
   npm-latest (no 5.x release exists) and its NESTED engine
   axe-core@4.13.0 is byte-identical to the v38/v62/v63 audits; the
   top-level axe-core@4.14.0 still belongs to eslint-plugin-jsx-a11y
   (lint-time only). The next re-check point unchanged.
4. **ref-standing-v58.sh / standing-checks-v58.sh** — the 58th round
   (version bumps of the v57 scripts; the mobile menu verified working
   the 58th consecutive time; the reference's four bugs ALL live; the
   data census unchanged — the 58th clean drift check).
5. **The v64 pin** (tests/e2e/items.spec.ts) — the INCOME view's
   filter-card COMPUTED census at 1280 (the never-census'd sibling of
   the v38 S2 savings pin; the early-era income test pins class strings
   only): the card 960×86, the search 447×36 with the asymmetric 40px
   left pad, the 4-track 215.5px grid with the search spanning 2, the
   two 216×36 comboboxes at 14px. Three pin-sanity mutations verified
   to FAIL (the card p-6→p-4, the search wrapper md:col-span-2 removed,
   the grid gap-4→gap-2).

**The v64 lessons:**
1. A VLM can contradict itself on the SAME platform-chrome element
   between two pairs in one comparison run — the Base44 FAB was
   "missing from the clone" in pair 1 and "present in the clone" in
   pair 2. Platform chrome is excluded from comparisons by rule;
   never arbitrate it, just note the class.
2. The re-run cadence on an OLD pair re-proves the documented data
   classes live — the v57 conditional-footer and badge-wrap contracts
   re-measured byte-identical five iterations later.
3. A never-census'd sibling can hide behind an early-era CLASS-STRING
   pin — the income filter card looked pinned (rounded-2xl /
   md:grid-cols-4 / md:col-span-2 / pl-10 were pinned as class
   strings) but its computed geometry (960×86 / 447×36 / 215.5px
   tracks) was never measured.


## v65 — the OLDEST remaining desktop pair's fresh standing sweep + the
axe-core 5.x wrapper watch + the savings page-header-row pin (session-156)

The session-155 v65 queue's two items (the re-run cadence's other OLDEST
candidate — the v58-era savings pair re-run, the v64 pass having covered
the v57-era items pair — and the axe-core 5.x wrapper watch) and the 59th
standing checks.

1. **vlm-shots-v65.sh / clone-vlmshots-v65.sh / vlm-compare-v65.mjs** —
   the savings pair at desktop 1280x800, FULL-PAGE, the fresh re-run of
   the OLDEST remaining desktop pair (the v58 shots predate the v61
   dashboard fix and the v62/v63 mobile twins). The parked-pointer
   discipline (mouse at 5,5) so no hover-revealed chrome is caught
   mid-flight.
2. **arbit-v65.sh + arbit-v65b.sh** — the DOM arbitration census (both
   sides at 1280x800): the avatar (36x36/radius 9999px/14px-600/white/
   bg rgb(143,188,63) — BYTE-IDENTICAL chrome; only the initial "U" vs
   "D" is the user-identity class), the grid axes (960/16px/3 tracks —
   the seed-count class), the goal-card footer + badge chrome (the v57
   classes re-measured byte-identical), and the never-census'd
   PAGE-HEADER ROW family (the row/chip/icon/h1/subtitle/Add-button
   computed geometry). The v65b pass re-ran with the fixed avatar
   finder (the clone's avatar uses rounded-[9999px], not rounded-full)
   and the FULL Add-button shadow strings. NOTE the census-JS-in-
   unquoted-heredoc rule re-learned: NO dollar sequences in the census
   string (a comment "N items · $X" blew up as "X: unbound variable").
3. **ref-standing-v59.sh / standing-checks-v59.sh** — the 59th standing
   checks (version-bumped from v58). Reference: the four bugs ALL live
   + the data census unchanged (59th clean drift check) + the SEO pair.
   Clone: R1-R4 green — the mobile menu VERIFIED WORKING (59th
   consecutive time), zero overflow at 390 on all five views.
4. **F1 — the axe-core 5.x wrapper watch** — NO DRIFT: npm-latest
   @axe-core/playwright still 4.13.0 (no 5.x exists), the wrapper's
   NESTED engine axe-core@4.13.0 byte-identical to the v38/v62/v63/v64
   audits, the top-level 4.14.0 still eslint-plugin-jsx-a11y's.
5. **The v65 pin** (tests/e2e/items.spec.ts) — the SAVINGS view's
   PAGE-HEADER ROW computed census at 1280: the row flex
   space-between/center/gap 16px/mb 32px/h 60, the chip 48×48 radius
   12px with the savings blue gradient + the white 24×24 icon, the h1
   30px/700/lh 36/forestDark, the subtitle 16px/400/gray-500, the Add
   button 150×36/6px radius/8px 16px pad/14px-500/white with the
   .zb-btn-add visible shadow layers, the 16×16 plus icon. Three
   pin-sanity mutations verified to FAIL (the row mb-8→mb-4, the chip
   h-12 w-12→h-10 w-10, the h1 text-3xl→text-2xl — the last moving the
   ROW height 60→56, proving the text block governs the row height).

**The v65 lessons:**
1. Identical computed colors can read as different hues to a VLM — the
   avatar's "green vs lime" flag dissolved on census (bg rgb(143,188,63)
   on BOTH sides). Always read the computed backgroundColor before
   believing a color flag.
2. The grid's fractional last-track distribution is CONTENT-COUNT-
   CONDITIONAL — the reference's template reads 309.328×3 at one child
   while the clone's reads 309.328/309.328/309.344 at two (the v64
   census measured the same 309.344 tail on both sides at 4-vs-3
   children). Compare the AXES — width, gap, track count — never the
   subpixel tail at differing child counts.
3. A view's header row can hide behind a MID-VIEWPORT stacked-state
   census — the v42 pin covered the 640 dir-column state only; the
   1280 row's computed geometry (the space-between row, the chip, the
   subtitle chrome, the Add button) was never measured.
4. The reference's savings page carries a HIDDEN zero-size h1
   "ZeroBalance" FIRST in its DOM (its own SEO pattern; an 18px/700 h2
   logo in its sidebar) before the VISIBLE 30px/700 h1 —
   querySelector('h1') is ambiguous on the reference; filter by
   non-zero geometry (the v65 first-pass measured the hidden 20px h1
   before the fix).
5. The row-height governor: the h1+subtitle TEXT BLOCK (36+24 = 60)
   sets the header row's height, not the 48px chip — the text-3xl→
   text-2xl mutation moved the row h to 56 while the chip stayed 48.

## v66 — the v59-era pair's fresh standing sweep + the axe-core 5.x
wrapper watch (an upstream 4.14.0 appears) + the calculator dialog's
height-family pin (session-157)

The session-159/160 v66 queue's two items (the re-run cadence rotates to
the v59-era pair — the calculator dialog + login view re-run at 1280, the
oldest remaining after v64/v65 covered the v57/v58 pairs — and the
axe-core 5.x wrapper watch) and the 60th standing checks.

1. **vlm-shots-v66.sh / clone-vlmshots-v66.sh / vlm-compare-v66.mjs** —
   the calculator pair at 1280x800 (the dialog opened on the Rent card;
   the clone half adds the matching "Contents Insurance" $25 monthly-
   active line item through the real UI then FULLY restores the fixture:
   delete + restore Rent's $1850 + verify the "$2235.00" page total).
   The fresh-login warm-up retry: the reference's /expenses first fetch
   can exceed the wait window (a transient "0 items" state) — retry the
   Rent finder on a warm session before the hover.
2. **login-shots-v66.sh / clone-login-shots-v66.sh** — the login pair at
   1280x800 (the logged-out surface; the clone shot against the
   production standalone on :3200).
3. **arbit-v66.sh + arbit-v66b.sh** — the DOM arbitration census (both
   sides at 1280x800, the row-HEIGHT family added): the actions rest at
   opacity 0 on BOTH sides (btnCount 2 each — the pointer-position
   class; the reference's screenshot caught the pair mid-reveal), the
   "• Will update category total" span DATA-CONDITIONAL (the reference's
   natively-$25 Rent hides it, the clone's opened-at $1850 snapshot shows
   it), the panel shadow's two LEADING zero-alpha layers (the Tailwind v4
   computed-form class), and the never-pinned HEIGHT family measured
   BYTE-IDENTICAL: the row 720x102, the name h4 (16px/600/h 24/mb 4px),
   the badge pill row (h 20) + the first pill (20/65/2px 8px/9999px),
   the amount P (h 28), the totalCard h 90. The v66b pass re-ran with
   the fixture add + full restore on the clone side (the quoted-heredoc
   + two-level escaping conventions).
4. **ref-standing-v60.sh / standing-checks-v60.sh** — the 60th standing
   checks (version-bumped from v59). Reference: the four bugs ALL live +
   the data census unchanged (60th clean drift check) + the SEO pair.
   Clone: R1-R4 green — the mobile menu VERIFIED WORKING (60th
   consecutive time), zero overflow at 390 on all five views.
5. **F1 — the axe-core 5.x wrapper watch** — local NO DRIFT (the
   lockfile resolves 4.13.0; the wrapper's NESTED engine axe-core@4.13.0
   byte-identical to the v38–v65 audits; the top-level 4.14.0 still
   eslint-plugin-jsx-a11y's — lint-time only) — BUT the npm registry now
   carries @axe-core/playwright@4.14.0 (a MINOR bump inside 4.x, NOT the
   guarded 5.x). Recorded as the candidate for a future DEDICATED
   upgrade iteration; the next re-check point unchanged.
6. **The v66 pin** (tests/e2e/calculator.spec.ts) — the calculator
   dialog's HEIGHT-family computed census at 1280 (a new describe after
   the v59 panel-census block, riding the add-then-restoreRent fixture
   flow): the row 720x102/pad 16/radius 12/border rgb(229,231,227)/bg
   white, the name h4 16/600/forestDark/h 24/mb 4, the pill row
   flex/gap 8/12px/h 20, the first pill 20/65/2px 8px/9999px/12px/400,
   the amount P 20/700/orangeDark/h 28, the totalCard 720x90. Three
   pin-sanity mutations verified to FAIL (the row p-4→p-2 [6 failures —
   the v45/v49/v53/v59 pins + the v66]; the h4 mb-1→mb-2; the totalCard
   p-4→p-2).
7. **The screenshot DATE-class re-arbitration** — the 16-screenshot
   regeneration came out 15 byte-identical + 1 (07-add-item-modal) the
   documented dialog-default DATE class (the v60 class): the calendar
   had rolled past midnight. Pixel-arbitrated this time — a programmatic
   PIL diff localized the change to a 16x22 px region at
   (1552,931)–(1568,953), exactly the date input's day digits
   "15"→"16"; everything else in the 2880x1800 frame byte-stable.

**The v66 lessons:**
1. The VLM's "shorter row" was a perception artifact — the row measured
   720x102 on BOTH sides. Always measure the computed heights before
   believing a proportion claim.
2. The fresh-login first fetch can exceed the wait window — the
   reference's /expenses rendered "0 items · $0.00" transiently before
   the data landed. Retry the finder on a warm session; a "data gone"
   reading on a standing-check surface is usually a cold-session
   artifact, never a drift verdict on its own.
3. The height arithmetic is DETERMINISTIC: 32 (actions) + 4 (mb) + 28
   (amount) + 32 (p-4) + 2 (border) = 102. A pin on the parts makes the
   whole predictable — and a mutation on any part bites the whole.
4. A single-region screenshot diff is better arbitrated by a
   programmatic pixel-diff than a VLM verdict — the bbox and the changed-
   row histogram localize the change to the exact widget, with no
   perception artifacts.
5. The dialog-default DATE class recurs every calendar rollover — the
   capture script's date field (the Add Item dialog's todayIso() default)
   re-renders daily. Expect exactly one 16-pixel-region diff per
   overnight regeneration; the class is documented, never a regression.

## v67 — the v60-era pair's fresh standing sweep + the axe-core 5.x
wrapper watch (the upgrade DECISION: v68 = the dedicated upgrade
iteration) + the networth summary card's height-family pin (session-158)

The session-161/162 v67 queue's two items (the re-run cadence rotates to
the v60-era pair — the networth view + the dashboard drill-down EXPANDED
re-run at 1280, the oldest remaining after v64/v65/v66 covered the
v57/v58/v59 pairs — and the axe-core wrapper upgrade decision) and the
61st standing checks.

1. **vlm-shots-v67.sh / clone-vlmshots-v67.sh / vlm-compare-v67.mjs** —
   the v60-era pair re-run, BOTH of that era's pairs (the v66 precedent:
   the v59-era re-run covered the calculator + login set): the networth
   FULL-PAGE pair + the dashboard drill-down EXPANDED pair at 1280x800
   (the expansion clicks are VIEW-STATE toggles — safe under the v46
   read-only rule; the parked-pointer discipline at (5,5) before every
   shot so no hover-revealed chrome is caught mid-flight). The networth
   half: VERDICT IDENTICAL, zero style flags. The drill-down half:
   5 style flags, all arbitrated (item 3).
2. **ref-standing-v61.sh / standing-checks-v61.sh** — the 61st standing
   checks (version-bumped from v60). Reference: the four bugs ALL live +
   the data census unchanged (61st clean drift check) + the SEO pair.
   Clone: R1-R4 green — the mobile menu VERIFIED WORKING (61st
   consecutive time), zero overflow at 390 on all five views.
3. **arbit-v67.sh + arbit-v67b.sh** — the two-part DOM arbitration
   census (both sides at 1280x800): PART A the five drill-down flags —
   the nav highlight (the root-URL active-nav gap: the reference
   transparent/zinc-700/400 vs the clone transparent/white/500), the
   avatar (the user-identity class), the hero progress fill (the pct ×
   568 data class: the track 568x12 byte-identical, the fills 173/357 =
   each site's own allocation pct), the donut percentage labels (the
   perception artifact re-confirmed: both sides count 4 [1 group + 3
   labels]/labelLineCount 0/16px/black/3 sectors), and the stat cards'
   footer TREND ICONS (a NEW flag variant — "different paths/angles" —
   arbitrated via the GLYPH census: byte-identical 16x16/
   rgb(143,188,63)/"0 0 24 24" with the same two-polyline Heroicons-v1
   outline trending-up; plus the hero-glyph census: the same 7 svgs in
   the same order both sides); PART B the networth summary card's HEIGHT
   family (the F-pin candidate): the card 960x333, the head row h 76/mb
   32px, the label mb 8px/h 20, the figure lh 48px/h 48, the medallion
   64x64 + icon 32x32, the stat grid rows "84px"/h 84, the stat tile
   440x84 (label 16 + mb 4 + amount 32 + pad 32), the ratio footer
   mt/pt 24/24 + border 1px + h 53 — BYTE-IDENTICAL on both sides.
4. **F1 — the axe-core 5.x wrapper watch + the upgrade DECISION** —
   local NO DRIFT (the registry state unchanged from v66: npm-latest
   4.14.0 with the declared nested engine axe-core ~4.14.0, verified by
   packing the tarball; the lockfile resolves 4.13.0; the NESTED engine
   axe-core@4.13.0 byte-identical to the v38–v66 audits; the top-level
   4.14.0 still eslint-plugin-jsx-a11y's — lint-time only). THE
   DECISION: the 4.14.0 upgrade is DEFERRED TO A DEDICATED v68
   ITERATION — never a drift, never a rider. The complete upgrade
   specification (the pin bump ^4.13.0→^4.14.0 + the lockfile
   regeneration + the nested-engine verify + the full a11y gate re-run +
   the rule-coverage re-audit) is carried in the v67 plan's v68 queue.
5. **The v67 pin** (tests/e2e/networth.spec.ts) — the networth summary
   card's HEIGHT-family computed census at 1280 (a new describe after
   the v60 F1 block, the read-only logged-in state, no fixture flow
   needed): the card 960x333, the head row h 76/mb 32px, the label mb
   8px/h 20, the figure lh 48px/h 48, the medallion h 64/iconH 32, the
   stat grid rows "84px"/h 84, the stat tile h 84/labelH 16/labelMb
   4px/amtH 32, the ratio footer mt 24px/pt 24px/borderTopW 1px/h 53.
   Three pin-sanity mutations verified to FAIL (the head row mb-8→mb-4;
   BOTH stat tiles p-4→p-2 — the shared-class regression, see lesson 5;
   the ratio footer mt-6 pt-6→mt-3 pt-3).
6. **The screenshots** — the 16-screenshot regeneration came out 16/16
   BYTE-IDENTICAL (no production-code change; the capture date matching
   the committed set's — no DATE-class diff this run).

**The v67 lessons:**
1. The single-quote-selector rule bites BOTH ways — the v60 lesson #1
   (a single quote inside a single-quoted bash string terminates it)
   applies inside the quoted-heredoc clone script too: the eval
   argument is ITSELF a single-quoted bash string. Use double-quoted
   attribute-value selectors — closest("[class*=grid]") — never
   closest('[class*="grid"]'). The failure signature is the same: an
   empty eval line between the === markers.
2. A `const` census variable assigned inside a walk-up loop throws
   "Assignment to constant variable" — and with stderr discarded the
   ONLY signature is that same empty eval line. Debug census evals
   with stderr visible before assuming a finder problem.
3. A childless-div finder pattern FAILS on container tracks — the hero
   progress TRACK legitimately carries the fill as a child. Drop the
   !children.length requirement when the element is a container; filter
   by geometry + computed chrome instead.
4. The reference's Heroicons-v1 trend glyph is POLYLINE-based — the svg
   carries NO `<path>` element, so a path-`d` signature census returns
   null. A glyph census needs the innerHTML signature (the polyline
   points); pathSig null ≠ broken, it means "no path element".
5. The stat tile's height at 1280 is STRETCH-GOVERNED — the grid row
   follows the TALLER sibling and stretch-fills both tiles to it
   (align-items: stretch, the default). A FIRST-tile-only pad mutation
   leaves the pinned h axis untouched (measured live: pad 8px + h 84 on
   the mutated tile beside its p-4 sibling) — the pin-sanity mutation
   must be the SHARED-class regression (both tiles). The stretch also
   explains the arithmetic's stability: both tiles share the content
   structure, so the row = either tile's natural height.

## v68 — the DEDICATED axe-core wrapper upgrade (the deliberate 4.14.0
pin bump + the rule-coverage re-audit) + the v61-era pair re-run (the
dashboard full-page 1280) + the a11y gate's engine-contract pin (session-165)

The session-163/164 v68 queue's two items (the DEDICATED axe-core
wrapper upgrade — the v67 plan's own decision, executed mechanically —
and the re-run cadence rotating to the v61-era pair, the dashboard
full-page 1280 standing pair, the oldest remaining after
v64/v65/v66/v67 covered the v57/v58/v59/v60 pairs) and the 62nd
standing checks. TOOLCHAIN-ONLY — src/ untouched (the pin-only line
continues; the upgrade touches package.json + package-lock.json).

1. **axe-rule-census-v68.mjs** — the rule-coverage census: enumerates
   the ACTIVATED rule set at the a11y gate's TAGS
   (wcag2a/wcag2aa/wcag21a/wcag21aa) from any axe.js bundle, via a
   plain Node require (the bundle attaches `axe` to module.exports).
   Run on BOTH engines — the pre-upgrade nested
   axe-core@4.13.0 (69 of 105 rules) and the 4.14.0 (69 of 105):
   the sets byte-identical, ZERO added, ZERO removed. The upgrade
   changes the engine version, NOT the activated coverage — no new
   rule to arbitrate, no markup issue to fix.
2. **The upgrade itself** — the deliberate pin bump (package.json
   ^4.13.0→^4.14.0, one line, the only manifest change) + npm install
   (the lockfile regenerates: the wrapper 4.14.0 and the NESTED engine
   entry DISSOLVES — npm dedupe; the top-level axe-core@4.14.0
   [eslint-plugin-jsx-a11y's, whose ^4.10.0 admits it] now satisfies
   the wrapper's ~4.14.0 too, so the tree carries ONE axe-core; 23
   lockfile lines, net -7) + the engine verify (the wrapper's own
   require.resolve('axe-core') → node_modules/axe-core/axe.js = 4.14.0,
   no nested dir remains) + the full a11y gate re-run: 22 passed (the
   v38 contract holds — no rule-behavior regression on any surface).
3. **ref-standing-v62.sh / standing-checks-v62.sh** — the 62nd standing
   checks (version-bumped from v61). Reference: the four bugs ALL live
   + the data census unchanged (62nd clean drift check) + the SEO pair.
   Clone: R1-R4 green — the mobile menu VERIFIED WORKING (62nd
   consecutive time), zero overflow at 390 on all five views.
4. **vlm-shots-v68.sh / clone-vlmshots-v68.sh / vlm-compare-v68.mjs** —
   the v61-era pair re-run (the dashboard FULL-PAGE at 1280x800 — the
   Budget Guidelines card + the quick-action row below the fold; login
   on the first attempt both sides, the parked pointer at (5,5)):
   VERDICT IDENTICAL, zero style flags — the re-run re-proves the
   v61-era surfaces live after the v61 STRETCH fix and v62-v67's pins.
5. **db-seedcheck-v68.cjs** — the pre-capture dev-DB seed-state check
   (7 items / Rent 1850 / expenses 2235 / 0 line items / 3 assets / 2
   liabilities) via the Prisma client (BudgetItem is keyed `category`,
   not `name` — the first draft's `name: "Rent"` query crashed).
6. **The v68 pin (+1 e2e = 270)** — the a11y gate's ENGINE-CONTRACT
   pin (a new describe at the a11y.spec.ts tail, the logged-out login
   surface): a real AxeBuilder scan asserts testEngine.name "axe-core"
   + testEngine.version /^4\.14\./ — the AxeResults carry the identity
   of the engine that ACTUALLY executed the scan, so the pinned
   toolchain is executable, not aspirational. The pin-sanity mutation
   is the TOOLCHAIN downgrade (npm install @axe-core/playwright@4.13.0
   — no rebuild needed, axe-core is a test-only dep never in the
   standalone build): the pin FAILED with the exact diagnostic, then
   the manifest was restored and the gate re-run green.
7. **The screenshots** — 10/16 byte-identical + 6 the DATE class: the
   FRESH-CLONED workspace's re-seed re-anchored the seed's
   isoDate(offsetDays) dates one day later (the committed set's DB was
   seeded 2026-10-15; db/ is gitignored — it does not travel). Every
   changed region pixel-arbitrated to date digits via the v66 PIL-diff
   method (the income "10"→"11", the expenses "13, 2026"→"14, 2026";
   the calculator's diff sub-perceptual at max channel 2).

**The v68 lessons:**
1. The axe.js bundle is a UMD-ish IIFE — under require() it attaches
   `axe` to module.exports. A vm sandbox with window/document stubs
   FAILS silently (the IIFE takes `typeof window === 'object' ? window
   : this`, attaches, then the load aborts on the missing DOM pieces —
   the global never appears). The honest census load is the plain
   Node require.
2. axe.getRules() returns metadata keyed `ruleId`, NOT `id` — a census
   sorting by `.id` crashes on undefined (the first draft's
   `Cannot read properties of undefined (reading 'localeCompare')`).
   Each entry carries `tags` + an `enabled` field; filter by the tag
   intersection with the gate's TAGS.
3. A createRequire path passed as a relative string resolves against
   the SCRIPT's directory, not the CWD — resolve(process.cwd(), arg)
   before require() or the census reports "Cannot find module".
4. An npm dedupe can DISSOLVE the wrapper's nested engine — after the
   ^4.14.0 bump the tree carries ONE axe-core (the top-level
   eslint-plugin-jsx-a11y copy satisfies both). The engine-verify
   must follow the WRAPPER'S OWN require.resolve('axe-core'), never
   assume the nested path exists.
5. A fresh-cloned workspace re-anchors the seed's relative dates —
   db/custom.db is gitignored, so a re-seed on a different day shifts
   every rendered date digit (the committed screenshots' DATE class).
   The PIL pixel-diff (the v66 method) arbitrates it in minutes; the
   honest capture is committed, not reverted.

## v69 — the mobile 390 pair re-run (BOTH twins — the networth
## full-page, the documented queue item, PLUS the dashboard twin) + the
## networth page-header row pin + the F0 lint-gate repair (session-167)

The session-165/166 v69 queue's items (the re-run cadence rotating to
the mobile twins — both covered in one two-pair iteration, the v62/v67
precedent; the axe-core watch at its re-check point [NO DRIFT — only a
5.x wrapper changes the calculus now, the engine-contract pin guarding
the toolchain]; the deferred reference-write censuses [unchanged,
blocked by the v46 read-only rule]) plus the 63rd standing checks.
PIN-ONLY for src/ (the pin-only line continues; the three pin-sanity
mutations were verified then reverted, `git diff src/` = 0 lines).

1. **vlm-shots-v69.sh / clone-vlmshots-v69.sh / vlm-compare-v69.mjs** —
   BOTH mobile 390x844 full-page twins re-run (the networth view — the
   documented queue surface — and the dashboard, the other never-re-run
   mobile pair; login on the first attempt both sides, the parked
   pointer at (5,5)): both pairs CLEAN, every flag DOM-arbitrated via
   arbit-v69.sh. The networth re-run's three flags = the v63-era classes
   re-confirmed live with the EXACT v63 numbers (the stat-tile stacking
   [the v41 mobile-superset class], the trend icon [the v54 clipping
   perception artifact], the Base44 overlay [platform chrome]); the
   dashboard re-run's flags = the Base44 tooltip [platform chrome] + the
   subtitle wrap [the documented v62 class — the chrome byte-identical,
   the reference's own docSW 395 overflow shifting its wrap point by one
   word] + a NEW flag variant DOM-DISPROVEN ("the reference's breakdown
   card contains a donut" — ZERO donut on EITHER side).
2. **arbit-v69.sh** — the four flags' DOM census on BOTH sides at 390:
   the networth summary-card family (the v63 census re-used verbatim)
   plus the dashboard pair's two censuses (the subtitle's per-word line
   bucketing via a Range walk — the exact wrap lines on both sides —
   and the breakdown/spending cards' chart census: the recharts-wrapper
   + pie-sector counts that disproved the donut claim).
3. **nw-header-v69.sh** — the v69 pin's measurement probe: the
   /networth view's PAGE-HEADER ROW computed census at 390 on the clone
   (the never-census'd family — the v14 chip test pins x-positions
   only; the v65 savings header-row pin's sibling).
4. **ref-standing-v63.sh / standing-checks-v63.sh** — the 63rd standing
   checks (version-bumped from v62). Reference: the four bugs ALL live
   + the data census unchanged (63rd clean drift check) + the SEO pair.
   Clone: R1-R4 green — the mobile menu VERIFIED WORKING (63rd
   consecutive time), zero overflow at 390 on all five views.
5. **db-seedcheck-v68.cjs** — the F0 repair: the v68 ship's own miss
   (the file was created AFTER v68's final lint run, so the committed
   v68 tree failed `npm run lint`). The single-file eslint-disable
   directive; the gate stays strict for the rest of scripts/. NOTE the
   v69 lesson: run it under `env -u DATABASE_URL` — the sandbox's
   inherited parent-workspace URL breaks one-shot Prisma scripts.
6. **The v69 pin (+1 e2e = 271)** — the networth page-header row
   computed census at 390 (a new describe at the networth.spec.ts tail):
   the row flex/center/gap-3 12px/mb-8 32px/w 358/h 60 (the TEXT BLOCK
   governs — the h1 36 + the subtitle 24 — not the 48px chip), the chip
   48×48/rounded-xl/forest→lime gradient + the 24×24 white icon, the
   h1 30px/700/lh 36px/forestDark, the block w 250/h 60, the subtitle
   16px/400/gray-500 ONE line, the row→card gap 32, docSW 390. GREEN on
   first run; three pin-sanity mutations verified to FAIL then restored
   (the row mb-8→mb-4; the chip h-12 w-12→h-10 w-10; the h1
   text-3xl→text-2xl — each with the standalone REBUILD as a SEPARATE
   command).
7. **The screenshots** — 16/16 BYTE-IDENTICAL (the first
   fully-identical set since v65: the v68 re-seed and the v69 capture
   share the 2026-10-16 calendar day, every rendered date digit
   matching; no DATE-class arbitration needed this run).

**The v69 lessons:**
1. One-shot Prisma scripts need `env -u DATABASE_URL` — the sandbox
   exports an absolute parent-workspace URL that silently overrides the
   .env resolution and breaks the DB open (error code 14). The
   documented npm-script discipline applies to every direct node
   invocation of the client too.
2. The VLM can INVENT a chart inside a card that carries none on either
   side (the "faint circle behind the text" donut claim). A
   chart-presence claim needs the recharts-wrapper/pie-sector census on
   BOTH sides — never a screenshot read.
3. A wrap-point difference with byte-identical chrome is a WIDTH-DELTA
   class — measure the block width + the docSW before believing a
   typography flag (the reference's own 395px overflow shifted its
   subtitle wrap by one word; the chrome was byte-identical).
4. The clean-check gate must re-run AFTER every new file lands, not
   only before the ship summary — a file created in the screenshots
   phase (the chain's tail) escapes a chain run from the morning (the
   v68 seedcheck miss, the F0 repair's own lesson).

## v70 — the OLDEST re-run candidate's fresh standing sweep (the
## v57-era items pair re-run) + the expenses filter-card pin (session-169)

The session-167/168 v70 queue's items (the re-run cadence returning to
the DESKTOP pairs — the OLDEST re-run candidate: the v57-era items
pair, last re-shot by v64 itself, the cadence's first COMPLETED cycle
[v64→v70]; the NEW-pair program stays the v71+ candidate; the axe-core
watch at its re-check point [NO DRIFT — only a 5.x wrapper changes the
calculus now, the engine-contract pin guarding the toolchain]; the
deferred reference-write censuses [unchanged, blocked by the v46
read-only rule]) plus the 64th standing checks. PIN-ONLY for src/ (the
pin-only line continues; the three pin-sanity mutations were verified
then reverted, `git diff src/` = 0 lines).

1. **vlm-shots-v70.sh / clone-vlmshots-v70.sh / vlm-compare-v70.mjs** —
   the items pair (income + expenses) at desktop 1280x800, FULL-PAGE
   both views, the fresh re-run of the OLDEST re-run candidate (the
   v57-era pair; login on the first attempt both sides, the parked
   pointer at (5,5)). PAIR 1 (income): the avatar + the card grid + the
   seed data — all documented classes. PAIR 2 (expenses): the footer +
   the badge arrangement + the avatar — all documented classes. **Both
   pairs CLEAN.**
2. **arbit-v70.sh** — the DOM arbitration census (both sides, both
   views at 1280x800): the avatar (the first-pass finder caught the
   clone's brand block — see arbit-v70b.sh) + the item grid + the
   first-card chrome + the footer (per-child spans + icons) + the badge
   row + the FILTER CARD on BOTH views — the income variant re-confirmed
   AND the never-census'd EXPENSES variant measured (the v70 pin's
   reference-side parity proof: the card 960×86, the search 216×36 NOT
   spanning, the 4-track 215.5px grid, the 4 children, the three
   comboboxes 216×36) + the header.
3. **arbit-v70b.sh** — the follow-up census for the two items the first
   pass left open: (1) the clone-side AVATAR finder (the v65b pattern —
   a small round element with 1-2 text chars near the rail bottom; the
   clone's avatar uses rounded-[9999px], not rounded-full) — the chrome
   measured BYTE-IDENTICAL (36×36/radius 9999px/14px-600/white/bg
   rgb(143,188,63), only "U" vs "D"); (2) the CARD INTERNALS
   decomposition — every card's title/subcategory/amount/badge-row/
   footer blocks censused on both sides, both views: the card-height
   delta (ref 200 vs clone 230) decomposes arithmetic-wise — the
   Recurring superset badge's wrap h 52 (22+8+22) → +30px, and the
   1-row grid STRETCHES the shorter sibling to the taller card's
   natural height (the v67 stretch-governed lesson generalized to the
   item cards).
4. **ref-standing-v64.sh / standing-checks-v64.sh** — the 64th standing
   checks (version-bumped from v63). Reference: the four bugs ALL live
   + the data census unchanged (64th clean drift check) + the SEO pair.
   Clone: R1-R4 green — the mobile menu VERIFIED WORKING (64th
   consecutive time), zero overflow at 390 on all five views.
5. **The v70 pin (+1 e2e = 272)** — the EXPENSES view's filter-card
   computed census at 1280 (a new describe at the items.spec.ts tail):
   the card 960×86, the search 216×36 (the 1-COL span — the expenses
   variant's defining difference, the search NOT spanning 2 columns)
   with the asymmetric 40px left pad, the 4-track 215.5px grid with 4
   children, the three 216×36 comboboxes at 14px. GREEN on first run;
   three pin-sanity mutations verified to FAIL then restored (the
   expense-branch gap-4→gap-2; the card p-6→p-4; the search
   pl-10→pl-4 — each with the standalone REBUILD as a SEPARATE
   command).
6. **The screenshots** — 16/16 BYTE-IDENTICAL (the second consecutive
   fully-identical set: the dev DB's 2026-10-16 seed and the v70
   capture share the calendar day; no DATE-class arbitration needed).

**The v70 lessons:**
1. A card-height delta decomposes arithmetic-wise — census the card's
   internal blocks (title/subtitle/amount/badge row/footer) on both
   sides before classifying; the wrap arithmetic (22+8+22 = 52 → +30px)
   explains a "mystery" 30px delta exactly.
2. The grid STRETCH governs sibling card heights — a 1-row grid
   stretches every card to the tallest sibling's natural height, so a
   card with an unwrapped badge row can still measure the wrapped
   height (the v67 stat-tile lesson generalized to the item cards; a
   single-card mutation may not move the axis if the sibling holds it).
3. The clone's avatar uses `rounded-[9999px]`, not `rounded-full` — the
   reliable avatar census is the v65b finder pattern (a small round
   element with 1-2 text chars near the rail bottom), never a
   rounded-full class selector.

## v71 — the NEW-pair program opens (the items views' mobile 390
## full-page pairs) + the item-card subtitle-P conditional-render fix
## (session-171)

The session-170/171 v71 queue's items (the NEW-pair program opens —
the below-the-fold 390 surfaces, the items views' mobile twins never
individually shot, the v62/v63 precedent extending the standing-pair
matrix to the remaining views; the axe-core watch at its re-check point
[NO DRIFT — npm-latest 4.14.0, only 4.14.1 rc/next prereleases, no 5.x
exists; the lockfile holding the v68 dedupe state; the engine-contract
pin green in the baseline]; the deferred reference-write censuses
[unchanged, blocked by the v46 read-only rule]) plus the 65th standing
checks. THE FIX iteration — the first production-code change since v61
(the pin-only line broken): the item-card SUBTITLE-P conditional render.

1. **vlm-shots-v71.sh / clone-vlmshots-v71.sh / vlm-compare-v71.mjs** —
   the NEW-pair program's first family: the ITEMS views' mobile 390x844
   FULL-PAGE pairs (income + expenses + savings — the below-the-fold
   surfaces never individually shot; login on the first attempt both
   sides, the parked pointer at (5,5)). PAIR 1 (income): VERDICT
   IDENTICAL — zero layout/style flags. PAIR 2 (expenses): the footer +
   the badge wrapping + the Base44 FAB. PAIR 3 (savings): the footer +
   the badge arrangement + the badge styling + the "active badge
   padding" claim.
2. **arbit-v71.sh** — the DOM arbitration census (both sides, all three
   views at 390x844): the full card-internals decomposition per card —
   the title row (h/mb) + the SUBTITLE P (presence + h/fs/lh/color —
   the NEW axis) + the amount block + the badge row (per-badge chrome:
   h/w/pad/radius/fs/fw/bg/color/border) + the footer (per-child spans
   + icons). Every PAIR 2/3 flag arbitrates to a documented class: the
   footer = the v57 DATA-CONDITIONAL class (chrome byte-identical; the
   childCount the reference's own data), the badge wrapping = the v57
   wrap class (chrome byte-identical; the Recurring superset badge's
   wrap h 52), the badge styling = the v58 classification-VALUE data
   class (the color maps byte-identical per classification), the
   "active badge padding" = a PERCEPTION ARTIFACT (byte-identical on
   every card both sides: h 22/w 63/pad "2px 10px"/radius 6px/fs 12px/
   fw 600/bg rgb(248,250,252)/color rgb(51,65,85)). **THE DISCOVERY:**
   the reference's Miscellaneous/Investments expense cards (EMPTY
   subcategory) render subtitleP {present:false} with titleRow 28 and
   card 180 — **the reference CONDITIONALLY RENDERS the subtitle P**;
   the clone's item-card.tsx:127 rendered `{item.subcategory ?? ""}`
   unconditionally (a 20px empty block on user-created
   empty-subcategory items).
3. **ref-standing-v65.sh / standing-checks-v65.sh** — the 65th standing
   checks (version-bumped from v64). Reference: the four bugs ALL live
   + the data census unchanged (65th clean drift check) + the SEO pair.
   Clone: R1-R4 green — the mobile menu VERIFIED WORKING (65th
   consecutive time), zero overflow at 390 on all five views.
4. **The v71 fix (+2 e2e = 274)** — the subtitle-P conditional render
   (the v52 details-sheet idiom applied to the item-card: `{item.subcategory ?
   (<p>…</p>) : null}`) + the F4 REGRESSION test (an Add-Expense
   no-subcategory fixture renders NO subtitle P, titleRow 28, card h
   180 at 390 in the 1-col grid — the reference's own no-subtitle
   geometry; RED on the unfixed build, GREEN after; the cleanup rides
   the Edit dialog's Delete path, the header count restored) + the F5
   PIN (the seeded Rent card's WITH-subtitle geometry: the P's chrome
   h 20/fs 14px/lh 20px/color rgb(107,114,128), titleRow 48,
   titleRowMb 12 — pins the other side of the conditional so the fix
   cannot regress the populated state) + the pin-sanity mutation (the
   reverted conditional → F4 FAILS at exactly subtitleCount; restored
   → GREEN; the standalone REBUILD as a SEPARATE command).
5. **The screenshots** — 16/16 BYTE-IDENTICAL (the third consecutive
   fully-identical set: the same-day seed; the fix touches no seeded
   surface — the dev seed carries no empty-subcategory items, the gap
   lived in the UNSHIPPED state space).

**The v71 lessons:**
1. A conditional-render gap can hide for 40+ iterations when the seed
   never exercises the empty state — the NEW-pair program's richer
   flag surfaces are what expose it (the reference's own demo data
   carries empty-subcategory cards; the clone's richer seed does not).
2. The card-internals census now includes the SUBTITLE-P PRESENCE axis
   — census the OPTIONAL-field renders' PRESENCE, not just their
   chrome: `{value ?? ""}` renders an invisible block the reference
   never draws (the v52 details-sheet lesson, finally generalized to
   every optional-field render site).
3. The grid STRETCH + badge-wrap arithmetic re-confirmed at 390 — a
   card-height delta decomposes through the same internal blocks at
   every viewport (the v70 lesson holds at mobile).

## v72 — the NEW-pair program continues (the details-sheet mobile 390
## twins + the drill-down EXPANDED mobile twin) + the details-sheet
## EMPTY-subtitle pin (session-173)

The session-171/172 v72 queue's items (the NEW-pair program's remaining
below-the-fold 390 surfaces — the details-sheet mobile twin + the
drill-down EXPANDED mobile twin; the re-run alternative was the v58-era
savings pair, the NEW-pair chosen as the stronger candidate per the v71
precedent) + the axe-core watch at its re-check point + the 66th
standing checks. **PIN-ONLY for src/ — no production-code change; +1
e2e = 275.** The probes:

- `vlm-shots-v72.sh` / `clone-vlmshots-v72.sh` /
  `vlm-compare-v72.mjs` — the three NEW pairs at mobile 390x844:
  PAIR 1 the WITH-subtitle details sheet (the Rent card — subcategory
  "Apartment" on BOTH sides, the tightest data-matched pair), PAIR 2
  the EMPTY-subcategory details sheet (the reference's Miscellaneous
  card vs the clone's user-created Add-Expense fixture — the v71 F4
  discipline; the v52 sheet conditional's EMPTY side never shot against
  the reference's own empty-side sheet), PAIR 3 the dashboard's
  drill-down EXPANDED state (the v67 desktop pair's mobile twin — the
  Total Income section + first category expanded, view-state clicks
  only). The sheet pairs are VIEWPORT captures (the bottom-anchored
  overlay state IS the page state); the drill-down pair is full-page.
- `arbit-v72.sh` — the DOM arbitration census at 390 on BOTH sides:
  the sheet root (the fixed z>=50 overlay whose text starts with
  "Budget Item Details"), the scrim, the surface (the white rounded
  panel: x/y/w/h/bottom/maxH/overflow/radius/shadow), the sticky
  header + the X close button (the full chrome: border/outline/
  boxShadow/bg/radius/svg), the summary text blocks (the H3 name /
  the subtitle P / the amount — the leaf fs>=18 census), the pill
  badges, the fact-row + meta-footer inventory (the label scan), and
  the drill-down expanded rows (the button texts/h/pad/fs/radius +
  the container indent + the footer count).
- `ref-standing-v66.sh` / `standing-checks-v66.sh` — the 66th
  standing checks (version-bumped from v65).
- `cleanup-fixture-v72.sh` — the corrective probe (the first
  cleanup pass missed: the Edit dialog carries the item name in the
  Category INPUT VALUE, not textContent — the fixture was stranded
  and recovered via this script; the seedcheck confirmed the exact
  seed state after).

**The arbitration's findings:** NO NEW GAP — every flag arbitrates to
a documented class. The close-button "visible square border" claim =
a PERCEPTION ARTIFACT (the chrome BYTE-IDENTICAL: 36x36/radius
6px/border 0px/transparent bg/no shadow/no outline/16px #0a0a0a X;
the clone's extra "Close" text is sr-only — invisible). The
"reference cropped below Status / clone reveals Created-Last Updated"
claim = a PERCEPTION ARTIFACT (the sheet geometry byte-identical —
surface 390x717 anchored at bottom 844, maxH 717.4px, overflow auto,
radius 24px top corners, the scrim rgba(26,58,46,0.5)+blur(8px); BOTH
sides carry the Created/Last Updated meta rows with identical chrome
rowH 36/labelFs 12px/labelColor rgb(107,114,128) — the reference's
meta rows sit behind its own platform FAB overlay in the
bottom-right corner). The Payment-Method row = the v52 optional-field
DATA-CONDITIONAL class. The drill-down row inventory = the seed-data
class (the reference's 1 income item vs the clone's 2; the category
chrome byte-identical h 28/pad "6px 12px"/fs 16px/400/radius 8px;
the item-row label "Item" vs "Net monthly salary" = the NOTES-VALUE
data class — the reference's own v60-dumped behavior renders the
literal "Item" for notes-less items, the clone's itemLabel implements
exactly this contract). The 5px row-width delta = the reference's own
docSW-395 overflow class (documented v62/v69). **THE HEADLINE: the
no-sub sheets BOTH render NO subtitle P (the H3 name -> the amount
directly) — the v52 sheet conditional's EMPTY side verified LIVE
against the reference's own empty-side sheet, the v71 card-side
fix's sibling surface.**

The v72 pin: the details sheet's EMPTY-subtitle side census at 390
(`tests/e2e/item-details.spec.ts` — an Add-Expense no-subcategory
fixture's sheet renders NO subtitle P, the H3->amount adjacency holds,
the 24/700/mb-8 H3 + the 36/700/mt-16 amount chrome, the panel w 390;
the fixture create/cleanup rides the v71 F4 discipline). GREEN on
first run — the v52 conditional has been correct in the code since
v52; the pin locks it. The pin-sanity mutation (the conditional
reverted to the unconditional empty-P render) verified to FAIL at
exactly subtitleCount, then restored (the standalone REBUILD as a
SEPARATE command; git diff src/ = 0 lines).

**The v72 lessons:**
1. The reference's details sheet carries NO `role=dialog` — it is a
   custom fixed overlay (`fixed inset-0 z-50 flex items-end…`). The
   sheet detection must census the fixed z>=50 overlay whose TEXT
   starts with the sheet title (the clone's Radix sheet also matches
   — the same detection works on both sides).
2. The reference's card-open mechanism is the CARD ROOT click
   (`div.rounded-xl.cursor-pointer`) — an h4-only click did not open
   it in the probe's first pass; target the card root, not the title.
3. The clone-side Edit-dialog cleanup must identify the dialog by the
   Category INPUT VALUE (`#item-category.value`), never textContent —
   the item name lives in the input's value; a textContent check
   silently misses the dialog and strands the fixture.
4. The reference's scrim and the clone's scrim are structurally
   different elements (the reference's overlay WRAPS the panel and
   carries the text; the clone's Radix scrim is a SIBLING of the
   content) — the rendered geometry is the contract, not the DOM
   shape (both: x 0, y 127, w 390, h 717, bottom 844).
5. An sr-only text span does not render — but it DOES appear in
   textContent (the clone's close button "Close" span); a VLM cannot
   see it, and a census must not treat its presence as a visual
   difference (read the computed sr-only geometry or ignore leaf
   text inside buttons when censusing chrome).

## v73 — the NEW-pair program's LAST never-shot surfaces (the login + calculator mobile 390 twins) + the calculator scrim + summary-text chrome pin (PIN-ONLY)

The session-173/174 v73 queue's items (the NEW-pair program's remaining
surfaces — the login page's mobile 390 twin, the simplest never-shot
pair; the calculator dialog's mobile 390 twin, the v66 desktop pair's
mobile twin) and the axe watch at its re-check point — plus the 67th
standing checks. With these two pairs the NEW-pair program is COMPLETE:
every view + dialog + sheet surface now carries BOTH a desktop pair and
a mobile-390 twin.

- `vlm-shots-v73.sh` / `clone-vlmshots-v73.sh` / `vlm-compare-v73.mjs` —
  the two NEW pairs at mobile 390x844: PAIR 1 (the LOGIN page, the fresh
  logged-out surface — the shot precedes any login submit) VERDICT
  IDENTICAL, zero flags; PAIR 2 (the CALCULATOR dialog — the hover +
  Calculate click at the mobile viewport, the reference's OWN Rent card
  $25.00 with its single Contents Insurance line item; the clone's 1-row
  state rides the v66 fixture discipline: add the line item through the
  real UI, screenshot, then FULLY restore) — two flags, both DOM-arbitrated:
  the "scrim lighter" claim a PERCEPTION ARTIFACT (the scrim chrome
  byte-identical: bg rgba(26,58,46,0.5) / opacity 1 / blur(8px) / 390x844)
  and the "Will update category total" span the v66 DATA-CONDITIONAL class.
- `arbit-v73.sh` — the calculator's complete chrome census at 390 on BOTH
  sides (the scrim family, the panel, the header + chip + close, the title
  + description, the Total Calculated block + the amount + the based-on
  line + the will-update span, the line-item row, the Add Item button) —
  byte-identical on every axis.
- `ref-standing-v67.sh` / `standing-checks-v67.sh` — the 67th standing
  checks (version-bumped from v66).
- The v73 pin (tests/e2e/calculator.spec.ts): the calculator's scrim +
  summary-text chrome census at 390 — the never-pinned axes (the scrim
  itself — the details-sheet overlay was pinned, the calculator's never
  was; the summary amount 24/700/lh-32; the based-on line 12px gray; the
  description 14/20 gray; the will-update span 12/400 #ea580c with the
  fixture). GREEN on first run. The pin-sanity mutation (the scrim blur
  8px→4px in `.zb-modal-overlay`) verified to FAIL at exactly the scrim
  axis, then restored (the standalone REBUILD as a SEPARATE command;
  git diff src/ = 0 lines).

**The v73 lessons:**
1. The mobile fold: at 390 the Rent card sits BELOW the fold in the
   1-col grid (card center y > 844). A raw mouse move to out-of-viewport
   coordinates never engages the card's `:hover` — the Calculate button
   stays hidden and the click misses (`no dialog`). `scrollIntoView({block:
   'center'})` BEFORE the hover is the required step.
2. The unquoted-heredoc dollar trap: a `<<EOF` (unquoted) heredoc expands
   `\$1850` into `$1850` at heredoc-processing time, and the inner
   `bash -s` then reads `$1` (a positional parameter) inside the
   double-quoted eval string — `set -u` kills the script with
   "unbound variable". The fix: the QUOTED `<<'EOF'` heredoc with the
   shared census injected via an ENVIRONMENT variable
   (`CALC_CENSUS_JS="$CALC_CENSUS_JS" bash ... bash -s <<'EOF'`), the
   inner script keeping the probe's own `\$` escaping conventions.
3. A scrim "transparency" claim arbitrates through the computed style,
   not the screenshot: the bg color, the computed opacity, and the
   backdrop-filter are three separate axes (all byte-identical here) —
   the VLM's "lighter" read tracked none of them.

## v74 — the re-run cycle's OLDEST candidate (the v58-era savings pair's second re-run) + the savings goal-card's interior-text + hidden-h1 pin (PIN-ONLY)

The session-178 v74 cycle: with the NEW-pair program complete (v73), the
cadence rotates to the re-run cycle's OLDEST candidate — the v58-era
savings pair, last re-shot v65, the only pre-v70 pair not re-run since —
plus the axe watch at its re-check point and the 68th standing checks.

**The probes:**
- `vlm-shots-v74.sh` — the reference side: the savings view at desktop
  1280x800, FULL-PAGE (the fresh sweep; login-retry loop; the parked
  pointer at (5,5)).
- `clone-vlmshots-v74.sh` — the clone side, the same shot inside
  with-server.sh (the :3200 standalone parity server).
- `vlm-compare-v74.mjs` — the VLM pairwise (the savings-view prompt).
- `arbit-v74.sh` — the both-sides /savings DOM census at 1280 (the v43
  rule: every VLM flag DOM-verified before it counts): the header row
  (h1/subtitle/Add button), the grid (template/gap/w/childCount), the
  card chrome, the h4 title + the amount (the amount matched by the
  `text-2xl` CLASS — see the lessons below), the footer (the
  DATA-CONDITIONAL childCount axis) + its children's chrome + icons, the
  badge row + every badge's full chrome (the classification color maps),
  the docSW — plus the db-seedcheck-v68.cjs seedcheck at the end.
- `ref-standing-v68.sh` / `standing-checks-v68.sh` — the 68th standing
  checks (version-bumped from v67).
- The v74 pin (tests/e2e/items.spec.ts): the savings goal-card's
  interior-text chrome + the hidden app-shell h1 census at 1280 — the
  never-pinned axes (the h4 title's lh + the 1280 state of the v51 pin's
  390-only family; the amount's lh + 1280 state; the hidden first-in-DOM
  h1 "ZeroBalance" — the v65-documented surface, pinned for the first
  time). GREEN on first run. The pin-sanity mutation (the amount's
  `text-2xl` → `text-xl`) verified to FAIL at exactly the cardAmount
  axis, then restored (the standalone REBUILD as a SEPARATE command;
  git diff src/ = 0 lines).

**The v74 lessons:**
1. The amount's dollar-prefixed textContent is matched by the `text-2xl`
   CLASS, never by text — the v64 dollar rule's census corollary: a
   literal `$` inside a double-quoted bash census string expands against
   bash's own positional parameters (`$4` in `[$0-9,]` silently empties),
   so the class-based finder is the only safe detector for
   dollar-prefixed text.
2. The md-hidden-subtree census: an element inside a `display:none`
   SUBTREE keeps its OWN computed display ("block" for an h1) while
   rendering zero-size boxes (w 0/h 0 — getBoundingClientRect on a
   no-layout subtree returns zeros). The v65 note's "hidden zero-size"
   mechanism: assert w/h 0, never display "none", for md-hidden
   subtrees — the ancestor carries the display:none, the descendant
   reports its own.
3. A pre-pin probe beats a wrong assertion: the pin's first draft
   asserted `display === "none"` for the hidden h1; the live h1probe
   (with-server + one eval) returned display "block"/w 0/h 0 and
   corrected the pin BEFORE the RED/GREEN cycle — the mutation check
   only validates the axes you actually assert.

## v75 — the re-run cycle's next-oldest candidate (the v59-era login + calculator pair's second re-run) + the login card's geometry + typography pin (PIN-ONLY)

The session-180 v75 cycle: the re-run cadence rotating past the v74
savings pair to the next-oldest candidate — the v59-era pair (the login
view + the calculator dialog at 1280, last re-shot v66) — plus the axe
watch at its re-check point and the 69th standing checks.

**The probes:**
- `vlm-shots-v75.sh` — the reference side: the CALCULATOR dialog at
  1280x800 (the login-retry loop; the Rent-card finder RETRIES — the
  fresh-login first fetch can be slow; the real-mouse hover + the
  Calculate click; the parked pointer after the census).
- `clone-vlmshots-v75.sh` — the clone side, the same shot inside
  with-server.sh (the :3200 standalone parity server), riding the v66
  fixture discipline: the matching "Contents Insurance" $25 monthly-active
  line item added through the real UI, the 1-row state shot, then the
  FULL restore (delete + Rent's $1850 re-edit + the "$2235.00" page-total
  verification).
- `login-shots-v75.sh` / `clone-login-shots-v75.sh` — the LOGIN pair at
  1280x800 (the logged-out surface, no session).
- `vlm-compare-v75.mjs` — the VLM pairwise (the calculator + login
  prompts).
- `arbit-v75.sh` — the both-sides DOM arbitration census (the v43 rule):
  the CALCULATOR census (the panel + scrim + the header family + the
  totalCard + the row + the pills + the amount + the hover actions + the
  Add Item button — the shared env-injected JS, the amount leaf found via
  String.fromCharCode(36), the v64 dollar rule) + the LOGIN census (the
  card + h1 + subtitle + inputs + signIn + links + brand) — the clone side
  inside the QUOTED heredoc with the censuses env-injected (the v73
  lesson) + the seedcheck at the end.
- `login-census-ref-v75.sh` — the reference login census FOLLOW-UP: the
  arbit-v75.sh pass raced the cold session's page load (the form wasn't
  in the DOM at census time — "form not found"); this script RETRIES the
  load until the census lands.
- `pixel-diff-v75.py` — the 07-add-item-modal DATE-class arbitration
  (the v66 discipline): the PIL diff localizing the overnight change to
  the date input's day-digit region.
- `ref-standing-v69.sh` / `standing-checks-v69.sh` — the 69th standing
  checks (version-bumped from v68, the ordinal included).
- The v75 pin (tests/e2e/login-parity.spec.ts): the login card's
  geometry + typography census at 1280 — the never-pinned axes of the
  VLM-identical surface (the card w 448/radius 16px/bg white-95; the
  h1's TYPOGRAPHY family 30px/700/lh 36px — only its color was pinned
  by v7; the subtitle fs 16px; the input pair 48/12px/14px; the Sign in
  FULL chrome 368x48/12px/14px/500; the logo 96x96/alt; the docSW
  guard). GREEN on first run. The pin-sanity mutation (the h1's
  sm:text-3xl → sm:text-2xl) verified to FAIL at exactly the h1 axis
  (fs 30px→24px), then restored (the standalone REBUILD as a SEPARATE
  command; git diff src/ = 0 lines).

**The v75 findings:**

1. **PAIR 1 (the LOGIN view at 1280) — VERDICT IDENTICAL, zero style
   flags** (the only delta the Base44 FAB — platform chrome). The
   census byte-identical on every axis: the card 448/16px/
   rgba(255,255,255,0.95), the h1 30/700/lh 36/rgb(15,23,42), the
   subtitle 16/rgb(100,116,139), the logo 96x96, the inputs
   48/12px/14px/1px rgb(226,232,240), the Sign in
   368x48/12px/14px/500/rgb(15,23,42), the links [] on BOTH sides (the
   mode switchers are buttons, not anchors), the Google + OR blocks
   both present. The card shadow: the reference's 3-layer computed form
   (2 transparent leads) vs the clone's 5-layer (4 transparent leads) —
   the VISIBLE layer byte-identical (rgba(0,0,0,0.25) 0px 25px 50px
   -12px), the lead-layer count the v66 documented computed-form class.
2. **PAIR 2 (the CALCULATOR dialog at 1280)** — three VLM flags, every
   one DOM-arbitrated to a documented class: the "extra will-update
   line" the v66 DATA-CONDITIONAL class (ref false/clone true — the
   reference's Rent natively $25.00 === its line-item total); the "row
   hover state" the v66 pointer-position class (actionsAtRest opacity
   0/btnCount 2 on BOTH sides — the reference's screenshot caught the
   actions mid-reveal because the shot precedes the pointer park, the
   clone's follows it); the "amount alignment" the pointer-position
   corollary (the amount chrome byte-identical
   20/700/rgb(224,122,59)/h 28). The full census otherwise
   byte-identical: the panel 768x393/16px/white, the scrim
   rgba(26,58,46,0.5)/blur(8px)/1280x800, the title 18/700/lh 28, the
   desc 14/20 gray, the totalCard 720x90/16px/12px/rgb(252,221,213),
   the nameH4 16/600/h 24/mb 4, the row 720x102/16px/12px/
   rgb(229,231,227), the pillRow flex/gap 8/h 20, the pill1
   20x65/2px 8px/9999px/12px/400, the addBtn 110x32/6px/12px/500,
   the docSW 1280. NO NEW GAP.
3. The screenshots 15/16 byte-identical + 07-add-item-modal the
   documented dialog-default DATE class (the calendar rolled
   2026-10-16 → 2026-10-17): pixel-arbitrated via pixel-diff-v75.py —
   the 16x22 px region at (1552,931)-(1568,953), the EXACT v66 bbox,
   everything else in the 2880x1800 frame byte-stable.

**The v75 lessons:**
1. The cold-session login census races its page load: a single-shot
   read returned "form not found" on the reference side (the fresh
   context's first navigation hadn't painted the form at census time).
   The load-RETRIED census (login-census-ref-v75.sh — loop the open +
   census until the form lands) is the reliable pattern for a
   cold-context surface; never accept a "not found" as a verdict.
2. The login card's shadow arbitrates through the VISIBLE layer: the
   reference's computed string carries 2 transparent lead layers, the
   clone's 4 (different engines, different lead counts) — the rendered
   chrome (the one non-transparent layer) is byte-identical. The v66
   computed-form class generalizes: compare the full string, classify
   on the visible layer.
3. The DATE-class screenshot diff recurs every calendar rollover —
   expect exactly one small-region diff per overnight regeneration and
   arbitrate it programmatically (the PIL bbox + the region size), never
   with a VLM verdict.

## v76 — the re-run cycle's next-oldest candidate (the v60-era networth + drill-down pair's second re-run) + the breakdown section-icon chip glyph + donut label chrome pin (PIN-ONLY)

The session-181 v76 cycle: the re-run cadence rotating past the v75
login+calculator pair to the next-oldest candidate — the v60-era pair (the
networth view + the dashboard drill-down EXPANDED at 1280, last re-shot v67)
— plus the axe watch at its re-check point, the 70th standing checks, and
the F0 standalone-static-copy environment lesson.

**The probes:**
- `vlm-shots-v76.sh` — the reference side: the NETWORTH view at desktop
  1280x800 FULL-PAGE + the DASHBOARD's drill-down EXPANDED state (the
  login-retry loop; the parked pointer at (5,5); the expansion clicks
  VIEW-STATE only — the v46 read-only rule holds).
- `clone-vlmshots-v76.sh` — the clone side, the same shots inside
  with-server.sh (the :3200 standalone parity server).
- `vlm-compare-v76.mjs` — the VLM pairwise (the networth + drill-down
  prompts, the v67 prompt lineage).
- `arbit-v76.sh` — the both-sides DOM arbitration census (the v43 rule),
  the v75 single-script convention: the reference side direct + the clone
  side inside the QUOTED heredoc with the censuses env-injected (the v73
  lesson) + the seedcheck at the end. PART A (the drill-down): the nav
  highlight (the v56 class), the avatar letter, the hero progress track +
  fill (the pct data class), the donut labels (the v60 perception class),
  the stat trend icons + the hero trend glyphs (the v67 axes — the drift
  re-check). PART B (the networth): the summary card's full HEIGHT family
  (the v67 F3 pin's own axes — the drift re-check).
- `ref-standing-v70.sh` / `standing-checks-v70.sh` — the 70th standing
  checks (version-bumped from v69).
- The v76 pin (tests/e2e/dashboard.spec.ts): the breakdown card's
  income-SECTION ICON CHIP glyph + the donut label chrome census at 1280 —
  the never-pinned axes (the section icon's 16x16 twin-polyline
  glyphSig/color rgb(143,188,63)/viewBox 0 0 24 24 + its h-8 w-8 chip
  32x32/radius 8px/rgba(143,188,63,0.125) + the donut label count 4/fs
  16px/fill rgb(0,0,0)/sectors 3/labelLineCount 0), with the precise
  section-button finder. GREEN on first run. The pin-sanity mutation (the
  section icon's h-4 w-4 → h-5 w-5 at dashboard-view.tsx:316) verified to
  FAIL at exactly the sectionIcons axis (the empty array at 20x20), then
  restored (the standalone REBUILD as a SEPARATE command; git diff src/ =
  0 lines).

**The v76 findings:**

1. PAIR 1 (the networth view at 1280) — two style flags, both documented
   classes (the Base44 FAB + the avatar letter, which the VLM misread as
   "P" on the clone — the census says "D"). The PART B census — the
   summary card's full HEIGHT family — byte-identical on every axis with
   ZERO drift since the v67 pin: the card 960x333/32px/16px/gradient/
   shadow, the headRow 76/mb 32, the label 14/80-white/mb 8/h 20, the
   figure 48/700/white/lh 48/h 48, the medallion 64x64/icon 32, the
   statGrid 440px 440px/rows 84/gap 16, the statTile 440x84/pad 16/
   radius 12/white-10/blur(10)/label 12/h 16/mb 4/amount 24/700/h 32,
   the ratioFooter mt 24/pt 24/1px/white-20/h 53/14/18/700. The
   labelBlock width 304-vs-357 is the figure-text-length data class.
2. PAIR 2 (the drill-down EXPANDED at 1280) — six flags, every one
   DOM-arbitrated to a documented class: the nav highlight the v56
   root-URL class (bg TRANSPARENT both sides; the delta the clone's
   white/500 vs the reference's zinc-600/400); the progress fill the pct
   × 568 data class (the track chrome byte-identical; fillW 173 vs 357);
   the donut labels the v60 perception class (the label chrome
   byte-identical — count 4/16px/black/3 sectors/0 lines — the
   reference's first label element carries the three texts concatenated,
   the clone's distributed: a recharts label-grouping DOM artifact); the
   extra rows + footer + stat counts the seed-data classes; the tooltip
   the Base44 platform chrome. The stat trend icons + the hero trend
   glyph row byte-identical (the v67 axes, no drift).
3. The screenshots 16/16 byte-identical — the seventh consecutive
   fully-identical set (the same-day regeneration, no calendar rollover
   since the v75 re-baseline).

**The v76 lessons:**
1. THE F0 LESSON (the standalone static copy): `npx next build` alone does
   NOT produce a servable standalone — package.json's `build` script is
   `next build && cp -r .next/static .next/standalone/.next/ && cp -r
   public .next/standalone/`, and the bare build leaves the standalone
   404ing every `/_next/static/chunks/*` request: the server renders the
   HTML shell but the client never hydrates, boot() never runs, and every
   hydration-dependent assertion burns its full 10s expect timeout (a
   "slow suite" that is really a 404 loop). The F0 build step must run
   `npm run build`, and a boot-failure-style stuck-at-Loading page with a
   fast /api/health is the fingerprint of the missing static copy.
2. THE FINDER-DESCRIPTION LESSON: the v67/v76 arbitration's "stat-card
   footer trend icon" label was a MISNOMER — its width-200-500 "Total
   Income" finder matches the BREAKDOWN SECTION ROW first in the DOM on
   BOTH sites (the actual stat tiles match second/third), and THAT row's
   icon chrome is what measured byte-identical all along. Name a census's
   finder by what it actually resolves to (dump the matched element's
   text when in doubt), and when a pin-sanity mutation FAILS TO FAIL,
   debug the finder before touching the pin — the first v76 mutation
   (the hero-stat-tile trend icon, dashboard-view.tsx:619) stayed GREEN
   because the pin never measured that icon; the corrected mutation (the
   section icon at :316) failed at exactly the pinned axis.

## v77 — the re-run cycle's next-oldest candidate (the v61-era dashboard pair's second re-run) + the Budget Guidelines interior-text family + quick-action icon viewBox pin (PIN-ONLY)

The session-183 v77 cycle: the re-run cadence rotating past the v76
networth+drill-down pair to the next-oldest candidate — the v61-era pair
(the dashboard FULL-PAGE at desktop 1280, last re-shot v68) — plus the
axe watch at its re-check point, the 71st standing checks, and the
target-selection correction (the v76 plan's v77 queue named the mobile
390 twins [last re-shot v69], but the cadence's own oldest-first rule —
the v74 "OLDEST candidate" convention, ordering by LAST RE-SHOT DATE —
points at the v61-era pair [v68 < v69]; the mobile twins become the v78
candidate).

**The probes:**
- `vlm-shots-v77.sh` — the reference side: the DASHBOARD at desktop
  1280x800 FULL-PAGE (the login-retry loop; the parked pointer at
  (5,5); read-only — the v46 rule).
- `clone-vlmshots-v77.sh` — the clone side, the same shot inside
  with-server.sh (the :3200 standalone parity server).
- `vlm-compare-v77.mjs` — the VLM pairwise (the v68 prompt lineage —
  the guidelines + quick-action focus).
- `arbit-v77.sh` — the both-sides DOM census (the v75 convention: the
  IDENTICAL verdict's census, the v61 qa-census axes re-measured): PART
  G (the guidelines card: the card/header/body/tiles with the
  label/pct/desc chrome), PART Q (the quick-action row: the grid/cards
  with the tile/icon/label/plus chrome + the icons' viewBox), PART X
  (the cross-row gap) + the seedcheck at the end.
- `ref-standing-v71.sh` / `standing-checks-v71.sh` — the 71st standing
  checks (version-bumped from v70).
- The v77 pin (tests/e2e/dashboard.spec.ts): the Budget Guidelines
  card's interior-TEXT family + the quick-action icons' viewBox census
  at 1280 — the never-pinned axes (the header's lh 16px + tracking
  -0.4px, the tiles 2/3 chrome, ALL three tiles' label/pct/desc text
  chrome at 1280 [the v51 F4 family's desktop twin], the icons'
  viewBox [the v76 glyph family's extension]). GREEN on first run. The
  pin-sanity mutation (the tile label's font-medium -> font-normal at
  dashboard-view.tsx:848) verified to FAIL at exactly the three tiles'
  label.fw axes (fw 500->400), then restored (the standalone REBUILD as
  a SEPARATE command; git diff src/ = 0 lines).

**The v77 findings:**

1. The VLM verdict **IDENTICAL, ZERO style flags** — the LAYOUT/STYLE
   section explicitly empty (the guidelines card + the quick-action
   cards visually identical on every axis); every reported delta a
   documented data/identity class (the seed figures, the v56 root-URL
   active-nav, the avatar letter). Matches the v68 re-run's own
   IDENTICAL verdict — zero drift since v68 on the VLM layer.
2. The both-sides census byte-identical on every axis with ZERO drift
   since v61: the guidelines card 468x348 (the STRETCH-fix natural
   height holding 16 iterations later), the header
   24px/16px/600/forestDark/lh 16px/tracking -0.4px, the three tiles
   418x78 with the tint+border pairs + label 16/500/type + pct
   14/400/type + desc 12/gray/lh 16px; the quick-action grid
   960/3x304/gap 24, the cards 304x90/16px/24px, the tiles 40x40, the
   icons 20x20 + viewBox 0 0 24 24, the plus 16/0.5. The three deltas
   all documented classes: the card shadow's transparent lead layers
   (the v66 computed-form class — the visible layers byte-identical);
   the quick-action label's fw/color under the census's bare finder
   (the v61 wrapper-vs-leaf lesson — the v61 F3 pin's LEAF finder
   measures the leaf byte-identical); the grid mt 0-vs-32px (the
   margin-structure class — the rendered cross-row gap 340
   byte-identical on BOTH sides, cardBottom 1122/gridTop 1462).
3. The screenshots 16/16 byte-identical — the eighth consecutive
   fully-identical set (the same-day regeneration, no calendar
   rollover since the v75 re-baseline).

**The v77 lessons:**
1. THE TARGET-SELECTION LESSON: verify a queue suggestion against the
   rotation ledger before executing it — the v76 plan's v77 queue named
   the mobile 390 twins (last re-shot v69) while the ledger's own
   oldest-first rule pointed at the v61-era pair (last re-shot v68).
   A queue suggestion is a hint, not a commitment; the ledger is the
   truth.
2. THE v61 WRAPPER-VS-LEAF LABEL LESSON re-confirmed live: the
   quick-action label's WRAPPER span still reads fw 400/rgb(10,10,10)
   under a bare textContent finder while the reference's first match is
   the leaf (fw 500/rgb(26,58,46)) — the DOM shapes differ, the leaf
   chrome does not. Keep pinning the LEAF (the exact text + zero
   element children), and expect the wrapper delta to reappear in any
   census that forgets the finder discipline.

## v78 — the mobile 390 twins' second re-run + the breakdown card's
## mobile svg + chart-absence + width pin (session-186)

The session-185 v78 cycle: the re-run cadence rotating to the
next-oldest candidate — the mobile 390 twins (the networth + dashboard
full-page pair, last re-shot v69) — plus the axe watch at its re-check
point (NO DRIFT — only a 5.x wrapper changes the calculus, the
engine-contract pin guarding the toolchain), the 72nd standing checks,
and the ledger-verified queue (the v77 plan's v78 suggestion agreeing
with the rotation ledger this time: v69 < v70 items < v74-v77, the
oldest remaining by LAST RE-SHOT DATE — the v77 target-selection lesson
applied: the queue suggestion verified against the ledger before
commitment, no correction needed).

**The probes:**
- `vlm-shots-v78.sh` — the reference side: BOTH mobile 390x844
  full-page twins (the login-retry loop; the parked pointer at (5,5);
  read-only — the v46 rule).
- `clone-vlmshots-v78.sh` — the clone side, the same shots inside
  with-server.sh (the :3200 standalone parity server).
- `vlm-compare-v78.mjs` — the VLM pairwise (the v69 prompt lineage —
  the networth + dashboard mobile focus).
- `arbit-v78.sh` — the both-sides DOM census (the v75 convention: the
  census runs regardless of the verdict; the v69 census axes
  re-measured): the networth summary-card family (the card/stat
  grid/tiles/medallion/trend icon) + the dashboard subtitle wrap (the
  Range-walk line bucketing) + the breakdown/spending cards' chart
  census (the recharts-wrapper/pie-sector counts).
- `ref-standing-v72.sh` / `standing-checks-v72.sh` — the 72nd standing
  checks (version-bumped from v71).
- The v78 pin (tests/e2e/dashboard.spec.ts): the Net Zero Breakdown
  card's mobile svg family + chart-absence + width census at 390 — the
  never-pinned axes (the card w 358 [the v44 F2a pin covers the heights
  only], the svg family svgCount 7 with the full size census
  [16,14,16,14,16,14,16], the chart-absence contract rechartsWrappers 0
  + pieSectors 0 [the v69 donut-invention lesson's regression guard],
  the children's width family H3 308x20 + DIV 308x238). GREEN on first
  run. The pin-sanity mutation (the collapsed section chevron's
  h-3.5 w-3.5 -> h-4 w-4 at dashboard-view.tsx:339) verified to FAIL at
  exactly the three chevron axes (14 -> 16, the section row h 48
  governed by the 32px chip), then restored (the standalone REBUILD as
  a SEPARATE command; git diff src/ = 0 lines).

**The v78 findings:**

1. BOTH mobile twins' VLM verdicts DIFFERENT with every flag a
   documented class — the networth pair: the stat tiles side-by-side
   (ref) vs stacked (clone) the v41 mobile-superset class; the asset
   groups the seed-data class; the "Edit with Base44" overlay the
   platform chrome; the avatar the user-identity class (matching the
   v69 re-run's own flag set exactly). The dashboard pair: the subtitle
   wrap point the v62 width-delta class; the progress-bar length the
   pct data class; the black tooltip the Base44 platform chrome; the
   donut proportions the seed-data class.
2. The both-sides census — the chrome BYTE-IDENTICAL on every axis
   with zero drift since the v69/v63 censuses: the networth medallion
   64x64 + trend icon 32x32 + tiles h 84 + grid gap 16px (the deltas
   all the v41 mobile-superset class: the reference's card 432/docSW
   464/fixed 2-col tiles 176x84/medallion clipping at right 416 vs the
   clone's card 358/docSW 390/1-col tiles 294x84/medallion fitting at
   right 342); the dashboard subtitle chrome (fs 16/fw 400/
   rgb(107,114,128)/lh 24px, the P h 48, the block h 92, 2 lines) +
   the breakdown card's h 324 + svgCount 7 + the first-four svgs
   [16x16, 14x14, 16x16, 14x14] + rechartsWrappers 0 + pieSectors 0 on
   BOTH sides (no donut in the breakdown card anywhere — the v69
   disproof class); the 5px width family delta (card 363 vs 358, H3
   313 vs 308, DIV 313x238 vs 308x238) the reference's own docSW-395
   overflow class (the heights byte-identical).
3. The screenshots 16/16 byte-identical — the ninth consecutive
   fully-identical set (the same-day regeneration, no calendar
   rollover).

**The v78 lessons:**
1. THE LEDGER-VERIFIED QUEUE: when the queue suggestion and the
   rotation ledger agree, say so explicitly in the plan (the v77
   target-selection lesson's positive case — the verification step ran
   the same way, the outcome was agreement; the discipline is the
   check, not the correction).
2. The v69 chart-presence lesson now has its regression guard: the
   breakdown card's rechartsWrappers/pieSectors counts are PINNED at
   390 — the VLM's invented-donut class can no longer resurface
   un-arbitrated in a future re-run (the pin fails if a chart ever
   appears in the breakdown card).

## v79 — the v57-era items pair's third re-run + the rail-avatar /
## amount-accent / card-height pin (session-188)

The session-187 v79 cycle: the re-run cadence rotating to the
next-oldest candidate — the v57-era items pair (the income + expenses
view pair at desktop 1280, last re-shot v70 — the pair's THIRD re-run
[v57 → v64 → v70 → v79], the cadence's most-re-verified desktop
surface) — plus the axe watch at its re-check point (NO DRIFT — only a
5.x wrapper changes the calculus, the engine-contract pin guarding the
toolchain), the 73rd standing checks, and the ledger-verified queue
(the v78 plan's v79 suggestion agreeing with the rotation ledger:
v70 items < v74 savings < v75 login+calculator < v76 networth+drill-down
< v77 dashboard < v78 mobile twins — the oldest remaining by LAST
RE-SHOT DATE; the v77 target-selection lesson applied: the queue
suggestion verified against the ledger before commitment, no
correction needed — the second consecutive agreement).

**The probes:**
- `vlm-shots-v79.sh` — the reference side: BOTH items views at desktop
  1280x800 FULL-PAGE (the login-retry loop; the parked pointer at
  (5,5); read-only — the v46 rule).
- `clone-vlmshots-v79.sh` — the clone side, the same shots inside
  with-server.sh (the :3200 standalone parity server).
- `vlm-compare-v79.mjs` — the VLM pairwise (the v70 prompt lineage —
  the items focus).
- `arbit-v79.sh` — the both-sides DOM census (the v75 convention: the
  census runs regardless of the verdict; the v70 census axes
  re-measured on BOTH views): the sidebar avatar (the v70b round
  1-2-char finder) + the item grid + the first card (w AND h) + the
  titleRow + the AMOUNT leaf (the ≥20px-font P — the never-pinned
  axis) + the footer + the badge row + the filter card (both variants)
  + the header + the docSW guard.
- `ref-standing-v73.sh` / `standing-checks-v73.sh` — the 73rd standing
  checks (version-bumped from v72).
- The v79 pin (tests/e2e/items.spec.ts): the rail-avatar's full chrome
  + the item-card amount leaf's per-type accent family + the income
  view's first-card HEIGHT at 1280 — the never-pinned axes (the
  avatar's w 36/h 36/radius 9999px/fs 14px/fw 600/color white/bg
  rgb(143,188,63) [the tokens.spec pin holds the radius only]; the
  amount's 24px/700/lh 32px/h 32 with the income lime + expenses
  orange accents [the v74 pin holds the savings variant only —
  completed to all three types]; the income first card's h 230 [the
  v70b wrap/stretch arithmetic regression guard: the Salary sibling's
  Recurring-wrap natural 230 + the 1-row grid stretching the Freelance
  card]). GREEN on first run. The pin-sanity mutation (the avatar's
  font-semibold -> font-medium at sidebar.tsx:120) verified to FAIL at
  exactly the avatar.fw axis (600 -> 500), cascade-free (the
  tokens.spec radius pin + the boot-failure shell pin verified GREEN
  under the mutation), then restored (the standalone REBUILD as a
  SEPARATE command; git diff src/ = 0 lines).

**The v79 findings:**

1. BOTH items views' VLM verdicts DIFFERENT with every flag a
   documented class — the income pair: the avatar letter the
   user-identity class; the 1-card vs 2-card grid the seed-count
   class; the figures the seed-data class. The expenses pair: the
   footer's payment-method chips the v57 DATA-CONDITIONAL class; the
   badge arrangement the v57 Recurring superset wrap class; the avatar
   the user-identity class (matching the v70 re-run's own flag set
   exactly — zero drift on the flag-class layer nine iterations
   later).
2. The both-sides census — the chrome BYTE-IDENTICAL on every axis
   with zero drift since the v70 census: the AVATAR (36x36 / 9999px /
   14px / 600 / white / rgb(143,188,63) — the identity text the only
   delta); the GRID + CARD (960 / 16px / the 3-col template; 309 /
   20px / 12px / rgb(229,231,227) — the card h 200-vs-230 the
   v70b-decomposed class: the Recurring superset wrap h 52 → +30px +
   the 1-row sibling stretch); the AMOUNT leaf (24/700/lh 32/h 32 with
   the per-type accents); the FOOTER + BADGE chrome; the FILTER CARD
   on both variants (the income 447-spanning + the expenses
   216-not-spanning — the v64/v70 pins' own values); the header; the
   docSW 1280 on both views.
3. The screenshots 16/16 byte-identical — the tenth consecutive
   fully-identical set (the same-day regeneration, no calendar
   rollover).

**The v79 lessons:**
1. The reference session's mid-script expiry hit the F2 data census
   this time (the income leg read "no match" — the /income redirect
   landed on /login): the census re-read after a fresh login-retry
   recovered the exact documented values. The standing pattern
   generalizes: ANY multi-eval reference flow should treat a "no
   match"/empty census as a possible EXPIRY first (re-login + re-read)
   before suspecting drift — the v75 cold-session lesson's expiry
   twin.
2. The v70b card-height lesson now has its regression guard: the
   income view's first-card HEIGHT 230 is pinned at 1280 — the
   wrap/stretch arithmetic (the Recurring superset badge's 52px wrap +
   the 1-row grid stretching the shorter sibling) can no longer
   silently regress (a broken wrap or a broken stretch both flip the
   pin).

## v80 — the v58-era savings pair's third re-run + the savings
## goal-card's double-wrap heights / title-row geometry / border-bg pin
## (session-190)

The session-189 v80 cycle: the re-run cadence rotating to the
next-oldest candidate — the v58-era savings pair (the savings view at
desktop 1280, last re-shot v74 — the pair's THIRD re-run [v58 -> v65 ->
v74 -> v80], now the oldest remaining candidate [v74 < v75 < v76 < v77
< v78 < v79]) — plus the axe watch at its re-check point (NO DRIFT —
only a 5.x wrapper changes the calculus, the engine-contract pin
guarding the toolchain), the 74th standing checks, and the
ledger-verified queue (the v79 plan's v80 suggestion agreeing with the
rotation ledger — the third consecutive agreement).

**The probes:**
- `vlm-shots-v80.sh` — the reference side: the savings view at desktop
  1280x800 FULL-PAGE (the login-retry loop; the parked pointer at
  (5,5); read-only — the v46 rule).
- `clone-vlmshots-v80.sh` — the clone side, the same shot inside
  with-server.sh (the :3200 standalone parity server).
- `vlm-compare-v80.mjs` — the VLM pairwise (the v74 savings-view
  prompt lineage).
- `arbit-v80.sh` — the both-sides /savings DOM census (the v75
  convention: the census runs regardless of the verdict; the v74
  census axes re-measured PLUS the v80 titleRow geometry — the h4's
  parent row + the category dot, the never-census'd axis): the header
  + the grid + the first card (w AND h AND border AND bg) + the
  titleRow + the h4 + the amount + the footer + the badge row + every
  badge + the docSW guard.
- `vlm-arbit-v80.mjs` — the screenshot DATE-class diff crops'
  visual arbitration (the v66/v75 discipline's crop variant: the
  changed region pairs [baseline above, fresh below] verified
  DATE-TEXT-ONLY with identical chrome).
- `ref-standing-v74.sh` / `standing-checks-v74.sh` — the 74th standing
  checks (version-bumped from v73).
- The v80 pin (tests/e2e/items.spec.ts): the savings goal-card's
  double-wrap heights + title-row geometry + border/bg at 1280 — the
  never-pinned axes (the savings view's card HEIGHTS [230, 230] — the
  DOUBLE-WRAP twins, both cards carrying 4 badges wrapping their rows
  to 52px [the v58 pin holds w/pad/radius only, the v79 pin the income
  view's stretch twin]; the titleRow's geometry flex/8px/center/h 24/
  the 8x8 dot at 9999px in the savings blue rgb(59,126,161) [the 1280
  state of the v51/v54 390-only family — the v45 F1a pin's income
  lime-dot twin completed]; the card's border 1px solid
  rgb(229,231,227) + bg white [the v45 F1a income family's savings
  twin]). GREEN on first run. The pin-sanity mutation (the titleRow's
  lg:items-start at item-card.tsx:120) verified to FAIL at exactly the
  titleRow.alignItems axis ("center" -> "flex-start") — cascade-free
  by construction (the responsive variant inert at 390 — the v51/v54
  family untouched; the v45 F1a pin asserts no alignItems; the row
  height content-governed — the full items.spec.ts under the mutation:
  36 green, only the v80 pin red), then restored (the standalone
  REBUILD as a SEPARATE command; git diff src/ = 0 lines).

**The v80 findings:**

1. The savings verdict DIFFERENT with every flag a documented class —
   the seed-count grid (1 vs 2 cards), the v58 DATA-CONDITIONAL footer
   chips, the classification-VALUE badges, the Recurring superset, the
   seed-data figures, the user-identity avatar — matching the v74
   re-run's own flag set exactly (zero drift on the flag-class layer
   six iterations later).
2. The both-sides census — the chrome BYTE-IDENTICAL on every axis
   with zero drift since the v74 census: the GRID + CARD (960 / 16px /
   the 3-col template; 309 / 20px / 12px / 1px solid rgb(229,231,227)
   / white — the card h 200-vs-230 the v70b-decomposed class); the
   TITLE ROW (the new axis: flex / 8px / center / h 24 / the 8x8 dot
   at 9999px in rgb(59,126,161)); the INTERIOR TEXT (the h4
   16/600/lh 24; the amount 24/700/lh 32 in the savings blue); the
   FOOTER + BADGE chrome; the docSW 1280.
3. The fresh-reclone F0: the workspace reset path exercised for the
   first time since v76 — node_modules + chromium-1243 reinstalled,
   .env rewritten, db:push + db:seed re-run, the seedcheck exact, and
   the baseline chain fully green as-shipped on the rebuilt workspace
   (282 e2e pre-pin).
4. The screenshots 10/16 byte-identical + 6/16 DATE-class
   pixel-arbitrated: the fresh seed's isoDate() offsets resolve against
   the re-clone's seeding day (a +1-day shift on the date texts), the
   chrome byte-identical — every diff crop VLM-arbitrated
   DATE-TEXT-ONLY (03-income / 04-expenses / 05-savings / 06-networth
   / 08-calculator / 16-item-details, all confined to the date-bearing
   text bands).

**The v80 lessons:**
1. THE VIEWPORT-SCOPED CASCADE-FREE MUTATION: a per-view completion
   pin whose every axis is sibling-pinned (the shared-component
   reality — the titleRow/dot/border axes all held on other views or
   viewports) gets its cascade-free sanity via a RESPONSIVE variant:
   lg:items-start flips the 1280 axis while the 390 family stays green
   — the mutation scoped by viewport, not by component.
2. THE STRETCH-TWIN ATTRIBUTION CORRECTION: the v70b "shorter sibling
   stretched" mechanism holds, but WHICH sibling is stretched is a
   per-view fact — the items-start experiment (measure the naturals
   with the stretch off) is the probe that settles it. The income
   view's FIRST card (Salary, natural 200) is the stretched one; the
   savings view's two cards are BOTH natural wrap twins. Probe before
   writing the attribution into a pin's comment.
3. THE FRESH-SEED DATE SHIFT: a re-clone's db:seed shifts every
   isoDate() field by the seeding-day delta — expect DATE-class
   screenshot diffs after any workspace reset, and pixel-arbitrate
   them (crop pairs, DATE-TEXT-ONLY verdicts), never a full-page VLM
   verdict.


## v81 — the login + calculator pair's third re-run (the preserved workspace)

The v81 iteration (docs/remediation-plan-v81.md): the re-run cycle's
next-oldest candidate — the ledger-verified queue (the v80 plan's v81
suggestion AGREEING with the rotation ledger: the v59-era login +
calculator pair [the login view + the calculator dialog at desktop
1280], last re-shot v75, the oldest remaining by LAST RE-SHOT DATE
[v75 < v76 < v77 < v78 < v79 < v80]; the pair's THIRD re-run [v59 ->
v66 -> v75 -> v81] — the FOURTH consecutive queue/ledger agreement),
plus the axe watch at its re-check point (NO DRIFT — 4.14.0, no 5.x,
the v68 dedupe holds) and the 75th standing checks (ref-standing-v75.sh
+ standing-checks-v75.sh, version-bumped from v74 — version-bump-only
diffs verified).

The probe series (the v75 lineage, version-bumped):
- vlm-shots-v81.sh + login-shots-v81.sh — the REFERENCE side (login
  on the first attempt; the calculator via the Rent-card hover +
  Calculate click; the parked pointer at (5,5); read-only).
- clone-vlmshots-v81.sh + clone-login-shots-v81.sh — the CLONE side
  (the with-server :3200 parity server; the calculator twin adds the
  matching "Contents Insurance" $25 monthly line item through the real
  UI then FULLY restores the fixture — the delete + Rent's $1850
  re-edit + the "$2235.00" page-total verify).
- vlm-compare-v81.mjs — the VLM pairwise (the login twin IDENTICAL
  with zero style flags; the calculator twin DIFFERENT with three
  flags, every one DOM-arbitrated to a documented class).
- arbit-v81.sh + login-census-ref-v81.sh — the both-sides census (the
  v75 axes re-measured: the panel/scrim/title/desc/close/totalCard/
  nameH4/row/pillRow/pill1/amountP/addBtn chrome all BYTE-IDENTICAL;
  the login census re-run after the cold-session race).

The findings:
1. The LOGIN pair: IDENTICAL, zero style flags — zero drift since v75
   on the VLM layer. The both-sides census byte-identical on every
   axis; the card's 0px-width border computed-color (the ref's
   slate-200 form vs the clone's border token) and the shadow's
   transparent lead-layer count are the v66 computed-form INVISIBLE
   class.
2. The CALCULATOR pair: DIFFERENT with three flags — (a) the
   "extra will-update line" the v66 DATA-CONDITIONAL class
   (hasWillUpdateSpan ref false [its Rent natively $25.00 === its
   line-item total] vs clone true [opened-at $1850]); (b) the "hover
   action buttons missing in the clone" the POINTER-POSITION
   perception class — the reference's shot is taken with the pointer
   still inside the dialog after the Calculate click, the clone's
   after the parked-pointer move: the DOM census (actionsAtRest
   opacity 0 / btnCount 2) is BYTE-IDENTICAL on both sides; (c) the
   "row height shorter in the clone" a VLM MISREAD — the row measures
   720x102 BYTE-IDENTICAL on both sides.
3. NO NEW GAP — the iteration is PIN-ONLY: the calculator dialog's
   header family + Add Item button + scrim census at 1280 (the
   never-pinned axes: the title's typography [18px/700/lh 28px/
   rgb(26,58,46) — the v53 390 pin's {fs,fw,color} twin completed
   with the never-pinned lh], the desc's family [14px/lh 20px/
   rgb(107,114,128) — the v73 390 family's desktop twin], the
   addBtn's chrome [110x32/radius 6px/12px/500/white — the radius
   never pinned at any viewport], the scrim [rgba(26,58,46,0.5)/
   blur(8px)/1280x800 — the v73 390 family's desktop twin]) — every
   pinned axis STATIC dialog chrome, the pin riding the v59 read-only
   EMPTY-state discipline (hover -> Calculate -> census -> Close, no
   fixture writes). The pin-sanity mutation: the DialogTitle's
   lg:text-xl (calculator-dialog.tsx:127) FAILS at exactly the
   title.fs axis ("18px" -> "20px") — cascade-free by construction
   (inert at 390 — the v53 h2/header pins untouched; the v59 pin
   asserts no title-dependent axis, the panel.y invariant holds for
   any height; the v66 height family lives in the panel body; the
   full calculator.spec.ts under the mutation: 15 green, only the
   v81 pin red).
4. The screenshots 16/16 BYTE-IDENTICAL — the twelfth consecutive
   fully-identical set (the same-day regeneration against the
   preserved db, no calendar rollover; the seedcheck exact).

**The v81 lessons:**
1. THE STATIC-CHROME READ-ONLY PIN: a dialog pin whose every axis is
   static chrome (title/desc/addBtn/scrim — none data-dependent) can
   ride the read-only EMPTY state, eliminating the fixture
   add/restore burden of the with-row pins (the v66/v73 discipline)
   — the empty state measures the same values the 1-row census
   measured.
2. THE POINTER-PHASE PERCEPTION CLASS: a screenshot pair taken at
   different pointer phases (pre-park vs post-park) makes
   hover-revealed chrome appear on one side only — the DOM census
   (actionsAtRest opacity) is the arbiter, not the pixels.
3. THE 0px-WIDTH BORDER COMPUTED-COLOR: a borderless surface's 0px
   border still carries a computed color (the ref's slate-200 form vs
   the clone's border token) — an INVISIBLE computed-form class,
   never a parity gap.

The v82 queue (suggestions — verify against the rotation ledger
before executing): (1) the re-run cadence rotates to the next-oldest
candidate after this pair (the v60-era networth + drill-down pair
[the networth view + the dashboard drill-down EXPANDED at 1280], last
re-shot v76 — now the oldest remaining), (2) the axe-core watch at
its next re-check point (only a 5.x wrapper changes the calculus),
(3) the deferred reference-write censuses (unchanged — out of bounds
under the v46 read-only rule).

## v82 — the networth + drill-down pair's third re-run (the rebuilt workspace)

The v82 iteration (docs/remediation-plan-v82.md): the re-run cycle's
next-oldest candidate — the ledger-verified queue (the v81 plan's v82
suggestion AGREEING with the rotation ledger: the v60-era networth +
drill-down pair [the networth view + the dashboard drill-down EXPANDED
at desktop 1280], last re-shot v76, the oldest remaining by LAST
RE-SHOT DATE [v76 < v77 < v78 < v79 < v80 < v81]; the pair's THIRD
re-run [v60 -> v67 -> v76 -> v82] — the FIFTH consecutive queue/ledger
agreement), plus the axe watch at its re-check point (NO DRIFT —
4.14.0, no 5.x, the v68 dedupe holds) and the 76th standing checks
(ref-standing-v76.sh + standing-checks-v76.sh, version-bumped from
v75 — version-bump-only diffs verified).

The probe series (the v76 lineage, version-bumped):
- vlm-shots-v82.sh — the REFERENCE side (login on the first attempt;
  the drill-down expanded via the Total Income section + first
  category clicks; the parked pointer at (5,5); read-only — the v46
  rule).
- clone-vlmshots-v82.sh — the CLONE side (the with-server :3200 parity
  server; the same expansion clicks; no fixture writes).
- vlm-compare-v82.mjs — the VLM pairwise (the networth twin IDENTICAL
  with the only style flag the Base44 overlay; the drill-down twin
  DIFFERENT with eight flags, every one DOM-arbitrated to a documented
  class).
- arbit-v82.sh — the both-sides census (the v76 axes re-measured:
  PART A the drill-down census [nav highlight, avatar, progress fill,
  donut labels, stat trend icons], PART B the networth summary-card
  family; the census runs regardless of the verdict — the v75
  convention).
- stat-title-ref-v82.sh — the dedicated DOM arbitration for the VLM's
  "Total Expense vs Total Expenses" flag: the reference's statTitles
  measured VERBATIM (SPAN + H3 both: "Total Income"/"Total Savings"/
  "Total Expenses" at 14px/500/rgb(107,114,128); hasSingular:false,
  hasPlural:true) — the MISREAD disproven in one probe.

The findings:
1. The NETWORTH pair: IDENTICAL — the only layout/style flag the
   reference's "Edit with Base44" overlay (the platform-chrome
   class); every other delta the seed classes (the figures, the
   1-asset vs 3-asset groups, the ratio). The PART B census
   byte-identical on every chrome axis (the card/head row/label/
   figure/medallion/stat grid/stat tile/ratio footer families); the
   ONE width delta — the labelBlock w ref 304 vs clone 357 — the
   DATA-CONDITIONAL width class (the 48px figure's text length:
   "$25,000.00" vs "-$245,950.00"; the heights byte-identical).
2. The DRILL-DOWN pair: DIFFERENT with eight flags, every one
   DOM-arbitrated to a documented class — (a) the nav highlight the
   v56 SUPERSET class (the reference's link INERT rgb(63,63,70)/400
   vs the clone's ACTIVE white/500); (b) the progress-bar length the
   pct x 568 DATA class (fillW ref 173 vs clone 357 on the
   byte-identical 568x12 track — the v60 arbitration's own values
   REPRODUCED EXACTLY, zero drift since v60); (c) the extra expanded
   category + the footer count the seed-data class (the clone's 2
   income categories vs the reference's 1); (d) the donut proportions
   the seed-data class; (e) the percentage-labels claim the v60
   PERCEPTION class re-arbitrated live (the reference DOES render its
   labels — the census's own texts 92.3%/4.6%/3.1%, count 4 = 1 group
   + 3 labels, 0 lines, 16px, black, 3 sectors — the chrome
   byte-identical, the texts each site's own data); (f) the "Total
   Expense vs Total Expenses" a VLM MISREAD (the stat-title probe:
   the plural on BOTH sides, measured verbatim); (g) the avatar the
   user-identity class; (h) the Base44 overlay the platform-chrome
   class.
3. NO NEW GAP — the iteration is PIN-ONLY: the networth summary
   card's COMPLETION family at 1280 (the never-pinned axes: the head
   row's ALIGNMENT [items center — the v80 titleRow.alignItems
   pattern's networth twin; the v67 pin holds the row's h/mb/display],
   the label block's HEIGHT [76 — the min-w-0 wrapper's own height],
   the stat grid's content-box WIDTH [896 — the 960 card - the 2x32
   pad arithmetic twin], the ratio label's TYPOGRAPHY [fs 14px — G9
   holds the color, the structure test the VALUE's 18px/700 + the
   tile label's 12px + the footer border's rgba — never the label's
   own font-size]) — every pinned axis STATIC chrome (the
   labelBlock's WIDTH is the data-conditional axis, EXCLUDED); the
   pin-sanity mutation the ratio label's text-sm -> text-sm
   lg:text-base (viewport-scoped; the value-governed ratio row keeps
   the v67 footer h 53 green — cascade-free: 26 green under the
   mutation, only the v82 pin red).
4. The screenshots 16/16 BYTE-IDENTICAL — the thirteenth consecutive
   fully-identical set (the same-day seed + the same-day shots
   reproducing the committed set byte-for-byte; the seedcheck exact).

**The v82 lessons:**
1. THE VERBATIM-TITLE MISREAD DISPROOF: a VLM flag that claims a TEXT
   difference ("Total Expense" vs "Total Expenses") is cheapest to
   disprove with a dedicated verbatim-DOM probe (the exact strings,
   their tags, and their typography measured on the live reference) —
   one probe settles what pixel-cropping never could; the v43
   misattribution rule's text-twin.
2. THE CENSUS-ARITHMETIC REPRODUCTION: when a re-run's data-class
   delta reproduces a PRIOR arbitration's exact values (the fillW 173
   vs 357 = the v60 numbers, five re-runs later), cite the
   reproduction explicitly — it is the strongest possible
   no-drift evidence for the standing chrome.
3. THE SAME-DAY-SEED BYTE-IDENTITY: a fresh seed planted and shot on
   the same calendar day reproduces the committed screenshot set
   byte-for-byte — the v80 date-shift lesson's converse: the date
   bands shift ONLY when the seed day and the shot day differ.

The v83 queue (suggestions — verify against the rotation ledger
before executing): (1) the re-run cadence rotates to the next-oldest
candidate after this pair (the v61-era dashboard pair [the dashboard
FULL-PAGE at desktop 1280], last re-shot v77 — now the oldest
remaining), (2) the axe-core watch at its next re-check point (only a
5.x wrapper changes the calculus), (3) the deferred reference-write
censuses (unchanged — out of bounds under the v46 read-only rule).

## v83 — the dashboard pair's third re-run (the rebuilt workspace)

The third reset-boundary workspace (git clone at main @ 7b28990, the v82
shipped state + the session_195 transcript): node_modules reinstalled
(354 packages), chromium-1243 reinstalled, `.env` rewritten
(DATABASE_URL=file:../db/custom.db, db/ at the repo root), db:generate +
db:push + db:seed re-run, the seedcheck exact before any flow. The
baseline chain FULLY GREEN as-shipped (lint -> typecheck -> 108 unit ->
build -> 285 e2e [101+108+78 chunk executions = 287 total] -> 35/35
smoke — the exact documented v82 state). The queue: the v82 plan's v83
suggestion — the v61-era DASHBOARD pair (the FULL-PAGE at desktop
1280, last re-shot v77, now the oldest remaining [v77 < v78 < v79 <
v80 < v81 < v82]) — agreeing with the rotation ledger (the SIXTH
consecutive agreement); the pair's THIRD re-run (v61 -> v68 -> v77 ->
v83).

**The probes:**
- ref-standing-v77.sh + standing-checks-v77.sh — the 77th standing
  checks (version-bumped from v76 — version-bump-only diffs): the
  mobile menu verified working the 77th consecutive time; the
  reference's four bugs ALL live; the data census the 77th clean drift
  check; the SEO pair live on both sides.
- vlm-shots-v83.sh + clone-vlmshots-v83.sh + vlm-compare-v83.mjs —
  the re-run pair (login on the first attempt both sides, the parked
  pointer at (5,5), read-only on the reference): the DASHBOARD verdict
  IDENTICAL — the two v61-era target surfaces (the Budget Guidelines
  card + the quick-action row) identical on every reported chrome
  axis; the only deltas the seed classes + the v56 SUPERSET nav class
  + the user-identity avatar + the platform-chrome overlay.
- arbit-v83.sh — the both-sides census (the v77 axes re-measured; the
  v75 convention: the census runs regardless of the verdict): the v77
  census values REPRODUCED EXACTLY — zero drift since v77 on every
  axis (PART G the guidelines card byte-identical modulo the v66
  transparent-shadow class; PART Q the quick-action row byte-identical
  modulo the v77 mt-mechanism class [ref mt 0 vs clone 32px, the
  rendered gap IDENTICAL at 340 — the wrapper stretch 308 + mt-8 32
  arithmetic] + the v61 label-finder wrapper class [the clone's LEAF
  carries the identical 500/rgb(26,58,46), pinned green by the v61 F3
  leaf-span finder]; PART X cardBottom 1122 / gridTop 1462 / gap 340
  on both sides).

**The pin:** the dashboard's CROSS-ROW vertical-rhythm census at 1280
(tests/e2e/dashboard.spec.ts — the never-pinned PART X family: the
guidelines card's BOTTOM [1122 — the cumulative upstream rhythm], the
quick-action grid's TOP [1462], the RENDERED cross-row gap [340 — the
byte-identical both-sides parity axis], the grid's OWN mt [32px — the
v51 F5 390 axis's desktop twin]) — GREEN on first run; the pin-sanity
mutation the quick-action grid's mt-8 -> mt-8 lg:mt-6
(dashboard-view.tsx:993 — the QUICK-ACTION grid only; the stat row's
identical class string at :954 untouched): FAILS at exactly the pin's
own axes (mt 32->24, gridTop 1462->1454, gap 340->332; cardBottom
1122 unchanged), cascade-free by construction (the lg: variant inert
below 1024px — the v51 F5 390 mt pin + the 390 card y-positions
2751/2865/2979 + the v42 F2 640 scrollHeight 3029 all green under the
mutation; the v61 F3 grid expectation carries no mt axis; the
quick-action grid the LAST child of the dashboard view — no
downstream cascade; the full dashboard.spec.ts under the mutation: 38
green, only the v83 pin red), then restored (the standalone REBUILD as
a SEPARATE command; git diff src/ = 0 lines; 39/39 green after).

**The v83 lessons:**
1. THE FULL-CENSUS REPRODUCTION: when a re-run pair returns an
   IDENTICAL verdict, the both-sides census STILL runs (the v75
   convention) — and when it reproduces the PRIOR cycle's census
   values EXACTLY (every PART G/Q/X axis matching v77's own numbers,
   two cycles later), cite the full-census reproduction as the
   standing pair's zero-drift proof; the verdict alone is weaker
   evidence than the verdict + the census.
2. THE IDENTICAL-STRING LINE MUTATION: when two source lines carry
   IDENTICAL class strings (the stat row and the quick-action grid
   both `mt-8 grid grid-cols-1 gap-6 md:grid-cols-3`), a pin-sanity
   mutation must be applied by LINE NUMBER (sed '993s/...'), never by
   string replace — a bare replace hits both lines and turns a
   single-axis mutation into an uninterpretable multi-surface break.
3. THE MT-MECHANISM vs RENDERED-GAP DISTINCTION: a census axis that
   differs between the sites (the grid's mt: ref 0px vs clone 32px)
   while the RENDERED geometry is byte-identical (the gap 340) is a
   MECHANISM class, not a parity gap — pin the RENDERED axis (the
   gap/positions), never the mechanism axis alone; the mechanism axis
   may accompany it only as the clone's own twin of an
   already-pinned family (the v51 F5 390 mt pin's desktop twin).

## v84 — the mobile 390 twins' third re-run (the preserved workspace)

The preserved-workspace path (git pull at main @ 2b2ba34, the v83
shipped state + the session_199 transcript; no reset): node_modules in
place (354 packages), chromium-1243 in place, `.env` verified
(DATABASE_URL=file:../db/custom.db, db/ at the repo root), the
seedcheck exact before any flow (7 items / rent 1850 / expenses 2235 /
0 line items / 3 assets / 2 liabilities). The baseline chain FULLY
GREEN as-shipped (lint -> typecheck -> 108 unit -> build -> 286 e2e
[102+108+78 chunk executions = 288 total] -> 35/35 smoke — the exact
documented v83 state). The queue: the v83 plan's v84 suggestion — the
mobile 390 TWINS (the networth + dashboard FULL-PAGE pair at
390x844, last re-shot v78, now the oldest remaining [v78 < v79 < v80 <
v81 < v82 < v83]) — agreeing with the rotation ledger (the SEVENTH
consecutive agreement); the pair's THIRD re-run (v62/v63 -> v69 -> v78
-> v84).

**The probes:**
- ref-standing-v78.sh + standing-checks-v78.sh — the 78th standing
  checks (version-bumped from v77 — version-bump-only diffs): the
  mobile menu verified working the 78th consecutive time; the
  reference's four bugs ALL live (toast-blocker, sheet-trap,
  no-landmark, the 464px /networth overflow); the data census the 78th
  clean drift check; the SEO pair live on both sides.
- vlm-shots-v84.sh + clone-vlmshots-v84.sh + vlm-compare-v84.mjs —
  the re-run pair (login on the first attempt both sides, the parked
  pointer at (5,5), read-only on the reference): both verdicts
  DIFFERENT with every flag DOM-arbitrated to a documented class — the
  NETWORTH flags the v41 mobile-superset class (the tiles stacked) +
  the seed-data class + the platform-chrome class + ONE NEW FLAG (the
  "divider missing in the clone" claim); the DASHBOARD flags the v62
  width-delta class (the subtitle wrap point) + the pct data class +
  the Base44 platform-chrome class + the seed-data class — matching
  the v78 re-run's own flag-set classes exactly (modulo the divider
  claim).
- arbit-v84.sh — the both-sides census (the v78 axes re-measured; the
  v75 convention: the census runs regardless of the verdict): the v78
  census values REPRODUCED EXACTLY — zero drift since v78 on every
  axis (the networth medallion 64x64 + the trend icon 32x32 + the
  tiles h 84 + the grid gap 16px byte-identical, the deltas all the
  v41 mobile-superset class — the reference's card 432/docSW 464/
  2-col tiles 176x84/medallion clipping at right 416 vs the clone's
  358/390/1-col 294x84/fully-visible; the dashboard subtitle chrome
  byte-identical — fs 16px/fw 400/rgb(107,114,128)/lh 24px, the P h
  48, the block h 92, 2 lines — with the wrap-point delta the v62
  width class; the breakdown card's svg family [16,14,16,14,...] +
  chart-absence byte-identical, the heights 324/20/238 identical, the
  widths the v62 page-width class).
- ratio-divider-arbit-v84.sh — the ONE-SHOT both-sides arbitration for
  the v84 networth pair's NEW flag ("the divider missing in the
  clone"): measures the ratio footer row's computed borderTop +
  rhythm + geometry on BOTH sides at 390. Verdict: the divider
  renders on BOTH sides BYTE-IDENTICAL (borderTop 1px solid
  rgba(255,255,255,0.2), mt 24/pt 24, footer h 53, label 14px/400,
  the label box 156x20) — the only deltas the footer w (368 ref vs
  294 clone — the v41 width class) + the footer top (417 vs 505 — the
  stacked-tile card arithmetic). The VLM's claim is a MISREAD (the
  perception class); the census is the authority.
- vlm-arbit-crop-v84.mjs + pixel-diff-v84.mjs +
  crop-diff-v84.mjs — the screenshot diff-crop arbitration
  (the v80 discipline): the 07-add-item-modal.png diff pixel-located
  to 229 pixels in a 7x11 CSS box, the crop pair VLM-read — the delta
  is the modal's default-DATE field (10/17/2026 -> 10/18/2026, the
  UTC calendar rollover between the committed shot and this
  regeneration) — DATE-TEXT-ONLY, the chrome byte-identical.

**The pin:** the networth summary card's RATIO-FOOTER census at 390
(tests/e2e/networth.spec.ts — the never-pinned family at the mobile
viewport: the footer's border-t family [1px/solid/
rgba(255,255,255,0.2) — the inline style, unconditional], the
mt-6/pt-6 rhythm [24/24], the footer h 53 [the pt 24 + the border 1 +
the value-governed 28px ratio row], and the ratio LABEL's typography
+ box [text-sm's 14px/400 + the 156x20 line box] — the v67 F3 pin
holds the footer's {mt, pt, borderTopW, h} at 1280 ONLY, the v4-era
structure test the border style/color + the VALUE's 18px/700 at 1280,
the v82 pin the label's fs at 1280) — GREEN on first run; the
pin-sanity mutation the ratio label's text-sm -> text-xs lg:text-sm
(net-worth-view.tsx:389, applied by LINE NUMBER — the ONLY
className="text-sm" in the file): FAILS at exactly the pin's label
axes (fs 14->12, h 20->16, w 156->134; the footer family GREEN — the
row stays value-governed), cascade-free by construction (the mutation
DESKTOP-RESTORED: at 1280 the lg: variant restores text-sm — the v82
ratioLabel.fs pin, the v67 F3 footer arithmetic, and the v4-era
structure test all green under the mutation; at 390 no other pin
asserts the ratio label — the v41 F3/v63 F3 families stop at the stat
grid/tiles/medallion/card box, the v53/v69/v14 families disjoint; the
full networth.spec.ts under the mutation: 27 green, only the v84 pin
red), then restored (the standalone REBUILD as a SEPARATE command;
git diff src/ = 0 lines; 28/28 green after).

**The v84 lessons:**
1. THE DIVIDER-MISREAD DISPROOF: a VLM flag claiming a structural
   element is MISSING ("the divider is absent in the clone") is
   disproven cheapest by a dedicated ONE-SHOT both-sides census of
   that element's computed chrome (ratio-divider-arbit-v84.sh) — the
   inline-style border family measured byte-identical on both sides;
   the flag's class is PERCEPTION, not a gap. Never accept a
   "missing element" claim without a DOM census of the element's
   computed presence.
2. THE SED-SUBSTITUTION GAP: deriving a versioned probe series by sed
   requires BOTH the version substitutions AND the session-name /
   tmp-dir substitutions — "v78" as a SUBSTRING never matches
   "vlm78" or "arbit78" (the l-m and a-r-b-i-t letters intervene), so
   a bare s/v78/v84/g leaves the shots writing to the OLD /tmp dir
   and the OLD browser session. Always grep the derived script for
   the old version string before running it (the first v84 reference
   run silently shot into /tmp/vlm78 and failed).
3. THE DESKTOP-RESTORED INVERSE MUTATION: the established
   viewport-scoped mutation pattern (base + lg: override) has an
   INVERSE twin for MOBILE-pinned axes: mutate the BASE class and
   RESTORE it under lg: (text-sm -> text-xs lg:text-sm) — the 390
   axes flip while every 1280 pin stays green; the mutation's own
   failure diff (fs 14->12, h 20->16, w 156->134) reads as exactly
   the label sub-family, proving the pin's axis ownership.

## v85 — the v79-era items pair's fourth re-run (the preserved workspace)

The preserved-workspace path (git pull at main @ 3f92b87, the v84
shipped state + the session_202 transcript; no reset): node_modules in
place, chromium-1243 in place, `.env` verified
(DATABASE_URL=file:../db/custom.db, db/ at the repo root), the
seedcheck exact before any flow (7 items / rent 1850 / expenses 2235 /
0 line items / 3 assets / 2 liabilities). The baseline chain FULLY
GREEN as-shipped (lint -> typecheck -> 108 unit -> build -> 289 e2e
chunk executions [102+104+83 — the same total as the documented v84
102+108+79] -> 35/35 smoke). The queue: the v84 plan's v85 suggestion —
the v79-era ITEMS pair (the income + expenses view pair at desktop
1280x800, last re-shot v79, now the oldest remaining [v79 < v80 < v81 <
v82 < v83 < v84]) — agreeing with the rotation ledger (the EIGHTH
consecutive agreement); the pair's FOURTH re-run (v57 -> v64 -> v70 ->
v79 -> v85).

**The probes:**
- ref-standing-v79.sh + standing-checks-v79.sh — the 79th standing
  checks (version-bumped from v78 — version-bump-only diffs verified
  after normalizing the version tokens): the mobile menu verified
  working the 79th consecutive time; the reference's four bugs ALL
  live (toast-blocker, sheet-trap, no-landmark, the 464px /networth
  overflow); the data census the 79th clean drift check; the SEO pair
  live on both sides.
- vlm-shots-v85.sh + clone-vlmshots-v85.sh + vlm-compare-v85.mjs —
  the re-run pair (sed-derived from the v79 series with BOTH the
  version substitutions AND the session-name/tmp-dir substitutions —
  the v84 lesson applied; grep-verified clean of old strings; the
  header comments history-corrected to the fourth re-run): login on
  the first attempt both sides, the parked pointer at (5,5), read-only
  on the reference. Both verdicts DIFFERENT: the PAIR 1 (income) flags
  the user-identity + seed-data classes + ONE NEW FLAG (the "Edit with
  Base44" FAB claimed present in Image 2 — the CLONE); the PAIR 2
  (expenses) flags the v57 DATA-CONDITIONAL chips + the Recurring-wrap
  + the user-identity + the seed classes — matching the v79 re-run's
  own flag-set classes exactly.
- base44-fab-arbit-v85.sh + crop-fab-v85.mjs +
  vlm-arbit-fabcrop-v85.mjs — the ONE-FLAG two-step arbitration for
  the v85 income pair's NEW flag: (1) the DOM census on BOTH sides at
  1280 finds ZERO Base44 elements on either side (the platform FAB
  renders outside the queryable body text — the platform's iframe
  chrome, invisible to a textContent walk); (2) the PIXEL census crops
  the bottom-right 340x100 of both full-page shots and counts dark
  pixels: the REFERENCE's crop carries 6585 dark px (the black
  ~150x40 FAB), the clone's 0 (solid white); the SINGLE-IMAGE VLM
  reads of the two crops confirm it (the reference crop: the black
  "Edit with Base44" button with the orange icon and the x close; the
  clone crop: nothing). Verdict: the VLM's claim is an
  IMAGE-ATTRIBUTION SWAP — the FAB is the reference's own
  platform-chrome, exactly the documented class since v57.
- arbit-v85.sh — the both-sides census (the v79 axes re-measured; the
  v75 convention): the v79 census values REPRODUCED EXACTLY — zero
  drift on every axis (the avatar chrome 36x36/9999px/14px-600/white/
  rgb(143,188,63); the grid 960/16px/309.328 template; the card
  309/20px/12px/border with the h 200-vs-230 v70b wrap class; the
  titleRow gap/dot/dotBg per type; the amount leaf + per-type accents;
  the footer + badge chrome; both filter-card variants; the docSW
  1280).
- wrapper-arbit-v85.sh — the pin's own supplemental both-sides census
  (the v84 ratio-divider precedent): the EXPENSE-ONLY content wrapper
  family measured for the first time on both sides at 1280 — the
  wrapper {display block / flexGrow 1 / paddingRight 96px} on expenses
  and {0px} on income (the conditional control), the titleRow's FULL
  geometry {flex/center/8px/h 24 + the 8x8/9999px dot in the expenses
  orange + the h4 16px/600/rgb(26,58,46)}, the hover action row
  {top 247/right 696/opacity 0/gap 8px} — all byte-identical on both
  sides; the subtitle null-vs-Streaming the subtitle-CONDITIONAL class
  (the v71 F4 idiom).

**The pin:** the expense-card content-wrapper + orange-dot titleRow
census at 1280 (tests/e2e/items.spec.ts — the never-pinned families:
the expenses-conditional pr-24 wrapper — the ONLY pr-24 in src — with
its income paddingRight-0 control; the titleRow's full geometry with
the expenses orange dot's FIRST pin anywhere [completing the v80
savings blue twin's per-type trilogy] and the h4's forestDark color,
never pinned on any item-card title) — GREEN on first run; the
pin-sanity mutation the wrapper's pr-24 -> pr-20 (item-card.tsx:119,
applied by LINE NUMBER): FAILS at exactly the wrapper.paddingRight
axis ("96px" -> "80px" — the failure diff reads as the wrapper
sub-family alone), cascade-free by construction (the titleRow family
content-governed; the amount/badge/footer rows wrapper-external
siblings; the action row absolute; the income/savings wrappers
pr-free; the 390 subtitle texts single-line at both paddings; the full
items.spec.ts under the mutation: 37 green, only the v85 pin red), then
restored (the standalone REBUILD as a SEPARATE command; git diff
src/ = 0 lines; 38/38 green after).

**The v85 lessons:**
1. THE IMAGE-ATTRIBUTION SWAP: a VLM pairwise verdict can SWAP which
   image an element belongs to (the v85 income pair's FAB flag claimed
   the reference's platform chrome was in the clone). The disproof is
   the two-step arbitration: the DOM census (does the element exist in
   either DOM at all?) + the PIXEL crop census with SINGLE-IMAGE VLM
   reads (one image per call — no image-order confusion possible).
   Never trust a pairwise verdict's image attribution for a
   presence/absence claim; the census is the authority.
2. THE TYPE-SCOPED MUTATION: the shared-component cascade problem
   (one card component across three views — any dot/row/h4 mutation
   flips every view's pins) is dodged by mutating the ONE type-scoped
   class in the component (the expenses-conditional pr-24): the
   mutation flips only the expenses wrapper's axis while the
   income/savings pins stay green by construction — the coverage-map
   discipline (v80's responsive-variant dodge) has a type-conditional
   twin.
3. THE FOURTH-RUN STABILITY: the pair's fourth re-run reproduces the
   v79 census values EXACTLY on every axis — the fifth consecutive
   zero-drift re-run after v81/v82/v83/v84's own zero-drift results;
   the rotation cadence's value compounds with each verified cycle.

## v86 — the v80-era savings pair's fourth re-run (the RESET workspace — the fresh-clone path)

The v86 cycle (`docs/remediation-plan-v86.md`; the formal narrative
`docs/session_206.md`): the ledger-verified queue (the v85 plan's
suggestion agreeing with the rotation ledger — the NINTH consecutive
agreement) pointed at the v80-era SAVINGS pair (the savings view at
desktop 1280, last re-shot v80 — the oldest remaining [v80 < v81 < v82
< v83 < v84 < v85]); the pair's FOURTH re-run [v58 → v65 → v74 → v80 →
v86]. The workspace RESET (the fresh-clone path, exercised once before
in v80): git clone at main @ 0d20198, npm ci + the four approved
install scripts, .env written, db/ pushed + seeded, chromium-1243
installed — the baseline chain FULLY GREEN as-shipped (290 e2e chunk
executions = 288 unique = the documented v85 state). The probes this
cycle: the v86 series derived from the v80 series via sed (vlm-shots +
clone-vlmshots + vlm-compare + arbit — the version + session-name +
tmp-dir substitutions, the headers history-corrected to the fourth
re-run), ref-standing-v80.sh + standing-checks-v80.sh (the 80th
standing checks — version-bumped from v79 with the bare-number
session-name token family TOO), wrapper-arbit-v86.sh (the pin's own
one-shot both-sides census), and pixel-diff-v86.mjs + crop-diff-v86.mjs
+ vlm-arbit-crop-v86.mjs (the screenshot DATE-class arbitration).

**The verdict: IDENTICAL — the pair's FIRST non-DIFFERENT verdict in
its five-shot history** (v58 → v65 → v74 → v80 → v86): the VLM's own
flag list confined to the expected data/identity classes (the subtitle
counts, the card figures/names/badges, the avatar letter), zero
layout/style flags to arbitrate. The census STILL RUN per the v75
convention (arbit-v86.sh) — and it reproduced the v80 census values
EXACTLY, zero drift on every axis (the header, the grid 960/16px/~309
template, the card box with the v70b wrap class [ref 200 vs clone 230],
the titleRow with the savings blue dot, the amount leaf, the footer +
badge chrome with the v58 DATA-CONDITIONAL + v57 wrap classes, the
docSW 1280). NO NEW GAP — the v86 iteration PIN-ONLY.

The v86 pin (tests/e2e/items.spec.ts, +1 e2e = 289): the savings
goal-card's SUBTITLE-P + HEADER-ROW + WRAPPER-THIRD-LEG census at 1280
— the never-pinned families measured byte-identical on both sides by
wrapper-arbit-v86.sh first (the v84/v85 one-shot precedent): the
subtitle P's full chrome {h 20 / fs 14px / lh 20px / rgb(107,114,128)
/ mt 0 — the 1280 state of the v51 F3 390-only family, the reference's
"Home Savings" vs the clone's "Index Funds" the data class}, the
with-subtitle arithmetic (the titleRow's mb 4px + the headerRow
{flex/space-between/flex-start/h 48/mb 12px} — the 48 = 24 + 4 + 20
twin of the 390 Rent-card family, never pinned at 1280), and the
wrapper's savings paddingRight-0 THIRD LEG (completing the v85
pr-conditional trilogy: expenses 96px / income 0 / savings 0 — the pr
scoped to expenses only, now verified on all three types). GREEN on
first run.

**The v86 lessons:**
1. THE TAILWIND V4 RATIO-LINE-HEIGHT TRAP: `text-sm` computes
   `line-height: var(--tw-leading, var(--text-sm--line-height))` where
   `--text-sm--line-height` is stored as the UNITLESS RATIO
   calc(1.25 / 0.875) ≈ 1.42857 — so ANY font-size override (even a
   pure `lg:[font-size:15px]` arbitrary property that touches nothing
   else) proportionally scales the line-height (20px → 21.43px) and the
   element's box (20 → 21), cascading into every height-governed pin
   (the v80 savings heights measured 254 under the candidate). A
   font-size axis CANNOT be isolated via Tailwind classes — when the
   pin family is typography, mutate a GEOMETRY axis (alignItems /
   justify) or a type-conditional class instead, and verify the
   cascade-freedom EMPIRICALLY (the full spec file under the mutation)
   before believing the construction argument.
2. THE NARROWED-CONTENT WRAP CASCADE: a padding-widening mutation (the
   v85 type-scoped pattern's conditional extension: expense-only pr-24
   → non-income pr-24) narrows the wrapper's content box (269px →
   137px) — and a text that fits at the OLD width can WRAP at the new
   one (the Emergency Fund h4, ~125px at 16px/600, wrapped +24), after
   which the 1-row grid STRETCHES both cards to the taller natural
   (254) and every card-height pin cascades. The pr-narrowing family is
   only safe when EVERY text on the surface stays single-line at the
   narrowed width — check the LONGEST text, not the first card's.
3. THE IDENTICAL-VERDICT CENSUS: a VLM IDENTICAL verdict does NOT
   retire the both-sides census (the v75 convention holds regardless of
   the verdict) — the census remains the authority (this cycle's census
   reproduced the v80 values exactly, the pair's first IDENTICAL
   verdict riding the same zero-drift evidence). The verdict is a
   signal; the census is the record.
4. THE THIRD TOKEN FAMILY: the standing-checks version bump needs the
   bare-number session-name tokens too (ref79 → ref80 / clone79 →
   clone80 — "79" never matches "v79" as a substring); the v84
   substitution-gap lesson now has three token families to check: the
   version (v79), the ordinal (79th), and the bare session numbers.
5. THE BENIGN-NOISE SCREENSHOT CLASS: a screenshot diff that is
   ±1-channel gradient rounding in a solid-color band (no text, no
   layout, both crops VLM-read identical — the 08-calculator band this
   cycle: 1077 px over 55×74, every differing pixel exactly one R-unit)
   is RASTERIZATION-NOISE, not a regression: pixel-locate it, dump the
   actual channel deltas, and classify it as its own benign class next
   to DATE-TEXT-ONLY — the regenerated set still ships.

## v87 — the login + calculator pair's fourth re-run (the preserved workspace)

The v87 iteration (docs/remediation-plan-v87.md): the re-run cycle's
next-oldest candidate — the ledger-verified queue (the v86 plan's v87
suggestion AGREEING with the rotation ledger: the v81-era login +
calculator pair [the login view + the calculator dialog at desktop
1280], last re-shot v81, the oldest remaining by LAST RE-SHOT DATE
[v81 < v82 < v83 < v84 < v85 < v86]; the pair's FOURTH re-run [v59 ->
v66 -> v75 -> v81 -> v87] — the TENTH consecutive queue/ledger
agreement), plus the axe watch at its re-check point (NO DRIFT — 4.14.0,
no 5.x, the v68 dedupe holds) and the 81st standing checks
(ref-standing-v81.sh + standing-checks-v81.sh, version-bumped from v80
across the three token families — version-bump-only diffs verified).

The probe series (the v81 lineage, sed-derived with the version +
session-name/tmp-dir substitutions, the headers history-corrected to
the fourth re-run):
- login-shots-v87.sh + vlm-shots-v87.sh — the REFERENCE side (login on
  the first attempt; the calculator via the Rent-card hover + Calculate
  click; the parked pointer at (5,5); read-only).
- clone-login-shots-v87.sh + clone-vlmshots-v87.sh — the CLONE side
  (the with-server :3200 parity server; the calculator twin adds the
  matching "Contents Insurance" $25 monthly line item through the real
  UI then FULLY restores the fixture — the delete + Rent's $1850
  re-edit + the "$2235.00" page-total verify).
- vlm-compare-v87.mjs — the VLM pairwise (the login twin IDENTICAL
  with zero style flags, the third consecutive; the calculator twin
  DIFFERENT with the SAME three flag-set classes as v75/v81).
- arbit-v87.sh + login-census-ref-v87.sh — the both-sides census (the
  v81 axes re-measured: panel/scrim/title/desc/totalCard/nameH4/row/
  pillRow/pill1/amountP/addBtn chrome all BYTE-IDENTICAL — zero drift).
- close-arbit-v87.sh — the NEW one-shot button-inventory probe (the
  arbitration follow-up: the arbit census's close-button finder
  returned no match on the REF side this run — the probe dumps every
  button in the ref's panel with aria-label/textContent/geometry).
- pair-arbit-v87.sh — the supplemental one-shot census for the pin's
  own axes (the v84/v85/v86 precedent): the calculator close's full
  chrome + the login card's pad family + the logo's own radius,
  measured byte-identical on both sides.

The findings:
1. The LOGIN pair: IDENTICAL, zero style flags — zero drift since v75
   on the VLM layer (the third consecutive IDENTICAL). The both-sides
   census byte-identical on every axis; the card's 0px-width border
   computed-color and the shadow's transparent lead-layer count the v66
   computed-form INVISIBLE class.
2. The CALCULATOR pair: DIFFERENT with the SAME three flags as v75/v81
   — (a) the "extra will-update line" the v66 DATA-CONDITIONAL class
   (hasWillUpdateSpan ref false vs clone true); (b) the "hover action
   buttons missing in the clone" the POINTER-POSITION perception class
   (actionsAtRest {opacity 0, btnCount 2} BYTE-IDENTICAL); (c) the
   "row height shorter" a VLM MISREAD (the row 720x102 BYTE-IDENTICAL).
3. **THE NEW REFERENCE-SIDE OBSERVATION — the reference's calculator
   close button LOST its accessible name**: the v81 census found the
   ref's close by aria-label/text; the v87 census's name-based finder
   returns no match, and close-arbit-v87.sh's inventory shows the
   button with aria:"" and txt:"" (a bare SVG x). The CHROME is
   unchanged and byte-identical (36x36/radius 6px/transparent/0px
   border). The clone retains aria-label="Close" — the superset
   behavior, already functionally pinned by every calculator.spec.ts
   interaction (getByRole name:"Close"). NO clone gap — PIN-ONLY.
4. NO NEW CLONE GAP — the iteration is PIN-ONLY: the calculator
   CLOSE-BUTTON chrome census at 1280 (the never-pinned axes: the
   close's radius "6px" / bg rgba(0,0,0,0) / borderTopWidth "0px" /
   display "flex" — the v49/v53/v59 pins hold {w,h} geometry only, no
   spec asserted the calculator close's radius/bg/border at ANY
   viewport; the 0px-border computed-COLOR excluded — the v66 INVISIBLE
   class), the pin riding the v59/v81 read-only EMPTY-state discipline.
   The pin-sanity mutation: the close's rounded-md ->
   rounded-md lg:rounded-lg (calculator-dialog.tsx:127 header area,
   line 138) FAILS at exactly the close.radius axis ("6px" -> "8px") —
   cascade-free BY CONSTRUCTION (border-radius never affects w/h — the
   v49/v53/v59 geometry pins green under it by construction; the full
   calculator.spec.ts under the mutation: 16 green, only the v87 pin
   red).
5. The screenshots 16/16 BYTE-IDENTICAL — the same-db regeneration law
   (the preserved v86-cycle db + same-day shots reproduce the committed
   set byte-for-byte, even the v86 rasterization-noise file
   08-calculator: no re-seed, no pixel arbitration needed).

**The v87 lessons:**
1. THE NAME-INDEPENDENT FINDER: the reference's ACCESSIBLE NAMES are
   not stable contracts — the ref's calculator close button lost its
   aria-label between v81 and v87 while its chrome stayed
   byte-identical. Census finders for REFERENCE-side elements must use
   GEOMETRY + POSITION + TEXT-CONTENT filters (the 36x36 header-area
   button), never name-based selectors alone — and a census axis that
   silently goes MISSING (the finder's no-match) is itself a finding to
   arbitrate with a dedicated inventory probe, not a failure to paper
   over.
2. THE REFERENCE-REGRESSION CLASS: a reference-side a11y regression
   (the name loss) is NOT a clone parity gap — the clone's retained
   accessible name is the SUPERSET behavior (the v56 family), already
   functionally pinned by the role-based interactions; the census
   records the observation, the pin records the chrome, no production
   change.
3. THE SAME-DB REGENERATION LAW: when the workspace is PRESERVED (no
   re-seed), the screenshot regeneration reproduces the committed set
   byte-for-byte (16/16 this cycle — including the prior cycle's
   rasterization-noise file, which is byte-stable against the same db
   and rendering pipeline). The DATE-TEXT-ONLY and noise classes appear
   only after a FRESH seed — prefer the same-db regeneration when the
   seed state is already exact (the seedcheck gate) and no fixture
   drift occurred.

The v88 queue (suggestions — verify against the rotation ledger
before executing): (1) the re-run cadence rotates to the next-oldest
candidate after this pair (the v82-era networth + drill-down pair [the
networth view + the dashboard drill-down EXPANDED at 1280], last
re-shot v82 — now the oldest remaining), (2) the axe-core watch at its
next re-check point (only a 5.x wrapper changes the calculus), (3) the
deferred reference-write censuses (unchanged) + the login card's pad
family + logo radius pin (the pair-arbit-v87.sh values recorded in the
v87 plan's F4 — the pair's fifth re-run).

## v88 — the networth + drill-down pair's fourth re-run (the fresh-clone workspace)

The v88 iteration (docs/remediation-plan-v88.md): the re-run cycle's
next-oldest candidate — the ledger-verified queue (the v87 plan's v88
suggestion AGREEING with the rotation ledger: the v82-era networth +
drill-down pair [the networth view + the dashboard drill-down EXPANDED
at desktop 1280], last re-shot v82, the oldest remaining by LAST
RE-SHOT DATE [v82 < v83 < v84 < v85 < v86 < v87]; the pair's FOURTH
re-run [v60 -> v67 -> v76 -> v82 -> v88] — the ELEVENTH consecutive
queue/ledger agreement), plus the axe watch at its re-check point (NO
DRIFT — 4.14.0, no 5.x, the v68 dedupe holds) and the 82nd standing
checks (ref-standing-v82.sh + standing-checks-v82.sh, version-bumped
from v81 across the three token families — version-bump-only diffs
verified).

The workspace REBUILT (the fresh-clone path, the v86 precedent): the
workspace had been reset — git clone at main @ 154ac6a, the tree clean;
npm ci (354 packages, the four approved install scripts); .env written
(DATABASE_URL=file:../db/custom.db, db/ at the repo root, db:generate +
db:push + db:seed); chromium-1243 installed; the paramiko ssh shim
deployed outside the repo; the seedcheck exact before any flow.

The probe series (the v82 lineage, sed-derived with the version +
session-name + tmp-dir substitutions — the /tmp/vlm82 -> /tmp/vlm88
bare-number family caught by the grep verification, the v84 lesson's
second face; the headers history-corrected to the fourth re-run):
- vlm-shots-v88.sh — the REFERENCE side (login on the first attempt;
  the drill-down expanded via the Total Income section + first category
  clicks; the parked pointer at (5,5); read-only — the v46 rule).
- clone-vlmshots-v88.sh — the CLONE side (the with-server :3200 parity
  server; the same expansion clicks; no fixture writes).
- vlm-compare-v88.mjs — the VLM pairwise (the networth twin IDENTICAL
  with the only style flag the Base44 overlay; the drill-down twin
  DIFFERENT with seven flags, every one DOM-arbitrated to a documented
  class).
- arbit-v88.sh — the both-sides census (the v82 axes re-measured:
  PART A the drill-down census [nav highlight, avatar, progress fill,
  donut labels, stat trend icons], PART B the networth summary-card
  family; the census runs regardless of the verdict — the v75
  convention).
- stat-divider-arbit-v88.sh — the dedicated one-shot both-sides census
  for the VLM's NEW flag ("the stat-card footer divider lines missing
  in the reference") — the v87 close-arbit precedent applied to a
  divider-visibility claim.

The findings:
1. The NETWORTH pair: IDENTICAL — the only layout/style flag the
   reference's "Edit with Base44" overlay (the platform-chrome class);
   every other delta the seed classes. The PART B census REPRODUCES the
   v82 census values EXACTLY — zero drift on every axis (the card/
   headRow/label/figure/medallion/statGrid/statTile/ratioFooter
   families byte-identical; the labelBlock width 304-vs-357 the
   standing DATA-CONDITIONAL width class; the heights byte-identical).
2. The DRILL-DOWN pair: DIFFERENT with seven flags, every one
   DOM-arbitrated to a documented class — the nav highlight the v56
   SUPERSET class; the avatar the user-identity class; the progress
   fill the pct x 568 DATA class (fillW 173-vs-357 on the
   byte-identical 568x12 track — the v60 arbitration's own values
   REPRODUCED EXACTLY, five re-runs later, the v82
   census-arithmetic-reproduction lesson's standing case); the donut
   percentage-labels claim the v60 PERCEPTION class re-arbitrated live
   (the reference DOES render its labels — count 4, 16px, black, 3
   sectors, 0 lines, the chrome byte-identical, the texts each site's
   own data); the expanded-content/counts/proportions the seed-data
   classes; the Base44 overlay the platform-chrome class.
3. **THE CYCLE'S NEW FLAG — the "stat-card footer divider lines present
   in the clone but missing in the reference" a VLM MISREAD**, disproven
   by the dedicated one-shot both-sides census (stat-divider-arbit-v88.sh):
   the divider renders BYTE-IDENTICALLY on BOTH sides — the count row
   {h 20 / w 254 / flex / gap 8px / center / 14px / rgb(10,10,10)} with
   the rowChildTags [SPAN, DIV, svg]; the divider {DIV, h 1, bg
   rgb(229,231,227), flexGrow 1} on every card; the trend icons 16x16
   with the per-type colors (lime/blue/orange). The only delta the
   itemsText ("1 item" vs "2 items") — the seed-data class. The VLM
   read the faint 1px rgb(229,231,227) line's VISIBILITY difference as
   presence/absence — the divider twin of the v84 divider-misread
   lesson.
4. NO NEW CLONE GAP — the iteration is PIN-ONLY: the stat-card
   COUNT-ROW + DIVIDER census at 1280 (the never-pinned families: the
   count row's full chrome + the h-px flex-1 divider [never pinned at
   ANY viewport] + the trend icon's per-type color trilogy — the
   stat-card twin of the v80/v85 per-type-dot trilogy; the divider's
   WIDTH excluded as the flex-1 data-conditional remainder, the v82
   convention). The pin-sanity mutation: the divider's h-px ->
   h-px lg:h-0.5 (dashboard-view.tsx:618) FAILS at exactly the
   divider.height axis ("1px" -> "2px") — cascade-free BY CONSTRUCTION
   (the flex items-center row's height stays the text's 20px line box;
   the card height 210 unchanged — the v40 F1 bands green; 39 green
   under the mutation, only the v88 pin red; restored 40/40 green).
5. The screenshots 16/16 BYTE-IDENTICAL — the same-day-seed
   byte-identity law (the fresh seed planted and the shots taken on
   the same calendar day reproduce the committed set byte-for-byte).

**The v88 lessons:**
1. THE DIVIDER-VISIBILITY MISREAD: a VLM claim that a FAINT element
   (a 1px line in a near-background color) is "missing" on one side is
   cheapest to disprove with a dedicated both-sides census of that
   element's computed chrome — the v84 divider-misread twin, now with
   the trend-icon per-type trilogy as the bonus census axes. The
   visibility-of-faint-chrome is NOT a parity axis; the computed style
   is.
2. THE FINDER/ASSERTION DECOUPLING: the census finder must NEVER
   filter on the axis it is about to assert — the first v88 pin draft
   found the divider by its <=1px height (the very axis the pin
   asserts), so the pin-sanity mutation (h 2px) made the finder return
   null and the failure diff read as "null vs object" instead of the
   clean "1px vs 2px". The structural finder (the middle child that is
   neither the text span nor the svg) keeps the element findable under
   the mutation and the failure diff reads as the axis alone — the v87
   name-independent-finder lesson's finder-twin.
3. THE SED TMP-DIR TOKEN FAMILY: the sed derivation needs the
   BARE-NUMBER tmp-dir family TOO (/tmp/vlm82 -> /tmp/vlm88 — "vlm82"
   contains no "v82" substring) — the v84 lesson's second face,
   grep-caught before any probe ran against the stale directory.

The v89 queue (suggestions — verify against the rotation ledger
before executing): (1) the re-run cadence rotates to the next-oldest
candidate after this pair (the v83-era DASHBOARD pair [the dashboard
FULL-PAGE at desktop 1280 — the below-the-fold Budget Guidelines card
+ the quick-action row], last re-shot v83 — now the oldest remaining
[v83 < v84 < v85 < v86 < v87 < v88]; the pair's FOURTH re-run [v61 ->
v68 -> v77 -> v83 -> v89]), (2) the axe-core watch at its next
re-check point (only a 5.x wrapper changes the calculus), (3) the
deferred reference-write censuses (unchanged — out of bounds under the
v46 read-only rule).

## v89 — the dashboard pair's fourth re-run (the preserved workspace)

The v89 iteration (docs/remediation-plan-v89.md): the re-run cycle's
next-oldest candidate — the ledger-verified queue (the v88 plan's v89
suggestion AGREEING with the rotation ledger: the v83-era DASHBOARD
pair [the dashboard FULL-PAGE at desktop 1280x800 — the below-the-fold
Budget Guidelines card + the quick-action row], last re-shot v83, the
oldest remaining by LAST RE-SHOT DATE [v83 < v84 < v85 < v86 < v87 <
v88]; the pair's FOURTH re-run [v61 -> v68 -> v77 -> v83 -> v89] — the
TWELFTH consecutive queue/ledger agreement), plus the axe watch at its
re-check point (NO DRIFT — 4.14.0, no 5.x, the v68 dedupe holds) and
the 83rd standing checks (ref-standing-v83.sh + standing-checks-v83.sh,
version-bumped from v82 across the three token families —
version-bump-only diffs verified by normalizing back and diffing
clean).

The workspace PRESERVED (the v87 precedent — no reset): git pull
fast-forward 0cae166..ef681c0 (the session_214 transcript only), the
tree clean; the environment verified in place (.env, db/ with custom.db
+ e2e.db, node_modules 354 packages, chromium-1243, the paramiko ssh
shim); the seedcheck exact before any flow.

The probe series (the v83 lineage, sed-derived with the version +
session-name + tmp-dir substitutions [vlm83 -> vlm89, refar83 ->
refar89, clonear83 -> clonear89 — the bare-number families caught by
the grep verification, the v84 lesson's faces]; the headers
history-corrected to the fourth re-run [v61 -> v68 -> v77 -> v83 ->
v89]; the functional bodies verified version-bump-only by the
normalize-back diff):
- vlm-shots-v89.sh — the REFERENCE side (login on the first attempt;
  the parked pointer at (5,5); read-only — the v46 rule).
- clone-vlmshots-v89.sh — the CLONE side (the with-server :3200 parity
  server; no fixture writes).
- vlm-compare-v89.mjs — the VLM pairwise.
- arbit-v89.sh — the both-sides census (the v83 PART G/Q/X axes
  re-measured; the census runs regardless of the verdict — the v75
  convention). Executed in the CONTROLLED TWO-HALF FORM after the
  sandbox's chromium resource exhaustion aborted the combined run:
  ref-arbit-v89.sh + clone-arbit-v89.sh, the census JS IDENTICAL to the
  combined script's.
- qa-transition-arbit-v89.sh — the supplemental one-shot both-sides
  census for the pin's own axes (the v87/v88 precedent).

The findings:
1. The verdict IDENTICAL — zero style flags (the pair's SECOND
   consecutive IDENTICAL verdict [v83 -> v89]; every VLM flag the
   documented seed-data classes: the allocation bar 30.5%-vs-62.8%, the
   balance $3475-vs-$2065, the stat figures, the donut proportions).
2. The both-sides census REPRODUCES the v83 census values EXACTLY —
   zero drift on every axis (PART G: the guidelines card
   468x348/radius 12px/border/bg/the visible shadow layers, the header
   pad 24px/fs 16px/fw 600/rgb(26,58,46)/lh 16px/tracking -0.4px, the
   body pad 0px 24px 24px/display block, the three tiles 418x78 with
   the Needs/Wants/Savings tints and the label/pct/desc chrome — the
   ONLY delta the shadow's transparent lead-layer count [the v66
   computed-form INVISIBLE class]; PART Q: the grid 304px x3/gap 24px/
   w 960, the three cards 304x90/radius 16px/pad 24px/white/border/
   the tinted tiles/the 20px icons/the labels/the 0.5-opacity pluses/
   transition 0.2s — the grid-mt [ref 0px vs clone 32px] the v77
   mechanism class with the RENDERED gap 340 byte-identical, the label
   wrapper-catch the v61 lesson; PART X: cardBottom 1122/gridTop 1462/
   gap 340 byte-identical on BOTH sides).
3. NO NEW CLONE GAP — the iteration is PIN-ONLY: the quick-action
   TRANSITION + PLUS-viewBox + GUIDELINES-BODY-DISPLAY census at 1280
   (the never-pinned families: the three cards' transition
   {transitionDuration "0.2s"/transitionProperty "all" — never pinned
   at ANY viewport; the items.spec.ts transitionDur pins are the ITEM
   card's own family} + the three plus icons' viewBox {0 0 24 24 — the
   v77 icon-viewBox family's plus twin} + the guidelines body's display
   {block — the v61 F2 pad family's companion axis} + the docSW guard).
   The pin-sanity mutation: the card's duration-200 ->
   duration-200 lg:duration-300 (dashboard-view.tsx:885) FAILS at
   exactly the card.transitionDuration axis ("0.2s" -> "0.3s") —
   cascade-free BY CONSTRUCTION (transitionDuration never affects
   geometry — every geometry pin green; the v45 F3b hover-shadow pin
   asserts the SETTLED layers; 40 green under the mutation, only the
   v89 pin red; restored 41/41 green).
4. The screenshots 16/16 BYTE-IDENTICAL — the same-day-seed
   byte-identity law (the seed planted and the shots taken on the same
   calendar day 2026-10-18 reproduce the committed set byte-for-byte).

**The v89 lessons:**
1. THE CHROMIUM RESOURCE-EXHAUSTION REAPING: the sandbox's
   agent-browser chromium processes accumulate across long probe
   sessions (66 zombie processes observed mid-cycle) until
   fork/pthread_create fails (`Resource temporarily unavailable`) —
   and the symptom is EMPTY eval results, NOT an error surface. The
   fix: `pkill -f agent-browser` + a fresh AGENT_BROWSER_SESSION name
   before the next eval. Budget a reaping step between the reference
   and clone halves of any long combined probe.
2. THE TWO-HALF CONTROLLED CENSUS FORM: when the combined arbit script
   fails mid-run (the resource exhaustion above, or a transient
   with-server boot abort — the standalone server "Aborted" once with
   an empty log, then booted clean on the manual retry), the census's
   reference half and clone half can run as SEPARATE scripts with the
   IDENTICAL census JS. The both-sides census contract is the JS
   identity (the version-bump-only functional-body diff), not the
   single-script form — retry-first before investigating, split-second
   if the retry fails.

## v90 — the mobile 390 twins' fourth re-run (the fresh-clone workspace)

The v90 iteration (docs/remediation-plan-v90.md): the re-run cycle's
next-oldest candidate — the ledger-verified queue (the v89 plan's v90
suggestion AGREEING with the rotation ledger once the v89-era docs'
surface-name transcription error is corrected: the v84-era MOBILE 390
TWINS [the /networth + the dashboard FULL-PAGE pair at 390x844], last
re-shot v84, the oldest remaining [v84 < v85 < v86 < v87 < v88 < v89];
the pair's FOURTH re-run [v62/v63 -> v69 -> v78 -> v84 -> v90] — the
THIRTEENTH consecutive queue/ledger agreement), plus the axe watch at
its re-check point (NO DRIFT — 4.14.0, no 5.x, the v68 dedupe holds)
and the 84th standing checks (ref-standing-v84.sh +
standing-checks-v84.sh, version-bumped from v83 across the three token
families — version-bump-only diffs verified by normalizing back and
diffing clean).

The workspace REBUILT (the fresh-clone path, the v86/v88 precedent):
git clone at main @ 0f8bec4, the tree clean; the environment
re-provisioned (npm ci 354 packages; .env written
[DATABASE_URL="file:../db/custom.db"]; db/ at the repo root,
db:generate + db:push + db:seed; chromium-1243; the paramiko ssh shim
outside the repo at /home/z/my-project/bin/ssh); the seedcheck exact
before any flow; the full baseline chain green on the first run (lint
-> typecheck -> 108 unit -> build -> 292 e2e [121+114+59 = 295 chunk
executions] -> 35/35 smoke).

The probe series (the v84 lineage, sed-derived with the version +
session-name + tmp-dir substitutions [vlm84 -> vlm90, refarbit84 ->
refarbit90, clonearbit84 -> clonearbit90, ref84 -> ref90, clone84 ->
clone90]; the headers history-corrected to the FOURTH re-run [v62/v63
-> v69 -> v78 -> v84 -> v90]; the functional bodies verified
version-bump-only by the normalize-back diff — only the intentional
history-correction comment lines differ):
- vlm-shots-v90.sh — the REFERENCE side (login on the first attempt;
  the parked pointer at (5,5); read-only — the v46 rule).
- clone-vlmshots-v90.sh — the CLONE side (the with-server :3200 parity
  server).
- vlm-compare-v90.mjs — the VLM pairwise.
- arbit-v90.sh — the both-sides census (the v84 census axes
  re-measured; the census runs regardless of the verdict — the v75
  convention; the combined script ran clean this cycle — no resource
  exhaustion, no two-half split needed).
- tile-interior-arbit-v90.sh — the supplemental one-shot both-sides
  census for the pin's own axes (the v87/v88/v89 precedent).

The findings:
1. Both verdicts DIFFERENT, every flag DOM-arbitrated to the v84
   re-run's OWN documented classes (the v41 mobile-superset stacking;
   the medallion "larger circle" a VLM perception misread — the
   64x64 + 32x32 chrome byte-identical, the artifact riding the
   reference's own viewport-clipped medallion; the tab-bar alignment a
   misread under the v53 tablist-390 pin; the v62 subtitle width-delta
   wrap; the Base44 platform-chrome overlay; the seed-data classes).
2. The both-sides census REPRODUCES the v84 census values EXACTLY —
   zero drift on every axis (the summary card/statGrid/tiles/medallion/
   trendIcon families; the subtitle chrome fs 16px/fw 400/
   rgb(107,114,128)/lh 24px/P h 48/block h 92; the breakdown card's
   svg family [svgCount 7, the 16/14 alternation, rechartsWrappers 0,
   pieSectors 0] + the children heights byte-identical). NO NEW CLONE
   GAP — the iteration PIN-ONLY.
3. The v90 pin (+1 e2e = 293): the stat-tile INTERIOR census at 390
   (tests/e2e/networth.spec.ts — the never-pinned families: the two
   tiles' LABEL {P/12px/rgba(255,255,255,0.7)/mb 4px/h 16} + VALUE
   {P/24px/700/white} interiors; the v63 F3 pin held the tile BOX
   only) — the pin's own axes first measured byte-identical on both
   sides by the supplemental census — GREEN on first run.
4. THE MUTATION-AS-COVERAGE-AUDIT CATCH: the pin-sanity mutation's
   FIRST attempt (the bare font-bold -> font-extrabold swap at
   net-worth-view.tsx:371) cascaded to the v60 F1 pin's amtFw axis at
   1280 — the plan's fw-token grep had MISSED the v60 pin's amtFw
   shorthand (the tile value's fw was already pinned at 1280 all
   along). The mutation discipline is the coverage-map audit, not just
   the pin's sensitivity check: grep with BOTH the `fw:` and the
   shorthand (`amtFw`-style) tokens before claiming a never-pinned
   axis. The corrected viewport-scoped dodge (font-bold ->
   font-bold max-lg:font-extrabold — the max-lg variant INERT at
   >=1024px, active below) confines the flip to the pin's own viewport
   family: only the v90 pin red under it (28 green), the failure diff
   reads as the fw axis alone ("700" -> "800"), restored green
   (git diff src/ = 0; post-restore 29/29).
5. The full chain re-run GREEN: lint -> typecheck -> 108 unit -> build
   -> 293 e2e (122+114+59 = 295 chunk executions, zero flakes) ->
   35/35 smoke; the screenshots 16/16 BYTE-IDENTICAL (the same-day-seed
   byte-identity law on the fresh-clone seed).

**The v90 lessons:**
- THE QUEUE-PROSE VERIFICATION LESSON: the rotation ledger's authority
  is the PROBE LINEAGE (the shot scripts' own surface lists), never
  the prose queue phrasing — the v89-era docs' "login + dashboard" v90
  phrasing (and its "FIFTH re-run [v69 -> v74 -> v78 -> v84 -> v90]"
  bracket, v74 being the savings DESKTOP pair) was a transcription
  error caught by reading vlm-shots-v84.sh before deriving the v90
  series. Verify the surface names AND the re-run bracket against the
  probe scripts before every derivation; correct the record in the
  plan.
- THE SHORTHAND-TOKEN GREP LESSON: coverage-map greps must search the
  ASSERTION'S VALUE TOKENS in both the long form (`fw: "700"`) and the
  census-shorthand form (`amtFw`) — the v90 first-attempt cascade was
  exactly a shorthand miss. When a mutation cascades, do not abandon
  the mutation: read the cascaded pin's assertion, correct the
  coverage map, and re-scope the mutation (the viewport-scoped dodge)
  so the flip lands only where the new pin is the sole assertion.
- The fresh-clone reprovisioning checklist re-verified end-to-end (npm
  ci -> .env -> db:generate/push/seed -> chromium-1243 -> the paramiko
  shim outside the repo -> the seedcheck exact): the full chain lands
  on the documented state with zero flakes on the first run.

The v91 queue (suggestions — verify against the rotation ledger
before executing): (1) the re-run cadence rotates to the next-oldest
candidate after this pair (the v85-era ITEMS pair [the income +
expenses view pair at desktop 1280], last re-shot v85 — now the oldest
remaining [v85 < v86 < v87 < v88 < v89 < v90]; the pair's FIFTH re-run
[v57 -> v64 -> v70 -> v79 -> v85 -> v91]), (2) the axe-core watch at
its next re-check point (only a 5.x wrapper changes the calculus), (3)
the deferred reference-write censuses (unchanged — out of bounds under
the v46 read-only rule).

## v91 — the items pair's fifth re-run (the two-half census + the FAB re-arbitration)

The v91 iteration (docs/remediation-plan-v91.md): the re-run cycle's
next-oldest candidate — the ledger-verified queue (the v90-era docs'
v91 suggestion AGREEING with the rotation ledger: the v85-era ITEMS
pair [the INCOME + EXPENSES view pair at desktop 1280x800, full-page],
last re-shot v85, the oldest remaining [v85 < v86 < v87 < v88 < v89 <
v90]; the pair's FIFTH re-run [v57 -> v64 -> v70 -> v79 -> v85 -> v91]
— the FOURTEENTH consecutive queue/ledger agreement, the surface names
verified against vlm-shots-v85.sh's own surface list before the
derivation, no transcription error this cycle), plus the axe watch at
its re-check point (NO DRIFT — 4.14.0 npm-latest, only rc prereleases
beyond, no 5.x, the v68 dedupe holds) and the 85th standing checks
(ref-standing-v85.sh + standing-checks-v85.sh, version-bumped from v84
across the three token families — version-bump-only diffs verified by
normalizing back and diffing clean).

The workspace REBUILT (the fresh-clone path, the v86/v88/v90
precedent): git clone at main @ 07586b7, the tree clean; the
environment re-provisioned (npm ci 354 packages; .env written
[DATABASE_URL="file:../db/custom.db"]; db/ at the repo root,
db:generate + db:push + db:seed; chromium-1243; the paramiko ssh shim
outside the repo at /home/z/my-project/bin/ssh); the seedcheck exact
before any flow; the full baseline chain green on the first run (lint
-> typecheck -> 108 unit -> build -> 293 e2e [127+106+62 = 295 chunk
executions] -> 35/35 smoke).

The probe series (the v85 lineage, sed-derived with the version +
session-name + tmp-dir substitutions [vlm85 -> vlm91, refarbv85 ->
refarbit91, clonearbv85 -> clonearbit91, v85 -> v91; the shots'
session names refvlm85 -> refvlm91 / clonevlm85 -> clonevlm91 riding
the vlm85 -> vlm91 family]; the headers history-corrected to the FIFTH
re-run [v57 -> v64 -> v70 -> v79 -> v85 -> v91] + "last re-shot v85";
the functional bodies verified version-bump-only by the normalize-back
diff — only the intentional history-correction comment lines differ):
- vlm-shots-v91.sh — the REFERENCE side (login on the first attempt;
  the parked pointer at (5,5); read-only — the v46 rule).
- clone-vlmshots-v91.sh — the CLONE side (the with-server :3200 parity
  server).
- vlm-compare-v91.mjs — the VLM pairwise.
- arbit-v91.sh — the both-sides census (the v85 census axes
  re-measured; the census runs regardless of the verdict — the v75
  convention) — which TIMED OUT mid-run in the chromium resource
  exhaustion (70 zombie processes; the v89-documented symptom class),
  and was completed in the TWO-HALF controlled form:
  - ref-arbit-v91.sh — the reference half.
  - clone-arbit-v91.sh — the clone half (the census JS byte-identical
    across the halves — the lines-1-215 identity verified).
- base44-fab-arbit-v91.sh — the one-shot both-sides DOM arbitration of
  the recurring FAB flag (the v85 precedent's own finder).
- filter-interior-arbit-v91.sh + filter-interior-clone-v91.sh — the
  supplemental one-shot both-sides census for the pin's own axes (the
  v87/v88/v89/v90 precedent), BUILT TWO-HALF from the start after the
  cycle's first exhaustion.

The findings:
1. Both verdicts DIFFERENT, every flag DOM-arbitrated to the v85
   re-run's OWN documented classes (the v57 payment-chip
   DATA-CONDITIONAL footer; the v57 Recurring superset wrap [the card
   h 200-vs-230, the badgeRow h 22-vs-52]; the seed-count grids; the
   user-identity avatar; the seed-data figures/dates/badges).
2. The "Edit with Base44" FAB flag RECURRED with its v85-documented
   IMAGE-ATTRIBUTION SWAP (the VLM attributing the reference's own
   platform FAB to the clone) — re-arbitrated live by the one-shot DOM
   census: fabCount 0 + bodyHasBase44 false on BOTH sides (the FAB
   renders in the reference's platform iframe chrome, outside the
   queryable body DOM; the v85 pixel census already located its pixels
   in the reference's bottom-right crop alone).
3. The both-sides census (the two-half form) REPRODUCES the v85 census
   values EXACTLY — zero drift on every axis (the avatar/grid/card/
   titleRow/amount/footer/badge/filterCard families; the docSW 1280
   guard). NO NEW CLONE GAP — the iteration PIN-ONLY.
4. The v91 pin (+1 e2e = 294): the filter-card INTERACTIVE-INTERIOR
   census at 1280 (tests/e2e/items.spec.ts — the never-pinned
   families: the search input's TYPOGRAPHY {14px/400/20px/
   rgb(10,10,10)} + every combobox trigger's RESTING chrome {pad
   8px 12px/space-between/center/transparent/6px/1px
   rgb(229,229,229)/14px/400 + the chevron 16x16 currentColor} — the
   v64/v70 pins held the geometry, the v37 pins the focus state; the
   interiors never pinned at ANY viewport) — the pin's own axes first
   measured byte-identical on both sides by the supplemental two-half
   census — GREEN on first run.
5. The pin-sanity mutation (the executed form — the viewport-scoped
   pl-10 -> pl-10 lg:font-medium at items-view.tsx:188, by LINE
   NUMBER; AT-lg because the pin runs at 1280): the failure diff reads
   as the search's fw axis alone ("400" -> "500"); the full
   items.spec.ts under the mutation reads ONLY the v91 pin red (39
   green) — cascade-free BY CONSTRUCTION (fw never changes
   line-height/color/geometry; no spec asserts any input's fw at any
   viewport — the coverage grep run with BOTH the fw: long form AND
   the Fw-suffix shorthand family, the v90 lesson applied); restored
   (git diff src/ = 0; the standalone REBUILD via the FULL npm run
   build; post-restore 40/40 green).
6. The full chain re-run GREEN: lint -> typecheck -> 108 unit -> build
   -> 294 e2e (128+106+62 = 296 chunk executions, zero flakes) ->
   35/35 smoke; the screenshots 16/16 BYTE-IDENTICAL (the same-day-seed
   byte-identity law on the fresh-clone seed).

**The v91 lessons:**
- THE FAB RE-ARBITRATION: the v85-documented Base44 FAB
  image-attribution swap RECURRED (the VLM attributing the reference's
  own platform FAB to the clone) — a documented VLM misattribution
  class that recurs is settled by the one-shot both-sides DOM census
  (the DOM zero + the documented pixel evidence together), without
  re-running the v85 pixel-crop chain.
- THE TWO-HALF CENSUS, RETROFITTED: the combined arbit script can fail
  mid-cycle in the chromium resource exhaustion (70 zombies this
  cycle) — the v89 two-half form (the census JS byte-identity as the
  contract, verified by the md5 line-block diff) is the recovery, and
  the supplemental one-shot censuses can be BUILT two-half from the
  start when the sandbox has already shown the exhaustion once in the
  cycle.
- THE FULL-BUILD REBUILD DISCIPLINE: under a mutation, the standalone
  rebuild must run the FULL npm run build (next build + the static/
  public copy steps) — a bare `next build` leaves the standalone dir
  without its static assets and the e2e server renders a broken page
  (the failure surfaces as "element(s) not found", not as a style
  diff).

The v92 queue (suggestions — verify against the rotation ledger
before executing): (1) the re-run cadence rotates to the next-oldest
candidate after this pair (the v86-era SAVINGS pair [the savings view
at desktop 1280x800, full-page], last re-shot v86 — now the oldest
remaining [v86 < v87 < v88 < v89 < v90 < v91]; the pair's FIFTH re-run
[v58 -> v65 -> v74 -> v80 -> v86 -> v92]), (2) the axe-core watch at
its next re-check point (only a 5.x wrapper changes the calculus), (3)
the deferred reference-write censuses (unchanged — out of bounds under
the v46 read-only rule).

## v92 — the savings pair's fifth re-run + the savings filter-interior + search-icon pin (2026-10-19)

The cycle (`docs/remediation-plan-v92.md` — the plan validated against
the codebase before execution; the narrative: `docs/session_222.md`):
the v91-era docs' v92 queue suggestion agreeing with the rotation
ledger — the FIFTEENTH consecutive agreement (the surface names
verified against vlm-shots-v86.sh's own surface list before the
derivation, the queue-prose verification lesson applied) — the v86-era
SAVINGS pair (the savings view at desktop 1280x800, full-page, last
re-shot v86; the pair's FIFTH re-run [v58 -> v65 -> v74 -> v80 -> v86
-> v92]), plus the axe watch at its re-check point (NO DRIFT: 4.14.0
npm-latest, no stable beyond, no 5.x, the v68 dedupe holds) and the
86th standing checks (ref-standing-v86.sh + standing-checks-v86.sh,
version-bumped from v85 across the three token families —
version-bump-only diffs verified by normalizing back and diffing
clean).

The workspace REBUILT (the fresh-clone path, the v86/v88/v90/v91
precedent): git clone at main @ e520a61, the tree clean; the
environment re-provisioned (npm ci 354 packages; .env written
[DATABASE_URL="file:../db/custom.db"]; db/ at the repo root,
db:generate + db:push + db:seed; chromium-1243; the paramiko ssh shim
outside the repo at /home/z/my-project/bin/ssh); the seedcheck exact
before any flow; the full baseline chain green on the first run (lint
-> typecheck -> 108 unit -> build -> 294 e2e [132+108+56 = 296 chunk
executions] -> 35/35 smoke).

The probe series (the v86 lineage, sed-derived with the version +
session-name + tmp-dir substitutions [vlm86 -> vlm92, refarbit86 ->
refarbit92, clonearbit86 -> clonearbit92, v86 -> v92; the shots'
session names refvlm86 -> refvlm92 / clonevlm86 -> clonevlm92 riding
the vlm86 -> vlm92 family]; the headers history-corrected to the FIFTH
re-run [v58 -> v65 -> v74 -> v80 -> v86 -> v92] + "last re-shot v86" +
the oldest-remaining bracket [v86 < v87 < v88 < v89 < v90 < v91] + the
agreement ordinal NINTH -> FIFTEENTH + the suggesting plan v85 -> v91;
the functional bodies verified version-bump-only by the normalize-back
diff — only the intentional history-correction comment lines differ):
- vlm-shots-v92.sh — the REFERENCE side (login on the first attempt;
  the parked pointer at (5,5); read-only — the v46 rule).
- clone-vlmshots-v92.sh — the CLONE side (the with-server :3200 parity
  server).
- vlm-compare-v92.mjs — the VLM pairwise.
- arbit-v92.sh — the both-sides census (the v86 census axes
  re-measured; the census runs regardless of the verdict — the v75
  convention) — whose CLONE half aborted in the chromium resource
  exhaustion (the v89/v91-documented symptom class), and was completed
  in the TWO-HALF controlled form:
  - ref-arbit-v92.sh — the reference half (derived by
    build-twohalf-v92.py, the census JS extracted once and embedded
    byte-identically in both halves).
  - clone-arbit-v92.sh — the clone half (the census JS byte-identical
    across the halves — the lines-1-153 identity verified by the md5
    line-block diff).
- savings-filter-arbit-v92.sh + savings-filter-clone-v92.sh — the
  supplemental one-shot both-sides census for the pin's own axes (the
  v87-v91 precedent), BUILT TWO-HALF from the start after the cycle's
  first exhaustion.
- pixel-diff-v92.mjs + crop-diff-v92.mjs + crop-analyze-v92.mjs +
  vlm-arbit-crop-v92.mjs + crop-left-v92.mjs + vlm-left-v92.mjs — the
  screenshot DATE-class arbitration chain (the v80/v86 discipline).

The findings:
1. The verdict DIFFERENT, every flag DOM-arbitrated to the v86 re-run's
   OWN documented classes (the seed-count grid; the v58
   DATA-CONDITIONAL footer + its derived internal-spacing note; the
   seed-data figures/badges/subtexts; the user-identity avatar; no FAB
   flag this cycle — the platform iframe chrome absent from this
   verdict's flag set).
2. The both-sides census (the two-half form) REPRODUCES the v86 census
   values EXACTLY — zero drift on every axis (the header/grid/card/
   titleRow/amount/footer/badge families; the docSW 1280 guard). NO NEW
   CLONE GAP — the iteration PIN-ONLY.
3. The v92 pin (+1 e2e = 295): the savings filter-interior + SEARCH-
   ICON census at 1280 (tests/e2e/items.spec.ts — the v91 pin family's
   THIRD variant [income + expenses pinned v91; the savings variant
   never] PLUS the search icon's computed chrome {svg/20x20/
   rgb(107,114,128)/absolute/left 12px} — the filter card's last
   never-pinned element, never pinned at ANY viewport on ANY view; the
   glyph spec holds the PATH data only, the class-string test the w-5
   SUBSTRING only) — the pin's own axes first measured byte-identical
   on both sides by the supplemental two-half census — GREEN on first
   run.
4. The pin-sanity mutation (the executed form — the viewport-scoped
   h-5 w-5 -> h-5 w-5 lg:h-6 at items-view.tsx:181, by LINE NUMBER;
   AT-lg because the pin runs at 1280): the failure diff reads as the
   searchIcon.h axis alone ("20" -> "24"); the full items.spec.ts under
   the mutation reads ONLY the v92 pin red (40 green) — cascade-free
   BY CONSTRUCTION (the icon is absolutely positioned, out of flow —
   no geometry moves; no spec asserts any search icon's computed w/h
   at ANY viewport); restored (git diff src/ = 0; the standalone
   REBUILD via the FULL npm run build; post-restore 41/41 green).
5. The full chain re-run GREEN: lint -> typecheck -> 108 unit -> build
   -> 295 e2e (133+108+56 = 297 chunk executions, zero flakes) ->
   35/35 smoke; the screenshots 9/16 BYTE-IDENTICAL + 7/16
   benign-pixel-arbitrated (6 DATE-TEXT-ONLY [03/04/05/06/07/16 — the
   fresh seed planted 2026-10-19 vs the committed set's 2026-10-18
   seed: the day number +1, every crop pair single-image
   VLM-arbitrated, the chrome byte-identical] + 1 RASTERIZATION-NOISE
   [08-calculator: every differing pixel <=4 channel units, both crops
   VLM-read "solid gray, no text"]; the regenerated set ships per the
   v80 discipline — the honest capture is committed).

**The v92 lessons:**
- THE TWO-HALF CENSUS, FROM THE START, AGAIN: the combined arbit
  script's clone half aborted in the chromium resource exhaustion (the
  v89/v91 symptom class) — the two-half form (the census JS
  byte-identity as the contract) is the recovery, and the supplemental
  one-shot censuses are again BUILT two-half from the start after the
  cycle's first exhaustion; the build-twohalf-v92.py helper (the
  census block extracted ONCE from the combined script and embedded in
  both halves) makes the byte-identity a construction guarantee rather
  than a hand-editing discipline.
- THE MUTATION-FAMILY ROTATION: the v91 mutation form (the search's fw
  axis via the view-local className) is NOT reusable on the same
  component once its axes are pinned on the sibling views — the Input
  instance is shared by all three items views, so an fw flip at
  >=1024px cascades to the v91 pin (TWO pins red). The v92 mutation
  rotates to a DIFFERENT element on the same surface — the search
  ICON's height — whose computed chrome is asserted by NO other spec at
  any viewport. When the pin family extends across the sibling
  variants of a shared component, the mutation axis must move to an
  element whose axes the earlier variants' pins do not hold.
- THE SEED-DAY DATE-CLASS, RE-CLASSIFIED PER PIXEL: the 16-item-details
  wide-region diff decomposed by the within-crop column-band analysis
  into the date-text glyphs (the right band) + a sub-perceptual
  <=4-channel noise tail (the left band, both crops VLM-read "solid
  gray, no chrome") — the DATE-TEXT-ONLY and RASTERIZATION-NOISE
  classes can CO-OCCUR in one file; the crop-band analysis plus the
  targeted band reads settle it without a full-page verdict.

The v93 queue (suggestions — verify against the rotation ledger
before executing): (1) the re-run cadence rotates to the next-oldest
candidate after this pair (the v87-era LOGIN + CALCULATOR pair [the
calculator dialog at desktop 1280x800], last re-shot v87 — now the
oldest remaining [v87 < v88 < v89 < v90 < v91 < v92]; the pair's FIFTH
re-run [v59 -> v66 -> v75 -> v81 -> v87 -> v93] — the surface names
verified against vlm-shots-v87.sh's own header this session), (2) the
axe-core watch at its next re-check point (only a 5.x wrapper changes
the calculus), (3) the deferred reference-write censuses (unchanged —
out of bounds under the v46 read-only rule).

## The v93 cycle (executed 2026-10-19 — the v87-era login + calculator pair's fifth re-run)

The queue's own paragraph above was EXECUTED this cycle. The probe series
derived from the v87 lineage by the sed substitution families
(vlm87->vlm93, login87->login93, calc87->calc93, v87->v93 — the shots'
session names riding the families), the headers history-corrected to the
FIFTH re-run [v59 -> v66 -> v75 -> v81 -> v87 -> v93] + "last re-shot
v87" + the oldest-remaining bracket [v87 < v88 < v89 < v90 < v91 < v92]
+ the queue agreement ordinal TENTH -> SIXTEENTH + the suggesting plan
v86 -> v92; the functional bodies verified version-bump-only by the
normalize-back diff (only the intentional history-correction comment
lines differ; the residual "87" tokens all legitimate history
references). The new probes this cycle: vlm-shots-v93.sh +
login-shots-v93.sh + clone-vlmshots-v93.sh + clone-login-shots-v93.sh +
vlm-compare-v93.mjs + arbit-v93.sh + build-twohalf-v93.py (the two-half
builder for the two-census-block arbit form — the CALC + LOGIN census
blocks extracted once, embedded byte-identically across the halves by
the md5 line-block contract) + ref-arbit-v93.sh + clone-arbit-v93.sh +
totalcard-arbit-v93.sh + totalcard-clone-v93.sh (the supplemental
one-shot, BUILT two-half from the start) + ref-standing-v87.sh +
standing-checks-v87.sh (the 87th standing checks, version-bumped from
the v86 pair across the three token families).

The verdicts: the LOGIN pair IDENTICAL the FOURTH consecutive
(v75/v81/v87/v93 — zero style flags, the both-sides census
byte-identical on every axis); the CALCULATOR pair DIFFERENT with every
flag DOM-arbitrated to the v75/v81/v87 re-runs' own documented classes
(the v66 DATA-CONDITIONAL will-update span + its derived card-height
note [the totalCard box itself 720x90 byte-identical]; the v75/v81/v87
POINTER-POSITION actions perception [actionsAtRest {opacity: 0,
btnCount: 2} byte-identical on both sides]; the seed-data figures; no
FAB flag this cycle; the close census axis absent ref-side — the
v87-documented lost-accessible-name observation holding, the clone's
close census the v87 pin's own values, the clone the SUPERSET). The
both-sides census — executed in the TWO-HALF controlled form BUILT
two-half from the start — REPRODUCED the v87 census values EXACTLY
(zero drift on every axis). NO NEW CLONE GAP — the v93 iteration
PIN-ONLY.

The +1 e2e pin: the totalCard INNER-TEXT census at 1280
(tests/e2e/calculator.spec.ts — the v73 390 summary-text family's
DESKTOP twin [the amount/basedOn/willUpdate] PLUS the "Total
Calculated" LABEL leaf's typography — never pinned at ANY viewport —
PLUS the two summary rows' chrome + the box re-affirm + the docSW 1280
guard), the pin's own axes first measured byte-identical on both sides
by the supplemental two-half census (the reference's NATIVE 1-row state
read-only; the clone's added-then-fully-restored twin; the seedcheck
exact after the run). The pin-sanity mutation: the viewport-scoped
text-sm font-medium -> text-sm font-medium lg:font-semibold at
calculator-dialog.tsx:153 (by LINE NUMBER, AT-lg because the pin runs at
1280) — ONLY the v93 pin red (17 green under the mutation), the failure
diff reads as the label.fw axis ALONE ("500" -> "600") — cascade-free
BY CONSTRUCTION (the inline label's lh 20px bound by the amount's 32px
row; the totalCard box unchanged; no spec asserts the label's computed
styles at ANY viewport; the lg: variant inert below 1024px — every
390/640 pin green).

The screenshots: **16/16 BYTE-IDENTICAL** — the same-day-seed
byte-identity law in its purest form (the seed planted and the shots
taken on the same calendar day 2026-10-19, byte-for-byte reproduction,
ZERO arbitration needed this cycle — the v92 cycle's cross-day re-seed
needed 7 pixel-arbitrations; the same-day capture needs none).

The v93 cycle's operational lessons:

- THE REAPING BUDGET, BETWEEN THE HALVES, FROM THE START: the
  clone-side shots' first run hit the chromium resource-exhaustion
  symptom (70 zombie processes observed; the EMPTY-eval signature — no
  error surface, the v89-documented class). The fix (pkill -f
  agent-browser + the session-file sweep) is now budgeted as a STANDING
  STEP between the reference and clone halves of EVERY long probe, not
  just the recovery. CAUTION: a `bash -c` whose command string contains
  the literal "agent-browser" self-matches the pkill pattern and dies
  instantly (SIGTERM at launch) — run the reaping as its OWN tool call,
  never inline in a compound command that names the pattern.
- THE TWO-HALF CENSUS, BUILT FROM THE START, AGAIN — now for the
  TWO-census-block form too: build-twohalf-v93.py extracts BOTH census
  JS blocks (CALC + LOGIN) once and embeds them byte-identically across
  the halves (the md5 line-block contract generalized from one block to
  N blocks); the supplemental one-shots remain two-half from the start
  (the v92 lesson holding).
- THE SESSION-LOG-ONLY COMMIT CLASS: a pulled docs-only commit (the
  926f193 session-log) requires ZERO re-provisioning — the npm ci
  state, the db, the chromium, and the shim all carry over when the
  delta touches no src/ or lockfile path; the baseline chain re-run on
  the carried-over environment IS the shipped-state verification (the
  tree clean at the pulled HEAD).
- THE LABEL-FIRST FAMILY EXTENSION: when a pin family extends to a new
  viewport (the v73 390 -> v93 1280 twin), the mutation axis should
  target the family member never pinned at ANY viewport (the label) —
  the viewport-twin axes are held by the 390 pin whose lg:-scoped
  inertness keeps it green, but the label's never-pinned-anywhere
  status makes its flip the cleanest single-axis proof that the NEW pin
  bites.

The v94 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after this pair (the v88-era NETWORTH + DRILL-DOWN pair [the NETWORTH
view + the DASHBOARD's drill-down EXPANDED state, both desktop
1280x800 full-page], last re-shot v88 — now the oldest remaining [v88 <
v89 < v90 < v91 < v92 < v93]; the pair's FIFTH re-run [v60 -> v67 ->
v76 -> v82 -> v88 -> v94] — the surface names verified against
vlm-shots-v88.sh's own header this session), (2) the axe-core watch at
its next re-check point (only a 5.x wrapper changes the calculus), (3)
the deferred reference-write censuses (unchanged — out of bounds under
the v46 read-only rule).


## The v94 cycle (executed 2026-10-19 — the v88-era networth + drill-down pair's fifth re-run)

The queue's own paragraph above was EXECUTED this cycle. The probe series
derived from the v88 lineage by the sed substitution families
(vlm88->vlm94, v88->v94, FOURTH->FIFTH, ELEVENTH->SEVENTEENTH — the
shots' session names riding the families), the headers history-corrected
to the FIFTH re-run [v60 -> v67 -> v76 -> v82 -> v88 -> v94] + "last
re-shot v88" + the oldest-remaining bracket [v88 < v89 < v90 < v91 <
v92 < v93] + the v88-era-pair (not v60-era) correction; the functional
bodies verified version-bump-only by the normalize-back diff (only the
intentional history-correction comment lines differ; the residual "88"
tokens all legitimate history references). The arbit lineage's SESSION
NAMES (refar88/clonear88) ride the "ar" token family, NOT the "v88"
family — the first sed pass missed them; an explicit second pass
(refar88->refar94/clonear88->clonear94) corrected the derivation before
any execution. The new probes this cycle: vlm-shots-v94.sh +
clone-vlmshots-v94.sh + vlm-compare-v94.mjs + arbit-v94.sh (the
intermediate combined form, header-corrected) + build-twohalf-v94.py
(the two-half builder — the ARBIT_A + ARBIT_B census blocks extracted
once, embedded byte-identically across the halves by the md5
line-block contract [a9cdcc96 / baa22974]) + ref-arbit-v94.sh +
clone-arbit-v94.sh + build-nwsection-v94.py +
nwsection-arbit-v94.sh + nwsection-clone-v94.sh (the supplemental
one-shot for the v94 pin's own axes, BUILT two-half from the start —
the census JS byte-identical by the md5 line-block diff [f8b3cabf]) +
ref-standing-v88.sh + standing-checks-v88.sh (the 88th standing
checks, version-bumped from the v87 pair across the three token
families).

The verdicts: BOTH pairs DIFFERENT with every flag DOM-arbitrated to
the v82/v88 re-runs' own documented classes — the NETWORTH pair's
flags: the avatar (the user-identity class), the "Edit with Base44"
FAB (the platform-chrome class, RE-ARBITRATED LIVE by re-running
base44-fab-arbit-v91.sh: fabCount 0 + bodyHasBase44 false on BOTH
sides — the FAB lives in the reference's platform iframe chrome), and
the seed-data figures (the 1-asset vs 3-asset groups, the ∞:1 vs
0.21:1 ratio); the DRILL-DOWN pair's flags: the "Dashboard link
highlighted in the clone" (the v56 SUPERSET class — the reference's
link INERT rgb(63,63,70)/400 vs the clone's ACTIVE white/500), the
avatar, the "progress bar longer" (the pct × 568 DATA class — fillW
ref 173 vs clone 357 on the byte-identical 568×12 track, the v82/v88
values REPRODUCED EXACTLY six re-runs later), the "donut percentage
labels absent in the ref" (the v60 PERCEPTION class — the reference
DOES render its labels: count 4, labelLineCount 0, 16px, black, 3
sectors, the chrome byte-identical), the "'Total Expense' vs 'Total
Expenses'" (the v82 VLM MISREAD class, re-arbitrated live by re-running
stat-divider-arbit-v88.sh: both sides' titles "Total Income"/"Total
Savings"/"Total Expenses" plural, byte-identical), the "divider lines
missing in the ref" (the v88 VLM MISREAD class, re-arbitrated live by
the same one-shot: the divider {DIV, h 1, bg rgb(229,231,227),
flexGrow 1} byte-identical on every card), and the seed-data classes.
The both-sides census — executed in the TWO-HALF controlled form BUILT
two-half from the start — REPRODUCED the v88 census values EXACTLY
(zero drift on every axis; the labelBlock's width the v82
DATA-CONDITIONAL class [ref 304 vs clone 357 — the 48px figure's text
length]). NO NEW CLONE GAP — the v94 iteration PIN-ONLY.

The +1 e2e pin: the networth SECTION-HEADER row census at 1280
(tests/e2e/networth.spec.ts — the tab panel's "Assets" header row,
never pinned at ANY viewport: the row's flex chrome + the h2
typography + the count subtitle P + the Add Asset button's chrome on
this row + the row-to-group rhythm + the groupH3 re-affirm), the pin's
own axes first measured byte-identical on both sides by the
supplemental two-half census (BOTH sides read-only this cycle — the
reference's populated Assets panel passively measured; the clone's
seeded panel passively measured; the seedcheck exact after the run).
The pin-sanity mutation: the viewport-scoped text-2xl font-bold ->
text-2xl font-bold lg:font-black at net-worth-view.tsx:418 (by LINE
NUMBER, AT-lg because the pin runs at 1280; the line-scoping keeps the
file's OTHER text-2xl font-bold instances untouched) — ONLY the v94
pin red (29 green under the mutation), the failure diff reads as the
h2.fw axis ALONE ("700" -> "900") — cascade-free BY CONSTRUCTION (the
h2's lh 32px bound by text-2xl's line-height — a font-weight flip does
not scale it; no spec asserts the "Assets" section h2's computed
styles at ANY viewport; lg:font-black appears NOWHERE in src/).

The screenshots: **16/16 BYTE-IDENTICAL** — the same-day-seed
byte-identity law, the SECOND consecutive pure-form cycle (the seed
planted and the shots taken on the same calendar day 2026-10-19,
byte-for-byte reproduction, ZERO arbitration needed).

The v94 cycle's operational lessons:

- THE REAPING BUDGET AS A STANDING STEP, APPLIED CLEAN: the v93
  lesson (the between-halves reap budgeted from the start) applied as
  a PRE-RUN + BETWEEN-HALVES step on EVERY probe this cycle — zero
  resource-exhaustion symptoms throughout (the 70-zombie class
  absent). The self-matching pkill caution respected via the
  `agent[-]browser` character-class form (a bash -c whose command
  string contains the literal "agent-browser" self-matches the pkill
  pattern and dies instantly).
- THE SECOND-PASS SESSION-NAME SED: the arbit lineage's session names
  (refar88/clonear88) ride the "ar" token family, NOT the "v88"
  version family — the first sed pass (v88->v94) missed them; the
  explicit second pass (refar88->refar94/clonear88->clonear94)
  corrected the derivation BEFORE any execution. Future derivations:
  sweep for residual old tokens by SESSION-NAME pattern, not just the
  version family.
- THE MISREAD-CLASS LIVE RE-ARBITRATION: when a re-run cycle's VLM
  verdict re-flags a documented MISREAD class (the v82 stat-title, the
  v88 divider), the existing one-shot census is RE-RUN live rather
  than re-derived — the disproven-in-advance form (the flag's class
  already documented, the re-run the fresh evidence). The same for the
  FAB platform-chrome class (base44-fab-arbit-v91.sh re-run).

The v95 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after this pair (the v89-era DASHBOARD pair [the BUDGET GUIDELINES
card + the QUICK-ACTION card row, both below-the-fold surfaces of the
dashboard FULL-PAGE at desktop 1280x800], last re-shot v89 — now the
oldest remaining [v89 < v90 < v91 < v92 < v93 < v94]; the pair's FIFTH
re-run [v61 -> v68 -> v77 -> v83 -> v89 -> v95] — the surface names
verified against vlm-shots-v89.sh's own header this session), (2) the
axe-core watch at its next re-check point (only a 5.x wrapper changes
the calculus), (3) the deferred reference-write censuses (unchanged —
out of bounds under the v46 read-only rule).

## The v95 cycle (executed 2026-10-19/20 — the v89-era dashboard pair's fifth re-run)

The queue's own paragraph above was EXECUTED this cycle. The probe series
derived from the v89 lineage by the sed substitution families
(vlm89->vlm95, v89->v95, FOURTH->FIFTH, TWELFTH->EIGHTEENTH — the
shots' session names riding the families) PLUS the explicit second-pass
session-name substitutions (refar89->refar95, clonear89->clonear95 —
the "ar" token family, the v94 lesson applied from the start), the
headers history-corrected to the FIFTH re-run [v61 -> v68 -> v77 ->
v83 -> v89 -> v95] + "last re-shot v89" + the oldest-remaining bracket
[v89 < v90 < v91 < v92 < v93 < v94] + the v89-era-pair (not v61-era)
correction + the "after v89-v94" (not "after v83-v88") correction; the
functional bodies verified version-bump-only by the normalize-back
diff (only the intentional history-correction comment lines differ).
The new probes this cycle: vlm-shots-v95.sh + clone-vlmshots-v95.sh +
vlm-compare-v95.mjs + arbit-v95.sh (the intermediate combined form,
header-corrected) + build-twohalf-v95.py (the two-half builder — the
THREE census blocks [ARBIT_G/ARBIT_Q/ARBIT_X] extracted once, embedded
byte-identically across the halves by the md5 line-block contract
[b500dd29 / da04e995 / 7a381755]) + ref-arbit-v95.sh +
clone-arbit-v95.sh + build-qa-timing-v95.py + qa-timing-arbit-v95.sh +
qa-timing-clone-v95.sh (the supplemental one-shot for the v95 pin's own
axes, BUILT two-half from the start — the census JS byte-identical by
the md5 line-block diff [ba296202]) + ref-standing-v89.sh +
standing-checks-v89.sh (the 89th standing checks, version-bumped from
the v88 pair across the three token families).

The verdict: IDENTICAL — ZERO style flags on the pair's own target
surfaces (the Budget Guidelines card and the Quick Action cards both
"visually identical" per the VLM's own targeted analysis) — the THIRD
consecutive IDENTICAL verdict for this pair [v83 -> v89 -> v95]. The
only flags the documented standing classes: the seed-data figures (the
allocation bar 30.5%-vs-62.8%, the balance $3475-vs-$2065, the stat
figures, the donut proportions), the root-URL active-nav highlight
(the v56 SUPERSET class), the "Edit with Base44" FAB (the
platform-chrome class), and the avatar "U" vs "D" (the user-identity
class).

The both-sides census — executed in the TWO-HALF controlled form BUILT
two-half from the start — REPRODUCED the v89 census values EXACTLY
(zero drift on every axis): PART G the guidelines card 468x348/radius
12px/border/bg/the header pad 24px/fs 16px/fw 600/rgb(26,58,46)/lh
16px/tracking -0.4px/the body pad 0px 24px 24px/the three tiles
418x78 with the Needs/Wants/Savings tints and the label/pct/desc
chrome — the only delta the shadow's transparent lead-layer count (the
v66 computed-form INVISIBLE class); PART Q the grid 304px x3/gap
24px/w 960/the three cards 304x90/radius 16px/pad 24px/white/border/
the 40x40 tinted tiles/the 20px icons/the labels/the 0.5-opacity
pluses/transition 0.2s — the TWO census deltas both documented classes
(the grid mt [ref 0px vs clone 32px — the rendered gap IDENTICAL at
340, the v77 mechanism class] and the label finder's wrapper catch
[ref leaf 500/rgb(26,58,46) vs clone wrapper 400/rgb(10,10,10) — the
v61 label lesson: the clone's LEAF span carries the identical chrome,
pinned green by the v61 F3 pin]); PART X cardBottom 1122/gridTop
1462/gap 340 on BOTH sides, byte-identical. NO NEW CLONE GAP — the v95
iteration PIN-ONLY.

The +1 e2e pin: the quick-action TRANSITION-TIMING family census at
1280 (tests/e2e/dashboard.spec.ts — the never-pinned family: the three
cards' transitionTimingFunction + transitionDelay [the v89 pin holds
the duration/property only], the three tinted tiles'
transition-transform family, and the three plus icons'
transition-opacity family — grep-verified never pinned at ANY
viewport), the pin's own axes first measured byte-identical on both
sides by the supplemental two-half census (both sides read-only; the
seedcheck exact after the run). The pin-sanity mutation: the
viewport-scoped transition-all duration-200 -> transition-all
duration-200 lg:ease-linear at dashboard-view.tsx:885 (by LINE
NUMBER, AT-lg because the pin runs at 1280; the line-scoping keeps
the file's OTHER transition-all duration-200 instance [line 578, the
breakdown category card] untouched) — ONLY the v95 pin red (41 green
under the mutation), the failure diff reads as the cardTiming axis
ALONE ("cubic-bezier(0.4, 0, 0.2, 1)" -> "linear") — cascade-free BY
CONSTRUCTION (a timing-function flip affects no geometry and no
computed style any other pin asserts; lg:ease-linear appears NOWHERE
in src/).

The screenshots: **16/16 BYTE-IDENTICAL** — the same-day-seed
byte-identity law, the THIRD consecutive pure-form cycle (the seed
planted and the shots taken on the same calendar day, byte-for-byte
reproduction, ZERO arbitration needed).

The v95 cycle's operational lessons:

- THE TEMPLATE-BRACE GENERATOR BUG: the two-half generator script
  (build-qa-timing-v95.py) was written with .format()-style doubled
  braces but applied with .replace() — the generated LOGIN_JS kept
  literal `{{`/`}}`, a JS syntax error that made agent-browser eval
  return EMPTY on every attempt (the empty-eval signature — the same
  SYMPTOM class as the v89 chromium resource exhaustion, but the
  CAUSE was the generator, not the sandbox). The diagnosis that
  separated them: a manual `agent-browser open` + `snapshot` against
  the reference (the page loaded fine — the site was UP, the script
  was broken). The discipline: bash -n + a spot grep for doubled
  braces after ANY generator run, BEFORE executing the probe; when
  the empty-eval signature appears, check the script first if a fresh
  generator produced it, and only then suspect the sandbox.
- THE TWO-HALF FORM AS THE DEFAULT (the v92/v93/v94 lesson, applied
  clean): the v95 census + the supplemental census were BOTH built
  two-half from the start (the builders extract the census blocks
  once, the md5 line-block contract) — zero resource-exhaustion
  symptoms, no mid-run splits needed, the reaping budget applied as
  the standing pre-run + between-halves step throughout.
- THE v4 TRANSITION-PROPERTY COMPUTED-FORM CLASS (NEW): Tailwind v4's
  `transition-transform` computes `transform, translate, scale,
  rotate` where v3 computed `transform` — a property-LIST superset
  with identical rendered behavior (the tile's only animated property
  `scale` covered by BOTH lists). The pin form for such axes:
  CONTAINS, never exact (the v66 shadow lead-layer / v82 labelBlock
  width / v94 margin-attribution family's newest member). The
  reference-side value was measured in the same census run — the
  class documented from LIVE both-sides evidence, not assumption.

The v96 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after this pair (the v90-era MOBILE 390 twins [the /networth + the
dashboard FULL-PAGE pair at 390x844], last re-shot v90 — now the
oldest remaining [v90 < v91 < v92 < v93 < v94 < v95]; the pair's FIFTH
re-run [v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96] — verify the
surface names against vlm-shots-v90.sh's own header before the
derivation), (2) the axe-core watch at its next re-check point (only a
5.x wrapper changes the calculus), (3) the deferred reference-write
censuses (unchanged — out of bounds under the v46 read-only rule).

## The v96 cycle (executed 2026-10-20 — the v90-era MOBILE 390 twins' fifth re-run)

The queue's own paragraph above was EXECUTED this cycle. The probe series
derived from the v90 lineage by derive-v96-series.py (the PERSISTED
derivation script — the generic swaps [vlm90->vlm96, v90->v96, the
session names, the /tmp dir] followed by the exact-fragment history
corrections [the queue source "the v95 plan's own suggestion", the
oldest-remaining list, the FIFTH re-run bracket, FOURTH->FIFTH, the
census-axes provenance, the verdict note], every correction verified
applied — the DERIVATION MISS-REPORT DISCIPLINE: the script reports each
correction's hit/miss and the one first-run MISS [the lowercase 'the' in
the verdict-note fragment] was caught by the report itself and fixed
before any probe executed; zero residual old tokens across all four
files; bash -n + node --check clean). The new probes this cycle:
vlm-shots-v96.sh + clone-vlmshots-v96.sh + vlm-compare-v96.mjs +
arbit-v96.sh (the intermediate combined form, header-corrected) +
build-twohalf-v96.py (the two-half builder — the TWO census blocks
[NW_CENSUS 42 lines / DASH_CENSUS 87 lines] extracted once, embedded
byte-identically across the halves by the md5 line-block contract
[82cf8a43 / 85e4ec7e]) + ref-arbit-v96.sh + clone-arbit-v96.sh +
derive-standing-v96.py (the persisted standing derivation — the 90th
pair, version-bump-only verified by the normalize-back diff) +
ref-standing-v90.sh + standing-checks-v90.sh + figclip-clone-v96.sh (the
NEW clipped-figure flag's one-shot arbitration) + build-headrow-v96.py +
headrow-arbit-v96.sh + headrow-clone-v96.sh (the supplemental two-half
census for the v96 pin's own axes — the census JS byte-identical by the
md5 line-block diff [519ef222]; the doubled-brace spot grep clean, the
v95 template-brace lesson pre-applied) + pixel-diff-v96.py (the
07-add-item-modal DATE-class arbitration).

The verdicts: BOTH DIFFERENT (the pair's documented verdict class — the
same flag-set classes as the v84/v90 re-runs) with every flag
DOM-arbitrated: the stat-tile side-by-side-vs-stacked the v41
mobile-superset class (the census: the statGrid cols ref
"175.828px 175.844px" 2-col vs clone "294px" 1-col, the gap 16px
IDENTICAL, the tiles ref 176x84 vs clone 294x84 — the h 84
byte-identical); the clipped negative figure the NEW flag —
DOM-arbitrated as a VLM MISREAD by the figclip one-shot census (the
figure H2 at x=48 w=179 h=32, the textRect x=48 w=179 — the text starts
EXACTLY at the content-left edge [textLeftOfContent 0, zero overhang]
and ends 115px INSIDE the content-right; figureScrolls false; docSW 390
— the figure fully in-bounds on every axis, no clipping exists; THE
FLUSH-LEFT FIGURE PERCEPTION CLASS: the VLM flags a "clipped" negative
currency figure when the text starts flush at the content-box left edge
— the arbitration is the Range-walk textRect vs the padding-aware
content box, NOT the element rect alone); the subtitle wrap-point the
v62 width-delta class (the census: the chrome byte-identical [fs
16px/fw 400/rgb(107,114,128)/lh 24px, the P h 48, the block h 92], BOTH
sides 2 DOM lines; the reference's own 395px overflow shifts its wrap);
the FAB the platform-chrome class; the figures/counts/donut the
seed-data classes. The two-half census REPRODUCES the v90 values
EXACTLY — zero drift on every axis (the summary
card/statGrid/tiles/medallion/trendIcon families; the subtitle chrome;
the breakdown card's svg family [svgCount 7, the 16/14 alternation];
the children heights; the spendingCard finder reading the SAME fallback
string on BOTH sides — the heading is a div, not an h1-h4, on both
sites, the parity-correct rendering). NO NEW CLONE GAP.

The standing-script timing artifact (NEW this cycle): the
reference-side standing check's R-bug-4 (/networth overflow) read docSW
390/390 on the script's sleep-3 — the eval raced the reference's
client-side boot and measured the PRE-RENDER document; the 8s+2s settle
re-read measured the true 464. THE DISCIPLINE: when a standing bug
check reads CLEAN against its own documented-live history (the bug live
89 consecutive checks), re-measure with an explicit settle-wait before
recording any state change — a bug that has been live for 89
consecutive checks does not vanish on the 90th without a DOM-visible
cause.

The DATE-class screenshot arbitration (the v96 form): the cycle crosses
the UTC midnight boundary (the seed + the baseline shots Oct 19 22:41
UTC; the regeneration Oct 20 00:1x UTC) — the Add Item form's default
date (budget-item-dialog.tsx:83, todayIso(), computed at RENDER time)
rolls "2026-10-19" -> "2026-10-20" and the 07-add-item-modal shot
differs by exactly the two day digits: the pixel-diff-v96.py
arbitration localizes the delta to a 32x22px region at x1535 (the
v75 acceptance form: width <= 48, height <= 40, x > 1000 — the date
field in the dialog's form column right-of-center at the 2x DPR shot);
the other 15 shots byte-identical; the committed set updated with the
new 07 shot (the date-class delta documented, never a regression).

The v97 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the twins (the v91-era ITEMS pair [the INCOME + EXPENSES view
pair at desktop 1280x800], last re-shot v91 — now the oldest remaining
[v91 < v92 < v93 < v94 < v95 < v96]; the pair's SIXTH re-run
[v57 -> v64 -> v70 -> v79 -> v85 -> v91 -> v97] — verify the surface
names against vlm-shots-v91.sh's own header before the derivation),
(2) the axe-core watch at its next re-check point (only a 5.x wrapper
changes the calculus), (3) the deferred reference-write censuses
(unchanged — out of bounds under the v46 read-only rule).

## v97 — the items pair's sixth re-run (the missing-middle listbox pin)

The v97 iteration (docs/remediation-plan-v97.md): the re-run cycle's
next-oldest candidate — the ledger-verified queue (the v96-era docs'
v97 suggestion AGREEING with the rotation ledger: the v91-era ITEMS
pair [the INCOME + EXPENSES view pair at desktop 1280x800, full-page],
last re-shot v91, the oldest remaining [v91 < v92 < v93 < v94 < v95 <
v96]; the pair's SIXTH re-run [v57 -> v64 -> v70 -> v79 -> v85 -> v91
-> v97] — the TWENTIETH consecutive queue/ledger agreement, the surface
names verified against vlm-shots-v91.sh's own header before the
derivation), plus the axe watch at its re-check point (NO DRIFT —
4.14.0 npm-latest, only rc/next sha prereleases beyond, no 5.x, the
v68 dedupe holds) and the 91st standing checks (version-bumped from v90
across the three token families — version-bump-only diffs verified by
normalizing back and diffing clean).

The probe series (the v91 lineage, derive-v97-series.py — the generic
swaps then the exact-fragment history corrections [last-re-shot v85 ->
v91, FIFTH -> SIXTH, the re-run bracket extension, the
every-other-pair list], every correction's hit/miss REPORTED, all four
applied clean on the first run; bash -n + node --check clean; zero
residual old tokens — the legitimate "last re-shot v91" provenance +
the SIXTH bracket whitelisted by context):
- vlm-shots-v97.sh — the REFERENCE side (login on the first attempt;
  the parked pointer at (5,5); read-only — the v46 rule).
- clone-vlmshots-v97.sh — the CLONE side (the with-server :3200 parity
  server).
- vlm-compare-v97.mjs — the VLM pairwise.
- arbit-v97.sh + ref-arbit-v97.sh + clone-arbit-v97.sh — the
  both-sides census, BUILT two-half from the start via
  build-twohalf-v97.py (the ONE CENSUS_JS block [193 lines]
  byte-identical across the halves — the md5 line-block contract
  b55dcd29).
- base44-fab-arbit-v97.sh — the one-shot both-sides DOM re-arbitration
  of the recurring FAB flag (fabCount 0 + bodyHasBase44 false on BOTH
  sides — the platform-chrome class; this cycle the VLM attributed the
  FAB to the REFERENCE, the non-inverted form of the v85/v91-documented
  attribution class).
- listbox-arbit-v97.sh + listbox-clone-v97.sh — the supplemental
  two-half census for the pin's own axes (the filter listbox PANEL +
  option-resting interior at 1280), BUILT two-half from the start via
  build-listbox-v97.py (the census JS byte-identical by the md5
  line-block contract 34c916da).

The findings:
1. Both verdicts DIFFERENT, every flag DOM-arbitrated to the v85/v91
   re-run's OWN documented classes (the v57 payment-chip
   DATA-CONDITIONAL footer — PROVEN by the reference's own income
   card's footer childCount 2 with the "Bank Account" chip while its
   expense items ship none; the v57/v70b Recurring superset wrap [the
   card h 200-vs-230, the badgeRow h 22-vs-52]; the seed-count grids;
   the user-identity avatar; the seed-data figures/dates/badges).
2. The both-sides census (the two-half form) REPRODUCES the v85/v91
   census values EXACTLY — zero drift on every axis (the
   avatar/grid/card/titleRow/amount/footer/badge/filterCard families;
   the docSW 1280 guard; the income template's last-column sub-pixel
   the column-distribution rounding noise WITHIN the documented
   309.328px family). NO NEW CLONE GAP — the iteration PIN-ONLY.
3. The v97 pin (+1 e2e = 300): the filter LISTBOX PANEL +
   OPTION-RESTING interior census at 1280 (tests/e2e/items.spec.ts —
   the MISSING-MIDDLE family: the v91 pin holds the TRIGGER's resting
   chrome, the v36 S2 the OPTION's focus-state family, but the PANEL
   container itself [bg/radius/border/shadow/max-h/overflow/z + the
   viewport's 4px pad] and the option's RESTING interior
   [fs/fw/color/pad/radius/h] were never pinned at ANY viewport in ANY
   spec — the family-extension survey walking the COMPONENT LAYERS
   [trigger -> panel -> viewport -> option]) — the pin's own axes first
   measured byte-identical on both sides by the supplemental two-half
   census — GREEN on first run.
4. The pin-sanity mutation (the executed form — the SelectContent
   panel's rounded-md -> rounded-lg at src/components/ui/select.tsx:68,
   by LINE NUMBER; the line-scoping keeps the SelectTrigger's own
   rounded-md at line 19 untouched [the v91 pin's 6px trigger axis]):
   the failure diff reads as the panel radius axis ALONE ("6px" ->
   "8px"); the full items.spec.ts under the mutation reads ONLY the
   v97 pin red (41 green) — cascade-free BY CONSTRUCTION — then
   restored (git diff src/ = 0; the standalone REBUILD; the
   post-restore full run 42/42 green).
5. The full chain re-run GREEN: lint -> typecheck -> 108 unit -> build
   -> 300 e2e (135+96+71 = 302 chunk executions, zero flakes) ->
   35/35 smoke; the screenshots 16/16 BYTE-IDENTICAL (the same-day
   regeneration — both sides Oct 20 UTC, the 07-add-item-modal's day
   digits matching, no midnight crossing this cycle).

**The v97 lessons:**
- THE CENSUS RENDER-RACE GENERALIZATION (the v79 expiry-twin, extended):
  the reference-side expenses census read "no match" — not the session
  expiry (the v79 form) but the eval racing the page's client-side
  render (the timing-artifact family). The generalized discipline: ANY
  multi-eval reference flow treats a "no match"/empty census as a
  possible expiry OR render race first (re-login + settle-wait +
  re-read) before suspecting drift — and never records the state change
  on a single raced read.
- THE PANEL-CHROME MISSING-MIDDLE FAMILY (NEW): the v91/v92
  trigger-interior pins and the v36 option-state pins bracket the
  filter select's popover, but the PANEL container itself was never
  pinned at any viewport — the family-extension survey should walk the
  COMPONENT LAYERS (trigger -> panel -> viewport -> option), not just
  the axes of one layer.
- THE TWO-HALF FORM AS THE DEFAULT (the v92..v96 lesson, applied clean
  again): every census this cycle BUILT two-half from the start — zero
  resource-exhaustion symptoms.

The v98 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the items pair (the v92-era SAVINGS pair [the SAVINGS view + the
goal-card interior pair at desktop 1280x800], last re-shot v92 — now
the oldest remaining [v92 < v93 < v94 < v95 < v96 < v97]; the pair's
re-run bracket to be verified against vlm-shots-v92.sh's own header
before the derivation), (2) the axe-core watch at its next re-check
point (only a 5.x wrapper changes the calculus), (3) the deferred
reference-write censuses (unchanged — out of bounds under the v46
read-only rule).

## v98 — the savings pair's sixth re-run + the goal-card action-menu pin (2026-10-20)

The cycle (`docs/remediation-plan-v98.md` — the plan validated against
the codebase before execution; the narrative: `docs/session_236.md`):
the v97-era docs' v98 queue suggestion agreeing with the rotation
ledger — the TWENTY-FIRST consecutive agreement (the surface names
verified against vlm-shots-v92.sh's own header before the derivation,
the queue-prose verification lesson applied) — the v92-era SAVINGS pair
(the savings view at desktop 1280x800, full-page, last re-shot v92; the
pair's SIXTH re-run [v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98]),
plus the axe watch at its re-check point (NO DRIFT: 4.14.0 npm-latest,
no stable beyond, no 5.x, the v68 dedupe holds) and the 92nd standing
checks (ref-standing-v92.sh + standing-checks-v92.sh, version-bumped
from v91 across the three token families — version-bump-only diffs
verified by normalizing back and diffing clean; the persisted
derive-standing-v98.py).

The workspace REBUILT (the fresh-clone path, the v86/v88/v90/v91/v92
precedent — the sandbox had been reset): git clone at main @ 9152c18,
the tree clean; the environment re-provisioned (npm install; .env
written [DATABASE_URL="file:../db/custom.db"]; db/ at the repo root,
db:generate + db:push + db:seed; chromium-1243 installed for the pinned
@playwright/test 1.63.0 — the cache's pre-installed 1200 build belongs
to a different playwright generation, the first e2e chunk failed with
"Executable doesn't exist" until the install; the
/home/z/my-project/tool-results/ dir re-created for with-server.sh); the
seedcheck exact before any flow (7 items / rent 1850 / expensesTotal
2235 / 0 line items / 3 assets / 2 liabilities); the full baseline
chain green on the first run after the browser install (lint ->
typecheck -> 108 unit -> build [robots + sitemap prerendered] -> 300
e2e [135+96+71 = 302 chunk executions = 300 unique, zero flakes] ->
35/35 smoke). The two commits since the v97 push (d4b77c5 + 9152c18)
audited session-log-only (session_234.md + session_235.md — ZERO src/
or lockfile deltas).

The probe series (the v92 lineage, derived via the PERSISTED
derive-v98-series.py — the generic swaps then the exact-fragment
history corrections, every correction's hit/miss REPORTED; the one
first-run MISS [the arbit header's line break — "(the savings view
full-page —
# the v86-era..." vs the assumed "...full-page — the
#..."]
caught by the report itself and fixed before any probe executed — the
v96 miss-report discipline; bash -n + node --check clean on all four;
zero residual old tokens):
- vlm-shots-v98.sh — the REFERENCE side (login on the first attempt;
  the parked pointer at (5,5); read-only — the v46 rule).
- clone-vlmshots-v98.sh — the CLONE side (the with-server :3200 parity
  server).
- vlm-compare-v98.mjs — the VLM pairwise.
- arbit-v98.sh — the both-sides census (the v86/v92 axes re-measured;
  the census runs regardless of the verdict — the v75 convention).
- ref-arbit-v98.sh + clone-arbit-v98.sh — the TWO-HALF controlled form,
  BUILT two-half from the start via build-twohalf-v98.py (the
  SV_CENSUS_JS block [153 lines] extracted once and embedded
  byte-identically across the halves — the md5 line-block contract
  [31d181ed]). The reference half's first run hit the 300s tool
  timeout with buffered output (the census itself completed — the
  login/census/done markers all present in the partial output); the
  re-run with the output streamed completed clean. The reaping budget
  applied between every half.
- menu-arbit-v98.sh + menu-clone-v98.sh — the supplemental one-shot
  two-half census for the pin's own axes (the v87..v97 precedent),
  BUILT two-half from the start via build-menu-v98.py (the census JS
  md5 0f83b786 — 42 lines — byte-identical across the halves).
- pixel-diff-v98.py + inspect-diff-v98.py — the screenshot DATE-class
  arbitration (the v68/v92/v96 discipline, programmatic PIL diffs;
  never a VLM verdict for the acceptance).

The findings:
1. The verdict DIFFERENT, every flag DOM-arbitrated to the documented
   classes (the v57 DATA-CONDITIONAL footer [the census proving the
   footer childCount 1-vs-2 with the clone's "Brokerage" chip]; the
   seed-count grid [1 vs 2]; the seed-data figures/badges/subtexts;
   the user-identity avatar; no FAB flag this cycle — the platform
   iframe chrome absent from this verdict's flag set, same as v92).
2. The both-sides census (the two-half form) REPRODUCES the v86/v92
   census values EXACTLY — zero drift on every axis (the h1/grid/card/
   cardTitle/titleRow/cardAmount/footer/badge families; the docSW 1280
   guard; the clone template's last-column sub-pixel the documented
   column-distribution rounding noise). NO NEW CLONE GAP — the
   iteration PIN-ONLY.
3. The v98 pin (+1 e2e = 301): the goal-card ACTION-MENU PANEL +
   MENUITEM-RESTING interior census at 1280 (tests/e2e/items.spec.ts —
   the v97 missing-middle lesson applied to the ACTION layer: the
   tokens G5/G9 pins hold the menu ITEM's COLOR family [editRest
   rgb(10,10,10) / deleteColor rgb(220,38,38) / the focus-state bg] +
   the CONTENT's border-COLOR on the income view, the v35 S1 pin the
   keyboard contract — but the menu PANEL's GEOMETRY {bg/radius/shadow/
   min-w/overflow/z/w/h} and the menuitem's RESTING interior {fs/fw/
   pad/radius/lh/h} were NEVER pinned at ANY viewport in ANY spec — the
   coverage-map grep across all 24 specs; the panel {bg white, radius
   6px, border 1px rgb(229,229,229), minW 128px, overflow hidden, z 50,
   pos static, w 128, h 74} + the shadow-md VISIBLE layers via
   toContain [the v37 O1 v3/v4-construct precedent] + the item0
   {fs 14px, fw 400, color rgb(10,10,10), pad 6px 8px, radius 4px,
   lh 20px, h 32} + the itemCount 2 + the docSW 1280 guard — the panel
   w/h + itemCount DATA-INDEPENDENT [the structural Edit+Delete pair:
   2x32 + 2x4 pad + 2x1 border = 74], so unlike the v97 pin's
   clone-only guards these axes assert the cross-side-verified values
   directly) — the pin's own axes first measured byte-identical on
   both sides by the supplemental two-half census — GREEN on first
   run.
4. The pin-sanity mutation (the executed form — the DropdownMenuContent
   panel's rounded-md -> rounded-lg at src/components/ui/dropdown-menu.
   tsx:20, by LINE NUMBER; the line-scoping keeps the DropdownMenuItem's
   own rounded-sm at line 36 untouched): the failure diff reads as the
   panel radius axis alone ("6px" -> "8px"); the full items.spec.ts
   under the mutation reads ONLY the v98 pin red (42 green) —
   cascade-free BY CONSTRUCTION (no spec asserts any dropdown-menu
   panel radius — this pin is the first; the v97 listbox panel radius
   6px reads select.tsx's SelectContent, a DIFFERENT component; the
   tokens G5 contentBorder is the border-COLOR axis, not radius) —
   NOTE the mutation only bites after the standalone REBUILD (the e2e
   runs the PREBUILT standalone server; the first mutation run against
   the stale build read 43 green — the rebuild-then-test discipline);
   restored (git diff src/ = 0; the standalone REBUILD; the
   post-restore full run 43/43 green).
5. The full chain re-run GREEN: lint -> typecheck -> 108 unit -> build
   -> 301 e2e (136+96+71 = 303 chunk executions, zero flakes) ->
   35/35 smoke; the screenshots 10/16 BYTE-IDENTICAL + 6/16 the
   fresh-reseed DATE class (the fresh-clone re-seed re-anchoring the
   seed's isoDate offsets to the new seed day — db/ is gitignored, it
   does not travel; every differing region pixel-arbitrated by
   pixel-diff-v98.py: 03-income 2 date spans, 04-expenses 3,
   05-savings 2, 06-networth 1, 16-item-details 1 date span + two
   max-channel-2 sub-perceptual re-render regions, 08-calculator one
   77x77 max-channel-2 region — the v68 calculator precedent, below
   the ~2.5 JND; the VLM crop re-read over-read the sub-threshold
   noise as a "missing border" — the measurement is the authority, the
   v43 rule).

The operational lessons (the D6 section):
- THE REFERENCE POINTER-EVENT FAMILY (NEW): the reference's React tree
  opens its ellipsis dropdown only on the full pointer event SEQUENCE
  (pointerdown -> mousedown -> pointerup -> mouseup -> click); a bare
  synthetic el.click() opens the clone's Radix menu but NOT the
  reference's. Any future census that must OPEN reference-side
  interactive chrome dispatches the full sequence.
- THE UNLABELLED-TRIGGER FINDER CLASS (NEW): the reference's card
  action trigger carries NO aria-label (the clone's "Actions for ..."
  is the a11y superset — the v38 search-input aria-label note's
  sibling) — cross-side finders for action chrome must be GEOMETRIC
  (the textless 36x36 svg button), with the clone-only aria-label
  reserved for the e2e pin's locator.
- THE DATA-INDEPENDENT PANEL: the action menu's Edit+Delete pair is
  STRUCTURAL (both sides render exactly 2 items), so the panel w/h +
  itemCount are data-independent — these axes assert cross-side-
  verified values directly (unlike the v97 pin's clone-only h/optCount
  guards).
- THE MUTATION-REBUILD DISCIPLINE: a pin-sanity mutation only bites
  after the standalone REBUILD (the e2e runs the PREBUILT
  .next/standalone server) — a mutation run against the stale build
  reads green and proves nothing.

## v99 — the login + calculator pair's sixth re-run + the login social-row pin (2026-10-20)

The cycle (`docs/remediation-plan-v99.md` — the plan validated against
the codebase before execution; the narrative: `docs/session_239.md`):
the v98-era docs' v99 queue suggestion agreeing with the rotation
ledger (the TWENTY-SECOND consecutive agreement) — the v93-era LOGIN +
CALCULATOR pair (the LOGIN view + the CALCULATOR dialog at desktop
1280x800, last re-shot v93, now the oldest remaining
[v93 < v94 < v95 < v96 < v97 < v98]; the pair's SIXTH re-run
[v59 -> v66 -> v75 -> v81 -> v87 -> v93 -> v99], the surface names
verified against vlm-shots-v93.sh's own header before the derivation).

The baseline — the CARRIED-OVER workspace (the session-log-only commit
class: pulled to main @ 74a206e; the two commits since the v98 push
08cc3cf verified session-log-only [session_237 + session_238 — ZERO
src/ or lockfile deltas], the v98 fresh-clone environment carries over
unchanged): seedcheck exact; lint/typecheck/108 unit/build green
(robots + sitemap prerendered); 301 e2e in three chunks
(114+99+90 = 303 executions = 301 unique) with ONE first-run timing
flake (the not-found head-parity test at the 15-file chunk's tail —
clean on the single-spec re-run AND the full-chunk re-run, the
documented v96-era timing-artifact class); 35/35 smoke. The production
seams re-audited (auth, db-path, the SEO pair, the Tailwind v4
mitigations, the three test tiers; skills/ excluded).

The probe series (derive-v99-series.py, persisted — the generic swaps
then the exact-fragment history corrections; the ONE first-run MISS
[the clone-login header's "the re-run\n# cycle's" line break] caught by
the derive script's own hit/miss report and fixed before any probe
executed):
- vlm-shots-v99.sh + login-shots-v99.sh — the REFERENCE side (login on
  the first attempt; the parked pointer at (5,5); read-only).
- clone-vlmshots-v99.sh + clone-login-shots-v99.sh — the CLONE side
  (the "Contents Insurance" $25 line-item pairing through the real UI +
  the FULL restore: delete + confirm + restore $1850 + the
  "3 items · $2235.00" re-read; the first run hit a 300s tool timeout
  on a hung agent-browser call — the re-run discipline; the seedcheck
  exact after).
- vlm-compare-v99.mjs — the VLM pairwise (calculator DIFFERENT, login
  IDENTICAL).
- arbit-v99.sh — the both-sides census, executed as ref-arbit-v99.sh +
  clone-arbit-v99.sh (the TWO-HALF controlled form, BUILT two-half from
  the start via build-twohalf-v99.py — the CALC + LOGIN census JS
  blocks byte-identical across the halves, md5 e1092d12 / 9e5a52d2).
- closebtn-arbit-v99.sh — the one-shot REFERENCE close-button GEOMETRIC
  census (the arbitration for the census's own finder artifact — see
  the lessons).
- social-arbit-v99.sh + social-clone-v99.sh — the supplemental one-shot
  two-half census for the pin's own axes (build-social-v99.py, the
  census JS byte-identical, md5 d7add89b; both sides read-only passive
  navigation — the logged-out /login surface needs no session).

The verdicts: the CALCULATOR pair DIFFERENT — every flag
DOM-arbitrated to a documented class (the "Will update category total"
line the SEED-DATA class [hasWillUpdateSpan false-vs-true: the
reference's own Rent $25.00 EQUALS its calculated total; the clone's
Rent $1850 vs the recalculated $25.00 shows the note — the v73
DATA-CONDITIONAL class]; the reference-row-shows-hover-buttons flags
the RESTING-PARITY class [actionsAtRest opacity 0 / btnCount 2
byte-identical — the VLM caught the reference's row post-pointer, the
v43 rule applied]); the LOGIN pair IDENTICAL (zero flags). The
two-half census REPRODUCES the v87/v93 census values EXACTLY — zero
drift on every axis. NO NEW CLONE GAP — the v99 iteration PIN-ONLY.

The v99 pin (+1 e2e = 302): the login card's SOCIAL-LOGIN ROW census
at 1280 (tests/e2e/login-parity.spec.ts — the family-extension survey
applied to the LOGIN surface's social row: the v75 F4 pin walked
card/h1/subtitle/inputs/signIn/logo; the v7 G3 pin holds the Google
button's COLORS + the v45 F4 pin its HOVER shadow + the auth.spec pins
the OR divider's PRESENCE — the OR divider's computed chrome and the
Google button's geometry/typography were NEVER pinned at ANY viewport
in ANY spec, the coverage-map grep across all 24 specs). The pin's own
axes first measured byte-identical on both sides by the supplemental
two-half census: the Google button {w 368, h 54, radius 12px, fs 16px,
fw 500, lh 24px, color rgb(51,65,85), bg white, border 1px
rgb(226,232,240), pad 14px 20px, gap 12px, svg 20x20}; the "or" text
{fs 12px, fw 500, color rgb(100,116,139), lh 16px, uppercase, ls
0.6px, pad 0px 12px, bg white, h 16, w 43}; the single rule {1px,
rgb(226,232,240), w 368}; the googleToOr rhythm 32; docSW 1280. Every
axis DATA-INDEPENDENT (the static logged-out surface — the v98
data-independent-panel strength class). The pin-sanity mutation
(rounded-xl -> rounded-lg at login-card.tsx:172, by LINE NUMBER — the
line carries exactly one rounded-xl): ONLY the v99 pin red (29 green)
AFTER the standalone REBUILD (the v98 mutation-rebuild discipline — the
first run against the stale build read green and proved nothing), the
failure diff reads as the google radius axis alone ("12px" -> "8px") —
cascade-free BY CONSTRUCTION; restored (git diff src/ = 0; the REBUILD;
the post-restore full run 30/30 green).

The F5 full chain re-run GREEN: lint -> typecheck -> 108 unit ->
build -> 302 e2e (114+100+90 = 304 chunk executions = 302 unique
tests, zero flakes) -> 35/35 smoke; the screenshots **16/16
BYTE-IDENTICAL** (the same-day-seed byte-identity law — the
carried-over workspace's seed and the shots on one calendar day, no
fresh re-seed, no midnight crossing).

The operational lessons (the D6 section):
- THE UNLABELLED-TRIGGER FINDER CLASS, EXTENDED (the v98 lesson's
  second sighting): the two-half census's OWN close-button finder
  (aria-label/text) matched the clone's labelled Radix button but NOT
  the reference's TEXTLESS SVG button — the supplemental GEOMETRIC
  probe (closebtn-arbit-v99.sh: the header-band button census) is the
  arbitration form, reading the reference's close button byte-identical
  {36x36, radius 6px, bg transparent, border 0}. Any future census
  finder for reference-side chrome must be geometric or
  labelled-on-both-sides from the start.
- THE SOCIAL-BLOCK-ABOVE-THE-FORM ORDER (a measurement note): the
  reference's login card renders the Google + OR block ABOVE the
  email/password form (signInToGoogle -358 on BOTH sides) — the clone's
  GoogleBlock-before-AuthForm order (login-card.tsx:583-584) is the
  parity-correct one; the rhythm axes' sign is the tell.
- THE CENSUS-TAG CONSTRUCT CLASS (a pin-strength note): the OR rule
  renders as DIV on the reference and SPAN on the clone with
  byte-identical chrome — pins on such elements assert the COMPUTED
  chrome + the geometric count, never the tag name.

The v100 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the login + calculator pair (the v94-era NETWORTH + DRILL-DOWN
pair [the networth view + the dashboard drill-down EXPANDED state, both
desktop 1280x800 full-page], last re-shot v94 — now the oldest
remaining [v94 < v95 < v96 < v97 < v98 < v99]; the pair's SIXTH re-run
bracket [v60 -> v67 -> v76 -> v82 -> v88 -> v94 -> v100] to be verified
against vlm-shots-v94.sh's own header before the derivation), (2) the
axe-core watch at its next re-check point (only a 5.x wrapper changes
the calculus), (3) the deferred reference-write censuses (unchanged —
out of bounds under the v46 read-only rule).

## v100 — the networth + drill-down pair's sixth re-run + the tablist→section-row junction pin (2026-10-20)

The cycle (`docs/remediation-plan-v100.md` — the plan validated against
the codebase before execution; the narrative: `docs/session_242.md`):
the v99-era docs' v100 queue suggestion agreeing with the rotation
ledger (the TWENTY-THIRD consecutive agreement) — the v94-era NETWORTH
+ DRILL-DOWN pair (the NETWORTH view + the DASHBOARD's drill-down
EXPANDED state at desktop 1280x800, last re-shot v94, now the oldest
remaining [v94 < v95 < v96 < v97 < v98 < v99]; the pair's SIXTH re-run
[v60 -> v67 -> v76 -> v82 -> v88 -> v94 -> v100], the surface names
verified against vlm-shots-v94.sh's own header before the derivation —
the queue-prose verification lesson applied).

The baseline — the FRESH-CLONE workspace (the sandbox reset — the
v86/v88/v90/v91/v92/v98 precedent): git clone at main @ fd06b78; npm
install; `.env` written (DATABASE_URL="file:../db/custom.db"); db/
re-seeded (the seedcheck exact); chromium-1243 installed for the pinned
@playwright/test 1.63.0 (the cache's 1200 build belongs to a different
playwright generation); the tool-results dir re-created for
with-server.sh; the two commits since the v99 push 4b0b6aa (b43db6f +
fd06b78) audited session-log-only (session_240 + session_241 — ZERO
src/ or lockfile deltas). Seedcheck exact; lint/typecheck/108
unit/build green (robots + sitemap prerendered); 302 e2e (108+116+83 =
307 chunk executions = 302 unique, zero flakes on the FIRST run);
35/35 smoke. The production seams re-audited (auth, db-path, the SEO
pair, the Tailwind v4 mitigations, the three test tiers; skills/
excluded).

The probe series (derive-v100-series.py, persisted — the generic swaps
then the exact-fragment history corrections [last-re-shot v88 → v94,
FIFTH → SIXTH, the re-run bracket extension, the oldest-remaining
bracket, the agreement ordinal SEVENTEENTH → TWENTY-THIRD, the
census-axes reference v88 → v94]; every correction verified applied by
the derive script's own hit/miss report — zero misses this cycle;
bash -n + node --check clean on all four; zero residual old tokens,
the legitimate v60/v67/v75/v82 pin-provenance tokens whitelisted by
context):
- vlm-shots-v100.sh + clone-vlmshots-v100.sh — the reference + clone
  FULL-PAGE shots (login on the first attempt both sides; the parked
  pointer at (5,5); read-only — the v46 rule holds).
- vlm-compare-v100.mjs — the VLM pairwise (networth IDENTICAL,
  drill-down DIFFERENT).
- ref-arbit-v100.sh + clone-arbit-v100.sh — the both-sides census,
  BUILT two-half from the start via build-twohalf-v100.py (the TWO
  census JS blocks [ARBIT_A 90 lines + ARBIT_B 111 lines]
  byte-identical across the halves, md5 50e0cbf2 / cb3afbfc).
- derive-standing-v100.py — the 94th standing-checks derivation
  (ref-standing-v94.sh + standing-checks-v94.sh from the v93 pair
  across the THREE token families, version-bump-only verified by the
  normalize-back diff).
- nwjunction-arbit-v100.sh + nwjunction-clone-v100.sh — the
  supplemental two-half census for the pin's own axes
  (build-nwjunction-v100.py, the census JS byte-identical, md5
  5f124436; both sides read-only passive navigation).

The verdicts: the NETWORTH pair IDENTICAL — zero layout/style flags
(only the expected data classes + the platform-chrome FAB); the
DRILL-DOWN pair DIFFERENT (the documented re-run class) — every flag
DOM-arbitrated to a documented class: the nav-highlight the v56
SUPERSET class (the reference's root-route bug marks NO nav item
active at /; the census: INERT rgb(63,63,70)/fw 400 on the reference
vs ACTIVE rgb(255,255,255)/fw 500 on the clone — the deliberate
superset delta, NOT a drift); the avatar U-vs-D the user-identity
class (the VLM's "P" misread of the clone's "D" the v43 perception
rule); the Edit-with-Base44 FAB the platform-chrome class (fabCount 0
+ bodyHasBase44 false on BOTH sides — the FAB never renders in the app
DOM); the donut-labels the v60 perception class (the census proving
the reference's own labels ARE in its DOM: count 4, texts
["92.3%4.6%3.1%", "92.3%", "4.6%", "3.1%"], labelLineCount 0, labelFs
16px, labelFill rgb(0,0,0), sectors 3 — the chrome byte-identical to
the clone's; the reference's own seed data renders its three labels
OVERLAPPING and illegible to the VLM, the clone's well-separated); the
slice proportions the seed-data class. The two-half census REPRODUCES
the v88/v94 census values EXACTLY — zero drift on every axis. NO NEW
CLONE GAP — the v100 iteration PIN-ONLY.

The v100 pin (+1 e2e = 303): the networth TABLIST→SECTION-ROW junction
census at 1280 (tests/e2e/networth.spec.ts — the FAMILY-EXTENSION
pattern, the v94 missing-middle lesson applied to the networth view's
INTER-BLOCK RHYTHM: the v41 F2 pin [640] walks the UPPER rhythm only,
the v60 F1 pin [1280] the summary card + tablist interiors, the v94 F4
pin the section row's own chrome + the row-to-group rhythm — the
JUNCTION between them [the tablist bottom → the section row top gap,
the TabsContent's mt-6] NEVER pinned at ANY viewport in ANY spec, the
coverage-map grep across all 24 specs). The pin's own axes first
measured byte-identical on both sides by the supplemental two-half
census: the tablist {w 448, h 36, bottom 525, template "220px 220px",
maxW "448px", pad "4px"}; the section row {top 549, h 56, w 960,
display flex, justify space-between}; the junction {gap 24}; the
continuation {groupH3 fs 18px/fw 600/mb 12px; rowToGroup 24}; docSW
1280. Every axis DATA-INDEPENDENT (the structural chrome — the v98
data-independent-panel strength class). The pin-sanity mutation (mt-6
-> mt-8 at net-worth-view.tsx:415, by LINE NUMBER — the line carries
EXACTLY ONE mt-6; the line-scoping keeps the liabilities TabsContent's
own mt-6 at line 479 untouched): ONLY the v100 pin red (31 green)
AFTER the standalone REBUILD (the v98 mutation-rebuild discipline),
the failure diff reads as the junction position family alone
(sectionRow.top 549 -> 557 — the direct y-consequence of the 24 -> 32
gap; no width/height/chrome axis touched) — cascade-free BY
CONSTRUCTION; restored (git diff src/ = 0; the REBUILD; the
post-restore full file run 32/32 green).

The ship full chain re-run GREEN: lint -> typecheck -> 108 unit ->
build -> 303 e2e (105+105+95 = 305 chunk executions = 303 unique
tests — 302 spec tests + the setup test re-run per chunk, three
disjoint file splits; zero flakes) -> 35/35 smoke; the screenshots
**16/16 BYTE-IDENTICAL** (the same-day-seed byte-identity law — the
fresh-clone workspace's same-day re-seed and the shots on one calendar
day, no midnight crossing).

The operational lessons (the D6 section):
- THE REAPING BUDGET AS THE STANDING STEP (the v89/v91 symptom class,
  re-confirmed): the clone census half's FIRST run read EMPTY output —
  65 stale chromium processes from the reference half's sessions;
  after the reap the identical script ran clean. The two-half form is
  necessary but not sufficient — the reaping BETWEEN halves is
  load-bearing on this sandbox.
- THE CLEAN-PARENTHETICAL DERIVATION (a derivation-quality note): the
  v94-era headers' "the v89-era pair covered by v90" parenthetical
  carried an internally-confused rotation framing (decoded via the
  v83/v88/v89 headers: "the vN-era pair covered by vM" = the pair
  re-shot at vM); the v100 headers use the clean form ("the v94-era
  pair last re-shot v94 — now the oldest remaining [v94 < v95 < …]") —
  future derivations should carry the clean form forward.
- THE JUNCTION-COMPLETE RHYTHM MAP (a coverage-map note): the networth
  view's inter-block rhythm is now FULLY pinned — headerToCard 32 +
  cardToTablist 32 (v41 F2, 640) + tablistToSection 24 (the v100 pin,
  1280) + rowToGroup 24 + groupToGrid 12 (v94 F4, 1280) — the
  family-extension survey should walk the JUNCTIONS between pinned
  blocks, not just the blocks' interiors.

The v101 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the networth + drill-down pair (the v95-era DASHBOARD pair [the
dashboard view + …, both desktop 1280x800 full-page], last re-shot v95 —
now the oldest remaining [v95 < v96 < v97 < v98 < v99 < v100]; the
pair's SIXTH re-run bracket to be verified against vlm-shots-v95.sh's
own header before the derivation), (2) the axe-core watch at its next
re-check point (only a 5.x wrapper changes the calculus), (3) the
deferred reference-write censuses (unchanged — out of bounds under the
v46 read-only rule).
## The v101 cycle (executed 2026-10-20 — the v95-era dashboard pair's sixth re-run)

The queue's own paragraph above was EXECUTED this cycle. The rotation
ledger verified FIRST (the queue-prose verification lesson): the
vlm-shots-v95.sh header read "the DASHBOARD at desktop 1280x800,
FULL-PAGE, last re-shot v89 — now the oldest remaining [v89 < v90 < v91
< v92 < v93 < v94]; the pair's FIFTH re-run [v61 → v68 → v77 → v83 →
v89 → v95]" — the SIXTH re-run bracket [v61 → v68 → v77 → v83 → v89 →
v95 → v101] constructed from it, the TWENTY-FOURTH consecutive
queue/ledger agreement. The two commits since the v100 push (1a5c5bb +
840e25c) audited session-log-only (session_243.md + session_244.md —
zero src/ or lockfile deltas).

The probe series derived from the v95 lineage by the persisted
derive-v101-series.py (the generic swaps [refvlm95→refvlm101,
clonevlm95→clonevlm101, refar95→refar101, clonear95→clonear101,
/tmp/vlm95→/tmp/vlm101, v95→v101] then the exact-fragment history
corrections [last-re-shot v89→v95, FIFTH→SIXTH, the bracket extension,
the oldest-remaining bracket v95<v96<v97<v98<v99<v100, the agreement
ordinal EIGHTEENTH→TWENTY-FOURTH, the previous-verdict reference
v89→v95, "after v89-v94"→"after v95-v100", the census-axes drift-check
baseline→v95] — every correction's hit/miss REPORTED by the script
itself, ZERO misses; the line-count-preservation check green on all
four files so build-twohalf-v101.py inherits the v95 line boundaries;
bash -n + node --check clean; the residual check clean with the
era-asymmetric whitelist). The new probes this cycle: vlm-shots-v101.sh
+ clone-vlmshots-v101.sh + vlm-compare-v101.mjs + arbit-v101.sh (the
intermediate combined form, header-corrected) + build-twohalf-v101.py
(the two-half builder — the THREE census blocks [ARBIT_G/ARBIT_Q/
ARBIT_X] extracted once, embedded byte-identically across the halves by
the md5 line-block contract [b500dd29 / da04e995 / 7a381755 — the v95
census blocks verbatim]) + ref-arbit-v101.sh + clone-arbit-v101.sh +
build-spending-v101.py + spending-arbit-v101.sh +
spending-clone-v101.sh (the supplemental two-half census for the v101
pin's own axes, BUILT two-half from the start — the census JS
byte-identical by the md5 line-block contract [7e6a13c3 — 48 lines]) +
derive-standing-v101.py + ref-standing-v95.sh + standing-checks-v95.sh
(the 95th standing checks, version-bumped from the v94 pair across the
three token families). The reaping budget applied as the standing step
between every half; login on the first attempt both sides; the parked
pointer at (5,5); read-only — the v46 rule holds.

The verdict: IDENTICAL — ZERO style flags on the pair's own target
surfaces (the Budget Guidelines card and the Quick Action cards both
"visually identical" per the VLM's own targeted analysis) — the FOURTH
consecutive IDENTICAL verdict for this pair [v83 → v89 → v95 → v101].
The only flags the documented standing classes: the seed-data figures
(the allocation bar 30.5%-vs-62.8%, the balance $3475-vs-$2065, the
stat figures, the donut proportions), the root-URL active-nav highlight
(the v56 SUPERSET class), and the avatar "U" vs "D" (the user-identity
class).

The both-sides census — executed in the TWO-HALF controlled form BUILT
two-half from the start — REPRODUCED the v89/v95 census values EXACTLY
(zero drift on every axis): PART G the guidelines card 468x348/radius
12px/border/bg/the header pad 24px/fs 16px/fw 600/rgb(26,58,46)/lh
16px/tracking -0.4px/the body pad 0px 24px 24px/the three tiles 418x78
with the Needs/Wants/Savings tints and the label/pct/desc chrome — the
only delta the shadow's transparent lead-layer count (the v66
computed-form INVISIBLE class); PART Q the grid 304px x3/gap 24px/w
960/the three cards 304x90/radius 16px/pad 24px/white/border/the
40x40 tinted tiles/the 20px icons/the labels/the 0.5-opacity pluses/
transition 0.2s — the TWO census deltas both documented classes (the
grid mt [ref 0px vs clone 32px — the rendered gap IDENTICAL at 340, the
v77 mechanism class] and the label finder's wrapper catch [ref leaf
500/rgb(26,58,46) vs clone wrapper 400/rgb(10,10,10) — the v61 label
lesson: the clone's LEAF span carries the identical chrome, pinned
green by the v61 F3 pin]); PART X cardBottom 1122/gridTop 1462/gap 340
on BOTH sides, byte-identical. NO NEW CLONE GAP — the v101 iteration
PIN-ONLY.

The v101 pin (+1 e2e = 304): the spending+guidelines 2-COL ROW's grid
+ the Spending Breakdown card's own box/header census at 1280
(tests/e2e/dashboard.spec.ts — the FAMILY-EXTENSION pattern, the v100
junction-walk lesson applied to the 2-col row: the v61 F2 pin walks the
row ONLY for rowH 656 [the stretch contract] + the guidelines card's
own box, the v77 pin the guidelines card's interior text, the v83 F4 pin
the card-level cross-row gap — the ROW'S OWN GRID CHROME [the
"468px 468px" template, the 24px column gap, the 960 width, the two
children's 468 widths] and the SPENDING CARD'S OWN BOX + HEADER [the
card radius/border/bg/shadow, the title's typography, the subtitle's
chrome, the title→subtitle rhythm, the body's pt-0 contract] NEVER
pinned at ANY viewport in ANY spec — the coverage-map grep across all
24 specs: zero "468px 468px" template matches, zero spending-card
radius/border/shadow assertions, the subtitle only visibility-asserted,
the only columnGap census the v61 F3 quick-action grid's own). The
pin's own axes first measured byte-identical on BOTH sides by the
supplemental two-half census (spending-arbit-v101.sh +
spending-clone-v101.sh via build-spending-v101.py, the census JS
byte-identical by the md5 line-block contract [7e6a13c3]; both sides
READ-ONLY login + passive navigation — the v46 rule holds; the
seedcheck exact after the clone half): the row {display grid, template
"468px 468px", colGap 24px, w 960}; the two children [{w 468, block},
{w 468, block}]; the card {w 468, radius 12px, border
rgb(229,231,227), bg white + the visible shadow pair — the lead-layer
count the v66 INVISIBLE class}; the header {pad 24px} + the title
{fs 16px, fw 600, color rgb(26,58,46), lh 16px, tracking -0.4px} + the
subtitle {text "Needs vs Wants vs Savings", fs 14px, fw 400, color
rgb(107,114,128), lh 20px, top 6 — the space-y-1.5 rhythm}; the body
{pad "0px 24px 24px" — the pt-0 contract}; the docSW 1280 guard. Every
axis DATA-INDEPENDENT (the structural chrome + the fixed header texts;
the data-locked heights stay with the v61 F2 pin's own rowH contract)
— the v98 data-independent-panel strength class. The pin-sanity
mutation (the SpendingBreakdownCard's rounded-xl → rounded-2xl at
src/components/budget/dashboard-view.tsx:695, by LINE NUMBER — the line
carries EXACTLY ONE rounded-xl; the line-scoping keeps the
BudgetGuidelinesCard's own rounded-xl at line 832 untouched): ONLY the
v101 pin red (42 green) AFTER the standalone REBUILD (the v98
mutation-rebuild discipline), the failure diff reads as the card radius
axis ALONE ("12px" → "16px") — cascade-free BY CONSTRUCTION
(border-radius never changes the layout box — the v99 precedent), then
restored (git diff src/ = 0; the REBUILD; the post-restore full file
run 43/43 green).

The ship full chain re-run GREEN: lint -> typecheck -> 108 unit ->
build -> 304 e2e (116+92+98 = 306 chunk executions = 304 unique tests
— 303 spec tests + the setup test re-run per chunk, three disjoint
file splits; zero flakes) -> 35/35 smoke; the screenshots **16/16
BYTE-IDENTICAL** (the same-day-seed byte-identity law — the
fresh-clone workspace's same-day re-seed and the shots on one calendar
day, no midnight crossing).

The operational lessons (the D6 section):
- THE RESIDUAL-CHECK ASYMMETRY (a derivation-quality note): the v101
  residual whitelist must tolerate the NEW-era v95 tokens the history
  corrections introduce ("the v95-era" / "re-shot v95" / "since v95" /
  "after v95-v100") while still flagging the OLD v89-era/FIFTH/
  EIGHTEENTH tokens — the whitelist is era-asymmetric by construction
  and must be re-derived per cycle, never copied blindly from the
  previous cycle's script.
- THE CUMULATIVE-PIN COUPLING (a mutation-selection note): the
  dashboard's cumulative y-position pins (the v83 F4 cardBottom 1122 /
  gridTop 1462; the v56 F1 hero children y 136) make ANY inter-row
  margin mutation NON-cascade-free — the mutation-selection for
  dashboard-surface pins must target box-chrome axes (radius/border/
  typography), never the inter-row rhythm, unless the cumulative pins
  are re-baselined in the same change.
- THE LEFT-COLUMN COMPLETION (a coverage-map note): the 2-col row's
  coverage is now COMPLETE — the row's own grid chrome + BOTH columns'
  cards (the guidelines card by v61 F2/v77, the spending card by the
  v101 pin) + the cross-row junction by v83 F4 — the family-extension
  survey on a two-column row must walk BOTH columns' boxes, not just
  the arbitrarily-chosen first.

The v102 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the dashboard pair (the v96-era MOBILE 390 twins pair [the five
views' mobile surfaces at 390x844], last re-shot v96 — now the oldest
remaining [v96 < v97 < v98 < v99 < v100 < v101]; the pair's SIXTH
re-run bracket to be verified against vlm-shots-v96.sh's own header
before the derivation), (2) the axe-core watch at its next re-check
point (only a 5.x wrapper changes the calculus), (3) the deferred
reference-write censuses (unchanged — out of bounds under the v46
read-only rule).

## The v102 cycle (executed 2026-10-21 — the v96-era mobile 390 twins' sixth re-run)

The queue's own paragraph above was EXECUTED this cycle. The probe series
derived from the v96 lineage by derive-v102-series.py (the PERSISTED
derivation script — the generic swaps [refvlm96->refvlm102,
clonevlm96->clonevlm102, refarbit96->refarbit102, clonearbit96->
clonearbit102, /tmp/vlm96->/tmp/vlm102, v96->v102] followed by the
exact-fragment history corrections [the queue source "the v95 plan's own
suggestion"->"the v101 plan's own suggestion", the last-re-shot version
v90->v96, FIFTH->SIXTH, the re-run bracket extension + the
oldest-remaining bracket v96 < v97 < v98 < v99 < v100 < v101, the re-runs'
verdict note v84/v90->v84/v90/v96, the census-axes provenance "The v90
census axes"->"The v96 census axes"], every correction verified applied —
zero misses this cycle; zero residual old tokens across all four files;
bash -n + node --check clean; the line-count-preservation check green on
all four — the two-half builder inherits the v96 line boundaries). The
new probes this cycle: vlm-shots-v102.sh + clone-vlmshots-v102.sh +
vlm-compare-v102.mjs + arbit-v102.sh (the intermediate combined form,
header-corrected) + build-twohalf-v102.py (the two-half builder — the TWO
census blocks [NW_CENSUS 42 lines / DASH_CENSUS 87 lines] extracted once,
embedded byte-identically across the halves by the md5 line-block
contract [82cf8a43 / 85e4ec7e]) + ref-arbit-v102.sh + clone-arbit-v102.sh
+ derive-standing-v102.py (the persisted standing derivation — the 96th
pair, version-bump-only verified by the normalize-back diff) +
ref-standing-v96.sh + standing-checks-v96.sh + headgap-arbit-v102.sh (the
NEW top-header-spacing flag's one-shot arbitration — the topbar/h1/gap
census on BOTH sides) + build-mobjunction-v102.py + mobjunction-arbit-
v102.sh + mobjunction-clone-v102.sh (the supplemental two-half census for
the v102 pin's own axes — the census JS byte-identical by the md5
line-block contract [83a04c0e]; the doubled-brace spot check clean).

The verdicts: BOTH DIFFERENT (the pair's documented verdict class — the
same flag-set classes as the v84/v90/v96 re-runs) with every flag
DOM-arbitrated: the stat-tile side-by-side-vs-stacked the v41
mobile-superset class (the census: statGrid cols ref "175.828px
175.844px" 2-col vs clone "294px" 1-col, the gap 16px IDENTICAL, the
tiles ref 176x84 vs clone 294x84 — the h 84 byte-identical); the subtitle
"third line" + the top-header-spacing flags BOTH VLM MISREADS (the
census: the clone's subtitle P h 48 = exactly 2 DOM lines, the
Range-walk buckets at tops 123/147, the chrome byte-identical; the
headgap one-shot census: topbar {h 28, bottom 44, static} + h1 {h 36,
top 77, fs 30px, fw 700, lh 36px} + gapTopbarToH1 33 + gapH1ToCard 56 —
BYTE-IDENTICAL across sides, the flags artifacts of comparing the
reference's 464-wide full-page image against the clone's 390-wide); the
wrap-point delta itself the v62 width-delta class; the tab-bar alignment
the v47/v53 divergence class (the reference's own 432-wide list inside
its 464-overflow page; the clone's 358-wide in-bounds list with the
identical "175px 175px" grid — pinned green by the v53 F1 pin); the
figure + trend-icon flags the seed-data classes (the v82
DATA-CONDITIONAL width class + the trend direction; the medallion 64x64
+ trendIcon 32x32 byte-identical per the census); the "Edit with Base44"
FAB the platform-chrome class; the progress-bar + donut flags the
seed-data classes. The two-half census REPRODUCES the v96 values EXACTLY
— zero drift on every axis (the networth card/statGrid/tiles/medallion/
trendIcon families with docSW ref 464 / clone 390; the dashboard subtitle
chrome + the 2-DOM-lines bucketing + the breakdown card's h 324/svgCount
7/the 16-14 alternation + the spendingCard finder's same div-heading
fallback string on BOTH sides). NO NEW CLONE GAP.

The standing-script timing artifact: NONE this cycle (the census clean
on the FIRST read, no render-race — the v96-era settle discipline holds).

The DATE-class screenshot arbitration (the v96 form, re-confirmed): the
cycle crosses the calendar-day boundary against the committed set (the
v101-era shots Oct 20 UTC; the regeneration Oct 21 00:1x UTC) — the Add
Item form's default date (budget-item-dialog.tsx:83, todayIso(), computed
at RENDER time) rolls "2026-10-20" -> "2026-10-21" and the
07-add-item-modal shot differs by exactly the two day digits: the
pixel-diff localization (the inline PIL diff this cycle, the v96
pixel-diff-v96.py form) localizes the delta to a 15x22px region at
x=1552 (the v75 acceptance form: width <= 48, height <= 40, x > 1000 —
the date field in the dialog's form column at the 2x DPR shot); the
other 15 shots byte-identical; the committed set updated with the new
07 shot (the date-class delta documented, never a regression).

The v102 pin (tests/e2e/networth.spec.ts, +1 -> 305): the networth
MOBILE junctions census at 390 — the card->tablist gap 32 (the summary
card's mb-8) + the assets tablist->section gap 24 (the assets
TabsContent's mt-6, re-anchored at the mobile viewport) + the LIABILITIES
panel's OWN junction 24 (its own mt-6 — never pinned at ANY viewport in
ANY spec; the coverage-map grep: the only cardToTablist assertion the
v41 F2 pin's own at 640, the only tablist-to-section junction assertion
the v100 pin's own at 1280 on the ASSETS tab) + the tablist {h 36, pad
4px} + both section rows {h 56, flex, space-between} anchors + the
docSW 390 guard — measured byte-identical on both sides first (the
mobjunction two-half census, md5 83a04c0e); the mutation mt-6 -> mt-8 at
net-worth-view.tsx:479 (line-scoped — the assets mt-6 at line 415 AND
the ratio footer's at line 385 untouched) verified single-axis (ONLY the
v102 pin red, 32 green, after the standalone REBUILD; the liabilities
junction axis alone [24 -> 32]).

The operational lessons (the D6 section):
- THE REFERENCE TAB-SWITCH INTERACTION CLASS (a census-finder note): the
  reference's Radix-style TabsTrigger ignores a bare DOM `.click()` —
  the aria-selected state never flips and the panel never swaps (the
  first liabilities-pass attempt read "no liabilities h2 after click"
  for exactly this reason); the FULL pointer-event sequence
  (pointerdown + mousedown + pointerup + mouseup + click) is
  load-bearing on the reference side (the clone responds to both).
  Future censuses that switch tabs on the reference must dispatch the
  full sequence — or use the Playwright locator click in the pin itself
  (which dispatches the full family natively).
- THE FORK-RETRY EXHAUSTION RE-CONFIRMED (a reaping-budget note): the
  clone census half's first run this cycle hit `bash: fork: retry:
  Resource temporarily unavailable` and read EMPTY output even after a
  routine pkill — the THOROUGH reaping (pkill -9 on chromium AND chrome
  AND agent-browser AND the standalone server + a 5s settle) was needed
  before the clean retry; the two-half form remains necessary but not
  sufficient — the reaping must be thorough between halves on this
  sandbox.
- THE SECOND-PANEL COVERAGE RULE (a coverage-map note): a tabbed view's
  junction coverage is complete only when BOTH panels' junctions are
  pinned — the assets panel's junction (the v100 pin at 1280) and the
  liabilities panel's own (the v102 pin at 390); the family-extension
  survey on a tabbed surface must walk EVERY panel's junction, not just
  the default tab's (the same both-columns lesson as the v101 2-col
  row).

The v103 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the mobile twins (the v97-era ITEMS pair [the INCOME + EXPENSES
view pair at desktop 1280x800], last re-shot v97 — now the oldest
remaining [v97 < v98 < v99 < v100 < v101 < v102]; the pair's SEVENTH
re-run bracket [v57 -> v64 -> v70 -> v79 -> v85 -> v91 -> v97 -> v103]
to be verified against vlm-shots-v97.sh's own header before the
derivation), (2) the axe-core watch at its next re-check point (only a
5.x wrapper changes the calculus), (3) the deferred reference-write
censuses (unchanged — out of bounds under the v46 read-only rule).

## The v103 cycle (executed 2026-10-21 — the v97-era items pair's seventh re-run)

The queue's own paragraph above was EXECUTED this cycle. The probe series
derived from the v97 lineage by derive-v103-series.py (the PERSISTED
derivation script — the generic swaps [refvlm97->refvlm103,
clonevlm97->clonevlm103, refarbit97->refarbit103, clonearbit97->
clonearbit103, /tmp/vlm97->/tmp/vlm103, v97->v103] followed by the
exact-fragment history corrections [the last-re-shot version v91->v97,
SIXTH->SEVENTH, the re-run bracket extension + the other-pairs list
bumped to the current era {savings v98, login+calculator v99,
networth+drill-down v100, dashboard v101, mobile twins v102}], every
correction verified applied — zero misses this cycle; zero residual old
tokens across all four files; bash -n + node --check clean; the
line-count-preservation check green on all four — the two-half builder
inherits the v97 line boundaries). The new probes this cycle:
vlm-shots-v103.sh + clone-vlmshots-v103.sh + vlm-compare-v103.mjs +
arbit-v103.sh (the intermediate combined form, header-corrected) +
build-twohalf-v103.py (the two-half builder — the ONE census block
[CENSUS_JS 193 lines] extracted once, embedded byte-identically across
the halves by the md5 line-block contract [b55dcd29]; the
doubled-brace spot check clean) + ref-arbit-v103.sh + clone-arbit-
v103.sh + derive-standing-v103.py (the persisted standing derivation —
the 97th pair, version-bump-only verified by the normalize-back diff) +
ref-standing-v97.sh + standing-checks-v97.sh + base44-fab-arbit-v103.sh
(the FAB one-shot re-arbitration, derived from the v97 twin) +
userfooter-arbit-v103.sh (the v103 pin's own one-shot both-sides census
— the base44-fab one-shot pattern applied to the rail's bottom family)
+ diff-shots-v103.mjs + diff-shots-v103-bands.mjs (the fresh-seed
DATE-class screenshot arbitration — the bbox + the row-band
decomposition; NOTE the pngjs dependency loaded via createRequire from
the /tmp/pngtools scratch install, NOT a repo dependency — PIN-ONLY
preserved).

The verdicts: BOTH DIFFERENT (the pair's documented verdict class — the
same flag-set classes as the v91/v97 re-runs) with every flag
DOM-arbitrated: the avatar U-vs-D the user-identity class (the chrome
byte-identical: 36x36 / 9999px / 14px / 600 / white / rgb(143,188,63));
the "Edit with Base44" FAB the platform-chrome class with the INVERTED
attribution form on PAIR 1 (the VLM attributed the FAB to the CLONE /
image 2 — the v85/v91-documented class; re-arbitrated live by
base44-fab-arbit-v103.sh: fabCount 0 + bodyHasBase44 false on BOTH
sides, the FAB lives in the reference's platform iframe chrome outside
the queryable body DOM) and the NON-inverted form on PAIR 2 (attributed
to the reference — the v97 form) IN THE SAME COMPARISON RUN — both
forms documented, both arbitrate identically, neither surprising; the
payment-method footer chips the v57 DATA-CONDITIONAL class (the census:
the reference's own income card's footer childCount 2 with the "Bank
Account" chip + icon — it RENDERS chips when data carries them; its
expense items ship none, childCount 1 — while the clone's carry them);
the header stats + the card grids (the reference's 3+1 two-row vs the
clone's 3 one-row — the seed-count class) + the card contents the
seed-data classes; the "Recurring" 4th badge the DATA-CONDITIONAL class.
The two-half census REPRODUCES the v97 values EXACTLY — zero drift on
every axis (the avatar chrome; the grid/card chrome [960/16px/309.328
family; card 309/pad 20/radius 12/border rgb(229,231,227); card h
200-vs-230 the v70b-decomposed class; the income template's last-column
sub-pixel the rounding-noise class]; the titleRow/amount/footer/badge
chrome [the expenses footer childCount the v57 class; the badgeRow h
22-vs-52 the v57 wrap class]; the filter-card both variants [the
v64/v70 contract: the income 447-spanning/3-child/2-combobox form + the
expenses 216/4-child/3-combobox form]; the docSW 1280 guard). NO NEW
CLONE GAP.

The standing-script timing artifact: NONE this cycle (the census clean
on the FIRST read, no render-race).

The DATE-class screenshot arbitration (the fresh-seed form, the
v86/v80/v92 precedent): the FRESH-CLONE workspace re-seeded the db on
Oct 21 while the committed set carried the carried-over-era dates —
every isoDate offset rolled +1 day, so SIX shots differ (03-income,
04-expenses, 05-savings, 06-networth, 08-calculator, 16-item-details —
exactly the v92 fresh-clone cycle's own file list, the same mechanism).
The pixel-band arbitration (diff-shots-v103.mjs + diff-shots-v103-
bands.mjs): every delta decomposes into TEXT-ROW bands (h 19 glyph rows
at 2x DPR — the card date footers; the 06 shot a single 13x19 glyph;
the 08 shot the calculator's date-field region; the 16 shot the sheet's
fact-row block + one 24px row) — ZERO structural bands (no full-width
bands, no container-boundary diffs, no layout shift); the 306-e2e chain
green in the same cycle independently confirms no layout regression;
the committed set updated with the regenerated shots (the date-class
deltas documented, never regressions).

The v103 pin (tests/e2e/nav-geometry.spec.ts, +1 -> 306): the rail's
bottom USER-FOOTER tile census at 1280 — the border-t wrapper
{borderTop 1px rgb(229,231,227), pad 16px, gap 8px} + the tinted tile
{223x60, radius 8px, pad 12px, bg rgb(245,248,245), flex center gap
12px} + the avatar w 36 control + the name {"Budget Pro" 14px/500/
rgb(26,58,46) ellipsis} + the subtitle {"Track your finances" 12px/400/
rgb(45,90,74) ellipsis} — the FAMILY-EXTENSION survey found the family
never census'd at ANY viewport (the v79 F4 pin covers the avatar INSIDE
the tile; the mobile sheet asserts only the texts' visibility; the
coverage-map grep across all 23 spec files: zero tile-chrome assertions)
— measured byte-identical on both sides first (the one-shot census
userfooter-arbit-v103.sh); the mutation rounded-lg -> rounded-xl at
sidebar.tsx:116 (line-scoped — the nav links' own rounded-lg at line 79
+ the mobile burger's own at line 227 untouched) verified single-axis
(ONLY the v103 pin red, 8 green, after the standalone REBUILD; the tile
radius axis alone ["8px" -> "12px"]).

The operational lessons (the D6 section):
- THE CHUNK-SPLIT SELF-AUDIT (a baseline-chain note): the Playwright
  file-filter argument is a PATH REGEX — "items.spec.ts" does NOT match
  "item-details.spec.ts" (nor does "networth.spec.ts" match
  "networth-error.spec.ts"); a chunk split copied from prose can
  silently drop a spec file from the baseline run. Derive the per-chunk
  file lists from `ls tests/e2e/*.spec.ts` explicitly and SUM the
  per-file `playwright test --list` counts against the authoritative
  total before declaring the chain green — the v103 four-chunk form
  (117+96+85+10 = 308 = 305 unique) is the auditable split.
- THE ONE-SHOT CENSUS FORM FOR SMALL FAMILIES (a probe-form note): the
  user-footer arbitration ran as a single both-sides script (the
  base44-fab pattern) rather than the two-half split — legitimate for
  SMALL censuses (one element family, one eval per side) where the
  chromium-exhaustion budget is not in play; the two-half form remains
  the default for the multi-view census series (the v92..v95 lesson).
- THE INVERTED-FAB ATTRIBUTION IS A STANDING CLASS (a VLM-arbitration
  note): the v103 PAIR 1 attributed the "Edit with Base44" FAB to the
  CLONE (image 2) while PAIR 2 attributed it to the reference — in the
  SAME comparison run; both forms are documented (v85/v91 inverted, v97
  non-inverted) and both arbitrate identically (fabCount 0 +
  bodyHasBase44 false on BOTH sides). Future cycles expect EITHER form
  without surprise; the one-shot census is the answer in both cases.

The v104 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the items pair (the v98-era SAVINGS pair, last re-shot v98 — now
the oldest remaining [v98 < v99 < v100 < v101 < v102 < v103]; the pair's
re-run bracket to be verified against vlm-shots-v98.sh's own header
before the derivation), (2) the axe-core watch at its next re-check
point (only a 5.x wrapper changes the calculus), (3) the deferred
reference-write censuses (unchanged — out of bounds under the v46
read-only rule).

## The v104 cycle (executed 2026-10-21 — the v98-era savings pair's seventh re-run)

The queue's own paragraph above was EXECUTED this cycle. The probe series
derived from the v98 lineage by derive-v104-series.py (the PERSISTED
derivation script — the generic swaps [refvlm98->refvlm104,
clonevlm98->clonevlm104, refarbit98->refarbit104, clonearbit98->
clonearbit104, /tmp/vlm98->/tmp/vlm104, v98->v104] followed by the
exact-fragment history corrections [the last-re-shot version v92->v98,
the era marker v92-era->v98-era, SIXTH->SEVENTH, the re-run bracket
extension v58->...->v92->v98->v104, the oldest-remaining list bumped to
the current era {v98 < v99 < v100 < v101 < v102 < v103}, the plan
attribution v97->v103, the agreement count TWENTY-FIRST->
TWENTY-SEVENTH, and the v98-era pin-candidate provenance note kept
historical], every correction verified applied — zero misses this
cycle; zero residual old tokens across all four files; bash -n + node
--check clean; the line-count-preservation check green on all four —
the two-half builder inherits the v98 line boundaries). The new probes
this cycle: vlm-shots-v104.sh + clone-vlmshots-v104.sh +
vlm-compare-v104.mjs + arbit-v104.sh (the intermediate combined form,
header-corrected) + build-twohalf-v104.py (the two-half builder — the
ONE census block [SV_CENSUS_JS 153 lines] extracted once, embedded
byte-identically across the halves by the md5 line-block contract
[891ab9b6]) + ref-arbit-v104.sh + clone-arbit-v104.sh +
derive-standing-v104.py (the persisted standing derivation — the 98th
pair, version-bump-only verified by the normalize-back diff) +
ref-standing-v98.sh + standing-checks-v98.sh + brand-arbit-v104.sh (the
v104 pin's own one-shot both-sides census — the base44-fab/userfooter
one-shot pattern applied to the rail's TOP family).

The verdict: DIFFERENT (the pair's documented verdict class) with every
flag DOM-arbitrated: the "Card Footer Layout" the v57
DATA-CONDITIONAL class (the footer childCount 1-vs-2 — the clone's
"Brokerage" chip; the reference RENDERS payment chips when data carries
them per the v97 income-card evidence); the "Card Grid" the seed-count
class (grid childCount 1 vs 2); the header-subtitle + card-contents
flags the seed-data classes (the reference's 1 savings item vs the
clone's 2-item dev seed); the avatar the user-identity class; the
"Edit with Base44" FAB NOT FLAGGED this cycle — the THIRD documented
form (unflagged platform chrome, no attribution either way, no
arbitration needed for an unflagged family). The two-half census
(SV_CENSUS_JS 153 lines, md5 891ab9b6) REPRODUCES the v98 census values
EXACTLY — zero drift on every axis (the h1/grid/card/titleRow/amount/
footer/badge families; the card h 200-vs-230 the v57/v70b
Recurring-wrap class; the clone template's last-column sub-pixel the
column-distribution rounding noise WITHIN the documented 309.328px
family; the docSW 1280 guard) — NO NEW CLONE GAP.

The v104 pin (+1 e2e = 307): the rail's TOP brand-block subtitle/row
census at 1280 (tests/e2e/nav-geometry.spec.ts) — the row {flex,
center, gap 12px} + the h2 {18px/700/lh 28px/rgb(26,58,46)} + the
"Budget Planner" subtitle {12px/400/rgb(45,90,74)} + the tile
40x40/12px + the icon 24x24 context controls; the family never pinned
beyond the v7 G4 tile/icon/h2-size axes (the coverage-map grep across
all 23 specs: the only "Budget Planner" assertion the mobile sheet's
VISIBILITY check). Measured byte-identical on BOTH sides via the
one-shot census brand-arbit-v104.sh. The pin-sanity mutation
(text-xs -> text-sm at sidebar.tsx:48, line-number-scoped — the
section label's line 61 + the user-footer subtitle's line 129
untouched): ONLY the v104 pin red (9 green) at the subtitle.fs axis
ALONE ("12px" -> "14px"; the pin deliberately omits the subtitle's
line-height — text-sm moves fs AND lh, a two-axis failure diff), after
the standalone REBUILD; the v36 nav-pitch band headroom measured live
(navY[0] 145 + the worst-case 4px shift = 149 < 150 — the band
survives); restored, rebuilt, post-restore 10/10 green.

The ship chain: 307 e2e zero flakes (126+90+57+37 = 310 chunk
executions across the four-chunk auditable split = 307 unique); the
seedcheck exact; the screenshots 16/16 BYTE-IDENTICAL (the same-day
regeneration — both the v103 committed set and this cycle's capture on
Oct 21 UTC, the fresh seed's date offsets anchoring identically, no
midnight crossing — the v97 precedent).

### D6 — the operational lessons this cycle

- THE REFERENCE RAIL IS A DIV (a finder note): the brand one-shot's
  first run returned `{err: "no h2"}` on the reference — the `aside h2`
  finder assumed the reference's rail was an `<aside>` like the
  clone's; the reference's rail is a DIV. The v103 userfooter finder
  already carried the geometric fallback chain (aside OR the
  180-320px-wide 700px-tall left-anchored div) — the lesson: every
  cross-side rail finder must use the fallback-chain form, never a
  bare `aside` selector.
- THE UNFLAGGED-FAB CYCLE (a VLM-arbitration note): the v104 pairwise
  report omitted the "Edit with Base44" FAB entirely — after the
  inverted (v85/v91/v103-PAIR1) and non-inverted (v97/v103-PAIR2)
  attribution forms, the THIRD form (no flag at all) is now documented;
  future cycles expect any of the three forms without surprise, and an
  unflagged platform-chrome family needs no arbitration.
- THE SUBTITLE-LH EXCLUSION (a pin-design note): the pin deliberately
  omits the subtitle's line-height axis because the chosen mutation
  (`text-xs` -> `text-sm`) moves fs AND lh together — asserting both
  would make the mutation's failure diff two-axis; the single-axis
  discipline prefers the fs axis alone (the lh implicitly covered by
  the row-height arithmetic in the headroom analysis).

### The v105 cycle (Session 140 — 2026-10-23, PIN-ONLY, +1 e2e = 308)

The queue verified against vlm-shots-v99.sh's own header before the
derivation (the TWENTY-EIGHTH consecutive queue/ledger agreement): the
v99-era LOGIN + CALCULATOR pair — the CALCULATOR dialog + the /login
view at desktop 1280x800, the pair's SEVENTH re-run
[v59 -> v66 -> v75 -> v81 -> v87 -> v93 -> v99 -> v105]. The series
derived via derive-v105-series.py (six files: the calculator pair + the
login pair + the compare + the arbit; the generic swaps + the
exact-fragment history corrections, zero misses, line-count-preserving);
the census built two-half from the start via build-twohalf-v105.py
(CALC 61 + LOGIN 36 lines, md5 e1092d12/9e5a52d2 — the v99 blocks
verbatim); the standing pair derived v98->v99 via
derive-standing-v105.py (version-bump-only verified). The verdicts:
CALCULATOR DIFFERENT (every flag DOM-arbitrated — the "Will update
category total" line the SEED-DATA class [hasWillUpdateSpan false-vs-
true: the reference's own Rent $25.00 equals its calculated total]; the
hover-state flag the RESTING-STATE parity class [actionsAtRest
identical]; the amount-alignment flag the consequence class) + LOGIN
IDENTICAL (the FAB the unflagged platform-chrome third form). The
census reproduces the v99 values exactly — NO NEW CLONE GAP. The +1
pin: the login auth-mode action row census at 1280 (login-parity.spec.ts
— the row {flex, center, space-between, gap 0px, w 368, h 20} + the
forgot context + the signup-side button + the "Sign up" emphasis span;
measured byte-identical both sides via moderow-arbit-v105.sh, the
one-shot form on the logged-out surface; mutation font-medium ->
font-semibold at login-card.tsx:381 line-scoped — the span.fw axis
alone). The ship: 308 e2e zero flakes (311 chunk executions); the
screenshots 9/16 byte-identical + seven fresh-seed deltas arbitrated
(the +2-day roll; the blur-rounding class discovered — see the lessons).

### D6 — the operational lessons this cycle (v105)

- THE MODE-SWITCHER BUTTON CLASS (a finder note): the v105 login
  census's `links` array came back EMPTY on BOTH sides — the login's
  auth-mode switchers ("Forgot password?" / "Need an account? Sign
  up") are BUTTONS on both sides, not anchors; any future census that
  wants the mode-switcher family must find them among `form button` by
  text, never `a[href]`.
- THE SPAN-FW MUTATION FORM (a pin-design note): the chosen mutation
  (`font-medium` -> `font-semibold` on the emphasis span) moves fw
  ALONE — unlike the fs mutations of prior cycles (which drag lh and
  inherited fs with them), a font-weight change on a leaf span is
  single-axis BY CONSTRUCTION, the cleanest mutation form yet; future
  cycles prefer it when the family carries a fw axis.
- THE BLUR-ROUNDING DELTA CLASS (a screenshot-arbitration note): the
  backdrop-blur(8px) scrim regions can show ±1-3 RGB rounding drift
  between capture sessions (the GPU blur compositing's rounding) —
  localized near the dialog panel edges, glyph-free, structure-free.
  The v105 arbitration discipline: decompose every "wide band" by its
  MAX PER-PIXEL DELTA first — glyph rolls read d 400-700, rounding
  drift reads d <= 3; only the former are text changes. A wide band
  with d <= 3 and no ASCII-map structure is rounding noise, never a
  clone gap.

### The v106 cycle (Session 141) — the v100-lineage derivation

- `derive-v106-series.py` (persisted) — the v106 series derived from the
  v100 lineage: vlm-shots-v106.sh + clone-vlmshots-v106.sh +
  vlm-compare-v106.mjs + arbit-v106.sh; the generic swaps + the
  exact-fragment history corrections (era v94-era->v100-era, last-re-shot
  v94->v100, SIXTH->SEVENTH, the bracket extension ...v100 -> v106, the
  TWENTY-THIRD->TWENTY-NINTH agreement ordinal, the census-axes reference)
  — zero misses, zero residuals, line-count-preserving on all four.
- `build-twohalf-v106.py` — the two-half builder (ARBIT_A 90 + ARBIT_B 111
  lines, md5 457438e8/0b895e19): ref-arbit-v106.sh + clone-arbit-v106.sh,
  the census JS byte-identical across the halves.
- `derive-standing-v106.py` — the 100th standing pair (ref-standing-v100.sh
  + standing-checks-v100.sh) from the v99 pair, the THREE token families,
  normalize-back verified version-bump-only.
- `nw-facts-arbit-v106.sh` — the ONE-SHOT both-sides census of the networth
  ASSET CARD's FACTS-ROW interior family (the v106 pin's own axes measured
  byte-identical on both sides before the pin). Finder lessons: the
  "Updated" text is a BARE TEXT NODE beside the svg — no element leaf
  carries it alone, so anchor the row finder on the row div whose
  textContent STARTS WITH "Updated" (a /Updated/ substring match returns
  the space-y-2 WRAPPER first — pre-order traversal); the facts wrapper is
  the Updated row's parentElement, never a walk-up loop (a 12px+svg
  predicate overshoots to the card body).

### D6 — the operational lessons this cycle (v106)

- THE TEXT-LAYER MISREAD CLASS (a VLM-arbitration note): the VLM can
  misread a word's inflection ("Total Expense" vs the DOM's "Total
  Expenses") — a flag class the v43 rule now covers at the TEXT layer:
  when a VLM flag claims a WORD-level difference, read the reference's
  live DOM for the exact string before counting the flag; the DOM is the
  authority at every layer, glyph-level AND word-level.
- THE QUEUE-PROSE VS LINEAGE NAMING (a rotation-ledger note): session
  prose may name the re-run pair by ONE of its surfaces ("the v100-era
  DASHBOARD pair" for the pair whose second surface IS the dashboard's
  drill-down EXPANDED state); the probe lineage's own header (which
  surfaces, which bracket) remains the authority — derive from the
  header, note the prose in the plan.
- THE SINGLE-DIMENSION ICON MUTATION FORM (a pin-design note): the
  cleanest icon-family mutation changes ONE dimension only
  (h-3 w-3 -> h-3 w-3.5: the W axis alone); the row height stays at the
  text line box (max(16, 14) = 16) so no row-height axis cascades —
  single-axis BY CONSTRUCTION, the v92 W-only form's sibling.

### The v107 cycle (Session 142) — the v101-lineage derivation

- `derive-v107-series.py` (persisted) — the v107 series derived from the
  v101 lineage: vlm-shots-v107.sh + clone-vlmshots-v107.sh +
  vlm-compare-v107.mjs + arbit-v107.sh; the generic swaps + the NINE
  exact-fragment history corrections (era v95-era->v101-era, last-re-shot
  v95->v101, SIXTH->SEVENTH, the bracket extension ...v101 -> v107, the
  oldest-remaining list bumped to the current era, the TWENTY-FOURTH->
  THIRTIETH agreement ordinal, the re-proves window v95-v100->v101-v106,
  the arbit verdict reference v95->v101, the drift-re-check v95->v101)
  — 9/9 on the FIRST run, zero residuals, line-count-preserving on all
  four (57/42/45/258).
- `build-twohalf-v107.py` — the two-half builder (ARBIT_G 61 + ARBIT_Q 58
  + ARBIT_X 25 lines, md5 b500dd29/da04e995/7a381755 — the v101 census
  blocks VERBATIM, the blocks themselves version-free): ref-arbit-v107.sh
  + clone-arbit-v107.sh, the census JS byte-identical across the halves.
- `derive-standing-v107.py` — the 101st standing pair (ref-standing-v101.sh
  + standing-checks-v101.sh) from the v100 pair, the THREE token families
  (note the ordinal token's suffix flip 100th->101st), normalize-back
  verified version-bump-only.
- `qarow-arbit-v107.sh` — the ONE-SHOT both-sides census of the
  quick-action card's INTERIOR FLEX-ROW family (the v107 pin's own axes
  measured byte-identical on both sides before the pin). THE
  STRUCTURAL-FINDER LESSON: the reference's row/tile are DIVs while the
  clone's are SPANs — identical computed chrome, different tags — so the
  finders walk POSITIONALLY (the row = the button's firstElementChild;
  the tile = the row's firstElementChild; the icon = the row's first
  svg; the plus = the row's last svg), NEVER by tag; the label leaf
  finder is the v61 leaf lesson generalized TAG-AGNOSTIC (the exact
  text + zero element children, any tag — a div on the reference, a
  span on the clone).

### D6 — the operational lessons this cycle (v107)

- THE STRUCTURAL-FINDER RULE (a census-finder note): when a family's DOM
  tags differ across sites (DIV vs SPAN — the computed-chrome class),
  walk POSITIONALLY (firstElementChild children order), never by tag;
  generalize leaf finders tag-agnostically (exact text + zero element
  children, any tag) — the v61 leaf lesson's next form. A tag-matched
  finder silently returns null on one side and manufactures a false
  gap.
- THE LINE-BREAK FRAGMENT HAZARD (a derive-script note): history-
  correction fragments must be SINGLE-LINE-SAFE — probe headers wrap at
  ~78 chars, so a fragment spanning a line break ("the\n# v95-era pair",
  "SIXTH\n# re-run", "after\n# v95-v100", "The v95\n# verdict") never
  matches; cut each correction fragment to the unbroken span ("v95-era
  pair", "SIXTH", "v95-v100", "The v95") and verify per-file hit counts
  so a miss fails the derivation rather than shipping a stale header.
- THE UNPINNED POSITION-ARITHMETIC AXES (a pin-design note): the census
  may measure position arithmetic byte-identical (the label's 40+12
  junction x = 52; the plus's right-edge anchor = 238), but the PIN
  holds the STRUCTURAL chrome only — position axes co-move with
  unrelated mutations (gap-3 -> gap-4 moves the label's x too), so
  pinning them would break the single-axis mutation discipline; keep
  them census-documented, pin-unasserted.

### The v108 cycle (Session 143) — the v102-lineage derivation

- `derive-v108-series.py` (persisted) — the v108 series derived from the
  v102 lineage: vlm-shots-v108.sh + clone-vlmshots-v108.sh +
  vlm-compare-v108.mjs + arbit-v108.sh; the generic swaps + the EIGHT
  exact-fragment history corrections (the queue source v101-plan ->
  v107-plan, last-re-shot v96->v102, the oldest-remaining bracket
  bumped as TWO single-line halves [the v102 compare header wraps it
  across lines 4-5], SIXTH->SEVENTH, the bracket extension v96->v102
  ->v108, the re-runs' verdict note v84/v90/v96->v84/v90/v96/v102, the
  census-axes provenance v96->v102) — 8/8 on the FIRST run, zero
  residuals, line-count-preserving on all four (60/47/68/219).
- `build-twohalf-v108.py` — the two-half builder (NW_CENSUS 42 +
  DASH_CENSUS 87 lines, md5 82cf8a43/85e4ec7e — the v102 census blocks
  VERBATIM, the blocks themselves version-free): ref-arbit-v108.sh +
  clone-arbit-v108.sh, the census JS byte-identical across the halves.
- `derive-standing-v108.py` — the 102nd standing pair
  (ref-standing-v102.sh + standing-checks-v102.sh) from the v101 pair,
  the THREE token families (the ordinal token's suffix flip
  101st->102nd), normalize-back verified version-bump-only.
- `base44-fab-arbit-v108.sh` — the ONE-SHOT both-sides arbitration for
  the cycle's TWO disproven claims: the FAB census (fabCount 0 +
  bodyHasBase44 false on both sides — the v97/v103 standing disproof
  form, run because a FAB flag WAS raised) EXTENDED with the burger
  glyph census (rect + accessibleName + svgClass + pathD + stroke) —
  BOTH sides byte-identical {24,16,28x28} panel-left 'Toggle Sidebar'.
- `topbar-arbit-v108.sh` — the ONE-SHOT both-sides census of the
  MOBILE TOPBAR's interior junction family (the v108 pin's own axes
  measured byte-identical on both sides before the pin): the header
  {h 61, pad 24/16, border-b 1px rgb(229,231,227), bg white} + the row
  {flex/center/gap 16/h 28/childCount 2} + the burger {24/16/28x28/
  8px} + the icon {16x16, rgb(10,10,10)} + the brand {ZeroBalance,
  20px/700/28px/rgb(26,58,46)}.

### D6 — the operational lessons this cycle (v108)

- THE NPM-CI PROVISIONING RULE (a fresh-clone note): a startup
  module-resolution crash on a LOCKFILE-PINNED package (eslint's
  `Cannot find module '.../zod/v4/index.cjs'` — 59 of 840 files
  installed, the v4/ subdirectory absent while zod 4.6.5's own exports
  map references it) means the LOCAL extraction is corrupt, NOT the
  lockfile: verify the installed file count against the registry
  tarball (`npm pack zod@4.6.5` -> 840 files) and fix with `npm ci`
  (the clean lockfile-exact reinstall, integrity re-verified on every
  package) — never a version change.
- THE GLYPH-MISREAD ARBITRATION (a VLM-flag note): a VLM presence/
  absence claim about an ICON is arbitrated by the svg FINGERPRINT
  (class + pathD + stroke + rect + accessibleName), not by re-asking
  the VLM — the v108 'hamburger missing in Image 2' claim died on the
  byte-identical panel-left fingerprints (the reference's OWN toggle
  is the 28x28 panel-left button documented since v3/v7; no 3-line
  hamburger exists on either side). The VLM's second run did not even
  raise the flag — the non-determinism itself the second form of the
  class.
- THE WRAPPED-BRACKET CORRECTION FORM (a derive-script note): when a
  probe header wraps the oldest-remaining bracket across lines (the
  v102 compare's `[v96 < v97 <` + `v98 < v99 < v100 < v101]`), correct
  it as TWO single-line fragments rather than one multi-line fragment
  — each half gets its own per-file hit count, keeping the
  single-line-safe discipline (the v107 lesson's applied form).

### The v109 cycle (Session 144) — the v103-lineage derivation

- `derive-v109-series.py` (persisted) — the v109 series derived from the
  v103 lineage: vlm-shots-v109.sh + clone-vlmshots-v109.sh +
  vlm-compare-v109.mjs + arbit-v109.sh; the generic swaps + the FIVE
  exact-fragment history corrections (last-re-shot v97->v103, SIXTH-
  era SEVENTH->EIGHTH, the re-run bracket extension
  v91->v97->v103->v109, the later-pairs list [savings v98...v102 ->
  v104...v108] as TWO single-line halves) — 5/5 on the FIRST run (11
  hit-checks), zero residuals, line-count-preserving on all four
  (56/48/49/284).
- `build-twohalf-v109.py` — the two-half builder (CENSUS_JS 193
  lines, md5 b55dcd29 — the v97/v103 census block VERBATIM, the
  block itself version-free but for the v70b finder provenance):
  ref-arbit-v109.sh + clone-arbit-v109.sh, the census JS
  byte-identical across the halves.
- `derive-standing-v109.py` — the 103rd standing pair
  (ref-standing-v103.sh + standing-checks-v103.sh) from the v102
  pair, the THREE token families (the ordinal token's suffix flip
  102nd->103rd), normalize-back verified version-bump-only.
- `base44-fab-arbit-v109.sh` — the ONE-SHOT both-sides arbitration
  for the cycle's FAB flag (fabCount 0 + bodyHasBase44 false on
  BOTH sides at 1280 on /expenses — the v97/v103/v108 standing
  disproof form, run because a FAB flag WAS raised).
- `header-arbit-v109.sh` — the ONE-SHOT both-sides census of the
  ITEMS VIEWS' PAGE-HEADER ROW INTERIOR family (the v109 pin's own
  axes measured byte-identical on both sides on BOTH variants before
  the pin): the row {flex/space-between/center/gap 16/mb 32/h 60} +
  the left block {flex/center/gap 12/h 60/childCount 2} + the chip
  {48x48/12px/the per-type gradient} + the icon {24x24/white} + the
  h1 {30px/700/36px/forestDark} + the subtitle {16px/400/gray} + the
  Add button {147x36 income/155x36 expenses, 6px, 8px 16px, 14px/500,
  white, the per-type gradient} + the plus {16x16/mr 8px}.
- `crop-07-v109.mjs` + `vlm-read-07-v109.mjs` — the screenshot
  arbitration pair for the one fresh-seed delta: the band-crop + the
  VLM read ('10/23/2026' -> '10/24/2026' — the modal's default-date
  field rolling with the UTC day).

### D6 — the operational lessons this cycle (v109)

- THE SINGLE-AXIS CASCADE RULE (a mutation-selection note): when the
  pin's family lives in a SHARED component (items-view.tsx serves
  income + expenses + savings), the mutation target must be an axis NO
  OTHER SPEC asserts in ANY variant — the left block's gap-3 (never
  asserted anywhere) passes; the row's own gap-4/mb-8 would cascade
  into the v65 savings + v52 mobile pins (multi-spec failures). The
  mutation-selection discipline extends from single-axis to
  single-axis AND single-spec-by-construction.
- THE DATE-ROLL ARBITRATION (a screenshot note): a single-band
  maxD-200+ pixel delta in a regenerated set decomposes via the
  band-crop + VLM read — the 07-add-item-modal's one 22-row band read
  as '10/23/2026' -> '10/24/2026' (the default-date field rolling
  with the UTC day) — the documented fresh-seed date-roll class (the
  v104/v105 precedent), the updated set committed.
- THE VERDICT-VARIATION FORM (a VLM note): the pair's verdict may
  vary across re-runs within the documented class set — v103 read
  BOTH DIFFERENT, v109 read INCOME IDENTICAL + EXPENSES DIFFERENT; the
  income side's documented flags were all-data classes, so the
  IDENTICAL verdict is the cleaner outcome on the same chrome (the
  v105 LOGIN-IDENTICAL precedent) — the CLASSES, not the verdict
  string, are the contract.

### The v110 cycle (Session 145) — the v104-lineage derivation

- `derive-v110-series.py` (persisted) — the v110 series derived from
  the v104 lineage: vlm-shots-v110.sh + clone-vlmshots-v110.sh +
  vlm-compare-v110.mjs + arbit-v110.sh; the generic swaps + the NINE
  exact-fragment history corrections (the plan-source fragment reads
  `v103 plan's` NOT `the v103 plan's` — the 'the' sits at the END of
  the preceding line, a live derivation discovery; last-re-shot
  v98->v104, the era marker v98-era->v104-era, SEVENTH->EIGHTH, the
  re-run bracket extension [v58 -> ... -> v98 -> v104 -> v110], the
  oldest-remaining bracket [v104 < v105 < ... < v109],
  TWENTY-SEVENTH->THIRTY-THIRD, the queue-source v103 plan -> v109
  plan) — 9/9 on the FIRST run (11 hit-checks), zero residuals,
  line-count-preserving on all four (49/41/38/261).
- `derive-build-twohalf-v110.py` (persisted) + `build-twohalf-v110.py`
  — the builder derivation (the swap-order lesson: the GENERIC version
  swap FIRST, the lineage-note fixups LAST so no later swap re-touches
  the inserted tokens; normalize-back verified) + the two-half builder
  (SV_CENSUS_JS 153 lines, md5 891ab9b6 — the v98/v104 census block
  VERBATIM, the builder-form md5 verified against the EXISTING v104
  halves): ref-arbit-v110.sh + clone-arbit-v110.sh, the census JS
  byte-identical across the halves.
- `derive-standing-v110.py` — the 104th standing pair
  (ref-standing-v104.sh + standing-checks-v104.sh) from the v103
  pair, the THREE token families (the ordinal token's suffix flip
  103rd->104th), normalize-back verified version-bump-only.
- `nav-arbit-v110.sh` — the ONE-SHOT both-sides census of the RAIL's
  NAV-BLOCK INTERIOR family (the v110 pin's own axes measured
  byte-identical on both sides at 1280x800 on /savings before the
  pin): the 'Navigation' label {32px/12px/600/uppercase/0.6px/
  rgb(45,90,74)/8px 12px/6px radius} + the UL {flex column/gap 4/5
  links/215 wide} + the LI {relative/mb 0/36px} + the link box
  controls + the nav ICON {16x16} + the span truncate family + the
  ACTIVE link {the 135deg gradient/white/500/32px}. The
  reference-side finder is STRUCTURAL (the reference renders NO nav
  landmark — its documented no-landmark bug): the ul is found by its
  5-anchor shape, the label by the wrapper-sibling walk with the
  childless-uppercase-div fallback, the active link by
  aria-current OR the gradient OR the text.
- `vlm-read-crops-v110.mjs` — the screenshot arbitration read for the
  SIX fresh-seed deltas (the +1-day date rolls VLM glyph-read: 'Oct
  18' -> 'Oct 19', 'Oct 13' -> 'Oct 14', 'October 14, 2026' ->
  'October 15, 2026'; the 08/16 y817-900 bands the v105-documented
  backdrop-blur scrim rounding drift [maxDelta 1-2, zero glyphs] —
  zero structural bands, the updated set committed).

### D6 — the operational lessons this cycle (v110)

- THE SECURITY-BUMP RE-VERIFICATION PATH (a dependency note): the
  first production-dependency change since v68 ran through the full
  parity apparatus — npm audit added to the F0b audit (a NEW standing
  audit step), the exposure analysis FIRST (all three next paths
  unexposed; the zod exposure real but rate-limit-bounded), the
  minimal in-range fix (package.json untouched, 43 lockfile pins),
  then the standing checks + the VLM pair + the census + the ship
  chain + the screenshots byte-compare ALL re-run against the bumped
  tree — 10/16 byte-identical proves the bump produced ZERO visual
  drift (the six deltas all the documented date-roll/scrim classes).
- THE PHANTOM-GLITCH DISPEL (a tooling note): the v107-era 'save
  glitch' never existed — od-hexdump verifies ALL committed dev
  scripts (v107/v108/v109) carry the byte-correct a[href*=
  "income"]:visible locator on disk; the perceived '[h' loss is a
  DISPLAY-layer artifact (the tool-output pipeline eats the [h
  sequence — escape-sequence filtering), never a file defect. The
  v108/v109 comments described fixing a phantom. ANY tool output
  showing a bracket-h sequence must be od-verified before acting on
  it.
- THE NO-LANDMARK FINDER RULE (a census note): a census finder must
  never assume the clone's element semantics exist on the reference —
  the reference's documented no-landmark bug means NO nav element on
  its side; the first nav-arbit-v110 run returned 'no nav' until the
  finder was rewalked STRUCTURALLY (the ul by its 5-anchor shape).
  The reference's OWN bugs are part of the finder contract.
- THE SWAP-ORDER RULE (a derivation note): when deriving a builder
  script with token swaps PLUS lineage-note fixups that insert
  version tokens, the GENERIC version swap runs FIRST and the
  fixups LAST — else the generic swap re-touches the inserted tokens
  (the first derive-build-twohalf-v110 attempt failed its
  normalize-back on exactly this).

The v111 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v104-era SAVINGS pair (the v105-era LOGIN + CALCULATOR pair —
the LOGIN view + the CALCULATOR dialog at desktop 1280x800, last re-shot
v105 — now the oldest remaining [v105 < v106 < v107 < v108 < v109 <
v110]; the pair's EIGHTH re-run bracket [v59 -> v66 -> v75 -> v81 ->
v87 -> v93 -> v99 -> v105 -> v111] to be verified against
vlm-shots-v105.sh's own header before the derivation), (2) the axe-core
watch at its next re-check point (only a 5.x wrapper changes the
calculus), (3) the npm-audit watch at its re-check point (the NEW
standing audit step — only a new advisory in the next/zod ranges
changes the calculus), (4) the deferred reference-write censuses
(unchanged — out of bounds under the v46 read-only rule).

## The v113 cycle (the v107-era BUDGET GUIDELINES + QUICK-ACTION pair's EIGHTH re-run — Session 148)

The re-run cadence's next-oldest candidate: the v107-era BUDGET
GUIDELINES + QUICK-ACTION pair (both v61 target surfaces below the fold
on the DASHBOARD at desktop 1280x800 FULL-PAGE, last re-shot v107 — now
the oldest remaining [v107 < v108 < v109 < v110 < v111 < v112]; the
pair's EIGHTH re-run bracket [v61 -> v68 -> v77 -> v83 -> v89 -> v95 ->
v101 -> v107 -> v113]; the THIRTY-SIXTH consecutive queue/ledger
agreement — the surface names verified against vlm-shots-v107.sh's own
header before the derivation). PIN-ONLY for src/; the cycle's standing
items: the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe
verified), the npm-audit watch at its fourth re-check (0
vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]), the
107th standing checks (ALL GREEN — the mobile menu the 107th
consecutive green; the reference's four bugs all live; the data census
clean on the FIRST reads, no render-race hit this cycle). The verdict:
IDENTICAL — ZERO layout/style flags on the pair's own target surfaces
(the SIXTH consecutive IDENTICAL verdict for this pair [v83 -> v89 ->
v95 -> v101 -> v107 -> v113]; the only flags the documented seed-data
classes; no FAB flag raised — the v103 standing class). The two-half
census (ARBIT_G 61 lines md5 b500dd29 + ARBIT_Q 58 lines md5 da04e995 +
ARBIT_X 25 lines md5 7a381755 — the version-free v101/v107 census
blocks carried over VERBATIM), compared axis-by-axis by the persisted
compare-v113-census.py (154 axes: 144 identical + 10 deltas, every
delta a documented class — the shadow lead-layer count the v66
INVISIBLE class; the quick-action label census delta the v61 label
lesson [the finder's wrapper catch; the clone's LEAF carries the
identical chrome — the v61 F3 + v107 F4 pins]; the grid mt the v77
mechanism class [the rendered gap byte-identical at 340]; the gridCls
strings the site-source class), reproduces the v107 values exactly —
the PART X hard axes cardBottom 1122/gridTop 1462/gap 340 byte-
identical — NO NEW CLONE GAP. The +1 pin (tests/e2e/dashboard.spec.ts):
the Budget Guidelines card's TILE LABEL-ROW family + the tile stack
rhythm at 1280 — the row {flex/center/space-between/mb 4px/h 24/w 384/
childCount 2} + the rhythm {gap1 12/gap2 12} — never pinned at ANY
viewport in ANY spec (the label/pct x-position axes stay
census-documented but UNPINNED — the v107 xInRow discipline), measured
byte-identical both sides via the one-shot glrow-arbit-v113.sh (the
finders structural: the childless-exact-text heading + the
shadow/radius/p card walk-up + the flex-ancestor-of-the-label-that-
contains-the-pct row walk), mutation-verified single-axis AND
cascade-free (justify-between -> justify-start at dashboard-view.tsx:847
line-scoped — the ONLY mb-1 flex items-center justify-between line in
the file; only the v113 pin red at the row.justify axis alone
[space-between -> flex-start] after the standalone REBUILD; the v61/
v77/v83/v89/v101/v107/v112 pins green under the mutation). The ship
chain: 316 e2e zero flakes (83+77+75+84 = 319 executions = 316 unique);
35/35 smoke; the screenshots 16/16 byte-identical (the same-day-seed
law); the dev evidence re-captured + VLM-verified.

- THE IDEMPOTENT-RUN DUPLICATION TRAP (an alignment-scripting lesson):
  the align-docs re-run after a mid-script MISS duplicated every
  insert-after edit (the anchor text SURVIVES the insertion, so the
  second run inserts a SECOND copy) — grep -c undercounts (it counts
  LINES, not occurrences, and the docs carry one paragraph per line);
  the repair the persisted dedup-align-v113.py (grep -o | wc -l is the
  occurrence counter; the alignment scripts' insert-after edits are
  NOT idempotent — rerunning requires a dedup pass or an
  already-applied guard).

## The v112 cycle (the v106-era NETWORTH + drill-down-DASHBOARD pair's EIGHTH re-run — Session 147)

The re-run cadence's next-oldest candidate: the v106-era NETWORTH +
drill-down-DASHBOARD pair (the desktop 1280x800 FULL-PAGE NETWORTH view
+ the DASHBOARD's drill-down EXPANDED state, the v60-era pair's
surfaces, last re-shot v106 — now the oldest remaining [v106 < v107 <
v108 < v109 < v110 < v111]; the pair's EIGHTH re-run bracket [v60 ->
v67 -> v76 -> v82 -> v88 -> v94 -> v100 -> v106 -> v112]; the
THIRTY-FIFTH consecutive queue/ledger agreement — the surface names
verified against vlm-shots-v106.sh's own header before the derivation).
PIN-ONLY for src/; the cycle's standing items: the axe watch (NO DRIFT
— 4.14.0 holds, the v68 dedupe verified), the npm-audit watch at its
third re-check (0 vulnerabilities — the v110 bump holds [next 16.4.3 +
zod 4.6.7]), the 106th standing checks (ALL GREEN — the mobile menu the
106th consecutive green; the reference's four bugs all live). The
verdicts: BOTH PAIRS DIFFERENT (the pair's documented verdict class)
with every flag DOM-arbitrated to a documented class (the FAB the
platform-chrome class DISPROVEN live [fabCount 0 + bodyHasBase44 false
on BOTH sides]; the nav-highlight delta the v56 SUPERSET class; the
avatar the user-identity class; the progress fill the pct DATA class
over the byte-identical 568px track; the donut labels the v60
perception class; the stat-card footer "dashed line" a NEW VLM
perception-flag form DISPROVEN live [the leader SOLID + byte-identical
both sides — the v88 pin's family]; the "Total Expense" singular the
v106-documented text-misread re-disproven [statTitles PLURAL on BOTH
sides]; the data figures the seed-data classes). The two-half census
(ARBIT_A 90 lines md5 6fda636c + ARBIT_B 111 lines md5 9a4e73cc — the
block deltas verified version-bump-only, exactly the two census
view-label tokens) reproduces the v106 values exactly — NO NEW CLONE
GAP. The +1 pin (tests/e2e/dashboard.spec.ts): the drill-down card's
NET-BALANCE FOOTER ROW interior at 1280 — the border-t wrapper {mt 12px
/ pt 12px / 1px rgb(229,231,227)} + the row {flex/center/
space-between/h 32} + the left block {flex/center/gap 8px/h 32} + the
chip {32x32/radius 8px/rgba(245,169,98,0.125)} + the chip icon {16x16,
the twin-polyline trending-up glyphSig, 0 0 24 24} + the label
{"Net Balance"/14px/600/rgb(107,114,128)/h 20} + the value {18px/700/
rgb(245,169,98)/h 28} + the junction (chipCy === rowCy === labelCy) —
never pinned at ANY viewport in ANY spec, measured byte-identical both
sides via the one-shot netrow-arbit-v112.sh, mutation-verified
single-axis AND cascade-free (font-semibold -> font-bold at
dashboard-view.tsx:532 line-scoped — the line-135 occurrence
untouched; only the v112 pin red at label.fw alone [600 -> 700] after
the standalone REBUILD). The ship chain: 315 e2e zero flakes (82+80+
72+84 = 318 executions = 315 unique); 35/35 smoke; the screenshots
16/16 byte-identical (the same-day-seed law); the dev evidence
re-captured + VLM-verified.

- THE REGEXP-DOLLAR RULE (a one-shot-census addendum — the v64 rule's
  sharpest form yet): a `new RegExp('^[-+]' + D + '...')` built from
  String.fromCharCode(36) inserts a RAW dollar into the pattern — where
  it is the regex END-ANCHOR, so the money-leaf finder silently matches
  NOTHING ("no value leaf" on both sides, zero errors). The literal
  dollar in a RegExp pattern needs the ESCAPED form: build the
  pattern as '^[-+]\\' + D + '[\\d,]+...' so the regex receives
  "\$". Symptom class: a census that returns a finder-miss string on
  BOTH sides with no JS error — check the escape chain BEFORE blaming
  the DOM or the seed.
- THE RENDER-RACE RE-READ (a standing-checks note, the v75 convention
  applied): the reference's data census can read "no match" on ONE
  view after a long eval gap (the session EXPIRES between the R-bug
  checks and the census; the page re-renders the login flash before
  the view hydrates) — the disciplined response is the cold re-login
  re-read, which returned "4 items · $525.00" EXACT this cycle. It is
  the documented session-expiry class, NEVER a reference data change;
  do not re-document the census values off the racy read.

The v114 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v107-era BUDGET GUIDELINES + QUICK-ACTION pair (the v108-era
MOBILE TWINS pair — BOTH mobile 390x844 full-page twins: the /NETWORTH
view [the v63-era pair's surface] and the DASHBOARD [the v62-era mobile
twin's surface], last re-shot v108 — now the oldest remaining [v108 <
v109 < v110 < v111 < v112 < v113]; the pair's EIGHTH re-run bracket
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114] to
be verified against vlm-shots-v108.sh's own header before the
derivation), (2) the axe-core watch at its next re-check point (only a
5.x wrapper changes the calculus), (3) the npm-audit watch at its
re-check point (only a new advisory in the next/zod ranges changes the
calculus), (4) the deferred reference-write censuses (unchanged — out
of bounds under the v46 read-only rule).

## The v122 cycle (the v116-era SAVINGS pair's TENTH re-run — Session 157)

The re-run cadence's next-oldest candidate: the v116-era SAVINGS pair —
the SAVINGS view at desktop 1280x800 FULL-PAGE, the v58-era savings
pair's surface family, last re-shot v116 — now the oldest remaining
[v116 < v117 < v118 < v119 < v120 < v121]; the pair's TENTH re-run
bracket [v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98 -> v104 -> v110
-> v116 -> v122]; the FORTY-FIFTH consecutive queue/ledger agreement —
the surface names verified against vlm-shots-v116.sh's own header
BEFORE the derivation, with the v116 header's own NINTH ordinal
CONSISTENT with its 10-entry bracket [v58 the original — no off-by-one
this lineage]. **A PIN-ONLY cycle for src/ — zero production-code
changes** + one e2e pin + ONE tests-only spec repair (the cycle's
baseline find); the cycle's standing items: the axe watch (NO DRIFT —
4.14.0 holds, only the canary sha prerelease beyond, the v68 dedupe
verified), the npm-audit watch at its thirteenth re-check (0
vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]), the
116th standing checks (ALL GREEN — the mobile menu the 116th
consecutive green; the reference's four bugs all live; the data census
clean on the FIRST reads, no render-race hit this cycle).

**F0 baseline: ONE LIVE RED on the first chunk — THE v120 PIN'S
DATE-AXIS TIME-BOMB, repaired tests-only (the cycle's baseline find)**:
the chunk-1 run (dashboard + networth + networth-error) failed the
v120 liability-card pin at its third facts row — `txt: "Updated Oct 25,
2026"` expected vs `"Oct 26, 2026"` received. THE MECHANISM:
prisma/seed.ts stamps the liabilities' `lastUpdated: isoDate(0)` —
TODAY at seed time — and net-worth-view.tsx renders it via
toLocaleDateString; the e2e global-setup re-seeds db/e2e.db on EVERY
run, so the rendered text is always the RUN DAY. The v120 cycle
authored the pin with the LITERAL date string — green on its own seed
day (2026-10-25, both the v120 and v121 cycles shipping before the UTC
rollover), red every day after: a TIME-BOMB AXIS, the same-day-seed
law's spec-side blind spot (the screenshots side has honored the law
since v77; the e2e side never hit it because every prior run happened
same-day). It is the ONLY literal-date assertion in the suite. THE
REPAIR (TDD — the live red IS the red phase): the axis computed from
the seed's own rule — `new Date().toLocaleDateString("en-US", {month:
"short", day: "numeric", year: "numeric"})` in the spec process (the
same TZ class as the seed and the rendered page), the row asserted as
the template `Updated ${seedDay}` (the midnight-crossing window
accepted per the law); the full networth file 36/36 green after the
repair; the mutation proof inherent (the axis red when the underlying
value rolled a day). The rest of the baseline FULLY GREEN on the
FRESH-CLONE-PROVISIONED workspace (the RESET class — the v121
environment did not persist; the repo re-cloned from main @ 075df6d;
the v108 FRESH-CLONE provisioning end-to-end: npm ci in the foreground
[354 entries], the zod extraction verified intact, BOTH v1243
playwright pairs installed with INSTALLATION_COMPLETE verified, the
explicit-env-prefix Prisma discipline, the seedcheck exact before any
gate). The gates: lint · typecheck · 108/108 unit · build (robots +
sitemap prerendered) · **324 e2e ZERO FLAKES after the repair**
(87+81+77+82 = 327 executions = 324 unique, every chunk green on its
FIRST run) · 35/35 smoke. The post-push commits audited
session-log-only.

**F2 the 116th standing checks ALL GREEN** (the pair derived from the
v115 pair via the persisted derive-standing-v122.py — three token
families, normalize-back diff clean, zero old tokens): the reference's
four bugs all live [toast-blocker hitIsBurgerChild:false; sheet-trap
overlayCount:1 after nav; no-landmark navLandmark:false; the 464px
/networth overflow measured docSW 464 directly]; the data census clean
on the FIRST reads; the SEO pair live both sides; the clone's mobile
menu VERIFIED WORKING the 116th consecutive time (zero overflow at 390
on all five views); the seedcheck exact after the clone half.

**F3 the re-run pair**: the probe series derived from the v116 lineage
(the persisted derive-v122-series.py — the generic swaps + EIGHT
exact-fragment history corrections [the era re-pointed v110-era ->
v116-era, last-re-shot v110 -> v116, the oldest-remaining list
re-pointed, NINTH -> TENTH, the plan attribution v115 plan's -> v121
plan's, THIRTY-NINTH -> FORTY-FIFTH, the bracket extension], 8/8
families applied on the FIRST run, 19 instances, line counts preserved
50/42/39/262); the census BUILT two-half from the start
(build-twohalf-v122.py — ref-arbit-v122.sh + clone-arbit-v122.sh, the
ONE census JS block [SV_CENSUS_JS 153 lines] byte-identical across the
halves, the md5 line-block contract [891ab9b6 — the v104/v110/v116
census blocks VERBATIM]; the STALE refarbit116 SESSION TOKEN in the
builder's ref_exec assertion FIXED to refarbit122 — the no-'v'-prefix
bare token the generic swap cannot touch, the v116 lineage's own
documented repair class); the comparator derived
(derive-compare-v122.py -> compare-v122-census.py — the census-era
corrections, the provenance citations re-pointed at the v116
measurement). **The verdict pass 1 IDENTICAL / pass 2 DIFFERENT — the
pair's VLM-verdict VARIATION form (the documented class: v98/v104/v110/
v116 read DIFFERENT; the IDENTICAL pass the cleaner all-data-classes
outcome — the v105 LOGIN-IDENTICAL + the v121 pass-2 INCOME-IDENTICAL
precedents)** — every pass-2 flag DOM-arbitrated: the card-grid the
SEED-COUNT class (grid.childCount 1-vs-2, the template/gap/w
byte-identical, the card w 309 both sides); the footer content the v58
DATA-CONDITIONAL class (the reference's savings item ships no
paymentMethod — the date-only DIV, childCount 1 — while the clone's
render the SPAN pair, the same two-child structure the reference's own
income card renders); the badge styles the classification-VALUE + v57
wrap/SUPERSET-CHIP classes (badges[0] need-red vs savings-green,
badges[2] active-slate vs Recurring-green-iconed; badgeRow h 22-vs-52
+ n 3-vs-4 — the Recurring superset chip + the wrap; the per-badge
chrome byte-identical); the avatar the user-identity class; the figures
the seed-data classes. The both-sides census compared AXIS-BY-AXIS by
the persisted compare-v122-census.py: **120 axes — 80 identical + 40
documented-class deltas, ZERO new** (the v116 values reproduced
EXACTLY, the same 120/80/40 split). NO NEW CLONE GAP.

**F4 the pin — the SAVINGS goal-card kebab-trigger's OPEN-MENU reveal
census at 1280 (the never-pinned PATH of the pinned reveal family,
PIN-ONLY — +1 e2e = 325)**: the trigger's reveal has THREE paths — the
HOVER path (group-hover:opacity-100, pinned by the v116 pin), the
KEYBOARD path (focus-visible:opacity-100, pinned by the v36 S3
Tab-order census), and the OPEN path (data-[state=open]:opacity-100 —
superset fix #7's "stays revealed while its menu is open" clause) —
the OPEN path held by NO spec (the v98 pin opens the menu but
censuses the PANEL + menuitem interior only; the behavioral specs
never read the trigger's opacity). The CLONE-ONLY form (the v46 F3
adapted precedent): the reference's trigger stays INVISIBLE (opacity
0) when its menu is opened (its own superset-#7 bug) and a
reference-side measurement would require a CLICK (the v46 read-only
rule: passive navigation + real pointer hover only) — the pin locks
the CLONE's own superset chrome; the family chrome = the v116 pinned
contract BY CONSTRUCTION (the identical class string: item-card.tsx:
139). The one-shot census (kebabopen-arbit-v122.sh — the
REVEAL-LADDER form: at-rest 0 -> hover 1 -> open+parked 1 [THE AXIS]
-> dismissed; the synthetic PointerEvent/MouseEvent sequence does NOT
move the real pointer, so the group-hover path stays disengaged
through the open read, isolating the data-[state=open] token; the
dynamic card-center read in the v116 plain 'x,y' convention — the
JSON form's escaped quotes break the shell-side extraction) measured:
the open+parked state {opacity "1" / dataState "open" / the box chrome
unchanged 36x36 / radius 6px / bg transparent / color rgb(10,10,10) /
cardTop 21 / cardRight 21} — with the REAL pointer parked at (5,5),
the data-[state=open] token ALONE holding the reveal. TWO
census-world artifacts documented (the synthetic-pointerdown
focus-return leaves Chromium's focus-visible heuristic in keyboard
mode — the post-restore trigger reads the v36 keyboard-path "1", not
the at-rest "0"; the restore read asserts the DISMISSED state only).
THE PIN'S LIVE-RED DISCOVERY (documented in the spec comment):
getByRole(name) is UNRESOLVABLE mid-open — Radix's modal layer marks
the app aria-hidden, EXCLUDING the trigger from the accessibility
tree — the STRUCTURAL aria-label CSS finder the fix (the v72
discipline). The +1 e2e pin (tests/e2e/items.spec.ts, appended by the
persisted append-pin-v122.py): the open+parked reveal census at 1280 —
the at-rest baseline + the axis + the unchanged box chrome + the
fixture-restore Escape (the v98 form; no menuitem ever clicked — the
data never touched). The pin-sanity mutation (item-card.tsx:139
line-scoped data-[state=open]:opacity-100 -> opacity-90; the
net-worth-view.tsx:82/192 family twins untouched by the file+line
scoping): the SOLE FAILURE verified live — the pin ALONE red at the
opacity axis ("1" -> "0.9"), the full items run 47 others green (the
v116 hover-path / v36 keyboard / v98 panel / v121 confirm-bar / v45
at-rest pins all immune); restored + the full rebuild (the v98
REBUILD discipline) + the 48/48 post-restore regression + the networth
kebab twins green (the different-file immunity).

**F5 the ship chain**: lint · typecheck · 108 unit · 0 vulnerabilities ·
**325 e2e zero flakes** (87+82+77+82 = 328 executions = 325 unique) ·
35/35 smoke. **The screenshots 7/16 regenerated — the DAY-ROLLOVER
REFRESH (the same-day-seed law's expected consequence: the committed
set was same-day with the Oct 25 seed, the re-capture same-day with
the Oct 26 seed — the date-only diffs VLM-verified [the card footers'
Updated dates Oct 17->18 / Oct 18->19], ZERO chrome drift, the other 9
byte-identical)**; the dev evidence 4/4 captured + VLM-verified (3
byte-identical + dev-mobile-income-390 the date-only refresh; the menu
proof: /income, docSW 390, navLandmark true; the menu open with all 5
links + the brand; the sheet closed post-nav; the dashboard clean —
the dev-shots scripts derived v121->v122 with the version-swap-only
verification).

The v123 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v116-era SAVINGS pair (the v117-era LOGIN + CALCULATOR pair —
the LOGIN page + the CALCULATOR dialog at desktop 1280x800, the
v59-era pair's surface family, last re-shot v117 — now the oldest
remaining [v117 < v118 < v119 < v120 < v121 < v122]; the pair's TENTH
re-run bracket [v59 -> v66 -> v75 -> v81 -> v87 -> v93 -> v99 -> v105
-> v111 -> v117 -> v123] to be verified against vlm-shots-v117.sh's
own header before the derivation — the v117 header's own NINTH ordinal
should be consistent with its 10-entry bracket [v59 the original], so
v123 = the TENTH re-run by the same convention), (2) the axe-core
watch at its next re-check point (only a 5.x wrapper changes the
calculus), (3) the npm-audit watch at its re-check point (only a new
advisory in the next/zod ranges changes the calculus), (4) the
deferred reference-write censuses (unchanged — out of bounds under the
v46 read-only rule).

## The v123 cycle (the v117-era LOGIN + CALCULATOR pair's TENTH re-run — Session 158)

The re-run cadence's next-oldest candidate: the v117-era LOGIN +
CALCULATOR pair — the LOGIN view + the CALCULATOR dialog at desktop
1280x800, the v59-era pair's surface family, last re-shot v117 — now the
oldest remaining [v117 < v118 < v119 < v120 < v121 < v122]; the pair's
TENTH re-run bracket [v59 -> v66 -> v75 -> v81 -> v87 -> v93 -> v99 ->
v105 -> v111 -> v117 -> v123]; the FORTY-SIXTH consecutive queue/ledger
agreement — the surface names verified against vlm-shots-v117.sh's own
header BEFORE the derivation (the v117 header's own NINTH ordinal
CONSISTENT with its 10-entry bracket [v59 the original — no off-by-one
this lineage]). **A PIN-ONLY cycle for src/ — zero production-code
changes** + one e2e pin; the cycle's standing items: the axe watch (NO
DRIFT — 4.14.0 holds, only the canary sha prerelease beyond, the v68
dedupe verified), the npm-audit watch at its fourteenth re-check (0
vulnerabilities — the v110 bump holds), the 117th standing checks (ALL
GREEN — the reference's four bugs live; the data census clean on the
FIRST reads; the clone's mobile menu VERIFIED WORKING the 117th
consecutive time; zero overflow at 390 on all five views; the seedcheck
exact after the clone half).

The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs this cycle
(the v122 date-axis repair verified holding on the new day: the v120
liability-card pin green with its computed seedDay form). The verdict:
**CALCULATOR DIFFERENT ×2 / LOGIN IDENTICAL ×2** (the consistent form —
no variation this cycle) — every flag DOM-arbitrated: the row action
buttons + the "shorter row" the POINTER-POSITION/HOVER-STATE screenshot
artifact + the VLM MISREAD (the census `actionsAtRest {opacity "0",
btnCount 2}` IDENTICAL both sides + `row.h 102` byte-identical; the
mechanism: the REFERENCE shots script captures BEFORE parking its
pointer — still at the Calculate button, INSIDE the opened dialog —
while the CLONE script parks at (5,5) BEFORE its capture; the shots
scripts' own structure, inherited verbatim from the v59 lineage); the
"Will update category total" note the SEED-DATA class; the login
"Edit with Base44" badge the PLATFORM-CHROME class disproven live
(base44-fab-arbit-v123.sh: fabCount 0 + bodyHasBase44 false BOTH
sides). The two-half census (build-twohalf-v123.py from the v117
builder — the TWO blocks CALC_CENSUS_JS 61 lines + LOGIN_CENSUS_JS 36
lines byte-identical across the halves, the md5 line-block contract
verified by direct python extraction; compare-v123-census.py with the
census-era corrections + the /tmp/vlm-path explicit swap [the bare
v117 swap cannot touch 'vlm117' — no 'v117' substring]): **106 axes —
97 identical + 9 documented-class deltas, ZERO new**.

The pin: the CALCULATOR line-item DELETE-CONFIRM BAR census at 1280
(confirmbar-arbit-v123.sh — the one-shot CONFIRM-LADDER census; the
never-pinned FOURTH member of the confirm-bar family: the v121 pin
holds the item-card bar, the net-worth twins are held BY CONSTRUCTION
via the identical class strings, the calculator's mt-3 variant held by
NO spec; the CLONE-ONLY form — the reference's row delete destroys
immediately, its R6 bug, and a reference-side measurement would need a
DESTRUCTIVE click under the v46 read-only rule): the bar {mt "12px" /
flex / center / space-between / radius "8px" / pad "12px" / w 686 /
h 48} + the label 14px/400 + the pills {4px 12px / 6px / 12px/500 /
h 24} + the shadow-sm VISIBLE layer + **the +60 bar-open delta (the
row card 102 -> 162)** + the Cancel path. The pin-sanity mutation
(p-3 -> p-4 at calculator-dialog.tsx:279, line-scoped, the mt-4 family
twins untouched): the SOLE FAILURE verified live — the pin ALONE red at
the pad + h axes, the full calculator file's 19 others green. The
census script's own first-run bug fixed live: the agent-browser
`mouse move` takes x y as TWO args — the single-arg "x,y" form moves
nowhere. The ship: 326 e2e zero flakes (87+86+74+82 = 329 executions =
326 unique); 35/35 smoke; the screenshots 16/16 byte-identical (the
same-day-seed law — no day-rollover this cycle); the dev evidence 4/4
byte-identical + VLM-verified (the menu proof: /income, docSW 390,
navLandmark true; the dev-shots scripts derived v122 -> v123 with the
version-swap-only verification).

The v124 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v117-era LOGIN + CALCULATOR pair (the v118-era NETWORTH +
drill-down-DASHBOARD pair — the /networth view + the dashboard
drill-down at desktop 1280x800, the v60-era pair's surface family,
last re-shot v118 — now the oldest remaining [v118 < v119 < v120 <
v121 < v122 < v123]; the pair's ELEVENTH re-run bracket [v60 -> v67 ->
v76 -> v82 -> v88 -> v94 -> v100 -> v106 -> v112 -> v118 -> v124] to be
verified against vlm-shots-v118.sh's own header before the derivation —
the v118 header's own TENTH ordinal should be consistent with its
11-entry bracket [v60 the original], so v124 = the ELEVENTH re-run by
the same convention), (2) the axe-core watch at its next re-check point
(only a 5.x wrapper changes the calculus), (3) the npm-audit watch at
its re-check point (only a new advisory in the next/zod ranges changes
the calculus), (4) the deferred reference-write censuses (unchanged —
out of bounds under the v46 read-only rule).

## The v121 cycle (the v115-era ITEMS pair's TENTH re-run — Session 156)

The re-run cadence's next-oldest candidate: the v115-era ITEMS pair —
the ITEMS view (income + expenses) at desktop 1280x800 FULL-PAGE, the
v57-era items pair's surface family, last re-shot v115 — now the oldest
remaining [v115 < v116 < v117 < v118 < v119 < v120]; the pair's TENTH
re-run bracket [v57 -> v64 -> v70 -> v79 -> v85 -> v91 -> v97 -> v103
-> v109 -> v115 -> v121]; the FORTY-FOURTH consecutive queue/ledger
agreement — the surface names verified against vlm-shots-v115.sh's own
header BEFORE the derivation, with the v115 header's own NINTH ordinal
CONSISTENT with its 10-entry bracket [v57 the original — no off-by-one
this lineage]. **A PIN-ONLY cycle for src/ — zero production-code
changes** + one e2e pin; the cycle's standing items: the axe watch (NO
DRIFT — 4.14.0 holds, only the canary sha prerelease beyond, the v68
dedupe verified), the npm-audit watch at its twelfth re-check (0
vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]), the
115th standing checks (ALL GREEN — the mobile menu the 115th
consecutive green; the reference's four bugs all live; the data census
clean on the FIRST reads, no render-race hit this cycle).

**F0 baseline FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace**
(the RESET class — the v120 environment did not persist; the repo
re-cloned from main @ 19d6d1f; the v108 FRESH-CLONE provisioning
end-to-end: npm ci in the foreground, the zod extraction verified
intact, BOTH v1243 playwright pairs installed with
INSTALLATION_COMPLETE verified, the explicit-env-prefix Prisma
discipline [the v119 workspace-root .env discovery], the seedcheck
exact before any gate). The gates: lint · typecheck · 108/108 unit ·
build (robots + sitemap prerendered) · **323 e2e ZERO FLAKES**
(87+80+77+82 = 326 executions = 323 unique, every chunk green on its
FIRST run) · 35/35 smoke. The post-push commits audited
session-log-only.

**F2 the 115th standing checks ALL GREEN** (the pair derived from the
v114 pair via the persisted derive-standing-v121.py — three token
families, normalize-back diff clean, zero old tokens): the reference's
four bugs all live [toast-blocker hitIsBurgerChild:false; sheet-trap
overlayCount:1 after nav; no-landmark navLandmark:false; the 464px
/networth overflow measured docSW 464 directly]; the data census clean
on the FIRST reads; the SEO pair live both sides; the clone's mobile
menu VERIFIED WORKING the 115th consecutive time (zero overflow at 390
on all five views); the seedcheck exact after the clone half.

**F3 the re-run pair**: the probe series derived from the v115 lineage
(the persisted derive-v121-series.py — the generic swaps + FIVE
exact-fragment history corrections [last-re-shot v109->v115, the
ordinal NINTH->TENTH, the bracket extension -> v109 -> v115 -> v121,
the later-pairs list re-pointed, the re-shot era], 5/5 applied on the
FIRST run, 12 instances, line counts preserved 57/49/50/285); the
census BUILT two-half from the start (build-twohalf-v121.py —
ref-arbit-v121.sh + clone-arbit-v121.sh, the ONE census JS block
[CENSUS_JS 193 lines] byte-identical across the halves, the md5
line-block contract [b55dcd29 — the v97/v103/v109/v115 census blocks
VERBATIM]; the STALE clonearbit109 SESSION TOKEN in the v115 builder's
clone_login FIXED to clonearbit121 in this lineage — the same quirk
class as the v114 builder's clonearbit108 fixed in the v120 lineage).
**The verdict pass 1 BOTH PAIRS DIFFERENT / pass 2 INCOME IDENTICAL +
EXPENSES DIFFERENT — the pair's documented verdict classes (the same
split as v109/v115; v103 read BOTH DIFFERENT; the income side's
documented flags all-data classes, so the IDENTICAL verdict on pass 2
the cleaner outcome on the same chrome — the VLM-verdict variation
form, the v105 LOGIN-IDENTICAL precedent)** — every flag
DOM-arbitrated: the payment chips the v57 DATA-CONDITIONAL class (the
reference's own income card footer childCount 2 with the Bank Account
chip — it RENDERS payment chips when data carries them); the badge
wrap the v57 wrap/classification-VALUE classes (badgeRow h 22-vs-52,
badgeCount 3-vs-4 — the Recurring superset chip + the wrap, the chip
chrome byte-identical); the "Edit with Base44" widget the
platform-chrome class DISPROVEN LIVE (the INVERTED reading this cycle
— the VLM claimed the widget present in the CLONE: base44-fab-arbit-
v121.sh measured fabCount 0 + bodyHasBase44 false on BOTH sides at
1280 /expenses — the overlay lives in the reference's platform iframe
chrome); the avatar the user-identity class; the figures the seed-data
classes. The both-sides census compared AXIS-BY-AXIS by the persisted
compare-v121-census.py: **187 axes — 163 identical + 24
documented-class deltas, ZERO new** (the v115 values reproduced
EXACTLY, the same 187/163/24 split — the avatar chrome, the grid +
card chrome [the 3-col 309.328px family], the titleRow, the amount
leaf, the footer + badge chrome, the filter card on BOTH variants,
the page-header family, the docSW 1280 guards). NO NEW CLONE GAP.

**F4 the pin — the ITEM-CARD's inline CONFIRM-BAR census at 1280 (the
never-pinned twin of the pinned family, PIN-ONLY — the v120
LIABILITY-TWIN precedent form)**: the FIRST candidate (the expenses
filter's md-band state at 800 — measured BYTE-IDENTICAL on both sides
by the one-shot census expband-arbit-v121.sh: the inner grid cols
207px 207px + the not-spanning search wrapper w 207 + the 3 comboboxes
207/36/14px + the card 480/138/mb 24 + the docSW 800, both census JSON
lines the IDENTICAL string) **REJECTED by the LIVE SOLE-FAILURE TEST**
(the v116 first-attempt precedent, the SPEC-ALIAS COVERAGE lesson
re-hit: the v1-era items.spec.ts:622 asserts the RAW `md:grid-cols-2`
CLASS TOKEN itself — the line-175 mutation reds both the new pin AND
the old spec; the re-scope analysis found NO alternative sole-failure
axis on the family: the gap-4 token -> the v70 pin's innerGrid.gap at
1280, the lg:grid-cols-4 token -> the 622 token + the v70 cols, the
wrapper col-span -> the v70 searchW, the shared card lines -> the
v64/v70/v115 pins). The candidate the ITEM-CARD's inline confirm bar
(the income/savings cards' "Delete this item?" bar): the confirm-bar
FAMILY pinned ONLY on the /networth instances (the v46 F3 pin — the
asset card's bar), the ITEM-CARD instance held by NO spec (every
existing confirm-bar assertion in the items specs BEHAVIORAL only —
the text visibility, the click paths, the failed-delete toast); the
reference has NO confirm bars at all (its card-menu Delete destroys
immediately — its R6 bug), so no both-sides census is possible (the
v46 F3 adapted form); the family chrome = the v46 F3 contract BY
CONSTRUCTION (the identical class strings: item-card.tsx:210 <->
net-worth-view.tsx:124/235). The one-shot clone census
(confirmbar-arbit-v121.sh — the full PointerEvent/MouseEvent sequence
for the Radix menu [the v120 TAB-SWITCH lesson applied to the
dropdown], the FIXTURE-RESTORE Cancel — the delete never fired, the
card restored to its at-rest 230) measured: the bar {mt 16px / display
flex / align center / justify space-between / radius 8px / pad 12px /
bg rgb(254,242,242) / w 267 — the pinned card 309 - the 40 p-5 - the
2px border}, the label {fs 14px / fw 400 / the item-card-only text
"Delete this item?"}, the cancelPill {bg white / pad 4px 12px /
radius 6px / fs 12px / fw 500 / h 24 / the shadow-sm VISIBLE layer
rgba(0,0,0,0.05) 0px 1px 2px 0px — the regression net's SIXTH site},
the deleteBtn {color white / pad 4px 12px / radius 6px / fs 12px /
fw 500 / h 24}, the BAR-OPEN DELTA +80 (the at-rest 230 -> the
bar-open 310 = the mt 16 + the bar 64, THE ARITHMETIC EXACT — the
data-independent chrome delta); the colors (the label red-700 / the
delete bg red-600) deliberately NOT asserted (the lab() named-palette
drift — the v46 F3 family form, the engine-independence discipline).
The +1 e2e pin (tests/e2e/items.spec.ts, appended by the persisted
append-pin-v121.py): the confirm-bar census at 1280 — the family + the
delta + the fixture-restore Cancel, the finders STRUCTURAL (the v46 F3
finder family: the bg + the Cancel/Delete button pair); the PIN-ONLY
form (the standalone GREEN 47/47 — the first run's 622 red the STALE
mutated standalone, the v98 REBUILD discipline + THE PIN-SANITY
MUTATION [item-card.tsx:210 the bar's p-3 -> p-4, LINE-SCOPED — the
SOLE FAILURE VERIFIED LIVE: the v121 pin ALONE red, bar.pad 12px ->
16px the primary axis + the co-moving delta 80 -> 88, the full items +
networth run 81 GREEN including the v46 F3 networth twin — the
different-file immunity verified live; restored + the full rebuild +
the 47/47 post-restore regression]).

**F5 the ship chain**: lint · typecheck · 108 unit · 0 vulnerabilities ·
**324 e2e zero flakes** (87+81+77+82 = 327 executions = 324 unique) ·
35/35 smoke. **The screenshots 16/16 byte-IDENTICAL (the same-day-seed
law — the seed and the capture ran the same day, the relative dates
matching)**; the dev evidence 4/4 byte-identical + VLM-verified (the
menu proof: /income, docSW 390, navLandmark true; the menu open with
all 5 links + the brand; the sheet closed post-nav; the dashboard
clean — the dev-shots scripts derived v120->v121 with the
version-swap-only verification).

The v122 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v115-era ITEMS pair (the v116-era SAVINGS pair — the SAVINGS
view at desktop 1280x800 FULL-PAGE, the v58-era savings pair's surface
family, last re-shot v116 — now the oldest remaining [v116 < v117 <
v118 < v119 < v120 < v121]; the pair's TENTH re-run bracket [v58 -> v65
-> v74 -> v80 -> v86 -> v92 -> v98 -> v104 -> v110 -> v116 -> v122] to
be verified against vlm-shots-v116.sh's own header before the
derivation — the v116 header's own NINTH ordinal should be consistent
with its 10-entry bracket [v58 the original], so v122 = the TENTH
re-run by the same convention), (2) the axe-core watch at its next
re-check point (only a 5.x wrapper changes the calculus), (3) the
npm-audit watch at its re-check point (only a new advisory in the
next/zod ranges changes the calculus), (4) the deferred reference-write
censuses (unchanged — out of bounds under the v46 read-only rule).

## The v120 cycle (the v114-era MOBILE TWINS pair's NINTH re-run — Session 155)

The re-run cadence's next-oldest candidate: the v114-era MOBILE TWINS
pair — BOTH mobile 390x844 full-page twins: (1) the /NETWORTH view (the
v63-era pair's surface) and (2) the DASHBOARD (the v62-era mobile twin's
surface), last re-shot v114 — now the oldest remaining [v114 < v115 <
v116 < v117 < v118 < v119]; the pair's NINTH re-run bracket [v62/v63 ->
v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120]; the
FORTY-THIRD consecutive queue/ledger agreement — the surface names
verified against vlm-shots-v114.sh's own header BEFORE the derivation,
with the v114 header's own EIGHTH ordinal CONSISTENT with its 9-entry
bracket [v62/v63 the original pair — no off-by-one this lineage, unlike
the v113 lineage's SEVENTH-vs-bracket]. **A PIN-ONLY cycle for src/ —
zero production-code changes** + one e2e pin; the cycle's standing
items: the axe watch (NO DRIFT — 4.14.0 holds, only the canary sha
prerelease beyond, the v68 dedupe verified), the npm-audit watch at its
eleventh re-check (0 vulnerabilities — the v110 bump holds [next
16.4.3 + zod 4.6.7]), the 114th standing checks (ALL GREEN — the mobile
menu the 114th consecutive green; the reference's four bugs all live;
the data census clean on the FIRST reads, no render-race hit this
cycle).

**F0 baseline FULLY GREEN on the PERSISTED workspace** (the first
PERSISTED-class cycle in the recent ledger — the v119 environment
survived between the cycles: node_modules 354 entries, the db at
<repo>/db/custom.db, BOTH playwright v1243 binary pairs in the cache;
only the git pull needed for the session_291.md handoff [0455e0e ->
a060896, session-log-only]). The seedcheck exact (7/1850/2235/0/3/2)
before any gate; the gates: lint · typecheck · 108/108 unit · build
(robots + sitemap prerendered) · **322 e2e ZERO FLAKES** (86+80+77+82 =
325 executions = 322 unique, every chunk green on its FIRST run) ·
35/35 smoke. The post-push commits audited session-log-only.

**F2 the 114th standing checks ALL GREEN** (the pair derived from the
v113 pair via the persisted derive-standing-v120.py — three token
families, normalize-back diff clean, zero old tokens): the reference's
four bugs all live [toast-blocker hitIsBurgerChild:false; sheet-trap
overlayCount:1 after nav; no-landmark navLandmark:false; the 464px
/networth overflow measured docSW 464 directly]; the data census clean
on the FIRST reads; the SEO pair live both sides; the clone's mobile
menu VERIFIED WORKING the 114th consecutive time (zero overflow at 390
on all five views); the seedcheck exact after the clone half.

**F3 the re-run pair**: the probe series derived from the v114 lineage
(the persisted derive-v120-series.py — the generic swaps + FIVE
exact-fragment history corrections, 5/5 applied on the FIRST run, line
counts preserved 61/48/69/220); the census BUILT two-half from the
start (build-twohalf-v120.py — ref-arbit-v120.sh + clone-arbit-v120.sh,
the TWO census JS blocks [NW_CENSUS 42 + DASH_CENSUS 87 lines]
byte-identical across the halves, the md5 line-block contracts
[82cf8a43 / 85e4ec7e — the v102/v108/v114 census blocks VERBATIM]; the
STALE clonearbit108 SESSION TOKEN in the v114 builder's clone_login
FIXED to clonearbit120 in this lineage — the v114 derivation had
inherited the v108 token unbumped). **The verdict BOTH PAIRS DIFFERENT
— the pair's documented verdict class (the same verdict family as the
v84/v90/v96/v102/v108/v114 re-runs)** — every flag DOM-arbitrated: the
NETWORTH stat-tiles stacking + card height the v41 mobile-superset
class (census-confirmed: statGrid.cols 2-col-vs-1-col, tiles
176-vs-294, card 432x333-vs-358x421, medallion clipsViewport
true-vs-false); the trend-icon circle the PERCEPTION-ARTIFACT class
(the census axis trendIcon 32x32 BYTE-IDENTICAL both sides + the
medallion 64x64 identical — the VLM's own contradictory descriptions
across the two passes the disproof); the card grouping/figures the
SEED-DATA classes; the Base44 overlay the PLATFORM-CHROME class
DISPROVEN LIVE at BOTH flagged surfaces (base44-fab-arbit-v120.sh:
fabCount 0 + bodyHasBase44 false on BOTH sides at BOTH surfaces — the
overlay lives in the reference's platform iframe chrome); the progress
bar/donut/labels the SEED-DATA classes; the subtitle wrap the RANGE-
WALK line bucketing (the DASH width-guard class's documented
consequence: the ref's 363px-vs-clone's 358px content width buckets the
same text differently; the line TOPS identical 123/147, the computed
chrome identical). The census compared AXIS-BY-AXIS by the persisted
compare-v120-census.py: **55 axes — 37 identical + 18 documented-class
deltas, ZERO new** (the v41 mobile-superset family + the DASH
width-guard family + the Range-walk line texts) — reproducing the v114
census values EXACTLY (the same 55/37/18 split), zero drift on every
axis.

**F4 THE PIN — the /networth LIABILITY-CARD census at 390 (the
never-pinned family, PIN-ONLY — the FAMILY-CONSISTENCY form, the v29
G1 precedent)**: the twins' own surfaces among the most-pinned in the
codebase (the rejected candidates documented with the collision
evidence — the section-row/facts-row/spending-header 390 twins the
v94/v106/v101 1280 collisions [the v114 rejections standing]; the
640-band form REJECTED [dashboard-view carries ZERO sm: variants — the
640 rendering = the 390 rendering for every family, any 640 pin either
duplicates the 390 values cascading to the 390 pin or the aggregate
band state already pinned by the v42 F2/F3 censuses]; the empty-state
REJECTED [the clone seeds 2 liabilities]); the candidate the /networth
view's LIABILITY CARD family — NEVER pinned at ANY viewport (only the
v29 G1 badge family-consistency pin + the interest-line TEXT existence
+ the group headers + the Add Liability gradient; the ASSET twin fully
pinned v46/v47/v106). The FAMILY-CONSISTENCY form: the reference's own
liability data is EMPTY (0 liabilities — no cards to measure; the v46
read-only rule forbids writing reference data), the chrome family =
the AssetCard's pinned contract BY CONSTRUCTION (net-worth-view.tsx:169
the identical class strings to :65; the v46 F1 liability-twin fix's
own comment documents the shared mb-4 P + space-y-2 facts stack). The
one-shot census (liabcard-arbit-v120.sh — the RADIX TAB-SWITCH LESSON
baked in: the tabs activate on pointerdown, the bare el.click() leaves
the tab inactive, the full PointerEvent/MouseEvent sequence the fix)
measured the family: the card {358x218 — the asset's pinned 194 + the
third facts row's 16 + the space-y-2's 8, THE ARITHMETIC EXACT /
radius 12px / pad 20px / border / shadow / transition all the v47
contract}, the head row {mb 12 / flex / flex-start / space-between /
h 52}, the dot {8x8 / 9999px / the LIABILITY_COLOR orange
rgb(224,122,59)}, the h4 {16px/600/forestDark}, the badge {the v29 G1
family}, the value P {24px/700/the orange/mb 16px — the v46 F1
liability twin}, the facts {12px/gray/rowGap 8px/rowCount 3 — the
liability-ONLY axis: institution + interest + updated vs the asset's 2
rows}, the three rows {flex/center/gap 8px/h 16/icon 12x12}, the
valueToFactsGap 16, the docSW 390. The +1 e2e pin
(tests/e2e/networth.spec.ts, appended by the persisted
append-pin-v120.py): the family census + the docSW guard, the finders
STRUCTURAL, the tab switch by Playwright's locator click (the full
pointer sequence — the census lesson encoded in the spec form); the
PIN-ONLY form (the standalone GREEN run + THE PIN-SANITY MUTATION
[net-worth-view.tsx:223 the interest row's gap-2 -> gap-3, LINE-SCOPED
— the pin FAILED at rows[1].gap ALONE, 8px -> 12px, every other axis
green; the 6 other same-class lines untouched; restored + the full
rebuild + the 36/36 post-restore networth regression]).

**F5 the ship chain**: lint · typecheck · 108 unit · 0 vulnerabilities ·
**323 e2e zero flakes** (87+80+77+82 = 326 executions = 323 unique) ·
35/35 smoke. **The screenshots 16/16 byte-IDENTICAL (the same-day-seed
law — the seed and the capture ran the same day, the relative dates
matching)**; the dev evidence 4/4 byte-identical + VLM-verified (the
menu proof: /income, docSW 390, navLandmark true; the menu open with
all 5 links + the brand; the sheet closed post-nav; the dashboard
clean — the dev-shots scripts derived v119->v120 with the
version-swap-only verification). The v119-RESIDUAL AGENTS.md
DUPLICATION FIXED this cycle (the v119 paragraph's tail carried the
workspace-class sentence 3 EXTRA times — a latent v119-cycle defect,
the duplicates removed in the docs alignment D0).

The v121 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v114-era MOBILE TWINS pair (the v115-era ITEMS pair — the
ITEMS view (income + expenses) at desktop 1280x800 FULL-PAGE, the
v57-era items pair's surface family, last re-shot v115 — now the oldest
remaining [v115 < v116 < v117 < v118 < v119 < v120]; the pair's TENTH
re-run bracket [v57 -> v64 -> v70 -> v79 -> v85 -> v91 -> v97 -> v103
-> v109 -> v115 -> v121] to be verified against vlm-shots-v115.sh's own
header before the derivation — the v115 header's own NINTH ordinal is
consistent with its 10-entry bracket [v57 the original], so v121 = the
TENTH re-run by the same convention), (2) the axe-core watch at its next
re-check point (only a 5.x wrapper changes the calculus), (3) the
npm-audit watch at its re-check point (only a new advisory in the
next/zod ranges changes the calculus), (4) the deferred reference-write
censuses (unchanged — out of bounds under the v46 read-only rule).

## The v119 cycle (the v113-era DASHBOARD pair's NINTH re-run — Session 154)

The re-run cadence's next-oldest candidate: the v113-era DASHBOARD pair
(the DASHBOARD at desktop 1280x800 FULL-PAGE, both v61 target surfaces
below the fold on the same view: (1) the BUDGET GUIDELINES card (the
tinted, bordered 50/30/20 rows) and (2) the QUICK-ACTION card row (the
three Add Income / Add Savings / Add Expense card buttons), last re-shot
v113 — now the oldest remaining [v113 < v114 < v115 < v116 < v117 <
v118]; the pair's NINTH re-run bracket [v61 -> v68 -> v77 -> v83 -> v89
-> v95 -> v101 -> v107 -> v113 -> v119]; the FORTY-SECOND consecutive
queue/ledger agreement — the surface names verified against
vlm-shots-v113.sh's own header BEFORE the derivation, with the v113
header's own SEVENTH-vs-bracket off-by-one identified BEFORE the
derivation and the NINTH ordinal fixed IN it [the consistent v112-lineage
convention: EIGHTH for 9 entries, NINTH for 10 — v61 the original in
every bracket; the BRACKET is the authority per the queue-prose
verification lesson]). **A PIN-ONLY cycle for src/ — zero
production-code changes** + one e2e pin; the cycle's standing items: the
axe watch (NO DRIFT — 4.14.0 holds, only a canary sha prerelease beyond,
the v68 dedupe verified), the npm-audit watch at its tenth re-check (0
vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]), the
113th standing checks (ALL GREEN — the mobile menu the 113th consecutive
green; the reference's four bugs all live; the data census clean on the
FIRST reads, no render-race hit this cycle).

**F0 baseline FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace**
(the RESET class — the v118 environment did not persist; the repo
re-cloned from main @ ec146b5). The v108 FRESH-CLONE lesson applied
END-TO-END: npm ci (354 entries; the first BACKGROUND attempt died
SILENTLY with an empty log — the v114 silent-death lesson's exact
symptom — the run redone in the FOREGROUND) with the zod extraction
verified INTACT [840/840 files by the total-file count, the src/v4
subdirectory present, one package-lock zod entry — the v68 dedupe];
BOTH v1243 playwright binaries verified DIRECTLY (the fresh cache held
only the OLD chromium-1200 pair; the v1243 layout the
chrome-linux64/chrome + chrome-headless-shell-linux64/chrome-headless-shell
pair, INSTALLATION_COMPLETE markers + direct binary reads). **The
fresh-workspace discovery**: the sandbox's workspace root carries its
own /home/z/my-project/.env with an ABSOLUTE
DATABASE_URL=file:/home/z/my-project/db/custom.db — the Prisma CLI
walks PARENT directories for .env files and the parent's absolute URL
WON over the repo's file:../db/custom.db (the first db push wrote
OUTSIDE the repo). THE FIX (the discipline for every fresh workspace):
the EXPLICIT env prefix on every Prisma CLI call
(DATABASE_URL="file:../db/custom.db" npx prisma db push / ... npm run
db:seed) — the explicit shell env beats any .env file; the app itself
unaffected (Next.js loads the repo .env only + db-path.ts anchors the
relative URL against the repo root regardless of CWD). The db verified
at <repo>/db/custom.db + the seed (7 items / 3 assets / 2 liabilities);
the seedcheck exact (7/1850/2235/0/3/2). The gates: lint · typecheck ·
108/108 unit · build (robots + sitemap prerendered) · **321 e2e ZERO
FLAKES** (85+80+77+82 = 324 executions = 321 unique) · 35/35 smoke.
NOTE the a11y-filename grep lesson re-hit: a `[a-z-]+\.spec\.ts` grep
pattern truncated "a11y.spec.ts" to "y.spec.ts" (the digit class
missing) — the first chunk-4 run executed 60 of 82 before the filename
check caught it; the re-run with the REAL filename green (the v111
lesson: verify the filename list against `--list` before running). The
post-push commits since the v118 parity push (d14d56f) audited
session-log-only [d48fabd adds docs/session_287.md + ec146b5 adds
docs/session_288.md — ZERO src/, tests/, prisma/ or lockfile deltas].

**F3**: the series derived from the v113 lineage (derive-v119-series.py
— the generic swaps + the EIGHT exact-fragment history corrections
[the era re-pointed v107-era -> v113-era, last-re-shot v107 -> v113,
the oldest-remaining list re-pointed, the ordinal off-by-one FIXED
SEVENTH/EIGHTH -> NINTH + the bracket extension -> v113 -> v119, the
agreement THIRTY-SIXTH -> FORTY-SECOND, the re-proves window
v101-v107 -> v101-v113, the verdict reference "The v107" -> "The v113",
the drift-re-check "since v107" -> "since v113", and the compare PAIR
banner], 8/8 applied on the second run — the first run's single MISS
the arbit header fragment written from the line-START where the file
carries it MID-LINE after "# 1280x800 (the..."; line counts preserved
[58/43/46/259]). The census BUILT two-half from the start
(build-twohalf-v119.py via derive-build-twohalf-v119.py with the
swap-order rule [generic swap FIRST, the lesson-range bump
v92..v112 -> v92..v118 — the BARE-RANGE form: the v113 builder's
TWOHALF_NOTE carries the range SPLIT ACROSS TWO LINES and the
v118-template phrase-form swap missed it, the bare-range swap catches
both occurrences; the lineage-note fixup "build-twohalf-v107.py" ->
"build-twohalf-v113.py" LAST]; the THREE census JS blocks [ARBIT_G 61
lines + ARBIT_Q 58 lines + ARBIT_X 25 lines] byte-identical across the
halves — the md5 line-block contracts [b500dd29 / da04e995 / 7a381755 —
the v101/v107/v113 census blocks VERBATIM, verified by marker-based
extraction across the source + both halves]). Both halves executed
cleanly (the reaping budget between halves; the parked pointer at
(5,5); read-only — the v46 rule holds; login on the first attempt both
sides).

**The verdict: IDENTICAL — the SEVENTH consecutive IDENTICAL verdict
for this pair [v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119]** —
run TWICE with the full log captured; the only flags the documented
classes: the nav highlight the v56 SUPERSET delta (the clone highlights
its ACTIVE nav item; the reference's own shortcoming); the avatar
letters the USER-IDENTITY data class; the figures the SEED-DATA classes
(each site's own data). No FAB flag raised this cycle (the v103
standing class: either form without surprise — no disproof needed when
no flag is raised). The both-sides census compared AXIS-BY-AXIS by the
persisted compare-v119-census.py (**154 axes: 144 identical + 10
documented-class deltas, ZERO new** — Gcard.shadow the v66 INVISIBLE
shadow-lead class; Qcards[i].label.color/.fw the v61 label-wrapper
lesson [the census finder catches the clone's WRAPPER 400/rgb(10,10,10)
while the ref's is the leaf — the clone's LEAF span byte-identical
16px/500/rgb(26,58,46), pinned green by the v61 F3 pin + the v107 F4
label-leaf census]; Qgrid.mt + XgridMt the v77 mechanism class
[explicit mt-8 on the clone vs structural spacing on the ref]; XgridCls
the site-source class) — reproducing the v113 census values EXACTLY
(the same 154/144/10 split), zero drift on every axis, the rendered
geometry HARD-ASSERTED byte-identical (cardBottom 1122 / gridTop 1462 /
gap 340 / gridParentMt 0px on BOTH sides).

**F4 [PIN] — the /dashboard PAGE-HEADER-ROW census at 1280 (the
never-pinned family, PIN-ONLY — the cleanest form)**: the pin-candidate
survey found the pair's own below-the-fold surfaces among the
most-pinned in the codebase (the guidelines card: v61 F2 + v77 F4 + v89
F4 + v101 F4 + v113 F4; the quick-action row: v61 F3 + v45 F3b + v83 F4
+ v89 F4 + v95 F4 + v107 F4 — every PART G/Q/X census axis family
pinned), so the candidate went to the SAME VIEW's never-pinned family
per the v118 precedent: **the DASHBOARD PAGE-HEADER ROW at 1280** — the
family pinned ONLY at 390 before this (the v114 F4 pin: the row's flex
chrome + the block->button junction + the Add Item button's box chrome;
the v62 F2 pin: the subtitle block's interior) and at 1280 only
POSITION-pinned (the v40 F1 Tab-order census: the Add Item button's
band [x 1121, w 127, h 36]; the session-5 gradient; the v35 S2 focus
shadow; the G3 Plus-icon geometry). The one-shot both-sides census
(drow-arbit-v119.sh — the census JS defined ONCE and eval'd on BOTH
sides, byte-identical by construction): **the family BYTE-IDENTICAL on
EVERY axis — not even a mechanism axis diverged** (the reference's and
the clone's census JSON lines the IDENTICAL string): the row {display
flex / flexDirection row / align center / justify space-between / gap
16px / mb 32px / h 72 / w 960}, the h1 {fs 36px — the md:text-4xl tier,
the 390 twin's text-3xl 30px the OTHER breakpoint / fw 700 / lh 40px /
color rgb(26,58,46) / h 40 / mb 8px}, the subtitle {fs 16px / fw 400 /
lh 24px / color rgb(107,114,128) / h 24}, the block {h 72 / w 498 /
right 786}, the addBtn {left 1121 / top 50 / h 36 / w 127 / pad 8px
16px / radius 6px / fs 14px / fw 500 / color white / bg the 135deg
forest->lime gradient / icon 16x16}, the junction {hGap 335 — the
justify-between SPREAD, the row's gap-4 16px the computed minimum}, the
nextGap {gap 32 — the mb-8 rendered, the next sibling the
lg:grid-cols-3 stat grid}, the docSW 1280 — the Add Item button's band
CROSS-VALIDATED against the v40 F1 pin's own [1121, 127, 36] exactly.

**THE CLASSIFICATION — PIN-ONLY (the cleanest form)**: no construct
question even arises this cycle (unlike the v118 wrapper find) — the
family is byte-identical on every axis INCLUDING the positions. The pin
locks the never-pinned 1280 family's computed chrome as the desktop
twin of the v114 390 pin.

The pin (tests/e2e/dashboard.spec.ts, the v119 describe block —
appended by the persisted append-pin-v119.py): the /dashboard
page-header row census at 1280x800 — the row {display flex /
flexDirection row / align center / justify space-between / gap 16px /
mb 32px} + the h1 {fs 36px / fw 700 / lh 40px / mb 8px — the
md:text-4xl tier} + the subtitle {fs 16px / fw 400 / lh 24px} + the
block {h 72 / w 498 — the TEXT BLOCK governs the row height, the
v65/v69/v118 lesson} + the addBtn BOX chrome {h 36 / w 127 / pad 8px
16px / radius 6px / fs 14px / fw 500 / color white / bg the 135deg
gradient / icon 16x16 — the v114 390 pin's desktop twin, the band
cross-validating the v40 F1 pin} + the horizontal junction (the block's
right -> the button's left, the justify-between spread — data-stable
via the fixed strings) + the row->stat-grid rhythm (the nextGap 32) +
the docSW 1280 guard; the finders STRUCTURAL (the h1 by its childless
exact text "Budget Dashboard"; the block as its parent; the row as the
block's parent; the button by its /Add Item/ text within the row; the
next sibling as the row's nextElementSibling). The PIN-ONLY form (the
v116/v118 precedent): the pin written asserting the measured clone
values -> the standalone GREEN run (no red phase — nothing to fix, the
values already hold) -> the 48/48 dashboard surface regression -> the
full-suite ship chain.

**F5 the ship chain**: lint · typecheck · 108 unit · 0 vulnerabilities ·
**322 e2e zero flakes** (86+80+77+82 = 325 executions = 322 unique) ·
35/35 smoke. **The screenshots 16/16 byte-IDENTICAL (the same-day-seed
law — the seed and the capture ran the same day, the relative dates
matching)**; the dev evidence 4/4 byte-identical + VLM-verified (the
menu proof: /income, docSW 390, navLandmark true; the menu open with
all 5 links + the brand; the sheet closed post-nav; the dashboard
clean — the dev-shots scripts derived v118->v119 with the
version-swap-only verification).

The v120 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v113-era DASHBOARD pair (the v114-era MOBILE TWINS pair —
BOTH mobile 390x844 full-page twins: (1) the /NETWORTH view (the
v63-era pair's surface) and (2) the DASHBOARD (the v62-era mobile
twin's surface), last re-shot v114 — now the oldest remaining [v114 <
v115 < v116 < v117 < v118 < v119]; the pair's next re-run bracket
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 ->
v120] to be verified against vlm-shots-v114.sh's own header before the
derivation — the v114 header's own EIGHTH ordinal is consistent with
its 9-entry bracket [v62/v63 the original pair], so v120 = the NINTH
re-run by the same convention), (2) the axe-core watch at its next
re-check point (only a 5.x wrapper changes the calculus), (3) the
npm-audit watch at its re-check point (only a new advisory in the
next/zod ranges changes the calculus), (4) the deferred reference-write
censuses (unchanged — out of bounds under the v46 read-only rule).

## The v118 cycle (the v112-era NETWORTH + drill-down-DASHBOARD pair's NINTH re-run — Session 153)

The re-run cadence's next-oldest candidate: the v112-era NETWORTH +
drill-down-DASHBOARD pair (the desktop 1280x800 FULL-PAGE state of
(1) the NETWORTH view and (2) the DASHBOARD's drill-down EXPANDED
state, last re-shot v112 — now the oldest remaining [v112 < v113 <
v114 < v115 < v116 < v117]; the pair's NINTH re-run bracket [v60 -> v67
-> v76 -> v82 -> v88 -> v94 -> v100 -> v106 -> v112 -> v118]; the
FORTY-FIRST consecutive queue/ledger agreement — the surface names
verified against vlm-shots-v112.sh's own header BEFORE the derivation).
**A PIN-ONLY cycle for src/ — zero production-code changes** + one e2e
pin; the cycle's standing items: the axe watch (NO DRIFT — 4.14.0
holds, only a canary sha prerelease beyond, the v68 dedupe verified),
the npm-audit watch at its ninth re-check (0 vulnerabilities — the
v110 bump holds [next 16.4.3 + zod 4.6.7]), the 112th standing checks
(ALL GREEN — the mobile menu the 112th consecutive green; the
reference's four bugs all live; the data census clean on the FIRST
reads, no render-race hit this cycle).

**F0 baseline FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace**
(the RESET class — the v117 environment did not persist; the repo
re-cloned from main @ dba644d). The v108 FRESH-CLONE lesson applied
END-TO-END: npm ci (run in the foreground — the v114 silent-death
lesson; 354 entries) with the zod extraction verified INTACT [840/840
files by the total-file count, the src/v4 subdirectory present,
verified BEFORE any gate; one package-lock zod entry — the v68
dedupe]; .env [DATABASE_URL="file:../db/custom.db"] + db/ at the repo
root; db:push + db:seed (7 items / 3 assets / 2 liabilities); BOTH
v1243 playwright binaries verified DIRECTLY (the fresh cache held only
the OLD chromium-1200 pair). The gates: seedcheck exact
(7/1850/2235/0/3/2) · lint · typecheck · 108/108 unit · build (robots +
sitemap prerendered) · **320 e2e ZERO FLAKES** (84+80+77+82 = 323
executions = 320 unique — every chunk green on its FIRST run) · 35/35
smoke. The post-push commit since the v117 parity push (0f657e9)
audited session-log-only [dba644d adds docs/session_285.md — ZERO
src/, tests/, prisma/ or lockfile deltas].

**F3**: the series derived from the v112 lineage (derive-v118-series.py
— the generic swaps + the FOUR exact-fragment history corrections, 4/4
applied on the FIRST run; line counts preserved [84/71/65/328]). The
census BUILT two-half from the start (build-twohalf-v118.py via
derive-build-twohalf-v118.py with the swap-order rule [generic swap
FIRST, the lesson-range bump v92..v111 -> v92..v117, the lineage-note
fixup "the v106-lineage derivation" -> "the v112-lineage derivation"
LAST]; ZERO builder repairs needed this cycle; the TWO census JS
blocks [ARBIT_A 90 lines + ARBIT_B 111 lines] byte-identical across
the halves — the md5 line-block contracts [45b9a439 / 8ed66a88,
verified by marker-based extraction across the source + both halves]).
Both halves executed cleanly (the reaping budget between halves; the
parked pointer at (5,5); read-only — the v46 rule holds; the
drill-down expansion clicks mutate no data; login on the first attempt
both sides).

**The verdicts: NETWORTH DIFFERENT + drill-down DIFFERENT — every flag
DOM-arbitrated to a documented class**: the FAB flags (raised on BOTH
pairs) DISPROVEN live (base44-fab-arbit-v118.sh on the flagged
/networth surface at 1280: fabCount 0 + bodyHasBase44 false on BOTH
sides — the platform-iframe chrome class, the standing disproof form
re-confirmed); the avatar letters the USER-IDENTITY data class; the
nav-highlight flag the v56 SUPERSET delta + perception (the census: bg
rgba(0,0,0,0) transparent on BOTH sides — no green background; the
color/fw asymmetry the documented superset); the hero progress % the
PCT data class (fillW 173-vs-357); the donut % labels the
EACH-SITE'S-DATA + perception class (count 4 / labelFs 16px / sectors
3 byte-identical — the reference DOES render its labels); the stat
counts / the extra category the SEED-DATA class; **the "Total Expense
(singular) vs Total Expenses (plural)" flag DISPROVEN live — the
reference reads "Total Expenses" PLURAL on ALL SIX instances (the 3
tab-button SPANs + the 3 stat-card H3s), the full family byte-identical
to the clone's down to every chrome axis (statlabel-explore-v118.sh +
statlabel-explore-clone-v118.sh) — the VLM TEXT-MISREAD class**. The
both-sides census compared AXIS-BY-AXIS by the persisted
compare-v118-census.py (**73 axes: 67 identical + 6 documented-class
deltas, ZERO new** — navHighlight.color/fw the v56 superset delta;
avatarLetter the user-identity data class; progress.fillW the pct data
class; donutLabels.texts the each-site's-data class; labelBlock.w the
v82 DATA-CONDITIONAL width class [the 48px figure's text length]) —
reproducing the v106/v112 census values EXACTLY, zero drift on every
axis. NOTE: the census lines are DOUBLE-ESCAPED in the halves' logs
(agent-browser prints the JSON object itself serialized as a quoted
string — structural quotes escaped once, nested quotes inside values
like glyphSig twice); the recovery is a DOUBLE json.loads (the
compare-v118-census.py parser form).

**F4 [PIN] — THE WRAPPER-MECHANISM CONSTRUCT CLASS (the cycle's find,
PIN-ONLY)**: the pin-candidate survey targeted the /networth PAGE-HEADER
ROW at 1280 (the element family every 1280 networth census walked past:
the v60 view census jumps straight to the summary card's label; the
v67/v82 pins the card interior; the v94 the GROUP headers; the v100 the
tablist junction; the v106 the asset cards — the PAGE header row pinned
ONLY at 390 before this [the v69 F3 pin, measured on the CLONE only];
the v14 G3 test pins the chip's existence + gradient + geometry + the
h1 x-positions only). The one-shot both-sides census
(nwheader-arbit-v118.sh) measured the family BYTE-IDENTICAL on every
VISUAL axis — the row {flex/center/gap 12px/h 60}, the chip {48x48 /
radius 12px / the 135deg forest->lime gradient / the 24x24 svg}, the h1
{30px/700/36px/rgb(26,58,46)}, the subtitle {16px/400/24px/
rgb(107,114,128)}, the block {h 60 / w 250}, the row->card gap 32, the
card w 960 — with ONE mechanism axis diverging: the row's margin-bottom
(the reference 0px vs the clone 32px). The drill-down
(nwheader-mechanism-v118.sh + nwheader-wrapper-v118.sh, both sides):
**the reference wraps its header row in a SINGLE-CHILD responsive
wrapper** (`flex flex-col md:flex-row justify-between items-start
md:items-center gap-4 mb-8` — the wrapper carries the mb-8 = 32px; the
row itself bare) while the clone puts the mb-8 directly on the row (no
wrapper). The wrapper's census: childCount 1 — the chip+title row alone
(w 310, right 682, NOTHING on the right); justify-between has no second
child to spread. ZERO visual consequence: the pixel arithmetic
identical both sides (the row top 32 / bottom 92, the card top 124, the
gap 32), the 390 rhythm matching too (the v69 pin's gap 32 = the
reference's wrapper mb 32). Notably the clone's OWN dashboard header
uses the reference's wrapper form verbatim (dashboard-view.tsx:927) —
the /networth header is the v14-era simplification, predating the
wrapper's discovery. **THE CLASSIFICATION — the CONSTRUCT class per the
v7 accepted-construct convention (constructs that paint nothing are not
parity axes)**: the single-child wrapper paints nothing, organizes
only — its computed effect is exactly {mb 32}, which the clone achieves
on the row itself; the DOM-tree shape is not the contract (the v72
structural-finder principle). The production-code changes remain
reserved for REAL visual deltas (the six since v46 — all visual).

**THE LESSON (formalized): a STRUCTURAL-layer difference with zero
computed-style consequence on every visible axis is a CONSTRUCT class,
not a parity gap — measure the MECHANISM (which element carries the
margin/gap) before flagging it, and pin the VISUAL contract (the
geometry the user sees), not the mechanism axis. The corollary: when a
census axis diverges, first compute whether ANY pixel the user can see
differs (the position arithmetic: tops/bottoms/gaps of the elements
AROUND the axis); if the arithmetic is identical, the axis is a
mechanism axis — document the class, do not touch src/.**

The pin (tests/e2e/networth.spec.ts, the v118 describe block —
appended by the persisted append-pin-v118.py): the /networth
page-header row census at 1280x800 — the row {display flex / alignItems
center / gap 12px / mb 32px — the clone's own rhythm, the reference's
living on its wrapper: the construct class documented in the pin's
comment} + the chip {48x48 / radius 12px / the 135deg gradient} + the
h1 {30px/700/lh 36px} + the subtitle {16px/400/lh 24px} + the block {h
60 / w 250 — the TEXT BLOCK governs the row height, the v65/v69
lesson} + the row->card gap 32 + the card w 960 context + the docSW
1280 guard; the finders STRUCTURAL (the h1 by its text; the block as
its parent; the row as the block's parent; the chip as the row's
svg-carrying child; the card via the "Total Net Worth" label walk-up —
the v60 finder). The PIN-ONLY form (the v116 precedent): the pin
written asserting the measured clone values -> the standalone GREEN run
(no red phase — nothing to fix, the values already hold) -> the 35/35
networth surface regression -> the full-suite ship chain.

**F5 the ship chain**: lint · typecheck · 108 unit · 0 vulnerabilities ·
**321 e2e zero flakes** (85+80+77+82 = 324 executions = 321 unique) ·
35/35 smoke. **The screenshots 16/16 byte-IDENTICAL (the same-day-seed
law — the seed and the capture ran the same day, the relative dates
matching)**; the dev evidence 4/4 byte-identical + VLM-verified (the
menu proof: /income, docSW 390, navLandmark true; the menu open with
all 5 links + the brand; the sheet closed post-nav; the dashboard
clean — the dev-shots scripts derived v117->v118 with the
version-swap-only verification).

The v119 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v112-era NETWORTH + drill-down-DASHBOARD pair (the v113-era
DASHBOARD pair — the DASHBOARD at desktop 1280x800 FULL-PAGE, both v61
target surfaces below the fold on the same view: (1) the BUDGET
GUIDELINES card (the tinted, bordered 50/30/20 rows) and (2) the
QUICK-ACTION card row (the three Add Income / Add Savings / Add
Expense card buttons), last re-shot v113 — now the oldest remaining
[v113 < v114 < v115 < v116 < v117 < v118]; the pair's next re-run
bracket [v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113
-> v119] to be verified against vlm-shots-v113.sh's own header before
the derivation — NOTE the v113 header's own ordinal reads SEVENTH for a
9-entry bracket, an off-by-one vs the v112-lineage convention (EIGHTH
for 9 entries); the BRACKET is the authority per the queue-prose
verification lesson, so v119 = the NINTH re-run by the consistent
convention), (2) the axe-core watch at its next re-check point (only a
5.x wrapper changes the calculus), (3) the npm-audit watch at its
re-check point (only a new advisory in the next/zod ranges changes the
calculus), (4) the deferred reference-write censuses (unchanged — out
of bounds under the v46 read-only rule).

## The v117 cycle (the v111-era LOGIN + CALCULATOR pair's NINTH re-run — Session 152)

The re-run cadence's next-oldest candidate: the v111-era LOGIN +
CALCULATOR pair (the LOGIN view + the CALCULATOR dialog at desktop
1280x800, last re-shot v111 — now the oldest remaining [v111 < v112 <
v113 < v114 < v115 < v116]; the pair's NINTH re-run bracket [v59 -> v66
-> v75 -> v81 -> v87 -> v93 -> v99 -> v105 -> v111 -> v117]; the
FORTIETH consecutive queue/ledger agreement — the surface names verified
against vlm-shots-v111.sh's own header BEFORE the derivation). **A FIX
CYCLE for src/ — the sixth production-code change since v46** (the
globals.css sm:space-y-3 restore) + one e2e pin; the cycle's standing
items: the axe watch (NO DRIFT — 4.14.0 holds, only a canary sha
prerelease beyond, the v68 dedupe verified), the npm-audit watch at its
eighth re-check (0 vulnerabilities — the v110 bump holds [next 16.4.3 +
zod 4.6.7]), the 111th standing checks (ALL GREEN — the mobile menu the
111th consecutive green; the reference's four bugs all live; the data
census clean on the FIRST reads, no render-race hit this cycle).

**F0 baseline FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace**
(the RESET class — the v116 environment did not persist; the repo
re-cloned from main @ b40d034). The v108 FRESH-CLONE lesson applied
END-TO-END: npm ci (run in the foreground — the v114 silent-death
lesson; 354 entries) with the zod extraction verified INTACT [840/840
files, the src/v4 subdirectory present, verified BEFORE any gate; one
node_modules/zod entry — the v68 dedupe]; .env
[DATABASE_URL="file:../db/custom.db"] + db/ at the repo root; db:push +
db:seed (7 items / 3 assets / 2 liabilities); BOTH v1243 playwright
binaries verified DIRECTLY (the fresh cache held only the OLD
chromium-1200 pair). The gates: seedcheck exact (7/1850/2235/0/3/2) ·
lint · typecheck · 108/108 unit · build (robots + sitemap prerendered) ·
319 e2e (ONE documented flake: the not-found document-head-parity test
red on chunk 3's first run, green on the isolated spec re-run AND the
full chunk re-run [77/77] — the transient head-metadata read class) ·
35/35 smoke. The post-push commit since the v116 parity push (b40d034)
audited: session log + the owner's skills/ tree prune — ZERO src/,
tests/, prisma/ or lockfile deltas.

**F3**: the series derived from the v111 lineage (derive-v117-series.py
— the generic swaps + the SIX exact-fragment history corrections, 6/6
applied on the FIRST run; line counts preserved). The census BUILT
two-half from the start (build-twohalf-v117.py via
derive-build-twohalf-v117.py with the swap-order rule; the TWO census JS
blocks [CALC_CENSUS_JS 61 lines + LOGIN_CENSUS_JS 36 lines]
byte-identical across the halves — the md5 line-block contracts
[e1092d12 / 9e5a52d2 — the v99/v105/v111 census blocks VERBATIM]; ONE
builder derivation REPAIR documented: the lineage-note fragment must
target the LINE-INTERNAL bare form "build-twohalf-v105.py — the v117
derivation" — the source wraps the line after "from", so the
with-prefix fragment missed silently on the first pass [the MISSING-
SOURCES report], the v107 line-break lesson's builder instance). The
verdicts: CALCULATOR DIFFERENT (the pair's documented verdict class —
the will-update note the SEED-DATA class [ref hasWillUpdateSpan:false,
its own Rent $25.00 equals its calculated total]; the hover-action row
the RESTING-STATE parity class [actionsAtRest {opacity 0, btnCount 2}
identical both sides]; the row-height flag their consequence) + LOGIN
DIFFERENT (the FAB flag alone — DISPROVEN live by the one-shot
base44-fab-arbit-v117.sh on the flagged /login surface at 1280: fabCount
0 + bodyHasBase44 false on BOTH sides — the platform-iframe chrome
class, the v97/v103/v108/v109/v115 standing disproof form re-confirmed).
The census compared AXIS-BY-AXIS by the persisted compare-v117-census.py
(**106 axes: 97 identical + 9 documented-class deltas, ZERO new** — the
card.shadow/panel.shadow zero-layer lead counts the v3/v4 construct
class [the visible layer the contract, the v45 F4 pin]; the card.border
zero-width computed-color artifact [border-width 0 both sides, nothing
renders — the v3 base default gray-200 vs the app's measured
--color-border token, the card line exactly as pinned in v7]; the
close-key family the v99 finder artifact [the v87 pin the authority, the
asymmetry direction verified still clone-only]; hasWillUpdateSpan the
SEED-DATA class) — with the strip census's `bottom` axis divergence (ref
742 vs clone 738) NOT whitelisted but root-caused (below) — the cycle's
find.

**F4 [FIX + PIN] — THE SM:TIER FREEZE (a new member of the trap-4b
family, the cycle's Tailwind v4 bug)**: the pin-candidate survey (the
login card's TOP ACCENT STRIP — the element every login census walked
past: the v7 G2 pin holds its gradient COLORS via toContain only, its
geometry never pinned at ANY viewport in ANY spec) measured the strip
byte-identical both sides — but the census's `bottom` axis read ref 742
vs clone 738, exposing a 4px card-height delta (ref 746 vs clone 742).
The drill-down (cardheight-arbit-v117.sh + the h1/subtitle reads): the
padding (48px 40px 40px), the form blocks (172 + 80), the h1 (72), the
subtitle (24) all IDENTICAL — the delta isolated to the h1 BLOCK's
internal gap: **the reference's subtitle margin-top 12px (its
sm:space-y-3 tier at >=640) vs the clone's 8px (its space-y-2 base tier
— the sm: tier FROZEN OUT)**. Both sides declare the reference's own
verbatim classes `space-y-2 sm:space-y-3` (login-card.tsx:574, the ONLY
sm-paired tier in the codebase). THE MECHANISM (the built-CSS
verification): the v9 G3 mitigation restores v3 space-y semantics for
the BASE tiers with class-specificity rules (`.space-y-2 > * + *
{ margin-block-start: 0.5rem }`, 0-1-2) — which BEAT v4's
zero-specificity `:where(.sm\:space-y-3 > :not(:last-child))` media
variant at >=640: **the sm: tier can never override the mitigated
base**. The v3 engine (the reference): the base and the media variant
share specificity and the media rule wins at >=640 — 12px. THE FIX (the
v50 zb-sm6 precedent's form): the sm:-variant restore in globals.css's
@layer utilities — `@media (min-width: 640px) { .sm\:space-y-3 > * + *
{ margin-block-start: 0.75rem } }` (source order after the base restore
decides the same-specificity tie). Cascade-verified SURGICAL: exactly
ONE element in the codebase carries sm:space-y-3; the v99 social-row
pin's rhythm axis is RELATIVE (both elements shift equally), the
v105/v7/v25/v45/v55/v51 pins element-local or other-mode — zero
existing pins redden (verified live, 52/52). THE RULE: a base-tier
mitigation restore MUST be accompanied by its responsive-variant
members — the class-specificity restore freezes out every
zero-specificity :where() variant of the same utility family at the
media breakpoint (check the built CSS for the :where() media form
whenever a mitigated utility carries an sm:/md:/lg: sibling in the
source classes).

The +1 pin (tests/e2e/login-parity.spec.ts): the login card's
TOP-ACCENT-STRIP + H1-BLOCK census at 1280 (+1 e2e = 320) — the strip's
never-pinned geometry {tag DIV/position absolute/top 0px/right 0px/
left 0px/h 4/w 448/bgImage the full 3-stop slate gradient} + the FIXED
family {subtitle mt "12px"/block h 108} + the card context {w 448/h
746} + the docSW guard; the finders STRUCTURAL (the form-walk-up card
finder; the strip as the card's absolutely-positioned thin top child;
the `bottom` axis deliberately UNPINNED — the card-height-derived data
axis, the v107 position-arithmetic discipline). TDD-verified: the
pre-fix RED run failed at the sm:TIER axes alone [subMt "8px" vs
"12px"] — the fix load-bearing; the standalone REBUILD; the post-fix
GREEN; the 52/52 surface regression check.

The ship: 320 e2e zero flakes across the auditable four-chunk split
(84+80+77+82 = 323 executions = 320 unique); 35/35 smoke; the
screenshots regenerated with 9 byte-diffs ARBITRATED (2 fix-effects
[01-login + 14-login-error — the +4px card shift, the fix's own
evidence] + 7 date-drifts [the relative-seed dates rolled a day:
03/04/05/06/07/08/16, the footer-band bboxes — the standing
same-day-seed law's boundary]; 15-forgot-reset byte-IDENTICAL — the
surgical-fix confirmation, the forgot mode rides the .zb-auth-mode
container untouched); the dev evidence 3 same + 1 date-drift +
VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the
menu open with all 5 links + the brand; the sheet closed post-nav; the
dashboard clean — the dev-shots scripts derived v116->v117 with the
version-swap-only verification).

The v118 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v111-era LOGIN + CALCULATOR pair (the v112-era NETWORTH +
drill-down-DASHBOARD pair — the desktop 1280x800 FULL-PAGE state of
(1) the NETWORTH view and (2) the DASHBOARD's drill-down EXPANDED
state, last re-shot v112 — now the oldest remaining [v112 < v113 <
v114 < v115 < v116 < v117]; the pair's NINTH re-run bracket [v60 -> v67
-> v76 -> v82 -> v88 -> v94 -> v100 -> v106 -> v112 -> v118] to be
verified against vlm-shots-v112.sh's own header before the
derivation), (2) the axe-core watch at its next re-check point (only a
5.x wrapper changes the calculus), (3) the npm-audit watch at its
re-check point (only a new advisory in the next/zod ranges changes the
calculus), (4) the deferred reference-write censuses (unchanged — out
of bounds under the v46 read-only rule).

## The v116 cycle (the v110-era SAVINGS pair's NINTH re-run — Session 151)

The re-run cadence's next-oldest candidate: the v110-era SAVINGS pair (the
SAVINGS view at desktop 1280x800, FULL-PAGE, last re-shot v110 — now the
oldest remaining [v110 < v111 < v112 < v113 < v114 < v115]; the pair's
NINTH re-run bracket [v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98 ->
v104 -> v110 -> v116]; the THIRTY-NINTH consecutive queue/ledger
agreement — the surface names verified against vlm-shots-v110.sh's own
header BEFORE the derivation). PIN-ONLY for src/; the cycle's standing
items: the axe watch (NO DRIFT — 4.14.0 holds, canary-only prereleases
beyond, the v68 dedupe verified), the npm-audit watch at its seventh
re-check (0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod
4.6.7]), the 110th standing checks (ALL GREEN — the mobile menu the
110th consecutive green; the reference's four bugs all live; the data
census clean on the FIRST reads, no render-race hit this cycle).

**F0 baseline FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace**
(the RESET class — the v115 environment did not persist; the repo
re-cloned from main @ 3e1c2e8). The v108 FRESH-CLONE lesson applied
END-TO-END: npm ci (run in the foreground — the v114 silent-death
lesson; 354 entries) with the zod extraction verified INTACT [840/840
files, the src/v4 subdirectory present, verified BEFORE any gate]; .env
[DATABASE_URL="file:../db/custom.db"] + db/ at the repo root; db:push +
db:seed (7 items / 3 assets / 2 liabilities); BOTH v1243 playwright
binaries verified DIRECTLY (the fresh cache held only the OLD
chromium-1200 pair). The gates: seedcheck exact (7/1850/2235/0/3/2) ·
lint · typecheck · 108/108 unit · build (robots + sitemap prerendered) ·
318 e2e zero flakes (84+78+77+82 = 321 executions = 318 unique — the
a11y file kept INSIDE chunk 4) · 35/35 smoke.

**F3**: the series derived from the v110 lineage (derive-v116-series.py
— the generic swaps + the EIGHT single-line-safe history corrections,
19 correction instances; ONE derivation REPAIR documented: the
plan-attribution fragment must target the line-internal BARE
"v109 plan's" form — the with-article form spans the v110 headers' line
break, the v107 line-break lesson's bare-form instance — see the lesson
below). The census BUILT two-half from the start (build-twohalf-v116.py
via derive-build-twohalf-v116.py with the swap-order rule; the ONE
census JS block [SV_CENSUS_JS 153 lines] byte-identical across the
halves — the md5 line-block contract [891ab9b6 — the v104/v110 census
blocks VERBATIM, the block itself version-free]; the builder's OWN
repair documented: the ref_exec startswith assertion's bare session
token [refarbit110 -> refarbit116] is a no-'v'-prefix token the generic
swap CANNOT touch — swapped explicitly this cycle, closing the v115
builder's clonearbit109 leftover counter-precedent). The verdict:
SAVINGS DIFFERENT — the pair's documented flag-set class (v104/v98/v110
read DIFFERENT) — every flag DOM-arbitrated (the payment chips the v57
DATA-CONDITIONAL class [the reference's savings item ships no
paymentMethod — its footer renders the date-only DIV, childCount 1;
the clone's render the SPAN pair, childCount 2]; the card grid the
seed-count class; the header stats + card contents the seed-data
classes; the avatar the user-identity class; NO FAB flag raised — the
disproof not required, the v103 standing class). The census compared
AXIS-BY-AXIS by the persisted compare-v116-census.py (120 axes: 80
identical + 40 documented-class deltas, ZERO new — the asymmetric
footer.children[1].*/badges[3].* families the DATA-CONDITIONAL and
superset-chip classes BY CONSTRUCTION) — NO NEW CLONE GAP.

**F4 [PIN]**: the savings goal-card's KEBAB TRIGGER census at 1280
(+1 e2e = 319). THE SPEC-ALIAS COVERAGE LESSON (the cycle's survey
finding — the V94-COLLISION criterion at its live form): the FIRST
mutation attempt (the h axis, h-9 w-9 -> h-10 w-9 at item-card.tsx:139)
failed the sole-failure test with TWO reds — the new pin AND the v45 F1a
pin, which holds the trigger's w 36 / h 36 / at-rest opacity "0" on
/income (items.spec.ts:1264-1266) — the SAME shared component line. The
coverage-map survey had missed it because it grepped the SOURCE token
forms (h-9 w-9, opacity-0, group-hover) instead of the SPECS' own alias:
the trigger's spec name is "kebab", a word that appears NOWHERE in the
source. THE RULES: (a) a coverage map for a shared-component family
must grep the spec-side ALIASES (the census variable names — "kebab",
"trigger", "actions") not just the source class tokens; (b) an axis held
in ANY view is held for EVERY view (the shared component renders them
all); (c) the resolution keeps the pin but re-scopes it to the axes NO
other spec holds — the at-rest {tag/display/radius/bg/color/cardTop/
cardRight} + the HOVER-path group-hover reveal {opacity "1"} (the
focus-path reveal is the tab-walk pin's sibling, never held) — with
the v45-held {w/h/at-rest-opacity} axes left OUT of the census return
value itself (a toEqual census whose return carries held axes would
re-collide); the FIRST mutation's two-red run kept as the collision
evidence (the v94 precedent). The final mutation: rounded-md ->
rounded-lg at item-card.tsx:139 line-scoped — only the v116 pin red at
the radius family axis alone ["6px" -> "8px"], the v45/tab-walk/v98/v80
pins structurally immune; restored, rebuilt, post-restore 46/46 green.

THE STATIC-HOVER-COORDINATE TRAP (the census-side lesson): the first
hover read's STATIC mouse move (640,300) missed the reference's ONLY
card — the reference's 1-item seed renders its Emergency Fund card in
grid COLUMN 1 (x 288-597), and x=640 lands on the column-gap
whitespace; the reference's trigger read hoverOpacity "0" (an apparent
REVEAL DIVERGENCE — the clone's column-2 card had caught the pointer
and read "1"). THE RULE: a hover-state census on seeded data must read
the target element's OWN bounding rect and move the pointer to the
element's OWN center — never a static viewport coordinate (the
reference's and the clone's layouts differ by the seed-count class,
and a static coordinate can land on either side of that boundary). One
more settle discipline: a hover-reveal pin must wait out the
transition-opacity window (~150ms) before reading (the v98 animate-in
settle precedent applied to the reveal — the first run read 0.033
mid-transition).

The ship: 319 e2e zero flakes across the auditable four-chunk split
(84+79+77+82 = 322 executions = 319 unique); 35/35 smoke; the
screenshots 20/20 byte-identical (the same-day-seed law — zero
arbitration); the dev evidence 4/4 byte-identical + VLM-verified (the
menu proof: /income, docSW 390, navLandmark true; the dev-shots scripts
derived v115->v116 with the version-swap-only verification).

The v117 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v110-era SAVINGS pair (the v111-era LOGIN + CALCULATOR pair —
the LOGIN view + the CALCULATOR dialog at desktop 1280x800, last re-shot
v111 — now the oldest remaining [v111 < v112 < v113 < v114 < v115 <
v116]; the pair's NINTH re-run bracket [v59 -> v66 -> v75 -> v81 ->
v87 -> v93 -> v99 -> v105 -> v111 -> v117] to be verified against
vlm-shots-v111.sh's own header before the derivation), (2) the axe-core
watch at its next re-check point (only a 5.x wrapper changes the
calculus), (3) the npm-audit watch at its re-check point (only a new
advisory in the next/zod ranges changes the calculus), (4) the deferred
reference-write censuses (unchanged — out of bounds under the v46
read-only rule).

## The v115 cycle (the v109-era ITEMS pair's NINTH re-run — Session 150)

The re-run cadence's next-oldest candidate: the v109-era ITEMS pair (the
ITEMS view — INCOME + EXPENSES — at desktop 1280x800, FULL-PAGE, last
re-shot v109 — now the oldest remaining [v109 < v110 < v111 < v112 <
v113 < v114]; the pair's NINTH re-run bracket [v57 -> v64 -> v70 -> v79
-> v85 -> v91 -> v97 -> v103 -> v109 -> v115]; the THIRTY-EIGHTH
consecutive queue/ledger agreement — the surface names verified against
vlm-shots-v109.sh's own header BEFORE the derivation).

**F0 baseline FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace**
(the RESET class — the v114 environment did not persist; the repo
re-cloned from main @ 735f612). The v108 FRESH-CLONE lesson applied
END-TO-END: npm ci (run in the foreground — the v114 silent-death
lesson) with the zod extraction verified INTACT [840/840 files, the
src/v4 subdirectory present, verified BEFORE any gate]; .env
[DATABASE_URL="file:../db/custom.db"] + db/ at the repo root; db:push +
db:seed (7 items / 3 assets / 2 liabilities); BOTH v1243 playwright
binaries verified DIRECTLY (the fresh cache held only the OLD
chromium-1200 pair). The gates: seedcheck exact (7/1850/2235/0/3/2 —
the env -u DATABASE_URL discipline, the canonical db-seedcheck-v68.cjs;
an initial ad-hoc seedcheck script hit the PrismaClient CWD-resolution
trap and was replaced by the canonical form before any gate) · lint ·
typecheck · 108/108 unit · build (robots + sitemap prerendered) · 317
e2e zero flakes (84+77+77+82 = 320 executions = 317 unique — the a11y
file kept INSIDE chunk 4) · 35/35 smoke. F0b the npm-audit watch (the
standing step's SIXTH cycle): 0 vulnerabilities — the v110 bump holds.
F1 the axe watch: NO DRIFT (npm-latest 4.14.0; wrapper + engine 4.14.0;
the v68 dedupe verified live — one node_modules/axe-core entry).

**F2: the 109th standing checks ALL GREEN** — derived v108->v109
(derive-standing-v115.py, three token families, normalize-back clean).
Reference: the four bugs ALL live (toast-blocker; sheet-trap; no-
landmark; the 464px /networth overflow) + the data census clean on the
FIRST reads (no render-race hit this cycle) + the SEO pair live. Clone:
R1-R4 ALL GREEN — the mobile menu VERIFIED WORKING the 109TH
CONSECUTIVE TIME, zero overflow at 390 on all five views, the SEO pair
live; the seedcheck exact after the clone half.

**F3**: the series derived from the v109 lineage (derive-v115-series.py
— the generic swaps + the FIVE single-line-safe history corrections, 13
correction instances; ONE derivation REPAIR documented: the bracket-
extension fragment must be written against the POST-generic-swap state
— see the lesson below). The census BUILT two-half from the start
(build-twohalf-v115.py via derive-build-twohalf-v115.py with the
swap-order rule; the ONE census JS block [193 lines] byte-identical
across the halves — the md5 line-block contract [b55dcd29 — the
v97/v103/v109 census blocks VERBATIM, the block itself version-free]).

**The verdicts: INCOME IDENTICAL + EXPENSES DIFFERENT — the pair's
documented verdict split (the same split as v109; v103 read BOTH
DIFFERENT; the income side's documented flags were all-data classes,
so the IDENTICAL verdict this run is the cleaner outcome on the same
chrome — the VLM-verdict variation form, the v105 LOGIN-IDENTICAL
precedent)** — with every flag DOM-arbitrated to a documented class:
the expenses card-footer payment chips the v57 DATA-CONDITIONAL class,
census-proven live (the reference's OWN income card's footer reads
childCount 2 with the "Bank Account" chip + icon — the reference
RENDERS payment chips when data carries them; its expense items simply
ship no payment method — footer childCount 1 — while the clone's carry
them); the badge-arrangement wrap the v57 wrap/classification-VALUE
classes (the expenses badgeRow h ref 22 vs clone 52, badgeCount ref 3
vs clone 4 — the clone's "Recurring" superset chip + the wrap; the chip
CHROME byte-identical); the "Edit with Base44" FAB the platform-chrome
class DISPROVEN live (the one-shot both-sides census
base44-fab-arbit-v115.sh: fabCount 0 + bodyHasBase44 false on BOTH
sides at 1280 on /expenses — the v97/v103/v108/v109 standing disproof
form re-confirmed; a FAB flag WAS raised, so the disproof ran); the
avatar the user-identity class; the header stats + card contents the
seed-data classes. The both-sides census compared AXIS-BY-AXIS by the
persisted compare-v115-census.py (**187 axes: 163 identical + 24
documented-class deltas, ZERO new deltas** — the avatar chrome, the
grid/card/titleRow/amount/footer/badge0 chrome, the filter card on
BOTH variants, the page header row, the docSW 1280 guard all
byte-identical) REPRODUCES the v109 census values EXACTLY — **NO NEW
CLONE GAP.**

**F4 [PIN]**: the family-extension survey walked the items views'
surfaces with the V94-COLLISION criterion (a family is only viable when
the mutation can fail ONE spec) and found **the VIEWPORT-BAND family:
the ITEMS view's md-band state (768 <= w < 1024) — the band NO spec
pins on the items views** (the coverage map: the items views pinned
ONLY at 390 [v52] and 1280 [v45/v64/v91/v92/v109]; the v42 five-route
mid-viewport census sits at 640 — BELOW md, the 1-col state; NOTHING in
the 768-1023 band on ANY items view). The one-shot both-sides census
(mdband-arbit-v115.sh, /income at 800x600 — the finders structural:
the card-like-children grid walk [radius 12px + pad 20px], the
Add-button->row walk [the v109 finder], the search->card->inner-grid
walk): **EVERY chrome axis byte-identical** — the item grid's md state
{the 2-col template `232px 232px`, gap 16px} + the page header row's
md state {flex/row/space-between/center/gap 16px/mb 32px/h 60/
childCount 2} + the filter card's inner grid md state {4 tracks
`95.5px x4`, gap 16px, childCount 3} + the card box at the 2-col width
{w 232/pad 20px/radius 12px/border rgb(229,231,227)/bg white} + the
filter card {w 480, mb 24px} + docSW 800 (no overflow in the band); the
childCount (1 vs 2) the seed-count class and the card h (230 vs 246)
the v70b-decomposed class — both DATA axes deliberately left UNPINNED
(the v107 position-arithmetic discipline). **Pin GREEN on the first
run** (45 passed in items.spec.ts; the count now **318**). **Mutation
verified single-family**: md:grid-cols-2 -> md:grid-cols-1 at
items-view.tsx:262 line-scoped (the ONLY `grid grid-cols-1 gap-4
md:grid-cols-2 lg:grid-cols-3` line in the file; the expenses filter
card's own md:grid-cols-2 on line 175 a DIFFERENT line — untouched by
the full-string scoping) — ONLY the v115 pin red (44 green), the
failure diff reading as the grid-template family axis ALONE
(`232px 232px` -> `480px`) after the standalone REBUILD; the 390/640
states structurally immune (grid-cols-1 base), the >=1024 states
structurally immune (lg:grid-cols-3 overrides md — the v45 1280 pin
green under the mutation), the header row's md:flex-row + the filter
card's md:grid-cols-4 separate tokens — untouched. Restored (git diff
src/ = 0), rebuilt, post-restore 45/45 green.

**F5 the ship chain**: lint · typecheck · 108 unit · 0 vulnerabilities ·
**318 e2e zero flakes** (84+78+77+82 = 321 executions = 318 unique) ·
35/35 smoke · the screenshots 16/16 byte-identical (the same-day-seed
law) · the dev evidence 4/4 byte-identical + re-captured + VLM-verified
(the menu proof: /income, docSW 390, navLandmark true; the menu open
with all 5 links + the brand; the sheet closed post-nav; the dashboard
clean — the dev-shots scripts derived v114->v115 with the
version-swap-only verification).

- THE POST-SWAP-FRAGMENT RULE (the derivation lesson, formalized): a
  history-correction fragment containing the CURRENT cycle's version
  token must be written against the POST-generic-swap state, not the
  pre-swap source form — the generic swap consumes the version token
  FIRST (v109 -> v115), so a correction written against the source
  (e.g. `-> v97 -> v103 -> v109]`) finds ZERO matches and the bracket
  silently loses its newest entry. The v115 run's first pass produced
  `[v57 -> ... -> v103 -> v115]` (the v109 entry MISSING) — caught by
  reading the derived header BEFORE proceeding, repaired by targeting
  the post-swap form (`-> v97 -> v103 -> v115]` -> `-> v97 -> v103 ->
  v109 -> v115]`). The v114 derivation's own precedent (its bracket
  correction targeted the already-swapped `v96 -> v102 -> v114])` form)
  now formalized as a rule: every correction's old-fragment must be
  checked against the file state AS THE CORRECTIONS SEE IT (after the
  generic swaps), and the residual check must include the corrected
  bracket's full expected form.

The v116 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v109-era ITEMS pair (the v110-era SAVINGS pair — the SAVINGS
view at desktop 1280x800, FULL-PAGE, last re-shot v110 — now the oldest
remaining [v110 < v111 < v112 < v113 < v114 < v115]; the pair's NINTH
re-run bracket [v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98 -> v104
-> v110 -> v116] to be verified against vlm-shots-v110.sh's own header
before the derivation), (2) the axe-core watch at its next re-check
point (only a 5.x wrapper changes the calculus), (3) the npm-audit
watch at its re-check point (only a new advisory in the next/zod
ranges changes the calculus), (4) the deferred reference-write censuses
(unchanged — out of bounds under the v46 read-only rule).

## The v114 cycle (the v108-era MOBILE TWINS pair's EIGHTH re-run — Session 149)

The re-run cadence's next-oldest candidate: the v108-era MOBILE TWINS
pair (BOTH mobile 390x844 full-page twins — (1) the /NETWORTH view [the
v63-era pair's surface] and (2) the DASHBOARD [the v62-era mobile
twin's surface], last re-shot v108 — now the oldest remaining [v108 <
v109 < v110 < v111 < v112 < v113]; the pair's EIGHTH re-run bracket
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114];
the THIRTY-SEVENTH consecutive queue/ledger agreement — the surface
names verified against vlm-shots-v108.sh's own header before the
derivation). PIN-ONLY for src/; the cycle's standing items: the axe
watch (NO DRIFT — 4.14.0 holds, only rc/next sha prereleases beyond,
the v68 dedupe verified), the npm-audit watch at its fifth re-check (0
vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]), the
108th standing checks (ALL GREEN — the mobile menu the 108th
consecutive green; the reference's four bugs all live; the data census
clean on the FIRST reads, no render-race hit this cycle). The verdicts:
BOTH PAIRS DIFFERENT — the pair's documented verdict class (the
v84/v90/v96/v102/v108 re-run family) — with every flag DOM-arbitrated
to a documented class: the stat-tile side-by-side-vs-stacked the v41
mobile-superset class (statGrid cols 2-col-vs-1-col, gap 16px
identical, tiles h 84 byte-identical); the summary-card height the same
class's width consequence (432x333 vs 358x421); the trend-circle claim
the VLM MISREAD class (the medallion 64x64 + the trendIcon 32x32
byte-identical; the v108 "slightly larger" misread now in its
color-perception form — the class's non-determinism); the TAB-BAR
ALIGNMENT flag — a NEW flag form this cycle ("the reference's tabs
CENTERED, the clone's LEFT-ALIGNED") — the v41 width-consequence class
with the centering claim DISPROVEN live by the one-shot both-sides
census fabtab-arbit-v114.sh (the tablist's justifyContent "center" +
alignItems "center" byte-identical on BOTH sides; the w ref-432 vs
clone-358 + the gridCols + the tabs' w 212-vs-175 the reference's own
464px overflow width class; every non-width axis byte-identical [h 36,
bg rgb(245,245,245), radius 8px, pad 4px, maxW 448px, the tabs' h
28/radius 6px/fs 14px/fw 500/pad 4px 12px/icon 16x16, the active +
inactive color/bg pairs]); the "Edit with Base44" overlay — flagged on
BOTH pairs — the platform-chrome class DISPROVEN live (the one-shot:
fabCount 0 + bodyHasBase44 false on BOTH sides at BOTH surfaces
[/networth AND /] at 390 — the FAB lives in the reference's platform
iframe chrome; the v85/v91/v97/v103/v108 standing disproof form
re-confirmed — a FAB flag WAS raised, so the disproof ran); the
subtitle wrap-point the v62 width-delta class (chrome byte-identical
[blockH 92, exactly 2 DOM lines both sides, tops 123/147] — the
reference's own 395px overflow shifts its wrap; its block 363 vs the
clone's 358); the progress-bar geometry the pct DATA class (the fill
width each site's own allocation over the byte-identical track/fill
chrome — the "different border-radius/thickness" sub-claim the
perception of the same fill-width delta); the data figures the
seed-data classes. The two-half census (NW_CENSUS 42 lines md5
82cf8a43 + DASH_CENSUS 87 lines md5 85e4ec7e — the version-free
v102/v108 census blocks carried over VERBATIM) reproduces the v108
values EXACTLY on every axis (the NW summary card 432x333/358x421 +
statGrid cols/gap 16/children 2 + tiles 176x84 / 294x84 [the h 84
identical] + medallion 64x64 [clipsViewport ref true / clone false —
the R-bug-4 consequence] + trendIcon 32x32 + docSW 464/390; the DASH
subtitle 363x48/358x48 + computed identical + blockH 92 + 2 lines tops
123/147 + breakdownCard h 324/svgCount 7/the 16-14 alternation/children
H3 h 20 + DIV h 238 + the spendingCard finder's SAME fallback string
both sides + docSW 395/390) — NO NEW CLONE GAP. The +1 pin
(tests/e2e/dashboard.spec.ts): the DASHBOARD mobile twin's HEADER-ROW
interior family at 390 — the row {flex/column/flex-start/space-between/
gap 16px/mb 32px/h 144} + the block {h 92/bottom 169} + the junction
{gap 16} + the Add Item button's BOX chrome {36x127/pad 8px 16px/radius
6px/14px/500/white/the 135deg gradient/icon 16x16} — never pinned at
ANY viewport in ANY spec (the v62 pin walks the h1's PARENT BLOCK's
interior, never the row; the session-5 pin the button's gradient; the
v35 S2 the focus shadow; the G3 the icon; the v52 F3/v65/v109 pins the
items-view headers — different elements), measured byte-identical both
sides via the one-shot drow-arbit-v114.sh (the finders structural: the
childless-exact-text h1 + the parentElement block walk [the v62
lesson] + the parentElement row walk + the row's button-with-text
walk); mutation-verified single-axis AND cascade-free (items-start ->
items-center at dashboard-view.tsx:927 line-scoped — the ONLY
mb-8 flex flex-col justify-between items-start gap-4 line in the
file; only the v114 pin red at the row.align axis alone [flex-start ->
center] after the standalone REBUILD; the cross-axis alignment moves
only the deliberately-unpinned x positions — the block's h/bottom, the
button's top/h, the junction, the row's h, the goalCard.y 253 below
all green under the mutation; the >=768px rendering untouched by the
md:items-center override). The workspace: the RESET class (the v113
environment did not persist) — the v108 FRESH-CLONE provisioning lesson
applied end-to-end (npm ci; the zod extraction verified 840/840 with
src/v4 present BEFORE any gate; BOTH v1243 playwright binaries verified
DIRECTLY; .env + db push/seed). The ship chain: 317 e2e zero flakes
(84+77+75+84 = 320 executions across the auditable four-chunk split);
35/35 smoke; the screenshots 16/16 byte-identical (the same-day-seed
law — zero arbitration); the dev evidence 4/4 byte-identical +
re-captured + VLM-verified (the menu proof: /income, docSW 390,
navLandmark true).

- THE V94-COLLISION SURVEY LESSON (the F4 family-extension method, its
  sharpest form): a pin family is only viable when the MUTATION can
  fail ONE spec — the networth section-row interior at 390 (the v94
  pin's mobile twin, measured byte-identical both sides by the one-shot
  secrow-arbit-v114.sh) was REJECTED because EVERY axis of the family
  is already held by the v94 pin at 1280: any mutation on the shared
  element fails BOTH pins (the multi-spec cascade). The same collision
  rejected the asset-card facts-row mobile twin (the v106 pin), the
  mobile sheet's brand/nav/footer interiors (the v104/v110/v103 rail
  pins hold the SAME components at 1280 — every sheet mutation
  cascades), the mobile topbar (the v108 pin's own family), the
  content wrapper's p-4 (the v53 tablist-x + G13 collisions under any
  pad mutation), and the spending-card header at 390 (the 1280
  box/header census collision). The WINNING family carries at least
  one axis pinned ONLY by the new pin (the mutation target) — the
  dashboard header-row's align axis, held by NO other spec at ANY
  viewport, with the >=768px md: override making the desktop pins
  structurally immune.

The v115 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v108-era MOBILE TWINS pair (the v109-era ITEMS pair — the
ITEMS view [income + expenses] at desktop 1280x800, FULL-PAGE, last
re-shot v109 — now the oldest remaining [v109 < v110 < v111 < v112 <
v113 < v114]; the pair's NINTH re-run bracket [v57 -> v64 -> v70 -> v79
-> v85 -> v91 -> v97 -> v103 -> v109 -> v115] to be verified against
vlm-shots-v109.sh's own header before the derivation), (2) the
axe-core watch at its next re-check point (only a 5.x wrapper changes
the calculus), (3) the npm-audit watch at its re-check point (only a
new advisory in the next/zod ranges changes the calculus), (4) the
deferred reference-write censuses (unchanged — out of bounds under the
v46 read-only rule).

## The v111 cycle (the v105-era LOGIN + CALCULATOR pair's EIGHTH re-run — Session 146)

The re-run cadence's next-oldest candidate: the v105-era LOGIN +
CALCULATOR pair (the LOGIN view + the CALCULATOR dialog at desktop
1280x800, last re-shot v105 — now the oldest remaining [v105 < v106 <
v107 < v108 < v109 < v110]; the pair's EIGHTH re-run bracket [v59 -> v66
-> v75 -> v81 -> v87 -> v93 -> v99 -> v105 -> v111]; the THIRTY-FOURTH
consecutive queue/ledger agreement — the surface names verified against
vlm-shots-v105.sh's own header before the derivation). PIN-ONLY for
src/; the cycle's standing items: the axe watch (NO DRIFT — 4.14.0
holds, the v68 dedupe verified), the npm-audit watch at its second
re-check (0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod
4.6.7]), the 105th standing checks (ALL GREEN — the mobile menu the
105th consecutive green; the reference's four bugs all live; the census
clean on the first read). The verdicts: CALCULATOR DIFFERENT (every
flag DOM-arbitrated to a documented class — the "Will update category
total" note the SEED-DATA class [ref hasWillUpdateSpan false: its own
Rent $25.00 equals its calculated total]; the hover-action row the
RESTING-STATE parity class [actionsAtRest {opacity 0, btnCount 2}
identical both sides]; the row-height flag their consequence) + LOGIN
IDENTICAL (the v105 precedent — the verdict-variation form). The
two-half census (CALC_CENSUS_JS 61 lines md5 e1092d12 + LOGIN_CENSUS_JS
36 lines md5 9e5a52d2 — the v99/v105 census blocks VERBATIM,
source-to-source verified) reproduces the v105 values exactly — NO NEW
CLONE GAP. The +1 pin (tests/e2e/calculator.spec.ts): the calculator's
LINE-ITEMS SECTION HEADER ROW at 1280 — the row {flex/center/
space-between/mb 16px/mt 0px/h 32/w 720/childCount 2} + the "Line
Items" h3 {16px/600/rgb(26,58,46)/lh 24px/h 24/margin 0px} + the
junction (h3CenterY === rowCenterY) + the addBtn context {110x32} —
never pinned at ANY viewport in ANY spec (zero "Line Items"
assertions across all 24 specs; the v81 addBtn pin + the v66 height
family + the v93 totalCard census all live on DIFFERENT elements),
measured byte-identical both sides via the one-shot
sectionrow-arbit-v111.sh, mutation-verified single-axis AND
cascade-free (font-semibold -> font-bold at calculator-dialog.tsx:171
line-scoped — the ONLY bare font-semibold line in the file; the
nameH4's mb-1 font-semibold at line 210 untouched; only the v111 pin
red at sectionH3.fw alone [600 -> 700] after the standalone REBUILD).
The ship chain: 314 e2e zero flakes (76+80+79+82 = 317 executions =
314 unique); 35/35 smoke; the screenshots 16/16 byte-identical (the
same-day-seed law); the dev evidence re-captured + VLM-verified.

- THE PROVISIONING LESSON (a fresh-workspace note): a fresh sandbox's
  playwright browser cache can hold only an OLDER pin's binaries
  (chromium-1200 + chromium_headless_shell-1200 here) while
  `npx playwright install chromium --dry-run` happily REPORTS the
  current pin's install location — the dry-run is a location report,
  NEVER an existence proof. The first chunk failed 74/75 with
  "Executable doesn't exist at .../chromium_headless_shell-1243"
  (the headless suite runs the headless-SHELL binary, not the full
  chromium). THE CHECKLIST RULE: verify the cache DIRECTLY
  (`ls /home/z/.cache/ms-playwright/` for BOTH `chromium-<pin>` AND
  `chromium_headless_shell-<pin>`) before the first e2e run; the
  full `npx playwright install chromium` downloads BOTH binaries.
- THE ONE-SHOT CENSUS COMMAND FORM (a census-note addendum): opening
  a hover-revealed control needs the vlm-shots form — mouse-move to
  the button center FIRST (the hover state holds), then mouse-down +
  mouse-up; the bare `agent-browser click` command can drop the
  hover-revealed button before the press lands (the first
  sectionrow-arbit run read "no panel" on exactly this), and a census
  passed into `with-server.sh bash -s` must travel as an ENV VARIABLE
  (the quoted heredoc never expands the parent's shell variables).

The v112 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v105-era LOGIN + CALCULATOR pair (the v106-era NETWORTH +
drill-down-DASHBOARD pair — the desktop 1280x800 FULL-PAGE NETWORTH
view + the DASHBOARD's drill-down EXPANDED state, last re-shot v106 —
now the oldest remaining [v106 < v107 < v108 < v109 < v110 < v111]; the
pair's EIGHTH re-run bracket [v60 -> v67 -> v76 -> v82 -> v88 -> v94 ->
v100 -> v106 -> v112] to be verified against vlm-shots-v106.sh's own
header before the derivation), (2) the axe-core watch at its next
re-check point (only a 5.x wrapper changes the calculus), (3) the
npm-audit watch at its re-check point (only a new advisory in the
next/zod ranges changes the calculus), (4) the deferred reference-write
censuses (unchanged — out of bounds under the v46 read-only rule).
