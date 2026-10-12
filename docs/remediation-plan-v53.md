# Remediation Plan v53 — The /networth Tablist's Mobile Pin + the
# Calculator Dialog's Mobile Pin (PIN-ONLY — the second consecutive
# pin-only iteration after the v52 fix)

Date: 2026-10-12 · Scope: the session-124 v53 queue's read-only members
(the /networth view's TABLIST at 390 — the v50 pin walked this family at
640 only, never the mobile reflow; the CALCULATOR DIALOG at 390 — the
v45/v49 pins walked the family at 640 only, the v53 queue's calculator
dialog 390 reflow). Measured live on BOTH sites via the agent-browser
evals (the v53 family: `ref-v53.sh` + `clone-v53.sh` + `clone-v53b.sh`
(the with-row follow-up), READ-ONLY on the reference — no form submits,
no data mutations, no auth state writes; the v46 incident rule).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **245/245 e2e ✓ (5.4m — the second run clean; the first run
had ONE flake in not-found.spec.ts's Go Home test, passing standalone
immediately — the fresh-clone environment's cold-cache timing, not a
production defect)** · 35/35 smoke ✓. The 47th standing checks all
clean (mobile-nav R1–R4 both sites — the clone's mobile menu VERIFIED
WORKING: the R1 burger opens the 5-link sheet via the v52-fixed
text-walk selector, the Income nav closes the sheet AND navigates,
the Escape closes it; the reference's four bugs ALL live — the
toast-blocker (the fixed z-[100] toast viewport eats the burger's
center hit), the sheet-trap (the overlayCount 1 after nav), the
no-landmark, the 464 /networth overflow; the data census read-only and
intact — "1 items · $25,000" networth / "1 items · $5000.00" income;
the SEO pair live on both sites). npm audit = 0 production
vulnerabilities (the same 5 dev-only ESLint-chain advisories, accepted,
unchanged); `.env` recreated from `.env.example` (the fresh clone —
the dev AUTH_SECRET value, never committed). The trap-log scan CLEAN:
only two `-mb-2` utilities live in src/ — both the auth back buttons,
both inside their converted `zb-auth-mode` containers (the v50 + v51
fixes; no un-converted trap site remains).

## The v53 sweep — what the measurement found

