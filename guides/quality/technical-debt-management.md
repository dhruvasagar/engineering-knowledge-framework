---
title: "Technical Debt Management"
description: "Technical debt is the gap between the current state of a codebase and the desired state."
type: guide
capability: quality
status: published
tags: [technical, debt, management]
last_reviewed: 2026-07-28
---

# Purpose

Technical debt is the gap between the current state of a codebase and
the desired state.

Some debt is intentional — taken to achieve a business outcome with a
plan to repay. Some debt is accidental — accumulated through neglect,
inadequate design or insufficient testing.

This guide defines a systematic approach to managing both.

# Classification

## Strategic Debt

Debt taken intentionally to meet a deadline or deliver a feature.

Characteristics:

- The team knows the debt exists.
- The decision to incur the debt is deliberate.
- There is a plan to repay it.
- The debt is tracked and visible.

Examples:

- Shipping a feature without tests to meet a release date.
- Using a simpler but less scalable design for an MVP.
- Delaying a refactoring to avoid blocking dependent work.

## Accidental Debt

Debt accumulated through oversight, inadequate practices or neglect.

Characteristics:

- The team may not be aware of the debt.
- There was no deliberate decision to incur it.
- There is no plan to repay it.
- The debt grows silently.

Examples:

- Code duplication introduced without awareness.
- Tests that become brittle and are never refactored.
- Dependencies that fall out of date.

# Assessment

## Severity Levels

| Severity | Description                                   | Response Time   |
|----------|-----------------------------------------------|-----------------|
| Critical | Blocks delivery, causes production incidents, | Immediate       |
|          | or introduces security vulnerabilities.       |                 |
| High     | Significantly slows development, causes       | Within 1 sprint |
|          | frequent bugs, or makes the codebase hard to  |                 |
|          | change.                                       |                 |
| Medium   | Moderate impact on development speed or       | Schedule within |
|          | code quality.                                 | the quarter.    |
| Low      | Minor inconvenience or cosmetic issue.        | Opportunistic.  |

## Assessment Criteria

For each area of the codebase, evaluate:

- How often does this area cause defects?
- How long does it take to make changes in this area?
- How confident are we that changes will not break existing behaviour?
- How difficult is it for new team members to understand this code?

# Management Process

## Step 1: Identify

Use multiple sources to identify debt:

- Automated tools (SonarQube, CodeClimate, RuboCop TODOs).
- Code review comments.
- Incident post-mortems.
- Team discussion and retrospectives.

## Step 2: Classify and Prioritise

For each item:

1. Classify as strategic or accidental.
2. Assign a severity level.
3. Estimate the effort to remediate.
4. Estimate the business value of remediation.

Prioritise using effort vs value: high-value, low-effort items first.

## Step 3: Track

Record each debt item with:

- Description and location.
- Classification (strategic or accidental).
- Severity.
- Estimated effort.
- Business impact.
- Owner.
- Review date.

## Step 4: Remediate

- Schedule debt repayment alongside feature work.
- Dedicate a regular percentage of capacity (e.g., 20%) to debt
  reduction.
- Fix debt incrementally. Avoid rewrites.

## Step 5: Prevent

- Improve code review to catch debt early.
- Automate quality checks in CI.
- Address root causes of accidental debt.

# Tracking Approaches

## Debt Log

Maintain a simple log of known technical debt:

```text
| ID | Area      | Description          | Severity | Effort | Status  |
|----|-----------|----------------------|----------|--------|---------|
| 1  | Auth      | Duplicate auth logic | High     | 2 days | Tracked |
|    |           | across controllers   |          |        |         |
| 2  | Reporting | Reports take > 30s   | Critical | 1 week | Planned |
|    |           | to generate          |          |        |         |
```

## Percentage-Based Allocation

Reserve a fixed percentage of each sprint for debt reduction:

- 20% for active projects.
- 10% for maintenance mode projects.

This ensures debt is addressed consistently without needing special
approval.

# Related Documents

- [Engineering Quality Handbook](../../handbooks/quality/README.md)
- [Tech Debt Assessment Checklist](../../checklists/tech-debt-assessment.md)
- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
- [Code Review Playbook](../../playbooks/code-review/README.md)
