# Session 251 — Parity iteration v103 (Session 138): the re-run cycle's next-oldest candidate (the v97-era ITEMS pair's seventh re-run) + the axe watch (NO DRIFT) + the 97th standing checks + the rail user-footer tile census pin (PIN-ONLY)

The workspace refreshed: `git clone` at main @ 0291a6e (the sandbox
reset — the fresh-clone class, the v86/v88/v90/v91/v92/v98/v100/v101
precedent). The core docs re-reviewed (AGENTS/CLAUDE/README/PAD/SKILL)
+ the session docs (session_249, remediation-plan-v102, worklog
Session 137, session_250). The state understood: v102 shipped PIN-ONLY
(+1 e2e = 305) + the two session-log follow-up commits; the queue's
v103 suggestion targets the v97-era ITEMS pair — verified against
vlm-shots-v97.sh's own header (the TWENTY-SIXTH consecutive
queue/ledger agreement) BEFORE the derivation, per protocol.

The environment re-provisioned: npm install; `.env` written
(DATABASE_URL="file:../db/custom.db"); `db/` at the repo root,
db:generate + db:push + db:seed; chromium-1243 installed for the
pinned @playwright/test 1.63.0; the tool-results dir re-created for
with-server.sh. The two commits since the v102 parity push (ef1148c +
0291a6e) audited session-log-only (session_249 + session_250 — ZERO
src/ or lockfile deltas). Seedcheck exact (7 items / rent 1850 /
expensesTotal 2235 / 0 line items / 3 assets / 2 liabilities) before
any flow ran.

F0 baseline: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots +
sitemap prerendered) · 305 e2e in FOUR chunks (117+96+85+10 = 308
executions = 305 unique — the exact documented v102 state, the count
first derived authoritatively via `playwright test --list`; zero flakes
on the FIRST run; the chunk-split self-audit lesson learned live: the
Playwright file filter is a path regex — "items.spec.ts" does NOT match
item-details.spec.ts, so the first three-chunk plan silently dropped
item-details' 9 tests; the per-chunk file lists re-derived from ls +
the per-file --list counts summed against the authoritative total) ·
35/35 smoke. The production seams re-audited clean (auth, db-path, the
SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/
excluded).

F1 the axe-core watch: NO DRIFT — npm-latest 4.14.0 (only rc/next sha
prereleases beyond — no stable 4.14.1, no 5.x); the installed wrapper +
engine both 4.14.0; the v68 dedupe holds (exactly one
node_modules/axe-core lockfile entry); the engine-contract pin GREEN
standalone (2 passed).

F2 the 97th standing checks: ALL GREEN (ref-standing-v97.sh +
standing-checks-v97.sh, derived from the v96 pair via the PERSISTED
derive-standing-v103.py across the THREE token families [v96→v97,
96th→97th, ref96→ref97/clone96→clone97], version-bump-only verified by
the normalize-back diff — zero old tokens remaining, both halves bash
-n clean). Reference side: the four bugs ALL live (toast-blocker
`hitIsBurgerChild:false`; sheet-trap `overlayCount:1` after nav;
no-landmark `navLandmark:false`; the 464px /networth overflow at 390
measured docSW 464 directly); the data census UNCHANGED on the FIRST
read (networth "1 items · $25,000" / income "1 items · $5000.00" /
expenses "4 items · $525.00" — no render-race this cycle); the SEO pair
live. Clone side: R1–R4 ALL GREEN — **the mobile menu VERIFIED WORKING
the 97th consecutive time** (`hitIsBurgerChild:true`, the sheet opens,
closes on nav, the nav landmark present — the Tailwind v4 mitigation
holds), zero overflow at 390 on all five views, the SEO pair live; the
seedcheck exact after the clone half.

F3 the re-run pair (the v97-lineage derivation, the two-half census
form): the probe series derived from the v97 lineage via the PERSISTED
derive-v103-series.py (the generic swaps + the exact-fragment history
corrections [last-re-shot v91→v97, SIXTH→SEVENTH, the bracket
extension, the other-pairs list bumped to the current era] — every
correction's hit/miss REPORTED by the script itself, ZERO misses; the
line-count-preservation check green on all four files; bash -n + node
--check clean; the residual check clean with the provenance whitelist).
The census BUILT two-half from the start via build-twohalf-v103.py
(ref-arbit-v103.sh + clone-arbit-v103.sh — the ONE census JS block
[CENSUS_JS 193 lines] byte-identical across the halves by the md5
line-block contract [b55dcd29 — the v97 census block verbatim]; the
doubled-brace spot check clean). The reaping budget applied as the
standing step between halves. Login on the first attempt both sides;
the parked pointer at (5,5); read-only — the v46 rule holds; the
seedcheck exact after the clone half.

