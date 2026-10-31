#!/usr/bin/env python3
"""align-docs-v137.py — D1-D5 of the v137 docs alignment (the D0 anchor
discipline: every insert/replace anchor verified 1-hit BEFORE any write;
the script refuses and exits non-zero on any anchor miss or multi-hit).
  D1 AGENTS.md — the v137 paragraph appended after the v136 paragraph
  D2 CLAUDE.md — the e2e count 339 -> 340 + the v137 clause appended to
     the e2e enumeration line's end (after the v136 clause)
  D3 README.md — the two test-count lines 339 -> 340 + the v137 plan row
     inserted after the v136 row
  D4 zero-balance_SKILL.md — the project_state line 338 -> 340 (THE
     v136-SKIP REPAIR: the v136 cycle's D4a anchor missed the
     project_state line's own format and bumped the Session 170 row's
     historical cell instead — the state line left stale at 338) + the
     Session 170 historical cell REPAIRED 339 -> 338 (the v135 cycle's
     own shipped count) + the Session 172 row inserted after the
     Session 171 row
  D5 Project_Architecture_Document.md — the v1.1.94 revision block
     inserted before the v1.1.93 block
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
anchor = "the dev-shots scripts derived v135→v136 with the version-swap-only verification).\n\n"
if one_hit(text, anchor, "AGENTS v136-paragraph tail"):
    v137 = (
        "Reference surfaces pinned by the v137 iteration (`docs/remediation-plan-v137.md`) — "
        "**the re-run cycle's next-oldest candidate (the v131-era DASHBOARD pair — the DASHBOARD at desktop 1280x800 FULL-PAGE, the v125-era pair's surface family, the pair's TWELFTH re-run "
        "[v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137], the SIXTIETH consecutive queue/ledger agreement "
        "— the corrected entries-minus-one convention applied cleanly: the ELEVENTH ordinal recorded in the v131 plan's own header on its 12-entry bracket [v61 the original, one entry] → v137 = the TWELFTH, no prose/header conflict; "
        "the v131 shots header carries the FULL bracket form — the documented verification source)** "
        "+ the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, the v68 dedupe holds) "
        "+ the npm-audit watch at its twenty-eighth re-check (0 VULNERABILITIES --omit=dev — the v110 bump holds: next 16.4.3 + zod 4.6.7; the 16 moderate the accepted dev-only ESLint braces chain) "
        "+ the 131st standing checks (ALL GREEN — the reference's four bugs all live [toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1` after nav, no-landmark `navLandmark:false`, "
        "the 464px /networth overflow measured docSW 464 directly]; the data census clean on the FIRST reads; the SEO pair live both sides; "
        "the clone's mobile menu VERIFIED WORKING the 131st consecutive time, zero overflow at 390 on all five views; the seedcheck exact after the clone half). "
        "**The baseline GREEN ON THE FIRST CHAIN** (the RE-PROVISIONED workspace — the v108 provisioning end-to-end [npm ci 354, the zod 4.6.7 extraction intact, BOTH chromium pairs 1200+1243 — "
        "the fresh cache held only the OLD 1200 pair, the dry-run-is-a-location-report lesson re-verified], the .env + db/ + db:push + db:seed, the seedcheck EXACT 7/1850/2235/0/3/2 before any gate]: "
        "lint, typecheck, 108/108 unit, build [robots + sitemap prerendered], the 4-chunk e2e [342 executions = 339 unique, ZERO flakes — both v136-closed watch classes green through the chain], 35/35 smoke; "
        "the production-seam audit clean; skills/ excluded). "
        "The probe series derived from the v131 lineage (derive-v137-series.py — FOUR explicit session-token families + NINE history-correction fragments [the era marker v125-era→v131-era + last re-shot v125→v131 + "
        "the oldest-remaining list [v125 < … < v130]→[v131 < v132]; the ordinal ELEVENTH→TWELFTH + the bracket extended; the agreement ordinal FIFTY-FOURTH→SIXTIETH; the re-proves chain v101-v125→v101-v131; "
        "the arbit verdict/census provenance re-pointed at the v131 measurement], all applied on the FIRST run, zero residual, line counts preserved 57/42/45/258) "
        "+ the two-half builder (derive-build-twohalf-v137.py — the lesson-range bump v92..v130→v92..v136 [the BARE range token: the v131 lineage's TWOHALF_NOTE wraps the phrase across two lines] + the lineage-note fixup LAST) "
        "+ the comparator (derive-compare-v137.py — the explicit /tmp/vlm131→/tmp/vlm137 log-path swap + the provenance citations re-pointed at the v131 measurement) "
        "+ the THREE-block two-half contract verified three-way (verify-twohalf-v137.py — ARBIT_G 61 lines md5 b500dd299e5e9a94eaf07b29facc69db + ARBIT_Q 58 lines md5 da04e9954976eb58d9aff2b95d2dcfc6 + "
        "ARBIT_X 25 lines md5 7a381755a22ce55c62f70a053f826852 — **the v131 lineage's own recorded digests, carried byte-identical through the version-swap derivation**). "
        "**The VLM verdict — IDENTICAL ×2, THE CLEANEST PAIR FORM** (the v131/v125 verdict form re-confirmed: zero layout/style flags BOTH passes, NO DOM arbitration needed this cycle; "
        "every flag in the documented classes — the PCT/seed-data classes [the hero allocation pct + balance, the stat amounts/counts, the donut proportions + legend] + the pass-2 nav-highlight the v56 SUPERSET class + "
        "the avatar letter the USER-IDENTITY class, exactly the v131 cycle's own flag set); the both-sides census **154 axes — 144 identical + 10 documented-class deltas, ZERO new — REPRODUCING the v131 census values EXACTLY** "
        "(the same 154/144/10 split, zero drift on every axis: the 10 documented = the v66 INVISIBLE shadow lead-layer count + the v61 label-lesson ×6 [the finder catches the clone's WRAPPER, the clone's LEAF span identical — "
        "pinned green by the v61 F3 + v107 F4 pins] + the v77 mechanism class ×3 [grid mt 0px-vs-32px with the rendered gap byte-identical]). "
        "**A PIN-ONLY cycle for src/ — zero production-code changes (the seventh PIN-ONLY cycle in the last eight) + one e2e pin (339 → 340): the INTERACTIVE STAT CARD's OWN-HOVER SHADOW LADDER at 1280** "
        "(the never-pinned shadow path of the pinned hover family: the v131 pin the own-hover REVEAL ladder [the radial + the chevron opacity], the v45 F3b pin the QUICK-ACTION TWIN's LIVE hover:shadow-lg layers, "
        "the v51 F2 pin the AT-REST card chrome at 390 incl. the inline rest shadow — the stat card's hovered shadow held by NO spec at ANY viewport; THE CONSTRUCT: the card carries BOTH the hover:shadow-lg utility AND "
        "the INLINE boxShadow rgba(0,0,0,0.06) 0px 4px 20px — the inline beats the utility in the cascade [the v43 category-row precedent], so the hovered end-state is the INLINE PERSISTENCE); "
        "the both-sides one-shot census stathovershadow-arbit-v137.sh (the v131 stathover form adapted to the shadow axes; the (5,5)-parked ladder; the live-read center — both sides (440,400); READ-ONLY per the v46 rule) "
        "measured the ladder **CLEAN — NO GAP** (the inline shadow persists under hover IDENTICALLY both sides at every rung; the construct deltas — the class token + the transition metadata — the documented classes); "
        "the pin appended (append-pin-v137.py — the at-rest rung → the REAL-hover rung {cardHover true + THE unchanged inline boxShadow — the persistence axis} → the restored rung; the V94-COLLISION-safe axis set; "
        "GREEN on the first run; the authoritative --list: 340 in 24 files); "
        "the pin-sanity mutation — the MUTATION-FAMILY ROTATION (the first-chosen INLINE-VALUE form run and REJECTED as a cascade [2 failed — the v51 F2 pin shares the inline rest-shadow VALUE axis at "
        "dashboard.spec.ts:2057, no line-scoping can separate same-element same-axis pins]; the rotated IMPORTANT-MODIFIER form hover:shadow-lg → hover:shadow-lg! at dashboard-view.tsx:578 — cascade-free BY CONSTRUCTION "
        "[hover-scoped] AND simulating the guarded drift [the utility going LIVE under hover]) sole-failure verified live [1 failed + 51 passed in the full dashboard sweep — the failure diff the LIVE shadow-lg construct "
        "vs the inline persistence, cardHover preserved]; restored (git diff src/ = 0 lines) + the FULL REBUILD + the post-restore regression 142 passed (dashboard 52 + networth 39 + items 51 — "
        "the v136/v134 pins' different-file immunity verified live). "
        "The ship chain **340 e2e zero flakes** (93+93+75+82 = 343 executions = 340 unique — the count derived authoritatively via --list before any chunk ran; both closed watches green through the chain); 35/35 smoke; "
        "**the screenshots 16/16 BYTE-IDENTICAL (the same-day-seed law — this workspace and the v136 cycle both seeded Oct 31 UTC, every date-bearing surface rendering identically)**; "
        "the dev evidence 4/4 byte-identical + VLM-verified (the menu proof: the sheet closed, the heading \"Income\", the top bar + toggle + brand; the dev-shots scripts derived v136→v137 with the version-swap-only verification). "
        "THE DOCS REPAIR: the SKILL's project_state line was left STALE at 338 by the v136 cycle's D4a (its anchor missed the line's own format and bumped the Session 170 row's historical cell instead) — "
        "this cycle's D4 repairs the state line to the current 340 AND restores the Session 170 row's cell to the v135 cycle's own shipped 338.\n\n"
    )
    text = text.replace(anchor, anchor + v137)
    io.open(AG, "w", encoding="utf-8").write(text)
    print("D1 AGENTS.md: the v137 paragraph appended")

# ---------- D2: CLAUDE.md ----------
CL = "CLAUDE.md"
text = io.open(CL, encoding="utf-8").read()
if one_hit(text, "E2E (Playwright, 339)", "CLAUDE e2e count"):
    text = text.replace("E2E (Playwright, 339)", "E2E (Playwright, 340)")
    io.open(CL, "w", encoding="utf-8").write(text)
    print("D2a CLAUDE.md: 339 -> 340")
text = io.open(CL, encoding="utf-8").read()
anchor = "the full 338 re-verified green under the fix, then 339 with the pin)\n"
if one_hit(text, anchor, "CLAUDE v136 clause tail"):
    v137clause = (
        "; the v137 pin — the INTERACTIVE STAT CARD's OWN-HOVER SHADOW LADDER at 1280 (the PIN-ONLY form — src/ ZERO changes, the seventh PIN-ONLY cycle in the last eight: "
        "the never-pinned shadow path of the pinned hover family [the v131 pin the own-hover REVEAL ladder — the radial + the chevron opacity, never the card's own shadow; the v45 F3b pin the QUICK-ACTION TWIN's LIVE "
        "hover:shadow-lg — that card carries NO inline boxShadow; the v51 F2 pin the AT-REST card chrome at 390 incl. the inline rest shadow]; THE CONSTRUCT: the stat card carries BOTH the hover:shadow-lg utility AND "
        "the INLINE boxShadow rgba(0,0,0,0.06) 0px 4px 20px — the inline beats the utility in the cascade [the v43 category-row precedent], so the hovered end-state is the INLINE PERSISTENCE; "
        "the both-sides census stathovershadow-arbit-v137.sh measured the ladder CLEAN — the inline shadow persists under hover IDENTICALLY both sides at every rung, both cards' centers (440,400), "
        "the construct deltas [the class token + the transition metadata] the documented classes — NO GAP, NO REPAIR; the pin: the at-rest rung → the REAL-hover rung {cardHover true + the unchanged inline boxShadow} → "
        "the restored rung, GREEN on the first run, --list 340 in 24 files; the pin-sanity mutation — the MUTATION-FAMILY ROTATION: the first-chosen INLINE-VALUE form REJECTED as a cascade [the v51 F2 pin shares "
        "the inline rest-shadow VALUE axis, 2 failed], the rotated IMPORTANT-MODIFIER form [hover:shadow-lg → hover:shadow-lg! — cascade-free by construction, hover-scoped, simulating the guarded drift] "
        "sole-failure verified live [1 failed + 51 passed in the full dashboard sweep — the failure diff the LIVE shadow-lg construct vs the inline persistence]; "
        "the post-restore regression 142/142 [dashboard 52 + networth 39 + items 51 — the v136/v134 pins' different-file immunity verified live])\n"
    )
    text = text.replace(anchor, anchor[:-1] + v137clause)
    io.open(CL, "w", encoding="utf-8").write(text)
    print("D2b CLAUDE.md: the v137 clause appended")

# ---------- D3: README.md ----------
RM = "README.md"
text = io.open(RM, encoding="utf-8").read()
if text.count("(339 tests)") == 2:
    text = text.replace("(339 tests)", "(340 tests)")
    io.open(RM, "w", encoding="utf-8").write(text)
    print("D3a README.md: the two count lines 339 -> 340")
text = io.open(RM, encoding="utf-8").read()
anchor = "the screenshots 16/16 (9 byte-identical + 7 the deterministic seed-date/cross-day classes), the dev evidence 4/4 + VLM-verified). |\n"
if one_hit(text, anchor, "README v136 row tail"):
    v137row = (
        "| [`docs/remediation-plan-v137.md`](docs/remediation-plan-v137.md) | **The re-run cycle's next-oldest candidate (the v131-era DASHBOARD pair's TWELFTH re-run — the v125-era pair's surface family, "
        "the SIXTIETH consecutive queue/ledger agreement) + the stat-card own-hover shadow ladder pin at 1280 (PIN-ONLY — src/ zero changes, the seventh PIN-ONLY cycle in the last eight; "
        "the census measured the ladder CLEAN: the INLINE boxShadow persists under hover IDENTICALLY both sides, the hover:shadow-lg utility inert [the v43 inline-beats-utility class]; "
        "the pin-sanity mutation the MUTATION-FAMILY ROTATION — the inline-value form rejected as a cascade [the v51 F2 pin shares the value axis], the rotated important-modifier form sole-failure verified; "
        "the post-restore regression 142/142) — the 131st standing checks ALL GREEN (the mobile menu the 131st consecutive), the watches green (0 vulnerabilities --omit=dev, axe-core NO DRIFT), "
        "the VLM IDENTICAL ×2 (the cleanest pair form, zero style flags both passes, no DOM arbitration), the census 154/144/10 reproducing the v131 values EXACTLY, "
        "the ship chain 340 e2e zero flakes + 35/35 smoke, the screenshots 16/16 byte-identical (the same-day-seed law), the dev evidence 4/4 + VLM-verified; "
        "the SKILL project_state line repaired (the v136 cycle left it stale at 338)). |\n"
    )
    text = text.replace(anchor, anchor + v137row)
    io.open(RM, "w", encoding="utf-8").write(text)
    print("D3b README.md: the v137 plan row inserted")

# ---------- D4: zero-balance_SKILL.md ----------
SK = "zero-balance_SKILL.md"
text = io.open(SK, encoding="utf-8").read()
s_line = "project_state: 108 unit tests / 338 e2e tests / 35 smoke steps — all green"
if one_hit(text, s_line, "SKILL project_state line (the v136-skip repair)"):
    text = text.replace(
        s_line,
        "project_state: 108 unit tests / 340 e2e tests / 35 smoke steps — all green",
    )
    io.open(SK, "w", encoding="utf-8").write(text)
    print("D4a SKILL.md: the project_state line 338 -> 340 (the v136-skip repair, two-count jump through the v136 pin)")
text = io.open(SK, encoding="utf-8").read()
s170 = "|** 108/339/35 green — the workspace the CONTINUING class "
if one_hit(text, s170, "SKILL Session 170 historical cell (the v136 D4a mis-bump repair)"):
    text = text.replace(s170, "|** 108/338/35 green — the workspace the CONTINUING class ")
    io.open(SK, "w", encoding="utf-8").write(text)
    print("D4b SKILL.md: the Session 170 historical cell repaired 339 -> 338 (the v135 cycle's own shipped count)")
text = io.open(SK, encoding="utf-8").read()
anchor = "the workspace the RE-PROVISIONED class (the v108 provisioning end-to-end, the seedcheck EXACT before any gate) |** 108/339/35 green |\n"
if one_hit(text, anchor, "SKILL Session 171 row tail"):
    s172 = (
        "| 2026-10-31 | Session 172 — parity iteration v137 (`docs/remediation-plan-v137.md`) | **The re-run cycle's next-oldest candidate (the v131-era DASHBOARD pair's TWELFTH re-run "
        "[v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137], the SIXTIETH consecutive queue/ledger agreement) "
        "+ the stat-card own-hover shadow ladder pin at 1280 (PIN-ONLY — src/ ZERO changes, the seventh PIN-ONLY cycle in the last eight: the never-pinned shadow path of the pinned hover family; "
        "the census measured the ladder CLEAN — the INLINE boxShadow persists under hover IDENTICALLY both sides, the hover:shadow-lg inert [the v43 inline-beats-utility class]; "
        "the pin-sanity mutation the MUTATION-FAMILY ROTATION [the inline-value form rejected as a cascade — the v51 F2 pin shares the value axis; the rotated important-modifier form sole-failure verified: "
        "1 failed + 51 passed in the full dashboard sweep]; the post-restore regression 142/142) — the 131st standing checks ALL GREEN (the mobile menu the 131st consecutive; the four reference bugs live; "
        "the census clean on the FIRST reads), the watches green (0 vulnerabilities --omit=dev — the twenty-eighth; axe-core NO DRIFT), the VLM IDENTICAL ×2 (the cleanest pair form, zero style flags, "
        "no DOM arbitration), the census 154 axes — 144 identical + 10 documented, ZERO new (the v131 values reproduced EXACTLY), the ship chain 340 e2e zero flakes (343 executions) + 35/35 smoke, "
        "the screenshots 16/16 byte-identical (the same-day-seed law), the dev evidence 4/4 + VLM-verified; the workspace the RE-PROVISIONED class (the v108 provisioning end-to-end, the seedcheck EXACT before any gate); "
        "the docs repair: the project_state line recovered from the v136 cycle's stale 338 to the current 340 |** 108/340/35 green |\n"
    )
    text = text.replace(anchor, anchor + s172)
    io.open(SK, "w", encoding="utf-8").write(text)
    print("D4c SKILL.md: the Session 172 row inserted")

# ---------- D5: Project_Architecture_Document.md ----------
PAD = "Project_Architecture_Document.md"
text = io.open(PAD, encoding="utf-8").read()
anchor = "#### Revision Block — v1.1.93 (Tracked Changes)"
if one_hit(text, anchor, "PAD v1.1.93 block heading"):
    v1194 = (
        "#### Revision Block — v1.1.94 (Tracked Changes)\n"
        "- `[UI]` v1.1.94 (2026-10-31) — the v137 parity iteration (**PIN-ONLY for src/ — zero production-code changes, the seventh PIN-ONLY cycle in the last eight** + one e2e pin; "
        "no config change, no dependency change): the counts 108 unit / **340 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v131-era DASHBOARD pair's TWELFTH re-run "
        "[v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137], the SIXTIETH consecutive queue/ledger agreement)** "
        "+ the INTERACTIVE STAT CARD's OWN-HOVER SHADOW LADDER pin at 1280 (the never-pinned shadow path of the pinned hover family: the card carries BOTH the hover:shadow-lg utility AND the INLINE boxShadow — "
        "the inline beats the utility in the cascade [the v43 category-row precedent], so the hovered end-state is the INLINE PERSISTENCE, measured byte-identical both sides by the one-shot census "
        "stathovershadow-arbit-v137.sh — NO GAP, NO REPAIR; the pin-sanity mutation the MUTATION-FAMILY ROTATION: the first-chosen inline-value form rejected as a cascade [the v51 F2 pin shares the "
        "inline rest-shadow value axis], the rotated important-modifier form [hover:shadow-lg → hover:shadow-lg! — cascade-free by construction] sole-failure verified live [1 failed + 51 passed]; "
        "the post-restore regression 142/142); the 131st standing checks ALL GREEN (the mobile menu the 131st consecutive); the VLM verdict IDENTICAL ×2 (the cleanest pair form — zero style flags both passes, "
        "no DOM arbitration); the both-sides census 154 axes — 144 identical + 10 documented-class deltas, ZERO new (the v131 values reproduced EXACTLY); the ship chain 340 e2e zero flakes (343 executions) + 35/35 smoke; "
        "the screenshots 16/16 byte-identical (the same-day-seed law); the dev evidence 4/4 + VLM-verified; the docs repair: the SKILL project_state line recovered from the v136 cycle's stale 338 to the current 340 "
        "(the v136 D4a's anchor had missed the line's format and bumped the Session 170 row's historical cell instead — both repaired this cycle).\n\n"
    )
    text = text.replace(anchor, v1194 + anchor)
    io.open(PAD, "w", encoding="utf-8").write(text)
    print("D5 PAD.md: the v1.1.94 revision block inserted")

print("DONE" if ok else "FAILED — anchor misses above")
sys.exit(0 if ok else 1)
