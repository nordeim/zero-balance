# Session 137 — Parity iteration v57: the items-view desktop 1280 VLM standing pair + the item-card footer/badge-row census (PIN-ONLY — no production-code change; the pin-only line's continuation) + the not-found G7 flake fix (TEST-ONLY)

**Goal:** the session-134 v57 queue's own standing-check suggestion —
a fresh VLM pair on the ITEMS view's desktop 1280 state (the
search-input glyph swap surface + the item-card grid at 1280; the v56
pair covered the dashboard + networth) — plus the 51st standing
checks. The sweep found NO production gap (every VLM flag
DOM-arbitrated to the documented data classes), so the v57
deliverable
is the PIN: the item-card footer + badge-row census (+2 e2e → 257,
three pin-sanity mutations) and ONE test-only fix (the not-found G7
"Go Home" flake — a genuine race, root-caused and killed). (The
workspace was re-cloned TWICE this session — the sandbox reset
mid-conversation; the environment rebuilt from scratch both times.)

## What was done

**Step 0 — the workspace.** `git clone` (the fresh tree at ef18561 —
the "update session log" commit on top of the v56 parity commit
bbb355e). The five core docs (AGENTS / CLAUDE / README / PAD / SKILL)
+ the four session docs (session_135 / remediation-plan-v56 / the
repo worklog / session_136) reviewed; the v56 state verified (the
hero-desk pin, the 255 e2e, the .env `file:../db/custom.db` contract,
the sitemap/robots pair, the vitest + playwright configs, the skills/
catalog). The environment: npm install, `cp .env.example .env` + the
dev AUTH_SECRET, `db:push` + `db:seed` (db/custom.db at the repo
root), `npx playwright install chromium`, agent-browser.

**Step 1 — the baseline chain.** lint ✓ · typecheck ✓ · 108/108 unit
✓ · build ✓ (robots + sitemap prerendered) · **255 e2e ✓ (115 + 141,
two ordered chunks, zero failures)** · 35/35 smoke ✓.

**Step 2 — the 51st standing checks.** The reference side
(`ref-standing-v51.sh`): the four bugs ALL live (the toast-blocker
`hitIsBurgerChild: false`, the sheet-trap via `overlayCount: 1`, the
no-landmark `navLandmark: false`, the 464 /networth overflow), the
data census intact ("1 items · $25,000" networth / "1 items ·
$5000.00" income — no trending-down opportunity), the SEO pair live.
The clone side (`standing-checks-v51.sh`): R1 the burger hit-test
true + the sheet opens, R2 the Income nav closes AND navigates, R3
the nav landmark, R4 zero overflow at 390 on all five views, the SEO
pair live — **the mobile navigation menu VERIFIED WORKING (the 51st
time)**.

**Step 3 — the v57 sweep.** The desktop 1280x800 VLM pair
(`vlm-shots-v57.sh` + `clone-vlmshots-v57.sh` +
`vlm-compare-v57.mjs`): PAIR 1 the income view, PAIR 2 the expenses
view. Every flag DOM-arbitrated (`vlm-arbit-v57.sh` + the
badge-census pair, the v43 rule): (1) the avatar — the
user-identity data class; (2) the header subtitle + the card
counts/names/amounts/dates — the seed-data class; (3) the
expense-card footer's payment chips — **DATA-CONDITIONAL: the footer
row's chrome is byte-identical on both sites** (flex justify-between
12px rgb(107,114,128) h 16; each span flex gap 4px with the 12×12
gray icon) — the reference's own income card renders the SAME
two-child structure (the date + "Bank Account") while its expense
items carry no payment methods; the clone's items carry them; (4)
the badge wrap — **DATA-CONDITIONAL: the badge row's chrome is
byte-identical** (flex wrap, 8px gap, 12px mb; every badge flex
center / 6px radius / 2px 10px pad / 12px/600 / h 22 / 12×12 icons)
— the clone's Recurring superset badge (the 4th badge) wraps the row
to h 52 (22 + 8 + 22); (5) the classification badge colors — the
data class already locked by badge-colors.spec.ts. **The pair
CLEAN.** The grid census: the 960px 3-column grid (each column
≈309.33px) with the 16px gap + the card chrome (309 / 20px / 12px /
1px solid rgb(229,231,227) / white) — the v45 F1a pin's own values.

