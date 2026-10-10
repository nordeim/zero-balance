I'll continue the recurring zero-balance task. Let me start by checking the workspace state — the sandbox was reset, so I'll clone the repo fresh.

The repo is cloned at f9a9637 (the v30 session-log commit). Let me set up the environment: node_modules, .env, db, and the scandihaven reference clone — all in parallel with the doc reading.

npm install + db push + seed done. Now the project docs — AGENTS.md, CLAUDE.md, README, PAD, SKILL — then the session_61 / remediation-plan-v30 / worklog / session_62 set. The project is at parity iteration v30 (108/161/35); my brief is the same recurring pattern, so this session is iteration v31.

The codebase structure validates against the docs. Let me run the baseline audit chain (Phase 1: lint + typecheck + unit).

Lint ✓, typecheck ✓, 108/108 unit ✓. Now the production build (robots + sitemap prerendered — SEO confirmed at build level), then the e2e suite and the smoke test.

**Full baseline chain green on the FIRST full run**: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ · 161/161 e2e ✓ · 35/35 smoke ✓. Audit Phase 2: npm audit = the same 5 dev-only advisories (accepted); the secret scan matches only documented files; .env.example current. **Audit clean.**

Now the two-site sweep. Reference login first — with the password's `$` at the START ($Abcd1234), the first attempt typed it wrong; the eval-based refill with the escaped \$ works.

Logged in. Data census (25th): allocation 30.5%, Balance $3475.00, income $5000/1, savings $1000/1, expenses $525/4 — clean, read-only.

Mobile-nav R1–R4 on the reference (25th): R1 the toast container still blocks the burger (hit DIV.fixed.top-0.z-[100], 395); R2 the sheet traps after nav (overlay + body locked on /income — screenshot captured); R3 nothing active on /, no nav landmark; R4 395/395/464 overflows — wait, /networth read 390 at 2.5s settle. Timing artifact — re-measure at 6s: 464. Confirmed.

SEO pair on the reference: robots + sitemap live; the head census captured (byte-identical strings later confirmed against the clone); the manifest endpoint 302s empty.

Now the clone side — parity server boot via with-server.sh, login, R1–R4 (all clean: direct svg hit, sheet closes on nav, Dashboard active + landmark, 390 everywhere), and the head census (byte-identical).

Now the session-61 suggested surfaces. #1 the donut's keyboard semantics — the surface/layer/sector census first.

**First drift found**: the clone's svg.recharts-surface has tabIndex=0 + role="application"; the reference has neither. And the tooltip's inner div carries role="status" + aria-live="assertive" on the clone; the reference's has no attributes. Both trace to recharts 3's accessibilityLayer defaulting ON.

Let me read the recharts 3 source (RootSurface) — the explicit tabIndex/role props win over the a11y defaults; accessibilityLayer={false} kills both. The Tooltip's DefaultTooltipContent reads the same flag.

Deeper: the reference's arrows DO rove sector focus (ArrowRight from the layer → g.recharts-pie-sector focused, Escape → BODY). recharts 3.10 has no such handlers. Let me install recharts 2.15.3 in a scratch dir and read its Pie source — found it: attachKeyboardHandlers sets pieRef.onkeydown with ArrowLeft ++wrap / ArrowRight --wrap (backwards!) / Escape blur+reset, and rootTabIndex: 0 on the layer (both versions — parity there). The reference's surface is inert because 2.15 only sets surface attrs with an explicit accessibilityLayer (which the reference doesn't set).

The arrow-walk re-verified on the reference with strict settles: layer.focus() holds; ArrowDown does nothing; ArrowRight → sector (the LAST one, per the --wrap quirk); Escape → BODY; no tooltips during the walk. The rings: both sites render the same default 5px auto near-black ring on the focused layer/sector.

#2 the filter selects' arrow semantics — open + arrows on both sites: identical Radix listbox roving with data-highlighted, no wrap. NO finding.

#3 the dialog forms' full Tab order — the strict census (tabindex property; the reference's 1×1 native-select shadows correctly excluded): the same 14-field sequence on both sites EXCEPT the reference's classification field has TWO stops (container + checked radio at tabindex=0). The clone's fresh state has all radios at −1. Fresh re-open re-verified on the reference (Escape + reopen, zero prior interactions) — checked=0 is real, not interaction contamination.

The tile arrow behavior: identical on both sites (entry focus on ArrowDown, automatic activation on arrows). A REAL Tab from Amount on the reference lands on the CHECKED RADIO (the container's entry focus forwards instantly — measured on both; activeElement never reads the container).

VLM pairs: dashboard + add-dialog captured and compared. All flags DOM-explained (superset #3 active-nav, seeded data, the Radix X-focus ring — computed arbitration confirms both X's byte-identical at rest).

Findings complete: G1 the donut keyboard trio, G2 the tiles' fresh roving. Let me write remediation-plan-v31.md, validate it against the codebase (no existing pins collide), then TDD.

G1 RED: the two donut tests written → both FAIL on the drifted implementation. GREEN: accessibilityLayer={false} + usePieKeyboardParity (an onkeydown DOM property on the donut wrapper — delegation via bubbling, immune to the ResponsiveContainer mount race). A typecheck fix on the test's evaluate typing. GREEN.

G2 RED: the tiles' fresh census test → FAIL (checked reads −1). GREEN: tabIndex={selected ? 0 : −1} on RadioGroupItem. The Tab-walk assertion initially expected the container — wrong: the entry focus forwards to the checked radio (measured on both sites). Fixed the test to assert the real contract. GREEN.

Pin-sanity: a11y prop removed → test 1 FAILs; the roving wrap mutated (+2) → test 2 FAILs; the tile prop flipped to −1 → test 3 FAILs. All restored → GREEN.

**Full chain: 108 unit · 164 e2e · 35 smoke + lint/typecheck/build.** Live re-verification on :3200: the surface census null/null, the tooltip attrs gone, the arrow walk byte-identical (layer → LAST sector → Escape → BODY), the tiles' fresh census container 0 + checked 0 + unchecked −1. The 16 screenshots regenerated (zero visual change).

Docs aligned: probe README (v31 catalog + lessons), README (v31 row + 164 counts), CLAUDE.md (e2e description), AGENTS.md (the v31 paragraph), SKILL (the session row + project_state), session_63.md, this narrative, the worklog.

**Parity iteration v31 shipped to main** — commit + SSH-wrapper push next.
