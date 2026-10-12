I'll continue the zero-balance project task. Let me set up the task list and start by refreshing the workspace.
Workspace cloned successfully with all target docs present. Now let me review the 5 core documents.
The core docs are large. Let me read more of the key sections and other core docs.
Now let me read the session docs — the most critical for understanding current state.
Session 124 confirms v52 is delivered. Now let me read the remediation plan v52 and worklog tail.
Now let me check the worklog tail for the latest state and the project structure.
Now let me quickly review the remaining core docs (PAD + SKILL) key sections and verify the codebase state.
The .env doesn't exist in the fresh clone. Let me check .env.example and the package.json scripts.
Fresh clone needs setup. Let me create .env, install dependencies, and set up the database.
Environment set up with db at repo root, sitemap/robots, and test configs in place. Now let me run the baseline verification chain.
构建已通过，且 sitemap/robots 已完成预渲染。现在正运行 e2e 测试套件（245 个测试，大约需要 5.5 分钟）。
244/245 — one possible flake in not-found.spec.ts. Let me re-run just that spec to verify.
Passes standalone — it was a flake. Let me re-run the full e2e suite for a clean baseline.
**245/245 e2e green.** Now the smoke test to complete the baseline chain.
基线链完全通过 — 已确认 v52 状态。本次会话为 **第 53 次迭代**。队列（来自 `session_124`）：/networth 移动端 tablist 普查 + calculator 对话框 390 重排。让我查看一下技能目录。
Skills catalog reviewed — `tailwind-patterns`, `agent-browser`, `tdd`, `clone-app-pat-pro` are the relevant ones. Let me check the key skills and parity probe scripts.
Now let me run the 47th standing checks — reference side first (with the stale-session sweep per the v51 lesson).
部分输出已被过滤。让我查看完整的参考常置检查输出。
参考端检查全部通过 —— 所有 4 个参考 bug 依然存在（superset 已保留），数据完好，SEO 正常。现在通过 with-server 进行克隆端测试。
克隆端检查全部通过 —— v52 P1 burger-selector 修复生效 (R1: sheetLinks 5)，mobile nav 已验证。现在开始针对 Tailwind v4 陷阱的代码审计。
Trap-log scan clean — both `-mb-2` sites live in converted containers. Let me audit the recent v52 production change and review the queue surfaces.
v52 state fully verified. Now planning the v53 sweep: /networth mobile tablist + calculator dialog 390. Let me survey existing coverage.
Coverage map confirms the v53 gaps: networth tablist pinned at 640 only (never 390), calculator dialog pinned at 640 (never 390). Let me study both components' structures.
Now let me study the calculator dialog structure for the 390 reflow.
Let me study the v51/v52 probe script pattern to build the v53 probes correctly.
Let me check how the calculator dialog was opened read-only in the v49 reference probe.
I have the pattern. Let me check how the clone's e2e opens the calculator, then write the v53 probe scripts.
Let me review the existing v50 tablist pin (640) in networth.spec.ts to match the census pattern.
Now I have the full pattern. Let me write the v53 probe scripts — reference side first.
Reference v53 census captured — tablist 432-wide (inside its documented 464-overflow page), calculator panel 358×413. Now the clone-side probe.
Fascinating results — tablist byte-parity (modulo the documented width class), calculator panel chrome identical but the clone shows an **empty state** ("Add First Item") while the reference shows 1 line item. Let me investigate the seed data.
The dev seed has no line items — the reference's 1-row state is a data class. Let me examine the clone's calculator empty state and the Add button variants.
The empty state is the clone's own surface (the reference's empty state is unmeasurable — needs writes, deferred per the v46 rule). Let me run a follow-up clone probe with a line item added to census the row family at 390 (writes are allowed on our own db).
The calculator didn't open. Let me debug with fuller output.
Let me debug the login and page state manually.
The agent-browser session hung (the known stale-engine issue). Let me clean up and retry.
Browser works now. Let me fix the v53b script with better waits and re-run.
Let me use sed to adjust the sleeps directly.
Let me debug the page state directly within the server context.
The manual flow works. Let me inspect the v53b script's login block closely.
Found it — line 25 is missing the `()` invocation, so the login eval never runs. Let me fix it.
**V53 扫描已完成 — 两个表面均字节对齐：**

| 轴 | 参考值 | 克隆值 |
|---|---|---|
| Tablist 390 | 432/36 (在其 464-溢出页面内) | 358/36 (超集修复，pageSW 390) — 所有其他轴完全一致 |
| Calculator 390 | panel 358×413, row 310, addBtn 110×32 | **完全相同** — 413 面板高度且带有 1 行，所有轴均匹配 |

