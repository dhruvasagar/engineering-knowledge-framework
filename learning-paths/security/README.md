---
title: "Security Learning Paths"
description: "Structured learning progression for security engineering"
---


# Purpose

These learning paths provide a structured progression through security
engineering, from understanding basic threats to designing secure
architectures.

# Beginner Path

## Objective

Understand common threats, follow secure coding practices and
participate in security reviews.

## Prerequisites

- Basic understanding of web applications and networking.

## Topics

1. ***Security Principles***
   - Defense in depth, least privilege, secure by default.
   - Reference: [Security Engineering Handbook](../../handbooks/security/README/)

2. ***Common Web Vulnerabilities***
   - OWASP Top 10 overview.
   - SQL injection, XSS, CSRF, IDOR.
   - Reference: [Web Vulnerabilities Guide](../../guides/security/web-vulnerabilities/)

3. ***Secure Coding Practices***
   - Input validation, authentication, output encoding.
   - Reference: [Secure Coding Guide](../../guides/security/secure-coding/)

4. ***Using Security Tools***
   - Running SAST scanners (Brakeman, RuboCop).
   - Running dependency scanners (bundler-audit).
   - Reference: [Dependency Security Guide](../../guides/security/dependency-security/)

5. ***Participating in Security Reviews***
   - What to look for as a reviewer.
   - Basic threat identification.
   - Reference: [Security Review Playbook](../../playbooks/security-review/README/)

## Assessment

Demonstrate by: Identifying vulnerabilities in a code review.
Running security tools and interpreting results correctly.

# Intermediate Path

## Objective

Conduct security reviews, perform threat modeling and implement
security controls.

## Prerequisites

- Completed Beginner Path or equivalent experience.

## Topics

1. ***Threat Modeling***
   - STRIDE framework.
   - Identifying trust boundaries.
   - Reference: [Security Engineering Handbook](../../handbooks/security/README/)

2. ***Authentication and Authorization***
   - Implementing secure authentication.
   - Role-based and attribute-based access control.
   - Reference: [Authentication and Authorization Guide](../../guides/rails/authentication-authorization/)

3. ***Security Testing***
   - SAST, DAST, and manual testing.
   - Writing security test cases.
   - Reference: [Security Review Playbook](../../playbooks/security-review/README/)

4. ***Dependency Management***
   - Vulnerability response workflow.
   - Dependency evaluation and selection.
   - Reference: [Dependency Security Guide](../../guides/security/dependency-security/)

5. ***Security Configuration***
   - Security headers (CSP, HSTS).
   - Secure deployment configuration.
   - Reference: [Security Engineering Handbook](../../handbooks/security/README/)

## Assessment

Demonstrate by: Leading a security review. Performing threat modeling
for a new feature. Implementing security controls in an application.

# Advanced Path

## Objective

Design secure architectures, establish security standards and
respond to security incidents.

## Prerequisites

- Completed Intermediate Path or equivalent experience.

## Topics

1. ***Secure Architecture Design***
   - Architecture-level threat modeling.
   - Zero trust architecture.
   - Security patterns and anti-patterns.

2. ***Incident Response***
   - Detection, containment, eradication, recovery.
   - Post-incident analysis.
   - Reference: Incident Response Playbook (not yet developed)

3. ***Security Standards and Compliance***
   - Defining security standards for an organization.
   - Compliance frameworks (SOC 2, ISO 27001).
   - Security audit preparation.

4. ***Cryptography***
   - Applied cryptography for engineers.
   - Key management.
   - TLS and certificate management.

5. ***Security Mentoring***
   - Conducting security training.
   - Reviewing for security mindset, not just vulnerabilities.

## Assessment

Demonstrate by: Designing a secure system architecture. Establishing
security standards for a team. Mentoring others in security practices.

# Related Documents

- [Security Engineering Handbook](../../handbooks/security/README/)
- [Security Glossary](../../glossary/security/README/)
- [Security Review Playbook](../../playbooks/security-review/README/)
- [Secure Coding Guide](../../guides/security/secure-coding/)
- [Web Vulnerabilities Guide](../../guides/security/web-vulnerabilities/)
- [Dependency Security Guide](../../guides/security/dependency-security/)
