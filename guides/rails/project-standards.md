# Purpose

Every Rails project should start with a consistent baseline of code
quality tools, testing standards and CI/CD configuration.

This document defines the mandatory tooling and practices that every
Rails project in this organization must adopt. It ensures consistency
across projects, reduces onboarding friction and prevents common
issues from reaching production.

Unlike the [Rails Audit Guide](./audit-guide.md), which describes how to perform a
periodic audit, this document defines the standards that should be in
place from project inception and enforced continuously.

# Scope

This standard applies to all Rails projects within the organization,
including:

- Greenfield applications.
- Existing applications being brought under management.
- Internal tools and services.
- API-only Rails applications.

Exceptions require written approval from the engineering lead.

# Mandatory Tooling

Every Rails project MUST include the following tools.

## Style and Correctness — RuboCop

Purpose: Enforce consistent Ruby style and catch common errors.

Mandatory gems:

```
group :development, :test do
  gem "rubocop", require: false
  gem "rubocop-rails", require: false
  gem "rubocop-rspec", require: false
  gem "rubocop-performance", require: false
end
```

Configuration requirements:

- Inherit from rubocop-rails and rubocop-rspec defaults.
- Enable `NewCops` to adopt new rules as they are released.
- Keep configuration in version control at `.rubocop.yml`.
- Run in CI with `--fail-level`convention=.

## Security — Brakeman

Purpose: Static analysis for security vulnerabilities.

Mandatory gem:

```
group :development, :test do
  gem "brakeman", require: false
end
```

CI requirement:

- Run `bundle exec brakeman --no-pager --quiet --ensure-latest` in CI.
- Fail the build on any new warning.

## Dependency Vulnerabilities — bundler-audit

Purpose: Scan Gemfile.lock for known vulnerabilities.

Mandatory gem:

```
group :development, :test do
  gem "bundler-audit", require: false
end
```

CI requirement:

- Run `bundle exec bundler-audit check --update` in CI.
- Fail the build on any critical or high-severity advisory.

## N+1 Detection — Bullet

Purpose: Detect N+1 queries and unused eager loading in development and
test.

Mandatory gem:

```
group :development, :test do
  gem "bullet", require: false
end
```

Configuration requirements:

- Enable in development and test environments.
- Configure to raise errors in test.
- Configure to log warnings in development.

## Performance Profiling — Rack::MiniProfiler

Purpose: In-browser performance profiling for development.

Mandatory gem:

```
group :development do
  gem "rack-mini-profiler", require: false
end
```

Configuration requirements:

- Enabled in development only.
- Never enabled in production.

## Code Coverage — SimpleCov

Purpose: Measure test coverage and enforce minimum thresholds.

Mandatory gem:

```
group :test do
  gem "simplecov", require: false
end
```

Configuration requirements:

- Generate coverage report on every CI run.
- Enforce minimum coverage threshold (>= 90% for new projects).
- Fail CI build if coverage drops below threshold.

## Recommended Tooling

The following tools are strongly recommended but not mandatory:

| Tool                 | Purpose                               | When to Add                          |
|----------------------|---------------------------------------|--------------------------------------|
| Reek                 | Code smell detection                  | Existing codebases with significant  |
|                      |                                       | technical debt.                      |
| rails_best_practices | Rails-specific anti-pattern detection | Teams new to Rails conventions.      |
| Flog / Flay          | Complexity and duplication tracking   | Projects with complex domain logic.  |
| standardrb           | Opinionated zero-config Ruby style    | Teams that prefer no RuboCop config. |
| strong_migrations    | Safe migration enforcement            | Projects with production databases.  |
| LicenseFinder        | License compliance                    | Projects with third-party            |
|                      |                                       | distribution.                        |
| Mutant               | Mutation testing                      | Critical domain logic that demands   |
|                      |                                       | high test quality.                   |

# CI*CD Baseline

Every Rails project MUST have a CI pipeline that runs on every push.

## Minimum CI Pipeline

```
# .github*workflows*ci.yml
name: CI
on: [push]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions*checkout@v4
      - uses: ruby*setup-ruby@v1
        with:
          bundler-cache: true
      - run: bundle exec rubocop
      - run: bundle exec brakeman --no-pager --quiet --ensure-latest
      - run: bundle exec bundler-audit check --update

  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    steps:
      - uses: actions*checkout@v4
      - uses: ruby*setup-ruby@v1
        with:
          bundler-cache: true
      - run: bundle exec rails db:create db:migrate
      - run: bundle exec rspec
      - run: bundle exec rails db:seed  # if applicable
```

