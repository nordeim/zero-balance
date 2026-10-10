(async () => {
  const rg = document.querySelector('[role=radiogroup]');
  if (!rg) return 'no radiogroup';
  const radios = [...rg.querySelectorAll('[role=radio]')];
  const read = () => radios.map(r => ({ c: r.getAttribute('aria-checked') === 'true', tb: r.tabIndex }));
  // 1. focus the container (as a Tab would)
  rg.focus();
  await new Promise(r => setTimeout(r, 250));
  const afterFocusContainer = { active: document.activeElement === rg, radios: read() };
  // 2. ArrowDown from container
  rg.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowDown', bubbles: true, cancelable: true }));
  await new Promise(r => setTimeout(r, 300));
  const afterArrowDown1 = { activeIsRadio: radios.includes(document.activeElement), activeText: document.activeElement ? (document.activeElement.textContent || document.activeElement.parentElement.textContent || '').trim().slice(0, 12) : 'none', radios: read() };
  // 3. ArrowRight
  const el = document.activeElement;
  if (el) el.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true, cancelable: true }));
  await new Promise(r => setTimeout(r, 300));
  const afterArrowRight = { activeIsRadio: radios.includes(document.activeElement), activeText: document.activeElement ? (document.activeElement.textContent || document.activeElement.parentElement.textContent || '').trim().slice(0, 12) : 'none', radios: read() };
  return JSON.stringify({ afterFocusContainer, afterArrowDown1, afterArrowRight }, null, 1);
})()
