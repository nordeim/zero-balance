(async () => {
  const sector = document.querySelector('.recharts-pie-sector');
  if (!sector) return 'no sector';
  sector.scrollIntoView({ block: 'center' });
  const r = sector.getBoundingClientRect();
  const cx = Math.round(r.x + r.width / 2), cy = Math.round(r.y + r.height / 2);
  sector.dispatchEvent(new PointerEvent('pointermove', { bubbles: true, clientX: cx, clientY: cy }));
  sector.dispatchEvent(new MouseEvent('mousemove', { bubbles: true, clientX: cx, clientY: cy }));
  sector.dispatchEvent(new MouseEvent('mouseover', { bubbles: true, clientX: cx, clientY: cy }));
  await new Promise(res => setTimeout(res, 600));
  const tip = document.querySelector('.recharts-tooltip-wrapper');
  if (!tip) return 'no tooltip appeared';
  const inner = tip.firstElementChild;
  const deep = inner ? inner.firstElementChild : null;
  const attrDump = (el) => {
    if (!el) return null;
    const attrs = {};
    for (const a of el.attributes) { if (!/^class$|^style$/.test(a.name)) attrs[a.name] = a.value; }
    return { tag: el.tagName, attrs, cls: (el.getAttribute('class') || '').slice(0, 60) };
  };
  return JSON.stringify({
    wrapper: attrDump(tip),
    inner: attrDump(inner),
    deep: attrDump(deep),
    tipText: tip.textContent.replace(/\n+/g, '|').slice(0, 80)
  }, null, 1);
})()
