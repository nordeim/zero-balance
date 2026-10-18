# Remediation Plan v91 — the re-run cycle's next-oldest candidate (the v85-era items pair's fifth re-run) + the axe watch + the filter-card interactive-interior census pin (PIN-ONLY)

The formal narrative: `docs/session_219.md` (the v90 cycle's own narrative
log). The queue: the v90 plan's v91 suggestion — **the ledger-verified
target** (the v90-era docs' suggestion AGREEING with the rotation ledger:
the v85-era ITEMS pair [the INCOME + EXPENSES view pair at desktop
1280x800, FULL-PAGE] — last re-shot v85, the oldest remaining
[v85 < v86 < v87 < v88 < v89 < v90]; the pair's FIFTH re-run
[v57 → v64 → v70 → v79 → v85 → v91] — the FOURTEENTH consecutive
queue/ledger agreement), plus the axe-core watch at its re-check point
and the 85th standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 294.**

## The pre-execution ledger verification (the queue-prose verification lesson, applied)

The rotation ledger's authority is the PROBE LINEAGE, never the prose
queue phrasing. Verified against `scripts/parity-probes/vlm-shots-v85.sh`
before the derivation: its own surface list reads "(1) the INCOME view …
(2) the EXPENSES view" at "desktop 1280x800, FULL-PAGE" — the ITEMS pair,
matching the queue's phrasing exactly this cycle (no transcription error
to correct). The re-run bracket verified against the same scripts' header
("the FOURTH re-run of the pair [v57 → v64 → v70 → v79 → v85]") — v91 is
the FIFTH re-run. The standing-checks pair (ref-standing-v85.sh +
standing-checks-v85.sh) derived from v84 across the three token families
(v84→v85, 84th→85th, ref84→ref85/clone84→clone85), version-bump-only
verified by normalizing back and diffing clean.

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered) · **293 e2e ✓** (127 + 106 + 62 chunk executions
across three chunk splits of the 23 files = 295 total = 293 unique tests
[292 chromium + 1 setup, the setup re-run per chunk as the project
dependency] — the exact documented v90 state, zero flakes on the first
run) · 35/35 smoke ✓. The workspace REBUILT (the fresh-clone path, the
v86/v88/v90 precedent): `git clone` at main @ 07586b7, the tree clean;
the environment re-provisioned (npm ci 354 packages; `.env` written
[DATABASE_URL="file:../db/custom.db"], `db/` at the repo root,
db:generate + db:push + db:seed; chromium-1243 installed; the paramiko
ssh shim deployed outside the repo at /home/z/my-project/bin/ssh); the
seedcheck exact (7 items / rent 1850 / 0 line items / 3 assets /
2 liabilities) before any flow ran, no orphaned servers.

The codebase audit clean: the v90 commit (1c9438f) re-verified PIN-ONLY
as documented (17 files, +1429/-13, ZERO src/ changes); the one commit
since (07586b7) session-log-only (session_219.md); the production seams
re-audited (auth scrypt/HMAC, the db-path contract, the SEO pair
[robots.ts + sitemap.ts — both prerendered by the build], the Tailwind v4
mitigations [`@variant hover (&:hover)` + the toast pointer-events fix +
the space-y v3-semantics restore + the inline-rgba color discipline],
the three test tiers); the repo's skills/ folder excluded from
checking/testing/compilation throughout (eslint ignores + tsconfig
exclude, verified live).

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next
prereleases beyond — no stable 4.14.1, no 5.x exists); the installed
wrapper 4.14.0 + the engine 4.14.0; the lockfile holding the v68 dedupe
state (no nested engine dir under node_modules/@axe-core/playwright/);
the engine-contract pin GREEN standalone (2 passed).

### F2 — the 85th standing checks: ALL GREEN (version-bumped from v84 — version-bump-only diffs verified)

