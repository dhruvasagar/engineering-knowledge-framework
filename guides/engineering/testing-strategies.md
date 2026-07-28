# Purpose

Automated testing is the practice of verifying that software behaves
correctly through repeatable, machine-executable checks.

Well-designed tests provide confidence that changes work as expected,
document system behaviour, and enable refactoring without fear.

Poorly designed tests become brittle, slow, and expensive to maintain —
reducing rather than increasing engineering velocity.

This guide defines the principles and patterns for building effective,
maintainable test suites.

# Background

The value of a test is not in how much code it covers, but in how much
confidence it provides.

A test suite that catches regressions, documents behaviour and runs
quickly is more valuable than a test suite with 100% coverage that is
slow, flaky and hard to understand.

The goal is sustainable test quality, not maximal test quantity.

# Principles

## Test Behaviour, Not Implementation

Tests should verify that the system behaves correctly, not that it is
implemented in a specific way.

Tests coupled to implementation details break when the implementation
changes, even when the behaviour remains correct.

Good tests:

- Assert on outputs, return values and observable side effects.
- Avoid asserting on internal state or method call ordering.
- Treat the subject under test as a black box when possible.

## Prefer Fast, Reliable Tests

A slow test suite discourages running tests. A flaky test suite
undermines trust in test results.

Optimise for speed and reliability:

- Use unit tests for detailed verification of logic.
- Use integration tests for critical paths.
- Minimise end-to-end tests that exercise the full stack.
- Mock or stub slow dependencies (databases, network services) in unit
  tests.

## One Logical Assertion Per Test

Each test should verify one specific behaviour.

Tests that verify multiple behaviours are harder to understand, harder
to debug when they fail, and more likely to mask regressions.

Good:

```
def test_returns_error_when_email_is_missing():
    result = register_user(email=None)
    assert result.is_error()

def test_returns_error_when_email_is_invalid():
    result = register_user(email="not-an-email")
    assert result.is_error()
```

## Tests Are Code. Treat Them That Way.

Tests should follow the same quality standards as production code:

- Descriptive names.
- Clear structure (arrange, act, assert).
- No duplication.
- Regular refactoring.

Poorly maintained tests become a liability.

# The Test Pyramid

The test pyramid describes the optimal distribution of test types:

```
        /\
       /  \
      / E2E\    Few: full-stack, slow, expensive
     /------\
    / Integ- \  Some: service-level, moderate speed
   /  ration  \
  /------------\
 /   Unit      \ Many: fast, isolated, reliable
/    Tests      \
-----------------
```

| Type | Speed | Scope | Confidence | Count |
| --- | --- | --- | --- | --- |
|---------------+---------+---------------+------------+---------|
| Unit tests | Fast | Single unit | Low | Many |
| --- | --- | --- | --- | --- |
| Integration | Moderate | Service/Component | Medium | Some |
| E2E tests | Slow | Full system | High | Few |

## Unit Tests

Test a single unit of behaviour in isolation.

- Fast to run and write.
- Pinpoint failures precisely.
- Enable refactoring with confidence.
- Should form the majority of your test suite.

## Integration Tests

Test that components work together correctly.

Focus on the boundaries between your code and external systems:

- Database queries and transactions.
- API endpoints and request handling.
- Service-to-service communication.

## End-to-End Tests

Test critical user journeys through the full system.

Use sparingly:

- Cover the most important business flows.
- Test deployment and infrastructure integration.
- Accept that they are slow and occasionally flaky.

# Test Structure

## Arrange, Act, Assert

Every test should follow three clear phases:

1. ***Arrange***: Set up the test data and preconditions.
2. ***Act***: Execute the behaviour under test.
3. ***Assert***: Verify the outcome.

Separating these phases makes tests easier to read and debug.

## Descriptive Test Names

Test names should describe the scenario and expected outcome.

Good:

```
test_returns_400_when_email_is_missing
test_sends_welcome_email_after_successful_registration
test_does_not_send_welcome_email_when_registration_fails
```

# What to Test

## Test Public Interfaces

Test the contract that a module exposes to its consumers.

Internal implementation details should not be tested directly. They are
exercised through the public interface.

## Test Boundary Conditions

Errors cluster at boundaries.

Test:

- Empty inputs.
- Maximum inputs.
- Invalid inputs.
- Missing resources.
- Concurrent access.
- Timeouts and failures.

## Test Error Paths

Happy paths are important.

Error paths are where systems fail in production.

Every recoverable error state should have a test.

# What Not to Test

## Framework Code

Do not test behaviour provided by your framework.

Test that your configuration is correct, not that the framework works.

## Generated Code

Do not test code that is generated by tools.

If the generator is trustworthy, the generated code is already tested.

## Infrastructure

Do not test infrastructure behaviour (database transactions, network
retries) in unit tests. Test your integration with infrastructure in
integration tests.

# Test Doubles

| Double Type | Purpose |
| --- | --- |
|-------------+------------------------------------------|
| Stub | Returns a fixed value. |
| --- | --- |
| Mock | Verifies that a method was called. |
| Fake | Provides a lightweight implementation. |
| Spy | Records method calls for later assertion. |

Use fakes for dependencies that are slow or unreliable (databases,
network services). Use mocks sparingly — prefer verifying outcomes over
verifying interactions.

# Anti-patterns

## Testing Without Assertions

A test that does not assert anything provides false confidence.

## Overspecified Tests

Tests that assert on internal implementation details break when the
code is refactored.

Test the observable behaviour, not the internal steps.

## Flaky Tests

A test that sometimes passes and sometimes fails erodes trust in the
entire suite.

Flaky tests should be fixed or removed. Never ignore flaky tests.

# AI Integration

AI assistants can help with testing by:

- Generating test cases from production code.
- Identifying untested boundary conditions.
- Suggesting test data for edge cases.
- Detecting test smells and anti-patterns.
- Converting integration tests to use test doubles.

When asking AI for testing advice, provide:

- The function or module being tested.
- Its inputs, outputs and error states.
- Existing test conventions in the codebase.
- Testing framework and tooling in use.

# Related Documents

- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
- [Engineering Glossary](../../glossary/engineering/README.md)
- [Code Review Playbook](../../playbooks/code-review/README.md)
