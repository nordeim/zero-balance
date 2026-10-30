拉取快进了一个文档文件（session_330.md —— 操作者的 v134 转录记录，79 行）。这是 **v135 周期**（指令引用 session_329/plan-v134/session_330 —— session_330 为操作者的 v134 转录记录，其中命名了 v135 队列）。
工作空间为 CONTINUING 类——v134 周期自身的沙盒工作空间持续存在（node_modules 354 包、两对 chromium、.env + db/ 完好）；任何门禁前 seedcheck 精确（7/1850/2235/0/3/2）。
读取 session_330 + session_329 + v134 计划；验证 v134 状态：items.spec.ts:5252/5280 的 v134 pin、状态行 108/337/35、PAD v1.1.91、CLAUDE 337、探针 README 的 v135 队列——全部确认。
v135 队列：**v129 时代的 LOGIN + CALCULATOR 配对（LOGIN 视图 + CALCULATOR 对话框于 1280x800，第 12 次重跑）**。账本验证：v129 计划的 F3 在 12 项括号上记录 ELEVENTH 序数 [v59 为原始] → v135 = TWELFTH。第 58 次连续一致性。开始 F0 门禁链。
Lint ✓ · 类型检查 ✓ · 108/108 unit ✓。构建 ✓（robots + sitemap 预渲染）。E2e 经 --list 计数：24 个文件中的 337（336 spec + 1 setup）。4 个分块：93 ✓ · 91 ✓ · 74 ✓ · 第 4 块……
**闪烁复现**：第 4 块首跑失败于 not-found:111（1 失败 + 81 通过——v134 已记录的间歇性）。执行已记录的升级步骤：隔离 spec 7/7 ✓；带 trace 复跑 82/82；有界捕获循环 4 次干净（一次被工具超时中途杀死）；3/3 带仪表运行干净（服务器日志在场——无崩溃输出）。**捕获：page.goto: net::ERR_CONNECTION_REFUSED at http://localhost:3100/——测试死于导航本身；v134 的"瞬态错误 head"假设被证伪。** 已验证的不对称：服务器绑定 0.0.0.0（仅 IPv4；127.0.0.1 → 200，[::1] → REFUSED）——localhost 解析抢跑 ::1 优先即机制。**修复：BASE_URL 钉在 IPv4 字面量（playwright.config.ts——测试配置变更）；修复下全套 337 复验绿。**
**第二个间歇性**：合并复跑中 empty-states:85 以 `TypeError: Cannot read properties of undefined (reading 'map')` 失败——保留的 trace 显示 GET /api/liabilities 未携带 Cookie 头 → 401 {"error"} → data 未定义。storageState 验证健康；触发未确认（一次性的 cookie 附加缺失）。**已添加诊断守卫**（json 解构前 expect(list.ok())）——第 2 次出现（交付链）恰如设计读取："Expected: true / Received: false"。另一次工具超时击杀后的 17 失败终端块事故——基础设施伪迹，已记录、未计数。
Smoke 35/35 ✓。监控绿：npm-audit 0 漏洞（第 26 次复核）· axe-core 无漂移（4.14.0，去重保持）。
F2：派生第 129 对常设对（derive-standing-v135.py，128th→129th th→th 纯替换）。干净派生。参考侧全绿（四缺陷俱在，普查首读干净，SEO 对俱在）。克隆侧全绿——**移动端菜单连续第 129 次验证通过**，390 零溢出；seedcheck 精确。
F3：v135 系列派生自 v129 谱系——首跑 4/4 历史修正，零残留，行数保持 102/166/65/355。login-shots 子系列派生（30/30）。构建器派生（教训区间 v92..v128 → v92..v134 + 谱系注记修正最后）+ 两半构建：**双块 md5 契约三方验证（CALC_CENSUS_JS 61 行 e1092d12d06677a4 + LOGIN_CENSUS_JS 36 行 9e5a52d2ab0f2ab9——v123/v129 数值逐字）**。比较器派生（/tmp/vlm129→vlm135 日志路径交换 + 两处溯源引文重指 v129 度量）。
两半在资源规范下执行（首登成功；完整日志由运行器重定向捕获）。普查：**106 轴——97 相同 + 9 已记录类别差异，零新增——精确复现 v129 数值**（同 106/97/9 分布）。
VLM 截图双方捕获。第一轮：**CALCULATOR 不同 / LOGIN 相同**。第二轮：**CALCULATOR 不同 / LOGIN 不同——唯一旗标为 "Edit with Base44" FAB**——由 base44-fab-arbit-v135.sh 现场证伪（fabCount 0 + bodyHasBase44 false 双方）。配对的判定-变化族。
F4——LOGIN + CALCULATOR 表面的 pin 候选调查（survey-logincalc-v135.sh）。登录按钮的 hover 族在参考上实测：提交 #0f172a→#1e293b、Google #f8fafc/#cbd5e1/shadow-sm、模式链接 #64748b→#334155——全部与克隆类精确匹配（双方匹配，已记录）。计算器 X 的 :138 类串不携带任何 focus 类（:239/:247 的行动按钮则有）——**键盘路径完全未 pin。候选：计算器 X 的 FOCUS-VISIBLE 阶梯 @1280。**
编写 focusx-arbit-v135.sh（v129 xhover 形式适配键盘阶梯）。两个查找器 bug 现场修复：Calculate 正则（单引号中的 `\$` = 字面美元——去掉反斜杠）与面板回退（ref-arbit 的 maxWidth-768px 形式）。克隆的走查落在 Radix 自动聚焦上（fv false）——**落点条件修正为要求 :focus-visible**（自动聚焦为程序性，不得满足走查）。
修正后的普查测得**差距**：参考的聚焦档携带 1px #0a0a0a ring（白色前导 + rgb(10,10,10) 0px 0px 0px 1px）+ outline 形式（solid 2px 透明，offset 2px），而克隆携带 UA 默认 outline（auto 1px）无 ring。**v129 hover 修复的孪生——FOCUS 族从未对齐。编写修复计划（pin 前——固定协议）。**
计划已存。TDD 顺序：pin 追加（append-pin-v135.py）→ **RED 运行现场验证**（pin 单独失败于 ring toContain："none" 接收 vs ring 预期——恰为预测轴）→ **修复**（zb-row-action 类 + focus-visible:ring-1 ring-ring 于 calculator-dialog.tsx:138——本文件自身的同级族）→ 重建 → **GREEN 首试**。修复后普查复跑：聚焦档双方字节一致。
Pin-sanity 突变——第 138 行作用域的 focus token 回退。独立重建 + 全量 calculator 扫描：**唯一失败现场验证——1 失败 + 21 通过。** 恢复 + 全量重建 + 恢复后回归 **89/89 绿**（calculator 21 + dialog-buttons 17 + items 51）。
F5 交付链：快速门禁绿。4 分块 e2e：93+92+74+82 = **341 次执行 = 338 个唯一——一个已记录间歇性**（empty-states:85 夹具 GET 失败一次——第 2 次出现，由守卫精确诊断；隔离复跑 4/4；IPv4 修复下 not-found:111 监控绿）。Smoke 35/35 ✓。
日期类规律检查：v134 截图于 UTC 10 月 29 日捕获；现 UTC 10 月 30 日 → 模态的 todayIso 默认值偏移。捕获：**16/16——15 字节一致 + 07 确定性跨天日期类刷新**（种子日期表面字节一致——CONTINUING 工作空间未变种子）。
开发证据：dev-shots 脚本派生 v134→v135（仅版本替换）——**4/4 字节一致** + VLM 验证（菜单证明：/income，docSW 390，navLandmark true）。
D1–D7 对齐（D0 锚点先验证 1 命中）：AGENTS v135 段、CLAUDE 338 + v135 子句、README 计数 + v135 计划行、SKILL Session 170 行 + 状态行 108/338/35、PAD v1.1.92、探针 README 的 v135 节 + v136 队列（v130 时代的 NETWORTH + 钻取配对，第 12 次重跑——已对照 v130 计划 F3 验证 [12 项括号上的 ELEVENTH，v60 为原始；v130 shots header 携带完整形式]）+ 双闪烁监控，session_331.md（交付记录，推送后段落延后），worklog Session 170 条目。`.env.example` 验证未动。
变更集：41 文件（src/ 一行——REPAIR 形式，v129 以来首个 src/ 变更；tests/ +1 pin = 338 + 诊断守卫；配置 IPv4 钉）。奇偶校验提交 `2f44bc4` 已创建。
SSH 推送：密钥物化 + 指纹对照谱系验证（`4FSV1Pro...`——与 v129–v134 同一密钥）。**首次 dry-run 失败——包装器默认 --remote 为另一仓库；修正后的调用显式携带 --remote git@github.com:nordeim/zero-balance.git**（fetch 确认无分叉——origin/main @ 173b5e7，本地 HEAD 恰好快进一阶）。修正后 dry-run 干净（173b5e7..2f44bc4 授权），随后实际推送：**远端 main @ 2f44bc4 == 本地 HEAD**，HTTPS 复验逐字节一致，密钥已粉碎。
**v135 周期已完成并推送。** 编写 session_331 的验证段落（已填充）、session_332.md（本记录）+ session_333.md（转录记录）及最终推送。
