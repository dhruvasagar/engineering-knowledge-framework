---
title: "ADR Writing Guide"
description: "An Architecture Decision Record (ADR) is a short document that captures a significant architectural decision, its context, alternatives considered and consequences."
type: guide
capability: architecture
status: published
tags: [adr, writing]
last_reviewed: 2026-07-28
---

# Purpose

An Architecture Decision Record (ADR) is a short document that captures
a significant architectural decision, its context, alternatives
considered and consequences.

ADRs exist to answer a single question for future engineers:

> Why is the system the way it is?

This guide explains when to write an ADR, how to structure one
effectively, and what makes an ADR useful over time.

# Background

Architectural decisions are the most expensive decisions in a software
system. They shape what can be built, how it can be changed, and what
it costs to operate.

Without documentation, architectural decisions become invisible.
Future engineers inherit the consequences without understanding the
reasoning. They repeat mistakes, reverse sound decisions, and waste
time reconstructing context that was once well understood.

ADRs transform invisible decisions into a durable record of
architectural reasoning.

# When to Write an ADR

Write an ADR when a decision:

- Is significant and costly to reverse.
- Affects multiple teams or systems.
- Involves meaningful trade-offs.
- Sets a precedent for future decisions.
- Introduces a new pattern, technology or architectural approach.
- Responds to a significant change in context.

Do not write an ADR for:

- Routine implementation choices.
- Decisions that are easily reversible.
- Choices with no meaningful trade-offs.
- Personal preferences or style decisions.

A good heuristic: if you would benefit from explaining the decision to
a future engineer, write an ADR.

# ADR Lifecycle

An ADR progresses through these states:

| State      | Meaning                                       |
|------------|-----------------------------------------------|
| Proposed   | The decision is under discussion.             |
| Accepted   | The decision has been agreed and implemented. |
| Deprecated | The decision is no longer relevant.           |
| Superseded | A newer ADR has replaced this decision.       |

ADRs are never deleted. A deprecated or superseded ADR remains as a
historical record of why the system evolved the way it did.

# Writing an ADR

## Title

Use a clear, descriptive title that summarizes the decision.

Good:

- ADR-0012: Adopt Event-Driven Architecture for Order Processing
- ADR-0015: Use Postgres for Event Store

Avoid:

- ADR-0012: Database Decision
- ADR-0015: Architecture Change

## Context

The context section provides the background necessary to understand why
the decision was made.

Include:

- The problem or opportunity being addressed.
- Relevant constraints (time, budget, technology, team).
- Current architecture context.
- Forces influencing the decision.

Write the context so that someone joining the team in two years can
understand the situation without prior knowledge.

## Decision

State the decision clearly and explicitly.

Avoid vague language.

Good:

> We will use Apache Kafka for asynchronous communication between the
> Order Service and the Inventory Service.

Avoid:

> We decided to look into using some kind of message queue.

## Consequences

Describe the trade-offs, implications and results of the decision.

Include both positive and negative consequences.

Positive consequences answer:

- What becomes easier?
- What improves?
- What new capabilities does this enable?

Negative consequences answer:

- What becomes harder?
- What risks are introduced?
- What complexity is added?
- What previous capabilities are lost?

Be honest about negative consequences. A decision that acknowledges its
downsides is more credible than one that only lists benefits.

## Alternatives Considered

Every significant decision involves choice.

Listing alternatives demonstrates that the decision was deliberate.

For each alternative:

- Describe the approach briefly.
- Explain why it was not chosen.
- Reference the evaluation criteria.

This section is particularly valuable for future engineers who may
wonder why a seemingly obvious alternative was not selected.

# Characteristics of Good ADRs

## Focused

An ADR should capture one decision. If a document captures multiple
decisions, split it into multiple ADRs.

## Timely

Write the ADR when the decision is made, not months later. The context
fades quickly.

## Explicit about Trade-offs

The most valuable ADRs are those that honestly describe what was
sacrificed.

No architectural decision is without trade-offs. Pretending otherwise
undermines trust in the ADR.

## Self-Contained

An ADR should be understandable without reading other documents.

Include enough context that someone encountering the ADR in isolation
can understand the decision.

## Linked

Reference related ADRs, design documents, and discussion threads.

Build a connected graph of architectural decisions.

# Common Mistakes

## Too Much Detail

An ADR is not a design document. It should capture the decision and
reasoning, not the implementation details.

Keep it to one or two pages. If it is longer, split it or include
details in referenced documents.

## No Context

An ADR that states the decision without explaining why is useless to
future engineers.

The context is often more valuable than the decision itself.

## No Alternatives

An ADR that does not list alternatives suggests that no alternatives
were considered. This undermines confidence in the decision.

Even when alternatives are clearly inferior, listing them and explaining
why they were rejected demonstrates thoroughness.

## Hiding Negative Consequences

A decision that appears to have only positive consequences is hiding
trade-offs.

Every architectural decision involves sacrifice. Document it.

# AI Integration

AI assistants can help with ADRs by:

- Drafting the initial ADR from a discussion or notes.
- Identifying alternatives that may not have been considered.
- Suggesting consequences based on similar decisions.
- Reviewing ADRs for completeness and clarity.
- Linking related ADRs and decisions.

When asking AI to draft an ADR, provide:

- The decision to be made.
- The context and constraints.
- Any alternatives already identified.
- The preferred approach and initial reasoning.

# References

- [ADR Template](../../templates/adr/README.md)
- [ADR-0001: Capability Model for Knowledge Organization](../../adr/0001-capability-model.md)
- [ADR-0003: Document Taxonomy with Single Responsibility](../../adr/0003-document-taxonomy.md)
- [Software Architecture Handbook](../../handbooks/architecture/README.md)
- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
