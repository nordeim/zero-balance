# Remediation Plan v50 — The Auth States' Panel Heights (THE FIX —
# the v4 space-y × `-mb-2` override) + the Networth Tablist's 640
# Chrome Pin + the Dashboard Hero's Mobile Reflow Pin

Date: 2026-10-12 · Scope: the session-115 v50 queue's three candidates
(the auth states' full 390 census — the surface that found ONE REAL
DRIFT, the second production-code change since v46) + the networth
tablist's chrome at 640 + the dashboard hero's mobile reflow at 390.
Measured live on BOTH sites via the agent-browser evals (the v50
family: `ref-v50.sh` + `clone-v50.sh`, READ-ONLY on the reference —
the auth state swaps sign-in→sign-up→forgot are client state changes,
the v49 precedent; no form submits, no data mutations, the v46
incident rule).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **232/232 e2e ✓ (5.4m)** · 35/35 smoke ✓. The 44th standing
checks all clean (mobile-nav R1–R4 both sites — Tailwind v4 pins hold,
the mobile menu works; the reference's sheet-trap re-verified with the
precise overlay census — the z-50 rgba(0,0,0,0.8) scrim still open on
/income after the nav click; the toast-blocker via elementFromPoint at
the burger's center; the no-landmark; the 464 /networth overflow; the
data census read-only — "1 items · $25,000" networth / "1 items ·
$5000.00" income intact; the SEO pair live on both sites). npm audit =
the same 5 dev-only ESLint-chain advisories (accepted, unchanged;
`--omit=dev` = 0); the secret-pattern scan clean (the parity-probe
reference credentials are the by-design probe inputs, not secrets);
`.env` ≡ `.env.example` (modulo the dev AUTH_SECRET value).

## The v50 sweep — what the measurement found

- **THE AUTH STATES AT 390 (the session-115 queue #1): ONE REAL DRIFT —
  the clone's sign-up and forgot panels are 16px SHORT at every
  viewport (406 vs 422 sign-up; 294 vs 310 forgot).** Measured on the
  reference's sign-up AND forgot states (the client state-swap
  idiom), live on both sites, at 390×844:
  - The sign-in state is BYTE-IDENTICAL (the v49 F1 contract holds:
    the wrapper 730 / the panel 682 / y 57 — re-verified this sweep).
  - The reference's sign-up: the wrapper 470 / the panel 422 / y 187
    (the centered stack); the forgot: the wrapper 358 / the panel 310
    / y 243. The clone: 454/406/y 195 and 342/294/y 251 — the panels
    16px short, the wrappers 16px short, the y 8px low (the
    centering arithmetic follows the height).
  - The inner census isolates the drift to ONE junction: the back
    button → the heading. The reference (v3-era space-y semantics:
    margin-top on `> * + *`): the button (h 20, its own `-mb-2` =
    -8) + the heading's mt 16 COLLAPSE to a net 8px gap (the heading
    at rel y 28). The clone (v4 space-y semantics:
    `:where(& > :not(:last-child))` margin-block-end, ZERO
    specificity): the button's own `-mb-2` utility OVERRIDES the
    container's margin-bottom (16 → -8) — so the heading lands at rel
    y 12, OVERLAPPING the button by 8px, and the container loses 16px
    (the heading→form gap is 16 on both sites; the form heights are
    IDENTICAL — 286 sign-up / 126 forgot).
  - ROOT CAUSE: the trap-log rule 4 violation — "no `mt-*`/`mb-*`
    utilities on children of `space-y-*` containers" — the clone's
    back button carries the reference's OWN `-mb-2` idiom, which
    stacks under v3 semantics but overrides under v4's
    zero-specificity `:where()`. The same class as the v9 G3 (the
    dialogs' space-y-2 inline-label collapse) and the v24 G2 (the
    auth-card's space-y-1.5) — the SPACE-Y V3 SEMANTICS family's
    THIRD member, this time on a BLOCK child with its own margin
    utility.
  - BONUS FINDING (the forgot container's sm tier): the reference's
    forgot inner container is `space-y-4 sm:space-y-6` (24px gaps at
    ≥640); the clone's is `space-y-4` (16px at every viewport). The
    sign-up container is `space-y-4` on BOTH sites (no sm tier).
  - The verify-email state shares the same construction idiom (the
    `-mb-2` back button + a `space-y-4` container, login-card.tsx:603)
    — the same fix applies; its reference measurement is inherited
    from the v21 live session (a fresh reference registration is a
    write — out of bounds under the v46 read-only discipline; the
    verify panel's full census is a future-queue candidate).
- **THE NETWORTH TABLIST AT 640 (the session-115 queue #2): BYTE-PARITY
  on every visible axis — PIN-ONLY.** Measured on the /networth
  tablist (Assets/Liabilities), live on both sites, at 640×960:
  - The list: w 448 / h 36 / display grid / gridTemplateColumns
    "220px 220px" / bg rgb(245,245,245) / radius 8px / pad 4px / x 16
    / y 534 — IDENTICAL (the v14 G2 `grid w-full max-w-md
    grid-cols-2`).
  - The active trigger (Assets): w 220 / h 28 / radius 6px / fs 14px /
    fw 500 / color rgb(20,83,45) / bg rgb(220,252,231) / a 2-slot
    shadow with 2 transparent layers (`rgba(0,0,0,0) 0px 0px 0px 0px,
    rgba(0,0,0,0)...` — the data-[state=active]:shadow emission) /
    the 16×16 lucide icon at currentColor rgb(20,83,45) — IDENTICAL.
  - The inactive trigger (Liabilities): w 220 / h 28 / radius 6px /
    fs 14px / fw 500 / color rgb(115,115,115) / bg transparent /
    shadow none / the 16×16 icon at rgb(115,115,115) — IDENTICAL.
  - The v14 G2 tab-icons pin + the v30 G2 roving keyboard contract +
    the EXISTING 1280 tablist test (the 448 grid / the green active
    pair) hold; the v50 pin adds the 640 mid-viewport + the fuller
    chrome (radius/fs/fw/shadow/pad/icons/gridCols).
- **THE DASHBOARD HERO AT 390 (the session-115 queue #3): BYTE-PARITY
  on every visible axis — PIN-ONLY.** Measured on the dashboard's hero
  (the NET ZERO GOAL card + the Net Zero Breakdown card), live on both
  sites, at 390×844:
  - The hero grid: display grid / 1 column (362.5px ref vs 358px
    clone — the reference's own 395 docSW overflow, the documented
    superset-fix-#4 family) / gap 24px / 2 children — the goal card
    316@y 253 + the breakdown card 324@y 593 (the 24px rhythm:
    253+316+24 = 593 ✓ on BOTH sites) — IDENTICAL.
  - The goal card: radius 16 / pad 32 / the 135deg forest gradient /
    the shadow rgba(26,58,46,0.3) 0px 20px 60px — IDENTICAL. The
    clone's docSW 390 (no overflow — the superset fix).
  - The internals: the icon circle 48×48 / bg rgba(143,188,63,0.2) /
    the 24px target icon at rgb(143,188,63); the H3 18/700/white/lh
    28; the sublabel 14/rgba(255,255,255,0.6); the allocation label
    14/rgba(255,255,255,0.8); the pct 18/600/white; the track
    12px/rgba(255,255,255,0.1)/9999px radius; the fill's
    90deg-status gradient (the under-budget orange
    rgb(224,122,59)→rgb(245,169,98))/9999px; the balance box
    radius 12/pad 24/bg rgba(255,255,255,0.05)/blur(10px); the
    Balance label 14/0.6; the figure 30/700/white — IDENTICAL (the
    fill WIDTH and the figure TEXT are data-dependent — never
    pinned).
  - THE CHIP (a shared artifact): both sites render the under-budget
    chip as a flex gap-8 center row with the 20px lucide
    trending-up SQUISHED to 12px wide (flex-shrink under the row's
    width pressure — `w-5 h-5` classed but 11.7px computed) at
    rgb(245,169,98) + the "Under Budget" span 16/600
    rgb(245,169,98) — the squish is IDENTICAL on both sites (the
    chipBox 93 / the left figure block 158 on both). A data-pressure
    class, byte-shared — the pin locks the family, not the artifact.

## Findings

### F1. [FIX] the auth states' 16px panel shortfall (the v4 space-y ×
### `-mb-2` override) + the forgot's sm tier

Two production changes:

1. `src/app/globals.css` — the SPACE-Y V3 SEMANTICS block (the v9 G3 /
   v24 G2 family) gains the scoped third member:

```css
/* v50 F1 (docs/remediation-plan-v50.md): the auth card's non-signin
   mode containers — the reference's `space-y-4 [sm:space-y-6]` under
   v3's margin-top-on-following-sibling semantics. The back button
   carries the reference's OWN -mb-2; under v4's zero-specificity
   :where(& > :not(:last-child)) margin-block-end the utility
   OVERRIDES the container gap (the heading overlaps the button by
   8px, the panel 16px short at every viewport) where the reference's
   v3 build STACKS them (the collapsed 16 + (-8) = the 8px net gap —
   the sign-up panel 422 / the forgot 310 at 390). The forgot
   container's sm tier (the reference's space-y-4 sm:space-y-6) rides
   the zb-sm6 modifier — 24px at >=640. */
.zb-auth-mode > :not(:last-child) { margin-block-end: 0; }
.zb-auth-mode > * + * { margin-block-start: 1rem; }
@media (min-width: 640px) {
  .zb-auth-mode.zb-sm6 > * + * { margin-block-start: 1.5rem; }
}
```

2. `src/components/budget/login-card.tsx` — line 693 (the shared
   signup/forgot container): `space-y-4` →
   `zb-auth-mode${mode === "forgot" ? " zb-sm6" : ""}`; line 603 (the
   verify branch's container): `space-y-4` → `zb-auth-mode`.

One e2e test (`tests/e2e/login-parity.spec.ts`, a new
`test.describe("auth-mode panel census (v50 — plan F1)")` with
`test.use({ viewport: { width: 390, height: 844 } })`): the sign-up
state — the panel 422 / the wrapper 470 / the panel y 187 / the
button→heading net gap 8 / the heading→form gap 16; the forgot state —
the panel 310 / the wrapper 358 / y 243; then
`page.setViewportSize(640, 960)` — the forgot container's heading mt
24px (the sm:space-y-6 contract; the sign-up's stays 16).

### F2. [PIN] the networth tablist's chrome at 640

One e2e test (`tests/e2e/networth.spec.ts` — a 640×960 describe or a
setViewportSize flow): the list (w 448 / h 36 / grid "220px 220px" /
bg rgb(245,245,245) / radius 8px / pad 4px / x 16); the active
trigger (w 220 / h 28 / radius 6px / fs 14 / fw 500 / color
rgb(20,83,45) / bg rgb(220,252,231) / a shadow string CONTAINING 2
transparent layers / the 16×16 icon at rgb(20,83,45)); the inactive
trigger (w 220 / h 28 / radius 6px / fs 14 / fw 500 / color
rgb(115,115,115) / bg transparent / shadow none / the 16×16 icon at
rgb(115,115,115)).

### F3. [PIN] the dashboard hero's mobile reflow at 390

One e2e test (`tests/e2e/dashboard.spec.ts` — `setViewportSize(390,
844)`): the hero grid (display grid / 1 column / gap 24px / 2
children); the goal card (w 358 / h 316 / radius 16 / pad 32 / the
135deg forest gradient / the shadow `rgba(26, 58, 46, 0.3) 0px 20px
60px 0px`); the breakdown card (w 358 / h 324 / y = the goal y + 316
+ 24); the icon circle (48×48 / rgba(143,188,63,0.2) / the 24px svg
at rgb(143,188,63)); the H3 (18/700/white/lh 28); the sublabel
(14/rgba(255,255,255,0.6)); the allocation row (the label
14/rgba(255,255,255,0.8); the pct 18/600/white); the track (h 12 /
rgba(255,255,255,0.1) / 9999px); the fill (the 90deg
rgb(224,122,59)→rgb(245,169,98) gradient / 9999px — the under-budget
status of the seed); the balance box (radius 12 / pad 24 /
rgba(255,255,255,0.05) / blur(10px)); the Balance label (14/0.6); the
figure (30/700/white); the chip (the flex gap 8 center row / the span
16/600 rgb(245,169,98) / the svg color rgb(245,169,98)); docSW 390.

### S1. [MUTATION-SANITY] the pins bite

(a) the `zb-auth-mode` class removed (the container back to
`space-y-4`) → the F1 pin fails (the sign-up panel 422→406);
(b) the back button's `-mb-2` removed → the F1 pin fails (the
button→heading gap 8→16, the panel +8);
(c) the forgot's `zb-sm6` modifier removed → the F1 640 sub-check
fails (the heading mt 24→16);
(d) the trigger's `data-[state=active]:bg-[#dcfce7]` removed → the F2
pin fails (the active bg transparent);
(e) the hero track's `h-3` → `h-2` → the F3 pin fails (the track h
12→8).
All restored → GREEN. **Each mutation needs the standalone REBUILD
before the run bites** (the v47/v48/v49 execution lesson — the e2e
suite runs against the BUILD, not the source tree).

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v50 paragraph. D2: CLAUDE.md — the v50 entry + the
counts. D3: README — the v50 row + the counts. D4: the SKILL doc — the
Session 85 row, the count sites, the state line. D5: the PAD — a
v1.1.7 revision block. D6: the probe README — the v50 section (the
drivers + the lessons). D7: session_116.md (the formal log) +
session_117.md (the raw transcript) + the repo worklog Session 84 +
the ledger list. D8: the workspace worklog
(/home/z/my-project/worklog.md).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1 — the RED pin first (the pre-fix run must FAIL: the sign-up panel 406 / the forgot 294 / the heading overlap), then the globals.css + login-card.tsx fix, then GREEN (TDD — the second production change since v46) | fix+test | `src/app/globals.css` + `src/components/budget/login-card.tsx` + `tests/e2e/login-parity.spec.ts` |
| 2 | F2 + F3 written (pin-only — GREEN immediately against the unchanged build, the TDD pin discipline: the pin proves the parity, the mutations prove the pin) | test | `tests/e2e/networth.spec.ts` + `tests/e2e/dashboard.spec.ts` |
| 3 | The probe scripts persisted + the probe README's v50 section | docs | `scripts/parity-probes/` |
| 4 | S1(a)–(e): the five pin-sanity mutations, each verified to FAIL then restored (each preceded by `npm run build`) | verify | `src/components/budget/login-card.tsx` + `src/components/ui/tabs.tsx` + `src/components/budget/dashboard-view.tsx` |
| 5 | The full chain re-run (108 unit · **236** e2e · 35 smoke + lint + typecheck + build) — all green; the standing VLM pair on a fresh surface | verify | — |
| 6 | The 16 screenshots regenerated (the capture script) | docs | `docs/screenshots/` |
| 7 | D1–D8 + the formal session log (session_116.md) + the raw transcript (session_117.md) + the repo worklog Session 84 + the SKILL doc Session 85 row | docs | repo root + `docs/` |
| 8 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/login-card.tsx:693` — the shared signup/forgot
  container `<div className="space-y-4">` (the back button at 694–701
  carries `-mb-2`; the heading block 702–713; the AuthForm 714). The
  F1 class swap lands on line 693.
- `src/components/budget/login-card.tsx:603` — the verify branch's own
  `<div className="space-y-4">` (its back button at 606–613 also
  carries `-mb-2`) — the family fix's second site.
- `src/app/globals.css:19–50` — the SPACE-Y V3 SEMANTICS block (the
  v9 G3 space-y-2 + the v24 G2 space-y-1.5 restores) — the v50 rules
  append inside the same `@layer utilities` block.
- The existing pins are SAFE: the v12/v13 login pins walk the CONTROLS
  (the 44px inputs, the placeholders, the rings — never the panel
  height or y); the v24 mobile auth census walks the controls; the
  v49 F1 pin walks the SIGN-IN state only (its container is the
  `space-y-6 sm:space-y-8` outer flex — block children without own
  margin utilities, v3/v4 layout-equivalent — untouched by the fix);
  the v21/v23/v33 verify-email pins walk the controls (the circle /
  the h2 / the code inputs — never the container spacing).
- `src/components/ui/tabs.tsx:30–38` — the trigger classes (the
  `data-[state=active]:bg-[#dcfce7] text-[#14532d]` + the shadow) —
  the F2 target, byte-verified against the reference census.
- `src/components/budget/dashboard-view.tsx:946–953` — the hero grid
  (`grid grid-cols-1 gap-6 lg:grid-cols-3` — 1-col + 24px at 390);
  `:64–160` — the NetZeroGoalCard internals (the icon circle, the
  track `h-3`, the balance box `rounded-xl p-6` + the
  `backdropFilter: blur(10px)` inline, the chip's `h-5 w-5` icons) —
  the F3 target, byte-verified against the reference census.
- The e2e contract: the networth + dashboard specs run AUTHENTICATED
  via the setup project's storageState; the login specs opt out (the
  v24 precedent at login-parity.spec.ts:564). The F1 pin reuses the
  v49 F1 describe's viewport idiom (390×844 + the 640 sub-check).
- The chain gate: lint → typecheck → 108 unit → build → 232 e2e
  (**235** after: +3 — F1, F2, F3) → 35 smoke.
- Execution notes: `pkill -f agent-browser` + a stale-session-file
  sweep (`rm -f ~/.agent-browser/<session>.*`) before every
  agent-browser run — a killed run leaves a stale `.config`/`.engine`
  pair that hangs the next `agent-browser open` on that session name
  (THE v50 probe lesson — the first clone-v50 run hung 600s on the
  stale `clone50` session). The Playwright runs need
  `npx playwright install chromium` on a fresh sandbox (the
  chromium_headless_shell-1243 download).
- The VLM pair: a fresh surface for the v50 screening — the /login
  sign-UP state at 390 (THE FIXED SURFACE — the panel-position family,
  a data-free static form; the expected flags: the reference's own
  Base44 FAB only, the v49 precedent).
