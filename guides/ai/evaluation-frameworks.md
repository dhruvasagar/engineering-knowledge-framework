+++
title = "AI Evaluation Frameworks"
description = "Frameworks for measuring AI output quality and reliability"
+++


# Purpose

AI evaluation frameworks provide systematic methods for assessing the
quality, correctness and reliability of AI-generated output. Consistent
evaluation enables teams to measure improvement, identify failure modes
and build trust in AI-assisted workflows.

# Principles

## Evaluate Output, Not Process

Judge AI by what it produces, not how it produces it. The quality of
the output is what matters for engineering work.

## Evaluate in Context

AI output that is correct in one context may be wrong in another.
Always evaluate against specific requirements, constraints and
standards.

## Measure What Matters

Different tasks need different evaluation criteria. Code generation
needs correctness and security; documentation needs accuracy and
clarity; design needs trade-off awareness.

## Bias Toward Objective Criteria

Prefer verifiable criteria (does the code compile? do tests pass?)
over subjective criteria (does this look right?). Use subjective
assessment only when objective measures are unavailable.

# Evaluation Dimensions

| Dimension | What It Measures | How to Test |
| --- | --- | --- |
+----------------+-----------------------------------------------+-------------------------------------+
| Correctness | Is the output technically accurate? | Tests, compilation, manual review. |
| --- | --- | --- |
| Completeness | Does it address all requirements? | Checklist against requirements. |
| Consistency | Does it follow conventions and standards? | Linting, style checks, review. |
| Security | Does it introduce vulnerabilities? | Security scan, manual review. |
| Performance | Is it efficient and scalable? | Benchmarks, profiling. |
| Maintainability | Is it easy to understand and change? | Code review, complexity metrics. |
| Safety | Does it avoid harmful or misleading output? | Safety checklist, edge case testing. |

# Evaluation Methods

## Method 1: Automated Verification

Run automated checks against AI-generated output.

```
Checklist:
[x] Code compiles without errors.
[x] All existing tests pass.
[x] Linting passes with no new violations.
[x] Security scan shows no critical or high findings.
[x] Test coverage meets the project threshold.
```

| Strength | Weakness |
| --- | --- |
+--------------------------------+-----------------------------------+
| Fast, objective, repeatable. | Catches only ~30% of issues. |
| --- | --- |
| Can be run in CI. | Misses semantic correctness. |

## Method 2: Structured Human Review

A human reviewer evaluates AI output against defined criteria.

```
Criteria:
[ ] Correctness: Is the logic correct?
[ ] Completeness: Are all requirements addressed?
[ ] Consistency: Does it match project conventions?
[ ] Security: Are there vulnerabilities?
[ ] Maintainability: Is it well-structured?

Rating per criterion: Pass / Minor Issue / Major Issue / Fail
```

| Strength | Weakness |
| --- | --- |
+--------------------------------+-----------------------------------+
| Catches nuanced issues. | Subjective, time-consuming. |
| --- | --- |
| Can evaluate correctness. | Requires domain expertise. |

## Method 3: Comparative Evaluation

Compare AI output against a baseline or alternative.

```
Approach:
1. Generate output from two different prompts or models.
2. Compare both against requirements.
3. Identify where they agree (likely correct).
4. Investigate where they differ (needs human judgment).
```

| Strength | Weakness |
| --- | --- |
+--------------------------------+-----------------------------------+
| Reduces blind spots. | Doubles evaluation time. |
| --- | --- |
| Highlights uncertainty areas. | Agreement does not guarantee |
|  | correctness. |

## Method 4: Longitudinal Tracking

Track AI output quality over time to measure improvement.

```
Metrics to track per task type:
- Pass rate on first attempt.
- Number of issues found per review.
- Time spent reviewing and correcting.
- Severity distribution of issues.

Track per model, prompt template and task type.
```

| Strength | Weakness |
| --- | --- |
+--------------------------------+-----------------------------------+
| Identifies trends and regressions. | Requires consistent measurement. |
| --- | --- |
| Informs prompt improvements. | Needs data collection over time. |

# Task-Specific Evaluation Criteria

## Code Generation

| Criterion | How to Evaluate |
| --- | --- |
+--------------------+--------------------------------------------+
| Compilation | Does it compile without errors? |
| --- | --- |
| Test passage | Do existing and generated tests pass? |
| Correctness | Does it implement the specified behaviour? |
| Edge cases | Are error paths and boundary conditions |
|  | handled? |
| Security | Are inputs validated, outputs encoded? |
| Style | Does it match project conventions? |
| Performance | Are there obvious inefficiencies? |

## Documentation

| Criterion | How to Evaluate |
| --- | --- |
+--------------------+--------------------------------------------+
| Accuracy | Are facts correct and verifiable? |
| --- | --- |
| Completeness | Does it cover all required topics? |
| Clarity | Is it understandable without prior |
|  | context? |
| Structure | Is it well-organised with clear headings? |
| Examples | Are examples correct and relevant? |
| Cross-references | Are related documents linked? |

## Architecture / Design

| Criterion | How to Evaluate |
| --- | --- |
+--------------------+--------------------------------------------+
| Trade-off awareness | Are trade-offs explicitly discussed? |
| --- | --- |
| Constraint fit | Does it respect stated constraints? |
| Consistency | Does it align with existing patterns? |
| Completeness | Are all quality attributes addressed? |
| Feasibility | Is the design implementable? |
| Clarity | Is the design easy to understand? |

## Test Generation

| Criterion | How to Evaluate |
| --- | --- |
+--------------------+--------------------------------------------+
| Correctness | Do tests accurately test the intended |
| --- | --- |
|  | behaviour? |
| Coverage | Do they cover key paths and edge cases? |
| Independence | Are tests independent and deterministic? |
| Readability | Are test names and assertions clear? |
| Maintainability | Are tests resilient to refactoring? |

# Scoring Rubric

| Score | Label | Description |
| --- | --- | --- |
+-------+--------------+-------------------------------------------+
| 5 | Excellent | Production-ready with minor or no changes. |
| --- | --- | --- |
| 4 | Good | Usable after moderate revision. |
| 3 | Acceptable | Requires significant revision. |
| 2 | Poor | Major issues, needs substantial rework. |
| 1 | Unusable | Cannot be used — start over. |

# Evaluation Workflow

1. ***Define criteria*** before generating output.
2. ***Generate output*** using best prompt practices.
3. ***Run automated checks*** (compile, lint, test, security).
4. ***Perform structured review*** against criteria.
5. ***Score each dimension*** using the rubric.
6. ***Document findings*** — what worked, what did not.
7. ***Feed back*** into prompt and context improvements.

# Anti-patterns

- ***Evaluating without criteria***: Review without defined standards
  leads to inconsistent assessment.
- ***Confirmation bias***: Favouring AI output that matches your
  preconceptions.
- ***Ignoring false positives***: Flagging correct output as incorrect
  wastes time and reduces trust.
- ***Single-dimension evaluation***: Judging AI output on correctness
  alone misses security, performance and maintainability issues.
- ***Not tracking over time***: Without longitudinal data, it is
  impossible to know if AI output is improving or degrading.

# Related Documents

- [Human Review Strategies](./human-review-strategies/)
- [Verification Workflows](../../playbooks/ai/verification-workflows/)
- [AI Usage Checklist](../../checklists/ai-usage/)
- [AI Safety and Verification](../ai/ai-safety/)
- [AI References](../../references/ai/README/)
