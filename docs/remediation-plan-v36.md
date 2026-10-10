# Remediation Plan v36 — Session-72 Parity Iteration

Date: 2026-10-10 · Scope: fresh two-site re-audit after the v35 baseline
(`5069de8` + the session-log commit `51f1fd9` on `main`; this session's
re-run of the whole chain green on the FIRST full run: lint ✓ ·
typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**171/171 e2e ✓** · 35/35 smoke ✓). Workspace intact from session 68
(node_modules, `db/` seeded at the repo root, `.env` with
`DATABASE_URL="file:../db/custom.db"`, scandihaven cloned at the
workspace root, never compiled). Probes: the standing disciplines —
one-shot `agent-browser eval` (base64 via run-probe.sh), the :3200
parity server inside ONE `with-server.sh` invocation, REAL key presses
and REAL hovers (`agent-browser hover` — synthetic mouse events do NOT
move Radix's menu highlight) for every focus/hover claim, parked-pointer
settles, FULL computed strings, and the v34 `document.hasFocus()` gate
before any `:focus`-computed read.

## The sweep — method and results

The pass swept the three session-72 suggested surfaces — the **item-card
action menu's HOVER-highlight family** (hover → Radix moves focus → the
accent tint; verified implicitly since v5 but never asserted), the
**filter Selects' listbox keyboard contract** (the v34 frequency pin
covered the calculator sub-dialog instance; the `/income` filter-card
instances were never measured), and the **items-view Tab-order census**
(the v33 census covered the sub-dialog, not the page) — plus the
standing re-verification set (mobile-nav R1–R4 on BOTH sites, data
drift, the SEO pair, two VLM pairs) and the code audit (npm audit = the
same 5 dev-only ESLint `braces`/eslint-config-next advisories —
accepted, unchanged, dev-only; the secret-pattern scan clean;
`.env.example` verified current, keys matching `.env`).

