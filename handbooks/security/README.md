---
title: "Security Engineering Handbook"
description: "Security engineering is the discipline of building systems that remain secure even when under attack."
type: handbook
capability: security
status: published
last_reviewed: 2026-07-28
---

# Purpose

Security engineering is the discipline of building systems that remain
secure even when under attack.

Security is not a feature or a phase. It is a property of the entire
system that must be considered from design through operations.

This handbook defines the principles, standards and practices for
building and maintaining secure systems within this organization.

It builds upon the [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md) and
[Software Architecture Handbook](../../handbooks/architecture/README.md), applying their principles to the
security domain.

# Scope

This handbook covers:

- Security principles and philosophy.
- Threat modeling and risk assessment.
- Secure development lifecycle.
- Security standards for engineering teams.
- Common vulnerabilities and mitigations.
- Security testing and verification.
- Incident response fundamentals.
- AI integration in security engineering.

# Principles

## Defense in Depth

No single security control is sufficient. Layer multiple independent
defenses so that if one fails, another provides protection.

Layers include:

- Network security (firewalls, segmentation).
- Application security (input validation, authentication).
- Data security (encryption, access control).
- Operational security (monitoring, incident response).

## Least Privilege

Every user, process and system should have only the minimum permissions
necessary to perform its function.

Apply least privilege at every level:

- Database accounts should have only the permissions needed.
- Service accounts should not have admin access.
- Users should not have access they do not need.

## Secure by Default

Systems should be secure in their default configuration.

Engineers should explicitly opt into reduced security, not opt into
increased security. Defaults should be restrictive.

## Fail Securely

When a system fails, it should fail in a secure state.

- Access control failures should deny access.
- Authentication failures should deny access.
- Error messages should not leak sensitive information.

## Never Trust User Input

All user input is potentially malicious until validated.

This applies to:

- Form parameters and query strings.
- HTTP headers and cookies.
- File uploads.
- API request bodies.
- Data from external systems.

## Security is Everyone's Responsibility

Security is not the sole responsibility of a security team.

Every engineer is responsible for understanding security principles and
applying them in their work.

# Threat Modeling

Threat modeling is the practice of identifying potential threats and
designing mitigations before they are exploited.

## When to Threat Model

- During the design phase of a new system or feature.
- When integrating with an external system.
- When introducing a new technology or dependency.
- When a significant architectural change is proposed.

## STRIDE Framework

| Threat       | Definition                  | Example                        |
|--------------|-----------------------------|--------------------------------|
| Spoofing     | Impersonating another user  | Stealing session token.        |
|              | or system.                  |                                |
| Tampering    | Modifying data or code      | Modifying request parameters.  |
|              | without authorization.      |                                |
| Repudiation  | Denying an action was       | User claims they did not       |
|              | performed.                  | make a transaction.            |
| Information  | Exposing information to     | Leaking customer data through  |
| Disclosure   | unauthorized parties.       | an API endpoint.               |
| Denial of    | Making a system unavailable | Flooding an endpoint with      |
| Service      | to legitimate users.        | requests to exhaust resources. |
| Elevation of | Gaining unauthorized access | Exploiting a vulnerability to  |
| Privilege    | to higher permissions.      | gain admin access.             |

# Secure Development Lifecycle

Integrate security into every phase of development.

## Design Phase

- Perform threat modeling for significant changes.
- Review security architecture.
- Identify security requirements.
- Document trust boundaries.

## Development Phase

- Follow secure coding standards.
- Validate all inputs.
- Use parameterized queries (no raw SQL concatenation).
- Encrypt sensitive data at rest and in transit.
- Log security-relevant events.

## Testing Phase

- Run static analysis security tools (SAST).
- Run dependency vulnerability scanners.
- Perform dynamic security testing (DAST) where feasible.
- Conduct manual security review for critical changes.

## Deployment Phase

- Verify production configuration is secure.
- Ensure secrets are not exposed in configuration.
- Verify access controls are correctly configured.

## Operations Phase

- Monitor security events.
- Apply security patches promptly.
- Conduct regular security reviews.
- Perform incident response drills.

# Common Vulnerabilities

## SQL Injection

Occurs when untrusted input is concatenated into SQL queries.

Prevention:

