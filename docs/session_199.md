I'll start by internalizing the operating instructions, then set up a structured plan for this comprehensive codebase audit and remediation task. Since this is a web development task on an existing repo with explicit instructions to "proceed with best recommendations," I'll dive straight in.
The workspace has been reset. Let me clone the zero-balance repo:
Repo cloned successfully. This is a mature project with 196 session logs. Let me check the key documentation files:
The repo is at v82 iteration with extremely detailed commit hygiene. Now let me read the core documentation files:
The docs are dense. Let me read the persisted outputs carefully:
The files have extremely long lines. Let me use bash to read them with truncation per line:
Now let me read the most recent session logs and the v82 remediation plan:
The current state is clear: v82 shipped, next recommended is the v83 cycle. Let me read the v82 remediation plan and recent worklog:
Let me check the worklog's most recent entries (Session 117) and the README:
Now let me review the repo's skills catalog and the SSH wrapper instructions:
Now let me read the SSH wrapper skill doc and validate the codebase state:
I now have a thorough understanding of the protocol. Let me validate the codebase state and check key configs:
`.env.example` is tracked and complete; `.env` needs creation (fresh clone). Let me log progress and kick off the environment rebuild in parallel with scandihaven cloning:
While npm installs, let me review the scandihaven reference repo's key docs:
scandihaven patterns noted (Next.js 16 conventions, Tailwind v4 @theme, SEO surface, Vitest+Playwright+axe gates — all already reflected in zero-balance's architecture). Let me check npm install progress and review the remaining key docs:
npm install completed (354 packages). Now let me set up the environment — .env, database push + seed:
The shell has a polluting `DATABASE_URL` — exactly the documented gotcha. The npm scripts' `env -u` discipline handles it. Let me run the DB setup via npm scripts only:
Database seeded. Let me run the seedcheck to verify the exact documented state:
The seedcheck needs the right field — let me check the schema and the standing-checks precedent:
Type values are lowercase. Fixing the seedcheck:
Seedcheck exact ✓ (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities). Now installing Playwright chromium and starting the F0 baseline chain:
Lint is clean. Let me verify the skills/ exclusion and run typecheck + unit tests:
Lint ✓, typecheck ✓, skills/ properly excluded from eslint. Let me verify tsconfig exclusion and run unit tests:
108/108 unit ✓. Now the production build:
Build ✓ with robots + sitemap prerendered. Checking chromium install, then running the e2e suite in chunks:
Chromium 1243 ✓. 23 spec files. Let me check for orphaned servers, then run the e2e in 3 chunks per protocol:
Chunk 1: 101 passed. Running chunk 2:
All e2e chunks green: **101 + 108 + 78 = 287 executions = 285 unique tests** — exactly the documented v82 state. Now the 35-step smoke test:
**F0 baseline chain FULLY GREEN**: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ · 285 e2e (287 executions) ✓ · 35/35 smoke ✓ — exactly the documented v82 state on the rebuilt workspace.
Now the audit phase — reviewing the recent v82 changes and key code areas:
v82 commit verified: PIN-ONLY as documented (17 files, all tests/docs/probes — zero `src/` changes). Now a focused audit of key production files:
SEO pair + db-path implementation verified. Now checking the Tailwind v4 mitigations and auth:
Audit conclusion: codebase is at documented v82 state, all mitigations in place. Now **F1 — the axe-core watch**:
**F1 — axe watch: NO DRIFT** ✓ (npm-latest 4.14.0, no 5.x; lockfile dedupe state holds; engine-contract pin 2 passed). Now **F2 — the 77th standing checks**. Creating v77 scripts (version-bump from v76):
Version-bump-only diffs verified ✓. Running the reference-side 77th standing check (READ-ONLY discipline):
Reference-side 77th standing check ALL GREEN — four reference bugs all live, data census unchanged, SEO pair live. Now the clone side:
**F2 — 77th standing checks ALL GREEN** — mobile menu verified working (77th consecutive time), all five views zero overflow, SEO pair live. Now **F3 — the v83 re-run pair** (dashboard full-page @1280, last re-shot v77). Studying the v77 probe series as the model:
Now creating the v83 probe series (sed-derived from v77 with version substitutions):
Version-bump diffs verified. Let me confirm the clone and compare scripts:
v83 probe series ready. Running the reference-side shots:
Both sides shot (first-attempt logins). Running the VLM pairwise comparison:
**VLM verdict: IDENTICAL** — the two v61-era target surfaces (Budget Guidelines + Quick Actions) match on every chrome axis; all other deltas are documented classes (seed data, superset nav highlight, user avatar, Base44 platform overlay). Per the v75 convention, the census runs regardless of verdict. Checking the v77 arbitration script:
Creating arbit-v83.sh (the both-sides census) via sed derivation:
Running the v83 both-sides census (reference side first, then clone side):
The census shows the guidelines card byte-identical (visible shadow layers match — the extra clone layers are the v66 transparent-class), grid geometry identical (cardBottom 1122 → gridTop 1462 both sides). But two axes need historical verification: the quick-action label `fw`/`color` and grid `mt`. Checking the v77 census records:
All three deltas are documented classes (v66 shadow-transparent, v61 label-finder wrapper, mt-mechanism with identical rendered gap) — the v83 census **reproduces the v77 census values exactly: zero drift, NO NEW GAP**. Now for **F4 — the pin**. Checking existing pin coverage in dashboard.spec.ts:
Let me examine the v61 F2/F3 pin coverage to identify the never-pinned axes:
No existing pin covers the cross-row gap axes (340/1122/1462) — the v83 pin candidate. Let me check the v61 F3 grid expectation for overlap:
v61 F3 grid expect covers {display, template, gap, w} — no mt, no positions. The cross-row family is truly never-pinned. Let me verify the source structure:
The quick-action grid (line 993) is the last element — no downstream cascade. Checking for any other test pinning this grid's mt or position at any viewport:
Line 2296 mentions "the mt-8 section gap" pinned at 390 by v51 F5. Let me check its exact assertions:
The v51 F5 pins `mt: "32px"` at **390** — so the mutation must be viewport-scoped (`mt-8` → `mt-8 lg:mt-6`) to avoid cascading into it. Let me verify the v51 F5 viewport and check for any 1280 y-position pins:
v51 F5 confirmed at 390. The mutation `lg:mt-6` is inert below 1024px — all 390/640 pins safe. One final check — any full-page height pins at 1280:
All pre-pin verification complete. Writing the remediation plan v83 (plan before execution, per protocol):
Plan saved. Now executing **F4 — writing the v83 pin**. Checking the dashboard.spec.ts tail for the append point:
**PIN GREEN on first run** ✓. Now the pin-sanity mutation (line-targeted — the stat row at :954 has an identical class string):
Mutation applied at exactly :993. Now the standalone REBUILD (separate command, per the v53 lesson), then the pin under mutation:
Pin FAILS under mutation at gridTop ✓ (after cardBottom passed — upstream unaffected). Verifying the exact mutation values and cascade-freedom with the full spec run:
**Cascade-free verified** — 38 green, only the v83 pin red under mutation. Restoring:
**F4 COMPLETE — PIN-ONLY** ✓ (pin green first run; mutation fails at exactly its axes; cascade-free 38 green; restored — 39/39 green, `git diff src/` = 0). Now **F5 — the full chain re-run**:
**F5 chain GREEN**: 102+108+78 = 288 executions = **286 unique e2e** (+1) · 35/35 smoke. Now the 16 standing screenshots:
**16/16 screenshots BYTE-IDENTICAL** ✓ (fourteenth consecutive fully-identical set). Final seedcheck for the record:
**F5 COMPLETE** — full chain green, screenshots byte-identical, seedcheck exact. Now **D1-D7 docs alignment**. Checking current doc states:
Now making the D2 edit (CLAUDE.md — 286 + the v83 pin clause):
Now D1 (AGENTS.md v83 paragraph):
Now D3 (README.md — counts + plan-table row):
Now D4 (zero-balance_SKILL.md — Session 118 row + state lines):
Now D5 (PAD v1.1.40 revision block):
Now D6 (probe README v83 section). Checking the v82 section format:
Now D7 — session_197.md narrative. Checking the session_194 format:
Writing session_197.md (the v83 formal narrative):
Now the repo worklog Session 118 entry:
All D1-D7 aligned. Pre-ship verification — the clean-check gate re-run after the new files landed:
Changeset matches the v82 ship shape — `src/` untouched (PIN-ONLY ✓). Final artifact cleanup check:
All clean. Now the ship phase. Setting up the SSH push infrastructure (paramiko shim outside the repo, per the runbook):
Let me use the field-tested shim from the runbook's Appendix A instead of my hand-rolled version:
Shim deployed. Writing the operator key and verifying it parses:
Key verified (ed25519). Creating the v83 parity commit:
Commit `e0f32ff` created (16 files, +1062). Dry-run push with the explicit `--remote` flag (the v81 lesson):
Dry-run succeeded (fast-forward `7b28990..e0f32ff`). Real push:
**Pushed ✅** — remote verified `main @ e0f32ff`. Shredding the operator key and writing the session transcript:
Remote verified at `064f636 == local HEAD` — both commits pushed. Updating my agent worklog and finalizing:
All tasks complete. Final verification:
The **v83 iteration is complete and pushed**. Here's what was accomplished:

## Summary

**Workspace & Docs** — Fresh clone at `main @ 7b28990` (v82 state); reviewed all core docs (AGENTS/CLAUDE/README/PAD/SKILL), session logs 195/196, the v82 plan, and the worklog. Validated understanding against the codebase — the F0 baseline chain reproduced the documented v82 state exactly (lint · typecheck · 108 unit · build · 285 e2e · 35 smoke, all green on the rebuilt environment with `DATABASE_URL="file:../db/custom.db"` and `db/` at the repo root).

**Audit** — Recent v81/v82 commits verified PIN-ONLY as documented; production seams re-audited clean (scrypt/HMAC auth, db-path resolution, SEO pair, Tailwind v4 mitigations, three test tiers). The `skills/` folder stayed excluded from all checking/testing/compilation. No new findings.

**v83 cycle** (per the repo's own protocol, following the ledger-verified queue):
- **F1** axe-core watch: no drift (4.14.0, engine-contract pin green)
- **F2** 77th standing checks: mobile menu verified working (77th consecutive time), all four reference bugs still live, SEO pair live, zero mobile overflow
- **F3** Dashboard re-run pair @1280: **VLM verdict IDENTICAL**; the both-sides census reproduced v77's values exactly — zero drift
- **F4** +1 pin (286 e2e): cross-row vertical-rhythm census, mutation-sanity verified cascade-free (38 green under mutation)
- **F5** Full chain green; **16/16 screenshots byte-identical** (14th consecutive set)

**Ship** — Commit `e0f32ff` (16 files, +1062) + session-log commit `064f636` pushed to `main` via the SSH wrapper (explicit `--remote`, remote verified == HEAD, operator key shredded). All docs aligned D1–D7; `remediation-plan-v83.md` and `session_197/198.md` saved under `docs/`.

**Recommended next step:** run the **v84 cycle** — the queue points to the v78-era mobile pair (networth + dashboard full-page twins @390, now the oldest re-run candidate); verify against the rotation ledger first, per protocol.
