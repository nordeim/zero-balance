# Remediation Plan v7 — Session-13 Parity Iteration

> **Status: COMPLETE** — all 8 finding groups fixed TDD-first (6 new/extended
> spec groups, RED→GREEN); full chain green at 96 unit / 79 e2e / 30 smoke;
> live parity re-verified surface-by-surface. See `docs/session_13.md`.

Date: 2026-10-07 · Scope: fresh two-site re-audit after the v6 baseline
(`42f50da` + `7295906`) re-verified green (typecheck · lint · 96/96 unit ·
build · 73/73 e2e · 30/30 smoke). Probes: `scripts/parity-probes/probe-v7-*.mjs`
via `run-probe.sh` + the per-command `with-server.sh` parity server on :3200.

This pass audited the surfaces no prior session had touched: the **login
page's full computed chrome** (every slate color, the gradient, the logo
ring), the **sidebar brand block** (icon size + logo type size), the
**mobile topbar toggle**, the **mobile sheet border/overlay colors**, the
**custom 404 page**, and the **document head** (description, OG/Twitter
cards, canonical, manifest, apple meta). It found **8 clone-side finding
groups**; no new reference bugs (R1–R7 all re-confirmed live: the toast
container still covers the ref's hamburger at `pointer-events:auto`, its
sheet still traps after nav, `/` still marks no nav item active, its mobile
pages still overflow 395px, its dialogs still ignore Escape AND
outside-click, its deletes are still unconfirmed, and its live data is
unchanged since session 11 — income 5000 / savings 1000 / expenses 525 →
`+$3475.00`, 30.5% allocation).

---

## Findings ledger

