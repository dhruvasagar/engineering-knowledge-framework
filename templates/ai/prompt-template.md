# Prompt Template

Use this structure when writing prompts for engineering tasks. Adapt the
sections based on the task type. See [Prompt Engineering](../../guides/ai/prompt-engineering.md) for detailed
guidance on each pattern.

# Structure

## Persona

Describe the role the AI should adopt:

```
You are a senior [Rails / security / architecture / etc.] engineer
reviewing [code / design / documentation].
```

## Context

Provide the minimum context needed:

```
Context:
- Project: [project name]
- Framework: [framework and version]
- Standards: [relevant standards]
- Relevant files: [file paths]
```

## Task

State the task clearly and specifically:

```
Please [review / generate / analyse / explain] the following [code /
design / document]:

[paste content here]
```

## Constraints

Specify boundaries and requirements:

```
Constraints:
- Follow [specific standard or convention].
- Consider [security / performance / maintainability].
- Output format: [code with comments / bullet points / markdown document].
```

## Verification

Ask the AI to verify its own output:

```
Before responding, verify that:
1. [Specific check 1]
2. [Specific check 2]
```

# Examples

## Code Review

```
You are a senior Rails engineer reviewing a pull request.
Focus on correctness, security and adherence to project conventions.

PR: [link or diff]

Please review for:
1. Security vulnerabilities (especially mass assignment, SQL injection, XSS).
2. Performance concerns (N+1 queries, missing indexes).
3. Test coverage and quality.
4. Adherence to service object patterns.

For each issue, indicate severity: critical / major / minor / suggestion.
```

## Design Exploration

```
You are a software architect. I need to choose between [Option A]
and [Option B] for [use case].

Context:
- Current system: [description]
- Constraints: [performance, team size, timeline]
- Quality attributes: [scalability, maintainability, security]

Analyse the trade-offs and recommend an approach with rationale.
```

# Related Documents

- [Prompt Engineering guide](../../guides/ai/prompt-engineering.md)
- [Context Engineering guide](../../guides/ai/context-engineering.md)
- [AI References — prompt patterns quick reference](../../references/ai/README.md)
