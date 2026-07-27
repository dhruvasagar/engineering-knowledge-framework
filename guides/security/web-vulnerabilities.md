+++
title = "Web Application Vulnerabilities"
description = "Common web application vulnerabilities and their mitigations"
+++


# Purpose

Understanding common web vulnerabilities is essential for building
secure applications.

This guide explains the most prevalent web vulnerabilities, how they
work, and how to prevent them.

# OWASP Top 10

The OWASP Top 10 is the industry-standard awareness document for web
application security.

## A01: Broken Access Control

Occurs when users can act outside their intended permissions.

Prevention:

- Deny access by default.
- Implement authorization checks on every request.
- Disable directory listing.
- Rate-limit API endpoints.

## A02: Cryptographic Failures

Occurs when sensitive data is not properly protected.

Prevention:

- Encrypt data in transit (TLS 1.2+).
- Encrypt sensitive data at rest.
- Use strong, modern algorithms.
- Never roll your own cryptography.

## A03: Injection

Occurs when untrusted data is sent to an interpreter as part of a
command or query.

Prevention:

- Use parameterized queries (SQL, NoSQL).
- Use safe APIs that avoid the interpreter entirely.
- Validate and sanitize all input.

## A04: Insecure Design

Occurs when architecture and design choices introduce risks.

Prevention:

- Perform threat modeling during design.
- Establish secure design patterns.
- Use secure by default configurations.

## A05: Security Misconfiguration

Occurs when security settings are not defined or deployed correctly.

Prevention:

- Automate deployment configuration.
- Disable unnecessary services and features.
- Use security linters for configuration files.

## A06: Vulnerable and Outdated Components

Occurs when using software components with known vulnerabilities.

Prevention:

- Regularly scan dependencies for vulnerabilities.
- Apply security patches promptly.
- Remove unused dependencies.

## A07: Identification and Authentication Failures

Occurs when authentication mechanisms are weak.

Prevention:

- Enforce strong password policies.
- Implement MFA for privileged access.
- Use secure session management.
- Protect against credential stuffing (rate limiting).

## A08: Software and Data Integrity Failures

Occurs when software or data is tampered with during build or
deployment.

Prevention:

- Sign software releases.
- Verify integrity of dependencies (checksums, signatures).
- Use secure CI/CD pipelines.

## A09: Security Logging and Monitoring Failures

Occurs when security events are not logged or monitored.

Prevention:

- Log authentication and authorization events.
- Monitor for suspicious activity.
- Implement alerting on security events.

## A10: Server-Side Request Forgery (SSRF)

Occurs when an attacker can make the server send requests to
unintended destinations.

Prevention:

- Validate and sanitize URLs provided by users.
- Restrict outbound network access.
- Use allowlists for external destinations.

# Rails-Specific Vulnerabilities

## Mass Assignment

Occurs when an attacker can modify model attributes they should not
have access to.

Prevention: Use strong parameters in Rails controllers.

## Insecure Deserialization

Occurs when untrusted data is deserialized without validation.

Prevention: Avoid deserializing untrusted data. Use JSON instead of
Marshal or YAML for external data.

# Related Documents

- [Security Engineering Handbook](../../handbooks/security/README/)
- [Secure Coding Practices Guide](../../guides/security/secure-coding/)
- [Security Glossary](../../glossary/security/README/)
- [Rails Security Review Checklist](../../checklists/rails/security-review/)
