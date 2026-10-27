#!/usr/bin/env python3
"""compare-v130-census.py — the AXIS-BY-AXIS comparison of the v130 two-half
census (the v124-era NETWORTH + DRILL-DOWN pair's ELEVENTH re-run).

Parses the drill-down + networth summary-card census JSON lines from the two
halves' full logs (/tmp/vlm130/ref-census.log + clone-census.log), flattens
every axis, and compares ref vs clone axis-by-axis. Deltas are classified
against the DOCUMENTED-CLASS whitelist; any axis that differs WITHOUT a
documented class is a NEW CLONE GAP and fails the run.

Documented classes for this pair (the v118/v124 records):
  - navHighlight.color + navHighlight.fw — the v56 SUPERSET delta: the
    clone highlights its ACTIVE nav item (white/500 text state) while the
    reference's Dashboard link renders its un-highlighted zinc-600/400
    state (the reference's own nav-highlight shortcoming; the superset
    fix documented since v56 — bg transparent BOTH sides, radius 8px
    identical).
  - avatarLetter — the USER-IDENTITY data class (the reference account's
    'U' vs the clone demo account's 'D').
  - progress.fillW — the PCT data class (fillW 173-vs-357: the budget
    allocation percentages are seed-data derived; track/gradient
    byte-identical).
  - donutLabels.texts — the EACH-SITE'S-DATA class (the label percentages
    are seed-data derived: ref 92.3/4.6/3.1 vs clone 81.6/13.8/4.6; count
    4 / labelLineCount 0 / labelFs 16px / labelFill black / sectors 3
    byte-identical).
  - labelBlock.w — the v82 DATA-CONDITIONAL width class (the 48px
    figure's text length: ref "$25,000.00" 304px vs clone
    "-$245,950.00" 357px; the block's other axes byte-identical).
Everything else must be byte-identical.
"""
import json, sys

def load_censuses(path):
    """Extract the drill + networth census dicts from a half's full log.

    The census lines are DOUBLE-ESCAPED: agent-browser's eval prints the
    JSON object itself serialized as a quoted string (structural quotes
    escaped once, nested quotes inside values like glyphSig twice), so the
    recovery is a DOUBLE json.loads — the outer parse unescapes the string
    literal, the inner parse decodes the census object.
    """
    drill = networth = None
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not (line.startswith('"{') and line.endswith('}"')):
            continue
        try:
            inner = json.loads(line)
            d = json.loads(inner)
        except (json.JSONDecodeError, ValueError):
            continue
        if not isinstance(d, dict):
            continue
        if d.get('view') == 'drill-arbit-1280-v130':
            drill = d
        elif d.get('view') == 'nw-height-1280-v130':
            networth = d
    return drill, networth

def flatten(obj, prefix=""):
    """Flatten nested dicts into {dotted.path: value} axes."""
    out = {}
    for k, v in obj.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            out.update(flatten(v, key))
        else:
            out[key] = v
    return out

# axis -> documented class (ref value, clone value tolerated)
DOCUMENTED = {
    "navHighlight.color":
        "v56 SUPERSET delta (the clone highlights its ACTIVE nav item "
        "[white text]; the reference's Dashboard link renders its "
        "un-highlighted zinc-600 state — the reference's own nav-highlight "
        "shortcoming, the superset fix documented since v56)",
    "navHighlight.fw":
        "v56 SUPERSET delta (the clone's active-nav 500 weight vs the "
        "reference's un-highlighted 400 — same superset class)",
    "avatarLetter":
        "USER-IDENTITY data class (the reference account's 'U' vs the clone "
        "demo account's 'D')",
    "progress.fillW":
        "PCT data class (fillW 173-vs-357: the budget allocation percentages "
        "are seed-data derived; track/gradient byte-identical)",
    "donutLabels.texts":
        "EACH-SITE'S-DATA class (the label percentages are seed-data derived: "
        "ref 92.3/4.6/3.1 vs clone 81.6/13.8/4.6; count 4 / labelLineCount 0 / "
        "labelFs 16px / labelFill black / sectors 3 byte-identical)",
    "labelBlock.w":
        "v82 DATA-CONDITIONAL width class (the 48px figure's text length: ref "
        "'$25,000.00' 304px vs clone '-$245,950.00' 357px; the block's other "
        "axes byte-identical)",
}

ref_drill, ref_networth = load_censuses("/tmp/vlm130/ref-census.log")
clone_drill, clone_networth = load_censuses("/tmp/vlm130/clone-census.log")
if not (ref_drill and ref_networth and clone_drill and clone_networth):
    print("FAIL: could not extract all four censuses from the logs")
    sys.exit(1)

def compare(name, ref, clone):
    rf, cf = flatten(ref), flatten(clone)
    axes = sorted(set(rf) | set(cf))
    identical = documented = new = 0
    print(f"\n===== {name}: {len(axes)} axes =====")
    for axis in axes:
        rv, cv = rf.get(axis, "<absent>"), cf.get(axis, "<absent>")
        if rv == cv:
            identical += 1
            continue
        if axis in DOCUMENTED:
            documented += 1
            print(f"  DOCUMENTED {axis}: ref {rv!r} vs clone {cv!r} — {DOCUMENTED[axis]}")
        else:
            new += 1
            print(f"  ** NEW DELTA {axis}: ref {rv!r} vs clone {cv!r} **")
    return identical, documented, new


di, dd, dn = compare("DRILL-DOWN census (PART A)", ref_drill, clone_drill)
ni, nd, nn = compare("NETWORTH summary-card census (PART B)", ref_networth, clone_networth)

ti, td, tn = di + ni, dd + nd, dn + nn
print(f"\n===== TOTAL: {ti + td + tn} axes: {ti} identical + {td} documented-class deltas, {tn} NEW =====")
sys.exit(1 if tn else 0)
