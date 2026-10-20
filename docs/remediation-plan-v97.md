# Remediation Plan v97 — the re-run cycle's next-oldest candidate (the v91-era ITEMS pair's sixth re-run) + the axe watch + the filter-listbox panel/option-interior census pin (PIN-ONLY)

The formal narrative: `docs/session_232.md` (the v96 cycle's own narrative
log). The queue: the v96 plan's v97 suggestion — **the ledger-verified
target** (the v96-era docs' suggestion AGREEING with the rotation ledger:
the v91-era ITEMS pair [the INCOME + EXPENSES view pair at desktop
1280x800, full-page], last re-shot v91 — now the oldest remaining
[v91 < v92 < v93 < v94 < v95 < v96]; the pair's SIXTH re-run
[v57 → v64 → v70 → v79 → v85 → v91 → v97] — the TWENTIETH consecutive
queue/ledger agreement), plus the axe-core watch at its re-check point
and the 91st standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 300.**

## The pre-execution ledger verification (the queue-prose verification lesson, applied)

The rotation ledger's authority is the PROBE LINEAGE, never the prose
queue phrasing. Verified against `scripts/parity-probes/vlm-shots-v91.sh`
before the derivation: its own header reads "the ITEMS view (income +
expenses) at desktop 1280x800, FULL-PAGE — the fresh re-run of the
OLDEST re-run candidate (the v57-era items pair, last re-shot v85 — the
FIFTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91]" — matching
the queue's phrasing exactly (no transcription error; the v91-era
surface names confirmed: INCOME + EXPENSES at desktop 1280x800
full-page). The SIXTH re-run bracket [v57 → v64 → v70 → v79 → v85 →
v91 → v97] constructed from the same header's FIFTH bracket. The
standing-checks pair (ref-standing-v91.sh + standing-checks-v91.sh)
derived from v90 across the THREE token families (v90→v91, 90th→91st,
ref90→ref91/clone90→clone91), version-bump-only verified by normalizing
back and diffing clean (zero old tokens remaining — the persisted
derive-standing-v97.py, both halves bash -n clean).

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items
/ 3 assets / 2 liabilities) before any flow ran; lint ✓ · typecheck ✓ ·
108/108 unit ✓ · `npm run build` ✓ (robots + sitemap prerendered) ·
**299 e2e ✓** (134 + 96 + 71 chunk executions across three chunk splits
of the 24 files = 301 total = 299 unique tests — the exact documented
v96 state, zero flakes on the first run) · 35/35 smoke ✓. The workspace:
the CARRIED-OVER environment (the session-log-only commit class — pulled
to main @ 27c5970; the two commits since the v96 push 90f766e
[59e7d14 + 27c5970] verified session-log-only [docs/session_231.md +
docs/session_232.md — ZERO src/ or lockfile deltas], so the v96 cycle's
own environment carries over unchanged, no re-provisioning).

The codebase audit clean: the production seams re-audited — auth
(scrypt/HMAC), the db-path contract (db-path.ts + its unit test; the
sandbox's polluted parent DATABASE_URL re-confirmed the reason the
`env -u` discipline is load-bearing), the SEO pair (robots.ts allow-all
+ sitemap.ts 5-URL structure — both prerendered by the build), the
Tailwind v4 mitigations (`@variant hover (&:hover)` + the toast
pointer-events fix + the space-y v3-semantics restore + the inline-rgba
color discipline), the three test tiers; skills/ excluded throughout
(the eslint ignores + the tsconfig exclude verified live).

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (dist-tags: rc/next sha
prereleases only beyond — no stable 4.14.1, no 5.x exists); the
installed wrapper 4.14.0 + the engine 4.14.0; the lockfile holding the
v68 dedupe state (exactly one `node_modules/axe-core` entry); the
engine-contract pin GREEN standalone (2 passed).

### F2 — the 91st standing checks: ALL GREEN (version-bumped from v90 — version-bump-only diffs verified)

