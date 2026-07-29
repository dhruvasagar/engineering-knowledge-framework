---
title: "AI Usage Checklist"
description: "Verify that AI-generated output is safe, correct and appropriate before acceptance."
type: checklist
capability: ai
status: published
tags: [usage]
last_reviewed: 2026-07-28
---

# Purpose

Verify that AI-generated output is safe, correct and appropriate before
acceptance.

# Before Using AI

- [ ] Is the task appropriate for AI assistance?
- [ ] Do I have the context needed to evaluate AI output?
- [ ] Have I identified the risk level (low, medium, high)?
- [ ] Do I know which parts of the output need most scrutiny?

# For Code

- [ ] Code compiles and builds without errors.
- [ ] Existing tests pass.
- [ ] New tests cover the AI-generated code.
- [ ] Security scanners pass.
- [ ] Code follows project conventions (style, naming, structure).
- [ ] I understand every line of the generated code.
- [ ] No unnecessary dependencies introduced.

# For Documentation

- [ ] Facts are verified against authoritative sources.
- [ ] Terminology matches the relevant glossary.
- [ ] Links are valid.
- [ ] Tone and style match the target audience.
- [ ] No proprietary or confidential information exposed.

# For Architecture

- [ ] Decision is evaluated against relevant principles.
- [ ] Trade-offs are documented correctly.
- [ ] Alternatives were considered.
- [ ] An architect has reviewed the recommendation.

# Verification

- [ ] AI output has been reviewed by a human.
- [ ] High-risk output has been reviewed by a subject matter expert.
- [ ] Output is appropriate for its intended use.
- [ ] AI was used as a collaborator, not a decision-maker.

# Related Documents

- [AI Engineering Handbook](../handbooks/ai/README.md)
- [AI Safety Guide](../guides/ai/ai-safety.md)
- [Code Review Playbook](../playbooks/code-review/README.md)
