# Remediation Plan v47 — The Dialog-Input Focus Composite + the Net-Worth
# Card Mobile Census + the Mobile Sheet's Shadow-lg — a PIN-ONLY iteration

Date: 2026-10-11 · Scope: the session-101 queue's second candidate (the
dialog inputs' focus-state shadow composition — the ring+shadow layer
interaction under focus) + the v46 follow-up (the net-worth card's
MOBILE census at 390, the post-fix internal rhythm) + the session-104
queue's sheet item (the mobile sheet's shadow-lg at 390). Measured live
on BOTH sites via the agent-browser evals (the ref/clone drivers
persisted as `dlg-input-v47` family: the dialog input's rest + focus
compositions, the net-worth card at 390, the mobile sheet chrome).

**NO production-code change — the measured chrome is already at parity
on every VISIBLE layer; the pins lock it as the regression net** (the
v45-family PIN-ONLY iteration, the third since the v44 production
change).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **223/223 e2e ✓ (5.2m)** · 35/35 smoke ✓. The 41st standing
checks all clean (mobile-nav R1–R4 both sites — Tailwind v4 pins hold,
the mobile menu works; the reference's toast-blocker, sheet-trap,
no-landmark, 395/464 overflows all still live; the data census read-only
before + after — "1 items · $25,000", the Savings Account /
Commonwealth Bank restoration from the v46 incident intact; the SEO pair
live on both sites). npm audit = the same 5 dev-only ESLint-chain
advisories (accepted, unchanged; `--omit=dev` = 0); the secret-pattern
scan clean; `.env` byte-identical to `.env.example`; the workspace
rebuilt after the reset (clone → npm install → db:push → db:seed; the
playwright chromium-1243 build installed to match the lockfile-resolved
1.63.0).

## The v47 sweep — what the measurement found

- **THE DIALOG INPUT FOCUS COMPOSITE (session-101 queue #2): every
  VISIBLE layer matches on both sites; the LEAD layers diverge by
  construction — the accepted v10/v25/v45 class.** Measured on the
  Add-Item dialog's first input, live on both sites, at 1280:
  - REST: the reference `rgba(0,0,0,0) 0px 0px 0px 0px, rgba(0,0,0,0)
    0px 0px 0px 0px, rgba(0,0,0,0.05) 0px 1px 2px 0px` (3 layers: 2
    transparent leads + the shadow-sm VISIBLE layer) vs the clone's 5
    layers (4 transparent leads + **the same `rgba(0, 0, 0, 0.05) 0px
    1px 2px 0px`** — the `--shadow-sm` theme pin's restored v3 value).
  - FOCUS (a REAL `.focus()` + `:focus-visible` matched on both sites):
    the reference `rgb(255, 255, 255) 0px 0px 0px 0px, rgb(10, 10, 10)
    0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px` (the white
    zero-spread lead + **the 1px #0a0a0a RING** + the shadow-sm visible
    layer) vs the clone's 5 layers (3 transparent leads + **the same
    `rgb(10, 10, 10) 0px 0px 0px 1px` ring** + **the same shadow-sm
    visible layer**). The shadcn `focus-visible:ring-1
    focus-visible:ring-ring` + the v45 `--shadow-sm` pin compose the
    reference's visible layers EXACTLY.
  - The input chrome: h 36 / radius 6 / pad 4px 12px / border 1px
    rgb(229,229,229) / bg transparent — IDENTICAL on both sites, and
    the border color is UNCHANGED under focus on both sites (the ring
    does the work, not the border).
  - The outline family: the reference's v3 `outline-none` computes
    `rgba(0, 0, 0, 0) solid 2px` under focus (a transparent 2px) while
    the clone's v4 computes `none` — BOTH invisible (the v35 quick-
    action button chose to mimic the v3 form in custom CSS; the input
    family does not need it — the computed geometry contract is the
    painted pixels, and none paints the same nothing).
