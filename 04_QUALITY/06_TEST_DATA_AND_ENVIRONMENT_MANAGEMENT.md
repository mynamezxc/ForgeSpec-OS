# Test Data and Environment Management

## Deterministic tests
Prefer controlled factories/fixtures and isolated state. Tests should not depend on execution order unless intentionally testing sequence.

## Realistic datasets
Use synthetic/anonymized representative shapes for performance and migration testing. Include skew, nulls, long strings, old records and unusual states that production can contain.

## External providers
Use layered tests:
- mocked contract tests for deterministic edge cases;
- sandbox/staging integration tests where available;
- minimal live smoke tests only when justified.

## Cleanup
Tests that create external/stateful artifacts must clean up safely or use namespaced disposable environments.
