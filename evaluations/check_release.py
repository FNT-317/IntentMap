#!/usr/bin/env python3
"""Dependency-free structural checks for the IntentMap v0.1 release candidate.

This script checks files, identifiers, frontmatter, and local Markdown links. It
does not run IntentMap conversations or claim behavioral model coverage.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "agents/openai.yaml",
    "docs/product-principles.md",
    "references/requirement-discovery.md",
    "references/dynamic-questioning.md",
    "references/confirmation-checkpoints.md",
    "references/requirement-discovery-examples.md",
    "references/scope-definition.md",
    "references/scope-definition-examples.md",
    "references/task-decomposition.md",
    "references/task-decomposition-examples.md",
    "references/final-codex-task-generation.md",
    "references/final-codex-task-generation-examples.md",
    "references/post-execution-review.md",
    "references/post-execution-review-examples.md",
    "evaluations/README.md",
    "evaluations/scenarios.md",
    "evaluations/rubric.md",
    "evaluations/failure-modes.md",
    "evaluations/context-and-task-sizing.md",
    "evaluations/stress-test-report.md",
    "evaluations/check_release.py",
)

EXAMPLE_COUNTS = {
    "references/requirement-discovery-examples.md": 5,
    "references/scope-definition-examples.md": 5,
    "references/task-decomposition-examples.md": 7,
    "references/final-codex-task-generation-examples.md": 8,
    "references/post-execution-review-examples.md": 10,
}


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def check_required_files(errors: list[str]) -> None:
    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path
        if not path.is_file():
            errors.append(f"missing required file: {relative_path}")


def check_skill_frontmatter(errors: list[str]) -> None:
    skill = read("SKILL.md")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", skill, re.DOTALL)
    if not match:
        errors.append("SKILL.md does not start with a closed YAML frontmatter block")
        return

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            errors.append(f"unsupported SKILL.md frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"\'')

    if set(fields) != {"name", "description"}:
        errors.append("SKILL.md frontmatter must contain exactly name and description")

    name = fields.get("name", "")
    description = fields.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("skill name must use lowercase letters, numbers, and single hyphens")
    if not 1 <= len(name) <= 64:
        errors.append("skill name must be 1–64 characters")
    if not 1 <= len(description) <= 1024:
        errors.append("skill description must be 1–1024 characters")
    if len(skill.splitlines()) > 120:
        errors.append("SKILL.md is no longer a concise router (more than 120 lines)")


def check_agent_metadata(errors: list[str]) -> None:
    metadata = read("agents/openai.yaml")
    for key in ("interface:", "display_name:", "short_description:", "default_prompt:"):
        if key not in metadata:
            errors.append(f"agents/openai.yaml is missing {key}")
    if "$intentmap" not in metadata:
        errors.append("agents/openai.yaml default prompt must invoke $intentmap")


def check_markdown_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for source in ROOT.rglob("*.md"):
        text = source.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().strip("<>")
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            resolved = (source.parent / target).resolve()
            if not resolved.exists():
                relative_source = source.relative_to(ROOT).as_posix()
                errors.append(f"broken local link in {relative_source}: {raw_target}")


def check_ids(errors: list[str]) -> None:
    scenarios = read("evaluations/scenarios.md")
    scenario_ids = re.findall(r"^### S(\d{2})\b", scenarios, re.MULTILINE)
    expected_scenarios = [f"{number:02d}" for number in range(1, 33)]
    if scenario_ids != expected_scenarios:
        errors.append(f"scenario headings must be exactly S01–S32 in order; found {scenario_ids}")
    for scenario_id in expected_scenarios:
        heading = re.search(
            rf"^### S{scenario_id}\b(.*?)(?=^### S\d{{2}}\b|\Z)",
            scenarios,
            re.MULTILINE | re.DOTALL,
        )
        if not heading:
            continue
        for label in ("Start", "Stress", "Expected", "Fail if"):
            if f"**{label}:**" not in heading.group(0):
                errors.append(f"S{scenario_id} is missing the {label} field")

    rubric_ids = re.findall(r"^\| R(\d{2}) \|", read("evaluations/rubric.md"), re.MULTILINE)
    expected_rubric = [f"{number:02d}" for number in range(1, 26)]
    if rubric_ids != expected_rubric:
        errors.append("rubric rows must be exactly R01–R25 in order")

    failure_ids = re.findall(r"^\| F(\d{2}) \|", read("evaluations/failure-modes.md"), re.MULTILINE)
    expected_failures = [f"{number:02d}" for number in range(1, 27)]
    if failure_ids != expected_failures:
        errors.append("failure-mode rows must be exactly F01–F26 in order")


def check_examples(errors: list[str]) -> None:
    for relative_path, expected_count in EXAMPLE_COUNTS.items():
        count = len(re.findall(r"^## \d+\.", read(relative_path), re.MULTILINE))
        if count != expected_count:
            errors.append(
                f"{relative_path} should contain {expected_count} numbered examples; found {count}"
            )


def check_production_separation(errors: list[str]) -> None:
    production_files = [ROOT / "SKILL.md", ROOT / "docs" / "product-principles.md"]
    production_files.extend((ROOT / "references").glob("*.md"))
    for path in production_files:
        if "evaluations/" in path.read_text(encoding="utf-8").replace("\\", "/"):
            relative_path = path.relative_to(ROOT).as_posix()
            errors.append(f"production instruction links to evaluation-only content: {relative_path}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    if not errors:
        check_skill_frontmatter(errors)
        check_agent_metadata(errors)
        check_markdown_links(errors)
        check_ids(errors)
        check_examples(errors)
        check_production_separation(errors)

    if errors:
        print("Structural release checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Structural release checks passed. This does not run behavioral model evaluations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
