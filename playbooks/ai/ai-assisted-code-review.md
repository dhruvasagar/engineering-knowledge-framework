---
title: "AI-Assisted Code Review Playbook"
description: "Workflow for reviewing code with AI assistance"
---


# Objective

Perform thorough code reviews by combining AI analysis with human
engineering judgement. AI accelerates routine checks and surfaces
potential issues, while humans evaluate design, trade-offs and context.

# Inputs

- Pull request or patch to review.
- Relevant engineering standards and style guides.
- Context from the codebase (directory structure, key modules).

# Prerequisites

- Access to an AI coding assistant configured with the project context.
- Familiarity with the [Context Engineering guide](../../guides/ai/context-engineering/).
- Understanding of the [standard code review process](../../playbooks/code-review/README/).

# Workflow

## Step 1: Prepare Context

1. Collect relevant context files:
   - The diff or PR description.
   - Related architecture documents or ADRs.
   - Relevant style guides or standards.
2. Build an AI context pack following the [Context Engineering guide](../../guides/ai/context-engineering/).

## Step 2: AI Pre-Review

Ask the AI to perform an initial review covering:

- Correctness: Does the code do what it intends?
- Consistency: Does it follow project conventions?
- Security: Are there obvious vulnerabilities?
- Testing: Is there appropriate test coverage?
- Performance: Are there obvious performance concerns?

Use the prompt patterns from [AI Workflows for Engineering](../../prompts/engineering-ai-workflows/).

## Step 3: Human Review

1. Read through the code independently.
2. Compare your findings with the AI pre-review.
3. Focus on aspects AI handles poorly:
   - Design decisions and trade-offs.
   - Business logic correctness.
   - Future maintainability.
   - Team conventions not captured in documentation.

## Step 4: Reconcile

1. Merge your findings with AI findings.
2. Discard false positives from the AI review.
3. Add context and rationale the AI may have missed.
4. Assign severity levels following [Code Review Standards](../../guides/quality/code-review-standards/).

## Step 5: Provide Feedback

1. Write clear, actionable review comments.
2. Reference specific lines and standards.
3. Explain why changes are needed (not just what).
4. Use the AI to draft feedback for your review.

# Checklist

- [ ] AI pre-review completed.
- [ ] Human review completed.
- [ ] Findings reconciled.
- [ ] False positives identified and discarded.
- [ ] Feedback provided with rationale.
- [ ] Severity labels applied.
- [ ] Critical issues resolved before merge.

# Escalation Points

- Disagreement between AI and human judgement: human judgement wins.
- AI identifies a potential security issue: escalate to security review.
- AI misses a clear design problem: update context and retry.

# Expected Outputs

- Review comments on the PR.
- Documented findings with severity labels.
- Updated context or prompts for future reviews.

# Related Documents

- [Code Review Playbook](../../playbooks/code-review/README/)
- [Context Engineering](../../guides/ai/context-engineering/)
- [AI Workflows for Engineering](../../prompts/engineering-ai-workflows/)
- [AI Usage Checklist](../../checklists/ai-usage/)
