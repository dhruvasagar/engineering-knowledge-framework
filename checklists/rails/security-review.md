+++
title = "Rails Security Review Checklist"
description = "Verification checklist for Rails application security"
+++


# Purpose

Verify that a Rails application meets security standards before
deployment.

# Authentication

- [ ] Passwords are hashed with bcrypt (Devise default).
- [ ] Session expiration is configured.
- [ ] Account lockout is enabled after repeated failures.
- [ ] Email confirmation is required for new accounts.
- [ ] No hard-coded credentials in the codebase.

# Authorization

- [ ] Pundit or CanCanCan policies cover all controllers.
- [ ] `skip_before_action` is not used to bypass authorization.
- [ ] Authorization is enforced at the service*model level, not only
      at the controller level.
- [ ] API endpoints validate authentication tokens.

# Data Protection

- [ ] Sensitive data is encrypted at rest.
- [ ] Secrets are stored in `config*credentials.yml.enc`.
- [ ] No secrets committed to git history.
- [ ] Database credentials use environment variables, not defaults.
- [ ] API keys are rotated regularly.

# Input Validation

- [ ] Strong parameters are used everywhere.
- [ ] SQL injection is prevented via ActiveRecord or sanitized queries.
- [ ] No raw SQL in the codebase (unless reviewed and documented).
- [ ] File uploads are validated (type, size, content).
- [ ] Redirect URLs are validated (open redirect prevention).

# Output Protection

- [ ] CSRF protection is enabled (default in Rails).
- [ ] Content Security Policy header is configured.
- [ ] X-Frame-Options header is set.
- [ ] X-Content-Type-Options header is set.
- [ ] User-generated content is escaped in views.

# Dependency Security

- [ ] bundler-audit passes with no advisories.
- [ ] Dependabot or equivalent is enabled for automated updates.
- [ ] Gems are regularly updated.
- [ ] No gems with known unpatched vulnerabilities.

# Infrastructure

- [ ] HTTPS is enforced (HSTS configured).
- [ ] Rate limiting is enabled on authentication endpoints.
- [ ] Production error pages do not leak stack traces.
- [ ] Logs do not contain sensitive data (passwords, tokens, PII).
- [ ] Admin interfaces are restricted by IP or VPN.

# Related Documents

- [Rails Engineering Handbook](../../handbooks/rails/README/)
- [Authentication and Authorization Guide](../../guides/rails/authentication-authorization/)
- [Security Engineering Handbook](../../handbooks/security/README/)
- [Rails Deployment Playbook](../../playbooks/rails/deployment/)
