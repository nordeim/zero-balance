I'll start by internalizing this complex task. Let me first set up my task plan, then check the workspace and get the repo.
The workspace has been reset. Let me clone the zero-balance repo first.
仓库已克隆。现在我来阅读关键文档，以了解项目。
The repo is at iteration v30. Now let me read the key documents. Given their size, I'll read them strategically.
Now let me read the session docs the user specifically asked about: session_61.md, remediation-plan-v30.md, worklog.md, and session_62.md.
我现在已经清楚了情况——这是 parity iteration v30 之后的成熟项目（已交付 session 61）。我本次的任务是延续该模式：**parity iteration v31**。让我检查一下环境状态并阅读剩余的关键文档。
工作区已完全重置 — 没有 node_modules、.env、db/ 或 scandihaven。我来重新构建环境（同时安装依赖项），并阅读其余的关键文档。
在安装过程中，我先来阅读一下 AGENTS.md 和技能目录。
Now let me check the skills catalog and the SSH push instructions.
npm install 和 scandihaven 克隆已完成。现在让我来设置数据库并验证应用是否能正常运行。
Database seeded. Now let me validate the codebase structure against the docs.
所有基础设施已确认就绪。现在让我运行基准审计链（阶段 1：lint + typecheck + unit tests）。
Lint, typecheck, and 108/108 unit tests all green. Now the production build.
Build green with robots.txt + sitemap.xml prerendered. Now the e2e suite (161 tests).
**Full baseline chain GREEN on first run**: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots+sitemap) · 161/161 e2e ✓ · 35/35 smoke ✓. Now Phase 2 audit (npm audit + secret scan).
Audit clean — same 5 dev-only ESLint advisories (accepted, no patched release), secret scan matches only documented files. Now let me study the probe tooling and check the agent-browser skill.
I have full understanding of the tooling patterns. Now let me start the two-site sweep — first, login to the reference site.
The password was mistyped — `$` belongs at the start (`$Abcd1234`). Let me retry.
Logged into the reference dashboard. Now let me run the standing checks — data drift census first (25th).
Data drift clean (25th) — identical to v30 census. Now mobile-nav R1-R4 on the reference (25th consecutive check).
R1 confirmed — the reference's toast container still blocks the burger (25th). Now R2: sheet trap after nav.
R2 confirmed — the reference's sheet+overlay still trap the user after nav (overlay open, body locked). Let me capture evidence and close the sheet, then run R3/R4.
The trapped-sheet evidence is captured. Now R3 (root-URL active nav) and R4 (per-route mobile overflow) on the reference.
R3 confirmed — nothing active on `/`, no nav landmark. Now R4: per-route mobile overflow.
R4: `/` and `/dashboard` still overflow (395), but `/networth` measured 390 this time vs the documented 464. Let me re-verify with a longer settle — this could be data drift or timing.
R4 已确认并完全解决 — `/networth` = 464（之前读取的 390 是正在加载的页面）。**R1–R4 均已在参考站点上重新验证（第 25 次）。** 接下来是 SEO 配对检查。
SEO endpoints confirmed on the reference. Now the full head-metadata census.
Reference head census captured. Now let me boot the clone parity server and run the same census + clone-side standing checks.
Clone head census byte-identical on all pinned fields. Now the clone-side mobile-nav R1–R4 (25th).
R1 和 R4 在克隆版本上表现正常。让我更严谨地重新验证 R2（克隆的 sheet 是一个 Radix 对话框——使用 role=dialog 检测器）。
R2 superset fix verified. Let me confirm R3 on the clone, then sweep the session-61 suggested surfaces (donut keyboard, filter selects arrow semantics, dialog Tab order).
R3 ✓ on clone (Dashboard active with gradient + nav landmark). **All 25th standing checks clean.** Now the session-61 suggested surfaces — first, the donut sector keyboard semantics on the reference.
Reference donut: all 3 sectors `tabindex="-1"` — not keyboard-focusable. Let me verify the clone side and test actual behavior.
**FINDING**: The clone's recharts surface has `tabIndex="0"` + `role="application"` (recharts 3 default) while the reference's has neither — a keyboard-semantics divergence. Let me verify actual Tab behavior on both sites.
**FINDING CONFIRMED**: The clone's recharts-3 surface IS a Tab stop rendering an unpinned 5px lab-colored focus ring; the reference (recharts 2) has a non-focusable chart. Let me investigate the `g` stop and the clone's donut code.
The recharts 3 mechanism is clear: explicit `tabIndex`/`role` props override the a11y-layer defaults. Let me check where `accessibilityLayer` defaults come from and how props flow to the surface.
The a11y layer also adds `role=status` + `aria-live=assertive` to the tooltip wrapper. Let me check what the reference's tooltip renders (hover the sector synthetically) and how the clone's tooltip is configured.
Reference tooltip: wrapper `tabindex=-1`, inner has NO role/aria-live. Now the clone's tooltip DOM with the same probe.
**FINDING G1 confirmed**: clone's recharts-3 a11y layer leaks `role=status` + `aria-live=assertive` on the tooltip + a Tab-stop surface — neither on the reference. Fix: `accessibilityLayer={false}`. Now the second suggested surface: **filter selects' open-state arrow semantics**. Let me measure on the reference first.
The reference's select is Radix (combobox/listbox/options). Now test arrow-key behavior on the reference.
Reference select arrows work (no wrap at ends). Now the same test on the clone.
**Filter selects: NO finding** — identical Radix roving behavior on both sites. Now the third suggested surface: **dialog forms' full Tab order**. Let me open the Add Item dialog on the reference and walk Tab through it.
The probe is rough — let me do a full focusables census in DOM order plus a REAL Tab walk with native key presses.
The reference dialog has BOTH Radix comboboxes AND native SELECTs (focusable!). Let me check their geometry and get the full dialog census.
The native selects are `tabindex=-1` + 1×1 hidden — NOT real Tab stops; my census filter was too loose. Let me redo with the tabindex property and check the radiogroup's focusability.
Reference Tab order captured (15 stops). Now the same strict census on the clone's dialog.
**FINDING G2**: The reference has the classification radio BUTTON as a Tab stop; the clone doesn't. Let me dig into the classification tile structure on both sites.
**FINDING G2 confirmed**: reference's checked radio = `tabindex=0` (roving Tab stop); clone's = `tabindex=-1`. Let me examine the clone's tile code.
The clone uses stock Radix — but the checked radio measures `tabindex=-1`. Let me check the installed Radix version's roving logic.
The clone renders the fresh Radix roving state (container 0, items -1). The reference's checked-item tabindex=0 may have been interaction contamination from my earlier Tab-walk. Let me re-measure the reference fresh.
**FINDING G2 is real on fresh open**: reference checked radio = tabindex 0, clone = -1. Now let me measure the arrow-key behavior on both sites to complete the contract.
Reference: entry-focus lands on checked radio, arrows move focus + flip check (automatic activation). Now the clone.
**Arrow behavior IDENTICAL on both sites** — the only delta is the fresh-state tabindex. Let me also identify the mystery `g` Tab stop I saw earlier on the clone.
The clone's donut has TWO extra Tab stops: `svg.recharts-surface` AND `g.recharts-layer.recharts-pie`. Let me check if `accessibilityLayer={false}` removes both.
`rootTabIndex` (default 0) is the Pie layer's own prop, separate from the surface. Let me confirm the reference's pie layer tabindex.
**Correction**: the reference's pie LAYER is tabindex=0 (focusable on both sites ✓); the drift is only the SURFACE (ref: -1/no role; clone: 0 + role=application). Let me test arrow behavior from the layer on both sites to complete the contract.
**Keyboard drift found on the donut**: reference arrows move focus to sectors; clone arrows open a tooltip without moving focus. Let me map the full keyboard contract on both sites.
The reference's arrows rove sector focus (recharts 2.15-style a11y layer). Let me inspect recharts 2.15's source to understand the reference's exact mechanism.
recharts 2.15 confirmed: `rootTabIndex: 0` (layer focusable — same as clone ✓); surface attrs only when a11y layer on. My probe had a focus race — let me re-measure the reference's donut keyboard contract carefully.
The reference's Pie has raw keydown handlers (ArrowLeft/Right rove sectors with wrap; Escape blurs). Let me check recharts 3.10's Pie keyboard implementation.
recharts 3 REMOVED the pie keyboard roving that the reference has — a real functional parity gap. Let me check the focus-ring rendering on both sites to complete the contract.
Full contract mapped. The reference's rings render identically (5px auto near-black). Now let me check existing e2e Tab usage that could be affected by the G2 fix, and look at the donut code structure for the fix.
Both findings are mapped. Let me check the v30 VLM compare script and run a VLM pairwise on the two surfaces my fixes touch (dashboard + add-dialog) as the standing visual check.
All VLM flags need DOM arbitration per the discipline. The dashboard flags are data/superset-driven; let me arbitrate the dialog X-close flag with computed geometry.
My X-finder matched the wrong element on the clone (`opacity-0` = a card action button). Let me re-arbitrate with the correct finders.
All VLM flags DOM-explained (data + documented supersets). The sweep is complete. Let me examine the donut code region for the G1 implementation, then write the remediation plan.
All findings mapped. Now let me write the remediation plan v31.
Plan written. Now let me validate it against the codebase as claimed.
All claims validated. Now TDD Step 1 — write the G1 tests (RED phase). Let me check the dashboard spec structure first.
**RED confirmed** — both tests fail against the drifted implementation. Now GREEN: implement G1 in dashboard-view.tsx.
G1 implemented. Now rebuild and run the G1 tests (expect GREEN).
**G1 GREEN**. Now TDD Step 3: G2 RED — the classification tiles' fresh roving test. Let me check the dialog-buttons spec structure.
**G2 RED confirmed**. Now GREEN — implement the G2 fix.
The static census passes (G2 fix works) but the real Tab walk skipped the container. Let me debug the actual focus sequence live.
The DOM is correct (fix works) — but focus skips the container. Let me check if Radix forwards focus from the container to an item.
**The container is a transient pass-through** — Radix's entry-focus forwards keyboard focus from the container to the checked radio. Let me verify the reference does the same with a REAL Tab press.
**Confirmed**: the reference's REAL Tab from Amount lands on the checked radio (entry-focus pass-through — same as the clone). Let me fix the test to assert the true contract.
**G2 GREEN**. Now Step 5: pin-sanity mutations — prove the assertions are load-bearing. Mutation 1: remove the a11y prop.
Mutation 1 confirmed (test 1 fails). Restore, then Mutation 2: break the roving wrap.
The mutation-3 output got swallowed by the rg error. Let me redo mutation 3 cleanly.
**All TDD cycles complete** (RED → GREEN → pin-sanity → restored). Now the full clean-check chain.
**FULL CHAIN GREEN: 108 · 164 · 35 + lint/typecheck/build.** Now Step 7: live re-verification on the parity server.
**Donut keyboard semantics live-verified — byte-identical to the reference** (surface null/null, roving + Escape identical). Now the G2 live check.
**G2 live-verified — byte-identical fresh census.** Now regenerate the screenshots.
All 16 screenshots regenerated. Now let me persist the v31 probes and update all documentation.
Now update README.md — find the v30 row and test counts.
Now let me update all the documentation. First README.md.
Now CLAUDE.md.
The count updated but the v31 surfaces addition didn't match. Let me fix with the exact string.
Now AGENTS.md — add the v31 verification paragraph after the v30 one.
Now the SKILL doc — find the session history table.
Now write the formal session log (docs/session_63.md) and the raw narrative (docs/session_64.md).
Now update the worklog.
Now let me update the parent workspace worklog and check the git status before committing.
Clean changeset — no .env, no db, no test artifacts. The verification gate is green. Now commit and push via the SSH wrapper.
No system ssh. Let me check the repo's bundled shim scripts and install paramiko.
paramiko installed. Now set up the ssh shim outside the repo and run the wrapper.
Dry-run clean. Now the real push.
**Parity iteration v31 is shipped to `main`** (commit `157fecd`, remote-verified via the SSH wrapper, key shredded, tree clean).

