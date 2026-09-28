# Rule Classification — Prevent ForgeSpec OS from Polluting Product Design

Every reusable rule belongs to one of three classes.

## Class I — Invariant
A universal execution/quality requirement. Examples:
- do not claim completion without evidence;
- do not silently delete a requirement;
- inspect before replacing existing implementation;
- protect data during migrations;
- preserve context through checkpoints.

Class I rules apply unless an explicit higher-priority instruction changes the process.

## Class D — Default
A preferred approach when Product SPEC is silent. Examples:
- prefer small coherent vertical slices;
- prefer native/simple implementation before adding a dependency;
- prefer backward-compatible contract evolution.

A Product SPEC may override a Default without being considered non-compliant.

## Class C — Conditional Profile
Only activates when a product has a matching capability/risk. Examples:
- offline sync;
- hardware/device discovery;
- multi-tenancy;
- money/accounting;
- realtime collaboration;
- plugin execution;
- public API/SDK;
- high availability.

## Required interpretation
When reading ForgeSpec OS, agents must first ask: “Is this rule invariant, default, or conditional?” Do not enforce conditional requirements on unrelated products.

## Product override documentation
If a Product SPEC intentionally chooses a different approach from a Main default, record the decision only when it materially affects implementation or future maintenance. Do not generate paperwork for trivial deviations.
