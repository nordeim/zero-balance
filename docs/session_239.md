# Session 239 — Parity iteration v99 (Session 134): the re-run cycle's next-oldest candidate (the v93-era LOGIN + CALCULATOR pair's sixth re-run) + the axe watch (NO DRIFT) + the 93rd standing checks + the login social-row census pin (PIN-ONLY)

The workspace refreshed: `git pull` to main @ 74a206e (fast-forward —
docs/session_238.md the one new file). The core docs re-reviewed
(AGENTS/CLAUDE/README/PAD/SKILL) + the session docs (session_237,
remediation-plan-v98, worklog Session 133, session_238). The state
understood: v98 shipped PIN-ONLY (+1 e2e = 301); the queue's v99
suggestion targets the v93-era LOGIN + CALCULATOR pair — verified
against vlm-shots-v93.sh's own header (the TWENTY-SECOND consecutive
queue/ledger agreement) BEFORE the derivation, per protocol.

The environment: the CARRIED-OVER class — the two commits since the
v98 push 08cc3cf (7939458 + 74a206e) verified session-log-only
(session_237.md + session_238.md — ZERO src/ or lockfile deltas), so
the v98 cycle's own fresh-clone environment carries over unchanged (no
re-provisioning; node_modules 354 packages present; `.env` verified
[DATABASE_URL="file:../db/custom.db"]; `db/` at the repo root; the
sandbox's polluted parent DATABASE_URL re-confirming the env -u
discipline). Seedcheck exact (7 items / rent 1850 / expensesTotal 2235
/ 0 line items / 3 assets / 2 liabilities) before any flow ran.

F0 baseline: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots +
sitemap prerendered) · 301 e2e in three chunks (114+99+90 = 303
executions = 301 unique) with ONE first-run timing flake — the
not-found.spec.ts head-parity test at the 15-file chunk's tail, clean
on the immediate single-spec re-run AND the full-chunk re-run (90/90),
the documented v96-era timing-artifact class · 35/35 smoke. The
production seams re-audited clean (auth, db-path, the SEO pair, the
Tailwind v4 mitigations, the three test tiers; skills/ excluded).

F1 axe-core watch: NO DRIFT (npm-latest 4.14.0, only rc/next sha
prereleases beyond — no stable 4.14.1, no 5.x; the installed wrapper +
engine both 4.14.0; the v68 dedupe holds; the engine-contract pin
GREEN standalone, 2 passed).

F2 the 93rd standing checks: derived ref-standing-v93.sh +
standing-checks-v93.sh from the v92 pair via the PERSISTED
derive-standing-v99.py (three token families: v92→v93, 92nd→93rd,
ref92→ref93/clone92→clone93 — version-bump-only verified by the
normalize-back diff, zero old tokens, bash -n clean). Reference side:
the four bugs ALL live (toast-blocker hitIsBurgerChild:false /
sheet-trap overlayCount:1 after nav / no-landmark navLandmark:false /
the 464px /networth overflow measured docSW 464 directly); the data
census UNCHANGED on the FIRST read (networth "1 items · $25,000" /
income "1 items · $5000.00" / expenses "4 items · $525.00" — no
render-race this cycle); the SEO pair live. Clone side: R1–R4 ALL
GREEN — the mobile menu VERIFIED WORKING the 93rd consecutive time
(hitIsBurgerChild:true, the sheet opens, closes on nav, the nav
landmark present — the Tailwind v4 mitigation holds), zero overflow at
390 on all five views, the SEO pair live.

