+++
title = "Context Engineering"
description = "How to provide effective context to AI systems"
+++


# Purpose

Context engineering is the practice of providing AI systems with
structured, relevant information to improve the quality and accuracy
of their output.

It is the single most effective way to improve AI output quality.
Better context produces better results than better prompts.

# Why Context Matters

AI systems have no inherent knowledge of your specific:

- Codebase structure and conventions.
- Business domain and terminology.
- Technology stack and versions.
- Quality standards and expectations.
- Architectural decisions and history.

Without context, AI relies on general patterns which may not apply to
your situation. Providing context bridges this gap.

# The Context Categories

## Scope

What are you trying to accomplish?

Include:

- The specific task or problem.
- What is in scope and what is out of scope.
- The desired outcome.

## Constraints

What limits apply?

Examples:

- "Must support 10,000 requests per second."
- "Must work with Rails 7.1 and Ruby 3.3."
- "Cannot introduce new dependencies."
- "Must be backwards compatible with the existing API."

## Standards

What conventions should be followed?

Reference:

- Style guides.
- Coding standards.
- Architectural principles.
- Naming conventions.

Use links to the relevant documents in this repository.

## Examples

What does good output look like?

Provide:

- Before*after examples for refactoring.
- Example inputs and expected outputs.
- Reference implementations.

## References

What should the AI consult?

Link to:

- Handbooks for principles.
- Glossaries for terminology.
- Playbooks for workflows.
- Existing code or documentation.

# Context Templates

## For Code Generation

```
I need to [task description].

Language: [language]
Framework: [framework]
Constraints:
- [constraint 1]
- [constraint 2]

Existing code context:
```[language]
[paste relevant code]
```

Standards to follow:
- [link to handbook or style guide]

Desired output:
- [description of expected output]
- [format specification]
```

## For Code Review

```
Review this code for [purpose of the change].

Focus on:
1. [area of concern 1]
2. [area of concern 2]

Relevant standards:
- [link to handbook or guidelines]

Code:
```[language]
[paste code]
```
```

## For Design Exploration

```
I am designing [system*feature].

Goals:
- [goal 1]
- [goal 2]

Constraints:
- [constraint 1]
- [constraint 2]

Quality attribute priorities (ranked):
1. [attribute 1]
2. [attribute 2]

Approaches already considered:
- [approach 1]
- [approach 2]

What alternatives am I missing?
```

# Using Repository Documents as Context

The Engineering Knowledge Framework is designed to provide rich
context for AI systems.

When working on a task, reference these documents in your prompts:

| Need | Reference Document |
+--------------------------------+----------------------------------+
| Engineering principles | Engineering Fundamentals Handbook |
+--------------------------------+----------------------------------+
| Architecture standards | Software Architecture Handbook |
+--------------------------------+----------------------------------+
| Rails conventions | Rails Engineering Handbook |
+--------------------------------+----------------------------------+
| Security requirements | Security Engineering Handbook |
+--------------------------------+----------------------------------+
| Terminology definitions | Relevant capability glossary |
+--------------------------------+----------------------------------+
| Workflow steps | Relevant capability playbook |
+--------------------------------+----------------------------------+
| Quality criteria | Relevant capability checklist |
+--------------------------------+----------------------------------+
| Code examples and patterns | Relevant capability templates |
+--------------------------------+----------------------------------+

# Related Documents

- [AI Engineering Handbook](../..*handbooks*ai*README*)
- [Prompt Engineering Guide](../..*guides*ai*prompt-engineering*)
- [AI Workflows for Engineering](../..*prompts*engineering-ai-workflows*)
- [AI Workflows for Architecture](..*..*prompts*architecture-ai-workflows/)
