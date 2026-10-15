I'll continue the task from where we left off. The workspace was reset (a
fresh sandbox) — the repo needed a re-clone, then the full environment
rebuild before the v64 iteration could run.

Cloned https://github.com/nordeim/zero-balance.git at 1ba981c (main) —
the session-154 transcript on top of 55e5a5b, the v63 ship. The latest
session docs confirmed: session_153 documents v63 (shipped), and the
documented v64 queue is (1) the re-run cadence on the OLDEST desktop
pairs, (2) the axe-core 5.x wrapper watch, (3) the deferred
reference-write censuses (out of bounds).

Reviewed the five core docs (AGENTS/CLAUDE/README/PAD/SKILL) with the
wrapped-read discipline, then the session records
(remediation-plan-v63 + the worklog's Session 97 entry). The picture:
v63 completed the pair matrix; the pin-only line holds since v61.

Environment rebuild: npm install (+ the prisma engines rebuild + the
npm rebuild for the postinstall-blocked packages), .env restored
(DATABASE_URL="file:../db/custom.db"), db:push + db:seed (7 items / 3
assets / 2 liabilities). First e2e chunk run failed with "Executable
doesn't exist" — the fresh-sandbox caveat (the v62 lesson): npx
playwright install chromium, then the chunks ran green.

**Baseline chain GREEN: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓
(robots + sitemap prerendered) · 265 e2e ✓ (91 + 94 + 82 chunks = 264
chromium + 1 setup) · 35/35 smoke ✓** — the codebase matches the
documented v63 state exactly (the v63 pin verified at
networth.spec.ts:868).

Now the 58th standing checks — version-bumped the v57 scripts to v58:

Reference side: the four bugs ALL still live (the toast-blocker, the
overlay trap, no-landmark, the 464px /networth overflow); the data
census unchanged (the 58th clean drift check); the SEO pair live.
Clone side: R1-R4 all green. **The mobile navigation menu VERIFIED
WORKING — the 58th consecutive time.**

F1 — the axe-core 5.x wrapper watch: npm-latest @axe-core/playwright
is STILL 4.13.0 (no 5.x exists); the wrapper's nested engine
axe-core@4.13.0 is byte-identical to the v38/v62/v63 audits; the
top-level 4.14.0 still belongs to eslint-plugin-jsx-a11y. **NO DRIFT.**

F2 — the fresh items pair (the OLDEST desktop pair re-run): wrote the
v64 probe family (vlm-shots-v64.sh + clone-vlmshots-v64.sh +
vlm-compare-v64.mjs, FULL-PAGE both views at 1280×800, the
parked-pointer discipline). The VLM flagged: PAIR 1 the avatar + the
missing Base44 FAB + the seed data; PAIR 2 the footer content, the
badge arrangement, the grid population, the avatar/FAB/seed classes.

Every flag needed DOM arbitration (the v43 rule). Wrote arbit-v64.sh
(following the v63 pattern — the unquoted heredoc with the expanded
census, JS in single quotes, no `$` in the census):

The census proved: the footer chrome BYTE-IDENTICAL (the reference's
expense footers render the date alone — its items carry no
paymentMethod; the clone's render the same two-child structure the
reference's OWN income card renders, "Oct 7, 2026" + "Bank Account");
the badge chrome BYTE-IDENTICAL (the clone's Recurring superset badge
wraps h 52 = 22+8+22); the grid axes BYTE-IDENTICAL (the same
fractional 309.344px last track both sides; the counts are seed data);
the card heights (200 vs 230) = the badge-wrap arithmetic. **The pair
is CLEAN.** Noted: the VLM CONTRADICTED ITSELF on the Base44 FAB
between the two pairs ("missing from the clone" in pair 1, "present in
the clone" in pair 2) — platform chrome is excluded by rule.

The census also measured a never-census'd family: the INCOME view's
filter card at 1280 (the v38 S2 pin covered /savings; v37/v38 the
/expenses triggers; the v52 F2 pin this card's MOBILE state; the
early-era income test pins CLASS STRINGS only). That's the v64 pin
candidate.

Wrote docs/remediation-plan-v64.md (the 64th plan, the 13-row ToDo).
Then the TDD execution — the F3 pin in tests/e2e/items.spec.ts, inside
the income describe right after the early-era class-string test:

GREEN first run (PIN-ONLY). The mutation-sanity checks — S1: the card
p-6→p-4 (pad 24→16 + h 86→70) BITES; S2: the search wrapper
md:col-span-2 removed (w 447→215.5) BITES; S3: the grid gap-4→gap-2
(gap 16→8 + tracks recompute) BITES — each with the standalone REBUILD
as a SEPARATE command. Restored; git status src/ clean; the full items
spec 29 passed (+1).

The screenshots: all 16 BYTE-IDENTICAL (the fresh sandbox's re-seed
anchored to the same day as the v63 capture — even the SEED-DATE class
is absent).

Docs alignment D1-D8: the AGENTS v64 paragraph (+2 lines,
additive-only); CLAUDE 265→266 + the filter-card pin reference; the
README state lines + the v64 table row; the SKILL Session 99 row + the
three count lines; the PAD v1.1.21 revision block; the probe README's
v64 section; session_155.md + the repo worklog Session 98 entry; the
workspace worklog. Verified every edited doc's line count (the v63
truncation lesson).

**Full chain re-run GREEN: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓
· 266 e2e ✓ (91 + 95 + 82 chunks) · 35/35 smoke ✓** — the
authoritative count 266 tests.

The ship: credential scan clean (the only matches the pre-existing
historical docs); the changeset staged (16 files); the commit created
(4f388f0, +1139/−8). The SSH push: paramiko installed
(--break-system-packages), the Appendix-A shim deployed to the
workspace bin/ (outside the repo), the operator key materialized and
its fingerprint verified (SHA256:3ddaNlFhMz1JXiGEDgVEaRsUzI4Ev0IpGEEB7NnU4PU
— the documented one). Dry-run clean (1ba981c..4f388f0 fast-forward);
the real push verified: **remote main @ 4f388f0 == local HEAD**. The
operator key shredded.

## Session summary (parity iteration v64 — pin-only)

- **Refresh & validate**: fresh sandbox — re-cloned at 1ba981c; the
  environment rebuilt from scratch (npm install + engines, .env, db
  push + seed, the Playwright browsers — the fresh-sandbox caveat);
  baseline chain GREEN (108 unit / 265 e2e / 35 smoke) — the codebase
  matched the documented v63 state exactly
- **58th standing checks**: mobile navigation menu **verified working**
  (58th consecutive round); the reference's four mobile bugs all still
  live; data census unchanged; SEO pairs live on both sites
- **F1 — the axe-core 5.x wrapper watch**: **NO DRIFT** —
  @axe-core/playwright@4.13.0 is still npm-latest (no 5.x exists) and
  its nested engine is byte-identical to the v38/v62/v63 audits
- **F2 — the OLDEST desktop pair's fresh sweep**: the v57-era items
  pair re-run (income + expenses, FULL-PAGE 1280×800) — **the pair is
  CLEAN**: every flag DOM-arbitrated to documented classes (the v57
  DATA-CONDITIONAL footer + the badge-wrap contracts re-measured
  byte-identical five iterations later; the seed-count grid; the
  avatar; the Base44 FAB — with the VLM self-contradiction lesson)
- **TDD pin added**: the income view's filter-card computed census at
  1280 (+1 e2e = **266** — the never-census'd sibling of the v38 S2
  savings pin), three mutations verified to FAIL; all 16 screenshots
  byte-identical; docs aligned D1–D8
- **Shipped**: commit `4f388f0` (16 files, +1139/−8) pushed to `main`
  via the SSH wrapper — fingerprint matched, remote verified, keys
  shredded

**Suggested next steps** (the documented v65 queue): the v58-era
savings pair's fresh sweep (the queue's other OLDEST candidate), the
axe-core 5.x wrapper watch (unchanged), or the deferred
reference-write censuses — just say the word.
