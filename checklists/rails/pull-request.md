+++
title = "Rails Pull Request Checklist"
description = "Verification checklist for Rails pull requests"
+++


# Purpose

Ensure every Rails pull request meets quality standards before merging.

# Author Checklist

## Code Quality

- [ ] Code follows Rails conventions (naming, structure, routing).
- [ ] Controllers are thin — business logic is in models or service
      objects.
- [ ] No unnecessary N+1 queries. Includes are specified where needed.
- [ ] Database migrations are reversible and correctly ordered.
- [ ] No hard-coded values that should be configuration or constants.
- [ ] No commented-out code or debug logging.

## Testing

- [ ] New behaviour is covered by tests.
- [ ] Model specs cover validations, associations and scopes.
- [ ] Request specs cover API endpoints and status codes.
- [ ] System specs cover critical user journeys (if applicable).
- [ ] Test suite passes locally.
- [ ] No flaky tests introduced.

## Security

- [ ] User input is properly sanitized.
- [ ] Authentication and authorization are enforced.
- [ ] No sensitive data exposed in logs or responses.
- [ ] Mass assignment is protected (strong parameters used).

## Documentation

- [ ] API changes are documented.
- [ ] Database schema changes are documented.
- [ ] README or relevant guides are updated if needed.
- [ ] CHANGELOG is updated if appropriate.

## Migration Safety

- [ ] Migrations are reversible (`down` method or `reversible` block).
- [ ] Backfilling data is handled separately (not in migration).
- [ ] Zero-downtime deployment is considered for lock-heavy
      migrations.

# Reviewer Checklist

- [ ] Design follows Rails conventions.
- [ ] Tests are meaningful and test behaviour, not implementation.
- [ ] Error handling is appropriate.
- [ ] Performance concerns are addressed.
- [ ] No unnecessary dependencies introduced.

# Related Documents

- [Rails Engineering Handbook](../../handbooks/rails/README/)
- [Code Review Playbook](../../playbooks/code-review/README/)
- [Testing Rails Applications Guide](../../guides/rails/testing/)
- [Service Objects Guide](../../guides/rails/service-objects/)
