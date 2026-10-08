# Session 24 — Fresh verification & parity iteration v12

> Continuation note: `docs/session_23.md` holds the incoming session-21
> conversation summary (the record this session was briefed to review),
> so this work session's formal log lives here. Work-session numbering
> continues the odd convention: 15 → 17 → 19 → 21 → **23** (this
> session), iteration v11 → **v12**.

Date: 2026-10-08 · Baseline: `740d6e1` (v11 code `00dad5a`, all green) ·
Plan: `docs/remediation-plan-v12.md` · Outcome: **4 finding groups fixed
TDD-first; 96 unit · 112 e2e · 30 smoke all green; live parity
re-verified side by side.**

## What happened

1. **Workspace + doc chain.** `git pull` fast-forwarded to `740d6e1`
   (`docs/session_23.md` + a `prompt-to-review-3.md` touch). Full doc
   chain re-read (AGENTS, CLAUDE, README, PAD, SKILL, session_22/23,
   remediation-plan-v11, worklog) and the uploaded coding-agent
   operating instructions internalized. Environment intact (`.env`
   `DATABASE_URL="file:../db/custom.db"`, `db/custom.db` at the repo
   root, `.env.example` matching, node_modules present).

2. **Baseline chain at `740d6e1` fully green**: lint ✓ · typecheck ✓ ·
   96/96 unit ✓ · build ✓ · 107/107 e2e ✓ · 30/30 smoke ✓. The v11 pins
   spot-checked in the code first (`.zb-btn-add` focus-visible rules,
   `text-xl` empty-state headings, 16px Add icons). Scandihaven cloned
   and its AGENTS/SKILL reviewed for tech-stack patterns (the relevant
   ones — Tailwind v4 CSS-first rules, integer-minor-unit money, strict
   TS, test gates — already reflected in this repo's ADRs).

3. **Audit infrastructure.** Four agent-browser sessions
   (`ref12`/`clone12` desktop 1280×800, `ref12m`/`clone12m` 390×844),
   both sites logged in; the parity server on :3200 per command via
   `with-server.sh` (the sandbox still reaps background processes).
   The clone login flow must run inside ONE `with-server.sh` invocation
   (splitting it across invocations reaps the server between the fill
   and the submit → "Network error").

4. **Data drift check**: reference UNCHANGED since session 19
   (allocation 30.5%, income `$5000.00`/1 item, savings `$1000.00`,
   expenses `$525.00` with the documented `$0.00` "Miscellaneous"
   residual); clone seed arithmetic intact (`+$2065.00`, 62.8%).

5. **Mobile navigation (task focus) re-verified end-to-end**: R1
   re-confirmed live — the ref's toast container (390×32, `pe:auto`,
   z-100, top-0) still intercepts its burger's center hit; the clone's
   hit is DIRECT on the svg. R2 re-confirmed — tapping Income in the
   ref's sheet navigated to `/income` with `sheetStillOpen: true` AND
   `overlayStillUp: true` (the trap), its Income link rendering the
   full active style (v10 finding); the clone's sheet CLOSED on nav
   and fits 390px. R4 re-confirmed — ref scrollWidth 395 at 390, clone
   390. Burger/topbar geometry identical (28×28 at (24,16)).
   NEW observation: the ref's mobile SHEET closes on Escape (unlike
   its dialogs — R5); the clone's Radix sheet matches.

6. **Fresh angles swept (first-ever measurements)**: the login ERROR
   state (wrong password on both sites — found the banner), the
   per-route document.title set (all 7 routes), the login root
   landmark, the forgot-password confirmation state (submit flow), the
   expenses payment-method filter card + its listbox OPEN state
   (identical — the option count differs only by data), and an a11y
   structure sweep (h1s, `lang`, landmarks, button names — identical
   except the login `<main>`; the clone's `aside` rail is a superset
   over the ref's div rail).

7. **Four finding groups** (`docs/remediation-plan-v12.md`):
   - **G1**: the login error renders as bare red text (`#dc2626`
     14px/500 `p`) while the reference renders a red-tinted bordered
     banner — bg `rgba(254,242,242,0.7)`, border `1px solid
     rgb(254,202,202)`, radius 12, padding 16, centered `#b91c1c`
     14px/400 inner text (the shadcn FormMessage pattern; 368×54
     desktop, 294×54 mobile, 16/20px space-y gaps). The same slot
     serves sign-in 401s and the sign-up "Passwords do not match".
   - **G2**: per-route tab titles — the reference's SPA sets "Income |
     ZeroBudget" etc. (one-word "Networth"); the clone rendered
     "ZeroBudget" everywhere.
   - **G3**: the login page root is a `<main>` landmark on the
     reference; the clone rendered a div with identical styles.
   - **G4**: the forgot-password submit transitions the reference's
     card to a "Check your email" confirmation state; the clone kept
     the form + an honesty toast.

8. **TDD RED**: 5 new/extended tests (login-parity: banner chrome +
   main landmark + forgot state; nav-geometry: route titles ×2; auth:
   the wrong-password banner extension) — RED confirmed at the exact
   unfixed values (one test-bug fixed: `getByLabel("Password")`
   substring-matches "Confirm Password" in the sign-up state — needs
   `exact: true`).

9. **GREEN — with one root-cause detour (lesson 27)**: the G2 fix was
   first implemented as a `usePathname()`-driven `document.title`
   effect in the AppShell. It RAN (in-page 20ms poller: title set at
   260ms) and was silently RESET at 284ms — React Float re-emits the
   static `<title>` from the RSC flight payload during hydration
   recovery. Reverted to the framework-native mechanism: route-segment
   `layout.tsx` metadata (`Income`/`Expenses`/`Savings`/`Networth`) +
   the root layout's `"%s | ZeroBudget"` pipe template — the titles
   ship in the prerendered HTML and the re-emission is idempotent.
   G1/G3/G4 landed as planned (inline-style pins per the
   parity-surface pattern).

10. **Full chain**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ ·
    **112/112 e2e** ✓ · 30/30 smoke ✓.

11. **Live parity re-verification on fresh sessions**
    (`ref13`/`clone13`/`ref13m`): the error banner byte-identical both
    sides (desktop 368×54 full chrome + inner text styles; mobile
    294×54 with 16px space-y gaps and no overflow); the route titles
    identical on all 7 routes; the `<main>` landmark with identical
    computed styles (flex/min-h-screen/center/p-4, h1 inside); the
    forgot state typography identical (H2 24px/700 `#0f172a`, desc
    16px `#475569` lh 24, back 14px/500 `#64748b`, form replaced) with
    the honest copy. The agent-browser daemon hit memory pressure
    mid-verification (CDP `Connection refused`) — recovered by closing
    sessions one at a time with timeout wrappers.

12. **Screenshots**: the catalog extended 13 → 15 shots —
    `14-login-error.png` (the banner) and `15-forgot-reset.png` (the
    confirmation state) added to `capture-screenshots.mjs` (one failed
    login attempt, within the rate-limit budget); all 15 regenerated.

13. **Docs aligned**: README (counts 112, the plan-v12 row, 15-shot
    set), CLAUDE.md (counts, the title-effect trap note), AGENTS.md
    (the v12 pin paragraph), SKILL (state 96/112/30, lessons 27–28,
    Appendix B row), the probe README v12 rows, this log, and the
    worklogs.
