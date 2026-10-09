# Session 46 — Fresh verification & parity iteration v23

> Continuation note: `docs/session_45.md` holds the incoming session-43
> conversation summary (the record this session was briefed to review),
> so this work session's formal log lives here. Work-session numbering
> continues the odd convention: 15 → 17 → 19 → 21 → 23 → 25 → 27 → 29 →
> 31 → 33 → 35 → 37 → 39 → 41 → 43 → 45 (this session), iteration v22 →
> **v23**.

Date: 2026-10-09 · Baseline: `93e3b70` (v22 code `38def33`, all green per
this session's re-run) · Plan: `docs/remediation-plan-v23.md` · Outcome:
**a clean verification pass — the app matched the reference on every
measured axis, so the two finding groups are TEST-PINS of newly measured
surfaces: (G1) the mobile sheet's keyboard semantics (the Tab focus loop
through the five links + the blue #3b82f6 sidebar-ring focus layer —
measured live for the first time, both sites, then pinned); (G2) the
register verify-email state's MOBILE chrome (the responsive mobile scale
— 56px circle / 28px icon / 20px h2 — measured for the first time at
390×844, then pinned); 2 new e2e; 108 unit · 145 e2e · 35 smoke all
green; mobile-nav R1–R4, the SEO pair, and the data drift (17th check)
all re-verified clean.**

## What happened

1. **Workspace refresh**: `git pull` fast-forwarded `38def33 → 93e3b70`
   (the session-45 log doc — the environment survived the boundary:
   `.env` with `DATABASE_URL="file:../db/custom.db"` verified, `db/` at
   the repo root with the seeded demo workspace, node_modules intact).
   Full doc chain re-read (AGENTS, CLAUDE, README, PAD, SKILL,
   session_44, remediation-plan-v22, worklog, session_45); the v22
   changeset verified in the code first (the inline `maxHeight: "85vh"`
   + `space-y-5` form in `line-item-dialog.tsx`, the parked-pointer
   discipline in `registerFreshAccount`).

2. **Baseline chain fully green on the FIRST run** (the v22 G1 spec fix
   holds deterministically): lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
   build ✓ (robots.txt + sitemap.xml prerendered) · **143/143 e2e** ✓ ·
   **35/35 smoke** ✓.

3. **Code audit** (`skills/code-review-and-audit` native-CLI fallback):
   Phase 1 green (the baseline above); Phase 2: `npm audit` = the same 5
   dev-only ESLint `braces` advisories (no patched release — accepted,
   unchanged); the secret-pattern scan clean (matches only in the
   documented runbook + redacted wrapper placeholder); the v22 changeset
   (`38def33`) diff-reviewed — clean, commented, pinned; scandihaven
   unchanged at `d4789c3` (patterns already reflected).

4. **Audit infrastructure**: the shared parity browser (the
   agent-browser "sessions" `ref25`/`clone25` — see lesson (a) below:
   they resolve to ONE browser tab), both sites logged in (the reference
   with the brief's credentials; the clone with the seeded demo user
   inside one `with-server.sh` invocation), the :3200 parity server
   booted per command.

5. **Mobile navigation (task focus) re-verified end-to-end (17th
   consecutive), all four live**: R1 (the reference's TWO toast
   containers still intercept the burger's center hit at (38,30) —
   `pe:auto`, z-100; the clone's hit is DIRECT on the svg, viewport
   `pe:none`; burger 28×28 at (24,16) both). R2 (the reference's sheet
   still traps after nav — `sheetStillOpen: true`; the clone's sheet
   CLOSES; sheet 288px + Income link (20,185) 247×32 identical both). R3
   (nothing active on `/` on the reference — all five links
   `rgb(63,63,70)`/400, no `<nav>` landmark; the clone highlights
   Dashboard). R4 (the reference overflows 395px on `/`+`/dashboard`,
   464px on `/networth`; the clone fits 390 on ALL six routes). The
   Tailwind v4 pins hold.

