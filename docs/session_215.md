# Session 215 — the v89 parity cycle (the dashboard pair's fourth re-run)

The formal narrative of the v89 iteration (docs/remediation-plan-v89.md —
the plan validated against the codebase before execution, the mutation
refutations included). The continuation of the audit → align → remediate →
push workflow on the preserved workspace.

## The workspace

The preserved-workspace path (the v87 precedent — no reset): `git pull`
fast-forward `0cae166..ef681c0` (the session_214 transcript only), the tree
clean. The environment verified in place: `.env`
(DATABASE_URL="file:../db/custom.db"), `db/` at the repo root (custom.db +
e2e.db), node_modules (354 packages), chromium-1243, the paramiko ssh shim
at /home/z/my-project/bin/ssh. The seedcheck exact before any flow ran (7
items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2
liabilities).

## The audit

The v88 commit (464025b) re-verified PIN-ONLY as documented (17 files,
+1513/-4, ZERO src/ changes); the two commits since session-log-only
(session_213 + session_214). The production seams re-audited clean: the
auth scrypt/HMAC chain, the db-path contract, the SEO pair
(robots.ts + sitemap.ts), the Tailwind v4 mitigations in globals.css, the
three test tiers, the skills/ exclusion (eslint ignores + tsconfig
exclude).

## F0 — the baseline chain: FULLY GREEN as-shipped

lint ✓ · typecheck ✓ · 108/108 unit ✓ · `npm run build` ✓ (robots +
sitemap prerendered) · **291 e2e** (120 + 113 + 60 chunk executions = 293
total = 291 unique tests — the chunk boundaries split differently than
v88's 104 + 129 + 60 but the unique total identical) · 35/35 smoke ✓.

## F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (only 4.14.1 rc/next
prereleases — no stable 4.14.1, no 5.x); the lockfile holding the v68
dedupe state (no nested engine dir); the engine-contract pin GREEN
standalone (2 passed).

## F2 — the 83rd standing checks: ALL GREEN

ref-standing-v83.sh + standing-checks-v83.sh (version-bumped from v82
across the three token families — version-bump-only diffs verified by
normalizing back and diffing clean). Reference side: the four bugs ALL
live (toast-blocker `hitIsBurgerChild:false`; sheet-trap
`overlayCount:1`; no-landmark `navLandmark:false`; the 464px /networth
overflow at 390); the data census UNCHANGED (the 83rd clean drift
check); the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile
navigation menu VERIFIED WORKING (the **83rd consecutive time**:
`hitIsBurgerChild:true`, the sheet opens, closes on nav, the nav
landmark present), zero overflow at 390 on all five views, the SEO pair
live.

## F3 — the re-run pair (the v83-era dashboard pair's fourth re-run)

The probe series derived from the v83 lineage (vlm-shots-v89.sh +
clone-vlmshots-v89.sh + vlm-compare-v89.mjs + arbit-v89.sh — the sed
substitutions with the version + session-name + tmp-dir token families,
the headers history-corrected to the fourth re-run, the functional
bodies verified version-bump-only).

**The verdict: IDENTICAL — zero style flags** (the pair's second
consecutive IDENTICAL verdict [v83 → v89]; every VLM flag the documented
seed-data classes — the allocation bar, the balance figures, the stat
values, the donut proportions).

**The both-sides census** (arbit-v89.sh — the v75 convention: the census
runs regardless of the verdict) — executed in the CONTROLLED TWO-HALF
FORM (ref-arbit-v89.sh + clone-arbit-v89.sh) after the sandbox's chromium
resource exhaustion (66 zombie processes reaped via `pkill -f
agent-browser`) aborted the combined run; a transient with-server boot
abort (the standalone server "Aborted" once with an empty log, then
booted clean on retry) resolved retry-first. The census REPRODUCES the
v83 census values EXACTLY — zero drift on every axis:

1. PART G (the guidelines card): the card 468×348/radius 12px/border
   rgb(229,231,227) 1px/white/the visible shadow layers; the header pad
   24px/fs 16px/fw 600/rgb(26,58,46)/lh 16px/tracking -0.4px; the body
   pad 0px 24px 24px/display block; the three tiles 418×78 with the
   Needs/Wants/Savings tint families — the ONLY delta the shadow's
   transparent lead-layer count (the v66 computed-form INVISIBLE class).
2. PART Q (the quick-action row): the grid 304px×3/gap 24px/w 960; the
   three cards 304×90/radius 16px/pad 24px/the full chrome — the grid-mt
   (ref 0px vs clone 32px) the v77 mechanism class with the RENDERED gap
   340 byte-identical; the label wrapper-catch the v61 lesson.
3. PART X (the cross-row gap): cardBottom 1122/gridTop 1462/gap 340
   byte-identical on BOTH sides.

**NO NEW CLONE GAP — the v89 iteration is PIN-ONLY.**

## F4 — the +1 pin (292 e2e): the quick-action transition + plus-viewBox + guidelines-body-display census at 1280

The never-pinned families (the pin's own axes first measured
byte-identical on both sides by the supplemental one-shot census —
qa-transition-arbit-v89.sh, the v87/v88 precedent):

- the three quick-action cards' TRANSITION family
  {transitionDuration "0.2s", transitionProperty "all"} — never pinned
  at ANY viewport (the items.spec.ts transitionDur pins are the ITEM
  card's own family, a different component);
- the three PLUS icons' viewBox {"0 0 24 24"} — the v77 icon-viewBox
  family's plus twin;
- the guidelines body's DISPLAY {"block"} — the v61 F2 pad family's
  companion axis;
- the docSW 1280 guard.

The pin (tests/e2e/dashboard.spec.ts) GREEN on first run. The pin-sanity
mutation (the executed form — the viewport-scoped responsive-variant
dodge): the card's `duration-200` → `duration-200 lg:duration-300`
(dashboard-view.tsx:885, applied by LINE NUMBER) — the pin FAILS at
exactly the card.transitionDuration axis ("0.2s" → "0.3s"; the failure
diff reads as the duration axis alone), the full dashboard.spec.ts under
the mutation 40 green + only the v89 pin red — cascade-free BY
CONSTRUCTION (transitionDuration never affects geometry; the v45 F3b
hover-shadow pin asserts the settled layers). Restored (the standalone
REBUILD as a SEPARATE command; git diff src/ = 0 lines; the post-restore
full run 41/41 green). The disproven-in-advance candidates documented in
the plan without execution (the plus-viewBox shared-component cascade,
the body-display shared-card-interior cascade, the v86 ratio-line-height
trap on the fs axis).

## F5 — the full chain re-run + the screenshots

lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **292 e2e** (121 + 113 +
60 chunk executions = 294 total = 292 unique tests, zero flakes) ·
35/35 smoke ✓. The screenshots **16/16 BYTE-IDENTICAL** (the
same-day-seed byte-identity law — the seed planted and the shots taken
on the same calendar day 2026-10-18 reproduce the committed set
byte-for-byte; no pixel arbitration needed). The final seedcheck exact.

## The docs alignment (D1–D7)

D1 AGENTS.md (the v89 paragraph), D2 CLAUDE.md (292 + the v89 pin
clause), D3 README.md (the counts + the v89 plan-table row), D4
zero-balance_SKILL.md (Session 124 audit row + the state lines), D5 the
PAD's v1.1.46 revision block, D6 the probe README's v89 section (the
chromium resource-exhaustion lesson + the two-half controlled census
form), D7 this session_215.md + the worklog Session 124 entry.

## The ship

The pre-ship gate: lint ✓ · typecheck ✓ · PIN-ONLY ✓ (git diff src/ = 0
lines) · test-results cleaned · no orphaned servers · .env.example
tracked and matching. The parity commit + the session-log commit pushed
via the SSH wrapper (the explicit --remote flag), the remote verified
main == local HEAD, the operator key shredded after the push.
