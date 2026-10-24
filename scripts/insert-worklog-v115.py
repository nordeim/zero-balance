#!/usr/bin/env python3
"""Insert the Session 150 (v115) entry into worklog.md — newest-first,
inserted before the Session 149 entry. Also updates the plan-list header's
'through' reference. Idempotent (the marker check fails loudly)."""
import sys

ENTRY = """## Session 150 — Parity iteration v115: the re-run cycle's next-oldest candidate (the v109-era ITEMS pair's ninth re-run) + the axe watch (NO DRIFT) + the npm-audit watch (0 vulnerabilities — the standing step's sixth cycle) + the 109th standing checks + the items md-band state census pin (PIN-ONLY) (2026-10-24)

**The cycle** (`docs/remediation-plan-v115.md` — the plan validated against the codebase before execution; the delivery record: `docs/session_280.md`): the re-run cadence's next-oldest candidate — the v109-era ITEMS pair (the ITEMS view [INCOME + EXPENSES] at desktop 1280x800 FULL-PAGE, last re-shot v109 — now the oldest remaining [v109 < v110 < v111 < v112 < v113 < v114]; the pair's NINTH re-run bracket [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115]; the THIRTY-EIGHTH consecutive queue/ledger agreement — the surface names verified against vlm-shots-v109.sh's own header before the derivation) + the axe watch (NO DRIFT — 4.14.0 holds; the v68 dedupe verified) + the npm-audit watch at its sixth cycle (0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]) + the 109th standing checks + the items md-band state census pin at 800x600 (PIN-ONLY; +1 e2e = 318).

- **The verdicts INCOME IDENTICAL + EXPENSES DIFFERENT** — the pair's documented verdict split (the same split as v109; v103 read BOTH DIFFERENT; the income side's documented flags all-data classes, the IDENTICAL verdict the cleaner outcome on the same chrome — the VLM-verdict variation form, the v105 LOGIN-IDENTICAL precedent) — with every flag DOM-arbitrated to a documented class: the expenses card-footer payment chips the v57 DATA-CONDITIONAL class census-proven live (the reference's OWN income card's footer reads childCount 2 with the "Bank Account" chip + icon — the reference RENDERS payment chips when data carries them; its expense items simply ship no payment method — footer childCount 1 — while the clone's carry them); the badge-arrangement wrap the v57 wrap/classification-VALUE classes (badgeRow h ref 22 vs clone 52, badgeCount 3 vs 4 — the clone's "Recurring" superset chip + the wrap, the chip chrome byte-identical); the "Edit with Base44" FAB the platform-chrome class DISPROVEN live (fabCount 0 + bodyHasBase44 false on BOTH sides at 1280 on /expenses — the base44-fab-arbit-v115.sh standing disproof form; a FAB flag WAS raised, so the disproof ran); the avatar the user-identity class; the header stats + card contents the seed-data classes.
- **The both-sides census** (the ONE census JS block [193 lines] byte-identical across the halves — the md5 line-block contract [b55dcd29 — the v97/v103/v109 census blocks VERBATIM, the block itself version-free]; the builder derived via derive-build-twohalf-v115.py with the swap-order rule) **compared AXIS-BY-AXIS by the persisted compare-v115-census.py — 187 axes: 163 identical + 24 documented-class deltas, ZERO new deltas** (the avatar chrome {36x36/radius 9999px/14px-600/white/rgb(143,188,63)}; the grid {w 960/gap 16/the 3-col 309.328px family}; the card {w 309/pad 20/radius 12/border rgb(229,231,227)}; the titleRow, the amount leaf, the footer + badge0 chrome; the filter card on BOTH variants {income 960x86/search 447x36 spanning/2 comboboxes; expenses search 216 not spanning/3 comboboxes}; the page header row; the docSW 1280 guard — all byte-identical) — **NO NEW CLONE GAP**.
- **The +1 pin** (tests/e2e/items.spec.ts): the ITEMS view's MD-BAND STATE at 800x600 — the viewport band (768 <= w < 1024) NO spec pins on the items views (the coverage map: pinned ONLY at 390 [v52] and 1280 [v45/v64/v91/v92/v109]; the v42 five-route mid-viewport census sits at 640 — BELOW md, the 1-col state) — the item grid's md state {the 2-col template `232px 232px`, gap 16px} + the page header row's md state {flex/row/space-between/center/gap 16px/mb 32px/h 60/childCount 2} + the filter card's inner grid md state {4 tracks `95.5px x4`, gap 16px, childCount 3} + the card box at the 2-col width {w 232/pad 20px/radius 12px/border rgb(229,231,227)/bg white} + the docSW 800 guard; the grid childCount (the seed count) + the card h (the v70b wrap consequence) stay UNPINNED — data axes (the v107 position-arithmetic discipline); measured byte-identical both sides via the one-shot mdband-arbit-v115.sh (the finders structural: the card-like-children grid walk [radius 12px + pad 20px], the Add-button→row walk [the v109 finder], the search→card→inner-grid walk); mutation-verified single-family (md:grid-cols-2 → md:grid-cols-1 at items-view.tsx:262 line-scoped — the ONLY `grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3` line in the file, the expenses filter card's own md:grid-cols-2 on line 175 a DIFFERENT line untouched by the full-string scoping; ONLY the v115 pin red [44 green] with the failure diff reading as the grid-template family axis ALONE [`232px 232px` → `480px`] after the standalone REBUILD; the 390/640 states structurally immune [grid-cols-1 base], the >=1024 states structurally immune [lg:grid-cols-3 overrides md — the v45 1280 pin green under the mutation], the header row's md:flex-row + the filter card's md:grid-cols-4 separate tokens — untouched); restored (git diff src/ = 0), rebuilt, post-restore 45/45 green.
- **The derivation lesson**: THE POST-SWAP-FRAGMENT RULE (a history-correction fragment containing the CURRENT cycle's version token must be written against the POST-generic-swap state — the generic swap consumes the version token first [v109 → v115], so a correction written against the source form [`-> v97 -> v103 -> v109]`] finds ZERO matches and the bracket silently loses its newest entry; the first pass's bracket read `[v57 -> ... -> v103 -> v115]` — the v109 entry MISSING — caught by reading the derived header BEFORE proceeding, the repair targeting the post-swap form [`-> v97 -> v103 -> v115]` → `-> v97 -> v103 -> v109 -> v115]`]; the v114 derivation's own precedent now formalized).
- **The baseline chain FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace** (the RESET class — the v114 environment did not persist; the repo re-cloned from main @ 735f612; the v108 FRESH-CLONE lesson applied end-to-end: npm ci run in the FOREGROUND [the v114 silent-death lesson] with the zod extraction verified 840/840 + src/v4 present BEFORE any gate, BOTH v1243 playwright binaries verified DIRECTLY, .env + db push/seed; the seedcheck via the canonical db-seedcheck-v68.cjs — an initial ad-hoc seedcheck script hit the PrismaClient CWD-resolution trap and was replaced before any gate): seedcheck exact (7/1850/2235/0/3/2); lint; typecheck; 108 unit; build (robots + sitemap prerendered); 317 e2e zero flakes across the four-chunk split (84+77+77+82 = 320 executions — the a11y file kept INSIDE chunk 4); 35/35 smoke; npm audit 0 vulnerabilities; the post-push commits audited session-log-only.
- **The ship chain**: 318 e2e zero flakes (84+78+77+82 = 321 executions = 318 unique); 35/35 smoke; the screenshots 16/16 byte-identical (the same-day-seed law — zero arbitration); the dev evidence 4/4 byte-identical + re-captured + VLM-verified (the menu proof: /income, docSW 390, navLandmark true — the dev-shots scripts derived v114→v115 with the version-swap-only verification).
- **The 109th standing checks ALL GREEN** — the mobile menu VERIFIED WORKING the 109th consecutive time; the reference's four bugs all live; the data census clean on the FIRST reads (no render-race hit this cycle); the SEO pair live both sides.
- The docs aligned D1–D7 (AGENTS the v115 paragraph; CLAUDE 318 + the v115 clause; README counts + the v115 plan row; the SKILL Session 150 row + the state line; PAD v1.1.72; the probe README's v115 section + THE POST-SWAP-FRAGMENT RULE lesson + the v116 queue [the v110-era SAVINGS pair, NINTH re-run]; this Session 150 entry); `docs/session_280.md` saved. `.env.example` verified matching the codebase.

---

"""

