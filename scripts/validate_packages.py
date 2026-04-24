#!/usr/bin/env python3
"""Validate the Codex marketplace package staging tree."""
from __future__ import annotations

import json
import os
import py_compile
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
PLUGINS_DIR = ROOT / "plugins"

LEGACY_PATTERNS = {
    "AskUserQuestion": re.compile(r"AskUserQuestion"),
    "CLAUDE_PLUGIN_ROOT": re.compile(r"CLAUDE_PLUGIN_ROOT"),
    ".claude path": re.compile(r"\.claude"),
    "Claude Code": re.compile(r"Claude Code"),
    "Claude word": re.compile(r"\bClaude\b"),
    "Task call": re.compile(r"(?<![A-Za-z0-9_])Task\s*\("),
    "background Task flag": re.compile(r"run_in_background"),
    "legacy plugin manifest": re.compile(r"\.claude-plugin"),
    "legacy command directory": re.compile(r"\bcommands/"),
    "legacy reference directory": re.compile(r"(?:references|scripts)/legacy/"),
    "external pumasi launcher": re.compile(r"\bpumasi\.sh\b|\bpumasi\.cmd\b|\bpumasi-job\b|pumasi\.config\.yaml"),
    "external image launcher": re.compile(r"codex /imagen|codex exec|imagen\.sh"),
}

PORT_NOTE_PATTERNS = {
    "codex-port file": re.compile(r"codex-port"),
    "codex suffixed markdown": re.compile(r"-[Cc]odex\.md"),
    "README-codex": re.compile(r"README-codex"),
    "workflow-codex": re.compile(r"workflow-codex"),
    "template-codex": re.compile(r"template-codex"),
}

TEXT_SUFFIXES = {
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".py",
    ".sh",
    ".svg",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}

TEXT_SCAN_EXCLUDE = {
    Path("scripts") / "validate_packages.py",
    Path("scripts") / "run_package_smoke_tests.sh",
}


@dataclass
class Issue:
    severity: str
    path: Path
    message: str

    def format(self) -> str:
        rel = self.path.relative_to(ROOT) if self.path.is_absolute() else self.path
        return f"{self.severity}: {rel}: {self.message}"


def load_json(path: Path, issues: list[Issue]) -> object | None:
    try:
        with path.open(encoding="utf-8") as f:
            return json.load(f)
    except Exception as exc:  # noqa: BLE001 - validation should report all parse errors.
        issues.append(Issue("ERROR", path, f"invalid JSON: {exc}"))
        return None


