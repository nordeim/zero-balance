# Remediation Plan v48 — The Item-Details Sheet's Shadow-2xl + the
# Dialog-Input Focus Composite at 390 + the Empty-State Census — a
# PIN-ONLY iteration

Date: 2026-10-12 · Scope: the session-108 queue's first candidate (the
item-details sheet's panel shadow — the shadow-scale regression net's
SEVENTH site, the 2xl end on the details surface) + the session-108
queue's fourth candidate (the dialog inputs' focus composite at 390 —
the v47 F1's MOBILE follow-up) + the session-108 queue's third
candidate (the empty-state cards' chrome via filter-to-zero — the
read-only empty-surface census). Measured live on BOTH sites via the
agent-browser evals (the ref/clone drivers persisted as the v48 family:
`ref-v48.sh` + `clone-v48.sh` + the detail re-probes).

**NO production-code change — the measured chrome is already at parity
on every VISIBLE layer; the three pins lock it as the regression net**
(the v45-family PIN-ONLY iteration, the FOURTH since the v44 production
change).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **226/226 e2e ✓ (5.3m)** · 35/35 smoke ✓. The 42nd standing
checks all clean (mobile-nav R1–R4 both sites — Tailwind v4 pins hold,
the mobile menu works; the reference's toast-blocker measured via
elementFromPoint at the burger's center `DIV.fixed top-0 z-[100]`, the
sheet-trap via the live nav — sheet + overlay still open after
navigating to /income, the no-landmark `navLandmark: false`, the
395/464 overflows all still live; the data census read-only before +
after — "1 items · $25,000" networth / "1 items · $5000.00" income,
the v46 incident's restoration intact; the SEO pair live on both
sites). npm audit = the same 5 dev-only ESLint-chain advisories
(accepted, unchanged; `--omit=dev` = 0); the secret-pattern scan clean;
`.env` ≡ `.env.example` (modulo the dev AUTH_SECRET value — the
documented pattern); the workspace rebuilt after the reset (clone →
npm install → db:push → db:seed; the playwright chromium-1243 build
installed to match the lockfile-resolved 1.63.0 — the v46 lesson
pre-applied).

## The v48 sweep — what the measurement found

