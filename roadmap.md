# Purpose

This roadmap describes the planned evolution of the Engineering
Knowledge Framework.

Unlike the [Strategy](./strategy.md), which defines the long-term vision, this document
captures the major initiatives required to realize that vision.

The roadmap should evolve continuously as the project matures.

# Guiding Principles

Roadmap priorities should always support the framework's mission:

- Build reusable engineering knowledge.
- Capture institutional learning.
- Enable effective collaboration between engineers and AI.
- Prefer timeless knowledge over transient implementation details.
- Improve engineering practice rather than simply increasing documentation.

Priority should always be given to work that strengthens the framework
itself before expanding its content.

# Phase Progression

Progress through phases is not strictly sequential. Work may overlap
between phases, especially for cross-cutting initiatives like AI
integration and tooling.

## Transition Criteria

A phase is considered complete when:

- All primary deliverables are published and reviewable.
- The phase's success criteria are satisfied.
- Lessons learned are captured in the framework.
- The next phase can build on solid foundations.

## Current Phase

The project has completed ***Phase 1*** (Foundation), ***Phase 2***
(Foundation Capabilities), ***Phase 3*** (Engineering Capabilities),
and ***Phase 4*** (AI Engineering Framework). All five Phase 3
capabilities — Rails Engineering, Security Engineering,
AI Engineering, Engineering Quality and Accessibility Engineering — are
now built out with all nine document types covered.

The Learning Framework (Phase 5) has learning paths for all seven
capabilities and needs practical exercises and assessments.

Framework Tooling (Phase 6) and the Static Site (Phase 7a) are
substantially built out — validation tools, knowledge graph generation,
Zola-based site with full-text search, and GitHub Pages deployment are
all operational. Remaining tooling work focuses on generator tooling
and deeper AI integration.

See the [CHANGELOG](./changelog.md) for the detailed deliverable list.

# Phase 1 — Foundation

Establish the governance and architectural foundations of the framework.

## Status

[x] ***Complete*** — All governance documents, repository structure,
    document taxonomy, and capability stubs are in place. Phase 1
    transition criteria are satisfied.

## Objectives

- Define repository philosophy.
- Establish writing standards.
- Define document taxonomy.
- Define repository architecture.
- Establish glossary structure.
- Create contribution guidelines.
- Define capability model.

## Deliverables

- [x] `README.org`: Repository overview, mission and philosophy.
- [x] `CLAUDE.md`: AI-specific project instructions and guidelines.
- [x] `STRATEGY.org`: Long-term strategy and guiding vision.
- [x] `ROADMAP.org`: Strategic roadmap (this document).
- [x] `STYLE_GUIDE.org`: Writing, formatting and documentation standards.
- [x] `DOCUMENT_TYPES.org`: Canonical document taxonomy.
- [x] `CONTRIBUTING.org`: Contribution guidelines and processes.
- [x] `ARCHITECTURE.org`: Architectural overview of the framework.
- [x] `glossary*README.org`: Glossary structure and writing guidelines.
- [x] Capability handbook stubs: engineering, architecture, rails, security, accessibility, quality, ai.
- [x] Workflow playbook stubs: code-review, architecture-review, security-review, accessibility-review, incident-response, release, project-kickoff.

## Success Criteria

- Governance documents are internally consistent.
- Repository structure is stable.
- Contributors can understand how the framework is organized.
- AI assistants can navigate the repository effectively.

## Lessons Learned

- Capability stubs provided clear scaffolding for later content.
- Org-mode with consistent heading levels improved AI parsability.
- Separating governance from content prevented architectural drift.

# Phase 2 — Foundation Capabilities

Develop foundational engineering capabilities that establish patterns
for all future capabilities.

Engineering Fundamentals and Software Architecture are the initial
foundation capabilities. They are chosen because engineering principles
apply across all capabilities and architecture concepts are referenced
by every engineering discipline.

## Status

[x] ***Complete*** — All deliverables published, validated, and reviewed.
    Phase 2 transition criteria are satisfied. These capabilities now
    serve as reusable templates for Phase 3.

## Objectives

