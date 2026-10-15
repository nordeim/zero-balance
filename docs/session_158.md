# Session 158 — Parity iteration v65 (the OLDEST remaining desktop pair's fresh standing sweep + the axe watch + the savings page-header-row pin)

Fresh sandbox — the repo re-cloned at f3e8934 (main), the environment
rebuilt from scratch: npm install (+ the prisma engines rebuild + the
npm rebuild for the postinstall-blocked packages), .env restored
(DATABASE_URL="file:../db/custom.db"), db:push + db:seed (7 items / 3
assets / 2 liabilities), and the Playwright browsers installed (the
fresh-sandbox caveat — `npx playwright install chromium` before the
first e2e run).

**Baseline chain GREEN: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓
(robots + sitemap prerendered) · 266 e2e ✓ (91 + 95 + 82 chunk runs =
265 chromium + 1 setup per chunk) · 35/35 smoke ✓** — the codebase
matches the documented v64 state exactly (the v64 pin verified present
at items.spec.ts "the income filter-card computed census at 1280").

## The v65 iteration (the session-155 queue)

The documented v65 queue's two items: (1) the v58-era savings pair's
fresh sweep — "the queue's other OLDEST candidate — the v64 pass
covered the v57-era items pair" — and (2) the axe-core 5.x wrapper
watch (the unchanged next re-check point), plus the 59th standing
checks. **PIN-ONLY** — no production-code change; the pin-only line
continues.

### The 59th standing checks — ALL GREEN

Version-bumped the v58 scripts to v59 (`ref-standing-v59.sh` +
`standing-checks-v59.sh`). Reference side: the four bugs ALL still live
— the toast-blocker (`hitIsBurgerChild:false`, the burger's center hit
intercepted by `DIV.fixed top-0 z-[100]`), the sheet-trap (the overlay
remains after the nav click, `overlayCount:1`), the no-landmark
(`navLandmark:false`), the 464px `/networth` overflow at 390; the data
census UNCHANGED (the 59th consecutive clean drift check: "1 items ·
$25,000" networth / "1 items · $5000.00" income / "4 items · $525.00"
expenses); the SEO pair live. Clone side: R1 the burger hit-test TRUE +
the sheet opens · R2 the sheet CLOSES + navigates · R3 the nav landmark
present · R4 ZERO overflow at 390 on all five views. **The mobile
navigation menu VERIFIED WORKING — the 59th consecutive time.**

### F1 — the axe-core 5.x wrapper watch: NO DRIFT

The npm-latest `@axe-core/playwright` is STILL 4.13.0 (no 5.x release
exists), the lockfile resolves the wrapper to 4.13.0, and the engine
that actually executes the AxeBuilder scans — the wrapper's NESTED
`axe-core@4.13.0` — is byte-identical to the v38/v62/v63/v64 audits.
The top-level `axe-core@4.14.0` still belongs to eslint-plugin-jsx-a11y
(lint-time only). The next re-check point: unchanged.

### F2 — the OLDEST remaining desktop pair's fresh sweep: the v58-era savings pair re-run

Wrote the v65 probe family (`vlm-shots-v65.sh` +
`clone-vlmshots-v65.sh` + `vlm-compare-v65.mjs` — the savings view
FULL-PAGE at 1280×800, the parked-pointer discipline). The VLM flagged:
the avatar color + initial, the card grid layout, and the expected data
differences.

Every flag DOM-arbitrated (the v43 rule) via `arbit-v65.sh` (a
two-pass arbitration — the first pass re-learned the v64 rule that the
census JS inside the unquoted heredoc must carry NO dollar sequences:
a comment "N items · $X" blew up as "X: unbound variable"; also the
clone-side avatar finder had to learn the clone's rounded-[9999px]
class, and the reference's HIDDEN zero-size h1 "ZeroBalance" made
querySelector('h1') ambiguous — the v65b pass fixed all three):

- **The avatar** — the user-identity class, re-measured live with a
  NEW perception lesson: the chrome BYTE-IDENTICAL (36×36, radius
  9999px, 14px/600, white text, **bg rgb(143, 188, 63) on BOTH
  sides** — the same lime). Only the INITIAL differs: the reference
  renders "U" for its nameless account; the clone's demo user renders
  "D" (the documented name-derived-initial contract). The VLM's
  "green vs lime" color claim was a PERCEPTION ARTIFACT — identical
  computed colors read as different hues.
- **The card grid layout** — the seed-count data class: the axes
  BYTE-IDENTICAL (w 960, gap 16px, 3 tracks); the reference's 1
  savings item vs the clone's 2-item seed. NOTE: the fractional
  last-track distribution is CONTENT-COUNT-CONDITIONAL (the
  reference's template reads 309.328×3 at ONE child while the
  clone's reads 309.328/309.328/309.344 at TWO; the v64 census
  measured the SAME 309.344 tail on both sides at 4-vs-3 children) —
  the axes are the contract, the subpixel tail a rendering artifact
  of the data class.
