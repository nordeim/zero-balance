# Session 77 — Parity iteration v37 (session-76 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_75.md` /
`docs/remediation-plan-v36.md` / `worklog.md` / `docs/session_76.md`.
Full autonomy granted on the open questions, so I worked the whole
chain directly.

**Step 1 — workspace refresh.** The local workspace had been RESET (a
fresh clone with only an "Initial commit" and no remote), so
`git clone https://github.com/nordeim/zero-balance.git` re-materialized
it at `118a45b` (the session-75 transcript commit). Environment
rebuild: `npm install`, `cp .env.example .env`
(`DATABASE_URL="file:../db/custom.db"`), `npm run db:push` +
`npm run db:seed` (7 budget items, 3 assets, 2 liabilities,
demo@zerobalance.app). The `db/` folder lives at the repo root as
required; scandihaven cloned at the workspace root, never compiled.

**Step 2 — docs review.** The five project docs (AGENTS, CLAUDE, README,
PAD, SKILL) re-read; the v36 changeset verified in place (the S1/S2/S3
pins in tokens.spec/items.spec; zero production drift). The worklog's
newest entry is Session 70 (v36); this session is Session 71 /
iteration v37.

**Step 3 — baseline audit chain green on the FIRST full run.** lint ✓ ·
typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap
prerendered) · 174/174 e2e ✓ (3.1m) · 35/35 smoke ✓. npm audit: the
same 5 dev-only `braces`/eslint-config-next advisories (accepted,
unchanged, dev-only); the secret-pattern scan clean; `.env.example`
verified current.

**Step 4 — the two-site sweep.** Logged into the reference
(`sepnetflix2023@outlook.com`) on the `ref37` agent-browser session.
The standing checks (the 31st consecutive): data-drift census clean
BEFORE + AFTER all probes (allocation 30.5%, income $5000.00, savings
$1000.00, expenses $525.00 — unchanged; read-only throughout);
mobile-nav R1–R4 live on BOTH sites (R1: the reference's toast
container still intercepts the burger's center hit, scrollWidth 395 vs
the clone's DIRECT svg hit at 390 fit; R2: the reference's sheet still
traps after nav, the clone's closes [superset #2]; R3: the reference
marks nothing active on `/` and has no `<nav>`, the clone has the
landmark; R4: the reference overflows 395 on `/`+`/dashboard` and 464
on `/networth`, the clone fits 390 on all routes — **the Tailwind v4
pins hold, the mobile menu works**); the SEO pair (robots.txt
allow-all + the sitemap line, sitemap.xml five URLs priority 1.0/0.8
weekly, the head census: title ZeroBudget + the description/canonical/
OG/Twitter/apple/manifest pair — all matching the pinned values; the
reference's sitemap capitalizes its app-route URLs `/Income`/
`/Savings` — measured live this session, documented as an observation
while the clone mirrors its own lowercase routes, the v21 decision).

The three session-76 suggested surfaces, all first-time measurements,
**ZERO production-code drift**:

- **Surface A — the filter Select TRIGGERS' focus-visible family**
  (the v36 Tab-walk census walked PAST the stops without asserting
  their chrome): a REAL Tab walk (blur → 8 Tabs) onto the reference's
  closed category-filter trigger engages `:focus-visible` and renders
  the 1px #0a0a0a ring (`rgb(10,10,10) 0px 0px 0px 1px`) layered over
  the ambient `rgba(0,0,0,0.05) 0px 1px 2px 0px`; the border stays
  `rgb(229,229,229)` 1px; the geometry unchanged (216×36). The clone:
  the VISIBLE layers byte-identical. **O1 (construct observation, not
  drift)**: the full computed strings differ in their INVISIBLE lead
  layers — the reference's v3 three-slot construct (a white
  ring-offset lead) vs the clone's v4 five-slot construct (four
  transparent leads); every lead is a 0px-spread shadow, invisible by
  construction (the v11 shadow-scale precedent).
- **Surface B — the search input's focus + typing contract**: the
  REAL-Tab focus family (Shift+Tab back onto the input — the same
  ring + ambient, border untinted, 447×36, transparent bg); the
  typing contract measured with REAL keyboard chars on the reference:
  typing the exact card name "Salary" → the card list narrows to the
  Salary card + the header recomputes ("Income 1 items · $5000.00");
  a no-match string → the EMPTY state (its heading is the reference's
  h3 "No income items yet" + "Start by adding your first income
  source", the header "0 items · $0.00"); clearing → the card
  restored. The clone: byte-identical behavior over its own seed
  ("1 items · $5200.00"; the empty state; both cards restored).
  Probe lessons: the reference's card titles are h4 (an h3-only card
  census fabricated "no cards" readings — L1); `agent-browser
  keyboard press Backspace` does NOT register in the reference's
  focused search input and the CLI's `fill ""` dispatches no input
  event — clear React-controlled inputs via the native value setter +
  a bubbled input Event (L2); Playwright's own `fill("")` is
  unaffected.
