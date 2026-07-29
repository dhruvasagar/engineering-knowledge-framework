#!/usr/bin/env python3
"""
Tests for the style validation rules.

Run with:
    python3 tools/test_validate_style.py

Deliberately uses unittest from the standard library so the tooling keeps
its no-external-dependency property and runs anywhere CI does.
"""

import unittest

from validate_style_lib import (
    check_code_fences,
    check_filename,
    check_frontmatter,
    check_headings,
    check_mangled_urls,
    check_org_residue,
    check_stray_script,
    check_tables,
    parse_frontmatter,
    split_frontmatter,
    validate_document,
)

VALID_FRONTMATTER = """---
title: Service Objects
description: Encapsulating a single business operation in a dedicated class.
type: guide
capability: rails
status: published
tags: [patterns, refactoring]
last_reviewed: 2026-07-29
---
"""


def doc(body, frontmatter=VALID_FRONTMATTER):
    return frontmatter + '\n' + body


class TestFrontmatterParsing(unittest.TestCase):

    def test_splits_frontmatter_from_body(self):
        text, body, offset = split_frontmatter(doc('# Purpose\n'))
        self.assertIn('title: Service Objects', text)
        self.assertIn('# Purpose', body)
        self.assertEqual(offset, 10)

    def test_returns_none_when_absent(self):
        text, body, offset = split_frontmatter('# Purpose\n')
        self.assertIsNone(text)
        self.assertEqual(body, '# Purpose\n')
        self.assertEqual(offset, 1)

    def test_unterminated_frontmatter_is_not_frontmatter(self):
        text, _, _ = split_frontmatter('---\ntitle: X\n# Purpose\n')
        self.assertIsNone(text)

    def test_parses_scalars_and_lists(self):
        data = parse_frontmatter(
            'title: Service Objects\ntags: [patterns, refactoring]\n'
        )
        self.assertEqual(data['title'], 'Service Objects')
        self.assertEqual(data['tags'], ['patterns', 'refactoring'])

    def test_parses_empty_list(self):
        self.assertEqual(parse_frontmatter('tags: []')['tags'], [])

    def test_value_containing_colon_is_preserved(self):
        data = parse_frontmatter('description: Use AI: carefully.')
        self.assertEqual(data['description'], 'Use AI: carefully.')


class TestFrontmatterRule(unittest.TestCase):

    def test_valid_frontmatter_passes(self):
        self.assertEqual(check_frontmatter(doc('# Purpose\n')), [])

    def test_missing_frontmatter_is_reported(self):
        errors = check_frontmatter('# Purpose\n')
        self.assertEqual(len(errors), 1)
        self.assertIn('Missing YAML frontmatter', errors[0])

    def test_missing_required_field_is_reported(self):
        fm = VALID_FRONTMATTER.replace(
            'description: Encapsulating a single business operation in a dedicated class.\n',
            '',
        )
        errors = check_frontmatter(doc('# Purpose\n', fm))
        self.assertTrue(any('`description`' in e for e in errors))

    def test_empty_required_field_is_reported(self):
        fm = VALID_FRONTMATTER.replace('title: Service Objects', 'title:')
        errors = check_frontmatter(doc('# Purpose\n', fm))
        self.assertTrue(any('`title`' in e for e in errors))

    def test_unknown_type_is_reported(self):
        fm = VALID_FRONTMATTER.replace('type: guide', 'type: blogpost')
        errors = check_frontmatter(doc('# Purpose\n', fm))
        self.assertTrue(any('unknown type' in e for e in errors))

    def test_unknown_capability_is_reported(self):
        fm = VALID_FRONTMATTER.replace('capability: rails', 'capability: django')
        errors = check_frontmatter(doc('# Purpose\n', fm))
        self.assertTrue(any('unknown capability' in e for e in errors))

    def test_unknown_status_is_reported(self):
        fm = VALID_FRONTMATTER.replace('status: published', 'status: wip')
        errors = check_frontmatter(doc('# Purpose\n', fm))
        self.assertTrue(any('unknown status' in e for e in errors))

    def test_malformed_review_date_is_reported(self):
        fm = VALID_FRONTMATTER.replace(
            'last_reviewed: 2026-07-29', 'last_reviewed: July 2026'
        )
        errors = check_frontmatter(doc('# Purpose\n', fm))
        self.assertTrue(any('not YYYY-MM-DD' in e for e in errors))


