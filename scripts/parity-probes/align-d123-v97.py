#!/usr/bin/env python3
"""D1-D3 docs alignment for the v97 cycle (Session 132).

D1 AGENTS.md — append the v97 audit-history paragraph.
D2 CLAUDE.md — 299 -> 300 + the v97 clause at the E2E line's tail.
D3 README.md — the counts (2 places) + the v97 plan-table row.
"""
import sys

ok = True

def must_replace(path, old, new, count=1):
    global ok
    text = open(path, encoding="utf-8").read()
    n = text.count(old)
    if n != count:
        print(f"MISS ({n} found, want {count}) in {path}: {old[:60]!r}")
        ok = False
        return
    open(path, "w", encoding="utf-8").write(text.replace(old, new, count))
    print(f"applied in {path}: {old[:48]!r}")

AGENTS_V97 = """The v97 parity iteration (2026-10-20, PIN-ONLY for src/ — no production-code change; +1 e2e = 300; the plan `docs/remediation-plan-v97.md`, the narrative `docs/session_233.md`, the worklog Session 132 entry): the re-run cycle's next-oldest candidate — the v91-era ITEMS pair (the INCOME + EXPENSES view pair at desktop 1280x800, full-page, last re-shot v91, now the oldest remaining [v91 < v92 < v93 < v94 < v95 < v96]; the pair's SIXTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97] — the TWENTIETH consecutive queue/ledger agreement, the surface names verified against vlm-shots-v91.sh's own header before the derivation) + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only rc/next sha prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds; the engine-contract pin 2 passed standalone) + the 91st standing checks (ALL GREEN — the mobile menu VERIFIED WORKING the 91st consecutive time; the reference's four bugs all live [the 464px /networth overflow measured directly — the settle-wait form]; the data census the 91st clean drift check with ONE timing-artifact re-read [the expenses leg first read "no match" — the eval raced the page's client-side render; the settle-wait re-read after a fresh login measured the exact documented "4 items · $525.00"]; the SEO pair live both sides) + the filter-listbox panel/option-interior census pin at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 300). The baseline chain FULLY GREEN on the CARRIED-OVER workspace (the session-log-only commit class: pulled to main @ 27c5970; the two commits since the v96 push 90f766e [59e7d14 + 27c5970] verified session-log-only [docs/session_231.md + docs/session_232.md — ZERO src/ or lockfile deltas], so the v96 cycle's own environment carries over unchanged, no re-provisioning; the seedcheck exact before any flow ran; lint → typecheck → 108 unit → npm run build [robots + sitemap prerendered] → 299 e2e chunk executions [134+96+71 = 301 = 299 unique, zero flakes on the first run] → 35/35 smoke). The codebase audit clean (the production seams re-audited — auth, db-path [the sandbox's polluted parent DATABASE_URL re-confirming why the env -u discipline is load-bearing], the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout). The v97 cycle's findings: BOTH VLM verdicts DIFFERENT (the pair's documented verdict class) with every flag DOM-arbitrated to a documented class (the avatar the user-identity class; the header stats/grids/card contents the seed-data classes; the payment-method footer chips the v57 DATA-CONDITIONAL class — the census proving the reference RENDERS payment chips when data carries them [its own income card's footer childCount 2 with the "Bank Account" chip] while its expense items ship none; the badge wrap + the card h 200-vs-230 the v57/v70b Recurring-wrap class [+30px wrap + the 1-row sibling stretch]; the "Edit with Base44" FAB the platform-chrome class re-arbitrated live by the one-shot both-sides DOM census [fabCount 0 + bodyHasBase44 false on BOTH sides — the FAB renders in the reference's platform iframe chrome; this cycle the VLM attributed it to the reference — the non-inverted form of the v85/v91-documented attribution class]). The both-sides census — executed in the TWO-HALF controlled form, BUILT TWO-HALF FROM THE START (ref-arbit-v97.sh + clone-arbit-v97.sh via build-twohalf-v97.py, the ONE census JS block [CENSUS_JS 193 lines] extracted once and embedded byte-identically across the halves — the md5 line-block contract [b55dcd29]) — REPRODUCES the v85/v91 census values EXACTLY: zero drift on every axis (the avatar/grid/card/titleRow/amount/footer/badge/filterCard families; the docSW 1280 guard; the income template's last-column sub-pixel the column-distribution rounding noise WITHIN the documented 309.328px family). NO NEW CLONE GAP — the v97 iteration PIN-ONLY. The +1 e2e pin: the filter LISTBOX PANEL + OPTION-RESTING interior census at 1280 (tests/e2e/items.spec.ts — the MISSING-MIDDLE family: the v91 pin holds the TRIGGER's resting chrome, the v36 S2 the OPTION's focus-state family, but the PANEL container itself [bg/radius/border/shadow/max-h/overflow/z + the viewport's 4px pad] and the option's RESTING interior [fs/fw/color/pad/radius/h] were NEVER pinned at ANY viewport in ANY spec — the family-extension survey walking the COMPONENT LAYERS [trigger → panel → viewport → option]; + the panel {bg white, radius 6px, border 1px rgb(229,229,229), maxH 384px, overflow hidden, z 50, w 218} + the shadow-md VISIBLE layers via toContain [the v37 O1 v3/v4-construct precedent — the zero-layer lead count 2-vs-4 the documented class] + the viewport {pad 4px, display block} + the opt0 {fs 14px, fw 400, color rgb(23,23,23), pad 6px 32px 6px 8px, radius 4px, h 32} + the clone's own data-dependent guards [panel h 106, optCount 3] + the docSW 1280 guard; the pin's own axes first measured byte-identical on both sides by the supplemental two-half census listbox-arbit-v97.sh + listbox-clone-v97.sh via build-listbox-v97.py, the census JS byte-identical by the md5 line-block diff 34c916da; both sides read-only; the seedcheck exact after the run). The pin-sanity mutation (the executed form — the SelectContent panel's rounded-md → rounded-lg at src/components/ui/select.tsx:68, by LINE NUMBER; the line-scoping keeps the SelectTrigger's own rounded-md at line 19 untouched [the v91 pin's 6px trigger axis]): the failure diff reads as the panel radius axis ALONE ("6px" → "8px"); the full items.spec.ts under the mutation reads ONLY the v97 pin red (41 green) — cascade-free BY CONSTRUCTION (no spec asserts any listbox panel radius — this pin is the first; the calculator's panel.radius 16px is the calculator DIALOG panel, a different element; the radius never changes bg/border/shadow/max-h/overflow/z/viewport-pad/option-interior) — then restored (git diff src/ = 0 lines; the standalone REBUILD via the FULL npm run build; the post-restore full run 42/42 green). The F5 full chain re-run GREEN: lint → typecheck → 108 unit → build → 300 e2e (135+96+71 = 302 chunk executions = 300 unique tests, zero flakes) → 35/35 smoke; the screenshots 16/16 BYTE-IDENTICAL (the same-day regeneration — both sides Oct 20 UTC, the 07-add-item-modal's day digits matching, no midnight crossing); the final seedcheck exact. The operational lessons (the probe README's D6 section): the census render-race generalization (ANY multi-eval reference flow treats a "no match"/empty census as a possible expiry OR render race first — re-login + settle-wait + re-read — before suspecting drift; never record the state change on a single raced read), the panel-chrome missing-middle family (the family-extension survey should walk the COMPONENT LAYERS, not just the axes of one layer), and the two-half form as the default (applied clean again — zero resource-exhaustion symptoms). The docs alignment: D1 AGENTS.md (the v97 paragraph), D2 CLAUDE.md (299 → 300 + the v97 clause at the E2E line's tail), D3 README.md (the counts + the v97 plan-table row), D4 zero-balance_SKILL.md (Session 132 audit row + the state line + the last_updated date), D5 the PAD's v1.1.54 revision block, D6 the probe README's v97 section (+ the v98 queue — the v92-era SAVINGS pair, to be verified against vlm-shots-v92.sh's own header next cycle), D7 session_233.md + the worklog Session 132 entry; docs/remediation-plan-v97.md saved (the validated plan — the pre-execution validation section recording the measured values, the mutation target line verified by reading the source, the coverage-map grep, the disproven-in-advance candidates).
"""

