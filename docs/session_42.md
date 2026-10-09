# Session 42 — Fresh verification & parity iteration v21

> Continuation note: `docs/session_41.md` holds the incoming session-39
> conversation summary (the record this session was briefed to review),
> so this work session's formal log lives here. Work-session numbering
> continues the odd convention: 15 → 17 → 19 → 21 → 23 → 25 → 27 → 29 →
> 31 → 33 → 35 → 37 → 39 → 41 (this session), iteration v20 → **v21**.

Date: 2026-10-09 · Baseline: `dc09bf5` (v20 code `1bb1358`, all green) ·
Plan: `docs/remediation-plan-v21.md` · Outcome: **3 finding groups fixed
TDD-first — (G1) the sitemap.xml + robots.txt the reference serves,
added via Next.js MetadataRoute routes; (G2) the calculator line-item
row actions re-measured HOVER-REVEALED on the live reference (its chrome
changed since the v6 pin) and matched with a new group-hover variant
pin; (G3) the register flow's EMAIL-VERIFICATION GATE (the reference's
measured post-success landing) rebuilt as the honest superset — the full
"Verify your email" state + `/api/auth/verify-email` +
`/api/auth/resend` + the register re-issue path + the 403
unverified-login rejection + the honest no-mail code delivery; 6 new
e2e tests + 12 new unit tests + 5 new smoke steps; 108 unit · 142 e2e ·
35 smoke all green; live parity re-verified (the VLM pair on the verify
state: IDENTICAL).**

## What happened

1. **Workspace refresh**: `git pull` to `dc09bf5` (brought in
   `docs/session_41.md` — the incoming session-39 conversation
   summary). The environment survived the session boundary (`.env` with
   `DATABASE_URL="file:../db/custom.db"`, `db/` at the repo root with
   the seeded demo workspace, node_modules — all re-verified). Full doc
   chain re-read (AGENTS, CLAUDE, README, PAD, SKILL, session_40,
   remediation-plan-v20, worklog, session_41); the pulled v20 changeset
   verified in the code first (the G1 `items-start`+`mb-8` row class +
   the G2 `CLASSIFICATION_ICONS` map). The scandihaven pattern repo
   re-checked — current at `d4789c3` (its patterns already reflected).

2. **Baseline chain at `dc09bf5` fully green, first full run, no
   flakes**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ · 137/137 e2e
   ✓ · 30/30 smoke ✓.

3. **Code audit** (`skills/code-review-and-audit` native-CLI fallback):
   Phase 1/4 green; Phase 2: `npm audit` = the same 5 dev-only ESLint
   `braces` advisories (no patched release — accepted, unchanged); the
   secret-pattern scan clean (the SSH wrapper's `[REDACTED:...]`
   placeholder + the runbook's marker-only validation command; no key
   material anywhere).

4. **Audit infrastructure**: agent-browser sessions `ref23`/`clone23`
   (desktop 1280×800, resized per check), both sites logged in (the
   reference with the brief's credentials; the clone with the seeded
   demo user through one `with-server.sh` invocation), the :3200 parity
   server booted per command.

5. **Mobile navigation (task focus) re-verified end-to-end, all four
   live**: R1 (the reference's TWO toast containers still intercept the
   burger's center hit at (38,30) — pe `auto`, z-100; the clone's hit is
   DIRECT on the svg, viewport `pe:none`; burger 28×28 at (24,16) both).
   R2 (the reference's sheet still traps after nav —
   `sheetStillOpen: true` + overlay; the clone's sheet CLOSES; sheet
   288px + Income link (20,185) 247×32 identical both). R3 (nothing
   active on `/` on the reference — all five links `rgb(63,63,70)`/400,
   no `<nav>` landmark; the clone highlights Dashboard — white + 500 +
   the landmark). R4 (the reference overflows 395px on `/` +
   `/dashboard`, 464px on `/networth`; the clone fits 390 on ALL six
   routes). The Tailwind v4 pins hold — the clone's mobile menu works
   as expected.

6. **Data drift check clean (fifteenth consecutive)**: reference
   unchanged since session 19 (allocation 30.5%, income `$5000.00`/1
   item, savings `$1000.00`/1, expenses `$525.00`/4 items, Balance
   `$3475.00`).