path = "worklog.md"
t = open(path, encoding="utf-8").read()

if "## Session 150 — Parity iteration v115" in t:
    print("ALREADY APPLIED: the Session 150 entry")
    sys.exit(1)

anchor = "## Session 149 — Parity iteration v114"
if anchor not in t:
    print("MISS: the Session 149 anchor")
    sys.exit(1)
t = t.replace(anchor, ENTRY + anchor, 1)

# the plan-list header's 'through' reference — bumped to the v115 cycle
old_through = "and every subsequent plan through\n`docs/remediation-plan-v112.md` (the v112 cycle — Session 147)."
new_through = "and every subsequent plan through\n`docs/remediation-plan-v115.md` (the v115 cycle — Session 150)."
if old_through in t:
    t = t.replace(old_through, new_through, 1)
    print("bumped the plan-list header through-reference to v115")
else:
    print("NOTE: the plan-list header through-reference not found in the expected form — checking")
    import re
    m = re.search(r"and every subsequent plan through\n`docs/remediation-plan-v\d+\.md` \(the v\d+ cycle — Session \d+\)\.", t)
    if not m:
        print("WARN: no through-reference found at all — leaving as-is")
    else:
        print(f"found variant form: {m.group(0)[:80]!r} — leaving as-is (manual check advised)")

open(path, "w", encoding="utf-8").write(t)
print("inserted the Session 150 entry (newest-first, before Session 149)")
