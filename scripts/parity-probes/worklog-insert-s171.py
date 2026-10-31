#!/usr/bin/env python3
"""worklog-insert-s171.py — D7 of the v136 docs alignment: insert the
Session 171 entry at the top of worklog.md's session log (newest first),
immediately before the Session 170 entry. D0 discipline: the anchor
verified 1-hit BEFORE any write."""
import io
import sys

WL = "worklog.md"
text = io.open(WL, encoding="utf-8").read()

anchor = "## Session 170 — Parity iteration v135"
n = text.count(anchor)
if n != 1:
    print(f"ANCHOR MISS (the Session 170 header): {n} hits")
    sys.exit(1)

ENTRY = """## Session 171 — Parity iteration v136: the re-run cycle's next-oldest candidate (the v130-era NETWORTH + drill-down-DASHBOARD pair's TWELFTH re-run — the corrected entries-minus-one convention applied cleanly) + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — the standing step's twenty-seventh cycle) + the 130th standing checks + THE EMPTY-STATES:85 WATCH CLOSED (the root cause + the dual-stack/localhost test-config fix) + the networth kebab's focus-visible ladder pin at 1280 (PIN-ONLY — src/ zero changes) (2026-10-31)

The v130-era NETWORTH + drill-down-DASHBOARD pair (the /networth view +
the DASHBOARD's drill-down EXPANDED state at desktop 1280x800, the
v60-era pair's surface family, last re-shot v130 — now the oldest
remaining [v130 < v131 < v132]; the pair's TWELFTH re-run bracket [v60
-> v67 -> v76 -> v82 -> v88 -> v94 -> v100 -> v106 -> v112 -> v118 ->
v124 -> v130 -> v136]; the FIFTY-NINTH consecutive queue/ledger
agreement — the corrected entries-minus-one convention applied cleanly,
the ELEVENTH ordinal recorded in the v130 plan's own header on its
12-entry bracket [v60 the original, one entry] with no prose/header
conflict; the v130 shots header carries the FULL bracket form — the
documented verification source).

**A PIN-ONLY cycle for src/ — zero production-code changes (the sixth
PIN-ONLY cycle in the last seven) + one e2e pin (338 -> 339) + ONE
test-config repair** (the playwright.config.ts dual-stack/localhost
form — the empty-states:85 watch closed with its root cause).

The baseline GREEN — **THE EMPTY-STATES:85 WATCH ESCALATED TO ITS ROOT
CAUSE AND CLOSED** (the RE-PROVISIONED workspace — the repo re-cloned
from main @ 4406a3f; the v108 FRESH-CLONE provisioning end-to-end [npm
ci 354, the zod 4.6.7 extraction intact, BOTH chromium pairs 1200 +
1243, the .env [DATABASE_URL="file:../db/custom.db"] + db/ at the repo
root + db:push + db:seed, the seedcheck EXACT 7/1850/2235/0/3/2 before
any gate]; lint, typecheck, 108/108 unit, build [robots + sitemap
prerendered], the 4-chunk e2e, 35/35 smoke; the production-seam audit
clean). The recurrence DETERMINISTIC on this workspace (3/3 — the v135
"intermittent" classification disproven; the v135 diagnostic guard
firing exactly as designed). The retained trace captured (the watch's
documented step): the GET /api/liabilities with NO Cookie header -> 401.
**THE ROOT CAUSE, verified three ways**: the storageState cookie
carries `secure: true` (the e2e webServer runs NODE_ENV=production ->
src/lib/auth.ts:77); the installed Playwright 1.63.0 source —
`isLocalHostname(hostname) { return hostname === "localhost" ||
hostname.endsWith(".localhost"); }` — **grants the Secure-cookie
exemption ONLY to the "localhost" NAME, never the 127.0.0.1 literal
the v135 IPv4 pin introduced**; the direct two-host probe (127.0.0.1 ->
401 NO cookie / localhost -> 200 cookie attached). The blast radius
exactly ONE test (the suite's only authenticated page.request
consumer) — why the suite was otherwise green and the v135 occurrences
looked intermittent (both occurred AFTER the IPv4 pin). **THE FIX
(playwright.config.ts — a test-config change, src/ untouched): the
webServer env gains `HOSTNAME: "::"` (the standalone server.js's own
bind knob — DUAL-STACK, verified live: 127.0.0.1 -> 200 AND [::1] ->
200) + BASE_URL back to `http://localhost:${PORT}`** — resolving BOTH
watch classes at once (the empty-states:85 cookie class AND the
not-found:111 resolver-race class); the bash-local-HOSTNAME discovery
(the sandbox shell sets HOSTNAME but never exports it — the explicit
override deterministic; smoke-test.sh's own explicit-bind precedent);
the full 338 re-verified green under the fix + the 35/35 smoke; the
v135 diagnostic guard retained.

The standing items: the npm-audit watch 0 vulnerabilities (the
twenty-seventh re-check — --omit=dev clean; the v110 bump holds), the
axe-core watch NO DRIFT (4.14.0, the v68 dedupe holds), **the 130th
standing checks ALL GREEN** (the reference's four bugs live; the data
census clean on the FIRST reads; the clone's mobile menu VERIFIED
WORKING the 130th consecutive time, zero overflow at 390 on all five
views; the seedcheck exact after the clone half).

The probe series derived from the v130 lineage (derive-v136-series.py —
FOUR explicit session-token families + FOUR history-correction
fragments [the era marker last-re-shot v124 -> v130 + the
oldest-remaining list [v124 < ... < v129] -> [v130 < v131 < v132] —
the backlog shrank to three lineages, a within-line edit; the ordinal
ELEVENTH -> TWELFTH + the bracket extended; the agreement ordinal
FIFTY-THIRD -> FIFTY-NINTH; the arbit census provenance re-pointed],
all applied on the FIRST run, zero residual, line counts preserved
84/71/65/328) + the two-half builder (the lesson-range bump v92..v129
-> v92..v135 + the lineage-note fixup LAST) + the comparator (the
/tmp/vlm130 -> /tmp/vlm136 log-path swap; the provenance citations
re-pointed at the v130 measurement) + the TWO-block md5 contract
verified three-way (ARBIT_A 90 lines f55be05098ed53a8491c317fd2edb4fb
+ ARBIT_B 111 lines 7ed3739995e943621272409caa316e47 — the
within-cycle contract; the view-label tokens carry the version).
**The VLM verdict — NETWORTH IDENTICAL x2 + DRILL-DOWN DIFFERENT x2
(the stable-identical-networth form); every flag in the documented
classes** — the nav-highlight (v56 superset), the avatar
(user-identity), the progress fill (pct data), the donut labels (the
v60 perception class), the slice proportions + legend (seed data), the
FAB claim (platform-chrome, BOTH directions, DISPROVEN LIVE by
base44-fab-arbit-v136.sh), **the pass-1 NEW stat-card-footer-divider
flag DISPROVEN LIVE by statfooter-arbit-v136.sh** (the divider present
+ byte-identical both sides — the row 254x20, the divider DIV h:1
bg:rgb(229,231,227), the trend icons 16x16 identical; the sole deltas
the count texts — the seed-count class; the VLM misread the identical
chrome), the pass-2 "Total Expense[s]" title claim a misread (both
sides "Total Expenses" measured). The both-sides census **73 axes — 67
identical + 6 documented-class deltas, ZERO new — REPRODUCING the v130
census values EXACTLY** (the same 73/67/6 split, zero drift).

THE PIN — the NETWORTH ASSET-CARD KEBAB-TRIGGER's FOCUS-VISIBLE LADDER
at 1280 (the never-pinned keyboard path of the pinned reveal family on
the networth file: the v46 F2 at-rest/card-hover, the v124 open, the
v130 own-hover, the v132 badge — the same file; the v36 S3 on /income
a DIFFERENT file; the v134 on /savings [item-card.tsx again]; the
twins net-worth-view.tsx:82/192 held by NO spec at ANY viewport). The
both-sides one-shot census focusnw-arbit-v136.sh (the v130 structural
finder + the v134 REAL-Tab walk + the v135 outline axes) measured the
ladder **CLEAN — NO GAP**: the at-rest rung identical; the FOCUSED
rung (both walks landed after exactly 9 Tabs) — REF {fv true, opacity
0 [stays invisible], the white-lead + THE 1px #0a0a0a ring + the
transparent tail, the transparent 2px outline} vs CLONE {fv true,
opacity 1 [the keyboard-reveal superset], the TW v4 5-slot construct
with the SAME visible ring layer rgb(10,10,10) 0px 0px 0px 1px,
outlineStyle none}; the blurred rung identical — **the visible focused
chrome byte-identical, the deltas the documented superset/construct
classes**. The pin appended (append-pin-v136.py — the v130 pin's own
card finder + the v134/v135 REAL-Tab walk; the at-rest rung -> the
REAL-Tab-focused rung {fv true + opacity 1 + THE ring via toContain +
outlineStyle none} -> the blurred rung; the V94-COLLISION-safe axis
set); the first run caught the pin's own missing settle (the v134
discipline's 120ms/450ms transition-opacity settle added; green after
the fix); the authoritative --list: 339 in 24 files. **THE PIN-SANITY
MUTATION** (the value-scoped focus-visible:ring-1 -> ring-2 on the
twins' class string — the different-file/different-rung pins immune):
the SOLE FAILURE verified live — 1 failed [the pin] + 39 passed in the
full networth sweep (the ring axis reads 2px — exactly the predicted
axis); restored (git diff src/ = 0 lines) + the FULL REBUILD + the
112/112 post-restore regression (networth 39 + items 51 + calculator
21 + the setup — the v134/v135 pins' different-file immunity verified
live).

The ship chain 339 e2e zero flakes (93+92+75+82 = 342 executions = 339
unique — the count derived authoritatively via --list before any chunk
ran; both closed watches green through the chain); 35/35 smoke; the
screenshots 16/16 — 9 byte-identical + 7 changed (03/04/05/06 + 08 +
16 the SEED-DATE class [the fresh re-seed Oct 31 vs the v135
workspace's Oct 29 seed] + 07 the CROSS-DAY DATE-CLASS refresh [the
todayIso default shifted Oct 30 -> 31 UTC] — the deterministic union
of the v134/v135 re-provisioning classes, the changed set EXACTLY the
date-bearing surfaces); the dev evidence 4/4 (3 byte-identical +
dev-mobile-income-390 the date-class twin) + VLM-verified (the menu
proof: the sheet closed, the heading "Income", the top bar + toggle +
brand; the dev-shots scripts derived v135 -> v136 with the
version-swap-only verification). The docs D1-D7 aligned; `.env.example`
verified untouched.

---

"""

text = text.replace(anchor, ENTRY + anchor, 1)
io.open(WL, "w", encoding="utf-8").write(text)
print("D7 worklog.md: the Session 171 entry inserted")
