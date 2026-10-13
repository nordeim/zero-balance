# Session 139 — Parity iteration v58: the savings-view desktop 1280 VLM standing pair + the savings goal-card's footer/badge census (PIN-ONLY — no production-code change; the pin-only line's continuation)

**Goal:** the session-137 v58 queue's own first suggestion — the
SAVINGS view's desktop 1280 VLM pair (the items family's remaining
view; the v57 pair covered income + expenses; the savings goal-card's
1280 state was unpinned at the pair viewport, its internals pinned at
390 only [v54 F1]) — plus the 52nd standing checks. The sweep found
NO production gap (every VLM flag DOM-arbitrated to the documented
data classes), so the v58 deliverable is the PIN: the savings
goal-card's footer + badge census (+1 e2e → 258, three pin-sanity
mutations — the third on the fresh VERTICAL-pad axis proving the wrap
arithmetic). (The workspace was re-cloned this session — the sandbox
had reset again; the environment rebuilt from scratch.)

## What was done

**Step 0 — the workspace.** `git clone` (the fresh tree at e5553df —
the "update session log" commit on top of the v57 parity commit
c4c38aa). The five core docs (AGENTS / CLAUDE / README / PAD / SKILL)
+ the four session docs (session_137 / remediation-plan-v57 / the
repo worklog / session_138) reviewed; the v57 state verified (the
items-view pins in items.spec.ts, the not-found G7 describe-scoped
storageState fix, the 257 e2e, the .env `file:../db/custom.db`
contract, the sitemap/robots pair, the skills/ catalog). The
environment: npm install, `cp .env.example .env` + the dev
AUTH_SECRET, `db:push` + `db:seed` (db/custom.db at the repo root),
`npx playwright install chromium`, agent-browser.

**Step 1 — the baseline chain.** lint ✓ · typecheck ✓ · 108/108 unit
✓ · build ✓ (robots + sitemap prerendered) · **257 e2e ✓ (104 + 138 +
14, three ordered chunks this session — the chunk-regex lesson below,
zero failures)** · 35/35 smoke ✓.

