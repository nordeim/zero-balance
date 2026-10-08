I'll continue the zero-balance remediation task from where we left off. The brief now references `docs/session_20.md`, `docs/remediation-plan-v10.md`, and `docs/session_21.md` — the repo has advanced further, so let me refresh the workspace and re-establish context.
Workspace refreshed — `docs/session_21.md` pulled in, and the repo has already completed parity iterations v8–v10. Let me review the core project docs and the latest session history per the brief.
`session_21.md` confirms the repo state: parity iteration v10 is complete and pushed (`cf66a57`). The convention is clear — each session runs a fresh two-site verification audit, fixes remaining gaps TDD-first, then commits and pushes. My current task is the next iteration (v11). Let me review the remaining docs per the brief.
Now let me review the remaining core docs — CLAUDE.md, README.md, the architecture doc, the SKILL doc, and worklog.
The pattern is now clear. The last work session (19, recorded in session_20/21.md) shipped parity iteration v10 with everything green: 96 unit / 104 e2e / 30 smoke. My task is the next fresh verification & parity iteration (v11). Let me review the remaining docs and validate the environment.
Environment intact: `.env` has the right `DATABASE_URL="file:../db/custom.db"`, `db/custom.db` exists at repo root, `.env.example` matches. Now let me check the SKILL doc's current state and lessons, plus the skills catalog.
I now have complete context. The repo is at parity iteration v10 (all green: 96 unit / 104 e2e / 30 smoke). This session continues the established pattern: **fresh verification & parity iteration v11**. Let me set up the task plan.
**Task type: code repo remediation (continuation session).** Now validating the codebase — spot-checking v10 pins and the parity infrastructure.
v10 pin confirmed in code. Now running the baseline verification chain — lint, typecheck, and unit tests first.
Lint ✓ · typecheck ✓ · 96/96 unit ✓. Now the production build (required for e2e and the parity server).
Build ✓. Now the e2e suite (104 tests) — no live browser sessions are open, so the resource-pressure trap from session 17/19 is avoided.
104/104 e2e ✓. Completing the baseline chain with the 30-step API smoke test.
**Baseline chain fully green at `061a16f`**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ · 104/104 e2e ✓ · 30/30 smoke ✓. Now setting up the audit infrastructure — let me check the probe README and agent-browser state.
No active sessions. Setting up the four audit sessions — reference desktop first.
Reference logged in. Let me check the probe runner pattern before setting up clone sessions.
Now the clone desktop session — full login flow in one `with-server.sh` invocation.
Both desktop sessions live. Now the mobile sessions (390×844).
The mobile login form needs more time to hydrate. Retrying after a wait.
All four sessions live and logged in. Starting the audit — data drift check first.
**Data drift check: reference UNCHANGED** since session 19 (allocation 30.5%, expenses $525/4 items with the documented $0.00 residual) — clone seed arithmetic intact. Donut legends on both sides render value-DESC per the v9 pin. Now the mobile navigation task-focus re-verification.
R4 re-confirmed (395px overflow) + R1's toast container present. The probe's burger selector didn't match — let me find it directly.
Burger found: 28×28 at (24,16), "Toggle Sidebar". Now the R1 hit test at its center.
**R1 + R4 re-confirmed live**: ref's toast container intercepts the burger hit (DIV, not burger); clone's hit is direct (svg inside burger). Ref overflows to 395px; clone fits exactly 390. Now R2 — opening the ref's sheet via programmatic click (its overlay refuses real clicks).
Ref sheet open at 288×844 with all links inactive (root-route bug — documented superset #3). Now R2: tapping Income in the ref's sheet.
**R2 re-confirmed**: ref navigated to `/income` but the sheet stays open (trap). The v10 finding re-confirmed too — its sheet highlights Income (white + gradient + fw 500). Now the clone's full mobile flow.
Quoting issue — using the established base64 probe pattern instead.
Clone's sheet highlights Dashboard on `/` (v10 fix + superset #3 intact). Now R2 on the clone — tap Income, verify the sheet closes.
The sheet is still open — I need to run the tap probe first, then re-check.
**R2 clone fix verified**: navigated to `/income`, sheet closed, fits 390px. Mobile nav task-focus re-verification complete — R1/R2/R4 all live on the ref, all clone fixes intact.

Now the fresh-angle audit v11. First angle: **intermediate breakpoints (tablet)** — never measured across 10 iterations.
Ref renders the 256px fixed rail at both 768 and 1024 (burger hidden at 0×0). Now the clone at the same widths.
Identical at 768/1024. Now the boundary — 767px (one below the md breakpoint) on both sites, plus the main-content offset at 768.
767 boundary identical. Now the content offset at 768 (rail active) on both.
**Potential finding at 768px**: ref's `main` starts at x=256 (offset by the rail), clone's `main` at x=0 — possible rail/content overlap in the 768–1023 range. Let me investigate precisely.
The layouts are structurally different but likely visually identical — the ref positions `main` at x=256 while the clone uses `md:pl-(--sidebar-width)` padding. Let me verify the actual visible content position on both.
Tablet layout verified identical (NET ZERO GOAL card at 288/200/448 on both). Next angle: **desktop rail hover state** — never measured.
Synthetic events don't trigger CSS `:hover`. Using agent-browser's native hover with a href selector.
Ref rail hover: color `rgb(24,24,27)`, bg `rgb(240,253,244)`. Now the clone's.
Rail hover identical. Next: **hero status conditional** (Under Budget state) on both.
The probe matched the "NET ZERO GOAL" heading instead of the status badge. Fixing the probe and resetting the clone viewport to 1280.
**Hero status badge identical** (label #0a0a0a 16/400 + value `rgb(245,169,98)` 16/600 — both "Under Budget"). Next: **filter card** — geometry + functional behavior on `/income`.
Filter geometry identical. Now the functional test — typing a search term on both.
Filter behavior matches. But I spotted a possible badge difference — the ref's card shows "active" while the clone's shows "Recurring". Let me compare the full card badge sets.
The ref's badges didn't match my span filter — let me dump its card structure directly.
Search is reset and the card is visible — my card-finder's `button` requirement was too strict for the ref's DOM. Let me fix the probe to locate cards by amount text.
Badges match (monthly/active identical). But the "need" classification badge didn't appear in the ref's leaf list — let me check it specifically.
Ref's "need" badge: red `#b91c1c`/`#fef2f2`, 71×22 **with an svg icon child**. Let me check whether the clone's has the icon too.
Badge families fully identical (including the svg icon child). Next: **dialog overlay** — opening Add Income on the ref.
**Ref dialog overlay: `rgba(26, 58, 46, 0.5)`** — forest-dark at 50% (not black). Now the clone's.
Clone overlay identical. Let me also grab the ref's dialog panel for completeness.
**FINDING (v11-G1)**: The ref's dialog panel renders **no box-shadow** (all-transparent layers); the clone renders shadcn's `shadow-xl` (`rgba(0,0,0,0.25) 0 25px 50px -12px`). Both panels are otherwise identical (672×720 @ (304,40), white, radius 16). Let me close both dialogs and check the mobile sheet's shadow too.
Both surfaces confirmed: the ref renders NO shadow on the sheet either, while the clone's SheetContent carries `shadow-lg`. Let me examine the full dialog component.
The DialogContent uses `zb-modal-panel` — the shadow must live in globals.css. Let me check.
The clone's shadow comes from `.zb-modal-panel`'s `box-shadow` in globals.css. Let me get the ref panel's FULL shadow string to be certain no visible layer exists at the end.
**Correction — the ref's FULL shadow string includes the identical visible layer** `rgba(0,0,0,0.25) 0 25px 50px -12px` as its third layer; my earlier slice cut it off. Dialog panel shadows are identical. Same check needed for the sheet — let me get its full string.
Ref sheet has `shadow-lg` layers. Confirming the clone's sheet shadow matches.
Clone sheet shadow identical (same visible shadow-lg layers). Shadows all match — and a methodology lesson: computed `box-shadow` must be read in full, never sliced. Let me close the clone sheet and check the **logout flow** — the user avatar/footer block.
The ref's rail footer is a static block — **no logout button**. Let me sweep the ref for any logout affordance, then compare the clone's.
The ref has **no logout UI** (static footer block) — the clone matches it visually while keeping the store/API logout capability. That's a documented observation, not a change. Next fresh angle: the **filtered empty state** (search "zzz" → 0 results) — a different state from the v6-pinned initial empty state.
Ref filtered empty state captured (icon 64×64 op 0.2, heading 20/600, desc 16px). Now the clone's.
**FINDING (v11-G1)**: empty-state heading — ref renders **20px**, clone renders **18px**. Everything else matches (icon 64×64 op 0.2, mb 8px, desc 16px, block 960×328). Let me check the clone's code.
**Code confirms it**: `items-view.tsx:237` uses `text-lg` (18px) — the ref renders 20px. Let me check the other empty-state surfaces (net-worth tabs, calculator) in the clone's code.
Now measuring the ref's other empty states live — net-worth tabs and the calculator.
The ref's net-worth empty state is unreachable without destructive data mutation (both tabs have data) — skipping that (will handle by code symmetry). Now the calculator empty state on the ref.
The ref's "Miscellaneous $0.00" item (v10 residual) has no line items — opening its calculator to see the empty state.
**Calculator empty state: identical** (icon 48×48 op 0.2 mb 12, text 14px/400 mb 16, no heading — v6 pin holds). The finding is isolated to the empty-state **heading size**. Let me check what the existing e2e spec pins.
The existing spec pins structure but not heading size — a genuinely unpinned dimension. Let me check if the ref's net-worth view has a filter (to reach its empty state without mutation).
No filter on the ref's net-worth — its empty state is unreachable live. Let me check how the v6 audit measured it (session-11 had the same problem).
The v6 audit reached the ref's net-worth empty state via a delete/restore dance but never recorded the heading size. Let me check how many liabilities the ref has — if few, the dance is cheap.
The ref has **zero liabilities** — its Liabilities tab shows the empty state directly! Let me switch and measure.
The content still shows Assets — let me inspect the tab elements' state directly.
Tab switched — content is now short (empty state). Measuring it.
The programmatic click isn't switching the tab. Using agent-browser's native click with an xpath selector.
Tab switched — the empty state is live. Measuring its computed styles.
**Net-worth empty heading also 20px on the ref** (in the carded variant: 960×330, white, radius 16, pad 64). Finding G1 confirmed for both view families. Now the button focus-visible state (buttons — v10 covered inputs only) and the Add-button hover.
The ref's focus ring renders via box-shadow (1px #0a0a0a + white inner) with a transparent 2px outline. Retrying the clone dialog with a longer hydration wait.
The clone's dialog is open but the Save button didn't match. Let me dump the dialog's buttons.
Structure difference: the clone's Radix panel is a portal sibling of the overlay, not a child. Fixing the probe to search the panel.
`.zb-btn-add` has no focus-visible styles. The ref's ring composition also reveals a shadow-scale difference. Let me check the clone's `--shadow-sm` definition.
The globals.css trap-5 pin says `--shadow-sm: 0 1px 2px 0 rgb(0 0 0/0.05)` was "the reference geometry" — but my live measurement shows the ref's Save button carrying the two-layer v3-style shadow. Let me read the validation report's trap 5 to reconcile.
History reconciled: trap 5 pinned `--shadow-sm` for the *navbar* surface, but the ref's dialog buttons carry v3's **bare shadow** (2 layers, 0.1) — a different slot. Let me measure the full button-shadow census on both sites (Cancel, Save, page Add).
**Findings crystallizing**: the Cancel matches, but the **Save/Add (zb-btn-add) family** renders a one-notch-lighter ambient shadow (0.05/1-layer vs ref's 0.1/2-layer) and lacks the ref's focus-visible ring (browser default instead). Plus a 4px width gap on the page Add button (147 vs 151). Let me pin down the width difference.
**Root cause found**: the clone's Add-button Plus icon renders 20px vs the ref's 16px. Let me find the icon in the code.
Plus-icon census: the clone renders `h-5 w-5` (20px) on page/empty-state/net-worth/dashboard Add buttons while the calculator and Save buttons already use 16px. Let me verify the ref's icon sizes on those other surfaces.
The ref's Add Asset: 134px with a 16px icon. Let me also check the ref's dashboard Add button (the breakdown quick-add surface).
Two patterns on the ref's dashboard: quick-add "Add Item" 16px icon, but the stat-card Add buttons (304×90) carry **20px** icons. Let me check the clone's stat-card buttons.
The QuickActionCard chip icon (h-5 w-5) matches the ref's first svg (20px). Let me check the ref's trailing Plus icon inside those buttons.
QuickActionCards already match. Let me verify the ref's empty-state Add button icon + the clone's dialog Save icon sizes.
Empty-state Add also 16px on the ref. One more fresh angle — **stat card ambient shadows** (never measured).
Stat cards identical. Let me complete the button-shadow census with the calculator's Add Item (sm variant) and its outline empty-state button on the ref.
Ref calculator: panel 768×515, "Add Item" gradient carries the v3 bare-shadow, "Add First Item" outline carries v3 shadow-sm. Let me verify the clone's calculator panel + buttons.
Calculator panel identical; the button shadows confirm G2 across all three variants. Let me measure the ref's outline-variant focus state (Add First Item + Cancel).
The ref's outline-variant focus uses the same ring + its lighter ambient. Let me verify the clone's Cancel (Button primitive) focus matches.
The Cancel primitive already matches (ring + ambient + invisible outline). The audit is complete — 3 finding groups. Let me grab the heading line-height detail for the G1 fix, then write the remediation plan.
Both headings share lh 28px — the swap won't shift block heights. Let me review the current zb-btn-add CSS variants before writing the plan.
One more state check — the Add button's hover state on the ref (the clone pins `opacity: 0.9`).
**Ref hover: opacity stays 1** — the clone's `:hover { opacity: 0.9 }` looks like drift. Let me check the git history/docs for where that came from.
The `opacity: 0.9` hover dates to the original build — never measured against the ref. Let me confirm on more surfaces (the ref's Save Item + dashboard Add Item hovers).
**G4 confirmed on all three gradient-button surfaces**: the ref keeps opacity 1.0 on hover — the clone's 0.9 fade is an unmeasured session-1 assumption. The audit is complete with 4 finding groups. Now writing remediation plan v11 — first, let me review the spec structures for TDD placement.
Now let me validate the exact fix sites in the code before writing the plan.
All sites validated. Writing remediation plan v11.
Plan saved and validated. Now the TDD RED phase — writing the new specs. First, let me read the net-worth empty-state test to extend it.
Let me check how the existing calculator test opens the calculator dialog, then write all RED specs.
Now writing the RED-phase spec changes — empty-states first.
Now the new dialog-buttons test for G2 (ambient shadows + focus ring).
Now the tokens.spec test for G3/G4. Let me check the file's end structure.
TS's DOM lib lacks the newer `focusVisible` option. Fixing with a documented cast (runtime support confirmed by the live probes).
Typecheck + lint pass. Now the RED phase — but first, closing the live browser sessions (session-17/19 lesson: they crash e2e runs under memory pressure).
RED confirmed for the G2 test. Now running the other new assertions (empty-states extensions + tokens v11).
**RED fully confirmed — 5 tests failing for exactly the right reasons** (2× heading 18px, 1× shadow+ring, 2× icon/hover). Now implementing the fixes (GREEN phase).
Applying the G3 icon fixes with targeted replacements.
G1 + G3 applied (7 icon sites + 3 headings; calculator's 2 pre-existing 16px icons untouched). Now G2 + G4 in globals.css.
All fixes applied. Rebuilding for the GREEN run.
**GREEN — 26/26** in the affected files. Now the full verification chain.
106/107 — one failure in the not-found spec (unrelated surface). Checking whether it's a flake or a real regression.
Flake confirmed (passes in isolation) — a known navigation-timing race under full-suite load. Re-running the full suite for a clean gate.
**Full chain GREEN: lint · typecheck · 96 unit · build · 107 e2e · 30 smoke.** Now the live side-by-side parity re-verification of every fixed surface with fresh sessions.
**G3/G2a/G4 verified live**: button 147 = 147, icon 16 = 16, identical visible shadow layers, opacity 1. Now G1 (empty heading) and G2's focus ring.
**G1 verified: 20px/600/28px both sides.** Now the G2 focus ring + calculator variants + hover on the clone.
**G2c verified — byte-identical ring composition to the ref.** Now the calculator variants and hover.
All calculator variants identical to the ref. All four fixes verified live. Now regenerating the screenshot catalog (the Add buttons carry visible deltas: icon size + shadow).
All 13 screenshots regenerated (10 show the Add-button deltas; login/mobile-menu/not-found unchanged as expected). Now the documentation alignment.
Now CLAUDE.md.
Now AGENTS.md — adding the v11 pin paragraph.
Now the SKILL doc — state, lesson, Appendix B.
Now the probe README v11 rows.
Now the formal session log — `docs/session_22.md` (session_21.md holds the incoming conversation summary, so this session's log continues the numbering).
Now the repo worklog entry.
Now the shared workspace worklog.
Docs aligned. Now the final phase — commit and push. Let me read the SSH wrapper runbook.
The runbook is clear. Let me check the ssh shim from previous sessions and verify the wrapper.
The shim exists at `/home/z/my-project/bin/ssh` and the wrapper defaults to the old repo — I'll pass `--remote` explicitly (session-19 precedent). Final review of the change set + secret scan before committing.
Clean change set, no secrets. Verifying `.env.example` is tracked, then committing.
Committed as `00dad5a`. Now the push — writing the operator key to a 0600 file outside the repo.
Dry-run green — clean fast-forward. Executing the real push.
**Session complete — parity iteration v11 shipped to main as `00dad5a`, push verified, key shredded.**

**What I did this session:**
- Pulled to the latest HEAD, re-read the full doc chain, and confirmed the v10 baseline green (96 unit / 104 e2e / 30 smoke)
- Re-verified the mobile-navigation task focus end-to-end: the reference's bugs are all still live (toast-blocked burger, sheet-trap, 395px overflow) and all six clone superset fixes intact — including v10's sheet active-highlighting
- Ran a fresh two-site audit with first-ever measurement angles: tablet breakpoints (767/768/1024), rail hover, hero status badge, filter behavior, button shadows/focus/icons — and defused one near-false-finding (computed box-shadow strings must be read in full)
- **Fixed 4 drift groups TDD-first**: empty-state headings 18→20px, the `.zb-btn-add` shadow + focus-ring family, 16px Add-button icons, and removed the unmeasured hover fade — final chain **96/107/30 all green**, live parity re-verified side by side, screenshots regenerated, docs aligned, committed and pushed via the SSH wrapper

**Suggested next steps:** run another verification pass anytime (each sweep finds new state dimensions — v11's findings survived ten passes precisely because button internals were never measured), wire real OAuth for "Continue with Google", or set up hosted CI to run the gate on every push.
