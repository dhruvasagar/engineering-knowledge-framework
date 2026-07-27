+++
title = "AI-Assisted Architecture Review Playbook"
description = "Workflow for architecture review with AI assistance"
+++


# Objective

Leverage AI to accelerate architecture reviews by analysing trade-offs,
checking consistency against principles and generating review materials.
Human architects retain final authority on all decisions.

# Inputs

- Architecture proposal, RFC or ADR draft.
- System context (diagrams, data flow, existing architecture docs).
- Relevant architectural patterns and principles.

# Prerequisites

- The proposal is documented in the standard format (see [RFC template](../..*templates*rfc*README*) or [ADR template](../..*templates*adr*README*)).
- Review team is identified.
- AI assistant has access to the [Architecture Handbook](../..*handbooks*architecture*README*) and relevant [pattern guides](../..*guides*architecture*architectural-patterns*).

# Workflow

## Step 1: Context Preparation

1. Gather the architecture proposal and supporting documents.
2. Collect relevant patterns, principles and quality attribute scenarios.
3. Build an AI context pack with the architecture handbook and relevant guides.

## Step 2: AI Pre-Review

Ask the AI to analyse:

- Pattern fit: Does the proposed pattern match the problem context?
- Quality attributes: How does the proposal address performance, scalability,
  maintainability, security?
- Consistency: Does it follow established architectural principles?
- Trade-off identification: What trade-offs are implicit or unstated?
- Completeness: Are there gaps in the proposal?

Use the prompt patterns from [AI Workflows for Architecture](../..*prompts*architecture-ai-workflows*).

## Step 3: Human Review

1. Review the architecture proposal independently.
2. Evaluate the AI's findings critically.
3. Assess what the AI cannot evaluate:
   - Organisational context and team capability.
   - Long-term strategic alignment.
   - Political and cultural fit.
   - Implementation feasibility with existing systems.

## Step 4: Reconcile

1. Combine AI and human findings into a consolidated review.
2. Identify action items for the proposal author.
3. Document unresolved trade-offs for decision-makers.

## Step 5: Decision and Documentation

1. Record the review outcome (approved, changes required, rejected).
2. Update the proposal or ADR with review feedback.
3. Archive the review for future reference.

# Checklist

- [ ] AI pre-review completed.
- [ ] Quality attribute analysis performed.
- [ ] Pattern consistency checked.
- [ ] Trade-offs identified and documented.
- [ ] Human review completed.
- [ ] Findings reconciled and prioritised.
- [ ] Review outcome documented.

# Escalation Points

- Major trade-offs without clear resolution: escalate to architecture board.
- AI identifies a conflicting pattern: investigate and document rationale.
- Proposal changes scope significantly during review: request revision.

# Expected Outputs

- Consolidated architecture review report.
- Action items for the proposal author.
- Updated ADR or RFC with review feedback.
- Documented trade-offs and decision rationale.

# Related Documents

- [Architecture Review Playbook](..*..*playbooks*architecture-review*README*)
- [AI Workflows for Architecture](../..*prompts*architecture-ai-workflows*)
- [Architectural Patterns](..*..*guides*architecture*architectural-patterns*)
- [Architecture Handbook](../..*handbooks*architecture*README*)
