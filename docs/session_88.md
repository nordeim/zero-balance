工作区已存在。我来刷新它并查看当前状态。
工作区已刷新至 `8a7a3b4` (session_85.md)。让我制定工作计划并审阅所有文档。
现在我来读取仓库工作日志（最新条目在最前）并检查环境状态。
环境完好（.env ✓, db/custom.db ✓, Playwright ✓）。现在我来审阅剩余的核心文档和技能目录。
很好，我已经理解了该项目的架构。现在让我验证关键的技术交付物（sitemap/SEO、测试配置、a11y gate 状态），并检查代码仓库的 skills catalog。
所有关键交付物已验证。让我检查一下文档结构以及 a11y gate 的当前状态，以规划下一次迭代。
确认状态为：v39 已交付 (108/195/35)。现在让我启动基准链并继续进行文档审查。
Baseline: lint ✓, typecheck ✓, 108/108 unit ✓, build ✓。正在后台启动 e2e 套件（195 个测试），同时进行审计。
审计结果与已知接受状态相符（5个仅限开发的 `braces` 建议，secret scan 无异常，`.env` 与模板匹配）。在 e2e 运行的同时，我来审查一下 `v39` 正式日志的队列以及 `a11y` sheet-open 测试结构。
现在让我检查一下两个候选 v40 队列界面的代码——仪表盘快速操作和净资产摘要 chip。
e2e 后台运行似乎没有启动。让我检查并重启它。
E2E 正在运行（10 个进程）。在进行基准测试的同时，让我先查看用于双站扫描的 standing-check 脚本。
E2E 正在运行。现在让我开始进行双站点扫描——首先通过 `agent-browser` 对参考站点进行第 34 次例行检查。
Reference 侧第 34 次检查 —— 所有四个 reference 移动端 bug 仍然存在，数据为只读，SEO 组已上线。现在进行 clone 侧检查。
克隆端检查全部为绿色。让我验证一下 R3 探针语义（activeHighlighted 为空），以确保与 v39 相比没有出现偏差。
E2E 在 91/195。参考会话仍处于登录状态。现在让我来测量 v40 表面 —— 两个站点上的仪表板 Tab 顺序焦点走查（来自 session-78 队列中最后一个未测量的表面）。
Key discovery — the reference dashboard's Tab walk: stat cards are **buttons**, the donut `g` IS a tab stop, and there's a Base44 "Close badge" platform stop. Let me check how the clone renders these.
The reference's stat cards are real `<button>`s and its donut `g` is a tab stop. Now the clone's walk for comparison.
存在明显的差异。让我获取清晰的 DOM 级焦点快照（无需 `Tab-scroll` 瑕疵）并检查实际的页面组件。
我来把普查写成正式的探测文件。
干净的统计数据确认了参考站点具有 14 个可聚焦的停止点。让我探究这两个站点的 stat-card 区域结构，以确定差异。
现在我明白了参考站点上有两个统计界面（按钮行 = 可聚焦；大卡片 = 无效 div）。让我来探究一下在这两个站点上，是哪个 donut 元素接收了焦点停止点。
The reference's donut stop is `g.recharts-pie` with tabindex=0. Now the clone's donut stop (13 tabs in its walk).
The donut stop structure matches v31's replication exactly. Now the clone's clean focusable census for the geometry bands.
完整的人口普查差异已映射。让我检查一下 `StatCard` 的交互性之前是否有过相关决策，并找到 donut 键盘测试所在的位置。
圆环图键盘表面已完全固定。现在在编写 v40 计划之前，让我先检查一下 e2e 基准结果。
**Baseline chain fully green: 108/195 + build + lint + typecheck.** Now the smoke test to complete the chain, and the VLM pair for the session.
现在进行 VLM 配对——获取两个站点上所测量表面的全新 dashboard 截图。
VLM 组合：不同，有三个标志 —— 全部已解释（active-highlight 超集 #3，allocation bar = 演示数据，头像字母 = 演示用户）。测量阶段已完成。让我检查一下 v36 census 结束模式，然后编写 v40 计划。
All patterns confirmed. Now writing the v40 remediation plan.
计划已保存。现在开始 TDD —— 编写仪表板 Tab 键顺序遍历测试。让我先检查一下 spec 的头部。
Now writing the v40 census test at the end of dashboard.spec.ts.
让我验证一下 Add Item 按钮选择器 — 检查 app-shell 的顶部栏结构。
The `header button` selector would match the mobile burger (display:none). Fixing the band query to match the Add Item by text.
现在让我对该新测试进行 lint/typecheck，并针对现有的 build 运行它。
测试首次运行即已通过。让我检查一下 lint 警告。
该警告存在于我不使用的草稿探测中。正在将其删除（实际方法是 tabwalk + focused-dump）。
Lint 检查已通过。现在是变动健全性测试 (a)：移除 StatCard 的 role 和 tabIndex。
Mutation (a) 精确触发 —— 在 `stat-card` 停止点处未通过测试。正在恢复，随后进行 mutation (b)。
已恢复 → GREEN（测试通过）。现在进行变异测试 (b)：移除 StatCard 的按键处理程序。
变异 (b) 起到了作用——激活 pin 失败了（这个变异实际上重现了参考站点的死 UI 行为）。正在恢复。
两个 mutations 均已验证，src/ 的 diff 为空——生产环境代码零变更。现在正后台重新运行完整的 e2e 测试链（预期 196 个测试），同时持久化 v40 探针。
E2E 正在运行，108/108 个单元测试已通过。现在正在持久化 v40 常备检查脚本。
修复 v40 脚本中的头部注释，以准确描述 v40 surface。
现在处理探针 README 的 v40 部分。我来检查一下 v39 的格式。
E2E 运行至 16/196。现在正在调整文档。首先，对 README 的 v39 行和计数进行处理。
Now CLAUDE.md — the count + the census entry.
现在 AGENTS.md —— v40 段落。
现在处理 SKILL 文档 —— 状态行和会话行。
SKILL 文档已更新。我来检查一下 `e2e` 的进度，并查看正式的日志格式。
现在开始编写正式的会话日志 —— session_86.md。
现在处理仓库工作日志 —— Session 74 条目（最新优先）。
E2E 进度为 109/196。在它运行的同时，让我更新工作区工作日志并检查 SSH wrapper 的先决条件。
E2E 运行至 138/196。正在准备 SSH 推送先决条件 — 安装 paramiko 并审查包装器手册。
E2E 测试进度 145/196。在等待的同时，让我检查一下用于提交的变更集。
变更集已清理 — 无生产代码变更。正在等待 e2e 完成。
**196/196 e2e 已通过。** 使用最终构建重新运行冒烟测试以确保完整性，然后重新生成截图。
All 16 screenshots regenerated. Full chain green (108/196/35). Now committing the change set.
提交 `fc781d0` 已落地。现在进行 SSH 推送流程：将密钥实体化，验证指纹，然后进行空运行（dry-run）。
Fingerprint verified (matches v39's recorded key). Now the dry-run.
Dry-run clean (8a7a3b4..fc781d0). Executing the real push.
**推送已验证：main @ fc781d0。** 正在销毁操作员密钥，然后执行原始转录后续提交。
密钥已销毁。现在进行原始转录 (session_87.md) —— 即后续的 commit。
Both commits pushed. Final verification of the remote state.
**Parity iteration v40 已交付并推送到 main**（commits `fc781d0` + `5b0a6f3`，远端已验证，密钥已销毁）。

本会话核心成果：

- **第 34 次常备检查全清**：移动端导航 R1–R4 两站复验（Tailwind v4 pins 稳固，克隆站移动菜单正常；参考站四个移动端 bug 仍存活）、数据只读校验前后一致、SEO pair（robots + sitemap）两站在线
- **仪表盘 Tab 键序焦点走查**（session-78 队列最后一个未测表面）双站实测：参考站 14 个焦点停靠点，克隆站 16 个 —— **核心发现：参考站的大号统计卡片是无交互死 UI**（无 role/tabindex/处理器），克隆站是可键盘聚焦 + Enter/Space 激活导航的功能超集
- **1 个新 e2e（共 196）**，两项 pin-sanity 突变均验证会 FAIL（突变 b 精确复现参考站的死 UI 行为），**src/ 零生产代码改动**，全链 108/196/35 全绿
- 计划存至 `docs/remediation-plan-v40.md`，16 张截图重生成，全部文档对齐

**建议下一步**：重新下发简报并引用 `docs/session_86.md` / `docs/remediation-plan-v40.md` —— 队列中还剩 net-worth summary chip 的 savings-class 视口、a11y 门禁 sheet-open 扫描扩展到其余 5 个路由，或您指定的新表面。
