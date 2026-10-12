我将按照操作指令继续执行 zero-balance 项目的任务。文档版本已更新为 session_126、remediation-plan-v53、session_127。让我先建立任务清单，然后开始刷新工作区。
现在开始第一步：刷新工作区。
工作区状态异常（无 origin remote）。让我检查目录结构：
`zero-balance` 目录为空——工作区已被重置，需要重新 clone：
Clone 成功。确认最新文档与提交状态：
工作区已刷新，最新提交为 parity iteration v53。仓库已包含 vitest.config.ts、playwright.config.ts、tests/、.env.example、worklog.md。现在审阅核心文档（这些文件很大，采用头部+尾部+关键段落策略）：
AGENTS.md 已审阅。现在读取最新的会话文档（session_126、remediation-plan-v53、session_127）：
现在读取 session_127.md（最新会话文档，包含下一个工作队列）：
session_127.md 记录了 v53 交付过程。让我检查最新提交内容、session_125.md 中的 v54 队列以及 worklog 尾部：
v54 队列已明确。现在检查 worklog 尾部与技能目录：
核心文档审阅完成。现在验证代码库当前状态——检查 package.json、探针脚本、.env.example：
仓库探针基础设施完备。现在配置环境（npm install + .env + db）：
环境就绪（db/custom.db 位于仓库根，种子已填充）。现在运行基线验证链：
Lint ✓ · Typecheck ✓ · 108/108 单元测试 ✓。现在构建：
构建成功（sitemap.xml 与 robots.txt 已预渲染）。检查孤儿服务器后运行 e2e：
Playwright 配置确认无孤儿服务器。运行完整 e2e 套件（246 目标，参考 v53 经验用分块方式防超时）：
输出异常（仅 1 passed）。让我检查测试列表并重新分块运行：
247 个测试确认。按 v53 经验分两块有序运行：
输出仍异常。让我查看完整输出诊断：
输出很奇怪——只显示 1 passed 但列出了很多测试。让我捕获完整输出：
根因找到：Playwright 浏览器可执行文件缺失（fresh clone 环境）。安装 Chromium：
Chromium 已安装。重新运行 e2e 验证修复：
22/22 通过——浏览器问题已解决。现在分两块运行完整 e2e 套件：
**e2e 全绿：140 + 108 = 248 通过（247 chromium + setup），零失败**。现在运行 smoke 测试完成基线链：
**基线链完全通过——v53 状态确认**。现在执行第 48 次常置检查。先读取常置检查脚本：
执行 v53 经验的预清理（pkill + 会话文件清扫），然后运行参考站常置检查：
参考站检查全部确认——4 个参考 bug 依然存在（克隆超集保留）、数据完好、SEO 在线。现在运行克隆站检查：
**第 48 次常置检查全部通过——克隆站移动端导航菜单验证正常工作**（R1 burger 命中 + sheet 打开、R2 导航关闭、R3 nav landmark、R4 全视图零溢出 390 vs 参考站 464）。

