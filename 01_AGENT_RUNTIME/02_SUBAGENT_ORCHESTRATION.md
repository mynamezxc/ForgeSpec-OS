# Subagent Orchestration

## Why use subagents
Use subagents to increase parallelism and independent verification, not to outsource thinking blindly.

Good subagent boundaries:
- repository reconnaissance;
- domain/API research;
- isolated component implementation;
- migration review;
- test authoring;
- security review;
- UI/UX audit;
- benchmark design;
- regression verification.

Avoid spawning a subagent when coordination cost exceeds the work, or when two agents would modify the same hot files concurrently.

## Required assignment packet
Every subagent receives:
- objective;
- exact scope and exclusions;
- relevant requirement IDs;
- files/modules it may edit;
- invariants that must remain true;
- expected deliverables;
- tests/evidence required;
- known context and dependencies.

## Required return packet
A subagent must return:
1. Summary of work.
2. Files changed or inspected.
3. Decisions/assumptions.
4. Tests/commands and outcomes.
5. Known limitations/risks.
6. Requirement coverage.
7. Follow-up actions if any.

“Done” without this packet is not accepted.

## Main-agent responsibilities
The main agent remains accountable for:
- architecture consistency;
- conflict resolution;
- merging competing changes;
- integration tests;
- requirement completeness;
- final release verdict.

## Independent verifier pattern
For high-risk or high-impact changes, prefer a verifier subagent that did not implement the feature. It should try to falsify completion by checking edge cases, contract mismatches, security, migration and regression risks.

## Context budget
Do not send the entire repository/history to every subagent. Give focused context and references. Require concise evidence-based returns that can be merged into the central checkpoint.
