# Session 119 — Parity iteration v51: the verify-email mode container's missing `.zb-auth-mode` conversion (THE FIX — the third production-code change since v46, completing the v50 F1's claimed-but-never-applied third site) + four 390 pin surfaces (2026-10-12)

**Goal:** the session-118 v51 queue's read-only members — the savings
goal-card mobile census, the hero stats-card row's 390 reflow (the
verify-email panel census resolved WITHOUT a reference write) — plus
two sibling sweep surfaces the same session added (the Budget
Guidelines card at 390, the quick-actions row at 390). TDD-first,
docs aligned, commit + push via the SSH wrapper. (The workspace
SURVIVED this session — a `git pull` fast-forward to 7a7f912, the
session_118.md "update session log" commit on top of the v50 parity
commit f807aac; the environment was already in place: node_modules,
the seeded db/custom.db, the .env contract.)

## What was done

**Step 0 — the workspace.** `git pull` fast-forwarded f807aac →
7a7f912 (docs/session_118.md added — the v50 session's narrative +
the v51 queue suggestions). The five core docs (AGENTS / CLAUDE /
README / PAD / SKILL) + the four session docs (session_117 /
remediation-plan-v50 / the repo worklog / session_118) reviewed; the
v50 state verified: the `.zb-auth-mode` + `.zb-sm6` rules in
globals.css, the signup/forgot container swap at login-card.tsx:705,
the 236 e2e, .env `file:../db/custom.db` with db/ at the repo root,
the sitemap/robots pair, .env.example matching.

**Step 1 — the baseline chain.** lint ✓ · typecheck ✓ · 108/108 unit
✓ · build ✓ (robots + sitemap prerendered) · **236/236 e2e ✓ (5.4m)**
· 35/35 smoke ✓. The audit: npm audit = 0 production vulnerabilities
(the same 5 dev-only ESLint-chain advisories); the secret-pattern
scan clean; `.env` ≡ `.env.example` (modulo the dev AUTH_SECRET).

**Step 2 — the 45th standing checks.** Reference side
(`ref-standing-v49.sh`, re-run verbatim): all four bugs live — the
toast-blocker (the hit `DIV.fixed top-0 z-[100]`,
hitIsBurgerChild false), the sheet-trap (the overlayCount census:
`sheetOpenAfterNav false, overlayCount 1` — the z-50 scrim remains on
/income after the nav click), no nav landmark, the /networth 464
overflow; the data census read-only ("1 items · $25,000" networth /
"1 items · $5000.00" income — intact before + after); the SEO pair
live. Clone side (`standing-checks-v49.sh` via with-server): R1 the
burger hit-test + the sheet opens, R2 the sheet closes on nav, R3 the
landmark, R4 docSW 390 on all five routes, the SEO pair. **The 45th
standing checks ALL CLEAN.**

