#!/usr/bin/env python3
"""Align the docs for the v124 cycle (Session 159).

D1  AGENTS.md     — the v124 paragraph appended after the v123 paragraph
D2  CLAUDE.md     — the E2E count 326 -> 327 + the v124 clause
D3  README.md     — the count strings 326 -> 327 (two places) + the v124
                    plan row appended after the v123 row
D4  SKILL.md      — project_state 326 -> 327 + the Session 159 row appended
                    after the Session 158 row
D5  PAD           — the [UI] v1.1.81 revision block (inserted newest-first,
                    before the v1.1.80 block)
D6  probe README  — the v124 section (after the v123 section) + the v125 queue
D7  session_304.md + the worklog Session 159 entry (separate steps)

D0 checked clean: the v123 paragraph's tail anchor ('re-cloned from main @
cbc38e9' + the provisioning tail) verified appearing exactly ONCE in
AGENTS.md — no duplication, the v119-defect class checked and absent.
"""
import sys

def replace1(path, old, new):
    t = open(path, encoding="utf-8").read()
    n = t.count(old)
    if n != 1:
        print(f"AMBIGUOUS/MISS in {path}: {n} hits for {old[:60]!r}")
        return False
    open(path, "w", encoding="utf-8").write(t.replace(old, new))
    return True

def insert_after(path, anchor, content, marker):
    t = open(path, encoding="utf-8").read()
    if marker in t:
        print(f"ALREADY APPLIED: {path} — {marker[:40]!r}")
        return True
    n = t.count(anchor)
    if n != 1:
        print(f"AMBIGUOUS/MISS in {path}: {n} hits for anchor {anchor[:60]!r}")
        return False
    open(path, "w", encoding="utf-8").write(t.replace(anchor, anchor + content))
    return True

ok = True

