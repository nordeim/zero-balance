#!/usr/bin/env python3
"""D1-D7 docs alignment for the v111 cycle (the persisted alignment-script
precedent — the v110 cycle's align-docs-v110.py form).

D1  AGENTS.md     — the v111 paragraph appended after the v110 paragraph
D2  CLAUDE.md     — the E2E count 313 -> 314 + the v111 clause appended to
                    the E2E bullet's tail (before the Smoke bullet)
D3  README.md     — the two (313 tests) counts -> 314 + the v111 plan row
                    appended after the v110 row
D4  SKILL.md      — project_state 313 -> 314 + the Session 146 row appended
D5  PAD           — the v1.1.68 revision block inserted before v1.1.67
D6  probe README  — the v111 section (the cycle record + the one new lesson
                    + the v112 queue) appended
D7  worklog.md    — the ledger tail v110->v111 + the Session 146 entry
                    inserted above Session 145

Each edit verifies its anchor exists (a miss fails the run loudly).
"""
import sys

ok = True

def edit(path, pairs, mode="replace"):
    global ok
    t = open(path, encoding="utf-8").read()
    for old, new in pairs:
        if mode == "replace":
            if old not in t:
                print(f"MISS in {path}: {old[:80]!r}")
                ok = False
                continue
            if t.count(old) != 1:
                print(f"AMBIGUOUS in {path} ({t.count(old)} hits): {old[:80]!r}")
                ok = False
                continue
            t = t.replace(old, new)
        else:  # insert-after
            if old not in t:
                print(f"MISS in {path}: {old[:80]!r}")
                ok = False
                continue
            t = t.replace(old, old + new, 1)
    open(path, "w", encoding="utf-8").write(t)
    print(f"aligned {path}")

# ---------------- D1: AGENTS.md ----------------
V111_AGENTS = """

Reference surfaces pinned by the v111 iteration (`docs/remediation-plan-v111.md`) — **the re-run cycle's next-oldest candidate (the v105-era LOGIN + CALCULATOR pair — the LOGIN view + the CALCULATOR dialog at desktop 1280x800, last re-shot v105; the pair's EIGHTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111]; the THIRTY-FOURTH consecutive queue/ledger agreement) + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — the v110 bump holds) + the 105th standing checks + the calculator's Line-Items section-header row census pin (PIN-ONLY; +1 e2e = 314)**: the verdicts CALCULATOR DIFFERENT (every flag DOM-arbitrated to a documented class — the "Will update category total" note the SEED-DATA class [ref hasWillUpdateSpan false — its own Rent $25.00 equals its calculated total; the clone's $1850-vs-$25 shows the note], the hover-action row the RESTING-STATE parity class [actionsAtRest {opacity 0, btnCount 2} identical both sides], the row-height flag their consequence) + LOGIN IDENTICAL (the v105 precedent — the verdict-variation form); the two-half census (CALC_CENSUS_JS 61 lines md5 e1092d12 + LOGIN_CENSUS_JS 36 lines md5 9e5a52d2 — the v99/v105 census blocks VERBATIM, source-to-source verified) reproduces the v105 values exactly on every axis — NO NEW CLONE GAP. The +1 pin (tests/e2e/calculator.spec.ts): the dialog's SECTION HEADER ROW between the v93-pinned totalCard and the items — the row {flex/center/space-between/mb 16px/h 32/w 720/childCount 2} + the "Line Items" h3 {16px/600/rgb(26,58,46)/lh 24px/h 24/margin 0} + the junction (h3CenterY === rowCenterY) + the addBtn context {110×32} — never pinned at ANY viewport before (zero "Line Items" assertions across all 24 specs); measured byte-identical both sides via the one-shot sectionrow-arbit-v111.sh; the mutation font-semibold → font-bold at calculator-dialog.tsx:171 line-scoped — only the v111 pin red at the sectionH3.fw axis alone (600→700) after the standalone REBUILD (the nameH4's own font-semibold at line 210 untouched — the v66 pin stays green); restored, rebuilt, post-restore 19/19 green. The cycle's tooling finding — THE PROVISIONING LESSON: the fresh sandbox's playwright cache held only v1200-era binaries; `npx playwright install chromium --dry-run` reported the v1243 location WITHOUT verifying existence, and the first chunk failed 74/75 with "Executable doesn't exist at .../chromium_headless_shell-1243" (the headless suite runs the headless-SHELL binary); the fix the FULL install (both binaries); the checklist rule — verify the cache DIRECTLY, the dry-run is a location REPORT never an existence proof."""
edit("AGENTS.md", [("Reference surfaces pinned by the v110 iteration", None)]) if False else None
t = open("AGENTS.md", encoding="utf-8").read()
anchor = "\nReference surfaces pinned by the v110 iteration"
if anchor not in t:
    print("MISS: AGENTS.md v110 paragraph anchor")
    ok = False
