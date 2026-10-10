(async () => {
  // Radix-aware: open the calculator, then the sub-dialog, then the
  // frequency select — anchored via [role=dialog] / [data-state=open].
  const calcBtn = [...document.querySelectorAll('button')].find(b => /^Calculate$/i.test(b.textContent.trim()));
  if (!calcBtn) return JSON.stringify({error: 'no calculate button'});
  calcBtn.click();
  await new Promise(r => setTimeout(r, 900));
  const dialogs = [...document.querySelectorAll('[role=dialog], [data-state=open]')].filter(d => d.textContent?.includes('Calculator'));
  if (!dialogs.length) return JSON.stringify({error: 'calculator dialog not open'});
  const addBtn = [...dialogs[0].querySelectorAll('button')].find(b => /^Add (First )?Item$/i.test(b.textContent.trim()));
  if (!addBtn) return JSON.stringify({error: 'no add item button in calculator', calcText: dialogs[0].innerText.split('\n').slice(0, 5)});
  addBtn.click();
  await new Promise(r => setTimeout(r, 900));
  const subDialogs = [...document.querySelectorAll('[role=dialog], [data-state=open]')].filter(d => d.textContent?.includes('Add Line Item') || /Line Item/i.test(d.querySelector('h2')?.textContent || ''));
  const freq = subDialogs.length ? [...subDialogs[0].querySelectorAll('button[role=combobox], button')].find(b => /One-time|Weekly|Bi-weekly|Monthly|Quarterly|Annually/.test(b.textContent)) : null;
  if (!freq) return JSON.stringify({error: 'no freq trigger', subDialogCount: subDialogs.length});
  freq.click();
  await new Promise(r => setTimeout(r, 600));
  const opts = [...document.querySelectorAll('[role=option]')];
  return JSON.stringify({
    subDialogOpen: subDialogs.length > 0,
    freqTrigger: freq.textContent.trim(),
    listboxOpen: document.querySelectorAll('[role=listbox]').length,
    options: opts.map(o => o.textContent.trim()),
    hlOnOpen: opts.findIndex(o => o.getAttribute('data-highlighted') !== null),
    triggerRole: freq.getAttribute('role'),
    ariaExpanded: freq.getAttribute('aria-expanded'),
  });
})()
