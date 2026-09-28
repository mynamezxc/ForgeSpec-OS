# Business Logic Specification Method

Business logic must be explicit enough that two independent implementers reach compatible behavior.

## For each important domain process define
- actors and authority;
- trigger;
- prerequisites;
- canonical state before;
- state transition;
- calculations/rules;
- side effects;
- events/notifications;
- permissions;
- idempotency/retry behavior;
- cancellation/reversal;
- error outcomes;
- audit requirements;
- time/date/timezone behavior;
- concurrency conflict behavior.

## Invariants
State invariants as rules that must always hold, for example:
- an approved object cannot return to draft without an explicit reversal transition;
- a payment allocation cannot exceed authoritative available amount;
- a tenant cannot access another tenant's record;
- a finalized sequence number is immutable.

## Derived versus stored values
The Product SPEC should state which values are authoritative stored facts and which are derived, cached or projections. This prevents duplicated calculations from drifting.

## Workflow diagrams
Text state machines are preferred for precision; diagrams may supplement them. Every transition should map to permissions, validation and tests.
