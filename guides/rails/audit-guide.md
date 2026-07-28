---
title: "Ruby on Rails: Audit Guide"
description: "Systematic audit of Rails applications covering code quality, performance, security, database health and operational concerns"
---


# Purpose

Rails applications accumulate technical debt, security vulnerabilities
and performance regressions over time.

This guide provides a systematic approach to auditing a Rails
application, covering code quality, performance, database health,
security and operational concerns.

For each area, it recommends both process steps and the appropriate
tools — many of which can be automated in CI to catch issues before
they reach production.

# Preparation and Scope

Before beginning an audit, establish clear goals and boundaries.

## Define Goals

What is the primary objective of this audit?

- Improve response times.
- Eliminate N+1 queries.
- Raise security posture.
- Reduce technical debt.
- Prepare for a major upgrade.

## Define Scope

- Which areas are in scope: application code, data access, external
  services, CI*CD, infrastructure?
- Which areas are explicitly out of scope.

## Set Up the Environment

- Use a separate audit branch or fresh clone.
- Install audit tools in a dedicated gem group in the Gemfile.
- Ensure the audit is reproducible by documenting the environment.

# Static Code Quality and Code Smells

## RuboCop

RuboCop is the standard Ruby linter. It enforces style conventions and
catches common errors.

Plugins:

- `rubocop-rails`: Rails-specific rules.
- `rubocop-performance`: Performance-related rules.
- `rubocop-rspec`: RSpec-specific rules.

Run:

```
bundle exec rubocop --auto-correct
```

## Reek

Reek detects code smells: Feature Envy, Long Methods, God Classes,
Utility Functions and more.

Configure via `.reek.yml` and run:

```
bundle exec reek
```

## Rails Best Practices

The `rails_best_practices` gem flags controller bloat, unused routes,
missing specs and other Rails-specific anti-patterns.

Run:

```
bundle exec rails_best_practices .
```

## Flog and Flay — Complexity and Duplication

- ***Flog***: Scores method complexity. High scores indicate methods that
  are difficult to understand and test.
  Run: `bundle exec flog app*`

- ***Flay***: Finds structurally similar code (duplication) across files.
  Run: `bundle exec flay app/`

Both are useful for identifying refactoring targets that other tools
may miss.

## CodeClimate / SonarQube — Aggregated Reports

For teams that want continuous quality metrics, integrate an aggregated
reporting tool:

- CodeClimate: Maintainability, duplication, complexity, test coverage.
- SonarQube: Quality gates, technical debt ratio, security hotspots.

These tools provide dashboards and enforce minimum quality thresholds in
CI.

# Code Review Process

Auditing is not just automated tools. Human code review remains
essential.

## Pull Request Template Checklist

Every PR should include a checklist covering:

- [ ] Tests added or updated for the change.
- [ ] RuboCop and Reek violations addressed.
- [ ] Security dependencies scanned.
- [ ] N+1 risk or unbounded queries reviewed.

## Peer Review Guidelines

Reviewers should verify:

- SOLID design principles are followed.
- Single responsibility is maintained.
- Domain models encapsulate business logic.
- Controllers remain thin.

## Automated Checks in CI

CI should run the full audit suite on every PR:

- Linters (RuboCop, Reek).
- Security scans (Brakeman, bundler-audit).
- Test suite.
- Coverage thresholds.

# Performance Profiling and Monitoring

## Rack::MiniProfiler — In-Browser Profiling

Measures SQL time, view rendering and call stack hotspots directly in
the browser. Install the gem and mount it in development.

## Bullet — N+1 Detection

The `bullet` gem catches missing or redundant eager loads (`includes`)
at runtime. Configure it to raise errors, log to console, or notify in
the browser.

## memory_profiler and derailed_benchmarks

- `memory_profiler`: Capture memory allocation snapshots to identify
  allocations hotspots.
- `derailed_benchmarks`: Compare boot and runtime memory.
  `bundle exec derailed bundle:mem` and `derailed exec perf:objects`.

## Application Performance Monitoring (APM)

Production profiling tools provide transaction traces, slow endpoint
identification and flamegraphs under real load.

- New Relic
- Skylight
- Scout APM

Use these to identify hotspots that only appear under production
traffic patterns.

# Database and Query Analysis

## ActiveRecord Query Logging

Enable verbose query logging in development to see the code-to-SQL
mapping:

```
config.active_record.verbose_query_logs = true
```

## EXPLAIN and EXPLAIN ANALYZE

Use the `rails db` console or a tool like PgHero to inspect query
plans. Look for sequential scans on large tables and missing indexes.

## PgHero

PgHero provides a dashboard showing:

- Slow queries.
- Index usage and suggestions.
- Replication lag.
- Table bloat.

## APM Database Breakdown

