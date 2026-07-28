---
title: "Engineering Fundamentals Handbook"
description: "Enduring principles, standards and decision frameworks for software engineering"
---


# Purpose

Engineering is the disciplined application of knowledge to build and
maintain software systems.

This handbook defines the enduring principles, standards and decision
frameworks that guide engineering work within this organization.

Unlike technology-specific guides, this document focuses on fundamentals
that remain valuable regardless of programming language, framework or
tooling choices.

Its primary objective is to improve engineering judgement.

Engineers who understand these principles can make better decisions,
produce higher quality software and collaborate more effectively with
both humans and AI.

# Scope

This handbook covers:

- Core engineering principles.
- Code organization and design.
- Quality and testing philosophy.
- Technical debt management.
- Engineering decision frameworks.
- AI integration principles.

Technology-specific guidance belongs in capability-specific handbooks
(e.g., Rails Engineering, Software Architecture).

# Principles

## Separation of Concerns

Every module, class, function or component should have a single, clearly
defined responsibility.

Code that attempts to do many things simultaneously is harder to
understand, harder to test and harder to change.

Applying separation of concerns means:

- Organising code by what it does rather than what it is.
- Extracting distinct responsibilities into separate modules.
- Ensuring each layer or component has a clear boundary.
- Keeping coupling loose and cohesion high.

See the [Engineering Glossary](../../glossary/engineering/README/) for definitions of coupling and cohesion.

## Encapsulation

Components should hide their internal implementation details behind a
stable interface.

Encapsulation enables change by ensuring that internal refactoring does
not affect consumers.

Well-encapsulated code:

- Exposes only what is necessary.
- Protects internal invariants.
- Can be changed without external impact.
- Is easier to reason about.

## Composition over Inheritance

Prefer composing behaviours from small, focused units over building deep
inheritance hierarchies.

Composition is more flexible, easier to test and less likely to produce
fragile code.

Inheritance is appropriate when:

- There is a genuine is-a relationship.
- The hierarchy is shallow (typically one or two levels).
- Behaviour is extended rather than overridden.

When in doubt, prefer composition.

## Dependency Inversion

High-level modules should not depend on low-level modules.

Both should depend on abstractions.

This principle enables:

- Swappable implementations.
- Easier testing through mocking or stubbing.
- Reduced coupling between layers.
- Evolution of implementations without affecting consumers.

Apply dependency inversion at architectural boundaries.

## Explicit Dependencies

Components should declare their dependencies explicitly rather than
obtaining them implicitly.

Explicit dependencies:

- Make the component's requirements visible.
- Simplify testing.
- Reduce hidden coupling.
- Improve readability.

Prefer dependency injection, constructor injection or service locators
over global state or static access.

## Consistency

Consistent code is easier to read, review and maintain.

Consistency applies to:

- Naming conventions.
- Code structure.
- Error handling patterns.
- Logging conventions.
- Testing approaches.

Follow the conventions established in the capability-specific handbooks.
When no convention exists, establish one rather than introducing a new
style.

## Defend against Complexity

Software complexity is the primary driver of long-term cost.

Complexity manifests as:

- Code that is hard to understand.
- Systems that are hard to change.
- Interactions that are hard to predict.
- Dependencies that are hard to manage.

Defend against complexity by:

- Preferring simple designs over clever ones.
- Decomposing large systems into small, independent modules.
- Establishing clear boundaries between components.
- Regularly refactoring toward simpler structures.
- Saying no to unnecessary features.

Simplicity is not simplicity of implementation.

It is simplicity of understanding.

## Prefer Clarity over Cleverness

Code is read far more often than it is written.

Optimise for the reader.

Clear code:

- Uses descriptive names.
- Expresses intent directly.
- Avoids unnecessary abstraction.
- Favours obvious solutions over clever ones.

If code is difficult to understand, it is difficult to maintain.

# Code Organization

## Module Boundaries

Organise code into modules with clear responsibilities.

Each module should:

- Have one primary purpose.
- Expose a well-defined interface.
- Minimise knowledge of other modules.
- Be independently testable.

## Layer Separation

Separate code into logical layers.

Common layers include:

- Presentation: Handles user interaction.
- Application: Orchestrates business operations.
- Domain: Contains business logic.
- Infrastructure: Manages technical concerns.

Each layer should depend only on the layer beneath it.

## Package by Feature

Organise code by feature rather than by layer.

Feature-based organisation:

- Groups related code together.
- Makes features self-contained.
- Simplifies navigation.
- Enables independent evolution.

# Engineering Standards

## Naming

Names should reveal intent.

Good names:

- Describe what something does.
- Use the vocabulary of the domain.
- Are specific rather than generic.
- Avoid abbreviations unless universally understood.

| Good | Avoid |
| --- | --- |
|------+-------|
| `UserRegistrationService` | `UserService` |
| --- | --- |
| `send_password_reset_email` | `handle_email` |
| `calculate_total_revenue` | `calc` |

## Error Handling

Errors are a normal part of software operation.

Engineers should:

- Handle errors at the appropriate level of abstraction.
- Never silently swallow exceptions.
- Provide meaningful error messages.
- Distinguish between recoverable and unrecoverable errors.
- Log errors with sufficient context for diagnosis.