- **Surface C — the /expenses payment-method filter** (the third
  Select, never measured live): the reference's filter card carries
  three 216×36 comboboxes ("All Categories" / "All Frequencies" /
  "All Payment Methods"); its PM listbox open shows exactly ONE
  option (the All option — its demo expense items carry NO
  paymentMethod values, verified: no Bank/Card/PayPal/Cash/Transfer/
  Brokerage text anywhere in its /expenses DOM). The clone's open:
  All + "Bank Transfer" + "Credit Card" — the dynamic derivation
  over its own seed. Data-level, not drift. The reference's EDIT
  DIALOG (opened read-only + Escape-closed) carries the "payment
  method" field — its model supports the values; the clone's
  conditional `item.paymentMethod ? chip` matches the model. The
  clone's round-trip verified end-to-end: select "Credit Card" → the
  trigger text updates, the cards narrow to Entertainment +
  Groceries, the header recomputes ("2 items · $385.00"); reset to
  All → the three cards restored. Also re-verified on the reference:
  the expense cards' action family is the INLINE hover-revealed
  "Edit Category" (77×32) + "Open Calculator" (110×32) buttons (the
  v8-pinned family; the kebab lives on the income/savings cards).
- **The VLM pairwise** (one fresh pair, viewport-asserted 1280×800):
  /expenses with the PM filter open — VERDICT DIFFERENT with ALL five
  flags data-explained (4 cards vs 3; the extra tags + the footer
  Credit Card/Bank Transfer chips + the two extra dropdown options =
  the clone's seed carrying paymentMethod values; the avatar letter
  U vs D). Zero unexplained visual drift.

**Step 5 — the remediation plan v37.** Written and validated against
the codebase pre-execution: the S1 insertion point (items.spec after
the v36 S3 census), the S1 pin-sanity target (select.tsx line ~19's
`focus:ring-1 focus:ring-ring`), the S2 target (input.tsx line ~10's
`focus-visible:ring-1 focus-visible:ring-ring`), the S3 target
(items-view.tsx's `paymentMethods` memo), and the seed's exact
arithmetic (Rent 1850 / Groceries 320 / Entertainment 65 → $385.00
for the two Credit Card expenses, $2235.00 at All).

**Step 6 — TDD execution.** S1 test first (the trigger's focus-visible
family): GREEN on the first run. Pin-sanity: stripping the
SelectTrigger's `focus:ring-1 focus:ring-ring` → the ring-layer
assertion FAILS; restored → GREEN. (The first mutation run passed
wrongly — the e2e drives the PRODUCTION build, so a rebuild is
required before a mutation can bite; the build then caught the new
tests' TS errors first — `document.activeElement.blur` and
`el.offsetWidth` on the SVGElement union — fixed with instanceof
guards and HTMLElement casts.) S2 test (the search focus + typing
contract): GREEN; the pin-sanity (stripping the Input's
`focus-visible:ring-1 focus-visible:ring-ring`) FAILS the focus-ring
assertion; restored → GREEN. S3 test (the payment-method filter's
full contract): GREEN; the pin-sanity (`.filter((p): p is string =>
!!p && false)` emptying the derivation) FAILS the options assertion;
restored → GREEN. The changeset verified via git diff: exactly the
one spec file, +149 lines, zero production changes.

**Step 7 — the full chain re-run.** lint ✓ · typecheck ✓ · 108/108
unit ✓ · build ✓ · **177/177 e2e** ✓ (174 → 177) · 35/35 smoke ✓.
The dev DB census clean (demo + the smoke test's throwaway users, 7
budget items). The 16 screenshots regenerated.

**Step 8 — docs aligned.** The probe README's v37 section (the L1/L2
lessons), README (the 177 counts + the v37 table row), CLAUDE.md (the
counts + the v37 surface entries), AGENTS.md (the v37 paragraph +
the O1 construct note), the SKILL doc (the state line + the Session
72 row), this session log, the repo worklog (Session 71), the
workspace worklog.

**Step 9 — ship.** Committed and pushed to `main` via the SSH
wrapper (`docs/ssh_git_wrapper_v3.py`, the runbook in
`docs/how-to-git-push-using-ssh-wrapper_SKILL.md`); the key
materialized outside the repo, fingerprint-verified, shredded after
the push.

**What this session delivered:**

- **Standing checks clean (31st consecutive)** — mobile-nav R1–R4 on
  both sites (**Tailwind v4 pins hold, the mobile menu works**), data
  drift (reference read-only, verified before + after), the SEO pair
  (+ the reference's capitalized sitemap URLs documented), one VLM
  pair (all flags data-explained)
- **The session-76 suggested surfaces all measured for the first
  time — ZERO production-code drift**: the filter triggers'
  focus-visible family (the visible layers byte-identical; the O1
  v3/v4 construct note), the search input's focus + typing contract
  (byte-identical), the /expenses payment-method filter (structure +
  dynamic derivation + round-trip byte-identical; the option-list
  difference is data-level)
- **Three new pins** (S1/S2/S3, TDD — every pin-sanity mutation
  verified to FAIL its pin) → **108/177/35 green**

**Suggested next steps**: the tooling pass still open from session 72
(the hasFocus() helper + the a11y CI step); or the next
suggested-surface queue — the frequency filter's option-list census
at /expenses (the payment-method sibling), the savings view's
filter-card instance, or the dashboard quick-action Add Item's focus
walk from the search input's family.
