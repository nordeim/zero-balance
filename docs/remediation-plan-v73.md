# Remediation Plan v73 — the NEW-pair program's LAST never-shot surfaces (the login + calculator mobile 390 twins) + the axe watch (NO DRIFT) + the calculator scrim + summary-text chrome pin (PIN-ONLY)

The session's plan, validated against the codebase before execution. The formal narrative ships in `docs/session_175.md`; the repo worklog entry: Session 107.

## The v73 sweep — what the measurement found

### F1 [WATCH] — the axe-core watch at its re-check point: NO DRIFT

npm-latest `@axe-core/playwright` = 4.14.0 (the dist-tags carry only 4.14.1 rc/next prereleases — no stable 4.14.1, no 4.15, no 5.x); npm-latest `axe-core` = 4.14.0 (no 5.x engine exists). The lockfile holds the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core@4.14.0, verified live via the wrapper's own `require.resolve`; no nested engine dir). The engine-contract pin executed GREEN standalone (2 passed). Only a 5.x wrapper (or a nested-engine change) changes the calculus; the next re-check point unchanged.

### F2 [STANDING] — the 67th standing checks: ALL GREEN

ref-standing-v67.sh + standing-checks-v67.sh (version-bumped from v66). Reference side: the four bugs ALL still live (the toast-blocker `hitIsBurgerChild:false`; the sheet-trap `overlayCount:1`; the no-landmark `navLandmark:false`; the 464px /networth overflow at 390) + the data census UNCHANGED (the 67th consecutive clean drift check: "1 items · $25,000" networth / "1 items · $5000.00" income / "4 items · $525.00" expenses) + the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation menu VERIFIED WORKING (the 67th consecutive time), zero overflow at 390 on all five views, the SEO pair live.

### F3 [PAIR] — the NEW-pair program's LAST never-shot surfaces: the login + calculator mobile 390 twins — NO NEW GAP, every flag arbitrated

vlm-shots-v73.sh + clone-vlmshots-v73.sh + vlm-compare-v73.mjs (login on the first attempt both sides; the parked pointer at (5,5); the hover + Calculate clicks are VIEW-STATE only — the v46 read-only rule holds on the reference; the clone's 1-row calculator state rides the v66 fixture discipline — the Contents Insurance $25 line item added through the real UI, then FULLY restored: delete + Rent's $1850 re-edit + the "3 items · $2235.00" page-total verification + the seedcheck confirming the exact seed state):

