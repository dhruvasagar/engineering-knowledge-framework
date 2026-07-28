---
title: "Verification Workflows"
description: "Systematic verification of AI-generated output"
---


# Objective

Systematically verify AI-generated code, architecture and documentation
to ensure correctness, security and compliance with engineering
standards. Verification is the human quality gate that makes AI
assistance safe and reliable.

# Inputs

- AI-generated output (code, design, documentation, tests).
- Task requirements and success criteria.
- Relevant standards, style guides and conventions.
- Existing test suite and quality tooling.

# Prerequisites

- Familiarity with [AI Evaluation Frameworks](../../guides/ai/evaluation-frameworks/).
- Access to standard engineering tooling (compiler, linter, test runner,
  security scanner).
- Understanding of [Human Review Strategies](../../guides/ai/human-review-strategies/).

# Workflow

## Step 1: Classify the Output

Determine the type and risk level of the AI-generated output:

| Type | Risk Level | Examples |
| --- | --- | --- |
+----------------+------------+----------------------------------+
| Code | Variable | Feature implementation, bug fix. |
| --- | --- | --- |
| Architecture | High | System design, pattern selection. |
| Documentation | Low-Medium | README, API docs, comments. |
| Tests | Medium | Unit tests, integration tests. |
| Configuration | Medium | CI config, dependency changes. |
| Data / Content | Low | Migration data, seed data. |

## Step 2: Run Automated Verification

Always run automated checks first — they are fast and catch common
issues.

```
Automated verification gates:
[ ] Compilation / syntax check passes.
[ ] All existing tests pass.
[ ] Linting passes with no new violations.
[ ] Security scan shows no critical/high findings.
[ ] Dependency audit passes (if dependencies changed).
[ ] Test coverage meets project threshold.
```

## Step 3: Perform Structured Review

Use the appropriate review strategy from [Human Review Strategies](../../guides/ai/human-review-strategies/).

```
For code:
[ ] Read-through for logic errors.
[ ] Test edge cases (empty, nil, boundary, error).
[ ] Verify security (input validation, auth, injection).
[ ] Check style and convention adherence.
[ ] Verify test coverage for new code.

For architecture:
[ ] Verify trade-offs are documented.
[ ] Check constraint compliance.
[ ] Review consistency with existing patterns.
[ ] Assess feasibility and implementation effort.

For documentation:
[ ] Verify factual accuracy.
[ ] Check clarity and completeness.
[ ] Test examples for correctness.
[ ] Verify cross-references resolve.
```

## Step 4: Remediate Issues

For each issue found:

1. Classify by severity (Critical / High / Medium / Low / Suggestion).
2. Decide whether to fix manually or regenerate with improved prompt.
3. If regenerating, update the prompt with specific feedback.
4. If fixing manually, document the fix for future prompt improvement.

## Step 5: Final Approval

1. All critical and high issues must be resolved.
2. Medium issues should be resolved or explicitly accepted.
3. Run automated verification again after fixes.
4. Document the verification outcome.

# Verification Depth by Risk

| Risk Level | Automated Checks | Review Strategy | Review Time | Approval |
| --- | --- | --- | --- | --- |
+------------+------------------+-----------------+-------------+----------+
| Critical | Full suite | Decomposition | 30-60 min | Senior |
| --- | --- | --- | --- | --- |
|  |  | + Walkaway |  | engineer |
| High | Full suite | Test-Driven | 15-30 min | Any |
|  |  | + Read-Through |  | engineer |
| Medium | Standard suite | Read-Through | 5-15 min | Author |
| Low | Lint + compile | Spot-check | < 5 min | Author |

# Verification Checklist

- [ ] Output classified by type and risk level.
- [ ] Automated checks run and passed.
- [ ] Appropriate review strategy applied.
- [ ] All critical and high issues resolved.
- [ ] Medium issues resolved or accepted.
- [ ] Automated checks re-run after fixes.
- [ ] Verification outcome documented.
- [ ] Prompt or context improved based on findings.

# Escalation Points

- Repeated failure in the same area: improve prompt or context.
- AI output contradicts established engineering principles: escalate
  to senior engineer.
- Security vulnerability found: follow standard security response
  process.
- Verification consistently finds no issues: reduce review depth for
  low-risk outputs from the same workflow.

# Expected Outputs

- Verified AI output ready for integration.
- Documented verification findings and decisions.
- Improved prompts and context for future iterations.
- Metrics on verification outcomes (pass rate, issues found, time
  spent).

# Related Documents

- [AI Evaluation Frameworks](../../guides/ai/evaluation-frameworks/)
- [Human Review Strategies](../../guides/ai/human-review-strategies/)
- [Agentic Workflows](../../guides/ai/agentic-workflows/)
- [AI Usage Checklist](../../checklists/ai-usage/)
- [AI Safety and Verification](../../guides/ai/ai-safety/)
