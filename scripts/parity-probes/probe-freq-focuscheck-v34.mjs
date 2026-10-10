(async () => {
  const hasFocusBefore = document.hasFocus();
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
  return JSON.stringify({
    hasFocusBefore,
    hasFocusNow: document.hasFocus(),
    monthlyMatchesFocus: monthly.matches(':focus'),
    monthlyBg: getComputedStyle(monthly).backgroundColor,
    monthlyColor: getComputedStyle(monthly).color,
    activeIsMonthly: document.activeElement === monthly,
  });
})()
