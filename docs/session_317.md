我将开始 v130 周期的执行。首先进行 F0 基线门禁：刷新工作区并确认远端状态。
本地 `zero-balance` 目录为空（工作区已重置）。执行 `git clone` 重建工作区。
F0 基线确认：clone 完成，main @ f25870b，v129 周期已推送（927ccab 含 CALCULATOR ghost-hover 修复 + 332 e2e）。现在核对周期文档存在性。
所有周期文档齐备（session_314/315、remediation-plan-v129、worklog.md）。建立 v130 周期任务清单。
remediation-plan-v130.md 尚不存在——本轮将创建。先读周期文档（session_315 是本轮操作者指令）。
session_315.md 确认为 v129 周期操作记录。v130 队列已验证：**v124-era NETWORTH + drill-down 对（第 11 次重跑，v60 原始）**。继续读 v129 交付记录与计划。
v129 计划与交付记录已读。现在读核心文档状态行与探针 README（v130 队列权威来源）。
v130 队列确认：**v124-era NETWORTH + drill-down 对（第 11 次重跑）+ 双 watch + 第 124 次常设检查**。验证 v124 谱系头部 bracket（权威来源）。
v124 头部已验证：11 项 bracket（v60 原始）+ TENTH 序数 → v130 = 第 11 次重跑，第 53 次 queue/ledger 一致。现在检查 v124 谱系的会话 token 与 census 结构。
v124 builder 为双 census 块形态（ARBIT_A/ARBIT_B）。研究最近派生形式（v129）与 v124 谱系的差异。
派生模式明确。现在检查环境状态（全新沙盒判定），然后按 v108 FRESH-CLONE 教训置备。
环境判定：**RE-PROVISIONED 类**（node_modules 空、无 .env、无 db/、仅旧 1200 chromium 对、内存健康 3567MB、无守护进程）。按 v127/v129 形态完整重建。启动 npm ci（前台，v108 教训）。
npm ci 完成（0 漏洞）。验证 zod 提取 + next 版本 + axe 引擎，安装缺失的 chromium 1243 对。
zod 840/840 ✓、chromium 1243 对已装。置备 .env + db/ 并执行 db:push + db:seed。
Seed 完成（7 items / 3 assets / 2 liabilities）。运行权威 seedcheck（预期 7/1850/2235/0/3/2）。
Seedcheck 精确 ✓。环境重建完成。开始 F0 基线门禁链：lint → typecheck → unit。
Lint ✓ · Typecheck ✓ · 108/108 unit ✓。生产构建：
构建成功 ✓（robots + sitemap 已预渲染）。正在权威推导 e2e 计数（--list，分块运行前）：
e2e 清单：**332 in 24 files**（331 spec + 1 setup）。核对 playwright 配置的项目结构与 v129 分块方案：
项目结构确认：setup + chromium 双项目。分块方案（v129 形态 + v129 pin）：ch1 90 · ch2 89 · ch3 74 · ch4 82 = 335 执行 = 332 unique。运行 chunk 1：
Chunk 1: 90 passed ✓。Chunk 2:
e2e 四块全绿：90+89+74+82 = 335 执行 = 332 unique，零抖动 ✓。运行冒烟测试套件：
**F0 基线首轮全绿**（lint · typecheck · 108 unit · build · 332 e2e 零抖动 · 35/35 smoke）。执行双 watch + 生产接缝审计：
双 watch 绿：npm-audit **0 漏洞**（第 21 次复查）· axe-core **无漂移**（4.14.0 == latest，dedupe=1）。生产接缝审计 + v129 修复验证：
生产接缝审计全绿（v129 修复在位、SEO 对、db-path、auth/rate-limit、TW4 缓解 ×2、三层测试、skills/ 排除）。进入 F2 —— 第 124 次常设检查。先研究派生形式：
派生形式明确。写 `derive-standing-v130.py`（123rd→124th，rd→th 转换）：
第 124 次常设对派生干净。执行参考侧：
参考侧全绿（四缺陷俱在、数据普查首读干净、SEO 对在线）。资源纪律（v128/v129 教训）后执行克隆侧：
克隆侧全绿——移动菜单连续第 **124** 次验证工作。核对 seedcheck 尾部：
**F2 完成 —— 第 124 次常设检查全绿**（seedcheck 精确 7/1850/2235/0/3/2）。进入 F3 —— v130 重跑对派生。先全面勘查 v124 谱系四个文件的头部与 era token 分布：
头部片段齐备。全面扫描四个 v124 文件中的 era token 残留位点，确保 correction 覆盖完整：
无 plan-pointer token（v124 谱系独有形态——只有四组 correction）。提取精确头部片段以构建 correction map：
构建 `derive-v130-series.py`（通用交换 6 组 + 四组 history corrections）。先精确验证 v118-v123 在四个文件中的全部位点：
全部 era token 限于头部（2-8 行）。写 `derive-v130-series.py`：
系列派生干净（4/4 首跑全中、零残留、行数保持 84/71/65/328）。研究两半构建器与 comparator 派生形式：
两半构建器派生形式明确。验证 arbit-v130.sh 标记结构后写 `derive-build-twohalf-v130.py`：
标记结构逐行验证一致。写 `derive-build-twohalf-v130.py`：
两半构建完成（ARBIT_A 90 行 md5 5033e36a… · ARBIT_B 111 行 fb8fec53…）。写三向 md5 验证器：
v124 形态为两向验证。核对 v129 的三向形态（source + 双半）并升级 v130 验证器：
升级 `verify-twohalf-v130.py` 为标准三向形态（source + 双半）：
三向合约全保持。派生 comparator —— 研究 v124 形式：
F3 派生全部完成。检查 v130 探针系列的截图产出与 VLM 比较器输入契约：
VLM 比较器需 4 张截图。核对 arbit 半的 log 路径后开始执行参考侧仲裁半：
运行参考侧仲裁半（log 重定向至 /tmp/vlm130/ref-census.log）：
/tmp/vlm130 目录不存在（arbit 半不自建）。创建后重跑：
参考半完成（PART A drill-down + PART B networth census 齐）。资源纪律后运行克隆仲裁半：
克隆半首跑成功（seedcheck 精确尾部）。运行 census 逐轴对比：
73 轴 —— 67 相同 + 6 已记录类差异，**0 新增**。验证与 v124 记录值精确一致：
v130 census **精确复现 v124 值**（同 73/67/6 分割、同类、零漂移）。执行参考侧截图：
4 张截图齐备。运行 VLM 成对比较（第一遍，全 log 捕获）：
VLM 第一遍：**NETWORTH IDENTICAL / DRILL-DOWN DIFFERENT** —— v124 一致形态。但出现 "Edit with Base44" FAB 声明（drill-down 面）—— 按常设形态需现场证伪。查 v129 证伪脚本形式：
按 v97+ 常设形态派生 `base44-fab-arbit-v130.sh`（drill-down/dashboard 面，登录态双侧）：
**FAB 现场证伪**：双侧 fabCount 0 + bodyHasBase44 false（dashboard 面，1280，登录态）。运行 VLM 第二遍：
第二遍反转（NETWORTH DIFFERENT / DRILL-DOWN IDENTICAL）—— 与第一遍及 v124 形态不一致。读完整 log 分析 flag：
第二遍的 FAB 声明指向 **/networth 面**（参考侧）。扩展 v130 FAB 仲裁脚本覆盖两个被标记面（dashboard + networth）：
FAB 双面双侧证伪完毕。第二遍 networth 的另一 flag（profile 卡垂直位移）需 DOM 仲裁（v43 规则）。查 app-shell 侧栏实现后写仲裁 census：
侧栏为 `fixed inset-y-0` 固定轨——profile 卡双侧应同钉视口底。写单次双侧 census 仲裁（v43 形式）：
定位器过松（命中全文档根）。修正为最内层 "Budget Pro" 块：
**仲裁决定性**：profile 卡几何逐字节相同（x16/y724/w223/h60，底距 16px，fixed 轨钉定）——第二遍 flag 为 **VLM 误读**（把 seed-count 文档高度差 895 vs 1411 误判为卡片位移）。查历轮是否有 verdict 翻转先例：
v127/v121 先例确认——**verdict-variation family**（跨遍翻转、每 flag 均已记录类、census 权威零新增）。F3 完成。进入 F4 pin 候选勘查——networth 面 kebab 双子的 hover 端态覆盖：
networth kebab 双子（82/192 行）携带完整 ghost 家族（`hover:bg-accent hover:text-accent-foreground`）。v46 持 card-hover 揭示、v124 持 OPEN 态——**own-hover 计算端态无 spec 持有**（v128 形态的异文件孪生）。勘全网 networth.spec 覆盖图以确认最强候选：
核对 v124 pin 注释中的 reveal 家族覆盖图，确认 own-hover 轴确实无持有：
v124 覆盖图确认：networth kebab 的 **own-hover 端态**（opacity 1 + tint + color）无任何 spec 持有。再核对 summary-card 侧（v60/v67）的已持轴，完成候选空间勘查：
覆盖图完备：summary-card/tablist/drill-down 1280 已被 v60/v67/v44 彻底持有；**networth kebab own-hover 是唯一无持有轴族**。候选锁定。研究 v128 census 形式以派生 v130 版：
派生 v130 census。先核对 networth 资产卡容器结构（finder 结构选择器）：
networth 卡为 `div.group.rounded-xl` + h4。查参考侧 networth 卡片的既有 census finder（v46 时代参考侧形态）：
v46 网格 finder 形式明确（`lg:grid-cols-3` 双侧通用）。核对 v124 pin 的断言轴（避免 V94-COLLISION）：
v124 pin 持 OPEN 慁全套 chrome（w/h/radius/bg/color/insets）——v130 pin 按 V94-COLLISION 纪律只持阶梯轴。写双侧单次 census `kebabhover-arbit-v130.sh`：
**双侧 census：own-hover 阶梯逐字节相同**（at-rest opacity 0/bg transparent/color rgb(10,10,10) → OWN-HOVERED opacity 1/bg rgb(245,245,245)/color rgb(23,23,23) → restored；几何 36×36/r6px/transition opacity 0.15s 全等）——**零差距，v130 为 PIN-ONLY 周期**。按固定协议先写 remediation plan：
Plan v130 已存。对照代码库复核计划（执行前验证）——先核对 v131 队列候选（v125-era 对的身份）：
修正：v125-era 对是 **DASHBOARD 对**（非 SAVINGS）。更新计划中的 v131 队列：
继续复核：研究 v128 pin 的 spec 代码与 append 脚本形式：
v128 pin 形态完备，networth.spec.ts 尾部即插入点。查 append-pin-v128.py 形式：
写 `append-pin-v130.py`（PIN-ONLY 形态——先 GREEN 后突变）：
**测试通过 — 首次运行全绿（2 个通过）**。执行**测试健全性变异**（第 82 行作用域仅限值的 alpha 修饰符形态）：
唯一故障验证（1 failed = v130 pin + 37 passed）。核对故障轴恰为预测的 hovered-bg 行：
故障轴恰为预测（hovered bg → lab(...0.5) alpha 形态，其余轴全保留）。恢复变异 + 完整重建 + 恢复后回归：
**恢复后回归 107/107 全绿**（networth 37 + items 49 + calculator 20 + setup——v128/v129 异文件免疫现场验证）。更新计划状态并进入 F5 ship 链：
F5 ship 链启动 —— 快速门禁（lint/typecheck/unit/audit）：
e2e 四块全绿（91+89+74+82 = 336 执行 = 333 unique，零抖动）+ 35/35 smoke。截图字节比对——查 v129 截图捕获形式：
截图最后一次提交于 v127（Oct 27 06 UTC，今日同日——same-day law 成立，预期 16/16 字节一致）。运行捕获并比对：
**截图 16/16 字节一致**（git 零变更）。开发环境证据——派生 v130 dev-shots 脚本（version-swap-only 验证）：
开发截图 4 张捕获 + 菜单证明通过（/income, docSW 390, navLandmark true）。运行 verify：
**F5 ship 链全绿**（dev 4/4 字节一致 + VLM 通过）。进入 D1-D7 文档对齐——先采集各文档 D0 锚点（v129 形态）：
按常设形式用持久化脚本对齐。读 align-docs-v129.py 结构：
构建 align-docs-v130.py 前先验证 D0 锚点（每处 1-hit）：
全部 9 锚点 1-hit。写 `align-docs-v130.py`：
D1-D5 已对齐。D6 —— 探针 README（v130 节 + v131 队列）。研究 v129 形式：
写 `align-probereadme-v130.py`（v130 节 + v131 队列——v125-era DASHBOARD 对，v61 原始）：
D6 完成。D7 —— worklog Session 165 条目。研究 s164 插入形式：
写 `worklog-insert-s165.py`（Session 165 条目， newest-first 插入）：
D7 完成 + .env.example 未动。编写 session_316.md（v130 交付记录）：
session_316.md 已写。更新计划 ToDo 11-12 并审查预提交变更集：
变更集形态正确（src/ 0 行、.env.example 未动、tests +142、docs/scripts 对齐齐备）。读 SSH wrapper 使用技能：
核对 shim 与 paramiko 状态（工作区重置后需重建）：
shim 存在，paramiko 需重装（工作区重置）。按 v129 形态在正确环境安装：
paramiko 5.1.0 就绪。验证 shim 在 PATH 上可用：
shim 功能正常（需 PATH 导出）。创建 parity commit（消息按仓库惯例完整撰写）：
Parity commit `ab6ab3e` 已建。SSH 推送序列——密钥写入 0600 临时文件（仓库外）+ 指纹核验：
指纹与谱系记录一致（`4FSV1Pro...` 前缀匹配）。Dry-run（显式 --remote，v128 教训）：
Dry-run 干净（远端在 f25870b，快进至 ab6ab3e 已授权）。正式推送：
**推送已验证**：remote main @ ab6ab3e == HEAD，HTTPS 复核逐字节一致。补 session_316.md post-push 段（两部分惯例）+ tail commit：
**双推送已验证**（remote main @ 3903721 == HEAD，工作树干净，密钥已粉碎）。更新工作区 worklog：
**v130 周期完成并推送** — 远端 `main @ 3903721`，工作树干净，未建新分支。

**亮点：**
- **基线与常设**：RE-PROVISIONED 工作区首轮全绿（108 unit · 332→333 e2e · 35 smoke）；双 watch 绿；移动菜单连续第 **124** 次验证工作
- **重跑对**：NETWORTH + drill-down 第 11 次重跑（第 53 次 queue/ledger 一致）；census **73 轴复现 v124 值、零新增**
- **VLM 判定**：inverse-split verdict-variation family（v121/v127 先例形态）——两遍翻转但每个 flag 均已归类：FAB 声明（双向）在**两个被标记面**双侧现场证伪；profile 卡“位移”经 DOM 仲裁为 **VLM 误读**（几何逐字节相同，docH 差为 seed-count 类）
- **PIN-ONLY 周期**（src/ 零变更）：networth kebab own-hover 阶梯双侧 census 逐字节相同——无需修复；+1 e2e = 333；alpha 修饰符突变唯一故障现场验证 + 恢复后回归 107/107

**下一步**：v131 —— v125-era **DASHBOARD 对**（第 11 次重跑，v131 队列已排定并写入探针 README），等待您的下一条指令。
