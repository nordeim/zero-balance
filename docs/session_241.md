The workspace exists with prior work. Let me check git status and refresh from remote.
Workspace is on main, clean. Let me pull the latest and check for the latest session docs.
Pull completed — `session_238.md` is new. Let me set up the task plan, then review all docs.
AGENTS.md 很大 (316KB)。让我先检查一下它的结构，并阅读最新的部分。
Now let me read CLAUDE.md, README.md, and the latest session docs.
现在让我阅读最新的会话文档和工作日志尾部。
Now the worklog tail and probe README for the v99 queue details.
The picture is clear. The v98 cycle (Session 133) is complete and pushed; **v99 targets the v93-era LOGIN + CALCULATOR pair (sixth re-run)**. Let me validate the workspace state and audit the commits since the v98 push.
Workspace is the **carried-over class** (session-log-only commits since v98 push, zero src/lockfile deltas) — no re-provisioning needed. The parent-shell `DATABASE_URL` pollution is present as documented; `env -u` discipline applies. Now let me check the skills catalog and verify the v99 queue against the probe lineage.
Let me perform the pre-execution ledger verification — reading `vlm-shots-v93.sh`'s own header per protocol.
Ledger verification complete: `vlm-shots-v93.sh`'s header confirms the v99 target — **the LOGIN + CALCULATOR pair's SIXTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99]**, now the oldest remaining [v93 < v94 < v95 < v96 < v97 < v98] — matching the v98 plan's queue suggestion (the 22nd consecutive agreement). Let me check the probe README and derivation scripts.
v99 queue confirmed. Now starting **F0 — the baseline chain**. First the seedcheck.
Seedcheck exact. Now the baseline chain — lint and typecheck first.
Lint ✓ · typecheck ✓ · 108/108 unit ✓. Now the production build.
Build ✓ with robots + sitemap prerendered. Now the e2e suite in three chunks — let me derive the split from the v98 pattern.
Let me count tests per spec to compose the three chunks.
Running the e2e suite in three chunks (113 + 98 + 89 = 300 spec tests + 3 setup runs = 301 unique).
One failure in `not-found.spec.ts` head-parity test. Let me investigate — re-run with details.
Single-spec re-run is green — likely a flake. Let me re-run the full chunk 3 to confirm zero flakes.
Chunk 3 re-run: 90/90 green — the single failure was a one-time timing flake (clean on both re-runs). F0 e2e: 114+99+90 = 303 executions = 301 unique. Now the smoke test.
**F0 baseline FULLY GREEN.** Now the production-seams re-audit (auth, db-path, SEO pair, Tailwind v4 mitigations, skills/ exclusion).
All seams verified. **F0 complete.** Now **F1 — the axe-core watch**.
**F1: NO DRIFT** (4.14.0 both sides; only rc/next sha prereleases beyond; dedupe holds; engine-contract pin 2 passed). Now **F2 — deriving the 93rd standing checks** from the v92 pair.
Derived cleanly. Let me inspect the reference-side standing script before executing.
Running the reference-side standing checks (93rd).
Reference side: **all four bugs live, census clean on first read, SEO pair live.** Now the clone side — let me check what it needs.
**F2 complete — mobile menu VERIFIED WORKING the 93rd consecutive time; all four reference bugs live; census clean.** Now **F3 — deriving the v99 probe series from the v93 lineage**. Let me study the derivation script pattern first.
现在让我检查所有 v93 系列文件的头信息，以构建 v99 推导。
Line markers verified. Now let me catalog all `93` tokens in the v93 series files to build a complete swap list.
Let me check the full vlm-compare-v93.mjs header for legitimate pin-provenance tokens.
Now writing the v99 series derivation script with the exact cataloged fragments.
Two fixes needed: the clone-login fragment has a line break I missed, and the v87-pin whitelist needs adjusting. Let me patch the derivation script.
Series derived cleanly. Now building the two-half census form from arbit-v99.sh.
Structure identical to v93. Writing build-twohalf-v99.py.
Two-half census built with byte-identical blocks. Now executing the probe series — reference-side shots first (calculator + login).
Reference shots captured. Now the clone-side twins.
The clone calculator script timed out. Let me analyze its flow and sleeps.
Sleep profile is modest (~33s of sleeps). Likely a hung agent-browser call. Let me check for stale processes and re-run with streaming + longer timeout.
Clone calculator shots clean — fixture fully restored ($2235.00 verified). Now the clone login shots.
All four shots captured. Now the VLM pairwise comparison.
**Calculator verdict: DIFFERENT** (3 flags — expected documented classes); **Login verdict: IDENTICAL**. Now the two-half census for DOM arbitration — reference half first.
Reference half captured — key arbitration facts: reference's `hasWillUpdateSpan: false` and `actionsAtRest opacity: 0` (both VLM flags point to documented classes). Reaping budget, then the clone half.
Census halves complete — chrome byte-identical on every axis except the documented classes. One anomaly: the clone census includes a `close` field the reference lacks. Let me check the census JS finder.
The close-button finder uses aria-label/text patterns — the reference's unlabelled SVG close button (the v98-documented class) doesn't match. Let me verify geometrically with a one-shot reference probe.
The card finder failed. Let me check the working finder from the shots script.
The shots script uses explicit `mouse down` + `mouse up` (the full pointer sequence the reference needs). Let me fix my probe.
**关闭按钮在几何上逐字节一致**（两侧均为 36×36/6px/transparent；参考按钮是无标签的 SVG —— v98 查找器类）。**F3 裁决：无新的克隆差异 —— 仅限 PIN。** 现在进行 F4 —— 覆盖图调研，以在 login/calculator 表面上寻找从未进行过 PIN 的家族。
计算器表面已被彻底锁定。让我检查一下登录视图的 OR 分割线覆盖率——即 census 的 `hasORDivider` 轴。
The OR divider's computed chrome is never pinned. Let me check the Google button's geometry coverage in v7/v45 pins to map the full candidate family.
**Found the never-pinned family: the login card's SOCIAL-LOGIN ROW** — the OR divider's computed chrome (text typography + rule lines) + the Google button's geometry/typography (v7 pins colors only; v45 pins hover shadow only; v9 notes its 16px text but never pins it). Let me design the supplemental two-half census — first inspecting the clone's login DOM.
现在让我检查克隆登录卡片中的卡片结构（表单与 GoogleBlock 的顺序），然后构建补充的人口普查。
Now writing the supplemental two-half census builder for the social-row family.
Reference half shows `signInToGoogle: -358` — suggesting the Google block sits ABOVE the form on the reference. Let me check the clone's card layout order, then run the clone half.
The clone also renders `GoogleBlock` BEFORE `AuthForm` (line 583-584) — the negative rhythm is the correct both-sides form. Now the clone half.
**Social-row census: BYTE-IDENTICAL across sides on every axis** (google full chrome, orText chrome, rule {1px, rgb(226,232,240), w 368}, rhythm 32; the SPAN/DIV tag the inert construct class). Now let me verify the mutation target line and spec tail, then write the plan.
All pre-execution validations complete. Writing the remediation plan v99 BEFORE the pin's execution.
Plan validated and saved. Now appending the v99 pin to login-parity.spec.ts.
**Pin GREEN on first run.** Now the pin-sanity mutation — line-scoped `rounded-xl` → `rounded-lg` at login-card.tsx:172, then the REBUILD (the v98 discipline).
The build failed on a TS error in my pin (the `card` variable's inferred type) — need to fix the spec's typing, then rebuild with the mutation still in place.
Only the v99 pin red under the mutation (29 green). Let me verify the failure diff is the radius axis alone.
The failure diff is the radius axis alone (`12px`→`8px`) — cascade-free as planned. Now restore and rebuild.
**F4 complete — 30/30 green post-restore.** Now **F5 — the full chain re-run**.
**F5 e2e: 114+100+90 = 304 chunk executions = 302 unique, zero flakes.** Now the smoke test.
F5 chain fully green. Now the screenshots regeneration + byte-compare.
**Screenshots: 16/16 BYTE-IDENTICAL** (the same-day regeneration law). Final seedcheck, then the docs alignment.
F5 complete. Now **D1-D7 docs alignment**. Starting with D1 (AGENTS.md v99 paragraph) and D2 (CLAUDE.md counts).
Now D6 — the probe README's v99 section.
Now D1 — the AGENTS.md v99 paragraph.
Now D7 — the session_239.md narrative and the worklog Session 134 entry.
D1-D7 已对齐。让我检查一下是否有遗留的陈旧计数引用，然后更新共享的工作空间 `worklog`。
Historical mentions only — clean. Now updating the shared workspace worklog.
Now the pre-ship gates and commit.
All gates green — 27 files, +2844/−13, zero src/ changes. Now the commit + SSH-wrapper push. Let me review the runbook first.
Runbook understood — the wrapper needs the `--remote` override (the v97/v98 lesson). First, the commit.
Commit `4b0b6aa` created, tree clean. Now verifying the key fingerprint and the ssh shim.
`python3.13` has paramiko 5.1.0 and the shim's shebang matches. Verifying the fingerprint.
Fingerprint matches the documented key. Dry-run with the remote override.
Dry-run clean — fast-forward `74a206e..4b0b6aa`. Executing the real push.
**Push verified** — remote main @ `4b0b6aa` == local HEAD (independent HTTPS check), keys shredded, tree clean. Following the established pattern, now the session-log follow-up commit.
The **v99 parity cycle (Session 134)** is complete and pushed to `main @ b43db6f` — remote verified via independent HTTPS re-check, tree clean, keys shredded with zero residue.

**What shipped (PIN-ONLY, zero src/ changes, +1 e2e = 302):**
- **Baseline all green** on the carried-over workspace (301 e2e, 35/35 smoke); axe watch no drift; 93rd standing checks — mobile menu working the 93rd consecutive time
- **LOGIN + CALCULATOR pair's 6th re-run**: calculator flags DOM-arbitrated to documented classes, login IDENTICAL, census zero-drift — **no new clone gap**
- **New pin**: login social-row census (OR divider + Google button chrome, measured byte-identical both sides, mutation-verified single-axis)
- Screenshots 16/16 byte-identical; docs aligned D1–D7; `remediation-plan-v99.md` + `session_239/240.md` saved

**Next:** per the rotation ledger, v100 targets the v94-era NETWORTH + DRILL-DOWN pair — say "continue v100" to proceed, or request adjustments.
