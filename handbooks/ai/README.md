+++
title = "AI Engineering Handbook"
description = "Principles, patterns and practices for AI-assisted engineering"
+++


# Purpose

AI engineering is the practice of integrating AI assistants into the
software development lifecycle to improve productivity, quality and
decision-making.

This handbook defines the principles, patterns and practices for
using AI effectively throughout the engineering lifecycle.

It builds upon the [Engineering Fundamentals Handbook](../../handbooks/engineering/README/) and
[Software Architecture Handbook](../../handbooks/architecture/README/), applying their principles to the
AI context.

# Scope

This handbook covers:

- AI engineering principles and philosophy.
- Context engineering and prompt design.
- AI-assisted workflows for engineering tasks.
- Verification and validation of AI output.
- AI safety and human oversight.
- Integrating AI into team practices.

Capability-specific AI guidance is in the AI Workflow documents for
each capability (e.g., [AI Workflows for Rails](../../prompts/rails-ai-workflows/)).

# Principles

## AI Augments, Does Not Replace

AI accelerates engineering work but does not replace engineering
judgement.

- AI can generate code, but humans must review it.
- AI can suggest designs, but humans must evaluate trade-offs.
- AI can identify issues, but humans must prioritize and decide.

## Human Responsibility is Final

Every engineering decision ultimately belongs to a human.

AI-generated code, designs, documentation or analysis must be reviewed
by a human before acceptance. AI can assist, but it cannot be held
accountable.

## Context is the Primary Lever

The quality of AI output depends directly on the quality of context
provided.

Investing in clear, well-structured context produces better results
than optimizing prompts in isolation.

## Verify Everything

AI systems make mistakes confidently.

Every AI output must be verified:

- Code must be tested.
- Facts must be checked.
- Recommendations must be evaluated against first principles.
- Security implications must be reviewed.

## Prefer Structured Inputs

AI performs better with structured inputs than unstructured ones.

When providing context, prefer:

- Defined terminology (use glossary terms).
- Explicit constraints and requirements.
- Examples of desired output.
- Reference documents and standards.

# Context Engineering

Context engineering is the practice of providing AI systems with the
information they need to produce useful output.

## Context Categories

| Category | What to Include |
| --- | --- |
+---------------+---------------------------------------------------+
| Scope | What are we trying to accomplish? What are the |
| --- | --- |
|  | boundaries? |
+---------------+---------------------------------------------------+
| Constraints | What limits apply? Time, technology, performance, |
| --- | --- |
|  | compliance. |
+---------------+---------------------------------------------------+
| Standards | What conventions, style guides or patterns should |
| --- | --- |
|  | be followed? |
+---------------+---------------------------------------------------+
| Examples | What does good output look like? Provide samples. |
| --- | --- |
+---------------+---------------------------------------------------+
| References | What documents, code or resources should the AI |
| --- | --- |
|  | reference? |
+---------------+---------------------------------------------------+
| Quality | What criteria define success? How will the output |
| --- | --- |
| Criteria | be evaluated? |
+---------------+---------------------------------------------------+

## Context Sources in This Repository

The framework provides rich context for AI:

- Handbooks: Principles and standards for each capability.
- Glossaries: Canonical terminology with definitions.
- Style Guide: Writing and formatting standards.
- Playbooks: Repeatable workflows with verification steps.
- Checklists: Explicit quality gates.

When using AI for engineering work, reference these documents in your
prompts.

# AI Workflow Patterns

## Pattern 1: Draft and Refine

Start broad, then refine through iteration.

1. Provide high-level context and ask for a draft.
2. Review the draft and identify gaps or issues.
3. Provide specific feedback and ask for revision.
4. Repeat until the output meets quality criteria.

Best for: Documentation, design proposals, initial code generation.

## Pattern 2: Constrain and Generate

Provide tight constraints and ask for a focused output.

1. Define the exact scope, format and quality criteria.
2. Provide reference examples and standards.
3. Ask for the specific output.
4. Verify against the constraints.

Best for: Code generation with specific requirements, test generation,
configuration generation.

## Pattern 3: Analyse and Advise

Ask AI to analyse existing work and provide recommendations.

1. Provide the work to be analysed (code, design, text).
2. Specify the analysis criteria.
3. Ask for specific recommendations.
4. Evaluate recommendations using engineering judgement.

Best for: Code review, design review, performance analysis,
security review.

## Pattern 4: Explore and Discover

Use AI to explore alternatives and identify blind spots.

1. Describe the problem and your current approach.
2. Ask for alternatives or considerations you might have missed.
3. Evaluate each alternative against your criteria.
4. Document the exploration for future reference.

Best for: Design exploration, architecture decisions, problem diagnosis.

# Verification and Validation

## Verification Checklist

Before accepting AI-generated output:

- [ ] Does the output meet the stated requirements?
- [ ] Is the output consistent with referenced standards?
- [ ] Are all stated facts accurate?
- [ ] Does the code compile and pass tests?
- [ ] Are there security concerns?
- [ ] Is the output appropriate for its intended audience?

## Common Failure Modes

| Failure Mode | Description | Mitigation |
| --- | --- | --- |
+-------------------+------------------------------------------------+------------------------------------+
| Hallucination | AI generates plausible but incorrect | Verify facts against authoritative |
| --- | --- | --- |
|  | information. | sources. |
+-------------------+------------------------------------------------+------------------------------------+
| Over-confidence | AI presents incorrect output with high | Always verify, especially when AI |
| --- | --- | --- |
|  | certainty. | seems confident. |
+-------------------+------------------------------------------------+------------------------------------+
| Style drift | AI output diverges from project conventions | Provide style references in |
| --- | --- | --- |
|  | over multiple interactions. | context. |
+-------------------+------------------------------------------------+------------------------------------+
| Context loss | AI loses track of earlier context in long | Periodically recap context in |
| --- | --- | --- |
|  | conversations. | long sessions. |
+-------------------+------------------------------------------------+------------------------------------+

# Integrating AI into Team Practices

## Code Review with AI

AI can assist human code review by:

- Detecting common issues (style, bugs, security).
- Suggesting improvements.
- Generating review comments.
- Summarising large diffs.

AI should not replace human reviewers. AI is a first pass; human
reviewers focus on design, trade-offs and context.

## Architecture with AI

AI can assist architectural work by:

- Analysing trade-offs between approaches.
- Identifying alternatives.
- Drafting ADRs from discussion notes.
- Reviewing architecture for consistency.

AI cannot evaluate organisational context or business strategy.

## Testing with AI

AI can assist testing by:

- Generating test cases from code.
- Identifying untested code paths.
- Suggesting edge cases.
- Writing test fixtures and factories.

AI-generated tests must be reviewed for correctness and completeness.

# Related Documents

- [AI Workflows for Engineering](../../prompts/engineering-ai-workflows/)
- [AI Workflows for Architecture](../../prompts/architecture-ai-workflows/)
- [AI Workflows for Rails](../../prompts/rails-ai-workflows/)
- [AI Workflows for Security](../../prompts/security-ai-workflows/)
- [Engineering Fundamentals Handbook](../../handbooks/engineering/README/)
- [Style Guide](../../STYLE_GUIDE/)
