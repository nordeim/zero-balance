# Remediation Plan v38 — The A11y Tooling Pass + the Expenses Frequency Filter + the Savings Filter-Card Instance

Date: 2026-10-11 · Scope: fresh two-site re-audit after the v37 baseline
(`aee5a37` + the session-log commits `c035106`/`bac2246` on `main`; this
session's re-run of the whole chain green on the FIRST full run: lint ✓ ·
typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**177/177 e2e ✓ (3.2m)** · 35/35 smoke ✓; npm audit = the same 5 dev-only
ESLint `braces` advisories — accepted, unchanged, dev-only; the
secret-pattern scan clean; `.env.example` verified current, keys matching
`.env`). Workspace intact this session (no re-clone needed): `db/custom.db`
at the repo root, `DATABASE_URL="file:../db/custom.db"`, node_modules
present. `@axe-core/playwright` 4.13.0 added as a devDependency this
session (the a11y tooling pass below). Probes: the standing disciplines —
one-shot `agent-browser eval` (base64 via run-probe.sh), the :3200 parity
server inside ONE `with-server.sh` invocation, REAL key presses and REAL
hovers for every focus/hover claim, parked-pointer settles, FULL computed
strings, and the v34 `document.hasFocus()` gate before any `:focus`-
computed read (now formalized as the shared hasfocus-gate.sh helper —
T2 below).

## The sweep — method and results

The pass swept the three v38 surfaces — **the a11y tooling pass** (the
longest-open queue item, open since session 72: the
`document.hasFocus()` probe helper + the a11y audit CI step),
**the /expenses frequency-filter option census** (the payment-method
sibling, never measured live), and **the /savings filter-card instance**
(the third items-view instance) — plus the standing re-verification set
(mobile-nav R1–R4 on BOTH sites, data drift, the SEO pair, one VLM pair)
and the code audit (unchanged from v37: the same 5 dev-only advisories).

- **Mobile navigation (the task focus) R1–R4 all re-verified live on BOTH
  sites — the 32nd consecutive check.** R1: the reference's toast
  containers still intercept the burger's center hit
  (`DIV.fixed.top-0.z-[100]`, scrollWidth 395); the clone's hit DIRECT on
  the svg, fits 390. R2: the reference's sheet still traps after nav
  (sheet open, body locked); the clone's closes (superset #2). R3: the
  reference marks nothing active on `/` and has no `<nav>`; the clone has
  the landmark. R4: the reference overflows 395 on `/`+`/dashboard`;
  the clone fits 390 on all routes. **The Tailwind v4 pins hold — the
  mobile menu works as expected.**
- **Data drift clean (32nd)**: the reference's census re-verified BEFORE
  and AFTER all probes (allocation 30.5%, income `$5000.00`, savings
  `$1000.00`, expenses `$525.00` — unchanged; read-only throughout: the
  frequency probe Escape-closed then reset its selection to All, the
  savings category probe reset to All, the a11y scans inject + read only).
  The clone's seed census unchanged (62.8% / 5550 / 1250 / 2235).
- **SEO pair ✓** (live, both sites): robots.txt (allow-all + the sitemap
  line) + sitemap.xml (five URLs, priority 1.0/0.8, weekly) live on both;
  the reference's sitemap still capitalizes its app-route URLs (`/Income`,
  `/Savings`) while the clone mirrors its own lowercase routes (the
  documented v21 decision).
