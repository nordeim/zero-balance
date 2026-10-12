# Session 131 — Parity iteration v55: the ICON-GLYPH swap (the piggy-bank / trending-up / search / mail legacy glyphs — THE FIX, the fifth production-code change since v46) + the full-glyph-audit probe family

**Goal:** the session-128 v55 queue's first read-only member (the
goal-card's classification-icon glyph census — the v44 glyph-swap
family's badge-row application), extended to a FULL icon-glyph audit
across the five views + the login page — which found FOUR drifted
glyphs and delivered the first production-code change since the v52
fix. TDD-first (the glyph-parity spec RED before the fix), the
standing checks (49th), the VLM pair (the calculator with-row + the
post-swap goal card), the docs aligned, commit + push via the SSH
wrapper. (The workspace was RE-CLONED this session — the sandbox had
been reset again; the environment rebuilt from scratch.)

## What was done

**Step 0 — the workspace.** `git clone` (the fresh tree at 78a1966 —
the "update session log" commit on top of the v54 parity commit
efe6a0f, adding docs/session_130.md). The five core docs (AGENTS /
CLAUDE / README / PAD / SKILL) + the four session docs (session_129 /
remediation-plan-v54 / the repo worklog / session_130) reviewed; the
v54 state verified: the pin-only diff (16 files — docs/probes/one
spec, zero src/ changes), the 248 e2e, the .env
`file:../db/custom.db` contract with db/ at the repo root
(src/lib/db-path.ts + tests/db-path.test.ts), the sitemap/robots
pair (prerendered at build), the vitest + playwright configs, the
skills/ catalog (the tdd/tailwind-patterns/agent-browser/clone-app
families). The trap-log scan CLEAN (the two `-mb-2` auth back
buttons inside their converted containers). The environment: npm
install, `cp .env.example .env` + the dev AUTH_SECRET, `db:push` +
`db:seed` (db/custom.db at the repo root), `npx playwright install
chromium` (the headless-shell-1243 binary).

**Step 1 — the baseline chain.** lint ✓ · typecheck ✓ · 108/108 unit
✓ · build ✓ (robots + sitemap prerendered) · **248 e2e ✓ (116 + 133,
two ordered chunks, both exit 0, zero failures)** · 35/35 smoke ✓.

