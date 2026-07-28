# Purpose

Agentic workflows are multi-step processes where AI assists across
multiple stages of an engineering task. Unlike single-prompt
interactions, agentic workflows chain together context gathering,
analysis, generation, verification and refinement steps to produce
higher-quality outcomes.

This guide defines patterns for designing and using agentic workflows
effectively.

# Principles

## Humans Set Direction, AI Executes Steps

The engineer defines the goal and makes judgment calls at each stage.
AI handles well-defined sub-tasks within those boundaries.

## Verify at Each Step

Each stage in an agentic workflow should produce verifiable output
before the next stage begins. Do not chain steps without intermediate
verification.

## Maintain Context Across Steps

Agentic workflows require context to flow from one step to the next.
Design prompts and context packs that accumulate information as the
workflow progresses.

## Fail Fast

If a step produces unexpected or low-quality output, stop and
investigate before continuing. Iteration on a poor foundation compounds
errors.

# Common Patterns

## Draft-and-Refine

Best for: Code generation, documentation writing, test generation.

```
Step 1: Context gathering
  → Engineer provides requirements, constraints, examples.
Step 2: AI generates initial draft
  → Engineer provides scope and standards.
Step 3: Human review
  → Engineer evaluates correctness, completeness, style.
Step 4: AI refines based on feedback
  → Engineer provides specific revision requests.
Step 5: Final human approval
→ Engineer verifies the final output meets all criteria.
```

## Analyse-and-Recommend

Best for: Code review, architecture review, security analysis.

```
Step 1: AI analyses input (code, design, config)
  → Engineer provides context and focus areas.
Step 2: AI produces findings with evidence
  → AI categorises by severity, references standards.
Step 3: Human review of findings
  → Engineer confirms, rejects or investigates each finding.
Step 4: AI generates remediation suggestions
  → Engineer provides preferences and constraints.
Step 5: Human applies or adapts fixes
→ Engineer owns all changes.
```

## Explore-and-Discover

Best for: Design exploration, technology selection, debugging.

```
Step 1: Define problem space
  → Engineer describes the problem, constraints, success criteria.
Step 2: AI generates multiple approaches
  → AI outlines 2-5 approaches with trade-offs.
Step 3: Human narrows options
  → Engineer selects promising approaches for deeper analysis.
Step 4: AI deep-dives on selected options
  → AI provides detailed analysis, pros/cons, examples.
Step 5: Human makes final decision
→ Engineer documents the decision and rationale.
```

## Constrain-and-Generate

Best for: Boilerplate code, migrations, repetitive tasks.

```
Step 1: Define constraints
  → Engineer specifies inputs, outputs, conventions, boundaries.
Step 2: AI generates within constraints
  → AI produces output matching all constraints.
Step 3: Human verifies constraints are met
  → Engineer checks each constraint systematically.
Step 4: AI iterates on specific sections
  → Engineer points to specific issues for refinement.
Step 5: Human approves and integrates
→ Engineer runs tests, reviews edge cases.
```

# Designing an Agentic Workflow

## Step 1: Decompose the Task

Break the overall task into discrete, verifiable steps:

- Each step should produce a clear output.
- Each step should be verifiable independently.
- Steps should be sequenced so that later steps depend on earlier ones.

## Step 2: Define Human Touchpoints

For each step, decide:

- Is this step fully automated (AI runs, human verifies)?
- Is this step AI-assisted (AI proposes, human decides)?
- Is this step human-only (no AI involvement)?

## Step 3: Engineer Context Flow

Ensure each step has the context it needs:

- What context does this step require from previous steps?
- What context does this step add for subsequent steps?
- How is context passed between steps (prompt accumulation, memory)?

## Step 4: Add Verification Gates

For each step, define:

- What constitutes success for this step?
- How is success verified (automated test, human review, both)?
- What happens if the step fails (retry, adjust context, escalate)?

# Anti-patterns

- ***Fully autonomous chains***: Running multiple AI steps without human
  verification between them amplifies errors.
- ***Context starvation***: Each step must receive sufficient context.
  Do not assume the AI remembers earlier steps.
- ***Over-engineering***: Not every task needs an agentic workflow.
  Simple tasks benefit from single-prompt interactions.
- ***Ignoring costs***: Multi-step workflows consume more tokens and time.
  Evaluate whether the complexity is justified.

# Workflow Selection Guide

| Pattern | Best For | Human Effort | AI Autonomy |
| --- | --- | --- | --- |
+----------------------+-----------------------------------+--------------+-------------+
| Draft-and-Refine | Code, docs, tests | Medium | High |
| --- | --- | --- | --- |
| Analyse-and-Recommend | Reviews, audits | High | Medium |
| Explore-and-Discover | Design, research, debugging | High | Medium |
| Constrain-and-Generate | Boilerplate, migrations | Low | High |

# Related Documents

- [Prompt Engineering](./prompt-engineering.md)
- [Context Engineering](./context-engineering.md)
- [AI-Assisted Code Review Playbook](../../playbooks/ai/ai-assisted-code-review.md)
- [AI-Assisted Architecture Review Playbook](../../playbooks/ai/ai-assisted-architecture-review.md)
- [AI References](../../references/ai/README.md)