- Use parameterized queries (ActiveRecord, prepared statements).
- Never use raw SQL with string interpolation.
- Use ActiveRecord's query interface.

## Cross-Site Scripting (XSS)

Occurs when untrusted input is rendered in HTML without escaping.

Prevention:

- Rails auto-escapes by default. Do not use `.html_safe` or `raw`
  unless necessary and reviewed.
- Use Content Security Policy headers.

## Cross-Site Request Forgery (CSRF)

Occurs when an attacker tricks a user into performing an action they
did not intend.

Prevention:

- Rails includes CSRF protection by default. Do not disable it.
- Use SameSite cookies.

## Insecure Direct Object Reference (IDOR)

Occurs when an attacker can access a resource by guessing or
manipulating an identifier.

Prevention:

- Always authorize access to resources.
- Use random, unguessable identifiers where appropriate.
- Never rely on identifier obscurity alone.

## Security Misconfiguration

Occurs when default configurations are insecure.

Prevention:

- Disable unnecessary services and features.
- Use secure defaults.
- Regularly audit configuration.

# Security Standards

## Password Storage

- Use bcrypt with cost factor >= 12.
- Never store passwords in plain text.
- Never log passwords or password hashes.

## Encryption

- Encrypt data in transit using TLS 1.2+.
- Encrypt sensitive data at rest.
- Use strong, modern encryption algorithms.
- Store encryption keys separately from encrypted data.

## Authentication

- Enforce strong password policies (minimum length, complexity).
- Implement account lockout after repeated failures.
- Use multi-factor authentication for privileged access.
- Use secure session management.

## Logging

- Log authentication successes and failures.
- Log authorization failures.
- Log privileged operations.
- Never log sensitive data (passwords, tokens, PII).
- Use structured logging for security events.

# AI Integration

AI assistants can support security engineering through:

- Threat modeling assistance (identifying potential threats).
- Code review for security vulnerabilities.
- Generating security test cases.
- Reviewing security configuration.
- Analysing security logs and incident data.

AI limitations in security:

- AI may not understand organizational security context.
- AI-generated security recommendations must be reviewed by a security
  engineer.
- AI cannot replace human security review for critical systems.

When using AI for security work, provide:

- System architecture and context.
- Security requirements and compliance obligations.
- Existing security controls and policies.
- Specific security concerns or threat models.

# Capability Map

This handbook is the entry point for the Security Engineering
capability. The following documents form the complete capability:

## Handbooks

- [Security Engineering Handbook](./README.md) — This document. Principles,
  threat modeling, secure development lifecycle and standards.

## Glossaries

- [Security Glossary](../../glossary/security/README.md) — Canonical security terminology (CSRF,
  defense in depth, SAST, STRIDE, XSS, etc.).

## Guides

- [Secure Coding Practices](../../guides/security/secure-coding.md) — Input validation, authentication,
  authorization, output encoding, error handling, cryptography.
- [Web Application Vulnerabilities](../../guides/security/web-vulnerabilities.md) — OWASP Top 10 (2021)
  with explanations and mitigations for each category.
- [Dependency Security](../../guides/security/dependency-security.md) — Vulnerability scanning, dependency
  selection, vulnerability response, license compliance.

## Playbooks

- [Security Review Playbook](../../playbooks/security-review/README.md) — Security review workflow with
  scoping, threat modeling (STRIDE) and remediation.

## Checklists

- [Security Review Checklist](../../checklists/security-review.md) — General security verification
  for any project.
- [Rails Security Review Checklist](../../checklists/rails/security-review.md) — Rails-specific security
  verification.

## Learning Paths

- [Security Learning Paths](../../learning-paths/security/README.md) — Beginner, intermediate and
  advanced tracks for security engineering.

## References

- [Security References](../../references/security/README.md) — Quick lookup: OWASP Top 10, STRIDE,
  tools, response timeline, security headers.

## AI Workflows

- [AI Workflows for Security](../../prompts/security-ai-workflows.md) — Prompt patterns for
  vulnerability identification, threat modeling, configuration
  review and incident analysis.

# Related Documents

- [Security Glossary](../../glossary/security/README.md)
- [Security Review Playbook](../../playbooks/security-review/README.md)
- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
- [Software Architecture Handbook](../../handbooks/architecture/README.md)
- [Rails Security Review Checklist](../../checklists/rails/security-review.md)
