# Remediation Plan v99 — the re-run cycle's next-oldest candidate (the v93-era LOGIN + CALCULATOR pair's sixth re-run) + the axe watch + the login social-row (OR divider + Google button) census pin (PIN-ONLY)

The formal narrative: `docs/session_236.md` (the v98 cycle's own narrative
log). The queue: the v98 plan's v99 suggestion — **the ledger-verified
target** (the v98-era docs' suggestion AGREEING with the rotation ledger:
the v93-era LOGIN + CALCULATOR pair [the login view + the calculator
dialog at desktop 1280x800], last re-shot v93 — now the oldest remaining
[v93 < v94 < v95 < v96 < v97 < v98]; the pair's SIXTH re-run
[v59 → v66 → v75 → v81 → v87 → v93 → v99] — the TWENTY-SECOND consecutive
queue/ledger agreement), plus the axe-core watch at its re-check point
and the 93rd standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 302.**

## The pre-execution ledger verification (the queue-prose verification lesson, applied)

The rotation ledger's authority is the PROBE LINEAGE, never the prose
queue phrasing. Verified against `scripts/parity-probes/vlm-shots-v93.sh`
before the derivation: its own header reads "the v87-era LOGIN +
CALCULATOR pair, last re-shot v87, now the oldest remaining [v87 < v88 <
v89 < v90 < v91 < v92]; the v92 plan's v93 queue suggestion, agreeing
with the rotation ledger — the SIXTEENTH consecutive agreement; the
pair's FIFTH re-run [v59 → v66 → v75 → v81 → v87 → v93]" — matching the
queue's phrasing exactly (no transcription error; the v93-era surface
names confirmed: the LOGIN view + the CALCULATOR dialog at desktop
1280x800). The SIXTH re-run bracket [v59 → v66 → v75 → v81 → v87 → v93 →
v99] constructed from the same header's FIFTH bracket. The
standing-checks pair (ref-standing-v93.sh + standing-checks-v93.sh)
derived from v92 across the THREE token families (v92→v93, 92nd→93rd,
ref92→ref93/clone92→clone93), version-bump-only verified by normalizing
back and diffing clean (zero old tokens remaining — the persisted
derive-standing-v99.py, both halves bash -n clean).

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items
/ 3 assets / 2 liabilities) before any flow ran; lint ✓ · typecheck ✓ ·
108/108 unit ✓ · `npm run build` ✓ (robots + sitemap prerendered) ·
**301 e2e ✓** (114 + 99 + 90 chunk executions across three chunk splits
of the 23 spec files + the setup project = 303 total = 301 unique tests —
the exact documented v98 state; ONE first-run timing flake in the
not-found.spec.ts head-parity test [the 15-file chunk's tail] — clean on
the immediate single-spec re-run AND the full-chunk re-run, the
documented v96-era timing-artifact class; the chunk re-run 90/90 green)
· 35/35 smoke ✓. The workspace: the CARRIED-OVER class (pulled to
main @ 74a206e; the two commits since the v98 push 08cc3cf [7939458 +
74a206e] verified session-log-only [docs/session_237.md +
docs/session_238.md — ZERO src/ or lockfile deltas], so the v98 cycle's
own fresh-clone environment carries over unchanged, no re-provisioning;
npm install 354 packages already present; `.env` verified
[DATABASE_URL="file:../db/custom.db"]; `db/` at the repo root; the
sandbox's polluted parent DATABASE_URL re-confirming the env -u
discipline).

The codebase audit clean: the production seams re-audited — auth
(scrypt/HMAC), the db-path contract (db-path.ts + its unit test), the
SEO pair (robots.ts allow-all + sitemap.ts 5-URL structure — both
prerendered by the build), the Tailwind v4 mitigations
(`@variant hover (&:hover)` + the toast pointer-events fix), the three
test tiers; skills/ excluded throughout (the eslint ignores + the
tsconfig exclude verified live).

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (dist-tags: rc/next sha
prereleases only beyond — no stable 4.14.1, no 5.x exists); the
installed wrapper 4.14.0 + the engine 4.14.0; the lockfile holding the
v68 dedupe state (exactly one `node_modules/axe-core` entry); the
engine-contract pin GREEN standalone (2 passed).

### F2 — the 93rd standing checks: ALL GREEN (version-bumped from v92 — version-bump-only diffs verified)

ref-standing-v93.sh + standing-checks-v93.sh (version-bumped from v92
via the persisted derive-standing-v99.py across the THREE token families
[v92→v93, 92nd→93rd, AND the bare session names ref92→ref93/
clone92→clone93]; after normalizing back the files are version-bump-only:
diffed clean, zero old tokens remaining). Reference side: the four bugs
ALL live [toast-blocker `hitIsBurgerChild:false`; sheet-trap
`overlayCount:1` after nav; no-landmark `navLandmark:false`; the 464px
/networth overflow at 390 measured docSW 464 directly]; the data census
UNCHANGED on the first read (networth "1 items · $25,000" / income "1
items · $5000.00" / expenses "4 items · $525.00" — no render-race this
cycle); the SEO pair live. Clone side: R1–R4 ALL GREEN — **the mobile
menu VERIFIED WORKING the 93rd consecutive time**
(`hitIsBurgerChild: true`, the sheet opens, closes on nav, the nav
landmark present — the Tailwind v4 mitigation holds), zero overflow at
390 on all five views, the SEO pair live.

### F3 — the re-run pair (the v93-lineage derivation, the two-half census form)

The probe series derived from the v93 lineage (derive-v99-series.py,
persisted): vlm-shots-v99.sh + login-shots-v99.sh +
clone-vlmshots-v99.sh + clone-login-shots-v99.sh + vlm-compare-v99.mjs +
arbit-v99.sh — the generic swaps (v93→v99, refvlm93→refvlm99,
clonevlm93→clonevlm99, reflogin93→reflogin99, clonelogin93→clonelogin99,
refcalc93arbit→refcalc99arbit, clonecalc93arbit→clonecalc99arbit,
/tmp/vlm93→/tmp/vlm99) followed by the exact-fragment history
corrections (last-re-shot v87→v93, FIFTH→SIXTH, the re-run bracket
extension, the oldest-remaining bracket [v93 < v94 < v95 < v96 < v97 <
v98], the agreement ordinal SIXTEENTH→TWENTY-SECOND, the suggesting plan
v92→v98) — every correction verified applied (the derive script reports
each hit/miss; the ONE first-run MISS [the clone-login header's
"the re-run\n# cycle's" line break — the assumed form carried "the
re-run cycle's" unbroken] caught by the report itself and fixed before
any probe executed; the v96/v98 miss-report discipline). bash -n +
node --check clean on all six; zero residual old tokens (the legitimate
v87 pin-provenance token whitelisted by context). The census BUILT
two-half from the start (build-twohalf-v99.py — ref-arbit-v99.sh +
clone-arbit-v99.sh, the TWO census JS blocks [CALC_CENSUS_JS 61 lines +
LOGIN_CENSUS_JS 36 lines] extracted once and embedded byte-identically
across the halves — the md5 line-block contract [e1092d12 / 9e5a52d2]).
The reaping budget applied as the standing step between every half.
Login on the first attempt both sides; the parked pointer at (5,5);
read-only — the v46 rule holds (the clone side's "Contents Insurance"
line-item pairing + full restore verified: delete + confirm + restore
$1850 + "3 items · $2235.00" re-read + the seedcheck exact).

**The verdicts: the CALCULATOR pair DIFFERENT (the documented re-run
class), the LOGIN pair IDENTICAL — every calculator flag
DOM-arbitrated to a documented class:**

1. The "Total Calculated Card: the clone includes the '• Will update
   category total' line" — the **SEED-DATA class** (the census proving
   the reference's `hasWillUpdateSpan: false` vs the clone's `true`: the
   reference's OWN Rent is $25.00 — its calculated total EQUALS the
   saved amount so the note stays hidden; the clone's Rent $1850 vs the
   recalculated $25.00 shows the note. The v73-documented
   DATA-CONDITIONAL class, re-proven byte-identical chrome: the
   totalCard {720×90, pad 16px, radius 12px, border 1px solid
   rgb(252,221,213)} IDENTICAL on both sides).
2. The "reference row in active/hover state showing edit/delete; the
   clone's resting row hides them" — the **RESTING-STATE parity class**
   (the census's `actionsAtRest` {opacity 0, btnCount 2} IDENTICAL on
   both sides — the reference's screenshot simply caught its row
   post-pointer; the VLM hover-state perception class, the v43 rule
   applied: the measurement is the authority).
3. The "row height / less populated right side" — the consequence of
   flag 2 (the row {720×102, pad 16px, radius 12px, borderTop 1px
   rgb(229,231,227)} byte-identical).

The both-sides census (the two-half controlled form) **REPRODUCES the
v87/v93 census values EXACTLY — zero drift on every axis**:

- **The LOGIN view**: {card 448 / radius 16px / bg rgba(255,255,255,0.95);
  h1 30px/700/rgb(15,23,42)/lh 36px; subtitle 16px/rgb(100,116,139);
  logo 96×96 + alt; email + pw inputs h 48 / radius 12px / border 1px
  rgb(226,232,240) / fs 14px + the placeholders; signIn 368×48 /
  radius 12px / bg rgb(15,23,42) / white / 14px/500; hasGoogle true;
  hasORDivider true; docSW 1280} — byte-identical (the login shadow's
  zero-layer lead count + the 0px-width border-color string the
  documented v3/v4 construct classes; the VISIBLE layer
  rgba(0,0,0,0.25) 0px 25px 50px -12px the contract — the v45 F4 pin
  holds it).
- **The CALCULATOR dialog**: {panel 768×393 / radius 16px / maxW 768px /
  bg white + the shadow's visible layer; scrim rgba(26,58,46,0.5) /
  blur(8px) / 1280×800; title 18px/700/rgb(26,58,46)/lh 28px; desc
  14px/rgb(107,114,128)/lh 20px; totalCard 720×90 / pad 16px / radius
  12px / border 1px solid rgb(252,221,213); nameH4 16px/600/
  rgb(26,58,46)/h 24/mb 4px; row 720×102 / pad 16px / radius 12px /
  borderTop 1px rgb(229,231,227) / bg white; pillRow flex/8px/12px/h 20;
  pill1 h 20/w 65/pad 2px 8px/radius 9999px/12px/400; amountP
  20px/700/rgb(224,122,59)/h 28; actionsAtRest opacity 0/btnCount 2;
  addBtn 110×32/radius 6px/12px/500/white; docSW 1280} — byte-identical.
- **The census's own finder artifact, arbitrated this cycle (the v98
  unlabelled-trigger class EXTENDED)**: the LOGIN half's JS finder for
  the calculator close button (aria-label/text pattern) matched the
  CLONE's labelled Radix button but NOT the reference's TEXTLESS SVG
  button — the supplemental geometric probe (closebtn-arbit-v99.sh,
  persisted: the header-band button census with the full pointer-event
  sequence per the v98 lesson) reads the reference's close button
  {36×36, radius 6px, bg rgba(0,0,0,0), border 0px, svg 1} —
  **byte-identical to the clone's census `close` field** (the 0px-width
  border-color string the inert construct class). The finder's miss is
  the DOCUMENTED unlabelled-trigger class, not a surface difference.

