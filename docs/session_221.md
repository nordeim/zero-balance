我将开始执行 zero-balance 仓库的「审计 → 对齐 → 修复 → 推送」完整工作流。先建立任务清单，然后刷新工作区。
工作区已被重置，需要重新克隆仓库：
仓库已克隆，处于 main 分支，最新 commit 是 v90 迭代（session_218）。现在审阅仓库结构与核心文档：
仓库包含 session_219.md 与 remediation-plan-v90.md。现在审阅核心文档（这些文档很大，先看头部与最新章节）：
文档很大。先读取最新的 session_219.md 和 remediation-plan-v90.md 了解当前状态与下一步队列：
session_219.md 记录了 v90 周期已完成并推送。当前任务即执行 **v91 周期**。现在读取 remediation-plan-v90.md 了解计划结构与 v91 队列：
现在读取 probe README 的 v90 章节（包含权威的 v91 队列）与 worklog 最新条目：
v91 队列已明确：**v85-era ITEMS pair（income + expenses 桌面 1280 视图对）第 5 次重跑 [v57→v64→v70→v79→v85→v91]** + axe watch + 新 pin。现在读取 CLAUDE.md 与 worklog 最新条目：
CLAUDE.md 已与 v90 状态对齐（293 e2e）。现在读取 worklog.md 最新条目与 AGENTS.md 的 v90 段落：
worklog 确认 v91 目标。按「队列散文验证规则」，先对照 v85 探针脚本验证轮换台账的真实表面：
v85 探针脚本证实：**ITEMS pair = income + expenses 桌面 1280x800 全页**，与队列一致，v91 将是第 5 次重跑。现在查看 v85 系列的其余探针文件与 AGENTS.md 尾部：
现在查看技能目录，随后开始环境配置（耗时长，先启动）：
现在查看 SSH wrapper 使用说明与 package.json 脚本：
工作区状态清晰。现在按 v86/v88/v90 的「fresh-clone 重配置清单」开始环境配置。先启动 npm ci（耗时较长）：
354 包安装完成，5 个已知 dev-only braces 审计项与文档一致。现在写 .env、初始化数据库、检查 chromium 与 paramiko shim：
**Seedcheck 精确匹配**：7 items / rent 1850 / 0 lineItems / 3 assets / 2 liabilities。现在安装 chromium-1243 与 paramiko：
无 ssh 二进制 → 按运行手册部署 paramiko shim 到仓库外 `/home/z/my-project/bin/ssh`：
环境配置完成。更新任务清单并开始审计阶段——先验证 v90 commit 的 PIN-ONLY 声明：
**v90 commit 验证为 PIN-ONLY**（17 文件，+1429/-13，零 src/ 变更）；其后仅一个 session-log commit。现在审计生产接缝：
生产接缝审计全部通过。现在执行 **F0 基线链**——lint、typecheck、单元测试：
构建成功（robots + sitemap 已预渲染）。现在分块运行 e2e 套件——先看 playwright 配置与分块方案：
23 个 spec 文件。统计每个文件的测试数以规划三块分片：
总计 293 测试（292 chromium + 1 setup）与文档一致。检查 global-setup 后按三块运行：
需要精确的每文件 chromium 测试数。用正确的 project 过滤重新统计：
292 个 chromium 测试确认。规划三块分片（126+105+61=292）。先检查无残留服务器，然后运行块 1：
三块全绿：127+106+62 = 295 次执行 = 293 个唯一测试，零抖动。运行 smoke 测试：
**F0 基线链全绿**。现在 **F1 axe-core watch**：
**F1 无偏差** (4.14.0 稳定版，v68 去重保持，engine pin 通过)。现在 **F2 第 85 次常设检查** —— 从 v84 对派生。先检查 v84 脚本的 token 家族：
v85 常设检查对已派生（仅版本号变更验证通过）。查看 clone 侧脚本的运行要求：
agent-browser 可用。先运行参考侧常设检查（只读规则）：
参考侧全部符合预期：四个 bug 全部存活、数据普查零漂移、SEO 对在线。现在运行 clone 侧：
**F2 全绿——移动端菜单已验证工作正常（连续第 85 次）**。现在进入 **F3 v91 重跑对**。先研究 v85 系列的 token 家族：
会话命名各代不同（v85 用 `refarbv85`，v90 用 `refarbit90`）。先看 v85 四个核心文件的头部以规划历史修正：
现在执行 v91 探针系列的 sed 派生。先检查 v85 文件正文中是否有需要保留的历史引用：
Token 普查完成。执行 v91 系列的 sed 派生（会话名替换先于裸 v85 版本替换）：
现在进行头部历史修正（重新运行括号 + 最后重拍 + 序数词）：
现在验证功能正文仅版本号变更——反向规范化后 diff：
差异仅限于有意的历史修正头部行——功能正文仅版本号变更。检查残留 token：
残留的 "85" 均为合法（历史括号 + 参考 URL 中的应用 ID）。现在执行 **F3 参考侧截图**：
参考侧截图完成（首次尝试登录成功）。现在运行克隆侧截图：
两个判定均为不同——与 v85 周期一致。现在查 v85 计划的仲裁记录对照旗标类别：
v91 旗标与 v85 记录的类别完全对应（含 FAB 的 VLM 归因交换现象——v85 已用两步仲裁证伪）。现在运行双侧 census（v75 惯例：无论判定如何都运行）：
组合 census 超时（70 个僵尸 chromium 进程——v89 文档记录的资源耗尽现象）。按 v89 教训先收割进程，再按「两半受控 census 形式」拆分：
进程已收割。创建两半受控 census（census JS 必须逐字节一致）：
参考侧半体运行干净。但 census JS 的 md5 不一致——需要排查（census JS 一致性是两半形式的合同）：
Census JS 合同成立（前 215 行逐字节一致）。运行 clone 侧半体：
**Census 完全复现 v85 值——每个轴零漂移**。VLM 旗标全部对应已记录类别。还剩 FAB 旗标需要 DOM 仲裁（v43 规则）。查看 v85 的 FAB 仲裁工具：
**FAB 仲裁决定性**：双侧 DOM 均为 `fabCount:0`——FAB 属参考站平台 chrome（v85 已记录的归因交换类别）。**F3 完成：无新差距，仅限锁定。**

