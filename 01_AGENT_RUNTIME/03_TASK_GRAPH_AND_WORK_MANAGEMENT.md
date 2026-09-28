# Task Graph and Work Management

## Task sizing
A task should be small enough to verify objectively and large enough to produce meaningful progress. Avoid both:
- mega tasks such as “build backend”; and
- micro tasks such as “rename variable” as top-level milestones.

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
