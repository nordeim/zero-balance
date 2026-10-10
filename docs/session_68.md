# Session 68 — Parity iteration v33 (session-67 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_66.md` / `docs/remediation-plan-v32.md`
/ `worklog.md` / `docs/session_67.md`. Full autonomy granted on the open
questions, so I worked the whole chain directly.

**Step 1 — workspace refresh.** `git pull` brought in the session-log
commit `3818922` (the session-67 transcript). The workspace otherwise
survived intact from v32 — node_modules, `.env` with
`DATABASE_URL="file:../db/custom.db"`, the `db/` seed at the repo root
all re-verified; `scandihaven` (the reference-only repo) was re-cloned.
The five project docs + the four session docs re-read; the codebase
validated against them — the v32 changeset in place (the 165-test
suite, the zb-row-action pin, the breakdown aria-expanded pins),
verified by the full chain below.

**Step 2 — the audit.** The baseline chain green on the FIRST full run:
lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap
prerendered) · **165/165 e2e ✓** · 35/35 smoke ✓. Audit Phase 2 clean:
the same 5 dev-only ESLint `braces`/eslint-config-next advisories (no
patched release — accepted, dev-only), the secret-pattern scan matching
only the documented files, `.env.example` verified current.

**Step 3 — the two-site sweep** (agent-browser on the ref33/clone
sessions + the :3200 parity server; the fresh-open + settle +
parked-pointer + real-click/real-hover/real-Tab disciplines throughout):

- **Mobile navigation (the task focus) R1–R4 all re-verified live on BOTH
  sites — the 27th consecutive check.** R1: the reference's `fixed
  top-0 z-[100]` toast containers still intercept the burger's center hit
  (scrollWidth 395), while the clone's burger hit is DIRECT on the svg
  with 390 fit on every route. R2: the reference's sheet still traps
  after nav (the robust structure detector on `/income`: sheet open,
  body locked, 3 dark overlays); the clone's closes (superset fix #2).
  R3: the reference marks nothing active on `/` and has no `<nav>`
  landmark; the clone highlights Dashboard + has the landmark. R4: the
  reference overflows 395 on `/`+`/dashboard` and 464 on `/networth`;
  the clone fits 390 on all six routes. **The Tailwind v4 pins hold —
  the clone's mobile menu works as expected.**
- **Data drift clean (27th — the reference only read)**: allocation
  30.5%, Balance `$3475.00`, income `$5000.00`/1 (Salary), savings
  `$1000.00`/1 (Emergency Fund), expenses `$525.00`/4 — verified before
  and after the probe cycles (the register throwaway + the
  same-values item save never moved the census).
- **SEO pair ✓** (live, both sites): robots.txt + sitemap.xml live on
  both; the full head-metadata census byte-identical; canonical +
  og:image keyed off `NEXT_PUBLIC_SITE_URL`; the reference's
  `/manifest.json` still 302s empty (broken) while the clone's
  `manifest.webmanifest` serves the v7-pinned document — a superset.
- **The line-item sub-dialog's focus traversal (session-67 suggestion
  #1) — NO finding, byte-identical at every axis.** Both sites' "Add
  Line Item" sub-dialog renders exactly THIRTEEN focusable stops in the
  same order (X → name → amount → frequency → provider → policy → the
  two native dates → payment → status → notes → cancel → save); a REAL
  Tab walk reproduces the same sequence on both, INCLUDING the native
  date segments (each `<input type="date">` is a 4-stop segment walk —
  8 consecutive date stops; browser-native, identical). The deltas are
  the two documented Radix supersets (auto-focus X on open vs the
  reference's stays-on-trigger; the trap wrap vs the reference's exit).
  The reference's plain-div dialogs IGNORE Escape (measured — two
  Escape presses left the sub-dialog open).
- **The sub-dialog's select triggers' focus chrome — NO finding, a
  probe lesson.** The clone's Frequency/Status triggers under REAL
  keyboard focus resolve `--tw-ring-color: #0a0a0a` +
  `--tw-ring-shadow: 0 0 0 calc(1px + 0px) #0a0a0a` — the 1px ring IS
  present as the FOURTH layer of v4's composed box-shadow, behind
  three zero-width transparent placeholders. The first 85-character
  read looked like "no ring" — a truncated read fabricates the
  finding; always read the FULL string plus the `--tw-ring-*`
  properties.
