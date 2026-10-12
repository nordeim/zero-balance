# Session 126 — the v53 session's raw tool-call narrative (2026-10-12)

The condensed transcript of the session that delivered
`docs/remediation-plan-v53.md` (parity iteration v53 — the
/networth tablist's mobile pin + the calculator dialog's mobile pin,
PIN-ONLY — plus the orphaned-server and restoreRent execution
lessons).

The workspace had been RESET (the sandbox reaped the tree) —
`git clone` rebuilt it at 3f33d5f (docs/session_124.md, the v52
session's raw transcript + the v53 queue: the /networth mobile
tablist census, the calculator dialog 390 reflow, the
reference-side verify/forgot-confirm censuses [WRITES — deferred]).
The environment rebuilt: npm install, .env from .env.example (the
dev AUTH_SECRET), db:push + db:seed (db/custom.db at the repo
root). The five core docs + the four session docs reviewed; the v52
state verified (the subcategory P, the 245 e2e, the .env contract,
the sitemap/robots pair, the test configs, the skills/ catalog).
The baseline chain GREEN (the first run had ONE not-found flake —
passing standalone immediately; the cold-cache timing): lint ✓ ·
typecheck ✓ · 108/108 unit ✓ · build ✓ · 245/245 e2e (5.4m) ·
35/35 smoke ✓.
The 47th standing checks — reference side all four bugs live (the
toast-blocker; the sheet-trap via overlayCount 1; the no-landmark;
the 464 /networth overflow), the data census intact, the SEO pair
live; clone side R1 sheetLinks 5 (the v52-fixed text-walk
selector), R2 nav + closed, R3/R4 green, the SEO pair 200 — **the
mobile navigation menu verified working as expected**.
The code audit: the trap-log scan CLEAN (both -mb-2 back buttons
inside their converted containers), the v52 diff verified, the
sitemap/robots/vitest/playwright configs in place, .env.example
matching.
The v53 sweep — `ref-v53.sh` + `clone-v53.sh` (READ-ONLY on the
reference): the /networth TABLIST at 390 — byte-parity on every
chrome axis (the list 36/grid/#f5f5f5/8px/4px/maxW 448; the active
175×28 green pair + the shadow-sm VISIBLE pair; the inactive
#737373 pair; the 16×16 icons) — the width family rides the
reference's own 464-overflow bug (its list 432 with fractional
tracks overhangs the 390 viewport; the clone's superset fix keeps
the page in-bounds at 358/pageSW 390 — the v47 divergence class).
The CALCULATOR at 390 — the first clone census read the EMPTY state
(the dev seed carries no line items; the reference's own Rent
carries one — "Contents Insurance"): the empty-state "Add First
Item" outline button 141×32 + the panel 358×555. The with-row
follow-up (`clone-v53b.sh`, the add-then-delete flow on the clone's
OWN db): the panel 358×413 — **the h 413 byte-identical to the
reference's 1-row state** — the header 101, the chip 32×40 + the
close 29×36 (the identical flex-shrink squish on both sites), the
total card 310×90/#fff7f5/12/16, the row 310/16/white/border-t, the
Add Item button 110×32/12/500/gradient. The clone-v53b debug: the
login eval's closing `()` was missing (an un-invoked async
function expression submits NOTHING — the "no card" cascade).
NO PRODUCTION GAP — the second consecutive pin-only iteration.
The remediation plan v53 written + validated (the source lines,
the existing pins' safety, the e2e contract).
The TDD cycle: F1 GREEN immediately (pin-only). F2's first run
FAILED — the missing page.goto("/expenses") (the new describe sits
outside the parent's beforeEach); fixed, GREEN.
The S1 mutation series (each with the standalone REBUILD — and the
v53 lesson: the rebuild and the test run as SEPARATE commands; the
combined one-liner raced the .next/standalone swap TWICE, reading
"1 passed" against a not-yet-swapped build — the served-build probe
on :3199 confirmed the mutation live before the clean re-run bit):
(a) grid-cols-2 → grid-cols-1 → F1 FAILS; (b) the active bg utility
removed → F1 FAILS; (c) the header py-4 → py-2 → F2 FAILS; (d) the
panel maxWidth 48rem → 40rem → F2 FAILS; (e) the total card p-4 →
p-2 → F2 FAILS. All restored — the clean diff: the two specs, 337
insertions, ZERO production changes.
The full-chain diagnosis (the session's hard-won lessons):
(1) the full e2e run started TIMING OUT — the first diagnosis
suspected the environment pace (the foreground run held 141 tests
at 570s; the split runs passed 55-in-53s then 40-in-2.6m —
inconsistent), then the split runs' failures traced to an
**ORPHANED webServer on :3100** — a timed-out run's `bun
.next/standalone/server.js` child survived the kill, and the next
run REUSED it (reuseExistingServer: true) with a db handle gone
stale under the global-setup's delete-and-re-seed → every
data-driven assertion timed out at the 10s gate (the 45-failure
cascade). Killed the pid → the suite's pace and correctness
returned.
(2) even after the orphan kill, the dashboard spec failed 35-wide
in one run — the root cause: **the F2 test's cleanup lacked
restoreRent(page)** — the line-item mutations recalculate the
parent's amount server-side (the calculator rule), so the test left
Rent ≠ 1850 and poisoned every later spec's dashboard arithmetic
(+$2065.00). The v45 F2b test has always ended with restoreRent; a
new calculator test must copy the WHOLE cleanup, not just the
delete. Fixed; the standalone re-runs of the "failed" tests all
passed.
The full chain re-run: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓
· **246/246 chromium e2e (the 247 single-run equivalent — run as
two ordered chunks, 140 + 108, both exit 0, zero failures)** ·
35/35 smoke ✓.
The VLM pair (the calculator at 390 — the F2 surface): 5 flags —
the close-button "boxed X" INVESTIGATED to the root: the pixel
analysis (672 gray pixels vs 0), the computed-style dump (the
clone's outline auto 1px vs the reference's outline-style none +
activeElement BODY), and the desktop 08-calculator.png (no ring in
real mouse flows) — the ring is the probe's synthetic-click focus
artifact (the :focus-visible-only keyboard a11y superset; the
reference's never-focused close is its own a11y regression); the
other 4 flags the documented data/platform classes. The pair CLEAN.
The 16 screenshots regenerated — ZERO byte-diffs (the pin-only
invariant). The dev db re-seeded (the probe's add/delete had left
Rent recalculated — the capture script's +$2065.00 wait hung until
the reset). The docs aligned (AGENTS / CLAUDE / README / PAD
v1.1.10 / the SKILL Session 88 row + the 247 state / the probe
README's v53 section with the five execution lessons / session_125
+ session_126 / the repo worklog Session 87 + the ledger list /
the workspace worklog). Commit + push to main via the SSH wrapper.