Build comprehensive documentation for Engineering Fundamentals and
Software Architecture that:

- Demonstrates every supported document type.
- Follows all writing principles and style guidelines.
- Shows how capabilities compose across document types.
- Provides reusable patterns for future capabilities.
- Serves as a testbed for tooling and templates.
- Establishes cross-referencing conventions between capabilities.

## Deliverables

### 2a — Engineering Fundamentals

- [x] `handbooks*engineering*README.org`: Engineering Fundamentals Handbook covering core principles, quality philosophy and decision frameworks.
- [x] `glossary*engineering*README.org`: Foundational engineering terminology (abstraction, cohesion, coupling, encapsulation, modularity, separation of concerns, technical debt).
- [x] `guides*engineering*code-organization.org`: Code organization principles, patterns and anti-patterns.
- [x] `guides*engineering*error-handling.org`: Error handling principles, patterns and logging standards.
- [x] `guides*engineering*testing-strategies.org`: Testing philosophy, test pyramid and best practices.
- [x] `guides*engineering*logging.org`: Logging standards and structured logging patterns.
- [x] `learning-paths*engineering*README.org`: Progressive learning paths (beginner, intermediate, advanced) with topics, projects and assessment criteria.
- [x] `references*engineering*README.org`: Quick-reference material including design principles, code organization patterns, testing guidelines, log levels, error handling and recommended reading.

### 2b — Software Architecture

- [x] `handbooks*architecture*README.org`: Software Architecture Handbook covering architectural principles, patterns, decision frameworks and documentation standards.
- [x] `glossary*architecture*README.org`: Architecture-specific terminology (ADR, C4 model, DDD, hexagonal architecture, quality attributes, trade-offs).
- [x] `guides*architecture*adr-writing-guide.org`: How to write effective Architecture Decision Records.
- [x] `guides*architecture*architectural-patterns.org`: Guide to common architectural patterns and when to apply them.
- [x] `guides*architecture*api-design.org`: API design principles and standards.
- [x] `guides*architecture*system-modeling.org`: System modeling with C4 and event modeling.
- [x] `learning-paths*architecture*README.org`: Architecture learning paths (beginner, intermediate, advanced) with topics, projects and assessment criteria.
- [x] `references*architecture*README.org`: Quick-reference material including C4 model, pattern comparison, HTTP status codes, quality attributes, ADR lifecycle and recommended reading.

### Practices

- [x] `templates*adr*README.org`: ADR template with context, decision, consequences and alternatives format.
- [x] `templates*rfc*README.org`: RFC template for major architectural proposals.
- [x] `checklists*architecture-review.org`: Verification checklist for architecture reviews.
- [x] `checklists*design-decision.org`: Verification checklist for design decisions.
- [x] `checklists*tech-debt-assessment.org`: Verification checklist for technical debt assessment.

### Workflows

- [x] `playbooks*architecture-review*README.org`: Architecture review playbook with criteria, process and documentation standards.
- [x] `playbooks*code-review*README.org`: Engineering code review playbook covering principle-based and implementation-level review.

### AI Workflows

- [x] AI Workflows for Engineering (`prompts*engineering-ai-workflows.org`): Prompt patterns for code review, design exploration, refactoring, documentation generation and problem diagnosis.
- [x] AI Workflows for Architecture (`prompts*architecture-ai-workflows.org`): Prompt patterns for trade-off analysis, ADR drafting, pattern selection, review preparation and system design exploration.

## Success Criteria

- Demonstrates every supported document type from `DOCUMENT_TYPES.org`.
- Engineering Fundamentals and Architecture documents are internally consistent and cross-reference each other effectively.
- Every document follows the [Style Guide](./style-guide.md) and [Writing Principles](./writing-principles.md).
- Documents form a connected knowledge network with rich cross-references.
- Serves as a repeatable template for future capabilities.
- AI assistants can use the capabilities effectively.
- Provides clear vocabulary and principles that downstream capabilities will reference.

## Lessons Learned

