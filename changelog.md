---
title: "Changelog"
description: "Version history of the Engineering Knowledge Framework, newest release last."
type: governance
capability: governance
status: published
tags: [changelog]
last_reviewed: 2026-07-28
---

# 0.1.0 (2026-07-27)

## Initial Framework Creation

- Established the Engineering Knowledge Framework repository.

## Governance Documents

- Added `README.org`: Repository overview, mission, vision, and core philosophy.
- Added `CLAUDE.md`: AI-specific project instructions and guidelines.
- Added `STRATEGY.org`: Long-term strategy and guiding vision.
- Added `ROADMAP.org`: Strategic roadmap with milestones and themes.
- Added `CONTRIBUTING.org`: Contribution guidelines and processes.
- Added `STYLE_GUIDE.org`: Writing, formatting, and documentation standards.
- Added `WRITING_PRINCIPLES.org`: Principles for creating high-quality, timeless engineering knowledge.
- Added `ARCHITECTURE.org`: Architectural overview of the framework.
- Added `CHANGELOG.org`: Version history (this file).

## Knowledge Architecture

- Added `DOCUMENT_TYPES.org`: Canonical document taxonomy defining all document types (handbook, guide, playbook, checklist, reference, template, glossary, RFC, ADR, learning path).
- Added `glossary/README.org`: Glossary structure and writing guidelines.
- Established capability-aligned glossary directories:
  - `glossary/engineering/`, `glossary/architecture/`, `glossary/rails/`
  - `glossary/security/`, `glossary/accessibility/`, `glossary/testing/`

## Engineering Capabilities (Stubs)

- Established handbook directories for core capabilities:
  - `handbooks/engineering/`, `handbooks/architecture/`, `handbooks/rails/`
  - `handbooks/security/`, `handbooks/accessibility/`, `handbooks/quality/`
  - `handbooks/ai/`
- Established playbook directories for key workflows:
  - `playbooks/code-review/`, `playbooks/architecture-review/`
  - `playbooks/security-review/`, `playbooks/accessibility-review/`
  - `playbooks/incident-response/`, `playbooks/release/`
  - `playbooks/project-kickoff/`
- Added `assets/diagrams/` and `assets/images/` for visual resources.

## Placeholder Directories

- Created stub directories for future content:
  - `adr/` (Architecture Decision Records)
  - `checklists/`, `guides/`, `learning-paths/`, `prompts/`
  - `references/`, `rfc/`, `templates/`, `docs/`

# 0.2.0 (2026-07-27)

## Foundation Capabilities (Phase 2)

### Engineering Fundamentals

- Added `handbooks/engineering/README.org`: Engineering Fundamentals Handbook covering core principles (separation of concerns, encapsulation, composition over inheritance, dependency inversion, explicit dependencies, consistency), code organization, quality philosophy, technical debt management, decision frameworks and AI integration.
- Added `glossary/engineering/README.org`: Canonical engineering glossary with definitions for abstraction, cohesion, composition, coupling, dependency injection, encapsulation, modularity, refactoring, separation of concerns and technical debt.

### Software Architecture

- Added `handbooks/architecture/README.org`: Software Architecture Handbook covering architectural principles, patterns (layered, hexagonal, event-driven, microservices), decision documentation standards (ADRs, RFCs, decision log), C4 model, event modeling, quality attribute trade-offs, architecture review practices and AI integration.
- Added `glossary/architecture/README.org`: Architecture glossary with definitions for ADR, bounded context, C4 model, decision log, DDD, event storming, hexagonal architecture, layered architecture, quality attributes, RFC and trade-off.

## Roadmap Restructured

- Renamed "Phase Transition" to "Phase Progression" to clarify it is not a phase.
- Normalized phase sections with consistent `*** Objectives`, `*** Deliverables`, `*** Success Criteria` structure.
- Added `*** Objectives` and `** Potential Tooling` headings to Phases 4-9 for consistency.
- Updated Phase 2 deliverables to mark completed handbook and glossary items as [x].
- Reorganized closing sections (Measuring Progress, Near-term Priorities, Future Evolution) to sit clearly after phases.

## Architecture Decision Records

