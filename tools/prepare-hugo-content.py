#!/usr/bin/env python3
"""
Prepare Hugo content — copy .org files into Hugo's content directory.

README.org files are renamed to _index.org (Hugo section indexes).
All other .org files keep their name.

Usage:
    python3 tools/prepare-hugo-content.py
"""

import os
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HUGO_CONTENT = REPO_ROOT / 'site' / 'content'

# Root-level governance files to copy (with special URL handling)
GOVERNANCE_FILES = {
    'STRATEGY.org': 'strategy/_index.org',
    'ROADMAP.org': 'roadmap/_index.org',
    'ARCHITECTURE.org': 'architecture/_index.org',
    'DOCUMENT_TYPES.org': 'document-types/_index.org',
    'STYLE_GUIDE.org': 'style-guide/_index.org',
    'WRITING_PRINCIPLES.org': 'writing-principles/_index.org',
    'CONTRIBUTING.org': 'contributing/_index.org',
    'CHANGELOG.org': 'changelog/_index.org',
}

SKIP_DIRS = {'.git', 'site', 'tools', 'assets'}


def prepare_content():
    """Copy org files into Hugo content directory."""
    if HUGO_CONTENT.exists():
        shutil.rmtree(HUGO_CONTENT)
    HUGO_CONTENT.mkdir(parents=True)

    count = 0

    # Copy root README.org as homepage
    readme = REPO_ROOT / 'README.org'
    if readme.exists():
        shutil.copy2(readme, HUGO_CONTENT / '_index.org')
        count += 1

    # Copy governance files to their own directories
    for src_name, dst_rel in GOVERNANCE_FILES.items():
        src = REPO_ROOT / src_name
        if src.exists():
            dst = HUGO_CONTENT / dst_rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            count += 1

    # Walk the repo and copy capability directories
    for root, dirs, files in os.walk(REPO_ROOT):
        rel_root = Path(root).relative_to(REPO_ROOT)

        # Skip ignored directories
        parts = set(rel_root.parts)
        if SKIP_DIRS & parts:
            continue

        # Skip root-level governance files (already handled)
        if rel_root == Path('.'):
            continue

        for f in files:
            if not f.endswith('.org'):
                continue

            src_path = Path(root) / f

            # Determine destination
            if f == 'README.org':
                # README.org becomes _index.org (section index)
                dst_rel = rel_root / '_index.org'
            else:
                dst_rel = rel_root / f

            dst_path = HUGO_CONTENT / dst_rel
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_path, dst_path)
            count += 1

    return count


def main():
    print("📦 Preparing Hugo content...")
    count = prepare_content()
    print(f"   Copied {count} .org files to {HUGO_CONTENT}")
    print("✅ Done!")


if __name__ == '__main__':
    main()
