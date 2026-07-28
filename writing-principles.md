# Purpose

This document defines the principles that guide how engineering
knowledge should be written within the Engineering Knowledge Framework.

Unlike the [Style Guide](./style-guide.md), which defines formatting and writing
conventions, this document explains the philosophy behind effective
engineering documentation.

The Style Guide answers:

#+BEGIN_QUOTE
How should we write?
#+END_QUOTE

This document answers:

#+BEGIN_QUOTE
How should we think when writing?
#+END_QUOTE

These principles should guide every contribution to the framework.

# Philosophy

The purpose of engineering documentation is not to create documents.

It is to improve engineering understanding.

Every document should help engineers make better decisions today while
remaining valuable years into the future.

Knowledge compounds.

Documentation decays.

Our objective is to continually transform documentation into enduring
knowledge.

# Knowledge First

Always optimize for knowledge rather than information.

Information answers:

- What happened?
- What exists?

Knowledge answers:

- Why?
- When?
- How?
- What are the trade-offs?
- What should I do?

Documents should prioritize understanding over completeness.

# Write Timelessly

Technology changes.

Engineering principles evolve much more slowly.

Whenever possible, document:

- Principles.
- Decision frameworks.
- Trade-offs.
- Mental models.
- Patterns.
- Engineering judgement.

Avoid writing documents that are tightly coupled to:

- Framework versions.
- Tool versions.
- Vendor products.
- Temporary organizational structures.

Implementation-specific details belong in references, examples and
playbooks—not handbooks.

A useful question to ask is:

#+BEGIN_QUOTE
Will this still be useful five years from now?
#+END_QUOTE

# Explain Why

The most valuable engineering knowledge explains **why**.

When introducing a recommendation, explain:

- The problem it solves.
- Why it exists.
- Alternatives.
- Trade-offs.
- Failure modes.
- When it should not be used.

Reasoning survives technological change.

Instructions alone rarely do.

# Optimize for Decisions

Engineering is largely the process of making decisions under
constraints.

Good documentation should improve decision making.

Instead of writing:

#+BEGIN_QUOTE
Use Service Objects.
#+END_QUOTE

Prefer:

#+BEGIN_QUOTE
Use Service Objects when business logic exceeds the responsibilities of
models or controllers, because they improve separation of concerns,
testability and reuse.
#+END_QUOTE

The second example teaches judgement rather than rules.

# Single Responsibility

Every document should answer one primary question.

Examples:

| Question                    | Document Type |
|-----------------------------|---------------|
| Why should we do this?      | Handbook      |
| How does this concept work? | Guide         |
| How do I perform this task? | Playbook      |
| How do I verify it?         | Checklist     |

If a document attempts to answer multiple unrelated questions, split it
into multiple documents.

Small documents compose better than large documents.

# Prefer Composition

Knowledge should be assembled from reusable building blocks.

Avoid creating large monolithic documents.

Instead:

```
Handbook
↓
Guide
↓
Playbook
↓
Checklist
↓
Template
```

Each document should contribute one piece to the larger knowledge graph.

# Canonical Sources

Every engineering concept should have one authoritative source.

Other documents should reference it.

Never maintain the same explanation in multiple places.

Benefits include:

- Reduced maintenance.
- Better consistency.
- Easier review.
- Better AI retrieval.
- Fewer contradictions.

Duplication is technical debt.

Documentation duplication is knowledge debt.

# Explicit Over Implicit

Assume the reader has not seen any previous document.

State important assumptions explicitly.

Avoid:

- "It"
- "This"
- "That approach"

Prefer explicit nouns.

Good engineering writing minimizes ambiguity.

# Context Independence

Documents should remain understandable when read independently.

This is particularly important for:

- Search.
- AI retrieval.
- Knowledge graphs.
- Future repository organization.

Avoid:

#+BEGIN_QUOTE
As discussed earlier...
#+END_QUOTE

Prefer:

#+BEGIN_QUOTE
See the
[Rails Engineering Handbook](./handbooks/rails/README.md)
for the underlying architectural principles.
#+END_QUOTE

# Build a Knowledge Graph

Think beyond individual documents.

Every document should strengthen the connections between ideas.

When introducing a concept, ask:

- Where is this defined?
- What depends on it?
- What should readers learn next?
- What complements this knowledge?

Prefer links over repetition.

Knowledge should form a graph rather than a hierarchy.

# Write for Humans and AI

The framework serves two audiences:

- Engineers.
- AI systems.

Fortunately, both benefit from the same characteristics:

- Clear language.
- Explicit terminology.
- Consistent structure.
- Logical progression.
- Meaningful headings.
- Small focused documents.
- Strong cross-linking.

Good engineering writing is naturally AI-friendly.

# Teach Mental Models

Documentation should teach engineers how to think rather than what to
memorize.

Prefer:

- Principles.
- Heuristics.
- Decision trees.
- Trade-offs.
- Failure analysis.
- Patterns.

Avoid documenting only procedures.

Procedures change.

Mental models endure.

# Show Good Engineering

Whenever possible, demonstrate:

- Good examples.
- Bad examples.
- Common mistakes.
- Better alternatives.

Engineers often learn faster through comparison than explanation.

# Prefer Evolution Over Perfection

Knowledge is never finished.

Every document can be improved.

Contributors should feel comfortable:

- Refining wording.
- Improving examples.
- Clarifying explanations.
- Improving structure.
- Adding references.
- Simplifying concepts.

Continuous refinement produces better knowledge than infrequent
rewrites.

# Capture Experience

Projects generate valuable engineering knowledge.

Examples include:

- Incidents.
- Retrospectives.
- Architectural decisions.
- Production failures.
- Successful patterns.
- Lessons learned.

These should become reusable engineering knowledge rather than remaining
project-specific artifacts.

Experience should evolve into standards.

# Optimize for Reuse

Ask:

#+BEGIN_QUOTE
Can another team reuse this?
#+END_QUOTE

If the answer is no, consider whether the knowledge belongs in a
project-specific repository instead.

The framework exists to capture reusable engineering knowledge.

# Respect the Reader

Good engineering writing respects the reader's time.

Prefer:

- Concise explanations.
- Clear organization.
- Meaningful headings.
- Direct language.
- Practical examples.

Avoid unnecessary complexity.

The best engineering writing often feels simple.

# Continuous Improvement

Knowledge should continuously evolve.

The expected lifecycle is:

```
Experience
↓
Reflection
↓
Knowledge
↓
Standards
↓
Practice
↓
Learning
↓
Improvement
```

Every contribution should move knowledge one step further along this
journey.

# Questions Every Author Should Ask

Before publishing, ask:

1. Does this improve engineering understanding?
2. Will this remain valuable over time?
3. Have I explained why?
4. Is there one clear responsibility?
5. Have I duplicated existing knowledge?
6. Have I linked related concepts?
7. Can this be understood independently?
8. Will this help AI retrieve the right information?
9. Does this improve engineering judgement?
10. Would I want future engineers to learn from this?

If the answer to several of these questions is "no", continue refining
the document.

# Guiding Statement

#+BEGIN_QUOTE
The purpose of engineering documentation is not to record what we know.

It is to help future engineers know what we have learned.

The Engineering Knowledge Framework exists to transform experience into
timeless engineering knowledge that benefits both humans and AI.
#+END_QUOTE

# Related Documents

- [CLAUDE.md](./CLAUDE.md)
- [Strategy](./strategy.md)
- [Architecture](./architecture.md)
- [Style Guide](./style-guide.md)
- [Document Types](./document-types.md)
- [Contributing](./contributing.md)
- [Repository Overview](../README.md)
