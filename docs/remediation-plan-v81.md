# Remediation Plan v81 — the re-run cycle's next-oldest candidate (the v59-era login + calculator pair's third re-run) + the axe watch + the calculator header/addBtn/scrim census pin (PIN-ONLY)

The formal narrative: `docs/session_192.md`. The queue: the session-191
continuation of the v80 plan's v81 suggestion — **the ledger-verified
target** (the v80 plan's suggestion AGREEING with the rotation ledger:
the v59-era login + calculator pair [the login view + the calculator
dialog at desktop 1280], last re-shot v75, is the oldest remaining
candidate [v75 < v76 < v77 < v78 < v79 < v80]; the pair's THIRD re-run
[v59 → v66 → v75 → v81] — the FOURTH consecutive queue/ledger
agreement), plus the axe-core watch at its re-check point and the 75th
standing checks. **PIN-ONLY for src/ — no production-code change; +1
e2e = 284.**

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered; the standalone static + public copies verified) ·
283 e2e ✓ (100 + 108 + 77 chunk executions = 283 unique tests in 23
files [282 chromium + 1 setup, the setup re-run per chunk as the
project dependency] — the exact documented v80 state) · 35/35 smoke ✓.
The workspace PRESERVED across the session boundary (no reset; the
environment verified in place — `.env` DATABASE_URL="file:../db/custom.db",
`db/` at the repo root, node_modules intact, no orphaned servers; the
seedcheck exact [7 items / rent 1850 / expenses 2235 / 0 line items /
3 assets / 2 liabilities] before any flow ran).

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next
prereleases; no 5.x exists), the lockfile holding the v68 dedupe state
(the wrapper 4.14.0 + ONE hoisted axe-core 4.14.0, no nested engine
dir), the engine-contract pin GREEN standalone (2 passed).

### F2 — the 75th standing checks: ALL GREEN (version-bumped from v74 — version-bump-only diffs verified)

The mobile menu VERIFIED WORKING (the 75th consecutive time —
`hitIsBurgerChild:true`, the sheet opens + closes on nav, the nav
landmark present); the reference's four bugs ALL live [toast-blocker,
sheet-trap `overlayCount:1`, no-landmark, the 464px /networth
overflow]; the data census UNCHANGED (the 75th clean drift check:
networth "1 items · $25,000" / income "1 items · $5000.00" /
expenses "4 items · $525.00"); the SEO pair live; zero overflow at 390
on all five clone views.

### F3 — the re-run pair (the login view + the calculator dialog at desktop 1280x800)

**The LOGIN pair: VERDICT IDENTICAL, ZERO style flags** (matching the
v75 re-run's own IDENTICAL verdict — zero drift since v75 on the VLM
layer). The both-sides census byte-identical on every axis: the card
448/16px/rgba(255,255,255,0.95); the h1 30/700/lh 36px/rgb(15,23,42);
the subtitle 16px/rgb(100,116,139); the logo 96×96; the inputs
48/12px/14px/1px rgb(226,232,240); the Sign in
368×48/12px/14px/500/rgb(15,23,42); the Google + OR blocks both
present. The card's 0px-width border computed-color (ref slate-200 form
vs clone's border token) and the shadow's transparent lead-layer count
are the v66 computed-form INVISIBLE class — both surfaces render
identically.

**The CALCULATOR pair: VERDICT DIFFERENT with THREE flags, every one
DOM-arbitrated to a documented class** (matching the v75 re-run's own
flag-set classes — the same three mechanisms):

1. the "extra will-update line" — the v66 DATA-CONDITIONAL class
   (`hasWillUpdateSpan` ref FALSE [its Rent natively $25.00 === its
   line-item total] vs clone TRUE [opened-at $1850 ≠ the recalculated
   $25.00]);
2. the "hover action buttons missing in the clone" — the v75
   POINTER-POSITION class (a screenshot-timing perception artifact: the
   reference's shot is taken with the pointer still inside the dialog
   after the Calculate click, the clone's shot after the parked-pointer
   move — the DOM census: `actionsAtRest {opacity: 0, btnCount: 2}`
   BYTE-IDENTICAL on both sides);
3. the "row height shorter in the clone" — a VLM MISREAD (the v43
   misattribution lesson's live case: the row measures 720×102
   BYTE-IDENTICAL on both sides).

