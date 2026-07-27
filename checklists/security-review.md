+++
title = "Security Review Checklist"
description = "General security review checklist (framework-wide)"
+++


# Purpose

Verify that a system meets security standards.

This checklist applies to all projects, regardless of language or
framework. For Rails-specific security checks, see
[Rails Security Review Checklist](rails/security-review/).

# Authentication

- [ ] Authentication is required for all protected endpoints.
- [ ] Passwords are hashed with a strong algorithm (bcrypt, argon2).
- [ ] Session management is secure (timeout, regeneration, HTTP-only).
- [ ] MFA is enforced for privileged access.
- [ ] Account lockout is enabled after repeated failures.

# Authorization

- [ ] Authorization is checked on every resource access.
- [ ] Authorization is enforced at the service layer, not only at UI.
- [ ] Default is deny — access must be explicitly granted.
- [ ] Privilege levels are clearly defined and enforced.

# Input Validation

- [ ] All external input is validated (type, length, format).
- [ ] Parameterized queries are used for all database access.
- [ ] File uploads are validated (type, size, content scanning).
- [ ] No raw SQL or command execution with user input.

# Output Protection

- [ ] Output is encoded appropriately for the context (HTML, JSON, JS).
- [ ] Security headers are configured (CSP, HSTS, XFO, XCTO).
- [ ] Error messages do not leak sensitive information.

# Data Protection

- [ ] Sensitive data is encrypted at rest.
- [ ] Data in transit uses TLS 1.2+.
- [ ] Secrets and credentials are not in the codebase.
- [ ] Encryption keys are stored separately from encrypted data.

# Dependencies

- [ ] Dependency vulnerability scan passes.
- [ ] No dependencies with known critical vulnerabilities.
- [ ] Unused dependencies are removed.

# Logging and Monitoring

- [ ] Authentication events are logged.
- [ ] Authorization failures are logged.
- [ ] Privileged operations are logged.
- [ ] Logs do not contain sensitive data.

# Infrastructure

- [ ] HTTPS is enforced (HTTP redirects to HTTPS).
- [ ] Rate limiting is configured on authentication endpoints.
- [ ] Admin interfaces are restricted.
- [ ] Production does not expose debug or development endpoints.

# Related Documents

- [Security Engineering Handbook](../handbooks/security/README/)
- [Security Review Playbook](../playbooks/security-review/README/)
- [Secure Coding Guide](../guides/security/secure-coding/)
- [Web Vulnerabilities Guide](../guides/security/web-vulnerabilities/)