6. **Data drift check clean (17th consecutive)** — after one false
   alarm: a drift probe read 62.8%/`$2065` (the CLONE's seed numbers) on
   the "reference" session — the probe had not re-opened the target URL,
   and the shared parity browser was still on the clone's dashboard from
   the previous navigation (**the session's probe lesson (a)**: the
   agent-browser "sessions" resolve to ONE browser tab; the discipline
   is ALWAYS `open <target-url>` + settle before every eval). Three
   re-probes + the per-view census confirm the reference unchanged since
   session 19: allocation 30.5%, income `$5000.00`/1, savings
   `$1000.00`/1, expenses `$525.00`/4, Balance `$3475.00`, guidelines
   30.5/92.3/4.6.

7. **SEO check (the brief's standing ask) PASSES**: the clone serves
   `/robots.txt` (allow-all + the sitemap link) and `/sitemap.xml` (five
   URLs, weekly, priorities 1/0.8) — verified live on :3200 against the
   reference's files (origin-keyed fields correctly differ,
   `NEXT_PUBLIC_SITE_URL`).

8. **The v23 sweep — the session-44 log's two measurable suggestions +
   two fresh mobile surfaces:**
   - **Budget-item dialog MOBILE pair (suggestion 1 — VLM + DOM,
     390×844)**: DOM-identical (panel 358×760 at (16,42), 90vh cap,
     `overflow-y auto`, radius 16, white bg, form gaps 24px). The VLM
     flagged the classification "Need" radio as "thicker border" on the
     clone — DOM-REFUTED (both 16×16, `1px solid rgb(23,23,23)`,
     radius 9999px — the FIFTH consecutive dialog-scale VLM misread);
     the other flag was the platform badge (non-finding).
   - **Mobile sheet KEYBOARD sweep (suggestion 2)**: initial focus → a
     sheet container on both; REAL Tab presses (CDP key events) cycle
     the five links at IDENTICAL positions and WRAP (a focus loop both —
     the reference's sheet traps; the clone's Radix trap matches); the
     focused link's VISIBLE ring is the blue `rgb(59,130,246) 0px 0px
     0px 2px` layer on both (full-string reads; the clone's transparent
     lead layers invisible); Escape closes both. **No findings → G1's
     pin.**
   - **Verify-email state at MOBILE (fresh, 390×844, first time)**:
     DOM-identical (circle 56 + icon 28 `#334155` — the responsive
     mobile scale; 6×40×44 inputs gap 6 radius 8; Verify 294×44
     `#0f172a` radius 12 — the reference's own class is `h-11`; h2
     20px/700). The VLM pair flagged only the dev-code box (the
     documented superset). Two probe lessons surfaced (**(b)** the
     parked-pointer hover artifact now in a PROBE — the clone's bg read
     `#1e293b` until parked; **(c)** one transient first geometry read
     — the reference's button read h=40 once, two re-measures + the
     `h-11` class refute it). **No findings → G2's pin.**
   - **Custom 404 at MOBILE (fresh)**: identical (title, 72px/300 h1,
     quoted path, Go Home 123×38, no overflow).
   - **v22 G2 sub-dialog re-verification**: exact at both viewports
     (desktop 672×680/85vh/20px, mobile 358×717/85vh/20px).
   - The session-44 log's third suggestion (the reference's
     5-attempts-exhausted lockout) remains unmeasurable without burning
     a reference account's attempts — the standing note.

9. **2 finding groups** (`docs/remediation-plan-v23.md`) — the plan
   written, validated against the codebase, then executed TDD-first
   (both groups are TEST-PINS; the app side already matched — the RED
   steps are pin-sanity mutations proving the assertions are
   load-bearing).

10. **TDD (G1 — the sheet keyboard pin)**: the new mobile-navigation
    test passed its Tab-order assertions immediately; the ring read
    caught the fade-in MID-TRANSITION (`rgba(59,130,246,0.647) …
    1.2925px` ≈ 65% through — the documented ring-fade settle lesson,
    now in a spec) → the 350ms settle → GREEN. Pin-sanity: mutated the
    expected order ("Dashboard X") → RED → restored → GREEN.

11. **TDD (G2 — the verify-email mobile pin)**: the new mobile describe
    GREEN on the first run. Pin-sanity: mutated the circle expectation
    56→64 → RED → restore… the restore script's `replace(..., 1)` hit
    the DESKTOP test's original `.toBe(64)` line instead (the same
    assertion pattern exists twice in the file) — an accidental SECOND
    mutation that the desktop pin immediately caught (both tests RED
    with swapped expectations) → both restored via the Edit tool with
    unique context → 6/6 GREEN. Mutation-restore lesson: never blind-
    replace an assertion pattern that exists twice; use unique-context
    edits.

12. **Full chain**: lint ✓ · typecheck ✓ · **108/108 unit** ✓ · build ✓
    · **145/145 e2e** ✓ (143 + 2 new) · **35/35 smoke** ✓.

13. **Screenshots**: all 15 regenerated — byte-identical (deterministic
    captures; no app-code change this session). `.env.example` verified
    matching the codebase.

14. **Docs aligned**: README (counts 145, the v23 plan row), CLAUDE.md
    (counts + the e2e contract's probe-pointer + register-budget +
    ring-fade notes), AGENTS.md (the v23 pin paragraph — the three probe
    lessons), SKILL (state 108/145/35, lesson 41, Appendix B row), the
    probe README (the v23 catalog: eight new files), this log, and the
    worklog.

## Suggested next steps

- A **VLM pair on the register SIGN-UP state at mobile** (the pre-submit
  state — this pass paired the post-submit verify state at mobile; the
  sign-up form's mobile rendering was only e2e-pinned, never visually
  paired).
- A **keyboard sweep of the sheet's ARROW-key semantics** (this pass
  swept Tab + Escape; the sheet's nav list is a plain list on both
  sites, but Arrow-key behavior inside the open sheet was never
  compared).
- The **5-attempts-exhausted lockout path** remains the standing
  unmeasurable (would burn a reference account's attempts).
