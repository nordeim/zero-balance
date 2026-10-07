`git pull` 成功 —— 更新至 `e23d854`，引入了 `docs/session_8.md`（第 7 次会话的原始日志；第 7 次会话自身已交付 remediation v4 并推送了 `28ad5fc`）。现在让我阅读剩余的关键文档。
I have the full picture now. Sessions 1–7 delivered the build plus remediations v1–v4 (last: nav geometry, net-worth summary card, mobile overflow fix, filter-aware counts — all green at 96 unit / 52 e2e / 30 smoke, pushed as `28ad5fc`; `e23d854` added session_8.md, the raw narrative record). This session continues with a fresh verification + parity iteration v5.
文档已查看。现在让我检查 `SKILL` 文档的当前状态部分，并根据文档描述验证代码库。
Environment matches the documented contract. Let me validate the v4 fixes are present in code and verify route counts.
v4 fixes verified in code. Let me check the net-worth and items-view fixes, then kick off the verification chain.
All v4 remediation fixes confirmed live in code. Now the full verification chain — starting with typecheck, lint, and unit tests.
96/96 unit green. Now the production build.
**Full chain green: typecheck ✓ · lint ✓ · 96/96 unit ✓ · build ✓ · 52/52 e2e ✓ · 30/30 smoke ✓** — baseline confirmed at `e23d854`. Now the fresh two-site parity audit.
Now let me boot the clone's standalone server on :3200 (killing any stale process by port first — the documented gotcha).
Clone server live. Opening both browser sessions and logging in.
The server died when the shell exited (process-group kill). Let me detach it properly with `setsid`.
Clone logged in. Now the reference session.
Both sessions logged in (clone `/dashboard`, ref `/`). Let me review the existing probe infrastructure to reuse the established pattern.
The probe pattern is established. Let me set up a runner helper and start the v5 audit — first a quick re-verification of the v4 surfaces, then fresh angles (calculator dialog, breakdown drill-down expanded states, guidelines, focus rings, select chrome, intermediate breakpoints).
Nav geometry matches exactly on both sides. Now the fresh v5 angles — starting with a dashboard probe covering the Budget Guidelines card leaf detail, breakdown drill-down expanded states, and page title.
Two leads: (1) guidelines row text color differs subtly — ref `rgb(10,10,10)` vs clone `rgb(63,63,63)`; (2) my breakdown selector found nothing on either side. Let me write a leaf-level probe for both.
Rich data. I see three candidate findings: (F1) donut-legend/guidelines row text `rgb(10,10,10)` on ref vs `rgb(63,63,63)` on clone; (F2) white-alpha text computing as oklab on the clone; (F3) quick-action cards — clone has a `border` class the ref lacks. Let me probe leaf-level to confirm.
F3 and F1 resolved — both false alarms (row containers inherit a color no leaf uses; quick-action borders compute identically). F2 confirmed: white-alpha hero labels compute as oklab on the clone vs rgba on the ref. Let me fix my legend probe (icon wrapper divs broke the filter) and enumerate where `text-white/NN` appears in the clone.
Donut legend text: ref `rgb(10,10,10)` vs clone `rgb(63,63,63)` — potentially visible. Let me get the inner spans to see exactly which text carries which color.
Label spans and slice labels match. The amounts DIV (`$300.00 4.6%`) is where the colors diverge — let me dump its inner HTML structure directly.
Leaf-for-leaf identical — the color diff is only on an inherited wrapper no bare text uses. Let me systematically check both sides for ANY text node that actually renders with the inherited base color (#0a0a0a ref vs #3f3f3f clone), to be sure no surface relies on inheritance.
No dashboard text renders the base color on either side — that difference is invisible (I'll note it as a candidate micro-fix for computed body parity). Now let me sweep the items views and net-worth with the same probe, then move to the calculator dialog.
发现了一个关键问题：克隆项目的“所有类别”/“所有频率”选择占位符，以及“资产/负债”标签页，都渲染了继承的基色——而参考项目没有任何继承。让我去测量参考项目中这些具体元素的样式。
Real visible findings: select-trigger text `rgb(10,10,10)` ref vs `rgb(63,63,63)` clone, and border `rgb(229,229,229)` vs `rgb(229,231,227)`. Let me check the ref's net-worth tabs and dialog inputs for the same class of drift.
**Major visible finding (D)**: the ref's active net-worth tab is green-tinted (`bg #dcfce7`, text `#14532d`) while the clone renders white bg + gray text. Let me examine the clone's tab implementation and the globals.css base tokens.
已找到根本原因：克隆项目的 token `--color-foreground: #3f3f3f` 与参考项目的 `#0a0a0a`，`--color-input: #e5e7e3` 与 `#e5e5e5` 不一致，外加通用 shadcn 标签页激活态（`bg-white`) 与参考项目的绿色处理方式。让我获取参考项目标签页完整的 class 列表及其 TabsList 容器。
The ref's tab list is a `grid w-full max-w-md grid-cols-2` with green active state — the clone renders a compact inline-flex white pill. Clearly visible. Let me measure the geometry (widths, gaps) to complete the picture.
The full finding set is emerging. The ref uses shadcn's neutral palette (#0a0a0a foreground, #f5f5f5 muted, #e5e5e5 input) while the clone used zinc-ish variants. Let me read globals.css and constants.ts to map every token.
让我直接从两个站点的 `:root` 中测量参考站点的 `shadcn` token 值——这是最根本的真实数据源（source of truth）。
The ref's exact token set is now measured. Key drift: foreground `#0a0a0a` vs clone `#3f3f3f`, muted `#f5f5f5` vs `#f4f4f5`, input `#e5e5e5` vs `#e5e7e3`, ring near-black vs forest-dark, accent `#f5f5f5` vs `#f0f2ee`. Notably the ref's card borders stay `#e5e7e3` (clone already matches) — only form controls use `#e5e5e5`. Let me now open the Add Item dialog on both sides and audit its inputs, dropdown chrome, and buttons.
The dialog is open (fixed overlay covers the page). Let me snapshot it properly.
Ref dialog mapped. Now let me write a deep dialog-chrome probe (panel, inputs, labels, tiles, buttons) and run it on the ref.
Ref dialog: labels near-black `rgb(10,10,10)`, inputs bordered `#e5e5e5`, Cancel white/`#e5e5e5`-border, Save transparent-bg (gradient). Let me capture the Save gradient and run the same probe on the clone.
已捕获参考对话框：保存 = forest→lime 渐变，取消 = 白色/`#e5e5e5`/接近黑色文本。现在在克隆上进行同样的操作。
发现明显的对话框差异：ref Cancel = 轮廓（白色背景，`#e5e5e5` 边框，接近黑色文本， 6px 圆角）对比 clone ghost（透明，灰色，无边框， 8px 圆角）；ref Save = forest→lime 渐变对比 clone 实心 lime。让我检查一下克隆项目的对话框代码，以及 ref 在其他对话框（计算器、资产）中是如何渲染其操作按钮的。
Escape 没有关闭参考项目的对话框——如果确认的话，这可能是另一个参考项目 bug。让我来仔细验证一下。
Escape works (the earlier catch was the exit animation). Now let me open the ref's calculator dialog.
The Add dialog reopened via a stray click. Let me close it, then hover a card and click its Calculate button properly.
Something keeps reopening. Let me just look at the current state directly.
The dialog heading persists in the a11y tree with no `[data-state=open]`. Let me measure whether it's actually visible and blocking interaction — this could be another reference bug.
My earlier check was a false negative — the ref's overlay has NO `data-state` attribute, and it's still fully visible and blocking. Escape did NOT close it. Let me re-test rigorously with focus inside the dialog.
**Confirmed new reference bug (R5)**: the ref's Add Budget Item dialog ignores Escape entirely (custom overlay, no `data-state`, no keyboard dismissal) — only X/Cancel close it. The clone's Radix dialog closes on Escape — a superset behavior to pin. Let me close it via X and continue to the calculator dialog.
Dialog closed via X. Now the calculator — hover the Netflix card, click its Calculate button.
Ref calculator empty state captured. Let me probe its chrome and compare with the clone — first snapshot the clone's expenses.
Ref calculator captured — "Add First Item" is an outline button. Let me check which clone items have no line items to compare, then open its calculator.
The clone's expenses have no seeded line items — its calculator will show the empty state like the ref's Netflix. Let me close any clone dialog and open its calculator.
Both calculators open. The outline-button drift repeats (`#1f2937` text + `#e5e7e3` border vs ref's `#0a0a0a` + `#e5e5e5`). Let me fix the banner probe climb and compare the "Add Item" header button + banner card on both.
Banner chrome matches; the "Will update" text computes as `lab()` on the clone vs `rgb(234,88,12)` on the ref (v4 color-space drift). Let me capture the Add Item button gradients on both.
Gradient matches. Now let me add a line item on the ref to inspect the line-item dialog buttons and row chrome.
**Key discovery**: the ref's line-item dialog Save = ORANGE gradient (`#e07a3b→#f5a962`) while the budget-item dialog Save = forest→lime — the Save buttons are contextual per dialog. Let me check the income/savings/asset dialogs on the ref to map the full pattern.
Escape doesn't work on the ref's line-item dialog either (R5 consistent). Closing via Cancel, then sweeping income/savings/asset dialogs.
Budget-dialog Save = forest→lime everywhere; line-item dialog Save = orange. Now the ref's asset dialog, then the clone's full button set.
Ref asset dialog: Cancel outline + Save Asset forest→lime. Now the clone's line-item and asset dialog buttons.
Same drift confirmed on the clone's asset dialog. Now the last dialog family: the delete confirmation (destructive colors + dropdown menu hover) on the ref.
Ref menu: Delete item = `#dc2626` (red-600), content `#e5e5e5` border. Let me capture hover bg and then the delete-confirm dialog.
**重要提示**：参考项目的 Delete 会立即删除，且没有确认步骤——我刚才删除了参考项目的 Salary 项目。让我立即通过 Add Income 对话框将其恢复。
Salary restored with identical card text. Let me verify the ref's dashboard totals returned to the original state.
Ref restored (1/1/3 items). Now the clone's menu + delete flow for comparison.
Clone menu: Delete renders as `lab()` red vs ref's clean `#dc2626`; content border `#e5e7e3` vs `#e5e5e5`. The ref uses two border systems — cards `#e5e7e3`, popovers/inputs `#e5e5e5`. Let me check the ref's select-dropdown content and dialog panel borders to complete the map.
Select-item highlight differs too: ref `#171717` on `#f5f5f5` vs clone forest on `#f0f2ee`. Let me measure nav-hover text color on both sides (the last hover state), then move to tablet/mobile.
Both showed the active link. Let me hover an inactive link ("Expenses") on both sides and measure the hovered state.
**Real regression found**: the clone's nav hover bg computes transparent — the hover style isn't applying at all on the live build (ref: green-50 + zinc-900 text). Let me inspect the sidebar code and the built CSS.
The class is in the source. Let me check whether the built CSS actually contains the rule and the `--color-green-50` variable.
The built CSS has TWO `--color-green-50` definitions — a pinned hex `#f0fdf4` AND v4's default `lab(98.1563% …)` — and the hover computed transparent (invalid-at-computed-value-time → initial). Let me confirm what the live page resolves.
`var(--color-green-50)` resolves fine — my hover measurement may have been flawed. Let me redo it carefully with a `:hover` match check.
Hover is active but the bg rule doesn't paint, and the hover text resolves to a lab value that isn't the forest token. Let me inspect the full selector in the CSS and the live var values.
The rule exists and the var resolves — yet the paint fails. Let me test whether a forced inline `var(--color-green-50)` paints on that very element, and check the transition behavior.
The forced var paints — so the rule itself isn't applying. This smells like the documented stale-cache gotcha. Let me check the LIVE stylesheet rules the page actually loaded.
The rule lives inside `@layer utilities` — and Tailwind v4 wraps hover variants in `@media (hover: hover)`. If the headless session reports no hover capability, the rule never fires. Let me check the media query and the rule's context.
The session reports `hover: none` — Tailwind v4's hover variants are media-gated so they don't fire here (the ref's v3-era hovers do). That's a real v3/v4 behavior difference I can pin with `@variant hover`. Also `--color-sidebar-accent-foreground` never emits as a var — let me check how the utility was compiled.
The clone's hover text compiles to forest `#1a3a2e` but the ref's sidebar-accent-foreground is zinc-900 (`rgb(24,24,27)` measured) — same class, different token. And v4's media-gated hover variants break parity on non-hover devices. Let me measure both sides' resting nav text, then finish the audit sweep.
Let me convert precisely in-browser: compare the clone's resting color against candidate hexes.
`lab(26.8…)` = `rgb(63,63,70)` — the clone's resting nav = zinc-700, the ref's = zinc-900 `rgb(24,24,27)`: a real visible difference. Let me cross-check with another ref link and dump its full class list.
The ref's resting nav = zinc-700 (my earlier read was hover-polluted — mouse still over Expenses). Refined finding: only the HOVER TEXT differs (ref zinc-900 vs clone forest). Let me clear the hover, check the ref's dialog panel border, and compare focus rings.
Dialog panels identical. Now focus rings — Tab to a button on each side and measure the focus-visible ring.
Reference nav focus ring = blue-500 `#3b82f6` (its sidebar-ring token) vs clone forest. Let me also check the search input's focus ring (the general `ring` token) on both sides.
General ring confirmed drifting too (near-black vs forest). Now the tablet breakpoint sweep at 768×1024 on both sides.
At 768 the ref shows NEITHER rail NOR burger while the clone shows the rail — a breakpoint regime difference. Let me map both sites' chrome across widths (640/768/820/1024).
Both match at ≥768. The 640 results are finder artifacts — let me snapshot both sites at 640 directly.
Both sites match at 640 (mobile chrome with "Toggle Sidebar"). Now the priority mobile re-verification at 390×844.
Ref bugs R3/R4 still live; clone fits everywhere. Now the mobile nav interaction flows on both sides.
Ref bug #1 re-confirmed (toast container blocks); clone's burger clickable at identical geometry. Now the sheet nav flow on both.
Ref bug #2 re-confirmed (sheet stuck open after nav). Now the clone's flow.
Clone's sheet closes on nav ✓ — all mobile superset fixes hold. One last spot-check: the ref's EDIT dialog buttons (to confirm the gradient pattern there too).
Income cards use the ellipsis menu on the ref. Let me open it → Edit.
Edit dialog confirms the same button pattern. One last micro-check — the sidebar rail divider color — then I'll compile the remediation plan.
Rail dividers match. **The audit is complete.** Let me now read the clone's relevant source files to plan exact fixes for the findings ledger.
The button primitive system is clear. One more precision measurement — the full focus-ring geometry on the search inputs (ref showed 1px ring, clone appears to be 2px + offset).
Focus rings share geometry (1px + shadow-sm); only the color drifts — the token fix covers it. **Audit complete.** Let me check existing Escape-key test coverage, then write the remediation plan v5.
No dialog-Escape coverage — I'll add a spec. Now writing the remediation plan v5.
Plan saved. Now validating it against the codebase — checking every file the plan touches.
The `button.tsx` outline variant is exactly the ref's Cancel — the token fixes will make it pixel-correct. Let me read button.tsx and the gradient constants.
All the pieces exist. Let me examine the remaining fix sites: calculator's empty-state button + "Will update" text, item-card's Delete menu color, dashboard hero white-alpha labels, and the sidebar focus ring.
All sites located. Now the TDD specs — first let me check the Playwright project structure to place them correctly.
The mobile specs already emulate `isMobile: true` (→ `hover: none`) — perfect for the G7 pin. Let me review the house spec style, then write the new specs.
House style clear. Writing the new specs now — `tokens.spec.ts` first.
Now the net-worth tabs spec — let me see the end of networth.spec.ts to append.
All specs written. TDD step 2 — verify they're RED against the current build.
**All 13 new specs RED** — TDD confirmed. Now implementing. First, checking remaining token usages before editing globals.css.
Clean — no stray usages. Implementing now: globals.css tokens + hover variant pin first.
All token edits applied. Let me verify the final state of the tokens block.
Tokens done. Line 270 still has the body base color — let me fix that context.
That's the toast text color. Let me check the ref's toast chrome first (trigger a validation toast — no data mutation).
No toast on the ref's silent validation. I'll align the clone's toast text to the foreground family and move on. Closing the ref dialog, then implementing the dialog buttons.
Now the `.zb-btn-add-outline` fix and `.zb-btn-primary` removal in globals.css, then the dialog footers.
Now the dialog footers — checking imports in each file.
All imports located. Before editing the liability dialog, let me measure its Save button on the ref (forest vs orange — don't assume).
The ref's liability dialog submit is labeled "Add Liability" (orange gradient). Let me check the clone's label.
Let me verify the ref's liability dialog submit label directly — the double "Add Liability" match needs explaining.
"Save Liability" exists on the ref (my regex missed it). The dialog is still open — measuring its gradient directly.
Ref's Save Liability = ORANGE gradient. Closing the ref dialog and applying all four dialog edits.
My first edit clobbered needed imports — restoring the full import block.
Imports fixed. Now the footer buttons in budget-item-dialog.tsx.
`rgb` still used — import stays. Now line-item-dialog.tsx.
`ASSET_LABELS` lost its import — fixing.
Now the calculator hint, menu Delete color, tabs, TabsList, white-alpha labels, and sidebar ring.
All white-alpha labels pinned. Now let me investigate why the Escape spec failed — checking the clone's dialog component.
The dialog is Radix-based — Escape should work. Let me check the overlay/panel CSS for exit animations that might hold the node mounted.
No animations — the unmount should be instant. Let me run the Escape spec alone to see the actual failure.
Strict-mode violation — two "Add Income" buttons on /income. Let me find the second one.
The empty state renders a second button only with zero items — yet a fresh seed has items. Let me count the actual buttons on the live page.
Only one button on the live page. Let me read Playwright's error context — it lists both resolved elements.
Cards render yet the empty-state button also exists — let me see the full page tree in the error context.
The a11y tree shows an empty `alert` at root but no second button. Let me dump the actual matched buttons with a quick Playwright probe.
The debug run finds ONE button — but the failing run found two. Let me read the full error-context file for the second button's ref details.
Let me check test 1's error context — did it fail the same way?
Same pattern — the second button must live in that `alert` element. Let me read the toast component.
The alert is only in the login card — yet it appears on /income. Let me extend the debug spec to dump the alert's content and the getByRole matches.
**Root cause found**: the `/income` page is prerendered static with an EMPTY store — the initial HTML contains BOTH the header and empty-state "Add Income" buttons; hydration removes the empty state once data loads. My specs clicked before hydration settled. Let me check how the existing items.spec handles this.
The existing round-trip test has the same latent race (passes only on a warm server). Let me check test 3's failure reason, then harden all the specs.
Clear: tests 1/4 hit the prerender race; tests 2/3 are genuine RED (stale build). Fixing the specs' race, hardening the existing latent race, removing the debug spec.
Wait — my asset-test settle uses the ref's data text. Let me check the e2e seed's actual asset header.
One flaw in my focus-ring test: Tab from the search input moves forward, not to the nav. Fixing it to walk backwards with Shift+Tab.
The menu test's ellipsis click is fragile too (first svg button = Add Income). Fixing to use the proper accessible name.
Typecheck + lint clean. Rebuilding and re-running the new specs.
21 passing now. Digging into the 6 remaining — budget dialog first.
The outline variant's `bg-background` resolves to the page-warm `#fafaf8`; the ref's token is white. Let me check the other failures before batching fixes.
Two issues: the spec evaluates mid-transition (200ms `transition-all`), and v4 computes `green-50` as oklab (needs an arbitrary-hex class for exact parity). Let me check the remaining failures.
Both popover surfaces set `text-popover-foreground`. The ref renders its menu/option text at the body foreground — aligning the token to the rendered value. Let me check where card-foreground renders too.
Applying the remaining fixes: popover-foreground token, outline button bg, arbitrary-hex hover class, and the spec settle waits.
The ring was captured mid-loop before the settle. Restructuring to re-read fresh after the wait.
Menu item colors pass; the popover content border needs the input token. Fixing both dropdown-menu and select contents.
The hover-highlight mechanism needs a live look. Let me probe both sites' menu items under real hover.
The mechanism works (hover→focus→tint); the spec's hover raced the menu's zoom animation. Switching to deterministic keyboard navigation (ArrowDown) in the spec.
All tokens specs green. Running the full e2e suite for regressions.
The old calculator spec pins the class name I just changed. Updating it to the computed-color assertion.
**65/65 e2e green.** Completing the chain: typecheck, lint, unit, smoke.
**Full chain green: typecheck ✓ · lint ✓ · 96/96 unit ✓ · build ✓ · 65/65 e2e ✓ · 30/30 smoke ✓.** Now the live parity re-verification — restarting the :3200 server with the new build.
The e2e suite proved the build is fresh — the :3200 session is cache-serving stale chunks (the documented gotcha). Cache-busting now.
The server is still an old process serving a deleted chunk. Checking what's actually on :3200.
The server has a stale build layout. Killing all next-server processes and booting fresh.
Fresh server serves the new build. Re-logging in and re-running the verification probes.
Fresh build matches: trigger `rgb(10,10,10)`/`rgb(229,229,229)`, hero `rgba(255,255,255,0.8)`. Continuing the side-by-side verification — nav hover and tabs.
Nav hover matches exactly. Now the net-worth tabs.
Tabs geometry/colors now identical — only the gap below (ref 24 vs clone 16) remains. Let me measure the clone's TabsContent margin.
Margin collapsing explains it: ref = content `mt-6` (24px), no list margin; clone = `mb-4`+`mt-2` collapsing to 16. Fixing to the ref's exact structure.
The kill missed the listener (lsof doesn't see it — only `ss` does); my new server died on EADDRINUSE. Killing by the `ss` PID and re-booting.
Gap 24px, list 448px — tabs fully match. Now verifying the dialog buttons and menu on the fresh build.
Budget dialog buttons match exactly. Now the calculator + line-item + asset dialogs.
Calculator + line-item Save all match. Now the asset dialog and the dropdown menu.
Menu matches. Now hover highlight + select dropdown + focus rings.
All match. Now focus rings and the mobile verification.
Input ring matches. Now the mobile verification at 390×844 — hover:none tint (G7), hamburger, sheet flow, overflow.
**G7 verified live** — the tint applies under `hover:none`, matching v3 semantics. Now the superset flows and overflow.
**All mobile checks pass.** Live parity re-verification complete. Final full-chain run after the tabs spacing change.
**Final chain green: typecheck ✓ · lint ✓ · 96/96 unit ✓ · build ✓ · 65/65 e2e ✓ · 30/30 smoke ✓.** Now regenerating the screenshot catalog.
All 12 screenshots regenerated. Now the docs alignment — starting with README.
README done. Now CLAUDE.md.
Now AGENTS.md.
The first batch was atomic-failed, so the testing note needs re-applying.
Now the SKILL doc — project_state and the debugging rows.
Now the session log (`docs/session_9.md`) and the worklog update.
Let me check for remaining stale counts in the SKILL doc and verify everything.
SKILL clean. Updating the shared workspace worklog per protocol.
All docs aligned. Reviewing the change set before commit.
Change set is clean. Final sanity gate, then commit.
Committed as `db757a2`. Now the SSH-wrapper push — checking the runbook and shim infrastructure.
Infrastructure intact. Staging the key outside the repo and running the preflight + dry-run.
No ssh-keygen here (session 7 used the wrapper's preflight instead). Running the dry-run with the shim on PATH.
The dry-run hit the wrapper's DEFAULT remote (task-management) — wrong repo. Checking the wrapper's CLI for the remote override.
Dry-run green — clean fast-forward `e23d854..db757a2`. Executing the real push.
**Push verified** — remote main @ `db757a2` == local HEAD. Shredding the staged key and confirming final state.
All clean — key shredded, tree clean, remote verified. Closing browser sessions and the parity server.
Session 9 complete — everything shipped. Here's the wrap-up:

**Audit** — Pulled to `e23d854`, re-verified the v4 baseline green, then ran a deeper two-site audit: read the reference's own `:root` tokens, swept inherited-color text, and compared dialog buttons, dropdown states, focus rings, and hover semantics. Found **10 gaps** (zinc-vs-neutral tokens, pill vs 448px green tab grid, ghost vs outline/gradient dialog buttons, v4's media-gated hover variants, lab-color drift, ring colors) plus **2 new reference bugs**: R5 (its dialogs ignore Escape) and R6 (its Delete has no confirmation).

**Fixes** — All TDD-first (13 new specs, red→green): token block + `@variant hover` pin, reference tab structure, outline Cancel + per-dialog gradient Saves, arbitrary-hex color pins. Final chain: **96/96 unit · 65/65 e2e · 30/30 smoke**, live parity verified surface-by-surface, 12 screenshots, docs aligned.

**Shipped** — Committed `db757a2`, pushed to `main` via the SSH wrapper (remote verified, key shredded).

Next steps: I can wire real OAuth for "Continue with Google", add multi-currency support, or run another verification pass anytime — just say the word.
