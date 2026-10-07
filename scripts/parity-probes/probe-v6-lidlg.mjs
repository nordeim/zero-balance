(() => {
  const h = [...document.querySelectorAll('h2')].find((e) => /Add Line Item|Edit Line Item/.test(e.textContent || ''));
  if (!h) return JSON.stringify({ err: 'no li dialog' });
  let panel = h;
  while (panel.parentElement && !/rounded-2xl/.test(panel.className || '')) panel = panel.parentElement;
  const labels = [...panel.querySelectorAll('label')].map((l) => (l.textContent || '').replace(/\s+/g, ' ').trim()).filter(Boolean);
  const phs = [...panel.querySelectorAll('input, textarea')].map((i) => ({ ph: i.getAttribute('placeholder'), value: (i.value || '').slice(0, 14), type: i.getAttribute('type') }));
  return JSON.stringify({ title: (h.textContent || '').trim(), labels, phs }, null, 1);
})()
