# Purpose

This plan describes how the Engineering Knowledge Framework moves from
*documents that can be read* to *knowledge that executes inside a
developer's workflow*.

The framework currently publishes knowledge well. It does not yet
**reach into a working session**. A static site and an MCP search tool
are both pull mechanisms: they require a developer to stop, decide that
framework knowledge is relevant, and go looking for it. Adoption comes
from push — knowledge that arrives at the decision point without being
requested.

This plan is organized into five layers. Layer 0 repairs the substrate
and is a prerequisite for everything above it. Layers 1 to 4 are
independently valuable and can be sequenced by preference.

# Status

- [x] ***Layer 0*** — Substrate repair
- [ ] ***Layer 1*** — Compile knowledge into a Claude Code plugin
- [ ] ***Layer 2*** — Retrieval that works
- [ ] ***Layer 3*** — Close the lifecycle loop
- [ ] ***Layer 4*** — Conformance

# Background

An audit of the repository on 2026-07-29 found strong prose sitting on a
defective substrate.

## What is working

- Document structure is consistently applied: 76 `# Purpose` sections,
  88 `# Related Documents` sections, 17 `# Anti-patterns` sections.
- Cross-linking is real rather than decorative: the knowledge graph
  contains 1,176 edges across 150 nodes.
- The tooling architecture is the right shape — validators, knowledge
  graph, context packs, MCP server and site build are all present and
  share a CI pipeline.

## What is broken

### Validation reported a false green

`tools/validate-style.py` reported success across 302 files while
checking almost nothing:

| Defect                                                              | Effect                                        |
|---------------------------------------------------------------------|-----------------------------------------------|
| `HEADING_PATTERN` used org-mode syntax (`^\*+\s`)                    | Heading-level validation never matched a `#`  |
| `validate_metadata()` returned `[]` unconditionally                  | Metadata was never checked                    |
| `validate_bullets()` returned `[]` unconditionally                   | Bullet syntax was never checked               |
| `REQUIRED_METADATA` was defined but unused                           | Dead configuration implying a check existed   |

Only the filename check performed real work. The link, glossary and TOC
validators were unaffected — this was specific to the style validator.

### Migration damage the validators could not see

The org-mode to Markdown migration corrupted content silently:

- ***9 destroyed external links*** where `/` became `*`, rendering as
  literal `[[https:*/www.w3.org*TR*WCAG22*][WCAG 2.2 Specification]]`.
  `validate-links.py` only parses `](...)`, so org `[[...][...]]` syntax
  was invisible to it.
- ***11 broken nested code fences***, where an inner ` ```ruby ` closes
  the outer fence early. The AI workflow prompt documents — the ones most
  likely to be copied into an agent — were the worst affected.
- ***Destroyed teaching examples***: the Style Guide's "Bullet Format"
  section had identical `Correct` and `Incorrect` examples, because the
  `*` counterexample was converted to `-` during migration.
- ***Org residue in governance***: `CLAUDE.md` instructed contributors
  using org verbatim markup (`=-=`) and claimed `*` creates a headline in
  Markdown, which is false.

### The AI-native layer was starved of metadata

This is the gap that most directly contradicts the framework's stated
mission.

- ***Zero frontmatter*** across all 150 source documents — no type,
  capability, tags, status or review date.
- Consequently ***150 of 150 knowledge graph nodes had empty
  descriptions***.
- Consequently ***search matched titles and paths only***. Queries for
  `N+1`, `background jobs` and `caching` returned nothing, despite N+1
  being discussed in six documents. The MCP server's `search-knowledge`
  tool inherited the same weakness.
- ***Of roughly 250 code blocks, 4 carried a language tag***, preventing
  syntax highlighting and reliable example extraction.

### Coverage and hygiene

- Only ***7 valid external links*** across roughly 94,000 words, in a
  framework whose quality standard requires references.
- ***No performance or caching knowledge at all*** — zero documents
  mention caching.
- Depth is uneven: Rails has 25 documents; Engineering Fundamentals has 9
  and lacks playbooks, checklists and templates entirely.
- `.org-backup/` tracks ***149 org files*** duplicating the whole tree,
  polluting search for anyone who clones the repository.
- Each tool carries its own divergent copy of `SKIP_DIRS`.

# Layer 0 — Substrate Repair

Everything above this layer depends on documents being machine-readable
and on validation being trustworthy. This layer is mostly mechanical.

## Objectives

- Make `make validate` mean something.
- Make every defect class found in the audit impossible to reintroduce.
- Give every document the metadata that retrieval and compilation need.

## Deliverables

- [x] Exclude `docs/` from the site build, knowledge graph, context packs
      and TOC validation.
- [x] Rewrite `validate-style.py` against Markdown, with 62 tests.
- [x] Add checks for untagged fences, nested fences, malformed tables,
      org residue, mangled URLs and untranslated text.
- [x] Repair the 9 mangled links and 11 nested fences.
- [x] Repair a further 367 lines of path and verbatim corruption found
      during the fence review.
- [x] Repair the Style Guide, `CLAUDE.md` and `README.md` defects.
- [x] Tag all 227 untagged code fences with a language.
- [x] Add YAML frontmatter to all 150 source documents.
- [x] Teach `prepare-site-content.py` and `build-knowledge-graph.py` to
      consume frontmatter.
- [x] Run the rule tests as the first gate in `make validate` and in CI.
- [x] Correct the inaccurate Phase 6a and 6c roadmap claims.

## Frontmatter Schema

```yaml
---
title: Service Objects
description: Encapsulating a single business operation in a dedicated class.
type: guide
capability: rails
status: published
tags: [patterns, refactoring, testability]
last_reviewed: 2026-07-29
---
```

| Field           | Required | Purpose                                                       |
|-----------------|----------|---------------------------------------------------------------|
| `title`         | Yes      | Display name; replaces path-derived titles in the site build   |
| `description`   | Yes      | One-line summary; powers search results and graph nodes        |
| `type`          | Yes      | Document taxonomy; drives plugin compilation targets           |
| `capability`    | Yes      | Owning capability; drives grouping and context pack assembly   |
| `status`        | Yes      | `draft`, `published` or `deprecated`                           |
| `tags`          | No       | Retrieval hints beyond title tokens                            |
| `last_reviewed` | Yes      | Enables staleness reporting; knowledge decays silently without it |

## Acceptance Criteria

- `make validate` fails on a document with an untagged fence, a nested
  fence, org residue, a mangled URL, a skipped heading level or missing
  required frontmatter.
- The validator has tests covering each check, including the org-mode
  heading regression that caused the original false green.
- `knowledge-graph.json` contains a non-empty description for every node.

# Layer 1 — Compile Knowledge into a Claude Code Plugin

The highest-leverage layer. Knowledge that loads itself at the moment of
relevance is qualitatively different from knowledge a developer must go
and find.

## Architectural Principle

***One source, many runtime targets.***

Markdown remains canonical. The site, the MCP server, the plugin, editor
rule files and `AGENTS.md` are all build artifacts compiled from it. No
knowledge is ever authored in a runtime format.

```text
                    knowledge base (markdown + frontmatter)
                                    │
        ┌───────────────┬───────────┼───────────┬──────────────────┐
        ▼               ▼           ▼           ▼                  ▼
   Zola site      MCP server   Claude Code   editor rules    AGENTS.md
                               plugin