现在进入 **F4——寻找本周期表面的从未锁定轴**。检查 items.spec.ts 的现有 1280 pin 覆盖：
检查 v64/v70 filter-card pin 与 v57 footer pin 的具体轴，寻找从未被 pin 的家族：
Grid 模板已 pin。继续寻找 1280 下从未被 pin 的内部家族——检查 v65 页头 pin 与 v57 footer 子项断言的轴：
查看 v85 F4 与 v74 F4 pin 的精确轴，锁定从未覆盖的内部家族：
v37 只 pin 了 focus 态。**从未被 pin 的轴已锁定：filter-card 交互内部——combobox trigger 的静态 chrome（pad/justify/bg/radius/chevron 图标）与 search 输入框的排版（fs/lh/color）**。先看 arbit-v91 census 的 finder 方式以复用：
现在编写补充性一次性双侧 census（两半受控形式）测量 pin 自身轴。先写参考半体：
验证方式有缺陷（sed 报错导致空比较）。改用行号提取验证：
Census JS 块逐字节一致（md5 相同）。重试参考半体（延长超时）：
参考半体干净完成。运行 clone 半体：
**Pin 自身轴双侧逐字节一致（零差异，含 placeholder 文本）**。现在检查 pin 目标的源码位置以设计突变：
搜索框为共享 `Input` 组件 + 视图局部 `pl-10` 类。突变目标定为 **items-view.tsx:188 的 `lg:font-medium` 视口作用域闪避**（fw 轴——几何惰性，v90 先例）。先按「速记-token grep 教训」全面验证覆盖图：
**覆盖图验证完成**：搜索框的 fw 在任何视口都从未被 pin（所有 Fw 速记键属于其他元素），无碰撞可能。突变设计确定为 `pl-10` → `pl-10 lg:font-medium`（items-view.tsx:188，视口作用域闪避）。