class TestHeadings(unittest.TestCase):

    def test_sequential_levels_pass(self):
        self.assertEqual(
            check_headings(doc('# Purpose\n\n## Detail\n\n### Deeper\n')), []
        )

    def test_skipped_level_is_reported(self):
        errors = check_headings(doc('# Purpose\n\n### Too deep\n'))
        self.assertEqual(len(errors), 1)
        self.assertIn('Skipped heading level (1 → 3)', errors[0])

    def test_returning_to_a_shallower_level_is_fine(self):
        body = '# One\n\n## Two\n\n### Three\n\n# Back to one\n\n## Two again\n'
        self.assertEqual(check_headings(doc(body)), [])

    def test_headings_inside_code_fences_are_ignored(self):
        body = '# Purpose\n\n```text\n### Not a real heading\n```\n'
        self.assertEqual(check_headings(doc(body)), [])

    def test_blank_lines_do_not_reset_tracking(self):
        # The original validator reset its level counter on every blank
        # line, which made the rule unable to fire on normal prose.
        self.assertEqual(len(check_headings(doc('# Purpose\n\n\n### Deep\n'))), 1)

    def test_line_numbers_account_for_frontmatter(self):
        # Frontmatter occupies lines 1-9, doc() adds a blank line 10,
        # so `# Purpose` is line 11 and `### Deep` is line 13.
        errors = check_headings(doc('# Purpose\n\n### Deep\n'))
        self.assertIn('Line 13', errors[0])

    def test_org_headings_are_not_treated_as_markdown(self):
        # Regression: the original regex was `^(\*+)\s`, which matched
        # org-mode headings and never matched Markdown ones.
        self.assertEqual(check_headings(doc('* One\n\n*** Three\n')), [])


class TestCodeFences(unittest.TestCase):

    def test_tagged_balanced_fence_passes(self):
        self.assertEqual(check_code_fences(doc('```ruby\nx = 1\n```\n')), [])

    def test_untagged_fence_is_reported(self):
        errors = check_code_fences(doc('```\nx = 1\n```\n'))
        self.assertEqual(len(errors), 1)
        self.assertIn('no language tag', errors[0])

    def test_longer_outer_fence_may_contain_a_shorter_one(self):
        # A prompt template embedding a code sample. Per CommonMark only
        # a fence at least as long as the opener closes the block, so
        # this is the correct way to nest.
        body = '````text\nPrompt:\n```ruby\nx = 1\n```\n````\n'
        self.assertEqual(check_code_fences(doc(body)), [])

    def test_equal_length_nested_fence_is_reported(self):
        body = '```text\nPrompt:\n```ruby\nx = 1\n```\n'
        errors = check_code_fences(doc(body))
        self.assertTrue(any('Nested code fence' in e for e in errors))

    def test_nested_fence_names_the_outer_block(self):
        body = '```text\nPrompt:\n```ruby\nx = 1\n```\n'
        errors = check_code_fences(doc(body))
        self.assertTrue(any('opened on line 11' in e for e in errors))

    def test_unclosed_fence_is_reported(self):
        errors = check_code_fences(doc('```ruby\nx = 1\n'))
        self.assertTrue(any('Unclosed code fence' in e for e in errors))

    def test_multiple_blocks_pass(self):
        body = '```ruby\nx = 1\n```\n\ntext\n\n```bash\nls\n```\n'
        self.assertEqual(check_code_fences(doc(body)), [])

    def test_indented_fence_in_a_list_passes(self):
        body = '- Item:\n\n  ```ruby\n  x = 1\n  ```\n'
        self.assertEqual(check_code_fences(doc(body)), [])


