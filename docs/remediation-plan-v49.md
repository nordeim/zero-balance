# Remediation Plan v49 — The Login Panel's Mobile Spacer (THE FIX) +
# the Donut Legend's Mobile Reflow Pin + the Calculator Dialog's 640
# Chrome Pin

Date: 2026-10-12 · Scope: the session-111 v49 queue's first candidate
(the login panel's mobile 390 census — the surface that found ONE REAL
DRIFT, the first production-code change since v46) + the second
candidate (the donut legend's mobile reflow at 390 — pin-only) + the
third candidate (the calculator dialog's 640 chrome — pin-only).
Measured live on BOTH sites via the agent-browser evals (the v49 family:
`ref-v49.sh` + `clone-v49.sh` + `ref-standing-v49.sh` +
`standing-checks-v49.sh`, READ-ONLY on the reference — the calculator
opens via its Calculate click + census + Cancel/X close; no saves, no
deletes, the v46 incident rule).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **229/229 e2e ✓ (5.3m)** · 35/35 smoke ✓. The 43rd standing
checks all clean (mobile-nav R1–R4 both sites — Tailwind v4 pins hold,
the mobile menu works; the reference's toast-blocker re-measured via
elementFromPoint at the burger's center `DIV.fixed top-0 z-[100]`, the
sheet-trap re-verified with the precise overlay census — the z-50
rgba(0,0,0,0.8) scrim STILL open on /income after the nav click, the
no-landmark `navLandmark: false`, the 464 /networth overflow; the data
census read-only — "1 items · $25,000" networth / "1 items · $5000.00"
income intact; the SEO pair live on both sites). npm audit = the same
5 dev-only ESLint-chain advisories (accepted, unchanged;
`--omit=dev` = 0); the secret-pattern scan clean; `.env` ≡
`.env.example` (modulo the dev AUTH_SECRET value); the v48 diff audit
= ZERO src/ changes since 3f00e47 (the pin-only contract confirmed).

## The v49 sweep — what the measurement found

- **THE LOGIN PANEL AT 390 (the session-111 queue #1): ONE REAL DRIFT —
  the reference's mobile-only `&nbsp;` spacer is missing from the
  clone, leaving the clone's card stack 24px BELOW the reference's.**
  Measured on the sign-in state (and re-verified on the sign-up state),
  live on both sites, at 390×844:
  - The reference's login root: `<main class="flex min-h-screen
    items-center justify-center p-4">` — h 844 / minH 844 / flex /
    center / center / pad 16 — IDENTICAL on both sites.
  - The reference's `w-full max-w-md` wrapper carries TWO children: the
    panel (w 358 / h 682 / y 57 / radius 16 / bg rgba(255,255,255,0.95)
    / shadow 2 transparent leads + the v3 2xl layer
    `rgba(0,0,0,0.25) 0px 25px 50px -12px` / contentPad 32 / heading
    24-700-rgb(15,23,42) — all IDENTICAL on the clone) **and a
    mobile-only spacer `<div class="mt-8 text-center text-xs
    text-slate-400 sm:hidden"><p>&nbsp;</p></div>`** — h 16 (the fs-12
    line box), mt 32, color rgb(148,163,184) (#94a3b8, slate-400),
    text-align center, EMPTY content (a bare `&nbsp;`), display none
    at ≥640 (sm:hidden — re-verified live: at 640 the reference's panel
    re-centers to y 111, the spacer display none).
  - The clone's wrapper carries ONE child (the panel) — so its stack is
    682 tall vs the reference's 730 (682 + 32 + 16) and centers at
    y 81 while the reference sits at y 57 — **the whole login card
    renders 24px lower on the clone at mobile**. The panel itself is
    byte-identical (w/h/radius/shadow-visible-layer/bg/heading/pad); the
    drift is the stack's vertical position ONLY.
  - The v12/v13 login pins were measured at DESKTOP (1280) where
    `sm:hidden` hides the spacer — invisible there, never measured.
    The v24 auth-forms mobile census walked the CONTROLS, never the
    panel's position. First-time measurement at 390 catches it.
- **THE DONUT LEGEND AT 390 (the session-111 queue #2): BYTE-PARITY on
  every visible axis — PIN-ONLY.** Measured on the dashboard's Spending
  Breakdown legend, live on both sites, at 390×844 (leaf-node census):
  - The container: display flex / flex-direction column / gap 12px /
    mt 24px — IDENTICAL (the clone's `mt-6 flex flex-col gap-3`).
  - The row (Need): h 64 / radius 8px / pad 12px / bg
    rgb(245,248,245) — IDENTICAL (`rounded-lg p-3` + the inline tint).
  - The dot: 16×16 / radius 4px / bg rgb(224,122,59) (the Need slice's
    orange) — IDENTICAL (`h-4 w-4 rounded` + CLASSIFICATION_COLORS).
  - The leaves: the label SPAN "Need" fs 16 / fw 500 /
    rgb(26,58,46) — IDENTICAL; the amount P fs 16 / fw 700 /
    rgb(224,122,59) (the classification color) — IDENTICAL; the pct P
    fs 12 / fw 400 / rgb(107,114,128) — IDENTICAL; the right block
    text-align right — IDENTICAL.
  - The svg legend icon: w 16 / color rgb(224,122,59) — IDENTICAL.
  - The row width: the reference 313 vs the clone 308 — the EXACT 5px
    of the reference's own /dashboard horizontal overflow (its docSW
    395 vs the clone's 390 — the documented superset-fix-#4 bug; the
    reference's card rides its own overflow). A data/platform class,
    not a chrome gap (the v46/v47 lesson).
  - The row's inherited color (rgb(10,10,10) vs rgb(23,23,23) — the
    neutral vs accent foreground inheritance) never renders: every text
    leaf on both sites carries an explicit color. Invisible divergence.
  - The v44 F3 census measured BOTH viewports but only PINNED 1280 —
    the v49 pin locks the 390 reflow.
- **THE CALCULATOR DIALOG AT 640 (the session-111 queue #3): BYTE-PARITY
  on every visible axis — PIN-ONLY.** Measured on the Rent calculator
    (hover → Calculate → census → X close), live on both sites, at
    640×960:
  - The panel: w 608 (640 − the 2×16 overlay padding) / x 16 /
    radius 16px / maxW 768px (max-w-3xl) / maxH 816px (85vh of 960) /
    bg rgb(255,255,255) / overflow hidden / flex column — IDENTICAL.
  - The shadow: the reference 2 transparent leads + **the v3 2xl layer
    `rgba(0,0,0,0.25) 0px 25px 50px -12px`** vs the clone's
    `.zb-modal-panel` custom-class emission of **the SAME single
    visible layer** (no leads — the accepted lead-divergence class,
    v10/v25/v45; the clone's custom class simply emits the visible
    layer directly).
  - The close button: 36×36 — IDENTICAL. The header's border-b: 1px
    solid rgb(229,231,227) — IDENTICAL. The panel vertically centered
    (y 223 = (960−515)/2, h 515 on both — data-coincident, the pin
    asserts the centering invariant + the chrome, never the absolute
    content height). sw 640 — IDENTICAL.
  - The v45 F2b test already pins the 640 WIDTHS (panelW 608 / rowW
    560 / sw 640) after a line-item add; the v49 pin adds the chrome
    census (radius/maxW/maxH/shadow/bg/overflow/close/header border)
    on the read-only open state.

## Findings

### F1. [FIX] the login panel's mobile-only spacer + the 24px stack offset

One production change (`src/components/budget/login-card.tsx`): add the
reference's mobile-only spacer as the SECOND child of the
`w-full max-w-md` wrapper (a sibling of the panel — it applies to every
auth state: sign-in / sign-up / forgot):

```jsx
{/* v49 F1: the reference's mobile-only spacer — an empty &nbsp; line
    (mt-8 text-center text-xs text-slate-400 sm:hidden) below the panel
    that lifts the card stack 24px above the geometric center at 390
    (the reference's panel y 57 vs the clone's pre-fix 81). The color is
    pinned as #94a3b8 (slate-400's hex) — Tailwind v4's named slate
    computes as oklab() (the v7 login-family rule); the content is a
    bare &nbsp; so the color never renders, but the census pins it
    byte-exact anyway. Hidden at sm+ — the desktop centering (and every
    v12/v13 desktop pin) is unchanged. */}
<div className="mt-8 text-center text-xs text-[#94a3b8] sm:hidden">
  <p>&nbsp;</p>
</div>
```

One e2e test (`tests/e2e/login-parity.spec.ts`, a new
`test.describe("login panel mobile census (v49 — plan F1)")` with
`test.use({ viewport: { width: 390, height: 844 } })`): goto /login,
wait for the heading, census — the wrapper (w 358 / h **730** — 682 +
32 + 16), the panel (y **57** / h 682 / w 358), the spacer (h 16 /
mt 32 / fs 12 / color rgb(148,163,184) / ta center / text "\u00A0" /
display block); then `page.setViewportSize(640, 960)` — the spacer
`display: none`, the panel re-centered (y == round((960 − h)/2)).

### F2. [PIN] the donut legend's mobile reflow at 390

One e2e test (`tests/e2e/dashboard.spec.ts` —
`setViewportSize(390, 844)` then the / census): the legend container
(display flex / flexDirection column / gap 12px / mt 24px / w 308), the
first row (w 308 / h 64 / radius 8px / pad 12px / bg
rgb(245,248,245)), the dot (16×16 / radius 4px / bg rgb(224,122,59)),
the leaf census (the label fs 16 / fw 500 / rgb(26,58,46); the amount
fs 16 / fw 700 / rgb(224,122,59); the pct fs 12 / fw 400 /
rgb(107,114,128)), the right block (ta right), the svg icon (w 16 /
color rgb(224,122,59)). The row w 308 (NOT 313 — the reference's 313
rides its own 395 docSW overflow; the clone's superset fix keeps 390).

### F3. [PIN] the calculator panel's chrome census at 640

One e2e test (`tests/e2e/calculator.spec.ts` —
`setViewportSize(640, 960)`, the read-only open flow: hover the Rent
card → Calculate → census → Close): the panel (w 608 / x 16 / radius
16px / maxW 768px / maxH 816px / bg rgb(255,255,255) / overflow
hidden), the boxShadow toContain **`rgba(0, 0, 0, 0.25) 0px 25px 50px
-12px`** (the 2xl visible layer), the close button 36×36, the header
border-b 1px solid rgb(229,231,227), the centering invariant (y ==
round((960 − h)/2)), sw 640. No fixture restore needed (the read-only
open + close leaves the seed untouched; the Rent amount is never
recalculated — no line items are added or deleted).

### S1. [MUTATION-SANITY] the pins bite

(a) the spacer removed → the F1 pin fails (the wrapper h 730→682, the
panel y 57→81);
(b) the spacer's `mt-8` → `mt-4` → the F1 pin fails (the wrapper h
730→722, the panel y 57→69);
(c) the spacer's `sm:hidden` removed → the F1 640 sub-check fails (the
spacer display block at 640, the panel y drifts off-center);
(d) the legend row's `p-3` → `p-2` → the F2 pin fails (pad 12→8, h
64→56);
(e) the `.zb-modal-panel` box-shadow removed → the F3 pin fails (no 2xl
layer);
(f) the calculator's inline `maxHeight: "85vh"` → `"90vh"` → the F3 pin
fails (maxH 816→864).
All restored → GREEN. **Each mutation needs the standalone REBUILD
before the run bites** (the v47/v48 execution lesson — the e2e suite
runs against the BUILD, not the source tree).

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v49 paragraph. D2: CLAUDE.md — the v49 entry + the
counts. D3: README — the v49 row + the counts. D4: the SKILL doc — the
Session 84 row, the count sites, the state line. D5: the PAD — a
v1.1.6 revision block. D6: the probe README — the v49 section (the
drivers + the lessons). D7: session_113.md (the formal log) +
session_114.md (the raw transcript) + the repo worklog Session 83 +
the ledger list. D8: the workspace worklog
(/home/z/my-project/worklog.md).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1 — the spacer added (the production fix) + its pin written RED first (the pre-fix run must FAIL: the wrapper 682 / y 81), then GREEN after the fix (TDD — the first production change since v46) | fix+test | `src/components/budget/login-card.tsx` + `tests/e2e/login-parity.spec.ts` |
| 2 | F2 + F3 written (pin-only — GREEN immediately against the unchanged build, the TDD pin discipline: the pin proves the parity, the mutations prove the pin) | test | `tests/e2e/dashboard.spec.ts` + `tests/e2e/calculator.spec.ts` |
| 3 | The probe scripts persisted + the probe README's v49 section | docs | `scripts/parity-probes/` |
| 4 | S1(a)–(f): the six pin-sanity mutations, each verified to FAIL then restored (each preceded by `npm run build` — the v47/v48 lesson) | verify | `src/components/budget/login-card.tsx` + `src/components/budget/dashboard-view.tsx` + `src/app/globals.css` + `src/components/budget/calculator-dialog.tsx` |
| 5 | The full chain re-run (108 unit · **232** e2e · 35 smoke + lint + typecheck + build) — all green; the standing VLM pair on a fresh surface | verify | — |
| 6 | The 16 screenshots regenerated (the capture script) | docs | `docs/screenshots/` |
| 7 | D1–D8 + the formal session log (session_113.md) + the raw transcript (session_114.md) + the repo worklog Session 83 + the SKILL doc Session 84 row | docs | repo root + `docs/` |
| 8 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/login-card.tsx:555` — the `w-full max-w-md`
  wrapper; the panel is its ONLY child (lines 556–723). The F1 insertion
  point: after the panel's closing `</div>` (line ~723), before the
  wrapper's closing `</div>` (line ~724) — a sibling at the same indent
  level, so every auth state (the mode ternary lives INSIDE the panel)
  carries it.
- The existing login pins are desktop-measured and desktop-run (the
  login-parity specs default to the 1280×800 viewport; the v24 mobile
  describe pins the CONTROLS, never the panel y) — the F1 fix changes
  NOTHING at ≥640 (`sm:hidden`), so no existing pin moves.
- `src/components/budget/dashboard-view.tsx:772–805` — the legend markup
  (`mt-6 flex flex-col gap-3`, the row `flex items-center justify-between
  rounded-lg p-3` + the inline rgb(245,248,245), the dot `h-4 w-4
  rounded`, the label `font-medium` + forestDark, the amount
  `font-bold` + CLASSIFICATION_COLORS, the pct `text-xs` + rgb.gray,
  the right block `text-right`, the icon `h-4 w-4` + the classification
  color) — the F2 target, byte-verified against the reference census.
- `src/components/budget/calculator-dialog.tsx:99–107` — the DialogContent
  inline overrides (`maxWidth: "48rem"`, `maxHeight: "85vh"`, `overflow:
  "hidden"`, `display: "flex"`, `flexDirection: "column"`) over the
  `.zb-modal-panel` base (`src/app/globals.css:347` — fixed/centered,
  radius 1rem, `box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25)`,
  `width: calc(100% - 2rem)`, overflow-y auto) — the F3 target.
- The e2e contract: the specs run AUTHENTICATED via the setup project's
  storageState (the dashboard + calculator specs); the login specs opt
  out (their own describe with no storageState — the v24 precedent at
  login-parity.spec.ts:564). The calculator opens via the v45 idiom
  (`div.rounded-xl` filter hasText "Rent" → hover → Calculate); the
  legend census reuses the v44 F3 finder idioms
  (`div.flex.flex-col.gap-3.mt-6`, the leaf regex finders).
- The chain gate: lint → typecheck → 108 unit → build → 229 e2e
  (**232** after: +3 — F1, F2, F3) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every Playwright run
  (the v46 lesson). The reference probes this session were READ-ONLY
  (the calculator opened + censused + closed via X/Cancel; the login
  state swap sign-in→sign-up is a client state change; no data
  mutations, no Delete clicks — the v46 incident rule).
- The VLM pair: a fresh surface for the v49 screening — the /dashboard
  at 390 post-fix (the login card's mobile position is the fixed
  surface; the dashboard's mobile donut + hero is the fresh census
  surface). Expected flags: the demo data values + the reference's own
  395 overflow (the 2-card grid data class, the avatar initial — the
  v43/v47/v48 lesson family).
