# Purpose

Ruby on Rails is a web application framework that emphasizes convention
over configuration, developer productivity and elegant code.

This handbook defines the principles, standards and patterns for
building Rails applications within this organization.

It builds upon the [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md) and
[Software Architecture Handbook](../../handbooks/architecture/README.md), applying their principles to the Rails
context.

# Scope

This handbook covers:

- Rails philosophy and core principles.
- Application structure and code organization.
- Models, views, controllers and service layer conventions.
- Testing strategy for Rails applications.
- Common patterns and anti-patterns.
- Decision frameworks for Rails-specific choices.
- AI integration in Rails development.

This document focuses on enduring Rails principles rather than
version-specific features. For version-specific guidance, see the
[Rails References](../../references/rails/README.md).

# Rails Philosophy

## Convention over Configuration

Rails provides sensible defaults for every aspect of application
structure, naming and behaviour.

Engineers should follow Rails conventions unless there is a clear,
documented reason to deviate. Conventions reduce decision fatigue, make
code predictable and enable developers to move between projects quickly.

## Don't Repeat Yourself (DRY)

Every piece of knowledge should have a single, unambiguous
representation within the system.

Duplication increases maintenance cost and creates opportunities for
inconsistency. When modifying behaviour, every duplicated location must
be updated — a process that is error-prone and容易遗漏.

## MVC Architecture

Rails follows the Model-View-Controller architectural pattern.

| Layer      | Responsibility                                            |
|------------|-----------------------------------------------------------|
| Model      | Business logic, data validation, persistence.             |
| View       | Presentation logic, user interface rendering.             |
| Controller | Request handling, parameter parsing, response generation. |

Controllers should be thin. Models should capture domain logic. Views
should contain minimal logic.

# Principles

## Thin Controllers

Controllers should only orchestrate: parse parameters, invoke business
logic, and render responses.

Business logic belongs in models, service objects or other domain
classes — not in controllers.

A controller action should typically be three to five lines.

## Fat Models, but Not Too Fat

Models naturally become the default home for business logic.

However, when a model exceeds a reasonable size, extract cohesive
groups of behaviour into separate classes: service objects,
value objects, policy objects or form objects.

A model that grows beyond a few hundred lines is a signal that
responsibilities should be extracted.

## Keep the View Dumb

Views should contain minimal logic.

Logic in views is hard to test, hard to maintain and easy to overlook
during refactoring.

Use presenters, decorators or view objects for presentation logic.
Use helpers sparingly and only for view-level formatting.

## Prefer Service Objects for Complex Operations

When an operation involves multiple models, external services or
complex orchestration, extract it into a service object.

A service object:

- Has a single responsibility (one public method).
- Is named after the operation it performs.
- Is easy to test in isolation.
- Can be reused across controllers, jobs and Rake tasks.

## Database as a Detail

Rails' ActiveRecord pattern makes the database feel like an invisible
part of the application.

Resist this abstraction. Design database schema deliberately.
Understand query performance. Use migrations to evolve schema
incrementally.

# Code Organization

## Application Structure

Follow Rails defaults for the standard directories. Custom code
belongs in `app*` with clear naming.

```
app*
  controllers/
  models/
  views/
  services/       # Service objects
  forms/          # Form objects
  policies/       # Authorization policies
  presenters/     # View presentation logic
  serializers/    # JSON serialization
  values/         # Value objects
  queries/        # Query objects
```

## Naming Conventions

Follow Rails naming conventions consistently.

| Concept    | Convention                        | Example                  |
|------------|-----------------------------------|--------------------------|
| Model      | Singular, CamelCase               | `UserAccount`            |
| Table      | Plural, snake_case                | `user_accounts`          |
| Controller | Plural, CamelCase with Controller | `UserAccountsController` |
| Service    | Named after operation             | `RegisterUser`           |
| Migration  | Descriptive snake_case            | `add_email_to_users`     |

# Standards

## Models

- Use validations to enforce data integrity.
- Use ActiveRecord callbacks sparingly. Prefer explicit service objects
  for side effects.