- **PAIR 1 (the LOGIN page at mobile 390x844 — the fresh logged-out surface, the simplest never-shot pair; the v59/v66 login pairs were desktop 1280 only): VERDICT IDENTICAL — zero flags.** Both sides render the centered login card byte-identically (the fresh-session census both sides: `hasLoginCard:true`, docSW 390, title "ZeroBudget"). CLEAN — the pair that needed no arbitration.
- **PAIR 2 (the CALCULATOR dialog at mobile 390x844 — the v66 desktop pair's mobile twin, the dialog-state surface): VERDICT DIFFERENT with two flags, every one DOM-arbitrated via arbit-v73.sh:** (1) "the clone's scrim appears slightly lighter or more transparent than the reference's" = a **PERCEPTION ARTIFACT, DOM-disproven** — the scrim chrome BYTE-IDENTICAL on both sides (bg `rgba(26, 58, 46, 0.5)`, computed opacity 1, `backdrop-filter: blur(8px)`, w 390, h 844; the reference's scrim is the wrapper that CARRIES the dialog's text — `hasText:true` — while the clone's Radix scrim is a textless SIBLING of the panel, the documented v72 structural class: the DOM shapes differ, the rendered chrome does not); (2) the "• Will update category total" span (shown on the clone, absent on the reference) = the **v66 DATA-CONDITIONAL class re-verified live** — the span renders while `total !== item.amount`: the reference's OWN Rent is natively $25.00 and its single line item sums to $25.00 → HIDDEN (measured `willUpdateSpan.present:false`); the clone's modal snapshot carries the opened-at parent $1850 against the recalculated $25.00 → SHOWN (measured 12px/400/rgb(234,88,12) — the pinned contract).
- **The full both-sides census (arbit-v73.sh — the calculator's complete chrome at 390, the panel-through-row inventory): BYTE-IDENTICAL on every axis** — the panel (x 16, y 216, w 358, h 413, maxW 768px, maxH 717.4px, radius 16px, bg white, border 0; the reference's transparent computed-form shadow layers vs the clone's visible `.zb-modal-panel` layer = the documented accepted lead-divergence class, the v49 pin's idiom; the panel `position:static` inside the reference's fixed wrapper vs the clone's `position:fixed` panel = the v72 structural class, rendered geometry identical), the header (h 101, pad "16px 24px", flex, border-b 1px rgb(229,231,227)), the close button (29×36 — the flex-squished width, the v53-pinned value — radius 6px, border 0, bg transparent, no shadow/outline, color rgb(10,10,10)), the title (18px/700/lh 28px/rgb(26,58,46)), the description (14px/lh 20px/rgb(107,114,128)), the Total Calculated block (bg rgb(255,247,245), border 1px rgb(252,221,213), radius 12px, pad 16px, w 310, h 90, mb 24px), the summary amount (24px/700/lh 32px/rgb(224,122,59)), the "Based on 1 item" line (12px/rgb(107,114,128)), the line-item row (h 102, w 310, pad 16px, radius 12px, bg white, border 1px rgb(229,231,227), the two 32px action buttons at opacity 1 — IDENTICAL on both sides), the Add Item button (110×32, 12px/500, radius 6px, white text). **NO NEW GAP.**
- **The probe-implementation lessons (the v73 findings on the process itself):** (a) the mobile fold — at 390 the Rent card sits BELOW the fold in the 1-col grid (card center y > 844); a raw mouse move to out-of-viewport coordinates never engages the card's `:hover`, so the Calculate button stays hidden and the click misses — `scrollIntoView({ block: 'center' })` BEFORE the hover is the required step (the probe's first pass failed exactly here: `no dialog`); (b) the unquoted-heredoc dollar trap — a `<<EOF` (unquoted) heredoc expands `\$1850` into `$1850` at heredoc-processing time, and the inner `bash -s` then reads `$1` (a positional parameter) inside the double-quoted eval string → `set -u` kills the script with `unbound variable` — the fix is the QUOTED `<<'EOF'` heredoc with the shared census injected via an ENVIRONMENT variable (`CALC_CENSUS_JS="$CALC_CENSUS_JS" bash ... bash -s <<'EOF'`), the inner script keeping the probe's own `\$` escaping conventions.

### F4 [PIN] — the calculator's scrim + summary-text chrome census at 390 (PIN-ONLY for src/ — no production-code change; +1 e2e = 276)

The never-pinned axes (the existing calculator pins cover the panel/header/chip/close/totalCard/row/addBtn GEOMETRY at 390 [v53 F2] and the height-family at 1280 [v66 F3] — the scrim and the text chrome were never pinned):

- the calculator dialog's SCRIM chrome at 390 (the details-sheet overlay is pinned in item-details.spec.ts; the calculator's own scrim never was): bg `rgba(26, 58, 46, 0.5)`, computed opacity 1, `backdrop-filter: blur(8px)`, the full-viewport geometry (w 390, h 844) — the clone's sibling overlay measured byte-identical to the reference's wrapper-scrim;
- the summary amount's full chrome at 390: fs 24px / fw 700 / lh 32px / color rgb(224,122,59);
- the "Based on 1 item" line chrome: fs 12px / color rgb(107,114,128);
- the description line chrome at 390: fs 14px / lh 20px / color rgb(107,114,128);
- the "• Will update category total" span's full chrome with the 1-row fixture: 12px / fw 400 / color rgb(234,88,12) (the early default-viewport pin covers the color only via toHaveCSS; the v73 pin locks the full family at 390).