- **THE NET-WORTH CARD MOBILE CENSUS AT 390 (the v46 follow-up): the
  card's internal rhythm is at BYTE-PARITY post-fix.** The reference's
  asset card at 390 (inside its 432-wide overflowing grid — its
  documented superset-fix-#4 bug): h **194** / pad 20 / radius 12 /
  border 1px solid rgb(229,231,227) / rest shadow `rgba(0, 0, 0, 0.04)
  0px 2px 8px 0px` / transition `0.2s cubic-bezier(0.4, 0, 0.2, 1)`;
  the value P `mb 0` inside its `div.mb-4` wrap (mb **16px**, the
  measured value→facts gap 16) / fs 24 / lh 32 / rgb(143,188,63); the
  facts `space-y-2 text-xs` (12px, rgb(107,114,128)). The clone's card
  at 390: grid 358 wide / 1 col / gap 16 (the page FITS — docSW 390,
  mainSW 390, the documented superset fix); the card **358×194** / the
  identical chrome; the value P `mb 16` (the v46 fix holds at 390 — the
  clone carries the margin ON the P, the reference on the wrap div: the
  computed geometry is the contract, the DOM shape is not, the v45
  lesson) / fs 24 / lh 32 / rgb(143,188,63); the facts 12px
  rgb(107,114,128) / the measured gap **16**. **The card heights match
  exactly (194) — the v46 fix's rhythm survives the mobile
  reflow.**
- **THE MOBILE SHEET CHROME AT 390 (the session-104 queue item): the
  shadow-lg visible layers match — the shadow-scale net's sixth
  site.** The reference's sheet (288×844, x 0, bg rgb(250,250,250),
  transform none after settle): shadow = 2 transparent leads + **the
  v3 shadow-lg pair `rgba(0, 0, 0, 0.1) 0px 10px 15px -3px,
  rgba(0, 0, 0, 0.1) 0px 4px 6px -4px`**; the overlay rgba(0,0,0,0.8),
  z 50. The clone's sheet (the same 288×844 geometry — already pinned
  by the v7 G6 / mobile-nav specs): shadow = 4 transparent leads +
  **the same two visible layers** (v4's 5-slot composition — the v45
  systemic family, this time at the lg end on the mobile surface); the
  overlay rgba(0,0,0,0.8), z 50 (already pinned — re-verified).

## Findings

### F1. [PIN] the dialog input's focus-state composite

One e2e test (`tests/e2e/dialog-buttons.spec.ts`): open the budget-item
dialog (Add Income on /income), census the first input — the chrome
(h 36 / radius 6 / pad 4px 12px / border 1px rgb(229,229,229) / bg
transparent), the REST boxShadow (toContain the shadow-sm visible layer
`rgba(0, 0, 0, 0.05) 0px 1px 2px 0px`; the layer count 5 = the v4
5-slot construction pin), then REAL-focus it
(`el.focus({ focusVisible: true })`, the v35 idiom): `:focus-visible`
matches, the focused boxShadow toContains **the ring `rgb(10, 10, 10)
0px 0px 0px 1px`** AND **the shadow-sm visible layer** (the rest shadow
persists under focus — the composed state), the border color UNCHANGED
under focus (rgb(229,229,229)), the outline style `none` (the
invisible-family contract), the layer count 5 (the construction pin).

### F2. [PIN] the net-worth card mobile census at 390

One e2e test (`tests/e2e/networth.spec.ts`, `page.setViewportSize(390)`
— the v46 card-census idiom ported to the mobile viewport): the grid
`grid-cols-1` 358 wide / gap 16 / 1 column; the first card 358 wide /
**h 194** / pad 20 / radius 12 / border 1px solid rgb(229,231,227) /
the rest shadow `rgba(0, 0, 0, 0.04) 0px 2px 8px 0px` / transition
`0.2s cubic-bezier(0.4, 0, 0.2, 1)`; the value P mb **16** / fs 24 /
lh 32 / rgb(143,188,63); the facts fs 12 / rgb(107,114,128) / the
measured value→facts gap 16; `document.scrollWidth` 390 + `main.scrollWidth`
390 (the fit — the documented superset fix #4, the reference's own page
overflows at 464).

### F3. [PIN] the mobile sheet's shadow-lg census at 390

One e2e test (`tests/e2e/mobile-navigation.spec.ts`, the sheet opened
via the burger, the 700ms settle wait — the existing geometry-test
idiom): the sheet's boxShadow toContains **both shadow-lg visible
layers** (`rgba(0, 0, 0, 0.1) 0px 10px 15px -3px` + `rgba(0, 0, 0,
0.1) 0px 4px 6px -4px`) — the shadow-scale net's SIXTH site (the lg
end, the mobile surface; joining the v45 md/lg/sm/2xl pins and the v46
white-pill sm site); the bg rgb(250,250,250) / w 288 / x 0 / the
overlay rgba(0,0,0,0.8) z 50 (the already-pinned geometry re-verified
in the same census).

### S1. [MUTATION-SANITY] the pins bite

