# Session 122 — Parity iteration v52: the details sheet's missing subcategory line (THE FIX — the fourth production-code change since v46) + the /income and /expenses 390 pins + the details-sheet internals pin + the standing script's burger-selector probe-infra fix (2026-10-12)

**Goal:** the session-121 v52 queue's read-only members — the
/expenses and /income mobile censuses at 390 (the item-card family
beyond the v51 savings pin) + the item-details 390 reflow (the v28
geometry pins walked the panel chrome only, never the summary's
content sequence). TDD-first, docs aligned, commit + push via the
SSH wrapper. (The workspace SURVIVED this session — a `git pull`
fast-forward to e71d357, the session_121.md "update session log"
commit on top of the v51 parity commit 2d2a776; the environment was
already in place: node_modules, the seeded db/custom.db, the .env
contract.)

## What was done

**Step 0 — the workspace.** `git pull` fast-forwarded 2d2a776 →
e71d357 (docs/session_121.md added — the v51 session's raw Chinese
transcript + the v52 queue suggestions: the reference-side verify /
forgot-confirm censuses [both WRITES — out of bounds, deferred],
the /expenses and /income mobile censuses, the item-details 390
reflow). The five core docs (AGENTS / CLAUDE / README / PAD / SKILL)
+ the four session docs (session_120 / remediation-plan-v51 / the
repo worklog / session_121) reviewed; the v51 state verified: the
`zb-auth-mode` class on the verify branch's container
(login-card.tsx:614), the `.zb-auth-mode`/`.zb-sm6` rules in
globals.css, the 241 e2e, .env `file:../db/custom.db` with db/ at
the repo root, the sitemap/robots pair, .env ≡ .env.example.

**Step 1 — the baseline chain.** lint ✓ · typecheck ✓ · 108/108 unit
✓ · build ✓ (robots + sitemap prerendered) · **241/241 e2e ✓ (5.5m —
clean on the FIRST run, no flakes)** · 35/35 smoke ✓. The audit: npm
audit = 0 production vulnerabilities (the same 5 dev-only
ESLint-chain advisories); `.env` ≡ `.env.example` (modulo the dev
AUTH_SECRET).

**Step 2 — the 46th standing checks.** Reference side
(`ref-standing-v49.sh`, re-run verbatim — the first run hit a cold
start: the login form hadn't rendered at the 3s settle, "already
logged in?" — the re-run on the warm session submitted clean): all
four bugs live — the toast-blocker (the hit `DIV.fixed top-0
z-[100]`, hitIsBurgerChild false), the sheet-trap (the overlayCount
census: `sheetOpenAfterNav false, overlayCount 1` — the z-50 scrim
remains on /income after the nav click), no nav landmark, the
/networth 464 overflow; the data census read-only ("1 items ·
$25,000" networth / "1 items · $5000.00" income — intact); the SEO
pair live. Clone side (`clone-stand47.sh` via with-server): **R1
read `sheetLinks: 0` — INVESTIGATED, not dismissed: the script's
`button[aria-label="Open menu"]` selector is the REFERENCE's DOM
idiom; the clone's burger carries no aria-label (its accessible
name rides the sr-only "Toggle Sidebar" span — the v7 idiom) so the
click failed SILENTLY (the `|| true` masked it).** The mobile nav
itself verified WORKING via a follow-up eval-flow: the burger click
opens the 5-link sheet (R1 semantics green), the Income nav
navigates to /income AND the sheet closes + the overlay clears (R2
green), the Escape key closes the sheet (the superset), R3/R4/SEO
green — the 7 mobile-navigation e2e tests all pass (the 241/241
run). The script's selector is the v52 P1 fix (a scripts/ change).

**Step 3 — the v52 sweep.** The probe pair
(`scripts/parity-probes/ref-v52.sh` + `clone-v52.sh`, READ-ONLY on
the reference): (1) the /INCOME view at 390 — the header row
358×112 (flex-col/gap 16/mb 32/align-start), the 48×48 radius-12
lime-gradient chip, the H1 30/700/forest, the sub 16/400/gray, the
Add button 147×36 (radius 6, the lime gradient, 14/500, pad 8 16),
the filter card 358/radius 16/pad 24/white/border/mb 24, the inner
grid 1-col 308/gap 16/3 children at the y rhythm 246/298/350, the
search 308×36/pad 4 12 4 40, the item grid 1-col/gap 16, the first
card radius 12/pad 20/the rgba(0,0,0,0.04) 0px 2px 8px shadow, the
H4 16/600/forest, the amount 16/400/rgb(10,10,10), docSW 390 —
BYTE-PARITY (the count/total and the card heights are the seed's
data class); (2) the /EXPENSES view at 390 — the same family + the
155×36 orange-gradient Add button + the filter's 4-children/
3-trigger inner grid — BYTE-PARITY; (3) the ITEM-DETAILS sheet's
internals at 390 (opened via the read-only card-body click) — **ONE
REAL GAP: the summary's missing SUBCATEGORY P.** The reference
renders FIVE summary elements (the chip row → the H3 name
`text-2xl font-bold mb-2` 24/700/forest → **the SUBCATEGORY P
`text-lg` 18/400/rgb(107,114,128)** → the amount P `text-4xl
font-bold mt-4` 36/700/type-color) — Rent → "Apartment", Salary →
"Main Job" — while the clone rendered FOUR (the H3 → the amount
directly). The `subcategory` field was always on the clone's model
(the card renders it at item-card.tsx:125, the edit dialog edits it
at budget-item-dialog.tsx:256); the details view never wired it.
The sheet's OTHER internals: byte-parity (the sticky header h 69,
the title 18/700, the 36×36 close, the body space-y-6 p-6, the
classification block, the facts, the meta footer). Probe lessons:
the reference session EXPIRES between long eval gaps (re-login via
the eval); the viewport state does NOT survive a session restart
(re-apply 390 before any mobile census — a post-restart census read
the desktop 4-col filter grid at "215.5px" tracks); the reference's
sheet has NO [role=dialog] (the no-landmark family — find it via
the `fixed inset-0 z-50` overlay class); the summary is a TWO-LEVEL
title structure (the H3 + the P — walk the full subtree, a leaf-only
census misses the siblings).

