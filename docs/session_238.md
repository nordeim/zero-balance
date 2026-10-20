I'll continue the zero-balance workflow from where we left off. Let me start by refreshing the workspace and reviewing the current state.
The workspace has been reset. Let me clone the repository fresh.
Repository cloned successfully. This is a highly iterative project at v97 iteration. Let me review the core documents and latest session files.
The repo is at v97 iteration with sessions up to 235. Let me review the latest session files and remediation plan.
Both session logs reviewed. The v97 cycle is complete; the v98 cycle targets the v92-era SAVINGS pair. Let me review the remediation plan and worklog tail.
Now let me check the worklog tail and probe README for the v98 queue details.
I now have full context. This is the **v98 parity cycle** (Session 133): the v92-era SAVINGS pair re-run + axe watch + 92nd standing checks + one new e2e pin. Since the workspace was reset, this requires full environment provisioning (fresh-clone class). Let me set up the task plan.
Queue verified against `vlm-shots-v92.sh`'s own header — the SAVINGS pair. Now let me start environment provisioning (the long pole) while reviewing the skills catalog.
npm install is running in the background. Let me examine the v92 series files (the derivation source for v98).
npm install completed. Now let me set up `.env` and the database, then check the skills catalog.
The seedcheck hit the documented polluted parent `DATABASE_URL` issue — the `env -u` discipline is load-bearing. Let me retry.
Seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items / 3 assets / 2 liabilities). Now let me check the skills catalog and playwright setup.
Playwright browsers installed. Now starting the **F0 baseline chain** — lint + typecheck first.
Lint ✓ · typecheck ✓ · 108/108 unit ✓. Now the production build.
Build ✓ (robots + sitemap prerendered). Now the e2e suite in three chunks — let me derive the split.
Let me find the exact v97 chunk split from the session log.
Now I'll run the e2e suite in three chunks (matching the v97 split pattern: 134+95+70 main + 3 setup = 302 executions = 300 unique).
134 failed — let me investigate the failure cause.
Browser version mismatch — the installed playwright expects a different chromium build. Let me check the version pinning.
The project pins playwright 1.63.0 which needs chromium build 1243; the cache has 1200. Installing the correct browser build.
Chunk 1: **135 passed**. Now chunk 2.
E2E fully green: **135 + 96 + 71 = 302 executions = 300 unique, zero flakes**. Now the 35-step smoke test.
**F0 baseline FULLY GREEN** (seedcheck exact · lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ · 300 e2e · 35/35 smoke). Now auditing the commits since the v97 push.
Session-log-only commits confirmed (zero src/ or lockfile deltas). Now the production-seams re-audit.
All seams verified. **F0 complete.** Now **F1 — the axe-core watch**.
**F1: NO DRIFT** (npm-latest 4.14.0, only rc/next sha prereleases beyond; wrapper + engine both 4.14.0; dedupe holds). Now the engine-contract pin standalone.
**F1 complete.** Now **F2 — the 92nd standing checks**. Let me examine the derive pattern.
Scripts derived cleanly. Let me check the reaping discipline before running.
Reference side: **all four bugs live, census exact, SEO pair live**. Now the clone side.
**F2 complete — mobile menu VERIFIED WORKING the 92nd consecutive time; all four reference bugs live; census clean.** Now **F3 — the v98 probe series derivation**. Let me study the exact v92 fragments for history corrections.
Let me check for all old-version tokens in the v92 files that need correction or whitelisting.
Now let me write the v98 series derivation script.
Let me check all version tokens in arbit-v92.sh to build a correct whitelist.
Now writing the v98 series derivation script.
The arbit correction missed — let me check the exact fragment.
Series derived cleanly. Now let me verify the arbit-v98.sh structure for the two-half builder.
Now writing the two-half census builder for v98.
Two-half census built (md5 31d181ed, byte-identical). Now executing the reference-side shots.
Both sides captured (login first attempt both sides). Now the VLM pairwise comparison.
**Verdict: DIFFERENT** — every flag maps to a documented class. Now the two-half census for DOM arbitration. Reference half first.
The script timed out. Let me check its structure and run with output streaming to diagnose.
Reference census captured (the earlier timeout was a buffered-tail artifact — the half completed cleanly). Reaping, then the clone half.
Both halves captured — **the census REPRODUCES the documented v86/v92 values exactly: zero drift on every chrome axis** (all deltas map to documented classes: seed-count 1-vs-2, v57 DATA-CONDITIONAL footer chips, Recurring-wrap +30px, seed-data texts). **NO NEW CLONE GAP.**

