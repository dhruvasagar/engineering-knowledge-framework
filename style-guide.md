# Purpose

This document defines the writing and formatting standards for the
Engineering Knowledge Framework.

Consistency makes engineering knowledge easier to read, maintain,
discover and evolve.

The style guide exists to ensure every document feels like it was written
by a single author, regardless of how many contributors participate.

This document focuses on **how** knowledge should be written.

The philosophy behind the framework is documented in
[CLAUDE.md](./CLAUDE.md) and
[Strategy](./strategy.md).

# AI-First Writing

The Engineering Knowledge Framework is designed to be consumed by both
humans and AI systems.

Good engineering documentation naturally serves both audiences.

Documents should therefore maximize:

- Human readability.
- Machine readability.
- Semantic clarity.
- Searchability.
- Discoverability.
- Long-term maintainability.

AI-friendly writing does not mean writing differently for humans.

Instead, it means writing with sufficient structure, explicitness and
consistency that both humans and AI systems can accurately interpret the
knowledge.

# Writing Principles

Every document should strive to be:

- Timeless.
- Modular.
- Explicit.
- Reusable.
- Well connected.
- Easy to navigate.
- Easy to review.
- Easy to maintain.

Prefer clarity over cleverness.

Prefer simplicity over completeness.

Prefer principles over implementation details.

# File Naming

| Convention         | Example                           | Rule                                               |
|--------------------|-----------------------------------|----------------------------------------------------|
| Lowercase          | `handbooks/rails/README.md`       | No capital letters in filenames or directory names |
| Hyphen-separated   | `service-objects.md`              | Use hyphens, never spaces or underscores           |
| Markdown extension | `testing-strategies.md`           | All documents use `.md` extension                  |
| Directory index    | `handbooks/engineering/README.md` | Each directory has a README.md as its index        |

Choose descriptive names.

Avoid abbreviations unless they are universally understood.

# Document Structure

Documents should follow a logical progression.

General guidance:

1. Purpose
2. Background
3. Principles
4. Main Content
5. Examples
6. References

Specific document structures are defined in
[Document Types](./document-types.md).

# Single Responsibility

Every document should answer one primary question.

Examples:

| Question                  | Document Type |
|---------------------------|---------------|
| Why?                      | Handbook      |
| How does it work?         | Guide         |
| How do I perform it?      | Playbook      |
| Did I finish everything?  | Checklist     |
| Where do I start?         | Template      |
| What does this mean?      | Glossary      |
| What should I learn next? | Learning Path |

If a document attempts to answer several unrelated questions, split it
into multiple documents.

Smaller documents are easier to maintain and significantly improve AI
retrieval.

# Headings

Use descriptive headings.

Avoid vague titles.

Good:

- Service Object Lifecycle
- Dependency Injection
- Pull Request Review Workflow

Avoid:

- Lifecycle
- Details
- Notes
- Miscellaneous

A heading should remain meaningful when viewed independently in search
results or a table of contents.

Do not skip heading levels. For example, do not jump from `##` to `####`
without `###` in between.

Prefer three heading levels or fewer whenever practical.

# Voice and Tone

Write for experienced engineers.

Assume competence.

Use:

- Active voice.
- Direct language.
- Declarative statements.
- Technical precision.

Avoid:

- Marketing language.
- Excessive adjectives.
- Unnecessary humour.
- Hedging.

Good:

> Controllers should remain thin.

Avoid:

> Controllers might perhaps benefit from being relatively small.

# Semantic Writing

Write so that each paragraph remains understandable in isolation.

Avoid ambiguous references.

Good:

> The Rails application loads configuration during initialization.

Avoid:

> It loads configuration.

Prefer explicit nouns over pronouns when ambiguity is possible.

State assumptions explicitly.

Do not rely on surrounding context.

# Context Independence

Engineering documents are often consumed through search or AI retrieval.

Readers may encounter only part of a document.

Whenever practical:

- Define important concepts.
- Avoid "as mentioned above".
- Avoid "the previous section".
- Prefer explicit links.

Good:

> See the
> [Rails Engineering Handbook](./handbooks/rails/README.md)
> for architectural principles.

# Timeless Writing

Prefer knowledge that remains valuable over implementation details that
change frequently.

Good:

- Controllers should remain thin.
- Prefer composition over inheritance.
- Minimize coupling.

Avoid:

- Rails 8.0.1 introduces...
- Ruby 3.4 changes...
- Current IDE behaviour...

Version-specific information belongs in references rather than
handbooks.

Explain:

- Why.
- Trade-offs.
- Decision criteria.

These age far more gracefully than implementation details.

# Canonical Sources

Every engineering concept should have a single authoritative source.

Other documents should reference that source rather than duplicate it.

Examples:

- Coding standards belong in the Handbook.
- Operational procedures belong in Playbooks.
- Definitions belong in the Glossary.

Duplication increases maintenance effort and causes knowledge to drift.

# Links

Prefer explicit links.

Every significant concept should be connected to related knowledge.

Good:

```
[Code Review Playbook](./playbooks/code-review/README.md)
```

Avoid:

> See the code review documentation.

# Knowledge Graph

The repository should evolve into a connected knowledge graph rather
than a collection of isolated documents.

