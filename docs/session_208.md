我将开始 zero-balance 仓库的审计-对齐-修复-推送工作流（v86 周期）。首先检查工作区状态。

工作区已被重置——执行全新克隆路径（v80 之后的第二次实践）：`git clone` 落在 `main @ 0d20198`（v85 已交付 + session_204/205 转录），树干净。

环境端到端重建：npm ci（354 包；npm 的 install-scripts 守卫拦截了四个 prisma/unrs 后安装脚本——经 `npm install-scripts approve` 批准，allowScripts 块由 npm 自身记录在 package.json）；写入 .env（DATABASE_URL="file:../db/custom.db"）；db/ 置于仓库根目录（db:push 同步 + db:seed）；安装 playwright chromium-1243；在 venv Python 上安装 paramiko 5.1.0。

核心文档已审阅（AGENTS.md、CLAUDE.md、README.md、PAD、zero-balance_SKILL.md——均为 v85 状态：288 e2e / Session 120 / PAD v1.1.42），随后审阅四份会话文档（session_204 + session_205、v85 修复计划、worklog Session 120 条目）。**v86 队列确认：v80 时代的储蓄对**（储蓄视图 @ 桌面 1280，上次重摄 v80，现为最旧候选 [v80 < v81 < v82 < v83 < v84 < v85]）——v85 计划的建议与轮换账本一致（连续第九次）；该对的第四次重跑 [v58 → v65 → v74 → v80 → v86]。

代码库审计（参照 skills/ 目录技能；skills/ 全程排除于检查/测试/编译）：v85 提交验证为 PIN-ONLY（20 文件，+1611/-6，零 src/ 变更）；其后两个提交仅会话日志。生产接缝全部干净（auth、db-path、SEO 对、Tailwind v4 缓解、三层测试）。Seedcheck 精确（7/1850/2235/0/3/2）。

**F0 基线链全绿**：lint ✓ · typecheck ✓ · 108/108 单元 ✓ · 构建 ✓（robots + sitemap 预渲染）· 290 次 e2e 分块执行（102+109+79 = 288 个唯一测试 = 文档化 v85 状态）· 35/35 冒烟 ✓。

**F1 axe 监视无漂移** ✓（npm 最新 4.14.0，仅 rc 预发布，无 5.x；v68 去重状态保持；引擎契约 pin 单独运行 2 通过）。

**F2 第 80 次常设检查全绿**：版本升级中发现**纯数字会话名 token 族**（ref79→ref80 / clone79→clone80——"79" 不匹配 "v79" 子串；v84 教训的第三个 token 族，本次捕获并修复），三族归一化后 diff 验证为纯版本升级。参考站四 bug 全部健在；数据普查第 80 次无漂移；克隆侧移动端菜单连续第 80 次验证正常；五视图 390 零溢出；SEO 对双端在线。

**F3 储蓄对第四次重跑**：v86 探针系列经 sed 从 v80 系列派生（版本 + 会话名/tmp 目录替换，grep 验证干净，头部历史注释修正为第四次重跑）。双侧截图（首次尝试即登录成功；指针停靠 (5,5)；参考站只读）。**VLM 判定为 IDENTICAL——该对五次截图史上首个非 DIFFERENT 判定**：旗帜列表全部限于预期的数据/身份类（副标题计数、卡片数字/名称/徽章、头像字母），零布局/样式旗帜。

**按 v75 惯例普查仍然运行**（arbit-v86.sh——无论判定如何普查必跑）：**v80 普查值精确复现——每一轴零漂移**（页头、网格 960/16px/~309 模板、卡片盒 + v70b 换行类 [ref 200 vs clone 230]、储蓄蓝点 titleRow、金额叶、页脚 + 徽章 chrome + v58/v57 类、docSW 1280）。**无新差距——v86 为 PIN-ONLY。**

**F4 pin**（+1 e2e = 289）：覆盖图走查——v51 F3 仅在 390 固定储蓄副标题的 fs/color；Rent 卡测试仅在 390 固定费用侧孪生；**任何视图都不存在 1280 副标题 pin**；headerRow 自身几何从未在任何视口固定；v85 wrapper pin 覆盖费用（96px）+ 收入（0px）但从未覆盖储蓄孪生。pin 自身轴先经补充双侧普查（wrapper-arbit-v86.sh——v84/v85 一次性先例）测量：**双侧全部字节一致**（wrapper {block/flex-1/pr 0px/w 231/h 48} + 副标题 P {h 20/fs 14px/lh 20px/灰/mt 0} + titleRow mb 4px + headerRow {flex/space-between/flex-start/h 48/mb 12px}；"Home Savings" vs "Index Funds" 为数据类）。修复计划 v86 先于执行写好并对照代码库验证。

