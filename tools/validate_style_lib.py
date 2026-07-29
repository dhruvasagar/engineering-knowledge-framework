#!/usr/bin/env python3
"""
Style validation rules for the Engineering Knowledge Framework.

This module holds the rules as pure functions so they can be unit
tested. `validate-style.py` is the CLI wrapper around it.

Every rule has the same shape:

    rule(content: str) -> list[str]

returning human-readable error strings, empty when the document passes.

Historical note: the original validator carried org-mode rules after the
repository migrated to Markdown. Its heading regex (`^\\*+\\s`) could
never match a Markdown `#`, and two of its rules returned an empty list
unconditionally, so it reported success across 302 files while checking
only filenames. Every rule here has a test, including a regression test
for that failure.
"""

import re

# --- Document taxonomy -----------------------------------------------------

DOCUMENT_TYPES = {
    'handbook', 'guide', 'playbook', 'checklist', 'template',
    'reference', 'glossary', 'learning-path', 'adr', 'rfc',
    'prompt', 'governance',
}

CAPABILITIES = {
    'engineering', 'architecture', 'rails', 'security', 'quality',
    'accessibility', 'ai', 'governance',
}

STATUSES = {'draft', 'published', 'deprecated'}

REQUIRED_FRONTMATTER = ('title', 'description', 'type', 'capability',
                        'status', 'last_reviewed')

# --- Patterns --------------------------------------------------------------

FENCE = re.compile(r'^(\s*)(`{3,})(.*)$')
HEADING = re.compile(r'^(#{1,6})\s+(\S.*)$')
DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')

# Org-mode constructs that should not survive the Markdown migration.
ORG_KEYWORD = re.compile(r'^#\+[A-Z_]+:')
ORG_LINK = re.compile(r'\[\[[^\]]*\]\[[^\]]*\]\]')
ORG_VERBATIM = re.compile(r'(?<![\w=])=[^\s=](?:[^=\n]*[^\s=])?=(?![\w=])')

# URLs mangled by the migration, where `/` was replaced with `*`.
MANGLED_URL = re.compile(r'https?:(?:\*/|/\*|\*\*)')

# CJK and Cyrillic ranges. The framework is written in English; a run of
# these characters means untranslated text reached the document.
STRAY_SCRIPT = re.compile(r'[぀-ヿ一-鿿Ѐ-ӿ]+')


def split_frontmatter(content):
    """Return (frontmatter_text_or_None, body, body_start_line).

    Frontmatter is a YAML block delimited by `---` at the very start of
    the file. `body_start_line` is 1-indexed and lets callers report
    line numbers against the original document.
    """
    lines = content.split('\n')
    if not lines or lines[0].strip() != '---':
        return None, content, 1
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            return '\n'.join(lines[1:i]), '\n'.join(lines[i + 1:]), i + 2
    return None, content, 1


def parse_frontmatter(text):
    """Parse the flat subset of YAML the framework's schema uses.

    Supports `key: scalar` and `key: [a, b, c]`. Deliberately minimal so
    the tooling keeps its no-external-dependency property.
    """
    data = {}
    for line in text.split('\n'):
        line = line.rstrip()
        if not line or line.lstrip().startswith('#'):
            continue
        if ':' not in line:
            continue
        key, _, value = line.partition(':')
        key = key.strip()
        value = value.strip()
        if value.startswith('[') and value.endswith(']'):
            inner = value[1:-1].strip()
            items = [v.strip().strip('"\'') for v in inner.split(',')] if inner else []
            data[key] = [v for v in items if v]
        else:
            data[key] = value.strip('"\'')
    return data


def iter_lines_outside_fences(content):
    """Yield (line_number, line) for lines that are not inside a code block.

    Rules that inspect prose must not fire on code samples. The Style
    Guide, for instance, shows deliberately wrong Markdown inside fences.
    """
    in_fence = False
    fence_marker = None
    for n, line in enumerate(content.split('\n'), 1):
        m = FENCE.match(line)
        if m:
            marker = m.group(2)
            if not in_fence:
                in_fence, fence_marker = True, marker
            elif marker.startswith(fence_marker):
                in_fence, fence_marker = False, None
            continue
        if not in_fence:
            yield n, line


# --- Rules -----------------------------------------------------------------

