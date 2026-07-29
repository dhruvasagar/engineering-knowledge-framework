# Purpose

Slice plans are working documents that describe planned changes to the
framework itself.

They are deliberately *not* part of the published knowledge base:

- They are time-bound, not timeless.
- They describe the framework's own construction, not engineering practice.
- They become obsolete once the work lands.

For this reason `docs/` is excluded from the site build, the knowledge
graph, context packs and TOC validation.

Durable outcomes from a slice plan belong elsewhere:

- Decisions with lasting consequence become [ADRs](../../adr/).
- Completed deliverables are recorded in the [Changelog](../../changelog.md).
- Direction and phasing live in the [Roadmap](../../roadmap.md).

# Relationship to the Roadmap

The [Roadmap](../../roadmap.md) describes *what* the framework intends to
build and in what order.

A slice plan describes *how* a specific piece of that work will be
executed — the concrete defects, the sequence, the acceptance criteria.

A slice plan may span multiple roadmap phases, and a roadmap phase may
be delivered by multiple slice plans.

# Naming

Slice plans are numbered and named after the outcome they produce:

```text
docs/slice-plans/0001-ai-native-tooling.md
```

# Index

| Plan                                             | Status      | Summary                                                          |
|--------------------------------------------------|-------------|------------------------------------------------------------------|
| [0001 — AI-Native Tooling](./0001-ai-native-tooling.md) | In Progress | Make framework knowledge executable in developer and AI workflows |

# Related Documents

- [Roadmap](../../roadmap.md)
- [Changelog](../../changelog.md)
- [Architecture](../../architecture.md)
- [Contributing](../../contributing.md)