pin 追加至 items.spec.ts——**首次运行即 GREEN**。**pin-sanity 变异——三个候选，一个执行，两个被驳回**：
(1) 朴素 fs 轴变异（text-sm → text-sm lg:text-[15px]）级联自由检查失败——失败差异翻转 fs + lh（20→21.43px）+ h（20→21），完整 items.spec.ts 运行中 v80 高度 pin 也变红（[230,230]→[254,254]）；生成 CSS 中找到根因：**.text-sm 计算 line-height: var(--tw-leading, var(--text-sm--line-height))，其中 --text-sm--line-height 存为无单位比率 calc(1.25/0.875) ≈ 1.42857——任何字号覆盖都会等比缩放行高**（纯 lg:[font-size:15px] 任意属性形式同样被驳回）；
(2) 类型作用域条件扩展（v85 模式，翻转储蓄 wrapper 的 paddingRight 0→96）同样失败——pr-96 将内容盒收窄至 137px，Emergency Fund h4（~125px @16px/600）换行（+24），单行网格拉伸两卡至 254；
(3) **执行形式——视口作用域响应式变体闪避**（headerRow 的 items-start → items-start lg:items-center @ item-card.tsx:118，v80 模式应用于兄弟行）：独立重建 → pin 精确失败于 headerRow.alignItems 轴（"flex-start"→"center"）→ 变异下完整运行 **38 绿、仅 v86 pin 红**（响应式变体在 390 惰性；居中在 1280 不改变任何高度——行高保持 max[48,36]）→ 恢复（git diff src/ = 0 行）→ 重建 → **39/39 绿**。

**F5 全链重跑全绿**：lint ✓ · typecheck ✓ · 108 单元 ✓ · 构建 ✓ · **289 e2e**（102+110+79 = 291 次执行 = 289 个唯一测试，零抖动）· 35/35 冒烟 ✓。16 张截图重新生成并字节对比：**10/16 字节一致 + 6/16 良性像素仲裁**——pixel-diff-v86.mjs 将每个差异定位到窄带；crop-diff-v86.mjs + vlm-arbit-crop-v86.mjs（单图读取，v85 纪律）仲裁五个 DATE-TEXT-ONLY（03/04/05/06/16——新种子 isoDate() 偏移比已提交集的种子晚一天：日期数字 +1，chrome 字节一致）和一个栅格化噪声（08-calculator：55×74 带内 1077 差异像素，每个差异像素恰为实心渐变的单通道 ±1——无文本[计算器对话框不渲染日期]、无布局、双侧裁剪 VLM 读取一致）。按 v80 纪律重新生成的集合交付。最终 seedcheck 精确。

**D1–D7 文档对齐**：D1 AGENTS.md（v86 段落）· D2 CLAUDE.md（289 + v86 pin 条款）· D3 README.md（计数 + v86 计划表行）· D4 zero-balance_SKILL.md（Session 121 审计行 + 状态行）· D5 PAD v1.1.43 修订块 · D6 探针 README v86 小节（五个新教训）· D7 session_206.md + worklog Session 121 条目。

**交付**：每个新文件落地后重跑清洁检查门（lint ✓ typecheck ✓）；test-results 清理；无孤立服务器；git diff src/ = 0（PIN-ONLY ✓）；.env.example 已跟踪且匹配；package.json 的 allowScripts 块（npm 自身记录的已批准安装脚本）随新鲜克隆可复现性交付。paramiko shim 部署于仓库外 /home/z/my-project/bin/ssh；操作员密钥写入（0600）并验证（ed25519，指纹 SHA256:3ddaNlFhMz1JXiGEDgVEaRsUzI4Ev0IpGEEB7NnU4PU——与文档化的 v84/v85 指纹一致）。提交 `858ad21` 创建（27 文件，+1500/-5）。带显式 --remote 标志的 dry-run 推送成功（fast-forward 0d20198..858ad21）→ 真实推送成功 → **远端验证 `main @ 858ad21 == local HEAD`**，追踪 ref 同步，wrapper 临时密钥销毁，操作员密钥销毁，树干净。

**v86 周期完成并推送**——`main @ 858ad21`（远端已验证、密钥已销毁、树干净）。

本次核心成果：
- **审计**：重置工作区上 F0 基线全绿（全新克隆路径端到端重建）
- **第 80 次常设检查**：移动端菜单连续第 80 次验证正常；版本升级中捕获纯数字会话名第三 token 族
- **储蓄对第四次重跑**：**五次截图史上首个 IDENTICAL 判定**，普查仍按 v75 惯例运行并精确复现 v80 值（零漂移）
- **+1 pin（289 e2e）**：储蓄卡片副标题 P 全 chrome + 带副标题算术 + wrapper 第三腿（完成 v85 pr 条件三部曲）
- **两个被驳回的变异候选留档为教训**：v4 比率行高陷阱（text-* 行高为字号相对比率——fs 变异必然级联高度）与收窄内容换行级联（pr 变异须对最长文本在收窄宽度下核验）
- 10/16 截图字节一致 + 6/16 良性像素仲裁（5 个 DATE-TEXT-ONLY + 1 个栅格化噪声）；D1–D7 文档全对齐

**建议下一步**：运行 v87 周期——队列指向 v81 时代的登录 + 计算器对（登录视图 + 计算器对话框 @ 桌面 1280，上次重摄 v81，现为最旧候选 [v81 < v82 < v83 < v84 < v85 < v86]），按协议先对照轮换账本验证。
