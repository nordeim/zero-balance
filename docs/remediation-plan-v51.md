# Remediation Plan v51 — The Verify-Email Container's Missing
# `.zb-auth-mode` Conversion (THE FIX — completing the v50 F1's
# claimed-but-never-applied third site) + Four 390 Pin Surfaces

Date: 2026-10-12 · Scope: the session-118 v51 queue's read-only members
(the verify-email panel census — which found ONE REAL GAP this session;
the savings goal-card mobile census; the hero stats-card row's 390
reflow) + two sibling sweep surfaces the same session added (the Budget
Guidelines card at 390 + the quick-actions row at 390). Measured live on
BOTH sites via the agent-browser evals (the v51 family: `ref-v51.sh` +
`clone-v51.sh`, READ-ONLY on the reference — no form submits, no data
mutations, no auth state writes; the v46 incident rule).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **236/236 e2e ✓ (5.4m)** · 35/35 smoke ✓. The 45th standing
checks all clean (mobile-nav R1–R4 both sites — Tailwind v4 pins hold,
the mobile menu works; the reference's sheet-trap re-verified via the
overlayCount census — the z-50 scrim remains after the nav click; the
toast-blocker via elementFromPoint; the no-landmark; the 464 /networth
overflow; the data census read-only — "1 items · $25,000" networth /
"1 items · $5000.00" income intact; the SEO pair live on both sites).
npm audit = 0 production vulnerabilities (the same 5 dev-only
ESLint-chain advisories, accepted, unchanged); the secret-pattern scan
clean (the parity-probe reference credentials are the by-design probe
inputs); `.env` ≡ `.env.example` (modulo the dev AUTH_SECRET value).

## The v51 sweep — what the measurement found

- **THE VERIFY-EMAIL MODE CONTAINER (the session-118 queue's deferred #1,
  resolved WITHOUT a reference write): ONE REAL GAP — the v50 F1's
  THIRD-site conversion was CLAIMED but NEVER APPLIED.** The v50 plan
  (§F1) and the v50 commit message both state "the verify-email branch's
  same-idiom container converted" — and the v50 diff DID add the
  describing comment at login-card.tsx:605-607 — but the class swap
  itself never landed: line 608 still reads `<div className="space-y-4">`
  where the plan says it should read `zb-auth-mode`. The consequence is
  the SAME drift the v50 F1 fixed for sign-up/forgot, still live on the
  verify state:
  - Measured on the clone (a fresh registration — the clone's own DB, a
    sanctioned write on OUR side), at 390×844: the panel 358×492 @ y 152,
    the wrapper 540, and the junction **netGap −8** — the centered inner
    stack's top (y 196) sits 8px ABOVE the back button's bottom (y 204):
    the button's own `-mb-2` (−8) OVERRIDES v4's zero-specificity
    `:where(& > :not(:last-child))` margin-block-end (16) where the
    reference's v3 build STACKS them (the collapsed 16 + (−8) = the 8px
    NET gap) — the inner stack overlaps the button by 8px and the panel
    is 16px short.
  - The expected POST-FIX geometry (the v3-stacking arithmetic, the same
    contract the v50 F1 pinned for sign-up 422/470 and forgot 310/358):
    the junction netGap **+8** (the button bottom 204 → the inner top
    212), the panel **508** (492 + 16), the wrapper **556** (540 + 16),
    the panel y **144** (152 − 8, the centering arithmetic follows the
    height). The inner stack's own height (416) is unchanged — the fix
    only restores the junction arithmetic.
  - The reference-side measurement is INHERITED (the v50 plan's own
    justification: the v21 live session registered a throwaway account
    and censused the verify state's structure — the same "-mb-2 back
    link + space-y-4" idiom; a fresh v51 reference registration is a
    WRITE, out of bounds under the v46 read-only rule). The structural
    identity + the v50's proven arithmetic carry the contract; the pin
    locks the v3-stacking semantics, the mutations prove the pin.
  - ROOT CAUSE (process): the v50 session applied the signup/forgot
    swap (line 705) and wrote the verify-site comment, but the line-608
    class swap was lost between the plan and the diff — the docs
    (AGENTS/CLAUDE/README/SKILL/worklog) all describe the conversion as
    done. The v51 fix closes BOTH the drift and the doc-vs-code
    mismatch (no doc retraction needed — the code now matches what the
    docs already claim).