- **Mobile navigation (the task focus) R1–R4 all re-verified live on BOTH
  sites — the 30th consecutive check.** R1: the reference's `fixed
  top-0 z-[100]` toast containers still intercept the burger's center
  hit (hit = `DIV.fixed.top-0.z-[100]`, scrollWidth 395), the clone's
  hit DIRECT on the svg with 390 fit. R2: the reference's sheet still
  traps after nav (sheet open, body locked); the clone's closes (superset
  #2). R3: the reference marks nothing active on `/` and has no `<nav>`;
  the clone has the landmark + the text-based active highlight. R4: the
  reference overflows 395 on `/`+`/dashboard` and 464 on `/networth`;
  the clone fits 390 on all routes. **The Tailwind v4 pins hold — the
  mobile menu works as expected.**
- **Data drift clean (30th)**: the reference's census re-verified BEFORE
  and AFTER all probes (allocation 30.5%, income `$5000.00`/1, savings
  `$1000.00`/1, expenses `$525.00`/4 — unchanged; read-only throughout:
  the filter probe Escape-closed or reset its selections, the menu
  probes Escape-closed, nothing selected/deleted). The clone's seed
  census unchanged (62.8% / 5550 / 1250 / 2235).
- **SEO pair ✓** (live, both sites): robots.txt (allow-all + the
  sitemap line) + sitemap.xml (five URLs, priority 1.0/0.8, weekly) live
  on both; the reference's head-metadata census re-captured (title
  ZeroBudget, the description/canonical/OG/Twitter pair,
  apple-mobile-web-app-title, manifest) — all matching the pinned
  values.
- **Suggestion #1 — the action menu's HOVER-highlight family: NO drift
  (first-time measurement with a REAL hover; the S1 pin below).** The
  full contract measured on BOTH sites with `agent-browser hover` (a
  synthetic `dispatchEvent(mousemove/mouseenter)` does NOT move Radix's
  highlight — only a REAL pointer move does; the first probe's
  no-op hover fabricated a "the reference ignores hover" reading until
  the real-hover retry): fresh-open via CLICK (pointerdown family) →
  focus on the menu CONTAINER, both items at rest (Edit
  `rgb(10,10,10)`, Delete `rgb(220,38,38)`); REAL hover on the Delete →
  **Radix moves DOM focus to the hovered item** (`:focus` matches,
  `data-highlighted` present) and the hovered chrome is the SAME accent
  family as keyboard focus (bg `rgb(245,245,245)` + text
  `rgb(23,23,23)` — the v35 G1 cascade holds on the HOVER path; the
  hovered Delete is NOT red); hover away (to body) → focus returns to
  the CONTAINER, both items back at rest (Delete red again), the menu
  stays open; Escape → the menu closes and focus returns to the
  trigger. Byte-identical on both sites, both open paths.
- **Suggestion #2 — the filter Selects' listbox keyboard contract (the
  `/income` instances): NO drift (first-time measurement; the S2 pin
  below).** The full Radix combobox contract measured on BOTH sites:
  fresh-open via CLICK **and** via ENTER both land focus on the
  SELECTED option (`aria-selected=true`, `data-highlighted` present,
  the accent family bg `rgb(245,245,245)` + text `rgb(23,23,23)` — the
  same `:focus`-driven family as the menu items; unlike the
  DropdownMenu, the Select's two open paths land identically);
  ArrowDown/ArrowUp rove the highlight; the arrows CLAMP at both ends;
  Home/End jump to the first/last option; Escape closes the popup only
  (focus returns to the TRIGGER, the page stays — no dialog involved in
  the filter instance); Enter selects the highlighted option (popup
  closes, the trigger's text updates, focus on the trigger). Trigger
  chrome: `button[role=combobox]` 216×36, `aria-expanded` toggling.
  The clone's category list differs in LENGTH (3 options vs the
  reference's 2 — the demo seed carries a Freelance item the reference
  account lacks) — data-level, not drift. One observation (documented,
  NOT drift): the reference's trigger PERSISTS `aria-controls` on the
  CLOSED trigger (a Radix-minor-version lifecycle detail); the clone
  carries the matching `aria-controls` while OPEN (the functional
  state), none while closed — and the id format differs
  (`radix-:r0:` vs `radix-_r_3_`) — React 18 vs 19 `useId` cosmetics.
- **Suggestion #3 — the items-view Tab-order census: the ORDER
  byte-identical (first-time page-level measurement; the S3 pin below),
  TWO keyboard-a11y supersets documented + one platform-chrome
  exclusion.** The REAL-Tab walk (16–18 stops, blur-then-Tab,
  450ms settles) on `/income` at 1280×800, both sites: the five nav
  links (Dashboard→Net Worth, 215×32 at x=20, y=145→305) → the Add
  Income button (147×36 at 1101,44) → the search input (447×36 at
  313,149) → the category combobox (216×36 at 776,149) → the frequency
  combobox (216×36 at 1008,149) → the card kebab triggers (36×36,
  one per card — the clone's 2 cards vs the reference's 1 = the
  data-level difference) → wrap. IDENTICAL sequence and geometry on
  both sites. Findings:
  - **O1 (keyboard-a11y SUPERSET — document + pin)**: the reference's
    kebab trigger stays INVISIBLE when keyboard-focused — a REAL Tab
    onto it leaves `opacity: 0` (measured live: `:focus-visible`
    matches, the ring's computed string is present, but the element
    renders nothing) and it also goes invisible while its menu is open
    via keyboard (no `data-[state=open]` reveal). A keyboard user on
    the reference LOSES the visual focus entirely at that stop. The
    clone carries `focus-visible:opacity-100` +
    `data-[state=open]:opacity-100` (day-one session-1 classes, commit
    `703ea74`) — the trigger reveals on keyboard focus and stays
    revealed while open. Same class as the toast-pointer-events fix:
    the reference's bug, the clone's superset.
  - **O2 (invisible a11y SUPERSET — document)**: the clone's filter
    comboboxes carry `aria-label` ("Filter by category" / "Filter by
    frequency") and the search input an `aria-label` mirroring its
    placeholder; the reference's controls are value-named only ("All
    Categories" — the selected value doubles as the accessible name)
    with no label on the search input. Invisible in visual parity;
    strictly better semantics for screen readers. Day-one decisions.
  - **O3 (platform chrome — documented exclusion)**: the reference's
    Tab order includes the Base44 platform's floating **"Edit with
    Base44" badge** (`#base44-edit-badge`, fixed bottom-right, z-index
    999999) and its 18×18 "Close badge" button. This is PLATFORM
    chrome, not app UI — the clone correctly does not replicate it
    (the same class as a hosting-provider toolbar). Tab-order
    comparisons must exclude it; the VLM pair also flags it.
