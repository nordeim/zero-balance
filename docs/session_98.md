# Session 98 — Parity iteration v44: the drill-down expansion ANIMATION + the chevron GLYPH swap + the 390/1280 census + the donut-legend census (2026-10-11)

**Goal:** the session-95/96/97 queue — the drill-down's EXPANDED-state
census at the remaining viewports (390 mobile / 1280 desktop — the 640
class was pinned in v43), the donut legend's geometry/interaction
states, and whatever the sweep finds. TDD-first, docs aligned, commit +
push via the SSH wrapper.

## What was done

**Step 0 — the workspace.** The sandbox had been reset (the repo
directory was gone): a fresh `git clone` + `npm install` + `prisma
generate` + `db:push` + `db:seed` + `playwright install chromium` +
`.env` from `.env.example` (byte-identical). The environment rebuilt.

**Step 1 — the baseline chain.** lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · **209/209 e2e ✓ (4.6m)** —
one earlier run showed 208/209 with a single verify-email failure, a
back-to-back register-bucket collision (the same class as the
documented rate-limit discipline), re-run green · 35/35 smoke ✓. npm
audit = the same 5 dev-only ESLint-chain advisories; the secret scan
clean; the v43 diff re-audited (exactly the documented changeset).

**Step 2 — the 38th standing checks.** Reference side: R1 the
toast-blocker still intercepts the burger (hit_is_burger false), R2 the
sheet still traps after navigation, R3 no nav landmark, R4 the 395
overflow on / and /dashboard — all four reference bugs still live; the
data census read-only (identical before + after); the SEO pair live.
Clone side (inside one with-server.sh): R1 the burger hit direct, R2
the sheet closes after nav, R3 the nav landmark present, R4 zero
overflow on all routes; the sheet's dialog-role/labelledby/nav/title
structure intact; the SEO pair live. **All clean — the superset
intact.**

**Step 3 — the v44 sweep (the queue's surfaces, measured live on BOTH
sites at 390×844 AND 1280×800).** Probes: `exp-vp-v44.mjs` (the
drill-down census + the expansion-height samples), `legend-v44.mjs`
(the donut legend), `collapse-ref-v44.mjs` + `band-mount-v44.mjs` (the
reference's collapse direction + mount semantics), `chev-glyph-v44.mjs`
(the glyph verification). Drivers: `vp-census-v44.sh` +
`clone-v44.sh`.

- **F1 — THE animation gap (the first production-code change since
  v43):** the reference's drill-down bands ANIMATE — the card ramps
  ~200ms in BOTH directions (324→346→364→387→398→405 on the section
  expand at 390; 459→429→384→359→339→324 on the collapse; the category
  level the same), mid-collapse the band's INLINE height reads
  25.5455px (a per-frame JS tween — no CSS transition writes the style
  attribute per frame) with the opacity easing concurrently (computed
  0.314 at 110ms), the end state `height: auto; opacity: 1`, and the
  section band UNMOUNTS after the collapse animation. The clone
  mounted/unmounted instantly (324→441 at the first sample — zero
  in-flight frames).
- **F4 — the glyph swap (found by the standing VLM pair, DOM-verified
  real):** the reference's chevrons SWAP ICONS — lucide-chevron-down
  when collapsed ↔ lucide-chevron-up when expanded, both levels
  (section 14px w-3.5, category 12px w-3), rotate: none at every
  state. The v43 "static" finding was correct-but-incomplete: the flip
  is the ICON, not the transform — **a computed-style census cannot see
  a glyph swap; read the svg's class.**
- **F2 — the 390/1280 census (pin-only):** the chrome byte-identical
  at every level on both sites; the 1280 section label WRAPS to two
  lines (labelH 40, row 56 — on BOTH sites: the v42 collapsed census's
  56px row explained, width-driven); the mobile indentation arithmetic
  identical (the inner ml 40px/mt 8px — no responsive indent); the
  clone's sw 390 fully expanded (the superset — the reference reads
  395, its own overflow bug).
- **F3 — the donut legend census (pin-only, the queue item
  resolved):** the geometry byte-identical (h 64/pad 12/radius 8/bg
  245,248,245; the label 16/500/forestDark; the amount 16/700 in the
  classification color; the pct 12/gray; the dot 16×16/r4; the icon
  16×16; the gap 12; the container mt 24) and the REAL hover INERT on
  both sites (bg/shadow/cursor unchanged, `changed: false`) — no
  interaction states exist to match.

