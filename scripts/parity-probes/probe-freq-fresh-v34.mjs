(async () => {
  // self-contained: calculator -> sub-dialog -> fresh-open freq listbox -> visual census
  const calcBtn = [...document.querySelectorAll('button')].find(b => /^Calculate$/i.test(b.textContent.trim()));
  if (!calcBtn) return JSON.stringify({error: 'no calculate button'});
  calcBtn.click();
  await new Promise(r => setTimeout(r, 900));
  const calcDialog = [...document.querySelectorAll('[role=dialog], [data-state=open]')].filter(d => d.textContent?.includes('Calculator'));
  if (!calcDialog.length) return JSON.stringify({error: 'calculator not open'});
  const addBtn = [...calcDialog[0].querySelectorAll('button')].find(b => /^Add (First )?Item$/i.test(b.textContent.trim()));
  if (!addBtn) return JSON.stringify({error: 'no add item'});
  addBtn.click();
  await new Promise(r => setTimeout(r, 900));
  const subDialog = [...document.querySelectorAll('[role=dialog], [data-state=open]')].filter(d => d.querySelector('h2') && /Line Item/i.test(d.querySelector('h2').textContent));
  if (!subDialog.length) return JSON.stringify({error: 'sub-dialog not open'});
  const freq = [...subDialog[0].querySelectorAll('button')].find(b => /^(One-time|Weekly|Bi-weekly|Monthly|Quarterly|Annually)$/i.test(b.textContent.trim()));
  if (!freq) return JSON.stringify({error: 'no freq trigger'});
  freq.click();
  await new Promise(r => setTimeout(r, 600));
  const opts = [...document.querySelectorAll('[role=option]')];
  return JSON.stringify({
    options: opts.map((o, i) => {
      const st = getComputedStyle(o);
      return { i, t: o.textContent.trim().slice(0, 10), bg: st.backgroundColor, color: st.color, focused: document.activeElement === o, dh: o.getAttribute('data-highlighted') !== null };
    }),
    activeEl: (document.activeElement?.textContent || '').trim().slice(0, 12) + ':' + document.activeElement?.getAttribute?.('role'),
    contentBg: getComputedStyle(document.querySelector('[role=listbox]')).backgroundColor,
  });
})()
