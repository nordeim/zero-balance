I'll continue the task from where we left off. Let me start by refreshing the local workspace and checking the current state.
The workspace has been reset. Let me clone the zero-balance repository fresh.
The repo is cloned with all the latest docs (session_108, session_109, remediation-plan-v47). Let me create a comprehensive TODO list and start the review process.
Let me read the key sections of the AGENTS.md file and other core documents.
The docs are very large. Let me read strategic sections — the project state summaries and latest session records.
Now I understand the v47 state. Let me review the worklog's latest entry and key sections of the remaining core docs.
Let me check the latest commit contents and the numbering conventions.
The numbering convention is clear. Now let me review key sections of the remaining core docs.
Now let me verify the current state lines in README and SKILL docs, then validate the codebase structure.
All docs reviewed. Now let me validate the codebase structure and verify the v47 state in code.
Codebase verified at v47 state. Now let me rebuild the environment (workspace was reset — `.env`, `db/`, `node_modules/` are missing).
环境已重建。现在开始运行基线链 —— 先进行 lint、typecheck 和单元测试。
108/108 unit ✓. Now the build (includes robots.txt + sitemap.xml prerender).
**226/226 e2e ✓** (5.3m). Now the smoke test to complete the baseline chain.
**Full baseline chain GREEN: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ · 226/226 e2e ✓ · 35/35 smoke ✓**

Now the audit phase — security audit, secret scan, env parity.
v47 diff audit clean — no src/ changes (pin-only confirmed). npm audit = same 5 dev-only advisories (accepted; --omit=dev = 0). Now let me review the skills catalog.
Let me check the probe infrastructure and the Tailwind v4 skill for known traps.
Let me study the with-server helper and start the clone server for standing checks.
agent-browser v0.39.0 ready. Now the 42nd standing checks — reference side first (login + the four reference bugs).
Logged into reference root. Now the 390 reference-bug checks (toast-blocker, no-landmark, overflow) + data census.
**R-bug 1 (toast-blocker) confirmed** — the z-[100] toast container intercepts the burger. Now R-bug 2 (sheet-trap) via JS click.
**R-bug 2 (sheet-trap) confirmed** — sheet stays open after nav. Now closing the sheet and checking R-bugs 3+4 + data census.
All 4 reference bugs live + data intact ("1 items · $25,000"). Now the reference SEO pair, then clone-side checks.
Reference SEO pair live. Now the clone-side standing checks (R1–R4 + SEO) via with-server.
R1 passed (burger hit is its own child — no toast-blocker in clone). R2 needs a re-check — the click result was missing. Let me write a proper standing-check script.
**第 42 次常规检查全部通过** — 克隆 R1–R4 + SEO 通过；参考站点上所有 4 个 bug 均存活（超集完好）。

