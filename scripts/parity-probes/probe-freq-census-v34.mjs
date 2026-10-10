(async () => {
  const lb = document.querySelector('[role=listbox]');
  const opts = [...document.querySelectorAll('[role=option]')];
  const trigger = [...document.querySelectorAll('button[aria-expanded]')].find(b => /Monthly|Weekly|Yearly|One-time/i.test(b.textContent));
  return JSON.stringify({
    options: opts.map(o => o.textContent.trim()),
    listboxAria: lb ? { id: lb.id, labelledby: lb.getAttribute('aria-labelledby'), activedesc: lb.getAttribute('aria-activedescendant') } : null,
    triggerAria: trigger ? { expanded: trigger.getAttribute('aria-expanded'), haspopup: trigger.getAttribute('aria-haspopup'), controls: trigger.getAttribute('aria-controls'), role: trigger.getAttribute('role') } : null,
  });
})()
