# Session 107 — Parity iteration v47: the dialog-input focus composite + the net-worth card mobile census + the mobile sheet's shadow-lg — a PIN-ONLY iteration (2026-10-11)

**Goal:** the session-101 queue's second candidate (the dialog inputs'
focus-state shadow composition — the ring+shadow layer interaction
under focus) + the v46 follow-up (the net-worth card's MOBILE census
at 390, the post-fix internal rhythm) + the session-104 queue's sheet
item (the mobile sheet's shadow-lg at 390). TDD-first, docs aligned,
commit + push via the SSH wrapper.

## What was done

**Step 0 — the workspace.** RESET this session (the sandbox was
reaped): `git clone https://github.com/nordeim/zero-balance.git`
(HEAD 9981c43 — the v46 iteration + the session_105/106 docs) →
`npm install` → `cp .env.example .env` → `npm run db:push` →
`npm run db:seed` (7 budget items, 3 assets, 2 liabilities, the demo
workspace) → `npx playwright install chromium` (the 1243 build to
match the lockfile-resolved 1.63.0 — the v46 session's lesson applied
pre-emptively). The five core docs + the session_105/106/v46/worklog
docs re-reviewed; the state verified (108/223/35, the v46
value→facts fix in the code at net-worth-view.tsx:105/:210).

**Step 1 — the baseline chain.** lint ✓ · typecheck ✓ · 108/108 unit
✓ · build ✓ (robots + sitemap prerendered) · **223/223 e2e ✓ (5.2m)**
· 35/35 smoke ✓. npm audit = the same 5 dev-only ESLint-chain
advisories (`--omit=dev` = 0); the secret scan clean; `.env`
byte-identical to `.env.example`; the tree clean. The v46 diff
re-audited: ONE src file (net-worth-view.tsx, 12 lines — the mb-2→mb-4
fix + the why-comments), matching the v46 plan exactly.

**Step 2 — the 41st standing checks.** Reference side: R1 the
toast-blocker still intercepts the burger (elementFromPoint at the
burger's center returns the reference's `fixed top-0 z-[100]` toast
container — the blocker measured live), R2 the sheet still traps
(navigated to /income via the sheet link, the sheet + overlay still
up), R3 no nav landmark, R4 the 395 overflow — all four reference
bugs still live; the data census read-only ("1 items · $25,000", the
Savings Account / Commonwealth Bank restoration from the v46 incident
intact, the net-worth totals $25,000 / $0 / ∞:1); the SEO pair live
(robots.txt + sitemap.xml 200 on both sites). Clone side (inside one
with-server.sh): R1 the burger opens the sheet (5 links), R2 the
nav → the sheet closes (url /income, 0 links), R1b the
elementFromPoint at the burger's center hits the burger's own SVG
child (the clone's toast viewport is pointer-events: none — no
blocker), R3 the nav landmark + 5 links, R4 zero overflow (390/390),
the SEO pair live. **All clean — the superset intact, the Tailwind v4
pins hold, the mobile menu works on both sites.**

**Step 3 — the v47 sweep (three surfaces, measured live on BOTH
sites).**

- **The dialog input's focus-state shadow composition** (the
  session-101 queue's second item — the top queued candidate): the
  reference's Add-Item dialog input measured at 1280 — REST: 3 layers
  (2 transparent leads + the shadow-sm visible layer `rgba(0, 0, 0,
  0.05) 0px 1px 2px 0px`); under REAL focus (`focus({ focusVisible:
  true })`, `:focus-visible` matched): 3 layers (the white zero-spread
  lead + **the 1px `rgb(10, 10, 10)` ring** + the shadow-sm visible
  layer). The clone's shadcn stack: REST 5 layers (4 transparent leads
  + **the same shadow-sm visible layer**); under focus: 5 layers (3
  transparent leads + **the same ring** + **the same shadow-sm visible
  layer**). **Every VISIBLE layer matches; the leads diverge by
  construction (the accepted v10/v25/v45 class).** The input chrome
  identical (h 36 / radius 6 / pad 4px 12px / border 1px
  rgb(229,229,229) / bg transparent); the border UNCHANGED under focus
  on both sites (the ring does the work); the outline: the reference's
  v3 transparent-solid-2px vs the clone's v4 `none` — both invisible.
  **PIN-ONLY.**
