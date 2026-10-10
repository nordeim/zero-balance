(async () => {
  const readHL = () => {
    const opts = [...document.querySelectorAll('[role=listbox] [role=option]')];
    return opts.map(o => ({ t: o.textContent.trim().slice(0, 16), hl: o.getAttribute('data-highlighted') !== null }));
  };
  const step = async (key) => {
    document.activeElement.dispatchEvent(new KeyboardEvent('keydown', { key, bubbles: true, cancelable: true }));
    await new Promise(r => setTimeout(r, 250));
    return readHL();
  };
  const before = readHL();
  const afterDown = await step('ArrowDown');
  const afterDown2 = await step('ArrowDown');
  const afterUp = await step('ArrowUp');
  return JSON.stringify({ before, afterDown, afterDown2, afterUp });
})()
