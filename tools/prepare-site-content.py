#!/usr/bin/env python3
"""
Prepare Zola content — copy .md files with proper section indexing.

Fixes relative links for Zola's URL structure:
- Strips /README/ from link targets (README → _index → directory URL)
- Root-level files: ./path/ → ../path/ (page served at /file/ not /)

Usage:
    python3 tools/prepare-site-content.py
"""

import os
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SITE_CONTENT = REPO_ROOT / 'site' / 'content'

SKIP_DIRS = {'.git', 'site', 'tools', 'assets', '__pycache__', '.org-backup'}
SKIP_FILES = {'CLAUDE.md', 'Makefile', '.gitignore', 'LICENSE'}


def fix_links(content, dst_rel):
    """Fix relative links for Zola's URL structure.

    When a .md file is served at /path/file/, relative links need
    to account for the extra path level.
    """
    depth = len(dst_rel.parent.parts) if dst_rel.parent.name else 0

    # Fix 1: Strip /README/ from end of link targets
    #   ./handbooks/engineering/README/ → ./handbooks/engineering/
    #   ../../handbooks/engineering/README/ → ../../handbooks/engineering/
    content = re.sub(r'(]\()([^)]*)/README/(\))', r'\1\2/\3', content)

    # Fix 2: For root-level files, ./ → ../ since page is at /file/ not /
    if depth == 0:
        content = re.sub(r'(]\()\./', r'\1../', content)

    return content


def copy_with_fixes(src, dst):
    """Copy a file and fix its links for Zola."""
    content = src.read_text(encoding='utf-8')
    dst_rel = dst.relative_to(SITE_CONTENT)
    content = fix_links(content, dst_rel)
    dst.write_text(content, encoding='utf-8')


def prepare():
    if SITE_CONTENT.exists():
        shutil.rmtree(SITE_CONTENT)
    SITE_CONTENT.mkdir(parents=True)

    count = 0
    for root, dirs, files in os.walk(REPO_ROOT):
        rel = Path(root).relative_to(REPO_ROOT)
        if any(p in SKIP_DIRS for p in rel.parts):
            continue
        for f in sorted(files):
            if not f.endswith('.md'):
                continue
            if f in SKIP_FILES:
                continue
            src = Path(root) / f
            if f == 'README.md':
                dst = SITE_CONTENT / rel / '_index.md'
            else:
                dst = SITE_CONTENT / rel / f
            dst.parent.mkdir(parents=True, exist_ok=True)
            copy_with_fixes(src, dst)
            count += 1
    return count


def main():
    print("📦 Preparing Zola content...")
    count = prepare()
    print(f"   Copied {count} .md files to {SITE_CONTENT}")
    print("✅ Done!")


if __name__ == '__main__':
    main()
