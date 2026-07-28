---
title: "Engineering Glossary"
description: "Canonical engineering terminology used throughout the Engineering Knowledge Framework"
---


# Purpose

This glossary defines the foundational engineering terminology used
throughout the Engineering Knowledge Framework.

Every term defined here is authoritative across the entire repository.

Capability-specific terminology belongs in the corresponding capability
glossary (e.g., [Architecture Glossary](../architecture/README/), [Rails Glossary](../rails/README/)).

# Glossary

## Abstraction

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | The process of hiding implementation details behind a |
| --- | --- |
|  | simplified interface, exposing only essential |
|  | characteristics. |
| Context | Abstraction reduces complexity by allowing engineers to |
|  | work at a higher level of understanding. It is a |
|  | fundamental tool for managing software complexity. |
| Related | [Encapsulation](#encapsulation), [Modularity](#modularity) |
| References | [Engineering Fundamentals Handbook](../../handbooks/engineering/README/) |

## Cohesion

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | The degree to which elements within a module belong |
| --- | --- |
|  | together and serve a single, well-defined purpose. |
| Context | High cohesion indicates that a module's responsibilities |
|  | are closely related and focused. Low cohesion means a |
|  | module attempts to do many unrelated things. High |
|  | cohesion is preferred. |
| Related | [Coupling](#coupling), [Separation of Concerns](#separation-of-concerns) |
| References | [Engineering Fundamentals Handbook](../../handbooks/engineering/README/) |

## Composition

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | A design principle in which complex behaviour is built |
| --- | --- |
|  | by combining small, focused, reusable components rather |
|  | than inheriting behaviour from a parent class. |
| Context | Composition is preferred over inheritance in most |
|  | cases because it is more flexible, easier to test and |
|  | less likely to produce fragile code. |
| Related | [Coupling](#coupling), [Encapsulation](#encapsulation) |
| References | [Engineering Fundamentals Handbook](../../handbooks/engineering/README/) |

## Coupling

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | The degree of dependency between two modules or |
| --- | --- |
|  | components. |
| Context | Loose coupling means modules interact through stable, |
|  | minimal interfaces and can be changed independently. |
|  | Tight coupling means changes to one module require |
|  | changes to others. Loose coupling is preferred. |
| Related | [Cohesion](#cohesion), [Encapsulation](#encapsulation) |
| References | [Engineering Fundamentals Handbook](../../handbooks/engineering/README/) |

## Dependency Injection

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | A technique in which an object receives its dependencies |
| --- | --- |
|  | from an external source rather than creating them |
|  | internally. |
| Context | Dependency injection makes dependencies explicit, |
|  | simplifies testing and reduces coupling. Common forms |
|  | include constructor injection, setter injection and |
|  | interface injection. |
| Related | [Coupling](#coupling), [Encapsulation](#encapsulation) |
| References | [Engineering Fundamentals Handbook](../../handbooks/engineering/README/) |

## Encapsulation

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | The practice of hiding internal implementation details |
| --- | --- |
|  | behind a stable interface, protecting internal |
|  | invariants from external interference. |
| Context | Encapsulation enables change by ensuring that internal |
|  | refactoring does not affect consumers. A well- |
|  | encapsulated component exposes only what is necessary. |
| Related | [Abstraction](#abstraction), [Modularity](#modularity) |
| References | [Engineering Fundamentals Handbook](../../handbooks/engineering/README/) |

## Modularity

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | The degree to which a system is composed of discrete, |
| --- | --- |
|  | independent modules that can be developed, tested and |
|  | changed in isolation. |
| Context | Modularity is a key tool for managing complexity. It |
|  | enables parallel development, simplifies testing and |
|  | reduces the impact of changes. |
| Related | [Cohesion](#cohesion), [Coupling](#coupling), [Encapsulation](#encapsulation) |
| References | [Engineering Fundamentals Handbook](../../handbooks/engineering/README/) |

## Refactoring

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | The disciplined practice of improving code structure |
| --- | --- |
|  | without changing its observable behaviour. |
| Context | Refactoring is an ongoing activity, not a separate |
|  | project. It should be driven by clear goals, supported |
|  | by tests and done incrementally. |
| Related | [Technical Debt](#technical-debt) |
| References | [Engineering Fundamentals Handbook](../../handbooks/engineering/README/) |

## Separation of Concerns

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | A design principle stating that each module, class, |
| --- | --- |
|  | function or component should have a single, clearly |
|  | defined responsibility. |
| Context | Separation of concerns is the foundation of modular |
|  | design. It reduces complexity, improves maintainability |
|  | and enables independent evolution of different parts |
|  | of a system. |
| Related | [Cohesion](#cohesion), [Coupling](#coupling), [Modularity](#modularity) |
| References | [Engineering Fundamentals Handbook](../../handbooks/engineering/README/) |

## Technical Debt

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | The gap between the current state of a codebase and the |
| --- | --- |
|  | desired state, representing future work required to |
|  | address suboptimal design, implementation or testing |
|  | decisions. |
| Context | Technical debt may be strategic (intentional with a |
|  | plan to repay) or accidental (accumulated through |
|  | neglect). All technical debt should be tracked |
|  | explicitly and regularly addressed. |
| Related | [Refactoring](#refactoring) |
| References | [Engineering Fundamentals Handbook](../../handbooks/engineering/README/) |

# Related Documents

- [Engineering Fundamentals Handbook](../../handbooks/engineering/README/)
- [Style Guide](../../style-guide/)
- [Writing Principles](../../writing-principles/)
- [Glossary Overview](../README/)