- The capability template (handbook → glossary → guides → playbooks → checklists → templates → learning paths → references → AI workflows) proved effective and was reused in Phase 3.
- Cross-referencing between Engineering Fundamentals and Architecture established conventions that later capabilities followed.
- AI workflows should be included from the start, not added after capability completion.

# Phase 3 — Engineering Capabilities

Expand the framework to additional engineering disciplines using the
Engineering Fundamentals and Architecture capabilities as templates.

## Status

[x] ***Complete*** — All five engineering capabilities are built out
    across all nine document types (handbook, glossary, guides,
    playbooks, checklists, templates, learning paths, references, AI
    workflows). Phase 3 transition criteria are satisfied. These
    capabilities now form the reusable knowledge foundation for future
    engineering disciplines.

## Objectives

- Build complete capabilities for additional engineering disciplines.
- Validate the capability template established in Phase 2.
- Establish cross-referencing patterns between capabilities.
- Grow the repository's knowledge graph.

## Capability Breakdown

### [x] Rails Engineering — Complete (all 9 document types)

- [x] `handbooks*rails*README.org`: Rails Engineering Handbook.
- [x] `glossary*rails*README.org`: Rails-specific terminology.
- [x] `guides*rails*service-objects.org`, `testing.org`, `audit-guide.org`, `project-standards.org`, `active-record.org`, `api-development.org`, `background-jobs.org`, `authentication-authorization.org` (8 guides).
- [x] `playbooks*rails*upgrade.org`, `deployment.org`, `README.org` (3 playbooks).
- [x] `checklists*rails*pull-request.org`, `security-review.org`, `deployment.org`, `README.org` (4 checklists).
- [x] `templates*rails*service-object.org`, `form-object.org`, `query-object.org`, `policy-object.org`, `README.org` (5 templates).
- [x] `learning-paths*rails*README.org`: Three-tier learning path.
- [x] `references*rails*README.org`: Quick-reference material.
- [x] `prompts*rails-ai-workflows.org`: AI workflows for Rails development.

### [x] Rails Engineering — Complete (all 9 document types)

- [x] `handbooks*rails*README.org`: Rails Engineering Handbook.
- [x] `glossary*rails*README.org`: Rails-specific terminology.
- [x] `guides*rails*` (8 guides): service-objects, testing, audit-guide,
  project-standards, active-record, api-development, background-jobs,
  authentication-authorization.
- [x] `playbooks*rails*` (3): upgrade, deployment, README.
- [x] `checklists*rails*` (4): pull-request, security-review, deployment, README.
- [x] `templates*rails*` (5): service-object, form-object, query-object,
  policy-object, README.
- [x] `learning-paths*rails*README.org`: Three-tier learning path.
- [x] `references*rails*README.org`: Quick-reference material.
- [x] `prompts*rails-ai-workflows.org`: AI workflows for Rails development.

### [x] Security Engineering — Complete (all 9 document types)

- [x] `handbooks*security*README.org`: Security Engineering Handbook.
- [x] `glossary*security*README.org`: Security terminology.
- [x] `guides*security*` (3 + README): secure-coding, web-vulnerabilities,
  dependency-security.
- [x] `playbooks*security-review*README.org`: Security review workflow.
- [x] `checklists*security-review.org`: General security review checklist.
- [x] `templates*security*` (3): threat-model, security-review-report, README.
- [x] `learning-paths*security*README.org`: Three-tier learning path.
- [x] `references*security*README.org`: Quick-reference material.
- [x] `prompts*security-ai-workflows.org`: AI workflows for security.

### [x] AI Engineering — Complete (all 9 document types)

- [x] `handbooks/ai*README.org`: AI Engineering Handbook.
- [x] `glossary*ai*README.org`: AI terminology.
- [x] `guides*ai*` (3): prompt-engineering, context-engineering, ai-safety.
- [x] `playbooks*ai*` (4): ai-assisted-code-review,
  ai-assisted-architecture-review, ai-pair-programming, README.
- [x] `checklists*ai-usage.org`: AI usage verification checklist.
- [x] `templates/ai*` (4): context-pack, prompt-template,
  ai-review-response, README.