- **The register/verify-email focus families (suggestion #2) — ONE
  drift (G1).** The register inputs (v13 slate family), the verify
  submit (v25 zinc family), the Resend + Back buttons (browser-default
  on both) all matched. The code inputs did not: the reference's
  focused box renders the 2px zinc-950 ring with NO border tint and
  the FIRST box auto-focuses on landing; the clone rendered an
  invented slate tint, no ring, no auto-focus.
- **The toast's focus semantics (suggestion #3) — NO finding; the
  clone is the documented superset at every layer.** The reference's
  viewports are semantic-less `pointer-events: auto` divs (the R1
  burger-blocker root cause) and its live toasts never fired on
  item-edit-save, line-item save, or line-item delete (measured). The
  clone's viewport is the labeled `pointer-events: none` region; its
  live toast is a focusable li plus Radix's hidden
  `role="status" aria-live="assertive"` announcer portal (measured
  inside its 1-second mount window: "Notification Line item added").
  Pinned (S1) so a toast-system rewrite cannot silently drop the
  announcement.
- **The performance/bundle pass (suggestion #4) — NO finding
  (documented numbers).** The clone's dashboard: 12 chunks, 1,104KB
  raw / 338KB gz + 147KB CSS, nav 66ms / DCL 26ms. The reference: one
  1,060KB raw / 317KB gz bundle + 68KB CSS + a 214KB dev-only badge.js.
  Wire-weight parity with a route-split superset. (No Lighthouse CLI
  in this environment — the resource-timing + curl census
  substitutes.)
- **The VLM pairwise (two fresh pairs, viewport-verified)**: the
  dashboard — IDENTICAL layout, one flag DOM-explained (the
  Dashboard-active rail = superset #3); the verify-email state — one
  flag DOM-explained (the dev-code hint box = the documented honest
  no-mail dev variant). Probe lesson: the FIRST dashboard pair this
  session compared a desktop reference against a mobile clone shot
  (the default agent-browser session kept a stale 390×844 viewport)
  and produced a phantom full-page drift verdict — re-assert the
  viewport before pairing.
- Probe-methodology notes: (a) v4's ring composition buries the
  visible ring in the FOURTH box-shadow layer — read the FULL string;
  (b) persistent sessions keep their last viewport; (c) the clone's
  Radix DialogContent is NOT inside a `div.fixed` (the overlay and
  content are portal SIBLINGS — anchor probes with
  `closest('[data-state=open],[role=dialog]')`; two silent probe
  failures this session); (d) the reference's plain-div dialogs ignore
  Escape — never assume closed; (e) the reference's register form is
  a STATE on `/login` (the `/register` route 404s).

**Step 4 — the plan + TDD.** `docs/remediation-plan-v33.md` written and
validated against the codebase (grep-verified: no `focus:shadow` in the
code-input class, no `autoFocus` in login-card.tsx, the register-input
precedent idiom at line ~200, no `[role=status]` assertions in the
calculator flow, the rate-limit budget at 6+1 of 10). TDD: the G1 test
written → RED (the auto-focus assertion failed first) → the
`focus:shadow-[0_0_0_0_#fff,0_0_0_2px_#09090b] focus:outline-none`
family + `autoFocus={i === 0}` → **GREEN**. Pin-sanity mutations: the
shadow family removed → the ring assertion FAILED; the autoFocus
removed → the focus assertion FAILED; restored → GREEN. The S1
announcer pin added to the calculator's line-item-add test → GREEN;
pin-sanity: the Radix Root swapped for a plain `li` (the
no-announcer rewrite simulation) → the pin FAILED; restored → GREEN.

**Step 5 — the chain.** **FULL CHAIN GREEN: 108 unit · 166 e2e · 35
smoke** + lint + typecheck + build (the suite went 165 → 166). Live
re-verification on the :3200 parity server: the register lands with
`INPUT / Digit 1` focused; the REAL-Tab-focused Digit 2 reads
`rgb(255,255,255) 0px 0px 0px 0px, rgb(9,9,11) 0px 0px 0px 2px` (the
2px zinc ring, byte-matching the reference's measurement modulo v4's
invisible zero-width lead layers) + the untinted `rgb(228,228,231)`
border. The mobile-nav R1/R4 spot check clean (direct svg hit, 390
fit). The 16 screenshots regenerated; the dev db restored after the
probe cycles (the toast-probe line items deleted, the Entertainment
parent back to $65, the probe users deleted — verified 2235 total /
0 line items).

**Step 6 — docs + ship.** The probe README (the v33 catalog + the five
lessons), README (the v33 row + the 166 counts), CLAUDE.md (the e2e
description + counts), AGENTS.md (the v33 verification paragraph), the
SKILL doc (the session row + the 166-test state), this session log,
the worklog.

## What this session did

- **Workspace refreshed** (`git pull` — the session-67 transcript
  commit) + the environment re-verified; the baseline chain green on
  the first full run
- **Standing checks all clean (27th consecutive)**: mobile-nav R1–R4 on
  both sites — **Tailwind v4 pins hold, the mobile menu works**; data
  drift clean (reference read-only, verified before + after the probe
  cycles); the SEO pair live (full head census byte-identical)
- **The session-67 suggested surfaces resolved with first-time
  measurements**: the line-item sub-dialog's focus traversal (NO
  finding — 13-stop census + REAL-Tab walk byte-identical, the native
  date-segment stops included), the register/verify-email focus
  families (one finding: the code inputs' ring + auto-focus), the
  toast's focus semantics (NO finding — the Radix announcer superset,
  measured + pinned), and the bundle pass (documented parity with a
  route-split superset)
- **TWO changes** (`docs/remediation-plan-v33.md`): the
  `focus:shadow-[0_0_0_0_#fff,0_0_0_2px_#09090b] focus:outline-none`
  family + `autoFocus={i === 0}` on the verify-email code inputs (the
  only production-code drift), and the toast announcer pin (the
  role=status/aria-live portal assertion) — TDD with pin-sanity
  mutations, the fix live-re-verified byte-identical
- Full chain **108/166/35 green**; docs/screenshots/worklog aligned;
  committed and pushed to main via the SSH wrapper

**Suggested next steps**: the keyboard sweep still has unmeasured
families — the forgot-password/reset state's focus walk, the item-card
action menus' open-state focus chrome, or the calculator's frequency
Select popup keyboard contract (arrow roving inside the listbox); or
the correctness pass (API error-tier audits, the money-math edge
cases, a Prisma query review). Just re-issue the brief referencing
`docs/session_68.md` / `docs/remediation-plan-v33.md` and I'll pick it
up from there.
