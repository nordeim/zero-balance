工作区已被重置，`zero-balance` 目录不存在。需要重新 clone 仓库。
仓库已克隆，最新为 v128 周期完成态（session_312 已写、worklog Session 163 已记、v129 队列已排定：LOGIN + CALCULATOR 对）。现在审查核心文档与周期文档。
已读 session_313（v128 操作记录）与 plan-v128。现在读 session_312（v128 交付记录）与 worklog 头部、probe README 的 v129 队列。
v128 周期已确认完成并推送（remote main @ f85bbec）。本会话为 **v129 周期**，队列目标：v123-era LOGIN + CALCULATOR 对（第 11 次重跑）。工作区为全新克隆，需按 v108 FRESH-CLONE 教训完整重建环境。先读 probe README 的 v129 队列与核心文档状态行。
v129 队列已确认：LOGIN + CALCULATOR 对（v59 原始，11 项 bracket，v123 自身 TENTH → v129 = 第 11 次重跑，第 52 次 queue/ledger 一致）。现在做核心文档压缩验证。
文档已对齐（CLAUDE 331、README/SKILL/PAD/AGENTS v128 段落齐备）。工作区为全新克隆 —— 属 **RE-PROVISIONED 类**（v127 周期自身形态，v108 FRESH-CLONE 教训全程适用）。先锚定 skills 与环境状态。
环境确认为 RE-PROVISIONED 类：node_modules 空、无 .env、无 db/、playwright 缓存仅有旧 1200 对。按 v127 形态完整重建。启动 npm ci（前台），同时锚定 skills。
zod 提取完好（840 文件）、next 16.4.3、axe 4.14.0。安装缺失的 chromium 1243 对。
seed 完成（7 items / 3 assets / 2 liabilities）。seedcheck 报错，查看完整输出。
**Seedcheck 精确核对：7/1850/2235/0/3/2** ✓。环境重建完成。按 v128 教训检查残留浏览器守护进程与内存，然后锚定技能。
内存健康（3539MB 可用）、无残留进程、端口空闲 —— 全新沙盒无需 daemon reap。重新锚定仓库技能。
技能已锚定（§3 db-path、§12 TW4、§14 三层测试、§16 安全映射至生产接缝审计）。开始 **F0 基线门禁**。
Lint ✓ · Typecheck ✓ · **108/108 unit** ✓。生产构建：
Build ✓（robots + sitemap 预渲染）。按惯例先权威推导 e2e 计数再分块运行。
每文件计数合计 330 specs + 1 setup = **331 in 24 files** ✓（与 v128 交付形态一致：items 49 含 v128 pin）。分块组成：ch1 90 · ch2 88 · ch3 74 · ch4 82 = 334 executions = 331 unique。运行四块：
**F0 基线首轮全绿（零修复）**：lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **331 e2e 零抖动**（334 执行 = 90+88+74+82）· **35/35 smoke** ✓。现在执行生产接缝审计 + 两个 watch。
**F0 完成 —— 首轮全绿、零修复（RE-PROVISIONED 类）**。双 watch 绿：npm-audit 0 漏洞（第 20 次复查）· axe-core 无漂移（4.14.0 == latest，dedupe 保持 1）。

进入 **F2 —— 第 123 次常设检查**。研究 v122 对的 token 结构与 v128 派生形式：
Token 结构干净（无子串陷阱）。查看 v128 派生脚本形式并写 `derive-standing-v129.py`：
第 123 次常设对派生干净。执行参考侧：
参考侧全绿（四缺陷俱在、数据普查首读干净、SEO 对在线）。克隆侧：
**F2 完成 —— 第 123 次常设检查全绿**（移动菜单连续第 123 次验证工作、seedcheck 精确）。

