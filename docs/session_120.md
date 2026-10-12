# Session 120 — the v51 session's raw tool-call narrative (2026-10-12)

The condensed transcript of the session that delivered
`docs/remediation-plan-v51.md` (parity iteration v51 — the
verify-email mode container's missing `.zb-auth-mode` conversion FIX
+ the stats-row / savings-view / Budget-Guidelines / quick-actions
390 pins).

The workspace SURVIVED — `git pull` fast-forwarded f807aac →
7a7f912 (session_118.md, the v50 session's narrative + the v51 queue
suggestions: the verify-email panel census, the forgot-confirm
census, the hero stats-card row at 390, the savings goal-card mobile
census). The five core docs + the four session docs reviewed — the
v50 state verified (the .zb-auth-mode rules in globals.css, the
signup/forgot container swap, 236 e2e).
The baseline chain GREEN on the first run: lint ✓ · typecheck ✓ ·
108/108 unit ✓ · build ✓ (the sitemap/robots pair prerendered) ·
**236/236 e2e (5.4m)** · 35/35 smoke ✓. npm audit: 0 production
vulnerabilities. `.env` ≡ `.env.example`.
The 45th standing checks (both sides, the v49 scripts verbatim):
the reference's four bugs ALL live (the toast-blocker; the
sheet-trap via the overlayCount — `sheetOpenAfterNav false,
overlayCount 1`; no landmark; the 464 /networth overflow); the data
census read-only and intact; the SEO pair live on both; the clone's
R1–R4 + SEO green.
Now the v51 sweep — `ref-v51.sh` (READ-ONLY): the STATS ROW at 390
(the grid 1-col/24px, the cards 210 @ 949/1183/1417, the radius-16
card, the icon circle 48, the title/amount/countRow — but the
AMOUNT finder missed: the reference's amount starts with "$" and
the probe's regex keyed on a bare digit — the follow-up census
caught it: 30/700/rgb(26,58,46)/mb 16). The SAVINGS view: the
first card census EMPTY (the h4 finder — the reference's card
titles ARE h4s but the fresh session wasn't logged in: the
page was the LOGIN screen; re-login → the census: the goal card
358×200, radius 12/pad 20, the rgba(0,0,0,0.04) 0px 2px 8px shadow,
the H4 16/600/forest, the amount 24/700/rgb(59,126,161), the
8×8 dot, the badges need/monthly/active). The GUIDELINES card: the
full shadow re-measured UNSLICED (4 layers: 2 transparent leads +
the shadow-sm pair; the probe's 60-char slice hid the pair). The
clone side (`clone-v51.sh`): the stats row IDENTICAL (the cards
358×210 @ the same y's); the savings view — the H1 finder hit the
CLONE'S HIDDEN H2 brand (18px, the desktop sidebar's BrandMark —
the v7 G4 idiom) before the 20px H1 top-bar brand (the visibility
check: the H2's rect is 0×0, display block, NOT visible — a probe
artifact, not a drift); the goal card 230 vs 200 — the inner
census isolates it to the badges row (the clone's 4 chips wrap to
52px vs the reference's single 22px row — the richer seed's data
class) + the footer's payment-method span (data). The guidelines
IDENTICAL (h 380 on both, the tiles 94/94/78, the tinted pairs
byte-identical). The follow-up quick-actions census (the walk from
the "Add Income" button up the chain): the BUTTON itself is the
card (p-6 rounded-2xl, 90 tall), the 40×40 circle, the trailing
plus's full class string `ml-auto opacity-50
group-hover:opacity-100 transition-opacity` — IDENTICAL on both
sites (the cards' y 2751/2865/2979 byte-identical — the full-page
rhythm).
FOUR PIN-ONLY SURFACES — but the task asks for a real audit: the
systematic Tailwind v4 trap-log scan (a scripted space-y ×
mt/mb-utility audit across all components) flags seven sites; six
are false positives (grandchildren — the scanner's line-walk
heuristic) or measured-safe (the pins green). The seventh: the
login-card VERIFY branch — **the v50 F1's third-site conversion was
CLAIMED but NEVER APPLIED.** The git diff of the v50 commit shows
it: the comment at login-card.tsx:605-607 landed, the line-608
class swap did not. The verify branch still reads `space-y-4` with
the -mb-2 back button — the SAME v4 trap.
The measurement (a fresh CLONE-side registration — the reference
stays read-only): the first attempt "registered" but stayed on
/login (the sign-up form carries THREE inputs — email + password +
Confirm Password; the two-field fill never submits, native
validation blocks it silently). The three-field fill lands the
verify state: the panel 492, the wrapper 540, the junction netGap
−8 (the inner stack's top 196 vs the button's bottom 204 — the
8px OVERLAP), the mode container `space-y-4`.
The remediation plan v51 written + validated (the existing verify
pins walk the controls — the panel/junction were never pinned; the
F2/F3/F4/F5 targets byte-verified in the source). The plan's
deferred queue: the reference-side verify + forgot-confirm
censuses (both WRITES — out of bounds).
The TDD cycle: the F1 RED pin (the modeCls + the panel 508 + the
wrapper 556 + the y 144 + the junction netGap 8) — **RED
CONFIRMED** (the modeCls assertion fails on `space-y-4`). The
one-class fix (login-card.tsx:608 → `zb-auth-mode`, no zb-sm6 — the
verify container carries no sm tier). The first GREEN run: the
panel **528**, not 508 — the email-length finding (the 38-char
throwaway address wrapped one extra line in the "We've sent a
6-digit code to {email}" block, +20px). The fix's fix: a FIXED
21-char email (the global-setup re-seeds db/e2e.db every run —
the address is reusable) → **GREEN: 508/556/144 + the junction
netGap 8 (the button bottom 196, the inner top 204).**
The F2/F4/F5 pins (dashboard.spec.ts, a 390 describe) + the F3 pin
(items.spec.ts): GREEN on the first run except F5's circle finder
(the quick-action circle is a SPAN in the clone, a DIV on the
reference — tag-agnostic, the finder extended to "span, div").
Then the chain-gate catch: `npm run build` FAILS on TS2774 —
the `c.querySelector &&` always-defined check in the new F2 census
(**Playwright does NOT typecheck** — the tests ran green at
runtime; `next build`'s tsc bit). The check removed; the build
green.
The mutation series (each with the standalone REBUILD): (a) the
zb-auth-mode removed → F1 FAILS (the RED run itself); (b) the stat
card's rounded-2xl → rounded-xl → F2 FAILS (radius 16 → 12); (c)
the goal card's inline shadow removed → F3 FAILS; (d) the Needs
tile's bg removed → F4 FAILS + the 1280 tinted-cards pin; (e) the
quick-action circle's w-10 h-10 → w-8 h-8 → F5 FAILS. All
restored — the clean diff: login-card.tsx ±8 + the three specs +
the docs.
The full chain: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ ·
**241/241 e2e (5.6m — the third run; the first two runs each
flaked ONE not-found test, a DIFFERENT test each time, both 7/7
standalone — the spec's known flake family)** · 35/35 smoke ✓.
The VLM pair (the /savings view at 390 — the F3 surface): 3 flags
(the count subtitle / the card contents / the extra-card length) —
ALL the documented seed-data classes (the v48 precedent's second
application; the chrome byte-pinned by F3).
The 16 screenshots regenerated. The docs aligned (AGENTS / CLAUDE
/ README / PAD v1.1.8 / the SKILL Session 86 row / the probe
README's v51 section / session_119 + session_120 / the repo
worklog Session 85 + the ledger list). Commit + push to main via
the SSH wrapper.
