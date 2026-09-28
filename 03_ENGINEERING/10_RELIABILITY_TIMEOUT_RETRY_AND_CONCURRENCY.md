# Reliability — Timeout, Retry, Idempotency and Concurrency

## Remote calls
Every remote dependency should have an intentional timeout. Infinite/default waits are not a reliability strategy.

## Retries
Retry only operations that are safe or protected by idempotency/deduplication. Use bounded retry/backoff; avoid synchronized retry storms.

## Idempotency
Use stable operation keys or domain deduplication where duplicate requests/events can create duplicate side effects.

## Concurrency
Identify race-prone flows such as inventory decrement, payments, sequence allocation, seat/slot booking, approval transitions and sync conflict resolution.

Choose appropriate control:
- transaction isolation;
- unique constraint;
- optimistic version/check;
- row/advisory lock;
- serialized queue;
- domain conflict resolution.

## Partial success
When one operation touches multiple systems, define compensation/reconciliation instead of pretending distributed atomicity exists.
