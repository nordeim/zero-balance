I'll continue the recurring zero-balance remediation workflow. Let me set up the task plan and start by refreshing the workspace.
The workspace was reset. I'll clone the repo fresh.
Repo cloned successfully. Now let me review the core project documentation.
Now let me read the remaining core docs and the latest session docs.
Now let me read the worklog's latest entries and the remediation plan v17.
The picture is clear: this is work session 35 → parity iteration v18, with the formal log destined for `docs/session_36.md`. Let me read the remaining core docs and validate the codebase state.
Let me validate the v17 changeset in the codebase and start the environment setup.
v17 changeset confirmed in code. Now let me start the environment rebuild (npm install) and continue doc review in parallel.
Install complete. Now let me set up the environment: `.env`, Prisma client, and the database.
Environment rebuilt. Now let me run the baseline verification chain (quick gates first), and clone the scandihaven pattern repo in parallel.
Build passed. Now the e2e suite (129 tests, ~45s).
One e2e failure in the register-flow spec. Let me investigate.
Passes in isolation — likely rate-limit accumulation across the full suite. Let me check the spec and the failure detail.
Trace was cleaned by the re-run. Let me re-run the full e2e suite to check if the failure reproduces.
129/129 on the re-run — the first-run failure was a load flake (noted for the audit). Now the smoke test.
Baseline chain fully GREEN (lint · typecheck · 96/96 unit · build · 129/129 e2e · 30/30 smoke). Now the code audit Phase 2: dependency + secret scan.
Audit Phase 2 matches documented state (5 dev-only ESLint braces advisories — accepted; secrets clean). Phase 3: review the v17 changeset diff.
v17 changeset audit clean. Let me verify the scandihaven pattern repo and review its key docs.
Scandihaven reviewed (patterns already reflected in the codebase). Now let me set up the parity audit infrastructure — first the agent-browser skill and the parity server script.
Infrastructure pattern confirmed. This session's fresh surface (per session_34's suggestion): the **net-worth asset/liability error tier** — the last unpinned dialog family. Let me first check the clone's net-worth dialog error handling.
The exact v17 pattern repeating: the net-worth view's DELETE paths use `void deleteAsset(...)` with no catch, and zero error-tier e2e coverage. Let me check the store's delete actions.
The v17 pattern repeats: `void deleteAsset()` rejects unhandled with no toast. Let me see the net-worth view's delete context (confirmation flow).
Structure confirmed. Now let me set up the two-site live audit. First, the reference desktop session (login inside one command).
Reference desktop logged in. Now the clone desktop session (login inside one with-server invocation).
Clone desktop logged in. Now the mobile sessions (390×844) — reference first, with the known React-state fill quirk in mind.
Reference mobile logged in. Now the clone mobile session.
All four audit sessions live. Now the standing checks — data drift (12th) first, using the existing probe pattern.
Allocation 30.5% / Balance $3475.00 — matches documented state. Let me complete the drift check with the items-view census.
**Data drift clean (12th consecutive)**. Now the mobile navigation re-verification (R1–R4) on the reference mobile session.
**R1 re-confirmed on reference** — both toast containers still intercept the burger center. Now the clone side.
**R1 clone confirmed** — direct svg hit, no toast interception. Now R2: the sheet trap test on the reference.
Sheet open, Income at (20,185) 247×32 — documented geometry. Now tap it and check the trap.
**R2 re-confirmed on reference** — navigated but sheet still trapped. Now the clone side.
**R2 clone confirmed** — sheet closes, 390px fit. Now R3: root-route nav highlight on both sides.
Mobile has no open sheet — the rail lives on desktop. Let me measure R3 on the reference desktop session.
**R3 re-confirmed on reference** — nothing active at root. Now the clone.
**R3 clone confirmed** — Dashboard highlighted. Now R4: mobile overflow on the reference (all six routes, `/networth` via full-page load).
**R4 re-confirmed on reference** — 395/464px overflow. Now the clone across all six routes.
**Mobile nav R1–R4 all re-confirmed.** Now the fresh v18 surface: the net-worth asset/liability error tier. First, examine the reference's net-worth cards and delete behavior.
Reference has 1 asset ("Savings Account" $25k) and zero liabilities. Let me inspect the asset card's action menu.
Reference asset menu: plain-text Edit/Delete. Now the key measurement — abort the entity API and test the Delete path.
DELETE request fired and was aborted — silent no-op confirmed on the reference. Now the SAVE failure path: open the Edit dialog with the API still dead.
Edit Asset dialog open. Now save with the dead API.
Dialog closed on save? Let me verify — this differs from the budget-item behavior.
Dialog DOM persists — the role query may be wrong. Let me check the actual dialog structure.
The dialog is still open (plain fixed div, not Radix) — same silent no-op family. Let me unroute and close cleanly.
Reference side measured. Now the clone side — first check the seed's assets, then test the delete failure with a dead API.
Seed: 3 assets. Now test the clone's asset DELETE failure with the API aborted.
**Finding confirmed live** — card stays but NO toast (the `void` swallow). Let me check for the unhandled rejection evidence.
Confirm bar stays open silently. Now the clone's SAVE failure path (dialog catch — expect the superset toast).
Dialog stays open but no toast detected — my selector may be wrong. Let me check the toast component's DOM contract.
The toast uses Radix (`zb-toast` class, role=status). Let me re-probe the save failure with the correct selector — clicking Save again while the dialog is still open.
**Asset SAVE superset verified live** (toast fires, dialog stays open). Let me clean up and quickly verify the liability DELETE failure path.
**Liability DELETE failure confirmed** — same silent swallow. Let me clean up and check the existing delete-toast text convention.
Cleanup done. Let me verify the clone DB is still at seed state (all mutations were aborted).
DB at seed state. The audit is complete — now let me write the remediation plan v18.
Plan saved. Now the TDD RED phase — let me study the v17 error-spec pattern and the networth spec conventions.
Now the networth spec conventions for selectors.
I have the conventions. Let me verify the dialog titles, then write the RED spec.
Now writing the RED-phase spec (tests first).
RED phase: close live browser sessions (memory discipline), then run the new spec before the fix.
**RED confirmed** — both delete specs fail on the missing toast; both save pins pass (superset live). Now the GREEN phase: implement the fix.
Fix in place. Now rebuild and run the GREEN phase.
**GREEN — all 4 specs pass.** Now the full regression chain.
The same register spec failed in the full run again — 2 of 3 full runs now. This is systematic, not a flake. Let me get the failure detail.
The banner vanished between waitForSelector and the evaluate. Let me check what renders `[role=alert]` on the login page.
The error banner was cleared — a second submit raced the evaluate. Let me reproduce with the full login-parity file.
File passes alone — full-suite load only. Let me check the rate limiter's bucket structure.
Buckets are separate — not the limiter. Let me read the trace to find the actual mechanism.
Let me examine the Create account button's busy behavior — that's the likely race source.
The button IS disabled while busy. Let me check the Playwright config for retries/trace settings, then reproduce with full tracing.
Retries: 0, trace retained on failure. Let me re-run the full suite to capture the trace and pin the mechanism.
133/133 — the failure is intermittent (~50% in full runs, never in isolation). Let me check whether the toast system renders any transient `role=alert`.
The toast uses role="status" — only the banner is `[role=alert]`. The one-shot evaluate read races the banner's transient churn (Playwright's actionability retry can re-dispatch the submit). Let me check for other uses of this fragile pattern.
Only the register spec uses the fragile one-shot pattern. Let me harden it with a retrying locator assertion.
Now let me add this flake fix as G2 to the remediation plan, then verify the hardened spec.
Now let me verify the hardened register spec passes, then run the full chain.
Still failing even in isolation now — my theory needs revision. Let me see the actual error.
**Root cause found**: Next.js's route announcer (`__next-route-announcer__`) also renders `role="alert"` — it appears/disappears dynamically, racing the old `querySelector`. My strict locator now hits both. The fix: filter by text.
Let me also check the v12 banner test for the same announcer race.
The v12 test waits on the banner text first (safe — banner precedes the announcer in DOM order). Now let me correct the G2 mechanism in the plan with the real root cause.
Spec fixed. Now the full regression chain.
**Full chain GREEN: 96/133/30 + lint/typecheck/build.** Now the live parity re-verification on a fresh session.
Fresh session needs login. Let me log in and run the verification flow in one invocation.
**Fix verified live** — card stays, confirm bar stays, honest toast fires. Now the recovery check: unroute, cancel, clean reload.
Recovery clean. Now regenerate the screenshots (after closing the live session — memory discipline).
**15 screenshots, zero pixel changes** (behavior-only fix). Now the docs alignment phase.
Now CLAUDE.md updates.
Now AGENTS.md — the v18 pin paragraph.
Now the SKILL doc — state, lesson 36, Appendix B row.
Now the parity-probes README v18 rows.
Now the formal session log — `docs/session_36.md`.
Let me verify the "no remaining void sites" claim before writing the worklog.
The claim was premature — `item-card.tsx:204` still has `void deleteItem(item.id)`. Let me examine its context.
Same pattern in the budget-item card path. Let me check e2e coverage for this specific path.
No coverage — a third void site in the same G1 family. Let me check how items.spec drives the card delete.
The item-card delete IS the tested path — the spec belongs in items.spec.ts. TDD: RED spec first.
RED confirmed. Now the GREEN fix for item-card.tsx.
Now rebuild and run the GREEN phase for the item-card spec.
Still failing — let me check the failure detail.
Wrong header text — let me check the e2e seed's income figures.
The e2e seed income is "2 items · $5550.00" (Salary + Freelance) — my spec used the reference's figures. Fixing.
**GREEN.** Now let me update the plan and docs to reflect the third G1 site (item-card).
Now update all docs for the third site and the new count (134).
Now fix session_36.md — the counts and my premature "no void sites" claim.
Let me verify the closing grep-sweep claim now stands true.
Two more candidate sites — but they call `onDelete` wrappers. Let me check whether those catch internally.
Both `onDelete` wrappers catch internally — those `void` sites are safe (never reject). The sweep claim holds. Now the full chain with 134 tests.
**Full chain GREEN: 96/134/30.** Now the worklog entry.
Now the final changeset review and the git push procedure. Let me review the changeset and read the SSH wrapper runbook.
Runbook clear. Let me check the wrapper's default remote and ssh availability, then commit.
No ssh binary — I'll need the paramiko shim. First, the commit.
Now the push procedure: install paramiko, materialize the key, deploy the shim.
Now materialize the key (outside the repo, 0600) and verify it parses.
Dry-run green. Now the real push.
**Push verified** — remote main @ `cf322f6` == local HEAD; key shredded. Final housekeeping: the workspace worklog.
**Session complete — parity iteration v18 shipped to `main` as `cf322f6` (push verified, key shredded).**

**What this session did:**
- Rebuilt the workspace from scratch (sandbox reset) and re-verified the v17 baseline fully green
- Two-site audit via agent-browser: data drift clean (12th check), mobile nav R1–R4 all re-confirmed — all six superset fixes + Tailwind v4 pins intact
- **Fresh surface measured**: the net-worth asset/liability error tier (the last unpinned dialog family) — the reference is silent on save/delete failures; the clone's delete paths were `void`-swallowed in **three** files (the post-fix grep sweep caught a third site the v16 audit missed)
- **TDD fix**: caught confirm bars + honest toasts across all three files; 5 new e2e specs (RED → GREEN), full chain **96/134/30, no flakes**
- **Bonus root-cause**: the register spec's intermittent flake was Next.js's route announcer rendering a second empty `role="alert"` — hardened and documented as lesson 36
- 15 screenshots regenerated (zero pixel changes — behavior-only fix); docs/worklog aligned; committed and pushed

**Suggested next steps**: the error-state audit is now complete across every entity family — good future directions are a VLM visual sweep of the auth surfaces, or re-measuring the reference's tablet breakpoints; or just say the word for the next verification iteration.