- Created `templates/adr/README.org`: ADR template with standard sections (context, decision, consequences, alternatives considered, references).
- Added `adr/0001-capability-model.org`: Decision to organize knowledge around Engineering Capabilities.
- Added `adr/0002-org-mode-format.org`: Decision to use Org-mode as the primary document format.
- Added `adr/0003-document-taxonomy.org`: Decision to use nine document types with single responsibility.
- Added `adr/0004-ai-native-knowledge-design.org`: Decision to treat AI as a first-class knowledge consumer.
- Added `adr/0005-foundation-capabilities-first.org`: Decision to build Engineering Fundamentals and Architecture before technology-specific capabilities.
- Added `adr/0006-per-capability-glossaries.org`: Decision to organize glossaries by capability with a shared root glossary.

## Engineering Guides

- Added `guides/engineering/code-organization.org`: Code organization principles, feature-based packaging, patterns and anti-patterns.
- Added `guides/engineering/error-handling.org`: Error handling principles, recoverable vs unrecoverable errors, patterns, logging standards.
- Added `guides/engineering/testing-strategies.org`: Testing philosophy, test pyramid, what to test, test doubles and anti-patterns.

## Architecture Guides

- Added `guides/architecture/adr-writing-guide.org`: When and how to write ADRs, lifecycle states, characteristics of good ADRs, common mistakes.
- Added `guides/architecture/architectural-patterns.org`: Pattern catalogue (layered, hexagonal, event-driven, microservices, CQRS) with trade-offs and composition guidance.

## Playbooks

- Added `playbooks/code-review/README.org`: Complete code review workflow with design review, implementation review, feedback guidelines, severity labels and AI workflow.
- Added `playbooks/architecture-review/README.org`: Architecture review workflow with scope determination, review team assembly, evaluation criteria, outcome documentation and AI workflow.

## Templates

- Added `templates/rfc/README.org`: RFC template for major architectural proposals with motivation, proposed solution, alternatives, impact assessment, quality attribute matrix and migration plan.

## Checklists

- Added `checklists/architecture-review.org`: Pre-review, during-review and post-review verification checklist.
- Added `checklists/design-decision.org`: Before, during and after design decision checklist.
- Added `checklists/tech-debt-assessment.org`: Identification, classification, tracking and remediation planning checklist.

## Additional Guides

- Added `guides/engineering/logging.org`: Logging principles, structured format standards, log levels, context fields and anti-patterns.
- Added `guides/architecture/api-design.org`: API design principles, RESTful conventions, versioning, documentation standards and anti-patterns.
- Added `guides/architecture/system-modeling.org`: C4 model (context, container, component, code) and event modeling with workshop format.

## Learning Paths

- Added `learning-paths/engineering/README.org`: Three-tier learning path (beginner, intermediate, advanced) with topics, suggested projects and assessment criteria for engineering fundamentals.
- Added `learning-paths/architecture/README.org`: Three-tier learning path (beginner, intermediate, advanced) with topics, suggested projects and assessment criteria for software architecture.

## References

- Added `references/engineering/README.org`: Quick-reference material for design principles, code organization patterns, testing, error handling, log levels and recommended reading.
- Added `references/architecture/README.org`: Quick-reference material for C4 model, architectural pattern comparison, HTTP status codes, quality attributes, ADR lifecycle and recommended reading.

## AI Workflows

- Added `prompts/engineering-ai-workflows.org`: Prompt patterns and workflows for AI-assisted code review, design exploration, refactoring, documentation generation and problem diagnosis.
- Added `prompts/architecture-ai-workflows.org`: Prompt patterns and workflows for AI-assisted trade-off analysis, ADR drafting, pattern selection, architecture review preparation and system design exploration.

# 0.3.0 (2026-07-27)

## Security Engineering Capability (Phase 3)

