+++
title = "Knowledge Extraction"
description = "Using AI to extract and structure engineering knowledge"
+++


# Purpose

Knowledge extraction is the process of capturing engineering knowledge
from experience, code, discussions and incidents, and structuring it
into reusable framework documents. AI accelerates this process by
analysing raw material, identifying patterns and generating structured
drafts.

This guide describes how to use AI effectively for knowledge
extraction while maintaining quality and consistency.

# Principles

## Human Experience, AI Structure

The engineer provides the experience, expertise and judgment. AI helps
organise, structure and articulate that knowledge. AI does not generate
engineering experience — it helps capture it.

## Extract, Do Not Generate

Knowledge extraction draws knowledge from real experience. AI should
help structure and articulate what already exists, not fabricate new
engineering principles.

## Always Attribute

Distinguish between extracted knowledge (from real experience) and
AI-suggested patterns (which need human validation). The source of
knowledge should be traceable.

## Iterate on Structure

The first draft is rarely the final structure. Use AI to experiment
with different organisations before settling on the final form.

# Extraction Sources

| Source | What Can Be Extracted |
| --- | --- |
+---------------------+----------------------------------------------+
| Code review comments | Patterns, anti-patterns, conventions. |
| --- | --- |
| Incident reports | Runbooks, playbooks, prevention checklists. |
| Architecture decisions (ADRs) | Decision frameworks, trade-off patterns. |
| Retrospectives | Process improvements, best practices. |
| Pull request discussions | Standards, review criteria. |
| Onboarding sessions | Glossary terms, conceptual guides. |
| Codebase analysis | Coding standards, architectural patterns. |
| Team discussions | Decision frameworks, heuristics. |

# Workflow

## Step 1: Source Collection

Gather the raw material for extraction:

- Pull request descriptions and discussions.
- Incident reports and post-mortems.
- Architecture Decision Records.
- Retrospective notes.
- Code review archives.
- Team wiki or documentation.

## Step 2: Analysis

Ask AI to analyse the source material:

```
Analyse these code review comments and identify:
1. Recurring issues or patterns.
2. Conventions that are frequently enforced.
3. Anti-patterns that appear repeatedly.
4. Knowledge gaps that new team members encounter.

[Paste source material]
```

## Step 3: Structure Identification

Ask AI to propose a document structure:

```
Based on the patterns identified, propose a structure for a
[guide / playbook / checklist / reference] on [topic].

The document should follow the framework's conventions:
- Clear purpose and scope.
- Principles before procedures.
- Examples and anti-patterns where appropriate.
- Cross-references to related documents.

[Paste analysis results]
```

## Step 4: Draft Generation

Ask AI to generate a draft following the proposed structure:

```
Using the structure below, generate a draft [guide / playbook] for
[topic]. Use real examples from the source material where possible.
Mark any AI-suggested content that is not directly from the source
as [AI SUGGESTION] for human review.

Structure:
[Paste structure]
Source material:
[Paste source material]
```

## Step 5: Human Review and Refinement

1. Read the draft critically.
2. Verify all extracted knowledge against your experience.
3. Remove or rewrite AI-suggested content that does not match reality.
4. Add missing knowledge that AI did not extract.
5. Refine the structure if needed.

## Step 6: Integration

1. Place the document in the appropriate capability directory.
2. Add cross-references to related documents.
3. Update the handbook's Capability Map section.
4. Update TOC.org with the new document entry.

# Extraction Templates

## Guide Extraction

```
Extract a guide on [topic] from the following source material.

Structure the guide as:
1. Purpose — what this guide covers and why it exists.
2. Background — context needed to understand the topic.
3. Principles — the key principles to follow.
4. Patterns — practical patterns with examples.
5. Anti-patterns — common mistakes to avoid.
6. Related documents — cross-references.

Source:
[paste material]
```

## Playbook Extraction

```
Extract a playbook for [workflow] from the following incident reports
and retrospectives.

Structure the playbook as:
1. Objective — what this playbook achieves.
2. Inputs — what you need before starting.
3. Prerequisites — what must be in place.
4. Workflow — step-by-step instructions.
5. Checklist — verification items.
6. Escalation points — when to get help.
7. Expected outputs — what success looks like.

Source:
[paste material]
```

## Checklist Extraction

```
Extract a checklist for [activity] from the following code review
comments and standards.

The checklist should be specific, verifiable items that can be checked
off during review. Group by category.

Source:
[paste material]
```

# Quality Criteria

| Criterion | Description |
| --- | --- |
+-------------------+---------------------------------------------+
| Faithfulness | Does the document accurately reflect the |
| --- | --- |
|  | source material? |
| Completeness | Are all important patterns from the source |
|  | captured? |
| Generalisation | Is the knowledge presented as general |
|  | guidance, not tied to a specific instance? |
| Actionability | Can a reader use this to make better |
|  | decisions? |
| Consistency | Does it follow framework conventions and |
|  | document type structure? |

# Anti-patterns

- ***Fabrication***: AI generating knowledge that does not come from
  real experience. Always verify against source material.
- ***Over-generalisation***: Extracting universal principles from a single
  incident or code review.
- ***Loss of context***: Extracting knowledge without preserving the
  context that made it relevant.
- ***Passive extraction***: Asking AI to "write a guide" without providing
  source material. Extraction requires real input.
- ***Not iterating***: Accepting the first AI-proposed structure without
  experimenting with alternatives.

# Related Documents

- [Agentic Workflows — Explore-and-Discover pattern](./agentic-workflows/)
- [AI Evaluation Frameworks](./evaluation-frameworks/)
- [AI Engineering Handbook](../../handbooks/ai/README/)
- [Style Guide](../../STYLE_GUIDE/)
- [Document Types](../../DOCUMENT_TYPES/)
