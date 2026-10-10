# Session 72 — Parity iteration v35 (session-70 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_70.md` /
`docs/remediation-plan-v34.md` / `worklog.md` / `docs/session_71.md`.
Full autonomy granted on the open questions, so I worked the whole chain
directly.

**Step 1 — workspace rebuild.** The sandbox had been RESET — the repo,
node_modules, .env, and the db/ seed were all gone. Fresh
`git clone` (HEAD `54b07f4` — the session-log commit carrying
session_70/71), `npm install`, `.env` restored from `.env.example`
(`DATABASE_URL="file:../db/custom.db"` + the dev AUTH_SECRET + the
:3200 site URL), `db/` pushed + seeded at the repo root (7 items,
demo@zerobalance.app), `scandihaven` re-cloned (the reference-only
repo, never compiled). The five project docs re-read; the codebase
validated against them — the v34 changeset in place (the S1/S2 pins,
the 168 suite), verified by the full chain below.

**Step 2 — the audit.** The baseline chain green on the FIRST full run:
lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap
prerendered) · **168/168 e2e ✓** · 35/35 smoke ✓. Audit Phase 2 clean:
the same 5 dev-only ESLint `braces`/eslint-config-next advisories (no
patched release — accepted, dev-only), the secret-pattern scan clean,
`.env.example` verified current.

**Step 3 — the two-site sweep** (agent-browser on the ref35/clone35
sessions + the :3200 parity server; the fresh-open + settle +
parked-pointer + real-click/real-hover/real-Tab disciplines + the v34
`document.hasFocus()` gate throughout):

- **Mobile navigation (the task focus) R1–R4 all re-verified live on BOTH
  sites — the 29th consecutive check.** R1: the reference's `fixed
  top-0 z-[100]` toast containers still intercept the burger's center
  hit (scrollWidth 395), the clone's hit DIRECT on the svg with 390
  fit. R2: the reference's sheet still traps after nav; the clone's
  closes (superset #2). R3: the reference marks nothing active on `/`
  and has no `<nav>`; the clone highlights Dashboard (white/500 —
  verified directly this session) + the landmark. R4: the reference
  overflows 395 on `/`+`/dashboard` and 464 on `/networth`; the clone
  fits 390 on all six. **The Tailwind v4 pins hold — the mobile menu
  works as expected.**
- **Data drift clean (29th)**: the reference's own census re-verified
  before and after (allocation 30.5%, income `$5000.00`/1, savings
  `$1000.00`/1, expenses `$525.00`/4 — read-only throughout; the
  from_url probe logged in once with the correct password, the menu
  probes Escape-closed, nothing selected).
- **SEO pair ✓**: the robots/sitemap/head census re-captured on the
  reference — all matching the pinned values.
- **The item-card action menus' open-state focus chrome (the
  session-70 suggestion #1) — TWO drifts (G1/G2) + the rest
  byte-identical.** The full keyboard contract measured first-time with
  REAL keys on both sites: fresh-open via CLICK lands focus on the
  menu CONTAINER, via ENTER on the FIRST item (both sites identical on
  both paths — the first clone probe compared its Enter-open against
  the reference's click-open and fabricated a phantom landing
  difference, resolved by measuring the full matrix); ArrowUp from the
  container lands on the LAST item (the Radix convention — an
  Enter-open-then-ArrowUp reads a clamped first item and contaminated
  the first S1 draft); arrows rove with the accent highlight; Home/End
  jump; Tab while open is TRAPPED; Escape closes + returns focus to
  the trigger; the trigger is 36×36, hover-revealed (opacity-0 at rest
  on BOTH), and its REAL-Tab focus-visible chrome is the shadcn 1px
  #0a0a0a ring family. **G1: the focused DELETE renders
  `rgb(23,23,23)` accent-foreground on the reference but RED
  `rgb(220,38,38)` on the clone** — the clone's v5-era
  `focus:text-[#dc2626]` migration (never re-measured; the reference's
  `focus:text-accent-foreground` outspecifies its `text-red-600`).
  **G2: the clone's menu triggers carried NO focus-visible ring at
  all** (`box-shadow: none` vs the reference's 1px #0a0a0a
  three-layer ring) — the clone's DropdownMenuTrigger is the RAW Radix
  primitive. The net-worth asset/liability menus re-measured: the same
  two drifts + the same byte-identical contract.