- Added `handbooks/security/README.org`: Security Engineering Handbook covering security principles (defense in depth, least privilege, secure by default, fail securely), threat modeling (STRIDE), secure development lifecycle, common vulnerabilities, security standards and AI integration.
- Added `glossary/security/README.org`: Security terminology (CSRF, defense in depth, IDOR, least privilege, SAST, secure by default, SQL injection, threat modeling, XSS).
- Added `guides/security/secure-coding.org`: Secure coding practices covering input validation, authentication, authorization, output encoding, error handling and cryptography.
- Added `guides/security/web-vulnerabilities.org`: OWASP Top 10 (2021) with explanations and mitigations for each category, plus Rails-specific vulnerabilities.
- Added `guides/security/dependency-security.org`: Dependency security management covering vulnerability scanning, dependency selection criteria, vulnerability response workflow, license compliance and hygiene.
- Added `playbooks/security-review/README.org`: Security review workflow with scoping, threat modeling (STRIDE), code/configuration review, dependency review, finding documentation and remediation.
- Added `checklists/security-review.org`: General security review checklist covering authentication, authorization, input validation, output protection, data protection, dependencies, logging and infrastructure.
- Added `learning-paths/security/README.org`: Three-tier learning path (beginner, intermediate, advanced) for security engineering.
- Added `references/security/README.org`: Quick-reference material for OWASP Top 10, STRIDE, security tools, response timeline and security headers.
- Added `prompts/security-ai-workflows.org`: Prompt patterns for vulnerability identification, threat modeling, configuration review and incident analysis.

## AI Engineering Capability (Phase 3)

- Added `handbooks/ai/README.org`: AI Engineering Handbook covering principles (AI augments, human responsibility, context is primary lever, verify everything), context engineering, AI workflow patterns (draft and refine, constrain and generate, analyse and advise, explore and discover), verification and validation, team integration practices.
- Added `glossary/ai/README.org`: AI terminology (context engineering, hallucination, prompt engineering, verification).
- Added `guides/ai/prompt-engineering.org`: Prompt engineering principles, patterns (persona, format, constraint, verification, decomposition) and anti-patterns.
- Added `guides/ai/context-engineering.org`: Context engineering with categories (scope, constraints, standards, examples, references), context templates for code generation, code review and design exploration.
- Added `guides/ai/ai-safety.org`: AI safety practices covering human oversight, high-risk use cases, prohibited uses, verification practices and over-reliance prevention.
- Added `checklists/ai-usage.org`: Verification checklist for AI-generated code, documentation, architecture and general usage.
- Added `learning-paths/ai/README.org`: Three-tier learning path (beginner, intermediate, advanced) for AI-assisted engineering.
- Added `references/ai/README.org`: Quick-reference material for AI workflow patterns, context categories, failure modes and prompt patterns.

## Engineering Quality Capability (Phase 3)

- Added `handbooks/quality/README.org`: Engineering Quality Handbook covering quality principles, quality gates (pre-commit, PR, deploy, release), quality metrics (DORA, code quality), code review standards, technical debt management and quality culture.
- Added `glossary/quality/README.org`: Quality terminology (change failure rate, defect escape rate, MTTR, quality gate, technical debt).
- Added `guides/quality/code-review-standards.org`: Code review standards covering review velocity, what to review (design, correctness, maintainability, testing), review quality and severity labels.
- Added `guides/quality/quality-metrics.org`: Quality metrics guide covering code quality metrics (complexity, duplication, coverage), process metrics (deployment frequency, change failure rate, MTTR), implementation steps and common pitfalls.
- Added `guides/quality/technical-debt-management.org`: Technical debt management guide covering classification (strategic vs accidental), assessment, management process, tracking approaches and prevention.
- Added `learning-paths/quality/README.org`: Three-tier learning path for engineering quality.
- Added `references/quality/README.org`: Quick-reference material for quality gates, metrics targets, severity labels and debt classification.

## Rails Engineering Capability (Phase 3)

