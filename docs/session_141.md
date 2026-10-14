# Session 141 — Parity iteration v59: the calculator-view desktop 1280 VLM standing pair + the calculator panel/total-card census (PIN-ONLY — no production-code change; the pin-only line's continuation)

**Goal:** the session-139 v59 queue's first TWO suggestions — the
CALCULATOR dialog's desktop 1280x800 VLM pair (the panel + row
surfaces; the v45 F2a pin covered the panelW + row census at 1280, the
v49 F3 panel chrome at 640 only) and the LOGIN view's 1280 pair (the
v55 glyph pin's surface, no pair at 1280 yet) — plus the 53rd standing
checks. The sweep found NO production gap (every VLM flag
DOM-arbitrated to the documented classes), so the v59 deliverable is
the PIN: the calculator panel + total-card census at 1280 (+1 e2e →
259, three pin-sanity mutations). (The workspace was re-cloned this
session — the sandbox had reset again; the environment rebuilt from
scratch.)

## What was done

**Step 0 — the workspace.** `git clone` (the fresh tree at 5585eff —
the session-log commit on top of the v58 parity commit 8769dc8). The
five core docs (AGENTS / CLAUDE / README / PAD / SKILL) + the four
session docs (session_139 / remediation-plan-v58 / the repo worklog /
session_140) reviewed; the v58 state verified (the savings-view pins
in items.spec.ts, the 258 e2e, the .env `file:../db/custom.db`
contract, the sitemap/robots pair, the skills/ catalog, the scandihaven
tech-stack reference). The environment: npm install, `cp .env.example
.env` + a fresh dev AUTH_SECRET, `db:push` + `db:seed` (db/custom.db
at the repo root), `npx playwright install chromium`, agent-browser
0.39.0.

**Step 1 — the baseline chain.** lint ✓ · typecheck ✓ · 108/108 unit
✓ · build ✓ (robots + sitemap prerendered) · **258 e2e ✓ (89 + 94 +
76, three ordered chunks, zero failures)** · 35/35 smoke ✓.

**Step 2 — the 53rd standing checks.** The reference side
(`ref-standing-v53.sh`): the four bugs ALL live (the toast-blocker
`hitIsBurgerChild: false`, the sheet-trap via `overlayCount: 1`, the
no-landmark `navLandmark: false`, the 464 /networth overflow), the
data census intact ("1 items · $25,000" networth / "1 items ·
$5000.00" income + this session's expenses census "4 items ·
$525.00"), the SEO pair live. The clone side (`standing-checks-v53.sh`):
R1 the burger hit-test true + the sheet opens, R2 the Income nav
closes AND navigates, R3 the nav landmark, R4 zero overflow at 390 on
all five views, the SEO pair live — **the mobile navigation menu
VERIFIED WORKING (the 53rd time)**.

**Step 3 — the v59 sweep, item 1: the calculator pair.** The desktop
1280x800 VLM pair (`vlm-shots-v59.sh` + `clone-vlmshots-v59.sh` +
`vlm-compare-v59.mjs`): the reference's own Rent calculator (its Rent
$25.00 carries ONE "Contents Insurance" $25.00 monthly-active line
item — its own data) vs the clone's (the SAME line item added through
the real UI for the apples-to-apples pair state, then FULLY restored:
delete + the $1850 edit-flow restore + the "3 items · $2235.00" page
total verified). Every flag DOM-arbitrated (`calc-census-ref-v59.sh` +
`calc-census-clone-v59.sh`, the v43 rule): (1) the total card's "•
Will update category total" span — DATA-CONDITIONAL (the
lineTotal-vs-parentAmount-at-open contract: the reference's 25 === 25
→ hidden, the clone's 25 !== 1850 → shown; the conditional is the
pinned contract); (2) the row's hover-action pair — POINTER-POSITION
artifact (both sites gate it at opacity 0 at rest — the reference's
shot caught it mid-hover). The census byte-identical on every axis:
the panel 768×393 @ (256,204) — the centering invariant round((800−
393)/2) — radius 16 / maxW 768px / maxH 680px (85vh of 800) / bg white
/ overflow hidden / the 2xl VISIBLE layer; the total card 720×90 /
#fff7f5 / radius 12 / pad 16 / border 1px solid rgb(252,221,213); the
close 36×36; the header border-b 1px solid rgb(229,231,227); the row
720 / pad 16 / radius 12 / border / transition all 0.15s (the v45 F2a
values re-confirmed live). **The pair CLEAN.**

