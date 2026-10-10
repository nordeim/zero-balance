I'll continue with the zero-balance project task. Let me first check the current workspace state and then proceed through the phases.
The workspace exists from the previous v32 session. Now starting the **v33 iteration** — the recurring comprehensive remediation workflow. Let me create the task plan and begin.
`git pull` brought in a new `docs/session_67.md` (144 lines). Let me read the session chain and latest docs.
`docs/session_67.md` is the v32 session transcript with suggested next surfaces: **line-item sub-dialog focus traversal, signup/email-verification focus rings, toast focus semantics, Lighthouse/bundle-size**. Let me review the remaining context docs.
Now let me read the latest context docs — session_66.md (v32 formal log) and remediation-plan-v32.md.
I have the full v32 context. Now let me quickly validate the core docs and environment state in parallel.
Environment intact from v32 (node_modules, .env, db/, docs all aligned). Now let me check the skills catalog for this session's audit work.
技能目录已确认 —— `agent-browser`、`tdd`、`tailwind-patterns` 以及探针基础设施都是此会话的工具链。第一阶段已完成。现在进入**第二阶段：基线审计链**。我来检查一下探针基础设施并启动该链。
scandihaven 引用克隆已丢失（工作空间已部分重置）。我来重新克隆它，并并行启动基准审计链。
Lint ✓ · Typecheck ✓. Now unit tests + build.
Build ✓ (robots + sitemap prerendered). Now the 165-test E2E suite.
**Baseline chain GREEN on first full run: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ · 165/165 e2e ✓ · 35/35 smoke ✓.** Now the audit phase — npm audit + secret scan.
Audit clean — same 5 documented dev-only advisories, secret scan matches only documented dev files. **Phase 2 complete.** Now Phase 3 — the two-site parity sweep. Let me check the probe toolchain first.
工具链完好。现在开始进行双站点扫描。**第 1 步：使用 `agent-browser` 登录参考站点。**
Logged into the reference dashboard. **Standing check 1: data drift census (27th).**
**Data drift clean (27th)** — allocation 30.5%, Balance $3475.00, Income $5000.00, Savings $1000.00, Expenses $525.00. Now **mobile-nav R1–R4 (27th)** — the task's priority check.
Now running the mobile-nav standing checks on the reference — set mobile viewport and run R1 (burger hit test).
**R1 confirmed (27th)** — reference burger blocked by `DIV.fixed.top-0.z-[100]` (toast container, standing bug), scrollWidth 395. Now R2 — open sheet, nav, check the trap.
Sheet open (structure detector: panel + body lock + 3 overlays). Now click a nav link and check the trap.
**R2 confirmed (27th)** — reference sheet traps after nav (still open + body locked on /income). Now close the sheet and run R3 (active nav on `/`) + R4 (per-route overflow).
**R3 confirmed (27th)** — no nav landmark, nothing active on `/`. Now R4 (per-route overflow, 6s settle discipline).
**R4 confirmed (27th)** — reference overflows 395 on `/`+`/dashboard`, 464 on `/networth`. All four mobile-nav checks verified on the reference. Now the **SEO pair** — reference endpoints + head census.
Reference SEO census captured. Now boot the clone parity server and run clone-side standing checks + SEO pair.
SEO pair confirmed. Now the clone-side standing checks — checking the established clone probe pattern first.
**Clone-side standing checks (27th) all clean** — R1 direct hit, R2 sheet closes (superset), R3 landmark present, R4 all routes fit 390. **The clone's mobile menu works — Tailwind v4 pins hold.**

