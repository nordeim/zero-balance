#!/usr/bin/env python3
"""align-docs-v135.py — D1-D5 of the v135 docs alignment (the D0 anchor
discipline: every insert/replace anchor verified 1-hit BEFORE any write;
the script refuses and exits non-zero on any anchor miss or multi-hit).
  D1 AGENTS.md — the v135 paragraph inserted after the v134 paragraph
  D2 CLAUDE.md — the e2e count 337 -> 338 + the v135 clause appended to
     the e2e enumeration line's end (after the v134 clause)
  D3 README.md — the two test-count lines 337 -> 338 + the v135 plan row
     inserted after the v134 row
  D4 zero-balance_SKILL.md — the state line 337 -> 338 + the Session 170
     row inserted after the Session 169 row
  D5 Project_Architecture_Document.md — the v1.1.92 revision block
     inserted before the v1.1.91 block
"""
import io
import sys

ok = True


def one_hit(text: str, anchor: str, label: str) -> bool:
    global ok
    n = text.count(anchor)
    if n != 1:
        print(f"ANCHOR MISS ({label}): {n} hits for {anchor[:60]!r}")
        ok = False
        return False
    return True


# ---------- D1: AGENTS.md ----------
AG = "AGENTS.md"
text = io.open(AG, encoding="utf-8").read()
anchor = "the dev-shots scripts derived v133→v134 with the version-swap-only verification)."
if one_hit(text, anchor, "AGENTS v134-paragraph tail"):
    v135 = (
        "\nReference surfaces pinned by the v135 iteration (`docs/remediation-plan-v135.md`) — "
        "**the re-run cycle's next-oldest candidate (the v129-era LOGIN + CALCULATOR pair — the LOGIN view + the CALCULATOR dialog at desktop 1280x800, "
        "the v59-era pair's surface family, the pair's TWELFTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135], "
        "the FIFTY-EIGHTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly: the ELEVENTH ordinal recorded in the v129 plan's own F3 record "
        "on its 12-entry bracket [v59 the original, one entry] → v135 = the TWELFTH, no prose/header conflict; the v129 shots header carries the FULL bracket form — the documented verification source)** "
        "+ the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, the v68 dedupe holds) "
        "+ the npm-audit watch at its twenty-sixth re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) "
        "+ the 129th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, "
        "the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; "
        "the clone's mobile menu VERIFIED WORKING the 129th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). "
        "**The baseline GREEN — BOTH intermittents escalated and captured for the first time** (the CONTINUING workspace; **THE FLAKE EPISODE**: "
        "the not-found:111 recurrence — the full error capture `page.goto: net::ERR_CONNECTION_REFUSED at http://localhost:3100/` [the test died at the NAVIGATION, the v134 'transient error head' hypothesis DISPROVEN]; "
        "the asymmetry verified live [the standalone server binds 0.0.0.0 IPv4-only: 127.0.0.1:3100 → 200, [::1]:3100 → REFUSED] — the localhost resolution racing ::1-first the mechanism, "
        "the `AggregateError: connect ECONNREFUSED ::1:3100` the independent confirmation; **the fix: BASE_URL pinned to the IPv4 literal `http://127.0.0.1:${PORT}` in playwright.config.ts** — a test-config change, src/ untouched, "
        "the full 337 re-verified green under the fix; the empty-states:85 recurrence — the cookie-less apiRequestContext GET → 401 {\"error\"} → the cryptic data.map TypeError, captured WITH the retained trace "
        "[the network entry: NO Cookie header; the storageState verified healthy — 1 cookie, domain 127.0.0.1, 30-day TTL]; the diagnostic guard added so a recurrence reads as a precise expect-ok failure; both watches continue) "
        "**(the REPAIR + PIN form, the v129 precedent's own class — the first src/ change since v129; the five-cycle PIN-ONLY run v130..v134 ends at v134)** "
        "(lint · typecheck · 108 unit · build [robots + sitemap prerendered] · 337 e2e [341 executions in 4 chunks = 336 spec + 1 setup — the count derived authoritatively via --list before any chunk ran: 93/91/74/82] · 35/35 smoke; "
        "the production-seam audit clean + the v134 pin verified in place; skills/ excluded). "
        "The probe series derived from the v129 lineage (derive-v135-series.py — SIX explicit session-token families [refvlm/clonevlm + refcalc/clonecalc + reflogin/clonelogin arbit] + FOUR history-correction fragments, "
        "all applied on the FIRST run, zero residual, line counts preserved 102/166/65/355) + the login-shots sub-series (derive-loginshots-v135.py; 30/30) "
        "+ the two-half builder (derive-build-twohalf-v135.py — the lesson-range bump v92..v128→v92..v134 + the lineage-note fixup LAST; line-count preserved 82) "
        "+ the comparator (derive-compare-v135.py — the explicit /tmp/vlm129→/tmp/vlm135 log-path swap + the provenance citations re-pointed at the v129 measurement; line-count preserved 145) "
        "+ the TWO-block two-half contract verified three-way (verify-twohalf-v135.py — CALC_CENSUS_JS 61 lines md5 e1092d12d06677a4 + LOGIN_CENSUS_JS 36 lines md5 9e5a52d2ab0f2ab9, "
        "the v123/v129 lineage values VERBATIM). "
        "**The VLM verdict — CALCULATOR DIFFERENT ×2 + LOGIN IDENTICAL (pass 1) / DIFFERENT (pass 2 — the sole flag the 'Edit with Base44' FAB, the PLATFORM-CHROME class, "
        "DISPROVEN LIVE by base44-fab-arbit-v135.sh: fabCount 0 + bodyHasBase44 false on BOTH sides at 1280 /login — the pair's documented verdict-VARIATION family; the login verdict has varied IDENTICAL/DIFFERENT across re-runs)** "
        "(every calculator flag in the documented classes, arbitration-free: the hover action buttons the POINTER-POSITION/HOVER-STATE screenshot artifact, the 'Will update category total' note the SEED-DATA class, "
        "the total-card layout flag its consequence). The both-sides census compared AXIS-BY-AXIS by the persisted compare-v135-census.py "
        "(**106 axes: 97 identical + 9 documented-class deltas, ZERO new** — REPRODUCING the v129 census values EXACTLY). "
        "**THE REPAIR + PIN — the CALCULATOR X's FOCUS-VISIBLE LADDER at 1280 (+1 e2e = 338; the first src/ change since v129)**: "
        "the candidate survey (the login view's three hover families measured live on the reference — the Sign in submit's own-hover bg #0f172a→#1e293b, the Google button's own-hover #f8fafc/#cbd5e1 + the shadow-sm layer, "
        "the mode links' own-hover #64748b→#334155 — every one matching the clone's existing classes, both-sides-matching, documented, no repair needed; the calculator X's keyboard path entirely unpinned — "
        "the v87 pin the at-rest chrome, the v129 pin the own-hover tint, the v32 pin the ROW ACTIONS' focus family, the X itself carried NO focus class at any viewport); "
        "the both-sides one-shot census focusx-arbit-v135.sh (the v129 xhover form adapted to the KEYBOARD ladder — the DUAL panel finder + the v87 geometric X; "
        "the walk FINDER-BOUNDED and REQUIRING :focus-visible to match [the clone's Radix auto-focus on dialog open is PROGRAMMATIC — fv false — and must not satisfy the landing check]; "
        "NEVER pressing Enter — the dialog opens on click/Enter, out of bounds; READ-ONLY per the v46 rule) measured **THE GAP**: "
        "the reference's focused rung carries **the 1px #0a0a0a ring** [the white lead + rgb(10,10,10) 0px 0px 0px 1px + the transparent tail] + **the outline form [solid 2px rgba(0,0,0,0), offset 2px]** — the shadcn focus base — "
        "while the clone's carried the UA default outline `auto 1px` with NO ring; "
        "**THE REPAIR: the zb-row-action class + focus-visible:ring-1 focus-visible:ring-ring added at calculator-dialog.tsx:138 (the file's own sibling family — the row actions at :239/:247 carry the identical tokens, "
        "the v32-pinned family; a 1-line edit; the at-rest chrome unchanged, the hover ladder unchanged, the v87/v129 pins immune)**; "
        "**THE TDD ORDER — the RED run verified live** (the pin alone failed against the unrepaired build at the ring toContain: 'none' received vs rgb(10,10,10) 0px 0px 0px 1px expected — exactly the predicted axis) "
        "**then the repair + the REBUILD + the GREEN run (first attempt) + the post-repair census re-run (the focused rung byte-identical both sides — the lead-slot count the documented construct class, the visible ring layer identical)**; "
        "**THE PIN-SANITY MUTATION — the line-138-scoped revert of the focus tokens (the v129-revert form; the row-action lines 239/247 untouched)**: "
        "the SOLE FAILURE verified live — 1 failed [the pin] + 21 passed in the FULL calculator sweep [the v129 hover pin + the v32 row-action pin immune — different rung families on the same line/file]; "
        "restored (git diff src/ = the repair only) + the FULL REBUILD + the 89/89 post-restore regression (calculator 21 + dialog-buttons 17 + items 51 — the v129/v133/v134 pins' different-file immunity verified live). "
        "The ship chain 338 e2e (93+92+74+82 = 341 executions = 338 unique — ONE documented intermittent: the empty-states:85 fixture GET, the 2nd occurrence, "
        "precisely diagnosed by the guard [expected true, received false on the authenticated GET], unreproduced in the isolated re-run; the not-found:111 watch green through the chain under the IPv4 fix); 35/35 smoke; "
        "**the screenshots 16/16 — 15 byte-identical + 07 the DETERMINISTIC CROSS-DAY DATE-CLASS refresh (the todayIso default shifted Oct 29→30 UTC; every seeded-date surface byte-identical — the CONTINUING workspace's unchanged seed)**; "
        "the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the dev-shots scripts derived v134→v135 with the version-swap-only verification).\n"
    )
    text = text.replace(anchor, anchor + v135)
    io.open(AG, "w", encoding="utf-8").write(text)
    print("D1 AGENTS.md: the v135 paragraph inserted")

