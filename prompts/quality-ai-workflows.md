---
title: "AI Workflows for Engineering Quality"
description: "Prompt patterns for AI-assisted quality engineering tasks"
---


# Purpose

This document provides prompt patterns for using AI to assist with
engineering quality tasks — quality review, technical debt analysis,
test coverage assessment and quality metrics tracking.

# Principles

- AI augments quality analysis but cannot replace engineering judgement.
- All AI-generated quality findings must be verified by a human.
- Quality metrics should be objective and reproducible.

# Workflows

## Code Quality Review

Use AI to review code quality before human review.

Context:

```
Review the following code for quality issues:

[paste code]

Focus on:
1. Complexity — is this more complex than it needs to be?
2. Duplication — is there repeated logic that could be extracted?
3. Readability — is the intent clear?
4. Maintainability — will this be easy to change?

For each issue, suggest a specific improvement.
```

## Technical Debt Identification

Use AI to identify potential technical debt in code.

Context:

```
Analyse this code for signs of technical debt:

[paste code]

Look for:
1. Workarounds or temporary solutions.
2. Missing error handling or edge cases.
3. Outdated patterns or deprecated APIs.
4. Missing tests or inadequate coverage.
5. Violations of project conventions.

Classify each finding as strategic or accidental debt.
```

## Test Coverage Analysis

Use AI to assess test quality and coverage gaps.

Context:

```
Review these test files for coverage quality:

[paste test code]

Evaluate:
1. Are edge cases tested (empty, nil, boundary conditions)?
2. Are error paths tested?
3. Are there integration tests for key workflows?
4. Are tests independent and deterministic?
5. Is there over-mocking (testing implementation, not behaviour)?

Suggest additional tests to fill gaps.
```

## Quality Metrics Review

Use AI to interpret quality metrics and suggest improvements.

Context:

```
Here are the current quality metrics for [project]:

[paste metrics]

Based on these metrics:
1. What are the most concerning trends?
2. What should be prioritised for improvement?
3. What is working well?
4. Are there metrics that need investigation?

Provide specific, actionable recommendations.
```

## Code Review Preparation

Use AI to prepare for a code review by highlighting areas of concern.

Context:

```
Prepare this code for review:

[paste diff or code]

Highlight:
1. Sections that need the most careful review.
2. Potential design issues or trade-offs.
3. Security considerations.
4. Performance implications.
5. Testing gaps.

Organise findings by severity: critical / major / minor / suggestion.
```

# Anti-patterns

- ***Metric fixation***: AI can analyse metrics but cannot interpret
  organisational context. Always combine data with judgement.
- ***False precision***: Quality metrics are indicators, not absolute
  measures. Use them to identify areas for investigation, not as
  pass/fail criteria.
- ***Automated gatekeeping***: Never let AI alone block or approve changes.
  Human review remains mandatory for quality gates.

# Related Documents

- [Engineering Quality Handbook](../handbooks/quality/README/)
- [Quality Metrics](../guides/quality/quality-metrics/)
- [Code Review Standards](../guides/quality/code-review-standards/)
- [Quality Review Playbook](../playbooks/quality/quality-review/)
- [AI Usage Checklist](../checklists/ai-usage/)
