# Session 13 — Fresh Verification & Parity Iteration v7

**Date:** 2026-10-07 · **Baseline:** `7295906` (session-12 = session-11's
narrative record) · **Outcome:** 8 finding groups fixed TDD-first —
**96/96 unit · 83/83 e2e · 30/30 smoke**, live parity re-verified.

## Baseline re-verification

Workspace was RESET this session — re-cloned `nordeim/zero-balance` fresh into
`/home/z/my-project/zero-balance`, re-created `.env`
(`DATABASE_URL="file:../db/custom.db"`), `db/` at the repo root, `db:push` +
`db:seed` (the sandbox still exports its polluting absolute `DATABASE_URL` —
the npm scripts' `env -u` discipline handled it untouched). Read the full doc
chain (AGENTS → CLAUDE → README → PAD → SKILL → session_11 → plan v6 →
worklog → session_12), spot-checked the structure against the docs (7 routes,
14 budget components, 15 lib seams, 8 unit files, 15 e2e specs, probe
infrastructure incl. `with-server.sh`), then ran the whole chain at HEAD:

**lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ · 73/73 e2e ✓ · 30/30
smoke ✓** — the v6 baseline confirmed intact.

## The v7 audit — surfaces no prior session had covered

Two browser sessions (`ref7` = live reference, `clone7` = the standalone
parity server on :3200 through `with-server.sh`). Fresh angles: the **login
page's full computed chrome** (it turned out to be the last surface still
styled with named slate classes), the **rail brand block**, the **mobile
topbar toggle**, the **sheet border/overlay colors**, the **404 page**, and
the **document head**. Plus the explicit mobile-navigation re-check the task
demands.

**Mobile nav verification (task focus):** R1 re-confirmed live — the ref's
empty toast container (`fixed top-0 z-[100] w-full`, h=32, `pointer-events:
auto`) swallowed the first real click on its hamburger (had to JS-click to
open its sheet); the clone's hamburger takes a real click. R2 re-confirmed —
after tapping Income in the ref's sheet the URL changed but the sheet stayed
open (`sheetOpen: true` behind the overlay); the clone's sheet closed on nav
(`url: /income, sheetOpen: false`). R4 re-confirmed — the ref's /income page
still scrolls to 395px at 390; the clone fits exactly. Both clone superset
fixes remain live and pinned.

**Findings ledger (8 groups, `docs/remediation-plan-v7.md`):**

- **G1 [MED]** post-login redirect: ref lands on `/` (root renders the
  dashboard); clone pushed `/dashboard`. Fixed the `?from_url=` fallback in
  both spots; flipped the e2e pin.
