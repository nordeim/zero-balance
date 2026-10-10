(async () => {
  // find the filter card selects on the items view
  const buttons = [...document.querySelectorAll('button')];
  const trigger = buttons.find(b => /all categories/i.test(b.textContent) || (/category/i.test(b.textContent) && b.getAttribute('aria-haspopup') === 'listbox'));
  if (!trigger) {
    const listboxTriggers = buttons.filter(b => b.getAttribute('aria-haspopup'));
    return JSON.stringify({ found: false, haspopupCount: listboxTriggers.length, firstThree: listboxTriggers.slice(0,3).map(b => b.textContent.trim().slice(0, 25)) });
  }
  const trigInfo = { text: trigger.textContent.trim().slice(0, 30), role: trigger.getAttribute('role'), expanded: trigger.getAttribute('aria-expanded') };
  trigger.click();
  await new Promise(r => setTimeout(r, 700));
  const list = document.querySelector('[role=listbox]');
  const opts = list ? [...list.querySelectorAll('[role=option]')].map(o => ({
    text: o.textContent.trim().slice(0, 20),
    highlighted: o.getAttribute('data-highlighted') !== null || o.getAttribute('aria-selected') === 'true' || (getComputedStyle(o).backgroundColor !== 'rgba(0, 0, 0, 0)')
  })) : null;
  return JSON.stringify({
    trigger: trigInfo,
    listOpen: !!list,
    listRole: list ? list.getAttribute('role') : null,
    listTag: list ? list.tagName : null,
    options: opts ? opts.slice(0, 10) : null,
    activeElement: document.activeElement ? document.activeElement.tagName + '.' + (document.activeElement.getAttribute('role') || '') : null
  }, null, 1);
})()
