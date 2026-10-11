# Session 101 — Parity iteration v45: the shadow-scale sweep + the items-view card grid census + the calculator row hover (2026-10-11)

**Goal:** the session-99/100 queue — the items-view card grid at 1280
(unmeasured), the calculator line-item row's hover, the category-level
animation pin, and whatever the sweep finds. TDD-first, docs aligned,
commit + push via the SSH wrapper.

## What was done

**Step 0 — the workspace.** Intact this session: `git pull`
fast-forwarded 31b275d → e327b57 (the session_100.md log) — the
environment survived (node_modules, db/, the playwright browsers, .env
≡ .env.example). The five core docs + the session docs re-reviewed.

**Step 1 — the baseline chain.** lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · **214/214 e2e ✓ (4.9m, the
first run)** · 35/35 smoke ✓. npm audit = the same 5 dev-only
ESLint-chain advisories; the secret scan clean (the docs reference
files only); the tree clean.

**Step 2 — the 39th standing checks.** Reference side: R1 the
toast-blocker still intercepts the burger, R2 the sheet still traps, R3
no nav landmark, R4 the 395 overflow — all four reference bugs still
live; the data census read-only (identical before + after); the SEO
pair live. Clone side (inside one with-server.sh): R1 the burger hit
direct, R2 the sheet closes after nav, R3 the nav landmark present, R4
zero overflow; the sheet structure intact; the SEO pair live. **All
clean — the superset intact.**

**Step 3 — the v45 sweep (the queue's surfaces, measured live on BOTH
sites).** Probes: `items-card-v45.mjs` (the items-view card census) +
`calc-row-v45.mjs` (the calculator row) + the REAL-hover driver steps +
`vlm-compare-v45.mjs`. The sweep:

- **THE SHADOW-SCALE DISCOVERY** (opened by the calculator row's hover):
  a SYSTEMIC v3↔v4 divergence in the computed box-shadow composition —
  every live `shadow-*` utility's VISIBLE layers match on BOTH sites
  (the `--shadow-sm` theme pin is load-bearing for the small end: v4
  RENAMED the scale, its native shadow-sm = v3's "shadow"; the pin
  restores `0 1px 2px 0 rgb(0 0 0 / 0.05)` — measured matching on the
  Google-button hover, the slate submit, the dialog inputs) while the
  LEAD layers diverge by construction (v4's 5-slot composition emits 4
  transparent leads vs v3's 2 — e.g. the calculator row's hover: the
  reference reads `rgba(0,0,0,0)×2 + rgba(0,0,0,0.1) 0 4px 6px -1px +
  rgba(0,0,0,0.1) 0 2px 4px -2px` (4 layers), the clone 6 layers with
  the same 2 visible — invisible, the accepted v10/v25 class). The
  md/lg/xl/2xl numerics were NOT renamed and were UNPINNED — v45 pins
  the md/lg/sm/2xl sites as the regression net. The shadow survey
  covered: the calculator row's hover (md), the expense-card action
  buttons' rest (md), the quick-action card's hover (lg), the login
  panel (2xl), the details sheet (2xl), the Google button's hover (sm),
  the slate buttons (sm), the dialog inputs (sm), the white pills (sm),
  the mobile sheet (lg), the login logo (lg/xl) — plus the
  inert-by-construction family (the item/net-worth cards' inline
  boxShadow beats their hover:shadow-lg on BOTH sites — the v29 family,
  DOM-identical) and the `.zb-modal-panel`'s explicit single-layer
  shadow (visible ✓, leads absent — the same accepted class).
- **The items-view card census at 1280: BYTE-IDENTICAL** — the grid 960
  (the rail 256 + the content column 1024 − the p-8 64 — the SAME
  arithmetic on both sites), 3 cols × 309.328, gap 16; the card
  309/pad 20/radius 12/border 1px rgb(229,231,227)/the rest shadow
  `rgba(0, 0, 0, 0.04) 0px 2px 8px 0px` (Chrome normalizes the clone's
  3-value inline and the reference's inline to the SAME string)/
  transition all 0.2s; the title row gap 8/dot 8×8/title 16-600; the
  income kebab 36×36 opacity 0; the expense action row top 12/right
  12/gap 8/btn 32/padX 12/12px; **the card's REAL hover INERT on BOTH
  sites** (the inline boxShadow beats hover:shadow-lg) while the action
  row REVEALS. The card heights differ (230 vs 200) — DATA (the notes
  rows), the v43 +36 class. sw 1280 on both.
- **The calculator row census + REAL hover: BYTE-IDENTICAL** — the
  panel 768@1280/608@640, the row 720/560, pad 16, radius 12, border,
  rest-shadow none, transition all 0.15s; the action pair opacity 0 /
  32px. Under a REAL hover (agent-browser `hover` — the synthetic
  dispatchEvent CANNOT engage :hover, the first draft's trap): the
  shadow-md's visible layers identical on both sites + the action
  reveal. The reference's RENT calculator is the only one of its four
  expense cards with line items ("Contents Insurance"); the clone's row
  was API-created and restored (delete + PATCH the parent — the
  calculator rule sets the parent to the line-items SUM; deleting alone
  recalcs to 0).
- **The category-level band animation works on the clone** (the v44
  Collapse at the nested level): 441→453→463→479→484→491→493→495 on the
  expand, the reverse on the collapse — in-flight frames both
  directions. Unpinned before v45.

**Step 4 — the plan.** `docs/remediation-plan-v45.md` — F1 (the
items-card census pins), F2 (the calculator row census + hover pins),
F3 (the category-animation + quick-action shadow pins), F4 (the
shadow-scale regression pins), S1 (five mutations), D1–D8. **A PIN-ONLY
iteration — no production-code change** (the measured chrome was
already at parity; the pins lock it).

**Step 5 — TDD.** The seven e2e tests written first (F1a/F1b items, the
F2a/F2b calculator, the F3a/F3b dashboard, the F4 login). The F2 pair's
first run failed on a missing describe-level beforeEach (no
`page.goto("/expenses")` — the rent locator timed out; a test-layer
fix). The build's typecheck caught a TS union in the F3a evaluate's
early return (fixed by widening the shape — `next build` typechecks the
spec files too). All seven GREEN against the unchanged build — the
pin-only contract. Then the five mutations, each verified to FAIL:
(a) the card inline 0.04→0.08 → F1a fails; (b) the grid gap-4→gap-6 →
F1a+F1b fail; (c) the row hover:shadow-md removed → F2a fails; (d) the
quick-action hover:shadow-lg removed → F3b fails; (e) the slate
shadow-sm removed → F4 fails. All restored → GREEN.

**Step 6 — the full chain.** lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **221/221 e2e ✓ (5.2m — 214 → 221)** · 35/35 smoke ✓. The 16
screenshots regenerated. The VLM pair on the /income items-view at
1280: **IDENTICAL, zero flags — the first fully-clean screening since
the pair began.**

**Step 7 — the docs.** AGENTS.md (the v45 paragraph), CLAUDE.md (221 +
four v45 insertions), README (the v45 row + the counts), the SKILL doc
(the Session 80 row + the state line + the command + the three-tier
row), the PAD (the v1.1.2 revision block), the probe README (the v45
section — six lessons), session_101.md (this log) + session_102.md (the
raw transcript), the repo worklog (Session 79 + the ledger list), the
workspace worklog.

**Step 8 — ship.** Commit + push to main via the SSH wrapper
(`docs/ssh_git_wrapper_v3.py` — the key materialized, the fingerprint
verified, the dry-run, the real push, the key shredded).

## The numbers

108 unit · 221 e2e (+7) · 35 smoke · 16 screenshots · 45 remediation
plans · 102 session docs · 5 mutations verified.

## Suggested next steps (the v46 queue candidates)

- The net-worth ASSET/LIABILITY card hover at 1280 (the same
  inline-beats-utility family — its rest shadow is pinned, its action
  buttons' shadow-md is not).
- The dialog inputs' focus-state shadow composition (the ring+shadow
  layer interaction under focus — the reference's v3 composed string vs
  the clone's; the visible layers are pinned via the v13/v25 families,
  the full composition is not).
- The white pills' shadow-sm sites (the five pill badges' rest shadows —
  the same shadow-scale regression net, unpinned).
- Or any new surface — the net-worth tabs' hover, the sheet's shadow-lg
  at 390, the toast's shadow family.