- **The quick-action buttons' focus-visible family (suggestion #2) —
  NO drift (first-time measurement; S2 pin).** The reference's Add
  Item, REAL-Tab-measured: the FOUR-layer composite (white 0px lead +
  1px #0a0a0a ring + the gradient family's two ambient layers) + v3's
  outline-none. The clone renders the byte-identical string (the
  `.zb-btn-add:focus-visible` v11 rule); the dashboard instance now
  pinned (the dialog instances were, the header instance never was).
  Rest-state: the visible ambient identical on both (the reference's
  two transparent lead slots are its compiled-output artifact).
- **The deep-link/URL contract (suggestion #3) — NO drift (S3 pin +
  one documented superset).** The reference's login HONORS
  `?from_url=/income` (measured live — logout via its
  `/api/auth/logout` POST, then the param'd login lands on `/income`);
  the clone byte-matches; pinned. The 404: the title derivation
  byte-identical (`No Such Route | ZeroBudget`), the quoted path, the
  slate-family Go Home — the reference's is a BUTTON (client-side
  navigate), the clone's a real `Link href="/"` — a documented
  SUPERSET (crawler-followable, middle-clickable, click-identical).
- **The VLM pairwise (two fresh pairs, viewport-asserted 1280×800)**:
  the dashboard — VERDICT IDENTICAL, flags DOM-explained (the
  Dashboard-active rail = superset #3; the avatar letter + progress
  fill = the different demo data); the income page with the action
  menu OPEN + Delete highlighted — VERDICT IDENTICAL, zero flags (the
  G1 red-vs-dark text is a 12px color difference below VLM resolution
  — the DOM-level measurement is the authority).

**Step 4 — the plan + TDD** (`docs/remediation-plan-v35.md`, validated
against the codebase pre-execution). TDD: the S1 test written FIRST —
RED on exactly the G1 drift (`Expected "rgb(23, 23, 23)" / Received
"rgb(220, 38, 38)"`) — then the G1 fix (the `focus:text-[#dc2626]`
override removed on all three Delete items) → the trigger-ring
assertion surfaced **G2** (the trigger's `box-shadow: none`) → the G2
fix (the shadcn ring family added to all three triggers) → **GREEN**;
pin-sanity: the override re-added → the color assertion FAILS ✓; the
ring stripped → the ring assertion FAILS ✓ (the strip also removed the
expense-card buttons' ring family — the full-chain re-run caught it,
restored, the final changeset re-verified against `git diff` before
shipping) → GREEN. S2 (the dashboard Add Item focus-visible composite)
GREEN on the first run; pin-sanity (the `.zb-btn-add:focus-visible`
box-shadow stripped) → FAILS ✓ → restored → GREEN. S3 (the from_url
deep-link) GREEN on the first run (the implementation was already
correct — `login-card.tsx` reads the param with the `/` fallback; the
test pins it).

**Step 5 — the chain.** **FULL CHAIN GREEN: 108 unit · 171 e2e (168 →
171) · 35 smoke** + lint + typecheck + build. The dev DB census clean
(7 items / 0 line items / 0 probe users). The 16 screenshots
regenerated (the two net-worth shots' diffs = the seeded relative
dates rolling forward — content-level, not visual).

**Step 6 — docs + ship.** The probe README (the v35 catalog + the
L1–L5 lessons), README (the v35 row + the 171 counts), CLAUDE.md (the
171 count + the v35 surface entries), AGENTS.md (the v35 paragraph),
the SKILL doc (the state line + the Session-70 row), this session
log, the repo worklog (the Session 68 entry), the workspace worklog.

## What this session did

- **Workspace REBUILT from scratch** (the sandbox reset — clone,
  install, .env, db/ push + seed, scandihaven re-clone); the baseline
  chain green on the first full run
- **Standing checks all clean (29th consecutive)**: mobile-nav R1–R4
  on both sites (**Tailwind v4 pins hold, the mobile menu works**),
  data drift (reference read-only), the SEO pair
- **The session-70 suggested surfaces all swept with first-time
  REAL-key measurements**: the action-menu focus chrome (TWO drifts
  found + fixed), the quick-action focus-visible family (byte-
  identical, pinned), the deep-link/URL contract (byte-identical,
  pinned; the 404 link-vs-button documented as a superset)
- **G1 + G2 fixed** (the focused Delete's accent-foreground cascade;
  the triggers' shadcn focus-visible ring) + **three new pins**
  (S1/S2/S3, TDD with pin-sanity mutations) → **108/171/35 green**
- Full chain green; docs/screenshots/worklog aligned; committed and
  pushed to main via the SSH wrapper

**Suggested next steps**: the unmeasured families keep shrinking — the
item-card menu's HOVER-highlight family (hover → Radix moves focus →
the same accent tint; verified implicitly but never asserted), the
filter selects' listbox keyboard contract (the v34 frequency pin
covered the sub-dialog instance; the /income filter instances never
measured), or the tab-key order census of the whole items view (the
v33 sub-dialog census covered the dialog, not the page). Or the
tooling pass (a `document.hasFocus()` assertion helper baked into the
probe README's standing scripts, a Playwright a11y audit CI step).
Just re-issue the brief referencing `docs/session_72.md` /
`docs/remediation-plan-v35.md` and I'll pick it up from there.
