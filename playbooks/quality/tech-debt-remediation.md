---
title: "Technical Debt Remediation"
description: "Systematically identify, classify and reduce technical debt."
type: playbook
capability: quality
status: published
tags: [tech, debt, remediation]
last_reviewed: 2026-07-28
---

# Objective

Systematically identify, classify and reduce technical debt. This
playbook provides a repeatable process for technical debt management
that balances remediation with feature delivery.

# Inputs

- Technical debt assessment (see [Tech Debt Assessment Checklist](../../checklists/tech-debt-assessment.md)).
- Project roadmap and sprint commitments.
- Existing debt tracking (issue tracker, ADRs, team knowledge).

# Prerequisites

- Familiarity with [Technical Debt Management](../../guides/quality/technical-debt-management.md).
- Understanding of the debt classification system.
- Team agreement on remediation approach.

# Workflow

## Step 1: Inventory

1. Collect known technical debt items from:
   - [Tech Debt Assessment Checklist](../../checklists/tech-debt-assessment.md) results.
   - Issue tracker labels.
   - Team knowledge and retrospection.
   - Static analysis reports (complexity, duplication, coverage gaps).
2. Record each item with:
   - Description and location.
   - Type (strategic vs accidental).
   - Estimated remediation effort.
   - Impact on development velocity.

## Step 2: Classify

Classify each debt item using the framework in [Technical Debt Management](../../guides/quality/technical-debt-management.md):

| Type       | Description                    | Example                       |
|------------|--------------------------------|-------------------------------|
| Strategic  | Intentional shortcut for speed | Skipping tests for MVP        |
| Accidental | Unintended quality degradation | Growing cyclomatic complexity |
| Prudent    | Known and tracked              | Documented in ADR             |
| Reckless   | Unknown or ignored             | No tests, no documentation    |

## Step 3: Prioritise

1. Score each item by:
   - Impact on development velocity (1-5).
   - Risk of defects or incidents (1-5).
   - Remediation effort (story points or time estimate).
2. Plot on an impact-vs-effort matrix.
3. Identify quick wins (high impact, low effort) and strategic bets
   (high impact, high effort).

## Step 4: Plan Remediation

1. Allocate remediation capacity (e.g., 20% of each sprint).
2. Schedule quick wins in the next sprint.
3. Break large items into smaller, addressable chunks.
4. Document the remediation plan with owners and target dates.

## Step 5: Execute and Track

1. Remediate debt items during allocated capacity.
2. Verify fixes with tests and reviews.
3. Update the debt inventory after each sprint.
4. Track trends — is total debt decreasing or increasing?

# Debt Budget

| Category         | Target                                        |
|------------------|-----------------------------------------------|
| Critical debt    | Zero — remediate immediately.                 |
| Strategic debt   | Document and track with planned remediation.  |
| Accidental debt  | Investigate root cause to prevent recurrence. |
| Total debt ratio | Keep below 20% of codebase churn.             |

# Checklist

- [ ] Debt inventory created.
- [ ] Each item classified.
- [ ] Impact and effort scored.
- [ ] Prioritisation matrix completed.
- [ ] Remediation plan documented.
- [ ] Capacity allocated in sprint planning.
- [ ] Quick wins scheduled.
- [ ] Large items decomposed.
- [ ] Progress tracked.
- [ ] Root causes investigated for accidental debt.

# Escalation Points

- Critical debt blocking delivery: escalate to engineering manager.
- Accidental debt growing: investigate process gaps.
- Team consistently exceeding debt budget: revisit planning process.

# Expected Outputs

- Technical debt inventory with classified items.
- Prioritised remediation plan.
- Sprint allocation for debt work.
- Trend data for tracking progress.

# Related Documents

- [Technical Debt Management](../../guides/quality/technical-debt-management.md)
- [Tech Debt Assessment Checklist](../../checklists/tech-debt-assessment.md)
- [Quality References](../../references/quality/README.md)