**Step 4 — the trap-log scan.** The systematic Tailwind v4 audit
(the space-y × negative-margin scan across all 39 components):
CLEAN — only two `-mb-` utilities live in src/ (the auth back
buttons at login-card.tsx:617 and :714), both inside their converted
`zb-auth-mode` containers (the v50 + v51 fixes). No un-converted
trap site remains.

**Step 5 — the remediation plan v52** written +
pre-execution-validated (the F1 insertion point at
item-details-dialog.tsx:173-177; `rgb` already imported; the panel
stays capped at its 85vh max-height — the v28 mobile geometry test
and the v48 shadow census ride the cap, unaffected by the body's
+27px; the v28 summary assertions walk the H3's role and the
amount's class — the new P adds only a text node).

**Step 6 — the TDD cycle.** F1 RED: the subcategory-P pin written
and run against the unfixed build — **RED CONFIRMED** (the P does
not exist; the F4 internals test alongside it GREEN immediately —
pin-only, modulo two pin transcription fixes: the chip row's gap is
gap-2 8px not 12px [conflated with the facts' gap-3], and
rounded-full computes 3.35544e+07px on v4 vs the reference's 9999px
— the class is the pinned contract]). The one-insert fix
(`item.subcategory ? <p className="text-lg" style={{ color:
rgb.gray }}>{item.subcategory}</p> : null` between the H3 and the
amount, with the explaining comment). The chain-gate catch: the
first rebuild FAILED on TS18047/TS2345 (the new items.spec.ts
census code's `h1.closest()` null-safety — Playwright does NOT
typecheck but `next build`'s tsc does; the third application of the
v51 lesson) — fixed with explicit null guards. GREEN: **all four
v52 tests pass** (F1 + F2 + F3 + F4).

**Step 7 — the mutation-sanity series** (each with the standalone
REBUILD): (a) the subcategory P removed → F1 FAILS (the TDD RED run
— the pre-fix proof); (b) the income chip's inline gradient removed
→ F2 FAILS; (c) the filter card's `p-6` → `p-4` → F2 AND F3 FAIL;
(d) the details header's `py-4` → `py-2` → F4 FAILS (the header
69 → 53); (e) the H1's `text-3xl` → `text-2xl` → F2 AND F3 FAIL (fs
30 → 24). All restored — the clean diff: item-details-dialog.tsx
+17 (the insert + the comment) + the two specs.

**Step 8 — the full chain.** lint ✓ · typecheck ✓ · 108 unit ✓ ·
build ✓ · **245/245 e2e ✓ (5.5m — clean on the FIRST run)** · 35/35
smoke ✓. The VLM pair (the /expenses view at 390 — THE F3 SURFACE):
4 flagged diffs — the header count/total, the card contents, the
"Edit with Base44" FAB (the VLM mislabeled which image carries it —
the FAB is the reference's own platform chrome), the layout length
— ALL DOM-verified as the documented seed-data/platform classes
(the v47/v48 precedents; the chrome byte-pinned by F3).

**Step 9 — the deliverables.** The P1 probe-infra fix applied +
verified (the standing script's R1 now reads "burger clicked" +
sheetLinks: 5; R2 /income + closed). The 16 screenshots regenerated
(ONE byte-diff: 16-item-details.png — the F1 fix's visual effect;
the other 15 byte-identical). The .env.example re-checked (≡ .env).

**Step 10 — the docs + the ship.** AGENTS (the v52 paragraph) /
CLAUDE (the 245 count + the v52 entries) / README (the v52 row + the
245 counts) / PAD (the v1.1.9 revision block) / the SKILL doc (the
Session 87 row + the state line) / the probe README (the v52
section) / session_122.md + session_123.md / the repo worklog
Session 86 + the ledger list / the workspace worklog. Commit + push
to main via the SSH wrapper.