- [x] `learning-paths*ai*README.org`: Three-tier learning path.
- [x] `references*ai*README.org`: Quick-reference material.
- [x] `prompts*ai-ai-workflows.org`: AI workflows for AI engineering.

### [x] Engineering Quality — Complete (all 9 document types)

- [x] `handbooks*quality*README.org`: Engineering Quality Handbook.
- [x] `glossary*quality*README.org`: Quality terminology.
- [x] `guides*quality*` (3): code-review-standards, quality-metrics,
  technical-debt-management.
- [x] `playbooks*quality*` (4): quality-review, tech-debt-remediation,
  release-quality-gate, README.
- [x] `checklists*quality*` (4): quality-gate, release-readiness,
  tech-debt-triage, README.
- [x] `templates*quality*` (4): quality-report, tech-debt-register,
  quality-dashboard, README.
- [x] `learning-paths*quality*README.org`: Three-tier learning path.
- [x] `references*quality*README.org`: Quick-reference material.
- [x] `prompts*quality-ai-workflows.org`: AI workflows for quality.

### [x] Accessibility Engineering — Complete (all 9 document types)

- [x] `handbooks*accessibility*README.org`: Accessibility Engineering Handbook.
- [x] `glossary*accessibility*README.org`: Accessibility terminology.
- [x] `guides*accessibility*` (6 + README): semantic-html,
  keyboard-accessibility, accessible-forms, aria-patterns,
  colour-and-contrast, screen-reader-testing.
- [x] `playbooks*accessibility-review*README.org`: Accessibility review workflow.
- [x] `checklists*accessibility*` (4): wcag-audit, pr-review,
  design-review, README.
- [x] `templates*accessibility*` (3): accessibility-report,
  accessibility-statement, README.
- [x] `learning-paths*accessibility*README.org`: Three-tier learning path.
- [x] `references*accessibility*README.org`: Quick-reference material.
- [x] `prompts*accessibility-ai-workflows.org`: AI workflows for accessibility.



## Future Capabilities

Additional capabilities to be developed as the community grows:

- Platform Engineering
- DevOps
- Testing
- Observability
- Performance Engineering
- Distributed Systems
- API Design
- Frontend Engineering
- Backend Engineering
- Data Engineering
- Site Reliability Engineering
- Engineering Leadership

## Development Approach

Each capability should:

1. Define its scope and boundaries.
2. Identify related capabilities and cross-references.
3. Build incrementally: handbook → glossary → guides → playbooks → checklists → templates → learning paths → references → AI workflows.
4. Include AI workflows alongside traditional documentation.
5. Pass style and link validation before release.

Priority should follow organizational need rather than attempting to
build all capabilities simultaneously.

## Lessons Learned

- The capability template scaled well from 2 to 6 capabilities.
- Rails capability demonstrated that technology-specific capabilities need more guides than cross-cutting ones.
- AI workflows are most useful when they reference specific guides and patterns within the same capability.
- Security and Quality capabilities benefited from tight cross-referencing with Rails (e.g., Rails security checklist).
- Building capabilities in parallel (Rails, Security, AI, Quality) was more efficient than sequential builds.
- Accessibility demonstrated that a complete capability can be built efficiently by following the established template.
- Filling document-type gaps later (Security templates, AI playbooks) is possible but less efficient than building them
  alongside the initial content.

# Phase 4 — AI Engineering Framework

Develop AI-native engineering practices that integrate AI throughout
the engineering lifecycle.

## Status

[x] ***Complete*** — The AI Engineering capability is fully built out
    across all nine document types. All six cross-cutting AI topics
    (agentic workflows, collaboration patterns, human review strategies,
    evaluation frameworks, verification workflows, knowledge extraction)
    have been developed as guides and playbooks. Domain-specific AI
    workflows exist for Engineering, Architecture, Rails, Security,
    Quality and Accessibility. All Phase 4 deliverables are published.

## Objectives

- Establish context engineering standards.
- Define AI collaboration patterns.
- Create review and verification workflows.
- Provide practical guidance for AI-assisted engineering.
- Build AI evaluation and verification frameworks.

## Completed