- **THE ITEM-DETAILS SHEET'S SHADOW-2XL (the session-108 queue #1): the
  visible layer matches — the shadow-scale net's SEVENTH site (the 2xl
  end, the details panel; joining the v45 login-panel 2xl site).**
  Measured on the Salary item's details sheet (card-body click → the
  read-only details dialog), live on both sites, at 1280:
  - The reference's panel (`bg-white rounded-t-3xl md:rounded-2xl
    shadow-2xl max-w-lg w-full max-h-[85vh] overflow-y-auto`, inside
    `fixed inset-0 z-50 flex items-end md:items-center justify-center
    p-0 md:p-4`): w 512 / h 680 (the 85vh cap at the 800 viewport) /
    radius 16 (md:rounded-2xl) / bg white / border 0px — shadow = 2
    transparent leads + **the v3 shadow-2xl layer `rgba(0, 0, 0, 0.25)
    0px 25px 50px -12px`**.
  - The clone's panel (the Radix Content `[role=dialog]` itself —
    `fixed bottom-0 left-1/2 z-50 max-h-[85vh] w-full max-w-lg
    -translate-x-1/2 overflow-y-auto rounded-t-3xl bg-white shadow-2xl
    md:bottom-auto md:top-1/2 md:-translate-y-1/2 md:rounded-2xl`):
    w 512 / h 680 / radius 16 / bg white — shadow = 4 transparent
    leads + **the SAME `rgba(0, 0, 0, 0.25) 0px 25px 50px -12px`**
    (v4's 5-slot construction — the accepted v10/v25/v45
    lead-divergence class, this time at the 2xl end on the details
    surface).
  - The overlay: `rgba(26, 58, 46, 0.5)` (the forest scrim) + z 50 on
    both sites; the clone carries the blur(8px) backdropFilter (the v7
    G6 inline-pinned forest scrim — the reference's same family,
    already pinned by the v28 item-details specs; re-verified live).
  - The close button: 36×36 / radius 6 / transparent bg / border 0 /
    no rest shadow on both sites (the v9 in-header X family — the
    reference's icon-only button, re-verified in the same census).
- **THE DIALOG-INPUT FOCUS COMPOSITE AT 390 (the v47 F1's mobile
  follow-up): every VISIBLE layer matches at the mobile viewport —
  PIN-ONLY.** Measured on the Add-Income dialog's first input, live on
  both sites, at 390×844:
  - The input **w 310** on BOTH sites (the mobile dialog's content
    width — 390 − 2×40 page+dialog padding).
  - REST: the reference 3 layers (2 transparent leads + the shadow-sm
    visible layer `rgba(0, 0, 0, 0.05) 0px 1px 2px 0px`) vs the
    clone's 5 layers (4 transparent leads + **the same visible
    layer**); h 36 / radius 6 / pad 4px 12px / border 1px
    rgb(229,229,229) / bg transparent — IDENTICAL.
  - FOCUS (a REAL `.focus({ focusVisible: true })`, `:focus-visible`
    matched on both sites): the reference 3 layers (the white
    zero-spread lead + **the 1px rgb(10,10,10) ring** + the shadow-sm
    visible layer) vs the clone's 5 layers (3 transparent leads + the
    same ring + the same shadow-sm layer); the border color UNCHANGED
    under focus on both sites; the outline (the reference's v3
    transparent-2px solid vs the clone's v4 `none`) both invisible.
  - **The v47 desktop composite holds at 390 — the focus family is
    viewport-independent on both sites.**
- **THE EMPTY-STATE CENSUS VIA FILTER-TO-ZERO (the session-108 queue
  #3): BYTE-PARITY — the whole block pins.** Measured on the /income
  empty state (frequency filter → One-time, read-only; the reference's
  Salary is Monthly so the list goes to zero), live on both sites, at
  390×844:
  - The container: `text-center py-16` (pad 64px 0px, text-align
    center, transparent bg, NO border/radius — a BARE block directly
    on the warm page bg) — w 358 / h 328 IDENTICAL.
  - The icon: 64×64 / opacity 0.2 / color rgb(10,10,10) / mb 16 —
    IDENTICAL (the bare lucide type icon).
  - The H3 title (`text-xl font-semibold mb-2`): fs 20 / fw 600 /
    color rgb(26,58,46) (forest) / mb 8 — IDENTICAL.
  - The P subtitle (`mb-6`): fs 16 / color rgb(107,114,128) / mb 24 —
    IDENTICAL.
  - The Add button: h 36 / w 147 / the 135deg gradient
    rgb(143,188,63)→rgb(184,216,126) / pad 8px 16px / radius 6 / fw
    500 / shadow **`rgba(0,0,0,0.1) 0px 1px 3px 0px, rgba(0,0,0,0.1)
    0px 1px 2px -1px`** — v3's BARE shadow (the `.zb-btn-add` v11 G2a
    pin) — IDENTICAL on both sites.
  - The v6 G12 spec already pins the empty state's STRUCTURE (bare
    block, no card, no circle); the v48 census adds the FULL
    byte-parity pin (the measured geometry + the chrome + the Add
    button's shadow family).

## Findings

### F1. [PIN] the item-details sheet's shadow-2xl census

One e2e test (`tests/e2e/item-details.spec.ts`): click the income
card body (the v28 flow — the Salary item), census the panel — the
geometry (w 512 / h 680 the 85vh cap / radius 16 / maxW 512 / bg
white), the boxShadow toContain **the v3 2xl visible layer
`rgba(0, 0, 0, 0.25) 0px 25px 50px -12px`** + the 5-slot layer count
(the v4 construction pin), the overlay `rgba(26, 58, 46, 0.5)` + z 50
+ blur(8px) (the v7 G6 forest scrim, re-verified), the close button
(36×36 / radius 6 / transparent / border 0).

### F2. [PIN] the dialog-input focus composite at 390

One e2e test (`tests/e2e/dialog-buttons.spec.ts`,
`page.setViewportSize(390, 844)` — the v47 F1 idiom ported to the
mobile viewport): open the budget-item dialog (Add Income on
/income), census the first input — the **w 310** (the mobile
content width), the chrome (h 36 / radius 6 / pad 4px 12px / border
1px rgb(229,229,229) / bg transparent), the REST boxShadow toContain
the shadow-sm visible layer + the layer count 5, then REAL-focus it
(`el.focus({ focusVisible: true })`, the v35 idiom): the focused
boxShadow toContains **the ring `rgb(10, 10, 10) 0px 0px 0px 1px`**
AND **the shadow-sm visible layer**, the border color UNCHANGED under
focus, the outline style `none`, the layer count 5.

### F3. [PIN] the empty-state census (the full byte-parity pin)

One e2e test (`tests/e2e/empty-states.spec.ts` — the search
filter-to-zero idiom from the v6 G12 spec): filter /income to zero
(the search "zzzz-no-match"), census the empty block — the container
(`py-16 text-center` / pad 64px 0px / transparent / no border — w
358 / h 328 at 390), the icon (64×64 / opacity 0.2 / color
rgb(10,10,10) / mb 16), the H3 (fs 20 / fw 600 / rgb(26,58,46) / mb
8), the P (fs 16 / rgb(107,114,128) / mb 24), the Add button (h 36 /
the gradient background-image / pad 8px 16px / radius 6 / fw 500 /
the boxShadow toContain **both v3 bare-shadow layers** `rgba(0, 0,
0.1) 0px 1px 3px 0px` + `rgba(0, 0, 0, 0.1) 0px 1px 2px -1px`).

### S1. [MUTATION-SANITY] the pins bite

(a) the details panel's `shadow-2xl` removed → the F1 pin fails (no
2xl layers);
(b) the input's `focus-visible:ring-1` removed → the F2 pin fails
(no ring layer under focus — also v47's F1, the shared-class family);
(c) the empty-state's icon `mb-4` reverted to `mb-2` → the F3 census
fails (the icon mb 16→8 AND the container h 328→320);
(d) the `.zb-btn-add` box-shadow removed → the F3 pin fails (no bare
shadow layers).
All restored → GREEN. **Each mutation needs the standalone REBUILD
before the run bites** (the v47 execution lesson — the e2e suite runs
against the BUILD, not the source tree).

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v48 paragraph. D2: CLAUDE.md — the v48 entry +
the counts. D3: README — the v48 row + the counts. D4: the SKILL
doc — the Session 83 row, the count sites, the state line. D5: the
PAD — a v1.1.5 revision block. D6: the probe README — the v48 section
(the drivers + the lessons). D7: session_110.md (the formal log) +
session_111.md (the raw transcript) + the repo worklog Session 82 +
the ledger list. D8: the workspace worklog
(/home/z/my-project/worklog.md).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1 + F2 + F3 written (pin-only — GREEN immediately against the unchanged build, the TDD pin discipline: the pin proves the parity, the mutations prove the pin) | test | `tests/e2e/item-details.spec.ts` + `tests/e2e/dialog-buttons.spec.ts` + `tests/e2e/empty-states.spec.ts` |
| 2 | The probe scripts persisted + the probe README's v48 section | docs | `scripts/parity-probes/` |
| 3 | S1(a)–(d): the four pin-sanity mutations, each verified to FAIL then restored (each preceded by `npm run build` — the v47 lesson) | verify | `src/components/budget/item-details-dialog.tsx` + `src/components/ui/input.tsx` + `src/components/budget/items-view.tsx` + `src/app/globals.css` |
| 4 | The full chain re-run (108 unit · **229** e2e · 35 smoke + lint + typecheck + build) — all green; the standing VLM pair on the /savings view at 1280 (the fresh desktop surface) | verify | — |
| 5 | The 16 screenshots regenerated (the capture script) | docs | `docs/screenshots/` |
| 6 | D1–D8 + the formal session log (session_110.md) + the raw transcript (session_111.md) + the repo worklog Session 82 + the SKILL doc Session 83 row | docs | repo root + `docs/` |
| 7 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/item-details-dialog.tsx:141` — the panel class
  `fixed bottom-0 left-1/2 z-50 max-h-[85vh] w-full max-w-lg
  -translate-x-1/2 overflow-y-auto rounded-t-3xl bg-white shadow-2xl
  md:bottom-auto md:top-1/2 md:-translate-y-1/2 md:rounded-2xl` (the
  F1 target — the shadow-2xl site + the geometry family); the overlay
  (:132–138) the inline forest scrim `rgba(26, 58, 46, 0.5)` +
  blur(8px) (already pinned by the v28 specs — the F1 census
  re-verifies it in the same sweep).
