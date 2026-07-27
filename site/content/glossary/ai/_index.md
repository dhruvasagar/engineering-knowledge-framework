+++
title = "AI Engineering Glossary"
description = "AI engineering terminology used throughout the Engineering Knowledge Framework"
+++


# Purpose

This glossary defines AI engineering terminology used throughout the
Engineering Knowledge Framework.

# Glossary

## Context Engineering

| Property | Value |
| --- | --- |
| Definition | The practice of providing AI systems with structured, |
|  | relevant information to improve the quality and accuracy |
|  | of their output. |
| Context | Context engineering includes defining scope, |
|  | constraints, standards, examples, references and quality |
|  | criteria. It is the primary lever for improving AI |
|  | output quality. |
| Related | [[#prompt-engineering][Prompt Engineering]] |
| References | [AI Engineering Handbook](../..*handbooks*ai*README*) |

## Hallucination

| Property | Value |
| --- | --- |
| Definition | The tendency of AI systems to generate plausible but |
|  | incorrect information with high confidence. |
| Context | Hallucinations are a known limitation of large language |
|  | models. Mitigation requires verifying AI output against |
|  | authoritative sources and applying human review. |
| Related | [[#verification][Verification]] |
| References | [AI Engineering Handbook](../..*handbooks*ai*README*) |

## Prompt Engineering

| Property | Value |
| --- | --- |
| Definition | The practice of designing input prompts to elicit |
|  | desired responses from AI systems. |
| Context | Prompt engineering is a subset of context engineering. |
|  | Effective prompts are specific, structured and include |
|  | relevant context. |
| Related | [[#context-engineering][Context Engineering]] |
| References | [AI Engineering Handbook](../..*handbooks*ai*README*) |

## Verification

| Property | Value |
| --- | --- |
| Definition | The process of evaluating AI-generated output for |
|  | correctness, consistency and safety before acceptance. |
| Context | Every AI output must be verified. Verification includes |
|  | testing code, checking facts, reviewing security |
|  | implications and evaluating against requirements. |
| Related | [[#hallucination][Hallucination]] |
| References | [AI Engineering Handbook](../..*handbooks*ai*README*) |

# Related Documents

- [AI Engineering Handbook](../..*handbooks*ai*README*)
- [Engineering Glossary](..*engineering*README*)
- [AI Workflows for Engineering](..*..*prompts*engineering-ai-workflows/)
