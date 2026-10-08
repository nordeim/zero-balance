# Remediation Plan v13 — Session-25 Parity Iteration

Date: 2026-10-08 · Scope: fresh two-site re-audit after the v12 baseline
(`5957b2a` / code `4ba60f5`) re-verified green (lint · typecheck · 96/96
unit · build · 112/112 e2e · 30/30 smoke). Probes: one-shot
`agent-browser eval` scripts, sessions `ref14`/`clone14` desktop
1280×800 + `ref14m`/`clone14m` 390×844, the standalone parity server on
:3200 booted per command through `with-server.sh` (the sandbox still
reaps background processes; the agent-browser daemon persists — one
zombie `ref13` session lingered from the prior session and was worked
around, not fatal).

This pass swept state dimensions no earlier pass had measured: the
**register-flow API error** (duplicate email — a read-only probe on the
reference: submitting the existing account's email creates nothing and
returns the 409 text), the **sign-up-mode password placeholders**, the
**login inputs' FOCUS ring** (computed styles under `.focus()` — never
measured; v10 measured the DIALOG inputs' `:focus-visible` ring only),
the **authenticated-user visit to `/login`** (both render the card — no
redirect on either side), the **"Continue with Google" click behavior**
(the reference opens a real Google OAuth flow through the Base44
platform; the clone's honest-unavailable toast is the documented
self-hosted divergence), the **item-card date format** ("Oct 7, 2026" —
identical), the **hero progress-bar chrome** (track 568×12
`rgba(255,255,255,0.1)` 9999px + 90deg orange gradient fill — identical;
fill widths differ by data), the **"OR" divider** (both render the
DOM-lowercase "or" span with `text-transform: uppercase`, 12px/500
`#64748b` ls 0.6px — identical), a **cursor sweep** (pointer/text,
identical), and a code-audit pass on the v12 changes (lint/typecheck/
tests green; `npm audit` = 5 high, ALL in the dev-only ESLint
`braces` glob chain with **no patched release existing** — accepted,
documented; secret-pattern scan clean — the only "BEGIN OPENSSH PRIVATE
KEY" matches are the wrapper's own `OPENSSH_BEGIN` constant and the
runbook's troubleshooting snippet, the documented display artifact).

The mobile-navigation stack (the task focus) was re-verified
end-to-end first, and the reference data-drift check ran clean. The
audit found **3 clone-side finding groups**; no new reference bugs
(R1/R2/R4 all re-confirmed live; reference data unchanged since session
19: allocation 30.5%, expenses `$525.00` with the documented `$0.00`
"Miscellaneous" residual).

---

## Findings ledger

### G1. [LOW] Register duplicate-email error text drifts from the reference

Measured live on the reference (sign-up state, email =
`sepnetflix2023@outlook.com` + matching ≥8-char passwords → 409): the
error banner renders **"A user with this email already exists"** — the
same v12-pinned banner chrome (bg `rgba(254,242,242,0.7)`, border
`1px solid rgb(254,202,202)`, radius 12, padding 16, 368×54, inner
`#b91c1c` 14px/400 lh 20 centered — byte-identical both sides).

The clone's register route returns **"An account with this email
already exists"** (`src/app/api/auth/register/route.ts:19`, 409) — a
one-word-class text drift in a user-visible surface. Not an
honesty-class divergence (no lying involved) → parity-first: match the
reference text exactly. The login 401 text ("Invalid email or
password") already matches both sides (re-verified live this pass).

Fix: change the fail() string in the register route. No test pins the
current text (grepped tests/ + scripts/).

Fix files: `src/app/api/auth/register/route.ts`.

### G2. [LOW] Sign-up-mode password placeholders differ

Measured live on the reference's sign-up state: the password field's
placeholder is **"Min. 8 characters"** and the confirm field's is
**"Re-enter password"** (the shadcn hint pattern; sign-IN mode keeps
`••••••••` — re-verified). The clone renders `••••••••` for all
password fields in every mode (`login-card.tsx` hardcodes both).

Fix: per-mode placeholders — password: `"Min. 8 characters"` in
sign-up mode (else `••••••••`); confirm: `"Re-enter password"` always
(it only renders in sign-up mode). The email placeholder
("you@example.com") already matches.

Fix files: `src/components/budget/login-card.tsx`.

### G3. [MED] Login inputs render NO focus ring; the reference renders the shadcn two-layer ring

Measured live on the reference (`.focus()` on the email AND password
inputs, settle-verified): on `:focus` the input renders border
`rgb(148,163,184)` (slate-400) PLUS the two-layer shadcn ring —

```
box-shadow: rgb(255, 255, 255) 0px 0px 0px 2px,
            rgb(148, 163, 184) 0px 0px 0px 4px,
            rgba(0, 0, 0, 0) 0px 0px 0px 0px
```

(white 2px offset layer + slate-400 4px ring + v3's transparent
transition layer — the trailing layer paints nothing per the v10
lesson). The clone's `INPUT_CLS` carries `focus:border-[#94a3b8]
focus:ring-[#94a3b8] focus:outline-none` — the border DOES change
(settle-verified) but v4's color-only `ring-[…]` utility emits NO
box-shadow without a width class, so the clone renders a bare border
swap and NO ring. The ref applies the ring on plain `:focus`
(programmatic `.focus()` triggers it — not `:focus-visible`-only).

Fix: pin the visible layers with an engine-independent arbitrary
shadow — replace `focus:ring-[#94a3b8]` with
`focus:shadow-[0_0_0_2px_#fff,0_0_0_4px_#94a3b8]` in `INPUT_CLS`
(covers email/password/confirm — all three inputs share it; the ref's
ring is identical on email and password, measured both). Hex values
compute to the exact measured rgb() strings; no v4 ring machinery
involved.

Fix files: `src/components/budget/login-card.tsx`.

### Observations (documented, no action)

- **The reference's TRAPPED sheet re-renders its active link with DARK
  text** — in the R2 trap state (post-navigation, sheet still up) the
  ref's Income link computes `color: rgb(24, 24, 27)` (its
  `sidebar-accent-foreground` token, per the `data-[active=true]:
  text-sidebar-accent-foreground` class on its shadcn-sidebar link)
  while keeping the gradient + fw 500. A FRESH-opened sheet at
  `/income` renders the v10-pinned WHITE text (`rgb(255,255,255)`) —
  re-measured today, both states, same session. The ref's sheet-active
  text color is therefore state-dependent (fresh-open: white;
  post-nav-trapped: dark) — a reference-internal inconsistency that
  only manifests in a state the clone deliberately does not have (the
  clone's sheet CLOSES on nav — superset fix #2). The clone pins the
  fresh-open state, verified byte-identical today (247×32, radius 8,
  pad 10px 12px, white + 135deg gradient + 500, others `#3f3f46`/400).
  No action; recorded so a future pass doesn't mistake the trapped
  state for the parity target.
- **"Continue with Google" is a REAL OAuth flow on the reference** —
  the click redirects through `accounts.google.com` (Base44 app client
  185178814199-…, redirect `app.base44.com/api/apps/auth/callback`).
  The clone's button chrome is byte-identical (368×54, white,
  slate-200 border, radius 12, 16px/500 `#334155`) and degrades to the
  honest-unavailable toast — the documented self-hosted divergence
  (same class as the forgot-password honest copy). No action.
- **Authenticated `/login` renders the card on BOTH sites** (no
  redirect): h1 "Welcome to ZeroBudget", form + Google + footer
  buttons, identical button census. No action.
- **autoComplete attributes**: the reference's inputs carry empty
  strings; the clone sets proper `email`/`current-password`/
  `new-password` hints — a password-manager-friendly superset (same
  class as the `<aside>` rail landmark). No action.
- **npm audit (code-audit Phase 2)**: 5 high — all in
  `eslint-config-next` → `fast-glob` → `micromatch` → `braces@3.0.3`
  (the stack-exhaustion advisory, GHSA-vfj7-8cjw-p6xm; no patched
  release exists — 3.0.3 IS latest). Dev-only lint toolchain, not
  runtime; npm's own "fix" downgrades eslint-config-next to 14 (a
  breaking change). Accepted + documented.
- **Secret scan (Phase 2)**: clean — the only `BEGIN OPENSSH PRIVATE
  KEY` hits are the wrapper's `OPENSSH_BEGIN` constant and the
  runbook's display-artifact troubleshooting snippet.

### Verified matching this pass (no action)

Mobile navigation (task focus, both sites 390×844): R1 re-confirmed
live (the ref's toast containers — TWO now, both `fixed top-0
z-[100]` 390×32 `pe:auto` — intercept the burger's center hit;
`elementFromPoint` returns the container; the clone's hit is DIRECT on
the svg; burger 28×28 at (24,16) both). R2 re-confirmed (tapping
Income in the ref's sheet navigated to `/income` with
`sheetStillOpen: true` — the trap; the clone's sheet CLOSED on nav).
R3 re-confirmed (no ref link active on `/`; clone highlights
Dashboard — superset #3 — white + gradient + 500, re-measured). R4
re-confirmed (ref scrollWidth 395 at 390; clone 390 on `/` and
`/income`). Sheet panel 288px both; sheet closes on Escape both (the
v12 observation holds); sheet active-state byte-identical in the
fresh-open state.

Register banner chrome (NEW): byte-identical both sides (the v12 pin
covers the register path). Login 401 text (NEW): "Invalid email or
password" identical. Sign-in placeholders (NEW): "you@example.com" +
"••••••••" identical. Date formats (NEW): "Oct 7, 2026" /
"Sep 27, 2026" — identical "MMM D, YYYY" card footers. Hero
progress-bar chrome (NEW): identical. OR divider (NEW): identical.
Google button chrome (NEW): byte-identical. Cursor sweep (NEW):
pointer/text identical. Authed `/login` (NEW): identical. Reference
data: unchanged since session 19.

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | G1: register 409 text → "A user with this email already exists" | `login-parity.spec.ts`: NEW "register duplicate-email error text (v13)" — sign-up state, `demo@zerobalance.app` + matching valid passwords, submit → banner (v12 chrome) renders the reference's exact text (ONE register call — its own rate-limit bucket, `register:<ip>`, budget-safe) | `register/route.ts` |
| 2 | G2: per-mode password placeholders | `login-parity.spec.ts`: NEW "sign-up password placeholders (v13)" — sign-up state: password ph "Min. 8 characters", confirm ph "Re-enter password"; sign-in state: password ph "••••••••" (pure DOM reads, no API) | `login-card.tsx` |
| 3 | G3: the login inputs' focus ring — two-layer arbitrary shadow on `:focus` | `login-parity.spec.ts`: NEW "login input focus ring (v13)" — focus the email input, settle, assert `borderColor rgb(148,163,184)` + `boxShadow` contains both visible layers (`rgb(255, 255, 255) 0px 0px 0px 2px` and `rgb(148, 163, 184) 0px 0px 0px 4px`); same for the password input in the sign-up state | `login-card.tsx` |
| 4 | Docs: session log (`docs/session_26.md`), worklog, README/AGENTS/CLAUDE/SKILL alignment + probe README v13 rows | — | docs |
| 5 | Regression: full chain + live parity re-check of every fixed surface + screenshot refresh only if visual deltas (the sign-in screenshot's placeholders are unchanged — expect NO regen) | — | — |

## Regression pin map (must NOT change)

- All six superset fixes (hamburger hit, sheet close-on-nav, root-URL
  nav highlight — rail AND sheet, no mobile overflow, Escape close,
  delete confirmations) and the v10–v12 sheet/banner/title pins
- The v12 error-banner chrome family (the G1 fix touches TEXT only)
- The v9 login per-state geometry pins (44px/48px controls, 14px
  button text) — the focus ring is additive chrome on the same inputs
- The v7 login hex-pinned slate family + logo ring + page gradient —
  the new focus shadow uses hex values from the same family
  (#94a3b8 = slate-400, #fff = white)
- The 404 client-side title pin (v7) and the route-segment title
  metadata (v12) — untouched
- v5–v11 surface pins: token block, `@variant hover`, dialog
  X/footers/labels/tiles, radio/switch `#171717`, 9999px radii, donut
  value-DESC, badge hex pins, plain-text menus, empty-state family,
  `.zb-btn-add` shadow/focus-ring family, 16px Add icons
- e2e fixture discipline: every spec restores what it mutates; login
  attempts stay within the rate-limit budget (the G1 test uses the
  register endpoint's own bucket; the sign-up state's failed register
  creates no rows — duplicate email 409s before any write)
