---
name: forgespec-skill-inspector
description: Reviews external agent skills before installation or upgrade for provenance, prompt injection, data exfiltration, excessive agency, dangerous scripts, permissions, and supply-chain risk. Use whenever adding or materially updating a third-party skill.
---

# ForgeSpec Skill Inspector

Follow `07_SKILLS/04_SKILL_SECURITY_GATE.md`.

## Preferred provider
Use NVIDIA SkillSpector when available, then perform manual source-aware review for significant permissions/scripts.

## Required output
- source repository and owner;
- exact version/commit;
- license;
- scripts/dependencies/network destinations;
- requested tool/filesystem permissions;
- automated findings if scanner used;
- manual findings;
- restrictions;
- decision: `APPROVED_PINNED`, `APPROVED_WITH_RESTRICTIONS`, `QUARANTINED_FOR_REVIEW`, or `REJECTED`;
- rollback/removal instructions.

No skill may approve itself.