CLAUDE_TAIL_OLD = "the max-sm dodge keeps the 640/1280-tier pins green)"
CLAUDE_TAIL_NEW = ("the max-sm dodge keeps the 640/1280-tier pins green); the v97 filter-listbox "
  "panel + option-resting interior census pin at 1280 (the MISSING-MIDDLE family — the panel "
  "container between the v91 trigger pin and the v36 option-state pin: the panel {bg white, "
  "radius 6px, border 1px rgb(229,229,229), maxH 384px, overflow hidden, z 50, w 218} + the "
  "shadow-md visible layers via toContain [the v37 O1 v3/v4-construct precedent] + the viewport "
  "{pad 4px} + the opt0 resting interior {14px/400/rgb(23,23,23)/pad 6px 32px 6px 8px/radius "
  "4px/h 32} + the clone's own guards [panel h 106, optCount 3] — never pinned at ANY viewport "
  "in ANY spec before; the mutation rounded-md → rounded-lg at ui/select.tsx:68 only the v97 "
  "pin red — the panel radius axis alone, cascade-free; the line-scoping keeps the trigger's "
  "own rounded-md at line 19 [the v91 pin] untouched)")

README_ROW = ("| [`docs/remediation-plan-v97.md`](docs/remediation-plan-v97.md) | **The re-run cycle's next-oldest candidate (the v91-era ITEMS pair's sixth re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97] — the INCOME + EXPENSES view pair at desktop 1280x800, full-page, last re-shot v91; the twentieth consecutive queue/ledger agreement, the surface names verified against the v91 probe's own header) + the axe watch (NO DRIFT) + the filter-listbox panel/option-interior census pin at 1280 (PIN-ONLY — no production-code change; +1 e2e = 300)**: BOTH verdicts DIFFERENT (the pair's documented verdict class) with every flag DOM-arbitrated to a documented class — the payment-method footer chips the v57 DATA-CONDITIONAL class (the reference renders payment chips when data carries them — its own income card's footer childCount 2 with the \"Bank Account\" chip — while its expense items ship none), the badge wrap + the card h 200-vs-230 the v57/v70b Recurring-wrap class, the FAB the platform-chrome class (re-arbitrated live: fabCount 0 + bodyHasBase44 false on both sides); the two-half census (BUILT two-half from the start — the CENSUS_JS block md5-identical across the halves) reproducing the v85/v91 values exactly (zero drift on every axis); the +1 pin the LISTBOX PANEL + OPTION-RESTING interior {the panel {bg white/radius 6px/border 1px rgb(229,229,229)/maxH 384px/overflow hidden/z 50/w 218} + the shadow-md visible layers via toContain + the viewport {pad 4px} + the opt0 {14px/400/rgb(23,23,23)/pad 6px 32px 6px 8px/radius 4px/h 32}} — the missing-middle family never pinned at ANY viewport, the pin's own axes first measured byte-identical on both sides by the supplemental two-half census (both sides read-only); the pin-sanity mutation rounded-md → rounded-lg at ui/select.tsx:68 (only the v97 pin red, the failure diff reads as the panel radius axis alone — cascade-free; the line-scoping keeps the trigger's rounded-md at line 19 [the v91 pin] untouched); the screenshots 16/16 byte-identical (the same-day regeneration); the lessons: the census render-race generalization + the panel-chrome missing-middle family |")

