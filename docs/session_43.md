Workspace exists. Let me refresh it with `git pull` first.
Pull successful — brought in `docs/session_41.md`. Now let me review the core project docs.
The AGENTS.md lines are very long. Let me view the rest via bash with line wrapping.
Now let me read the remaining core docs.
Now the session docs — starting with session_40, session_41, and the v20 plan.
Now let me validate the workspace environment state and codebase structure.
The repo `skills/` folder exists. Let me review the catalog and key skills.
Let me set up my task plan now, then check the sitemap/SEO status (a specific ask in this brief).
Key finding: **no sitemap.ts/robots.ts exist** in the app, while `.env.example` mentions them — this brief explicitly asks to check Sitemap + SEO. Let me check the reference site's SEO surface and verify the rest of the parity state.
The reference has both `robots.txt` and `sitemap.xml` (with routes `/`, `/Income`, `/Savings`, `/Expenses`, `/NetWorth` at weekly/1.0/0.8). The clone has neither — a real SEO/parity gap. Let me check how head metadata is currently tested, then run the baseline chain.
Now the baseline verification chain. Starting with the fast gates.
Lint ✓, typecheck ✓, 96/96 unit ✓. Now build + e2e + smoke.
**Baseline fully green: 96 unit · 137 e2e · 30 smoke + lint/typecheck/build.** Now the code audit phases (per `skills/code-review-and-audit` native-CLI pattern).
Audit clean: no real secrets (wrapper has a redacted placeholder; runbook references the marker only in a validation command), npm audit = same 5 dev-only ESLint braces advisories. Scandihaven current at `d4789c3`. Now the two-site agent-browser parity audit.
Probe infra intact. Now let me set up the two-site agent-browser sessions (ref + clone).
Reference logged in. Now the clone session (login inside one with-server invocation).
Form filled but still on login page. Let me click Sign in directly.
Clone logged in. Now the mobile navigation re-verification (R1–R4) — the task focus. First resize both sessions to mobile.
Viewports set. Reference already shows its documented 395px overflow. Now R1 (burger hit test) on both sites.
**R1 re-confirmed**: reference's two toast containers (`pe:auto`) still intercept the burger at (38,30); clone's hit is DIRECT on the svg with a `pe:none` viewport, 390px fit. Now R2.
**R2 re-confirmed**: reference sheet traps after nav (`sheetStillOpen: true`); clone closes (`openDialogCount: 0`), identical geometry. Now R3 (root-route highlight) at desktop.
**R3 re-confirmed**: reference marks nothing active on `/`; clone highlights Dashboard (white/500 + nav landmark). Now R4 — per-route mobile overflow.
Clone viewport reset to 1280. Resetting and re-running.
**R1–R4 all re-confirmed** — clone fits 390px on all six routes (reference: 395/464). Now the data drift check (15th consecutive).
**Data drift clean (15th consecutive)**: reference unchanged (income $5000.00/1, savings $1000.00/1, expenses $525.00/4, balance $3475.00). Now the fresh parity surfaces — session_40's suggested next steps. Let me verify the VLM tooling and capture the calculator populated state.
Reference calculator captured: 1 line item (Contents Insurance, $25.00). Let me check the clone's seed for an expense with line items.
The screenshot script already has the calculator create+cleanup pattern. Let me capture the VLM pairs — first the reference calculator (already open with 1 line item).
The VLM flags two calculator diffs. Per the v19/v20 lesson, every flag needs DOM verification before it becomes a finding. Let me verify both claims in the DOM.
**Major flag**: the reference's row actions are `opacity-0 group-hover:opacity-100` (hover-revealed) with `w-3.5 h-3.5` (14px) icons — while the v6 pin documented them as ALWAYS visible 32px/16px. Let me check the clone's rendering and the "Will update" conditional.
Let me measure the reference's row-action computed styles precisely — opacity, icon size, button size.
The reference's buttons are 32×32/16×16 (same geometry + colors as the clone) but the container is `opacity-0` at rest — hover-revealed. This contradicts the v6 "always visible" pin. Let me check the v6 plan's original finding.
The v6 measurement said reference opacity-1 "on a live row" — likely measured under hover. The current at-rest measurement (opacity 0, hover-revealed) is ground truth now. Let me also verify the "Will update" conditional — need the reference's Rent parent amount.
**"Will update" flag refuted as data-driven**: reference's Rent parent ($25.00) equals its line-item sum, so the hint correctly hides; the clone's Rent ($1850) doesn't. Both conditionals match. Let me verify the clone's post-mutation parent amount, then restore the seed.
The clone's parent recalculated to $25.00 — "Will update" flag is fully data-driven (refuted). Now let me check globals.css for the group-hover variant situation (Tailwind v4 media-gating matters for this fix).
No group-hover variant pin exists yet — needed for the fix. Let me check the existing spec that pins the row-button opacity.
The v6 spec measured opacity 1 with the mouse parked away — so the **reference has changed** since session 11 (real reference chrome drift, like v19's recurring row). This is a v21 finding. Now let me restore the clone's seed state, then continue the sweep.
Seed restored. Now the mobile sheet's open state — VLM pair at 390×844.
The sheet pair's only flag is route-state (reference was on `/expenses`, clone on `/`). My capture error — let me re-capture on the same route.
Sheet-open verdict: both flags are the documented superset #3 (root-route Dashboard highlight) + avatar letter (data) — **chrome parity holds**. Now the net-worth populated EDIT dialogs.
The X-close claim again (flagged and DOM-refuted twice before). Let me verify it a third time on this exact dialog state, both sides.
X-close **thrice-DOM-refuted** (identical 36×36/16px/transparent both sides) — net-worth edit-asset chrome parity holds. Now the register POST-SUCCESS landing (the unmeasured auth flow). First check the smoke test DB so I don't pollute it.
Smoke test only uses the demo account — safe. Let me check the clone's register flow code first, then measure the reference live.
The clone auto-logins and lands on `/`. Now measure the reference's register post-success landing live.
**Major finding**: the reference's register flow gates on **email verification** — a 6-digit code state, NOT auto-login. Let me capture the full state.
The reference's register gates on a 6-digit email code (6×40×44 numeric inputs). Let me measure the wrong-code path and the unverified-sign-in path on the reference.
The reference's full register semantics are now measured: verify-email gate, wrong-code countdown ("4 attempts remaining"), and unverified sign-in rejection ("Please verify your email before logging in..."). Let me check the clone's current register spec expectations.
Existing register specs only test error paths — safe. Now a quick keyboard-navigation sweep on the login surface (the last suggested surface).
The clone's email input shows NO focus ring under Tab — while the reference shows the pinned two-layer ring. Let me check the INPUT_CLS code.
The clone's measured focus state contradicts the pinned v13 spec (which passes in e2e). Let me re-verify carefully — the probe may have raced.
The clone's input under Tab shows no ring — but the v13 spec passes. Let me read how the spec triggers focus.
The spec settles 350ms before reading. My probe raced the transition. Re-measuring with settle:
Focus ring confirmed present (the truncation + transition lessons again). Keyboard sweep clean. Now let me capture the verify-state chrome details on the reference — and test the re-register-with-unverified-email path.
**Re-register with an unverified email → verify state again** (the reference's resend semantics). Let me measure this state's chrome in one pass.
Chrome captured — the v12 confirmation-state family (24px/700 h2, 16px slate-600, 14px slate-500 back link, 44px primary button). One wrong-code entry to capture the error chrome:
Error chrome: 14px/400 `#b91c1c` centered (the v12 banner-red family as plain text). Let me test Resend, then screenshot the clean state.
All reference measurements complete. Let me confirm the clone's current sitemap/robots state (should be 404s), then write the remediation plan v21.
Both 404 — confirmed. Now let me read the current auth API + validation code to spec G3 precisely.
All context gathered. Now writing the remediation plan v21.
Plan saved. **G1 TDD — RED first**: the sitemap/robots e2e spec.
**RED confirmed** (sitemap 404s). Now GREEN — the MetadataRoute files.
Next emits `User-Agent: *` (capital A) vs the reference's `User-agent: *` — robots directives are case-insensitive per RFC 9309. Let me see the actual generated bodies, then relax the spec with documentation.
Two deltas: Next serializes priority 1.0 as `1`, and my `lastModified` adds a field the reference's sitemap omits. Fixing both for parity:
G1 GREEN. Let me also pin the no-lastmod shape (the reference omits it):
**G1 complete.** Now **G2 TDD** — flip the calculator spec's G9/G10 block to the hover-reveal contract.
**RED confirmed** at the exact unfixed state (opacity 1 at rest). GREEN — the fix:
Now the group-hover variant pin in globals.css:
**G2 GREEN.** Now **G3** — the register verify-email flow. Schema first:
Now the verification pure seam + unit tests:
Now the zod schemas:
Now the register route — re-issue for unverified, 409 for verified, no session:
Now the new verify-email route:
Now the login route — the unverified rejection:
Now the store actions:
Now the login card — let me study its mode machine first.
The file is fine (display artifact — `od -c` shows `const [mode,` correctly). Let me grab the last reference chrome details (hint text + input borders) before writing the verify UI.
One more structural check — the back button's position and that image between it and the h2:
Structure captured: top-left back link, 64px centered logo mark, h2, 2-line paragraph. Let me check the clone's LogoMark, then write the verify mode.
Complete reference spec captured: 64px slate-100 circle with 32px `lucide-shield-check #334155`. Now writing the verify mode into the login card:
Now the CodeInputs module-scope component (after LogoMark):
Now the LoginCard state machine — verify states, submit handler, and the verify panel:
Now the submit handler — the signup→verify transition and the verify submit:
Now the verify panel rendering. Let me check the primary button's exact class string first:
Clean. Now the seed — pre-verify the demo user:
Global-setup re-seeds e2e.db with the same seed (demo pre-verified). Now the e2e spec:
The email lives inside the paragraph (not its own element) — the exact locator can't match. Fixing:
All 5 G3 specs green. Let me add the validation schema unit tests:
Unit tests green. The smoke test should cover the new endpoints too — let me check its structure:
Adding the verify-email gate steps to the smoke test:
**35/35 smoke.** Now the full clean-check chain — complete e2e suite:
**FULL CHAIN GREEN: 108 unit · 142 e2e · 35 smoke.** Now the live parity re-verification of all three groups on :3200.
Synthetic events can't apply `:hover` — using a real hover via the CLI:
**G2 live-verified**: identical container classes, geometry, colors; opacity 0 at rest → 1 under hover. Cleaning up the line item, then G3's live check + VLM pair:
Now G3's live verification — register a fresh account on the clone and screenshot the verify state:
The state isn't advancing. Let me test the register API directly:
My test email was malformed (two `@` symbols) — native validation correctly blocked it. The app works. Retrying with a proper email:
The verify state renders. Screenshot + VLM comparison:
**VLM: IDENTICAL.** Let me complete the live flow — enter the code, verify, land on the dashboard:
All three groups live-verified. Now regenerating the docs screenshots:
Two shots changed — 08 (expected: G2's hover-revealed row actions). Let me verify 07's change is only frame noise:
07 is frame noise (0.0%). Only 08 changed meaningfully (the G2 fix). Now docs alignment — starting with README:
Now CLAUDE.md:
Now AGENTS.md — the v21 pin paragraph:
Now the SKILL doc:
Now the probe README v21 rows:
Now the formal session log — docs/session_42.md:
Now the repo worklog entry:
Now the parent workspace worklog per the multi-agent protocol:
All docs aligned. Final verification of the changeset + quick gates:
All gates green. Now the commit + push per the SSH wrapper runbook:
Shim + paramiko ready. Materializing the key outside the repo, then committing:
Key valid. Committing the changeset:
Now the push via the SSH wrapper (dry-run first, then the real push):
**Push verified** — remote main @ `34f0911` == local HEAD, key shredded. Final cleanup:
**Session complete — parity iteration v21 shipped to `main` as `34f0911`** (push verified via the SSH wrapper: remote ref == local HEAD, key materialized outside the repo and shredded after use).

**What this session did:**
- **Refreshed** the workspace (`git pull` → `dc09bf5`), re-read the full doc chain, re-verified the baseline (96/137/30 green) and the environment (`.env` with `DATABASE_URL="file:../db/custom.db"`, `db/` at repo root, Vitest + Playwright configs intact)
- **Re-audited both sites live** — mobile nav R1–R4 all re-confirmed working (the Tailwind v4 pins hold), data drift clean (15th consecutive), the v20 changeset verified in code
- **Found and fixed 3 finding groups, TDD-first** (6 new e2e + 12 unit tests + 5 smoke steps): **(G1)** the SEO gap — the reference's `sitemap.xml`/`robots.txt` added via Next.js MetadataRoute; **(G2)** the calculator's row actions re-measured hover-revealed on the live reference (its chrome changed since v6) + the `@variant group-hover` pin; **(G3)** the register flow's **email-verification gate** measured live for the first time and rebuilt as the honest superset (full "Verify your email" state, verify-email + resend APIs, 403 unverified-login rejection, honest no-mail code delivery, demo user pre-verified)
- **Full chain green: 108 unit · 142 e2e · 35 smoke**; the verify-state VLM pair came back IDENTICAL; docs, screenshots, session log (`docs/session_42.md`), remediation plan v21, and both worklogs aligned

**Suggested next steps** (per session_42.md): the mobile-viewport calculator pair + the nested line-item edit dialog under the VLM, a systematic keyboard-nav sweep on the app views, or the reference's 5-attempts-exhausted lockout state — say the word for the next iteration.
