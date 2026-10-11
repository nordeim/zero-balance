# Session 104 — Parity iteration v46: the net-worth card census + the value→facts spacing fix + the confirm-bar white-pill pin (2026-10-11)

**Goal:** the session-101/102 queue's first and third candidates — the
net-worth ASSET/LIABILITY card census at 1280 (the grid pitch, the card
chrome, the hover state, the kebab reveal) and the five-site
confirm-bar white-pill family's shadow-sm (the shadow-scale regression
net, unpinned) — plus whatever the sweep finds. TDD-first, docs
aligned, commit + push via the SSH wrapper.

## What was done

**Step 0 — the workspace.** RESET this session (the sandbox was
reaped): `git clone https://github.com/nordeim/zero-balance.git`
(HEAD fb8d00f — the v45 iteration + the session_101/102/103 docs) →
`npm install` → `cp .env.example .env` → `npm run db:push` →
`npm run db:seed` (7 budget items, 3 assets, 2 liabilities, the demo
workspace). One environment note: the fresh `npm install` resolved
@playwright/test 1.63.0 to a lockfile patch that expects the
chromium-1243 browser build (the cache carried 1200/1248) — the first
e2e run failed 220/221 on `browserType.launch: Executable doesn't
exist`; `npx playwright install chromium` fetched 1243 and the suite
went green. The five core docs + the session docs re-reviewed.

**Step 1 — the baseline chain.** lint ✓ · typecheck ✓ · 108/108 unit ✓
· build ✓ (robots + sitemap prerendered) · **221/221 e2e ✓ (5.0m)** ·
35/35 smoke ✓. npm audit = the same 5 dev-only ESLint-chain advisories
(`--omit=dev` = 0); the secret scan clean (the docs reference files
only); `.env` byte-identical to `.env.example`; the tree clean.

**Step 2 — the 40th standing checks.** Reference side (ref-v40.sh):
R1 the toast-blocker still intercepts the burger, R2 the sheet still
traps, R3 no nav landmark, R4 the 395 overflow — all four reference
bugs still live; the data census read-only (allocation 30.5 /
5000.00 / 1000.00 / 525.00, identical before + after); the SEO pair
live. Clone side (inside one with-server.sh, clone-v40.sh): R1 the
burger hit direct, R2 the sheet closes after nav, R3 the nav landmark
present, R4 zero overflow on all routes; the sheet structure intact
(role=dialog, nav aria-label=Primary, DialogTitle "Navigation", the
named burger); the SEO pair live. **All clean — the superset intact,
the Tailwind v4 pins hold, the mobile menu works on both sites.**

**Step 3 — the v46 sweep (the queue's surfaces, measured live on BOTH
sites).** Probes: `nw-card-v46.mjs` (the net-worth card census) +
`confirm-pill-v46.mjs` (the confirm-bar white pill) + the REAL-hover
driver steps + `vlm-compare-v46.mjs`. The sweep:

- **THE ONE REAL GAP (the value→facts spacing):** the reference wraps
  its card value in `<div class="mb-4"><p class="text-2xl
  font-bold">` — a 16px gap to the facts — while the clone's
  AssetCard/LiabilityCard carry the margin ON the P
  (`mb-2` = 8px). Measured at 1280: the reference card 194px vs the
  clone 186px — the 8px delta IS the gap (the census otherwise
  byte-identical). The item-card's own `mb-4` wrap (item-card.tsx:152)
  is the in-repo precedent — the net-worth cards were the one
  oversight; no prior census had sampled the 1280 card's internal
  rhythm (the v29 card-content census, the v41 summary-card census,
  and the mobile superset census all sampled other surfaces).