现在进行代码审计（trap-log 扫描 + 近期变更审查）：
Trap-log 扫描结果：仅 2 处 `-mb-2`（均为 auth 返回按钮）。验证它们位于已转换的 `zb-auth-mode` 容器内：
Trap-log 扫描清洁——两处 `-mb-2` 均在已转换容器内。现在审查 SEO 实现、移动端导航与 v54 候选表面的覆盖情况：
查看 savings 视图的目标卡内部结构（item-card）：
item-card 结构清晰。v51 pin 覆盖卡片外框 chrome，**未覆盖内部：badge 芯片行 + 日期/支付方式 footer**。这正是 v54 队列的第一个候选。先研究 v53 探针模式：
研究 v52 pin 对卡片内部结构的覆盖情况，确定 v54 精确缺口：
检查 badge-colors.spec.ts 已覆盖的内容，确定 v54 缺口边界：
badge 颜色已 pin（badge-colors.spec.ts），但 **badge 几何结构（h/radius/pad/fs/fw/图标）与 footer 未覆盖**——v54 缺口确认。检查克隆种子数据后编写 v54 探针：
种子确认：Emergency Fund（4 chips）。现在编写 v54 探针脚本（参考站只读普查）：
参考站普查返回，但 footer 部分可疑（fs 16px / 空文本 paySpan / h 48——可能匹配到错误元素）。让我转储参考站卡片的实际 DOM 结构：
参考站卡片结构清晰（footer 仅含日期 + 日历图标）。让我精确转储 footer 的内部 HTML 以解释普查异常：
找到了首次普查异常的根因：footer 过滤器误匹配了 header 行（同样有 justify-between + svg）。修正两个探针的 footer 定位器（取无 h4 的最后一个 justify-between 行）：
参考站普查修正完成。现在运行克隆站普查：
**v54 普查结果：字节级对等——纯 PIN（无生产差距）**。所有差异均为已记录的数据类别（种子数据 vs 参考站数据）。验证 pin 目标源码行后编写修复计划：
所有验证数据确认。现在编写 remediation-plan-v54.md：
修复计划已保存。现在进行 TDD 执行——编写 F1 pin。先检查 items.spec.ts 结构以正确追加：
现在追加 v54 F1 pin 到 items.spec.ts：
追加 v54 F1 pin（与探针普查完全一致的 censure）：
F1 pin 已写入。类型检查后运行测试（pin-only 应立即通过）：
F1 失败——查看详细错误：
census 返回 null。检查 e2e 种子数据的 savings 项目名称（e2e seed 可能与 dev seed 不同）：
e2e 种子相同（Emergency Fund 存在）。用 with-server 逐步调试 census 逻辑找出失败步骤：
**根因找到**：badge 行的子元素计算样式为 `flex` 而非 `inline-flex`（flex 容器的子项被块化——CSS 规范行为）。探针脚本用 OR 子句正是为此。修正测试查找器：
重跑 F1 pin：
**F1 GREEN**。现在执行 S1 突变验证系列（每次突变：改代码 → 单独重建 → 单独运行测试 → 验证失败 → 还原）。突变 (a)：badge 行 gap-2 → gap-4：
**突变 (a) 咬合 ✓**（gap 8→16）。还原并应用突变 (b)：分类 chip 的 px-2.5 → px-1.5：
**突变 (b) 咬合 ✓**（pad 2px 10px→2px 6px）。还原并应用突变 (c)：chip 的 text-xs → text-sm：
**突变 (c) 咬合 ✓**（fs 12→14 使 chip 高 22→26）。还原并应用突变 (d)：footer 的 text-xs → text-sm：
**突变 (d) 咬合 ✓**。还原并应用突变 (e)：date span 的 gap-1 → gap-2：
**全部 5 个突变验证咬合 ✓**。还原 (e)、干净重建、验证 GREEN：
干净 diff 确认：仅 spec 文件 + 新文档/探针，零生产代码变更。验证 F1 GREEN：
F1 GREEN。现在执行 F2 VLM 配对——先研究 v53 的 VLM 模式：
编写 v54 VLM 脚本（networth tablist + savings 目标卡两对截图）：
VLM 标记了若干差异。按 v43 规则，所有 flag 必须 DOM 溯源验证。PAIR 2 的 flags 全部为已知数据类。PAIR 1 有 3 个需要 DOM 验证：趋势图标重叠、active tab 背景、Add 按钮截断：
参考站会话已过期。重新登录后验证：
Active tab 背景 DOM 验证：**rgb(220, 252, 231) 与克隆完全一致**（VLM 的“更亮”是截图伪影）；Add 按钮 **"Add Asset" 完整无截断**（scrollW 134 = clientW 134，VLM 误读）。趋势图标配对需进一步普查——搜索参考站 summary 区域的所有 svg：
参考站 summary 带 ±120px 内**无任何 svg**。转储 summary 卡完整结构以定位 VLM 所见的“趋势图标”：
参考站金额卡内无 svg。检查克隆站同一家族与参考站页面顶部区域：
找到了 VLM 所指的“趋势图标”：参考站 32×32 trending-up 位于 x 368（越过 390 视口右缘——参考站自身 464 溢出 bug 的一部分）。验证克隆站同一家族：
**VLM 配对判定：CLEAN（按 v43 规则）**——3 个待验证 flag 全部 DOM 溯源为噪声（tab bg 字节一致 rgb(220,252,231)、Add 按钮双站完整无截断、趋势图标为已记录的 464-溢出宽度类分歧）。