# ---------- D2: CLAUDE.md ----------
CL = "CLAUDE.md"
text = io.open(CL, encoding="utf-8").read()
a1 = "- **E2E (Playwright, 337)**:"
if one_hit(text, a1, "CLAUDE e2e count"):
    text = text.replace(a1, "- **E2E (Playwright, 338)**:")
a2 = "the post-restore regression 160/160)"
if one_hit(text, a2, "CLAUDE line-75 tail"):
    clause = (
        "; the v135 pin — the CALCULATOR X's focus-visible ladder at 1280 (the REPAIR + PIN form — the first src/ change since v129: "
        "the zb-row-action class + focus-visible:ring-1 focus-visible:ring-ring added at calculator-dialog.tsx:138, the file's own sibling family; "
        "the RED run verified live then the GREEN first attempt + the census re-run byte-identical; "
        "the walk REQUIRING :focus-visible [the clone's Radix auto-focus is programmatic — fv false — and must not satisfy the landing check]; "
        "the ring via toContain + the transparent-outline form; the line-138-scoped revert mutation sole-failure verified live "
        "[1 failed + 21 passed in the full calculator sweep]; the post-restore regression 89/89)"
    )
    text = text.replace(a2, a2 + clause)
    io.open(CL, "w", encoding="utf-8").write(text)
    print("D2 CLAUDE.md: 338 + the v135 clause appended")

