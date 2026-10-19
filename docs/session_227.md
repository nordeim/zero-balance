我将开始对 zero-balance 仓库执行完整的审计→对齐→修复→推送工作流。首先检查工作区状态并刷新代码库。
工作区已存在 zero-balance 仓库。现在执行 `git pull` 刷新工作区：
`git pull` 成功，更新到最新 commit（包含新增的 `docs/session_225.md`）。现在查看最近提交记录并审阅核心文档：
`git pull` 完成（fast-forward 到 `13e1445`，新增 `docs/session_225.md`）。现在制定任务计划并审阅核心文档：
核心文档内容较大（长行）。让我读取持久化输出的关键部分：
现在审阅最新会话文档（session_224、session_225、remediation-plan-v93）与最新 worklog 条目：
v93 周期已完成推送，本会话任务明确为 **v94 parity 周期**（v88 时代的 networth + drill-down 组合第五次重跑）。继续审阅 remediation-plan-v93 与 worklog 最新条目：
v93 计划模式已完全掌握。现在查看 worklog 最新条目（Session 128）并验证环境状态：
worklog 结构清晰（Session 128 = v93，本周期 v94 = Session 129）。现在验证 v94 队列与 v88 探针系列、环境状态：
v88 探针头部确认 v94 队列：**NETWORTH 视图 + DASHBOARD drill-down EXPANDED 状态**（桌面 1280×800 全页，第五次重跑 [v60→v67→v76→v82→v88→v94]）。现在验证环境状态：
环境完好（.env 正确、db/ 在根目录、shim 就绪、chromium-1243、355 包）。拉取的增量仅为 session-log-only（`docs/session_225.md`，零 src/ 变更），无需重新配置。现在查看 skills 目录目录与 seedcheck 方法：
skills 目录已审阅（将使用 agent-browser、tdd、evidence-driven-testing、how-to-git-push-using-ssh-wrapper 等技能）。现在进入 **F0 基线链** — 先运行 seedcheck：
**Seedcheck 精确匹配**（7 items / rent 1850 / expensesTotal 2235 / 0 line items / 3 assets / 2 liabilities）。启动基线链 — lint 与 typecheck：
lint ✓ · typecheck ✓。运行 108 个单元测试：
108/108 单元测试 ✓。运行生产构建：
构建 ✓（SEO 对 robots.txt + sitemap.xml 均已预渲染）。现在规划 e2e 分块执行：
23 个 spec 文件。统计各文件测试数以规划三块分片（v93 记录：105+112+80=297 次执行=296 唯一）：
规划三块分片并执行第一块（重规格）：
第一块 111 通过（110 chromium + 1 setup）。执行第二块：
**F0 基线链全绿**：lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓（SEO 对预渲染）· **296 e2e ✓**（111+105+82=298 次执行=296 唯一，零抖动）。运行 35 步 API smoke 测试：
**F0 完成**（35/35 smoke ✓）。进入 **F1 axe-core watch**：
npm-latest 为 4.14.0（其后仅 sha 预发布）— 无漂移。用文件读取方式验证已安装版本：
**F1 axe-core watch: 无漂移 (NO DRIFT)** ✓（wrapper/engine/npm-latest 均为 4.14.0，去重 (dedupe) 状态保持，合约 `pin` 2 个测试通过）。进入 **F2 第 88 次 `standing checks`** — 从 v87 对派生：
派生 v88 standing-checks 对（三个 token 族替换）：
派生验证通过（version-bump-only 干净）。先检查僵尸进程（reaping 纪律），然后执行参考侧（只读纪律）：
存在一个 54 分钟前启动的 agent-browser 守护进程（约 14 个 chrome 进程）。按 reaping 纪律先清理（使用字符类模式避免自匹配）：
Reaping 完成（0 残留进程）。执行参考侧 standing check（只读纪律）：
参考侧 ✓ — 四个 bug 全部存活（toast-blocker / sheet-trap / no-landmark / 464px overflow），数据 census 第 88 次零漂移，SEO 对存活。执行克隆侧：
**F2 全绿** — 移动端菜单第 88 次连续验证工作正常。进入 **F3 v94 重跑组合**。先检查 v88 探针系列结构：
v88 探针系列已完全理解。查看 v93 的两半构建器模式（v94 需从一开始就构建两半形式）：
理解两半构建器模式。先查看 v93 派生系列的头部修正形式（v94 头部修正的参照）：
查看探针 README 的 v93 章节中的 v94 队列建议（验证队列散文）：
v94 队列已确认（与轮换账本一致）。执行 sed 派生（token 族：vlm88→vlm94、v88→v94、FOURTH→FIFTH、ELEVENTH→SEVENTEENTH）：
派生完成，语法全部通过。现在检查各文件头部以应用历史修正：
编写幂等的头部历史修正脚本（Python 多行精确替换）：
头部修正完成。执行 normalize-back 验证（功能性代码体必须为 version-bump-only）：
Normalize-back 验证通过 — 所有差异仅限头部历史修正注释行，功能性代码体为 version-bump-only。检查残留 token：
残留 token 全部为合法历史引用。验证执行层 session 名称已正确重命名：
修正 arbit-v94.sh 中漏掉的 session 名称（refar88/clonear88 → refar94/clonear94）：
Session 名称修正完成。现在构建两半 census 形式（v93 教训：从一开始就两半）。先定位 census JS 块的行边界：
查看 v93 两半脚本的最终形式（v94 构建器的参照）：
理解两半形式结构。编写 build-twohalf-v94.py（提取 census JS 块一次、两半字节一致嵌入）：
两半 census 构建完成（md5 契约验证：ARBIT_A 90 行 a9cdcc96 / ARBIT_B 111 行 baa22974，两半字节一致）。执行参考侧截图（只读纪律）：
参考侧截图完成（首次尝试登录成功，两个表面均已捕获）。执行 halves 间 reaping（固定步骤），然后克隆侧截图：
克隆侧截图完成（fixture 无需恢复 — drill-down 仅视图状态点击，无数据变更）。执行 VLM 成对比对：
**VLM 裁决：两对均为 DIFFERENT**，多个 flag 需要 DOM 仲裁。其中两个 flag 涉及 v88 pin 的主题区域（stat-card count-row + divider）与 "Total Expense(s)" 文本 — 需要仔细核查。先查看 v88 pin 内容与相关源码：
v88 pin 上下文确认：v88 周期 VLM 同样误读了 divider（both-sides census 证明字节一致）。检查 v88 计划中记录的 flag 类别与 "Total Expense" 文本轴是否曾被记录：
v88 计划第 79 行提到 "stat-title misread" — 正是本周期 "Total Expense(s)" flag 的文档化类。读取完整上下文：
v88 记录确认了本周期所有 flag 的文档化类。查找 v82 的 "stat-title misread" 原始记录（"Total Expense(s)" 类的源头）：
**所有 VLM flag 已映射到文档化类**：
- Pair 1: avatar 用户身份类 / FAB 平台 chrome 类（v85/v91）/ 数据 figures 种子数据类
- Pair 2: Dashboard 高亮 = v56 SUPERSET 类 / 进度条 = pct×568 DATA 类 / donut 标签 = v60 PERCEPTION 类 / "Total Expense(s)" = v82 误读类 / divider = v88 误读类 / 其余 = 种子数据类

