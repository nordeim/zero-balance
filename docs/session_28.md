# Session 28 — Fresh verification & parity iteration v14

> Continuation note: `docs/session_27.md` holds the incoming session-25
> conversation summary (the record this session was briefed to review),
> so this work session's formal log lives here. Work-session numbering
> continues the odd convention: 15 → 17 → 19 → 21 → 23 → 25 → 27 (this
> session), iteration v13 → **v14**.

Date: 2026-10-08 · Baseline: `931bfcd` (v13 code `8b634fe`, all green) ·
Plan: `docs/remediation-plan-v14.md` · Outcome: **4 finding groups fixed
TDD-first (3 finding groups + the in-flight tooltip-chrome expansion);
96 unit · 119 e2e · 30 smoke all green; live parity re-verified; 2 of 15
screenshots changed (the net-worth chip + tab icons — the expected
visual delta), the other 13 byte-identical.**

## What happened

1. **Workspace + doc chain.** `git pull` fast-forwarded `8b634fe →
   931bfcd` (`docs/session_27.md` — the session-25 conversation
   summary, the only change; the HTTPS remote worked this time). Full
   doc chain re-read (AGENTS, CLAUDE, README, PAD, SKILL, session_26/27,
   remediation-plan-v13, worklogs). Environment intact (`.env`
   `DATABASE_URL="file:../db/custom.db"`, `db/custom.db` at the repo
   root, `.env.example` matching, vitest + playwright configs in place).

2. **Baseline chain at `931bfcd` fully green**: lint ✓ · typecheck ✓ ·
   96/96 unit ✓ · build ✓ · 115/115 e2e ✓ (one not-found navigation
   flake on the first run — the known timing-race class, clean in
   isolation and on the full re-run) · 30/30 smoke ✓. The v13 pins
   spot-checked in the code first (register 409 text, sign-up
   placeholders, the INPUT_CLS focus ring).

3. **Code audit (skills: code-review-and-audit, native CLI
   fallback).** Phase 1/4 green; Phase 2: `npm audit` = 5 high, all the
   dev-only ESLint `braces` chain (unchanged advisory, no patched
   release — accepted + documented); secret scan clean (0 hits in
   src/scripts/tests; the only "BEGIN OPENSSH" matches remain the
   wrapper constant + runbook artifact). Phase 3: the v13 changeset
   re-reviewed clean (evidence-commented, all pins test-covered).

4. **Audit infrastructure rebuilt**: `scripts/with-server.sh` recreated
   (the per-command :3200 parity-server wrapper, referenced by the
   probe README since v10 — now committed) + four agent-browser
   sessions (`ref15`/`clone15` desktop 1280×800, `ref15m`/`clone15m`
   390×844) both sites logged in. One `EAGAIN` daemon hiccup and the
   lingering zombie `ref13` worked around with timeout-wrapped closes.

5. **Data drift check**: reference UNCHANGED since session 19
   (allocation 30.5%, income `$5000.00`/1 item, savings `$1000.00`,
   expenses `$525.00`/4 items, balance `$3475.00`); clone seed intact
   (62.8%, `+$2065.00`).

6. **Mobile navigation (task focus) re-verified end-to-end**: R1
   re-confirmed live (the ref's two `pe:auto` toast containers intercept
   the burger's center hit at (38,30); the clone's hit is DIRECT on the
   svg; burger 28×28 at (24,16) both). R2 re-confirmed (tapping Income
   in the ref's sheet navigated with `sheetStillOpen: true`; the
   clone's sheet CLOSED + 390px fit at `/income`). R3 re-confirmed (no
   ref link active on `/` — all five rail links `#3f3f46`/400; the
   clone highlights Dashboard — white + gradient + 500). R4
   re-confirmed (ref scrollWidth 395; clone 390 on `/` and `/income`).
   Sheet link geometry identical (Income at (20,185) 247×32 both).

