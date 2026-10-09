# Remediation Plan v29 — Session-57 Parity Iteration

Date: 2026-10-10 · Scope: fresh two-site re-audit after the v28 baseline
(`d622f2e` + the session-58 log doc through `34b4970` on `main`, all green
per this session's re-run: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓
(robots + sitemap prerendered) · **158/158 e2e** ✓ (one transient
not-found-spec flake on the first full run under fresh-sandbox load;
isolated re-run + full third run green) · 35/35 smoke ✓). The workspace
was re-cloned fresh (the sandbox reset); the environment restored and
re-verified (`.env` with `DATABASE_URL="file:../db/custom.db"`, `db/`
at the repo root re-pushed + re-seeded — 7 budget items, 3 assets, 2
liabilities for `demo@zerobalance.app` — node_modules reinstalled, the
scandihaven pattern repo re-cloned). Probes: the standing disciplines —
one-shot `agent-browser eval` (base64-encoded via run-probe.sh), the
:3200 parity server inside ONE `with-server.sh` invocation, REAL CDP
hovers via `mouse move` (synthetic events never engage `:hover`), REAL
ref clicks for Radix triggers, full computed strings (never truncated).

## The sweep — method and results

The pass swept the session-57 log's four suggested surfaces — the
**details sheet's keyboard semantics**, the **VLM pairwise of the new
details capture**, the **edit-dialog entry-point consistency**, and the
**net-worth view interactive-family census** (never class-diffed) — plus
the standing re-verification set (mobile-nav R1–R4 on BOTH sites, data
drift, the SEO pair, the v28 fix in place) and the code audit
(lint/tsc/tests green; `npm audit` = the same 5 dev-only ESLint `braces`
advisories — accepted, unchanged; the secret-pattern scan matching only
the documented files; the v28 changeset re-verified in the tree: the
`item-details-dialog.tsx` component + the store's `details` slot + the
card's guarded onClick + the app-shell mount + the `.zb-badge-hover` pin
+ the four badge class strings + the two button strings).

- **Mobile navigation (the task focus) R1–R4 all re-verified live on BOTH
  sites — the 23rd consecutive check.** R1: the reference's two `fixed
  top-0 z-[100]` toast containers still intercept the burger's center
  hit at (38,30) (`pe:auto`, 390×32, z-100; scrollWidth 395 on `/`),
  while the clone's burger hit is DIRECT on the svg with the viewport
  `pe:none` and 390 fit on every route. R2: the reference's sheet still
  traps after nav; the clone's closes (superset fix #2). R3: the
  reference marks nothing active on `/` and has no `<nav>` landmark;
  the clone highlights Dashboard + has the landmark (the documented
  superset). R4: the reference overflows 395 on `/`+`/dashboard` and 464
  on `/networth`; the clone fits 390 on all six routes. **The Tailwind v4
  pins hold — the clone's mobile menu works as expected.**
- **Data drift clean (23rd)**: the reference unchanged (allocation 30.5%,
  Balance `$3475.00`, income `$5000.00`/1, savings `$1000.00`/1, expenses
  `$525.00`/4). No probe items were created this session (the reference
  was only read).
- **SEO check (the brief's standing ask) PASSES**: both sites serve
  `/robots.txt` (allow-all + the sitemap link) and `/sitemap.xml` (the
  route set; `/login` excluded on the clone).
- **The details sheet's keyboard semantics (session-57 suggestion #1)
  — NO parity gap; the clone is the accessible superset (documented):**
  the reference's sheet is a plain-div overlay — NO initial focus
  (activeElement stays BODY), NO `role`/`aria-modal`, and a real Tab
  walk walks the ENTIRE underlying page (stops 1–14 measured: the five
  sidebar links, Add Expense, the three filter triggers, then the
  cards' Edit/Calculate buttons) — the sheet never traps focus and its
  single focusable (the X) is reachable only after every page element.
  The clone (Radix) opens with initial focus ON the X (which renders
  the pinned 1px `#0a0a0a` ring — Chrome applies `:focus-visible` to
  the programmatic focus), traps all Tab stops inside, and closes on
  Escape. All measured live on both sites. **Superset — no change.**