**Step 4 — the plan.** `docs/remediation-plan-v44.md` written and
validated against the codebase (the two band targets, the existing
pins' settle discipline, the accordion count-0 assertions vs the
delayed unmount, the a11y gate's post-settle scans).

**Step 5 — TDD.** The five e2e written FIRST: the animation pin (RED
pre-fix — zero in-flight samples), the 390 census, the 1280 census,
the legend census, the glyph-swap pin (RED pre-fix — chevron-down at
every state). The fixes: the `Collapse` wrapper (the grid 0fr↔1f
technique + `@starting-style` for the entry + the onTransitionEnd
delayed unmount — the collapsed DOM returns to exactly the pre-fix
node tree; the render-phase mount flip via the
adjust-state-during-render pattern with a prev-value STATE, not a ref
— react-hooks/refs forbids ref access during render) + the chevron
glyph swap at both levels. GREEN on the first run.

**Step 6 — five pin-sanity mutations, each verified to FAIL:** (a) the
zeroed duration → the in-flight pin fails; (b) the removed
@starting-style → the entry pin fails; (c) the legend p-3→p-4 → the
legend census fails (64→72); (d) the sub-row py-1→py-2 → the 390
census fails; (e) the reverted glyph swap → the glyph pin fails. All
restored → GREEN.

**Step 7 — the full chain.** lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **214/214 e2e ✓ (4.9m — 209 → 214)** · 35/35 smoke ✓. The 16
screenshots regenerated (the drill-down shot now shows the swapped
chevron-up glyph when expanded).

**Step 8 — the standing VLM pair.** The expanded drill-down post-fix:
the glyph-direction flag WAS real (the F4 fix — the VLM screening
earns its keep; the opposite of v43's misattributed Base44 badge); the
other flags (the icon outline-vs-solid, the bold labels) were
screenshot-scale misreads, DOM-refuted (the lucide classes and the
font weights identical). The data-level flags (the seed's 2 categories
vs the reference's 1, the item labels) in the known classes.

**Step 9 — docs aligned.** AGENTS.md (the v44 paragraph), CLAUDE.md
(the 214 count + the v44 census entry), README (the v44 row + the
testing-section counts 206→214 — a stale v42-era count the v43
D-series missed), the SKILL doc (the five count sites + the Session 79
row), the PAD (the v1.1.1 revision block), the probe README (the v44
section: the six probes + the drivers + the lessons), session_98.md
(this log), session_99.md (the raw transcript), the repo worklog
Session 78, the workspace worklog.

**Step 10 — commit + push via the SSH wrapper.** The verification gate
green (108/214/35). The commit lands on main; the key materialized,
the fingerprint verified, the dry-run clean, the push verified, the
key shredded.

## What this session delivered

- **The drill-down expansion ANIMATION shipped** — the reference's
  ~200ms height+opacity tween (both levels, both directions) rebuilt
  via the grid 0fr↔1f + @starting-style + the delayed unmount; the
  collapsed DOM byte-identical to the pre-fix tree
- **The chevron GLYPH swap shipped** — chevron-down ↔ chevron-up (the
  VLM-found, DOM-verified gap; the computed-style census lesson)
- **The 390/1280 census + the donut-legend census pinned** — the queue
  items closed with the chrome byte-identical and the legend's
  interaction resolved (inert on both)
- **5 new e2e (209 → 214)** — 108/214/35 green, five mutations
  verified
- Standing checks clean (38th): mobile-nav R1–R4 both sites (Tailwind
  v4 pins hold, the mobile menu works), data drift (reference
  read-only), the SEO pair, the VLM pair (one REAL flag)

**Suggested next steps**: re-issue the brief referencing
`docs/session_98.md` / `docs/remediation-plan-v44.md` — the queue
candidates: the drill-down's animation census on the CATEGORY level
pinned at the other viewports (the F1 pin covers the section level),
the items-view card chrome at 1280 (the kebab-family geometry), the
calculator's row hover at 640, or a fresh surface of your choosing.
