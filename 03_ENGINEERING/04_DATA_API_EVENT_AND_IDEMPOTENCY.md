# Data, API, Event and Idempotency Rules

## Data ownership
Every mutable business entity has one authoritative owner. Other modules access it through approved contracts, not hidden direct writes.

## API contracts
Specify:
- request/response schemas;
- error codes/semantics;
- authentication/authorization;
- pagination/filter/sort;
- idempotency where retries can duplicate effects;
- versioning/deprecation;
- limits/timeouts.

## Events/jobs
Specify:
- producer and consumer;
- delivery semantics;
- ordering needs;
- deduplication/idempotency;
- retry/backoff;
- poison/dead-letter behavior;
- schema evolution;
- observability/correlation.

## Transactions and concurrency
Document invariants that require atomicity, locking, optimistic concurrency or conflict resolution. Do not rely on UI sequencing to protect data integrity.

## Time and money
Use explicit timezone rules and stable monetary precision/rounding rules when applicable.