# ---------------- D1: AGENTS.md ----------------
V124_AGENTS = """

Reference surfaces pinned by the v124 iteration (`docs/remediation-plan-v124.md`) — **the re-run cycle's next-oldest candidate (the v118-era NETWORTH + drill-down-DASHBOARD pair — the /networth view + the dashboard drill-down EXPANDED state at desktop 1280x800, the v60-era pair's surface family, the pair's TENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124], the FORTY-SEVENTH consecutive queue/ledger agreement — THE QUEUE PROSE'S ORDINAL OFF-BY-ONE CAUGHT BY THE HEADER VERIFICATION: the prose named "the ELEVENTH re-run" expecting "the v118 header's own TENTH ordinal... consistent with its 11-entry bracket", but vlm-shots-v118.sh's own header reads "The pair's NINTH re-run [v60 → … → v118]" — a 10-ENTRY bracket; the ordinal chain verified BACKWARDS [v106 SEVENTH → v112 EIGHTH → v118 NINTH] before the derivation — the lineage carries NO off-by-one, the prose does; v124 = the TENTH by the same convention that made v123 the TENTH from v117's NINTH, the surface unaffected)** + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only the canary 4.14.0-canary.6b52b84 prerelease beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds — one node_modules/axe-core entry verified live; the engine-contract pin green) + the npm-audit watch at its fifteenth re-check (0 VULNERABILITIES — the v110 bump holds: next 16.4.3 + zod 4.6.7) + the 118th standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads [1 items USD 25,000 / 1 items USD 5000.00 / 4 items USD 525.00]; the SEO pair live both sides; the clone's mobile menu VERIFIED WORKING the 118th consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). **The baseline FULLY GREEN ON THE FIRST CHAIN — zero repairs this cycle** (lint · typecheck · 108 unit · build · 326 e2e zero flakes [329 executions in 4 chunks] · 35/35 smoke; the v122 date-axis repair verified holding; the production-seam audit clean; the post-push commits audited session-log-only). **The verdict NETWORTH IDENTICAL ×2 / DRILL-DOWN DIFFERENT ×2 (the consistent form — no variation this cycle)** — every DRILL-DOWN flag DOM-arbitrated: the "Dashboard nav highlighted (green background) in the clone" the v56 SUPERSET delta + the PERCEPTION class (the census: navHighlight bg `rgba(0,0,0,0)` transparent on BOTH sides, no green anywhere — the color/fw asymmetry [ref zinc-600/400 vs clone white/500] the documented superset delta, the reference's own shortcoming); the avatar U-vs-D the USER-IDENTITY class; the progress 30.5%-vs-62.8% the PCT data class (fillW 173-vs-357, the track+gradient byte-identical); the donut labels "missing in the reference" the EACH-SITE'S-DATA + perception class (count 4 / labelFs 16px / sectors 3 byte-identical BOTH sides — the reference DOES render its 92.3/4.6/3.1 labels; the VLM's "missing" a small-slice perception artifact); the stat-card trend icons "slightly different stroke paths" the v67 PATH-SIGNATURE misread (the glyphSig `<polyline points="22 7 13.5 15.5 8.5 10.5 2 17">` byte-identical both sides); the networth group headers/cards the SEED-DATA class (the reference's 1-asset data vs the clone's dev seed). The both-sides census (the TWO blocks — ARBIT_A 90 lines + ARBIT_B 111 lines, md5 b4ba7fe7/dfb1a1df — byte-identical across the halves, the contract verified by direct python extraction [verify-twohalf-v124.py]; built two-half by build-twohalf-v124.py, derived from build-twohalf-v118.py with the lesson-range bump v92..v123 + the lineage-note fixup) compared AXIS-BY-AXIS by the persisted compare-v124-census.py (**73 axes: 67 identical + 6 documented-class deltas, ZERO new** — REPRODUCING the v106/v112/v118 census values EXACTLY, the same 73/67/6 split, zero drift on every axis: the navHighlight.color/fw v56 superset, the avatarLetter user-identity, the progress.fillW pct, the donutLabels.texts each-site's-data, the labelBlock.w v82 data-conditional width ["$25,000.00" 304px vs "-$245,950.00" 357px]). **THE PIN — the NETWORTH asset-card kebab-trigger's OPEN-MENU reveal census at 1280 (PIN-ONLY — the reveal family's open path on the never-pinned networth file, +1 e2e = 327)**: the reveal family's OPEN path (`data-[state=open]:opacity-100`, superset fix #7's "stays revealed while its menu is open" clause) was pinned ONLY on the SAVINGS item-card (the v122 pin, item-card.tsx:139) — the networth twins (net-worth-view.tsx:82 asset + :192 liability) held by NO spec (the v46 census holds the networth kebab's at-rest + hover rungs only; the networth spec's `data-state` assertions are the TABS', never the menu trigger; the v122 cycle's own mutation proved the file-scoped immunity). The CLONE-ONLY form (the v46 F3 + v122 twin precedent: the reference's trigger stays INVISIBLE when its menu opens — its own superset-#7 bug — and the reference's net-worth kebab flow is NEVER safe to probe past the menu open); the family chrome = the v122 pinned contract BY CONSTRUCTION (the identical class strings). The one-shot census (`kebabopen-arbit-v124.sh` — the reveal ladder, measured cleanly on the FIRST run): the hover rung 1 → the at-rest {opacity "0"/closed/36×36/6px/transparent/rgb(10,10,10)/insets 21/21} → **THE OPEN+PARKED READ {opacity "1" / dataState "open" / the unchanged box chrome}** → the fixture-restore dismissed (no menuitem ever clicked). **THE PIN-SANITY MUTATION'S CONDITIONAL-FORM DISCOVERY (the cycle's live-red lesson)**: the v122 UNCONDITIONAL form (`→ opacity-90`) reddens the v46 at-rest census TOO on this surface — the unconditional token beats `opacity-0` in the Tailwind utilities cascade (same specificity, later in the property-group order), leaking the at-rest state to 0.9; the v122 form worked only because the items file holds NO at-rest assertion for the item-card kebab, while the networth file DOES (the v46 census, networth.spec.ts:1084); the CORRECTED CONDITIONAL form (`data-[state=open]:opacity-100` → `data-[state=open]:opacity-90`, the conditionality preserved) isolates the open path alone — **the SOLE FAILURE verified live: the pin ALONE red at the open+parked opacity axis ("1"→"0.9", the deep-equality diff the SINGLE opacity line), the full networth file's 36 others green, the items file 48/48 green (the v122 pin's different-file immunity re-verified)**; restored + the full rebuild + the 37/37 post-restore regression. The ship chain 327 e2e zero flakes (88+86+74+82 = 330 executions = 327 unique); 35/35 smoke; **the screenshots 15/16 byte-identical + 1 DAY-ROLLOVER REFRESH (07-add-item-modal.png — the CAPTURE-DAY-DEPENDENT class: the dialog's date input defaults to todayIso(), the one surface in the 16-shot catalog that follows the CAPTURE day rather than the seed day; the committed shot same-day with the Oct 26 v123 capture, the re-capture shows Oct 27; the pixel pre-analysis 234/5,184,000 pixels in a single 16×22 bbox — the date digits alone — + the VLM verification: date-only, zero chrome drift; the refreshed shot committed)**; the dev evidence 4/4 captured + VLM-verified (byte-identical; the menu proof: /income, docSW 390, navLandmark true — the dev-shots scripts derived v123→v124 with the version-swap-only verification; the stale dev-server LOCK reaped — a hung next-server held .next/dev/lock with its listening socket already dead, the port-scan reaper missed it, the PID-direct kill the fix). The workspace the CARRIED-OVER class (the v123 environment persisted between the cycles — the repo refreshed via git pull, main @ 333c2cb; NO re-provisioning needed: the zod extraction verified intact [840/840], BOTH v1243 playwright pairs verified in the cache directly, the `.env` + `db/` in place, the seedcheck exact before any gate)."""
ok = ok and insert_after("AGENTS.md",
             "the repo re-cloned from main @ cbc38e9; the v108 FRESH-CLONE provisioning end-to-end: npm ci in the foreground [354 entries, the zod extraction verified intact 840/840], BOTH v1243 playwright pairs installed with INSTALLATION_COMPLETE verified [the fresh cache held only the old chromium-1200 pair], the explicit-env-prefix Prisma discipline, the seedcheck exact before any gate).",
             V124_AGENTS,
             "Reference surfaces pinned by the v124 iteration")