进入 **F3 —— v129 重跑对（LOGIN + CALCULATOR）**。v123 头部已确认 TENTH/11 项 bracket（v59 原始）→ v129 = 第 11 次重跑，第 52 次 queue/ledger 一致。清点 v123 谱系的 history-correction 位点：
研究派生形式完成。全面清点 v123 谱系的 era token 与 correction 位点：
注意：arbit-v123.sh 的会话 token 为 `refcalc`/`clonecalc`（无版本子串）—— 需按 v121 教训显式交换。检查 v123 谱系是否有两半构建器形态：
会话 token 为 `refcalc123arbit`/`clonecalc123arbit`（"123" 无 "v" 前缀 —— 通用交换无法触及，需显式交换）。研究两半构建器派生形式：
v123 谱系有两块 census JS（CALC 22-82 + LOGIN 84-119）—— 与 v122 谱系的单块形态不同。查看 verify 形式与 compare 形式：
研究完所有派生形式。现在提取四个 v123 文件的精确头部片段以设计 history-correction：
提取完毕。全面扫描四个文件中的 era token 残留位点，确保 correction 覆盖完整：
所有 era token 均在头部（3-8 行）。检查其它无前缀数字 token：
所有纠错位点已限定。写 `derive-v129-series.py`（通用交换 + 四组纠错 + 残留检查 + 行数保持）：
系列派生干净（4/4 纠错首跑全中、零残留、行数保持）。现在检查 comparator 的 era token 分布，然后写两个 derive 脚本：
写 `derive-build-twohalf-v129.py` 与 `derive-compare-v129.py`：
comparator 残留 `/tmp/vlm123` —— 路径 token 含 "lm123" 而非 "v123"，通用交换无法触及。修复 GENERIC 列表加入显式路径交换：
两半构建完成（CALC 61 行 + LOGIN 36 行）。写 `verify-twohalf-v129.py`（双块三向 md5 验证）：
**F3 派生完成 —— 双块三向 md5 合约全保持**（CALC e1092d12d06677a4 · LOGIN 9e5a52d2ab0f2ab9）。执行前按 v128 教训检查资源：
参考侧仲裁半完成。验证 log 中两块 census 齐全后运行克隆侧：
⚠️ 参考 log 中未见 login census（grep "view" = 0）且 log 仅 2.7KB。检查完整 log：
Login census 实际在 log 中（转义引号导致 grep 未中）。两块参考 census 干净。运行克隆仲裁半：
克隆半超时（300 秒）。检查日志与进程状态诊断：
log 为空且无 server.js 进程 —— with-server 启动失败。查 parity-server.log：
深入诊断：检查 clone-arbit 脚本结构、parity-server.log 是否存在、:3200 残留服务器：
`clonelogin123arbit` —— 发现第三个会话 token（我此前 grep 模式漏掉了 `reflogin/clonelogin` 家族）！但会话名不应导致空 log 挂起。读取整个 clone-arbit-v129.sh 排查结构问题：
Heredoc 结构完好（EOF 在 274 行）。发现 **2 个漏换的陈旧会话 token**（`reflogin123arbit`/`clonelogin123arbit`）。继续查挂起点 —— 看 marker 与 130 行之间的内容：
with-server 直接测试正常（health OK）。检查超时运行期间产物的实际状态：
**矛盾**：with-server 测试成功（health OK）但 parity-server.log 不存在！完整读取 with-server.sh：
**谜底揭晓** —— 有两个 with-server.sh！clone 半调用的是 `scripts/parity-probes/with-server.sh`（bun 启动，日志在 tool-results/parity3200.log）。查该日志：
服务器启动正常 —— 挂起原因是 agent-browser 守护进程资源耗尽（v128 事件类的变体：ref 半与 clone 半之间未执行 pkill 资源纪律 + 新会话 spawn 阻塞）。同时确认派生遗漏了 `reflogin123arbit`/`clonelogin123arbit` 两个会话 token。先全面扫描残留 123 token：
仅这两个会话 token 残留（其余 123 均合法：era 标记、密码、bracket）。更新派生脚本加入遗漏的交换，重新派生：
重派生干净、md5 合约不变、4 个会话 token 全部正确。执行资源纪律（pkill 守护进程），重跑 ref 半（契约一致性），再 pkill，再跑 clone 半：
**Clone 半重跑成功**（资源纪律生效 —— v128 教训在 v129 的确认）。运行 census 对比：
**106 轴 —— 97 相同 + 9 已记录类差异，0 新增**，close 键不对称方向保持。验证与 v123 记录的数字一致性：
v129 census **精确复现 v123 值**（106/97/9 同分、同类、零漂移）。运行 VLM 成对比较（两次、全 log 捕获）：
Pass 1 CALCULATOR 判定 DIFFERENT（两个 flag 均为 v123 已记录类）。但 LOGIN 对截图缺失（ENOENT ref-login.png）—— 检查 v123 形态中 login 截图的来源：
存在独立的 login 截图对（`login-shots-v123.sh`）。查找克隆侧对应脚本并派生 v129 版：
需补充派生 login 截图对。写 `derive-loginshots-v129.py`：
四张截图齐备，两侧 login census 逐字节一致。运行 VLM 比较（两遍，全 log）：
VLM pass 1：**CALCULATOR DIFFERENT / LOGIN IDENTICAL**（v123 一致形态；calculator 三个 flag 均为已记录类）。LOGIN 的 FAB 声明（Image 1 的 Base44 徽章）需按常设形态现场证伪。查看 v127 证伪脚本：
v129 的 FAB flag 在 LOGIN 视图（登出面）。检查是否有 v123 形态的直接对应：
v123 的 FAB 证伪正是所需形态（/login 面、1280）。派生 v129 版并执行：
**FAB 现场证伪**：双侧 fabCount 0 + bodyHasBase44 false。运行 VLM pass 2：
**VLM 双遍一致**：CALCULATOR DIFFERENT / LOGIN IDENTICAL —— 与 v123 判定形态一致，所有 flag 均在已记录类中，FAB 已现场证伪。验证 clone 半尾部 seedcheck：
Seedcheck 精确。**F3 完成 —— 无新克隆差距，v129 为 PIN-ONLY**。进入 **F4 —— pin 候选勘查**。查 v123 周期自身的 pin 与该面的覆盖图：
v123 pin 了 confirm-bar。现在勘查 v129 的 pin 候选 —— 该面族的 hover 端态覆盖。查 calculator 与 login 源码的 hover 类及 specs 覆盖：
Calculator 面有多个 hover 家族。勘查 specs 对这些元素 hover 端态的覆盖：
覆盖图：行操作的 group-hover 揭示已被 pin（calculator.spec:376）；X 按钮仅有 v27 G1 的**类 token** pin（无计算端态）。查 addBtn/login-card 的 hover 与 specs：
v27 G1 pin 的是 **item dialog** 的 X（含 hover:text-accent-foreground），而 calculator X（calculator-dialog.tsx:138，仅 hover:bg-accent）是不同元素。确认 v87 pin 对象与全套件对该 X 的 hover 覆盖：
v87 pin 的是 calculator X 的**静止态** chrome（v59/v49/v53 持几何）。该 X 的 OWN-HOVER 计算端态（tint）无任何 spec 持有 —— 与 v128 kebab 形态直接对应。核对 login 侧覆盖以确认最强候选：
登录面 hover 家族已被 v13/v45 持有。**候选确认：calculator X 的 OWN-HOVER 端态**（静止态已被 v59/v49/v53/v87 完全持有；computed tint 零覆盖 —— v128 形态的直接孪生）。研究 v128 census 形式：
写 v129 census 前，查 v87 pin 的几何 finder 形式（参考侧 X 无可访问名 —— 必须 tag-agnostic）：
v87 finder 形式明确。写 `xhover-arbit-v129.sh`（calculator X 的 own-hover 阶梯 census，双侧）：
克隆半完美（阶梯：transparent → **rgb(245,245,245)** → transparent，几何 36×36/r6px 全等）。但参考半的 state read 报 "no panel" —— 需完整输出诊断。单独重跑参考半并捕获全输出：
参考半 "calculate clicked" 但面板未找到 —— 而 arbit-v123 的 CALC census 在参考侧成功过。对比 v123 的面板 finder 与打开方式：
参考侧面板是 **plain fixed div（maxWidth 768px）** 而非 [role=dialog] —— 我的 finder 缺少回退分支（v99 工件类的根源）。看 v123 形态的参考侧打开流程后修正 finder：
v123 形态要点：参考侧面板是 plain div（需 maxWidth 回退分支）、真实指针按下/抬起点击、Rent 卡重试环。重写 census 脚本：
**关键发现 —— 双侧阶梯测得一个新差异**：hovered bg 双侧同为 rgb(245,245,245) ✓，但 **hovered color：参考 侧 rgb(23,23,23)（accent-foreground）vs 克隆 侧 rgb(10,10,10)** —— 参考站的计算器 X 携带 `hover:text-accent-foreground`（v27 G1 记录的 ghost 家族），克隆的计算器 X 没有。这是 v87 静止态 census 无法看到的**新克隆差距**（该轴从未被测量）。

