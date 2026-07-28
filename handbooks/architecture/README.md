# Purpose

Software architecture is the set of design decisions that shape a system
and are costly to change.

This handbook defines the principles, patterns and decision frameworks
that guide architectural work within this organization.

Architecture is not simply the structure of a system.

It is the reasoning behind that structure.

This document focuses on enduring architectural thinking that remains
valuable regardless of technology stacks or deployment models.

# Scope

This handbook covers:

- Architectural principles and philosophy.
- Architectural patterns and when to apply them.
- Decision documentation standards (ADRs, RFCs).
- System design and modeling approaches.
- Quality attribute trade-offs.
- Architecture review practices.
- AI integration in architectural work.

Implementation-specific architectural guidance belongs in
capability-specific handbooks (e.g., Rails Engineering, Security
Engineering).

# Principles

## Architecture as Trade-offs

Every architectural decision involves trade-offs.

There are no perfect architectures.

There are only architectures that optimise for different outcomes.

Engineers should:

- Identify which trade-offs a decision introduces.
- Document both the chosen and rejected alternatives.
- Explain the reasoning behind each decision.
- Revisit decisions when context changes.

## Align Architecture with Business Goals

Architecture exists to serve business outcomes.

Architectural decisions should be guided by:

- System goals and constraints.
- Expected evolution and growth.
- Operational requirements.
- Team structure and capabilities.
- Organisational context.

An architecture that serves business goals is more valuable than one
that is technically elegant.

## Evolvability over Perfection

Systems evolve.

Architecture should anticipate change without attempting to predict it.

Prefer architectures that:

- Enable incremental change.
- Isolate change impact.
- Make dependencies explicit.
- Support experimentation.
- Allow reversible decisions.

An evolvable architecture that exists is better than a perfect
architecture that is never built.

## Minimise Accidental Complexity

Architecture should solve essential complexity, not create accidental
complexity.

Essential complexity arises from the domain.

Accidental complexity arises from the architecture itself.

When evaluating architectural choices, ask:

- Does this simplify or complicate the system?
- Does this reduce or increase cognitive load?
- Does this make change easier or harder?

## Prefer Simple Integration

Integration between components is a primary source of complexity.

Prefer:

- Simple interfaces over complex protocols.
- Synchronous communication where appropriate.
- Asynchronous communication where necessary.
- Well-defined contracts between services.

## Document Architectural Decisions

Undocumented architecture is invisible architecture.

Every significant architectural decision should be documented so that
future engineers can understand:

- Why the decision was made.
- What alternatives were considered.
- What trade-offs were accepted.

See the [ADR Template](../../templates/adr/README.md) for the standard decision documentation format.

# Architectural Patterns

## Layered Architecture

Organise the system into horizontal layers, each with a specific
responsibility.

| Layer | Responsibility |
| --- | --- |
|---------------+---------------------------------------|
| Presentation | User interaction and interface |
| --- | --- |
| Application | Request handling and orchestration |
| Domain | Business logic and rules |
| Infrastructure | Technical capabilities and persistence |

Each layer depends only on the layer directly beneath it.

***Use when:***

- The system has clear separation of concerns.
- The team is organised around technical skills.
- The system is relatively stable in structure.

***Avoid when:***

- Layers become leaky abstractions.
- Performance requires bypassing layers.
- The domain is complex and cross-cutting.

## Hexagonal Architecture (Ports and Adapters)

Isolate core business logic from external concerns (databases, APIs,
UIs) through ports (interfaces) and adapters (implementations).

The core domain has no dependency on external systems.

***Use when:***

- The domain is complex and central to the business.
- The system integrates with multiple external systems.
- Testability of business logic is a priority.

***Avoid when:***

- The system is simple and unlikely to change.
- The overhead of indirection exceeds its benefit.
- The team is unfamiliar with the pattern.

## Event-Driven Architecture

Components communicate through events rather than direct calls.

Producers emit events without knowing which consumers will handle them.

***Use when:***

- Loose coupling between components is essential.
- Workflows are asynchronous or long-running.
- Multiple consumers need to react to the same occurrence.

***Avoid when:***

- Workflow visibility and debugging are priorities.
- Event ordering and consistency are difficult to guarantee.
- The team lacks experience with event-driven systems.

## Microservices Architecture

Compose the system from independently deployable services, each owning
its own data and domain.

***Use when:***

- Teams are aligned around bounded contexts.
- Independent scaling and deployment are required.
- The system is large enough to justify the operational overhead.

***Avoid when:***

- The system is small or early in its lifecycle.
- The team lacks operational maturity.
- Network complexity and latency are significant concerns.

# Decision Documentation

## Architecture Decision Records

Every significant architectural decision should be recorded as an ADR.

An ADR answers:

- What was decided?
- Why was it decided?
- What alternatives were considered?
- What are the consequences?

ADR files are stored in the [adr/](../../adr/0001-capability-model.md) directory.

See the [ADR Template](../../templates/adr/README.md) for the standard format.

## RFCs

Major architectural changes should follow the RFC process.

An RFC proposes a significant change and invites review before a
decision is made.

