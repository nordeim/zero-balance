#!/usr/bin/env python3
"""Insert the Session 159 row into zero-balance_SKILL.md (the D4 second
half — the state line already landed; this script is idempotent)."""
import sys

t = open("zero-balance_SKILL.md", encoding="utf-8").read()
if "Session 159 — parity iteration v124" in t:
    print("ALREADY APPLIED")
    sys.exit(0)

anchor = "108/326/35 green — the workspace the RESET class (re-cloned from main @ cbc38e9) |"
n = t.count(anchor)
if n != 1:
    print(f"AMBIGUOUS: {n} hits")
    sys.exit(1)

S159_ROW = """
| 2026-10-27 | Session 159 — parity iteration v124 (`docs/remediation-plan-v124.md`) | **The re-run cycle's next-oldest candidate (the v118-era NETWORTH + drill-down-DASHBOARD pair's TENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124] — the /networth view + the dashboard drill-down at 1280x800; the FORTY-SEVENTH consecutive queue/ledger agreement — the queue prose's ORDINAL OFF-BY-ONE caught by the header verification [the prose said ELEVENTH; the v118 header's own NINTH/10-entry bracket makes v124 the TENTH])** + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — fifteenth re-check) + the 118th standing checks (ALL GREEN — the reference's four bugs live, the mobile menu the 118th consecutive pass, zero overflow at 390) + the VLM pair (NETWORTH IDENTICAL ×2 / DRILL-DOWN DIFFERENT ×2 — every flag DOM-arbitrated: the nav-highlight v56 superset + perception, the avatar user-identity, the progress pct, the donut labels data+perception, the trend-icons v67 misread, the networth groups seed-data) + the two-half census (73 axes — 67 identical + 6 documented, ZERO new — the v106/v112/v118 values reproduced EXACTLY) + the networth kebab-trigger OPEN-MENU reveal census pin at 1280 (PIN-ONLY — the reveal family's open path on the never-pinned networth file, the v122 twin; the CONDITIONAL-form mutation discovery [the unconditional form leaks into the at-rest state where the v46 census asserts it — the Tailwind cascade lesson]; the sole-failure mutation verified live; +1 e2e = 327) + the ship chain fully green (327 e2e zero flakes [330 executions], 35/35 smoke, the screenshots 15/16 byte-identical + 1 day-rollover refresh [the add-item modal's capture-day date input — 234 pixels in a 16×22 bbox, VLM-verified date-only], the dev evidence 4/4 byte-identical + VLM-verified) |** 108/327/35 green — the workspace the CARRIED-OVER class (git pull, no re-provisioning) |
"""

open("zero-balance_SKILL.md", "w", encoding="utf-8").write(t.replace(anchor, anchor + S159_ROW))
print("OK: Session 159 row inserted after the Session 158 row")