**What this session found & fixed** (all measured live on both sites, TDD with pin-sanity mutations):

1. **The donut's keyboard semantics** — recharts 3's a11y defaults drifted from the reference's recharts 2.15: an extra tab-stop surface (`tabIndex=0` + `role="application"`) with an unpinned 5px ring, live-region semantics on the tooltip, and the *removed* pie sector roving. Fixed via `accessibilityLayer={false}` + a byte-exact replication of 2.15's roving contract (backwards-wrap quirk included).
2. **The classification tiles' fresh roving state** — the checked radio now renders as a real tab stop (`tabIndex={selected ? 0 : -1}`), matching the reference's two-stop fresh DOM.

**Standing checks all clean for the 25th consecutive time** — mobile nav works (Tailwind v4 pins hold), zero data drift, SEO byte-identical. Full chain: **108 unit · 164 e2e (was 161) · 35 smoke**, all green; 16 screenshots regenerated; docs, worklog, and session logs aligned.

**Suggested next steps**: the keyboard sweep still has unmeasured families — the net-worth dropdown menus, the calculator row actions, and the breakdown accordion — or a performance/correctness pass (Lighthouse, bundle sizes, API error tiers). Just re-issue the brief referencing `docs/session_63.md` / `docs/remediation-plan-v31.md` and I'll pick it up from there.
