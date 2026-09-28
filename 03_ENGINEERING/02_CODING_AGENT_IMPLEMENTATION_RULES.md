# Coding Agent Implementation Rules

## Inspect first
Never create a parallel implementation before checking whether the repository already has an equivalent service, component, model or pattern.

## No fake feature rule
A screen connected to static objects is not a completed feature when real persistence/API behavior is required.

Mocks/fakes are acceptable only for:
- isolated tests;
- explicitly labeled prototypes;
- development fixtures that cannot leak into production paths.

## Business logic placement
Keep canonical business invariants in authoritative domain/service/backend layers. UI validation may duplicate checks for UX, but backend/domain validation remains authoritative.

## Error handling
Do not swallow errors. Distinguish expected domain errors, retryable infrastructure errors and programmer faults. Preserve useful context without leaking secrets.

## Readability
Prefer clear names and cohesive functions/classes over clever compression. Comments should explain why, invariants and non-obvious constraints—not restate syntax.

## Type/contracts
Use types/schemas/contracts supported by the selected stack. Validate external boundaries.

## Generated code
Generated artifacts must be reproducible and not manually diverge from their source schema/templates.

## Cleanup
Before completion, remove accidental debug logs, disabled guards, dead branches, temporary bypasses and obsolete TODOs in required scope.
