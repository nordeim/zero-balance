# Session 19 — Fresh Verification & Parity Iteration v10

**Date:** 2026-10-08 · **Baseline:** `ab9f80c` (session-18 = session-17's
narrative record) · **Outcome:** 1 finding group fixed TDD-first —
**96/96 unit · 104/104 e2e · 30/30 smoke**, live parity re-verified.

## Baseline re-verification

The workspace survived from session 17 (repo at `9c23518`, clean tree);
`git pull` fast-forwarded to `ab9f80c` (only `docs/session_18.md` — the
session-17 narration). Environment intact (`.env`
`DATABASE_URL="file:../db/custom.db"`, `db/custom.db`, node_modules). Doc
chain re-read (AGENTS → CLAUDE → README → PAD → SKILL → session_17 →
plan-v9 → worklog → session_18), v9 pins spot-checked in the code
(`DialogCloseButton` wired in all four form dialogs, `rounded-[9999px]`
census, the donut value-DESC sort, the inline Label), then the full chain
at HEAD: **lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ · 102/102 e2e ✓ ·
30/30 smoke ✓** — the v9 baseline confirmed intact.

Environment note: the sandbox returned to reaping background processes
this session (session-11 behavior D-9) — the detached :3200 parity server
died at every command exit, so the audit ran through `with-server.sh`
per command (boot + probe + kill), while the agent-browser daemon kept
persisting across tool calls (sessions survive, the server doesn't).
Mid-session the daemon itself hit resource pressure (EAGAIN spawns, a
browser auto-launch CDP timeout) — a full `agent-browser close --all` +
daemon kill + fresh re-login of all four sessions cleared it. The same
pressure crashed the first full e2e run (22 failures) — closing the live
sessions before the run fixed it (session-17 lesson, re-confirmed).

## The v10 audit — the sheet's active state and the open-state surfaces

Fresh angles this pass (surfaces the earlier passes had not measured):
the **mobile sheet's active-link styling** — the task-focus surface's one
unmeasured state dimension — plus the sheet's **brand/user-footer
internals**, the **Select popover OPEN state**, the **card action-menu
OPEN state**, the **breakdown drill-down EXPANDED rows**, the **Budget
Guidelines leaf typography**, the **live focus-visible ring**, the
**tall-dialog scroll mechanics**, the **date input rendering**, and the
**empty-submit validation behavior** — plus the standard mobile-nav
re-verification (R1/R2/R4/R5 all re-confirmed live) and the reference
data-drift check (unchanged: +$3475.00, 30.5%).

**Findings ledger (1 group, `docs/remediation-plan-v10.md`):**

- **G1 [MED] mobile sheet active highlighting**: measured live on the
  reference's sheet at `/income` — its current-route link carries the
  FULL active style (`linear-gradient(135deg, rgb(45, 90, 74),
  rgb(143, 188, 63))`, white, fw 500, on the same 32px `rounded-lg
  px-3 py-2.5` row classes the clone already uses) while the other four
  links stay `#3f3f46`/400. The clone's sheet shipped
  `highlightActive={false}` from session 1 — an unmeasured assumption
  that survived eight audit passes because none measured the sheet's
  ACTIVE dimension. Fixed: the prop removed from the sheet's
  `SidebarBody` (the sheet now shares the rail's active logic, including
  the superset #3 root-route Dashboard highlight).

Observations documented (no action): the reference does NOT toast on
budget-item save (a live save fired nothing — its Notifications region
stayed empty; the clone's success toasts are superset UX); empty-submit
is silent on BOTH sites (native `required` blocks the submit); and the
reference's dialogs carry no `role="dialog"` — probing via that selector
silently reports "closed" (its overlays are plain fixed divs; R5
re-confirmed properly through the click-refusal + heading evidence).

Audit mutation, neutralized in place: the probe expense item ("Probe
toast test", $1.00) is undeletable on the reference (it has no
expense-delete path — the documented superset #6 gap), so it was edited
to "Miscellaneous" / $0.00; the reference's dashboard totals are restored
(+$3475.00, expenses $525.00) with a residual expenses item count of 4
(was 3).

Also verified MATCHING (no action): burger/topbar/brand geometry
(28×28 at (24,16), 16px `#0a0a0a` icon, "ZeroBalance" 20px/700); sheet
chrome (288×844 `#fafafa`, 1px `#e5e5e5`, `rgba(0,0,0,0.8)` overlay) and
nav rows (32px, y 145/185/225/265/305); sheet brand block (18px/700
`#1a3a2e` at (76,24)) + user footer (36×36 lime avatar, "Budget Pro"
14px/500); Select popover OPEN state (listbox 306×106, white, 1px
`#e5e5e5`, r6, no shadow; options 32px 14px/400 `#0a0a0a`, pad
6px 32px 6px 8px; selected `#171717`/`#f5f5f5` + check); card
action-menu OPEN state (128×74, plain-text Edit `#0a0a0a` + Delete
`#dc2626`, pad 6px 8px); drill-down EXPANDED rows (collapsed 254×64,
subcategory 28px `#f9fafb` tint); guidelines leaves (~50% `#e07a3b`,
~30% `#3b7ea1`, ~20% `#8fbc3f`, 12px `#6b7280` descriptions); live
focus-visible ring (1px `rgb(10,10,10)` box-shadow ring + ambient —
the clone's extra transparent layers paint nothing); dialog scroll
mechanics (672×519 `maxHeight 519.3px` panel, `overflow: auto`, sticky
69px header, static footer, whole-panel scroll); native date inputs
(304×36, 14px); mobile overflow — the clone fits exactly 390 on all
five routes (the reference scrolls to 395 on `/`).

## TDD execution

2 new e2e tests, RED first: "the sheet highlights the CURRENT route like
the reference (v10)" (on `/income`: Income = white + the exact gradient
string + fw 500; the other four inactive) and "the sheet highlights
Dashboard on the root route (superset #3, v10)" (on `/`: Dashboard
active in the sheet). Both failed against the current build for the
right reasons; the fix (one prop removed from `sidebar.tsx`) turned
them GREEN with the full mobile-navigation file at 11/11. The first
full-suite run failed 22 tests under resource pressure from the four
live agent-browser sessions — closing them (session-17 lesson) brought
the chain to **104/104 e2e** (102 + 2 net-new).

## Verification & docs

Full chain: lint · typecheck · **96/96 unit** · build · **104/104 e2e** ·
**30/30 smoke**. Live parity re-verified on the fixed build, side by
side with a fresh reference session: on `/income` the clone's sheet now
renders Income EXACTLY as the reference does (white +
`linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))` + 500,
others `#3f3f46`/400); on `/` the clone's sheet highlights Dashboard
(the superset #3 behavior, now consistent across rail AND sheet — the
reference's own sheet marks nothing active there, its documented
root-route gap).

Screenshots: db re-seeded, all 13 shots regenerated on the fixed build —
only `10-mobile-menu.png` changed (the sheet now shows the active
highlight). `.env.example` verified to match the codebase (3 vars —
DATABASE_URL relative contract, NEXT_PUBLIC_SITE_URL, AUTH_SECRET).

Docs aligned: README (feature row, counts 104, plan-v10 row, the
close-live-sessions-before-e2e note), CLAUDE.md (counts + the sheet
pin), AGENTS.md (v10 pin paragraph), SKILL (state 96/104/30, lesson
12.24, Appendix B row), probe README (v10 catalog), this session log,
and `worklog.md`.