Documents should both:

- Reference related knowledge.
- Be referenced by related knowledge.

Example:

```
Rails Handbook → Service Objects Guide → Code Review Playbook
```

Navigation should emphasize relationships rather than directory
structure.

# Lists

Use unordered lists (`-`) for collections.

Use ordered lists (`1.`) for sequences.

Keep nesting shallow.

Avoid deeply nested lists.

## Bullet Format

Use `-` for bullet list items, never `*`.

Correct:

- Item one.
- Item two.
  - Nested sub-item.

Incorrect:

- Item one.
- Item two.

## Checklist Format

Use `- [ ]` for checklist items.

Correct:

- [ ] Task to complete.
- [x] Completed task.

# Tables

Use markdown tables for structured information.

Tables are appropriate for:

- Comparisons.
- Decision matrices.
- Standards.
- Capability summaries.
- Configuration matrices.

Avoid using tables for layout.

## Format

Every table must follow this structure:

```
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
```

Rules:

- The header separator row uses `|---|` (three or more dashes between pipes).
- All rows must have the same number of columns.
- A blank line ends the table.

## Correct Example

```
| Principle      | Description                        |
|----------------|------------------------------------|
| Keep it simple | Prefer simple over clever designs. |
| Single purpose | One responsibility per module.     |
```

Rendered:

| Principle      | Description                        |
|----------------|------------------------------------|
| Keep it simple | Prefer simple over clever designs. |
| Single purpose | One responsibility per module.     |

## Multi-line Cells

Markdown does not support multi-line cells natively. For content that
needs multiple lines, use separate rows with the first column empty:

```
| Type | Speed | Notes                               |
|------|-------|-------------------------------------|
| Unit | Fast  | Isolated, single behaviour.         |
|      |       | Tests a single module in isolation. |
| E2E  | Slow  | Full stack, critical journeys only. |
```

Or use a list within a cell if the renderer supports it (most do not).
For complex multi-line content, prefer a definition list or bullet list
outside the table.

# Blockquotes

Use `>` for blockquotes.

Used for:

- Highlighting important principles.
- Showing good and bad examples.
- Excerpts from other documents.

Example:

> Controllers should remain thin. Move business logic into service
> objects or models.

# Code Blocks

Always specify the language for syntax highlighting.

Example:

```ruby
class User < ApplicationRecord
  has_many :posts
end
```

Prefer small examples.

Examples should demonstrate principles rather than complete
applications.

# Examples

Examples should be:

- Realistic.
- Minimal.
- Correct.
- Easy to understand.

When appropriate, include:

- Good examples.
- Bad examples.
- Before/after comparisons.

Examples are often the fastest way to teach engineering concepts.

# Cross References

Prefer links over repeated explanations.

If knowledge already exists elsewhere, reference it.

Every document should contribute to the repository's knowledge graph.

# Terminology

Use terminology consistently.

Define new terminology in the appropriate glossary.

Avoid introducing multiple names for the same concept.

Prefer:

- Pull Request
- Repository
- Capability
- Knowledge Artifact

Avoid unnecessary synonyms.

# AI Readability

Documents should optimize retrieval quality.

Prefer:

- Explicit language.
- Meaningful headings.
- Small focused sections.
- Defined terminology.
- Logical progression.
- Internal links.
- Single responsibility.

Avoid:

- Large monolithic documents.
- Ambiguous wording.
- Duplicate explanations.
- Excessively deep heading hierarchies.

Good documentation naturally improves AI performance.

# Continuous Evolution

Engineering knowledge evolves.

Improve existing documents before creating new ones whenever practical.

Documentation refactoring is encouraged.

Repository quality is more important than document count.

# Validation Checklist

Before committing a document, verify:

- [ ] Correct document type was used (handbook, guide, playbook, etc.).
- [ ] The document has a single responsibility.
- [ ] Headings are meaningful and descriptive.
- [ ] Heading levels do not skip (e.g., `##` to `####` without `###`).
- [ ] Terminology is consistent with the relevant glossary.
- [ ] Internal links are valid and use lowercase paths.
- [ ] Lists use `-` for bullets, not `*`.
- [ ] Checklists use `- [ ]` format.
- [ ] Table formatting is correct and consistent.
- [ ] Code blocks specify a language.
- [ ] Duplicate knowledge has been consolidated.
- [ ] Examples are technically accurate.
- [ ] `toc.md` is updated if this is a new or renamed document.
- [ ] Handbook capability map is updated if this is a new or renamed
      document.
- [ ] The document follows repository conventions.

## AI Readability Checklist

Additionally verify:

- [ ] The document can be understood independently.
- [ ] Important concepts are explicitly named.
- [ ] Assumptions are explained.
- [ ] Related documents are linked.
- [ ] Canonical sources are referenced.
- [ ] The document is modular (not monolithic).
- [ ] Sections are concise.
- [ ] AI-generated content has been reviewed by a human.

# References

- [CLAUDE.md](./CLAUDE.md)
- [Strategy](./strategy.md)
- [Architecture](./architecture.md)
- [Document Types](./document-types.md)
- [Contributing](./contributing.md)
- [Repository Overview](../README.md)
- [Markdown Guide](https://www.markdownguide.org/)