执行两半 census 进行 DOM 仲裁 — 先参考半：
参考半 census 完成 — 所有轴值与 v88 记录精确一致（navHighlight INERT / avatar U / fillW 173 / donutLabels count 4 / 卡族全匹配）。执行 halves 间 reaping，然后克隆半：
克隆半 census 完成（seedcheck 精确）。**逐轴比对：census 精确复现 v88 记录值 — 每轴零漂移**：
- navHighlight：clone ACTIVE white/500 vs ref INERT（v56 SUPERSET 类）✓
- avatarLetter：D vs U（用户身份类）✓
- progress：fillW 357 vs 173（track 568×12 字节一致，pct DATA 类 — v82/v88 记录值精确复现）✓
- donutLabels：count 4 / labelLineCount 0 / 16px / black / sectors 3 字节一致（v60 PERCEPTION 类，texts 各自数据）✓
- statTrendIcons/heroTrendGlyphs/statCardCount：字节一致 ✓
- PART B 卡族：960×333/32px/16px/渐变/阴影、headRow 76/32、label 14px、figure 48px/700、medallion 64×64、statGrid 440×2/84/16/896、statTile、ratioFooter 全部字节一致；labelBlock w 357-vs-304 为 v82 DATA-CONDITIONAL 宽度类 ✓

