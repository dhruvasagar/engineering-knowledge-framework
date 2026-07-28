# Purpose

Code organization is the practice of structuring source code into
modules, directories and files that make the system easier to
understand, navigate and change.

Well-organized code communicates intent through structure. Poorly
organized code obscures logic behind arbitrary arrangement.

This guide explains the principles and patterns for organizing code
effectively, independent of programming language or framework.

# Background

As systems grow, the cost of poor organization compounds.

Engineers spend more time navigating code than writing it. The
structure of the codebase directly affects how quickly engineers can:

- Find relevant code.
- Understand how components relate.
- Assess the impact of changes.
- Onboard new team members.

Code organization is the first line of defence against accidental
complexity.

# Principles

## Organize by Feature, Not by Layer

Group code by the feature or domain concept it implements, rather than
by the technical layer it belongs to.

Feature-based organization:

- Keeps related code together.
- Makes features self-contained and independently evolvable.
- Reduces the cognitive load of jumping between directories.
- Enables teams to own features end-to-end.

***Good:***

```
src/
  users/
    UserRegistration/
      registration_controller.rb
      registration_service.rb
      registration_mailer.rb
      registration_test.rb
  billing/
    InvoiceGeneration/
      invoice_generator.rb
      invoice_presenter.rb
      invoice_generator_test.rb
```

***Avoid:***

```
src/
  controllers/
    users_controller.rb
    billing_controller.rb
  models/
    user.rb
    invoice.rb
  services/
    registration_service.rb
    invoice_generator.rb
```

## Establish Clear Boundaries

Every module or directory should have a clearly defined responsibility.

Ask:

- What belongs here?
- What does not belong here?
- What depends on this module?
- What does this module depend on?

Document the boundary in a README or module comment when the
responsibility is not obvious from the name.

## Limit Module Size

A module that grows too large loses cohesion and becomes hard to
understand.

Signs a module should be split:

- It has multiple unrelated responsibilities.
- It exceeds a reasonable size for the language and context.
- Its name no longer accurately describes its contents.
- Changes frequently touch only part of the module.

When splitting, prefer extracting cohesive subsets into new modules
rather than creating a generic "utilities" bucket.

## Keep Dependencies Flowing in One Direction

Dependencies should form an acyclic graph.

Higher-level modules may depend on lower-level modules, but lower-level
modules should never depend on higher-level ones.

This principle applies at every scale: package, module, class, and
function.

## Make the Structure Explain the Architecture

The directory tree should tell the story of the system.

A new engineer should be able to understand the system's architecture by
browsing the directory structure. If the architecture is not visible in
the structure, the organization is hiding the design.

# Patterns

## Package by Feature

Organize code around business features or domain concepts.

Suitable for most applications, especially those with clear domain
boundaries.

```
src/
  checkout/
  product_catalog/
  user_accounts/
  notifications/
```

Each package contains all layers (controllers, models, services, tests)
needed for that feature.

## Package by Layer

Organize code by technical role (controllers, models, services).

Suitable for small applications or systems with very stable layer
boundaries. Generally not recommended for larger systems.

```
src/
  controllers/
  models/
  services/
  repositories/
```

## Package by Component

Organize code around independently deployable or replaceable
components.

Suitable for systems with strong separation between major subsystems.

```
src/
  payment_processing/
  inventory_management/
  shipping/
  analytics/
```

# Common Anti-patterns

## The Utils Module

A module named `utils`, `helpers`, or `misc` is a sign of missing
structure.

Every function in a utils module belongs somewhere more specific. Find
that somewhere.

## Deep Nesting

Deep directory hierarchies increase navigation cost.

Prefer wide, shallow structures over deep, narrow ones.

A good rule of thumb: no more than three or four levels of nesting for
application code.

## Circular Dependencies

Two modules that depend on each other create a circular dependency.

Break the cycle by:

- Extracting the shared dependency into a third module.
- Inverting one of the dependencies through an interface.
- Merging the two modules if they are tightly coupled.

## God Modules

A module that grows to encompass unrelated responsibilities becomes a
god module.

Split god modules by extracting cohesive subsets. Each extracted module
should have a single, clear responsibility.

# AI Integration

AI assistants can help with code organization by:

- Analyzing module structure and suggesting reorganizations.
- Detecting circular dependencies in the codebase.
- Identifying candidate modules for extraction.
- Generating README files for module boundaries.

When asking AI for organization advice, provide:

- Current directory structure.
- Module responsibilities.
- Known dependency relationships.
- System architecture context.

# Related Documents

- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
- [Engineering Glossary](../../glossary/engineering/README.md)
- [Code Review Playbook](../../playbooks/code-review/README.md)
