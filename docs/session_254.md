# Session 254 — Parity iteration v104 (Session 139): the re-run cycle's next-oldest candidate (the v98-era SAVINGS pair's seventh re-run) + the axe watch (NO DRIFT) + the 98th standing checks + the rail brand-block subtitle/row census pin (PIN-ONLY)

The workspace refreshed: `git clone` at main @ bb7e02e (the sandbox
reset — the fresh-clone class, the v86/v88/v90/v91/v92/v98/v100/v101/
v103 precedent). The core docs re-reviewed (AGENTS/CLAUDE/README/PAD/
SKILL) + the session docs (session_252, remediation-plan-v103, worklog
Session 138, session_253). The state understood: v103 shipped PIN-ONLY
(+1 e2e = 306) + the two session-log follow-up commits (f6b5ccf +
bb7e02e, both audited session-log-only — ZERO src/ or lockfile
deltas); the queue's v104 suggestion targets the v98-era SAVINGS pair
— verified against vlm-shots-v98.sh's own header (the TWENTY-SEVENTH
consecutive queue/ledger agreement) BEFORE the derivation, per
protocol.

The environment re-provisioned: npm install; `.env` written
(DATABASE_URL="file:../db/custom.db"); `db/` at the repo root,
db:generate + db:push + db:seed; chromium-1243 installed for the
pinned @playwright/test 1.63.0; the tool-results dir re-created for
with-server.sh. Seedcheck exact (7 items / rent 1850 / expensesTotal
2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran
(the `env -u DATABASE_URL` discipline).

F0 baseline: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots +
sitemap prerendered) · 306 e2e in FOUR chunks (126+90+57+37 = 310
executions = 306 unique — the exact documented v103 state [305 spec +
the v103 pin + 1 setup], the count first derived authoritatively via
`playwright test --list` and the per-file counts summed against the
authoritative total BEFORE any chunk ran — the v103 chunk-split
self-audit lesson applied by construction; zero flakes on the FIRST
run) · 35/35 smoke ✓.

F1 axe watch: NO DRIFT (npm-latest @axe-core/playwright 4.14.0 — only
rc/next sha prereleases beyond, no stable 4.14.1, no 5.x; the
installed wrapper 4.14.0 + the engine 4.14.0; the lockfile holding
the v68 dedupe state [exactly one node_modules/axe-core entry]; the
engine-contract pin GREEN standalone [2 passed]).

F2 the 98th standing checks: derived from the v97 pair via the
persisted derive-standing-v104.py (the THREE token families
[v97→v98, 97th→98th, ref97→ref98/clone97→clone98]; version-bump-only
verified by the normalize-back diff — zero old tokens remaining; both
halves bash -n clean). Reference side: the four bugs ALL live
(toast-blocker hitIsBurgerChild:false; sheet-trap overlayCount:1 after
nav; no-landmark navLandmark:false; the 464px /networth overflow
measured docSW 464 directly); the data census UNCHANGED on the FIRST
read (networth "1 items · $25,000" / income "1 items · $5000.00" /
expenses "4 items · $525.00" — no render-race this cycle); the SEO
pair live. Clone side: R1–R4 ALL GREEN — the mobile menu VERIFIED
WORKING the 98th consecutive time (hitIsBurgerChild: true, the sheet
opens, closes on nav, the nav landmark present — the Tailwind v4
mitigation holds), zero overflow at 390 on all five views, the SEO
pair live. The seedcheck exact after the clone half.

F3 the re-run pair: the probe series derived from the v98 lineage via
the persisted derive-v104-series.py — the generic swaps + the
exact-fragment history corrections (last-re-shot v92→v98, the era
marker v92-era→v98-era, SIXTH→SEVENTH, the re-run bracket extension
[v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104], the
oldest-remaining list bumped to the current era [v98 < v99 < v100 <
v101 < v102 < v103], the plan attribution v97→v103, the agreement
count TWENTY-FIRST→TWENTY-SEVENTH, and the v98-era pin-candidate
provenance note kept historical) — zero misses, zero residual old
tokens, line counts preserved on all four files. The two-half census
BUILT from the start (build-twohalf-v104.py: ref-arbit-v104.sh +
clone-arbit-v104.sh, the ONE SV_CENSUS_JS block [153 lines]
byte-identical across the halves — the md5 line-block contract
[891ab9b6]). Login on the first attempt both sides; the parked pointer
at (5,5); read-only — the v46 rule holds; the seedcheck exact after
the clone half.

The VLM verdict: DIFFERENT (the pair's documented verdict class) with
every flag DOM-arbitrated to a documented class — the "Card Footer
Layout" the v57 DATA-CONDITIONAL class (the footer childCount 1-vs-2,
the clone's "Brokerage" chip; the reference RENDERS payment chips when
data carries them per the v97 income-card evidence); the "Card Grid"
the seed-count class (1 vs 2); the header-subtitle + card-contents
flags the seed-data classes; the avatar the user-identity class; the
"Edit with Base44" FAB NOT FLAGGED this cycle — the THIRD documented
form (unflagged platform chrome, no attribution either way, no
arbitration needed for an unflagged family).