def parse_frontmatter(path: Path, issues: list[Issue]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        issues.append(Issue("ERROR", path, "missing YAML-style frontmatter"))
        return {}

    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            issues.append(Issue("ERROR", path, f"invalid frontmatter line: {line}"))
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("\"'")
    return data


def is_text_file(path: Path) -> bool:
    return path.suffix in TEXT_SUFFIXES and path.is_file()


def check_marketplace(issues: list[Issue]) -> list[str]:
    data = load_json(MARKETPLACE, issues)
    if not isinstance(data, dict):
        return []

    plugins = data.get("plugins")
    if not isinstance(plugins, list):
        issues.append(Issue("ERROR", MARKETPLACE, "`plugins` must be a list"))
        return []

    names: list[str] = []
    seen: set[str] = set()
    for entry in plugins:
        if not isinstance(entry, dict):
            issues.append(Issue("ERROR", MARKETPLACE, "plugin entry must be an object"))
            continue

        name = entry.get("name")
        if not isinstance(name, str) or not name:
            issues.append(Issue("ERROR", MARKETPLACE, "plugin entry missing name"))
            continue
        names.append(name)
        if name in seen:
            issues.append(Issue("ERROR", MARKETPLACE, f"duplicate plugin entry: {name}"))
        seen.add(name)

        expected_path = f"./plugins/{name}"
        source = entry.get("source")
        if not isinstance(source, dict) or source.get("source") != "local" or source.get("path") != expected_path:
            issues.append(Issue("ERROR", MARKETPLACE, f"{name} source must be local path {expected_path}"))

        policy = entry.get("policy")
        if not isinstance(policy, dict):
            issues.append(Issue("ERROR", MARKETPLACE, f"{name} missing policy"))
        else:
            if policy.get("installation") not in {"AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"}:
                issues.append(Issue("ERROR", MARKETPLACE, f"{name} invalid policy.installation"))
            if policy.get("authentication") not in {"ON_INSTALL", "ON_USE"}:
                issues.append(Issue("ERROR", MARKETPLACE, f"{name} invalid policy.authentication"))

        if not isinstance(entry.get("category"), str) or not entry.get("category"):
            issues.append(Issue("ERROR", MARKETPLACE, f"{name} missing category"))

    package_names = sorted(p.name for p in PLUGINS_DIR.iterdir() if p.is_dir())
    if sorted(names) != package_names:
        missing = sorted(set(package_names) - set(names))
        extra = sorted(set(names) - set(package_names))
        if missing:
            issues.append(Issue("ERROR", MARKETPLACE, f"packages missing marketplace entries: {', '.join(missing)}"))
        if extra:
            issues.append(Issue("ERROR", MARKETPLACE, f"marketplace entries missing package dirs: {', '.join(extra)}"))

    return names


def check_plugin(package: Path, issues: list[Issue]) -> None:
    manifest_path = package / ".codex-plugin" / "plugin.json"
    if not manifest_path.exists():
        issues.append(Issue("ERROR", package, "missing .codex-plugin/plugin.json"))
        return

    manifest = load_json(manifest_path, issues)
    if not isinstance(manifest, dict):
        return

    if manifest.get("name") != package.name:
        issues.append(Issue("ERROR", manifest_path, "manifest name must match package folder"))

    for key in ("version", "description", "author", "license", "skills", "interface"):
        if key not in manifest:
            issues.append(Issue("ERROR", manifest_path, f"missing required key: {key}"))

    if "[TODO:" in json.dumps(manifest):
        issues.append(Issue("ERROR", manifest_path, "contains TODO placeholder"))

    skills_path = package / str(manifest.get("skills", "./skills/")).rstrip("/")
    if not skills_path.exists() or not skills_path.is_dir():
        issues.append(Issue("ERROR", manifest_path, "skills path does not exist"))

    interface = manifest.get("interface")
    if not isinstance(interface, dict):
        return

    for key in ("displayName", "shortDescription", "longDescription", "developerName", "category", "capabilities", "defaultPrompt"):
        if key not in interface:
            issues.append(Issue("ERROR", manifest_path, f"interface missing key: {key}"))

    for key in ("composerIcon", "logo"):
        value = interface.get(key)
        if isinstance(value, str) and value.startswith("./") and not (package / value[2:]).exists():
            issues.append(Issue("ERROR", manifest_path, f"interface.{key} target does not exist: {value}"))

    if skills_path.exists():
        skill_dirs = [p for p in skills_path.iterdir() if p.is_dir()]
        if not skill_dirs:
            issues.append(Issue("ERROR", skills_path, "plugin has no skills"))
        for skill_dir in skill_dirs:
            check_skill(skill_dir, issues)


def check_skill(skill_dir: Path, issues: list[Issue]) -> None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        issues.append(Issue("ERROR", skill_dir, "missing SKILL.md"))
        return

    frontmatter = parse_frontmatter(skill_md, issues)
    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        issues.append(Issue("ERROR", skill_md, "frontmatter name must be kebab-case"))
    if name and name != skill_dir.name:
        issues.append(Issue("WARN", skill_md, f"skill folder `{skill_dir.name}` differs from frontmatter name `{name}`"))
    if not description:
        issues.append(Issue("ERROR", skill_md, "missing description"))
    if len(description) > 1024:
        issues.append(Issue("ERROR", skill_md, "description exceeds 1024 chars"))

    body = skill_md.read_text(encoding="utf-8", errors="replace")
    for ref in re.findall(r"`((?:references|scripts|assets)/[^`]+)`", body):
        if any(token in ref for token in ("*", "{", "}", "$", "<", ">", "|")):
            continue
        if ref.endswith("/"):
            continue
        if not (skill_dir / ref).exists():
            issues.append(Issue("ERROR", skill_md, f"referenced path does not exist: {ref}"))


def scan_text(issues: list[Issue]) -> None:
    for path in ROOT.rglob("*"):
        if not is_text_file(path):
            continue
        rel = path.relative_to(ROOT)
        if rel in TEXT_SCAN_EXCLUDE:
            continue
        if "logs" in rel.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in LEGACY_PATTERNS.items():
            if pattern.search(text):
                issues.append(Issue("ERROR", path, f"legacy residue found: {label}"))
        for label, pattern in PORT_NOTE_PATTERNS.items():
            if pattern.search(text):
                issues.append(Issue("ERROR", path, f"port-note residue found: {label}"))


def check_legacy_dirs(issues: list[Issue]) -> None:
    for path in PLUGINS_DIR.rglob("legacy"):
        if path.is_dir():
            issues.append(Issue("ERROR", path, "legacy directory must not be packaged"))


def run_syntax_checks(issues: list[Issue]) -> None:
    for path in ROOT.rglob("*.py"):
        tmp_name = ""
        try:
            with tempfile.NamedTemporaryFile(suffix=".pyc", delete=False) as tmp:
                tmp_name = tmp.name
            py_compile.compile(str(path), cfile=tmp_name, doraise=True)
        except py_compile.PyCompileError as exc:
            issues.append(Issue("ERROR", path, str(exc)))
        finally:
            if tmp_name:
                try:
                    os.unlink(tmp_name)
                except FileNotFoundError:
                    pass

    for path in ROOT.rglob("*.sh"):
        proc = subprocess.run(["bash", "-n", str(path)], cwd=ROOT, capture_output=True, text=True)
        if proc.returncode:
            issues.append(Issue("ERROR", path, proc.stderr.strip() or "bash -n failed"))

    for path in ROOT.rglob("*.js"):
        proc = subprocess.run(["node", "--check", str(path)], cwd=ROOT, capture_output=True, text=True)
        if proc.returncode:
            issues.append(Issue("ERROR", path, proc.stderr.strip() or "node --check failed"))


def main() -> int:
    issues: list[Issue] = []
    names = check_marketplace(issues)
    for name in names:
        check_plugin(PLUGINS_DIR / name, issues)
    check_legacy_dirs(issues)
    scan_text(issues)
    run_syntax_checks(issues)

    errors = [issue for issue in issues if issue.severity == "ERROR"]
    warnings = [issue for issue in issues if issue.severity == "WARN"]

    for issue in issues:
        print(issue.format())

    print(f"packages={len(names)} errors={len(errors)} warnings={len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
