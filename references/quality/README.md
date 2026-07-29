---
title: "Engineering Quality References"
description: "Quick-reference material for engineering quality."
type: reference
capability: quality
status: published
last_reviewed: 2026-07-28
---

# Purpose

Quick-reference material for engineering quality.

# Quality Gates

| Gate         | Checks                                                    |
|--------------|-----------------------------------------------------------|
| Pre-commit   | Linting passes, unit tests pass, no secrets committed.    |
| Pull Request | CI passes, coverage meets threshold, no new violations,   |
|              | dependency scan passes, code review approved.             |
| Deploy       | PR gates passed, integration tests pass, migration        |
|              | reviewed, rollback plan documented.                       |
| Release      | Full test suite passes, benchmarks within range, security |
|              | audit completed, changelog updated.                       |

# Quality Metrics

| Metric                | Target           | Tools                            |
|-----------------------|------------------|----------------------------------|
| Cyclomatic complexity | <= 10 per method | RuboCop, Flog, ESLint            |
| Code duplication      | < 5%             | Flay, PMD, ESLint                |
| Code coverage         | >= 90%           | SimpleCov, Istanbul, JaCoCo      |
| Style violations      | 0 in new code    | RuboCop, ESLint, StandardRB      |
| Defect escape rate    | < 5%             | Incident tracking, test analysis |
| Change failure rate   | < 5%             | Deployment tracking, monitoring  |
| MTTR                  | < 1 hour         | Incident management, monitoring  |
| Deployment frequency  | Daily or more    | CI/CD pipeline, deployment       |
|                       |                  | tracking                         |

# Code Review Severity Labels

| Label        | Meaning                                              |
|--------------|------------------------------------------------------|
| BLOCKER      | Must be fixed before merge. Design flaw, correctness |
|              | issue, security vulnerability.                       |
| SHOULD FIX   | Important but not blocking. Follow-up required.      |
| NICE TO HAVE | Suggestion for improvement. Can be deferred.         |
| QUESTION     | Clarification needed. Not a change request.          |

# Technical Debt Classification

| Category   | Characteristics                  | Approach                      |
|------------|----------------------------------|-------------------------------|
| Strategic  | Intentional, with plan to repay. | Track, schedule, communicate. |
| Accidental | Accumulated through neglect.     | Assess, prioritise, reduce    |
|            |                                  | incrementally.                |

# Defect Cost Escalation

| Phase       | Relative Cost |
|-------------|---------------|
| Design      | 1x            |
| Development | 5x            |
| Testing     | 10x           |
| Production  | 50x+          |

# Recommended Reading

| Title      | Author            | Focus                  |
|------------|-------------------|------------------------|
| Accelerate | Forsgren, Humble, | DORA metrics, DevOps   |
|            | Kim               |                        |
| Clean Code | Robert C. Martin  | Code quality, naming,  |
|            |                   | functions.             |
| The Goal   | Eliyahu Goldratt  | Theory of constraints, |
|            |                   | process improvement.   |

# Related Documents

- [Engineering Quality Handbook](../../handbooks/quality/README.md)
- [Engineering Quality Glossary](../../glossary/quality/README.md)
- [Code Review Standards Guide](../../guides/quality/code-review-standards.md)
- [Quality Metrics Guide](../../guides/quality/quality-metrics.md)
