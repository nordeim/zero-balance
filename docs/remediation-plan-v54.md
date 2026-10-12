# Remediation Plan v54 — The Savings Goal-Card's Badge-Row + Footer
# Internals at 390 (PIN-ONLY — the third consecutive pin-only iteration
# after the v52 fix)

Date: 2026-10-12 · Scope: the session-125 v54 queue's first read-only
member (the SAVINGS VIEW's GOAL-CARD INTERNALS at 390 — the badge chip
row + the date/payment footer — the internals BEYOND the v51 F3 chrome
pin; the v51 pin walked the card's outer chrome + the h4/sub/amount
typography, never the badge-row or footer internals). Measured live on
BOTH sites via the agent-browser evals (the v54 family:
`ref-v54.sh` + `clone-v54.sh`, READ-ONLY on the reference — no form
submits, no data mutations, no auth state writes; the v46 incident
rule).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **248 e2e ✓ (the 247 chromium count: 140 + 108, two ordered
chunks, both exit 0, zero failures — the 10-minute Bash-timeout
discipline; the fresh-clone environment needed
`npx playwright install chromium` first — the headless-shell-1243
binary was absent, the first a11y run failed 21-wide on
browserType.launch, the install fixed it)** · 35/35 smoke ✓. The 48th
standing checks all clean (mobile-nav R1–R4 both sites — the clone's
mobile menu VERIFIED WORKING: the R1 burger hit-test true + the
5-link sheet opens, the Income nav closes the sheet AND navigates;
the reference's four bugs ALL live — the toast-blocker [the burger's
center hit eaten by the fixed z-[100] toast viewport], the
sheet-trap [overlayCount 1 after nav], the no-landmark
[navLandmark false], the 464 /networth overflow [docSW 464 > vw
390]; the data census read-only and intact — "1 items · $25,000"
networth / "1 items · $5000.00" income; the SEO pair live on both
sites). npm audit = 0 production vulnerabilities. `.env` recreated
from `.env.example` (the fresh clone — the dev AUTH_SECRET value,
never committed). The trap-log scan CLEAN: only two `-mb-2`
utilities live in src/ — both the auth back buttons, both inside
their converted `zb-auth-mode` containers (the v50 + v51 fixes;
src/components/budget/login-card.tsx:617 + :714).

## The v54 sweep — what the measurement found

- **THE SAVINGS GOAL-CARD'S INTERNALS AT 390 (the session-125 queue's
  goal-card-internals census): BYTE-PARITY on every chrome axis —
  PIN-ONLY.** Measured live on both sites at 390×844 (the reference's
  own Emergency Fund goal — classification need, $1000.00, monthly,
  active, no payment method; the clone's dev seed's Emergency Fund —
  classification savings, $800, monthly, Recurring, Bank Account
  payment... the Investments card is the clone's SECOND goal; the
  census walks the FIRST card's h4 on both sites):
  - The header row (the dot + h4 line): **flex / gap 8px / mb 4px /
    items-center** — IDENTICAL. The dot: **8×8 / radius 9999px /
    bg rgb(59, 126, 161)** (the savings TYPE_COLORS.blueMedium accent
    on BOTH sites — the reference colors its dot by TYPE, not by
    classification; its need-classified goal still carries the teal
    savings dot) — IDENTICAL.
  - The h4: **16px / 600 / rgb(26, 58, 46)** — IDENTICAL (the v51 pin
    already walked this axis; re-measured byte-identical).
  - The amount: **24px / 700 / mb 0px** (the wrapper carries the
    mb-4) — IDENTICAL (the color axis is the v51 pin's
    rgb(59, 126, 161)).
  - The BADGE ROW: **display flex / gap 8px / flex-wrap wrap /
    mb 12px** — IDENTICAL. The row HEIGHT and chip COUNT are DATA
    classes (the reference's 3 chips fit one 22px row; the clone's
    richer seed's 4 chips wrap to 52px — the v51 F3 pin's documented
    class; never pinned).
  - The CHIP CHROME (every chip, both sites): **h 22 / radius 6px /
    pad 2px 10px (py-0.5 + px-2.5) / fs 12px / fw 600** — IDENTICAL.
    The chip COLORS per class are the badge-colors.spec.ts pins
    (v8 G2 — need red / monthly purple / active slate / savings +
    Recurring green, all plain rgb, byte-identical) — re-measured
    byte-identical this sweep. The chip ICONS: **12×12 / mr 4px**
    at the chip's own color — IDENTICAL (the classification chip
    and the Recurring chip carry icons; the frequency + status
    chips carry none on BOTH sites). The width PROOF: the
    "monthly" chip measures **78×22 on BOTH sites** (the same text
    at the same chrome renders the same width — the strongest
    byte-parity signal in the census); the "active" chip
    **63×22 on BOTH**.
  - The FOOTER ROW: **flex / items-center / justify-between /
    fs 12px / color rgb(107, 114, 128) / h 16** — IDENTICAL. The
    date span: **flex / gap 4px / fs 12px / rgb(107, 114, 128) /
    the calendar svg 12×12 at rgb(107, 114, 128)** — IDENTICAL. The
    payment span: the clone's own surface (the reference's goal
    carries NO payment method — its footer renders the date span
    alone; the clone's seed carries "Bank Account"/"Brokerage" and
    renders the mirrored credit-card span: **flex / gap 4px / fs
    12px / rgb(107, 114, 128) / the svg 12×12** — the same chrome,
    the DATA class is the seed's own payment values).
  - docSW 390 on both sites (the savings page fits the mobile
    viewport on both).
