#!/usr/bin/env python3
"""
Org to Markdown Converter — Convert .org files to Zola-compatible .md.

Handles the org-mode features used across the framework:
- #+TITLE:, #+DESCRIPTION: → front matter
- * headings → # headings
- [[file:path][desc]] links → [desc](path) links
- [[file:path]] links → relative path links
- - bullet lists
- Tables (org → markdown)
- Code blocks (BEGIN_SRC/END_SRC, BEGIN_EXAMPLE/END_EXAMPLE)
- #+BEGIN_VERSE, #+END_VERSE
- Bold, italic, code, verbatim markup

Usage:
    python3 tools/org-to-md.py                    # Convert all files
    python3 tools/org-to-md.py --watch            # Watch for changes
    python3 tools/org-to-md.py path/to/file.org   # Convert single file
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = REPO_ROOT / 'site'
CONTENT_DIR = SITE_DIR / 'content'

# Files to skip (no need to convert for site)
SKIP_FILES = {
    'CHANGELOG.org',
    'TOC.org',
    'CLAUDE.md',
}

# Org-mode markup patterns
BOLD_PATTERN = re.compile(r'\*(\S[^*]+\S)\*')
ITALIC_PATTERN = re.compile(r'/(\S[^/]+\S)/')
CODE_PATTERN = re.compile(r'=(\S[^=]+\S)=')
VERBATIM_PATTERN = re.compile(r'~(\S[^~]+\S)~')
LINK_PATTERN = re.compile(r'\[\[file:([^\]]+)\]\[([^\]]*)\]\]')
LINK_SIMPLE_PATTERN = re.compile(r'\[\[file:([^\]]+)\]\]')
HEADING_PATTERN = re.compile(r'^(\*+)\s+(.*)')
TABLE_PATTERN = re.compile(r'^\|(.+)\|$')
TABLE_SEPARATOR = re.compile(r'^\|[-+|]+\|$')

# Org metadata patterns
TITLE_PATTERN = re.compile(r'^#\+TITLE:\s*(.*)', re.MULTILINE)
DESC_PATTERN = re.compile(r'^#\+DESCRIPTION:\s*(.*)', re.MULTILINE)
DATE_PATTERN = re.compile(r'^#\+DATE:\s*(.*)', re.MULTILINE)
AUTHOR_PATTERN = re.compile(r'^#\+AUTHOR:\s*(.*)', re.MULTILINE)


def convert_inline_markup(text):
    """Convert org-mode inline markup to markdown."""
    text = BOLD_PATTERN.sub(r'**\1**', text)
    text = ITALIC_PATTERN.sub(r'*\1*', text)
    text = CODE_PATTERN.sub(r'`\1`', text)
    text = VERBATIM_PATTERN.sub(r'`\1`', text)
    return text


def convert_links(text, filepath):
    """Convert [[file:path][desc]] to markdown links."""
    def replace_link(match):
        target = match.group(1)
        desc = match.group(2) or target

        # Convert .org to .html for internal links
        if target.endswith('.org'):
            target = target[:-4] + '/'

        # Make relative path work from the converted file's location
        # Since we're flattening to content/, resolve relative to the source
        return f'[{desc}]({target})'

    text = LINK_PATTERN.sub(replace_link, text)
    text = LINK_SIMPLE_PATTERN.sub(r'[\1](\1)', text)
    return text


def convert_headings(text):
    """Convert org headings to markdown headings."""
    lines = text.split('\n')
    result = []
    for line in lines:
        match = HEADING_PATTERN.match(line)
        if match:
            level = len(match.group(1))
            heading_text = convert_inline_markup(match.group(2))
            heading_text = convert_links(heading_text, None)
            result.append(f'{"#" * level} {heading_text}')
        else:
            result.append(line)
    return '\n'.join(result)


def convert_tables(text):
    """Convert org tables to markdown tables."""
    lines = text.split('\n')
    result = []
    in_table = False
    header_separated = False
    table_lines = []

    for line in lines:
        if TABLE_PATTERN.match(line):
            if TABLE_SEPARATOR.match(line):
                continue  # Skip org table separators
            table_lines.append(line)
            in_table = True
            header_separated = False
        else:
            if in_table:
                # Flush the table
                for i, tline in enumerate(table_lines):
                    cells = [c.strip() for c in tline.strip('|').split('|')]
                    md_line = '| ' + ' | '.join(cells) + ' |'
                    if i == 1 and not header_separated:
                        # Add markdown header separator after first row
                        result.append('| ' + ' | '.join(['---'] * len(cells)) + ' |')
                        header_separated = True
                    result.append(md_line)
                table_lines = []
                in_table = False
            result.append(line)

    # Flush remaining table
    if table_lines:
        for i, tline in enumerate(table_lines):
            cells = [c.strip() for c in tline.strip('|').split('|')]
            md_line = '| ' + ' | '.join(cells) + ' |'
            if i == 1 and not header_separated:
                result.append('| ' + ' | '.join(['---'] * len(cells)) + ' |')
            result.append(md_line)

    return '\n'.join(result)


def convert_code_blocks(text):
    """Convert org code blocks to markdown code blocks."""
    lines = text.split('\n')
    result = []
    in_block = False
    block_lang = ''

    for line in lines:
        stripped = line.strip()

        if stripped.startswith('#+BEGIN_SRC') or stripped.startswith('#+BEGIN_EXAMPLE'):
            in_block = True
            # Extract language
            lang_match = re.search(r'#\+BEGIN_SRC\s+(\w+)', stripped)
            block_lang = lang_match.group(1) if lang_match else ''
            result.append(f'```{block_lang}')
            continue

        if stripped.startswith('#+END_SRC') or stripped.startswith('#+END_EXAMPLE'):
            in_block = False
            result.append('```')
            continue

        if stripped.startswith('#+BEGIN_VERSE'):
            result.append('> ')
            continue

        if stripped.startswith('#+END_VERSE'):
            continue

        if in_block:
            result.append(line)
        else:
            result.append(line)

    return '\n'.join(result)


def convert_org_to_md(content, filepath):
    """Convert full org file content to markdown."""
    # Remove org metadata
    title = ''
    description = ''
    date = ''
    author = ''

    title_match = TITLE_PATTERN.search(content)
    desc_match = DESC_PATTERN.search(content)
    date_match = DATE_PATTERN.search(content)
    author_match = AUTHOR_PATTERN.search(content)

    if title_match:
        title = title_match.group(1).strip()
    if desc_match:
        description = desc_match.group(1).strip()
    if date_match:
        date = date_match.group(1).strip()
    if author_match:
        author = author_match.group(1).strip()

    # Remove org metadata lines
    content = re.sub(r'^#\+[A-Z_]+:.*\n?', '', content, flags=re.MULTILINE)

    # Remove org startup directive
    content = re.sub(r'^#\+STARTUP:.*\n?', '', content, flags=re.MULTILINE)

    # Convert
    content = convert_code_blocks(content)
    content = convert_tables(content)
    content = convert_headings(content)
    content = convert_links(content, filepath)
    content = convert_inline_markup(content)

    # Build front matter (only valid Zola section/page fields)
    front_matter = ['+++']
    if title:
        safe_title = title.replace('"', '\\"')
        front_matter.append(f'title = "{safe_title}"')
    if description:
        safe_desc = description.replace('"', '\\"')
        front_matter.append(f'description = "{safe_desc}"')
    front_matter.append('+++\n')

    return '\n'.join(front_matter) + '\n' + content


def get_output_path(filepath):
    """Get the output path for a converted file.

    README.org files become _index.md (Zola section indexes).
    All other .org files keep their name as .md.
    """
    rel_path = filepath.relative_to(REPO_ROOT)

    if filepath.name == 'README.org':
        # Section index — becomes _index.md
        md_path = rel_path.parent / '_index.md'
    else:
        md_path = rel_path.with_suffix('.md')

    return CONTENT_DIR / md_path


def convert_file(filepath):
    """Convert a single org file to markdown."""
    try:
        content = filepath.read_text(encoding='utf-8')
        md_content = convert_org_to_md(content, filepath)
        output_path = get_output_path(filepath)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(md_content, encoding='utf-8')
        rel = filepath.relative_to(REPO_ROOT)
        print(f"  ✓ {rel}")
        return True
    except Exception as e:
        rel = filepath.relative_to(REPO_ROOT)
        print(f"  ✗ {rel}: {e}")
        return False


def convert_all():
    """Convert all org files in the repository."""
    count = 0
    errors = 0

    for root, dirs, files in os.walk(REPO_ROOT):
        if '.git' in root.split(os.sep):
            continue
        if 'site' in root.split(os.sep):
            continue
        if 'tools' in root.split(os.sep):
            continue

        for f in sorted(files):
            if f in SKIP_FILES:
                continue
            if f.endswith('.org'):
                filepath = Path(root) / f
                if convert_file(filepath):
                    count += 1
                else:
                    errors += 1

    return count, errors


def main():
    print("🔄 Org to Markdown Converter")
    print(f"   Source: {REPO_ROOT}")
    print(f"   Target: {CONTENT_DIR}\n")

    count, errors = convert_all()

    print(f"\n   Converted: {count} files")
    if errors:
        print(f"   Errors: {errors}")
    print("✅ Done!")


if __name__ == '__main__':
    main()
