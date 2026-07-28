---
title: "Prompt Engineering"
description: "Principles and patterns for effective AI prompt design"
---


# Purpose

Prompt engineering is the practice of designing inputs that elicit
useful, accurate output from AI systems.

Well-crafted prompts produce better results than raw queries. Investing
in prompt quality reduces iteration time and improves output
consistency.

# Principles

## Be Specific

Vague prompts produce vague results.

Good:

```
Write a Ruby method that validates an email address format using a
regular expression. Return true if valid, false otherwise.
```

Avoid:

```
Write some code for email validation.
```

## Provide Context

AI performs better when it understands the full picture.

Include:

- The problem you are solving.
- Relevant constraints (language, framework, performance).
- Existing code or architecture context.
- The audience for the output.

## Use Structure

Structured prompts produce structured outputs.

- Use bullet points for lists of requirements.
- Use sections for complex requests.
- Specify the desired output format.

## Show Examples

Examples are more effective than descriptions.

Provide one or two examples of the input and desired output before
asking for the actual work.

## Iterate

First attempts are rarely perfect.

Treat prompt engineering as an iterative process:

1. Write an initial prompt.
2. Evaluate the output.
3. Refine the prompt based on gaps.
4. Repeat.

# Patterns

## The Persona Pattern

Assign a role to the AI to focus its output.

```
You are a senior Rails engineer reviewing a pull request. Focus on
design issues, security concerns and testing gaps.
```

## The Format Pattern

Specify the exact output format.

```
Provide the response as a JSON object with keys: "summary",
"issues" (array), and "recommendations" (array).
```

## The Constraint Pattern

Limit the scope explicitly.

```
Only suggest changes to the service layer. Do not suggest changes to
the database schema or frontend code.
```

## The Verification Pattern

Ask the AI to verify its own output.

```
After generating the code, review it for:
1. Security vulnerabilities.
2. Edge cases that are not handled.
3. Performance concerns.
```

## The Decomposition Pattern

Break complex requests into smaller steps.

```
Step 1: Analyse the current error handling in this controller.
Step 2: Propose a service object to extract the business logic.
Step 3: Write the service object implementation.
```

# Anti-patterns

## Over-Prompting

Including excessive irrelevant context dilutes the important
information. Be concise.

## Assuming Knowledge

Do not assume the AI knows your codebase, conventions or history.
Provide explicit context even if it feels redundant.

## Accepting First Output

First attempts are often incomplete or incorrect. Iterate.

## No Verification

Trusting AI output without verification is the most dangerous
anti-pattern. Always verify.

# Related Documents

- [AI Engineering Handbook](../../handbooks/ai/README/)
- [Context Engineering Guide](../../guides/ai/context-engineering/)
- [AI Workflows for Engineering](../../prompts/engineering-ai-workflows/)
