I'll continue the zero-balance workflow. Note the document references have advanced again — now session_252/253 and remediation-plan-v103 (v103 cycle). Let me first refresh the workspace and establish the true state.
工作区已被重置 — `zero-balance` 代码库缺失。根据指令，我将进行全新克隆。
Clone successful at latest main (bb7e02e). The v103 cycle appears complete per commit 85e6189. Now let me read the key state documents — starting with the latest sessions and remediation plan v103.
The v103 cycle is complete and pushed (remote main @ bb7e02e). Per the rotation ledger, the next cycle is **v104 = the v98-era SAVINGS pair re-run**. Let me set up the task plan and review the core documents.
Core docs reviewed (persisted outputs). Let me check the rotation ledger and the v103-era sections of the key docs to confirm the v104 queue derivation.
v104 queue confirmed: the v98-era SAVINGS pair. Let me locate the probe scripts directory and the v98 lineage files.
The probe scripts are in `scripts/parity-probes/` (985 files). Now let me verify the v104 queue against vlm-shots-v98.sh's own header (the established discipline), then kick off environment provisioning.
v104 queue verified against vlm-shots-v98.sh's header: **the SAVINGS view at desktop 1280x800, FULL-PAGE — the EIGHTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104]**. Now let me start environment provisioning (npm install in background) while reviewing the remaining docs.
Now let me check npm install progress and study the v98 lineage structure + seedcheck procedure in detail.
npm install complete (354 packages). Now writing `.env`, provisioning the database, and installing chromium.
Seedcheck exact. Now installing chromium for the pinned Playwright version.
Environment fully provisioned. The two post-push commits (f6b5ccf + bb7e02e) audited session-log-only — zero src/ or lockfile deltas. Now starting **F0 — the baseline chain**.
Lint ✓ · typecheck ✓ · 108/108 unit ✓. Now the production build.
Build ✓ (robots + sitemap prerendered). Now the authoritative e2e count and the auditable chunk split (per the v103 chunk-split self-audit lesson).
Per-file sum = 305 spec tests + 1 setup = 306 total ✓ (matches authoritative count). Planning the four-chunk disjoint split: **Chunk 1** (items + item-details + dashboard + networth = 125+1), **Chunk 2** (login-parity + calculator + nav-geometry + a11y + mobile-navigation = 88+1), **Chunk 3** (auth + badge-colors + boot-failure + breakdown + calculator-error + dialog-buttons + empty-states + glyph-parity + loading-state = 56+1), **Chunk 4** (mobile-layout + networth-error + not-found + tokens + verify-email = 36+1). Total = 309 executions = 306 unique.
Chunk 1: 126 passed. Running chunk 2.
All 306 e2e green across four chunks (126+89+57+37 = 309 executions, zero flakes). Now the smoke test.
**F0 complete — all green.** Now F1: the axe-core drift watch.
F1: NO DRIFT (npm-latest 4.14.0; wrapper + engine 4.14.0; v68 dedupe holds). Now the engine-contract pin standalone.
F1 complete. Now F2 — deriving the 98th standing-checks pair from the v103 (97th) pair. Let me study the derivation script pattern.
注意命名约定——让我确认一下当前序列文件（v97 = 第 97 个）与现有 v98 序列文件（v98 周期的第 92 个）之间的正确源配对。
Confirmed: the latest standing pair is ref-standing-v97.sh + standing-checks-v97.sh (97th, run by v103). Cycle v104 derives the **98th pair** (v97→v98 tokens). Writing the derivation script.
98th pair derived cleanly (version-bump-only verified). Running the reference side first.
Reference side: all four bugs LIVE, census clean on first read, SEO pair live. Reaping, then the clone side.
F2 ALL GREEN — mobile menu VERIFIED WORKING the 98th consecutive time. Post-half seedcheck, then F3.
Now F3 — deriving the v104 probe series from the v98 lineage. Let me study the v103 derivation script (the most recent example).
The script runs clean (exit 0) despite that odd line — let me check if it's inside a string literal.
Resolved — the actual file content is sound (`text[max(0, ...)` — the display layer dropped `[m`; ast.parse + exit 0 confirm). Now let me survey the v98 lineage headers to plan the v104 derivation corrections precisely.
现在正在调研四个 v98 谱系文件中的所有 history tokens，以规划精确的修正。
Now let me study the two-half builder pattern and the with-server tool before writing the derivation.
所有 token 已映射。现在正在写入 v104 派生脚本。
One correction missed — the search string had "the v104 pin candidate" but the actual text is "// v104 pin candidate:". Fixing it.
推导无误 —— 零未命中，行数已保留，语法无误。现在正在验证 v104 census 边界并写入双半构建器。
Two-half census built (md5 891ab9b6, 153 lines, byte-identical across halves). Now capturing the reference-side screenshots.
双方均已捕获。正在运行 VLM 成对比对。
Verdict DIFFERENT — the pair's documented class. All flags map to documented classes (footer chips = v57 DATA-CONDITIONAL; grid 1-vs-2 = seed-count; contents/subtitle = seed-data; avatar = user-identity). Now the two-half census arbitration — reference half first.
Reference half complete. Reaping thoroughly, then the clone half.
Both halves complete, seedcheck exact after the clone half. Let me verify the census reproduces the v98-documented values exactly.
**F3 census verdict: ZERO DRIFT on every axis — the v104 census reproduces the v98 values exactly. NO NEW CLONE GAP.** Now F4 — surveying the coverage map for a never-pinned family.
正在调研 F4 候选对象。v103 的 pin 锁定了桌面端导航栏 (1280) 的用户页脚磁贴——让我检查一下移动端表单 (390) 的变体及其他候选对象。
Toast family is behaviorally covered but chrome-unpinned — however it's not cross-side verifiable under the read-only rule (reference toasts need write flows). Surveying other candidates.
The card's inline delete-confirm bar is a candidate. Checking its coverage across all specs.
Strong candidate emerging: the rail brand-block's "Budget Planner" subtitle + row chrome — v7 G4 pinned the tile/icon/logo but NOT the subtitle or row chrome. Let me verify the app-shell h1 and check for any other subtitle assertions.
The brand-block subtitle family is a strong candidate — never chrome-pinned (only mobile-sheet visibility). Let me study the v103 one-shot census pattern and write the both-sides probe.
Writing the brand-block one-shot census (both sides) modeled on the v103 userfooter pattern.
Clone side measured cleanly, but the reference returned "no h2" — its rail isn't an `aside`. Probing the reference's actual rail structure.
The reference's rail is a DIV with matching H2 + P values — byte-identical family confirmed. Fixing the finder (rail fallback per the v103 pattern) and re-running the full census.
**Brand-block family BYTE-IDENTICAL across both sides.** Now verifying the mutation target line and the definitive coverage map.
The pin is validated. Now checking the v36 nav-pitch band headroom (the mutation shifts the brand row height by +4px if text column drives it).
navPitch[0] = 145 with band (140,150) — the +4px mutation shift lands at 149, safely inside. Now reading the v103 pin's code to model the v104 append.
Now writing the remediation plan (pre-execution validated, per the discipline) before appending the pin.
Plan saved. Now appending the v104 pin to nav-geometry.spec.ts.
**Pin GREEN on first run** (10/10). Now the pin-sanity mutation — line-scoped text-xs → text-sm at sidebar.tsx:48.
ONLY the v104 pin red (9 green). Verifying the failure diff reads as the subtitle.fs axis alone.
**Single-axis confirmed** — fs "12px" → "14px" alone. Restoring and rebuilding.
**F4 complete.** Now F5 — the full chain re-run (307 e2e across four chunks).
F5 chain all green (307 e2e, zero flakes; 35/35 smoke). Now the screenshots regeneration + byte-compare.
**All 16 screenshots BYTE-IDENTICAL** (same-day regeneration — no DATE-class deltas this cycle). F5 complete. Now D1–D7 docs alignment.
All anchors located. Writing D1 — the AGENTS.md v104 paragraph.
D2 — CLAUDE.md count update + v104 clause.
D3 — README.md: counts + the v104 plan-table row.
D4 — zero-balance_SKILL.md: Session 139 audit row + state line.
D5 — PAD revision block v1.1.61.
D6 — the probe README's v104 section + v105 queue.
D7 — writing session_254.md (the cycle narrative). Let me check the v103 narrative structure first.
Now the worklog Session 139 entry. Checking the worklog structure first.
D1–D7 complete. Updating the plan's ToDo statuses, then running pre-ship gates.
Now the pre-ship gates: PIN-ONLY confirmation, .env.example check, gitignore verification, staleness sweep.
File modes consistent (644, matching the v103 convention). Final seedcheck, then staging and committing.
All 22 files staged (+2139/−5). Creating the commit.
**Commit 6589c35 created.** Now provisioning the push environment — reading the SSH wrapper runbook first.
Provisioning the push environment (paramiko venv + ssh shim — reset with the workspace).
Shim deployed. Now materializing the operator key and verifying the fingerprint against the documented record.
**Fingerprint matches the documented record** (SHA256:3ddaNlFh...U4PU — the same operator key as v99–v103). Dry-run with the remote override.
Dry-run clean (fast-forward bb7e02e..6589c35). Executing the real push.
**Push verified** — remote main @ 6589c35 == local HEAD. Shredding the operator key and running the independent HTTPS re-check.
Push doubly verified. Now the session-log follow-up — writing session_255.md (the ship record) and pushing it.
v104 cycle fully shipped. Final step — the workspace worklog per protocol.
The **v104 parity cycle is complete and pushed to `main @ 55c2c04`** ✅ (remote doubly verified — the SSH wrapper's assertion + an independent HTTPS re-check; tree clean; operator keys shredded with zero residue).

**What shipped (PIN-ONLY, zero src/ changes, +1 e2e = 307):**
- **Baseline all green** on the fresh-clone workspace: lint · typecheck · 108 unit · build (SEO prerendered) · 306→307 e2e zero flakes · 35/35 smoke
- **The v98-era SAVINGS pair's seventh re-run**: verdict DIFFERENT with every flag DOM-arbitrated to documented classes (footer chips the DATA-CONDITIONAL class; grid the seed-count; FAB the third documented form — unflagged); the two-half census reproduced the v98 values exactly — **no new clone gap**
- **New pin**: the rail brand-block subtitle/row census at 1280 — the family never pinned beyond v7 G4's tile/icon/h2-size axes, measured byte-identical both sides, mutation-verified single-axis. Live discovery: the reference's rail is a DIV, not an `<aside>` (fallback-chain finder lesson)
- **98th standing checks**: mobile menu working the 98th consecutive time; all four reference bugs still live
- Screenshots **16/16 byte-identical** (same-day regeneration); docs aligned D1–D7; remediation plan + session logs saved

**Next:** per the rotation ledger, v105 targets the **v99-era LOGIN + CALCULATOR pair** — say "continue v105" to proceed, or request adjustments.