else:
    # append the v111 paragraph at the end of the file (the v110 paragraph is the last line)
    t = t.rstrip("\n") + "\n" + V111_AGENTS.strip() + "\n"
    open("AGENTS.md", "w", encoding="utf-8").write(t)
    print("aligned AGENTS.md (the v111 paragraph appended)")

# ---------------- D2: CLAUDE.md ----------------
t = open("CLAUDE.md", encoding="utf-8").read()
old_count = "- **E2E (Playwright, 313)**:"
new_count = "- **E2E (Playwright, 314)**:"
if t.count(old_count) != 1:
    print(f"MISS/AMBIGUOUS: CLAUDE.md E2E count ({t.count(old_count)} hits)")
    ok = False
else:
    t = t.replace(old_count, new_count)
smoke_anchor = "\n- **Smoke (bash, 35 steps)**:"
v111_clause = (", and the v111 pin: the calculator's Line-Items section-header row census at 1280 "
               "(calculator.spec.ts — the section row {flex/center/space-between/mb 16px/h 32/w 720/2 children} "
               "+ the 'Line Items' h3 {16px/600/rgb(26,58,46)/lh 24px/margin 0} + the junction centers + the "
               "addBtn context — never pinned at ANY viewport; zero 'Line Items' assertions across all 24 specs "
               "before the pin; measured byte-identical both sides by the one-shot sectionrow-arbit-v111.sh; the "
               "mutation font-semibold → font-bold at calculator-dialog.tsx:171 line-scoped — single-axis "
               "sectionH3.fw 600→700 alone, the v66 nameH4 pin untouched)")
if t.count(smoke_anchor) != 1:
    print(f"MISS/AMBIGUOUS: CLAUDE.md Smoke anchor ({t.count(smoke_anchor)} hits)")
    ok = False
else:
    t = t.replace(smoke_anchor, v111_clause + smoke_anchor)
open("CLAUDE.md", "w", encoding="utf-8").write(t)
print("aligned CLAUDE.md (314 + the v111 clause)")

# ---------------- D3: README.md ----------------
edit("README.md", [
    ("📂 e2e/                    # Playwright specs (313 tests) + global setup",
     "📂 e2e/                    # Playwright specs (314 tests) + global setup"),
    ("npm run test:e2e    # Playwright e2e (313 tests) — needs `npm run build` first",
     "npm run test:e2e    # Playwright e2e (314 tests) — needs `npm run build` first"),
])

# ---------------- D3b: README.md the v111 plan row ----------------
t = open("README.md", encoding="utf-8").read()
lines = t.split("\n")
row110_idx = None
for i, l in enumerate(lines):
    if l.startswith("| [`docs/remediation-plan-v110.md`]"):
        row110_idx = i
if row110_idx is None:
    print("MISS: README v110 plan row")
    ok = False
else:
    v111_row = ("| [`docs/remediation-plan-v111.md`](docs/remediation-plan-v111.md) | **The re-run cycle's next-oldest candidate (the v105-era LOGIN + CALCULATOR pair's EIGHTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111] — the LOGIN view + the CALCULATOR dialog at desktop 1280x800, last re-shot v105 — now the oldest remaining [v105 < v106 < v107 < v108 < v109 < v110]; the THIRTY-FOURTH consecutive queue/ledger agreement) + the axe watch (NO DRIFT) + the npm-audit watch (the standing step's second cycle: 0 vulnerabilities — the v110 bump holds, next 16.4.3 + zod 4.6.7) + the 105th standing checks + the calculator's Line-Items section-header row census pin (PIN-ONLY)**. The verdicts CALCULATOR DIFFERENT (every flag DOM-arbitrated — the 'Will update category total' note the SEED-DATA class [ref hasWillUpdateSpan false: its own Rent $25.00 equals its calculated total], the hover-action row the RESTING-STATE parity class [actionsAtRest {opacity 0, btnCount 2} identical both sides], the row-height flag their consequence) + LOGIN IDENTICAL (the v105 precedent); the two-half census (CALC_CENSUS_JS md5 e1092d12 + LOGIN_CENSUS_JS md5 9e5a52d2 — the v99/v105 blocks VERBATIM, source-to-source verified) reproduces the v105 values exactly — NO NEW CLONE GAP; the +1 e2e pins the never-pinned SECTION HEADER ROW at 1280 (the row {flex/center/space-between/mb 16px/h 32/w 720} + the 'Line Items' h3 {16px/600/rgb(26,58,46)} + the junction + the addBtn context; 314 e2e total), measured byte-identical both sides via the one-shot sectionrow-arbit-v111.sh, mutation-verified single-axis (font-semibold → font-bold at calculator-dialog.tsx:171 line-scoped — sectionH3.fw 600→700 alone; the v66 nameH4 pin untouched). The ship: 314 e2e zero flakes across the auditable four-chunk split (76+80+79+82 = 317 executions = 314 unique); the screenshots 16/16 byte-identical (the same-day-seed law — zero arbitration); the dev evidence re-captured + VLM-verified; THE PROVISIONING LESSON (the fresh sandbox's playwright cache held only v1200-era binaries — the dry-run check is a location report, never an existence proof; verify BOTH chromium-1243 AND chromium_headless_shell-1243 directly). |")
    lines.insert(row110_idx + 1, v111_row)
    open("README.md", "w", encoding="utf-8").write("\n".join(lines))
    print("aligned README.md (the v111 plan row appended)")

