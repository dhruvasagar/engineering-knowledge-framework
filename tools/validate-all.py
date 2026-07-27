#!/usr/bin/env python3
"""
Validation Runner — Run all validation tools.

Usage:
    python3 tools/validate-all.py          # Run all validators
    python3 tools/validate-all.py --quiet  # Only show failures
"""

import subprocess
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
VALIDATORS = [
    ('🔗  Links',        'validate-links.py'),
    ('📝  Style',        'validate-style.py'),
    ('📖  Glossary',     'validate-glossary.py'),
    ('📑  TOC',          'validate-toc.py'),
]


def run_validator(name, script, quiet=False):
    """Run a single validator and return success/failure."""
    script_path = TOOLS_DIR / script
    if not quiet:
        print(f"\n{'='*50}")
        print(f" {name}")
        print(f"{'='*50}")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True, text=True
    )

    if quiet:
        if result.returncode != 0:
            print(f"\n❌ {name}")
            # Show just the error lines
            for line in result.stdout.split('\n'):
                if '❌' in line or '  ' in line.strip() and line.strip():
                    print(f"  {line.strip()}")
            for line in result.stderr.split('\n'):
                if line.strip():
                    print(f"  {line.strip()}")
    else:
        print(result.stdout)
        if result.stderr:
            print(result.stderr)

    return result.returncode == 0


def main():
    quiet = '--quiet' in sys.argv
    exit_code = 0

    print("🔍 Engineering Knowledge Framework — Validation Suite")
    print(f"   {len(VALIDATORS)} checks to run\n")

    for name, script in VALIDATORS:
        if not run_validator(name, script, quiet):
            exit_code = 1

    print(f"\n{'='*50}")
    if exit_code == 0:
        print("✅ All validators passed!")
    else:
        print("❌ Some validators failed — see above for details.")

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