# ---------------- D2: CLAUDE.md ----------------
ok = ok and replace1("CLAUDE.md",
    "- **E2E (Playwright, 326)**:",
    "- **E2E (Playwright, 327)**:")
ok = ok and insert_after("CLAUDE.md",
    "the pin-sanity p-3→p-4 line-scoped mutation sole-failure verified live, the 19 others green)",
    "; the v124 pin — the networth asset-card kebab-trigger's OPEN-MENU reveal census at 1280: the reveal family's open path on the never-pinned networth file (the v122 pin's different-file twin — net-worth-view.tsx:82/192 by identical class strings; the open+parked opacity-1 axis with the pointer off the card + the unchanged 36×36 box chrome; the pin-sanity CONDITIONAL mutation [data-[state=open]:opacity-100→opacity-90] sole-failure verified live — the v122 unconditional form leaks into the at-rest state where the v46 census asserts it, the Tailwind utilities-cascade lesson; the 36 others green)",
    "the v124 pin — the networth asset-card kebab-trigger's OPEN-MENU reveal census")

# ---------------- D3: README.md ----------------
ok = ok and replace1("README.md",
    "Playwright specs (326 tests) + global setup",
    "Playwright specs (327 tests) + global setup")
ok = ok and replace1("README.md",
    "Playwright e2e (326 tests) — needs `npm run build` first",
    "Playwright e2e (327 tests) — needs `npm run build` first")
V124_ROW = """| [`docs/remediation-plan-v124.md`](docs/remediation-plan-v124.md) | **The re-run cycle's next-oldest candidate (the v118-era NETWORTH + drill-down-DASHBOARD pair's TENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124] — the /networth view + the dashboard drill-down at desktop 1280x800; the FORTY-SEVENTH consecutive queue/ledger agreement — THE QUEUE PROSE'S ORDINAL OFF-BY-ONE caught by the header verification: the prose said ELEVENTH, the v118 header's own NINTH/10-entry bracket makes v124 the TENTH, the chain verified backwards v106→v112→v118)** + the axe watch (NO DRIFT — 4.14.0 holds) + the npm-audit watch (0 vulnerabilities, fifteenth re-check) + the 118th standing checks (ALL GREEN — the mobile menu the 118th consecutive pass) + the networth kebab-trigger OPEN-MENU reveal census pin at 1280 (PIN-ONLY — +1 e2e = 327; the reveal family's open path on the never-pinned networth file, the v122 twin; the CONDITIONAL-form mutation discovery — the unconditional v122 form leaks into the at-rest state where the v46 census asserts it) + the baseline fully green on the first chain (the CARRIED-OVER workspace — no re-provisioning needed) + the screenshots 15/16 byte-identical + 1 day-rollover refresh (the add-item modal's capture-day date input, VLM-verified date-only). |
"""
ok = ok and insert_after("README.md",
    "the baseline fully green on the first chain (the v122 date-axis repair holding). |",
    "\n" + V124_ROW,
    "docs/remediation-plan-v124.md")

# ---------------- D4: zero-balance_SKILL.md ----------------
ok = ok and replace1("zero-balance_SKILL.md",
    "project_state: 108 unit tests / 326 e2e tests / 35 smoke steps — all green",
    "project_state: 108 unit tests / 327 e2e tests / 35 smoke steps — all green")
