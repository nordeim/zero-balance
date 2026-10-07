(() => {
  const panel = document.querySelector('[role="tabpanel"][data-state="active"]') || document;
  const card = [...panel.querySelectorAll('div')].filter((d) => /hover:shadow-lg/.test(d.className)).sort((a, b) => a.querySelectorAll('div').length - b.querySelectorAll('div').length)[0];
  if (!card) return JSON.stringify({ err: 'no card' });
  const b = card.querySelector('button');
  const matches = (sel) => { try { return b.matches(sel); } catch { return 'err'; } };
  return JSON.stringify({
    btnClasses: b.className,
    cardHover: matches(':hover') === true ? true : matches(':hover'),
    btnHover: (() => { try { return b.matches(':hover'); } catch { return 'err'; } })(),
    outerHTML: b.outerHTML.slice(0, 400),
  }, null, 1);
})()
