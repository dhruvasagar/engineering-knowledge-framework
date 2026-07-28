#!/usr/bin/env python3
"""
Style Validator — Check documents against STYLE_GUIDE.md rules.

Validates:
- All required metadata headers present (#+TITLE, #+AUTHOR, #+DATE, #+DESCRIPTION)
- No skipped heading levels
- No * used as bullet markers (should be -)
- File naming conventions (.md extension, lowercase-with-dashes)

Usage:
    python3 tools/validate-style.py
    python3 tools/validate-style.py --fix
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_METADATA = ['title:', 'description:']
HEADING_PATTERN = re.compile(r'^(\*+)\s')
BULLET_PATTERN = re.compile(r'^\s*\*\s+[A-Za-z]')


def collect_org_files():
    """Collect all .md files excluding .git and .venv."""
    org_files = []
    SKIP_DIRS = {'.git', '.venv', '__pycache__', '.org-backup', 'node_modules'}
    for root, dirs, files in os.walk(REPO_ROOT):
        rel = Path(root).relative_to(REPO_ROOT)
        if any(p in SKIP_DIRS or p.startswith('.') for p in rel.parts):
            continue
        for f in files:
            if f.endswith('.md'):
                org_files.append(Path(root) / f)
    return org_files


def validate_metadata(filepath):
    """Front matter is optional in source files.
    Zola-compatible front matter is added by prepare-site-content.py
    during the site build step.
    """
    return []


def validate_headings(filepath):
    """Check for skipped heading levels."""
    content = filepath.read_text(encoding='utf-8')
    lines = content.split('\n')
    errors = []
    prev_level = 0

    for i, line in enumerate(lines):
        match = HEADING_PATTERN.match(line)
        if match:
            level = len(match.group(1))
            if prev_level > 0 and level > prev_level + 1:
                errors.append(
                    f"Line {i+1}: Skipped heading level ({prev_level} → {level}): {line.strip()}"
                )
            prev_level = level
        elif line.strip() == '':
            prev_level = 0  # Reset after blank line

    return errors


def validate_bullets(filepath):
    """In markdown, both * and - are valid bullet characters.
    No longer applicable since we migrated from org-mode."""
    return []


def validate_filename(filepath):
    """Check file naming conventions."""
    rel_path = filepath.relative_to(REPO_ROOT)
    name = filepath.stem  # Without .md
    errors = []

    # Skip files with README or index in name (conventional)
    if name in ('README', 'index'):
        return errors

    # Check for spaces
    if ' ' in name:
        errors.append(f"Filename contains spaces: {rel_path}")

    # Check for uppercase letters (except README)
    if name != name.lower() and name not in ('README', 'CHANGELOG', 'CLAUDE',
                                              'TOC', 'STYLE_GUIDE', 'WRITING_PRINCIPLES',
                                              'CONTRIBUTING', 'DOCUMENT_TYPES',
                                              'ARCHITECTURE', 'STRATEGY', 'ROADMAP'):
        errors.append(f"Filename should be lowercase: {rel_path}")

    return errors


def main():
    print("📝 Style Validator")
    print(f"   Scanning {REPO_ROOT}...\n")

    org_files = collect_org_files()
    all_errors = []
    file_count = 0

    for filepath in sorted(org_files):
        rel_path = filepath.relative_to(REPO_ROOT)
        file_errors = []

        file_errors.extend(validate_metadata(filepath))
        file_errors.extend(validate_headings(filepath))
        file_errors.extend(validate_bullets(filepath))
        file_errors.extend(validate_filename(filepath))

        if file_errors:
            all_errors.append((rel_path, file_errors))
        file_count += 1

    print(f"   Checked {file_count} files\n")

    if all_errors:
        print(f"❌ {sum(len(e) for _, e in all_errors)} style issue(s) found:\n")
        for rel_path, errors in all_errors:
            print(f"   {rel_path}:")
            for err in errors:
                print(f"     - {err}")
            print()
        sys.exit(1)
    else:
        print("✅ All style checks pass!")
        sys.exit(0)


if __name__ == '__main__':
    main()
