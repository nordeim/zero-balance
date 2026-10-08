I'll continue the zero-balance project work. Let me set up my task plan and start with the workspace refresh.
Git pull succeeded — brought in `docs/session_23.md` and an update to `docs/prompt-to-review-3.md`. Let me read the full operating instructions file, then the project docs.
I've internalized the operating instructions. Now let me review the project docs.
Excellent — the project has advanced significantly (v11 iteration complete, 96 unit + 107 e2e tests). Let me continue with the remaining project docs.
Architecture doc reviewed. Now the SKILL.md and session docs.
Now let me read session_23.md (the summary doc), remediation-plan-v11.md, and worklog.md.
Now the worklog and SKILL doc (key sections).
Environment intact: `.env` DATABASE_URL correct, `db/custom.db` at repo root, `.env.example` present, skills catalog present. Now let me check the skills catalog, clone scandihaven (not present), and start the baseline verification chain.
Skills catalog reviewed — I'll use `code-review-and-audit`, `tdd`, `agent-browser`, and `tailwind-patterns` guidance. Now let me validate the baseline: running the verification chain (lint, typecheck, unit tests first).
Lint ✓ · typecheck ✓ · 96/96 unit ✓. Now the production build, then e2e.
107/107 e2e ✓. Completing the baseline chain with the 30-step API smoke test.
**Baseline chain fully green at `740d6e1` (v11)**: lint ✓ · typecheck ✓ · 96/96 unit ✓ · build ✓ · 107/107 e2e ✓ · 30/30 smoke ✓. Now let me spot-check the v11 pins in the code and review the scandihaven pattern repo.
v11 pins confirmed in code. Now let me review the scandihaven pattern repo (tech-stack reference per the brief).
Scandihaven patterns reviewed (Tailwind v4 CSS-first rules, money-as-integer-cents, strict TS, test gates — zero-balance already incorporates the applicable ones via its ADRs). Now the audit phase: reviewing the most recent code changes (v11 commit `00dad5a`).
v11 commit diff reviewed — clean, well-documented changes. Now let me set up the audit infrastructure for the two-site parity verification. First, checking the probe infrastructure and agent-browser state.
Probe infrastructure understood. Now setting up the audit sessions — checking agent-browser state first.
No active sessions. Setting up the four audit sessions — reference desktop first.
Reference logged in. Now the clone desktop session (server booted per command via with-server.sh).
The login POST raced with server restarts (each command boots its own server). Let me redo the whole login flow in one with-server.sh invocation, as previous sessions did.
Clone logged in. Now the mobile sessions (390×844) — reference first with hydration wait.
All four sessions live and logged in. Starting the audit — data drift check first.
Reference data unchanged since session 19 (30.5%, $525); clone seed intact ($5550/$1250/$2235 → +$2065). Now the mobile navigation task-focus re-verification — R1 (toast-blocked burger) + R4 (overflow) on the reference.
R1 + R4 re-confirmed live on the reference (toast container `pe:auto` intercepts the burger hit; scrollWidth 395). Now the clone's side.
Clone fixes intact: DIRECT hit on the burger svg, no blocking container, 390px fit. Now R2 — the sheet-trap test on the reference.
Ref sheet open at 288px with all links inactive on `/` (root-route bug, superset #3). Now tap Income — the R2 trap test.
R2 re-confirmed: reference navigated to `/income` but sheet + overlay still trap, with Income rendering the full active style (v10 pin). Let me close the ref sheet, then run the clone's full mobile flow.
The reference's sheet does close on Escape (unlike its dialogs). Ref is clean. Now the clone's full mobile flow — sheet open, Dashboard highlight, tap Income → close + navigate + fit.
Clone sheet highlights Dashboard on `/` (v10 + superset #3 intact). Now tap Income — the clone must close the sheet.
**R2 clone fix verified**: navigated, sheet closed, 390px fit. Mobile nav task-focus fully re-verified (R1/R2/R4 live on ref; all six clone superset fixes intact).

Now the fresh-angle audit v12. Dimensions never measured at computed-style depth: **login error state** (wrong-password), **forgot-password submit behavior**, **document.title per route**, and **a11y roles/labels**. Let me first check the clone's login-card error handling in code.
Clone's error state: `p[role=alert]` with `text-sm font-medium text-[#dc2626]`. Now let me measure the reference's login error state live (one attempt, within rate-limit budget).
Reference error message: `#b91c1c` (red-700), 14px/400, block. Now the clone's error state.
**FINDING (v12-G1)**: login error drift — clone renders `#dc2626`/fw500; reference renders `#b91c1c`/fw400. Let me measure the exact geometry + spacing on both sides.
The reference's error is a **tinted banner** (bg `rgba(254,242,242,0.7)`, 16px padding) — the clone renders a bare `p`. Let me capture the full banner chrome.
Reference banner fully measured: `rgba(254,242,242,0.7)` bg + `1px solid rgb(254,202,202)` border + 12px radius + 16px padding, inner text `#b91c1c` 14px/400. Now let me check the reference's signup-mode validation error (mismatched passwords) — the same slot on a different flow.
Same banner on the signup flow ("Passwords do not match"). Now the reference's forgot-password submit behavior.
The reference's forgot flow transitions to a "Check your email" confirmation state. Let me check what the clone does.
The clone's forgot flow shows an honest "reset unavailable" toast (documented self-hosted decision — no mail transport), while the reference renders a "Check your email" confirmation state. Noting this as a parity/honesty tradeoff to address. Now the remaining fresh angles: document.title per route + a11y roles.
**FINDING (v12-G2)**: per-route titles — reference sets "Income | ZeroBudget" etc. (note "Networth" one-word); clone renders "ZeroBudget" everywhere. Let me check the login title too, then the a11y angle.
Clone login matches on title/h1/lang, but the reference's login card sits inside a `main` landmark while the clone's doesn't. Let me check the clone's login page structure and the dashboard a11y on both sides.
**FINDING (v12-G3)**: reference login root is a `<main>` landmark; clone's is a bare div (visually identical). Now the dashboard a11y structure on both sides.
Dashboard a11y matches (h1s identical; clone's `aside` landmark is a superset — ref's rail is a div). Now the last fresh angle: the expenses view's payment-method filter (never measured live).
Filter card identical. Let me check the payment-method dropdown OPEN state (listbox options) on both sides.
Option geometry identical (data-driven count difference only). Let me finalize the G1 evidence — banner's DOM position and the form height delta on the reference.
G1 fully mapped: banner is a direct form child in the `space-y-4 sm:space-y-5` flow. One more precision pass — horizontal padding and inner layout.
Full banner spec captured (bg red-50/70%, border #fecaca, radius 12, pad 16, centered #b91c1c 14px/400 text — shadcn FormMessage pattern). Let me check the clone's form spacing to confirm the fix integrates cleanly.
The clone's form already has the parity `space-y` classes — the banner fix is a drop-in at the same slot. Now let me measure the reference's forgot-confirmation state layout (for the honest-copy variant decision).
The audit found 4 finding groups. Let me complete the final evidence — the reference login `main` padding (G3 precision).
`main` has `p-4` — same as the clone's root div, so G3 is a pure tag swap. The audit is complete with 4 finding groups. Let me close the browser sessions (pre-e2e discipline) and review the login e2e spec for TDD placement.
Now let me check the auth spec's rate-limit usage before writing the plan (e2e login-attempt budget discipline).
The existing wrong-password test can be extended for the banner (zero extra login attempts). Now let me check the app-shell structure for the per-route title fix.
AppShell is the single place for the title effect. Let me verify the layout metadata + login-card's exact fix sites, then write the remediation plan.
I have all the evidence. Writing remediation plan v12.
Plan saved. Now validating the fix sites and writing the RED-phase specs. Let me read the exact spec sections to extend.
Now let me check nav-geometry.spec.ts (candidate home for the route-title tests — needs shared storageState).
Spec conventions clear. Writing the RED-phase specs — first the login-parity additions.
Now the per-route title tests in nav-geometry.spec.ts.
Now extending the auth.spec wrong-password test with the banner assertion.
All specs written. Now the RED phase — running the new tests against the current build (expect failures at the exact unfixed values).
5 failures as expected. Let me verify each fails at the exact unfixed value (not setup errors).
G3/G4 fail for the right reasons. G1 has a test bug — `getByLabel("Password")` matches both Password and Confirm Password fields. Fixing the locator.
**RED fully confirmed** — all 5 failures at the exact unfixed values. Now the GREEN phase. Let me read the login-card's state rendering to implement the fixes.
Now implementing all fixes. First let me find `backToSignin`:
Now implementing all login-card fixes (G1 banner, G3 main landmark, G4 confirmation state) with MultiEdit.
One cleanup — the duplicate `setError(null)` in the forgot branch:
Now the G2 fix — the per-route title effect in AppShell.
All fixes applied. Lint + typecheck, then rebuild for the GREEN run.
G1/G4 pass. Let me inspect the G3/G2 failures.
G3 failure is a viewport artifact (720px Playwright default vs 800px agent-browser measurement — my test hardcoded a viewport-dependent value). G2 needs proper debugging. Let me isolate.
The effect isn't landing at all in the e2e build. Let me check whether the string is even in the built bundle.
The code is in the bundle. Let me poll the title over time to see if the effect fires and gets reset, or never fires.
The effect never fires — but I need to know if the page even hydrates. Let me capture page errors and hydration evidence.
Page IS hydrated (Salary content present), no errors — but the effect never lands. Let me inspect the built client chunk around my code.
The effect IS in the bundle. Let me see what feeds `n` (the pathname variable) — wider context.
The build is correct. Let me probe the live behavior directly with agent-browser against the parity server.
The agent-browser session wasn't logged in (redirected). Let me replicate the e2e conditions — logged in.
Title stays "ZeroBudget" even logged in — likely React Float re-emitting the static `<title>` after my effect. Let me get definitive evidence with a MutationObserver installed before page load.
The observer approach failed (init-script timing). Let me use a high-frequency in-page poller instead.
**ROOT CAUSE FOUND**: my effect runs at 260ms and sets the title — then React Float re-emits the layout's static `<title>` at 284ms, resetting it. The framework-native fix is per-route static metadata (the reference's pipe format). Let me check the page structure.
The pages are thin client wrappers — a per-route server `layout.tsx` exporting segment metadata is the clean fix (no client race; matches the reference's observable outcome). Implementing.
Now update the root layout template and revert the AppShell client effect (the losing race).
Now fixing the G3 test's viewport-dependent assertion, and updating the G2 test comment to match the final implementation.
**GREEN — 29/29** in the affected files. Now the full verification chain.
**Full chain GREEN: 96 unit · 112 e2e · 30 smoke** (5 new tests). Now the live side-by-side parity re-verification with fresh sessions.
**G1 verified live — byte-identical banner.** Now G2 titles, G3 main landmark, G4 forgot state.
The clone13 session isn't logged in — every workspace route redirected to /login. Let me log in first and re-verify.
**G2 verified — all titles match the reference.** Now G4 — the forgot confirmation state.
**G4 verified — state typography identical to the reference.** Final live check: the banner on mobile (390px).
Clone mobile banner verified (294×54, 16px gaps, no overflow). The ref13m session wasn't created — let me set it up and measure the reference's mobile banner.
CDP connection refused — the daemon is under resource pressure (known session-19 issue). Let me close stale sessions and retry.
The daemon appears hung. Let me check its state with a lightweight command.
Daemon alive but sessions linger. Closing them individually with timeouts.
Daemon recovered — ref13m is live. Now the reference mobile banner measurement.
**Mobile banner parity confirmed** (294×54, 16px gaps both sides). All four fixes verified live. Now regenerating the screenshot catalog.
The 13-shot set needs regeneration plus two new shots documenting the new parity surfaces (error banner + forgot state). Let me read the script.
Extending the screenshot script with the two new parity surfaces (error banner + forgot state).
All 15 screenshots captured. Now the documentation alignment — README first.
Now CLAUDE.md updates.
Now AGENTS.md — adding the v12 pin paragraph.
Now the SKILL doc — state, new lesson, Appendix B row.
Now the Appendix B row in the SKILL doc:
Now the probe README v12 rows.
Now the formal session log — `docs/session_24.md`.
Now the repo worklog entry (newest first).
Now the shared workspace worklog.
All docs aligned. Now the final phase — commit and push. First, the change-set review and secret scan.
The flagged files are pre-existing tracked docs (task briefs containing the reference credentials — already in the repo from prior sessions). Let me verify my change set introduces no secrets and review the wrapper.
Change set clean. Let me check the SSH shim and the runbook.
Runbook understood — the wrapper needs `--remote` explicitly (defaults to the old repo). Now committing.
Commit `4ba60f5` created; key parses (ed25519). Now the push — dry-run first with the shim on PATH.
Dry-run green — clean fast-forward. Executing the real push.
**Session complete — parity iteration v12 shipped to main as `4ba60f5`, push verified, key shredded.**

**What I did this session:**
- Pulled to the latest HEAD, re-read the full doc chain + your uploaded operating instructions, and confirmed the v11 baseline green (96 unit / 107 e2e / 30 smoke)
- Re-verified mobile navigation end-to-end: all reference bugs still live (toast-blocked burger, sheet-trap, 395px overflow), all six clone superset fixes intact
- Ran a fresh two-site audit with first-ever angles — **error states, route titles, landmarks, and the forgot flow** — and fixed 4 drift groups TDD-first: the login error banner (red-tinted bordered box, byte-identical to the reference), per-route tab titles ("Income | ZeroBudget"…), the `<main>` login landmark, and the forgot-password confirmation state with honest copy
- Along the way I diagnosed a subtle React Float race that silently resets client-side titles after hydration — solved with route-segment metadata and recorded as lesson 27
- Final chain **96 / 112 / 30 all green**, live parity re-verified side by side, 15 screenshots, docs aligned, committed and pushed via the SSH wrapper

**Suggested next steps:** run another verification pass anytime (error/post-submit states were this pass's goldmine — loading states and the register flow's API errors are still unmeasured), wire real OAuth for "Continue with Google", or configure an SMTP transport to make the forgot-password flow fully functional.
