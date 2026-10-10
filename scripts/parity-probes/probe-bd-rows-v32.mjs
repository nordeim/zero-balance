// v32: the breakdown accordion's keyboard semantics — the section-row census
// + arrow/Home/End inertness (focus a row first, then REAL key presses; this
// probe only reads). The measured contract on BOTH sites: arrows/Home/End
// inert (focus never moves); Enter expands (focus stays); Escape does NOT
// collapse. The clone's rows carry aria-expanded (the kept superset); the
// reference's have none. Prereq: the dashboard open.
// bash scripts/parity-probes/run-probe.sh <session> probe-bd-rows-v32.mjs
(() => {
  const rows = [...document.querySelectorAll('button')].filter(b => /w-full/.test(b.className || '') && /cursor-pointer/.test(b.className || '') && /\$/.test(b.textContent));
  if (!rows.length) return 'no breakdown rows';
  const r = rows[0];
  const cs = getComputedStyle(r);
  return JSON.stringify({
    rowCount: rows.length,
    rows: rows.map(x => ({ tabindex: x.tabIndex, ariaExpanded: x.getAttribute('aria-expanded'), text: (x.textContent || '').replace(/\s+/g, ' ').slice(0, 30) })),
    chrome: { radius: cs.borderRadius, bg: cs.backgroundColor, cursor: cs.cursor },
    hint: 'focus rows[0] then press ArrowDown/ArrowUp/Home/End/Enter/Escape with agent-browser press; read document.activeElement + aria-expanded after each'
  });
})()