def check_frontmatter(content):
    """Every document declares the metadata retrieval and compilation need."""
    text, _, _ = split_frontmatter(content)
    if text is None:
        return ['Line 1: Missing YAML frontmatter block']

    data = parse_frontmatter(text)
    errors = []

    for field in REQUIRED_FRONTMATTER:
        if not data.get(field):
            errors.append(f'Frontmatter: missing required field `{field}`')

    if (t := data.get('type')) and t not in DOCUMENT_TYPES:
        errors.append(
            f'Frontmatter: unknown type `{t}` '
            f'(expected one of: {", ".join(sorted(DOCUMENT_TYPES))})'
        )
    if (c := data.get('capability')) and c not in CAPABILITIES:
        errors.append(
            f'Frontmatter: unknown capability `{c}` '
            f'(expected one of: {", ".join(sorted(CAPABILITIES))})'
        )
    if (s := data.get('status')) and s not in STATUSES:
        errors.append(
            f'Frontmatter: unknown status `{s}` '
            f'(expected one of: {", ".join(sorted(STATUSES))})'
        )
    if (d := data.get('last_reviewed')) and not DATE.match(str(d)):
        errors.append(f'Frontmatter: last_reviewed `{d}` is not YYYY-MM-DD')
    if (tags := data.get('tags')) is not None and not isinstance(tags, list):
        errors.append('Frontmatter: tags must be a list, e.g. [a, b]')

    return errors


def check_headings(content):
    """Heading levels must not skip (`#` straight to `###`)."""
    _, body, offset = split_frontmatter(content)
    errors = []
    prev = 0
    for n, line in iter_lines_outside_fences(body):
        m = HEADING.match(line)
        if not m:
            continue
        level = len(m.group(1))
        if prev and level > prev + 1:
            errors.append(
                f'Line {n + offset - 1}: Skipped heading level '
                f'({prev} → {level}): {line.strip()}'
            )
        prev = level
    return errors


def check_code_fences(content):
    """Fences must be balanced, tagged with a language, and never nested.

    An untagged fence loses syntax highlighting on the site and prevents
    agents from extracting runnable examples. A nested fence silently
    closes the outer block, truncating the document when rendered.
    """
    errors = []
    stack = []  # (line_number, marker)
    for n, line in enumerate(content.split('\n'), 1):
        m = FENCE.match(line)
        if not m:
            continue
        marker, info = m.group(2), m.group(3).strip()

        if not stack:
            if not info:
                errors.append(
                    f'Line {n}: Code fence has no language tag '
                    f'(use ```text if there is no better fit)'
                )
            stack.append((n, marker))
            continue

        open_line, open_marker = stack[-1]

        # A shorter fence inside a longer one is literal content, not a
        # delimiter. This is how a prompt template legitimately embeds a
        # code sample: open the outer block with ````.
        if len(marker) < len(open_marker):
            continue

        if info:
            errors.append(
                f'Line {n}: Nested code fence ```{info} inside the block '
                f'opened on line {open_line} — this closes the outer block '
                f'early. Open the outer block with a longer fence (````).'
            )
        stack.pop()

    for open_line, _ in stack:
        errors.append(f'Line {open_line}: Unclosed code fence')
    return errors


def check_org_residue(content):
    """Org-mode syntax must not survive the migration to Markdown.

    Inline code spans are exempt: the Style Guide and this project's own
    roadmap legitimately quote org syntax when explaining what not to
    write.
    """
    errors = []
    for n, raw in iter_lines_outside_fences(content):
        line = re.sub(r'`[^`\n]*`', lambda m: ' ' * len(m.group(0)), raw)
        if ORG_KEYWORD.match(line.strip()):
            errors.append(f'Line {n}: org-mode keyword: {line.strip()}')
        if ORG_LINK.search(line):
            errors.append(
                f'Line {n}: org-mode link syntax [[target][text]] — '
                f'use [text](target): {raw.strip()}'
            )
        if ORG_VERBATIM.search(line):
            errors.append(
                f'Line {n}: org-mode verbatim =markup= — '
                f'use `backticks`: {raw.strip()}'
            )
    return errors


def _table_cells(line):
    """Split a table row into cells, ignoring pipes inside inline code."""
    masked = re.sub(r'`[^`\n]*`', lambda m: '\x00' * len(m.group(0)), line)
    masked = masked.replace(r'\|', '\x01\x01')
    stripped = masked.strip()
    if stripped.startswith('|'):
        stripped = stripped[1:]
    if stripped.endswith('|'):
        stripped = stripped[:-1]
    return stripped.split('|')