- **Suggestion #1 — the a11y tooling pass (the headline, open since
  session 72): the clone is a structural a11y SUPERSET of the reference,
  measured with axe-core 4.13 on BOTH sites** (the wcag2a/2aa/21a/21aa
  tag sets, desktop 1280×800, the booted state; `scripts/parity-probes/
  a11y-scan-v38.mjs` + `axe-detail-v38.mjs`/`axe-detail-ref-v38.mjs`):
  - **The reference FAILS two structural rule families the clone PASSES**:
    `button-name` (CRITICAL — 3 nodes per items view: its two/three Select
    triggers `button[aria-controls=…]` and its card kebab `#radix-…` carry
    NO accessible name; the clone's aria-label superset covers every
    trigger) and `svg-img-alt` (SERIOUS — 3 nodes on `/`+`/dashboard`: its
    recharts donut sectors `path[name="Need"/"Savings"/"Want"]` are
    exposed as image roles without alt; the clone's donut is INERT —
    recharts 3 `accessibilityLayer={false}`, the v31 pin).
  - **The clone fails ONLY `color-contrast` — and every flagged node maps
    1:1 to the reference's own failure with a byte-identical color.** The
    full node-by-node enumeration (both sites): the 3 breakdown section
    rows (lime `rgb(143,188,63)` / blue `rgb(59,126,161)` / orange
    `rgb(224,122,59)`), the hero status label (`rgb(245,169,98)`), the
    50/30/20 guideline amounts (the same 3 type colors), the stat-card
    rows (the type colors + one `rgb(107,114,128)` sublabel on a tinted
    card), the item-card amounts (the type accents — the reference's
    `/income` flags 1 node because its demo income has ONE card, the
    clone's 2 — data-level), the net-worth inactive Liabilities tab
    (`rgb(115,115,115)` on the tinted tablist) + asset card amounts, and
    the 404 `h1` (`rgb(203,213,225)`). All 7 colors are the reference's
    own measured palette — parity-pinned design, not drift.
  - **/savings and /login scan CLEAN on both sites** (0 violations).
- **Suggestion #2 — the /expenses frequency filter: NO drift (first-time
  live measurement of the second Select; the S1 pin below).** The trigger
  chrome 216×36 ("All Frequencies") on BOTH sites (the clone carries the
  aria-label superset). The option list is a STATIC 7-option list —
  byte-identical on BOTH sites: "All Frequencies" (selected) + One-time +
  Weekly + Bi-weekly + Monthly + Quarterly + Annually — the SAME static
  list the v34 pin covered in the sub-dialog instance. Round-trip on the
  reference: "One-time" → 0 cards + "0 items · $0.00" (its demo expenses
  are all recurring frequencies — data-level), reset → its 4 cards.
  Round-trip on the clone: "Weekly" → the Groceries card + "1 items ·
  $320.00", reset → 3 cards + "3 items · $2235.00". The contract shape is
  identical; the difference is demo data only.
- **Suggestion #3 — the /savings filter-card instance: NO drift
  (first-time live measurement of the third items-view instance; the S2
  pin below).** The filter card on BOTH sites: white `rgb(255,255,255)`,
  radius 16px, border `rgb(229,231,227)`, padding 24px, 960×86; the
  search input 447×36 with the placeholder "Search savings items..."
  (border `rgb(229,229,229)`, the ambient-only rest shadow — the O1
  invisible-lead note applies); TWO comboboxes ("All Categories" +
  "All Frequencies", 216×36 each); the 4-column grid (4 × 215.5px —
  md:grid-cols-4 with the search spanning 2). The category round-trip:
  the reference's options = All + "Emergency Fund" (its demo savings has
  ONE item — data-level; picking it → its 1 card); the clone's options =
  All + Emergency Fund + Investments (its 2 categories — data-level
  richer), "Emergency Fund" → 1 card + "1 items · $800.00", reset → 2
  cards + "2 items · $1250.00". The reference's search input carries NO
  aria-label; the clone's does (the superset, same as /income).
- **The VLM pairwise (one fresh pair, viewport-asserted 1280×800)**: the
  /savings view — VERDICT DIFFERENT with ALL four flags DOM-explained
  (1 card vs 2 = the demo data; the reference's Emergency Fund carries a
  red "need" tag vs the clone's green "savings" + Recurring tags = the
  demo items' classification values, data-level; the footer
  Brokerage/Bank Account chips = the clone's seed carrying paymentMethod
  values the reference's items lack [data-level]; the avatar letter U vs
  D = the different demo users). Zero unexplained visual drift.

## Findings

### F1. [SUPERSET — pinned] the clone's a11y gate