- [x] `handbooks/ai*README.org`: AI Engineering Handbook — principles, context engineering, workflow patterns, verification.
- [x] `glossary*ai*README.org`: AI terminology.
- [x] `guides*ai*prompt-engineering.org`: Prompt engineering principles and patterns.
- [x] `guides*ai*context-engineering.org`: Context engineering with categories and templates.
- [x] `guides*ai*ai-safety.org`: AI safety practices and human oversight.
- [x] `checklists*ai-usage.org`: Verification checklist for AI-generated output.
- [x] `learning-paths/ai*README.org`: Three-tier learning path.
- [x] `references*ai*README.org`: Quick-reference material.
- [x] `prompts*engineering-ai-workflows.org`: AI workflows for code review, design exploration, refactoring.
- [x] `prompts*architecture-ai-workflows.org`: AI workflows for trade-off analysis, ADR drafting, pattern selection.
- [x] `prompts*rails-ai-workflows.org`: AI workflows for Rails model generation, API development, testing.
- [x] `prompts*security-ai-workflows.org`: AI workflows for vulnerability identification, threat modeling.
- [x] `playbooks*ai*ai-assisted-code-review.org`: AI-assisted code review workflow.
- [x] `playbooks*ai*ai-assisted-architecture-review.org`: AI-assisted architecture review workflow.
- [x] `playbooks*ai*ai-pair-programming.org`: AI pair programming workflow.
- [x] `templates*ai*context-pack.org`: Context pack template for AI assistants.
- [x] `templates*ai*prompt-template.org`: Standard prompt structure template.
- [x] `templates*ai*ai-review-response.org`: AI review findings documentation template.
- [x] `prompts*ai-ai-workflows.org`: AI workflows for AI engineering.
- [x] `prompts*quality-ai-workflows.org`: AI workflows for quality engineering.
- [x] `prompts*accessibility-ai-workflows.org`: AI workflows for accessibility engineering.
- [x] `prompts*README.org`: Index of all AI workflow documents.

## Completed (added)

- [x] `guides*ai*agentic-workflows.org`: Patterns for multi-step AI-assisted engineering workflows.
- [x] `guides*ai*collaboration-patterns.org`: How engineers and AI interact in different contexts.
- [x] `guides*ai*human-review-strategies.org`: When and how to review AI output effectively.
- [x] `guides*ai*evaluation-frameworks.org`: Frameworks for measuring AI output quality and reliability.
- [x] `playbooks*ai*verification-workflows.org`: Systematic verification of AI-generated code, architecture and documentation.
- [x] `guides*ai*knowledge-extraction.org`: Using AI to extract and structure engineering knowledge.

## Long-term Goal

Provide practical guidance for integrating AI throughout the engineering
lifecycle, establishing AI-assisted engineering as a core organizational
capability.

# Phase 5 — Learning Framework

Build structured learning experiences for every capability.

## Status

[x] ***In Progress*** — Beginner, intermediate and advanced learning
    paths exist for Engineering, Architecture, Rails, Security, AI
    Engineering, Engineering Quality, and Accessibility Engineering.
    All seven capabilities have structured learning paths with topics,
    suggested projects and assessment criteria. The next step is to
    add practical exercises aligned with each level, formal competency
    assessments, and cross-capability learning sequences.

## Objectives

Develop standardized learning paths that support progressive skill
development.

## Completed

- [x] `learning-paths*engineering*README.org`: Three-tier learning path for Engineering Fundamentals.
- [x] `learning-paths*architecture*README.org`: Three-tier learning path for Software Architecture.
- [x] `learning-paths*rails*README.org`: Three-tier learning path for Rails Engineering.
- [x] `learning-paths*security*README.org`: Three-tier learning path for Security Engineering.
- [x] `learning-paths*ai*README.org`: Three-tier learning path for AI Engineering.
- [x] `learning-paths*quality*README.org`: Three-tier learning path for Engineering Quality.

## Next Steps

Each capability should eventually include:

- [ ] Practical exercises aligned with learning path levels.
- [ ] Suggested projects for portfolio building.
- [ ] Reading lists with curated resources.
- [ ] Competency assessments to validate skill progression.
- [ ] Cross-capability learning sequences (e.g., Engineering → Architecture → Rails).