S159_ROW = """| 2026-10-27 | Session 159 — parity iteration v124 (`docs/remediation-plan-v124.md`) | **The re-run cycle's next-oldest candidate (the v118-era NETWORTH + drill-down-DASHBOARD pair's TENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124] — the /networth view + the dashboard drill-down at 1280x800; the FORTY-SEVENTH consecutive queue/ledger agreement — the queue prose's ORDINAL OFF-BY-ONE caught by the header verification [the prose said ELEVENTH; the v118 header's own NINTH/10-entry bracket makes v124 the TENTH])** + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — fifteenth re-check) + the 118th standing checks (ALL GREEN — the reference's four bugs live, the mobile menu the 118th consecutive pass, zero overflow at 390) + the VLM pair (NETWORTH IDENTICAL ×2 / DRILL-DOWN DIFFERENT ×2 — every flag DOM-arbitrated: the nav-highlight v56 superset + perception, the avatar user-identity, the progress pct, the donut labels data+perception, the trend-icons v67 misread, the networth groups seed-data) + the two-half census (73 axes — 67 identical + 6 documented, ZERO new — the v106/v112/v118 values reproduced EXACTLY) + the networth kebab-trigger OPEN-MENU reveal census pin at 1280 (PIN-ONLY — the reveal family's open path on the never-pinned networth file, the v122 twin; the CONDITIONAL-form mutation discovery [the unconditional form leaks into the at-rest state where the v46 census asserts it — the Tailwind cascade lesson]; the sole-failure mutation verified live; +1 e2e = 327) + the ship chain fully green (327 e2e zero flakes [330 executions], 35/35 smoke, the screenshots 15/16 byte-identical + 1 day-rollover refresh [the add-item modal's capture-day date input — 234 pixels in a 16×22 bbox, VLM-verified date-only], the dev evidence 4/4 byte-identical + VLM-verified) |** 108/327/35 green — the workspace the CARRIED-OVER class (git pull, no re-provisioning) |
"""
ok = ok and insert_after("zero-balance_SKILL.md",
    "108/326/35 green — the workspace the RESET class (re-cloned from main @ cbc38e9) |",
    "\n" + S159_ROW,
    "Session 159 — parity iteration v124")

# ---------------- D5: Project_Architecture_Document.md ----------------
V1181_BLOCK = """#### Revision Block — v1.1.81 (Tracked Changes)
- `[UI]` v1.1.81 (2026-10-27) — the v124 parity iteration (**PIN-ONLY — zero production-code changes** + one e2e pin; no dependency change): the counts 108 unit / **327 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v118-era NETWORTH + drill-down-DASHBOARD pair's TENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124] — the /networth view + the dashboard drill-down at desktop 1280x800; the FORTY-SEVENTH consecutive queue/ledger agreement; THE QUEUE PROSE'S ORDINAL OFF-BY-ONE caught by the header verification — the v118 header's own NINTH/10-entry bracket makes v124 the TENTH, the chain verified backwards)**; the baseline fully green on the first chain (the CARRIED-OVER workspace — no re-provisioning); the VLM pair NETWORTH IDENTICAL ×2 / DRILL-DOWN DIFFERENT ×2 (every flag DOM-arbitrated — the nav-highlight v56 superset + perception, the avatar user-identity, the progress pct, the donut labels data+perception, the trend-icons v67 path-signature misread, the networth groups seed-data); the two-half census **73 axes — 67 identical + 6 documented-class deltas, ZERO new** (the v106/v112/v118 values reproduced EXACTLY); **THE PIN — the networth asset-card kebab-trigger's OPEN-MENU reveal census at 1280** (the reveal family's open path on the never-pinned networth file — the v122 pin's different-file twin, net-worth-view.tsx:82/192 by identical class strings; the open+parked opacity-1 axis + the unchanged 36×36 box chrome; the clone-only form — the reference's trigger stays invisible when its menu opens, its own superset-#7 bug; **the CONDITIONAL-form mutation discovery: the unconditional v122 form leaks into the at-rest state where the v46 census asserts it — the Tailwind utilities-cascade lesson**; the sole-failure mutation verified live); the ship chain 327 e2e zero flakes (330 executions in 4 chunks) + 35/35 smoke + the screenshots 15/16 byte-identical + 1 day-rollover refresh (the add-item modal's capture-day date input — 234 pixels in a 16×22 bbox, VLM-verified date-only, zero chrome drift) + the dev evidence 4/4 (the menu proof: /income, docSW 390, navLandmark true).
"""
if True:
    t = open("Project_Architecture_Document.md", encoding="utf-8").read()
    if "#### Revision Block — v1.1.81" not in t:
        old = "#### Revision Block — v1.1.80 (Tracked Changes)"
        n = t.count(old)
        if n != 1:
            print(f"D5 AMBIGUOUS: {n} hits")
            ok = False
        else:
            open("Project_Architecture_Document.md", "w", encoding="utf-8").write(
                t.replace(old, V1181_BLOCK + old))
            print("D5: v1.1.81 block inserted (newest-first)")
    else:
        print("D5: v1.1.81 block already present")

print("ALIGN RESULT:", "OK" if ok else "FAIL")
sys.exit(0 if ok else 1)