## Quality Gates

The CI pipeline MUST block merges when:

- RuboCop reports any convention-level offence.
- Brakeman reports any warning.
- bundler-audit reports any advisory.
- Test suite has any failure.
- Code coverage drops below the project's threshold.

## Scheduled Audits

In addition to per-push CI, schedule these weekly:

- `bundler-audit` full scan (`--update`).
- `brakeman` full report output.

# Project Bootstrap

Every new Rails project MUST be initialized with the mandatory tooling
from this document.

## Default Gemfile Template

```
source "https:/*rubygems.org"

ruby "`> 3.3"

gem "rails", "`> 7.1"
gem "pg"
gem "puma"

# Authentication and authorization
gem "devise"
gem "pundit"

group :development, :test do
  gem "rspec-rails"
  gem "factory_bot_rails"
  gem "rubocop", require: false
  gem "rubocop-rails", require: false
  gem "rubocop-rspec", require: false
  gem "rubocop-performance", require: false
  gem "brakeman", require: false
  gem "bundler-audit", require: false
  gem "bullet"
end

group :development do
  gem "rack-mini-profiler", require: false
end

group :test do
  gem "simplecov", require: false
end
```

## Bootstrap Script

When creating a new project, run:

```
rails new my_app --database=postgresql --skip-test
cd my_app

# Add testing framework
bundle add rspec-rails --group "development, test"
rails generate rspec:install

# Add mandatory tooling
bundle add rubocop --group "development, test" --require false
bundle add rubocop-rails --group "development, test" --require false
bundle add rubocop-rspec --group "development, test" --require false
bundle add rubocop-performance --group "development, test" --require false
bundle add brakeman --group "development, test" --require false
bundle add bundler-audit --group "development, test" --require false
bundle add bullet --group "development, test"
bundle add rack-mini-profiler --group "development" --require false
bundle add simplecov --group "test" --require false

# Set up pre-commit hooks (optional but recommended)
# See .hooks section below
```

# Pre-Commit Hooks

While not mandatory, pre-commit hooks catch issues before they reach
CI. Every project SHOULD configure them.

## Using Lefthook

```
# lefthook.yml
pre-commit:
  parallel: true
  commands:
    rubocop:
      run: bundle exec rubocop --force-exclusion {staged_files}
    brakeman:
      run: bundle exec brakeman --no-pager --quiet
```

## Using Overcommit

```
# .overcommit.yml
PreCommit:
  RuboCop:
    enabled: true
    command: ["bundle", "exec", "rubocop", "--force-exclusion"]
  Brakeman:
    enabled: true
    command: ["bundle", "exec", "brakeman", "--no-pager", "--quiet"]
```

# Exceptions and Escalation

## Requesting an Exception

A project may request an exception from a mandatory requirement by:

1. Documenting the reason in the project's README or a decision record.
2. Obtaining written approval from the engineering lead.
3. Setting a review date to reassess the exception.

## Reasons That May Justify an Exception

- The tool is incompatible with the project's technology stack.
- The project is in maintenance mode with a defined end-of-life.
- The project is a prototype explicitly designated as non-production.

## Reasons That Do NOT Justify an Exception

- "We don't have time to set it up."
- "The codebase won't pass the checks."
- "We've never used it before."

# Compliance Verification

## For New Projects

The project bootstrap MUST include all mandatory tools before the first
production deployment. This is verified during the architecture review.

## For Existing Projects

Existing projects MUST add the mandatory tooling within one quarter of
this standard being adopted. A transition plan SHOULD be documented if
immediate compliance is not feasible.

## Periodic Review

This standard SHOULD be reviewed quarterly to:

- Add new tools that have become industry standard.
- Remove tools that are no longer valuable.
- Adjust thresholds based on experience.

# Related Documents

- [Rails Audit Guide](./audit-guide.md)
- [Rails Engineering Handbook](../../handbooks/rails/README.md)
- [Testing Rails Applications Guide](../../guides/rails/testing.md)
- [Rails Upgrade Playbook](../../playbooks/rails/upgrade.md)
- [Rails Pull Request Checklist](../../checklists/rails/pull-request.md)
- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
