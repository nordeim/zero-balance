# Session 63 — Parity iteration v31 (session-61 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_61.md` / `docs/remediation-plan-v30.md`
/ `worklog.md` / `docs/session_62.md`. Full autonomy granted on the open
questions, so I worked the whole chain directly.

**Step 1 — workspace refresh.** The workspace had been RESET — the repo
re-cloned (`zero-balance` at `f9a9637`), `scandihaven` re-cloned, and the
environment rebuilt and re-verified: node_modules, `.env`
(`DATABASE_URL="file:../db/custom.db"`), the `db/` folder re-pushed +
re-seeded at the repo root. The five project docs + the four session docs
re-read; the codebase validated against them — the v30 changeset in place
(the 161-test suite, the details-sheet keyboard pins, the tablist roving
pin), verified by the full chain below.

**Step 2 — the audit.** The baseline chain green on the FIRST full run: lint
✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**161/161 e2e ✓** · 35/35 smoke ✓. Audit Phase 2 clean: the same 5 dev-only
ESLint `braces`/eslint-config-next advisories (no patched release —
accepted, dev-only), the secret-pattern scan matching only the documented
files, `.env.example` verified current.

**Step 3 — the two-site sweep** (agent-browser on the ref31/clone31
sessions + the :3200 parity server; the fresh-open + settle +
parked-pointer + real-click/real-hover/real-Tab disciplines throughout):

