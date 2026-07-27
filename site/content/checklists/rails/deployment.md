+++
title = "Rails Deployment Checklist"
description = "Pre-deployment verification checklist for Rails applications"
+++


# Purpose

Ensure every Rails deployment is safe, reversible and verified.

# Pre-Deployment

- [ ] All CI checks pass (RuboCop, Brakeman, bundler-audit, tests).
- [ ] Code coverage meets the project threshold.
- [ ] No pending migrations with dangerous operations.
- [ ] Migrations are reviewed by a second engineer.
- [ ] Strong migrations check passes.
- [ ] Gemfile.lock is up to date.
- [ ] Release notes are documented.
- [ ] Rollback plan is documented.
- [ ] Deployment window is communicated to the team.

# Migration Safety

- [ ] All migrations are reversible.
- [ ] No columns added with a default value on large tables.
- [ ] Indexes on large tables use `algorithm: :concurrently`.
- [ ] Data backfills are in Rake tasks, not migrations.
- [ ] Column removals use the two-phase process (ignore → remove).
- [ ] Renames are handled with the add*backfill*drop pattern.

# Deployment

- [ ] Migrations are run before application code deployment.
- [ ] Monitoring is active (error rates, response times, queue depth).
- [ ] Smoke tests pass after deployment.
- [ ] Background jobs are processing correctly.
- [ ] No unexpected error spikes.

# Post-Deployment

- [ ] Deployment is recorded in the release log.
- [ ] Rollback plan is updated based on lessons learned.
- [ ] Monitoring continues for the next 24 hours.
- [ ] Team is notified of successful deployment.

# Related Documents

- [Rails Deployment Playbook](../..*playbooks*rails*deployment*)
- [Rails Engineering Handbook](../..*handbooks*rails*README*)
- [Rails Pull Request Checklist](../..*checklists*rails*pull-request*)
- [Rails Security Review Checklist](../..*checklists*rails*security-review*)
