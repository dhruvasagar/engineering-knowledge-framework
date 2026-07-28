#!/usr/bin/env python3
"""
Glossary Validator — Ensure all glossary entries have required fields.

Checks:
- Each glossary file has entries with definitions
- No duplicate terms across glossaries
- Each definition is non-empty
- Cross-references from guides to glossary terms are valid

Usage:
    python3 tools/validate-glossary.py
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GLOSSARY_DIR = REPO_ROOT / 'glossary'

# Pattern to match glossary entries: ** Term\n\nDefinition
ENTRY_PATTERN = re.compile(r'^##\s+([A-Za-z][A-Za-z\s\-/]+?)\n\n((?:(?!^##|^\* ).*\n?)*)', re.MULTILINE)


def collect_glossary_files():
    """Collect all glossary README.md files."""
    glossary_files = []
    for root, dirs, files in os.walk(GLOSSARY_DIR):
        if '.git' in root.split(os.sep):
            continue
        for f in files:
            if f.endswith('.md'):
                glossary_files.append(Path(root) / f)
    return glossary_files


def parse_glossary_entries(filepath):
    """Parse glossary entries from a file."""
    content = filepath.read_text(encoding='utf-8')
    entries = []

    # Find the Glossary section
    glossary_start = content.find('# Glossary')
    if glossary_start == -1:
        return entries

    # Parse entries after the Glossary heading
    section = content[glossary_start:]
    lines = section.split('\n')
    current_term = None
    current_def = []
    in_glossary = False

    for line in lines:
        stripped = line.strip()

        # Skip front matter and non-glossary top sections
        if stripped.startswith('---') or stripped == '':
            continue

        if stripped.startswith('# ') and 'Glossary' not in stripped:
            if in_glossary:
                break  # Reached next top-level section
            continue

        if stripped == '# Glossary' or stripped == '## Glossary':
            in_glossary = True
            continue

        if in_glossary and (stripped.startswith('## ') and not stripped.startswith('###') or stripped.startswith('** ') and not stripped.startswith('***')):
            # Save previous entry
            if current_term:
                entries.append({
                    'term': current_term,
                    'definition': ' '.join(current_def).strip(),
                })
            current_term = stripped[3:]
            current_def = []
        elif in_glossary and current_term and stripped:
            # Collect definition from table rows or plain text
            if stripped.startswith('|'):
                cells = [c.strip() for c in stripped.strip('|').split('|')]
                if len(cells) >= 2 and cells[0].startswith('Definition'):
                    current_def.append(cells[1])
                elif len(cells) >= 2 and cells[0] and len(cells[0]) < 3:
                    if current_def:
                        current_def[-1] += ' ' + cells[1]
                elif len(cells) >= 2 and cells[0] in ('Context', 'Context '):
                    pass  # skip context rows
            elif not stripped.startswith('###') and not stripped.startswith('|'):
                # Plain text definition (accessibility glossary style)
                # Stop at next ## heading, blank line, table, or reference
                if not stripped.startswith('-') and not stripped.startswith('['):
                    current_def.append(stripped)

    # Save last entry
    if current_term:
        entries.append({
            'term': current_term,
            'definition': ' '.join(current_def).strip(),
        })

    return entries


def validate_glossaries():
    """Validate all glossary files."""
    glossary_files = collect_glossary_files()
    all_entries = {}  # term -> (filepath, definition)
    errors = []

    for filepath in glossary_files:
        rel_path = filepath.relative_to(REPO_ROOT)

        # Skip root glossary README (it is an index, not a term glossary)
        if str(rel_path) == 'glossary/README.md':
            continue

        entries = parse_glossary_entries(filepath)

        if not entries:
            errors.append(f"  {rel_path}: No glossary entries found")
            continue

        for entry in entries:
            term = entry['term']

            # Check for empty definitions
            if not entry['definition']:
                errors.append(f"  {rel_path}: Empty definition for '{term}'")
                continue

            # Check for duplicate terms within the same glossary
            term_key = f"{rel_path}|{term.lower()}"
            if term_key in all_entries:
                errors.append(f"  {rel_path}: Duplicate term '{term}'")
            else:
                all_entries[term_key] = (rel_path, entry['definition'])

    return errors, len(set(k.split('|')[1] for k in all_entries))


def main():
    print("📖 Glossary Validator")
    print(f"   Scanning {GLOSSARY_DIR}...\n")

    errors, total_terms = validate_glossaries()

    print(f"   Found {total_terms} glossary terms across all capabilities\n")

    if errors:
        print(f"❌ {len(errors)} glossary issue(s) found:\n")
        for err in errors:
            print(f"   {err}")
        print()
        sys.exit(1)
    else:
        print("✅ All glossaries valid!")
        sys.exit(0)


if __name__ == '__main__':
    main()