按修复纪律先复核，并顺带测量参考侧行操作按钮的 hover 家族（判定修复范围）：
JSON 输出多行导致提取失败。修正为紧凑单行格式：
**修复范围扩大**：参考站的 calculator ghost-hover 家族覆盖全部三个按钮（X + edit + trash 均为 hover 后 → rgb(23,23,23)，连红色 trash 也变灰）。克隆的三个按钮（138/239/247 行）均缺失 `hover:text-accent-foreground`。查 Add Item 按钮的 hover 家族以完成范围判定：
Add Item 按钮属品牌渐变家族（zb-btn-add），不在 ghost-icon 修复范围。**修复范围锁定：138/239/247 三处**。研究 v123/v128 pin 代码形式以设计 v129 pin：
看 v123 pin 的 fixture 恢复尾部与行操作按钮的 aria-label：
Pin 设计完备。按固定协议先写 remediation plan（修复 + pin 周期 —— v46 以来首个 src/ 修复）：
Plan 已存。写 `append-pin-v129.py`（X 阶梯 + 行操作阶梯 + fixture 恢复）：
**TDD RED 验证** —— pin 在未修复构建上恰好在 X 的 hovered-color 轴失败（预期 rgb(23,23,23)，实际 rgb(10,10,10)）。应用修复：
**GREEN 验证** —— pin 通过（修复 3 行）。重跑双侧 census 验证修复后契约一致：
**修复后契约逐字节一致**（双侧 OWN-HOVERED：bg rgb(245,245,245) + color rgb(23,23,23)，仅余已记录的 v3/v4 transitionProperty 计算形式差）。执行 pin-sanity 突变（138 行单行回退）：
**唯一故障验证：仅 v129 pin 失败（1 个失败 + 20 个通过）**。确认故障轴为预测的 X hovered-color 后恢复：
故障轴恰为预测（X 的 hovered color，bg/hoverMatch/radius/w/h 全保留）。恢复修复并跑恢复后回归：
**恢复后回归通过：86/86**（calculator + dialog-buttons + items，v123/v128 pin 全绿 —— 异文件免疫现场验证）。更新 plan ToDo 并进入 F5 ship chain：
Ship chain 前半全绿，**332 tests in 24 files**（331 + v129 pin）。跑四块 e2e：
**e2e 全绿零抖动**（336 执行 = 332 unique）+ **35/35 smoke**。截图字节比对（hover-only 修复预期逐字节一致）：
**截图 16/16 逐字节一致**（仅悬停修复不影响任何静态截图）。开发环境证据 —— v128→v129 派生：
4 张开发截图**字节一致**（`git status` 为空），菜单验证通过（`/income`、`docSW` 390、`navLandmark` 为 `true`）。请确认 `verify` 脚本的期望答案形态：
Dashboard 答案符合期望形态（Guidelines 卡在折叠线下、汇总卡 + 通用 Add Item 为正确状态）。**F5 ship chain 全绿完成**。

