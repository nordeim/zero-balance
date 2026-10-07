# Session 7 — Fresh Verification & Parity Iteration v4

**Date:** 2026-10-07 · **Scope:** workspace refresh (`git pull` → `4f9cb28`), docs re-validation, full-chain re-verification, a fresh two-site parity audit (desktop 1280×800 + mobile 390×844) and remediation v4 · **Outcome:** 6 finding groups fixed TDD-first, full chain green (96 unit / 52 e2e / 30 smoke), live parity re-verified, pushed to `main`.

## Where this session started

Session 5 had completed remediation v3 and pushed `a037acc`;
`4f9cb28` added its raw narrative (`docs/session_6.md`). This session
treated that as the baseline: docs review (AGENTS / CLAUDE / README / PAD /
SKILL / session_5 / session_6 / remediation-plan-v3 / worklog), a
codebase validation (13 route files / 21 handlers, `.env` →
`file:../db/custom.db`, db at repo root, suites intact), and the full
chain from scratch — **typecheck ✓ · lint ✓ · 96/96 unit ✓ · build ✓ ·
46/46 e2e ✓ · 30/30 smoke ✓** — before touching anything.

One doc drift found during the review: CLAUDE.md still carried the
session-2 test counts (87 unit / 34 e2e) — fixed in this session's docs
pass.

## The fresh audit (probe scripts under `scripts/parity-probes/`)

Two agent-browser sessions (clone standalone on :3200, live reference),
DOM + computed-style probes on both. Probe sources are passed via
`eval(atob(...))` (base64) — raw `"$(cat file)"` quoting mangles `$` in
regexes. New probes: `probe-dashboard-v4`, `probe-followup-v4`,
`probe-legend-v4`, `probe-nav-v4`, `probe-navlink-detail-v4`,
`probe-nav-hover-v4`, `probe-items-v4`, `probe-item-card-v4`,
`probe-badges-v4`, `probe-footers-v4`, `probe-networth{,2,3,4}-v4`,
`probe-nw-panel-v4`, `probe-outline-v4`, `probe-desktop-chrome-v4`,
`probe-mobile-v4`, `probe-hamburger-v4`, `probe-overflow-v4`,
`probe-nw-overflow-v4`, `probe-shell-chain-v4`, `probe-isolate-v4`,
`probe-dialog{,2,3}-v4`, `probe-savings-v4`, `probe-empty-type`.

Confirmed matching (no action): hero card gradient/label/status badge
(`Under Budget` rgb(245,169,98))/allocation fill, stat cards (30px/700
amounts, `1 item` count rows, separators), donut sectors + labels +
legend (icons, colors, card chrome), breakdown sections/footers, brand
block, rail geometry, avatar footer, items-view headers/filter
cards/cards/badges/footers/hover buttons, both dialogs (fields, tiles,
358px mobile panels), net-worth tabs/type groups/cards, savings add
gradient, empty-search content, mobile top bar + hamburger + sheet.

**Two new reference mobile bugs measured** (the reference's own pages
scroll sideways at 390×844):

- **R3** — reference `/dashboard`: `scrollWidth` 395 (its `main`,
  flex-1 with `min-width:auto`, renders 395px inside the 390px
  `SidebarProvider` wrapper).
- **R4** — reference `/networth`: `scrollWidth` **464** (its fixed
  `text-5xl` net figure + fixed `grid-cols-2` summary grid).

Both prior reference bugs re-confirmed live (toast-viewport hamburger
block — hit-test top element is the empty container; sheet-stuck-open
after nav — the `bg-black/80` overlay persists after the route change).
The clone's fixes for both re-verified end-to-end on the same probes.

## Six finding groups — `docs/remediation-plan-v4.md`

1. **G1 [MED]** Nav links 40px tall vs the reference's **32px** — the
   reference's shadcn `SidebarMenuButton` carries `h-8`; the clone
   relied on py-2.5 + line-height (40px).
2. **G2 [MED]** Inactive nav hover: the reference tints `hover:bg-green-50`
   (#f0fdf4); the clone used `hover:bg-sidebar-accent` (#f0f2ee — a
   warm gray, visibly different).
3. **G3 [LOW]** Active nav hover: the reference's gradient persists
   (inline style outranks class hovers); the clone dimmed it with
   `hover:opacity-90`.
