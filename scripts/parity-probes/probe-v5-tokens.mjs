// Session-8 (v5): read the site's own :root CSS custom properties (shadcn tokens).
(() => {
  const out = {};
  const cs = getComputedStyle(document.documentElement);
  const vars = ['--background', '--foreground', '--card', '--card-foreground', '--popover', '--popover-foreground',
    '--primary', '--primary-foreground', '--secondary', '--secondary-foreground', '--muted', '--muted-foreground',
    '--accent', '--accent-foreground', '--destructive', '--destructive-foreground', '--border', '--input', '--ring',
    '--sidebar', '--sidebar-foreground', '--sidebar-primary', '--sidebar-primary-foreground', '--sidebar-accent',
    '--sidebar-accent-foreground', '--sidebar-border', '--sidebar-ring', '--radius', '--forest-dark', '--forest-medium',
    '--lime-green', '--lime-light', '--orange-dark', '--orange-light', '--blue-dark', '--blue-medium', '--neutral-warm'];
  for (const v of vars) {
    const val = cs.getPropertyValue(v).trim();
    if (val) out[v] = val;
  }
  out.bodyColor = getComputedStyle(document.body).color;
  return JSON.stringify(out, null, 1);
})()
