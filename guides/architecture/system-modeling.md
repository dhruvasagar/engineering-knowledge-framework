# Purpose

System modeling is the practice of creating abstract representations of
a software system to communicate its structure, behaviour and
constraints.

Models enable engineers to reason about architecture at different
levels of detail, discuss trade-offs, and document decisions in a
shared visual language.

This guide covers the C4 model for structural diagrams and event
modeling for designing event-driven systems.

# Background

Software systems are complex. No single diagram can capture every
aspect of a system.

Different audiences need different views:

| Audience | Needs |
| --- | --- |
|--------------------+----------------------------------------------|
| Stakeholders | System context, boundaries, external |
| --- | --- |
|  | integrations. |
| Engineers | Component structure, interactions, data flow. |
| New team members | High-level orientation, key concepts. |
| Operations | Deployment topology, infrastructure. |

Using a consistent modeling approach ensures that diagrams across the
organization use the same conventions and are understandable by
everyone.

# The C4 Model

The C4 model provides a hierarchical approach to visualizing software
architecture at four levels.

## Level 1: System Context

Shows the system being built, its users and the external systems it
integrates with.

Purpose: Provide a high-level overview for everyone from stakeholders
to developers.

```
[Customer] ──→ [Order Management System] ←── [Payment Gateway]
                                    ↓
                              [Notification Service]
```

Recommended for: Every system. This is the starting point for any
architecture discussion.

## Level 2: Container

Shows the high-level technology choices and how responsibilities are
distributed across containers (applications, services, databases).

A container is a separately runnable or deployable unit.

```
[Web App] ──→ [API Service] ──→ [Database]
                ↓
           [Background Worker] ──→ [Queue]
```

Recommended for: Every system. Essential for understanding deployment
boundaries and technology choices.

## Level 3: Component

Shows the major structural components inside a container and their
interactions.

Components are the building blocks within a container (modules,
controllers, services, repositories).

```
[OrderController] ──→ [OrderService] ──→ [OrderRepository] ──→ [Database]
                         ↓
                   [PaymentService] ──→ [PaymentGateway]
```

Recommended for: Complex containers. Useful for onboarding and design
reviews.

## Level 4: Code

Shows the implementation details of a specific component.

Typically represented as a class diagram, entity relationship diagram
or detailed design document.

Recommended for: Critical or complex components where implementation
detail matters.

## Diagram Standards

All C4 diagrams should follow these conventions:

- Use boxes for elements, arrows for relationships.
- Label relationships with a description of the interaction.
- Use consistent colours for element types (person, system, container,
  component).
- Include a legend for any non-standard notation.
- Store diagrams in [assets*diagrams*](../../assets/diagrams/) as source files (PlantUML,
  Mermaid, or draw.io).

# Event Modeling

Event modeling is a collaborative technique for designing systems driven
by events and commands.

It is particularly useful for:

- Event-driven architectures.
- Microservices with asynchronous communication.
- Systems with complex business workflows.
- Designing bounded contexts and aggregates.

## Core Concepts

| Concept | Meaning |
| --- | --- |
|----------+--------------------------------------------------------|
| Event | Something that has happened in the past. Immutable. |
| --- | --- |
|  | Examples: OrderPlaced, PaymentReceived, InvoiceSent. |
| Command | An intention to perform an action. May be rejected. |
|  | Examples: PlaceOrder, ProcessPayment, SendInvoice. |
| Aggregate | A cluster of domain objects treated as a unit. |
|  | Ensures consistency within its boundary. |

## Workshop Format

Event modeling is typically done as a collaborative workshop with
domain experts and engineers.

1. ***Big Picture***: Identify business events across the domain.
   Place events on a timeline from left to right.
2. ***Process Level***: Add commands, actors and read models for each
   workflow.
3. ***Design Level***: Define aggregates, commands, events and
   constraints for each bounded context.

## Artefacts

The workshop produces:

- An event timeline showing the sequence of business events.
- Bounded context boundaries and their relationships.
- Aggregate definitions with commands and events.
- Read models for each user-facing view.
- Integration contracts between contexts.

# Choosing the Right Model

| Situation | Recommended Approach |
| --- | --- |
|-----------------------------------------+-----------------------------------------|
| New system, need to communicate | C4 Level 1-2: Context and Container |
| --- | --- |
| overall architecture | diagrams |
|-----------------------------------------+-----------------------------------------|
| Complex component, need detail | C4 Level 3-4: Component and Code |
| --- | --- |
|-----------------------------------------+-----------------------------------------|
| Designing an event-driven system | Event modeling workshop |
| --- | --- |
|-----------------------------------------+-----------------------------------------|
| Exploring a new domain | Event modeling big picture |
| --- | --- |
|-----------------------------------------+-----------------------------------------|
| Documenting existing architecture | C4 Level 1-3: Reverse-engineer diagrams |
| --- | --- |
|-----------------------------------------+-----------------------------------------|
| Defining service boundaries | Event modeling or DDD context mapping |
| --- | --- |

# Keeping Models Current

Outdated diagrams are worse than no diagrams because they actively
mislead.

- Treat diagrams as living documentation.
- Update diagrams as part of the implementation work.
- Review diagrams during architecture reviews.
- Use automated tools where possible (diagrams from code, ADR
  references).

A diagram that is 80% accurate and up to date is more valuable than a
diagram that is 100% accurate but six months out of date.

# AI Integration

AI assistants can help with system modeling by:

- Generating C4 diagrams from natural language descriptions.
- Suggesting bounded context boundaries from domain descriptions.
- Identifying missing events or commands in event models.
- Converting between modeling formats (PlantUML, Mermaid, text).
- Reviewing diagrams for consistency with written architecture.

When asking AI for modeling assistance, provide:

- The purpose and audience for the diagram.
- The system's key elements and their relationships.
- Any existing diagrams or descriptions.
- The preferred diagram format.

# Related Documents

- [Software Architecture Handbook](../../handbooks/architecture/README.md)
- [Architectural Patterns Guide](../../guides/architecture/architectural-patterns.md)
- [Architecture Review Playbook](../../playbooks/architecture-review/README.md)
- [Architecture Glossary](../../glossary/architecture/README.md)
- [Diagrams Directory](../../assets/diagrams/)