ref-standing-v91.sh + standing-checks-v91.sh (version-bumped from v90
via the persisted derive-standing-v97.py across the THREE token families
[v90→v91, 90th→91st, AND the bare session names ref90→ref91/
clone90→clone91]; after normalizing back the files are version-bump-only:
diffed clean, zero old tokens remaining). Reference side: the four bugs
ALL live [toast-blocker `hitIsBurgerChild:false`; sheet-trap
`overlayCount:1` after nav; no-landmark `navLandmark:false`; the 464px
/networth overflow at 390 measured docSW 464 directly — the script's
settle-wait form working]; the data census UNCHANGED with ONE
timing-artifact re-read (the expenses leg first read "no match" — the
eval raced the page's client-side render; the settle-wait re-read after
a fresh login measured the exact documented "4 items · $525.00"; the
networth "1 items · $25,000" / income "1 items · $5000.00" clean on the
first read — the v79 lesson generalized: ANY multi-eval reference flow
treats a "no match"/empty census as a possible expiry/render race first);
the SEO pair live. Clone side: R1–R4 ALL GREEN — **the mobile menu
VERIFIED WORKING the 91st consecutive time** (`hitIsBurgerChild: true`,
the sheet opens, closes on nav, the nav landmark present — the Tailwind
v4 mitigation holds), zero overflow at 390 on all five views, the SEO
pair live.

### F3 — the re-run pair (the v91-lineage derivation, the two-half census form)

The probe series derived from the v91 lineage (derive-v97-series.py,
persisted): vlm-shots-v97.sh + clone-vlmshots-v97.sh +
vlm-compare-v97.mjs + arbit-v97.sh — the generic swaps (v91→v97,
refvlm91→refvlm97, clonevlm91→clonevlm97, refarbit91→refarbit97,
clonearbit91→clonearbit97, /tmp/vlm91→/tmp/vlm97) followed by the
exact-fragment history corrections (last-re-shot v85→v91, FIFTH→SIXTH,
the re-run bracket extension, the every-other-pair list [savings v92,
login+calculator v93, networth+drill-down v94, dashboard v95, mobile
twins v96]) — every correction verified applied (the derive script
reports each hit; all four applied clean on the first run); bash -n +
node --check clean on all four; zero residual old tokens (the
legitimate v91 tokens — the "last re-shot v91" provenance + the SIXTH
bracket — whitelisted in the residual check by context). The census
BUILT two-half from the start (build-twohalf-v97.py — ref-arbit-v97.sh +
clone-arbit-v97.sh, the ONE census JS block [CENSUS_JS 193 lines]
extracted once and embedded byte-identically across the halves — the
md5 line-block contract [b55dcd29]; the doubled-brace spot grep clean).
The reaping budget applied as the standing step between every half.
Login on the first attempt both sides; the parked pointer at (5,5);
read-only — the v46 rule holds.

**Both verdicts DIFFERENT, every flag DOM-arbitrated to a documented
class:**

1. **PAIR 1 (INCOME at 1280)**: the avatar "U" vs "D" — the
   user-identity class (the chrome byte-identical: 36×36 / 9999px /
   14px / 600 / white / rgb(143,188,63)); the header stats "1 items ·
   $5000.00" vs "2 items · $5550.00" + the 1-card vs 2-card grid + the
   card contents (amounts/dates/badges) — the seed-data classes; the
   "Recurring" 4th badge — the DATA-CONDITIONAL class (the reference's
   own income item ships recurring=false).
2. **PAIR 2 (EXPENSES at 1280)**: the payment-method footer chips (the
   reference's expense cards date-only vs the clone's date + chip) —
   the **v57 DATA-CONDITIONAL class** (the census proves the reference
   RENDERS payment chips when data carries them: its own income card's
   footer childCount 2 with the "Bank Account" chip + icon; its expense
   items simply ship no payment method — footer childCount 1 — while
   the clone's carry them); the badge wrap (the clone's badgeRow h 52,
   2 DOM lines) — the **v57/v70b Recurring-wrap class** (the superset
   Recurring badge wraps → h 52 [22+8+22] → the card h 230 vs the
   reference's 200 — the v70b-decomposed class: +30px wrap + the 1-row
   sibling stretch); the "Edit with Base44" FAB — the platform-chrome
   class, re-arbitrated live by the one-shot both-sides DOM census
   (base44-fab-arbit-v97.sh: fabCount 0 + bodyHasBase44 false on BOTH
   sides — the FAB renders in the reference's platform iframe chrome,
   outside the queryable body DOM; this cycle the VLM attributed it to
   the reference — the non-inverted form of the v85/v91-documented
   attribution class); the header stats + card contents — the
   seed-data classes.

The both-sides census (the two-half controlled form) **REPRODUCES the
v85/v91 census values EXACTLY — zero drift on every axis**:

- **The AVATAR chrome** {36×36 / radius 9999px / fs 14px / fw 600 /
  color white / bg rgb(143,188,63)} — byte-identical; the identity text
  the only delta (the user-identity class).
