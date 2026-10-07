// Session-7: nav link hover states — measure :hover computed bg on both sites.
(async () => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

  const links = [...document.querySelectorAll('a')].filter((a) => /^(Dashboard|Income|Expenses|Savings|Net Worth)$/.test(txt(a) || ''));

  // CSS var bg-sidebar-accent value
  out.sidebarAccent = getComputedStyle(document.documentElement).getPropertyValue('--sidebar-accent') || null;
  out.sidebarBg = getComputedStyle(document.documentElement).getPropertyValue('--sidebar') || null;

  // hover the INACTIVE "Income" link
  const income = links.find((a) => txt(a) === 'Income');
  if (income) {
    out.inactiveCls = income.className.toString();
    income.scrollIntoView({ block: 'center' });
    const r = income.getBoundingClientRect();
    const evt = new MouseEvent('mousemove', { bubbles: true, clientX: r.x + r.width / 2, clientY: r.y + r.height / 2 });
    income.dispatchEvent(evt);
    await sleep(400);
    out.inactiveHoverBg = cs(income, 'backgroundColor');
    out.inactiveHoverColor = cs(income, 'color');
  }

  // hover the ACTIVE "Dashboard" link
  const dash = links.find((a) => txt(a) === 'Dashboard');
  if (dash) {
    const r = dash.getBoundingClientRect();
    const evt = new MouseEvent('mousemove', { bubbles: true, clientX: r.x + r.width / 2, clientY: r.y + r.height / 2 });
    dash.dispatchEvent(evt);
    await sleep(400);
    out.activeHoverBgImg = cs(dash, 'backgroundImage').slice(0, 80);
    out.activeHoverOpacity = cs(dash, 'opacity');
  }

  return JSON.stringify(out, null, 1);
})()
