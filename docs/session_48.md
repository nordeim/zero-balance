# Session 48 — Parity iteration v24 (auth-form mobile families + the v4 space-y-1.5 label gap)

> Continuation note: `docs/session_47.md` holds the incoming session-45
> conversation summary (the record this session was briefed to review),
> so this work session's formal log lives here. Work-session numbering
> continues the convention: 15 → 17 → 19 → 21 → 23 → 25 → 27 → 29 →
> 31 → 33 → 35 → 37 → 39 → 41 → 43 → 45 → 47 (this session), iteration
> v23 → **v24**.

Date: 2026-10-09 · Baseline: `dd49681` (v23 code `1420e55`, all green per
this session's re-run) · Plan: `docs/remediation-plan-v24.md` · Outcome:
**two REAL app fixes — the first visual-drift findings since v22, both
found by DOM measurement behind a CLEAN VLM verdict: (G1) the auth
forms' MOBILE responsive families (the reference runs THREE distinct
families — sign-in `h-11 sm:h-12`, sign-up/forgot `h-10 sm:h-11` (40px
at mobile) with the sign-up font dropping to 14px; the clone rendered
the flat 44px sign-in family on all three states); (G2) the v4
`space-y-1.5` inline-label trap (the label→input gap collapsed to 4px
where the reference renders 10px at EVERY viewport — the v9 globals.css
v3-pin stopped at `space-y-2`); 5 new e2e; 108 unit · 150 e2e · 35
smoke all green; mobile-nav R1–R4, the SEO pair, and the data drift
(18th check) all re-verified clean.**

## What happened

1. **Workspace refresh**: `git pull` fast-forwarded `1420e55 →
   dd49681` (the session-47 log doc — the environment survived the
   boundary: `.env` with `DATABASE_URL="file:../db/custom.db"`
   verified, `db/` at the repo root with the seeded demo workspace,
   node_modules intact). Full doc chain re-read (AGENTS, CLAUDE, README,
   PAD, SKILL, session_46, remediation-plan-v23, worklog, session_47);
   the v23 changeset verified in the code first (the two spec pins +
   the probe catalog).

2. **Baseline chain fully green on the FIRST run**: lint ✓ · typecheck
   ✓ · 108/108 unit ✓ · build ✓ (robots.txt + sitemap.xml prerendered)
   · **145/145 e2e** ✓ · **35/35 smoke** ✓.

