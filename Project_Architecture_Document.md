# ZeroBalance — Master Project Architecture Document (PAD) v1.1.13

**Classification:** Internal Engineering Reference
**Status:** DEFINITIVE, PRODUCTION-LOCKED BLUEPRINT
**Companion Document:** README.md (user-facing); AGENTS.md / CLAUDE.md (agent operating rules)
**Last Updated:** 2026-10-13
**Audience:** Senior Engineers, Tech Leads, DevOps, and Onboarding Engineers
**Rule:** Every architectural decision in this document traces to a specific rationale.
           Nothing is here "because it's popular."

#### Revision Block — v1.1.13 (Tracked Changes)

- `[UI]` v1.1.13 (2026-10-13) — the v56 parity iteration (PIN-ONLY — no production-code change, the v53/v54 line's return to pin-only after the v55 fix): the counts 108 unit / 255 e2e / 35 smoke; the 1280 desktop VLM standing pair + the glyph-swap HOLD re-audit — the glyph re-audit (glyph-audit-v56.sh, the polyline/rect-rx capture fix) confirms the v55 legacy-icon swap holds byte-identical (24 shared glyph names, 0 diffs among the shared set, 1 one-side-only repeat); the desktop 1280x800 VLM pair (the dashboard + the networth view): the networth pair IDENTICAL, the dashboard pair's four flags all DOM-arbitrated to the documented classes (the root-URL active-nav gap superset fix — the non-root control renders the byte-identical forest-gradient active style on both sites; the data-driven fill width — the track byte-identical 568x12; the avatar; the Base44 FAB); the new hero-card DESKTOP 1280 census pin in tests/e2e/dashboard.spec.ts (+1 → 255: the 304px triple-column hero grid + the [632x364, 304x364] children at y 136, the goal card 632x316/radius 16/pad 32/forest gradient + shadow, the 568x12 track, the fill's pct-proportional width arithmetic, the 48px stat tiles) with three pin-sanity mutations; the v56 probe family (glyph-audit-v56.sh + the VLM trio + vlm-arbit-v56.sh + clone-arbit-v56.sh + hero-desk-v56.sh + standing-checks-v50.sh + ref-standing-v50.sh) + the probe lessons (branch the shape dump per tag; the reference has no nav landmark — scan all anchors; split long shot scripts per-view under the timeout); the 56th remediation plan + the probe catalog through v56.
- `[UI]` v1.1.12 (2026-10-13) — the v55 parity iteration (THE FIX — the fifth production-code change since v46, breaking the v53/v54 pin-only streak): the counts 108 unit / 254 e2e / 35 smoke; the ICON-GLYPH swap — a new module `src/components/ui/legacy-icons.tsx` (PiggyBankIcon / TrendingUpIcon / SearchIcon / MailIcon) rendering the reference's OLD lucide glyphs (lucide-react 0.525 redesigned four shapes since the reference's lucide version — the v44 chevron-swap class; the full audit: 24 lucide glyphs across the five views + the login page, 19 byte-identical, 4 drifted: piggy-bank, trending-up [two POLYLINES, not paths], search [handle 4.3, not 4.34], mail [flap a1.94 1.94, not a2 2]) with the `lucide lucide-<name>` class prefix kept (the e2e pins select svg.lucide-*; the class is part of the reference's DOM) and aria-hidden mirroring lucide's own no-a11y-prop rule; the eight import swaps (item-card / items-view / dashboard-view / item-details-dialog / budget-item-dialog / sidebar / net-worth-view / login-card) — the reference renders the piggy's OLD glyph on EVERY surface (piggy-sweep-v55.sh: the nav rail, the stat rows, the donut legend, the quick actions, the hero, the chips); the new `tests/e2e/glyph-parity.spec.ts` (+6, the shape-data census: the goal card's piggy/calendar/repeat at 390, every dashboard + networth piggy + trending, the search handle, the login mail + lock, the /expenses heart + circle-alert same-glyph control); six pin-sanity mutations verified (the body path, the polyline points, the search handle, the mail flap, a usage-site revert); the v55 probe family (ref-v55.sh + clone-v55.sh + piggy-sweep-v55.sh + glyph-audit-v55.sh + glyph-exact-v55.sh + glyph-diff-v55.mjs + the VLM trio) + the probe lessons (a path-only glyph census reads zero paths on circle-alert — walk every shape tag, read `points` for polylines; the glyph audit's login can race the page mount — retry + explicit auth check; agent-browser eval output is a JSON-encoded string); the 55th remediation plan + the probe catalog through v55.

#### Revision Block — v1.1.11 (Tracked Changes)

- `[UI]` v1.1.11 (2026-10-12) — the v54 parity iteration (PIN-ONLY — the third consecutive pin-only iteration, no production-code change): the counts 108 unit / 248 e2e / 35 smoke; the SAVINGS GOAL-CARD's badge-row + footer internals pin at 390 (byte-parity on every chrome axis — the header row flex/gap 8/mb 4, the dot 8×8/rgb(59,126,161) [the savings TYPE accent on both sites; the reference colors by TYPE, not classification], the badge row flex/wrap/gap 8/mb 12, every chip h 22/radius 6/pad 2px 10px/12/600 with the 12×12 icons at mr 4 [the monthly chip w 78 and the active chip w 63 on BOTH sites — the byte-parity width proof], the footer flex/space-between/12/rgb(107,114,128)/h 16 + the date span flex/gap 4 with the 12×12 calendar icon; the chip count/row height/payment span are the documented data classes); the v54 probe lessons (the justify-between footer finder's header-row false match — the locator is "the LAST justify-between direct child WITHOUT an h4"; the chips' inline-flex source class computes to "flex" as blockified flex items; the fresh-clone environment needs `npx playwright install chromium` — the per-version headless-shell binary); the 54th remediation plan + the probe catalog through v54.

#### Revision Block — v1.1.10 (Tracked Changes)

- `[UI]` v1.1.10 (2026-10-12) — the v53 parity iteration (PIN-ONLY — the second consecutive pin-only iteration, no production-code change): the counts 108 unit / 247 e2e / 35 smoke; the /networth view's TABLIST pin at 390 (byte-parity on every chrome axis — the list h 36/grid/#f5f5f5/radius 8/pad 4/maxW 448, the active 175×28 green pair + the shadow-sm VISIBLE pair, the inactive #737373 pair, the 16×16 currentColor icons; the WIDTH family rides the reference's own documented 464-overflow bug — its list 432 overhangs the 390 viewport where the clone's superset fix keeps the page in-bounds at 358/pageSW 390, the v47 divergence class); the CALCULATOR DIALOG's pin at 390 (the v45 add-then-restoreRent flow: the panel 358 @ x 16/radius 16/maxW 768/maxH 717.4/white/overflow hidden/flex + the 2xl VISIBLE layer + the centering invariant; the header h 101/pad 16 24; the chip 32×40 + the close 29×36 — the identical flex-shrink squish on both sites; the total card 310/#fff7f5/radius 12/pad 16; the row 310/pad 16/border-t; the Add Item button 110×32/12/500/gradient; docSW 390 — the panel h 413 with 1 row on both sites is data-dependent, never pinned); the execution lessons (the orphaned :3100 webServer reuse trap after a timed-out run — a stale db handle poisons the next run's data assertions; every calculator add/delete e2e ends with restoreRent; the rebuild and the test run as separate commands; the eval string's closing `()`); the 53rd remediation plan + the probe catalog through v53.

#### Revision Block — v1.1.9 (Tracked Changes)

- `[UI]` v1.1.9 (2026-10-12) — the v52 parity iteration (ONE production fix — the fourth since v46 — + three pins + one probe-infra fix): the counts 108 unit / 245 e2e / 35 smoke; the details sheet's missing SUBCATEGORY line fixed (item-details-dialog.tsx, between the H3 and the amount: the reference's FIFTH summary element — the P.text-lg 18/400/rgb(107,114,128) gray subcategory, measured live Rent → "Apartment" / Salary → "Main Job" — the field was always on the model, the card renders it, the edit dialog edits it, but the details view never wired it; the panel stays capped at its 85vh max-height so no geometry pin is affected); the /income and /expenses views' mobile pins at 390 (the header row's reflow + the filter card's 1-col grid + the first card's chrome — byte-parity); the details sheet's internals pin at 390 (the sticky header + the chip row + the facts + the meta footer); the standing script's R1 burger selector fixed (the reference's aria-label idiom silently failed on the clone's sr-only-named burger); the 52nd remediation plan + the probe catalog through v52.

#### Revision Block — v1.1.8 (Tracked Changes)

- `[AUTH]` v1.1.8 (2026-10-12) — the v51 parity iteration (ONE production fix — the third since v46 — + four pins): the counts 108 unit / 241 e2e / 35 smoke; the verify-email mode container's missing conversion fixed (login-card.tsx line 608: `space-y-4` → `zb-auth-mode` — the v50 F1's claimed-but-never-applied third site: the v50 plan/commit/docs stated the conversion happened, the diff landed the comment at 605-607 but not the class swap; the verify panel was 16px short at every viewport with the junction net gap -8 — the centered inner stack overlapping the back button by 8px, the same v4 space-y × `-mb-2` override the v50 F1 fixed for sign-up/forgot; the fix reuses the existing `.zb-auth-mode` rules, no `zb-sm6` — the reference's verify container carries no sm tier); the verify-mode panel census pin (the panel 508/wrapper 556/y 144 at 390 with a fixed 21-char email — the panel height is email-length-dependent, the "We've sent a 6-digit code to {email}" block wraps per the address length); the stats row pin at 390 (the three 210-tall cards @ 949/1183/1417, the radius-16 card, the 48px icon circle); the savings view pin at 390 (the goal card radius 12/pad 20, the H4 16/600, the amount 24/700 savings-blue, the card height a data class — the richer seed's 4-chip wrap); the Budget Guidelines pin at 390 (the BLOCK tiles stack, the three tinted tiles h 94/94/78); the quick-actions row pin at 390 (the three 90-tall cards @ 2751/2865/2979, the 40px icon circle, the trailing plus at opacity 0.5); the 51st remediation plan + the probe catalog through v51.

#### Revision Block — v1.1.7 (Tracked Changes)

- `[AUTH]` v1.1.7 (2026-10-12) — the v50 parity iteration (ONE production fix — the second since v46 — + two pins): the counts 108 unit / 236 e2e / 35 smoke; the auth-mode containers' scoped `.zb-auth-mode` + `.zb-sm6` classes added to `globals.css` + `login-card.tsx` (the v4 space-y × `-mb-2` override fix: the sign-up/forgot panels 16px short at every viewport — the reference's v3 build STACKS the button's own -mb-2 with the heading's mt (the collapsed 16 + (-8) = the 8px net gap) where v4's zero-specificity margin-block-end lets the utility OVERRIDE the gap — the pre-fix heading overlapped the button by 8px; the scoped restore drops the space-y class entirely, no zeroing rule (a 0-2-0 `> :not(:last-child)` zero would beat the 0-1-0 utility and kill the collapse — the first attempt's measured 430); the forgot's sm tier (the reference's `sm:space-y-6`) via the zb-sm6 modifier, 24px at >=640; the verify-email branch's same-idiom container converted); the networth tablist's chrome pin at 640 (the list 448/36/grid 220px 220px/#f5f5f5/8px/4px, the trigger pair's full chrome + the shadow-sm VISIBLE pair — the accepted lead-divergence class, the 16px currentColor icons); the dashboard hero's mobile reflow pin at 390 (the 1-col/24px-gap grid, the goal card 358×316@253 + the breakdown 324@593, the full goal-card internals, the chip pair — both sites' 20px svgs squish identically under the row's flex-shrink); the 50th remediation plan + the probe catalog through v50.

#### Revision Block — v1.1.6 (Tracked Changes)

- `[AUTH]` v1.1.6 (2026-10-12) — the v49 parity iteration (ONE production fix — the first since v46 — + two pins): the counts 108 unit / 232 e2e / 35 smoke; the login panel's mobile-only &nbsp; spacer added to `login-card.tsx` (the reference's `mt-8 text-center text-xs text-slate-400 sm:hidden` second child of the `w-full max-w-md` wrapper — h 16, mt 32, #94a3b8 — lifting the clone's card stack to the reference's panel y 57 at 390, the pre-fix clone centered alone at y 81; hidden at sm+, the desktop pins unchanged); the donut legend's mobile reflow pin at 390 (the container flex/column/gap 12/mt 24, the row 64/8px/12px/tinted, the dot 16/4, the leaves 16-500/16-700/12-400, the 16px icon); the calculator panel's chrome pin at 640 (w 608/radius 16/maxW 768/maxH 816/bg white/overflow hidden, the 2xl visible layer, the 36×36 close, the header border-b rgb(229,231,227), the centering invariant); the 49th remediation plan + the probe catalog through v49.

#### Revision Block — v1.1.5 (Tracked Changes)

- `[AUTH]` v1.1.5 (2026-10-12) — the v48 parity iteration (PIN-ONLY — no production-code change): the counts 108 unit / 229 e2e / 35 smoke (three new pins: the item-details sheet's shadow-2xl, the dialog-input focus composite at 390, the empty-state full census); the item-details panel's shadow-2xl VISIBLE layer `rgba(0,0,0,0.25) 0px 25px 50px -12px` on the 512×680/85vh-capped/radius-16 panel (the shadow-scale regression net's SEVENTH site — the 2xl end on the details surface, joining the v45 login-panel 2xl site) + the forest-scrim overlay rgba(26,58,46,0.5)/z 50/blur(8px); the dialog input's focus composite at MOBILE 390 (the input w 310 on both sites, the same visible layers as the desktop composite — the family viewport-independent); the empty-state full byte-parity census (the bare 358×328 py-16 block, the 64px icon at opacity 0.2, the 36px gradient Add button + v3's bare two-layer shadow); the 48th remediation plan + the probe catalog through v48.

#### Revision Block — v1.1.4 (Tracked Changes)

- `[AUTH]` v1.1.4 (2026-10-11) — the v47 parity iteration (PIN-ONLY — no production-code change): the counts 108 unit / 226 e2e / 35 smoke (three new pins: the dialog-input focus composite, the net-worth card mobile census, the mobile sheet's shadow-lg); the dialog-input FOCUS-state shadow composition contract (the rest shadow-sm visible layer + under REAL focus the 1px #0a0a0a ring with the rest shadow persisting beneath it + the border UNCHANGED under focus — the reference's 3-layer v3 composite vs the clone's 5-layer v4 construction, the same two VISIBLE layers, the accepted v10/v25/v45 lead-divergence class); the net-worth card's MOBILE rhythm contract at 390 (the 358-wide card h 194 with the value mb 16 — the v46 fix's rhythm survives the mobile reflow; the reference's own card 432 wide inside its 464-overflow page, its documented bug); the mobile sheet's shadow-lg visible pair (the shadow-scale regression net's sixth site); the 47th remediation plan + the probe catalog through v47.
- `[SR]` The measured-parity ledger: 47 remediation plans (`docs/remediation-plan-v1.md` … `v47.md`), 16 screenshots, the session-document chain — see `README.md`'s parity table for the per-iteration detail.

#### Revision Block — v1.1.3 (Tracked Changes)

- `[AUTH]` v1.1.3 (2026-10-11) — the v46 parity iteration: the counts 108 unit / 223 e2e / 35 smoke (two new pins: the net-worth asset-card census at 1280 + the confirm-bar white-pill shadow-sm regression pin); **THE VALUE→FACTS SPACING FIX** (the reference's `mb-4` wrap = 16px vs the clone's bare `mb-2` P = 8px — the card h 186→194, the `mb-2`→`mb-4` fix on both net-worth cards' value P; the item-card's own `mb-4` wrap the in-repo precedent); the net-worth card grid contract at 1280 (`md:grid-cols-2 lg:grid-cols-3 gap-4`, 960/3×309.328/gap 16 — the same family on both sites, the summary card's inner `sm:grid-cols-2` the v4 G4 stat-blocks design); the card's REAL hover INERT (the inline-beats-utility mechanism) + the kebab reveal; the confirm-bar white-pill family's shadow-sm visible layer pinned (the `--shadow-sm` theme pin's regression net, the five-site family); the 46th remediation plan + the probe catalog through v46.
- `[SR]` The measured-parity ledger: 46 remediation plans (`docs/remediation-plan-v1.md` … `v46.md`), 16 screenshots, the session-document chain — see `README.md`'s parity table for the per-iteration detail.

#### Revision Block — v1.1.2 (Tracked Changes)

- `[AUTH]` v1.1.2 (2026-10-11) — the v45 parity iteration (PIN-ONLY — no production-code change): the counts 108 unit / 221 e2e / 35 smoke (seven new pins: the items-card grid census at 1280 income + expenses, the calculator row census + REAL-hover shadow-md, the calculator 640 dialog, the category-level animation, the quick-action hover shadow-lg, the login shadow-scale regression pins); the SHADOW-SCALE SWEEP finding (every live `shadow-*` utility's VISIBLE layers match on both sites — the `--shadow-sm` theme pin is load-bearing for the small end since v4 RENAMED the scale; the md/lg/xl/2xl numerics were kept by v4 and are now pinned as the regression net; the LEAD-layer count diverges by construction — v4's 5-slot composition vs v3's 3-slot, invisible, the accepted v10/v25 class); the items-view card grid contract at 1280 (the 960 = rail 256 + content 1024 − p-8 64 arithmetic on both sites, the card's REAL hover INERT via the inline-beats-utility mechanism); the calculator row's LIVE hover (no inline shadow — the shadow-md visible layers + the action reveal); the 45th remediation plan + the probe catalog through v45.
- `[SR]` The measured-parity ledger: 45 remediation plans (`docs/remediation-plan-v1.md` … `v45.md`), 16 screenshots, the session-document chain — see `README.md`'s parity table for the per-iteration summaries.

#### Revision Block — v1.1.1 (Tracked Changes)

- `[AUTH]` v1.1.1 (2026-10-11) — the v44 parity iteration: the counts 108 unit / 214 e2e / 35 smoke (five new e2e: the expansion-animation pin, the 390/1280 drill-down censuses, the donut-legend census, the chevron glyph-swap pin); the drill-down expansion ANIMATION contract (the reference's ~200ms height+opacity tween in both directions — implemented via the `Collapse` wrapper: the grid 0fr↔1f technique + `@starting-style` entry + the onTransitionEnd delayed unmount in `src/components/budget/dashboard-view.tsx` + the `.zb-collapse`/`.zb-collapse-clip` class pair in `src/app/globals.css`; the collapsed DOM returns to the pre-fix node tree); the chevron GLYPH-swap contract (lucide-chevron-down ↔ chevron-up, both levels, rotate: none — a computed-style census cannot see glyph swaps, read the svg's class); the 44th remediation plan + the probe catalog through v44.
- `[SR]` The measured-parity ledger: 44 remediation plans (`docs/remediation-plan-v1.md` … `v44.md`), 16 screenshots, the session-document chain — see `README.md`'s parity table for the per-iteration summaries.

---

#### Revision Block — v1.0.0 (Tracked Changes)

- `[AUTH]` v1.0.0 — the ZeroBalance application built on the repo scaffolding: all 7 routes, 21 API handlers across 13 route files, the Prisma schema, the three-tier test suite, and the Tailwind v4 trap mitigations. ORBITAL-era specs/scripts replaced.
- `[SR]` Both reference mobile-navigation bugs fixed and pinned by e2e (toast click-block, sheet-stays-open).
- `[SR]` zustand v5 derived-selector re-render loop (React #185) found on production build and fixed with `useShallow`.

#### Revision Block — v1.1.0 (Tracked Changes)

- `[AUTH]` v1.1.0 (2026-10-11) — the parity-remediation era's alignment pass: the counts 108 unit / 209 e2e / 35 smoke (the v1.0.0 numbers were 87/34/30); the API surface 23 handlers across 15 route files (auth x6 incl. verify-email + resend, budget-items x2, line-items x2, assets x2, liabilities x2, health); the login card's FOUR states (idle/error/confirmation/forgot — the register flow's verify-email gate added in v21); the SEO routes (`src/app/robots.ts` + `src/app/sitemap.ts` MetadataRoute files, `NEXT_PUBLIC_SITE_URL`-driven); the Budget Item Details sheet (v28 — the card-body-click bottom sheet); the axe-core a11y gate (v38/39 — the two-gate structural + provenance contract, desktop AND mobile, the sheet-open structural pins on all six routes); the email-verification lib (`src/lib/verification.ts` + `User.verificationCode`); the seven superset fixes (mobile hamburger/sheet-close/active-highlight/no-overflow/mobile figure fit/kebab keyboard reveal); the test-suite structure (9 unit files / 22 e2e spec files / the 35-step smoke with verify-email); the parity-probe catalog (`scripts/parity-probes/` — 43+ files through v43) and the TDD census-pin discipline (every production change measured live on BOTH sites, pinned RED-first, mutation-sanity-verified).
- `[SR]` The measured-parity ledger: 43 remediation plans (`docs/remediation-plan-v1.md` … `v43.md`), 16 screenshots, the session-document chain — see `README.md`'s parity table for the per-iteration summaries.

---

## Table of Contents

1. [System Overview & Decisions](#1-system-overview--decisions)
2. [High-Level System Topology](#2-high-level-system-topology)
3. [Application Architecture](#3-application-architecture)
4. [Data Architecture](#4-data-architecture)
5. [Design System Reference](#5-design-system-reference)
6. [Security Architecture](#6-security-architecture)
7. [Testing Strategy](#7-testing-strategy)
8. [Build & Deployment](#8-build--deployment)
9. [Developer Handbook](#9-developer-handbook)
10. [Known Issues & Outstanding Tasks](#10-known-issues--outstanding-tasks)
11. [Key Files Reference](#11-key-files-reference)
12. [Glossary](#12-glossary)

---

## 1. System Overview & Decisions

### 1.1 Document Metadata & Purpose

ZeroBalance is a self-hosted budget planner and a **superset clone** of the ZeroBudget reference app (`zero-balance-4885a8f3.base44.app`): it reproduces the reference's seven routes, four entities, and measured design system, while fixing the reference's two mobile-navigation bugs and hardening the stack (validation, rate limiting, sessions, integer-cent arithmetic).

Use this PAD to understand, extend, debug, or replicate the system. New engineers: read §1–§4 first. Debugging: §6 (security), §8 (build), §10 (known issues). Reviewing tech choices: §1.3 (ADRs).

### 1.2 Technology Stack Summary

| Layer | Technology | Version | Key Rationale |
|-------|-----------|---------|---------------|
| Web framework | Next.js (App Router) | ^16.1.1 | Standalone output + static prerender of the item views; route handlers colocate the API |
| UI runtime | React | ^19.0.0 | Required by Next 16; hooks-v6 lint rules enforced |
| Language | TypeScript (strict) | ^5 | `tsc --noEmit` is a gate; no build-time escape hatches |
| Styling | Tailwind CSS | 4 | CSS-first `@theme`; parity colors done with inline styles + CSS vars (engine-independent) |
| Charts | recharts | ^3.10.1 | The reference's donut is recharts; same library = same sector geometry |
| Client state | Zustand | ^5.0.6 | One store for server data + modal stack; `useShallow` for derived selectors |
| UI primitives | Radix UI (dialog, select, dropdown, radio, toast, tabs, switch, label, popover, alert-dialog) | ^1.x/2.x | The reference is Radix-based; accessible behavior matches by construction |
| Icons | lucide-react | ^0.525.0 | The reference's icon set |
| ORM | Prisma | 6.11.1 (pinned) | Schema-first, typed client; version pinned — URL resolution behavior differs across minors |
| Database | SQLite | — | Zero-config single-file; matches the reference's deployment model |
| Validation | zod | ^4.6.5 | Field-level 400s at the API boundary; preprocessors normalize wire formats |
| Unit tests | Vitest | ^5.0.1 | Fast node-env tests for pure domain seams |
| E2E tests | Playwright | ^1.63.0 | Drives the production standalone build in real Chromium |
| Runtime | Node ≥ 20 / bun ≥ 1.2 | — | `bun` used for scripts; Node for the standalone server |

### 1.3 Architecture Decision Records (ADRs)

**ADR-001: Single Next.js application (no monorepo, no separate API service)**

- **Context:** The reference is a Base44 SPA with a generic entity API. The clone must be self-hostable with minimal moving parts, and the e2e suite must exercise the production build end-to-end.
- **Decision:** One Next.js 16 app: App Router pages for the 7 routes, route handlers for the 21 API endpoints (13 route files), one Prisma client.
- **Rationale:** The deployment model is single-server SQLite; a separate API would add operational surface with zero benefit. Colocated handlers keep the envelope, validation, and serialization conventions enforceable in one place.
- **Consequences:** + simple deploys, one typecheck/lint gate. − API and UI share a release cadence (acceptable at this scale).
- **Alternatives Rejected:** Turborepo monorepo (the scandihaven lineage) — overkill for one app; separate Express/Fastify API — doubles infra.

**ADR-002: Client-side state in one Zustand store; API as the persistence seam**

- **Context:** The reference is an SPA whose views all read one client cache. Hydrated static pages + client fetches must not fight over data ownership.
- **Decision:** All server data (items/assets/liabilities/lineItems) lives in a single Zustand store; pages are thin client components; mutations go store → API → store update. No React Context, no server components fetching domain data.
- **Rationale:** Matches the reference's interaction model exactly (optimistic-free, fetch-on-boot, mutate-and-refresh), and keeps every view reactive to every mutation (the dashboard follows the calculator's parent-recalc live).
- **Consequences:** + one source of truth, simple modals. − derived selectors need `useShallow` (see ADR-006), and the first paint waits for the boot fetch.
- **Alternatives Rejected:** TanStack Query (server-cache semantics don't match the modal-driven mutation flow); Redux Toolkit (boilerplate).

**ADR-003: SQLite via a schema-anchored relative `file:` URL**

- **Context:** The repo contract is `DATABASE_URL="file:../db/custom.db"` with `db/` at the repo root. Prisma's CLI resolves relative URLs differently depending on whether the value came from `.env` (schema-dir anchored) or the shell (CWD anchored) — a real footgun that put databases in the wrong folder during this build.
- **Decision:** `src/lib/db-path.ts` implements the runtime rule: a relative `file:` URL resolves against the first anchor containing `prisma/schema.prisma` (standalone-build detection included). npm scripts pin `DATABASE_URL` for the runtime and strip it (`env -u`) for CLI commands.
- **Rationale:** One database location for `next dev`, `next build`, the standalone server, the Prisma CLI, and the seed — regardless of CWD or a polluting parent-shell export. Pinned by `tests/db-path.test.ts` (15 cases).
- **Consequences:** + reproducible DB location everywhere. − contributors must use the npm wrapper scripts, not bare `prisma` commands (documented in AGENTS.md).
- **Alternatives Rejected:** Absolute URLs in `.env` (not portable); a `datasources` override in code (hides the resolution from the CLI).

**ADR-004: Integer-cent money arithmetic behind a plain-number wire format**

- **Context:** The reference API exchanges plain JSON numbers; naive float sums drift (`0.1 + 0.2`).
- **Decision:** Amounts are stored and exchanged as user-entered decimals; **every** aggregation converts to integer cents first (`src/lib/money.ts`). Display uses TWO formatters, mirroring the reference bundle: plain `"$" + toFixed(2)` without grouping for the dashboard / items views / calculator (`$5550.00`), and `toLocaleString` grouping for net worth only (`$25,000.00`).
- **Rationale:** API parity with the reference without inheriting its float math; totals are exact and deterministic (the e2e suite asserts them to the cent).
- **Consequences:** + exact totals; format functions are the single display authority. − the wire format permits more decimals than cents (rounded at conversion).
- **Alternatives Rejected:** Storing integer cents in the DB (breaks wire parity); decimal libraries (unnecessary at this scale).

**ADR-005: scrypt + HMAC-signed cookie sessions; no auth service**

- **Context:** Self-hosted, single-server; no external identity provider.
- **Decision:** `src/lib/auth.ts`: scrypt (N=16384) password hashing with per-user salt; HMAC-SHA256 signed session cookies (7-day expiry, constant-time compare); `AUTH_SECRET` required in production.
- **Rationale:** Zero external dependencies; the reference's cookie-session behavior (including `?from_url=` return handling and login rendering for authenticated users) is reproduced.
- **Consequences:** + auditable in ~100 lines. − per-process rate-limit state and no SSO (both acceptable for the single-server model; documented).
- **Alternatives Rejected:** NextAuth/Auth.js (needs an adapter + provider config for a local-password app); JWTs (larger, revocable only by rotation).

**ADR-006: Tailwind v4 with measured mitigations (not defaults)**

- **Context:** `docs/Tailwind-V4-Validation-Report.md` documents five v4 behavior changes that silently alter visual output (bare-HSL transparent theme, oklch palette drift, oklab gradients, `space-y` selector rewrite, shadow-scale shift). The reference also breaks mobile nav through a toast-container bug.
- **Decision:** `src/app/globals.css` pins the mitigations: `@theme` colors in hex with `inline` reference, the reference's shadow scale pinned, v4-native `w-(--var)` syntax, `h-svh` for full-height fixed chrome, and the toast viewport `pointer-events: none`. Parity colors are applied via inline styles + CSS vars.
- **Rationale:** Utility classes for layout + inline CSS-var colors reproduces the reference's computed styles engine-independently — v4's color-space conversions can't drift what isn't in the palette pipeline.
- **Consequences:** + stable computed parity, both reference nav bugs fixed and test-pinned. − two styling channels (documented convention).
- **Alternatives Rejected:** Tailwind v3 (abandons v4 perf/tooling); CSS modules (loses utility velocity).

**ADR-007: Three-tier verification with a self-resetting e2e database**

- **Context:** The parity spec asserts the seed's exact arithmetic; leftover fixtures from a failed run poison every later assertion (observed during this build).
- **Decision:** Vitest for pure seams (87), Playwright against the production standalone build (34) with `db/e2e.db` **deleted and re-seeded by global setup every run**, and a 30-step bash API smoke. E2e specs restore their own fixtures; one worker; one storageState login (auth is rate-limited 10/IP/15 min).
- **Rationale:** Deterministic runs from any working tree state; the suite can assert to-the-cent numbers forever.
- **Consequences:** + zero flake from state, real-production coverage. − e2e wall time ~45s; a spec that crashes mid-flow must be re-run (the next global setup cleans it).
- **Alternatives Rejected:** Per-test databases (slower, changes timing); API-level-only tests (miss the hydration bugs this suite caught — React #185, modal stacking).

---

## 2. High-Level System Topology

```mermaid
flowchart TB
    subgraph Client["Browser (desktop ≥768 / mobile 390)"]
        PAGES["App Router pages<br/>/login · / · /dashboard · /income<br/>/expenses · /savings · /networth<br/>(static-prerendered shells, hydrated)"]
        STORE["Zustand store<br/>user · items · assets · liabilities<br/>lineItems · modal stack"]
        DIALOGS["Radix modals: budget-item · line-item ·<br/>calculator · asset · liability + mobile sheet"]
    end
    subgraph Server["Next.js standalone server (Node)"]
        API["/api/auth/* · /api/budget-items[/:id]<br/>/api/line-items[/:id] · /api/assets[/:id]<br/>/api/liabilities[/:id] · /api/health"]
        GUARD["requireSession + rate limiter"]
        ZOD["zod schemas"]
        SVC["line-item-service (parent recalc)"]
        SER["serializers"]
    end
    AUTHLIB["auth.ts — scrypt verify,<br/>HMAC cookie sign/read"]
    DB[("SQLite — db/custom.db<br/>(schema-anchored path)")]
    PAGES --> STORE --> API --> GUARD --> ZOD --> SVC --> SER --> AUTHLIB --> DB
```

**Scaling & constraints:** single Node process, single SQLite file (WAL journaling off by default). The rate limiter is per-process memory — correct for the single-server model, swap for shared storage before horizontal scaling. Every route handler is stateless apart from the DB file and the limiter.

---

## 3. Application Architecture

### 3.1 The Layer Model

```
Layer 0: Routes (src/app/**/page.tsx) — compose AppShell + one view.
         Rule: pages never fetch; they render views.
Layer 1: Views & dialogs (src/components/budget/*) — read the store,
         dispatch store actions. Rule: no direct API calls except
         through store actions; inline styles + CSS vars for colors.
Layer 2: Store (store.ts) — the only API caller (src/lib/api.ts) and
         the only modal owner. Rule: one store; selectors returning
         derived references must use useShallow.
Layer 3: Domain seams (src/lib/*) — pure functions + the API routes'
         helpers (validation, auth, money, dashboard math, serializers,
         db-path, rate-limit). Rule: no React imports here.
Layer 4: Prisma + SQLite (prisma/schema.prisma, src/lib/db.ts) —
         typed rows only. Rule: rows cross into the API shape only
         through serializers.
```

The Golden Rule: **data flows `UI → store action → API → zod → Prisma → serializer → store update → UI`** — any shortcut around the store or the serializers is a defect.

### 3.2 Annotated Directory Structure

```
├── prisma/
│   ├── schema.prisma        # User, BudgetItem, ExpenseLineItem, Asset, Liability (+ cascade + indexes)
│   └── seed.ts              # Idempotent demo seed: 2 income / 3 expense / 2 savings items, 3 assets, 2 liabilities
├── src/
│   ├── app/
│   │   ├── api/             # 13 route files / 21 handlers (auth x4, budget-items x2, line-items x2,
│   │   │                    #   assets x2, liabilities x2, health) — envelope + zod + session guard
│   │   ├── login/page.tsx   # Three-state auth card (sign-in / sign-up / forgot)
│   │   ├── page.tsx         # "/" — dashboard (dual route with /dashboard, like the reference)
│   │   └── [dashboard|income|expenses|savings|networth]/page.tsx
│   ├── components/
│   │   ├── budget/
│   │   │   ├── store.ts             # THE Zustand store: state + actions + modal stack + api client use
│   │   │   ├── app-shell.tsx        # Boots the store; sidebar + main + ModalHost (conditional mounts)
│   │   │   ├── sidebar.tsx          # 256px desktop rail + mobile header + 288px sheet (nav-close fix)
│   │   │   ├── dashboard-view.tsx   # NET ZERO hero, breakdown, stat cards, donut, guidelines, quick actions
│   │   │   ├── items-view.tsx       # Shared income/savings/expenses view (filters, cards, empty state)
│   │   │   ├── item-card.tsx        # Badges, ellipsis menu, inline Edit/Calculate (expenses), inline confirm
│   │   │   ├── net-worth-view.tsx   # Gradient summary + Assets/Liabilities tabs + cards
│   │   │   ├── budget-item-dialog.tsx   # Add/Edit item: type/classification/amount/frequency/status/…
│   │   │   ├── calculator-dialog.tsx    # Category calculator (category-adaptive chrome)
│   │   │   ├── line-item-dialog.tsx     # Nested add/edit line item (scoped close: calculator stays open)
│   │   │   ├── asset-dialog.tsx / liability-dialog.tsx
│   │   │   ├── login-card.tsx       # Reference auth card (circular logo chip, Google button, states)
│   │   │   └── require-session.tsx  # /login?from_url= redirect gate
│   │   └── ui/              # shadcn-style Radix primitives (dialog w/ sheet, select, dropdown,
│   │                        #   radio-group, toast w/ pointer-events fix, tabs, switch, input, …)
│   └── lib/
│       ├── api.ts           # Typed fetch client + ApiError (the only direct fetch)
│       ├── api-helpers.ts   # ok/fail envelope, parseBody, requireSession
│       ├── auth.ts          # scrypt hash/verify, HMAC cookie sessions, session user resolution
│       ├── constants.ts     # Domain enums, labels, measured palette (single source of truth)
│       ├── dashboard.ts     # computeTotals, goalStatus, spendingBreakdown, computeNetWorth
│       ├── db.ts / db-path.ts  # Prisma client + the schema-anchored URL resolution contract
│       ├── line-item-service.ts # Parent recalculation rule (sum of line items, server-side)
│       ├── money.ts         # Integer-cent arithmetic + formatters ($, +/−, ∞ ratio, %)
│       ├── rate-limit.ts    # Fixed-window limiter (10/15min) + clientIp
│       ├── serializers.ts   # Prisma row → API payload (ISO dates, null → undefined, no userId)
│       ├── types.ts         # Client-facing domain types (mirror the API payloads)
│       └── validation.ts    # Every zod schema (incl. optionalIsoDate "" normalizer)
├── tests/
│   ├── *.test.ts            # Vitest unit suites (money, dashboard-math, validation, rate-limit,
│   │                        #   constants, serializers, line-item-service, db-path)
│   └── e2e/                 # Playwright: auth, dashboard, items, calculator, networth,
│                            #   mobile-navigation (+ auth.setup, global-setup, helpers)
├── scripts/
│   ├── smoke-test.sh        # 30-step production API smoke (own server on :3210)
│   └── capture-screenshots.mjs  # docs/screenshots generator (boots its own standalone server)
├── docs/                    # Tailwind v4 report, SSH push runbook + wrapper, DEPLOYMENT.md
└── db/custom.db             # SQLite database (gitignored; e2e.db alongside during runs)
```

### 3.3 Critical Code Patterns

**Pattern 1 — Integer-cent aggregation (the arithmetic seam)**

```ts
// src/lib/money.ts — every total in the app runs through this seam so
// IEEE-754 drift (0.1 + 0.2) can never reach a displayed amount.
export function sumAmounts(amounts: number[]): number {
  return fromCents(amounts.reduce((acc, a) => acc + toCents(a), 0));
}
```

*Why this pattern:* the wire format is plain numbers (reference parity), but totals must be exact — the e2e suite asserts `+$2065.00` computed from seven seeded decimals. Centralizing the conversion means no view can accidentally sum floats.

**Pattern 2 — useShallow on derived Zustand selectors**

```tsx
// src/components/budget/items-view.tsx — without useShallow the selector
// returns a NEW array on every snapshot call; zustand v5's
// useSyncExternalStore then sees a changed snapshot every render and
// loops to "Maximum update depth exceeded" (React #185) on the hydrated
// static pages. useShallow returns the previous reference when the
// elements are shallow-equal.
const items = useBudgetStore(
  useShallow((s) => s.items.filter((i) => i.type === type)),
);
```

*Why this pattern:* the bug only manifested in the production build (hydration timing), not in `next dev` — it reached the e2e suite and crashed all three item views. Every future derived selector must follow this form.

**Pattern 3 — Store-driven modals with lazy form initialization**

```tsx
// src/components/budget/budget-item-dialog.tsx — the ModalHost only
// mounts this dialog while a modal is open, so every open is a fresh
// mount: the form derives from the modal AT MOUNT (lazy initializer) and
// re-derives if the modal identity ever changes in place
// (adjust-state-during-render — no effects, no cascading renders).
const [form, setForm] = React.useState<BudgetItemFormData>(() => initialForm(modal));
const modalKey = modal
  ? modal.mode === "edit" ? `edit:${modal.item.id}` : `create:${modal.type}`
  : null;
const [resetKey, setResetKey] = React.useState(modalKey);
if (resetKey !== modalKey) { setResetKey(modalKey); setForm(initialForm(modal)); }
```

*Why this pattern:* an earlier effect-based reset silently never fired (the component mounted with the modal already set), leaving create-forms at their defaults; the lazy initializer makes initialization structural rather than timing-dependent, and satisfies `react-hooks/set-state-in-effect`.

**Pattern 4 — Modal panel stacking (clicks must land)**

```css
/* src/app/globals.css — the panel is fixed + centered ABOVE the z-50
   overlay. A static panel would paint below the fixed overlay: visible
   through its translucency but unclickable (the overlay intercepted
   every pointer event). Same z-index as the overlay, later in the DOM
   → stacked on top. */
.zb-modal-panel {
  position: fixed; z-index: 50;
  left: 50%; top: 50%; transform: translate(-50%, -50%);
  width: calc(100% - 2rem); max-width: 42rem; max-height: 90vh; overflow-y: auto;
}
```

*Why this pattern:* the dialog built-in Close button additionally needs `z-20` — the sticky dialog header creates a `z-10` stacking context that otherwise buries it. Both lessons are e2e-pinned.

**Pattern 5 — Server-side parent recalculation (calculator rule)**

```ts
// src/lib/line-item-service.ts — creating/editing/deleting a line item
// recalculates and persists the parent BudgetItem's amount as the sum of
// its line items. The response carries { lineItem, parentAmount } so the
// store can update the parent in place — the dashboard follows live.
export async function recalcParentAmount(budgetItemId: string) {
  const lineItems = await db.expenseLineItem.findMany({
    where: { budgetItemId }, select: { amount: true },
  });
  const total = sumAmounts(lineItems.map((li) => li.amount));
  return db.budgetItem.update({ where: { id: budgetItemId }, data: { amount: total } });
}
```

*Why this pattern:* the reference recalculates the category total immediately (no client save step); reproducing the rule server-side keeps every client consistent and makes the recalc testable through the real API.

*(Additional pinned patterns: the toast viewport `pointer-events: none` fix — `src/components/ui/toast.tsx`; the schema-anchored `file:` URL resolution — `src/lib/db-path.ts`, with the standalone-build CWD detector; the mobile sheet's pathname-driven close — `src/components/budget/sidebar.tsx`.)*

---

## 4. Data Architecture

### 4.1 Database Schema

```mermaid
erDiagram
    User ||--o{ BudgetItem : owns
    User ||--o{ ExpenseLineItem : owns
    User ||--o{ Asset : owns
    User ||--o{ Liability : owns
    BudgetItem ||--o{ ExpenseLineItem : "broken down into"
    User {
      string id PK
      string email UK
      string passwordHash
      string name
    }
    BudgetItem {
      string id PK
      string userId FK
      string type
      string classification
      float amount
      string category
      string subcategory
      string paymentMethod
      string frequency
      string date
      bool recurring
      string status
      string notes
    }
    ExpenseLineItem {
      string id PK
      string budgetItemId FK
      string userId FK
      string name
      float amount
      string frequency
      string provider
      string policyNumber
      string paymentMethod
      string startDate
      string endDate
      string status
    }
    Asset {
      string id PK
      string userId FK
      string type
      string name
      string institution
      string accountNumber
      float value
      string lastUpdated
    }
    Liability {
      string id PK
      string userId FK
      string type
      string name
      string institution
      string accountNumber
      float value
      float interestRate
      float monthlyPayment
      string lastUpdated
    }
```

**Enum-string columns** (`type`, `classification`, `frequency`, `status`) are validated at the API boundary by zod (`src/lib/validation.ts` mirrors `src/lib/constants.ts`) — SQLite has no native enums. Indexes: `@@index([userId, type])` and `@@index([userId, createdAt])` on BudgetItem back the list views. Deletes cascade (`onDelete: Cascade`) so a deleted user (or budget item) takes its children with it.

### 4.2 Data Models

The client-facing types (`src/lib/types.ts`) mirror the API payloads exactly (camelCase, optional nulls as `| undefined`): `BudgetItem`, `ExpenseLineItem`, `Asset`, `Liability`, plus form-data variants. Prisma rows never reach a component — `src/lib/serializers.ts` is the only translator (ISO timestamps, `null → undefined` elision, `userId` never serialized).

### 4.3 Persistence Strategy

- **Connection model:** one `PrismaClient` per process (`src/lib/db.ts`), instantiated with the schema-anchored URL. SQLite file locking means a single server process — the intended deployment.
- **Migrations:** `prisma db push` during development (schema-first, no migration history); `prisma migrate dev` available for hosted environments (`npm run db:migrate`).
- **Seed:** `prisma/seed.ts` is idempotent (upserts the user; reuses items by natural keys `type+category+subcategory`) and safe to re-run — the e2e global setup relies on exactly that property after deleting the file.
- **Backup:** the database is one file (`db/custom.db`) — copy it offline; there is no WAL sidecar in normal operation.

---

## 5. Design System Reference

### 5.1 Typographic System

The reference uses the **system font stack** (`ui-sans-serif, system-ui, sans-serif, …`) — no webfonts, zero font loading. Hierarchy is by weight and size only: `text-3xl font-bold` page titles (forest-dark), `text-sm font-medium gray` card labels, `text-xs font-semibold uppercase tracking-wider` group labels, `text-2xl/3xl font-bold` amounts.

### 5.2 Color Tokens

Measured from the reference's `:root` (computed styles as ground truth); canonical definitions in `src/lib/constants.ts` (`COLORS`, `rgb`, `TYPE_COLORS`):

| Token | Hex / rgb | Usage |
|-------|-----------|-------|
| `--forest-dark` | `#1a3a2e` / `rgb(26,58,46)` | Headings, hero gradient start, modal titles |
| `--forest-medium` | `#2d5a4a` / `rgb(45,90,74)` | Active-nav gradient start, secondary text |
| `--lime-green` | `#8fbc3f` / `rgb(143,188,63)` | Income accent, primary buttons, avatar, "Savings" donut slice |
| `--lime-light` | `#b8d87e` | (supporting) |
| `--orange-dark` | `#e07a3b` / `rgb(224,122,59)` | Expense accent, "Need" slice, hero allocation gradient |
| `--orange-light` | `#f5a962` | Goal-card status text |
| `--blue-dark` / `--blue-medium` | `#2c5f7c` / `#3b7ea1` | Savings accent ("Want" slice `#3b7ea1`) |
| `--neutral-warm` | `#fafaf8` | Page background |
| (non-var) | `rgb(229,231,227)` | Borders/dividers |
| (non-var) | `rgb(107,114,128)` | Secondary gray text |
| (non-var) | `rgb(245,248,245)` | Sidebar footer / legend chip tint |
| Icon tints | `rgba(accent, 0.125)` | Card/empty-state icon squares |

**Application rule:** Tailwind utilities for layout/spacing; **inline styles + CSS vars for colors** on parity surfaces — computed-style parity independent of the engine's color-space conversions (ADR-006).

### 5.3 Component Primitives

shadcn-style Radix primitives in `src/components/ui/` (dialog with left/right `SheetContent`, select, dropdown-menu, radio-group, toast, tabs, switch, input, label, textarea, badge, button, alert-dialog, popover), styled to the reference's measured geometry (256px rail `h-svh`, 288px sheet `w-(--sheet-width)` with `h-svh`, sticky `z-10` modal headers with `z-20` close buttons, `max-w-2xl`/`42rem` panels, `max-h-[90vh]` scroll).

### 5.4 Motion / Animation

Radix `data-[state]`-driven: sheet slide-in 500ms / slide-out 300ms with fade; modals without entrance animation (matching the reference); toast slide-in top (mobile) / bottom-right (sm+) with 4s duration and swipe-dismiss. Donut entrance animation is recharts' default. No reduced-motion handling beyond Radix defaults (no custom keyframes to degrade).

---

## 6. Security Architecture

### 6.1 Security Rules

| Rule | Enforcement |
|------|-------------|
| Every API input is validated | `parseBody(schema)` in every handler — zod rejects with field-level 400s |
| Sessions are signed, not encrypted-but-trusted | HMAC-SHA256 over `userId.expiry`, constant-time compare in `auth.ts` |
| Passwords are salted + slow-hashed | scrypt (N=16384, 64-byte), per-user random salt — never reversible |
| Auth endpoints are rate-limited | `authLimiter` 10 attempts / 15 min / IP → 429 + `Retry-After` |
| No account enumeration | Unknown email and wrong password both → 401 `"Invalid email or password"` |
| Rows are user-scoped | Every query filters `userId` from the session (`requireSession`) |
| Secrets never enter the tree | `.gitignore` rejects `.env`, `*.key`, `ssh-key.txt`; push keys live outside the repo (SSH wrapper runbook) |
| No `userId` leaks in payloads | Serializers are the only row→payload translator |
| `AUTH_SECRET` required in production | Boot warns loudly; generate with `openssl rand -hex 32` |

### 6.2 Security Utilities

`src/lib/auth.ts` (hash/verify/session sign+read), `src/lib/rate-limit.ts` (fixed-window limiter, pure + unit-tested; `clientIp` prefers `x-forwarded-for`'s first hop), `src/lib/api-helpers.ts` (`requireSession` guard), `src/lib/validation.ts` (all schemas, including the empty-string date normalizer and the real-calendar-date check).

### 6.3 Authentication & Authorization

Single-role model: a signed-in user owns every row they create. Session cookie (`zb_session`): `userId.exiryTs` HMAC-signed, `httpOnly`, `sameSite=lax`, 7-day expiry, set on login/register, cleared on logout. Client boot (`store.boot()`) resolves `/api/auth/me`; `RequireSession` redirects unauthenticated workspace visits to `/login?from_url=<path>` (the reference's return-URL behavior), and the login card renders for authenticated users too (reference parity — re-sign-in lands on the workspace).

### 6.4 Threat Model

| Vector | Mitigation |
|--------|-----------|
| Credential stuffing | Rate limiting (10/15min/IP) + identical 401s for unknown email / wrong password |
| Session forgery | HMAC signature + constant-time verification; secret required in prod |
| Session fixation | Fresh cookie value on every login |
| SQL injection | Prisma parameterized queries only — no raw SQL anywhere |
| XSS | React escaping; no `dangerouslySetInnerHTML`; cookies `httpOnly` |
| CSRF on mutations | `sameSite=lax` cookies + JSON-only bodies (cross-site form posts can't produce JSON content-type without CORS preflight) |
| Click-blocking overlay UI hijack | Toast viewport `pointer-events: none` (the reference's bug — fixed here) |
| Secret leakage via git | `.gitignore` + wrapper-based SSH pushes; keys shredded after use |

---

## 7. Testing Strategy

### 7.1 Test Distribution

| Category | Files | Tests | Location | Framework |
|----------|-------|-------|----------|-----------|
| Unit — money math | 1 | 17 | `tests/money.test.ts` | Vitest |
| Unit — dashboard aggregations | 1 | 9 | `tests/dashboard-math.test.ts` | Vitest |
| Unit — zod schemas | 1 | 18 | `tests/validation.test.ts` | Vitest |
| Unit — rate limiter | 1 | 8 | `tests/rate-limit.test.ts` | Vitest |
| Unit — domain constants | 1 | 5 | `tests/constants.test.ts` | Vitest |
| Unit — serializers | 1 | 5 | `tests/serializers.test.ts` | Vitest |
| Unit — line-item rule | 1 | 4 | `tests/line-item-service.test.ts` | Vitest |
| Unit — db-path contract | 1 | 15+ | `tests/db-path.test.ts` | Vitest |
| E2E — auth | 1 | 6 | `tests/e2e/auth.spec.ts` | Playwright |
| E2E — dashboard | 1 | 7 | `tests/e2e/dashboard.spec.ts` | Playwright |
| E2E — item views + CRUD | 1 | 8 | `tests/e2e/items.spec.ts` | Playwright |
| E2E — calculator | 1 | 3 | `tests/e2e/calculator.spec.ts` | Playwright |
| E2E — net worth | 1 | 4 | `tests/e2e/networth.spec.ts` | Playwright |
| E2E — mobile + desktop nav | 1 | 6 | `tests/e2e/mobile-navigation.spec.ts` | Playwright |
| Smoke — production API | 1 script | 30 steps | `scripts/smoke-test.sh` | bash + curl |

### 7.2 Test Patterns

- **Unit tests target pure seams only** — money, dashboard math, validators, limiter, serializers — with the reference's own numbers as fixtures (the seed arithmetic: income 5550 / savings 1250 / expenses 2235 → `+$2065.00`, allocation 62.8%, savings 13.8% / want 4.6% / need 81.6% — the donut renders [Savings, Want, Need]).
- **E2E drives the production standalone build** (`playwright.config.ts` webServer → `bun .next/standalone/server.js` on :3100 with `db/e2e.db`), signing in once via the `setup` project and replaying `storageState` — never per-test logins (rate-limit budget).
- **Global setup wipes and re-seeds the e2e database every run**; specs restore their own fixtures (delete created items; restore edited amounts through the real edit flow) because the suite shares one file in one worker.
- **Both superset fixes have dedicated specs**: the hamburger is clicked for real (a covering overlay would fail the hit-test) and every nav link's tap asserts the sheet closes.

### 7.3 Coverage Thresholds

No numeric coverage gate is configured; the standard is **every bug fixed gets a test that would have caught it** (all six engineering fixes in this build did), and every parity number asserted to the cent.

### 7.4 Pre-PR / Pre-Deploy Checklist

- [ ] `npm run lint` — zero errors (react-hooks v6 rules included)
- [ ] `npm run typecheck` — clean
- [ ] `npm test` — all unit suites green
- [ ] `npm run build` — standalone output builds
- [ ] `npm run test:e2e` — all specs green (run after the build)
- [ ] `bash scripts/smoke-test.sh` — 30/30 (pre-deploy)
- [ ] No secrets, `db/*.db`, `test-results/`, or `.auth/` staged

---

## 8. Build & Deployment

### 8.1 Production Build

```bash
npm run build   # next build (pins DATABASE_URL) + standalone assembly
                #   → .next/standalone/server.js (+ static/ + public/ copies)
npm start       # NODE_ENV=production, DATABASE_URL pinned, bun server.js
```

Static shells for the 7 routes are prerendered at build time; API routes are dynamic. The runtime resolves the schema-anchored `file:` URL (the standalone CWD is detected and mapped back to the repo root by `db-path.ts`).

### 8.2 Environment Variables

| Name | Required | Description | Default |
|------|----------|-------------|---------|
| `DATABASE_URL` | yes | SQLite location; relative values anchor to `prisma/schema.prisma`. Use an **absolute** path in production. | `file:../db/custom.db` |
| `AUTH_SECRET` | prod | HMAC key for session cookies (`openssl rand -hex 32`) | insecure dev constant + loud warning |
| `NEXT_PUBLIC_SITE_URL` | no | Canonical origin for metadata | `http://localhost:3000` |
| `PORT` / `HOSTNAME` | no | Standalone server bind | `3000` / `0.0.0.0` |

### 8.3 Docker Configuration

Not shipped (single-file SQLite + Node is the deployment model); `docs/DEPLOYMENT.md` documents the bare-metal flow. A container image would only need Node 20+, the standalone folder, `public/`, `.next/static`, and an absolute `DATABASE_URL` volume mount.

### 8.4 CI/CD Pipeline

No hosted CI — the local clean-check gate (`lint → typecheck → test → build → test:e2e`, plus the smoke script pre-deploy) is the only gate, enforced by convention in AGENTS.md/CLAUDE.md. Pushes go to `main` only, via the SSH wrapper runbook (`docs/ssh_git_wrapper_v3.py` + `docs/how-to-git-push-using-ssh-wrapper_SKILL.md`) with post-push remote verification.

---

## 9. Developer Handbook

### 9.1 Local Setup

```bash
npm install
npm run db:push     # db/custom.db
npm run db:seed     # demo@zerobalance.app / Demo1234!
npm run dev         # http://localhost:3000
```

Full check: `npm run lint && npm run typecheck && npm test && npm run build && npm run test:e2e`.

### 9.2 Common Commands

| Command | Location | Purpose |
|---------|----------|---------|
| `npm run dev` / `build` / `start` | package.json | Dev server / standalone build / prod boot |
| `npm run db:push · db:seed · db:migrate · db:reset` | package.json | Prisma CLI through wrappers (`env -u` discipline) |
| `npm test` / `test:watch` / `test:e2e` | package.json | Vitest once / watch / Playwright |
| `bash scripts/smoke-test.sh` | scripts/ | 30-step production API smoke (:3210) |
| `node scripts/capture-screenshots.mjs` | scripts/ | Regenerate `docs/screenshots/` (needs a build) |
| `python3 docs/ssh_git_wrapper_v3.py --key-file … --remote git@github.com:nordeim/zero-balance.git` | docs/ | Verified push (runbook in docs/) |

### 9.3 Code Style Rules

Strict TypeScript; ESLint 9 flat config with `eslint-config-next` and react-hooks v6 (no `set-state-in-effect`, no components created during render); no formatter config (style is enforced by review); money through `src/lib/money.ts`; colors through the constants + inline CSS vars; every new enum value added to `src/lib/constants.ts` and mirrored in `src/lib/validation.ts` + `tests/constants.test.ts`.

### 9.4 Git Workflow

`main` only; Conventional Commits; atomic commits; the clean-check gate before every push; pushes through the SSH wrapper (key materialized to a 0600 temp file outside the repo, shredded after); never commit `.env`, `db/*.db`, test artifacts, or the ssh shim.

---

## 10. Known Issues & Outstanding Tasks

| Priority | Issue | Impact | Status |
|----------|-------|--------|--------|
| LOW | Rate-limiter state is per-process | A multi-instance deploy would need shared storage | Documented (ADR-005); acceptable for the single-server model |
| LOW | `isMobile` emulation quirk: percentage heights resolve against the large viewport | Sheets must use `h-svh` (they do) | Mitigated + test-pinned |
| LOW | Radix Select click immediately after a state-changing dialog interaction can land on a stale node | A dropdown may not open if clicked mid-re-render (user-perceived: click again) | Mitigated in specs with a settle-wait; framework-level behavior |
| LOW | No hosted CI | The local gate is the only gate | By design for this repo; documented |

---

## 11. Key Files Reference

| File | Lines | Purpose |
|------|-------|---------|
| `src/components/budget/store.ts` | ~281 | The Zustand store: state, actions, modal stack — the app's client heart |
| `src/components/budget/dashboard-view.tsx` | ~554 | Hero, breakdown, stat cards, donut, guidelines, quick actions |
| `src/components/budget/budget-item-dialog.tsx` | ~309 | Add/Edit budget item (lazy form init pattern) |
| `src/components/budget/net-worth-view.tsx` | ~420 | Net-worth summary + assets/liabilities tabs and cards |
| `src/components/budget/login-card.tsx` | ~303 | Three-state reference auth card |
| `src/components/budget/items-view.tsx` | ~236 | Shared item views (useShallow pattern) |
| `src/components/budget/calculator-dialog.tsx` | ~224 | Category calculator (category-adaptive chrome) |
| `src/components/budget/sidebar.tsx` | ~212 | Desktop rail + mobile header/sheet (both superset fixes) |
| `src/lib/validation.ts` | ~186 | Every zod schema (boundary contract) |
| `src/lib/constants.ts` | ~118 | Enums, labels, measured palette — single source of truth |
| `src/lib/db-path.ts` | ~107 | Schema-anchored SQLite URL resolution (15-test contract) |
| `src/lib/auth.ts` | ~104 | scrypt + HMAC cookie sessions |
| `src/lib/dashboard.ts` | ~92 | Dashboard/net-worth aggregations (pure) |
| `src/lib/serializers.ts` | ~81 | Row → payload translation |
| `src/lib/money.ts` | ~66 | Integer-cent arithmetic + formatters |
| `src/lib/rate-limit.ts` | ~63 | Fixed-window limiter + clientIp |
| `src/lib/line-item-service.ts` | ~28 | Parent recalculation rule |
| `prisma/schema.prisma` | ~120 | Five models, cascades, indexes |
| `prisma/seed.ts` | ~234 | Idempotent demo seed (the e2e fixture) |
| `src/app/globals.css` | ~214 | Tailwind v4 `@theme` + all trap mitigations |
| `tests/e2e/mobile-navigation.spec.ts` | — | Both superset fixes pinned |
| `scripts/smoke-test.sh` | — | 30-step production API smoke |

---

## 12. Glossary

| Term | Definition |
|------|------------|
| **Net zero (rule)** | The budgeting identity `Income = Savings + Expenses`; the hero card's goal state |
| **Net Balance** | `income − savings − expenses`; displayed with an explicit `+`/`−` prefix |
| **Allocation %** | `(savings + expenses) / income × 100` — the hero's progress bar (one decimal) |
| **Budget item** | One income / savings / expense entry (type, classification, amount, frequency, status…) |
| **Classification** | `need` / `want` / `savings` — drives the donut slices and badge colors |
| **Line item** | A sub-entry of an expense category (calculator); the parent's amount is the sum of its line items |
| **Category Calculator** | The category-adaptive dialog ("Rent Calculator / Break down your rent…") managing line items |
| **Superset (fix)** | A reference bug fixed in the clone — behavior the reference lacks, pinned by tests |
| **Schema-anchored URL** | A relative `file:` SQLite URL resolved against `prisma/schema.prisma` (not the CWD) |
| **Schema anchor** | The first directory containing `prisma/schema.prisma` from the candidate roots (source tree, standalone build's repo, CWD) |
| **StorageState** | Playwright's saved auth context; the e2e suite replays one login to respect the rate limiter |
