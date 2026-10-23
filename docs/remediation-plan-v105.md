# Remediation Plan v105 — the re-run cycle's next-oldest candidate (the v99-era LOGIN + CALCULATOR pair's seventh re-run) + the axe watch + the 99th standing checks + the login auth-mode action row census pin (PIN-ONLY)

The formal narrative: `docs/session_254.md`→`docs/session_255.md`/`docs/session_256.md` (the v104 cycle's own narrative + ship records). The queue: the v104 plan's v105 suggestion — **the ledger-verified target** (the v104-era docs' suggestion AGREEING with the rotation ledger: the v99-era LOGIN + CALCULATOR pair [the CALCULATOR dialog + the /login view at desktop 1280x800], last re-shot v99 — now the oldest remaining [v99 < v100 < v101 < v102 < v103 < v104]; the pair's SEVENTH re-run bracket [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105] — the TWENTY-EIGHTH consecutive queue/ledger agreement), plus the axe-core watch at its re-check point and the 99th standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 308.**

## The pre-execution ledger verification (the queue-prose verification lesson, applied)

The rotation ledger's authority is the PROBE LINEAGE, never the prose
queue phrasing. Verified against `scripts/parity-probes/vlm-shots-v99.sh`
before the derivation: its own header reads "the v93-era LOGIN +
CALCULATOR pair, last re-shot v93, now the oldest remaining [v93 < v94 <
v95 < v96 < v97 < v98]; the pair's SIXTH re-run [v59 → v66 → v75 → v81 →
v87 → v93 → v99]" — matching the queue's phrasing (the v99-era surface
names confirmed: the CALCULATOR dialog + the /login view at desktop
1280x800). The SEVENTH re-run bracket [v59 → v66 → v75 → v81 → v87 → v93
→ v99 → v105] constructed from the same header's SIXTH bracket. The
standing-checks pair (ref-standing-v99.sh + standing-checks-v99.sh)
derived from v98 across the THREE token families (v98→v99, 98th→99th,
ref98→ref99/clone98→clone99), version-bump-only verified by normalizing
back and diffing clean (zero old tokens remaining — the persisted
derive-standing-v105.py, both halves bash -n clean).

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items
/ 3 assets / 2 liabilities) before any flow ran (the `env -u DATABASE_URL`
discipline); lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓
(robots + sitemap prerendered) · **306 e2e ✓** (126 + 90 + 57 + 37 chunk
executions across four disjoint file splits of the 23 spec files + the
setup project = 310 total = 307 unique tests [306 spec + 1 setup] — the
exact documented v104 state [305 spec + the v104 pin + 1 setup], the
count first derived authoritatively via `playwright test --list` and the
per-file counts summed against the authoritative total before any chunk
ran — the v103 chunk-split self-audit lesson applied; zero flakes on the
FIRST run) · 35/35 smoke ✓. The workspace: the FRESH-CLONE class (the
sandbox reset — the v86/v88/v90/v91/v92/v98/v100/v101/v103/v104
precedent): the environment re-provisioned from scratch (npm install;
`.env` written [DATABASE_URL="file:../db/custom.db"]; `db/` at the repo
root + db:generate + db:push + db:seed; chromium-1243 installed for the
pinned @playwright/test 1.63.0; the tool-results dir re-created for
with-server.sh). The two commits since the v104 parity push (55c2c04 +
50423c0) audited session-log/skills-sync-only [docs/session_255.md +
docs/session_256.md + the out-of-band `skills/` refresh — ZERO src/ or
lockfile deltas].

The codebase audit clean: the production seams re-audited — auth
(scrypt/HMAC + timingSafeEqual), the db-path contract (db-path.ts + its
unit test), the SEO pair (robots.ts allow-all + sitemap.ts 5-URL
structure — both prerendered by the build), the Tailwind v4 mitigations
(`@variant hover (&:hover)` + `@variant group-hover` + the toast
pointer-events fix), the three test tiers; skills/ excluded throughout
(the eslint ignores + the tsconfig exclude verified live).

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (dist-tags: rc/next sha
prereleases only beyond — no stable 4.14.1, no 5.x exists); the installed
wrapper 4.14.0 + the engine 4.14.0; the lockfile holding the v68 dedupe
state (exactly one `node_modules/axe-core` entry); the engine-contract
pin GREEN standalone (2 passed).