- **The net-worth card's MOBILE census at 390** (the v46 follow-up):
  the reference's asset card (inside its 432-wide OVERFLOWING grid —
  its documented superset-fix-#4 bug, docSW 464) — h **194** / pad 20
  / radius 12 / border 1px solid rgb(229,231,227) / rest shadow
  `rgba(0, 0, 0, 0.04) 0px 2px 8px 0px` / transition 0.2s; the value
  wrapped in `div.mb-4` (mb 16, the measured value→facts gap 16); the
  facts 12px rgb(107,114,128). The clone's card: grid 358 / 1 col /
  gap 16 (the page FITS — docSW 390, mainSW 390); the card
  **358×194** — **the card heights match EXACTLY**; the value P mb 16
  (the v46 fix holds at 390 — the clone carries the margin ON the P,
  the reference on the wrap div: the computed geometry is the
  contract); the facts 12px rgb(107,114,128) / the measured gap 16.
  **PIN-ONLY** (the width divergence is the documented superset fix —
  the reference's own page overflows).
- **The mobile sheet's chrome at 390** (the session-104 queue item):
  the reference's sheet (288×844, x 0, bg rgb(250,250,250), transform
  none after settle) — shadow = 2 transparent leads + **the v3
  shadow-lg pair** `rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0,
  0, 0.1) 0px 4px 6px -4px`; the overlay rgba(0,0,0,0.8), z 50. The
  clone's sheet (the same geometry — already pinned by the v7
  G6/mobile-nav specs): 4 transparent leads + **the same two visible
  layers**; the overlay identical. **PIN-ONLY** — the shadow-scale
  regression net's SIXTH site (the lg end, the mobile surface).

**Step 4 — the remediation plan.** `docs/remediation-plan-v47.md`:
F1 the dialog-input focus composite pin, F2 the net-worth mobile card
census pin, F3 the mobile sheet's shadow-lg pin, S1 four pin-sanity
mutations, D1–D8 the doc alignment. A **PIN-ONLY** iteration (the
v45-family's third): NO production-code change — the measured chrome
was already at parity on every VISIBLE layer; the pins lock it.
Validated against the codebase pre-execution (input.tsx:11 the class
stack, net-worth-view.tsx:105/:210 the mb-4 P, dialog.tsx:132 the
sheet's shadow-lg site; the spec idioms — the dialog-buttons
Add-Income opener, the networth beforeEach, the mobile-nav
Toggle-Sidebar + 700ms settle, the v35 focusVisible cast).

**Step 5 — TDD.** The three pins written and GREEN immediately
against the unchanged build (the pin-only discipline: the pin proves
the parity, the mutations prove the pin). The S1 mutations, each
verified to FAIL then restored: (a) the input's `focus-visible:ring-1`
removed → the F1 pin fails; (b) the input's `shadow-sm` removed → the
F1 pin fails; (c) the net-worth value `mb-4` reverted to `mb-2` → the
F2 census fails (the mb 16→8 AND the h 194→186); (d) the sheet's
`shadow-lg` removed → the F3 pin fails. **One execution lesson: the
first mutation (a) initially "passed" — the e2e suite runs against
the STANDALONE BUILD, not the source tree; every mutation needs
`npm run build` before the run can see it** (documented in the plan +
the probe README + the SKILL row).

**Step 6 — the full chain.** lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **226/226 e2e ✓ (5.2m, 223→226)** · 35/35 smoke ✓ (one
not-found flake in the first full run — the Go Home navigation test
passed in isolation and in the re-run; the standing-class resource
flake, not a regression). The VLM pair on the MOBILE /income view at
390 (a fresh surface — the reference's /income is overflow-free at
390, verified live): **3 flags, all DOM-verified as data/platform
classes** — the clone's richer seed carries a second income card
whose 4th (Recurring) badge wraps in the byte-identical `flex
flex-wrap gap-2` container (the reference's single-card data never
shows this; the badge row chrome measured identical: same container,
same per-badge geometry, single-row layout when the badges fit); the
"Edit with Base44" FAB is the reference's own platform chrome; no
chrome gaps (the v43 misattribution lesson, third application). The
16 screenshots regenerated (the capture script).

**Step 7 — the docs.** AGENTS.md (the v47 paragraph), CLAUDE.md (the
226 count + the three v47 insertions), README (the v47 row + the
counts), the SKILL doc (the Session 82 row + the state line), the PAD
(the v1.1.4 revision block), the probe README (the v47 section — the
three probes + the two drivers + the six lessons), session_107.md
(this log) + session_108.md (the raw transcript), the repo worklog
(the Session 81 entry + the ledger list), the workspace worklog.

**Step 8 — ship.** Commit + push to main via the SSH wrapper
(`docs/ssh_git_wrapper_v3.py` — the key materialized, the fingerprint
verified, the dry-run, the real push, the key shredded).

## The numbers

108 unit · 226 e2e (+3) · 35 smoke · 16 screenshots · 47 remediation
plans · 107 session docs · 4 mutations verified.

## Suggested next steps (the v48 queue candidates)

- The item-details sheet's action buttons' shadow family (the v28
  surface, the shadow-scale net's remaining sites — joined by the v47
  sixth site, the details sheet's buttons are the natural seventh).
- The toast's shadow family (the sonner toast — the clone's superset
  surface, unpinned).
- The empty-state cards' chrome (the v34-era surface, unpinned at the
  mobile viewports).
- The dialog input's focus composite at the MOBILE viewport (the v47
  pin is 1280-only; the 390 reflow of the same family).
- Or any new surface — the breakdown donut's sector stroke, the
  tablist's trigger chrome at 390, the login panel's input census.