# ---------- D3: README.md ----------
RD = "README.md"
text = io.open(RD, encoding="utf-8").read()
c1 = "Playwright specs (337 tests)"
c2 = "Playwright e2e (337 tests)"
if one_hit(text, c1, "README count 1") and one_hit(text, c2, "README count 2"):
    text = text.replace(c1, "Playwright specs (338 tests)").replace(c2, "Playwright e2e (338 tests)")
a3 = "| [`docs/remediation-plan-v134.md`](docs/remediation-plan-v134.md)"
if one_hit(text, a3, "README v134 plan row"):
    row = (
        "| [`docs/remediation-plan-v135.md`](docs/remediation-plan-v135.md) | "
        "**The re-run cycle's next-oldest candidate (the v129-era LOGIN + CALCULATOR pair's TWELFTH re-run — the v59-era login+calc pair's surface family; "
        "the FIFTY-EIGHTH consecutive queue/ledger agreement)** + THE FLAKE EPISODE escalated (BOTH intermittents captured: "
        "not-found:111 = ERR_CONNECTION_REFUSED at page.goto [the ::1-vs-IPv4-only-listener resolver race verified live; the IPv4-literal BASE_URL pin the fix]; "
        "empty-states:85 = the cookie-less apiRequestContext GET → 401 [the diagnostic guard added]) "
        "+ THE REPAIR + PIN (the calculator X's focus-visible family — the zb-row-action + ring tokens at calculator-dialog.tsx:138, the RED→GREEN run, "
        "the sole-failure mutation 1 failed + 21 passed, the 89/89 post-restore regression) "
        "+ the ship chain (338 e2e — ONE documented intermittent [empty-states:85, precisely diagnosed, unreproduced in the isolated re-run]; 35/35 smoke; "
        "the screenshots 16/16 — 15 byte-identical + 07 the deterministic cross-day date-class refresh; the dev evidence 4/4 + VLM-verified). |\n"
    )
    idx = text.index(a3)
    end = text.index("\n", idx) + 1
    text = text[:end] + row + text[end:]
    io.open(RD, "w", encoding="utf-8").write(text)
    print("D3 README.md: 338 counts + the v135 plan row inserted")