现在对两个误读类 flag（stat-title + divider）执行 live 复核 — 运行 v88 一次性双侧 census：
两个误读 flag 均被 live 复核推翻：
- **Stat titles**：两侧逐字均为 "Total Income"/"Total Savings"/"Total Expenses"（复数）— v82 误读类复现，标题字节一致 ✓
- **Divider**：两侧每张卡均为 {DIV, h 1, bg rgb(229,231,227), flexGrow 1} — v88 误读类复现，字节一致（宽 177-vs-170 为 flex-1 数据条件余量类）✓

再复核 FAB flag（v85/v91 文档化平台 chrome 类）：
**F3 完成：无新克隆差距** — 每个 VLM flag 均被 DOM 仲裁到文档化类（FAB live 复核：两侧 fabCount 0）。v94 迭代至目前为止仅涉及 PIN。

进入 **F4 — v94 pin 调查**。调查 networth + drill-down 表面的现有 pin 覆盖，寻找未固定轴：
调查 v56 hero census 与 v88 pin 的具体轴覆盖，寻找未固定族：
v69 pin 覆盖 PAGE-header（390）。**SECTION-header 族（"Assets" h2 + 计数副标题）仅有文本可见性断言，无计算样式 pin**。检查源码结构：
**v94 pin 候选确认：networth 视图的 SECTION-HEADER + GROUP-HEADER 行族 @1280**。执行覆盖图 grep 验证（任何视口均未固定）：
v60 pin 已覆盖 group header（18px/600/capitalize/mb12）。读取 v60 F1 pin 的完整轴覆盖，并检查 section-header 行族是否在其中：
**覆盖图确认：SECTION-HEADER 行族在任何视口均从未固定**（h2 "Assets" 排版 / 计数副标题 P / 行 flex chrome / Add Asset 按钮在此行的 chrome）。检查 zb-btn-add 家族的既有 pin 与源码行号：
tokens.spec 的 zb-btn-add pin 仅覆盖默认视口的 16px Plus 图标。**v94 pin 设计确定：networth 视图 SECTION-HEADER 行族 @1280**（h2 排版 / 计数 P / 行 flex / Add 按钮 chrome / 节奏 — 全部任何视口从未固定）。执行执行前验证（mutation 目标行 + 覆盖图 grep + lg:font-black 唯一性）：
验证通过（lg:font-black 不存在于 src/；"Assets" 断言均为 tab role 或可见性 — fw 翻转下全绿）。构建补充两半 census（v93 totalcard 先例形式）：
编写 v94 补充两半 census（networth SECTION-HEADER 族）— 用 Python 生成器保证 census JS 字节一致：
Census 块结束引号处理有误（raw 字符串中 `\"` 写入了字面反斜杠）。修正生成器：
census JS 字节一致（md5 f8b3cabf，43 行）。验证文件内容正确性后执行参考半：
参考半 census 完成。Reaping 后执行克隆半：
克隆半报错 — with-server heredoc 是引用形式，子 bash 未继承 CENSUS_JS 变量。修正生成器添加 env-injection（v88 惯例）：
with-server 通过 `"$@"` 继承环境变量。重建并重跑克隆半：
**补充 census 完成 — pin 自身轴两侧字节一致**（row/h2/countP/addBtn/addBtnIcon/groupH3/delta/docSW 全部相同；countText/groupH3Text 为数据类、mt 形式差异为 v3/v4 margin-form 计算类 — delta 24 两侧一致）。

