(async () => {
  const a = document.activeElement;
  const st = getComputedStyle(a);
  return JSON.stringify({
    stop: a.tagName + ':' + (a.name || a.textContent.trim().slice(0, 12)),
    shadow: st.boxShadow,
    outline: st.outlineStyle + ' ' + st.outlineWidth + ' ' + st.outlineColor,
    borderColor: st.borderColor,
  });
})()
