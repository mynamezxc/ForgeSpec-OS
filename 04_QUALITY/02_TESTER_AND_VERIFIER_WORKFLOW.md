# Tester and Verifier Workflow

## Separation of intent
Developer agent asks: “How do I satisfy the requirement?”
Verifier/tester asks: “How can I prove this is incomplete or broken?”

## Verification inputs
- requirement/acceptance IDs;
- implementation diff;
- known risk areas;
- environment and data setup;
- previous failures/regressions.

## Verification passes
1. Happy path with real integrations/persistence.
2. Boundary values and invalid input.
3. Permission-denied and unauthorized behavior.
4. Partial dependency/network failure.
5. Retry/duplicate/concurrency behavior where applicable.
6. Refresh/restart/reconnect/reload persistence.
7. Backward compatibility/regression.
8. Operator/debug visibility.

## Evidence standard
Record steps, expected, actual and environment. For UI issues, screenshot/video can supplement but not replace a reproducible description.

## Re-test policy
When a defect is fixed:
- rerun the narrow reproduction;
- run nearby regression tests;
- avoid unrelated full-suite runs unless coupling/risk justifies it.