# ---------------- D4: SKILL.md ----------------
edit("zero-balance_SKILL.md", [
    ("project_state: 108 unit tests / 313 e2e tests / 35 smoke steps — all green",
     "project_state: 108 unit tests / 314 e2e tests / 35 smoke steps — all green"),
])

# ---------------- D4b: SKILL.md the Session 146 row ----------------
t = open("zero-balance_SKILL.md", encoding="utf-8").read()
lines = t.split("\n")
s145_idx = None
for i, l in enumerate(lines):
    if l.startswith("| 2026-10-24 | Session 145 — parity iteration v110"):
        s145_idx = i
if s145_idx is None:
    print("MISS: SKILL Session 145 row")
    ok = False
else:
    v111_skill_row = ("| 2026-10-24 | Session 146 — parity iteration v111 (`docs/remediation-plan-v111.md`) | **The re-run cycle's next-oldest candidate (the v105-era LOGIN + CALCULATOR pair's EIGHTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111] — the LOGIN view + the CALCULATOR dialog at desktop 1280×800, last re-shot v105, now the oldest remaining [v105 < v106 < v107 < v108 < v109 < v110]; the THIRTY-FOURTH consecutive queue/ledger agreement — the surface names verified against vlm-shots-v105.sh's own header before the derivation) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's second cycle: 0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 105th standing checks (ALL GREEN — the mobile menu working the 105th consecutive time; the reference's four bugs all live; the census clean on the first read) + the calculator's Line-Items section-header row census pin at 1280 (PIN-ONLY; +1 e2e = 314)**: the verdicts CALCULATOR DIFFERENT + LOGIN IDENTICAL (the v105 precedent — the verdict-variation form) with every calculator flag DOM-arbitrated to a documented class (the 'Will update category total' note the SEED-DATA class [the census: ref hasWillUpdateSpan false vs clone true — the reference's own Rent $25.00 equals its calculated total so the note hides; the totalCard chrome byte-identical]; the hover-action row the RESTING-STATE parity class [actionsAtRest {opacity 0, btnCount 2} identical both sides]; the row-height flag their consequence; the LOGIN pair's FAB unflagged — the standing disproof form stays documented); the two-half census (CALC_CENSUS_JS 61 lines md5 e1092d12 + LOGIN_CENSUS_JS 36 lines md5 9e5a52d2 — the v99/v105 census blocks VERBATIM, source-to-source verified against arbit-v105.sh's own blocks) reproduces the v105 values exactly on every axis — NO NEW CLONE GAP; the +1 pin (tests/e2e/calculator.spec.ts) the dialog's SECTION HEADER ROW family at 1280 — the row {flex/center/space-between/mb 16px/mt 0px/h 32/w 720/childCount 2} + the 'Line Items' h3 {16px/600/rgb(26,58,46)/lh 24px/h 24/margin 0} + the junction (h3CenterY === rowCenterY — the items-center alignment read live) + the addBtn context {110×32} — never pinned at ANY viewport in ANY spec (zero 'Line Items' assertions across all 24 specs), measured byte-identical both sides via the one-shot sectionrow-arbit-v111.sh (the h3 finder STRUCTURAL — exact text, childless; the row by the walk-up to the nearest flex ancestor carrying the Add Item button), mutation-verified single-axis AND cascade-free (font-semibold → font-bold at calculator-dialog.tsx:171 line-scoped — the ONLY bare font-semibold line in the file; the nameH4's mb-1 font-semibold at line 210 untouched; only the v111 pin red at the sectionH3.fw axis alone [600 → 700] after the standalone REBUILD; the v66/v81/v87/v93 pins green under the mutation); restored, rebuilt, post-restore 19/19 green; the ship 314 e2e zero flakes (76+80+79+82 = 317 executions = 314 unique); 35/35 smoke; the screenshots 16/16 byte-identical (the same-day-seed law); the dev evidence re-captured + VLM-verified (the menu proof: /income, docSW 390, navLandmark true); THE PROVISIONING LESSON (the fresh sandbox's playwright cache held only v1200-era binaries; the dry-run check reported the v1243 location without verifying existence — the first chunk failed 74/75 on the missing chromium_headless_shell-1243; the fix the FULL install downloading BOTH binaries; the checklist rule: verify the cache DIRECTLY — the dry-run is a location report, never an existence proof) |** 108/314/35 green |")
    lines.insert(s145_idx + 1, v111_skill_row)
    open("zero-balance_SKILL.md", "w", encoding="utf-8").write("\n".join(lines))
    print("aligned zero-balance_SKILL.md (the Session 146 row appended)")