Use Skylight or Scout to see the percentage of time spent in the
database vs application code. This reveals whether performance issues
are query-bound or code-bound.

## Index Audit

Regularly review the schema for:

- Unused indexes (bloat).
- Missing indexes on foreign keys and frequently queried columns.
- `pg_stat_statements` for identifying the most expensive queries.

# Security Auditing

## Brakeman — Static Analysis

Brakeman scans for SQL injection, mass-assignment vulnerabilities, XSS,
CSRF gaps and other Rails-specific security issues.

Run:

```
bundle exec brakeman -q -o brakeman-report.html
```

## bundler-audit — Dependency Vulnerabilities

Scans `Gemfile.lock` for gems with known vulnerabilities.

Run:

```
bundle exec bundler-audit check --update
```

## OWASP ZAP / Arachni — Dynamic Scanning

For comprehensive security testing, use a dynamic scanner to crawl
endpoints and test for SQL injection, XSS, CSRF and other injection
attacks.

- OWASP ZAP: Free, extensive plugin ecosystem.
- Arachni: Commercial, high-performance scanner.

## Rails Secrets Audit

Ensure no credentials are committed to git history:

- `git-secrets`: Prevents committing secrets.
- `truffleHog`: Scans git history for high-entropy strings.

Credentials should use `config*credentials.yml.enc` for encrypted
storage.

## Content Security Policy and Secure Headers

Use the `secure_headers` gem to set:

- Content Security Policy (CSP).
- HTTP Strict Transport Security (HSTS).
- X-Frame-Options, X-Content-Type-Options.

## Authorization Checks

Verify that:

- Pundit or CanCanCan policies cover all controllers.
- `skip_before_action` is not used to bypass authorization.
- Critical paths have explicit authorization tests.

# Dependency and License Management

## Dependency Monitoring

- `gemnasium` (or Dependabot): Automated dependency vulnerability
  monitoring.
- `bundler-audit`: CI-enforced vulnerability check.

## License Compliance

Use `license_finder` to enforce approved licenses and prevent
introduction of incompatible dependencies.

## Version Hygiene

- Keep Ruby and Rails versions up to date.
- Apply security patches promptly.
- Regularly prune unused gems with `bundle doctor`.

# Testing and Coverage

## Test Quality

- RSpec or Minitest: Prefer fast, isolated tests.
- Avoid database hits in unit specs.
- Use FactoryBot or fixtures responsibly — keep factories minimal.

## Code Coverage

SimpleCov measures test coverage. Enforce minimum thresholds and break
the CI build if coverage drops below the agreed level.

## Mutation Testing

Mutation testing (Mutant, mutation-test) verifies test suite quality by
mutating code and expecting tests to fail. A test suite that passes
against mutated code has gaps.

- `mutant`: Ruby mutation testing.
- Integration is advanced — start with critical domain classes.

# Logging, Monitoring and Alerting

## Structured Logging

Use `lograge` to produce structured JSON logs in production. This makes
logs searchable and consumable by log aggregation systems.

## Exception Monitoring

- Sentry
- Honeybadger
- Rollbar

These provide real-time exception tracking with context (request
parameters, user, environment).

## Metrics and Alerting

For operational visibility:

- Prometheus + Grafana: Application metrics (request rates, error
  rates, queue lengths, latency percentiles).
- Datadog: Commercial APM and infrastructure monitoring.

Set SLAs and alert on latency spikes or error percentage thresholds.

# CI*CD and Release Hygiene

## CI Pipeline

Every push should run the full audit suite:

- Linters (RuboCop, Reek).
- Security scans (Brakeman, bundler-audit).
- Test suite with coverage thresholds.
- rails_best_practices and Flog*Flay for trend tracking.

## Deployment Safety

- Use canary or blue*green deployments to roll out changes safely.
- Use the `strong_migrations` gem to prevent dangerous schema changes
  (long-running locks, irreversible migrations).
- Maintain a rollback plan for every deployment.

## Pre-Release Audit

Before tagging a release, run a comprehensive audit pass:

- Full security audit.
- Dependency review.
- Performance benchmark comparison.
- Database migration review.

# Audit Frequency

