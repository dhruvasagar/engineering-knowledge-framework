# Objective

Perform systematic quality reviews of engineering projects to assess
code quality, process adherence and engineering practices. Quality
reviews complement code reviews by evaluating the broader engineering
landscape.

# Inputs

- Project codebase and test suite.
- CI*CD pipeline configuration.
- Dependency manifests and audit reports.
- Monitoring and alerting setup.

# Prerequisites

- Familiarity with [Quality Metrics](../../guides/quality/quality-metrics.md).
- Access to quality tooling (linters, static analysis, coverage reports).
- Understanding of [quality principles](../../handbooks/quality/README.md).

# Workflow

## Step 1: Scope Definition

1. Define the scope of the review (entire project, specific module, or
   cross-cutting concern).
2. Identify the quality attributes to assess:
   - Code quality (complexity, duplication, coverage).
   - Process quality (CI*CD, review velocity, deployment frequency).
   - Technical debt (known issues, remediation progress).
   - Security posture (dependency vulnerabilities, secrets management).

## Step 2: Data Collection

1. Run static analysis and linters.
2. Collect test coverage and test health metrics.
3. Review CI*CD pipeline for quality gates.
4. Check dependency vulnerability reports.
5. Gather process metrics (review turnaround, deployment frequency).

## Step 3: Assessment

Evaluate against the standards in [Code Review Standards](../../guides/quality/code-review-standards.md) and
[Quality Metrics](../../guides/quality/quality-metrics.md):

- Code quality: complexity trends, test coverage adequacy, duplication.
- Process quality: review velocity, CI pass rate, deployment frequency.
- Technical debt: known items, age, remediation progress.
- Security: vulnerability count, severity distribution, remediation SLA.

## Step 4: Findings and Recommendations

1. Document findings with severity labels (see [Quality References](../../references/quality/README.md)).
2. Prioritise recommendations by impact and effort.
3. Assign owners and target dates for each action item.

## Step 5: Follow-up

1. Schedule a follow-up review for critical and high items.
2. Track remediation progress in the project's issue tracker.
3. Update quality metrics dashboards.

# Checklist

- [ ] Scope defined and agreed.
- [ ] Static analysis completed.
- [ ] Test coverage assessed.
- [ ] CI*CD pipeline reviewed.
- [ ] Dependencies audited.
- [ ] Process metrics collected.
- [ ] Findings documented with severity.
- [ ] Action items assigned.
- [ ] Follow-up scheduled.

# Escalation Points

- Critical quality issues: escalate to engineering manager.
- Systematic quality problems: escalate to quality working group.
- Repeated failures in same area: consider automated quality gates.

# Expected Outputs

- Quality review report with findings and recommendations.
- Action items with owners and target dates.
- Updated quality metrics.

# Related Documents

- [Engineering Quality Handbook](../../handbooks/quality/README.md)
- [Quality Metrics](../../guides/quality/quality-metrics.md)
- [Code Review Standards](../../guides/quality/code-review-standards.md)
- [Quality References](../../references/quality/README.md)