- **G2 [HIGH]** login surface: every named slate class computed as `lab()`
  (h1 `#0f172a`, Sign-in bg, links/subtitle/icons `#64748b`, labels/Google
  `#334155`, input border `#e2e8f0`, bg `rgba(248,250,252,0.5)`, card
  `bg-white/95` → oklab, the page gradient slate-50→100 → lab stops — the
  documented oklab-gradient trap was alive on this page), AND the footer
  links were missing `text-sm` (16px/24px vs the ref's 14px/20px). Full
  hex-pin pass over all three states + inline gradients.
- **G3 [LOW]** (corrected during validation): the logo halo ring was NOT
  missing — the initial probe's 60-char `boxShadow` slice read only the
  transparent offset layers (SKILL lesson 12.13). Real drift: the ring
  computed `oklab(0.999…/0.5)` vs the ref's `rgba(255,255,255,0.5)`. Fixed
  with a sibling `.zb-logo-ring` layer — an inline boxShadow on the span
  would have overridden its `shadow-lg`/`group-hover:shadow-xl` (lesson 12.14).
- **G4 [MED]** rail brand: the ref renders a 24px white lucide-target in the
  40×40 forest-gradient tile + the H2 at `text-lg` (18px); the clone had a
  hand-rolled 20px target + `text-base` — its whole rail below sat 4px high
  (label y 109 vs 113). Now `TargetIcon h-6 w-6` + `text-lg` + the ref's
  `div.w-full.text-sm` ul wrapper + label ring classes. Post-fix: label
  y=113, first link y=145 — exact.
- **G5 [MED]** mobile toggle: the ref's 16px panel-left icon survives the
  padded 28px box via `[&_svg]:size-4 [&_svg]:shrink-0`; the clone's icon
  was flex-squeezed to 12px and colored forestDark. Now 16px `#0a0a0a` with
  the shrink pin (lesson 12.15).
- **G6 [LOW]** sheet: border `#e5e7e3` → the ref's shadcn neutral
  `#e5e5e5`; overlay `bg-black/80` → oklab → inline `rgba(0,0,0,0.8)`.
- **G7 [MED]** the clone shipped Next's default 404; the ref has a branded
  one (h1 404 `text-7xl font-light text-slate-300`, the 2×64px divider bar,
  h2 "Page Not Found", the quoted-path message, white outline Go Home →
  root, tab title "Nonexistent Page Xyz | ZeroBudget"). Built
  `src/app/not-found.tsx` (client, hex-pinned) with the path read from
  `window.location` (leading slash stripped) via lazy-init +
  `suppressHydrationWarning`, and the title set in an effect.
- **G8 [MED]** head parity: the ref ships its marketing description
  verbatim, OG + Twitter cards, canonical, `manifest.json` and the apple
  meta set. Added all of it to `layout.tsx` keyed off `NEXT_PUBLIC_SITE_URL`
  + `public/manifest.webmanifest` (local favicon, never the ref's hosted
  storage).

Also audited and verified MATCHING (no action): the dashboard sweep (hero
gradient/radius/padding, Add-Item gradient, white-alpha labels, stat
structure), mobile login geometry (logo 80px, card 358px at 390), mobile
income view, net-worth tabs/ratio/figure, rail geometry, sheet geometry,
close-button display:none on BOTH sides, and the reference's data state
(unchanged since session 11: 5000/1000/525 → +$3475.00, 30.5%).

## TDD execution

13 specs RED first (`auth.spec` redirect flip; NEW `login-parity.spec` ×5;
NEW `not-found.spec` ×4; `nav-geometry` +1 brand block;
`mobile-navigation` toggle + sheet assertions folded into two existing
tests). Implementation across `login-card.tsx`, `sidebar.tsx`,
`ui/dialog.tsx`, NEW `app/not-found.tsx`, `layout.tsx`,
`public/manifest.webmanifest`. Mid-flight corrections — three instructive
spec/impl co-adjustments: the INPUT template-literal class string (Tailwind
scans source text — never interpolate class values), the G3 sibling-layer
structure, and the 404's leading-slash strip. **83/83 e2e green** (73 + 10
net-new).

## Verification & docs

Full chain: lint · typecheck · **96/96 unit** · build · **83/83 e2e** ·
**30/30 smoke**. Live parity re-verified surface-by-surface on :3200 — the
login card now measures identical to the ref on every pinned value (h1
`rgb(15,23,42)`, Sign-in `rgb(15,23,42)`/48px, Google `rgb(51,65,85)`/54px,
links 123×20/14px, gradients plain-rgb stops, halo rgba plain), the rail
label/link y-positions are exact (113/145), the toggle reads 16px
`rgb(10,10,10)`, the sheet borders `#e5e5e5` + `rgba(0,0,0,0.8)` overlay,
the head carries the ref's description/OG/Twitter/canonical/manifest/apple
meta, and a real login flow lands on `http://localhost:3200/`.

Screenshots: the capture script gained shot 13 (the 404) and its post-login
wait flipped to the root URL; db re-seeded, full 13-shot catalog
regenerated, seed arithmetic verified intact afterwards by the smoke suite.

Docs aligned: README (counts 83, plan-v7 row, 13-shot set), CLAUDE.md
(counts, env-table note), AGENTS.md (v7 pin paragraph + the slate trap
example), SKILL (state 96/83/30, lessons 12.13–12.15, Appendix B rows),
probe README (v7 catalog), this session log, and `worklog.md`.
