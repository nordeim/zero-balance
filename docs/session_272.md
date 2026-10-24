The workspace was reset — the repo needed a fresh clone. Cloned at main @
9a78446 (the v110 cycle shipped + its session logs [session_270 +
session_271]), re-establishing the full context from the v110 delivery
records + `docs/remediation-plan-v110.md` + the worklog Session 145 entry.

The queue is clear: **v111 targets the v105-era LOGIN + CALCULATOR pair**
(the probe README's v111 queue agreeing with the rotation ledger — the
LOGIN view + the CALCULATOR dialog at desktop 1280x800, the pair's EIGHTH
re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111]). The
v105 probe header verified before anything derived (the queue-prose
verification lesson): the login + calculator surfaces + the SEVENTH
bracket [v99 → v105] confirmed. Environment provisioning started while
studying the derivation patterns.

npm install completed in 15s — **the zod extraction INTACT** (840/840
files, the v4/ subdirectory present — no npm ci needed). next 16.4.3 +
zod 4.6.7 confirmed installed — **the v110 security bump holds**. `.env`
written (DATABASE_URL="file:../db/custom.db"), db/ seeded (db:generate +
db:push + db:seed), **seedcheck EXACT** (7 / 1850 / 2235 / 0 / 3 / 2 —
the env -u DATABASE_URL discipline: the parent shell's polluted absolute
URL re-confirmed live). The post-push commit audit clean (fe528fa +
9a78446 session-log-only — session_270.md + session_271.md, zero src/ or
lockfile deltas).

**THE PROVISIONING MISS (caught and fixed before any conclusion):** the
fresh sandbox's playwright cache held only v1200-era binaries
(chromium-1200 + chromium_headless_shell-1200 — an older pin's
leftovers). The `npx playwright install chromium --dry-run` check
REPORTED the v1243 install location without verifying the binaries
exist; the first e2e chunk then failed 74/75 with "Executable doesn't
exist at .../chromium_headless_shell-1243" (the suite's default headless
mode runs the headless-SHELL binary, not the full chromium). The fix: the
FULL `npx playwright install chromium` — downloading BOTH binaries
(chromium-1243 114.3MiB + chromium_headless_shell-1243). All subsequent
runs green on the first re-run. **THE CHECKLIST RULE: verify the cache
DIRECTLY (`ls /home/z/.cache/ms-playwright/` for BOTH entries) — the
dry-run's "Install location:" line is a location REPORT, never an
existence proof.**

**F0 baseline FULLY GREEN** — lint · typecheck · 108/108 unit · build
(robots + sitemap prerendered) · **313 e2e** (75+80+79+60+23 = 317
executions across the disjoint chunk splits — the a11y file initially
dropped from chunk 4 by a filename-parsing artifact [the "y.spec.ts"
grep miss on "a11y"], caught because 60 ≠ 82, re-run as its own chunk;
zero flakes) · 35/35 smoke. The count derived authoritatively via
--list [313 in 24 files] before any chunk ran.

**F0b the npm-audit watch (the standing step's second cycle): 0
vulnerabilities** — the v110 bump's end-state verified holding (next
16.4.3 + zod 4.6.7, both within the existing caret ranges, package.json
untouched). No new advisories; no action required.

**F1: NO DRIFT** ✓ (npm-latest 4.14.0; only rc/next sha prereleases
beyond; wrapper+engine 4.14.0; the v68 dedupe verified live — exactly
one node_modules/axe-core entry; the engine-contract pin green inside
the a11y chunk).

**F2: the 105th standing checks ALL GREEN** — derived v104→v105 via the
persisted derive-standing-v111.py (three token families, normalize-back
diff clean, zero old tokens). Reference side: the four bugs ALL live
(toast-blocker hitIsBurgerChild:false; sheet-trap overlayCount:1 after
nav; no-landmark; the 464px /networth overflow measured docSW 464
directly) + the census clean on the first read + the SEO pair live.
Clone side: R1–R4 ALL GREEN — **the mobile menu VERIFIED WORKING the
105th consecutive time**, zero overflow at 390 on all five views, the
SEO pair live; the seedcheck exact after the clone half. One
zombie-browser cleanup applied between the halves (the standing reaping
step).

**F3: the pair's derivation + verdicts + census.** The series derived
from the v105 lineage (derive-v111-series.py, persisted): the six
generic swaps + the SIX exact-fragment history corrections (era marker,
last-re-shot, bracket extension, ordinal, agreement count, plan
attribution) — 6/6 on the FIRST run, zero residuals, line-count
preservation on all six files (101/29/165/29/64/354), bash -n +
node --check clean. The census BUILT two-half (build-twohalf-v111.py —
derived via derive-build-twohalf-v111.py with the swap-order rule; the
first derive attempt failed its MISSING-SOURCES check on three
builder-specific forms [the v105 builder carries no refarbit session
token; the lesson-range wrapped form; the lineage-note line break] —
corrected against the actual builder bytes, the second run clean):
**md5 contracts e1092d12 (CALC, 61 lines) + 9e5a52d2 (LOGIN, 36 lines)
source-to-source verified** — arbit-v105.sh's own blocks hash to the
same md5s; the v111 blocks carry them VERBATIM. The one-shot both-sides
census ran cleanly both halves (one zombie cleanup before the clone
half; the clone's "Contents Insurance" pairing + full restore verified:
delete + confirm + restore $1850 + "3 items · $2235.00" re-read + the
seedcheck exact).

