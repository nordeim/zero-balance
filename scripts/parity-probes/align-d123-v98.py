#!/usr/bin/env python3
"""align-d123-v98.py — D1 AGENTS.md (the v98 paragraph), D2 CLAUDE.md
(300 -> 301 + the v98 clause at the E2E line's tail), D3 README.md (the
counts + the v98 plan-table row)."""
import sys

V98_AGENTS = """The v98 parity iteration (2026-10-20, PIN-ONLY for src/ — no production-code change; +1 e2e = 301; the plan `docs/remediation-plan-v98.md`, the narrative `docs/session_236.md`, the worklog Session 133 entry): the re-run cycle's next-oldest candidate — the v92-era SAVINGS pair (the SAVINGS view at desktop 1280x800, full-page, last re-shot v92, now the oldest remaining [v92 < v93 < v94 < v95 < v96 < v97]; the pair's SIXTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98] — the TWENTY-FIRST consecutive queue/ledger agreement, the surface names verified against vlm-shots-v92.sh's own header before the derivation) + the axe-core watch at its re-check point (NO DRIFT — npm-latest 4.14.0, only rc/next sha prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds; the engine-contract pin 2 passed standalone) + the 92nd standing checks (ALL GREEN — the mobile menu VERIFIED WORKING the 92nd consecutive time; the reference's four bugs all live [the 464px /networth overflow measured docSW 464 directly]; the data census the 92nd clean drift check — clean on the FIRST read, no render-race this cycle; the SEO pair live both sides) + the goal-card action-menu panel/menuitem-resting census pin at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 301). The baseline chain FULLY GREEN on the FRESH-CLONE workspace (the sandbox reset — the v86/v88/v90/v91/v92 precedent: git clone at main @ 9152c18; npm install; .env written [DATABASE_URL="file:../db/custom.db"]; db/ re-seeded [the seedcheck exact: 7 items / rent 1850 / expensesTotal 2235 / 0 line items / 3 assets / 2 liabilities]; chromium-1243 installed for the pinned @playwright/test 1.63.0 — the cache's 1200 build belongs to a different playwright generation; lint → typecheck → 108 unit → npm run build [robots + sitemap prerendered] → 300 e2e chunk executions [135+96+71 = 302 = 300 unique, zero flakes on the first run] → 35/35 smoke). The codebase audit clean (the two commits since the v97 push 6a6725c [d4b77c5 + 9152c18] verified session-log-only [docs/session_234.md + docs/session_235.md — ZERO src/ or lockfile deltas]; the production seams re-audited — auth, db-path [the sandbox's polluted parent DATABASE_URL re-confirming why the env -u discipline is load-bearing], the SEO pair, the Tailwind v4 mitigations, the three test tiers; skills/ excluded throughout). The v98 cycle's findings: the verdict DIFFERENT with every flag DOM-arbitrated to a documented class (the "Card Footer Alignment" the v57 DATA-CONDITIONAL class — the census proving the footer childCount 1-vs-2 with the clone's "Brokerage" chip, the reference RENDERING payment chips when data carries them per the v97 income-card evidence; the card grid the seed-count class [1 vs 2]; the header subtitle + card contents the seed-data classes; the avatar the user-identity class). The both-sides census — executed in the TWO-HALF controlled form, BUILT TWO-HALF FROM THE START (ref-arbit-v98.sh + clone-arbit-v98.sh via build-twohalf-v98.py, the ONE census JS block [SV_CENSUS_JS 153 lines] extracted once and embedded byte-identically across the halves — the md5 line-block contract [31d181ed]) — REPRODUCES the v86/v92 census values EXACTLY: zero drift on every axis (the h1/grid/card/cardTitle/titleRow/cardAmount/footer/badge families; the docSW 1280 guard; the clone template's last-column sub-pixel the column-distribution rounding noise WITHIN the documented 309.328px family). NO NEW CLONE GAP — the v98 iteration PIN-ONLY. The +1 e2e pin: the goal-card ACTION-MENU PANEL + MENUITEM-RESTING interior census at 1280 (tests/e2e/items.spec.ts — the v97 missing-middle lesson applied to the ACTION layer: the tokens G5/G9 pins hold the menu ITEM's COLOR family + the CONTENT's border-COLOR on the income view, the v35 S1 the keyboard contract, but the menu PANEL's GEOMETRY [bg/radius/shadow/min-w/overflow/z/w/h] and the menuitem's RESTING interior [fs/fw/pad/radius/lh/h] were NEVER pinned at ANY viewport in ANY spec — the coverage-map grep across all 24 specs; + the panel {bg white, radius 6px, border 1px rgb(229,229,229), minW 128px, overflow hidden, z 50, pos static, w 128, h 74} + the shadow-md VISIBLE layers via toContain [the v37 O1 v3/v4-construct precedent — the zero-layer lead count 2-vs-4 the documented class] + the item0 {fs 14px, fw 400, color rgb(10,10,10), pad 6px 8px, radius 4px, lh 20px, h 32} + the itemCount 2 + the docSW 1280 guard — the panel w/h + itemCount DATA-INDEPENDENT [the structural Edit+Delete pair: 2×32 + 2×4 pad + 2×1 border = 74], so unlike the v97 pin's clone-only guards these axes assert the cross-side-verified values directly; the pin's own axes first measured byte-identical on both sides by the supplemental two-half census menu-arbit-v98.sh + menu-clone-v98.sh via build-menu-v98.py, the census JS byte-identical by the md5 line-block diff 0f83b786; both sides read-only [a menu OPEN only, no item clicks]; the seedcheck exact after the run; the cross-side census discovery — the reference's action trigger carries NO aria-label [the clone's "Actions for …" label is the a11y superset, the v38 search-input note's sibling], so the census's finder is GEOMETRIC [the textless 36×36 svg button], AND the reference's menu opens only on the full POINTER EVENT SEQUENCE [pointerdown → mousedown → pointerup → mouseup → click — a bare el.click() opens the clone's Radix menu but NOT the reference's]). The pin-sanity mutation (the executed form — the DropdownMenuContent panel's rounded-md → rounded-lg at src/components/ui/dropdown-menu.tsx:20, by LINE NUMBER; the line-scoping keeps the DropdownMenuItem's own rounded-sm at line 36 untouched [the item's 4px radius axis]): the failure diff reads as the panel radius axis ALONE ("6px" → "8px"); the full items.spec.ts under the mutation reads ONLY the v98 pin red (42 green) — cascade-free BY CONSTRUCTION (no spec asserts any dropdown-menu panel radius — this pin is the first; the v97 listbox panel radius 6px reads select.tsx's SelectContent, a DIFFERENT component; the tokens G5 contentBorder is the border-COLOR axis, not radius) — then restored (git diff src/ = 0 lines; the standalone REBUILD via the FULL npm run build; the post-restore full run 43/43 green). The F5 full chain re-run GREEN: lint → typecheck → 108 unit → build → 301 e2e (136+96+71 = 303 chunk executions = 301 unique tests, zero flakes) → 35/35 smoke; the screenshots 10/16 BYTE-IDENTICAL + 6/16 the fresh-reseed DATE class (the fresh-clone re-seed re-anchoring the seed's isoDate offsets to the new seed day — db/ is gitignored, it does not travel; every differing region pixel-arbitrated by pixel-diff-v98.py to a date-digit span [03-income 2 spans, 04-expenses 3, 05-savings 2, 06-networth 1, 16-item-details 1 + two max-channel-2 sub-perceptual re-render regions, 08-calculator one 77x77 max-channel-2 region — the v68 calculator precedent, below the ~2.5 JND; the VLM crop re-read over-read the sub-threshold noise as a "missing border" — the measurement is the authority, the v43 rule]); the final seedcheck exact. The operational lessons (the probe README's D6 section): the reference pointer-event family (the reference's React tree opens its ellipsis dropdown only on the full pointer event SEQUENCE — any future census that must OPEN reference-side interactive chrome dispatches the full sequence), the unlabelled-trigger finder class (the reference's card action trigger carries NO aria-label — cross-side finders for action chrome must be GEOMETRIC, the clone-only aria-label reserved for the e2e pin's locator), and the data-independent panel (the action menu's Edit+Delete pair is STRUCTURAL — the panel w/h + itemCount assert cross-side-verified values directly). The docs alignment: D1 AGENTS.md (the v98 paragraph), D2 CLAUDE.md (300 → 301 + the v98 clause at the E2E line's tail), D3 README.md (the counts + the v98 plan-table row), D4 zero-balance_SKILL.md (Session 133 audit row + the state line + the last_updated date), D5 the PAD's v1.1.55 revision block, D6 the probe README's v98 section (+ the v99 queue — the v93-era LOGIN + CALCULATOR pair, to be verified against vlm-shots-v93.sh's own header next cycle), D7 session_236.md + the worklog Session 133 entry; docs/remediation-plan-v98.md saved (the validated plan — the pre-execution validation section recording the measured values, the mutation target line verified by reading the source, the coverage-map grep, the disproven-in-advance candidates).
"""

