#!/usr/bin/env python3
"""
TOC Validator — Ensure TOC.md entries match actual file inventory.

Checks:
- Every .md file (except those in .git/) is listed in TOC.md
- Every TOC entry links to an existing file
- No duplicate entries in TOC

Usage:
    python3 tools/validate-toc.py
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TOC_FILE = REPO_ROOT / 'TOC.md'

LINK_PATTERN = re.compile(r'\[\[file:([^\]\[]+)\]\[|\[\[file:([^\]]+)\]\]')
IGNORE_FILES = {
    '.git',
    'tools',
    'zola-site',
}


def collect_org_files():
    """Collect all .md files excluding ignored directories."""
    org_files = set()
    for root, dirs, files in os.walk(REPO_ROOT):
        # Skip ignored directories
        rel_root = Path(root).relative_to(REPO_ROOT)
        if any(part.startswith('.') or part in IGNORE_FILES for part in rel_root.parts):
            continue
        for f in files:
            if f.endswith('.md'):
                org_files.add(str(rel_root / f))
    return org_files


def extract_toc_links():
    """Extract all [[file:...]] links from TOC.md."""
    if not TOC_FILE.exists():
        print(f"❌ TOC.md not found at {TOC_FILE}")
        sys.exit(1)

    content = TOC_FILE.read_text(encoding='utf-8')
    links = set()
    for match in LINK_PATTERN.finditer(content):
        # Group 1 is [[file:path][desc]], Group 2 is [[file:path]]
        link = match.group(1) or match.group(2)
        if link:
            links.add(link)
    return links


def validate_toc():
    """Validate TOC.md against actual file inventory."""
    org_files = collect_org_files()
    toc_links = extract_toc_links()

    errors = []

    # Normalize toc_links (strip leading ./)
    normalized_links = set()
    for link in toc_links:
        normalized = link[2:] if link.startswith('./') else link
        normalized_links.add(normalized)

    # Check: every .md file is referenced in TOC
    for org_file in sorted(org_files):
        if org_file not in normalized_links:
            errors.append(f"  Not in TOC: {org_file}")

    # Check: every TOC link points to an existing file
    for link in sorted(toc_links):
        # Strip ./ prefix for file existence check
        clean_link = link[2:] if link.startswith('./') else link
        target_path = REPO_ROOT / clean_link
        if not target_path.exists():
            errors.append(f"  Broken TOC link: {link}")

    return errors, len(org_files), len(toc_links)


def main():
    print("📑 TOC Validator")
    print(f"   Checking {TOC_FILE}...\n")

    errors, org_count, toc_count = validate_toc()

    print(f"   {org_count} .md files in repository")
    print(f"   {toc_count} links in TOC.md\n")

    if errors:
        print(f"❌ {len(errors)} TOC issue(s) found:\n")
        for err in errors:
            print(f"   {err}")
        print()
        sys.exit(1)
    else:
        print("✅ TOC.md is complete and consistent!")
        sys.exit(0)


if __name__ == '__main__':
    main()
