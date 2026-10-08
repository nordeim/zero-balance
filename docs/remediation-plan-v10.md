# Remediation Plan v10 — Session-19 Parity Iteration

> **Status: COMPLETE** — the single finding group fixed TDD-first (2 new e2e
> tests, RED → GREEN); full chain green at 96 unit / 104 e2e / 30 smoke;
> live parity re-verified. See `docs/session_19.md`.

Date: 2026-10-08 · Scope: fresh two-site re-audit after the v9 baseline
(`ab9f80c`) re-verified green (lint · typecheck · 96/96 unit · build ·
102/102 e2e · 30/30 smoke). Probes: `scripts/parity-probes/probe-v10-*.mjs`
via `run-probe.sh`, agent-browser sessions (`ref10`/`clone10` desktop
1280×800 + `ref10m`/`clone10m` 390×844), the standalone parity server on
:3200 booted per command through `with-server.sh` (this session's sandbox
returned to reaping background processes — session-11 behavior D-9; the
agent-browser daemon still persists across tool calls).

This pass re-verified the entire mobile-navigation stack end-to-end (the task
focus) — including, for the first time, the sheet's **active-link styling**
and the sheet's **brand/user-footer internals** at mobile depth — and then
swept surfaces no earlier pass had measured at computed-style depth: the
**Select popover OPEN state**, the **card action-menu OPEN state**, the
**breakdown drill-down EXPANDED rows**, the **Budget Guidelines leaf
typography**, the **live focus-visible ring**, the **tall-dialog scroll
mechanics**, the **form-validation empty-submit behavior**, and the **date
input rendering**. It found **1 clone-side finding group**; no new reference
bugs (R1–R7 all re-confirmed live; reference data unchanged since session 11:
income 5000 / savings 1000 / expenses 525 → `+$3475.00`, 30.5% — one audit
mutation neutralized in place, see Observations).

---

## Findings ledger

### G1. [MED] Mobile sheet: active-nav highlighting missing (the task-focus area)