V98_CLAUDE_CLAUSE = """, and the v98 goal-card action-menu panel + menuitem-resting interior census pin at 1280 (the v97 missing-middle lesson applied to the ACTION layer — the menu PANEL's GEOMETRY {bg white, radius 6px, border 1px rgb(229,229,229), minW 128px, overflow hidden, z 50, pos static, w 128, h 74} + the shadow-md visible layers via toContain + the item0 resting interior {14px/400/rgb(10,10,10)/pad 6px 8px/radius 4px/lh 20px/h 32} + the itemCount 2 — never pinned at ANY viewport in ANY spec before [the G5/G9 pins hold the COLOR family only]; the panel w/h + itemCount DATA-INDEPENDENT [the structural Edit+Delete pair]; the mutation rounded-md → rounded-lg at ui/dropdown-menu.tsx:20 only the v98 pin red — the panel radius axis alone, cascade-free; the line-scoping keeps the item's rounded-sm at line 36 untouched; the census's cross-side finder GEOMETRIC [the reference's trigger is unlabelled] with the full pointer event SEQUENCE required reference-side)
"""

V98_README_ROW = """| [`docs/remediation-plan-v98.md`](docs/remediation-plan-v98.md) | **The re-run cycle's next-oldest candidate (the v92-era SAVINGS pair's sixth re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98] — the SAVINGS view at desktop 1280x800, full-page, last re-shot v92; the twenty-first consecutive queue/ledger agreement) + the axe watch (NO DRIFT) + the goal-card action-menu panel/menuitem-resting census pin at 1280 (PIN-ONLY; +1 e2e = 301)**: the verdict DIFFERENT with every flag DOM-arbitrated (the v57 DATA-CONDITIONAL footer, the seed-count/seed-data classes, the user-identity avatar); the two-half census reproducing the v86/v92 values exactly (zero drift); the +1 pin the ACTION-MENU PANEL + MENUITEM-RESTING interior (never pinned at ANY viewport in ANY spec — the G5/G9 pins hold the COLOR family only; the panel w/h + itemCount DATA-INDEPENDENT [the structural Edit+Delete pair]); the reference pointer-event + unlabelled-trigger lessons; the screenshots 10/16 byte-identical + 6/16 the fresh-reseed DATE class (pixel-arbitrated) |** 108/301/35 green |
"""

