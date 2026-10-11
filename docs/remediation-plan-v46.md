# Remediation Plan v46 — The Net-Worth Card Census + the Value→Facts
# Spacing Fix + the Confirm-Bar White-Pill Regression Pin

Date: 2026-10-11 · Scope: the session-101 queue's first and third
candidates — the net-worth ASSET/LIABILITY card census at 1280 (the
2→3-col grid pitch, the card chrome, the card's hover state, the kebab
reveal) and the five-site confirm-bar white-pill family's shadow-sm
(the shadow-scale regression net, unpinned) — PLUS the one REAL parity
gap the census opened: the value→facts spacing (the reference's `mb-4`
wrap vs the clone's bare `mb-2` P). Measured live on BOTH sites via
`nw-card-v46.mjs` + `confirm-pill-v46.mjs` (drivers: `ref-v46.sh` /
`clone-v46.sh`) and direct agent-browser evals (the REAL-hover steps).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **221/221 e2e ✓ (5.0m)** · 35/35 smoke ✓. The 40th standing
checks all clean (mobile-nav R1–R4 both sites — Tailwind v4 pins hold,
the mobile menu works; the reference's toast-blocker, sheet-trap,
no-landmark, 395 overflows all still live; the data census read-only
before + after; the SEO pair live). npm audit = the same 5 dev-only
ESLint-chain advisories (accepted, unchanged; `--omit=dev` = 0); the
secret-pattern scan clean (doc references only); `.env` byte-identical
to `.env.example`; the workspace rebuilt after the reset (clone →
npm install → db:push → db:seed; the playwright chromium-1243 build
installed to match the lockfile-resolved 1.63.0).

## The v46 sweep — what the measurement found

- **THE ONE REAL GAP (the value→facts spacing):** the reference wraps
  the card's value figure in `<div class="mb-4"><p
  class="text-2xl font-bold">` — a **16px** gap to the facts block —
  while the clone's AssetCard/LiabilityCard carry the margin ON the P
  (`<p class="mb-2 text-2xl font-bold">`, **8px**). Measured at 1280:
  the reference card **194px** tall vs the clone **186px** — the 8px
  delta IS the gap (the card census is otherwise byte-identical). The
  item-card's own value block already uses the `mb-4` wrap
  (item-card.tsx:152 — `<div className="mb-4">` wrapping the same
  `text-2xl font-bold` P): the net-worth cards are the ONE place the
  pattern was mis-transcribed, an oversight no census had caught (the
  v29 net-worth census measured the card CONTENT, the v41 summary-card
  census measured the HERO card, the mobile superset census the 390
  layout — nobody sampled the 1280 card's internal rhythm).
- **The net-worth card census at 1280: BYTE-IDENTICAL except the gap.**
  The grid `md:grid-cols-2 lg:grid-cols-3 gap-4` (net-worth-view.tsx:459
  on the clone, the reference's own asset grid the identical family):
  960 wide (the rail 256 + the content column 1024 − the p-8 64), 3
  columns × 309.328, gap 16, y 669; the card 309 wide / pad 20 / radius
  12 / border 1px solid rgb(229,231,227) / the rest shadow
  `rgba(0, 0, 0, 0.04) 0px 2px 8px 0px` (computed 4-value — Chrome
  normalizes the clone's 3-value inline and the reference's inline to
  the SAME string, the v45 lesson) / bg white / transition all 0.2s;
  the title row gap 8 / dot 8×8 rgb(143,188,63) / title 16px-600
  rgb(26,58,46); the type badge `inline-flex items-center rounded-md
  border px-2.5` bg rgb(243,244,246) / pad 2px 10px / radius 6 / 12px-600
  / rgb(55,65,81) / h 22 / border 1px transparent; the value 24px-700
  rgb(143,188,63) / line-height 32 / **mb 16 on the reference, 8 on the
  clone (the F1 fix)**; the facts 12px rgb(107,114,128) space-y-2 (16px
  rows, 12×12 svg icons); the kebab 36×36 opacity 0 (a 16×16 svg).
  **The card's REAL hover is INERT on BOTH sites** (the inline
  boxShadow beats the `hover:shadow-lg` utility — the v29
  inline-beats-class family, the same as the v45 items-card) while the
  kebab REVEALS (opacity 0→1, the group-hover) and translateY stays
  none — verified via agent-browser's REAL `.hover()` on both sites.
- **The reference's net-worth DELETE is DIRECT (no confirm bar)** — the
  kebab menu's Delete click IS the delete attempt (the v18-documented
  superset-fix-#6 family, re-confirmed live this session: the menu
  click removed the reference's only asset; restored via its Add Asset
  form — name "Savings Account", type bank account, value 25000,
  institution "Commonwealth Bank", date 2026-10-07 — the panel census
  re-reading "1 items · $25,000" byte-identical to the before state,
  and the dashboard census unchanged). The clone's inline confirm bars
  are the SUPERSET (the v18 catch-toast tier).
- **The confirm-bar white-pill census (the clone's superset chrome):**
  the bar mt 16 / radius 8 / pad 12 / bg rgb(254,242,242) /
  space-between; the label 14px red-700; the Cancel pill bg white /
  pad 4px 12px / radius 6 / 12px-500 / **the shadow-sm VISIBLE layer
  `rgba(0, 0, 0, 0.05) 0px 1px 2px 0px`** (the `--shadow-sm` theme pin's
  restored v3 value — the five-site family: item-card:209,
  budget-item-dialog:364, calculator-dialog:286, net-worth-view:123/232,
  all `rounded-md bg-white px-3 py-1 text-xs font-medium text-slate-700
  shadow-sm`); the Delete twin bg red-600 / white / the same pad+radius.
  NOTE: the pill/text colors compute as `lab(...)` strings (Tailwind v4
  emits oklab for the named palette — the v43 named-palette trap) —
  ACCEPTED for these superset-only surfaces (no reference counterpart
  to byte-match; the painted colors are the intended red/slate); the
  shadow-sm VISIBLE layer is the pin that matters (the theme pin's
  regression guard — a Tailwind upgrade that changes the scale fails
  the suite, the v45 net's fifth site).

## Findings

### F1. [PARITY — fix] the value→facts spacing (the 8px gap)

`net-worth-view.tsx` — the AssetCard's value P (:99) and the
LiabilityCard's value P (:202): `mb-2` → `mb-4` (the computed gap 8 →
16px; the card height 186 → 194 = the reference's measured 194; the
reference wraps in a `div.mb-4` while the clone carries the margin on
the P — the computed geometry is the parity contract, the DOM shape is
not, the v45 lesson). The item-card's `mb-4` wrap (item-card.tsx:152)
is the in-repo precedent — the net-worth cards were the oversight.

### F2. [PARITY — pin] the net-worth card census at 1280

One e2e test (`tests/e2e/networth.spec.ts`, `page.setViewportSize(1280)`,
the nw-card-v46 probe ported to the spec's page.evaluate idiom):
the grid 960 / 3 columns × 309.328 / gap 16; the first card 309 wide /
pad 20 / radius 12 / border 1px solid rgb(229,231,227) / the rest
shadow `rgba(0, 0, 0, 0.04) 0px 2px 8px 0px` / bg white / transition
all 0.2s / **h 194 (the F1 fix's assertion — RED before the fix)** /
the value's marginBottom **16px (the F1 fix's second assertion)**; the
title row gap 8 / dot 8×8 rgb(143,188,63) / title 16px-600
rgb(26,58,46); the badge bg rgb(243,244,246) / pad 2px 10px / radius
6 / 12px-600 / rgb(55,65,81); the value 24px-700 rgb(143,188,63); the
facts 12px rgb(107,114,128); the kebab 36×36 / opacity 0; a REAL
`.hover()` leaves the boxShadow UNCHANGED (the inert pin — the inline
beats the utility on both sites) AND reveals the kebab (opacity 0→1).

### F3. [SUPERSET — pin] the confirm-bar white-pill census

One e2e test (`tests/e2e/networth.spec.ts`): open the first asset
card's kebab menu (native click), click Delete (the menu item), then
census the confirm bar — the bar mt 16 / radius 8 / pad 12 / bg
rgb(254,242,242); the Cancel pill bg white / pad 4px 12px / radius 6 /
12px-500 / **the shadow-sm visible layer `rgba(0, 0, 0, 0.05) 0px 1px
2px 0px` (toContain — the accepted-leads convention, the v10 lesson)**;
the Delete twin bg + pad + radius; then click Cancel (the bar
dismisses, the card survives — the fixture-restore discipline). The
reference has NO confirm bars (the v18 direct-delete family) — the pin
is the clone's own superset regression net (the shadow-scale pin's
fifth site, joining the v45 md/lg/sm/2xl pins).

### S1. [MUTATION-SANITY] the pins bite

(a) the value `mb-4` reverted to `mb-2` → the F2 census fails (the
value mb 16→8 AND the card h 194→186);
(b) the pill's `shadow-sm` removed → the F3 pin fails (no shadow
layers);
(c) the card's inline boxShadow 0.04→0.08 → the F2 rest-shadow pin
fails;
(d) the kebab's `group-hover:opacity-100` removed → the F2 hover step
fails (the kebab stays opacity 0 under the REAL hover).
All restored → GREEN.

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v46 paragraph + the e2e count. D2: CLAUDE.md — the
v46 entry + the counts. D3: README — the v46 row + the counts. D4: the
SKILL doc — the Session 81 row, the count sites, the state line. D5:
the PAD — a v1.1.3 revision block. D6: the probe README — the v46
section (the two probes + the drivers + the incident lessons). D7:
session_104.md (the formal log) + session_105.md (the raw transcript) +
the repo worklog Session 80 + the ledger list. D8: the workspace
worklog (/home/z/my-project/worklog.md).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F2 written FIRST (TDD — RED against the mb-2 build: the value mb 8 + the card h 186 fail the 16/194 assertions), then the F1 fix (`mb-2`→`mb-4` on both cards' value P), then F2 GREEN; F3 written (pin-only, GREEN immediately) | test+fix | `tests/e2e/networth.spec.ts` + `net-worth-view.tsx` |
| 2 | The probe scripts persisted + the probe README's v46 section | docs | `scripts/parity-probes/` |
| 3 | S1(a)–(d): the four pin-sanity mutations, each verified to FAIL then restored | verify | `net-worth-view.tsx` |
| 4 | The full chain re-run (108 unit · **223** e2e · 35 smoke + lint + typecheck + build) — all green; the standing VLM pair on the /networth surface at 1280 | verify | — |
| 5 | The 16 screenshots regenerated (the capture script) | docs | `docs/screenshots/` |
| 6 | D1–D8 + the formal session log (session_104.md) + the raw transcript (session_105.md) + the repo worklog Session 80 + the SKILL doc Session 81 row | docs | repo root + `docs/` |
| 7 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/net-worth-view.tsx:99` — the AssetCard's value
  `<p className="mb-2 text-2xl font-bold" style={{ color: ASSET_COLOR }}>`
  (the F1 target; the reference's census: the P mb 0 inside a `mb-4`
  wrap — 16px gap).
- `src/components/budget/net-worth-view.tsx:202` — the LiabilityCard's
  value P, the same `mb-2` (the F1 target's twin).
- `src/components/budget/net-worth-view.tsx:63/:167` — the card wrapper
  `group rounded-xl border bg-white p-5 transition-all duration-200
  hover:shadow-lg` + the inline `borderColor: rgb.border` + `boxShadow:
  rgba(0, 0, 0, 0.04) 0px 2px 8px` (the inline beats the hover utility —
  the F2 inert pin's mechanism; the reference's card: `bg-white
  rounded-xl p-5 group transition-all duration-200 hover:shadow-lg`
  + its own inline border/shadow — the computed census identical).
- `src/components/budget/net-worth-view.tsx:459/:522` — the card grids
  `grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3` (the F2 grid
  pin's target; the reference's asset grid the identical family —
  verified live, 3×309.328 at 1280). The summary card's INNER
  `sm:grid-cols-2` (:355) is NOT the card grid (the v4 G4 stat-blocks
  design — the probe's finder targets `lg:grid-cols-3`).
- `src/components/budget/net-worth-view.tsx:78-84` — the kebab trigger
  `opacity-0 ... focus-visible:opacity-100 group-hover:opacity-100
  data-[state=open]:opacity-100` (the F2 hover-reveal pin).
- `src/components/budget/net-worth-view.tsx:114-155` — the confirm bar
  (`rgb(254, 242, 242)` + the Cancel pill `rounded-md bg-white px-3
  py-1 text-xs font-medium text-slate-700 shadow-sm` + the red Delete —
  the F3 census; the delete-failure catch-toast tier is v18-pinned in
  networth-error.spec.ts, unchanged).
- The e2e contract: the networth spec's existing tests run against the
  seed (assets 65,300 total — 3 assets; the first card = the first
  group's first card); the F2/F3 tests need NO fixture restore beyond
  the confirm bar's own Cancel (the delete never fires — the census
  runs while the bar is up). The REAL `.hover()` idiom is the v43/v44/
  v45 precedent (the synthetic dispatchEvent cannot engage `:hover`).
  The kebab menu open needs a NATIVE Playwright click (the Radix
  dropdown ignores synthetic el.click() — this session's lesson,
  re-confirmed: `agent-browser click` works, `el.click()` does not).
- The chain gate: lint → typecheck → 108 unit → build → 221 e2e
  (**223** after: +2 — F2, F3) → 35 smoke. The two tests add ~8s. The
  F1 production change is the `mb-2`→`mb-4` class swap on two lines
  (no API/store/validation surface touched).
- Execution notes: the F2 test asserts h 194 + value mb 16px — it MUST
  be written before the fix to prove the RED→GREEN cycle (the TDD
  contract). The reference's restore incident (the asset deleted by
  the menu's direct Delete, restored via its Add Asset form) is
  documented in the probe README's v46 lessons — the reference's
  net-worth kebab flow is NEVER safe to probe past the menu open.