(a) the input's `focus-visible:ring-1` removed → the F1 pin fails (no
ring layer under focus);
(b) the input's `shadow-sm` removed → the F1 pin fails (no rest
visible layer);
(c) the net-worth card's value `mb-4` reverted to `mb-2` → the F2
census fails (the value mb 16→8 AND the card h 194→186);
(d) the sheet's `shadow-lg` removed → the F3 pin fails (no shadow
layers).
All restored → GREEN.

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v47 paragraph + the e2e count. D2: CLAUDE.md — the
v47 entry + the counts. D3: README — the v47 row + the counts. D4: the
SKILL doc — the Session 82 row, the count sites, the state line. D5:
the PAD — a v1.1.4 revision block. D6: the probe README — the v47
section (the three probes + the drivers + the lessons). D7:
session_107.md (the formal log) + session_108.md (the raw transcript) +
the repo worklog Session 81 + the ledger list. D8: the workspace
worklog (/home/z/my-project/worklog.md).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1 + F2 + F3 written (pin-only — GREEN immediately against the unchanged build, the TDD pin discipline: the pin proves the parity, the mutations prove the pin) | test | `tests/e2e/dialog-buttons.spec.ts` + `tests/e2e/networth.spec.ts` + `tests/e2e/mobile-navigation.spec.ts` |
| 2 | The probe scripts persisted + the probe README's v47 section | docs | `scripts/parity-probes/` |
| 3 | S1(a)–(d): the four pin-sanity mutations, each verified to FAIL then restored | verify | `src/components/ui/input.tsx` + `net-worth-view.tsx` + `sidebar.tsx` (or the sheet's class site) |
| 4 | The full chain re-run (108 unit · **226** e2e · 35 smoke + lint + typecheck + build) — all green; the standing VLM pair on the /income view at 390 | verify | — |
| 5 | The 16 screenshots regenerated (the capture script) | docs | `docs/screenshots/` |
| 6 | D1–D8 + the formal session log (session_107.md) + the raw transcript (session_108.md) + the repo worklog Session 81 + the SKILL doc Session 82 row | docs | repo root + `docs/` |
| 7 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/ui/input.tsx:11` — the shadcn class stack
  `shadow-sm transition-colors ... focus-visible:outline-none
  focus-visible:ring-1 focus-visible:ring-ring` (the F1 target — the
  rest shadow-sm + the focus ring + the outline-none, all measured
  composing the reference's visible layers exactly).
- `src/components/budget/net-worth-view.tsx:105/:210` — the value P
  `mb-4 text-2xl font-bold` (the F2 target — the v46 fix's rhythm at
  390); the card wrapper (:63/:167) `group rounded-xl border bg-white
  p-5 transition-all duration-200 hover:shadow-lg` + the inline
  border/shadow (the F2 chrome — the same census family as the v46
  desktop pin); the grid (:459/:522) `grid grid-cols-1 gap-4
  md:grid-cols-2 lg:grid-cols-3` (the F2 grid).
- The mobile sheet: `src/components/budget/sidebar.tsx` (the Sheet
  content — the `w-(--sheet-width)` 288px + the shadow-lg site on the
  sheet's panel class). The F3 mutation targets the sheet panel's
  `shadow-lg` class.
- The e2e contract: the specs run AUTHENTICATED (the setup project's
  storageState); the dialog opens via `getByRole("button", { name: "Add
  Income" })` on /income after the seeded card waits (the
  dialog-buttons.spec.ts:37 idiom); the networth spec's beforeEach
  navigates to /networth (the seeded 3-asset grid — the first card =
  the first group's first card); the mobile-nav spec's burger opens
  via `getByRole("button", { name: "Toggle Sidebar" })` + the 700ms
  settle (the mobile-navigation.spec.ts:86 idiom). The REAL-focus
  idiom: `el.focus({ focusVisible: true } as unknown as FocusOptions)`
  (the v35 dashboard.spec.ts:47 precedent — the TS DOM lib lags the
  Chromium FocusOptions member, hence the cast).
- The chain gate: lint → typecheck → 108 unit → build → 223 e2e
  (**226** after: +3 — F1, F2, F3) → 35 smoke. The three tests add
  ~4s. NO production change in this iteration (the S1 mutations are
  verify-only, each restored immediately).
- Execution notes: `pkill -f agent-browser` before every Playwright
  run (the v46 lesson — the daemon's Chrome instances crash the
  browser contexts on pthread_create exhaustion). The reference's
  net-worth kebab flow is NEVER probed past the menu open (the v46
  incident rule — this session's probes are read-only on the
  reference: the dialog-open + input-focus steps only, the sheet-open
  + census only, no Delete clicks anywhere).
- The VLM pair: the /income view at 390 (the fresh mobile surface —
  the reference's /income is overflow-free at 390, docSW 390 verified
  live; both sites' items-view cards pinned byte-identical at 1280 by
  v45, the mobile reflow is the new ground). Expected flags: the demo
  data values only (the reference's live data vs the clone's seed).
