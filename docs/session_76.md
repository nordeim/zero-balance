I'll continue the workflow with the updated task requirements (now referencing session_72/73 and remediation-plan-v35). Let me set up my task plan and refresh the workspace first.
Now let me refresh the workspace and check current state:
Workspace refreshed with new commit `51f1fd9` adding `docs/session_73.md`. Let me examine the document set:
Workspace is clean and updated. Now let me review the key documents, starting with the newest session docs:
Now let me read the current remediation plan v35 and the worklog tail:
Now let me check the worklog tail (latest entries):
The worklog confirms v35 shipped (Session 68, 108/171/35 green). This session will be **parity iteration v36**. Let me check the environment state and review the project docs:
Environment is fully intact. Now let me review the project docs — CLAUDE.md first:
CLAUDE.md reviewed. Now let me examine the structure of the larger docs (AGENTS.md, README.md, Project_Architecture_Document.md, zero-balance_SKILL.md):
Let me read the remaining persisted AGENTS.md content and the README's key sections:
Docs reviewed. Now let me validate the codebase structure and confirm the v35 changeset is in place:
v35 changeset confirmed in place. Let me verify the G2 trigger ring and check the skills catalog:
所有项目文档已审阅并验证。现在让我标记进度并启动基准审计链（lint → typecheck → unit → build）：
Build green with robots + sitemap prerendered. Now the e2e suite (171 tests — this takes a while):
171/171 e2e green. Now the smoke test (35 steps):
**基准审计链完全通过 (GREEN)**：lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓（已预渲染 robots 和 sitemap）· 171/171 e2e ✓ · 35/35 smoke ✓ · npm audit（同样是 5 个仅限开发环境的建议——已记录/接受）· secret 扫描正常 · `.env.example` 为最新。