- **THE /NETWORTH VIEW'S TABLIST AT 390 (the session-124 queue's
  /networth mobile tablist census): BYTE-PARITY on every chrome axis
  — PIN-ONLY.** Measured live on both sites at 390×844:
  - The list: **h 36 / grid / bg rgb(245,245,245) / radius 8px / pad
    4px / maxW 448px / x 16** — IDENTICAL. The WIDTH family diverges
    BY CONSTRUCTION: the reference's list is **432 wide with tracks
    "211.828px 211.844px"** (its /networth page overflows to 464 —
    the documented reference bug; the content column stretches to 432,
    the list overhangs the 390 viewport at x 16 + 432 = 448) where
    the clone's superset fix keeps the page in-bounds (**pageSW 390**)
    and the list renders **358 wide with tracks "175px 175px"** —
    the SAME documented-divergence class as the v47 net-worth card
    mobile census ("the reference's own card 432 wide inside its
    464-overflow page, its documented bug"). Every non-width axis is
    byte-identical.
  - The ACTIVE trigger (Assets): **175×28 (the reference 212×28 — the
    width class above) / radius 6px / 14px/500 / rgb(20,83,45) on
    rgb(220,252,231) / pad 4px 12px / the data-[state=active]:shadow
    emission (the shadow-sm VISIBLE pair, the accepted lead-divergence
    class)** — IDENTICAL. The icon: **16×16 at currentColor
    rgb(20,83,45) / mr 8px** — IDENTICAL.
  - The INACTIVE trigger (Liabilities): **175×28 / radius 6 / 14px/500
    / rgb(115,115,115) / transparent / shadow none / pad 4px 12px /
    the icon 16×16 at rgb(115,115,115) / mr 8px** — IDENTICAL.
- **THE CALCULATOR DIALOG AT 390 (the session-124 queue's calculator
  dialog 390 reflow): BYTE-PARITY on every measurable axis — PIN-ONLY.**
  Measured live on both sites at 390×844 (the reference's Rent
  calculator opened read-only via the Calculate click; the clone's via
  the same click + the v45 F2b add-then-cleanup flow for the row
  family — the reference's own data carries 1 row; the clone's dev
  seed carries none, the e2e seed's flow creates its own):
  - The panel: **w 358 @ x 16 (the 390 − 2×16 overlay-pad arithmetic)
    / radius 16px / maxW 768px / maxH 717.4px (the 85vh cap) / bg
    white / overflow hidden / display flex** — IDENTICAL. The shadow:
    the 2xl VISIBLE layer `rgba(0,0,0,0.25) 0px 25px 50px -12px` (the
    reference's 2 transparent leads + the layer = 3; the clone's 4
    leads + the layer = 5 — the accepted lead-divergence class,
    v10/v25/v45/v48) — IDENTICAL. The panel h measured **413 on BOTH
    sites with 1 row** (the centering invariant holds on both: y =
    round((844 − h) / 2); the h itself is data-dependent — never
    pinned).
  - The header: **h 101 / pad 16px 24px / border-b 1px solid
    rgb(229,231,227)** — IDENTICAL (the flex row at 390 SQUISHES the
    chip to 32×40 and the close to 29×36 on BOTH sites — the identical
    flex-shrink behavior, byte-pinned).
  - The chip: **32×40 / radius 12px / the orange gradient
    `linear-gradient(135deg, rgb(224,122,59), rgb(245,169,98))`** —
    IDENTICAL. The close: **29×36** — IDENTICAL.
  - The h2: **18/700/rgb(26,58,46) "Rent Calculator"**; the desc:
    **14px/rgb(107,114,128)** — IDENTICAL.
  - The total card: **w 310 (the 358 − 2×24 p-6 arithmetic) / bg
    rgb(255,247,245) / radius 12px / pad 16px** — IDENTICAL.
  - The line-item row (the with-row state): **w 310 / pad 16px / bg
    white / border-t 1px solid rgb(229,231,227) / radius 12px** —
    IDENTICAL.
  - The Add Item button: **110×32 / fs 12px / fw 500 / the orange
    gradient / white text** — IDENTICAL.
  - docSW 390 on both sites (the calculator overlay constrains the
    page).
  - The clone's EMPTY state (the "Add First Item" outline button, the
    48px icon at opacity 0.2, the "No line items yet" block) is the
    clone's own surface — the reference's empty state is UNMEASURABLE
    (emptying its calculator needs WRITES — the deferred class, same
    as the verify/forgot-confirm censuses).
- **NO PRODUCTION GAP FOUND** — the fifth-iteration sweep family
  (v48 PIN-ONLY → v49 fix → v50 fix → v51 fix → v52 fix → v53
  PIN-ONLY): both v53 surfaces are already at byte-parity; the
  deliverable is the pin pair + the probe scripts + the docs.

## Findings

### F1. [PIN] the /networth view's tablist at 390

One e2e test (`tests/e2e/networth.spec.ts`, a new
`test.describe("net worth tablist mobile census (v53 — plan F1)")`,
390×844 viewport): the list (w 358 / h 36 / x 16 / display grid /
gridCols "175px 175px" / bg rgb(245,245,245) / radius 8px / pad 4px /
maxW 448px); the ACTIVE trigger (w 175 / h 28 / radius 6px / fs 14px /
fw 500 / color rgb(20,83,45) / bg rgb(220,252,231) / pad "4px 12px" +
the shadow-sm VISIBLE pair via toContain); its icon (w 16 / h 16 /
color rgb(20,83,45)); the INACTIVE trigger (w 175 / h 28 / radius 6px
/ fs 14px / fw 500 / color rgb(115,115,115) / bg transparent / shadow
"none"); its icon (w 16 / h 16 / color rgb(115,115,115)); docSW 390
(the superset invariant — the reference reads 464, its own documented
overflow bug).

### F2. [PIN] the calculator dialog at 390

One e2e test (`tests/e2e/calculator.spec.ts`, a new
`test.describe("calculator dialog mobile census (v53 — plan F2)")`,
390×844 viewport, the v45 F2b add-then-cleanup flow): hover the Rent
card → the Calculate click → Add Item → fill "Contents Insurance" /
25 → Save Item → the census: the panel (w 358 / x 16 / radius 16px /
maxW 768px / maxH 717.4px / bg white / overflow hidden / display flex
+ the 2xl VISIBLE layer via toContain + the centering invariant
y === round((844 − h) / 2)); the header (h 101 / pad "16px 24px" /
border-b 1px solid rgb(229,231,227)); the chip (w 32 / h 40 / radius
12px / the orange gradient); the close (w 29 / h 36); the h2 (fs 18px
/ fw 700 / rgb(26,58,46)); the total card (w 310 / bg rgb(255,247,245)
/ radius 12px / pad 16px); the row (w 310 / pad 16px / bg white /
border-t + radius 12px); the Add Item button (w 110 / h 32 / fs 12px /
fw 500 / the gradient / white); docSW 390. Cleanup: delete the row →
confirm → close.

### S1. [MUTATION-SANITY] the pins bite

(a) the TabsList's `grid-cols-2` → `grid-cols-1` → the F1 pin fails
(the tracks "175px 175px" → "350px");
(b) the trigger's `data-[state=active]:bg-[#dcfce7]` removed → the F1
pin fails (the active bg transparent);
(c) the calculator header's `py-4` → `py-2` → the F2 pin fails (the
header 101 → 69);
(d) the calculator panel's `maxWidth: "48rem"` → `"40rem"` → the F2
pin fails (the maxW 768 → 640);
(e) the total card's `p-4` → `p-2` → the F2 pin fails (the pad 16 →
8).
All restored → GREEN. **Each mutation needs the standalone REBUILD
before the run bites** (the v47–v52 execution lesson — the e2e suite
runs against the BUILD, not the source tree). **The v53 addition: the
rebuild and the test run must be SEPARATE commands** — the combined
`npm run build … && npx playwright test …` one-liner RACED the
.next/standalone swap twice this session (the mutation-(a) and the
mutation-(b) runs both read "1 passed" against a not-yet-swapped
build; the clean separate re-runs both bit). The verification idiom:
build in one command (check the exit code), then run the test in the
next — and when a mutation unexpectedly does NOT bite, probe the
SERVED build directly (the live-computed-style check on :3199) before
doubting the pin.

