# Purpose

Quality metrics provide objective data for evaluating and improving
engineering effectiveness.

This guide defines the metrics every team should track, how to measure
them and how to use them for continuous improvement.

# Principles

## Measure What Matters

Not everything that counts can be counted. Focus on metrics that
correlate with better outcomes: reliability, maintainability and
delivery speed.

## Use Metrics for Improvement, Not Judgement

Metrics should guide improvement, not evaluate individuals. When
metrics are used as targets, they lose their effectiveness (Goodhart's
Law).

## Track Trends, Not Absolute Values

A single measurement is noise. A trend over time is signal. Track
metrics consistently and look for patterns.

# Code Quality Metrics

## Cyclomatic Complexity

Measures the number of linearly independent paths through a method.

- Lower is better.
- Target: <= 10 per method.
- High complexity indicates hard-to-test, hard-to-maintain code.

Tools: RuboCop (Ruby), ESLint (JavaScript), Flog (Ruby).

## Code Duplication

Measures the percentage of duplicated code blocks.

- Target: < 5%.
- Duplication increases maintenance cost and bug risk.

Tools: Flay (Ruby), PMD Copy*Paste Detector (Java), ESLint (JS).

## Code Coverage

Measures the percentage of code exercised by the test suite.

- Target: >= 90%.
- Coverage is a lower bound, not a quality target. High coverage does
  not guarantee good tests.

Tools: SimpleCov (Ruby), Istanbul (JS), JaCoCo (Java).

## Style Violations

Measures deviations from the project's coding standards.

- Target: 0 in new code.
- Existing violations should be tracked and reduced over time.

Tools: RuboCop (Ruby), ESLint (JavaScript), StandardRB.

# Process Quality Metrics

## Deployment Frequency

How often the team deploys to production.

- Higher frequency correlates with higher engineering maturity.
- Target: Daily or more.

## Change Failure Rate

Percentage of deployments that cause a failure, incident or rollback.

- Target: < 5%.
- If the rate is high, focus on testing and review processes.

## Mean Time to Recover (MTTR)

Average time to restore service after an incident.

- Target: < 1 hour.
- Invest in monitoring, rollback automation and incident response.

## Defect Escape Rate

Percentage of defects found in production versus those found during
development.

- Target: < 5%.
- If the rate is high, strengthen testing and review processes.

# Implementing Metrics

## Step 1: Establish Baselines

Measure current values for each metric before setting targets. Without
a baseline, targets are arbitrary.

## Step 2: Set Targets

Set realistic improvement targets based on baselines and team
capacity. Aggressive targets without capacity create perverse
incentives.

## Step 3: Automate Collection

- Use CI*CD to collect metrics automatically.
- Display metrics on a dashboard visible to the team.
- Alert on significant regressions.

## Step 4: Review Regularly

- Review metrics in sprint retrospectives.
- Look for trends, not single data points.
- Adjust targets as the team improves.

# Common Pitfalls

## Gaming Metrics

When metrics become targets, they lose their effectiveness.

Example: If coverage targets are enforced rigidly, teams may write
trivial tests that exercise code without asserting anything meaningful.

## Ignoring Context

Metrics without context can mislead.

A low change failure rate may mean the team is not deploying risky
changes — or that they are not deploying at all.

## Analysis Paralysis

Collecting too many metrics creates noise.

Start with a small set of high-signal metrics and expand only when
needed.

# Related Documents

- [Engineering Quality Handbook](../../handbooks/quality/README.md)
- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
- [Rails Project Standards](../../guides/rails/project-standards.md)
- [Tech Debt Assessment Checklist](../../checklists/tech-debt-assessment.md)