F3 the re-run pair: derived the v99 probe series from the v93 lineage
via the PERSISTED derive-v99-series.py — the generic swaps (v93→v99,
refvlm93→refvlm99, clonevlm93→clonevlm99, reflogin93→reflogin99,
clonelogin93→clonelogin99, refcalc93arbit→refcalc99arbit,
clonecalc93arbit→clonecalc99arbit, /tmp/vlm93→/tmp/vlm99) then the
exact-fragment history corrections (last-re-shot v87→v93, FIFTH→SIXTH,
the re-run bracket extension, the oldest-remaining bracket [v93 < v94 <
v95 < v96 < v97 < v98], the agreement ordinal SIXTEENTH→TWENTY-SECOND,
the suggesting plan v92→v98) — every correction's hit/miss REPORTED
(the ONE first-run MISS — the clone-login header's "the re-run\n#
cycle's" line break, the assumed form carried it unbroken — caught by
the report itself and fixed before any probe executed; the v96/v98
miss-report discipline). bash -n + node --check clean on all six; zero
residual old tokens (the legitimate v87 pin-provenance token
whitelisted by context). Built the two-half census via
build-twohalf-v99.py (CALC_CENSUS_JS 61 lines md5 e1092d12 +
LOGIN_CENSUS_JS 36 lines md5 9e5a52d2, byte-identical across the
halves). The reaping budget between every half. Reference shots clean
(login first attempt; the calculator dialog opened via the full
mouse-down/up sequence). The clone calculator half hit a 300s tool
timeout on a hung agent-browser call — the re-run discipline (reaped,
re-ran, completed clean with the FULL fixture restore: delete +
confirm + restore $1850 + the "3 items · $2235.00" re-read); the clone
login half clean.

The VLM verdicts: the CALCULATOR pair DIFFERENT (the documented re-run
class) with every flag DOM-arbitrated to a documented class — the
"Will update category total" line the SEED-DATA class (the census
proving the reference's hasWillUpdateSpan false vs the clone's true:
the reference's own Rent $25.00 EQUALS its calculated total so the note
stays hidden; the clone's Rent $1850 vs the recalculated $25.00 shows
it — the v73-documented DATA-CONDITIONAL class; the totalCard chrome
byte-identical); the reference-row-shows-hover-buttons flags the
RESTING-PARITY class (actionsAtRest opacity 0 / btnCount 2
byte-identical on both sides — the VLM caught the reference's row
post-pointer, the v43 rule applied: the measurement is the authority).
The LOGIN pair IDENTICAL — zero flags.

The both-sides census (the two-half controlled form) REPRODUCES the
v87/v93 census values EXACTLY — zero drift on every axis: the login
{card 448/16px/rgba(255,255,255,0.95); h1 30px/700/rgb(15,23,42)/lh
36px; subtitle 16px/rgb(100,116,139); logo 96×96; inputs h 48/radius
12px/border rgb(226,232,240)/fs 14px; signIn 368×48/12px/
rgb(15,23,42)/white/14px/500; hasGoogle true; hasORDivider true; docSW
1280} and the calculator {panel 768×393/16px/768px/white; scrim
rgba(26,58,46,0.5)/blur(8px)/1280×800; title 18px/700/rgb(26,58,46)/lh
28px; desc 14px/rgb(107,114,128)/lh 20px; totalCard 720×90/pad
16px/12px/border rgb(252,221,213); nameH4 16px/600/rgb(26,58,46)/h 24/
mb 4px; row 720×102/16px/12px/borderTop rgb(229,231,227)/white;
pillRow flex/8px/12px/h 20; pill1 h 20/w 65/pad 2px 8px/radius
9999px/12px/400; amountP 20px/700/rgb(224,122,59)/h 28; actionsAtRest
opacity 0/btnCount 2; addBtn 110×32/6px/12px/500/white; docSW 1280}.
The census's own close-button finder artifact arbitrated this cycle:
the LOGIN half's JS finder (aria-label/text) matched the clone's
labelled Radix close button but NOT the reference's TEXTLESS SVG button
— the supplemental geometric probe closebtn-arbit-v99.sh (the
header-band button census, the full pointer-event sequence per the v98
lesson) reads the reference's close button {36×36, radius 6px, bg
rgba(0,0,0,0), border 0px, svg 1} — byte-identical to the clone's
census close field. The v98 unlabelled-trigger class EXTENDED. NO NEW
CLONE GAP — PIN-ONLY.

F4 the +1 e2e pin (301 → 302): the family-extension survey applied the
v97 missing-middle lesson to the LOGIN surface's SOCIAL row. The
coverage-map grep across all 24 specs: the v75 F4 pin walked
card/h1/subtitle/inputs/signIn/logo; the v7 G3 pin holds the Google
button's COLORS; the v45 F4 pin its HOVER shadow; the auth.spec pins
the OR divider's PRESENCE (booleans) — the OR divider's computed chrome
and the Google button's geometry/typography NEVER pinned at ANY
viewport in ANY spec.

