# ZeroBalance — Project Worklog

Rolling log of the engineering sessions on this repo, newest first. Each
session's detailed narrative lives in `docs/session_<n>.md`; findings ledgers
live in `docs/remediation-plan.md` (v1), `docs/remediation-plan-v2.md`,
`docs/remediation-plan-v3.md`, `docs/remediation-plan-v4.md`,
`docs/remediation-plan-v5.md`, `docs/remediation-plan-v6.md`,
`docs/remediation-plan-v7.md`, `docs/remediation-plan-v8.md`,
`docs/remediation-plan-v9.md`, `docs/remediation-plan-v10.md`,
`docs/remediation-plan-v11.md`, `docs/remediation-plan-v12.md`,
`docs/remediation-plan-v13.md`, `docs/remediation-plan-v14.md`,
`docs/remediation-plan-v15.md`, `docs/remediation-plan-v16.md`,
`docs/remediation-plan-v17.md`, `docs/remediation-plan-v18.md`,
`docs/remediation-plan-v19.md`, `docs/remediation-plan-v20.md`,
`docs/remediation-plan-v21.md`, `docs/remediation-plan-v22.md`,
`docs/remediation-plan-v23.md`, `docs/remediation-plan-v24.md`,
and `docs/remediation-plan-v25.md`,
and `docs/remediation-plan-v26.md`,
and `docs/remediation-plan-v27.md`,
and `docs/remediation-plan-v28.md`,
and `docs/remediation-plan-v29.md`,
and `docs/remediation-plan-v30.md`,
and `docs/remediation-plan-v31.md`,
and `docs/remediation-plan-v32.md`,
and `docs/remediation-plan-v33.md`,
and `docs/remediation-plan-v34.md`,
and `docs/remediation-plan-v35.md`,
and `docs/remediation-plan-v36.md`,
and `docs/remediation-plan-v37.md`,
and `docs/remediation-plan-v38.md`,
and `docs/remediation-plan-v39.md`,
and `docs/remediation-plan-v40.md`,
and `docs/remediation-plan-v41.md`,
and `docs/remediation-plan-v42.md`,
and `docs/remediation-plan-v43.md`,
and `docs/remediation-plan-v44.md`,
and `docs/remediation-plan-v45.md`,
and `docs/remediation-plan-v46.md`,
and `docs/remediation-plan-v47.md`,
and `docs/remediation-plan-v48.md`,
and `docs/remediation-plan-v49.md`,
and `docs/remediation-plan-v50.md`,
and `docs/remediation-plan-v51.md`,
and `docs/remediation-plan-v52.md`,
and `docs/remediation-plan-v53.md`,
and `docs/remediation-plan-v54.md`,
and `docs/remediation-plan-v55.md`,
and `docs/remediation-plan-v56.md`,
and `docs/remediation-plan-v57.md`,
and `docs/remediation-plan-v58.md`,
and `docs/remediation-plan-v59.md`,
and `docs/remediation-plan-v60.md`,
and `docs/remediation-plan-v61.md`,
and `docs/remediation-plan-v62.md`,
and `docs/remediation-plan-v63.md`,
and `docs/remediation-plan-v64.md`,
and `docs/remediation-plan-v65.md`,
and `docs/remediation-plan-v66.md`,
and `docs/remediation-plan-v67.md`,
and `docs/remediation-plan-v68.md`,
and `docs/remediation-plan-v69.md`,
and `docs/remediation-plan-v70.md`,
and `docs/remediation-plan-v71.md`,
and `docs/remediation-plan-v72.md`,
and `docs/remediation-plan-v73.md`,
and `docs/remediation-plan-v74.md`,
and `docs/remediation-plan-v75.md`,
and `docs/remediation-plan-v76.md`,
and `docs/remediation-plan-v77.md`,
and `docs/remediation-plan-v78.md`,
and `docs/remediation-plan-v79.md`,
and `docs/remediation-plan-v80.md`,
and `docs/remediation-plan-v81.md`,
and `docs/remediation-plan-v82.md`,
and `docs/remediation-plan-v83.md`,
and `docs/remediation-plan-v84.md`,
and `docs/remediation-plan-v85.md`,
and `docs/remediation-plan-v86.md`,
and `docs/remediation-plan-v87.md`,
and `docs/remediation-plan-v88.md`,
and `docs/remediation-plan-v89.md`,
and `docs/remediation-plan-v90.md`,
and `docs/remediation-plan-v91.md`,
and `docs/remediation-plan-v92.md`,
and `docs/remediation-plan-v93.md`,
and `docs/remediation-plan-v94.md`,
and `docs/remediation-plan-v95.md`,
and `docs/remediation-plan-v96.md`.

---

## Session 133 — Parity iteration v98: the re-run cycle's next-oldest candidate (the v92-era SAVINGS pair's sixth re-run) + the axe watch (NO DRIFT) + the goal-card action-menu panel/menuitem-resting census pin (PIN-ONLY) (2026-10-20)

**The cycle** (`docs/remediation-plan-v98.md` — the plan validated against the codebase before execution; the narrative: `docs/session_236.md`): the re-run cadence's next-oldest candidate — the v92-era SAVINGS pair (the SAVINGS view at desktop 1280x800, full-page, last re-shot v92 — now the oldest remaining [v92 < v93 < v94 < v95 < v96 < v97]; the pair's SIXTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98]; the TWENTY-FIRST consecutive queue/ledger agreement, the surface names verified against vlm-shots-v92.sh's own header before the derivation) + the axe-core watch at its re-check point + the 92nd standing checks. PIN-ONLY for src/ — no production-code change; +1 e2e = 301.

**The baseline — the FRESH-CLONE workspace** (the sandbox reset — the v86/v88/v90/v91/v92 precedent): git clone at main @ 9152c18, the tree clean; the environment re-provisioned (npm install; `.env` written [DATABASE_URL="file:../db/custom.db"]; `db/` at the repo root, db:generate + db:push + db:seed; chromium-1243 installed for the pinned @playwright/test 1.63.0 — the cache's pre-installed 1200 build belongs to a different playwright generation, the first e2e chunk failed with "Executable doesn't exist" until the install; the `/home/z/my-project/tool-results/` dir re-created for with-server.sh); the seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran; lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · **300 e2e ✓** (135+96+71 = 302 chunk executions = 300 unique, zero flakes on the first run) · 35/35 smoke ✓. The codebase audit clean (the two commits since the v97 push 6a6725c [d4b77c5 + 9152c18] verified session-log-only [docs/session_234.md + docs/session_235.md — ZERO src/ or lockfile deltas]; the production seams re-audited — auth, db-path [the sandbox's polluted parent DATABASE_URL re-confirming the env -u discipline], the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout).

**F1 the axe-core watch: NO DRIFT** — npm-latest 4.14.0 (only rc/next sha prereleases beyond — no stable 4.14.1, no 5.x); the installed wrapper + engine both 4.14.0; the v68 dedupe holds; the engine-contract pin 2 passed standalone.

**F2 the 92nd standing checks: ALL GREEN** (ref-standing-v92.sh + standing-checks-v92.sh, derived from the v91 pair via the PERSISTED derive-standing-v98.py across the three token families, version-bump-only verified by the normalize-back diff): the reference's four bugs ALL live (toast-blocker / sheet-trap `overlayCount:1` after nav / no-landmark / the 464px /networth overflow measured docSW 464 directly); the data census the 92nd clean drift check — UNCHANGED on the FIRST read (networth "1 items · $25,000" / income "1 items · $5000.00" / expenses "4 items · $525.00" — no render-race this cycle; the v97 generalization held in the clean direction); the SEO pair live both sides. Clone side: R1–R4 ALL GREEN — **the mobile menu VERIFIED WORKING the 92nd consecutive time** (hitIsBurgerChild:true, the sheet opens, closes on nav, the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

**F3 the re-run pair** (vlm-shots-v98.sh + clone-vlmshots-v98.sh + vlm-compare-v98.mjs + arbit-v98.sh — the derivation from the v92 lineage via the PERSISTED derive-v98-series.py: the generic swaps + the exact-fragment history corrections [last-re-shot v86 → v92, FIFTH → SIXTH, the bracket extension, the oldest-remaining bracket, the agreement ordinal FIFTEENTH → TWENTY-FIRST, the suggesting plan v91 → v97], every correction's hit/miss REPORTED by the script itself — the one first-run MISS [the arbit header's line break] caught by the report and fixed before any probe executed; the two-half census BUILT two-half from the start via build-twohalf-v98.py — the ONE SV_CENSUS_JS block [153 lines] byte-identical across the halves by the md5 line-block contract [31d181ed]; the reaping budget applied as the standing step; login on the first attempt both sides; the parked pointer at (5,5); read-only — the v46 rule holds): **the verdict DIFFERENT, every flag DOM-arbitrated to a documented class** — the "Card Footer Alignment" the v57 DATA-CONDITIONAL class (the census proving the footer childCount 1-vs-2 with the clone's "Brokerage" chip — the reference RENDERS payment chips when data carries them per the v97 income-card evidence; its savings item simply ships no payment method); the card grid the seed-count class (1 vs 2); the header subtitle + card contents the seed-data classes; the avatar the user-identity class; no FAB flag this cycle. The census **REPRODUCES the v86/v92 census values EXACTLY: zero drift on every axis** (the h1/grid/card/cardTitle/titleRow/cardAmount/footer/badge families; the docSW 1280 guard; the clone template's last-column sub-pixel the documented column-distribution rounding noise WITHIN the 309.328px family). **NO NEW CLONE GAP.**

**F4 the +1 e2e pin (300 → 301): the goal-card ACTION-MENU PANEL + MENUITEM-RESTING interior census at 1280** (tests/e2e/items.spec.ts — the v97 missing-middle lesson applied to the ACTION layer: the tokens G5/G9 pins hold the menu ITEM's COLOR family + the CONTENT's border-COLOR on the income view, the v35 S1 pin the keyboard contract — but the menu PANEL's GEOMETRY [bg/radius/shadow/min-w/overflow/z/w/h] and the menuitem's RESTING interior [fs/fw/pad/radius/lh/h] were NEVER pinned at ANY viewport in ANY spec — the coverage-map grep across all 24 specs; + the panel {bg white, radius 6px, border 1px rgb(229,229,229), minW 128px, overflow hidden, z 50, pos static, w 128, h 74} + the shadow-md VISIBLE layers via toContain [the v37 O1 v3/v4-construct precedent] + the item0 {fs 14px, fw 400, color rgb(10,10,10), pad 6px 8px, radius 4px, lh 20px, h 32} + the itemCount 2 + the docSW 1280 guard — the panel w/h + itemCount DATA-INDEPENDENT [the structural Edit+Delete pair: 2×32 + 2×4 pad + 2×1 border = 74], so unlike the v97 pin's clone-only guards these axes assert the cross-side-verified values directly; the pin's own axes first measured byte-identical on BOTH sides by the supplemental two-half census menu-arbit-v98.sh + menu-clone-v98.sh via build-menu-v98.py, the census JS byte-identical by the md5 line-block diff 0f83b786; both sides read-only [a menu OPEN only, no item clicks]; the seedcheck exact after the run; **the census's TWO discoveries: the reference's action trigger is UNLABELLED (the clone's "Actions for …" aria-label is the a11y superset — the v38 search-input note's sibling — so the cross-side finder is GEOMETRIC [the textless 36×36 svg button]) AND the reference's menu opens only on the full POINTER EVENT SEQUENCE (pointerdown → mousedown → pointerup → mouseup → click — a bare el.click() opens the clone's Radix menu but NOT the reference's)**) — GREEN on first run. **The pin-sanity mutation (the executed form)**: the DropdownMenuContent panel's `rounded-md` → `rounded-lg` (src/components/ui/dropdown-menu.tsx:20, by LINE NUMBER — the line-scoping keeps the DropdownMenuItem's own `rounded-sm` at line 36 untouched [the item's 4px radius axis]): the first mutation run read 43 GREEN — **the mutation had NOT bitten (the e2e runs the PREBUILT standalone server — the rebuild-then-test discipline: a mutation only bites after the standalone REBUILD)**; after the rebuild, ONLY the v98 pin red (42 green under the mutation), the failure diff reads as the panel radius axis ALONE ("6px" → "8px") — cascade-free BY CONSTRUCTION (no spec asserts any dropdown-menu panel radius — this pin is the first; the v97 listbox panel radius 6px reads select.tsx's SelectContent, a DIFFERENT component; the tokens G5 contentBorder is the border-COLOR axis, not radius) — then restored (git diff src/ = 0 lines; the standalone REBUILD via the FULL npm run build; the post-restore full run 43/43 green).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **301 e2e** (136+96+71 = 303 chunk executions = 301 unique tests, zero flakes) · 35/35 smoke ✓; the screenshots **10/16 BYTE-IDENTICAL + 6/16 the fresh-reseed DATE class** (the fresh-clone re-seed re-anchoring the seed's isoDate offsets to the new seed day — db/ is gitignored, it does not travel; every differing region pixel-arbitrated by pixel-diff-v98.py: 03-income 2 date spans, 04-expenses 3, 05-savings 2, 06-networth 1, 16-item-details 1 date span + two max-channel-2 sub-perceptual re-render regions, 08-calculator one 77×77 max-channel-2 region — the v68 calculator precedent, below the ~2.5 JND; the VLM crop re-read over-read the sub-threshold noise as a "missing border" — the measurement is the authority, the v43 rule); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v98 paragraph), D2 CLAUDE.md (300 → 301 + the v98 clause at the E2E line's tail), D3 README.md (the counts + the plan-table row), D4 zero-balance_SKILL.md (Session 133 audit row + the state line), D5 the PAD's v1.1.55 revision block, D6 the probe README's v98 section (the reference pointer-event family + the unlabelled-trigger finder class + the data-independent panel + the mutation-rebuild discipline + the v99 queue), D7 session_236.md + this Session 133 entry.

**The next queue:** the v99 cycle — the v93-era LOGIN + CALCULATOR pair (the login view + the calculator card pair at desktop 1280x800, last re-shot v93 — now the oldest remaining [v93 < v94 < v95 < v96 < v97 < v98]); verify against vlm-shots-v93.sh's own header first, per protocol.

---

## Session 132 — Parity iteration v97: the re-run cycle's next-oldest candidate (the v91-era ITEMS pair's sixth re-run) + the axe watch (NO DRIFT) + the filter-listbox panel/option-interior census pin (PIN-ONLY) (2026-10-20)

**The cycle** (`docs/remediation-plan-v97.md` — the plan validated against the codebase before execution; the narrative: `docs/session_233.md`): the re-run cadence's next-oldest candidate — the v91-era ITEMS pair (the INCOME + EXPENSES view pair at desktop 1280x800, full-page, last re-shot v91 — now the oldest remaining [v91 < v92 < v93 < v94 < v95 < v96]; the pair's SIXTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97]; the TWENTIETH consecutive queue/ledger agreement, the surface names verified against vlm-shots-v91.sh's own header before the derivation) + the axe-core watch at its re-check point + the 91st standing checks. PIN-ONLY for src/ — no production-code change; +1 e2e = 300.

**The baseline — the CARRIED-OVER workspace** (the session-log-only commit class): `git pull` to main @ 27c5970 (the two commits since the v96 push 90f766e — 59e7d14 + 27c5970 — verified session-log-only [docs/session_231.md + docs/session_232.md], ZERO src/ or lockfile deltas, so the v96 cycle's own environment carries over unchanged, no re-provisioning); the seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran; lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · **299 e2e ✓** (134+96+71 = 301 chunk executions = 299 unique, zero flakes on the first run) · 35/35 smoke ✓. The codebase audit clean (the production seams re-audited — auth, db-path [the sandbox's polluted parent DATABASE_URL re-confirming the env -u discipline], the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout).

**F1 the axe-core watch: NO DRIFT** — npm-latest 4.14.0 (only rc/next sha prereleases beyond — no stable 4.14.1, no 5.x); the installed wrapper + engine both 4.14.0; the v68 dedupe holds; the engine-contract pin 2 passed standalone.

**F2 the 91st standing checks: ALL GREEN** (ref-standing-v91.sh + standing-checks-v91.sh, derived from the v90 pair via the PERSISTED derive-standing-v97.py across the three token families, version-bump-only verified by the normalize-back diff): the reference's four bugs ALL live (toast-blocker / sheet-trap / no-landmark / the 464px /networth overflow measured directly by the settle-wait form); the data census the 91st clean drift check — **the expenses leg first read "no match": THE RENDER-RACE ARTIFACT** (the eval raced the page's client-side render; the settle-wait re-read after a fresh login measured the exact documented "4 items · $525.00" — the CENSUS RENDER-RACE GENERALIZATION: ANY multi-eval reference flow treats a "no match"/empty census as a possible expiry OR render race first, never recording the state change on a single raced read); the SEO pair live both sides. Clone side: R1–R4 ALL GREEN — **the mobile menu VERIFIED WORKING the 91st consecutive time** (hitIsBurgerChild:true, the sheet opens, closes on nav, the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

**F3 the re-run pair** (vlm-shots-v97.sh + clone-vlmshots-v97.sh + vlm-compare-v97.mjs + arbit-v97.sh — the derivation from the v91 lineage via the PERSISTED derive-v97-series.py: the generic swaps + the exact-fragment history corrections [last-re-shot v85 → v91, FIFTH → SIXTH, the bracket extension, the every-other-pair list], every correction's hit/miss REPORTED by the script itself — all four applied clean on the first run; the two-half census BUILT two-half from the start via build-twohalf-v97.py — the ONE CENSUS_JS block [193 lines] byte-identical across the halves by the md5 line-block contract [b55dcd29]; the reaping budget applied as the standing step; login on the first attempt both sides; the parked pointer at (5,5); read-only — the v46 rule holds): **BOTH verdicts DIFFERENT (the pair's documented verdict class), every flag DOM-arbitrated to a documented class** — the avatar the user-identity class; the stats/grids/card contents the seed-data classes; **the payment-method footer chips the v57 DATA-CONDITIONAL class — PROVEN by the reference's own income card's footer childCount 2 with the "Bank Account" chip while its expense items ship none** (footer childCount 1); **the badge wrap + the card h 200-vs-230 the v57/v70b Recurring-wrap class** (the superset Recurring badge wraps → badgeRow h 52 [22+8+22] → +30px + the 1-row sibling stretch); **the "Edit with Base44" FAB the platform-chrome class, re-arbitrated live** by base44-fab-arbit-v97.sh (fabCount 0 + bodyHasBase44 false on BOTH sides — the FAB renders in the reference's platform iframe chrome; this cycle the VLM attributed it to the reference — the non-inverted form of the v85/v91-documented attribution class). The census **REPRODUCES the v85/v91 census values EXACTLY: zero drift on every axis** (the avatar/grid/card/titleRow/amount/footer/badge/filterCard families; the docSW 1280 guard; the income template's last-column sub-pixel the column-distribution rounding noise WITHIN the documented 309.328px family). **NO NEW CLONE GAP.**

**F4 the +1 e2e pin (299 → 300): the filter LISTBOX PANEL + OPTION-RESTING interior census at 1280** (tests/e2e/items.spec.ts — **the MISSING-MIDDLE family**: the family-extension survey walking the filter select's COMPONENT LAYERS [trigger → panel → viewport → option] — the v91 pin holds the TRIGGER's resting chrome, the v36 S2 the OPTION's focus-state family, but the PANEL container itself [bg/radius/border/shadow/max-h/overflow/z + the viewport's 4px pad] and the option's RESTING interior [fs/fw/color/pad/radius/h] were NEVER pinned at ANY viewport in ANY spec — the coverage-map grep across all 24 specs; + the panel {bg white, radius 6px, border 1px rgb(229,229,229), maxH 384px, overflow hidden, z 50, pos relative, w 218} + the shadow-md VISIBLE layers via toContain [the v37 O1 v3/v4-construct precedent — the zero-layer lead count 2-vs-4 the documented class] + the viewport {pad 4px, display block} + the opt0 {fs 14px, fw 400, color rgb(23,23,23), pad 6px 32px 6px 8px, radius 4px, h 32} + the clone's own data-dependent guards [panel h 106, optCount 3] + the docSW 1280 guard; the pin's own axes first measured byte-identical on BOTH sides by the supplemental two-half census listbox-arbit-v97.sh + listbox-clone-v97.sh via build-listbox-v97.py, the census JS byte-identical by the md5 line-block diff 34c916da; both sides read-only; the seedcheck exact after the run]) — GREEN on first run. **The pin-sanity mutation (the executed form)**: the SelectContent panel's `rounded-md` → `rounded-lg` (src/components/ui/select.tsx:68, by LINE NUMBER — the line-scoping keeps the SelectTrigger's own `rounded-md` at line 19 untouched [the v91 pin's 6px trigger axis]): ONLY the v97 pin red (41 green under the mutation), the failure diff reads as the panel radius axis ALONE ("6px" → "8px") — cascade-free BY CONSTRUCTION (no spec asserts any listbox panel radius — this pin is the first; the calculator's panel.radius 16px is the calculator DIALOG panel, a different element; the radius changes no other axis) — then restored (git diff src/ = 0 lines; the standalone REBUILD via the FULL npm run build; the post-restore full run 42/42 green).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **300 e2e** (135+96+71 = 302 chunk executions = 300 unique tests, zero flakes) · 35/35 smoke ✓; the screenshots **16/16 BYTE-IDENTICAL** (the same-day regeneration — both sides Oct 20 UTC, the 07-add-item-modal's day digits matching, no midnight crossing this cycle); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v97 paragraph), D2 CLAUDE.md (299 → 300 + the v97 clause at the E2E line's tail), D3 README.md (the counts + the v97 plan-table row), D4 zero-balance_SKILL.md (Session 132 audit row + the state line), D5 the PAD's v1.1.54 revision block, D6 the probe README's v97 section (the census render-race generalization + the panel-chrome missing-middle family + the v98 queue), D7 session_233.md + this Session 132 entry.

**The next queue:** the v98 cycle — the v92-era SAVINGS pair (the SAVINGS view + the goal-card interior pair at desktop 1280x800, last re-shot v92 — now the oldest remaining [v92 < v93 < v94 < v95 < v96 < v97]); verify against vlm-shots-v92.sh's own header first, per protocol.

---

## Session 131 — Parity iteration v96: the re-run cycle's next-oldest candidate (the v90-era MOBILE 390 twins' fifth re-run) + the axe watch (NO DRIFT) + the head-row typography/figure-fit census pin (PIN-ONLY) (2026-10-20)

**The cycle** (`docs/remediation-plan-v96.md` — the plan validated against the codebase before execution; the narrative: `docs/session_230.md`): the re-run cadence's next-oldest candidate — the v90-era MOBILE 390 twins (the /NETWORTH view + the DASHBOARD FULL-PAGE pair at 390x844, last re-shot v90 — now the oldest remaining [v90 < v91 < v92 < v93 < v94 < v95]; the pair's FIFTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96]; the NINETEENTH consecutive queue/ledger agreement, the surface names verified against vlm-shots-v90.sh's own header before the derivation) + the axe-core watch at its re-check point + the 90th standing checks. PIN-ONLY for src/ — no production-code change; +1 e2e = 299.

**The baseline — the CARRIED-OVER workspace** (the session-log-only commit class): `git pull` to main @ 2b0bb52 (the docs-only session-log commit [docs/session_229.md, 99 insertions] — ZERO src/ or lockfile deltas since the v95 push 7a1ce9a, so the v95 cycle's own fresh-clone environment carries over unchanged, no re-provisioning); the seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran; lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · **298 e2e ✓** (139+100+61 = 300 chunk executions = 298 unique, zero flakes on the first run) · 35/35 smoke ✓. The codebase audit clean (the v95 commit verified PIN-ONLY as documented; the production seams re-audited — auth, db-path, the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout).

**F1 the axe-core watch: NO DRIFT** — npm-latest 4.14.0 (only sha prereleases beyond — no stable, no 5.x); the installed wrapper + engine both 4.14.0; the v68 dedupe holds; the engine-contract pin 2 passed standalone.

**F2 the 90th standing checks: ALL GREEN** (ref-standing-v90.sh + standing-checks-v90.sh, derived from the v89 pair via the PERSISTED derive-standing-v96.py across the three token families, version-bump-only verified by the normalize-back diff): the reference's four bugs ALL live (toast-blocker / sheet-trap / no-landmark / the 464px /networth overflow — **the overflow re-verified with the settle-wait after the script's sleep-3 raced the reference's client-side boot and read the PRE-RENDER document [390/390]; the 8s+2s re-read measured the true 464 — the standing-script timing artifact lesson**); the data census the 90th clean drift check; the SEO pair live both sides. Clone side: R1–R4 ALL GREEN — **the mobile menu VERIFIED WORKING the 90th consecutive time** (hitIsBurgerChild:true, the sheet opens, closes on nav, the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

**F3 the re-run pair** (vlm-shots-v96.sh + clone-vlmshots-v96.sh + vlm-compare-v96.mjs + arbit-v96.sh — the derivation from the v90 lineage via the PERSISTED derive-v96-series.py: the generic swaps + the exact-fragment history corrections, every correction's hit/miss REPORTED by the script itself [the derivation miss-report discipline — the one first-run MISS caught and fixed before any probe executed]; the two-half census BUILT two-half from the start via build-twohalf-v96.py — the NW/DASH census blocks byte-identical across the halves by the md5 line-block contract [82cf8a43 / 85e4ec7e]; the reaping budget applied as the standing step; login on the first attempt both sides; the parked pointer at (5,5); read-only — the v46 rule holds): **BOTH verdicts DIFFERENT (the pair's documented verdict class — same as v84/v90), every flag DOM-arbitrated to a documented class** — the stat-tile stacking the v41 mobile-superset class; the subtitle wrap-point the v62 width-delta class; the FAB the platform-chrome class; the figures/donut the seed-data classes; **the NEW clipped-figure flag ("-$245,950.00 clipped on the left") DOM-arbitrated as a VLM MISREAD** (figclip-clone-v96.sh: the textRect flush at the content-left [textLeftOfContent 0 — zero overhang] and 115px inside the content-right, figureScrolls false, docSW 390 — the figure fully in-bounds; the FLUSH-LEFT FIGURE PERCEPTION CLASS new this cycle). The census **REPRODUCES the v90 census values EXACTLY: zero drift on every axis** (the summary card/statGrid/tiles/medallion/trendIcon families; the subtitle chrome; the breakdown card's svg family; the children heights; the spendingCard finder reading the SAME fallback string on both sides — the heading is a div on both sites). **NO NEW CLONE GAP.**

**F4 the +1 e2e pin (298 → 299): the summary-card HEAD-ROW typography + FIGURE-FIT census at 390** (tests/e2e/networth.spec.ts — the FAMILY-EXTENSION pattern: the figure's fw + color pinned at 640/1280 but NEVER at 390 [the v41 F3 pin holds the fs only]; the label's family pinned at 1280 only; the figure's FIT contract never pinned at ANY viewport — the flush-left start, the in-bounds right, the no-scroll state; + the figure {fs 24px, fw 700, color white, lh 32px} + the label {fs 14px, fw 400, color rgba(255,255,255,0.8), mb 8px, h 20} + the card box re-affirm + the docSW 390 guard; the pin's own axes first measured byte-identical on BOTH sides by the supplemental two-half census [headrow-arbit-v96.sh + headrow-clone-v96.sh via build-headrow-v96.py, the census JS byte-identical by the md5 line-block diff 519ef222; both sides read-only; the seedcheck exact after the run]) — GREEN on first run. **The pin-sanity mutation (the executed form)**: the figure's `font-bold` → `font-bold max-sm:font-extrabold` (net-worth-view.tsx:348, by LINE NUMBER — the line-scoping keeps the stat-tile VALUE's identical class string at line 372 untouched; AT-max-sm because the pin runs at 390 and the variant is INERT at ≥640 — the v90 LESSON APPLIED, the 640/1280-tier pins stay green): ONLY the v96 pin red (30 green under the mutation), the failure diff reads as the figure fw axis ALONE ("700" → "800") — cascade-free BY CONSTRUCTION (font-weight never changes line-height — the card-height arithmetic [421, the v63 F3 pin] unchanged; font-weight never affects color; max-sm: appears NOWHERE in src/) — then restored (git diff src/ = 0 lines; the standalone REBUILD via the FULL npm run build; the post-restore full run 31/31 green).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **299 e2e** (140+100+61 = 301 chunk executions = 299 unique tests, zero flakes) · 35/35 smoke ✓; the screenshots **15/16 BYTE-IDENTICAL + 1/16 the DATE class** (the cycle crosses the UTC midnight boundary — the 07-add-item-modal's day digits "19"→"20" rolled [the budget-item-dialog's render-time default date todayIso(), line 83, the mechanism]; the pixel-diff-v96.py arbitration localizing the delta to a 32×22px region at x1535 — exactly the two day digits, the v75 acceptance form; everything else byte-stable); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v96 paragraph), D2 CLAUDE.md (298 → 299 + the v96 clause at the E2E line's tail), D3 README.md (the counts + the v96 plan-table row), D4 zero-balance_SKILL.md (Session 131 audit row + the state line + the last_updated date), D5 the PAD's v1.1.53 revision block, D6 the probe README's v96 section (the standing-script timing artifact lesson + the flush-left figure perception class + the derivation miss-report discipline + the DATE-class arbitration record + the v97 queue), D7 session_230.md + this Session 131 entry.

**The next queue:** the v97 cycle — the v91-era ITEMS pair (the INCOME + EXPENSES view pair at desktop 1280x800, last re-shot v91 — now the oldest remaining [v91 < v92 < v93 < v94 < v95 < v96]; the pair's SIXTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97]); verify against the rotation ledger first, per protocol.

---

## Session 130 — Parity iteration v95: the re-run cycle's next-oldest candidate (the v89-era dashboard pair's fifth re-run) + the axe watch (NO DRIFT) + the quick-action transition-timing family census pin (PIN-ONLY) (2026-10-19/20)

**The cycle** (`docs/remediation-plan-v95.md` — the plan validated against the codebase before execution; the narrative: `docs/session_228.md`): the re-run cadence's next-oldest candidate — the v89-era DASHBOARD pair (the BUDGET GUIDELINES card + the QUICK-ACTION card row, both below-the-fold surfaces of the dashboard FULL-PAGE at desktop 1280x800, last re-shot v89 — now the oldest remaining [v89 < v90 < v91 < v92 < v93 < v94]; the pair's FIFTH re-run [v61 → v68 → v77 → v83 → v89 → v95]; the EIGHTEENTH consecutive queue/ledger agreement, the surface names verified against vlm-shots-v89.sh's own header before the derivation) + the axe-core watch at its re-check point + the 89th standing checks. PIN-ONLY for src/ — no production-code change; +1 e2e = 298.

**The baseline — a FRESH-CLONE workspace** (the sandbox reset between cycles): `git clone` to main @ e0f99f2 (the session-log-only commit — ZERO src/ or lockfile deltas since the v94 push ca38efa); the environment provisioned from scratch (npm install at the identical lockfile; `.env` with `DATABASE_URL="file:../db/custom.db"`; `db/` at the repo root pushed + seeded; chromium-1243 installed); the seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran; lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · **297 e2e ✓** (106+98+95 = 299 chunk executions = 297 unique, zero flakes on the first run) · 35/35 smoke ✓. The codebase audit clean (the v94 commit verified PIN-ONLY as documented; the production seams re-audited — auth, db-path, the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout).

**F1 the axe-core watch: NO DRIFT** — npm-latest 4.14.0 (only canary prereleases beyond — no stable, no 5.x); the installed wrapper + engine both 4.14.0; the v68 dedupe holds; the engine-contract pin 2 passed standalone.

**F2 the 89th standing checks: ALL GREEN** (ref-standing-v89.sh + standing-checks-v89.sh, version-bumped from the v88 pair across the three token families, version-bump-only verified by the normalize-back diff): the reference's four bugs ALL live (toast-blocker / sheet-trap / no-landmark / the 464px /networth overflow); the data census the 89th clean drift check; the SEO pair live both sides. Clone side: R1–R4 ALL GREEN — **the mobile menu VERIFIED WORKING the 89th consecutive time** (hitIsBurgerChild:true, the sheet opens, closes on nav, the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

**F3 the re-run pair** (vlm-shots-v95.sh + clone-vlmshots-v95.sh + vlm-compare-v95.mjs + arbit-v95.sh — the sed derivation from the v89 lineage with the version + ordinal + agreement-count + second-pass session-name substitutions, the headers history-corrected to the FIFTH re-run, the functional bodies verified version-bump-only by the normalize-back diff; the two-half census BUILT two-half from the start via build-twohalf-v95.py — the ARBIT_G/Q/X census blocks byte-identical across the halves by the md5 line-block contract [b500dd29 / da04e995 / 7a381755]; the reaping budget applied as the standing step; login on the first attempt both sides; the parked pointer at (5,5); read-only — the v46 rule holds): **the verdict IDENTICAL — zero style flags on the pair's own target surfaces** (the THIRD consecutive IDENTICAL for this pair [v83 → v89 → v95]); every VLM flag the documented standing classes (the seed-data figures; the v56 SUPERSET root-URL active-nav highlight; the "Edit with Base44" FAB the platform-chrome class; the avatar "U" vs "D" the user-identity class). The census **REPRODUCES the v89 census values EXACTLY: zero drift on every axis** (PART G the guidelines card + the three tiles — the shadow lead-layer the v66 invisible class; PART Q the quick-action grid + the three cards — the grid mt the v77 mechanism class [rendered gap 340 byte-identical], the label wrapper-catch the v61 lesson; PART X cardBottom 1122/gridTop 1462/gap 340 byte-identical). **NO NEW CLONE GAP.**

**F4 the +1 e2e pin (297 → 298): the quick-action TRANSITION-TIMING family census at 1280** (tests/e2e/dashboard.spec.ts — never pinned at ANY viewport: the three cards' transitionTimingFunction {cubic-bezier(0.4, 0, 0.2, 1)} + transitionDelay {0s} [the v89 pin holds the duration/property only] + the three tinted tiles' transition-transform family {dur 0.2s, timing} + the three plus icons' transition-opacity family {prop opacity, dur 0.15s, timing, delay 0s} + the docSW 1280 guard; the tiles' transitionProperty asserted in the CONTAINS form — **the v95 TAILWIND v4 COMPUTED-FORM class NEW this cycle** [the reference's v3 "transform" vs the clone's v4 "transform, translate, scale, rotate" superset, the rendered behavior identical, documented from live both-sides evidence]; the pin's own axes first measured byte-identical on BOTH sides by the supplemental two-half census [qa-timing-arbit-v95.sh + qa-timing-clone-v95.sh via build-qa-timing-v95.py, the census JS byte-identical by the md5 line-block diff ba296202; both sides read-only; the seedcheck exact after the run]) — GREEN on first run. **The pin-sanity mutation (the executed form)**: the card's `transition-all duration-200` → `transition-all duration-200 lg:ease-linear` (dashboard-view.tsx:885, by LINE NUMBER — the line-scoping keeps the file's OTHER transition-all duration-200 instance [line 578] untouched; AT-lg because the pin runs at 1280): ONLY the v95 pin red (41 green under the mutation), the failure diff reads as the cardTiming axis ALONE ("cubic-bezier(0.4, 0, 0.2, 1)" → "linear") — cascade-free BY CONSTRUCTION (a timing-function flip affects no geometry and no computed style any other pin asserts; lg:ease-linear appears NOWHERE in src/) — then restored (git diff src/ = 0 lines; the standalone REBUILD via the FULL npm run build; the post-restore full run 42/42 green).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **298 e2e** (107+98+95 = 300 chunk executions = 298 unique tests, zero flakes) · 35/35 smoke ✓; the screenshots **16/16 BYTE-IDENTICAL** (the same-day-seed byte-identity law — the third consecutive pure-form cycle, ZERO arbitration needed); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v95 paragraph), D2 CLAUDE.md (297 → 298 + the v95 clause at the E2E line's tail), D3 README.md (the counts + the v95 plan-table row), D4 zero-balance_SKILL.md (Session 130 audit row + the state line), D5 the PAD's v1.1.52 revision block, D6 the probe README's v95 section (the template-brace generator bug lesson + the two-half-form-as-default lesson + the v4 transition-property computed-form class lesson + the v96 queue), D7 session_228.md + this Session 130 entry.

**The next queue:** the v96 cycle — the v90-era MOBILE 390 twins (the /networth + the dashboard FULL-PAGE pair at 390x844, last re-shot v90 — now the oldest remaining [v90 < v91 < v92 < v93 < v94 < v95]; the pair's FIFTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96]); verify against the rotation ledger first, per protocol.

---

## Session 129 — Parity iteration v94: the re-run cycle's next-oldest candidate (the v88-era networth + drill-down pair's fifth re-run) + the axe watch (NO DRIFT) + the networth section-header row census pin (PIN-ONLY) (2026-10-19)

**The cycle** (`docs/remediation-plan-v94.md` — the plan validated against the codebase before execution; the narrative: `docs/session_226.md`): the re-run cadence's next-oldest candidate — the v88-era NETWORTH + DRILL-DOWN pair (the NETWORTH view + the DASHBOARD's drill-down EXPANDED state at desktop 1280x800, full-pair, last re-shot v88 — now the oldest remaining [v88 < v89 < v90 < v91 < v92 < v93]; the pair's FIFTH re-run [v60 → v67 → v76 → v82 → v88 → v94]; the SEVENTEENTH consecutive queue/ledger agreement, the surface names verified against vlm-shots-v88.sh's own header before the derivation) + the axe-core watch at its re-check point + the 88th standing checks. PIN-ONLY for src/ — no production-code change; +1 e2e = 297.

**The baseline — the carried-over workspace (the session-log-only commit class, the second consecutive)**: pulled to main @ 13e1445 (the docs-only session-log commit — ZERO src/ or lockfile deltas since the v93 push 1a2ecb5); the seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran; lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · **296 e2e ✓** (111+105+82 = 298 chunk executions = 296 unique, zero flakes on the first run) · 35/35 smoke ✓. The codebase audit clean (the v93 commit verified PIN-ONLY as documented; the production seams re-audited — auth, db-path, the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout).

**F1 the axe-core watch: NO DRIFT** — npm-latest 4.14.0 (only 4.14.1 sha prereleases beyond — no stable, no 5.x); the installed wrapper + engine both 4.14.0; the v68 dedupe holds; the engine-contract pin 2 passed standalone.

**F2 the 88th standing checks: ALL GREEN** (ref-standing-v88.sh + standing-checks-v88.sh, version-bumped from the v87 pair across the three token families, version-bump-only verified by the normalize-back diff): the reference's four bugs ALL live (toast-blocker / sheet-trap / no-landmark / the 464px /networth overflow); the data census the 88th clean drift check; the SEO pair live both sides. Clone side: R1–R4 ALL GREEN — **the mobile menu VERIFIED WORKING the 88th consecutive time** (hitIsBurgerChild:true, the sheet opens, closes on nav, the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

**F3 the re-run pair** (vlm-shots-v94.sh + clone-vlmshots-v94.sh + vlm-compare-v94.mjs + arbit-v94.sh — the sed derivation from the v88 series with the version + session-name + tmp-dir substitutions, the headers history-corrected to the FIFTH re-run, the functional bodies verified version-bump-only by the normalize-back diff; the arbit lineage's SESSION NAMES (refar88/clonear88) caught by the explicit SECOND sed pass — they ride the "ar" token family, not the "v88" family; login on the first attempt both sides; the parked pointer at (5,5); read-only — the v46 rule holds; the reaping budget applied as a standing step — the pre-run + between-halves reaps on every probe, zero resource-exhaustion symptoms this cycle): **both verdicts DIFFERENT with every flag DOM-arbitrated to the v82/v88 re-runs' own documented classes** — the NETWORTH pair's flags (the avatar user-identity class; the "Edit with Base44" FAB the platform-chrome class RE-ARBITRATED LIVE [fabCount 0 + bodyHasBase44 false on BOTH sides]; the seed-data figures — the 1-asset vs 3-asset groups, the ∞:1 vs 0.21:1 ratio) + the DRILL-DOWN pair's flags (the v56 SUPERSET nav-highlight [the reference's link INERT vs the clone's ACTIVE white/500]; the avatar; the pct × 568 DATA class [fillW ref 173 vs clone 357 on the byte-identical 568×12 track — the v82/v88 values REPRODUCED EXACTLY six re-runs later]; the v60 PERCEPTION donut-labels class [count 4, labelLineCount 0, 16px, black, 3 sectors — chrome byte-identical]; the v82 VLM-MISREAD stat-title class RE-ARBITRATED LIVE [both sides' titles "Total Income"/"Total Savings"/"Total Expenses" plural, byte-identical]; the v88 VLM-MISREAD divider class RE-ARBITRATED LIVE [the divider {DIV, h 1, bg rgb(229,231,227), flexGrow 1} byte-identical on every card]; the seed-data classes). The census — **executed in the TWO-HALF controlled form BUILT two-half from the start** (ref-arbit-v94.sh + clone-arbit-v94.sh via build-twohalf-v94.py, the ARBIT_A + ARBIT_B census blocks byte-identical across the halves by the md5 line-block contract [a9cdcc96 / baa22974]) — **REPRODUCES the v88 census values EXACTLY: zero drift on every axis** (the drill-down census: navHighlight/avatarLetter/progress/donutLabels/statTrendIcons/heroTrendGlyphs; the networth summary-card census: the card 960×333/32px/16px/the gradient/the shadow, the headRow/label/figure/medallion/statGrid/statTile/ratioFooter families — the labelBlock's width the v82 DATA-CONDITIONAL class [304 vs 357]). **NO NEW CLONE GAP.**

**F4 the +1 e2e pin (296 → 297): the networth SECTION-HEADER row census at 1280** (tests/e2e/networth.spec.ts — the tab panel's "Assets" header row, never pinned at ANY viewport: the row's flex chrome {flex/center/space-between/h 56/w 960} + the h2 "Assets" typography {24px/700/lh 32px/rgb(26,58,46)/mb 0/h 32} + the count subtitle P {16px/400/lh 24px/rgb(107,114,128)} + the left block's h 56 [the width EXCLUDED — the countText data-coupled width class, the v82 labelBlock convention] + the Add Asset button's chrome on this row {36×134/8px 16px/6px/14px/500/white/the forest→lime gradient} + the 16px Plus + the row→group rhythm delta 24 [the margin-TOP form EXCLUDED — the v3/v4 space-y margin-attribution computed class] + the first type-group header's re-affirm {18px/600/lh 28px/mb 12} + the docSW 1280 guard). The pin's own axes first measured byte-identical on BOTH sides by the supplemental two-half census (nwsection-arbit-v94.sh + nwsection-clone-v94.sh — BUILT two-half from the start via build-nwsection-v94.py, the census JS byte-identical by the md5 line-block diff [f8b3cabf]; BOTH sides read-only — the reference's populated Assets panel passively measured, the clone's seeded panel passively measured, the seedcheck exact after the run) — GREEN on first run. **The pin-sanity mutation (the executed form)**: the h2's `text-2xl font-bold` → `text-2xl font-bold lg:font-black` (net-worth-view.tsx:418, by LINE NUMBER — the line-scoping keeps the file's OTHER text-2xl font-bold instances [107/212/348/371/378/482] untouched; AT-lg because the pin runs at 1280): ONLY the v94 pin red (29 green under the mutation), the failure diff reads as the h2.fw axis ALONE ("700" → "900" at ≥1024px) — cascade-free BY CONSTRUCTION (the h2's lh 32px bound by text-2xl's line-height — a font-weight flip does not scale it; the block h 56, the row, the countP, the addBtn, the rhythm, and the docSW all unchanged; no spec asserts the "Assets" section h2's computed styles at ANY viewport — the getByRole heading + the a11y TAB-role references text-matching, green under a weight flip; lg:font-black appears NOWHERE in src/) — then restored (git diff src/ = 0 lines; the standalone REBUILD via the FULL npm run build; the post-restore full run 30/30 green).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **297 e2e** (111+106+82 = 299 chunk executions = 297 unique tests, zero flakes) · 35/35 smoke ✓; the screenshots **16/16 BYTE-IDENTICAL** (the same-day-seed byte-identity law — the second consecutive pure-form cycle: the seed planted and the shots taken on the same calendar day 2026-10-19, byte-for-byte reproduction, ZERO arbitration needed); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v94 paragraph), D2 CLAUDE.md (296 → 297 + the v94 clause at the E2E line's tail), D3 README.md (the counts + the v94 plan-table row), D4 zero-balance_SKILL.md (Session 129 audit row + the state line), D5 the PAD's v1.1.51 revision block, D6 the probe README's v94 section (the reaping-standing-step lesson + the second-pass session-name sed lesson + the misread-class live re-arbitration lesson + the v95 queue), D7 session_226.md + this Session 129 entry.

**The next queue:** the v95 cycle — the v89-era DASHBOARD pair (the BUDGET GUIDELINES card + the QUICK-ACTION card row, both below-the-fold surfaces of the dashboard FULL-PAGE at desktop 1280x800, last re-shot v89 — now the oldest remaining [v89 < v90 < v91 < v92 < v93 < v94]; the pair's FIFTH re-run [v61 → v68 → v77 → v83 → v89 → v95]); verify against the rotation ledger first, per protocol.

---

## Session 128 — Parity iteration v93: the re-run cycle's next-oldest candidate (the v87-era login + calculator pair's fifth re-run) + the axe watch (NO DRIFT) + the totalCard inner-text census pin (PIN-ONLY) (2026-10-19)

**The cycle** (`docs/remediation-plan-v93.md` — the plan validated against the codebase before execution; the narrative: `docs/session_224.md`): the v92-era docs' v93 queue suggestion agreeing with the rotation ledger (the SIXTEENTH consecutive agreement) — the v87-era LOGIN + CALCULATOR pair (the LOGIN view + the CALCULATOR dialog at desktop 1280x800, last re-shot v87, the oldest remaining [v87 < v88 < v89 < v90 < v91 < v92]; the pair's FIFTH re-run [v59 → v66 → v75 → v81 → v87 → v93]; the surface names verified against vlm-shots-v87.sh's own header before the derivation — the queue-prose verification lesson applied, no error to correct this cycle).

**The baseline — the carried-over workspace (the session-log-only commit class)**: pulled to main @ 926f193 (the docs-only session-log commit — ZERO src/ or lockfile deltas since the v92 push 6567512), so the v92 cycle's own fresh-clone environment carries over unchanged (npm ci 354 packages at the identical lockfile; .env [DATABASE_URL="file:../db/custom.db"], db/ at the repo root; chromium-1243; the paramiko ssh shim outside the repo); the seedcheck exact before any flow ran; lint → typecheck → 108 unit → build → 295 e2e (105+112+80 = 297 chunk executions = 295 unique, zero flakes on the first run) → 35/35 smoke — the exact documented v92 state. The audit clean (the v92 commit 6567512 re-verified PIN-ONLY [34 files, +2476/−6, ZERO src/ changes]; the one commit since session-log-only; the production seams re-audited — auth, db-path, the SEO pair [prerendered by the build], the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout). The axe watch NO DRIFT (4.14.0 npm-latest, only sha prereleases beyond, no 5.x; the v68 dedupe holds; the engine-contract pin 2 passed standalone).

**F2 the 87th standing checks** (ref-standing-v87.sh + standing-checks-v87.sh, version-bumped from v86 across the three token families — version-bump-only diffs verified): the mobile menu VERIFIED WORKING (the 87th consecutive time); the reference's four bugs ALL live; the data census the 87th clean drift check; the SEO pair live on both sides.

**F3 the re-run pair** (vlm-shots-v93.sh + login-shots-v93.sh + clone-vlmshots-v93.sh + clone-login-shots-v93.sh + vlm-compare-v93.mjs + arbit-v93.sh — the sed derivation from the v87 lineage with the version + session-name + tmp-dir substitutions, the headers history-corrected to the fifth re-run; login on the first attempt both sides; the parked pointer at (5,5); read-only — the v46 rule holds; the v89/v92 reaping lesson applied mid-cycle — the clone-side shots' first run hit the chromium resource exhaustion [70 zombie processes, the EMPTY-eval signature], the pkill + session-file sweep + a reaping step budgeted between the halves of every long probe from then on): **the LOGIN verdict IDENTICAL the FOURTH consecutive (v75/v81/v87/v93)** with the both-sides census byte-identical on every axis; **the CALCULATOR verdict DIFFERENT with every flag DOM-arbitrated to the v75/v81/v87 re-runs' own documented classes** (the v66 DATA-CONDITIONAL will-update span + its derived card-height note [the totalCard box 720×90 byte-identical]; the v75/v81/v87 POINTER-POSITION actions perception [actionsAtRest {opacity: 0, btnCount: 2} byte-identical]; the seed-data figures; the close axis absent ref-side — the v87-documented lost-accessible-name observation holding, the clone the SUPERSET). The census — **executed in the TWO-HALF controlled form, BUILT two-half from the start** (ref-arbit-v93.sh + clone-arbit-v93.sh via build-twohalf-v93.py, the TWO census JS blocks [CALC + LOGIN] extracted once and embedded byte-identically across the halves — the md5 line-block contract) — **REPRODUCES the v87 census values EXACTLY: zero drift on every axis**. NO NEW CLONE GAP.

**F4 the v93 pin (+1 e2e = 296)**: the totalCard INNER-TEXT census at 1280 (tests/e2e/calculator.spec.ts — the v73 390 summary-text family's DESKTOP twin [the amount {24px/700/32px/rgb(224,122,59)} + the basedOn {12px/16px/rgb(107,114,128)} + the willUpdate {12px/400/rgb(234,88,12)}] PLUS the "Total Calculated" LABEL leaf's typography {14px/500/20px/rgb(107,114,128)} — never pinned at ANY viewport — PLUS the two summary rows' chrome + the box re-affirm + the docSW 1280 guard) — the pin's own axes first measured byte-identical on both sides by the supplemental two-half census (totalcard-arbit-v93.sh + totalcard-clone-v93.sh — BUILT two-half from the start, the census JS byte-identical by the md5 line-block diff; the reference's NATIVE 1-row state read-only, the clone's added-then-fully-restored twin) — GREEN on first run. **The pin-sanity mutation** (the executed form — the viewport-scoped text-sm font-medium → text-sm font-medium lg:font-semibold at calculator-dialog.tsx:153, by LINE NUMBER; AT-lg because the pin runs at 1280): the failure diff reads as the label.fw axis ALONE ("500" → "600" at ≥1024px); the full calculator.spec.ts under the mutation reads ONLY the v93 pin red (17 green) — cascade-free BY CONSTRUCTION (the inline label's lh 20px bound by the amount's 32px row; the totalCard box unchanged; no spec asserts the label's computed styles at ANY viewport) — then restored (git diff src/ = 0 lines; the standalone REBUILD via the FULL npm run build; the post-restore full run 18/18 green).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **296 e2e** (106+112+80 = 298 chunk executions = 296 unique tests, zero flakes) · 35/35 smoke ✓; the screenshots **16/16 BYTE-IDENTICAL** (the same-day-seed byte-identity law in its purest form — the seed planted and the shots taken on the same calendar day 2026-10-19, byte-for-byte reproduction, ZERO arbitration needed this cycle); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v93 paragraph), D2 CLAUDE.md (296 + the v93 clause), D3 README.md (the counts + the v93 plan-table row + the v92/v58 row-boundary repair), D4 zero-balance_SKILL.md (Session 128 audit row + the state line), D5 the PAD's v1.1.50 revision block, D6 the probe README's v93 section (the reaping-budget-between-halves lesson + the self-matching pkill caution + the session-log-only commit class + the label-first family extension + the v94 queue), D7 session_224.md + this Session 128 entry.

**The next queue:** the v94 cycle — the v88-era NETWORTH + DRILL-DOWN pair (the NETWORTH view + the dashboard's drill-down EXPANDED state, both desktop 1280x800 full-page, last re-shot v88 — now the oldest remaining [v88 < v89 < v90 < v91 < v92 < v93]; the pair's FIFTH re-run [v60 → v67 → v76 → v82 → v88 → v94]); verify against the rotation ledger first, per protocol.

---

## Session 127 — Parity iteration v92: the re-run cycle's next-oldest candidate (the v86-era savings pair's fifth re-run) + the axe watch (NO DRIFT) + the savings filter-interior + search-icon census pin (PIN-ONLY) (2026-10-19)

**The cycle** (`docs/remediation-plan-v92.md` — the plan validated against the codebase before execution; the narrative: `docs/session_222.md`): the v91-era docs' v92 queue suggestion agreeing with the rotation ledger (the FIFTEENTH consecutive agreement) — the v86-era SAVINGS pair (the SAVINGS view at desktop 1280x800, full-page, last re-shot v86, the oldest remaining [v86 < v87 < v88 < v89 < v90 < v91]; the pair's FIFTH re-run [v58 → v65 → v74 → v80 → v86 → v92]; the surface names verified against vlm-shots-v86.sh's own surface list before the derivation — the queue-prose verification lesson applied, no error to correct this cycle).

**The baseline — the REBUILT fresh-clone workspace (the v86/v88/v90/v91 precedent)**: git clone at main @ e520a61, the tree clean; the environment re-provisioned (npm ci 354 packages; .env [DATABASE_URL="file:../db/custom.db"], db/ at the repo root with db:generate + db:push + db:seed; chromium-1243; the paramiko ssh shim outside the repo); the seedcheck exact before any flow; lint → typecheck → 108 unit → build → 294 e2e (132+108+56 = 296 chunk executions = 294 unique, zero flakes on the first run) → 35/35 smoke — the exact documented v91 state. The audit clean (the v91 commit c794a7c re-verified PIN-ONLY [21 files, +2161/-6, ZERO src/ changes]; the one commit since session-log + skills-folder-only; the production seams re-audited — auth, db-path, the SEO pair [prerendered by the build], the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout). The axe watch NO DRIFT (4.14.0 npm-latest, only rc prereleases beyond, no 5.x; the v68 dedupe holds; the engine-contract pin 2 passed standalone).

**F2 the 86th standing checks** (ref-standing-v86.sh + standing-checks-v86.sh, version-bumped from v85 across the three token families — version-bump-only diffs verified): the mobile menu VERIFIED WORKING (the 86th consecutive time); the reference's four bugs ALL live; the data census the 86th clean drift check; the SEO pair live on both sides.

**F3 the re-run pair** (vlm-shots-v92.sh + clone-vlmshots-v92.sh + vlm-compare-v92.mjs + arbit-v92.sh — the sed derivation from the v86 series with the version + session-name + tmp-dir substitutions, the headers history-corrected to the fifth re-run; login on the first attempt both sides; the parked pointer at (5,5); read-only — the v46 rule holds): **the verdict DIFFERENT with every flag DOM-arbitrated to the v86 re-run's own documented classes** (the seed-count grid; the v58 DATA-CONDITIONAL footer + its derived internal-spacing note; the seed-data figures/badges/subtexts; the user-identity avatar; no FAB flag this cycle). The census — **executed in the TWO-HALF controlled form** (ref-arbit-v92.sh + clone-arbit-v92.sh, derived by build-twohalf-v92.py with the census JS extracted once and embedded byte-identically across the halves — the lines-1-153 identity verified) after the combined script's clone half aborted in the chromium resource exhaustion (the v89/v91-documented symptom class, the lesson re-verified) — **REPRODUCES the v86 census values EXACTLY: zero drift on every axis** (the h1; the grid 960/16px/~309px; the card 309/20px/12px/border with the h 200-vs-230 v70b wrap class; the titleRow flex/center/8px/h 24 with the savings blue dot; the amount 24px/700/32px/blue; the footer + badge chrome with the v58 DATA-CONDITIONAL + v57 wrap classes; the docSW 1280 guard). NO NEW CLONE GAP.

**F4 the v92 pin (+1 e2e = 295)**: the savings filter-interior + SEARCH-ICON census at 1280 (tests/e2e/items.spec.ts — the v91 pin family's THIRD variant [income + expenses pinned v91; the savings variant never — the v38 S2 pin held the card chrome + the search/combobox GEOMETRY at the default viewport only] PLUS the search icon's computed chrome {svg/20×20/rgb(107,114,128)/absolute/left 12px} — the filter card's last never-pinned element, never pinned at ANY viewport on ANY view; the glyph spec holds the PATH data only, the class-string test the w-5 SUBSTRING only) — the pin's own axes first measured byte-identical on both sides by the supplemental two-half census (savings-filter-arbit-v92.sh + savings-filter-clone-v92.sh — the v87-v91 one-shot precedent, BUILT two-half from the start after the cycle's first exhaustion) — GREEN on first run. **The pin-sanity mutation** (the executed form — the viewport-scoped h-5 w-5 → h-5 w-5 lg:h-6 at items-view.tsx:181, by LINE NUMBER; AT-lg because the pin runs at 1280): the failure diff reads as the searchIcon.h axis ALONE ("20" → "24"); the full items.spec.ts under the mutation reads ONLY the v92 pin red (40 green) — cascade-free BY CONSTRUCTION (the icon absolutely positioned, out of flow; no spec asserts any search icon's computed w/h at ANY viewport; the v91 fw-dodge form NOT reusable — the shared Input instance would cascade the v91 pin red, the MUTATION-FAMILY ROTATION lesson) — then restored (git diff src/ = 0 lines; the standalone REBUILD via the FULL npm run build; the post-restore full run 41/41 green).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **295 e2e** (133+108+56 = 297 chunk executions = 295 unique tests, zero flakes) · 35/35 smoke ✓; the screenshots **9/16 BYTE-IDENTICAL + 7/16 benign-pixel-arbitrated** (6 DATE-TEXT-ONLY [03/04/05/06/07/16 — the fresh seed planted 2026-10-19 vs the committed set's 2026-10-18 seed, the day number +1, every crop pair single-image VLM-arbitrated, the chrome byte-identical; the 16-item-details wide-region diff decomposed by the within-crop column-band analysis into the date glyphs + the sub-perceptual noise tail — both classes benign, co-occurring] + 1 RASTERIZATION-NOISE [08-calculator: every differing pixel ≤4 channel units, both crops VLM-read "solid gray, no text"]; the regenerated set ships per the v80 discipline); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v92 paragraph), D2 CLAUDE.md (295 + the v92 pin clause), D3 README.md (the counts + the v92 plan-table row), D4 zero-balance_SKILL.md (Session 127 audit row + the state lines), D5 the PAD's v1.1.49 revision block, D6 the probe README's v92 section (the two-half-from-the-start lesson + the mutation-family-rotation lesson + the seed-day date-class decomposition lesson + the v93 queue), D7 session_222.md + this Session 127 entry.

**The next queue:** the v93 cycle — the v87-era LOGIN + CALCULATOR pair (the calculator dialog at desktop 1280x800, last re-shot v87 — now the oldest remaining [v87 < v88 < v89 < v90 < v91 < v92]; the pair's FIFTH re-run [v59 → v66 → v75 → v81 → v87 → v93]); verify against the rotation ledger first, per protocol.

---

## Session 126 — Parity iteration v91: the re-run cycle's next-oldest candidate (the v85-era items pair's fifth re-run) + the axe watch (NO DRIFT) + the filter-card interactive-interior census pin (PIN-ONLY) (2026-10-19)

**The cycle** (`docs/remediation-plan-v91.md` — the plan validated against the codebase before execution; the narrative: `docs/session_220.md`): the v90-era docs' v91 queue suggestion agreeing with the rotation ledger (the FOURTEENTH consecutive agreement) — the v85-era ITEMS pair (the INCOME + EXPENSES view pair at desktop 1280x800, full-page, last re-shot v85, the oldest remaining [v85 < v86 < v87 < v88 < v89 < v90]; the pair's FIFTH re-run [v57 → v64 → v70 → v79 → v85 → v91]; the surface names verified against vlm-shots-v85.sh's own surface list before the derivation — the queue-prose verification lesson applied, no error to correct this cycle).

**The baseline — the REBUILT fresh-clone workspace (the v86/v88/v90 precedent)**: git clone at main @ 07586b7, the tree clean; the environment re-provisioned (npm ci 354 packages; .env [DATABASE_URL="file:../db/custom.db"], db/ at the repo root with db:generate + db:push + db:seed; chromium-1243; the paramiko ssh shim outside the repo); the seedcheck exact before any flow; lint → typecheck → 108 unit → build → 293 e2e (127+106+62 = 295 chunk executions = 293 unique, zero flakes on the first run) → 35/35 smoke — the exact documented v90 state. The audit clean (the v90 commit 1c9438f re-verified PIN-ONLY [17 files, +1429/-13, ZERO src/ changes]; the one commit since session-log-only; the production seams re-audited — auth, db-path, the SEO pair [prerendered by the build], the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout). The axe watch NO DRIFT (4.14.0 npm-latest, only rc prereleases beyond, no 5.x; the v68 dedupe holds; the engine-contract pin 2 passed standalone).

**F2 the 85th standing checks** (ref-standing-v85.sh + standing-checks-v85.sh, version-bumped from v84 across the three token families — version-bump-only diffs verified): the mobile menu VERIFIED WORKING (the 85th consecutive time); the reference's four bugs ALL live; the data census the 85th clean drift check; the SEO pair live on both sides.

**F3 the re-run pair** (vlm-shots-v91.sh + clone-vlmshots-v91.sh + vlm-compare-v91.mjs + arbit-v91.sh — the sed derivation from the v85 series with the version + session-name + tmp-dir substitutions, the headers history-corrected to the fifth re-run; login on the first attempt both sides; the parked pointer at (5,5); read-only — the v46 rule holds): **both verdicts DIFFERENT with every flag DOM-arbitrated to the v85 re-run's own documented classes** (the v57 payment-chip DATA-CONDITIONAL footer; the v57 Recurring superset wrap [the card h 200-vs-230, the badgeRow h 22-vs-52]; the seed-count grids; the user-identity avatar; the seed-data classes; the "Edit with Base44" FAB the v85-documented VLM image-attribution swap RECURRED and was re-arbitrated live by the one-shot both-sides DOM census [base44-fab-arbit-v91.sh: fabCount 0 + bodyHasBase44 false on BOTH sides — the FAB lives in the reference's platform iframe chrome]). The census — **executed in the TWO-HALF controlled form** (ref-arbit-v91.sh + clone-arbit-v91.sh, the census JS byte-identical across the halves) after the combined script's mid-run chromium resource exhaustion (70 zombies reaped; the v89 lesson re-verified) — **REPRODUCES the v85 census values EXACTLY: zero drift on every axis** (the avatar/grid/card/titleRow/amount/footer/badge/filterCard families; the docSW 1280 guard). NO NEW CLONE GAP.

**F4 the v91 pin (+1 e2e = 294)**: the filter-card INTERACTIVE-INTERIOR census at 1280 (tests/e2e/items.spec.ts — the never-pinned families: the search input's TYPOGRAPHY {INPUT/14px/400/20px/rgb(10,10,10)} + every combobox trigger's RESTING chrome {BUTTON/216×36/pad 8px 12px/space-between/center/transparent bg/6px radius/1px rgb(229,229,229) border/14px/400/rgb(10,10,10) + the chevron 16×16 currentColor} — the v64 F3/v70 F4 pins held the card + search GEOMETRY + the comboboxes' w/h/fs/text, the v37 S1/S2 pins the FOCUS state; the interiors never pinned at ANY viewport) — the pin's own axes first measured byte-identical on both sides by the supplemental two-half census (filter-interior-arbit-v91.sh + filter-interior-clone-v91.sh — the v87/v88/v89/v90 one-shot precedent, BUILT two-half from the start after the cycle's first exhaustion) — GREEN on first run. **The pin-sanity mutation** (the executed form — the viewport-scoped pl-10 → pl-10 lg:font-medium at items-view.tsx:188, by LINE NUMBER; AT-lg because the pin runs at 1280): the failure diff reads as the search's fw axis ALONE ("400" → "500"); the full items.spec.ts under the mutation reads ONLY the v91 pin red (39 green) — cascade-free BY CONSTRUCTION (fw never changes line-height/color/geometry; the coverage-map grep run with BOTH the fw: long form AND the Fw-suffix shorthand family — no spec asserts any input's fw at any viewport, the v90 shorthand-token lesson applied) — then restored (git diff src/ = 0 lines; the standalone REBUILD via the FULL npm run build — a bare `next build` leaves the standalone dir without its static assets, the failure surfacing as "element(s) not found"; the post-restore full run 40/40 green).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **294 e2e** (128+106+62 = 296 chunk executions = 294 unique tests, zero flakes) · 35/35 smoke ✓; the screenshots **16/16 BYTE-IDENTICAL** (the same-day-seed byte-identity law on the fresh-clone seed); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v91 paragraph), D2 CLAUDE.md (294 + the v91 pin clause), D3 README.md (the counts + the v91 plan-table row), D4 zero-balance_SKILL.md (Session 126 audit row + the state lines), D5 the PAD's v1.1.48 revision block, D6 the probe README's v91 section (the FAB re-arbitration lesson + the two-half-census-retrofitted lesson + the full-build rebuild discipline + the v92 queue), D7 session_220.md + this Session 126 entry.

**The next queue:** the v92 cycle — the v86-era SAVINGS pair (the savings view at desktop 1280x800, full-page, last re-shot v86 — now the oldest remaining [v86 < v87 < v88 < v89 < v90 < v91]; the pair's FIFTH re-run [v58 → v65 → v74 → v80 → v86 → v92]); verify against the rotation ledger first, per protocol.

---

## Session 125 — Parity iteration v90: the re-run cycle's next-oldest candidate (the v84-era mobile 390 twins' fourth re-run) + the axe watch (NO DRIFT) + the stat-tile interior census pin (PIN-ONLY) (2026-10-19)

**The cycle** (`docs/remediation-plan-v90.md` — the plan validated against the codebase before execution, the mutation cascade catch included; the narrative: `docs/session_218.md`): the v89 plan's v90 queue suggestion agreeing with the rotation ledger ONCE THE SURFACE-NAME TRANSCRIPTION ERROR IS CORRECTED (the THIRTEENTH consecutive agreement) — the v84-era MOBILE 390 TWINS (the /networth + the dashboard FULL-PAGE pair at 390x844, last re-shot v84, the oldest remaining [v84 < v85 < v86 < v87 < v88 < v89]; the pair's FOURTH re-run [v62/v63 → v69 → v78 → v84 → v90]; the v89-era docs' "login + dashboard" phrasing and "FIFTH re-run" bracket corrected against the v84 probe scripts themselves — the queue-prose verification lesson).

**The baseline — the REBUILT fresh-clone workspace (the v86/v88 precedent)**: git clone at main @ 0f8bec4, the tree clean; the environment re-provisioned (npm ci 354 packages; .env [DATABASE_URL="file:../db/custom.db"], db/ at the repo root with db:generate + db:push + db:seed; chromium-1243; the paramiko ssh shim outside the repo); the seedcheck exact before any flow; lint → typecheck → 108 unit → build → 292 e2e (121+114+59 = 295 chunk executions = 292 unique, zero flakes on the first run) → 35/35 smoke — the exact documented v89 state. The audit clean (the v89 commit f2040a3 re-verified PIN-ONLY [19 files, +1748/-4, ZERO src/ changes]; the two commits since session-log-only; the production seams re-audited — auth, db-path, the SEO pair [prerendered by the build], the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout). The axe watch NO DRIFT (4.14.0, only rc prereleases, the v68 dedupe holds; the engine-contract pin 2 passed standalone).

**F2 the 84th standing checks** (ref-standing-v84.sh + standing-checks-v84.sh, version-bumped from v83 across the three token families — version-bump-only diffs verified): the mobile menu VERIFIED WORKING (the 84th consecutive time); the reference's four bugs ALL live; the data census the 84th clean drift check; the SEO pair live on both sides.

**F3 the re-run pair** (vlm-shots-v90.sh + clone-vlmshots-v90.sh + vlm-compare-v90.mjs + arbit-v90.sh — the sed derivation from the v84 series with the version + session-name + tmp-dir substitutions, the headers history-corrected to the fourth re-run; login on the first attempt both sides; the parked pointer at (5,5); read-only — the v46 rule): **both verdicts DIFFERENT with every flag DOM-arbitrated to the v84 re-run's own documented classes** (the v41 mobile-superset stacking; the medallion "larger circle" a VLM perception misread — the 64×64 + 32×32 chrome byte-identical; the tab-bar alignment a misread under the v53 pin; the v62 subtitle width-delta wrap; the Base44 platform-chrome overlay; the seed-data classes). The census — the combined arbit-v90.sh ran clean this cycle (no resource exhaustion, no two-half split needed) — REPRODUCES the v84 census values EXACTLY: zero drift on every axis (the summary card/statGrid/tiles/medallion/trendIcon families; the subtitle chrome fs 16px/fw 400/rgb(107,114,128)/lh 24px/P h 48/block h 92; the breakdown card's svg family [svgCount 7, the 16/14 alternation, rechartsWrappers 0, pieSectors 0] + the children heights byte-identical). NO NEW CLONE GAP.

**F4 the v90 pin (+1 e2e = 293)**: the stat-tile INTERIOR census at 390 (tests/e2e/networth.spec.ts — the never-pinned families: the two tiles' LABEL {P/12px/rgba(255,255,255,0.7)/mb 4px/h 16} + VALUE {P/24px/700/white} interiors — the v63 F3 pin held the tile BOX only; the tile-box/grid/docSW re-affirm) — the pin's own axes first measured byte-identical on both sides by the supplemental census (tile-interior-arbit-v90.sh, the v87/v88/v89 one-shot precedent) — GREEN on first run. **THE MUTATION-AS-COVERAGE-AUDIT CATCH**: the pin-sanity mutation's FIRST attempt (the bare font-bold → font-extrabold swap at net-worth-view.tsx:371, by LINE NUMBER) cascaded to the v60 F1 pin's amtFw axis at 1280 — the plan's fw-token grep had missed the v60 pin's amtFw shorthand (the tile value's fw was already pinned at 1280 all along); the catch is the mutation discipline working as designed. The corrected viewport-scoped dodge (font-bold → font-bold max-lg:font-extrabold — the max-lg variant INERT at ≥1024px) confines the flip to below 1024px: only the v90 pin red under it (28 green, the v60 pin green; the failure diff reads as the fw axis alone "700" → "800") — then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines; the post-restore full run 29/29 green).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **293 e2e** (122+114+59 = 295 chunk executions = 293 unique tests, zero flakes) · 35/35 smoke ✓; the screenshots **16/16 BYTE-IDENTICAL** (the same-day-seed byte-identity law on the fresh-clone seed); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v90 paragraph + the queue-correction note), D2 CLAUDE.md (293 + the v90 pin clause), D3 README.md (the counts + the v90 plan-table row), D4 zero-balance_SKILL.md (Session 125 audit row + the state lines), D5 the PAD's v1.1.47 revision block, D6 the probe README's v90 section (the queue-prose verification lesson + the shorthand-token grep lesson + the fresh-clone reprovisioning note + the v91 queue), D7 session_218.md + this Session 125 entry.

**The next queue:** the v91 cycle — the v85-era ITEMS pair (the income + expenses view pair at desktop 1280, last re-shot v85 — now the oldest remaining [v85 < v86 < v87 < v88 < v89 < v90]; the pair's FIFTH re-run [v57 → v64 → v70 → v79 → v85 → v91]); verify against the rotation ledger first, per protocol.

---

## Session 124 — Parity iteration v89: the re-run cycle's next-oldest candidate (the v83-era dashboard pair's fourth re-run) + the axe watch (NO DRIFT) + the quick-action transition + plus-viewBox + guidelines-body-display census pin (PIN-ONLY) (2026-10-18)

**The cycle** (`docs/remediation-plan-v89.md` — the plan validated against the codebase before execution, the mutation refutations included; the narrative: `docs/session_215.md`): the v88 plan's v89 queue suggestion agreeing with the rotation ledger (the TWELFTH consecutive agreement) — the v83-era DASHBOARD pair (the dashboard FULL-PAGE at desktop 1280x800, the below-the-fold Budget Guidelines card + the quick-action row, last re-shot v83, the oldest remaining [v83 < v84 < v85 < v86 < v87 < v88]; the pair's FOURTH re-run [v61 → v68 → v77 → v83 → v89]).

**The baseline — the PRESERVED workspace (the v87 precedent — no reset)**: git pull fast-forward 0cae166..ef681c0 (the session_214 transcript only), the tree clean; the environment verified in place (.env, db/, node_modules 354, chromium-1243, the ssh shim); the seedcheck exact before any flow; lint → typecheck → 108 unit → build → 291 e2e (120+113+60 = 293 chunk executions = 291 unique, the chunk boundaries split differently than v88's but the unique total identical) → 35/35 smoke — the exact documented v88 state. The audit clean (the v88 commit 464025b re-verified PIN-ONLY [17 files, +1513/-4, ZERO src/ changes]; the commits since session-log-only; the production seams re-audited; skills/ excluded throughout). The axe watch NO DRIFT (4.14.0, only rc prereleases, the v68 dedupe holds; the engine-contract pin 2 passed standalone).

**F2 the 83rd standing checks** (ref-standing-v83.sh + standing-checks-v83.sh, version-bumped from v82 across the three token families — version-bump-only diffs verified): the mobile menu VERIFIED WORKING (the 83rd consecutive time); the reference's four bugs ALL live; the data census the 83rd clean drift check; the SEO pair live on both sides.

**F3 the re-run pair** (vlm-shots-v89.sh + clone-vlmshots-v89.sh + vlm-compare-v89.mjs + arbit-v89.sh — the sed derivation from the v83 series with the version + session-name + tmp-dir substitutions, the headers history-corrected to the fourth re-run; login on the first attempt both sides; the parked pointer at (5,5); read-only — the v46 rule): **the verdict IDENTICAL — zero style flags** (the pair's SECOND consecutive IDENTICAL verdict [v83 → v89]; every VLM flag the documented seed-data classes). The census — executed in the CONTROLLED TWO-HALF FORM (ref-arbit-v89.sh + clone-arbit-v89.sh) after the sandbox's chromium resource exhaustion (66 zombie processes reaped; the symptom EMPTY eval results, not an error surface) and a transient with-server boot abort (retry-first resolved) — REPRODUCES the v83 census values EXACTLY: zero drift on every axis (the guidelines card/header/body/three-tiles; the quick-action grid + the three cards' full chrome; the cross-row gap 340 byte-identical; the two census deltas both documented classes [the v66 INVISIBLE shadow lead-layer count; the v77 grid-mt mechanism class with the rendered gap byte-identical]). NO NEW CLONE GAP.

**F4 the v89 pin (+1 e2e = 292)**: the quick-action TRANSITION + PLUS-viewBox + GUIDELINES-BODY-DISPLAY census at 1280 (tests/e2e/dashboard.spec.ts — the never-pinned families: the three cards' transition {transitionDuration "0.2s"/transitionProperty "all" — never pinned at ANY viewport} + the three plus icons' viewBox {0 0 24 24 — the v77 icon-viewBox family's plus twin} + the guidelines body's display {block — the v61 F2 pad family's companion} + the docSW guard) — the pin's own axes first measured byte-identical on both sides by the supplemental census (qa-transition-arbit-v89.sh, the v87/v88 one-shot precedent) — GREEN on first run. The pin-sanity mutation (the viewport-scoped responsive-variant dodge): the card's duration-200 → duration-200 lg:duration-300 (dashboard-view.tsx:885, by LINE NUMBER) FAILS at exactly the card.transitionDuration axis ("0.2s" → "0.3s" — the failure diff reads as the duration axis alone) — cascade-free BY CONSTRUCTION (transitionDuration never affects geometry — every geometry pin green; the v45 F3b hover-shadow pin asserts the settled layers; 40 green under the mutation, only the v89 pin red) — then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines; the post-restore full run 41/41 green).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **292 e2e** (121+113+60 = 294 chunk executions = 292 unique, zero flakes) · 35/35 smoke ✓; the screenshots **16/16 BYTE-IDENTICAL** (the same-day-seed byte-identity law); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v89 paragraph), D2 CLAUDE.md (292 + the v89 pin clause), D3 README.md (the counts + the v89 plan-table row), D4 zero-balance_SKILL.md (Session 124 audit row + the state lines), D5 the PAD's v1.1.46 revision block, D6 the probe README's v89 section (two new lessons: the chromium resource-exhaustion reaping, the two-half controlled census form), D7 session_215.md + this Session 124 entry.

**The next queue:** the v90 cycle — the v84-era MOBILE 390 TWINS (the login + dashboard mobile views, last re-shot v84 — now the oldest remaining [v84 < v85 < v86 < v87 < v88 < v89]; the twins' FIFTH re-run [v69 → v74 → v78 → v84 → v90]); verify against the rotation ledger first, per protocol.

---

## Session 123 — Parity iteration v88: the re-run cycle's next-oldest candidate (the v82-era networth + drill-down pair's fourth re-run) + the axe watch (NO DRIFT) + the stat-card count-row + divider census pin (PIN-ONLY) (2026-10-18)

**The cycle** (`docs/remediation-plan-v88.md` — the plan validated against the codebase before execution, the mutation refutations included; the narrative: `docs/session_212.md`): the v87 plan's v88 queue suggestion agreeing with the rotation ledger (the ELEVENTH consecutive agreement) — the v82-era NETWORTH + DRILL-DOWN pair (the networth view + the dashboard drill-down EXPANDED at desktop 1280, last re-shot v82, the oldest remaining [v82 < v83 < v84 < v85 < v86 < v87]); the pair's FOURTH re-run [v60 → v67 → v76 → v82 → v88]. **PIN-ONLY for src/ — no production-code change; +1 e2e = 291.**

**The baseline — the REBUILT workspace (the fresh-clone path, the v86 precedent)**: git clone at main @ 154ac6a (the v87 shipped state + the session_211 transcript), the tree clean; the environment re-provisioned (npm ci 354 packages + the four approved install scripts; .env written [DATABASE_URL=file:../db/custom.db], db/ at the repo root, db:generate + db:push + db:seed; chromium-1243 installed; the paramiko shim deployed); the seedcheck exact [7/1850/2235/0/3/2] before any flow: lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ · 292 e2e chunk executions (103+129+60 = 290 unique = the documented v87 state) ✓ · 35/35 smoke ✓. **The audit clean** (the v87 commit 30bdf9f verified PIN-ONLY [21 files, +1847/-4, ZERO src/ changes]; the one commit since session-log-only; the production seams re-audited — auth scrypt/timingSafeEqual/HMAC, db-path, the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout [eslint + tsconfig verified]). **F1 axe watch: NO DRIFT** (npm-latest 4.14.0, only rc prereleases beyond, no 5.x; the v68 dedupe state holding; the engine-contract pin 2 passed). **F2 the 82nd standing checks ALL GREEN** (version-bumped from v81 across the THREE token families — v81→v82, 81st→82nd, AND the bare session names ref81→ref82/clone81→clone82, version-bump-only diffs verified by normalizing back; the mobile menu VERIFIED WORKING the 82nd consecutive time; the reference's four bugs ALL live [toast-blocker, sheet-trap, no-landmark, the 464px /networth overflow]; the data census the 82nd clean drift check; the SEO pair live both sides).

**F3 the re-run pair** (vlm-shots-v88.sh + clone-vlmshots-v88.sh + vlm-compare-v88.mjs + arbit-v88.sh — the sed derivation from the v82 series with the version + session-name + tmp-dir substitutions [the bare-number tmp-dir family /tmp/vlm82→/tmp/vlm88 caught by the grep, the v84 lesson's second face], the headers history-corrected to the fourth re-run; login on the first attempt both sides; the parked pointer at (5,5); read-only on the reference): **the NETWORTH verdict IDENTICAL** (zero style flags — matching the v82 re-run's own verdict; the VLM's only note the Base44 FAB, the platform-chrome class). **The DRILL-DOWN verdict DIFFERENT with seven flags** — six the documented classes (the v56 nav-highlight superset; the user-identity avatar; the pct × 568 progress DATA class [fillW 173-vs-357 — the v60 arbitration's own values REPRODUCED EXACTLY, five re-runs later]; the v60 donut-labels PERCEPTION class re-arbitrated live; the seed-data classes; the platform-chrome class) — **and ONE NEW FLAG ("the stat-card footer divider lines missing in the reference") a VLM MISREAD disproven by the dedicated one-shot both-sides census (stat-divider-arbit-v88.sh — the v87 close-arbit precedent)**: the divider renders BYTE-IDENTICALLY on both sides (the count row h 20/w 254/flex/gap 8px/center/14px/rgb(10,10,10) with rowChildTags [SPAN, DIV, svg]; the divider {DIV, h 1, bg rgb(229,231,227), flexGrow 1} on every card; the trend icons 16×16 with the per-type colors; the width 177-vs-170 the flex-1 data-conditional remainder). **The census (arbit-v88.sh — the v75 convention) reproducing the v82 values EXACTLY — zero drift on every axis** (PART B: the card 960×333/32px/16px/gradient/shadow; the headRow 76/32px/flex/center; the label/figure/medallion/statGrid/statTile/ratioFooter families — the labelBlock width 304-vs-357 the standing DATA-CONDITIONAL class; PART A: the nav highlight the v56 class, the progress track byte-identical, the donut label chrome byte-identical, the stat trend icons byte-identical, the hero trend glyphs byte-identical). NO NEW CLONE GAP.

**F4 the v88 pin (+1 e2e = 291)**: the stat-card COUNT-ROW + DIVIDER census at 1280 (tests/e2e/dashboard.spec.ts — the never-pinned families: the count row's full chrome {h 20/flex/gap 8px/center/14px/rgb(10,10,10)} + the h-px flex-1 divider {tag DIV/h 1px/bg rgb(229,231,227)/flexGrow 1 — never pinned at ANY viewport} + the trend icon's per-type color trilogy {income lime/savings blue/expenses orange — the stat-card twin of the v80/v85 dot trilogy} + the docSW guard; the divider's WIDTH excluded — the flex-1 data-conditional remainder, the v82 convention) — the pin's own axes first measured byte-identical on both sides by the supplemental census (stat-divider-arbit-v88.sh) — **GREEN on first run**; **the pin-sanity mutation** the viewport-scoped h-px → h-px lg:h-0.5 (dashboard-view.tsx:618, by LINE NUMBER) verified to FAIL at exactly the divider.height axis ("1px" → "2px") — **cascade-free BY CONSTRUCTION** (the flex items-center row's height stays the text's 20px line box; the card height 210 unchanged — the v40 F1 bands green; the full dashboard.spec.ts under the mutation: **39 green, only the v88 pin red**) — then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines; the post-restore full run **40/40 green**); **the finder/assertion decoupling lesson**: the first draft's height-filtered finder returned null under the mutation (the diff degraded to null-vs-object) — the structural middle-child finder (never the text span, never the svg) keeps the element findable and the diff axis-alone; the disproven-in-advance candidates documented (the inline-style bg mutation, the trend-color trilogy cascade, the v86 ratio-line-height trap on the fs axis).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **291 e2e** (104+129+60 chunk executions = 293 = 291 unique tests, zero flakes) · 35/35 smoke ✓; the screenshots **16/16 BYTE-IDENTICAL** (the same-day-seed byte-identity law — the fresh seed planted and shot on the same calendar day 2026-10-18 reproduce the committed set byte-for-byte; no pixel arbitration needed); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v88 paragraph), D2 CLAUDE.md (291 + the v88 pin clause), D3 README.md (the counts + the v88 plan-table row), D4 zero-balance_SKILL.md (Session 123 audit row + the state line), D5 the PAD's v1.1.45 revision block, D6 the probe README's v88 section (the divider-visibility-misread + finder-assertion-decoupling + sed-tmp-dir-token lessons), D7 session_212.md + this entry.

**The next queue:** the v89 cycle — the v83-era DASHBOARD pair (the dashboard FULL-PAGE at desktop 1280 — the below-the-fold Budget Guidelines card + the quick-action row, last re-shot v83, now the oldest remaining [v83 < v84 < v85 < v86 < v87 < v88]; the pair's FOURTH re-run [v61 → v68 → v77 → v83 → v89]); verify against the rotation ledger first, per protocol.

---

## Session 122 — Parity iteration v87: the re-run cycle's next-oldest candidate (the v81-era login + calculator pair's fourth re-run) + the axe watch (NO DRIFT) + the calculator close-button chrome census pin (PIN-ONLY) (2026-10-18)

**The cycle** (`docs/remediation-plan-v87.md` — the plan validated against the codebase before execution; the narrative: `docs/session_210.md`): the v86 plan's v87 queue suggestion agreeing with the rotation ledger (the TENTH consecutive agreement) — the v81-era LOGIN + CALCULATOR pair (the login view + the calculator dialog at desktop 1280, last re-shot v81, the oldest remaining [v81 < v82 < v83 < v84 < v85 < v86]); the pair's FOURTH re-run [v59 → v66 → v75 → v81 → v87]. **PIN-ONLY for src/ — no production-code change; +1 e2e = 290.**

**The baseline — the PRESERVED workspace (the v81 precedent — no reset)**: git pull fast-forward 5c4818e..40cee12 (the session_209 transcript only), the tree clean; the environment verified in place (.env [DATABASE_URL=file:../db/custom.db], db/ at the repo root, node_modules + prisma, chromium-1243); the seedcheck exact [7/1850/2235/0/3/2] before any flow: lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ · 291 e2e chunk executions (102+110+79 = 289 unique = the documented v86 state) ✓ · 35/35 smoke ✓. **The audit clean** (the v86 commit 858ad21 verified PIN-ONLY [27 files, +1500/-5, ZERO src/ changes]; the two commits since session-log-only; the production seams re-audited; skills/ excluded throughout [eslint + tsconfig verified]). **F1 axe watch: NO DRIFT** (npm-latest 4.14.0, only rc prereleases beyond, no 5.x; the v68 dedupe state holding; the engine-contract pin 2 passed). **F2 the 81st standing checks ALL GREEN** (version-bumped from v80 across the THREE token families — v80→v81, 80th→81st, AND the bare session names ref80→ref81/clone80→clone81; the mobile menu VERIFIED WORKING the 81st consecutive time; the reference's four bugs ALL live [toast-blocker, sheet-trap, no-landmark, the 464px /networth overflow]; the data census the 81st clean drift check; the SEO pair live both sides).

**F3 the re-run pair** (login-shots-v87.sh + vlm-shots-v87.sh + clone-login-shots-v87.sh + clone-vlmshots-v87.sh + vlm-compare-v87.mjs — the sed derivation from the v81 series with the version + session-name/tmp-dir substitutions, grep-verified clean, the headers history-corrected to the fourth re-run; login on the first attempt both sides; the parked pointer at (5,5); read-only on the reference; the clone twin's fixture FULLY restored): **the LOGIN verdict IDENTICAL** (zero style flags — the third consecutive; the VLM's only note the reference's Base44 FAB, the platform-chrome class). **The CALCULATOR verdict DIFFERENT with the SAME three flag-set classes as v75/v81** (the v66 DATA-CONDITIONAL will-update span [hasWillUpdateSpan ref false vs clone true]; the POINTER-POSITION perception class [actionsAtRest {opacity 0, btnCount 2} BYTE-IDENTICAL]; the row-height VLM MISREAD [the row 720×102 BYTE-IDENTICAL]). **The census (arbit-v87.sh — the v75 convention) reproducing the v81 values EXACTLY — zero drift on every axis** (the panel 768×393/16px/white; the scrim rgba(26,58,46,0.5)/blur(8px)/1280×800; the title 18px/700/lh 28px/forestDark; the desc 14px/lh 20px/gray; the totalCard 720×90; the nameH4 16/600/h 24/mb 4px; the row 720×102; the pillRow/pill1 family; the amountP 20/700/orange/h 28; the addBtn 110×32/radius 6px; the docSW 1280). **THE NEW REFERENCE-SIDE OBSERVATION**: the reference's calculator close button LOST its accessible name (the close-arbit-v87.sh button-inventory probe: aria-label and textContent both empty — a bare SVG ×; the v81 census still found it by name) while its chrome stayed byte-identical (36×36/radius 6px/transparent/0px border) — the clone retains aria-label="Close" (the superset behavior, functionally pinned by every dialog interaction). NO NEW CLONE GAP.

**F4 the v87 pin (+1 e2e = 290)**: the calculator CLOSE-BUTTON chrome census at 1280 (tests/e2e/calculator.spec.ts — the never-pinned axes: the close's radius "6px"/bg rgba(0,0,0,0)/borderTopWidth "0px"/display "flex" — no spec asserted the calculator close's radius/bg/border at ANY viewport; the {36,36} re-affirming v59; the 0px-border computed-COLOR excluded, the v66 INVISIBLE class) — the pin's own axes first measured byte-identical on both sides by the supplemental census (pair-arbit-v87.sh — the v84/v85/v86 one-shot precedent; it also census-recorded the LOGIN half's never-pinned axes [the card's outer pad 0px + the inner pad 48px 40px 40px + the logo's own radius 0px] for the pair's next rotation) — **GREEN on first run**; **the pin-sanity mutation** the viewport-scoped rounded-md → rounded-md lg:rounded-lg (calculator-dialog.tsx:138, by LINE NUMBER) verified to FAIL at exactly the close.radius axis ("6px" → "8px") — **cascade-free BY CONSTRUCTION** (border-radius never affects w/h: the v49/v53/v59 geometry pins green under it; the item-details close pin a different component; the full calculator.spec.ts under the mutation: **16 green, only the v87 pin red**) — then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines; the post-restore full run **17/17 green**); the disproven-in-advance candidates documented in the plan without execution (the v86 ratio-line-height trap; the login pad height cascade).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **290 e2e** (103+110+79 chunk executions = 292 = 290 unique tests, zero flakes) · 35/35 smoke ✓; the screenshots **16/16 BYTE-IDENTICAL** (the same-db regeneration law — the preserved v86-cycle db + same-day shots reproduce the committed set byte-for-byte, even the v86 rasterization-noise file; no re-seed, no pixel arbitration); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v87 paragraph), D2 CLAUDE.md (290 + the v87 pin clause), D3 README.md (the counts + the v87 plan-table row), D4 zero-balance_SKILL.md (Session 122 audit row + the state line), D5 the PAD's v1.1.44 revision block, D6 the probe README's v87 section (the name-independent-finder + reference-regression-class + same-db-regeneration-law lessons), D7 session_210.md + this entry.

**The next queue:** the v88 cycle — the v82-era networth + drill-down pair (the networth view + the dashboard drill-down EXPANDED at 1280, last re-shot v82, now the oldest remaining [v82 < v83 < v84 < v85 < v86 < v87]); verify against the rotation ledger first, per protocol.

---

## Session 121 — Parity iteration v86: the re-run cycle's next-oldest candidate (the v80-era savings pair's fourth re-run) + the axe watch (NO DRIFT) + the savings goal-card's subtitle-P + header-row + wrapper-third-leg census pin (PIN-ONLY) (2026-10-18)

**The cycle** (`docs/remediation-plan-v86.md` — the plan validated against the codebase before execution, the mutation refutations included; the narrative: `docs/session_206.md`): the v85 plan's v86 queue suggestion agreeing with the rotation ledger (the NINTH consecutive agreement) — the v80-era SAVINGS pair (the savings view at desktop 1280x800, last re-shot v80, the oldest remaining [v80 < v81 < v82 < v83 < v84 < v85]); the pair's FOURTH re-run [v58 → v65 → v74 → v80 → v86]. **PIN-ONLY for src/ — no production-code change; +1 e2e = 289.**

**The baseline — the RESET workspace (the fresh-clone path, the second exercise after v80)**: git clone at main @ 0d20198, the tree clean; the environment re-provisioned (npm ci 354 packages + the four approved install scripts; .env written [DATABASE_URL=file:../db/custom.db, db/ at the repo root, db:push in-sync + db:seed]; chromium-1243 installed; the paramiko shim deployed); the seedcheck exact [7/1850/2235/0/3/2] before any flow: lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ · 290 e2e chunk executions (102+109+79 = 288 unique = the documented v85 state) ✓ · 35/35 smoke ✓. **The audit clean** (the v85 commit d92b352 verified PIN-ONLY [20 files, +1611/-6, ZERO src/ changes]; the two commits since session-log-only; the production seams re-audited — auth scrypt/timingSafeEqual/HMAC, db-path, the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout [eslint + tsconfig verified]). **F1 axe watch: NO DRIFT** (npm-latest 4.14.0, only rc/next prereleases beyond, no 5.x; the v68 dedupe state holding; the engine-contract pin 2 passed). **F2 the 80th standing checks ALL GREEN** (version-bumped from v79 with the THREE token families — v79→v80, 79th→80th, AND the bare session names ref79→ref80/clone79→clone80, the third family caught this cycle; the mobile menu VERIFIED WORKING the 80th consecutive time; the reference's four bugs ALL live [toast-blocker, sheet-trap, no-landmark, the 464px /networth overflow]; the data census the 80th clean drift check; the SEO pair live both sides).

**F3 the re-run pair** (vlm-shots-v86.sh + clone-vlmshots-v86.sh + vlm-compare-v86.mjs — the sed derivation from the v80 series with the version + session-name/tmp-dir substitutions, grep-verified clean, the headers history-corrected to the fourth re-run; login on the first attempt both sides; the parked pointer at (5,5); read-only on the reference): **the verdict IDENTICAL — the pair's FIRST non-DIFFERENT verdict in its five-shot history** (the VLM's own flags confined to the expected data/identity classes — the subtitle counts, the card figures/names/badges, the avatar — zero layout/style flags), **the census still run per the v75 convention (arbit-v86.sh) and reproducing the v80 census values EXACTLY — zero drift on every axis** (the header; the grid 960/16px/~309 template; the card box with the v70b wrap class [ref 200 vs clone 230]; the titleRow with the savings blue dot; the amount leaf 24px/700/32px/blue; the footer + badge chrome with the v58 DATA-CONDITIONAL + v57 wrap classes; the docSW 1280). The supplemental census (wrapper-arbit-v86.sh): the savings wrapper {block/flex-1/pr 0px/w 231/h 48} + the subtitle P {h 20/fs 14px/lh 20px/rgb(107,114,128)/mt 0} + the titleRow mb 4px + the headerRow {flex/space-between/flex-start/h 48/mb 12px} — all byte-identical on both sides (the subtitle TEXT "Home Savings" vs "Index Funds" the data class). **NO NEW GAP.**

**F4 the v86 pin (+1 e2e = 289)**: the savings goal-card's SUBTITLE-P + HEADER-ROW + WRAPPER-THIRD-LEG census at 1280 (tests/e2e/items.spec.ts — the never-pinned families: the subtitle P's full chrome [the 1280 state of the v51 F3 390-only family — no 1280 subtitle pin anywhere] + the with-subtitle arithmetic [the titleRow mb 4px + the headerRow's own geometry, never pinned at 1280] + the wrapper's savings paddingRight-0 third leg [completing the v85 pr-conditional trilogy — expenses 96px / income 0 / savings 0]) — GREEN on first run; **the pin-sanity mutation (the executed form)** the viewport-scoped items-start → items-start lg:items-center at item-card.tsx:118 (the v80 responsive-variant dodge on the sibling row — inert at 390, no height change at 1280) verified to FAIL at exactly the headerRow.alignItems axis (flex-start → center) — cascade-free (the full items.spec.ts under the mutation: **38 green, only the v86 pin red**) — then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines; the post-restore full run **39/39 green**); **two DISPROVEN candidates kept as lessons**: the fs-axis text-sm → lg:text-[15px] refuted by the TAILWIND V4 RATIO-LINE-HEIGHT TRAP (text-sm's lh is the unitless ratio calc(1.25/0.875) — any fs override scales the lh and the heights cascade [the v80 pin measured 254 under it]), and the type-scoped conditional extension refuted by the NARROWED-CONTENT WRAP CASCADE (the pr-96 box at 137px wraps the Emergency Fund h4 +24, the grid stretches both cards to 254).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **289 e2e** (102+110+79 chunk executions = 291 = 289 unique tests, zero flakes) · 35/35 smoke ✓; the screenshots **10/16 BYTE-IDENTICAL + 6/16 benign-pixel-arbitrated** (5 DATE-TEXT-ONLY [03/04/05/06/16 — the fresh-seed +1-day, every diff crop single-image VLM-arbitrated: the day number +1, the chrome byte-identical] + 1 RASTERIZATION-NOISE [08-calculator: ±1-channel gradient rounding in a 55×74 band, no text, no layout, both crops VLM-read identical]; the regenerated set ships per the v80 discipline); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v86 paragraph), D2 CLAUDE.md (289 + the v86 pin clause), D3 README.md (the counts + the v86 plan-table row), D4 zero-balance_SKILL.md (Session 121 audit row + the state lines), D5 the PAD's v1.1.43 revision block, D6 the probe README's v86 section (the ratio-line-height-trap + narrowed-content-wrap-cascade + identical-verdict-census + third-token-family + benign-noise lessons), D7 session_206.md + this entry.

**The next queue:** the v87 cycle — the v81-era LOGIN + CALCULATOR pair (the login view + the calculator dialog at desktop 1280, last re-shot v81, now the oldest remaining [v81 < v82 < v83 < v84 < v85 < v86]); verify against the rotation ledger first, per protocol.

---

## Session 120 — Parity iteration v85: the re-run cycle's next-oldest candidate (the v79-era items pair's fourth re-run) + the axe watch (NO DRIFT) + the expense-card content-wrapper + orange-dot titleRow census pin (PIN-ONLY) (2026-10-18)

**The cycle** (`docs/remediation-plan-v85.md` — the plan validated against the codebase before execution; the narrative: `docs/session_203.md`): the v84 plan's v85 queue suggestion agreeing with the rotation ledger (the EIGHTH consecutive agreement) — the v79-era ITEMS pair (the income + expenses view pair at desktop 1280x800, last re-shot v79, the oldest remaining [v79 < v80 < v81 < v82 < v83 < v84]); the pair's FOURTH re-run [v57 → v64 → v70 → v79 → v85]. **PIN-ONLY for src/ — no production-code change; +1 e2e = 288.**

**The baseline** — the preserved workspace (git pull at main @ 3f92b87, the tree clean; node_modules + chromium-1243 + .env [DATABASE_URL=file:../db/custom.db, db/ at the repo root] all in place; the seedcheck exact [7/1850/2235/0/3/2]): lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ · 289 e2e chunk executions (102+104+83 — the documented v84 total) ✓ · 35/35 smoke ✓. **The audit clean** (the v84 commit f66e76d verified PIN-ONLY [22 files, +1354/-6, ZERO src/ changes]; the two commits since session-log-only; the production seams re-audited — auth scrypt/timingSafeEqual/HMAC, db-path, the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout [eslint + tsconfig verified]). **F1 axe watch: NO DRIFT** (npm-latest 4.14.0, only rc/next prereleases beyond, no 5.x; the v68 dedupe state holding; the engine-contract pin 2 passed). **F2 the 79th standing checks ALL GREEN** (version-bumped from v78 — version-bump-only diffs verified; the mobile menu VERIFIED WORKING the 79th consecutive time; the reference's four bugs ALL live [toast-blocker, sheet-trap, no-landmark, the 464px /networth overflow]; the data census the 79th clean drift check; the SEO pair live both sides).

**F3 the re-run pair** (vlm-shots-v85.sh + clone-vlmshots-v85.sh + vlm-compare-v85.mjs — the sed derivation with BOTH the version AND the session-name/tmp-dir substitutions per the v84 lesson, grep-verified clean; login on the first attempt both sides; the parked pointer at (5,5); read-only on the reference): both verdicts DIFFERENT with every flag DOM-arbitrated to a documented class — the INCOME flags the user-identity + seed-data classes + ONE NEW FLAG (the "Edit with Base44" FAB claimed present in the CLONE) **disproven as a VLM IMAGE-ATTRIBUTION SWAP by the two-step arbitration** (base44-fab-arbit-v85.sh: the DOM census finds ZERO Base44 elements on EITHER side — the platform FAB renders outside the queryable body text; crop-fab-v85.mjs + vlm-arbit-fabcrop-v85.mjs: the pixel census locates the dark FAB pixels in the REFERENCE shot's corner ONLY [6585 vs 0 dark px in the 340x100 crops] and the single-image VLM reads confirm it — the platform-chrome class on the reference, the documented class since v57); the EXPENSES flags the v57 DATA-CONDITIONAL chips + the Recurring superset wrap + the user-identity + the seed classes — matching the v79 re-run's own flag-set classes exactly. **The both-sides census (arbit-v85.sh — the v75 convention): the v79 census values REPRODUCED EXACTLY — zero drift on every axis** (the avatar chrome; the grid 960/16px/309.328; the card box + the h 200-vs-230 v70b class; the titleRow chrome with the per-type dots; the amount leaf + accents; the footer + badge chrome; both filter-card variants; the docSW 1280). The wrapper-family supplemental census (wrapper-arbit-v85.sh): the expense-only pr-24 wrapper + the income pr-0 control + the titleRow's full geometry + the h4's forestDark + the hover action row — all byte-identical on both sides. **NO NEW GAP.**

**F4 the v85 pin (+1 e2e = 288)**: the expense-card CONTENT-WRAPPER + orange-dot titleRow census at 1280 (tests/e2e/items.spec.ts — the never-pinned families: the expenses-conditional pr-24 wrapper [item-card.tsx:119 — the ONLY pr-24 in src] {display block/flexGrow 1/paddingRight 96px} + the income twin's paddingRight-0 control + the titleRow's full geometry {flex/center/8px/h 24 + the dot 8x8/9999px in the expenses orange rgb(224,122,59) — the orange twin's first pin anywhere, the v80 savings blue twin's per-type trilogy completed — + the h4 16px/600/rgb(26,58,46)}) — GREEN on first run; the pin-sanity mutation the wrapper's pr-24 → pr-20 (by LINE NUMBER) verified to FAIL at exactly the wrapper.paddingRight axis ("96px" → "80px") — cascade-free by construction (the titleRow family content-governed; the amount/badge/footer rows wrapper-external siblings; the action row absolute; the income/savings wrappers pr-free; the 390 subtitle texts single-line at both paddings; the full items.spec.ts under the mutation: **37 green, only the v85 pin red**) — then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines; the post-restore full run **38/38 green**).

**F5 the full chain re-run GREEN**: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **288 e2e** (102+105+83 chunk executions = 290 = 288 unique, zero flakes) · 35/35 smoke ✓; the screenshots **16/16 BYTE-IDENTICAL** (the fifteenth consecutive fully-identical set — the same-day seed law; the v84 cycle's DATE-class modal diff resolved by the same calendar day); the final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v85 paragraph), D2 CLAUDE.md (288 + the v85 pin clause), D3 README.md (the counts + the v85 plan-table row), D4 zero-balance_SKILL.md (Session 120 audit row + the state lines), D5 the PAD's v1.1.42 revision block, D6 the probe README's v85 section (the image-attribution-swap + type-scoped-mutation + fourth-run-stability lessons), D7 session_203.md + this entry.

**The next queue:** the v86 cycle — the v80-era SAVINGS pair (the savings view at desktop 1280, last re-shot v80, now the oldest remaining [v80 < v81 < v82 < v83 < v84 < v85]); verify against the rotation ledger first, per protocol.

---

## Session 119 — Parity iteration v84: the re-run cycle's next-oldest candidate (the mobile 390 twins' third re-run) + the axe watch (NO DRIFT) + the networth ratio-footer divider + label census pin (PIN-ONLY) (2026-10-18)

**Goal:** the v84 queue — the ledger-verified target (the v83 plan's suggestion agreeing with the rotation ledger: the mobile 390 twins [the networth + dashboard FULL-PAGE pair at 390x844], last re-shot v78, is the oldest remaining candidate [v78 < v79 < v80 < v81 < v82 < v83]; the pair's THIRD re-run [v62/v63 → v69 → v78 → v84] — the seventh consecutive queue/ledger agreement), plus the axe-core watch at its re-check point and the 78th standing checks. PIN-ONLY for src/ — no production-code change; +1 e2e = 287.

**The workspace PRESERVED (the v81-style path — no reset):** `git pull` landed at `main @ 2b2ba34` (v83 shipped at e0f32ff + the session_198/199 transcripts), the tree clean; node_modules in place (354 packages), chromium-1243 in place, `.env` verified (DATABASE_URL="file:../db/custom.db", db/ at the repo root), the seedcheck exact (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran, no orphaned servers.

**The baseline chain FULLY GREEN as-shipped on the preserved workspace:** lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · 286 e2e ✓ (102 + 108 + 78 chunk executions = 288 total = 286 unique tests — the exact documented v83 state) · 35/35 smoke ✓.

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (no 5.x exists), the lockfile holding the v68 dedupe state, the engine-contract pin GREEN standalone (2 passed).

**The 78th standing checks ALL GREEN:** the mobile menu VERIFIED WORKING (the 78th consecutive time — `hitIsBurgerChild:true`, the sheet opens + closes on nav, the nav landmark present); the reference's four bugs ALL live [toast-blocker, sheet-trap, no-landmark, the 464px /networth overflow]; the data census UNCHANGED (the 78th clean drift check); the SEO pair live on both sides; zero overflow at 390 on all five clone views.

**The re-run pair (the mobile 390 twins at 390x844):** both verdicts DIFFERENT with every flag DOM-arbitrated to a documented class — the NETWORTH flags the v41 mobile-superset + seed-data + platform-chrome classes, with the one NEW flag ("the divider missing in the clone") a VLM MISREAD disproven by the dedicated one-shot both-sides arbitration (ratio-divider-arbit-v84.sh: the divider byte-identical — borderTop 1px solid rgba(255,255,255,0.2), mt 24/pt 24, footer h 53, label 14px/400/156×20); the DASHBOARD flags the v62 width-delta + pct-data + platform-chrome + seed-data classes — matching the v78 re-run's own flag-set classes exactly. The both-sides census (arbit-v84.sh — the v78 census axes re-measured): **the v78 census values REPRODUCED EXACTLY — zero drift since v78 on every axis** (the networth medallion 64×64 + trend icon 32×32 + tiles h 84 + grid gap 16px byte-identical; the dashboard subtitle chrome + the breakdown card's svg family + chart-absence byte-identical). NO NEW GAP.

**The v84 pin (+1 e2e = 287):** the networth summary card's RATIO-FOOTER census at 390 (tests/e2e/networth.spec.ts — the never-pinned family at the mobile viewport: the border-t family + the mt-6/pt-6 rhythm + the value-governed h 53 + the ratio label's 14px/400/156×20) — GREEN on first run; the pin-sanity mutation (the ratio label's `text-sm` → `text-xs lg:text-sm` at net-worth-view.tsx:389, by LINE NUMBER) verified to FAIL at exactly the pin's label axes (fs 14→12, h 20→16, w 156→134) — cascade-free by construction (desktop-restored: the v82/v67/v4-era 1280 pins all green under the mutation; the full networth.spec.ts under the mutation: 27 green, only the v84 pin red) — then restored (the standalone REBUILD as a SEPARATE command; `git diff src/` = 0 lines; the post-restore full run 28/28 green).

**The full chain re-run GREEN:** lint → typecheck → 108 unit → `npm run build` → 287 e2e (102 + 108 + 79 chunk executions = 289 total = 287 unique tests; one transient Liabilities-tab flake in the first chunk-3 run re-verified GREEN standalone twice + in-chunk) → 35/35 smoke. The screenshots **15/16 BYTE-IDENTICAL + 1/16 DATE-class pixel-arbitrated** (the 07-add-item-modal diff: 229 pixels in a 7×11 CSS box, the crop pair VLM-read — the modal's default-DATE field 10/17/2026 → 10/18/2026, the UTC calendar rollover; DATE-TEXT-ONLY per the v80 discipline, the chrome byte-identical). The final seedcheck exact.

**The docs alignment:** D1 AGENTS.md (the v84 paragraph), D2 CLAUDE.md (287 + the v84 pin clause), D3 README.md (the counts + the v84 plan-table row), D4 zero-balance_SKILL.md (Session 119 audit row + the state lines), D5 the PAD's v1.1.41 revision block, D6 the probe README's v84 section, D7 session_200.md + this entry.

**The v84 lessons:** (1) THE DIVIDER-MISREAD DISPROOF — a VLM "missing element" claim is disproven by a one-shot both-sides census of that element's computed chrome (the inline-style border family measured byte-identical); (2) THE SED-SUBSTITUTION GAP — versioned probe derivations need BOTH the version AND the session-name/tmp-dir substitutions ("v78" never matches "vlm78" as a substring — always grep the derived script for the old version string before running); (3) THE DESKTOP-RESTORED INVERSE MUTATION — for mobile-pinned axes, mutate the BASE class + restore under lg: (text-sm → text-xs lg:text-sm): the 390 axes flip while every 1280 pin stays green.

---

## Session 118 — Parity iteration v83: the re-run cycle's next-oldest candidate (the v61-era dashboard pair's third re-run) + the axe watch (NO DRIFT) + the cross-row vertical-rhythm census pin (PIN-ONLY) (2026-10-18)

**Goal:** the v83 queue — the ledger-verified target (the v82 plan's suggestion agreeing with the rotation ledger: the v61-era dashboard pair [the dashboard FULL-PAGE at desktop 1280 — the below-the-fold Budget Guidelines card + the quick-action row], last re-shot v77, is the oldest remaining candidate [v77 < v78 < v79 < v80 < v81 < v82]; the pair's THIRD re-run [v61 → v68 → v77 → v83] — the sixth consecutive queue/ledger agreement) + the axe-core watch + the 77th standing checks. PIN-ONLY for src/ — no production-code change; +1 e2e = 286.

**The environment REBUILT (the reset path — the third consecutive reset-boundary)**: the workspace had been reset — `git clone` landed at `main @ 7b28990` (v82 shipped + the session_195 transcript), the tree clean; node_modules reinstalled (354 packages), chromium-1243 reinstalled, `.env` rewritten (DATABASE_URL="file:../db/custom.db", db/ at the repo root — the polluting shell DATABASE_URL handled via the npm scripts' `env -u` discipline), `prisma generate` + `npm run db:push` + `npm run db:seed` re-run, the seedcheck exact (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran. The codebase audit (per the user's review request): the recent v81/v82 commits verified PIN-ONLY as documented; the production seams (auth, db-path, the SEO pair, the Tailwind v4 mitigations in globals.css, the three test tiers) re-audited clean — no new findings; the repo's `skills/` folder excluded from checking/testing/compilation throughout (the eslint + tsconfig excludes verified).

**The baseline chain FULLY GREEN as-shipped on the rebuilt workspace**: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · 285 e2e ✓ (101 + 108 + 78 chunk executions = 287 total = 285 unique tests in 23 files — the exact documented v82 state) · 35/35 smoke ✓.

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (no 5.x exists), the lockfile holding the v68 dedupe state, the engine-contract pin GREEN standalone (2 passed).

**The 77th standing checks ALL GREEN:** the mobile menu VERIFIED WORKING (the 77th consecutive time — `hitIsBurgerChild:true`, the sheet opens + closes on nav, the nav landmark present); the reference's four bugs ALL live [toast-blocker, sheet-trap `overlayCount:1`, no-landmark, the 464px /networth overflow]; the data census UNCHANGED (the 77th clean drift check); the SEO pair live on both sides; zero overflow at 390 on all five clone views.

**The re-run pair (the dashboard FULL-PAGE at desktop 1280x800):** the DASHBOARD verdict **IDENTICAL** — the two v61-era target surfaces (the Budget Guidelines card + the quick-action row) identical on every reported chrome axis; the only deltas the seed classes + the documented non-chrome classes (the v56 SUPERSET nav state, the user-identity avatar, the Base44 platform overlay). The both-sides census (arbit-v83.sh — the v75 convention, the census runs regardless of the verdict; the v77 census axes re-measured): **the v77 census values REPRODUCED EXACTLY — zero drift since v77 on every axis** (PART G the guidelines card byte-identical modulo the v66 transparent-shadow class; PART Q the quick-action row byte-identical modulo the v77 mt-mechanism class [ref mt 0 vs clone 32px, the rendered gap IDENTICAL at 340] + the v61 label-finder wrapper class [the clone's LEAF carries the identical 500/rgb(26,58,46)]; PART X cardBottom 1122 / gridTop 1462 / gap 340 both sides). **NO NEW GAP.**

**The v83 pin (+1 e2e = 286):** the dashboard's CROSS-ROW vertical-rhythm census at 1280 (tests/e2e/dashboard.spec.ts — the never-pinned PART X family: the guidelines card's BOTTOM [1122 — the cumulative upstream rhythm], the quick-action grid's TOP [1462], the RENDERED cross-row gap [340 — the byte-identical both-sides parity axis], the grid's OWN mt [32px — the v51 F5 390 axis's desktop twin]) — GREEN on first run; the pin-sanity mutation (the quick-action grid's `mt-8` → `mt-8 lg:mt-6` at dashboard-view.tsx:993, applied by LINE NUMBER — the stat row's identical class string at :954 untouched) verified to FAIL at exactly the pin's own axes (mt 32→24, gridTop 1462→1454, gap 340→332; cardBottom 1122 unchanged) — cascade-free by construction (viewport-scoped: the 390/640 families untouched; the v61 F3 grid expectation carries no mt axis; the quick-action grid the LAST child of the view; the full dashboard.spec.ts under the mutation: 38 green, only the v83 pin red) — then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines; 39/39 green after).

**The full chain re-run GREEN:** lint → typecheck → 108 unit → `npm run build` → 286 e2e (102 + 108 + 78 chunk executions = 288 total = 286 unique tests) → 35/35 smoke. The screenshots **16/16 BYTE-IDENTICAL** (the fourteenth consecutive fully-identical set — the same-day seed + the same-day shots, the v82 same-day-seed law; the seedcheck exact).

**The docs alignment:** D1 AGENTS.md (the v83 paragraph), D2 CLAUDE.md (286 + the v83 pin clause), D3 README.md (the counts + the v83 plan-table row), D4 zero-balance_SKILL.md (Session 118 audit row + the state lines), D5 the PAD's v1.1.40 revision block, D6 the probe README's v83 section, D7 session_197.md + this entry.

**The v83 lessons:** (1) THE FULL-CENSUS REPRODUCTION — an IDENTICAL verdict still gets the both-sides census, and a census that reproduces the prior cycle's values exactly is the strongest zero-drift proof; (2) THE IDENTICAL-STRING LINE MUTATION — when two source lines carry identical class strings, apply pin-sanity mutations by LINE NUMBER, never by string replace; (3) THE MT-MECHANISM vs RENDERED-GAP DISTINCTION — a differing mechanism axis with byte-identical rendered geometry is a mechanism class, not a parity gap: pin the RENDERED axis.

---

## Session 117 — Parity iteration v82: the re-run cycle's next-oldest candidate (the v60-era networth + drill-down pair's third re-run) + the axe watch (NO DRIFT) + the summary card's completion-family census pin (PIN-ONLY) (2026-10-18)

**Goal:** the v82 queue — the ledger-verified target (the v81 plan's suggestion agreeing with the rotation ledger: the v60-era networth + drill-down pair [the networth view + the dashboard drill-down EXPANDED at desktop 1280, last re-shot v76] is the oldest remaining candidate [v76 < v77 < v78 < v79 < v80 < v81]; the pair's THIRD re-run [v60 → v67 → v76 → v82] — the fifth consecutive queue/ledger agreement), plus the axe-core watch at its re-check point and the 76th standing checks. **PIN-ONLY for src/ — no production-code change; +1 e2e = 285.** The formal narrative: `docs/session_194.md`; the plan: `docs/remediation-plan-v82.md`.

**The environment REBUILT (the reset path — the second consecutive reset-boundary)**: the workspace had been reset — `git clone` landed at `main @ edb4707` (v81 shipped + the session_193 transcript), the tree clean; node_modules reinstalled (354 packages), chromium-1243 reinstalled, `.env` rewritten (DATABASE_URL="file:../db/custom.db", db/ at the repo root), `prisma generate` + `npm run db:push` + `npm run db:seed` re-run, no orphaned servers, the seedcheck confirming the exact seed (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran.

**The baseline chain FULLY GREEN as-shipped on the rebuilt workspace**: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap; the standalone static + public copies verified) · 284 e2e ✓ (104 + 104 + 78 chunk executions = 286 total = 284 unique tests in 24 files [283 chromium + 1 setup] — the exact documented v81 state) · 35/35 smoke ✓.

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next prereleases; no 5.x exists), the lockfile holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core 4.14.0, no nested engine dir), the engine-contract pin GREEN standalone (2 passed).

**The 76th standing checks ALL GREEN:** the mobile menu VERIFIED WORKING (the 76th consecutive time — `hitIsBurgerChild:true`, the sheet opens + closes on nav, the nav landmark present); the reference's four bugs ALL live [toast-blocker, sheet-trap `overlayCount:1`, no-landmark, the 464px /networth overflow]; the data census UNCHANGED (the 76th clean drift check: "1 items · $25,000" / "1 items · $5000.00" / "4 items · $525.00"); the SEO pair live; zero overflow at 390 on all five clone views.

**The re-run pair (the networth view + the dashboard drill-down EXPANDED at desktop 1280x800):** the NETWORTH verdict **IDENTICAL** (the only layout/style flag the reference's Base44 overlay — the platform-chrome class; every other delta the seed classes — matching the v76 re-run's own networth verdict classes). The both-sides census (arbit-v82.sh PART B — the v76 census axes re-measured) BYTE-IDENTICAL on every chrome axis (the card 960×333/32px/16px/the 135deg forest→lime gradient/the 26-58-46 shadow; the head row 76/mb 32px/flex/center; the label 14px/white-80/mb 8px/h 20; the figure 48px/700/white/lh 48px/h 48; the medallion 64×64/white-20/icon 32×32; the stat grid 440px 440px/rows 84px/gap 16px/896×84; the stat tile 440×84/16px/12px/white-10/blur(10px)/label 12px-h16-mb4/amount 24px-700-h32; the ratio footer mt 24/pt 24/1px rgba(255,255,255,0.2)/h 53/label 14px/value 18px-700 — the ONE width delta the labelBlock w ref 304 vs clone 357 the DATA-CONDITIONAL figure-text class ["$25,000.00" vs "-$245,950.00" at the same 48px/700]). The DRILL-DOWN verdict **DIFFERENT with EIGHT flags, every one DOM-arbitrated to a documented class** (matching the v76 re-run's own flag-set classes): the nav highlight the v56 SUPERSET class (the reference's link INERT rgb(63,63,70)/400 vs the clone's ACTIVE white/500); the progress-bar length the pct × 568 DATA class — **the v60 arbitration's own values REPRODUCED EXACTLY** (fillW ref 173 vs clone 357 on the byte-identical 568×12 track, zero drift since v60); the extra expanded category + the footer count the seed-data class (the clone's 2 income categories vs the reference's 1); the donut proportions the seed-data class; the percentage-labels claim the v60 PERCEPTION class re-arbitrated live (the reference DOES render its labels — texts 92.3%/4.6%/3.1%, count 4 = 1 group + 3 labels, 0 lines, 16px, black, 3 sectors, the chrome byte-identical); the "Total Expense vs Total Expenses" a VLM MISREAD (the dedicated stat-title-ref-v82.sh probe: the reference's statTitles measured VERBATIM — the plural on BOTH sides, SPAN + H3, 14px/500/rgb(107,114,128), hasSingular:false; the clone's source renders the same plural, the v40 Tab-census pin holding the accessible name); the avatar the user-identity class; the Base44 overlay the platform-chrome class. **NO NEW GAP.**

**The v82 pin (+1 e2e = 285):** the networth summary card's COMPLETION-family census at 1280 (tests/e2e/networth.spec.ts — the never-pinned axes: the head row's ALIGNMENT [items "center" — the v80 titleRow.alignItems pattern's networth twin; the v67 pin holds the row's h/mb/display], the label block's HEIGHT [h 76 — the min-w-0 wrapper's own height], the stat grid's content-box WIDTH [w 896 — the 960 card − the 2×32 pad arithmetic twin], the ratio label's TYPOGRAPHY [fs "14px" — text-sm; G9 holds the color, the structure test the VALUE's 18px/700 + the tile label's 12px + the footer border's rgba]) — every pinned axis STATIC chrome (the labelBlock's WIDTH the data-conditional axis, EXCLUDED) — GREEN on first run; the pin-sanity mutation (the ratio label's `text-sm` → `text-sm lg:text-base` at net-worth-view.tsx:389) verified to FAIL at exactly the ratioLabel.fs axis ("14px" → "16px") — **cascade-free by construction** (viewport-scoped: below 1024px inert — the 390/640 families untouched; the value-governed ratio row keeping the v67 footer h 53 + the v60 value axes green; the G9 color pin + the structure test's ratioSize green; the full networth.spec.ts run under the mutation: 26 green, only the v82 pin red) — then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines; the post-restore full run 27/27 green).

**The full chain re-run GREEN:** lint → typecheck → 108 unit → `npm run build` → 285 e2e (105 + 104 + 78 chunk executions = 287 total = 285 unique tests) → 35/35 smoke. The screenshots **16/16 BYTE-IDENTICAL** (the thirteenth consecutive fully-identical set — the same-day seed + the same-day shots reproducing the committed set byte-for-byte, the v80 date-shift lesson's converse; the seedcheck under `env -u DATABASE_URL` confirming the exact seed state).

**The docs alignment:** D1 AGENTS.md (the v82 paragraph), D2 CLAUDE.md (285 + the v82 pin clause), D3 README.md (the counts + the v82 plan-table row), D4 zero-balance_SKILL.md (Session 117 audit row + the state lines), D5 the PAD's v1.1.39 revision block, D6 the probe README's v82 section, D7 session_194.md + this entry.

**The probe lessons:** (1) THE VERBATIM-TITLE MISREAD DISPROOF — a VLM flag that claims a TEXT difference is cheapest to disprove with a dedicated verbatim-DOM probe (the exact strings + tags + typography measured on the live reference): one probe settles what pixel-cropping never could, the v43 misattribution rule's text-twin; (2) THE CENSUS-ARITHMETIC REPRODUCTION — when a re-run's data-class delta reproduces a PRIOR arbitration's exact values (the fillW 173 vs 357 = the v60 numbers, five re-runs later), cite the reproduction explicitly: the strongest possible no-drift evidence for the standing chrome; (3) THE SAME-DAY-SEED BYTE-IDENTITY — a fresh seed planted and shot on the same calendar day reproduces the committed screenshot set byte-for-byte (the v80 date-shift lesson's converse: the date bands shift ONLY when the seed day and the shot day differ).

---

## Session 116 — Parity iteration v81: the re-run cycle's next-oldest candidate (the v59-era login + calculator pair's third re-run) + the axe watch (NO DRIFT) + the calculator header / addBtn / scrim census pin (PIN-ONLY) (2026-10-17)

**Goal:** the v81 queue — the ledger-verified target (the v80 plan's suggestion agreeing with the rotation ledger: the v59-era login + calculator pair [the login view + the calculator dialog at desktop 1280, last re-shot v75] is the oldest remaining candidate [v75 < v76 < v77 < v78 < v79 < v80]; the pair's THIRD re-run [v59 → v66 → v75 → v81] — the fourth consecutive queue/ledger agreement), plus the axe-core watch at its re-check point and the 75th standing checks. **PIN-ONLY for src/ — no production-code change; +1 e2e = 284.** The formal narrative: `docs/session_192.md`; the plan: `docs/remediation-plan-v81.md`.

**The environment preserved** (no reset — the v80-rebuilt workspace verified in place): `git pull` landed at `main @ 3cede95` (v80 shipped at 89772b1 + the session_191 transcript), the tree clean; `.env` (`DATABASE_URL="file:../db/custom.db"`), `db/` (custom.db + e2e.db), node_modules (354 packages), no orphaned servers; the seedcheck exact (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran.

**The baseline chain FULLY GREEN as-shipped** (no F0 finding — the v76 lesson applied by construction: `npm run build`, the standalone static + public copies verified): lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap) · 283 e2e ✓ (100 + 108 + 77 chunk executions = 283 unique tests in 23 files [282 chromium + 1 setup, the setup re-run per chunk as the project dependency] — the exact documented v80 state) · 35/35 smoke ✓.

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next prereleases; no 5.x exists), the lockfile holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core 4.14.0, no nested engine dir), the engine-contract pin GREEN standalone (2 passed).

**The 75th standing checks ALL GREEN:** the mobile menu VERIFIED WORKING (the 75th consecutive time — `hitIsBurgerChild:true`, the sheet opens + closes on nav, the nav landmark present); the reference's four bugs ALL live [toast-blocker, sheet-trap `overlayCount:1`, no-landmark, the 464px /networth overflow]; the data census UNCHANGED (the 75th clean drift check); the SEO pair live; zero overflow at 390 on all five clone views.

**The re-run pair (the login view + the calculator dialog at desktop 1280x800):** the LOGIN verdict **IDENTICAL with ZERO style flags** (matching the v75 re-run's own IDENTICAL verdict — zero drift since v75 on the VLM layer; the both-sides census byte-identical on every axis: the card 448/16px/rgba(255,255,255,0.95); the h1 30px/700/lh 36px/rgb(15,23,42); the subtitle 16px/rgb(100,116,139); the logo 96×96; the inputs 48/12px/14px/1px rgb(226,232,240); the Sign in 368×48/12px/14px/500/rgb(15,23,42); the Google + OR blocks both — the card's 0px-width border computed-color + the shadow's transparent lead-layer count the v66 computed-form INVISIBLE class). The CALCULATOR verdict DIFFERENT with THREE flags, every one DOM-arbitrated to a documented class (the "extra will-update line" the v66 DATA-CONDITIONAL class [hasWillUpdateSpan ref false — its Rent natively $25.00 === its line-item total; clone true — opened-at $1850]; the "hover buttons missing" the POINTER-POSITION perception class [actionsAtRest {opacity: 0, btnCount: 2} BYTE-IDENTICAL on both sides — the shots taken at different pointer phases]; the "row height shorter" a VLM MISREAD [the row 720×102 BYTE-IDENTICAL] — matching the v75 re-run's own flag-set classes exactly). The both-sides census (arbit-v81.sh — the v75 convention, the v75 census axes re-measured): the PANEL + SCRIM + TITLE + DESC + CLOSE + TOTALCARD + NAMEH4 + ROW + PILLROW + PILL1 + AMOUNTP + ADDBTN chrome all BYTE-IDENTICAL (the panel 768×393/16px/white/maxW 768px; the scrim rgba(26,58,46,0.5)/blur(8px)/1280×800; the title 18px/700/lh 28px/rgb(26,58,46); the desc 14px/lh 20px/rgb(107,114,128); the close 36×36; the totalCard 720×90/16px/12px/1px solid rgb(252,221,213); the nameH4 16/600/h 24/mb 4px; the row 720×102/16px/12px/1px solid rgb(229,231,227); the pillRow/pill1 family; the amountP 20/700/rgb(224,122,59)/h 28; the addBtn 110×32/radius 6px/12px/500/white; the docSW 1280 guard) — the panel shadow's transparent lead-layer count the v66 computed-form class (the visible layer byte-identical). The clone twin's fixture FULLY restored (the delete + Rent's $1850 re-edit + the "$2235.00" page-total verify; the seedcheck exact after). **NO NEW GAP.**

**The v81 pin (+1 e2e = 284):** the calculator dialog's HEADER family + Add Item button + SCRIM census at 1280 (tests/e2e/calculator.spec.ts — the never-pinned axes: the title's typography family [fs 18px/fw 700/lh 28px/color rgb(26,58,46) — the v53 390 pin's {fs, fw, color} twin completed with the NEVER-pinned lh axis], the desc's typography family [fs 14px/lh 20px/color rgb(107,114,128) — the v73 390 family's desktop twin], the addBtn's chrome [w 110/h 32/radius 6px/fs 12px/fw 500/color white — the v53 390 family's desktop twin, the radius never pinned at any viewport], the scrim [bg rgba(26,58,46,0.5)/blur blur(8px)/w 1280/h 800 — the v73 390 family's desktop twin]) + the docSW 1280 guard — every pinned axis STATIC dialog chrome, the pin riding the v59 read-only EMPTY-state discipline (hover → Calculate → census → Close, no fixture writes) — GREEN on first run; the pin-sanity mutation (the DialogTitle's `lg:text-xl` at calculator-dialog.tsx:127) verified to FAIL at exactly the title.fs axis ("18px" → "20px") — **cascade-free by construction** (the responsive variant inert at 390 — the v53 h2/header pins untouched; the v73 390 scrim/summary family untouched; the v59 pin asserts no title-dependent axis, the panel.y invariant holds for ANY panel height; the v66 height family lives in the panel body — the full calculator.spec.ts run under the mutation: 15 green, only the v81 pin red) — then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines).

**The full chain re-run GREEN:** lint → typecheck → 108 unit → `npm run build` → **284 e2e** (101 + 108 + 77 chunk executions = 284 unique tests) → 35/35 smoke. The screenshots **16/16 BYTE-IDENTICAL** (the twelfth consecutive fully-identical set — the same-day regeneration against the PRESERVED db, no calendar rollover, no fresh-seed date shift; the seedcheck under `env -u DATABASE_URL` confirming the exact seed state).

**The docs alignment:** D1 AGENTS.md (the v81 paragraph), D2 CLAUDE.md (284 + the v81 pin clause), D3 README.md (the counts + the v81 plan-table row), D4 zero-balance_SKILL.md (Session 116 audit row + the state lines), D5 the PAD's v1.1.38 revision block, D6 the probe README's v81 section, D7 session_192.md + this entry.

**The probe lessons:** (1) THE STATIC-CHROME READ-ONLY PIN — a dialog pin whose every axis is static chrome (title/desc/addBtn/scrim — none data-dependent) can ride the read-only EMPTY state, eliminating the fixture add/restore burden of the with-row pins; (2) THE POINTER-PHASE PERCEPTION CLASS — a screenshot pair taken at different pointer phases (the reference's pre-park shot vs the clone's post-park shot) makes hover-revealed chrome appear on one side only: the DOM census (actionsAtRest opacity) is the arbiter, not the pixels — aligning the pointer phase across the two shot scripts would prevent the flag at the source; (3) THE 0px-WIDTH BORDER COMPUTED-COLOR — a borderless surface's 0px border still carries a computed color (the ref's slate-200 form vs the clone's border token): an INVISIBLE computed-form class, never a parity gap.

---

## Session 115 — Parity iteration v80: the re-run cycle's next-oldest candidate (the v58-era savings pair's third re-run) + the axe watch (NO DRIFT) + the savings goal-card's double-wrap heights / title-row geometry / border-bg pin (PIN-ONLY) (2026-10-17)

**Goal:** the v80 queue — the ledger-verified target (the v79 plan's suggestion agreeing with the rotation ledger: the v58-era savings pair [the savings view at desktop 1280, last re-shot v74] is the oldest remaining candidate [v74 < v75 < v76 < v77 < v78 < v79]; the pair's THIRD re-run [v58 → v65 → v74 → v80] — the third consecutive queue/ledger agreement), plus the axe-core watch at its re-check point and the 74th standing checks. **PIN-ONLY for src/ — no production-code change; +1 e2e = 283.** The formal narrative: `docs/session_190.md`; the plan: `docs/remediation-plan-v80.md`.

**The environment REBUILT (the reset path exercised for the first time since v76)**: the workspace had been reset — `git clone` landed at `main @ 9d5c26a` (v79 shipped + the session_189 transcript), the tree clean; node_modules reinstalled (npm install, 37 deps), chromium-1243 reinstalled (npx playwright install chromium — the documented revision), `.env` rewritten (DATABASE_URL="file:../db/custom.db", db/ at the repo root), `prisma generate` + `npm run db:push` + `npm run db:seed` re-run (the polluting shell DATABASE_URL handled via the documented `env -u` discipline), no orphaned servers, the seedcheck confirming the exact seed (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran.

**The baseline chain FULLY GREEN as-shipped on the rebuilt workspace** (no F0 finding — the v76 lesson applied by construction: `npm run build`, the standalone static + public copies verified): lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap) · 282 e2e ✓ (101 + 122 + 61 chunk executions = 282 unique tests in 24 files [281 chromium + 1 setup, the setup re-run per chunk as the project dependency] — the exact documented v79 state) · 35/35 smoke ✓.

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next prereleases; no 5.x exists), the lockfile holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core 4.14.0, no nested engine dir), the engine-contract pin GREEN standalone (2 passed).

**The 74th standing checks ALL GREEN:** the mobile menu VERIFIED WORKING (the 74th consecutive time — `hitIsBurgerChild:true`, the sheet opens + closes on nav, the nav landmark present); the reference's four bugs ALL live [toast-blocker, sheet-trap `overlayCount:1`, no-landmark, the 464px /networth overflow]; the data census UNCHANGED (the 74th clean drift check); the SEO pair live; zero overflow at 390 on all five clone views.

**The re-run pair (the savings view at desktop 1280x800 full-page):** the verdict DIFFERENT with every flag a documented class (the single-card vs two-card grid the seed-count class; the footer's account-type chips the v58 DATA-CONDITIONAL class; the badge family the classification-VALUE + Recurring superset classes; the figures the seed-data class; the avatar the user-identity class — matching the v74 re-run's own flag set exactly). The both-sides census (arbit-v80.sh — the v75 convention, the v74 census axes re-measured PLUS the v80 titleRow geometry — the never-census'd axis): the HEADER + GRID + CARD chrome BYTE-IDENTICAL (grid 960 / gap 16px / the 3-col ~309px template; card 309 / pad 20px / radius 12px / border 1px solid rgb(229,231,227) / bg white — the card h ref-200 vs clone-230 the v70b-decomposed class: the Recurring superset badge's wrap h 52 [22+8+22] → +30px); **the TITLE ROW BYTE-IDENTICAL (display flex / gap 8px / alignItems center / row h 24 / the dot 8×8 / radius 9999px / dotBg rgb(59,126,161) — the savings blue on BOTH sides — the 1280 state of the v51/v54 390-only family)**; the INTERIOR TEXT BYTE-IDENTICAL (the h4 16px/600/lh 24px; the amount 24px/700/lh 32px/rgb(59,126,161)); the FOOTER + BADGE chrome BYTE-IDENTICAL (the footer childCount the v58 DATA-CONDITIONAL class; the badgeRow h 22 vs 52 the v57 wrap class); the docSW 1280 guard on both sides. **NO NEW GAP.**

**The stretch-twin attribution correction (the v80 probe's items-start experiment):** measuring the naturals with the grid's stretch disabled showed the income view at [200, 230] (the Salary card natural 200 with 3 badges; the Freelance card natural 230 with the 4-badge wrap) and the savings view at [230, 230] (BOTH cards 4-badge wrap naturals) — the v79 pin's income heights[0] 230 is the STRETCH twin (the Salary card stretched to the Freelance card's natural wrap; its comment's sibling attribution inverted, the pin's VALUE and dual guard exactly right), while the savings view's two cards are BOTH natural wrap twins. The first mutation candidate (the grid's items-start) was thereby invalidated as the v80 sanity (it flips the v79 income pin — a cascade) and replaced with the viewport-scoped titleRow mutation.

**The v80 pin (+1 e2e = 283):** the savings goal-card's double-wrap heights + title-row geometry + border/bg census at 1280 (tests/e2e/items.spec.ts — the never-pinned axes: the savings view's CARD HEIGHTS [230, 230] [the DOUBLE-WRAP twins — both cards carry 4 badges wrapping their rows to 52px; the v58 pin holds w/pad/radius only], the titleRow's geometry [flex/8px/center/h 24/the 8×8 dot at 9999px in the savings blue — the v45 F1a pin's income lime-dot twin completed to the savings type], the card's border 1px solid rgb(229,231,227) + bg white [the v45 F1a income family's savings twin]) — GREEN on first run; the pin-sanity mutation (the titleRow's `lg:items-start` at item-card.tsx:120) verified to FAIL at exactly the titleRow.alignItems axis ("center" → "flex-start") — **cascade-free by construction** (the responsive variant inert at 390 — the v51/v54 family untouched; the v45 F1a pin asserts no alignItems; the row height content-governed — the full items.spec.ts run under the mutation: 36 green, only the v80 pin red) — then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines).

**The full chain re-run GREEN:** lint → typecheck → 108 unit → `npm run build` → 283 e2e (102 + 122 + 61 chunk executions = 283 unique tests in 24 files) → 35/35 smoke. The screenshots 10/16 BYTE-IDENTICAL + 6/16 DATE-class pixel-arbitrated (the eleventh consecutive disciplined set — the FRESH SEED's `isoDate()` offsets resolving against the re-clone's seeding day: a +1-day shift on the date texts [03-income / 04-expenses / 05-savings / 06-networth / 08-calculator / 16-item-details — all confined to the date-bearing text bands], the chrome byte-identical, every diff crop VLM-arbitrated DATE-TEXT-ONLY via scripts/parity-probes/vlm-arbit-v80.mjs).

**The docs alignment:** D1 AGENTS.md (the v80 paragraph), D2 CLAUDE.md (283 + the v80 pin clause), D3 README.md (the counts + the v80 plan-table row), D4 zero-balance_SKILL.md (Session 115 audit row + the state lines), D5 the PAD's v1.1.37 revision block, D6 the probe README's v80 section, D7 session_190.md + this entry.

**The probe lessons:** (1) THE VIEWPORT-SCOPED CASCADE-FREE MUTATION — a per-view completion pin whose every axis is sibling-pinned (the shared-component reality) gets its cascade-free sanity via a responsive variant (lg:items-start flips the 1280 axis while the 390 family stays green — the mutation scoped by viewport, not by component); (2) THE STRETCH-TWIN ATTRIBUTION CORRECTION — the v70b "shorter sibling stretched" mechanism holds, but WHICH sibling is stretched is a per-view fact: probe it (the items-start experiment) before writing the attribution into a pin's comment; (3) THE FRESH-SEED DATE SHIFT — a re-clone's db:seed shifts every isoDate() field by the seeding-day delta: expect DATE-class screenshot diffs after any workspace reset and pixel-arbitrate them (crop pairs, DATE-TEXT-ONLY verdicts), never a full-page VLM verdict.

---

## Session 114 — Parity iteration v79: the re-run cycle's next-oldest candidate (the v57-era items pair's third re-run) + the axe watch (NO DRIFT) + the rail-avatar chrome + item-card amount-accent + wrap/stretch card-height pin (PIN-ONLY) (2026-10-17)

**Goal:** the v79 queue — the ledger-verified target (the v78 plan's suggestion agreeing with the rotation ledger: the v57-era items pair [the income + expenses view pair at desktop 1280, last re-shot v70] is the oldest remaining candidate [v70 < v74 < v75 < v76 < v77 < v78]; the pair's THIRD re-run, the cadence's most-re-verified desktop surface), plus the axe-core watch at its re-check point and the 73rd standing checks. **PIN-ONLY for src/ — no production-code change; +1 e2e = 282.** The formal narrative: `docs/session_188.md`; the plan: `docs/remediation-plan-v79.md`.

**The environment preserved** (no reset this session): the workspace survived the boundary intact — `main @ 387efae` (v78 shipped + the session_187 transcript via git pull), node_modules + `.env` (DATABASE_URL="file:../db/custom.db", db/ at the repo root) + `db/custom.db` + chromium-1243 all verified, no orphaned servers, the seedcheck confirming the exact seed (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran.

**The baseline chain FULLY GREEN as-shipped** (no F0 finding — the v76 lesson applied by construction: `npm run build`, the standalone static + public copies verified): lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap) · 281 e2e ✓ (100 + 106 + 77 chunks = 281 unique tests in 24 files — the exact documented v78 state) · 35/35 smoke ✓.

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next prereleases; no 5.x exists), the lockfile holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core 4.14.0, no nested engine dir), the engine-contract pin GREEN standalone (2 passed).

**The 73rd standing checks ALL GREEN:** the mobile menu VERIFIED WORKING (the 73rd consecutive time — `hitIsBurgerChild:true`, the sheet opens + closes on nav, the nav landmark present); the reference's four bugs ALL live [toast-blocker, sheet-trap `overlayCount:1`, no-landmark, the 464px /networth overflow]; the data census UNCHANGED (the 73rd clean drift check — the income leg re-read after a mid-script session expiry, the documented login-retry pattern); the SEO pair live; zero overflow at 390 on all five clone views.

**The re-run pair (BOTH items views at desktop 1280x800 full-page):** the income verdict DIFFERENT with every flag a documented class (the avatar letter the user-identity class; the 1-card vs 2-card grid the seed-count class; the figures the seed-data class); the expenses verdict DIFFERENT with every flag a documented class (the footer's payment-method chips the v57 DATA-CONDITIONAL class; the badge arrangement the v57 Recurring superset wrap class; the avatar the user-identity class — matching the v70 re-run's own flag set exactly). The both-sides census (arbit-v79.sh — the v75 convention, the v70 census axes re-measured on BOTH views): the AVATAR chrome BYTE-IDENTICAL (w 36 × h 36 / radius 9999px / fs 14px / fw 600 / color rgb(255,255,255) / bg rgb(143,188,63) — the identity text the only delta); the GRID + CARD chrome BYTE-IDENTICAL (grid 960 / gap 16px / the 3-col 309.328px template; card 309 / pad 20px / radius 12px / border rgb(229,231,227) — the card h ref-200 vs clone-230 the v70b-decomposed class: the Recurring superset badge's wrap h 52 [22+8+22] → +30px + the 1-row sibling stretch); the TITLE ROW + AMOUNT leaf chrome BYTE-IDENTICAL (the amount 24px/700/lh 32px/h 32 with the income lime rgb(143,188,63) + expenses orange rgb(224,122,59) accents matching per type); the FOOTER + BADGE chrome BYTE-IDENTICAL (the footer childCount the v57 DATA-CONDITIONAL class; the badgeRow h 22 vs 52 the v57 wrap class); the FILTER CARD BYTE-IDENTICAL on BOTH variants (the income 447-spanning + the expenses 216-not-spanning — the v64/v70 pins' own values, zero drift) + the header + the docSW 1280 guard. **NO NEW GAP.**

**The v79 pin (+1 e2e = 282):** the rail-avatar chrome + the item-card amount-accent + wrap/stretch card-height census at 1280 (tests/e2e/items.spec.ts — the never-pinned axes: the avatar's full chrome w 36/h 36/radius 9999px/fs 14px/fw 600/color white/bg rgb(143,188,63) [the tokens.spec pin holds the radius only]; the amount leaf's per-type accent family 24px/700/lh 32px/h 32 [the income lime + expenses orange accents — the v74 pin's savings twin completed to all three types]; the income view's first-card HEIGHT 230 [the v70b lesson's wrap/stretch arithmetic regression guard: the Salary sibling's Recurring-wrap natural 230 + the 1-row grid stretching the Freelance card]) — GREEN on first run; the pin-sanity mutation (the avatar's `font-semibold` → `font-medium` at sidebar.tsx:120) verified to FAIL at exactly the avatar.fw axis (600 → 500) — cascade-free (the tokens.spec radius pin + the boot-failure shell pin verified GREEN under the mutation) — then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines).

**The full chain re-run GREEN:** lint → typecheck → 108 unit → `npm run build` → 282 e2e (100 + 107 + 77 chunks = 282 unique tests in 24 files) → 35/35 smoke. The screenshots 16/16 BYTE-IDENTICAL — the tenth consecutive fully-identical set (the same-day regeneration, no calendar rollover).

**The docs alignment:** D1 AGENTS.md (the v79 paragraph), D2 CLAUDE.md (282 + the v79 pin clause), D3 README.md (the counts + the v79 plan-table row), D4 zero-balance_SKILL.md (Session 114 audit row + the state lines), D5 the PAD's v1.1.36 revision block, D6 the probe README's v79 section, D7 session_188.md + this entry.

**The probe lessons:** (1) THE MID-SCRIPT EXPIRY TWIN — the reference session expired between the F2 R-bug checks and the data census (the income leg read "no match" — the /income redirect had landed on /login); the re-read after a fresh login-retry recovered the exact documented values: treat a "no match"/empty census as a possible EXPIRY first (re-login + re-read) before suspecting drift; (2) THE v70b CARD-HEIGHT LESSON NOW HAS ITS REGRESSION GUARD — the income view's first-card HEIGHT 230 is pinned at 1280, so the wrap/stretch arithmetic (the Recurring superset badge's 52px wrap + the 1-row grid stretching the shorter sibling) can no longer silently regress.

---

## Session 113 — Parity iteration v78: the re-run cycle's next-oldest candidate (the mobile 390 twins' second re-run) + the axe watch (NO DRIFT) + the breakdown card's mobile svg family + chart-absence + width census pin (PIN-ONLY) (2026-10-17)

**Goal:** the v78 queue — the ledger-verified target (the v77 plan's suggestion agreeing with the rotation ledger this time: the mobile 390 twins [the networth + dashboard full-page pair, last re-shot v69] are the oldest remaining candidate [v69 < v70 items < v74-v77]; the v77 target-selection lesson applied — the queue suggestion verified against the ledger before commitment, no correction needed), plus the axe-core watch at its re-check point and the 72nd standing checks. **PIN-ONLY for src/ — no production-code change; +1 e2e = 281.** The formal narrative: `docs/session_186.md`; the plan: `docs/remediation-plan-v78.md`.

**The environment preserved** (no reset this session): the workspace survived the boundary intact — `main @ 67e988b` (v77 shipped + the session_185 transcript via git pull), node_modules + `.env` (DATABASE_URL="file:../db/custom.db", db/ at the repo root) + `db/custom.db` + chromium-1243 all verified, no orphaned servers, the seedcheck confirming the exact seed (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran.

**The baseline chain FULLY GREEN as-shipped** (no F0 finding — the v76 lesson applied by construction: `npm run build`, the standalone static + public copies verified): lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap) · 280 e2e ✓ (99 + 102 + 81 chunks = 279 chromium + 3 setups — the exact documented v77 state) · 35/35 smoke ✓.

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next prereleases; no 5.x exists), the lockfile holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core 4.14.0, no nested engine dir), the engine-contract pin GREEN standalone (2 passed).

**The 72nd standing checks ALL GREEN:** the mobile menu VERIFIED WORKING (the 72nd consecutive time — `hitIsBurgerChild:true`, the sheet opens + closes on nav, the nav landmark present); the reference's four bugs ALL live [toast-blocker, sheet-trap `overlayCount:1`, no-landmark, the 464px /networth overflow]; the data census UNCHANGED (the 72nd clean drift check); the SEO pair live; zero overflow at 390 on all five clone views.

**The re-run pair (BOTH mobile 390x844 full-page twins):** the networth verdict DIFFERENT with every flag a documented class (the stat tiles side-by-side vs stacked the v41 mobile-superset class; the asset groups the seed-data class; the Base44 overlay the platform chrome; the avatar the user-identity class — matching the v69 re-run's own flag set exactly); the dashboard verdict DIFFERENT with every flag a documented class (the subtitle wrap point the v62 width-delta class — the reference's own 395px docSW overflow shifts its wrap by one word, the chrome byte-identical; the progress-bar length the pct data class; the black tooltip the Base44 platform chrome; the donut proportions the seed-data class). The both-sides census (arbit-v78.sh — the v75 convention, the v69 census axes re-measured): the networth medallion 64×64 + trend icon 32×32 + tiles h 84 + grid gap 16px BYTE-IDENTICAL (the deltas all the v41 mobile-superset class — the reference's card 432/docSW 464/fixed 2-col tiles 176×84/medallion clipping at right 416 vs the clone's card 358/docSW 390/1-col tiles 294×84/medallion fitting at right 342 — zero drift since the v69/v63 censuses); the dashboard subtitle chrome BYTE-IDENTICAL + the breakdown card's height + svg families BYTE-IDENTICAL (h 324, svgCount 7, the first-four svgs [16×16, 14×14, 16×16, 14×14], rechartsWrappers 0, pieSectors 0 on BOTH sides — no donut in the breakdown card anywhere, the v69 disproof class) + the 5px width family delta (card 363 vs 358, H3 313 vs 308, DIV 313×238 vs 308×238) the reference's own docSW-395 overflow class (the heights byte-identical). **NO NEW GAP.**

**The v78 pin (+1 e2e = 281):** the Net Zero Breakdown card's mobile svg family + chart-absence + width census at 390 (tests/e2e/dashboard.spec.ts — the never-pinned axes: the card's w 358 [the v44 F2a pin covers the heights only], the svg family svgCount 7 with the full size census [16,14,16,14,16,14,16] [the three section icons + the three collapsed chevrons + the net-balance icon — never pinned at any viewport], the chart-absence contract rechartsWrappers 0 + pieSectors 0 [the v69 donut-invention lesson's regression guard], the children's width family H3 308×20 + DIV 308×238) — GREEN on first run; the pin-sanity mutation (the collapsed section chevron's `h-3.5 w-3.5` → `h-4 w-4` at dashboard-view.tsx:339) verified to FAIL at exactly the three chevron axes (14 → 16, the section row h 48 governed by the 32px chip — the v44/v76 pins untouched), then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines).

**The full chain re-run GREEN:** lint → typecheck → 108 unit → `npm run build` → 281 e2e (99 + 102 + 81 chunks = 280 chromium + 3 setups; one transient head-parity flake re-verified GREEN in-chunk) → 35/35 smoke. The screenshots 16/16 BYTE-IDENTICAL — the ninth consecutive fully-identical set (the same-day regeneration, no calendar rollover).

**The docs alignment:** D1 AGENTS.md (the v78 paragraph), D2 CLAUDE.md (281 + the v78 pin clause), D3 README.md (the counts + the v78 plan-table row), D4 zero-balance_SKILL.md (Session 113 audit row + the state lines), D5 the PAD's v1.1.35 revision block, D6 the probe README's v78 section, D7 session_186.md + this entry.

**The probe lessons:** (1) THE LEDGER-VERIFIED QUEUE — when the queue suggestion and the rotation ledger agree, say so explicitly in the plan (the v77 target-selection lesson's positive case: the verification step ran the same way, the outcome was agreement; the discipline is the check, not the correction); (2) THE v69 CHART-PRESENCE LESSON NOW HAS ITS REGRESSION GUARD — the breakdown card's rechartsWrappers/pieSectors counts are pinned at 390, so the VLM's invented-donut class can no longer resurface un-arbitrated (the pin fails if a chart ever appears in the breakdown card).

---

## Session 111 — Parity iteration v77: the re-run cycle's next-oldest candidate (the v61-era dashboard pair's second re-run) + the axe watch (NO DRIFT) + the Budget Guidelines interior-text family + quick-action icon viewBox pin (PIN-ONLY) (2026-10-17)

**Goal:** the session-183 v77 queue — corrected by the rotation ledger (the v76 plan's suggestion named the mobile 390 twins [last re-shot v69], but the cadence's own oldest-first rule points at the v61-era pair [last re-shot v68] — the mobile twins become the v78 candidate), plus the axe-core watch at its re-check point and the 71st standing checks. **PIN-ONLY for src/ — no production-code change; +1 e2e = 280.** The formal narrative: `docs/session_184.md`; the plan: `docs/remediation-plan-v77.md`.

**The environment preserved** (no reset this session): the workspace survived the boundary intact — `main @ 9d694b3` (v76 shipped + the session_183 transcript), node_modules + `.env` (DATABASE_URL="file:../db/custom.db", db/ at the repo root) + `db/custom.db` + chromium-1243 all verified, no orphaned servers, the seedcheck confirming the exact seed before any flow ran.

**The baseline chain FULLY GREEN as-shipped** (no F0 finding — the v76 lesson applied by construction: `npm run build`, the standalone static + public copies verified): lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap) · 279 e2e ✓ (98 + 64 + 119 chunks = 278 chromium + 3 setups — the exact documented v76 state) · 35/35 smoke ✓.

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next prereleases; no 5.x exists), the lockfile holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core 4.14.0, no nested engine dir), the engine-contract pin GREEN standalone (2 passed).

**The 71st standing checks ALL GREEN:** the mobile menu VERIFIED WORKING (the 71st consecutive time — `hitIsBurgerChild:true`, the sheet opens + closes on nav, the nav landmark present); the reference's four bugs ALL live [toast-blocker, sheet-trap `overlayCount:1`, no-landmark, the 464px /networth overflow]; the data census UNCHANGED (the 71st clean drift check); the SEO pair live; zero overflow at 390 on all five clone views.

**The re-run pair (the dashboard FULL-PAGE at desktop 1280x800 — the Budget Guidelines card + the quick-action row below the fold):** the VLM verdict **IDENTICAL, ZERO style flags** — the LAYOUT/STYLE section explicitly empty; every reported delta a documented data/identity class (the seed figures, the v56 root-URL active-nav, the avatar letter) — matching the v68 re-run's own IDENTICAL verdict. The both-sides census (arbit-v77.sh — the v75 convention, the v61 qa-census axes re-measured): the guidelines card **byte-identical on every axis with ZERO drift since v61** (the card 468×348 — the STRETCH-fix natural height holding 16 iterations later; the header 24px/16px/600/forestDark/lh 16px/tracking −0.4px; the body 0px 24px 24px; the three tiles 418×78 with the tint+border pairs + label 16/500/type + pct 14/400/type + desc 12/gray/lh 16px — the shadow's transparent lead layers the v66 computed-form class); the quick-action row byte-identical on every axis (the grid 960/3×304/gap 24; the cards 304×90/16px/24px; the tiles 40×40; the icons 20×20 + viewBox 0 0 24 24; the plus 16/0.5) — the label fw/color delta the v61 wrapper-vs-leaf lesson re-learned (the census's bare finder catching the clone's row WRAPPER span; the v61 F3 pin's LEAF finder measures the leaf byte-identical, GREEN in the baseline), the grid mt (ref 0px vs clone 32px) the margin-structure class with the rendered cross-row gap byte-identical (340, cardBottom 1122, gridTop 1462 BOTH sides). The seedcheck exact after. **NO NEW GAP.**

**The v77 pin (+1 e2e = 280):** the Budget Guidelines card's interior-TEXT family + the quick-action icons' viewBox census at 1280 (tests/e2e/dashboard.spec.ts — the never-pinned axes: the header's lh 16px + tracking −0.4px, the tiles 2/3 chrome, ALL three tiles' label/pct/desc TEXT chrome at 1280 [the v51 F4 family's desktop twin — the one-line-desc h-78 arithmetic], the quick-action icons' viewBox [the v76 glyph family's extension] — the arbitration's own measured values) — GREEN on first run; the pin-sanity mutation (the tile label's `font-medium` → `font-normal` at dashboard-view.tsx:848) verified to FAIL at exactly the three tiles' label.fw axes (fw 500→400), then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines).

**The full chain re-run GREEN:** lint → typecheck → 108 unit → `npm run build` → 280 e2e (99 + 64 + 119 chunks = 279 chromium + 3 setups) → 35/35 smoke. The screenshots 16/16 BYTE-IDENTICAL — the eighth consecutive fully-identical set (the same-day regeneration, no calendar rollover).

**The docs alignment:** D1 AGENTS.md (the v77 paragraph), D2 CLAUDE.md (280 + the v77 pin clause), D3 README.md (the counts + the v77 plan-table row), D4 zero-balance_SKILL.md (Session 112 audit row + the state lines), D5 the PAD's v1.1.34 revision block, D6 the probe README's v77 section, D7 session_184.md + this entry.

**The probe lessons:** (1) THE TARGET-SELECTION LESSON — verify a queue suggestion against the rotation ledger before executing it: the v76 plan's v77 queue named the mobile twins while the ledger's own oldest-first rule pointed at the v61-era pair (a queue suggestion is a hint, not a commitment; the ledger is the truth); (2) THE v61 WRAPPER-VS-LEAF LABEL LESSON re-confirmed live — the quick-action label's wrapper span still reads fw 400/rgb(10,10,10) under a bare textContent finder while the leaf measures byte-identical: keep pinning the LEAF.

---

---

## Session 110 — Parity iteration v76: the re-run cycle's next-oldest candidate (the v60-era networth + drill-down pair's second re-run) + the axe watch (NO DRIFT) + the breakdown section-icon chip glyph + donut label chrome pin (PIN-ONLY) (2026-10-17)

**Goal:** the session-181 v76 queue's first item — the re-run cadence rotating past the v75 login+calculator pair to the next-oldest candidate (the v60-era networth + drill-down pair, last re-shot v67 — the oldest remaining standing pair), plus the axe-core watch at its re-check point and the 70th standing checks. **PIN-ONLY for src/ — no production-code change; +1 e2e = 279.** The formal narrative: `docs/session_182.md`; the plan: `docs/remediation-plan-v76.md`.

**The environment preserved** (no reset this session): the workspace survived the boundary intact — `main @ 2f69d0e` (v75 shipped + the session_181 transcript), node_modules + `.env` (DATABASE_URL="file:../db/custom.db", db/ at the repo root) + `db/custom.db` + chromium-1243 all verified, no orphaned servers, the seedcheck confirming the exact seed before any flow ran.

**The baseline chain GREEN with THE F0 ENVIRONMENT LESSON** (no code defect): the first e2e pass hit a 20-test 5.9-minute wall with the boot-failure spec stuck at `aria-label="Loading"` — every `/_next/static/chunks/*` request 404ing. The root cause: a bare `npx next build` does NOT produce a servable standalone — package.json's `build` script's `cp -r .next/static .next/standalone/.next/` + `cp -r public .next/standalone/` steps are part of the build contract; without them the client never hydrates and every hydration-dependent assertion burns its 10s expect timeout (the "slow suite" was the 404 loop). After `npm run build`: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap) · 278 e2e ✓ (98 + 60 + 122 chunks = 277 chromium + 3 setups) · 35/35 smoke ✓ — the exact documented v75 state.

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next prereleases; no 5.x exists), the lockfile holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core 4.14.0, no nested engine dir), the engine-contract pin GREEN standalone (2 passed).

**The 70th standing checks ALL GREEN:** the mobile menu VERIFIED WORKING (the 70th consecutive time — `hitIsBurgerChild:true`, the sheet opens + closes on nav, the nav landmark present); the reference's four bugs ALL live [toast-blocker, sheet-trap `overlayCount:1`, no-landmark, the 464px /networth overflow]; the data census UNCHANGED (the 70th clean drift check); the SEO pair live; zero overflow at 390 on all five clone views.

**The re-run pair (the networth view + the dashboard drill-down EXPANDED at desktop 1280x800):** the networth pair DIFFERENT with two style flags, both documented classes (the Base44 FAB + the avatar letter — which the VLM misread as "P"; the census says "D"); the PART B census — the summary card's full HEIGHT family — **byte-identical on every axis with ZERO drift since the v67 pin** (the card 960×333/32px/16px/gradient/shadow; the headRow 76/mb 32; the label 14/80-white/mb 8/h 20; the figure 48/700/white/lh 48; the medallion 64×64/icon 32; the statGrid 440px×2/rows 84/gap 16; the statTile 440×84/pad 16/radius 12/white-10/blur(10)/label 12/amount 24/700; the ratioFooter mt 24/pt 24/1px/53) — the labelBlock width 304-vs-357 the figure-text-length data class. The drill-down pair DIFFERENT with six flags, every one DOM-arbitrated via arbit-v76.sh to a documented class: the nav highlight the v56 root-URL class (bg TRANSPARENT both sides — the delta the clone's white/500 vs the reference's zinc-600/400); the progress fill the pct × 568 data class (the track chrome byte-identical; fillW 173-vs-357); the donut labels the v60 perception class (the label chrome BYTE-IDENTICAL — count 4/16px/black/3 sectors/0 lines; the reference's first label element carries the three texts concatenated, the clone's distributed — a recharts label-grouping DOM artifact); the extra rows + footer + stat counts the seed-data classes; the tooltip the Base44 platform chrome. The stat trend icons + the hero trend glyph row byte-identical (the v67 axes — no drift). The seedcheck exact after. **NO NEW GAP.**

**The v76 pin (+1 e2e = 279):** the breakdown card's income-SECTION ICON CHIP glyph + the donut label chrome census at 1280 (tests/e2e/dashboard.spec.ts — the never-pinned axes: the section icon's 16×16 twin-polyline glyphSig/rgb(143,188,63)/viewBox 0 0 24 24 + its h-8 w-8 chip 32×32/radius 8px/rgba(143,188,63,0.125) + the donut label count 4/fs 16px/fill rgb(0,0,0)/sectors 3/labelLineCount 0; the precise section-button finder — the arbitration's own measured values) — GREEN on first run; the pin-sanity mutation (the section icon's h-4 w-4 → h-5 w-5 at dashboard-view.tsx:316) verified to FAIL at exactly the sectionIcons axis (the empty array at 20×20), then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines).

**The full chain re-run GREEN:** lint → typecheck → 108 unit → `npm run build` → 279 e2e (98 + 60 + 123 chunks = 278 chromium + 3 setups) → 35/35 smoke. The screenshots 16/16 BYTE-IDENTICAL — the seventh consecutive fully-identical set (the same-day regeneration, no calendar rollover since the v75 re-baseline).

**The docs alignment:** D1 AGENTS.md (the v76 paragraph), D2 CLAUDE.md (279 + the v76 pin clause), D3 README.md (the counts + the v76 plan-table row), D4 zero-balance_SKILL.md (Session 111 audit row + the state lines), D5 the PAD's v1.1.33 revision block, D6 the probe README's v76 section, D7 session_182.md + this entry.

**The probe lessons:** (1) THE F0 LESSON — `npm run build`, never a bare `npx next build`: the standalone static+public copy is part of the build contract, and a stuck-at-Loading page with a fast /api/health is the fingerprint of the missing static copy; (2) THE FINDER-DESCRIPTION LESSON — the v67/v76 arbitration's "stat-card footer trend icon" label was a MISNOMER (its width-200-500 "Total Income" finder matches the breakdown section row FIRST in the DOM on BOTH sites): name a census's finder by what it actually resolves to, and when a pin-sanity mutation FAILS TO FAIL, debug the finder before touching the pin.

---

## Session 109 — Parity iteration v75: the re-run cycle's next-oldest candidate (the v59-era login + calculator pair's second re-run) + the axe watch (NO DRIFT) + the login card's geometry + typography pin (PIN-ONLY) (2026-10-17)

**Goal:** the session-179 v75 queue's first item — the re-run cadence rotating past the v74 savings pair to the next-oldest candidate (the v59-era login + calculator pair, last re-shot v66), plus the axe-core watch at its re-check point and the 69th standing checks. **PIN-ONLY for src/ — no production-code change; +1 e2e = 278.** The formal narrative: `docs/session_180.md`; the plan: `docs/remediation-plan-v75.md`.

**The environment preserved** (no reset this session): the workspace survived the boundary intact — `main @ d6c278a` (v74 shipped + the session_179 transcript), node_modules + `.env` + `db/` + chromium-1243 all verified, the seedcheck confirming the exact seed before any flow ran.

**The baseline chain FULLY GREEN as-shipped** (no F0 finding): lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap) · 277 e2e ✓ (84 + 74 + 122 chunks = 276 chromium + 3 setups) · 35/35 smoke ✓.

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next prereleases; no 5.x exists), the lockfile holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core 4.14.0, no nested engine dir), the engine-contract pin GREEN standalone (2 passed).

**The 69th standing checks ALL GREEN:** the mobile menu VERIFIED WORKING (the 69th consecutive time — `hitIsBurgerChild:true`, the sheet opens + closes on nav, the nav landmark present); the reference's four bugs ALL live [toast-blocker, sheet-trap `overlayCount:1`, no-landmark, the 464px /networth overflow]; the data census UNCHANGED (the 69th clean drift check); the SEO pair live; zero overflow at 390 on all five clone views.

**The re-run pair (the login view + the calculator dialog at desktop 1280x800):** the login pair **VERDICT IDENTICAL, zero style flags** — the both-sides census byte-identical on every axis (the card 448/16px/rgba(255,255,255,0.95); the h1 30/700/lh 36/rgb(15,23,42); the subtitle 16/rgb(100,116,139); the logo 96×96; the inputs 48/12px/14px/1px rgb(226,232,240); the Sign in 368×48/12px/14px/500/rgb(15,23,42); the Google + OR blocks both; the card shadow's visible layer byte-identical — the lead-layer count the v66 computed-form class). The calculator pair DIFFERENT with three flags, every one DOM-arbitrated to a documented class: the "extra will-update line" the v66 DATA-CONDITIONAL class (ref false — its Rent natively $25.00 === its line-item total; clone true — opened-at $1850); the "row hover state" the v66 pointer-position class (actionsAtRest opacity 0/btnCount 2 on BOTH sides); the "amount alignment" the corollary (the amount chrome byte-identical 20/700/rgb(224,122,59)/h 28). The full census otherwise byte-identical (the panel 768×393/16px/white; the scrim rgba(26,58,46,0.5)/blur(8px); the title 18/700/lh 28; the desc 14/20 gray; the totalCard 720×90; the row 720×102; the pillRow/pill1; the addBtn 110×32; the docSW 1280). The clone twin's fixture FULLY restored (the delete + Rent's $1850 re-edit + the "$2235.00" page-total verify; the seedcheck exact after). **NO NEW GAP.**

**The v75 pin (+1 e2e = 278):** the login card's geometry + typography census at 1280 (tests/e2e/login-parity.spec.ts — the never-pinned axes of the VLM-identical surface: the card w 448/radius 16px/bg white-95; the h1's TYPOGRAPHY family 30px/700/lh 36px; the subtitle fs 16px; the input pair 48/12px/14px; the Sign in FULL chrome 368×48/12px/14px/500; the logo 96×96/alt; the docSW 1280 guard — the logged-out storageState opt-out, fixture-free) — GREEN on first run; the pin-sanity mutation (the h1's sm:text-3xl → sm:text-2xl) verified to FAIL at exactly the h1 axis (fs 30px→24px), then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines).

**The full chain re-run GREEN:** lint → typecheck → 108 unit → build → 278 e2e (84 + 74 + 122 chunks = 277 chromium + 3 setups) → 35/35 smoke. The screenshots 15/16 BYTE-IDENTICAL + 07-add-item-modal the documented dialog-default DATE class (the calendar rolled 2026-10-16 → 2026-10-17; pixel-arbitrated via pixel-diff-v75.py — the 16×22 px region at (1552,931)-(1568,953), the exact v66 bbox; the new shot re-baselined).

**The docs alignment:** D1 AGENTS.md (the v75 paragraph), D2 CLAUDE.md (278 + the v75 pin clause), D3 README.md (the counts + the v75 plan-table row), D4 zero-balance_SKILL.md (Session 110 audit row + the state lines), D5 the PAD's v1.1.32 revision block, D6 the probe README's v75 section, D7 session_180.md + this entry (the ledger's v74 omission repaired alongside v75's row).

**The probe lessons:** (1) the cold-session login census races its page load — the load-RETRIED census is the reliable pattern, never a single-shot "not found" verdict; (2) the login card's shadow arbitrates through the VISIBLE layer — the lead-layer count differs by engine, the rendered chrome does not; (3) the DATE-class screenshot diff recurs every calendar rollover — arbitrate programmatically (the PIL bbox), never with a VLM verdict.

---

## Session 108 — Parity iteration v74: the re-run cycle's OLDEST candidate (the v58-era savings pair's second re-run) + the axe watch (NO DRIFT) + the savings goal-card's interior-text chrome + the hidden app-shell h1 pin (PIN-ONLY) (2026-10-17)

**Goal:** the session-177 v74 queue's first item — the re-run cadence rotating to the OLDEST candidate after the NEW-pair program's v73 completion (the v58-era savings pair, last re-shot v65 — the only pre-v70 pair not re-run since), plus the axe-core watch at its re-check point and the 68th standing checks. **PIN-ONLY for src/ — no production-code change; +1 e2e = 277.** The formal narrative: `docs/session_178.md`; the plan: `docs/remediation-plan-v74.md`.

**The environment rebuilt** (the workspace was reset): fresh clone from `main @ f5e03c6`, `.env` + `db/` re-provisioned (the exact seed: 7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities), `npm ci`, the Playwright chromium re-installed (the reset left the old 1200 cache; the toolchain needs 1243).

**The baseline chain FULLY GREEN as-shipped** (no F0 finding): lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap) · 276 e2e ✓ (69 + 92 + 118 chunks = 275 chromium + 3 setups) · 35/35 smoke ✓.

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next prereleases; no 5.x exists), the lockfile holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core 4.14.0, no nested engine dir), the engine-contract pin GREEN standalone.

**The 68th standing checks** (ref-standing-v68.sh + standing-checks-v68.sh, version-bumped from v67): the mobile menu VERIFIED WORKING (the 68th consecutive time), the reference's four bugs ALL live (toast-blocker, sheet-trap, no-landmark, the 464px /networth overflow), the data census intact (the 68th clean drift check), the SEO pair live.

**The re-run pair — the savings view at desktop 1280 FULL-PAGE, NO NEW GAP** (vlm-shots-v74.sh + clone-vlmshots-v74.sh + vlm-compare-v74.mjs, login on the first attempt both sides, the parked pointer at (5,5), read-only): the VLM verdict DIFFERENT with two layout/style flags, every one DOM-arbitrated via arbit-v74.sh (the both-sides /savings census at 1280): (1) the "Card Grid Alignment" flag = the SEED-DATA class + BYTE-IDENTICAL grid chrome (display grid, the ≈309.33px 3-col template [the ref's `309.328px×3` vs the clone's `309.328px 309.328px 309.344px` — the last track's 0.016px sub-pixel distribution with 2 children vs 1], the gap 16px, the w 960 — the childCount 1-vs-2 is the reference's own 1-item seed vs the clone's 2-item dev seed); (2) the "Card Footer Content" flag = the v58 DATA-CONDITIONAL footer class re-verified live (the footer chrome byte-identical [flex justify-between/12px/rgb(107,114,128)/h 16]; the reference's item carries NO paymentMethod → ONE child, the clone's carry paymentMethods → the same two-child structure; every child's chrome byte-identical [flex gap 4px/12px/gray/12×12 gray icons]; a NEW micro-observation: the reference's footer children are DIVs, the clone's SPANs — the v72 structural-class family); the badge family (the classification VALUE the data class — the reference's "need" red vs the clone's "savings" green, the maps locked by badge-colors.spec.ts; the monthly + active badges byte-identical; the clone's 4th Recurring superset badge wraps the row to h 52 — the v57 arithmetic); the card + interior-text chrome byte-identical (309/20px/12px/1px rgb(229,231,227)/white; the h4 16/600/lh 24/rgb(26,58,46); the amount 24/700/lh 32/rgb(59,126,161); the card heights 200-vs-230 decomposing through the badge-wrap arithmetic); the hidden first-in-DOM h1 "ZeroBalance" (the app-shell mobile topbar's h1, inside the md:hidden header) computed chrome byte-identical both sides (20px/700/rgb(26,58,46)) — the v65-documented SEO surface measured live again.

**The v74 pin (+1 e2e = 277):** the savings goal-card's interior-text chrome + the hidden app-shell h1 census at 1280 (tests/e2e/items.spec.ts — the h4 title 16/600/lh 24/rgb(26,58,46) + the amount 24/700/lh 32/rgb(59,126,161) [the v51 pin's 390-only family now pinned at 1280 with the lh] + the hidden h1 "ZeroBalance" 20px/700/rgb(26,58,46) rendered ZERO-SIZE [w 0/h 0, its own display "block" — the md:hidden-header mechanism, the v65 note's "hidden zero-size", pinned for the first time] + the docSW 1280 guard; read-only, the seeded Investments card — the v58 pin's own style) — GREEN on first run; a PRE-PIN PROBE corrected the draft (the first draft asserted display "none"; the live h1probe returned display "block"/w 0/h 0 — an element inside a display:none subtree keeps its OWN display while rendering zero-size; the pin asserts w/h 0); the pin-sanity mutation (the amount's text-2xl → text-xl) verified to FAIL at exactly the cardAmount axis, then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines).

**The full chain re-run GREEN:** lint → typecheck → 108 unit → build → **277 e2e** (69 + 92 + 118 chunks = 276 chromium + 3 setups) → 35/35 smoke. The screenshots **16/16 BYTE-IDENTICAL** (the sixth consecutive fully-identical set; the seedcheck under `env -u DATABASE_URL` confirming the exact seed state).

**The probe lessons:** (a) the dollar-text census corollary — the amount's dollar-prefixed textContent is matched by the `text-2xl` CLASS, never by text (a literal `$` in a double-quoted bash census expands against bash's positional parameters — `$4` in a character class silently empties); (b) the md-hidden-subtree census — an element inside a display:none subtree keeps its OWN computed display ("block") while rendering zero-size boxes: assert w/h 0, never display "none"; (c) a pre-pin probe beats a wrong assertion — the live probe corrected the pin's draft BEFORE the RED/GREEN cycle (the mutation check only validates the axes you actually assert).

**The v75 queue (suggestions):** the re-run cadence rotates to the next-oldest candidate (the v59-era login pair, last re-shot v66 — or the v60-era networth pair, last re-shot v67), the axe-core watch at its next re-check point, and the deferred reference-write censuses (unchanged, blocked by the v46 read-only rule).

---

## Session 107 — Parity iteration v73: the NEW-pair program's LAST never-shot surfaces (the login + calculator mobile 390 twins) + the axe watch (NO DRIFT) + the calculator scrim + summary-text chrome pin (PIN-ONLY) (2026-10-17)

**Goal:** the session-173/174 v73 queue's items — the NEW-pair program's remaining never-shot surfaces (the login page's mobile 390 twin, the simplest pair; the calculator dialog's mobile 390 twin, the v66 desktop pair's mobile twin) and the axe-core watch at its re-check point — plus the 67th standing checks. **PIN-ONLY for src/ — no production-code change; +1 e2e = 276.** The formal narrative: `docs/session_175.md`; the plan: `docs/remediation-plan-v73.md`.

**The baseline chain FULLY GREEN as-shipped** (no F0 finding): lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · 275 e2e ✓ (100 + 83 + 94 chunks = 274 chromium + 3 setups) · 35/35 smoke ✓. (The fresh clone needed `npx playwright install chromium` — the sandbox reset wiped the browser cache; the suite itself untouched.)

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next prereleases; no 5.x exists), the lockfile holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core 4.14.0, no nested engine), the engine-contract pin GREEN (re-verified standalone).

**The 67th standing checks** (ref-standing-v67.sh + standing-checks-v67.sh, version-bumped from v66): the mobile menu VERIFIED WORKING (the 67th consecutive time), the reference's four bugs ALL live (toast-blocker, sheet-trap, no-landmark, the 464px /networth overflow), the data census intact (the 67th clean drift check), the SEO pair live.

**The NEW-pair program — the LAST never-shot surfaces, NO NEW GAP** (vlm-shots-v73.sh + clone-vlmshots-v73.sh + vlm-compare-v73.mjs, login on the first attempt both sides, the parked pointer at (5,5), the hover + Calculate clicks VIEW-STATE only; the clone's 1-row calculator state rides the v66 fixture discipline — Contents Insurance $25 added through the real UI, then FULLY restored: delete + Rent's $1850 re-edit + the "3 items · $2235.00" page-total verification + the seedcheck confirming the exact seed state): **PAIR 1 (the LOGIN page at mobile 390 — the fresh logged-out surface) — VERDICT IDENTICAL, zero flags** (the fresh-session census both sides: hasLoginCard true, docSW 390, title "ZeroBudget"). **PAIR 2 (the CALCULATOR dialog at mobile 390 — the v66 desktop pair's mobile twin)** — the "scrim lighter" claim a PERCEPTION ARTIFACT (the scrim chrome BYTE-IDENTICAL: bg rgba(26,58,46,0.5) / computed opacity 1 / blur(8px) / 390×844; the reference's wrapper-scrim carries the dialog's text, the clone's Radix scrim a textless sibling — the v72 structural class), the "Will update category total" span the v66 DATA-CONDITIONAL class re-verified live (the reference's Rent natively 25.00 === its line-item total 25.00 → hidden; the clone's opened-at 1850 vs the recalculated 25.00 → shown, 12px/400/rgb(234,88,12)). The full both-sides census via arbit-v73.sh — the panel x16/y216/w358/h413/maxW 768/maxH 717.4/radius 16/white + the header 101/"16px 24px"/border-b + the close 29×36/radius 6/transparent + the title 18/700/lh 28 + the desc 14/lh 20 gray + the Total Calculated block #fff7f5/#fcddd5/radius 12/pad 16/310×90/mb 24 + the amount 24/700/lh 32 rgb(224,122,59) + the row 102/310/pad 16 + the Add Item 110×32 — BYTE-IDENTICAL on every axis. **With these two pairs the NEW-pair program is COMPLETE — every view + dialog + sheet surface now carries BOTH a desktop pair and a mobile-390 twin.**

**The v73 pin (+1 e2e = 276):** the calculator's scrim + summary-text chrome census at 390 (tests/e2e/calculator.spec.ts — the scrim bg/opacity/blur/geometry [the details-sheet overlay was pinned, the calculator's own scrim never was], the summary amount 24/700/lh 32, the "Based on 1 item" line 12px gray, the description 14/20 gray, the "Will update category total" span 12/400 rgb(234,88,12) with the 1-row fixture — the arbitration's own measured values; the fixture rides the v53 discipline: hover → Calculate → Add Line Item → census → Delete → restoreRent) — GREEN on first run; the pin-sanity mutation (the scrim blur 8px→4px in `.zb-modal-overlay`) verified to FAIL at exactly the scrim axis, then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines).

**The full chain re-run GREEN:** lint → typecheck → 108 unit → build → **276 e2e** (100 + 84 + 94 chunks = 275 chromium + 3 setups) → 35/35 smoke. The screenshots **16/16 BYTE-IDENTICAL** (the fifth consecutive fully-identical set; the seedcheck under `env -u DATABASE_URL` confirming the exact seed state).

**The probe lessons:** (a) the mobile fold — at 390 the Rent card sits BELOW the fold in the 1-col grid (card center y > 844); a raw out-of-viewport mouse move never engages `:hover` (the Calculate button stays hidden, the click misses — the probe's first pass failed exactly there): `scrollIntoView({block:'center'})` BEFORE the hover is required; (b) the unquoted-heredoc dollar trap — a `<<EOF` heredoc expands `\$1850` into `$1850` and the inner `bash -s` reads `$1` (a positional parameter) → `set -u` kills the script; the QUOTED `<<'EOF'` heredoc with the env-injected census (`CALC_CENSUS_JS="$CALC_CENSUS_JS" bash ... bash -s <<'EOF'`) is the fix; (c) a scrim "transparency" claim arbitrates through the computed style (bg + opacity + backdrop-filter are three separate axes), never the screenshot read.

**The v74 queue (suggestions):** the NEW-pair program complete — the cadence rotates to the re-run cycle's OLDEST candidate (the v58-era savings pair, last re-shot v65 — the only pre-v70 pair not re-run since), the axe-core watch at its next re-check point, and the deferred reference-write censuses (unchanged, blocked by the v46 read-only rule).

---

## Session 106 — Parity iteration v72: the NEW-pair program continues (the details-sheet mobile 390 twins + the drill-down EXPANDED mobile twin) + the axe watch (NO DRIFT) + the details-sheet EMPTY-subtitle pin (PIN-ONLY) (2026-10-17)

**Goal:** the session-171 v72 queue's items — the NEW-pair program's remaining below-the-fold 390 surfaces (the details-sheet mobile twin, the drill-down EXPANDED mobile twin), the axe-core watch at its re-check point, and the deferred reference-write censuses (unchanged) — plus the 66th standing checks. **PIN-ONLY for src/ — no production-code change; +1 e2e = 275.** The formal narrative: `docs/session_173.md`; the plan: `docs/remediation-plan-v72.md`.

**The baseline chain FULLY GREEN as-shipped** (no F0 finding): lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · 274 e2e ✓ (93 + 91 + 92 chunks = 273 chromium + 3 setups) · 35/35 smoke ✓.

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next prereleases; no 5.x exists), the lockfile holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core 4.14.0, no nested engine), the engine-contract pin GREEN (re-verified standalone).

**The 66th standing checks** (ref-standing-v66.sh + standing-checks-v66.sh, version-bumped from v65): the mobile menu VERIFIED WORKING (the 66th consecutive time), the reference's four bugs ALL live (toast-blocker, sheet-trap, no-landmark, the 464px /networth overflow), the data census intact (the 66th clean drift check), the SEO pair live.

**The NEW-pair program — NO NEW GAP** (vlm-shots-v72.sh + clone-vlmshots-v72.sh + vlm-compare-v72.mjs, login on the first attempt both sides, the parked pointer at (5,5), the card-open and drill-expand clicks VIEW-STATE only): PAIR 1 (the WITH-subtitle details sheet — the Rent card, "Apartment" both sides) — the close-button "border" claim a PERCEPTION ARTIFACT (the chrome byte-identical: 36x36/radius 6px/border 0px/transparent/no shadow/no outline/16px #0a0a0a X; the clone's "Close" text sr-only), the amount/Recurring values DATA classes, the Payment-Method row the v52 optional-field DATA-CONDITIONAL class, the Base44 FAB platform chrome. PAIR 2 (the EMPTY-subcategory details sheet — the reference's Miscellaneous vs the clone's user-created fixture, the v71 F4 discipline) — the "reference cropped below Status" claim a PERCEPTION ARTIFACT (the sheet geometry byte-identical — surface 390x717@bottom 844, maxH 717.4px, the scrim rgba(26,58,46,0.5)+blur(8px); BOTH sides carry the Created/Last Updated meta rows, the reference's behind its own platform FAB), and **THE HEADLINE: the no-sub sheets BOTH render NO subtitle P — the v52 sheet conditional's EMPTY side verified LIVE against the reference's own empty-side sheet (the v71 card-side fix's sibling surface; the v52 assumption "every reference item carries a subcategory" disproven by v71 — the empty side now measured on the reference itself)**. PAIR 3 (the drill-down EXPANDED at 390 — the v67 desktop pair's mobile twin) — the row inventory the seed-data class (the reference's 1 income item vs the clone's 2; the category chrome byte-identical h 28/pad "6px 12px"/fs 16px/400/radius 8px; the item-row label "Item" vs "Net monthly salary" the NOTES-VALUE data class — the reference's own v60-dumped literal "Item" for notes-less items), the pie/legend/summary values DATA classes, the 5px row-width delta the reference's own docSW-395 overflow class, the Base44 toast platform chrome. Every flag DOM-arbitrated via arbit-v72.sh (the sheet + drill-down census at 390 on BOTH sides).

**The v72 pin (+1 e2e = 275):** the details sheet's EMPTY-subtitle side census at 390 — an Add-Expense no-subcategory fixture's sheet renders NO subtitle P (the H3→amount adjacency holds, the 24/700/mb-8 H3 + the 36/700/mt-16 amount chrome, the panel w 390 — the arbitration's own measured values, byte-identical on both sides' no-sub sheets); the fixture create/cleanup rides the v71 F4 discipline (the Edit-dialog Delete path, the header count restored). GREEN on first run (the v52 conditional correct in the code since v52 — the pin locks it); the pin-sanity mutation (the conditional reverted to the unconditional empty-P render) verified to FAIL at exactly subtitleCount, then restored (the standalone REBUILD as a SEPARATE command; git diff src/ = 0 lines).

**The full chain re-run GREEN:** lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ · **275 e2e** ✓ (93 + 91 + 93 chunks = 274 chromium + 3 setups) · 35/35 smoke ✓. The screenshots **16/16 BYTE-IDENTICAL** (the fourth consecutive fully-identical set — the same DB, no re-seed, the stored dates stable; the seedcheck under `env -u DATABASE_URL` confirming the exact seed state).

**The probe lessons** (the reference's details sheet carries NO role=dialog — the custom fixed-overlay detection via the z>=50 text-prefixed overlay, the clone's Radix sheet also matching; the reference's card-open is the CARD ROOT click, an h4-only click did not open it; the clone's Edit-dialog cleanup must read the Category INPUT VALUE, never textContent — the first pass stranded the fixture and cleanup-fixture-v72.sh recovered it; the reference's scrim wraps the panel while the clone's Radix scrim is a sibling — the rendered geometry the contract, both x 0/y 127/w 390/h 717/bottom 844).

## Session 105 — Parity iteration v71: the NEW-pair program opens (the items views' mobile 390 full-page pairs — income + expenses + savings) + the axe watch (NO DRIFT) + the item-card SUBTITLE-P conditional-render fix (2026-10-17)

**Goal:** the session-170/171 v71 queue's items — the NEW-pair program (the below-the-fold 390 surfaces, the items views' mobile twins never individually shot, the v62/v63 precedent), the axe-core watch at its re-check point, and the deferred reference-write censuses (unchanged) — plus the 65th standing checks. **THE FIX iteration — the first production-code change since v61** (the pin-only line broken): the item-card subtitle-P conditional render. The formal narrative: `docs/session_171.md`; the plan: `docs/remediation-plan-v71.md`. (The prior session's identical iteration — executed through the fix's GREEN — was lost to a workspace reset before its commit; re-executed end-to-end from the freshly re-cloned v70 tree.)

**The baseline chain FULLY GREEN as-shipped** (no F0 finding): lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · 272 e2e ✓ (96 + 72 + 108 chunks = 271 chromium + 3 setups) · 35/35 smoke ✓.

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next prereleases; no 5.x exists), the lockfile holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core 4.14.0), the engine-contract pin green in the baseline.

**The 65th standing checks** (ref-standing-v65.sh + standing-checks-v65.sh, version-bumped from v64): the mobile menu VERIFIED WORKING (the 65th consecutive time), the reference's four bugs ALL live (toast-blocker, sheet-trap, no-landmark, the 464px /networth overflow), the data census intact (the 65th clean drift check), the SEO pair live.

**The NEW-pair program — ONE REAL GAP FOUND** (vlm-shots-v71.sh + clone-vlmshots-v71.sh + vlm-compare-v71.mjs, login on the first attempt both sides, the parked pointer at (5,5)): PAIR 1 (income) — VERDICT IDENTICAL, zero layout/style flags. PAIR 2 (expenses) — the footer (the v57 DATA-CONDITIONAL class: the chrome byte-identical, the reference's expense items carrying no paymentMethod values), the badge wrapping (the v57 wrap class: the chrome byte-identical, the clone's 4th Recurring superset badge wrapping the row to h 52), the Base44 FAB (platform chrome). PAIR 3 (savings) — the footer + badge flags the same classes, the badge styling (the v58 classification-VALUE data class: the color maps byte-identical per classification — the reference's own Investments card carries the "savings" badge with exactly the clone's values), the "active badge padding" claim (a PERCEPTION ARTIFACT — the active badge byte-identical on every card both sides: h 22/w 63/pad "2px 10px"/radius 6px/bg rgb(248,250,252)/color rgb(51,65,85)). **THE DISCOVERY:** the reference's Miscellaneous/Investments expense cards (empty subcategory) render NO subtitle P (titleRow 28, card 180 — the arithmetic 20+28+12+32+16+22+12+16+20+2) while its with-subcategory cards render it (h 20, fs 14px, lh 20px, gray; titleRow 48) — **the reference CONDITIONALLY RENDERS the subtitle P**; the clone's item-card.tsx:127 rendered `{item.subcategory ?? ""}` unconditionally (a 20px empty block on user-created empty-subcategory items — the dev seed carries none, the gap hidden in the unshipped state space).

**THE v71 FIX (TDD):** the F4 regression test (an Add-Expense no-subcategory fixture renders NO subtitle P, titleRow 28, card h 180 at 390 in the 1-col grid; the cleanup via the Edit dialog's Delete path, the header count restored) RED on the unfixed build → the fix (the v52 details-sheet idiom: `{item.subcategory ? (<p>…</p>) : null}`) → GREEN; the F5 pin (the seeded Rent card's WITH-subtitle chrome: P h 20/fs 14px/lh 20px/color rgb(107,114,128), titleRow 48, titleRowMb 12) locks the populated state; the pin-sanity mutation (the reverted conditional) verified to FAIL at exactly subtitleCount, then restored. +2 e2e = **274**.

Full chain: lint + typecheck + 108 unit + build + 274 e2e (96 + 72 + 108 chunks) + 35/35 smoke green. **The screenshots: 16/16 BYTE-IDENTICAL** (the third consecutive fully-identical set — the same-day seed; the fix touches no seeded surface; the seedcheck run under `env -u DATABASE_URL`). The docs aligned (AGENTS/CLAUDE/README/SKILL Session 106 row + the 274 state/PAD v1.1.28/the probe README's v71 section/session_171/the repo worklog Session 105 + the ledger list). **Next** (the v72 queue): (1) the NEW-pair program continues (the remaining below-the-fold 390 surfaces: the drill-down EXPANDED mobile twin, the details-sheet mobile twin) or the re-run cadence's second cycle (the v58-era savings pair, last re-shot v65), (2) the axe watch at its next re-check point, (3) the deferred reference-write censuses (unchanged).

---

## Session 104 — Parity iteration v70: the OLDEST re-run candidate's fresh standing sweep (the v57-era items pair re-run — income + expenses at 1280) + the axe-core watch (NO DRIFT) + the expenses view's filter-card computed census pin (2026-10-16)

**Goal:** the session-167/168 v70 queue's items — the re-run cadence returning to the DESKTOP pairs (the OLDEST re-run candidate: the v57-era items pair, last re-shot by v64 itself — the cadence's first COMPLETED cycle, v64→v70; the NEW-pair program stays the v71+ candidate), the axe-core watch at its re-check point, and the deferred reference-write censuses (unchanged, blocked by the v46 read-only rule) — plus the 64th standing checks. **PIN-ONLY for src/** (the pin-only line continues; `git diff src/` = 0 lines at ship). The formal narrative: `docs/session_169.md`; the plan: `docs/remediation-plan-v70.md`.

**The baseline chain FULLY GREEN as-shipped** (no F0 finding — the v68 tail-phase lesson holding): lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · 271 e2e ✓ (93 + 94 + 86 chunks = 270 chromium + 3 setups) · 35/35 smoke ✓.

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next prereleases; no 5.x exists), the lockfile holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core 4.14.0), the engine-contract pin green (re-verified standalone).

**The 64th standing checks** (ref-standing-v64.sh + standing-checks-v64.sh, version-bumped from v63): the mobile menu VERIFIED WORKING (the 64th consecutive time), the reference's four bugs ALL live (toast-blocker, sheet-trap, no-landmark, the 464px /networth overflow), the data census intact (the 64th clean drift check), the SEO pair live.

**Both items pairs CLEAN** (vlm-shots-v70.sh + clone-vlmshots-v70.sh + vlm-compare-v70.mjs, login on the first attempt both sides, the parked pointer at (5,5)): PAIR 1 (income) — the avatar (the user-identity class: the chrome BYTE-IDENTICAL 36×36/radius 9999px/14px-600/white/bg rgb(143,188,63), only "U" vs "D"; the fixed v65b finder re-used after the first pass caught the clone's brand block), the card grid (the seed-count class: the AXES byte-identical — w 960/gap 16px/the same fractional 309.344px last track class as v64), and the card heights (ref 200 vs clone 230) DECOMPOSED arithmetic-wise via arbit-v70b.sh's card-internals census — the clone's Salary card carries the 4th Recurring superset badge → the wrap h 52 (22+8+22) → +30px, AND the sibling Freelance card (natural 200) STRETCHES to 230 with it = the v57 badge-wrap class + the grid STRETCH-GOVERNED class (the v67 lesson); PAIR 2 (expenses) — the footer (the v57 DATA-CONDITIONAL class: the chrome byte-identical, the reference's expense items carrying no paymentMethod values), the badge arrangement (the v57 wrap class re-confirmed live: 4 badges → h 52 vs 3 → h 22), the avatar (user-identity, again).

**The v70 pin (+1 → 272):** the EXPENSES view's filter-card computed census at 1280 (tests/e2e/items.spec.ts, a new describe at the file tail, the logged-in read-only state, measured BYTE-IDENTICAL on both sides via arbit-v70.sh) — the LAST never-census'd filter-card variant (the v38 S2 pin covered /savings, the v64 pin /income, the v52 F3 pin the expenses card's MOBILE 390 state only): the card 960×86 (pad 24/radius 16/white/border rgb(229,231,227)/mb 24), the search 216×36 — the 1-COL span, the expenses variant's defining difference (the search does NOT span 2 columns; the 215.5px track rounds to 216 via offsetWidth) with the asymmetric pad "4px 12px 4px 40px", the inner grid 4 tracks 215.5px/16px gap/4 children, the three comboboxes 216×36 at 14px ("All Categories"/"All Frequencies"/"All Payment Methods"). GREEN on first run; THREE pin-sanity mutations verified to FAIL then restored (the expense-branch grid gap-4→gap-2 [the expense branch only, the v64 income pin untouched]; the card p-6→p-4 [the shared-class regression]; the search pl-10→pl-4 — each with the standalone REBUILD as a SEPARATE command).

Full chain: lint + typecheck + 108 unit + build + 272 e2e (93 + 95 + 86 chunks) + 35/35 smoke green. **The screenshots: 16/16 BYTE-IDENTICAL** (the second consecutive fully-identical set — the same-day seed; the seedcheck run under `env -u DATABASE_URL`). The docs aligned (AGENTS/CLAUDE/README/SKILL Session 105 row + the 272 state/PAD v1.1.27/the probe README's v70 section/session_169/the repo worklog Session 104 + the ledger list). **Next** (the v71 queue): (1) the NEW-pair program opens (the below-the-fold 390 surfaces — the items views' mobile twins never individually shot, the v62/v63 precedent) or the re-run cadence's second cycle (the v58-era savings pair, last re-shot v65), (2) the axe watch at its next re-check point, (3) the deferred reference-write censuses (unchanged).

---

## Session 103 — Parity iteration v69: the mobile 390 pair re-run (BOTH twins — the networth full-page + the dashboard mobile twin) + the axe-core watch (NO DRIFT) + the networth page-header row computed census pin + the F0 lint-gate repair (2026-10-16)

**Goal:** the session-165/166 v69 queue's items — the re-run cadence rotating to the mobile 390 twins (the documented queue surface, the networth full-page twin, PLUS the dashboard mobile twin, the other never-re-run mobile pair — both in one two-pair iteration, the v62/v67 precedent), the axe-core watch at its re-check point, and the deferred reference-write censuses (unchanged, blocked by the v46 read-only rule) — plus the 63rd standing checks. **PIN-ONLY for src/** (the pin-only line continues; `git diff src/` = 0 lines at ship). The formal narrative: `docs/session_167.md`; the plan: `docs/remediation-plan-v69.md`.

**The F0 lint-gate repair (the audit's first finding, caught by the baseline chain itself):** the v68 changeset shipped `scripts/parity-probes/db-seedcheck-v68.cjs` — the repo's only `.cjs`, created during v68's screenshot phase AFTER its final lint run — and its CommonJS `require()` tripped `@typescript-eslint/no-require-imports`: the committed v68 tree did NOT pass `npm run lint`. The repair: a single-file eslint-disable directive (the file keeps its name + logic; the gate stays strict for the rest of scripts/). LESSON: the clean-check gate must re-run AFTER every new file lands — a file created in the screenshots phase (the chain's tail) escapes a chain run from the morning.

**The axe watch NO DRIFT:** npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next prereleases; no 5.x exists), the lockfile holding the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core 4.14.0), the engine-contract pin green in the baseline — the 4.x story stays closed.

**The 63rd standing checks** (ref-standing-v63.sh + standing-checks-v63.sh, version-bumped from v62): the mobile menu VERIFIED WORKING (the 63rd consecutive time), the reference's four bugs ALL live (toast-blocker, sheet-trap, no-landmark, the 464px /networth overflow), the data census intact (the 63rd clean drift check), the SEO pair live.

**Both mobile pairs CLEAN** (vlm-shots-v69.sh + clone-vlmshots-v69.sh + vlm-compare-v69.mjs, login on the first attempt both sides, the parked pointer at (5,5)): the networth 390 re-run's three flags ALL arbitrated via arbit-v69.sh to the v63-era classes re-confirmed live with the EXACT v63 numbers (the stat-tile stacking = the v41 mobile-superset class; the trend icon = the v54 clipping perception artifact [the medallion 64×64 + icon 32×32 byte-identical both sides, the ref clipping at 416, the clone fitting at 342]; the Base44 overlay = platform chrome); the dashboard 390 re-run's flags arbitrated (the Base44 tooltip = platform chrome; the subtitle wrap = the documented v62 class [the chrome byte-identical — the exact v62 pin values re-measured both sides; the ref's own docSW 395 overflow shifting its wrap point by one word]; and a NEW flag variant DOM-DISPROVEN — "the reference's breakdown card contains a donut": ZERO donut on EITHER side [rechartsWrappers 0, pieSectors 0 both; the card h 324 both sides — the v42 census value; the 7 svgs the byte-identical row icons] — a perception artifact, the DOM census the ground truth).

**The v69 pin (+1 → 271):** the networth view's PAGE-HEADER ROW computed census at 390 (tests/e2e/networth.spec.ts, a new describe at the file tail, the logged-in read-only state, measured live via nw-header-v69.sh) — the never-census'd family (the v14 chip test pins x-positions only; the v65 savings header-row pin's sibling): the row flex/center/gap-3 12px/mb-8 32px/w 358/h 60 (the TEXT BLOCK governs — the h1 36 + the subtitle 24 — not the 48px chip, the v65 lesson); the chip 48×48/rounded-xl 12px/forest→lime gradient + the 24×24 white icon; the h1 30px/700/lh 36px/forestDark/h 36/x 76; the block w 250/h 60 (the subtitle's max-content governs); the subtitle 16px/400/gray-500 ONE line; the row→card gap 32; docSW 390. GREEN on first run; THREE pin-sanity mutations verified to FAIL then restored (the row mb-8→mb-4; the chip h-12 w-12→h-10 w-10; the h1 text-3xl→text-2xl — each with the standalone REBUILD as a SEPARATE command).

Full chain: lint + typecheck + 108 unit + build + 271 e2e (97 + 99 + 77 chunks) + 35/35 smoke green. **The screenshots: 16/16 BYTE-IDENTICAL** (the first fully-identical set since v65 — the v68 re-seed and the v69 capture share the 2026-10-16 calendar day; the seedcheck run under `env -u DATABASE_URL`, the sandbox's inherited parent-workspace URL being the documented pollution). The docs aligned (AGENTS/CLAUDE/README/SKILL Session 104 row + the 271 state/PAD v1.1.26/the probe README's v69 section/session_167/the repo worklog Session 103 + the ledger list). **Next** (the v70 queue): (1) the mobile twins both re-run — the re-run cadence returns to the desktop pairs or a NEW-pair program (the below-the-fold 390 surfaces, the items views' mobile twins never individually shot), (2) the axe watch at its next re-check point (only a 5.x wrapper changes the calculus), (3) the deferred reference-write censuses (unchanged).

---

## Session 102 — Parity iteration v68: the DEDICATED axe-core wrapper upgrade (the deliberate 4.14.0 pin bump + the rule-coverage re-audit: the sets byte-identical) + the v61-era pair re-run (the dashboard full-page 1280) + the a11y gate's ENGINE-CONTRACT pin (2026-10-16)

**Goal:** the session-163/164 v68 queue's two items — the DEDICATED
axe-core wrapper upgrade (the v67 plan's own decision, executed
mechanically: never a drift, never a rider) and the re-run cadence
rotating to the v61-era pair (the dashboard full-page 1280 — the
quick-action row + the Budget Guidelines card) — plus the 62nd
standing checks. **TOOLCHAIN-ONLY** — no production-code change (the
pin-only line continues; the upgrade touches package.json +
package-lock.json, never src/). The formal narrative:
`docs/session_165.md`; the plan: `docs/remediation-plan-v68.md`.

**The upgrade chain, measured live:** the registry state (npm-latest
`@axe-core/playwright` 4.14.0, no 5.x exists); the RULE-COVERAGE
re-audit — the activated rule sets at the gate's TAGS enumerated from
BOTH engines via `scripts/parity-probes/axe-rule-census-v68.mjs`
(the axe.js bundle requires cleanly under Node, attaching `axe` to
module.exports; `axe.getRules()` returns metadata keyed `ruleId`):
**69 of 105 rules activated on 4.13.0 AND 69 of 105 on 4.14.0 — the
sets byte-identical, zero added, zero removed** — no new rule to
arbitrate, no markup issue to fix; the deliberate pin bump
(package.json one line, the only manifest change); the lockfile
regeneration (npm dedupe: the wrapper's NESTED engine entry DISSOLVES
— the top-level axe-core@4.14.0, eslint-plugin-jsx-a11y's, whose
^4.10.0 admits it, now satisfies the wrapper's ~4.14.0 too, so the
tree carries ONE axe-core; 23 lockfile lines changed, net -7); the
engine verify (the wrapper's own `require.resolve('axe-core')` →
`node_modules/axe-core/axe.js` = **4.14.0**, no nested dir remains);
**the full a11y gate re-run under 4.14.0: 22 passed** (the v38
contract holds — structural clean, contrast failures only in the
reference's 7-color palette, the login page zero-violation) — no
rule-behavior regression on any scanned surface.

**The v61-era pair re-run** (the dashboard FULL-PAGE at 1280x800 via
vlm-shots-v68.sh + clone-vlmshots-v68.sh + vlm-compare-v68.mjs; login
on the first attempt both sides, the parked pointer at (5,5)):
**VERDICT IDENTICAL** — zero layout/style flags ("the geometry,
borders, padding, typography, icon sizing/tinting, and color palette
for the Budget Guidelines card and the Quick Actions row are visually
identical"), every difference the expected DATA class; the re-run
re-proves the v61-era surfaces live after the v61 STRETCH fix and
v62-v67's pins.

**The v68 pin (+1 → 270):** the a11y gate's ENGINE-CONTRACT pin
(tests/e2e/a11y.spec.ts, a new describe at the file tail, the
logged-out login surface, read-only) — a real AxeBuilder scan asserts
testEngine.name "axe-core" + testEngine.version /^4\.14\./ (the
AxeResults carry the identity of the engine that ACTUALLY executed
the scan — the ground truth, not the lockfile's promise); any future
engine change without a conscious re-verification (a lockfile drift,
a dedupe flip, a wrapper downgrade, a 4.15/5.x bump) fails the suite
— the "never a drift" discipline made executable. GREEN on first
run. The pin-sanity mutation (the TOOLCHAIN downgrade: `npm install
@axe-core/playwright@4.13.0`, no rebuild needed — axe-core is a
test-only dep never in the standalone build) verified to FAIL with
the exact diagnostic, then restored (the restore's own lesson:
`git checkout` reverts to HEAD's ^4.13.0 while the bump is
uncommitted — the restore must re-apply the bump deliberately).

**The 62nd standing checks** (ref-standing-v62.sh +
standing-checks-v62.sh, version-bumped from v61): the mobile menu
VERIFIED WORKING (the 62nd consecutive time), the reference's four
bugs ALL live (toast-blocker, sheet-trap, no-landmark, the 464px
/networth overflow), the data census intact (the 62nd clean drift
check), the SEO pair live. **The screenshots: 10/16 byte-identical
+ 6 the DATE class** (the fresh-cloned workspace's re-seed
re-anchored the seed's isoDate(offsetDays) dates one day later — the
committed set's DB was seeded 2026-10-15; db/ is gitignored, it does
not travel; every changed region pixel-arbitrated to date digits via
the v66 PIL-diff method, the calculator's diff sub-perceptual at max
channel 2; `git diff src/` = 0 lines). Full chain: lint + typecheck
+ 108 unit + build + 270 e2e (97 + 98 + 77 chunks) + 35/35 smoke
green. The docs aligned (AGENTS/CLAUDE/README/SKILL Session 103 row +
the 270 state/PAD v1.1.25/the probe README's v68 section/session_165/
the repo worklog Session 102 + the ledger list). **Next** (the v69
queue): (1) the re-run cadence rotates to the v62-era pair (the
networth mobile 390 full-page twin — the oldest remaining), (2) the
axe-core watch continues at its next re-check point (the 4.14.0
upgrade closes the 4.x story; only a 5.x wrapper changes the
calculus — the engine-contract pin now guards the gate's toolchain),
(3) the deferred reference-write censuses (unchanged).

---

## Session 101 — Parity iteration v67: the v60-era pair's fresh standing sweep (the networth + drill-down EXPANDED re-run) + the axe-core 5.x wrapper watch (the upgrade DECISION: v68 = the dedicated upgrade iteration) + the networth summary card's height-family computed census pin (2026-10-16)

**Goal:** the session-161/162 v67 queue's two items — "the re-run
cadence rotates to the v60-era pair (the networth-view desktop 1280
standing pair — the oldest remaining after v64/v65/v66 covered the
v57/v58/v59 pairs)" and "the axe-core wrapper upgrade decision (the
upstream 4.14.0 — a dedicated upgrade iteration, never a drift)" —
plus the 61st standing checks. **PIN-ONLY** — no production-code
change; the pin-only line continues. The formal narrative:
`docs/session_163.md`; the plan: `docs/remediation-plan-v67.md`.

**The v60-era pair re-run (BOTH of that era's pairs — the v66 precedent:
the v59-era re-run covered the calculator + login set), FULL-PAGE at
1280x800 via vlm-shots-v67.sh + clone-vlmshots-v67.sh +
vlm-compare-v67.mjs: the pair is CLEAN.** The networth half: VERDICT
IDENTICAL — the VLM found ZERO layout/style differences ("pixel-perfect
matches" on the nav rail, the page header, the summary card
geometry/gradient, the tab bar, the card layouts, the typography, the
spacing); every difference the expected DATA class + the Base44 FAB
(platform chrome, excluded by rule). The drill-down EXPANDED half:
VERDICT DIFFERENT with 5 style flags, every one DOM-arbitrated via
arbit-v67.sh + arbit-v67b.sh (the two-part computed census on both
sides — the five flags + the networth summary-card HEIGHT family) to
documented classes: the Dashboard nav highlight (the root-URL
active-nav gap, re-confirmed live: the reference transparent/zinc-700/
400 vs the clone transparent/white/500 — the superset contrast #3),
the avatar ("U" vs "D" — the user-identity class), the hero
progress-bar fill (the pct × 568 data class re-measured live: the
track 568×12 rgba(255,255,255,0.1) BYTE-IDENTICAL both sides, the
fills 173/357 = each site's own allocation pct), the donut percentage
labels (the PERCEPTION ARTIFACT re-confirmed live: both sides render
count 4 [1 group + 3 labels]/labelLineCount 0/16px/black/3 sectors —
the v9 G1b contract holds), and the stat cards' footer TREND ICONS (a
NEW flag variant — "different paths/angles" — DOM-arbitrated to a
PERCEPTION ARTIFACT via a GLYPH census: the icons BYTE-IDENTICAL
16×16/rgb(143,188,63)/viewBox "0 0 24 24" with the same two-polyline
Heroicons-v1 outline trending-up — POLYLINE-based, no `<path>`
element, which is why the census needs the innerHTML glyph signature;
plus the hero-glyph census: the same 7 svgs in the same order on both
sides, every path signature byte-identical).

**The arbitration's own discovery — the never-pinned HEIGHT family**
(the v60 F1 pin covered the card's width/pad/radius/gradient/shadow +
the fonts + the grid template/gap; the v63 F3 pin the stat-tile
heights at 390 — NEVER the 1280 heights), measured BYTE-IDENTICAL on
both sides: the card **960×333** (the deterministic arithmetic 32 +
76 + 32 + 84 + 24 + 24 + 1 + 28 + 32), the head row **h 76** (the
label h 20 + mb 8 + the figure h 48 govern; the 64px medallion rides),
the figure **h 48** (lh 48px), the stat grid **rows "84px"/h 84** (ONE
row at 1280 — the 390 twin's two-row 184 is the v63 class), the stat
tile **440×84** (pad 16 + the label 16 + mb 4 + the amount 32 + pad
16), the ratio footer **mt/pt 24/24 + border 1px + h 53** (the pt 24 +
the border 1 + the ratio row 28 — text-lg's 28px lh).

**The axe watch + the upgrade DECISION:** local NO DRIFT (the registry
state unchanged from v66 — npm-latest 4.14.0 with the declared nested
engine axe-core ~4.14.0 verified by packing the tarball; the lockfile
resolves 4.13.0; the NESTED engine axe-core@4.13.0 byte-identical to
the v38–v66 audits; the top-level 4.14.0 still eslint-plugin-jsx-a11y's
— lint-time only). **The DECISION: the 4.14.0 upgrade is DEFERRED TO A
DEDICATED v68 ITERATION** — never a drift, never a rider (the upgrade
changes the toolchain the a11y.spec.ts contract executes under and
deserves an iteration whose center of gravity is the toolchain change;
the complete specification — the pin bump ^4.13.0→^4.14.0 + the
lockfile regeneration + the nested-engine verify + the full a11y gate
re-run + the rule-coverage re-audit — is carried in the v67 plan's v68
queue). The watch's next re-check point unchanged.

**The v67 pin (+1 → 269):** the networth summary card's HEIGHT-family
computed census at 1280 (tests/e2e/networth.spec.ts, a new describe
after the v60 F1 block, the read-only logged-in state — no fixture
flow needed): the card 960×333, the head row h 76/mb 32px, the label
mb 8px/h 20, the figure lh 48px/h 48, the medallion h 64/iconH 32,
the stat grid rows "84px"/h 84, the stat tile h 84/labelH 16/labelMb
4px/amtH 32, the ratio footer mt 24px/pt 24px/borderTopW 1px/h 53.
GREEN on first run. THREE pin-sanity mutations verified to FAIL then
restored (the head row mb-8→mb-4 [mb 32→16 + card h 333→317]; BOTH
stat tiles p-4→p-2 [the shared-class regression — a FIRST-tile-only
mutation does NOT move the axis: the tile height is STRETCH-GOVERNED,
the grid row follows the taller p-4 sibling and stretches the p-2
tile back to 84, measured live; BOTH tiles: pad 16→8 + tile h 84→68 +
grid rows "84px"→"68px" + card h 333→317]; the ratio footer mt-6
pt-6→mt-3 pt-3 [mt/pt 24→12 + footer h 53→29 + card h 333→309] — each
with the standalone REBUILD as a SEPARATE command).

**The 61st standing checks** (ref-standing-v61.sh +
standing-checks-v61.sh, version-bumped from the v60 family): the
mobile menu VERIFIED WORKING (the 61st consecutive time), the
reference's four bugs ALL live (toast-blocker, sheet-trap,
no-landmark, the 464px /networth overflow), the data census intact
(the 61st clean drift check), the SEO pair live. **The 16 screenshots
BYTE-IDENTICAL** (no production-code change; the capture date
matching the committed set's). Full chain: lint + typecheck + 108
unit + build + 269 e2e (97 + 97 + 77 chunks) + 35/35 smoke green.
The docs aligned (AGENTS/CLAUDE/README/SKILL Session 102 row + the 269
state/PAD v1.1.24/the probe README's v67 section/session_163/the repo
worklog Session 101 + the ledger list). **Next** (the v68 queue): (1)
the DEDICATED axe-core wrapper upgrade iteration (the pin bump
^4.13.0→^4.14.0 + the lockfile regeneration + the nested-engine verify
+ the full a11y gate re-run + the rule-coverage re-audit), (2) the
re-run cadence rotates to the v61-era pair (the dashboard full-page
1280 — the quick-action row + the Budget Guidelines card), (3) the
deferred reference-write censuses (unchanged).

---

## Session 100 — Parity iteration v66: the v59-era pair's fresh standing sweep (the calculator dialog + login view re-run) + the axe-core 5.x wrapper watch (an upstream 4.14.0 appears) + the calculator dialog's height-family computed census pin (2026-10-16)

**Goal:** the session-159/160 v66 queue's two items — "the re-run
cadence rotates to the v59-era pair (the calculator + login views at
1280 — the oldest remaining after v64/v65 covered the v57/v58 pairs)"
and "the axe-core 5.x wrapper watch (unchanged next re-check point)" —
plus the 60th standing checks. **PIN-ONLY** — no production-code
change; the pin-only line continues. The formal narrative:
`docs/session_161.md`; the plan: `docs/remediation-plan-v66.md`.

**The fresh calculator pair (1280x800, `vlm-shots-v66.sh` +
`clone-vlmshots-v66.sh` + `vlm-compare-v66.mjs`): the pair is CLEAN** —
both style flags DOM-arbitrated via `arbit-v66.sh` + `arbit-v66b.sh`
(the computed census on both sides, the row-HEIGHT family added) to
documented classes: the row actions (the POINTER-POSITION class: the
actions rest at **opacity 0 on BOTH sides** [btnCount 2 each; the v6
G9/G10 + v45 F2a pins]; the reference's screenshot caught the pair
mid-reveal — the pointer had rested inside the dialog at shot time, a
capture-timing artifact) and the "• Will update category total" span
(the DATA-CONDITIONAL class: renders while total !== item.amount; the
reference's OWN Rent is natively $25.00 and its single line item sums
to $25.00 → HIDDEN [measured hasWillUpdateSpan:false]; the clone's
modal snapshot carries the opened-at parent $1850 against the
recalculated $25.00 → SHOWN — the conditional itself the pinned
contract); plus the panel's computed box-shadow censused (the
reference's two LEADING zero-alpha layers — the Tailwind v4
computed-form class — over the clone's `.zb-modal-panel` visible layer:
the documented accepted lead-divergence class, the v49 pin's idiom).

**The fresh login pair (`login-shots-v66.sh` + `clone-login-shots-v66.sh`):
VERDICT IDENTICAL** — the only distinction the reference's "Edit with
Base44" FAB (platform chrome, excluded by rule); the census
byte-for-byte (title "ZeroBudget", h1 "Welcome to ZeroBudget", the
same placeholders, the Sign in button 368x48, no `<a>` on either side).

**The never-pinned HEIGHT family (the v66 census's own discovery),
measured BYTE-IDENTICAL on both sides:** the row **720x102** (the
deterministic arithmetic: the 32px top-actions row + the h4's 4px mb +
the 28px amount block + the 32px p-4 padding + the 2px border), the
name h4 block (16px/600/rgb(26,58,46)/h 24/mb 4px), the badge pill row
(flex/gap 8px/12px/h 20), the first pill (h 20/w 65/pad 2px 8px/
radius 9999px/12px/400), the amount P (20px/700/rgb(224,122,59)/h 28),
and the totalCard **h 90** (the 32px total row + the 8px mb-2 + the
16px caption row + the 32px p-4 + the 2px border — the height
arithmetic of the v59-pinned chrome).

**F1 — the axe-core 5.x wrapper watch: local NO DRIFT + an upstream
4.14.0 appears.** The lockfile resolves `@axe-core/playwright` to
4.13.0; the wrapper's NESTED engine `axe-core@4.13.0` byte-identical
to the v38–v65 audits; the top-level 4.14.0 still
eslint-plugin-jsx-a11y's (lint-time only). BUT the npm registry now
carries `@axe-core/playwright@4.14.0` (a MINOR bump inside the
documented 4.x family, NOT the guarded 5.x; the pinned ^4.13.0 would
admit it on an unconstrained fresh install but the lockfile holds the
tree) — recorded as the candidate for a future DEDICATED upgrade
iteration (bump deliberately + re-run the full a11y gate + re-audit
the rule coverage — never a side-effect lockfile drift). The next
re-check point: unchanged.

**The 60th standing checks (`ref-standing-v60.sh` +
`standing-checks-v60.sh`, version-bumped from v59):** reference — the
four bugs ALL live + the data census unchanged (the 60th clean drift
check) + the SEO pair live; clone — R1-R4 green, the mobile navigation
menu **VERIFIED WORKING (the 60th consecutive time)**, zero overflow
at 390 on all five views.

**The v66 pin (+1 → 268): the calculator dialog's HEIGHT-family
computed census at 1280** (`tests/e2e/calculator.spec.ts`, a new
describe after the v59 panel-census block, riding the established
add-then-restoreRent fixture flow): the row 720x102/pad 16px/radius
12px/border-top 1px solid rgb(229,231,227)/bg white, the name h4
16px/600/rgb(26,58,46)/h 24/mb 4px, the badge pill row flex/gap 8px/
12px/h 20, the first pill h 20/w 65/pad 2px 8px/radius 9999px/12px/
400, the amount P 20px/700/rgb(224,122,59)/h 28, the totalCard 720x90.
**THREE pin-sanity mutations verified to FAIL then restored** (the row
p-4→p-2 [pad 16→8 + row h 102→70 — caught by the v66 pin AND the
v45/v49/v53/v59 row pins, 6 failures]; the h4 mb-1→mb-2 [the nameH4
mb axis 4→8]; the totalCard p-4→p-2 [pad 16→8 + totalCard h 90→58] —
each with the standalone REBUILD as a SEPARATE command).

**The 16 screenshots: 15 byte-identical + 1 the documented
dialog-default DATE class** (07-add-item-modal — the calendar rolled
past midnight; the committed set 2026-10-15, this capture 2026-10-16).
Re-arbitrated with a STRONGER method: a programmatic pixel-diff
localized the change to a 16x22 px region at (1552,931)–(1568,953) —
exactly the date input's day digits "15"→"16"; everything else in the
2880x1800 frame byte-stable.

**Probe lessons:** the VLM's "shorter row" was a perception artifact
(the row 720x102 BOTH sides — always measure the computed heights
before believing a proportion claim); the fresh-login first fetch can
exceed the wait window (the reference's /expenses rendered "0 items"
transiently before the data landed — retry the finder on a warm
session); the height arithmetic is deterministic (32+4+28+32+2 = 102 —
a pin on the parts makes the whole predictable); a single-region
screenshot diff is better arbitrated by a programmatic pixel-diff than
a VLM verdict.

**Full chain green:** lint + typecheck + 108 unit + build + 268 e2e
(the --list convention; 267 chromium + 1 setup — the chunk runs 95 +
96 + 79) + 35/35 smoke. **The docs aligned** (AGENTS/CLAUDE/README/
SKILL Session 101 row + the 268 state/PAD v1.1.23/the probe README's
v66 section/session_161/the repo worklog Session 100). Shipped to
`main` via the SSH wrapper, remote-verified, keys shredded.

---

---

---

---

---

---

## Session 99 — Parity iteration v65: the OLDEST remaining desktop pair's fresh standing sweep (the v58-era savings pair re-run) + the axe-core 5.x wrapper watch + the savings page-header row computed census pin (2026-10-15)

**Goal:** the session-155 v65 queue's two items — "the v58-era savings
pair's fresh sweep (the queue's other OLDEST candidate — the v64 pass
covered the v57-era items pair)" and "the axe-core 5.x wrapper watch
(unchanged next re-check point)" — plus the 59th standing checks.
**PIN-ONLY** — no production-code change; the pin-only line continues.
The formal narrative: `docs/session_158.md`; the plan:
`docs/remediation-plan-v65.md`.

**The fresh savings pair (FULL-PAGE at 1280x800, `vlm-shots-v65.sh` +
`clone-vlmshots-v65.sh` + `vlm-compare-v65.mjs`): the pair is CLEAN** —
every flag DOM-arbitrated via `arbit-v65.sh` + `arbit-v65b.sh` (the
computed census on both sides) to documented classes: the avatar (the
user-identity class re-measured live with a NEW perception lesson: the
chrome BYTE-IDENTICAL [36x36/radius 9999px/14px-600/white/bg
rgb(143, 188, 63) on BOTH sides — the same lime]; only the INITIAL
differs — the reference renders "U" for its nameless account, the
clone's demo user "D"; the VLM's "green vs lime" color claim was a
PERCEPTION ARTIFACT — identical computed colors read as different
hues), the card grid layout (the seed-count data class: the axes
BYTE-IDENTICAL [w 960, gap 16px, 3 tracks]; the fractional last-track
distribution CONTENT-COUNT-CONDITIONAL — the reference's template reads
309.328x3 at one child, the clone's 309.328/309.328/309.344 at two;
the v64 census measured the same 309.344 tail both sides at 4-vs-3 —
the axes are the contract, the subpixel tail a rendering artifact of
the data class), the goal-card footer + badges + card heights (the v57
DATA-CONDITIONAL + wrap classes re-measured live: the chrome
BYTE-IDENTICAL [the footer flex justify-between 12px
rgb(107,114,128) h 16 + the 12x12 icons; the badges flex/6px radius/
2px 10px pad/12px-600/h 22; the row flex wrap 8px gap mb 12px]; the
reference's item carries no paymentMethod so its footer renders the
date alone; the clone's Recurring superset badge wraps the row to
h 52 = 22+8+22; the heights 200 vs 230 = the wrap arithmetic), and the
Add button's computed box-shadow (the reference's two LEADING
zero-alpha layers — the Tailwind v4 computed-form class — over the
clone's `.zb-btn-add` visible layers: the visible geometry
BYTE-IDENTICAL, the documented v11 class). **A DOM-structure discovery
(documented, not a gap):** the reference's savings page carries a
HIDDEN zero-size h1 "ZeroBalance" FIRST in its DOM (its own SEO
pattern; an 18px/700 h2 "ZeroBalance" logo in its sidebar) before the
VISIBLE 30px/700 h1 "Savings" — the clone renders the visible h1
alone, BYTE-IDENTICAL chrome.

**The axe-core 5.x wrapper watch: NO DRIFT** — the npm-latest
`@axe-core/playwright` is STILL 4.13.0 (no 5.x release exists), the
wrapper's NESTED engine `axe-core@4.13.0` (what AxeBuilder actually
executes) is byte-identical to the v38/v62/v63/v64 audits, and the
top-level `axe-core@4.14.0` still belongs to eslint-plugin-jsx-a11y
(lint-time only); the next re-check point unchanged.

**The v65 pin (+1 e2e = 267): the SAVINGS view's PAGE-HEADER ROW
COMPUTED census at 1280** (`tests/e2e/items.spec.ts`, inside the
savings describe right after the v38 S2 filter-card test) — the
never-census'd family: the v42 census pinned the MID-640 STACKED state
only (headerRowMb 32px/dir column); the v63 pin the mobile 390 networth
block; the early-era tests pin CLASS STRINGS but never the computed
geometry of the 1280 row. The census, measured BYTE-IDENTICAL on both
sides: the row flex space-between/center/gap 16px/mb 32px/h 60; the
chip 48x48 radius 12px with the savings blue gradient + the white
24x24 icon; the h1 30px/700/lh 36/forestDark; the count subtitle
16px/400/rgb(107,114,128); the Add button 150x36/6px radius/8px 16px
pad/14px/500/white with the savings blue gradient + the .zb-btn-add
visible shadow layers; the 16x16 plus icon. THREE pin-sanity mutations
verified to FAIL then restored (the header row mb-8→mb-4 [mb 32→16];
the chip h-12 w-12→h-10 w-10 [48→40 + the chip finder nulls]; the h1
text-3xl→text-2xl [30px→24px + lh 36→32 + the row h 60→56 — the TEXT
BLOCK governs the row height, not the 48px chip] — each with the
standalone REBUILD as a SEPARATE command).

**The 59th standing checks** (`ref-standing-v59.sh` +
`standing-checks-v59.sh`): the mobile menu verified working (the 59th
consecutive time); the reference's four bugs ALL live (the
toast-blocker, the sheet-trap, the no-landmark, the 464px /networth
overflow); the data census intact (the 59th clean drift check); the SEO
pair live on both sites. **The 16 screenshots BYTE-IDENTICAL.**

**Probe lessons:** identical computed colors can read as different
hues to a VLM (always read the computed backgroundColor before
believing a color flag); the grid's fractional last-track distribution
is content-count-conditional (compare the AXES, never the subpixel
tail at differing child counts); a view's header row can hide behind a
MID-VIEWPORT stacked-state census (the v42 pin covered 640 only); the
hidden zero-size h1 makes querySelector('h1') ambiguous on the
reference — filter by non-zero geometry; the census JS inside the
unquoted heredoc must carry NO dollar sequences (the v64 rule
re-learned as "X: unbound variable").

## Session 98 — Parity iteration v64: the OLDEST desktop pair's fresh standing sweep (the v57-era items pair re-run) + the axe-core 5.x wrapper watch + the income filter-card computed census pin (2026-10-15)

**Goal:** the session-153 v64 queue's first two items — the re-run
cadence on the OLDEST desktop pairs ("v57's items pair and v58's
savings pair predate the v61 dashboard fix and the v62/v63 mobile
twins — a fresh standing sweep of one of them") and the axe-core 5.x
wrapper watch (F1's documented next re-check point) — plus the 58th
standing checks. **PIN-ONLY** — no production-code change; the
pin-only line continues. The formal narrative: `docs/session_155.md`;
the plan: `docs/remediation-plan-v64.md`.

**The fresh items pair (FULL-PAGE income + expenses at 1280×800,
`vlm-shots-v64.sh` + `clone-vlmshots-v64.sh` + `vlm-compare-v64.mjs`):
the pair is CLEAN** — PAIR 1's flags the documented avatar/user-identity
+ Base44/platform-chrome + seed classes (the VLM CONTRADICTED ITSELF on
the FAB between the two pairs — "missing from the clone" in pair 1,
"present in the clone" in pair 2; platform chrome is excluded by rule,
never arbitrated); PAIR 2's three style flags ALL DOM-arbitrated via
`arbit-v64.sh` to documented classes — the card footer content (the v57
DATA-CONDITIONAL class re-measured live: the chrome BYTE-IDENTICAL
[flex justify-between 12px rgb(107,114,128) h 16; every child span
flex gap 4px + the 12×12 gray icon]; the reference's expense items
carry no paymentMethod values so their footers render the date alone;
the clone's render the SAME two-child structure the reference's OWN
income card renders ["Oct 7, 2026" + "Bank Account"]), the badge wrap
(the v57 class re-measured: the chrome BYTE-IDENTICAL; the clone's
Recurring superset badge wraps the row to h 52 = 22+8+22), and the
grid population (the seed-count class: the axes BYTE-IDENTICAL
[960/16px/the template "309.328px 309.328px 309.344px" — the same
fractional last track both sides]; the reference's 4 cards vs the
clone's 3) — plus the card heights (200 vs 230 = the badge-wrap
arithmetic data class).

**The axe-core 5.x wrapper watch: NO DRIFT** — the npm-latest
`@axe-core/playwright` is STILL 4.13.0 (no 5.x release exists), the
wrapper's NESTED engine `axe-core@4.13.0` (what AxeBuilder actually
executes) is byte-identical to the v38/v62/v63 audits, and the
top-level `axe-core@4.14.0` still belongs to eslint-plugin-jsx-a11y
(lint-time only); the next re-check point unchanged.

**The v64 pin (+1 e2e = 266): the INCOME view's filter-card COMPUTED
census at 1280** (`tests/e2e/items.spec.ts`, inside the income describe
right after the early-era class-string filter-card test) — the
never-census'd sibling of the v38 S2 savings pin (v37/v38 measured the
/expenses triggers + the /savings instance; the v52 F2 pin covered this
card's MOBILE 390 state; the early-era test pins CLASS STRINGS only):
the card 960×86 (pad 24px/radius 16px/white/border rgb(229,231,227)/
mb 24px — the 24+36+24+2 height arithmetic) · the search 447×36 (the
2-col span 215.5+16+215.5; the asymmetric 40px left pad — the icon's
room, pl-10; radius 6px/border rgb(229,229,229)) · the inner grid 4
tracks "215.5px"/16px gap/3 children · the two comboboxes 216×36 at
14px ("All Categories"/"All Frequencies"). THREE pin-sanity mutations
verified to FAIL then restored (the card p-6→p-4 [pad 24→16 + h
86→70]; the search wrapper md:col-span-2 removed [w 447→215.5]; the
grid gap-4→gap-2 [gap 16→8 + the tracks recompute] — each with the
standalone REBUILD as a SEPARATE command).

**The 58th standing checks ALL GREEN** (the mobile menu verified
working — the 58th consecutive time; the reference's four bugs ALL
live; the data census unchanged, the 58th clean drift check; the SEO
pair live). The 16 screenshots BYTE-IDENTICAL. Full chain: lint +
typecheck + 108 unit + build + 266 e2e + 35/35 smoke green. The docs
aligned D1–D8 (AGENTS/CLAUDE/README/SKILL Session 99 row + the 266
state/PAD v1.1.21/the probe README's v64 section/session_155 + this
worklog).

---

## Session 97 — Parity iteration v63: the /networth mobile 390 full-page pair (the standing-pair matrix COMPLETED) + the stat-tile family pin + the axe-core version-drift re-check (2026-10-15)

**Goal:** the session-149/151 v63 queue's two items — the standing-pair
program's last un-paired viewport × view combination (a /networth 390
full-page pair) and the axe-core version-drift re-check — plus the 57th
standing checks. **PIN-ONLY** — no production-code change; the pin-only
line continues. The formal narrative: `docs/session_153.md`; the plan:
`docs/remediation-plan-v63.md`.

**The /networth 390 pair — the matrix COMPLETED** (`vlm-shots-v63.sh` +
`clone-vlmshots-v63.sh` + `vlm-compare-v63.mjs`): with this pair, the
{dashboard, items (income/expenses), savings, calculator, networth} ×
{1280 desktop, 390 mobile} matrix is fully paired. VERDICT DIFFERENT
with three flags, ALL DOM-arbitrated via `arbit-v63.sh` to documented
classes — (1) the stat-tile stacking = the v41 mobile-superset class
(the reference's 432-wide card in its own 464 overflow renders its
fixed 2-col grid, tiles 176×84; the clone's 358-fit card stacks 1-col,
tiles 294×84 — the v4 data-fit superset); (2) the card height = the
arithmetic consequence (333 + 84 + 16 = 421); (3) the trend-icon
"larger" = a PERCEPTION ARTIFACT of the v54 clipping class (the
medallion 64×64 + the icon 32×32 BYTE-IDENTICAL both sides; the
reference's clips the 390 viewport at right 416, the clone's fits at
342 — the VLM read the clipped medallion as "smaller").

**The axe-core version-drift re-check: NO DRIFT** — the pinned
`@axe-core/playwright@4.13.0` is still npm-latest and its NESTED engine
`axe-core@4.13.0` (what AxeBuilder actually executes) is
byte-identical to the v38/v62 audits; the top-level `axe-core@4.14.0`
belongs to `eslint-plugin-jsx-a11y` (lint-time only, never scans
pages). The a11y.spec.ts contract stays valid as pinned.

**The v63 pin (+1 e2e = 265): the networth summary card's STAT-TILE
family census at 390** (`tests/e2e/networth.spec.ts`, extending the
v41 F3 describe): the stat grid {cols "294px", gap "16px", w 294, 2
children} · the tiles {294×84; bg rgba(255,255,255,0.1), backdrop
blur(10px), radius 12px, pad 16px} · the card HEIGHT 421 (the 1-col
stacking arithmetic) · the medallion's inner icon 32×32. THREE
pin-sanity mutations verified to FAIL then restored (the grid
gap-4→gap-2 [gap 16→8 + card h 413]; the tile p-4→p-2 [h 68]; the
medallion svg h-8→h-6 [icon 24] — each with the standalone REBUILD as
a SEPARATE command).

**The 57th standing checks ALL GREEN** (the mobile menu verified
working — the 57th consecutive time; the reference's four bugs ALL
live; the data census unchanged, the 57th clean drift check; the SEO
pair live). The 16 screenshots BYTE-IDENTICAL (no re-seed this
session). Full chain: lint + typecheck + 108 unit + build + 265 e2e +
35/35 smoke green. The docs aligned D1–D8 (AGENTS/CLAUDE/README/SKILL
Session 98 row + the 265 state/PAD v1.1.20/the probe README's v63
section/session_153 + this worklog).

---

## Session 96 — Parity iteration v62: the reference-side a11y re-audit (NO DRIFT since v38) + the TWO-pair VLM program (desktop + the NEW mobile 390 twin) + the mobile header-subtitle 390 census pin (2026-10-15)

**Goal:** the session-147 v62 queue's first TWO items — the reference-side
a11y surface re-audit (deferred from v61: "has the reference's own axe
tree drifted since v38?") and the SKILL doc's four stale count lines
(177/474/1191/1255, the v61 doc digest's flag) — plus the 56th standing
checks and the standing VLM program's mobile extension. **PIN-ONLY** — no
production-code change; the pin-only line resumes after the v61 fix.
The formal narrative: `docs/session_151.md`; the plan:
`docs/remediation-plan-v62.md`.

**The a11y re-audit (`axe-detail-ref-v62.mjs`, the full a11y.spec.ts
surface: six authed routes at 1280 + the 404 + the logged-out login + the
mobile 390 sheet-open state, axe-core 4.13, the same four tags): NO
DRIFT** — the logged-out login still ZERO-violation clean; the structural
families still exactly `button-name` (10 nodes: the unlabeled Select
triggers + card kebabs) + `svg-img-alt` (6 nodes: the recharts donut
sectors `path[name=…]`) — the two families the clone deliberately fixes
(GATE 1's superset contrast); the contrast palette still EXACTLY the v38
7-color set (lime / blue / orange / orangeLight / gray-500 / #cbd5e1 /
zinc-500) — no new low-contrast color entered the reference's design, so
the clone's GATE 2 allow-list needs no change; the mobile sheet-open tree
carries color-contrast only. **The clone's a11y.spec.ts contract remains
valid as pinned.**

**The TWO-pair VLM program (`vlm-shots-v62.sh` + `clone-vlmshots-v62.sh` +
`vlm-compare-v62.mjs`): the desktop 1280 full-page pair + the NEW mobile
390x844 full-page twin.** The desktop pair's five flags ALL arbitrated to
documented classes (the nav-highlight root-URL gap [the reference's own
bug, the clone's superset fix #3]; the avatar U-vs-D [user-identity]; the
progress-bar length [allocation data class]; the donut labels [PERCEPTION
ARTIFACT — the reference renders its three (92.3/4.6/3.1), DOM-verified,
the clone its own (81.6/13.8/4.6)]; the Base44 FAB [platform chrome]).
The mobile pair's two flags both arbitrated (the Base44 tooltip [platform
chrome]; **"the clone's subtitle wraps to a third line" — a PERCEPTION
ARTIFACT**, DOM-arbitrated via `arbit2-v62.sh`: the leaf-text census
measured the subtitle P on BOTH sides byte-identical [h 48, 2 lines,
16px/400/rgb(107,114,128), lh 24px, block h 92, top 121; the 5px width
delta is the reference's own 395px docSW overflow] — the v61
meta-lesson's INVERSE: the DOM census ACQUITTED what the VLM convicted).

**The v62 pin (+1 e2e = 264): the mobile header-subtitle block census at
390** (`tests/e2e/dashboard.spec.ts`, the "mobile header-subtitle block
census at 390" describe — the never-pinned surface the M2 arbitration
measured): the P {h 48, top 121, 16px/400/gray-500, lh 24px, 2 lines} +
the lineRhythm contract [the delta between the two line tops = exactly
the 24px line-height — the glyph rects themselves are ~19px font
metrics, deliberately NOT pinned] + the block {h 92 = h1 36 + mb-2 8 +
p 48, top 77} + the h1 {36/30px/700/mb 8px}; the WIDTH axis deliberately
not pinned (the WRAP OUTCOME is the contract). ONE pin-sanity mutation
verified to FAIL then restored (the inline lineHeight 24→28px → h 48→56,
lineRhythm 24→28, lh "28px" — three axes at once; the standalone REBUILD
as a SEPARATE command).

**The F3 docs sweep:** the SKILL doc's four stale current-state count
lines corrected (the 214-era bootstrap line, the 223/223 gate line, the
223 decisions line, the 22-files/214-tests inventory line — all now the
current counts; the historical session rows stay era-correct).

**The 56th standing checks:** the mobile menu VERIFIED WORKING (the 56th
consecutive time — R1 hit-test true + sheet opens, R2 closes + navigates,
R3 landmark, R4 zero overflow at 390 on all five views); the reference's
four bugs ALL live (toast-blocker, overlay trap, no-landmark, the 464px
/networth overflow); the data census intact ("1 items · $25,000" /
"1 items · $5000.00" / "4 items · $525.00"); the SEO pair live on both
sites.

**The 16 screenshots:** 10 byte-identical + 6 VLM-arbitrated (5 the
SEED-DATE class — the item-view card footers + the details date row +
the networth Updated stamp, each advanced exactly one day, the dev DB
re-seeded this session; 1 [08-calculator] a 1,596-pixel/57×73-bbox
sub-perceptual AA-timing class — the full-shot VLM AND the 3×-upscaled
region-crop re-arbitration both IDENTICAL).

**Full chain GREEN: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · 264
e2e ✓ (95 + 93 + 75, three ordered chunks, zero failures) · 35/35 smoke
✓.** The docs aligned (AGENTS/CLAUDE/README/SKILL Session 97 row + the
264 state / PAD v1.1.19 / the probe README's v62 section / session_151 /
this worklog). One new e2e, 263 → 264.

---

## Session 95 — Parity iteration v61: the Budget Guidelines card's STRETCH fix (the FIRST production-code change since v55) + the quick-action row + the guidelines chrome 1280 censuses (2026-10-15)

**Goal:** the session-144 v61 queue's first TWO items — the
QUICK-ACTION card surfaces' 1280 pair (the v45 F3 hover-shadow pin is
at 640; the resting chrome at the pair viewport unpaired) and the
BUDGET GUIDELINES card's 1280 pair (the v51 F4 mobile census's desktop
twin) — plus the 55th standing checks. **NOT pin-only**: the DOM
census caught a real production gap the full-page VLM pair missed.
The formal narrative: `docs/session_147.md`; the plan:
`docs/remediation-plan-v61.md`.

**The finding:** the reference's Budget Guidelines card sits at
NATURAL height (348) inside a stretched `space-y-4` wrapper (the grid
child; the row 656 under the seed; the card ends right after the
Savings tile — the remaining ~308px of the column are page
background), while the clone's card ITSELF stretched to 656 with
~308px of empty white card body + border + shadow below the last
tile. Arbitrated three ways — the DOM census both sides, the
REGION-CROP VLM re-arbitration (the x 770-1258 / y 764-1472 column
crops: DIFFERENT pre-fix / SAME post-fix), and the reference's own
row DOM measured live. **The fix mirrors the reference's DOM** (the
guidelines card wrapped in a `space-y-4` div at the lg:grid-cols-2
row's right column) — TDD: the pin RED (cardH Expected 348, Received
656) → the fix → GREEN.

**The censuses:** the quick-action row byte-identical on every axis
both sides (the grid 960/"304px 304px 304px"/gap 24 — the content
column 1280 − 256 sidebar − 64 p-8; the cards 304×90/radius 16px/pad
24px/border rgb(229,231,227)/shadow none at rest; the icon tile
40×40/radius 12px/the type tints [a DIV on the reference, a SPAN on
the clone — the chrome the contract]; the label 16px/500/
rgb(26,58,46) via the LEAF-SPAN finder [the v61 label lesson]; the
plus 16px/opacity 0.5). The guidelines chrome byte-identical (the
card 468/12px/white + the shadow's visible layers [the leading
zero-alpha layer count the Tailwind v4 computed-form class]; the
header/body; the three GUIDELINE_ROWS tiles 418×78 byte-identical —
the constant content, the deterministic natural height). The DOM-shape
classes documented (no action): the reference's `mb-8` row margins vs
the clone's `mt-8` (identical geometry — the quick grid top 1462 BOTH
sides); the tile/row tag differences; the shadow's leading layers.

**The pins:** the "Budget Guidelines card census at 1280" describe
(the card chrome + the NO-STRETCH contract: cardH 348 + the card
bottom one body-pad below the last tile [±1 subpixel] + the row 656 −
card 308) + the "quick-action card row census at 1280" describe (the
grid + the three cards' chrome trio + the leaf-span label) — +2 →
263. THREE pin-sanity mutations verified to FAIL then restored (the
wrapper removal → cardH 656 again; the card p-6→p-8 → h 106 vs 90;
the tile rounded-xl→rounded-2xl → the radius-12 chrome finder nulls).
The 55th standing checks clean (the mobile menu verified working —
the 55th time; the reference's four bugs ALL live; the data census
intact; the SEO pair live both sides).

**The chain:** lint + typecheck + 108 unit + build + **263 e2e (93 +
94 + 78, three ordered chunks, zero failures)** + 35/35 smoke — all
green. The 16 screenshots byte-identical (the fix's visual effect
lives below every viewport shot's fold — the pinned census + the
crop arbitration carry the verification). Docs aligned D1–D8;
`docs/remediation-plan-v61.md` + the probe family persisted.

**Next:** the v62 queue — the reference-side a11y surface re-audit
(has the reference's own axe tree drifted since v38?), the deferred
reference-write censuses (unchanged), and a sweep of the SKILL doc's
stale count lines (177, 474, 1191, 1255 — pre-existing doc drift
flagged by the v61 doc digest).

---

## Session 94 — Parity iteration v60: the networth-view desktop 1280 VLM standing pair + the dashboard drill-down EXPANDED-state pair (PIN-ONLY — the sixth consecutive pin-only iteration) (2026-10-15)

**Goal:** the session-141 v60 queue's first TWO suggestions — the
NETWORTH view's DEDICATED desktop 1280x800 pair (the standing-pair
program's remaining major view; the v56 PAIR 2 was the glyph-swap
audit pass) and the DASHBOARD's drill-down EXPANDED surfaces at 1280
(the first VLM pair over the expanded drill-down) — plus the 54th
standing checks (the expenses census now in the standing script).
PIN-ONLY: no production gap found; the deliverables are TWO pins (+2
e2e → 261). The formal narrative: `docs/session_144.md`; the plan:
`docs/remediation-plan-v60.md`.

**The sweep:** the networth pair VERDICT IDENTICAL (zero layout/style
flags; every difference the expected data class — the figures, the
groups, the ratio "∞:1" vs "0.21:1"); the census byte-identical on
every axis (the summary card 960/32px/16px/the 135deg forest→lime
gradient/the rgba(26,58,46,0.3) shadow; the medallion 64×64; the stat
grid 440px 440px gap 16; the tile 16px/12px/white-10%/blur(10px);
the tablist 448/36/"220px 220px"; the group header 18px/600/forest-
medium; the grid 960/3×309.328/gap 16 + the card 309/20px/12px — the
v46 F2 values re-confirmed live). The drill-down pair: FIVE flags,
every one DOM-arbitrated — the nav highlight (the root-URL active-nav
gap), the avatar (user-identity), the Base44 tooltip (platform
chrome), the hero progress fill 30.5% vs 62.8% (the pct × 568 data
class), and the donut percentage labels (a PERCEPTION ARTIFACT — the
reference DOES render them: 3 texts/labelLineCount 0/16px/black, the
v9 G1b measurement re-confirmed live both sides); the drill census
byte-identical on every axis (the card 304; collapsed 364 BOTH; the
section/category/sub/item/footer chrome; the heights 364→445→499
[reference] vs 364→481→535 [clone] = the data class — its one Salary
category vs the seed's two). One census-axis false alarm arbitrated
by the itemdump (the reference-side rows[last] caught the item row's
INNER label-group div — the REAL item row byte-identical).

**The pins:** the "net worth view census at 1280" describe in
`tests/e2e/networth.spec.ts` (+1) + the "drill-down sub/item-row
census at 1280" describe in `tests/e2e/dashboard.spec.ts` (+1 → 261)
— both GREEN on the first run; the finder pins the REAL rows by
their chrome (justify-between + pad "4px 8px"), never rows[last].
THREE pin-sanity mutations verified to FAIL then restored (the
summary card p-8→p-10; the tablist max-w-md→max-w-lg [448→512]; the
item label max-w-[120px]→max-w-[140px]). The 54th standing checks
clean (the mobile menu verified working — the 54th time; the
reference's four bugs ALL live; the data census intact; the SEO pair
live both sides).

**The chain:** lint + typecheck + 108 unit + build + 261 e2e (91 +
94 + 78, three ordered chunks, zero failures) + 35 smoke — all
green. The 16 screenshots: 15 byte-identical + 1 diff the DATE class
(07-add-item-modal's Date input defaults to the capture-run day
10/14→10/15 — VLM-arbitrated DATE-TEXT-only, zero layout diffs).
Docs aligned: AGENTS/CLAUDE/README/the SKILL doc (Session 95 row +
the 261 state)/the PAD (v1.1.17)/the probe README (the v60 section +
five lessons)/this worklog.

**Probe lessons (the v60 five):** a single-quoted bash census string
must contain NO single quotes (the JS '[role="tablist"]' selectors
terminate the string — the eval silently returns empty; escaped
double-quoted JS strings or a quoted heredoc); the FULL-PAGE
screenshot (--full) is the pair-shot mode for views taller than the
800 viewport; the drill-down expansion clicks are view-state toggles
(safe under the v46 read-only rule); the recharts label census
filters the individual <text> labels from the group wrapper (count 4
= 1 group + 3 labels); census row-finders pin rows by chrome (pad/
justify-between), never by array position.

**Next:** the v61 queue — the quick-action card surfaces' 1280 pair,
the Budget Guidelines card's 1280 pair, or the deferred
reference-write censuses (unchanged).

---

## Session 93 — Parity iteration v59: the calculator-view desktop 1280 VLM standing pair + the calculator panel/total-card census (PIN-ONLY — the fifth consecutive pin-only iteration) (2026-10-15)

**Goal:** the session-139 v59 queue's first TWO suggestions — the
CALCULATOR dialog's desktop 1280x800 VLM pair (the panel + row
surfaces) and the LOGIN view's 1280 pair — plus the 53rd standing
checks. PIN-ONLY: no production gap found; the deliverable is the
calculator panel + total-card census pin (+1 e2e → 259). The formal
narrative: `docs/session_141.md`; the plan:
`docs/remediation-plan-v59.md`.

**The sweep:** the calculator pair CLEAN per the v43 rule — both VLM
flags DOM-arbitrated (the "Will update category total" span is
DATA-CONDITIONAL [the lineTotal-vs-parentAmount-at-open contract; the
reference's own Rent $25 === its line-item sum so hidden, the clone's
$1850 parent showed it]; the row's hover-action pair a
POINTER-POSITION artifact [both sites gate opacity 0 at rest]); the
census byte-identical on every axis (the panel 768×393 @ 256,204 —
the centering invariant / radius 16 / maxW 768px / maxH 680px [85vh
of 800] / the 2xl VISIBLE layer / the total card 720×90 #fff7f5
radius 12 pad 16 / the close 36×36 / the header border-b / the row
720 pad 16 radius 12 transition all 0.15s — the v45 F2a values). The
login pair IDENTICAL (the only flag the reference's Base44 platform
badge). The clone-side pair state built by adding the reference's OWN
"Contents Insurance" $25 line item through the real UI, then FULLY
restored (delete + the $1850 edit restore + the $2235.00 total
verified).

**The pin:** the "calculator panel census at 1280" describe in
`tests/e2e/calculator.spec.ts` (+1 → 259) — GREEN on the first run;
THREE pin-sanity mutations verified to FAIL then restored (the total
card bg #fff7f5→#fff8f0; the panel maxWidth 48rem→42rem; the total
card p-4→p-5). The 53rd standing checks clean (the mobile menu
verified working — the 53rd time; the reference's four bugs ALL
live; the reference's /expenses census documented: "4 items ·
$525.00", its Rent carrying one "Contents Insurance" line item).

**The chain:** lint + typecheck + 108 unit + build + 259 e2e (90 +
94 + 76, three ordered chunks, zero failures) + 35 smoke — all
green. The 16 screenshots: 9 byte-identical + 7 diff the SEED-DATE
class (the seed's isoDate(-N) anchors to the seed-run date —
VLM-arbitrated DATE-TEXT-only, zero layout diffs).

**Probe lessons:** `agent-browser mouse click` DOES NOT EXIST in
0.39.0 (`mouse down`+`mouse up` after a `mouse move`; the swallowed
failure opens the ITEM DETAILS dialog — a false-failure signature);
the eval output is a JSON-encoded STRING (strip the quotes before
`cut`); the reference's dialogs are PLAIN fixed divs (find by
geometry, not [role=dialog]); the reference's session EXPIRES between
long eval gaps.

---

## Session 92 — Parity iteration v58: the savings-view desktop 1280 VLM standing pair + the savings goal-card's footer/badge census (PIN-ONLY — the fourth consecutive pin-only iteration) (2026-10-13)

**Goal:** the session-137 v58 queue's own first suggestion — the
SAVINGS view's desktop 1280 pair (the items family's remaining view;
the v57 pair covered income + expenses) — plus the 52nd standing
checks. The sweep found NO production gap, so the v58 deliverable is
the PIN: the savings goal-card's footer + badge census (+1 e2e ->
258). (The workspace re-cloned once this session — the sandbox had
reset again; the environment rebuilt from scratch.)

**The baseline chain.** lint + typecheck + 108/108 unit + build +
257 e2e (104 + 138 + 14, three ordered chunks this session — the
chunk-regex lesson: the Playwright file-filter alternation must match
the FULL filename stem, an `auth\.spec` stem plus the shared
`\.spec\.ts` suffix double-matches and silently drops three spec
files) + 35/35 smoke — all green.

**The 52nd standing checks.** The reference side: the four bugs ALL
live (the toast-blocker, the sheet-trap via overlayCount 1, the
no-landmark, the 464 /networth overflow), the data census intact
("1 items · $25,000" / "1 items · $5000.00"), the SEO pair live. The
clone side: R1 the burger hit-test true + the sheet opens, R2 the
Income nav closes AND navigates, R3 the nav landmark, R4 zero
overflow at 390 on all five views — **the mobile navigation menu
VERIFIED WORKING (the 52nd time)**.

**The v58 sweep** (the probe family, READ-ONLY on the reference):
the desktop 1280x800 VLM pair on the savings view — every flag
DOM-arbitrated to the documented data classes: the seed data (the
reference's own 1-item savings view ["1 items · $1000.00",
"Emergency Fund" $1000] vs the clone's dev seed ["2 items ·
$1250.00", Investments + Emergency Fund]); the savings card's footer
content (DATA-CONDITIONAL — the footer row's chrome byte-identical
on both sites [flex justify-between 12px rgb(107,114,128) h 16; each
span flex gap 4px with the 12×12 gray icon]; the reference's own
savings item carries NO paymentMethod so its footer renders the
ONE-child date-only form, the clone's render the SAME two-child
structure the reference's own income card renders [the date +
"Brokerage"] — the v57 conditional-footer contract measured on the
third view); the badge family (DATA-CONDITIONAL — the row's chrome
byte-identical [flex wrap 8px mb 12px; every badge flex center /
6px / 2px 10px / 12px/600 / h 22 / the 12×12 icons]; the reference's
savings item is classified "need" [the red family] while the clone's
are "savings" [the green family] — the classification VALUE is the
data class, the color maps stay locked by badge-colors.spec.ts; the
monthly purple-50 + active slate-50 badges byte-identical both
sides; the clone's Recurring superset badge wraps the row to h 52 =
22+8+22). The grid census: the 960px 3-column grid + the 16px gap +
the card chrome (309 / 20px / 12px / 1px solid rgb(229,231,227) /
white) — the v45 F1a pin's own values.

**The pin.** The "the savings goal-card census at 1280 (v58 — plan
F1)" describe in `tests/e2e/items.spec.ts` (+1): the /savings grid
(960/2 children/16px gap/3-col template) + the Investments card's
two-children conditional footer (the date span + the "Brokerage"
chip) + the wrapped 4-badge row (h 52, [savings, monthly,
Recurring, active]) + every badge's geometry. GREEN on the first
run (the pin-only iteration's own expectation). THREE pin-sanity
mutations verified to FAIL then restored (the footer text-xs->
text-sm, the badge-row gap-2->gap-4, the classification badge
py-0.5->py-1 — the fresh VERTICAL-pad axis proving the wrap
arithmetic 22+8+22 — each with the standalone REBUILD as a SEPARATE
command; each also bit the v57/v54 footer+badge pins, the correct
shared-line signature).

**The full chain (final).** lint + typecheck + 108/108 unit + build +
**258 e2e (78 + 38 + 144, three ordered chunks, zero failures)** +
35/35 smoke. The 16 screenshots regenerated ALL BYTE-IDENTICAL (the
pin-only invariant; `git diff src/` empty).

**The probe lessons.** (1) a comment apostrophe inside a
single-quoted shell census variable terminates the quote (bash -n
before every run); (2) the reference's savings item is classified
NEED — the classification VALUE is the data class, the color maps
stay locked by badge-colors.spec.ts; (3) the e2e-chunk filter's
file alternation must match the full filename stem.

**The docs.** AGENTS/CLAUDE/README (the 258 counts + the v58
entries), the SKILL Session 93 row + the state line, the PAD
v1.1.15 block, the probe README's v58 section, session_139.md (the
formal log), the ledger list + this Session 92 entry. Ship: the
Conventional Commit + the SSH-wrapper push to main.

---

## Session 91 — Parity iteration v57: the items-view desktop 1280 VLM standing pair + the item-card footer/badge-row census (PIN-ONLY + one TEST-ONLY flake fix) (2026-10-13)

**Goal:** the session-134 v57 queue's own standing-check suggestion —
a fresh VLM pair on the ITEMS view's desktop 1280 state (the v56 pair
covered the dashboard + networth) — plus the 51st standing checks.
The sweep found NO production gap, so the v57 deliverable is the PIN:
the item-card footer + badge-row census (+2 e2e -> 257) and one
TEST-ONLY flake fix (the not-found G7 "Go Home" race). (The workspace
re-cloned TWICE this session — the sandbox reset mid-conversation;
the environment rebuilt both times.)

**The baseline chain.** lint + typecheck + 108/108 unit + build +
255 e2e (115 + 141, two ordered chunks) + 35/35 smoke — all green.

**The 51st standing checks.** The reference side: the four bugs ALL
live (the toast-blocker, the sheet-trap via overlayCount 1, the
no-landmark, the 464 /networth overflow), the data census intact
("1 items · $25,000" / "1 items · $5000.00"), the SEO pair live. The
clone side: R1 the burger hit-test true + the sheet opens, R2 the
Income nav closes AND navigates, R3 the nav landmark, R4 zero
overflow at 390 on all five views — **the mobile navigation menu
VERIFIED WORKING (the 51st time)**.

**The v57 sweep** (the probe family, READ-ONLY on the reference):
the desktop 1280x800 VLM pair on the income + expenses views — every
flag DOM-arbitrated to the documented data classes: the avatar (the
user-identity class), the seed data, the payment-method chips
(DATA-CONDITIONAL — the footer row's chrome byte-identical on both
sites [flex justify-between 12px rgb(107,114,128) h 16; each span
flex gap 4px with the 12×12 gray icon]; the reference's own income
card renders the SAME two-child structure [the date + "Bank Account"]
while its expense items carry no payment methods), the badge wrap
(the row's chrome byte-identical [flex wrap 8px mb 12px; every badge
flex center / 6px / 2px 10px / 12px/600 / h 22]; the clone's
Recurring superset badge wraps the row to h 52 = 22+8+22). The grid
census: the 960px 3-column grid + the 16px gap + the card chrome
(309 / 20px / 12px / 1px solid rgb(229,231,227) / white) — the v45
F1a pin's own values.

**The pin.** The "items card footer + badge census at 1280 (v57 —
plan F1)" describe in `tests/e2e/items.spec.ts` (+2): F1a the
/income card's footer two-children conditional render (the date span
+ the PayPal chip) + the badge chrome; F1b the /expenses grid census
(960/3 children/16px gap/3-col template) + the wrapped 4-badge row
(h 52). THREE pin-sanity mutations verified to FAIL then restored
(the footer text-xs->text-sm, the badge-row gap-2->gap-4, the badge
px-2.5->px-2 — each with the standalone REBUILD as a SEPARATE
command).

**The flake fix (TEST-ONLY).** The full-chain re-run surfaced the
not-found G7 "Go Home" flake (three chunk-run failures in one
session); the root-cause probe (`--repeat-each=8` on an idle
machine) proved it a genuine ~1-in-8 race — the file-wide logged-out
opt-out applied to a test asserting an AUTHENTICATED surface (the
"Budget Dashboard" heading lives only in the ~50-180ms window
between the page boot and the RequireSession /login redirect). The
fix: the test moves into its own describe carrying a describe-scoped
storageState override (`tests/e2e/.auth/user.json`). Verified:
`--repeat-each=10` -> 21/21, the full spec 7/7, the whole chunk 2
green (143).

**The full chain (final).** lint + typecheck + 108/108 unit + build +
**257 e2e (115 + 143, two ordered chunks, zero failures)** + 35/35
smoke. The 16 screenshots regenerated ALL BYTE-IDENTICAL (the
pin-only invariant; `git diff src/` empty).

**The probe lessons.** (1) the badge-row finder walks the card's
DIRECT children (the row is a direct child, not nested); (2) the
clone-side with-server heredoc must be QUOTED (<<'EOF') when it
carries a $-expanded census variable; (3) the reference's expenses
items carry no payment methods — the conditional footer is the
parity contract, not a drift.

**The docs.** AGENTS/CLAUDE/README (the 257 counts + the v57
entries), the SKILL Session 92 row + the state line, the PAD
v1.1.14 block, the probe README's v57 section, session_137.md (the
formal log), the ledger list + this Session 91 entry. Ship: the
Conventional Commit + the SSH-wrapper push to main.

---

## Session 90 — Parity iteration v56: the 1280 desktop VLM standing pair + the glyph-swap HOLD re-audit (PIN-ONLY — no production-code change, the return to pin-only after the v55 fix) (2026-10-13)

**Goal:** the session-131 v56 queue's own standing-check suggestion —
a fresh VLM pair on the v55 F1 surfaces' desktop 1280 state —
extended with the full glyph re-audit (does the v55 swap still
hold?) and the 50th standing checks. The sweep found NO production
gap, so the v56 deliverable is the PIN: the hero-card DESKTOP 1280
census (+1 e2e -> 255). (The workspace re-cloned at 818f553; the
environment rebuilt — npm install + .env from .env.example +
db:push/db:seed + `npx playwright install chromium`.)

**The v56 sweep** (the ten-probe family, READ-ONLY on the
reference): `glyph-audit-v56.sh` re-audited the full per-view lucide
glyph dictionary on BOTH sites (the v55 audit with the
polyline/rect-rx capture fix) — **24 shared glyph names, 0 DIFFS
among the shared set: the v55 legacy-icon swap HOLDS byte-identical;
no new drift** (1 one-side-only: repeat, the Recurring superset
badge). `vlm-shots-v56.sh` + `clone-vlmshots-v56.sh` +
`vlm-compare-v56.mjs` ran the desktop 1280x800 pair (the session-131
queue item): PAIR 2 (the networth trending surfaces) VERDICT
IDENTICAL; PAIR 1 (the dashboard) flagged 4. `vlm-arbit-v56.sh` +
`clone-arbit-v56.sh` arbitrated every PAIR 1 flag (the v43 rule):
the nav highlight = the documented root-URL active-nav gap (a
reference bug the clone fixes; the non-root control at /networth
renders the byte-identical 135deg forest-gradient active style on
BOTH sites), the progress bar = the track byte-identical 568x12 on
both sites with the fill = pct x 568 per each site's own data, the
avatar = the user-identity class, the FAB = the Base44 platform
chrome — the pair CLEAN. `hero-desk-v56.sh` censused the hero card
at 1280x800 on both sites: byte-identical (the 304px triple-column
grid, the 632x316 goal card, the 568x12 track, the 90deg fill, the
48px stat tiles).

**The pin.** The "hero desktop 1280 census (v56 — plan F1)"
describe in `tests/e2e/dashboard.spec.ts` (+1): the hero grid's
304px triple-column template + 24px gap + the [632x364, 304x364]
children at y 136, the goal card's 632x316/radius 16/pad 32/135deg
forest gradient + shadow, the 568x12 track, the fill's 90deg
status-gradient family + the pct-proportional width arithmetic
(+-2px), the three 48px stat tiles' 24x24 svgs. GREEN on the first
run (pin-only). THREE pin-sanity mutations verified to FAIL then
restored (the track h-3->h-2; the card p-8->p-6; the grid
gap-6->gap-4) — each with the standalone REBUILD as a SEPARATE
command (the first sed attempt taught the line-addressed
class-token lesson — a display-rendering pattern silently no-ops
against the source's own spacing).

**The standing checks (50th).** The reference's four bugs ALL live
(the toast-blocker, the sheet-trap, the no-landmark, the 464
/networth overflow); the data census intact (no trending-down
opportunity); the clone's mobile navigation menu VERIFIED WORKING
(R1 the burger hit + the sheet, R2 the close-on-nav, R3 the
landmark, R4 the zero overflow at 390 on all five views; the SEO
pair 200 on both).

**The chain.** lint + typecheck + 108/108 unit + build + **255 e2e
(105 + 151, two ordered chunks, both exit 0, zero failures — +1:
the hero-desk pin)** + 35/35 smoke. The 16 screenshots regenerated
— 7 trivial timing diffs (0.002-0.005% of pixels, pixel-compared;
`git diff src/` empty — the pin-only invariant). The docs aligned
(AGENTS/CLAUDE/README/SKILL Session 91 row + the 255 state/PAD
v1.1.13/the probe README's v56 section/session_134 +
session_135/this worklog + the ledger list). Commit + push to main
via the SSH wrapper.

---

## Session 89 — Parity iteration v55: the ICON-GLYPH swap (the piggy-bank / trending-up / search / mail legacy glyphs — THE FIX, the fifth production-code change since v46) + the full-glyph-audit probe family (2026-10-13)

**Goal:** the session-128 v55 queue's goal-card classification-icon
glyph census (the v44 glyph-swap family's badge-row application),
extended to a FULL icon-glyph audit — which found FOUR drifted
glyphs and delivered the first production-code change since the v52
fix. TDD-first, the 49th standing checks, the VLM pair, the docs
aligned, push via the SSH wrapper. (The workspace re-cloned at
78a1966; the environment rebuilt — npm install + .env from
.env.example + db:push/db:seed + `npx playwright install chromium`.)

**The v55 sweep** (the six-probe family, READ-ONLY on the reference):
`ref-v55.sh` + `clone-v55.sh` measured the goal-card's icon glyphs
at 390 + the /expenses same-glyph control — the heart, the
circle-alert, and the calendar glyphs byte-identical, but the
PIGGY-BANK differs (the reference's OLD 3-path body vs
lucide-react 0.525's redesign). `piggy-sweep-v55.sh` swept the
reference's every piggy svg (six surfaces — the nav rail, the
quick-action, the stat row, the donut legend, the hero, the chip —
all the OLD glyph). `glyph-audit-v55.sh` + `glyph-diff-v55.mjs`
ran the FULL audit: 24 shared lucide glyphs — 19 byte-identical,
4 DRIFTED (piggy-bank, trending-up [two POLYLINES], search [4.3
vs 4.34], mail [a1.94 1.94 vs a2 2]), 1 clone-only (repeat).
`glyph-exact-v55.sh` captured the exact reference markup — the
byte source for the fix.

**The fix + the pin.** `src/components/ui/legacy-icons.tsx` (four
components rendering the reference's EXACT svg: the base attrs +
the path/polyline/rect/circle children byte-identical, the `lucide
lucide-<name>` class prefix kept — the e2e pins select
svg.lucide-* — and aria-hidden mirroring lucide's own no-a11y-prop
rule) + the eight import swaps (item-card / items-view /
dashboard-view / item-details-dialog / budget-item-dialog /
sidebar / net-worth-view / login-card). The spec written FIRST:
`tests/e2e/glyph-parity.spec.ts` RED (5 failed — the four glyph
families + networth; the heart + circle-alert controls passed),
GREEN post-fix (7 passed). SIX pin-sanity mutations verified to
FAIL then restored (the piggy body path; the trending polyline
points; the search handle 4.3→4.34; the mail flap a1.94→a2; ONE
usage-site revert) — each with the standalone REBUILD as a
SEPARATE command.

**The standing checks (49th) + the VLM pair.** The reference's four
bugs ALL live; the clone's mobile navigation menu VERIFIED WORKING
(R1–R4, the SEO pair 200 on both). The VLM pair (the calculator
dialog's with-row — the v53 F2 surface + the goal card post-swap):
every flag DOM-verified (the X-close 29×36 transparent
byte-identical — an artifact; the amounts 24/700 on both — a
digits-count misread; the calculator's state difference + the
goal-card flags = the documented seed-data classes) — the pair
CLEAN per the v43 rule.

**The chain.** lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
254 e2e (122 + 133, two ordered chunks, both exit 0, zero failures
— +6: the glyph-parity suite) · 35/35 smoke ✓. The 16 screenshots
regenerated — 14 byte-diffs (the production-change invariant, the
first non-pin-only regeneration since v49). The docs aligned
(AGENTS/CLAUDE/README/SKILL Session 90 row + the 254 state/PAD
v1.1.12/the probe README's v55 section/session_131 +
session_132/this worklog + the ledger list). Commit + push to main
via the SSH wrapper.

---

## Session 88 — Parity iteration v54: the savings goal-card's badge-row + footer internals at 390 (PIN-ONLY — the third consecutive pin-only iteration) + the footer-locator/blockification probe lessons (2026-10-12)

**Goal:** the session-125 v54 queue's first read-only member — the
savings view's GOAL-CARD INTERNALS census at 390 (the badge chip row
+ the date/payment footer, the internals BEYOND the v51 F3 chrome
pin) + the queue's standing-check suggestion (a fresh VLM pair on
the /networth tablist). TDD-first, docs aligned, push via the SSH
wrapper. The workspace re-cloned at 664cfd7; the environment rebuilt
(npm install + .env from .env.example + db:push/db:seed + `npx
playwright install chromium` — the fresh-clone lacked the
per-version headless-shell-1243 binary; the first e2e run failed
21-wide on browserType.launch before the install).

**The v54 sweep** (`ref-v54.sh` + `clone-v54.sh`, READ-ONLY on the
reference): the goal-card internals at 390 — **BYTE-PARITY on every
chrome axis, PIN-ONLY**. The header row flex/gap 8/mb 4/center; the
dot 8×8/9999/rgb(59,126,161) (the savings TYPE accent on BOTH sites
— the reference colors its dot by TYPE, not classification; its
need-classified goal still carries the teal savings dot); the badge
row flex/wrap/gap 8/mb 12; every chip h 22/radius 6/pad 2px 10px/
12/600 with the 12×12 icons at mr 4 (the "monthly" chip w 78 and the
"active" chip w 63 on BOTH sites — the byte-parity width proof);
the footer flex/space-between/12/rgb(107,114,128)/h 16 + the date
span flex/gap 4/12 with the 12×12 calendar icon. The chip count
(3 vs 4 — the Recurring chip), the row height (22 vs 52), the
payment span, and the card height (200 vs 230) are the documented
DATA classes.

**The pin + the mutations.** F1 (`tests/e2e/items.spec.ts`, the new
"savings goal-card internals census at 390 (v54 — plan F1)"
describe): the first run FAILED — the badge-row finder required the
chips' computed display "inline-flex" but flex items are BLOCKIFIED
(the CSS spec: inline-flex → flex as a flex container's child) — the
finder fixed to accept "flex", GREEN. FIVE pin-sanity mutations
verified to FAIL then restored (the badge row gap-2→gap-4 [8→16];
the chip px-2.5→px-1.5 [pad 2px 10px→2px 6px]; the chip text-xs→
text-sm [h 22→26]; the footer text-xs→text-sm; the date span
gap-1→gap-2 [4→8]) — each with the standalone REBUILD as a SEPARATE
command (the v53 lesson).

**The standing checks (48th) + the VLM pair.** The reference's four
bugs ALL live (the toast-blocker, the sheet-trap via overlayCount 1,
the no-landmark, the 464 /networth overflow); the clone's mobile
navigation menu VERIFIED WORKING (R1 burger hit-test true + the
5-link sheet, R2 the Income nav closes AND navigates, R3 nav
landmark, R4 zero overflow at 390 on all five views); the data
census intact; the SEO pair live on both. The VLM pair on the
/networth tablist (the v53 F1 surface) AND the savings goal card
(the F1 surface): every flag DOM-verified (the active tab bg
byte-identical rgb(220,252,231) — a perception artifact; the Add
button's full "Add Asset" on both sites, scrollW 134 = clientW 134
— a small-text misread; the trend icon = the documented 464-overflow
width class; the rest = the seed-data/platform classes) — the pair
CLEAN per the v43 rule.

**The probe lessons (the v54 additions).** (1) A generic
justify-between + svg footer finder matches the card's HEADER row
first (the header also carries justify-between + the kebab svg; the
fs-16/h-48 reading is the tell-tale) — the footer locator is "the
LAST justify-between direct child WITHOUT an h4". (2) The chips'
inline-flex SOURCE class computes to "flex" as blockified flex
items. (3) The fresh-clone environment needs `npx playwright
install chromium` (the per-version headless-shell binary). (4) The
reference session EXPIRES between long eval gaps — re-login before
any follow-up census.

**The chain.** lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
248 e2e (141 + 108, two ordered chunks, both exit 0, zero failures)
· 35/35 smoke ✓. The 16 screenshots regenerated — ZERO byte-diffs
(the pin-only invariant). The docs aligned (AGENTS/CLAUDE/README/
SKILL Session 89 row + the 248 state/PAD v1.1.11/the probe README's
v54 section/session_128 + session_129/this worklog + the ledger
list). Commit + push to main via the SSH wrapper.

---

## Session 87 — Parity iteration v53: the /networth tablist's mobile pin + the calculator dialog's mobile pin (PIN-ONLY) + the orphaned-server/restoreRent execution lessons (2026-10-12)

**Goal:** the session-124 v53 queue's read-only members — the
/networth view's TABLIST census at 390 (the v50 pin walked the
family at 640 only) + the calculator dialog's 390 reflow (the
v45/v49 pins walked the family at 640 only). TDD-first, docs
aligned, commit + push via the SSH wrapper. (The workspace was
RE-CLONED — the sandbox had been reset; the environment rebuilt
from scratch.)

**What was done:** the baseline chain GREEN (108 unit / 245 e2e —
one not-found flake on the first run, passing standalone — / 35
smoke); the 47th standing checks both sites clean (the clone's
mobile menu verified working — R1 sheetLinks 5 via the v52-fixed
text-walk selector; the reference's four bugs ALL live — the
superset preserved); the code audit clean (the Tailwind v4
trap-log scan — both -mb-2 back buttons inside their converted
containers; the sitemap/robots/test-config/.env.example contracts
verified). The v53 sweep (ref-v53.sh + clone-v53.sh + the
clone-v53b.sh with-row follow-up — READ-ONLY on the reference):
the /networth TABLIST at 390 — byte-parity on every chrome axis,
the width family riding the reference's own documented 464-overflow
bug (its list 432 overhangs the viewport; the clone's superset fix
keeps the page in-bounds at 358/pageSW 390); the CALCULATOR at 390
— byte-parity on every axis with 1 row (the panel 358×413 on BOTH
sites — the h data-dependent, never pinned; the header 101; the
chip 32×40 + the close 29×36 — the identical flex-shrink squish;
the total card 310/#fff7f5; the row 310/pad 16/border-t; the Add
Item button 110×32). NO PRODUCTION GAP — the second consecutive
pin-only iteration. The remediation plan v53 written + validated.
The TDD execution: F1/F2 pins GREEN (F2's first run needed the
missing page.goto fix); the FIVE pin-sanity mutations all verified
FAILING (each with the standalone rebuild — the v53 lesson: the
rebuild and the test run as SEPARATE commands, the combined
one-liner raced the .next/standalone swap twice). **The full-chain
diagnosis — two hard-won lessons:** (1) a timed-out playwright run
leaves an ORPHANED webServer on :3100 that the next run REUSES
(reuseExistingServer) with a stale db handle after the
global-setup's re-seed — poisoning every data-driven assertion (the
45-failure 10.5s cascade; `ss -tlnp | grep :3100` + kill before
every full-chain run); (2) every calculator add/delete e2e MUST end
with restoreRent(page) — the line-item mutations recalculate the
parent's amount server-side, and the F2 test's missing restore
poisoned the later specs' dashboard arithmetic (fixed; the clean
diff: the two specs, ZERO production changes). The full chain: 108
unit / **246/246 chromium e2e (the 247 single-run equivalent, run
as two ordered chunks — 140 + 108, both exit 0)** / 35 smoke green.
The VLM pair on the calculator at 390 (the F2 surface): 5 flags
ALL DOM-verified (the close-button "boxed X" = the probe's
synthetic-click focus artifact — the :focus-visible-only keyboard
a11y superset, no ring in real mouse flows, the reference's
never-focused/outline-none close is its own a11y regression; the
rest = the data/platform classes). The 16 screenshots regenerated
(ZERO byte-diffs — the pin-only invariant; the dev db re-seeded
after the probe's add/delete left Rent recalculated). The docs
aligned (AGENTS / CLAUDE / README / PAD v1.1.10 / the SKILL Session
88 row + the 247 state / the probe README's v53 section with the
five execution lessons / session_125 + session_126 / this worklog +
the ledger list / the workspace worklog). Commit + push to main via
the SSH wrapper.

## Session 86 — Parity iteration v52: the details sheet's missing subcategory line (THE FIX — the fourth production-code change since v46) + the /income and /expenses 390 pins + the details-sheet internals pin + the standing script's burger-selector probe-infra fix (2026-10-12)

**Goal:** the session-121 v52 queue's read-only members — the
/expenses and /income mobile censuses at 390 (the item-card family
beyond the v51 savings pin) + the item-details 390 reflow (the v28
geometry pins walked the panel chrome only, never the summary's
content sequence). TDD-first, docs aligned, commit + push via the
SSH wrapper. (The workspace survived — a `git pull` fast-forward to
e71d357.)

**What was done:** the baseline chain GREEN (108 unit / 241 e2e /
35 smoke — clean on the FIRST run, no flakes — the v51 state
confirmed); the 46th standing checks (the reference's first run hit
a base44 COLD START — the re-run clean: all four bugs live, the
superset preserved; the clone side's R1 read sheetLinks:0 —
INVESTIGATED: the script's `button[aria-label="Open menu"]` is the
REFERENCE's DOM idiom, the clone's sr-only-named burger never
matched it and the `|| true` masked the failure; the mobile nav
itself verified WORKING via the eval flow — the sheet opens 5
links, the nav closes + navigates, the Escape closes; the stale
selector became the P1 scripts/ fix); the trap-log scan CLEAN (the
two -mb- back buttons both inside their converted containers); the
v52 probe pair found ONE REAL GAP — the details sheet's summary was
missing the SUBCATEGORY P (the reference renders FIVE summary
elements: the chip row, the H3 name, the P.text-lg 18/400/gray
subcategory — Rent "Apartment" / Salary "Main Job" — the amount;
the clone rendered four; the field was always on the model, the
card renders it, the edit dialog edits it, the details view never
wired it) + the /income and /expenses 390 censuses at BYTE-PARITY;
the remediation plan v52 written + validated; the TDD cycle (the
F1 RED run, the one-insert fix, GREEN — plus the chain-gate catch:
the new census code's `h1.closest()` null-safety, TS18047/TS2345
at `next build`'s tsc — the third application of the v51 lesson);
the five mutations verified biting (the P removed [the RED];
the chip's gradient; the filter's p-6->p-4 [BOTH F2+F3]; the
details header's py-4->py-2; the H1's text-3xl->text-2xl [BOTH]);
the P1 fix applied + re-verified (R1 "burger clicked" + sheetLinks
5); the full chain 245/245 e2e (clean first run) + 35/35 smoke;
the VLM pair on the /expenses view at 390 (4 flags, all the
documented seed-data/platform classes); the 16 screenshots
regenerated (ONE byte-diff: 16-item-details.png — the fix's visual
effect); the docs aligned (AGENTS/CLAUDE/README/PAD v1.1.9/SKILL
Session 87 + the 245 state/the probe README's v52 section/
session_122 + session_123/this worklog + the ledger list). Commit
+ push to main via the SSH wrapper.

**Artifacts:** `docs/remediation-plan-v52.md` (the plan), the
one-insert fix in `src/components/budget/item-details-dialog.tsx`
(+17 lines), four new e2e (item-details.spec.ts: the F1 subcategory
census + the F4 internals census; items.spec.ts: the F2 income +
F3 expenses 390 censuses — 241 to 245), the P1 fix in
`scripts/parity-probes/clone-stand47.sh`, the v52 probe pair +
the VLM script in `scripts/parity-probes/`, the regenerated
screenshot set (16), `docs/session_122.md` + `docs/session_123.md`,
the docs alignment (AGENTS/CLAUDE/README/PAD/SKILL/probe README).
Full chain: lint + typecheck + 108 unit + build + 245/245 e2e +
35/35 smoke — all green.

**Probe lessons:** the reference session EXPIRES between long eval
gaps (re-login via the eval); the viewport state does NOT survive a
session restart (re-apply 390 before any mobile census — the
"215.5px" desktop false reading); the reference's details sheet has
NO [role=dialog] (the no-landmark family — find it via the
`fixed inset-0 z-50` overlay); the summary is a TWO-LEVEL title
structure (the H3 + the subcategory P — walk the full subtree);
rounded-full computes 9999px on v3 vs 3.35544e+07px on v4 — pin the
CLASS, not the computed value.

## Session 85 — Parity iteration v51: the verify-email mode container's missing `.zb-auth-mode` conversion (THE FIX — the third production-code change since v46, completing the v50 F1's CLAIMED-but-never-applied third site) + four 390 pin surfaces (2026-10-12)

**Goal:** the session-118 v51 queue's read-only members (the savings
goal-card mobile census, the hero stats-card row's 390 reflow) + two
sibling sweep surfaces (the Budget Guidelines card at 390, the
quick-actions row at 390) — one of which resolved the deferred
verify-email queue item WITHOUT a reference write. TDD-first, docs
aligned, commit + push via the SSH wrapper. (The workspace survived
— a `git pull` fast-forward to 7a7f912.)

**What was done:** the baseline chain GREEN (108 unit / 236 e2e /
35 smoke — the v50 state confirmed); the 45th standing checks ALL
CLEAN (the reference's four bugs live — the superset preserved; the
data census read-only and intact; the SEO pair live on both); the
v51 probe pair (ref-v51.sh + clone-v51.sh, READ-ONLY on the
reference) measured FOUR pin-only surfaces at byte-parity (the
stats row: the three 210-tall cards @ 949/1183/1417 on both sites,
the full-page vertical rhythm identical; the savings view: the
goal card's chrome + the H1/filter/search — the card HEIGHT a data
class, the richer seed's 4-chip badge wrap; the Budget Guidelines
card: the BLOCK tiles stack + the byte-identical tinted pairs; the
quick-actions row: the three 90-tall cards @ 2751/2865/2979, the
40×40 circle, the trailing plus's class string read from the
reference's own DOM). A systematic Tailwind v4 trap-log audit (the
space-y × mt/mb-utility scan) then found THE REAL GAP: **the v50
F1's third-site conversion was CLAIMED but NEVER APPLIED** — the
v50 plan/commit/docs all stated the verify-email branch's container
was converted; the v50 diff landed the describing comment at
login-card.tsx:605-607 but NOT the line-608 class swap. Measured
via a fresh CLONE-side registration: the verify panel 16px short
(492 vs 508), the junction netGap −8 (the centered inner stack
overlapping the back button by 8px — the same v4 space-y × -mb-2
override). The remediation plan v51 written + validated; the TDD
cycle: RED CONFIRMED (the modeCls assertion fails on `space-y-4`)
→ the one-class fix (`zb-auth-mode`, no zb-sm6 — the verify
container carries no sm tier) → the first GREEN measured 528 not
508 (THE EMAIL-LENGTH FINDING: the "We've sent a 6-digit code to
{email}" block wraps per the address's length — the pin switched
to a fixed 21-char email) → GREEN (the panel 508 / the wrapper 556
/ the y 144 / the junction netGap 8). The F2/F4/F5 + F3 pins
written pin-only (one finder fix: the quick-action circle is a
SPAN in the clone, a DIV on the reference; one chain-gate catch:
Playwright does NOT typecheck — the TS2774 `querySelector &&`
check bit at `next build`, not at runtime). FIVE mutations verified
to FAIL (the zb-auth-mode removed [the RED run]; the stat card's
rounded-2xl→rounded-xl; the goal card's shadow removed; the Needs
tile's bg removed; the circle's w-10→w-8) — each with the standalone
REBUILD. The full chain: lint + typecheck + 108 unit + build +
**241/241 e2e (5.6m — the not-found flake family on the first two
runs, both 7/7 standalone, clean on the third)** + 35/35 smoke.
The VLM pair on the /savings view at 390: 3 flags, all the
documented seed-data classes (the v48 precedent's second
application). The 16 screenshots regenerated; the docs aligned
(AGENTS / CLAUDE / README / PAD v1.1.8 / the SKILL Session 86 row /
the probe README's v51 section / session_119 + session_120 / this
worklog + the ledger list). Commit + push to main via the SSH
wrapper.

**Outcome:** 108 unit / **241 e2e** / 35 smoke — all green; ONE
production fix (the third since v46) + four pin surfaces; the
doc-vs-code mismatch closed (the code now matches what the v50 docs
already claimed).

---

## Session 84 — Parity iteration v50: the auth states' panel heights (THE FIX — the second production-code change since v46) + the networth tablist's 640 chrome + the dashboard hero's 390 reflow (2026-10-12)

**Goal:** the session-115 v50 queue's three candidates (the auth
states' full 390 census — the surface that found ONE REAL DRIFT; the
networth tablist's chrome at 640; the dashboard hero's mobile
reflow at 390). TDD-first, docs aligned, commit + push via the SSH
wrapper. (The workspace was RESET — a fresh clone at 3f0202e; the
environment rebuilt: npm install, .env from .env.example, db:push +
db:seed, `npx playwright install chromium` — the fresh-sandbox
chromium download.)

- Baseline: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
  **232/232 e2e ✓ (5.4m)** · 35/35 smoke ✓. Audit clean (the same 5
  dev-only advisories, --omit=dev = 0; the secret scan clean; .env ≡
  .env.example).
- Standing checks all clean: mobile-nav R1–R4 (**44th** — Tailwind v4
  pins hold, both sites; the reference's sheet-trap re-verified with
  the PRECISE overlay census — the z-50 rgba(0,0,0,0.8) 390×844 scrim
  still open on /income after the nav click; the heuristic
  text-keyed detector read false again, the known artifact), data
  drift (44th — read-only, "1 items · $25,000" / "1 items ·
  $5000.00"), the SEO pair (both sites).
- **THE v50 SWEEP (three surfaces, both sites — ref-v50.sh +
  clone-v50.sh, READ-ONLY on the reference)**:
  - **The auth states at 390: ONE REAL DRIFT — THE FIX (the second
    production-code change since v46).** The sign-in state
    byte-identical (the v49 F1 contract holds: 730/682/57). The
    sign-up: the reference 470/422/187 vs the clone 454/406/195; the
    forgot: 358/310/243 vs 342/294/251 — the panels 16px SHORT at
    every viewport. The drift isolated to ONE junction (the form
    heights IDENTICAL): the reference's v3 space-y STACKS the back
    button's own -mb-2 with the heading's mt (the collapsed 16 +
    (-8) = the 8px net gap) while v4's zero-specificity margin-block-
    end lets the utility OVERRIDE the gap (the pre-fix heading
    overlapped the button by 8px). The forgot container's `sm:space-
    y-6` (24px at >=640) missing from the clone. The fix: the scoped
    `.zb-auth-mode` restore (the SPACE-Y V3 SEMANTICS family's third
    member — v9 G3 / v24 G2) with the container DROPPING the space-y
    class entirely (the first attempt's `> :not(:last-child)` zero at
    0-2-0 beat the -mb-2 utility at 0-1-0 and killed the 8px collapse
    — the measured 430, caught by the pin) + the `.zb-sm6` modifier +
    the verify-email branch's same-idiom container converted.
  - **The networth tablist at 640: BYTE-PARITY — PIN.** The list
    448/36/grid 220px 220px/#f5f5f5/8px/4px; the trigger pair's full
    chrome; the active green pair + the shadow-sm VISIBLE pair (the
    FULL reference string re-measured unsliced: 2 transparent leads +
    the pair; the clone: 4 leads + the pair — the accepted
    lead-divergence class); the 16×16 currentColor icons.
  - **The dashboard hero at 390: BYTE-PARITY — PIN.** The grid
    1-col/gap 24; the goal card 358×316@y 253 + the breakdown
    324@593 (the reference's 363 rides its own 395 overflow); the
    full internals; the chip pair — both sites' 20px svgs squish
    IDENTICALLY under the row's flex-shrink (a byte-shared
    width-pressure artifact).
- TDD: F1 written RED first (both tests failed against the pre-fix
  build) → the fix → **GREEN** (422/470/187 + 310/358/243 + the 640
  sm tier 24px). F2 + F3 pin-only (GREEN immediately; the F2 shadow
  assertion corrected from the sliced probe's 2-layer assumption to
  the unsliced 4-layer truth with the visible pair pinned). **Four
  new e2e, 232 → 236.**
- The mutation sanity (five, each with the standalone REBUILD): the
  zb-auth-mode removed (both F1 tests fail — the TDD RED); the -mb-2
  removed (the wrapper 478 = +8); the zb-sm6 removed (the 640
  sub-check: mt 24→16); the active-tab bg removed (F2); the hero
  track's h-3→h-2 (F3). All restored — the diff: globals.css +28 /
  login-card.tsx ±14.
- Full chain GREEN: lint · typecheck · 108 unit · build · **236/236
  e2e (5.4m — one flaky not-found metadata test on the first run,
  clean on the re-run)** · 35 smoke. The VLM pair on the login
  SIGN-UP state at 390 (THE FIXED SURFACE): the 4 flagged diffs ALL
  DOM-verified as noise (the panel y 187 / h 422 / the button
  294@x 48 IDENTICAL — the v43 misattribution lesson's fifth
  application). The 16 screenshots regenerated (7 byte-diffs). The
  docs aligned (AGENTS/CLAUDE/README/SKILL Session 85 row + the 236
  state/PAD v1.1.7/the probe README's v50 section/session_116 +
  session_117/the repo worklog Session 83→84 + the ledger list).
- Probe lessons: a stale agent-browser session hangs the next open
  (pkill + a session-file sweep before every run); a rebuild swaps
  .next/standalone under a running parity server (reboot after every
  build; the smoke script's pkill kills it too); slice-bounded
  censuses lie about multi-layer shadows (re-measure unsliced); the
  reference's sm: tiers are readable from its own DOM class list; a
  specificity collision inside a fix is caught by the pin (the
  RED→GREEN loop is the guard, the mutation series the proof).

**v51 queue suggestions:** the verify-email state's full panel
census (needs a reference registration — a write; only under an
explicit waiver), the forgot CONFIRMATION state's 390 census, the
hero's stat-card row reflow at 390, the savings view's goal-card
mobile census.

## Session 83 — Parity iteration v49: the login panel's mobile-only &nbsp; spacer (THE FIX — the first production-code change since v46) + the donut legend's mobile reflow + the calculator dialog's 640 chrome (2026-10-12)

**Goal:** the session-111 v49 queue's three candidates (the login
panel's mobile 390 census — the surface that found ONE REAL DRIFT;
the donut legend's mobile reflow at 390; the calculator dialog's 640
chrome). TDD-first, docs aligned, commit + push via the SSH wrapper.
(The workspace was INTACT — `git pull` 3f00e47→0bf89ce; the
environment survived from the v48 session.)

- Baseline: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
  **229/229 e2e ✓ (5.3m)** · 35/35 smoke ✓. Audit clean (the same 5
  dev-only advisories, --omit=dev = 0; the secret scan clean; .env ≡
  .env.example; the v48 diff = ZERO src/ changes — pin-only held).
- Standing checks all clean: mobile-nav R1–R4 (**43rd** — Tailwind v4
  pins hold, both sites; the reference's sheet-trap re-verified with
  the PRECISE overlay census — the z-50 rgba(0,0,0,0.8) scrim still
  open on /income after the nav; an earlier heuristic text-keyed
  detector had missed it), data drift (43rd — read-only, "1 items ·
  $25,000" / "1 items · $5000.00"), the SEO pair (both sites).
- **THE v49 SWEEP (three surfaces, both sites — ref-v49.sh +
  clone-v49.sh, READ-ONLY on the reference)**:
  - **The login panel at 390: ONE REAL DRIFT — THE FIX (the first
    production-code change since v46).** The reference's
    `w-full max-w-md` wrapper carries a mobile-only SECOND child —
    `<div class="mt-8 text-center text-xs text-slate-400
    sm:hidden"><p>&nbsp;</p></div>` (h 16, mt 32, rgb(148,163,184),
    empty content) — which lifts its card stack 24px above the
    geometric center (the panel y 57 / the wrapper 730; the pre-fix
    clone centered the panel ALONE at y 81 / 682). Verified on the
    sign-in AND sign-up states (a panel SIBLING — every auth state
    carries it); the 640 contract live (display none, the panel
    re-centers). The v12/v13 pins were desktop-measured; the v24
    mobile census walked the controls — first-time 390 measurement
    caught it. The fix: the spacer added to login-card.tsx (+14
    lines), the color as the `text-[#94a3b8]` hex (the v4 oklab
    trap).
  - **The donut legend at 390: BYTE-PARITY — PIN.** The container
    flex/column/gap 12/mt 24; the row 64/8px/12px/tinted; the dot
    16/4/classified; the leaves 16-500-forest / 16-700-classified /
    12-400-gray; the right-aligned values; the 16px icon (the
    reference's row w 313 rides its own 395 docSW overflow — the
    clone's 308 fits; the v44 F3 pinned only 1280).
  - **The calculator panel at 640: BYTE-PARITY — PIN.** w 608/x 16/
    radius 16/maxW 768px/maxH 816px (85vh)/bg white/overflow
    hidden/the 2xl VISIBLE layer (the clone's .zb-modal-panel emits
    it directly — no leads)/the 36×36 close/the header border-b
    1px rgb(229,231,227)/the centering invariant (the v45 F2b pinned
    only the widths).
- TDD: F1 RED first (the pre-fix run fails — the spacer absent),
  the fix, the rebuild, GREEN. F2 + F3 pin-only — 3/3 GREEN
  immediately. S1 six mutations, each with the standalone REBUILD:
  (a) the spacer removed → F1 fails (the TDD RED); (b) mt-8→mt-4 →
  F1 fails (730→722); (c) sm:hidden removed → the 640 sub-check
  fails; (d) the legend p-3→p-2 → F2 fails (64→56); (e) the
  zb-modal-panel shadow removed → F3 fails; (f) 85vh→90vh → F3
  fails (816→864). All restored — `git diff --stat src/` = ONE
  file, +14 lines.
- Full chain: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ ·
  **232/232 e2e ✓ (5.3m — 229→232)** · 35/35 smoke ✓. The VLM pair
  on the LOGIN page at 390 (THE FIXED SURFACE, a data-free form):
  **IDENTICAL — zero app flags** (the only flag the reference's own
  Base44 FAB). The 16 screenshots regenerated; the docs aligned
  (AGENTS/CLAUDE/README/SKILL Session 84 row + the 232 state/PAD
  v1.1.6/the probe README's v49 section/session_113 +
  session_114/the repo worklog Session 83 + the ledger list). Three
  new e2e, 229 to 232, 108/232/35 green.

---

## Session 82 — Parity iteration v48: the item-details sheet's shadow-2xl + the dialog-input focus composite at 390 + the empty-state full census — a PIN-ONLY iteration (2026-10-12)

**Goal:** the session-108 queue's first candidate (the details
panel's shadow — the regression net's seventh site) + the queue's
fourth (the dialog input's focus composite at 390 — the v47 F1's
mobile follow-up) + the queue's third (the empty-state census via
filter-to-zero). TDD-first, docs aligned, commit + push via the SSH
wrapper. (The workspace was RESET this session: git clone 3f00e47 →
npm install → db:push → db:seed; the playwright chromium-1243 build
fetched pre-emptively — the v46 lesson.)

- Baseline: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
  **226/226 e2e ✓ (5.3m)** · 35/35 smoke ✓. Audit clean (the same 5
  dev-only ESLint-chain advisories, --omit=dev = 0; the secret scan
  clean; .env ≡ .env.example; the v47 diff = tests/probes/docs only).
- Standing checks all clean: mobile-nav R1–R4 (**42nd** — Tailwind v4
  pins hold, both sites; the reference's toast-blocker measured via
  elementFromPoint at the burger's center, the sheet-trap via the
  live nav — the sheet + overlay still open on /income after the
  nav), data drift (42nd — reference read-only before + after: "1
  items · $25,000" networth / "1 items · $5,000.00" income, the
  frequency filter reset verified), the SEO pair (both sites).
- **THE v48 SWEEP (three surfaces, both sites — ref-v48.sh +
  clone-v48.sh, READ-ONLY on the reference)**:
  - **The item-details sheet's shadow-2xl (the net's SEVENTH site):
    every VISIBLE layer matches — PIN-ONLY.** The reference's panel
    (card-body click → details): 512×680 (the 85vh cap at 800) /
    radius 16 / 2 transparent leads + the v3 2xl layer
    `rgba(0,0,0,0.25) 0px 25px 50px -12px`; the overlay
    rgba(26,58,46,0.5) + the 36×36 close. The clone's panel (the
    Radix Content): 512×680 / 4 transparent leads + **the SAME 2xl
    visible layer** (v4's 5-slot, the accepted class) + the same
    overlay (the v7 G6 forest scrim, re-verified) + the same close
    button.
  - **The dialog-input focus composite at 390 (the v47 F1's mobile
    follow-up): the input w 310 on BOTH sites** with the same
    visible layers at rest and under REAL focus (the shadow-sm layer
    + the 1px ring + the persisting rest layer, the border
    unchanged) — the focus family is viewport-independent on both
    sites. PIN-ONLY.
  - **The empty-state full census (filter-to-zero): BYTE-PARITY.**
    The reference's /income frequency filter → One-time (its Salary
    is monthly — the read-only zero path; the filter reset verified
    by the after-census): the bare `py-16 text-center` 358×328
    block / the 64px icon at opacity 0.2, rgb(10,10,10), mb 16 / the
    H3 20-600-forest mb 8 / the P 16-gray mb 24 / the Add button h
    36, w 147, the 135deg gradient + the v3 BARE shadow pair. The
    clone: identical on every dimension. PIN-ONLY.
  - The queue's toast item RESOLVED as superset-only: the
    reference's toast never fired on the empty-form saves (measured
    twice — /income and /networth); its toasts are rare-path only
    (the v10/v33 notes); a reference toast census needs a REAL data
    mutation, against the v46 read-only discipline. Deferred.
- TDD: **3/3 pins GREEN immediately** (the first F1 draft's
  close-button finder missed the sr-only "Close" accessible name —
  fixed to the accessible-name idiom). S1 four mutations, each with
  the standalone REBUILD (the v47 lesson): (a) the panel's
  shadow-2xl removed → F1 fails; (b) the input's ring-1 removed →
  F2 fails (and v47's F1 — the shared class); (c) the icon mb-4→mb-2
  → F3 fails (h 328→320); (d) the .zb-btn-add shadow removed → F3
  fails. All restored — `git status src/` empty.
- Full chain: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ ·
  **229/229 e2e ✓ (5.3m — 226→229)** · 35/35 smoke ✓. The VLM pair
  on /savings at 1280: 4 flags, all DOM-verified as data classes
  (the richer seed's 2-card grid + the Recurring/payment-method rows
  + the avatar initial; the badge chrome byte-identical — the
  reference's need chip = the clone's CLASSIFICATION_BADGES need
  entry exactly). No chrome gaps.
- The 16 screenshots regenerated; the docs aligned (AGENTS/CLAUDE/
  README/SKILL Session 83 row + the 229 state/PAD v1.1.5/the probe
  README's v48 section/session_110 + session_111/the repo worklog
  Session 82 + the ledger list). Three new e2e, 226 to 229,
  108/229/35 green.

---

## Session 81 — Parity iteration v47: the dialog-input focus composite + the net-worth card mobile census + the mobile sheet's shadow-lg — a PIN-ONLY iteration (2026-10-11)

**Goal:** the session-101 queue's second candidate (the dialog inputs'
focus-state shadow composition) + the v46 follow-up (the net-worth
card's mobile census at 390) + the session-104 queue's sheet item (the
mobile sheet's shadow-lg). TDD-first, docs aligned, commit + push via
the SSH wrapper. (The workspace was RESET this session: git clone
9981c43 → npm install → db:push → db:seed; the playwright
chromium-1243 build fetched pre-emptively — the v46 session's lesson.)

- Baseline: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
  **223/223 e2e ✓ (5.2m)** · 35/35 smoke ✓. Audit clean (the same 5
  dev-only ESLint-chain advisories, --omit=dev = 0; the secret scan
  clean; .env ≡ .env.example; the v46 diff re-audited — ONE src file,
  the 12-line mb-2→mb-4 fix, matching the plan).
- Standing checks all clean: mobile-nav R1–R4 (**41st** — Tailwind v4
  pins hold, both sites; the reference's toast-blocker,
  sheet-trap, no-landmark, 395/464 overflows all still live — the
  toast-blocker measured via elementFromPoint at the burger's center,
  the sheet-trap via the live nav), data drift (41st — reference
  read-only, the v46 incident's restoration intact: "1 items ·
  $25,000"), the SEO pair (both sites).
- **THE v47 SWEEP (three surfaces, both sites — dlg-focus-v47.mjs +
  nw-mobcard-v47.mjs + sheet-chrome-v47.mjs + ref/clone-v47.sh)**:
  - **The dialog input's focus composite (session-101 queue #2): every
    VISIBLE layer matches — PIN-ONLY.** The reference composes (under
    REAL focus, :focus-visible matched) the white zero-spread lead +
    the 1px rgb(10,10,10) ring + the shadow-sm visible layer (3
    layers, v3); the clone's shadcn stack composes the same ring + the
    same shadow-sm layer with 4/3 transparent leads (v4's 5-slot
    construction — the accepted v10/v25/v45 class). The chrome
    identical (h 36/radius 6/pad 4px 12px/border 1px
    rgb(229,229,229)/bg transparent); the border UNCHANGED under focus
    on both sites; the outline (v3 transparent-2px vs v4 none) both
    invisible.
  - **The net-worth card's MOBILE census at 390: byte-parity post-v46
    — PIN-ONLY.** The reference's card h 194 (inside its 432-wide
    OVERFLOWING grid, docSW 464 — its documented bug); the clone's
    358×194 (the page fits, docSW 390) — **the card heights match
    exactly**; the value mb 16 both sites (the v46 fix survives the
    mobile reflow; the reference wraps in div.mb-4, the clone carries
    mb-4 on the P — the computed geometry is the contract); the facts
    12px rgb(107,114,128)/gap 16.
  - **The mobile sheet's shadow-lg at 390: the visible pair matches —
    PIN-ONLY.** Both sites: rgba(0,0,0,0.1) 0px 10px 15px -3px + 0px
    4px 6px -4px (the shadow-scale regression net's SIXTH site); the
    sheet 288×844/x 0/bg rgb(250,250,250); the overlay
    rgba(0,0,0,0.8) z 50.
  - Probe lessons: **a src/ mutation is invisible to the e2e suite
    until `npm run build` runs** (the first ring-1 mutation "passed"
    until the rebuild — the tests run against the standalone build);
    the reference's net-worth grid class carries no grid-cols-1 (key
    the shared finder on the md:/lg: pair); the reference's badges are
    leaf DIVs; the VLM's 3 mobile-/income flags all DOM-verified as
    data/platform classes (the richer seed's 4th Recurring badge
    wrapping in the byte-identical flex-wrap container + the
    reference's own Base44 FAB).
- TDD: the three pins GREEN immediately (pin-only); FOUR pin-sanity
  mutations verified to FAIL (the input's ring-1 removed; the input's
  shadow-sm removed; the value mb-4 reverted; the sheet's shadow-lg
  removed — each after the REBUILD). Full chain: **226/226 e2e
  (223→226)** · 108 unit · 35 smoke · lint + typecheck + build green;
  the VLM pair (mobile /income @390): 3 flags, all data/platform — no
  chrome gaps; the 16 screenshots regenerated.
- Docs: AGENTS/CLAUDE/README/SKILL/PAD (v1.1.4)/probe-README +
  session_107.md + session_108.md + this entry + the workspace worklog.
  Ship: commit + push to main via the SSH wrapper.

---

## Session 80 — Parity iteration v46: the net-worth card census + the value→facts spacing fix + the confirm-bar white-pill regression pin (2026-10-11)

**Goal:** the session-101/102 queue's first and third candidates — the
net-worth ASSET/LIABILITY card census at 1280 + the five-site
confirm-bar white-pill family's shadow-sm. TDD-first, docs aligned,
commit + push via the SSH wrapper. (The workspace was RESET this
session: git clone fb8d00f → npm install → db:push → db:seed; the
playwright chromium-1243 build fetched to match the lockfile-resolved
1.63.0.)

- Baseline: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
  **221/221 e2e ✓ (5.0m)** · 35/35 smoke ✓. Audit clean (the same 5
  dev-only ESLint-chain advisories, --omit=dev = 0; the secret scan
  clean; the v45 diff re-audited — PIN-ONLY, no src/ change).
- Standing checks all clean: mobile-nav R1–R4 (**40th** — Tailwind v4
  pins hold, both sites; the reference's toast-blocker, sheet-trap,
  no-landmark, 395 overflows all still live), data drift (40th —
  reference read-only), the SEO pair.
- **THE V46 SWEEP (both sites — nw-card-v46.mjs + confirm-pill-v46.mjs
  + the REAL-hover driver steps + vlm-compare-v46.mjs)**:
  - **THE ONE REAL GAP (the value→facts spacing):** the reference
    wraps its card value in `mb-4` (16px) while the clone's bare
    `mb-2` P rendered 8px — the card h 186 vs the reference's 194, the
    8px delta IS the gap (the census otherwise byte-identical). The
    item-card's own `mb-4` wrap the in-repo precedent — the net-worth
    cards were the one oversight. Fixed: `mb-2`→`mb-4` on both cards'
    value P.
  - **THE INCIDENT:** the reference's kebab menu → Delete click IS the
    delete (no confirm bar — the v18 superset-fix-#6 family,
    re-confirmed live): the probe deleted the reference's only asset;
    restored via its Add Asset form ("Savings Account" / bank account
    / 25000 / "Commonwealth Bank" / 2026-10-07) — the panel census
    re-read "1 items · $25,000" byte-identical to the before state.
  - The net-worth card census at 1280: the grid `md:grid-cols-2
    lg:grid-cols-3 gap-4` 960/3×309.328/gap 16, the card chrome
    byte-identical, **the REAL hover INERT on both sites** (the inline
    beats the hover:shadow-lg utility) while the kebab REVEALS.
  - The confirm-bar white-pill pin (the clone's superset chrome): the
    bar chrome + the Cancel pill's shadow-sm VISIBLE layer
    `rgba(0,0,0,0.05) 0px 1px 2px 0px` — the `--shadow-sm` theme pin's
    regression net (the five-site family).
  - Probe lessons: a Radix dropdown (and the reference's tabs) ignore
    synthetic `el.click()` — NATIVE clicks only; the reference's
    dialogs are plain `fixed inset-0` divs (no [role=dialog] — find by
    the Save-button text); the agent-browser Chrome daemons must be
    killed before a Playwright run (pthread_create exhaustion).
- TDD: F2 RED first (the value mb 8 ≠ 16 + the card h 186 ≠ 194 — the
  failure precisely on the gap), F3 GREEN immediately (pin-only), the
  fix → 19/19 networth spec. FOUR pin-sanity mutations verified to
  FAIL (the reverted mb-4; the pill's shadow-sm removed; the card
  inline 0.04→0.08; the kebab's group-hover reveal removed).
- Full chain: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ ·
  **223/223 e2e ✓ (221→223)** · 35/35 smoke ✓. The VLM pair on the
  /networth view at 1280: **IDENTICAL — zero flags** (the second
  fully-clean screening). 16 screenshots regenerated.
- Docs: AGENTS.md + CLAUDE.md + README + the SKILL doc (Session 81) +
  the PAD (v1.1.3) + the probe README (the incident + five lessons) +
  session_104.md + session_105.md + this worklog.
- Ship: commit + push to main via the SSH wrapper.

---

## Session 79 — Parity iteration v45: the shadow-scale sweep + the items-view card grid census + the calculator row hover — a PIN-ONLY iteration (2026-10-11)

**Goal:** the session-99/100 queue — the items-view card grid at 1280,
the calculator line-item row's hover, the category-level animation
pin. TDD-first, docs aligned, commit + push via the SSH wrapper. (The
workspace SURVIVED the session break: git pull fast-forwarded
31b275d → e327b57, the environment intact.)

- Baseline: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
  **214/214 e2e ✓ (4.9m, the FIRST run)** · 35/35 smoke ✓. Audit clean
  (the same 5 dev-only ESLint-chain advisories, the secret scan clean,
  the tree clean, the v44 diff re-audited).
- Standing checks all clean: mobile-nav R1–R4 (**39th** — Tailwind v4
  pins hold, both sites; the reference's toast-blocker, sheet-trap,
  no-landmark, 395 overflows all still live), data drift (39th —
  reference read-only, verified before + after), the SEO pair.
- **THE V45 SWEEP (both sites — items-card-v45.mjs + calc-row-v45.mjs +
  the REAL-hover driver steps + vlm-compare-v45.mjs)**:
  - **THE SHADOW-SCALE DISCOVERY:** a SYSTEMIC v3↔v4 divergence in the
    computed box-shadow composition — every live `shadow-*` utility's
    VISIBLE layers match on BOTH sites (the `--shadow-sm` theme pin is
    load-bearing for the small end: v4 RENAMED the scale, its native
    shadow-sm = v3's "shadow"; the pin restores `0 1px 2px 0
    rgb(0 0 0 / 0.05)` — measured matching) while the LEAD layers
    diverge by construction (v4's 5-slot composition emits 4 transparent
    leads vs v3's 2 — invisible, the accepted v10/v25 class). The
    md/lg/xl/2xl numerics were NOT renamed and were UNPINNED — v45
    pins the md/lg/sm/2xl sites as the regression net (a future
    Tailwind upgrade that changes the scale numerics fails the suite).
    Surveyed: the calculator row's hover (md), the action buttons' rest
    (md), the quick-action card's hover (lg), the login panel (2xl),
    the details sheet (2xl), the Google button's hover (sm), the slate
    buttons (sm), the dialog inputs (sm), the white pills (sm), the
    mobile sheet (lg), the login logo (lg/xl), the .zb-modal-panel
    (explicit — visible ✓) + the inert-by-construction family (the
    item/net-worth cards' inline boxShadow beats hover:shadow-lg on
    BOTH sites — the v29 family).
  - **The items-view card census at 1280: BYTE-IDENTICAL** — the grid
    960 (the rail 256 + the content column 1024 − the p-8 64 — the
    SAME arithmetic on both sites), 3 cols × 309.328, gap 16; the card
    309/pad 20/radius 12/border/`rgba(0, 0, 0, 0.04) 0px 2px 8px 0px`
    (Chrome normalizes the 3-value inline and the reference's to the
    SAME string)/transition all 0.2s; the title row gap 8/dot 8×8/
    16-600; the income kebab 36×36 opacity 0; the expense action row
    top 12/right 12/gap 8/btn 32/padX 12/12px; the card's REAL hover
    INERT on BOTH sites while the action row REVEALS. Heights 230 vs
    200 = DATA (the notes rows).
  - **The calculator row census + REAL hover: BYTE-IDENTICAL** — the
    panel 768@1280/608@640, the row 720/560, pad 16/radius 12/border/
    rest-shadow none/transition all 0.15s; the action pair opacity 0/
    32px; under a REAL hover the shadow-md visible layers + the action
    reveal on both sites. (The reference's RENT calculator is the only
    one of its four expense cards with line items; the clone's row
    API-created + restored — the calculator rule sets the parent to the
    line-items SUM, so the restore PATCHes the parent back.)
  - **The category-level band animation works** (the v44 Collapse at
    the nested level): 441→453→…→495 + the reverse — in-flight frames
    both directions, now pinned.
- **The seven e2e (TDD — pin-only, all GREEN against the unchanged
  build; the F2 pair needed its describe-level beforeEach, the one
  test-layer fix; the build's typecheck caught a TS union in the F3a
  evaluate's early return)**: F1a/F1b the items-card grid census +
  the REAL-hover inert + the action reveal + the action buttons' rest
  shadow-md; F2a/F2b the calculator row census + the hover shadow-md +
  the 640 dialog; F3a the category-level animation + F3b the
  quick-action hover shadow-lg; F4 the login shadow-scale regression
  pins (slate sm + panel 2xl + Google hover sm).
- **Five pin-sanity mutations verified to FAIL**: the card inline
  0.04→0.08; the grid gap-4→gap-6; the row hover:shadow-md removed;
  the quick-action hover:shadow-lg removed; the slate shadow-sm
  removed. All restored → GREEN.
- The full chain: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
  **221/221 e2e ✓ (5.2m — 214 → 221)** · 35/35 smoke ✓. The 16
  screenshots regenerated. The VLM pair (the /income items-view at
  1280): **IDENTICAL, zero flags — the first fully-clean screening
  since the pair began.**
- Docs aligned: AGENTS.md (the v45 paragraph), CLAUDE.md (221 + four
  v45 insertions), README (the v45 row + the counts), the SKILL doc
  (the Session 80 row + the state line + the command + the three-tier
  row), the PAD (the v1.1.2 revision block), the probe README (the
  v45 section — six lessons), session_101 + session_102, the repo
  worklog (this entry), the workspace worklog.

---
## Session 78 — Parity iteration v44: the drill-down expansion ANIMATION + the chevron GLYPH swap + the 390/1280 census + the donut-legend census — the first production-code change since v43 (2026-10-11)

**Goal:** the session-95/96/97 queue — the drill-down's EXPANDED-state
census at the remaining viewports (390/1280), the donut legend's
geometry/interaction states, and what the sweep finds. TDD-first, docs
aligned, commit + push via the SSH wrapper. (The sandbox had been
reset — a fresh clone + full environment rebuild.)

- Baseline rebuilt: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
  **209/209 e2e ✓ (4.6m)** · 35/35 smoke ✓. Audit clean (the same 5
  dev-only ESLint-chain advisories, the secret scan clean, .env ≡
  .env.example, the v43 diff re-audited).
- Standing checks all clean: mobile-nav R1–R4 (**38th** — Tailwind v4
  pins hold, both sites; the reference's toast-blocker, sheet-trap,
  no-landmark, and 395 overflows all still live), data drift (38th —
  reference read-only, verified before + after), the SEO pair.
- **THE V44 SWEEP (both sites, 390×844 AND 1280×800 — exp-vp-v44.mjs +
  legend-v44.mjs + collapse-ref-v44.mjs + band-mount-v44.mjs)**:
  - **F1 — the drill-down expansion ANIMATES on the reference** (~200ms
    height+opacity tween, both levels, both directions — mid-collapse
    the band's INLINE height reads 25.5455px: a per-frame JS tween, the
    end state height:auto/opacity:1, the section band unmounts after
    the collapse animation) **while the clone mounted/unmounted
    instantly** (324→441 at the first sample, zero in-flight frames).
    Fixed: the `Collapse` wrapper — the grid 0fr↔1f technique +
    @starting-style for the entry + the onTransitionEnd delayed
    unmount (the collapsed DOM returns to EXACTLY the pre-fix node
    tree — the accordion count-0 pins hold; the mount flip via the
    adjust-state-during-render pattern with a prev-value STATE, not a
    ref — react-hooks/refs forbids ref access during render).
  - **F4 — the chevron GLYPH swap** (found by the standing VLM pair,
    DOM-verified REAL — chev-glyph-v44.mjs): lucide-chevron-down
    collapsed ↔ lucide-chevron-up expanded at BOTH levels, rotate:
    none at every state. The v43 "static" finding was
    correct-but-incomplete — **the flip is the ICON, not the transform:
    a computed-style census cannot see a glyph swap; read the svg's
    class**. Fixed: conditional glyph render at both levels.
  - **F2 — the 390/1280 census (pin-only):** the chrome byte-identical;
    the 1280 section label's 2-line WRAP (labelH 40, row 56 — on BOTH
    sites: the v42 collapsed census's 56px row explained, width-driven);
    the mobile indentation identical (the inner ml 40px/mt 8px); the
    clone's sw 390 fully expanded (the superset — the reference reads
    395, its own overflow).
  - **F3 — the donut legend census (pin-only, the queue item
    resolved):** the geometry byte-identical (h 64/pad 12/radius 8/the
    label-amount-pct fonts/the 16×16 dot/gap 12/mt 24) and the REAL
    hover INERT on both sites — no interaction states exist to match.
- **The five e2e (TDD: the animation + glyph tests RED pre-fix, the
  three census tests pinning correct chrome)**: the expansion-animation
  pin (in-flight samples both directions + the band's opacity ease +
  the end states + the unmount), the 390 census, the 1280 census, the
  legend census, the glyph-swap pin. GREEN first-run after the fixes.
- **Five pin-sanity mutations verified to FAIL**: the zeroed duration;
  the removed @starting-style; the legend p-3→p-4 (64→72); the sub-row
  py-1→py-2; the reverted glyph swap. All restored → GREEN.
- The full chain: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
  **214/214 e2e ✓ (4.9m — 209 → 214)** · 35/35 smoke ✓. The 16
  screenshots regenerated (the drill-down shot shows the swapped
  chevron-up glyph). The VLM pair: the glyph flag was REAL (the F4 fix
  — the screening earns its keep); the icon/bold flags were
  screenshot-scale misreads, DOM-refuted.
- Docs aligned: AGENTS.md (the v44 paragraph), CLAUDE.md (214 + the
  v44 entry), README (the v44 row + the stale 206 testing-count fixed),
  the SKILL doc (five count sites + the Session 79 row), the PAD (the
  v1.1.1 revision block), the probe README (the v44 section), session_98
  + session_99, the repo worklog (this entry), the workspace worklog.

---
## Session 77 — Parity iteration v43: the drill-down EXPANDED-state census + the static-chevron and hover-rgb fixes — the first production-code change since v42 (2026-10-11)

**Goal:** refresh the workspace (git pull — intact this session), re-run
the baseline chain, sweep the session-92/93 queue (the drill-down
EXPANDED-state census + the summary card's hover/interaction states),
pin what the measurement finds, TDD-first, docs aligned (including the
D-series doc nits from the core-doc review), commit + push via the SSH
wrapper.

- Workspace SURVIVED the session break: git pull fast-forwarded
  288cfea → d55299f; the environment intact. Baseline: lint ✓ ·
  typecheck ✓ · 108/108 unit ✓ · build ✓ · **206/206 e2e ✓ (4.7m, the
  FIRST run, zero flakes)** · 35/35 smoke ✓. Audit clean (the same 5
  dev-only braces advisories, the secret scan clean, .env =
  .env.example, the v42 src diff re-audited).
- Standing checks all clean: mobile-nav R1–R4 (**37th** — Tailwind v4
  pins hold, both sites; the reference's toast-blocker, sheet-trap,
  no-landmark, and 395 overflows all still live), data drift (37th —
  reference read-only, verified before + after), the SEO pair.
- **THE V43 SURFACE — the drill-down's expanded bands measured live on
  BOTH sites at 640×960 (exp-census-v43.mjs + exp-detail-v43.mjs +
  exp-rotate-v43.mjs + hover-v43.mjs)**:
  - The per-row chrome BYTE-IDENTICAL at every level (the section
    48/8px/-8px/8px radius/14px chevron, the category 28/6-12px/inline
    rgb(249,250,251)/6×6 dot, the sub 24/4-8px/rgb(250,250,250)/4×4 dot
    at 0.6, the item 24/4-8px/12px/rgb(156,163,175)/2×2 dot at 0.4/120px
    truncate, the footer 29/6-12px/border-t); the arithmetic
    324 → 441 → 495 (the +36 vs the reference = DATA: 2 categories
    vs 1); sw 640 fully expanded.
  - **THE PARITY GAPS (the first production-code change since v42)**:
    (F1) the chevrons ROTATE on the clone (v4 `rotate: 180deg`, 0.15s)
    and are STATIC on the reference (rotate: none, transition "all" 0s
    at both levels — **Tailwind v4's rotate-* emits the `rotate`
    PROPERTY, not `transform`; the transform: none readings on both
    sites were meaningless — the v4 property trap**); (F2) the
    section-row hover renders **lab(98.2596 -0.247031 -0.706708)** (the
    v4 named palette, LIVE: the section button carries no inline bg)
    where the reference computes rgb(249, 250, 251). Fixed: both
    chevrons stripped (aria-expanded kept — the v32 superset) +
    `hover:bg-[#f9fafb]`.
  - The category rows' hover INERT on both sites (the inline bg
    overrides — v29, DOM-identical). **The queue's summary-card item
    RESOLVED: the net-worth gradient card is STATIC on both** (the same
    gradient/shadow/cursor under a REAL hover — no interaction states
    exist to match).
- **F3/F4 — the three census e2e** (dashboard.spec.ts): the expanded
  band census (the per-row chrome + the arithmetic 324/441/495 + sw
  640) + the STATIC-chevron pin (rotate: none at both levels, fresh
  post-expansion queries) + the hover rgb pin (a REAL .hover() — the
  exact-name locator disambiguated from the Total Income stat card).
  TDD: written FIRST, run RED (F1 at "180deg" ≠ "none"; F2 at lab ≠
  rgb), the fixes applied, GREEN on the first run.
- **Three pin-sanity mutations verified to FAIL**: the restored
  rotate-180 → the rotate pin fails; the reverted hover hex → the rgb
  pin fails; the sub-row py-1 → py-2 → the census pin fails (503 ≠
  495). All restored → GREEN.
- The full chain: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
  **209/209 e2e ✓ (4.8m — 206 → 209)** · 35/35 smoke ✓. The 16
  screenshots regenerated. The VLM pair clean (all flags in the known
  classes — the reference's own Base44 badge was MISATTRIBUTED to the
  clone by the VLM, DOM-verified before it counted).
- **The D-series doc alignment (the core-doc review's seven nits)**:
  AGENTS.md's "Six"→"Seven" superset count + its v40/v41/v42/v43
  paragraph order normalized newest-last; the SKILL doc's :3333 →
  :3100 port + four stale 87/34/30 count sites; README's "21 handlers
  (13 files)" → "23 (15)" + the v36/v37 session labels reconciled to
  the SKILL doc's table; the PAD's v1.1.0 revision block (the counts,
  the 23/15 surface, the four-state login, the SEO routes, the
  item-details sheet, the a11y gate, the verification lib, the seven
  supersets). Docs aligned (the probe README's v43 section, README's
  v43 row + the 209 counts, CLAUDE.md's entry, AGENTS.md's v43
  paragraph, the SKILL doc's state + Session 78 row, session_95.md,
  session_96.md, the repo worklog, the workspace worklog).

## Session 76 — Parity iteration v42: the mid-viewport census of the five routes + the breakdown card's single-divider fix — the first production-code change since v41 (2026-10-11)

**Goal:** refresh the workspace (git pull — intact this session), re-run
the baseline chain, sweep the session-90/91 queue (the MID viewport
640×960 census of the five non-networth routes — the v41 lesson applied
to the remaining route set), pin what the measurement finds, TDD-first,
docs aligned, commit + push via the SSH wrapper.

- Workspace SURVIVED the session break: git pull fast-forwarded
  3f89e53 → d5068c8; the environment intact (node_modules, .env with
  `DATABASE_URL="file:../db/custom.db"`, db/custom.db + db/e2e.db at
  the repo root, playwright chromium). Baseline: lint ✓ · typecheck ✓
  · 108/108 unit ✓ · build ✓ · **203/203 e2e ✓ (4.7m, the FIRST run,
  zero flakes)**. Audit clean (the same 5 dev-only braces advisories,
  the secret scan clean, .env = .env.example, the v41 src diff
  re-audited — exactly the documented 3-file changeset).
- Standing checks all clean: mobile-nav R1–R4 (**36th** — Tailwind v4
  pins hold, both sites; the reference's toast-blocker, sheet-trap,
  no-landmark, and 395 overflows all still live), data drift (36th —
  reference read-only, verified before + after), the SEO pair
  (robots/sitemap live on both), the reference's mobile sheet
  re-measured (still the plain fixed div).
- **THE V42 SURFACE — the five routes measured live on BOTH sites at
  640×960 (mid-census-v42.mjs)**:
  - **The 32px rhythm HOLDS on all five routes** (gapRowToFirst === 32
    everywhere — the v20 G1 pin's class extended to the mid viewport);
    the header 61, the h1 30px/36, the cap 608, sw 640, the items-view
    structure identical (the filter card block mb-24, the 1-col grid
    gap-16).
  - **THE PARITY GAP (the first production-code change since v41)**:
    the dashboard's NetZeroBreakdownCard ran +13px taller at BOTH
    viewports (640: 337 vs 324; 1280: 377 vs 364) — attributed
    band-by-band: the goalCard byte-identical (316, bands 48/48/108,
    donut 558×300), the row heights identical (56/64/64 at 1280 —
    width-driven wrap) — **the delta was ONE EXTRA DIVIDER: the clone
    rendered TWO (Income|Savings AND Savings|Expenses), the reference
    ONE (Income|Savings only — the app's ONE rule grouped: [Income] |
    [Savings, Expenses] | border-t | [Net Balance])**. The tail check:
    lastBand mb=0 on both sites, scrollH 3029 vs 3042 — exactly the
    +13, the divider alone. **Fixed: `{i === 1 && <Divider />}`.**
- **F2/F3 — the three census e2e** (dashboard.spec.ts): the breakdown
  band census at 1280 (the 5-band stack [56, 1, 64, 64, 45], the
  single divider, the 364 card) + the hero grid census at 640
  (goalCard 316, breakdownCard 324@y=569, hero 664, secondBand 925,
  thirdBand 1635, scrollH 3029) + the five-route mid-viewport census
  (the common rhythm + the route-class branches). TDD: written FIRST,
  run RED (all three failed at exactly the expected pins), the fix
  applied, GREEN on the first run.
- **Three pin-sanity mutations verified to FAIL**: the reverted divider
  condition → the band-count pin fails (6 ≠ 5); the items-view mb-8 →
  mb-6 → the /income rhythm pin fails; the dashboard mb-8 → mb-6 →
  the / rhythm pin fails. All restored → GREEN.
- The full chain: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
  **206/206 e2e ✓ (4.7m — 203 → 206)** · 35/35 smoke ✓. The 16
  screenshots regenerated. The VLM pair clean (all flags in the known
  classes). Docs aligned (the probe README's v42 section, README's
  v42 row + the 206 counts, CLAUDE.md's entries, AGENTS.md's v42
  paragraph, the SKILL doc's state + Session 77 row, session_92.md,
  the repo worklog, the workspace worklog).

## Session 75 — Parity iteration v41: the net-worth summary card's viewport census + the vertical-rhythm fix — the first production-code change since v38 (2026-10-11)

**Goal:** refresh the workspace (git pull — intact this session), re-run
the baseline chain, sweep the session-86/87 queue (the net-worth
summary card's gradient chip at the savings-class viewports + the
a11y gate's sheet-open extension to the remaining five routes), pin
what the measurement finds, TDD-first, docs aligned, commit + push
via the SSH wrapper.

- Workspace SURVIVED the session break: git pull fast-forwarded
  5b0a6f3 → 009453c; the environment intact (node_modules, .env with
  `DATABASE_URL="file:../db/custom.db"`, db/custom.db + db/e2e.db at
  the repo root, playwright chromium). Baseline: lint ✓ · typecheck ✓
  · 108/108 unit ✓ · build ✓ · **196/196 e2e ✓ (4.5m, the FIRST run,
  zero flakes)**. Audit clean (the same 5 dev-only braces advisories,
  secret scan clean, `.env` = `.env.example`). One process discovery:
  this sandbox reaps background processes between tool calls — long
  jobs run inside ONE invocation (`with-server.sh`); the agent-browser
  daemon survives.
- Standing checks all clean: mobile-nav R1–R4 (**35th** — Tailwind v4
  pins hold, both sites; the reference's toast-blocker, sheet-trap,
  no-landmark, and 395 overflows all still live), data drift (35th —
  reference read-only, verified before + after), the SEO pair
  (robots/sitemap live on both), the reference's mobile sheet
  re-measured (still the plain fixed div).
- **THE V41 SURFACE — the summary card's viewport census, measured
  live on BOTH sites at 390×844, 640×960 AND 1280×800**
  (nw-summary-v41.mjs + nw-yoffset-v41.mjs + nw-below-v41.mjs):
  - **At the MID viewport (640 — the unmeasured savings-class class):
    FULL geometry parity** — the 608×333 card (p-8, radius 16, the
    forest→lime gradient, the shadow), the 48px/700 figure, the
    64×64 white/20% gradient chip at x=528 (9999px, the 32px icon),
    the 264×2 stats grid (16px gap, 84px cells), the 18px ratio, the
    48@x=16 header chip, the 256/0.1 overlay, the 448×36 tabs, the
    144 tabs→grid gap, sw=vw on both.
  - **THE PARITY GAP (the first production-code change since v38)**:
    the net-worth page's section rhythm ran `mb-6` (24px) where the
    reference runs `mb-8` (32px) at BOTH gaps — the header row→card
    and the card→tablist — 8px offsets at every viewport. The
    y-offset probe attributed the delta in ONE run (the stack
    above/below matches byte-for-byte); the items-view control
    (items-rhythm-v41.mjs on /income, identical both sites) proved
    the net-worth was the ONE outlier. **Fixed: the two `mb-6` →
    `mb-8` in net-worth-view.tsx.**
  - **The mobile superset pair re-measured at the card level**: the
    reference's card is 432px wide at 390 (74px overflow, sw=464, its
    chip 26px offscreen at x=352, its grid a fixed 2-col, its figure
    a fixed 48px); the clone's fits (358 card, 24px figure, 1-col
    grid, chip inside, sw=390) with byte-identical chrome.
- **F2/F3 — the two census e2e** (networth.spec.ts): the 640 census
  (the full band census + **the two rhythm pins**: card.y −
  chipRow.bottom === 32, tablist.y − card.bottom === 32) + the 390
  superset census (the fits-everywhere pair). TDD: written FIRST, run
  RED (the rhythm pin failed 24 ≠ 32), the fix applied, GREEN.
- **F4 — the a11y sheet-open structural pins extended to the
  remaining five routes** (a11y.spec.ts: /dashboard /income /expenses
  /savings /networth — the v39 test covered `/` only; the same
  dialog/labelledby/nav/five-links/Escape contract; the full axe scan
  stays on `/` — the sheet's DOM contribution is route-independent).
  GREEN on the first run.
- **Four pin-sanity mutations verified to FAIL**: the reverted mb-8 →
  the rhythm pin fails; the stripped sm:text-5xl → the 48px pin
  fails; the fixed 2-col grid → the 1-col pin fails; the stripped
  DialogTitle → all five route tests fail. All restored → GREEN.
- The full chain: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
  **203/203 e2e ✓ (4.7m — 196 → 203)** · 35/35 smoke ✓. The 16
  screenshots regenerated. Docs aligned (the probe README's v41
  section, README's v41 row + the 203 counts, CLAUDE.md's entries,
  AGENTS.md's v41 paragraph, the SKILL doc's state + Session 76 row,
  session_89.md, the repo worklog, the workspace worklog).

## Session 74 — Parity iteration v40: the dashboard's Tab-order focus walk — the interactive stat-card superset pinned, zero production-code changes (2026-10-11)

**Goal:** refresh the workspace (git pull — intact this session), re-run
the baseline chain, sweep the session-84/85 queue (the dashboard
quick-action focus walk — the session-78 queue's LAST unmeasured
surface), pin what the walk finds, TDD-first, docs aligned, commit +
push via the SSH wrapper.

- Workspace SURVIVED the session break: git pull fast-forwarded
  6e75f2b → 8a7a3b4; the environment intact (node_modules, .env with
  `DATABASE_URL="file:../db/custom.db"`, db/custom.db + db/e2e.db at
  the repo root, playwright chromium). Baseline: lint ✓ · typecheck ✓
  · 108/108 unit ✓ · build ✓ · **195/195 e2e ✓ (4.5m, the FIRST run,
  zero flakes)** · 35/35 smoke ✓. Audit clean (the same 5 dev-only
  braces advisories, secret scan clean, `.env` = `.env.example`).
- Standing checks all clean: mobile-nav R1–R4 (**34th** — Tailwind v4
  pins hold, both sites; the reference's toast-blocker, sheet-trap,
  no-landmark, and 395 overflows all still live), data drift (34th —
  reference read-only, verified before + after), the SEO pair
  (robots/sitemap live on both; the reference's capitalized app-route
  URLs still documented).
- **THE DASHBOARD'S TAB-ORDER FOCUS WALK (the session-78 queue's last
  unmeasured surface) — measured live on BOTH sites and pinned**:
  - The measurement (`tabwalk-v36.sh` + `focus-census-v40.mjs` +
    `stat-card-chain-v40.mjs` + `donut-focused-dump-v40.mjs`): the
    reference's cycle is 14 focusable stops — the five nav links →
    the Add Item header button → the three NetZero-breakdown
    stat-row buttons → the donut's `g.recharts-pie` (tabindex=0) →
    the three quick-action cards → the Base44 "Close badge"
    (platform chrome). The clone's is the SAME walk minus the badge
    **plus the three interactive stat cards** (`div[role=button]`
    tabindex=0 — stops 10–12).
  - **THE HEADLINE FUNCTIONAL SUPERSET**: the reference's big
    304×210 stat cards are **INERT divs** (no role, no tabindex, no
    handler — dead UI; only the text-ancestor chain probe separates
    them from the stat rows, which ARE real buttons on both sites).
    The clone's are keyboard-focusable and Enter/Space-activated
    navigation cards.
  - The donut stop matches structurally on both sites (the pie layer
    tabindex=0, the sector paths tabindex=-1 roving, the inert svg
    surface — the v31 replication confirmed at the walk level; the
    reference's g carries its label texts inside, the clone's in a
    separate recharts-3 layer — library internals, VLM-clean).
  - The census test (`tests/e2e/dashboard.spec.ts`, 1 new e2e): the
    16 REAL-Tab stops with tag + role + name + tabindex + the
    geometry bands (nav x=20 w=215 pitch 40; the stat-row buttons
    x=961 w=254; the stat cards [288/616/944, 304×210]) + the wrap +
    the superset activation pair (Enter on the focused Total Income
    card → /income; Space on Total Savings → /savings). GREEN on the
    first run.
  - Both pin-sanity mutations verified to FAIL: (a) the stripped
    role+tabIndex drops the stat-card stops out of the walk (the Tab
    skips straight to the donut g); (b) the removed Enter/Space
    handler fails the activation pin — the mutation literally
    reproduces the reference's dead-UI behavior. Both restored →
    GREEN. Zero production-code changes (`git diff src/` empty).
- The VLM pair (the desktop dashboard, 1280×800): VERDICT DIFFERENT
  with ALL THREE flags explained (the clone's Dashboard active
  highlight = superset fix #3; the allocation-bar length = the
  different demo data; the avatar letter = the different demo users).
- Probe lessons: the clean focusable census must filter
  [tabindex]=-1 AND zero-rect elements (recharts' hidden zIndex
  layers); the reference's stat-card inertness is only visible via
  the TEXT-ANCESTOR CHAIN; `document.querySelector('header button')`
  matches the display:none MobileTopbar burger first — query by text
  when the target has no semantic landmark; the tabwalk's 450ms
  settles leave the page scrolled — assert only scroll-independent
  bands (x/w/h); the reference's own stat-row column gaps are
  inconsistent (25px then 12px) while the clone's are a consistent
  25px — a 13px band drift below that point, VLM-clean.
- The full chain re-run: **108/196/35** (195 → 196: the census test).
  The 16 screenshots regenerated. Docs aligned: README (the 196
  counts + the v40 row), CLAUDE.md (the census entry), AGENTS.md
  (the v40 paragraph), the SKILL doc (Session 75 row), session_86.md,
  the probe README (the v40 section), this worklog.

---

## Session 73 — Parity iteration v39: the a11y gate's MOBILE extension — the 390×844 sheet-state scan, zero production-code changes (2026-10-11)

**Goal:** re-clone the reset workspace, rebuild the environment, re-run
the baseline chain, sweep the session-80/81 queue (the a11y gate's
MOBILE extension — the 390×844 scan of the sheet-open state), fix what
the DOM finds, TDD-first, docs aligned, commit + push via the SSH
wrapper.

- Workspace RE-CLONED fresh (`a2d5381`; the old one had been reset).
  Environment rebuilt: npm install (495 packages), `cp .env.example
  .env` (`DATABASE_URL="file:../db/custom.db"`), db:push + db:seed,
  playwright chromium. Baseline: the first full e2e run flagged ONE
  flake (not-found Go Home — a toBeVisible at 11.1s; passed in
  isolation AND the full re-run — a first-run-after-rebuild warm-up
  artifact); the re-run **187/187** + lint + typecheck + 108/108 unit
  + build + 35/35 smoke. Audit clean (the same 5 dev-only braces
  advisories, secret scan clean, `.env.example` current).
- Standing checks all clean: mobile-nav R1–R4 (**33rd** — Tailwind v4
  pins hold, both sites; the reference's toast-blocker, sheet-trap,
  no-landmark, and 395 overflows all still live), data drift (33rd —
  reference read-only, verified before + after), the SEO pair
  (robots/sitemap live on both; the reference's capitalized app-route
  URLs still documented).
- **THE A11Y GATE'S MOBILE EXTENSION (the v38 queue's third item) —
  shipped**:
  - The exploratory scan (`a11y-scan-v39.mjs`, the 390×844
    isMobile+hasTouch emulation, BOTH sites + the per-node color
    enumeration `axe-detail-v39.mjs`/`axe-detail-ref-v39.mjs`): the
    reference at mobile fails `button-name` (critical — its unlabeled
    Select triggers + kebabs) on the four item views and
    `svg-img-alt` (its donut sectors) on the two dashboard routes —
    the same families as desktop — while the clone PASSES both
    everywhere; the clone's only mobile failures are color-contrast,
    every flagged color in the reference's own 7-color palette (the
    mobile node counts differ from desktop only by the demo card
    counts).
  - **THE HEADLINE STRUCTURAL SUPERSET**: the reference's mobile sheet
    is a plain fixed div — NO dialog role, NO aria-labelledby, NO
    `<nav>` landmark, NO accessible title — while the clone's is
    `role="dialog"` + `aria-labelledby` → the sr-only "Navigation"
    DialogTitle + `<nav aria-label="Primary">` + the five links + the
    named burger (sr-only "Toggle Sidebar").
  - **The permanent mobile gate** (`tests/e2e/a11y.spec.ts`, 8 tests,
    a new `test.use` describe): the six authed routes sheet-closed
    under the SAME two gates (the shared assertParityClean helper) +
    the sheet-OPEN test (the REAL burger click, the structural pins —
    role=dialog, the labelledby resolving to "Navigation", the nav
    label, the five links, the Escape close — then both gates) + the
    logged-out mobile login (its own opt-out describe, ZERO
    violations). All 17 a11y tests GREEN on the first run.
  - **The stripped-burger mutation is the extension's raison d'être**:
    removing the burger's sr-only span fires `button-name` on ALL SIX
    mobile routes while every desktop scan stays green — the burger
    is md:hidden at desktop, so a desktop-only gate can NEVER catch a
    nameless burger (verified to FAIL; restored → GREEN). The removed
    DialogTitle mutation breaks the aria-labelledby pin exactly as
    designed (verified; restored → GREEN). Zero production-code
    changes (`git diff src/` empty).
- The VLM pair (the mobile sheet-open state, 390×844): VERDICT
  DIFFERENT with BOTH flags explained (the clone's Dashboard active
  highlight = superset fix #3 [the reference marks nothing active on
  `/`]; the avatar letter = the different demo users).
- Probe lessons: the agent-browser daemon can WEDGE after a killed
  parity server (`pkill agent-browser` restarts it cleanly); the
  clone's burger is named by its sr-only SPAN, not an aria-label;
  `document.querySelector('nav')` on mobile finds the display:none
  desktop rail first — query the sheet element for its own nav; the
  reference's burger is hit-test blocked by its toast viewport (R1) —
  mobile sheet probes must JS-click it; `playwright test -g` with
  parens in the title breaks the grep regex.
- The full chain re-run: **108/195/35** (187 → 195: the 8 mobile a11y
  tests). The 16 screenshots regenerated. Docs aligned: README (the
  195 counts + the v39 row), CLAUDE.md (the mobile-gate entry),
  AGENTS.md (the v39 paragraph), the SKILL doc (Session 74 row),
  session_83.md, the probe README (the v39 section), this worklog.

---

## Session 72 — Parity iteration v38: the a11y tooling pass shipped as a permanent gate + the expenses frequency filter + the savings filter-card pinned, zero production-code changes (2026-10-11)

**Goal:** refresh the workspace (git pull — intact this session), re-run
the baseline chain, sweep the session-78/79 queue (the a11y tooling pass
open since session 72, the /expenses frequency-filter option census, the
/savings filter-card instance), fix what the DOM finds, TDD-first, docs
aligned, commit + push via the SSH wrapper.

- Workspace INTACT (git pull `c035106..bac2246`; no re-clone/reinstall).
  Baseline green on the FIRST full run: **108/177/35** + lint + typecheck
  + build. Audit clean (the same 5 dev-only braces advisories).
  `@axe-core/playwright` 4.13.0 added as a devDependency.
- Standing checks all clean: mobile-nav R1–R4 (**32nd** — Tailwind v4
  pins hold, both sites; the reference's toast-blocker, sheet-trap,
  no-landmark, and 395 overflows all still live), data drift (32nd —
  reference read-only, verified before + after; the frequency + category
  probes reset to All), the SEO pair (robots/sitemap live on both; the
  reference's capitalized app-route URLs still documented), the VLM
  /savings pair (all four flags data-explained: the card count, the
  classification tags, the payment-method footer chips, the avatar
  letter).
- **THE A11Y TOOLING PASS (open since session 72) — shipped**:
  - The exploratory axe-core 4.13 deep scan on BOTH sites
    (a11y-scan-v38.mjs, the wcag2a/2aa/21a/21aa tags, desktop
    1280×800, the booted state) + the per-node enumeration with
    computed colors (axe-detail-v38.mjs / axe-detail-ref-v38.mjs):
    **the reference FAILS `button-name` (critical — its unlabeled
    Select triggers + card kebabs) and `svg-img-alt` (its recharts
    donut sectors) while the clone PASSES both** (the aria-label
    superset + the v31 inert donut). The clone's ONLY failures are
    color-contrast — every flagged node 1:1 with the reference's own
    failure at a byte-identical color (7-color palette: the lime/
    blue/orange type accents, the hero status rgb(245,169,98), the
    stat-card sublabel rgb(107,114,128), the 404 slate
    rgb(203,213,225), the net-worth inactive tab rgb(115,115,115)).
    /savings + /login scan CLEAN on both sites.
  - **The permanent gate** (`tests/e2e/a11y.spec.ts`, 8 tests): the 6
    authed routes + the 404 + the logged-out login (its own
    storageState-opt-out describe — `test.use` is hoisted per
    describe). GATE 1 (structural): no violation id other than
    color-contrast may appear. GATE 2 (provenance): every flagged
    node's computed color (read via its axe node.target selector
    chain) must be one of the reference's 7 palette colors. The login
    asserts ZERO violations. Mutation-verified (a stripped
    SelectTrigger aria-label → the button-name gate FAILS, restored →
    GREEN).
  - **The hasFocus() helper** (`scripts/parity-probes/
    hasfocus-gate.sh`): the v34 discipline formalized — assert
    `document.hasFocus()`, re-focus with a REAL `press Shift`,
    re-assert, fail loud. Demonstrated live; baked into the v39+
    standing-script discipline (README section).
- **Surface A — the /expenses frequency filter (first-time live, NO
  drift)**: the second Select's STATIC 7-option list BYTE-IDENTICAL to
  the reference's (All Frequencies + One-time/Weekly/Bi-weekly/
  Monthly/Quarterly/Annually); the round-trip (the clone: Weekly →
  Groceries + "1 items · $320.00", reset → 3 cards; the reference:
  One-time → 0 cards — its demo expenses are all recurring,
  data-level). Pinned (S1) with the mutation sanity (removing the
  Weekly SelectItem FAILS the census).
- **Surface B — the /savings filter-card instance (the third
  items-view, first-time live, NO drift)**: the white rounded-2xl card
  (bg/radius/border/padding byte-identical), the 447×36 search with
  the aria-label superset (the reference's input carries NO label),
  the two 216×36 comboboxes, the 4-column grid; the category
  round-trip (Emergency Fund → 1 card + "1 items · $800.00" → the
  reset; the reference's own list carries only All + Emergency Fund —
  its demo savings has ONE item, data-level). Pinned (S2) with the
  mutation sanity (changing the savings searchPlaceholder FAILS).
- Probe lessons: `getByRole("option", {name:"Weekly"})` collides with
  "Bi-weekly" (substring matching — use exact:true in census loops);
  AxeBuilder.analyze() requires a page from browser.newContext();
  test.use({storageState}) is hoisted per describe; the axe
  node.target selector chains resolve cleanly for the
  color-provenance reads; the reference's /income holds ONE card
  (Salary $5000) — its 1-vs-2 flagged-node difference is demo data.
- The full chain re-run: **108/187/35** (177 → 187: the 8 a11y tests +
  S1 + S2). The 16 screenshots regenerated. Docs aligned: README (the
  187 counts + the v38 row), CLAUDE.md (the a11y-gate entry), AGENTS.md
  (the v38 paragraph), the SKILL doc (Session 73 row), session_80.md,
  the probe README (the v38 section). Changeset: +1 devDependency,
  +133 items.spec lines, the new a11y.spec, the v38 probes + the
  helper, **zero production-code changes**.

---

## Session 71 — Parity iteration v37: the filter triggers' focus family + the search typing contract + the payment-method filter pinned, zero production-code drift (2026-10-11)

**Goal:** re-clone the reset workspace, re-run the baseline chain,
audit, sweep the session-76 suggestions (the filter Select TRIGGERS'
focus-visible family, the search input's focus + typing contract, the
/expenses payment-method filter), fix what the DOM finds, TDD-first,
docs aligned, commit + push via the SSH wrapper.

- Workspace re-cloned fresh (`118a45b`; the old one had been reset —
  only an "Initial commit", no remote). Environment rebuilt: npm
  install, `cp .env.example .env` (`DATABASE_URL="file:../db/
  custom.db"`), db:push + db:seed. Baseline green on the FIRST full
  run: **108/174/35** + lint + typecheck + build. Audit clean (the
  same 5 dev-only braces advisories, secret scan clean,
  `.env.example` current).
- Standing checks all clean: mobile-nav R1–R4 (**31st** — Tailwind v4
  pins hold, both sites; the reference's toast-blocker, sheet-trap,
  no-landmark, and 395/464 overflows all still live), data drift
  (31st — reference read-only, verified before + after; the PM probe
  Escape-closed without selecting, the edit-dialog probe opened +
  Escape-closed without saving), the SEO pair (robots/sitemap/head
  census matching the pinned values; the reference's sitemap
  capitalizes its app-route URLs — measured live, documented), the
  VLM /expenses+PM-open pair (all five flags data-explained: the card
  count, the extra tags + footer chips + the two extra dropdown
  options = the clone's seed carrying paymentMethod values, the
  avatar letter).
- The session-76 suggested surfaces, all first-time measurements,
  **ZERO production-code drift**:
  - **Surface A** — the filter Select TRIGGERS' focus-visible family
    (the v36 census walked past the stops without asserting their
    chrome): a REAL Tab onto the closed trigger renders the 1px
    #0a0a0a ring + the ambient shadow over the UNTINTED border
    (216×36). Pinned (S1) with the mutation sanity (stripping the
    SelectTrigger's `focus:ring-1 focus:ring-ring` FAILS it). **O1
    documented (not drift)**: the full box-shadow strings differ in
    their INVISIBLE lead layers (the reference's v3 three-slot
    white-offset construct vs the clone's v4 five-slot transparent
    construct — every lead a 0px-spread shadow, invisible by
    construction; the VISIBLE layers byte-identical, the v11
    shadow-scale precedent).
  - **Surface B** — the search input's focus + typing contract: the
    same ring family on the REAL-Tab landing + the REAL-key behavior
    (an exact-name match narrows the list + recomputes the header; a
    no-match string swaps to the EMPTY state — the reference's h3;
    clearing restores the cards). Pinned (S2) with the mutation
    sanity (stripping the Input's `focus-visible:ring-1
    focus-visible:ring-ring` FAILS it).
  - **Surface C** — the /expenses payment-method filter (the third
    Select, first-time live): the trigger chrome + the DYNAMIC option
    derivation + the Credit Card round-trip (2 cards, "2 items ·
    $385.00") + the reset. The reference's own list carries only its
    All option (its demo items hold no paymentMethod values —
    data-level; its edit dialog carries the "payment method" field,
    verified read-only — the model matches). Pinned (S3) with the
    mutation sanity (emptying the `paymentMethods` derivation FAILS
    it). Also re-verified: the reference's expense cards carry the
    inline Edit (77×32) + Calculate (110×32) hover-revealed buttons
    (the v8-pinned family).
- Probe lessons: the reference's card titles are h4 (its empty-state
  heading h3 — an h3-only card census fabricated "no cards"
  readings); `agent-browser keyboard press Backspace` does not
  register in the reference's focused search input and the CLI's
  `fill ""` dispatches no input event — clear React-controlled
  inputs via the native value setter + a bubbled input Event
  (Playwright's `fill("")` is unaffected); the e2e drives the
  PRODUCTION build — rebuild before a pin-sanity mutation can bite.
- Three new pins (S1/S2/S3, TDD — every pin's mutation verified to
  FAIL it) → **108/177/35 green**. The final changeset verified
  against `git diff`: exactly the one spec file (+149 lines), zero
  production changes. The 16 screenshots regenerated.
- Committed and pushed to main via the SSH wrapper.

## Session 70 — Parity iteration v36: the hover-highlight family + the filter listbox + the Tab-order census pinned, zero production-code drift (2026-10-10)

**Goal:** refresh the workspace, re-run the baseline chain, audit,
sweep the session-72 suggestions (the item-card menu's hover-highlight
family, the filter Selects' listbox keyboard contract, the items-view
Tab-order census), fix what the DOM finds, TDD-first, docs aligned,
commit + push via the SSH wrapper.

- Workspace refreshed (`51f1fd9` — the session-73 transcript; the
  environment otherwise intact). Baseline green on the FIRST full
  run: **108/171/35** + lint + typecheck + build. Audit clean (the
  same 5 dev-only braces advisories, secret scan clean,
  `.env.example` current).
- Standing checks all clean: mobile-nav R1–R4 (**30th** — Tailwind v4
  pins hold, both sites; the reference's toast-blocker, sheet-trap,
  no-landmark, and 395/464 overflows all still live), data drift
  (30th — reference read-only, verified before + after), the SEO pair
  (robots/sitemap/head census matching the pinned values), the VLM
  dashboard + filter-open pairs (all flags DOM-explained: superset #3
  + demo data + the Base44 platform badge).
- The session-72 suggested surfaces, all first-time measurements,
  **ZERO production-code drift**:
  - **Surface A** — the action menu's HOVER-highlight family (REAL
    `agent-browser hover` on both sites; synthetic mouse events do
    NOT move Radix's highlight — the probe lesson): hover → Radix
    moves DOM focus to the item → the SAME accent family as keyboard
    focus (bg rgb(245,245,245) + text rgb(23,23,23); the hovered
    Delete NOT red — the v35 G1 cascade holds on the hover path);
    pointer-off → focus back to the container, items at rest, the
    menu survives. Pinned (S1) with the mutation sanity (the
    re-added `focus:text-[#dc2626]` FAILS it).
  - **Surface B** — the filter Selects' listbox keyboard contract
    (the /income instances; v34 covered the sub-dialog): fresh-open
    via click AND Enter → the SELECTED option's accent highlight;
    arrows rove clamped at both ends; Home/End; Escape → trigger
    (popup only); Enter selects + updates the trigger text. Pinned
    (S2) with the fixture-restore discipline + the mutation sanity
    (the stripped `focus:bg-accent` FAILS it).
  - **Surface C** — the items-view Tab-order census (page-level,
    first-time): the five nav links → Add Income → the search input →
    the two filter comboboxes → the card kebabs — the same sequence
    the reference walks MINUS its Base44 platform badge
    (`#base44-edit-badge` — platform chrome, correctly not
    replicated). Pinned (S3). **Superset #7 documented + pinned from
    the walk**: the reference's kebab stays INVISIBLE (opacity 0)
    when keyboard-focused and when keyboard-opened; the clone's
    day-one `focus-visible:opacity-100` +
    `data-[state=open]:opacity-100` keep it visible. Also documented:
    the clone's invisible aria-labels on the filter controls (a
    day-one superset), the reference's closed-trigger aria-controls
    persistence (a Radix-minor-version detail).
- Three new pins (S1/S2/S3, TDD — every pin's mutation verified to
  FAIL it) → **108/174/35 green**. The final changeset verified
  against `git diff`: exactly the two spec files, zero production
  changes. The 16 screenshots regenerated (byte-identical).
- Probe lessons: synthetic mouse events do not move Radix's hover
  highlight (only a REAL pointer move); a blur does not reset the
  sequential focus navigation position (walk past the wrap); Radix
  Select's post-open focus landing is ASYNC (a racing key press hits
  the trigger — interleave a toBeFocused() between presses).
- Committed and pushed to main via the SSH wrapper.

---

## Session 68 — Parity iteration v35: the action-menu focus family fixed + the quick-action/deep-link surfaces pinned (2026-10-10)

**Goal:** rebuild the reset workspace, re-run the baseline chain, audit,
sweep the session-70 suggestions (the item-card action menus' open-state
focus chrome, the dashboard quick-action buttons' focus-visible family,
the deep-link/URL contract), fix what the DOM finds, TDD-first, docs
aligned, commit + push via the SSH wrapper.

- Workspace REBUILT from scratch (the sandbox was reset): fresh clone
  (`54b07f4`), npm install, .env restored, db/ pushed + seeded,
  scandihaven re-cloned. Baseline green on the FIRST full run:
  **108/168/35** + lint + typecheck + build. Audit clean (the same 5
  dev-only braces advisories, secret scan clean, .env.example current).
- Standing checks all clean: mobile-nav R1–R4 (**29th** — Tailwind v4
  pins hold, both sites; the reference's toast-blocker, sheet-trap,
  no-landmark, and 395/464 overflows all still live), data drift
  (29th — reference read-only, verified before + after), the SEO pair
  (head census matching the pinned values), the VLM dashboard +
  menu-open pairs (dashboard flags DOM-explained = superset #3 + demo
  data; menu-open IDENTICAL, zero flags).
- The session-70 suggested surfaces, first-time REAL-key measurements:
  **G1** — the action-menu DELETE's FOCUSED text color (the reference
  renders accent-foreground rgb(23,23,23); the clone's v5-era
  `focus:text-[#dc2626]` kept it RED) — fixed on all three Delete
  items; **G2** — the menu TRIGGERS lacked the reference's shadcn
  `focus-visible:ring-1 ring-ring` family entirely (the raw Radix
  primitive) — fixed on all three triggers; the rest of the menu
  contract byte-identical (click-open container / Enter-open first
  item / ArrowUp-from-container LAST item / roving / Home-End /
  Tab-trap / Escape→trigger / 118×32 items / 36×36 hover-revealed
  trigger); the quick-action Add Item's focus-visible four-layer
  composite byte-identical (pinned at the dashboard instance); the
  from_url deep-link honored identically on both sites (pinned); the
  404's Go Home link-vs-button documented as a SUPERSET.
- THREE new pins (TDD: S1 RED on exactly the G1 drift → the fixes →
  GREEN → both pin-sanity mutations bite → restored; S2/S3 GREEN with
  the mutation verified) — `docs/remediation-plan-v35.md` written and
  validated against the codebase pre-execution.
- Full chain **108/171/35 green** (168 → 171); the 16 screenshots
  regenerated (the net-worth diffs = the seeded relative dates rolling
  forward); docs aligned (README/CLAUDE/AGENTS/SKILL/probe-README/
  session_72); committed and pushed to main via the SSH wrapper.

## Session 67 — Parity iteration v34: the forgot-state focus walk + the frequency listbox contract pinned, zero production-code drift (2026-10-10)

**Goal:** `git pull` (the session-69 transcript commit `3ff3d7c`) + re-verify the
environment, re-run the baseline chain, audit, sweep the session-69
suggestions (the forgot-password state's focus walk, the calculator
frequency Select's listbox keyboard contract, the API error-tier audit),
fix what the DOM finds, TDD-first, docs aligned, commit + push via the
SSH wrapper.

- Workspace refreshed via `git pull` (`3ff3d7c` — the session_69
  transcript; the first pull ran before the user pushed it); the v33
  environment survived intact (node_modules, .env, the db/ seed —
  re-verified). Baseline green on the FIRST full run: **108/166/35** +
  lint + typecheck + build. Audit clean (the same 5 dev-only `braces`
  advisories, secret scan clean, .env.example current).
- Standing checks all clean: mobile-nav R1–R4 (**28th** — Tailwind v4
  pins hold, both sites; the clone's burger hit direct, its sheet
  closes, its landmark + active state present, all six routes fit 390;
  the reference's toast-blocker, sheet-trap, no-landmark, and 395/464
  overflows all still live), data drift (28th — allocation 30.5% /
  $3475.00 / $5000 / $1000 / $525, reference read-only, verified before
  + after), the SEO pair (byte-identical head census + the superset
  webmanifest), the VLM dashboard + forgot pairs (dashboard one flag
  DOM-explained = superset #3; forgot IDENTICAL, zero flags).
- The session-69 suggested surfaces ALL clean with first-time
  measurements: **S1 (pin)** the forgot-password state's focus walk —
  THREE app stops in order (Back → Email → Send reset link), NO
  auto-focus on landing, the v13 slate input family + the v25 zinc
  submit family (focus-VISIBLE-gated — programmatic focus never
  engages it; programmatic-focus-then-real-Tab measures it) + the raw
  back button, all byte-identical — pinned by login-parity; **S2 (pin)**
  the frequency Select's listbox keyboard contract — the same Radix
  combobox family, fresh-open accent highlight on the selected option
  (`rgb(245,245,245)` — `:focus`-driven), arrows roving CLAMPED at both
  ends, Home/End, NO typeahead (both sites), Escape closing the POPUP
  only (focus → trigger, the sub-dialog stays), Enter selecting — pinned
  by the calculator spec; **S3** the API error-tier audit (401/400/404/
  429/403/409 consistent, the client layered network → non-JSON →
  envelope, every Prisma query userId-scoped, money math pinned).
- **The big probe lesson: the UNFOCUSED-HEADLESS-WINDOW `:focus`
  ARTIFACT** — an eval that DOM-clicks a Select trigger open reads
  `document.activeElement` = the selected option while
  `element.matches(':focus')` is FALSE and
  `document.querySelector(':focus')` returns NOTHING (the headless
  page's OS-level window focus was lost after a navigation without
  real key presses). The first fresh-open listbox comparison
  FABRICATED a "the clone renders no highlight" finding — the reference
  read had run after real key presses (page focused), the clone read
  after JS clicks alone. GATE every `:focus`-computed read on
  `document.hasFocus()` (a real `press Shift` re-focuses the page);
  Playwright is immune (its pages hold real focus). Also: the display
  pipeline eats `[h`/`[m` sequences DISPLAY-ONLY (a python repr read
  fabricated a "file mangled" conclusion; byte-level reads proved every
  file intact), `[tabindex=-1]` must be quoted in CSS selectors, the
  reference's burger is named by its sr-only span (no aria-label), and
  the reference's mobile sheet closes via the burger toggle (no X).
- D1: the README's structure/commands sections still said 165 e2e
  after v33's 166 — fixed to the new 168.
- TDD: S1 RED→GREEN (the census mapping + the focus-visible
  restructure) + 2 pin-sanity mutations; S2 GREEN (the roving
  settle) + 1 pin-sanity mutation (SelectItem's `focus:bg-accent`
  removed → FAILED → restored). Full chain re-run **108/168/35 green**
  (166→168). The 16 screenshots regenerated; the dev DB census clean
  (7 items / 0 line items / 0 probe users).
- Docs aligned: README (the v34 row + counts), CLAUDE.md, AGENTS.md,
  the SKILL doc, docs/session_70.md, this worklog, the probe README
  (the v34 catalog + the L1–L7 lessons). Committed and pushed to main
  via docs/ssh_git_wrapper_v3.py.

---

## Session 65 — Parity iteration v33: the verify-email code inputs' focus family + the toast announcer pinned (2026-10-10)

**Goal:** `git pull` (the session-67 transcript commit) + re-verify the
environment, re-run the baseline chain, audit, sweep the session-67
suggestions (the line-item sub-dialog's focus traversal, the
register/verify-email focus families, the toast's focus semantics, the
performance/bundle pass), fix what the DOM finds, TDD-first, docs
aligned, commit + push via the SSH wrapper.

- Workspace refreshed via `git pull` (`3818922`); the v32 environment
  survived intact (node_modules, .env, the db/ seed — re-verified);
  `scandihaven` re-cloned (reference only). Baseline green on the FIRST
  full run: **108/165/35** + lint + typecheck + build. Audit clean (the
  same 5 dev-only `braces` advisories, secret scan clean, .env.example
  current).
- Standing checks all clean: mobile-nav R1–R4 (**27th** — Tailwind v4
  pins hold, both sites), data drift (27th — the reference read-only,
  verified before + after the probe cycles), the SEO pair (full
  head-metadata census byte-identical; the reference's /manifest.json
  still 302s empty — the clone's webmanifest is the superset).
- **The session-67 suggested surfaces resolved**: the line-item
  sub-dialog's focus traversal (NO finding — the 13-stop census +
  the REAL-Tab walk byte-identical on both sites INCLUDING the native
  date segments: each `<input type="date">` is a 4-stop walk; the
  reference keeps focus on its trigger on mouse-open and EXITS after
  the last stop, both documented Radix supersets; the reference's
  plain-div dialogs IGNORE Escape — measured); the sub-dialog's select
  triggers (NO finding — the 1px ring IS present as the FOURTH
  box-shadow layer behind v4's three transparent placeholders; the
  first 85-char read fabricated a missing ring — read FULL strings);
  the register/verify-email focus families (the register inputs, the
  verify submit, Resend, and Back all matched — the CODE inputs did
  not); the toast's focus semantics (NO finding — the clone's
  viewport is the labeled pe:none region, its live toast is a
  focusable li PLUS Radix's hidden role=status/aria-live=assertive
  announcer portal measured inside its 1s window; the reference's
  viewports are semantic-less pe:auto divs and its toasts never fire
  on the measured flows); the bundle pass (documented: 12 chunks
  1,104KB raw/338KB gz vs the reference's 1,060KB/317KB single bundle
  + a 214KB dev-only badge.js — wire-weight parity, route-split
  superset).
- **G1 (the code inputs' focus family)**: the reference's focused 40x44
  boxes render the 2px zinc-950 ring (`rgb(255,255,255) 0 0 0 0,
  rgb(9,9,11) 0 0 0 2px`) with NO border tint (stays #e4e4e7) and the
  first box AUTO-FOCUSES on landing; the clone's
  `focus:border-[#94a3b8] focus:outline-none` was an invented tint
  with no ring and no auto-focus. Fixed with the register-input
  idiom `focus:shadow-[0_0_0_0_#fff,0_0_0_2px_#09090b]
  focus:outline-none` + `autoFocus={i === 0}` (the reference itself
  switches families — register slate vs code zinc; each surface
  measured separately).
- **S1 (the toast announcer pin)**: the calculator's line-item-add test
  now asserts the `[role="status"][aria-live]` announcer (count 1 +
  the toast text, read inside the 1s window) — pin-sanity verified by
  swapping the Radix Root for a plain li (the no-announcer rewrite
  simulation): the pin FAILS, restored GREEN.
- TDD: G1 RED (the auto-focus assertion) → GREEN → 2 pin-sanity
  mutations (the shadow removed, the autoFocus removed — both FAIL)
  → restored → GREEN. **Full chain re-run: 108 unit · 166 e2e
  (165→166) · 35 smoke.** Live re-verification on the :3200 parity
  server: the focused Digit 2 renders the 2px zinc ring + the
  untinted border (byte-matching the reference modulo v4's invisible
  lead layers); the mobile-nav R1/R4 spot check clean. The 16
  screenshots regenerated; the dev db restored (0 line items,
  Entertainment $65, 2235 total, the probe users deleted).
- Docs aligned: README (v33 row + counts), CLAUDE.md (e2e description
  + counts), AGENTS.md (v33 paragraph), the SKILL doc (session row +
  166 state), docs/session_68.md, the probe README (the v33 catalog +
  five lessons), this worklog.
- Committed and pushed to main via docs/ssh_git_wrapper_v3.py
  (paramiko shim; key shredded after).

## Session 63 — Parity iteration v32: the calculator row actions' focus-visible ring family + the breakdown aria-expanded superset pinned (2026-10-10)

**Goal:** workspace re-clone (the sandbox reset) + rebuild, re-run the
baseline chain, audit, sweep the session-63 suggestions (the net-worth
dropdown menus' keyboard contract, the calculator line-item row actions'
Tab order, the breakdown accordion's arrow semantics), fix what the DOM
finds, TDD-first, docs aligned, commit + push via the SSH wrapper.

- The workspace was RESET — the repo re-cloned (`zero-balance` at
  `0c91904`, `scandihaven` re-cloned); the environment rebuilt and
  re-verified (node_modules, .env with `DATABASE_URL="file:../db/custom.db"`,
  db/ re-pushed + re-seeded at the repo root). Baseline green on the FIRST
  full run: **108/164/35** + lint + typecheck + build. Audit clean (the
  same 5 dev-only `braces` advisories, secret scan clean, .env.example
  current).
- Standing checks all clean: mobile-nav R1–R4 (**26th** — Tailwind v4
  pins hold, both sites; R2 re-verified with a robust STRUCTURE-based
  sheet detector — the v31 white-bg matcher missed the reference's sheet
  this session), data drift (26th — the reference read-only, verified
  before + after the calculator probe cycles), the SEO pair (full
  head-metadata census byte-identical; the reference's /manifest.json
  endpoint 302s empty — the clone's webmanifest is the superset).
- **The session-63 suggested surfaces resolved**: the net-worth dropdown
  menus' keyboard contract (NO finding — byte-identical: click-open
  container focus / Enter-open first item / arrow roving with
  data-highlighted / CLAMPED at the ends / Home-End / NO typeahead /
  Escape returns focus to the trigger); the calculator line-item row
  actions' Tab order (the 4-stop census + the REAL-Tab walk byte-identical
  — the row actions are Tab stops inside their opacity-0 hover-reveal
  container on BOTH sites; the reveal is hover-only, never focus; the
  reference's dialog EXITS after the last stop vs the clone's Radix wrap
  = the documented trap superset); and the breakdown accordion's arrow
  semantics (NO functional finding — arrows/Home/End inert on both,
  Enter expands both, Escape collapses on neither; the reference's row
  delete is IMMEDIATE, the clone's inline confirm is the documented
  "unconfirmed deletes fixed" superset).
- **G1 (the calculator row actions' focus-visible ring family)**: the
  reference's 32px Edit/Delete buttons carry the shadcn focus family —
  REAL-Tab-measured, the focused Edit renders `outline: solid 2px
  rgba(0,0,0,0)` + the 1px #0a0a0a ring shadow (`rgb(255,255,255) 0 0 0
  0, rgb(10,10,10) 0 0 0 1px, …`) — while the clone's raw
  `h-8 w-8 … hover:bg-accent` buttons rendered the browser-default
  `outline: auto`. Fixed with `focus-visible:ring-1
  focus-visible:ring-ring` inline + a NEW globals.css pin
  `.zb-row-action:focus-visible` — **a THIRD Tailwind v4 class-name-parity
  trap documented**: v4's `outline-none` utility emits `outline-style:
  none` ONLY, so v3's `outline: 2px solid transparent; outline-offset:
  2px` form must be pinned in CSS (the same trap family as the
  shadow-scale shift and the hover media-gate). The test-side trap:
  `transition-colors`' v4 property list INCLUDES outline-color — the
  focus-chrome read must settle ≥350ms or it catches the transparent
  settle mid-flight in oklab form.
- **S1 (the breakdown rows' aria-expanded)**: the clone's section +
  category rows carry accurate `aria-expanded` (the reference's have
  none) — measured, KEPT as a deliberate a11y superset (the aria-label
  family: invisible, correct, no spurious semantics), and pinned by the
  breakdown spec so a future sweep doesn't "fix" it away.
- Two VLM pairs (dashboard + calculator): both DIFFERENT flags
  DOM-explained (the Dashboard-active rail = superset #3; the X's
  open-state ring = the documented v29 Radix superset).
- TDD: RED → GREEN → pin-sanity mutations (the ring utilities removed,
  the globals pin removed, the aria-expanded attribute removed) → FAIL →
  restored → GREEN. Full chain **108/165/35 green** (164 → 165); the fix
  live-re-verified byte-identical on the :3200 parity server (the REAL-Tab
  focused Edit reads the reference's exact outline + ring); the 16
  screenshots regenerated (2 PNGs byte-noise only); docs aligned (probe
  README, README, CLAUDE, AGENTS, SKILL, session_66, the worklog);
  committed and pushed to main via the SSH wrapper.

---

## Session 61 — Parity iteration v31: the donut's keyboard semantics + the tiles' fresh roving state (2026-10-10)

**Goal:** workspace re-clone (the sandbox reset) + rebuild, re-run the
baseline chain, audit, sweep the session-61 suggestions (the donut's
keyboard semantics, the filter selects' open-state arrow semantics, the
dialog forms' full Tab order), fix what the DOM finds, TDD-first, docs
aligned, commit + push via the SSH wrapper.

- The workspace was RESET — the repo re-cloned (`zero-balance` at
  `f9a9637`, `scandihaven` re-cloned); the environment rebuilt and
  re-verified (node_modules, .env with `DATABASE_URL="file:../db/custom.db"`,
  db/ re-pushed + re-seeded at the repo root). Baseline green on the FIRST
  full run: **108/161/35** + lint + typecheck + build. Audit clean (the
  same 5 dev-only `braces` advisories, secret scan clean, .env.example
  current).
- Standing checks all clean: mobile-nav R1–R4 (**25th** — Tailwind v4
  pins hold, both sites; one timing artifact caught — a 2.5s settle read
  the still-loading /networth as 390, the 6s re-measure restored the
  documented 464), data drift (25th — the reference read-only), the SEO
  pair (full head-metadata census byte-identical; the reference's
  /manifest.json endpoint 302s empty — the clone's webmanifest is the
  superset).
- **The session-61 suggested surfaces resolved**: the filter selects'
  arrow semantics (NO finding — identical Radix listbox roving on both
  sites, no wrap at the ends); the dialog forms' full Tab order (the
  strict 14-field census byte-identical — the reference's 1×1
  native-select shadows are not stops on either site); and the donut's
  keyboard semantics — **the recharts 3↔2.15 drift trio** (G1).
- **G1 (the donut's keyboard semantics)**: recharts 3's
  `accessibilityLayer` defaults ON — the clone's svg surface carried
  `tabIndex=0` + `role="application"` (an extra tab stop rendering the
  browser's unpinned 5px auto ring; the reference's surface is inert —
  no attribute, no role) and its tooltip's default content carried
  `role="status"` + `aria-live="assertive"` (the reference's renders
  neither) — both killed by `<PieChart accessibilityLayer={false}>`;
  AND recharts 3 REMOVED 2.15's `attachKeyboardHandlers` pie roving
  (ArrowLeft `++n % len` forward / ArrowRight `--n < 0 → len-1`
  BACKWARD — the first ArrowRight focuses the LAST sector / Escape blurs
  + resets / alt-arrows ignored / no preventDefault; the contract read
  from the installed 2.15.3 source) — replicated exactly in
  `usePieKeyboardParity` (an onkeydown DOM property on the donut wrapper,
  delegation via bubbling — immune to the ResponsiveContainer mount
  race; the pie layer g stays the shared tab stop at `rootTabIndex: 0`).
- **G2 (the tiles' fresh roving state)**: the reference's older Radix ties
  the fresh roving tabindex to the CHECKED state (container 0 + checked
  radio 0 = two stops; Radix 1.4.8's fresh state renders all radios −1)
  — fixed with `tabIndex={selected ? 0 : −1}` on the tiles'
  RadioGroupItem. Measured on both sites: a REAL Tab into the group lands
  on the CHECKED item (the container's entry focus forwards instantly).
- Two VLM pairs (dashboard + add-dialog): all flags DOM-explained (the
  Dashboard-active rail = superset #3; the allocation bar + avatar =
  seeded data; the X's open-state ring = the documented v29 Radix
  superset — both X's byte-identical at rest).
- TDD: RED → GREEN → pin-sanity mutations (the a11y prop removed, the
  roving wrap broken, the tile prop flipped) → FAIL → restored → GREEN.
  Full chain **108/164/35 green**; both fixes live-re-verified
  byte-identical on the :3200 parity server; the 16 screenshots
  regenerated (zero visual change); docs aligned (probe README, README,
  CLAUDE, AGENTS, SKILL, session_63, the narrative, this log); committed
  and pushed to main via the SSH wrapper.

---

## Session 59 — Parity iteration v30: zero drift, the semantics pinned (2026-10-10)

**Goal:** pull the session-60 transcript doc, re-run the baseline chain,
audit, sweep the session-59 suggestions (the guideline-row hovers, the
quick-action card-button hovers, the savings card family, the net-worth
tablist's arrow-key semantics, the details sheet's keyboard semantics at
MOBILE), fix what the DOM finds, TDD-first, docs aligned, commit + push
via the SSH wrapper.

- `git pull` fast-forwarded `368712d` → `ece66b5` (the session-60
  transcript doc); the workspace intact (node_modules, .env, seeded db/,
  scandihaven). Baseline green on the FIRST full run: **108/158/35** +
  lint + typecheck + build. Audit clean (the same 5 dev-only `braces`
  advisories, secret scan clean).
- Standing checks all clean: mobile-nav R1–R4 (**24th** — Tailwind v4
  pins hold, both sites), data drift (24th — the reference read-only),
  the SEO pair — **DEEPENED to the full head-metadata census**
  (description/OG/Twitter byte-identical; the reference's /manifest.json
  endpoint serves EMPTY — the clone's webmanifest is the superset).
- **ZERO production-code drift found** — every session-59 suggested
  surface swept clean with first-time REAL-hover/keyboard measurements:
  the guideline rows (no hover family on either site), the quick-action
  buttons (rendered parity: v4's `scale: 1.1` property + the extra
  TRANSPARENT shadow lead layers — the visible pair byte-identical), the
  savings card family (byte-identical; the details sheet opens on
  savings-card click), the tablist's arrow-key semantics (the reference
  IS Radix — the identical RovingFocusGroup contract), and the mobile
  details-sheet keyboard (geometry byte-identical 0/390/717.4px; the
  reference's no-trap bug confirmed at the bottom-sheet breakpoint; the
  clone's trap holds). Two VLM pairs: both IDENTICAL.
- **The remediation = the pins** (`docs/remediation-plan-v30.md`): three
  new e2e tests — the details sheet's keyboard semantics (initial focus
  X + Tab containment + Escape, desktop AND mobile with the measured
  bottom-sheet geometry) and the tablist's roving arrow-key contract
  (focus move + automatic activation + the roving tabindex update + the
  panel switch). TDD: GREEN → pin-sanity mutations (flipped trap
  containment, flipped maxH, flipped focus target + aria-selected) →
  FAIL → restored → GREEN.
- Full chain **108/161/35 green**; both pins live-re-verified on the
  :3200 parity server; the 16 screenshots regenerated; docs aligned
  (probe README, README, CLAUDE, AGENTS, SKILL, session_61, this log);
  committed and pushed to main via the SSH wrapper.

---

## Session 57 — Parity iteration v29: the net-worth card labels + the keyboard-semantics measurements (2026-10-10)

**Goal:** workspace re-clone (the sandbox reset) + rebuild, re-run the
baseline chain, audit, sweep the session-57 suggestions (the details
sheet's keyboard semantics, the VLM details pair, the edit entry-point
consistency, the net-worth interactive-family census), fix what the
DOM finds, TDD-first, docs aligned, commit + push via the SSH wrapper.

- The workspace was RESET — the repo re-cloned (`zero-balance` at
  `34b4970`, `scandihaven` re-cloned); the environment rebuilt and
  re-verified (.env, db re-pushed + re-seeded, node_modules). Baseline
  green: 108/158/35 + lint + typecheck + build (one transient
  not-found-spec e2e flake under fresh-sandbox load — investigated: a
  transient /api/auth/me failure flips the boot gate to the login
  redirect; isolated + full re-runs green; environmental, pre-existing).
  Audit clean (the same 5 dev-only `braces` advisories, secret scan
  clean).
- Standing checks all clean: mobile-nav R1–R4 (23rd — Tailwind v4 pins
  hold, both sites), data drift (23rd — the reference read-only this
  session), the SEO pair.
- **G1 (the one fix)**: the net-worth asset/liability card TYPE labels
  — the reference's are Badge-base DIVs (rest bg `rgb(243,244,246)` /
  text `rgb(55,65,81)` + the REAL-hover tint `rgba(245,245,245,0.8)`
  over 150ms — the v28 G1 family on a surface never diffed); the
  clone's spans computed TW4 oklab with no hover family. Fixed on both
  label strings: the hex pins `bg-[#f3f4f6] text-[#374151]` + the
  existing `.zb-badge-hover` class; TDD (RED → GREEN → pin-sanity) and
  live-verified byte-identical on both axes.
- The session-57 suggestions all resolved: the details sheet's KEYBOARD
  semantics measured for the first time (the reference: NO focus, NO
  trap, NO role, NO Escape — its Tab walk tours the whole underlying
  page; the clone's Radix initial-focus→X + trap + Escape is the
  documented superset, and Chrome renders the pinned X ring on open);
  the VLM details pair (both DIFFERENT flags DOM-explained: the X ring
  = the superset, the fact rows = data); the ellipsis-Edit vs
  footer-Edit (the SAME 14-field dialog — no finding); the net-worth
  census (tabs/tablist/gradients/containers/menus all byte-identical —
  the finding above).
- The net-worth mobile VLM pair's three flags all DOM-arbitrated
  NO-change: the 1-col summary stacking re-proven as the v4 data-fit
  superset by a LIVE 2-col DOM experiment (the seeded $65,300/$311,250
  glyphs need 152/169px vs the 107px cells; the reference's own
  $25,000 already micro-overflows); the trend icon inset 48px on both;
  the tab icons the v14 circle-arrow pair.
- Also verified: the breakdown-row hover is INERT on both sites (each
  site's inline background-color overrides its own hover class), the
  reference's asset-card click opens NOTHING, and its liability tab
  holds 0 items. Full chain **108/158/35 green**; the screenshots
  regenerated (14 byte-identical + 2 sub-pixel net-worth captures);
  probe lessons persisted (the reference's tab triggers ignore
  synthetic clicks; VLM glyph claims need computed-geometry
  arbitration; the clone's dialog X is found by its sr-only text).

---

## Session 55 — Parity iteration v28: the Budget Item Details sheet + the badge/button families (2026-10-09)

**Goal:** workspace re-clone (the sandbox reset) + rebuild, re-run the
baseline chain, audit, sweep the session-55 suggestions (the button
census, the card action trigger, the avatar chip, the toast close
buttons), fix what the DOM finds, TDD-first, docs aligned, commit + push
via the SSH wrapper.

- The workspace was RESET — both repos re-cloned (`zero-balance` at
  `8329114`, `scandihaven` at `d4789c3`); the environment rebuilt and
  re-verified (.env, db re-pushed + re-seeded, node_modules). Baseline
  green on the first run: 108/155/35 + lint + typecheck + build. Audit
  clean (the same 5 dev-only `braces` advisories, secret scan clean).
- Standing checks all clean: mobile-nav R1–R4 (22nd — Tailwind v4 pins
  hold, both sites), data drift (22nd — the toast probes' throwaway
  items deleted through the reference's own UI, census re-verified), the
  SEO pair.
- The session-55 suggestions all resolved: the one-pass button census
  (found G1+G2), the avatar chip (non-interactive on both — no
  finding), the toast close buttons (the reference renders NO toasts on
  add-success — viewport heights [32,32] at 200ms/900ms/3.4s — the
  clone's toasts remain the superset).
- **G3 (the headline — a whole missing surface)**: the reference's
  card-body click opens a read-only **Budget Item Details sheet**; the
  clone's card click was dead. Fully measured (all three types, both
  viewports: the forest-50%+blur overlay, the mobile bottom sheet /
  desktop 512px max-w-lg panel, the sticky header + X-close, the
  pill-badge summary with the type-colored amount, the tinted
  classification block with its own copy map, the icon-led fact rows
  incl. conditional Payment Method + Notes, the Created/Last Updated
  footer) and built: `item-details-dialog.tsx` + the store's `details`
  slot + the card's guarded onClick + the app-shell mount.
- **G1**: the card badges' hover family — the reference tints to
  `rgba(245,245,245,0.8)` on a REAL CDP hover; fixed via the
  `.zb-badge-hover` globals.css pin (the direct TW4 utility computes as
  oklab — the v7 G6 drift class).
- **G2**: the expense-card Edit/Calculate buttons' keyboard family —
  `focus-visible:ring-1` + the Edit's `hover:text-accent-foreground`
  (the clone's hand-written strings had none; the UA default outline
  rendered on real Tab).
- TDD throughout: RED first for all three, pin-sanity mutations all
  FAIL, restored; live re-verification on :3200 (the sheet's geometry
  byte-identical at both viewports; the badge tint + the real-Tab ring
  measured exact). Full chain **108/158/35 green** (3 new e2e);
  screenshots regenerated — 15 byte-identical + the new
  `16-item-details.png`. Probe lessons persisted: synthetic mouseenter
  NEVER engages :hover (REAL `mouse move` does); the reference's
  dialogs don't close on Escape; its number-input's value stays empty.

---

## Session 53 — Parity iteration v27: the dialog X-close button's focus/hover family (2026-10-09)

**Goal:** refresh (`git pull` → `d7d92f7`; environment intact), re-run the
baseline chain, audit, sweep the session-53 suggestions (reduced-motion,
print/overscroll, scrollbars) + fresh extensions, fix what the DOM finds,
TDD-first, docs aligned, commit + push via the SSH wrapper.

- Baseline fully green on the first run: 108/108 unit · 155/155 e2e ·
  35/35 smoke + lint + typecheck + build. Audit clean (the same 5
  dev-only `braces` advisories, secret scan clean, the v26 changeset
  re-reviewed).
- Standing checks all clean: mobile-nav R1–R4 (21st — Tailwind v4 pins
  hold; the clone fits 390 on all routes), data drift (21st), the SEO
  pair, the v26 fixes re-verified live (the classless body on both
  sides).
- **The session-53 suggested surfaces all swept on FIRST measurement —
  NO drift** (`docs/remediation-plan-v27.md`): prefers-reduced-motion
  (BOTH sites run the full 500ms sheet slide-in + the 1s spinner under
  `reduce` — zero reduced-motion rules in either CSSOM; parity is "both
  ignore it"), print/overscroll of the white body canvas (auto
  overscroll, zero print rules on both), and scrollbar styling at the
  dialog's 90vh `overflow-y-auto` (native `auto` scrollbars, zero
  `::-webkit-scrollbar` rules on both).
- Extensions also clean: dark mode (both stay light), the app-surface
  REAL-Tab focus rings (three distinct families — the rail links' blue
  2px sidebar-ring, the Add Item ambient family, the stat cards'
  NO-ring — all matching), the filter triggers + search inputs
  (byte-identical classes).
- **(G1) the ONE real finding — the dialog X-close button's
  keyboard/hover family**: the reference's X runs the shadcn ghost-icon
  base (`focus-visible:outline-none focus-visible:ring-1
  focus-visible:ring-ring` — a 1px #0a0a0a ring on a REAL 18-stop Tab
  walk, the same family as the dialog Cancel/Save buttons v26 verified
  byte-identical) + `hover:bg-accent hover:text-accent-foreground`; the
  clone's hand-written `DialogCloseButton` had drifted to
  `focus:outline-none focus-visible:ring-2` (a 2px ring) with no hover
  text. Fixed with the ONE class string in `dialog.tsx` (all four
  dialogs), pinned by the extended v9 X-close spec.
- TDD: the class-attribute assertions written RED first → the one-line
  fix → GREEN → pin-sanity mutations (ring-2 + a wrong hover class) both
  RED → restored. Live re-verification on the :3200 parity server (the
  real-Tab ring reads 1px #0a0a0a). Full chain **108/155/35 green** (1
  e2e extended); screenshots regenerated byte-identical.
- Probe methodology persisted: the clone's Radix dialog TRAPS focus (the
  reference's plain-div dialogs do not) — the walk-to-X stop counts
  differ, a keydown-dispatched Tab inside one eval reaches the clone's
  X; and the with-server one-invocation pattern boots pages against a
  dying server (the v16 zero-state renders honestly — data probes need
  one invocation). Docs aligned; committed and pushed to main via the
  SSH wrapper.

---

## Session 51 — Parity iteration v26: the reference's classless body + the OTP autocomplete convention (2026-10-09)

**Goal:** refresh (`git pull` → `6b46804`; environment intact), re-run the
baseline chain, audit, sweep the session-51 suggestions (the dialog
buttons' mouse-focus pair + the verify-email inputs audit), fix what the
DOM finds, TDD-first, docs aligned, commit + push via the SSH wrapper.

- Baseline fully green on the first run: 108/108 unit · 154/154 e2e ·
  35/35 smoke + lint + typecheck + build. Audit clean (the same 5
  dev-only `braces` advisories, secret scan clean, the v25 changeset
  re-reviewed).
- Standing checks all clean: mobile-nav R1–R4 (20th — Tailwind v4 pins
  hold; the clone fits 390 on all routes), data drift (20th), the SEO
  pair, the v24 auth census (the three-family table), the v25 fixes
  re-verified live (submit ring #09090b, 404 ring #64748b, body white).
- **The session-51 suggestions swept** (`docs/remediation-plan-v26.md`):
  suggestion 1 (the dialog buttons' Tab-vs-click mouse-focus pair) —
  NO drift: both sites' dialog Cancel/Save carry the byte-identical
  `focus-visible:ring-1 ring-ring` family, no ring on mouse clicks, the
  same visible layers on real Tab (the v19 `focusVisible:true`
  methodology vindicated; an empty-form Save click moves focus to the
  first invalid input via native validation on BOTH sites). Suggestion
  2 (the verify-email state's inputs as an aria/landmark/focus
  surface, first measurement) — structure/geometry/behavior all match,
  ONE attribute fix: (G2) the reference runs `autocomplete
  ="one-time-code"` on the FIRST box only and `off` on the rest (the
  standard OTP convention); the clone had it on all six — fixed with
  the conditional prop; the clone's `aria-label="Digit N"` boxes +
  arrow-key navigation stay as documented supersets (the reference's
  inputs are unnamed and arrow-inert, measured live).
- (G1) **a reference-side drift caught by the v25 re-verification**: the
  reference REMOVED its body's `antialiased` class after v25 (body class
  "" on /login, /, and the 404, `-webkit-font-smoothing: auto`); the
  clone still carried the class — fixed to the reference's classless
  body (rendering byte-identical on Linux Chromium, A/B-pixel-verified;
  on macOS the reference's subpixel text is the target).
- TDD: the classless-body test written RED first + the autocomplete
  distribution extended into the verify-email chrome test (no new
  register-class call) → fixes → GREEN → pin-sanity mutations (the old
  class name + the old first-box value) both RED → restored. Live
  re-verification on the :3200 parity server (body "" + auto; the six
  boxes' attribute distribution). Full chain now **108/155/35 green**;
  screenshots regenerated byte-identical.
- Observation: the reference's register endpoint started demanding
  "Security verification" after ~2 synthetic registrations (a platform
  anti-automation gate — future live verify-state probes on the
  reference may be rate-capped; the 5-attempts lockout stays doubly
  blocked behind it). Docs aligned; committed and pushed to main via
  the SSH wrapper.

---

## Session 49 — Parity iteration v25: the keyboard-focus-ring families + the body's layer (2026-10-09)

**Goal:** refresh (`git pull` → `e7109fd`; environment intact), re-run the
baseline chain, audit, sweep the session-48/50 suggestions (the sm-band
auth pair + the auth submit focus rings), fix what the DOM finds,
TDD-first, docs aligned, commit + push via the SSH wrapper.

- Baseline fully green on the first run: 108/108 unit · 150/150 e2e ·
  35/35 smoke + lint + typecheck + build. Audit clean (the same 5
  dev-only `braces` advisories, secret scan clean, the v24 changeset
  re-reviewed). One false alarm: a "syntax error" that was the display
  pipeline stripping the literal bracket+m sequence (lesson 44 — tsc was
  green the whole time).
- Standing checks all clean: mobile-nav R1–R4 (19th — Tailwind v4 pins
  hold; the clone fits 390 on all routes), data drift (19th), the SEO
  pair, the v24 fixes re-verified live at 390×844 AND the sm band
  672×800 (the sign-up font's 16px middle step — exact match on both
  sites).
- **The FIRST keyboard-focus-ring sweep (REAL Tab presses, pointer
  parked) — three REAL fixes** (`docs/remediation-plan-v25.md`):
  (G1) the auth submits' focus-visible ring — the reference renders
  zinc-950 `#09090b` (its shadcn `ring-ring` + white offset + the v3
  ambient); the clone had the INPUTS' slate-400 `#94a3b8` (the
  reference runs DISTINCT ring families per component — inputs
  #94a3b8 v13, submits #09090b, dialog buttons 1px #0a0a0a v19, the 404
  #64748b); fixed on both submit lines in `login-card.tsx`.
  (G2) the 404 Go Home button — plain `focus:` (any focus, not
  keyboard-only) + slate-500 `#64748b`; fixed verbatim in
  `not-found.tsx`. (G3) the body background layer — the reference
  styles NO body bg (white canvas; the warm #fafaf8 paper on its
  app-shell wrapper); the clone had the paper on the body (a v7-era
  manifest read) — visually invisible (byte-identical screenshots,
  PIL-verified) but a real computed-style + layer drift: fixed with
  `--color-background: #ffffff` + the shell's `bg-(--neutral-warm)`.
- TDD throughout: 4 new e2e written RED first, pin-sanity mutations
  (ring colors + body white → the old values) all RED, restored, GREEN;
  live re-verification with the REAL-Tab walk (the clone's submit ring
  now `rgb(9,9,11) 0 0 0 4px`, the 404 ring `rgb(100,116,139)`, the
  shell paper over the white body). Full chain now **108/154/35 green**.
- Probe lessons 43 (programmatic focus() in agent-browser evals never
  engages :focus/:focus-visible on either site — REAL Tab presses are
  the only reliable focus-chrome probe) and 44 (the display pipeline
  strips the literal bracket+m sequence — verify with charCodeAt before
  "fixing" phantom corruption). Docs/screenshots/worklog aligned;
  committed and pushed to main via the SSH wrapper.

---

## Session 47 — Parity iteration v24: the auth forms' mobile families + the v4 space-y-1.5 label gap (2026-10-09)

**Goal:** refresh (`git pull` → `dd49681`; environment intact — `.env`
DATABASE_URL `file:../db/custom.db`, `db/` at root, node_modules,
configs, sitemap/robots all verified), re-run the baseline chain,
audit, sweep the session-46 suggestions, fix what the DOM finds,
TDD-first, docs aligned, commit + push via the SSH wrapper.

- Baseline fully green on the first run: 108/108 unit · 145/145 e2e ·
  35/35 smoke + lint + typecheck + build (robots/sitemap prerendered).
  Audit clean: same 5 dev-only `braces` advisories, secret scan clean,
  scandihaven unchanged at `d4789c3`, the v23 changeset re-reviewed.
- Standing checks all clean: mobile-nav R1–R4 (18th — Tailwind v4 pins
  hold), data drift (18th — reference unchanged since session 19), the
  SEO pair live on both sites, the v23 sheet-keyboard fix re-verified
  live (Tab loop + Escape identical), the v9 dialog label gap (12px
  both).
- The v24 sweep (session-46's suggestions): the register SIGN-UP state
  at mobile — the VLM said IDENTICAL, the DOM found TWO real drifts:
  (G1) the reference's THREE auth-form responsive families (sign-up/
  forgot run `h-10 sm:h-11` — 40px at mobile — the sign-up font 14px;
  the clone rendered the flat 44px family; desktop coincides, which is
  why every prior pin passed); (G2) the label→input gap (the reference
  10px at every viewport via v3 space-y-1.5's margin-top on the
  input's wrapper; the clone's v4 margin-bottom on the INLINE label is
  absorbed by the line box → 4px). The sheet's ARROW keys: inert on
  both (no findings). The forgot state: desktop identical, mobile
  same two findings.
- Fixed both: per-mode height/font branches in `login-card.tsx` (the
  `INPUT_CLS` constant now carries only the invariant chrome) + the
  globals.css v3-pin extended to `space-y-1.5` (the v9 space-y-2
  pattern's missing scope).
- TDD: 5 new e2e written RED first (4 failing + the sign-in guard) →
  fixes → GREEN → pin-sanity mutations (heights 40→44, gap 10→4 both
  RED) → restored. The live census re-run confirms the clone now
  matches the reference's auth table exactly.
- Full chain green: 108/108 unit · 150/150 e2e (5 new) · 35/35 smoke ·
  lint/typecheck/build. Screenshots regenerated (2 changed — the
  desktop auth forms moved 6px closer to the reference, correctly);
  .env.example verified.
- Docs aligned: README, CLAUDE.md, AGENTS.md, SKILL (lesson 42 — the
  shared-tab false-read struck again; the census pattern + the class
  attribute as tie-breaker), probe README (v24 catalog), the v24 plan,
  `docs/session_48.md`, this worklog. Commit + push to
  git@github.com:nordeim/zero-balance.git main via the SSH wrapper
  (key materialized outside the repo, shredded after).

---

---

---

## Session 45 — Fresh verification & parity iteration v23 (2026-10-09)

**Goal:** refresh the workspace (`git pull` to `93e3b70` — the
environment survived the boundary: `.env`/`db/`/node_modules intact,
all standing brief requirements re-verified: the DATABASE_URL at
`file:../db/custom.db` with `db/` at the repo root, the Vitest/Playwright
configs, the sitemap/robots pair in the build), re-verify the v22
baseline (fully green on the FIRST run — the v22 G1 spec fix holds
deterministically: 108/143/35 + lint/typecheck/build), code-audit the
recent changes (repo skills: code-review-and-audit native-CLI fallback —
lint/tsc/tests green; npm audit = the same 5 dev-only ESLint braces
advisories; secret scan clean; the v22 changeset diff-reviewed), then
the fresh two-site parity surfaces — the session-44 log's two measurable
suggestions (the budget-item dialog's MOBILE pair, the mobile sheet's
KEYBOARD sweep) + two fresh mobile surfaces (the register verify-email
state, the custom 404) + the standing mobile-navigation re-verification
+ data-drift check + the SEO pair. Formal log: `docs/session_46.md`
(the session_45.md slot holds the incoming session-43 conversation
summary).

- Baseline chain: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
  143/143 e2e ✓ (first run, no flakes) · 35/35 smoke ✓.
- Mobile stack re-verified end-to-end (R1–R4) + data drift clean (17th
  consecutive — one FALSE alarm: a drift probe read the clone's numbers
  on the "reference" session because the shared parity browser was
  still on the clone's page; three re-probes + the census confirm
  unchanged) + the SEO pair served on both sites.
- **The v23 sweep**: the budget-item dialog's mobile pair (the VLM's
  classification-radio claim DOM-refuted — the FIFTH dialog-scale
  misread; panel 358×760/90vh/24px identical), the mobile sheet's
  KEYBOARD semantics (Tab focus loop + the blue #3b82f6 ring + Escape —
  identical, first measurement), the verify-email state at MOBILE
  (first measurement: the responsive scale 56/28/20 + the 294×44 button
  — identical), the 404 at mobile (identical), and the v22 sub-dialog
  fix re-verified at both viewports.
- **Two finding groups, both TEST-PINS of measured parity (TDD-first
  with pin-sanity mutations)**: **(G1)** the mobile sheet's keyboard
  semantics pinned by the new mobile-navigation test (the Tab order
  loop + the visible ring; the ring's ~200ms fade-in needed the 350ms
  settle in the spec too); **(G2)** the verify-email state's mobile
  chrome pinned by the new mobile describe (register budget 5→6 calls).
  The pin-sanity restore taught its own lesson: a blind
  `replace(..., 1)` on an assertion pattern that exists twice in a file
  mutated the WRONG test — the desktop pin caught it immediately
  (unique-context edits for mutation restores).
- Full chain: lint · typecheck · **108/108 unit** · build ·
  **145/145 e2e** (2 new) · **35/35 smoke**.
- Screenshots regenerated byte-identical (no app change); `.env.example`
  verified. Docs aligned: README, CLAUDE.md, AGENTS.md, SKILL (lesson 41
  + Appendix B), the probe README (the v23 catalog), the formal log
  `docs/session_46.md`, this worklog.

---

## Session 43 — Fresh verification & parity iteration v22 (2026-10-09)

**Goal:** rebuild the workspace from scratch (the sandbox had been
reset — the repo re-cloned at `dee3176`, node_modules/`.env`/
`db/custom.db` re-created, all standing brief requirements re-verified:
the DATABASE_URL at `file:../db/custom.db` with `db/` at the repo root,
the Vitest/Playwright configs, the sitemap/robots pair in the build),
re-verify the v21 baseline, code-audit the recent changes (repo skills:
code-review-and-audit native-CLI fallback — lint/tsc/tests green; npm
audit = the same 5 dev-only ESLint braces advisories; secret scan
clean), then the fresh two-site parity surfaces — the session-42 log's
three suggested classes (the MOBILE calculator pair, the line-item
EDIT SUB-DIALOG, the app-view KEYBOARD sweeps) + the standing
mobile-navigation re-verification + data-drift check + the SEO pair.
Formal log: `docs/session_44.md` (the session_43.md slot holds the
incoming session-41 conversation summary).

- Baseline chain: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
  **141/142 e2e — ONE deterministic failure** (the verify-email chrome
  spec; the session's first finding, root-caused below) · smoke green.
- Mobile stack re-verified end-to-end (R1 the toast-container
  interception, R2 the sheet trap, R3 the root-route highlight, R4 the
  per-route overflow — ref 395/464 vs clone 390 on all six) + data
  drift clean (sixteenth consecutive check) + the SEO pair served on
  both sites (robots/sitemap live-verified).
- **The v22 sweep**: the mobile calculator pair (the row-actions
  "missing" flag = a SCREENSHOT POINTER ARTIFACT — the reference's shot
  caught its row under the parked mouse; re-measured pointer-away on
  both sides: identical classes/opacities/geometry/colors; the X-close
  claim DOM-refuted for the FOURTH time), the line-item Edit
  sub-dialog measured live for the first time (found the THIRD dialog
  family: 85vh panel cap + `space-y-5` form gaps — the clone rode the
  generic 90vh/`space-y-6` budget family), and the keyboard Tab
  sweeps on the dashboard + income views (order + focus chrome
  identical — no findings).
- **Two finding groups fixed TDD-first** (RED → GREEN each): **(G1)**
  the verify-email spec's parked-pointer race — the Create-account
  click parks Playwright's mouse where the swapped-in Verify button
  renders, and its 200ms hover transition read mid-flight
  (`rgb(19,27,46)` on a correct `#0f172a` button); fixed with the
  park-at-(5,5) + 350ms settle discipline in `registerFreshAccount`
  (the app needed no change); **(G2)** the line-item sub-dialog
  matched to the reference's third family — the inline
  `maxHeight: "85vh"` + the `p-6 space-y-5` form — pinned by the new
  dialog-buttons spec test (which also pins the budget dialog's 90vh
  so the family split can't regress).
- Full chain: lint · typecheck · **108/108 unit** · build ·
  **143/143 e2e** (1 new) · **35/35 smoke**.
- Live parity re-verified: the sub-dialog panel 672×680 desktop /
  358×717 mobile / form gaps 20px — exactly the reference's
  measurements at both viewports. The demo DB restored after the
  audit's line-item mutation. All 15 screenshots regenerated.
- Docs aligned: README, CLAUDE.md, AGENTS.md, SKILL (lesson 40 +
  Appendix B), the probe README (the v22 catalog),
  `docs/session_44.md`, this worklog.

---

## Session 41 — Fresh verification & parity iteration v21 (2026-10-09)

**Goal:** refresh the workspace (`git pull` to `dc09bf5` — the
environment survived the boundary: `.env`/`db/`/node_modules intact,
all standing brief requirements re-verified), re-verify the v20
baseline, code-audit the recent changes (repo skills:
code-review-and-audit native-CLI fallback — lint/tsc/tests green; npm
audit = the same 5 dev-only ESLint braces advisories; secret scan
clean), then the fresh two-site parity surfaces — the session-40 log's
three suggested classes (the calculator's POPULATED state, the mobile
SHEET-OPEN state, the net-worth populated EDIT dialogs) + the two
remaining unmeasured auth flows (the register post-success landing —
measured live for the first time — + a keyboard-focus spot sweep) +
the brief's new standing SEO check — plus the explicit
mobile-navigation re-verification + data-drift check. Formal log:
`docs/session_42.md` (the session_41.md slot holds the incoming
session-39 conversation summary).

- Baseline chain at `dc09bf5` fully green (96/137/30 + lint/typecheck/
  build — first full run, no flakes); the pulled v20 changeset
  re-verified in the code first.
- Mobile stack re-verified end-to-end (R1 the toast-container
  interception, R2 the sheet trap, R3 the root-route highlight, R4 the
  per-route overflow — ref 395/464 vs clone 390 on all six) + data
  drift clean (fifteenth consecutive check).
- **The v21 sweep**: the calculator populated pair (the row-actions
  flag = a REAL reference chrome change — the live reference now
  hover-reveals its line-item row actions, `opacity-0
  group-hover:opacity-100`; the v6-era always-visible pin had aged; the
  "Will update category total" flag = data-driven), the mobile
  sheet-open pair (both flags = the documented superset #3 + avatar
  data — chrome parity holds), the net-worth populated edit-asset pair
  (the X-close claim thrice-DOM-refuted), the register flow measured
  live (the "Verify your email" gate: 6-digit code inputs, the
  5-attempt countdown, resend, re-register-re-issues, the unverified
  sign-in rejection — all measured on the reference with a throwaway
  account), the keyboard spot sweep (clean — the v13 focus ring holds
  once settled + read in full), and the SEO check (the reference
  serves robots.txt + sitemap.xml; the clone 404'd both).
- **Three finding groups fixed TDD-first** (RED → GREEN each):
  **(G1)** `src/app/robots.ts` + `src/app/sitemap.ts` via the Next.js
  MetadataRoute conventions (the reference's five-URL/priority/weekly
  structure mirrored with the clone's routes; Next's canonicalizations
  documented as protocol-equivalent); **(G2)** the calculator row
  actions matched to the live reference + the `@variant group-hover`
  pin in globals.css (v4 media-gates the group family — the pin keeps
  the reveal alive on hover:none devices); **(G3)** the register
  verification gate rebuilt as the honest superset — the full state
  chrome (the 64px shield-check circle, the 6×40×44 inputs, the 44px
  primary button, the countdown line, resend), the new
  `/api/auth/verify-email` + `/api/auth/resend` routes, the register
  re-issue path (no session), the 403 unverified-login rejection with
  the reference's exact banner, the honest no-mail dev-code delivery
  (the v12 forgot-password precedent), and the seeded demo user
  pre-verified (every login-dependent flow unaffected).
- Full chain: lint · typecheck · **108/108 unit** · build ·
  **142/142 e2e** (6 new) · **35/35 smoke** (5 new verify-gate steps).
- Live parity re-verified: G1 both files served, G2 the byte-identical
  container classes + the rest/hover opacities + geometry, G3 the full
  live flow (register → the state → the correct code → the `/`
  dashboard) + the VLM pair on the verify state: **IDENTICAL**. The
  calculator shot regenerated (the G2 surface); all other shots
  pixel-stable.
- Docs aligned: README, CLAUDE.md, AGENTS.md, SKILL (lesson 39 +
  Appendix B), the probe README (v21 catalog), `docs/session_42.md`,
  this worklog.

---

## Session 39 — Fresh verification & parity iteration v20 (2026-10-09)

**Goal:** rebuild the workspace from scratch (the sandbox had been
reset — the repo re-cloned at `365f2a4`, node_modules/`.env`/
`db/custom.db` re-created, all standing brief requirements re-verified),
re-verify the v19 baseline, code-audit the recent changes (repo skills:
code-review-and-audit native-CLI fallback — lint/tsc/tests green; npm
audit = the same 5 dev-only ESLint braces advisories, no patched
release; secret scan clean), then the fresh two-site parity surfaces —
the **MOBILE-APP-VIEW + POPULATED-EDIT-DIALOG VLM sweep** (the
session-38 log's two top suggestions) + the breakdown drill-down —
plus the explicit mobile-navigation re-verification + data-drift check.
Formal log: `docs/session_40.md` (the session_39.md slot holds the
incoming session-37 conversation summary).

- Baseline chain at `365f2a4` fully green (96/135/30 + lint/typecheck/
  build — first full run, no flakes); the pulled v19 changeset
  re-verified in the code first (the fixed recurring row + the v19 pin
  spec).
- Mobile stack re-verified end-to-end: R1 (the ref's TWO toast
  containers still intercept the burger's center hit at (38,30); the
  clone's is DIRECT on the svg), R2 (the ref's sheet still traps after
  nav — `sheetStillOpen: true` + overlay, via the new one-eval
  synthetic-event probe; the clone's closes + 390px fit), R3 (nothing
  active on `/` on the ref; the clone highlights Dashboard), R4 (ref
  395/464px overflow; clone 390 on all six routes). Sheet + link
  geometry identical. Data drift clean — fourteenth consecutive check
  (the census probe's base64→atob UTF-8 mangling root-caused and fixed
  transport-safe — lesson 38).
- **The VLM sweep** (5 mobile views at 390×844 + the populated Edit
  dialog + the breakdown drill-down, z-ai vision + DOM verification of
  every flag): the mobile dashboard IDENTICAL; the networth flags all
  the documented superset fix #4 (the reference's own 464px overflow)
  plus one tab-tint hallucination refuted (identical rgb(220,252,231));
  the drill-down clean; TWO real drifts found and DOM-verified:
  **(G1) the items-view header row** — base `items-start` missing (the
  Add button stretched full-width 358px on mobile vs the reference's
  auto-width 147/155/150) + `mb-6` vs `mb-8` (a 24 vs 32px
  header→filter gap at BOTH viewports; the dashboard's row already
  carried the correct pattern); **(G2) the classification tiles** —
  the reference's tile labels carry 16px lucide icons (circle-alert
  #e07a3b / heart #3b7ea1 / piggy-bank #8fbc3f — the donut-legend
  family) in both Add and Edit states; the v19 empty-dialog sweep had
  missed them.
- Both fixed TDD-first: `items-view.tsx`'s row class aligned to the
  reference's (`items-start` + `mb-8`), `budget-item-dialog.tsx`'s
  tiles given the `CLASSIFICATION_ICONS` map (inline accent colors).
  2 new e2e specs (the mobile-layout header-geometry test + the
  dialog-buttons tile-icons test), RED at the unfixed states, GREEN
  after the fixes; the v9 tile-geometry pins untouched.
- Full chain: lint · typecheck · 96/96 unit · build · **137/137 e2e**
  · 30/30 smoke.
- Live parity re-verified: fresh paired measurements — G1 all values
  identical (147×36 at (16,153), rowBottom 189 → nextTop 221, gap 32);
  G2 all values identical (the three icons at 16px in the exact
  measured colors, tiles 197×52); the post-fix mobile income pair
  passes the VLM comparison IDENTICAL.
- All 15 screenshots regenerated — FIVE changed (the three items-view
  shots + the two dialog shots — exactly the fix scope; the dashboard
  shot pixel-stable, its row already matched).
- Docs aligned: README (counts 137, plan-v20 row), CLAUDE.md (counts +
  the two v20 pins), AGENTS.md (the v20 pin paragraph + the
  probe-transport lesson), SKILL (state 96/137/30, lesson 38, Appendix
  B row), probe README (v20 catalog), `docs/session_40.md`, this
  worklog.

---

## Session 37 — Fresh verification & parity iteration v19 (2026-10-09)

**Goal:** refresh the workspace (`git pull` to `7576e56` — the
environment survived the session boundary: `.env`/`db/`/node_modules
intact, all standing brief requirements re-verified), re-verify the v18
baseline, code-audit the recent changes (repo skills:
code-review-and-audit native-CLI fallback — lint/tsc/tests green; npm
audit = the same 5 dev-only ESLint braces advisories, no patched
release; secret scan clean), then the fresh two-site parity surface —
**the VLM VISUAL SWEEP** (the session-36 log's top suggestion, extended
from the auth surfaces to the app views and dialogs: the first
full-page visual-AI comparison layer the project has run) — plus the
explicit mobile-navigation re-verification + data-drift check + the
tablet-breakpoint re-measurement. Formal log: `docs/session_38.md`
(the session_37.md slot holds the incoming session-35 conversation
summary).

- Baseline chain at `7576e56` fully green (96/134/30 + lint/typecheck/
  build — first full run, no flakes); the pulled v18 changeset
  re-verified in the code first (the caught confirm bars + the
  route-announcer-hardened register spec).
- Mobile stack re-verified end-to-end: R1 (the ref's TWO toast
  containers still intercept the burger's center hit at (38,30) —
  agent-browser's actionability check refused the click, the bug
  live; the clone's is DIRECT on the svg), R2 (the ref's sheet still
  traps after nav; the clone's closes + 390px fit), R3 (nothing active
  on `/` on the ref; the clone highlights Dashboard), R4 (ref
  395/464px overflow; clone 390 on all six routes). Data drift clean —
  thirteenth consecutive check.
- **The VLM sweep** (12 auth pairs + 5 app views + 3 dialogs, z-ai
  vision + a mechanical pixel-diff layer + MD5 asset hashing): the auth
  surfaces IDENTICAL ×6 (the v12/v13 text pins held; the logo PNGs
  byte-identical by MD5), the app views LAYOUT_IDENTICAL ×5, the
  dialogs clean except ONE real drift — the item dialog's
  RECURRING-TOGGLE ROW (the reference: switch LEFT as the first child,
  no calendar icon, no border, a green-tinted rgb(245,248,245) surface,
  h 72; the clone: icon+label left, switch right, 1px border,
  transparent, h 74). Two VLM hallucinations DOM-refuted (the "faded
  logo" — MD5-identical; the "taller button" — 294×44 both) — lesson
  37: the VLM is a screening layer, every flag needs measurement. The
  calculator's "extra line" refuted as a matching data-conditional.
  Tablet breakpoints 767/768/1024 re-measured: visual parity holds
  (rail switch at 768 both; first heading x=288 both).
- G1 fixed TDD-first: `budget-item-dialog.tsx`'s recurring row
  rearranged to the reference's switch-left structure (the CalendarIcon
  and its import removed, the border dropped, the rgb(245,248,245)
  inline background added; the v9 switch-primitive pins untouched).
  1 new e2e spec (the dialog-buttons spec's recurring-row test —
  arrangement + chrome assertions), RED at the unfixed state, GREEN
  after the fix.
- Full chain: lint · typecheck · 96/96 unit · build · **135/135 e2e**
  · 30/30 smoke.
- Live parity re-verified: the fixed row measured on both sites — all
  8 values match exactly (swIdx 0, swX 16, labelX 64, h 72, border
  0px, bg rgb(245,248,245), svg 0, gap 12px); the post-fix dialog
  screenshot pair passes the VLM comparison.
- All 15 screenshots regenerated — exactly ONE changed
  (`07-add-item-modal.png`, the dialog shot; the fix is
  dialog-internal, every other shot pixel-stable).
- Docs aligned: README (counts 135, plan-v19 row), CLAUDE.md (counts +
  the recurring-row pin), AGENTS.md (the v19 pin paragraph + the
  VLM-sweep methodology), SKILL (state 96/135/30, lesson 37,
  Appendix B row), probe README (v19 catalog), `docs/session_38.md`,
  this worklog.

---

## Session 35 — Fresh verification & parity iteration v18 (2026-10-09)

**Goal:** rebuild the workspace from scratch (the sandbox had been reset —
the repo re-cloned at `eec5427`, node_modules/`.env`/`db/custom.db`
re-created, all standing brief requirements re-verified), re-verify the
v17 baseline, code-audit the recent changes (repo skills:
code-review-and-audit native-CLI fallback — lint/tsc/tests green; npm
audit = the same 5 dev-only ESLint braces advisories, no patched
release; secret scan clean), then a fresh two-site parity audit of the
NET-WORTH ASSET/LIABILITY ERROR TIER — the last unpinned dialog family
(the session-34 log's own suggestion) — plus the explicit
mobile-navigation re-verification + data-drift check. Formal log:
`docs/session_36.md` (the session_35.md slot holds the incoming
session-33 conversation summary).

- Baseline chain at `eec5427` fully green (96/129/30 + lint/typecheck/
  build); v17 pins spot-checked in the code first (the caught
  calculator mount effect + the calculator-error spec file).
- Mobile stack re-verified end-to-end: R1 (the ref's TWO toast
  containers still intercept the burger's center hit at (38,30); the
  clone's is DIRECT on the svg), R2 (the ref's sheet still traps after
  nav — `sheetStillOpen: true` + overlay; the clone's closes + 390px
  fit), R3 (nothing active on `/` on the ref; the clone highlights
  Dashboard), R4 (ref 395/464px overflow; clone 390 on all six routes).
  Sheet geometry + link positions identical. Data drift clean —
  twelfth consecutive check (the ref's net worth holds 1 asset, 0
  liabilities — new observation).
- Fresh angles: the NET-WORTH ERROR TIER measured for the first time —
  the reference (entity API aborted) is SILENT on both paths (asset
  delete: NO confirmation, card stays, zero feedback, the DELETE XHR
  verified fired-and-failed; asset save: the plain-div dialog stays
  open, no feedback). The clone's save superset verified live
  ("Could not save the asset"; first probe missed it — the toasts are
  Radix `.zb-toast`, NOT sonner) but BOTH delete paths were swallowed
  (`void deleteAsset()` / `void deleteLiability()` in net-worth-view) —
  and the whole tier had ZERO e2e coverage.
- G1 fixed TDD-first across THREE files: the net-worth confirm bars +
  (the post-fix grep sweep's find) `item-card.tsx`'s `void
  deleteItem()` — the card-menu path the v16 dialog audit missed (the
  dialog's own delete was always caught). All three now catch + toast
  the honest errors ("Could not delete the asset/liability/item"),
  rendering unchanged (card + confirm bar stay — the store only mutates
  after the API resolves). 5 new e2e specs: 4 in
  `tests/e2e/networth-error.spec.ts` (asset/liability save/delete
  under route-aborted APIs) + 1 in `tests/e2e/items.spec.ts` (the
  item-card delete failure). RED → GREEN at the exact unfixed states.
- G2: the register duplicate-email spec's full-suite flake (2 of 4
  runs, never in isolation) root-caused by hardening it — Next.js App
  Router's ROUTE ANNOUNCER renders a second EMPTY `role="alert"`
  (`__next-route-announcer__`, dynamically mounted): the old bare
  `waitForSelector("[role='alert']")` matched the announcer and the
  one-shot evaluate raced the 409's arrival. Fixed with a
  text-filtered retrying locator (SKILL lesson 36).
- Full chain: lint · typecheck · 96/96 unit · build · **134/134 e2e**
  · 30/30 smoke.
- Live parity re-verified: the route-aborted net-worth delete renders
  the reference's surfaces (card + confirm bar) WITH the toast caught
  live; a clean reload shows the normal state with NO toast. Dev DB
  verified at seed after all probes (3 assets, 2 liabilities, 7 items).
- All 15 screenshots regenerated — ZERO pixel changes (the fix is
  behavior-only; `git status` on `docs/screenshots/` empty).
- Docs aligned: README (counts 134, plan-v18 row), CLAUDE.md (counts +
  the error tiers + the v18 e2e-contract note), AGENTS.md (the v18 pin
  paragraph + the third site), SKILL (state 96/134/30, lesson 36,
  Appendix B row), probe README (v18 catalog + the toast-selector +
  tab + announcer lessons), `docs/session_36.md`, this worklog.

## Session 33 — Fresh verification & parity iteration v17 (2026-10-08)

**Goal:** rebuild the workspace from scratch (the sandbox had been reset —
the repo re-cloned at `7c45de1`, node_modules/`.env`/`db/custom.db`
re-created, all standing brief requirements re-verified), re-verify the
v16 baseline, code-audit the recent changes (repo skills:
code-review-and-audit native-CLI fallback — lint/tsc/tests green; npm
audit = the same 5 dev-only ESLint braces advisories, no patched
release; secret scan clean), then a fresh two-site parity audit of the
CALCULATOR LINE-ITEM ERROR TIER — the parent-recalc response family the
session-32 log flagged as the next surface — plus the explicit
mobile-navigation re-verification + data-drift check. Formal log:
`docs/session_34.md` (the session_33.md slot holds the incoming
session-31 conversation summary).

- Baseline chain at `7c45de1` fully green (96/126/30 + lint/typecheck/
  build — first full run, no flakes); v16 pins spot-checked in the code
  first (the nested-try boot + bootError flag + the AppShell one-shot
  toast effect).
- Mobile stack re-verified end-to-end: R1 (the ref's TWO toast
  containers still intercept the burger's center hit at (38,30); the
  clone's is DIRECT on the svg), R2 (the ref's sheet still traps after
  nav — `sheetStillOpen: true` + overlay; the clone's closes + 390px
  fit), R3 (nothing active on `/` on the ref; the clone highlights
  Dashboard), R4 (ref 395/464px overflow; clone 390 on all six routes).
  Sheet geometry + link positions identical. Data drift clean —
  eleventh consecutive check.
- Fresh angles: the CALCULATOR LINE-ITEM ERROR TIER measured for the
  first time — the reference (entity API aborted) is SILENT on every
  path: its calculator LOAD renders the empty-state ("$0.00 / 0 items /
  No line items yet"), its CREATE leaves the sub-dialog open with no
  feedback and NO optimistic update, its DELETE leaves the row with no
  feedback. The clone's mutation-failure superset verified live
  (create: "Could not save the line item"; delete: "Could not remove
  the line item" — dialog open + row stays + error toasts), but its
  calculator LOAD failure was swallowed as an unhandled rejection
  (`void loadLineItems(item.id)`) — silent, untested, an accident
  rather than a decision.
- 1 finding group (`docs/remediation-plan-v17.md`): the calculator
  load-failure rebuild — `calculator-dialog.tsx`'s mount effect now
  CATCHES the rejection and fires the honest error toast ("Could not
  load the line items / Network error — check your connection and try
  again" — per-open semantics, the same superset class as the v16 boot
  toast and the dialogs' mutation toasts), rendering unchanged (the
  reference's empty-state parity via the `?? []` fallback). Plus the
  test tier: the previously-unpinned create/delete catch blocks now
  guarded by regression-pin specs.
- TDD: 3 new e2e specs (`tests/e2e/calculator-error.spec.ts`) using
  route-aborted `**/api/line-items**` — RED at the exact unfixed values
  (the load toast missing; the mutation pins passing, proving the
  existing superset live) → 1-file fix → GREEN. SKILL lesson 35
  documents the `void promise` swallow + the nested-Radix-dialog
  aria-hidden trap (calculator assertions must wait until the
  sub-dialog closes).
- Full chain: lint · typecheck · 96/96 unit · build · **129/129 e2e**
  (first full run, no flakes) · 30/30 smoke.
- Live parity re-verified: the route-aborted calculator open renders
  the reference's empty-state + the toast caught live; a live-API
  reopen shows the normal state with NO toast. Dev DB restored to seed
  state after the mutation probes.
- All 15 screenshots regenerated — ZERO pixel changes (the fix is
  behavior-only; `git status` on `docs/screenshots/` empty).
- Docs aligned: README (counts 129, plan-v17 row), CLAUDE.md (counts +
  the v17 e2e-contract note), AGENTS.md (v17 pin paragraph), SKILL
  (state 96/129/30, lesson 35, Appendix B row), probe README (v17
  catalog + the calculator-error technique), `docs/session_34.md`,
  this worklog.

---

## Session 31 — Fresh verification & parity iteration v16 (2026-10-08)

**Goal:** sync to `a141322` (the session-29 summary record — the workspace
survived, no reset), re-verify the v15 baseline, code-audit the recent
changes (repo skills: code-review-and-audit native-CLI fallback —
lint/tsc/tests green; npm audit = the same 5 dev-only ESLint braces
advisories, no patched release; secret scan clean), then a fresh two-site
parity audit of the error/network-failure surface class — the natural
sibling of the v15 loading-state work — plus the explicit
mobile-navigation re-verification + data-drift check. Formal log:
`docs/session_32.md` (the session_31.md slot holds the incoming
session-29 conversation summary).

- Baseline chain at `a141322` fully green (96/123/30 + lint/typecheck/
  build; one known login-parity 409 flake, clean in isolation); v15 pins
  spot-checked in the code first.
- Mobile stack re-verified end-to-end: R1 (the ref's TWO toast containers
  still intercept the burger's center hit at (38,30); the clone's is
  DIRECT on the svg), R2 (the ref's sheet still traps after nav —
  `sheetStillOpen: true` + overlay; the clone's closes + 390px fit), R3
  (nothing active on `/` on the ref; the clone highlights Dashboard), R4
  (ref 395/464px overflow; clone 390 on all six routes). Sheet geometry +
  link positions identical. Data drift clean — tenth consecutive check.
- Fresh angles: the ERROR/NETWORK-FAILURE states measured for the first
  time — the reference's entity API aborted during a full-page load
  renders a SILENT ZERO-STATE (full shell, 0.0% / $0.00 / ✓ NET ZERO,
  items views "0 items · $0.00" + their standard empty states, NO error
  surface); the clone BUMPED to /login (boot()'s single catch conflated
  a data failure with a logged-out session). Also measured: the ref's
  mutation failure (silent no-op — dialog stays open, no feedback; the
  clone's dialog + error-toast superset verified live), its client-nav
  under a dead API (no refetch — in-memory, matching), and its
  session-probe failure (unobservable — the platform cookie carries it).
- 1 finding group (`docs/remediation-plan-v16.md`): the boot data-failure
  rebuild — `store.boot()`'s nested try keeps the user + sets a
  `bootError` flag when `refresh()` fails after a successful session
  probe (the reference's stay-in-app zero-state renders), and AppShell
  fires a one-shot honest error toast ("Could not load your data /
  Network error — check your connection and try again" — the same
  superset class as the mutation-failure toasts; the flag clears on
  fire). A failed session probe (401) keeps the login redirect.
- TDD: 3 new e2e specs (`tests/e2e/boot-failure.spec.ts`) using
  route-aborted data APIs (`route.abort("failed")`, `/api/auth/me` left
  live) + a 401-probe regression pin — RED at the exact unfixed values
  (the async login redirect leaves no hero heading; no toast exists) →
  2-file fix → GREEN. SKILL lesson 34 documents the Radix live-region
  double-match (toast `getByText` needs `{ exact: true }`) and the
  catch-conflation anti-pattern.
- Full chain: lint · typecheck · 96/96 unit · build · **126/126 e2e**
  (first full run, no flakes) · 30/30 smoke.
- Live parity re-verified: the route-aborted reload stays on `/` with
  the reference's zero-state + the toast caught live; a clean reload
  recovers `+$2065.00`.
- All 15 screenshots regenerated — ZERO pixel changes (the fix is
  behavior-only; `git status` on `docs/screenshots/` empty).
- Docs aligned: README (counts 126, plan-v16 row), CLAUDE.md (counts +
  the v16 e2e-contract note), AGENTS.md (v16 pin paragraph), SKILL
  (state 96/126/30, lesson 34, Appendix B row), probe README (v16
  catalog + the route-abort technique), `docs/session_32.md`, this
  worklog.

---

## Session 29 — Fresh verification & parity iteration v15 (2026-10-08)

**Goal:** rebuild the workspace from scratch (the sandbox had been reset —
both repos re-cloned, `.env`/db re-created, all standing brief requirements
re-verified), re-verify the v14 baseline at `04e6b4e`, code-audit the
recent changes (repo skills: code-review-and-audit native-CLI fallback —
lint/tsc/tests green; npm audit = the same 5 dev-only ESLint braces
advisories, no patched release; secret scan clean), then a fresh two-site
parity audit of the LAST unmeasured surface class — the loading/spinner
states during data fetches — plus the Select keyboard flows, a VLM
three-page sweep (income/savings/mobile), and the explicit
mobile-navigation re-verification + data-drift check. Formal log:
`docs/session_30.md` (the session_29.md slot holds the incoming
session-27 conversation summary).

- Baseline chain at `04e6b4e` fully green (96/119/30 + lint/typecheck/
  build; one known login-parity 409 flake, clean in isolation + re-run);
  v14 pins spot-checked in the code first.
- Mobile stack re-verified end-to-end: R1 (the ref's TWO toast containers
  still intercept the burger's center hit; the clone's is DIRECT on the
  svg), R2 (the ref's sheet still traps after nav — `sheetStillOpen:
  true` + overlay; the clone's closes + 390px fit), R3 (nothing active
  on `/` on the ref; the clone highlights Dashboard), R4 (ref 395/464px
  overflow; clone 390 on all six routes). Sheet geometry + link
  positions identical. Data drift clean — ninth consecutive check.
- Fresh angles: the LOADING STATE measured for the first time — the
  reference renders a DOM-replacing full-screen spinner on every
  full-page load (fixed inset-0 flex centered overlay, white behind,
  `w-8 h-8 border-4 border-slate-200 border-t-slate-800 rounded-full
  animate-spin`, NO shell in the DOM, until the DATA renders); the
  clone's spinner drifted on chrome (2px lime/transparent-top), DOM
  (inline in main, shell mounted), and timing (booted flipped after the
  session probe, not the data). The Select keyboard flows: the ref is
  internally inconsistent (filter selects advance the highlight, dialog
  selects highlight current — the clone's uniform Radix matches the
  dialog/a11y pattern; documented). VLM sweep: every flag DOM-refuted
  as data-driven; mobile dashboard MATCH.
- 1 finding group (`docs/remediation-plan-v15.md`): the loading-state
  rebuild — `app-shell.tsx` renders ONLY the reference's overlay +
  slate spinner while `!booted` (hex pins per the v8 named-palette
  lesson, 9999px per the v9 radius lesson, `role="status"` kept as the
  a11y superset), and `store.boot()` flips `booted` AFTER `refresh()`
  resolves for authed users.
- TDD: 4 new e2e specs (`tests/e2e/loading-state.spec.ts`) using
  route-delayed API interception (`page.route` + `waitForTimeout` +
  `unrouteAll({behavior:'ignoreErrors'})`) — RED at the exact unfixed
  values → 2-file fix → GREEN. SKILL lesson 33 documents the
  route-delay technique, the rotated-bounding-box measurement trap, and
  the 1280×720 Desktop-Chrome viewport gotcha.
- Full chain: lint · typecheck · 96/96 unit · build · **123/123 e2e**
  (first full run, no flakes) · 30/30 smoke.
- Live parity re-verified: the prerendered HTML ships exactly the
  reference's loading DOM (overlay + spinner + toast region, ZERO
  shell elements); the spinner caught live on a real reload; the
  post-boot shell + seed arithmetic verified on a fresh session.
- All 15 screenshots regenerated — 5 changed, every diff verified as
  seed date-text drift (the re-seeded DB's relative-day offsets; no
  visual-surface change — the spinner is transient, invisible in the
  content-waiting shots).
- Docs aligned: README (counts 123, plan-v15 row), CLAUDE.md (counts +
  the v15 e2e-contract note), AGENTS.md (v15 pin paragraph + the
  updated prerender note), SKILL (state 96/123/30, lesson 33,
  Appendix B row), probe README (v15 catalog), `docs/session_30.md`,
  this worklog.

---

## Session 27 — Fresh verification & parity iteration v14 (2026-10-08)

**Goal:** `git pull` to `931bfcd` (the session-25 summary record), re-verify
the v13 baseline, code-audit the recent changes (repo skills:
code-review-and-audit native-CLI fallback — lint/tsc/tests green; npm audit =
the same 5 dev-only ESLint braces advisories, no patched release; secret scan
clean), then a fresh two-site parity audit led by a three-page VLM screenshot
sweep with DOM verification of every flagged diff. Explicit mobile-navigation
re-verification (the task focus) + reference data-drift check. Formal log:
`docs/session_28.md` (the session_27.md slot holds the incoming session-25
conversation summary).

- Baseline chain at `931bfcd` fully green (96/115/30 + lint/typecheck/
  build); v13 pins spot-checked in the code first.
- Mobile stack re-verified end-to-end: R1 (the ref's toast containers still
  intercept the burger's center hit; the clone's is DIRECT), R2 (the ref's
  sheet still traps after nav; the clone's closes), R3 (nothing active on
  `/` on the ref; the clone highlights Dashboard), R4 (ref 395px overflow;
  clone 390). Sheet geometry + link positions identical.
- Fresh angles: net-worth tablist keyboard flow (identical — roles,
  aria-selected, ArrowRight activation), dialog initial focus (the ref
  leaves focus on the TRIGGER — no trap; the clone's Radix trap is the
  documented a11y superset), invalid-input validation (silent both sides,
  no fixture residue), guideline/accordion hover states (none both),
  user-select sweep (auto both), and the VLM three-page comparison — 3
  real findings, 4 VLM flags refuted by computed styles.
- 4 finding groups (`docs/remediation-plan-v14.md`): the donut hover
  TOOLTIP rebuilt to the reference's recharts-2 chrome (value "$X.XX" +
  #e5e7e3 border + radius 8 + 0 4px 12px shadow + black item row —
  recharts 3's bare defaults drift on all four axes); the net-worth tab
  icons restored (16px lucide circle-arrow-up/down, mr-2, currentColor);
  and the net-worth page header's 48×48 gradient icon chip (forest→lime,
  radius 12, 24px white trending-up — measured at BOTH viewports).
- TDD: 4 new e2e specs — RED at the exact unfixed values → 3-file fix →
  GREEN. The G1 scope GREW during the live re-verification (the tooltip
  chrome axes) and was pinned + locked by four CSS assertions. Test-bug
  fixes documented as SKILL lesson 32 (the mouse-following tooltip breaks
  Playwright .hover() — dispatch synthetically; transition settle for
  post-click icon colors).
- Full chain: lint · typecheck · 96/96 unit · build · **119/119 e2e** ·
  30/30 smoke.
- Live parity re-verified on a fresh clone session: the tooltip reads
  "Need : $7370.00" in the byte-identical chrome; the chip 48×48 at
  (288,38) with the exact gradient; the tab icons 16×16 mr-2 with the
  exact color pair.
- All 15 screenshots regenerated — `06-networth.png` +
  `12-mobile-networth.png` changed (the visible fixes; VLM-verified),
  the other 13 byte-identical.
- Docs aligned: README (counts 119, plan-v14 row), CLAUDE.md (the
  recharts-3 tooltip trap), AGENTS.md (v14 pin paragraph), SKILL (state
  96/119/30, lessons 31-32, Appendix B row), probe README (v14 catalog +
  the VLM-sweep discipline), `scripts/with-server.sh` committed,
  `docs/session_28.md`, this worklog.

---

## Session 25 — Fresh verification & parity iteration v13 (2026-10-08)

**Goal:** `git pull` to `5957b2a` (the session-23 summary record; pulled via
the SSH remote — HTTPS has no credentials in the sandbox), re-verify the v12
baseline, code-audit the recent changes (repo skills: code-review-and-audit
native-CLI fallback — lint/tsc/tests green; npm audit = 5 high all in the
dev-only ESLint braces chain with NO patched release; secret scan clean),
then a fresh two-site parity audit of the dimensions no earlier pass had
measured: the register-flow API error (duplicate email — a read-only probe),
the sign-up password placeholders, the login inputs' :focus ring, the
authed `/login` visit, the Google button's click behavior, item-card date
formats, the hero progress-bar chrome, the OR divider, and a cursor sweep.
Explicit mobile-navigation re-verification (the task focus) + reference
data-drift check. Formal log: `docs/session_26.md` (the session_25.md slot
holds the incoming session-23 conversation summary).

- Baseline chain at `5957b2a` fully green (96/112/30 + lint/typecheck/
  build); v12 pins spot-checked in the code first.
- Mobile stack re-verified end-to-end: R1 (the ref's TWO toast containers
  still intercept the burger's center hit; the clone's is DIRECT), R2 (the
  ref's sheet still traps after nav — the clone's closes), R3 (nothing
  active on `/` on the ref; the clone highlights Dashboard), R4 (ref 395px
  overflow; clone 390). NEW observation (lesson 30): the ref's TRAPPED
  sheet re-renders its active link with dark `#18181b` text while its
  FRESH-opened sheet renders the v10-pinned white — a ref-internal
  inconsistency in a state the clone never has (its sheet closes on nav);
  the clone's fresh-open state re-verified byte-identical.
- 3 finding groups (`docs/remediation-plan-v13.md`): the register
  duplicate-email 409 text matched to the reference ("A user with this
  email already exists" — TEXT-only, the v12 banner chrome already
  matched); the sign-up state's password placeholders restored ("Min. 8
  characters" / "Re-enter password" — sign-in keeps dots); the login
  inputs' focus ring pinned as the reference's two-layer shadcn v1 ring
  (white 0 0 0 2px + slate-400 0 0 0 4px — v4's color-only ring utility
  emits NO shadow without a width class; fixed as an arbitrary
  box-shadow class in `INPUT_CLS`).
- Everything else measured MATCHED: the register banner chrome, the login
  401 text, sign-in placeholders, item-card date formats ("MMM D, YYYY"),
  the hero progress-bar chrome, the OR divider, the Google button chrome,
  cursor styles, the authed `/login` card (no redirect either side), and
  the reference data state (no drift since session 19). The ref's Google
  button opens a REAL OAuth flow through Base44 — the clone's honest-
  unavailable toast is the documented self-hosted divergence.
- TDD: 3 new e2e specs (RED at the exact unfixed values — "An account
  with…", dots, shadow "none"; one waitForSelector fix for the async 409)
  → 3-file fix → GREEN. Full chain: lint · typecheck · 96/96 unit ·
  build · **115/115 e2e** · 30/30 smoke.
- Live parity re-verified on a fresh clone session: the register banner
  byte-identical (368×54 full chrome + the reference's exact text), the
  placeholders exact, the focused email + password inputs rendering the
  exact visible ring layers.
- All 15 screenshots regenerated — **byte-identical** to the committed
  set (git shows no delta; the v13 changes touch no captured surface's
  visible state — the regeneration doubles as a live login smoke).
- Docs aligned: README (counts 115, plan-v13 row), CLAUDE.md (the
  color-only-ring trap), AGENTS.md (v13 pin paragraph), SKILL (state
  96/115/30, lessons 29-30, Appendix B row), probe README (v13 catalog),
  `docs/session_26.md`, this worklog.

---

## Session 23 — Fresh verification & parity iteration v12 (2026-10-08)

**Goal:** `git pull` to `740d6e1` (the session-21 summary record), re-verify
the v11 baseline, then a fresh two-site parity audit of the dimensions no
earlier pass had measured: the login ERROR state (wrong password / mismatched
confirm — never measured on either site), the per-route document.title set,
the login page's root landmark, the forgot-password confirmation state, the
expenses payment-method filter + its listbox OPEN state, and an a11y
structure sweep. Explicit mobile-navigation re-verification (the task
focus) + reference data-drift check. Formal log: `docs/session_24.md` (the
session_23.md slot holds the incoming session-21 conversation summary).

- Baseline chain at `740d6e1` fully green (96/107/30 + lint/typecheck/
  build); v11 pins spot-checked in the code first; scandihaven patterns
  reviewed (already reflected in the ADRs).
- Mobile stack re-verified end-to-end: R1 (the ref's toast container still
  intercepts its burger's center hit), R2 (its sheet still traps after
  nav — Income rendering the full active style in the trapped sheet), R4
  (395px overflow); all clone superset fixes intact (DIRECT hit,
  close-on-nav, 390px fit, sheet active highlighting + the root-route
  Dashboard highlight). NEW observation: the ref's mobile SHEET closes on
  Escape (unlike its dialogs) — the clone's Radix sheet matches.
- 4 finding groups (`docs/remediation-plan-v12.md`): the login error
  state rebuilt as the reference's red-tinted bordered banner
  (red-50/70% wash, red-200 border, radius 12, pad 16, centered red-700
  14px/400 — the shadcn FormMessage pattern; the same slot serves 401s
  and sign-up mismatches); the per-route tab titles restored
  ("Income | ZeroBudget" etc., the one-word "Networth") via route-segment
  layout metadata + the root pipe template; the login root promoted to a
  `<main>` landmark (tag swap); and the forgot-password flow rebuilt as
  the reference's confirmation-state layout with honest copy (no mail
  transport — the reference pretends a link was sent).
- Root-cause detour worth remembering (lesson 27): the title fix was
  first a client-side `document.title` effect — it ran and was silently
  reset ~24ms later by React Float re-emitting the static `<title>` from
  the RSC flight payload after hydration. Diagnosed with an in-page 20ms
  title poller; solved with route-segment metadata (the value ships in
  the prerendered HTML).
- Everything else measured MATCHED: the payment-method filter card +
  listbox OPEN state (option count differs only by data), the a11y h1/
  lang/landmark structure (the clone's aside rail is a superset), login
  h1 + accessible names, and the reference data state (no drift since
  session 19).
- TDD: 5 new/extended e2e specs (RED at the exact unfixed values — one
  locator fix: `getByLabel("Password", { exact: true })` in the sign-up
  state) → 4-file fix → GREEN. Full chain: lint · typecheck · 96/96
  unit · build · **112/112 e2e** · 30/30 smoke.
- Live parity re-verified side by side on fresh sessions: the error
  banner byte-identical (desktop + mobile), the route titles identical
  on all 7 routes, the `<main>` landmark identical, the forgot-state
  typography identical with honest copy. The screenshot catalog grew
  13 → 15 shots (`14-login-error`, `15-forgot-reset`); docs aligned
  (README/CLAUDE/AGENTS/SKILL/probe README/session_24 + this worklog).

---

## Session 21 — Fresh verification & parity iteration v11 (2026-10-08)

**Goal:** `git pull` to `061a16f` (the session-19 summary record), re-verify
the v10 baseline, then a fresh two-site parity audit at computed-style depth
of the dimensions no earlier pass had measured that way: the intermediate /
tablet breakpoints (767/768/1024 — where the rail and the mobile chrome
switch), the desktop rail hover, the hero status badge, the filter card's
live behavior + the item-badge census, the dialog/sheet/stat-card
box-shadows, the `.zb-btn-add` gradient-button family (ambient shadow,
focus-visible ring, Plus-icon size, hover state), the calculator's
sm/outline variants, and the logout affordance. Explicit
mobile-navigation re-verification (the task focus) + reference data-drift
check. Formal log: `docs/session_22.md` (the session_21.md slot holds the
incoming session-19 conversation summary).

- Baseline chain at `061a16f` fully green (96/104/30 + lint/typecheck/
  build); v10 pins spot-checked in the code first.
- Mobile stack re-verified end-to-end: R1 (the ref's toast container still
  intercepts its burger's center hit), R2 (its sheet still traps after
  nav — while ALSO re-confirming the v10 finding: its trapped sheet at
  `/income` renders Income in the FULL active style), R4 (395px
  overflow); all clone superset fixes intact (DIRECT hit, close-on-nav,
  390px fit, sheet active highlighting + the root-route Dashboard
  highlight). Reference data unchanged since session 19.
- Near-false-finding defused: the ref's dialog panel box-shadow reads
  "shadowless" through a truncated string — the visible layer trails two
  transparent lead layers; the full strings are identical both sides.
  Recorded as probe-hygiene lesson 25 (never `.slice()` computed
  multi-layer strings).
- 4 finding groups (`docs/remediation-plan-v11.md`): the empty-state
  headings at 18px vs the reference's measured 20px (items + net-worth —
  the ref's liabilities empty state was reachable live this pass because
  that account has zero liabilities); the `.zb-btn-add` family (v3
  bare-shadow ambient on the gradient buttons, v3 shadow-sm on the
  outline variant, and the shadcn focus-visible ring — white inner +
  1px #0a0a0a + transparent 2px outline — replacing the browser-default
  outline); the Plus icons 20px → 16px on the 7 Add-button sites; and
  the session-1 hover opacity-0.9 fade removed (the reference's gradient
  buttons have no hover state).
- Everything else measured MATCHED: tablet breakpoints (767/768/1024 —
  identical chrome switching and content column), rail hover, hero
  status badge, filter card (geometry + live behavior), item-badge
  census, dialog overlay/panel, stat cards, calculator empty state,
  QuickActionCard icons, Cancel primitive focus — and no logout UI on
  either site (the clone's store/API logout is a headless superset).
- TDD: 3 new/extended e2e specs (5 assertions failing for the right
  reasons in RED) → 4-file fix → GREEN. Full chain: lint · typecheck ·
  96/96 unit · build · **107/107 e2e** (one not-found navigation flake
  on the first run, clean on re-run) · 30/30 smoke.
- Live parity re-verified side by side on fresh sessions (Add button
  147 = 147 / icon 16 / identical visible shadow layers; empty heading
  20px both sides; the focused Save ring byte-identical; calculator
  variants matched); 13 screenshots regenerated (10 changed — the
  Add-button deltas); docs aligned (README/CLAUDE/AGENTS/SKILL/probe
  README/session_22 + this worklog).

---

## Session 19 — Fresh verification & parity iteration v10 (2026-10-08)

**Goal:** `git pull` to `ab9f80c` (session-18 record), re-verify the v9
baseline, then a fresh two-site parity audit at computed-style depth of the
surfaces no earlier pass had measured that way: the mobile sheet's
ACTIVE-link styling (the task-focus surface's one unmeasured state
dimension), the Select popover / card action-menu OPEN states, the breakdown
drill-down EXPANDED rows, the guidelines leaf typography, the live
focus-visible ring, the tall-dialog scroll mechanics, the date inputs, and
the empty-submit behavior. Explicit mobile-navigation re-verification.

- Environment note: the sandbox returned to reaping background processes
  (D-9) — the parity server booted per command through `with-server.sh`
  while the agent-browser daemon persisted; mid-session daemon resource
  pressure (EAGAIN/CDP timeouts) required a full close/re-login cycle, and
  the first full e2e run crashed under the same pressure (22 failures)
  until the live sessions were closed (session-17 lesson re-confirmed).
- Baseline chain at `ab9f80c` fully green (96/102/30 + lint/typecheck/build);
  v9 pins spot-checked in the code first.
- Mobile stack re-verified end-to-end: R1 (agent-browser's own actionability
  check REFUSES the ref's burger click — the toast container covers it —
  live confirmation), R2 (its sheet still traps after nav), R4 (395px
  overflow), R5 (its dialogs ignore Escape — a `[role=dialog]` selector
  artifact false-positived "closed" on the ref's non-Radix dialogs; the
  click-refusal + heading evidence is the reliable pattern); all clone
  superset fixes intact (DIRECT hit, close-on-nav, 390px fit on all five
  routes).
- 1 finding group (`docs/remediation-plan-v10.md`): **the mobile sheet's
  active-nav highlighting** — measured live on the ref's sheet at
  `/income`, the current route renders the FULL active style (135deg
  forest-medium→lime gradient, white, fw 500 — identical to its rail);
  the clone's sheet had `highlightActive={false}` since session 1 (an
  unmeasured assumption that survived eight audit passes). Fixed by
  removing the prop (the sheet shares the rail's active logic; superset
  #3's root-route Dashboard highlight now applies to the sheet too).
- Observations documented: the reference does NOT toast on save (the
  clone's success toasts are superset UX); empty-submit is silent on both;
  audit mutation neutralized in place (the undeletable probe expense →
  "Miscellaneous" $0.00; ref totals restored +$3475.00, expenses count
  3→4 residual).
- Everything else measured MATCHED: Select popover OPEN state, card
  action-menu OPEN state, drill-down EXPANDED rows, guidelines leaves,
  focus-visible ring, dialog scroll mechanics, date inputs, sheet
  internals (brand/avatar/footer), burger/topbar geometry, and the
  reference data state (no drift since session 11).
- TDD: 2 new e2e specs RED → GREEN (sheet active on `/income`; Dashboard
  on `/`). Full chain: lint · typecheck · 96/96 unit · build ·
  **104/104 e2e** · 30/30 smoke. Live parity re-verified side by side on
  the fixed build; 13 screenshots regenerated (only `10-mobile-menu.png`
  changed — the visible delta of the fix); docs aligned
  (README/CLAUDE/AGENTS/SKILL/probe README/session_19 + this worklog).

---

## Session 17 — Fresh verification & parity iteration v9 (2026-10-08)

**Goal:** `git pull` to `92e837e` (session-16 record), re-verify the v8
baseline, then a fresh two-site parity audit at computed-style depth of the
surfaces no earlier pass had measured that way: the donut's data-order
convention, every form dialog's X-close geometry + sticky-header height,
the form-label line box, the classification-tile text line-height, the
shadcn radio/switch primitive tokens, the v4 `rounded-full` computed
radius, and the login card's per-state control geometry. Explicit
mobile-navigation re-verification (the task focus) + reference data-drift
check.

- Baseline chain at `92e837e` fully green (96/92/30 + lint/typecheck/build);
  detached :3200 parity server + `ref9`/`clone9` (desktop) and
  `reflog9`/`clonelog9` (fresh login) browser sessions.
- Mobile stack re-verified end-to-end: R1/R2/R4 all still live on the
  reference (toast-block hit-test, sheet-trap after nav, 395px overflow);
  all clone superset fixes intact (DIRECT hit, sheet closes, 390px fit).
- 7 finding groups (`docs/remediation-plan-v9.md`): the donut re-sorted to
  the reference's value-DESC convention (biggest slice anchored at
  recharts' 3-o'clock start — the v2-era [S,W,N] pin was the same sort
  wearing that era's data) + `labelLine={false}`; the dialog X-close
  rebuilt as the 36×36 in-header `DialogCloseButton` (sticky header
  69px, default absolute X removed); the form Label restored to the
  inline shadcn-v1 line box (12px label→input gap); 52px classification
  tiles; the radio/switch `#171717` primitive family (checked switch
  track, radio borders/dot, white ring-0 thumb — hex-pinned off the brand
  forest `--primary`); `rounded-full` → `rounded-[9999px]` across 24 sites
  (v4 computes calc(infinity) → 33554432px); login per-state geometry
  (14px primary-button text; 44px sign-up/forgot controls vs 48px
  sign-in). Withdrawn: the login-card border-color difference (both cards
  render border-width 0).
- Mid-flight root-cause: v4 rewrote `space-y-*` to margin-block-end on
  `:not(:last-child)` — layout-IGNORED for inline first children (the
  reference's labels), collapsing the gap to 4px. v3 semantics restored
  for `.space-y-2` in `globals.css` (trap 4b; all 43 usages audited safe).
- TDD: 10 new e2e + 4 updated pins RED → GREEN (donut order/lines, dialog
  chrome ×4, primitive tokens ×3 incl. an `expect.poll` for the
  `transition-colors` race, login geometry ×3; two old `rounded-full`
  class-string pins updated). Full chain: lint · typecheck · 96/96 unit ·
  build · **102/102 e2e** · 30/30 smoke.
- Live parity re-verified surface-by-surface on the fixed build (header
  69, X 36/16, gap 12, tiles 52, switch #171717 + white thumb, radio
  #171717, donut [orange, lime, blue] with 0 label lines, legend
  value-desc, 9999px radii with 0 infinity elements left, login 14px +
  48/44 per state); mobile re-checked; 13 screenshots regenerated;
  docs aligned (README/CLAUDE/AGENTS/SKILL/probe README/session_17 +
  this worklog).

---

## Session 15 — Fresh verification & parity iteration v8 (2026-10-08)

**Goal:** workspace was RESET — re-clone, re-provision the environment, then
a fresh two-site parity audit at computed-style depth of the surfaces v7 had
not covered that way (every form dialog's footer-button geometry, the
item-card badge family's computed colors); fix what it found. Explicit
mobile-navigation re-verification (the task focus).

- Re-cloned fresh; `.env` + `db/` re-provisioned (seed intact); full doc
  chain re-read; baseline chain green at `c6d40fa` (96 unit / 83 e2e /
  30 smoke). v7 fixes confirmed live. Notable environment change: a
  detached parity-server boot now survives across tool calls, so the audit
  ran both sites through persistent agent-browser sessions (`ref8`/`clone8`).
- Mobile nav re-verified live on both sites: R1 (toast container still
  swallows the ref's hamburger — hit-test returns the container), R2 (its
  sheet still traps after nav), R4 (395px/464px overflow) all still live on
  the reference; the clone's superset fixes verified end-to-end (DIRECT
  hit, close-on-nav, 390px fit on all five routes).
- Fresh probe audit → **2 finding groups + 1 hygiene item**
  (`docs/remediation-plan-v8.md`): every form dialog's footer is the
  reference's `flex gap-3 pt-4` full-row split with Cancel + Save at
  `flex-1` (≈ 306px each — the clone ran right-aligned 81px/127px buttons);
  the remaining named-palette classes on parity surfaces all compute as
  `lab()` in v4 (nav `text-zinc-700`, both badge maps, the Recurring/status
  badges, the Calculate button's orange) — values identical to the
  reference's plain rgb, so a full hex-pin pass; and `prisma/db/custom.db`
  (a session-1 stray tracked at the wrong path) untracked.
- The instructive non-finding: the "Recurring" card badge — flipping the
  reference's own Recurring Item switch made the same green badge appear on
  its card (then restored); the badge is CONDITIONAL on both sides and the
  difference was pure live-data drift (SKILL lesson 12.18).
- All fixes TDD-first (12 tests / 13 assertions RED → GREEN): NEW
  `badge-colors.spec.ts` (8), +1 nav-geometry, +3 dialog-buttons footer
  geometry; the unit constants pins and items.spec class pins updated to
  the hex forms (computed values now pinned by the new spec).
- Full chain: typecheck · lint · **96/96 unit** · build · **92/92 e2e**
  (83 + 9 net-new) · 30/30 smoke. Live parity re-verified
  surface-by-surface (footer Cancel 307px + Save 305px — the reference's
  exact numbers; every badge at the reference's exact rgb; nav links
  `rgb(63,63,70)`). 13 screenshots regenerated; seed arithmetic intact.
- Docs aligned (README/CLAUDE/AGENTS/SKILL/session_15 + plan v8 + probe
  README). SKILL gained lessons 12.16–12.18; AGENTS gained the v8 pin
  paragraph.

---

## Session 13 — Fresh verification & parity iteration v7 (2026-10-07)

**Goal:** workspace was RESET — re-clone, re-provision the environment, then
a fresh two-site parity audit of the surfaces no prior session had covered
(the login page's full computed chrome, the rail brand block, the mobile
topbar toggle, the sheet border/overlay colors, the 404 page, the document
head); fix what it found. Explicit mobile-navigation re-verification.

- Re-cloned fresh; `.env` + `db/` re-provisioned (seed intact); full doc
  chain re-read; baseline chain green at `7295906` (96 unit / 73 e2e /
  30 smoke). v6 fixes confirmed live.
- Mobile nav re-verified live on both sites: R1 (toast container still
  swallows the ref's hamburger click), R2 (its sheet still traps after
  nav — `sheetOpen: true` while the URL changed), R4 (395px overflow)
  all still live on the reference; the clone's superset fixes verified
  end-to-end (real-click hamburger, close-on-nav, 390 fit).
- Fresh probe audit → **8 finding groups**
  (`docs/remediation-plan-v7.md`): post-login redirect must land on `/`
  (not `/dashboard`); the login surface — the last one still on named slate
  classes — computed everything in lab()/oklab() AND its footer links were
  missing `text-sm` (16px vs the ref's 14px); the logo halo's ring color
  drifted to oklab (a first probe FALSE-POSITIVED "missing ring" by slicing
  boxShadow at 60 chars — corrected during plan validation); the rail brand
  needed a 24px white lucide-target + `text-lg` logo (the clone's 20px +
  `text-base` sat the whole rail 4px high); the mobile toggle's icon was
  flex-squeezed to 12px (no shrink-0) in the wrong color; the sheet border
  (#e5e7e3 vs the ref's neutral #e5e5e5) and overlay (oklab vs rgba)
  drifted; the clone shipped Next's default 404 (the ref has a branded
  one with the quoted path + Go Home); and the head lacked the ref's
  description/OG/Twitter/canonical/manifest/apple meta.
- All fixes TDD-first (13 specs RED → GREEN): login-card full slate hex
  pin pass + inline gradients + text-sm links + `.zb-logo-ring` sibling
  halo layer (an inline boxShadow on the span would kill its
  shadow-lg/hover), sidebar `TargetIcon h-6 w-6` + `text-lg` + the ref's
  `div.w-full.text-sm` ul wrapper, toggle `[&_svg]:size-4
  [&_svg]:shrink-0` in `#0a0a0a`, sheet border/overlay pins, NEW
  `src/app/not-found.tsx` (quoted-path message via window.location lazy
  init + suppressHydrationWarning, client-side "Page Name | ZeroBudget"
  title, Go Home → `/`), and `layout.tsx` metadata +
  `public/manifest.webmanifest`.
- Full chain: typecheck · lint · **96/96 unit** · build · **83/83 e2e**
  (73 + 10 net-new) · 30/30 smoke. Live parity re-verified
  surface-by-surface (login card identical to the ref on every pinned
  value; rail label/link y exact at 113/145; toggle 16px near-black;
  post-login URL `/`; head complete). 13 screenshots regenerated (new:
  13-not-found), seed arithmetic verified intact after the catalog run.
- Docs aligned (README/CLAUDE/AGENTS/SKILL/session_13 + plan v7 + probe
  README). SKILL gained lessons 12.13–12.15 (probe slicing, inline-shadow
  override, flex-squeeze); AGENTS gained the v7 pin paragraph.

---

## Session 11 — Fresh verification & parity iteration v6 (2026-10-07)

**Goal:** workspace refresh + a fresh two-site parity audit of the surfaces
v2–v5 had NOT covered (net-worth cards/menus, every dialog's EDIT variant,
the calculator's populated rows, ALL empty states, wide-viewport geometry,
overlay dismissal); fix what it found.

- Pulled to `bd2e4be` (session-10 = session-9's narrative record);
  re-validated all docs against the codebase; re-ran the full chain green
  (96 unit / 65 e2e / 30 smoke). v5 fixes confirmed live in code.
- New sandbox behavior (D-9): every background process is reaped at command
  exit and the standalone server crashes under `node` — built
  `scripts/parity-probes/with-server.sh` (per-command bun boot + health
  wait + teardown) and audited through it.
- Fresh probe audit of the un-audited surfaces → **14 finding groups**
  (`docs/remediation-plan-v6.md`): menu items must be plain text (no
  pencil/trash icons), all four Save buttons carry the lucide Save icon,
  asset/liability Name + Last Updated span 624px (`md:col-span-2`) with the
  Type select disabled on edit, the reference's bare-icon empty-state
  pattern (wallet/piggy-bank/receipt/circle-arrow-up/down, no tinted
  circles; items views render it card-less, net-worth carded), the
  calculator's always-visible row actions (32px/16px, near-black/red),
  placeholder strings, hex-pinned status pills, and the padding-outside-
  max-w-7xl content column (the clone was 64px narrow at ≥1568px).
- Measured **reference bug R7** (its dialogs ignore outside-click too) and
  discovered the reference's live DATA changed since the recon (seed
  unchanged — pinned by tests). R1/R5/R6 re-confirmed live; every reference
  mutation this session (test line item, one asset, one recalculated
  category) restored and verified.
- All fixes TDD-first (8 new/extended specs, all RED first): NEW
  `empty-states.spec.ts` (3, incl. an API delete/restore fixture dance that
  re-creates liabilities in reverse capture order to preserve `createdAt`
  ordering — D-10), +1 dialog-buttons (Save icons), +2 networth (dialog
  grid spans, disabled-on-edit type), +1 tokens (plain-text menus + red
  pins + trigger hover class), +1 calculator (row chrome + placeholders +
  pills + empty icon).
- Full chain: typecheck · lint · **96/96 unit** · build · **73/73 e2e** ·
  30/30 smoke. Live parity re-verified surface-by-surface; 12 screenshots
  regenerated.
- Docs aligned (README/CLAUDE/AGENTS/SKILL/session_11 + plan v6). SKILL
  gained D-9/D-10; AGENTS gained the v6 parity pin paragraph and the
  fixture-order restore rule.

---

## Session 9 — Fresh verification & parity iteration v5 (2026-10-07)

**Goal:** workspace refresh + a deeper two-site parity audit (the reference's
own token layer, dialog buttons, dropdown states, focus rings, hover
semantics, responsive chrome map); fix what it found.

- Pulled to `e23d854` (session-8 = session-7's narrative record);
  re-validated all docs against the codebase; re-ran the full chain green
  (96 unit / 52 e2e / 30 smoke). v4 fixes confirmed live in code and browser.
- Token-level audit (reading the reference's `:root` vars + an
  inherited-text sweep + `hover:none` emulation) → **10 finding groups**
  (`docs/remediation-plan-v5.md`): zinc-vs-neutral foreground family,
  input/popover borders, the net-worth tab grid + green active state,
  dialog action buttons (ghost Cancel + solid-lime Save vs outline +
  per-dialog gradients), the accent pair, nav hover text, v4's
  media-gated hover variants, muted, lab/oklab drift on three colored
  texts, and the focus-ring tokens.
- Measured **two new reference bugs**: R5 (its dialogs ignore Escape —
  plain fixed overlays, no keyboard dismissal) and R6 (its card-menu
  Delete destroys items immediately, no confirmation). R1–R4 re-confirmed
  live; all clone superset fixes re-verified end-to-end.
- All fixes TDD-first (13 new/extended specs, all RED first): the
  reference's neutral token block in `globals.css`, `@variant hover
  (&:hover)` (v3 hover semantics on every device), the reference tab
  structure (448px grid, `#dcfce7`/`#14532d` active, 24px gap),
  outline Cancellations + gradient Saves (forest for budget/asset,
  orange for line-item/liability — `.zb-btn-primary` removed),
  popover borders → input neutral, arbitrary-hex pins for the
  lab-drifted colors, inline rgba white-alpha labels, ring tokens
  (`#0a0a0a` / `#3b82f6`).
- Full chain: typecheck · lint · **96/96 unit** · build · **65/65 e2e** ·
  30/30 smoke. Live parity re-verified surface-by-surface (every fixed
  value now measures identical to the reference); 12 screenshots
  regenerated.
- Docs aligned (README/CLAUDE/AGENTS/SKILL/session_9 + plan v5). SKILL
  gained D-6/D-7/D-8 (hover media gate, prerender empty-store race,
  lab/oklab drift); AGENTS gained the prerender settle convention and
  the six-superset pin list.

---

## Session 8 — Audit narrative record (2026-10-07)

Session-7's fresh-verification + remediation-v4 narrative, committed as
`docs/session_8.md` (the raw work log of `28ad5fc`).

---

## Session 7 — Fresh verification & parity iteration v4 (2026-10-07)

**Goal:** workspace refresh + a fresh two-site parity audit of every
surface; fix what it found.

- Pulled to `4f9cb28` (session-6 = session-5's narrative record);
  re-validated all docs against the codebase; re-ran the full chain green
  (96 unit / 46 e2e / 30 smoke). Found CLAUDE.md carrying stale session-2
  test counts — fixed in the docs pass.
- Fresh probe-based audit (clone vs live reference, desktop 1280×800 +
  mobile 390×844) → **6 finding groups** (`docs/remediation-plan-v4.md`):
  nav-link height (40px vs the reference's `h-8` 32px), inactive hover
  tint (sidebar-accent vs green-50), active hover dim, the net-worth
  summary card's structure (3-col ratio grid vs the reference's 2-col
  grid + border-t ratio footer row), a 38px mobile net-worth overflow
  (unbreakable `text-4xl` figure stretching the flex-1 `main`), and the
  items-view header count ignoring active filters.
- Measured **two new reference mobile bugs**: its own `/dashboard` scrolls
  to 395px and `/networth` to 464px at 390px (R3/R4). Both prior reference
  mobile-nav bugs re-confirmed live; the clone's fixes re-verified.
- All fixes TDD-first: new `nav-geometry.spec.ts` (3), +2 networth specs,
  +1 items spec — all verified red before implementing. Key changes:
  `h-8` + `hover:bg-green-50` nav links, the reference's summary-card
  layout (2-col grid, xs/70 labels, 2xl amounts, blur, ratio footer row
  with an inline rgba border — dodging the v4 oklab drift), responsive
  `text-2xl sm:text-5xl` net figure, **`min-w-0` on `main`** (the
  structural superset fix for flex min-width:auto overflows), and
  `filtered.length` header counts.
- Full chain: typecheck · lint · **96/96 unit** · build · **52/52 e2e** ·
  30/30 smoke. Live parity re-verified (nav 32px, summary card
  leaf-identical at desktop, all mobile views exactly 390px).
- Screenshot catalog regenerated — now 12 shots (new
  `12-mobile-networth.png`). README/CLAUDE/AGENTS/SKILL/session_7
  aligned; SKILL gained the D-5 row (min-width:auto trap +
  `overflow-wrap: break-word` ≠ min-content).

---

## Session 5 — Fresh verification & parity iteration v3 (2026-10-07)

**Goal:** workspace refresh + a fresh two-site parity audit of every
surface; fix what it found.

- Re-cloned (workspace had been reset); validated all docs against the
  codebase; re-ran the full chain green (95 unit / 39 e2e / 30 smoke).
- Fresh probe-based audit (clone vs live reference, desktop + mobile
  390×844) → **6 finding groups** (`docs/remediation-plan-v3.md`),
  headlined by a CRITICAL clone-side mobile layout bug present since
  session 1: the mobile top bar rendered as a row-flex sibling of `<main>`
  (222px column, main squeezed to 214px, 90px overflow) — invisible to
  the interaction-only e2e suite. Also: the items-views filter card,
  classification tile chrome, the line-item dialog's Payment Method
  field / labels / OWN status enum (active/pending/cancelled), the login
  card's sign-up/forgot structure (+ removal of the dead guest link),
  and the reference's root-URL active-nav gap (documented superset #3).
- All fixes TDD-first: new `mobile-layout.spec.ts` (3), +2 items specs,
  +1 calculator spec, +1 auth spec, +1 validation test. Full chain:
  typecheck · lint · **96/96 unit** · build · **46/46 e2e** · 30/30
  smoke.
- Live parity re-verified on the remediated build (mobile geometry,
  filter card, tiles, line-item dialog, login states — all matching);
  both reference mobile-nav bugs confirmed still live.
- Screenshots regenerated (11); README/PAD/SKILL/session_5 aligned.

---

## Session 4 — Audit narrative record (2026-10-07)

Session-3's deep-audit + remediation-v2 narrative, committed as
`docs/session_4.md` (the raw work log of `8b82e4c`).

---

## Session 3 — Deep parity audit & remediation v2 (2026-10-07)

**Goal:** production-ready superset of `zero-balance-4885a8f3.base44.app` with
visual parity; fresh re-verification of every surface.

- Deep-audited the live reference DOM (computed styles, real clicks/hovers)
  AND its minified JS bundle (template extraction) → **14 finding groups**
  (`docs/remediation-plan-v2.md`): money format split (plain `toFixed(2)` vs
  networth-only grouping), `0.21:1` ratio, the 3-level accordion breakdown
  drill-down, donut order/icons, calculator card restructure, stat cards,
  hero conditional states (✓ NET ZERO / blue over-budget / Math.abs), per-view
  add-button gradients, quick-action card-buttons, badge color maps,
  expense-card hover buttons (no ellipsis), networth type grouping, icon
  corrections, always-plural "N items".
- Implemented all fixes TDD-first: money/constants/dashboard-math unit tests
  rewritten or extended; new `breakdown.spec.ts`; dashboard/items/networth/
  calculator specs rewritten. Superset: delete path for expense items via the
  edit dialog (the reference has none on expense cards).
- Full chain green: typecheck · lint · 95/95 unit · build · 39/39 e2e
  (incl. 7 mobile-nav + 5 breakdown) · 30/30 smoke.
- Live parity re-verified on the remediated build; both reference mobile-nav
  bugs confirmed still live (clone fixes both — pinned).
- Screenshots regenerated (11, incl. `11-breakdown-drilldown.png`); README /
  PAD / SKILL / session_3.md aligned.

---

## Session 2 — Re-verification + distillation (2026-10-07)

**Goal:** re-run the full verification chain, live parity check, and produce
the added deliverables (remediation plan record, SKILL doc, doc alignment).

- Re-validated docs against the codebase; re-ran the full chain (87 unit /
  34 e2e / 30 smoke, typecheck/lint clean).
- Live parity re-check (desktop + mobile 390×844): both reference mobile-nav
  bugs confirmed still live; clone superset verified (hamburger hit-test,
  sheet close-on-nav, Escape).
- Wrote `docs/remediation-plan.md` (session-1/2 findings ledger with the
  20-item ToDo record and regression pin map).
- Distilled `zero-balance_SKILL.md` (20 sections + ADRs + audit history +
  quick-reference card) per the distill-codebase / to-distill-project-into-skill
  method, with every claim verified against the codebase.
- Fixed doc drift (.env.example header, API handler count 13 route files /
  21 handlers). Pushed `6bf69a6`.

---

## Session 1 — Build (2026-10-07)

**Goal:** from scaffolding repo to production clone with test suites.

- Reconned the reference (all views, modals, mobile chrome, design tokens,
  entity schemas); found the two reference mobile-nav bugs (toast viewport
  click-block; sheet stays open after nav).
- Built the app: Next.js 16 App Router, Prisma/SQLite (`db/custom.db`),
  scrypt+HMAC cookie auth, Zustand store, Tailwind v4 with the five trap-log
  mitigations, recharts donut, shadcn-style primitives.
- 13 route files / 21 API handlers, zod validation, rate-limited login,
  server-side line-item recalculation contract.
- Replaced the ORBITAL-era tests with the ZeroBalance suites (87 unit + 34
  e2e incl. 7 mobile-nav specs) + a 30-step smoke test; fixed 7 real bugs the
  tests caught (zustand v5 loop, modal stacking, dialog states, date
  validation…).
- Rewrote the root docs (README, AGENTS, CLAUDE, PAD); screenshots; pushed
  `703ea74`, `6efc1ce`.
