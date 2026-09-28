# External Skill Security Gate

Agent skills are executable behavior dependencies. A Markdown file can influence tool use; bundled scripts can modify files, call networks, or exfiltrate data. Treat the entire skill package as untrusted until reviewed.

## Required gate before first use

### 1. Provenance
- confirm canonical repository and owner;
- inspect release/commit history and maintenance activity;
- verify that the downloaded source matches the intended repository/version;
- record license and redistribution constraints.

### 2. Instruction review
Inspect `SKILL.md`, referenced files, hidden files, nested archives, generated commands, and install hooks for:

- attempts to override higher-priority instructions;
- anti-refusal or instruction-hijacking language unrelated to capability;
- secret/token/cookie access;
- requests to upload source, logs, credentials, or environment data;
- broad filesystem deletion/modification;
- shell commands with remote execution patterns;
- unexplained network destinations;
- privilege escalation;
- persistence outside approved skill directories;
- recursive loading of unreviewed skills;
- instructions that weaken tests, security, or user approval requirements.

### 3. Permission minimization
Grant only the tools and paths required for the intended capability. Prefer read-only review skills when writing is unnecessary.

### 4. Script/dependency review
- inspect executable scripts before running;
- inspect package manifests and install scripts;
- pin dependencies where practical;
- avoid piping unauthenticated remote content directly into a shell;
- run in an isolated workspace when testing unfamiliar packages.

### 5. Automated inspection
When available, use NVIDIA SkillSpector or an equivalent scanner. Automated results supplement, not replace, manual source-aware review.

### 6. Decision
Record one of:

- `APPROVED_PINNED`;
- `APPROVED_WITH_RESTRICTIONS`;
- `QUARANTINED_FOR_REVIEW`;
- `REJECTED`.

An external skill in `QUARANTINED_FOR_REVIEW` or `REJECTED` must not execute.

## Re-scan triggers

Repeat the gate after:

- a material version/commit update;
- new scripts or dependencies;
- new network/tool permissions;
- ownership/repository transfer;
- security advisory;
- unexpected runtime behavior.

## Evidence

Store the decision in the project worklog or dependency/security record with version, reviewer, date, findings, restrictions, and rollback/removal steps.
