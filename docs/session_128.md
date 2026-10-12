# Session 128 — Parity iteration v54: the savings goal-card's badge-row + footer internals at 390 (PIN-ONLY — the third consecutive pin-only iteration) + the footer-locator/blockification probe lessons (2026-10-12)

**Goal:** the session-125 v54 queue's first read-only member — the
savings view's GOAL-CARD INTERNALS census at 390 (the badge chip row
+ the date/payment footer — the internals BEYOND the v51 F3 chrome
pin, which walked the card's outer chrome + the h4/sub/amount
typography but never the badge row or the footer) + the queue's
standing-check suggestion (a fresh VLM pair on the /networth
tablist). TDD-first, docs aligned, commit + push via the SSH wrapper.
(The workspace was RE-CLONED this session — the sandbox had been
reset again, so `git clone` replaced the empty tree; the environment
rebuilt from scratch.)

## What was done

**Step 0 — the workspace.** `git clone` (the fresh tree at 664cfd7 —
the "update session log" commit on top of the v53 parity commit
a6ab17e, adding docs/session_127.md). The five core docs (AGENTS /
CLAUDE / README / PAD / SKILL) + the four session docs (session_126 /
remediation-plan-v53 / the repo worklog / session_127) reviewed; the
v53 state verified: the pin-only diff (the two spec files + the probe
family), the 247 e2e, the .env `file:../db/custom.db` contract with
db/ at the repo root (src/lib/db-path.ts + tests/db-path.test.ts),
the sitemap/robots pair (src/app/sitemap.ts + src/app/robots.ts,
prerendered at build), the vitest + playwright configs, the skills/
catalog (the trap-log, probe, and TDD families). The environment:
npm install, `cp .env.example .env` + the dev AUTH_SECRET,
`db:push` + `db:seed` (7 budget items, 3 assets, 2 liabilities —
db/custom.db at the repo root).