- **The GRID + CARD chrome** {grid w 960 / gap 16px / the 3-col
  309.328px template family; card w 309 / pad 20px / radius 12px /
  border rgb(229,231,227)} — byte-identical; the childCount (1 vs 2
  income, 4 vs 3 expenses) the seed-count class; the card h (200 vs
  230) the v70b-decomposed class; the income template's last-column
  sub-pixel (ref .328 ×3 vs clone .328/.328/.344) the column-distribution
  rounding noise WITHIN the documented 309.328px family (the ref
  expenses template reads .328/.328/.344 — byte-identical to the
  clone's).
- **The TITLE ROW chrome** {gap 8px / dot 8×8 / dotBg per type
  [rgb(143,188,63) income / rgb(224,122,59) expenses] / font 16px /
  weight 600} — byte-identical.
- **The AMOUNT leaf chrome** {fs 24px / fw 700 / lh 32px / h 32; the
  per-type accents matching} — byte-identical; the texts the seed-data
  class.
- **The FOOTER + BADGE chrome** {footer flex/space-between/12px/
  rgb(107,114,128)/h 16 with the children flex gap 4px icons 12×12; the
  badge row flex/wrap/8px gap/mb 12px; badge0 radius 6px/pad 2px 10px/
  fs 12px/fw 600/h 22} — byte-identical; the expenses footer childCount
  (1 vs 2) the v57 DATA-CONDITIONAL class; the badgeRow h (22 vs 52) +
  texts the v57 wrap/classification-VALUE classes.
- **The FILTER CARD on BOTH variants** {the income variant: card
  960×86/pad 24px/radius 16px/search 447×36 SPANNING/3 children/2
  comboboxes 216×36 at 14px; the expenses variant: search 216×36 NOT
  spanning/4 children/3 comboboxes} — byte-identical (the v64/v70
  contract); the page header row + the docSW 1280 guard on both views.

**NO NEW CLONE GAP — the v97 iteration PIN-ONLY.**

### F4 [PIN] — the filter LISTBOX PANEL + OPTION-RESTING interior census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 300)

The never-pinned family (the FAMILY-EXTENSION pattern — the missing
middle layer): the items view's filter SELECT listbox PANEL chrome. The
v36 S2 pin holds the listbox's OPTION-level chrome (the selected
option's focus-state bg rgb(245,245,245) + color rgb(23,23,23) — the
:focus-driven family); the v91 pin holds the TRIGGER's resting chrome
{pad 8px 12px/radius 6px/border/typography}; the v92 pin the savings
variant's search-icon family — **the PANEL container itself (the
popover's bg/radius/border/shadow/max-h/overflow/z + the viewport's
4px pad) and the option's RESTING interior (fs/fw/color/pad/radius/h)
are NEVER pinned at ANY viewport in ANY spec** (the coverage-map grep
across all 24 specs: no spec asserts any `[role=listbox]` panel
geometry; the only option-level computed-style pins are the
focus/highlight state [items.spec v36 + tokens.spec G5] and the
calculator's v34 S2 keyboard contract — none pin the resting interior).

**The pin's own axes first measured byte-identical on BOTH sides** by
the supplemental two-half census (listbox-arbit-v97.sh +
listbox-clone-v97.sh — BUILT two-half from the start via
build-listbox-v97.py, the census JS byte-identical by the md5
line-block diff [34c916da — 36 lines]; both sides read-only; the
seedcheck exact after the run; the doubled-brace spot grep clean):

- The PANEL: {bg `rgb(255, 255, 255)`, radius `6px`, border `1px
  rgb(229, 229, 229)`, maxH `384px`, overflow `hidden`, z `50`, pos
  `relative`, w `218`} — **byte-identical across sides** (the
  rounded-md/border-input/bg-popover/max-h-96 family).
- The shadow's VISIBLE layers: `rgba(0, 0, 0, 0.1) 0px 4px 6px -1px` +
  `rgba(0, 0, 0, 0.1) 0px 2px 4px -2px` (the shadow-md family) —
  byte-identical; the full string's zero-layer LEAD count differs (ref
  2 leads vs clone 4) — the **v3/v4 shadow-construct class** (the
  documented v37 O1 note: every lead is a 0px-spread shadow, invisible
  by construction; the VISIBLE layers are the contract — asserted via
  containment, the established toContain form).
- The VIEWPORT: {pad `4px`, display `block`} — byte-identical (the
  p-1 family).