Measured live on the reference's mobile sheet (390×844, sheet open at
`/income`): the current route's nav link renders in the FULL ACTIVE style —
`linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))` background
(the same forest-medium→lime gradient as the desktop rail's active link),
white text `rgb(255,255,255)`, `font-weight: 500`, h 32, radius 8px, pad
10px 12px — while the other four links stay inactive
(`rgb(63,63,70)`, fw 400). (On `/` the reference's own root-route bug
supersedes — its active check compares the pathname to `/dashboard`, so
nothing lights up there; that gap is the documented superset #3.)

The clone's sheet renders `highlightActive={false}`
(`src/components/budget/sidebar.tsx:195`) — a session-1 assumption, never
measured against the reference until now — so its mobile sheet NEVER
highlights the current route on ANY page. Every other sheet surface matches
(brand block, nav rows, avatar, footer), making this the one visible
mobile-nav difference between the apps.

The link classes already match the reference exactly (`flex h-8 w-full
items-center gap-3 rounded-lg px-3 py-2.5` → h 32 / radius 8 / pad 10px
12px), and the active-style branch (white + inline gradient + `font-medium`)
is already implemented and shared with the rail — the fix is to STOP
suppressing it: drop the `highlightActive={false}` prop from the sheet's
`SidebarBody` (default is `true`). The sheet then inherits the same active
logic as the rail, including the superset #3 root-route Dashboard highlight.

Fix files: `src/components/budget/sidebar.tsx` (one prop removed — the
`highlightActive` plumbing itself stays, documented as an explicit off-switch
should a future surface need it).

### Observations (documented, no action)

- **The reference does NOT toast on budget-item save.** A live save (the
  audit's probe item) fired no toast anywhere on the reference — its
  Notifications region stayed empty. The clone's success toasts are
  therefore a **superset UX feature** (in the same class as delete
  confirmations), not a parity drift — keep them.
- **Empty-submit is silent on BOTH sites.** Clicking Save Item with empty
  required fields does nothing visible on either app (native `required`
  validation blocks the submit; no toast, no red borders, no `aria-invalid`).
  Matching behavior — no action.
- **Audit mutation, neutralized in place:** the probe expense item
  ("Probe toast test", $1.00) is undeletable on the reference (it has no
  expense-delete path — the documented superset #6 gap), so it was edited to
  "Miscellaneous" / $0.00. The reference's dashboard totals are restored
  (`+$3475.00`, expenses `$525.00`); the residual is the expenses item count
  (3 → 4, a $0.00 row in its breakdown).
- **R5 selector note:** the reference's dialogs carry no `role="dialog"` —
  probing them via that selector silently reports "closed". Its overlays are
  plain fixed divs (as documented); an overlay-climb or heading-text probe is
  the reliable pattern (the v9 probes already do this).

### Verified matching this pass (no action)

Mobile navigation (task focus, both sites 390×844): toggle 28×28 at (24,16)
with a 16px `#0a0a0a` icon; top-bar brand "ZeroBalance" 20px/700 at (68,16)
140×28 — identical; **R1 re-confirmed live** — the ref's toast container
(`fixed top-0 z-[100]`, h32, w390, `pointer-events: auto`) still intercepts
its hamburger's center hit (elementFromPoint returns the container; a real
agent-browser click is REFUSED by its own actionability check), the clone's
hit is DIRECT; **R2 re-confirmed** — tapping Income in the ref's sheet
navigated but left `sheetStillOpen: true`; the clone's closed; **R4
re-confirmed** — the ref scrolls to 395px on `/` at 390px; the clone fits
exactly 390 on all five routes; sheet chrome identical (288×844 `#fafafa`,
1px `#e5e5e5`); sheet nav rows identical (32px, 14px, `#3f3f46`, y
145/185/225/265/305); sheet brand block identical (18px/700 `#1a3a2e` at
(76,24), 12px `#2d5a4a` subtitle); sheet user footer identical (36×36
lime `#8fbc3f` 9999px avatar, "Budget Pro" 14px/500 `#1a3a2e`). R5
re-confirmed (the ref's dialog ignores Escape with focus inside — only its
Select popover layer closes). Select popover OPEN state identical (listbox
306×106 at trigger-left+20, white, 1px `#e5e5e5`, radius 6, no shadow,
z-50; options 32px 14px/400 `#0a0a0a`, pad 6px 32px 6px 8px; selected
option `#171717` + `#f5f5f5` + check icon). Card action-menu OPEN state
identical (128×74, white, 1px `#e5e5e5`, radius 6, no shadow; plain-text
"Edit" 32px `#0a0a0a` + "Delete" 32px `#dc2626`, pad 6px 8px — no icons).
Breakdown drill-down EXPANDED rows identical (collapsed row 254×64 16px/400;
subcategory rows 28px 214px 16px/400 `#0a0a0a`, pad 6px 12px, `#f9fafb`
tint). Budget Guidelines identical (~50% `#e07a3b` / ~30% `#3b7ea1` / ~20%
`#8fbc3f` at 14px/400; descriptions 12px `#6b7280`; no bars — text-only
card). Focus-visible ring identical (keyboard-focused text input renders
the 1px `rgb(10,10,10)` box-shadow ring + `rgba(0,0,0,0.05) 0 1px 2px`
ambient on both — the clone's extra transparent shadow layers and outline
metadata paint nothing). Dialog scroll mechanics identical (panel 672×519
`maxHeight 519.3px`, `overflow: auto`, radius 16; sticky 69px white header
with 1px `#e5e7e3` border; static footer `16px 0 0` pad; the WHOLE panel
scrolls, header sticks). Date inputs identical (native `type=date`, 304×36,
14px, `#0a0a0a`, `#e5e5e5` border). Hero/stat/donut/guideline text state
unchanged vs the v9 pins. Reference data state unchanged (no drift).

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | G1 sheet active highlight: drop `highlightActive={false}` from the sheet's `SidebarBody` | `mobile-navigation.spec.ts`: NEW "the sheet highlights the CURRENT route like the reference (v10)" (on `/income`: Income link = white text + `linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))` + fw 500; the other four links inactive) + NEW "the sheet highlights Dashboard on the root route (superset #3, v10)" (on `/`: Dashboard active in the sheet) | `src/components/budget/sidebar.tsx` |
| 2 | Docs: session_19 log, worklog, README/AGENTS/CLAUDE/SKILL alignment + probe README v10 rows | — | docs |
| 3 | Regression: full chain + live parity re-check of the sheet + screenshot refresh | — | — |

## Regression pin map (must NOT change)

- All six superset fixes (hamburger hit, sheet close-on-nav, root-URL nav
  highlight — which the sheet now ALSO honors, no mobile overflow, Escape
  close, delete confirmations)
- The desktop rail's active gradient pin (mobile-navigation.spec's rail test)
  and the sheet hover-tint pin (Income stays inactive on `/dashboard`, so
  the hover test is unaffected)
- Sheet geometry (288×844, `#fafafa`, 1px `#e5e5e5`, `rgba(0,0,0,0.8)`
  overlay), sheet nav row geometry (32px, y 145/185/225/265/305), brand
  block, user footer — all re-measured identical this pass
- v5–v9 surface pins: token block, `@variant hover`, dialog X/footers/labels
  /tiles, radio/switch `#171717`, 9999px radii, donut value-DESC +
  labelLine={false}, login per-state geometry, badge hex pins, plain-text
  menus, empty states
- e2e fixture discipline: every spec restores what it mutates
