工作区已被重置 —— `zero-balance` 代码库缺失。我将按照操作说明重新进行克隆。
代码库已克隆至 HEAD `19d6d1f`。v120 的迭代提交 (`5ac804d`) 已在 main 分支中——因此本周期为 **v121**，依据于对 `session_293.md`、`remediation-plan-v120.md`、`session_294.md` 的引用。让我来设置待办事项列表并开始深度阅读。
已确认：v120 已交付；session_293 预测下一个周期为 **v121 —— v115 时代的 ITEMS 对（第十次重跑）**。现在正在读取 session_294 和 worklog 尾部。
session_294 确认 v120 已交付。当前周期为 **v121 — v115 时期的 ITEMS 对（第十次重跑）**。现在正在读取 worklog 尾部 + 核心文档。
worklog 看起来是按最新在前排序的。让我查看一下它的开头，以获取 Session 155 条目。
AGENTS.md 有一些非常长的行（在此项目中很常见）。让我先提取其结构，然后阅读关键部分。
v121 队列已确认。现在正根据 `vlm-shots-v115.sh` 自身的头部（队列文本验证经验教训 —— 谱系为权威）进行验证。
Header 已验证：v115 时代的 ITEMS 对（/income + /expenses @ 1280×800 桌面端全页），在 10 个条目的括号中排在第 9 位，因此 **v121 = 第 10 次重新运行** —— 第 44 次队列/账本协议。现在正在研究 v115 谱系（判决类 + census 形式）。
现在我来查看 v116–v120 的 pin 和该配对的裁决历史（用于比较器历史修正），并检查环境状态。
让我检查一下 `item-card` 和 `goal-card` 之间的 `kebab` 类系列（新的 `pin` 候选方案需要进行 `collision survey`），并检查环境配置状态。
现在正在调查本轮循环的潜在 pin（expense card 的 hover 动作行 vs v116 savings kebab —— 不同的家族）以及 spec 覆盖率中的碰撞准则。
v45 F1b 已经锁定了 action row 系列。让我阅读 items-view.tsx 以映射其谱系并寻找从未被锁定的系列。
有两个潜在的候选方案。我来检查一下 pin 覆盖率：(a) 项目视图的空状态（可通过搜索 `filter-to-zero` 确定），(b) `expenses` 过滤器在 800 处的 `md-band`。
空状态已固定 (v6 G12 + v48 F3) ——已拒绝。候选 B：md band 800 处的 expenses-filter 内部网格。正在验证与 v115 (income md pin) 和 v70 (expenses 1280 pin) 的冲突。
pin candidate 已确认：**800 处的 expenses-filter md-band 状态**（从未固定；第 175 行的 mutation line 是 expense-conditional，与 v115 的 income line 和 v70 的 1280 pin 结构不同）。现在配置全新的 clone 工作区（v108 FRESH-CLONE 课程：在前台运行 npm ci 并设置长超时）。
npm ci 状态正常（zod src/v4 完好，axe-core 4.14.0 x1，357 个模块）。正在检查 Playwright v1243 的二进制文件。
两个 v1243 对均已验证 (INSTALLATION_COMPLETE ×2)。现在正在配置 `.env` + `db/` + seed，然后运行 seedcheck。
Seedcheck 精确 ✓ (7/1850/2235/0/3/2)。正在启动 F0 基准链：lint → typecheck → 单元测试。
Lint ✓ · Typecheck ✓ · 108/108 unit ✓。现在开始构建。
构建完成 ✓（robots + sitemap 已预渲染）。正在获取权威的 e2e 计数以进行分片。
24 个文件中共有 323 个测试（v120 交付状态）。正在构建不相交的 4-chunk 拆分。
每个文件的统计与 v120 运送表完全一致：ch1 = dashboard+networth+networth-error (86+setup=87) · ch2 = items+login-parity+calculator-error (79+setup=80) · ch3 = calculator+dialog-buttons+tokens+mobile-navigation+item-details+not-found (76+setup=77) · ch4 = a11y+rest (81+setup=82) → 326 executions = 323 unique。正在检查 chunk runner 接口。
Playwright 会自行启动其 webServer (port 3100, e2e.db)。现在正在运行 Chunk 1：dashboard + networth + networth-error。
Chunk 1: 87/87 ✓ (1.6m)。Chunk 2：items + login-parity + calculator-error。
Chunk 2: 80/80 ✓。Chunk 3：calculator + dialog-buttons + tokens + mobile-navigation + item-details + not-found。
第 3 部分：77/77 ✓。第 4 部分：其真实文件名下的 a11y (v111 教训) + 其余部分。
All 4 chunks green on first runs: 87+80+77+82 = 326 = 323 unique, zero flakes ✓. Now the smoke suite.
F0 基线已全部通过 (绿灯) ✓。现在进行 F0b (npm audit — 第十二次复核) + F1 (axe-core 监控)。
F0b：0 个漏洞 ✓（第十二次复核，next 16.4.3 + zod 4.6.7 成立）。F1：无漂移 ✓（npm-latest 4.14.0，单引擎条目）。快速生产接缝验证，然后进行 F2 处理。
All seams verified ✓ (hover/group-hover variants, toast fix, SEO pair, skills/ excluded, v117 restore). Now F2 — deriving the 115th standing pair from the v114 lineage.
第 115 个常备对已推导出 ✓。现在开始从 v115 谱系中推导 F3 探针系列——正在研究派生模板。
正在读取四个 v115-lineage 文件，以映射 v121 衍生版本的精确修正片段。
所有 token 已映射。正在写入派生脚本。
推导过程：首次运行 5/5，零残留，行数保持完整 (57/49/50/285)。所有四个文件的语法检查。
Derived header correct. Now the two-half census builder — studying the v115 builder + its derivation template.
已确认 provenance carry 格式。正在编写 v121 builder 推导。
Census 已构建：193 行的 block md5 b55dcd29（逐字记录），两半部分字节完全一致。正在验证语法 + session tokens。
两半部分语法均无误，会话 token 正确。现在开始运行 F2 — 第 115 次常驻检查：先处理参考端。
Reference side: 所有四个 bug 均在 ✓，首次读取数据统计准确 ✓，SEO 双方均在线 ✓。清理 zombie 并运行 clone half。
克隆端：R1–R4 全部通过 —— **移动端菜单在第 115 次连续验证通过**，所有五个视图均无溢出。克隆端之后的 Seedcheck。
F2 完成 ✓。现在进行 F3 —— 执行 reference 侧的 VLM 截图。
参考截图已捕获（首次尝试登录 ✓）。正在清理，然后进行克隆端处理。
第一轮：**两对均不同** —— 该配对的已记录判定类（v103 的拆分；VLM 判定变化形式）。第二轮以完整日志记录规范开始。
第 2 轮：**收入一致 + 支出不同** —— 确切的 v109/v115 拆分（第 1 轮中收入侧的标识均为全数据类；更清晰的结果形式）。现在进行双方普查 —— 参考一半。
Reference half 的值与 v115 记录匹配。现在处理 clone half。
Both halves captured + seedcheck exact ✓. Now deriving the axis-by-axis comparator from the v115 form.
All quads hold — the v121 census reproduces the v115 values exactly. Deriving the comparator.
普查：**187 个轴 — 163 个相同 + 24 个已记录类别，零新增** ✓（v115 精确分割）。已触发 FAB 标记（反向形式）——正在运行实时反证。
FAB 在双端被实时证伪（fabCount 0, bodyHasBase44 false）✓。**F3 已完成。** 现在开始 F4 —— 正在研究 v115 md-band 普查脚本，以构建一次性双端 v121 普查。
现在正在编写一次性双边普查 (expenses filter md-band at 800) —— v121 形式。
**在两侧字节完全一致** — 每个轴（207px 双轨道，非跨越搜索，3 个组合框 @207/36/14，卡片 480/138/24，docSW 800）。最干净的 PIN-ONLY 形式。正在验证 mutation 行作用域。
第 175 行是唯一的类字符串出现位置（第 165 行是注释）——符合行作用域规范。现在先编写补救计划（遵循规范），然后再执行 pin 操作。
Plan saved. Now the pin append — studying the v120 append template.
Pin 已附加：数量 324，类型检查通过，**47/47 的项目测试通过**（GREEN，仅 PIN-ONLY 形式，无失败状态）。现在进行 pin-sanity 突变测试 — 第 175 行范围限定，然后重新构建。
在 v121 pin 下有 2 个红色——有一个意外的冲突。正在识别第二个故障。
冲突原因：旧版的 622 测试锁定了原始的 class token `md:grid-cols-2` 本身。正在检查 v70 pin 的轴，以寻找另一个唯一的失败突变目标。
支出 `md-band` 候选方案**未通过唯一失败测试** —— 旧的 622 测试断言了原始的 `md:grid-cols-2` token 本身（这是 spec-alias 覆盖教训的重现）。根据 v116 第一次尝试的先例：拒绝，重新调查。首先恢复该 mutation。
所有现有的断言都是行为相关的——确认栏的 **chrome 从未被固定**。这是新候选者（仅超集表面，参考站点上无双向对应）。正在检查 net-worth confirm-bar twins 以进行变更范围界定。
The confirm-bar family is pinned on /networth (v46 F3) but the **item-card instance is never pinned** — the v120 liability-twin precedent form (pinned family, never-pinned twin). Reading the v46 F3 contract values.
v46 F3 合约已映射。正在更新计划的 F4（已记录被拒绝的候选者 → 新候选者：item-card confirm-bar 实例，v120 liability-twin 先例形式）。
现在从 `items.spec.ts` 中移除被拒绝的 pin 块，然后测量 `confirm-bar` 系列。
The rejected pin is fully removed (count back to 323). Studying the v116 census interaction form, then writing the confirm-bar census.
正在编写仅限克隆的一次性 confirm-bar census。
普查结果：柱条 {mt 16/flex/center/space-between/radius 8/pad 12/w 267}，标签 14px/400 “删除此项目？”，胶囊组件匹配 v46 F3 合约，柱条展开增量 **230→310 = +80 (16 mt + 64 bar — 计算准确)**，取消恢复 ✓。颜色读取为 lab()（v4 漂移类 — 根据 v46 F3 形式排除在断言之外）。重写追加脚本。
622 的失败是由于修改后的**过期预构建**导致的——`standalone` 仍然包含着 `md:grid-cols-1` 的构建（这是 `v98` 原则：还原后需要重新构建）。现在正在重新构建。
**恢复后的构建中 47/47 通过** ——该 pin 独立通过，622 确认通过。现在对该确认栏 pin 进行 pin-sanity mutation：第 210 行作用域限制的 `p-3`→`p-4`。
**SOLE FAILURE 已确认** —— 只有 v121 pin 变红；networth v46 F3 pin（不同的文件孪生）显示为绿色。正在验证红轴，然后恢复。
已确认失败点在 `pad` 轴（12px→16px）。正在恢复、重建并运行回归测试。
验证构建确实已成功完成（静默失败教训），然后更新计划状态。
F4 完成。现在开始 F5 ship chain：lint → typecheck → unit。
Ship chain gates 1–4 ✓。现在进行 4-chunk e2e 发布运行（分片 2 增加了 v121 pin：items 46）。
e2e 已交付：87+81+77+82 = 327 = **324 个唯一，零 flake** ✓。现在进行冒烟测试 + 截图。
截图字节完全相同 ✓ (git clean)。现在开始处理 dev-server evidence set —— 派生 v121 dev-shots 脚本 (仅版本号交换)。
开发证据 4/4 字节完全一致 + VLM 已验证 ✓。**F5 已完成。** 接下来进行 D1–D7 文档对齐 — 正在研究 v120 对齐脚本。
正在检查 align-docs-v120.py 锚点 + 扫描 AGENTS.md 中是否存在 v120-tail 缺陷（D0 检查）。
正在检查 AGENTS.md 中 v120 段落的末尾，寻找 v119 缺陷类别（D0 检查）+ 锚点。
D0 检查：正常（无重复缺陷——v120 段落末尾出现恰好一次）。正在检查 README 锚点。
所有锚点已验证。正在编写 align-docs-v121.py (D1–D5；D0 不需要 — v120 尾部干净)。
All D1–D5 landed ✓. Now D6 — the probe README alignment (v121 section + the v122 queue).
D6 已完成。现在进行 D7 — 编写 session_295.md（v121 正式记录）。
现在是 worklog Session 156 条目——正在研究 insert-worklog-v120.py。
D1–D7 已完成。最终审查：git status + `.env.example` 验证。
变更集已清理（32 个文件：D1–D7 + v121 探测系列 + 计划 + pin）。正在 git commit 树外编写提交信息（v112 卫生规范）。
已创建 Commit `5528489`，工作树清洁。现在开始 SSH wrapper 推送 —— 正在阅读 runbook。
paramiko 位于 python3.13 下。正在阅读 Appendix A shim 表单，然后部署 key。
正在从 runbook 中提取完整的 shim，将其部署到 repo 之外，并使用 python3.13 shebang。
密钥已解析 ✓。正在 PATH 中使用 shim 进行预运行（Dry-run）。
该 wrapper 的默认远程仓库是旧的示例仓库 —— 正在检查远程覆盖选项。
Dry-run clean: `19d6d1f..5528489` fast-forward to main ✓. Real push now.
推送并经 SSH 验证 ✓。HTTPS 双重验证 + 正在检查 push 后的 session-log 约定。
HTTPS verified: remote main `5528489` == local HEAD ✓。正在编写推送后的会话日志（根据约定分为两部分）。
REST API 受到速率限制；现在改用 git 的 HTTPS 协议进行验证。
**已通过 HTTPS 验证**：远程 `main @ 8a8561d` == 本地 HEAD ✓。正在销毁操作员密钥。
**v121 周期已完成并已推送** — `main @ 5528489` (功能对齐) + `8a8561d` (会话日志)，均已通过 HTTPS 验证，密钥已销毁。

**亮点：**
- **目标**：v115 时期的 ITEMS 对（收入 + 支出 @ 1280×800）的第十次重运行 — 结果：v109/v115 分割，统计 **187 个维度，零新增差异**；FAB（悬浮按钮）在实时测试中被证伪。
- **方案**：item-card 内联确认栏（inline confirm-bar）在 1280 处的统计（从未固定的孪生组件）— +80 的栏打开差值是准确的，单一故障突变（mutation）为绿色（通过）。
- **被拒绝的候选方案**：800 处的支出 md-band（字节完全相同）未能通过单一故障测试 — v1 时期的 spec 断言了原始的 `md:grid-cols-2` token（SPEC-ALIAS 的经验教训再次应验）。
- **交付状态**：324 个 e2e 零抖动（zero flakes），35/35 冒烟测试，0 个漏洞，移动端菜单连续第 115 次绿色（通过），屏幕截图 16/16 字节完全相同。

**下一步**：回复“continue v122”以运行 v116 时期的 SAVINGS 对，或建议调整执行节奏。
