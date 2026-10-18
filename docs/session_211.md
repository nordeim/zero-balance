I'll continue the zero-balance remediation workflow. Note the session documents have been updated to session_208/session_209/remediation-plan-v86. Let me set up the task tracking and start with refreshing the workspace.
The workspace exists with substantial prior work (session_208, remediation-plan-v86, tests, screenshots). Let me refresh the workspace with git pull and check the current state.
Workspace is on main, clean, up-to-date with origin. Let me pull the latest and check for the session_209.md document.
Workspace refreshed: fast-forward to `40cee12`, bringing in `docs/session_209.md`. Now let me review the core documents, starting with the newest session doc and the key architecture docs.
Session 209 confirms: v86 cycle is complete and pushed; the next step is the **v87 cycle** targeting the v81-era login + calculator pair. Let me review the core docs and remediation plan v86.
The persisted files add double line-numbering. Let me read the originals directly in chunks.
One giant line (the v86 paragraph) is bloating reads. Let me extract content with line-length limits.
Now let me read the worklog's latest entry and remediation-plan-v86.md's structure to understand the v87 cycle requirements.
The picture is clear: v86 is pushed; the v87 cycle targets the **v81-era login + calculator pair**. Let me read the v86 plan structure (the template for v87) and verify the environment state.
I now have the full picture of the v86 plan structure. Let me mark docs review progress and verify the environment + rotation ledger for the v87 target.
Environment is fully provisioned (.env correct, db/ at root, chromium-1243). Now let me verify the rotation ledger for the v87 target and audit the v86 commit's PIN-ONLY claim.
v86 commit verified PIN-ONLY (27 files, +1500/-5, zero src/ changes; the two commits since are session-log-only). Now let me verify the rotation ledger for the v87 target pair.
Rotation ledger confirmed: the login+calculator pair (v59 → v66 → v75 → v81) is due its **fourth re-run** at v87 — the tenth consecutive queue/ledger agreement. Let me check the skills catalog for the relevant audit skills, then examine the v81 probe series I'll derive v87 from.
The relevant skills (agent-browser, tdd, verification-and-review-protocol, clone-app-pat-pro, tailwind-patterns) are confirmed in the catalog. Now let me examine the v81 probe series I'll derive v87 from.
Now let me look at the census scripts (arbit-v81.sh, login-census-ref-v81.sh) and the v86 derivation pattern from v80.
I have the full v81 series understanding. Let me check the v86 probe derivation pattern (how v86 was derived from v80) and the with-server.sh helper.
The derivation pattern is clear. Now let me start the v87 cycle. First, check for orphaned servers and run the seedcheck + baseline chain (F0).
23 spec files confirmed. Now starting **F0 — the baseline chain**. First: orphaned-server hygiene + seedcheck.
Seedcheck exact (7/1850/2235/0/3/2). Now running the baseline chain: lint → typecheck → unit tests.
Lint ✓, typecheck ✓, 108/108 unit ✓. Now the production build.
Build ✓ (robots + sitemap prerendered). Now the e2e suite in chunks. Let me check the playwright config first.
The config uses a setup project + storageState. Let me check how the v86 session ran the chunks (from session_206.md) to replicate the exact discipline.
Now running the e2e suite in chunks (the v86 discipline: 3 chunks, each including auth.setup.ts, fresh e2e.db per chunk).
Chunk 1: 102 passed. Running chunk 2.
E2E chunks complete: 102 + 110 + 79 = 291 executions = **289 unique tests** — matches the documented v86 state. Now the 35-step smoke test.
**F0 baseline chain FULLY GREEN** — lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · 289 e2e ✓ · 35/35 smoke ✓. Now **F1 — the axe-core watch**.
F1: npm-latest 4.14.0, only rc prereleases beyond, lockfile holding the v68 dedupe state. Now the engine-contract pin standalone run.
F1 complete: NO DRIFT (engine-contract pin 2 passed standalone). Now **F2 — the 81st standing checks**: version-bump from v80 with the three token families.
Now deriving the 81st standing checks (v80 → v81) with all three token families, then verifying version-bump-only diffs.
Version-bump-only diffs verified ✓, zero old tokens remain (the exit 1 is grep's no-match success). Now running the reference side (read-only).
Reference side: four bugs ALL live, data census unchanged (81st clean drift check), SEO pair live. Now the clone side.
**F2 — the 81st standing checks ALL GREEN** (mobile menu verified the 81st consecutive time; all four reference bugs live; data census clean; SEO pair live). Now **F3 — deriving the v87 probe series** from the v81 series.
Sed derivation clean. Now history-correcting the header comments (the re-run ordinal: fourth re-run, last re-shot v81, tenth consecutive queue/ledger agreement).
All headers corrected. Now executing **F3** — reference side shots first (read-only).
Reference side complete (login first attempt; calculator dialog opened with the expected state). Now the clone side shots.
Clone side complete with full fixture restoration (page total $2235.00, Rent $1850.00 verified). Now the VLM pairwise comparison.
VLM verdicts: **login IDENTICAL** (zero style flags); **calculator DIFFERENT with three flags** — the same three documented v81 classes. Per the v75 convention, the census runs regardless. Executing the both-sides census.
Census complete. All axes byte-identical except the documented classes — but the REF side's `close` button census is missing this run (the clone returned it). Let me check the v81 documented values to determine if this is drift.
The v59 F1 pin holds closeBtn {36,36} at 1280. The ref side's missing `close` key needs arbitration — let me probe the reference's calculator close button directly.
The v81 census documented the close 36×36 on both sides. This run the ref side didn't return it — direct arbitration needed. Writing a one-shot probe to inspect the reference's dialog buttons.
**关键发现**：参考页面的关闭按钮**大小为 36×36，与记录的值一致**——但它现在有**空的 `aria-label` 和空的 `textContent`**（关闭图标是纯 SVG，没有可访问名称）。v87 人口普查的查找器匹配了 `aria-label` 或 `textContent`——两者现在都不存在。让我检查一下在 v81 时参考页面的关闭按钮是否有一个可访问名称。
The v81 census recorded the ref close 36×36 (finder-matched via accessible name). Today the ref's close button has **no aria-label and no text** — the reference removed the accessible name. My probe confirms the visual chrome (36×36/radius 6px) still matches byte-identically. Let me check how the clone pins the close button's accessible name.
The clone's close accessible name is functionally pinned throughout calculator.spec.ts (`getByRole("button", { name: "Close" })`). The ref's lost name is a reference-side a11y regression the clone supersedes — **no production change needed**. Now for F4, let me map the existing pin coverage on the login/calculator surfaces to find never-pinned axes.
Coverage map built. The never-pinned axes: the calculator **close button's chrome beyond {36,36}** (radius 6px / transparent bg / 0px border), the **login card's pad (0px)** and **logo radius (0px)**. Let me examine the source files to design the pin precisely.
The card's padding lives on the inner div (p-8 sm:p-10 md:...). Per the v84/v85/v86 one-shot precedent, the pin's axes need a supplemental both-sides census first. Let me check the wrapper-arbit-v86.sh template.
I have the template. The v87 pin family proposal: the calculator close button's chrome (radius/bg/border-width — v59 holds only {36,36}) + the login card's pad + logo radius. Let me verify no existing pin asserts those axes at any viewport.
No close-button radius/bg/border assertions exist at any viewport — the family is never-pinned. Now writing the supplemental both-sides census for the pin's axes (the v84/v85/v86 one-shot precedent).
**The supplemental census: byte-identical on BOTH sides** — close {36×36, radius 6px, transparent bg, 0px border, flex}, card {pad 0px, innerPad 48px 40px 40px}, logo {96×96, radius 0px}. Now let me check how login-parity.spec.ts handles auth state before designing the pin.
login-parity opts out of storageState. Let me check the +2 precedent (v84) before finalizing the pin structure.
Confirmed: every cycle is +1 e2e. The v87 pin: **the calculator close button's full chrome at 1280** (+1 e2e = 290) — the timely family given the reference's close-name regression, with the login pad family census-recorded for the deferred queue. Now writing the remediation plan (mandated order: plan before execution).
Plan saved. Now validating against the codebase: the mutation target's uniqueness and line number.
One radius assertion exists — but in item-details.spec.ts (the item-details dialog's close, a different component). Let me confirm they're distinct surfaces.
Validation complete — the item-details pin is a distinct component, unaffected by the calculator mutation. Now executing **F4 — appending the v87 pin** to calculator.spec.ts.
**PIN GREEN on first run.** Now the pin-sanity mutation: `rounded-md` → `rounded-md lg:rounded-lg` at calculator-dialog.tsx:138, then the standalone rebuild.
The pin fails under the mutation. Let me verify the failure diff reads as the radius axis alone.
The failure diff is exactly one axis: radius 6px → 8px. Now the full calculator.spec.ts under the mutation — only the v87 pin should be red.
**Cascade-free: 16 green, only the v87 pin red.** Now restoring the source and rebuilding.
**F4 complete — PIN-ONLY** (pin green; mutation verified cascade-free; restored; post-restore 17/17 green). Now **F5 — the full chain re-run**: clean-check gate first.
E2E complete: 103 + 110 + 79 = 292 executions = **290 unique tests** (+1, zero flakes). Now the smoke test.
35/35 smoke ✓. Now the screenshot regeneration. Let me check the capture script's flow first.
The capture script uses the existing seeded db (no re-seed) — same-db shots against the v86-committed set should reproduce byte-for-byte. Running the regeneration.
**16/16 BYTE-IDENTICAL** — the same-db regeneration law holds; no pixel arbitration needed. Final seedcheck, then docs alignment.
Seedcheck exact, tree clean of unintended changes. Now **D1–D7 docs alignment**. Starting with D1 (AGENTS.md v87 paragraph) — let me view the v86 paragraph to append after it.
D1 done. Now D2 — CLAUDE.md state bump (289→290 + the v87 entry).
D2 done. Now D3 — README.md counts + plan-table row.
D3 done. Now D4 — zero-balance_SKILL.md Session 122 audit row + state lines.
D4 done. Now D5 — the PAD's v1.1.44 revision block.
D5 done. Now D6 — the probe README's v87 section.
D6 done. Now D7 — the formal narrative session_210.md + worklog Session 122 entry.
D7 complete. Now the pre-ship verification gate.
Pre-ship gate ALL GREEN. Now the ship — let me consult the SSH wrapper runbook.
The runbook is clear. Deploying the SSH infrastructure: the shim exists at /home/z/my-project/bin/ssh (verified earlier). Writing the operator key and verifying its fingerprint.
Key verified — fingerprint matches the documented v84/v85/v86 record. Creating the parity commit.
Commit `30bdf9f` created, PIN-ONLY verified. Now the dry-run push with the explicit --remote flag.
Dry-run successful (fast-forward 40cee12..30bdf9f). Executing the real push.
**Push successful** — remote verified `main @ 30bdf9f == local HEAD`. Shredding the operator key and verifying the final state.
Remote verified via the wrapper during push (`main @ 30bdf9f == local HEAD`); keys shredded; tree clean. Updating the agent workspace worklog.
**v87 cycle complete and pushed** — `main @ 30bdf9f` on your GitHub repo, remote verified, keys shredded, tree clean.

What happened this session:
- **Baseline + audit clean**: F0 fully green (108 unit · 290→289 e2e baseline · 35 smoke); v86 commit re-verified PIN-ONLY
- **81st standing checks**: mobile menu working (81st consecutive time); reference's four bugs all live
- **The pair's fourth re-run**: login verdict IDENTICAL (3rd consecutive); calculator's three flags all documented classes; census reproduced v81 values exactly — zero drift
- **New finding**: the *reference's* calculator close button lost its accessible name (a11y regression on their side) — the clone keeps `aria-label="Close"` (the superset behavior)
- **+1 pin (290 e2e)**: the close button's full chrome at 1280, mutation-sanity cascade-free; screenshots 16/16 byte-identical

**Next**: run the v88 cycle — the queue points to the v82-era networth + drill-down pair (now the oldest re-shot candidate); verify against the rotation ledger first, per protocol.