- **THE DASHBOARD STATS ROW AT 390 (the session-118 queue #3): BYTE-PARITY
  on every visible axis — PIN-ONLY.** Measured on the dashboard's three
  StatCards (Total Income / Total Savings / Total Expenses), live on both
  sites, at 390×844:
  - The grid: display grid / 1 column / gap 24px / 3 children — IDENTICAL
    (the v50 F3's hero grid sibling, the same `grid grid-cols-1 gap-6
    md:grid-cols-3` idiom).
  - The cards: h 210 each @ y 949 / 1183 / 1417 (the 24px rhythm:
    949+210+24 = 1183 ✓ on BOTH sites) — IDENTICAL.
  - The first card: radius 16px / pad 24px / border 1px solid
    rgb(229,231,227) / bg white / shadow rgba(0,0,0,0.06) 0px 4px 20px
    0px — IDENTICAL.
  - The internals: the icon circle 48×48 / radius 12px / bg
    rgba(143,188,63,0.125); the 24×24 lucide icon at rgb(143,188,63);
    the H3 title 14/500/rgb(107,114,128)/mb 4; the amount 30/700/
    rgb(26,58,46)/mb 16; the count row 14px / gap 8px (the span "1
    item"/"2 items" — data class); the divider + the 16×16 trending icon
    — IDENTICAL.
  - The widths: the reference's 363 rides its own 395 docSW overflow
    (the documented superset-fix-#4 family); the clone's 358 fits
    (docSW 390) — the accepted width class, the heights and rhythm
    byte-identical.
- **THE SAVINGS VIEW AT 390 (the session-118 queue #4): BYTE-PARITY on
  every chrome axis — PIN-ONLY.** Measured on the /savings view, live on
  both sites, at 390×844:
  - The goal card: radius 12px / pad 20px / border 1px solid
    rgb(229,231,227) / bg white / shadow rgba(0,0,0,0.04) 0px 2px 8px
    0px — IDENTICAL.
  - The card internals: the H4 title 16/600/rgb(26,58,46); the subtitle
    14/400/rgb(107,114,128); the amount 24/700/rgb(59,126,161) (the
    savings blue); the 8×8 accent dot at rgb(59,126,161) / radius
    9999px; the badge chips 12/600 (the CLASSIFICATION_BADGES /
    frequency / status chrome, byte-identical per value — the v48
    verification); the footer row 16px with the 12px icons — IDENTICAL.
  - The card grid: 1 column / gap 16px — IDENTICAL.
  - The view chrome: the H1 "Savings" 30/700/rgb(26,58,46); the count
    sub 16/rgb(107,114,128); the filter card 358 wide / radius 16px /
    pad 24px / white; the search input 308×36 — IDENTICAL. docSW 390 on
    both (the /savings route is overflow-free on the reference too).
  - The card HEIGHT is a data class, never pinned: the clone's richer
    seed renders 4 chips (classification + frequency + Recurring +
    status) that wrap to 2 rows (the badges row 52px) where the
    reference's 3 chips fit 1 row (22px) — the measured clone card 230
    vs the reference's 200, the drift fully accounted for by the seed
    (the v48 VLM-pair's documented data-divergence family).
- **THE BUDGET GUIDELINES CARD AT 390 (the sibling sweep): BYTE-PARITY
  on every visible axis — PIN-ONLY.** Measured on the dashboard's
  Budget Guidelines card, live on both sites, at 390×844:
  - The card: h 380 / radius 12px / border 1px solid rgb(229,231,227) /
    bg white / the shadow's VISIBLE pair rgba(0,0,0,0.1) 0px 1px 3px
    0px + rgba(0,0,0,0.1) 0px 1px 2px -1px (the reference's FULL
    string re-measured UNSLICED: 2 transparent leads + the pair = 4
    layers; the clone: 4 leads + the pair = 6 — the accepted
    lead-divergence class, v10/v25/v45/v49/v50) — IDENTICAL.
  - The tiles container: display block / 3 children (the `space-y-3
    p-6 pt-0` stack) — IDENTICAL.
  - The three tiles: radius 8px / pad 16px / h 94, 94, 78 — IDENTICAL.
    Needs: bg rgb(255,247,245) / border rgb(252,221,213) / label
    16/500/rgb(224,122,59) / pct "~50%" 14px; Wants: bg
    rgb(240,247,251) / border rgb(212,233,245) / rgb(59,126,161) / "~30%";
    Savings: bg rgb(245,249,240) / border rgb(223,236,208) /
    rgb(143,188,63) / "~20%"; the desc 12/rgb(107,114,128) — all
    byte-identical. The tile widths (313 vs 308) ride the reference's
    own 395 overflow family.
- **THE QUICK-ACTIONS ROW AT 390 (the sibling sweep): BYTE-PARITY on
  every visible axis — PIN-ONLY.** Measured on the dashboard's three
  quick-action cards (Add Income / Add Savings / Add Expense), live on
  both sites, at 390×844:
  - The grid: 1 column / gap 24px / 3 children — IDENTICAL.
  - The cards: h 90 each @ y 2751 / 2865 / 2979 (the 114px rhythm =
    90 + 24 ✓ on BOTH sites — the full-page vertical rhythm identical
    through the whole dashboard) — IDENTICAL.
  - The card: radius 16px / pad 24px / border 1px solid
    rgb(229,231,227) / bg white / shadow none (the rest state) —
    IDENTICAL.
  - The internals: the 40×40 icon circle `w-10 h-10 rounded-xl` /
    bg rgba(143,188,63,0.125) / the group-hover:scale-110
    transition-transform idiom; the 20×20 lucide icon at
    rgb(143,188,63); the label 16/500/rgb(26,58,46); the trailing plus
    16×16 `ml-auto opacity-50 group-hover:opacity-100
    transition-opacity` at rgb(143,188,63) — the class strings
    byte-identical (the reference's own DOM classes read directly).
  - The wrapper element tag diverges (the reference wraps in a DIV, the
    clone in a SPAN — both `flex items-center gap-3`, identical
    computed chrome; tag-agnostic).

## Findings

### F1. [FIX] the verify-email mode container's missing `.zb-auth-mode`
### conversion (the v50 F1's third site, claimed but never applied)

One production change:

1. `src/components/budget/login-card.tsx` line 608 — the verify branch's
   mode container: `space-y-4` → `zb-auth-mode` (the comment at
   605-607 already describes exactly this; the class swap is the
   missing half). NO `.zb-sm6` modifier — the reference's verify
   container carries no sm tier (the v21-measured structure), unlike
   the forgot branch.

One e2e test (`tests/e2e/verify-email.spec.ts`, a new
`test.describe("verify-mode panel census (v51 — plan F1)")` with
`test.use({ viewport: { width: 390, height: 844 } })`, logged-OUT like
the file's other verifies, registering a throwaway account via the
existing `registerFreshAccount` helper): the panel 358×508 @ y 144, the
wrapper 556, the junction netGap +8 (the back button h 20 / mb −8 / the
inner stack's top 8px below the button's bottom), the h2 20/700 anchor.
RED against the current build (the panel 492 / the wrapper 540 / the
netGap −8 / the y 152) → the one-class fix → GREEN.

### F2. [PIN] the dashboard stats row's census at 390

One e2e test (`tests/e2e/dashboard.spec.ts` — a 390×844 describe or a
setViewportSize flow): the grid (display grid / 1 col / gap 24px / 3
children); the three cards (358×210 @ y 949, 1183, 1417 — the 24px
rhythm); the first card's chrome (radius 16 / pad 24 / border / white /
the shadow rgba(0,0,0,0.06) 0px 4px 20px 0px); the icon circle (48×48 /
radius 12 / rgba(143,188,63,0.125)); the icon (24×24 /
rgb(143,188,63)); the title (14/500/rgb(107,114,128)/mb 4); the amount
(30/700/rgb(26,58,46)/mb 16); the count row (14px / gap 8px); the trend
icon (16×16).

### F3. [PIN] the savings view's goal card + view chrome at 390

One e2e test (`tests/e2e/items.spec.ts` — the savings describe's 390
extension): the goal card (radius 12 / pad 20 / border / white / the
shadow rgba(0,0,0,0.04) 0px 2px 8px 0px); the H4 (16/600/
rgb(26,58,46)); the subtitle (14/400/rgb(107,114,128)); the amount
(24/700/rgb(59,126,161)); the dot (8×8 / rgb(59,126,161) / 9999px);
the grid (1 col / gap 16); the H1 "Savings" (30/700/rgb(26,58,46)); the
sub (16/rgb(107,114,128)); the filter card (358 / radius 16 / pad 24);
the search (308×36); docSW 390. The card HEIGHT and the badge COUNT are
data-dependent (the richer seed's 4-chip wrap) — never pinned.

### F4. [PIN] the Budget Guidelines card's census at 390

One e2e test (`tests/e2e/dashboard.spec.ts` — the same 390 describe):
the card (358×380 / radius 12 / border / white / the shadow CONTAINING
the visible pair rgba(0,0,0,0.1) 0px 1px 3px 0px +
rgba(0,0,0,0.1) 0px 1px 2px -1px); the tiles container (display block /
3 children); the tiles (radius 8 / pad 16 / h 94, 94, 78); the Needs /
Wants / Savings tile chrome (the three tinted bg/border pairs + the
label 16/500 + the pct 14px + the desc 12/rgb(107,114,128)).

### F5. [PIN] the quick-actions row's census at 390

One e2e test (`tests/e2e/dashboard.spec.ts` — the same 390 describe):
the grid (1 col / gap 24 / 3 children); the cards (358×90 @ y 2751,
2865, 2979 — the 114px rhythm); the card chrome (radius 16 / pad 24 /
border / white / shadow none); the icon circle (40×40 / radius 12 /
rgba(143,188,63,0.125)); the icon (20×20 / rgb(143,188,63)); the label
(16/500/rgb(26,58,46)); the trailing plus (16×16 / opacity 0.5 /
rgb(143,188,63)).

### S1. [MUTATION-SANITY] the pins bite

(a) the verify container's `zb-auth-mode` removed (back to `space-y-4`)
→ the F1 pin fails (the TDD RED run — the pre-fix proof);
(b) a stat card's `rounded-2xl` → `rounded-xl` → the F2 pin fails (the
radius 16 → 12);
(c) the savings goal card's inline shadow removed → the F3 pin fails;
(d) the Needs tile's inline bg removed → the F4 pin fails;
(e) the quick-action circle's `w-10 h-10` → `w-8 h-8` → the F5 pin
fails (the circle 40 → 32).
All restored → GREEN. **Each mutation needs the standalone REBUILD
before the run bites** (the v47–v50 execution lesson — the e2e suite
runs against the BUILD, not the source tree).

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v51 paragraph. D2: CLAUDE.md — the v51 entry + the
counts. D3: README — the v51 row + the counts. D4: the SKILL doc — the
Session 86 row, the count sites, the state line. D5: the PAD — a
v1.1.8 revision block. D6: the probe README — the v51 section (the
drivers + the lessons). D7: session_119.md (the formal log) +
session_120.md (the raw transcript) + the repo worklog Session 85 + the
ledger list. D8: the workspace worklog
(/home/z/my-project/worklog.md).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1 — the RED pin first (the pre-fix run must FAIL: the panel 492 / the wrapper 540 / the netGap −8 / the y 152), then the one-class login-card.tsx fix (line 608: `space-y-4` → `zb-auth-mode`), then GREEN (TDD — the third production change since v46, completing the v50 F1's claimed third site) | fix+test | `src/components/budget/login-card.tsx` + `tests/e2e/verify-email.spec.ts` |
| 2 | F2 + F4 + F5 written (pin-only — GREEN immediately against the unchanged build, the TDD pin discipline: the pin proves the parity, the mutations prove the pin) | test | `tests/e2e/dashboard.spec.ts` |
| 3 | F3 written (pin-only — the savings goal card + the view chrome) | test | `tests/e2e/items.spec.ts` |
| 4 | The probe scripts persisted + the probe README's v51 section | docs | `scripts/parity-probes/` |
| 5 | S1(a)–(e): the five pin-sanity mutations, each verified to FAIL then restored (each preceded by `npm run build`) | verify | `src/components/budget/login-card.tsx` + `src/components/budget/dashboard-view.tsx` + `src/components/budget/item-card.tsx` |
| 6 | The full chain re-run (108 unit · **241** e2e · 35 smoke + lint + typecheck + build) — all green; the standing VLM pair on a fresh surface | verify | — |
| 7 | The 16 screenshots regenerated (the capture script) | docs | `docs/screenshots/` |
| 8 | D1–D8 + the formal session log (session_119.md) + the raw transcript (session_120.md) + the repo worklog Session 85 + the SKILL doc Session 86 row | docs | repo root + `docs/` |
| 9 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/login-card.tsx:608` — the verify branch's mode
  container `<div className="space-y-4">` (its back button at 610–616
  carries `-mb-2`); the v50-added comment at 605–607 already describes
  the intended `zb-auth-mode` conversion. The F1 class swap lands on
  line 608.
- `src/app/globals.css:62–76` — the SPACE-Y V3 SEMANTICS block's
  `.zb-auth-mode` rule pair (the v50 F1) + the `.zb-sm6` modifier —
  the fix REUSES the existing rules; no CSS change needed. The verify
  container takes NO `zb-sm6` (the reference's verify container has no
  sm tier).
- The existing pins are SAFE: the v21/v23/v33 verify-email pins walk
  the CONTROLS (the circle 56 / the icon 28 / the six 40×44 inputs at
  x 60–290 / the 294×44 button / the h2 20/700) — never the panel
  height, the wrapper, or the junction; the v22 G1 pointer-parking
  discipline applies to the new test's chrome reads (the
  registerFreshAccount helper already parks at (5,5) + waits 350ms);
  the v50 F1 pins cover the SIGN-UP and FORGOT states only (the verify
  state's mode container is a SEPARATE JSX branch — the fix touches
  no pinned surface).
- `src/components/budget/dashboard-view.tsx:953` — the stats row grid
  (`mt-8 grid grid-cols-1 gap-6 md:grid-cols-3`); `:549–620` — the
  StatCard (the circle `h-12 w-12 rounded-xl` + hexToRgba(color, 0.125),
  the H3 `text-sm font-medium` + rgb.gray, the amount `text-3xl
  font-bold` + rgb.forestDark mb-4 — wait: the reference's amount mb is
  16px and the clone's P carries `mb-4` (16px) ✓; the count row `flex
  items-center gap-2 text-sm`) — the F2 target, byte-verified against
  the reference census.
- `src/components/budget/dashboard-view.tsx:825–860` — the
  BudgetGuidelinesCard (the card `rounded-xl border bg-card shadow` +
  the inner `space-y-3 p-6 pt-0`; the tiles `rounded-lg p-4` + the
  inline bgColor/borderColor; the label `font-medium`; the pct
  `text-sm`; the desc `text-xs` + rgb.gray) — the F4 target.
- `src/components/budget/dashboard-view.tsx:873–905` — the
  QuickActionCard (the button `group rounded-2xl border p-6 text-left`;
  the span `flex items-center gap-3`; the circle `h-10 w-10
  rounded-xl` + hexToRgba(color, 0.125) + `group-hover:scale-110
  transition-transform`; the label span `font-medium` + forestDark; the
  PlusIcon `ml-auto h-4 w-4 opacity-50 transition-opacity
  group-hover:opacity-100`) — the F5 target.
- `src/components/budget/item-card.tsx:73–80` — the goal card (the
  `rounded-xl` (12px) + `p-5` (20px) + the inline
  `boxShadow: "rgba(0, 0, 0, 0.04) 0px 2px 8px"` — byte-verified against
  the reference census); `:116–160` — the title block + the dot `h-2
  w-2 rounded-[9999px]` + the amount `text-2xl font-bold` + the badges
  row — the F3 target.
- The e2e contract: the dashboard + items specs run AUTHENTICATED via
  the setup project's storageState (the deterministic seed — the
  y-position pins 949/1183/1417 and 2751/2865/2979 are stable across
  runs; the global-setup re-seeds db/e2e.db fresh every run); the
  verify-email spec opts OUT (the logged-out surface, its own
  throwaway registrations — the rate-limit budget: the file's 5
  existing register-class calls + this test's 1 = 6, still under the
  10/IP/15min bucket).
- The chain gate: lint → typecheck → 108 unit → build → 236 e2e
  (**241** after: +5 — F1, F2, F3, F4, F5) → 35 smoke.
- Execution notes: `pkill -f agent-browser` + a stale-session-file
  sweep (`rm -f ~/.agent-browser/<session>.*`) before every
  agent-browser run (the v50 probe lesson); a rebuild swaps
  `.next/standalone` UNDER a running parity server — reboot the :3200
  server after every build; the with-server heredoc KILLS its server at
  the end — every follow-up eval needs a fresh invocation (the v51
  probe lesson: the "Network error" mid-flow).
- The VLM pair: a fresh surface for the v51 screening — the /savings
  view at 390 (THE F3 SURFACE — the goal-card family, a data-divergent
  surface; the expected flags: the reference's own Base44 FAB + the
  seed-data classes, the v48 precedent).
- DEFERRED queue (unchanged, both need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side verify-email
  panel census (a registration) and the reference-side forgot-confirm
  state census (a reset-link submit). The v51 F1's reference contract
  rides the v21-inherited structure + the v50's proven arithmetic.
