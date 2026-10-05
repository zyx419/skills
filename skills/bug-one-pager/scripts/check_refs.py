#!/usr/bin/env python3
"""Verify the reference contract of a bug one-pager.

The left column may only cite rail items that exist, and every rail item must
be cited at least once. Run this before handing the file over — a dangling
citation sends the reader hunting for something that isn't there, and an
uncited rail item is by definition material nobody needs.

    python3 scripts/check_refs.py slide.html

Exits 1 on any violation.
"""
import re
import sys


def audit(html):
    # Commented-out markup (e.g. an unused screenshot slot in the template) is
    # not on the page, so it must not count as a rail item or a citation.
    live = re.sub(r"<!--.*?-->", "", html, flags=re.S)

    cited = re.findall(r'class="ref"[^>]*>\s*([A-Z])\s*<', live)
    defined = re.findall(r'class="id"[^>]*>\s*([A-Z])\s*<', live)

    problems = []

    dangling = sorted(set(cited) - set(defined))
    if dangling:
        problems.append(
            "dangling citation(s) %s — the left column points at rail items "
            "that do not exist" % ", ".join(dangling))

    orphaned = sorted(set(defined) - set(cited))
    if orphaned:
        problems.append(
            "uncited rail item(s) %s — delete them, or add the citation that "
            "makes them worth keeping" % ", ".join(orphaned))

    dupes = sorted({x for x in defined if defined.count(x) > 1})
    if dupes:
        problems.append("duplicate rail label(s) %s" % ", ".join(dupes))

    if not defined and not cited:
        problems.append(
            "no rail items at all — the left column is probably carrying "
            "material that belongs on the right")

    return problems, cited, defined


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    html = open(sys.argv[1], encoding="utf-8").read()
    problems, cited, defined = audit(html)

    print("rail items : %s" % (", ".join(sorted(set(defined))) or "none"))
    print("citations  : %s" % (", ".join(sorted(set(cited))) or "none"))

    if problems:
        print("\nFAIL")
        for p in problems:
            print("  - %s" % p)
        return 1
    print("\nOK — every citation resolves, every rail item is cited.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
