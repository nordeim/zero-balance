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
