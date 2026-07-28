# Objective

Upgrade a Rails application to a new version with minimal risk, minimal
downtime and clear rollback capability.

This playbook describes both the manual upgrade workflow and
AI-assisted upgrade using the
[Ruby Upgrade Toolkit](https://github.com/dhruvasagar/ruby-upgrade-toolkit),
a Claude Code plugin that automates Ruby and Rails upgrades.

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

# AI-Assisted Upgrade

The [Ruby Upgrade Toolkit](https://github.com/dhruvasagar/ruby-upgrade-toolkit)
is a Claude Code plugin that packages skills and commands for
AI-assisted Ruby and Rails upgrades. It follows the same phased
methodology as this playbook but automates detection, fix application,
and verification.

## Installation

Add the marketplace and install the plugin in Claude Code:

```
/plugin marketplace add dhruvasagar/ruby-upgrade-toolkit
/plugin install ruby-upgrade-toolkit@dhruvasagar
/reload-plugins
```

## Workflow Modes

The toolkit provides three modes of operation, each suited to
different levels of control:

### Mode 1: Fully Automated

```
/ruby-upgrade-toolkit:upgrade ruby:X.Y.Z [rails:X.Y]
```

One command runs everything: detects versions, validates
compatibility, computes the full upgrade path with intermediate
versions, applies fixes phase by phase (Ruby first, then Rails),
verifies after each phase with the test suite and RuboCop, and
pauses with a recovery menu if anything fails.

**Use when** you want to move quickly and trust Claude to sequence
and execute the work.

### Mode 2: Review First, Then Automate

```
/ruby-upgrade-toolkit:audit ruby:X.Y.Z [rails:X.Y.Y]   # understand the scope
/ruby-upgrade-toolkit:plan ruby:X.Y.Z [rails:X.Y.Y]    # review the phase sequence
/ruby-upgrade-toolkit:upgrade ruby:X.Y.Z [rails:X.Y.Y] # execute the plan
```

`audit` surfaces breaking changes and gives an effort estimate
before touching any code. `plan` shows exactly which phases will
run, in what order, with per-phase effort, risk, blast radius and
confidence estimates derived from concrete grep counts. Once you
approve, `upgrade` executes the sequence.

**Use when** you're doing a major version jump or want to
understand scope before committing to execution.

### Mode 3: Fully Manual (Per-Phase Control)

```
/ruby-upgrade-toolkit:audit ruby:X.Y.Z [rails:X.Y.Y]   # read-only scan
/ruby-upgrade-toolkit:plan  ruby:X.Y.Z [rails:X.Y.Y]   # roadmap + task list
/ruby-upgrade-toolkit:fix   next                         # apply next phase
```

`plan` creates a task list (one task per upgrade phase). `fix next`
reads the list, applies the next pending phase, runs the test suite
iteratively until green, runs RuboCop iteratively until clean, then
prompts for a commit with a detailed message. Iterate `fix next`
until all phases are complete.

**Use when** you want to inspect and approve changes phase by
phase, or resume a partially completed upgrade.

## How It Works

1. **Phase sequencing**: Ruby upgrades complete before Rails
   upgrades begin. Intermediate minor versions are never skipped
   (e.g., 6.1 → 7.0 → 7.1 → 8.0, not 6.1 → 8.0).
2. **Per-phase verification**: Each phase runs the full test suite
   and RuboCop before prompting for a commit. Failures pause with
   recovery options.
3. **Commit checkpoints**: Each successful phase produces a
   detailed commit message itemising version pins, gem diffs, fix
   counts and verification results.
4. **Custom rules**: Project-specific policies (gem pins, gem
   swaps, private-source substitutions, extra verification gates)
   can be declared in `.ruby-upgrade-toolkit/rules.yml`.

## Command Reference

| Command | Purpose |
| --- | --- |
| `audit ruby:X.Y.Z [rails:X.Y]` | Read-only pre-upgrade assessment. Surfaces breaking changes, gem incompatibilities, effort estimate. Never modifies files. |
| `plan ruby:X.Y.Z [rails:X.Y]` | Generates a phased upgrade roadmap with per-phase effort/risk/blast-radius estimates. Creates a task list that drives `fix` and `upgrade`. |
| `fix next` | Applies the next pending upgrade phase. Iterates test suite and RuboCop to green. Prompts for commit with detailed message. |
| `upgrade ruby:X.Y.Z [rails:X.Y]` | Full automated pipeline: prerequisites, phased fixes with per-phase commits, final infra checks. |
| `status` | Current upgrade health dashboard: versions, test status, deprecation warnings, RuboCop offenses, Zeitwerk status. |
| `rules` | Manage project-specific upgrade policies (gem pins, swaps, verification gates) in `.ruby-upgrade-toolkit/rules.yml`. |

## Relationship to Manual Workflow

The toolkit automates the same phases described in the manual
workflow above. Understanding the manual process helps you:

- Review the toolkit's plan and audit output with context.
- Intervene manually when a phase fails.
- Customise the toolkit's behaviour via `rules.yml`.

The manual workflow remains the definitive reference for what each
upgrade phase entails.

## When to Use Each Approach

| Situation | Recommended Approach |
| --- | --- |
| Simple patch bump | Manual or Mode 1 (automated) |
| Minor version jump, small codebase | Mode 1 (automated) |
| Minor version jump, large codebase | Mode 2 (review then automate) |
| Major version jump | Mode 2 or Mode 3 (per-phase control) |
| First-time upgrade on unfamiliar codebase | Mode 3 (full control) |
| Learning the upgrade process | Manual workflow first, then try the toolkit |

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

- [Rails Engineering Handbook](../../handbooks/rails/README.md)
- [Rails Glossary](../../glossary/rails/README.md)
- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
