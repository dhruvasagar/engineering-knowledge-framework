# Purpose

Quick-reference material for AI-assisted engineering.

# AI Workflow Patterns

| Pattern            | Use When                                     | Approach                  |
|--------------------|----------------------------------------------|---------------------------|
| Draft and Refine   | Open-ended tasks, documentation, design.     | Start broad, iterate.     |
| Constrain and      | Code generation, tests, config with specific | Set tight constraints.    |
| Generate           | requirements.                                |                           |
| Analyse and Advise | Code review, design review, performance      | Provide work, specify     |
|                    | analysis.                                    | criteria.                 |
| Explore and        | Design exploration, alternatives, problem    | Describe problem, ask for |
| Discover           | diagnosis.                                   | what you missed.          |

# Context Categories

| Category    | What to Provide                                     |
|-------------|-----------------------------------------------------|
| Scope       | Task, boundaries, desired outcome.                  |
| Constraints | Time, technology, performance, compliance limits.   |
| Standards   | Conventions, style guides, patterns to follow.      |
| Examples    | Sample inputs and desired outputs.                  |
| References  | Documents, code or resources for the AI to consult. |
| Quality     | Criteria for evaluating success.                    |
| Criteria    |                                                     |

# Failure Modes

| Failure Mode    | Description                     | Mitigation                     |
|-----------------|---------------------------------|--------------------------------|
| Hallucination   | AI generates plausible but      | Verify against authoritative   |
|                 | incorrect information.          | sources.                       |
| Over-confidence | Incorrect output presented with | Always verify, especially when |
|                 | high certainty.                 | AI seems confident.            |
| Style drift     | Output diverges from project    | Provide style references in    |
|                 | conventions over time.          | context.                       |
| Context loss    | AI loses context in long        | Periodically recap context.    |
|                 | conversations.                  |                                |

# Prompt Patterns Quick Reference

| Pattern       | Example                                            |
|---------------|----------------------------------------------------|
| Persona       | "You are a senior Rails engineer..."               |
| Format        | "Provide the response as JSON with keys: ..."      |
| Constraint    | "Only suggest changes to the service layer..."     |
| Verification  | "After generating, review for security issues..."  |
| Decomposition | "Step 1: Analyse. Step 2: Propose. Step 3: Write." |

# Related Documents

- [AI Engineering Handbook](../../handbooks/ai/README.md)
- [AI Engineering Glossary](../../glossary/ai/README.md)
- [AI Workflows for Engineering](../../prompts/engineering-ai-workflows.md)