**Step 2 — the 52nd standing checks.** The reference side
(`ref-standing-v52.sh`): the four bugs ALL live (the toast-blocker
`hitIsBurgerChild: false`, the sheet-trap via `overlayCount: 1`, the
no-landmark `navLandmark: false`, the 464 /networth overflow), the
data census intact ("1 items · $25,000" networth / "1 items ·
$5000.00" income — no trending-down opportunity), the SEO pair live.
The clone side (`standing-checks-v52.sh`): R1 the burger hit-test
true + the sheet opens, R2 the Income nav closes AND navigates, R3
the nav landmark, R4 zero overflow at 390 on all five views, the SEO
pair live — **the mobile navigation menu VERIFIED WORKING (the 52nd
time)**.

**Step 3 — the v58 sweep.** The desktop 1280x800 VLM pair
(`vlm-shots-v58.sh` + `clone-vlmshots-v58.sh` +
`vlm-compare-v58.mjs`): the savings view. Every flag DOM-arbitrated
(`savings-census-ref-v58.sh` + `savings-census-clone-v58.sh`, the
v43 rule): (1) the header stats + the card names/amounts/dates — the
seed-data class (the reference's own 1-item savings view ["1 items ·
$1000.00", "Emergency Fund" $1000, "Home Savings"] vs the clone's
dev seed ["2 items · $1250.00", Investments $450 + Emergency Fund
$800]); (2) the savings card's footer content — **DATA-CONDITIONAL:
the footer row's chrome is byte-identical on both sites** (flex
justify-between 12px rgb(107,114,128) h 16; each span flex gap 4px
with the 12×12 gray icon) — the reference's own savings item carries
NO paymentMethod so its footer renders ONE child (the date alone,
"Oct 7, 2026" + the 12×12 calendar icon) while the clone's items
carry them (the date + "Brokerage" with the 12×12 credit-card icon)
— the v57 conditional-footer contract measured on the third view;
(3) the badge family — **DATA-CONDITIONAL: the badge-row chrome is
byte-identical** (flex wrap, 8px gap, 12px mb; every badge flex
center / 6px radius / 2px 10px pad / 12px/600 / h 22 / the 12×12
icons) — the reference's savings item is classified "need" (the red
family: bg rgb(254,242,242) + 1px solid rgb(254,202,202) — the
badge-colors.spec.ts need map) while the clone's are "savings" (the
green family: bg rgb(240,253,244) + 1px solid rgb(187,247,208) — the
savings map): the classification VALUE is the data class, the color
maps stay locked by badge-colors.spec.ts; the monthly (purple-50)
+ active (slate-50) badges are byte-identical both sides; the
clone's Recurring superset badge (the 4th) wraps the row to h 52
(22 + 8 + 22) — the reference's 3-badge row stays h 22 (the
documented wrap class). (4) the grid — 960/16px gap/the 3-column
template each ≈309.33px (the reference's own 1 savings card vs the
clone's 2 — the seed class; the card chrome 309 / 20px / 12px /
1px solid rgb(229,231,227) / white — the v45 F1a pin's own values).
**The pair CLEAN.**

**Step 4 — the pin.** The "the savings goal-card census at 1280
(v58 — plan F1)" describe in `tests/e2e/items.spec.ts` (+1): the
/savings grid (960 / 2 children / 16px gap / the 3-col template),
the Investments card's two-children conditional footer (the date
span + the "Brokerage" chip), the wrapped 4-badge row (h 52,
[savings, monthly, Recurring, active]) + every badge's geometry
(flex/center/6px/2px 10px/12px/600/h 22; the classification
badge's icon 12×12) + the card chrome control (the v45 values).
GREEN on the first run (the pin-only iteration's own expectation —
the surface is already correct).

**Step 5 — the pin-sanity mutations.** THREE mutations verified to
FAIL then restored: (a) the footer `text-xs` → `text-sm` (12px →
14px — the F1 footer fs assertion, h 16 → 20); (b) the badge row
`gap-2` → `gap-4` (8px → 16px — the F1 badgeRow gap); (c) the
classification badge `py-0.5` → `py-1` ("2px 10px" → "4px 10px" —
the F1 badge pad loop, the badge h 22 → 26, AND the wrapped row's
h 52 → 60 — the fresh VERTICAL-pad axis proving the wrap ARITHMETIC
(22 + 8 + 22), the v57 S1(c) having mutated the same line's
HORIZONTAL pad). Each with the standalone REBUILD as a SEPARATE
command; `git diff src/` empty after the restores. (Each mutation
also bit the v57/v54 footer+badge pins — the correct shared-line
signature, 4 failures per mutation.)

**Step 6 — the full chain + the screenshots.** lint + typecheck +
108/108 unit + build + **258 e2e (78 + 38 + 144, three ordered
chunks, zero failures — 257 + the v58 pin)** + 35/35 smoke. The 16
screenshots regenerated — **ALL BYTE-IDENTICAL to HEAD** (the
pin-only invariant; `git diff src/` empty, zero timing drift this
run).

**Step 7 — the docs.** AGENTS.md (the v58 paragraph), CLAUDE.md (the
258 count + the v58 family entry), README.md (the counts + the v58
row), the SKILL doc (the Session 93 row + the state line), the PAD
(v1.1.15 + the revision block), the probe README (the v58 section +
the lessons), the repo worklog (the Session 92 entry + the ledger
list), this formal log (session_139.md).

**Step 8 — ship.** Conventional Commit + push to main via the SSH
wrapper (docs/ssh_git_wrapper_v3.py per
docs/how-to-git-push-using-ssh-wrapper_SKILL.md), no new branch.

## The v58 probe family (P1 — persisted)

vlm-shots-v58.sh + clone-vlmshots-v58.sh + vlm-compare-v58.mjs (the
savings view's desktop 1280 pair), savings-census-ref-v58.sh +
savings-census-clone-v58.sh (the DOM arbitration + the full census,
both sides — the clone script carries the P1.2 quoted-heredoc fix by
construction), ref-standing-v52.sh + standing-checks-v52.sh (the
52nd standing checks).

## The v59 queue for v59 (suggestions)

- The CALCULATOR view's desktop 1280 VLM pair (the panel + row
  surfaces — the v45/v49 pins cover 1280/640 chrome, no VLM pair).
- The LOGIN view's desktop 1280 pair (the v55 glyph pin's own
  surface — no pair at 1280 yet).
- The reference-side write-dependent censuses — still DEFERRED (all
  need reference WRITES, out of bounds under the v46 read-only
  rule): the verify-email panel census, the forgot-confirm state,
  the calculator EMPTY state, the line-items dialog glyphs.
- The reference's trending-down glyph — still data-conditional (its
  net is positive; the 52nd data census confirms "1 items · $25,000"
  unchanged).
