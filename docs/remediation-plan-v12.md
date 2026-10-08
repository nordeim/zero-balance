# Remediation Plan v12 — Session-23 Parity Iteration

Date: 2026-10-08 · Scope: fresh two-site re-audit after the v11 baseline
(`740d6e1` / code `00dad5a`) re-verified green (lint · typecheck · 96/96
unit · build · 107/107 e2e · 30/30 smoke). Probes: one-shot
`agent-browser eval` scripts, sessions `ref12`/`clone12` desktop
1280×800 + `ref12m`/`clone12m` 390×844, the standalone parity server on
:3200 booted per command through `with-server.sh` (the sandbox still
reaps background processes; the agent-browser daemon persists).

This pass swept state dimensions no earlier pass had measured: the
**login ERROR state** (wrong password / mismatched passwords — the
reference renders a red-tinted bordered banner, not bare text), the
**per-route document.title** set (the reference's SPA sets
`"Income | ZeroBudget"` etc. client-side), the **login page's root
landmark** (`<main>` on the reference, a bare `div` on the clone), the
**forgot-password confirmation state** (the reference transitions to a
"Check your email" view), the **expenses payment-method filter card +
its listbox OPEN state**, and an **a11y structure sweep** (h1s, lang,
landmarks, button accessible names). The mobile-navigation stack (the
task focus) was re-verified end-to-end first. It found **4 clone-side
finding groups**; no new reference bugs (R1/R2/R4 all re-confirmed
live; reference data unchanged since session 19: allocation 30.5%,
expenses `$525.00` with the documented `$0.00` "Miscellaneous"
residual).

---

## Findings ledger

### G1. [MED] Login error message renders as bare red text; the reference renders a red-tinted bordered banner

Measured live on the reference (wrong-password sign-in AND mismatched
confirm on sign-up — the same slot renders both): the error renders as
a direct child of `form.space-y-4 sm:space-y-5`, a block DIV with

- `background-color: rgba(254, 242, 242, 0.7)` (red-50 at 70%),
- `border: 1px solid rgb(254, 202, 202)` (red-200),
- `border-radius: 12px`, `padding: 16px` (all sides), box 368×54,
- inner DIV (`[&_p]:leading-relaxed text-red-700 text-sm` — the shadcn
  FormMessage pattern): `#b91c1c` (red-700), 14px/400, line-height
  20px, **text-align: center**,
