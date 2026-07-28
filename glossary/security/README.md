# Purpose

This glossary defines security terminology used throughout the
Engineering Knowledge Framework.

Security terms defined here are authoritative across the repository.
Foundational engineering terms are defined in the
[Engineering Glossary](../engineering/README.md).

# Glossary

## CSRF (Cross-Site Request Forgery) {#csrf}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | An attack that tricks a user into performing an action |
| --- | --- |
|  | they did not intend on a web application where they are |
|  | authenticated. |
| Context | Rails includes CSRF protection by default via |
|  | `protect_from_forgery with: :exception`. Do not disable |
|  | it. |
| Related | [XSS](#xss), [SQL Injection](#sql-injection) |
| References | [Security Engineering Handbook](../../handbooks/security/README.md) |

## Defense in Depth {#defense-in-depth}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | A security strategy that uses multiple independent |
| --- | --- |
|  | layers of defense so that if one layer fails, another |
|  | provides protection. |
| Context | No single security control is sufficient. Defense in |
|  | depth combines network, application, data and |
|  | operational security controls. |
| Related | [Least Privilege](#least-privilege), [Secure by Default](#secure-by-default) |
| References | [Security Engineering Handbook](../../handbooks/security/README.md) |

## IDOR (Insecure Direct Object Reference) {#idor}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | A vulnerability that occurs when an attacker can access |
| --- | --- |
|  | or modify a resource by manipulating an identifier |
|  | (e.g., changing a user ID in a URL parameter). |
| Context | Prevention requires authorization checks on every |
|  | resource access, not relying on identifier obscurity. |
| Related | [SQL Injection](#sql-injection), [XSS](#xss) |
| References | [Security Engineering Handbook](../../handbooks/security/README.md) |

## Least Privilege {#least-privilege}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | The principle that every user, process and system should |
| --- | --- |
|  | have only the minimum permissions necessary to perform |
|  | its function. |
| Context | Apply least privilege at every level: database accounts, |
|  | service accounts, user permissions and network access. |
| Related | [Defense in Depth](#defense-in-depth), [Secure by Default](#secure-by-default) |
| References | [Security Engineering Handbook](../../handbooks/security/README.md) |

## SAST (Static Application Security Testing) {#sast}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | Security testing that analyses source code for |
| --- | --- |
|  | vulnerabilities without executing the application. |
| Context | SAST tools (e.g., Brakeman) scan code for patterns |
|  | known to be insecure. They are fast and can be run in |
|  | CI, but may produce false positives. |
| Related | [Threat Modeling](#threat-modeling) |
| References | [Security Engineering Handbook](../../handbooks/security/README.md) |

## Secure by Default {#secure-by-default}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | The principle that systems should be secure in their |
| --- | --- |
|  | default configuration, requiring explicit action to |
|  | reduce security. |
| Context | Engineers should explicitly opt into reduced security, |
|  | not opt into increased security. Defaults should be |
|  | restrictive. |
| Related | [Defense in Depth](#defense-in-depth), [Least Privilege](#least-privilege) |
| References | [Security Engineering Handbook](../../handbooks/security/README.md) |

## SQL Injection {#sql-injection}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | A vulnerability that occurs when untrusted input is |
| --- | --- |
|  | concatenated into SQL queries, allowing an attacker to |
|  | execute arbitrary SQL commands. |
| Context | Prevention: use parameterized queries, prepared |
|  | statements or an ORM like ActiveRecord. Never use raw |
|  | SQL with string interpolation from user input. |
| Related | [XSS](#xss), [IDOR](#idor) |
| References | [Security Engineering Handbook](../../handbooks/security/README.md) |

## Threat Modeling {#threat-modeling}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | The practice of identifying potential threats to a |
| --- | --- |
|  | system and designing mitigations before they are |
|  | exploited. |
| Context | Threat modeling should be performed during the design |
|  | phase of new systems or significant changes. The STRIDE |
|  | framework provides a structured approach. |
| Related | [SAST](#sast), [Defense in Depth](#defense-in-depth) |
| References | [Security Engineering Handbook](../../handbooks/security/README.md) |

## XSS (Cross-Site Scripting) {#xss}

| Property | Value |
| --- | --- |
|-------------+----------------------------------------------------------|
| Definition | A vulnerability that occurs when untrusted input is |
| --- | --- |
|  | rendered in HTML without proper escaping, allowing an |
|  | attacker to inject malicious scripts. |
| Context | Rails auto-escapes in views by default. Avoid using |
|  | `.html_safe` or `raw` unless necessary and reviewed. |
|  | Content Security Policy provides additional protection. |
| Related | [CSRF](#csrf), [SQL Injection](#sql-injection) |
| References | [Security Engineering Handbook](../../handbooks/security/README.md) |

# Related Documents

- [Security Engineering Handbook](../../handbooks/security/README.md)
- [Engineering Glossary](../engineering/README.md)
- [Security Review Playbook](../../playbooks/security-review/README.md)
- [Glossary Overview](../README.md)
