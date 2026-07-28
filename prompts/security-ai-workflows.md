---
title: "AI Workflows for Security"
description: "Prompt patterns and AI workflows for security engineering"
---


# Purpose

AI assistants can support security engineering through code analysis,
threat identification, configuration review and incident response.

# Workflows

## Vulnerability Identification

### Prompt Pattern

```
Review this code for security vulnerabilities:

```[language]
[paste code]
```

Focus on:
1. SQL injection.
2. Cross-site scripting (XSS).
3. Insecure direct object references.
4. Authentication and authorization gaps.
5. Sensitive data exposure.

For each finding, describe:
- The vulnerability.
- How it could be exploited.
- How to fix it.
```

## Threat Modeling Assistance

### Prompt Pattern

```
Help me threat model this system using STRIDE:

***System Description***
[describe the system, architecture, data flows]

***Trust Boundaries***
[describe where trust boundaries exist]

For each STRIDE category:
1. Identify potential threats.
2. Rate the likelihood and impact.
3. Suggest mitigations.
```

## Security Configuration Review

### Prompt Pattern

```
Review this security configuration for best practices:

```[config language]
[paste configuration]
```

Check for:
1. Missing security headers.
2. Weak cipher configurations.
3. Permissive access controls.
4. Debug or development settings enabled.
5. Exposed secrets or credentials.

Suggest fixes for any issues found.
```

## Incident Analysis

### Prompt Pattern

```
Help me analyze this security incident:

***Timeline***
[describe the sequence of events]

***Logs***
[paste relevant logs]

***System Context***
[describe affected system]

Questions:
1. What is the most likely root cause?
2. What is the blast radius?
3. What immediate containment steps are needed?
4. What long-term remediation is recommended?
```

# Related Documents

- [Security Engineering Handbook](../handbooks/security/README/)
- [Security Review Playbook](../playbooks/security-review/README/)
- [Secure Coding Guide](../guides/security/secure-coding/)
- [AI Workflows for Engineering](../prompts/engineering-ai-workflows/)
