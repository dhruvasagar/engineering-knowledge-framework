---
title: "Table of Contents"
description: "Complete inventory of framework documents, organized by capability and by cross-cutting topic."
type: governance
capability: governance
status: published
tags: [toc]
last_reviewed: 2026-07-28
---

# How to Use This TOC

This document provides two complementary views of the repository:

- ***From Top to Bottom***: Complete inventory organized by capability
  and document type — for when you know which capability you need.
- ***Cross-Cutting Topics***: Topic-based indexes that gather documents
  across capabilities — for when you know what you need but not
  where it lives.



## Directory Indexes

Index documents for capability directories (references overviews of each directory's contents).

| Document                                                               | Description                                   |
|------------------------------------------------------------------------|-----------------------------------------------|
| [Checklists Index](./checklists/README.md)                             | Overview of checklist directories.            |
| [Accessibility Checklists Index](./checklists/accessibility/README.md) | Overview of accessibility checklists.         |
| [Quality Checklists Index](./checklists/quality/README.md)             | Overview of quality checklists.               |
| [Rails Checklists Index](./checklists/rails/README.md)                 | Overview of Rails checklists.                 |
| [Glossary Index](./glossary/README.md)                                 | Glossary organization and writing guidelines. |
| [Accessibility Guides Index](./guides/accessibility/README.md)         | Overview of accessibility guides.             |
| [Architecture Guides Index](./guides/architecture/README.md)           | Overview of architecture guides.              |
| [Engineering Guides Index](./guides/engineering/README.md)             | Overview of engineering guides.               |
| [Rails Guides Index](./guides/rails/README.md)                         | Overview of Rails guides.                     |
| [Security Guides Index](./guides/security/README.md)                   | Overview of security guides.                  |
| [AI Playbooks Index](./playbooks/ai/README.md)                         | Overview of AI playbooks.                     |
| [Code Review Playbook](./playbooks/code-review/README.md)              | Code review workflow.                         |
| [Quality Playbooks Index](./playbooks/quality/README.md)               | Overview of quality playbooks.                |
| [Rails Playbooks Index](./playbooks/rails/README.md)                   | Overview of Rails playbooks.                  |
| [AI Workflows Index](./prompts/README.md)                              | Index of all AI workflow documents.           |
| [Accessibility Templates Index](./templates/accessibility/README.md)   | Overview of accessibility templates.          |
| [AI Templates Index](./templates/ai/README.md)                         | Overview of AI templates.                     |
| [Quality Templates Index](./templates/quality/README.md)               | Overview of quality templates.                |
| [Rails Templates Index](./templates/rails/README.md)                   | Overview of Rails templates.                  |
| [Security Templates Index](./templates/security/README.md)             | Overview of security templates.               |


# From Top to Bottom

## Governance

The foundational documents that define the framework itself.

| Document                                      | Description                                            |
|-----------------------------------------------|--------------------------------------------------------|
| [CLAUDE.md](./CLAUDE.md)                      | AI-specific project instructions for coding agents.    |
| [README.md](./README.md)                      | Repository overview, mission, vision and philosophy.   |
| [Strategy](./strategy.md)                     | Long-term vision and guiding strategy.                 |
| [Roadmap](./roadmap.md)                       | Strategic roadmap and phase progression.               |
| [Architecture](./architecture.md)             | Repository architecture and knowledge organization.    |
| [Document Types](./document-types.md)         | Canonical document taxonomy.                           |
| [Style Guide](./style-guide.md)               | Writing, formatting and documentation standards.       |
| [Writing Principles](./writing-principles.md) | Philosophy behind effective engineering documentation. |
| [Contributing](./contributing.md)             | Contribution guidelines and workflows.                 |
| [Changelog](./changelog.md)                   | Version history of the framework.                      |
| [toc.md](./toc.md)                            | This document — table of contents and indexes.         |

## Engineering Fundamentals

### Handbooks

| Document                                                               | Description                                               |
|------------------------------------------------------------------------|-----------------------------------------------------------|
| [Engineering Fundamentals Handbook](./handbooks/engineering/README.md) | Core principles, quality philosophy, decision frameworks. |

### Glossaries

| Document                                                 | Description                                                       |
|----------------------------------------------------------|-------------------------------------------------------------------|
| [Engineering Glossary](./glossary/engineering/README.md) | Foundational terminology (abstraction, coupling, cohesion, etc.). |

### Guides

| Document                                                         | Description                                                    |
|------------------------------------------------------------------|----------------------------------------------------------------|
| [Code Organization](./guides/engineering/code-organization.md)   | Feature-based packaging, module boundaries, anti-patterns.     |
| [Error Handling](./guides/engineering/error-handling.md)         | Recoverable vs unrecoverable errors, patterns, logging.        |
| [Testing Strategies](./guides/engineering/testing-strategies.md) | Test pyramid, what to test, test doubles, anti-patterns.       |
| [Logging](./guides/engineering/logging.md)                       | Structured logging, log levels, context fields, anti-patterns. |

### Learning Paths

| Document                                                             | Description                            |
|----------------------------------------------------------------------|----------------------------------------|
| [Engineering Learning Paths](./learning-paths/engineering/README.md) | Beginner/intermediate/advanced tracks. |

### References

| Document                                                     | Description                                           |
|--------------------------------------------------------------|-------------------------------------------------------|
| [Engineering References](./references/engineering/README.md) | Quick lookup: principles, patterns, testing, logging. |

### AI Workflows

| Document                                                              | Description                                              |
|-----------------------------------------------------------------------|----------------------------------------------------------|
| [AI Workflows for Engineering](./prompts/engineering-ai-workflows.md) | Prompt patterns for code review, refactoring, diagnosis. |

## Software Architecture

### Handbooks

| Document                                                             | Description                                      |
|----------------------------------------------------------------------|--------------------------------------------------|
| [Software Architecture Handbook](./handbooks/architecture/README.md) | Principles, patterns, decision frameworks, ADRs. |

### Glossaries

| Document                                                   | Description                                        |
|------------------------------------------------------------|----------------------------------------------------|
| [Architecture Glossary](./glossary/architecture/README.md) | Terminology (ADR, C4, DDD, hexagonal, trade-offs). |

### Guides

| Document                                                                  | Description                                               |
|---------------------------------------------------------------------------|-----------------------------------------------------------|
| [ADR Writing Guide](./guides/architecture/adr-writing-guide.md)           | When and how to write Architecture Decision Records.      |
| [Architectural Patterns](./guides/architecture/architectural-patterns.md) | Pattern catalogue with trade-offs and selection guidance. |
| [API Design](./guides/architecture/api-design.md)                         | RESTful conventions, versioning, error formats.           |
| [System Modeling](./guides/architecture/system-modeling.md)               | C4 model levels, event modeling techniques.               |

### Playbooks

| Document                                                                  | Description                                          |
|---------------------------------------------------------------------------|------------------------------------------------------|
| [Architecture Review Playbook](./playbooks/architecture-review/README.md) | Review workflow, team assembly, evaluation criteria. |

### Checklists

| Document                                                             | Description                                            |
|----------------------------------------------------------------------|--------------------------------------------------------|
| [Architecture Review Checklist](./checklists/architecture-review.md) | Pre, during and post-review verification.              |
| [Design Decision Checklist](./checklists/design-decision.md)         | Before, during and after design decision verification. |

### Templates

| Document                                  | Description                                        |
|-------------------------------------------|----------------------------------------------------|
| [ADR Template](./templates/adr/README.md) | Standard format for Architecture Decision Records. |
| [RFC Template](./templates/rfc/README.md) | Format for major architectural proposals.          |

### Learning Paths

| Document                                                               | Description                            |
|------------------------------------------------------------------------|----------------------------------------|
| [Architecture Learning Paths](./learning-paths/architecture/README.md) | Beginner/intermediate/advanced tracks. |

### References

| Document                                                       | Description                                       |
|----------------------------------------------------------------|---------------------------------------------------|
| [Architecture References](./references/architecture/README.md) | Quick lookup: C4, pattern comparison, HTTP codes. |

### AI Workflows

| Document                                                                | Description                                           |
|-------------------------------------------------------------------------|-------------------------------------------------------|
| [AI Workflows for Architecture](./prompts/architecture-ai-workflows.md) | Prompt patterns for trade-off analysis, ADR drafting. |

## Rails Engineering

### Handbooks

| Document                                                  | Description                                           |
|-----------------------------------------------------------|-------------------------------------------------------|
| [Rails Engineering Handbook](./handbooks/rails/README.md) | Principles, standards, patterns, decision frameworks. |

### Glossaries

| Document                                     | Description                                                   |
|----------------------------------------------|---------------------------------------------------------------|
| [Rails Glossary](./glossary/rails/README.md) | Terminology (ActiveRecord, controller, service object, etc.). |

### Guides

| Document                                                                           | Description                                                  |
|------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [Service Objects](./guides/rails/service-objects.md)                               | When and how to use service objects, patterns, testing.      |
| [Testing Rails Applications](./guides/rails/testing.md)                            | Test distribution, model/request/system specs.               |
| [Rails Audit Guide](./guides/rails/audit-guide.md)                                 | Systematic code quality, performance and security auditing.  |
| [Rails Project Standards](./guides/rails/project-standards.md)                     | Mandatory tooling and CI/CD baseline for every project.      |
| [ActiveRecord Patterns](./guides/rails/active-record.md)                           | Scopes, query optimization, N+1 prevention, indexing.        |
| [API Development with Rails](./guides/rails/api-development.md)                    | API-only setup, serialization, versioning, auth.             |
| [Background Jobs](./guides/rails/background-jobs.md)                               | Framework selection, job design, error handling, monitoring. |
| [Authentication and Authorization](./guides/rails/authentication-authorization.md) | Devise, Pundit, roles, anti-patterns.                        |

### Playbooks

| Document                                                     | Description                                           |
|--------------------------------------------------------------|-------------------------------------------------------|
| [Rails Upgrade Playbook](./playbooks/rails/upgrade.md)       | Step-by-step version upgrade with rollback plan.      |
| [Rails Deployment Playbook](./playbooks/rails/deployment.md) | Safe deployment with migration safety, zero-downtime. |

### Checklists

| Document                                                                 | Description                                             |
|--------------------------------------------------------------------------|---------------------------------------------------------|
| [Rails Pull Request Checklist](./checklists/rails/pull-request.md)       | Code quality, testing, security, migration safety.      |
| [Rails Security Review Checklist](./checklists/rails/security-review.md) | Auth, data protection, dependency, infrastructure.      |
| [Rails Deployment Checklist](./checklists/rails/deployment.md)           | Pre-deploy, migration safety, post-deploy verification. |

### Templates

| Document                                                       | Description                                |
|----------------------------------------------------------------|--------------------------------------------|
| [Service Object Template](./templates/rails/service-object.md) | Reusable pattern with result object.       |
| [Form Object Template](./templates/rails/form-object.md)       | ActiveModel integration for complex forms. |
| [Query Object Template](./templates/rails/query-object.md)     | Composable scope chaining.                 |
| [Policy Object Template](./templates/rails/policy-object.md)   | Authorization with Pundit conventions.     |

### Learning Paths

| Document                                                 | Description                            |
|----------------------------------------------------------|----------------------------------------|
| [Rails Learning Paths](./learning-paths/rails/README.md) | Beginner/intermediate/advanced tracks. |

### References

| Document                                         | Description                                              |
|--------------------------------------------------|----------------------------------------------------------|
| [Rails References](./references/rails/README.md) | Quick lookup: conventions, generators, gems, HTTP codes. |

### AI Workflows

| Document                                                  | Description                                      |
|-----------------------------------------------------------|--------------------------------------------------|
| [AI Workflows for Rails](./prompts/rails-ai-workflows.md) | Prompt patterns for model gen, API dev, testing. |

## Security Engineering

### Handbooks

| Document                                                        | Description                                   |
|-----------------------------------------------------------------|-----------------------------------------------|
| [Security Engineering Handbook](./handbooks/security/README.md) | Principles, threat modeling, SDLC, standards. |

### Glossaries

| Document                                           | Description                                            |
|----------------------------------------------------|--------------------------------------------------------|
| [Security Glossary](./glossary/security/README.md) | Terminology (CSRF, defense in depth, SAST, XSS, etc.). |

### Guides

| Document                                                                    | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [Secure Coding Practices](./guides/security/secure-coding.md)               | Input validation, auth, output encoding, crypto.        |
| [Web Application Vulnerabilities](./guides/security/web-vulnerabilities.md) | OWASP Top 10 with explanations and mitigations.         |
| [Dependency Security](./guides/security/dependency-security.md)             | Vulnerability scanning, selection, response, licensing. |

### Playbooks

| Document                                                          | Description                                           |
|-------------------------------------------------------------------|-------------------------------------------------------|
| [Security Review Playbook](./playbooks/security-review/README.md) | Review workflow, STRIDE threat modeling, remediation. |

### Checklists

| Document                                                                 | Description                                    |
|--------------------------------------------------------------------------|------------------------------------------------|
| [Security Review Checklist](./checklists/security-review.md)             | General security verification for any project. |
| [Rails Security Review Checklist](./checklists/rails/security-review.md) | Rails-specific security verification.          |

### Learning Paths

| Document                                                       | Description                            |
|----------------------------------------------------------------|----------------------------------------|
| [Security Learning Paths](./learning-paths/security/README.md) | Beginner/intermediate/advanced tracks. |

### References

| Document                                               | Description                                         |
|--------------------------------------------------------|-----------------------------------------------------|
| [Security References](./references/security/README.md) | Quick lookup: OWASP Top 10, STRIDE, tools, headers. |

### Templates

| Document                                                                 | Description                                    |
|--------------------------------------------------------------------------|------------------------------------------------|
| [Threat Model Template](./templates/security/threat-model.md)            | Structured threat model document using STRIDE. |
| [Security Review Report](./templates/security/security-review-report.md) | Findings report for security review outcomes.  |

### AI Workflows

| Document                                                        | Description                                            |
|-----------------------------------------------------------------|--------------------------------------------------------|
| [AI Workflows for Security](./prompts/security-ai-workflows.md) | Prompt patterns for vulnerability ID, threat modeling. |

## Engineering Quality

### Handbooks

| Document                                                      | Description                                                |
|---------------------------------------------------------------|------------------------------------------------------------|
| [Engineering Quality Handbook](./handbooks/quality/README.md) | Principles, quality gates, metrics, code review standards. |

### Glossaries

| Document                                                     | Description                                                    |
|--------------------------------------------------------------|----------------------------------------------------------------|
| [Engineering Quality Glossary](./glossary/quality/README.md) | Terminology (change failure rate, MTTR, technical debt, etc.). |

### Guides

| Document                                                                   | Description                                                     |
|----------------------------------------------------------------------------|-----------------------------------------------------------------|
| [Code Review Standards](./guides/quality/code-review-standards.md)         | Standards for review velocity, what to review, severity labels. |
| [Quality Metrics](./guides/quality/quality-metrics.md)                     | Code quality and process metrics, implementation, pitfalls.     |
| [Technical Debt Management](./guides/quality/technical-debt-management.md) | Classification, assessment, management process.                 |

### Playbooks

| Document                                                                   | Description                                        |
|----------------------------------------------------------------------------|----------------------------------------------------|
| [Quality Review Playbook](./playbooks/quality/quality-review.md)           | Systematic quality assessment and reporting.       |
| [Technical Debt Remediation](./playbooks/quality/tech-debt-remediation.md) | Workflow for managing and reducing technical debt. |
| [Release Quality Gate](./playbooks/quality/release-quality-gate.md)        | Quality verification before production release.    |

### Checklists

| Document                                                                 | Description                                          |
|--------------------------------------------------------------------------|------------------------------------------------------|
| [Quality Gate Checklist](./checklists/quality/quality-gate.md)           | Verification before accepting changes.               |
| [Release Readiness Checklist](./checklists/quality/release-readiness.md) | Verification before production release.              |
| [Technical Debt Triage](./checklists/quality/tech-debt-triage.md)        | Classification and prioritisation of technical debt. |

### Templates

| Document                                                               | Description                                 |
|------------------------------------------------------------------------|---------------------------------------------|
| [Quality Report Template](./templates/quality/quality-report.md)       | Standard format for quality review reports. |
| [Technical Debt Register](./templates/quality/tech-debt-register.md)   | Track and monitor technical debt items.     |
| [Quality Dashboard Template](./templates/quality/quality-dashboard.md) | Template for tracking quality metrics.      |

### Learning Paths

| Document                                                                 | Description                            |
|--------------------------------------------------------------------------|----------------------------------------|
| [Engineering Quality Learning Paths](./learning-paths/quality/README.md) | Beginner/intermediate/advanced tracks. |

### References

| Document                                                         | Description                                            |
|------------------------------------------------------------------|--------------------------------------------------------|
| [Engineering Quality References](./references/quality/README.md) | Quick lookup: gates, metrics targets, severity labels. |

### AI Workflows

| Document                                                      | Description                                                 |
|---------------------------------------------------------------|-------------------------------------------------------------|
| [AI Workflows for Quality](./prompts/quality-ai-workflows.md) | Prompt patterns for quality review, debt analysis, testing. |

## AI Engineering

### Handbooks

| Document                                            | Description                                                          |
|-----------------------------------------------------|----------------------------------------------------------------------|
| [AI Engineering Handbook](./handbooks/ai/README.md) | Principles, context engineering, AI workflow patterns, verification. |

### Glossaries

| Document                                           | Description                                                                         |
|----------------------------------------------------|-------------------------------------------------------------------------------------|
| [AI Engineering Glossary](./glossary/ai/README.md) | Terminology (context engineering, hallucination, prompt engineering, verification). |

### Guides

| Document                                                           | Description                                                                         |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [Prompt Engineering](./guides/ai/prompt-engineering.md)            | Principles, patterns (persona, format, constraint, verification) and anti-patterns. |
| [Context Engineering](./guides/ai/context-engineering.md)          | Context categories, templates for code, review and design.                          |
| [AI Safety and Verification](./guides/ai/ai-safety.md)             | Human oversight, high-risk use cases, prohibited uses, verification practices.      |
| [Agentic Workflows](./guides/ai/agentic-workflows.md)              | Multi-step AI-assisted engineering workflow patterns.                               |
| [AI Collaboration Patterns](./guides/ai/collaboration-patterns.md) | How engineers and AI should interact in different contexts.                         |
| [Human Review Strategies](./guides/ai/human-review-strategies.md)  | When and how to review AI output effectively.                                       |
| [AI Evaluation Frameworks](./guides/ai/evaluation-frameworks.md)   | Frameworks for measuring AI output quality and reliability.                         |
| [Knowledge Extraction](./guides/ai/knowledge-extraction.md)        | Using AI to extract and structure engineering knowledge.                            |

### Playbooks

| Document                                                                             | Description                                          |
|--------------------------------------------------------------------------------------|------------------------------------------------------|
| [AI-Assisted Code Review](./playbooks/ai/ai-assisted-code-review.md)                 | Workflow for reviewing code with AI assistance.      |
| [AI-Assisted Architecture Review](./playbooks/ai/ai-assisted-architecture-review.md) | Workflow for architecture review with AI assistance. |
| [AI Pair Programming](./playbooks/ai/ai-pair-programming.md)                         | Workflow for collaborative coding with AI.           |
| [Verification Workflows](./playbooks/ai/verification-workflows.md)                   | Systematic verification of AI-generated output.      |

### Checklists

| Document                                       | Description                                                          |
|------------------------------------------------|----------------------------------------------------------------------|
| [AI Usage Checklist](./checklists/ai-usage.md) | Verification checklist for AI-generated code, docs and architecture. |

### Templates

| Document                                                            | Description                                   |
|---------------------------------------------------------------------|-----------------------------------------------|
| [Context Pack Template](./templates/ai/context-pack.md)             | Structure for assembling AI context packs.    |
| [Prompt Template](./templates/ai/prompt-template.md)                | Standard prompt structure for engineering AI. |
| [AI Review Response Template](./templates/ai/ai-review-response.md) | Format for documenting AI review findings.    |

### Learning Paths

| Document                                                       | Description                            |
|----------------------------------------------------------------|----------------------------------------|
| [AI Engineering Learning Paths](./learning-paths/ai/README.md) | Beginner/intermediate/advanced tracks. |

### References

| Document                                               | Description                                                         |
|--------------------------------------------------------|---------------------------------------------------------------------|
| [AI Engineering References](./references/ai/README.md) | Quick lookup: workflow patterns, context categories, failure modes. |

### AI Workflows

| Document                                                        | Description                                           |
|-----------------------------------------------------------------|-------------------------------------------------------|
| [AI Workflows for AI Engineering](./prompts/ai-ai-workflows.md) | Prompt patterns for AI-assisted AI engineering tasks. |

## Accessibility Engineering

### Handbooks

| Document                                                                  | Description                                          |
|---------------------------------------------------------------------------|------------------------------------------------------|
| [Accessibility Engineering Handbook](./handbooks/accessibility/README.md) | Principles, WCAG standards, testing, AI integration. |

### Glossaries

| Document                                                     | Description                                               |
|--------------------------------------------------------------|-----------------------------------------------------------|
| [Accessibility Glossary](./glossary/accessibility/README.md) | Terminology (WCAG, ARIA, screen reader, colour contrast). |

### Guides

| Document                                                                   | Description                                     |
|----------------------------------------------------------------------------|-------------------------------------------------|
| [Semantic HTML](./guides/accessibility/semantic-html.md)                   | Using HTML elements for their intended purpose. |
| [Keyboard Accessibility](./guides/accessibility/keyboard-accessibility.md) | Ensuring full keyboard operability.             |
| [Accessible Forms](./guides/accessibility/accessible-forms.md)             | Building forms that work for everyone.          |
| [ARIA Patterns](./guides/accessibility/aria-patterns.md)                   | Using ARIA correctly for custom widgets.        |
| [Colour and Contrast](./guides/accessibility/colour-and-contrast.md)       | Meeting colour contrast requirements.           |
| [Screen Reader Testing](./guides/accessibility/screen-reader-testing.md)   | Testing with assistive technologies.            |

### Playbooks

| Document                                                                    | Description                                   |
|-----------------------------------------------------------------------------|-----------------------------------------------|
| [Accessibility Review Playbook](./playbooks/accessibility-review/README.md) | Workflow for reviewing digital accessibility. |

### Checklists

| Document                                                               | Description                                        |
|------------------------------------------------------------------------|----------------------------------------------------|
| [WCAG Audit Checklist](./checklists/accessibility/wcag-audit.md)       | Comprehensive WCAG compliance audit.               |
| [PR Accessibility Checklist](./checklists/accessibility/pr-review.md)  | Quick accessibility checks for every pull request. |
| [Design Review Checklist](./checklists/accessibility/design-review.md) | Accessibility checks during the design phase.      |

### Templates

| Document                                                                        | Description                                       |
|---------------------------------------------------------------------------------|---------------------------------------------------|
| [Accessibility Report](./templates/accessibility/accessibility-report.md)       | Standard format for accessibility audit findings. |
| [Accessibility Statement](./templates/accessibility/accessibility-statement.md) | Public-facing accessibility statement.            |

### Learning Paths

| Document                                                                 | Description                            |
|--------------------------------------------------------------------------|----------------------------------------|
| [Accessibility Learning Paths](./learning-paths/accessibility/README.md) | Beginner/intermediate/advanced tracks. |

### References

| Document                                                         | Description                                                 |
|------------------------------------------------------------------|-------------------------------------------------------------|
| [Accessibility References](./references/accessibility/README.md) | Quick lookup: WCAG levels, contrast ratios, ARIA landmarks. |

### AI Workflows

| Document                                                                  | Description                                            |
|---------------------------------------------------------------------------|--------------------------------------------------------|
| [AI Workflows for Accessibility](./prompts/accessibility-ai-workflows.md) | Prompt patterns for auditing, remediation and testing. |

# Cross-Cutting Topics

The following indexes gather documents across capabilities by topic.

## Testing

| Capability   | Document                                                                  | Type      | Description                                   |
|--------------|---------------------------------------------------------------------------|-----------|-----------------------------------------------|
| Engineering  | [Testing Strategies](./guides/engineering/testing-strategies.md)          | Guide     | Test pyramid, what to test, test doubles.     |
| Rails        | [Testing Rails Applications](./guides/rails/testing.md)                   | Guide     | Model/request/system specs, factory patterns. |
| Rails        | [Rails Pull Request Checklist](./checklists/rails/pull-request.md)        | Checklist | Testing verification for every PR.            |
| Architecture | [Architecture Review Playbook](./playbooks/architecture-review/README.md) | Playbook  | Review criteria includes testability.         |

## API Design and Development

| Capability   | Document                                                        | Type     | Description                                    |
|--------------|-----------------------------------------------------------------|----------|------------------------------------------------|
| Architecture | [API Design](./guides/architecture/api-design.md)               | Guide    | RESTful conventions, versioning, status codes. |
| Rails        | [API Development with Rails](./guides/rails/api-development.md) | Guide    | Rails-specific API setup, serialization, auth. |
| Rails        | [Rails Engineering Handbook](./handbooks/rails/README.md)       | Handbook | API standards and conventions section.         |

## Error Handling

| Capability  | Document                                                  | Type     | Description                                   |
|-------------|-----------------------------------------------------------|----------|-----------------------------------------------|
| Engineering | [Error Handling](./guides/engineering/error-handling.md)  | Guide    | Principles, patterns, logging, anti-patterns. |
| Engineering | [Logging](./guides/engineering/logging.md)                | Guide    | Structured logging, log levels, context.      |
| Rails       | [Service Objects](./guides/rails/service-objects.md)      | Guide    | Error handling in service objects.            |
| Rails       | [Rails Engineering Handbook](./handbooks/rails/README.md) | Handbook | Error handling standards.                     |

## Performance

| Capability | Document                                                 | Type  | Description                                   |
|------------|----------------------------------------------------------|-------|-----------------------------------------------|
| Rails      | [Rails Audit Guide](./guides/rails/audit-guide.md)       | Guide | Performance profiling, N+1 detection, APM.    |
| Rails      | [ActiveRecord Patterns](./guides/rails/active-record.md) | Guide | Query optimization, N+1 prevention, indexing. |
| Rails      | [Background Jobs](./guides/rails/background-jobs.md)     | Guide | Job performance, queue monitoring.            |

## Security

| Capability | Document                                                                 | Type      | Description                        |
|------------|--------------------------------------------------------------------------|-----------|------------------------------------|
| Security   | [Security Engineering Handbook](./handbooks/security/README.md)          | Handbook  | Principles, threat modeling, SDLC. |
| Security   | [Secure Coding Practices](./guides/security/secure-coding.md)            | Guide     | Input validation, auth, crypto.    |
| Security   | [Web Vulnerabilities](./guides/security/web-vulnerabilities.md)          | Guide     | OWASP Top 10 with mitigations.     |
| Security   | [Dependency Security](./guides/security/dependency-security.md)          | Guide     | Vulnerability scanning, response.  |
| Security   | [Security Review Playbook](./playbooks/security-review/README.md)        | Playbook  | Threat modeling, review workflow.  |
| Security   | [Security Review Checklist](./checklists/security-review.md)             | Checklist | General security verification.     |
| Rails      | [Rails Security Review Checklist](./checklists/rails/security-review.md) | Checklist | Rails-specific security checks.    |
| Rails      | [Rails Audit Guide](./guides/rails/audit-guide.md)                       | Guide     | Security auditing section.         |

## Architecture Decisions

| Capability   | Document                                                        | Type      | Description                                |
|--------------|-----------------------------------------------------------------|-----------|--------------------------------------------|
| Architecture | [Architecture Handbook](./handbooks/architecture/README.md)     | Handbook  | Decision frameworks, ADR standards.        |
| Architecture | [ADR Writing Guide](./guides/architecture/adr-writing-guide.md) | Guide     | When and how to write ADRs.                |
| Architecture | [ADR Template](./templates/adr/README.md)                       | Template  | Standard ADR format.                       |
| Architecture | [RFC Template](./templates/rfc/README.md)                       | Template  | Major proposal format.                     |
| Architecture | [Design Decision Checklist](./checklists/design-decision.md)    | Checklist | Before/during/after decision verification. |

## Architecture Decision Records

| Document                                                                               | Description                                        |
|----------------------------------------------------------------------------------------|----------------------------------------------------|
| [ADR 0001: Capability Model](./adr/0001-capability-model.md)                           | Knowledge organization around capabilities.        |
| [ADR 0002: Org-Mode Format](./adr/0002-org-mode-format.md)                             | Org-mode as primary document format.               |
| [ADR 0003: Document Taxonomy](./adr/0003-document-taxonomy.md)                         | Nine document types with single responsibility.    |
| [ADR 0004: AI-Native Knowledge Design](./adr/0004-ai-native-knowledge-design.md)       | AI as first-class knowledge consumer.              |
| [ADR 0005: Foundation Capabilities First](./adr/0005-foundation-capabilities-first.md) | Build fundamentals before technology capabilities. |
| [ADR 0006: Per-Capability Glossaries](./adr/0006-per-capability-glossaries.md)         | Glossaries organized by capability.                |


## Project Setup and Standards

| Capability  | Document                                                       | Type      | Description                        |
|-------------|----------------------------------------------------------------|-----------|------------------------------------|
| Rails       | [Rails Project Standards](./guides/rails/project-standards.md) | Guide     | Mandatory tooling, CI/CD baseline. |
| Rails       | [Rails Deployment Playbook](./playbooks/rails/deployment.md)   | Playbook  | Safe deployment with migrations.   |
| Rails       | [Rails Deployment Checklist](./checklists/rails/deployment.md) | Checklist | Pre/post-deploy verification.      |
| Engineering | [Tech Debt Assessment](./checklists/tech-debt-assessment.md)   | Checklist | Debt identification and tracking.  |

## Quality

| Capability | Document                                                                   | Type      | Description                             |
|------------|----------------------------------------------------------------------------|-----------|-----------------------------------------|
| Quality    | [Engineering Quality Handbook](./handbooks/quality/README.md)              | Handbook  | Quality principles, gates, metrics.     |
| Quality    | [Code Review Standards](./guides/quality/code-review-standards.md)         | Guide     | Review velocity, what to review.        |
| Quality    | [Quality Metrics](./guides/quality/quality-metrics.md)                     | Guide     | Code quality and process metrics.       |
| Quality    | [Technical Debt Management](./guides/quality/technical-debt-management.md) | Guide     | Debt classification and management.     |
| Quality    | [Quality Review Playbook](./playbooks/quality/quality-review.md)           | Playbook  | Systematic quality assessment.          |
| Quality    | [Technical Debt Remediation](./playbooks/quality/tech-debt-remediation.md) | Playbook  | Managing and reducing technical debt.   |
| Quality    | [Release Quality Gate](./playbooks/quality/release-quality-gate.md)        | Playbook  | Quality verification before release.    |
| Quality    | [Quality Gate Checklist](./checklists/quality/quality-gate.md)             | Checklist | Verification before accepting changes.  |
| Quality    | [Release Readiness Checklist](./checklists/quality/release-readiness.md)   | Checklist | Verification before production release. |
| Quality    | [Technical Debt Triage](./checklists/quality/tech-debt-triage.md)          | Checklist | Classification and prioritisation.      |
| Quality    | [Quality Report Template](./templates/quality/quality-report.md)           | Template  | Standard quality review report format.  |
| Quality    | [Technical Debt Register](./templates/quality/tech-debt-register.md)       | Template  | Track and monitor technical debt.       |
| Quality    | [Quality Dashboard Template](./templates/quality/quality-dashboard.md)     | Template  | Track quality metrics over time.        |
| Quality    | [AI Workflows for Quality](./prompts/quality-ai-workflows.md)              | AI Work   | Prompt patterns for quality review.     |

## AI and Engineering

| Capability     | Document                                                                             | Type      | Description                             |
|----------------|--------------------------------------------------------------------------------------|-----------|-----------------------------------------|
| AI Engineering | [AI Engineering Handbook](./handbooks/ai/README.md)                                  | Handbook  | AI principles, context engineering,     |
|                |                                                                                      |           | workflow patterns.                      |
|                | [Prompt Engineering](./guides/ai/prompt-engineering.md)                              | Guide     | Patterns and anti-patterns for prompt   |
|                |                                                                                      |           | design.                                 |
|                | [Context Engineering](./guides/ai/context-engineering.md)                            | Guide     | Providing effective context to AI.      |
|                | [AI Safety and Verification](./guides/ai/ai-safety.md)                               | Guide     | Safe and responsible AI use practices.  |
|                | [Agentic Workflows](./guides/ai/agentic-workflows.md)                                | Guide     | Multi-step AI-assisted workflows.       |
|                | [AI Collaboration Patterns](./guides/ai/collaboration-patterns.md)                   | Guide     | Engineer-AI interaction models.         |
|                | [Human Review Strategies](./guides/ai/human-review-strategies.md)                    | Guide     | Reviewing AI output effectively.        |
|                | [AI Evaluation Frameworks](./guides/ai/evaluation-frameworks.md)                     | Guide     | Measuring AI output quality.            |
|                | [Knowledge Extraction](./guides/ai/knowledge-extraction.md)                          | Guide     | Extracting knowledge with AI.           |
|                | [AI-Assisted Code Review](./playbooks/ai/ai-assisted-code-review.md)                 | Playbook  | AI-assisted code review workflow.       |
|                | [AI-Assisted Architecture Review](./playbooks/ai/ai-assisted-architecture-review.md) | Playbook  | AI-assisted architecture review.        |
|                | [AI Pair Programming](./playbooks/ai/ai-pair-programming.md)                         | Playbook  | Collaborative coding with AI.           |
|                | [Verification Workflows](./playbooks/ai/verification-workflows.md)                   | Playbook  | Systematic AI output verification.      |
|                | [AI Usage Checklist](./checklists/ai-usage.md)                                       | Checklist | Verification for AI-generated output.   |
|                | [Context Pack Template](./templates/ai/context-pack.md)                              | Template  | Structure for AI context packs.         |
|                | [Prompt Template](./templates/ai/prompt-template.md)                                 | Template  | Standard prompt structure.              |
|                | [AI Engineering References](./references/ai/README.md)                               | Reference | Workflow patterns, failure modes.       |
| Engineering    | [AI Workflows for Engineering](./prompts/engineering-ai-workflows.md)                | AI Work   | Prompt patterns for code review, design |
|                |                                                                                      |           | exploration, refactoring.               |
| Architecture   | [AI Workflows for Architecture](./prompts/architecture-ai-workflows.md)              | AI Work   | Prompt patterns for trade-off analysis, |
|                |                                                                                      |           | ADR drafting, pattern selection.        |
| Rails          | [AI Workflows for Rails](./prompts/rails-ai-workflows.md)                            | AI Work   | Prompt patterns for model gen, API dev, |
|                |                                                                                      |           | testing.                                |
| Security       | [AI Workflows for Security](./prompts/security-ai-workflows.md)                      | AI Work   | Prompt patterns for vulnerability ID,   |
|                |                                                                                      |           | threat modeling.                        |
| Quality        | [AI Workflows for Quality](./prompts/quality-ai-workflows.md)                        | AI Work   | Prompt patterns for quality review.     |
| Accessibility  | [AI Workflows for Accessibility](./prompts/accessibility-ai-workflows.md)            | AI Work   | Prompt patterns for accessibility.      |
| AI Engineering | [AI Workflows for AI Engineering](./prompts/ai-ai-workflows.md)                      | AI Work   | Prompt patterns for AI engineering.     |

# Related Documents

- [Repository Overview](./README.md)
- [Roadmap](./roadmap.md)
- [Style Guide](./style-guide.md)