def main():
    ok = True
    # D1: AGENTS.md — insert the v98 paragraph after the v97 paragraph (line 264)
    text = open("AGENTS.md", encoding="utf-8").read()
    anchor = "the disproven-in-advance candidates).\n"
    idx = text.rindex(anchor)
    if "The v98 parity iteration" in text:
        print("D1: v98 paragraph already present")
    else:
        text = text[: idx + len(anchor)] + V98_AGENTS + "\n" + text[idx + len(anchor) :]
        open("AGENTS.md", "w", encoding="utf-8").write(text)
        print("D1: AGENTS.md v98 paragraph inserted after the v97 paragraph")

    # D2: CLAUDE.md — 300 -> 301 + the v98 clause at the E2E line's tail
    text = open("CLAUDE.md", encoding="utf-8").read()
    if "**E2E (Playwright, 301)**" in text:
        print("D2: already 301")
    else:
        old_head = "- **E2E (Playwright, 300)**:"
        if old_head not in text:
            print("D2 MISS: E2E line head"); ok = False
        else:
            text = text.replace(old_head, "- **E2E (Playwright, 301)**:", 1)
    tail_anchor = "the line-scoping keeps the trigger's own rounded-md at line 19 [the v91 pin] untouched)"
    if "the v98 goal-card action-menu panel" in text:
        print("D2: v98 clause already present")
    elif tail_anchor in text:
        text = text.replace(tail_anchor, tail_anchor + V98_CLAUDE_CLAUSE.rstrip("\n"), 1)
        open("CLAUDE.md", "w", encoding="utf-8").write(text)
        print("D2: CLAUDE.md 300->301 + the v98 clause appended at the E2E line's tail")
    else:
        print("D2 MISS: E2E tail anchor"); ok = False

    # D3: README.md — the counts + the v98 plan-table row
    text = open("README.md", encoding="utf-8").read()
    text = text.replace("e2e/                    # Playwright specs (300 tests)", "e2e/                    # Playwright specs (301 tests)")
    text = text.replace("npm run test:e2e    # Playwright e2e (300 tests)", "npm run test:e2e    # Playwright e2e (301 tests)")
    row_anchor = "| [`docs/remediation-plan-v97.md`](docs/remediation-plan-v97.md)"
    if "remediation-plan-v98.md" in text:
        print("D3: v98 row already present")
    elif row_anchor in text:
        idx = text.index(row_anchor)
        text = text[:idx] + V98_README_ROW + text[idx:]
        open("README.md", "w", encoding="utf-8").write(text)
        print("D3: README.md counts 300->301 + the v98 plan-table row inserted")
    else:
        print("D3 MISS: plan-table anchor"); ok = False

    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