7. **Fresh angles swept (first-ever measurements)**: the net-worth
   TABLIST keyboard flow (roles/aria-selected/ArrowRight activation —
   identical), the dialog INITIAL focus (the ref leaves focus on the
   trigger — the clone's Radix trap is the a11y superset, documented),
   INVALID-input validation (negative amount → silent rejection both,
   no fixture residue on either side), guideline + accordion hover
   states (none both), a user-select sweep (auto both), and a
   **three-page VLM screenshot comparison** (dashboard/expenses/
   networth) whose flagged diffs were each DOM-verified: 3 real (below),
   4 refuted (the summary divider and ratio icon are identical; the
   active-tab tint is identical `rgb(220,252,231)`; the expenses badge
   wrap + payment-method footers are data-driven).

8. **4 finding groups** (`docs/remediation-plan-v14.md`):
   - **G1**: the donut hover TOOLTIP — the clone rendered the raw
     number ("7370") with recharts 3's bare chrome (#cccccc border, no
     radius/shadow, sector-colored item text); the reference renders
     "$6025.00" in the recharts-2 chrome (#e5e7e3 border, radius 8,
     `0 4px 12px` shadow, black item row). All four axes pinned
     (`formatter` + `contentStyle` + `itemStyle`).
   - **G2**: the net-worth TAB icons — the ref's triggers carry 16px
     lucide circle-arrow-up/down (`mr-2`, currentColor: active
     green-900 / inactive gray); the clone was text-only.
   - **G3**: the net-worth HEADER icon chip — the ref renders the
     48×48 forest→lime gradient chip (radius 12, 24px white
     lucide-trending-up) at BOTH viewports; the clone's h1 row was
     bare. (The items-view chips were pinned in v4; this page's chip
     had never been measured.)

9. **TDD RED → GREEN**: 4 new e2e specs (dashboard G1; networth G2 +
   G3 desktop + G3 mobile) — RED confirmed at the exact unfixed values
   ("7370", icons not found, chip null), then GREEN after the 3-file
   fix. Three test-bug fixes mid-flight: the recharts hover dispatched
   synthetically (a Playwright `.hover()` loops forever on the
   mouse-following tooltip — lesson 31), the tab-icon color asserted
   per-STATE (the active tab's icon is correctly green at rest — the
   premise error), and the post-click icon color read after the
   documented `transition-all` settle. The G1 scope GREW during GREEN:
   the live re-verification caught the tooltip's border/radius/shadow/
   item-color chrome drift (recharts 3 defaults) — pinned with
   `contentStyle` + `itemStyle` and locked by four new CSS assertions.

10. **Full chain**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ ·
    **119/119 e2e** ✓ (one login-parity 409 flake on an intermediate
    run — clean in isolation and on the full re-run) · 30/30 smoke ✓.

11. **Live parity re-verification on a fresh clone session**: the
    tooltip reads "Need : $7370.00" with the full ref chrome (padding
    10, radius 8, `#e5e7e3` border, the exact shadow, black item row); the chip measures 48×48 at (288,38) with
    radius 12 + the exact 135deg gradient + 24px white trending-up, h1
    at 348 (gap-3); the tab icons measure 16×16 `mr-2` with the exact
    active/inactive color pair.

12. **Screenshots**: all 15 regenerated — `06-networth.png` and
    `12-mobile-networth.png` CHANGED (the chip + tab icons are visible
    surfaces; VLM-verified the chip + icons render), the other 13
    byte-identical (the tooltip is hover-only, invisible in static
    shots).

13. **Docs aligned**: README (counts 119, plan-v14 row), CLAUDE.md
    (counts, the recharts-3 tooltip trap + the synthetic-hover pattern),
    AGENTS.md (the v14 pin paragraph), SKILL (state 96/119/30, lessons
    31–32, Appendix B row), the probe README (v14 catalog + the
    VLM-sweep discipline + the session-cookie note), `scripts/
    with-server.sh` committed, this log, and the worklogs.
