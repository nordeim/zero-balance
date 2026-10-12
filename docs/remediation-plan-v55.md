# Remediation Plan v55 — The Icon-Glyph Swap: the piggy-bank / mail /
# search / trending-up glyphs (THE FIX — the fifth production-code
# change since v46, breaking the v53/v54 pin-only streak)

Date: 2026-10-13 · Scope: the session-128 v55 queue's read-only member
(the goal-card's classification-icon glyph census — the v44 glyph-swap
family's badge-row application) which, extended to a FULL icon-glyph
audit across the five views + the login page, found **FOUR drifted
glyphs**. Measured live on BOTH sites via the v55 family
(`ref-v55.sh` + `clone-v55.sh`, the goal-card glyph census;
`glyph-audit-v55.sh`, the full per-view lucide glyph dictionary;
`glyph-exact-v55.sh`, the exact-svg-markup capture; `glyph-diff-v55.mjs`,
the dictionary diff — all READ-ONLY on the reference, the v46 rule).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **248 e2e ✓ (116 + 133, two ordered chunks, both exit 0, zero
failures — the 10-minute Bash-timeout discipline; the fresh-clone
environment needed `npx playwright install chromium` first, the
headless-shell-1243 binary)** · 35/35 smoke ✓. The 49th standing checks
all clean (mobile-nav R1–R4 both sides — the reference's four bugs ALL
live [toast-blocker, sheet-trap, no-landmark, the 464 /networth
overflow], the clone's mobile menu VERIFIED WORKING, the data census
intact, the SEO pair live on both sites). The trap-log scan CLEAN (both
`-mb-2` back buttons inside their converted `zb-auth-mode` containers).
The v54 diff verified PIN-ONLY (16 files: docs/probes/one spec, zero
src/ changes).

## The v55 sweep — what the measurement found

- **THE FULL GLYPH AUDIT (24 lucide glyphs across the five views + the
  login page): 19 byte-identical, 4 DRIFTED, 1 one-side-only.** The
  identical set includes every glyph the audit could see on both sites:
  target, layout-dashboard, wallet, receipt, panel-left, plus,
  chevron-down, chevron-right, circle-alert, heart, lock, calendar,
  credit-card, ellipsis-vertical, pen, calculator, building2,
  circle-arrow-down, circle-arrow-up — the lucide versions render the
  same path data for these. The one-side-only glyph is `repeat` (the
  clone's Recurring badge — the documented superset data class; the
  reference's seed carries no recurring items, so no reference glyph
  exists to match).
- **THE FOUR DRIFTED GLYPHS (the v44 chevron-swap class — lucide
  redesigned these shapes between the reference's lucide version and
  lucide-react 0.525):**
  1. **piggy-bank** — the reference renders the OLD 3-path glyph
     (`M19 5c-1.5 0-2.8 1.4-3 2-3.5-1.5-11-.3-11 5 0 1.8 0 3 2
     4.5V20h4v-2h3v2h4v-4c1-.5 1.7-1 2-2h2v-4h-2c0-1-.5-1.5-1-2V5z` +
     `M2 9v1c0 1.1.9 2 2 2h1` + `M16 11h.01`); the clone renders the
     redesigned body-curve glyph. Rendered on BOTH sites at: the nav
     rail's Savings link (16×16), the dashboard's Total-Savings stat row
     (24×24 in the 48px tile), the donut legend's Savings row (16×16),
     the quick-actions' Add Savings (16×16 in the 32px tile), the
     savings view's hero (24×24), the classification chips (12×12, mr
     4) — measured via `piggy-sweep-v55.sh` (the reference's EVERY
     piggy svg carries the old glyph, all six surfaces).
  2. **trending-up** — the reference renders the OLD two-POLYLINE glyph
     (`points="22 7 13.5 15.5 8.5 10.5 2 17"` +
     `points="16 7 22 7 22 13"`); the clone renders the redesigned
     two-path glyph. Sites: the dashboard's Total-Income stat row +
     the breakdown card's net row + the networth hero/summary trend
     icons + the nav rail's Net Worth link.
  3. **search** — the reference renders `m21 21-4.3-4.3` (the old
     handle); the clone renders `m21 21-4.34-4.34` (the redesign
     nudged the handle's length). Sites: the items-view search input
     (20×20, gray).
  4. **mail** — the reference renders the OLD envelope flap
     (`m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7` with the rect's
     rx 2); the clone renders the re-tuned `m22 7-8.991 5.727a2 2 0
     0 1-2.009 0L2 7`. Site: the login page's email input icon
     (16×16, slate-500).
- **The already-parity glyphs the sweep PIN-LOCKED (the strongest
  same-glyph evidence):** the goal card's date-span CALENDAR glyph
  (3 paths `M8 2v4`/`M16 2v4`/`M3 10h18` + the rect 3,4,18×18 rx 2 —
  byte-identical on both sites at 12×12, mr 0, rgb(107,114,128)); the
  classification glyph trio measured on the /expenses control census —
  the reference's Investments (savings) vs the clone's savings chips
  share the piggy family (the DRIFT above), the reference's Netflix
  (want) vs the clone's Entertainment (want) HEART glyphs
  byte-identical (`M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5
  3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0
  2.3 1.5 4.05 3 5.5l7 7Z`), the need CIRCLE-ALERT glyphs
  byte-identical (circle 12,12 r10 + line 12,8→12,12 + line
  12,16→12.01,16 — the reference's Miscellaneous/Rent vs the clone's
  Groceries/Rent). The icon CHROME identical everywhere: viewBox
  `0 0 24 24`, fill none, stroke currentColor, stroke-width 2,
  stroke-linecap round, stroke-linejoin round, the chip icons 12×12 at
  mr 4 colored by the chip's own color.
- **NO other production gap found** — the glyph drift IS the v55
  production gap (the first since the v52 fix).

## Findings

### F1. [FIX + PIN] the legacy-icon swap module + the glyph-parity e2e spec

One new module `src/components/ui/legacy-icons.tsx` exporting four
components — `PiggyBankIcon`, `TrendingUpIcon`, `SearchIcon`,
`MailIcon` — each rendering the reference's EXACT svg: the base attrs
(`xmlns`, `width 24`, `height 24`, `viewBox 0 0 24 24`, `fill none`,
`stroke currentColor`, `stroke-width 2`, `stroke-linecap round`,
`stroke-linejoin round`), the class prefix `lucide lucide-<name>`
merged with the caller's className (the existing e2e pins select
`svg.lucide-piggy-bank` — the class is part of the reference's DOM),
and the exact shape children (paths/polyline/rect/circle with the
byte-identical `d`/`points`/attrs measured live). The eight usage
files swap their lucide imports for the module: item-card.tsx,
items-view.tsx, dashboard-view.tsx, item-details-dialog.tsx,
budget-item-dialog.tsx, sidebar.tsx, net-worth-view.tsx,
login-card.tsx.

One new e2e spec `tests/e2e/glyph-parity.spec.ts` (TDD RED first — the
current lucide glyphs FAIL the shape assertions, then GREEN post-swap):
(1) the /savings goal-card census at 390 — the classification chip's
icon (3 paths, the exact d strings, 12×12, mr 4, the chip color), the
date-span calendar glyph (3 paths + the rect, 12×12), the Recurring
chip's repeat glyph (4 paths, the clone-only superset pin), docSW 390;
(2) the dashboard stat-row census — the Total-Savings piggy glyph +
the Total-Income trending glyph (2 polylines, the exact points) +
the Total-Expenses receipt glyph (already parity, pin-locked);
(3) the items-view search-input glyph (circle + the old handle path);
(4) the login-page mail glyph (logged-out, the empty storageState
pattern) + the lock glyph (parity, pin-locked). The heart + circle-alert
glyphs pin via the /expenses classification chips (the same-glyph
control census).

### F2. [VLM-PAIR] the standing VLM pair on the calculator dialog's with-row state + the swapped goal card

The session-128 v55 queue's own suggestion — a fresh VLM pair on the
calculator dialog's with-row state (the v53 F2 surface) as the next
standing check, plus the v55 F1 surface (the savings goal card
post-swap). The expected flags per the v43 misattribution rule: the
seed-data classes and the reference's own platform chrome (the Base44
FAB) — each flag DOM-verified before it is accepted.