ref-standing-v85.sh + standing-checks-v85.sh (version-bumped from v84 —
after normalizing the THREE token families [v84→v85, 84th→85th, AND the
bare session names ref84→ref85/clone84→clone85] the files are
version-bump-only: verified by normalizing back and diffing clean, zero
old tokens remaining). Reference side: the four bugs ALL live
[toast-blocker `hitIsBurgerChild:false`; sheet-trap `overlayCount:1`;
no-landmark `navLandmark:false`; the 464px /networth overflow at 390];
the data census UNCHANGED (the 85th clean drift check: networth "1 items
· $25,000" / income "1 items · $5000.00" / expenses "4 items · $525.00");
the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation
menu VERIFIED WORKING (the **85th consecutive time**:
`hitIsBurgerChild:true`, the sheet opens, closes on nav, the nav landmark
present), zero overflow at 390 on all five views (docSW 390 everywhere),
the SEO pair live.

### F3 — the re-run pair (the v85-era items pair: the income + expenses views at desktop 1280x800, full-page — the pair's FIFTH re-run)

The probe series derived from the v85 lineage (vlm-shots-v91.sh +
clone-vlmshots-v91.sh + vlm-compare-v91.mjs + arbit-v91.sh — the sed
derivation with the version + session-name + tmp-dir substitutions
[vlm85→vlm91, refarbv85→refarbit91, clonearbv85→clonearbit91,
v85→v91; the shots' session names refvlm85→refvlm91/
clonevlm85→clonevlm91 riding the vlm85→vlm91 family]; the headers
history-corrected to the FIFTH re-run [v57 → v64 → v70 → v79 → v85 →
v91] + "last re-shot v85"; the functional bodies verified
version-bump-only by the normalize-back diff — only the intentional
history-correction comment lines differ; login on the first attempt both
sides; the parked pointer at (5,5); read-only on the reference — the
v46 rule holds).

**Both verdicts DIFFERENT, every flag DOM-arbitrated to a documented
class — the SAME flag-set classes as the v85 re-run itself:**

1. **PAIR 1 (INCOME at 1280)**: the avatar letter "U" vs "D" — the
   user-identity class; the 1-card vs 2-card grid + the card figures +
   the badge variations — the seed-data classes (the reference's 1 income
   item vs the clone's dev-seed 2; the Recurring badge the clone's
   superset).
2. **PAIR 2 (EXPENSES at 1280)**: the card footer's payment-method chips
   (ref: date only on its first card) — the v57 DATA-CONDITIONAL class;
   the badge wrap to a second line (the taller cards) — the v57 Recurring
   superset wrap class; the 4-vs-3 card grid — the seed-count class; the
   avatar — the user-identity class; **the "Edit with Base44" FAB flag —
   the SAME VLM IMAGE-ATTRIBUTION SWAP class the v85 re-run itself
   documented, re-arbitrated live this cycle by the one-shot both-sides
   DOM census (base44-fab-arbit-v91.sh, the v85 precedent's own finder):
   `fabCount:0, bodyHasBase44:false` on BOTH sides' /income at 1280 —
   the FAB renders in the REFERENCE's platform iframe chrome, outside
   the queryable body DOM, exactly as the v85 pixel census proved (6585
   dark px in the reference's bottom-right crop vs 0 in the clone's);
   the flag's true class: the Base44 platform-chrome class.**

The both-sides census (arbit-v91.sh — **executed in the TWO-HALF
CONTROLLED FORM** [ref-arbit-v91.sh + clone-arbit-v91.sh, the census JS
byte-identical across the halves — the lines-1-215 identity verified] —
after the combined script's mid-run chromium resource exhaustion: 70
zombie processes reaped; the symptom the v89-documented one [the timeout
with empty eval results, not an error surface]; retry-first confirmed
the two-half form clean, the v89 lesson re-verified) — **REPRODUCES the
v85 census values EXACTLY — zero drift since v85 on every axis:**

- **The AVATAR chrome BYTE-IDENTICAL** (w 36 × h 36 / radius 9999px /
  fs 14px / fw 600 / color rgb(255,255,255) / bg rgb(143,188,63) — the
  identity text "U" vs "D" the only delta, the user-identity class).
- **The GRID + CARD chrome BYTE-IDENTICAL** (grid w 960 / gap 16px /
  the 3-col 309.328px template; card w 309 / pad 20px / radius 12px /
  border rgb(229,231,227)); the childCount (1 vs 2 income, 4 vs 3
  expenses) the seed-count class; the card h (ref 200 vs clone 230) the
  v70b-decomposed class — the Recurring superset badge's wrap h 52
  (22+8+22) → +30px, and the 1-row grid STRETCHES the shorter sibling.
- **The TITLE ROW chrome BYTE-IDENTICAL** (gap 8px / dot 8×8 / income
  dotBg rgb(143,188,63) + expenses dotBg rgb(224,122,59) on BOTH sides /
  font 16px / weight 600).
- **The AMOUNT leaf chrome BYTE-IDENTICAL** (fs 24px / fw 700 / lh 32px
  / h 32; the income accent rgb(143,188,63) + the expenses accent
  rgb(224,122,59) matching per type — the texts the seed-data class).
- **The FOOTER + BADGE chrome BYTE-IDENTICAL** (footer
  flex/space-between/12px/rgb(107,114,128)/h 16 with the children flex
  gap 4px icons 12×12; the badge row flex/wrap/8px gap/mb 12px; badge0
  radius 6px/pad 2px 10px/fs 12px/fw 600/h 22); the expenses footer
  childCount (1 vs 2) the v57 DATA-CONDITIONAL class; the badgeRow h
  (22 vs 52) + texts the v57 wrap/classification-VALUE classes.
- **The FILTER CARD BYTE-IDENTICAL on BOTH variants** (the income
  variant: card 960×86/pad 24px/radius 16px/search 447×36
  SPANNING/3 children/2 comboboxes 216×36 at 14px; the expenses variant:
  search 216×36 NOT spanning/4 children/3 comboboxes — the v64/v70
  contract re-verified) + the page header row + the docSW 1280 guard.

**NO NEW CLONE GAP — the v91 iteration is PIN-ONLY.**

### F4 [PIN] — the filter-card INTERACTIVE-INTERIOR census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 294)

The never-pinned axes (the existing pins cover around them — the v64 F3
pin holds the filter CARD + search GEOMETRY {w/h/pad/radius/border} +
the innerGrid + the comboboxes' {w/h/fs/text} at 1280 on the income
variant; the v70 F4 pin the expenses variant's 4-child/3-combobox
census; the v37 S1 pin the triggers' FOCUS-STATE chrome {fv ring/
borderColor/borderWidth/w/h} and the v37 S2 pin the search's focus ring;
the v65 F3 pin the page-header row at 1280 [on /savings]; the v45/v57/
v74/v79/v80/v85/v86 pins the card/titleRow/amount/footer/badge/subtitle
families; **the INTERACTIVE INTERIORS' RESTING chrome — the combobox
triggers' own pad/justify/align/bg/radius/border/fw/color + the chevron
svg's size and color, and the search input's TYPOGRAPHY {fs/fw/lh/color}
— are never pinned at ANY viewport**):

- **The SEARCH input's TYPOGRAPHY at 1280** (items-view.tsx:184-190 —
  the shared `Input` with the view-local `pl-10`): {tag "INPUT", fs
  "14px", fw "400", lh "20px", color "rgb(10, 10, 10)"} + the per-view
  placeholder texts ("Search income items..." / "Search expense
  items...") + the pad "4px 12px 4px 40px" / radius "6px" re-affirm
  (the v64/v70 contract);
- **The combobox TRIGGERS' RESTING chrome at 1280** (per trigger, every
  trigger on both views): {tag "BUTTON", w 216, h 36, pad "8px 12px",
  justify "space-between", align "center", bg "rgba(0, 0, 0, 0)",
  radius "6px", borderW "1px", borderC "rgb(229, 229, 229)", fs "14px",
  fw "400", color "rgb(10, 10, 10)", chev {w 16, h 16, color
  "rgb(10, 10, 10)"}} + the trigger texts ("All Categories" / "All
  Frequencies" / "All Payment Methods");
- The docSW 1280 guard on both views.

Every pinned axis is STATIC chrome (the filter card's default resting
state — the placeholders and trigger texts are view-constant, no data
conditionals); the pin rides the plain authenticated /income and
/expenses views at 1280×800 on the e2e seed (read-only — no fixture
writes), in tests/e2e/items.spec.ts (the v57/v64/v70/v85 pins' own
file), reusing the census's own finder verbatim (the wide input > 100 →
the closest div.rounded-2xl → the inner grid → the [role=combobox]
children + the svg inside each).

