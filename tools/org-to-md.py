#!/usr/bin/env python3
"""
One-time Org to Markdown Converter — Converts all .md files to .md in-place.

- Converts [[file:path.md][desc]] → [desc](path.md) for inter-file links
- Converts all org markup to markdown
- Removes .md files after successful conversion

Usage:
    python3 tools/org-to-md.py
"""

import os
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Patterns
BOLD = re.compile(r'\*(\S[^*]+\S)\*')
ITALIC = re.compile(r'/(\S[^/]+\S)/')
CODE = re.compile(r'=(\S[^=]+\S)=')
VERBATIM = re.compile(r'~(\S[^~]+\S)~')
LINK_ORG = re.compile(r'\[\[file:([^\]]+)\]\[([^\]]*)\]\]')
LINK_ORG_SIMPLE = re.compile(r'\[\[file:([^\]]+)\]\]')
HEADING = re.compile(r'^(\*+)\s+(.*)')
TABLE = re.compile(r'^\|(.+)\|$')
TABLE_SEP = re.compile(r'^\|[-+|]+\|$')
TITLE = re.compile(r'^#\+TITLE:\s*(.*)', re.MULTILINE)
DESC = re.compile(r'^#\+DESCRIPTION:\s*(.*)', re.MULTILINE)
ORG_META = re.compile(r'^#\+[A-Z_]+:.*\n?', re.MULTILINE)
ORG_STARTUP = re.compile(r'^#\+STARTUP:.*\n?', re.MULTILINE)

SKIP_DIRS = {'.git', 'site', 'tools', 'assets', '__pycache__'}
BACKUP_DIR = REPO_ROOT / '.md-backup'


def convert_inline(text):
    """Convert org inline markup to markdown."""
    text = BOLD.sub(r'**\1**', text)
    text = ITALIC.sub(r'*\1*', text)
    text = CODE.sub(r'`\1`', text)
    text = VERBATIM.sub(r'`\1`', text)
    return text


def convert_links(content):
    """Convert [[file:path.md][desc]] → [desc](path.md)."""
    def replace(m):
        target = m.group(1)
        try:
            desc = m.group(2)
        except IndexError:
            desc = None
        if desc is None:
            desc = target
        desc = convert_inline(desc)
        # Strip .md extension → directory path for Zola
        if target.endswith('.md'):
            target = target[:-4] + '/'
        elif target.endswith('/'):
            pass  # Already a directory path
        return f'[{desc}]({target})'

    # Protect links from inline markup, convert them, restore
    placeholders = {}
    def save(m):
        idx = len(placeholders)
        key = f'⛓{idx}⛓'
        placeholders[key] = (m.group(0), m.re)  # Store match + pattern
        return key

    content = LINK_ORG.sub(save, content)
    content = LINK_ORG_SIMPLE.sub(save, content)
    content = convert_inline(content)
    for key, (org_link, pattern) in placeholders.items():
        md_link = pattern.sub(replace, org_link)
        content = content.replace(key, md_link)
    return content


def convert_headings(content):
    """Convert * headings → # headings."""
    lines = content.split('\n')
    result = []
    for line in lines:
        m = HEADING.match(line)
        if m:
            level = len(m.group(1))
            text = convert_inline(m.group(2))
            result.append(f'{"#" * level} {text}')
        else:
            result.append(line)
    return '\n'.join(result)


def convert_tables(content):
    """Convert org tables to markdown tables."""
    lines = content.split('\n')
    result = []
    in_table = False
    header_done = False
    table = []

    for line in lines:
        if TABLE.match(line) and not TABLE_SEP.match(line):
            table.append(line)
            in_table = True
        else:
            if in_table:
                for i, t in enumerate(table):
                    cells = [c.strip() for c in t.strip('|').split('|')]
                    result.append('| ' + ' | '.join(cells) + ' |')
                    if i == 0:
                        result.append('| ' + ' | '.join(['---'] * len(cells)) + ' |')
                table = []
                in_table = False
            result.append(line)

    if table:
        for i, t in enumerate(table):
            cells = [c.strip() for c in t.strip('|').split('|')]
            result.append('| ' + ' | '.join(cells) + ' |')
            if i == 0:
                result.append('| ' + ' | '.join(['---'] * len(cells)) + ' |')

    return '\n'.join(result)