**NO NEW CLONE GAP — the v99 iteration PIN-ONLY.**

### F4 [PIN] — the login card's SOCIAL-LOGIN ROW census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 302)

The never-pinned family (the FAMILY-EXTENSION pattern — the v97
missing-middle lesson applied to the LOGIN surface's social row): the
login card's OR-divider + Google-button block. The v75 F4 pin walked
the card/h1/subtitle/inputs/signIn/logo; the v7 G3 pin holds the Google
button's COLORS (text/border/bg) and the v45 F4 pin its HOVER
shadow-sm; the auth.spec pins hold the OR divider's PRESENCE per state
(booleans only) — **the OR divider's computed chrome (the "or" text's
typography + tracking + padding + the rule line's height/bg/width) and
the Google button's GEOMETRY/typography (w/h/radius/fs/lh/pad/gap +
the svg glyph size) are NEVER pinned at ANY viewport in ANY spec** (the
coverage-map grep across all 24 specs: zero specs assert any Google
button radius or geometry; zero specs assert any OR-divider computed
style — the only "divider" assertions in the suite are the auth.spec
presence booleans and unrelated dashboard/networth dividers).

**The pin's own axes first measured byte-identical on BOTH sides** by
the supplemental two-half census (social-arbit-v99.sh +
social-clone-v99.sh — BUILT two-half from the start via
build-social-v99.py, the census JS byte-identical by the md5
line-block contract [d7add89b — 32 lines]; both sides READ-ONLY passive
navigation — the logged-out /login surface needs no session, the v46
rule holds trivially; the seedcheck exact after the clone half):

