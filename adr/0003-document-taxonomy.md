:PROPERTIES:
:STATUS:   accepted
:DATE:     2026-07-27
:END:

# Context

The framework needed a standardized set of document types that:

- Cover the full range of engineering knowledge needs.
- Have clear, non-overlapping responsibilities.
- Support composition from small focused documents into larger
  understanding.
- Enable AI retrieval by being modular and explicit.
- Are stable enough to serve as the taxonomy for the entire framework.

Without a clear taxonomy, documents drift into undefined formats,
duplicate each other's responsibilities, and become harder to maintain.

# Decision

Define nine document types, each with a single, distinct responsibility:

| Document Type | Primary Purpose | Answers |
| --- | --- | --- |
|---------------+--------------------------------------+----------------------------|
| Handbook | Principles, philosophy and standards | Why? What? |
| --- | --- | --- |
| Guide | Explain a focused engineering topic | How does it work? |
| Playbook | Repeatable engineering workflow | How do I do this? |
| Checklist | Verify correctness | Did I complete everything? |
| Template | Standardize repeatable artifacts | Where do I start? |
| Reference | Quick factual lookup | What is the syntax? |
| Glossary | Canonical terminology | What does this mean? |
| Learning Path | Structured learning progression | What should I learn next? |
| Example | Practical implementation | What does good look like? |

The taxonomy follows a clear progression:

```

Handbook → Guide → Playbook → Checklist → Template

Glossary and References support all document types.

Learning Paths connect all document types.

Examples support Guides and Playbooks.

```

Each document type has a single responsibility. Documents should never
attempt to fulfil multiple responsibilities. Complex knowledge emerges
from composition of specialized documents.

# Consequences

## Positive

- Clear guidance for authors on what to write and how to structure it.
- AI systems can route queries to the document type best suited to
  answer them.
- Small, focused documents are easier to maintain than large monoliths.
- Document types compose naturally into a knowledge graph.
- New capabilities follow the same taxonomy, ensuring consistency.

## Negative

- Authors must learn to decompose knowledge into the correct document
  types, which requires judgement.
- Some topics may not fit neatly into a single type, requiring
  cross-referencing rather than a single document.
- The taxonomy adds structure that simpler repositories do not need.

# Alternatives Considered

## Single Document Type (Monolithic)

One type of document that contains everything.

Rejected because it produces large, hard-to-maintain documents that are
difficult for AI to retrieve from effectively. It also provides no
guidance to authors about structure.

## Fewer Types

Use only handbooks, guides, and playbooks.

Rejected because checklists, templates, references and glossaries each
serve distinct purposes that cannot be absorbed into the other types
without losing clarity.

## More Types

Include additional types like tutorial, FAQ, cookbook, specification.

Rejected because each additional type increases complexity and the core
nine cover the essential needs. New types can be added later if a clear
gap emerges.

# References

- [Document Types](../document-types.md)
- [Engineering Fundamentals Handbook](../handbooks/engineering/README.md)
