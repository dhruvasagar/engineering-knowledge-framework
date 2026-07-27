+++
title = "Engineering Learning Paths"
description = "Structured learning progression for engineering fundamentals"
+++


# Purpose

These learning paths provide a structured progression through
engineering fundamentals, from foundational concepts to advanced
practice.

Each path is designed to develop engineering judgement, not just
technical knowledge. The goal is to produce engineers who can make
sound design decisions, not just write working code.

# Beginner Path

## Objective

Build a solid understanding of core engineering principles and apply
them in everyday work.

## Prerequisites

- Some experience writing code in any language.
- Familiarity with basic development workflows (version control,
  testing, deployment).

## Topics

1. ***Separation of Concerns***
   - Core concept and why it matters.
   - Identifying mixed responsibilities in existing code.
   - Practice: Refactor a monolithic function into focused modules.
   - Reference: [Engineering Fundamentals Handbook](../../handbooks/engineering/README/)

2. ***Code Organization***
   - Feature-based vs layer-based organization.
   - Module boundaries and responsibilities.
   - Practice: Restructure a small project by feature.
   - Reference: [Code Organization Guide](../../guides/engineering/code-organization/)

3. ***Basic Testing***
   - Test pyramid and where to focus.
   - Writing unit tests for isolated logic.
   - Practice: Add tests to an untested module.
   - Reference: [Testing Strategies Guide](../../guides/engineering/testing-strategies/)

4. ***Error Handling***
   - Distinguishing recoverable and unrecoverable errors.
   - Writing meaningful error messages.
   - Practice: Audit and improve error handling in a service.
   - Reference: [Error Handling Guide](../../guides/engineering/error-handling/)

5. ***Code Review Fundamentals***
   - Reviewing for correctness, design and maintainability.
   - Writing constructive review feedback.
   - Practice: Review a pull request using the code review checklist.
   - Reference: [Code Review Playbook](../../playbooks/code-review/README/)

## Suggested Projects

- Refactor a small existing project to improve separation of concerns.
- Add comprehensive error handling and logging to a service.
- Build a simple feature with tests following the test pyramid.

## Assessment

Demonstrate by: Successfully reviewing a peer's pull request with
meaningful feedback on design, not just style.

# Intermediate Path

## Objective

Make consistent design decisions, manage complexity and contribute to
architecture discussions.

## Prerequisites

- Completed Beginner Path or equivalent experience.
- Comfortable with testing and code review practices.

## Topics

1. ***Coupling and Cohesion***
   - Measuring and evaluating coupling.
   - Improving cohesion through module design.
   - Practice: Analyse coupling in an existing system and propose
     improvements.
   - Reference: [Engineering Glossary](../../glossary/engineering/README/)

2. ***Dependency Management***
   - Dependency inversion principle.
   - Dependency injection patterns.
   - Practice: Refactor a tightly coupled module to use dependency
     injection.
   - Reference: [Engineering Fundamentals Handbook](../../handbooks/engineering/README/)

3. ***Technical Debt Management***
   - Strategic vs accidental debt.
   - Assessment and prioritization.
   - Practice: Conduct a technical debt assessment on a code area.
   - Reference: [Tech Debt Assessment Checklist](../../checklists/tech-debt-assessment/)

4. ***Logging and Observability***
   - Structured logging standards.
   - Log levels and context.
   - Practice: Add structured logging to a service and verify in
     development.
   - Reference: [Logging Guide](../../guides/engineering/logging/)

5. ***Architecture Awareness***
   - Understanding architectural patterns (layered, hexagonal).
   - How engineering decisions affect architecture.
   - Practice: Document the architecture of an existing system using C4
     Level 1-2.
   - Reference: [Software Architecture Handbook](../../handbooks/architecture/README/)

## Suggested Projects

- Identify and document technical debt in a team codebase.
- Propose and implement a refactoring that improves coupling.
- Write an ADR for a significant design decision.

## Assessment

Demonstrate by: Leading a code review that catches design-level issues.
Contributing to an architecture review with meaningful observations.

# Advanced Path

## Objective

Shape engineering strategy, influence organizational practices and
mentor other engineers.

## Prerequisites

- Completed Intermediate Path or equivalent experience.
- Experience leading medium-to-large features or projects.

## Topics

1. ***System Design and Trade-offs***
   - Quality attribute trade-off analysis.
   - Architectural decision documentation.
   - Practice: Evaluate two architectural approaches and document the
     trade-offs in an ADR.
   - Reference: [Architectural Patterns Guide](../../guides/architecture/architectural-patterns/)

2. ***Engineering Strategy***
   - Defining engineering standards for a team or organization.
   - Balancing velocity, quality and innovation.
   - Practice: Draft an engineering standard for a capability.
   - Reference: [Engineering Fundamentals Handbook](../../handbooks/engineering/README/)

3. ***Mentoring and Review***
   - Reviewing for engineering growth, not just code correctness.
   - Providing feedback that builds judgement.
   - Practice: Mentor a junior engineer through a code review cycle.
   - Reference: [Code Review Playbook](../../playbooks/code-review/README/)

4. ***Cross-Capability Integration***
   - How engineering principles intersect with architecture, security
     and testing.
   - Building shared standards across capabilities.
   - Practice: Identify a cross-cutting concern and propose a standard
     that spans multiple capabilities.

5. ***AI-Assisted Engineering***
   - Using AI for code review, design exploration and documentation.
   - Maintaining engineering judgement alongside AI assistance.
   - Practice: Conduct a code review with AI assistance and evaluate
     the AI's suggestions.
   - Reference: AI Workflows for Engineering

## Suggested Projects

- Define a team engineering standard and drive its adoption.
- Lead an architecture review for a cross-team initiative.
- Establish an ADR practice for a team or project.

## Assessment

Demonstrate by: Influencing engineering practices beyond your immediate
team. Mentoring others in engineering fundamentals. Contributing to the
engineering knowledge framework.

# Related Documents

- [Engineering Fundamentals Handbook](../../handbooks/engineering/README/)
- [Software Architecture Handbook](../../handbooks/architecture/README/)
- [Code Review Playbook](../../playbooks/code-review/README/)
- [Code Organization Guide](../../guides/engineering/code-organization/)
- [Testing Strategies Guide](../../guides/engineering/testing-strategies/)
- [Error Handling Guide](../../guides/engineering/error-handling/)
- [ADR Writing Guide](../../guides/architecture/adr-writing-guide/)
