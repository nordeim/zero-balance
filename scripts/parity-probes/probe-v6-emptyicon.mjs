(() => {
  const h = [...document.querySelectorAll('h3, h4')].find((e) => /No (savings|expense) items yet/i.test(e.textContent || ''));
  if (!h) return JSON.stringify({ err: 'none' });
  const svg = [...h.parentElement.querySelectorAll('svg')].find((s) => !s.closest('button'));
  const p = h.parentElement.querySelector('p');
  return JSON.stringify({ icon: svg?.getAttribute('class'), descSize: p ? getComputedStyle(p).fontSize : null, hmb: getComputedStyle(h).marginBottom });
})()