## Logging

Logging should support operations.

Effective logging:

- Uses structured formats.
- Includes relevant context.
- Distinguishes severity levels.
- Avoids logging sensitive information.
- Follows consistent conventions.

## Testing

Every capability should define its testing standards.

Common principles include:

- Test behaviour, not implementation.
- Write tests that are readable and maintainable.
- Prefer fast, reliable tests over comprehensive slow ones.
- Follow the test pyramid: many unit tests, fewer integration tests,
  fewest end-to-end tests.

See the [Code Review Playbook](../../playbooks/code-review/README/) for testing review standards.

# Quality Philosophy

## Define Done

Every engineering task should have a clear definition of done.

A task is complete when:

- The change is implemented.
- Tests are written and passing.
- Code has been reviewed.
- Documentation has been updated.
- The change is deployed to production.

## Technical Debt

Technical debt is the gap between the current state of the code and the
desired state.

Some technical debt is strategic: taken intentionally to achieve a
business outcome with a plan to repay.

Some technical debt is accidental: accumulated through neglect,
inadequate design or insufficient testing.

Engineers should:

- Track technical debt explicitly.
- Distinguish strategic from accidental debt.
- Regularly allocate time for debt reduction.
- Document the reasoning behind intentional debt.

## Refactoring

Refactoring is the disciplined practice of improving code structure
without changing behaviour.

Refactoring should:

- Be driven by clear goals.
- Be supported by tests.
- Be done incrementally.
- Be reviewed as carefully as new code.

Regular refactoring prevents gradual decay.

# Decision Frameworks

## When to Introduce Abstraction

Ask these questions before introducing a new abstraction:

1. Does the abstraction simplify the code?
2. Is the abstraction likely to be reused?
3. Can we demonstrate at least three concrete use cases?
4. Does the abstraction hide genuine complexity?

If the answer to most questions is no, defer the abstraction.

## When to Accept Technical Debt

Technical debt may be acceptable when:

- The cost of delay exceeds the cost of repayment.
- The debt is explicitly tracked and scheduled.
- The team understands the trade-offs.
- The decision is documented for future engineers.

Technical debt is never acceptable when:

- It compromises security.
- It introduces production risk.
- It blocks future work.
- It is invisible to the team.

## When to Rewrite

Rewriting a system carries significant risk.

Consider a rewrite only when:

- The existing system cannot evolve to meet requirements.
- The cost of maintenance exceeds the cost of replacement.
- The team understands the existing domain and failure modes.
- Incremental improvement has been ruled out.

Prefer incremental improvement over wholesale replacement.

# AI Integration

## AI as Collaborator

AI systems should be treated as engineering collaborators.

They can assist with:

- Research and exploration.
- Drafting and outlining.
- Code generation.
- Review and analysis.
- Refactoring suggestions.
- Documentation generation.

## Human Responsibility

Human engineers remain responsible for all engineering decisions.

AI-generated code, designs or documentation must be reviewed by a human
before acceptance.

AI can accelerate engineering work, but it cannot replace engineering
judgement.

## Context for AI

AI systems are more effective when provided with:

- Clear scope and constraints.
- Relevant context documents.
- Defined terminology.
- Explicit success criteria.
- Examples of desired output.

See the [AI Engineering Handbook](../../handbooks/ai/README/) for detailed guidance on AI
workflows and context engineering.

# Capability Map

This handbook is the entry point for the Engineering Fundamentals
capability. The following documents form the complete capability:

## Handbooks

- [Engineering Fundamentals Handbook](./README/) — This document. Core
  engineering principles, quality philosophy and decision frameworks.

## Glossaries

- [Engineering Glossary](../../glossary/engineering/README/) — Foundational terminology (abstraction,
  cohesion, coupling, encapsulation, separation of concerns, etc.).

## Guides

- [Code Organization](../../guides/engineering/code-organization/) — Feature-based packaging, module
  boundaries, dependency flow, anti-patterns.
- [Error Handling](../../guides/engineering/error-handling/) — Recoverable vs unrecoverable errors,
  patterns, logging standards, anti-patterns.
- [Testing Strategies](../../guides/engineering/testing-strategies/) — Test pyramid, what to test, test
  doubles, sustainable testing practices.
- [Logging](../../guides/engineering/logging/) — Structured logging standards, log levels,
  context fields, anti-patterns.

## Learning Paths

- [Engineering Learning Paths](../../learning-paths/engineering/README/) — Beginner, intermediate and
  advanced tracks for engineering fundamentals.

## References

- [Engineering References](../../references/engineering/README/) — Quick lookup: design principles,
  patterns, testing, logging, error handling.

## AI Workflows

- [AI Workflows for Engineering](../../prompts/engineering-ai-workflows/) — Prompt patterns for code
  review, design exploration, refactoring, documentation.

# Related Documents

- [Engineering Glossary](../../glossary/engineering/README/)
- [Software Architecture Handbook](../../handbooks/architecture/README/)
- [Code Review Playbook](../../playbooks/code-review/README/)
- [Style Guide](../../style-guide/)
- [Writing Principles](../../writing-principles/)
- [Document Types](../../document-types/)