- **The goal-card footer + badges + card heights** — the v57
  DATA-CONDITIONAL classes re-measured live: the footer chrome
  BYTE-IDENTICAL (flex justify-between 12px rgb(107,114,128) h 16;
  every child span flex gap 4px with the 12×12 gray icon; the
  reference's item carries no paymentMethod so its footer renders
  ONE child, the clone's TWO); the badge chrome BYTE-IDENTICAL
  (flex/6px radius/2px 10px pad/12px-600/h 22; the row flex wrap
  8px gap mb 12px; the clone's Recurring superset badge wraps the
  row to h 52 = 22+8+22); the card heights 200 vs 230 = the
  badge-wrap arithmetic.
- **The Add button's computed box-shadow** — the reference renders
  two LEADING zero-alpha layers (the Tailwind v4 computed-form class)
  over the clone's `.zb-btn-add` visible layers alone: the visible
  geometry BYTE-IDENTICAL (`rgba(0,0,0,0.1) 0 1px 3px 0,
  rgba(0,0,0,0.1) 0 1px 2px -1px`) — the documented v11 class.

**The pair is CLEAN: every flag arbitrates to a documented class. No
production-code parity gap.**

A DOM-structure discovery (documented, not a gap): the reference's
savings page carries a HIDDEN zero-size h1 "ZeroBalance" FIRST in its
DOM (x:0, y:0, w:0, h:0 — its own SEO pattern; an 18px/700 h2
"ZeroBalance" logo sits in its sidebar) before the VISIBLE 30px/700 h1
"Savings" — the clone renders the visible h1 alone, BYTE-IDENTICAL
chrome (30px/700/lh 36/forestDark).

### F3 — the savings view's page-header row computed census at 1280

The F2 arbitration census measured a never-census'd family: the
DESKTOP 1280 page-header row of the items views — the v42 census
pinned the MID-640 STACKED state only (headerRowMb 32px/dir column
across all five routes); the v63 pin the mobile 390 networth block;
the early-era tests pin CLASS STRINGS (the chip h-12, the Add-button
gradient) but never the computed geometry of the 1280 row. The census,
measured BYTE-IDENTICAL on both sides (the savings instance): the row
flex space-between/center/gap 16px/mb 32px/h 60; the chip 48×48
radius 12px with the savings blue gradient; the white 24×24 chip
icon; the h1 30px/700/lh 36px/forestDark; the count subtitle
16px/400/rgb(107,114,128); the Add button 150×36/6px radius/8px 16px
pad/14px/500/white with the savings blue gradient + the .zb-btn-add
visible shadow layers; the 16×16 plus icon.

Wrote `docs/remediation-plan-v65.md` (the 65th plan, the 13-row
ToDo), validated against the codebase (the finders tested live in the
arbitration; the mutation targets located at items-view.tsx:131/136/
144), then the TDD execution — the F3 pin in `tests/e2e/items.spec.ts`
inside the savings describe right after the v38 S2 filter-card test:

**GREEN first run (PIN-ONLY).** The mutation-sanity checks — S1: the
header row `mb-8`→`mb-4` (mb 32→16) BITES; S2: the chip `h-12 w-12`→
`h-10 w-10` (the chip finder nulls, 48→40) BITES; S3: the h1
`text-3xl`→`text-2xl` (30px→24px + lh 36→32 + the row h 60→56 — the
TEXT BLOCK governs the row height, not the 48px chip) BITES — each
with the standalone REBUILD as a SEPARATE command. Restored; git
status src/ clean; the full items spec 31 passed (+1).

### The screenshots

All 16 BYTE-IDENTICAL (the fresh sandbox's re-seed anchored to the
same day as the v64 capture — no production change, no drift).

### Docs alignment D1–D8

The AGENTS v65 paragraph (+2 lines, additive-only); CLAUDE 266→267 +
the header-row pin reference; the README state lines + the v65 table
row; the SKILL Session 100 row + the three count lines; the PAD
v1.1.22 revision block (title + the block); the probe README's v65
section; session_158.md + the repo worklog Session 99 entry; the
workspace worklog. Verified every edited doc's line count (the v63
truncation lesson).

## Session summary (parity iteration v65 — pin-only)

- **Refresh & validate**: fresh sandbox — re-cloned at f3e8934; the
  environment rebuilt from scratch; baseline chain GREEN (108 unit /
  266 e2e / 35 smoke) — the codebase matched the documented v64 state
  exactly
- **59th standing checks**: mobile navigation menu **verified
  working** (59th consecutive round); the reference's four mobile
  bugs all still live; data census unchanged; SEO pairs live on both
  sites
- **F1 — the axe-core 5.x wrapper watch**: **NO DRIFT** — still
  4.13.0 (no 5.x exists); the nested engine byte-identical to the
  v38/v62/v63/v64 audits
- **F2 — the OLDEST remaining desktop pair's fresh sweep**: the
  v58-era savings pair re-run (FULL-PAGE 1280×800) — **the pair is
  CLEAN**: every flag DOM-arbitrated to documented classes (the
  avatar's "green vs lime" a perception artifact — the bg
  BYTE-IDENTICAL; the grid's subpixel tail content-count-conditional;
  the v57 footer/badge contracts re-measured byte-identical; the v11
  shadow class re-confirmed) + the hidden-h1 discovery (the
  reference's SEO pattern)
- **TDD pin added**: the savings view's page-header row computed
  census at 1280 (+1 e2e = **267** — the never-census'd family behind
  the v42 mid-640 stacked-state census), three mutations verified to
  FAIL; all 16 screenshots byte-identical; docs aligned D1–D8
- **Shipped**: pushed to `main` via the SSH wrapper — fingerprint
  matched, remote verified, keys shredded

**Suggested next steps** (the documented v66 queue): the re-run
cadence rotates to the v59-era pair (the calculator + login views at
1280 — the v61-fix-era shots, the oldest remaining after v64/v65
covered the v57/v58 pairs), the axe-core 5.x wrapper watch (unchanged),
or the deferred reference-write censuses — just say the word.
