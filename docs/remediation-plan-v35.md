# Remediation Plan v35 — Session-70 Parity Iteration

Date: 2026-10-10 · Scope: fresh two-site re-audit after the v34 baseline
(`f9168b0` + the session-log commit `54b07f4` on `main`; this session's
re-run of the whole chain green on the FIRST full run: lint ✓ ·
typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**168/168 e2e ✓** · 35/35 smoke ✓). Workspace rebuilt from scratch (the
sandbox was reset — fresh clone, `npm install`, `db/` pushed + seeded at
the repo root, `.env` with `DATABASE_URL="file:../db/custom.db"`);
`scandihaven` re-cloned (the reference-only repo, never compiled).
Probes: the standing disciplines — one-shot `agent-browser eval` (base64
via run-probe.sh for `$`-bearing probes), the :3200 parity server inside
ONE `with-server.sh` invocation, REAL key presses for every
focus-chrome claim, parked-pointer settles, FULL computed strings,
full-settle re-reads, and the v34 `document.hasFocus()` gate before any
`:focus`-computed read.

## The sweep — method and results

The pass swept the three session-70 suggested surfaces — the **item-card
action menus' open-state focus chrome** (the dropdown menu items' focus
families — v29 measured the containers, not the item focus), the
**dashboard quick-action buttons' focus-visible family**, and the
**deep-link/URL contract** (the `?from_url` redirect family, the 404
route's link semantics) — plus the standing re-verification set
(mobile-nav R1–R4 on BOTH sites, data drift, the SEO pair, two VLM
pairs) and the code audit (`npm audit` = the same 5 dev-only ESLint
`braces`/eslint-config-next advisories — accepted, unchanged, dev-only;
the secret-pattern scan clean; `.env.example` verified current).

- **Mobile navigation (the task focus) R1–R4 all re-verified live on BOTH
  sites — the 29th consecutive check.** R1: the reference's `fixed
  top-0 z-[100]` toast containers still intercept the burger's center
  hit (scrollWidth 395), while the clone's burger hit is DIRECT on the
  svg with 390 fit on every route. R2: the reference's sheet still traps
  after nav (structure detector on `/income`: sheet open, body locked);
  the clone's closes (superset fix #2). R3: the reference marks nothing
  active on `/` and has no `<nav>` landmark; the clone highlights
  Dashboard (white/500 text — verified directly this session, the
  bg-filter read was the v34 false-negative) + has the landmark. R4: the
  reference overflows 395 on `/`+`/dashboard` and 464 on `/networth`;
  the clone fits 390 on all six routes. **The Tailwind v4 pins hold —
  the clone's mobile menu works as expected.**
- **Data drift clean (29th)**: the reference census re-verified (its own
  live data: allocation 30.5%, income `$5000.00`/1, savings
  `$1000.00`/1, expenses `$525.00`/4 — unchanged before and after the
  probe cycles; the from_url probe logged in once more with the correct
  password, the menu probes all Escape-closed without selecting). The
  clone's seed census unchanged (62.8% / 5550 / 1250 / 2235).
- **SEO pair ✓** (live, both sites): robots.txt + sitemap.xml live on
  both; the reference's head-metadata census re-captured (title,
  canonical, description, og/twitter pair, apple-mobile-web-app-title —
  all matching the pinned values).
- **Suggestion #1 — the item-card action menu's open-state focus chrome:
  ONE finding (G1 below), everything else byte-identical.** First-time
  REAL-key measurement of the full contract on BOTH sites:
  fresh-open via CLICK lands focus on the menu CONTAINER (`DIV` with
  `role=menu`); fresh-open via ENTER lands focus on the FIRST item —
  both sites identical on both open paths (the first clone probe
  compared its Enter-open against the reference's click-open and
  fabricated a landing difference — resolved by measuring the full
  matrix). ArrowDown/ArrowUp rove the highlight; both arrows from the
  container land on the FIRST item; Home/End jump to the ends; Tab
  while open is TRAPPED (focus stays on the highlighted item, the menu
  survives); Escape closes the menu and returns focus to the trigger.
  The items' focused chrome is the SAME `:focus`-driven accent family
  as the Select options (bg `rgb(245,245,245)` + text
  `rgb(23,23,23)`, no ring — the white/1px #0a0a0a/transparent outline
  slots are style `none`/invisible on both). The trigger: 36×36,
  hover-revealed (`opacity-0` at rest on BOTH sites — the v29 family),
  `aria-haspopup=menu`, no `aria-controls` while closed, and its REAL-Tab
  focus-visible chrome is the shadcn 1px ring family
  (`rgb(255,255,255) 0 0 0 0, rgb(10,10,10) 0 0 0 1px, rgba(0,0,0,0)…`).
  Item geometry 118×32 both. The Edit item's rest + focused colors
  byte-match (rgb(10,10,10) → rgb(23,23,23)). **The drift: the DELETE
  item's FOCUSED text color — see G1.** (The same contract re-measured
  on the reference's net-worth asset card menu: identical — the drift
  exists in the clone's net-worth Delete instances too.)
- **Suggestion #2 — the dashboard quick-action button's focus-visible
  family: NO finding (first-time measurement; the S2 pin below).** The
  reference's "Add Item" header button, REAL-Tab-measured: `:focus` +
  `:focus-visible` engaged, box-shadow
  `rgb(255,255,255) 0px 0px 0px 0px, rgb(10,10,10) 0px 0px 0px 1px,
  rgba(0,0,0,0.1) 0px 1px 3px 0px, rgba(0,0,0,0.1) 0px 1px 2px -1px`
  — the four-layer composite (the v4 white lead + the shadcn 1px
  #0a0a0a ring + the gradient button's two ambient layers), outline
  transparent 2px (v3 outline-none). The clone's button renders the
  BYTE-IDENTICAL composite (the `.zb-btn-add:focus-visible` globals.css
  pin, v11). Rest state: both render the two-layer ambient
  (the reference's two transparent lead slots are v3's compiled-output
  artifact — the visible pixels identical). The family was
  CSS-pinned since v11 and dialog-instance-tested (dialog-buttons.spec)
  but the reference's quick-action surface itself was never measured —
  now measured, identical, and pinned at the dashboard instance (S2).
- **Suggestion #3 — the deep-link/URL contract: NO finding (first-time
  measurement; the S3 pin below).** The reference's login honors
  `?from_url=/income`: after a successful sign-in it lands on `/income`
  (measured live — logout via its `/api/auth/logout` POST, then the
  param'd login). The clone's login lands on `/income` too — identical
  (the v7 pin established the no-param fallback `/`; the param-honoring
  path was never explicitly measured or test-pinned). The 404 route's
  link semantics: the reference's title derivation is path-aware
  (`No Such Route | ZeroBudget` for `/no-such-route` — the clone's
  derivation produces the byte-identical title), h1 "404", the quoted
  path without the leading slash, and the "Go Home" control carries the
  slate-700-on-white family with the plain-`focus:` slate-500 ring
  (v25-pinned). The reference's Go Home is a BUTTON (click →
  client-side navigate to `/`); the clone's is a real `Link href="/"`
  — **a documented superset** (the link is the better semantic:
  middle-click/right-click/crawler-followable; the click behavior
  identical — measured live on both).
- **The VLM pairwise (two fresh pairs, viewport-asserted 1280×800
  before each capture — the v33 lesson)**: the dashboard — VERDICT
  IDENTICAL, flags DOM-explained (the Dashboard-active rail = superset
  #3; the avatar letter + the progress fill = the different demo data,
  text-content excluded); the income page with the action menu OPEN and
  Delete highlighted — VERDICT IDENTICAL, zero flags (the G1
  red-vs-dark text is a 12px color difference below VLM resolution —
  the DOM-level measurement is the authoritative one).
- Probe-methodology lessons: (L1) compare the SAME open path across
  sites (click-open vs Enter-open land focus differently on BOTH —
  a cross-path comparison fabricated a phantom difference this
  session); (L2) the persistent eval scope strikes again — wrap every
  probe body in an IIFE via the base64 run-probe.sh (the `Identifier
  already declared` family); (L3) a "rest" style read AFTER a REAL-Tab
  focus sequence is still a focused read — blur first (the Add Item
  rest-shadow probe initially read the focused composite).

## Findings

### G1. [MEDIUM — parity drift] the action-menu DELETE item's focused text color stays red on the clone

The reference's dropdown Delete items (income/savings card + the
net-worth asset/liability cards) run `text-red-600` at rest with the
base shadcn `focus:text-accent-foreground` — when FOCUSED (arrow-roving
or hover), the accent-foreground utility (specificity 0,2,0 with the
`:focus` pseudo-class) outspecifies the plain red class (0,1,0), so the
highlighted Delete renders `rgb(23,23,23)` — the SAME dark text as the
Edit item, only the accent bg tint behind it. Measured live this
session (REAL ArrowDown roving, `document.hasFocus()` gated):
reference focused Delete = bg `rgb(245,245,245)` + color
`rgb(23,23,23)`; clone focused Delete = bg `rgb(245,245,245)` + color
`rgb(220,38,38)` (RED). The clone's three Delete items carry an
invented `focus:text-[#dc2626]` override — a v5-era hex-migration of
`focus:text-red-600` (commit `db757a2`, the v4 lab-color trap fix) that
was never re-measured against the reference's actual focused color. The
rest-state red is correct (v29 pinned `rgb(220,38,38)` at rest); the
FOCUSED state is the drift. Fix: remove the `focus:text-[#dc2626]`
override from the three spots — the base DropdownMenuItem
`focus:text-accent-foreground` (src/components/ui/dropdown-menu.tsx)
then wins on focus, matching the reference's cascade exactly.

Files: `src/components/budget/item-card.tsx` (~line 142),
`src/components/budget/net-worth-view.tsx` (~lines 91 + 194 — the
asset + liability Delete instances).

### S1. [PIN] the action-menu keyboard contract + the focused Delete family

The session-70 surface #1's measurable contract, now measured and
pinned: fresh-open via click lands focus on the menu container, via
Enter on the first item; both arrows from the container land on the
first item; arrows rove with the accent highlight following; Home/End
jump; Tab is trapped (menu survives, focus stays); Escape closes +
focus returns to the trigger; the focused Delete renders the accent
family (bg `rgb(245,245,245)` + text `rgb(23,23,23)` — the G1 fix
pinned); the trigger's focus-visible is the shadcn 1px #0a0a0a ring
family. A new e2e test in `tests/e2e/tokens.spec.ts` (next to the
existing G5+G9 menu test — the file that already pins the menu's rest
family) pins the contract so a future dropdown-menu or item-card
refactor cannot re-invent the focused Delete tint or break the roving.

### S2. [PIN] the dashboard quick-action button's focus-visible composite

The session-70 surface #2's measurable contract, first-time measured on
the reference and pinned: the "Add Item" header button's focus-visible
box-shadow is the four-layer composite
(`rgb(255,255,255) 0px 0px 0px 0px, rgb(10,10,10) 0px 0px 0px 1px,
rgba(0,0,0,0.1) 0px 1px 3px 0px, rgba(0,0,0,0.1) 0px 1px 2px -1px`)
with v3's outline-none (transparent 2px, offset 2px). No production
change — the `.zb-btn-add:focus-visible` globals.css rule already
emits it; a new e2e test in `tests/e2e/dashboard.spec.ts` (next to the
gradient test) pins the dashboard instance (the dialog instances are
pinned in dialog-buttons.spec.ts since v11 — the quick-action header
instance never was).

### S3. [PIN] the deep-link from_url redirect

The session-70 surface #3's measurable contract, first-time measured on
the reference and pinned: `/login?from_url=/income` + valid
credentials lands on `/income` (the no-param fallback `/` is the v7
pin). No production change — the clone honors the param identically;
a new e2e test in `tests/e2e/auth.spec.ts` (next to the existing
"valid credentials sign in and land on the dashboard" test) pins the
deep-link path (the 404 title derivation + Go Home surface are already
pinned by not-found.spec.ts; the link-vs-button superset documented
above).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | S1 test: the action-menu keyboard contract + focused-Delete (written FIRST — the focused-Delete assertion is RED against the current `focus:text-[#dc2626]`) | test | `tests/e2e/tokens.spec.ts` |
| 2 | G1 fix: remove the `focus:text-[#dc2626]` override (3 spots) → S1 GREEN | fix | `src/components/budget/item-card.tsx`, `src/components/budget/net-worth-view.tsx` |
| 3 | S1 pin-sanity: re-add the override on item-card → the focused-Delete assertion FAILS; restore → GREEN | verify | `src/components/budget/item-card.tsx` |
| 4 | S2 test: the dashboard Add Item's focus-visible four-layer composite (focusVisible technique) | test | `tests/e2e/dashboard.spec.ts` |
| 5 | S2 pin-sanity: strip the `.zb-btn-add:focus-visible` box-shadow → the composite assertions FAIL; restore | verify | `src/app/globals.css` |
| 6 | S3 test: the from_url deep-link redirect (login → /income) | test | `tests/e2e/auth.spec.ts` |
| 7 | The full chain re-run (108 unit · 171 e2e · 35 smoke + lint + typecheck + build) | verify | — |
| 8 | The 16 screenshots regenerated | docs | `docs/screenshots/` |
| 9 | The v35 probes persisted + the probe README updated (the L1–L3 lessons) | docs | `scripts/parity-probes/` |
| 10 | Docs aligned (README v35 row + counts, CLAUDE, AGENTS, SKILL, session_72, the repo worklog Session 68, the workspace worklog) | docs | repo root + `docs/` |
| 11 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `item-card.tsx` line ~142: the Delete DropdownMenuItem carries
  `className="text-[#dc2626] focus:text-[#dc2626]"` — the override the
  G1 fix removes (the rest-red stays; grep confirms the identical
  pattern at net-worth-view.tsx ~91 + ~194).
- `dropdown-menu.tsx` line ~36: the DropdownItem base carries
  `focus:bg-accent focus:text-accent-foreground` — with the override
  removed, the cascade matches the reference's (the focused Delete
  renders #171717 over the accent bg; `--color-accent` = `#f5f5f5`,
  `--color-accent-foreground` = `#171717` per globals.css).
- `tokens.spec.ts`: the existing "dropdown menu hover + destructive item
  match the reference (G5 + G9)" test pins the REST family (Edit
  rgb(10,10,10), Delete rgb(220,38,38), the content border
  rgb(229,229,229), the Edit-focused accent) — the new S1 test extends
  the same surface with the Delete-focused color + the full keyboard
  contract; the file's `main .group` card-scoped hover pattern is the
  established menu-opening idiom.
- `dashboard.spec.ts`: the "renders the page header with the gradient
  Add Item button" test is the S2 insertion point; the
  `focus({focusVisible: true})` programmatic technique is the
  dialog-buttons.spec.ts precedent (real Chromium FocusOptions — TS
  DOM-lib lag needs the cast).
- `auth.spec.ts`: the "valid credentials sign in and land on the
  dashboard" test (line ~152) is the S3 insertion point — the from_url
  variant reuses its fill/submit pattern (+1 real login: the suite's
  login count stays far under the 10/IP/15min bucket).
- `globals.css` line ~245: `.zb-btn-add:focus-visible` emits the exact
  four-layer composite — the S2 pin asserts the dashboard instance's
  computed string; the S2 pin-sanity mutation strips the box-shadow
  declaration.
- The chain gate: lint → typecheck → 108 unit → build → 168 e2e (171
  after S1+S2+S3; all three are new tests) → 35 smoke.
