# Purpose

This glossary defines engineering quality terminology used throughout
the Engineering Knowledge Framework.

# Glossary

## Change Failure Rate {#change-failure-rate}

| Property   | Value                                                                    |
|------------|--------------------------------------------------------------------------|
| Definition | The percentage of deployments to production that result                  |
|            | in a failure, incident or rollback.                                      |
| Context    | A key DORA metric for measuring deployment reliability.                  |
|            | Target: < 5%.                                                            |
| Related    | [Defect Escape Rate](#defect-escape-rate), [MTTR](#mean-time-to-recover) |
| References | [Engineering Quality Handbook](../../handbooks/quality/README.md)        |

## Defect Escape Rate {#defect-escape-rate}

| Property   | Value                                                             |
|------------|-------------------------------------------------------------------|
| Definition | The percentage of defects found in production versus              |
|            | those found during development and testing.                       |
| Context    | Measures the effectiveness of testing and review                  |
|            | processes. Target: < 5%.                                          |
| Related    | [Change Failure Rate](#change-failure-rate)                       |
| References | [Engineering Quality Handbook](../../handbooks/quality/README.md) |

## Mean Time to Recover (MTTR) {#mean-time-to-recover}

| Property   | Value                                                                                  |
|------------|----------------------------------------------------------------------------------------|
| Definition | The average time it takes to restore service after a                                   |
|            | production incident or deployment failure.                                             |
| Context    | A key DORA metric for operational quality. Target:                                     |
|            | < 1 hour.                                                                              |
| Related    | [Change Failure Rate](#change-failure-rate), [Defect Escape Rate](#defect-escape-rate) |
| References | [Engineering Quality Handbook](../../handbooks/quality/README.md)                      |

## Quality Gate {#quality-gate}

| Property   | Value                                                             |
|------------|-------------------------------------------------------------------|
| Definition | An automated check that must pass before a change                 |
|            | proceeds to the next stage (commit, PR, deploy, release).         |
| Context    | Quality gates prevent defects from propagating. They              |
|            | should be automated, fast and enforced in CI/CD.                  |
| Related    | [Technical Debt](#technical-debt)                                 |
| References | [Engineering Quality Handbook](../../handbooks/quality/README.md) |

## Technical Debt {#technical-debt}

| Property   | Value                                                                      |
|------------|----------------------------------------------------------------------------|
| Definition | The gap between the current state of a codebase and the                    |
|            | desired state, representing future work required to                        |
|            | address suboptimal design, implementation or testing                       |
|            | decisions.                                                                 |
| Context    | Technical debt may be strategic (intentional with a                        |
|            | plan to repay) or accidental (accumulated through                          |
|            | neglect). All technical debt should be tracked                             |
|            | explicitly and regularly addressed.                                        |
| Related    | [Quality Gate](#quality-gate)                                              |
| References | [Engineering Quality Handbook](../../handbooks/quality/README.md),         |
|            | [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md) |

# Related Documents

- [Engineering Quality Handbook](../../handbooks/quality/README.md)
- [Engineering Glossary](../engineering/README.md)
- [Testing Strategies Guide](../../guides/engineering/testing-strategies.md)
