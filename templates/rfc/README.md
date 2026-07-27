+++
title = "RFC Template"
description = "Template for major architectural proposals (Request for Comments)"
+++


# RFC-NNNN: Title

:PROPERTIES:
:STATUS:   draft | review | accepted | rejected | implemented
:DATE:     YYYY-MM-DD
:END:

# Summary

A brief, one-paragraph summary of the proposal.

Write this for a busy engineer who needs to understand the essence of
the proposal in 30 seconds.

# Motivation

Why is this change needed?

Describe the problem or opportunity. Include concrete evidence where
possible (metrics, user feedback, incident reports, growth projections).

What happens if we do not make this change?

# Proposed Solution

Describe the proposed approach at a level of detail appropriate for
review.

Include:

- Architecture or system diagram (C4 level 2 or 3).
- Key design decisions and rationale.
- Interfaces, contracts or APIs affected.
- Data model changes, if any.
- Migration or transition approach.

# Alternatives Considered

For each alternative:

- ***Approach***: Brief description.
- ***Why Rejected***: Specific reasons, not generic statements.

At minimum, include the "do nothing" alternative.

## Alternative 1: Do Nothing

Describe the outcome of not making any change.

## Alternative 2: Title

Describe the approach and why it was not chosen.

# Impact and Trade-offs

## Positive Consequences

What improves? What becomes easier?

## Negative Consequences

What becomes harder? What risks are introduced?

## Quality Attribute Impact

| Attribute | Impact | Notes |
| --- | --- | --- |
|---------------+-------------+---------------------------------|
| Performance | Positive | Expected 20% reduction in p99 |
| --- | --- | --- |
|  | / Neutral | latency |
|  | / Negative |  |
| Scalability |  |  |
| Availability |  |  |
| Security |  |  |
| Maintainability |  |  |
| Evolvability |  |  |
| Operability |  |  |
| Testability |  |  |

# Migration Plan

If applicable, describe how to transition from the current state to the
proposed state.

- Can this be done incrementally?
- What is the rollback strategy?
- What is the expected timeline?
- What dependencies exist?

# Open Questions

List unresolved questions or decisions that need to be made during
review.

# References

- Links to related ADRs, design documents, discussions or research.