The framework should support both self-paced learning and organizational
training.

## Lessons Learned

- Three-tier structure (beginner, intermediate, advanced) works well but needs concrete exercises to be actionable.
- Learning paths are more useful when they reference specific guides and playbooks within the capability.

# Phase 6 — Framework Tooling

Develop tooling that improves authoring, validation and discovery.

## Status

[x] ***Substantially Complete*** — Validation tooling (6a) and knowledge
    graph tooling (6c) are fully implemented. Generator tooling (6b)
    remains to be built. All tooling runs locally via `make` commands
    and in CI via GitHub Actions.

## Objectives

- Automate repetitive documentation tasks.
- Enforce style and structural consistency.
- Improve knowledge discovery and navigation.
- Support AI context packaging for coding agents.
- Provide quality gates for contributions.

## Deliverables

### Phase 6a — Validation Tooling (Complete)

Initial tooling focused on correctness and consistency:

- [x] Link validation: Verify all markdown cross-references resolve to existing files.
- [x] Style validation: Check documents against [Style Guide](./style-guide.md) rules (heading levels, metadata, front matter, filename conventions).
- [x] Glossary validation: Ensure all glossary entries have required fields, non-empty definitions, and no duplicate terms.
- [x] Bullet syntax linting: Detect incorrect list formatting.
- [x] Metadata validation: Verify required `title:` and `description:` front matter.
- [x] TOC validation: Ensure TOC.md entries match actual file inventory.
- [x] Validation runner: `make validate` runs all validators in sequence with summary output.

### Phase 6b — Generator Tooling (Not Started)

Tooling for scaffolding new capabilities and documents:

- [ ] Capability generator: Scaffold a new capability (handbook, glossary, guide stubs, learning path).
- [ ] Document type generators: Create new handbook, guide, playbook, checklist, reference stubs with correct metadata.
- [ ] Playbook generator: Scaffold playbooks with workflow sections.
- [ ] Learning path generator: Scaffold three-tier learning paths.

### Phase 6c — Knowledge Graph Tooling (Partial)

Tooling for discovery and navigation:

- [x] Cross-reference extraction: Parse all documents and extract markdown links.
- [x] Knowledge graph generation: Produce machine-readable graph (JSON + Graphviz DOT) of document relationships.
- [x] Capability completeness report: Per-capability report of which document types are present and missing.
- [ ] AI context packaging: Generate condensed context packs for AI assistants from selected documents.
- [ ] Search indexing: Build search index across all documents (handled by Zola for the site; standalone index pending).

## Development Approach

1. Build validation tooling first — it establishes quality gates that all
   other work must pass.
2. Use existing documents as test fixtures for validation rules.
3. Generators should produce templates that pass validation by default.
4. Knowledge graph tooling depends on consistent metadata and
   cross-references, so it comes after validation.
5. All tooling should run locally (CLI) and in CI.
6. Prefer standalone scripts over framework dependencies.

Tooling should automate repetitive work while preserving editorial
quality.

## Lessons Learned

- Python scripts with no external dependencies are easy to run in CI and locally.
- `make` targets provide a simple, discoverable interface for all tooling.
- Running validation in CI before building the site catches broken links
  before deployment.
- The knowledge graph generator revealed missing cross-references and
  capability gaps that were not obvious from directory listings.
- Validators should be strict during development but can be configured
  to allow selective exceptions for known issues.

# Phase 7 — Platform

Expand the framework into a complete engineering knowledge platform.

## Status

[x] ***In Progress*** — A Zola-based static site (Phase 7a) is fully
    operational with custom theme, full-text search, and GitHub Pages
    deployment via GitHub Actions. The static site serves all framework
    content with navigation by capability and document type. Remaining
    platform work focuses on the knowledge graph UI, AI integration,
    and advanced platform features.

## Objectives

- Improve discoverability of engineering knowledge.
- Provide interactive and visual access to the knowledge graph.
- Integrate with AI assistants and development workflows.
- Enable non-technical stakeholders to benefit from the knowledge.

