# Context

Engineering knowledge is consumed by two distinct audiences:

- Human engineers reading documentation.
- AI systems retrieving context for code generation, review, analysis
  and question answering.

Traditional documentation is written for humans only. AI systems are
typically an afterthought, consuming whatever format humans produce.

The framework needed to decide whether to:

- Write only for humans (traditional approach).
- Write for AI primarily and humans secondarily.
- Design for both from the start.

# Decision

Treat AI as a ***first-class consumer*** of the knowledge repository.

Documents should be designed so that they are effective for both humans
and AI simultaneously. This means:

- Small, focused documents with single responsibilities (improves AI
  retrieval precision).
- Clear, explicit terminology (reduces AI ambiguity).
- Consistent structure across documents (improves AI pattern matching).
- Rich cross-references (enables AI graph traversal).
- Explicit reasoning and trade-off documentation (improves AI response
  quality).
- Metadata for document classification (improves AI context selection).

The key insight is that good engineering writing naturally serves both
audiences. The framework does not require writing differently for AI.
It requires writing **better** for humans, which also benefits AI.

# Consequences

## Positive

- AI assistants can retrieve and use knowledge more effectively.
- Human readability is improved, not compromised.
- The repository is better positioned for AI-assisted tooling.
- Document structure standards improve overall quality.
- The framework differentiates itself from traditional documentation
  repositories.

## Negative

- Requires authors to think about structure and clarity more carefully.
- May lead to more documents overall (due to the preference for small,
  focused documents over monolithic ones).
- AI training data biases may affect how well the repository performs
  with different AI systems.

# Alternatives Considered

## Human-Only Design

Write documentation for humans only, with no consideration for AI
consumption.

Rejected because AI-assisted engineering is already a core use case.
Ignoring AI consumption would make the framework less effective for one
of its primary audiences.

## AI-First Design

Optimize documents primarily for AI parsing, accepting reduced human
readability.

Rejected because human engineers remain the primary audience. AI should
be a collaborator, not the sole consumer. Good human documentation
naturally produces good AI documentation.

# References

- [Engineering Fundamentals Handbook](../handbooks/engineering/README.md)
- [Writing Principles](../writing-principles.md)
- [Style Guide](../style-guide.md)
