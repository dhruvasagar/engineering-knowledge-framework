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
LINK_PATTERN = re.compile(r'\]\(([^)]+)\)')
IGNORE_PATTERNS = [
    re.compile(r'^https?://'),
    re.compile(r'^\.\./README\.md$'),  # Cross-repo links
]


def collect_org_files():
    """Collect all .md files in the repository."""
    org_files = []
    SKIP_DIRS = {'.git', 'site', 'tools', '.org-backup', '.venv', '__pycache__'}
    for root, dirs, files in os.walk(REPO_ROOT):
        rel = Path(root).relative_to(REPO_ROOT)
        # Skip ignored directories
        if any(p in SKIP_DIRS or p.startswith('.') for p in rel.parts):
            continue
        for f in files:
            if f.endswith('.md'):
                org_files.append(Path(root) / f)
    return org_files


def resolve_link(doc_path, link_target):
    """Resolve a markdown link to an absolute file path."""
    link_target = link_target.split('#')[0].split('?')[0]
    if not link_target or link_target.startswith('#'):
        return Path('/')  # anchor link, skip
    # Build path variants to try
    variants = [link_target]
    if link_target.endswith('/'):
        variants.append(link_target.rstrip('/'))
        variants.append(link_target.rstrip('/') + '.md')
    # Resolve from doc's directory
    for v in variants:
        resolved = (doc_path.parent / v).resolve()
        if resolved.exists() and resolved.is_file():
            try:
                resolved.relative_to(REPO_ROOT)
                return resolved
            except ValueError:
                pass
    # Resolve from repo root
    for v in variants:
        resolved = (REPO_ROOT / v.lstrip('./')).resolve()
        if resolved.exists() and resolved.is_file():
            return resolved
        # Try with .md if no extension
        parts = v.lstrip('./').split('/')
        if parts and '.' not in parts[-1]:
            # Try as a file with .md
            trial = (REPO_ROOT / v.lstrip('./') / '').with_suffix('.md').resolve()
            if trial.exists() and trial.is_file():
                return trial
            # Also try the last component as filename
            trial2 = (REPO_ROOT / '/'.join(parts[:-1]) / (parts[-1] + '.md')).resolve()
            if trial2.exists() and trial2.is_file():
                return trial2
    # Final: strip ../ prefix (Zola-style links from root files)
    clean = link_target
    while clean.startswith('../'):
        clean = clean[3:]
    if clean != link_target:
        return resolve_link(REPO_ROOT / 'README.md', clean)
    # Check if target is a directory (some links reference dirs like rfc/, assets/)
    dir_check = (doc_path.parent / link_target).resolve()
    if dir_check.is_dir():
        return dir_check  # Accept directory links
    return Path('/nonexistent')


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
            link_count += 1

            # Skip external links
            if link_target.startswith('http://') or link_target.startswith('https://'):
                continue

            resolved = resolve_link(doc_path, link_target)

            if not resolved.exists():
                errors.append({
                    'file': str(rel_path),
                    'line': _find_line_number(content, match.start()),
                    'target': link_target,
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
            print(f"     → {err['target']}")
            print()
        sys.exit(1)
    else:
        print("✅ All cross-references resolve correctly!")
        sys.exit(0)


if __name__ == '__main__':
    main()
