#!/usr/bin/env python3
"""align-docs-v136.py — D1-D5 of the v136 docs alignment (the D0 anchor
discipline: every insert/replace anchor verified 1-hit BEFORE any write;
the script refuses and exits non-zero on any anchor miss or multi-hit).
  D1 AGENTS.md — the v136 paragraph appended after the v135 paragraph
  D2 CLAUDE.md — the e2e count 338 -> 339 + the v136 clause appended to
     the e2e enumeration line's end (after the v135 clause)
  D3 README.md — the two test-count lines 338 -> 339 + the v136 plan row
     inserted after the v135 row
  D4 zero-balance_SKILL.md — the state line 108/338/35 -> 108/339/35 +
     the Session 171 row inserted after the Session 170 row
  D5 Project_Architecture_Document.md — the v1.1.93 revision block
     inserted before the v1.1.92 block
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
anchor = "the dev-shots scripts derived v134→v135 with the version-swap-only verification).\n\n"
if one_hit(text, anchor, "AGENTS v135-paragraph tail"):
    v136 = (
        "Reference surfaces pinned by the v136 iteration (`docs/remediation-plan-v136.md`) — "
        "**the re-run cycle's next-oldest candidate (the v130-era NETWORTH + drill-down-DASHBOARD pair — the /networth view + the DASHBOARD's drill-down EXPANDED state at desktop 1280x800, "
        "the v60-era pair's surface family, the pair's TWELFTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136], "
        "the FIFTY-NINTH consecutive queue/ledger agreement — the corrected entries-minus-one convention applied cleanly: the ELEVENTH ordinal recorded in the v130 plan's own header "
        "on its 12-entry bracket [v60 the original, one entry] → v136 = the TWELFTH, no prose/header conflict; the v130 shots header carries the FULL bracket form — the documented verification source)** "
        "+ the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, the v68 dedupe holds) "
        "+ the npm-audit watch at its twenty-seventh re-check (0 VULNERABILITIES --omit=dev — the v110 bump holds: next 16.4.3 + zod 4.6.7; the 16 moderate the accepted dev-only ESLint braces chain) "
        "+ the 130th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, "
        "the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; "
        "the clone's mobile menu VERIFIED WORKING the 130th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). "
        "**The baseline GREEN — THE EMPTY-STATES:85 WATCH ESCALATED TO ITS ROOT CAUSE AND CLOSED** (the RE-PROVISIONED workspace — the v108 provisioning end-to-end [npm ci 354, the zod 4.6.7 extraction intact, BOTH chromium pairs 1200+1243, the .env + db/ + db:push + db:seed, the seedcheck EXACT 7/1850/2235/0/3/2 before any gate]): "
        "the recurrence DETERMINISTIC on this workspace (3/3 — the v135 \"intermittent\" classification disproven), the retained trace captured (the `GET /api/liabilities` with NO Cookie header → 401), "
        "**the ROOT CAUSE verified three ways** (the storageState cookie carries `secure: true` [NODE_ENV=production → src/lib/auth.ts:77]; the installed Playwright 1.63.0 source: `isLocalHostname(hostname) { return hostname === \"localhost\" || hostname.endsWith(\".localhost\"); }` — "
        "**the Secure-cookie exemption is granted ONLY to the \"localhost\" NAME, never the 127.0.0.1 literal the v135 IPv4 pin introduced**; the direct two-host probe: 127.0.0.1 → 401 NO cookie / localhost → 200 cookie attached); "
        "the blast radius exactly ONE test (the suite's only authenticated page.request consumer); **THE FIX (playwright.config.ts — a test-config change, src/ untouched): the webServer env gains `HOSTNAME: \"::\"` [the standalone server.js's own bind knob — DUAL-STACK, verified live: 127.0.0.1 → 200 AND [::1] → 200] + BASE_URL back to `http://localhost:${PORT}`** — "
        "resolving BOTH watch classes at once (the empty-states:85 cookie class AND the not-found:111 resolver-race class — both stacks accept, whichever the resolver picks); the bash-local-HOSTNAME discovery (the sandbox shell sets HOSTNAME but never exports it — `sh -c` sees empty — so the explicit override is deterministic; smoke-test.sh's own explicit-bind precedent); "
        "the full 338 re-verified green under the fix (93+92+74+82 = 341 executions) + the 35/35 smoke; the v135 diagnostic guard retained. "
        "The probe series derived from the v130 lineage (derive-v136-series.py — FOUR explicit session-token families + FOUR history-correction fragments [the era marker last-re-shot v124→v130 + the oldest-remaining list [v124 < … < v129]→[v130 < v131 < v132] — the backlog shrank to three lineages, a within-line edit; the ordinal ELEVENTH→TWELFTH + the bracket extended; the agreement ordinal FIFTY-THIRD→FIFTY-NINTH; the arbit census provenance], "
        "all applied on the FIRST run, zero residual, line counts preserved 84/71/65/328) + the two-half builder (derive-build-twohalf-v136.py — the lesson-range bump v92..v129→v92..v135 + the lineage-note fixup LAST; line-count preserved 84) "
        "+ the comparator (derive-compare-v136.py — the explicit /tmp/vlm130→/tmp/vlm136 log-path swap + the two provenance citations re-pointed at the v130 measurement; line-count preserved 129) "
        "+ the TWO-block two-half contract verified three-way (verify-twohalf-v136.py — ARBIT_A 90 lines md5 f55be05098ed53a8491c317fd2edb4fb + ARBIT_B 111 lines md5 7ed3739995e943621272409caa316e47, byte-identical across the source + both halves — the within-cycle contract; the view-label tokens carry the version, so the digests differ from the v130 cycle's by construction). "
        "**The VLM verdict — NETWORTH IDENTICAL ×2 + DRILL-DOWN DIFFERENT ×2 (the stable-identical-networth form; the v130 inverse-split did not recur); every drill-down flag in the documented classes** "
        "(the nav-highlight v56 superset, the avatar user-identity, the progress-fill pct data, the donut labels the v60 perception class, the slice proportions + legend the seed-data classes, the FAB platform-chrome claim [BOTH directions across the passes] DISPROVEN LIVE by base44-fab-arbit-v136.sh [fabCount 0 + bodyHasBase44 false on BOTH sides, BOTH flagged surfaces, 1280, logged-in], "
        "**the pass-1 NEW stat-card-footer-divider flag DISPROVEN LIVE by statfooter-arbit-v136.sh** [the one-shot both-sides census: the divider DIV h:1 bg:rgb(229,231,227) present on BOTH sides, the row 254×20 flex gap-8px, the trend icons 16×16 identical — the sole deltas the count texts/widths, the seed-count class; the VLM misread the identical chrome — the v130 profilecard misread precedent's class], "
        "the pass-2 \"Total Expense[s]\" title claim a misread [both sides \"Total Expenses\" measured]); the both-sides census **73 axes — 67 identical + 6 documented-class deltas, ZERO new — REPRODUCING the v130 census values EXACTLY** (the same 73/67/6 split, zero drift on every axis). "
        "**A PIN-ONLY cycle for src/ — zero production-code changes (the sixth PIN-ONLY cycle in the last seven) + one e2e pin (338 → 339): the NETWORTH ASSET-CARD KEBAB-TRIGGER's FOCUS-VISIBLE LADDER at 1280** "
        "(the never-pinned keyboard path of the pinned reveal family on the networth file: the v46 F2 at-rest/card-hover, the v124 open, the v130 own-hover, the v132 badge, the v36 S3 on /income a DIFFERENT FILE; the twins net-worth-view.tsx:82/192 carrying focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring focus-visible:opacity-100 held by NO spec at ANY viewport); "
        "the both-sides one-shot census focusnw-arbit-v136.sh (the v130 structural finder + the v134 REAL-Tab walk + the v135 outline axes) measured the ladder **CLEAN — NO GAP** (the visible 1px #0a0a0a ring IDENTICAL both sides; both walks landed after exactly 9 Tabs; the deltas the documented classes: the clone's keyboard-reveal opacity-1 SUPERSET [the reference's trigger stays invisible under keyboard focus], the TW v4 5-slot boxShadow construct [the 0-width leads inert], the transparent-vs-none inert outline); "
        "the pin appended (append-pin-v136.py — the at-rest rung → the REAL-Tab-focused rung {fv true + opacity 1 + THE ring via toContain + outlineStyle none} → the blurred rung; the V94-COLLISION-safe axis set; the first run caught the pin's own missing settle — the v134 discipline's 120ms/450ms transition-opacity settle added, green after the fix); "
        "the pin-sanity mutation (the value-scoped focus-visible:ring-1 → ring-2 on the twins' class string) sole-failure verified live [1 failed + 39 passed in the full networth sweep — the ring axis reads rgb(10,10,10) 0px 0px 0px 2px, exactly the predicted axis; the v46/v124/v130/v132 same-file different-rung pins green]; "
        "restored (git diff src/ = 0 lines) + the FULL REBUILD + the post-restore regression 112 passed (networth 39 + items 51 + calculator 21 + the setup — the v134/v135 pins' different-file immunity verified live). "
        "The ship chain **339 e2e zero flakes** (93+92+75+82 = 342 executions = 339 unique — the count derived authoritatively via --list before any chunk ran; both closed watches green through the chain); 35/35 smoke; "
        "**the screenshots 16/16 — 9 byte-identical + 7 changed (03/04/05/06 + 08 + 16 the SEED-DATE class [the fresh re-seed Oct 31 vs the v135 workspace's Oct 29 seed — every relative isoDate(-N) shifted] + 07 the CROSS-DAY DATE-CLASS refresh [the todayIso default shifted Oct 30 → 31 UTC] — the deterministic union of the v134/v135 re-provisioning classes, the changed set EXACTLY the date-bearing surfaces)**; "
        "the dev evidence 4/4 (3 byte-identical + dev-mobile-income-390 the date-class twin) + VLM-verified (the menu proof: the sheet closed, the heading \"Income\", the top bar + toggle + brand; the dev-shots scripts derived v135→v136 with the version-swap-only verification).\n\n"
    )
    text = text.replace(anchor, anchor + v136)
    io.open(AG, "w", encoding="utf-8").write(text)
    print("D1 AGENTS.md: the v136 paragraph appended")

# ---------- D2: CLAUDE.md ----------
CL = "CLAUDE.md"
text = io.open(CL, encoding="utf-8").read()
if one_hit(text, "E2E (Playwright, 338)", "CLAUDE e2e count"):
    text = text.replace("E2E (Playwright, 338)", "E2E (Playwright, 339)")
    io.open(CL, "w", encoding="utf-8").write(text)
    print("D2a CLAUDE.md: 338 -> 339")
text = io.open(CL, encoding="utf-8").read()
anchor = "the line-138-scoped revert mutation sole-failure verified live [1 failed + 21 passed in the full calculator sweep]; the post-restore regression 89/89)\n"
if one_hit(text, anchor, "CLAUDE v135 clause tail"):
    v136clause = (
        "; the v136 pin — the NETWORTH asset-card kebab trigger's focus-visible ladder at 1280 (the PIN-ONLY form — src/ ZERO changes, the sixth PIN-ONLY cycle in the last seven: "
        "the never-pinned keyboard path of the pinned reveal family on the networth file [the v46 F2 at-rest/card-hover, the v124 open, the v130 own-hover, the v132 badge — the same file; the v36 S3 on /income a DIFFERENT file]; "
        "the both-sides census measured the ladder CLEAN — the 1px #0a0a0a ring identical, both walks landed after exactly 9 Tabs, the deltas the documented superset/construct classes — NO GAP, NO REPAIR; "
        "the at-rest rung → the REAL-Tab-focused rung {fv true + opacity 1 [the keyboard-reveal superset] + the ring via toContain + outlineStyle none} → the blurred rung, the v134 120ms/450ms transition-opacity settle discipline; "
        "the value-scoped ring-1→ring-2 mutation sole-failure verified live [1 failed + 39 passed in the full networth sweep — the ring axis reads 2px, exactly the predicted axis]; the post-restore regression 112/112 "
        "[networth 39 + items 51 + calculator 21 + the setup — the v134/v135 pins' different-file immunity verified live]; the cycle's other seam: the empty-states:85 watch CLOSED — the root cause the Playwright isLocalHostname Secure-cookie asymmetry "
        "[the exemption granted ONLY to the \"localhost\" name, never the 127.0.0.1 literal the v135 IPv4 pin introduced — the deterministic reproduction 3/3, the trace captured, the two-host probe verified], "
        "the fix playwright.config.ts HOSTNAME=\"::\" [dual-stack: 127.0.0.1 → 200 AND [::1] → 200] + BASE_URL back to localhost — BOTH watch classes resolved, the full 338 re-verified green under the fix, then 339 with the pin)\n"
    )
    text = text.replace(anchor, anchor[:-1] + v136clause)
    io.open(CL, "w", encoding="utf-8").write(text)
    print("D2b CLAUDE.md: the v136 clause appended")

# ---------- D3: README.md ----------
RM = "README.md"
text = io.open(RM, encoding="utf-8").read()
if text.count("(338 tests)") == 2:
    text = text.replace("(338 tests)", "(339 tests)")
    io.open(RM, "w", encoding="utf-8").write(text)
    print("D3a README.md: the two count lines 338 -> 339")
text = io.open(RM, encoding="utf-8").read()
anchor = "the dev evidence 4/4 + VLM-verified). |\n"
if one_hit(text, anchor, "README v135 row tail"):
    v136row = (
        "| [`docs/remediation-plan-v136.md`](docs/remediation-plan-v136.md) | **The re-run cycle's next-oldest candidate (the v130-era NETWORTH + drill-down-DASHBOARD pair's TWELFTH re-run — the v60-era pair's surface family, "
        "the FIFTY-NINTH consecutive queue/ledger agreement) + THE EMPTY-STATES:85 WATCH CLOSED (the root cause: Playwright's isLocalHostname grants the Secure-cookie exemption ONLY to the \"localhost\" name — never the 127.0.0.1 literal the v135 IPv4 pin introduced; "
        "the deterministic reproduction 3/3 + the retained trace + the installed-source verification + the two-host probe; the fix: playwright.config.ts HOSTNAME=\"::\" dual-stack bind + BASE_URL back to localhost — BOTH watch classes resolved, the full suite re-verified green) "
        "+ the networth kebab's focus-visible ladder pin at 1280 (PIN-ONLY — src/ zero changes; the census measured the ladder CLEAN: the 1px #0a0a0a ring identical both sides; the ring-1→ring-2 mutation sole-failure verified; the post-restore regression 112/112) "
        "— the 130th standing checks ALL GREEN (the mobile menu the 130th consecutive), the watches green (0 vulnerabilities --omit=dev, axe-core NO DRIFT), the census 73/67/6 reproducing the v130 values EXACTLY, "
        "the VLM NETWORTH IDENTICAL ×2 + DRILL-DOWN DIFFERENT ×2 (every flag in the documented classes; the NEW stat-card-divider flag disproven live), the ship chain 339 e2e zero flakes + 35/35 smoke, "
        "the screenshots 16/16 (9 byte-identical + 7 the deterministic seed-date/cross-day classes), the dev evidence 4/4 + VLM-verified). |\n"
    )
    text = text.replace(anchor, anchor + v136row)
    io.open(RM, "w", encoding="utf-8").write(text)
    print("D3b README.md: the v136 plan row inserted")

# ---------- D4: zero-balance_SKILL.md ----------
SK = "zero-balance_SKILL.md"
text = io.open(SK, encoding="utf-8").read()
if one_hit(text, "108/338/35", "SKILL state line"):
    text = text.replace("108/338/35", "108/339/35")
    io.open(SK, "w", encoding="utf-8").write(text)
    print("D4a SKILL.md: the state line 108/338/35 -> 108/339/35")
text = io.open(SK, encoding="utf-8").read()
anchor = "both flake watches documented — the IPv4 fix in, the empty-states guard in) |\n"
if one_hit(text, anchor, "SKILL Session 170 row tail"):
    s171 = (
        "| 2026-10-31 | Session 171 — parity iteration v136 (`docs/remediation-plan-v136.md`) | **The re-run cycle's next-oldest candidate (the v130-era NETWORTH + drill-down-DASHBOARD pair's TWELFTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136], "
        "the FIFTY-NINTH consecutive queue/ledger agreement) + THE EMPTY-STATES:85 WATCH CLOSED (the ROOT CAUSE: the Secure cookie [NODE_ENV=production] + Playwright's isLocalHostname granting the exemption ONLY to the \"localhost\" name — never the 127.0.0.1 literal the v135 IPv4 pin introduced; "
        "the deterministic reproduction 3/3, the retained trace, the installed-source verification, the two-host probe; THE FIX: playwright.config.ts HOSTNAME=\"::\" dual-stack + BASE_URL back to localhost — both watch classes resolved, the full suite re-verified green) "
        "+ the networth kebab's focus-visible ladder pin at 1280 (PIN-ONLY — src/ ZERO changes; the ladder CLEAN both sides — the 1px #0a0a0a ring identical, both walks 9 Tabs; the ring-1→ring-2 mutation sole-failure verified; the post-restore regression 112/112) "
        "— the 130th standing checks ALL GREEN (the mobile menu the 130th consecutive; the four reference bugs live; the census clean on the FIRST reads), the watches green (0 vulnerabilities --omit=dev — the twenty-seventh; axe-core NO DRIFT), "
        "the census 73 axes — 67 identical + 6 documented, ZERO new (the v130 values reproduced EXACTLY), the VLM NETWORTH IDENTICAL ×2 + DRILL-DOWN DIFFERENT ×2 (every flag documented; the NEW stat-card-divider flag DISPROVEN live; the FAB disproven both directions), "
        "the ship chain 339 e2e zero flakes (342 executions) + 35/35 smoke, the screenshots 16/16 (9 byte-identical + 7 the deterministic date classes), the dev evidence 4/4 + VLM-verified; the workspace the RE-PROVISIONED class (the v108 provisioning end-to-end, the seedcheck EXACT before any gate) |** 108/339/35 green |\n"
    )
    text = text.replace(anchor, anchor + s171)
    io.open(SK, "w", encoding="utf-8").write(text)
    print("D4b SKILL.md: the Session 171 row inserted")

# ---------- D5: Project_Architecture_Document.md ----------
PAD = "Project_Architecture_Document.md"
text = io.open(PAD, encoding="utf-8").read()
anchor = "#### Revision Block — v1.1.92 (Tracked Changes)"
if one_hit(text, anchor, "PAD v1.1.92 block heading"):
    v1193 = (
        "#### Revision Block — v1.1.93 (Tracked Changes)\n"
        "- `[UI]` v1.1.93 (2026-10-31) — the v136 parity iteration (**PIN-ONLY for src/ — zero production-code changes, the sixth PIN-ONLY cycle in the last seven** + one e2e pin; "
        "a test-config change [the playwright.config.ts dual-stack HOSTNAME=\"::\" bind + the BASE_URL return to localhost — the empty-states:85 watch CLOSED with its root cause: Playwright's isLocalHostname grants the Secure-cookie exemption ONLY to the \"localhost\" name, never the 127.0.0.1 literal the v135 IPv4 pin introduced]; "
        "no dependency change): the counts 108 unit / **339 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v130-era NETWORTH + drill-down-DASHBOARD pair's TWELFTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136], the FIFTY-NINTH consecutive queue/ledger agreement)** "
        "+ the networth asset-card kebab trigger's FOCUS-VISIBLE LADDER pin at 1280 (the never-pinned keyboard path of the pinned reveal family on the networth file; the both-sides census measured the ladder CLEAN — the 1px #0a0a0a ring identical, NO GAP, NO REPAIR; "
        "the value-scoped ring-1→ring-2 pin-sanity mutation sole-failure verified live; the post-restore regression 112/112); the 130th standing checks ALL GREEN (the mobile menu the 130th consecutive); "
        "the both-sides census 73 axes — 67 identical + 6 documented-class deltas, ZERO new (the v130 values reproduced EXACTLY); the VLM NETWORTH IDENTICAL ×2 + DRILL-DOWN DIFFERENT ×2 with every flag in the documented classes "
        "(the NEW stat-card-divider flag disproven live by the one-shot both-sides census; the FAB claim disproven in both directions); the ship chain 339 e2e zero flakes + 35/35 smoke; the screenshots 16/16 (9 byte-identical + 7 the deterministic seed-date/cross-day classes); the dev evidence 4/4 + VLM-verified.\n\n"
    )
    text = text.replace(anchor, v1193 + anchor)
    io.open(PAD, "w", encoding="utf-8").write(text)
    print("D5 PAD.md: the v1.1.93 revision block inserted")

print("DONE" if ok else "FAILED — anchor misses above")
sys.exit(0 if ok else 1)
