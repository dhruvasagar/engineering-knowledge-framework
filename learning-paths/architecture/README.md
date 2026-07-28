# Purpose

These learning paths provide a structured progression through software
architecture, from understanding architectural concepts to leading
architectural decisions across an organization.

Architecture is the set of decisions that are costly to change.
These paths develop the judgement needed to make sound architectural
decisions and communicate them effectively.

# Beginner Path

## Objective

Understand architectural concepts, read and contribute to architecture
documentation, and participate in architecture reviews.

## Prerequisites

- Some experience building and deploying software.
- Familiarity with basic engineering principles.

## Topics

1. ***What is Architecture?***
   - Architecture as significant decisions.
   - Quality attributes and trade-offs.
   - Reference: [Software Architecture Handbook](../../handbooks/architecture/README.md)

2. ***Reading C4 Diagrams***
   - System context and container diagrams.
   - Understanding architectural boundaries.
   - Exercise: Read and explain a C4 diagram for an existing system.
   - Reference: [System Modeling Guide](../../guides/architecture/system-modeling.md)

3. ***Architecture Decision Records***
   - Why ADRs matter.
   - Reading and understanding existing ADRs.
   - Exercise: Read three ADRs and summarize the decisions.
   - Reference: [ADR Writing Guide](../../guides/architecture/adr-writing-guide.md)

4. ***Layered Architecture***
   - Structure and responsibilities of each layer.
   - When layered architecture works and when it does not.
   - Exercise: Identify the layers in an existing application.
   - Reference: [Architectural Patterns Guide](../../guides/architecture/architectural-patterns.md)

5. ***Participating in Architecture Reviews***
   - What to look for as a reviewer.
   - Asking good questions about trade-offs.
   - Exercise: Attend an architecture review and provide feedback.
   - Reference: [Architecture Review Playbook](../../playbooks/architecture-review/README.md)

## Suggested Projects

- Document the system context and container diagrams for a service you
  work on.
- Write your first ADR for a recent design decision.
- Review an ADR written by a peer.

## Assessment

Demonstrate by: Reading and understanding architecture diagrams and
ADRs. Contributing meaningful observations during an architecture
review.

# Intermediate Path

## Objective

Make architectural decisions independently, document them effectively,
and lead architecture reviews for team-level changes.

## Prerequisites

- Completed Beginner Path or equivalent experience.
- Experience participating in architecture discussions.

## Topics

1. ***Architectural Patterns***
   - Hexagonal, event-driven and microservices patterns.
   - Pattern trade-offs and selection criteria.
   - Exercise: Evaluate which architectural pattern suits a given
     problem context.
   - Reference: [Architectural Patterns Guide](../../guides/architecture/architectural-patterns.md)

2. ***Writing Effective ADRs***
   - Structuring context, decision and consequences.
   - Documenting alternatives and trade-offs.
   - Exercise: Write an ADR for a proposed architecture change and
     seek review.
   - Reference: [ADR Writing Guide](../../guides/architecture/adr-writing-guide.md)

3. ***API Design***
   - RESTful API conventions.
   - Versioning and evolvability.
   - Exercise: Design an API for a new service and review it with a
     peer.
   - Reference: [API Design Guide](../../guides/architecture/api-design.md)

4. ***Quality Attribute Trade-offs***
   - Performance vs evolvability.
   - Consistency vs availability.
   - Exercise: Create a trade-off matrix for a proposed architecture
     change.
   - Reference: [Software Architecture Handbook](../../handbooks/architecture/README.md)

5. ***Leading Architecture Reviews***
   - Setting scope and assembling the review team.
   - Facilitating productive discussions.
   - Exercise: Lead an architecture review for a team-level decision.
   - Reference: [Architecture Review Playbook](../../playbooks/architecture-review/README.md)

## Suggested Projects

- Propose and document an architectural improvement for a service.
- Design an API for a new feature following API design standards.
- Lead the architecture review for a medium-complexity change.

## Assessment

Demonstrate by: Independently producing well-structured ADRs. Leading
architecture reviews that result in clear decisions. Making sound
architectural trade-off decisions.

# Advanced Path

## Objective

Shape architectural strategy across teams, establish architectural
standards, and mentor other architects.

## Prerequisites

- Completed Intermediate Path or equivalent experience.
- Experience making architectural decisions that affect multiple teams.

## Topics

1. ***Event-Driven Architecture and Event Modeling***
   - Designing bounded contexts and aggregates.
   - Event modeling workshops.
   - Exercise: Facilitate an event modeling session for a new domain.
   - Reference: [System Modeling Guide](../../guides/architecture/system-modeling.md)

2. ***Architectural Strategy***
   - Defining architectural principles and standards for an
     organization.
   - Balancing consistency with team autonomy.
   - Exercise: Draft an architectural standard for a cross-cutting
     concern.
   - Reference: [Software Architecture Handbook](../../handbooks/architecture/README.md)

3. ***Cross-Capability Architecture***
   - How architecture intersects with security, testing and operations.
   - Architectural implications of organizational structure (Conway's
     Law).
   - Exercise: Analyse how team boundaries affect system architecture
     and propose improvements.

4. ***Mentoring Architects***
   - Reviewing ADRs for architectural reasoning, not just correctness.
   - Developing architectural judgement in others.
   - Exercise: Mentor a engineer through their first significant
     architectural decision.

5. ***AI-Assisted Architecture***
   - Using AI for trade-off analysis and pattern recommendation.
   - Maintaining human judgement in AI-assisted architecture.
   - Exercise: Use AI to evaluate an architectural decision and
     critically assess its recommendations.
   - Reference: AI Workflows for Architecture

## Suggested Projects

- Establish an ADR practice across multiple teams.
- Define an architectural standard that spans engineering,
  security and operations.
- Lead a significant cross-team architectural initiative.

## Assessment

Demonstrate by: Influencing architectural practices beyond your team.
Mentoring others in architectural thinking. Contributing architectural
standards to the framework.

# Related Documents

- [Software Architecture Handbook](../../handbooks/architecture/README.md)
- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
- [ADR Writing Guide](../../guides/architecture/adr-writing-guide.md)
- [Architectural Patterns Guide](../../guides/architecture/architectural-patterns.md)
- [API Design Guide](../../guides/architecture/api-design.md)
- [System Modeling Guide](../../guides/architecture/system-modeling.md)
- [Architecture Review Playbook](../../playbooks/architecture-review/README.md)
