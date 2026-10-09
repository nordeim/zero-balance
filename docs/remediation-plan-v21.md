# Remediation Plan v21 — Session-41 Parity Iteration

Date: 2026-10-09 · Scope: fresh two-site re-audit after the v20 baseline
(`dc09bf5` / v20 code `1bb1358`, all green — pulled clean, the environment
survived the session boundary: `.env`/`db/`/node_modules intact, all standing
brief requirements re-verified). Baseline chain at `dc09bf5` fully green
BEFORE any work: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ · 137/137 e2e
✓ (first full run, no flakes) · 30/30 smoke ✓. Probes: one-shot
`agent-browser eval` scripts (sessions `ref23`/`clone23`, desktop 1280×800 +
390×844 resized per check), the standalone parity server on :3200 booted per
command through `scripts/with-server.sh`, and the VLM visual sweep
(`z-ai vision` pairs, the v19/v20 methodology — every flag DOM-verified
before it becomes a finding).

## The sweep — method and results

The pass swept the session-40 log's three suggested surface classes — the
CALCULATOR's populated state (one live line item + the row chrome), the MOBILE
SHEET's open state, and the net-worth populated EDIT dialog — plus the two
remaining unmeasured AUTH flows (the register post-success landing, measured
end-to-end for the first time with a throwaway account on the reference:
the verify-email gate, its wrong-code countdown, its unverified sign-in
rejection, and its re-register/resend semantics), a keyboard-navigation spot
sweep (Tab order + focus chrome on the login surface), the standing
task-focus re-verification (mobile navigation R1–R4 + reference data-drift
check), and the code audit (`skills/code-review-and-audit` native-CLI
fallback: lint/tsc/tests green; `npm audit` = the same 5 dev-only ESLint
`braces` advisories, no patched release — accepted, unchanged;
secret-pattern scan clean — the SSH wrapper's key field is the documented
`[REDACTED:ssh_private_key]` placeholder; scandihaven current at `d4789c3`).

- **Mobile navigation (task focus) R1–R4 re-confirmed, all four live:** R1
  (the reference's TWO `fixed top-0 z-[100]` toast containers still intercept
  the burger's center hit at (38,30); the clone's hit is DIRECT on the svg;
  burger 28×28 at (24,16) both; the clone's viewport `pe:none`), R2 (the
  reference's sheet still traps after nav — `sheetStillOpen: true` + overlay;
  the clone's closes; sheet 288px + Income link (20,185) 247×32 identical),
  R3 (nothing active on `/` on the reference — all five rail links
  `rgb(63,63,70)`/400, no `<nav>` landmark; the clone highlights Dashboard),
  R4 (the reference overflows 395px on `/`+`/dashboard`, 464px on `/networth`;
  the clone fits 390 on all six routes). The Tailwind v4 pins hold.
- **Data drift clean (fifteenth consecutive check)**: reference unchanged
  since session 19 (allocation 30.5%, income `$5000.00`/1, savings
  `$1000.00`/1, expenses `$525.00`/4, Balance `$3475.00`).
- **Calculator populated pair (VLM)**: TWO flags — one refuted as
  data-driven (the "• Will update category total" hint: the reference's Rent
  parent `$25.00` EQUALS its line-item sum so its identical conditional
  hides the hint; the clone's seeded Rent `$1850` did not — the conditionals
  match, the parent amounts differ) and ONE REAL DRIFT (**G2** below).
- **Mobile sheet-open pair (VLM, both sites at `/`)**: both flags refuted —
  the active-item difference is the documented superset fix #3 (the clone
  highlights Dashboard on the root route; the reference marks nothing), and
  the avatar letter is data. Chrome parity holds (geometry long-pinned, now
  visually diffed for the first time).
- **Net-worth populated Edit-Asset pair (VLM)**: ONE flag — the X-close
  "boxed" claim, DOM-refuted for the THIRD consecutive pass (identical
  36×36, 0px border, transparent bg, 16px svg, `#0a0a0a`, radius 6 both
  sides — the VLM persistently misreads this chrome at dialog scale).
- **Register post-success landing (measured live, first time)**: **REAL
  FUNCTIONAL GAP (G3)** — the reference gates registration behind an
  email-verification step the clone does not have (details below).