**The VLM pairwise verdicts: CALCULATOR DIFFERENT + LOGIN IDENTICAL**
(the v105 precedent — the verdict-variation form). Every calculator
flag DOM-arbitrated to a documented class: the "• Will update category
total" note the **SEED-DATA class** (ref hasWillUpdateSpan false — its
own Rent $25.00 EQUALS its calculated total so the note hides; the
clone's $1850-vs-$25 shows it; the totalCard chrome byte-identical);
the hover-action row the **RESTING-STATE parity class**
(actionsAtRest {opacity 0, btnCount 2} IDENTICAL both sides — the
reference's screenshot caught its row post-pointer; the VLM
hover-state perception class, the v43 rule); the row-height flag their
consequence. The LOGIN pair's FAB unflagged (the standing disproof form
stays documented). The census's close-key asymmetry the v99-documented
finder artifact (the v87 pin holds the close-button chrome
byte-identical). **The census reproduces the v99/v105 values EXACTLY on
every axis — NO NEW CLONE GAP.**

**F4: the family-extension survey + the pin.** Survey walked both pair
surfaces' families against the full pin map: the login's OR-divider
family (v99-pinned), the verify-code inputs (v33/v51-pinned), the
line-item dialog (v5/v22/v9-pinned), the calculator's empty-state
(unreachable on the reference — its data always carries 1 row; a
cross-side census impossible without mutating its data — REJECTED),
the hover-action buttons' boxes (v6 G10-pinned), the login's top accent
strip (its geometry never pinned but its bg stops v7-pinned — an
extension-of-partial-coverage, weaker than the winner). **The winning
candidate: the calculator's LINE-ITEMS SECTION HEADER ROW** — the
dialog's section row between the v93-pinned totalCard and the items:
the row's flex chrome + the "Line Items" h3's computed typography —
zero "Line Items" assertions across ALL 24 specs (the coverage-map
grep), the v81 addBtn walked as CONTEXT ONLY. The one-shot both-sides
census (sectionrow-arbit-v111.sh — the nav-arbit-v110 pattern; two
repairs mid-build: the bare `click` command dropped the
hover-revealed Calculate button [fixed with the vlm-shots mouse-move +
down/up form] and the quoted-heredoc needed the env-var census
pass-through): **EVERY AXIS BYTE-IDENTICAL both sides** — the row
{flex/center/space-between/mb 16px/mt 0px/h 32/w 720/childCount 2} +
the h3 {"Line Items"/H3/16px/600/rgb(26,58,46)/lh 24px/h 24/margin 0px}
+ the addBtn context {110×32} + the junction (h3CenterY ===
rowCenterY) + docSW 1280. The plan written + validated BEFORE the pin
(docs/remediation-plan-v111.md). The pin appended to
tests/e2e/calculator.spec.ts as the v111 describe block — **GREEN on
the first run** (19 passed in the file; the authoritative count now
**314**). **Mutation verified single-axis AND cascade-free**:
font-semibold → font-bold at calculator-dialog.tsx:171 line-scoped
(the ONLY bare font-semibold line in the file; the nameH4's
mb-1 font-semibold at line 210 untouched) — ONLY the v111 pin red
(18 green) with the failure diff reading as the sectionH3.fw axis
ALONE ("600" → "700"; the v66/v81/v87/v93 pins green under the
mutation); restored (git diff src/ = 0), rebuilt, post-restore 19/19
green.

**F5 the ship chain**: lint ✓ · typecheck ✓ · 108/108 unit ✓ · npm
audit 0 vulnerabilities ✓ · **314 e2e zero flakes** (76+80+79+82 =
317 executions = 314 unique across FOUR chunks) · 35/35 smoke ✓. The
screenshots regenerated: **16/16 BYTE-IDENTICAL** — the same-day-seed
law (the seed's relative dates roll with the UTC day; the v110 capture
and this one share the day — zero deltas, zero arbitration needed).
The dev-server evidence set re-captured + VLM-verified (the menu
proof: /income, docSW 390, navLandmark true; the menu open with all 5
links + the brand; the sheet closed post-nav; the dashboard clean —
the Budget Guidelines card below the 800px fold the documented
non-defect). The dev-shots scripts derived v110→v111 by the
version-swap protocol (4 + 2 tokens).

The docs aligned D1–D7 (AGENTS.md the v111 paragraph · CLAUDE.md 314 +
the v111 clause · README.md counts + the v111 plan row ·
zero-balance_SKILL.md the Session 146 row + the state line · PAD
v1.1.68 · the probe README's v111 section + THE PROVISIONING LESSON +
the v112 queue); `docs/remediation-plan-v111.md` saved (the ToDo
statuses updated to DONE through the pin); this delivery record saved.
The `.env.example` verified matching the codebase (untouched this
cycle — no env-facing change).

The ship: local commit → SSH-wrapper push (the dry-run fast-forward
check → the real push → SSH + independent HTTPS double-verify) → the
operator key shredded. The follow-up session log commits per the
standing two-commit precedent.