按强制顺序 — **先写计划再执行**。检查 networth.spec.ts 尾部插入点后创建 remediation-plan-v94.md：
写入 remediation-plan-v94.md（执行前验证已全部完成）：
计划已保存。现在执行 **F4 — 追加 v94 pin** 到 networth.spec.ts 尾部：
typecheck 发现接口可空性问题（行 2377）— 修正接口的可空字段：
typecheck 通过。运行 v94 pin 验证首次运行即绿：
**v94 pin 首次运行即绿** ✓。执行 **pin-sanity mutation**（按行号 418 修改 h2 的 fw）：
Mutation 命中。查看完整失败 diff 确认单轴命中：
**Mutation 精确命中 h2.fw 单轴**（"700"→"900"，fs/lh/color/h/mb 全绿）。运行完整 networth.spec.ts 验证无级联：
**无级联验证通过** — mutation 下仅 v94 pin 红（1 failed），其余 29 个全绿。恢复源码并独立重建：
**F4 完成**：pin 首次即绿 · mutation 单轴命中无级联 · 恢复后 30/30 全绿。进入 **F5 全链重跑**：
**e2e 全绿**：111+106+82 = 299 次执行 = **297 唯一测试**（+1 精确匹配，零抖动）。运行 smoke 与截图重生成：
运行截图重生成并字节比对（同日种子律 — 期望 16/16 字节一致）：
**F5 完成**：16/16 截图字节一致（同日种子律）。进入 **D1-D7 文档对齐**。先验证 v95 队列（对照 v89 探针自身头部 — 队列散文验证课）：
v95 队列已验证：**v89 时代的 DASHBOARD 组合**（Budget Guidelines 卡 + Quick-action 卡行，桌面 1280 全页，第五次重跑 [v61→v68→v77→v83→v89→v95]）。检查探针 README v93 章节结构以匹配格式：
v93 章节格式已掌握。探测各文档的精确锚点（D1-D6）：
检查 README 表格尾部行的实际顺序（v93 行插入位置）：
所有锚点已探测完毕（SKILL 表 newest-at-bottom、PAD 块 newest-at-top、README 表尾 newest-first 块）。编写 D1-D3 对齐脚本：
D1-D3 完成。编写 D4-D6 对齐脚本：
D1-D6 完成。编写 D7 — session_226.md 叙事文件：
session_226.md 完成。更新 worklog（头部文档列表 + Session 129 条目）：
写入 worklog Session 129 条目与文档列表更新：
**D1-D7 全部完成**。进入交付前检查（.env.example 准确性 / PIN-ONLY 验证 / 树状态 / 最终 lint）：
**交付前检查全绿**：.env.example 准确且已跟踪 · **PIN-ONLY 验证通过（git diff src/ = 0 行）** · 树状态符合预期形状（8 修改 + 16 新增，全在 docs/tests/scripts）。最终 lint 复跑：
Lint 干净。更新共享工作区 worklog：
共享 `worklog` 已更新。读取 SSH `wrapper` 使用说明并创建 `parity commit`：
Wrapper 支持 `--remote` 标志。创建 parity commit：
**Parity commit `ca38efa` 已创建**（24 文件，零 src/ 变更，树干净）。部署 SSH 密钥并通过 wrapper 推送：
Dry-run 干净（fast-forward 13e1445..ca38efa）。执行真实推送：
**v94 parity 周期已完成并推送** ✅（main @ `ca38efa`，24 文件 +2500/−5，零 src/ 变更，远程已验证 `refs/heads/main == local HEAD`，密钥已销毁，工作树干净）

**本周期交付摘要：**

| 阶段 | 结果 |
|---|---|
| **基线链** | seedcheck 精确 → lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓（SEO 对预渲染）· 296 e2e 零抖动 · 35/35 smoke |
| **F1 axe watch** | NO DRIFT（npm-latest/已装均 4.14.0，无 5.x，合约 pin 通过） |
| **F2 第 88 次 standing checks** | **移动端菜单第 88 次连续验证工作正常**（Tailwind v4 缓解保持）；参考站四 bug 仍存活；数据 census 零漂移 |
| **F3 重跑组合** | v88 时代 networth + drill-down 第五次重跑：两对 verdict 均 DIFFERENT，**每个 flag 均被 DOM 仲裁到文档化类**（含 3 个误读类/FAB 类 live 复核推翻）；两半 census 精确复现 v88 值 — **无新克隆差距，PIN-ONLY** |
| **F4 新 pin** | networth SECTION-HEADER 行族 @1280（h2 排版/计数 P/行 flex/Add Asset chrome/节奏 — 任何视口从未固定）；**+1 e2e = 297**；pin 首次即绿；mutation 单轴命中（h2.fw 700→900）且无级联（29 绿） |
| **F5 全链重跑** | 297 e2e（299 执行零抖动）· 35/35 smoke · **16/16 截图字节一致**（同日种子律第二连续纯形态） |
| **文档对齐 D1-D7** | AGENTS/CLAUDE(296→297)/README/SKILL(Session 129)/PAD(v1.1.51)/探针 README(+v95 队列)/session_226 + worklog；修复计划存至 `docs/remediation-plan-v94.md` |

**下一步建议**：按轮换账本，v95 周期目标是 **v89 时代的 DASHBOARD 组合**（Budget Guidelines 卡 + Quick-action 卡行 @1280，第五次重跑 [v61→v68→v77→v83→v89→v95]，已对照 vlm-shots-v89.sh 头部验证）。回复“继续 v95”即可开始，或提出对本周期交付的任何调整。
