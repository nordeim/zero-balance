# Session 114 — the v49 session's raw tool-call narrative (2026-10-12)

The condensed transcript of the session that delivered
`docs/remediation-plan-v49.md` (parity iteration v49 — the login
panel's mobile-only &nbsp; spacer FIX + the donut legend's mobile
reflow pin + the calculator dialog's 640 chrome pin).

I'll start by refreshing the workspace via git pull (or re-cloning if
reset). The workspace is intact — the pull fast-forwards c02dd1b →
0bf89ce (session_112.md arrives). Now the docs check + the TODO plan.
The five core docs reviewed (AGENTS' v48 paragraph / CLAUDE's state /
README / PAD v1.1.5 / the SKILL doc's Session 83 row) + the four
session docs (session_111 + remediation-plan-v48 + the repo worklog
Session 82 + session_112). Now validating the understanding against
the codebase: the 22 spec files, the v48 pins (item-details 10 /
dialog-buttons 17 / empty-states 8), the .env contract, the db/
folder, the sitemap/robots pair, the vitest/playwright configs.
Environment intact — straight into the baseline chain.
Lint ✓. Typecheck ✓. 108/108 unit ✓. Now the build (robots +
sitemap prerender).
Build ✓. Now the 229 e2e (killing the agent-browser daemons first —
the v46 lesson).
**229/229 e2e ✓ (5.3m).** Now the smoke test to complete the chain:
**Baseline chain GREEN: lint · typecheck · 108 unit · build · 229 e2e
· 35 smoke.** Now the audit — npm audit (the same 5 dev-only), the
secret scan (clean), the env parity (≡ modulo AUTH_SECRET), the v48
diff (ZERO src/ changes — the pin-only contract held).
Now the 43rd standing checks — the reference side first
(ref-standing-v49.sh, persisted). Login submitted. R-bug 1
(toast-blocker): the hit is `DIV.fixed top-0 z-[100]` —
hitIsBurgerChild false. R-bug 2 (sheet-trap): my heuristic detector
reads sheetOpenAfterNav false — that contradicts the standing record;
re-verifying with the precise overlay census. The sheet IS open (the
z-50 rgba(0,0,0,0.8) scrim, w 390, empty text). Clicking the income
link inside the sheet. Path /income + the overlay STILL open —
**R-bug 2 confirmed live** (the heuristic's text-keyed detector was
the artifact; the z-index+geometry census is the proof). R-bugs 3+4:
navLandmark false, /networth docSW 464. The data census read-only
("1 items · $25,000" / "1 items · $5000.00"). The SEO pair live.
Closing the reference sheet (Escape). Now the clone side
(standing-checks-v49.sh via with-server).
**The 43rd standing checks ALL PASS** — R1 the burger hit direct +
the sheet opens, R2 the sheet closes on nav, R3 the landmark, R4 docSW
390 on all five routes, the SEO pair. Now the v49 sweep — the three
queue candidates, the reference side first (ref-v49.sh).
REF surface 1 (the login panel at 390, logged out): w 358 / h 682 /
y 57 / radius 16 / the 2xl visible layer / bg rgba(255,255,255,0.95) /
contentPad 32 / heading 24-700. Interesting — y 57 is NOT the
geometric center (81 would be); something else is in the flow.
Logging in for surfaces 2+3. REF surface 2 (the donut legend at 390):
the container flex/gap 12/mt 24/w 313, the row 313×64/8px/12px/
rgb(245,248,245), the dot 16/4/rgb(224,122,59) — but my amount/percent
finder grabbed the PARENT (the text read "$6025.0092.3%" — the
concatenation). Re-measuring with leaf-node targeting.
The leaf census: the SPAN "Need" 16/500/rgb(26,58,46); the P "$6025.00"
16/700/rgb(224,122,59); the P "92.3%" 12/400/rgb(107,114,128); the
container flexDirection column; the right block ta right; the svg 16/
rgb(224,122,59). Now REF surface 3 (the calculator at 640): the
Calculate click → the panel w 608/h 515/x 16/y 223/radius 16/maxW
768px/maxH 816px/the 2xl visible layer/bg white/overflow hidden/the
close 36×36/the header border-b 1px rgb(229,231,227)/sw 640. Closed
via X. Now the clone side (clone-v49.sh via with-server).
CLONE surface 1: w 358 / h 682 / radius 16 / the same 2xl visible
layer (the 5-slot construct) / bg / contentPad / heading — IDENTICAL
except **y 81** (the reference y 57). Investigating the reference's
layout: the main is flex/center/p-4 on both — but the reference's
wrapper is 730 tall vs the clone's 682. Census the wrapper's children.
**FOUND THE DRIFT** — the reference's wrapper has TWO children: the
panel + a `mt-8 text-center text-xs text-slate-400 sm:hidden` div
(h 16, y 771, EMPTY text). The clone has ONE. Inspecting the div's
innerHTML: `<p>&nbsp;</p>` — a bare non-breaking space line. At 640:
display none (sm:hidden), the panel re-centers to y 111. Verifying
the spacer exists in the sign-up state too (the state swap is
read-only).
Sign-up state: the wrapper 470 = the panel 422 + 32 + 16, y 187 —
the spacer is a panel SIBLING, every auth state carries it. Now the
clone's login-card structure: line 555 the `w-full max-w-md` wrapper,
the panel its only child — the insertion point identified. CLONE
surface 2 (the donut legend): byte-parity on every leaf (the row w
308 vs 313 = the reference's own 395 docSW overflow — the
superset-fix-#4 family). CLONE surface 3 (the calculator): the panel
w 608/h 515/radius 16/maxW 768px/maxH 816px/the SAME visible shadow
layer (the clone's `.zb-modal-panel` emits it directly — no leads)/
the close 36×36/the header border — byte-identical.
All three surfaces resolved: F1 a REAL production fix (the first
since v46), F2 + F3 pin-only. Writing the plan.
`docs/remediation-plan-v49.md` written + validated. Now the TDD
execution — F1 written RED FIRST. Running it against the pre-fix
build.
**F1 RED ✓** (the spacer absent — `{ present: false }` fails the
census). Now applying the production fix (the spacer added, the color
pinned as `text-[#94a3b8]` — the v4 oklab trap), the rebuild.
**F1 GREEN ✓** (the wrapper 730, the panel y 57, the spacer census
byte-exact, the 640 re-check). Now F2 (the dashboard legend pin — the
"Spending Breakdown" title is a plain div, `getByRole("heading")`
would fail; fixing to `getByText` + the v42 settle idiom) + F3 (the
calculator chrome pin).
**All 3 v49 pins GREEN** (F1 + F2 + F3). Now the S1 mutation sanity
— six mutations, each with the standalone REBUILD. Mutation (a) is
the TDD RED run itself (the pre-fix proof). (b) mt-8→mt-4 → **F1
FAILS** (the wrapper 730→722). Restoring + (c) removing sm:hidden →
**F1 FAILS** (the 640 sub-check). Restoring + (d) the legend row p-3
→ p-2 → **F2 FAILS** (pad 12→8, h 64→56 — and the git diff confirms
no collateral: only the legend row). Restoring + (e) the
zb-modal-panel shadow commented out → **F3 FAILS** (no 2xl layer).
Restoring + (f) the calculator's 85vh → 90vh → **F3 FAILS** (maxH
816→864). All six restored — the git diff shows ONE file
(login-card.tsx, +14 lines: the F1 fix).
Now the full verification chain — the rebuild + the complete gate.
**232/232 e2e ✓ (5.3m — 229→232).** The smoke test: **35/35 ✓. Full
chain GREEN.** Now the VLM pair — the LOGIN page at 390 (THE FIXED
SURFACE). Capturing the reference shot… the screenshot didn't land —
the agent-browser syntax is `screenshot [selector] [path]`; my
`screenshot <path> full` parsed the path as a SELECTOR. Re-capturing
with `screenshot body <path>`.
Both shots captured. Running the VLM compare (vlm-compare-v49.mjs).
**VLM VERDICT: IDENTICAL** — zero app flags (the only flag the
reference's own "Edit with Base44" FAB). The F1 fix visually
verified. Now the 16 screenshots (the capture script).
16 screenshots regenerated. Now the D-series docs alignment — AGENTS
(the v49 paragraph), CLAUDE (three v49 entries + the 232 count — the
first calculator-anchor replacement missed, re-anchored), README (the
v49 row + the counts), the SKILL doc (the Session 84 row + the state
line), the PAD (the v1.1.6 block), the probe README (the v49 section
+ the five lessons), session_113 + session_114 + the repo worklog
Session 83 + the ledger list + the workspace worklog.
Docs aligned. Now the final verification before the commit — git
status + the ignore rules. Then the SSH wrapper push sequence.

## 本次会话概要

**会话链**：git pull（0bf89ce，工作区未重置——首次免重建会话）→ 基线链全绿（108/229/35）→ 审计净（src/ 零变更）→ 第 43 次常规检查（参考站四 bug 在线——sheet-trap 用精确 overlay census 复核；克隆 R1–R4 全过）→ v49 三表面双站实测（发现一个真实移动端差距）→ 计划（1 修复 + 2 pin）→ TDD（RED→修复→GREEN；六突变全咬合）→ 全链（108/232/35）→ VLM 登录对 IDENTICAL → 交付。

**核心发现**：参考站登录页的 `w-full max-w-md` wrapper 在移动端携带第二个子元素——`<div class="mt-8 text-center text-xs text-slate-400 sm:hidden"><p>&nbsp;</p></div>`（h 16、mt 32、#94a3b8、空内容）——把卡片堆栈从几何中心上移 24px（面板 y 57 vs 克隆修复前 y 81）。v12/v13 的登录 pin 均在桌面测量（sm:hidden 在那里隐藏 spacer）；v24 移动端普查只走了控件——390 首测捕获。这是 v46 以来第一个生产代码变更（+14 行）。

**其余成果**：donut 图例 390 移动端重排 pin（v44 实测过双视口但只 pin 了 1280；行宽 313 vs 308 = 参考站自身 5px 溢流）；计算器 640 chrome pin（v45 F2b 只 pin 过宽度；`.zb-modal-panel` 直接发射可见层——零 lead 的已接受类）；probe 目录新增 5 个文件（双驱动 + 双侧常规检查 + VLM 对）。

**建议下一步（v50 队列）**：注册/忘记密码状态的完整 390 census、净资产的 640 视口 tablist chrome、仪表盘 hero 移动端重排的完整 census——或任选新表面；toast 的参考站 census 仍留待数据变更被授权的会话。