**Step 4 — the v59 sweep, item 2: the login pair.** The desktop
1280x800 VLM pair (`login-shots-v59.sh` + `clone-login-shots-v59.sh`):
**IDENTICAL** — the VLM found zero layout/style differences (the card,
logo, fonts, colors, inputs, the dark navy button, the OR divider);
the only flag the reference's "Edit with Base44" platform badge (the
documented platform-chrome class). The census matches exactly (title /
h1 / inputs / the Sign-in button 368×48).

**Step 5 — the pin.** The "calculator panel census at 1280 (v59 —
plan F1)" describe in `tests/e2e/calculator.spec.ts` (+1): the
read-only open state — the panel chrome (768 / radius 16 / maxW 768px
/ maxH 680px / white / hidden / the 2xl VISIBLE layer) + the
centering invariant (y = round((800−h)/2)) + the 36×36 close + the
header border-b + the total card (720 / #fff7f5 / radius 12 / pad 16
/ border — the v53 F2 chrome at the pair viewport) + the panelW 768
control. GREEN on the first run (the pin-only iteration's own
expectation).

**Step 6 — the pin-sanity mutations.** THREE mutations verified to
FAIL then restored: (a) the total card `backgroundColor: "#fff7f5"` →
`"#fff8f0"` (the F1 totalCard assertion — the census finder returned
null for the mutated color); (b) the panel `maxWidth: "48rem"` →
`"42rem"` (the F1 panel w/maxW assertions — 768 → 672); (c) the total
card `p-4` → `p-5` (the F1 totalCard pad — 16px → 20px). Each with the
standalone REBUILD as a SEPARATE command; `git diff src/` empty after
the restores.

**Step 7 — the full chain + the screenshots.** lint + typecheck +
108/108 unit + build + **259 e2e (90 + 94 + 76, three ordered chunks,
zero failures — 258 + the v59 pin)** + 35/35 smoke. The 16 screenshots
regenerated — **9 byte-identical + 7 diff the SEED-DATE class** (the
seed's `isoDate(-N)` anchors the item dates to the seed-run date; the
fresh checkout seeded a day after v58's capture — VLM-arbitrated
DATE-TEXT-only [Oct 4→5, Oct 10→11, Oct 11→12 on the expense cards],
zero layout/style diffs; the e2e DB re-seeds every run so the suite is
date-independent; `git diff src/` empty — the pin-only invariant
holds on the code).

**Step 8 — the docs.** AGENTS.md (the v59 paragraph), CLAUDE.md (the
259 count + the v59 family entry), README.md (the counts + the v59
row), the SKILL doc (the Session 94 row + the state line), the PAD
(v1.1.16 + the revision block), the probe README (the v59 section +
the lessons), the repo worklog (the Session 93 entry + the ledger
list), this formal log (session_141.md).

**Step 9 — ship.** Conventional Commit + push to main via the SSH
wrapper (docs/ssh_git_wrapper_v3.py per
docs/how-to-git-push-using-ssh-wrapper_SKILL.md), no new branch.

## The v59 probe family (P1 — persisted)

vlm-shots-v59.sh + clone-vlmshots-v59.sh + vlm-compare-v59.mjs (the
calculator pair), login-shots-v59.sh + clone-login-shots-v59.sh (the
login pair), calc-census-ref-v59.sh + calc-census-clone-v59.sh (the
DOM arbitration + the full 1280 census, both sides),
ref-standing-v53.sh + standing-checks-v53.sh (the 53rd standing
checks), vlm-shotsdiff-v59.mjs (the screenshot seed-date arbitration),
+ the debug-calc-v59.sh trio (the mouse-click debugging trail — the
P1 lesson's own evidence).

## The v60 queue for v60 (suggestions)

- The NETWORTH view's desktop 1280 VLM pair (the v52-era pins cover
  the 390/640 chrome; the v56 pair covered the dashboard, the v57/58
  pairs the items family — networth is the remaining major view with
  no 1280 pair).
- The DASHBOARD's drill-down dialog surfaces at 1280 (the v43/v44
  pins cover the drill-down chrome at 640; the 1280 surfaces unpinned
  at the pair viewport).
- The reference-side write-dependent censuses — still DEFERRED (all
  need reference WRITES, out of bounds under the v46 read-only rule):
  the verify-email panel census, the forgot-confirm state, the
  calculator EMPTY state (the reference's Rent carries a line item —
  an empty state would need a reference delete), the line-items dialog
  glyphs.
- The reference's trending-down glyph — still data-conditional (its
  net is positive; the 53rd data census confirms "1 items · $25,000"
  unchanged).