- The OPTION's RESTING interior: {fs `14px`, fw `400`, color
  `rgb(23, 23, 23)`, pad `6px 32px 6px 8px`, radius `4px`, h `32`} —
  **byte-identical across sides** (the text-sm/pr-2/pl-2 family with
  the check-slot's 32px right pad).
- The documented-class deltas (NOT pin axes): the panel h {ref 74 vs
  clone 106} + the optCount {2 vs 3} — the seed-data class (the
  reference's 1 income item → 2 categories; the clone's 2 income items
  → 3 categories); the docSW 1280 on both sides.

**The pin** (tests/e2e/items.spec.ts, appended as the v97 describe
block): the census finder is the supplemental census's own finder
verbatim (the category trigger by aria-label/text → click → settle
past the animate-in window [700ms] → the [role=listbox] panel → the
viewport via [data-radix-select-viewport] with the 4px-pad fallback →
the first [role=option]); asserts — the panel {bg, radius `6px`,
border `1px rgb(229,229,229)`, maxH `384px`, overflow `hidden`, z
`50`, pos `relative`, w `218`}; the shadow's visible layers via
toContain (both `rgba(0, 0, 0, 0.1) 0px 4px 6px -1px` and
`rgba(0, 0, 0, 0.1) 0px 2px 4px -2px`); the viewport {pad `4px`,
display `block`}; the opt0 resting interior {fs `14px`, fw `400`,
color `rgb(23, 23, 23)`, pad `6px 32px 6px 8px`, radius `4px`, h
`32`}; the panel h asserted as the CLONE's own data-dependent value
(106 — the 3-option stack: 3×32 + 2×4 viewport pad + 2×1 border); the
optCount 3 guard (the clone's own seed); the docSW 1280 guard. The
panel h and optCount are asserted as the CLONE's own values (never
cross-side axes — the data-dependent class rule), re-affirmed as
regression guards of the clone's own rendering.

**The pin-sanity mutation (the planned form)**: the SelectContent
panel's `rounded-md` → `rounded-lg` (src/components/ui/select.tsx:68,
by LINE NUMBER — the line-scoping keeps the SelectTrigger's own
`rounded-md` at line 19 untouched [the v91 pin's 6px trigger axis]).
Expected: the pin FAILS at exactly the panel radius axis alone
(`6px` → `8px`); cascade-free BY CONSTRUCTION (no spec asserts any
listbox panel radius — this pin is the first; the trigger's radius is
a different element at a different line; the calculator's
`panel.radius 16px` [calculator.spec.ts:727] is the calculator DIALOG
panel, a different element; the radius never changes bg/border/shadow/
max-h/overflow/z/viewport-pad/option-interior; `rounded-lg` on the
panel does not affect the CLOSED state — the panel renders only when
open). Then restored (git diff src/ = 0 lines; the standalone REBUILD
via the FULL npm run build; the post-restore full items.spec.ts run
green).

**The disproven-in-advance candidates (documented without execution):**
the panel bg mutation (bg-popover → bg-white-visual-identical class
— a no-op flip, not a demonstration); the option pad mutation (pr-2 →
pr-3: cascades to the option's h arithmetic via the check-slot — a
weaker single-axis read than the radius); the viewport pad mutation
(p-1 → p-2: changes the panel h arithmetic [106 → 114] — a
two-axis failure, not the clean single-axis form); the border
mutation (border-input → border-2: changes borderWidth AND the panel
h — two axes).

## The ToDo list

| # | Step | Status |
|---|------|--------|
| 1 | F0 baseline chain on the carried-over workspace | DONE — all green |
| 2 | F1 axe-core watch | DONE — NO DRIFT |
| 3 | F2 91st standing checks (derived v90→v91, version-bump-only verified) | DONE — ALL GREEN (the expenses census timing-artifact re-read documented) |
| 4 | F3 the v91-lineage probe derivation (generic swaps + exact-fragment history corrections + residual checks) | DONE |
| 5 | F3 two-half census builder (build-twohalf-v97.py, md5 contract) + both halves executed | DONE |
| 6 | F3 the VLM pairwise | DONE — both verdicts DIFFERENT, all flags arbitrated |
| 7 | F3 the base44-fab one-shot re-arbitration | DONE — the platform-chrome class (fabCount 0 both sides) |
| 8 | F4 the supplemental listbox two-half census (the pin's own axes measured byte-identical) | DONE |
| 9 | F4 THIS PLAN written + validated BEFORE the pin's execution | DONE |
| 10 | F4 append the v97 pin to tests/e2e/items.spec.ts | PENDING |
| 11 | F4 pin first run (GREEN expected) | PENDING |
| 12 | F4 pin-sanity mutation (ui/select.tsx:68, line-number-scoped) → single-axis failure → restore (git diff src/ = 0) → standalone REBUILD → post-restore full file run | PENDING |
| 13 | F5 full chain re-run (lint/typecheck/108 unit/build/300 e2e/35 smoke) + the screenshots regeneration + byte-compare | PENDING |
| 14 | D1–D7 docs alignment + session_233.md + the worklog Session 132 entry | PENDING |
| 15 | ship: the full chain re-run + commit + SSH-wrapper push | PENDING |

## The pre-execution validation section (the measured evidence)

- The pin's measured values (the listbox two-half census, this session):
  panel {bg rgb(255,255,255), radius 6px, border 1px rgb(229,229,229),
  maxH 384px, overflow hidden, z 50, pos relative, w 218} byte-identical;
  the shadow's visible layers {rgba(0,0,0,0.1) 0px 4px 6px -1px +
  rgba(0,0,0,0.1) 0px 2px 4px -2px} byte-identical (the zero-layer lead
  count 2-vs-4 the v3/v4 construct class); the viewport {pad 4px,
  display block} byte-identical; the opt0 resting interior {fs 14px,
  fw 400, color rgb(23,23,23), pad 6px 32px 6px 8px, radius 4px, h 32}
  byte-identical; the clone's own axes {panel h 106, optCount 3,
  docSW 1280}; the seedcheck exact after the run.
- The mutation target line verified by reading the source:
  src/components/ui/select.tsx:68 — the SelectContent className carries
  EXACTLY ONE `rounded-md` (grep-count 1 on the line); the
  SelectTrigger's identical `rounded-md` token sits at line 19 (the
  v91 pin's 6px trigger axis — untouched by the line-number scoping).
- The coverage-map grep (run across ALL 24 specs): no spec asserts any
  `[role=listbox]` panel geometry (grep "listbox.*radius|panel" — the
  calculator's panel.radius 16px is the calculator DIALOG panel, a
  different element); the option-level computed-style pins are the
  focus/highlight STATE only (items.spec v36 S2 + tokens.spec G5 +
  calculator v34 S2) — the RESTING interior (pad/radius/h/fs/fw) never
  pinned; the option pad string "6px 32px 6px 8px" appears in NO spec.
- The rotation ledger verified: the items pair last re-shot v91 = the
  oldest remaining [v91 < v92 < v93 < v94 < v95 < v96] — the v96-era
  docs' v97 suggestion agreeing with the ledger (the TWENTIETH
  consecutive agreement), the surface names verified against
  vlm-shots-v91.sh's own header before the derivation.
