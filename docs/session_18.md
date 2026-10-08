I'll continue the comprehensive zero-balance remediation task. Since this is a continuation with full autonomy granted ("Proceed with your best recommendations"), I'll start immediately.
工作区已存在于上一个会话中。让我刷新它并检查进度状态。
Session 15 已完成并推送。新的拉取仅添加了 `docs/session_16.md` ——这是当前会话的任务。让我彻底查阅所有必需的文档。
`session_16.md` 记录了第 15 次会话已完成的 v8 工作。现在让我按照要求，查看剩余的文档链：`session_15.md`、`remediation-plan-v8.md` 以及仓库的 `worklog.md`。
The doc-numbering convention is now clear: formal session logs use the next unused number (I'll write `session_17.md`, plan v9). Now reading the remaining required docs.
Now let me check the SKILL doc's state section and validate the codebase structure against the docs.
Environment is intact. Now let me validate the baseline verification chain and confirm the scandihaven reference repo state.
92/92 e2e green. Now the smoke test to complete the baseline chain.
**Baseline fully green**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ · 92/92 e2e ✓ · 30/30 smoke ✓ — v8 baseline at `92e837e` confirmed intact.
Skills catalogs verified. Let me refresh on the key skills (agent-browser, clone-app-pat-pro) and Tailwind v4 patterns before the audit.
Skills refreshed. Now let me set up the two-site parity audit infrastructure. First, check the established probe pattern from previous sessions.
Probe infrastructure intact. Now boot the detached parity server on :3200 and set up both browser sessions.
The server booted on :3000. Let me move it to the conventional :3200 parity port.
Reference logged in. Now the clone session.
Both sessions live. Let me review the v8 probe style, then write the v9 audit probes with fresh angles.
Now writing the v9 audit probes. The fresh angles this session: dialog **form internals** (labels/inputs/radios/switch at computed depth), dashboard hero/stat/guideline internals, login card's sign-up/forgot states, plus the standard mobile-nav and data-state re-verification.
Now let me run the audits. First: reference data-state drift check + mobile nav re-verification (the task focus).
Reference data unchanged (no drift): +$3475.00, 30.5%. Let me check the correct viewport command syntax.
Now fix the dash probe's selector syntax error and run it on both sites.
Key differences spotted: (1) the reference's donut percentage labels are **near-black** while the clone's are **sector-colored**; (2) hero-bar radius `9999px` vs v4's `33554432px` (calc(infinity)). Let me dig deeper on both.
Two candidate findings: (1) the clone renders donut **label connector lines** the reference doesn't have; (2) possible sector angular-order difference. Let me measure precisely.
The sector-path math suggests the pies may be laid out differently (ref: orange-first counterclockwise from 3 o'clock; clone: lime-first). Let me verify empirically with hit-testing at clock positions around both donuts.
Hit-test failed — likely scaling mismatch. Let me debug via path bounding boxes instead.
The donut sector layouts may genuinely differ. Before concluding, let me check what previous audits pinned and what the clone's donut code actually does.
The v2 audit measured the ref's DOM path order as `[Savings, Want, Need]`, but today it's `[Need, Savings, Want]` — matching a **sort-descending-by-value** layout (N=92.3 > S=4.6 > W=3.1 today; S was biggest at v2 time). Plus the clone renders label connector lines the ref doesn't have. Let me inspect the clone's donut code.
Let me check recharts' actual default angles from the installed source — this settles the sweep convention question.
recharts defaults confirmed: startAngle=0 (3 o'clock), positive sweep = counterclockwise — so both apps share the sweep convention and the difference is the **data order**. Let me read the ref's donut legend amounts to understand its actual slice data.
**Breakthrough findings:**
1. **Donut data order**: the ref sorts slices by value DESC — legend `[Need $6025, Savings $300, Want $200]`, pie anchors the biggest at 3 o'clock. The clone uses fixed `[Savings, Want, Need]`. (Also explains the v2-era order — this is data-driven, not a code change.)
2. **Label connector lines**: ref renders none; clone renders 3 recharts label lines.
3. **Hero bar radius**: ref `9999px` vs clone v4 `33554432px` (calc(infinity)).

Let me continue the audit — now the dialog form internals on both sites.
The dialog is open ("Add Budget Item") but my probe's panel-climb failed. Let me fix the probe to find the panel via the overlay.
Rich reference data. Now the clone's same dialog for comparison.
Mostly identical, but several candidate drifts: header 69 vs 61px, label `mb:0 inline` vs `mb:8px flex`, radio tile height 52 vs 56 + text weight 400 vs 500, switch thumb `#fafaf8` vs `#fff`. Let me verify these precisely.
Real drifts confirmed: header 69 vs 61, label→input gap 12 vs 8, tile height 52 vs 56, tile text 400 vs 500. Let me find the header-height cause and get the ref's tile internals.
The ref's header = 28px H2 + **36×36 X button** → 69px. Let me check the clone's X button.
The clone's header lacks the X button (it lives elsewhere). Let me compare X-button geometry and header layout on both.
**Confirmed X-button drift**: ref = 36×36 (svg 16, radius 6) inside the sticky flex header → 69px header; clone = 20×20 (svg 20, radius 4) absolute on the panel → 61px header. Let me examine the clone's dialog shell code.
The calculator dialog already uses a 36×36 in-header X (v6 pin). The form dialogs use the default absolute 20×20. Let me check the v6 pin and the ref's calculator X for the icon size convention.
Let me measure the reference calculator dialog's X button for comparison.
Ref X convention is uniform: **36×36, radius 6, 16px icon, in-header flex child**. The clone's calculator has 36×36 but a 20px icon; the form dialogs use the 20×20 absolute default. Let me enumerate all DialogContent users before designing the fix.
Ref tiles: h52, **2px borders**, text lh 14px, radio 16px/#171717. Let me run the identical tile probe on the clone.
Tile text lh 20 vs 14 explains most of the 4px height gap, but the ref's content-box is 20px. Let me decompose the ref's tile children exactly.
Tile root cause found: ref label `lh 14` vs clone `lh 20`. Also **radio border color drift**: ref `#171717` (rgb(23,23,23)) vs clone `#1a3a2e` (forest). Let me check the clone's primary token.
Ref switch: thumb `bg-background`→**white** (ref's --background=#fff vs clone's #fafaf8), `ring-0` (clone has ring-1). Track checked-state: let me flip the ref's switch to measure its checked color, then restore.
Ref switch checked = **#171717** (near-black) vs clone forest. Dialog audit complete. Now the task-focus mobile navigation re-verification at 390×844 on both sites.
Pages are scrolled from the audit. Let me scroll to top and re-verify the hamburger hit-test (R1) properly.
The ref's R1 (toast-block) is confirmed live. The clone's blocked hit is just my leftover dialog — let me close it and re-verify.
R1 re-confirmed live on ref (pe:auto container blocks hamburger); clone's hit is DIRECT. Now test the sheet open + nav-link behavior (R2) on both.
R2 re-confirmed live on ref (sheet traps after nav). Now the clone's flow.
Mobile nav stack fully verified (R1/R2/R4 live on ref; all clone superset fixes intact). Now the login card states — using fresh unauthenticated sessions for both sites.
Signup-state drifts found: card border #e5e7eb vs warm #e5e7e3, button h44/fs14 vs h48/fs16, inputs h44 vs h48. Let me check the sign-in state and the existing spec pins.
Sign-in state: heading/inputs/heights match, but **button fs 14 vs 16** and **card border #e5e7eb vs #e5e7e3**. The ref's *signup* state uses h44 controls (clone: 48). Let me check the forgot state too.
Forgot state confirms the pattern: ref h44 controls vs clone h48. Now let me finish the dashboard stat cards + guidelines + breakdown rows with corrected selectors.
Sessions are on /income from the mobile test. Navigate both to the dashboard and re-run.
Stat cards IDENTICAL ✓. Let me do a quick text-level check of the guidelines card, then the breakdown rows.
Guidelines identical ✓. Now a net-worth spot check on both sites.
Net-worth structure identical ✓. Now the rounded-full census to scope the infinity-radius drift.
Perfectly symmetric census: same surfaces, ref=9999px, clone=v4 infinity. Let me count source usages of `rounded-full` in the clone.
24 usages across 10 files — a clean mechanical fix. Now let me scope the label-gap fix by examining the clone's Label component and field structure.
The clone uses `space-y-2` wrappers. Let me verify how the ref produces its 12px gap and check the description offset.
The ref ALSO uses `space-y-2` but measures 12px — its inline label has a taller line box. Let me compare label rects on both sides.
The ref's Label is plain inline (`text-sm font-medium leading-none` — no flex/gap-2) — that's the mechanism behind its 12px gap. Let me verify the clone's Label usages are all plain-text before scoping the fix.
Audit complete — 9 finding groups. Now let me check the existing spec pins that my fixes will affect (TDD planning).
Both login cards are border-0 — the border-color difference is invisible (withdrawn). The audit is complete with 7 real finding groups. Now let me check `spendingBreakdown` before writing the plan.
Now I'll write the remediation plan v9 with the complete findings ledger.
Plan saved. Let me validate the file/line references against the codebase before executing.
All references validated. Now TDD — writing the RED specs first. Let me study the existing spec patterns.
Now writing the RED specs. First, the dashboard donut spec updates:
Now add the v9 dialog-chrome test to dialog-buttons.spec.ts:
Now the tokens.spec.ts additions for radio/switch/radius pins:
Now the login-parity spec additions:
Now confirm RED (TDD step 2) — run the updated specs against the current build:
**RED confirmed — 11 new tests failing for the right reasons**, 23 pre-existing pass. Now implementing. G1 first — the donut sort + label lines:
G1 done. Now G2 — the `DialogCloseButton` primitive and removing the default absolute X:
Now wire `DialogCloseButton` into the 4 form dialogs' headers and fix the calculator's icon:
Typecheck clean. Now G3 (Label) + G4 (tile line-height):
Now G5 — the radio-group and switch token pins:
The radio's checked dot also uses `fill-primary` — let me verify the ref's dot color before pinning it.
Ref dot = `rgb(23,23,23)` (#171717). Pinning the indicator dot too:
Now the switch — checked track #171717, thumb white + ring-0 + 9999px radius:
Now G6 — the systematic `rounded-full` → `rounded-[9999px]` replacement across all remaining files:
All 24 replaced. Now G7 — the login card mode-dependent geometry:
All implemented. Lint + unit + rebuild, then the RED specs for GREEN:
Three issues to debug. Let me check the clone's live label/switch state on the parity server (needs rebuild first — the server runs the old build):
The clone's input is nested in a `div.relative` (icon wrapper) — different sibling structure. Let me measure the actual sibling geometry:
The ref's input gets `mt: 8px` from space-y-2; the clone's gets **0** — v4's space-y isn't applying! Let me inspect the generated CSS:
**Root cause found**: v4's `space-y-2` puts `margin-block-end` on the first child — and vertical margins on **inline** labels are ignored by layout, so the gap collapsed to 4px. The ref's v3 build applies `margin-top` to the *following* sibling. I'll restore v3 semantics for `space-y-2` in globals.css. First, verify all its usages are safe:
All 43 usages are safe (block children everywhere else — v3/v4 are layout-equivalent there). Adding the v3-semantics restoration to globals.css:
Trap 4 is already documented — my finding is its deeper manifestation. Adding the v3-semantics pin:
Now fix the two spec issues — the switch race and the radius finders:
Rebuild with the CSS fix and re-run the failing specs:
"Target crashed" — resource pressure from my 4 live browser sessions. Let me close the login sessions and retry:
`aria-checked` flips but the bg doesn't — the `data-[state=checked]:bg-[#171717]` class may not have generated. Let me check the built CSS:
The rule exists — let me see its full selector and test live:
Live works perfectly — the spec must be hitting a stale :3100 server from the crashed run. Let me check:
No stale server — build #2 was live and works manually. Let me re-run the single switch test to check for flakiness:
The switch IS checked but bg stays unchecked-colored. Let me inspect the exact generated rules for both state variants:
**Found it**: the switch has `transition-colors` — the bg animates over 150ms, and my evaluate ran at the transition's start. Fix: poll the computed value instead of racing it:
All green. Now the full e2e suite for regressions:
The old auth spec pins `span.rounded-full` — my class rename needs the spec updated:
**102/102 e2e green** (92 + 10 net-new). Smoke test to complete the chain:
**Full chain green**: lint ✓ · typecheck ✓ · 96/96 unit · build ✓ · 102/102 e2e · 30/30 smoke. Now the live parity re-verification on the fixed build:
Donut fixed ✓. Now the dialog chrome re-verification:
Dialog chrome matches exactly. Now switch/radio/radii + legend order:
All fixed. Now the login states on the fresh build:
All login states match. Final mobile-nav re-verification on the fixed build:
All live parity verifications pass. Now updating the plan status and regenerating the screenshot catalog:
Now regenerate the 13-shot screenshot catalog:
All 13 screenshots regenerated. Now the documentation alignment — README first:
Now the AGENTS.md v9 pin paragraph:
Now the SKILL doc — project state, lessons, and Appendix B:
Now the probe README v9 row and the session_17.md formal log:
Now update the repo worklog.md with the session 17 entry:
Now update the shared workspace worklog and run the final gate:
Change set is correct (45 files; only the 4 screenshots with visual deltas changed). The full 102-pass e2e run came after all changes. Now commit:
Committed as `9c23518`. Now the SSH push via the wrapper — following the runbook:
Runbook understood. Writing the operator key to a 0600 file outside the repo:
Dry-run green — clean fast-forward. Executing the real push:
Push verified — remote main @ `9c23518`, key shredded. Final housekeeping — verify no secrets in the tree, close browser sessions, stop the parity server:
**Session complete — parity iteration v9 shipped as `9c23518` on main, push verified via the SSH wrapper.**

The v8 baseline re-verified green, then a fresh two-site agent-browser audit (mobile nav re-verified end-to-end — all three reference bugs still live, all six superset fixes intact) surfaced **7 new finding groups**, all fixed TDD-first: the donut's value-DESC sort convention + no label lines, the 36×36 in-header dialog X (69px headers), the inline label line box (which exposed a genuine Tailwind v4 `space-y` bug — vertical margins on inline first children are layout-ignored, now pinned in globals.css), 52px tiles, the `#171717` radio/switch primitive family, `9999px` radius pins across 24 sites, and the login card's per-state geometry. Final chain: **96 unit · 102 e2e · 30 smoke — all green**, live parity re-verified surface-by-surface, screenshots regenerated, full doc chain aligned.

**Suggested next steps:** another verification pass anytime (the reference's data keeps drifting — lesson 12.19), or I can wire real OAuth for "Continue with Google", add multi-currency support, or set up a hosted CI to run the gate on every push.
