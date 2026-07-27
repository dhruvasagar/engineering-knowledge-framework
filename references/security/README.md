+++
title = "Security References"
description = "Quick-reference material for security engineering"
+++


# Purpose

Quick-reference material for security engineering.

# OWASP Top 10 (2021)

| Rank | Category |
| --- | --- |
|------+-------------------------------------------|
| A01 | Broken Access Control |
| --- | --- |
|------+-------------------------------------------|
| A02 | Cryptographic Failures |
| --- | --- |
|------+-------------------------------------------|
| A03 | Injection |
| --- | --- |
|------+-------------------------------------------|
| A04 | Insecure Design |
| --- | --- |
|------+-------------------------------------------|
| A05 | Security Misconfiguration |
| --- | --- |
|------+-------------------------------------------|
| A06 | Vulnerable and Outdated Components |
| --- | --- |
|------+-------------------------------------------|
| A07 | Identification and Authentication Failures |
| --- | --- |
|------+-------------------------------------------|
| A08 | Software and Data Integrity Failures |
| --- | --- |
|------+-------------------------------------------|
| A09 | Security Logging and Monitoring Failures |
| --- | --- |
|------+-------------------------------------------|
| A10 | Server-Side Request Forgery (SSRF) |
| --- | --- |
|------+-------------------------------------------|

# STRIDE Threat Model

| Threat | Definition | Example |
| --- | --- | --- |
|--------------------+-----------------------------------------------+----------------------------|
| Spoofing | Impersonating another user or system. | Session hijacking. |
| --- | --- | --- |
|--------------------+-----------------------------------------------+----------------------------|
| Tampering | Unauthorized modification of data or code. | Modifying request params. |
| --- | --- | --- |
|--------------------+-----------------------------------------------+----------------------------|
| Repudiation | Denying an action was performed. | User denies transaction. |
| --- | --- | --- |
|--------------------+-----------------------------------------------+----------------------------|
| Information | Exposing information to unauthorized parties. | Data leak via API. |
| --- | --- | --- |
| Disclosure |  |  |
|--------------------+-----------------------------------------------+----------------------------|
| Denial of Service | Making the system unavailable. | Flooding an endpoint. |
| --- | --- | --- |
|--------------------+-----------------------------------------------+----------------------------|
| Elevation of | Gaining unauthorized higher permissions. | Privilege escalation. |
| --- | --- | --- |
| Privilege |  |  |
|--------------------+-----------------------------------------------+----------------------------|

# Security Tools Quick Reference

| Tool | Type | Purpose | Run |
| --- | --- | --- | --- |
|-------------------+---------+---------------------------------------+-------------------------------|
| Brakeman | SAST | Rails static security analysis | `brakeman -q --no-pager` |
| --- | --- | --- | --- |
|-------------------+---------+---------------------------------------+-------------------------------|
| bundler-audit | SCA | Ruby dependency vulnerabilities | `bundler-audit check --update` |
| --- | --- | --- | --- |
|-------------------+---------+---------------------------------------+-------------------------------|
| Trivy | SCA | Container and filesystem scanning | =trivy fs . = |
| --- | --- | --- | --- |
|-------------------+---------+---------------------------------------+-------------------------------|
| OWASP ZAP | DAST | Dynamic web application scanning | `zap.sh -cmd -quickurl` |
| --- | --- | --- | --- |
|-------------------+---------+---------------------------------------+-------------------------------|
| git-secrets | Secrets | Prevent committing secrets | `git secrets --scan` |
| --- | --- | --- | --- |
|-------------------+---------+---------------------------------------+-------------------------------|
| truffleHog | Secrets | Scan git history for secrets | =trufflehog git file://. = |
| --- | --- | --- | --- |
|-------------------+---------+---------------------------------------+-------------------------------|

# Security Response Timeline

| Severity | Response Time | Examples |
| --- | --- | --- |
|----------+---------------+---------------------------------------------|
| Critical | Within 24 hrs | Remote code execution, auth bypass, data |
| --- | --- | --- |
|  |  | breach. |
|----------+---------------+---------------------------------------------|
| High | Within 1 week | Significant data exposure, privilege |
| --- | --- | --- |
|  |  | escalation. |
|----------+---------------+---------------------------------------------|
| Medium | Within 1 month | Limited info disclosure. |
| --- | --- | --- |
|----------+---------------+---------------------------------------------|
| Low | Next release | Minimal risk, difficult to exploit. |
| --- | --- | --- |
|----------+---------------+---------------------------------------------|

# Security Headers

| Header | Purpose | Value Example |
| --- | --- | --- |
|----------------------------+------------------------------------+--------------------------------|
| Content-Security-Policy | Controls resources the browser | `default-src 'self'` |
| --- | --- | --- |
|  | is allowed to load. |  |
|----------------------------+------------------------------------+--------------------------------|
| Strict-Transport-Security | Enforces HTTPS connections. | `max-age`31536000= |
| --- | --- | --- |
|----------------------------+------------------------------------+--------------------------------|
| X-Frame-Options | Prevents clickjacking. | `DENY` |
| --- | --- | --- |
|----------------------------+------------------------------------+--------------------------------|
| X-Content-Type-Options | Prevents MIME type sniffing. | `nosniff` |
| --- | --- | --- |
|----------------------------+------------------------------------+--------------------------------|

# Related Documents

- [Security Engineering Handbook](../../handbooks/security/README/)
- [Security Glossary](../../glossary/security/README/)
- [Security Review Playbook](../../playbooks/security-review/README/)
- [Web Vulnerabilities Guide](../../guides/security/web-vulnerabilities/)
