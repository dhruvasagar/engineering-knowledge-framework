---
title: "AI Collaboration Patterns"
description: "How engineers and AI should interact in different contexts"
---


# Purpose

AI collaboration patterns define how engineers and AI interact during
engineering tasks. Different tasks benefit from different interaction
models — from AI as a research assistant to AI as a pair programmer.

This guide describes the collaboration patterns available and when to
use each.

# Principles

## AI is a Tool, Not a Team Member

AI augments engineering capability but does not replace engineering
judgement, accountability or ownership. The engineer is always
responsible for the output.

## Match the Pattern to the Task

Different tasks require different levels of AI autonomy and human
oversight. Choose the collaboration pattern that fits the task's
complexity, risk and required creativity.

## Be Explicit About Expectations

At the start of each interaction, clarify the collaboration mode:
- What should the AI do?
- What will the human do?
- How will the output be verified?

# Collaboration Patterns

## AI as Research Assistant

The engineer asks AI to gather information, summarise knowledge or
explore options. The engineer evaluates the results and makes
decisions.

| Aspect | Description |
| --- | --- |
+-----------------+-------------------------------------------------+
| AI role | Gather, summarise, explore. |
| --- | --- |
| Human role | Evaluate, decide, direct. |
| Best for | Technology research, option exploration, |
|  | learning new domains. |
| Risk level | Low — output informs but does not execute. |
| Verification | Quick plausibility check. |

```
Engineer: "What approaches exist for implementing background jobs?"
AI: "Here are three approaches with their trade-offs..."
Engineer: "Deep-dive on option 2 — it fits our constraints."
```

## AI as Scribe

The engineer dictates or describes what to write, and AI produces the
initial draft. The engineer then reviews and edits.

| Aspect | Description |
| --- | --- |
+-----------------+-------------------------------------------------+
| AI role | Draft, format, structure. |
| --- | --- |
| Human role | Direct, review, edit. |
| Best for | Documentation, code comments, commit messages, |
|  | boilerplate code, test scaffolding. |
| Risk level | Low to medium — human reviews before use. |
| Verification | Human reads and approves before committing. |

```
Engineer: "Write a service object for processing order payments..."
AI: [produces draft]
Engineer: [reviews, edits, commits]
```

## AI as Reviewer

The engineer produces work and asks AI to review it for issues. The
engineer evaluates each finding and decides whether to act.

| Aspect | Description |
| --- | --- |
+-----------------+-------------------------------------------------+
| AI role | Analyse, identify issues, suggest improvements. |
| --- | --- |
| Human role | Produce work, evaluate findings, decide. |
| Best for | Code review, design review, documentation review. |
| Risk level | Medium — AI may miss context or generate false |
|  | positives. |
| Verification | Human evaluates each finding before acting. |

```
Engineer: "Review this pull request for security issues."
AI: [lists findings with severity]
Engineer: [confirms, dismisses, or investigates each]
```

## AI as Pair Programmer

The engineer and AI work side-by-side on a task. The AI handles routine
aspects while the engineer focuses on design and complex logic.

| Aspect | Description |
| --- | --- |
+-----------------+-------------------------------------------------+
| AI role | Generate, refactor, test. |
| --- | --- |
| Human role | Design, decide, verify. |
| Best for | Feature implementation, refactoring, debugging. |
| Risk level | Medium to high — code is used with human review. |
| Verification | Tests must pass, human reviews all logic. |

```
Engineer: "Let's implement the user authentication module..."
AI: "I'll generate the model and controller..."
Engineer: "I'll handle the custom OmniAuth strategy..."
AI: "I'll write the tests..."
```

## AI as Tutor

The engineer asks AI to explain concepts, suggest learning resources or
provide guided practice. The engineer drives the learning process.

| Aspect | Description |
| --- | --- |
+-----------------+-------------------------------------------------+
| AI role | Explain, demonstrate, provide examples. |
| --- | --- |
| Human role | Ask, practice, apply. |
| Best for | Learning new technologies, understanding patterns. |
| Risk level | Low — AI output may contain inaccuracies. |
| Verification | Cross-reference with official documentation. |

```
Engineer: "Explain the strategy pattern with a Rails example."
AI: [provides explanation and code example]
Engineer: "Now show me how it differs from the service object pattern."
```

# Selecting the Right Pattern

| Factor | Research Asst | Scribe | Reviewer | Pair Prog | Tutor |
| --- | --- | --- | --- | --- | --- |
+---------------------------+---------------+---------------+----------+-----------+-------+
| Task complexity | Any | Low | Any | Med-High | Any |
| --- | --- | --- | --- | --- | --- |
| Required creativity | Low | Low | Low | High | Low |
| Risk of incorrect output | Low | Med | Med | High | Low |
| Human effort required | Low | Med | High | High | Med |
| AI autonomy | High | High | Medium | Medium | High |

# Anti-patterns

- ***AI as decision-maker***: AI should inform decisions, not make them.
- ***Pattern mismatch***: Using "AI as Scribe" for a high-creativity task
  produces generic output. Use "AI as Pair Programmer" instead.
- ***No verification***: Every AI output must be verified, regardless of
  the collaboration pattern.
- ***Pattern rigidity***: Switch patterns mid-task if the current one is
  not working. Collaboration should adapt to the situation.

# Related Documents

- [Agentic Workflows](./agentic-workflows/)
- [Prompt Engineering](./prompt-engineering/)
- [AI Pair Programming Playbook](../../playbooks/ai/ai-pair-programming/)
- [AI Engineering Handbook](../../handbooks/ai/README/)