The both-sides census otherwise BYTE-IDENTICAL on every chrome axis
(the v75 axes re-measured): the panel 768×393/16px/white/maxW 768px;
the scrim rgba(26,58,46,0.5)/blur(8px)/1280×800; **the title
18px/700/lh 28px/rgb(26,58,46)**; **the desc 14px/lh 20px/
rgb(107,114,128)**; the close 36×36; the totalCard
720×90/16px/12px/1px solid rgb(252,221,213); the nameH4 16/600/h 24/mb
4px; the row 720×102/16px/12px/1px solid rgb(229,231,227); the
pillRow/pill1 family; the amountP 20/700/rgb(224,122,59)/h 28; **the
addBtn 110×32/radius 6px/12px/500/white**; the docSW 1280 guard on
both sides. The panel shadow's transparent lead-layer count is the v66
computed-form class (the visible layer byte-identical). The clone
twin's fixture FULLY restored (the delete + Rent's $1850 re-edit + the
"$2235.00" page-total verify; the seedcheck exact after).

**NO NEW GAP — the v81 iteration is PIN-ONLY.**

### F4 [PIN] — the calculator dialog's header family + Add Item button + scrim census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 284)

The never-pinned axes (the existing pins cover around them: the v53 F2
pin holds the panel/header/chip/close/totalCard/row/addBtn GEOMETRY at
**390 only**; the v59 F1 pin holds the panel + totalCard chrome +
closeBtn/hdrBorder at 1280 [no title/desc/addBtn/scrim]; the v66 F3
pin holds the row/height FAMILY at 1280 [body interior only]; the v73
F4 pin holds the scrim + summary-text at **390 only**; the v45 F2a pin
holds the row census + hover reveal at 1280):

- **The TITLE's typography family at 1280** (the arbitration's own
  measured values, byte-identical on both sides): fs 18px / fw 700 /
  lh 28px / color rgb(26,58,46) — the v53 pin's 390 {fs, fw, color}
  twin completed with the NEVER-pinned lh axis, at the pair viewport.
- **The DESC's typography family at 1280**: fs 14px / color
  rgb(107,114,128) / lh 20px — the v73 390 family's desktop twin.
- **The Add Item BUTTON's chrome at 1280**: w 110 / h 32 / radius
  6px / fs 12px / fw 500 / color rgb(255,255,255) — the v53 390
  family's desktop twin (the radius never pinned at any viewport).
- **The SCRIM at 1280**: bg rgba(26,58,46,0.5) / blur blur(8px) /
  w 1280 / h 800 — the v73 390 family's desktop twin (the full-viewport
  fixed overlay).
- The docSW 1280 guard.

The pin rides the **v59 read-only EMPTY-state discipline** (hover →
Calculate → census → Close): every pinned axis (title/desc/addBtn/
scrim) is STATIC dialog chrome — none depends on the line-item data —
so the empty state measures the same values the 1-row census measured
(no fixture add/restore burden).

