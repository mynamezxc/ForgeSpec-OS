#!/usr/bin/env python3
"""Validate ForgeSpec OS skill metadata and core machine-readable files.

Read-only, standard-library-only validator intended for CI or local maintenance.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    policy_path = ROOT / "forgespec-policy.json"
    registry_path = ROOT / "07_SKILLS" / "skill-registry.json"
    try:
        policy = json.loads(policy_path.read_text(encoding="utf-8"))
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"JSON parse failure: {exc}", file=sys.stderr)
        return 1

    if policy.get("version") != registry.get("forgespec_version"):
        fail("Policy and skill registry ForgeSpec versions differ", errors)

    skill_files = sorted((ROOT / "07_SKILLS" / "skills").glob("*/SKILL.md"))
    if not skill_files:
        fail("No ForgeSpec SKILL.md files found", errors)

    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            fail(f"Missing YAML frontmatter: {path.relative_to(ROOT)}", errors)
            continue
        close = text.find("\n---\n", 4)
        if close < 0:
            fail(f"Unclosed YAML frontmatter: {path.relative_to(ROOT)}", errors)
            continue
        fm = text[4:close]
        name = re.search(r"^name:\s*(.+)$", fm, re.M)
        description = re.search(r"^description:\s*(.+)$", fm, re.M)
        if not name or not description:
            fail(f"Missing name/description: {path.relative_to(ROOT)}", errors)
            continue
        if name.group(1).strip() != path.parent.name:
            fail(f"Skill name/folder mismatch: {path.relative_to(ROOT)}", errors)

    provider_ids = [p.get("id") for p in registry.get("providers", [])]
    if len(provider_ids) != len(set(provider_ids)):
        fail("Duplicate provider IDs in skill-registry.json", errors)

    required = [
        ROOT / "AGENT_ENTRYPOINT.md",
        ROOT / "AGENT_FILE_INDEX.md",
        ROOT / "07_SKILLS" / "01_SKILL_ROUTER.md",
        ROOT / "07_SKILLS" / "04_SKILL_SECURITY_GATE.md",
        ROOT / "07_SKILLS" / "07_EVIDENCE_AND_HANDOFF_CONTRACT.md",
    ]
    for path in required:
        if not path.exists():
            fail(f"Required file missing: {path.relative_to(ROOT)}", errors)

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    print(f"ForgeSpec OS {policy.get('version')} validation passed")
    print(f"Local skills: {len(skill_files)}")
    print(f"Curated external providers: {len(provider_ids)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
