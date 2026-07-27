+++
title = "Rails Upgrade Playbook"
description = "Repeatable workflow for upgrading Rails versions"
+++


# Objective

Upgrade a Rails application to a new version with minimal risk, minimal
downtime and clear rollback capability.

# Inputs

- Current Rails version.
- Target Rails version.
- Release notes and upgrade guides for the target version.
- List of gems and their compatibility with the target version.

# Prerequisites

- [ ] Current version is known and documented.
- [ ] Target version release notes have been reviewed.
- [ ] Deprecations in the current version have been addressed.
- [ ] Test suite provides adequate coverage of critical paths.
- [ ] Team has allocated time for the upgrade and potential rollback.
- [ ] Rollback plan is documented.

# Workflow

## Step 1: Assess Compatibility

- Review the Rails release notes for breaking changes.
- Check gem compatibility using `bundle outdated`.
- Identify gems that have not updated for the target version.
- Document deprecated APIs that will be removed.

## Step 2: Prepare the Codebase

- Resolve all deprecation warnings from the current version.
  Deprecation warnings from the current version should be addressed
  before upgrading. This narrows the source of issues after upgrade.
- Update the Ruby version if required by the target Rails version.
- Update the Gemfile to specify the target Rails version.

## Step 3: Upgrade Gems

- Run `bundle update rails` to update Rails and its dependencies.
- Run `bundle install` and verify the Gemfile.lock is correct.
- Update any gems that require newer versions for compatibility.
- Remove any gems that are no longer compatible.

## Step 4: Run Tests

- Run the full test suite.
- Fix any failures introduced by the upgrade.
- Pay special attention to:
  - Deprecation warnings (fix them, do not ignore them).
  - Changed behaviour in ActiveRecord, ActiveSupport and routing.
  - Changes to default configuration values.

## Step 5: Apply Configuration Changes

- Review the target version's default configuration changes.
- Update `config/application.rb` and environment files as needed.
- Add new configuration options with appropriate defaults.

## Step 6: Manual Verification

- Run the application locally against the target version.
- Verify critical user journeys manually.
- Check the admin interface and background jobs.
- Verify third-party integrations.

## Step 7: Deploy

- Deploy the upgraded application to a staging environment.
- Run the test suite in CI against the staging environment.
- Verify critical paths in staging.
- Monitor logs and error tracking for unexpected issues.

## Step 8: Production Deployment

- Deploy during a low-traffic period if possible.
- Monitor application health and error rates.
- Have the rollback plan ready.

# Checklist

- [ ] Deprecation warnings from current version are resolved.
- [ ] Gem compatibility is verified.
- [ ] Test suite passes on the target version.
- [ ] Configuration changes are applied.
- [ ] Critical paths are verified manually.
- [ ] Staging deployment is successful.
- [ ] Rollback plan is documented.
- [ ] Team is notified of the upgrade.

# Rollback Plan

If the upgrade causes issues in production:

1. Revert the Gemfile and Gemfile.lock to the previous version.
2. Revert any configuration changes.
3. Deploy the previous version.
4. Investigate and document the issue.

# Expected Outputs

- Application running on the target Rails version.
- Updated Gemfile.lock.
- Updated configuration files.
- No deprecation warnings.
- Documented issues encountered during upgrade.

# Related Documents

- [Rails Engineering Handbook](../../handbooks/rails/README/)
- [Rails Glossary](../../glossary/rails/README/)
- [Engineering Fundamentals Handbook](../../handbooks/engineering/README/)
