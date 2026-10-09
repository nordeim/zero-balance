# Session 57 — Parity iteration v28 (session-55 brief)

I continued the comprehensive zero-balance remediation workflow. This
iteration referenced `docs/session_55.md` / `docs/remediation-plan-v27.md`
/ `worklog.md` / `docs/session_56.md`. Full autonomy granted on the open
questions, so I worked the whole chain directly.

**Step 1 — workspace refresh.** The sandbox had been RESET — both repos
re-cloned fresh (`zero-balance` at `8329114`, `scandihaven` at `d4789c3`
— unchanged from the v27 verification); the environment rebuilt and
re-verified: `.env` from the accurate `.env.example`
(`DATABASE_URL="file:../db/custom.db"`), `db/` re-pushed + re-seeded at
the repo root (7 budget items, 3 assets, 2 liabilities for
`demo@zerobalance.app`), node_modules reinstalled, Vitest/Playwright
configs intact, robots.txt + sitemap.xml prerendering in the build. The
five project docs + four session docs re-read; the codebase validated
against them — the v27 changeset (`eca1754`) in place (the `dialog.tsx`
X-close class string + the extended v9 spec, all pinned).

**Step 2 — the audit.** The baseline chain green on the first run: lint ✓
· typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**155/155 e2e** ✓ · 35/35 smoke ✓. Audit Phase 2 clean: the same 5
dev-only ESLint `braces` advisories (no patched release — accepted), the
secret-pattern scan matching only the documented files.

**Step 3 — the two-site sweep** (agent-browser on the ONE shared tab +
the :3200 parity server; the fresh-open + settle + parked-pointer
disciplines throughout):