def convert_code_blocks(content):
    """Convert #+BEGIN_SRC/EXAMPLE → ```."""
    lines = content.split('\n')
    result = []
    in_block = False
    for line in lines:
        s = line.strip()
        if s.startswith('#+BEGIN_SRC') or s.startswith('#+BEGIN_EXAMPLE'):
            in_block = True
            lang = re.search(r'#\+BEGIN_SRC\s+(\w+)', s)
            result.append('```' + (lang.group(1) if lang else ''))
        elif s.startswith('#+END_SRC') or s.startswith('#+END_EXAMPLE'):
            in_block = False
            result.append('```')
        elif s.startswith('#+BEGIN_VERSE'):
            result.append('> ')
        elif s.startswith('#+END_VERSE'):
            pass
        else:
            result.append(line)
    return '\n'.join(result)


def convert_org_file(filepath):
    """Convert a single .md file to .md content."""
    content = filepath.read_text(encoding='utf-8')

    # Extract title/description
    title = ''
    description = ''
    tm = TITLE.search(content)
    dm = DESC.search(content)
    if tm:
        title = tm.group(1).strip()
    if dm:
        description = dm.group(1).strip()

    # Strip org metadata
    content = ORG_META.sub('', content)
    content = ORG_STARTUP.sub('', content)

    # Convert
    content = convert_code_blocks(content)
    content = convert_tables(content)
    content = convert_headings(content)
    content = convert_links(content)

    # Build front matter
    fm = ['+++']
    if title:
        fm.append(f'title = "{title.replace(chr(34), chr(92)+chr(34))}"')
    if description:
        fm.append(f'description = "{description.replace(chr(34), chr(92)+chr(34))}"')
    fm.append('+++\n')

    return '\n'.join(fm) + '\n' + content


def backup_org(filepath):
    """Backup an org file before replacing."""
    rel = filepath.relative_to(REPO_ROOT)
    backup_path = BACKUP_DIR / rel
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(filepath, backup_path)
    return backup_path


def convert_repo():
    """Convert all .md files in the repository to .md in-place."""
    converted = 0
    errors = 0
    backups = 0

    for root, dirs, files in os.walk(REPO_ROOT):
        rel = Path(root).relative_to(REPO_ROOT)
        if any(p in SKIP_DIRS for p in rel.parts):
            continue

        for f in sorted(files):
            if not f.endswith('.md'):
                continue

            src = Path(root) / f

            # Backup
            try:
                backup_org(src)
                backups += 1
            except Exception as e:
                print(f"  ⚠ Backup failed for {src.relative_to(REPO_ROOT)}: {e}")

            # Convert
            try:
                md_content = convert_org_file(src)
                md_path = src.with_suffix('.md')
                md_path.write_text(md_content, encoding='utf-8')
                src.unlink()  # Remove .md file
                converted += 1
                print(f"  ✓ {src.relative_to(REPO_ROOT)} → {md_path.name}")
            except Exception as e:
                errors += 1
                print(f"  ✗ {src.relative_to(REPO_ROOT)}: {e}")

    return converted, errors, backups


def main():
    print("🔄 Converting all .md files to .md in-place...\n")
    print(f"   Backup directory: {BACKUP_DIR}\n")

    converted, errors, backups = convert_repo()

    print(f"\n   Converted: {converted} files")
    print(f"   Backed up: {backups} files")
    if errors:
        print(f"   Errors: {errors}")
    if BACKUP_DIR.exists():
        print(f"   Backup: {BACKUP_DIR} (delete after verifying)")
    print("\n✅ Done! .md files replaced with .md. Backups saved to .md-backup/")
    print("   Run: rm -rf .md-backup  (after verifying everything works)")


if __name__ == '__main__':
    main()
