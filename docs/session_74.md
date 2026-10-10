# Session 74 — Parity iteration v36 (session-72 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_72.md` /
`docs/remediation-plan-v35.md` / `worklog.md` / `docs/session_73.md`.
Full autonomy granted on the open questions, so I worked the whole
chain directly.

**Step 1 — workspace refresh.** `git pull` brought `51f1fd9` (the
session-73 transcript commit). The workspace was otherwise intact
from session 68 (node_modules, the seeded `db/` at the repo root,
`.env` with `DATABASE_URL="file:../db/custom.db"`, scandihaven at the
workspace root). The five project docs re-read; the codebase validated
against them — the v35 changeset in place (the G1 cascade fix, the G2
trigger rings, the S1/S2/S3 pins), verified by the full chain below.

**Step 2 — the audit.** The baseline chain green on the FIRST full
run: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots +
sitemap prerendered) · **171/171 e2e ✓** · 35/35 smoke ✓. Audit Phase
2 clean: the same 5 dev-only ESLint `braces`/eslint-config-next
advisories (no patched release — accepted, dev-only), the
secret-pattern scan clean, `.env.example` verified current (keys
matching `.env`). The Sitemap/SEO surface re-verified live in the
sweep below (robots.txt allow-all, the five-URL/priority sitemap, the
full head census — all matching the pinned values).

**Step 3 — the two-site sweep** (agent-browser on the ref36/clone36
sessions + the :3200 parity server inside `with-server.sh`; the
fresh-open + settle + parked-pointer + real-click/real-hover/real-Tab
disciplines + the v34 `document.hasFocus()` gate throughout):

- **Mobile navigation (the task focus) R1–R4 all re-verified live on
  BOTH sites — the 30th consecutive check.** R1: the reference's
  `fixed top-0 z-[100]` toast containers still intercept the burger's
  center hit (scrollWidth 395), the clone's hit DIRECT on the svg
  with 390 fit. R2: the reference's sheet still traps after nav; the
  clone's closes (superset #2). R3: the reference marks nothing
  active on `/` and has no `<nav>`; the clone highlights Dashboard +
  has the landmark. R4: the reference overflows 395 on `/`+`/dashboard`
  and 464 on `/networth`; the clone fits 390 on all routes. **The
  Tailwind v4 pins hold — the mobile menu works as expected.**
- **Data drift clean (30th)**: the reference's own census re-verified
  BEFORE and AFTER all probes (allocation 30.5%, income `$5000.00`/1,
  savings `$1000.00`/1, expenses `$525.00`/4 — read-only throughout;
  the filter probes reset their selections, the menu probes
  Escape-closed, nothing selected). The clone's seed census unchanged
  (62.8% / 5550 / 1250 / 2235).
- **SEO pair ✓**: robots.txt + sitemap.xml live on both; the
  reference's head-metadata census re-captured (title, canonical,
  description, the og/twitter pair, apple-mobile-web-app-title,
  manifest) — all matching the pinned values.
- **Suggestion #1 — the item-card menu's HOVER-highlight family: NO
  drift (first-time REAL-hover measurement; the S1 pin).** The full
  contract measured on BOTH sites with `agent-browser hover`: the
  synthetic `dispatchEvent(mousemove/mouseenter)` does NOT move
  Radix's highlight — the first probe fabricated "the reference
  ignores hover" until the real-pointer retry. The genuine contract:
  a REAL hover on the Delete item moves DOM focus to it (`:focus`
  matches, `data-highlighted` present) and renders the SAME accent
  family as keyboard focus (bg `rgb(245,245,245)` + text
  `rgb(23,23,23)` — the v35 G1 cascade holds on the hover path; the
  hovered Delete is NOT red); moving the pointer off the menu returns
  focus to the CONTAINER and both items to rest (Delete red again,
  `data-highlighted` cleared) with the menu still open; Escape closes
  and refocuses the trigger. Byte-identical on both sites.