- **Mobile navigation (the task focus) R1–R4 all re-verified live on BOTH
  sites — the 22nd consecutive check.** R1: the reference's two `fixed
  top-0 z-[100]` toast containers still intercept the burger's center hit
  at (38,30) (`pe:auto`, 390×32, z-100; scrollWidth 395 on `/`), while
  the clone's burger hit is DIRECT on the svg with the viewport
  `pe:none` and 390 fit on every route. R2: the reference's sheet still
  traps after nav; the clone's closes (superset fix #2) — sheet 288px +
  Income link (20,185) 247×32 identical. R3: the reference marks nothing
  active on `/`; the clone highlights Dashboard (the documented
  superset). R4: the reference overflows 395 on `/`+`/dashboard` and 464
  on `/networth`; the clone fits 390 on all six routes. **The Tailwind v4
  pins hold — the clone's mobile menu works as expected.**
- **Data drift clean (22nd — with an explicit probe-cycle hygiene note)**:
  the reference unchanged (allocation 30.5%, Balance `$3475.00`, income
  `$5000.00`/1, savings `$1000.00`/1, expenses `$525.00`/4). The toast
  probes added then DELETED four throwaway items through the reference's
  own UI; the census re-verified clean afterwards.
- **SEO pair ✓**: both sites serve robots.txt (allow-all + the sitemap
  link) and sitemap.xml (five URLs, `/login` excluded).
- **The one-pass button-variant census (session-55's suggestion)**: every
  `<button>` on the items views, full class strings, both sites — the Add
  buttons (the `zb-btn-add` gradient pin, focus family verified v27),
  the three Select triggers (byte-identical), and the income card's
  hover-revealed 36×36 ghost-icon button all match; the census surfaced
  the TWO drifting families (G1 + G2 below).
- **The card action-menu trigger ("Active ▾", session-55's suggestion)**:
  the reference's status element is a plain DIV — no menu, no click
  handler; its `cursor: pointer` is inherited from the card. But the
  class read surfaced the REAL drift: the reference's card badges carry
  the shadcn Badge base with `transition-colors
  hover:bg-secondary/80`, and on a REAL CDP hover they tint to
  **`rgba(245, 245, 245, 0.8)`** (measured on the status and need
  badges; the clone's badges stayed static under the same hover) → G1.
- **The avatar/user chip (suggestion)**: non-interactive on both sites
  (the reference's sidebar footer row has no role/tabindex/handler; the
  clone's `UserFooter` matches the pinned structure) — NO finding.
- **The toast close buttons (suggestion)**: the reference renders **NO
  toasts at all** — the add-success flow leaves both toast viewports at
  their empty 32px padding (heights sampled at 200ms/900ms/3.4s after
  the save: [32, 32]). The clone's toasts + close buttons remain the
  established superset. No reference surface to compare — no finding.
- **THE HEADLINE — the Budget Item Details sheet (found while probing the
  card-click path)**: on the reference, clicking an item card BODY opens
  a read-only "Budget Item Details" sheet; the clone's card click did
  NOTHING (verified live: no overlay, no text change). The full contract
  measured across all three types and both viewports: the forest-50% +
  blur(8px) overlay (`items-end md:items-center` — a bottom sheet at
  mobile: x=0, w=390, bottom=844, radius 24px top-only; centered
  `max-w-lg` 512px at desktop), the sticky header + X-close, the
  centered summary (type/classification pill badges, `text-2xl` forest
  name, `text-4xl` type-colored amount), the tinted classification block
  (a separate details-copy map from the guidelines card), the icon-led
  fact rows (Date/Frequency/Recurring/Payment Method?/Status + the
  taller Notes? variant), and the Created/Last Updated footer → G3.
- Probe-methodology lessons (persisted in the probe README): synthetic
  `mouseenter`/`pointerover` NEVER engages CSS `:hover` — the REAL
  `agent-browser mouse move` to the element's center is the only hover
  arbiter; the reference's dialogs are plain divs that do NOT close on
  Escape (the X is the only close — the clone's Radix Escape-close
  remains the documented superset); and the reference's dialog
  number-input keeps an EMPTY value ("0.00" is its placeholder — match
  `input[type=number]` when probing).

**Step 4 — the plan + TDD.** `docs/remediation-plan-v28.md` written and
validated against the codebase (grep-verified scopes: the four badge
strings, the two button strings, the five-slot modal pattern, the
types' notes/createdAt/updatedAt fields, no existing card-click spec).
TDD: G1+G2 spec extensions written RED first (the class assertions
failed exactly on the drifting strings) → the class-string fixes →
GREEN → pin-sanity mutations (a wrong hover class + a flipped ring
width) both FAIL → restored. G3: the new `item-details.spec.ts` written
RED first (`getByRole('dialog')` not found) → the build (the store's
`details` slot + `item-details-dialog.tsx` + the card's guarded onClick
+ the app-shell mount) → GREEN → pin-sanity mutations (a wrong amount
color + a flipped Recurring fact) FAIL → restored. **One live-verified
refinement: the direct `hover:bg-secondary/80` utility computes as
oklab `lab(96.5375 0 0 / 0.8)` on the clone — the v4 oklab drift (the
v7 G6 lesson) — so the tint is pinned via `.zb-badge-hover` in
globals.css, computing `rgba(245, 245, 245, 0.8)` byte-identically to
the reference.**

**Step 5 — the chain.** **FULL CHAIN GREEN: 108 unit · 158 e2e (3 new)
· 35 smoke** + lint + typecheck + build. Live re-verification on the
:3200 parity server: the card click opens the sheet (desktop 512×680
centered at (384,60), mobile x=0/y=127/w=390/bottom=844/radius 24px
top-only — byte-identical to the reference's measured geometry); the
badges tint to `rgba(245,245,245,0.8)` on a real CDP hover with the
150ms transition; the Edit's real-Tab ring reads `rgb(10,10,10) 0 0 0
1px` + the shadow-md ambient. The screenshots regenerated — 15
byte-identical + the NEW `16-item-details.png` (the capture script
gained the 6b details step).

**Step 6 — docs + ship.** README (the v28 row + the 158 counts + the
16-shot set), CLAUDE.md (the e2e description), AGENTS.md (the v28 pin
paragraph), the SKILL doc (the session row + the state), the probe
README (the v28 catalog), this session log, the worklog.

## What this session did

- **Workspace re-cloned + environment rebuilt** (the sandbox reset);
  all standing requirements re-verified in place
- **Baseline fully green on the first run** — 108/155/35; the audit
  clean (the same 5 dev-only advisories, no secrets)
- **Standing checks all clean**: mobile-nav R1–R4 (22nd — Tailwind v4
  pins hold, both sites), data drift (22nd — with the probe cycle's
  add-then-delete hygiene), the SEO pair
- **THREE fixes** (`docs/remediation-plan-v28.md`):
  - **G3 (the headline — a whole missing surface)**: the Budget Item
    Details sheet — the reference's card-body-click read-only view,
    fully measured (both viewports, all three types) and built
    (component + store slot + guarded card onClick + app-shell mount)
  - **G1**: the card badges' hover tint — `.zb-badge-hover` pinning
    the reference's exact computed `rgba(245,245,245,0.8)`
  - **G2**: the expense-card Edit/Calculate buttons' keyboard family —
    `focus-visible:ring-1` + the Edit's `hover:text-accent-foreground`
- **The session-55 suggested surfaces all resolved**: the button census
  (two drifts found), the avatar chip (non-interactive on both — no
  finding), the toast close buttons (the reference renders none — no
  finding)
- Full chain now **108/158/35 green**; docs/screenshots (+
  `16-item-details.png`)/worklog aligned; committed and pushed to main
  via the SSH wrapper

**Suggested next steps**: the details sheet opens a new family of
surfaces to sweep — the sheet's KEYBOARD semantics on both sites (the
reference's plain-div sheet vs the clone's Radix trap + which element
gets initial focus), a VLM pairwise of the new
`16-item-details.png` against the reference's sheet, and the
edit-dialog-vs-details-sheet entry-point consistency (does the
reference's ellipsis-menu Edit open the same form as the footer Edit?);
alternatively continue the interactive-family census at the net-worth
view (its tab triggers + asset/liability card families were never
class-diffed). Just re-issue the brief referencing
`docs/session_57.md` / `docs/remediation-plan-v28.md` and I'll pick it
up from there.