class TestTables(unittest.TestCase):

    def test_well_formed_table_passes(self):
        body = (
            '| Principle      | Description                        |\n'
            '|----------------|------------------------------------|\n'
            '| Keep it simple | Prefer simple over clever designs. |\n'
        )
        self.assertEqual(check_tables(doc(body)), [])

    def test_minimal_three_dash_separator_passes(self):
        body = '| A | B |\n| --- | --- |\n| 1 | 2 |\n'
        self.assertEqual(check_tables(doc(body)), [])

    def test_alignment_colons_pass(self):
        body = '| A | B |\n|:---|---:|\n| 1 | 2 |\n'
        self.assertEqual(check_tables(doc(body)), [])

    def test_org_style_plus_separator_is_reported(self):
        body = '| Pro | Con |\n|-------+-------|\n| Testable | Complex |\n'
        errors = check_tables(doc(body))
        self.assertTrue(any('org-mode style' in e for e in errors))

    def test_too_few_dashes_is_reported(self):
        body = '| A | B |\n|--|--|\n| 1 | 2 |\n'
        errors = check_tables(doc(body))
        self.assertTrue(any('three or more dashes' in e for e in errors))

    def test_missing_separator_row_is_reported(self):
        body = '| A | B |\n| 1 | 2 |\n| 3 | 4 |\n'
        errors = check_tables(doc(body))
        self.assertTrue(any('no separator row' in e for e in errors))

    def test_extra_separator_mid_table_is_reported(self):
        body = (
            '| Type | Description |\n'
            '|------|-------------|\n'
            '| Unit | Fast tests. |\n'
            '|------|-------------|\n'
            '| E2E  | Slow tests. |\n'
        )
        errors = check_tables(doc(body))
        self.assertTrue(any('Extra separator row' in e for e in errors))

    def test_ragged_column_count_is_reported(self):
        body = '| A | B |\n|---|---|\n| 1 | 2 | 3 |\n'
        errors = check_tables(doc(body))
        self.assertTrue(any('3 column(s) but the header has 2' in e
                            for e in errors))

    def test_separator_column_count_mismatch_is_reported(self):
        body = '| A | B | C |\n|---|---|\n| 1 | 2 | 3 |\n'
        errors = check_tables(doc(body))
        self.assertTrue(any('separator has 2 column(s)' in e for e in errors))

    def test_wrapped_cell_continuation_row_passes(self):
        # A long cell continued on the next row with an empty first cell.
        body = (
            '| Exceptions | The error is unexpected or cannot be handled |\n'
            '|------------|---------------------------------------------|\n'
            '| Result     | You want type-safe error handling without    |\n'
            '|            | exceptions.                                 |\n'
        )
        self.assertEqual(check_tables(doc(body)), [])

    def test_pipe_inside_inline_code_is_not_a_column_break(self):
        body = '| Syntax | Meaning |\n|---|---|\n| `a \\| b` | union |\n'
        self.assertEqual(check_tables(doc(body)), [])

    def test_tables_inside_code_fences_are_ignored(self):
        body = '```markdown\n| Pro | Con |\n|-----+-----|\n| a | b |\n```\n'
        self.assertEqual(check_tables(doc(body)), [])

    def test_two_tables_separated_by_prose_are_checked_independently(self):
        body = (
            '| A | B |\n|---|---|\n| 1 | 2 |\n\n'
            'Prose between tables.\n\n'
            '| C | D |\n| 1 | 2 |\n'
        )
        errors = check_tables(doc(body))
        self.assertEqual(len(errors), 1)
        self.assertIn('no separator row', errors[0])