**Step 1 — the baseline chain.** lint ✓ · typecheck ✓ · 108/108 unit
✓ · build ✓ (robots + sitemap prerendered) · **248 e2e ✓ (the 247
chromium count: 140 + 108, two ordered chunks, both exit 0, zero
failures — the 10-minute Bash-timeout discipline; the first run
failed 21-wide on `browserType.launch: Executable doesn't exist` —
the fresh-clone environment lacked the headless-shell-1243 binary;
`npx playwright install chromium` fixed it)** · 35/35 smoke ✓. npm
audit = 0 production vulnerabilities; `.env` ≡ `.env.example`
(modulo the dev AUTH_SECRET value). No orphaned servers on
:3100/:3200/:3199 (the v53 lesson's `ss -tlnp` check, pre-applied).

**Step 2 — the 48th standing checks.** Reference side
(`ref-standing-v49.sh`, re-run verbatim): all four bugs live — the
toast-blocker (the burger's center hit eaten by the fixed z-[100]
toast viewport div, hitIsBurgerChild false), the sheet-trap
(overlayCount 1 after the Income nav click), the no-landmark
(navLandmark false), the 464 /networth overflow (docSW 464 > vw 390)
— the superset preserved. The data census read-only and intact
("1 items · $25,000" networth / "1 items · $5000.00" income); the
SEO pair live (robots.txt + sitemap.xml). Clone side
(`standing-checks-v49.sh` via with-server on :3200): R1 the burger
hit-test true + the 5-link sheet opens, R2 the Income nav closes the
sheet AND navigates (sheetGone + overlayGone), R3 navLandmark true,
R4 zero overflow at 390 on all five views (docSW 390 — vs the
reference's 464), the SEO pair live — **the mobile navigation menu
verified working as expected**.

**Step 3 — the code audit.** The trap-log scan CLEAN: only two
`-mb-2` utilities live in src/ — both the auth back buttons
(login-card.tsx:617 + :714), both inside their converted
`zb-auth-mode` containers (the v50 + v51 fixes; the globals.css
rules verified). The v53 diff verified pin-only (the two spec files
+ the probe family + the docs — zero production changes since 03fdfc6
's subcategory fix). The sitemap/robots/vitest/playwright configs
in place; `.env.example` matching the codebase (the db-path
contract).

**Step 4 — the v54 sweep.** `ref-v54.sh` + `clone-v54.sh` (READ-ONLY
on the reference — the passive census family): the savings view's
goal-card internals at 390×844 on both sites. The FIRST reference
run mis-read the footer (the generic justify-between + svg finder
matched the card's HEADER row first — its 16px/48px geometry and an
empty kebab read as the "footer"/"payment span"; the fs-16/h-48
signature is the tell-tale) — the footer locator fixed to "the LAST
justify-between direct child WITHOUT an h4", both drivers re-run.
**BYTE-PARITY on every chrome axis — PIN-ONLY (the third consecutive
pin-only iteration):** the header row (flex/gap 8/mb 4/center), the
dot (8×8/9999/rgb(59,126,161) — the savings TYPE accent on BOTH
sites; the reference colors its dot by TYPE, not classification, its
need-classified goal still carries the teal savings dot), the badge
row (flex/wrap/gap 8/mb 12), every chip (h 22/radius 6/pad 2px
10px/12/600 with the 12×12 icons at mr 4 — the "monthly" chip w 78
and the "active" chip w 63 on BOTH sites, the byte-parity width
proof), the footer (flex/space-between/12/rgb(107,114,128)/h 16),
the date span (flex/gap 4/12 with the 12×12 calendar icon at gray).
The divergences are all documented DATA classes: the chip COUNT (the
reference's 3 vs the seed's 4 — the Recurring chip), the row HEIGHT
(22 vs 52, the wrap), the payment span (the reference's goal carries
none), the card height (200 vs 230).

**Step 5 — the remediation plan v54.**
`docs/remediation-plan-v54.md` written (the F1 pin + the F2 VLM pair
+ the S1 five-mutation sanity + the P1 probe infra + the D1–D8 docs
alignment + the ToDo list) and validated against the codebase (the
item-card.tsx source lines for every pin axis; the existing pins'
safety — the v51 F3, v8 G2, v45 F1, v52 F2/F3 describes all run at
their own scopes; the e2e contract — the seeded Emergency Fund walk).

**Step 6 — the TDD cycle.** F1 written (the new describe
"savings goal-card internals census at 390 (v54 — plan F1)" in
items.spec.ts). The FIRST run FAILED — the census returned null: the
badge-row finder required the chips' computed display to be
"inline-flex" but the chips compute to "flex" (flex items are
blockified per the CSS spec — the probe's OR-clause lesson
re-learned the hard way). The finder fixed to accept "flex"; GREEN.
The S1 mutation series (each with the standalone REBUILD as a
SEPARATE command — the v53 lesson): (a) the badge row's gap-2 →
gap-4 → FAILS (the row gap 8 → 16); (b) the chip's px-2.5 → px-1.5
→ FAILS (the pad 2px 10px → 2px 6px); (c) the chip's text-xs →
text-sm → FAILS (the h 22 → 26); (d) the footer's text-xs → text-sm
→ FAILS; (e) the date span's gap-1 → gap-2 → FAILS (the gap 4 → 8).
All restored — the clean diff: ONE spec file, 214 insertions, ZERO
production changes.

**Step 7 — the VLM pair (F2).** `vlm-shots-v54.sh` +
`clone-vlmshots-v54.sh` + `vlm-compare-v54.mjs`: the /networth
tablist at 390 (the v53 F1 surface — the queue's standing-check
suggestion) AND the savings goal card (THE F1 surface). PAIR 1
flagged 5 diffs — every one DOM-verified: the data values (the
documented data class), the summary-card trend icon (the reference's
32×32 trending-up clips at its 464-overflow page's right edge, x 368
+ 32 > 390, where the clone's sits fully in-bounds at x 294 — the
documented width-divergence class), the active tab bg (byte-identical
rgb(220,252,231) on both sites — a screenshot-perception artifact),
the Add button text (the full "Add Asset" on both sites, scrollW 134
= clientW 134, no truncation — a small-text misread), the Base44 FAB
(the platform chrome). PAIR 2 flagged the seed-data classes only
(the count, the classification badges, the Recurring chip, the
payment span, the second card, the dates). **The pair CLEAN per the
v43 rule.**

**Step 8 — the full verification chain.** lint ✓ · typecheck ✓ ·
108/108 unit ✓ · build ✓ · **248 e2e ✓ (248 chromium: 141 + 108, two
ordered chunks, both exit 0, zero failures)** · 35/35 smoke ✓.

**Step 9 — the deliverables.** The 16 screenshots regenerated (ZERO
byte-diffs — the pin-only invariant, verified by git status);
`.env.example` verified matching the codebase (unchanged — the
db-path contract already correct); the probe family persisted
(ref-v54.sh + clone-v54.sh + vlm-shots-v54.sh + clone-vlmshots-v54.sh
+ vlm-compare-v54.mjs + the probe README's v54 section).

**Step 10 — the docs alignment (D1–D8).** AGENTS.md (the v54
paragraph), CLAUDE.md (the 248 count + the items-family extension),
README (the v54 row + the two count sites), the SKILL doc (the
Session 89 row + the 248 state line), the PAD (the v1.1.11 revision
block + the version header), the probe README (the v54 section with
the four lessons), session_128.md (this formal log) + session_129.md
(the raw transcript), the repo worklog Session 88 + the ledger list,
and the workspace worklog.

**Step 11 — ship.** Conventional Commit + push to main via the SSH
wrapper (docs/ssh_git_wrapper_v3.py per
docs/how-to-git-push-using-ssh-wrapper_SKILL.md), no new branch.

## The v54 queue for v55 (suggestions)

- The reference-side verify/forgot-confirm panel censuses — still
  DEFERRED (both need reference WRITES, out of bounds under the v46
  read-only rule).
- The reference-side calculator EMPTY-state census — the same
  deferred class (a line-item delete).
- The remaining un-censused mobile surfaces: the goal-card's
  classification-icon glyph census (the 12×12 lucide shapes at the
  chip colors — the v44 glyph-swap family's badge-row application),
  the a11y mobile sheet's post-v39 surfaces, or a fresh VLM pair on
  the calculator dialog's with-row state (the v53 F2 surface) as the
  next standing check.