Now **F4** — surveying the pin coverage map for a never-pinned family on the savings surfaces.
The v97 listbox panel pin runs on /income. Let me survey what's pinned on savings across viewports and elements — walking the component layers.
Let me survey what element families exist in the item-card and check the hover-action coverage.
The savings cards' action chrome is a Radix **DropdownMenu** (ellipsis trigger → Edit/Delete menu). Let me check if its panel chrome was ever pinned.
Found the candidate family — the dropdown-menu panel's geometry + menuitem resting interior. Let me check the ui component source.
The menu-panel geometry family is never pinned anywhere. Let me verify the mutation target line and check the reference's ellipsis menu exists.
Let me verify no other spec asserts dropdown-menu panel geometry (cascade check).
**The never-pinned family confirmed: the goal-card action-menu panel + menuitem resting interior** — zero specs assert any menu radius or item pad. Both sides render exactly Edit+Delete (data-independent). Now building the supplemental two-half census.
`no trigger` on the reference — per the render-race lesson, let me probe the reference's savings view directly to check what action chrome exists.
The session shows the login page — authentication didn't persist. Let me re-login in this session and verify.
Login succeeded but no "Actions for" trigger exists on the reference. Let me enumerate all buttons on the reference's savings view.
The reference's trigger is a 36×36 no-label svg button with opacity 0 — the clone's aria-label is the superset. Let me update the census finder to a cross-side form.
The trigger was found but the synthetic click didn't open the menu. Radix needs pointer events — let me test with the full pointer sequence.
The full pointer sequence opens the menu (2 items). Updating the census JS accordingly.
**Reference menu census captured** — panel {bg white, radius 6px, border 1px rgb(229,229,229), shadow-md visible layers, minW 128, w 128, h 74}, item0 {14px/400/rgb(10,10,10)/"6px 8px"/4px/32}. Now the clone half.
**The pin's axes measured BYTE-IDENTICAL on both sides** (only delta: the shadow's zero-layer lead count 2-vs-4 — the documented v3/v4 construct class; visible layers byte-identical). Even panel w/h/itemCount match (Edit+Delete is data-independent). Seedcheck exact.

