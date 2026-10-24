#!/usr/bin/env python3
"""De-duplicate the v113 alignment edits (the align-docs-v113.py re-run
duplicated the idempotent-unsafe inserts: CLAUDE's clause, README's plan
row, SKILL's Session 148 row, PAD's v1.1.70 block — each inserted twice).
Keep the FIRST occurrence, drop the SECOND (byte-identical copies)."""

def dedup(path, marker, is_block=False, block_end=None):
    t = open(path, encoding="utf-8").read()
    n = t.count(marker)
    if n < 2:
        print(f"{path}: {n} occurrence(s) — nothing to do")
        return
    # find the SECOND occurrence and remove it (with its enclosing block if
    # a block end is given)
    first = t.index(marker)
    second = t.index(marker, first + 1)
    if block_end:
        end = t.index(block_end, second) + len(block_end)
        t = t[:second] + t[end:]
    else:
        # marker-only removal: remove the marker's full inserted segment.
        # For the CLAUDE clause, the segment starts at ' and the v113' and
        # runs to the matching close paren — handled by caller text instead.
        raise SystemExit(f"{path}: marker-only dedup not supported")
    open(path, "w", encoding="utf-8").write(t)
    print(f"{path}: deduplicated ({n} -> {t.count(marker)})")

# README: the v113 plan row — each row is a full line starting '|' and
# ending ' |'; remove the second full line containing the marker.
def dedup_line(path, marker):
    lines = open(path, encoding="utf-8").read().split("\n")
    hits = [i for i, l in enumerate(lines) if marker in l]
    if len(hits) < 2:
        print(f"{path}: {len(hits)} line hit(s) — nothing to do")
        return
    # remove the SECOND hit line
    del lines[hits[1]]
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    print(f"{path}: removed the duplicate line (had {len(hits)})")

# SKILL: the Session 148 row is one line — same line-dedup.
dedup_line("README.md", "docs/remediation-plan-v113.md")
dedup_line("zero-balance_SKILL.md", "Session 148 — parity iteration v113")

# PAD: the v1.1.70 block — from the marker back to the block start, through
# the block's trailing blank line.
def dedup_pad():
    path = "Project_Architecture_Document.md"
    t = open(path, encoding="utf-8").read()
    marker = "#### Revision Block — v1.1.70 (Tracked Changes)"
    n = t.count(marker)
    if n < 2:
        print(f"{path}: {n} occurrence(s) — nothing to do")
        return
    first = t.index(marker)
    second = t.index(marker, first + 1)
    # the block ends at the next '#### Revision Block' header or the section end
    next_hdr = t.find("#### Revision Block", second + len(marker))
    if next_hdr == -1:
        next_hdr = t.find("\n## ", second)
    end = next_hdr if next_hdr != -1 else len(t)
    t = t[:second] + t[end:]
    # clean any doubled blank lines left behind
    while "\n\n\n" in t:
        t = t.replace("\n\n\n", "\n\n")
    open(path, "w", encoding="utf-8").write(t)
    print(f"{path}: removed the duplicate v1.1.70 block ({n} -> {t.count(marker)})")

dedup_pad()

# CLAUDE: the duplicated clause — ' and the v113 guidelines label-row census
# (...)' appears twice back-to-back; remove the second.
def dedup_claude():
    path = "CLAUDE.md"
    t = open(path, encoding="utf-8").read()
    marker = " and the v113 guidelines label-row census"
    n = t.count(marker)
    if n < 2:
        print(f"{path}: {n} occurrence(s) — nothing to do")
        return
    first = t.index(marker)
    second = t.index(marker, first + 1)
    # the clause ends at its closing ' zero layout boxes moved)' — find the
    # first occurrence of that terminator AFTER the second marker
    term = "zero layout boxes moved)"
    end = t.index(term, second) + len(term)
    t = t[:second] + t[end:]
    open(path, "w", encoding="utf-8").write(t)
    print(f"{path}: removed the duplicate clause ({n} -> {t.count(marker)})")

dedup_claude()

# final verification
checks = [
    ("CLAUDE.md", "v113 guidelines label-row census", 1),
    ("README.md", "docs/remediation-plan-v113.md", 2),  # 2 mentions in ONE row
    ("zero-balance_SKILL.md", "Session 148 — parity iteration v113", 1),
    ("Project_Architecture_Document.md", "v1.1.70 (2026-10-24)", 1),
    ("AGENTS.md", "v113 iteration", 1),
]
allok = True
for path, marker, want in checks:
    got = open(path, encoding="utf-8").read().count(marker)
    status = "OK" if got == want else f"FAIL (got {got}, want {want})"
    if got != want:
        allok = False
    print(f"verify {path}: {marker[:40]!r} -> {status}")
print("DEDUP COMPLETE" if allok else "DEDUP INCOMPLETE")
