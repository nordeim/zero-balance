// Locate Spending Breakdown card, legend rows, sectors, guidelines cards, quick-action buttons
(() => {
  const out = {};
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let node;
  while ((node = walker.nextNode())) {
    if ((node.textContent || '').trim() === 'Spending Breakdown') {
      out.found = node.parentElement?.tagName + '.' + (node.parentElement?.className || '').slice(0, 60);
      let card = node.parentElement;
      for (let i = 0; i < 6 && card; i++) {
        card = card.parentElement;
        if (card && /rounded-2xl/.test(card.className || '')) break;
      }
      out.card = card?.outerHTML.replace(/\s+/g, ' ').slice(0, 4000) || null;
      break;
    }
  }
  const glWalker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while ((node = glWalker.nextNode())) {
    if ((node.textContent || '').trim() === 'Budget Guidelines') {
      let card = node.parentElement;
      for (let i = 0; i < 6 && card; i++) {
        card = card.parentElement;
        if (card && /rounded-2xl/.test(card.className || '')) break;
      }
      out.guidelines = card?.outerHTML.replace(/\s+/g, ' ').slice(0, 3000) || null;
      break;
    }
  }
  const qaBtns = [...document.querySelectorAll('button')].filter((b) => /^Add (Income|Savings|Expense)$/.test((b.textContent || '').trim()));
  out.quickActions = qaBtns.map((b) => b.outerHTML.replace(/\s+/g, ' ').slice(0, 1400));
  out.sectors = [...document.querySelectorAll('.recharts-sector')].map((s) => s.getAttribute('fill'));
  return out;
})()
