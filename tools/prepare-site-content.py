#!/usr/bin/env python3
"""
Prepare Zola content — copy .md files from the repo root into
site/content/, adding Zola front matter and fixing links for Zola's
directory-based URL scheme.

Source files are plain markdown without front matter, using .md links:
    [text](../../handbooks/engineering/README.md)

Copied files get Zola front matter with title derived from path:
    [text](../../handbooks/engineering/README/)
    [text](./guides/testing/)

Usage:
    python3 tools/prepare-site-content.py
"""

import os
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SITE_CONTENT = REPO_ROOT / 'site' / 'content'

SKIP_DIRS = {'.git', 'site', 'tools', 'assets', '__pycache__', '.org-backup', '.venv'}
SKIP_FILES = {'CLAUDE.md', 'Makefile', '.gitignore', 'LICENSE'}

LINK_PATTERN = re.compile(r'\]\(([^)]+)\)')

# ── Title derivation ──────────────────────────────────────────────────

# Human-readable names for capability directories
CAPABILITY_NAMES = {
    'accessibility': 'Accessibility Engineering',
    'ai': 'AI Engineering',
    'architecture': 'Software Architecture',
    'engineering': 'Engineering Fundamentals',
    'quality': 'Engineering Quality',
    'rails': 'Rails Engineering',
    'security': 'Security Engineering',
}

# Document type labels for index/README files
DOC_TYPE_LABELS = {
    'handbooks': 'Handbook',
    'glossary': 'Glossary',
    'guides': 'Guides',
    'playbooks': 'Playbooks',
    'checklists': 'Checklists',
    'templates': 'Templates',
    'learning-paths': 'Learning Paths',
    'references': 'References',
    'prompts': 'AI Workflows',
}


def path_to_title(filepath):
    """Derive a human-readable title from a file's relative path.
    
    Uses conventions based on the file's location in the framework:
      handbooks/{cap}/README.md  → "{Capability} Handbook"
      guides/{cap}/{topic}.md    → "{Topic Title}"
      glossary/{cap}/README.md   → "{Capability} Glossary"
      etc.
    """
    rel = filepath.relative_to(REPO_ROOT)
    parts = rel.parts

    # Root-level governance docs
    if len(parts) == 1:
        name = parts[0].replace('-', ' ').replace('.md', '').title()
        # Handle special cases
        special = {
            'README': 'Engineering Knowledge Framework',
            'TOC': 'Table of Contents',
            'CLAUDE': 'CLAUDE',
        }
        return special.get(parts[0].replace('.md', ''), name)

    # ADR files: adr/XXXX-title.md
    if parts[0] == 'adr' and len(parts) >= 2:
        # Extract title from the ADR file content or use filename
        stem = parts[-1].replace('.md', '')
        title_part = stem[5:].replace('-', ' ').title()  # strip "0001-"
        return f"ADR-{stem[:4]}: {title_part}"

    # Capability documents
    doc_type_dir = parts[0]  # handbooks, guides, etc.
    cap_dir = parts[1] if len(parts) > 1 else ''
    filename = parts[-1]

    capability = CAPABILITY_NAMES.get(cap_dir, cap_dir.replace('-', ' ').title())
    doc_type = DOC_TYPE_LABELS.get(doc_type_dir, doc_type_dir.replace('-', ' ').title())

    # README means it's the index page of that directory
    if filename == 'README.md':
        # guides/rails/README.md → "Rails Guides"
        return f"{capability} {doc_type}"

    # Specific file within a capability: guides/rails/service-objects.md
    stem = filename.replace('.md', '')
    topic = stem.replace('-', ' ').title()
    return topic


def add_front_matter(content, title):
    """Wrap content with Zola front matter."""
    title_escaped = title.replace('"', '\\"')
    return f'+++\ntitle = "{title_escaped}"\n+++\n\n{content}'


def zolafy_link_target(target):
    """Convert a markdown .md link target to Zola's directory-style URL.
    
    Rules:
      path/README.md  → path/README/    (Zola serves README at dir/README/)
      path/file.md    → path/file/      (Zola serves without .md extension)
      ./path.md       → ./path/
      http://...      → unchanged
      #anchor         → unchanged
      mailto:...      → unchanged
    """
    if target.startswith(('http://', 'https://', '#', 'mailto:')):
        return target
    
    if target.endswith('.md'):
        target = target[:-3]
        if not target.endswith('/'):
            target += '/'
    
    return target


def copy_with_fixes(src, dst):
    """Copy a file from source to site content, applying Zola fixes."""
    content = src.read_text(encoding='utf-8')
    
    # Strip any existing front matter (in case some files have it)
    content = re.sub(r'^---\n.*?\n---\n\n*', '', content, flags=re.DOTALL)
    
    # Fix links: .md → Zola directory-style URLs
    def replace_link(m):
        return f']({zolafy_link_target(m.group(1))})'
    
    content = LINK_PATTERN.sub(replace_link, content)
    
    # Derive title from path and add Zola front matter
    title = path_to_title(src)
    content = add_front_matter(content, title)
    
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
            dst_name = '_index.md' if f == 'README.md' else f
            dst = SITE_CONTENT / rel / dst_name
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