### S1. [MUTATION-SANITY] the pins bite

(a) the piggy-bank's body path `M19 5c...` → `M19 6c...` → the F1 pin
fails (the d census mismatches);
(b) the trending-up's polyline points `22 7 13.5 15.5...` → `22 8
13.5 16.5...` → the F1 pin fails;
(c) the search handle `-4.3-4.3` → `-4.34-4.34` (the lucide redesign
value) → the F1 pin fails;
(d) the mail flap `a1.94 1.94` → `a2 2` (the redesign value) → the F1
pin fails;
(e) reverting ONE usage site (the item-card) to the lucide import →
the F1 chip-census pin fails (the new glyph renders).
All restored → GREEN. Each mutation needs the standalone REBUILD as a
SEPARATE command (the v47–v54 execution lesson).

### P1. [PROBE-INFRA] the v55 probe family persisted

`ref-v55.sh` + `clone-v55.sh` (the goal-card glyph census + the
/expenses same-glyph control), `piggy-sweep-v55.sh` (the reference's
every-piggy scope sweep), `glyph-audit-v55.sh` (the full per-view lucide
dictionary — with the login retry + auth check), `glyph-exact-v55.sh`
(the exact-svg capture), `glyph-diff-v55.mjs` (the dictionary diff),
plus the probe README's v55 section. The v55 probe lessons: (1) a
path-only glyph census reads ZERO paths on circle-alert — the glyphs
render `<circle>`/`<rect>`/`<polyline>` children; the shape dump must
walk every shape tag (and read `points`, not x1/y1, for polylines);
(2) the glyph audit's login can RACE the page mount — "no inputs" is
the RETRY signal (a fresh profile's /login can still be mounting at
3s), and the auth state needs an explicit post-login check before the
census loop (the first sweep censused the LOGIN PAGE six times);
(3) agent-browser eval output is a JSON-encoded string — unwrap it
(twice if doubly-encoded) before parsing dictionaries.

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v55 paragraph. D2: CLAUDE.md — the v55 entry + the
counts. D3: README — the v55 row + the counts. D4: the SKILL doc —
the Session 90 row, the count sites, the state line. D5: the PAD — a
v1.1.12 revision block. D6: the probe README — the v55 section (the
six probes + the three lessons). D7: session_131.md (the formal log) +
session_132.md (the raw transcript) + the repo worklog Session 89 +
the ledger list. D8: the workspace worklog (/home/z/my-project/worklog.md).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1's e2e spec written FIRST (TDD RED — the four glyph-shape assertions fail against the current lucide glyphs) | test | `tests/e2e/glyph-parity.spec.ts` |
| 2 | F1's fix: the legacy-icons module + the eight import swaps → GREEN | code | `src/components/ui/legacy-icons.tsx` + the eight files |
| 3 | S1(a)–(e): the five pin-sanity mutations, each verified to FAIL then restored (each preceded by `npm run build`, run as a SEPARATE command) | verify | `src/components/ui/legacy-icons.tsx` |
| 4 | The probe scripts persisted + the probe README's v55 section | docs | `scripts/parity-probes/` |
| 5 | F2: the VLM pair on the calculator dialog's with-row state (640, both sites) + the swapped goal card — every flag DOM-verified | verify | — |
| 6 | The full chain re-run (108 unit · **254** e2e · 35 smoke + lint + typecheck + build) — all green, two ordered chunks | verify | — |
| 7 | The 16 screenshots regenerated (the capture script) | docs | `docs/screenshots/` |
| 8 | D1–D8 + the formal session log (session_131.md) + the raw transcript (session_132.md) + the repo worklog Session 89 + the SKILL doc Session 90 row | docs | repo root + `docs/` |
| 9 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/item-card.tsx:45-52` — the CLASSIFICATION_ICONS
  map (savings: PiggyBankIcon); `:165` the chip's
  `<ClsIcon className="mr-1 h-3 w-3" />` (12×12, mr 4 — the measured
  chrome); `:178` the Recurring chip's RepeatIcon; `:189` the footer
  calendar icon — the swap touches the import only.
