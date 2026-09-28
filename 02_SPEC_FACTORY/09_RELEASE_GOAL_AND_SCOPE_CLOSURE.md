# Release Goal and Scope-Closure Specification

A Product SPEC must make the requested delivery boundary machine-checkable. Otherwise a coding agent may legitimately confuse "the next milestone" with "the whole product requested in this release."

## 1. Required release-goal artifact

Create:

`SPEC/<product>/07_DELIVERY/RELEASE_GOAL_AND_SCOPE.md`

It must define:

- release goal;
- release-level success predicate;
- mandatory requirement groups;
- mandatory variants/enumerations;
- deferred/non-goal scope;
- release gates;
- production-readiness expectations;
- dependencies and external assumptions;
- blocker policy;
- traceability to the acceptance matrix.

## 2. Enumeration-preservation rule

When the user's product idea or Product SPEC names several items in one category, preserve them as a structured matrix instead of collapsing them into a single representative example.

Example categories:

- industry packs;
- business models;
- sales/service channels;
- user roles;
- regions/locales;
- integrations;
- payment methods;
- app/modules;
- device types;
- deployment modes.

Each mandatory item should have a stable ID or map to stable requirement IDs.

## 3. Example-versus-obligation distinction

Words such as "for example", "e.g.", or a named reference workflow do not automatically make that example the full release scope.

The SPEC generator must determine whether the example is:

- illustrative only;
- a mandatory instance;
- the first implementation order;
- the only requested scope.

If the surrounding intent clearly requires broader coverage, preserve the broader coverage explicitly.

## 4. Scope-closure matrix

For any multi-variant product, add a closure table that can answer:

| Variant / domain | Required? | Requirement IDs | Implementation status | Evidence | Release blocking? |
|---|---:|---|---|---|---:|

A release cannot become `PRODUCTION_READY` while a mandatory release-blocking row is incomplete.

## 5. Vertical-slice planning rule

Vertical slices are an implementation strategy, not a scope-reduction strategy.

A Product SPEC roadmap must explicitly state:

- which release requirements each slice closes;
- what remains after the slice;
- which next slice becomes eligible;
- whether the slice is independently deployable;
- whether release is still blocked after the slice.

## 6. Release boundary lint

Before finalizing a Product SPEC, verify:

- the release goal is not merely a milestone name;
- all explicit named scope lists are represented;
- every mandatory workflow has acceptance criteria;
- shared/core requirements are separated from variant-specific requirements;
- one representative module cannot satisfy multiple mandatory variants unless the SPEC explicitly defines shared behavior as sufficient;
- release blockers are distinguishable from future enhancements.