**Step 3 — the v51 sweep.** The probe pair
(`scripts/parity-probes/ref-v51.sh` + `clone-v51.sh`, READ-ONLY on
the reference): (1) the dashboard STATS ROW at 390 — the three
StatCards' grid (1-col/24px-gap), the cards 210 tall @ y 949/1183/
1417 on BOTH sites (the full-page vertical rhythm byte-identical),
the radius-16/pad-24 card + the rgba(0,0,0,0.06) 0px 4px 20px
shadow, the 48px icon circle, the title/amount/count-row chrome —
byte-parity; (2) the SAVINGS view at 390 — the goal card radius
12/pad 20/the rgba(0,0,0,0.04) 0px 2px 8px shadow, the H4/subtitle/
amount/dot/badges chrome, the H1 30/700, the filter card, the search
308×36 — byte-parity (the card HEIGHT 230-vs-200 is a data class:
the richer seed's 4-chip badge row wraps to 52px where the
reference's 3 chips fit one 22px row); (3) the BUDGET GUIDELINES
card at 390 — the 380-tall card at radius 12, the BLOCK tiles stack,
the three tiles h 94/94/78 with the byte-identical tinted pairs, the
shadow re-measured UNSLICED (the shadow-sm VISIBLE pair + the
accepted 4-vs-2 lead divergence) — byte-parity; (4) the
QUICK-ACTIONS row at 390 (the sibling sweep) — the three 90-tall
cards @ y 2751/2865/2979 on BOTH sites, the 40×40 icon circle, the
trailing plus's `ml-auto opacity-50 group-hover:opacity-100
transition-opacity` class string read DIRECTLY from the reference's
own DOM — byte-parity. **Four pin-only surfaces.**

**Step 4 — THE REAL GAP.** A systematic Tailwind v4 trap-log audit
(a scripted scan for space-y containers with children carrying
mt-/mb- utilities — the rule-4 family) walked the flagged sites and
found the login-card verify branch: **the v50 F1's third-site
conversion was CLAIMED but NEVER APPLIED.** The v50 plan (§F1), the
v50 commit message, and all five docs state "the verify-email
branch's same-idiom container converted" — the v50 diff landed the
DESCRIBING COMMENT at login-card.tsx:605-607 but the line-608 class
swap itself never shipped: the verify branch still read
`space-y-4`. Measured via a fresh CLONE-side registration (the
reference stays read-only — the v46 rule): the verify panel 358×492
@ y 152 (16px SHORT vs the v3-stacking 508), the wrapper 540 (vs
556), and the junction netGap −8 — the centered inner stack's top
(196) sat 8px ABOVE the back button's bottom (204): the button's own
`-mb-2` (−8) OVERRIDES v4's zero-specificity `:where(& >
:not(:last-child))` margin-block-end (16) where the reference's v3
build STACKS them (the collapsed 16 + (−8) = the 8px NET gap) — the
SAME drift the v50 F1 fixed for sign-up/forgot, still live on the
verify state.

**Step 5 — the remediation plan.**
`docs/remediation-plan-v51.md` written and validated against the
codebase (the line-608 site, the existing pins' safety — the
v21/v23/v33 verify pins walk the CONTROLS, never the panel or the
junction; the F2/F3/F4/F5 targets byte-verified in
dashboard-view.tsx / item-card.tsx; the e2e contract — the
deterministic seed, the register-rate-limit budget at 6 calls).

**Step 6 — the TDD cycle.** The F1 RED pin written
(`tests/e2e/verify-email.spec.ts`, a logged-out 390×844 describe
with `registerFreshAccount`): **RED CONFIRMED** against the current
build (the modeCls assertion fails on `space-y-4`). The one-class
fix applied (login-card.tsx:608 `space-y-4` → `zb-auth-mode`, no
`zb-sm6` — the reference's verify container carries no sm tier).
The first GREEN attempt measured the panel 528, not 508 — **THE
EMAIL-LENGTH FINDING**: the "We've sent a 6-digit code to {email}"
block wraps per the address's length (the 38-char throwaway address
wrapped one extra line, +20px) — the pin switched to a FIXED 21-char
email (the global-setup re-seeds db/e2e.db every run, so the address
is reusable) → **GREEN: the panel 508 / the wrapper 556 / the y 144
/ the junction netGap 8** (the button h 20 / mb −8 / the inner top
204). The F2/F4/F5 pins (dashboard.spec.ts) + the F3 pin
(items.spec.ts) written — pin-only, GREEN immediately (one finder
fix: the quick-action circle is a SPAN in the clone, a DIV on the
reference — tag-agnostic). One chain-gate catch: **Playwright does
NOT typecheck** — the `c.querySelector &&` TS2774 always-defined
check ran green at runtime but failed `next build`'s tsc (removed;
the build then green).

**Step 7 — the mutation-sanity series.** Five mutations, each with
the standalone REBUILD before the run bites (the v47–v50 lesson,
pre-applied): (a) the verify container's `zb-auth-mode` removed →
F1 fails (the TDD RED run — the pre-fix proof); (b) the stat card's
`rounded-2xl` → `rounded-xl` → F2 fails (the radius 16 → 12); (c)
the goal card's inline shadow removed → F3 fails; (d) the Needs
tile's inline bg removed → F4 fails (also biting the 1280
tinted-cards pin); (e) the quick-action circle's `w-10 h-10` →
`w-8 h-8` → F5 fails (the circle finder misses at 32). All restored
— the clean diff: login-card.tsx (the one-class fix + its comment)
+ the three spec files + the docs.

**Step 8 — the full chain.** lint ✓ · typecheck ✓ · 108 unit ✓ ·
build ✓ · **241/241 e2e ✓ (5.6m — the not-found spec's flake family:
a different test failed on each of the first two full runs, both
7/7 standalone, clean on the third run)** · 35/35 smoke ✓.

**Step 9 — the VLM pair.** The /savings view at 390 (THE F3
SURFACE): the VLM flagged 3 diffs (the count subtitle / the card
contents / the extra-card layout length) — ALL DOM-verified as the
documented seed-data classes (the reference's 1 Emergency Fund card
vs the clone's 2 richer-seed cards with the 4-chip badge rows; the
chrome byte-pinned by the F3 test) — the v48 precedent's second
application.

**Step 10 — the screenshots + the docs.** The 16 screenshots
regenerated (`capture-screenshots.mjs`). The docs aligned: AGENTS
(the v51 paragraph), CLAUDE (the 241 count + the four inline items),
README (the v51 row), the PAD (v1.1.8), the SKILL doc (the Session
86 row), the probe README (the v51 section), session_119 (this log)
+ session_120 (the raw transcript), the repo worklog (the Session 85
entry + the ledger list).

**Step 11 — the ship.** Commit + push to main via the SSH wrapper
(`docs/ssh_git_wrapper_v3.py` per
`docs/how-to-git-push-using-ssh-wrapper_SKILL.md`).

## The v52 queue (suggestions)

- The reference-side verify-email panel census — needs a sanctioned
  reference registration (a WRITE; the v51 F1's reference contract
  rode the v21-inherited structure + the v50's proven arithmetic).
- The reference-side forgot-CONFIRMATION state census — needs a
  reset-link submit (a WRITE, out of bounds under the v46 rule).
- The /expenses view's full mobile census at 390 (the v47 VLM pair
  walked it; a computed-style census has never been pinned).
- The /income view's mobile census at 390 (the v45 F1a pinned 1280
  only; the v47 VLM flags were all data classes).
- The item-details sheet's 390 reflow (the v48 F1 pinned 1280 only).
