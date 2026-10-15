# Remediation Plan v62 — the reference-side a11y surface re-audit (NO
# DRIFT since v38) + the mobile header-subtitle 390 census pin + the SKILL
# doc's stale count-line sweep

Date: 2026-10-15 · Scope: the session-147 v62 queue's first TWO items —
"the reference-side a11y surface re-audit (has the reference's own axe
tree drifted since v38?)" and "a sweep of the SKILL doc's stale count
lines (177, 474, 1191, 1255 — pre-existing doc drift flagged by the v61
doc digest)" — plus the 56th standing checks and the standing VLM pair
(the dashboard full-page at BOTH 1280x800 AND — new this session —
390x844, the mobile pair the user directive emphasizes). All
READ-ONLY on the reference (the v46 rule). Measured live on BOTH sites
via the v62 family: axe-detail-ref-v62.mjs (the reference's axe tree,
the full a11y.spec.ts surface: six authed routes at 1280 + the 404 +
the logged-out login + the mobile 390 sheet-open state),
vlm-shots-v62.sh + clone-vlmshots-v62.sh + vlm-compare-v62.mjs (the
TWO-pair VLM program), arbit-v62.sh + arbit2-v62.sh (the two
unclassified-flag DOM arbitrations), ref-standing-v56.sh +
standing-checks-v56.sh (the 56th round, version-bumped from v55).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · 263 e2e ✓ (95 + 94 + 76,
three ordered chunks, zero failures — the fresh-sandbox caveat: the
Playwright browsers must be installed first, `npx playwright install
chromium`) · 35/35 smoke ✓. The v61 pins verified present
(dashboard.spec.ts: the F2 guidelines census @2643 + the F3 quick-action
census @2757). The dev DB re-seeded to the exact seed state (7 budget
items / 3 assets / 2 liabilities).

## The v62 sweep — what the measurement found

### The 56th standing checks — ALL GREEN

- **Reference side**: the four bugs ALL still live — the toast-blocker
  (`hitIsBurgerChild:false`, the burger's center hit intercepted by
  `DIV.fixed top-0 z-[100]`), the sheet-trap (the overlay remains after
  the nav click, `overlayCount:1`), the no-landmark
  (`navLandmark:false`), the 464px `/networth` overflow at 390. The
  data census UNCHANGED (the 56th consecutive clean drift check: "1
  items · $25,000" networth / "1 items · $5000.00" income /
  "4 items · $525.00" expenses). The SEO pair live (robots + sitemap
  200).
- **Clone side**: R1 the burger hit-test TRUE + the sheet opens (288px,
  5 links) · R2 the sheet CLOSES + navigates (`sheetGone:true,
  overlayGone:true` on /income) · R3 the nav landmark present · R4 ZERO
  overflow at 390 on all five views (docSW 390 each) · the SEO pair
  live. **The mobile navigation menu VERIFIED WORKING — the 56th
  consecutive time.**

### F1 [AUDIT] — the reference's a11y tree: NO DRIFT since v38

The full-surface re-scan (axe-core 4.13 via @axe-core/playwright, the
same tags `wcag2a/wcag2aa/wcag21a/wcag21aa`) measured the LIVE
reference and compared it against the v38 contract pinned in
`tests/e2e/a11y.spec.ts`:

- **The logged-out login page: 0 violations** — matches the v38 record
  (the zero-violation surface, both sites).
- **The structural families: IDENTICAL** — the reference still fails
  exactly `button-name` (10 nodes: its unlabeled Select triggers +
  card kebabs, across /income /expenses /savings /networth) and
  `svg-img-alt` (6 nodes: its recharts donut sectors `path[name=…]`, on
  / and /dashboard) — the two families the clone deliberately fixes
  (GATE 1's superset contrast). No new family appeared; neither family
  was fixed on the reference.
- **The contrast palette: IDENTICAL to the v38 7-color set** —
  rgb(143, 188, 63) lime, rgb(59, 126, 161) blue, rgb(224, 122, 59)
  orange, rgb(245, 169, 98) orangeLight, rgb(107, 114, 128) gray-500,
  rgb(203, 213, 225) #cbd5e1 (the 404 h1), rgb(115, 115, 115) zinc-500
  (the networth inactive Liabilities tab). NO new low-contrast color
  entered the reference's design → the clone's GATE 2 allow-list
  (PARITY_PALETTE) needs NO change.
- **The mobile 390 sheet-open state: color-contrast only** (14 nodes,
  the same palette) — no structural family in the open-sheet tree.

**VERDICT: the reference's axe tree has NOT drifted since v38.** The
clone's a11y.spec.ts contract (both gates) remains valid as pinned; no
code change required. The re-audit closes the v62 queue's top item.

### The TWO-pair VLM program — both pairs CLEAN (every flag arbitrated)

**Pair 1 — the dashboard full-page at 1280x800**: VERDICT DIFFERENT
with five flags, ALL arbitrated to documented classes:
1. the nav-highlight root-URL gap — the reference's own bug (its root
   `/` marks no active nav item) the clone's superset fix #3 highlights
   — the DOCUMENTED v60 class;
2. the avatar "U" vs "D" — the user-identity class;
3. the progress-bar length — the allocation DATA class (30.5% vs
   62.8%);
4. the donut labels — the VLM claimed the reference renders none;
   DOM-arbitrated (arbit-v62.sh): the reference renders THREE labels
   (92.3% / 4.6% / 3.1%), the clone three (81.6% / 13.8% / 4.6%) — a
   PERCEPTION ARTIFACT (the documented v60 class, re-confirmed live)
   + the values are the DATA class;
