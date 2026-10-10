I'll continue the task. Let me start by refreshing the workspace and checking the current state.
The workspace has been reset (only an initial commit, no remote). I'll re-clone the repository as instructed.
The workspace is refreshed — all latest docs are in place (session_75.md, session_76.md, remediation-plan-v36.md, worklog.md). The repo is at parity iteration v36 with 174 e2e tests. Let me set up my task plan and review the docs.
Sessions 75/76 reviewed — v36 shipped with 108/174/35 green, zero production drift. The suggested next surfaces for this session (v37): filter triggers' focus-visible family, search input's typing contract, expenses payment-method filter, and the tooling pass (a11y CI step). Let me review the remediation plan and worklog tail.
Now let me check the worklog tail and the key project docs structure.
Worklog confirms Session 70 (v36) is the latest. This session will be **Session 71 / parity iteration v37**. Now let me review the core project docs.
CLAUDE.md reviewed — clean-check gate, six-phase workflow, and the v4 pins documented. Now let me scan the structure of the remaining large docs.
Docs reviewed. Now let me validate the codebase and environment state, and check the skills catalog.
Environment needs setup: no `.env`, no `db/`, no `node_modules`. Let me check the skills catalog and start the install.
Install complete. Now let me set up `.env`, the database, and look at the key skills.
Database seeded. Let me verify the db file location and read the key skills.
Skills reviewed. Now let me check the agent-browser and tdd skills plus the established probe infrastructure.
Infrastructure understood. Now let me update my todos and run the baseline audit chain (lint → typecheck → unit → build).
Lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered). Now the e2e suite (174 tests):
**Full baseline chain GREEN on first run**: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ · 174/174 e2e ✓ · 35/35 smoke ✓. Now the audit steps:
Audit clean (same 5 dev-only braces advisories — accepted, unchanged). Now the two-site sweep. Let me check the v36 probe pattern for login + reference site access:
Now let me start the two-site sweep. First, login to the reference site:
Logged into the reference site. Now the standing checks — first the data drift census (31st):
Census clean (31st) — allocation 30.5%, income $5000.00, savings $1000.00, expenses $525.00. Now mobile-nav R1–R4 on the reference (the task's particular focus):
R1 (toast-blocker) and R2 (sheet-trap) reference bugs still live. Now R3 and R4:
R1–R4 reference bugs all still live (31st check). Now the SEO pair on the reference:
SEO pair on the reference matches pinned values. Interesting — the reference sitemap has capitalized paths (`/Income`, `/Savings`). Let me check the clone's sitemap and head census:
The clone's sitemap intentionally uses lowercase routes (documented v21 decision — the reference's capitalized URLs don't match its real routes). Now the reference head census:
Reference head census matches pinned values. Standing checks complete (31st). Now the v37 surfaces — first, the filter Select triggers' focus-visible family on the reference `/income`:
Reference trigger rest state measured. Now the focus-visible family — walking with REAL Tab presses:
Reference trigger focus-visible: the shadcn 1px #0a0a0a ring family (white 0px + black 1px + ambient shadow). Now the search input's focus contract — Shift+Tab back onto it:
Search input focus family measured — same 1px #0a0a0a ring. Now the typing/filtering contract on the reference:
Let me verify the "sal" filter match with a clean retry:
Suspicious results — let me verify with the real-key path (reload, Tab onto input, type char-by-char):
Typed the exact name "Salary" → no cards. Let me check the reference's card DOM structure (maybe the title isn't an h3):
The reference's card titles are **H4**, not h3 — my selector was wrong. Let me redo the search filtering test with the correct selector:
Search contract now clear: match → card shown (h4), no-match → empty state (h3), cleared → card restored. Let me check the header count with a match, then restore:
Reference search contract measured and restored. Now let me check the clone's search implementation code:
Now let me check the clone's /expenses view (the payment-method filter — the third Select) and the reference's equivalent:
Now let me measure the reference's /expenses view — the payment-method filter (third Select):
Reference has 3 comboboxes on /expenses. Let me open the payment-method filter and measure its options:
The reference's payment-method list has only the "All" option (its expense items carry no payment methods). Let me check the clone's seed data for payment methods:
The clone's seed carries payment methods while the reference shows none in the filter. Let me check if the reference's cards show payment-method data at all:
The reference shows no payment-method data anywhere (its demo items carry none — data-level). Now the clone-side sweep. Let me write the v37 clone probe script:
Clone sweep mostly byte-identical, but Surface A shows a lead-layer construct difference in the trigger shadows. Let me examine the clone's trigger code:
Surfaces B and C match the reference contract. Let me verify the clone's seed expenses (3 cards shown but census says 4 expenses — data-level check):
All data consistent (clone seed: 3 expenses = $2235 ✓). Now let me re-verify the reference census after all probes (read-only discipline):
Read-only discipline held. Now a VLM pairwise on the new Surface C (expenses with filter open) to complete the sweep:
VLM flags all trace to demo-data differences. Flag 3 raises a structural question — does the clone's card render a payment chip the reference lacks structurally? Let me check the code:
The chip is conditional (`item.paymentMethod ?`) — structurally correct. Let me verify the reference's edit dialog carries a payment-method field (open + Escape, read-only):
The reference's expense cards show an inline "Edit Category" button (not a kebab?). Let me get the full action row:
The reference's expense cards use inline Edit+Calculate buttons (matching the clone's v8 pins). Now let me open the reference's expense edit dialog to check the payment-method field (read-only, Escape after):
Reference's edit dialog HAS the payment-method field — its model supports it; the clone's conditional chip matches. Sweep complete, zero drift. Now let me examine the test files to plan the v37 pins:
Now let me look at the v36 S2/S3 test patterns for the REAL-key idiom:
I have full context. Now let me write the remediation plan v37:
Plan validated. Now TDD execution — writing the three v37 pin tests. Let me check the exact insertion point:
Now inserting the S1 and S2 tests after the v36 S3 test:
S1/S2 inserted. Now the S3 test in the expenses describe:
All three tests inserted. Now running them (pins — expecting GREEN):
All three pins GREEN. Now the pin-sanity mutations — S1 first (strip the SelectTrigger's ring):
The e2e runs against the production build — I need to rebuild for the mutation to take effect:
Build typecheck failed — let me find the source of this error:
The build typechecks test files too. Let me fix the type errors in my new tests:
**S1 mutation bites.** Now restore and verify GREEN:
S1 complete. Now S2 pin-sanity — strip the Input's ring classes:
**S2 mutation bites.** Restore and verify:
S2 complete. Now S3 pin-sanity — break the paymentMethods derivation:
Mutation placed wrong. Let me fix it:
**S3 mutation bites.** Restore the derivation:
All three pins complete (each mutation verified to bite). Let me verify the changeset and run the full chain:
Changeset clean: +149 test lines, zero production changes. Now the full chain re-run:
**Full chain green: 108/177/35.** Now the dev DB census and screenshot regeneration:
Census clean (demo + smoke throwaways, 7 items). Now regenerate the screenshots:
All 16 screenshots regenerated. Now docs alignment — starting with the probe README:
Now README.md — the counts and v37 table row:
Now add the v37 row to the README's engineering-references table:
README done. Now CLAUDE.md — counts and the v37 surface entries:
Now AGENTS.md — find the v36 paragraph location:
Now the SKILL doc — state line and session row:
Now the formal session log. Let me check the session doc naming pattern:
Now the repo worklog — Session 71 entry (newest-first):
Repo worklog updated. Now the workspace worklog:
All docs aligned. Now the final verification gate — the complete changeset review:
Changeset clean (+266 lines, zero production changes). Let me verify gitignore coverage before staging:
Gitignore correct. Now the SSH wrapper — let me review the runbook:
Runbook understood. Let me check the ssh/python environment and stage the shim if needed:
No ssh binary, no paramiko. Let me install paramiko and stage the shim:
Paramiko 5.0.0 installed on python3.13. Now stage the ssh shim outside the repo:
Now materialize the operator key and verify its fingerprint:
Key verified. Now the commit:
Commit `aee5a37` landed. Now the wrapper dry-run with the correct zero-balance remote:
Dry-run clean (`118a45b..aee5a37`). Now the real push:
**Pushed and verified** — `main @ aee5a37`. Now shred the operator key:
Following the repo's established pattern, let me add the raw transcript as the follow-up session-log commit:
All work shipped. Let me close the browser sessions and finalize:
**Parity iteration v37 shipped to `main`** (commits `aee5a37` + `c035106`, remote-verified, keys shredded).

## What this session delivered

- **Workspace re-cloned + rebuilt** (it had been reset) — `.env` with `DATABASE_URL="file:../db/custom.db"`, `db/` at the repo root, seeded; baseline chain green on the first full run (108/174/35)
- **Standing checks clean (31st consecutive)** — mobile-nav R1–R4 on both sites (**Tailwind v4 pins hold, the mobile menu works**; all four reference bugs still live), data drift (reference read-only, verified before + after), SEO pair, one VLM pair (all flags data-explained)
- **The session-76 suggested surfaces, all first-time measurements — zero production-code drift**: filter Select triggers' focus-visible family (visible layers byte-identical; the v3/v4 lead-layer construct difference documented as O1), the search input's focus + typing contract, and the /expenses payment-method filter (the third Select's dynamic derivation + round-trip)
- **Three new TDD pins** (S1/S2/S3, each mutation verified to fail) → **108/177/35 green**; docs + worklogs + session_77/78 aligned; screenshots regenerated

**Next steps**: re-issue the brief referencing `docs/session_77.md` / `docs/remediation-plan-v37.md` — the queue holds the a11y CI tooling pass (open since session 72), the frequency filter's option census at /expenses, or the savings view's filter-card instance.