**The verdict: BOTH DIFFERENT — the pair's documented verdict class (the
same flag-set classes as the v91/v97 re-runs) with every flag
DOM-arbitrated to a documented class:** the avatar the user-identity
class; the "Edit with Base44" FAB the platform-chrome class with the
INVERTED attribution form on PAIR 1 (re-arbitrated live by the one-shot
both-sides DOM census base44-fab-arbit-v103.sh: **fabCount 0 +
bodyHasBase44 false on BOTH sides**) and the non-inverted form on PAIR
2 — both forms documented; the payment-method footer chips the v57
DATA-CONDITIONAL class (the reference renders chips when data carries
them: its income footer childCount 2 with the "Bank Account" chip); the
header stats + card grids + contents the seed-data/seed-count classes;
the "Recurring" 4th badge the DATA-CONDITIONAL class.

The both-sides census REPRODUCES the v97 census values EXACTLY — zero
drift on every axis (the avatar chrome; the grid/card chrome; the
titleRow/amount/footer/badge chrome; the filter-card both variants [the
v64/v70 contract]; the header + the docSW 1280 guard). **NO NEW CLONE
GAP — the v103 iteration PIN-ONLY.**

F4 the +1 e2e pin (305 → 306): the rail's bottom USER-FOOTER tile
census at 1280 (tests/e2e/nav-geometry.spec.ts — the FAMILY-EXTENSION
pattern: the v79 F4 pin covers the avatar INSIDE the tile; the mobile
sheet asserts only the texts' visibility; **the tile's own box + the
name/subtitle typography + the border-t wrapper NEVER pinned at ANY
viewport in ANY spec** — the coverage-map grep across all 23 spec
files). The pin's own axes first measured byte-identical on BOTH sides
by the one-shot both-sides census (userfooter-arbit-v103.sh — the
base44-fab one-shot pattern; the census JS defined ONCE and eval'd on
both sides, byte-identical by construction; both sides READ-ONLY login
+ passive navigation): the tile {w 223, h 60, radius 8px, pad 12px, bg
rgb(245,248,245), flex, center, gap 12px}; the wrapper {borderTop 1px
rgb(229,231,227), pad 16px, gap 8px}; the avatar {w 36} control; the
name {"Budget Pro", fs 14px, fw 500, color rgb(26,58,46), ellipsis};
the subtitle {"Track your finances", fs 12px, fw 400, color
rgb(45,90,74), ellipsis} — every axis DATA-INDEPENDENT (the static
copy pair; the identity-dependent avatar TEXT never asserted). The
remediation plan v103 written + validated BEFORE the pin's execution
(docs/remediation-plan-v103.md — the pre-execution validation section
recording the measured values, the mutation target line verified by
reading the source [sidebar.tsx:116 carries EXACTLY ONE rounded-lg;
the nav links' own at line 79 + the burger's own at line 227 untouched
by the line-number scoping], the coverage-map grep, the
disproven-in-advance candidates). The pin GREEN on first run. The
pin-sanity mutation (the tile's rounded-lg → rounded-xl at
sidebar.tsx:116, by LINE NUMBER): the failure diff reads as the tile
radius axis ALONE ("8px" → "12px") — cascade-free BY CONSTRUCTION
(border-radius never changes the layout box — the v99/v101 precedent) —
ONLY the v103 pin red (8 green) after the standalone REBUILD (the v98
mutation-rebuild discipline), then restored (git diff src/ = 0; the
REBUILD; the post-restore full file run 9/9 green).

F5 the full chain re-run GREEN: lint ✓ · typecheck ✓ · 108/108 unit ✓
· build ✓ · **306 e2e** (117+96+86+10 = 309 chunk executions across the
four-chunk auditable split = 306 unique tests — 305 spec + the v103 pin
+ 1 setup; zero flakes) · 35/35 smoke ✓; the screenshots **10/16
byte-identical + SIX fresh-seed DATE-class deltas pixel-arbitrated**
(diff-shots-v103.mjs + diff-shots-v103-bands.mjs — the bbox + row-band
decomposition: every delta a text-row band [h 19 glyph rows / the field
regions], zero structural bands; the fresh-seed +1-day roll, the
v86/v80/v92 fresh-seed precedent, the updated set committed); the final
seedcheck exact; `.env.example` verified tracked + codebase-matched;
`.env` + `db/*.db` correctly gitignored.

The docs alignment: D1 AGENTS.md (the v103 paragraph), D2 CLAUDE.md
(305 → 306 + the v103 clause at the E2E line's tail), D3 README.md
(the two count lines + the v103 plan-table row), D4
zero-balance_SKILL.md (Session 138 audit row + the state line 305 →
306), D5 the PAD's v1.1.60 revision block (the header bumped + the
entry inserted above v1.1.59), D6 the probe README's v103 section (+
the three lessons + the v104 queue), D7 this file + the worklog
Session 138 entry. The staleness sweep clean (zero stale current-state
305 references in the count lines; the historical rows stay
era-correct).

**The next queue:** the v104 cycle — the v98-era SAVINGS pair (now the
oldest remaining [v98 < v99 < v100 < v101 < v102 < v103]); verify
against vlm-shots-v98.sh's own header first, per protocol.
