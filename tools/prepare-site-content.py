#!/usr/bin/env python3
"""
Prepare Zola content — copy .md files with proper section indexing.

- README.md → _index.md (Zola section indexes)
- Other .md files keep their name
- Excludes non-content files (CLAUDE.md, Makefile, .gitignore, etc.)

Usage:
    python3 tools/prepare-site-content.py
"""

import os
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SITE_CONTENT = REPO_ROOT / 'site' / 'content'

SKIP_DIRS = {'.git', 'site', 'tools', 'assets', '__pycache__', '.md-backup'}
SKIP_FILES = {'CLAUDE.md', 'Makefile', '.gitignore', 'LICENSE'}


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

            # README.md → _index.md (Zola section index)
            if f == 'README.md':
                dst = SITE_CONTENT / rel / '_index.md'
            else:
                dst = SITE_CONTENT / rel / f

            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            count += 1

    return count


def main():
    print("📦 Preparing Zola content...")
    count = prepare()
    print(f"   Copied {count} .md files to {SITE_CONTENT}")
    print("✅ Done!")


if __name__ == '__main__':
    main()