- **Mobile navigation (the task focus) R1–R4 all re-verified live on BOTH
  sites — the 25th consecutive check.** R1: the reference's two `fixed
  top-0 z-[100]` toast containers still intercept the burger's center hit
  (hit `DIV.fixed.top-0.z-[100]`, scrollWidth 395), while the clone's burger
  hit is DIRECT on the svg with 390 fit on every route. R2: the reference's
  sheet still traps after nav (overlay + `body overflow: hidden` measured on
  `/income` after the nav click; screenshot captured); the clone's closes
  (superset fix #2 — re-verified with the Radix `[role=dialog]` detector).
  R3: the reference marks nothing active on `/` and has no `<nav>` landmark;
  the clone highlights Dashboard + has the landmark. R4: the reference
  overflows 395 on `/`+`/dashboard` and 464 on `/networth` (one timing
  artifact caught: a 2.5s settle read the still-loading `/networth` as 390 —
  the 6s re-measure restored the documented 464); the clone fits 390 on all
  six routes. **The Tailwind v4 pins hold — the clone's mobile menu works as
  expected.**
- **Data drift clean (25th — the reference only read this session)**:
  allocation 30.5%, Balance `$3475.00`, income `$5000.00`/1 (Salary),
  savings `$1000.00`/1 (Emergency Fund), expenses `$525.00`/4.
- **SEO pair ✓ (the full head-metadata census)**: robots.txt +
  sitemap.xml live on both; description / og:title / og:description /
  og:type / twitter:card / twitter:title / twitter:description /
  apple-mobile-web-app-title / title byte-identical; canonical + og:image
  keyed off `NEXT_PUBLIC_SITE_URL`; charset + viewport present. The
  reference's `/manifest.json` endpoint 302s empty (broken); the clone's
  `manifest.webmanifest` serves the full v7-pinned document — a superset.
- **The filter selects' open-state arrow semantics (session-61 suggestion
  #2) — NO finding**: both sites' category filter is Radix
  (combobox/listbox/option with `data-highlighted`); ArrowDown moves the
  highlight, no wrap at the ends, ArrowUp back — identical roving on both
  (the option COUNT differs by data, not semantics).
- **The form dialogs' full Tab order (suggestion #3) — one finding (G2)**:
  the strict focusable census (tabindex property, aria-hidden + 1×1
  excluded) reads the SAME 14-field sequence on both sites; the reference's
  1×1 native-select shadows are not stops on either. The census delta: the
  reference's classification field renders TWO fresh stops (the radiogroup
  container AND the checked tile's radio at `tabindex=0`) — the clone's
  fresh state had all radios at −1. A REAL Tab into the group lands on the
  CHECKED item on both sites (the container's entry focus forwards
  instantly — measured live on both; activeElement never reads the
  container).
- **The dashboard donut's keyboard semantics (suggestion #1) — THREE
  recharts-3-vs-2.15 drifts (G1)**, measured at the computed + live
  behavior level: (a) the clone's `svg.recharts-surface` carried
  `tabIndex=0` + `role="application"` (recharts 3's a11y layer defaults ON)
  and rendered the browser's unpinned 5px auto ring when focused — the
  reference's surface is inert (no attribute, no role); (b) the clone's
  tooltip default content carried `role="status"` +
  `aria-live="assertive"` — the reference's carries neither; (c) recharts 3
  REMOVED 2.15's `attachKeyboardHandlers` pie roving — the reference's pie
  layer (tabIndex=0 on BOTH versions, `rootTabIndex: 0` — parity there)
  roves sector focus on ArrowLeft (`++n % len` forward) / ArrowRight
  (`--n < 0 → len-1` BACKWARD — the first ArrowRight focuses the LAST
  sector) / Escape (blur + reset); the clone's arrows did nothing. The
  recharts 2.15.3 source was installed and read in a scratch dir to pin the
  exact contract (the `attachKeyboardHandlers` body, `rootTabIndex: 0`,
  the surface attrs only under an explicit `accessibilityLayer`).
- **The VLM pairwise (two fresh pairs)**: the dashboard — flags all
  DOM-explained (the clone's Dashboard-active rail = superset #3; the
  allocation-bar length + avatar initial = seeded data); the add-income
  dialog — flag DOM-explained (the clone's X renders its v27-pinned ring-1
  on open because Radix focuses it — the documented v29 superset; computed
  arbitration: both X's byte-identical at rest, 36×36 / border 0 / radius
  6 / transparent / no outline).
- Probe-methodology lessons (persisted in the probe README): re-measure
  overflow with a 6s settle before declaring drift; scope the dialog-X
  finder to the topmost fixed overlay; SVG elements without a tabindex
  attribute read `.tabIndex === -1` — distinguish attribute-absent from
  attribute −1.

**Step 4 — the plan + TDD.** `docs/remediation-plan-v31.md` written and
validated against the codebase (grep-verified: no existing
surface/a11y/roving assertions in the specs, the RadioGroup surface, the
ArrowRight precedent). TDD: the G1 tests written → RED (both fail on the
drifted implementation) → `accessibilityLayer={false}` +
`usePieKeyboardParity` → GREEN → the G2 test → RED (checked radio reads
−1) → `tabIndex={selected ? 0 : -1}` → GREEN. **Pin-sanity mutations**
(a11y prop removed → test 1 fails; the roving wrap broken → test 2 fails;
the tile prop flipped to −1 → test 3 fails) → all FAIL → restored → GREEN
again. Two typecheck fixes along the way (the test evaluate return type;
the second from the G2 walk's stop typing).

**Step 5 — the chain.** **FULL CHAIN GREEN: 108 unit · 164 e2e · 35
smoke** + lint + typecheck + build (the suite went 161 → 164: G1 adds two
tests, G2 one). Live re-verification on the :3200 parity server: the
surface census reads `tabindex=null / role=null` (byte-identical to the
reference), the tooltip's inner div carries no attributes, the arrow walk
reproduces the reference's exact sequence (layer → ArrowRight → sector →
Escape → BODY), and the tiles' fresh census reads container 0 + checked 0 +
unchecked −1 — all byte-identical to the reference measurements. The 16
screenshots regenerated (zero visual change — both fixes are
keyboard/DOM-attribute level).

**Step 6 — docs + ship.** The probe README (the v31 catalog + the
lessons), README (the v31 row + the 164 counts), CLAUDE.md (the e2e
description), AGENTS.md (the v31 verification paragraph), the SKILL doc
(the session row + the 164-test state), this session log, the raw
narrative (`docs/session_64.md`), the worklog.

## What this session did

- **Workspace re-cloned (the sandbox reset) + environment rebuilt and
  re-verified**; the baseline chain green on the first full run
- **Standing checks all clean (25th consecutive)**: mobile-nav R1–R4 on
  both sites — **Tailwind v4 pins hold, the mobile menu works**; data drift
  clean (reference read-only); the SEO pair live (full head census
  byte-identical; the reference's broken manifest endpoint documented)
- **The session-61 suggested surfaces resolved with first-time keyboard
  measurements**: the filter selects' arrow semantics (NO finding —
  identical Radix roving), the dialog forms' full Tab order (one finding:
  the tiles' fresh roving state), and the donut's keyboard semantics (the
  recharts-3-vs-2.15 drift trio — the a11y-layer surface/role/tooltip
  semantics + the missing sector roving)
- **TWO fixes, three pin tests** (`docs/remediation-plan-v31.md`):
  `<PieChart accessibilityLayer={false}>` + `usePieKeyboardParity` (the
  recharts-2.15 roving contract replicated exactly, including the
  backwards-wrap quirk) + `tabIndex={selected ? 0 : -1}` on the
  classification tiles — TDD with pin-sanity mutations, all
  live-re-verified byte-identical
- Full chain **108/164/35 green**; docs/screenshots/worklog aligned;
  committed and pushed to main via the SSH wrapper

**Suggested next steps**: the keyboard-semantics sweep pattern still has
unmeasured families — the net-worth card action dropdown menus' keyboard
contract (Radix Menu's arrow/typeahead/Escape), the calculator line-item
row actions' Tab order, and the breakdown accordion's arrow semantics;
alternatively the performance/correctness audit pass (Lighthouse, bundle
sizes, the API's error-tier coverage). Just re-issue the brief referencing
`docs/session_63.md` / `docs/remediation-plan-v31.md` and I'll pick it up
from there.
