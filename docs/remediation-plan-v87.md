# Remediation Plan v87 — the re-run cycle's next-oldest candidate (the v81-era login + calculator pair's fourth re-run) + the axe watch + the calculator close-button chrome census pin (PIN-ONLY)

The formal narrative: `docs/session_210.md`. The queue: the v86 plan's v87
suggestion — **the ledger-verified target** (the v86 plan's suggestion
AGREEING with the rotation ledger: the v81-era LOGIN + CALCULATOR pair
[the login view + the calculator dialog at desktop 1280x800], last
re-shot v81, is the oldest remaining candidate [v81 < v82 < v83 < v84 <
v85 < v86]; the pair's FOURTH re-run [v59 → v66 → v75 → v81 → v87] — the
TENTH consecutive queue/ledger agreement), plus the axe-core watch at its
re-check point and the 81st standing checks. **PIN-ONLY for src/ — no
production-code change; +1 e2e = 290.**

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered) · **291 e2e chunk executions ✓** (102 + 110 + 79
across three chunk splits of the 23 files = 289 unique tests — the same
unique count as the documented v86 state's 291 = 289) · 35/35 smoke ✓.
The workspace PRESERVED (no reset — the v81 precedent): `git pull`
fast-forwarded `5c4818e..40cee12` (the session_209 transcript only), the
tree clean; the environment verified in place (.env
[DATABASE_URL="file:../db/custom.db"], db/ at the repo root with
custom.db + e2e.db, node_modules + prisma, chromium-1243); the seedcheck
exact (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2
liabilities) before any flow ran, no orphaned servers.

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next
prereleases beyond — no stable 4.14.1, no 5.x exists), npm-latest
`axe-core` 4.14.0; the lockfile holding the v68 dedupe state (the
wrapper 4.14.0 + ONE hoisted axe-core 4.14.0 — no nested engine dir
under `node_modules/@axe-core/playwright/`); the engine-contract pin
GREEN standalone (2 passed).

### F2 — the 81st standing checks: ALL GREEN (version-bumped from v80 — version-bump-only diffs verified)

