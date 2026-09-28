# Failure Pattern — Scope Collapse to a Representative Variant

## Signal

A Product SPEC or coding agent receives a broad explicit list of mandatory variants but implements only one familiar or early example and treats it as sufficient coverage.

Examples of variant dimensions:

- industries;
- sales channels;
- roles;
- app modules;
- payment methods;
- providers/integrations;
- locales;
- device/runtime targets.

## Root causes

- prose lists are not converted into stable scope IDs;
- roadmap names one example prominently and hides the rest in narrative text;
- acceptance matrices cover workflows but not variant dimensions;
- vertical-slice strategy is confused with release-scope reduction;
- shared/core implementation is incorrectly assumed to prove every variant-specific behavior.

## Countermeasure

Create a mandatory scope-closure matrix and connect every release-blocking variant to requirement IDs, tasks, evidence, and release gates.

A representative variant may validate shared architecture, but it cannot close other mandatory variants unless the Product SPEC explicitly states that no variant-specific behavior remains.

## Regression test

Given a Product SPEC with multiple mandatory variants, verify that:

1. every named variant appears in `RELEASE_GOAL_AND_SCOPE.md` and `PROJECT_GOAL.md`;
2. every mandatory variant has coverage/evidence status;
3. the release gate remains blocked while any release-blocking variant is incomplete;
4. completion of the first variant automatically selects work from the remaining variant inventory.
