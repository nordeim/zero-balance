# Session 55 — Parity iteration v27 (session-53 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_53.md` / `docs/remediation-plan-v26.md`
/ `worklog.md` / `docs/session_54.md`. Full autonomy granted on the open
questions, so I worked the whole chain directly.

**Step 1 — workspace refresh.** `git pull` fast-forwarded to `d7d92f7`
(bringing in `docs/session_54.md`); the environment survived the session
boundary intact (`.env` with `DATABASE_URL="file:../db/custom.db"`, `db/`
at the repo root, node_modules, Vitest/Playwright configs, sitemap/robots
prerendering, `.env.example` — all re-verified). The five project docs +
four session docs re-read; the codebase validated against them
(scandihaven unchanged at `d4789c3`, patterns already reflected; the v26
changeset `2879cb0` in place — the classless body, the conditional OTP
autocomplete).

**Step 2 — the audit.** The baseline chain green on the first run: lint ✓
· typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**155/155 e2e** ✓ · 35/35 smoke ✓. Audit Phase 2 clean: the same 5
dev-only ESLint `braces` advisories (no patched release — accepted), the
secret scan matching only the documented files, and the v26 changeset
re-reviewed — clean, commented, test-pinned.

**Step 3 — the two-site sweep** (agent-browser on the ONE shared tab +
the :3200 parity server; the fresh open+settle + parked-pointer
disciplines throughout):

- **Mobile navigation (the task focus) R1–R4 all re-verified live — the
  21st consecutive check.** R1: the reference's two `fixed top-0 z-[100]`
  toast containers still intercept the burger's center hit at (38,30)
  (`pe:auto`, 390×32, z-100; scrollWidth 395 on `/`), while the clone's
  burger hit is DIRECT on the svg with the viewport `pe:none` and 390 fit
  on every route. R2: the reference's sheet still traps after nav
  (`sheetStillOpen: true`); the clone's closes (superset fix #2) — sheet
  288px + Income link (20,185) 247×32 identical. R3: the reference marks
  nothing active on `/` (all `rgb(63,63,70)`/400, no nav landmark); the
  clone highlights Dashboard (white/500 + the landmark). R4: the
  reference overflows 395 on `/`+`/dashboard` and 464 on `/networth`;
  the clone fits 390 on all six routes. **The Tailwind v4 pins hold —
  the clone's mobile menu works as expected.**
- **Data drift clean (21st)**: the reference unchanged (allocation 30.5%,
  Balance `$3475.00`, income `$5000.00`/1, savings `$1000.00`/1,
  expenses `$525.00`/4).
- **SEO pair ✓**: both sites serve robots.txt (allow-all + sitemap link)
  and sitemap.xml (five URLs, `/login` excluded).
- **v26 fixes re-verified live**: the reference's body still classless
  (`""` + `-webkit-font-smoothing: auto` on /login and /; html classless
  too); the clone's matches on the parity server; the G2 autocomplete
  distribution green in the e2e run.
- **Suggestion 1 — prefers-reduced-motion (first measurement, NO
  FINDING)**: under `reduce` (media emulation), the reference's sheet
  still runs its full 500ms slide-in (33ms position sampling: −288 →
  −111 @235ms → −7 @434ms → 0 @634ms) and the clone's matches; an
  `animate-spin` probe element reads `spin/1s/running` with its
  transform ROTATING on both sites; both CSSOMs contain ZERO
  reduced-motion rules. Neither site honors reduced motion — parity.
- **Suggestion 2 — print/overscroll (first measurement, NO FINDING)**:
  both sites — white body, `overscroll-behavior auto` on body+html,
  `overflow visible`, `margin 0`, ZERO print media rules.
- **Suggestion 3 — scrollbar styling at the dialog's `overflow-y-auto`
  (first measurement, NO FINDING)**: with a dialog forced to scroll at a
  600px viewport, both panels compute `maxHeight 540px` (90vh),
  `scrollbar-width auto`, `scrollbar-color auto`, zero
  `::-webkit-scrollbar` rules — native scrollbars on both.
