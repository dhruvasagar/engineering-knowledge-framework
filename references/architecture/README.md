---
title: "Architecture References"
description: "Quick-reference material for software architecture."
type: reference
capability: architecture
status: published
last_reviewed: 2026-07-28
---

# Purpose

Quick-reference material for software architecture.

These references are intended for lookup rather than learning. For
in-depth explanations, see the referenced guides and handbooks.

# C4 Model Levels

| Level | View           | Audience       | Elements                        |
|-------|----------------|----------------|---------------------------------|
| 1     | System Context | Everyone       | Users, system, external systems |
| 2     | Container      | Technical team | Services, databases, queues     |
| 3     | Component      | Developers     | Modules, controllers, services  |
| 4     | Code           | Developers     | Classes, interfaces, functions  |

# Architectural Patterns Quick Comparison

| Pattern       | Coupling | Complexity | Scale        | Key Trade-off                |
|---------------|----------|------------|--------------|------------------------------|
| Layered       | Tight    | Low        | Small-Medium | Simplicity vs flexibility    |
| Hexagonal     | Loose    | Medium     | Medium       | Testability vs indirection   |
| Event-Driven  | Very     | High       | Medium-Large | Decoupling vs debuggability  |
|               | Loose    |            |              |                              |
| Microservices | Loose    | Very High  | Large        | Autonomy vs operational cost |
| CQRS          | Medium   | High       | Medium-Large | Optimization vs complexity   |

# HTTP Status Codes

| Code | Meaning           | When to Use                            |
|------|-------------------|----------------------------------------|
| 200  | OK                | Successful GET, PUT, PATCH.            |
| 201  | Created           | Successful POST.                       |
| 204  | No Content        | Successful DELETE.                     |
| 400  | Bad Request       | Malformed request, validation failure. |
| 401  | Unauthorized      | Missing or invalid authentication.     |
| 403  | Forbidden         | Not authorized.                        |
| 404  | Not Found         | Resource does not exist.               |
| 409  | Conflict          | State conflict (duplicate, stale).     |
| 422  | Unprocessable     | Semantic validation failure.           |
| 429  | Too Many Requests | Rate limit exceeded.                   |
| 500  | Internal Error    | Unexpected server error.               |
| 503  | Unavailable       | Temporary service unavailability.      |

# Quality Attributes

| Attribute       | Definition                                      |
|-----------------|-------------------------------------------------|
| Performance     | Response time, throughput, latency.             |
| Scalability     | Ability to handle increased load.               |
| Availability    | Uptime, fault tolerance, recovery.              |
| Security        | Authentication, authorization, data protection. |
| Maintainability | Ease of change, testing, debugging.             |
| Evolvability    | Ability to adapt to new requirements.           |
| Operability     | Monitoring, deployment, incident response.      |
| Testability     | Ability to verify correctness at every level.   |

# ADR Lifecycle States

| State      | Meaning                                 |
|------------|-----------------------------------------|
| Proposed   | Decision under discussion.              |
| Accepted   | Decision agreed and implemented.        |
| Deprecated | Decision is no longer relevant.         |
| Superseded | A newer ADR has replaced this decision. |

# Key Metrics

| Concept                  | Question to Ask                                  |
|--------------------------|--------------------------------------------------|
| Coupling                 | Can this module change without affecting others? |
| Cohesion                 | Does this module have one clear responsibility?  |
| Technical Debt           | Is this intentional or accidental?               |
| Architectural Fit        | Does this decision align with our principles?    |
| Quality Attribute Impact | What trade-off does this decision introduce?     |

# Recommended Reading

| Title                                 | Author          | Focus                      |
|---------------------------------------|-----------------|----------------------------|
| Software Architecture: The Hard Parts | Ford, Richards, | Trade-off analysis         |
|                                       | Sadalage        |                            |
| Building Evolutionary Architectures   | Ford, Parsons   | Evolvability and fitness   |
|                                       |                 | functions                  |
| Domain-Driven Design                  | Eric Evans      | Domain modeling and DDD    |
| Fundamentals of Software Architecture | Richards, Ford  | Architecture fundamentals  |
| Documenting Software Architectures    | Clements et al. | Architecture documentation |

# Related Documents

- [Software Architecture Handbook](../../handbooks/architecture/README.md)
- [Architectural Patterns Guide](../../guides/architecture/architectural-patterns.md)
- [API Design Guide](../../guides/architecture/api-design.md)
- [ADR Writing Guide](../../guides/architecture/adr-writing-guide.md)
- [System Modeling Guide](../../guides/architecture/system-modeling.md)
- [Architecture Glossary](../../glossary/architecture/README.md)
