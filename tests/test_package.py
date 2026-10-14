#!/usr/bin/env python3
"""Repository-level checks for the ai-prompting skill."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest
from importlib.util import module_from_spec, spec_from_file_location
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills/ai-prompting"
SKILL = SKILL_DIR / "SKILL.md"
MANIFEST = ROOT / "packaging/MANUS_SOURCE_MANIFEST.txt"
PATH_RE = re.compile(r"`((?:references|templates|examples)/[A-Za-z0-9_.-]+\.md)`")


def frontmatter(text: str) -> dict:
    return yaml.safe_load(text.split("---", 2)[1])


def resolve(path: str) -> Path:
    """Skill paths are relative to the skill folder. Manus files written for the
    old layout say templates/X.md and examples/X.md; those now live flat."""
    if path.startswith("templates/"):
        path = "references/TEMPLATE_" + path[len("templates/"):]
    elif path.startswith("examples/"):
        path = "references/EXAMPLE_" + path[len("examples/"):]
    return SKILL_DIR / path


class PackageTests(unittest.TestCase):
    @unittest.skipUnless(os.name == "posix" and shutil.which("bash"), "requires POSIX bash")
    def test_workflow_run_steps_have_valid_bash_syntax(self) -> None:
        for workflow in sorted((ROOT / ".github/workflows").glob("*.yml")):
            data = yaml.safe_load(workflow.read_text(encoding="utf-8"))
            for job in data["jobs"].values():
                for step in job["steps"]:
                    if "run" not in step:
                        continue
                    with self.subTest(workflow=workflow.name, step=step.get("name")):
                        result = subprocess.run(
                            ["bash", "-n"], input=step["run"], text=True,
                            capture_output=True, check=False,
                        )
                        self.assertEqual(result.returncode, 0, result.stderr)

    def test_frontmatter(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        fm = frontmatter(text)
        self.assertEqual(fm["name"], SKILL_DIR.name)
        self.assertLessEqual(len(fm["description"]), 1024)
        front_lines = text.split("---\n")[1].splitlines()
        self.assertTrue(any(l.startswith("name: ") for l in front_lines))
        self.assertTrue(any(l.startswith("description: ") for l in front_lines),
                        "Opal needs a single-line description")

    def test_versions_agree(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        expected = frontmatter(text)["metadata"]["version"]
        for path in (ROOT / ".codex-plugin/plugin.json", ROOT / ".claude-plugin/plugin.json"):
            with self.subTest(path=path):
                self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["version"], expected)
        self.assertRegex((ROOT / "README.md").read_text(encoding="utf-8"), rf"`{re.escape(expected)}`")
        self.assertTrue((ROOT / f"packaging/RELEASE_NOTES_v{expected}.md").is_file())
        self.assertIn(f"Loaded AI Prompting v{expected}", text)

    def test_marketplace_lists_plugin(self) -> None:
        data = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        self.assertIn("ai-prompting", [p["name"] for p in data["plugins"]])
        self.assertEqual(data["plugins"][0]["source"], "./")

    def test_layout_is_flat(self) -> None:
        # Opal imports only SKILL.md + references/*.md; keep every reference flat.
        for p in SKILL_DIR.rglob("*"):
            if p.is_file():
                rel = p.relative_to(SKILL_DIR).as_posix()
                with self.subTest(rel=rel):
                    self.assertTrue(rel == "SKILL.md" or rel == "agents/openai.yaml"
                                    or re.fullmatch(r"references/[^/]+\.md", rel))
                    self.assertNotIn(b"\r", p.read_bytes())

    def test_every_path_resolves(self) -> None:
        for doc in [SKILL, *sorted((SKILL_DIR / "references").glob("*.md"))]:
            for target in PATH_RE.findall(doc.read_text(encoding="utf-8")):
                with self.subTest(doc=doc.name, target=target):
                    self.assertTrue(resolve(target).is_file())

    def test_manus_files_byte_identical(self) -> None:
        rows = [l.split("  ") for l in MANIFEST.read_text(encoding="utf-8").splitlines() if l.strip()]
        files = [r for r in rows if not r[1].startswith("SKILL.md")]
        self.assertEqual(len(files), 30)
        for sha, _source, target in files:
            with self.subTest(target=target):
                self.assertEqual(hashlib.sha256((SKILL_DIR / target).read_bytes()).hexdigest(), sha)

    def test_manus_body_differs_only_by_template_paths(self) -> None:
        body_sha = next(l.split("  ")[0] for l in MANIFEST.read_text(encoding="utf-8").splitlines()
                        if "#body" in l)
        text = (SKILL_DIR / "references/manus.md").read_text(encoding="utf-8")
        body = text.split("---\n", 2)[2]
        body = body.replace("`references/TEMPLATE_", "`templates/").replace("`references/EXAMPLE_", "`examples/")
        self.assertEqual(hashlib.sha256(body.encode("utf-8")).hexdigest(), body_sha)

    def test_routing_table_files_exist(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        table = text.split("## Part 2", 1)[1]
        for target in re.findall(r"`(references/[a-z0-9-]+\.md)`", table):
            with self.subTest(target=target):
                self.assertTrue((SKILL_DIR / target).is_file())

    def test_receiving_agent_route_fits_opal_read(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        body = text.split("---\n", 2)[2]
        self.assertLess(len(body), 9500)
        self.assertIn("agent receiving", body.lower())
        self.assertIn("No receiving agent named", body)

    def test_openai_default_prompt_names_skill(self) -> None:
        data = yaml.safe_load((SKILL_DIR / "agents/openai.yaml").read_text(encoding="utf-8"))
        self.assertIn("$ai-prompting", data["interface"]["default_prompt"])

    def test_copilot_package_contains_all_markdown_references(self) -> None:
        spec = spec_from_file_location("build_packages", ROOT / "packaging/build_packages.py")
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        files = module.source_files()
        package, _folders = module.build_packages(files)["microsoft-copilot-agent-only"]
        expected = {"ai-prompting/SKILL.md", "ai-prompting/INSTALL.md"}
        expected.update("ai-prompting/" + n for n in files if n.startswith("references/"))
        self.assertEqual(set(package), expected)
        self.assertIn(b"Loaded AI Prompting v1.0.8", package["ai-prompting/INSTALL.md"])

    def test_package_verification_survives_optimized_python(self) -> None:
        script = (
            "import importlib.util, pathlib, sys, tempfile, zipfile; "
            "p = pathlib.Path(sys.argv[1]); "
            "s = importlib.util.spec_from_file_location('builder', p); "
            "b = importlib.util.module_from_spec(s); s.loader.exec_module(b); "
            "z = pathlib.Path(tempfile.mkdtemp()) / 'ai-prompting-verify-probe.zip'; "
            "f = zipfile.ZipFile(z, 'w'); f.writestr('wrong.txt', b'wrong'); f.close(); "
            "b.verify(z, 'UNIVERSAL-skill', {'ai-prompting/SKILL.md': b'correct'}, set(), {})"
        )
        result = subprocess.run(
            [os.sys.executable, "-O", "-c", script, str(ROOT / "packaging/build_packages.py")],
            capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Package check failed", result.stderr)

    def test_source_files_refuses_linked_entries(self) -> None:
        spec = spec_from_file_location("build_packages_link_test", ROOT / "packaging/build_packages.py")
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            skill = repo / "skills/ai-prompting"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("test\n", encoding="utf-8")
            target = repo / "target.txt"
            target.write_text("test\n", encoding="utf-8")
            try:
                (skill / "linked.txt").symlink_to(target)
            except OSError as error:
                self.skipTest("symlink creation unavailable: " + str(error))
            with patch.object(module, "REPO", repo), patch.object(module, "SKILL", skill):
                with self.assertRaisesRegex(ValueError, "Refusing linked package source"):
                    module.source_files()


if __name__ == "__main__":
    unittest.main()
