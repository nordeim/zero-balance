I'll continue the zero-balance clone project. Let me start by refreshing the workspace and reviewing the latest documentation (now session_114, remediation-plan-v49, session_115).
The workspace has been reset — the `zero-balance` directory is missing. I'll clone the repository fresh as instructed.
Repository cloned successfully with the latest state (v49, sessions 114/115). Let me set up the task plan and start the document review.
session_115.md is the v49 session transcript — v49 delivered & pushed (login mobile spacer fix, 232 e2e). Now reading remediation-plan-v49 and session_114:
v49 plan fully executed per the transcript. Let me read session_114.md and the worklog tail to complete the picture:
The worklog is newest-first. Let me read the head:
v49 fully delivered. Now let me review the 5 core docs' latest state sections (they're huge — I'll target the newest markers):
All docs confirm v49 state (108 unit / 232 e2e / 35 smoke). Now validating against the codebase:
Fresh clone needs `.env` + db setup. Let me check package.json scripts, configs, and v49 artifacts:
v49 artifacts confirmed. Now setting up the environment (.env + dependencies + database):
Database seeded. Let me check seed credentials and test configs:
Test infrastructure verified. Now running the baseline chain (lint → typecheck → unit → build):
Build ✓ with sitemap/robots prerendered. Now the e2e suite (232 tests, ~5.3m — killing agent-browser daemons first per the v46 lesson):
The tail was truncated. Let me get the full suite summary:
The fresh environment needs Playwright browsers installed. Installing chromium:
**232/232 e2e ✓ (5.4m)**. Now the smoke test to complete the baseline chain:
**基线链全绿：lint ✓ · typecheck ✓ · 108 个单元测试 ✓ · build ✓ · 232/232 个端到端测试 (5.4m) ✓ · 35/35 冒烟测试 ✓** — v49 已确认。正在更新待办事项并进行审计：
Audit matches the documented state (5 dev-only advisories, `--omit=dev` = 0; the scan hits are the by-design reference-site probe credentials). Now reviewing the skills catalog:
Let me check the key skills and existing probe infrastructure:
Let me examine the standing-check scripts to understand the invocation pattern:
Infrastructure ready. Running the **44th standing checks** — clone side first:
克隆端 R1–R4 + SEO 全部通过。现在处理引用端：
R-bugs 1, 3, 4 confirmed live. R-bug 2 needs the precise overlay census (the heuristic text-keyed detector is a known artifact). Re-verifying:
**R-bug 2 (sheet-trap) CONFIRMED LIVE** via precise census — overlay 390×844 remains open on /income. All 4 reference bugs live = superset preserved. Closing the sheet and proceeding to the **v50 sweep** (the three session-115 queue candidates):
The 44th standing checks are complete. Now planning the v50 sweep. Let me first study the clone's code for the three surfaces:
Let me check the login-card mode switching and the tabs primitive before writing the probes:
我在第 403 行发现了一个潜在的问题 —— `const ode, setMode]` 看起来格式错误。让我核实一下：
The line number shifted between reads (403 → 395) — something may be modifying the file. Let me check git status and the actual content:
Working tree is clean yet this line looks malformed — but typecheck/build/tests all passed. Let me hexdump it:
The octal dump confirms the file is actually correct (`const [mode, setMode]` — a display artifact in earlier output, not a real issue). The codebase is verified clean. Now writing the v50 reference-side probe for the three queue candidates:
Surfaces 1 & 2 measured. Surface 3 (hero) returned empty — the heading finder failed. Let me debug with a robust approach:
The H3 exists ("NET ZERO GOAL" 18px). The finder walk must have errored. Let me re-census with a direct approach:
The hero card structure needs deeper census. Let me study the clone's NetZeroGoalCard first, then census both sites properly:
Now let me census the reference hero's internal structure and the true grid level:
Empty output — likely an eval exception. Let me break the census into smaller steps:
Card found. Now the grid level and internals in separate smaller evals:
Grid censused (1-col, 24px gap, goal 316 + breakdown 324@y593). Now the goal card internals:
All internals censused except the chip. Let me find it in the balance box:
Chip found — svg is 12×20 (narrower than square). Let me check the svg's classes and then measure the clone side:
The reference's chip svg is squished by flex-shrink (w-5 h-5 class but computed 11.7px — the reference's own width pressure at 390). Now let me census the clone side with the same probes:
The probe timed out at 300s. Re-running with a longer timeout:
Something hangs. Let me debug step by step — boot the server and test agent-browser manually:
agent-browser works with a pre-booted server. Let me check if the background server survives across commands, and run the clone probe directly:
The server persists. Let me convert the clone probe to run directly against the pre-booted server:
The first eval hangs. Let me test it manually to find the cause:
Stale daemon state from the killed runs. Applying the v46 lesson (pkill before every run) and retrying:
The script exits 0 immediately after the first header — tracing to see why:
Found it — the stale `clone50` session state from the killed runs hangs agent-browser. Cleaning stale session files:
普查完成。对比结果如下：
- **表面对齐 (Surface parity)**：sign-in ✓, tablist 640 ✓ byte-identical, hero 390 ✓ byte-identical (包括相同的 chip squish)
- **发现真实偏差**：sign-up 面板 406 vs 422 以及 forgot 面板 294 vs 310 —— 两者均比参考值**短了 16px**

