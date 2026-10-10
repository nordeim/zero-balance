Workspace refreshed via git pull — commit 51f1fd9 (the session-73 transcript) landed; the environment otherwise intact from session 68.
The five project docs re-read (AGENTS, CLAUDE, README, PAD, SKILL); the v35 changeset verified in place (the G1 cascade fix, the G2 trigger rings, the S1/S2/S3 pins).
Baseline audit chain green on the FIRST full run: lint, typecheck, 108/108 unit, build (robots + sitemap prerendered), 171/171 e2e, 35/35 smoke. npm audit: the same 5 dev-only advisories; secret scan clean; .env.example current.
Now the two-site sweep. First, login to the reference site on the ref36 session.
Data drift census clean (30th): allocation 30.5%, income $5000.00/1, savings $1000.00/1, expenses $525.00/4.
Mobile-nav R1–R4 on the reference (the 30th): the toast-blocker, sheet-trap, no-landmark, and the 395/464 overflows all still live.
SEO pair on the reference: robots.txt + sitemap.xml + the full head census — all matching the pinned values.
Now Surface A — the item-card menu's hover-highlight family. First probe with synthetic mouse events.
The synthetic events did NOT move the highlight — the probe lesson: only a REAL pointer move triggers Radix's roving. Retrying with agent-browser's native hover.
REAL hover on the reference's Delete: DOM focus moves to the item, the accent family renders (bg rgb(245,245,245) + text rgb(23,23,23)) — the hovered Delete NOT red.
Mouseleave on the reference: focus returns to the container, both items at rest, the menu survives. Escape closes + refocuses the trigger.
Now the clone side — boot the :3200 parity server via with-server.sh, login, census, and the same hover measurement.
CLONE hover family: byte-identical (the v35 G1 cascade holds on the hover path). Mouseleave + Escape also identical.
Surface B — the filter Selects' listbox keyboard contract on /income (the instances v34 never measured). Opening the reference's category filter.
Reference fresh-open: focus on the SELECTED option with the accent highlight — both click-open and Enter-open land identically (unlike the DropdownMenu).
The full keyboard matrix on the reference: arrows rove clamped at both ends, Home/End jump, Escape closes the popup only (focus to the trigger), Enter selects + updates the trigger text. Filter reset to All Categories after (read-only discipline).
One observation: the reference persists aria-controls on its CLOSED trigger — a Radix-version detail; both carry the matching attribute while OPEN. Not drift.
CLONE Surface B: byte-identical on the full contract. The category list differs in length (3 options vs 2 — the demo seed's Freelance item; data-level).
Surface C — the items-view Tab-order census. REAL-Tab walks on both sites (16–18 stops, 450ms settles).
The reference's walk: nav×5 → Add Income → search input → category combobox → frequency combobox → the card kebab (opacity 0!) → an 18×18 "Close badge" button → wrap.
Investigating the "Close badge": it's #base44-edit-badge — the Base44 PLATFORM's floating "Edit with Base44" widget. Platform chrome, not app UI. The clone correctly omits it.
KEY FINDING: the reference's kebab reads opacity 0 RIGHT AFTER the landing Tab — the reference's trigger stays INVISIBLE when keyboard-focused. The clone's reads 1 (its day-one focus-visible:opacity-100 engaged).
Verifying directly: programmatic focus on the reference's trigger — :focus-visible matches, the ring computes, opacity still 0. The reference's keyboard users lose the visual focus at that stop. The clone's reveal is superset #7.
Also documented: the clone's comboboxes/search carry invisible aria-labels (day-one supersets); the aria-controls closed-state persistence.
CLONE Tab walk: the identical sequence (nav×5 → Add → search → combobox×2 → 2 kebabs → wrap). Order byte-identical modulo data count.
VLM pairs captured (dashboard + /income filter-open, viewport-asserted 1280×800): both verdicts DIFFERENT but ALL flags DOM-explained (superset #3 + demo data + the platform badge). Zero unexplained drift.
Reference census re-verified after all probes — unchanged (read-only discipline held).
The sweep complete: NO production-code drift. Writing docs/remediation-plan-v36.md (validated against the codebase pre-execution).
TDD — S1 test first (the hover-highlight family pin in tokens.spec.ts). GREEN on the first run.
S1 pin-sanity: re-adding the focus:text-[#dc2626] override → the hovered-Delete assertion FAILS. Restored → GREEN.
S2 test (the filter listbox contract pin in items.spec.ts). The fixture-restore step initially went RED — Radix Select's post-open focus landing is ASYNC and the racing Home hit the trigger. Fixed by interleaving a toBeFocused() (the AGENTS.md e2e-race lesson). Then GREEN.
S2 pin-sanity: stripping the SelectItem's focus:bg-accent → the highlight assertion FAILS. Restored → GREEN.
S3 test (the Tab-order census + the kebab reveal pin). GREEN on the first run.
S3 pin-sanity: stripping the trigger's focus-visible:opacity-100 → the reveal assertion FAILS. Restored → GREEN.
The changeset verified via git diff: exactly the two spec files, 269 insertions, zero production-code changes.
Full chain re-run: lint, typecheck, 108/108 unit, build, 174/174 e2e (171 → 174), 35/35 smoke. Dev DB census clean. The 16 screenshots regenerated (byte-identical — no production changes).
Docs aligned: probe README v36 section, README v36 row + 174 counts, CLAUDE.md, AGENTS.md (superset #7), SKILL doc, session_74.md, the repo worklog Session 70, the workspace worklog.
The wrapper runbook reviewed; the shim staged outside the repo (python3.13 shebang — the paramiko build); the key materialized + fingerprint verified.
Commit fa62a7f landed. The wrapper dry-run (the correct zero-balance remote), then the real push.
**Parity iteration v36 shipped to main** (commit fa62a7f, remote-verified, key shredded).

**What this session delivered:**

- **Standing checks clean (30th consecutive)** — mobile-nav R1–R4 on both sites (**Tailwind v4 pins hold, the mobile menu works**), data drift (reference read-only, verified before + after), the SEO pair, the VLM pairs (all flags DOM-explained)
- **The session-72 suggested surfaces all measured for the first time — ZERO production-code drift**: the hover-highlight family (byte-identical — the v35 G1 cascade holds on the hover path), the filter Selects' listbox keyboard contract (byte-identical), the items-view Tab-order census (order byte-identical)
- **Superset #7 documented + pinned**: the reference's kebab trigger stays INVISIBLE when keyboard-focused/keyboard-opened; the clone's day-one reveal classes keep it visible
- **Three new pins** (S1/S2/S3, TDD — every mutation verified to FAIL its pin) → **108/174/35 green**

**Suggested next steps**: the filter triggers' focus-visible family, the search input's focus/typing contract, the expenses payment-method filter (the third Select), or the tooling pass (the hasFocus() helper + the a11y CI step — still open from session 72).