- The pin's finder: the supplemental census's own finder verbatim (the
  category trigger by aria-label/text-content → click → the 700ms
  settle past the animate-in window → the [role=listbox] panel → the
  [data-radix-select-viewport] with the 4px-pad fallback → the first
  [role=option]) — proven stable across this session's three
  independent runs (the manual reference probe + the manual clone
  probe + the two-half census halves).

## Operational lessons this cycle (the probe README's D6 section)

- THE CENSUS RENDER-RACE GENERALIZATION (the v79 expiry-twin, extended):
  the reference-side expenses census read "no match" — not because of
  the session expiry (the v79 form) but because the eval raced the
  page's client-side render (the timing-artifact family). The
  generalized discipline: ANY multi-eval reference flow treats a "no
  match"/empty census as a possible expiry OR render race first
  (re-login + settle-wait + re-read) before suspecting drift — and
  never records the state change on a single raced read.
- THE PANEL-CHROME MISSING-MIDDLE FAMILY (NEW): the v91/v92
  trigger-interior pins and the v36 option-state pins bracket the
  filter select's popover, but the PANEL container itself (bg/radius/
  border/shadow/max-h/viewport-pad) was never pinned at any viewport —
  the family-extension survey should walk the COMPONENT LAYERS
  (trigger → panel → viewport → option), not just the axes of one
  layer.
- THE TWO-HALF FORM AS THE DEFAULT (the v92..v96 lesson, applied clean
  again): every census this cycle (the pair census + the supplemental)
  BUILT two-half from the start — zero resource-exhaustion symptoms.

## The next queue (the v98 suggestion — verify against the rotation ledger before executing)

(1) the re-run cadence rotates to the next-oldest candidate after the
items pair (the v92-era SAVINGS pair [the SAVINGS view + the goal-card
interior pair at desktop 1280x800], last re-shot v92 — now the oldest
remaining [v92 < v93 < v94 < v95 < v96 < v97]; the pair's re-run
bracket to be verified against vlm-shots-v92.sh's own header before
the derivation), (2) the axe-core watch at its next re-check point
(only a 5.x wrapper changes the calculus), (3) the deferred
reference-write censuses (unchanged — out of bounds under the v46
read-only rule).