**Step 4 — the pin.** The "items card footer + badge census at 1280
(v57 — plan F1)" describe in `tests/e2e/items.spec.ts` (+2): F1a the
/income card's footer two-children conditional render (the date span
+ the PayPal chip) + the badge chrome (flex/center/6px/2px
10px/12px/600/h 22; [want, monthly, active]); F1b the /expenses grid
census (960 / 3 children / 16px gap / the 3-col template) + the
wrapped 4-badge row (h 52, [want, monthly, Recurring, active]) + the
payment-chip footer. GREEN on the first run (the pin-only
iteration's own expectation — the surface is already correct).

**Step 5 — the pin-sanity mutations.** THREE mutations verified to
FAIL then restored: (a) the footer `text-xs` → `text-sm` (12px →
14px — the F1a footer fs assertion, h 16 → 20); (b) the badge row
`gap-2` → `gap-4` (8px → 16px — the F1a badgeRow gap); (c) the
first badge `px-2.5` → `px-2` ("2px 10px" → "2px 8px" — the F1a
badge pad loop). Each with the standalone REBUILD as a SEPARATE
command; `git diff src/` empty after the restores.

**Step 6 — the flake fix (TEST-ONLY).** The full-chain re-run
surfaced the not-found G7 "Go Home navigates to the dashboard" flake
(three chunk-run failures in one session, two different tests).
The root-cause probe (`--repeat-each=8` in isolation) reproduced it
at ~1-in-8 on an IDLE machine — NOT load. The cause: the file-wide
logged-out opt-out (not-found.spec.ts line 15) applied to a test
that asserts an AUTHENTICATED surface — logged-out, the "Budget
Dashboard" heading only exists in the ~50-180ms window between the
page boot and the RequireSession /login redirect (the trace:
/api/auth/me at .137, the /login?from_url client-nav at .187). The
fix: the test moves into its own describe carrying a describe-scoped
storageState override (`tests/e2e/.auth/user.json` — the same
AUTH_STATE the chromium project uses; describe-scope beats
file-scope), the header comment documents the exception. Verified:
`--repeat-each=10` → 21/21 (the pre-fix rate ~1-in-8), the full spec
7/7, the whole chunk 2 green (143).

**Step 7 — the full chain + the screenshots.** lint + typecheck +
108/108 unit + build + **257 e2e (115 + 143, two ordered chunks,
zero failures)** + 35/35 smoke. The 16 screenshots regenerated —
**ALL BYTE-IDENTICAL to HEAD** (the pin-only invariant; `git diff
src/` empty, zero timing drift this run).

**Step 8 — the docs.** AGENTS.md (the v57 paragraph), CLAUDE.md (the
257 count + the v57 family entry), README.md (the counts + the v57
row), the SKILL doc (the Session 92 row + the state line), the PAD
(v1.1.14 + the revision block), the probe README (the v57 section +
the lessons), the repo worklog (the Session 91 entry + the ledger
list), this formal log (session_137.md).

**Step 9 — ship.** Conventional Commit + push to main via the SSH
wrapper (docs/ssh_git_wrapper_v3.py per
docs/how-to-git-push-using-ssh-wrapper_SKILL.md), no new branch.

## The v57 probe family (P1 — persisted)

vlm-shots-v57.sh + clone-vlmshots-v57.sh + vlm-compare-v57.mjs (the
desktop 1280 pair), vlm-arbit-v57.sh (the DOM arbitration + the
reference-side census), badge-census-ref-v57.sh +
badge-census-clone-v57.sh + badge-census-clone-v57-debug.sh (the
badge-row chrome census, both sides — the debug variant carries the
heredoc-quoting fix), ref-standing-v51.sh + standing-checks-v51.sh
(the 51st standing checks).

## The v58 queue for v58 (suggestions)

- The SAVINGS view's desktop 1280 VLM pair (the items family's
  remaining view — income + expenses are now covered by the v57
  pair; the savings goal-card's 1280 state is unpinned at the exact
  pair viewport, its internals pinned at 390 only [v54 F1]).
- The CALCULATOR view's desktop 1280 VLM pair (the panel + row
  surfaces — the v45/v49 pins cover 1280/640 chrome, no VLM pair).
- The reference-side write-dependent censuses — still DEFERRED (all
  need reference WRITES, out of bounds under the v46 read-only
  rule): the verify-email panel census, the forgot-confirm state,
  the calculator EMPTY state, the line-items dialog glyphs.
- The reference's trending-down glyph — still data-conditional (its
  net is positive; the 51st data census confirms "1 items · $25,000"
  unchanged).
