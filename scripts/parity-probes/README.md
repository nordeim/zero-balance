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
