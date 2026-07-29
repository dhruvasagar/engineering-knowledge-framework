---
title: "AI Workflows for AI Engineering"
description: "This document provides prompt patterns for using AI to assist with AI Engineering tasks — designing prompts, building context packs, evaluating AI output and improving..."
type: prompt
capability: ai
status: published
tags: [workflows]
last_reviewed: 2026-07-28
---

# Purpose

This document provides prompt patterns for using AI to assist with
AI Engineering tasks — designing prompts, building context packs,
evaluating AI output and improving AI-assisted workflows.

# Principles

- AI should help improve AI-assisted workflows, not replace human
  judgement about when and how to use AI.
- All AI-generated AI workflows must be verified by a human before use.
- Context engineering skills transfer to designing prompts that help
  others use AI effectively.

# Workflows

## Prompt Design

Use AI to help design better prompts for engineering tasks.

Context:

```text
I need to write a prompt for [task]. The audience is [engineers /
architects / etc.]. The output should be [code / analysis / document].

Help me design a prompt that:
1. Clearly defines the task.
2. Provides sufficient context.
3. Includes relevant constraints.
4. Specifies the output format.
5. Includes verification criteria.
```

## Context Pack Review

Ask AI to review your context pack before using it.

Context:

```text
Review this context pack for [task]:

[paste context pack]

Does it include:
1. Clear scope and task definition.
2. Relevant standards and conventions.
3. Useful examples.
4. Necessary references.
5. Missing context that would improve results.

Suggest improvements.
```

## AI Output Evaluation

Ask AI to evaluate its own output quality.

Context:

```text
Evaluate the following AI output for [task type]:

[paste output]

Criteria:
1. Correctness: Is it technically accurate?
2. Completeness: Does it address the full task?
3. Consistency: Does it match project conventions?
4. Safety: Are there any security or correctness risks?

Rate each criterion and suggest improvements.
```

## Workflow Improvement

Use AI to improve your AI-assisted workflows.

Context:

```text
I'm using AI for [workflow — e.g., code review, architecture review].
My current process is:

[describe current process]

Challenges I'm facing:
1. [Challenge 1]
2. [Challenge 2]

Suggest improvements to my workflow, prompt patterns or context
engineering approach.
```

## Knowledge Extraction

Use AI to extract and structure engineering knowledge from experience.

Context:

```text
I need to capture engineering knowledge from [experience / incident /
project] and structure it as a [guide / playbook / checklist].

Raw notes:

[paste raw notes]

Help me structure this as a [document type] following the framework's
conventions. Include:
1. Clear title and purpose.
2. Principles or background.
3. Practical guidance.
4. Examples where applicable.
5. Cross-references to related documents.
```

# Anti-patterns

- ***Prompting without context***: AI cannot design good prompts without
  understanding the task and audience.
- ***Uncritical adoption***: AI-suggested workflows must be tested before
  adoption.
- ***Circular reliance***: Using AI to evaluate AI output without human
  verification creates an echo chamber.
- ***Over-optimisation***: Perfecting prompts is less valuable than using
  them effectively.

# Related Documents

- [AI Engineering Handbook](../handbooks/ai/README.md)
- [Prompt Engineering](../guides/ai/prompt-engineering.md)
- [Context Engineering](../guides/ai/context-engineering.md)
- [AI Safety and Verification](../guides/ai/ai-safety.md)
- [AI Usage Checklist](../checklists/ai-usage.md)
