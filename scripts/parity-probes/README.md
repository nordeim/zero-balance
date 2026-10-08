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