现在进行 v48 排队选择。让我研究一下候选项：item-details 对话框（操作按钮）、toast、empty-states。
The clone's toast uses a custom `.zb-toast` shadow. Now let me measure the v48 candidate surfaces on the reference — starting with the item-details sheet (read-only: open + census + close).
The layer found was the toast viewport — the card click didn't open item-details. Let me check the reference's card interaction pattern.
The item-details dialog is now open on the reference ("Budget Item Details" layer). Let me census its chrome and action buttons.
The reference panel: 512×680, radius 16, v3 shadow-2xl (2 leads + `rgba(0,0,0,0.25) 0px 25px 50px -12px`). Let me find the overlay and action buttons.
Reference measured: overlay `rgba(26,58,46,0.5)` (green-tinted), panel shadow-2xl (v3: 2 leads + `0.25 0px 25px 50px -12px`). Let me check the clone's item-details overlay + how the clone opens it.
The clone matches the card-click → details flow. Now let me close the reference dialog and probe the toast surface (empty-form Save — read-only, no data mutation).
No toast from empty-form save. Let me check the clone's toast triggers and find a read-safe equivalent on the reference.
No reference toast from empty-save either. Let me check if a prior session measured the reference's toast chrome.
Key finding: "The reference shows NO toast on save — the clone's toasts are superset UX". Let me check the v33 toast probe (a reference toast WAS measured once).
The reference's toasts are rare-path only (superset surface for the clone). Now measuring v48 candidate F2: the dialog-input focus composite at 390 (the mobile follow-up).
Reference dialog input at 390: same focus composite (3-layer v3 vs clone's 5-slot). Now F3: the empty-state via filter-to-zero on the reference.
The listbox looked stale. Let me re-probe the frequency filter options properly.
频率筛选器有非匹配的选项。选择“一次性”以触发参考的空状态。
The reference empty state renders. Let me census its chrome.
The reference empty state is fully measured. Now let me check the clone's empty-state markup.
The clone's markup matches. Let me verify the reference icon's opacity + the clone's `.zb-btn-add` shadow.
All three v48 surfaces identified. Let me reset the reference filter (leave as found) then measure the clone side via with-server.
Reference restored ("1 items · $5000.00"). Now the clone-side measurements via with-server.
Surface 2 (focus at 390) and Surface 3 (empty state) are at byte-parity — pin-only. Surface 1's card finder failed — let me check the clone's card structure.
The clone's card title is an h4 (reference uses h3). Let me re-run surface 1 with the corrected finder.
The panel finder failed — let me dump the dialog structure directly.
The `[role=dialog]` IS the panel (Radix Content). Let me census it directly.
All three surfaces at byte-parity — a PIN-ONLY iteration. Let me verify the clone's DialogCloseButton for the census.
The close button matches (36×36, radius 6). Now let me study the target spec files for the new pins.
All three v48 surfaces verified at parity — a pin-only iteration. Let me check the VLM compare pattern and write the remediation plan v48.
Now let me write the remediation plan v48.
Plan saved. Now let me validate the test idioms — reading the v47 F1 test pattern.
All idioms confirmed. Now writing the three v48 pin tests (TDD — pin-only). First F1 — the item-details shadow-2xl census.
Now F2 — the dialog-input focus composite at 390.
Now F3 — the empty-state full byte-parity census.
All three pins written. Killing agent-browser daemons (v46 lesson), then running the v48 tests.
The closeBtn finder returned null. Let me check how the X button renders (the v28 test expects textContent "Close").
The X button has an sr-only "Close" span. Let me fix the F1 finder.
F1 GREEN. Let me run all three v48 pins together.
**3/3 v48 pins GREEN immediately** (pin-only). Now the S1 mutation-sanity phase — each mutation needs the standalone REBUILD first (v47 lesson). Mutation (a): remove the panel's shadow-2xl.
Mutation (a) bites ✓. Restoring and applying mutation (b) — remove the input's focus-visible:ring-1.
Mutation (b) bites ✓ (both v47 F1 and v48 F2). Restoring and applying mutation (c) — icon mb-4 → mb-2.
Mutation (c) bites ✓ (h 328→320). Restoring and applying mutation (d) — remove the .zb-btn-add box-shadow.
Mutation (d) applied to the base rule (line 252 is the focus-state composite — a different site). Running F3.
All 4 mutations bite ✓. Restoring mutation (d) and verifying a clean source tree.
Pin-only contract reached — src/ untouched. Now persisting the probe files: the reference driver and the VLM compare script.
Now the VLM compare script for the /savings @1280 pair.
Now the full verification chain — rebuild the restored source + the complete test gate.
**229/229 e2e ✓** (226→229, +3 v48 pins). Now the smoke test to complete the chain.
**Full chain GREEN: 108 unit · 229/229 e2e · 35 smoke.** Now the VLM pair — capturing /savings at 1280 from both sites.
VLM flags 4 diffs — per the v43 lesson, the badge and metadata-row flags need DOM verification. Let me check both sites' savings cards.
Badge chrome identical (monthly/active). Let me verify the classification chip ("need"/"savings") chrome on both sites.
Session reset. Re-establishing the reference and re-running the census.
Chip geometry identical (h 22, radius 6, fs 12, flex-wrap container) — colors differ by classification value. Let me verify the clone's seed classifications + badge map.
**All 4 VLM flags DOM-verified as data classes** — badge colors match per classification value (need=red identical), the Recurring badge is richer seed data, avatar letter is user data. No chrome gaps.

Now regenerating the 16 screenshots.
16 screenshots regenerated. Now the D-series docs alignment. Starting with D1: AGENTS.md.
Now D1: AGENTS.md — the v48 paragraph after the v47 paragraph.
Now D2: CLAUDE.md — the v48 entry + count updates.
All 4 CLAUDE.md edits applied. Now D3: README.md — the v48 row + counts.
Now D4: the SKILL doc — Session 83 row + state line.
Now D5: the PAD v1.1.5 revision block.
Now D6: the probe README's v48 section.
Now D7: session_110.md (the formal log).
Now session_111.md (the raw transcript).
Now the repo worklog — Session 82 entry + the ledger list update.
All ledgers updated. Now D8: the workspace worklog.
Now the final verification before the commit — git status + the ignore rules.
All files verified, no secrets, ignores intact. Now reading the SSH wrapper runbook before the push.
The runbook is clear. Let me check the ssh availability and the shim.
paramiko 5.0.0 ready. Now deploying the Appendix A shim (outside the repo).
Deploying the shim outside the repo, then committing the v48 iteration.
Shim deployed. Now committing the v48 iteration to main.
Commit `c02dd1b` landed on main. Now the SSH push sequence — materializing the key.
Key verified. Now the dry-run push with the shim on PATH.
Dry-run succeeded (3f00e47..c02dd1b fast-forward). Now the real push.
**Push verified** — remote main @ `c02dd1b` == local HEAD. Now shredding the operator key and final verification.
**Parity iteration v48 delivered and pushed to main** (`c02dd1b` — remote verified, key shredded, tree clean).

**What v48 measured** (3 surfaces, both sites, read-only on the reference — everything at parity on every visible layer, hence a **pin-only** iteration): the item-details sheet's shadow-2xl (the regression net's 7th site), the dialog-input focus composite at mobile 390 (w 310 on both sites — the family is viewport-independent), and the empty-state full census (byte-parity via filter-to-zero). The queue's toast item resolved as superset-only — the reference's toasts never fire on empty-form saves (measured twice).

**Delivered:** 3 new e2e pins (TDD, 4 mutations verified, each with the rebuild-first lesson applied), **229/229 e2e + 108 unit + 35 smoke green**, 42nd standing checks clean (mobile nav works, all 4 reference bugs still live = superset intact), VLM pair DOM-verified clean, 16 screenshots, all docs + session_110/111 + worklogs aligned.

**Next (the v49 queue):** the login panel's mobile 390 census, the donut legend's mobile reflow, the calculator dialog's 640 chrome — or the toast reference-census (needs a mutation-sanctioned session). Just say the word.
