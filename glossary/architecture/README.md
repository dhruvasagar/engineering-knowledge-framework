# Purpose

This glossary defines the software architecture terminology used
throughout the Engineering Knowledge Framework.

Architecture terms defined here are authoritative across the entire
repository.

Foundational engineering terms are defined in the
[Engineering Glossary](../engineering/README.md).

# Glossary

## Architecture Decision Record (ADR) {#architecture-decision-record}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | A short document that captures an architectural decision, |
| --- | --- |
|  | its context, alternatives considered and consequences. |
| Context | ADRs provide a historical record of why the system is |
|  | the way it is. They enable future engineers to |
|  | understand past reasoning and avoid repeating mistakes. |
| Related | [RFC](#rfc), [Decision Log](#decision-log) |
| References | [Software Architecture Handbook](../../handbooks/architecture/README.md) |

## Bounded Context {#bounded-context}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | A logical boundary within which a particular domain |
| --- | --- |
|  | model applies, with its own ubiquitous language and |
|  | internal consistency. |
| Context | Bounded contexts are a core concept in Domain-Driven |
|  | Design. They define the boundaries of microservices, |
|  | modules and team ownership. |
| Related | [Domain-Driven Design](#domain-driven-design) |
| References | [Software Architecture Handbook](../../handbooks/architecture/README.md) |

## C4 Model {#c4-model}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | A hierarchical approach to visualizing software |
| --- | --- |
|  | architecture at four levels: System Context, Container, |
|  | Component and Code. |
| Context | The C4 model provides a structured way to communicate |
|  | architecture to different audiences, from stakeholders |
|  | to developers. |
| Related | [ADR](#architecture-decision-record) |
| References | [Software Architecture Handbook](../../handbooks/architecture/README.md) |

## Decision Log {#decision-log}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | A chronological index of all architectural decisions |
| --- | --- |
|  | made for a system, with links to the corresponding ADRs. |
| Context | The decision log provides a single entry point for |
|  | understanding the architectural history of a system. |
| Related | [ADR](#architecture-decision-record), [RFC](#rfc) |
| References | [Software Architecture Handbook](../../handbooks/architecture/README.md) |

## Domain-Driven Design (DDD) {#domain-driven-design}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | An approach to software development that emphasizes |
| --- | --- |
|  | modeling the domain and its logic using a shared |
|  | ubiquitous language between domain experts and |
|  | engineers. |
| Context | DDD provides patterns for handling complex domain |
|  | logic, including entities, value objects, aggregates, |
|  | repositories and domain events. |
| Related | [Bounded Context](#bounded-context), [Event Storming](#event-storming) |
| References | [Software Architecture Handbook](../../handbooks/architecture/README.md) |

## Event Storming {#event-storming}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | A collaborative modelling technique for exploring |
| --- | --- |
|  | complex business domains through events, commands and |
|  | aggregates. |
| Context | Event storming brings domain experts and engineers |
|  | together to build a shared understanding of the domain. |
|  | It is particularly useful for designing event-driven |
|  | systems. |
| Related | [Domain-Driven Design](#domain-driven-design), [Bounded Context](#bounded-context) |
| References | [Software Architecture Handbook](../../handbooks/architecture/README.md) |

## Hexagonal Architecture {#hexagonal-architecture}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | An architectural pattern that isolates core business |
| --- | --- |
|  | logic from external concerns through ports (interfaces) |
|  | and adapters (implementations). |
| Context | Also known as Ports and Adapters. The core domain has |
|  | no dependency on databases, APIs, UIs or other external |
|  | systems, improving testability and evolvability. |
| Related | [Layered Architecture](#layered-architecture) |
| References | [Software Architecture Handbook](../../handbooks/architecture/README.md) |

## Layered Architecture {#layered-architecture}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | An architectural pattern that organizes the system into |
| --- | --- |
|  | horizontal layers (presentation, application, domain, |
|  | infrastructure), each with a specific responsibility. |
| Context | Each layer depends only on the layer directly beneath |
|  | it. This is the most widely understood architectural |
|  | pattern but can lead to leaky abstractions. |
| Related | [Hexagonal Architecture](#hexagonal-architecture) |
| References | [Software Architecture Handbook](../../handbooks/architecture/README.md) |

## Quality Attribute {#quality-attribute}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | A measurable or testable property of a system that |
| --- | --- |
|  | indicates how well it satisfies stakeholder concerns |
|  | beyond functional requirements. |
| Context | Common quality attributes include performance, |
|  | scalability, availability, security, maintainability, |
|  | evolvability, operability and testability. Every |
|  | architectural decision involves trade-offs between |
|  | quality attributes. |
| Related | [ADR](#architecture-decision-record), [Trade-off](#trade-off) |
| References | [Software Architecture Handbook](../../handbooks/architecture/README.md) |

## RFC (Request for Comments) {#rfc}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | A proposal document for a significant architectural |
| --- | --- |
|  | change that invites review and discussion before a |
|  | decision is made. |
| Context | RFCs are used for changes that have broad impact, |
|  | involve significant trade-offs or affect multiple |
|  | teams. They precede ADRs, which capture the final |
|  | decision. |
| Related | [ADR](#architecture-decision-record), [Decision Log](#decision-log) |
| References | [Software Architecture Handbook](../../handbooks/architecture/README.md) |

## Trade-off {#trade-off}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | The recognition that improving one quality attribute or |
| --- | --- |
|  | characteristic of a system inevitably impacts another. |
| Context | Architecture is the art of managing trade-offs. Every |
|  | decision optimises for some outcomes at the expense of |
|  | others. Good architecture makes trade-offs explicit. |
| Related | [Quality Attribute](#quality-attribute), [ADR](#architecture-decision-record) |
| References | [Software Architecture Handbook](../../handbooks/architecture/README.md) |

# Related Documents

- [Software Architecture Handbook](../../handbooks/architecture/README.md)
- [Engineering Glossary](../engineering/README.md)
- [ADR Template](../../templates/adr/README.md)
- [Style Guide](../../style-guide.md)
- [Glossary Overview](../README.md)
