#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_VERSION = "1.0.1"

REQUIRED = [
    "README.md",
    "AGENT_ENTRYPOINT.md",
    "AGENT_START_PROMPT.md",
    "AGENT_FILE_INDEX.md",
    "PROMPT_BUILD_PRODUCT_SPEC.md",
    "forgespec-policy.json",
    "00_GOVERNANCE/07_PROJECT_GOAL_AND_TERMINAL_STATE.md",
    "01_AGENT_RUNTIME/10_AUTONOMOUS_CONTINUATION_CONTROLLER.md",
    "02_SPEC_FACTORY/09_RELEASE_GOAL_AND_SCOPE_CLOSURE.md",
    "04_QUALITY/10_AGENT_BEHAVIOR_REGRESSION_TESTS.md",
    "06_TEMPLATES/PROJECT_GOAL_TEMPLATE.md",
    "06_TEMPLATES/EXECUTION_STATE_TEMPLATE.md",
]

errors: list[str] = []

for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

for rel in ["forgespec-policy.json", "PACKAGE_MANIFEST.json"]:
    try:
        data = json.loads((ROOT / rel).read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid JSON {rel}: {exc}")
        continue
    if data.get("version") != EXPECTED_VERSION:
        errors.append(f"{rel} version={data.get('version')!r}, expected {EXPECTED_VERSION!r}")

entry = (ROOT / "AGENT_ENTRYPOINT.md").read_text(encoding="utf-8")
if f"**Version:** {EXPECTED_VERSION}" not in entry:
    errors.append("AGENT_ENTRYPOINT.md version mismatch")

prompt = (ROOT / "AGENT_START_PROMPT.md").read_text(encoding="utf-8")
for required_phrase in [
    "PROJECT_GOAL.md",
    "TASK_DONE != MILESTONE_DONE != PROJECT_DONE",
    "CONTINUATION_REQUIRED",
    "select the next task and continue",
]:
    if required_phrase not in prompt:
        errors.append(f"AGENT_START_PROMPT.md missing control phrase: {required_phrase}")

policy = json.loads((ROOT / "forgespec-policy.json").read_text(encoding="utf-8"))
for key in [
    "project_goal_required_for_substantial_implementation",
    "known_remaining_executable_work_forbids_terminal_completion",
    "scope_enumeration_preservation_required",
    "post_task_continuation_required",
]:
    if policy.get(key) is not True:
        errors.append(f"policy invariant not enabled: {key}")

for md in ROOT.rglob("*.md"):
    text = md.read_text(encoding="utf-8")
    if text.count("```") % 2:
        errors.append(f"unbalanced markdown fences: {md.relative_to(ROOT)}")
    if re.search(r"\b1\.3\.0\b|\bv1\.3(?:\.0)?\b|\b1\.2\.0\b|\bv1\.2\.0\b", text):
        errors.append(f"stale version reference: {md.relative_to(ROOT)}")

if (ROOT / "FILE_INDEX.md").exists():
    errors.append("obsolete FILE_INDEX.md exists; AGENT_FILE_INDEX.md should be canonical")

if errors:
    print("ForgeSpec OS validation FAILED")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print(f"ForgeSpec OS {EXPECTED_VERSION} validation passed")
print(f"Files: {sum(1 for p in ROOT.rglob('*') if p.is_file())}")
print("Project Goal / continuation controls: present")