- **NO PRODUCTION GAP FOUND** — the sixth-iteration sweep family
  (v48 PIN-ONLY → v49 fix → v50 fix → v51 fix → v52 fix → v53
  PIN-ONLY → v54 PIN-ONLY): the v54 surface is already at
  byte-parity; the deliverable is the pin + the probe scripts + the
  docs.

## Findings

### F1. [PIN] the savings goal-card's badge-row + footer internals at 390

One e2e test (`tests/e2e/items.spec.ts`, a new
`test.describe("savings goal-card internals census at 390 (v54 — plan F1)")`,
390×844 viewport, the same /savings walk as the v51 F3 pin): the
header row (flex / gap 8 / mb 4 / items-center); the dot (8×8 /
radius 9999px / bg rgb(59, 126, 161)); the badge row (display flex /
gap 8px / wrap / mb 12px); the FIRST chip's chrome (h 22 / radius
6px / pad "2px 10px" / fs 12px / fw 600 / the 12×12 icon at the
chip's color with mr 4px); the MONTHLY chip (w 78 — the byte-parity
width proof / h 22 / no icon); the ACTIVE chip (w 63 / h 22 / no
icon); the footer row (display flex / justify space-between / fs
12px / color rgb(107, 114, 128) / h 16); the date span (display
flex / gap 4px / fs 12px / rgb(107, 114, 128) / the 12×12 calendar
icon at rgb(107, 114, 128)); docSW 390.

### F2. [VLM-PAIR] the standing VLM pair on the /networth tablist + the v54 F1 surface

The session-125 v54 queue's own suggestion — a fresh VLM pair on the
/networth tablist (the v53 F1 surface) as the next standing check
plus the v54 F1 surface (the savings goal card). The expected flags
per the v43 misattribution rule: the seed-data classes (the
reference's need-classified goal vs the clone's savings
classification; the 4th Recurring chip; the payment-method span)
and the reference's own platform chrome (the Base44 FAB) — each
flag DOM-verified before it is accepted.

### S1. [MUTATION-SANITY] the pins bite

(a) the badge row's `gap-2` → `gap-4` → the F1 pin fails (the row
gap 8 → 16);
(b) the classification chip's `px-2.5` → `px-1.5` → the F1 pin
fails (the chip pad "2px 10px" → "2px 6px");
(c) the chip's `text-xs` → `text-sm` → the F1 pin fails (the chip
fs 12 → 14);
(d) the footer's `text-xs` → `text-sm` → the F1 pin fails (the
footer fs 12 → 14);
(e) the date span's `gap-1` → `gap-2` → the F1 pin fails (the date
span gap 4 → 8).
All restored → GREEN. **Each mutation needs the standalone REBUILD
before the run bites — and the rebuild and the test run as
SEPARATE commands** (the v47–v53 execution lesson — the e2e suite
runs against the BUILD, not the source tree; the combined one-liner
races the .next/standalone swap).

### P1. [PROBE-INFRA] the v54 probe family persisted

