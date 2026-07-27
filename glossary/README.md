+++
title = "Glossary"
description = "Canonical engineering terminology used throughout the Engineering Knowledge Base"
+++


# Purpose

The Glossary provides the canonical vocabulary used throughout the
Engineering Knowledge Base.

Its objectives are to:

- Establish consistent terminology.
- Reduce ambiguity.
- Improve communication.
- Standardize documentation.
- Provide a shared language for engineers and AI assistants.

Whenever a concept has a glossary entry, that definition should be
considered authoritative throughout the repository.

# Philosophy

Engineering documentation is only as effective as the language it uses.

Consistent terminology improves:

- Readability
- Searchability
- Cross-referencing
- AI-assisted authoring
- Organizational communication

The glossary should define concepts rather than duplicate handbook
content.

# Organization

Glossaries are organized by engineering capability.

```

glossary/

├── engineering/
├── architecture/
├── rails/
├── security/
├── accessibility/
├── testing/
└── ai/

```

Each capability owns its own vocabulary.

Repository-wide terminology belongs in the Engineering Glossary.

# Available Glossaries

| Glossary | Purpose |
| --- | --- |
|----------------+-----------------------------------------|
| [Engineering](engineering/README/) | Repository-wide engineering terminology |
| --- | --- |
| [Architecture](architecture/README/) | Software architecture concepts |
| [Rails](rails/README/) | Ruby on Rails terminology |
| [Security](security/README/) | Security concepts and terminology |
| [Accessibility](accessibility/README/) | Accessibility terminology |
| Testing (not yet developed) | Testing vocabulary |
| [AI Engineering](ai/README/) | AI engineering terminology |

# When to Add a Glossary Entry

Add a glossary entry when:

- A concept appears across multiple documents.
- Different people might interpret the term differently.
- The organization has adopted a preferred definition.
- AI should consistently use the same terminology.

Do not add glossary entries for concepts that are obvious, highly
localized or unlikely to be reused.

# Writing Guidelines

Every glossary entry should include:

- Definition
- Context
- Related terms
- References to relevant documentation

Definitions should be concise.

Handbooks should explain concepts in depth.

# Related Documents

- [Document Types](../document-types/)
- [Style Guide](../style-guide/)
- [Contributing](../contributing/)
