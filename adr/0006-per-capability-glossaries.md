---
title: "ADR 0006: Per-Capability Glossaries"
description: "Organize glossaries by capability, with a shared root glossary for repository-wide terminology."
type: adr
capability: architecture
status: published
tags: [per, capability, glossaries]
last_reviewed: 2026-07-28
---

# Context

The framework needs a standardized approach to terminology management.

Options considered:

- A single, monolithic glossary for the entire repository.
- Per-capability glossaries with a shared root glossary.
- Inline definitions within documents (no dedicated glossary).
- No formal glossary at all (ad-hoc terminology).

The chosen approach must support:

- Consistent terminology across documents.
- Authoritative definitions that AI can reference.
- Easy discovery of term meanings.
- Ownership by capability teams.

# Decision

Organize glossaries by capability, with a shared root glossary for
repository-wide terminology.

Each capability owns its own glossary directory:

```text
glossary/
├── README.org              (overview and writing guidelines)
├── engineering/            (repository-wide terminology)
├── architecture/           (architecture-specific terms)
├── rails/                  (Rails-specific terms)
└── security/               (security-specific terms)
```

Repository-wide terminology (abstraction, coupling, cohesion) lives in
the Engineering Glossary. Capability-specific terminology (ADR, bounded
context, hexogonal architecture) lives in the capability's glossary.

# Consequences

## Positive

- Terminology ownership is clear: each capability defines its own
  vocabulary.
- Repository-wide terms have a single authoritative home in the
  Engineering Glossary.
- AI assistants can scope glossary lookups to the relevant capability.
- Glossary directories can grow independently without conflicts.
- Engineers can quickly find definitions within their capability
  context.

## Negative

- Some terms may span multiple capabilities, requiring coordination to
  ensure consistent definitions.
- Contributors must determine whether a term is repository-wide or
  capability-specific, which requires judgement.
- Cross-referencing between glossaries is necessary for terms that
  relate across capabilities.

# Alternatives Considered

## Single Monolithic Glossary

All terms in one file.

Rejected because it creates coordination bottlenecks, makes ownership
unclear, and grows unwieldy as the framework scales.

## Inline Definitions Only

Define terms inline within documents.

Rejected because it prevents canonical definitions from being
referenced authoritatively, leads to duplication, and makes it harder
for AI to resolve terminology consistently.

## No Formal Glossary

Let terminology evolve organically without a glossary.

Rejected because inconsistent terminology undermines both human
readability and AI effectiveness. A glossary is essential for a
knowledge framework.

# References

- [Glossary Overview](../glossary/README.md)
- [Engineering Glossary](../glossary/engineering/README.md)
- [Architecture Glossary](../glossary/architecture/README.md)
- [Document Types](../document-types.md)
- [ADR-0001: Capability Model for Knowledge Organization](../adr/0001-capability-model.md)
