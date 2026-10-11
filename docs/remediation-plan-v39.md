# Remediation Plan v39 — The A11y Gate's MOBILE Extension (the 390×844 Sheet-State Scan)

Date: 2026-10-11 · Scope: fresh two-site re-audit after the v38 baseline
(`5592038` + the session-log commits `0fdb303`/`a2d5381` on `main`; this
session re-cloned the reset workspace and rebuilt the environment:
npm install → `cp .env.example .env` → db:push + db:seed). Baseline chain
on the re-run: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots +
sitemap prerendered) · **187/187 e2e ✓ (4.0m)** · 35/35 smoke ✓; npm
audit = the same 5 dev-only ESLint `braces` advisories — accepted,
unchanged, dev-only; the secret-pattern scan clean (src/tests/scripts);
`.env.example` verified current. NOTE: the FIRST full e2e run of the
session flagged ONE flake — `not-found.spec.ts › Go Home navigates to the
dashboard` failed a `toBeVisible` at 11.1s — it passed in isolation AND
in the full re-run (a first-run-after-rebuild warm-up timing artifact,
not a regression; the 33rd standing checks + both mobile scans below ran
against the same build and show no drift).

The sweep — method and results: the v38-queue headline surface (the a11y
gate's MOBILE extension — a 390×844 scan of the sheet-open state, the
session_80/81 suggested queue's third item), plus the standing
re-verification set (mobile-nav R1–R4 on BOTH sites, data drift, the SEO
pair, one VLM pair) and the code audit.

- **Mobile navigation (the standing task focus) R1–R4 all re-verified
  live on BOTH sites — the 33rd consecutive check.** R1: the reference's
  toast containers still intercept the burger's center hit
  (`DIV.fixed.top-0.z-[100]`, scrollWidth 395); the clone's hit DIRECT on
  the svg, fits 390. R2: the reference's sheet still traps after nav
  (sheet open, body locked on /income); the clone's closes. R3: the
  reference marks nothing active on `/` and has no `<nav>`; the clone
  has the landmark. R4: the reference overflows 395 on `/`+`/dashboard`;
  the clone fits 390 on all routes. **The Tailwind v4 pins hold — the
  mobile menu works as expected.**
- **Data drift clean (33rd)**: the reference's census re-verified BEFORE
  and AFTER all probes (allocation 30.5%, income `$5000.00`, savings
  `$1000.00`, expenses `$525.00` — unchanged; read-only throughout: the
  a11y scans inject + read only, the sheet probes Escape-close). The
  clone's seed census unchanged (62.8% / 5550 / 1250 / 2235).
- **SEO pair ✓** (live, both sites): robots.txt (allow-all + the
  sitemap line) + sitemap.xml (five URLs, priority 1.0/0.8, weekly) live
  on both; the reference's sitemap still capitalizes its app-route URLs
  (`/Income`, `/Savings`) while the clone mirrors its own lowercase
  routes (the documented v21 decision).

## The v39 surface — the a11y gate's mobile extension (first-time measured live on BOTH sites)

Measured with `a11y-scan-v39.mjs` (the v38 scanner extended with the
mobile emulation — 390×844, `isMobile: true`, `hasTouch: true`, the
mobile-navigation.spec.ts contract) + `axe-detail-v39.mjs` /
`axe-detail-ref-v39.mjs` (the per-node color enumeration):

- **The reference at 390×844 (sheet closed)** fails `button-name`
  (CRITICAL) on /income + /expenses + /savings (2–3 nodes each: its
  unlabeled Select triggers `button[aria-controls=radix-:r…:]` + the
  card kebab `#radix-…`) and on /networth (the kebab), plus
  `svg-img-alt` (SERIOUS, 3 nodes) on `/` + `/dashboard` (its recharts
  donut sectors `path[name="Need"/"Savings"/"Want"]`), plus
  color-contrast (14 nodes on `/`+`/dashboard`, 1 on /income, 4 on
  /expenses, 2 on /networth — its demo card counts).
- **The clone at 390×844 (sheet closed)** passes `button-name` and
  `svg-img-alt` on EVERY route — its ONLY failures are color-contrast:
  14 nodes on `/`+`/dashboard` (the same node-for-node family as
  desktop), 2 on /income (the 2 card amounts — the reference's 1 is its
  single-card demo data), 3 on /expenses (3 cards), 0 on /savings, 4 on
  /networth (the inactive Liabilities tab + the 3 asset-card amounts —
  the reference's 2 is its single-asset demo data). **GATE 2 provenance:
  every flagged color enumerated and in the reference's own 7-color
  palette** (lime `rgb(143,188,63)` / blue `rgb(59,126,161)` / orange
  `rgb(224,122,59)` / orangeLight `rgb(245,169,98)` / gray-500
  `rgb(107,114,128)` / zinc `rgb(115,115,115)` — the mobile node counts
  differ from desktop only by the demo data's card counts).
- **The sheet-OPEN structural census (the headline)**: the reference's
  mobile sheet is a plain `fixed` div — **NO dialog role, NO
  aria-labelledby, NO `<nav>` landmark, NO accessible title** (its 5
  links are bare anchors in a div; measured by the ref-v39.sh sheet
  probe + a11y-scan-v39.mjs's structure phase). The clone's sheet is a
  Radix Dialog: **`role="dialog"` + `aria-labelledby` → the sr-only
  "Navigation" DialogTitle + `<nav aria-label="Primary">` + the 5 links
  + the named burger** (the sr-only "Toggle Sidebar" span). The
  sheet-open scan on the clone adds ZERO violations beyond the 14
  color-contrast baseline; the reference's sheet-open scan shows the
  same color-contrast-only profile.
- **The VLM pairwise (one fresh pair, 390×844)**: the mobile
  sheet-open state — VERDICT DIFFERENT with BOTH flags explained: (1)
  the clone's Dashboard link carries the active highlight (superset fix
  #3 — the reference marks nothing active on `/`, its R3 bug); (2) the
  avatar letter U vs D (the different demo users). Zero unexplained
  visual drift.

## Findings

### F1. [SUPERSET — pin] the clone's MOBILE a11y gate (the v38 gate extended to the mobile viewport)

The v38 desktop gate pinned the clone as a structural a11y superset;
the v39 measurement proves the same holds at the mobile viewport AND
for the mobile navigation sheet itself. This session pins that state as
8 new e2e tests (`tests/e2e/a11y.spec.ts`, a new describe with
`test.use({ viewport: { width: 390, height: 844 }, hasTouch: true,
isMobile: true })` — the mobile-navigation.spec.ts emulation):

1–6. the six authed routes, sheet-closed, scanned under the SAME two
gates (GATE 1: no violation id other than color-contrast; GATE 2: every
flagged color in the reference's 7-color palette — the shared
`assertParityClean` helper).
7. the sheet-OPEN state on `/`: a REAL click on the burger (the clone's
toast viewport never blocks it), then the structural pins —
`role="dialog"`, the `aria-labelledby` resolving to an element whose
text is "Navigation", the `<nav aria-label="Primary">` with the five
links, the sheet's close behavior — then the scan under both gates.
8. the logged-out MOBILE login page (its own storageState-opt-out
sub-describe) asserting ZERO violations.

### S1. [MUTATION-SANITY] the burger's sr-only label and the sheet's DialogTitle

Two mutations verify the new pins bite:
(a) strip the MobileTopbar burger's `<span className="sr-only">Toggle
Sidebar</span>` + rebuild → the mobile `/` scan's GATE 1 FAILS
(`button-name` fires on the now-nameless burger).
(b) remove the sheet's `<DialogTitle className="sr-only">Navigation`
</DialogTitle>` + rebuild → the sheet-open test's structural pin FAILS
(the `aria-labelledby` no longer resolves to a titled element).
Both restored → GREEN.

### T2. [TOOLING] the v39 probes persisted + the README section

`a11y-scan-v39.mjs` (both sites, mobile), `axe-detail-v39.mjs` /
`axe-detail-ref-v39.mjs` (the mobile color provenance), `ref-v39.sh` /
`clone-v39.sh` (the 33rd standing checks + the sheet-structure probes),
`vlm-compare-v39.mjs` (the mobile sheet pair) — plus the probe README's
v39 section (the lessons: the agent-browser daemon can wedge after a
killed parity server — `pkill agent-browser` restarts it cleanly; the
JS-click workaround for the reference's toast-blocked burger).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | The mobile a11y gate: 8 tests (6 authed routes + the sheet-open structural pins + the logged-out login sub-describe) | test | `tests/e2e/a11y.spec.ts` |
| 2 | S1(a) pin-sanity: strip the burger's sr-only span → the mobile `/` GATE 1 FAILS; restore → GREEN | verify | `src/components/budget/sidebar.tsx` |
| 3 | S1(b) pin-sanity: remove the sheet's DialogTitle → the sheet-open structural pin FAILS; restore → GREEN | verify | `src/components/budget/sidebar.tsx` |
| 4 | The full chain re-run (108 unit · 195 e2e · 35 smoke + lint + typecheck + build) | verify | — |
| 5 | The 16 screenshots regenerated | docs | `docs/screenshots/` |
| 6 | The v39 probes persisted (the 5 scripts above) + the probe README's v39 section | docs | `scripts/parity-probes/` |
| 7 | Docs aligned (README v39 row + counts, CLAUDE.md the mobile-gate entry, AGENTS.md the v39 paragraph, SKILL state line + session row, session_83.md, the repo worklog Session 74, the workspace worklog) | docs | repo root + `docs/` |
| 8 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `tests/e2e/a11y.spec.ts` (118 lines): the v38 file holds the shared
  `assertParityClean` helper (GATE 1 + GATE 2 + the 7-color
  `PARITY_PALETTE` + the `TAGS` set) — the v39 describe reuses it
  verbatim; the insertion point is the file's end (after the login
  describe). `test.describe` merges `test.use` options: the outer v39
  describe sets the viewport/isMobile/hasTouch; the logged-out
  sub-describe adds the storageState opt-out (the v38 hoisting lesson —
  `test.use` is hoisted PER describe, so the opt-out never leaks to the
  authed tests).
- The authed markers (the seed content waits) are the v38 pairs:
  `Total Income` on /+/dashboard, `Salary` on /income, `Rent` on
  /expenses, `Emergency Fund` on /savings, `Assets` on /networth.
- `src/components/budget/sidebar.tsx`: the MobileTopbar burger
  (lines ~221–238) carries `<span className="sr-only">Toggle
  Sidebar</span>` — the S1(a) mutation removes that span; the sheet
  (lines ~192–205) renders `<DialogTitle className="sr-only">
  Navigation</DialogTitle>` inside `SheetContent` — the S1(b) mutation
  removes that element. Radix only sets `aria-labelledby` on the
  DialogContent when the DialogTitle mounts, so (b) breaks the
  labelledby resolution exactly as the pin asserts.
- The burger click in test 7: the mobile-navigation.spec.ts idiom —
  `page.getByRole("button", { name: "Toggle Sidebar" })` (the sr-only
  span IS the accessible name), then wait for the
  `[data-state=open]` sheet. The clone's toast viewport is
  pointer-events: none — a REAL Playwright click works (superset fix
  #1; the JS-click workaround is only needed on the reference, whose
  toast container intercepts hit-testing).
- The scan settles: the authed routes wait the marker + 2500ms (the
  v15 loading-overlay contract); the sheet-open test settles 1200ms
  after the burger click (the probe-measured sheet-open timing).
- The login sub-describe: the v38 zero-violation idiom (no allow-list)
  at the mobile viewport — the v24-pinned mobile auth chrome (44px
  sign-in controls) scans clean.
- The chain gate: lint → typecheck → 108 unit → build → 187 e2e (195
  after the 8 v39 tests) → 35 smoke. The 8 mobile scans add ~45s (each
  ~5s incl. settles; the sheet-open test ~8s with the interaction).