- spacing from the form's space-y: 20px above (after the password
  field) and 20px below (before the submit button) at ≥640px (16px at
  mobile — the form's own space-y classes).

The clone renders `<p role="alert" className="text-sm font-medium
text-[#dc2626]">` — wrong color (`#dc2626` red-600 vs `#b91c1c`
red-700), wrong weight (500 vs 400), centered nowhere, and NO banner
chrome (no background, border, radius, or padding). The error slot's
POSITION already matches (the `p` is a direct form child in the same
slot, so the space-y gaps are already correct).

Fix: replace the `p` with the banner structure — outer `div
role="alert"` (keep the a11y role; the reference's div has none — a
superset) carrying the banner chrome via inline styles (parity-surface
pattern: exact rgba, engine-independent), inner centered div with the
measured text styles.

Fix files: `src/components/budget/login-card.tsx`.

### G2. [MED] Per-route document.title missing; the reference sets "Income | ZeroBudget" etc. client-side

Measured live on the reference (every route, after SPA navigation):

| Route | Reference `document.title` |
|-------|----------------------------|
| `/` | `ZeroBudget` |
| `/dashboard` | `ZeroBudget` |
| `/income` | `Income | ZeroBudget` |
| `/expenses` | `Expenses | ZeroBudget` |
| `/savings` | `Savings | ZeroBudget` |
| `/networth` | **`Networth | ZeroBudget`** (one word — the reference's own spelling) |
| `/login` | `ZeroBudget` |

The clone renders `ZeroBudget` on every route (only the 404 page sets
a client-side title — the v7 pin). The reference is an SPA whose
titles land client-side after navigation; the clone's static
prerendered shells carry the static default. Reproduce the reference's
behavior with a client-side route→title effect in the AppShell (all
six workspace routes render through it; `/login` is outside the shell
and keeps the static default — matching the reference's `ZeroBudget`).

Fix: a `ROUTE_TITLES` map + a `usePathname()`-driven
`document.title` effect in `src/components/budget/app-shell.tsx`.

Fix files: `src/components/budget/app-shell.tsx`.

### G3. [LOW] Login page root is a bare div; the reference uses a `<main>` landmark

Measured live: the reference's login root is `<main class="min-h-screen
flex items-center justify-center bg-gradient-to-br from-slate-50
to-slate-100 p-4">` (flex, centered, p-4 — the card at 448×746 within
it). The clone's root renders the IDENTICAL computed styles (flex
`min-h-screen items-center justify-center p-4` + the same
slate-50→slate-100 gradient as an inline style, the v7 pin) but as a
bare `<div>` — a landmark difference for screen readers (the login
card is not inside any `main` landmark on the clone).

Fix: tag swap `div` → `main` on the login root (zero visual delta;
the classes and inline styles stay exactly as they are).

Fix files: `src/components/budget/login-card.tsx`.

### G4. [LOW] Forgot-password submit renders a toast; the reference transitions to a confirmation state

Measured live on the reference: submitting "Send reset link"
transitions the card to a centered confirmation state — H2 "Check your
email" 24px/700 `#0f172a` lh 32 centered; P "We've sent password reset
instructions to {email}" 16px/400 `#475569` lh 24 mt 8 centered; DIV
"Please check your email for the password reset link. It may take a
few minutes to arrive." 16px/400 `#09090b` lh 24 mt 24 centered;
BUTTON "Back to sign in" 14px/500 `#64748b` lh 20 mt 24 centered (the
form is replaced by the state).

The clone currently keeps the user on the form and toasts "Password
reset unavailable" (an honest, documented self-hosted decision — there
is no mail transport, and pretending a link was sent would lie to the
user).

Decision (parity-first + honest content): reproduce the reference's
confirmation STATE — its layout, typography, and the "Back to sign in"
return navigation — with honest copy: heading "Password reset
unavailable" and descriptions explaining that this self-hosted
instance has no email service configured. The state chrome matches the
reference exactly; the TEXT is a documented deliberate divergence (the
same class of decision as the no-logout-UI observation in v11). The
toast is replaced by the state.

Fix files: `src/components/budget/login-card.tsx`.

### Observations (documented, no action)

- **The reference's mobile sheet DOES close on Escape** (verified live
  this pass — unlike its dialogs, which ignore Escape AND outside-click,
  reference bug R5). The clone's Radix sheet also closes on Escape —
  matching behavior, no action.
- **Expenses payment-method filter**: geometry (three 216×36 triggers,
  `#e5e5e5` border, radius 6, space-between), search placeholder, and
  the listbox OPEN state (218 wide, 32px options, 14px, selected
  `#f5f5f5`) are identical both sides. The option COUNT differs only
  because the reference's expense items carry no payment methods (1
  option) while the clone's seed has Bank Transfer + Credit Card — a
  data difference, not rendering.
- **A11y sweep**: h1 sets identical on the dashboard ("ZeroBalance"
  20px + "Budget Dashboard" 36px, both visible); `lang="en"` both;
  login h1 "Welcome to ZeroBudget" + accessible button names match.
  The clone's desktop rail is an `<aside>` landmark while the
  reference's is a plain div — the clone is the a11y superset here;
  no action.
- **Reference data state unchanged** since session 19 (allocation
  30.5%, expenses `$525.00`, 4th item the `$0.00` "Miscellaneous"
  residual; income `$5000.00` 1 item, savings `$1000.00`).

### Verified matching this pass (no action)

