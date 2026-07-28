# Purpose

Engineering quality is the discipline of ensuring that software meets
its intended purpose, is maintainable over time and can be delivered
reliably.

Quality is not a phase or a role. It is a property of the entire
engineering process that must be designed, measured and continuously
improved.

This handbook defines the principles, standards and practices for
engineering quality across all capabilities.

# Scope

This handbook covers:

- Quality principles and philosophy.
- Quality metrics and measurement.
- Code quality standards.
- Testing and verification.
- Technical debt management.
- Quality gates and CI/CD.
- Quality culture and practices.
- AI integration for quality.

# Principles

## Quality is a Shared Responsibility

Quality is not the responsibility of a QA team or a quality engineer.
Every engineer is responsible for the quality of what they build.

## Quality Must Be Measured

You cannot improve what you do not measure.

Define quality metrics, measure them consistently and track trends over
time. Use data to guide quality improvements, not to punish teams.

## Prevent Defects, Don't Just Find Them

Finding defects through testing is important. Preventing defects through
good design, code review and standards is more effective and less
expensive.

The cost of fixing a defect increases exponentially the later it is
found:

| Phase | Relative Cost |
| --- | --- |
+------------------+---------------+
| Design | 1x |
| --- | --- |
+------------------+---------------+
| Development | 5x |
| --- | --- |
+------------------+---------------+
| Testing | 10x |
| --- | --- |
+------------------+---------------+
| Production | 50x+ |
| --- | --- |
+------------------+---------------+

## Consistency Enables Quality

Consistent code, processes and standards reduce cognitive load and
make it easier to spot anomalies.

Inconsistency hides defects.

## Quality is About Trade-offs

Perfect quality is not achievable. Every quality investment must be
balanced against time, cost and business value.

The goal is to achieve a level of quality that is appropriate for the
system's purpose and risk profile.

# Quality Metrics

## Code Quality Metrics

| Metric | What It Measures | Target |
| --- | --- | --- |
+-----------------------+------------------------------------------+------------------+
| Cyclomatic complexity | How difficult code is to test and | <= 10 per method |
| --- | --- | --- |
|  | maintain. |  |
+-----------------------+------------------------------------------+------------------+
| Duplication | Amount of duplicated code. | < 5% |
| --- | --- | --- |
+-----------------------+------------------------------------------+------------------+
| Code coverage | Percentage of code exercised by tests. | >= 90% |
| --- | --- | --- |
+-----------------------+------------------------------------------+------------------+
| Style violations | Deviations from coding standards. | 0 in new code |
| --- | --- | --- |
+-----------------------+------------------------------------------+------------------+
| Technical debt ratio | Estimated effort to fix issues vs | < 5% |
| --- | --- | --- |
|  | cost to rebuild. |  |
+-----------------------+------------------------------------------+------------------+

## Process Quality Metrics

| Metric | What It Measures | Target |
| --- | --- | --- |
+-----------------------+------------------------------------------+------------------+
| Defect escape rate | Defects found in production vs testing. | < 5% |
| --- | --- | --- |
+-----------------------+------------------------------------------+------------------+
| Mean time to recover | How quickly the team can recover from | < 1 hour |
| --- | --- | --- |
|  | production incidents. |  |
+-----------------------+------------------------------------------+------------------+
| Deployment frequency | How often the team deploys to | Daily or more |
| --- | --- | --- |
|  | production. |  |
+-----------------------+------------------------------------------+------------------+
| Change failure rate | Percentage of deployments that cause | < 5% |
| --- | --- | --- |
|  | a failure. |  |
+-----------------------+------------------------------------------+------------------+

# Quality Gates

Quality gates are automated checks that must pass before a change
proceeds to the next stage.

## Pre-Commit Gate

Run before every commit:

- [ ] Linting passes (RuboCop, ESLint, etc.).
- [ ] Unit tests pass.
- [ ] No secrets committed.

## Pull Request Gate

Run on every pull request:

- [ ] All CI checks pass.
- [ ] Code coverage meets threshold.
- [ ] No new style violations.
- [ ] Dependency vulnerabilities checked.
- [ ] Security scan passes.
- [ ] Code review approved.

## Deployment Gate

Run before every deployment:

- [ ] All PR gates passed.
- [ ] Integration tests pass.
- [ ] Migration safety reviewed.
- [ ] Rollback plan documented.

## Release Gate

Run before every release:

- [ ] Full test suite passes.
- [ ] Performance benchmarks are within range.
- [ ] Security audit completed.
- [ ] Changelog updated.

# Code Review and Quality

Code review is the most effective quality practice.

## What to Review For

- ***Correctness***: Does the code do what it intends?
- ***Design***: Is the approach appropriate for the system?
- ***Maintainability***: Will the code be easy to change?
- ***Test quality***: Are the tests meaningful and sufficient?
- ***Security***: Are there any security concerns?
- ***Performance***: Are there any performance concerns?

## Review Velocity

- Reviews should begin within 4 business hours.
- Changes should be reviewed within 1 business day.
- Large changes should be split into smaller, incremental changes.

# Technical Debt Management

## Classification

| Category | Description | Approach |
| --- | --- | --- |
+-------------+------------------------------------------+---------------------------------+
| Strategic | Intentional debt taken to meet a | Track, schedule repayment. |
| --- | --- | --- |
|  | deadline with a plan to repay. |  |
+-------------+------------------------------------------+---------------------------------+
| Accidental | Accumulated through inadequate design, | Assess, prioritise, reduce |
| --- | --- | --- |
|  | insufficient testing or neglect. | incrementally. |
+-------------+------------------------------------------+---------------------------------+

## Management Process

1. ***Identify***: Use tools (SonarQube, CodeClimate) and manual review.
2. ***Classify***: Strategic or accidental? Severity?
3. ***Track***: Record in the team's tracking system.
4. ***Prioritise***: Balance against feature work.
5. ***Remediate***: Fix incrementally, not in rewrites.
6. ***Prevent***: Improve processes to reduce future debt.

# Quality Culture

## Practices for Building Quality Culture

- ***Blame-free post-mortems***: Focus on process, not people.
- ***Quality time***: Allocate regular time for quality improvements.
- ***Peer review***: Every change is reviewed by at least one peer.
- ***Knowledge sharing***: Rotate review duties and share quality
  practices.
- ***Continuous improvement***: Regularly reflect on quality practices
  and adjust.

## Anti-patterns

- Quality as a separate phase at the end of development.
- Quality owned by a separate team.
- Incentives that reward speed over quality.
- Ignoring quality debt until it becomes a crisis.

# AI Integration

AI can assist engineering quality through:

- Automating code review for common issues.
- Identifying test coverage gaps.
- Detecting code smells and duplication.
- Suggesting refactoring opportunities.
- Monitoring quality metrics and trends.

AI cannot replace human judgement in quality decisions. Quality
standards and priorities must be set by humans.

# Related Documents

- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
- [Testing Strategies Guide](../../guides/engineering/testing-strategies.md)
- [Code Review Playbook](../../playbooks/code-review/README.md)
- [Tech Debt Assessment Checklist](../../checklists/tech-debt-assessment.md)
- [Rails Project Standards](../../guides/rails/project-standards.md)