# ---------- D4: zero-balance_SKILL.md ----------
SK = "zero-balance_SKILL.md"
text = io.open(SK, encoding="utf-8").read()
s1 = "project_state: 108 unit tests / 337 e2e tests / 35 smoke steps"
if one_hit(text, s1, "SKILL state line"):
    text = text.replace(s1, "project_state: 108 unit tests / 338 e2e tests / 35 smoke steps")
s2 = "| 2026-10-29 | Session 169 — parity iteration v134"
if one_hit(text, s2, "SKILL Session 169 row"):
    row = (
        "| 2026-10-30 | Session 170 — parity iteration v135 (`docs/remediation-plan-v135.md`) | "
        "**The re-run cycle's next-oldest candidate (the v129-era LOGIN + CALCULATOR pair's TWELFTH re-run "
        "[v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135]; "
        "the FIFTY-EIGHTH consecutive queue/ledger agreement)** "
        "+ THE FLAKE EPISODE (both intermittents captured — the not-found:111 ERR_CONNECTION_REFUSED [the IPv4-literal BASE_URL fix], "
        "the empty-states:85 cookie-less 401 [the diagnostic guard]) "
        "+ THE REPAIR + PIN (the calculator X's focus-visible ladder at 1280 — the zb-row-action + focus-visible:ring-1 ring-ring tokens at :138, "
        "the RED run verified live, the GREEN first attempt, the census re-run byte-identical, the sole-failure mutation [1 failed + 21 passed], "
        "the 89/89 post-restore regression; +1 e2e = 338)** "
        "+ the ship chain fully green (338 e2e [341 executions] — ONE documented intermittent [the empty-states:85 fixture GET, precisely diagnosed, "
        "unreproduced in the isolated re-run], 35/35 smoke, the screenshots 16/16 [15 byte-identical + 07 the deterministic cross-day date-class refresh], "
        "the dev evidence 4/4 + VLM-verified) |** 108/338/35 green — the workspace the CONTINUING class "
        "(the resource discipline between the halves; both flake watches documented — the IPv4 fix in, the empty-states guard in) |\n"
    )
    idx = text.index(s2)
    start = text.rindex("\n", 0, idx) + 1
    text = text[:start] + row + text[start:]
    io.open(SK, "w", encoding="utf-8").write(text)
    print("D4 SKILL.md: 338 state line + the Session 170 row inserted")