Mobile navigation (task focus, both sites 390×844): R1 re-confirmed
live (the ref's toast container `fixed top-0 z-[100]` 390×32
`pe:auto` intercepts its burger's center hit — elementFromPoint returns
the container; the clone's hit is DIRECT on the svg); R2 re-confirmed
(tapping Income in the ref's sheet navigated to `/income` with
`sheetStillOpen: true` AND `overlayStillUp: true` — the trap — while
its Income link renders the FULL active style: white + the 135deg
forest-medium→lime gradient + fw 500); R4 re-confirmed (ref scrollWidth
395 at 390; clone 390 on `/` and `/income`); the clone's sheet
highlights Dashboard on `/` (v10 fix + superset #3) and CLOSES on nav
with the 390px fit; burger/topbar geometry identical (28×28 at
(24,16)); clone seed arithmetic intact (`+$2065.00`, 62.8%).

Expenses filter card (NEW): trigger census + search placeholder +
header counts format identical. Payment-method listbox open state
(NEW): identical geometry. Login titles (NEW): `/login` and `/`
render `ZeroBudget` both sides. Dashboard a11y (NEW): identical h1s,
lang, and button names; landmark sets compatible (clone superset).
Data drift check: reference unchanged.

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | G1: the error banner — replace the bare `p` with the reference's chrome (bg `rgba(254,242,242,0.7)`, border `#fecaca`, radius 12, pad 16; inner centered `#b91c1c` 14px/400 lh 20) | `login-parity.spec.ts`: NEW "login error banner (v12)" — sign-up mismatched passwords (pure client-side, no API budget): banner chrome + inner text styles + the 54px height; extend `auth.spec.ts`'s existing wrong-password test to assert the banner renders with "Invalid email or password" (zero extra login attempts) | `login-card.tsx` |
| 2 | G2: per-route titles — `ROUTE_TITLES` map + `usePathname()` effect in the AppShell | `not-found.spec.ts`: NEW "per-route document titles (v12)" in the head-parity area — all six workspace routes + `/login` (networth asserts the one-word `Networth`) | `app-shell.tsx` |
| 3 | G3: login root `div` → `main` | `login-parity.spec.ts`: extend the card-chrome test with a landmark assertion (`main` exists, contains the card, keeps `p-4` + centering) | `login-card.tsx` |
| 4 | G4: the forgot confirmation state — reference layout/typography with honest copy, replacing the toast | `login-parity.spec.ts`: NEW "forgot-password confirmation state (v12)" — submit "Send reset link" → H2 24px/700 `#0f172a`, desc 16px `#475569`/`#09090b`, back button 14px/500 `#64748b`; "Back to sign in" returns to the sign-in state | `login-card.tsx` |
| 5 | Docs: session log, worklog, README/AGENTS/CLAUDE/SKILL alignment + probe README v12 rows | — | docs |
| 6 | Regression: full chain + live parity re-check of every fixed surface (incl. the mobile banner geometry) + screenshot refresh if visual deltas | — | — |

## Regression pin map (must NOT change)

- All six superset fixes (hamburger hit, sheet close-on-nav, root-URL
  nav highlight — rail AND sheet, no mobile overflow, Escape close,
  delete confirmations) and the v10/v11 sheet + button pins
- The v9 login per-state geometry pins (44px/48px controls, 14px
  button text) — the banner adds chrome in an already-correct slot
  (the form's own space-y supplies the gaps)
- The v7 login hex-pinned slate family + logo ring + page gradient —
  the banner's reds join them as inline-style pins (red-50/70%,
  red-200, red-700)
- The 404 client-side title pin (v7) and the static head metadata —
  the AppShell title effect only touches `document.title` client-side
- v5–v11 surface pins: token block, `@variant hover`, dialog
  X/footers/labels/tiles, radio/switch `#171717`, 9999px radii, donut
  value-DESC, badge hex pins, plain-text menus, empty-state family,
  `.zb-btn-add` shadow/focus-ring family, 16px Add icons
- e2e fixture discipline: every spec restores what it mutates; login
  attempts stay within the rate-limit budget (the new banner test uses
  the client-side signup-mismatch path; the wrong-password extension
  reuses the existing attempt)
