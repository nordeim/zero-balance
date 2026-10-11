# Remediation Plan v43 — The Drill-Down Expanded-State Census + the
# Static-Chevron and Hover-RGB Fixes (the session-92/93 queue)

Date: 2026-10-11 · Scope: the two queued surfaces — the drill-down
EXPANDED-state census (the v42 session pinned the collapsed state; the
categories/subcategories/items bands were never measured) and the summary
card's hover/interaction states. Both measured live on BOTH sites at
640×960 (the mid viewport — the v41/v42 lesson's measured class) via
`exp-census-v43.mjs` + `exp-detail-v43.mjs` + `exp-rotate-v43.mjs` +
`hover-v43.mjs`.

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · **206/206 e2e ✓ (4.7m, the
first run, zero flakes)** · 35/35 smoke ✓. The 37th standing checks all
clean (mobile-nav R1–R4 both sites — the Tailwind v4 pins hold, the
mobile menu works; the reference's toast-blocker, sheet-trap,
no-landmark, 395 overflows all still live; the data census read-only
before + after; the SEO pair live). npm audit = the same 5 dev-only
ESLint `braces` advisories (accepted, unchanged); the secret-pattern
scan clean; `.env` byte-identical to `.env.example`; the v42 src diff
re-audited (exactly the 1-line divider condition + the comment).

## The v43 sweep — what the expanded-state census found

- **The collapsed→expanded chrome is byte-identical at every level**
  (the v42 divider fix's structure verified under expansion): the
  section row 48/8px pad/-8px mx/8px radius/14×14 chevron; the category
  rows 28/"6px 12px"/8px radius/inline `rgb(249, 250, 251)`/6×6
  9999px dot/12px-500-forestDark label/12×12 chevron; the sub rows
  24/"4px 8px"/`rgb(250, 250, 250)`/12px-400-gray label/4×4 dot at 0.6;
  the item rows 24/"4px 8px"/12px-400-`rgb(156, 163, 175)`/2×2 dot at
  0.4/the 120px truncate; the footer 29/"6px 12px"/1px border-t/12px-600.
  The card's expansion heights (the seed's arithmetic): 324 collapsed →
  441 (section expanded) → 495 (fully expanded); `sw 640` — no overflow
  even fully expanded. The reference's own numbers differ only by DATA
  (1 category vs the seed's 2 → +36px).
- **THE PARITY GAP F1 (the first production-code change since v42): the
  drill-down chevrons ROTATE on the clone and are STATIC on the
  reference.** The clone's `rotate-180` + `transition-transform` render
  `rotate: 180deg` (0.15s) on both levels; the reference's chevrons read
  `rotate: none`, `transform: none`, transition "all" 0s — measured
  definitively on BOTH chevron levels (the section 14px AND the category
  12px, fresh queries post-expansion). The first probe's `transform:
  "none"` readings on both sites were MEANINGLESS — Tailwind v4's
  `rotate-*` emits the modern CSS `rotate` property, not `transform`
  (the v4 property trap class); the definitive read is `rotate`.
- **THE PARITY GAP F2 (the same commit): the section-row hover renders
  lab() on the clone.** The reference's engaged `:hover` computes
  `rgb(249, 250, 251)` (v3 gray-50); the clone's `hover:bg-gray-50`
  (the v4 named palette) computes `lab(98.2596 -0.247031 -0.706708)` —
  the documented v4 named-palette trap, LIVE on this surface (the
  section button carries no inline bg, so the hover engages; the
  category rows' `hover:bg-gray-100` is inert on BOTH sites — the
  inline `background-color` overrides it everywhere, v29's documented
  finding, DOM-identical).
- **The queue's summary-card item RESOLVED (no code change):** the
  net-worth gradient summary card is STATIC on both sites — a REAL
  pointer hover reads byte-identical chrome (the same
  `linear-gradient(135deg, rgb(45,90,74)…)`, the same shadow
  `rgba(26, 58, 46, 0.3) 0px 20px 60px`, `cursor: auto`, transition
  "all"). No hover/interaction states exist to match.

## Findings

### F1. [PARITY — fix] the drill-down chevrons: static, like the reference

Two lines in `src/components/budget/dashboard-view.tsx`:
line 261 `cn("h-3.5 w-3.5 transition-transform", expanded && "rotate-180")`
→ `cn("h-3.5 w-3.5")`; line 293
`cn("h-3 w-3 transition-transform", catOpen && "rotate-180")` →
`cn("h-3 w-3")`. The chevrons keep their size/color/`transition-colors`
inheritance but never rotate — joining the reference's measured contract
(`rotate: none` at both levels, no transition). The `aria-expanded`
attributes STAY (the invisible a11y superset, kept since v32).

### F2. [PARITY — fix] the section-row hover: rgb, not lab

One class in `src/components/budget/dashboard-view.tsx` line 247:
`hover:bg-gray-50` → `hover:bg-[#f9fafb]` — the arbitrary hex emits
`rgb(249, 250, 251)` in v4 (the named-palette trap's documented fix
pattern: arbitrary hex on parity surfaces), joining the reference's
engaged hover byte-for-byte.

### F3. [PARITY — pin] the expanded-state band census at 640

One e2e test (a new describe in `tests/e2e/dashboard.spec.ts`, the v42
census idiom): expand Total Income + its first category, then pin the
per-row chrome — the section 48/pad 8px/mx -8px/radius 8px; the category
28/"6px 12px"/inline rgb(249,250,251)/dot 6×6/label 12px-500; the sub
24/"4px 8px"/rgb(250,250,250)/dot 4×4 at 0.6; the item 24/"4px 8px"/
12px/color rgb(156,163,175)/truncate maxW 120px; the footer 29/border-t
1px — plus the card's expansion heights (324 → 441 → 495, the seed's
arithmetic) and `sw 640` (no overflow fully expanded).

### F4. [PARITY — pin] the static chevron + the hover rgb

One e2e test: post-expansion, BOTH chevrons' `rotate` computes "none"
(the F1 pin — pre-fix the clone reads "180deg"); a REAL `.hover()` on
the section row computes `rgb(249, 250, 251)` (the F2 pin — pre-fix
`lab(…)`), and the hover is only on the section row (the category rows'
inline bg stays rgb(249,250,251) under hover — inert on both sites).

### S1. [MUTATION-SANITY] the rotation, the hover, the sub-row pad

Three mutations verify the pins bite:
(a) restore `rotate-180` on the section chevron → the F4 rotate pin
fails ("180deg" ≠ "none");
(b) revert `hover:bg-[#f9fafb]` → `hover:bg-gray-50` → the F2 rgb pin
fails (lab ≠ rgb);
(c) the sub row's `py-1` → `py-2` → the F3 census pin fails (28 ≠ 24).
All restored → GREEN.

### D1–D7. [DOCS] the doc-nit alignment (the core-doc review's findings)

D1: AGENTS.md line 63 "Six superset fixes" → "Seven" (the list runs
1–7). D2: AGENTS.md's v40/v41/v42 paragraphs reordered newest-last. D3:
the SKILL doc's `:3333` webServer port → `:3100` (the config default).
D4: the SKILL doc's stale counts (§3 bootstrap, §11 checklist,
Appendix A ADR-7, the Quick Reference Card: 87/34/30 → 108/209/35).
D5: README's "21 API handlers (13 files)" → "23 (15)". D6: PAD's v1.1.0
revision block (the counts, the four-state login card, the SEO routes,
the item-details sheet, the a11y gate, the verification lib). D7: the
README v37 row's "Session-76" label (collides with SKILL's Session 76
= v41) → the queue-citation convention.

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F3/F4: the three e2e tests written FIRST (TDD RED: the chevron rotate reads 180deg, the hover reads lab(98.26…), the census chrome pins) | test | `tests/e2e/dashboard.spec.ts` |
| 2 | F1: the two chevron conditions stripped (`rotate-180` + `transition-transform`) | fix | `src/components/budget/dashboard-view.tsx:261,293` |
| 3 | F2: `hover:bg-gray-50` → `hover:bg-[#f9fafb]` | fix | `src/components/budget/dashboard-view.tsx:247` |
| 4 | Rebuild → GREEN (the three tests first-run) | verify | — |
| 5 | S1(a)–(c): the three pin-sanity mutations, each verified to FAIL then restored | verify | the two files above |
| 6 | The full chain re-run (108 unit · 209 e2e · 35 smoke + lint + typecheck + build) | verify | — |
| 7 | The 16 screenshots regenerated (the five dashboard-family shots show the static chevron) | docs | `docs/screenshots/` |
| 8 | The v43 probes persisted + the probe README's v43 section | docs | `scripts/parity-probes/` |
| 9 | The standing VLM pair (the desktop dashboard post-fix; every flagged diff DOM-verified) | verify | `scripts/parity-probes/` |
| 10 | D1–D7 + the formal session log (session_95.md) + the raw transcript (session_96.md) + the repo worklog Session 77 + the SKILL doc Session 78 row + the README/CLAUDE/AGENTS v43 rows | docs | repo root + `docs/` |
| 11 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/dashboard-view.tsx:247` — the section button's
  `hover:bg-gray-50` (no inline bg — the hover LIVES): the F2 target.
- `:261` / `:293` — the two `cn("h-… w-… transition-transform",
  … && "rotate-180")` chevrons: the F1 targets. The `aria-expanded`
  attributes (lines 245/281) STAY — the v32 a11y superset.
- The census tests port the v42 `page.setViewportSize({ width: 640,
  height: 960 })` + `page.evaluate` idiom (query by the text markers,
  never the class names); the rows live under the "Net Zero Breakdown"
  card; the seed's expansion arithmetic (2 income categories, the
  first with 1 sub + 1 item) is deterministic for `db/custom.db`.
- The `rotate` property read is the ONLY valid rotation probe on the
  clone (v4 emits `rotate`, not `transform`); on the reference both
  read none — the pin asserts `"none"` on both levels.
- The hover test uses a REAL `locator.hover()` (the drill-down rows
  carry no mouse-following tooltip — the donut's synthetic-hover
  lesson does not apply); the computed backgroundColor pin
  `"rgb(249, 250, 251)"` fails pre-fix (`lab(98.2596 -0.247031
  -0.706708)`).
- The chain gate: lint → typecheck → 108 unit → build → 206 e2e (209
  after: +3) → 35 smoke. The three tests add ~10s.