| Audit Type | Frequency | Tools | Owner |
| --- | --- | --- | --- |
|-------------------------+-----------+------------------------------------------+-------------|
| Pre-commit | Every | RuboCop, Fasterer | Developer |
| --- | --- | --- | --- |
|  | commit |  |  |
|-------------------------+-----------+------------------------------------------+-------------|
| CI audit | Every | RuboCop, Brakeman, bundler-audit, Reek, | CI pipeline |
| --- | --- | --- | --- |
|  | push | rails_best_practices, Flog, Flay, tests |  |
|-------------------------+-----------+------------------------------------------+-------------|
| Security audit | Weekly | Brakeman, bundler-audit, OWASP ZAP | Security |
| --- | --- | --- | --- |
|  |  |  | lead |
|-------------------------+-----------+------------------------------------------+-------------|
| Dependency review | Weekly | Dependabot, bundler-audit, LicenseFinder | Platform |
| --- | --- | --- | --- |
|-------------------------+-----------+------------------------------------------+-------------|
| Performance audit | Monthly | Rack::MiniProfiler, Bullet, APM tools, | Performance |
| --- | --- | --- | --- |
|  |  | memory_profiler, PgHero | lead |
|-------------------------+-----------+------------------------------------------+-------------|
| Full quality audit | Monthly | All tools + manual review | Team |
| --- | --- | --- | --- |
|-------------------------+-----------+------------------------------------------+-------------|
| Pre-release audit | Per | All tools + manual review | Release |
| --- | --- | --- | --- |
|  | release |  | manager |
|-------------------------+-----------+------------------------------------------+-------------|

# Interpreting Audit Results

## Prioritization Framework

| Priority | Criteria | Action |
| --- | --- | --- |
|----------+-----------------------------------------------+-------------------------------------|
| Critical | Security vulnerability in production | Fix immediately. Deploy out of |
| --- | --- | --- |
|  | dependencies. | cycle if needed. |
|----------+-----------------------------------------------+-------------------------------------|
| High | Security warnings, data exposure, severe | Fix within the current sprint. |
| --- | --- | --- |
|  | performance issues. |  |
|----------+-----------------------------------------------+-------------------------------------|
| Medium | Code smells, style violations, inadequate | Schedule in a future sprint. |
| --- | --- | --- |
|  | coverage. |  |
|----------+-----------------------------------------------+-------------------------------------|
| Low | Cosmetic issues, minor style preferences. | Fix opportunistically. |
| --- | --- | --- |
|----------+-----------------------------------------------+-------------------------------------|

## False Positives

Every audit tool produces false positives.

- Document known false positives in a `.rubocop_todo.yml` or equivalent.
- Review and prune the false positive list periodically.
- When ignoring a finding, document why.

## Trend Tracking

Track audit results over time:

- Is the number of RuboCop offences increasing or decreasing?
- Are there recurring security vulnerabilities?
- Is test coverage improving or declining?
- Are code smells concentrated in specific areas?

# Rails-Specific Audit Areas

## Migration Audit

Review recent migrations for:

- Long-running migrations that could cause downtime.
- Missing indexes on foreign keys.
- Irreversible migrations without a `down` method.
- Backfilling data in migrations (should be in Rake tasks).
- Use `strong_migrations` to prevent dangerous changes.

## Route Audit

Review `config/routes.rb` for:

- Unused routes.
- Routes with unnecessary nesting.
- Routes exposing admin or internal functionality publicly.

## Configuration Audit

Review environment configuration for:

- Hard-coded secrets or API keys.
- Differences between development and production configuration.
- Disabled security features in production.

# Establishing Quality Standards

## Choosing a Baseline

Run the full audit suite on the current codebase to establish a
baseline.

- Generate a baseline report for each tool.
- Set a target for improvement over the next quarter.
- Configure tools to fail CI only on new offences, not existing ones
  (e.g., RuboCop's `--auto-gen-config`).

## Enforcement

- Run fast audits in CI on every push.
- Block merges that introduce critical or high-priority issues.
- Allow medium and low issues to be addressed outside the merge
  workflow.
- Review audit trends in sprint retrospectives.

# Documentation and Knowledge Transfer

Maintain a living runbook that covers:

- How to run each audit tool.
- How to interpret the reports.
- How to remediate common findings.
- How to on-board new team members to the audit process.

The audit process itself should be audited — regularly review whether
the tools and thresholds are still serving the team's goals.

# AI Integration

AI assistants can support Rails audits by:

- Reviewing RuboCop offences and suggesting fixes.
- Identifying the root cause of Brakeman warnings.
- Generating migration safety reviews.
- Suggesting test improvements based on coverage gaps.
- Reviewing the Gemfile for outdated or insecure dependencies.
- Analysing query plans and suggesting index improvements.

When asking AI for audit assistance, provide:

- The audit tool output.
- The relevant code context.
- The project's coding conventions.
- Specific areas of concern.

# Related Documents

- [Rails Engineering Handbook](../../handbooks/rails/README/)
- [Engineering Fundamentals Handbook](../../handbooks/engineering/README/)
- [Testing Rails Applications Guide](../../guides/rails/testing/)
- [Rails Upgrade Playbook](../../playbooks/rails/upgrade/)
- [Rails Pull Request Checklist](../../checklists/rails/pull-request/)
- [Rails Glossary](../../glossary/rails/README/)
- [Security Engineering Handbook](../../handbooks/security/README/)
