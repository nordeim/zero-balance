# Session 129 — the v54 session's raw tool-call narrative (2026-10-12)

The condensed transcript of the session that delivered
`docs/remediation-plan-v54.md` (parity iteration v54 — the savings
goal-card's badge-row + footer internals at 390, PIN-ONLY — plus the
footer-locator and blockification probe lessons).

The workspace had been RESET (the zero-balance directory empty, the
sandbox reaped the tree) — `git clone` rebuilt it at 664cfd7
(docs/session_127.md, the v53 session's raw transcript; the v53
parity commit a6ab17e beneath it). The environment rebuilt: npm
install, .env from .env.example (the dev AUTH_SECRET), db:push +
db:seed (db/custom.db at the repo root). The five core docs + the
four session docs reviewed; the v53 state verified (the pin-only
diff, the 247 e2e, the .env contract, the sitemap/robots pair, the
test configs, the skills/ catalog).
The baseline chain: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓.
The first e2e run FAILED 21-wide — `browserType.launch: Executable
doesn't exist at chromium_headless_shell-1243` — the fresh-clone
environment lacked the per-version headless-shell binary; `npx
playwright install chromium` downloaded it. The a11y spec re-ran
22/22; the full suite ran as two ordered chunks: 140 + 108 = 248,
zero failures. The 35/35 smoke completed the baseline.
The 48th standing checks — reference side all four bugs live (the
toast-blocker; the sheet-trap via overlayCount 1; the no-landmark;
the 464 /networth overflow), the data census intact, the SEO pair
live; clone side R1 burger hit-test true + the sheet opens, R2 nav +
closed, R3 green, R4 zero overflow at 390 on all five views, the SEO
pair 200 — the mobile navigation menu verified working.
The code audit: the trap-log scan CLEAN (both -mb-2 back buttons
inside their converted containers), the v53 diff verified pin-only,
the sitemap/robots/vitest/playwright configs in place, .env.example
matching.
The v54 sweep — `ref-v54.sh` + `clone-v54.sh` (READ-ONLY on the
reference): the savings view's GOAL-CARD INTERNALS at 390. The FIRST
reference run's footer read 16px/48px with an empty "payment span" —
the generic justify-between + svg finder had matched the card's
HEADER row first (it also carries justify-between + the kebab svg).
The locator fixed to "the LAST justify-between direct child WITHOUT
an h4" (a card-children DOM dump confirmed the structure: the header
`flex items-start justify-between mb-3`, the amount `mb-4`, the
badge row `flex flex-wrap gap-2 mb-3`, the footer `flex
items-center justify-between text-xs`). Both drivers re-run:
BYTE-PARITY on every chrome axis — the header row flex/gap 8/mb 4,
the dot 8×8/rgb(59,126,161) (the savings TYPE accent on both sites —
the reference's need-classified goal still carries the teal dot: it
colors by TYPE, not classification), the badge row flex/wrap/gap
8/mb 12, every chip h 22/radius 6/pad 2px 10px/12/600 with the
12×12 icons at mr 4 (the "monthly" chip w 78 and the "active" chip
w 63 on BOTH sites — the same text at the same chrome renders the
same width), the footer 12/rgb(107,114,128)/h 16, the date span
flex/gap 4 with the 12×12 calendar icon. The chip count (3 vs 4),
the row height (22 vs 52), the payment span, and the card height
(200 vs 230) are the documented data classes. NO PRODUCTION GAP —
the third consecutive pin-only iteration.
The remediation plan v54 written + validated (the item-card.tsx
source lines, the existing pins' safety, the e2e contract).
The TDD cycle: F1's first run FAILED — the census returned null: the
badge-row finder required the chips' computed display to be
"inline-flex" but they compute to "flex" (flex items are blockified
per the CSS spec — a step-by-step debug probe against the dev server
found the flexRows dump: the chips' childDisplays all "flex"). The
finder fixed to accept "flex"; GREEN immediately.
The S1 mutation series (each with the standalone REBUILD as a
SEPARATE command — the v53 lesson): (a) gap-2 → gap-4 → FAILS (8 →
16); (b) px-2.5 → px-1.5 → FAILS (pad 2px 10px → 2px 6px); (c)
text-xs → text-sm → FAILS (h 22 → 26); (d) the footer's text-xs →
text-sm → FAILS; (e) the date span's gap-1 → gap-2 → FAILS (4 → 8).
All restored — the clean diff: ONE spec file, 214 insertions, ZERO
production changes.
The VLM pair (F2 — the /networth tablist at 390 [the v53 F1
surface, the queue's suggestion] + the savings goal card [THE F1
surface]): PAIR 1 flagged 5 diffs. The DOM verification: the
reference session had EXPIRED mid-census (the "Welcome to
ZeroBudge" landing + docSW 390 signature) — re-login, then the
arbitration: the active tab bg byte-identical rgb(220,252,231) (a
screenshot-perception artifact); the Add button's full "Add Asset"
on both sites (scrollW 134 = clientW 134, no truncation — a
small-text misread); the trend icon the documented 464-overflow
width class (the reference's 32×32 trending-up at x 368 + 32 > 390
clips at its overflow page's right edge; the clone's at x 294 fully
in-bounds); the data values + the Base44 FAB the documented
classes. PAIR 2's flags all the seed-data classes (the count, the
badges, the payment span, the second card). The pair CLEAN per the
v43 rule.
The full chain re-run: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓
· 248 e2e (141 + 108, two ordered chunks, both exit 0, zero
failures) · 35/35 smoke ✓. The 16 screenshots regenerated — ZERO
byte-diffs (the pin-only invariant). The docs aligned (AGENTS /
CLAUDE / README / PAD v1.1.11 / the SKILL Session 89 row + the 248
state / the probe README's v54 section / session_128 + session_129
/ the repo worklog Session 88 + the ledger list / the workspace
worklog). Commit + push to main via the SSH wrapper.