The pin rides the v53 fixture discipline (hover → Calculate → Add Line Item "Contents Insurance" $25 → the census → the Delete cleanup → restoreRent) and asserts the arbit-v73.sh census's own measured values, byte-identical on both sides' 1-row calculator dialogs at 390.

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → build → **276 e2e** in chunks (+1) → 35 smoke; the 16 standing screenshots regenerated + byte-compared (the same-DB discipline; the seedcheck under `env -u DATABASE_URL`).

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the calculator's scrim + summary-text chrome census at 390 (the v53 fixture discipline + the arbitration's own measured values) | tests/e2e/calculator.spec.ts |
| 2 | sanity | the pin-sanity mutation: the scrim's `backdrop-filter` removed (or the amount's color swapped) → the pin FAILS at exactly that axis; restored → GREEN (the standalone REBUILD as a SEPARATE command) | src/app/globals.css (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → build → 276 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v73 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (275→276 + the v73 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v73 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 108 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.30 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v73 section (the new probes + the v73 lessons: the mobile-fold scroll + the quoted-heredoc dollar trap) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_175.md + the repo worklog Session 107 entry | docs/session_175.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the arbit-v73.sh census's own measured values, byte-identical on both sides' 1-row calculator dialogs at 390: the scrim (bg rgba(26,58,46,0.5) / opacity 1 / blur(8px) / 390×844), the summary amount (24px/700/lh 32px/rgb(224,122,59)), the basedOn line (12px/rgb(107,114,128)), the desc (14px/lh 20px/rgb(107,114,128)), the willUpdate span (12px/400/rgb(234,88,12), present with the fixture).
- The fixture mechanics verified live TWICE this session (the v73 probe + the arbitration): the hover → Calculate → Add Item → Add Line Item ("Contents Insurance" / $25 / Save Item) flow, the Delete cleanup ("Delete Contents Insurance" → the inline "Delete" confirm), the restoreRent re-edit to $1850, the header restored to "3 items · $2235.00", the seedcheck confirming the exact seed state (7 items / rent 1850 / expenses 2235 / 0 line items) after BOTH passes.
- The existing pins are SAFE: the v53 F2 pin asserts the same panel/header/row axes (untouched by the new pin); the v66 height-family pin rides the 1280 viewport; the early default-viewport pin covers the totalCard colors (the v73 pin's text-chrome axes are disjoint); no existing test asserts the scrim's chrome on the calculator dialog.
- The blast radius: ZERO production-code change (every flag arbitrated to a documented class or disproven — the pin-only line resumes after v71's fix); the pin-sanity mutation touches `src/app/globals.css` (the `.zb-modal-overlay` backdrop-filter) REVERTED before ship (`git diff src/` = 0 lines at commit).
- The chain gate: lint → typecheck → 108 unit → build → 275 e2e (**276** after: +1 — the F4 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every agent-browser run; the with-server boots fresh per command; the reference session EXPIRES between long eval gaps — the login-retry loop handles it; the e2e chunks pass FULL file paths; `ss -tlnp | grep :3100` + kill before every full-chain run (the v53 orphaned-webServer lesson); one-shot Prisma scripts need `env -u DATABASE_URL` (the sandbox's inherited parent-workspace URL is the documented pollution); no dollar sequences in census JS inside double-quoted bash strings (the v64 rule); no attribute-value selectors in single-quoted eval strings (the v60/v67 rule — geometry + text-content filters instead); the QUOTED heredoc with the env-injected census (the v73 lesson); the mutations need the standalone REBUILD as a SEPARATE command (the v53 lesson); the clean-check gate re-runs AFTER every new file lands (the v69 lesson); the mobile calculator flow needs `scrollIntoView` before the hover (the v73 lesson).
- The deferred queue (unchanged, all need reference WRITES — out of bounds under the v46 read-only rule): the reference-side verify-email panel census, the forgot-confirm state census, the calculator EMPTY-state reference census, the line-items dialog glyphs.
- The v74 queue (suggestions): (1) the NEW-pair program is COMPLETE (every view + dialog + sheet surface now carries a mobile-390 twin AND a desktop pair) — the cadence rotates to the re-run cycle's OLDEST candidate (the v58-era savings pair, last re-shot v65 — the only pre-v70 pair not re-run since), (2) the axe-core watch at its next re-check point (only a 5.x wrapper changes the calculus), (3) the deferred reference-write censuses (unchanged).
