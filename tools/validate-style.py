#!/usr/bin/env python3
"""
Style Validator — Check documents against style-guide.md rules.

Validates:
- Required YAML frontmatter (title, description, type, capability,
  status, last_reviewed) with values drawn from the document taxonomy
- No skipped heading levels
- Every code fence carries a language tag, is balanced, and is not nested
- No org-mode residue (#+KEYWORD, =verbatim=, [[target][text]])
- No URLs mangled by the org-to-Markdown migration
- File naming conventions (lowercase-with-dashes)

The rules live in validate_style_lib.py and are unit tested by
test_validate_style.py.

Usage:
    python3 tools/validate-style.py
    python3 tools/validate-style.py --rule code_fences   # run one rule
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_style_lib import CONTENT_RULES, check_filename  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent

# Directories that hold generated output, working documents or the
# pre-migration archive — none of them are authored knowledge.
SKIP_DIRS = {'.git', '.venv', '__pycache__', '.org-backup', 'node_modules',
             'site', 'tools', 'docs'}


def collect_documents():
    """Collect all authored .md documents."""
    documents = []
    for root, dirs, files in os.walk(REPO_ROOT):
        rel = Path(root).relative_to(REPO_ROOT)
        if any(p in SKIP_DIRS or p.startswith('.') for p in rel.parts):
            continue
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
        for f in files:
            if f.endswith('.md'):
                documents.append(Path(root) / f)
    return sorted(documents)


def main():
    only = None
    if '--rule' in sys.argv:
        only = sys.argv[sys.argv.index('--rule') + 1]

    rules = CONTENT_RULES
    if only:
        rules = tuple(r for r in CONTENT_RULES if r.__name__ == f'check_{only}')
        if not rules:
            names = ', '.join(r.__name__.removeprefix('check_') for r in CONTENT_RULES)
            print(f'Unknown rule: {only}\nAvailable: {names}')
            sys.exit(2)

    print('📝 Style Validator')
    print(f'   Scanning {REPO_ROOT}...\n')

    documents = collect_documents()
    all_errors = []

    for filepath in documents:
        rel_path = filepath.relative_to(REPO_ROOT)
        content = filepath.read_text(encoding='utf-8')

        errors = []
        for rule in rules:
            errors.extend(rule(content))
        if not only:
            errors.extend(check_filename(str(rel_path), filepath.stem))

        if errors:
            all_errors.append((rel_path, errors))

    print(f'   Checked {len(documents)} files against {len(rules)} rule(s)\n')

    if all_errors:
        total = sum(len(e) for _, e in all_errors)
        print(f'❌ {total} style issue(s) in {len(all_errors)} file(s):\n')
        for rel_path, errors in all_errors:
            print(f'   {rel_path}:')
            for err in errors:
                print(f'     - {err}')
            print()
        sys.exit(1)

    print('✅ All style checks pass!')
    sys.exit(0)


if __name__ == '__main__':
    main()