### F2 — the 99th standing checks: ALL GREEN (version-bumped from v98 — version-bump-only diffs verified)

ref-standing-v99.sh + standing-checks-v99.sh (version-bumped from v98
via the persisted derive-standing-v105.py across the THREE token
families [v98→v99, 98th→99th, AND the bare session names ref98→ref99/
clone98→clone99]; after normalizing back the files are version-bump-only:
diffed clean, zero old tokens remaining). Reference side: the four bugs
ALL live [toast-blocker `hitIsBurgerChild:false`; sheet-trap
`overlayCount:1` after nav; no-landmark `navLandmark:false`; the 464px
/networth overflow at 390 measured docSW 464 directly]; the data census
UNCHANGED on the FIRST read (networth "1 items · $25,000" / income "1
items · $5000.00" / expenses "4 items · $525.00" — no render-race this
cycle); the SEO pair live. Clone side: R1–R4 ALL GREEN — **the mobile
menu VERIFIED WORKING the 99th consecutive time**
(`hitIsBurgerChild: true`, the sheet opens, closes on nav, the nav
landmark present — the Tailwind v4 mitigation holds), zero overflow at
390 on all five views, the SEO pair live. The seedcheck exact after the
clone half (the reaping budget between the halves).

### F3 — the re-run pair (the v99-lineage derivation, the two-half census form)

The probe series derived from the v99 lineage (derive-v105-series.py,
persisted): vlm-shots-v105.sh + login-shots-v105.sh +
clone-vlmshots-v105.sh + clone-login-shots-v105.sh +
vlm-compare-v105.mjs + arbit-v105.sh — the generic swaps (refvlm99→
refvlm105, clonevlm99→clonevlm105, reflogin99→reflogin105,
clonelogin99→clonelogin105, refcalc99→refcalc105, clonecalc99→
clonecalc105, /tmp/vlm99→/tmp/vlm105, v99→v105) followed by the
exact-fragment history corrections (last-re-shot v93→v99, the era marker
v93-era→v99-era, SIXTH→SEVENTH, the re-run bracket extension [v59 → v66
→ v75 → v81 → v87 → v93 → v99 → v105], the oldest-remaining list bumped
to the current era [v99 < v100 < v101 < v102 < v103 < v104], the plan
attribution v98→v104, and the agreement count TWENTY-SECOND→
TWENTY-EIGHTH) — every correction verified applied (the derive script
reports each hit/miss; zero misses this cycle; the line-count-preservation
check green on all six files — the two-half builder inherits the v99 line
boundaries). bash -n + node --check clean on all six; zero residual old
tokens (the legitimate v45/v49/v55/v59/v66/v73/v87 pin-provenance, the
v43/v46/v64 rule, the v7 G2, and the seedcheck-v68 lineage tokens
whitelisted by context). The census BUILT two-half from the start
(build-twohalf-v105.py — ref-arbit-v105.sh + clone-arbit-v105.sh, the TWO
census JS blocks [CALC_CENSUS_JS 61 lines + LOGIN_CENSUS_JS 36 lines]
byte-identical across the halves — the md5 line-block contracts
[e1092d12 / 9e5a52d2 — the v99 census blocks verbatim]; the boundary
assertions green). The reaping budget applied as the standing step between
halves. Login on the first attempt both sides; the parked pointer at
(5,5); read-only — the v46 rule holds (the clone side's "Contents
Insurance" line-item pairing + full restore verified: delete + confirm +
restore $1850 + "3 items · $2235.00" re-read + the seedcheck exact).

The VLM pairwise verdicts: **the CALCULATOR pair DIFFERENT (the pair's
documented verdict class), the LOGIN pair IDENTICAL** — every calculator
flag DOM-arbitrated to a documented class:

1. The "Total Calculated Card: the clone includes the '• Will update
   category total' line" — the **SEED-DATA class** (the census proving
   the reference's `hasWillUpdateSpan: false` vs the clone's `true`: the
   reference's OWN Rent is $25.00 — its calculated total EQUALS the saved
   amount so the note stays hidden; the clone's Rent $1850 vs the
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
3. The "Amount Alignment" flag — the consequence of flag 2 (the row's
   chrome byte-identical: {720×102, pad 16px, radius 12px, borderTop 1px
   rgb(229,231,227)}).

The LOGIN pair's IDENTICAL verdict with the "Edit with Base44" FAB noted
as an external tool overlay — the unflagged platform-chrome form (the
v104-documented THIRD form; no arbitration needed for an unflagged
family). The CALC census's `close` key present on the clone side only —
the v99-documented finder artifact (the reference's close button matches
neither the aria-label nor the ×/x text pattern; the v87 pin holds the
close-button chrome via its own geometric finder, byte-identical).

The both-sides census **REPRODUCES the v99 census values EXACTLY — zero
drift on every axis**:

- **The LOGIN view**: {card 448 / radius 16px / bg rgba(255,255,255,0.95);
  h1 30px/700/rgb(15,23,42)/lh 36px; subtitle 16px/rgb(100,116,139);
  logo 96×96 + alt; email + pw inputs h 48 / radius 12px / border 1px
  rgb(226,232,240) / fs 14px + the placeholders; signIn 368×48 /
  radius 12px / bg rgb(15,23,42) / white / 14px/500; hasGoogle true;
  hasORDivider true; docSW 1280} — byte-identical (the login shadow's
  zero-layer lead count the documented v3/v4 construct classes; the
  VISIBLE layer rgba(0,0,0,0.25) 0px 25px 50px -12px the contract — the
  v45 F4 pin holds it).
- **The CALCULATOR dialog**: {panel 768×393 / radius 16px / maxW 768px /
  bg white + the shadow's visible layer; scrim rgba(26,58,46,0.5) /
  blur(8px) / 1280×800; title 18px/700/rgb(26,58,46)/lh 28px; desc
  14px/rgb(107,114,128)/lh 20px; totalCard 720×90 / pad 16px / radius
  12px / border 1px solid rgb(252,221,213); nameH4 16px/600/
  rgb(26,58,46)/h 24/mb 4px; row 720×102 / pad 16px / radius 12px /
  borderTop 1px rgb(229,231,227); pillRow flex/8px/12px/h 20; pill1
  20×65/2px 8px/9999px/12px/400; amountP 20px/700/rgb(224,122,59)/h 28;
  actionsAtRest opacity 0 + btnCount 2; addBtn 110×32/6px/12px/500/
  white; docSW 1280} — byte-identical.

**NO NEW CLONE GAP — the v105 iteration PIN-ONLY.**

### F4 [PIN] — the login's AUTH-MODE ACTION ROW census at 1280: the flex row + the forgot context + the signup-side button + the "Sign up" emphasis span (PIN-ONLY for src/ — no production-code change; +1 e2e = 308)