- **Extensions (all clean)**: dark mode (both stay light — zero
  `prefers-color-scheme` rules, no color-scheme/theme-color meta); the
  app-surface REAL-Tab focus rings (rail links' blue `#3b82f6` 2px
  sidebar-ring — the v23-documented transparent-lead equivalence; the
  Add Item button's white-offset + `#0a0a0a` 1px + v3 ambient,
  byte-identical; the stat-card toggles' NO-ring, identical); the filter
  Select triggers + search inputs (byte-identical class lists,
  216×36, `focus:ring-1 focus:ring-ring`).
- **The dialog X-close button's keyboard/hover family (the ONE real
  finding — G1)**: the reference's X carries the shadcn ghost-icon base
  (`focus-visible:outline-none focus-visible:ring-1
  focus-visible:ring-ring` + `hover:bg-accent
  hover:text-accent-foreground`) — on a REAL 18-stop Tab walk its ring
  renders `#0a0a0a` at **1px**; the clone's hand-written
  `DialogCloseButton` carried `focus:outline-none
  focus-visible:ring-2` (a **2px** ring on real Tab) and no hover text
  family. Same finding class as v25 (distinct families per component —
  the reference's X runs the SAME family as the Cancel/Save buttons).
- Probe-methodology notes: the clone's Radix dialog TRAPS focus (the
  reference's plain-div dialogs do not), so the walk-to-X stop counts
  differ — a keydown-dispatched Tab inside one eval reaches the clone's
  X deterministically; and the `with-server.sh` one-invocation pattern
  boots pages against a dying server (the v16 zero-state renders
  honestly — the API + db were independently verified healthy).

**Step 4 — the plan + TDD.** `docs/remediation-plan-v27.md` written and
validated against the codebase (grep-verified scopes: the one class
string at `dialog.tsx:63`, the four bare usages, no existing X-class
pins, the other ring-2s all previously-pinned families). The v9 X-close
spec extended RED first (class-attribute assertions: `ring-1` present,
`ring-2` absent, `focus:outline-none` absent, `hover:text-accent-foreground`
present) → RED as expected (the received string showed the drift verbatim)
→ the one-line fix in `dialog.tsx` → GREEN → pin-sanity mutations (the
expected ring-2 + a wrong hover class) both FAIL → restored → GREEN.
Live re-verification on the :3200 parity server: the X's class list
carries the full reference family and a real-Tab press renders
`rgb(10,10,10) 0 0 0 1px` — the reference's exact visible layer.

**Step 5 — the chain.** **FULL CHAIN GREEN: 108 unit · 155 e2e (1
extended) · 35 smoke** + lint + typecheck + build. The screenshots
regenerated — byte-identical (git-clean; the X at rest is unchanged,
exactly as predicted).

**Step 6 — docs + ship.** README (the v27 row), CLAUDE.md (the e2e
list), AGENTS.md (the v27 pin paragraph), the SKILL (the session row),
the probe README (the v27 catalog + four persisted probe scripts), this
session log, the worklog. Committed and pushed to `main` through the SSH
wrapper.

## What this session did

- **Workspace refreshed** (`d7d92f7`), full doc chain re-read, all
  standing brief requirements re-verified in place
- **Baseline fully green on the first run** — 108/155/35; the audit clean
  (the same 5 dev-only advisories, no secrets, the v26 changeset clean)
- **Standing checks all clean**: mobile-nav R1–R4 (21st — Tailwind v4
  pins hold), data drift (21st), the SEO pair, the v26 fixes re-verified
  live
- **The session-53 suggested surfaces all swept on FIRST measurement —
  no drift**: prefers-reduced-motion (both sites animate identically
  under `reduce`), print/overscroll, scrollbar styling
- **One REAL fix** (`docs/remediation-plan-v27.md`): the dialog X-close
  button's keyboard-focus + hover family — `focus-visible:ring-1` (the
  shadcn ghost-icon base, 1px #0a0a0a on real Tab, matching the
  Cancel/Save family) + `hover:text-accent-foreground`; the clone had a
  2px ring with no hover text
- Full chain now **108/155/35 green**; docs/screenshots/worklog aligned;
  committed and pushed to main via the SSH wrapper

**Suggested next steps**: the X-family discipline suggests sweeping the
remaining interactive families that have never had a keyboard/hover
class read — the card action-menu TRIGGER (the "Active ▾" status button),
the avatar/user chip, and the toast close buttons (if the reference
renders any); alternatively a `:focus-visible` census of ALL button
variants at one go (a class-attribute dump diffed between the sites
would surface any remaining family drifts in one pass). Also open: the
reference's 5-attempts-exhausted lockout (still blocked behind its
register security gate).