# D1 — append the v97 paragraph to AGENTS.md
text = open("AGENTS.md", encoding="utf-8").read()
if "v97 parity iteration" in text:
    print("D1 already applied")
else:
    if not text.endswith("\n"):
        text += "\n"
    text += AGENTS_V97 + "\n"
    open("AGENTS.md", "w", encoding="utf-8").write(text)
    print("D1 applied: AGENTS.md v97 paragraph appended")

# D2 — CLAUDE.md
must_replace("CLAUDE.md", "E2E (Playwright, 299)", "E2E (Playwright, 300)")
must_replace("CLAUDE.md", CLAUDE_TAIL_OLD, CLAUDE_TAIL_NEW)

# D3 — README.md
must_replace("README.md", "Playwright specs (299 tests)", "Playwright specs (300 tests)")
must_replace("README.md", "Playwright e2e (299 tests)", "Playwright e2e (300 tests)")
text = open("README.md", encoding="utf-8").read()
if "remediation-plan-v97.md" in text:
    print("D3 row already applied")
else:
    anchor = "| [`docs/remediation-plan-v96.md`]"
    i = text.index(anchor)
    text = text[:i] + README_ROW + "\n" + text[i:]
    open("README.md", "w", encoding="utf-8").write(text)
    print("D3 applied: the v97 plan-table row inserted before the v96 row")

sys.exit(0 if ok else 1)