- Added `handbooks/rails/README.org`: Rails Engineering Handbook covering Rails philosophy, MVC principles, code organization, standards (models, migrations, routes, API), testing strategy, patterns (service objects, form objects, query objects, policy objects), anti-patterns and AI integration.
- Added `glossary/rails/README.org`: Rails-specific terminology (ActiveRecord, concern, controller, form object, migration, model, presenter, query object, service object, view).
- Added `guides/rails/service-objects.org`: When and how to use service objects with structure, patterns, testing and anti-patterns.
- Added `guides/rails/testing.org`: Rails-specific testing strategy covering test distribution, model specs, request specs, system specs, factory patterns and what to avoid.
- Added `playbooks/rails/upgrade.org`: Step-by-step Rails upgrade workflow with compatibility assessment, gem updates, testing, configuration changes, deployment and rollback plan.
- Added `checklists/rails/pull-request.org`: Rails PR checklist for authors and reviewers covering code quality, testing, security, documentation and migration safety.
- Added `references/rails/README.org`: Quick-reference material including Rails conventions, common generators, testing commands, key gems and HTTP status codes.
- Added `learning-paths/rails/README.org`: Three-tier learning path (beginner, intermediate, advanced) with topics, projects and assessment criteria.
- Added `prompts/rails-ai-workflows.org`: Prompt patterns for AI-assisted model generation, API development, testing, debugging and refactoring in Rails.
- Added `guides/rails/audit-guide.org`: Comprehensive guide to Rails code quality tools (RuboCop, Brakeman, bundler-audit, Reek, rails_best_practices, Bullet, Fasterer), audit pipeline setup (pre-commit, CI, scheduled, release gate), tool configuration, audit frequency, result prioritization, Rails-specific audit areas and quality standard establishment.
- Added `guides/rails/project-standards.org`: Mandatory tooling baseline for every Rails project covering required gems (RuboCop, Brakeman, bundler-audit, Bullet, Rack::MiniProfiler, SimpleCov), CI/CD pipeline template with quality gates, project bootstrap script, pre-commit hook configuration, exception process and compliance verification.
- Added `guides/rails/active-record.org`: ActiveRecord patterns and query optimization covering scopes, query optimization, N+1 prevention, indexing strategy, counter caches and transactions.
- Added `guides/rails/api-development.org`: API development with Rails covering API-only setup, routing, controllers, serialization, response format, authentication, versioning and testing.
- Added `guides/rails/background-jobs.org`: Background job patterns covering framework selection (Sidekiq, GoodJob, SolidQueue, DelayedJob), job structure, idempotency, error handling, monitoring and common patterns.
- Added `guides/rails/authentication-authorization.org`: Authentication and authorization patterns covering Devise setup, Pundit policies, role-based authorization, view-level authorization and anti-patterns.
- Added `playbooks/rails/deployment.org`: Rails deployment playbook with migration safety review, zero-downtime deployment patterns, deployment monitoring, rollback procedures and migration patterns (concurrent indexes, backfilling, safe column removal).
- Added `checklists/rails/security-review.org`: Security verification checklist covering authentication, authorization, data protection, input validation, output protection, dependency security and infrastructure.
- Added `checklists/rails/deployment.org`: Pre-deployment, deployment and post-deployment verification checklist.
- Added `templates/rails/service-object.org`: Reusable service object template with result object pattern.
- Added `templates/rails/form-object.org`: Reusable form object template with ActiveModel integration.
- Added `templates/rails/query-object.org`: Reusable query object template with composable scope chaining.
- Added `templates/rails/policy-object.org`: Reusable authorization policy template with Pundit conventions.

# 0.4.0 (2026-07-27)

## Roadmap Updated

- Updated Phase 1 (Foundation) to mark as complete with lessons learned.
- Updated Phase 2 (Foundation Capabilities) to mark as complete with lessons learned.
- Updated Phase 3 (Engineering Capabilities): Rails, Security, AI Engineering,
  and Engineering Quality capabilities are now marked complete with detailed
  deliverable breakdowns. Accessibility remains a stub for future development.
- Updated Phase 4 (AI Engineering Framework): Existing AI handbook, glossary,
  guides, checklists, learning paths, references and four domain AI workflow
  documents are now listed as completed deliverables. Next steps identified.
- Updated Phase 5 (Learning Framework): Existing learning paths are listed as
  completed. Next steps for practical exercises, projects and assessments added.
- Updated Current Phase section to reflect Phase 2 completion and Phase 3
  substantial delivery.
- Updated Near-term Priorities with completed items marked [x] and new items
  for Accessibility, learning path exercises, AI agentic workflows and tooling.

## Roadmap Phases 6-9 Expanded

- Phase 6 (Framework Tooling): Added Status, detailed deliverables across
  three sub-phases (validation, generators, knowledge graph), development
  approach and lessons learned.
- Phase 7 (Platform): Added Status, deliverables for static site, knowledge
  graph UI, AI integration and platform features, with development approach.
- Phase 8 (Community): Added Status, deliverables for onboarding, review,
  and engagement, with development approach.
- Phase 9 (Open Standard): Added Status, deliverables for specification,
  ecosystem and governance, with long-term development approach.

# 0.5.0 (2026-07-27)

## Phase 3 Gaps Filled

### Security Engineering — Templates Added

- Added `templates/security/README.org`: Security templates index.
- Added `templates/security/threat-model.org`: Structured threat model template using STRIDE.
- Added `templates/security/security-review-report.org`: Findings report template.