- **Keyboard spot sweep (login surface)**: Tab order identical (Google →
  Email → Password → Sign in → Forgot → Sign up); the Google button shows
  the UA-default outline on BOTH sites; the email/password inputs render
  the v13-pinned two-layer focus ring on the clone once the 350ms
  transition settle and the FULL shadow-string read are applied (the v11
  truncation lesson recurred in this pass's first probe — the visible ring
  layers trail v4's transparent lead layers). No drift.

### G1. [MED] SEO: the sitemap.xml + robots.txt the reference serves are missing

The reference serves BOTH files (measured live): `/robots.txt` →
`User-agent: * / Allow: / / Sitemap: <origin>/sitemap.xml`, and
`/sitemap.xml` → five URLs — `/` at priority 1.0 and its four app routes at
0.8, all `changefreq weekly` (its own capitalized paths; `/login` is
excluded). The clone 404s both (`/robots.txt` and `/sitemap.xml` measured on
the :3200 parity server) — and its own `.env.example` already documents
`NEXT_PUBLIC_SITE_URL` as "Canonical public origin — used for metadata,
sitemap.xml, and robots.txt" while nothing generates them. The brief
explicitly asks for the sitemap/SEO check.

**Fix (Next.js MetadataRoute conventions, the standard zero-config way):**
- `src/app/robots.ts` — `MetadataRoute.Robots`: allow-all + the sitemap link
  keyed off `NEXT_PUBLIC_SITE_URL` (the same `siteUrl` resolution the root
  layout's metadataBase uses).
- `src/app/sitemap.ts` — `MetadataRoute.Sitemap`: the clone's five routes
  (`/`, `/income`, `/savings`, `/expenses`, `/networth`) with the reference's
  priorities (1.0 / 0.8) and `weekly` changefreq. `/login` excluded exactly
  like the reference; authed-only budget data never listed.
- **Pinned by** a new e2e test (head-metadata describe in
  `not-found.spec.ts`, the v7-G8 home): fetch both routes from the running
  production server, assert the robots body (allow-all + sitemap link) and
  the sitemap's URL set + priorities + changefreq.

### G2. [MED] Calculator line-item row actions: the reference hover-reveals them now

Measured at rest on the live reference (pointer parked far from the row):
the row-action container renders `flex items-center gap-1 opacity-0
group-hover:opacity-100 transition-opacity` — the edit/delete buttons are
HIDDEN until the row is hovered. The buttons themselves still measure
32×32 with 16×16 icons (the button's `[&_svg]:size-4` overrides the icon's
own `w-3.5 h-3.5` class), edit near-black `rgb(10,10,10)`, delete red
`rgb(220,38,38)` — the v6 G10 geometry/colors hold; only the VISIBILITY
changed. The clone renders the actions always-visible — the v6 G9 pin
(session 11) measured the reference at `opacity: 1` at rest back then, and
the v17 re-check measured only the geometry (which is opacity-independent).
The reference's chrome has since changed (the same class as v19's
recurring-row drift): the current at-rest computed style is ground truth.

**Fix:**
- `calculator-dialog.tsx`: the action container gains the reference's exact
  classes (`opacity-0 group-hover:opacity-100 transition-opacity`).
- `src/app/globals.css`: add `@variant group-hover (.group:hover &);` beside
  the existing `@variant hover (&:hover)` — v4 media-gates `group-hover:`
  behind `@media (hover: hover)` exactly like plain `hover:` (trap 1); the
  pin restores the reference's v3 semantics so the buttons stay revealable
  on `hover: none` devices (tap-to-reveal, the reference's own behavior).
- **Spec update (TDD RED first)**: `calculator.spec.ts`'s G9/G10 test —
  assert opacity "0" at rest (pointer parked), opacity "1" after a real
  `.hover()` on the row, and keep the 32×32 + 16px + color pins.

### G3. [HIGH] Register flow: the reference's email-verification gate (measured live)

The reference's register post-success landing — measured end-to-end with a
throwaway account (the session-38/40 log's flagged unmeasured auth flow):

1. `Create account` → the card swaps to a centered **"Verify your email"**
   state on `/login`: a "Back to sign in" link (14px/500 `#64748b`,
   centered, arrow-left — the v12 forgot-confirmation family), h2 "Verify
   your email" (24px/700 `#0f172a`, centered), "We've sent a 6-digit code
   to {email}" (16px `#475569`, centered), SIX code inputs (each 40×44,
   radius 8, `inputmode="numeric"`, centered text, in a
   `flex items-center justify-center gap-1.5` row), "Enter the
   verification code sent to your email", a "Verify email" button (44px
   tall, full card width, `#0f172a` bg, white text, radius 12, weight 500),
   and "Didn't receive the code? Resend" (14px `#64748b` family).
2. Wrong code → centered red text "Invalid verification code. 4 attempts
   remaining." (14px/400 `#b91c1c`) — a 5-attempt countdown.
3. `Resend` → a transient "New verification code sent to your email"
   message (toast-family div, 16px `#09090b`) + a fresh code + attempts
   reset.
4. Re-registering with an existing UNVERIFIED email returns the verify
   state again (no 409 — the re-send semantics).
5. Signing in with an UNVERIFIED account is rejected: the sign-in card +
   error banner "Please verify your email before logging in. Check your
   email for the verification code."
6. (The correct-code landing is unmeasurable without the reference's
   inbox — the clone lands on `/` per its login behavior.)

The clone auto-logins immediately after `Create account` and lands on the
dashboard — the verification state does not exist. This is the largest
measured functional gap of the session.

**Fix — the honest superset (the v12 forgot-password precedent: match the
state, be honest about the mail transport):**
- **Schema** (`prisma/schema.prisma`): User += `emailVerifiedAt DateTime?`,
  `verificationCode String?`, `codeAttempts Int @default(0)`. Nullable/
  defaulted columns — no data loss on `db:push`.
- **New pure seam** (`src/lib/verification.ts`): `generateCode()` (crypto
  6-digit), `codeMatches()`, `remainingAttempts()` (5 max, the reference's
  countdown), attempt/lock semantics — unit-testable without a DB.
- **API**:
  - `POST /api/auth/register` — existing user + UNVERIFIED → re-issue a
    code (the reference's semantics #4; no 409) and return the verify
    payload; new user → create (unverified) + code. The response carries
    `{ email, devCode }` — the HONEST no-mail delivery: a self-hosted
    instance has no SMTP; the code rides the response and the UI shows it
    in the verify state with explicit "no mail transport" copy (the
    forgot-password precedent class). No session cookie is set by register
    anymore (the gate).
  - `POST /api/auth/verify-email` (NEW) — `{ email, code }`: attempt check
    (max 5, then require resend), on match set `emailVerifiedAt`, clear the
    code, set the session cookie (auto-login — the natural post-verify
    landing, `/`). On mismatch decrement and return "Invalid verification
    code. {N} attempts remaining." with 400.
  - `POST /api/auth/resend` (NEW) — `{ email }`: only for existing
    unverified users; fresh code + attempts reset; rate-limited by the
    same `register:<ip>` limiter bucket.
  - `POST /api/auth/login` — unverified user → 403 "Please verify your
    email before logging in. Check your email for the verification code."
    (the reference's exact banner text; the v12 banner renders it).
  - zod schemas (`verifyEmailSchema`, `resendSchema`) in `validation.ts`.
- **Login card** (`login-card.tsx`): a fourth mode `verify` — the
  reference's chrome above (the confirmation-state family classes already
  exist from v12: h2 24px/700 `#0f172a`, 16px `#475569`, 14px/500
  `#64748b` back link; the code inputs 40×44 rounded-lg gap-1.5
  `inputmode="numeric"`; the 44px `#0f172a` Verify button; the error line
  14px `#b91c1c` centered). The honest delivery note renders the code with
  copy like "No mail transport is configured on this self-hosted instance —
  your verification code is 123456" (muted 14px, below the email line).
  "Back to sign in" returns to the sign-in state; "Resend" calls the resend
  API and shows the transient "New verification code sent to your email"
  line.
- **Store** (`store.ts`): `register` becomes the verify-payload call (no
  session); new `verifyEmail(email, code)` (session + refresh) and
  `resendCode(email)` actions.
- **Seed** (`prisma/seed.ts`): the demo user created with `emailVerifiedAt`
  set (the demo login keeps working — the e2e `auth.setup` and every
  login-dependent spec are unaffected).
- **Unit tests**: `tests/verification.test.ts` (code format/length,
  match, countdown, lock-after-5) + the new zod schemas in
  `tests/validation.test.ts`.
- **E2E** (`tests/e2e/verify-email.spec.ts`): the state chrome + the 6-input
  geometry; wrong code → the countdown text; the correct code (read from
  the honest display) → verified + lands on `/` with the dashboard; the
  unverified sign-in banner; resend re-issues; the demo user still logs in
  directly. Registered-then-verified fixtures are throwaway emails (unique
  per run) — the register rate-limit budget stays under the 10/IP/15min
  cap (≤3 register-class calls per run).
- **Register response shape note**: `register` no longer sets a session or
  returns `{ user }` — the login card's submit handler drives the flow; no
  other consumer exists (grepped).

## Validation of this plan against the codebase

- G1: no `sitemap.ts`/`robots.ts` exists under `src/app/` (both 404 on the
  parity server); the root `layout.tsx` already resolves `siteUrl` the same
  way; the `.env.example` documents the intent. Route set matches
  `src/app/*/page.tsx` (dashboard renders at `/`).
- G2: `calculator-dialog.tsx:216-240` holds the always-visible action
  container (the v6 comment block marks it); `globals.css:8` holds the lone
  `@variant hover` pin (no group-hover pin); `calculator.spec.ts:228-265`
  pins the OLD opacity-1 behavior (the spec must flip RED first).
- G3: `schema.prisma` User model verified (additive columns safe);
  `api/auth/{register,login}/route.ts` read (the session-cookie set in
  register moves to verify-email); `validation.ts` auth schemas located;
  `login-card.tsx` mode machine + INPUT_CLS + the v12 confirmation-state
  classes located; `store.ts` register/login actions located; seed's
  upsert path verified (set `emailVerifiedAt` in the create + update);
  e2e register specs grep-verified error-path-only (the duplicate-email
  409 fires BEFORE any write — unaffected; the client-side mismatch test
  never calls the API). The smoke test only exercises the demo login +
  wrong-password + rate-limit — unaffected; the demo user stays verified.

## Execution order (TDD)

1. **G1** — write the sitemap/robots e2e test (RED: 404s today) → add
   `robots.ts` + `sitemap.ts` (GREEN) → re-run the spec file.
2. **G2** — flip the calculator spec's G9 assertions to the hover-reveal
   contract (RED at always-visible) → the container class + the
   group-hover variant pin (GREEN) → re-run.
3. **G3** — the schema push + `verification.ts` with its unit tests first
   (pure seam, RED→GREEN) → the API routes (+ zod schemas + unit tests) →
   the store actions + login-card verify mode → `verify-email.spec.ts`
   (RED at the missing state → GREEN) → the seed's verified demo user.
4. Full clean-check chain: `npm run lint && npm run typecheck && npm test
   && npm run build && npm run test:e2e` + `bash scripts/smoke-test.sh`.
5. Live parity re-verification of all three groups on :3200 vs the
   reference; regenerate the docs screenshots; align README/CLAUDE/AGENTS/
   SKILL/probe-README/session log/worklog.

## Risk notes

- G2's hover-gate must not strand touch users: the `@variant group-hover`
  pin is load-bearing (v4's default would hide the actions permanently on
  `hover: none` devices — worse than either site's behavior).
- G3's register no longer auto-logins — every existing spec that logs in
  does so with the (now pre-verified) demo user; the register 409 spec
  never reaches the write. The e2e rate-limit budget: verify-email spec
  adds ≤3 register-class calls (register + resend + one re-register) —
  inside the 10/IP/15min limiter with the rest of the suite's single
  login.
- The devCode-in-response is a documented self-hosted fallback (SMTP is
  out of scope); the copy says so explicitly. With SMTP configured in a
  future deployment the field would be dropped — noted in the route.