The both-sides census REPRODUCES the v98 census values EXACTLY —
zero drift on every axis (the h1/grid/card/titleRow/amount/footer/
badge families; the card h 200-vs-230 the v57/v70b Recurring-wrap
class; the clone template's last-column sub-pixel the
column-distribution rounding noise WITHIN the documented 309.328px
family; the docSW 1280 guard). NO NEW CLONE GAP — the iteration
PIN-ONLY.

F4 the +1 pin: the rail's TOP brand-block subtitle/row census at 1280
(tests/e2e/nav-geometry.spec.ts). The FAMILY-EXTENSION survey walked
the candidates — the savings view's card/header/filter families are
exhaustively pinned (v45/v51/v54/v57/v58/v64/v65/v70/v74/v80/v86/
v91/v98); the header family fully coupled (one component, 3 views —
not cascade-free); the toast family cross-side unverifiable under the
v46 read-only rule (the reference's toasts need write flows); the
confirm-bar family pinned by v46 F3 on the networth side. The
winning candidate: the brand block's never-pinned axes — the v7 G4
pin holds the tile/icon/h2 size+weight ONLY; the h2's COLOR +
LINE-HEIGHT, the subtitle P's computed chrome ("Budget Planner" —
only the mobile sheet's VISIBILITY check anywhere), and the brand
ROW's flex chrome NEVER pinned at ANY viewport in ANY spec (the
coverage-map grep across all 23 specs). The pin's own axes first
measured byte-identical on BOTH sides via the one-shot census
brand-arbit-v104.sh (the base44-fab/userfooter pattern): the row
{flex, center, gap 12px} + the h2 {18px/700/lh 28px/rgb(26,58,46)} +
the subtitle {"Budget Planner" 12px/400/rgb(45,90,74)} + the tile
40×40/12px + the icon 24×24 — every axis DATA-INDEPENDENT. The live
discovery: the reference's rail is a DIV not an aside — the first
`aside h2` run returned {err: no h2} on the reference; the finder
fixed with the v103 fallback chain (aside OR the 180–320px-wide
700px-tall left-anchored div) — every cross-side rail finder must use
the fallback-chain form.

The plan written and validated BEFORE the pin's execution
(docs/remediation-plan-v104.md — the measured values, the mutation
target line verified by reading the source, the coverage-map grep,
the nav-pitch headroom analysis, the disproven-in-advance candidates).
The pin appended; typecheck clean; GREEN on the first run (10/10 in
nav-geometry.spec.ts). The pin-sanity mutation (sidebar.tsx:48
text-xs → text-sm, LINE-NUMBER-SCOPED — the section label's own
text-xs at line 61 + the user-footer subtitle's own at line 129
untouched): ONLY the v104 pin red (9 green) at the subtitle.fs axis
ALONE ("12px" → "14px"; the pin deliberately omits the subtitle's
line-height — text-sm moves fs AND lh, a two-axis failure diff — the
single-axis discipline) after the standalone REBUILD; the one INDIRECT
coupling — the v36 S3 nav-pitch band (navY[0] within 140–150,
measured 145 live) — survives the mutation's worst-case +4px shift
(149 < 150, the headroom analysis in the plan); restored (git diff
src/ = 0), rebuilt, post-restore 10/10 green.

F5 the full chain re-run: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · 307 e2e zero flakes (126+90+57+37 = 310 chunk executions =
307 unique across the four-chunk auditable split) · 35/35 smoke ✓.
The screenshots regenerated: **16/16 BYTE-IDENTICAL** (the same-day
regeneration — both the v103 committed set and this cycle's capture
on Oct 21 UTC, the fresh seed's date offsets anchoring identically,
no midnight crossing — the v97 precedent; NO DATE-class deltas this
cycle, no pixel-diff arbitration needed). The final seedcheck exact.

D1–D7 docs alignment: D1 AGENTS.md (the v104 paragraph), D2 CLAUDE.md
(306 → 307 + the v104 clause at the E2E line's tail), D3 README.md
(the counts + the v104 plan-table row), D4 zero-balance_SKILL.md
(Session 139 audit row + the state line 306 → 307), D5 the PAD's
v1.1.61 revision block (the header bumped + the entry inserted above
v1.1.60), D6 the probe README's v104 section (+ the three lessons +
the v105 queue), D7 this file + the worklog Session 139 entry.

**The next queue:** the v105 cycle — the v99-era LOGIN + CALCULATOR
pair (now the oldest remaining [v99 < v100 < v101 < v102 < v103 <
v104]); verify against vlm-shots-v99.sh's own header first, per
protocol.