The supplemental two-half census (build-social-v99.py —
social-arbit-v99.sh + social-clone-v99.sh, the census JS byte-identical
by the md5 line-block contract [d7add89b — 32 lines]; both sides
READ-ONLY passive navigation — the logged-out /login surface needs no
session; the seedcheck exact after the clone half): the Google button
{w 368, h 54, radius 12px, fs 16px, fw 500, lh 24px, color
rgb(51,65,85), bg white, border 1px rgb(226,232,240), pad 14px 20px,
gap 12px, display flex, svg 20×20} + the "or" text {fs 12px, fw 500,
color rgb(100,116,139), lh 16px, uppercase, ls 0.6px, pad 0px 12px, bg
white, h 16, w 43} + the single rule {h 1px, bg rgb(226,232,240), w
368 — the tag DIV-vs-SPAN the inert construct class} + the rhythm
{googleToOr 32, signInToGoogle −358 — the social block renders ABOVE
the form on BOTH sites, the parity-correct order} + the docSW 1280 —
BYTE-IDENTICAL on both sides. Every axis DATA-INDEPENDENT (the static
logged-out surface).

The remediation plan v99 written and validated BEFORE the pin's
execution (the pre-execution validation section with the measured
values, the mutation target line verified against the source
[login-card.tsx:172 carries EXACTLY ONE rounded-xl], the coverage-map
grep, the disproven-in-advance candidates: py-3.5→py-4 [three axes],
text-xs→text-sm [four axes], tracking-wider→tracking-wide [two],
font-medium→font-normal [fw + possibly w]).

The pin appended to login-parity.spec.ts — GREEN on first run (2
passed). The pin-sanity mutation (rounded-xl → rounded-lg at
login-card.tsx:172, by LINE NUMBER): the first mutation run read the
TS build failing on the pin's own `card` typing (a `let card = form`
inference error — fixed with the explicit `HTMLElement | null`
annotation; the v98 lesson's variant: a NEW spec's first build can
carry its own type debt); after the fix + the standalone REBUILD, ONLY
the v99 pin red (29 green), the failure diff reads as the google radius
axis ALONE ("12px" → "8px") — cascade-free BY CONSTRUCTION
(border-radius never changes the layout box). Restored (git diff src/ =
0); the standalone REBUILD; the post-restore full run 30/30 green.

F5 the full chain: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · 302
e2e (114+100+90 = 304 executions = 302 unique tests, zero flakes) ·
35/35 smoke. The screenshots: 16/16 BYTE-IDENTICAL (the same-day-seed
byte-identity law — the carried-over workspace's seed and the shots on
one calendar day, no fresh re-seed, no midnight crossing). The final
seedcheck exact.

D1–D7 docs alignment: AGENTS.md (the v99 paragraph), CLAUDE.md (301 →
302 + the v99 clause at the E2E line's tail), README.md (the counts +
the v99 plan-table row), zero-balance_SKILL.md (Session 134 audit row
+ the state line + the last_updated date), the PAD (v1.1.56), the probe
README (the v99 section + the three lessons + the v100 queue),
session_239.md + the worklog Session 134 entry.

The pre-ship gates: lint green; the staged diff ZERO src/ changes;
`.env.example` verified tracked, clean, codebase-matched.

**v99 parity cycle (Session 134) complete — PIN-ONLY (zero src/
changes), +1 e2e = 302.**

**What was done:** Audited the carried-over workspace (baseline all
green — 301 e2e with one documented-class flake re-run clean, 35
smoke); axe watch no drift; 93rd standing checks (mobile menu working
the 93rd consecutive time, all four reference bugs live, census clean
on the first read); executed the LOGIN + CALCULATOR pair's sixth re-run
(calculator DIFFERENT — every flag DOM-arbitrated [the willUpdate line
the seed-data class, the hover flags the resting-parity class]; login
IDENTICAL; the census reproduces the v87/v93 values exactly; the
close-button finder artifact arbitrated geometrically — **NO NEW CLONE
GAP**); added the **login social-row census pin** (the OR divider +
Google button + rhythm — never pinned before, measured byte-identical
on both sides first, mutation-verified single-axis after the rebuild
discipline; +1 e2e = 302); screenshots 16/16 byte-identical; docs
aligned D1–D7; PIN-ONLY shipped (zero src/ changes).

**Next:** Per the rotation ledger, the v100 cycle targets the v94-era
NETWORTH + DRILL-DOWN pair (now the oldest remaining) — say "continue
v100" to proceed, or request adjustments to this cycle's deliverables.
