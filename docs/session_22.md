# Session 22 — Fresh verification & parity iteration v11

> Continuation note: `docs/session_21.md` holds the incoming session-19
> conversation summary (the record this session was briefed to review),
> so this work session's formal log lives here. Work-session numbering
> continues the odd convention: 15 → 17 → 19 → **21** (this session),
> iteration v10 → **v11**.

Date: 2026-10-08 · Baseline: `061a16f` (v10, all green) · Plan:
`docs/remediation-plan-v11.md` · Outcome: **4 finding groups fixed
TDD-first; 96 unit · 107 e2e · 30 smoke all green; live parity
re-verified side by side.**

## What happened

1. **Workspace + doc chain.** `git pull` fast-forwarded to `061a16f`
   (only `docs/session_21.md` — the session-19 conversation summary).
   Full doc chain re-read (AGENTS, CLAUDE, README, PAD, SKILL,
   session_20/21, remediation-plan-v10, worklog). Environment intact
   (`.env` `DATABASE_URL="file:../db/custom.db"`, `db/custom.db` at the
   repo root, `.env.example` matching, node_modules present).

2. **Baseline chain at `061a16f` fully green**: lint ✓ · typecheck ✓ ·
   96/96 unit ✓ · build ✓ · 104/104 e2e ✓ · 30/30 smoke ✓. The v10 pins
   spot-checked in the code first (the sheet's `highlightActive` default
   restored with its evidence comment).

3. **Audit infrastructure.** Four agent-browser sessions (`ref11`/
   `clone11` desktop 1280×800, `ref11m`/`clone11m` 390×844), both sites
   logged in; the parity server on :3200 per command via `with-server.sh`
   (the sandbox still reaps background processes). Reference login needed
   a hydration wait on the mobile session (the SPA form isn't in the
   first paint).

4. **Data drift check**: reference UNCHANGED since session 19 (allocation
   30.5%, expenses `$525.00` with the documented 4th `$0.00`
   "Miscellaneous" residual); clone seed arithmetic intact
   (`+$2065.00`, 62.8%); donut legends value-DESC both sides.

5. **Mobile navigation (task focus) re-verified end-to-end**: R1
   re-confirmed live — the ref's toast container still intercepts its
   burger's center hit (elementFromPoint → the container; the clone's hit
   is DIRECT on the svg); R2 re-confirmed — tapping Income in the ref's
   sheet navigated to `/income` with `sheetStillOpen: true` (and the v10
   finding re-confirmed: its Income link renders the FULL active style —
   white + the 135deg forest-medium→lime gradient + fw 500); the clone's
   sheet CLOSED on nav and fits 390px; R4 re-confirmed — ref scrollWidth
   395 at 390, clone 390; burger/topbar geometry identical (28×28 at
   (24,16), "ZeroBalance" 20px/700 at (68,16)); the clone's sheet
   highlights Dashboard on `/` (v10 fix + superset #3 intact).

6. **Fresh angles swept (first-ever computed-style measurements)**:
   tablet/intermediate breakpoints 767/768/1024 (identical rail↔mobile
   switching, identical content column at 768 — the ref offsets main,
   the clone pads it, the pixels match); desktop rail hover (identical);
   hero "Under Budget" status badge (identical); filter card geometry +
   live search behavior (identical — "zzz" reaches the same filtered
   empty state on both); item-card badge census (identical); dialog
   overlay + panel (identical); stat cards (identical); calculator empty
   state (identical); QuickActionCard icons (identical); Cancel
   primitive focus (identical); logout affordance (NONE on either site —
   the clone's store/API logout stays a headless superset).

7. **The near-false-finding**: the ref's dialog panel box-shadow read
   "shadowless" through a `.slice(0, 70)` — the full string carries the
   identical visible layer (`rgba(0,0,0,0.25) 0 25px 50px -12px`) behind
   two transparent lead layers. Recorded as methodology lesson 25
   (never truncate computed multi-layer strings); the dialog/sheet
   shadows are identical, no fix needed.

8. **Four finding groups** (`docs/remediation-plan-v11.md`):
   - **G1**: empty-state headings 18px → the reference's 20px
     (`text-lg` → `text-xl`; measured on its filtered income empty state
     AND its live liabilities empty state — the reference account has
     zero liabilities, so that state was reachable without any mutation
     this pass).
   - **G2**: the `.zb-btn-add` gradient-button family — rest ambient is
     v3's BARE shadow (two 0.1 layers, every size), the outline variant
     carries v3's shadow-sm (0.05), and `:focus-visible` renders the
     reference's shadcn ring (white zero-spread inner + 1px `#0a0a0a` +
     the variant's ambient + v3's transparent 2px outline at offset 2)
     instead of the browser-default `outline: auto`. The trap-5
     `--shadow-sm` pin stays for the navbar it was measured on.
   - **G3**: the Add buttons' Plus icons 20px → the reference's 16px
     (7 sites; the calculator and Save icons already matched).
   - **G4**: the session-1 `:hover { opacity: 0.9 }` fade removed — the
     reference's gradient buttons have NO hover state (measured with
     `matches(":hover")` on three surfaces).

9. **TDD**: 3 new/extended specs (empty-states ×2 extended, the new
   dialog-buttons "button ambient shadows + focus-visible ring (v11 G2)",
   the new tokens "gradient Add-button chrome (v11)" describe with 2
   tests) — **RED confirmed** (5 failures, each at the exact unfixed
   value), then the fixes (3 component files + globals.css), then
   **GREEN**: the affected files 26/26, full suite **107/107** (one
   not-found navigation flake on the first full run — passes in
   isolation, the known timing-race class; clean on the re-run).

10. **Full chain**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ ·
    **107/107 e2e** ✓ · 30/30 smoke ✓.

11. **Live parity re-verification on fresh sessions** (`ref12`/`clone12`):
    the Add Income button 147 = 147 with 16px icons and identical
    visible shadow layers; the empty heading 20px/600/28px both sides;
    the focused Save Item's ring **byte-identical** to the reference's
    measurement; the calculator's Add Item / Add First Item shadows
    matched. 13 screenshots regenerated (10 changed — the Add-button
    deltas; login/mobile-menu/not-found unchanged as their surfaces
    carry no `.zb-btn-add` buttons).

12. **Docs aligned**: README (counts 107, the plan-v11 row), CLAUDE.md
    (counts, the shadow-scale + full-string notes), AGENTS.md (the v11
    pin paragraph), SKILL (state 96/107/30, lessons 25–26, Appendix B
    row), the probe README v11 catalog, this log, and the worklogs.