The never-pinned family (the FAMILY-EXTENSION pattern — the login card's
bottom action row, never census'd as a whole): the v7 G2 pin holds the
forgot-side button's {fs, lh, h, color} ONLY (login-parity.spec.ts:23);
the signup-side button ("Need an account? Sign up") is CLICKED in 8+
tests but its computed chrome is NEVER asserted; the inner "Sign up"
emphasis span (font-medium text-[#334155]) is never asserted in ANY spec
at ANY viewport; the ROW's flex chrome (display/align/justify/gap — the
`flex flex-col items-center justify-between gap-2 sm:flex-row sm:gap-0`
family) is never pinned (the coverage-map grep across all 23 spec files:
zero "Need an account" chrome assertions outside getByRole clicks; zero
action-row flex assertions in the login specs; the dashboard/items
"actionRow" hits are DIFFERENT elements — the quick-action row + the
expense-card action row).

**The pin's own axes first measured byte-identical on BOTH sides** by
the one-shot both-sides DOM census (moderow-arbit-v105.sh — the
base44-fab/brand/userfooter one-shot pattern applied to the family; the
census JS defined ONCE and eval'd on both sides, byte-identical by
construction; both sides the LOGGED-OUT /login surface — passive
navigation only, no session, no credentials — the v46 rule trivially
holds; the parked pointer at (5,5)):

- The ROW: {display flex, align center, justify space-between, gap 0px,
  w 368, h 20} — **byte-identical across sides** (the sm: breakpoint's
  flex-row/gap-0 state at 1280).
- The FORGOT button (the v7 context controls re-walked + the NEW fw
  axis): {text "Forgot password?", fs 14px, lh 20px, fw 500, color
  rgb(100,116,139), h 20} — **byte-identical across sides**.
- The SIGNUP button: {text "Need an account? Sign up", fs 14px, lh 20px,
  fw 400, color rgb(100,116,139), h 20} — **byte-identical across
  sides**.
- The "Sign up" emphasis SPAN: {text "Sign up", fs 14px, fw 500, color
  rgb(51,65,85)} — **byte-identical across sides**.

Every axis is DATA-INDEPENDENT (the structural chrome + the static copy
texts — no seed data touches any axis; the v98 data-independent-panel
strength class: the pin asserts the cross-side-verified values
directly).

**The pin** (tests/e2e/login-parity.spec.ts, appended as the v105
describe block): navigate to /login at 1280×800 → the row walk (the form
→ the "Forgot password?" button + the "Need an account?" button → their
common ancestor ROW [the walk-up-until-contains finder] → the span
[the signup button's span]) → assert the row {flex, center,
space-between, gap 0px, w 368, h 20} + the forgot {14px/20px/500/
rgb(100,116,139)/h 20 + text} + the signup {14px/20px/400/
rgb(100,116,139)/h 20 + text} + the span {"Sign up" 14px/500/
rgb(51,65,85)}.

**The pin-sanity mutation (the planned form)**: the span's
`font-medium` → `font-semibold` (src/components/budget/login-card.tsx:381,
by LINE NUMBER — the line carries EXACTLY ONE font-medium, grep-count
verified; the line-scoping keeps the LABEL_CLS's own font-medium at line
217 AND the forgot button's own at line 370 AND the verify-mode link's
own at line 668 untouched — the label chrome, the v7 forgot pin's axes,
and the verify-email flow ride those lines). Expected: the pin FAILS at
exactly the span.fw axis alone ("500" → "600"). Cascade-free: no other
spec asserts the action row / the signup button / the span's computed
chrome — this pin is the FIRST; the 8+ tests that CLICK the button use
getByRole name (the text unchanged by a font-weight change); the v75
census asserts the card {w/radius/bg} + signIn + h1 + inputs + logo —
none touch the span; the v7 pin's forgot axes live on a different
element (line-scoped away); font-weight moves no layout box (lh stays
20px, the row h stays 20 — the justify-between row's button x positions
may shift sub-pixel with the glyph advance, but no spec asserts them).
NOTE the v98 mutation-rebuild discipline: the mutation only bites after
the standalone REBUILD (the e2e runs the PREBUILT .next/standalone
server). Then restored (git diff src/ = 0 lines; the standalone REBUILD
via the FULL npm run build; the post-restore full file run green).

**The disproven-in-advance candidates (documented without execution):**
the signup button's `text-sm` → `text-base` mutation (fs 14→16 — moves
the button fs AND its lh AND the span's inherited fs — a three-axis
failure diff, violating the single-axis discipline); the row's
`sm:gap-0` removal (gap 0→2px AND the flex-col fallback at <640 —
two-viewport cascade); the span's `text-[#334155]` → `text-[#0f172a]`
mutation (single-axis [color] but weaker than the fw form: the fw
mutation exercises the emphasis-typography axis the family exists to
carry); the forgot button's `font-medium` → `font-normal` (line 370 —
bites the v7-adjacent fw context axis AND is the CONTEXT control, not
the pin's primary target).

## The ToDo list

| # | Step | Status |
|---|------|--------|
| 1 | F0 baseline chain on the fresh-clone workspace (seedcheck exact; lint/typecheck/108 unit/build ✓; 306 e2e zero flakes on the first run; 35/35 smoke) | DONE — all green |
| 2 | F1 axe-core watch | DONE — NO DRIFT |
| 3 | F2 99th standing checks (derived v98→v99, version-bump-only verified) | DONE — ALL GREEN (census clean on the first read) |
| 4 | F3 the v99-lineage probe derivation (generic swaps + exact-fragment history corrections + residual checks + line-count preservation; zero misses) | DONE |
| 5 | F3 two-half census builder (build-twohalf-v105.py, md5 contracts) + both halves executed (the reaping budget between halves) | DONE |
| 6 | F3 the VLM pairwise + the flag arbitration | DONE — CALCULATOR DIFFERENT (every flag DOM-arbitrated) + LOGIN IDENTICAL (the FAB the unflagged platform-chrome form); NO NEW GAP |
| 7 | F4 the supplemental auth-mode action row one-shot census (the pin's own axes measured byte-identical) | DONE |
| 8 | F4 THIS PLAN written + validated BEFORE the pin's execution | DONE |
| 9 | F4 append the v105 pin to tests/e2e/login-parity.spec.ts | DONE — appended (typecheck clean) |
| 10 | F4 pin first run (GREEN expected) | DONE — GREEN on the first run (31/31 in login-parity.spec.ts) |
| 11 | F4 pin-sanity mutation (login-card.tsx:381, line-number-scoped) → single-axis failure after the REBUILD → restore (git diff src/ = 0) → standalone REBUILD → post-restore full file run | DONE — ONLY the v105 pin red (30 green), the failure diff reads as span.fw "500"→"600" ALONE; restored (git diff src/ = 0); rebuilt; post-restore 31/31 green |
| 12 | F5 full chain re-run (lint/typecheck/108 unit/build/307→308 e2e/35 smoke) + the screenshots regeneration + byte-compare | DONE — all green; 308 e2e in four chunks (126+91+57+37 = 311 executions = 308 unique, zero flakes); the screenshots 9/16 byte-identical + SEVEN fresh-seed deltas arbitrated (see the F5 record) |
| 13 | D1–D7 docs alignment + session_257.md + the worklog Session 140 entry | DONE |
| 14 | ship: the full chain re-run + commit + SSH-wrapper push | DONE — the commit + the wrapper push executed + verified; the session-log follow-up pushed |

## The F5 screenshot arbitration record (the fresh-seed +2-day roll)

The regenerated set vs the committed (HEAD) set: **9/16 byte-identical +
SEVEN fresh-seed deltas, every one arbitrated, ZERO structural bands**
(diff-shots-v105.mjs + diff-shots-v105-bands.mjs +
diff-shots-v105-rows.mjs + crop-diff-v105.mjs + the pixel-delta
forensics):

- **The +2-day roll magnitude** (the v86/v80/v92 fresh-seed precedent
  family): the v104 committed set was seeded Oct 21 UTC; the v105
  regeneration seeded Oct 23 UTC (the cycle spans two UTC midnights) —
  every seeded isoDate offset shifts +2 days (the DB verified: Rent
  date 2026-10-14 vs the committed set's October 12).
- **03-income / 04-expenses / 05-savings**: the card date footers —
  crisp glyph-scale rolls (max delta 416, single 19px text-row bands at
  the date positions).
- **06-networth**: a single date digit roll (144 px, 12px-wide bbox,
  max delta 416).
- **07-add-item-modal**: the date input field's day digit (191 px, 22px
  band, max delta 735).
- **16-item-details band 2** (y1009-1032, 24px): the details sheet's own
  "Date" FactRow — "October 12, 2026" → "October 14, 2026", the glyph
  diff read directly (max delta 635, the "2"→"4" glyph maps).
- **16-item-details band 1 (y817-901) + 08-calculator (y817-900)**: the
  initially-suspicious 84-85px "bands" decompose to **±1-3 RGB rounding
  drift in the backdrop-blur(8px) scrim region** near the dialog panel
  edges (4167 + 1212 diff px, max delta 3 and 2 — NO glyphs, NO
  structural displacement; the ASCII luminance maps show the identical
  gradient structure; the GPU blur compositing's rounding varies between
  capture sessions). The crisp band-2 read + the five clean files carry
  the actual date rolls.
- The updated set committed (the v103 fresh-seed precedent).

## The pre-execution validation section (the measured evidence)

- The pin's measured values (the auth-mode action row one-shot census,
  this session): the row {display flex, align center, justify
  space-between, gap 0px, w 368, h 20} byte-identical; the forgot
  {"Forgot password?" 14px/20px/500/rgb(100,116,139)/h 20}
  byte-identical; the signup {"Need an account? Sign up" 14px/20px/400/
  rgb(100,116,139)/h 20} byte-identical; the span {"Sign up" 14px/500/
  rgb(51,65,85)} byte-identical — on BOTH sides at 1280.
- The mutation target line verified by reading the source:
  src/components/budget/login-card.tsx:381 — the "Sign up" span's opening
  tag carries EXACTLY ONE `font-medium` (grep-count 1 on the line); the
  LABEL_CLS's own `font-medium` at line 217, the forgot button's own at
  line 370, and the verify-mode link's own at line 668 — untouched by the
  line-number scoping.
- The coverage-map grep (run across ALL 23 spec files): zero "Need an
  account" chrome assertions outside getByRole click locators; zero
  login action-row flex assertions; zero signup-span computed-style
  assertions; the only forgot-button chrome the v7 {fs, lh, h, color}
  set — this pin is the FIRST on the row/signup/span axes.
- The rotation ledger verified: the LOGIN + CALCULATOR pair last re-shot
  v99 = the oldest remaining [v99 < v100 < v101 < v102 < v103 < v104] —
  the v104-era docs' v105 suggestion agreeing with the ledger (the
  TWENTY-EIGHTH consecutive agreement), the surface names verified
  against vlm-shots-v99.sh's own header before the derivation.

## Operational lessons this cycle (the probe README's D6 section)

- THE MODE-SWITCHER BUTTON CLASS (a finder note): the v105 login
  census's `links` array came back EMPTY on BOTH sides — the login's
  auth-mode switchers ("Forgot password?" / "Need an account? Sign up")
  are BUTTONS on both sides, not anchors; any future census that wants
  the mode-switcher family must find them among `form button` by text,
  never `a[href]`.
- THE UNFLAGGED-FAB FORM HOLDS (a VLM-arbitration note): the v105 LOGIN
  pairwise returned IDENTICAL while noting the "Edit with Base44" FAB as
  an external tool overlay in its data note — the v104-documented THIRD
  form (no flag at all) repeating; the family needs no arbitration.
- THE SPAN-FW MUTATION FORM (a pin-design note): the chosen mutation
  (`font-medium` → `font-semibold` on the emphasis span) moves fw ALONE —
  unlike the fs mutations of prior cycles (which drag lh and inherited
  fs with them), a font-weight change on a leaf span is single-axis BY
  CONSTRUCTION, the cleanest mutation form yet; future cycles prefer it
  when the family carries a fw axis.
- THE BLUR-ROUNDING DELTA CLASS (a screenshot-arbitration note): the
  backdrop-blur(8px) scrim regions can show ±1-3 RGB rounding drift
  between capture sessions (the GPU blur compositing's rounding) —
  localized near the dialog panel edges, glyph-free, structure-free.
  The v105 arbitration discipline: decompose every "wide band" by its
  MAX PER-PIXEL DELTA first — glyph rolls read d 400-700, rounding
  drift reads d <= 3; only the former are text changes. A wide band
  with d <= 3 and no ASCII-map structure is rounding noise, never a
  clone gap.

## The next queue (the v106 suggestion — verify against the rotation ledger before executing)

(1) the re-run cadence rotates to the next-oldest candidate after the
LOGIN + CALCULATOR pair (the v100-era DASHBOARD pair, last re-shot v100 —
now the oldest remaining [v100 < v101 < v102 < v103 < v104 < v105]; the
pair's re-run bracket to be verified against vlm-shots-v100.sh's own
header before the derivation), (2) the axe-core watch at its next
re-check point (only a 5.x wrapper changes the calculus), (3) the
deferred reference-write censuses (unchanged — out of bounds under the
v46 read-only rule).
