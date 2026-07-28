#!/usr/bin/env python3
"""
Fix markdown source files:
1. Strip front matter (--- blocks) from all source .md files
2. Convert Zola-style directory links (path/README/ → path/README.md)
   back to standard markdown links

Run this once to clean up source files after the org→md migration
incorrectly introduced Zola-style paths in the source.

Usage:
    python3 tools/fix-markdown-links.py
    python3 tools/fix-markdown-links.py --dry-run   # Preview changes only
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {'.git', 'site', 'tools', '__pycache__', '.org-backup', '.venv', 'assets'}


def collect_md_files():
    """Collect all source .md files."""
    files = []
    for root, dirs, _ in os.walk(REPO_ROOT):
        rel = Path(root).relative_to(REPO_ROOT)
        if any(p in SKIP_DIRS or p.startswith('.') for p in rel.parts):
            continue
        for f in os.listdir(root):
            if f.endswith('.md'):
                files.append(Path(root) / f)
    return files


def strip_front_matter(content):
    """Strip YAML front matter (--- ... ---) from content.
    Also strips any leading blank lines left after removal.
    """
    m = re.match(r'^---\n.*?\n---\n', content, re.DOTALL)
    if m:
        return content[m.end():].lstrip('\n')
    return content


def fix_links(content):
    """Convert Zola-style directory links to standard .md links.
    
    Zola serves README.md as /path/README/ and file.md as /path/file/.
    The current source has links targeting these directory-style paths.
    We need to convert them back to normal .md links.
    
    Patterns:
      [text](../../handbooks/engineering/README/)  →  [text](../../handbooks/engineering/README.md)
      [text](./guides/testing/)                     →  [text](./guides/testing.md)
    """
    # The source file path is needed to resolve relative links
    src_path = getattr(fix_links, 'current_src', REPO_ROOT / 'README.md')
    
    def replace_link(m):
        prefix = m.group(1)  # everything before the target
        target = m.group(2)  # the URL portion
        suffix = m.group(3)  # closing )
        
        # Skip external links, anchors, mailto
        if target.startswith(('http://', 'https://', '#', 'mailto:')):
            return m.group(0)
        
        if target.endswith('/'):
            # Try resolving: could be a directory or a file without .md
            bare = target.rstrip('/')
            # Resolve relative to the source file's directory
            resolved_dir = (src_path.parent / bare).resolve()
            
            if resolved_dir.is_dir():
                # It's a directory — link to README.md inside
                target = bare + '/README.md'
            else:
                # It's a file reference — add .md
                target = bare + '.md'
            
            return f'{prefix}{target}{suffix}'
        
        return m.group(0)
    
    # Pattern: ](target) 
    content = re.sub(r'(\]\()([^)]*?)(\))', replace_link, content)
    return content


def main():
    dry_run = '--dry-run' in sys.argv
    
    md_files = collect_md_files()
    changed = 0
    total_fm = 0
    total_links = 0
    
    for fp in sorted(md_files):
        original = fp.read_text(encoding='utf-8')
        content = original
        
        # Strip front matter
        stripped = strip_front_matter(content)
        if stripped != content:
            total_fm += 1
        content = stripped
        
        # Fix links — pass current source path for relative resolution
        fix_links.current_src = fp
        fixed = fix_links(content)
        if fixed != content:
            # Count changed links
            orig_links = re.findall(r'\]\([^)]*/\)', content)
            new_links = re.findall(r'\]\([^)]*\.md\)', fixed)
            total_links += len(orig_links) - len(new_links) if len(orig_links) > len(new_links) else abs(len(orig_links) - len(new_links))
        content = fixed
        
        if content != original:
            changed += 1
            rel = fp.relative_to(REPO_ROOT)
            if dry_run:
                print(f"  Would fix: {rel}")
            else:
                fp.write_text(content, encoding='utf-8')
                print(f"  Fixed: {rel}")
    
    print(f"\nScanned {len(md_files)} files")
    print(f"Stripped front matter from {total_fm} files")
    print(f"Fixed links in {changed} files")
    if dry_run:
        print("(dry run — no files were modified)")


if __name__ == '__main__':
    import os
    main()
