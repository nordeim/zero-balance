# Session 117 — the v50 session's raw tool-call narrative (2026-10-12)

The condensed transcript of the session that delivered
`docs/remediation-plan-v50.md` (parity iteration v50 — the auth
states' panel-heights FIX + the networth tablist's 640 chrome pin +
the dashboard hero's 390 reflow pin).

The workspace was RESET — no zero-balance/ directory. Fresh `git
clone` at 3f0202e (the v49 session-log commit; the v49 parity commit
27df57b below it). session_115.md reviewed: the v49 session's own
narrative — the login spacer fix delivered, the v50 queue suggested
(the auth states' 390 census / the networth 640 tablist / the hero
mobile reflow).
Now the five core docs' latest-state sections (the AGENTS v49
paragraph, CLAUDE's state line, README's v49 row, the PAD's v1.1.6
block, the SKILL doc's Session 84 row) — all aligned with 232/232.
The environment rebuilt: npm install, .env from .env.example,
db:push + db:seed (7 items / 3 assets / 2 liabilities — the demo
workspace).
Lint ✓. Typecheck ✓. 108/108 unit ✓. Now the build — but the e2e
first run fails: "Executable doesn't exist at
chromium_headless_shell-1243" — the fresh sandbox needs `npx
playwright install chromium` (the 114.3 MiB download). Re-run:
**232/232 e2e ✓ (5.4m).** Smoke: **35/35 ✓ — the baseline chain
GREEN.**
The audit: npm audit = the same 5 dev-only advisories (--omit=dev =
0), the secret scan clean (the probe credentials are by-design
inputs), .env ≡ .env.example.
Now the 44th standing checks — the reference side first
(ref-standing-v49.sh verbatim): the toast-blocker live (the hit
`DIV.fixed top-0 z-[100]`, hitIsBurgerChild false), the sheet-trap's
heuristic detector reads false again (the known artifact — the
text-keyed heuristic misses the empty-text overlay) — re-verifying
with the PRECISE overlay census: the z-50 rgba(0,0,0,0.8) 390×844
scrim STILL open on /income after the nav click. R-bug 2 CONFIRMED
live. R-bug 3 (no landmark) + R-bug 4 (the 464 overflow) live. The
data census read-only. The SEO pair live. The clone side
(standing-checks-v49.sh via with-server): R1-R4 + SEO all green.
**The 44th standing checks ALL CLEAN.**
Now the v50 sweep — ref-v50.sh (the reference side, READ-ONLY). REF
surface 1a (the sign-in baseline at 390): the wrapper 730 / the panel
682 / y 57 — the v49 F1 contract holds. REF surface 1b (the sign-up
state swap): the wrapper 470 / the panel 422 / y 187, the heading 20/
700, the 3 inputs 40px, the submit 40px w 294, the back link 14px.
REF surface 1c (the forgot state): the wrapper 358 / the panel 310 /
y 243. REF surface 2 (the tablist at 640): the list 448/36/grid 220px
220px/#f5f5f5/8px/4px; the trigger pair's full chrome. REF surface 3
(the hero at 390): the eval returns EMPTY — the goal-heading walk
mis-fired; surveying the headings (H3 "NET ZERO GOAL" 18px exists),
re-censusing with a radius+shadow+width walk: the card 363×316 (the
reference's 395 overflow), the grid 1-col/24px, the figure 30/700
white. The internals census (two parts): the icon circle 48/
rgba(143,188,63,0.2)/the 24px svg; the h3 18/700/white/lh 28; the
sublabel; the allocation row; the track 299×12; the fill's 90deg
orange gradient; the balance box 299×108/12px/24px/0.05/blur(10px);
the figure; the chip — the census of the balance box's children
finds the chip box (flex gap 8): the svg 12×20 rgb(245,169,98) + the
span "Under Budget" 16/600 rgb(245,169,98). The svg's class is
`lucide lucide-trending-up w-5 h-5` with computed 11.7px width — the
flex-shrink squish (the reference's own width pressure).
Now the clone side — clone-v50.sh. THE FIRST RUN HANGS (600s): a
stale `clone50` session pair from the killed run. The lesson: pkill
+ a session-file sweep before every probe run. The re-run (the
direct variant against the pre-booted :3200 server): the clone's
sign-in IDENTICAL (730/682/57); the sign-up 454/406/195 and the
forgot 342/294/251 — **the panels 16px SHORT.** The tablist
IDENTICAL. The hero IDENTICAL (the goal card 358×316@253, the
breakdown 324@593, the internals, the chip — the SAME 12×20 squish).
The drift isolated: the inner census on both sites — the reference's
container `space-y-4` (the H2 mt 16, the form mt 16 — v3 semantics)
vs the clone's (the H2 mb 16, the form mt 0, the H2 at y 12 — the
OVERLAP). The v4 space-y zero-specificity margin-block-end × the
button's own -mb-2 override. The forgot container: the reference's
`space-y-4 sm:space-y-6` vs the clone's bare `space-y-4` — the sm
tier missing too.
The remediation plan written (docs/remediation-plan-v50.md) and
validated against the codebase (login-card.tsx:693 + :603, the
existing pins' safety). Now the TDD: the F1 pin written RED — both
tests FAIL against the pre-fix build (the wrapper 454/342). The fix
applied (the .zb-auth-mode + .zb-sm6 rules + the class swaps) — but
the first attempt's zeroing rule (`> :not(:last-child)
{ margin-block-end: 0 }`, the v9/v24 idiom) measures 478/430: the
0-2-0 zero BEATS the button's -mb-2 utility (0-1-0) and kills the 8px
collapse. The correction: the container DROPS the space-y class
entirely (v4's emission never matches — no zeroing needed). Rebuild
→ the stack finder needs a fix (an ancestor-match found the content
div; the forgot heading is a wrapped div not a direct h2) →
**GREEN: 422/470/187 + 310/358/243 + the 640 sm tier 24px.**
F2 (the tablist pin) — the first run fails on the shadow layer count
(2 expected, 6 received): the v49 probe's 50-char slice hid the full
string. Re-measuring the reference UNSLICED: 2 transparent leads +
the shadow-sm VISIBLE pair (4 layers); the clone: 4 leads + the pair
(6) — the accepted lead-divergence class, the visible layers
byte-identical. The pin corrected to the visible pair → GREEN.
(Mid-run the :3200 server died — the browser's "This page couldn't
load" interstitial: the rebuilds swapped .next/standalone under the
running server. Rebooted.)
F3 (the hero reflow pin) — GREEN immediately (pin-only).
Now the mutation series (each with the standalone REBUILD):
(a) the zb-auth-mode removed → both F1 tests FAIL (406/294);
(b) the -mb-2 removed → F1 FAILS (the wrapper 478 = +8);
(c) the zb-sm6 removed → the 640 sub-check FAILS (mt 16 not 24);
(d) the active-tab bg removed → F2 FAILS;
(e) the hero track's h-3→h-2 → F3 FAILS.
All restored — the diff: globals.css +28 / login-card.tsx ±14.
The full chain: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ ·
**236/236 e2e ✓ (5.4m — one flaky not-found metadata test on the
first run, clean on the re-run)** · 35/35 smoke ✓.
The VLM pair (the login SIGN-UP state at 390 — THE FIXED SURFACE):
the VLM says DIFFERENT with 4 flags (the card position / the button
width / the spacing / the shadow depth). DOM-verifying every flag:
the panel y 187 / h 422 / the button 294@x 48 IDENTICAL on both
sites — ALL NOISE (the v43 misattribution lesson's fifth
application).
The 16 screenshots regenerated (7 byte-diffs). The docs aligned
(D1-D8: AGENTS / CLAUDE / README / PAD v1.1.7 / the SKILL doc's
Session 85 row / the probe README / session_116 + session_117 / the
repo worklog Session 84). Commit + push to main via the SSH wrapper.