5. the "Edit with Base44" FAB — the platform-chrome class.

**Pair 2 — the dashboard full-page at 390x844 (NEW this session)**:
VERDICT DIFFERENT with two flags, BOTH arbitrated:
1. the Base44 tooltip overlay — platform chrome;
2. "the clone's header subtitle wraps to a third line" —
   DOM-arbitrated (arbit2-v62.sh, the leaf-text census on both sides):
   the reference P { w 363, h 48, top 121, 16px/400/rgb(107,114,128),
   lh 24px, 2 lines, parentH 92 } vs the clone P { w 358, h 48,
   top 121, 16px/400/rgb(107,114,128), lh 24px, 2 lines, parentH 92 } —
   **the wrap is IDENTICAL (2 lines, h 48, parentH 92, top 121)**; the
   5px width delta is the reference's own 395px docSW overflow (the
   R-bug-4 family — its content column renders 5px wider than the
   clone's overflow-free 390). A PERCEPTION ARTIFACT — the VLM
   fabricated the third line; the DOM census is the authority (the v61
   meta-lesson's inverse: this time the census ACQUITTED what the VLM
   convicted).

**No production-code parity gap found this session** — the pin-only
line holds from v61 (`git diff src/` stays empty).

### F2 [PIN] — the mobile header-subtitle block census at 390

The M2 arbitration measured a never-pinned surface: the dashboard
header block (h1 "Budget Dashboard" + the subtitle P) at 390x844. The
census, identical on both sides: the subtitle P { text "Track your
income, savings, and expenses to achieve net zero", h 48, 2 lines,
font 16px, weight 400, color rgb(107, 114, 128), line-height 24px } ·
the header block DIV { h 92 = h1 36 + mb-2 8 + p 48 } · top 121. The
existing pin (dashboard.spec.ts:26) covers the subtitle's VISIBILITY
at desktop only — the mobile wrap outcome (2 lines, the 48px height,
the 92px block) was never pinned. The F2 pin adds it to
`tests/e2e/dashboard.spec.ts` (PIN-ONLY — the surface is already
correct; TDD: GREEN first run expected).

### F3 [DOCS] — the SKILL doc's stale count lines

Four pre-existing stale lines in `zero-balance_SKILL.md` (flagged by
the v61 doc digest), all in CURRENT-state sections (bootstrap
verification, the clean-check gate, the decisions table, the file
inventory):
- line 177: "(214 tests)" → **263 tests**
- line 474: "223/223" → **263/263**
- line 1191: "Playwright e2e (223, desktop+mobile)" → **(263,
  desktop+mobile)**
- line 1255: "(22 files, 214 tests)" → **(23 files, 263 tests)**

(The historical session-log rows — v33's 166, v44's 214, v51's 241 —
are era-correct records and stay untouched.)

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F2 pin: the mobile header-subtitle census at 390 (GREEN first) | tests/e2e/dashboard.spec.ts |
| 2 | sanity | S1 mutation: the subtitle's lh 24px→28px (via inline style) must FAIL the pin; standalone rebuild; restore | src/components/budget/dashboard-view.tsx |
| 3 | docs | F3: the four stale count lines | zero-balance_SKILL.md |
| 4 | verify | the 16 screenshots regenerated + byte-compared (expect byte-identical — no production change) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v62 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md count/state bump | CLAUDE.md |
| 7 | docs | D3: README state + the v62 row | README.md |
| 8 | docs | D4: SKILL doc Session 97 row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.19 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v62 section | scripts/parity-probes/README.md |
| 11 | docs | D7: session_151.md + the repo worklog entry | docs/session_151.md + worklog.md |
| 12 | ship | the full chain re-run (lint → typecheck → 108 unit → build → 264 e2e → 35 smoke) + commit + SSH-wrapper push | — |

## Pre-execution validation (done before the plan's execution)

- The F2 pin's finder: the subtitle P is the h1's nextElementSibling
  inside the header DIV (`dashboard-view.tsx:927-934`) — walk
  `h1 → parentElement` (NOT closest — the v61 self-match trap), take
  the `p` child. The block DIV is the h1's parentElement (h 92). The
  existing pins are untouched: the desktop header test (line 20-35)
  asserts visibility only; the v51 F2/F4/F5 mobile census family
  (line 1921+) starts from the STAT CARDS — no subtitle overlap. The
  v44/v60 1280 censuses never touch the header block.
- The S1 mutation target: the subtitle P carries `style={{ color:
  rgb.gray }}` — a sibling inline style `lineHeight: "28px"` flips the
  measured lh AND the wrap arithmetic (48→56) — one mutation, two
  axes. The standalone rebuild must be its own command (the v53
  lesson).
- The chain gate: lint → typecheck → 108 unit → build → 263 e2e
  (**264** after: +1 — the F2 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every
  agent-browser run; the with-server boots fresh per command; the
  reference session EXPIRES between long eval gaps — re-login; the
  e2e chunks pass FULL file paths; each mutation's rebuild is a
  SEPARATE command.
- The deferred queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census, the line-items dialog
  glyphs. The reference's trending-down glyph stays data-conditional
  (its net is positive — the 56th data census confirms).
- The v63 queue (suggestions): the deferred reference-write censuses
  (unchanged), a re-check of the reference's axe-core VERSION drift
  (the 4.13 pinned family held this round; a major bump could shift
  rule coverage), and the standing-pair program's remaining minor
  surfaces (the /login 390 pair was covered by v39/v49/v50 pins; a
  /networth 390 full-page pair is the last un-paired viewport×view
  combination).
