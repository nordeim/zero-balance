# Session 80 — Parity iteration v38 (session-79 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_78.md` /
`docs/remediation-plan-v37.md` / `worklog.md` / `docs/session_79.md`.
Full autonomy granted on the open questions, so I worked the whole
chain directly.

**Step 1 — workspace refresh.** `git pull origin main` fast-forwarded
`c035106..bac2246` (the session-79 transcript commit — the only new
file). The environment was INTACT this session (no re-clone, no
reinstall): `.env` with `DATABASE_URL="file:../db/custom.db"`,
`db/custom.db` at the repo root, node_modules present, the v37 build
current. Working tree clean. scandihaven re-cloned at the workspace
root (depth 1, never compiled).

**Step 2 — docs review.** The five project docs (AGENTS, CLAUDE, README,
PAD, SKILL) re-read; the v37 changeset verified in place (the S1/S2/S3
pins in items.spec; the O1 construct note). The session_78/79
transcripts reviewed — the queue for this session: **the tooling pass
(open since session 72 — the hasFocus() helper + the a11y CI step)**,
the frequency filter's option-list census at /expenses, the savings
view's filter-card instance, or the dashboard quick-action's focus
walk. The worklog's newest entry is Session 71 (v37); this session is
Session 72 / iteration v38.

**Step 3 — baseline audit chain green on the FIRST full run.** lint ✓ ·
typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap
prerendered) · 177/177 e2e ✓ (3.2m) · 35/35 smoke ✓. npm audit: the
same 5 dev-only `braces` advisories (accepted, unchanged, dev-only).
`@axe-core/playwright` 4.13.0 installed as a devDependency (the
tooling pass below).

**Step 4 — the two-site sweep.** Logged into the reference
(`sepnetflix2023@outlook.com`) on the `ref38` agent-browser session.
The standing checks (the 32nd consecutive): data-drift census clean
BEFORE + AFTER all probes (allocation 30.5%, income $5000.00, savings
$1000.00, expenses $525.00 — unchanged; read-only throughout — the
frequency probe Escape-closed then reset its selection to All, the
savings category probe reset to All, the a11y scans inject + read
only); mobile-nav R1–R4 live on BOTH sites (R1: the reference's toast
container still intercepts the burger's center hit, scrollWidth 395 vs
the clone's DIRECT svg hit at 390 fit; R2: the reference's sheet still
traps after nav, the clone's closes [superset #2]; R3: the reference
marks nothing active on `/` and has no `<nav>`, the clone has the
landmark; R4: the reference overflows 395 on `/`+`/dashboard`, the
clone fits 390 on all routes — **the Tailwind v4 pins hold, the mobile
menu works**); the SEO pair live on both (robots allow-all + the
five-URL sitemap; the reference still capitalizes its app-route URLs
`/Income`/`/Savings` — the documented observation, the clone mirrors
its own lowercase routes per the v21 decision).

**Step 5 — the a11y tooling pass (the headline).** The exploratory
deep scan (`scripts/parity-probes/a11y-scan-v38.mjs` — axe-core 4.13,
the wcag2a/2aa/21a/21aa tags, desktop 1280×800, the booted state) ran
on BOTH sites, then the per-node enumeration with computed colors
(`axe-detail-v38.mjs` / `axe-detail-ref-v38.mjs`). **The reference
FAILS two structural rule families the clone PASSES**: `button-name`
(critical — 3 nodes per items view: its unlabeled Select triggers
`button[aria-controls=…]` + its card kebab) and `svg-img-alt`
(serious — its recharts donut sectors `path[name="Need"/"Savings"/
"Want"]`; the clone's donut is inert, `accessibilityLayer={false}`,
the v31 pin). **The clone's only failures are color-contrast — and
every flagged node maps 1:1 to the reference's own failure at a
byte-identical color**: the 3 breakdown section rows (lime
rgb(143,188,63) / blue rgb(59,126,161) / orange rgb(224,122,59)), the
hero status label (rgb(245,169,98)), the 50/30/20 guideline amounts
(the type colors), the stat-card rows (the type colors + one
rgb(107,114,128) sublabel on a tinted card), the item-card amounts
(the type accents — the reference's /income flags 1 node because its
demo income has ONE card, the clone's 2: data-level), the net-worth
inactive Liabilities tab (rgb(115,115,115)) + asset amounts, and the
404 h1 (rgb(203,213,225)). /savings and /login scan CLEAN on both
sites. A probe lesson from the reference's own /income census: its
income view holds a single Salary card ($5000.00, limeGreen) — the
1-vs-2 flagged-node difference is demo data, not chrome.

**Step 6 — the two first-time surfaces.** Surface A — the /expenses
frequency filter (the second Select): the trigger chrome 216×36
("All Frequencies") on both sites (the clone carries the aria-label
superset); the option list is a STATIC 7-option list BYTE-IDENTICAL
on both sites (All Frequencies + One-time + Weekly + Bi-weekly +
Monthly + Quarterly + Annually — the same static list the v34 pin
covered in the sub-dialog instance). Round-trip: the reference
"One-time" → 0 cards + "0 items · $0.00" (its demo expenses are all
recurring — data-level), reset → its 4 cards; the clone "Weekly" →
the Groceries card + "1 items · $320.00", reset → 3 cards + "3 items
· $2235.00". Surface B — the /savings filter-card instance (the
third items-view instance): the white rounded-2xl card (bg
rgb(255,255,255), radius 16px, border rgb(229,231,227), pad 24px,
960×86), the 447×36 search ("Search savings items...", the ambient-
only rest shadow — the O1 invisible-lead note), the two 216×36
comboboxes, the 4-column grid (4 × 215.5px) — byte-identical on both
sites. The category round-trip: the reference's options = All +
"Emergency Fund" (its demo savings has ONE item — data-level), the
clone's = All + Emergency Fund + Investments ("Emergency Fund" → 1
card + "1 items · $800.00", reset → 2 cards + "2 items · $1250.00").
The VLM pairwise (/savings): DIFFERENT with all four flags
data-explained (the card count, the classification tags, the
payment-method footer chips, the avatar letter). **The sweep found
ZERO production-code drift.**

