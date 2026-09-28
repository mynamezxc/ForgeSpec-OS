# E2E Stability and Maintenance

E2E suites should protect critical journeys, not mirror every low-level branch.

## Stable selectors
Prefer accessibility/semantic/test IDs over brittle CSS/layout selectors.

## E2E boundaries
Cover business outcomes such as login -> create -> approve -> persist -> reload, rather than testing one button per test when those steps only make sense together.

## Failure evidence
Capture relevant logs, network/error response and screenshots on failure. Avoid giant video artifacts for every passing test unless required.

## Flake reduction
Control clocks, seed randomness, wait on deterministic state rather than arbitrary sleep, isolate test data and eliminate shared-account contention.
