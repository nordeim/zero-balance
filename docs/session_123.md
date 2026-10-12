# Session 123 — the v52 session's raw tool-call narrative (2026-10-12)

The condensed transcript of the session that delivered
`docs/remediation-plan-v52.md` (parity iteration v52 — the details
sheet's missing subcategory line FIX + the /income and /expenses 390
pins + the details-sheet internals pin + the standing script's
burger-selector probe-infra fix).

The workspace SURVIVED — `git pull` fast-forwarded 2d2a776 →
e71d357 (docs/session_121.md, the v51 session's raw Chinese
transcript + the v52 queue: the reference-side verify/forgot-confirm
censuses [WRITES — deferred], the /expenses and /income mobile
censuses, the item-details 390 reflow). The five core docs + the
four session docs reviewed — the v51 state verified (the
zb-auth-mode on the verify branch, 241 e2e).
The baseline chain GREEN on the first run: lint ✓ · typecheck ✓ ·
108/108 unit ✓ · build ✓ (the sitemap/robots pair prerendered) ·
**241/241 e2e (5.5m)** · 35/35 smoke ✓. npm audit: 0 production
vulnerabilities. `.env` ≡ `.env.example`.
The 46th standing checks — the REFERENCE side's first run hit a
COLD START: the login eval found no form ("already logged in?")
because the 3s settle raced the base44 cold boot; the re-run on the
warm session read clean: all four reference bugs live (the
toast-blocker; the sheet-trap via overlayCount 1; the no-landmark;
the 464 /networth overflow), the data census intact, the SEO pair
live. The CLONE side read R1 `sheetLinks: 0` — INVESTIGATED (not
dismissed): the script's `button[aria-label="Open menu"]` selector
is the reference's DOM idiom; the clone's burger carries NO
aria-label (the sr-only "Toggle Sidebar" span names it — the v7
idiom), so the click failed silently under the `|| true`. The
mobile nav itself verified WORKING via the eval flow: the sheet
opens 5 links, the Income nav navigates AND the sheet closes AND
the overlay clears, the Escape closes it; the 7 mobile-nav e2e
tests pass in the 241 run. **The stale selector became the v52 P1
fix (a scripts/ change).**
The trap-log scan CLEAN: a scripted negative-margin sweep across
all 39 components — only the two auth back buttons carry `-mb-`,
both inside their converted zb-auth-mode containers.
The v52 sweep — `ref-v52.sh` + `clone-v52.sh` (READ-ONLY on the
reference): the /income view at 390 (the header row's mobile
reflow, the chip, the H1/sub, the Add button, the filter card, the
inner grid, the search, the item grid, the first card) —
BYTE-PARITY; the /expenses view at 390 (the same family + the
4-child/3-trigger filter grid) — BYTE-PARITY. The item-details
sheet's internals at 390 — **ONE REAL GAP: the summary's missing
SUBCATEGORY P.** The first census read the reference's sheet via
the h4 click — "no dialog": the reference's sheet carries NO
[role=dialog] (the no-landmark family); the card-body click + the
`fixed inset-0 z-50` overlay census found it. The reference's
summary dump: the chip row → the H3 `text-2xl font-bold mb-2` →
**the P `text-lg` 18/400/rgb(107,114,128)** ("Apartment" on Rent /
"Main Job" on Salary) → the amount P. The clone rendered the H3 →
the amount directly. The subcategory field was always on the
clone's model (the card renders it, the edit dialog edits it) —
the details view never wired it. A mid-flow session expiry forced
a re-login; the post-restart census then read the DESKTOP filter
grid ("215.5px" tracks) — the viewport state does not survive a
session restart (the re-apply + the re-measure got the true 390
census). The sheet's other internals: byte-parity (the sticky
header 69, the title 18/700, the close 36, the body, the
classification block, the facts, the meta footer).
The remediation plan v52 written + validated (the insertion point,
the 85vh cap arithmetic — no existing geometry pin affected; the
v28 summary assertions walk the H3's role, unaffected).
The TDD cycle: the F1 RED pin (the subcategory P visible + its
chrome + the H3→P→amount sequence) — **RED CONFIRMED** (the P
absent; the F4 internals test beside it GREEN immediately, modulo
two pin transcription fixes: the chip row's gap is gap-2 8px, and
rounded-full computes 3.35544e+07px on v4 — the CLASS is the
contract). The one-insert fix (the conditional P between the H3
and the amount). The chain-gate catch: the first rebuild FAILED on
TS18047/TS2345 — the new items.spec.ts census code's
`h1.closest()` null-safety (Playwright does NOT typecheck; the
third application of the v51 TS lesson). Fixed with explicit null
guards. **GREEN: all four v52 tests.**
The mutation series (each with the standalone REBUILD): (a) the
subcategory P removed → F1 FAILS (the RED run itself); (b) the
income chip's gradient removed → F2 FAILS; (c) the filter p-6 →
p-4 → F2 AND F3 FAIL; (d) the details header's py-4 → py-2 → F4
FAILS; (e) the H1's text-3xl → text-2xl → F2 AND F3 FAIL. All
restored — the clean diff: item-details-dialog.tsx +17 + the two
specs.
The P1 fix applied + verified: the standing script's R1 now reads
"burger clicked" + sheetLinks: 5; R2 /income + closed; R3/R4/SEO
green.
The full chain: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ ·
**245/245 e2e (5.5m — clean on the FIRST run)** · 35/35 smoke ✓.
The VLM pair (the /expenses view at 390 — the F3 surface): 4
flags — the header count/total, the card contents, the Base44 FAB
(mislabeled by the VLM — it is the reference's own platform
chrome), the layout length — ALL the documented seed-data/platform
classes.
The 16 screenshots regenerated (ONE byte-diff: 16-item-details.png
— the fix's visual effect). The docs aligned (AGENTS / CLAUDE /
README / PAD v1.1.9 / the SKILL Session 87 row / the probe
README's v52 section / session_122 + session_123 / the repo
worklog Session 86 + the ledger list). Commit + push to main via
the SSH wrapper.