## Deliverables

### Phase 7a — Static Site (Complete)

- [x] Zola static site generator integration with custom theme.
- [x] Full-text search across all documents (Zola search index with elasticlunr).
- [x] Navigation by capability and document type.
- [x] Cross-cutting topic indexes via TOC.md.
- [x] Responsive design with custom CSS.
- [x] GitHub Actions CI/CD pipeline: validate → build graph → prepare content → build site → deploy to GitHub Pages.
- [x] `make site` and `make serve` commands for local preview.

### Phase 7b — Knowledge Graph UI

- [ ] Interactive graph visualization of document relationships.
- [ ] Drill-down from capability to individual documents.
- [ ] Search with graph context (show related documents).

### Phase 7c — AI Integration

- [x] MCP server exposing framework knowledge to AI assistants via stdio transport.
  - Resources: capabilities, documents, search, knowledge graph stats.
  - Tools: context pack generation, document search, related documents, capability reports.
  - Prompts: engineering review, architecture review, Rails development templates.
- [x] AI context packaging API (CLI tool plus MCP tool).
- [ ] Automatic context injection for coding agents.

### Phase 7d — Platform Features

- [ ] Interactive learning paths with progress tracking.
- [ ] Documentation analytics (coverage, freshness, gaps).
- [ ] Versioned releases with changelog integration.
- [ ] Community portal for discussion and proposals.

## Development Approach

1. Static site was built alongside Phase 6 tooling — validation and site
   generation share the same CI pipeline.
2. Knowledge graph UI depends on Phase 6c (graph generation — already built).
3. AI integration should use the knowledge graph as its data source.
4. Community portal is last — it requires critical mass of users.

## Lessons Learned

- Zola's `_index.md` convention maps well to the directory-based
  capability structure.
- The `prepare-site-content.py` script is essential for fixing relative
  links between flat-file structure and Zola's URL hierarchy.
- Building the site in CI ensures broken links are caught before deployment.
- Full-text search was valuable immediately — should be included from the
  start in any future static site setup.

# Phase 8 — Community

Grow an active open-source community around the framework.

## Status

[ ] ***Not Started*** — Community growth depends on having stable
    documentation and tooling that others can build on. The
    CONTRIBUTING.md document establishes initial contribution
    guidelines. GitHub Issues and Discussions are enabled.

## Objectives

- Encourage community contributions.
- Establish review processes.
- Create mentoring resources.
- Develop maintainership practices.
- Foster engineering discussions.
- Share lessons learned from real-world adoption.
- Build a diverse contributor base.

## Deliverables

### Onboarding

- [ ] `CONTRIBUTING.org`: Already published (see [./CONTRIBUTING.md](./contributing.md)).
- [ ] Good first issue labels for new contributors.
- [ ] Contributor onboarding guide with step-by-step walkthrough.
- [ ] Community expectations and code of conduct.

### Review and Quality

- [ ] PR review checklist for community contributions.
- [ ] Maintainer decision-making framework.
- [ ] Release process and versioning policy.
- [ ] Advisory board for strategic direction.

### Engagement

- [ ] Community discussion forum (GitHub Discussions).
- [ ] Monthly community calls or async updates.
- [ ] Case studies and adoption stories.
- [ ] Community-contributed capabilities.

## Development Approach

1. Start with clear contribution guidelines and low-friction PR processes.
2. Use good-first-issue labels to lower the barrier to entry.
3. Build maintainer capacity before scaling contributor base.
4. Community contributions should follow the same quality standards as
   core contributions.
5. Recognise and celebrate community contributions.

The framework should evolve through practical engineering experience
rather than theoretical completeness.

# Phase 9 — Open Standard

Establish the Engineering Knowledge Framework as an open standard for
engineering knowledge management.

## Status

[ ] ***Future*** — This phase depends on community adoption and
    real-world validation. The framework must prove itself across
    multiple organizations before standardisation is meaningful.

## Objectives

- Define an interoperable specification for engineering knowledge.
- Enable third-party tooling and ecosystem development.
- Allow organizations to adopt the framework while maintaining
  compatibility with the broader ecosystem.

