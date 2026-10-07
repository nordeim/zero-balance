(() => {
  const h = [...document.querySelectorAll('h2')].find((e) => /(Add|Edit) /.test(e.textContent || '') && /Budget Item|Expense|Income|Line Item|Asset|Liability/i.test(e.textContent || ''));
  return JSON.stringify({ title: h?.textContent?.trim() || null });
})()