### G1. [MED] Post-login redirect: the reference lands on `/`, not `/dashboard`
Measured live: after a successful sign-in the reference's URL is
`https://zero-balance-4885a8f3.base44.app/` (root — which renders the
dashboard); the clone pushes `/dashboard` (`login-card.tsx:237` fallback
`"/dashboard"` and line 273's invalid-fromUrl fallback). Both render the
dashboard, but the URL is a visible parity surface. Fix: default fallback
`"/"` in both spots (keep `?from_url=` handling). The e2e pin
(`auth.spec.ts:145` `toHaveURL(/\/dashboard$/)`) must flip to `/` — the
reference's behavior is the source of truth.

### G2. [HIGH] Login surface: slate named-class lab/oklab drift + missing text-sm
The login page is the ONE surface still styled with named slate classes —
the exact pattern `AGENTS.md` forbids on parity surfaces (v4 computes them
in Lab color space while the reference emits plain rgb/rgba). Measured
(reference → clone):
- h1 "Welcome to ZeroBudget": `rgb(15,23,42)` → `lab(7.78…)` (text-slate-900)
- Sign-in button bg: `rgb(15,23,42)` → `lab(7.78…)` (bg-slate-900)
- Footer links + subtitle + mail/lock icons + "or" divider: `rgb(100,116,139)`
  → `lab(48.08…)` (text-slate-500)
- Labels + Google button text: `rgb(51,65,85)` → `lab(26.95…)` (text-slate-700)
- Inputs: border `rgb(226,232,240)` → `lab(91.73…)`, bg
  `rgba(248,250,252,0.5)` → `oklab(0.983…/0.5)`
- Card: `rgba(255,255,255,0.95)` → `oklab(0.999…/0.95)` (bg-white/95)
- Page gradient: `linear-gradient(to right bottom, rgb(248,250,252),
  rgb(241,245,249))` → lab() both stops (the documented oklab-gradient trap;
  globals.css mandates inline gradients but the login page still uses
  `bg-gradient-to-br from-slate-50 to-slate-100`)
- Top accent bar gradient: `rgb(226,232,240) → rgb(203,213,225) →
  rgb(226,232,240)` → lab() stops
- ALSO: the footer links are MISSING `text-sm` — 16px/24px-high vs the
  reference's 14px/20px (the only geometry diff on the surface).
Pin every value with arbitrary hex / inline styles per the convention
(slate-900 `#0f172a`, 800 `#1e293b`, 700 `#334155`, 600 `#475569`,
500 `#64748b`, 400 `#94a3b8`, 300 `#cbd5e1`, 200 `#e2e8f0`, 50 `#f8fafc`).
Files: `login-card.tsx` (all three states share the classes).

### G3. [LOW] Login logo ring color computes as oklab (not a missing ring)
> Correction during plan validation: an initial probe sliced boxShadow at 60
> chars and read the transparent ring-offset layers — the 4px ring DOES
> render (the existing auth spec pins it). The drift is the COLOR SPACE:
the reference renders `rgba(255,255,255,0.5) 0 0 0 4px`; the clone's
`ring-white/50` computes `oklab(0.99999… / 0.5)`. Fix: replace the ring
color class with the arbitrary `ring-[rgba(255,255,255,0.5)]` (keeps
`ring-4`, `shadow-lg` and the hover shadow composing). File:
`login-card.tsx` LogoMark.

### G4. [MED] Sidebar brand block: 24px lucide-target + text-lg logo
Measured: the reference renders the rail logo block as a 40×40
forest-gradient tile containing a **24px lucide-target**
(`w-6 h-6 text-white`, stroke=currentColor) + the "ZeroBalance" H2 at
**`text-lg` 18px** (row 44px tall → the "Navigation" label sits at y=113).
The clone hand-rolls a **20px** target and uses **`text-base` 16px** (row
40px → label at y=109; every rail element below is 4px high). The container,
gap, border, and footer all match. Also for structural fidelity: the
reference wraps the nav ul in `div.w-full.text-sm` and its label carries
shadcn focus/collapse classes (invisible). Fix: lucide `TargetIcon`
`h-6 w-6` white + `text-lg` on the H2 + the ul wrapper + label ring classes.
File: `sidebar.tsx` (BrandMark + NavList).

### G5. [MED] Mobile topbar toggle: icon squeezed to 12px, wrong color
Reference toggle: 28×28 button, **16px panel-left icon, near-black
`rgb(10,10,10)`**, `hover:bg-green-50` (#f0fdf4) + `hover:text-accent-foreground`,
`p-2 rounded-lg`, and critically `[&_svg]:size-4 [&_svg]:shrink-0` — the
**shrink-0** is what keeps the icon at 16px inside the padded 28px box.
The clone's icon (h-4 w-4, no shrink-0) is flex-squeezed to **12px** and
pinned forestDark `rgb(26,58,46)`. Fix: add the svg shrink-0/size pin +
near-black color + the hover text class on the toggle. File:
`sidebar.tsx` MobileTopbar.

### G6. [LOW] Mobile sheet: border + overlay color drift
Reference sheet: `border-right 1px rgb(229,229,229)` (neutral #e5e5e5 — the
shadcn sheet border, NOT the warm card border #e5e7e3 the clone pins) and
overlay `rgba(0,0,0,0.8)` — the clone's `bg-black/80` computes as
`oklab(0 0 0 / 0.8)` (v4 alpha drift). Fix: sheet borderColor
`rgb(229,229,229)`; overlay inline `rgba(0,0,0,0.8)`. File:
`src/components/ui/dialog.tsx` SheetContent.

### G7. [MED] Custom 404 page (the clone ships Next's default)
Reference `/nonexistent-page-xyz`: title `Nonexistent Page Xyz | ZeroBudget`;
`main.min-h-screen.flex.items-center.justify-center.p-6.bg-slate-50`
(`rgb(248,250,252)`) → `div.max-w-md.w-full` → `div.text-center.space-y-6`:
- `h1.text-7xl.font-light.text-slate-300` "404" (72px/300, `rgb(203,213,225)`)
- `div.h-0.5.w-16.bg-slate-200.mx-auto` divider (2×64px `rgb(226,232,240)`)
- `h2.text-2xl.font-medium.text-slate-800` "Page Not Found" (24px/500,
  `rgb(30,41,59)`)
- `p.text-slate-600.leading-relaxed` `The page "nonexistent-page-xyz" could
  not be found in this application.` (16px `rgb(71,85,105)`, the quoted path
  in a `span.font-medium.text-slate-700` `rgb(51,65,85)`)
- Go Home: `inline-flex items-center px-4 py-2 text-sm font-medium
  text-slate-700 bg-white border border-slate-200 rounded-lg
  hover:bg-slate-50 hover:border-slate-300` (38px tall, 8px radius) with a
  16px mr-2 lucide icon, navigates to `/`.
The clone renders Next's default "404 This page could not be found." Build
`src/app/not-found.tsx` with the reference's structure (hex-pinned slate
colors), a Go Home link to `/`, and a small client title component
(`<NotFoundTitle>` setting `document.title` to the Title-Cased path +
" | ZeroBudget" — mirrors the reference's dynamic title). Home link → `/`
(the dashboard route).

### G8. [MED] Document head parity: description, OG/Twitter, canonical, manifest, apple meta
The reference's head (measured): description "Your personal zero-budget
planner to manage income, savings, and expenses effortlessly. Achieve
financial clarity and meet your goals with intuitive tools and a clear net
zero overview. Also features a handy Net Worth Calculator."; OG
(og:title "ZeroBudget", og:description, og:type website, og:url, og:image)
+ twitter:title/description/card summary_large_image/image/url; canonical
`<link>`; `manifest.json`; `mobile-web-app-capable yes`;
`apple-mobile-web-app-status-bar-style black`; `apple-mobile-web-app-title
ZeroBudget`. The clone ships only title + its own description. Fix
`src/app/layout.tsx` metadata (openGraph + twitter objects keyed off
`NEXT_PUBLIC_SITE_URL`, alternates.canonical, appleWebApp meta) + add
`public/manifest.webmanifest` (name ZeroBudget, standalone, the local logo
as icon, theme `#fafaf8`/`#1a3a2e`) + link it via `metadata.manifest`. The
favicon stays the clone's own local logo (never hotlink the reference's
supabase storage). Also pin the reference's description text verbatim.

### Verified matching this pass (no action)
Dashboard sweep at 1280 (h1, Add-Item gradient button `135deg
rgb(45,90,74)→rgb(143,188,63)`, hero `135deg rgb(26,58,46) 0% →
rgb(45,90,74) 100%` / 16px radius / 32px padding, white-alpha labels,
stat-card structure, guidelines present); mobile login (logo 80px, h1
24px, card 358px at 390px — the clone's responsive logo/ring sizing
matches); mobile income view (390 fit, header row, search 308×36,
placeholder); net-worth tabs (220×28, active `rgb(220,252,231)` /
`rgb(20,83,45)`), ratio `0.21:1`/`∞:1`, 48px figure; rail geometry
(256px, border 1px rgb(229,231,227), scroll p-3 + inner p-2, label/links
x=20 w=215, brand x=76 y=24); sheet geometry (288×844, z-50, bg
rgb(250,250,250), close buttons display:none BOTH sides); the clone's
mobile-nav superset fixes re-verified live (sheet closes on nav; hamburger
clickable; no horizontal overflow).

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | G1 post-login redirect → `/` | flip `auth.spec.ts:145` to `/` (RED first) | `login-card.tsx` |
| 2 | G2 login slate hex pins + `text-sm` links | NEW `login-parity.spec.ts`: links 14px/20px, Sign-in bg rgb(15,23,42), card rgba(255,255,255,0.95), page gradient stops rgb(248,250,252)/rgb(241,245,249), h1 color, input border/bg, label color | `login-card.tsx` |
| 3 | G3 logo ring color pin | same spec (or reuse auth.spec's shadow regex with a stricter rgba assert): logo wrap boxShadow contains `rgba(255, 255, 255, 0.5) 0px 0px 0px 4px` exactly | `login-card.tsx` |
| 4 | G4 brand block 24px target + text-lg + ul wrapper | extend `nav-geometry.spec.ts`: brand svg 24×24, logo computed 18px, ul parent `w-full text-sm` | `sidebar.tsx` |
| 5 | G5 toggle icon 16px near-black + shrink-0 | extend `mobile-navigation.spec.ts`: toggle svg 16px + color rgb(10,10,10) | `sidebar.tsx` |
| 6 | G6 sheet border + overlay | extend `mobile-navigation.spec.ts`: sheet borderRight rgb(229,229,229), overlay bg rgba(0,0,0,0.8) (assert it parses as rgb(0,0,0) with 0.8 alpha — NOT oklab) | `dialog.tsx` |
| 7 | G7 custom 404 | NEW `not-found.spec.ts`: /nonexistent-page-xyz → h1 404 + h2 "Page Not Found" + quoted-path message + Go Home → `/` dashboard + title suffix " \| ZeroBudget" | NEW `not-found.tsx`, `layout.tsx` |
| 8 | G8 head metadata | same spec (or `metadata.spec.ts`): description meta, og:title property, canonical link, manifest link, apple-mobile-web-app-title | `layout.tsx`, NEW `public/manifest.webmanifest` |
| 9 | Docs: session_13 log, worklog, README/AGENTS/CLAUDE/SKILL alignment (login hex-pin note, 404 page, metadata) | — | docs |
| 10 | Regression: full chain + live parity re-check of every fixed surface + screenshots | — | — |

## Regression pin map (must NOT change)

- All six superset fixes (hamburger hit, sheet close-on-nav, root-URL nav
  highlight, no mobile overflow, Escape close, delete confirmations) — all
  re-verified live this pass on both sites
- Money two-formatter contract, breakdown drill-down, donut order/icons,
  stat cards, hero states, per-surface add gradients, badge maps, type
  grouping, ratio format, calculator server-side recalc, seed arithmetic
- The v5 token block, `@variant hover` pin, tab grid, outline Cancellations,
  gradient Saves with lucide Save icons, plain-text action menus, reference
  empty-state pattern, padding-outside-max-w column
- e2e fixture discipline: every spec restores what it mutates
