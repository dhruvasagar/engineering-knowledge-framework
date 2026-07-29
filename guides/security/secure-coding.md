---
title: "Secure Coding Practices"
description: "Secure coding is the practice of writing code that is resilient to attack."
type: guide
capability: security
status: published
tags: [secure, coding]
last_reviewed: 2026-07-28
---

# Purpose

Secure coding is the practice of writing code that is resilient to
attack.

This guide covers the fundamental practices every engineer should
follow to prevent common vulnerabilities.

# Input Validation

## Validate All Input

All external input is potentially malicious. Validate it before use.

Sources of external input:

- HTTP request parameters and headers.
- API request bodies.
- File uploads.
- User-supplied URLs.
- Data from external systems or APIs.

## Whitelist over Blacklist

Prefer whitelisting (accept known good values) over blacklisting
(reject known bad values).

Blacklists are always incomplete.

```text
# Good: whitelist
ALLOWED_ROLES = %w[admin editor viewer].freeze
raise "Invalid role" unless ALLOWED_ROLES.include?(params[:role])

# Bad: blacklist (misses edge cases)
raise "Invalid role" if params[:role].include?("admin")
```

## Validate Type, Length and Format

- Type: Ensure the input is the expected data type.
- Length: Enforce minimum and maximum lengths.
- Format: Use regular expressions or validators for structured data
  (email, phone, postal code).

# Authentication

## Password Handling

- Hash passwords with bcrypt (cost >= 12).
- Never store or transmit passwords in plain text.
- Never log passwords or password hashes.
- Enforce minimum password length (12+ characters).

## Session Management

- Use secure, HTTP-only cookies.
- Regenerate session IDs after login.
- Implement session timeout.
- Invalidate sessions on logout.

## Multi-Factor Authentication

Require MFA for:

- Administrative access.
- Access to sensitive data.
- Privileged operations (password change, API key generation).

# Authorization

## Check Authorization on Every Request

Authorization should be checked on every request, not just on the
login page.

```ruby
def show
  record = Record.find(params[:id])
  authorize record  # Check permission
  render json: record
end
```

## Use Centralized Authorization

Prefer a centralized authorization framework (Pundit, CanCanCan) over
dispersed conditionals.

## Deny by Default

If authorization is not explicitly granted, it should be denied.

# Output Encoding

## Context-Appropriate Encoding

Encode output according to the context where it will be used:

| Context        | Encoding               |
|----------------|------------------------|
| HTML body      | HTML entity encode.    |
| HTML attribute | HTML attribute encode. |
| JavaScript     | JavaScript escape.     |
| URL            | URL encoding.          |
| SQL            | Parameterized queries. |

Frameworks like Rails handle most output encoding automatically. Be
careful when bypassing it with `.html_safe` or `raw`.

# Error Handling

## Don't Leak Sensitive Information

Error messages should not reveal:

- Internal implementation details.
- Stack traces.
- Database structure.
- File paths.

```text
# Bad
render json: { error: "SQL error: column 'ssn' not found" }

# Good
render json: { error: "An unexpected error occurred" }
```

## Log Security Events

Log the following security events:

- Authentication successes and failures.
- Authorization failures.
- Input validation failures.
- Privileged operations.
- Data access to sensitive information.

# Cryptography

## Use Standard Libraries

Never implement custom cryptography. Use standard, well-reviewed
libraries.

## Encryption in Transit

- Use TLS 1.2 or higher.
- Disable weak cipher suites.
- Use valid certificates from trusted CAs.

## Encryption at Rest

- Encrypt sensitive data at rest.
- Use strong, modern algorithms (AES-256-GCM).
- Store encryption keys separately from encrypted data.

# Related Documents

- [Security Engineering Handbook](../../handbooks/security/README.md)
- [Security Glossary](../../glossary/security/README.md)
- [Security Review Playbook](../../playbooks/security-review/README.md)
- [Rails Engineering Handbook](../../handbooks/rails/README.md)