3. **Code audit** (`skills/code-review-and-audit` native-CLI fallback):
   Phase 1 green (the baseline above); Phase 2: `npm audit` = the same
   5 dev-only ESLint `braces` advisories (no patched release —
   accepted, unchanged); the secret-pattern scan clean (matches only
   in the documented runbook, the redacted wrapper placeholder, and
   the repo's own prompt-history docs); the v23 changeset (`1420e55`)
   diff-reviewed — clean, commented, pinned; scandihaven unchanged at
   `d4789c3` (patterns already reflected).

4. **Audit infrastructure**: the shared parity browser (one tab — the
   open+settle discipline), both sites logged in (the reference with
   the brief's credentials; the clone with the seeded demo user inside
   one `with-server.sh` invocation), the :3200 parity server booted
   per command.

5. **Mobile navigation (task focus) re-verified end-to-end (18th
   consecutive), all four live**: R1 (the reference's TWO toast
   containers still intercept the burger's center hit at (38,30) —
   `pe:auto`, z-100; the clone's hit is DIRECT on the svg, viewport
   `pe:none`; burger 28×28 at (24,16) both), R2 (the reference's sheet
   still traps after nav — `sheetStillOpen: true`; the clone's sheet
   CLOSES; sheet 288px + Income link (20,185) 247×32 identical both),
   R3 (nothing active on `/` on the reference — all five desktop-rail
   links `rgb(63,63,70)`/400, no `<nav>` landmark; the clone highlights
   Dashboard), R4 (the reference overflows 395px on `/`+`/dashboard`,
   464px on `/networth`; the clone fits 390 on ALL six routes). The
   Tailwind v4 pins hold.

6. **v23 G1 re-verified live (the newest change)**: the mobile sheet's
   keyboard sweep re-run on both sites — identical initial container
   focus, the five links at identical positions cycling under real Tab
   presses with the wrap-around loop, the sheet trapping through the
   loop, Escape closing both.

7. **Data drift check clean (18th consecutive)**: the reference
   unchanged since session 19 (allocation 30.5%, Balance `$3475.00`,
   income `$5000.00`/1, savings `$1000.00`/1, expenses `$525.00`/4,
   guidelines 30.5/92.3/4.6).

8. **SEO check (the brief's standing ask) PASSES**: the clone serves
   `/robots.txt` (allow-all + the sitemap link) and `/sitemap.xml`
   (five URLs, weekly, priorities 1/0.8) — verified live on :3200
   against the reference's files (origin-keyed fields correctly
   differ, `NEXT_PUBLIC_SITE_URL`).

9. **The v24 sweep — the session-46 log's two suggestions + one bonus
   surface, all DOM-paired:**
   - **Register SIGN-UP state at MOBILE (suggestion 1 — VLM + DOM,
     390×844)**: the VLM pair returned IDENTICAL — but the DOM pair
     found the session's two real findings (G1 + G2 below; the 6th
     consecutive form-scale VLM blind spot — the deltas are 4px/2px/
     6px, below VLM resolution). Everything else matched: h2 20px/700
     centered, placeholders, input width/radius/border/bg, the Back
     link 127×20, the submit gap 12, the h2→label gap 20, no overflow.
   - **Mobile sheet ARROW-key sweep (suggestion 2)**: full parity —
     arrows are inert on both sites (focus stays on the container, no
     scroll, sheet stays open; the reference implements no roving).
   - **FORGOT-password state (bonus, first-time pair)**: desktop
     identical (h2 24/700, input 368×44, Send 368×44, Back 127×20,
     form space-y-4 sm:space-y-5); mobile carries the same G1+G2
     findings.
   - **Dialog label→input gap re-verified (the v9 pin holds)**: 12px
     on both sites (inline leading-none labels + the pinned
     space-y-2) — which isolated the v9 pin's scope gap as G2's
     root cause.
   - The session-46 log's third suggestion (the 5-attempts lockout)
     remains unmeasurable — the standing note.
   - **Probe lesson 42 (this session's own)**: two "reference" class
     dumps read the CLONE's forgot page left in the shared browser
     tab by an intervening `with-server.sh` invocation — the
     session-46 false-read lesson repeating; the census pattern
     (read ALL states in ONE eval right after a fresh open) is the
     reliable form, and the CLASS ATTRIBUTE is the tie-breaker when
     geometry reads disagree.

10. **2 finding groups** (`docs/remediation-plan-v24.md`) — the plan
    written, validated against the codebase, then executed TDD-first:
    - **G1 (app fix)**: per-mode height/font branches in
      `login-card.tsx` — `INPUT_CLS` now carries only the
      viewport-invariant chrome; sign-in `h-11 sm:h-12` +
      `text-base md:text-sm` (unchanged), sign-up `h-10 sm:h-11` +
      `text-sm sm:text-base md:text-sm`, forgot `h-10 sm:h-11` +
      `text-base md:text-sm`; the submit button follows its state's
      height family.
    - **G2 (app fix)**: the globals.css v3-pin extended to
      `space-y-1.5` (`.space-y-1.5 > * + * { margin-block-start:
      0.375rem }` — the v9 space-y-2 pattern applied to the auth
      card's field wrappers; the dashboard's two block-child
      space-y-1.5 wrappers are layout-equivalent and unaffected).

11. **TDD execution**: the 5 new tests written FIRST (RED: 4 failing —
    the sign-up/forgot mobile families + the two label-gap tests; the
    sign-in guard passing) → both fixes applied → GREEN (20/20 in the
    login-parity spec) → **pin-sanity mutations** (the sign-up input
    heights 40→44 and the label gap 10→4 both went RED, restored via
    unique-context edits) → the live census re-run on :3200 confirms
    the clone now matches the reference's auth-form table exactly
    (signin 44/16, signup 40/14, forgot 40/16, gaps 10, relMt 6).

12. **Full chain**: lint ✓ · typecheck ✓ · **108/108 unit** ✓ · build
    ✓ · **150/150 e2e** ✓ (145 + 5 new) · **35/35 smoke** ✓.

13. **Screenshots**: all 15 regenerated — `01-login.png` and
    `14-login-error.png` changed (the label gap fix is
    viewport-invariant — the desktop auth forms correctly moved 6px
    closer to the reference), the other 13 byte-identical.
    `.env.example` verified matching the codebase.

14. **Docs aligned**: README (counts 150, the v24 plan row), CLAUDE.md
    (counts + the v24 surface note), AGENTS.md (the v24 pin
    paragraph), SKILL (state 108/150/35, lesson 42, Appendix B row),
    the probe README (the v24 catalog: two probes + the arrow sweep),
    this log, and the worklog.

## Suggested next steps

- A **VLM + DOM pair on the auth forms at the sm breakpoint
  (640–768)** — the band where the reference's sign-up font renders
  16px (`text-sm sm:text-base`'s middle step); this pass pinned the
  band's classes but did not visually pair it.
- A **focus-ring sweep of the auth inputs' focus-visible state** (the
  v13 pin covers plain `:focus`; the `:focus-visible`-only submit
  button ring was never paired on the reference).
- The **5-attempts-exhausted lockout path** remains the standing
  unmeasurable (would burn a reference account's attempts).