**The pin-sanity mutation**: the DialogTitle's ` lg:text-xl`
(calculator-dialog.tsx:127 — `text-lg font-bold` + ` lg:text-xl`)
— flips EXACTLY the title.fs axis at 1280 ("18px" → "20px") and
nothing else (the mutation is viewport-scoped: at 390 the lg: variant
is inert — the v53 h2 pin {fs 18px, fw 700, color} stays GREEN; the
v53 header.h 101 stays GREEN; the v73 390 scrim/summary family stays
GREEN; at 1280 the v59 pin asserts panel w/radius/maxW/maxH/bg/
overflow/shadow + closeBtn {36,36} + hdrBorder + totalCard — none
title-dependent, the panel.y centering invariant holds for ANY panel
height; the v66 height family lives in the panel BODY — unaffected by
the header's title size; the v45 F2a row census unaffected) —
cascade-free by construction, then restored (the standalone REBUILD
as a SEPARATE command; `git diff src/` = 0 lines).

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → `npm run build` → **284 e2e** in chunks
(+1) → 35 smoke; the 16 standing screenshots regenerated + byte-
compared (the same-DB discipline; the seedcheck under
`env -u DATABASE_URL`). EXPECTED: any DATE-class diff pixel-arbitrated
per the v66/v75 discipline, never a full-page VLM verdict.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the calculator's title/desc typography + addBtn chrome + scrim census at 1280 + the docSW guard (read-only empty state) | tests/e2e/calculator.spec.ts |
| 2 | sanity | the pin-sanity mutation: the DialogTitle's ` lg:text-xl` (calculator-dialog.tsx:127) → the pin FAILS at exactly the title.fs axis ("18px" → "20px"); restored → GREEN (the standalone REBUILD as a SEPARATE command) | src/components/budget/calculator-dialog.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 284 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v81 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (283→284 + the v81 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v81 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 116 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.38 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v81 section (the new probes + the ledger-verified queue note) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_192.md + the repo worklog Session 116 entry | docs/session_192.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the arbit-v81.sh census's own measured
  values, byte-identical on both sides' calculator dialogs at
  1280x800 (the 1-row state): the title `{fs: "18px", fw: "700",
  color: "rgb(26, 58, 46)", lh: "28px"}`; the desc `{fs: "14px",
  color: "rgb(107, 114, 128)", lh: "20px"}`; the addBtn `{w: 110,
  h: 32, radius: "6px", fs: "12px", fw: "500", color:
  "rgb(255, 255, 255)"}`; the scrim `{bg: "rgba(26, 58, 46, 0.5)",
  blur: "blur(8px)", w: 1280, h: 800}`; the docSW 1280.
- The source confirms the values: the DialogTitle `text-lg font-bold`
  + the inline forestDark color (calculator-dialog.tsx:127 — text-lg
  = 18px/lh 28px); the DialogDescription `text-sm` + the inline gray
  (line 129-131 — 14px/lh 20px); the Add Item button
  `zb-btn-add zb-btn-add-sm text-white` + the calculator gradient
  (lines 174-181); the scrim the `.zb-modal-overlay` fixed inset-0
  forest family (the v73 census's own values at the 1280 viewport).
- The pin-sanity target: the DialogTitle's ` lg:text-xl` flips ONLY
  the title.fs axis at 1280 ("18px" → "20px") — the v81 pin's own
  headline axis; viewport-scoped so the 390 families (v53's h2/header,
  v73's scrim/summary) are untouched; grep-verified: the ONLY other
  h2 assertion is the v53 390 pin (no fs/lh at 1280 anywhere); the
  v59/v66/v45 1280 pins assert no title-dependent axis; the header
  height is not pinned at 1280; the panel.y invariant holds for any
  panel height.
- The existing pins are SAFE: the v59 pin's panel/totalCard/closeBtn/
  hdrBorder (disjoint from title/desc/addBtn/scrim — the v81 pin
  adds, never duplicates); the v66 pin's height family (the panel
  BODY — disjoint from the header); the v53 pin's 390 family (a
  different viewport); the v73 pin's 390 scrim family (a different
  viewport — the v81 pin is the desktop twin of the same values).
- The blast radius: ZERO production-code change (every census delta a
  documented class — the pin-only line holds); the pin-sanity mutation
  touches `src/components/budget/calculator-dialog.tsx:127` (the
  DialogTitle's className) REVERTED before ship (`git diff src/` = 0
  lines at commit).
- The chain gate: lint → typecheck → 108 unit → `npm run build` →
  283 e2e (**284** after: +1 — the F4 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every agent-browser
  run; the with-server boots fresh per command; the reference session
  EXPIRES between long eval gaps — the login-retry loop handles it;
  the e2e chunks pass FULL file paths; `ss -tlnp | grep :3100` + kill
  before every full-chain run (the v53 orphaned-webServer lesson);
  one-shot Prisma scripts need `env -u DATABASE_URL`; no dollar
  sequences in census JS inside double-quoted bash strings (the v64
  rule); no attribute-value selectors in the census (the v78 rule —
  geometry + text-content filters only); the QUOTED heredoc with the
  env-injected census (the v73 lesson); the mutations need the
  standalone REBUILD as a SEPARATE command (the v53 lesson); the
  clean-check gate re-runs AFTER every new file lands (the v69
  lesson); the build step is `npm run build` (the v76 F0 lesson).
- The deferred queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census, the line-items dialog
  glyphs.
- The v82 queue (suggestions): (1) the re-run cadence rotates to the
  next-oldest candidate after this pair (the v60-era networth +
  drill-down pair [the networth view + the dashboard drill-down
  EXPANDED at 1280], last re-shot v76 — now the oldest remaining
  [v76 < v77 < v78 < v79 < v80 < v81]), (2) the axe-core watch at its
  next re-check point (only a 5.x wrapper changes the calculus), (3)
  the deferred reference-write censuses (unchanged).