**The pin's own axes first measured byte-identical on both sides by the
supplemental census** (filter-interior-arbit-v91.sh +
filter-interior-clone-v91.sh — the v87/v88/v89/v90 one-shot precedent,
executed in the two-half controlled form with the census JS verified
byte-identical across the halves by the md5 line-block diff): on BOTH
sides' /income AND /expenses at 1280×800, the search reads {INPUT/text,
fs 14px, fw 400, lh 20px, color rgb(10,10,10), pad "4px 12px 4px 40px",
radius 6px, the placeholders byte-identical} and every trigger reads
{BUTTON, 216×36, pad "8px 12px", justify space-between, align center,
bg rgba(0,0,0,0), radius 6px, borderW 1px, borderC rgb(229,229,229),
fs 14px, fw 400, color rgb(10,10,10), chev 16×16 rgb(10,10,10)} —
ZERO deltas on any axis (the docSW 1280 both views).

**The pin-sanity mutation (the executed form — the viewport-scoped
responsive-variant dodge, the v80/v86/v87/v88/v89/v90 pattern, scoped
AT-lg this cycle because the pin runs at 1280)**: the search input's
view-local `pl-10` → `pl-10 lg:font-medium` (items-view.tsx:188, applied
by LINE NUMBER — the className on the items views' OWN search Input
instances alone; the login page's and the dialogs' Input instances carry
their own classNames, untouched) — flips EXACTLY the pin's search.fw
axis at the pin's OWN viewport ("400" → "500" at ≥1024px, where the pin
runs at 1280) and nothing else: the `lg:` variant is INERT below 1024px
(every mobile/tablet pin green by construction); font-weight never
changes line-height (the input's lh stays text-sm's 20px — the
fs/lh/color axes green); font-weight never affects color or geometry
(the input's h 36 is the class-fixed h-9, the pad/radius/w green; the
trigger family a DIFFERENT element, untouched); **no other spec asserts
ANY input element's fontWeight at ANY viewport** — the coverage-map grep
run with BOTH the long form (`fw:` tokens) and the shorthand family
(the `Fw`-suffix keys: h4Fw [the card title], amtFw/trigFw [the
networth stat value and the networth TAB trigger — different
components], the calculator's h2/row families — NONE an input) —
**cascade-free BY CONSTRUCTION** (the expected failure diff reads as
the search's fw axis alone; the fs/lh/color/placeholder/pad/radius
axes, the entire trigger family, and the docSW guard all green), then
restored (the standalone REBUILD as a SEPARATE command; `git diff src/`
= 0 lines; the post-restore full run green).

**The disproven-in-advance candidates (documented without execution —
the design-probe analysis)**: (1) the search's fs mutation (text-sm →
text-base via the shared Input's base class) — REFUTED TWICE: the fs
rides the SHARED Input component (the login page's and the dialogs'
inputs flip too — the shared-component cascade) AND the v86
RATIO-LINE-HEIGHT TRAP (fs 14→16 scales lh 20→24, a two-axis failure
diff); (2) the trigger's pad mutation — the SelectTrigger is the SHARED
shadcn component (every dialog select flips — the v89
shared-component-cascade lesson); (3) the chevron's size — the lucide
ChevronDown inside the shared SelectTrigger (the same cascade); (4) the
search's color mutation — the color rides the shared Input's base
(token-driven, every input surface flips); (5) the borderW/borderC axes
— already pinned by the v37 S1 focus-state pin's own values (not
never-pinned); (6) the docSW axis — a page-level shared surface, never
a mutation target. The view-local `lg:font-medium` dodge is the ONLY
single-axis, view-local, geometry-inert flip on the pin's own surface.

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → `npm run build` → **294 e2e** in chunks
(+1) → 35 smoke; the 16 standing screenshots regenerated + byte-
compared (the same-DB discipline; the seedcheck under
`env -u DATABASE_URL`). EXPECTED: the seed planted and the shots taken
on the same calendar day reproduce the committed set byte-for-byte
(the v82/v88/v90 same-day-seed byte-identity law); any DATE-class diff
pixel-arbitrated per the v66/v75/v80/v86 discipline, never a full-page
VLM verdict; any rasterization-noise class re-classified per pixel if
it recurs.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the filter-card INTERACTIVE-INTERIOR census at 1280 (the search's typography {tag/fs/fw/lh/color/placeholder + the pad/radius re-affirm} + every trigger's resting chrome {tag/w/h/pad/justify/align/bg/radius/borderW/borderC/fs/fw/color/chev w/h/color + the texts} + the docSW guard), riding the plain authenticated /income AND /expenses views | tests/e2e/items.spec.ts |
| 2 | sanity | the pin-sanity mutation (the EXECUTED form): the search's view-local `pl-10` → `pl-10 lg:font-medium` (items-view.tsx:188, by LINE NUMBER) → the pin FAILS at exactly the search.fw axis ("400" → "500" at ≥1024px; the fs/lh/color/placeholder/pad/radius axes, the trigger family, and the docSW guard stay green; every below-1024 pin green — the lg variant inert there); the full items.spec.ts under the mutation: only the v91 pin red; restored → the standalone REBUILD → the post-restore full run green | src/components/budget/items-view.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 294 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v91 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (293→294 + the v91 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v91 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 126 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.48 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v91 section (the new probes + the FAB re-arbitration + the two-half census re-use + the v92 queue) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_220.md + the repo worklog Session 126 entry | docs/session_220.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the filter-interior census's own
  measured values, byte-identical on both sides' /income AND /expenses
  at 1280×800 (the supplemental census ran BEFORE this plan's execution
  — the values above are its verbatim output; the census JS verified
  byte-identical across the two halves by the md5 line-block diff).