- **The VLM pairwise of the details sheet (suggestion #2)**: the pair
  (`/tmp/vlm29/ref-item-details.png` vs the clone's capture) returned
  DIFFERENT with two flags, both explained by the DOM: (a) the clone's
  X shows a box — that is the Radix initial-focus ring (above), which
  the reference renders identically when its X is actually Tab-focused
  (the v27-pinned family); (b) the fact-row count/height differs —
  data-driven (the reference capture's item vs the clone's Rent: Notes
  + Payment Method presence changes the row count; both panels are the
  measured `max-h-[85vh] overflow-y-auto` contract). **No class-level
  drift — no change.**
- **The edit-dialog entry-point consistency (suggestion #3) — NO
  finding**: the reference's income-card ellipsis menu (Edit/Delete,
  opened via a real ref click) and the expense-card's hover-revealed
  footer Edit both open the **same "Edit Budget Item" dialog** (the
  identical 14-label field set — Type, Amount, Classification,
  Need/Want/Savings, Category, Subcategory, Frequency, Date, Payment
  Method, Status, Recurring Item, Notes — pre-filled per item). The
  clone's single shared `BudgetItemDialog` already does exactly this.
- **The net-worth view interactive-family census (suggestion #4 — never
  class-diffed; the bulk of this session's measurements)**:
  - The **tab triggers**: the reference's active trigger carries the
    shadcn base + `data-[state=active]:bg-green-100
    data-[state=active]:text-green-900` (computed `rgb(220,252,231)` /
    `rgb(20,83,45)`); the clone's byte-identical computed values via
    the hex-pin (`bg-[#dcfce7] text-[#14532d]` — the documented
    oklch-drift superset, v5 G3). The tablist container, width (448),
    muted bg `rgb(245,245,245)`, and 2-col grid all identical. ✓
  - The **Add Asset/Add Liability buttons**: the `zb-btn-add` pin +
    `ADD_BUTTON_GRADIENTS` (forest→lime / orange→peach) — computed
    byte-identical to the reference's measured gradients. ✓
  - The **asset/liability card containers**: `group rounded-xl border
    bg-white p-5 transition-all duration-200 hover:shadow-lg` + the
    inline `rgb(229,231,227)` border + `rgba(0,0,0,0.04) 0 2px 8px`
    shadow — identical; card cursor `auto` on BOTH sites (neither
    opens anything on card click — measured: the reference's asset
    card click opens NOTHING, unlike the budget items' details sheet;
    the clone's AssetCard has no onClick — parity). ✓
  - The **card action dropdown menu** (never diffed): the panel
    (`z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover
    p-1 text-popover-foreground shadow-md`), computed border `1px
    rgb(229,229,229)`, radius 6px, min-width 128px, the real
    shadow-md layers, the item base (`px-2 py-1.5 text-sm` 32px tall),
    Edit `rgb(10,10,10)` + Delete `rgb(220,38,38)` — all
    **byte-identical** (the clone's extra `border-input` class and
    v4 `[&_svg]` selector syntax compute identically — the v13
    rendered-parity precedent). ✓
  - The **type labels — THE FINDING (G1 below)**: the reference's
    asset-card type label is a DIV carrying the full shadcn **Badge
    base** — `transition-colors focus:outline-none focus:ring-2
    focus:ring-ring focus:ring-offset-2 border-transparent
    hover:bg-secondary/80 bg-gray-100 text-gray-700 text-xs` — with
    rest computed **`rgb(243,244,246)`** bg / **`rgb(55,65,81)`** text
    and, on a REAL CDP hover, the tint **`rgba(245, 245, 245, 0.8)`**
    over 150ms (measured live — the exact v28 G1 family on a surface
    that had never been diffed). The clone's label is a static span
    (`bg-gray-100 text-gray-700`) whose rest colors compute as **oklab**
    (`lab(96.1596 -0.0823438 -1.13575)` / `lab(27.1134 -0.956401
    -12.3224)` — the TW4 oklch drift, unpinned here) and which has NO
    hover family. → **G1**.
  - The reference's **liability panel holds 0 items** (its user data has
    no liabilities — only the pinned empty state renders), so the
    liability-card label family is unmeasurable on the reference; the
    clone's LiabilityCard label is the sibling implementation and takes
    the same fix for family consistency (the reference's shared Badge
    component implies the same family).
  - **The dashboard's breakdown nested-row hover — checked and NO
    finding**: the reference's nested rows carry the same
    `hover:bg-gray-100` + inline `background-color: rgb(249,250,251)`
    the clone has — and a REAL CDP hover leaves BOTH at
    `rgb(249,250,251)`: the inline style overrides the hover class on
    BOTH sites (the class is inert on both — rendered parity). The
    oklch computation never renders on either site.
- Probe-methodology notes: the reference's Radix-style TAB TRIGGERS do
  not respond to synthetic `element.click()` (only real ref clicks
  switch panels — the same v28 real-click lesson, now measured for
  tabs); the clone's details dialog exposes its X via the sr-only
  "Close" span (no aria-label — match `textContent` when probing); and
  Chrome applies `:focus-visible` to Radix's programmatic dialog-open
  focus, so the pinned X ring RENDERS in the open state (the reference's
  BODY-focus leaves its X ringless — the superset's visible signature).

### G1. [MED] The net-worth card type labels' rest colors + hover family — pin the reference's exact computed values

The reference's asset-card type label ("Bank Account") carries the full
shadcn Badge base: rest bg `rgb(243,244,246)` (gray-100 v3 hex), text
`rgb(55,65,81)` (gray-700 v3 hex), and on REAL hover the tint
`rgba(245,245,245,0.8)` over 150ms. The clone's spans compute oklab
rest colors (the TW4 drift — this surface was never pinned) and have no
hover family. This is the same fix family as v28 G1 (the item-card
badges), applied to the net-worth view's two label sites.

**Fix (executed — `src/components/budget/net-worth-view.tsx`, the two
label class strings at ~lines 74 and 178):** each label gains
`bg-[#f3f4f6] text-[#374151]` (computing the reference's exact
`rgb(243,244,246)` / `rgb(55,65,81)`) + `transition-colors
zb-badge-hover` (the existing v28 globals.css pin — the hover computes
`rgba(245,245,245,0.8)` byte-identically; the direct
`hover:bg-secondary/80` utility is NOT used — the v7 G6/v28 oklab
lesson). The reference's inert focus classes (`focus:outline-none
focus:ring-2 focus:ring-ring focus:ring-offset-2`) are NOT added —
non-focusable spans render nothing on both sites (the v13
tag-difference precedent: rendered parity is the bar; the clone's SPAN
vs the reference's DIV is the same precedent — identical rendering).

## Validation of this plan against the codebase

- The two label sites: `rg 'bg-gray-100 text-gray-700' src/` returns
  exactly two hits — `net-worth-view.tsx:74` (AssetCard) and
  `:178` (LiabilityCard). No other component renders this string (the
  dashboard's `hover:bg-gray-100` at dashboard-view.tsx:282 is the
  breakdown row — a different, verified-inert-on-both surface).
- The existing pins to reuse: `.zb-badge-hover` already in
  `globals.css` (the v28 G1 pin — plain CSS, applies to any element);
  the hex-pin pattern (`bg-[#f3f4f6]`) is the established
  tabs-trigger/summary-card discipline (networth.spec G9 asserts
  computed plain-rgb strings).
- The existing spec coverage: `tests/e2e/networth.spec.ts:187-189`
  currently asserts `bg-gray-100` + `text-gray-700` on the Bank Account
  badge — these assertions are updated to the pinned classes + new
  computed-color assertions (the G9 pattern), plus the hover-family
  class assertions (the v28 items.spec pattern). No other spec touches
  these labels (`rg 'bg-gray-100' tests/` → only the networth badge
  line + the dashboard breakdown row's own assertions).
- The e2e cost: extends the existing networth spec (no new page flows,
  no new spec file) — the suite count stays 158.

## Execution order (TDD)

1. **RED (G1)**: update the networth spec's badge assertions —
   `bg-[#f3f4f6]`, `text-[#374151]`, `transition-colors`,
   `zb-badge-hover`, and computed `rgb(243,244,246)` bg /
   `rgb(55,65,81)` color (both cards' labels; the G9 computed pattern).
   Run → RED (the current classes are `bg-gray-100 text-gray-700` and
   the computed values are oklab).
2. **G1 fix**: the two class-string edits in `net-worth-view.tsx`.
   Run → GREEN.
3. **Pin-sanity (G1)**: mutate one expectation (drop `zb-badge-hover`,
   flip the hex) → FAIL → restore.
4. Full clean-check chain: `npm run lint && npm run typecheck && npm
   test && npm run build && npm run test:e2e` + `bash
   scripts/smoke-test.sh` (158 e2e expected).
5. Live re-verification on the :3200 parity server: the label's rest
   bg computes `rgb(243,244,246)` / text `rgb(55,65,81)`; a REAL CDP
   hover tints to `rgba(245,245,245,0.8)` with the 150ms transition.
6. Regenerate the screenshots (`node scripts/capture-screenshots.mjs`)
   — the net-worth captures are expected byte-identical or
   sub-pixel (the rest colors are visually identical; the hover only
   engages under hover). Align README/CLAUDE/AGENTS/SKILL/session log/
   worklog + the probe README (the v29 catalog).

## Risk notes

- G1 touches two static label spans with existing e2e pins (the class
  assertions are UPDATED, not added — the rest geometry is untouched).
  The change is pure class-string — zero API/store/schema impact, zero
  data risk.
- The hex pins are visually identical to the oklab values (sub-1-unit
  sRGB deltas) — the risk is regression-only (the pinned values now
  byte-match the reference's computed strings, the durable guarantee).
- The `zb-badge-hover` pin is already live on 12 item-card badge
  instances (v28) — reusing it adds no new CSS surface.
- No other surface in the sweep requires a change (all verified
  identical/pinned/superset — see the results above).

## Appendix — the net-worth MOBILE VLM pair and its three flags (all verified no-change)

The regenerated `12-mobile-networth.png` was VLM-paired against a fresh
reference capture at 390×844. The verdict DIFFERED with three flags; each
was DOM-arbitrated (the VLM reads glyphs at 16–24px unreliably — the
computed geometry is the arbiter):

1. **"Summary grid 2-col (reference) vs 1-col (clone)"** — the reference's
   summary grid is `grid grid-cols-2 gap-4` at 390 (cells 175.8px); the
   clone's is `grid-cols-1 gap-4 sm:grid-cols-2` — the **v4-era G5
   data-fit superset, re-verified correct this session**: a live DOM
   experiment flipping the clone to 2-col measured the seeded values
   **"$65,300.00"/"$311,250.00" needing 152px/169px vs the 107px content
   box — the glyphs overlap the neighboring column** (the reference's own
   "$25,000.00" already micro-overflows its 144px cell at 152px, and its
   "$0.00" liabilities never exercise the case). The reference's contract
   is data-limited, not layout-protected (no min-w-0/break classes
   measured on its cells). **No change — the stacking stands** (the same
   family as the v4 H2 `text-3xl` responsive pin).
2. **"Trend icon far-right overlapping the border (reference) vs inset
   (clone)"** — measured with the identical gradient-card finder on BOTH
   sites: the 32×32 icon sits **insetFromRight: 48px on both** —
   byte-identical. The earlier 16px reading was a wrapper-div artifact.
   **False positive — no change.**
3. **"Tab icons: target/circle (reference) vs up/down arrows (clone)"** —
   the v14 G2 pin: the reference's triggers carry 16px lucide
   `circle-arrow-up`/`circle-arrow-down` (a circle WITH an arrow — what
   the VLM read as "target"/"circle" at 16px); the clone renders the
   identical pair. **No change.**
- Also re-verified while isolating flag 1: the reference's `/networth`
  464px mobile overflow involves BOTH its sidebar wrapper (hiding
  rootChild0 → 390) and its content column (hiding mainChild1 → 390 —
  the v4-era text-5xl/2-col width chain); the decorative `w-64 h-64
  opacity-10` circle is clipped by its card's `overflow-hidden` (hiding
  it changes nothing). The clone's 390 fit is its own shell's doing —
  the live 2-col DOM experiment kept the page at 390; only the seeded
  glyphs overflow their cells.

