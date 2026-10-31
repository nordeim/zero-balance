#!/usr/bin/env python3
"""align-probereadme-v136.py — D6 of the v136 docs alignment: insert the
v136 cycle section + the v137 queue into scripts/parity-probes/README.md,
immediately after the v136 queue paragraph (the v135 cycle's own section
form) and before the v121 section. D0 discipline: the insert anchor
verified 1-hit BEFORE any write; the script refuses on any miss."""
import io
import sys

PR = "scripts/parity-probes/README.md"
text = io.open(PR, encoding="utf-8").read()

anchor = (
    "the not-found:111 flake watch (the IPv4-pin fix in —\n"
    "the watch continues for any residual class) + the empty-states:85 fixture\n"
    "watch (the 2nd occurrence precisely diagnosed by the guard; if it recurs,\n"
    "the trace capture + the cookie-attachment root-cause is the documented\n"
    "step).\n"
)
n = text.count(anchor)
if n != 1:
    print(f"ANCHOR MISS (the v136 queue tail): {n} hits")
    sys.exit(1)
# the section goes AFTER the queue's trailing blank line, before the v121 section
insert_after = anchor + "\n"

SECTION = """## The v136 cycle (the v130-era NETWORTH + drill-down pair's TWELFTH re-run — Session 171)

The re-run cadence's next-oldest candidate: the v130-era NETWORTH +
drill-down-DASHBOARD pair — the /networth view + the DASHBOARD's
drill-down EXPANDED state at desktop 1280x800, the v60-era pair's surface
family, last re-shot v130 — now the oldest remaining [v130 < v131 < v132];
the pair's TWELFTH re-run bracket [v60 -> v67 -> v76 -> v82 -> v88 -> v94
-> v100 -> v106 -> v112 -> v118 -> v124 -> v130 -> v136]; the FIFTY-NINTH
consecutive queue/ledger agreement — the surface names verified against
the v130 lineage's own records BEFORE the derivation (the v130 plan's own
header: the ELEVENTH ordinal on its 12-entry bracket [v60 the original,
one entry — no off-by-one this lineage]; the v130 shots header carries
the FULL bracket form — the documented verification source). **A PIN-ONLY
cycle for src/ — zero production-code changes (the sixth PIN-ONLY cycle
in the last seven) + one e2e pin (338 -> 339) + ONE test-config repair**
(the playwright.config.ts dual-stack/localhost form — the cycle's own
headline finding, below); the cycle's standing items: the axe watch (NO
DRIFT — 4.14.0 holds, the v68 dedupe verified), the npm-audit watch at
its twenty-seventh re-check (0 vulnerabilities --omit=dev — the v110
bump holds [next 16.4.3 + zod 4.6.7]; the 16 moderate the accepted
dev-only ESLint braces chain), the 130th standing checks (ALL GREEN —
the reference's four bugs live; the data census clean on the FIRST
reads; the clone's mobile menu VERIFIED WORKING the 130th consecutive
time; zero overflow at 390 on all five views; the seedcheck exact after
the clone half).

The baseline GREEN — **THE EMPTY-STATES:85 WATCH ESCALATED TO ITS ROOT
CAUSE AND CLOSED** (the RE-PROVISIONED workspace — the repo re-cloned
from main @ 4406a3f, the v108 FRESH-CLONE provisioning end-to-end [npm
ci 354 entries, the zod 4.6.7 extraction intact, BOTH chromium pairs
1200 + 1243 installed with INSTALLATION_COMPLETE verified, the explicit-
env-prefix Prisma discipline, the .env [DATABASE_URL="file:../db/custom.
db"] + db/ at the repo root + db:push + db:seed, the seedcheck EXACT
7/1850/2235/0/3/2 before any gate]; lint, typecheck, 108/108 unit, build
[robots + sitemap prerendered], the 4-chunk e2e, 35/35 smoke; the
production-seam audit clean). **The recurrence DETERMINISTIC on this
workspace** (3/3: the chunk run + two isolated reruns — the v135
"intermittent" classification disproven; the v135 diagnostic guard
firing exactly as designed: "liabilities fixture GET must be
authenticated (200) — Expected: true / Received: false"). **The retained
trace captured** (the watch's documented step): the network entry shows
the GET /api/liabilities went out with NO Cookie header -> 401
{"ok":false,"error":"You must be logged in to access this app"} — the
same signature as both v135 occurrences. **THE ROOT CAUSE, verified
three ways**: (1) the storageState cookie carries `secure: true` — the
e2e webServer runs NODE_ENV=production, and setSessionCookie sets
`secure: process.env.NODE_ENV === "production"` (src/lib/auth.ts:77);
(2) the installed Playwright 1.63.0 source (coreBundle.js, the
CookieStore Cookie.matches implementation): `if (this._raw.secure &&
(url3.protocol !== "https:" && !isLocalHostname(url3.hostname))) return
false;` with `isLocalHostname(hostname) { return hostname ===
"localhost" || hostname.endsWith(".localhost"); }` — **the Secure-cookie
exemption is granted ONLY to the "localhost" NAME, never the 127.0.0.1
literal the v135 IPv4 pin introduced**; (3) the direct two-host probe
(scripts/probe-securecookie-v136.mjs — one browser context, one server,
the same Secure cookie): page.request via 127.0.0.1 -> 401 (NO cookie
attached), via localhost -> 200 (cookie attached). The blast radius:
exactly ONE test (the empty-states G6 fixture — the suite's only
authenticated page.request consumer; auth.spec's login POST
intentionally unauthenticated, the not-found SEO pair public routes) —
why the suite was otherwise green and the v135 occurrences looked
intermittent (both occurred AFTER the IPv4 pin went in; the pre-pin
localhost runs could not exhibit the class). **THE FIX (a test-config
change, src/ untouched — playwright.config.ts)**: the webServer env
gains `HOSTNAME: "::"` — the standalone server.js's own bind knob
(`process.env.HOSTNAME || '0.0.0.0'`) — making the listener DUAL-STACK
(verified live: 127.0.0.1:3105 -> 200 AND [::1]:3105 -> 200 AND
localhost:3105 -> 200), and BASE_URL returns to http://localhost:${PORT}
— the name under which (i) Playwright's isLocalHostname grants the
Secure-cookie exemption (the G6 fixture attaches -> 200) and (ii) the
not-found:111 ::1-vs-IPv4 resolver race is dead outright (BOTH stacks
accept, whichever the resolver picks). **The bash-local-HOSTNAME
discovery**: the sandbox shell sets HOSTNAME but never exports it (`env
| grep HOSTNAME` empty, `sh -c 'echo $HOSTNAME'` empty) — so the spawned
server always saw the server.js '0.0.0.0' fallback, and the explicit
override is deterministic; scripts/smoke-test.sh already uses the same
explicit-bind pattern (HOSTNAME="127.0.0.1"). **The verification: the
both-watch-spec file green (empty-states 5/5 x 3 runs + not-found 7/7),
the live playwright-managed server probed dual-stack (IPv4 200 + IPv6
200), and the FULL 338 e2e re-verified green under the fix (93+92+74+82
= 341 executions) + the 35/35 smoke.** The v135 diagnostic guard
retained. **BOTH watch classes CLOSED** (the standing watch continues
for any residual class).

F2 the 130th standing checks ALL GREEN (the pair derived from the v129
pair via the persisted derive-standing-v136.py — three token families,
the 129th->130th th->th plain replace, normalize-back diff clean, zero
old tokens; line counts preserved 119/74): the reference's four bugs all
live [toast-blocker hitIsBurgerChild:false; sheet-trap overlayCount:1
after nav; no-landmark navLandmark:false; the 464px /networth overflow
measured docSW 464 directly]; the data census clean on the FIRST reads;
the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING
the 130th consecutive time (zero overflow at 390 on all five views); the
seedcheck exact after the clone half.

F3 the re-run pair: the probe series derived from the v130 lineage
(derive-v136-series.py — the generic swaps [FOUR explicit session-token
families: refvlm/clonevlm + refar/clonear arbit — the tokens carry '130'
without the 'v' prefix, the v121-cycle stale-session-fix precedent] +
FOUR history-correction families [the era marker last-re-shot v124->v130
+ the oldest-remaining bracket [v124 < ... < v129] -> [v130 < v131 <
v132] — the rotation backlog shrank to three lineages, a within-line
edit preserving the line count; the ordinal ELEVENTH->TWELFTH + the
bracket extended [-> v118 -> v124 -> v130 -> v136]; the agreement
ordinal FIFTY-THIRD->FIFTY-NINTH; the arbit census provenance "the v124
census axes"->"the v130 census axes"], 4/4 applied on the FIRST run,
zero residual, line counts preserved 84/71/65/328 == the v130 lineage
exactly). The two-half builder derived (derive-build-twohalf-v136.py ->
build-twohalf-v136.py — the generic swap + the lesson-range bump
v92..v129->v92..v135 + the lineage-note fixup "the v124-lineage
derivation"->"the v130-lineage derivation" LAST; normalize-back diff
clean, zero residual); the halves built + the TWO-block md5 contract
verified by the direct THREE-WAY python extraction (verify-twohalf-
v136.py — ARBIT_A 90 lines md5 f55be05098ed53a8491c317fd2edb4fb +
ARBIT_B 111 lines md5 7ed3739995e943621272409caa316e47, byte-identical
across the source + both halves — the within-cycle contract; the
view-label tokens carry the version, so the digests differ from the
v130 cycle's by construction). The comparator derived (derive-compare-
v136.py -> compare-v136-census.py — the generic swap [the explicit
/tmp/vlm130->/tmp/vlm136 log-path swap] + the two provenance citations
re-pointed at the v130 measurement [the lineage ordinal v124-era/
ELEVENTH -> v130-era/TWELFTH; the records chain v118/v124 -> v124/v130]).
The resource discipline between every half; both halves + both shot
series first-attempt. **The VLM verdict — NETWORTH IDENTICAL x2 +
DRILL-DOWN DIFFERENT x2 (the stable-identical-networth form — the v130
inverse-split did not recur); every drill-down flag in the documented
classes**: the nav-highlight (the v56 SUPERSET class), the avatar letter
(the USER-IDENTITY class), the progress fill (the PCT data class), the
donut labels (the v60 PERCEPTION class), the donut slice proportions +
legend percentages (the SEED-DATA classes), the FAB claim (the
PLATFORM-CHROME class — claimed in BOTH directions across the two
passes [pass 1: ref-side; pass 2: clone-side], DISPROVEN LIVE by
base44-fab-arbit-v136.sh: fabCount 0 + bodyHasBase44 false on BOTH
sides, BOTH flagged surfaces, 1280, logged-in), **the pass-1 NEW
stat-card-footer-divider flag — DISPROVEN LIVE by statfooter-arbit-
v136.sh** (the one-shot both-sides census: the three stat cards' footer
rows — the divider DIV h:1, bg:rgb(229,231,227) present on BOTH sides,
the row 254x20 flex gap-8px, the trend icons 16x16 in the identical
type colors; the sole deltas the count texts and the count-span widths
[45px vs 52px] — the SEED-COUNT data class; the VLM misread the
identical chrome — the v130 profilecard misread precedent's class), and
the pass-2 "Total Expense vs Total Expense[s]" title claim (a MISREAD —
both sides' third card title measured "Total Expenses" in the same
census). **The both-sides census compared axis-by-axis (compare-v136-
census.py): 73 axes — 67 identical + 6 documented-class deltas, ZERO
new — REPRODUCING the v130 census values EXACTLY** (the same 73/67/6
split, zero drift on every axis). The seedcheck exact after the clone
half.

F4 [PIN-ONLY] — the NETWORTH ASSET-CARD KEBAB-TRIGGER's FOCUS-VISIBLE
LADDER at 1280: the never-pinned KEYBOARD path of the pinned reveal
family on the networth file (the v46 F2 at-rest + CARD-hover reveal at
640/390; the v124 OPEN+parked state at 1280; the v130 OWN-HOVER tint
ladder at 1280; the v132 BADGE own-hover at 390; the v36 S3 the keyboard
reveal on /INCOME — a DIFFERENT FILE [item-card.tsx:139, {fv, opacity}
alone, never the ring]; the v134 the focus ladder on /savings
[item-card.tsx again — the different-file immunity precedent]; the twins
net-worth-view.tsx:82 asset + :192 liability — the identical class
string carrying focus-visible:outline-none focus-visible:ring-1
focus-visible:ring-ring focus-visible:opacity-100 — held by NO spec at
ANY viewport on this file). The both-sides one-shot census focusnw-
arbit-v136.sh (the v130 structural finder [the lg:grid-cols-3 asset
grid -> the first card -> the textless single-svg square button — the
trigger UNLABELLED on the reference, the geometric v107 form; the
landing finder accepts opacity 0 OR 1 so the focused trigger stays
findable mid-walk] + the v134 REAL-Tab walk [FINDER-BOUNDED at 40
stops, NEVER Enter — the menu opens on click/Enter, both out of bounds;
the net-worth kebab flow NEVER safe to probe past the menu open: the
menu's Delete click IS the delete, the v124 rule] + the v135 outline
axes) measured the ladder **CLEAN — NO GAP**: the at-rest rung
IDENTICAL; the FOCUSED rung (BOTH sides landed after exactly 9 Tabs):
REF {fv true, opacity 0 [the trigger stays invisible under keyboard
focus — the reference's own shortcoming], the white-lead + THE 1px
#a0a0a0a ring rgb(10,10,10) 0px 0px 0px 1px + the transparent tail
[3 slots], the transparent 2px outline} vs CLONE {fv true, opacity 1
[the keyboard-reveal SUPERSET], the TW v4 5-slot construct with the
SAME visible ring layer rgb(10,10,10) 0px 0px 0px 1px, outlineStyle
none [the ring replaces the outline]}; the blurred rung IDENTICAL —
**the visible focused chrome byte-identical, the deltas the documented
superset/construct classes**. THE PIN (tests/e2e/networth.spec.ts,
appended by the persisted append-pin-v136.py — the v130 pin's own card
finder [the Share Portfolio h4 -> the rounded-xl card -> the ONLY small
square button] + the v134/v135 REAL-Tab walk): the at-rest rung ->
the REAL-Tab-focused rung {fv true + opacity 1 [the keyboard-reveal
superset] + THE ring via toContain "rgb(10, 10, 10) 0px 0px 0px 1px" +
outlineStyle "none"} -> the blurred rung; the V94-COLLISION-safe axis
set (the end-states alone). The first run caught the pin's own missing
settle (the v134 discipline's 120ms/450ms transition-opacity settle
added; green after the fix); the authoritative --list: 339 in 24 files.
THE PIN-SANITY MUTATION (the value-scoped focus-visible:ring-1 ->
ring-2 on the twins' class string — net-worth-view.tsx:82/192 alone;
the at-rest/hover/open tokens untouched by value scoping; the v134 pin
[item-card.tsx — a different file] + the v36 S3 pin [/income — a
different file, {fv, opacity} alone] + the v124/v130 pins [the open/
hover paths — different rungs of the same family] immune by
construction): the SOLE FAILURE verified live — 1 failed [the pin] +
39 passed in the full networth sweep (the ring axis reads rgb(10,10,10)
0px 0px 0px 2px — exactly the predicted axis); restored (git diff src/
= 0 lines) + the FULL REBUILD + the 112/112 post-restore regression
(networth 39 + items 51 + calculator 21 + the setup — the v134/v135
pins' different-file immunity verified live).

The ship chain: lint, typecheck, 108 unit, 0-vuln audit, **339 e2e
zero flakes (93+92+75+82 = 342 executions = 339 unique, the auditable
split — the count derived authoritatively via --list before any chunk
ran; both closed watches green through the chain)**, 35/35 smoke, **the
screenshots 16/16 — 9 byte-identical + 7 changed (03/04/05/06 + 08 + 16
the SEED-DATE class [the fresh re-seed Oct 31 vs the v135 workspace's
Oct 29 seed — every relative isoDate(-N) shifted; the changed set
EXACTLY the date-bearing surfaces] + 07 the CROSS-DAY DATE-CLASS
refresh [the todayIso default shifted Oct 30 -> 31 UTC] — the
deterministic union of the v134/v135 re-provisioning classes)**, the
dev evidence 4/4 (3 byte-identical + dev-mobile-income-390 the
date-class twin) + VLM-verified (the menu proof: the sheet closed, the
heading "Income", the top bar + toggle + brand; the dev-shots scripts
derived v135->v136 with the version-swap-only verification). The docs
D1-D7 aligned; `.env.example` verified untouched. The v136 probe
lineage persisted (derive-v136-series.py, derive-build-twohalf-v136.py,
derive-compare-v136.py, derive-standing-v136.py, build-twohalf-v136.py,
verify-twohalf-v136.py, compare-v136-census.py, focusnw-arbit-v136.sh,
statfooter-arbit-v136.sh, base44-fab-arbit-v136.sh, probe-securecookie-
v136.mjs, the v130-derived series [vlm-shots-v136.sh, arbit-v136.sh,
ref-arbit-v136.sh, clone-arbit-v136.sh, clone-vlmshots-v136.sh,
vlm-compare-v136.mjs], the 130th standing pair [ref-standing-v130.sh,
standing-checks-v130.sh], capture-dev-shots-v136.mjs,
verify-dev-shots-v136.mjs, append-pin-v136.py, align-docs-v136.py,
align-probereadme-v136.py, worklog-insert-s171.py, seedcheck-v136.ts).
src/ ZERO changes (the PIN-ONLY form); tests/ +1 pin (339 total); the
config playwright.config.ts (the dual-stack HOSTNAME bind + the
localhost BASE_URL — both watch classes closed).

The v137 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence rotates to the next-oldest
candidate after the v130-era NETWORTH + drill-down pair (the v125-era
DASHBOARD pair — the DASHBOARD at desktop 1280x800 FULL-PAGE, last
re-shot v131 — now the oldest remaining [v131 < v132]; the pair's
TWELFTH re-run bracket [v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101
-> v107 -> v113 -> v119 -> v125 -> v131 -> v137] to be verified against
the v131 lineage's own records before the derivation — the v131 plan's
own header records the ELEVENTH ordinal on its 12-entry bracket [v61
the original], consistent, no off-by-one this lineage; the v131 shots
header carries the FULL bracket form, the verification source), (2) the
axe-core watch at its next re-check point (only a 5.x wrapper changes
the calculus), (3) the npm-audit watch at its re-check point (only a
new advisory in the next/zod ranges changes the calculus), (4) the
deferred reference-write censuses (unchanged — out of bounds under the
v46 read-only rule), (5) the residual-class watch (both flake classes
CLOSED by the v136 dual-stack/localhost fix — the watch continues in
the standing form for any NEW class).

"""

text = text.replace(insert_after, insert_after + SECTION)
io.open(PR, "w", encoding="utf-8").write(text)
print("D6 probe README: the v136 section + the v137 queue inserted")
