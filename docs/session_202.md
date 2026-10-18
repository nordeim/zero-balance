I'll continue with the zero-balance audit-remediation workflow. Let me start by setting up the task plan and refreshing the workspace.
The workspace exists and is clean on main. Let me refresh it with `git pull` to get the latest changes.
工作区已更新至 commit `2b2ba34`，包含最新的 `docs/session_199.md`。现在我来审阅核心文档。先从最新的会话文档和项目文档开始。
v83 已确认交付。本次会话应执行 **v84 循环**。我先阅读 v83 修复计划和 worklog，以验证队列建议。
Now let me review the core docs. These are large append-style files, so I'll read the most recent sections (tails) plus key structural parts.
I now have the full picture: v83 shipped, and this session executes **v84 / session_200** — the v78-era mobile pair re-run (networth + dashboard @390, last re-shot v78, now the oldest candidate). Let me check the environment state and the skills catalog.
Environment is preserved (354 packages, .env correct, db/ present, chromium-1243). This matches the v81-style "preserved workspace" path. Let me review the skills catalog and the probe infrastructure for the v84 cycle.
Now let me check the standing-checks scripts (v77 → need v78 for the 78th check) and the probe README for the v83 lessons.
Let me review the standing-checks scripts (needed for the 78th version-bump) and my agent worklog.
All templates understood. Let me check my agent worklog and then begin the audit phase.
The v83 cycle was completed in the previous conversation. This session continues with **v84**. Let me log the start and begin the audit phase.
**Audit Phase** — First, verify the v83 commit is PIN-ONLY as documented (no `src/` changes):
v83 commit verified PIN-ONLY (16 files, zero `src/` changes). Now the production-seams re-audit:
Audit clean — all production seams verified (auth scrypt/HMAC, db-path, SEO pair, Tailwind v4 mitigations, toast fix, test tiers 108/286/smoke, skills/ excluded). Now **F0 — the baseline chain**. First the seedcheck:
**Seedcheck 确切无误** ✓ (7 项 / 租金 1850 / 开支 2235 / 0 个明细项 / 3 项资产 / 2 项负债)。现在进入 F0 基准链。首先检查孤立服务器，然后进行 lint + 类型检查：
Lint ✓ · typecheck ✓ · 108/108 unit ✓. Now the production build:
Build ✓ (robots + sitemap prerendered). Now the e2e suite in 3 chunks — let me split the 23 spec files:
Chunk 1: **102 passed** (v83 pin green). Chunk 2:
**E2E: 102 + 108 + 78 = 288 executions = 286 unique tests** — exact documented v83 state ✓. Now the smoke test:
**F0 FULLY GREEN** — lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · 286 e2e ✓ · 35/35 smoke ✓ (exact documented v83 state on the preserved workspace). Now **F1 — the axe-core watch**:
**F1 — axe watch: NO DRIFT** ✓ (4.14.0 latest, no 5.x; engine-contract pin 2 passed). Now **F2 — the 78th standing checks** (v77→v78 version-bump):
Version-bump-only diffs verified ✓. Running the reference-side 78th standing check (READ-ONLY):
Reference side: all four bugs live, data census unchanged, SEO pair live ✓. Now the clone side:
**F2 — 78th standing checks ALL GREEN** ✓ (mobile menu verified working — 78th consecutive time; R1-R4 + SEO all green). Now **F3 — the v84 re-run pair**. Let me first review the v78 plan (the mobile twins' last cycle) for the census values to reproduce:
Now let me check how the v83 probes were derived from v77 (the sed pattern to follow):
Derivation pattern clear. Creating the v84 probe series (sed-derived from v78 with history-reference corrections):
One missed substitution in the compare script (line 3-4 split across lines). Fixing:
v84 probe series ready. Running the reference-side shots (READ-ONLY):
The script failed silently. Let me debug:
Found it — `vlm78`/`arbit78` don't contain the substring `v78`, so those session-name substitutions were missed. Fixing all four scripts:
arbit-v84.sh correct. Cleaning the accidental `/tmp/vlm78` dir and re-running the reference shots:
Reference shots done (login first attempt ✓). Now the clone side:
Both sides shot (first-attempt logins). Running the VLM pairwise comparison:
Both verdicts DIFFERENT — every flag needs DOM arbitration. The dashboard flags match the v78 set exactly (wrap point v62 class, progress-bar pct class, Base44 tooltip, donut seed class). The networth set has one NEW flag — the "ratio divider" claim. Let me check the history:
The structure test pins the clone's divider (1px solid rgba(255,255,255,0.2)) — but it runs at desktop. The VLM flag is at mobile 390. Let me check the source's responsive summary card:
Source confirms the divider exists unconditionally in the clone (`borderTop: 1px solid rgba(255,255,255,0.2)`, no responsive variant) — the flag is a candidate perception artifact needing DOM arbitration. First, the both-sides census (the v75 convention — runs regardless of verdict):
**The census reproduces the v78 values EXACTLY — zero drift on every axis.** All deltas are documented classes (v41 mobile-superset, v62 width-delta). Now the targeted DOM arbitration for the one new flag — the ratio-divider claim. Let me check the one-shot probe precedent:
Writing the one-shot divider arbitration probe (both sides at 390):
**The divider flag is DISPROVEN — a VLM misread.** The divider renders on BOTH sides with byte-identical chrome (1px solid rgba(255,255,255,0.2), mt 24/pt 24, footer h 53, label 14px/400 156×20). All F3 flags now arbitrated — **NO NEW GAP, v84 is PIN-ONLY**. 

Now **F4 — pin planning**. The ratio-footer divider family (measured byte-identical at 390, never pinned there) is the candidate. Let me check existing 390 pin coverage in networth.spec.ts:
The networth 390 census axes are pinned (v41 F3 + v63 F3) — but the **ratio-footer family at 390 is never pinned** (the v4-era structure test runs at the default viewport). Let me confirm the config viewport and the structure test's placement:
The config default viewport is Desktop Chrome (1280×720) — so the structure test's footer assertions run at desktop. The ratio-footer family at 390 is never pinned. Let me verify what's pinned around it (footer h 53, mt/pt, label axes) to design a cascade-free mutation:
The v67 F3 pin holds the footer {mt, pt, borderTopW, h} at **1280 only**; the v82 pin holds the label's fs at 1280. At **390 the ratio-footer family is never pinned** — that's the v84 pin. Let me validate the mutation target (line numbers + identical class strings + cascade-freedom):
Validation complete: line 389 is unique (`text-sm` appears once), all other ratio-label pins are at 1280 — cascade-free. Now, per protocol (plan before execution), writing **remediation-plan-v84.md**:
Let me fix an awkward draft paragraph in the plan (the card-height arithmetic note) — checking the v63 F3 documented arithmetic first:
Plan saved and validated. **F4 execution** — appending the v84 pin to networth.spec.ts:
The standalone tsc used wrong flags — using the project typecheck instead, then running the pin:
**PIN GREEN on first run** ✓. Now the pin-sanity mutation (by LINE NUMBER per the v83 lesson):
The pin fails at exactly the `ratioLabel` expectation (the footer expectation above it passed — upstream unaffected). Let me verify the exact flipped values:
**Mutation flips exactly the label axes** (fs 14→12, h 20→16, w 156→134 — as predicted). Now the cascade-freedom check — the full networth.spec.ts under the mutation:
**Cascade-free verified** (27 green, only v84 red). Restoring the mutation:
**F4 COMPLETE — PIN-ONLY** ✓ (green first run; mutation fails at exactly its axes; cascade-free 27 green; restored; post-restore 28/28 green). Now **F5 — the full chain re-run**:
Chunk 3 shows 78 passed but should be 79 (+1 new pin) — and there's a test line above. Let me check:
79 passed on the re-run — the first run had a transient flake in the "Liabilities tab" test. Per the v78 precedent, verifying it standalone:
Flake re-verified GREEN standalone (twice) and in-chunk — the documented transient pattern. **F5 e2e: 102 + 108 + 79 = 289 = 287 unique tests (+1)** ✓. Now smoke:
35/35 smoke ✓. Now the 16 standing screenshots — regenerate and byte-compare:
15/16 byte-identical — one diff: `07-add-item-modal.png`. Investigating with a pixel diff (the committed version vs the new shot):
229 pixels in a tiny 14×22 box (~7×11 CSS px — one or two text characters). Cropping both versions for VLM arbitration of the diff crop only:
**The diff is DATE-class**: the Add Item modal's default date field reads `10/17/2026` (committed) vs `10/18/2026` (fresh) — the UTC calendar rollover between the two capture days; chrome byte-identical (229 px = exactly the two day digits). Arbitrated DATE-TEXT-ONLY per the v80 discipline — the regenerated shot ships. Final seedcheck:
**F5 已完成。** 现在进行 D1-D7 文档对齐。先从 D2 (CLAUDE.md 状态更新) 开始：
D2 done. Now D1 — the AGENTS.md v84 paragraph:
D1 done. Now D3 — README.md counts + plan-table row:
D3 done. Now D4 — the SKILL doc Session 119 row + state lines:
D4 done. Now D5 — the PAD v1.1.41 revision block:
D5 done. Now D6 — the probe README v84 section:
D6 done. Now D7 — session_200.md narrative:
Now the repo worklog Session 119 entry (newest-first at the top):
D1-D7 已对齐。现在是交付阶段 —— 首先检查 `arbitration-script` 的存放位置以及待处理变更集：
Changeset matches the v83 ship shape. Let me tidy the scratch scripts — move the arbitration utilities into `scripts/parity-probes/` per convention and decide on the seedcheck:
The convention: `db-seedcheck-v68.cjs` lives in parity-probes. Moving my utilities to match:
`src/` untouched — PIN-ONLY holds. Let me add a proper header to the seedcheck script (matching the v68 convention):
Pre-ship verification — the clean-check gate re-run after all new files landed (the v69 lesson):
All gates green. Now the ship phase — the SSH push infrastructure. Reading the wrapper skill doc first:
Deploying the push infrastructure (shim outside the repo + operator key):
Shim intact, paramiko 5.0.0 ready. Writing the operator key and verifying it parses:
Key verified. Creating the v84 parity commit:
Commit `f66e76d` created (22 files, +1354). Dry-run push with the explicit `--remote` flag (the v81 lesson):
Dry-run succeeded (fast-forward `2b2ba34..f66e76d`). Real push:
**Pushed ✅** — remote verified at `main @ f66e76d == local HEAD`. Shredding the operator key and committing the session transcript:
Now writing this session's transcript (session_201.md, following the session_199 format) for the final session-log commit:
Pushing the session-log commit (re-materializing the operator key for this push, then shredding again):
All pushed and verified. Updating my agent worklog to complete the session:
The **v84 / session_200 iteration is complete and pushed** to `main @ d247d16` on `git@github.com:nordeim/zero-balance.git` (remote verified == HEAD, operator key shredded, tree clean).

## What was accomplished

**Workspace & audit** — `git pull` refreshed to `2b2ba34` (preserved workspace, no reset needed); all core docs + session docs reviewed and validated against the codebase. The v83 commit verified PIN-ONLY (zero `src/` changes); production seams re-audited clean (auth, db-path, SEO pair, Tailwind v4 mitigations, toast fix); `skills/` excluded throughout; seedcheck exact.

**The v84 parity cycle** (ledger-verified queue: the mobile 390 twins, third re-run):
- **F0** baseline chain fully green (286 e2e — exact documented state) · **F1** axe watch no drift · **F2** 78th standing checks all green — **mobile menu verified working for the 78th consecutive time**
- **F3** both verdicts DIFFERENT with every flag DOM-arbitrated; the one **new flag ("divider missing in the clone") disproven** by a dedicated both-sides census — the divider is byte-identical (a VLM misread); the census reproduced v78's values exactly — **zero drift, NO NEW GAP**
- **F4** +1 pin (287 e2e): the ratio-footer family at 390, mutation-sanity verified cascade-free
- **F5** full chain green; screenshots 15/16 byte-identical + 1 DATE-class pixel-arbitrated (modal default-date rollover)

**Ship** — commit `f66e76d` (22 files, `src/` untouched) + session-log commit `d247d16`, pushed via the SSH wrapper; D1–D7 docs aligned; `remediation-plan-v84.md` + `session_200/201.md` saved under `docs/`.

**Suggested next step**: run the **v85 cycle** — the queue now points to the v79-era items pair (income + expenses views @1280, the oldest re-run candidate); verify against the rotation ledger first, per protocol.
