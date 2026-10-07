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