- `src/components/ui/input.tsx:11` — the shadcn class stack
  `shadow-sm transition-colors ... focus-visible:outline-none
  focus-visible:ring-1 focus-visible:ring-ring` (the F2 target — the
  v47 F1's stack, this time censused at 390).
- `src/components/budget/items-view.tsx:239–263` — the empty-state
  block (the F3 target — `py-16 text-center`, the icon `mx-auto mb-4
  h-16 w-16 text-[#0a0a0a] opacity-20`, the H3 `mb-2 text-xl
  font-semibold` + forestDark, the P `mb-6 text-base` + gray, the
  `.zb-btn-add` button); `src/app/globals.css` `.zb-btn-add` (the S1(d)
  mutation site — the v3 bare shadow).
- The e2e contract: the specs run AUTHENTICATED (the setup project's
  storageState); the item-details opens via the card-body click (the
  v28 idiom — `div.rounded-xl` filter hasText, the h4 click); the
  dialog opens via `getByRole("button", { name: "Add Income" })` on
  /income (the v47 F1 idiom); the empty state triggers via the search
  placeholder "Search income items..." + "zzzz-no-match" (the v6 G12
  idiom — read-only, no filter-select state to restore). The
  REAL-focus idiom: `el.focus({ focusVisible: true } as unknown as
  FocusOptions)` (the v35 dashboard.spec.ts:47 precedent — the TS DOM
  lib lags the Chromium FocusOptions member, hence the cast).
- The chain gate: lint → typecheck → 108 unit → build → 226 e2e
  (**229** after: +3 — F1, F2, F3) → 35 smoke. The three tests add
  ~4s. NO production change in this iteration (the S1 mutations are
  verify-only, each restored immediately).
- Execution notes: `pkill -f agent-browser` before every Playwright
  run (the v46 lesson — the daemon's Chrome instances crash the
  browser contexts on pthread_create exhaustion). The reference probes
  this session were READ-ONLY (the card-click + census + close; the
  dialog-open + focus + cancel; the filter-to-zero + restore — the
  frequency filter reset to All verified "1 items · $5000.00" after;
  no Delete clicks anywhere, the v46 incident rule).
- The VLM pair: the /savings view at 1280 (the fresh desktop surface —
  the reference's /savings holds 1 Emergency Fund item; the clone's
  seed richer; both sites' cards byte-identical per the v45 items-view
  census). Expected flags: the demo data values only (the reference's
  live data vs the clone's seed — the 2-card vs 1-card data class, the
  v47 lesson).
