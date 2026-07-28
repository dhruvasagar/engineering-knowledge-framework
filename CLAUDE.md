# CLAUDE.md

> **Engineering Knowledge Framework**
>
> Building AI-native engineering knowledge systems.

---

# Mission

The Engineering Knowledge Framework is an open-source framework for
capturing, organizing, evolving and applying engineering knowledge.

It enables organizations to build a living engineering knowledge system
that improves software quality, accelerates learning, preserves
institutional knowledge and enables effective collaboration between
engineers and AI.

This repository is not simply a documentation repository.

It is a framework for engineering knowledge.

---

# Vision

Create the definitive open framework for engineering knowledge
management.

The framework should enable organizations to:

* Capture institutional knowledge.
* Standardize engineering practices.
* Improve engineering decision making.
* Reduce repeated mistakes.
* Accelerate onboarding.
* Build engineering capabilities.
* Integrate AI throughout the engineering lifecycle.
* Continuously improve through organizational learning.

Knowledge should remain valuable regardless of changes in technology,
frameworks or organizational structure.

---

# Core Philosophy

## Engineering Knowledge over Documentation

Documentation is an artifact.

Knowledge is the objective.

Every document should improve engineering understanding rather than
simply describe implementation.

Always ask:

> Will this help engineers make better decisions?

---

## Principles over Tools

Document enduring engineering principles before documenting tools,
frameworks or libraries.

Examples:

Prefer

* Separation of Concerns

before

* Rails Service Objects

Prefer

* Dependency Inversion

before

* Dependency Injection Libraries

Technology changes.

Engineering principles endure.

---

## Explain Why

Every document should answer:

* Why does this exist?
* What problem does it solve?
* When should it be used?
* What are the trade-offs?
* When should it *not* be used?

Procedures without reasoning create fragile knowledge.

---

## Knowledge is Modular

Engineering knowledge should be composed from small,
single-responsibility documents.

Prefer:

Handbook

↓

Guide

↓

Playbook

↓

Checklist

↓

Reference

rather than one large document attempting to explain everything.

---

## Prefer Capabilities over Categories

The primary organizational unit of the framework is an
*Engineering Capability*.

A capability combines all knowledge required to master a subject.

Example:

#+BEGIN_EXAMPLE

Rails Engineering

├── Handbook
├── Guides
├── Playbooks
├── Checklists
├── Templates
├── References
├── Glossary
├── Learning Paths
└── AI Workflows

#+END_EXAMPLE

Documentation should evolve around capabilities rather than document
types.

---

# AI-first Philosophy

AI is a first-class consumer of this repository.

Documentation should be written so that it is useful for:

* Engineers
* AI assistants
* Coding agents
* Documentation generators
* Search systems
* Knowledge graph generators

Human readability remains the highest priority, but machine
understandability should always be considered.

---

## AI Responsibilities

AI should assist with:

* Research
* Outlining
* Draft generation
* Refactoring
* Technical review
* Cross-reference discovery
* Example generation
* Diagram generation
* Learning-path creation
* Style validation
* Knowledge extraction
* Gap analysis

AI should *not* replace engineering judgement.

Human review remains mandatory.

---

## Navigation and Discovery

The repository uses [toc.md](./toc.md) as the central navigation index.
It provides two views:

* **From Top to Bottom**: Complete inventory of all documents
  organized by capability, then by document type.
* **Cross-Cutting Topics**: Topic-based indexes (Testing, Security,
  API Design, etc.) that gather documents across capabilities.

Every handbook also includes a **Capability Map** section listing
all documents in that capability.

**When adding or moving documents, update toc.md and the
relevant handbook's Capability Map.**

When writing or editing documents:

- Use =-= for bullet lists and =*= [ ]= for checklists.
  Never use =*= for bullets — in Markdown, =*= creates a headline,
  not a list item.
- Do not skip headline levels (e.g., =*= to =***= without =**=).
- Follow the formatting rules in [STYLE_GUIDE.md](./style-guide.md).

