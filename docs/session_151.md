# Session 151 — v62: the reference-side a11y surface re-audit (NO DRIFT since v38) + the TWO-pair VLM program + the mobile header-subtitle 390 census pin

The continuation of the audit → fix → alignment → deliver workflow on
the `zero-balance` repo, executing the session-147 v62 queue. The
workspace was a fresh sandbox this session (the local clone was gone —
re-cloned from `https://github.com/nordeim/zero-balance.git` at
`a58e13e`, main, clean).

## Refresh & validation

Two parallel Explore digests covered the five huge core docs
(AGENTS/CLAUDE/README/PAD/SKILL) and the latest session records
(session_149 / remediation-plan-v61 / session_150 / the worklog head);
a third agent reviewed the scandihaven repo's tech-stack patterns
(near-exact stack match — Next 16/React 19/TS 5.9/Tailwind 4.3/Zod 4/
Zustand 5/Vitest 5/Playwright 1.63; its Tailwind v4 gotchas and e2e
discipline are already implemented here; the review confirmed no new
patterns to adopt this round). The environment bootstrap: `npm
install`, `npx prisma generate`, `npm run db:push`, `npm run
db:seed` (the dev DB re-seeded — the seed's `isoDate(-N)` dates now
anchor to today), `.env` copied from the verified `.env.example`
(`DATABASE_URL="file:../db/custom.db"`), and — the fresh-sandbox
caveat this session's probe lesson records — `npx playwright install
chromium` (the first e2e run failed on the missing browser binary:
94 failures with the "Executable doesn't exist" signature).

**Baseline chain GREEN: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · 263 e2e ✓ (95 + 94 + 76
chunk runs = 262 chromium + 1 setup) · 35/35 smoke ✓** — the codebase
matches the documented v61 state exactly (the v61 pins verified at
dashboard.spec.ts:2643 + 2757; the src tree identical to the v61
ship).

## The 56th standing checks

`ref-standing-v56.sh` + `standing-checks-v56.sh` (version bumps of
the v55 scripts). Reference: the four bugs ALL still live (the
toast-blocker `hitIsBurgerChild:false` via the `DIV.fixed top-0
z-[100]` intercept; the overlay trap `overlayCount:1` after the nav
click; `navLandmark:false`; the 464px `/networth` overflow at 390);
the data census UNCHANGED (the 56th consecutive clean drift check:
"1 items · $25,000" / "1 items · $5000.00" / "4 items · $525.00");
the SEO pair live. Clone: R1 the burger hit-test true + the sheet
opens; R2 the sheet closes + navigates; R3 the landmark; R4 zero
overflow at 390 on all five views; the SEO pair live. **The mobile
navigation menu VERIFIED WORKING — the 56th consecutive time.**

## The v62 sweep

**The a11y re-audit — the queue's top item (`axe-detail-ref-v62.mjs`):
NO DRIFT since v38.** The full a11y.spec.ts surface re-scanned on the
live reference (six authed routes at 1280 + the 404 + the logged-out
login + the mobile 390 sheet-open state, axe-core 4.13, the same four
tags): the login still zero-violation; the structural families still
exactly `button-name` (10 nodes) + `svg-img-alt` (6 nodes) — the two
families the clone's GATE 1 superset fixes; the contrast palette
still EXACTLY the v38 7-color set. The clone's a11y.spec.ts contract
remains valid as pinned — no code change.

**The TWO-pair VLM program (the standing pair + the NEW mobile 390
twin).** The desktop 1280 full-page pair: five flags, ALL arbitrated
to documented classes (the nav-highlight root-URL gap; the avatar;
the allocation data class; the donut labels — a PERCEPTION ARTIFACT,
the reference renders its three [92.3/4.6/3.1], DOM-verified via
`arbit-v62.sh`; the Base44 FAB). The mobile 390 full-page pair (new):
two flags, both arbitrated (the Base44 tooltip; **"the clone's
subtitle wraps to a third line" — a PERCEPTION ARTIFACT**:
`arbit2-v62.sh`'s leaf-text census measured the subtitle P on BOTH
sides byte-identical [h 48, 2 lines, 16px/400/rgb(107,114,128), lh
24px, block h 92, top 121] — the 5px width delta is the reference's
own 395px docSW overflow. The v61 meta-lesson's INVERSE: the DOM
census ACQUITTED what the VLM convicted.)

**No production-code parity gap this session** — the pin-only line
resumes after the v61 fix (`git diff src/` empty at ship).

## The remediation plan v62 + the TDD execution

`docs/remediation-plan-v62.md` (the 62nd plan; the ToDo table's 12
rows). The pin: **the mobile header-subtitle block census at 390**
(the never-pinned surface the M2 arbitration measured — the existing
desktop test asserted the subtitle's visibility only):
- RED-then-GREEN iteration: the first pin run failed on TWO of its
  own expectations — (1) the `getClientRects()` line heights are
  GLYPH boxes (~19px for a 16px font — the font-metric content
  height), NOT the 24px line boxes → replaced with the lineRhythm
  contract (the delta between the two line tops = exactly the 24px
  line-height); (2) the block-top expectation was derived arithmetic
  (68) instead of the probe's measured value (77 = P top 121 − h1 36
  − mb-2 8). Both are this session's recorded probe lessons.
- GREEN: the P {h 48, top 121, 16px/400/gray-500, lh 24px, 2 lines,
  lineRhythm 24} + the block {h 92, top 77} + the h1 {36/30px/700/mb
  8px}; the WIDTH axis deliberately not pinned (the reference's own
  395px overflow makes its column 5px wider — the WRAP OUTCOME is
  the contract).
- ONE pin-sanity mutation verified to FAIL then restored (the inline
  lineHeight 24→28px → h 48→56 + lineRhythm 24→28 + lh "28px" — three
  axes at once; the standalone REBUILD as a SEPARATE command; the
  restore verified with `git status src/` clean + the full dashboard
  spec 35 passed).

**The F3 docs sweep:** the SKILL doc's four stale current-state count
lines corrected (the 214-era bootstrap line 177, the 223/223 gate
line 474, the 223 decisions line 1191, the 22-files/214-tests
inventory line 1255 — all now the current counts; the historical
session rows stay era-correct).

## The screenshots

The 16 regenerated: 10 byte-identical + 6 VLM-arbitrated — 5 the
SEED-DATE class (the item-view card footers + the details date row +
the networth Updated stamp, each advanced exactly one day: the dev DB
was re-seeded this session, the seed dates anchor to the seed-run
day) + 1 [08-calculator] the sub-perceptual AA-timing class (1,596
differing pixels in a 57×73 bbox; the full-shot VLM IDENTICAL and the
3×-upscaled region-crop re-arbitration IDENTICAL —
`vlm-shotsdiff-v62.mjs` + `arbit-calc-v62.mjs`).

## The chain + the ship

**Full chain GREEN: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ ·
264 e2e ✓ (96 + 94 + 76 chunk runs = 263 chromium + 1 setup; zero
failures) · 35/35 smoke ✓.** The docs aligned D1–D8 (the AGENTS v62
paragraph; CLAUDE 263→264; the README state lines + the v62 table
row; the SKILL Session 97 row + the state line; the PAD v1.1.19
revision block; the probe README's v62 section; this session log +
the repo worklog Session 96; the workspace worklog). The v62 probe
family persisted: `axe-detail-ref-v62.mjs`, `vlm-shots-v62.sh`,
`clone-vlmshots-v62.sh`, `vlm-compare-v62.mjs`, `arbit-v62.sh`,
`arbit2-v62.sh`, `vlm-shotsdiff-v62.mjs`, `arbit-calc-v62.mjs`,
`ref-standing-v56.sh`, `standing-checks-v56.sh`.

## The v63 queue (suggestions)

1. The deferred reference-write censuses (unchanged — all need
   reference WRITES, out of bounds under the v46 read-only rule): the
   verify-email panel census, the forgot-confirm state census, the
   calculator EMPTY-state census, the line-items dialog glyphs.
2. A re-check of the reference's axe-core VERSION drift (the 4.13
   family set held this round; a major bump could shift rule
   coverage).
3. The standing-pair program's remaining minor surface: a /networth
   390 full-page pair (the last un-paired viewport × view
   combination).