RFC files are stored in the [rfc/](../../templates/rfc/README.md) directory (see the RFC template for the format).

## Decision Log

The decision log provides a chronological index of all architectural
decisions.

Each entry links to the corresponding ADR and summarises the decision
and its context.

# System Modeling

## C4 Model

The C4 model provides a hierarchical approach to communicating
architecture.

| Level | View | Audience |
| --- | --- | --- |
|-------+----------------------+---------------------|
| 1 | System Context | Everyone |
| --- | --- | --- |
| 2 | Container | Technical team |
| 3 | Component | Developers |
| 4 | Code | Developers (detail) |

Each level answers different questions about the system.

Diagrams should follow the C4 conventions and be stored in
[assets/diagrams/](../../assets/diagrams/).

## Event Modeling

Event modeling is a collaborative technique for designing systems driven
by events and commands.

It is particularly useful for event-driven and microservices
architectures.

# Quality Attributes

Architecture must balance competing quality attributes.

| Attribute | Consideration |
| --- | --- |
|----------------+---------------------------------------------------------|
| Performance | Response time, throughput, latency |
| --- | --- |
| Scalability | Ability to handle increased load |
| Availability | Uptime, fault tolerance, disaster recovery |
| Security | Authentication, authorisation, data protection |
| Maintainability | Ease of change, testing, and debugging |
| Evolvability | Ability to adapt to new requirements |
| Operability | Monitoring, deployment, incident response |
| Testability | Ability to verify correctness at every level |

Every architectural decision should explicitly consider its impact on
relevant quality attributes.

# Architecture Review

Architecture reviews ensure that decisions are sound, well-documented
and aligned with principles.

Reviews should focus on:

- Are the trade-offs understood and documented?
- Does the architecture support business goals?
- Are quality attributes addressed?
- Is the architecture documented appropriately?
- Can the architecture evolve?

See the [Architecture Review Playbook](../../playbooks/architecture-review/README.md) for the complete review
workflow.

# AI Integration

## AI in Architecture

AI can assist architectural work through:

- Pattern analysis and recommendation.
- Decision documentation and ADR drafting.
- Trade-off analysis and comparison.
- Diagram generation from descriptions.
- Review and gap analysis.

## AI Limitations

AI cannot replace architectural judgement.

Key limitations include:

- AI lacks deep understanding of business context.
- AI cannot evaluate organisational constraints.
- AI may recommend popular but inappropriate patterns.
- AI-generated decisions must be reviewed by a human architect.

## Context for AI

When using AI for architectural work, provide:

- System goals and constraints.
- Quality attribute requirements.
- Team and organisational context.
- Existing architectural decisions.
- Technology constraints and preferences.

See the [AI Engineering Handbook](../../handbooks/ai/README.md) for detailed AI workflow guidance.

# Capability Map

This handbook is the entry point for the Software Architecture
capability. The following documents form the complete capability:

## Handbooks

- [Software Architecture Handbook](./README.md) — This document. Principles,
  patterns, decision frameworks and documentation standards.

## Glossaries

- [Architecture Glossary](../../glossary/architecture/README.md) — Terminology (ADR, C4, DDD, hexagonal
  architecture, quality attributes, trade-offs).

## Guides

- [ADR Writing Guide](../../guides/architecture/adr-writing-guide.md) — When and how to write ADRs, lifecycle,
  characteristics of good ADRs, common mistakes.
- [Architectural Patterns](../../guides/architecture/architectural-patterns.md) — Pattern catalogue with trade-offs
  and selection guidance.
- [API Design](../../guides/architecture/api-design.md) — RESTful conventions, versioning, status codes,
  error formats.
- [System Modeling](../../guides/architecture/system-modeling.md) — C4 model levels, event modeling
  techniques and workshop format.

## Playbooks

- [Architecture Review Playbook](../../playbooks/architecture-review/README.md) — Review workflow with
  scope, team assembly, evaluation criteria.

## Checklists

- [Architecture Review Checklist](../../checklists/architecture-review.md) — Pre, during and
  post-review verification.

## Templates

- [ADR Template](../../templates/adr/README.md) — Standard format for Architecture Decision
  Records.
- [RFC Template](../../templates/rfc/README.md) — Format for major architectural proposals.

## Learning Paths

- [Architecture Learning Paths](../../learning-paths/architecture/README.md) — Beginner, intermediate and
  advanced tracks for software architecture.

## References

- [Architecture References](../../references/architecture/README.md) — Quick lookup: C4 model, pattern
  comparison, HTTP codes, quality attributes, ADR lifecycle.

## AI Workflows

- [AI Workflows for Architecture](../../prompts/architecture-ai-workflows.md) — Prompt patterns for
  trade-off analysis, ADR drafting, pattern selection and review.

# Related Documents

- [Architecture Glossary](../../glossary/architecture/README.md)
- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
- [Architecture Review Playbook](../../playbooks/architecture-review/README.md)
- [ADR Template](../../templates/adr/README.md)
- [Style Guide](../../style-guide.md)
- [Document Types](../../document-types.md)