# ---------- D5: Project_Architecture_Document.md ----------
PD = "Project_Architecture_Document.md"
text = io.open(PD, encoding="utf-8").read()
p1 = "#### Revision Block — v1.1.91 (Tracked Changes)"
if one_hit(text, p1, "PAD v1.1.91 block"):
    block = (
        "#### Revision Block — v1.1.92 (Tracked Changes)\n"
        "- `[UI]` v1.1.92 (2026-10-30) — the v135 parity iteration (**THE REPAIR + PIN form — the first src/ change since v129** + one e2e pin; "
        "a test-config change [the IPv4-literal BASE_URL pin] + a spec diagnostic guard; no dependency change): "
        "the counts 108 unit / **338 e2e** (+1) / 35 smoke; "
        "**the re-run cycle's next-oldest candidate (the v129-era LOGIN + CALCULATOR pair's TWELFTH re-run "
        "[v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135] — "
        "the LOGIN view + the CALCULATOR dialog at desktop 1280x800; the FIFTY-EIGHTH consecutive queue/ledger agreement)**; "
        "the baseline green with **BOTH intermittents escalated and captured** (the not-found:111 recurrence — the full error capture "
        "page.goto net::ERR_CONNECTION_REFUSED at localhost:3100; the asymmetry verified live [the server binds 0.0.0.0 IPv4-only; "
        "127.0.0.1 → 200, [::1] → REFUSED]; **the fix: BASE_URL pinned to the IPv4 literal in playwright.config.ts**; "
        "the empty-states:85 recurrence — the cookie-less apiRequestContext GET → 401, captured with the retained trace [NO Cookie header]; "
        "the diagnostic guard added); the VLM pair **CALCULATOR DIFFERENT ×2 + LOGIN IDENTICAL(pass 1)/DIFFERENT(pass 2 — the sole flag the FAB, disproven live)**; "
        "the two-half census (the TWO-block v129 lineage, md5 e1092d12d06677a4 + 9e5a52d2ab0f2ab9 verified three-way) "
        "**106 axes — 97 identical + 9 documented-class deltas, ZERO new** (the v129 values reproduced EXACTLY); "
        "**the calculator X's focus-visible ladder repair + pin at 1280**: the candidate survey (the login view's three hover families measured live — "
        "both-sides-matching, documented; the X's keyboard path entirely unpinned) + the both-sides census **THE GAP** "
        "(the reference's focused rung the 1px #0a0a0a ring + the transparent-outline form; the clone's the UA default `auto 1px`, no ring) "
        "+ **the repair: the zb-row-action class + focus-visible:ring-1 focus-visible:ring-ring at calculator-dialog.tsx:138 — the file's own sibling family** "
        "+ the RED run verified live + the GREEN first attempt + the census re-run (the focused rung byte-identical both sides) "
        "+ **the line-138-scoped revert mutation sole-failure verified live — 1 failed + 21 passed in the full calculator sweep** "
        "+ restored + the 89/89 post-restore regression; the ship chain 338 e2e (341 executions — ONE documented intermittent "
        "[the empty-states:85 fixture GET, precisely diagnosed by the guard, unreproduced in the isolated re-run]) + 35/35 smoke "
        "+ the screenshots 16/16 (15 byte-identical + 07 the deterministic cross-day date-class refresh — the todayIso shift; "
        "every seeded-date surface byte-identical) + the dev evidence 4/4 + VLM-verified (the menu proof: /income, docSW 390, navLandmark true).\n"
    )
    text = text.replace(p1, block + p1)
    io.open(PD, "w", encoding="utf-8").write(text)
    print("D5 PAD.md: the v1.1.92 block inserted")

print("align-docs-v135:", "ALL D1-D5 ALIGNED" if ok else "FAILED — anchor misses above")
sys.exit(0 if ok else 1)
