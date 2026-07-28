---
title: "Release Quality Gate Playbook"
description: "Quality verification before release"
---


# Objective

Ensure every release meets defined quality standards before reaching
production. Quality gates provide automated and manual checks that
protect users and infrastructure.

# Inputs

- Release candidate version.
- CI*CD pipeline results.
- Test coverage and health reports.
- Security scan results.
- Performance benchmark results.

# Prerequisites

- CI*CD pipeline configured with quality gates (see [Project Standards](../../guides/rails/project-standards/)).
- Quality metrics baselines established (see [Quality Metrics](../../guides/quality/quality-metrics/)).
- [Release Readiness Checklist](../../checklists/quality/release-readiness/) available.

# Workflow

## Step 1: Automated Gates

Before human review, the CI*CD pipeline must pass these automated gates:

| Gate | Threshold |
| --- | --- |
+----------------------+--------------------------------------------------+
| Test pass rate | 100% — no skipped, failed or flaky tests. |
| --- | --- |
| Test coverage | >= 80% line coverage (project baseline). |
| Linting | No errors, warnings reviewed. |
| Security scan | No critical or high vulnerabilities. |
| Dependency audit | No vulnerable or deprecated dependencies. |
| Performance check | No regression beyond 5% on critical paths. |

## Step 2: Manual Review Gates

Automated gates passed? Proceed to manual review:

1. ***Code review completeness***: All PRs merged into the release are reviewed.
2. ***Changelog accuracy***: Changelog entries are complete and accurate.
3. ***API compatibility***: No breaking changes without documented migration.
4. ***Database migration safety***: Migrations have rollback plans.
5. ***Feature flags***: New features are behind flags if not fully ready.

## Step 3: Go*No-Go Decision

Based on gate results, decide:

- ***Go***: All gates pass. Release proceeds.
- ***Go with exceptions***: Non-critical gates fail, exceptions documented
  and approved.
- ***No-Go***: Critical gates fail. Release is blocked until resolved.

## Step 4: Release

1. Tag the release candidate.
2. Deploy to staging and verify.
3. Run smoke tests in staging.
4. Deploy to production following the deployment playbook.
5. Monitor for incidents during the cooldown period.

## Step 5: Post-Release

1. Verify all services are healthy.
2. Check error rates and performance metrics.
3. Document any release issues for the retrospective.
4. Close the release checklist.

# Quality Gate Summary

| Gate | Automated | Manual | Blocking |
| --- | --- | --- | --- |
+--------------------+-----------+--------+----------+
| Tests pass | ✅ |  | ✅ |
| --- | --- | --- | --- |
| Coverage threshold | ✅ |  | ✅ |
| Linting | ✅ |  | ✅ |
| Security scan | ✅ |  | ✅ |
| Dependency audit | ✅ |  | ✅ |
| Performance | ✅ |  | ⚠️ |
| Code review |  | ✅ | ✅ |
| Changelog |  | ✅ | ✅ |
| API compat |  | ✅ | ⚠️ |
| Migration safety |  | ✅ | ✅ |
| Feature flags |  | ✅ | ⚠️ |

# Checklist

- [ ] All automated gates pass.
- [ ] Code reviews complete.
- [ ] Changelog verified.
- [ ] API compatibility checked.
- [ ] Migrations reviewed.
- [ ] Feature flags configured.
- [ ] Go/No-Go decision documented.
- [ ] Staging deployment verified.
- [ ] Production deployment completed.
- [ ] Post-release monitoring active.

# Escalation Points

- Blocking gate failure: fix before release or obtain exception approval.
- Performance regression > 5%: investigate before release.
- Security vulnerability discovered: follow [Dependency Security](../../guides/security/dependency-security/) response.

# Expected Outputs

- Release decision documented with rationale.
- Quality gate results archived.
- Release deployed to production.
- Post-release monitoring active for cooldown period.

# Related Documents

- [Quality Metrics](../../guides/quality/quality-metrics/)
- [Rails Project Standards](../../guides/rails/project-standards/)
- [Rails Deployment Checklist](../../checklists/rails/deployment/)
- [Rails Deployment Playbook](../../playbooks/rails/deployment/)
