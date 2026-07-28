# Purpose

Modern applications depend on hundreds of third-party packages.

Each dependency introduces potential security risks: known
vulnerabilities, malicious code, license compliance issues and
maintenance abandonment.

This guide covers the practices for managing dependency security
throughout the application lifecycle.

# Vulnerability Scanning

## Automated Scanning

Every project MUST scan dependencies for known vulnerabilities.

| Ecosystem | Tool | CI Integration |
| --- | --- | --- |
|-----------+-----------------------+-----------------------------------|
| Ruby | bundler-audit | `bundle exec bundler-audit check --update` |
| --- | --- | --- |
|-----------+-----------------------+-----------------------------------|
| JavaScript | npm audit / yarn audit | `npm audit --audit-level`high= |
| --- | --- | --- |
|-----------+-----------------------+-----------------------------------|
| Python | pip-audit | `pip-audit` |
| --- | --- | --- |
|-----------+-----------------------+-----------------------------------|
| Docker | Trivy / Grype | `trivy image myapp:latest` |
| --- | --- | --- |
|-----------+-----------------------+-----------------------------------|

## Continuous Monitoring

Use a service that monitors dependencies continuously:

- GitHub Dependabot.
- GitLab Dependency Scan.
- Snyk.
- Gemnasium.

These services automatically create pull requests when vulnerabilities
are detected.

# Dependency Selection

## Evaluation Criteria

Before adding a new dependency, evaluate:

| Criterion | Questions |
| --- | --- |
|---------------------+----------------------------------------------------|
| Necessity | Can we solve this without a dependency? |
| --- | --- |
|---------------------+----------------------------------------------------|
| Maintenance | When was the last release? Is it actively |
| --- | --- |
|  | maintained? |
|---------------------+----------------------------------------------------|
| Security track | Are there historical vulnerabilities? How quickly |
| --- | --- |
| record | are they addressed? |
|---------------------+----------------------------------------------------|
| Community | How many users? Is there a community around it? |
| --- | --- |
|---------------------+----------------------------------------------------|
| License | Is the license compatible with our project? |
| --- | --- |
|---------------------+----------------------------------------------------|
| Size and complexity | Is it a small focused library or a large framework? |
| --- | --- |
|---------------------+----------------------------------------------------|

## Minimum Dependency Principle

Prefer standard library or framework built-in features over external
dependencies.

For each dependency in the project, periodically ask: is this still
needed?

# Vulnerability Response

## Severity Classification

| Severity | Definition | Response Time |
| --- | --- | --- |
|----------+-----------------------------------------------+--------------------|
| Critical | Remote code execution, authentication bypass, | Within 24 hours |
| --- | --- | --- |
|  | data breach. |  |
|----------+-----------------------------------------------+--------------------|
| High | Significant data exposure, privilege | Within 1 week |
| --- | --- | --- |
|  | escalation. |  |
|----------+-----------------------------------------------+--------------------|
| Medium | Limited information disclosure, | Within 1 month |
| --- | --- | --- |
|  | minor privilege escalation. |  |
|----------+-----------------------------------------------+--------------------|
| Low | Minimal risk, difficult to exploit. | Next release. |
| --- | --- | --- |
|----------+-----------------------------------------------+--------------------|

## Response Workflow

1. Verify the vulnerability affects our usage.
2. Determine if a patched version is available.
3. Update the dependency.
4. Run tests to verify compatibility.
5. Deploy the fix.

If no patch is available:

- Assess the risk for your specific usage.
- Implement mitigating controls (WAF rules, network restrictions).
- Consider removing or replacing the dependency.

# License Compliance

## Approved Licenses

Maintain a list of approved licenses:

- MIT, Apache 2.0, BSD, ISC (permissive).
- LGPL (copyleft with exceptions).
- Ruby License, Python Software Foundation License.

## Restricted Licenses

Restricted licenses require legal review:

- GPL (strong copyleft).
- AGPL (network copyleft).
- Proprietary or commercial licenses.

## Tooling

Use `license_finder` or similar tools to enforce license policies in
CI.

# Dependency Hygiene

## Regular Audits

- Run a full dependency audit monthly.
- Audit for unused dependencies (`bundle doctor`, `depcheck`).
- Audit for outdated dependencies (`bundle outdated`, `npm outdated`).

## Removing Dependencies

When removing a dependency:

- Verify no code references the dependency.
- Remove it from the package manifest.
- Run full test suite.
- Remove any configuration or initialization code.

# Related Documents

- [Security Engineering Handbook](../../handbooks/security/README.md)
- [Security Review Playbook](../../playbooks/security-review/README.md)
- [Rails Project Standards](../../guides/rails/project-standards.md)
- [Rails Security Review Checklist](../../checklists/rails/security-review.md)