4. **G4 [MED]** Net-worth summary card: the reference is a **2-col grid**
   (Assets + Liabilities only — `text-xs`/white-70 labels, `text-2xl`
   amounts, `backdrop-filter: blur(10px)`) with the ratio in a separate
   `mt-6 pt-6 border-t border-white/20` footer row (`text-lg` value).
   The clone had a 3-col grid with the ratio as a third card, 20px
   amounts, no blur, no footer row.
5. **G5 [MED — clone bug, superset]** Mobile net-worth overflowed 38px
   (428px in a 390px viewport): the `text-4xl` H2 "−$245,950.00" (an
   unbreakable string — `overflow-wrap: break-word` does NOT reduce
   min-content) + the 64px icon exceeded the mobile content box and
   stretched `main` (flex-1, `min-width:auto`). The reference has the
   same bug at 74px (R4).
6. **G6 [MED — functional]** Items-view header count ignored the active
   filters: the reference recomputes "N items · $X" from the FILTERED
   list ("zzz" → "0 items · $0.00"); the clone rendered the unfiltered
   count ("2 items · $0.00").

## TDD execution

- NEW `tests/e2e/nav-geometry.spec.ts` (3 specs): 32px/h-8 chrome with
  padding/gap/radius assertions, `hover:bg-green-50` on inactive links,
  no `hover:opacity-90` on the active gradient link.
- `tests/e2e/networth.spec.ts` +2 specs: the summary-card structure
  (2 cards, 12px labels, 24px amounts, blur(10px), footer row with a
  computed `1px solid rgba(255,255,255,0.2)` border, 18px ratio) and
  the mobile no-overflow spec (390×844 → `scrollWidth` 390, H2 24px,
  `grid-cols-1 sm:grid-cols-2`).
- `tests/e2e/items.spec.ts` +1 spec: the count follows the search
  ("salary" → "1 items · $5200.00", "zzz" → "0 items · $0.00", clear →
  restored).
- All 6 new specs verified RED first, then implemented:
  - `sidebar.tsx` — `h-8` + `hover:bg-green-50` (inactive) + dropped
    `hover:opacity-90` (active).
  - `net-worth-view.tsx` — the reference summary-card structure with
    `text-2xl sm:text-5xl` + `break-words` + `min-w-0` on the figure
    block, `grid-cols-1 sm:grid-cols-2`, inline rgba border on the
    footer row (Tailwind v4 would emit `border-white/20` as oklab —
    the oklch-drift trap), backdrop blur on the two cards.
  - `app-shell.tsx` — **`min-w-0` on `main`**: the structural superset
    fix (a flex-1 item's automatic minimum size is its content's
    min-content width; pinning it to 0 keeps `main` inside the viewport
    and lets overflow-hidden cards clip gracefully).
  - `items-view.tsx` — `{filtered.length}` in the header count.

Two infra gotchas re-learned: (1) the rebuilt standalone server must
replace the old process — the running server renames itself to
`next-server (v1…)`, so `pkill -f "node .next/standalone/server.js"`
misses it; kill by port/PID, then re-verify the served markup. (2) A
restarted server needs a re-login (new AUTH_SECRET invalidates the
cookie) — and browser-tab caches can serve stale chunks; cache-bust
and confirm the new classes are live before probing.

## Verification

- Full chain: typecheck ✓ · lint ✓ · **96/96 unit** ✓ · build ✓ ·
  **52/52 e2e** (46 prior + 6 new) ✓ · **30/30 smoke** ✓.
- Live parity re-verified on the remediated build against the
  reference: nav links measure 32px/`h-8` with the reference chrome;
  the net-worth summary card matches leaf-for-leaf at desktop (48px
  H2, 12px/70 labels, 24px amounts, blur, 18px footer ratio, computed
  rgba border); mobile `/networth`, `/dashboard`, `/income` all measure
  exactly 390px (the reference: 464/395/390); the income header count
  follows the search ("2 items · $5550.00" → "0 items · $0.00").
- Screenshot catalog regenerated — now 12 shots (the new
  `12-mobile-networth.png` documents superset fix #4; the script also
  now closes the mobile sheet via a nav tap before it).

## Docs alignment

README (superset list +4th item, test counts 96/52, v4 plan row),
CLAUDE.md (stale 87/34 → 96/52, superset phrasing), AGENTS.md (four
pinned superset fixes), SKILL (project_state 96/52, identity §1, new
D-5 row: the flex min-width:auto overflow trap + the
`break-word`-doesn't-shrink-min-content note), `worklog.md`, this
session log, and `remediation-plan-v4.md` itself.
