# Session 110 — Parity iteration v48: the item-details sheet's shadow-2xl + the dialog-input focus composite at 390 + the empty-state full census — a PIN-ONLY iteration (2026-10-12)

**Goal:** the session-108 queue's first candidate (the item-details
sheet's panel shadow — the shadow-scale regression net's seventh
site) + the queue's fourth candidate (the dialog inputs' focus
composite at 390 — the v47 F1's mobile follow-up) + the queue's
third candidate (the empty-state cards' chrome via filter-to-zero).
TDD-first, docs aligned, commit + push via the SSH wrapper. (The
workspace was RESET this session: git clone 3f00e47 → npm install →
db:push → db:seed; the playwright chromium-1243 build fetched
pre-emptively — the v46 lesson.)

## What was done

**Step 0 — the workspace.** RESET this session (the sandbox's
zero-balance folder was gone). Cloned `3f00e47` (HEAD = the v47
delivery + session_109); rebuilt the environment (npm install → cp
.env.example .env + the dev AUTH_SECRET → db:push → db:seed → npx
playwright install chromium — the 1243 build matching the
lockfile-resolved 1.63.0). The five core docs + the four session docs
(session_108 / remediation-plan-v47 / worklog / session_109)
reviewed; the v47 state verified in code (net-worth-view.tsx:105/:210
mb-4, input.tsx's focus-visible:ring-1 stack, the 223→226 e2e count).

**Step 1 — the baseline chain.** lint ✓ · typecheck ✓ · 108/108 unit
✓ · build ✓ (robots + sitemap prerendered) · **226/226 e2e ✓ (5.3m)**
· 35/35 smoke ✓. The audit: npm audit = the same 5 dev-only
ESLint-chain advisories (`--omit=dev` = 0); the secret scan clean;
`.env` ≡ `.env.example` (modulo the documented dev AUTH_SECRET); the
v47 diff = tests + probes + docs only (no src/ change — the pin-only
contract verified in the log).

**Step 2 — the 42nd standing checks.** Reference side: all four bugs
live — the toast-blocker via elementFromPoint at the burger's center
(hit `DIV.fixed top-0 z-[100]`), the sheet-trap via the live nav
(sheet + overlay still open on /income after the nav click), no nav
landmark, the /networth 464 overflow; the data census read-only
before + after ("1 items · $25,000" networth, "1 items · $5,000.00"
income — the v46 restoration intact); the SEO pair live. Clone side
(`standing-checks-v48.sh` via with-server): R1 the burger hit-test
DIRECT (hitIsBurgerChild: true) + the sheet opens, R2 the sheet CLOSES
on nav (url /income, sheet + overlay gone), R3 the nav landmark, R4
zero overflow at 390 on all five routes (docSW 390 each), the SEO
pair live. **Superset intact.**

**Step 3 — the v48 sweep (three surfaces, both sites —
`ref-v48.sh` + `clone-v48.sh`, READ-ONLY on the reference).**
- **The item-details sheet's shadow-2xl (the net's SEVENTH site):**
  the reference's panel (card-body click → details; the layer `fixed
  inset-0 z-50` with bg rgba(26,58,46,0.5); the child panel
  `bg-white rounded-t-3xl md:rounded-2xl shadow-2xl max-w-lg w-full
  max-h-[85vh] overflow-y-auto`) — 512×680 (the 85vh cap at 800) /
  radius 16 / 2 transparent leads + `rgba(0,0,0,0.25) 0px 25px 50px
  -12px`; the clone's panel (the Radix Content, role=dialog) — 512×680
  / radius 16 / 4 transparent leads + **the SAME 2xl visible layer**
  (v4's 5-slot, the accepted class). The overlay + blur + the 36×36
  close button re-verified. **PIN-ONLY.**
- **The dialog-input focus composite at 390 (the v47 F1's mobile
  follow-up):** the input **w 310 on BOTH sites**; the rest + focus
  compositions identical in every visible layer (the shadow-sm layer
  at rest; the 1px rgb(10,10,10) ring + the persisting rest layer
  under REAL focus; the border unchanged; h 36 / radius 6 / pad 4px
  12px / border 1px rgb(229,229,229)). **PIN-ONLY — the family is
  viewport-independent.**
- **The empty-state full census (filter-to-zero):** the reference's
  /income frequency filter → One-time (its Salary is monthly — the
  list goes to zero; the filter reset verified after); the block:
  `text-center py-16` 358×328 / the 64px icon at opacity 0.2,
  rgb(10,10,10), mb 16 / the H3 20px-600-forest mb 8 / the P 16px
  gray mb 24 / the Add button h 36, w 147, the 135deg gradient, pad
  8px 16px, radius 6, fw 500, the v3 BARE shadow pair. The clone:
  **BYTE-PARITY on every dimension** (the search filter-to-zero idiom
  in the e2e). **PIN-ONLY.**
- The queue's toast item (session-108 #2) RESOLVED as
  superset-only-with-no-live-reference-surface: the reference's toast
  never fired on the empty-form saves (measured twice) — its toasts
  are rare-path only (the v10/v33 notes); a reference toast census
  needs a REAL data mutation, against the v46 read-only discipline.
  Deferred.

**Step 4 — the plan.** `docs/remediation-plan-v48.md` written (F1 +
F2 + F3 + the S1 four mutations + D1–D8), validated against the
codebase (the three spec targets + the idioms + the chain gate)
before execution.

**Step 5 — TDD.** The three pins written (`item-details.spec.ts` +
`dialog-buttons.spec.ts` + `empty-states.spec.ts`):
**3/3 GREEN immediately** (the pin-only discipline — the parity is
proven; the first F1 draft's close-button finder missed the sr-only
"Close" name, fixed to the accessible-name idiom). The S1
mutation-sanity — four mutations, each with the standalone REBUILD
(the v47 lesson pre-applied): (a) the panel's shadow-2xl removed →
F1 FAILS; (b) the input's ring-1 removed → F2 FAILS (and v47's F1 —
the shared class); (c) the icon mb-4→mb-2 → F3 FAILS (h 328→320);
(d) the `.zb-btn-add` shadow removed → F3 FAILS. All restored → the
clean tree verified (`git status src/` empty).

**Step 6 — the full chain + the VLM pair.** Rebuild + the gate: lint
✓ · typecheck ✓ · 108 unit ✓ · build ✓ · **229/229 e2e ✓ (5.3m —
226→229)** · 35/35 smoke ✓. The VLM pair on the /savings view at
1280 (`vlm-compare-v48.mjs`): 4 flags, **all DOM-verified as data
classes** — the richer seed's 2-card grid, the Recurring +
payment-method rows, the avatar initial; the badge chip chrome
byte-identical per classification value (the reference's need chip
rgb(254,242,242)/rgb(185,28,28) = the clone's need map exactly — the
v43 misattribution lesson's fourth application). No chrome gaps.

**Step 7 — the deliverables.** The 16 screenshots regenerated; the
probe files persisted (ref-v48.sh + clone-v48.sh +
standing-checks-v48.sh + vlm-compare-v48.mjs + the probe README's v48
section); the docs aligned (AGENTS/CLAUDE/README/SKILL Session 83 row
+ the 229 state/PAD v1.1.5/session_110 + session_111/the repo worklog
Session 82 + the ledger list); the commit + the SSH-wrapper push.

## Standing checks

- Mobile-nav R1–R4: **42nd consecutive pass** (both sites).
- Data drift: reference read-only throughout (the frequency filter
  reset verified by the after-census; the v46 restoration intact).
- SEO: robots + sitemap live on both sites.
- npm audit: unchanged (5 dev-only; --omit=dev = 0).

## Outcome

Three new e2e (226 → 229), 108/229/35 green, the net's seventh
shadow site pinned, the v47 composite extended to mobile, the empty
state fully censused. NO production-code change (the fourth pin-only
iteration of the v45 family).