- **Suggestion #2 — the filter Selects' listbox keyboard contract
  (the `/income` instances): NO drift (first-time measurement; the S2
  pin).** The full Radix combobox contract on BOTH sites: fresh-open
  via CLICK and via ENTER both land focus on the SELECTED option
  (`aria-selected=true`, the accent family — unlike the DropdownMenu,
  the Select's two open paths land identically); the arrows rove with
  the highlight; CLAMPED at both ends; Home/End jump; Escape closes
  the popup only (focus → the TRIGGER, the page stays — no dialog in
  the filter instance); Enter selects the highlighted option (the
  trigger's text updates, focus rests on the trigger). The clone's
  category list differs in LENGTH (3 options vs 2 — the demo seed's
  Freelance item; data-level). Observations documented, not drift: the
  reference persists `aria-controls` on its CLOSED trigger (a
  Radix-minor-version detail — both carry the matching attribute while
  OPEN; the id formats differ by React useId generation, cosmetic);
  the clone's comboboxes carry invisible aria-labels (a day-one a11y
  superset — the reference's are value-named only).
- **Suggestion #3 — the items-view Tab-order census: the ORDER
  byte-identical (first-time PAGE-level measurement; the S3 pin) +
  superset #7 documented.** The REAL-Tab walk on `/income` at
  1280×800, both sites: the five nav links (215×32, x=20, the 40px
  rail pitch) → Add Income (147×36) → the search input (447×36) → the
  category combobox (216×36) → the frequency combobox (216×36) → the
  card kebabs (36×36, one per card — the clone's 2 cards vs the
  reference's 1 = data-level) → wrap. IDENTICAL sequence and geometry.
  Findings: **O1 — superset #7**: the reference's kebab stays
  INVISIBLE (opacity 0) when keyboard-focused (measured: `:focus-visible`
  matches, the ring computes, the element renders nothing) and when
  keyboard-opened; the clone's day-one `focus-visible:opacity-100` +
  `data-[state=open]:opacity-100` reveal it (a keyboard user on the
  reference loses the visual focus at that stop) — now documented and
  pinned. **O2**: the clone's filter comboboxes + search input carry
  invisible aria-labels (day-one supersets). **O3**: the reference's
  walk includes the Base44 PLATFORM badge ("Edit with Base44" +
  its 18×18 "Close badge" button, `#base44-edit-badge`, fixed
  bottom-right, z-index 999999) — platform chrome, correctly absent
  on the clone; excluded from tab-order comparisons.
- **The VLM pairwise (two fresh pairs, viewport-asserted 1280×800)**:
  the dashboard — all four flags DOM-explained (the Dashboard-active
  rail = superset #3; the progress fill + the avatar letter = the
  different demo data; the "Edit with Base44" button = the O3 platform
  chrome); the `/income` page with the filter Select OPEN — all three
  flags data-explained (the card count, the option count, the avatar
  letter). Zero unexplained visual drift.

**Step 4 — the plan + TDD** (`docs/remediation-plan-v36.md`, validated
against the codebase pre-execution). No production-code drift — the
three pins are pure test additions. S1 (the hover-highlight family):
GREEN on the first run; pin-sanity (re-adding the v35-G1
`focus:text-[#dc2626]` override) → the hovered-Delete assertion
FAILS ✓ → restored → GREEN. S2 (the filter listbox contract): the
fixture-restore step initially went RED — Radix Select's post-open
focus landing is ASYNC and the racing Home hit the trigger instead
(the AGENTS.md e2e-race lesson; fixed by interleaving a `toBeFocused()`);
then GREEN; pin-sanity (stripping the SelectItem's `focus:bg-accent`)
→ the selected-option highlight assertion FAILS ✓ → restored → GREEN.
S3 (the Tab-order census + the kebab reveal): GREEN on the first run;
pin-sanity (stripping the trigger's `focus-visible:opacity-100`) →
the reveal assertion FAILS ✓ → restored → GREEN. The final changeset
verified against `git diff`: exactly the two spec files, 269 insertions,
zero production-code changes.

**Step 5 — the chain.** **FULL CHAIN GREEN: 108 unit · 174 e2e
(171 → 174) · 35 smoke** + lint + typecheck + build. The dev DB
census clean (7 items / 0 line items / demo + smoke throwaways only).
The 16 screenshots regenerated — byte-identical (no production-code
changes; expected).

**Step 6 — docs + ship.** The probe README (the v36 catalog + the
L1–L5 lessons), README (the v36 row + the 174 counts), CLAUDE.md (the
174 count + the v36 surface entries), AGENTS.md (the v36 paragraph +
superset #7), the SKILL doc (the state line + the Session-71 row),
this session log, the repo worklog (the Session 70 entry), the
workspace worklog.

## What this session did

- **Workspace refreshed** (`51f1fd9` pulled; the environment intact);
  the baseline chain green on the first full run
- **Standing checks all clean (30th consecutive)**: mobile-nav R1–R4
  on both sites (**Tailwind v4 pins hold, the mobile menu works**),
  data drift (reference read-only, verified before + after), the SEO
  pair
- **The session-72 suggested surfaces all swept with first-time
  measurements — ZERO production-code drift**: the hover-highlight
  family (byte-identical, the v35 G1 cascade holds on the hover path),
  the filter Selects' listbox keyboard contract (byte-identical), the
  items-view Tab-order census (order byte-identical)
- **Three new pins** (S1/S2/S3, TDD with pin-sanity mutations that
  all bite) + **superset #7 documented** (the kebab's keyboard
  reveal — the reference's trigger stays invisible when
  keyboard-focused) + the platform-badge exclusion documented →
  **108/174/35 green**
- Full chain green; docs/screenshots/worklog aligned; committed and
  pushed to main via the SSH wrapper

**Suggested next steps**: the unmeasured families keep shrinking —
the filter selects' TRIGGER focus-visible family (the v13/v25 pins
cover the dialog instances and the login surface; the filter-card
triggers' focus ring was never separately measured), the search
input's focus/typing contract (first-key behavior, the clearing
cross), or the expenses view's payment-method filter (the third
Select, never measured). Or the tooling pass (the
`document.hasFocus()` assertion helper baked into the standing
scripts, the Playwright a11y audit CI step — the session-72
suggestion that remains open). Just re-issue the brief referencing
`docs/session_74.md` / `docs/remediation-plan-v36.md` and I'll pick
it up from there.
