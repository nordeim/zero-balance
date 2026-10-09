# Session 44 — Fresh verification & parity iteration v22

> Continuation note: `docs/session_43.md` holds the incoming session-41
> conversation summary (the record this session was briefed to review),
> so this work session's formal log lives here. Work-session numbering
> continues the odd convention: 15 → 17 → 19 → 21 → 23 → 25 → 27 → 29 →
> 31 → 33 → 35 → 37 → 39 → 41 → 43 (this session), iteration v21 →
> **v22**.

Date: 2026-10-09 · Baseline: `dee3176` (v21 code `34f0911`, all green per
its records) · Plan: `docs/remediation-plan-v22.md` · Outcome: **2 finding
groups fixed TDD-first — (G1) the verify-email spec's parked-pointer race
(a deterministic flake on a correct app: the Create-account click parks
the mouse where the swapped-in Verify button renders, and its 200ms
hover transition read mid-flight; fixed with the park + settle
discipline); (G2) the line-item sub-dialog's THIRD dialog family measured
live for the first time (the reference caps its panel at 85vh with
`space-y-5` form gaps — the clone rode the generic 90vh/`space-y-6`
budget family) and matched + pinned (the budget dialog's 90vh pinned too,
so the family split can't regress); 1 new e2e test; 108 unit · 143 e2e ·
35 smoke all green; mobile-nav R1–R4, the SEO pair, and the data drift
(sixteenth check) all re-verified clean.**

## What happened

1. **Workspace refresh**: the sandbox had been reset — both repos
   re-cloned (`zero-balance` at `dee3176`, `scandihaven` at `d4789c3`),
   the environment rebuilt (`npm install`, `.env` with
   `DATABASE_URL="file:../db/custom.db"` re-created from the tracked
   `.env.example`, `db/` at the repo root re-pushed + re-seeded — the
   demo workspace with the pre-verified demo user). Full doc chain
   re-read (AGENTS, CLAUDE, README, PAD, SKILL, session_42,
   remediation-plan-v21, worklog, session_43); the pulled v21 changeset
   verified in the code first (`robots.ts`/`sitemap.ts` in the build
   output, the verify-email API family, the `verification.ts` seam).

2. **Baseline chain — one deterministic failure (the session's first
   finding)**: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
   **141/142 e2e** — `verify-email.spec.ts:47` "the register flow lands
   on the verify state with the reference chrome" failed at the 44px
   primary-button color: expected `rgb(15, 23, 42)` (#0f172a), received
   `rgb(19, 27, 46)` — a uniform +4/+4/+4 offset. **Triage probe**
   (pointer parked vs away on the :3100 build): the resting bg IS
   `#0f172a` (pointer away); the parked mouse (left at the
   Create-account click point, over the swapped-in Verify button) drives
   the `transition-all duration-200` toward the `#1e293b` hover — the
   measured value is ~27% through the transition, and the settled parked
   value is the full `rgb(30, 41, 59)`. The app is correct (the
   v13-pinned sign-up-family hover); the SPEC raced the transition. The
   prior session's green first run was timing luck → **G1**.

3. **Code audit** (`skills/code-review-and-audit` native-CLI fallback):
   Phase 1 green (the baseline above); Phase 2: `npm audit` = the same 5
   dev-only ESLint `braces` advisories (no patched release — accepted,
   unchanged); the secret-pattern scan clean (no key material anywhere
   outside the documented redacted wrapper placeholder).

4. **Audit infrastructure**: agent-browser sessions `ref24`/`clone24`
   (desktop 1280×800, resized per check), both sites logged in (the
   reference with the brief's credentials; the clone with the seeded
   demo user inside one `with-server.sh` invocation — the sandbox still
   reaps background processes between commands).

5. **Mobile navigation (task focus) re-verified end-to-end, all four
   live**: R1 (the reference's TWO toast containers still intercept the
   burger's center hit at (38,30) — `pe:auto`, z-100; the clone's hit is
   DIRECT on the svg, viewport `pe:none`; burger 28×28 at (24,16) both).
   R2 (the reference's sheet still traps after nav — `sheetStillOpen:
   true`; the clone's sheet CLOSES; sheet 288px + Income link (20,185)
   247×32 identical both). R3 (nothing active on `/` on the reference —
   all five links `rgb(63,63,70)`/400, no `<nav>` landmark; the clone
   highlights Dashboard). R4 (the reference overflows 395px on `/` +
   `/dashboard`, 464px on `/networth`; the clone fits 390 on ALL six
   routes). The Tailwind v4 pins hold.

6. **Data drift check clean (sixteenth consecutive)**: reference
   unchanged since session 19 (allocation 30.5%, income `$5000.00`/1
   item, savings `$1000.00`/1, expenses `$525.00`/4 items, Balance
   `$3475.00`).

7. **SEO check (the brief's standing ask) PASSES**: the clone serves
   `/robots.txt` (allow-all + the sitemap link) and `/sitemap.xml` (five
   URLs, weekly, priorities 1/0.8) — verified live on :3200 against the
   reference's files; head metadata parity re-verified on `/login`
   (title/description/OG/Twitter/apple/canonical + manifest; the
   origin-keyed fields correctly differ, `NEXT_PUBLIC_SITE_URL`).

8. **The v22 sweep — the session-42 log's three suggested surfaces:**
   - **Mobile calculator pair (VLM + DOM, 390×844)**: the first pair
     flagged three diffs — the toast (the documented success-toast
     superset), the "Will update category total" hint (data-driven: the
     reference's Rent parent `$25.00` equals its line-item sum so its
     identical conditional hides it; the clone's seeded `$1850` Rent
     does not), and the row actions "missing" on the clone — the last
     DOM-verified as a SCREENSHOT-PROCEDURE ARTIFACT: the reference's
     shot caught its row under the parked mouse (an earlier real click
     had left the pointer inside the row — `.group:hover` matched,
     opacity 1) while the clone's pointer sat at its Save button.
     Re-measured with the pointer parked away on BOTH sides: identical
     container classes, opacity 0 at rest, opacity 1 under a real row
     hover, 32×32 buttons, 16×16 icons, near-black/red colors. The
     re-taken pair flagged only the X-close claim — DOM-refuted for the
     FOURTH consecutive pass (identical 29×36 at mobile, 0px border,
     transparent bg, 16px svg, `#0a0a0a`, radius 6 both).
   - **Line-item EDIT sub-dialog (measured live, first time — the
     nested dialog's populated state)**: **G2** — the reference's
     sub-dialog is its THIRD dialog family: `max-w-2xl` +
     `max-h-[85vh]` + `overflow-y-auto` + form `p-6 space-y-5`
     (desktop 672×680, mobile 358×717, form 1002px, 20px row gaps; the
     calculator family is max-w-3xl/85vh/overflow-hidden — already
     matched; the budget-item family is max-w-2xl/90vh/`space-y-6` —
     also already matched). The clone's sub-dialog rode the generic
     `.zb-modal-panel` budget family: 90vh cap (desktop 720, mobile
     760) + 24px gaps. Inputs/buttons/widths identical.
   - **Keyboard sweeps (dashboard + income views, both sites)**: Tab
     order IDENTICAL (the five rail links → the Add button → the search
     input → the filter select); the nav links render the blue 2px
     `#3b82f6` sidebar-ring on both; the interactive elements render
     the shadcn 1px `#0a0a0a` ring + ambient on both (the clone's
     computed strings carry extra TRANSPARENT lead layers — invisible;
     the truncation lesson applied twice mid-sweep before the full
     reads); the stat buttons keep the browser-default outline on both.
     **No findings.**

9. **2 finding groups** (`docs/remediation-plan-v22.md`) — the plan
   written, validated against the codebase, then executed TDD-first.

10. **TDD RED → GREEN (G1 — the parked-pointer race)**: the RED was the
    baseline failure itself → `registerFreshAccount` parks the pointer
    at (5,5) + settles 350ms after the verify-state heading assert (the
    documented transition discipline, now encoding the state-swap
    corollary) → the file GREEN (all tests, deterministic on re-run).

11. **TDD RED → GREEN (G2 — the third dialog family)**: the new
    dialog-buttons spec test "the line-item sub-dialog carries the
    reference's third family (v22 G2)" RED at the exact unfixed state
    (`vhCap` 90, `formRowGap` 24) → `line-item-dialog.tsx`'s
    `DialogContent` gains the inline `maxHeight: "85vh"` (the
    calculator's precedent) + the form flips to `p-6 space-y-5` →
    GREEN — the test ALSO pins the budget-item dialog's 90vh cap so
    the family split can't regress into a global restyle.

12. **Full chain**: lint ✓ · typecheck ✓ · **108/108 unit** ✓ · build ✓
    · **143/143 e2e** ✓ (142 + 1 new) · **35/35 smoke** ✓.

13. **Live parity re-verification**: G2's sub-dialog panel re-measured
    on :3200 — desktop 672×680 (maxH 680px, 85vh), mobile 358×717
    (maxH 717.4px, 85vh), form `p-6 space-y-5` — exactly the
    reference's measurements at both viewports. The VLM pair on the
    fixed sub-dialog flagged only the X-close claim (refuted, the
    fourth time). The demo DB restored after the audit's line-item
    mutation (the stray "Contents Insurance" row deleted, the Rent
    parent re-set to its seeded `$1850` — the seed's create-only
    upsert leaves user edits alone by design).

14. **Screenshots**: all 15 regenerated (03–06 + 08 changed — the
    calculator shot rides the G2 sub-dialog family; the items views
    carry the seed's relative dates) — the rest byte-identical
    (deterministic captures).

15. **Docs aligned**: README (counts 143, the v22 plan row), CLAUDE.md
    (counts + the e2e contract's parked-pointer note + the family pin),
    AGENTS.md (the v22 pin paragraph — the parked-pointer +
    screenshot-procedure lessons), SKILL (state 108/143/35, lesson 40,
    Appendix B row), the probe README (the v22 catalog: six probes),
    this log, and the worklog.

## Suggested next steps

- The **"5 attempts exhausted" lockout path** on the reference remains
  unmeasurable without burning a reference account's five attempts (the
  session-42 log's standing note; the clone implements the documented
  re-send requirement).
- A **VLM pair on the budget-item dialog's MOBILE state** (this pass
  measured its 90vh cap in the DOM but never ran the visual pair — the
  family split is pinned by the spec, the pixels are not).
- A **keyboard sweep of the mobile sheet** (the R2 flow's focus
  semantics under Tab/Arrow keys — the desktop rail is swept, the
  sheet's focus trap never was).