Now verifying the mutation target line before writing the plan.
Mutation target verified (exactly one `rounded-md` at line 20; the item's `rounded-sm` at line 36 untouched). Now let me check the spec tail form.
The spec ends at line 3894. Now writing the remediation plan BEFORE pin execution (the mandatory order).
Plan saved. Now appending the v98 pin to items.spec.ts.
Those errors are from invoking tsc on a single file without the project config. Running the proper typecheck, then the pin's first run.
**Pin GREEN on first run** (1 setup + 1 test). Now the pin-sanity mutation — line-scoped `rounded-md` → `rounded-lg` at dropdown-menu.tsx:20.
43 passed — the mutation didn't bite because the e2e runs the PREBUILT standalone server. I need to rebuild with the mutation in place first.
**Mutation sanity: PERFECT** — only the v98 pin red (42 green), failure diff reads as the radius axis alone ("6px" → "8px"). Now restoring and rebuilding.
**F4 complete — 43/43 green post-restore.** Now **F5 — the full chain re-run**.
**F5 chain GREEN: 301 e2e (136+96+71 = 303 executions), zero flakes · 35/35 smoke.** Now the screenshots regeneration + byte-compare.
6/16 differ — the documented DATE class (fresh re-seed re-anchors isoDate offsets; db/ is gitignored and doesn't travel). Let me arbitrate via the pixel-diff method.
Five views arbitrate to date spans. The calculator + item-details regions need closer inspection — let me check the channel magnitudes and crop the regions.
Both "out-of-class" regions show **max channel 2** — the documented sub-perceptual re-render noise class (the v68 calculator precedent: invisible below the ~2.5 JND threshold). Let me visually confirm one crop.
The pixel measurement (max channel 2 = sub-perceptual, below JND) contradicts the VLM's over-read — but let me examine the region content directly to be certain.
The pixel measurement is decisive (max channel 2, src/ byte-identical, 300 e2e green including calculator chrome pins — a real border change would fail them). The VLM over-read is the documented misperception class. **Screenshots arbitrated: 10/16 byte-identical + 6/16 the DATE/re-render classes — all documented, never a regression.**

Now the D1–D7 docs alignment. Finding the anchors.
All anchors mapped. Let me check the remaining count mentions, then write the alignment script.
Now writing the D1–D3 alignment script.
D1–D3 aligned. Now D4–D6.
D4–D6 aligned. Now D7 — the session narrative and worklog entry.
D7 complete. Now updating the shared workspace worklog and running the pre-ship gates.
All gates green. Staging and committing the v98 cycle.
Commit `08cc3cf` created (35 files, +2831/−3, zero src/ changes). Now the SSH-wrapper push — reviewing the runbook first.
paramiko installed. Now deploying the key and the ssh shim per the runbook.
Deploying the shim and the key per the runbook.
Fingerprint matches the documented `SHA256:3ddaNlFhMz1JXiGEDgVEaRsUzI4Ev0IpGEEB7NnU4PU`. Now the dry-run with the correct remote override.
Dry-run clean (fast-forward `9152c18..08cc3cf`). Executing the real push.
**Push verified** — remote main @ `08cc3cf` == local HEAD (independent HTTPS re-verification), tree clean, keys shredded with zero residue. Following the established pattern, now the session-log follow-up commit (the transcript-style log).
The **v98 parity cycle (Session 133)** is complete and pushed to `main @ 7939458` — remote verified via independent HTTPS re-check, tree clean, keys shredded.

## Cycle summary

| Phase | Result |
|---|---|
| **F0 baseline** (fresh-clone provisioning) | npm install · prisma + seed (seedcheck exact) · chromium-1243 · lint/typecheck/108 unit/build ✓ · **300 e2e** zero flakes · 35/35 smoke |
| **F1 axe watch** | NO DRIFT (4.14.0 both sides; engine-contract pin 2 passed) |
| **F2 92nd standing checks** | **Mobile menu working the 92nd consecutive time** (Tailwind v4 mitigation holds); all four reference bugs live; census clean on first read |
| **F3 savings-pair 6th re-run** | Verdict DIFFERENT, every flag DOM-arbitrated (v57 DATA-CONDITIONAL footer, seed classes, avatar); census reproduces v86/v92 exactly — **NO NEW CLONE GAP** |
| **F4 pin (+1 e2e = 301)** | Goal-card **action-menu panel + menuitem-resting interior** — never pinned at any viewport; green first run; mutation hit the radius axis alone after rebuild; restored 43/43 |
| **F5 + ship** | 301 e2e · 35 smoke · screenshots 10/16 byte-identical + 6/16 pixel-arbitrated DATE class · **PIN-ONLY (zero src/ changes)** |

**Key deliverables:** `docs/remediation-plan-v98.md` (validated plan), `docs/session_236.md`/`session_237.md` (narratives), the v98 probe series + census scripts, the regenerated `docs/screenshots/`, docs aligned D1–D7 across AGENTS/CLAUDE/README/SKILL/PAD/probe-README/worklog, `.env.example` verified tracked.

**New lessons documented:** the reference pointer-event family (full sequence required to open reference chrome), the unlabelled-trigger geometric finder, the data-independent Edit+Delete panel, and the mutation-rebuild discipline.

**Next:** per the rotation ledger, v99 targets the v93-era **LOGIN + CALCULATOR pair** — say "continue v99" to proceed, or request adjustments to this cycle's deliverables.
