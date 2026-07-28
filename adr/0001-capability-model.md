# Context

Engineering knowledge can be organized in many ways:

- By technology stack (Rails, React, Kubernetes).
- By document type (all handbooks together, all guides together).
- By engineering discipline (architecture, security, testing).
- By project or team.

The framework needed a primary organizational unit that is:

- Stable over time as technologies change.
- Reusable across different engineering domains.
- Intuitive for both engineers and AI to navigate.
- Capable of grouping all knowledge artifacts for a subject together.

# Decision

Organize engineering knowledge around ***Engineering Capabilities***.

A capability represents an engineering discipline or area of expertise
(e.g., Software Architecture, Rails Engineering, Security Engineering).

Each capability owns the complete collection of knowledge artifacts
needed to master that discipline:

```
Capability
├── Handbook
├── Guides
├── Playbooks
├── Checklists
├── Templates
├── References
├── Glossary
├── Learning Paths
└── Examples
```

Capabilities are the primary organizational unit. Document types are
a secondary classification within each capability.

# Consequences

## Positive

- Capabilities are stable as technologies evolve (Architecture as a
  capability outlives any specific architectural pattern).
- Related knowledge lives together, making it easier to discover and
  maintain.
- New capabilities can be added without restructuring existing ones.
- AI assistants can target a capability context for better retrieval.
- Capabilities can be developed and maintained independently.

## Negative

- Some knowledge spans multiple capabilities (e.g., security concerns
  touch every discipline), requiring careful cross-referencing.
- The capability model is less familiar than a simple document-type
  hierarchy, requiring documentation and onboarding.
- Determining capability boundaries requires judgement.

# Alternatives Considered

## Document-Type Hierarchy

Organize documents primarily by type: all handbooks in one directory,
all guides in another, etc.

Rejected because it scatters related knowledge across the repository,
making it harder to discover and maintain. Engineers think in terms of
subjects ("I need the Rails guidance"), not document types.

## Technology-Specific Organization

Organize around technology stacks (Rails, Kubernetes, React).

Rejected because technologies change frequently, making this structure
unstable. Principles and practices transcend specific technologies.

## Flat Structure

Place all documents in a single directory with no grouping.

Rejected because it does not scale. Even a modest number of documents
becomes difficult to navigate.

# References

- [Document Types](../document-types.md)
- [Engineering Fundamentals Handbook](../handbooks/engineering/README.md)
