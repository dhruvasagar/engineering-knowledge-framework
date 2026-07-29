---
title: "Contributing"
description: "The Engineering Knowledge Framework is a community-driven project for building high-quality, AI-native engineering knowledge systems."
type: governance
capability: governance
status: published
tags: [contributing]
last_reviewed: 2026-07-28
---

# Purpose

The Engineering Knowledge Framework is a community-driven project for
building high-quality, AI-native engineering knowledge systems.

This document describes how to contribute effectively while maintaining
the consistency, quality and long-term vision of the framework.

Contributions are not limited to documentation. They include improving
the framework itself, expanding engineering capabilities, developing
tooling and advancing AI-assisted engineering practices.

# Guiding Philosophy

Contributors should view themselves as stewards of engineering
knowledge.

Every contribution should strive to:

- Improve engineering understanding.
- Preserve institutional knowledge.
- Increase reuse.
- Improve engineering quality.
- Reduce future maintenance.
- Help both engineers and AI systems make better decisions.

The goal is not simply to create more documents, but to build a better
framework for engineering knowledge.

# Types of Contributions

The framework welcomes contributions across multiple areas.

## Governance

Improve the framework itself.

Examples include:

- Repository architecture
- Strategy
- Writing standards
- Style guide
- Document taxonomy
- Governance processes

## Engineering Capabilities

Develop or improve engineering capabilities.

Examples include:

- Rails Engineering
- Security Engineering
- Software Architecture
- Accessibility
- AI Engineering
- Testing
- Platform Engineering

## Knowledge Artifacts

Create or improve reusable knowledge.

Examples include:

- Handbooks
- Guides
- Playbooks
- Checklists
- Templates
- References
- Learning Paths
- Examples
- Glossaries

## AI Workflows

Improve AI-assisted engineering.

Examples include:

- Prompt libraries
- Context engineering
- Agentic workflows
- Verification workflows
- AI review patterns
- Knowledge extraction

## Tooling

Build tools that improve the framework.

Examples include:

- Repository generators
- Validation tools
- Search
- Knowledge graph generation
- Documentation linting
- AI context generation

- Before Contributing

Before creating new content:

1. Read the repository [README](../README.md).
2. Read [CLAUDE.md](./CLAUDE.md).
3. Understand the [Strategy](./strategy.md).
4. Review the [Architecture](./architecture.md).
5. Read the [Style Guide](./style-guide.md).
6. Understand the [Document Types](./document-types.md).

Contributors should understand the framework before extending it.

# Contribution Principles

All contributions should follow these principles.

## Prefer improving existing knowledge

Before creating a new document, determine whether the knowledge belongs
within an existing document.

Avoid unnecessary duplication.

## Write timelessly

Prefer enduring engineering principles over transient implementation
details.

Instead of documenting a particular tool version, explain the underlying
engineering concepts whenever possible.

## Explain reasoning

Do not simply describe what should be done.

Explain:

- Why.
- Trade-offs.
- Alternatives.
- Decision criteria.

Reasoning has a longer lifespan than implementation details.

## One responsibility per document

Each document should have a clear purpose.

If a document attempts to answer several different questions, consider
splitting it into multiple documents.

## Prefer links over duplication

Knowledge should exist in one authoritative location.

Other documents should reference it rather than repeat it.

## Optimize for humans and AI

Documents should be:

- Easy to read.
- Easy to search.
- Easy to navigate.
- Easy for AI to retrieve.
- Easy to maintain.

- Contribution Workflow

The recommended workflow is:

```text
Identify a problem
↓
Discuss (if needed)
↓
Design the solution
↓
Create or update documents
↓
Cross-reference related knowledge
↓
Validate formatting
↓
Review
↓
Merge
```

Larger architectural changes should be discussed before implementation.

# Creating New Knowledge

When adding new engineering knowledge:

1. Determine the correct capability.
2. Choose the correct document type.
3. Follow the Style Guide.
4. Link related documents.
5. Explain reasoning.
6. Add practical examples where appropriate.
7. Consider AI integration opportunities.
8. Verify consistency with existing standards.