- **THE INCIDENT (the reference's direct delete):** the reference's
  net-worth kebab menu → Delete click IS the delete attempt — no
  confirm bar (the v18 superset-fix-#6 family, re-confirmed live — the
  hard way: the probe deleted the reference's only asset). Restored
  immediately via its Add Asset form (the reference's dialogs are
  plain `fixed inset-0` divs, no [role=dialog] — found by the
  Save-button text): name "Savings Account", type bank account, value
  25000, institution "Commonwealth Bank", date 2026-10-07 — the panel
  census re-read "1 items · $25,000" byte-identical to the before
  state, and the dashboard census unchanged. The read-only discipline
  HOLDS for every future net-worth probe: never go past the menu open.
- **The net-worth card census at 1280: BYTE-IDENTICAL except the
  gap.** The grid `md:grid-cols-2 lg:grid-cols-3 gap-4` — 960 wide /
  3 cols × 309.328 / gap 16 (the SAME family on both sites; the first
  probe draft's finder caught the summary card's inner
  `sm:grid-cols-2` stat-blocks grid and read "no grid" — the v4 G4
  design is NOT the card grid); the card 309 / pad 20 / radius 12 /
  border 1px solid rgb(229,231,227) / the rest shadow
  `rgba(0, 0, 0, 0.04) 0px 2px 8px 0px` / bg white / transition all
  0.2s; the title row gap 8 / dot 8×8 rgb(143,188,63) / title
  16px-600 rgb(26,58,46); the type badge bg rgb(243,244,246) / pad
  2px 10px / radius 6 / 12px-600 / rgb(55,65,81) / h 22; the value
  24px-700 rgb(143,188,63) / line-height 32; the facts 12px
  rgb(107,114,128) space-y-2; the kebab 36×36 opacity 0. **The card's
  REAL hover is INERT on BOTH sites** (the inline boxShadow beats the
  `hover:shadow-lg` utility — the v29 family) while the kebab REVEALS
  (opacity 0→1, the group-hover) — verified via agent-browser's REAL
  hover on both sites.
- **The confirm-bar white-pill census (the clone's superset
  chrome):** the bar mt 16 / radius 8 / pad 12 / rgb(254,242,242) /
  space-between; the Cancel pill bg white / pad 4px 12px / radius 6 /
  12px-500 / **the shadow-sm VISIBLE layer `rgba(0, 0, 0, 0.05) 0px
  1px 2px 0px`** (the `--shadow-sm` theme pin's restored v3 value —
  the five-site family's regression net); the Delete twin bg red-600.
  The pill/text colors compute as `lab(...)` strings (Tailwind v4's
  oklab emission) — accepted for the superset-only surfaces (no
  reference counterpart to byte-match).
- **The probe lessons:** the Radix dropdown AND the reference's tab
  triggers ignore synthetic `el.click()` — only a NATIVE
  Playwright/agent-browser click engages them; the reference's
  dialogs are plain `fixed inset-0` divs (find by the Save-button
  text); the agent-browser daemon's Chrome instances survive across
  tool calls — kill them before a Playwright run or the browser
  contexts crash on pthread_create resource exhaustion.

**Step 4 — the remediation plan.** `docs/remediation-plan-v46.md`:
F1 the value→facts fix (`mb-2`→`mb-4` on both cards' value P), F2 the
net-worth card census e2e (the grid + the card chrome + the hover
inert + the kebab reveal + **the h-194 + mb-16 assertions**), F3 the
confirm-bar white-pill census e2e (the bar + the pill's shadow-sm
visible layer + the Cancel restore), S1 four pin-sanity mutations,
D1–D8 the doc alignment. Validated against the codebase
pre-execution (the line numbers, the class families, the e2e
contract's fixture-restore discipline).

**Step 5 — TDD.** The F2 test written FIRST: RED against the mb-2
build (the value mb 8px ≠ 16px + the card h 186 ≠ 194 — the failure
precisely on the gap's assertions), F3 GREEN immediately (pin-only).
The F1 fix applied (`mb-2`→`mb-4`, both cards) → the networth spec
19/19 GREEN. The S1 mutations, each verified to FAIL then restored:
(a) the reverted `mb-4` → the F2 census fails (the mb + the height);
(b) the pill's `shadow-sm` removed → the F3 pin fails; (c) the card's
inline 0.04→0.08 → the F2 rest-shadow pin fails; (d) the kebab's
`group-hover:opacity-100` removed → the F2 hover step fails. One
execution note: the first `-g v46` run crashed on resource exhaustion
(the agent-browser daemons' Chrome instances) — `pkill -f
agent-browser` before the run fixed it.

**Step 6 — the full chain.** lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **223/223 e2e ✓ (5.2m, 221→223)** · 35/35 smoke ✓. The VLM
pair on the /networth view at 1280: **IDENTICAL — zero flags** (the
second fully-clean screening). The 16 screenshots regenerated (the
capture script, against the fixed build).

**Step 7 — the docs.** AGENTS.md (the v46 paragraph), CLAUDE.md (the
223 count + the v46 net-worth insertion), README (the v46 row + the
counts), the SKILL doc (the Session 81 row + the state line + the
command + the three-tier row), the PAD (the v1.1.3 revision block),
the probe README (the v46 section — the incident + the five lessons),
session_104.md (this log) + session_105.md (the raw transcript), the
repo worklog (the Session 80 entry + the ledger list), the workspace
worklog.

**Step 8 — ship.** Commit + push to main via the SSH wrapper
(`docs/ssh_git_wrapper_v3.py` — the key materialized, the fingerprint
verified, the dry-run, the real push, the key shredded).

## The numbers

108 unit · 223 e2e (+2) · 35 smoke · 16 screenshots · 46 remediation
plans · 105 session docs · 4 mutations verified.

## Suggested next steps (the v47 queue candidates)

- The dialog inputs' focus-state shadow composition (the session-101
  queue's second item — the ring+shadow layer interaction under
  focus; the visible layers are pinned via the v13/v25 families, the
  full composition is not).
- The net-worth card's MOBILE census at 390 (the card internal rhythm
  post-fix — the v41 mobile census measured the summary card, not the
  asset cards).
- The item-details sheet's action buttons' shadow family (the v28
  surface, the shadow-scale net's remaining sites).
- Or any new surface — the toast's shadow family, the sheet's
  shadow-lg at 390, the empty-state cards' chrome.
