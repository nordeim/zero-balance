# Remediation Plan v44 — The Drill-Down Expansion ANIMATION + the
# Chevron GLYPH Swap + the 390/1280 Census and the Donut-Legend Census
# (the session-95/96/97 queue)

Date: 2026-10-11 · Scope: the three queued surfaces — the drill-down
EXPANDED-state census at the REMAINING viewports (390 mobile / 1280
desktop — the 640 class was pinned in v43; the wrap behavior at 1280 and
the mobile indentation at 390 were unmeasured), the donut LEGEND's
geometry/interaction states (v14 pinned its content contract, never its
chrome), and — discovered DURING the sweep — the drill-down's EXPANSION
ANIMATION. Measured live on BOTH sites at 390×844 AND 1280×800 via
`exp-vp-v44.mjs` + `legend-v44.mjs` + `collapse-ref-v44.mjs` +
`band-mount-v44.mjs` (drivers: `vp-census-v44.sh` / `clone-v44.sh`).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **209/209 e2e ✓ (4.6m, clean re-run — one earlier verify-email
flake was a back-to-back register-bucket collision, re-run green)** ·
35/35 smoke ✓. The 38th standing checks all clean (mobile-nav R1–R4
both sites — Tailwind v4 pins hold, the mobile menu works; the
reference's toast-blocker, sheet-trap, no-landmark, 395 overflows all
still live; the data census read-only before + after; the SEO pair
live). npm audit = the same 5 dev-only ESLint-chain advisories
(accepted, unchanged); the secret-pattern scan clean; `.env`
byte-identical to `.env.example`; the workspace freshly re-cloned (the
environment rebuilt: npm install, prisma generate, db:push, db:seed,
playwright chromium install).

## The v44 sweep — what the measurement found

- **THE PARITY GAP F1 (the first production-code change since v43): the
  drill-down expansion ANIMATES on the reference and mounts INSTANTLY on
  the clone.** The reference's card height ramps smoothly over ~200ms on
  BOTH levels and in BOTH directions (section expand at 390:
  324→346→364→387→398→405 across ~40ms samples; section collapse:
  459→429→384→359→339→324; category expand: 405→421→437→454→459 —
  exp-vp-v44.mjs + collapse-ref-v44.mjs). The clone jumps straight to
  the end state at the first sample (324→441, 441→495, 495→324 — zero
  in-flight frames). The reference's mechanism, decoded by
  band-mount-v44.mjs: a JS per-frame height tween (mid-collapse the
  band's INLINE style reads `height: 25.5455px` — a fractional px value
  no CSS transition writes) with a concurrent opacity ease (computed
  0.314 at 110ms into a ~200ms collapse), the end state
  `style="height: auto; opacity: 1;"`, and the SECTION band UNMOUNTING
  after the collapse animation (collapsed root = the button alone).
