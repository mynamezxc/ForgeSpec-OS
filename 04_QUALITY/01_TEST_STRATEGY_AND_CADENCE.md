# Test Strategy and Cadence

Testing must maximize signal per unit time. Do not rerun the entire suite after every small edit.

## Test layers
1. **Static/cheap checks** — syntax, types, lint, schema validation.
2. **Unit tests** — pure/domain logic and edge cases.
3. **Integration tests** — DB, queues, providers/adapters, modules.
4. **Contract tests** — API/event/provider compatibility.
5. **E2E tests** — critical real user/operator journeys.
6. **Non-functional tests** — performance, security, recovery, offline/concurrency as applicable.

## Adaptive cadence
After a small local change:
- run targeted cheap checks and directly relevant tests.

After a coherent task:
- run targeted unit + integration/contract tests for affected modules.

After approximately 3–7 meaningful tasks **or earlier if a cross-cutting/high-risk change occurs**:
- run selected critical E2E/regression scenarios.

At milestone/release-candidate:
- run the full applicable regression/release suite.

The number 3–7 is a heuristic, not a ritual. Use change risk and coupling to decide.

## High-risk changes
Immediately expand verification for:
- auth/permissions;
- schema migrations;
- money/accounting calculations;
- concurrency/idempotency;
- shared core libraries;
- sync/offline engine;
- deployment/runtime bootstrap.

## Flaky tests
Do not normalize flakiness. Track root cause, quarantine only with explicit owner/reason and do not count quarantined critical coverage as passing.

## Specialist testing skills

Use `07_SKILLS/01_SKILL_ROUTER.md` to activate browser, accessibility, component, performance, or security evidence providers by risk. Tool availability must not cause every test type to run after every edit; preserve this document's staged cadence.
