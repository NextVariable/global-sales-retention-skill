#!/usr/bin/env python3
"""Check package portability and recorded test integrity, not business quality."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def package_errors():
    errors = []
    entries = list((ROOT / "skills").glob("*/SKILL.md"))
    if len(entries) != 1:
        return ["repository must contain exactly one installable skill"]
    skill = entries[0].parent
    text = entries[0].read_text(encoding="utf-8")
    front = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    fields = dict(re.findall(r"^(name|description):\s*(.+)$", front[1], re.M)) if front else {}
    if (
        fields.get("name") != skill.name
        or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill.name)
        or len(skill.name) > 64
    ):
        errors.append("invalid or mismatching skill name")
    if not 0 < len(fields.get("description", "")) <= 1024:
        errors.append("description must be a nonempty single line of at most 1024 characters")
    if not (skill / "LICENSE").is_file():
        errors.append("install unit is missing LICENSE")
    metadata = skill / "agents/openai.yaml"
    if not metadata.is_file():
        errors.append("missing client metadata")
    else:
        ui = metadata.read_text(encoding="utf-8")
        for field in ("display_name", "short_description", "default_prompt"):
            if not re.search(rf'^  {field}: "[^"\n]+"$', ui, re.M):
                errors.append(f"missing or invalid quoted metadata field: {field}")
        if f"${skill.name}" not in ui:
            errors.append("default prompt is missing invocation")
        short = re.search(r'^  short_description: "([^"\n]+)"$', ui, re.M)
        if short and not 25 <= len(short[1]) <= 64:
            errors.append("short_description must contain 25 to 64 characters")
    for path in sorted(skill.rglob("*")):
        if path.is_symlink():
            errors.append(f"symlink in install unit: {path.relative_to(skill)}")
        if not path.is_file() or path.suffix not in (".md", ".yaml", ".py"):
            continue
        body = path.read_text(encoding="utf-8")
        if re.search(r"/(?:Users|home)/[^\s/]+/", body):
            errors.append(f"personal absolute path in {path.relative_to(skill)}")
        if path.suffix != ".md":
            continue
        body = re.sub(r"```.*?```", "", body, flags=re.S)
        for link in re.findall(r"\[[^\]\n]+\]\(([^)]+)\)", body):
            target = link.split("#", 1)[0].strip("<>")
            if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue
            dest = (path.parent / target).resolve()
            if not dest.is_relative_to(skill.resolve()) or not dest.exists():
                errors.append(
                    f"broken or external local dependency: {path.relative_to(skill)}/{target}"
                )
    return errors


def evidence_errors():
    manifest = ROOT / "validation/forward-tests/manifest.json"
    if not manifest.exists():
        return []
    data = json.loads(manifest.read_text(encoding="utf-8"))
    errors = []
    records = data.get("cases", [])
    if not records:
        errors.append("test manifest has no recorded cases")
    if len({c["id"] for c in records}) != len(records):
        errors.append("duplicate test case IDs")
    for record in records:
        for kind in ("input", "output"):
            path = (manifest.parent / record[f"{kind}_file"]).resolve()
            if not path.is_relative_to(manifest.parent.resolve()) or not path.is_file():
                errors.append(f"invalid {kind} path: {record['id']}")
            elif sha(path) != record[f"{kind}_sha256"]:
                errors.append(f"changed {kind}: {record['id']}")
    # Match both the file set and content, so added untested methods are visible.
    accepted = data.get("accepted_runtime_sha256", {})
    actual = {
        p.relative_to(ROOT).as_posix(): sha(p)
        for p in (ROOT / "skills").rglob("*")
        if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"
    }
    if not accepted or set(accepted) != set(actual):
        errors.append("runtime file set changed since acceptance")
    for rel, digest in accepted.items():
        path = (ROOT / rel).resolve()
        if (
            not path.is_relative_to((ROOT / "skills").resolve())
            or not path.is_file()
            or sha(path) != digest
        ):
            errors.append(f"runtime changed since acceptance: {rel}")
    return errors


def documentation_errors(root):
    """Check maintained documentation links; raw historical outputs are not rewritten."""
    errors = []
    files = [root / "README.md", root / "CONTRIBUTING.md"]
    files += list((root / "docs").rglob("*.md"))
    files += list((root / "examples").rglob("*.md"))
    for path in files:
        if not path.is_file():
            continue
        body = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for link in re.findall(r"\[[^\]\n]+\]\(([^)]+)\)", body):
            target = link.split("#", 1)[0].strip("<>")
            if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(f"broken documentation link: {path.relative_to(root)} -> {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="optional directory for validation report")
    args = parser.parse_args()
    doc_errors = documentation_errors(ROOT)
    checks = [{"name": "repository-docs", "passed": not doc_errors, "errors": doc_errors}]
    for name, action in (
        ("portable-package", package_errors),
        ("recorded-evidence", evidence_errors),
    ):
        try:
            errors = action()
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors = [str(exc)]
        checks.append({"name": name, "passed": not errors, "errors": errors})
    if list((ROOT / "tests").glob("test_*.py")):
        run = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        checks.append(
            {
                "name": "calculation-tests",
                "passed": run.returncode == 0,
                "output": run.stdout + run.stderr,
            }
        )
    report = {
        "passed": all(check["passed"] for check in checks),
        "checks": checks,
        "scope": "Structure and recorded evidence integrity. This does not grade model output or prove business outcomes.",
    }
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.output:
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / "report.json").write_text(rendered + "\n", encoding="utf-8")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
