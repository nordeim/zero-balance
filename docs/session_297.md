工作日志确认 v120 已交付。现在开始 v121 周期（会话 156）。先刷新工作区并阅读文档。
Workspace was RESET — re-cloned from `main @ 19d6d1f` (npm ci, playwright v1243 pairs, .env + db push + db seed).
Seedcheck 准确无误 (7/1850/2235/0/3/2) ✓。Provisioning verified (zod src/v4 intact, both v1243 binaries INSTALLATION_COMPLETE, the explicit-env-prefix Prisma discipline)。
Docs aligned at v120 baseline。正在读取探针 README v121 队列 + v115 谱系标头（授权人）。
v121 queue confirmed: the v115-era ITEMS pair, TENTH re-run. Verified against `vlm-shots-v115.sh`'s own header (NINTH ordinal, 10-entry bracket — no off-by-one)。核心文档已锚定 — 正在启动 **F0 基准链**：lint → typecheck → 108 单测 → 构建。
F0 基线：lint ✓ · typecheck ✓ · 108/108 单测 ✓ · 构建 ✓ (robots + sitemap 已预渲染)。323 tests in 24 files (authoritative `--list`)。分片：ch1 = dashboard+networth+networth-error (86+setup)，ch2 = items+login-parity+calculator-error (79+setup)，ch3 = calculator+dialog-buttons+tokens+mobile-navigation+item-details+not-found (76+setup)，ch4 = a11y（其真实文件名）+其余 (81+setup)。
所有 4 个分片在首次运行中均通过：87+80+77+82 = 326 = 323 个唯一，零抖动 (zero flakes) ✓。冒烟测试 35/35 ✓。**F0 完全通过 (绿灯)。**
F0b：0 个漏洞 ✓（第 12 次复核，v110 加固保持：next 16.4.3 + zod 4.6.7）。F1：axe 无漂移 (NO DRIFT) ✓ (npm-latest 4.14.0，单个 node_modules/axe-core 条目)。接缝已验证 (hover/group-hover 变体，toast 修复，SEO 对，skills/ 已排除，v117 恢复)。
正在从 v114 谱系推导第 115 个常备对 (derive-standing-v121.py — 三个 token 系列，归一化后干净)。
115th 常备对已推导 ✓。正在运行参考端（四个 bug 存活，数据普查准确，SEO 实时）。
Reference side ALL GREEN ✓。清理僵尸进程，然后进行克隆半区 (clone half)。
Clone side ALL GREEN — mobile menu VERIFIED WORKING the 115th consecutive time, zero overflow at 390 on all five views。半区后的 Seedcheck ✓。**F2 已完成。**
正在从 v115 谱系推导 v121 探测序列 (derive-v121-series.py — mapping every history-correction fragment)。
5/5 correction families applied on the FIRST run (12 instances, line counts preserved 57/49/50/220→285)，语法均无误 ✓。
推导双半区构建器 — 发现 v115 构建器的 clone_login 带有过期的 `clonearbit109` token (与在 v120 中修复的 v114 `clonearbit108` 相同类别的怪癖)。在谱系中修正为 `clonearbit121`。
Halfs built with the md5 contract b55dcd29 (the 193-line census block verbatim) ✓。Running the reference-side VLM shots (first-attempt login)。
Reference shots captured ✓。清理，然后进行克隆镜头 + 双轮通过中的第一轮。
Pass 1 verdict: **BOTH PAIRS DIFFERENT**。运行第 2 轮（完整日志纪律）。
Pass 2: **INCOME IDENTICAL + EXPENSES DIFFERENT** — the v109/v115 split。被标记的 FAB（反向读取 — “在克隆中呈现”）→ 正在运行实时否证。
base44-fab-arbit-v121.sh: fabCount 0 + bodyHasBase44 false on BOTH sides ✓ — the FAB disproven live, the direction irrelevant。
运行双半区普查，并保存日志。克隆半区后的 Seedcheck 准确无误 ✓。
正在推导 compare-v121-census.py (v115 比较器 + census-era 修正)。
**普查：187 个轴 — 163 个相同 + 24 个已记录类，无新增** ✓ (v115 的拆分完全重现)。**F3 已完成。**
正在开始 **F4：pin 候选调研** — 映射 items 视图上的 pin 覆盖率（过滤器卡片、网格、表头行、卡片、空状态）。
候选 A：800 处的 expenses 过滤器 md 带区状态（从未锁定）。正在编写单次双方普查 (expband-arbit-v121.sh)。
普查：在双方均为字节相同 (BYTE-IDENTICAL) — 每个 chrome 轴均为 207px 双轨道 ✓。编写锁定 + 正在将其追加到 items.spec.ts。
Pin 追加，计数 324。正在运行 pin-sanity 突变 (第 175 行范围 `md:grid-cols-2`→`md:grid-cols-1`) + 重建。
**检测到两个红灯** — v121 pin + v1 时代的 items.spec.ts:622。正在检查冲突。
622 断言了原始的 `md:grid-cols-2` CLASS TOKEN 本身 — 任何对该 token 的突变都会使两个规格变红 (SPEC-ALIAS COVERAGE 教训重演)。重新作用域分析：在系列上不存在唯一的故障轴（gap-4→v70，lg token→622+v70，col-span→v70，卡片行→v64/v70/v115）。
**候选 A 已拒绝** — 根据实际唯一故障测试。移除追加的 pin 块（文件截断回 4587 行，计数恢复到 323，类型检查无误）。正在重新调研。
正在调研 confirm-bar 系列 — v46 F3 持有 /networth 实例；item-card 实例从未锁定（每个现有断言仅为行为相关）。
**候选 B：item-card 的内联 confirm bar at 1280** — v120 负债孪生前例形式（已锁定的系列，从未锁定的孪生；引用无 confirm bars — 其 R6 立即删除）。正在更新计划 F4 + 将候选 A 记录为已拒绝。
编写 confirmbar-arbit-v121.sh (仅克隆普查，完整 Radix 指针序列，fixture-restore Cancel)。
普查结果：柱条 {mt 16/flex/center/space-between/radius 8/pad 12/bg rgb(254,242,242)/w 267}，标签为 14px/400 "Delete this item?"，药丸匹配 v46 F3 合约，+80 柱条打开增量 (230→310 = 16+64 精确)，取消恢复 ✓。颜色读取为 lab() — 特意不进行断言 (v46 F3 系列)。
正在重写 append-pin-v121.py 以适配 confirm-bar 锁定并追加。Typecheck 正常，计数 324。
Pin GREEN 独立运行，但 622 变红 — 调查：STALE 变异的独立版本（重建还原后缺失）。
v98 重建纪律：重建 ✓ → **47/47 通过** (622 确认绿色 — 早些时候的红灯只是过期的构建)。
Pin-sanity 突变：第 210 行范围 `p-3`→`p-4` + 重建。
**唯一故障已实时验证**：v121 pin 单独红（柱条 pad 12px→16px 主轴），items+networth 的完整运行 81 个绿色，包括 v46 F3 networth 孪生。正在还原 + 重建。
重建后还原：**47/47** ✓。**F4 已完成。**
F5 交付链：lint ✓ · typecheck ✓ · 108 单测 ✓ · 0 漏洞 ✓。
交付分片：87 ✓ · 81 ✓ (items +1) · 77 ✓ · 82 ✓ = 327 = **324 个唯一，零抖动** ✓。冒烟测试 35/35 ✓。
Screenshots 16/16 字节相同 (git clean) ✓。开发证据已捕获 + VLM 已验证（菜单证明：/income，docSW 390，navLandmark true）✓。**F5 已完成。**
D1-D5 对齐 (align-docs-v121.py — v120 段落尾部的 D0 检查结果为 CLEAN，不需要 dedup)。D6 探针 README v121 部分 + v122 队列 (v116 时代的 SAVINGS 对，第十次重跑)。正在编写 session_295.md。
工作日志通过 insert-worklog-v121.py 插入会话 156 条目 ✓。已验证 .env.example 匹配（未触动）。
差异已验证 — 树外提交消息 (v112 卫生) 已写入，提交 `5528489` 已创建。
SSH 包装器推送：paramiko shim 已部署 (python3.13 — 3.12 缺少它)，密钥已解析 (ed25519)，干运行时第一次尝试旧的默认远程仓库 → 使用了 `--remote git@github.com:nordeim/zero-balance.git` 覆盖；干运行快进 (fast-forward) 干净。
**已推送并双重验证** — 远程 main @ 5528489 == 本地 HEAD，通过 SSH + HTTPS。正在编写推送后会话日志 (session_296 + session_297) 并销毁密钥。
正在推送会话日志提交。
密钥已销毁 ✓。最终工作区工作日志更新。
**v121 周期完成并已推送** — `main @ 5528489` (parity) + 会话日志提交，两者均 HTTPS 验证。

**头条新闻：**
- **目标**：v115 时代的 ITEMS 对的第十次重跑（收入 + 支出 @ 1280×800）— 结论为 v109/v115 拆分，普查 **187 个轴，零新差异**；反向读取时的 FAB 在现场被证伪。
- **锁定**：**item-card 内联 confirm-bar 普查 at 1280** — 从未锁定的孪生组件（v46 F3 持有 networth 实例），+80 柱条打开增量精确，唯一故障突变绿色。
- **被拒绝的候选 + 经验教训**：800 处的 expenses md 带区（双方字节相同）未能通过唯一故障测试 — v1 时代的规格断言了原始的 `md:grid-cols-2` token（SPEC-ALIAS COVERAGE 教训重演）；v98 重建纪律被重新验证。
- **交付状态**：324 e2e 零抖动，35/35 冒烟测试，0 个漏洞，移动菜单第 115 次连续绿色，截图 16/16 字节相同，工作区 RESET 类（全新克隆配置端到端）。

**下一步**：回复 "continue v122" 以运行 v116 时代的 SAVINGS 对（SAVINGS @ 1280×800，第十次重跑），或建议调整节奏。