`scripts/parity-probes/ref-v54.sh` + `clone-v54.sh` + the probe
README's v54 section. The v54 probe lesson: **a generic
justify-between + svg footer finder matches the card's HEADER row
first** (the header also carries justify-between and its own
kebab/trailing svg) — the footer locator must be "the LAST
justify-between direct child WITHOUT an h4"; the first census run
read the header's 16px/48px geometry as the "footer" and an empty
kebab as the "payment span" (the fs-16/h-48 signature is the
tell-tale of the wrong row).

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v54 paragraph. D2: CLAUDE.md — the v54 entry +
the counts. D3: README — the v54 row + the counts. D4: the SKILL
doc — the Session 89 row, the count sites, the state line. D5: the
PAD — a v1.1.11 revision block. D6: the probe README — the v54
section (the drivers + the footer-locator lesson). D7: session_128.md
(the formal log) + session_129.md (the raw transcript) + the repo
worklog Session 88 + the ledger list. D8: the workspace worklog
(/home/z/my-project/worklog.md).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1 written (pin-only — GREEN immediately against the unchanged build, the TDD pin discipline: the pin proves the parity, the mutations prove the pin) | test | `tests/e2e/items.spec.ts` |
| 2 | The probe scripts persisted + the probe README's v54 section | docs | `scripts/parity-probes/` |
| 3 | S1(a)–(e): the five pin-sanity mutations, each verified to FAIL then restored (each preceded by `npm run build`, run as a SEPARATE command) | verify | `src/components/budget/item-card.tsx` |
| 4 | F2: the VLM pair on the /networth tablist (390, both sites) + the savings goal card (the F1 surface) — every flag DOM-verified | verify | — |
| 5 | The full chain re-run (108 unit · **248** e2e · 35 smoke + lint + typecheck + build) — all green, two ordered chunks | verify | — |
| 6 | The 16 screenshots regenerated (the capture script) | docs | `docs/screenshots/` |
| 7 | D1–D8 + the formal session log (session_128.md) + the raw transcript (session_129.md) + the repo worklog Session 88 + the SKILL doc Session 89 row | docs | repo root + `docs/` |
| 8 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/item-card.tsx:118` — the header row
  (`mb-1 flex items-center gap-2` — gap 8 / mb 4 / center);
  `:119` — the dot (`h-2 w-2 rounded-[9999px]` at the TYPE_COLORS
  accent — 8×8 / 9999 / rgb(59,126,161) for savings);
  `:152-156` — the amount block (the `text-2xl font-bold` p inside
  the `mb-4` wrapper — 24/700/mb 0);
  `:158` — the badge row (`mb-3 flex flex-wrap gap-2` — flex / wrap
  / gap 8 / mb 12);
  `:159-184` — the chips (`inline-flex items-center rounded-md
  border px-2.5 py-0.5 text-xs font-semibold` + the per-class
  colors — h 22 / radius 6 / pad "2px 10px" / 12/600; the
  classification + Recurring chips carry `h-3 w-3` icons with
  `mr-1` — 12×12 / mr 4; the frequency + status chips carry none);
  `:187-198` — the footer (`flex items-center justify-between
  text-xs` + the inline `color: rgb.gray` — 12 / rgb(107,114,128) /
  h 16) with the date span `flex items-center gap-1` (gap 4) + the
  calendar `h-3 w-3` svg and the mirrored payment span. NO change
  needed — the pin proves the parity.
- The e2e contract: the spec runs AUTHENTICATED via the setup
  project's storageState (the deterministic e2e seed; the
  global-setup re-seeds db/e2e.db fresh every run). The savings
  view renders the seed's Emergency Fund + Investments cards (the
  v51 F3 pin's "2 items · $1250.00" wait is the established settle
  pattern). The F1 census walks the FIRST h4-bearing card — the
  same finder as the v51 F3 pin (the rounded-xl walk up to the grid
  child).
- The existing pins are SAFE: the v51 F3 chrome pin runs at its own
  describe (the card's outer chrome — unaffected); the v8 G2 badge
  colors pin (desktop, colors only — unaffected); the v45 F1 card
  grid census at 1280 (unaffected); the v52 F2/F3 view censuses
  (unaffected — their own describes). The new test adds no
  production change, so no existing pin can break.
- The chip-color map (`src/lib/constants.ts` — CLASSIFICATION_BADGES
  / FREQUENCY_BADGES): the need chip's red family, the monthly
  chip's purple family, the active chip's slate family — the exact
  families the badge-colors.spec.ts pins assert (v8 G2); the sweep
  re-measured them byte-identical on both sites.
- The chain gate: lint → typecheck → 108 unit → build → 247 e2e
  (**248** after: +1 — F1) → 35 smoke.
- Execution notes: `pkill -f agent-browser` + a stale-session-file
  sweep before every agent-browser run (the v50/v51 lesson); a
  rebuild swaps .next/standalone UNDER a running parity server —
  reboot the :3200 server after every build (with-server.sh boots
  fresh per command); the reference session EXPIRES between long
  eval gaps — re-login via the same eval before any follow-up
  census; the fresh-clone environment needs
  `npx playwright install chromium` (the headless-shell binary is
  per-Playwright-version — 1243 this session).
- DEFERRED queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census (a registration), the reference-side
  forgot-confirm state census (a reset-link submit), and the
  reference-side calculator EMPTY-state census (a line-item
  delete). The reference-side goal-card need-classification /
  no-payment / non-recurring footer census is MEASURED this
  iteration (read-only — the goal card renders as-is); only its
  EMPTY-state family stays deferred.
