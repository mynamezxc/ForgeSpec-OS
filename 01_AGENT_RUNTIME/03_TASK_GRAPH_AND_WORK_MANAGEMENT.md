# Task Graph and Work Management

The task graph must have a conceptual root node equal to the active **Project Goal**. Every mandatory release requirement and scope variant must be reachable from that root through one or more tasks. An orphaned requirement is a completion defect.

## Task sizing
A task should be small enough to verify objectively and large enough to produce meaningful progress. Avoid both:
- mega tasks such as “build backend”; and
- micro tasks such as “rename variable” as top-level milestones.

## Mandatory graph-level fields

Track at graph level:
- Project Goal ID/state;
- mandatory requirement count;
- mandatory scope-variant inventory count;
- release-gate status;
- uncovered requirements/variants;
- next executable tasks.

## Mandatory task fields
```yaml
id: TASK-001
requirements: [REQ-001, REQ-004]
title: ...
status: READY
risk: low|medium|high|critical
depends_on: []
owner: main|subagent:<name>
acceptance:
  - ...
evidence_expected:
  - ...
files_expected: []
notes: ...
```

## Priority model
Prefer tasks that:
1. unblock many dependencies;
2. validate risky architecture assumptions early;
3. create real vertical slices;
4. reduce unknowns;
5. protect existing functionality.

## WIP limits
Keep only a small number of `IN_PROGRESS` tasks per agent. Finish or explicitly block a task before opening many unrelated ones.

## Dependency discipline
Do not mark a dependent feature done if its required dependency is mocked or pending.

## Progress reporting
Track progress by verified requirement coverage, not number of files or lines changed.

## Completion propagation

Task `DONE` updates requirement/scope coverage but does not propagate directly to Project Goal completion. After each task, run the continuation controller. Only the release completion audit may transition the Project Goal to `PRODUCTION_READY`.