SEPARATOR_CELL = re.compile(r'^\s*:?-{3,}:?\s*$')


def _is_separator_row(line):
    cells = _table_cells(line)
    return bool(cells) and all(SEPARATOR_CELL.match(c) for c in cells)


def check_tables(content):
    """Tables follow the Style Guide's structure rules.

    The org-to-Markdown migration produced separator rows using `+`
    between columns, which is valid org and invalid Markdown — it renders
    as a data row rather than a separator, silently destroying the table.
    """
    errors = []
    rows = []  # (line_number, line)

    def flush():
        if len(rows) < 2:
            rows.clear()
            return

        start_line = rows[0][0]
        header_cells = _table_cells(rows[0][1])
        expected = len(header_cells)

        sep_line_no, sep_line = rows[1]
        if not _is_separator_row(sep_line):
            if '+' in sep_line and re.search(r'-\s*\+|\+\s*-', sep_line):
                errors.append(
                    f'Line {sep_line_no}: Table separator row uses `+` between '
                    f'columns (org-mode style) — use `|`: {sep_line.strip()}'
                )
            elif re.search(r'-{1,2}(?!-)', sep_line) and set(
                    sep_line.replace('|', '').replace(' ', '')) <= set('-:'):
                errors.append(
                    f'Line {sep_line_no}: Table separator cells need three or '
                    f'more dashes: {sep_line.strip()}'
                )
            else:
                errors.append(
                    f'Line {start_line}: Table has no separator row — the '
                    f'second row must be `|---|---|`'
                )
        else:
            sep_cells = _table_cells(sep_line)
            if len(sep_cells) != expected:
                errors.append(
                    f'Line {sep_line_no}: Table separator has {len(sep_cells)} '
                    f'column(s) but the header has {expected}'
                )

        for line_no, line in rows[2:]:
            if _is_separator_row(line):
                errors.append(
                    f'Line {line_no}: Extra separator row inside the table '
                    f'body — only one separator is allowed, after the header'
                )
                continue
            count = len(_table_cells(line))
            if count != expected:
                errors.append(
                    f'Line {line_no}: Table row has {count} column(s) but the '
                    f'header has {expected}: {line.strip()[:70]}'
                )
        rows.clear()

    for n, line in iter_lines_outside_fences(content):
        if line.strip().startswith('|'):
            rows.append((n, line))
        else:
            flush()
    flush()

    return errors


def check_mangled_urls(content):
    """Catch URLs whose slashes were replaced with `*` during migration."""
    errors = []
    for n, line in enumerate(content.split('\n'), 1):
        if MANGLED_URL.search(line):
            errors.append(
                f'Line {n}: URL has `*` where `/` belongs '
                f'(migration damage): {line.strip()}'
            )
    return errors


def check_stray_script(content):
    """Catch untranslated text left in an English document."""
    errors = []
    for n, line in enumerate(content.split('\n'), 1):
        for m in STRAY_SCRIPT.finditer(line):
            errors.append(
                f'Line {n}: Non-English text `{m.group(0)}` in an English '
                f'document: {line.strip()[:80]}'
            )
    return errors


CONTENT_RULES = (
    check_frontmatter,
    check_headings,
    check_code_fences,
    check_tables,
    check_org_residue,
    check_mangled_urls,
    check_stray_script,
)


def check_filename(rel_path, stem):
    """Filenames are lowercase-with-dashes, except conventional roots."""
    allowed_uppercase = {
        'README', 'index', 'CHANGELOG', 'CLAUDE', 'TOC', 'STYLE_GUIDE',
        'WRITING_PRINCIPLES', 'CONTRIBUTING', 'DOCUMENT_TYPES',
        'ARCHITECTURE', 'STRATEGY', 'ROADMAP',
    }
    errors = []
    if stem in allowed_uppercase:
        return errors
    if ' ' in stem:
        errors.append(f'Filename contains spaces: {rel_path}')
    if stem != stem.lower():
        errors.append(f'Filename should be lowercase: {rel_path}')
    return errors


def validate_document(rel_path, stem, content):
    """Run every rule against one document."""
    errors = []
    for rule in CONTENT_RULES:
        errors.extend(rule(content))
    errors.extend(check_filename(rel_path, stem))
    return errors