按规定的顺序——**先写计划再执行**。撰写 remediation-plan-v91.md：
计划已保存。现在执行 **F4——追加 v91 pin** 到 items.spec.ts。先看文件尾部结构：
现在追加 v91 pin 到 items.spec.ts 尾部：
**v91 pin 首次运行即通过（GREEN）**。现在执行 pin 完整性突变（第 188 行，按行号）：
突变下构建不完整——我只运行了 `next build` 而非完整 `npm run build`（缺少静态文件拷贝步骤，v88/v90 教训：standalone 重建须用完整脚本）。补全构建后重跑：
**突变验证精确命中**——失败 diff 仅为 fw 轴（400→500）。现在突变下运行完整 items.spec.ts 验证无级联：
**无级联验证通过**（39 绿，仅 v91 pin 红）。恢复源码并完整重建：
**F4 完成**（pin 首跑绿、突变单轴命中、无级联、恢复后 40/40 绿）。现在 **F5 全链重跑**：
**F5 全链绿**（294 唯一 e2e + 35 冒烟测试）。现在进行截图再生成与字节比对：
截图脚本用自己的 ：3100 服务器与已播种的 db/custom.db。运行再生成并字节比对：
**16/16 字节相同**——同日种子字节恒等律再次成立。最终 seedcheck 与树状态检查：
**最终 seedcheck 精确、树状态仅限锁定（PIN-ONLY）（零 src/ 变更）**。开始 D1–D7 文档对齐。先看 AGENTS.md 的 v90 段落位置：
D2 完成。现在 D3：README 计数与计划表行：
D3 完成。现在 D4：SKILL 文档 Session 126 行与状态行：
D4 完成。现在 D5：PAD v1.1.48 修订块：
D5 完成。D6 前先按台账验证 v92 队列（探针谱系权威原则）：
v92 队列已验证（v86-era savings pair 第 5 次重跑）。现在 D6：probe README 的 v91 段落：
D6 完成。现在 D7：session_220.md 会话叙述：
接下来是 worklog Session 126 条目（最新优先，插在 Session 125 之前）：
D1–D7 全部完成。现在执行预发布检查：
预发布检查全部通过（PIN-ONLY、env.example 已跟踪且准确、孤儿目录均被 gitignore）。更新共享工作区 worklog：
现在创建 parity commit：
**Parity commit `c794a7c` 已创建**（21 文件，+2161/-6，零 src/ 变更）。现在部署 SSH 密钥并通过 wrapper 推送：
试运行（Dry-run）干净（fast-forward 07586b7..c794a7c）。执行正式推送：
**v91 周期已完成并推送** ✅（main @ `c794a7c`，21 文件 +2161/-6，零 src/ 变更）

**本周期成果**：
- **基线首跑全绿**：108 单元 → **294 e2e**（+1）→ 35/35 冒烟测试；环境按 fresh-clone 清单完全重建，seedcheck 精确
- **第 85 次常设检查全绿**——移动端菜单连续第 85 次验证工作正常（Tailwind v4 缓解措施持续有效）；参考站四个 bug 仍存活；数据普查第 85 次零漂移
- **无新克隆差距**：双侧 census 完全复现 v85 值；复现的 FAB 归因交换旗标经一次性 DOM 仲裁证伪（双侧 fabCount 0）；组合脚本资源耗尽后按 v89 教训改用两半受控 census
- **新 pin**：filter-card 交互内部（搜索框排版 + 每个 trigger 静态 chrome——任何视口都从未被 pin），突变验证单轴命中（fw 400→500，39 绿仅 1 红）
- **交付物**：`docs/remediation-plan-v91.md`（已验证计划）、`docs/session_220.md`、10 个新探针脚本、16/16 字节相同截图、`.env.example` 已跟踪且准确、七处文档对齐（D1–D7）
- **已通过 SSH wrapper 推送并验证**：remote main == local HEAD，操作密钥已销毁

**下一步建议**：按轮换台账，v92 周期目标为 **v86-era savings pair**（桌面 1280 储蓄视图，第 5 次重跑 [v58→v65→v74→v80→v86→v92]）——执行前先对照 `vlm-shots-v86.sh` 验证台账。可以直接说「继续 v92」开始下一周期，或提出对本周期交付物的调整意见。