- Define scopes for common queries.
- Keep associations explicit and well-named.

## Migrations

- Each migration should change one logical thing.
- Never edit a migration that has been merged.
- Use reversible migrations whenever possible.
- Write a `down` method for every migration that could be rolled back.

## Routes

- Use resourceful routes (`resources`) by default.
- Limit nesting to one level deep.
- Use `member` and `collection` blocks sparingly.
- Keep `routes.rb` organized and commented.

## API Development

- Use namespaced controllers for API endpoints (`Api::V1::`).
- Use serializers or jbuilder for response formatting.
- Version APIs explicitly in the URL path.
- Follow the API design standards in the
  [API Design Guide](../../guides/architecture/api-design.md).

# Testing

## Testing Philosophy

- Test behaviour, not implementation.
- Prefer request specs over controller specs.
- Use factory patterns for test data.
- Keep tests fast and reliable.

## Test Distribution

Follow the testing principles in the
[Testing Strategies Guide](../../guides/engineering/testing-strategies.md).

For Rails specifically:

| Test Type     | What to Test                        | Speed    |
|---------------|-------------------------------------|----------|
| Model specs   | Validations, associations, scopes.  | Fast     |
| Request specs | Controller behaviour, status codes, | Moderate |
|               | response format.                    |          |
| Feature specs | Critical user journeys.             | Slow     |
| Unit tests    | Service objects, form objects,      | Fast     |
|               | presenters.                         |          |

# Patterns

## Service Objects

Use service objects to encapsulate complex operations.

```
class RegisterUser
  def initialize(params)
    @params = params
  end

  def call
    # Business logic here
  end
end
```

## Form Objects

Use form objects to encapsulate form validation and data processing for
complex forms that do not map directly to a single model.

## Query Objects

Use query objects to encapsulate complex database queries that do not
belong in a model scope.

## Policy Objects

Use policy objects to encapsulate authorization logic.

# Anti-patterns

## Fat Controllers

Controllers that exceed five to ten lines per action indicate that
business logic needs to be extracted.

## Callback Overuse

ActiveRecord callbacks (`after_save`, `before_update`) create implicit
dependencies that make code hard to reason about and test.

Prefer explicit service objects over callbacks for side effects.

## Magic Strings

Hard-coded values, status strings and configuration constants embedded
in business logic should be extracted into constants, enums or
configuration classes.

## Skipping Tests

Every non-trivial feature or fix should include tests.

Skipping tests creates technical debt that accumulates through
unexpected regressions and reduced confidence in changes.

# Decision Frameworks

## When to Use a Service Object

Use a service object when:

- The operation involves multiple models.
- The operation calls external services or APIs.
- The operation has complex error handling.
- The operation is invoked from multiple entry points (controller,
  job, Rake task).

## When to Introduce a Gem

Before adding a gem, ask:

1. What problem does this gem solve?
2. Could we solve it with a simple class?
3. Is the gem well-maintained and documented?
4. Does the gem add unnecessary complexity?
5. Is the gem compatible with our Rails version?

Prefer a simple custom implementation over a heavyweight gem for small
concerns.

# AI Integration

AI assistants can assist with Rails development through:

