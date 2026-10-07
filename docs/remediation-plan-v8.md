# Remediation Plan v8 — Session-15 Parity Iteration

> **Status: COMPLETE** — all finding groups fixed TDD-first (specs RED → GREEN);
> full chain green at 96 unit / 92 e2e / 30 smoke; live parity re-verified
> surface-by-surface. See `docs/session_15.md`.

Date: 2026-10-08 · Scope: fresh two-site re-audit after the v7 baseline
(`b8ab563` + `dd09525` + `c6d40fa`) re-verified green (lint · typecheck · 96/96
unit · build · 83/83 e2e · 30/30 smoke). Probes:
`scripts/parity-probes/probe-v8-*.mjs` via `run-probe.sh`, two agent-browser
sessions (`ref8` = live reference, `clone8` = the standalone parity server on
:3200, detached boot — survives across tool calls this session).

This pass re-verified the entire mobile-navigation stack (the task focus) and
then swept the surfaces the v7 pass had *not* measured at computed-style
depth: **every form dialog's footer-button geometry** and **the item-card
badge family's computed colors**. It found **2 clone-side finding groups**
plus one repo-hygiene item; no new reference bugs (R1–R7 all re-confirmed
live: the toast container still swallows the ref's hamburger at
`pointer-events:auto`, its sheet still traps after nav, `/` still marks no
nav item active, its mobile pages still overflow 395px/464px, its dialogs
still ignore Escape AND outside-click, its deletes are still unconfirmed,
and its live data is unchanged since session 11 — income 5000 / savings 1000
/ expenses 525 → `+$3475.00`, 30.5% allocation).

---

## Findings ledger

### G1. [MED] Dialog footers: content-sized right-aligned buttons vs the reference's full-row flex-1 split

Measured live on the reference (budget-item ADD + EDIT, asset, and line-item
dialogs — all identical): the footer is `flex gap-3 pt-4` filling the 624px
content row with **both buttons at `flex-1`** — Cancel ≈ 307px (left half,
white, `rgb(10,10,10)` text, 1px `#e5e5e5` border) and Save Item/Asset ≈ 305px
(right half, per-dialog gradient, white text), h=36. The clone renders
`flex items-center justify-end gap-3` with content-sized buttons — Cancel
**81px** and Save Item **127px** — with no `pt-4` (24px vs the ref's 24+16px
field→button gap). The dialog shells themselves match exactly (672px wide,
sticky 69px header, `p-6 space-y-6` scrolling form), so only the footer row
drifts. Files: `budget-item-dialog.tsx:341`, `line-item-dialog.tsx:231`,
`asset-dialog.tsx:201`, `liability-dialog.tsx:242`. Fix: footer container →
`flex gap-3 pt-4`; Cancel and Save get `flex-1`; the superset Delete link
keeps `mr-auto` (edit mode only) so the pair still splits the remaining row.

### G2. [MED] Remaining lab()/oklab() color-space drifts on parity surfaces

The v5 token block and the v7 login pass pinned most surfaces, but a
targeted computed-color sweep found these named-palette classes still alive
on parity surfaces. In every case the *value* matches the reference (v4
resolves the same hex through Lab space) — the drift is the color space of
the computed style, exactly the pattern AGENTS.md forbids ("never the named
classes on parity surfaces"; lab() also renders differently on
non-color-managed engines and falls back to nothing on browsers without
Lab support):

| Surface | Clone class | Reference (measured live) | Pin |
|---------|------------|---------------------------|-----|
| Inactive rail nav links (`sidebar.tsx:81`) | `text-zinc-700` → `lab(26.8…)` | `rgb(63,63,70)` | `text-[#3f3f46]` |
| Frequency badges (`constants.ts` FREQUENCY_BADGES) | `bg-gray-100 text-gray-700` / `bg-blue-50 text-blue-700` / `bg-purple-50 text-purple-700` / `bg-indigo-50 text-indigo-700` / `bg-pink-50 text-pink-700` | monthly measured: bg `rgb(250,245,255)` text `rgb(126,34,206)` | `bg-[#f3f4f6] text-[#374151]` / `bg-[#eff6ff] text-[#1d4ed8]` / `bg-[#faf5ff] text-[#7e22ce]` / `bg-[#eef2ff] text-[#4338ca]` / `bg-[#fdf2f8] text-[#be185d]` |
| Classification badges (`constants.ts` CLASSIFICATION_BADGES) | `bg-red-50 text-red-700 border-red-200` / `bg-blue-50 text-blue-700 border-blue-200` / `bg-green-50 text-green-700 border-green-200` | need measured: bg `rgb(254,242,242)` text `rgb(185,28,28)` border `rgb(254,202,202)`; want: `rgb(239,246,255)`/`rgb(29,78,216)`/`rgb(191,219,254)`; savings: `rgb(240,253,244)`/`rgb(21,128,61)`/`rgb(187,247,208)` | need `bg-[#fef2f2] text-[#b91c1c] border-[#fecaca]`, want `bg-[#eff6ff] text-[#1d4ed8] border-[#bfdbfe]`, savings `bg-[#f0fdf4] text-[#15803d] border-[#bbf7d0]` |
| Recurring badge (`item-card.tsx:164`) | `bg-green-50 text-green-700` | (recurring=true measured on ref) text `rgb(21,128,61)` | `bg-[#f0fdf4] text-[#15803d]` |
| Status badge (`item-card.tsx:169`) | `bg-slate-50 text-slate-700` | bg `rgb(248,250,252)` text `rgb(51,65,85)` | `bg-[#f8fafc] text-[#334155]` |
| Expense-card hover buttons (`item-card.tsx:85,94`) | Edit `hover:bg-gray-50`, Calculate `text-orange-600 border-orange-200 hover:bg-orange-50` | Calculate measured: color `rgb(234,88,12)` border `rgb(254,215,170)` | `hover:bg-[#f9fafb]`, `text-[#ea580c] border-[#fed7aa] hover:bg-[#fff7ed]` |

