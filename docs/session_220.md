I'll continue the task from where it left off. Let me start by checking the current workspace state and refreshing it.
The workspace has been reset — cloning the repository fresh at main @ 07586b7.
The git log shows v90 shipped (session_218 + session_219 logged). Per session_219's closing line, the next cycle is v91: **the v85-era ITEMS pair (income + expenses at desktop 1280), its FIFTH re-run** — verify against the rotation ledger first, per protocol.
Let me review the core docs: AGENTS.md (commands + the parity rules + the v90 paragraph), CLAUDE.md (the state lines), the worklog's Session 125 entry, and remediation-plan-v90.md.
The v90 plan's structure is clear: F0 baseline → F1 axe watch → F2 standing checks → F3 the re-run pair (shots + VLM + census) → F4 the pin + mutation → F5 the full chain → D1-D7 docs → ship.
Per the queue-prose verification lesson, let me verify the v91 target against the v85 probe scripts themselves (the ledger authority is the probe lineage).
Confirmed: **vlm-shots-v85.sh shoots the INCOME + EXPENSES views at desktop 1280x800, full-page** — the ITEMS pair, matching the queue's phrasing (no transcription error this cycle). The bracket [v57 → v64 → v70 → v79 → v85] makes v91 the FIFTH re-run.
Now provisioning the environment following the v86/v88/v90 fresh-clone reprovisioning checklist: npm ci first.
354 packages installed; the 5 high audit findings are the known dev-only braces chain. Now .env + the database.
Seeded: 7 budget items, 3 assets, 2 liabilities. Now the seedcheck — need a small script since sqlite3 isn't available.
**Seedcheck exact: 7 items / rent 1850 / 0 line items / 3 assets / 2 liabilities.** Chromium next — the cache has 1200, installing 1243.
chromium-1243 installed. Paramiko next (the venv python3), then the shim deployment.
Paramiko 5.1.0 available in /home/z/.venv. Deploying the shim to /home/z/my-project/bin/ssh (outside the repo, per the runbook).
Shim deployed. Now the audit phase — verifying the v90 commit's PIN-ONLY claim.
**v90 commit verified PIN-ONLY** (17 files, +1429/-13, zero src/ changes; the one commit since session-log-only). The production seams audit: db-path, SEO pair, Tailwind v4 mitigations, skills/ exclusion, auth, the three test tiers — all clean.
Now **F0 — the baseline chain**: lint → typecheck → 108 unit → build (robots + sitemap prerendered).
23 spec files, 293 tests total (292 chromium + 1 setup). Running the three chunks: 127 + 106 + 62 = 295 executions.
**F0 baseline FULLY GREEN** — the exact documented v90 state, zero flakes on the first run. Smoke: 35/35.
**F1 axe-core watch: NO DRIFT** (4.14.0 npm-latest, only rc prereleases beyond; the lockfile holding the v68 dedupe; the engine-contract pin green standalone).
**F2 — the 85th standing checks**: deriving ref-standing-v85.sh + standing-checks-v85.sh from the v84 pair across the three token families, version-bump-only verified by normalizing back.
Reference side: **all four bugs live, data census unchanged (the 85th clean drift check), SEO pair live.** Clone side: R1–R4 all green — **the mobile menu VERIFIED WORKING (the 85th consecutive time)**, zero overflow at 390, SEO live.
Now **F3 — the v91 re-run pair**. Deriving the probe series from the v85 lineage with the sed substitutions (vlm85→vlm91, refarbv85→refarbit91, clonearbv85→clonearbit91, v85→v91), then the header history-corrections to the FIFTH re-run.
The normalize-back diff confirms: the functional bodies version-bump-only; only the intentional history-correction headers differ. The leftover "85" tokens are all legitimate (the history bracket + the reference URL's app id).
Reference shots taken (login on the first attempt). Clone shots taken. Now the VLM pairwise.
**Both verdicts DIFFERENT** — the flags match the v85 re-run's own documented classes: the avatar (user-identity), the card grids and figures (seed-data), the payment-method chips (the v57 DATA-CONDITIONAL), the badge wrap (the v57 Recurring superset), and the FAB attributed to the CLONE this time — the v85-documented image-attribution swap recurring.
Running the combined census (arbit-v91.sh) — it TIMED OUT mid-run. 70 zombie chromium processes reaped. This is the v89-documented resource-exhaustion class: **the two-half controlled form is the recovery.**
Splitting the census into ref-arbit-v91.sh + clone-arbit-v91.sh with the census JS byte-identical across the halves (the lines-1-215 identity verified).
The reference half ran clean (login on the first attempt). The clone half ran clean.
**The census REPRODUCES the v85 values EXACTLY — zero drift on every axis.** For the FAB flag: the one-shot DOM arbitration (base44-fab-arbit-v91.sh, the v85 finder) reads fabCount 0 + bodyHasBase44 false on BOTH sides — the FAB lives in the reference's platform iframe chrome. **NO NEW GAP — PIN-ONLY.**
Now **F4 — mapping the existing pin coverage at 1280 on the items views** to find the never-pinned axes.
The card/grid/titleRow/amount/footer/badge families are all pinned (v45/v57/v64/v70/v74/v79/v80/v85/v86). The never-pinned families: **the filter-card INTERACTIVE INTERIORS** — the combobox triggers' RESTING chrome (pad/justify/align/bg/radius/border/fw/color + the chevron svg) and the search input's TYPOGRAPHY (fs/fw/lh/color). The v37 S1/S2 pins hold the FOCUS state; the v64/v70 pins the geometry.
Per the v87–v90 precedent, first the supplemental both-sides census of the pin's own axes — built TWO-HALF from the start this time (the cycle already showed the exhaustion once).
The supplemental census (filter-interior-arbit-v91.sh + filter-interior-clone-v91.sh, the census JS verified byte-identical by the md5 line-block diff): **the pin's own axes measured BYTE-IDENTICAL on both sides — ZERO deltas, including the placeholder texts.**
Now the mutation design: the search's view-local pl-10 → pl-10 lg:font-medium (items-view.tsx:188, by LINE NUMBER — AT-lg because the pin runs at 1280; fw chosen for its geometric inertness). The coverage-map grep with BOTH the fw: long form AND the Fw-suffix shorthand family (the v90 lesson): **no spec asserts any input's fw at any viewport.**
Per the mandated order — **plan before execution** — writing remediation-plan-v91.md with the full validated design.
Plan saved. Now executing **F4 — appending the v91 pin** to items.spec.ts.
**Pin GREEN on first run**, typecheck clean. Now the pin-sanity mutation.
The first mutation run failed at the WRONG place — "element(s) not found" at the settle wait. Root cause: I ran a bare `next build` instead of the FULL `npm run build` — the standalone dir lacked its static assets. Completing the copy steps and re-running.
**Mutation verified** — the failure diff reads as the search's fw axis ALONE ("400" → "500"), everything else green in the same assertion object.
**Cascade-free verified**: the full items.spec.ts under the mutation reads ONLY the v91 pin red (39 green).
Restoring the source, rebuilding via the full npm run build, re-running: **40/40 green post-restore.**
Now **F5 — the full chain re-run**: lint → typecheck → 108 unit → build → 294 e2e in chunks (128+106+62 = 296 executions) → 35/35 smoke.
**F5 chain GREEN, zero flakes.** The screenshots regenerated — **16/16 BYTE-IDENTICAL** (the same-day-seed law; no pixel arbitration needed). The final seedcheck exact.
F5 complete — PIN-ONLY maintained (git diff src/ = 0 lines). Now **D1–D7 docs alignment**.
D1: the AGENTS.md v91 paragraph. D2: the CLAUDE.md state bump (293→294 + the v91 clause). D3: the README counts + the v91 plan-table row. D4: the SKILL doc's Session 126 row + the state lines. D5: the PAD's v1.1.48 revision block. D6: the probe README's v91 section (the FAB re-arbitration + the two-half census + the full-build rebuild lessons + the v92 queue — verified against vlm-shots-v86.sh: the SAVINGS pair at desktop 1280, [v58 → v65 → v74 → v80 → v86 → v92]).
D7: session_220.md + the worklog Session 126 entry.
All docs aligned. Now the pre-ship gate: verify .env.example tracked + accurate, PIN-ONLY, no orphans, then commit.

**The v91 cycle is complete and pushed.** Summary of this session:

**Audit → align → remediate → push** on the fresh-cloned workspace:
- **Baseline all green** on first run: 108 unit · 293→**294 e2e** · 35/35 smoke; environment fully re-provisioned
- **85th standing checks green** — mobile menu working (85th consecutive), reference's four bugs still live, zero census drift
- **No new clone gap** — the two-half census reproduced the v85 values exactly; the recurring FAB flag re-arbitrated by the one-shot DOM census (fabCount 0 both sides)
- **New pin added**: the filter-card interactive interiors at 1280 (the search typography + every trigger's resting chrome), with a clean single-axis mutation (lg:font-medium at the view-local pl-10)
- **Operational lessons recorded**: the FAB re-arbitration, the two-half census retrofitted to the supplemental probes, the full-build rebuild discipline
- **Committed and pushed** to main via the SSH wrapper; keys shredded; docs aligned (plan v91, session_220, worklog Session 126)

**Next**: the v92 cycle per the rotation ledger — the v86-era savings pair (the savings view at desktop 1280), its 5th re-run [v58 → v65 → v74 → v80 → v86 → v92]. Want me to proceed, or adjust anything from this delivery?