- `src/components/budget/sidebar.tsx:23-24` — the nav rail's Savings
  (PiggyBankIcon) + Net Worth (TrendingUpIcon) links.
- `src/components/budget/dashboard-view.tsx:478-479` — the stat-row
  icons (TrendingUpIcon / PiggyBankIcon); `:54-56` the LEGEND_ICONS
  map; `:966/:994` the QuickAction + StatCard icon props — all take
  `{ className, style }` (the custom components' props signature).
- `src/components/budget/net-worth-view.tsx:309/:354` — the hero
  (h-6 w-6) + summary (h-8 w-8) TrendingUpIcons.
- `src/components/budget/items-view.tsx:57` (the view icon map) +
  `:178` the search-input SearchIcon; `login-card.tsx:259` the
  email-input MailIcon; `item-details-dialog.tsx:64` +
  `budget-item-dialog.tsx:64` the dialog icon maps — same signature.
- The e2e contract: the glyph spec runs AUTHENTICATED via the setup
  project's storageState (the deterministic e2e seed — the savings
  view renders Emergency Fund, the /expenses first card want-
  classified per the seed; the census asserts the GLYPH SHAPES not
  the classification text, so the seed's classifications are fine).
  The login-page mail glyph test opts OUT (the empty storageState —
  the auth.spec.ts:8 pattern). The existing pins are SAFE: the
  dashboard/dialog-buttons/items specs select `svg.lucide-piggy-bank`
  — the custom components keep the class prefix, so every selector
  still matches (the swap changes the SHAPES, which no existing pin
  asserts). The v54 F1 pin (the chip geometry) is unaffected (the
  chrome is identical; only the inner path data changes — the chip
  sizes at h-3 w-3 unchanged).
- TrendingDownIcon stays lucide (NEITHER site renders it on the
  current data — both nets positive; the reference's own trending-down
  glyph is unmeasured, a data-conditional surface noted for the queue).
- The chain gate: lint → typecheck → 108 unit → build → 248 e2e
  (**254** after: +6 — the glyph-parity suite) → 35 smoke.
- Execution notes: `pkill -f agent-browser` + a stale-session-file
  sweep before every agent-browser run (the v50/v51 lesson); a
  rebuild swaps .next/standalone UNDER a running parity server —
  reboot the :3200 server after every build (with-server.sh boots
  fresh per command); the reference session EXPIRES between long
  eval gaps — re-login via the same eval before any follow-up census.
- DEFERRED queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state census. NEW deferred: the reference's
  trending-down glyph (data-conditional — renders only when its net
  goes negative), and the reference's line-items dialog glyphs
  (a line-item CREATE on the reference is a write).
