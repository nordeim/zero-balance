(async () => {
  const freqTrigger = [...document.querySelectorAll('button')].find(b => /^Monthly$/i.test(b.textContent.trim()) && b.closest('div[class*=fixed]'));
  if (!freqTrigger) return JSON.stringify({error: 'no freq trigger (sub-dialog closed?)'});
  freqTrigger.click();
  await new Promise(r => setTimeout(r, 500));
  return JSON.stringify({ reopened: !!document.querySelector('[role=listbox]'), hl: [...document.querySelectorAll('[role=option]')].findIndex(o => o.getAttribute('data-highlighted') !== null) });
})()