```

## Deliverables

- [ ] `tools/build-plugin.py`, compiling the knowledge base into
      `.claude-plugin/`.
- [ ] Guides compile to ***skills***, each with a triggering
      `description` so it loads on demand. This is precisely the
      progressive disclosure the modularity principle was designed for.
- [ ] Playbooks compile to ***agents***, where the playbook body becomes
      the agent's system prompt.
- [ ] Checklists compile to ***slash commands*** that run against the
      current diff.
- [ ] Hooks that surface relevant anti-patterns after edits to matching
      paths.

## Acceptance Criteria

- Installing the plugin causes the Service Objects guide to load
  automatically when a developer extracts logic from a Rails controller,
  without anyone naming the document.
- Regenerating the plugin after a documentation change requires no
  hand-editing.

# Layer 2 — Retrieval That Works

## Deliverables

- [ ] Chunk documents by heading section and index full text. BM25 gets
      most of the benefit with zero dependencies and works offline.
- [ ] Make sections first-class retrievable units, addressable as
      `guides/rails/service-objects.md#anti-patterns`. Agents rarely need
      a whole document.
- [ ] Assemble context packs by relevance under a token budget, rather
      than by graph depth and document count.

## Acceptance Criteria

- Searching `N+1`, `caching` and `background jobs` returns the documents
  that actually discuss them, or reports an honest content gap.

# Layer 3 — Close the Lifecycle Loop

`CLAUDE.md` diagrams a lifecycle of Experience → Capture → Review →
Refine → Organize → Publish → Apply → Learn → Improve. Tooling currently
exists only for Publish and Apply.

## Deliverables

- [ ] `/ekf:capture` — turn a debugging session, incident or code review
      into a validated draft guide or ADR.
- [ ] Log searches and context packs that return nothing, and file them
      as content gaps automatically. This is how the roadmap stops being
      hand-maintained.
- [ ] `make stale` — report documents whose `last_reviewed` date has aged
      past a threshold.

## Acceptance Criteria

- The absence of caching knowledge would have been reported by tooling
  rather than discovered by audit.

# Layer 4 — Conformance

The differentiator between this framework and a documentation site.
Knowledge that verifies code is knowledge an organization adopts rather
than admires.

## Deliverables

- [ ] Give checklist items an optional executable `check` — a grep, AST
      query or shell probe.
- [ ] `make conform` — run a capability's checklists against a target
      repository.
- [ ] Report violations linked to the guide that explains *why*, not just
      *what*.

## Acceptance Criteria

- A violation report tells an engineer which principle was violated and
  where to read about it, turning the handbook into a linter with
  rationale.

# Sequencing

Layer 0 is a prerequisite: frontmatter is the input to plugin
compilation, retrieval indexing and staleness reporting alike.

Layers 1 and 2 reinforce each other and are best done together — a
plugin that cannot find the right document is not useful. Layers 3 and 4
can follow in either order.

# Open Questions

- Should `.org-backup/` be removed now that the migration is complete and
  the site builds exclusively from Markdown?
- Should the five divergent copies of `SKIP_DIRS` be consolidated into a
  shared module, or does that violate the "prefer standalone scripts"
  principle recorded in Phase 6?
- Should Performance become a capability in its own right, or do caching
  and query optimization belong inside existing capabilities?

# Related Documents

- [Slice Plans](./README.md)
- [Roadmap](../../roadmap.md)
- [Architecture](../../architecture.md)
- [Style Guide](../../style-guide.md)
- [MCP Server](../../tools/mcp-server/README.md)
