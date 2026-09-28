# Context Budget and Token Economy

The objective is not minimal context; it is **minimum sufficient context for correct execution**.

## Context tiers
### Tier 0 — Always hot
Keep concise:
- Project Goal ID/state and terminal predicate;
- mandatory scope coverage summary;
- current objective;
- current task IDs;
- critical invariants;
- latest blockers;
- next executable action and 2–6 following candidates.

### Tier 1 — Pull when task touches it
- relevant Product SPEC sections;
- module contracts;
- active ADRs;
- related tests;
- recent diff.

### Tier 2 — Retrieve only on demand
- old worklogs;
- unrelated modules;
- historical benchmark detail;
- completed task implementation detail.

## Avoid token waste
- Do not repeatedly paste full files when references/paths are enough.
- Do not ask subagents to reread the whole repository.
- Summarize tool output into durable facts after extracting evidence.
- Prefer structured checkpoint tables over narrative transcripts.
- Do not re-explain architecture every turn unless it changed.
- Do not generate speculative future modules during an active implementation task.

## Compression trigger behavior
When context is becoming crowded, checkpoint before loss of precision. Compression is a state-transfer operation, not a restart.

## Post-compression verification budget
Re-read only active scope plus checkpoint, then inspect actual repository state. Do not spend a large token budget reconstructing already-completed work from conversation history if the repository/checkpoint is authoritative.