现在让我检查探针基础设施和 `agent-browser` 工具，准备进行双站点扫描：
The probe infrastructure is well-documented. Let me check the agent-browser tool state and existing sessions:
The infrastructure is clear. Now let me start the two-site sweep. First, login to the reference site:
已登录参考站点。接下来执行例行检查 —— 数据差异普查（第30次）：
Census clean (30th). Now mobile-nav R1–R4 on the reference (the task's particular focus):
Reference R1–R4 confirmed (30th) — all four reference bugs still live. Now the SEO pair on the reference:
Shell quoting mangled the eval — let me use the documented base64 probe pattern instead:
SEO pair matches pinned values. Now let me measure the new v36 surfaces. First, let me examine the v35 menu probes to build the hover-highlight probe:
Now let me check the clone's items-view filter selects structure before writing the Surface B probe:
Now let me write the v36 Surface A probe — the item-card menu's hover-highlight family:
The synthetic events didn't move the highlight — Radix needs a REAL hover. Let me use agent-browser's native hover command instead:
**Reference hover contract measured**: real hover → Radix moves focus to the item → the same accent family (bg `rgb(245,245,245)` + text `rgb(23,23,23)`). Now let me check the mouseleave behavior:
Reference mouseleave contract: focus returns to container, highlight clears, Delete back to rest-red. Now let me close the menu and boot the clone's parity server for the same measurement:
Clone fresh-open state matches the reference byte-for-byte. The page is loaded client-side, so the real hover works without the server:
**Clone hover family byte-identical to reference.** Now the clone's mouseleave behavior:
**Surface A verdict: byte-identical, no drift.** Now Surface B — the filter selects' listbox keyboard contract. Let me find the v34 listbox probe to build on:
Now let me write the Surface B probe — the filter selects' listbox keyboard contract:
Reference filter Select fresh-open: focus on selected option with accent highlight. Now the REAL-key keyboard contract:
Reference Surface B contract fully measured. Now the clone-side Surface B — I'll write the full script to run inside one with-server.sh invocation:
Clone Surface B is byte-identical on the full keyboard contract. One micro-difference to verify: the reference's closed trigger carried `aria-controls` — let me check the clone's open-state:
Both sites carry matching `aria-controls` while open — the closed-state difference is a Radix version detail (documented as an observation, not drift). Now **Surface C — the Tab-order census of the items view**:
The synthetic Tab won't move focus — I need REAL Tab presses with reads between each. Let me write the walk script:
The reference Tab walk is revealing — note the search input (447×36) and an odd "Close badge" button at bottom-right. Let me investigate that element:
**Mystery solved**: the "Close badge" is part of `#base44-edit-badge` — the **Base44 platform's floating "Edit with Base44" widget**, not app UI. The clone correctly omits platform chrome. Now let me verify the clone's search input and run its Tab walk:
The clone has the search input. Now let me run the clone's Tab walk inside the parity server:
The Tab walks reveal two differences to investigate. Let me check the git history of the trigger's `focus-visible:opacity-100` and the reference's actual trigger behavior:
The `focus-visible:opacity-100` is a day-one (session 1) design decision. Let me check what the v35 test pins about the trigger and verify the reference's trigger truly stays invisible on focus:
Let me directly verify the reference's trigger focus-opacity behavior:
The reference's trigger stays invisible (opacity 0) even when `:focus-visible` matches — the clone's reveal is a keyboard-a11y superset. Let me capture the reference's full trigger class string:
Two keyboard-a11y supersets identified (focus-visible reveal + open-state reveal). Now let me check the combobox aria-label history — the reference's comboboxes are value-named, the clone's are aria-labeled:
The aria-label is also a day-one decision. Let me compare the search input's attributes on both sites:
Both inputs match visually; the clone's aria-labels are invisible day-one a11y supersets. Now let me complete the standing checks — clone-side mobile-nav R1–R4 (30th):
All clone standing checks clean (30th) — mobile menu works, Tailwind v4 pins hold. Now the VLM pairwise — capturing both sites' dashboard + filter-open states:
Both pairs captured. Now the VLM pairwise comparison:
The SDK needs a different vision API pattern. Let me load the VLM skill for the correct usage:
The correct method is `createVision()`. Let me fix the script:
VLM verdicts: both "DIFFERENT" but ALL flags are DOM-explained (superset #3 Dashboard highlight, demo-data differences, Base44 platform badge) — no unexplained drift. Let me complete the read-only discipline — re-verify the reference census after all probes:
Reference census unchanged — read-only discipline held. The sweep is complete with **no production-code drift**. Now let me examine the test files to plan the pin insertion points:
Now I have full context. Let me check the SelectItem classes for the pin design, then write the remediation plan v36:
Now let me write the remediation plan v36:
Plan written and validated against the codebase. Now **TDD execution — S1 test first** (the hover-highlight family pin). Let me check the exact insertion point:
Now let me insert the S1 test (the hover-highlight family pin) right after the v35 S1 test:
Now let me run the S1 test — expecting GREEN (it's a pin, no drift):
**S1 GREEN.** Now the pin-sanity mutation — re-add the `focus:text-[#dc2626]` override:
**Mutation bites.** Now restore the fix and verify GREEN:
**S1 complete** (GREEN → mutation bites → restored → GREEN; the diff is exactly the test). Now **S2 — the filter listbox contract test**:
The fixture-restore raced Radix's async focus landing — the documented "interleave a toBeFocused() between presses" lesson. Let me fix:
**S2 GREEN.** Now the S2 pin-sanity mutation — strip the SelectItem's `focus:bg-accent`:
**Mutation bites.** Restore the class:
Now **S3 — the Tab-order census test**. Let me add it after the S2 test:
**S3 GREEN.** Now the S3 pin-sanity mutation — strip the kebab's `focus-visible:opacity-100`:
**S3 mutation bites → restored.** All three pins complete. Let me verify the changeset is exactly the two test files, then run the full chain:
Lint shows 2 new warnings — likely unused vars in my tests. Let me check:
Two easy fixes — the dead loop in the probe and the expression-statement blur:
Now the full e2e re-run (expecting 174):
**174/174 e2e green.** Now the smoke test to complete the chain:
**Full chain green: 108/174/35.** Now the dev DB census and screenshot regeneration:
Census clean (demo + smoke throwaways, 7 items, 0 probe users). Now regenerate the 16 screenshots:
Screenshots regenerated — byte-identical (no production changes; expected). Now the docs alignment. Let me check the session doc naming pattern:
The pattern is clear: formal logs (even docs) + transcripts (odd docs). Let me verify what the v35 commit included:
Now the docs alignment. First, the probe README's v36 section:
Now the README updates — the test counts and the v36 table row:
Now add the v36 row to the README's engineering-references table:
Now CLAUDE.md — the count and v36 surface entries:
Now AGENTS.md — the v36 paragraph after the v35 one, plus superset #7 in the parity rules:
Now the SKILL doc — the state line and session row:
Now the formal session log — docs/session_74.md:
Now the repo worklog entry (Session 70, newest-first):
Now the workspace worklog and the .env.example verification:
All docs aligned. Now the final verification gate — the complete changeset review:
Final gate clean. Now let me review the SSH wrapper runbook before the commit:
The environment matches the v35 pattern. Let me stage the shim outside the repo with the python3.13 shebang:
Now materialize the key and verify its fingerprint:
Key verified. Now the commit:
The dry-run shows a push conflict hint. Let me inspect the full output and the wrapper's dry-run logic:
The wrapper defaults to the wrong remote (task-management). Let me retry with the correct zero-balance remote:
Dry-run clean (`51f1fd9..fa62a7f`). Now the real push:
**Pushed and verified** — `main @ fa62a7f`. Now shred the operator key:
Push complete and key shredded. Following the repo's established pattern, let me add the raw transcript (session_75.md) as the follow-up session-log commit:
All work is complete. Let me close the browser sessions and finalize the todos:
**Parity iteration v36 shipped to `main`** (commits `fa62a7f` + `1a3a61f`, remote-verified, keys shredded).

## What this session delivered

- **Baseline chain green on the first full run** (lint · typecheck · 108 unit · build · 171 e2e · 35 smoke · audit clean) after refreshing the workspace
- **Standing checks clean (30th consecutive)** — mobile-nav R1–R4 on both sites (**Tailwind v4 pins hold, the mobile menu works**), data drift (reference read-only, verified before + after), SEO pair, VLM pairs — all flags DOM-explained
- **The session-72 suggested surfaces all measured for the first time — zero production-code drift**:
  - **Hover-highlight family**: REAL hover → Radix moves focus → the accent tint (the v35 G1 cascade holds on the hover path); pointer-off resets — byte-identical
  - **Filter Selects' listbox contract**: selected-option highlight, clamped roving, Home/End, Escape/Enter — byte-identical
  - **Tab-order census**: identical sequence; the reference's Base44 platform badge documented as an exclusion; **superset #7 documented + pinned** (the reference's kebab stays invisible when keyboard-focused — the clone reveals it)
- **Three new TDD pins** (S1/S2/S3, every pin-sanity mutation verified to bite) → **108/174/35 green**

**Next steps**: re-issue the brief referencing `docs/session_74.md` / `docs/remediation-plan-v36.md` — the queue holds the filter triggers' focus-visible family, the search input's typing contract, the expenses payment-method filter, or the still-open tooling pass (a11y CI step).