### AI Engineering — Playbooks, Templates, AI Workflows Added

- Added `playbooks/ai/README.org`: AI engineering playbooks index.
- Added `playbooks/ai/ai-assisted-code-review.org`: AI-assisted code review workflow.
- Added `playbooks/ai/ai-assisted-architecture-review.org`: AI-assisted architecture review workflow.
- Added `playbooks/ai/ai-pair-programming.org`: AI pair programming workflow.
- Added `templates/ai/README.org`: AI templates index.
- Added `templates/ai/context-pack.org`: Context pack template.
- Added `templates/ai/prompt-template.org`: Standard prompt structure template.
- Added `templates/ai/ai-review-response.org`: AI review findings template.
- Added `prompts/ai-ai-workflows.org`: AI workflows for AI engineering.

### Engineering Quality — Playbooks, Checklists, Templates, AI Workflows Added

- Added `playbooks/quality/README.org`: Quality playbooks index.
- Added `playbooks/quality/quality-review.org`: Quality review process playbook.
- Added `playbooks/quality/tech-debt-remediation.org`: Technical debt remediation playbook.
- Added `playbooks/quality/release-quality-gate.org`: Release quality gate playbook.
- Added `checklists/quality/README.org`: Quality checklists index.
- Added `checklists/quality/quality-gate.org`: Quality gate checklist.
- Added `checklists/quality/release-readiness.org`: Release readiness checklist.
- Added `checklists/quality/tech-debt-triage.org`: Tech debt triage checklist.
- Added `templates/quality/README.org`: Quality templates index.
- Added `templates/quality/quality-report.org`: Quality report template.
- Added `templates/quality/tech-debt-register.org`: Tech debt register template.
- Added `templates/quality/quality-dashboard.org`: Quality dashboard template.
- Added `prompts/quality-ai-workflows.org`: AI workflows for quality engineering.

### Accessibility Engineering — Complete Capability Added

- Added `handbooks/accessibility/README.org`: Accessibility Engineering Handbook.
- Added `glossary/accessibility/README.org`: Accessibility terminology glossary.
- Added `guides/accessibility/README.org`: Accessibility guides index.
- Added `guides/accessibility/semantic-html.org`: Semantic HTML guide.
- Added `guides/accessibility/keyboard-accessibility.org`: Keyboard accessibility guide.
- Added `guides/accessibility/accessible-forms.org`: Accessible forms guide.
- Added `guides/accessibility/aria-patterns.org`: ARIA patterns guide.
- Added `guides/accessibility/colour-and-contrast.org`: Colour and contrast guide.
- Added `guides/accessibility/screen-reader-testing.org`: Screen reader testing guide.
- Added `playbooks/accessibility-review/README.org`: Accessibility review playbook.
- Added `checklists/accessibility/README.org`: Accessibility checklists index.
- Added `checklists/accessibility/wcag-audit.org`: WCAG audit checklist.
- Added `checklists/accessibility/pr-review.org`: PR accessibility checklist.
- Added `checklists/accessibility/design-review.org`: Design review checklist.
- Added `templates/accessibility/README.org`: Accessibility templates index.
- Added `templates/accessibility/accessibility-report.org`: Audit report template.
- Added `templates/accessibility/accessibility-statement.org`: Accessibility statement template.
- Added `learning-paths/accessibility/README.org`: Three-tier learning path.
- Added `references/accessibility/README.org`: Quick-reference material.
- Added `prompts/accessibility-ai-workflows.org`: AI workflows for accessibility.

## Roadmap Updated

- Phase 3 status changed from In Progress to Complete.
- Current Phase updated to reflect Phase 3 completion.
- Phase 3 capability breakdowns updated: all five capabilities now marked
  [x] Complete with full document-type inventories.
- Phase 4 (AI Engineering Framework) updated with newly created AI playbooks,
  templates and domain AI workflows in the Completed section.
- Near-term Priorities consolidated: 9 completed items marked [x], remaining
  5 priorities reorganised (learning path exercises, AI agentic workflows,
  validation tooling, knowledge graph tooling, community engagement).

# 0.6.0 (2026-07-27)

## Phase 4 AI Content Completed

- Added `guides/ai/agentic-workflows.org`: Patterns for multi-step AI-assisted
  engineering workflows (draft-and-refine, analyse-and-recommend,
  explore-and-discover, constrain-and-generate).
