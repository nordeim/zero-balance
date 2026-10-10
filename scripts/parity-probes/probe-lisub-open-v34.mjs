(async () => {
  const addBtn = [...document.querySelectorAll('button')].find(b => /^Add (First )?Item$/i.test(b.textContent.trim()));
  if (!addBtn) return JSON.stringify({error: 'no add item button', overlayText: 'none'});
  addBtn.click();
  await new Promise(r => setTimeout(r, 1000));
  const overlays = [...document.querySelectorAll('div')].filter(d => {
    const c = (d.className || '').toString();
    const r = d.getBoundingClientRect();
    return c.includes('fixed') && c.includes('z-[60]') && r.width > 200;
  });
  const freqTrigger = [...document.querySelectorAll('button')].find(b =>
    /monthly|weekly|frequency/i.test(b.textContent) && b.closest('div[class*=z-6], div[class*=z-\\[60\\]'));
  return JSON.stringify({
    subDialogOpen: overlays.length > 0,
    subDialogH2: overlays[0]?.querySelector('h2')?.textContent,
    freqTriggerFound: !!freqTrigger,
    freqTriggerText: freqTrigger?.textContent?.trim().slice(0, 20),
  });
})()
