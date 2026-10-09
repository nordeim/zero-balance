I'll continue the recurring zero-balance task, now referencing session_49 / remediation-plan-v24 / session_50. Let me set up the task plan and start.
Workspace exists. Let me pull the latest changes (session_49/v24/session_50 docs).
Pull brought in session_50.md. Now let me review the project docs and the latest session docs.
Docs are large; key facts captured. Now the session docs — session_49, remediation-plan-v24, worklog, session_50.
Session docs reviewed — prior session shipped v24 (auth responsive families + space-y-1.5 pin). Now reading the v24 remediation plan and worklog.
Now reviewing the remaining project docs (CLAUDE.md, architecture doc, SKILL) and validating codebase state.
All standing requirements verified in place (env, db, .env.example, scandihaven at `d4789c3`). Let me check the scripts infrastructure and skills catalog, then start the baseline chain.
Now running the baseline verification chain (audit Phase 1).
Lint ✓, typecheck ✓, 108/108 unit ✓. Now the build.
Build ✓ with robots.txt + sitemap.xml prerendered (SEO requirement holds). Now the e2e suite.
150/150 e2e ✓. Now the smoke test.
**Full baseline chain green: 108 unit · 150 e2e · 35 smoke.** Now audit Phase 2 — npm audit, secret scan, and reviewing the v24 changeset.
Same 5 dev-only `braces` advisories (accepted, documented). Now reviewing the v24 changeset diff as the recent-changes code review.
v24 changeset reviewed — clean, well-commented, test-pinned. Now setting up the two-site parity audit infrastructure.
Infrastructure in place. Let me check the agent-browser daemon and the probe README for current discipline.
Reference site is open. Now logging in with the brief's credentials.
Reference logged in — dashboard data matches the standing census (30.5%, $3475.00). Now the standing mobile-nav R1–R4 re-verification (19th check). Checking the probe patterns first.
Need the correct viewport command and session handling. Checking the core skill guide.
Two sessions exist — my login is in `default`. The "parity" session launched a second blank browser (the documented false-read trap). I'll work in ONE session (`default`) throughout.
R1 reference ✓ (toast containers intercept burger at (38,30), scrollWidth 395). Now R2 — the sheet trap test.
R2 reference ✓ (sheet traps — `sheetStillOpen: true`). Now R4 per-route overflow at mobile on the reference.
R4 reads one route at a time — let me sweep all six routes on the reference.
R4 reference ✓ (395 overflow on /+/dashboard, 464 on /networth). Now R3 — desktop rail link comparison.
Reference-side R1–R4 all verified (19th consecutive). Now the clone side — booting the parity server and logging in inside one invocation.
Clone session cookie survived — dashboard loaded. Now running the clone's R1–R2 at mobile inside one server invocation.
Clone R1 ✓ (direct hit, `pe:none` viewport) + R2 ✓ (sheet closes on nav). Now R4 route sweep + R3 desktop on the clone.
**Mobile-nav R1–R4 all verified (19th) — Tailwind v4 pins hold.** Now the data drift check (19th) and SEO pair.
The clone shows its demo-seed data (expected). The drift check targets the reference account — let me run the full census there.
Key drift values all match. Let me verify the guideline percentages quickly, then the SEO pair.
**SEO pair ✓** — both sites serve robots + 5-URL sitemaps. Standing checks complete. Now the v25 sweep — first, fresh-verification of the v24 G1/G2 fixes live on both sites (the standing discipline).
Reference census confirms the three-family table. Now the clone census at mobile (v24 fix re-verification).
**v24 G1+G2 re-verified live — clone census matches the reference exactly.** Now the v25 sweep surface 1: the sm-band (640–768) pair on the auth forms — the sign-up font's 16px middle step.
Reference sm-band census captured (sign-up 44px/16px in the band). Now the clone at 672.
**sm-band census: exact match on both sites** (sign-up 44/16 — the 16px middle step renders correctly). Session-48 suggestion 1 verified clean. Now sweep surface 2: the focus-visible ring of the auth submit buttons (real Tab presses). Checking the keyboard-sweep pattern first.
The pattern is clear (CDP Tab presses move focus natively). Writing the v25 focus-ring sweep probe for the auth submit buttons.
**First-time finding surfacing** — the reference's submit ring is `#09090b` (shadcn `--ring`), not slate-400. Measuring the clone's submit ring now.
**REAL FINDING (v25 G1)**: the submit's focus ring — reference `#09090b` (shadcn `--ring`), clone `#94a3b8`. Let me scope the fix — checking where this ring class appears and what other button families pin.
The `ring-[#94a3b8]` family appears in 3 places. Let me check what `--ring` resolves to in the clone and sweep the reference's other auth-surface buttons (verify state + swap link).
The clone's `--color-ring: #0a0a0a` vs the reference's measured `rgb(9,9,11)`. Let me check existing spec pins and sweep the reference's remaining auth focusables (swap links).
Conflicting pin data — let me read the tokens.spec pin and re-measure the reference's rings carefully (settle discipline).
The tokens spec pins the search ring at `rgb(10,10,10)` but today's submit read `rgb(9,9,11)`. Let me measure both on the reference in one careful session.
Two distinct ring colors confirmed on the reference (search input `currentColor` #0a0a0a; submit `ring-ring` #09090b). Now measuring the reference's 404-page button ring, and checking how the v21 verify probe measured the reference.
The reference's 404 button renders a slate-500 ring and says "Go Home". Let me get its full class and compare against the clone's 404.
The reference's 404 button uses `focus:ring-slate-500` (#64748b). Let me check the clone's 404 live + the reference's icon, and what not-found.spec pins.
Reference 404 icon matches the clone. Now a fuller keyboard walk of the login page focusables on both sites (captures swap-button rings too).
Reference walk complete — swap buttons show browser-default outlines; submit shows the #09090b ring. Now the clone's walk.
Stop #4 confirms the submit-ring G1 finding. There's also an outline-serialization difference on the browser-default outlines — let me check `color-scheme` on both pages.
The auto-outline colors differ — Chromium's `outline: auto` adapts to the underlying background. Let me check the login pages' outer backgrounds on both sites.
**Another real finding (G3)**: the login body bg — reference pure white, clone `rgb(250,250,248)` (stone-50). Let me find the source.
The clone's `--color-background: #fafaf8` was presumably measured on app surfaces. Let me check the reference's body bg on the dashboard vs login.
Both sites differ on the body bg everywhere. Let me check the reference's actual `--background` token and body class to understand the intent.
The reference styles NO body background (browser-default white canvas); the clone paints `#fafaf8`. Let me scope where the body is actually visible (login, 404, app pages).
Odd — line 389 shows `const ode, setMode]`. Since typecheck passes, it's likely a display artifact, but let me verify the actual file content.
Line 379 genuinely looks broken, yet build/typecheck passed. Let me check git state and re-run typecheck on this file.
The minimal test fails but the project compiles — line 379 must be inside a comment. Checking the raw context.
The line is live code yet everything compiles. Let me check when this corruption entered git history.
The corruption exists in git since v23 yet compiles. Let me run tsc on this exact file directly.
False alarm on line 379 — charCodeAt reveals `[m` (i.e. `const [mode,`) that the output pipeline strips as an ANSI sequence. The file is fine; tsc was right. Now let me scope G3 (body bg) — checking the reference's 404 outer bg, app surfaces, and the tokens.spec background pins.
Reference 404 paints its own `#f8fafc` root (clone matches — v21 pin holds). The body-bg drift manifests where body shows through. Let me check the app pages' visible background on both sites.
On the clone, card gaps show the `#fafaf8` body; the reference shows white. Let me check the tokens.spec header for the original background-token measurement.
Mystery solved — `#fafaf8` is the manifest's PWA `background_color` that the early session also applied as the CSS body bg; the reference's rendered body is white. Let me scope token usage before fixing.
The switch thumb already uses `bg-white` (v9 pin). Checking the v15 loading-overlay comment that referenced the body color.
The reference paints `#fafaf8` on the app-shell layer (not the body) — body stays white for the login page. Now the clone's shell chain.
**G3 scoped precisely**: both app pages render #fafaf8 (painted at different layers), but the login page drifts — reference white, clone warm. The fix: move the warm bg from body to the shell wrapper. Let me examine the app-shell structure.
The loading overlay already paints white explicitly — consistent after the fix. Let me identify the reference's mystery focusable (stop #7, y=756) to rule out an app surface.
Mystery solved — stop #7 is Base44's platform edit badge (not app UI; correctly absent). Now a VLM pair on the login pages to close the sweep.
VLM returns IDENTICAL (7th blind spot — DOM found the real bg drift). One more surface to check: the reference's dialog-button ring (the clone's `--color-ring: #0a0a0a` drives ui/button). Let me check the v19 pin and measure the reference's dialog Save button.
v19 pin shows the reference's dialog buttons use a 1px `#0a0a0a` ring (clone matches) — so the reference deliberately runs distinct ring families per component. Let me check the v21 reference read of the verify-email submit's class.
Sweep complete — three real findings. Let me check the existing not-found spec pins before writing the plan.
Now writing the remediation plan v25, validated against the codebase.
All evidence gathered. Writing the v25 remediation plan.
Plan v25 saved. Now TDD — writing the RED tests first. Checking the spec tail.
Now appending the v25 describe to login-parity.spec.ts (RED first).
Now adding the G2 pin to not-found.spec.ts and the G3-shell pin to tokens.spec.ts.
Now the tokens.spec shell-paper pin (G3):
All four RED tests written, typecheck clean. Running them to confirm RED.
**Perfect RED — all 4 fail as expected.** Now the G1 fix (both submit buttons).
Now the G2 fix (not-found.tsx) and G3 fix (globals.css + app-shell.tsx):
Now the app-shell wrapper gains the warm paper:
All three fixes applied. Rebuilding and running the v25 tests → expect GREEN.
**GREEN — 4/4.** Now pin-sanity mutations to prove the assertions are load-bearing.
All mutations RED — assertions are load-bearing. Restoring and re-verifying GREEN.
Pin-sanity complete. Now live re-verification on the parity server — the focus walk, body bg, and 404 ring.
The e2e tests pass but the live probe reads differ — let me diagnose the focus state directly.
Bizarre — activeElement is set but `:focus` doesn't match. Let me run the same diagnostic on the reference (where earlier reads worked).
The eval-context programmatic focus doesn't engage `:focus` on either site (an agent-browser world quirk) — the original measurements used REAL Tab presses. Re-verifying the clone with the Tab-walk method:
**G1 verified live — the clone's submit ring matches the reference exactly.** Now the 404 ring via real Tab.
**G2 verified live** — clone's 404 ring matches the reference. All three fixes live-verified. Now the full clean-check chain.
One e2e failure in the 404 navigation test — investigating.
Passes in isolation (7/7) — the full-run failure was a flake. Checking the saved error context to be sure.
All affected specs green. Re-running the FULL e2e suite to confirm a clean pass.
**154/154 e2e.** Completing the chain with the smoke test.
**FULL CHAIN GREEN: 108 unit · 154 e2e (4 new) · 35 smoke.** Now regenerating the screenshots.
Screenshots regenerated. Checking which actually changed:
Screenshots regenerated but git sees no content change — suspicious. Let me verify the login screenshot pixels directly.
My naive PNG decode ignores filters — let me use Pillow properly.
Both old and new login screenshots are identical — the visible bg is `#f8fafc` (a gradient layer), suggesting the body was never visible there. Let me examine the login page's actual layer stack.
The login main carries a full-viewport gradient — the body was never visible there. G3 is a computed-style drift on an invisible surface (which is why the screenshots are byte-identical). Let me verify the reference's gradient matches and re-test the outline serialization after the fix.
The gradient is identical on both sites — the body was never visible anywhere. Amending the plan's G3 narrative for accuracy (computed-style fix, zero visual change, byte-identical screenshots).
One more accuracy fix — the VLM bullet (the VLM was actually right; the bg is invisible):
Fixing the spec comments for the same accuracy (login-parity + tokens):
Final full-chain run against the finalized code (comment changes included):
**FINAL CHAIN GREEN: 108 unit · 154 e2e · 35 smoke.** Now docs alignment — checking current counts in README/CLAUDE/AGENTS/SKILL.
Updating README (counts + v25 row):
Now CLAUDE.md updates (counts + v25 surfaces + the ring-family lesson):
Now AGENTS.md — appending the v25 paragraph after the v24 one:
Lesson 44 just demonstrated itself — the `[m` in my own text may have been stripped. Checking the file bytes:
The `[m` was stripped from the actual file — lesson 44 is real. Fixing with a byte-safe construction:
The read-back display also strips it — verifying the actual file bytes via hash comparison instead:
File bytes are correct (count=2) — only the display pipeline strips the sequence. Lesson 44 fully confirmed. Now updating the SKILL doc:
Now the probe README (v25 catalog):
Now the formal session log (docs/session_51.md):
Now updating the repo worklog.md (newest-first + the plan list in the header):
Docs aligned. Final changeset review before commit:
One comment in app-shell.tsx needs the corrected narrative:
Comment-only change after the chain — quick re-gate (lint/typecheck/build + spot e2e) before commit:
All gates pass. Committing the v25 changeset:
Committed as `c60cb9e`. Now the SSH push — reading the wrapper runbook first.
Runbook reviewed. Checking the shim and materializing the key:
Key parses. Dry-run with the explicit zero-balance remote (the wrapper's default is task-management):
Dry-run clean (`e7109fd..c60cb9e`). Real push:
**v25 pushed to main as `c60cb9e`** — remote verified, key shredded, tree clean. Final step: the parent workspace worklog.
**Parity iteration v25 is shipped to `main`** (commit `c60cb9e`, push verified via the SSH wrapper, key shredded).

**This session's outcome:**
- **Baseline + audit fully green** (108 unit · 150 e2e · 35 smoke) — all standing requirements re-verified: mobile nav R1–R4 (19th check, Tailwind v4 pins hold), data drift, SEO pair, DATABASE_URL, db/ at root, Vitest/Playwright, `.env.example`
- **Session-48 suggestions swept**: sm-band (672px) auth pair — exact match; and the **first-ever keyboard-focus-ring sweep** (real Tab presses) which found **three REAL fixes**: the auth submits' zinc-950 `#09090b` ring (the reference runs distinct ring families per component), the 404's plain-`focus:` slate-500 ring, and the body's white-canvas/shell-paper layering (visually invisible, byte-identical screenshots)
- **TDD throughout**: 4 new e2e written RED first, pin-sanity mutations proved load-bearing, live re-verification with the Tab-walk — full chain now **108/154/35 green**

Two new probe lessons encoded in the SKILL: programmatic `focus()` in agent-browser evals never engages `:focus` (real Tab presses are the only reliable probe), and the display pipeline strips a certain literal 2-char sequence (verify with `charCodeAt` before "fixing" phantom corruption).

**Suggested next steps** (from session_51): a Tab-vs-click focus pair on the reference's dialog buttons (the v19 family was measured with forced `focusVisible`), an aria/landmark audit of the verify-email inputs, or the standing 5-attempts-lockout (still unmeasurable without burning reference attempts). Just re-issue the brief and I'll pick it up from `docs/session_51.md` / `docs/remediation-plan-v25.md`.