- **The VLM pairwise (two fresh pairs, viewport-asserted 1280×800
  before each capture)**: the dashboard — VERDICT DIFFERENT with ALL
  four flags DOM-explained (the Dashboard-active rail = superset #3;
  the progress fill ~63% vs ~30% + the avatar letter D vs U = the
  different demo data; the "Edit with Base44" floating button = O3
  platform chrome); the `/income` page with the filter Select OPEN —
  VERDICT DIFFERENT with all three flags data-explained (two cards vs
  one, three options vs two, the avatar letter). Zero unexplained
  visual drift.
- Probe-methodology lessons: (L1) **synthetic mouse events do not move
  Radix's hover highlight** — `dispatchEvent(mousemove/mouseenter)`
  leaves the highlight untouched; only a REAL pointer move
  (`agent-browser hover` / Playwright `.hover()`) triggers Radix's
  pointer-driven focus move. (L2) a blur does not reset the sequential
  focus navigation position — Chromium resumes the Tab walk from the
  last focus position (walk the cycle past the wrap to read the
  document-order sequence). (L3) the REAL-Tab walk reads the focused
  kebab's opacity as 1 on the clone (the `focus-visible:opacity-100`
  superset ENGAGED by the very Tab that landed) vs 0 on the reference
  — a live demonstration of O1, not a measurement artifact.

## Findings

### O1. [SUPERSET — documented + pinned] the action-menu trigger reveals on keyboard focus + while open (the reference stays invisible)

