(async () => {
  const calcBtn = [...document.querySelectorAll('button')].find(b => /^Calculate$/i.test(b.textContent.trim()));
  calcBtn.click();
  await new Promise(r => setTimeout(r, 900));
  const addBtn = [...document.querySelectorAll('[role=dialog] button')].find(b => /^Add (First )?Item$/i.test(b.textContent.trim()));
  addBtn.click();
  await new Promise(r => setTimeout(r, 900));
  const subDialog = [...document.querySelectorAll('[role=dialog]')].filter(d => d.querySelector('h2') && /Line Item/i.test(d.querySelector('h2').textContent));
  const freq = [...subDialog[0].querySelectorAll('button')].find(b => /^(One-time|Weekly|Bi-weekly|Monthly|Quarterly|Annually)$/i.test(b.textContent.trim()));
  freq.click();
  await new Promise(r => setTimeout(r, 800));
  const opts = [...document.querySelectorAll('[role=option]')];
  const monthly = opts[3];
  const lb = document.querySelector('[role=listbox]');
  const focusInDoc = document.querySelector(':focus');
  const focusInLb = lb ? lb.querySelector(':focus') : null;
  const focusIsLbItself = lb ? lb.matches(':focus') : false;
  return JSON.stringify({
    monthlyMatchesFocus: monthly.matches(':focus'),
    activeIsMonthly: document.activeElement === monthly,
    docFocusIs: focusInDoc ? focusInDoc.tagName + ':' + (focusInDoc.getAttribute('role') || focusInDoc.textContent.trim().slice(0, 12)) : 'none',
    lbMatchesFocus: focusIsLbItself,
    focusInLbIs: focusInLb ? focusInLb.tagName + ':' + (focusInLb.getAttribute('role') || focusInLb.textContent.trim().slice(0, 12)) : 'none',
    monthlyBg: getComputedStyle(monthly).backgroundColor,
    optsWithDh: opts.map((o, i) => (o.getAttribute('data-highlighted') !== null ? i : -1)).filter(i => i >= 0),
  });
})()
