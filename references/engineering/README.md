+++
title = "Engineering References"
description = "Quick-reference material for engineering fundamentals"
+++


# Purpose

Quick-reference material for engineering fundamentals.

These references are intended for lookup rather than learning. For
in-depth explanations, see the referenced guides and handbooks.

# Design Principles Quick Reference

| Principle | Core Idea |
| --- | --- |
|-------------------------+--------------------------------------------------|
| Separation of Concerns | Each module has one clearly defined |
| --- | --- |
|  | responsibility. |
| Encapsulation | Hide implementation behind a stable interface. |
| Composition over | Build behaviour by combining small, focused |
| Inheritance | components. |
| Dependency Inversion | Depend on abstractions, not concretions. |
| Explicit Dependencies | Declare dependencies openly; avoid implicit |
|  | global state. |
| Consistency | Follow established conventions; maintain uniform |
|  | style. |
| Defend against | Prefer simple designs; decompose large systems; |
| Complexity | refactor regularly. |
| Prefer Clarity over | Optimize for the reader; avoid clever but |
| Cleverness | obscure solutions. |

# Code Organization Patterns

| Pattern | Structure | Use When |
| --- | --- | --- |
|----------------------+------------------------------+------------------------------------|
| Package by Feature | Group code by business | Most applications; clear domain |
| --- | --- | --- |
|  | feature. | boundaries. |
|----------------------+------------------------------+------------------------------------|
| Package by Layer | Group by technical role | Small applications; stable layers. |
| --- | --- | --- |
|  | (controllers, models). |  |
|----------------------+------------------------------+------------------------------------|
| Package by Component | Group by deployable unit. | Large systems with strong |
| --- | --- | --- |
|  |  | subsystem boundaries. |

# Testing Quick Reference

| Concept | Guideline |
| --- | --- |
|------------------+-----------------------------------------------------|
| Test pyramid | Many unit, some integration, few end-to-end. |
| --- | --- |
|------------------+-----------------------------------------------------|
| What to test | Public interfaces, boundary conditions, error paths. |
| --- | --- |
|------------------+-----------------------------------------------------|
| What not to test | Framework code, generated code, infrastructure. |
| --- | --- |
|------------------+-----------------------------------------------------|
| Test doubles | Stubs for values, fakes for slow deps, mocks |
| --- | --- |
|  | sparingly. |
|------------------+-----------------------------------------------------|
| Structure | Arrange, Act, Assert. |
| --- | --- |

# Log Levels

| Level | Meaning |
| --- | --- |
|-------+------------------------------------------------------|
| ERROR | Failure requiring human investigation. |
| --- | --- |
|-------+------------------------------------------------------|
| WARN | Unexpected condition handled gracefully. |
| --- | --- |
|-------+------------------------------------------------------|
| INFO | Significant lifecycle events. |
| --- | --- |
|-------+------------------------------------------------------|
| DEBUG | Detailed diagnostic information (disabled in |
| --- | --- |
|  | production under normal operation). |
|-------+------------------------------------------------------|
| TRACE | Very detailed tracing for specific requests. |
| --- | --- |

# Error Handling

| Concept | Guideline |
| --- | --- |
|-----------------------+-----------------------------------------------------|
| Recoverable errors | Handle gracefully; continue operation. |
| --- | --- |
|-----------------------+-----------------------------------------------------|
| Unrecoverable errors | Fail fast with full context. |
| --- | --- |
|-----------------------+-----------------------------------------------------|
| Error propagation | Handle at the level with enough context to decide. |
| --- | --- |
|-----------------------+-----------------------------------------------------|
| Error messages | Include what, what was attempted, identifiers. |
| --- | --- |
|-----------------------+-----------------------------------------------------|
| Logging | Structured format; never log sensitive data. |
| --- | --- |

# Technical Debt Classification

| Category | Characteristics | Approach |
| --- | --- | --- |
|-------------+------------------------------------+----------------------------------|
| Strategic | Intentional, with plan to repay. | Track, schedule, communicate. |
| --- | --- | --- |
|-------------+------------------------------------+----------------------------------|
| Accidental | Accumulated through neglect. | Assess, prioritize, reduce |
| --- | --- | --- |
|  |  | incrementally. |

# Recommended Reading

| Title | Author | Focus |
| --- | --- | --- |
|--------------------------------------+-----------------+----------------------------|
| Clean Architecture | Robert C. Martin | Architectural principles |
| --- | --- | --- |
|--------------------------------------+-----------------+----------------------------|
| The Pragmatic Programmer | Hunt & Thomas | Engineering practice |
| --- | --- | --- |
|--------------------------------------+-----------------+----------------------------|
| Code Complete | Steve McConnell | Code quality and design |
| --- | --- | --- |
|--------------------------------------+-----------------+----------------------------|
| Working Effectively with Legacy Code | Michael Feathers | Refactoring and testing |
| --- | --- | --- |
|--------------------------------------+-----------------+----------------------------|
| A Philosophy of Software Design | John Ousterhout | Complexity management |
| --- | --- | --- |

# Related Documents

- [Engineering Fundamentals Handbook](../../handbooks/engineering/README/)
- [Code Organization Guide](../../guides/engineering/code-organization/)
- [Testing Strategies Guide](../../guides/engineering/testing-strategies/)
- [Error Handling Guide](../../guides/engineering/error-handling/)
- [Logging Guide](../../guides/engineering/logging/)
- [Engineering Glossary](../../glossary/engineering/README/)
