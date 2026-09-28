# External Skill and Tool Installation, Pinning, and Update Policy

External skills and security/design/testing tools affect agent behavior and release evidence. Treat them as engineering dependencies.

## Before installation

Record:

- repository and canonical owner;
- exact skill/tool name;
- license;
- intended capability and why existing project tooling is insufficient;
- scripts or binaries it executes;
- filesystem/network/tool permissions;
- installation method;
- selected release/tag/commit;
- rollback/removal path.

Then run `04_SKILL_SECURITY_GATE.md`.

## Pinning

For production work:

- prefer a signed/released version or reviewed commit;
- record the immutable version/commit in project tooling configuration;
- preserve lockfiles/checksums where the ecosystem supports them;
- do not silently move to `latest` during a milestone, incident, or release candidate;
- update intentionally in a dedicated task with regression evidence.

## Update process

1. Read upstream changelog/release notes.
2. Re-run skill security/provenance checks.
3. Diff behavior-relevant instructions/scripts from the pinned version.
4. Identify changed permissions, network access, commands, or output formats.
5. Run pressure/evaluation scenarios relevant to the skill.
6. Run project tests affected by the tool/skill.
7. Record version change and rollback version.
8. Promote only after evidence passes.

## Auto-update policy

Auto-update may be used only for low-risk development tooling when the repository explicitly accepts the risk. It is not the default for:

- agent skills that execute scripts or tools;
- security scanners used as release gates;
- deployment/migration tooling;
- skills with broad filesystem/network permissions;
- release candidate environments.

## Failure policy

If an external provider is unavailable:

- do not weaken acceptance criteria;
- use a documented fallback where possible;
- record evidence limitations;
- block the gate only when the missing evidence is required for the product's risk level.
