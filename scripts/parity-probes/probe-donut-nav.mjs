// Precise probe: donut percentage label location + visible active nav link.
(() => {
  const out = {};
  const cs = (el, prop) => (el ? getComputedStyle(el)[prop] : null);
  const vis = (el) => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0 && cs(el, 'visibility') !== 'hidden'; };

  // --- Donut: where do the standalone percentages live? ---
  // find first percentage text node that is NOT inside a legend row
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n; const pctEls = [];
  while ((n = walker.nextNode())) {
    const t = (n.textContent || '').trim();
    if (/^\d{1,2}\.\d%$/.test(t)) pctEls.push(n.parentElement);
  }
  out.pctCount = pctEls.length;
  if (pctEls.length) {
    const first = pctEls[0];
    // climb to a notable ancestor
    let anc = first; const chain = [];
    for (let i = 0; i < 12 && anc && anc !== document.body; i++) {
      chain.push(`${anc.tagName}.${(anc.className || '').toString().slice(0, 48)}`);
      anc = anc.parentElement;
    }
    out.pctAncestry = chain;
    out.pctFirst = { text: first.textContent.trim(), fontSize: cs(first, 'fontSize'), color: cs(first, 'color'), cls: (first.className || '').toString().slice(0, 60) };
    // is it inside the recharts surface?
    const inPie = !!first.closest('.recharts-surface, .recharts-wrapper, svg');
    out.pctInsideChart = inPie;
    // its position relative to the svg
    const svg = document.querySelector('.recharts-surface');
    if (svg) { const sr = svg.getBoundingClientRect(); const fr = first.getBoundingClientRect(); out.pctPos = { svg: [sr.x | 0, sr.y | 0, sr.width | 0, sr.height | 0], first: [fr.x | 0, fr.y | 0, fr.width | 0, fr.height | 0] }; }
  }

  // --- Nav: all Dashboard links, which is visible, computed active style ---
  out.dashLinks = [...document.querySelectorAll('a, button')].filter((x) => (x.textContent || '').trim() === 'Dashboard').map((x) => {
    const r = x.getBoundingClientRect();
    return {
      tag: x.tagName, visible: vis(x), rect: [r.x | 0, r.y | 0, r.width | 0, r.height | 0],
      bg: cs(x, 'backgroundImage') !== 'none' ? cs(x, 'backgroundImage').slice(0, 90) : cs(x, 'backgroundColor'),
      color: cs(x, 'color'), weight: cs(x, 'fontWeight'), cls: (x.className || '').toString().slice(0, 110),
      parentCls: (x.parentElement?.className || '').toString().slice(0, 60),
      // check children for gradient chips
      childBg: (() => { const c = x.querySelector(':scope > *'); return c ? (cs(c, 'backgroundImage') !== 'none' ? cs(c, 'backgroundImage').slice(0, 90) : cs(c, 'backgroundColor')) : null; })(),
    };
  });

  // --- Sidebar container: which sidebar is visible (rail vs expanded vs mobile)? ---
  out.sidebars = [...document.querySelectorAll('aside, nav')].map((a) => { const r = a.getBoundingClientRect(); return { tag: a.tagName, visible: r.width > 0 && r.height > 0, rect: [r.x | 0, r.y | 0, r.width | 0, r.height | 0], cls: (a.className || '').toString().slice(0, 60), text: (a.textContent || '').replace(/\s+/g, ' ').slice(0, 60) }; }).filter((s) => s.visible);

  return JSON.stringify(out, null, 1);
})()
