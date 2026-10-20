The workspace exists. Let me refresh it and check the git status.
工作区已在 `main` 分支且处于最新状态。我来执行 `git pull` 并开始文档审查。
工作区已更新至最新的 commit `2b0bb52`。让我来规划完整的工作流。
AGENTS.md is very large (292KB). Let me scan its structure and read key sections.
现在让我来审查会话文档 —— session_228.md、session_229.md 以及 remediation-plan-v95.md。
Session 229 已记录了已完成的 v95 周期。根据轮换记录，下一个周期是 **v96 —— v90 时代的 MOBILE 390 双生子重新运行**。让我来查看 v95 的补救计划和最新的 worklog。
The state is clear: v95 shipped, next cycle is **v96 — the v90-era MOBILE 390 twins fifth re-run**. Let me verify the workspace environment state (this appears to be a carried-over workspace, not a fresh clone).
工作区是来自 v95 的沿用环境 —— commit 2b0bb52 仅包含 session-log（仅文档，无 src/ 变动），因此不需要进行环境重新配置。现在让我根据轮转记录验证 v96 周期目标（队列文本验证经验教训）。
Ledger 已验证 —— v96 针对位于 390x844 的移动端 390 双胞胎（/networth + dashboard full-page），这是它们的第五次重运行。让我检查一下 skills 目录和 seedcheck 模式。
已找到 Seedcheck 模式。让我更新计划，并从 seedcheck + F0 基准链启动 v96 周期。
Seedcheck 完全一致。现在让我审计一下自 v95 推送以来的那一次 commit（会话日志专属 commit 类），然后开始基准链。
Confirmed: session-log-only commit — zero src/ deltas. Per the documented class rule, no re-provisioning needed. Starting the F0 baseline chain: lint + typecheck.
Lint ✓ · typecheck ✓ · 108/108 unit ✓. Now the production build:
使用 SEO 对（robots.txt + sitemap.xml）预渲染进行构建 ✓。现在开始 e2e 套件 —— 让我检查一下 v95 的分块策略和每个 spec 的计数。
Chunk 1: 139 passed. Now chunk 2:
E2E 全部通过：139 + 100 + 61 = 300 次执行 = 298 个唯一测试，零 flake。现在进行 API 冒烟测试：
F0 baseline FULLY GREEN. Now F1 — the axe-core watch:
F1 axe watch: NO DRIFT (4.14.0 both sides, only canary prereleases beyond, engine-contract pin 2 passed). Now F2 — derive the 90th standing checks from the v95 pair:
`Standing-checks` 脚本的索引已达到 `v89`。让我检查一下 `v95` 周期是如何处理 `F2` 的——阅读完整的 `session_229` 叙述部分，了解 `standing-checks` 的推导过程。
现在命名规范明确了——`standing-checks` 对追踪 `ORDINAL`（v95 运行了第 89 个）。对于 v96，我推导出第 90 个对。让我来编写推导脚本：
派生已验证。现在应用 pre-run reaping 规范，然后运行 reference-side 的 standing check：
参考侧的 bug 1-3 已确认生效。R-bug 4 显示 `docSW:390` ——让我检查一下测量详情，因为记录的 bug 是 464px 溢出：
R-bug 4 的测量值为 390（无溢出）——这很可疑；记录的 bug 为 464px。让我手动重新探测，延长等待时间以排除时序伪影的影响：
464px 的溢出 bug 确实存在 —— 早先 390 的读取结果是一个由于加载时间引起的问题。让我验证一下记录的 expenses census 值以进行对比：
参考侧数据一致。现在进行部分间的清理，然后进行克隆侧常规检查：
**F2 已完成 — 移动端菜单已验证连续第 90 次均正常工作。** 现在执行 F3 — 从 v90 lineage 推导 v96 probe series。让我研究一下 v90 series 的结构：
现在让我研究一下 v95 周期的推导方法（持久化脚本）以及 v95 任意结构：
现在让我看看 v95 推导出的 header，以了解正确的 header 修正形式：
让我看看完整的 v95 twohalf builder，以了解 clone-half 的结构：
让我检查一下 v90 周期的判定记录，以确保 v96 比较头部的历史记录准确无误：
v90 的判定结果与记录的类不同。现在开始编写带有精确片段替换和验证功能的 v96 推导脚本：
One miss — let me check the exact text form in the compare file:
All corrections applied. Let me verify the derived headers:
Headers correct. Now build the two-half census form:
已构建采用 `md5 contract` 的双半部分（`82cf8a43` / `85e4ec7e`）。现在开始执行 F3 —— 首先运行 `reference-side` 快照（包含 `reaping` 常驻步骤）：
VLM verdicts: DIFFERENT (same class as v84/v90 re-runs). Every flag needs DOM arbitration. Let me check the v90 plan's documented arbitration classes for these exact flags:
The stat-tile and subtitle-wrap flags map to documented classes, but the **clipped negative figure** is a NEW flag needing arbitration. First run the census halves, then a supplemental targeted probe. Running the reference census half:
Reference census reproduces v90 values exactly. But `spendingCard: "no Spending Breakdown heading"` — let me check the v90 documented value for this axis:
让我检查一下 v84 计划中两侧的 spendingCard 记录值：
The spendingCard axis values weren't documented in v84/v90 plans (only the summarized families). Running the clone census half now — the key comparison is the documented axes:
Clone census reproduces v90 values exactly on every documented axis — and `spendingCard` reads the same fallback string on BOTH sides (byte-identical axis). Let me quickly verify why the finder misses on the clone (source check):
Both sides use a div (not h1-h4) for that heading — the fallback string is itself the byte-identical reading. Now the one NEW VLM flag needs DOM arbitration: the **clipped negative net figure** on the clone's networth card at 390. Let me check what the v41 F3 pin already covers for the figure:
The figure's text-width axis is never pinned — the flag needs the supplemental one-shot census. Let me also visually check the screenshot first, then DOM-arbitrate:
**Flag DOM-arbitrated as a VLM misread** — the figure is fully in-bounds (0px left overhang, 115px right margin, no overflow). NO NEW CLONE GAP — the v96 iteration is PIN-ONLY. Now F4 — survey pin coverage to find the never-pinned family on the mobile twins' surfaces:
Let me survey the coverage map — grep the specs for the candidate never-pinned axes:
The breakdown svg family is already pinned (v78). Let me survey the figure/label/ratio coverage at 390 more precisely:
The coverage map is clear: **the figure's fw/color and the label's family are never pinned at 390** (pinned at 640/1280 only) — plus this cycle's new figclip in-bounds axes. Let me check the seed's net figure and the tile value line for mutation scoping:
Net figure confirmed: −245,950 (deterministic under the e2e seed). Now build the supplemental two-half census for the pin's axes — following the build-qa-timing-v95.py pattern:
Now let me quickly probe the reference's summary card head-row structure before finalizing the census (label text may differ):
Reference has the same "Total Net Worth" label structure. Building the supplemental two-half census:
The census output got cut by tail. Re-running the clone half with full output capture:
Both halves measured. **The parity axes are byte-identical** (label family, figure fw/color, flush-left start, no-scroll fit); the deltas are all documented classes (v41 card/fs, seed-data text). Now the coverage-map verification before writing the plan:
Coverage map verified: figure fw pinned only at 640/1280 (dashboard's 30px hero is a different element); `max-sm:` appears nowhere in src/. Now, per the mandatory order, write the remediation plan BEFORE executing the pin. Checking the v95 plan's F4 + validation structure:
Now writing the remediation plan v96 (before pin execution, per the mandatory order):
Plan saved and validated. Now appending the v96 pin to networth.spec.ts:
**Pin GREEN on first run.** Now the pin-sanity mutation — first verify the target line:
Only the v96 pin red (30 green). Verifying the failure diff reads as the fw axis alone:
**Mutation hits exactly the fw axis alone** ("700" → "800") — cascade-free as constructed. Now restore and rebuild:
F4 complete — 31/31 green post-restore. Now F5 — the full chain. First check the date situation for the screenshots byte-identity law:
Current time Oct 20 00:11 UTC — the seed (Oct 19 22:41) crosses the UTC day boundary. Let me check whether the shots render stored or relative dates:
Dates render from stored ISO values — the untouched db keeps the shots deterministic. Running F5 chain — lint, typecheck, unit first:
E2E: 140+100+61 = 301 executions = 299 unique tests (+1 as planned), zero flakes. Smoke test:
15/16 byte-identical; `07-add-item-modal.png` differs — likely the form's live default date (Oct 19 → Oct 20 rollover). Let me verify the mechanism:
Confirmed: `budget-item-dialog.tsx:83` — `date: todayIso()` (live render-time default). This is the date-rollover class crossing UTC midnight. Let me run the pixel-diff arbitration to prove the delta is confined to the date field:
区域为 32×22 物理像素（逻辑 16×11 —— 正好是两个日期数字），但我的 `y-bounds` 是针对错误的图像尺寸进行校准的。让我检查一下 `v75` 判例的验收形式和捕获视口：
The v75 precedent's criteria: width ≤ 48 ✓ (32), height ≤ 40 ✓ (22), x > 1000 ✓ (1535) — **the DATE class confirmed**. My script's bounds were miscalibrated. Fixing it to the precedent form:
**F5 完成** —— 截图 15/16 字节一致 + 1/16 已仲裁的 `DATE` 类。现在进行 D1–D7 文档对齐。让我研究一下 v95 对齐脚本作为模板：
Now let me find the current anchors for the D1–D6 alignment:
All anchors mapped. Writing the v96 alignment scripts:
D1–D3 aligned. Now D4–D6 — checking the v95-b script structure:
D4–D6 aligned. Now D7 — writing session_230.md (the formal narrative):
Now the worklog Session 131 entry:
D1–D7 complete. Updating the shared workspace worklog, then pre-ship gate checks:
ZERO src/ changes confirmed (PIN-ONLY). Checking the .env.example requirement from the task:
.env.example is tracked, clean, and codebase-matched. Final lint gate, then commit:
Commit `90f766e` created — 30 files, +2668/−6, ZERO src/ changes. Now the push via the SSH wrapper. Reviewing the runbook:
Shim ready (python3.13 has paramiko). Deploying the key and running the dry-run:
Dry-run clean (fast-forward 2b0bb52..90f766e). Executing the real push:
Push verified — remote main @ 90f766e == local HEAD, keys shredded, tree clean. Now the session-log follow-up commit (the established pattern — session_231.md):
The **v96 parity cycle (Session 131)** is complete and pushed to `main @ 59e7d14` — remote verified, keys shredded, tree clean.

**Cycle summary:**

| Phase | Result |
|---|---|
| **F0 baseline** (carried-over workspace) | seedcheck exact · lint/typecheck/108 unit/build ✓ · 298 e2e zero flakes · 35/35 smoke |
| **F1 axe watch** | NO DRIFT (4.14.0 both sides, dedupe holds) |
| **F2 90th standing checks** | Mobile menu working the **90th consecutive time** (Tailwind v4 mitigation holds); ref's four bugs live — the 464px overflow re-verified after a timing artifact |
| **F3 mobile-twins re-run** | Both verdicts DIFFERENT (documented class); **new "clipped figure" flag = VLM misread** (figclip census proves in-bounds); census reproduces v90 exactly — **NO NEW CLONE GAP** |
| **F4 pin (+1 e2e = 299)** | Head-row typography + figure-fit census at 390; mutation hit exactly the fw axis; restored 31/31 |
| **F5 + ship** | 299 e2e · 35 smoke · screenshots 15/16 byte-identical + 1/16 DATE class (UTC-midnight rollover, pixel-diff arbitrated) · 30 files, **ZERO src/ changes** |

Per the rotation ledger, the **v97 cycle** targets the v91-era INCOME+EXPENSES pair (sixth re-run) — say "continue v97" to proceed, or request adjustments to this cycle's deliverables.