ref-standing-v81.sh + standing-checks-v81.sh (version-bumped from v80
— after normalizing the THREE token families [v80→v81, 80th→81st, AND
the bare-number session names ref80→ref81 / clone80→clone81 — the v84
lesson's third family] the files are byte-identical: only the header
comment, the AGENT_BROWSER_SESSION names, and the done echo differ).
Reference side: the four bugs ALL live [toast-blocker
`hitIsBurgerChild:false`; sheet-trap `overlayCount:1`; no-landmark
`navLandmark:false`; the 464px /networth overflow at 390]; the data
census UNCHANGED (the 81st clean drift check: networth "1 items ·
$25,000" / income "1 items · $5000.00" / expenses "4 items · $525.00");
the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation
menu VERIFIED WORKING (the **81st consecutive time**:
`hitIsBurgerChild:true`, the sheet opens, closes on nav, the nav
landmark present), zero overflow at 390 on all five views (docSW 390
everywhere), the SEO pair live.

### F3 — the re-run pair (the v81-era login + calculator pair: the login view + the calculator dialog at desktop 1280x800)

**The LOGIN pair: VERDICT IDENTICAL, zero style flags** (matching the
v75 and v81 re-runs' own IDENTICAL verdicts — zero drift since v75 on
the VLM layer; the VLM's only note the reference's "Edit with Base44"
FAB, the platform-chrome class). The both-sides census
byte-identical on every axis: the card 448/0px-pad/16px/
rgba(255,255,255,0.95); the h1 30px/700/lh 36px/rgb(15,23,42); the
subtitle 16px/rgb(100,116,139); the logo 96×96; the inputs
48/12px/14px/1px rgb(226,232,240); the Sign in
368×48/12px/14px/500/rgb(15,23,42); the Google + OR blocks both
present; the docSW 1280 guard. The card's 0px-width border
computed-color (ref slate-200 form vs the clone's border token) and
the shadow's transparent lead-layer count are the v66 computed-form
INVISIBLE class — both surfaces render identically.

**The CALCULATOR pair: VERDICT DIFFERENT with THREE flags, every one
DOM-arbitrated to a documented class — the SAME three flag-set classes
as the v75 and v81 re-runs (zero drift in the mechanism classes):**

1. the "extra will-update line" — the v66 DATA-CONDITIONAL class
   (`hasWillUpdateSpan` ref FALSE [its Rent natively $25.00 === its
   line-item total] vs clone TRUE [opened-at $1850 ≠ the recalculated
   $25.00]);
2. the "hover action buttons missing in the clone" — the v75/v81
   POINTER-POSITION perception class (the reference's shot taken with
   the pointer still inside the dialog after the Calculate click, the
   clone's after the parked-pointer move — the DOM census:
   `actionsAtRest {opacity: 0, btnCount: 2}` BYTE-IDENTICAL on both
   sides);
3. the "row height shorter in the clone" — a VLM MISREAD (the v43
   misattribution lesson's standing case: the row measures 720×102
   BYTE-IDENTICAL on both sides).

**The both-sides census (arbit-v87.sh — the v75 convention: the census
runs regardless of the verdict; the v81 census axes re-measured): the
v81 census values REPRODUCED EXACTLY — zero drift since v81 on every
axis:**

- **The PANEL + SCRIM + TITLE + DESC + TOTALCARD + NAMEH4 + ROW +
  PILLROW + PILL1 + AMOUNTP + ADDBTN chrome BYTE-IDENTICAL** (the panel
  768×393/16px/white/maxW 768px; the scrim
  rgba(26,58,46,0.5)/blur(8px)/1280×800; the title
  18px/700/lh 28px/rgb(26,58,46); the desc 14px/lh 20px/
  rgb(107,114,128); the totalCard 720×90/16px/12px/1px solid
  rgb(252,221,213); the nameH4 16/600/h 24/mb 4px; the row
  720×102/16px/12px/1px solid rgb(229,231,227); the pillRow
  flex/8px/12px/h 20; the pill1 20/65/2px 8px/9999px/12px/400; the
  amountP 20px/700/rgb(224,122,59)/h 28; the addBtn
  110×32/radius 6px/12px/500/white); the panel shadow's transparent
  lead-layer count the v66 computed-form class (the visible layer
  byte-identical); the docSW 1280 guard on both sides.
- **The CLOSE button — a NEW REFERENCE-SIDE OBSERVATION (the v87
  cycle's own finding): the reference's calculator close button has
  LOST its accessible name** (the button-inventory probe
  close-arbit-v87.sh: `aria:""`, `txt:""` — the × rendered as a bare
  SVG with no aria-label and no text content; the arbit census's
  name-based finder returns no match on the ref side this cycle, while
  the v81 census found it via the name). **The CHROME is UNCHANGED and
  byte-identical on both sides**: 36×36 / radius 6px / bg
  rgba(0,0,0,0) / border 0px (the ref's 0px-border computed-color
  rgb(229,229,229) vs the clone's token — the v66 INVISIBLE class).
  The CLONE retains aria-label="Close" — the SUPERSET behavior (the
  v56 superset family: the reference regressing its own a11y while the
  clone keeps the working state), already functionally pinned by every
  calculator.spec.ts interaction (`getByRole("button", { name:
  "Close" })` — the accessible-name contract fails the suite if
  removed). NO production-code change (the clone's behavior is the
  intended superset; PIN-ONLY holds).

**NO NEW CLONE GAP — the v87 iteration is PIN-ONLY.**

### F4 [PIN] — the calculator close-button chrome census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 290)

The never-pinned axes (the existing pins cover around them: the v59 F1
pin holds the closeBtn's {w, h} GEOMETRY at 1280 only — never the
radius, the bg, the border-width, or the display; the v49 F3 pin the
{36,36} at 640; the v53 F2 pin the {29,36} at 390; grep-verified: no
spec asserts the close button's radius, background, or border at ANY
viewport; the v81 pin the title/desc/addBtn/scrim; the v66 pin the
row-height family; the v45 F2a pin the row census + hover reveal):

- **The CLOSE button's full chrome at 1280** (calculator-dialog.tsx:138
  — the `inline-flex h-9 w-9 items-center justify-center rounded-md`
  header button): {w 36, h 36, radius "6px", bg "rgba(0, 0, 0, 0)",
  borderTopWidth "0px", display "flex"} — the v59 geometry family's
  chrome completion at the pair viewport, byte-identical on both sides
  (the pair-arbit-v87.sh census's own measured values); the
  0px-border computed-COLOR axis EXCLUDED (the v66 computed-form
  INVISIBLE class — the width pinned, never the color);
- the docSW 1280 guard.

Every pinned axis STATIC chrome (the close button's geometry and
surface classes are unconditional — no data, no viewport conditionals);
the pin rides the v59/v81 read-only EMPTY-state discipline (hover →
Calculate → census → Close — no fixture writes, the Rent amount never
recalculated), in tests/e2e/calculator.spec.ts (the v59/v66/v81 pins'
own file).

**The LOGIN half's never-pinned axes — census-recorded this cycle
(byte-identical on both sides at 1280, per the pair-arbit-v87.sh
census) and DEFERRED to the pair's next rotation** (the +1-per-cycle
convention): the card's outer pad "0px" + borderTopWidth "0px"; the
inner content pad "48px 40px 40px" (the md:px-10 md:pt-12 md:pb-10
state); the logo img's own radius "0px" (the visual circle lives on
the parent span's rounded-[9999px] + overflow-hidden). Recorded here
as the future pin's expected values.

**The pin-sanity mutation (the executed form — the viewport-scoped
responsive-variant dodge, the v80/v86 pattern)**: the close button's
`rounded-md` → `rounded-md lg:rounded-lg` (calculator-dialog.tsx:138,
applied by LINE NUMBER) — flips EXACTLY the pin's close.radius axis
("6px" → "8px") and nothing else: the responsive variant is inert
below 1024px (the v49 640 pin and the v53 390 pin untouched); a
border-radius change alters NO width/height (the button's fixed h-9
w-9 — every w/h-asserting pin [v49 {36,36}, v53 {29,36}, v59 {36,36}]
GREEN under the mutation by construction); no other spec asserts the
close radius at any viewport; the bg/border/display axes unaffected —
**cascade-free by construction** (the expected failure diff reads as
the close.radius axis alone), then restored (the standalone REBUILD as
a SEPARATE command; `git diff src/` = 0 lines; the post-restore full
run green).

**The disproven-in-advance candidates (documented without execution —
the design-probe analysis)**: (1) an fs-axis mutation on the close
button's icon — REFUTED by the v86 RATIO-LINE-HEIGHT TRAP lesson (any
font-size override scales the icon's line-height; and no text axis is
pinned here anyway); (2) a login-side pad mutation (the inner pad's
`md:pt-12` → `md:pt-14`) — REFUTED by the pad-family's height cascade
(the +8px top pad grows the card's height, cascading every
card-height-dependent expectation in the v7/v9/v12/v24 families) — the
login axes are NOT pinned this cycle, so no login mutation is needed;
the close-radius mutation alone demonstrates the pin's failure
semantics.

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → `npm run build` → **290 e2e** in chunks
(+1) → 35 smoke; the 16 standing screenshots regenerated + byte-
compared (the same-DB discipline; the seedcheck under
`env -u DATABASE_URL`). EXPECTED: the same-day seed + same-day shots
reproduce the committed set byte-for-byte (the v82 same-day-seed
byte-identity law — the committed set was re-shot 2026-10-18 in the
v86 cycle, the v87 seed re-created the same calendar day); any
DATE-class diff pixel-arbitrated per the v66/v75/v80/v86 discipline,
never a full-page VLM verdict; the v86 cycle's RASTERIZATION-NOISE
class (08-calculator) re-classified per pixel if it recurs.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the calculator close button's full chrome census at 1280 (w/h re-affirming v59 + the never-pinned radius/bg/borderTopWidth/display + the docSW guard), riding the read-only EMPTY-state discipline | tests/e2e/calculator.spec.ts |
| 2 | sanity | the pin-sanity mutation (the EXECUTED form): the close button's `rounded-md` → `rounded-md lg:rounded-lg` (calculator-dialog.tsx:138, by LINE NUMBER) → the pin FAILS at exactly the close.radius axis ("6px" → "8px"; the w/h/bg/border/display axes stay green); the full calculator.spec.ts under the mutation: only the v87 pin red; restored → GREEN (the standalone REBUILD as a SEPARATE command; the post-restore full run green) | src/components/budget/calculator-dialog.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 290 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v87 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (289→290 + the v87 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v87 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 122 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.44 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v87 section (the new probes + the close-name-regression lesson + the name-independent-finder lesson) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_210.md + the repo worklog Session 122 entry | docs/session_210.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the pair-arbit-v87.sh census's own
  measured values, byte-identical on both sides' calculator dialogs at
  1280x800: the close `{w: 36, h: 36, radius: "6px", bg:
  "rgba(0, 0, 0, 0)", borderTopWidth: "0px", display: "flex"}`; the
  docSW 1280. The ref-side button-inventory probe (close-arbit-v87.sh)
  independently confirms the same values (the 0px-border computed-color
  the excluded INVISIBLE class).
- The source confirms the values: calculator-dialog.tsx:138 —
  `className="inline-flex h-9 w-9 items-center justify-center
  rounded-md text-[#0a0a0a] transition-colors hover:bg-accent"` (h-9
  w-9 = 36×36; rounded-md = radius 6px; no bg class = transparent; no
  border class = 0px; inline-flex = display flex).
- The pin-sanity target (the executed form): `rounded-md` →
  `rounded-md lg:rounded-lg` flips ONLY the close button's borderRadius
  at ≥1024px (6px → 8px) — grep-verified: no spec asserts the close
  button's radius at any viewport; the w/h axes are class-fixed (h-9
  w-9) and radius-independent; the bg/border/display axes untouched by
  the class change.
- The existing pins are SAFE: the v59 pin's closeBtn {36,36} — the
  mutation preserves w/h (radius never affects dimensions); the v49 640
  pin and the v53 390 pin — below the lg: breakpoint, the variant
  inert; the v81 pin (title/desc/addBtn/scrim) — different elements;
  the v66 pin (row-height family) — the panel body; the v45 F2a pin
  (row census + hover) — the row; the dialog interaction tests — the
  accessible name and the click behavior unchanged.
- The blast radius: ZERO production-code change (the close-name
  observation is the REFERENCE's own regression — the clone's
  aria-label="Close" superset retained; every census delta a documented
  class — the pin-only line holds); the pin-sanity mutation touches
  `src/components/budget/calculator-dialog.tsx:138` (the close button's
  className) REVERTED before ship (`git diff src/` = 0 lines at
  commit).
- The chain gate: lint → typecheck → 108 unit → `npm run build` →
  291+1 e2e chunk executions (**290 unique** after: +1 — the F4 pin)
  → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every
  agent-browser run; the with-server boots fresh per command; the
  reference session EXPIRES between long eval gaps — the login-retry
  loop handles it; the e2e chunks pass FULL file paths;
  `ss -tlnp | grep :3100` + kill before every full-chain run (the
  v53 orphaned-webServer lesson); one-shot Prisma scripts need
  `env -u DATABASE_URL`; no dollar sequences in census JS inside
  double-quoted bash strings (the v64 rule); no attribute-value
  selectors in the census (the v78 rule — geometry + text-content
  filters only); the UNQUOTED heredoc with the env-injected census
  (the v73 lesson); the mutations need the standalone REBUILD as a
  SEPARATE command (the v53 lesson); the clean-check gate re-runs
  AFTER every new file lands (the v69 lesson); the build step is
  `npm run build` (the v76 F0 lesson); the screenshot DATE-class diffs
  after a fresh seed are pixel-arbitrated, never full-page
  VLM-verdicted (the v80 lesson); the sed derivation of the standing
  checks needs the bare-number session-name token family TOO
  (ref80/clone80 — the v84 lesson, applied and diff-verified this
  session); a VLM IDENTICAL verdict still gets the census (the v75
  convention); the census finders must not depend on ACCESSIBLE NAMES
  for reference-side elements (the v87 lesson — the reference's names
  are not stable contracts; geometry + position + text-content finders
  only).
- The deferred queue (all need reference WRITES — out of bounds under
  the v46 read-only rule — plus the login family): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census, the line-items dialog
  glyphs; **the login card's pad family + logo radius pin** (the
  pair-arbit-v87.sh census values recorded in F4 — the pair's fifth
  re-run).
- The v88 queue (suggestions): (1) the re-run cadence rotates to the
  next-oldest candidate after this pair (the v82-era networth +
  drill-down pair [the networth view + the dashboard drill-down
  EXPANDED at 1280], last re-shot v82 — now the oldest remaining
  [v82 < v83 < v84 < v85 < v86 < v87]), (2) the axe-core watch at its
  next re-check point (only a 5.x wrapper changes the calculus), (3)
  the deferred reference-write censuses (unchanged).
