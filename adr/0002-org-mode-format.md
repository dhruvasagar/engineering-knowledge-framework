+++
title = "ADR-0002: Org-mode as Primary Document Format"
description = "Decision to use Org-mode as the primary document format"
+++


:PROPERTIES:
:STATUS:   accepted
:DATE:     2026-07-27
:END:

# Context

The framework needed a document format with:

- Rich structure (headings, lists, tables, code blocks).
- Plain-text readability without rendering tools.
- Good diff and merge behavior for collaborative editing.
- Machine-parseability for AI consumption and tooling.
- Support for cross-references and hyperlinks.
- Long-term stability as a format.

Common alternatives considered include Markdown, AsciiDoc,
reStructuredText, and LaTeX.

# Decision

Use ***Org-mode*** (plain text with `.org` extension) as the primary
document format for all framework documents.

Org-mode provides:

- Structured headings with native folding and navigation.
- Rich tables with column alignment and formulas.
- Inline code blocks with language annotation.
- Native hyperlink syntax for cross-references.
- Metadata via `#+KEY: VALUE` directives.
- Property drawers for structured data.
- Export to HTML, PDF, and other formats.
- Mature tooling ecosystem (Emacs, editors, parsers).

# Consequences

## Positive

- Plain-text format is universally readable and version-control
  friendly.
- Heading structure is machine-parseable for search and knowledge
  graphs.
- Cross-references are explicit and verifiable by tooling.
- Tables render well in both raw text and exported formats.
- Metadata provides a standardized way to describe documents.
- Format is stable and unlikely to become obsolete.

## Negative

- Less familiar to engineers accustomed to Markdown.
- Org-mode rendering varies across editors and platforms.
- Some AI systems have stronger training on Markdown than Org-mode.
- Fewer CI/CD tools natively understand Org-mode compared to Markdown.

# Alternatives Considered

## Markdown (.md)

Widely familiar, excellent AI training coverage, broad tooling support.

Rejected because Markdown lacks native table support, has inconsistent
implementations across parsers, and does not provide structured metadata
directives. Also used for `CLAUDE.md` by convention for AI instructions,
so using org for knowledge documents provides clear separation.

## AsciiDoc (.adoc)

Powerful, well-structured, good for technical documentation.

Rejected because it is less widely known than Org-mode or Markdown,
and has a more verbose syntax for common constructs.

## reStructuredText (.rst)

Standard for Python ecosystem documentation.

Rejected because it is tightly coupled to Python tooling and less
familiar to engineers outside that ecosystem.

# References

- [Software Architecture Handbook](../handbooks/architecture/README/)
- [Style Guide](../STYLE_GUIDE/)