- Generating models, migrations and controllers from descriptions.
- Writing tests for existing code.
- Suggesting refactoring opportunities.
- Reviewing Rails code for convention compliance.
- Debugging errors with Rails-specific knowledge.
- Automating Ruby and Rails upgrades via the
  [Ruby Upgrade Toolkit](https://github.com/dhruvasagar/ruby-upgrade-toolkit).

When using AI for Rails development, provide:

- The Rails version and Ruby version.
- Relevant models, routes and schema.
- The specific problem or task.
- Existing conventions or patterns to follow.

See the [AI Engineering Handbook](../../handbooks/ai/README.md) for general AI workflow guidance.

### AI-Assisted Upgrades

The [Ruby Upgrade Toolkit](https://github.com/dhruvasagar/ruby-upgrade-toolkit)
is a Claude Code plugin that fully automates Ruby and Rails version
upgrades. It follows a phased methodology — audit, plan, fix, verify
— with three workflow modes:

- **Fully automated**: `/ruby-upgrade-toolkit:upgrade ruby:X.Y.Z rails:X.Y`
- **Review-then-automate**: audit → plan → upgrade
- **Per-phase control**: audit → plan → fix next (iterate)

See the [Rails Upgrade Playbook](../../playbooks/rails/upgrade.md) for the
detailed workflow and usage guide.

# Capability Map

This handbook is the entry point for the Rails Engineering capability.
The following documents form the complete capability:

## Handbooks

- [Rails Engineering Handbook](./README.md) — This document. Principles, standards,
  and philosophy for Rails development.

## Glossaries

- [Rails Glossary](../../glossary/rails/README.md) — Canonical Rails terminology (ActiveRecord,
  controller, service object, view, etc.).

## Guides

- [Service Objects](../../guides/rails/service-objects.md) — When and how to use service objects,
  structure, patterns and testing.
- [Testing Rails Applications](../../guides/rails/testing.md) — Test distribution, model*request*
  system specs, factory patterns.
- [Rails Audit Guide](../../guides/rails/audit-guide.md) — Systematic code quality, performance,
  database and security auditing.
- [Rails Project Standards](../../guides/rails/project-standards.md) — Mandatory tooling baseline and
  CI/CD configuration for every Rails project.
- [ActiveRecord Patterns and Query Optimization](../../guides/rails/active-record.md) — Scopes, query
  optimization, N+1 prevention, indexing.
- [API Development with Rails](../../guides/rails/api-development.md) — API-only setup, serialization,
  versioning, authentication and testing.
- [Background Jobs](../../guides/rails/background-jobs.md) — Framework selection (Sidekiq, GoodJob,
  SolidQueue), job design, error handling, monitoring.
- [Authentication and Authorization](../../guides/rails/authentication-authorization.md) — Devise setup, Pundit
  policies, role-based authorization.

## Playbooks

- [Rails Upgrade Playbook](../../playbooks/rails/upgrade.md) — Step-by-step Rails version upgrade
  workflow with rollback plan.
- [Rails Deployment Playbook](../../playbooks/rails/deployment.md) — Safe deployment with database
  migration safety, zero-downtime patterns.

## Checklists

- [Rails Pull Request Checklist](../../checklists/rails/pull-request.md) — Code quality, testing,
  security and migration safety for every PR.
- [Rails Security Review Checklist](../../checklists/rails/security-review.md) — Authentication,
  authorization, data protection and dependency verification.
- [Rails Deployment Checklist](../../checklists/rails/deployment.md) — Pre-deployment, migration
  safety and post-deployment verification.

## Templates

- [Service Object Template](../../templates/rails/service-object.md) — Reusable service object with
  result object pattern.
- [Form Object Template](../../templates/rails/form-object.md) — Form object with ActiveModel
  integration.
- [Query Object Template](../../templates/rails/query-object.md) — Composable query object with scope
  chaining.
- [Policy Object Template](../../templates/rails/policy-object.md) — Authorization policy with Pundit
  conventions.

## Learning Paths

- [Rails Learning Paths](../../learning-paths/rails/README.md) — Beginner, intermediate and advanced
  tracks with topics, projects and assessment.

## References

- [Rails References](../../references/rails/README.md) — Quick lookup: conventions, generators,
  test commands, gems, HTTP codes.

## AI Workflows

- [AI Workflows for Rails](../../prompts/rails-ai-workflows.md) — Prompt patterns for model
  generation, API development, testing and debugging.

# Related Documents

- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
- [Software Architecture Handbook](../../handbooks/architecture/README.md)
- [Rails Glossary](../../glossary/rails/README.md)
- [API Design Guide](../../guides/architecture/api-design.md)
- [Code Review Playbook](../../playbooks/code-review/README.md)
- [Testing Strategies Guide](../../guides/engineering/testing-strategies.md)