## Deliverables

### Specification

- [ ] Engineering Knowledge Specification (EKS): Define the formal specification.
- [ ] Standardized metadata schema for all document types.
- [ ] Capability specification format.
- [ ] Document interoperability contracts.

### Ecosystem

- [ ] Reference implementation of the specification.
- [ ] Repository validation tools for specification compliance.
- [ ] Third-party tooling SDK.
- [ ] Community-contributed integrations.

### Governance

- [ ] Specification versioning and evolution process.
- [ ] Conformance testing framework.
- [ ] Advisory board representing adopters.

## Development Approach

1. Standardisation should follow adoption, not precede it.
2. Extract the specification from the reference implementation.
3. Keep the specification minimal — define only what must be
   interoperable.
4. Version the specification independently of the framework content.
5. Provide migration guides for breaking changes.

# Cross-cutting Initiatives

The following initiatives span multiple roadmap phases.

## AI Integration

Every capability should eventually include:

- AI-assisted workflows.
- AI review guidance.
- Prompt patterns.
- Context engineering recommendations.
- Verification strategies.

## Continuous Improvement

Regularly refine:

- Repository architecture.
- Writing standards.
- Templates.
- Learning paths.
- Contribution workflow.

Lessons learned from adopting the framework should feed back into the
framework itself.

## Knowledge Preservation

Prioritize capturing:

- Architectural decisions.
- Project retrospectives.
- Lessons learned.
- Engineering standards.
- Decision frameworks.
- Organizational practices.

Institutional knowledge should become reusable organizational assets.

# Measuring Progress

Progress should be measured by:

- Quality of engineering guidance.
- Reusability of knowledge.
- Completeness of engineering capabilities.
- Ease of adoption.
- AI effectiveness.
- Community participation.
- Long-term maintainability.

Document count is **not** a success metric.

# Near-term Priorities

Current priorities are:

1. [x] Build Engineering Fundamentals capability (Phase 2a).
2. [x] Build Software Architecture capability (Phase 2b).
3. [x] Create reusable document templates for all document types.
4. [x] Develop Rails Engineering capability (Phase 3).
5. [x] Develop Security Engineering capability (Phase 3).
6. [x] Develop AI Engineering capability (Phase 3/4).
7. [x] Develop Engineering Quality capability (Phase 3).
8. [x] Develop Accessibility Engineering capability (Phase 3).
9. [x] Establish RFC and ADR processes for framework evolution (see [adr/](./adr/0001-capability-model.md) directory and [ADR template](./templates/adr/README.md)).
10. [ ] Add practical exercises, formal assessments and cross-capability learning sequences to learning paths (Phase 5).
11. [x] Develop AI agentic workflows and evaluation frameworks (Phase 4).
12. [x] Build validation tooling — link validation, style validation, glossary validation, TOC validation (Phase 6a).
13. [x] Build knowledge graph generation tooling (Phase 6c).
14. [ ] Build generator tooling — capability scaffolding, document type generators (Phase 6b).
15. [ ] Build knowledge graph UI visualization (Phase 7b).
16. [x] Build AI context packaging for AI assistants — CLI tool + MCP server (Phase 6c/7c).
17. [ ] Explore community engagement and contribution workflows (Phase 8).

These initiatives build on the completed foundation. See [CHANGELOG](./changelog.md) for
completed milestones.

# Future Evolution

This roadmap intentionally focuses on enduring direction rather than
specific release schedules.

As the framework matures, priorities will evolve based on:

- Community feedback.
- Real-world adoption.
- Advances in AI-assisted engineering.
- Lessons learned from building new capabilities.
- Improvements to engineering practices.

The roadmap should remain flexible while preserving the framework's core
mission.

# Related Documents

- [Strategy](./strategy.md)
- [CLAUDE.md](./CLAUDE.md)
- [Document Types](./document-types.md)
- [Style Guide](./style-guide.md)
- [Contributing](./contributing.md)
- [Changelog](./changelog.md)
- [Architecture](./architecture.md)
- [Repository Overview](../README.md)
