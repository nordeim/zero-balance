The workspace has been reset — I'll clone the repo fresh.
Repo cloned fresh (workspace was reset). Latest commit is the v72 iteration — `session_173.md`, `session_174.md`, `remediation-plan-v72.md` all exist. `.env` and `db/` need recreation (gitignored). Let me set up the iteration plan.
While deps install, I'll review the core docs.
v72 shipped at `4738512`; this session runs the **v73 cycle**. Let me read the remediation plan (the v73 queue) and session_173 narrative.
Full context established. This session runs the **v73 cycle**: NEW-pair program's last never-shot surfaces (login + calculator mobile 390 twins), axe watch, 67th standing checks, pin-only line. Let me check install progress and review operational scripts.
Now let me verify how the Calculate button behaves at mobile viewport in the clone source:
The v73 surfaces are confirmed: login mobile 390 twin + calculator dialog mobile 390 twin (both hover-capable via real mouse moves). Let me check install status and set up the DB.
npm ci finished. Setting up the database now:
Environment ready (e2e.db is self-provisioned by global-setup). Starting **F0 — baseline chain**. First the orphaned-server check:
Lint ✓ · typecheck ✓ · 108/108 unit ✓. Now the build:
Build ✓ with robots+sitemap. Now the e2e suite in 3 chunks:
失败 —— 让我来诊断一下：
Fresh sandbox — Playwright browsers need installing:
Chunk 1: 100 passed. Chunk 2:
277 executions = 274 chromium + 3 setups = **275 unique e2e ✓** (exact documented v72 state). Now smoke:
**F0 已完成 —— baseline chain 完全通过**（lint · typecheck · 108 个单元测试 · 带 robots+sitemap 的构建 · 275 个 e2e 测试 · 35/35 冒烟测试）。现在进行 **F1 —— axe-core 监控**：
**F1 COMPLETE — axe watch NO DRIFT** (npm-latest 4.14.0 both packages, only rc/next prereleases; v68 dedupe state holds; engine-contract pin GREEN). Now **F2 — 67th standing checks**. Reading the v66 scripts:
Reference side: all four bugs STILL LIVE ✓, census clean (67th drift check), SEO live. Now clone side:
**F2 COMPLETE — 67th standing checks ALL GREEN** (mobile menu verified the 67th consecutive time; ref's four bugs all live; census clean; SEO live). Now **F3 — the NEW-pair program**. Let me first check the v66 calculator pair findings for the line-item state question:
Now let me study the calculator dialog's mobile geometry and the with-server harness:
The store confirms line-item writes recalculate the parent's amount — the v66 fixture/restore discipline is required. Now writing the v73 probe family. First the reference side:
Now the clone-side probe (with the v66 line-item fixture discipline):
Now the VLM compare script:
Now run the reference-side probe:
The reference calculator shot failed — the Rent card sits below the fold at 390 (y≈1195 > 844 viewport), so the hover/click missed. Adding scroll-into-view before hover:
Reference calculator dialog confirmed live at 390 (Rent Calculator, 1 Contents Insurance row, full-viewport overlay 390×844). Applying the same scroll fix to the clone script:
Clone side complete with full fixture restore verified ("3 items · $2235.00" + Rent "$1850.00"). Note the geometry question: the clone's Radix panel measured 358×413 centered vs the reference census catching its full-viewport wrapper (0,0,390,844) — the arbitration will measure the actual panels. First the seedcheck, then the VLM compare:
**PAIR 1 (login mobile): VERDICT IDENTICAL — CLEAN.** PAIR 2 (calculator): DIFFERENT with 2 flags (the "Will update" span — the documented v66 DATA-CONDITIONAL class — and a scrim-opacity claim). Both need DOM arbitration. Let me study the arbitration scaffolding:
Now let me check the clone's DialogContent panel classes for the census:
Both modal systems confirmed. Now writing the v73 arbitration census:
The reference census succeeded with rich data (scrim rgba(26,58,46,0.5)+blur(8px) — matching the clone's overlay; panel x16 y216 w358 h413 — byte-identical to the clone's). But the clone side broke: the unquoted heredoc expanded `\$1850` → `$1` unbound. Let me check DB state and fix the script:
DB intact (exact seed state). Now fixing the clone section — quoted heredoc + census via env var:
The clone dialog didn't open again ("no add item" → census err). Let me debug the clone-side flow manually:
Found it — `echo "\$POS"` survived the rewrite; under the quoted heredoc that echoes the literal text `$POS`. Fixing:
**BOTH SIDES CENSUSED — the arbitration verdict is complete:**

| Axis | Reference @390 | Clone @390 | Verdict |
|---|---|---|---|
| Scrim | rgba(26,58,46,0.5), opacity 1, blur(8px), 390×844 | **identical** | flag = **PERCEPTION ARTIFACT** (only hasText differs — the documented v72 wrapper-vs-sibling structural class) |
| Panel | x16 y216 w358 h413, maxW 768, maxH 717.4, r16, white | **identical** | byte-identical (pos static-vs-fixed = v72 structural class; shadow = the documented v49/v66 accepted lead-divergence) |
| Header/close/title/desc/summary/amount/row/addBtn | full chrome | **identical** | byte-identical |
| willUpdateSpan | absent (Rent native $25 === total $25) | present 12px rgb(234,88,12) | the documented v66 **DATA-CONDITIONAL class** |

**NO NEW GAP — the v73 iteration is PIN-ONLY.** The never-pinned axis: the calculator dialog's mobile-390 computed census. Writing the remediation plan first:
There's already a v53 mobile census — let me see what it covers to find the truly never-pinned axes:
The v53 pin already covers most panel axes. Let me find the truly never-pinned axes — checking existing scrim/amount/desc assertions:
All coverage mapped. The never-pinned axes: the calculator's **scrim chrome** (bg/blur/geometry — only the details-sheet overlay was pinned), the **summary-amount full chrome** (fs/fw/lh), the **basedOn + desc line chrome** at 390. Writing the remediation plan:
Now writing the F4 pin at the calculator.spec.ts tail:
Now run the pin (GREEN expected):
**PIN GREEN on first run.** Now the pin-sanity mutation check — mutate the scrim's blur, rebuild standalone, verify FAIL:
**Pin-sanity VERIFIED** — the mutation fails the pin at exactly the scrim axis (line 1373). Restoring:
**F4 COMPLETE — PIN-ONLY holds** (`git diff src/` = 0 lines). Now **F5 — full chain re-run**. First gates:
278 executions = 275 chromium + 3 setups = **276 unique e2e ✓** (+1). Now smoke + screenshots byte-compare:
**F5 已完成 — 完整链路完全绿灯 (276 个 e2e · 35 个 smoke · 16/16 张截图字节一致 · seedcheck 已通过)。** 现在开始进行文档对齐。正在查找 v72 锚点：
Now executing docs alignment. D2 — CLAUDE.md:
D1 — AGENTS.md v73 paragraph:
D3 — README.md. Finding the anchors:
D4 — zero-balance_SKILL.md. Finding the Session 107 audit row and state lines:
D5 — PAD revision block:
The PAD title has stayed v1.1.27 across v71/v72 (only revision blocks increment). Reverting my title bump to match the established convention:
D6 — probe README v73 section:
D7 — worklog Session 107 entry + ledger update:
Now the formal session narrative — `docs/session_175.md`:
All docs aligned. Final pre-ship verification — lint gate re-run + changeset review:
Changeset clean (`src/` untouched — PIN-ONLY, no key material). Now the ship — reading the SSH wrapper runbook:
No ssh binary and no paramiko — deploying the Appendix A shim. Reading it:
Deploying the ship infrastructure — paramiko, shim, operator key:
The wrapper needs no paramiko — only the shim does (via `/usr/bin/python3`). Deploying the shim:
Now materializing the operator key and verifying its fingerprint:
**Fingerprint MATCHES** the documented one. Pre-commit script checks, then the commit:
Commit `da2876e` created. Dry-run push with the shim on PATH:
Dry-run clean (auth ✓, fast-forward accepted). Executing the real push:
**PUSHED ✅ — remote verified: `main @ da2876e == local HEAD`.** Now the cleanup — shred the operator key and verify:
Push verified, keys shredded, tree clean. Final step per the established pattern — the session transcript doc + its "update session log" commit:
The wrapper already verified the push internally (its OK line follows remote verification). One final explicit remote check, then full cleanup:
All verified. Final housekeeping — the workspace worklog:
**v73 iteration complete and shipped ✅** — `main @ 2eef068` on `git@github.com:nordeim/zero-balance.git`, remote-verified via the SSH wrapper, key material shredded.

## What this session did

**Environment rebuilt** (the workspace was reset): fresh clone from `main @ c48f724`, `.env` + `db/` re-provisioned, `npm ci`, Playwright browsers re-installed (the reset wiped the cache — caught by the F0 first pass).

**The full iteration cycle, all green:**
- **F0 baseline** — lint · typecheck · 108 unit · build (robots+sitemap) · 275 e2e · 35/35 smoke, exactly the documented v72 state
- **F1 axe watch** — NO DRIFT (4.14.0 stable, v68 dedupe holds, engine-contract pin green)
- **F2 67th standing checks** — mobile menu verified the 67th consecutive time; the reference's four bugs all still live; census clean
- **F3 the NEW-pair program's LAST never-shot surfaces** — the **login mobile 390 twin: VERDICT IDENTICAL, zero flags**; the **calculator mobile 390 twin: CLEAN** (the scrim "lighter" claim a perception artifact — chrome byte-identical; the will-update span the documented data-conditional class). **With these pairs the NEW-pair program is complete** — every surface now has both a desktop pair and a mobile twin.
- **F4 one new pin** (276 e2e) — the calculator's scrim + summary-text chrome at 390, never pinned before; pin-sanity mutation proven to fail and restore; `src/` untouched (PIN-ONLY)
- **F5 verification chain** — fully green; 16/16 screenshots byte-identical (5th consecutive set); seedcheck exact
- **Docs** — remediation-plan-v73.md, session_175.md, session_176.md, worklog Session 107, and 8 alignment updates across AGENTS/CLAUDE/README/SKILL/PAD/probe-README

**Two new probe lessons documented**: the mobile-fold `scrollIntoView` before hover (out-of-viewport mouse moves never engage `:hover`), and the quoted-heredoc dollar trap (env-injected census).

**Suggested next**: run the **v74 cycle** — the NEW-pair program being complete, the cadence rotates to the re-run cycle's oldest candidate (the v58-era savings pair, last re-shot v65) plus the axe watch; the full queue is in `docs/remediation-plan-v73.md`.