现在运行全链验证（lint + typecheck + unit + e2e 两块 + smoke）：
**全链绿：141 + 108 = 249 e2e（248 chromium 等效，零失败）+ 35 smoke**。重生成 16 张截图：
截图零字节差异（pin-only 不变量保持）。.env.example 已验证匹配（本会话用它创建 .env 且全链通过）。现在执行文档对齐 D1-D8——先定位计数位点：
逐一定位精确更新位点（README 测试计数与 v53 行、各文档状态行）：
文档对齐开始。D3——README 计数更新（247→248）+ v54 行：
现在向 README 对等表添加 v54 行：
D3 完成。D2——CLAUDE.md 更新：
D2——更新 CLAUDE.md 计数与 items 覆盖扩展：
D1——AGENTS.md 添加 v54 段落：
在 v53 段落后插入 v54 段落（升序排列）：
D4——SKILL 文档（Session 89 行 + 状态行）：
D4——SKILL 文档更新（Session 89 行 + 状态行 247→248）：
D5——PAD v1.1.11 修订块：
D6——探针 README 添加 v54 节：
D7——创建 session_128.md（正式日志）。先查看 session_125 的格式：
编写 session_128.md 正式日志：
编写 session_129.md（原始转录）：
更新仓库 worklog（Session 88 条目 + 台账列表）：
验证 worklog 台账编辑的正确性：
修整台账语法：
D8——工作区 worklog 更新：
追加工作区 worklog 的 v54 条目：
所有文档对齐完成。现在准备交付——检查 git 状态并阅读 SSH wrapper 指令：
干净 pin-only diff 确认（350 插入，零生产代码变更）。现在阅读 SSH wrapper 使用指令：
环境无 OpenSSH 二进制，工作区 bin/ 有 shim（paramiko ssh），但 paramiko 未安装（新环境）。安装并验证 shim：
pip 被 PEP 668 阻止。用 --break-system-packages 安装：
paramiko 已装。验证 shim 可执行性，然后提交代码：
Shim 工作正常。现在提交（Conventional Commits 风格）：
提交 `efe6a0f` 完成，工作树干净。现在部署 SSH 密钥并 dry-run：
Dry-run 通过（认证成功，fast-forward 664cfd7..efe6a0f）。执行真实推送：
推送验证成功——远端 main @ `efe6a0f` == 本地 HEAD，密钥已销毁。最后验证 skills/ 排除配置：
skills/ 已在 eslint ignores 与 tsconfig exclude 中确认排除。任务全部完成：
**Parity iteration v54 已交付并推送到 main**（`efe6a0f` — 远端 == 本地，密钥已销毁）。

**本次会话核心成果**：

- **v54 普查（PIN-ONLY，零生产代码变更——连续第三次 pin-only 迭代）**：savings 目标卡的 **badge 芯片行 + 日期/支付 footer 内部结构**在 390 视口下双站字节级对等（"monthly" chip 双站同为 w 78、"active" chip 同为 w 63——同文本同 chrome 同宽度的最强对等证据）；点色按 TYPE 而非 classification（参考站语义已记录）
- **1 个新增 e2e pin**（247→248），5 个突变全部验证咬合
- **移动端导航菜单已验证正常工作**（R1 burger 命中 + 5 链接 sheet、R2 导航关闭、R4 全视图零溢出 390 vs 参考站 464）；Tailwind v4 trap-log 扫描清洁；SEO/sitemap 双站在线
- **VLM 配对 CLEAN**：3 个待验证 flag 全部 DOM 溯源（tab bg 字节一致、Add 按钮无截断、趋势图标为已记录溢出类）
- **新探针经验**（已记入 probe README）：justify-between footer 定位器须排除 header 行；chip 的 inline-flex 源类计算为 flex（CSS 块化）
- **全链绿**：108 unit / 248 e2e（两段有序执行）/ 35 smoke / lint / typecheck / build

**下一步建议**：v55 队列已写入 session_128（参考站 verify/forgot-confirm/计算器空态普查需写授权，仍延迟），或继续 badge 图标字形普查、计算器 with-row VLM 配对——随时吩咐。
