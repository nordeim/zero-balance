(async () => {
  // v47: the dialog input's FOCUS-state shadow composition census — the
  // session-101 queue's second item, measured on BOTH sites (the Add-Item
  // dialog's first input). The clone's shadcn stack composes the
  // reference's two VISIBLE layers exactly (the 1px #0a0a0a ring + the
  // shadow-sm layer); the LEAD layers diverge by construction (v4's
  // 5-slot vs v3's 3-slot — the accepted v10/v25/v45 class).
  // On the CLONE: the dialog is a Radix [role=dialog] portal.
  const dlg = document.querySelector('[role="dialog"]');
  if (!dlg) return "no dialog";
  const input = dlg.querySelector("input");
  if (!input) return "no input";
  const cs = getComputedStyle(input);
  const layerCount = (s) => (s.match(/px, /g) || []).length + 1;

  // REST census first.
  const rest = {
    h: cs.height,
    radius: cs.borderRadius,
    pad: cs.padding,
    border: `${cs.borderWidth} ${cs.borderColor}`,
    bg: cs.backgroundColor,
    shadow: cs.boxShadow,
    layers: layerCount(cs.boxShadow),
    outlineStyle: cs.outlineStyle,
  };

  // REAL focus with the visible heuristic (the v35 idiom).
  input.focus({ focusVisible: true });
  await new Promise((r) => setTimeout(r, 100));
  const fcs = getComputedStyle(input);
  const focus = {
    fv: input.matches(":focus-visible"),
    shadow: fcs.boxShadow,
    layers: layerCount(fcs.boxShadow),
    borderColor: fcs.borderColor,
    outlineStyle: fcs.outlineStyle,
  };

  input.blur();
  return JSON.stringify({ rest, focus });
})()