- **The drill-down chrome is BYTE-IDENTICAL at both new viewports** (the
  v43 640 findings extend cleanly): at 390 the card 324 collapsed →
  441 → 495, the section row 48/pad 8px, the inner indent ml 40px/mt
  8px, the category rows 28/"6px 12px"/inline rgb(249,250,251), the sub
  rows 24/"4px 8px"/rgb(250,250,250), the item rows 24/"4px
  8px"/12px/rgb(156,163,175)/120px truncate, the footer 29/"6px
  12px"/border-t — every reading matches the reference. At 1280 the
  card 304 wide, 364 collapsed → 481 → 535, and the section label
  WRAPS to two lines on BOTH sites (labelH 40, row 56 — the v42 band
  census's 56 explained: width-driven wrap, not chrome). The clone's
  sw stays 390/1280 fully expanded (the reference reads 395 at 390 —
  its own documented horizontal-overflow bug, R4).
- **The donut legend census: BYTE-IDENTICAL, and the queue's
  "interaction" item RESOLVED (no code change).** The legend rows (3,
  value-DESC order) read identical chrome on both sites at BOTH
  viewports: h 64/pad 12px/radius 8px/bg rgb(245,248,245); the label
  16px/500/rgb(26,58,46); the amount 16px/700 in the classification
  color; the percent 12px/rgb(107,114,128); the dot 16×16/radius 4px;
  the icon 16×16; the inter-row gap 12px; the container mt 24px (flex,
  gap 12px). A REAL pointer hover on the first row changes NOTHING on
  either site (bg/shadow/cursor byte-identical before vs after,
  `changed: false` — legend-v44.mjs): the rows are inert divs, cursor
  auto. The donut wrapper: 308px wide at 390 / 418px at 1280, h 300.

## Findings

### F1. [PARITY — fix] the drill-down expansion animation

The reference tweens the bands' height 0↔auto + opacity 0↔1 over ~200ms
in both directions, then unmounts (section level). The clone mounts and
unmounts instantly. Fix: a `Collapse` wrapper component
(`src/components/budget/dashboard-view.tsx`) + a `.zb-collapse` /
`.zb-collapse-clip` class pair in `src/app/globals.css`:
- The **grid 0fr↔1fr technique** animates height 0↔auto with NO JS
  frame games (`display: grid` + `grid-template-rows` transition — the
  mechanism; the reference uses a per-frame JS tween, the observable
  height/opacity ramp matches; the band's computed `transition`
  diverges by construction and is deliberately NOT pinned).
- **`@starting-style`** runs the ENTRY transition on mount (the band
  mounts directly in the open state and animates from 0fr/opacity 0 —
  no double-render frame dance).
- The **exit** keeps the band mounted while the 0fr transition runs;
  `onTransitionEnd` (the React event handler — no effects, no
  setState-in-effect) unmounts it — the collapsed DOM returns to
  EXACTLY the pre-fix node tree (the accordion's `toHaveCount(0)`
  pins hold via Playwright's retry across the ~200ms window).
- The render-phase mount flip uses the documented
  adjust-state-during-render pattern (a prev-value ref guard — the
  CLAUDE.md dialogs' discipline); `visibility` leaves the a11y tree
  only after the exit completes (the delayed flip), and the band is
  fully unmounted anyway at rest.
- Applied at BOTH levels: the section band (`dashboard-view.tsx:287`)
  and the category band (`:321`), replacing the bare
  `overflow-hidden` conditional mounts. The `aria-expanded` superset
  (v32) is untouched.

### F2. [PARITY — pin] the drill-down census at 390 + 1280

Two e2e tests (the v43 census idiom, `page.setViewportSize`):
- **390×844**: the card 324→441→495 (the seed's arithmetic), the
  section 48/pad 8px, the inner indent ml 40px/mt 8px, the category
  rows 28/"6px 12px"/bg, the sub/item rows 24/"4px 8px"/12px/
  rgb(156,163,175)/maxW 120px, the footer 29/border-t, and **sw 390
  fully expanded** (the superset pin — the reference reads 395, its
  own overflow).
- **1280×800**: the card 304 wide, 364→481→535, the section row 56
  with **labelH 40 (the 2-line wrap — byte-parity with the
  reference's wrap at the narrow 1280 column)**, the same row chrome,
  sw 1280.

### F3. [PARITY — pin] the donut legend census + the inert hover

One e2e test (the default 1280 viewport): the three rows' geometry
(h 64/pad 12/radius 8/bg 245,248,245), the label/amount/pct fonts
(16/500/forestDark · 16/700/class-color · 12/gray), the dot 16×16/r4,
the icon 16×16, the gap 12, the container mt 24, the donut wrapper
418×300 — plus the REAL `.hover()` inertness pin (bg/shadow/cursor
unchanged under a real pointer hover, matching the reference's inert
divs).

### F4. [PARITY — fix, discovered mid-session via the VLM pair] the
chevron GLYPH swap

The standing VLM pair (vlm-compare-v44) flagged "the chevron points UP
on the reference, DOWN on the clone" — DOM-verified REAL
(chev-glyph-v44.mjs, fresh queries at every state): the reference's
chevrons SWAP ICON GLYPHS — `lucide-chevron-down` when collapsed,
`lucide-chevron-up` when expanded, back on re-collapse — at BOTH levels
(section 14px w-3.5, category 12px w-3), with rotate: none at every
state. The v43 "static chevron" finding was CORRECT but incomplete: the
flip is the ICON, not the transform — **a computed-style census cannot
see a glyph swap; read the svg's class**. The clone (post-v43) rendered
chevron-down at all states. Fix: conditional glyph render
(`{expanded ? ChevronUpIcon : ChevronDownIcon}` at both levels — a
glyph swap, never a rotation; the v43 static-rotation contract and the
aria-expanded superset both kept).

### S1. [MUTATION-SANITY] the animation, the legend pad, the sub-row pad, the glyph

Five mutations verify the pins bite:
(a) the transition duration 200ms→0s → the F1 animation pin fails
(no in-flight sample);
(b) remove `@starting-style` → the F1 ENTRY in-flight sample fails
(the exit still animates);
(c) the legend row `p-3`→`p-4` → the F3 census pin fails (h 64→72);
(d) the sub row `py-1`→`py-2` → the F2 390 census pin fails (the
sub-row chrome drifts);
(e) revert the section glyph swap → the F4 glyph pin fails
(chevron-down at every state).
All restored → GREEN.

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v44 paragraph + the 209→214 e2e count. D2:
CLAUDE.md — the v44 census/animation/glyph entry + the 214 counts. D3: README —
the v44 row + the counts. D4: the SKILL doc — the Session 79 row, the
213 count sites, the state line. D5: the PAD — a v1.1.1 revision block
(the animation contract, the 213 counts). D6: the probe README — the
v44 section (the five probes + the drivers + the lessons). D7:
session_98.md (the formal log) + session_99.md (the raw transcript) +
the repo worklog Session 78 + the ledger list. D8: the workspace
worklog (/home/z/my-project/worklog.md).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1/F2/F3/F4: the five e2e tests written FIRST (TDD RED: the animation + glyph tests fail pre-fix; the three census tests pin the already-correct chrome) | test | `tests/e2e/dashboard.spec.ts` |
| 2 | F1: the `Collapse` component + the `.zb-collapse`/`.zb-collapse-clip` class pair (`@starting-style` + the grid 0fr/1fr transition + the onTransitionEnd delayed unmount) | fix | `src/components/budget/dashboard-view.tsx` + `src/app/globals.css` |
| 3 | F4: the chevron glyph swap at both levels (`{expanded ? ChevronUpIcon : ChevronDownIcon}`) | fix | `src/components/budget/dashboard-view.tsx` |
| 4 | Rebuild → the five tests GREEN (the v43/v42 pins unchanged) | verify | — |
| 5 | S1(a)–(e): the five pin-sanity mutations, each verified to FAIL then restored | verify | the two files above |
| 6 | The full chain re-run (108 unit · 214 e2e · 35 smoke + lint + typecheck + build) | verify | — |
| 7 | The 16 screenshots regenerated | docs | `docs/screenshots/` |
| 8 | The v44 probes persisted + the probe README's v44 section | docs | `scripts/parity-probes/` |
| 9 | The standing VLM pair (the expanded drill-down post-fix; every flagged diff DOM-verified — the F4 glyph swap WAS a real flag) | verify | `scripts/parity-probes/` |
| 10 | D1–D8 + the formal session log (session_98.md) + the raw transcript (session_99.md) + the repo worklog Session 78 + the SKILL doc Session 79 row + the README/CLAUDE/AGENTS v44 rows | docs | repo root + `docs/` |
| 11 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/dashboard-view.tsx:287` — the section band's
  conditional `{expanded && (<div className="overflow-hidden">`: the
  F1 mount target. `:321` — the category band's `{catOpen && (<div
  className="overflow-hidden">`: the second target. Both bands sit
  inside containers with NO space-y margin implications (the section
  root has no space-y; the category band is nested INSIDE the category
  div — the space-y-2 applies between the category divs, one level
  up). The `aria-expanded` buttons (lines 252/295) are untouched.
- `src/app/globals.css` — the `.zb-*` family (`.zb-btn-add`,
  `.zb-row-action`, …) is the established home for reference-pinned
  chrome classes; `.zb-collapse` joins it.
- The e2e contract: the existing v42/v43 census tests settle 500ms
  after clicks (the 200ms animation completes first — the pinned end
  states hold). The accordion test's `toHaveCount(0)` assertions
  (breakdown.spec.ts:95,101) pass via Playwright's retry across the
  ~200ms delayed-unmount window. The axe gate scans post-settle — the
  collapsed band is unmounted at rest (the a11y tree is unchanged).
- The e2e census finders port the v43 idiom (`page.evaluate`, query by
  text markers, `getBoundingClientRect().height > 0` for the band —
  the mounted-at-0fr band is excluded while closed). The animation
  test samples the card height + the band's computed opacity at ~25ms
  intervals inside ONE evaluate (click + poll loop — the probes'
  discipline); the assertions are curve-agnostic (in-flight sample
  strictly between the endpoints + the end states) so sampling jitter
  cannot flake them.
- `@starting-style` and `grid-template-rows` transitions: supported in
  the e2e Chromium (153) and every current browser; the reference's
  own audience is modern-only (its Base44 runtime uses the same
  features).
- The reference's curve (measured ~25/52/76/90/100% progress at
  40ms-jitter samples) sits between `linear` and `ease`; the fix uses
  `ease` — within the sampling tolerance, documented in the CSS
  comment. The duration 200ms matches both directions' settle points.
- The chain gate: lint → typecheck → 108 unit → build → 209 e2e (214
  after: +5) → 35 smoke. The five tests add ~18s.