Now the **session-67 suggested surfaces**. Surface #1: the line-item sub-dialog's focus traversal. Reference first — open the calculator's "Add Item" sub-dialog.
Calculator open. Now click "Add Item" to open the line-item sub-dialog.
The sub-dialog structure captured — 6 text fields, amount, date pickers, Cancel/Save. Now the strict focusable census + REAL Tab walk on the reference.
Census captured — 13 stops in DOM order (X → Name → Amount → Frequency dropdown → Provider → Policy → 2 native date inputs → Payment → Status dropdown → Notes → Cancel → Save). The overlay is a plain `fixed z-[60]` div. Now the **initial focus** + **REAL Tab walk** on the reference.
Programmatic focus isn't a REAL Tab (the v25 lesson). Let me use the CLI's real key presses instead.
Odd — T1 landed on a submit button "outside" my detected overlay. Let me debug the overlay detection vs actual focus location.
焦点位于 `z-50` 计算器对话框内的 “Add First Item” 按钮。让我追踪一下子对话框的 `h2` 祖先路径，以找到其真实的容器。
The sub-dialog is a z-[60] sibling overlay; focus stayed on the "Add First Item" trigger after opening (no auto-focus). But the REAL Tab press didn't move focus — let me verify the keypress routing directly.
Tab works now — X → Item Name. The earlier read was a race. Let me run the full walk — continue from Item Name through all 13 stops and beyond.
Tab 遍历了 **8 次日期输入停止** (T5–T12) —— 原生的 date-input 片段行为。让我统计一下实际的 DOM 日期输入并继续遍历直到结束。
**已测量参考子对话框契约：**
- 鼠标打开时无自动聚焦（焦点保持在触发器上）
- Tab 顺序 = DOM 顺序：X → Name → Amount → Freq → Provider → Policy → **8 个日期分段停靠点**（2 个原生日期输入 × 4 个分段） → Payment → Status → Notes → Cancel → Save
- **无捕获 (No trap)** — Save 之后的 Tab 键会移出子对话框（普通的 div 行为）

现在，在进行克隆端比对之前，让我先检查一下克隆源中子对话框的表单结构。
The clone's field order matches the reference exactly (native date inputs, same 13-stop census). Now the clone-side walk — REAL Tab presses inside the parity server.
**Surface #1 verdict: NO parity drift** — identical 13-stop census, identical Tab sequence (X → Name → Amount → Freq → Provider → Policy → 8 native date segments → Payment → Status → Notes → Cancel → Save). The two deltas are the documented Radix supersets (auto-focus X on open, trap wrap). Now the focused-chrome pair check on the sub-dialog fields.
Reference Save shows the standard shadcn family. Now land on the Status select trigger — the one control class not yet chrome-paired (Radix SelectTrigger vs reference plain button).
所有字段上的 Focus 系列是一致的。让我直接从 DOM 中获取 reference 的 Frequency/Status 触发器类（即待比较的控件），并检查 clone 的 SelectTrigger 源码。
The clone's SelectTrigger carries `focus:outline-none focus:ring-1 focus:ring-ring`. Now the empirical pair — REAL Tab onto the reference's Frequency trigger, settle, read chrome.
Unexpected landing — let me check what dialogs are actually open now.
The sub-dialog never closed — the reference's plain-div dialogs don't respond to Escape. Focus is on Notes; one Shift+Tab should land on the Status trigger.
**Reference Status trigger family measured**: `outline: solid 2px rgba(0,0,0,0)` + 1px #0a0a0a ring (the shadcn select-trigger family). Now the clone-side twin measurement — boot the parity server, walk to the Status trigger with REAL Tab.
**FINDING (G1 candidate)** — the clone's SelectTriggers render NO visible focus ring under REAL keyboard focus (all-transparent shadow), while the reference renders the 1px #0a0a0a ring. Same drift class as v32's G1. Let me deep-probe to root-cause before concluding — ring vars + a known-green control in the same page.
**Surface #1 extension: NO finding** — the deep probe shows the ring IS present: `--tw-ring-shadow: 0 0 0 calc(1px+0px) #0a0a0a` renders as the 4th box-shadow layer (`rgb(10,10,10) 0 0 0 1px`). My first read was truncated at 85 chars, cutting off the ring layer — a probe lesson (read the FULL shadow string; v4 puts the ring 4th). 