均为仅限 Pin 的交付物。现在让我检查 spec 结构以编写 v53 pin。
Both surfaces verified byte-parity. Now let me write the remediation plan v53. First, let me gather the validation data — exact source lines for the pin targets.
All validation data gathered. Now writing the remediation plan v53.
Now TDD execution — writing F1 (the tablist 390 pin). Let me check the spec's auth setup first.
Specs use authenticated storageState. Now appending the F1 pin to networth.spec.ts.
F1 已追加，类型检查无误。现在将 F2 追加到 calculator.spec.ts。
Both pins written, TS clean. Now rebuild and run the two new tests (should be GREEN immediately — pin-only).
Found it — my F2 test never navigates to /expenses (it's outside the parent describe's beforeEach). Let me fix.
**F1 + F2 both GREEN.** Now the S1 mutation-sanity series. Mutation (a): the TabsList `grid-cols-2` → `grid-cols-1`.
Mutation (a) didn't bite — let me check how the playwright webServer works.
No stale servers, mutation is in source. Let me verify the build picked it up.
The mutation IS in the build. Let me re-run the F1 test against the verified-mutated build.
**Mutation (a) bites ✓** (the earlier pass was a build-timing artifact — lesson: build and test as separate commands). Restore and run mutation (b).
Mutation (b) didn't bite — the active bg must come from elsewhere. Let me investigate.
The CSS rule lingers — let me check what the SSR HTML actually renders for the trigger.
Let me verify the ground truth — what the active tab actually renders on the live e2e server.
Let me look at the current tabs.tsx state and search for other class sources.
Let me directly probe the live server's networth tablist to see the actual computed bg.
The pkill matched the parent script itself. Let me retry without it.
The live build IS mutated (bg transparent) yet the test passed earlier. Let me re-run the test right now to resolve this.
**Mutation (b) bites ✓** (confirmed on the clean re-run — the earlier pass was a build-race artifact). Restoring and running mutations (c), (d), (e).
Sed hit the wrong line. Let me find the actual header line.
**Mutation (c) bites ✓.** Restore and apply mutation (d): panel maxWidth 48rem → 40rem.
**Mutation (d) bites ✓.** Restore and apply mutation (e): total card p-4 → p-2.
**All 5 mutations verified biting ✓.** Restore (e) and verify both tests green on the clean build.
Clean diff — 2 spec files only, zero production changes. Verify both tests GREEN.
Both GREEN. Let me update the plan with the build-race lesson, then run the full chain.
Now the full verification chain — lint, typecheck, unit, then the full e2e suite (247 target).
The suite is timing out — likely a stale process from the killed run. Let me clean up and run it detached with monitoring.
The log may be buffered or the suite is stuck. Let me check the process state.
The detached process was reaped. The timeouts may be the login rate-limiter from many rapid runs. Let me check the rate-limit logic.
Rate limiter is per-process (fresh each run) — not the cause. Let me run the suite foreground with output captured to diagnose the stall.
The suite is running ~2.4x slower than baseline — likely system load from zombie chrome processes. Let me clean up and check.
Load is fine — the environment is just slower now. I'll run the suite in two halves. First, the remaining specs.
2 verify-email tests failed. Let me check the failure details.
Splitting isn't safe — some tests depend on suite-order state. Part A ran fast (1s/test), so the slowdown was transient zombie load. Retrying the full suite now.
The environment is heavily throttled (~7s/test). Let me check whether the earlier split failures were order-dependent or environmental.
All failures are 10s expect-timeouts under env slowness — not real regressions. Let me check the global-setup's re-seed behavior to plan chunked runs.
The re-seed is deterministic per run. Let me verify the failures were environmental flakes by re-running the failed tests in isolation.
Both pass in isolation — purely environmental slowness (12-14s per test). Let me try the full suite once more; the pace has been fluctuating.
Only 41 ✓ but reached test 86 — something else is failing en masse. Let me inspect the log.
45 failures all at 10.5s timeouts, but some tests fly. Let me verify the source tree is still clean and check a failure detail.
Source tree is clean. Let me run one failing spec standalone and watch the server behavior.
1 passed, 4 failed standalone — the click-based tests fail. Let me check for lingering processes and CPU.
**Found it — an orphaned bun server from a killed run (PID 27781, since 06:10) is being reused by every run!** Let me verify and kill it.
Orphaned server killed (it was silently poisoning every run since 06:10). Now re-run the full suite clean.
155 tests all passing (pace restored). Running the remaining specs.
35 failures in the first run too, and the verify-email pair keeps failing. Let me examine these failures.
Many failures — my F2 test's add/delete flow may leave the Rent amount recalculated (server-side rule), breaking dashboard totals. Let me check how the existing v45 F2b test handles cleanup.
**Root cause found** — the v45 test ends with `restoreRent(page)` after its add/delete cycle; my F2 test lacks it, so the recalculated Rent amount poisons every later dashboard assertion. Let me find the helper.
My F2 test needs the `restoreRent` cleanup. Let me add it and check for another orphaned server.
Orphan killed, TS clean. Let me sanity-check dashboard.spec on a fresh boot first.
Dashboard 30/30 clean. Running the full suite as two ordered chunks with orphan checks.
**Chunk 1: 140/140 passed (3.8m), no failures.** Now chunk 2.
**Full e2e chain GREEN: 140 + 108 = 248 passed (246 chromium + 2 setup runs), zero failures — the equivalent of 247 in a single-run count (245 + 2 new pins).** Now the smoke test.
Full chain green. Now the VLM pair on the F2 surface (calculator dialog at 390). Let me check the v52 VLM pattern.
Let me capture the calculator dialog screenshots from both sites for the VLM pair.
VLM flags: 4 are documented data/platform classes. The close-button "boxed X" flag needs DOM verification — let me census both close buttons.
The close button has no border at rest. Let me visually inspect both screenshots directly.
The VLM sees a real difference. Let me crop both close-button regions and compare pixels directly.
The clone's calculator close really renders a boxed button. Let me check the calculator's own close button source.
The DOM shows no border class. Let me analyze the actual pixels in the crops.
The clone genuinely renders extra gray pixels. Let me dump the close button's full computed style and exact bounds on the live clone.
The clone's close has a **1px auto outline** — a browser focus ring (the screenshot caught it focused). Let me check the reference's close for the same.
**Real finding:** on dialog-open, the clone's Radix focuses the close button → the browser's default 1px focus outline renders (the reference's dialog doesn't focus its close; its outline-style is none). Let me check whether the clone's other dialogs show the same ring in existing screenshots.
Let me inspect the existing desktop calculator screenshot's close button.
Let me just ask the VLM directly about the existing desktop calculator screenshot.
**VLM 标记已解决**：`boxed-X` 追踪到 `probe` 的 `synthetic-click` 焦点伪影（仅限 `keyboard`/`script` 焦点的 `outline:auto` —— 即 `a11y` 超集；已验证在真实鼠标流中无 `ring`；参考对象的 `outline-style:none` 是其自身的 `a11y` 回退）。其他 4 个标记 = 文档化的 `data`/`platform` 类。根据 `v43` 规则，该配对很干净。现在正在重新生成 16 张截图。
The dev db still carries my probe's recalculated Rent. Let me reset the dev database and re-seed.
All 16 regenerated byte-identical (no git diffs — the pin-only invariant). Now the docs alignment (D1–D8). Let me find the count sites.
Let me update the docs systematically. First the README count sites and parity table.
Now the docs alignment. D3 first — README updates.
Now add the v53 row to the README parity table.
The remaining 245s are historical table rows (correct as-is). Now D1 — AGENTS.md.
Now D2 — CLAUDE.md.
CLAUDE.md line 75 is the giant E2E section. Let me make targeted edits — the count + the family extensions.
Now D4 — the SKILL doc state line + Session 88 row.
Now D5 — the PAD v1.1.10 revision block.
Now D6 — the probe README's v53 section.
Now D7 — the session logs. Let me check the formal log format first.
Writing session_125.md — the formal v53 session log.
Now session_126.md — the raw transcript.
Now the repo worklog — Session 87 entry + ledger list update.
Now D8 — the workspace worklog.
All docs aligned. Now the final pre-ship verification — git status and the SSH wrapper instructions.
Let me check the ssh shim setup and run the final gates.
Paramiko installed. Let me read the shim source from the how-to doc's Appendix A.
I have the complete shim. Let me deploy it outside the repo and run the final gates.
Key verified. Final gates before commit.
All gates green. Now the commit.
Commit `a6ab17e` landed, clean tree. Now the SSH wrapper dry-run.
Dry-run clean (3f33d5f..a6ab17e fast-forward). Executing the real push.
**推送已验证 — 远程 main @ `a6ab17e` == 本地 HEAD，密钥已销毁，工作区干净。**
**Parity iteration v53 已交付并推送到 main**（`a6ab17e` — 远端 == 本地，密钥已销毁）。

**本次会话核心成果**：
- **v53 普查（PIN-ONLY，零生产代码变更）**：/networth tablist 390（宽度族随参考站自身 464 溢出 bug 分歧，其余轴全部 byte-parity）+ 计算器对话框 390（面板 358×413 双站一致，chip/close 的 flex-shrink 压缩行为逐字节相同）
- **两个新增 e2e pin**（245→247），5 个突变全部验证咬合
- **关键执行经验**（已记入 probe README）：超时 run 遗留的 :3100 孤儿 webServer 被 reuse 导致 45 连败（已诊断+修复）；计算器测试必须以 `restoreRent` 收尾（服务端重算父项金额）
- **全链绿**：108 unit / 246 e2e（两段有序执行）/ 35 smoke / lint / typecheck / build；VLM 配对 5 个 flag 全部 DOM 溯源为数据/平台类
- 移动端导航菜单已验证正常工作，Tailwind v4 trap-log 扫描清洁，SEO/sitemap 双站在线

**下一步建议**：v54 队列已写入 session_125（延迟的参考站 verify/forgot-confirm/计算器空态普查需写授权），或继续剩余移动端表面普查——随时吩咐。