进入 **D1-D7 文档对齐**。先验证 v130 队列（v124-era NETWORTH + drill-down 对）的 bracket：
v130 队列验证：v124-era NETWORTH + drill-down 对，TENTH/11 项 bracket（v60 原始）→ v130 = 第 11 次重跑。研究 v128 对齐脚本形式并采集 D0 锚点：
研究完成。采集各文档的 D0 锚点（v128 段落尾部、CLAUDE v128 子句尾、README v128 行、SKILL S163 行尾、PAD v1.1.85 块头）：
锚点齐全。查看 PAD v1.1.85 块形式与 CLAUDE v128 子句尾、SKILL S163 行尾的精确文本：
README 的截图尾锚有 3 处命中 —— 需用 v128 唯一的普查 token 消歧。写 `align-docs-v129.py`：
D1-D5 对齐。D6 —— 探针 README（v129 节 + v130 队列）。研究 v128 形式：
写 `align-probereadme-v129.py`（v129 节 + v130 队列）：
D6 完成。D7 —— worklog Session 164 条目（研究 s163 形式后写）：
工作日志 S164 已插入，.env.example 未动。编写 session_314.md（v129 交付记录，post-push 段落待 tail commit）：
session_314.md 已写。更新 plan ToDo 12-13 并审查预提交变更集：
变更集形态正确（src/ 3 处修复、tests +1 pin、docs/scripts 对齐、.env.example 未动）。准备 commit 与 SSH push —— 先读 how-to 技能：
需要安装 paramiko 并创建 shim。读技能 Appendix A 的 shim 源码：
pip 受 PEP 668 限制。用 `--break-system-packages` 安装：
pip 与 python 版本错位（系统 pip → py3.13，活动 python → venv 3.12）。在 venv 中安装：
paramiko 5.1.0 就绪（与 v128 记录一致）。创建 shim（Appendix A 完整源码 + v127 重写形态）：
指纹与谱系记录一致（`4FSV1Pro...`）。创建 parity commit：
**Parity commit `927ccab` 已创建。** SSH-wrapper dry-run（显式 --remote，v128 教训）：
试运行（Dry-run）干净（远程仓库在 2cf6429，快进至 927ccab 已授权）。正式推送：
**已推送 —— 远程 main @ 927ccab == HEAD，HTTPS 复核一致。** Tail commit（session_314.md 追加 post-push 段）：
双推送已验证（远程 main @ ebc3a91 == HEAD、工作树干净、密钥已粉碎）。更新工作区 worklog：
v129 周期已交付并推送。最终总结：

**v129 周期完成并推送** — 远程 `main @ ebc3a91`，工作树干净，未建新分支。

**亮点：**
- **基线与常设**：首轮全绿（108 unit · 331→332 e2e · 35 smoke）；双 watch 绿；移动菜单连续第 123 次验证工作
- **重跑对**：LOGIN + CALCULATOR 第 11 次重跑（第 52 次 queue/ledger 一致）；census 106 轴复现 v123 值、零新增
- **本周期为修复（REPAIR）周期**（v46 以来首个 src/ 变更）：X-hover 双侧 census 发现计算器 ghost-hover 家族缺 `hover:text-accent-foreground`（X/编辑/删除三按钮，含红 trash 的 hover 变灰契约）——3 行修复，TDD RED→GREEN 现场验证，修复后逐字节一致
- **新 pin**：ghost-hover 家族 own-hover 阶梯（+1 e2e = 332），单行回退突变唯一失败验证

**下一步**：v130 —— v124-era NETWORTH + drill-down 对（第 11 次重跑，队列已验证），等待您的下一条指令。