Behavior note verified live this pass: the **Recurring card badge is
conditional** on the item's `recurring` flag exactly like the reference (its
dialog "Recurring Item" switch, false on all its current items → no badge;
flipping the switch on the reference's Investments item made the green badge
appear, `rgb(21,128,61)` — then restored). The clone's seed simply marks
some items recurring; the render logic already matches. No code change.

### G3. [LOW] Repo hygiene: stray committed SQLite binary at `prisma/db/custom.db`

`prisma/db/custom.db` (73KB) is tracked in git — a session-1 scaffolding
leftover at the WRONG path. The documented contract is `<repo>/db/custom.db`
(gitignored: "database binaries — recreate with db:push + db:seed"), and
nothing in the code references the prisma/db location (grep-verified; the
db-path contract resolves `file:../db/custom.db` → `<repo>/db/custom.db` for
CLI, build, and runtime). Remove from tracking with `git rm --cached`; the
fresh-checkout story stays `db:push` + `db:seed`. Also verified this session:
`.env.example` matches the codebase exactly (3 vars — DATABASE_URL relative
contract, NEXT_PUBLIC_SITE_URL metadata default, AUTH_SECRET prod HMAC).

### Verified matching this pass (no action)

Mobile navigation (task focus, both sites 390×844): topbar 61px `bg-white
border-b px-6 py-4` + h1 "ZeroBalance" 20px/700/`rgb(26,58,46)`; hamburger
28×28 at (24,16), svg 16px `rgb(10,10,10)`, pad 8px, radius 8px, svg
flex-shrink 0 — **identical**, with the ref's hit-test BLOCKED by its toast
container (R1) and the clone's DIRECT; sheet 288×844 `rgb(250,250,250)` +
1px `rgb(229,229,229)` right border + `rgba(0,0,0,0.8)` overlay — identical;
R2 sheet-trap and R4 overflow (395px/464px vs 390px) re-confirmed live.
Desktop rail: 256px, brand 40×40 forest-gradient tile + 24px white
lucide-target + `text-lg` 18px H2, label y=113, links x=20 y=145/185/225/…
h=32, active link gradient `135deg rgb(45,90,74)→rgb(143,188,63)` + white
500-weight text. Login page: every v7 pin still matches the reference
(h1 30px `rgb(15,23,42)`, card `rgba(255,255,255,0.95)`, Sign-in bg
`rgb(15,23,42)` h48, links 14px/20px `rgb(100,116,139)`, input border
`rgb(226,232,240)` bg `rgba(248,250,252,0.5)`). 404 (title
"Nonexistent V8 Check | ZeroBudget", quoted-path message, Go Home) and the
head metadata set (description/OG/Twitter/canonical/manifest/apple).
Calculator dialog buttons 110/141px content-sized — identical both sides.
Dialog shells 672px with sticky 69px header + scrolling `p-6 space-y-6`
form — identical. Reference data state unchanged since session 11.

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | G1 dialog footer flex-1 split | extend `dialog-buttons.spec.ts`: footer container `flex`, gap 12px, pt 16px; Cancel + Save widths ≥ 300px each in the budget ADD dialog; line-item dialog Save ≥ 300px; asset dialog Cancel/Save ≥ 300px (RED first) | `budget-item-dialog.tsx`, `line-item-dialog.tsx`, `asset-dialog.tsx`, `liability-dialog.tsx` |
| 2 | G2a nav link hex pin | extend `nav-geometry.spec.ts`: inactive link color computes `rgb(63, 63, 70)` (not lab) | `sidebar.tsx` |
| 3 | G2b badge map hex pins | NEW `badge-colors.spec.ts`: monthly badge bg `rgb(250,245,255)` + color `rgb(126,34,206)`; need badge bg/color/border `rgb(254,242,242)`/`rgb(185,28,28)`/`rgb(254,202,202)`; active badge `rgb(248,250,252)`/`rgb(51,65,85)`; Recurring badge color `rgb(21,128,61)` (seed item); Calculate button color `rgb(234,88,12)` + border `rgb(254,215,170)` | `constants.ts`, `item-card.tsx` |
| 4 | G3 remove stray `prisma/db/custom.db` from git | — (repo hygiene; `db-path.test.ts` already pins the resolution contract) | git index only |
| 5 | Docs: session_15 log, worklog, README/AGENTS/CLAUDE/SKILL alignment (footer pattern + hex-pin ledger + hygiene note) | — | docs |
| 6 | Regression: full chain + live parity re-check of every fixed surface + screenshot catalog | — | — |

## Regression pin map (must NOT change)

- All six superset fixes (hamburger hit, sheet close-on-nav, root-URL nav
  highlight, no mobile overflow, Escape close, delete confirmations) — all
  re-verified live this pass on both sites
- The dialog chrome pins that DO match (672px shell, sticky header, field
  geometry incl. the 624px full-row spans, outline-Cancel/gradient-Save
  colors + Save icons, plain-text menus) — only the footer row layout changes
- Money two-formatter contract, breakdown drill-down, donut order/icons,
  stat cards, hero states, per-surface add gradients, calculator
  server-side recalc, seed arithmetic, empty-state pattern
- The v5 token block, `@variant hover` pin, tab grid, login slate pins,
  mobile toggle/sheet pins, custom 404, head metadata
- e2e fixture discipline: every spec restores what it mutates
