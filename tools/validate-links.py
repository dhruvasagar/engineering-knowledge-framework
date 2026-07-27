#!/usr/bin/env python3
"""
Link Validator — Verify all [[file:...][...]] cross-references resolve.

Scans all .md files in the repository and checks that every
[[file:...][...]] link points to an existing file relative to the
repository root or the document's location.

Usage:
    python3 tools/validate-links.py
    python3 tools/validate-links.py --fix    # Report missing files
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LINK_PATTERN = re.compile(r'\[\[file:([^\]]+)\]\[([^\]]*)\]\]')
IGNORE_PATTERNS = [
    re.compile(r'^https?://'),
    re.compile(r'^\.\./README\.md$'),  # Cross-repo links
]


def collect_org_files():
    """Collect all .md files in the repository."""
    org_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        # Skip .git directory
        if '.git' in root.split(os.sep):
            continue
        for f in files:
            if f.endswith('.md'):
                org_files.append(Path(root) / f)
    return org_files


def resolve_link(doc_path, link_target):
    """Resolve a [[file:...]] link target to an absolute path."""
    # Relative to the document's directory
    doc_dir = doc_path.parent
    resolved = (doc_dir / link_target).resolve()

    # Try relative to repository root
    if not resolved.exists():
        resolved = (REPO_ROOT / link_target).resolve()

    return resolved


def validate_links(org_files):
    """Validate all links in all org files."""
    errors = []
    link_count = 0

    # Pre-build set of all org files for quick lookup
    all_org_files = set()
    for f in org_files:
        rel = f.relative_to(REPO_ROOT)
        all_org_files.add(str(rel))

    for doc_path in org_files:
        rel_path = doc_path.relative_to(REPO_ROOT)
        content = doc_path.read_text(encoding='utf-8')

        for match in LINK_PATTERN.finditer(content):
            link_target = match.group(1)
            link_text = match.group(2)
            link_count += 1

            # Skip external links
            if any(p.match(link_target) for p in IGNORE_PATTERNS):
                continue
            if link_target.startswith('http://') or link_target.startswith('https://'):
                continue

            resolved = resolve_link(doc_path, link_target)

            if not resolved.exists():
                errors.append({
                    'file': str(rel_path),
                    'line': _find_line_number(content, match.start()),
                    'target': link_target,
                    'text': link_text,
                })

    return errors, link_count


def _find_line_number(content, position):
    """Find the line number for a character position."""
    return content[:position].count('\n') + 1


def main():
    print("🔗 Link Validator")
    print(f"   Scanning {REPO_ROOT}...\n")

    org_files = collect_org_files()
    print(f"   Found {len(org_files)} .md files")

    errors, link_count = validate_links(org_files)
    print(f"   Checked {link_count} cross-references\n")

    if errors:
        print(f"❌ {len(errors)} broken link(s) found:\n")
        for err in errors:
            print(f"   {err['file']}:{err['line']}")
            print(f"     → [[file:{err['target']}][{err['text']}]]")
            print()
        sys.exit(1)
    else:
        print("✅ All cross-references resolve correctly!")
        sys.exit(0)


if __name__ == '__main__':
    main()
