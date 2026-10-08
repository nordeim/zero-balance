I'll continue with the task. Let me start by setting up a todo list and refreshing the workspace.
The workspace exists with prior work (db/, vitest.config.ts, playwright.config.ts present). Let me check git status and pull the latest.
Pull succeeded — brought in `docs/session_27.md`. The local repo already has all prior parity work (v13). Now let me review the project docs.
Now let me read CLAUDE.md, Project_Architecture_Document.md, and zero-balance_SKILL.md.
Let me read the key sections of the architecture doc and the skill file.
Session 26 (v13) is complete and pushed. Now let me review remediation-plan-v13, worklog, and the SKILL doc.
Now let me review the SKILL doc's key sections (state, lessons, appendix) and verify the environment state.
I now have a complete picture of the project state. Let me verify the environment and read the global worklog.
Environment is intact — all standing brief requirements (DATABASE_URL, db/ at root, .env.example, Vitest, Playwright) are in place. Let me read the global worklog and check the skills catalog.
I have full context now. This will be **work session 27 / parity iteration v14**. Let me update the plan and check the skills catalog for the audit phase.
Skills catalog confirmed. Now let me validate the v13 pins in the code and review the v13 changeset.
All three v13 pins confirmed in code. Now let me run the baseline verification chain.
Lint ✓ · typecheck ✓ · 96/96 unit ✓. Now the production build.
Build ✓. Now the e2e suite (115 tests) — this needs a clean memory state per the README warning about browser sessions.
One flaky navigation test (the known timing-race class from session 21). Let me re-run that spec in isolation.
Flake confirmed — passes in isolation. Now the API smoke test.
**Baseline chain fully GREEN**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ · 115/115 e2e ✓ · 30/30 smoke ✓. Now the code audit phase (security + quality review of the v13 changeset).
Audit complete: security scan matches the documented state (dev-only braces advisory, no patched release), secret scan clean, v13 changeset reviewed clean. Now let me set up the two-site parity audit infrastructure.
I need to reconstruct the per-command parity server wrapper. Let me check git status and set up the audit infrastructure.
Reference logged in. Let me check the viewport size and adjust if needed.
ref15 set to 1280×800. Now the clone desktop session — login flow inside one with-server invocation.
Both desktop sessions logged in. Now the mobile sessions (390×844) — reference first.
Reference mobile logged in — R4 visible already (scrollWidth 395 at 390). Now the clone mobile session.
EAGAIN — resource pressure. Let me check daemon sessions and recover.
All four sessions live. Now the data drift check + dashboard verification on both sites.
Data drift check clean — reference unchanged, clone seed intact. Now the mobile-nav task-focus re-verification.
**R1 re-confirmed live** — the reference's toast container intercepts the burger's center hit. Now R2: open the sheet via the exposed bottom half and test the trap.
**R2 re-confirmed live** — the reference sheet traps after nav. Now R3: close the sheet, return to root, check active states.
The mobile sheet is closed so nav links aren't in DOM. Let me check R3 on the desktop rail (ref15 at `/`).
**R3 re-confirmed** — no active link on reference root. Now the clone's mobile flow verification.
The clone is logged in with the burger present. Let me click it and measure the sheet.
Clone sheet shows Dashboard active (white + gradient, superset #3). Now the close-on-nav test — tap Income.
Two Income links (hidden rail + sheet). The sheet link is at (20,185) — same as reference. Now tap it and verify close-on-nav.
Sheet closes on nav ✓, 390px fit ✓. Now the clone's burger hit-test (R1 clone side).
**Mobile nav task-focus verification complete** — R1/R2/R3/R4 all live on the reference; all clone superset fixes intact. Now the fresh-angle sweep. First: net-worth tab keyboard flows (suggested by last session).
Reference tablist semantics captured. Now the keyboard flow test on the reference.
**Net-worth tabs: identical both sides** (roles, aria-selected, keyboard activation, geometry). Next fresh angle: dialog initial focus + field-level validation errors.
The reference's dialogs are plain fixed divs (documented R5/R6). Let me find it differently.
**Reference finding**: the ref does NOT move focus into its dialogs (focus stays on the trigger). Let me check the clone's behavior.
Clone moves focus into the dialog (Radix superset class — documented, no action). Now field-level validation: submit an invalid amount on the reference.
Reference silently rejects negative amounts (no error text). Now the same test on the clone.
Validation parity confirmed (both silently reject). Let me reset the dialogs and probe the donut hover tooltip (never measured).
Both sides clean — no phantom items. Now the donut hover tooltip probe on the reference.
Reference donut tooltip captured ("Need : $6025.00", transparent, 156×54). Now the clone.
**FINDING**: the clone's donut tooltip renders raw "7370" while the reference renders "$6025.00". Let me check the clone's donut tooltip code.
**G1 confirmed (v14)**: the donut tooltip value needs the `$X.XX` formatter. Let me examine the clone's code and check for existing test pins.
No pin exists — G1 is clean. Next: guideline rows hover (never measured).
Guideline hover: identical (both silent). Next fresh angle: the topbar avatar click behavior (never measured).
No avatar in the desktop title row (rail footer avatar already documented). Next: breakdown accordion button hover + user-select sweep.
Identical (accordion buttons, user-select). Let me do a visual screenshot comparison of key pages side-by-side.
Let me do a coarse pixel-block comparison to spot any structural differences beyond the known data deltas.
Diffs are in the text/data band, but a few blocks deserve a look (rail area on dashboard; bottom-right on all). Let me examine those crops with the VLM skill.
All dashboard diffs are expected (superset #3 highlight, data, initials, Base44 editor badge). Let me check expenses + networth.
The VLM flags several net-worth differences — but some contradict my earlier computed measurements (both tabs measured rgb(220,252,231)). Let me verify each claim in the DOM.
Reference facts confirmed: tab icons (16px SVGs) + white divider (1px rgba(255,255,255,0.2)). Now the clone.
**G2 confirmed**: ref tabs have icons; clone is text-only. The divider claim is false (both identical). Let me verify the header-icon claim more thoroughly.
The reference DOES have a 48×48 header icon. Let me measure its chrome and find what it looks like on other pages.
Reference has a 48×48 gradient header icon on networth. Let me check if it exists on the ref's other pages + which icons.
**G3 found**: the reference has a per-page 48×48 gradient header-icon family (income/expenses/savings/networth, none on dashboard). Let me check the clone's pages.
The clone HAS the icons on income/expenses/savings — only **/networth** is missing. Let me capture the ref's networth icon fully.
The ref's networth icon is lucide `trending-up`. Now let me check the clone's code for the header-icon family.
**G3 confirmed in code**: net-worth-view lacks the icon chip that items-view has. Let me examine the exact header structure + verify the ratio-icon claim.
The ratio icon claim is false (identical both sides). Let me pin down the ref's tab icons for the G2 fix.
The icons are already imported. Let me check the existing gradient constants to reuse for the fix.
Let me verify the ref's networth header icon on mobile (ref15m) and the inactive-tab icon color.
The ref has the chip on mobile too. Let me confirm the clone lacks it on mobile.
G3 applies at all viewports. All findings confirmed. Now let me check the existing test specs to plan the TDD additions.
The mobile specs won't conflict. Let me pin the exact ref header-row geometry for the G3 fix.
All fix details pinned. Let me check the clone's TabsTrigger component for the G2 fix.
All details pinned. Now let me write the remediation plan v14.
Plan saved. Now the TDD RED phase — writing the three new specs.
Now the net-worth specs for G2 and G3.
Let me remove the unused locator variable to keep lint clean.
Specs written. Now closing live browser sessions (pre-e2e memory discipline) and running the RED phase.
4 RED failures. Let me verify they fail at the exact unfixed values (not test bugs).
The Playwright hover loops (tooltip follows the mouse). Let me switch to evaluate-based event dispatch, as my live probe did.
**RED confirmed at the exact unfixed value** ("7370"). Let me verify the networth RED failures.
All RED confirmed at exact unfixed values. Now the GREEN phase — implementing the three fixes.
Now the G1 fix — the donut tooltip formatter.
Typecheck errors in the new spec. Let me see them all and fix.
The union return type needs narrowing. Let me fix the G3 test structure.
Now the recharts Formatter type fix (let inference type the param).
The literal type got widened. Let me restructure the evaluate to return null when missing.
Clean. Now rebuild and run the GREEN phase.
G1's value assertion passes — but the tooltip radius differs (0px vs ref's 8px). Let me inspect the clone's tooltip DOM.
Session cookies were wiped by the restart. Let me re-login clone15.
The recharts 3.x default tooltip lacks the ref's radius/shadow/border chrome. Let me check the G2 failure too, then fix both.
The Assets tab is active by default (green icon is CORRECT). My test wrongly asserted all icons gray. Let me fix the test logic.
Now the G1 chrome fix — add the ref's tooltip contentStyle.
Now update the e2e chrome assertions to pin the full ref tooltip chrome.
Chromium appends the spread. Fix the expected string and check G2.
The `transition-all` is mid-flight when I measure. Add a settle wait after the click.
All GREEN. Let me confirm the 5 test names and run the full chain.
4 new specs + setup. Now the full verification chain — unit, full e2e, smoke.
One v13 login test failed — my changes don't touch that surface. Let me check if it's a flake.
Flake confirmed — 15/15 in isolation. Let me re-run the full suite for a clean pass.
**119/119 e2e green.** Now the smoke test to complete the chain.
**Full chain GREEN: lint · typecheck · 96/96 unit · build · 119/119 e2e · 30/30 smoke.** Now live parity re-verification with fresh sessions.
G2+G3 verified byte-identical. Now the G1 donut tooltip live check.
One subtle remainder: the li text color (clone renders the sector color; ref renders black). Let me fix with itemStyle.
Lint clean, typecheck 0 errors (the grep chain broke on zero matches). Continue with build + test.
G1 fully verified. Now the full regression chain again (the itemStyle changed the dashboard).
Full chain green. Now regenerate the screenshot catalog (networth shots will change — chip + tab icons).
Exactly the two networth shots changed (as predicted). Let me verify the new shot with VLM.
Screenshots confirmed. Now docs alignment — first update the plan (G1's scope grew with the chrome pins).
Now README updates — counts + plan-v14 row.
Now AGENTS.md — the v14 pin paragraph.
Now CLAUDE.md — counts + v14 surfaces.
Now the SKILL doc — state, lessons 31-32, Appendix B row.
Now the probe README with the v14 catalog.
Now the formal session log — docs/session_28.md.
Fix a typo artifact in the session log.
Now the repo worklog entry (newest first) and the global workspace worklog.
All docs aligned. Now the final phase — review the change set and commit + push via the SSH wrapper.
Clean change set. Let me fix the stray server log (point it outside the repo like prior sessions).
Final review of the code diffs before committing.
Diffs clean. Committing.
Commit `8fb03dd` created. Now the push — let me follow the SSH wrapper runbook.
Following the runbook: materialize the key (outside the repo), verify the shim, dry-run, then push.
The wrapper defaulted to the wrong remote (the runbook's example repo). Re-run with the correct `--remote`.
Dry-run green (fast-forward 931bfcd..8fb03dd). Executing the real push.
Push verified. Fixing the key shred (wrong file mode).
Key shredded. Final cleanup of browser sessions and wrap-up.
**Session complete — parity iteration v14 shipped to `main` as `8fb03dd` (push verified, key shredded).**

**What I did this session:**
- Pulled the latest (one new doc), re-read the full doc chain, and re-verified the v13 baseline green (96/115/30 + lint/typecheck/build)
- Re-verified mobile navigation end-to-end: all four reference bugs still live, all six clone superset fixes intact
- Ran a fresh two-site audit led by a VLM screenshot sweep with DOM verification of every flag — found and fixed **4 drift groups TDD-first**: the donut hover tooltip (raw number + recharts-3 chrome drift), the net-worth tab icons, and the net-worth header's gradient icon chip
- Full chain now **96 unit · 119 e2e · 30 smoke all green**; docs, worklogs, and screenshots aligned; committed and pushed via the SSH wrapper

**Suggested next steps:** loading/spinner states during data fetches remain the last unmeasured surface class for a future pass; the net-worth tabs' Select popovers and the calculator's frequency listbox keyboard flows are also unmeasured; wiring real OAuth or SMTP would convert the two honest-copy divergences (Google sign-in, forgot-password) into full features.