- The GOOGLE button: {w 368, h 54, radius 12px, fs 16px, fw 500, lh
  24px, color rgb(51,65,85), bg rgb(255,255,255), border 1px
  rgb(226,232,240), pad 14px 20px, gap 12px, display flex, svg 20×20} —
  **byte-identical across sides** (the w-full content row [448 − 2×40
  md:px-10 = 368] + the py-3.5/px-5 + text-[16px]/font-medium family).
- The OR text: {fs 12px, fw 500, color rgb(100,116,139), lh 16px, tt
  uppercase, ls 0.6px, pad 0px 12px, bg rgb(255,255,255), h 16, w 43} —
  **byte-identical across sides** (the text-xs uppercase font-medium
  tracking-wider px-3 family over the white card).
- The RULE line: exactly ONE hairline per card {h 1px, bg
  rgb(226,232,240), w 368} — the chrome byte-identical; the element TAG
  differs (reference DIV vs clone SPAN — the inert construct class; the
  pin asserts the chrome + count, never the tag).
- The RHYTHM: the OR-text center 32px below the Google button's bottom
  (the my-6 24px margin + the 16px text row's half) — byte-identical;
  the signInToGoogle axis −358 on BOTH sides (the social block renders
  ABOVE the form on both sites — the order itself parity-correct).
- The docSW 1280 guard on both sides.

**The pin** (tests/e2e/login-parity.spec.ts, appended as the v99
describe block): navigate to /login at 1280×800 → the census walk (the
card from the form, the Google button by text, the OR leaf by /^or$/i,
the hairline rules ≤2px) → asserts the full social-row family above +
the docSW 1280 guard. Every axis is DATA-INDEPENDENT (the logged-out
static surface — no seed data touches it) — the census values assert
directly, the v98 data-independent-panel strength class.

**The pin-sanity mutation (the planned form)**: the Google button's
`rounded-xl` → `rounded-lg` (src/components/budget/login-card.tsx:172,
by LINE NUMBER — the line carries EXACTLY ONE rounded-xl, grep-count
verified). Expected: the pin FAILS at exactly the google radius axis
alone (`12px` → `8px`); cascade-free BY CONSTRUCTION (border-radius
never changes the layout box — w/h/pad/gap/fs/lh/color/bg/border stay;
the rhythm axes measure box edges, not corners; no other spec asserts
the Google button's radius — this pin is the first; the LINE-NUMBER
scoping keeps every other rounded-xl in the file — the inputs' own
rounded-xl at the INPUT_CLS constant, the card's rounded-2xl —
untouched). NOTE the v98 mutation-rebuild discipline: the mutation only
bites after the standalone REBUILD (the e2e runs the PREBUILT
.next/standalone server). Then restored (git diff src/ = 0 lines; the
standalone REBUILD via the FULL npm run build; the post-restore full
file run green).

**The disproven-in-advance candidates (documented without execution):**
the py-3.5 → py-4 mutation (pad 14px→16px AND h 54→58 AND the
googleToOr rhythm 32→30 — a three-axis failure, not the clean
single-axis form); the text-xs → text-sm mutation on the OR text (fs
12→14 AND lh 16→20 AND h 16→20 AND w 43→~49 — four axes); the
tracking-wider → tracking-wide mutation (ls 0.6→0.25 AND w — two
axes); the font-medium → font-normal mutation (fw AND possibly w — the
bold/regular glyph widths differ).

## The ToDo list

| # | Step | Status |
|---|------|--------|
| 1 | F0 baseline chain on the carried-over workspace (seedcheck exact; lint/typecheck/108 unit/build ✓; 301 e2e — one documented-class flake, re-runs clean; 35/35 smoke) | DONE — all green |
| 2 | F1 axe-core watch | DONE — NO DRIFT |
| 3 | F2 93rd standing checks (derived v92→v93, version-bump-only verified) | DONE — ALL GREEN (census clean on the first read) |
| 4 | F3 the v93-lineage probe derivation (generic swaps + exact-fragment history corrections + residual checks; the one MISS caught by the report) | DONE |
| 5 | F3 two-half census builder (build-twohalf-v99.py, md5 contract) + both halves executed | DONE |
| 6 | F3 the VLM pairwise | DONE — calculator DIFFERENT (all flags arbitrated), login IDENTICAL |
| 7 | F3 the close-button finder artifact arbitrated geometrically (closebtn-arbit-v99.sh) | DONE — byte-identical |
| 8 | F4 the supplemental social-row two-half census (the pin's own axes measured byte-identical) | DONE |
| 9 | F4 THIS PLAN written + validated BEFORE the pin's execution | DONE |
| 10 | F4 append the v99 pin to tests/e2e/login-parity.spec.ts | PENDING |
| 11 | F4 pin first run (GREEN expected) | PENDING |
| 12 | F4 pin-sanity mutation (login-card.tsx:172, line-number-scoped) → single-axis failure after the REBUILD → restore (git diff src/ = 0) → standalone REBUILD → post-restore full file run | PENDING |
| 13 | F5 full chain re-run (lint/typecheck/108 unit/build/302 e2e/35 smoke) + the screenshots regeneration + byte-compare | PENDING |
| 14 | D1–D7 docs alignment + session_239.md + the worklog Session 134 entry | PENDING |
| 15 | ship: the full chain re-run + commit + SSH-wrapper push | PENDING |

## The pre-execution validation section (the measured evidence)

- The pin's measured values (the social-row two-half census, this
  session): google {w 368, h 54, radius 12px, fs 16px, fw 500, lh 24px,
  color rgb(51,65,85), bg rgb(255,255,255), border 1px rgb(226,232,240),
  pad 14px 20px, gap 12px, display flex, svgW 20, svgH 20} byte-identical;
  orText {fs 12px, fw 500, color rgb(100,116,139), lh 16px, tt uppercase,
  ls 0.6px, pad 0px 12px, bg rgb(255,255,255), h 16, w 43} byte-identical;
  rules exactly 1 × {h 1px, bg rgb(226,232,240), w 368} byte-identical
  (the tag DIV-vs-SPAN the inert construct class); rhythm {googleToOr
  32, signInToGoogle −358} byte-identical; docSW 1280 both sides; the
  seedcheck exact after the clone half.
- The mutation target line verified by reading the source:
  src/components/budget/login-card.tsx:172 — the Google button's
  className carries EXACTLY ONE `rounded-xl` (grep-count 1 on the line);
  the OR divider's own chrome (login-card.tsx:182-195) and the
  INPUT_CLS rounded-xl constant sit at DIFFERENT lines — untouched by
  the line-number scoping.
- The coverage-map grep (run across ALL 24 specs): zero specs assert
  the Google button's radius or geometry (the v7 G3 pin holds
  color/border-color/bg; the v45 F4 pin the hover shadow); zero specs
  assert ANY OR-divider computed style (the auth.spec hasOrDivider
  booleans are presence-only) — this pin is the FIRST on the family.
