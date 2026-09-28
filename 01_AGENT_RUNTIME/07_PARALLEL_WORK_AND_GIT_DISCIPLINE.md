# Parallel Work and Git Discipline

## Parallelization rules
Parallel work is safe when tasks have low write overlap and stable interfaces. High-conflict files should have one writer at a time.

## Before parallel work
- define file/module ownership;
- define shared contract version;
- freeze or coordinate schema changes;
- identify integration order.

## Merge discipline
After integrating subagent/parallel branches:
1. inspect diff, not just merge status;
2. reconcile duplicated abstractions;
3. run affected integration tests;
4. verify generated/migration files;
5. update checkpoint and requirement matrix.

## Commit hygiene
Where repository workflow allows commits:
- keep commits coherent;
- avoid mixing unrelated formatting/refactor with behavior changes;
- include migration/schema artifacts with the feature that needs them;
- never rewrite shared history unless explicitly allowed by project policy.

## Dirty workspace
Do not discard unknown local changes. Determine whether they belong to the user/another task before modifying or resetting them.