**Step 7 — the remediation plan.** `docs/remediation-plan-v38.md`
written (the sweep evidence, F1/S1/S2/T2 findings, the 12-item ToDo
list) and validated against the codebase BEFORE execution — the
items.spec insertion points (the v37 S3 end / the savings describe),
the mutation targets (the frequency SelectItem, the META
searchPlaceholder, the SelectTrigger aria-label), the seed arithmetic
(Weekly → Groceries $320; Emergency Fund $800 + Investments $450 =
$1250), and the AxeBuilder API validated live by the exploratory
scan.

**Step 8 — TDD execution.** The a11y gate first:
`tests/e2e/a11y.spec.ts` — 8 tests (the 6 authed routes + the 404 +
the logged-out login in its own storageState-opt-out describe; a
`test.use` opt-out is HOISTED per describe — the authed tests must
never see it). Each authed test runs axe under TWO gates: GATE 1
(structural) asserts no violation id other than color-contrast; GATE
2 (provenance) resolves every flagged node via its axe
`node.target` selector chain and asserts its computed color is one
of the reference's 7 measured palette colors. The login test asserts
ZERO violations. All 8 GREEN on the first run (32s). Pin-sanity:
stripping the frequency SelectTrigger's aria-label + rebuild (the
e2e drives the PRODUCTION build — the v37 lesson) → the
`button-name` violation fires → GATE 1 FAILS; restored → GREEN. Then
S1 (the frequency filter's 7-option census + the Weekly round-trip +
the reset; the first run hit a strict-mode lesson —
`getByRole("option", { name: "Weekly" })` collides with "Bi-weekly",
fixed with `exact: true`) and S2 (the savings filter-card chrome +
the category round-trip + the reset) — both GREEN; each mutation
verified to FAIL (removing the Weekly SelectItem → the census FAILS;
changing the savings searchPlaceholder → the placeholder/aria-label
assertions FAIL). The hasFocus() helper shipped as
`scripts/parity-probes/hasfocus-gate.sh` (the v34 discipline
formalized: assert `document.hasFocus()`, re-focus with a REAL
`press Shift`, re-assert, fail loud) + demonstrated live. The
changeset verified: +1 devDependency, +133 spec lines in items.spec,
the new a11y.spec, the v38 probes + the helper, ZERO production-code
changes (the working tree shows no diff in src/).

**Step 9 — the full chain re-run.** lint ✓ · typecheck ✓ · 108/108
unit ✓ · build ✓ · **187/187 e2e ✓ (3.8m — 177 → 187: 8 a11y + S1 +
S2)** · 35/35 smoke ✓. The dev-DB census clean (7 items: the demo
seed's 2 income + 3 expenses + 2 savings). The 16 screenshots
regenerated. The probe README updated with the v38 section (the
scripts + the four lessons: the option-name substring collision, the
AxeBuilder newContext() requirement, the hoisted test.use, the
axe-target selector resolution).

**Step 10 — docs aligned + shipped.** README (the 187 counts + the
v38 table row), CLAUDE.md (the counts + the a11y-gate e2e entry),
AGENTS.md (the v38 paragraph — the two gates + the palette + the
helper), the SKILL doc (the state line + the Session 73 row), this
formal log, the repo worklog (Session 72, newest-first), the
workspace worklog. Commit + push to `main` via the SSH wrapper
runbook (`docs/ssh_git_wrapper_v3.py`, the key materialized to
~/.ssh/, fingerprint verified, the wrapper dry-run then the real
push, the key shredded after).

**What this session delivered:**

- **The a11y tooling pass shipped (open since session 72)** — the
  permanent axe-core gate (8 e2e: GATE 1 structural + GATE 2
  provenance + the login's zero-violation) + the hasFocus() probe
  helper; the superset measured: the clone passes the two structural
  rule families the reference fails (button-name, svg-img-alt) and
  its contrast failures are the reference's own parity-pinned palette
- **Two first-time surfaces measured + pinned — ZERO
  production-code drift**: the /expenses frequency filter (the
  byte-identical static 7-option census + the round-trip) and the
  /savings filter-card instance (the byte-identical card chrome +
  the category round-trip)
- **Standing checks clean (32nd consecutive)** — mobile-nav R1–R4 on
  both sites (**Tailwind v4 pins hold, the mobile menu works**), data
  drift (reference read-only, verified before + after), the SEO pair,
  one VLM pair (all flags data-explained)
- **Two new pins + the 8-test a11y gate** (TDD — every mutation
  verified to FAIL its pin) → **108/187/35 green**

**Suggested next steps**: the dashboard quick-action Add Item's focus
walk (the last unmeasured surface from the session-78 queue); or the
net-worth summary card's gradient chip at the /savings-class
viewports; or the a11y gate's MOBILE extension (a 390×844 scan of
the sheet-open state — the current gate covers desktop only); or
re-issue the brief referencing `docs/session_80.md` /
`docs/remediation-plan-v38.md` and I'll pick from the queue.
