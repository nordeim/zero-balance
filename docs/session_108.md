# Session 108 — the v47 session's raw tool-call narrative (2026-10-11)

The condensed transcript of the session that delivered
`docs/remediation-plan-v47.md` (parity iteration v47 — the
dialog-input focus composite + the net-worth card mobile census + the
mobile sheet's shadow-lg, a PIN-ONLY iteration).

工作区被重置——git clone 重建（HEAD 9981c43，v46 + session_105/106 文档就位）。环境重建：npm install → cp .env.example .env → db:push → db:seed → npx playwright install chromium（1243 构建，v46 教训前置应用）。五份核心文档 + 会话文档复审；v46 修复在代码中验证（net-worth-view.tsx:105/:210 的 mb-4）。
基线链：lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓（robots + sitemap 预渲染）· 223/223 e2e ✓（5.2m）· 35/35 smoke ✓。npm audit 同样的 5 个 dev-only advisory（--omit=dev = 0）；密钥扫描干净；.env ≡ .env.example；v46 差异复审：仅 1 个 src 文件（12 行，与计划逐行一致）。
第 41 次常规检查：参考站四 bug 仍在线——toast-blocker 用 elementFromPoint 实测（汉堡中心返回 fixed top-0 z-[100] 的空 toast 容器）；sheet-trap 实测（经 sheet 导航到 /income 后 sheet + overlay 仍在）；无 nav landmark；395 溢出。数据 census 只读（"1 items · $25,000"，v46 事故的 Savings Account/Commonwealth Bank 恢复完好）。SEO 对双站在线。克隆侧（with-server 内）：R1 汉堡开 sheet（5 链接）、R2 导航后 sheet 关闭、R1b 汉堡中心的 elementFromPoint 命中汉堡自己的 SVG 子元素（克隆的 toast viewport 是 pointer-events: none——无阻挡）、R3 nav landmark、R4 零溢出（390/390）。超集完好。
v47 三表面测量（双站实测）：(1) 对话框输入焦点态阴影组合（session-101 队列第二项）——参考站 REST 3 层（2 透明引线 + shadow-sm 可见层）、焦点态 3 层（白色零扩散引线 + 1px rgb(10,10,10) ring + shadow-sm 可见层）；克隆 REST 5 层、焦点 5 层——**两个可见层完全一致**，引线按构造分歧（v4 5-slot vs v3 3-slot，v10/v25/v45 接受类）。输入 chrome 全同（h 36/radius 6/pad 4px 12px/border 1px rgb(229,229,229)/bg 透明），焦点下边框色不变（双站）。**PIN-ONLY。**
(2) net-worth 卡移动端 census 390（v46 后续）——参考站卡（在它 432 宽的溢出网格里，docSW 464）h 194/pad 20/radius 12/border/rest shadow 0.04/transition 0.2s，值包 div.mb-4（mb 16，实测间距 16），facts 12px rgb(107,114,128)；克隆卡 358×194（页面适配，docSW 390）——**卡高完全一致（194）**，值 P mb 16（v46 修复在移动端成立——克隆把 margin 挂在 P 上，参考站在 wrap div 上：计算几何才是契约），facts 间距 16。**PIN-ONLY**（宽度分歧是文档化的超集修复——参考站自己的页面溢出）。
(3) 移动 sheet chrome 390（session-104 队列项）——参考 sheet 288×844/x 0/bg rgb(250,250,250)，shadow 2 透明引线 + v3 shadow-lg 对（rgba(0,0,0,0.1) 0px 10px 15px -3px + 0px 4px 6px -4px），overlay rgba(0,0,0,0.8) z 50；克隆同几何 + 4 透明引线 + **同两个可见层**——阴影刻度回归网第六站点。**PIN-ONLY。**
编写 remediation-plan-v47.md（F1 输入焦点组合 pin、F2 移动卡 census pin、F3 sheet shadow-lg pin、S1 四突变、D 系列）——v45 家族的第三个纯 pin 迭代，零生产代码变更。
TDD：三 pin 立即 GREEN（纯 pin 纪律：pin 证明对等，突变证明 pin）。S1 四突变验证（每个必须 FAIL）：(a) 移除 focus-visible:ring-1 → F1 失败；(b) 移除输入 shadow-sm → F1 失败；(c) 值 mb-4 还原 mb-2 → F2 失败（mb 16→8 + h 194→186）；(d) 移除 sheet shadow-lg → F3 失败。**执行教训：突变 (a) 首轮"通过"——e2e 套件跑的是 standalone BUILD 而非源码树；每个突变必须先 `npm run build` 才能被套件看见**（已写入计划 + 探针 README + SKILL 行）。
最终全链：lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **226/226 e2e ✓（5.2m——223→226）** · 35/35 smoke ✓（首轮一次 not-found 偶发——单独跑与复跑均绿，常规资源偶发类）。16 张截图重新生成。
常规 VLM 对（vlm-compare-v47.mjs，/income @390——新表面，参考站 /income 在 390 无溢出，实测 docSW 390）：**3 个旗标，全部 DOM 验证为数据/平台类**——克隆更丰富的种子带第二张收入卡，其第 4 个（Recurring）徽章在逐字节一致的 flex flex-wrap gap-2 容器中换行（参考站单卡数据永不显示此场景；徽章行 chrome 实测一致：同容器、同单徽章几何、徽章放得下时单行布局）；"Edit with Base44" FAB 是参考站自己的平台 chrome；无 chrome 差距（v43 误归因教训第三次应用）。
D 系列文档对齐：AGENTS.md 的 v47 段落；CLAUDE.md 的 226 计数 + 三处 v47 插入；README 的 v47 行 + 计数；SKILL 文档的 Session 82 行 + 状态行；PAD 的 v1.1.4 修订块；探针 README 的 v47 节（三探针 + 双驱动 + 六教训）；session_107.md（正式日志）+ session_108.md（本文）；仓库 worklog 的 Session 81 条目 + 账本清单；工作区 worklog。
提交 + SSH wrapper 推送（密钥物化、指纹验证、dry-run、真实推送、密钥销毁）。

## 本次会话概要

**会话链**：工作区重置重建（clone + 环境 + 1243 浏览器前置）→ 基线链全绿（108/223/35）→ 第 41 次常规检查通过（参考站四 bug 实测在线，超集完好）→ v47 三表面双站实测（全部可见层对等）→ 计划（纯 pin 迭代，3 pin）→ TDD（3 pin 立即绿 + 四突变全咬合 + 一次构建可见性教训）→ 交付。

**核心发现**：三个表面在所有可见层上均已对等——对话框输入的焦点组合（ring + shadow-sm 持久层）、net-worth 卡的移动端节奏（h 194 双站精确一致，v46 修复经受住移动端重排）、移动 sheet 的 shadow-lg 可见对（回归网第六站点）。零生产代码变更——第三次纯 pin 迭代（v45 家族）。

**其余成果**：e2e-tests-run-against-the-build 教训（突变必须先构建）；VLM 三旗标全部 DOM 验证为数据/平台类（更丰富的种子 + 参考站自己的 FAB）；参考站 /income @390 无溢出的新 VLM 表面；probe 目录新增 5 个文件（三探针 + 双驱动 + VLM 对）。

**建议下一步（v48 队列）**：item-details sheet 动作按钮阴影家族（回归网第七站点候选）、toast 阴影家族、空状态卡 chrome、对话框输入 390 焦点组合、或任选新表面。
