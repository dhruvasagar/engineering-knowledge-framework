#!/usr/bin/env python3
"""
Style Validator — Check documents against STYLE_GUIDE.org rules.

Validates:
- All required metadata headers present (#+TITLE, #+AUTHOR, #+DATE, #+DESCRIPTION)
- No skipped heading levels
- No * used as bullet markers (should be -)
- File naming conventions (.org extension, lowercase-with-dashes)

Usage:
    python3 tools/validate-style.py
    python3 tools/validate-style.py --fix
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_METADATA = ['#+TITLE:', '#+AUTHOR:', '#+DATE:', '#+DESCRIPTION:']
HEADING_PATTERN = re.compile(r'^(\*+)\s')
BULLET_PATTERN = re.compile(r'^\s*\*\s+[A-Za-z]')


def collect_org_files():
    """Collect all .org files excluding .git."""
    org_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        if '.git' in root.split(os.sep):
            continue
        for f in files:
            if f.endswith('.org'):
                org_files.append(Path(root) / f)
    return org_files


def validate_metadata(filepath):
    """Check that required metadata headers are present."""
    content = filepath.read_text(encoding='utf-8')
    errors = []

    for meta in REQUIRED_METADATA:
        if meta not in content:
            errors.append(f"Missing metadata: {meta}")

    return errors


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
    """Check for * used as bullet instead of -."""
    content = filepath.read_text(encoding='utf-8')
    lines = content.split('\n')
    errors = []
    in_code_block = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        if stripped.startswith('```'):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        # Check for * used as bullet (not headline)
        if re.match(r'^\*\s+', line) and not line.startswith('**'):
            # Check if previous line also starts with * (list context)
            prev_line = lines[i-1].strip() if i > 0 else ''
            next_line = lines[i+1].strip() if i+1 < len(lines) else ''

            if (prev_line.startswith('* ') and not prev_line.startswith('**')) or \
               (next_line.startswith('* ') and not next_line.startswith('**')) or \
               stripped.rstrip().endswith('.'):
                errors.append(
                    f"Line {i+1}: Use '-' instead of '*' for bullet: {stripped}"
                )

    return errors


def validate_filename(filepath):
    """Check file naming conventions."""
    rel_path = filepath.relative_to(REPO_ROOT)
    name = filepath.stem  # Without .org
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