**Step 2 — the 49th standing checks.** The reference side: the four
bugs ALL live (the toast-blocker [the burger's center hit eaten by
the fixed z-[100] toast viewport], the sheet-trap [overlayCount 1
after nav], the no-landmark [navLandmark false], the 464 /networth
overflow [docSW 464 > vw 390]), the data census intact ("1 items ·
$25,000" networth / "1 items · $5000.00" income), the SEO pair live.
The clone side: R1 the burger hit-test true + the 5-link sheet opens,
R2 the Income nav closes AND navigates, R3 the nav landmark, R4 zero
overflow at 390 on all five views, the SEO pair 200 — **the mobile
navigation menu VERIFIED WORKING**.

**Step 3 — the v55 sweep.** `ref-v55.sh` + `clone-v55.sh` (the
goal-card glyph census at 390 + the /expenses same-glyph control):
the heart + circle-alert + calendar glyphs byte-identical (the
control census matched by classification text — the reference's
Netflix/Investments/Rent vs the clone's Entertainment/Groceries/Rent)
— but the PIGGY-BANK glyph differs (the reference's OLD 3-path body
vs lucide-react 0.525's redesigned body curve). The scope sweep
(`piggy-sweep-v55.sh`): the reference renders the OLD piggy on EVERY
surface (the nav rail link, the quick-action tile, the stat row, the
donut legend, the savings hero, the classification chip — six
surfaces, all the same 3-path glyph). The FULL audit
(`glyph-audit-v55.sh` + `glyph-diff-v55.mjs`): 24 lucide glyphs —
19 byte-identical, **4 DRIFTED** (piggy-bank, trending-up [the
reference renders TWO POLYLINES — the redesign turned it into
paths], search [the handle 4.3 vs the redesign's 4.34], mail [the
flap a1.94 1.94 vs the redesign's a2 2]), 1 clone-only (repeat — the
Recurring superset badge). The exact markup captured
(`glyph-exact-v55.sh`) — the byte source for the fix. The first
audit run's reference side censused the LOGIN PAGE six times (the
login raced the page mount — the retry + auth-check lesson); the
path-only census read zero paths on circle-alert (the shape-tag
lesson).

**Step 4 — the remediation plan v55** written + validated (the
legacy-icons module design against lucide-react's own Icon.js
rendering rules — the class prefix + the aria-hidden no-a11y-prop
rule; the eight usage files' import blocks; the existing pins' safety
[the svg.lucide-piggy-bank selectors keep matching — the class is
kept]; the e2e contract [the glyph spec's logged-out login describe
uses the auth.spec.ts empty-storageState pattern]).

**Step 5 — the TDD cycle.** The spec written FIRST
(`tests/e2e/glyph-parity.spec.ts`): **RED — 5 failed** (the piggy
chip census, the dashboard piggy + trending, the networth trending,
the search handle, the login mail) + 2 passed (the heart +
circle-alert same-glyph controls — already parity). The fix:
`src/components/ui/legacy-icons.tsx` (four components rendering the
reference's EXACT svg — base attrs + shape children byte-identical,
the `lucide lucide-<name>` class prefix merged with the caller's
className, aria-hidden="true" unless the caller passes an a11y prop
— mirroring lucide's own rules) + the eight import swaps
(item-card / items-view / dashboard-view / item-details-dialog /
budget-item-dialog / sidebar / net-worth-view / login-card; one
`satisfies` typing generalized from `typeof CircleAlertIcon` to the
generic ComponentType). **GREEN — 7 passed** (one LOCK constant
fixed: the rect's rx 2). The SIX pin-sanity mutations, each verified
to FAIL then restored (the piggy body path M19 5→M19 6; the trending
polyline points; the search handle 4.3→4.34 [the redesign value];
the mail flap a1.94→a2 [the redesign value]; ONE usage-site revert
[item-card → the lucide import] — the with-row state alone breaks
the census) — each with the standalone REBUILD as a SEPARATE command
(the v53 lesson).

**Step 6 — the VLM pair.** `vlm-shots-v55.sh` +
`clone-vlmshots-v55.sh` + `vlm-compare-v55.mjs`: PAIR 1 (the
calculator dialog's with-row state — the v53 F2 surface, the
session-128 standing-check suggestion) flagged 4; PAIR 2 (the
savings goal card post-swap) flagged 9. The DOM arbitration
(`vlm-arbit-v55.sh`): the calculator's X-close byte-identical on
every visible layer (29×36, transparent, radius 6, the lucide-x
16×16 — the "square-outlined X" a screenshot-perception artifact;
the zero-width border colors differ [neutral-200 vs the clone's
--color-border] but render nothing); the amounts 24px/700 on both
sites' every card (the "smaller font" a digits-count misread); the
state/content differences (the reference's calculator carries its
own "Contents Insurance" row; the clone's dev seed's Rent has none)
are the documented seed-data classes; the Base44 FAB the platform
chrome. **The pair CLEAN per the v43 rule.**

**Step 7 — the full verification chain.** lint ✓ · typecheck ✓ ·
108/108 unit ✓ · build ✓ · **254 e2e ✓ (122 + 133, two ordered
chunks, both exit 0, zero failures — +6: the glyph-parity suite)**
· 35/35 smoke ✓.

**Step 8 — the deliverables.** The 16 screenshots regenerated — 14
byte-diffs (the production-change invariant, the first non-pin-only
regeneration since v49: every view carrying the four swapped icons
renders the old glyphs now); `.env.example` verified matching the
codebase (the .env was created from it and the whole chain passed);
the v55 probe family persisted (ref-v55.sh + clone-v55.sh +
piggy-sweep-v55.sh + glyph-audit-v55.sh + glyph-exact-v55.sh +
glyph-diff-v55.mjs + the VLM trio + the probe README's v55 section).

**Step 9 — the docs alignment (D1–D8).** AGENTS.md (the v55
paragraph), CLAUDE.md (the 254 count + the icon-glyph family entry),
README (the v55 row + the two count sites), the SKILL doc (the
Session 90 row + the 254 state line), the PAD (the v1.1.12 revision
block + the version header), the probe README (the v55 section with
the four lessons), session_131.md (this formal log) + session_132.md
(the raw transcript), the repo worklog Session 89 + the ledger list,
and the workspace worklog.

**Step 10 — ship.** Conventional Commit + push to main via the SSH
wrapper (docs/ssh_git_wrapper_v3.py per
docs/how-to-git-push-using-ssh-wrapper_SKILL.md), no new branch.

## The v55 queue for v56 (suggestions)

- The reference-side verify/forgot-confirm panel censuses — still
  DEFERRED (both need reference WRITES, out of bounds under the v46
  read-only rule).
- The reference-side calculator EMPTY-state census — the same
  deferred class (a line-item delete).
- The reference's trending-down glyph — data-conditional (renders
  only when its net goes negative); measure opportunistically if the
  reference's data ever flips.
- The reference's line-items dialog glyphs (a line-item CREATE on
  the reference — a write; deferred).
- The remaining audit one-side-classes: the reference's
  router-level icons (any glyphs only IT renders — e.g. its
  Base44 platform chrome, out of parity scope).
- A fresh VLM pair on the v55 F1 surface's desktop 1280 state (the
  donut legend + the stat rows post-swap) as the next standing
  check.
