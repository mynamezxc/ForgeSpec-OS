# Architecture and Modularity Rules

## Boundaries
Organize by stable domain/module boundaries rather than arbitrary technical layers when that improves ownership. Each module should make clear:
- responsibilities;
- owned data;
- public interfaces;
- dependencies;
- extension points;
- forbidden coupling.

## Dependency direction
Prefer dependencies toward stable abstractions/domain contracts. Avoid circular module dependencies.

## Shared code
Shared libraries must be justified by genuine reuse. Do not create a “common” dumping ground.

## Extensibility
Design explicit extension points only where Product SPEC requires likely variation: providers, integrations, workflows, strategies, feature modules, device adapters, etc.

## Configuration over forks
When customer/environment differences are predictable, prefer configuration/extension contracts over copy-pasted codebases.

## Failure isolation
Remote services, hardware, plugins and optional modules should fail in bounded ways. One optional integration should not crash unrelated core workflows.

## Backward compatibility
Public contracts require versioning or compatibility strategy. Internal refactors must not silently break external consumers.