Every new document should strengthen the overall knowledge graph.

# Creating New Capabilities

New capabilities should represent coherent engineering disciplines.

A capability should eventually contain:

- Handbook
- Guides
- Playbooks
- Checklists
- Templates
- References
- Glossary
- Learning Paths
- Examples

New capabilities should follow the repository architecture and document
taxonomy.

# Writing Guidelines

All contributions must follow the
[Style Guide](./style-guide.md).

In particular:

- Write in British English.
- Use consistent terminology.
- Prefer active voice.
- Explain concepts clearly.
- Avoid unnecessary jargon.
- Use meaningful headings.
- Cross-reference related knowledge.

- AI-Assisted Contributions

AI is encouraged throughout the authoring process.

Recommended uses include:

- Brainstorming.
- Research assistance.
- Draft generation.
- Editing.
- Structural improvements.
- Cross-reference suggestions.
- Gap analysis.
- Example generation.
- Diagram generation.
- Review preparation.

AI should accelerate engineering work rather than replace engineering
judgement.

# Human Review

Every contribution should undergo human review.

Reviewers should verify:

- Technical accuracy.
- Engineering quality.
- Alignment with framework philosophy.
- Appropriate document type.
- Correct cross-references.
- Writing quality.
- AI-generated content accuracy.

Human reviewers remain responsible for the final content.

# Quality Checklist

Before submitting a contribution, verify:

- [ ] The correct document type was used.
- [ ] The document has a single responsibility.
- [ ] Existing knowledge was reused where appropriate.
- [ ] Internal links are valid.
- [ ] Terminology is consistent.
- [ ] Examples are technically accurate.
- [ ] AI-generated content has been reviewed.
- [ ] Formatting follows the Style Guide.
- [ ] Metadata is complete.
- [ ] The document contributes lasting value.

- Proposing Framework Changes

Changes to governance documents should be considered carefully.

Examples include:

- Repository architecture.
- Document taxonomy.
- Capability model.
- Writing standards.
- Framework philosophy.

These changes affect the entire repository and should prioritize
long-term stability over short-term convenience.

# Community Expectations

The framework values constructive collaboration.

Contributors are expected to:

- Be respectful.
- Assume good intent.
- Provide constructive feedback.
- Welcome differing engineering perspectives.
- Support proposals with reasoning and practical experience.
- Be willing to revise ideas based on discussion.

Engineering is collaborative, and so is engineering knowledge.

# Long-Term Perspective

Every contribution should be evaluated using a simple question:

> Will this still help engineers make better decisions five years from
> now?

If the answer is no, consider whether the knowledge belongs in the
framework or in a project-specific repository.

The Engineering Knowledge Framework exists to preserve enduring
engineering knowledge rather than transient project documentation.

# Recognition

All meaningful contributions are valuable.

Whether you improve a sentence, contribute a handbook, create a new
capability or build tooling, you are helping improve the collective
engineering knowledge available to the community.

# Keeping the Index in Sync

[toc.md](./toc.md) is the central navigation index for the repository.

When adding a new document:

1. Add it to the relevant capability section in toc.md's "From Top
   to Bottom" inventory.
2. If the document addresses a cross-cutting topic, add it to the
   relevant topic index in toc.md's "Cross-Cutting Topics" section.
3. Update the handbook's ***Capability Map*** for the relevant
   capability.
4. Add a README.md entry if the document is in a directory that
   has one.

When moving or renaming a document:

1. Update all links in toc.md, the handbook capability map, and
   directory READMEs.
2. Update cross-references in related documents.

# Related Documents

- [Table of Contents](./toc.md)
- [Repository Overview](../README.md)
- [CLAUDE.md](./CLAUDE.md)
- [Strategy](./strategy.md)
- [Architecture](./architecture.md)
- [Document Types](./document-types.md)
- [Style Guide](./style-guide.md)
- [Roadmap](./roadmap.md)