7. **The v21 sweep — the session-40 log's three suggested surfaces +
   the two remaining auth flows**:
   - **Calculator populated pair (VLM)**: the "• Will update category
     total" flag refuted as data-driven (the reference's Rent parent
     `$25.00` equals its line-item sum — both conditionals match); the
     row-actions flag DOM-verified as a REAL reference chrome change
     (**G2**): the live reference renders `opacity-0
     group-hover:opacity-100` on the action container at rest (the
     v6-era pin measured always-visible; the 32×32 buttons, 16×16
     icons, and near-black/red colors held).
   - **Mobile sheet-open pair (VLM, both sites at `/`)**: both flags
     refuted — the active-item difference is the documented superset
     fix #3, the avatar letter is data. Chrome parity holds (this
     state's first visual diff — its geometry was long-pinned).
   - **Net-worth populated Edit-Asset pair (VLM)**: the X-close claim
     DOM-refuted for the THIRD consecutive pass (identical 36×36,
     0px border, transparent bg, 16px svg, `#0a0a0a`, radius 6 both).
   - **Register post-success landing (measured live, first time — the
     session-38/40 flagged surface)**: **G3** — the reference gates
     registration behind a "Verify your email" state (full chrome
     measured: the 64px slate-100 shield-check circle, the 6×40×44
     numeric inputs, the 44px #0f172a Verify button, the wrong-code
     countdown "Invalid verification code. 4 attempts remaining." at
     14px #b91c1c, the resend semantics with a fresh code + attempts
     reset, the re-register-re-issues path, and the unverified sign-in
     rejection "Please verify your email before logging in. Check your
     email for the verification code.").
   - **Keyboard spot sweep (login surface)**: Tab order identical
     (Google → Email → Password → Sign in → Forgot → Sign up); the
     Google button shows the UA-default outline on BOTH; the inputs'
     v13-pinned two-layer focus ring holds once the 350ms transition
     settle + the FULL shadow-string read are applied (the v11
     truncation lesson recurred in this pass's first probe).
   - **The SEO check (the brief's new standing ask)**: the reference
     serves `/robots.txt` (allow-all + sitemap link) and
     `/sitemap.xml` (five URLs — origin at 1.0, four app routes at 0.8,
     weekly, `/login` excluded); the clone 404'd both — **G1**.

8. **3 finding groups** (`docs/remediation-plan-v21.md`) — the plan
   written, validated against the codebase, then executed TDD-first.

9. **TDD RED → GREEN (G1 — the SEO pair)**: the sitemap/robots e2e test
   in `not-found.spec.ts` RED at the 404s → `src/app/robots.ts` +
   `src/app/sitemap.ts` (the MetadataRoute conventions, keyed off
   `NEXT_PUBLIC_SITE_URL`) GREEN. Next's generator canonicalizations
   documented as protocol-equivalent in the spec (`User-Agent` casing
   per RFC 9309 — robots directives are case-insensitive; priority `1`
   vs `1.0`; `<lastmod>` omitted by design — the reference's file shape).

10. **TDD RED → GREEN (G2 — the hover-revealed row actions)**: the
    calculator spec's G9/G10 block flipped to the new contract (RED at
    the always-visible clone: containerOpacity "1") → the action
    container gained the reference's exact classes + `globals.css`
    gained `@variant group-hover (.group:hover &)` (v4 media-gates the
    group family like plain hover — the pin keeps the reveal alive on
    `hover:none` devices; load-bearing) → GREEN (opacity 0 at rest, 1
    under a real row hover, geometry + colors unchanged).

11. **TDD RED → GREEN (G3 — the verification gate)**: the pure seam
    `src/lib/verification.ts` first with 9 unit tests (code format,
    match, the 5-attempt countdown, the reference's exact messages);
    the zod schemas (+3 unit tests); the API rework (register: re-issue
    for unverified/409 for verified/no session + the honest
    `devCode` delivery; `/api/auth/verify-email`: attempt check +
    verify + session; `/api/auth/resend`: fresh code + reset; login:
    the 403 unverified rejection); the store actions
    (`verifyEmail`/`resendCode`, register returning the verify
    payload); the login card's fourth mode (the CodeInputs component
    with the measured 40×44/radius-8/inputmode-numeric chrome + the
    full verify panel); the schema push (three additive User columns);
    the seeded demo user PRE-VERIFIED (the update branch also upgrades
    existing demo DBs); the `verify-email.spec.ts` (4 tests: state
    chrome + geometry, the countdown + correct-code dashboard landing,
    the unverified-login banner, resend) — RED at the missing state →
    GREEN. The smoke test extended with 5 steps (register issues the
    gate, 403 unverified, 400 wrong code, 200 verify + the authed
    post-verify session).

12. **Full chain**: lint ✓ · typecheck ✓ · **108/108 unit** ✓ · build ✓
    · **142/142 e2e** ✓ (137 + 1 sitemap + 4 verify-email, first full
    run, no flakes) · **35/35 smoke** ✓.

13. **Live parity re-verification**: G1 (both files served with the
    reference's structure); G2 (the clone's container class byte-identical,
    opacity 0 at rest → 1 under a real hover, 32px/16px/colors exact);
    G3 (the full live flow — register → verify state → the dev-code box
    → the correct code → the `/` dashboard landing — plus the VLM pair
    on the state: **IDENTICAL**). The live-audit lesson encoded in the
    probe: a malformed throwaway email (`a@b@c.com`) fails native
    `type=email` validation SILENTLY — check `form.checkValidity()`
    before suspecting React state.

14. **Screenshots**: all 15 regenerated — the calculator shot changed
    (the G2 hover-reveal — the only meaningful delta; the row actions
    now render hidden at rest exactly like the reference); the
    add-item-modal shot's 0.0% pixel delta is animation-frame noise.

15. **Docs aligned**: README (counts 108/142/35, the four-state auth
    card, the v21 plan row, the env-var row's sitemap/robots mention),
    CLAUDE.md (counts, the API surface + register envelope + the v21
    e2e additions, the group-hover variant pin, the register
    rate-limit budget note), AGENTS.md (the v21 pin paragraph + the
    live-audit lesson), SKILL (state 108/142/35, lesson 39 — the
    reference-site drift + the silent-native-validation lessons,
    Appendix B row), the probe README (v21 catalog: the wrapper, the
    verify-flow probe), this log, and the worklog.

## Suggested next steps

- The **correct-code landing** on the reference is still unmeasurable
  (no access to its email inbox) — if the platform ever exposes the
  code, measure the post-verify landing (the clone assumes `/`).
- The **VLM sweep of the seeded demo's line-item-populated calculator**
  at MOBILE viewport (this pass compared it at desktop only) and the
  **line-item EDIT sub-dialog** (the nested dialog's populated state).
- A **keyboard-navigation sweep beyond the login surface** (the app
  views' Tab order + focus visibility — the Radix-trap superset class
  has never been systematically swept on the item views).
- The **"5 attempts exhausted" path** (the reference's lockout state —
  unmeasurable without burning a reference account's 5 attempts; the
  clone implements the documented re-send requirement).
