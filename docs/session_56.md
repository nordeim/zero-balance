I'll continue the recurring zero-balance workflow. This iteration references `docs/session_53.md`, `docs/remediation-plan-v26.md`, `worklog.md`, and `docs/session_54.md`. Let me set up the task list and start.
Pull succeeded — brought in `docs/session_54.md`. Now let me review the project docs.
Now let me read the remaining core docs and session docs.
Now let me read the session docs.
All session docs reviewed. The state is consistent: v26 shipped (commit `2879cb0`), full chain green at 108/155/35. Session-53 suggested next surfaces: `prefers-reduced-motion` audit, print/overscroll check, scrollbar styling comparison. Now let me validate the codebase and environment state.
Environment intact and v26 changeset verified. Let me check the remaining state (layout body, node_modules, scandihaven, skills catalog).
Skills catalog reviewed. Let me check the Tailwind v4 skills for mobile-nav guidance (per the brief's emphasis) and the repo's own Tailwind v4 validation report.
Codebase validation complete — all standing requirements in place. Now the audit phase: baseline chain + review of recent changes.
Now running the baseline audit chain — lint, typecheck, and unit tests first.
Build ✓ with robots + sitemap prerendered. Now the e2e suite (155 tests, ~several minutes).
**Baseline chain fully GREEN: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ · 155/155 e2e ✓ · 35/35 smoke ✓.** Now audit Phase 2 — npm audit + secret scan.
Audit Phase 2 clean — same 5 dev-only `braces` advisories (accepted), secret scan matches only documented files. Now the two-site parity sweep. Let me check the probe tooling and boot the parity server.
Logged in to the reference — Balance $3475.00 matches the standing census. Now the data-drift check (21st) and the SEO pair.
Data drift clean (21st) — reference unchanged (alloc 30.5%, Balance $3475, income 1/$5000, savings 1/$1000, expenses 4/$525). SEO pair ✓ on reference. Now the mobile-nav R1–R4 standing check (21st).
R1 reference ✓ (toast containers still intercept the burger, scrollWidth 395 — reference bug persists). Now R2 — sheet trap test.
R2 reference ✓ (sheet still traps after nav — reference bug). Now R3 — desktop rail on `/`, and R4 — per-route overflow sweep.
Reference R1–R4 all verified (21st). Now the clone side — booting the parity server and logging in within one invocation.
**Mobile-nav R1–R4 verified on both sites (21st) — Tailwind v4 pins hold, the clone's mobile menu works.** Now the clone SEO pair + v26 fixes re-verification.
v26 G1 verified live on clone (classless body). Let me re-verify the reference's body class is still classless today, then start the new sweep surfaces.
Reference body still classless — v26 G1 holds. Now the new sweep surface 1: **prefers-reduced-motion audit** (session-53 suggestion, never measured on either site).
The reference does NOT honor reduced motion — sheet slides the full 500ms, zero reduced-motion rules in its CSSOM. Now the clone under the same conditions.
Sheet slide-in under reduced motion: both sites animate identically (full 500ms, zero reduced-motion rules on both). Now the spinner — measuring actual rotation under reduced motion on both sites.
Spinner also matches (both `spin 1s` running under reduced motion). **Surface 1 (reduced-motion): NO DRIFT.** Now surface 2: print + overscroll of the now-white body canvas.
**Surface 2 (print/overscroll): NO DRIFT** — white body, `auto` overscroll, zero print rules on both. Now surface 3: scrollbar styling at the dialog `overflow-y-auto` surfaces.
Need a live scrollable dialog. Setting a shorter viewport to force dialog scrolling, then opening the Add dialog on the reference.
The dialog is open — the reference uses no `role=dialog`. Let me probe it by climbing from the Save button.
Reference dialog: native scrollbars, no styling (`auto`/`auto`, zero rules). Now the same probe on the clone.
**Surface 3 (scrollbar): NO DRIFT** — both `auto`/`auto`, zero rules, identical 90vh panels. All three session-53 suggestions came back clean. Let me extend the sweep to genuinely unmeasured surfaces — starting with `prefers-color-scheme: dark` (never measured on either site).
Dark mode: both sites stay light — NO DRIFT. Extending to the app-surface keyboard-focus rings (the v25 sweep only covered auth + 404; the desktop rail's real-Tab family is unmeasured).
Reference families captured: rail links = blue `#3b82f6` ring-2; buttons = `#0a0a0a` ring-1 + ambient; **stat-card buttons = NO ring at all**. Now the same real-Tab walk on the clone.
Rail-link focus matches (visible blue layer identical — the v23 documented equivalence). But I noticed the clone's stat buttons read `$0.00` — let me verify the dashboard data state.
The clone dashboard shows the zero-state ($0.00) — need to diagnose. Let me check the parity server log and API state.
API + DB are healthy — the zero-state was a measurement artifact (server dies between `with-server.sh` invocations mid-data-flight; the app correctly renders the v16 zero-state for a dead API). Continuing the Tab walk in one invocation for clean conditions.
Stops 6–7 match identically (Add Item = white offset + `#0a0a0a` 1px + ambient; stat cards = no ring). One more unmeasured surface: the dialog **X-close button's** keyboard-focus family (Cancel/Save were swept in v25/v26, the 36×36 in-header X never was).
The reference's dialogs don't trap focus (plain divs) — Tab continues through the page. The class-attribute read is the reliable arbiter (v26 lesson). Let me read both sites' X-close button class lists directly.
**REAL FINDING (v27 G1 candidate)**: the dialog X-close button's keyboard-focus family — reference runs `focus-visible:ring-1` (1px shadcn ghost-icon family) while the clone runs `focus-visible:ring-2` (2px). Let me confirm on a real Tab press and scope the code.
The static probe can't force `:focus-visible`. Per the v25 discipline — real Tab walk until the X is focused, sampling as we go.
Reference X on real Tab: `#0a0a0a` **1px** ring, white 0px offset, no ambient. Now the clone's X under the same walk.
Stop 3 is the X button (empty text + svg). Let me capture its full shadow string.
The walk landed on different stops — let me verify the dialog state directly and walk to the actual 36px X button.
The X has an sr-only "Close" span — my finder required empty text. Fixing and re-running.
**CONFIRMED REAL FINDING (v27 G1):** X-close button renders `#0a0a0a` **2px** ring on the clone vs **1px** on the reference under real Tab. Let me sweep a couple more button families for additional findings — the filter select triggers and card action triggers.
Filter triggers byte-identical. Let me sweep the remaining button families — the burger toggle and the card action-menu trigger.
Search inputs match. Let me scope the full extent of the ring-family drift in the clone's source.
The X-close drift is well-scoped — a single line in `dialog.tsx` (all other ring-2 uses are verified/pinned families). Let me check whether the clone's sheet has a similar X button to scope the fix fully.
The sheet has no X (matches reference). One more sub-check: the reference X's hover color family (`hover:text-accent-foreground` in its class list — the clone lacks it). Measuring both.
**G1 confirmed on two axes**: the X's keyboard ring (1px vs 2px) AND hover text family (`hover:text-accent-foreground` missing on clone). Now writing remediation plan v27. First, let me check the test placement.
The extension pattern is clear. Now writing remediation plan v27.
Plan validated. Now TDD — Step 1: RED. Extending the v9 X-close test with the focus/hover family assertions.
Now I need to add `cls` to the evaluate return object.
Now typecheck and confirm RED (the current app renders the drifting classes).
**RED confirmed** — fails exactly on the drifting class string. Now the G1 fix.
**GREEN.** Now pin-sanity mutations — proving the assertions are load-bearing.
Pin-sanity confirmed — both mutations FAIL, restored GREEN. Now live re-verification on the parity server.
Live verification complete — the X renders the 1px `#0a0a0a` ring on real Tab, matching the reference. Now the full clean-check chain.
**FULL CHAIN GREEN: 108 unit · 155 e2e · 35 smoke.** Now regenerating the screenshots.
Screenshots byte-identical as predicted. Now updating documentation — README first.
Now CLAUDE.md — the e2e list.
Now AGENTS.md — the v27 pin paragraph.
Now the SKILL doc — session row + state updates.
Now persisting the v27 probe scripts into the repo and updating the probe README.
Now the formal session log (`docs/session_55.md`) and worklog entry.
The entry landed without proper spacing. Let me fix the formatting.
Worklog formatted. Final changeset review and re-gate before commit.
Source diff is clean and minimal. Lint green after doc changes; the full chain already ran green post-fix. Now the commit and SSH push — reviewing the wrapper runbook first.
Committed as `eca1754`. Now materializing the SSH key and pushing via the wrapper.
**Pushed and verified: `eca1754` on main.** Key shredded, tree clean. Now updating the parent workspace worklog.
**Parity iteration v27 is shipped to `main` (commit `eca1754`, push verified via the SSH wrapper, key shredded).**

This session's outcome:
- **Baseline + audit fully green on the first run** (108 unit · 155 e2e · 35 smoke) — all standing requirements re-verified: mobile nav R1–R4 (21st check — **Tailwind v4 pins hold, the mobile menu works**), data drift (21st, clean), SEO pair (robots + sitemap live on both sites), `DATABASE_URL=file:../db/custom.db` with `db/` at root, Vitest/Playwright suites, `.env.example`
- **Session-53's three suggested surfaces all swept on first measurement — no drift**: prefers-reduced-motion (both sites animate identically under `reduce`), print/overscroll, scrollbar styling
- **One real fix** (`docs/remediation-plan-v27.md`): the dialog X-close button's keyboard/hover family — the reference runs a 1px `#0a0a0a` focus ring + `hover:text-accent-foreground`; the clone had drifted to 2px with no hover text. Fixed with one class string, TDD-verified (RED → fix → GREEN → pin-sanity mutations), live re-verified on the parity server
- Docs, screenshots, worklog, and 4 new probe scripts all aligned; committed and pushed

**Suggested next steps** (from session_55): a one-pass `:focus-visible` class-census diff of all button variants between the sites (would surface any remaining family drifts in one sweep), or the card action-menu trigger / avatar chip / toast-close keyboard families. Just re-issue the brief referencing `docs/session_55.md` / `docs/remediation-plan-v27.md` and I'll pick it up from there.