### P1. [PROBE-INFRA] the v53 probe family persisted

`scripts/parity-probes/ref-v53.sh` + `clone-v53.sh` + `clone-v53b.sh`
(the with-row follow-up) + the probe README's v53 section. The
clone-v53b lesson: the eval string's closing `()` — an un-invoked
async function expression submits NOTHING (the login silently no-ops;
the "no card" cascade) — always grep the driver for `})()"` before
running.

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v53 paragraph. D2: CLAUDE.md — the v53 entry +
the counts. D3: README — the v53 row + the counts. D4: the SKILL doc
— the Session 88 row, the count sites, the state line. D5: the PAD —
a v1.1.10 revision block. D6: the probe README — the v53 section (the
drivers + the lessons). D7: session_125.md (the formal log) +
session_126.md (the raw transcript) + the repo worklog Session 87 +
the ledger list. D8: the workspace worklog
(/home/z/my-project/worklog.md).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1 written (pin-only — GREEN immediately against the unchanged build, the TDD pin discipline: the pin proves the parity, the mutations prove the pin) | test | `tests/e2e/networth.spec.ts` |
| 2 | F2 written (pin-only — the calculator at 390 with the add-then-cleanup flow) | test | `tests/e2e/calculator.spec.ts` |
| 3 | The probe scripts persisted + the probe README's v53 section | docs | `scripts/parity-probes/` |
| 4 | S1(a)–(e): the five pin-sanity mutations, each verified to FAIL then restored (each preceded by `npm run build`) | verify | `src/components/ui/tabs.tsx` + `calculator-dialog.tsx` |
| 5 | The full chain re-run (108 unit · **247** e2e · 35 smoke + lint + typecheck + build) — all green; the standing VLM pair on a fresh surface (the calculator dialog at 390 — THE F2 SURFACE) | verify | — |
| 6 | The 16 screenshots regenerated (the capture script) | docs | `docs/screenshots/` |
| 7 | D1–D8 + the formal session log (session_125.md) + the raw transcript (session_126.md) + the repo worklog Session 87 + the SKILL doc Session 88 row | docs | repo root + `docs/` |
| 8 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/net-worth-view.tsx:399` — the TabsList
  (`grid w-full max-w-md grid-cols-2`); `:403-410` — the triggers with
  the `mr-2 h-4 w-4` icons. `src/components/ui/tabs.tsx` — the list
  base (`inline-flex h-9 ... rounded-lg bg-muted p-1` — h 36 / radius
  8 / #f5f5f5 / pad 4) + the trigger base (`rounded-md px-3 py-1
  text-sm font-medium ... data-[state=active]:bg-[#dcfce7]
  data-[state=active]:text-[#14532d]` — radius 6 / pad 4 12 / 14/500
  / the green pair). The clone's tablist carries role=tablist/tab (the
  superset a11y) — the census walks the roles. The list's grid tracks
  at 390: (358 − 8 pad) / 2 = 175 each — the exact "175px 175px"
  reading. NO change needed — the pin proves the parity.
