# Remediation Plan v37 — Session-76 Parity Iteration

Date: 2026-10-11 · Scope: fresh two-site re-audit after the v36 baseline
(`fa62a7f` + the session-log commits `1a3a61f`/`118a45b` on `main`; this
session's re-run of the whole chain green on the FIRST full run: lint ✓ ·
typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**174/174 e2e ✓** · 35/35 smoke ✓). Workspace re-cloned fresh this session
(the old one had been reset); `npm install` + `cp .env.example .env` +
`db:push` + `db:seed` re-run; `db/custom.db` at the repo root;
scandihaven cloned at the workspace root, never compiled. Probes: the
standing disciplines — one-shot `agent-browser eval` (base64 via
run-probe.sh), the :3200 parity server inside ONE `with-server.sh`
invocation, REAL key presses and REAL hovers for every focus/hover claim,
parked-pointer settles, FULL computed strings, and the v34
`document.hasFocus()` gate before any `:focus`-computed read.

## The sweep — method and results

The pass swept the three session-76 suggested surfaces — the **filter
Select TRIGGERS' focus-visible family** (the ring contract when a REAL Tab
lands on the closed trigger — the v36 census walked PAST the stops, never
asserting their chrome), the **search input's focus + typing contract**
(the ring family + the match/no-match/cleared behavior — the existing
specs pin the fill()-driven filtering but never the focus chrome nor the
empty-state landing), and the **/expenses payment-method filter** (the
third Select — its trigger chrome, its dynamic option list, and its
filter/reset round-trip; never measured live against the reference) —
plus the standing re-verification set (mobile-nav R1–R4 on BOTH sites,
data drift, the SEO pair, one VLM pair) and the code audit (npm audit =
the same 5 dev-only ESLint `braces` advisories — accepted, unchanged,
dev-only; the secret-pattern scan clean; `.env.example` verified current,
keys matching `.env`).

