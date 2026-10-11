# Session 105 — the v46 session's raw tool-call narrative (2026-10-11)

The condensed transcript of the session that delivered
`docs/remediation-plan-v46.md` (parity iteration v46 — the net-worth
card census + the value→facts spacing fix + the confirm-bar white-pill
regression pin).

工作区被重置——git clone 重建（HEAD fb8d00f，v45 + session_101/102/103 文档就位）。环境重建：npm install → cp .env.example .env → db:push → db:seed。首个 e2e 跑挂了 220/221——browserType.launch：chromium-1243 不存在（缓存里是 1200/1248；npm install 解析的 1.63.0 锁文件补丁需要 1243）——npx playwright install chromium 后全绿。
基线链：lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓（robots + sitemap 预渲染）· 221/221 e2e ✓（5.0m）· 35/35 smoke ✓。npm audit 同样的 5 个 dev-only advisory（--omit=dev = 0）；密钥扫描干净；.env ≡ .env.example。
第 40 次常规检查：参考站四 bug 仍在线（toast-blocker、sheet-trap、no-landmark、395 溢出）；数据 census 前后一致（只读）；SEO 对在线。克隆侧（with-server 内）：R1 直击、R2 sheet 关闭、R3 nav landmark、R4 零溢出、sheet 结构完好、SEO 对在线。超集完好。
v45 差异审计：fb8d00f 为 PIN-ONLY 迭代（只有 tests + docs + probes，src/ 零变更）——与文档逐行一致。
v46 排队表面（session_101 的建议）：net-worth 卡片 hover 1280、对话框 input 聚焦态阴影、白 pill shadow-sm。编写探针：nw-card-v46.mjs + confirm-pill-v46.mjs + 驱动 ref-v46.sh / clone-v46.sh。
参考站首轮：探针的网格 finder 失败（"no sm:grid-cols-2 grid"）——dump 参考站 DOM：它的资产卡网格是 `md:grid-cols-2 lg:grid-cols-3`（960/3×309.328/gap 16），第一稿的 finder 误把汇总卡内部的 `sm:grid-cols-2` 统计块网格当成了卡网格（v4 G4 设计）。修正 finder 后 census 全捕获：卡 309/194/pad 20/radius 12/border/rest shadow 0.04/transition all 0.2s——**与克隆逐字节一致，唯独卡高 194 vs 186**。
关键发现——值→事实间距：参考站把值包在 `div.mb-4`（16px 间距）里；克隆的值 P 直接挂 `mb-2`（8px）。8px 差 = 卡高差。克隆自己的 item-card 用的就是 mb-4 包裹（:152）——net-worth 卡是唯一误抄处。
真实悬停（agent-browser hover）：双站卡的 shadow 都惰性（inline 压过 hover:shadow-lg，v29 家族）+ kebab 揭示（opacity 0→1）+ translateY none——一致。
**事故——参考站的直接删除**：kebab 菜单 → Delete 的点击就是删除本身（参考站无确认条，v18 超集修复家族的实测再证）——探针把参考站唯一的资产删了。立即通过它的 Add Asset 表单恢复（参考站的对话框是无 role 的 fixed inset-0 div——用 Save 按钮文本定位）：Savings Account / bank account / 25000 / Commonwealth Bank / 2026-10-07——面板 census 复读 "1 items · $25,000" 与删除前逐字节一致，仪表盘 census 不变。
克隆侧（with-server 内）：census 逐字节一致（卡高 186 = mb-2 间距差）；确认条白 pill census 全捕获（shadow-sm 可见层 rgba(0,0,0,0.05) 0px 1px 2px 0px——主题 pin 生效）；Cancel 恢复。合成 el.click() 打不开 Radix 菜单——native click（agent-browser click）才行。
编写 remediation-plan-v46.md（F1 间距修复、F2 卡 census pin、F3 白 pill pin、S1 四突变、D 系列）。
TDD：F2 先写——RED（值 mb 8px ≠ 16px + 卡高 186 ≠ 194，失败点精确落在间距断言上）；F3 立即 GREEN（pin-only）。F1 修复（mb-2→mb-4，两卡）→ networth spec 19/19 GREEN。S1 四突变验证（每个必须 FAIL）：(a) mb-4 还原 → F2 失败 ✓；(b) pill shadow-sm 移除 → F3 失败 ✓；(c) inline 0.04→0.08 → F2 失败 ✓；(d) kebab group-hover 移除 → F2 hover 步失败 ✓。全部还原 → 绿。
一次执行教训：首轮 -g v46 跑挂在资源耗尽（agent-browser 守护进程的 Chrome 实例跨工具调用存活）——pkill -f agent-browser 后恢复。
最终全链：lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **223/223 e2e ✓（5.2m——221→223）** · 35/35 smoke ✓。16 张截图重新生成。
常规 VLM 对（vlm-compare-v46.mjs，/networth @1280）：**IDENTICAL——零旗标**（第二次完全干净的筛查）。
D 系列文档对齐：AGENTS.md 的 v46 段落；CLAUDE.md 的 223 计数 + v46 插入；README 的 v46 行 + 计数；SKILL 文档的 Session 81 行 + 状态行 + 命令 + 三层行；PAD 的 v1.1.3 修订块；探针 README 的 v46 节（事故 + 五条教训）；session_104.md（正式日志）+ session_105.md（本文）；仓库 worklog 的 Session 80 条目 + 账本清单；工作区 worklog。
提交 + SSH wrapper 推送（密钥物化、指纹验证、dry-run、真实推送、密钥销毁）。

## 本次会话概要

**会话链**：工作区重置重建（clone + 环境 + 1243 浏览器）→ 基线链全绿（108/221/35）→ 第 40 次常规检查通过 → v46 三表面测量（含一次事故 + 完整恢复）→ 计划（1 修复 + 2 pin）→ TDD（1 RED→GREEN + 1 pin-only + 四突变）→ 交付。

**核心发现（值→事实间距）**：参考站的卡值包裹在 mb-4（16px）里；克隆的裸 P 挂 mb-2（8px）——卡高 186 vs 194。item-card 自己的 mb-4 包裹是库内先例——net-worth 卡是唯一误抄处。修复 = 两行类名交换。

**其余成果**：net-worth 卡 census 1280 逐字节对齐并钉住（含真实 hover 惰性 + kebab 揭示）；确认条白 pill 的 shadow-sm 可见层钉住（主题 pin 的回归网，五站点家族）；VLM 对第二次零旗标；事故完整恢复（参考站资产删除 + 逐字节还原）。

**建议下一步（v47 队列）**：对话框 input 聚焦态阴影组合（session-101 队列第二项）、net-worth 卡 390 移动端 census、item-details sheet 的动作按钮阴影家族、或任选新表面。