class TestOrgResidue(unittest.TestCase):

    def test_clean_markdown_passes(self):
        body = '# Purpose\n\nSee [the guide](./guide.md) and `code`.\n'
        self.assertEqual(check_org_residue(doc(body)), [])

    def test_org_link_is_reported(self):
        errors = check_org_residue(doc('- [[https://example.com][Example]]\n'))
        self.assertTrue(any('org-mode link syntax' in e for e in errors))

    def test_org_keyword_is_reported(self):
        errors = check_org_residue(doc('#+TITLE: Something\n'))
        self.assertTrue(any('org-mode keyword' in e for e in errors))

    def test_org_verbatim_is_reported(self):
        errors = check_org_residue(doc('Use =-= for bullet lists.\n'))
        self.assertTrue(any('org-mode verbatim' in e for e in errors))

    def test_equals_in_prose_is_not_flagged(self):
        body = 'Set x = 1 and y = 2.\n\nUse `a == b` for comparison.\n'
        self.assertEqual(check_org_residue(doc(body)), [])

    def test_org_syntax_quoted_in_inline_code_is_allowed(self):
        # Documenting what not to write is legitimate.
        body = 'Detect `=verbatim=` markup and `[[target][text]]` links.\n'
        self.assertEqual(check_org_residue(doc(body)), [])

    def test_unquoted_residue_beside_quoted_residue_is_still_reported(self):
        body = 'Use =-= for bullets, not `=verbatim=`.\n'
        errors = check_org_residue(doc(body))
        self.assertTrue(any('org-mode verbatim' in e for e in errors))

    def test_residue_inside_code_fences_is_ignored(self):
        body = '```text\n#+TITLE: Example of what not to write\n```\n'
        self.assertEqual(check_org_residue(doc(body)), [])


class TestMangledUrls(unittest.TestCase):

    def test_clean_url_passes(self):
        self.assertEqual(
            check_mangled_urls(doc('[WCAG](https://www.w3.org/TR/WCAG22/)\n')), []
        )

    def test_star_after_scheme_is_reported(self):
        errors = check_mangled_urls(doc('[[https:*/www.w3.org*TR*][WCAG]]\n'))
        self.assertTrue(any('migration damage' in e for e in errors))

    def test_star_inside_scheme_slashes_is_reported(self):
        errors = check_mangled_urls(doc('[[https:/*inclusive-components.design/]]\n'))
        self.assertTrue(any('migration damage' in e for e in errors))


class TestStrayScript(unittest.TestCase):

    def test_english_prose_passes(self):
        self.assertEqual(check_stray_script(doc('A process that is error-prone.\n')), [])

    def test_typographic_characters_pass(self):
        body = 'Cost — benefit. Arrows ↓ → and box drawing ├── are fine.\n'
        self.assertEqual(check_stray_script(doc(body)), [])

    def test_untranslated_text_is_reported(self):
        errors = check_stray_script(doc('error-prone and容易遗漏.\n'))
        self.assertTrue(any('Non-English text' in e for e in errors))


class TestFilename(unittest.TestCase):

    def test_lowercase_dashed_name_passes(self):
        self.assertEqual(check_filename('guides/rails/service-objects.md',
                                        'service-objects'), [])

    def test_readme_is_allowed(self):
        self.assertEqual(check_filename('guides/README.md', 'README'), [])

    def test_uppercase_is_reported(self):
        errors = check_filename('guides/ServiceObjects.md', 'ServiceObjects')
        self.assertTrue(any('lowercase' in e for e in errors))

    def test_spaces_are_reported(self):
        errors = check_filename('guides/service objects.md', 'service objects')
        self.assertTrue(any('spaces' in e for e in errors))


class TestValidateDocument(unittest.TestCase):

    def test_clean_document_passes_every_rule(self):
        body = (
            '# Purpose\n\nA guide.\n\n## Example\n\n'
            '```ruby\nx = 1\n```\n\n'
            '# Related Documents\n\n- [Handbook](../handbook.md)\n'
        )
        self.assertEqual(
            validate_document('guides/rails/service-objects.md',
                              'service-objects', doc(body)),
            [],
        )

    def test_a_document_with_no_defects_but_no_frontmatter_still_fails(self):
        # Regression: the old validator passed 302 files unconditionally.
        errors = validate_document('guides/rails/service-objects.md',
                                   'service-objects', '# Purpose\n\nText.\n')
        self.assertTrue(errors)


if __name__ == '__main__':
    unittest.main(verbosity=2)