- **Mobile navigation (the task focus) R1–R4 all re-verified live on BOTH
  sites — the 31st consecutive check.** R1: the reference's `fixed
  top-0 z-[100]` toast containers still intercept the burger's center
  hit (hit = `DIV.fixed.top-0.z-[100]`, scrollWidth 395), the clone's
  hit DIRECT on the svg with 390 fit. R2: the reference's sheet still
  traps after nav (sheet open, body locked); the clone's closes (superset
  #2). R3: the reference marks nothing active on `/` and has no `<nav>`;
  the clone has the landmark. R4: the reference overflows 395 on
  `/`+`/dashboard` and 464 on `/networth`; the clone fits 390 on all
  routes. **The Tailwind v4 pins hold — the mobile menu works as
  expected.**
- **Data drift clean (31st)**: the reference's census re-verified BEFORE
  and AFTER all probes (allocation 30.5%, income `$5000.00`, savings
  `$1000.00`, expenses `$525.00` — unchanged; read-only throughout: the
  search probe restored its input to "", the payment-method probe
  Escape-closed WITHOUT selecting, the edit-dialog probe opened + Escape
  closed without saving). The clone's seed census unchanged (62.8% /
  5550 / 1250 / 2235).
- **SEO pair ✓** (live, both sites): robots.txt (allow-all + the sitemap
  line) + sitemap.xml (five URLs, priority 1.0/0.8, weekly) live on both;
  the reference's head-metadata census re-captured (title ZeroBudget,
  the description/canonical/OG/Twitter pair, apple-mobile-web-app-title,
  manifest) — all matching the pinned values. The reference's sitemap
  capitalizes its app-route URLs (`/Income`, `/Savings` — measured live)
  while the clone's mirrors its own lowercase routes (the documented
  v21 decision; the reference's capitalized loc values do not match its
  own served routes).
- **Suggestion #1 — the filter Select triggers' focus-visible family: NO
  drift (first-time measurement of the closed trigger's keyboard
  chrome; the S1 pin below).** Measured on BOTH sites with REAL Tab
  walks (blur → 8 Tabs → the category combobox; the v36 census order):
  `:focus-visible` matches; the computed box-shadow's VISIBLE layers are
  byte-identical — the 1px #0a0a0a ring (`rgb(10,10,10) 0px 0px 0px
  1px`) + the ambient shadow (`rgba(0,0,0,0.05) 0px 1px 2px 0px`); the
  border stays `rgb(229,229,229)` 1px (untinted by focus — the v33 code-
  input lesson holds here too); the geometry unchanged (216×36). REST
  state also matches (border + the ambient layer only).
- **O1 (a construct observation — documented, NOT drift)**: the full
  computed box-shadow STRINGS differ in their invisible lead layers —
  the reference renders the v3 three-slot construct (ring-offset white
  `rgb(255,255,255) 0px 0px 0px 0px` + ring + shadow) while the clone
  renders Tailwind v4's five-slot construct (four `rgba(0,0,0,0) 0px
  0px 0px 0px` leads + ring + shadow). Every lead layer is a 0px-spread
  shadow — invisible by construction on both sites; the VISIBLE layers
  (the ring + the ambient) are byte-identical. Same class as the v11
  shadow-scale documentation: the construct differs, the render does
  not. The repo's full-string comparison rule exists so the visible
  layer is never missed — not to force lead-layer-count parity.
- **Suggestion #2 — the search input's focus + typing contract: NO
  drift (first-time measurement of the focus chrome + the typed
  behavior; the S2 pin below).** The focus family measured on BOTH
  sites with REAL Tabs (Shift+Tab from the combobox back onto the
  input): `:focus-visible` matches; the same 1px #0a0a0a ring + ambient
  (visible layers byte-identical; the same O1 construct note); the
  border untinted `rgb(229,229,229)`; geometry 447×36; bg transparent.
  The typing contract on the reference (REAL keyboard chars): typing
  the exact card name "Salary" → the card list narrows to the Salary
  card + the header recomputes ("Income 1 items · $5000.00"); a
  no-match string → the EMPTY state (h3 "No income items yet" +
  "Start by adding your first income source" + the header "0 items ·
  $0.00"); clearing → the card restored. The clone: byte-identical
  behavior ("Salary" → 1 card + "1 items · $5200.00" [its demo seed's
  Salary amount]; "zzz" → the same empty state; cleared → both income
  cards restored).
- **L1 (probe lesson)**: the reference's CARD titles are `h4` elements
  and its EMPTY-state heading an `h3` — an h3-only card census
  fabricated "the reference's search shows no cards" readings until the
  h4 selector caught them. Card probes must query the title tag the
  view actually renders (or both).
- **L2 (probe lesson)**: `agent-browser keyboard press Backspace` did
  NOT register in the reference's focused search input (six presses,
  the value unchanged) — and the CLI's `fill ""` dispatches no input
  event either. Clear a React-controlled input in probes via the
  native value setter + a bubbled `input` Event (the React onChange
  path). Playwright's own `fill("")` is unaffected (it drives proper
  input events — the existing spec's restore step holds).
- **Suggestion #3 — the /expenses payment-method filter: NO drift
  (first-time live measurement of the third Select; the S3 pin
  below).** The filter card on BOTH sites: three comboboxes at 216×36
  each ("All Categories" / "All Frequencies" / "All Payment Methods"),
  the search input "Search expense items...". The reference's PM
  listbox open: exactly ONE option ("All Payment Methods",
  `aria-selected=true`) — its demo expense items carry NO
  paymentMethod values (verified: no Bank/Card/PayPal/Cash/Transfer/
  Brokerage text anywhere in its /expenses DOM). The clone's open: the
  All option + "Bank Transfer" + "Credit Card" — the DYNAMIC derivation
  (`Array.from(new Set(items.map(i => i.paymentMethod).filter(Boolean)))`)
  working over its own seed (Rent: Bank Transfer; Groceries +
  Entertainment: Credit Card). Data-level difference (the richer demo
  seed), not drift. The reference's EDIT DIALOG (opened read-only +
  Escape-closed) carries the "payment method" field — its data model
  supports the values; its cards would render the chip when the value
  exists (the clone's conditional `item.paymentMethod ? chip` matches
  the model). The clone's round-trip: select "Credit Card" → the
  trigger text updates, the cards narrow to Entertainment + Groceries,
  the header recomputes ("2 items · $385.00"); reset to All → all three
  cards restored. Also re-verified on the reference this session: the
  expense cards' action family is the INLINE hover-revealed "Edit
  Category" (77×32) + "Open Calculator" (110×32) buttons (the v8-pinned
  family; the kebab lives on the income/savings cards — the v35/v36
  family).
- **The VLM pairwise (one fresh pair, viewport-asserted 1280×800)**: the
  /expenses page with the PM filter open — VERDICT DIFFERENT with ALL
  five flags DOM-explained (4 cards vs 3 = the demo data; the extra
  tags + the footer Credit Card/Bank Transfer chips + the two extra
  dropdown options = the clone's seed carrying paymentMethod values
  the reference's items lack [data-level]; the avatar letter U vs D =
  the different demo users). Zero unexplained visual drift.

## Findings

### O1. [OBSERVATION — documented, not drift] the v3/v4 ring construct difference on the filter triggers

The reference's shadcn ring family renders the v3 three-slot construct
(white ring-offset lead + ring + shadow) while the clone's `focus:ring-1
focus:ring-ring` compiles to v4's five-slot construct (four transparent
leads + ring + shadow). Every lead is a 0px-spread shadow — invisible by
construction; the VISIBLE layers (the 1px #0a0a0a ring + the
`rgba(0,0,0,0.05) 0px 1px 2px` ambient) are byte-identical. Documented
with the v11 shadow-scale precedent; the S1/S2 pins assert the VISIBLE
layers (the ring + ambient strings) so a future refactor cannot drop
them — they do not (and should not) pin the invisible lead count.

### S1. [PIN] the filter Select triggers' focus-visible family

The session-76 surface #1's measurable contract, first-time measured
with a REAL Tab walk on both sites and pinned: a REAL Tab onto the
closed category-filter trigger engages `:focus-visible` and renders the
1px #0a0a0a ring (`rgb(10, 10, 10) 0px 0px 0px 1px`) layered over the
ambient `rgba(0, 0, 0, 0.05) 0px 1px 2px 0px` shadow — the border stays
`rgb(229, 229, 229)` (untinted), the geometry unchanged (216×36). A new
e2e test in `tests/e2e/items.spec.ts` (after the v36 S2/S3 tests) walks
the REAL Tab onto the trigger and asserts `:focus-visible` + both
visible box-shadow layers + the border color.

### S2. [PIN] the search input's focus + typing contract

The session-76 surface #2's measurable contract, first-time measured
and pinned: a REAL Tab onto the search input engages `:focus-visible`
and renders the SAME 1px #0a0a0a ring + ambient family (border
untinted, 447×36, transparent bg); typing the exact card name with REAL
keyboard chars narrows the list to the card + recomputes the header
count; a no-match string swaps to the EMPTY state (the h3 "No income
items yet"); clearing restores the full card list. A new e2e test in
`tests/e2e/items.spec.ts` (next to the existing fill()-based search
tests) drives the REAL keys (`pressSequentially`) and asserts the focus
family + the three-way typing outcome.

### S3. [PIN] the /expenses payment-method filter's full contract

The session-76 surface #3's measurable contract, first-time measured
and pinned: the third Select's trigger ("All Payment Methods",
216×36, the aria-label superset) opens a listbox whose options are
DERIVED from the seed's expense payment methods (All + Bank Transfer +
Credit Card); selecting "Credit Card" updates the trigger text, narrows
the cards to the two Credit Card expenses (Entertainment + Groceries),
and recomputes the header ("2 items · $385.00"); resetting to "All
Payment Methods" restores the three cards. A new e2e test in
`tests/e2e/items.spec.ts` (in the expenses describe, after the
category-filter test) drives the round-trip with REAL clicks/keys and
restores the fixture (the selection reset — the same discipline as the
v36 S2 restore).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | S1 test: the filter Select trigger's focus-visible family (REAL Tab onto the combobox; the 1px #0a0a0a ring + ambient layers; the untinted border) | test | `tests/e2e/items.spec.ts` |
| 2 | S1 pin-sanity: strip the SelectTrigger's `focus:ring-1 focus:ring-ring` → the ring assertion FAILS; restore → GREEN | verify | `src/components/ui/select.tsx` |
| 3 | S2 test: the search input's focus family + the REAL-key typing contract (match → card + header; no-match → the empty state; cleared → restored) | test | `tests/e2e/items.spec.ts` |
| 4 | S2 pin-sanity: strip the Input's `focus-visible:ring-1 focus-visible:ring-ring` → the focus-ring assertion FAILS; restore → GREEN | verify | `src/components/ui/input.tsx` |
| 5 | S3 test: the payment-method filter's round-trip (the dynamic options; Credit Card → 2 cards + "2 items · $385.00"; reset → 3 cards) | test | `tests/e2e/items.spec.ts` |
| 6 | S3 pin-sanity: break the paymentMethods derivation (filter to nothing) → the options assertion FAILS; restore → GREEN | verify | `src/components/budget/items-view.tsx` |
| 7 | The full chain re-run (108 unit · 177 e2e · 35 smoke + lint + typecheck + build) | verify | — |
| 8 | The 16 screenshots regenerated | docs | `docs/screenshots/` |
| 9 | The v37 probes persisted + the probe README updated (the L1/L2 lessons) | docs | `scripts/parity-probes/` |
| 10 | Docs aligned (README v37 row + counts, CLAUDE, AGENTS — the O1 construct note, SKILL state line, session_77, the repo worklog Session 71, the workspace worklog) | docs | repo root + `docs/` |
| 11 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `items.spec.ts` line ~300 (the end of the v36 S3 Tab-census test):
  the S1/S2 insertion point — the walk idiom (blur → REAL Tabs →
  `:focus-visible` + computed chrome reads) is exactly the v36 S3
  pattern; the S1 walk needs 8 Tabs (the five nav links + Add Income +
  the search input + the category combobox — the v36 census order) and
  the S2 walk reuses the same walk then Shift+Tabs back onto the input.
- `select.tsx` line ~19: the SelectTrigger base carries
  `focus:outline-none focus:ring-1 focus:ring-ring` — the S1 pin-sanity
  mutation strips `focus:ring-1 focus:ring-ring` and the ring-layer
  assertion (box-shadow containing `rgb(10, 10, 10) 0px 0px 0px 1px`)
  FAILS (the remaining shadow renders the ambient only).
- `input.tsx` line ~10: the Input base carries
  `focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring`
  — the S2 pin-sanity mutation strips `focus-visible:ring-1
  focus-visible:ring-ring` and the focus-ring assertion FAILS. (The
  REAL Tab engages `:focus-visible` — programmatic focus alone never
  does; the v35 lesson holds.)
- `items-view.tsx` lines ~99–104: the `paymentMethods` memo derives the
  options via `Array.from(new Set(items.map((i) =>
  i.paymentMethod).filter((p): p is string => !!p))).sort()` — the S3
  pin-sanity mutation empties the derivation (`.filter(() => false)`)
  and the options assertion (Bank Transfer + Credit Card present) FAILS.
- The seed (`prisma/seed.ts`): the three expenses carry Rent/Bank
  Transfer 1850, Groceries/Credit Card 320, Entertainment/Credit Card
  65 — the S3 expectations (2 Credit Card cards summing $385.00, 3
  cards at All) are the seed's exact arithmetic.
- `items.spec.ts` line ~44: the existing "search filters the card list"
  test uses `fill()` — the S2 test complements it with REAL keyboard
  chars (`pressSequentially`) + the focus chrome + the empty-state h3
  landing (never asserted before) + the restore.
- The chain gate: lint → typecheck → 108 unit → build → 174 e2e (177
  after S1+S2+S3; all three are new tests) → 35 smoke.
