# Purpose

The Engineering Knowledge Framework is built from a small set of
well-defined document types.

Each document type exists to solve a specific problem and has a clearly
defined responsibility.

A document should never attempt to fulfil multiple responsibilities.

Instead, complex knowledge should emerge from the composition of
specialized documents.

This document defines the canonical document taxonomy of the framework.

# Philosophy

The framework is based on several principles.

- Knowledge is modular.
- Every document has a single responsibility.
- Documents should compose naturally.
- Knowledge should be reusable.
- Knowledge should be easy for both humans and AI to navigate.
- Prefer linking over duplication.

The goal is not to minimize the number of documents, but to maximize the
clarity, maintainability and reuse of engineering knowledge.

# Knowledge Architecture

Engineering knowledge is organized around **Capabilities**.

A capability represents an engineering discipline or area of expertise.

Examples include:

- Rails Engineering
- Software Architecture
- Security Engineering
- Accessibility
- Testing
- Platform Engineering
- AI Engineering

Each capability owns a collection of knowledge artifacts.

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

Each artifact has a distinct purpose.

# Document Taxonomy

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

No document type should duplicate the responsibility of another.

# Capability

A capability is the highest-level organizational unit within the
framework.

It groups all knowledge required to master an engineering discipline.

Capabilities should evolve independently while following common
governance and documentation standards.

Capabilities are intentionally technology-agnostic.

Examples include:

- Rails Engineering
- Rust Engineering
- Site Reliability Engineering
- Security Engineering

- Handbook

## Purpose

A Handbook defines the enduring principles, standards and philosophy of
a capability.

It explains **why** engineers should work in a particular way.

## Characteristics

- Timeless.
- Opinionated.
- Standards-focused.
- Technology-independent where possible.
- Stable over time.

## Typical Sections

- Purpose
- Principles
- Standards
- Best Practices
- Anti-patterns
- Decision Frameworks
- AI Integration
- References

## Examples

- Rails Engineering Handbook
- Security Engineering Handbook
- Architecture Handbook

- Guide

## Purpose

A Guide explains a focused engineering concept in depth.

Guides teach understanding rather than operational procedures.

## Characteristics

- Focused.
- Educational.
- Conceptual.
- Rich with examples.
- May reference multiple handbooks.

## Typical Sections

- Purpose
- Background
- Concepts
- Best Practices
- Common Mistakes
- Examples
- Related Guides

## Examples

- Service Objects
- Turbo Frames
- Dependency Injection
- Event Sourcing

- Playbook

## Purpose

A Playbook describes a repeatable engineering workflow.

It explains how to perform an engineering activity consistently.

## Characteristics

- Procedural.
- Sequential.
- Action-oriented.
- Repeatable.
- Operational.

## Typical Sections

- Objective
- Inputs
- Prerequisites
- Workflow
- Checklists
- Escalation Points
- AI Workflow
- Expected Outputs

## Examples

- Code Review Playbook
- Production Deployment Playbook
- Incident Response Playbook
- Architecture Review Playbook

- Checklist

## Purpose

A Checklist verifies that important work has been completed.

It minimizes mistakes and encourages consistency.

## Characteristics

- Short.
- Actionable.
- Verifiable.
- Used repeatedly.

## Examples

- Pull Request Checklist
- Accessibility Checklist
- Security Checklist
- Project Kickoff Checklist

- Template

## Purpose

Templates provide reusable starting points for recurring engineering
artifacts.

They standardize structure rather than content.

## Examples

- ADR Template
- RFC Template
- Incident Report Template
- Retrospective Template

- Reference

## Purpose

References provide quick factual information.

They are intended for lookup rather than learning.

## Characteristics

- Concise.
- Precise.
- Searchable.
- Frequently consulted.

## Examples

- Ruby Style Reference
- Rails Generator Reference
- Git Commands
- HTTP Status Codes

- Glossary

## Purpose

Glossaries establish canonical terminology.

They ensure that engineers and AI assistants use consistent language.

Each capability owns its own glossary.

Repository-wide terminology belongs in the Engineering Glossary.

Glossaries should define terms rather than explain them in depth.

# Learning Path

## Purpose

Learning Paths provide structured progression through a capability.

They help engineers develop competency over time.

## Typical Structure

- Fundamentals
- Core Topics
- Intermediate Topics
- Advanced Topics
- Practical Exercises
- Suggested Reading
- Capstone Projects

Learning Paths should reference all other document types.

# Example

## Purpose

Examples demonstrate practical application of engineering knowledge.

They bridge the gap between theory and implementation.

Examples should illustrate:

- Best practices.
- Anti-patterns.
- Before/after comparisons.
- Complete implementations.
- Real-world scenarios.

- Relationships Between Document Types

Document types are designed to complement one another.

```

```
             Handbook
                 │
  ┌──────────────┼──────────────┐
  │              │              │
```

Guides       References      Glossary
│
│
Playbooks
│
│
Checklists
│
│
Templates

Learning Paths connect all document types.

Examples support Guides and Playbooks.

```

This relationship intentionally separates principles, concepts,
workflows and verification.

# Choosing the Correct Document Type

When creating new knowledge, ask the following questions.

| Question | Document Type |
| --- | --- |
|---------------------------------+---------------|
| Why should we do this? | Handbook |
| --- | --- |
| How does this concept work? | Guide |
| How do I perform this task? | Playbook |
| How do I verify it? | Checklist |
| How do I start? | Template |
| Where can I quickly look it up? | Reference |
| What does this term mean? | Glossary |
| What should I learn next? | Learning Path |
| What does good look like? | Example |

If a document answers multiple questions, it should probably be split
into multiple documents.

# AI Considerations

Document types are intentionally designed to support AI-assisted
engineering.

Smaller, focused documents:

- Improve retrieval.
- Reduce ambiguity.
- Improve context quality.
- Simplify reasoning.
- Reduce maintenance.

AI should consume many small documents rather than one large document.

# Knowledge Evolution

Engineering knowledge evolves through experience.

```

Experience

↓

Lesson Learned

↓

Guide

↓

Handbook Standard

↓

Playbook

↓

Checklist

↓

Template

↓

Learning Path

```

The framework encourages converting project experience into reusable
engineering knowledge.

# Creating New Document Types

New document types should be introduced only when:

- Existing document types cannot adequately represent the knowledge.
- The responsibility is clearly distinct.
- The new type can be reused across multiple capabilities.
- It strengthens rather than complicates the framework.

Document proliferation should be avoided.

# Related Documents

- [Architecture](./architecture.md)
- [Strategy](./strategy.md)
- [Roadmap](./roadmap.md)
- [Style Guide](./style-guide.md)
- [Contributing](./contributing.md)
- [Repository Overview](../README.md)
- [Glossary](./glossary/README.md)
