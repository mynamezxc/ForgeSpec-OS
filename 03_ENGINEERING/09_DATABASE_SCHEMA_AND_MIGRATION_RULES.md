# Database Schema and Migration Rules

## Schema design
Use constraints/indexes/types to protect invariants where the database can reliably enforce them.

## Migration requirements
For nontrivial migrations specify:
- forward schema change;
- data backfill/transformation;
- compatibility window;
- locking/downtime risk;
- expected volume/time;
- validation query/check;
- rollback or recovery strategy.

## Large data changes
Prefer bounded batches/checkpoints where a single transaction risks locking or rollback explosion.

## Destructive change
Dropping/rewriting data requires explicit confirmation that old consumers/data are no longer needed and that recovery is possible or intentionally impossible.

## Migration tests
Test from a representative previous schema/data version, not only against a freshly created database.
