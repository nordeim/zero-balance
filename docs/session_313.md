I'll continue the zero-balance maintenance cycle. The new instruction references `session_310.md`, `remediation-plan-v127.md`, and `session_311.md` — following the established pattern, this means the v127 cycle was completed elsewhere and this session is the **v128 cycle**. Let me verify local state first.
Repo exists at `main` with HEAD `ce00280`. The v127 cycle is complete (commit `c8c3850`) — this session is the **v128 cycle**. The v127 commit message already names the v128 queue candidate: *the v122-era SAVINGS pair at desktop 1280x800 FULL-PAGE, eleventh re-run*. Let me sync and read the referenced docs.
Remote has one more commit (`597709a` — the session_311.md tail). Pulling now.
HEAD 已同步至 `597709a`。现在让我阅读参考文档 —— 首先是 session_311.md（操作员的尾部记录，其中可能包含 v128 指令），然后是 session_310.md 和 remediation-plan-v127.md。
session_310.md (v127 delivery record) and session_311.md (operator's v127 transcript) are clear. Now the remediation plan and worklog tail:
工作日志（worklog）是按最新优先原则排序的（会话 162 在顶部）。让我读取一下它的头部以及探测 README 的 v128 队列：
v127 record fully internalized. Now verifying the v128 queue against the authoritative header (`vlm-shots-v122.sh`) and checking the workspace environment state:
Workstation is the **CARRIED-OVER class** — node_modules (354 pkgs), `.env` correct, `db/` fresh from v127 (Oct 27 05:59), both chromium pairs, zod v4 intact, next 16.4.3. Now verifying the full v122 lineage header and the infrastructure state:
The v122 census contract: **120 axes / 80 identical / 40 documented-class deltas** on the SAVINGS surface. Now let me find the v122 bracket listing and the v122 pin, plus review the core docs' current state:
The first grep shows the v122 header carries no explicit bracket — the lineage must be verified by tracing the era chain through the headers. Let me trace it, and retry the docs read (previous command timed out):
Lineage chain verified: **v58 (original) → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 = 11 entries, TENTH re-run (per the v122 plan title)** — so **v128 = the ELEVENTH re-run**, matching the README queue. This will be the **51st consecutive queue/ledger agreement**.

Now reviewing the core docs' current state lines and checking for stale servers:
CLAUDE.md confirms the state line: **108 unit / 330 e2e**. The AGENTS tail contains the iteration paragraphs (v122→v127 in the last 12 giant lines). Let me do a compact validation of the remaining docs' v127 alignment:
文档已对齐（AGENTS v127 ¶、README plan row、SKILL Session 162 + 108/330/35）。两处备注：PAD 标题格式需要不同的 grep，并且**在 :3000 上有一个陈旧的 next-server（pid 23810）** —— 这是 v126 周期的已知类别，将在 dev-evidence 阶段处理。让我检查一下 PAD 格式和 seedcheck 基础设施：
PAD is at v1.1.84 with the v127 paragraph — all docs validated. Now let me confirm the two-part commit convention (ce00280) and re-anchor on the repo skills per the instruction:
Two-part convention confirmed (tail commit = 2-line post-push paragraph on session_310.md). Let me re-anchor on the skills per the instruction — headings of web-application SKILL + the catalog's relevant entries:
Skills re-anchored — the standing audit form (§3 db-path contract, §12 TW4, §14 three tiers, §16 security) maps to the production-seam audit. **Phase 1 — F0 baseline** begins: seedcheck first, before any gate.
**Seedcheck EXACT: 7/1850/2235/0/3/2** ✓. Now F0b — the two watches:
Both watches GREEN: **npm-audit 0 vulnerabilities (19th re-check)** · **axe-core NO DRIFT** (engine 4.14.0 == npm-latest, only the canary prerelease beyond, dedupe holds at 1). Now the F0c gates:
Lint ✓ · Typecheck ✓ · **108/108 unit** ✓. Now the production build:
Build ✓ — robots.txt + sitemap.xml prerendered, all five views static. Now the e2e baseline. Per the standing convention, I'll derive the per-file counts authoritatively via `--list` BEFORE any chunk runs:
The `--list` total says **330 tests in 24 files** (authoritative) but my per-file grep overcounts by exactly +1/file. Let me inspect the raw output form:
Per-file counts derived (the +1 was the [setup] project listed with every filtered file): **329 specs + 1 setup = 330 in 24 files** ✓ — exactly the v127 ship form (items 48 = 47 + the v127 pin). Chunk composition: **ch1 90 · ch2 87 · ch3 74 · ch4 82 → 333 executions = 330 unique**. Running the chunks:
**F0c e2e: 90+87+74+82 = 333 executions = 330 unique, ZERO flakes** ✓. Now the smoke suite:
**Smoke: 35/35** ✓ — **F0 baseline FULLY GREEN on the first chain, zero repairs**. Now F0d — the standing production-seam audit:
**F0d production-seam audit: CLEAN** (db-path 19-case unit file + .env contract, auth, SEO pair prerendered, TW4 `@variant` mitigations, three tiers, skills/ excluded). **F0 COMPLETE — fully green on the first chain, zero repairs, the CARRIED-OVER workspace class.**

Now **F2 — the 122nd standing checks**. Let me map the v121 pair's token structure before deriving:
Token map is clean (no substring traps: `121` occurrences decompose exactly into 121st/v121/ref121/clone121). Let me study the persisted derivation form, then write `derive-standing-v128.py`:
122nd pair derived cleanly (normalize-back diff clean, zero old tokens, bash -n clean). Executing the reference side first:
**Reference side ALL GREEN** — the four bugs all live (toast-blocker `hitIsBurgerChild:false`, sheet-trap `overlayCount:1`, no-landmark, docSW 464 overflow), data census clean on FIRST reads, SEO pair live. Now the clone half:
**F2 COMPLETE — the 122nd standing checks ALL GREEN**: the clone's mobile menu VERIFIED WORKING the **122nd consecutive time** (R1-R4 + SEO pair), seedcheck exact after. 

Now **F3 — the v128 re-run pair** (SAVINGS at 1280×800 FULL-PAGE). Studying the v127 derivation form and the v122 lineage structure:
Now let me examine the four v122 lineage files' headers to catalog every history-correction site:
Now let me sweep all four v122 files for every era token and history-correction site:
Correction sites cataloged — the v122 lineage is simpler than the v121 form (one plan-pointer, no later-pairs list; deeper v58/v65/v74/v80/v98 tokens are legitimate axis-provenance citations). Writing `derive-v128-series.py`:
**Series derived cleanly — 4/4 corrections on the first run, zero residual, line counts preserved (50/42/39/262).** Now the two-half builder + comparator. Let me study the v122 forms:
Let me check the session-token handling in the v121/v127 builders to get the swap pattern right:
The v122 builder carries `refarbit122` (line 26) — one explicit session-token swap needed. Let me check the comparator derivation form:
I have both derivation forms. Writing `derive-build-twohalf-v128.py` and `derive-compare-v128.py`:
Halves built — census block md5 `891ab9b6`, 153 lines, byte-identical. Now the three-way md5 verification against the source:
**F3 derivations complete — md5 contract 891ab9b6 HELD three-way.** Now executing the halves. Reference-side shots first:
The clone shot is only 4.7KB (vs the reference's 62KB) — likely a blank/error page, with a "no inputs" login miss. Diagnosing:
Server booted fine — the issue is on the page/login side. Let me inspect the clone shots script's flow:
The clone script has no login retry loop (unlike the ref side) — a transient first-load race ("no inputs" → unauthenticated → the shot captured the login page). Re-running the clone half:
Clone shot now 169KB (the authenticated savings view — 2 goal cards). Running the VLM pairwise comparison, pass 1 of 2 with full log capture:
The VLM reveals the real issue: **the clone shot captured the LOGIN page** — the login eval failed both runs ("no inputs"). The standing-checks login worked minutes earlier on the same server form, so this is specific to the fresh-session first-load. Diagnosing directly:
**Root cause found: "OS can't spawn worker thread: Resource temporarily unavailable"** — sandbox resource exhaustion. The stale `:3000` next-server (pid 23810) plus accumulated browser processes are the culprits. Reaping:
Multiple stale agent-browser daemon trees (from the v127 runs) + the stale next-server are exhausting the sandbox (only 1.1GB available of 4GB). Reaping all stale processes:
Memory recovered (1155MB → 2545MB available), ports clear. Verifying agent-browser is healthy again and retrying the clone shots:
Clone login **"submitted"** on first attempt after the reap — shot now 71KB (the real savings view). Finishing the stale-server reap (SIGKILL per the v126 hung-server class), then VLM pass 1:
**Pass 1: SAVINGS DIFFERENT** — every flag in the documented classes (seed-count grid, v57 data-conditional payment chips, classification-value badges, seed-data). Pass 2:
**Pass 2: DIFFERENT — both passes the documented form, every flag in documented classes (user-identity avatar, seed-count, data-conditional, seed-data). No FAB claim — no disproof needed.** Now the two-half census — reference half first:
Reference half clean — values reading the documented v122 classes exactly (grid 309.328px×3/960, card 309×200, footer childCount 1, badgeRow h 22/n 3, the "need" red-outlined badge). Clone half:
**F3 COMPLETE: 120 axes — 80 identical + 40 documented-class deltas, ZERO new — the v122 census values reproduced EXACTLY. NO NEW CLONE GAP — v128 is PIN-ONLY for src/.**

Now **F4 — the pin-candidate survey** on the savings surface. Mapping what's already pinned on `/savings`:
Coverage map so far: v51/v54 (390 mobile), v58/v74/v80/v86 (1280 card/header), v92 (filter interior at 1280), v116/v122 (kebab hover+open), v98 (menu panel), v45 (card hover/action row). Let me examine the remaining gaps — the v92 filter pin's exact coverage, the v109 Add-button coverage, and the search-input focus state:
v92 holds the at-rest chrome (search + icon + triggers + card). Now checking the v109 Add-button coverage and any existing focus/hover-end-state pins on filter elements:
Focus families held (v37 S1/S2). Let me check the v116 kebab pin's exact axes (reveal ladder vs hover chrome) and the v51 mobile census coverage:
v116 holds at-rest chrome + the card-hover reveal (opacity ladder), and v122 the open+parked state. The trigger's **OWN hover end-state** (pointer on the trigger itself — its hover tint) may be the never-pinned path. Checking the source:
**Candidate found: the kebab-trigger's OWN-HOVER end-state** — the trigger carries `hover:bg-accent hover:text-accent-foreground` (item-card.tsx:139) but has NO `hover:opacity-100`; its reveal comes from group-hover/focus/open (all pinned: v45/v116/v36/v122). The own-hover **tint** is never pinned at any viewport. Verifying the token values and the v127 hover-census form:
I have the full form. Now writing `kebabhover-arbit-v128.sh` — the both-sides one-shot census for the trigger's OWN-HOVER end-state (the reveal family's never-pinned tint path):
One test hit for `hover:bg-accent` — must check it before proceeding (collision map):
**Collision map resolved**: the dialog-buttons hit is a class-token check on the DIALOG X button (a different element/file) — immune to a line-scoped mutation at item-card.tsx:139 (the file's sole occurrence). The trigger's own-hover computed tint is held by **no spec**. Writing the both-sides census:
**The census measured cleanly BOTH SIDES — the parity contract IDENTICAL on the full ladder**: at-rest (opacity 0, bg transparent, color rgb(10,10,10)) → OWN-HOVERED (**opacity 1, bg rgb(245,245,245) — the accent tint, color rgb(23,23,23) — accent-foreground**, hoverMatch+cardHover true) → restored. Byte-identical both sides, w 36/h 36/radius 6px, seedcheck exact after.

Per the fixed protocol, writing the remediation plan **BEFORE** the pin append:
Plan saved. Now studying the v127 append-pin form and the items.spec.ts tail before appending the v128 pin:
Let me verify the savings card's hover action-row structure (button widths matter for the finder's uniqueness):
The action row is expense-only — savings cards carry just the 36×36 trigger. The finder is safe. Writing `append-pin-v128.py`:
**Pin GREEN on the first run.** Now the pin-sanity mutation — the alpha-modifier value-only form at item-card.tsx:139:
**SOLE FAILURE verified live — 1 failed (the v128 pin) + 49 green** in the full items file (v116/v121/v122/v127 all immune as designed). Verifying the diff is exactly the predicted line:
The diff is EXACTLY the predicted line — the hovered rung's `bg` axis alone flips (`rgb(245,245,245)` → the mutated `lab(...0.5)` alpha form), with `hoverMatch true` / `opacity "1"` / `color` preserved — the at-rest + restored rungs unaffected. Now the networth immunity file:
**Networth immunity: 37/37 green.** Restoring the mutation and rebuilding:
**Post-restore regression GREEN: 86 passed** (items 49 + networth 36 + setup). **F4 COMPLETE.** Updating the plan's ToDo statuses, then F5 — the ship chain:
The catalog script is `scripts/capture-screenshots.mjs`. Backing up the committed set, re-capturing, and byte-comparing:
**16/16 byte-identical — the same-day law holds, no refresh needed.** Now the dev evidence — deriving the v128 dev-shots pair from v127 (version-swap-only):
The dev-server boot timed out — the v124/v126 lesson: a SIGKILLed dev server leaves `.next/dev/lock` behind. Checking and removing:
A new orphan dev server (pid 6377) from the failed run. Killing it and retrying:
**Dev evidence captured + menu proof: /income, docSW 390, navLandmark true** ✓. Byte-compare + VLM verification:
**Dev evidence: 4/4 byte-identical + VLM-verified** (menu open with all links + brand; sheet closed post-nav; dashboard clean). Now the ship-chain gates — first the authoritative new count:
**331 tests in 24 files** ✓. Running the ship-chain gates:
**F5 SHIP CHAIN FULLY GREEN: 331 e2e zero flakes (334 executions in 4 chunks) · 35/35 smoke · 16+4 shots byte-identical · VLM-verified.**

Now **D1–D7 docs alignment**. First the v129 queue verification — the next-oldest candidate is the v123-era LOGIN+CALCULATOR pair. Checking its lineage header:
v123 header verified: the LOGIN+CALCULATOR pair, TENTH re-run on the 11-entry bracket [v59→...→v123] — so **v129 = the ELEVENTH re-run**. Now studying the v127 alignment script form:
The v127 alignment form is clear. Now gathering the D0 anchors — the exact tails of the v127 paragraphs/rows in each doc:
All anchors gathered. Checking the PAD block spacing, then writing the alignment script:
D1–D5 aligned. Now D6 — the probe README. Checking its section structure:
The mechanics are clear. Writing `align-probereadme-v128.py` — the v128 section + the v129 queue:
Sanity check failed — let me inspect what's actually before the v121 anchor:
The queue text is there — but wrapped across lines ("so\nv128 = ..."). Fixing the sanity check to normalize whitespace:
D6 done. Now the worklog Session 163 entry — studying the insert form:
Worklog updated. Now D7 — writing `session_312.md` (the v128 delivery record, two-part convention — the post-push paragraph comes in the tail commit):
D7 complete. Now the pre-commit changeset review:
Changeset is exactly the expected form — src/ ZERO, tests +136, docs + scripts aligned, .env.example untouched. Updating the plan ToDo, then preparing the commit:
Procedure confirmed — shim + paramiko in place. Creating the parity commit with the long-form message:
**Parity commit `47d8e9b` created.** Now the SSH-wrapper push — staging the key outside the repo, verifying the fingerprint:
Fingerprint matches the lineage record (`4FSV1Pro...`). Dry-run with the shim on PATH:
The wrapper defaulted to the wrong remote (`task-management.git`) — it needs the explicit `--remote` argument per the v127 form. Re-running:
**Dry-run clean** — remote at `597709a`, fast-forward to `47d8e9b` authorized. Real push:
**PUSHED — remote main @ `47d8e9b` == local HEAD, HTTPS verified byte-for-byte.** Now the tail commit — appending the post-push verification paragraph to session_312.md:
**Both pushes verified — remote main @ `f85bbec` == HEAD, working tree clean.** Final housekeeping — shredding the staged key and updating the workspace worklog:
**v128 cycle delivered and pushed** — remote `main @ f85bbec`, working tree clean, src/ unchanged (17th consecutive PIN-ONLY cycle).

**Highlights:**
- **Baseline fully green on the first chain** (carried-over workspace): 108 unit · 330 e2e zero flakes · 35/35 smoke · both watches green
- **122nd standing checks all green** — mobile menu working the 122nd consecutive pass
- **SAVINGS pair ELEVENTH re-run** (51st queue/ledger agreement): VLM both passes in documented classes; census 120 axes, zero new — the v122 values reproduced exactly
- **New pin**: the kebab-trigger's own-hover end-state (the never-pinned accent tint) — 331 e2e, mutation sole-failure verified live
- **New lesson**: the carried-over sandbox's stale browser daemons exhausted the 4GB memory — reaped and codified

**Next:** v129 — the v123-era LOGIN + CALCULATOR pair, awaiting your next instruction.
