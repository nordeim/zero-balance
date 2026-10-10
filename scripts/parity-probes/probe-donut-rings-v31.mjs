(async () => {
  const layer = document.querySelector('g.recharts-layer.recharts-pie, .recharts-pie');
  if (!layer) return 'no layer';
  await new Promise(r => setTimeout(r, 1500));
  layer.focus();
  await new Promise(r => setTimeout(r, 350));
  const lcs = getComputedStyle(layer);
  const layerRing = { outline: lcs.outline, outlineStyle: lcs.outlineStyle, outlineWidth: lcs.outlineWidth, outlineColor: lcs.outlineColor };
  // arrow to a sector
  layer.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true, cancelable: true }));
  await new Promise(r => setTimeout(r, 450));
  const sector = document.activeElement;
  const scs = sector && sector.classList && sector.classList.contains('recharts-pie-sector') ? getComputedStyle(sector) : null;
  const svg = document.querySelector('.recharts-surface');
  return JSON.stringify({
    layerRing,
    sectorFocused: !!scs,
    sectorRing: scs ? { outline: scs.outline, outlineStyle: scs.outlineStyle, outlineWidth: scs.outlineWidth, outlineColor: scs.outlineColor } : null,
    surfaceTabIndexAttr: svg ? svg.getAttribute('tabindex') : null,
    surfaceRole: svg ? svg.getAttribute('role') : null
  }, null, 1);
})()