- The mutation target line verified by reading the source:
  items-view.tsx:188 is the items views' search Input's own className
  (`className="pl-10"`) — view-local; the login page's Input
  (login-view.tsx) and the dialogs' Inputs carry their own classNames,
  untouched by the line-number-scoped mutation.
- The grep verification (run with BOTH the `fw:` long-form tokens AND
  the `Fw`-suffix shorthand family — the v90 shorthand-token grep
  lesson): NO spec asserts any INPUT element's fontWeight at any
  viewport; the only fw assertions at ≥1024px are on OTHER elements
  (the h4 card titles, the networth stat values and tab triggers, the
  calculator's rows, the badge/label families) — all untouched by the
  view-local flip; the v37 S2 search pin asserts only the focus-state
  chrome (fv/boxShadow/borderColor/borderWidth); the v64/v70 search
  assertions are geometry+pad+radius+border only.
- The rotation ledger verified: the items pair last re-shot v85 = the
  oldest remaining [v85 < v86 < v87 < v88 < v89 < v90] — the v90-era
  docs' v91 suggestion agreeing with the ledger (the FOURTEENTH
  consecutive agreement), the surface names verified against
  vlm-shots-v85.sh's own surface list before the derivation.
- The pin's finder: the census's own finder verbatim (the wide input
  > 100 → the closest div.rounded-2xl → the inner grid → the
  [role=combobox] children) — proven stable across the v64/v70/v85/v91
  censuses.

## Operational lessons this cycle (the probe README's D6 section)

- THE FAB RE-ARBITRATION: the v85-documented Base44 FAB
  image-attribution swap RECURRED at v91 (the VLM attributing the
  reference's own platform FAB to the clone) — re-arbitrated live by
  the one-shot both-sides DOM census (fabCount 0 on both sides, the v85
  finder verbatim): when a documented VLM misattribution class recurs,
  the one-shot DOM arbitration settles it without re-running the v85
  pixel-crop chain (the DOM zero + the documented pixel evidence
  together).
- THE TWO-HALF CENSUS, RETROFITTED: the combined arbit script can fail
  mid-cycle in the chromium resource exhaustion (70 zombies this cycle)
  — the v89 two-half form (the census JS byte-identity as the contract,
  verified by the md5 line-block diff) is the recovery, and the
  supplemental one-shot censuses can be BUILT two-half from the start
  when the sandbox has already shown the exhaustion once in the cycle.
