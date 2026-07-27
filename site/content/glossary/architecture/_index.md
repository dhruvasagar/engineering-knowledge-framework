+++
title = "Architecture Glossary"
description = "Software architecture terminology used throughout the Engineering Knowledge Framework"
+++


# Purpose

This glossary defines the software architecture terminology used
throughout the Engineering Knowledge Framework.

Architecture terms defined here are authoritative across the entire
repository.

Foundational engineering terms are defined in the
[Engineering Glossary](..*engineering*README*).

# Glossary

## Architecture Decision Record (ADR)

| Property | Value |
| --- | --- |
| Definition | A short document that captures an architectural decision, |
|  | its context, alternatives considered and consequences. |
| Context | ADRs provide a historical record of why the system is |
|  | the way it is. They enable future engineers to |
|  | understand past reasoning and avoid repeating mistakes. |
| Related | [[#rfc][RFC]], [[#decision-log][Decision Log]] |
| References | [Software Architecture Handbook](..*..*handbooks*architecture*README*) |

## Bounded Context

| Property | Value |
| --- | --- |
| Definition | A logical boundary within which a particular domain |
|  | model applies, with its own ubiquitous language and |
|  | internal consistency. |
| Context | Bounded contexts are a core concept in Domain-Driven |
|  | Design. They define the boundaries of microservices, |
|  | modules and team ownership. |
| Related | [[#domain-driven-design][Domain-Driven Design]] |
| References | [Software Architecture Handbook](../..*handbooks*architecture*README*) |

## C4 Model

| Property | Value |
| --- | --- |
| Definition | A hierarchical approach to visualizing software |
|  | architecture at four levels: System Context, Container, |
|  | Component and Code. |
| Context | The C4 model provides a structured way to communicate |
|  | architecture to different audiences, from stakeholders |
|  | to developers. |
| Related | [[#architecture-decision-record-adr][ADR]] |
| References | [Software Architecture Handbook](../..*handbooks*architecture*README*) |

## Decision Log

| Property | Value |
| --- | --- |
| Definition | A chronological index of all architectural decisions |
|  | made for a system, with links to the corresponding ADRs. |
| Context | The decision log provides a single entry point for |
|  | understanding the architectural history of a system. |
| Related | [[#architecture-decision-record-adr][ADR]], [[#rfc][RFC]] |
| References | [Software Architecture Handbook](../..*handbooks*architecture*README*) |

## Domain-Driven Design (DDD)

| Property | Value |
| --- | --- |
| Definition | An approach to software development that emphasizes |
|  | modeling the domain and its logic using a shared |
|  | ubiquitous language between domain experts and |
|  | engineers. |
| Context | DDD provides patterns for handling complex domain |
|  | logic, including entities, value objects, aggregates, |
|  | repositories and domain events. |
| Related | [[#bounded-context][Bounded Context]], [[#event-storming][Event Storming]] |
| References | [Software Architecture Handbook](../..*handbooks*architecture*README*) |

## Event Storming

| Property | Value |
| --- | --- |
| Definition | A collaborative modelling technique for exploring |
|  | complex business domains through events, commands and |
|  | aggregates. |
| Context | Event storming brings domain experts and engineers |
|  | together to build a shared understanding of the domain. |
|  | It is particularly useful for designing event-driven |
|  | systems. |
| Related | [[#domain-driven-design][Domain-Driven Design]], [[#bounded-context][Bounded Context]] |
| References | [Software Architecture Handbook](../..*handbooks*architecture*README*) |

## Hexagonal Architecture

| Property | Value |
| --- | --- |
| Definition | An architectural pattern that isolates core business |
|  | logic from external concerns through ports (interfaces) |
|  | and adapters (implementations). |
| Context | Also known as Ports and Adapters. The core domain has |
|  | no dependency on databases, APIs, UIs or other external |
|  | systems, improving testability and evolvability. |
| Related | [[#layered-architecture][Layered Architecture]] |
| References | [Software Architecture Handbook](../..*handbooks*architecture*README*) |

## Layered Architecture

| Property | Value |
| --- | --- |
| Definition | An architectural pattern that organizes the system into |
|  | horizontal layers (presentation, application, domain, |
|  | infrastructure), each with a specific responsibility. |
| Context | Each layer depends only on the layer directly beneath |
|  | it. This is the most widely understood architectural |
|  | pattern but can lead to leaky abstractions. |
| Related | [[#hexagonal-architecture][Hexagonal Architecture]] |
| References | [Software Architecture Handbook](../..*handbooks*architecture*README*) |

## Quality Attribute

| Property | Value |
| --- | --- |
| Definition | A measurable or testable property of a system that |
|  | indicates how well it satisfies stakeholder concerns |
|  | beyond functional requirements. |
| Context | Common quality attributes include performance, |
|  | scalability, availability, security, maintainability, |
|  | evolvability, operability and testability. Every |
|  | architectural decision involves trade-offs between |
|  | quality attributes. |
| Related | [[#architecture-decision-record-adr][ADR]], [[#trade-off][Trade-off]] |
| References | [Software Architecture Handbook](../..*handbooks*architecture*README*) |

## RFC (Request for Comments)

| Property | Value |
| --- | --- |
| Definition | A proposal document for a significant architectural |
|  | change that invites review and discussion before a |
|  | decision is made. |
| Context | RFCs are used for changes that have broad impact, |
|  | involve significant trade-offs or affect multiple |
|  | teams. They precede ADRs, which capture the final |
|  | decision. |
| Related | [[#architecture-decision-record-adr][ADR]], [[#decision-log][Decision Log]] |
| References | [Software Architecture Handbook](../..*handbooks*architecture*README*) |

## Trade-off

| Property | Value |
| --- | --- |
| Definition | The recognition that improving one quality attribute or |
|  | characteristic of a system inevitably impacts another. |
| Context | Architecture is the art of managing trade-offs. Every |
|  | decision optimises for some outcomes at the expense of |
|  | others. Good architecture makes trade-offs explicit. |
| Related | [[#quality-attribute][Quality Attribute]], [[#architecture-decision-record-adr][ADR]] |
| References | [Software Architecture Handbook](../..*handbooks*architecture*README*) |

# Related Documents

- [Software Architecture Handbook](../..*handbooks*architecture*README*)
- [Engineering Glossary](..*engineering*README*)
- [ADR Template](..*..*templates*adr*README*)
- [Style Guide](../..*STYLE_GUIDE*)
- [Glossary Overview](..*README*)