Now **Surface #2: the register/verify-email focus-ring families**. Reference first — open /register.
/register 404s — the sign-up entry is via the login page's "Sign up" link.
The sign-up state is on /login. Let me measure the register inputs' focus family with REAL Tab, then create a throwaway account to reach the verify-email state.
Reference register input: `ring-2 slate-400 + white offset-2` family (v13-pinned on the clone). Now submit a throwaway registration to reach the verify-email state.
The verify state is live — 6 code inputs + Verify + Resend. Now the REAL Tab focus measurement on the code inputs.
Reference code inputs: **2px zinc-950 (#09090b) ring family, 40×44 geometry, first input auto-focused**. Now check the clone's verify-email component source.
**发现 (G1 — 界面 #2)**：克隆的代码输入框带有 `focus:border-[#94a3b8] focus:outline-none` —— **没有 ring** —— 而参考实现渲染了一个明显的 **2px zinc-950 #09090b ring** (`rgb(9,9,11) 0 0 0 2px` + 白色前导)。让我补全参考实现的聚焦边框并验证克隆端的在线实时数据。
Reference code-input family complete: border stays **#e4e4e7 (no tint)** on focus, ring = 2px #09090b. Let me confirm focus state + the resting border, then the Verify/Resend buttons.
The walk hit "You need to enable JavaScript" — that's hidden noscript content or a page change. Let me check the current page state.
页面仍然是 `verify` 状态 —— 刚才的遍历跑到了隐藏的 `noscript` 元素上。让我清理一下：从最后一个 `code input` 使用 `Tab` 键移动一次，跳到 "Verify email" 提交按钮。
**Complete reference families measured:**
- Verify submit: white-2px + zinc-4px ring (v25-pinned, clone matches)
- **Resend: browser-default `outline: auto`** — raw button, no focus classes
- **Code inputs: 2px zinc-950 ring, border untinted — the clone LACKS this ring (G1)**

Let me check the clone's Resend button implementation before writing the plan.
Clone's Resend matches the reference (raw button, no focus family — browser default). Let me verify the reference's "Back to sign in" button family to complete the surface.
**G1 confirmed as the only drift in Surface #2.** One more check — does the clone auto-focus the first code input like the reference does?
无 `autoFocus` —— clone 缺少 reference 的首次输入 `auto-focus`（这是 `G1` 修复的一部分）。现在进行 **Surface #3: toast focus semantics**。Reference 的 `toast` 容器一直都在 `DOM` 中（即 R1 blockers）—— 让我来检查一下它们的语义。
No toast containers on the login route. Let me re-login to the standing account and inspect on `/`.
Back on `/` as the standing account. Now inspect the toast viewports + trigger a live toast.
Two plain-div viewports — no role/aria-live, `pointer-events: auto` (the R1 root cause). Let me check the first viewport's child and trigger a live toast via the calculator add cycle.
嵌套的 viewport div，无语义。现在通过 calculator add-item 循环触发一个实时 toast（v32 precedent）。
No toast on line-item save. Let me delete the probe item (cleanup anyway) and read the toast state immediately — the delete action may toast.
No toast on delete either. Let me check the probe history for the reference's live-toast evidence + the clone's toast implementation.
The clone's toast is Radix-based (role=status/aria-live built-in). Let me try the reference's item-edit save (same values — no mutation) to observe a live reference toast.
Reference shows no toasts on these flows — its viewport is semantic-less. The clone's Radix toast (role=status + aria-live) is the documented superset. Now **Surface #4: Lighthouse/bundle-size** — resource census on both sites.
No Lighthouse CLI — I'll do a network/transfer census via agent-browser instead. Reference first.
Reference: **1.06MB raw JS (317KB gz) + 68KB CSS + 214KB dev badge**. Now the clone's dashboard-load census on the parity server.
Toast live-region read came back empty and the cleanup lost the calculator — need to check the dev DB state and re-verify the toast. Let me check if the "Perf Probe" item persisted.
DB is clean (0 line items — the perf-script save never landed; the calculator chain broke silently). Let me verify the parent amounts, then re-run the toast probe properly.
The model uses `category`, not `name`. Let me fix the check.
Dev DB clean (2235 total, 0 line items). Now a focused toast-semantics probe with assertions at each step.
The sub-dialog probe used the wrong selector for the Radix dialog (needs `[data-state=open]`). Fixing and re-running.
Toast measured: `<li>` with **no role/aria-live** (an a11y gap — no screen-reader announcement) though tabindex 0 + visible. Now clean up the "Toast Probe" fixture via direct DB (the v32 precedent).
Restored Entertainment to the wrong value (category is 'Entertainment', subcategory 'Streaming'). Fixing.
Dev DB restored (2235 total, 0 line items ✓). The sweep is complete. Now the **VLM pairwise** (the standing discipline — two fresh pairs), then the remediation plan. Let me check the VLM compare tooling.
Now capture the VLM pairs — dashboard + verify-email state (this session's surface). Reference side first.
Reference shots captured. Now the clone side — dashboard + verify state inside the parity server.
All four shots captured. Running the VLM pairs.
The clone shots were captured at the stale mobile viewport (the default session persisted 390px). Re-capturing at 1280×800.
**Both VLM flags DOM-explained** (dashboard: the active-nav rail = superset #3; verify: the dev-code hint box = the documented no-mail dev variant). Cleaning up the clone's probe users now.
Sweep complete — both VLM flags DOM-explained, DB clean. **Phase 4: remediation plan + TDD.** Let me check the existing spec structures for the new tests.
The e2e comments mention a Radix "role=status mirror" — but my live probe found only the li. Let me dump the viewport's full DOM while a toast is live to settle it.
Empty-save was blocked by native `required` validation — no toast. Let me use the successful add-item path and dump the DOM with the toast live.
The full architecture: the li has NO role/aria-live AND the whole region carries `aria-hidden="true"`. Let me check the installed Radix toast source for the announcer/mirror behavior.
Radix DOES announce — a hidden portal with role=status + aria-live that unmounts after 1s (my probe timing missed it). Let me verify empirically within the 1s window.
**确认了** —— Radix announcer 存在：`role=status, aria-live=assertive, "Notification Line item added"`（隐藏，1秒窗口期）。**S1 降级为：无发现问题** —— clone 的 toast 语义是已记录的 Radix 超集。完整的变更集是 **一个修复（G1：code-input focus family + auto-focus）**。让我检查一下 calculator spec 以确定 announcer 的位置。
完整技术方案已确定。现在开始编写 **修复计划 v33** —— 唯一的生产环境代码修复（G1）加上播报器（announcer）锁定。
Plan written and validated. **TDD Step 1 — G1 RED**: the failing focus-family test.
Now run the RED phase — the test must FAIL against the drifted build.
**RED confirmed.** Now GREEN — apply the fix to the CodeInputs.
**G1 GREEN.** Now pin-sanity mutations — remove the shadow family, expect FAIL.
Mutation 1 confirmed. Restore + Mutation 2 — remove autoFocus.
Mutation 2 confirmed. Restore and verify GREEN.
**G1 complete.** Now **S1: the announcer pin** in the calculator's line-item-add test.
S1 pin GREEN. Now its pin-sanity — simulate a toast rewrite dropping the announcement (plain `li` instead of Radix Root), expect FAIL.
Pin-sanity confirmed — the plain-li toast fails the pin. Restore and verify GREEN.
**TDD complete.** Now the full chain re-run.
**FULL CHAIN GREEN: 108 unit · 166 e2e · 35 smoke.** Now the live re-verification on the parity server.
**Live-verified byte-identical**: Digit 1 auto-focused, the focused Digit 2 renders `rgb(9,9,11) 0px 0px 0px 2px` (the 2px zinc ring) + untinted border — matching the reference's measurement modulo v4's invisible zero-width lead layers. Mobile spot check clean. Now clean up + regenerate the 16 screenshots.
Two issues: 2 leftover probe line items under the demo user + the screenshot run timed out. Let me clean the DB first, then check the capture script.
All 16 screenshots regenerated. **Phase 5: docs alignment.** Let me check each doc's current state.
Now updating all docs. **README first** — the v33 table row.
README done. Now **CLAUDE.md** — the count and the v33 surfaces.
Now **AGENTS.md** — the v33 verification paragraph.
Now **zero-balance_SKILL.md** — the state + session row.
Now **docs/session_68.md** — the formal session log.
Now the **repo worklog.md** — the Session 65 entry.
Now the **probe README** — the v33 catalog.
The header naming follows the v32 convention (the plan reference disambiguates). Now the workspace worklog + final changeset verification.
The changeset is clean. Let me check the full untracked list and remove the superseded/misleading probe.
Final verification gate — lint once more (the new probe files), then the workspace worklog.
**Phase 6: commit + push.** Let me check the SSH wrapper instructions.
The wrapper procedure is clear (with the `--remote` flag for zero-balance). Now the commit.
Committed `07d890c`. Now the SSH wrapper push — key setup + shim check.
Shim ready. Now materialize the operator key and run the fingerprint sanity check.
Dry-run clean — fast-forward `3818922..07d890c`. Now the real push.
**已推送到 main — 远程验证 `07d890c` == 本地 HEAD，密钥已销毁，工作树干净。** 迭代 v33 已交付。
**一致性迭代 v33 已交付至 `main` 分支（提交 `07d890c`，已通过远程验证）。**

## 本次会话交付的内容

**环境与基准** — `git pull` 引入了 session-67 的记录；v32 环境完好；在首次完整运行中，整个链条全部通过（显示为绿色）：lint ✓ · 类型检查 ✓ · 108 个单元测试 ✓ · 构建 ✓ · **165 个端到端（e2e）测试 ✓** · 35 个冒烟测试 ✓；审计通过。

**常规检查（第 27 次，全部通过）** — 移动端导航 R1–R4 在两个站点上均正常（**克隆端的移动端菜单正常工作 — Tailwind v4 锁定规则依然生效**；参考站点中 R1 toast-blocker/R2 sheet-trap/R3 无地标/R4 溢出等问题仍作为证据进行记录），数据漂移正常，SEO 一致，VLM 对成对干净（DOM 属性说明）。

**Session-67 建议的界面**：
- **行项目（Line-item）子对话框焦点遍历 — 无发现**：13 个停靠点统计 + 真实的 Tab 键遍历在两个站点上字节完全一致（包括原生日期片段的停靠点）
- **注册/验证邮箱（verify-email）焦点系列 — G1（唯一漂移）**：参考站点的 40×44 代码输入框渲染出 **2px 锌-950 色环 + 无边框着色 + 首个框自动聚焦**；克隆端之前使用了带有无色环的板岩色（slate）调色。已通过 TDD 修复（红→绿→2 个变异）
- **Toast 焦点语义 — 无发现**：测量并固定了克隆端的 Radix 隐藏 `role=status / aria-live=assertive` 广播器；记录了捆绑包一致性（338KB 对比 317KB gz + 一个 214KB 的开发徽章）
- **探测（Probe）经验**：v4 将可见的选中环隐藏在第 4 个 `box-shadow` 层中 —— 截断读取会误报缺失

**最终状态**：108/166/35 全部通过（显示为绿色），16 张截图，文档对齐（`docs/remediation-plan-v33.md`，`docs/session_68.md`，README/CLAUDE/AGENTS/SKILL/worklog），已通过 SSH 封装器提交并推送。

**下一步**：建议的未测量界面 —— 忘记密码/重置焦点遍历、计算器频率 Select 列表框键盘协议，或 API 错误层级审计。重新发布引用 `docs/session_68.md` 的简介，我将从那里继续。
