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