# ---------------- D5: PAD ----------------
t = open("Project_Architecture_Document.md", encoding="utf-8").read()
pad_anchor = "#### Revision Block — v1.1.67 (Tracked Changes)"
if pad_anchor not in t:
    print("MISS: PAD v1.1.67 anchor")
    ok = False
else:
    v111_pad = """#### Revision Block — v1.1.68 (Tracked Changes)
- `[UI]` v1.1.68 (2026-10-24) — the v111 parity iteration (PIN-ONLY for src/ — no production-code change; no dependency change): the counts 108 unit / **314 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v105-era LOGIN + CALCULATOR pair's EIGHTH re-run [v59 -> v66 -> v75 -> v81 -> v87 -> v93 -> v99 -> v105 -> v111] — the LOGIN view + the CALCULATOR dialog at desktop 1280x800, the v59-era pair's surfaces, last re-shot v105; the THIRTY-FOURTH consecutive queue/ledger agreement) + the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the npm-audit watch (the standing step's second cycle: 0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 105th standing checks (ALL GREEN — the mobile menu working the 105th consecutive time; the reference's four bugs all live; the census clean on the first read) + the calculator's Line-Items section-header row census pin at 1280 (PIN-ONLY; +1 e2e = 314)**: the verdicts CALCULATOR DIFFERENT + LOGIN IDENTICAL (the v105 precedent — the verdict-variation form) with every flag DOM-arbitrated to a documented class (the 'Will update category total' note the SEED-DATA class [ref hasWillUpdateSpan false — its own Rent $25.00 equals its calculated total]; the hover-action row the RESTING-STATE parity class [actionsAtRest {opacity 0, btnCount 2} identical]; the row-height flag their consequence; the FAB unflagged); the two-half census (CALC_CENSUS_JS md5 e1092d12 + LOGIN_CENSUS_JS md5 9e5a52d2 — the v99/v105 blocks VERBATIM, source-to-source verified) reproduces the v105 values exactly — NO NEW CLONE GAP; the +1 pin (tests/e2e/calculator.spec.ts) the dialog's SECTION HEADER ROW at 1280 — the row {flex/center/space-between/mb 16px/h 32/w 720/2 children} + the 'Line Items' h3 {16px/600/rgb(26,58,46)/lh 24px/margin 0} + the junction centers + the addBtn context {110x32} — never pinned at ANY viewport in ANY spec (zero 'Line Items' assertions across all 24 specs), measured byte-identical both sides via the one-shot sectionrow-arbit-v111.sh, mutation-verified single-axis AND cascade-free (font-semibold -> font-bold at calculator-dialog.tsx:171 line-scoped — the v66 nameH4 pin's line 210 untouched; only the v111 pin red at sectionH3.fw alone [600 -> 700] after the standalone REBUILD); restored, rebuilt, post-restore 19/19 green; the ship chain 314 e2e zero flakes (76+80+79+82 = 317 executions across four chunks), 35/35 smoke, the screenshots 16/16 byte-identical (the same-day-seed law), the dev evidence re-captured + VLM-verified; THE PROVISIONING LESSON (the fresh sandbox's playwright cache held only v1200-era binaries; the dry-run check is a location report, never an existence proof — verify BOTH chromium-1243 AND chromium_headless_shell-1243 directly).

"""
    t = t.replace(pad_anchor, v111_pad + pad_anchor, 1)
    open("Project_Architecture_Document.md", "w", encoding="utf-8").write(t)
    print("aligned Project_Architecture_Document.md (v1.1.68 inserted)")

sys.exit(0 if ok else 1)