- Added `guides/ai/collaboration-patterns.org`: Five collaboration patterns
  (AI as research assistant, scribe, reviewer, pair programmer, tutor).
- Added `guides/ai/human-review-strategies.org`: Five review strategies
  (read-through, test-driven, decomposition, comparison, walkaway) with
  risk-based depth guidance and common AI failure modes.
- Added `guides/ai/evaluation-frameworks.org`: Four evaluation methods
  (automated, structured review, comparative, longitudinal) with
  task-specific criteria and scoring rubric.
- Added `playbooks/ai/verification-workflows.org`: Systematic verification
  workflow with classification, automated checks, structured review,
  remediation and approval gates.
- Added `guides/ai/knowledge-extraction.org`: Workflow for capturing
  knowledge from experience, code, incidents and discussions into
  framework documents using AI assistance.

## Roadmap Updated

- Phase 4 Status updated to Substantially Complete.
- Phase 4 Next Steps replaced with Completed (added) listing all six
  new documents.
- Near-term Priorities: AI agentic workflows item marked [x].

# 0.7.0 (2026-07-29)

## Substrate Repair (Slice Plan 0001, Layer 0)

Prerequisite work for making framework knowledge executable in developer
and AI workflows. See
[Slice Plan 0001](./docs/slice-plans/0001-ai-native-tooling.md).

## Validation Tooling Rebuilt

- Rewrote `tools/validate-style.py` against Markdown. Its heading rule
  had used org-mode syntax (`^\*+\s`) since the migration and could
  never match a Markdown heading; its metadata and bullet rules returned
  success unconditionally. The validator reported clean across 302 files
  while checking only filenames.
- Extracted the rules into `tools/validate_style_lib.py` as pure
  functions, covered by 62 tests in `tools/test_validate_style.py`,
  including a regression test for the org-mode heading rule.
- Added rules: required front matter with taxonomy-checked values, code
  fence language tags, fence balance and nesting, table structure,
  org-mode residue, migration-mangled URLs, and untranslated text.
- `make validate` now runs the rule tests first, so a validator that has
  stopped checking anything fails the build instead of reporting
  success. Added a `make test` target and a CI step.

## Content Repaired

- Fixed 9 external links in the Accessibility capability whose slashes
  had been replaced with `*` during the org-to-Markdown migration,
  rendering them as literal text.
- Fixed 367 further lines of migration corruption across 39 files:
  paths and URLs where `/` became `*`, and org `=verbatim=` markup that
  became a stray backtick with a trailing `=`.
- Fixed 11 nested code fences in the AI workflow prompts and the Context
  Engineering guide, where an inner fence closed the outer block early
  and truncated the document when rendered.
- Tagged 227 code fences with a language.
- Fixed the Style Guide's Bullet Format section, whose Correct and
  Incorrect examples had become identical.
- Fixed `CLAUDE.md`, which instructed contributors using org verbatim
  markup and claimed `*` creates a heading in Markdown.
- Fixed `README.md`, which rendered a heading as a bullet and documented
  two directories that do not exist.
- Fixed a skipped heading level in the Rails handbook and untranslated
  text in its DRY section.

## Metadata Layer Added

- Added YAML front matter to all 150 documents: `title`, `description`,
  `type`, `capability`, `status`, `tags` and `last_reviewed`. Review
  dates come from each file's git history rather than the date of this
  change, so staleness reporting starts honest.
- `build-knowledge-graph.py` now reads front matter through the same
  parser validation enforces. Node descriptions went from 0 of 150
  populated to 150 of 150.
- `prepare-site-content.py` now translates YAML front matter into Zola
  TOML instead of discarding it and re-deriving titles from paths.
  Descriptions, capability, document type, status, review date and tags
  reach the site and its search index.
- Context pack search improved as a direct result: `service objects`
  returned no documents before this change and returns six after.

## Documentation

- Added `docs/slice-plans/` for working documents describing the
  framework's own construction, excluded from the site, knowledge graph,
  context packs and TOC validation.
- Added a Front Matter section to the Style Guide and split its
  Validation Checklist into automated and review-required items.
- Corrected Phase 6a of the Roadmap, which marked metadata validation
  and bullet linting complete when both were no-ops, and Phase 6c, which
  marked AI context packaging incomplete while Phase 7c marked it done.
