---
name: forgespec-supply-chain
description: Audits dependencies, containers, repository configuration, secrets, licenses, and toolchain provenance with reproducible scanner versions and remediation decisions. Use for dependency changes, images, CI/CD, and release gates.
---

# ForgeSpec Supply Chain

## Workflow
1. Identify changed manifests, lockfiles, base images, build tools, CI actions, plugins, downloaded binaries, and external skills.
2. Prefer lockfile/source-aware dependency scans such as OSV-Scanner where supported.
3. Use Trivy or an approved equivalent for repository/image vulnerabilities, misconfiguration, secrets, and license signals when those surfaces apply.
4. Triage by affected version, reachability/exposure, exploitability, fix availability, runtime context, and transitive/direct ownership.
5. Verify dependency source and package integrity; avoid typo-squatting and unreviewed install scripts.
6. For container images, inspect base image provenance, unnecessary packages, user privileges, exposed secrets, and update path.
7. For CI, pin third-party actions/tools where the platform permits and restrict token permissions.
8. Record accepted risk with owner, rationale, expiry/review trigger, and compensating control.

## Tool trust
Security scanners are dependencies too. Pin reviewed versions, follow upstream advisories, and do not equate `latest` with safe.