## Context Engineering

Documents should maximize AI effectiveness by providing:

* Clear scope
* Explicit assumptions
* Consistent terminology
* Rich cross references
* Decision rationale
* Practical examples

Well-structured knowledge produces better AI outcomes than larger
context windows.

---

# Writing Principles

Every document should strive to be:

## Timeless

Avoid writing that depends on:

* Current versions
* Temporary tooling
* Organizational structures
* Short-lived technologies

Capture principles instead of implementation details whenever possible.

---

## Opinionated

The framework should recommend preferred engineering practices.

When multiple approaches exist:

* Explain alternatives.
* Explain trade-offs.
* State the recommended approach.
* Explain why.

Avoid presenting every option as equally valid.

---

## Practical

Documentation should enable better engineering work.

Every significant concept should eventually include:

* Examples
* Best practices
* Anti-patterns
* Common mistakes
* Decision frameworks
* AI workflows

---

## Incremental

Large documents should be decomposed.

Prefer many focused documents over monolithic references.

---

## Connected

Prefer linking over duplication.

Knowledge should form a connected network.

Whenever appropriate, reference:

* Handbooks
* Guides
* Playbooks
* References
* Learning Paths
* Glossaries

---

# Repository Architecture

The repository consists of six major layers.

1. Governance

Repository standards and philosophy.

Examples:

* README
* CLAUDE.md
* STRATEGY
* ROADMAP
* STYLE GUIDE
* CONTRIBUTING

2. Knowledge Architecture

Defines how engineering knowledge is organized.

Examples:

* Document Types
* Capability model
* Glossaries

3. Engineering Capabilities

Reusable engineering knowledge.

Examples:

* Rails
* Architecture
* Security
* Testing
* Accessibility
* Platform
* DevOps

4. AI Framework

Engineering workflows involving AI.

Examples:

* Context engineering
* Agentic workflows
* AI-assisted code review
* AI-assisted architecture review

5. Learning Framework

Knowledge progression.

Examples:

* Learning paths
* Exercises
* Assessments
* Reading sequences

6. Tooling

Automation supporting the framework.

Examples:

* Templates
* Linters
* Validators
* Generators
* Search
* Knowledge graphs

---

# Knowledge Lifecycle

Engineering knowledge continuously evolves.

#+BEGIN_EXAMPLE

Experience

↓

Capture

↓

Review

↓

Refine

↓

Organize

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

#+END_EXAMPLE

Every document contributes to this lifecycle.

---

# Contribution Philosophy

Prefer improving existing knowledge over creating new documents.

Every contribution should:

* Improve clarity.
* Improve decision making.
* Increase reuse.
* Reduce duplication.
* Strengthen cross references.
* Improve discoverability.

Small continuous improvements are encouraged.

---

# Quality Standards

Every document should:

* Have one primary purpose.
* Follow the Style Guide.
* Match a defined document type.
* Explain reasoning.
* Include references.
* Include examples where appropriate.
* Cross-reference related knowledge.
* Remain technically accurate.
* Remain useful over time.

---

# Definition of Success

The framework succeeds when it enables engineers to:

* Make better decisions.
* Deliver higher quality software.
* Learn faster.
* Avoid repeating previous mistakes.
* Preserve institutional knowledge.
* Collaborate effectively with AI.

Success is measured by improved engineering capability rather than the
number of documents produced.

---

# Long-term Vision

The Engineering Knowledge Framework should become an open standard for
engineering knowledge management.

Organizations should be able to:

* Fork the framework.
* Customize engineering capabilities.
* Add organization-specific knowledge.
* Integrate AI workflows.
* Contribute improvements back to the community.

The framework should provide a common architecture for capturing and
sharing engineering knowledge in the same way that OpenAPI standardized
API descriptions and Kubernetes standardized container orchestration.

---

# Guiding Principle

> *Engineering knowledge should scale with both people and AI.*

Every decision in this repository should move the framework closer to
that vision.