- The rotation ledger verified: the login + calculator pair last
  re-shot v93 = the oldest remaining [v93 < v94 < v95 < v96 < v97 <
  v98] — the v98-era docs' v99 suggestion agreeing with the ledger (the
  TWENTY-SECOND consecutive agreement), the surface names verified
  against vlm-shots-v93.sh's own header before the derivation.
- The pin's finder: the Google button via text (/Continue with
  Google/i — labelled on BOTH sides, unlike the v98 action trigger);
  the OR text via the leaf-element /^or$/i finder (proven stable across
  the census halves); the rules via the geometric hairline scan
  (≤2px tall, >150px wide, non-transparent bg — exactly 1 match per
  card on both sides).

## Operational lessons this cycle (the probe README's D6 section)

- THE UNLABELLED-TRIGGER FINDER CLASS, EXTENDED (the v98 lesson's
  second sighting): the two-half census's OWN close-button finder
  (aria-label/text) missed the reference's TEXTLESS SVG close button —
  the supplemental GEOMETRIC probe (header-band button census) is the
  arbitration form; any future census finder for reference-side chrome
  must be geometric or labelled-on-both-sides from the start.
- THE SOCIAL-BLOCK-ABOVE-THE-FORM ORDER (a measurement-note): the
  reference's login card renders the Google + OR block ABOVE the
  email/password form (signInToGoogle −358 on BOTH sides) — the
  clone's GoogleBlock-before-AuthForm order is the parity-correct one
  (login-card.tsx:583-584); the rhythm axes' sign is the tell.
- THE CENSUS-TAG CONSTRUCT CLASS (a pin-strength note): the OR rule
  renders as DIV on the reference and SPAN on the clone with
  byte-identical chrome — pins on such elements assert the COMPUTED
  chrome + the geometric count, never the tag name.

## The next queue (the v100 suggestion — verify against the rotation ledger before executing)

(1) the re-run cadence rotates to the next-oldest candidate after the
login + calculator pair (the v94-era NETWORTH + DRILL-DOWN pair [the
networth view + the dashboard drill-down EXPANDED state, both desktop
1280x800 full-page], last re-shot v94 — now the oldest remaining
[v94 < v95 < v96 < v97 < v98 < v99]; the pair's SIXTH re-run bracket
[v60 → v67 → v76 → v82 → v88 → v94 → v100] to be verified against
vlm-shots-v94.sh's own header before the derivation), (2) the axe-core
watch at its next re-check point (only a 5.x wrapper changes the
calculus), (3) the deferred reference-write censuses (unchanged — out
of bounds under the v46 read-only rule).