The clone passes the two structural rule families the reference fails
(`button-name`, `svg-img-alt`) and its only failures are the reference's
own parity-pinned contrast colors. This session pins that state as a
permanent e2e gate (`tests/e2e/a11y.spec.ts`): every app route scanned
with axe (wcag2a/2aa/21a/21aa) under TWO gates — GATE 1 (structural):
no violation id other than `color-contrast` may appear; GATE 2
(provenance): every color-contrast node's computed color must be one of
the 7 reference-measured palette colors
(`rgb(143, 188, 63)`, `rgb(59, 126, 161)`, `rgb(224, 122, 59)`,
`rgb(245, 169, 98)`, `rgb(107, 114, 128)`, `rgb(203, 213, 225)`,
`rgb(115, 115, 115)`). The login page asserts ZERO violations (no
allow-list). This is the "a11y CI step" from the session-72 queue —
there is no hosted CI, so the local clean-check gate (`npm run
test:e2e`) IS the CI step; AGENTS.md/CLAUDE.md document it.

### S1. [PIN] the /expenses frequency filter's option census + round-trip

The second Select's measurable contract, first-time measured live on
both sites and pinned: the trigger ("All Frequencies", 216×36, the
aria-label superset) opens a STATIC 7-option listbox byte-identical to
the reference's (All Frequencies + One-time + Weekly + Bi-weekly +
Monthly + Quarterly + Annually); selecting "Weekly" narrows the cards to
the Groceries card + recomputes the header ("1 items · $320.00");
resetting to "All Frequencies" restores the three cards ("3 items ·
$2235.00"). A new e2e test in `tests/e2e/items.spec.ts` (in the expenses
describe, after the v37 S3 test) drives the round-trip with REAL clicks
and restores the fixture.

### S2. [PIN] the /savings filter-card instance + the category round-trip

The third items-view instance's measurable contract, first-time measured
live on both sites and pinned: the white rounded-2xl filter card (bg
`rgb(255,255,255)`, radius 16px, border `rgb(229,231,227)`, padding
24px) with the search input (447×36, placeholder "Search savings
items...", the aria-label superset) + the two comboboxes ("All
Categories" / "All Frequencies", 216×36 each) in the 4-column grid; the
category filter's dynamic options (All + the seed's Emergency Fund +
Investments); selecting "Emergency Fund" narrows to its card +
recomputes the header ("1 items · $800.00"); the reset restores both
cards ("2 items · $1250.00"). A new e2e test in `tests/e2e/items.spec.ts`
(in the savings describe, after the existing savings test).

### T2. [TOOLING] the document.hasFocus() probe helper