- `src/components/budget/calculator-dialog.tsx:100-109` — the panel
  style (maxWidth 48rem / maxHeight 85vh / overflow hidden / flex
  column); `:112-115` — the header (`flex items-center justify-between
  border-b px-6 py-4` — pad 16 24); `:147-151` — the total card
  (`mb-6 rounded-xl p-4` + backgroundColor #fff7f5); `:178-183` — the
  Add Item button (`zb-btn-add zb-btn-add-sm` + the gradient); the row
  family (`group rounded-xl border bg-white p-4`). The overlay's 16px
  pad (the `fixed inset-0` family) yields the 358 = 390 − 32 panel
  arithmetic — pinned by the v49 640 test's 608 = 640 − 32, the same
  family. NO change needed.
- The e2e contract: the networth + calculator specs run AUTHENTICATED
  via the setup project's storageState (the deterministic e2e seed;
  the global-setup re-seeds db/e2e.db fresh every run). The Rent item
  + the v45 F2b add-flow are seed-stable. The tablist renders
  regardless of the assets/liabilities data. The F2 flow's
  "Contents Insurance" / 25 row + the delete-cleanup mirror the v45
  F2b test exactly (its cleanup deletes the row — the e2e db stays
  pristine).
- The existing pins are SAFE: the v50 tablist pin at 640 (the list
  448 / the triggers 220) runs at its own viewport — unaffected; the
  v14 G2 icon pin (1280) — unaffected; the v45 F2b row pin at 640 —
  unaffected (its own viewport); the v49 calculator chrome pin at 640
  — unaffected. The new tests add no production change, so no
  existing pin can break.
- The chain gate: lint → typecheck → 108 unit → build → 245 e2e
  (**247** after: +2 — F1, F2) → 35 smoke.
- Execution notes: `pkill -f agent-browser` + a stale-session-file
  sweep before every agent-browser run (the v50/v51 lesson — a killed
  run leaves the .engine pair that HANGS the next open; re-observed
  this session: the dbg53 hang → the cleanup → the clean re-run);
  a rebuild swaps .next/standalone UNDER a running parity server —
  reboot the :3200 server after every build (with-server.sh boots
  fresh per command); the reference session EXPIRES between long eval
  gaps — re-login via the same eval before any follow-up census; the
  eval-string closing `()` discipline (the P1 lesson above).
- The VLM pair: the calculator dialog at 390 (THE F2 SURFACE — a
  data-divergent surface: the reference's own Rent rows vs the
  clone's Contents Insurance row; the expected flags: the seed-data
  classes + the reference's own Base44 FAB, the v47/v48/v52
  precedents).
- DEFERRED queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census (a registration), the reference-side
  forgot-confirm state census (a reset-link submit), and the
  reference-side calculator EMPTY-state census (a line-item delete).
