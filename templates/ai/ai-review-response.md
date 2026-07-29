---
title: "AI Review Response Template"
description: "Use this template to document and track AI-generated review findings."
type: template
capability: ai
status: published
tags: [review, response]
last_reviewed: 2026-07-28
---

# AI Review Response Template

Use this template to document and track AI-generated review findings.
Each finding should be reviewed, verified and assigned by a human before
action is taken.

# Review Metadata

- ***Task:*** [Code review / Architecture review / Security review / Documentation review]
- ***AI Assistant:*** [Tool and model used]
- ***Date:*** [YYYY-MM-DD]
- ***Reviewer:*** [Human reviewer name]
- ***Context Pack:*** [Link to context pack used]

# Findings

## Finding 1: [Title]

| Field               | Value                                                       |
|---------------------|-------------------------------------------------------------|
| ***Severity***      | [Critical / High / Medium / Low / Informational]            |
| ***Category***      | [Correctness / Security / Performance / Style / etc.]       |
| ***Location***      | [File, line or component]                                   |
| ***AI Finding***    | [What the AI identified]                                    |
| ***Human Verdict*** | [Confirmed / False Positive / Needs Investigation]          |
| ***Action***        | [Description of required change or rationale for dismissal] |

## Finding 2: [Title]

| Field               | Value                                                       |
|---------------------|-------------------------------------------------------------|
| ***Severity***      | [Critical / High / Medium / Low / Informational]            |
| ***Category***      | [Correctness / Security / Performance / Style / etc.]       |
| ***Location***      | [File, line or component]                                   |
| ***AI Finding***    | [What the AI identified]                                    |
| ***Human Verdict*** | [Confirmed / False Positive / Needs Investigation]          |
| ***Action***        | [Description of required change or rationale for dismissal] |

# Summary

| Verdict             | Count |
|---------------------|-------|
| Confirmed           |       |
| False Positive      |       |
| Needs Investigation |       |

# Quality Notes

- How accurate was the AI review overall?
- What did the AI miss?
- How could the context or prompt be improved?

# Related Documents

- [AI Usage Checklist](../../checklists/ai-usage.md)
- [AI Safety and Verification](../../guides/ai/ai-safety.md)
- [Context Engineering](../../guides/ai/context-engineering.md)
