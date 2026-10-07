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
