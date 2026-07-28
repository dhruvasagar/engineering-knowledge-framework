---
title: "Architecture"
description: "Architectural overview of the Engineering Knowledge Framework"
---


# Purpose

This document describes the architecture of the Engineering Knowledge
Framework.

It explains how the framework is organized, how knowledge is structured,
how the various document types relate to one another, and how the
framework evolves over time.

Unlike the [Strategy](./strategy/), which explains **why** the framework exists, this
document explains **how** the framework is designed.

# Design Goals

The architecture of the framework is guided by several goals.

- Simple to understand.
- Easy to extend.
- Easy to navigate.
- Modular.
- AI-friendly.
- Technology agnostic.
- Timeless.
- Suitable for organizations of any size.

The architecture should continue to scale as the repository grows from
dozens of documents to thousands.

# Architectural Principles

## Knowledge over documentation

The framework manages knowledge rather than documents.

Documents are implementation artifacts.

Knowledge is the architectural concern.

## Separation of concerns

Each document should have one clear responsibility.

Knowledge should be decomposed into reusable components rather than
duplicated across multiple documents.

## Capability-driven organization

Engineering knowledge should be organized around engineering
capabilities rather than document types.

Capabilities represent domains of expertise.

Each capability owns all knowledge required to understand and practice
that discipline.

## Modular composition

Knowledge should be composed from many focused documents.

Smaller documents are:

- Easier to maintain.
- Easier to review.
- Easier to discover.
- Easier for AI systems to consume.
- Easier to reuse.

## Explicit relationships

Relationships between documents should be represented through links
rather than duplication.

Knowledge should form a connected graph rather than isolated pages.

# High-Level Architecture

The framework consists of several architectural layers.

```

Engineering Knowledge Framework

├── Governance
│
├── Knowledge Architecture
│
├── Engineering Capabilities
│
├── AI Framework
│
├── Learning Framework
│
└── Tooling

```

Each layer has a distinct responsibility.

# Governance Layer

The Governance layer defines the framework itself.

It answers questions such as:

- Why does the framework exist?
- How should knowledge be written?
- How is the repository organized?
- What standards should contributors follow?

Typical documents include:

- README
- CLAUDE.md
- STRATEGY
- ROADMAP
- STYLE_GUIDE
- DOCUMENT_TYPES
- CONTRIBUTING
- ARCHITECTURE

Governance documents evolve slowly and provide long-term stability.

# Knowledge Architecture Layer

The Knowledge Architecture layer defines how engineering knowledge is
organized.

Responsibilities include:

- Capability model.
- Document taxonomy.
- Cross-referencing.
- Repository organization.
- Glossaries.
- Metadata conventions.

Knowledge architecture should remain independent of any specific
engineering discipline.

# Engineering Capabilities

Capabilities are the primary building blocks of the framework.

A capability represents a complete engineering discipline.

Examples include:

- Rails Engineering
- Software Architecture
- Security Engineering
- Testing
- Accessibility
- Platform Engineering
- AI Engineering

Each capability should be self-contained.

# Capability Structure

Each capability is expected to contain a consistent collection of
knowledge artifacts.

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

Not every capability must initially contain every artifact, but this is
the target architecture.

# Knowledge Artifact Relationships

Knowledge artifacts have distinct responsibilities.

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

Learning Paths connect all of the above.

```

Responsibilities:

| Artifact | Responsibility |
| --- | --- |
|---------------+------------------------------------------|
| Handbook | Principles, philosophy and standards |
| --- | --- |
| Guide | Deep explanation of a focused topic |
| Playbook | Repeatable operational workflow |
| Checklist | Verification and quality gates |
| Template | Reusable starting point |
| Reference | Quick factual lookup |
| Glossary | Canonical terminology |
| Learning Path | Structured progression through knowledge |
| Example | Practical implementation |

Each artifact type is documented in
[Document Types](./document-types/).

# Knowledge Graph

The framework should be viewed as a graph rather than a hierarchy.

Example:

```

Rails Handbook

↓

Service Objects Guide

↓

Code Review Playbook

↓

Pull Request Checklist

↓

Service Object Template

↓

Learning Path

```

Documents should be interconnected through meaningful relationships.

Navigation should emphasize concepts rather than directory structure.

# Knowledge Lifecycle

Knowledge continuously evolves.

```

Experience

↓

Capture

↓

Review

↓

Refine

↓

Standardize

↓

Publish

↓

Apply

↓

Learn

↓

Improve

↓

Repeat

```

Every engineering experience should eventually become reusable
organizational knowledge.

Project retrospectives, architectural decisions and production incidents
are important sources of new knowledge.

# AI Architecture

AI is an architectural component of the framework rather than an
afterthought.

Knowledge should support AI throughout the engineering lifecycle.

AI responsibilities include:

- Research.
- Draft generation.
- Code review.
- Architecture review.
- Test generation.
- Documentation review.
- Knowledge extraction.
- Gap analysis.
- Cross-reference suggestions.
- Learning-path generation.

Human review remains mandatory.

# AI-Friendly Knowledge

Knowledge should be structured for effective AI consumption.

Documents should:

- Have a single responsibility.
- Follow consistent structure.
- Explain reasoning.
- Define terminology.
- Use meaningful headings.
- Link related knowledge.
- Avoid unnecessary duplication.
- Prefer principles over implementation details.

These characteristics improve both human readability and AI reasoning.

# Repository Organization

The repository is organized into two broad categories.

## Governance

Defines the framework itself.

```

governance/

README
CLAUDE
STRATEGY
ROADMAP
ARCHITECTURE
STYLE_GUIDE
DOCUMENT_TYPES
CONTRIBUTING

```

## Knowledge

Contains engineering capabilities.

```

glossary/

handbook/

guides/

playbooks/

checklists/

templates/

references/

learning-paths/

examples/

assets/

```

Future tooling should understand this organization automatically.

# Architectural Constraints

The framework intentionally avoids:

- Monolithic documentation.
- Technology-specific organization.
- Duplicate knowledge.
- Deep directory hierarchies.
- Project-specific assumptions.
- Vendor lock-in.

Knowledge should remain reusable across organizations.

# Architectural Decision Principles

When evolving the framework, prefer decisions that:

- Increase modularity.
- Improve discoverability.
- Reduce duplication.
- Encourage reuse.
- Improve AI collaboration.
- Preserve timeless knowledge.
- Scale naturally as the repository grows.
- Keep the framework approachable for new contributors.

- Evolution Strategy

The architecture is designed to evolve through incremental improvement.

Expected evolution includes:

Phase 1

Foundation

↓

Phase 2

Reference Capabilities

↓

Phase 3

Framework Tooling

↓

Phase 4

Knowledge Platform

↓

Phase 5

Community Ecosystem

↓

Phase 6

Open Standard

The architecture should remain stable while capabilities and tooling
continue to grow.

# Success Characteristics

A successful Engineering Knowledge Framework should be:

- Modular.
- Discoverable.
- Extensible.
- AI-native.
- Community-driven.
- Easy to contribute to.
- Easy to adopt.
- Easy to customize.
- Timeless.
- Sustainable.

Organizations should be able to adopt only the capabilities they need
without modifying the framework itself.

# Related Documents

- [Repository Overview](../README/)
- [CLAUDE](./CLAUDE.md)
- [Strategy](./strategy/)
- [Roadmap](./roadmap/)
- [Document Types](./document-types/)
- [Style Guide](./style-guide/)
- [Contributing](./contributing/)
- [Glossary](./glossary/README/)
