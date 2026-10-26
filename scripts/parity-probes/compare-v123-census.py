#!/usr/bin/env python3
"""compare-v123-census.py — the AXIS-BY-AXIS comparison of the v123 two-half
census (the v117-era LOGIN + CALCULATOR pair's TENTH re-run).

Parses the login + calculator census JSON lines from the two halves' full
logs (/tmp/vlm123/ref-arbit-full.log + clone-arbit-full.log), flattens every
axis, and compares ref vs clone axis-by-axis. Deltas are classified against
the DOCUMENTED-CLASS whitelist; any axis that differs WITHOUT a documented
class is a NEW CLONE GAP and fails the run.

Documented classes for this pair (the v105/v111/v117 records + the v45/v10
construct conventions):
  - calc totalCard.hasWillUpdateSpan (ref false vs clone true) — the SEED-DATA
    class: the reference's OWN Rent is $25.00, its calculated total EQUALS
    the saved amount so the note stays hidden; the clone's Rent $1850 vs the
    recalculated $25.00 shows the note. DATA-CONDITIONAL chrome, the totalCard
    box byte-identical.
  - the `close` key + its sub-axes present on the CLONE side only — the
    v99-documented FINDER ARTIFACT: the reference's close button matches
    neither the aria-label nor the x-text pattern the census finder uses;
    the v87 pin holds the close-button chrome via its own geometric finder,
    byte-identical.
  - card.shadow (login) + panel.shadow (calc) — the v3/v4 CONSTRUCT
    zero-layer-lead-count class (the v45 sweep + the v10 accepted-leads
    convention: v4's transparent composition leads paint nothing; the
    VISIBLE layer is the contract — held by the v45 F4 pin via toContain).
  - card.border (login) — the ZERO-WIDTH computed-color artifact: ref
    '0px rgb(229, 231, 235)' (the Tailwind v3 base default gray-200) vs
    clone '0px rgb(229, 231, 227)' (the app's measured --color-border
    token): border-width 0 on BOTH sides, nothing renders — the same
    accepted-construct convention (constructs that paint nothing are not
    parity axes); the card's pinned axes {w 448 / radius 16px / bg} are
    byte-identical, the card line exactly as pinned in v7.
Everything else must be byte-identical.
"""
import json, sys

def load_censuses(path):
    """Extract the login + calc census dicts from a half's full log."""
    login = calc = None
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not (line.startswith('"{') and line.endswith('}"')):
            continue
        raw = line[1:-1].replace('\\"', '"')
        try:
            d = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if 'view' in d and d.get('view') == 'login':
            login = d
        elif 'panel' in d:
            calc = d
    return login, calc

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
    "totalCard.hasWillUpdateSpan":
        "SEED-DATA class (ref Rent $25.00 == calculated total so the note hides; "
        "clone Rent $1850 vs recalculated $25.00 shows it — DATA-CONDITIONAL, "
        "the totalCard box byte-identical)",
    "card.shadow":
        "v3/v4 CONSTRUCT zero-layer-lead-count class (the v45 sweep + the v10 "
        "accepted-leads convention: transparent leads paint nothing; the "
        "VISIBLE layer rgba(0,0,0,0.25) 0px 25px 50px -12px is the contract — "
        "held by the v45 F4 pin via toContain)",
    "panel.shadow":
        "v3/v4 CONSTRUCT zero-layer-lead-count class (the clone emits the "
        "visible layer alone; the reference leads with two transparent layers "
        "— the accepted-leads convention, the visible layer the contract)",
    "card.border":
        "ZERO-WIDTH computed-color artifact (ref 0px + the v3 base default "
        "gray-200 vs clone 0px + the app's measured --color-border token; "
        "border-width 0 BOTH sides, nothing renders — the accepted-construct "
        "convention; the card's pinned axes w/radius/bg byte-identical, the "
        "card line exactly as pinned in v7)",
}

# the close.* family: the asymmetric-key FINDER ARTIFACT — every sub-axis of
# a key that exists on ONE side only inherits the artifact class (the v87
# pin is the close-button chrome authority, byte-identical via its own
# geometric finder)
CLOSE_ARTIFACT = (
    "the v99 FINDER ARTIFACT (the reference's close button matches neither "
    "the aria-label nor the x-text pattern the census finder uses; the v87 "
    "pin holds the close-button chrome via its own geometric finder, "
    "byte-identical)"
)

ref_login, ref_calc = load_censuses("/tmp/vlm123/ref-arbit-full.log")
clone_login, clone_calc = load_censuses("/tmp/vlm123/clone-arbit-full.log")
if not (ref_login and ref_calc and clone_login and clone_calc):
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
        elif axis == "close" or axis.startswith("close."):
            documented += 1
            print(f"  DOCUMENTED {axis}: ref {rv!r} vs clone {cv!r} — {CLOSE_ARTIFACT}")
        else:
            new += 1
            print(f"  ** NEW DELTA {axis}: ref {rv!r} vs clone {cv!r} **")
    return identical, documented, new


li, ld, ln = compare("LOGIN census", ref_login, clone_login)
ci, cd, cn = compare("CALC census", ref_calc, clone_calc)

# the close-key asymmetry direction check (the artifact must stay ONE-SIDED:
# present on the clone only — if the reference's button ever starts matching
# the finder, the artifact class changes and must be re-inspected)
if "close" in (clone_calc or {}) and "close" not in (ref_calc or {}):
    print("\nclose-key asymmetry: clone-only present — the documented v99 "
          "artifact direction HOLDS")
elif "close" in (ref_calc or {}) or "close" in (clone_calc or {}):
    print("\n** close-key asymmetry CHANGED from the documented form — inspect **")
    cn += 1

ti, td, tn = li + ci, ld + cd, ln + cn
print(f"\n===== TOTAL: {ti + td + tn} axes: {ti} identical + {td} documented-class deltas, {tn} NEW =====")
sys.exit(1 if tn else 0)