The session-72 queue item formalized: `scripts/parity-probes/
hasfocus-gate.sh` — a shared shell helper that asserts
`document.hasFocus()` before any focus-computed read and, when the page
lacks focus (the sandbox reaps focus between evals), re-focuses it with
a REAL `press Shift` (the v34 lesson) and re-asserts. Baked into the
standing scripts' discipline + documented in the probe README (the
v39+ standing scripts source it before every focus read).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | The a11y audit spec: 8 tests (6 authed routes + the 404 + the login page) — GATE 1 (only color-contrast allowed) + GATE 2 (the 7-color parity palette) + the login's zero-violation gate; `@axe-core/playwright` devDependency | test | `tests/e2e/a11y.spec.ts`, `package.json` |
| 2 | T1 pin-sanity: strip a SelectTrigger's aria-label in items-view.tsx → the button-name violation fires → GATE 1 FAILS; rebuild (the e2e drives the production build — the v37 lesson); restore → GREEN | verify | `src/components/budget/items-view.tsx` |
| 3 | S1 test: the frequency filter's 7-option static census + the Weekly round-trip + the reset | test | `tests/e2e/items.spec.ts` |
| 4 | S1 pin-sanity: remove the "Weekly" SelectItem from the frequency filter → the options assertion FAILS; restore → GREEN | verify | `src/components/budget/items-view.tsx` |
| 5 | S2 test: the savings filter-card geometry + the category round-trip (Emergency Fund → 1 card → reset) | test | `tests/e2e/items.spec.ts` |
| 6 | S2 pin-sanity: change the savings searchPlaceholder → the placeholder/aria-label assertions FAIL; restore → GREEN | verify | `src/components/budget/items-view.tsx` |
| 7 | T2: the hasfocus-gate.sh helper + the probe README section (the tooling pass's first half) | tooling | `scripts/parity-probes/hasfocus-gate.sh`, `scripts/parity-probes/README.md` |
| 8 | The full chain re-run (108 unit · 187 e2e · 35 smoke + lint + typecheck + build) | verify | — |
| 9 | The 16 screenshots regenerated | docs | `docs/screenshots/` |
| 10 | The v38 probes persisted (ref-v38.sh, clone-v38.sh, a11y-scan-v38.mjs, axe-detail scripts, the VLM pair) + the probe README updated | docs | `scripts/parity-probes/` |
| 11 | Docs aligned (README v38 row + counts, CLAUDE.md the a11y-gate entry, AGENTS.md the tooling/a11y paragraph, SKILL state line + session row, session_80.md, the repo worklog Session 72, the workspace worklog) | docs | repo root + `docs/` |
| 12 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `tests/e2e/items.spec.ts` line ~678 (the end of the v37 S3 test, inside
  the expenses describe): the S1 insertion point — the round-trip idiom
  (click the trigger → assert the listbox options → select → assert the
  narrowed cards + the recomputed header → reset to All → assert the
  restored state) is exactly the v37 S3 pattern (`page.getByRole
  ("combobox", { name: "Filter by frequency" })` — the aria-label
  superset makes the trigger addressable; the v36 keyboard-contract
  tests cover the roving, so S1 asserts the option census + the
  data round-trip only).
- `src/components/budget/items-view.tsx` lines ~203–215: the frequency
  Select renders the STATIC option list (`All Frequencies` + One-time +
  Weekly + Bi-weekly + Monthly + Quarterly + Annually) — the S1
  pin-sanity mutation removes the `<SelectItem value="weekly">` line and
  the options assertion (`getByRole("option", { name: "Weekly" })`)
  FAILS.
- `tests/e2e/items.spec.ts` line ~679+ (the savings describe, after the
  existing "renders the seeded savings items" test): the S2 insertion
  point. The savings seed (`prisma/seed.ts`): Emergency Fund $800 +
  Investments $450 = $1250 → "2 items · $1250.00"; the category
  round-trip "1 items · $800.00". The savings search placeholder lives
  in the META block (`items-view.tsx` line ~46: "Search savings
  items...") — the S2 pin-sanity mutation changes that string and the
  placeholder + aria-label assertions FAIL.
- `tests/e2e/a11y.spec.ts` (new file): follows the auth.spec.ts opt-out
  idiom for the login test (`test.use({ storageState: { cookies: [],
  origins: [] } })`); the authed tests reuse the chromium project's
  shared storageState. The AxeBuilder API:
  `new AxeBuilder({ page }).withTags(["wcag2a","wcag2aa","wcag21a",
  "wcag21aa"]).analyze()` — validated live this session by
  a11y-scan-v38.mjs (the exact violation sets quoted in F1). Gate 2
  reads each flagged node's computed color via `page.evaluate` on the
  axe `node.target` selector chain — the exact technique validated by
  axe-detail-v38.mjs (all 14 / nodes resolved; the escaped-class
  selectors query cleanly).
- The settle discipline: each authed scan waits for a seeded content
  marker (the card headings / the breakdown section rows) + a 2500ms
  settle (the v15 loading-overlay contract: the item views prerender the
  full-screen spinner; the scan must run against the BOOTED DOM). The
  404 needs no settle beyond domcontentloaded + 1500ms.
- `package.json`: `@axe-core/playwright` 4.13.0 lands in devDependencies
  (installed this session; `axe-core` itself is bundled inside the
  package — no separate dependency).
- The chain gate: lint → typecheck → 108 unit → build → 177 e2e (187
  after the 8 a11y tests + S1 + S2; all new tests) → 35 smoke. The a11y
  tests add ~50s to the suite (8 scans × ~6s incl. settles).