The reference's 36×36 hover-revealed kebab trigger carries
`opacity-0 group-hover:opacity-100` and NOTHING else in the reveal
family — on keyboard focus (`:focus-visible` matches, the shadcn
1px #0a0a0a ring computes) the element STILL renders invisible
(`opacity: 0`), and a keyboard-opened menu leaves the trigger
invisible too (the pointer is not on the card, so no group-hover).
Measured live this session (REAL Tab walk: reference kebab opacity
"0" right after the landing Tab; programmatic focus + 400ms: still
"0" with `fv: true`). The clone's day-one classes
`focus-visible:opacity-100` + `data-[state=open]:opacity-100`
(commit `703ea74`, session 1) keep the trigger visible for keyboard
users in both states. This joins the pinned superset family (the
toast hit, the sheet close, the active-route highlight, the no-overflow,
the dialog dismissal, the delete confirm) as #7. No production change
— the S3 pin asserts the reveal so a future refactor cannot drop it.

### S1. [PIN] the action-menu HOVER-highlight family

The session-72 surface #1's measurable contract, now measured with a
REAL hover on both sites and pinned: hovering a menu item moves DOM
focus to it (Radix's pointer-driven roving) and renders the SAME
accent family as keyboard focus (bg `rgb(245,245,245)` + text
`rgb(23,23,23)`; the hovered Delete is NOT red — the v35 G1 cascade
extended to the hover path); moving the pointer off the menu returns
focus to the container and both items to rest (Delete red at rest);
the menu survives the leave. A new e2e test in
`tests/e2e/tokens.spec.ts` (next to the v35 S1 keyboard-contract test)
pins the family via Playwright's REAL `.hover()` so a future
dropdown-menu refactor cannot break the pointer-driven roving or
re-invent the hovered Delete tint.

### S2. [PIN] the filter Selects' listbox keyboard contract (the /income instances)

The session-72 surface #2's measurable contract, first-time measured
on the reference's FILTER instances (v34 covered the calculator
sub-dialog only) and pinned: fresh-open via click AND Enter land focus
on the SELECTED option with the accent highlight; the arrows rove
with clamping at both ends; Home/End jump; Escape closes the popup
only (focus → the trigger, the page unaffected); Enter selects the
highlighted option and updates the trigger text. A new e2e test in
`tests/e2e/items.spec.ts` (next to the filter-card chrome test) pins
the contract at the category-filter instance, restoring the "All
Categories" selection afterward (the fixture-restore discipline).

### S3. [PIN] the items-view Tab-order census + the trigger's focus reveal

The session-72 surface #3's measurable contract, first-time measured
at the PAGE level (v33 covered the sub-dialog) and pinned: the Tab
sequence is exactly the five nav links → the Add button → the search
input → the category combobox → the frequency combobox → the card
kebab triggers (one per card, in DOM order) — the same order the
reference walks minus its platform badge (O3). The kebab stop also
pins O1: a REAL Tab onto the trigger engages
`focus-visible:opacity-100` (opacity → "1" — the reference stays
invisible; the superset) together with the v35-pinned ring family.
A new e2e test in `tests/e2e/items.spec.ts` walks the stops with
REAL Tab presses and asserts each landing (tag + accessible name +
geometry band) + the reveal.

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | S1 test: the action-menu hover-highlight family (REAL `.hover()` on the Delete; the hovered accent family; the leave-reset) | test | `tests/e2e/tokens.spec.ts` |
| 2 | S1 pin-sanity: re-add the `focus:text-[#dc2626]` override → the hovered-Delete color assertion FAILS; restore → GREEN | verify | `src/components/budget/item-card.tsx` |
| 3 | S2 test: the category filter's listbox keyboard contract (fresh-open selected-option highlight, arrow roving + clamping, Home/End, Escape → trigger, Enter selects + trigger text; restore the selection) | test | `tests/e2e/items.spec.ts` |
| 4 | S2 pin-sanity: strip the SelectItem's `focus:bg-accent` → the selected-option highlight assertion FAILS; restore → GREEN | verify | `src/components/ui/select.tsx` |
| 5 | S3 test: the items-view Tab-order census (the stop sequence + geometry bands + the kebab's focus-visible opacity reveal) | test | `tests/e2e/items.spec.ts` |
| 6 | S3 pin-sanity: strip the kebab's `focus-visible:opacity-100` → the reveal assertion FAILS; restore → GREEN | verify | `src/components/budget/item-card.tsx` |
| 7 | The full chain re-run (108 unit · 174 e2e · 35 smoke + lint + typecheck + build) | verify | — |
| 8 | The 16 screenshots regenerated | docs | `docs/screenshots/` |
| 9 | The v36 probes persisted + the probe README updated (the L1–L3 lessons) | docs | `scripts/parity-probes/` |
| 10 | Docs aligned (README v36 row + counts, CLAUDE, AGENTS — the O1 superset paragraph, SKILL state line, session_73, the repo worklog Session 70, the workspace worklog) | docs | repo root + `docs/` |
| 11 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `tokens.spec.ts` line ~99: the v35 S1 test ("the action-menu
  keyboard contract + focused Delete family") is the S1 insertion
  point — the new test reuses its `main .group` card-hover +
  `getByRole("button", { name: "Actions for Salary" })` menu-opening
  idiom and adds Playwright's REAL `.hover()` on the Delete item (the
  agent-browser L1 lesson: synthetic mouse events do not move the
  highlight; Playwright's `.hover()` is a real pointer move).
- `item-card.tsx` line ~142: the Delete item carries
  `className="text-[#dc2626]"` (rest-red only — the v35 G1 fix left no
  focus override); the S1 pin-sanity mutation re-adds
  `focus:text-[#dc2626]` — the hover moves DOM focus, so the override
  would win and the hovered-Delete assertion (rgb(23,23,23)) FAILS.
- `items.spec.ts` line ~71: the "filters sit inside the white
  rounded-2xl card" test is the S2 insertion point — the filter-card
  structure (search + 2 selects on income) is already pinned there;
  the new test opens the CATEGORY filter via
  `page.getByRole("combobox").first().click()` (the v35 G5 test's
  click-open idiom at tokens.spec line ~191) and drives the REAL keys
  (`page.keyboard.press`) — the clone's option list is
  "All Categories" / "Freelance" / "Salary" (the seed's two income
  categories), so the ArrowDown walk lands Freelance → Salary with
  the clamp at Salary.
- `select.tsx` line ~111: the SelectItem base carries
  `focus:bg-accent focus:text-accent-foreground` — the S2 pin-sanity
  mutation strips `focus:bg-accent` and the selected-option
  highlight assertion (bg `rgb(245,245,245)`) FAILS.
- `items-view.tsx` lines ~191/~204: the SelectTriggers carry
  `aria-label="Filter by category"` / `"Filter by frequency"` (O2) —
  the S3 walk asserts the stops by accessible name (the aria-labels
  make `getByRole` locators exact); the search input (line ~187)
  carries `aria-label={meta.searchPlaceholder}`.
- `item-card.tsx` line ~131: the trigger carries
  `opacity-0 ... focus-visible:opacity-100 group-hover:opacity-100
  data-[state=open]:opacity-100` — the S3 walk's kebab stop asserts
  opacity "1" after the landing Tab (O1 pinned); the pin-sanity
  mutation strips `focus-visible:opacity-100` and the assertion
  FAILS (the walk's REAL Tab engages :focus-visible — the v35
  lesson: programmatic focus alone never engages it).
- The chain gate: lint → typecheck → 108 unit → build → 171 e2e (174
  after S1+S2+S3; all three are new tests) → 35 smoke.
