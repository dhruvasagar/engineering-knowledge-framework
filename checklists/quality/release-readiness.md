---
title: "Release Readiness Checklist"
description: "Verification before production release"
---


# Purpose

Verify that the system is ready for production release. This checklist
should be completed before every production deployment.

# Code and Configuration

- [ ] All code changes are reviewed and approved.
- [ ] Feature flags are configured correctly.
- [ ] Configuration changes are reviewed and applied.
- [ ] Database migrations are reviewed and have rollback plans.
- [ ] No debug or development-only code in the release.

# Testing

- [ ] All automated tests pass.
- [ ] Test coverage meets the project threshold.
- [ ] Manual smoke tests pass in staging.
- [ ] Integration tests pass.
- [ ] Performance benchmarks show no regression.

# Security

- [ ] Security scan passes with no critical or high findings.
- [ ] Dependency audit shows no vulnerable dependencies.
- [ ] Secrets rotation completed if needed.
- [ ] Access controls are reviewed.

# Deployment

- [ ] Deployment playbook is up to date.
- [ ] Rollback plan is documented and tested.
- [ ] Deployment window is scheduled.
- [ ] Release announcement is prepared.
- [ ] Monitoring and alerting are configured for the release.

# Documentation

- [ ] Changelog is updated with release notes.
- [ ] API changes are documented.
- [ ] Migration guide is prepared for breaking changes.
- [ ] Runbook is updated if operational procedures changed.

# Post-Release

- [ ] Health checks pass after deployment.
- [ ] Error rates are normal.
- [ ] Performance metrics are normal.
- [ ] Monitoring dashboards are reviewed.
- [ ] Release is announced to stakeholders.

# Related Documents

- [Release Quality Gate Playbook](../../playbooks/quality/release-quality-gate/)
- [Rails Deployment Playbook](../../playbooks/rails/deployment/)
- [Rails Deployment Checklist](../../checklists/rails/deployment/)