让我来定位 sign-up/forgot 状态中缺失的 16px：
The reference sign-up structure has a `-mb-8px` back button trick. Now the clone's structure:
Both forms are 286px — the diff is in the heading/button spacing structure. Let me look at the clone's actual sign-up markup:
已找到根本原因：Tailwind v4 的 `space-y` 会输出 `margin-bottom` (`:where()` 零特异性) ——克隆的 `-mb-2` 覆盖了它，而不是像参考版本那样与其叠加。标题与按钮重叠了 8px，且容器缩短了 16px。让我验证一下忘记密码状态是否遵循相同的模式：
Confirmed — same 16px pattern in forgot. Also found: the reference's forgot container is `space-y-4 sm:space-y-6` (the clone lacks the sm variant). Let me check the v24 space-y trap mitigation precedent in globals.css:
The reference's forgot container also carries `sm:space-y-6`. Now let me check existing test pins for the auth state panels before designing the fix:
No existing panel-height pins for auth states (controls only + v49 F1's sign-in spacer). Let me check the v12 desktop panel geometry pins to be safe:
The v49 F1 pin only covers sign-in (unaffected by my fix). Let me check what the last commit added and study the verify-state container:
Now let me find the verify branch's container line:
Both containers located (line 603 verify, line 693 signup/forgot). Now writing the remediation plan v50:
Existing tablist pin is 1280-only. Now writing the remediation plan v50:
Now the TDD cycle — writing the F1 RED pin first (must fail against the current build):
The tsc errors are an artifact of single-file compilation (not the project config). Now running the F1 RED test — it must FAIL against the current (unfixed) build:
**F1 RED CONFIRMED** — both tests fail on the pre-fix build. Now applying the production fix:
Now the login-card.tsx class swaps:
The JSX comment placement is invalid (a `{/* */}` can't stand in a ternary arm before the element). Fixing:
Still failing after the fix — let me inspect the actual measured values:
Found it — my zeroing rule (0-2-0 specificity) kills the button's own `-mb-2` (0-1-0). Since the container no longer carries `space-y-4` at all, v4's emission never applies — the zeroing is both redundant and harmful. Removing it:
The wrapper/panel asserts PASSED (470/422 ✓) — only my stack finder is wrong (it matched an ancestor). Fixing the finder:
The forgot state's heading is wrapped in a div (not a direct h2 child). Updating the finder to accept both shapes:
**F1 GREEN ✓** — TDD cycle complete (RED → fix → GREEN). Now writing F2 (networth tablist 640 pin):
The shadow layer count assertion is wrong (splitting on `"),"` doesn't match the format). Fixing to count rgba occurrences:
6 layers vs my assumed 2 — the probe sliced the reference's shadow at 50 chars. Let me measure both full shadow strings:
The reference has 4 layers (shadow-sm family: 2 transparent leads + 2 visible). Let me get the clone's full shadow:
The session hit a load error. Reloading fresh:
The boot-failure state appeared — let me check the parity server log:
The browser interstitial is a network error — the running :3200 server was bootstrapped before my rebuilds swapped `.next/standalone` underneath it. Rebooting the server:
Both full shadows measured: **visible layers byte-identical** (shadow-sm pair `0.1 1px 3px` + `0.1 1px 2px -1px`); the clone carries 4 transparent leads vs the reference's 2 — the documented accepted lead-divergence class (v10/v25/v45/v49). Updating the F2 pin:
**F2 GREEN ✓**. Now writing F3 (dashboard hero mobile reflow pin at 390):
**F3 GREEN ✓** — all three v50 tests pass. Now the S1 mutation-sanity series. Mutation (a) — remove `zb-auth-mode` (back to `space-y-4`):
Mutation (a) bites ✓. Restoring and applying mutation (b) — remove the button's `-mb-2`:
Mutation (b) bites ✓ (478 — the panel +8 as predicted). Restoring and applying mutation (c) — remove `zb-sm6`:
Mutation (c) bites ✓ (16px vs 24px). Restoring and applying mutation (d) — remove the active tab bg:
All five mutations bite ✓. Restoring (e) and verifying the clean tree:
Clean diff — production changes only in globals.css + login-card.tsx. Now the full verification chain:
234/235 + one unexpected failure in not-found (metadata test — unrelated to my changes). Checking if it's flaky:
Flaky — passes standalone (7/7). Re-running the full suite for a clean 235/235:
**236/236 e2e ✓ (5.4m)** — F1 was two tests, so 232+4=236 (correcting the plan's count). Now smoke to complete the chain:
**Full chain GREEN: 108 unit · 236/236 e2e · 35 smoke.** Now the VLM pair on the fixed surface (login sign-up state at 390):
The smoke test's cleanup killed the :3200 server. Rebooting and capturing:
Both screenshots captured. Writing and running the VLM comparison:
VLM flags 4 diffs — per the v43 lesson, each must be DOM-verified. Checking the flagged geometry on both sites:
**DOM verdict: identical geometry on both sites** (y 187 / h 422 / button 294@x48) — all VLM flags are the noise family (the documented shadow lead-divergence perception + rendering AA). Now regenerating the 16 screenshots:
All 16 screenshots regenerated (7 with byte diffs from the fix). Now the D1–D8 docs alignment. First correcting the plan's test count (F1 = 2 tests → 236):
Now D7 — the formal session log. Let me check the session_113 format:
Now session_117.md (the raw transcript):
Now the repo worklog — Session 84 entry + ledger list:
No stale counts. Now D8 — the workspace worklog:
All docs aligned. Final verification before commit:
All files staged-ready. Now reading the SSH wrapper instructions before the push:
Now committing and pushing via the SSH wrapper. First the commit:
Paramiko ready. Deploying the SSH shim outside the repo and materializing the key:
密钥已验证 (ed25519)。正在使用详细的 v50 消息提交迭代：
The remote has moved ahead — the dry-run's push was rejected as non-fast-forward. Fetching to see what's new:
Remote is at 3f0202e (our base — no divergence) yet the dry-run failed. Let me inspect the wrapper's dry-run behavior:
Found it — the wrapper defaults to the task-management remote. Re-running with the explicit zero-balance remote:
Dry-run clean (3f0202e..f807aac fast-forward). Executing the real push:
**Push verified — remote main @ f807aac == local HEAD.** Destroying the operator key and final verification:
All verification complete — the wrapper's post-push check confirmed remote main @ f807aac == local HEAD (the authoritative verification; the public API call hit an unrelated rate limit). Closing out:
**Parity iteration v50 已交付并推送到 main**（`f807aac` — wrapper 验证了远端引用 == 本地 HEAD，密钥已销毁，工作区干净）。

## 本次会话核心成果

**发现并修复了一个真实差距（v46 以来第二个生产代码变更）**：克隆站的注册/忘记密码面板在所有视口都比参考站矮 16px — 根因是 Tailwind v4 的 `space-y` 零特异性 `margin-block-end` 与返回按钮自带的 `-mb-2` 冲突（覆盖了容器间距而非像 v3 那样叠加）。修复采用作用域 `.zb-auth-mode` 还原（v3 语义家族第三成员）+ 忘记密码的 `.zb-sm6` sm 档（24px @≥640）。首个修复方案（带零化规则）被 pin 当场抓出（量得 430 而非 422）— TDD 红绿循环的价值实证。

**交付**：44 次常设检查全清（4 个参考站 bug 仍在线 = 超集完好）、**108 unit / 236 e2e / 35 smoke 全绿**、5 个突变全部验证咬合、VLM 4 个旗标全部 DOM 溯源为噪声、16 张截图重生成、全链文档对齐（session_116/117、worklog Session 84、PAD v1.1.7、SKILL Session 85 行）。

**v51 队列建议**：验证邮箱状态的完整面板普查（需参考站注册授权豁免）、忘记密码确认状态 390 普查、hero 统计卡行 390 重排、储蓄视图目标卡移动端普查 — 随时吩咐。
