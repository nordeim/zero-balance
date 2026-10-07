(() => {
  const dlg = document.querySelector('[role="dialog"]');
  if (!dlg) return JSON.stringify({ err: 'no dialog' });
  const sw = dlg.querySelector('[role="switch"]');
  const p = [...dlg.querySelectorAll('p')].map((p) => (p.textContent || '').trim()).filter((t) => /repeat/i.test(t));
  const label = sw ? sw.parentElement.textContent : null;
  const cs = sw ? getComputedStyle(sw) : null;
  return JSON.stringify({ switchState: sw?.getAttribute('aria-checked'), label: (label || '').trim().slice(0, 40), desc: p, w: cs?.width, h: cs?.height }, null, 1);
})()
