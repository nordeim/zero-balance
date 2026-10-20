The workspace exists. Let me refresh it and set up a task plan.
The repo is on main and clean. Let me set up the task plan and refresh the workspace.
工作区已刷新至 `27c5970`。现在我来查看核心文档。
这些文档篇幅很大。让我先阅读其中最新的部分——会话日志和整改计划——其中记录了当前的状态。
Now the remediation plan v96 and worklog tail to understand the established cycle pattern.
Now I understand the state: v96 shipped (Session 131, main @ 59e7d14 + session-log commit 27c5970). Per the rotation ledger, **v97 targets the v91-era ITEMS pair (INCOME + EXPENSES at 1280x800, sixth re-run)**. Let me review the remaining core docs and skills catalog.
`.env`, `db/`, 和 `.env.example` 都已确认无误。现在我来验证 v97 轮换台账与 v91 探测的自身头部（这是强制性的队列验证规程），并检查探测基础设施。
Queue verified: the v91 probe's own header confirms the ITEMS pair (income + expenses, 1280x800, sixth re-run for v97). Let me check the probe README's v97 queue section and relevant skills.
Let me check the seedcheck mechanism and the environment state, then start the F0 baseline.
Seedcheck 完全一致 (7 items / rent 1850 / expensesTotal 2235 / 0 line items / 3 assets / 2 liabilities)。现在开始 F0 基准链：lint + typecheck。
Lint ✓ · typecheck ✓ · 108/108 unit ✓. Now the production build.
Build ✓ (robots + sitemap prerendered). Now the e2e suite in three chunks — let me check the v96 chunk split strategy.
299 tests in 24 files. Let me derive the three-chunk split by per-file counts.
总计 299 个唯一值。我将拆分为 137/101/61 的分块（遵循双阶段经验，以避免资源耗尽）。让我先检查一下 playwright config，然后运行分块 1。
Chunk 1: 134 passed. Now chunk 2.
E2E fully green: 134 + 96 + 71 = 301 executions = 299 unique tests, zero flakes. Now the API smoke test.
**F0 baseline FULLY GREEN.** Now auditing the commits since the v96 push (59e7d14, 27c5970).
Session-log-only commits confirmed — environment carries over. Now the production-seams re-audit (auth, db-path, SEO pair, Tailwind v4 mitigations, skills/ exclusion).
All seams verified — codebase audit clean. Now **F1 — the axe-core watch**.
F1：无偏差（两侧均为 4.14.0，去重保持）。现在进行 engine-contract 固定独立运行。
**F1 已完成 — 无漂移，引擎 pin 2 已独立通过。** 现在进行 F2 — 第 91 次常驻检查。让我检查一下现有的常驻检查对和派生脚本模式。
Derived clean. Let me check the reaping discipline and run the reference-side standing check.
Reference bugs 1-4 all live (464 overflow measured correctly with settle-wait). But the expenses census reads "no match" — the documented value was "4 items · $525.00". Let me check the script's finder.
The expenses census read "no match" vs the documented "4 items · $525.00" — possibly another timing artifact. Per the standing-script timing-artifact lesson, let me re-measure with an explicit settle-wait before recording.
重新探测使用了一个全新的（未认证）会话。让我找到脚本的会话名称并重试。
Session lost after reaping. Let me re-login and re-measure the expenses census with the settle-wait discipline.
Expenses census re-measured with settle-wait: **"4 items · $525.00"** — the documented value; the earlier read was the timing-artifact class. Reference side: all four bugs live, census unchanged, SEO pair live. Now the clone-side standing checks.
**F2 COMPLETE — mobile menu verified working the 91st consecutive time; all four reference bugs live; census unchanged.** Now F3 — deriving the v97 probe series from the v91 lineage. Let me study the derivation pattern.
Now let me examine the v91 series files to plan the v97 derivation's history corrections.
现在让我按照带有 `hit/miss` 报告规范的既定模式，编写 `v97` 系列推导脚本。
Corrections applied. The residual flags are likely the legitimate v91 tokens in the SIXTH re-run bracket — let me verify my check logic.
所有剩余的 v91 token 均属合法（"last re-shot v91" 的来源 + SIXTH re-run 括号）。我的检查逻辑有 Bug —— 正在修复它。
The bracket spans a line break ("v85\n# → v91 → v97") so the context check misses. Fixing the LEGIT patterns.
The v97 probe series derived cleanly. Now let me study the two-half builder pattern from v96.
Now let me examine the arbit-v97.sh structure for the two-half split.
`CENSUS_JS` 块 = 第 22-214 行，零美元序列。让我验证一下 `seedcheck` `.cjs` 在 `env -u` 规范下的工作情况，然后构建双半形式。
Confirmed — the sandbox's polluted DATABASE_URL is why `env -u` is load-bearing. Now building the two-half form.
Two-half census built (md5 b55dcd29, 193 lines, byte-identical). Now executing F3 — reference-side shots first (with reaping).
Both sides captured. Now the VLM pairwise comparison.
**Both verdicts DIFFERENT** (the documented re-run class). Every flag needs DOM arbitration. Running the two-half census — reference half first.
Reference census captured — note the reference income footer HAS a "Bank Account" payment chip (childCount 2) while expenses footer has only the date (childCount 1) — confirming the DATA-CONDITIONAL class. Now the clone half.
The census output got cut by tail — re-running the clone half with full output capture (the documented v96 lesson).
Both halves captured. Let me verify the card-height delta class (200 vs 230) against the v70b documentation before arbitrating.
The v70b class is documented (Recurring superset wrap h52 → +30px + 1-row sibling stretch). Let me verify the v91 census's documented template strings to compare drift.
v91 的记录确认了每一个标记类。让我将我的普查值与 v91 计划中记录的值进行比较，以进行漂移检查——特别是模板轴。
The census reproduces the v85/v91 values exactly — zero drift on every documented axis. One flag remains: the FAB re-arbitration (the v85/v91-documented class). Let me derive and run the one-shot both-sides FAB census.
**FAB re-arbitrated: fabCount 0 + bodyHasBase44 false on both sides — the platform-chrome class, no clone gap. F3 COMPLETE: NO NEW CLONE GAP.** Now F4 — surveying the pin coverage map for a never-pinned family on the ITEMS surfaces.
让我调研一下 `items` 表面上的覆盖率地图——检查 `v65` `header-row` `pin` 以及 `count-subtitle` `P` 轴。
Badge colors thoroughly pinned. Let me survey the combobox listbox popover interior — a candidate never-pinned family.
The listbox **panel chrome** (the popover container itself) is never pinned — the v36 pins cover option-level chrome, the v91 the trigger's resting chrome. Let me examine the Select component source to understand the panel structure.
The panel chrome (rounded-md/border-input/bg-popover/shadow-md/viewport p-1) is the never-pinned middle layer between the trigger (v91) and options (v36). Let me also check the classification tiles pin before finalizing the candidate.
Classification tiles are pinned (dialog context). The listbox panel chrome is the strongest never-pinned family. Let me find the items-view source for the mutation planning, then run the supplemental two-half census.
The panel chrome comes from the shared `ui/select.tsx` SelectContent. Let me probe both sides to establish the pin's axes — reference first.
Reference panel measured but the shadow string was truncated and the viewport finder hit the scroll button. Let me re-probe with refined finders.
Reference panel chrome fully measured (shadow-md 4-layer string, radius 6px, border 1px rgb(229,229,229), viewport pad 4px). Now the clone side.
Clone measured — visible shadow layers byte-identical, but the clone emits more zero-layers (Tailwind v4's shadow var slots). Let me check how the v45 shadow-md pin handled this.
The v3/v4 shadow-construct precedent is documented (toContain the visible layers). Now let me scope the pin-sanity mutation target — the panel's `rounded-md` line in select.tsx.
Mutation target: line 68 (panel's rounded-md), line 19 (trigger) untouched. Let me verify the v91 trigger pin's radius assertion for the cascade check.
Calculator 的 16px 是对话框面板，而不是列表框。再进行一次覆盖率检查 —— 选项的静止内部（`pad`/`radius`/`h`）从未被固定。
Coverage map finalized — the panel + option-resting interior is the never-pinned family. Now building the formal supplemental two-half census (the persisted measurement with the md5 contract).
**The pin's axes measured byte-identical on both sides** (only h/optCount differ — the seed-data class). Seedcheck exact after the run. Now verifying the mutation target line, then writing the plan BEFORE pin execution.
Mutation target verified (select.tsx:68, exactly one `rounded-md`). Now writing remediation plan v97 — BEFORE pin execution, per the mandatory order.
Plan saved. Now appending the v97 pin to items.spec.ts — let me check the file tail first for the established form.
**Pin GREEN on first run.** Now the pin-sanity mutation — line-number-scoped `rounded-md` → `rounded-lg` at select.tsx:68.
Only the v97 pin red (41 green). Let me verify the failure diff reads as the radius axis alone.
**Mutation hits exactly the radius axis alone** ("6px" → "8px"). Restoring, rebuilding, and running the post-restore full file.
**F4 COMPLETE — 42/42 green post-restore.** Now F5 — the full chain re-run.
**F5 full chain GREEN** — 300 e2e (135+96+71 = 302 executions = 300 unique, zero flakes), 35/35 smoke. Now the screenshots regeneration + byte-compare.
Same-day (Oct 20 UTC) as the committed set — the 07 shot's live date digits should match. Backing up, regenerating, and byte-comparing.
**16/16 BYTE-IDENTICAL** — even the 07 shot (same-day, no midnight crossing). Final seedcheck, then docs alignment.
Changeset is PIN-ONLY (zero src/). Now D1–D7 docs alignment. Let me find the anchors.
All anchors mapped. Writing the D1–D3 alignment script.
D1–D3 aligned. Now D4–D6 — checking the probe README's v96 section structure first.
D4–D6 aligned. Now D7 — session_233.md and the worklog Session 132 entry.
D7 complete. Now the shared workspace worklog update and the pre-ship gates.
Now staging and committing the v97 cycle.
Commit `6a6725c` created — 28 files, +2916/−4, ZERO src/ changes. Now the SSH-wrapper push. Let me review the runbook.
Key fingerprint verified (matches the documented SHA256:3ddaNlFh...). Dry-run now.
The remote has new commits. Let me fetch and check.
The fetch shows origin/main at 27c5970 (my parent) — the push should fast-forward. Let me see the full dry-run output.
The wrapper defaults to the WRONG repo (task-management). Let me check its remote option.
Dry-run clean (fast-forward 27c5970..6a6725c). Executing the real push.
Push verified — remote main @ 6a6725c == local HEAD. Now the independent re-verification and key shredding.
Remote verified, tree clean, keys shredded. Following the established pattern, now the session-log follow-up commit — writing the transcript-style log as session_234.md.
**v97 parity cycle (Session 132) complete and pushed to `main @ d4b77c5`** — remote verified, keys shredded, tree clean.

**What was done:** Refreshed the workspace (carried-over, session-log-only commits verified); ran the full audit chain — baseline all green (299 e2e, 35 smoke), axe watch no drift, 91st standing checks (mobile menu working the 91st consecutive time, all four reference bugs live); executed the ITEMS-pair re-run (both VLM verdicts DIFFERENT, every flag DOM-arbitrated — the payment-chip DATA-CONDITIONAL class proven by the reference's own income footer; **NO NEW CLONE GAP**); added the **filter-listbox panel/option-interior census pin** (the never-pinned "missing middle" layer, +1 e2e = 300, mutation sanity single-axis); screenshots 16/16 byte-identical; docs aligned D1–D7; PIN-ONLY shipped (zero src/ changes) via the SSH wrapper with the correct remote override.

**Next:** Per the rotation ledger, the v98 cycle targets the v92-era SAVINGS pair (now the oldest remaining) — say "continue v98" to proceed, or request adjustments to this cycle's deliverables.
