#!/usr/bin/env python3
"""Project initializer for agentic-research-template.

Renders template files with project-specific values and copies them
to an output directory. Two modes:
  - Interactive: prompts for each value (default)
  - Config-driven: reads from a JSON file (--config)

stdlib only — no Jinja, no cookiecutter. Works on any HPC.

Usage:
    python init.py --output ~/dev/my-new-project
    python init.py --config init_config.example.json --output /tmp/test-project
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from datetime import date
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent / "template"

# Placeholders use {{KEY}} syntax.
PLACEHOLDER_RE = re.compile(r"\{\{(\w+)\}\}")

# Conditional blocks: {{#IF KEY}} ... {{/IF KEY}}
CONDITIONAL_BLOCK_RE = re.compile(
    r"\{\{#IF (\w+)\}\}\n?(.*?)\{\{/IF \1\}\}\n?",
    re.DOTALL,
)

# Negated conditional blocks: {{#UNLESS KEY}} ... {{/UNLESS KEY}}
UNLESS_BLOCK_RE = re.compile(
    r"\{\{#UNLESS (\w+)\}\}\n?(.*?)\{\{/UNLESS \1\}\}\n?",
    re.DOTALL,
)

# File extensions to render (text files with potential placeholders).
RENDERABLE_EXTENSIONS = {
    ".md", ".py", ".sh", ".toml", ".txt", ".json", ".yaml", ".yml",
    ".cfg", ".ini", ".gitignore",
}


def slugify(name: str) -> str:
    """Convert project name to a valid Python package name."""
    slug = re.sub(r"[^a-zA-Z0-9]", "_", name.lower())
    slug = re.sub(r"_+", "_", slug).strip("_")
    if slug and slug[0].isdigit():
        slug = "_" + slug
    return slug


def prompt_value(key: str, description: str, default: str = "") -> str:
    """Prompt the user for a configuration value."""
    if default:
        raw = input(f"  {description} [{default}]: ").strip()
        return raw if raw else default
    while True:
        raw = input(f"  {description}: ").strip()
        if raw:
            return raw
        print("    (required)")


def prompt_bool(key: str, description: str, default: bool = False) -> bool:
    """Prompt the user for a yes/no value."""
    suffix = "[Y/n]" if default else "[y/N]"
    raw = input(f"  {description} {suffix}: ").strip().lower()
    if not raw:
        return default
    return raw in ("y", "yes", "1", "true")


def gather_interactive() -> dict[str, str]:
    """Gather configuration values interactively."""
    print("\n=== Project Identity ===")
    project_name = prompt_value("PROJECT_NAME", "Project name (human-readable)", "MyProject")
    package_name = prompt_value("PACKAGE_NAME", "Python package name", slugify(project_name))
    external_name = prompt_value("EXTERNAL_NAME", "External/branding name", project_name)
    project_description = prompt_value("PROJECT_DESCRIPTION", "One-line project description")
    author_name = prompt_value("AUTHOR_NAME", "Author name")
    author_email = prompt_value("AUTHOR_EMAIL", "Author email")
    github_username = prompt_value("GITHUB_USERNAME", "GitHub username")

    print("\n=== Python & Tooling ===")
    python_version = prompt_value("PYTHON_VERSION", "Minimum Python version", "3.11")

    print("\n=== Model & Framework ===")
    base_model = prompt_value("BASE_MODEL", "Base model (HuggingFace ID or name)", "")
    primary_metric = prompt_value("PRIMARY_METRIC", "Primary evaluation metric", "macro F1")
    framework_name = prompt_value("FRAMEWORK_NAME", "Core framework/library name", "")
    framework_rules = prompt_value(
        "FRAMEWORK_RULES",
        "Framework usage rules (or leave blank)",
        "",
    )

    print("\n=== Data ===")
    data_root_var = prompt_value("DATA_ROOT_VAR", "Data root env var name", "DATA_ROOT")
    data_root_default = prompt_value("DATA_ROOT_DEFAULT", "Default data path", "/home/data/my_dataset")
    shared_data_dir = prompt_value("SHARED_DATA_DIR", "Shared data parent directory", "/home/data/")
    data_description = prompt_value("DATA_DESCRIPTION", "Brief dataset description", "")

    print("\n=== HPC / Cluster ===")
    gpu_count_per_user = prompt_value("GPU_COUNT_PER_USER", "Max GPUs per user", "4")
    degraded_node_name = prompt_value(
        "DEGRADED_NODE_NAME",
        "Degraded node hostname (blank to skip)",
        "",
    )
    degraded_node_scratch = ""
    if degraded_node_name:
        degraded_node_scratch = prompt_value(
            "DEGRADED_NODE_SCRATCH",
            f"Scratch path on {degraded_node_name}",
            f"/scratch/{os.environ.get('USER', 'user')}/data",
        )

    print("\n=== Evaluation / Judge API ===")
    judge_api_enabled = prompt_bool("JUDGE_API_ENABLED", "Use LLM judge API?", default=False)
    judge_model = ""
    judge_api_default = ""
    if judge_api_enabled:
        judge_model = prompt_value("JUDGE_MODEL", "Judge model name", "qwen3-32b-awq")
        judge_api_default = prompt_value("JUDGE_API_DEFAULT", "Default judge API URL", "http://localhost:8267/v1")

    print("\n=== Experiment Tracking ===")
    wandb_enabled = prompt_bool("WANDB_ENABLED", "Use Weights & Biases?", default=True)
    wandb_project = ""
    if wandb_enabled:
        wandb_project = prompt_value("WANDB_PROJECT", "W&B project name", slugify(project_name))

    return _build_context(locals())


def gather_from_config(config_path: str) -> dict[str, str]:
    """Load configuration from a JSON file."""
    with open(config_path) as f:
        raw = json.load(f)

    return _build_context(raw)


def _build_context(raw: dict) -> dict[str, str]:
    """Normalize raw config into the template context dict."""
    # Normalize keys to UPPER_SNAKE_CASE
    ctx: dict[str, str] = {}
    for k, v in raw.items():
        key = k.upper()
        if isinstance(v, bool):
            ctx[key] = "1" if v else ""
        elif isinstance(v, (int, float)):
            ctx[key] = str(v)
        else:
            ctx[key] = str(v) if v else ""

    # Derive values
    if "PACKAGE_NAME" not in ctx or not ctx["PACKAGE_NAME"]:
        ctx["PACKAGE_NAME"] = slugify(ctx.get("PROJECT_NAME", "myproject"))
    if "EXTERNAL_NAME" not in ctx or not ctx["EXTERNAL_NAME"]:
        ctx["EXTERNAL_NAME"] = ctx.get("PROJECT_NAME", "MyProject")
    ctx["DATE_TODAY"] = date.today().isoformat()
    ctx["YEAR"] = str(date.today().year)

    # Boolean flags (truthy = non-empty string)
    ctx.setdefault("JUDGE_API_ENABLED", "1" if ctx.get("JUDGE_MODEL") else "")
    ctx.setdefault("WANDB_ENABLED", "1" if ctx.get("WANDB_PROJECT") else "")
    ctx.setdefault("DEGRADED_NODE_ENABLED", "1" if ctx.get("DEGRADED_NODE_NAME") else "")
    ctx.setdefault("FRAMEWORK_RULES_ENABLED", "1" if ctx.get("FRAMEWORK_RULES") else "")

    # Defaults
    ctx.setdefault("PROJECT_NAME", "MyProject")
    ctx.setdefault("PROJECT_DESCRIPTION", "A research project.")
    ctx.setdefault("AUTHOR_NAME", "Author")
    ctx.setdefault("AUTHOR_EMAIL", "author@example.com")
    ctx.setdefault("GITHUB_USERNAME", "username")
    ctx.setdefault("PYTHON_VERSION", "3.11")
    ctx.setdefault("BASE_MODEL", "")
    ctx.setdefault("PRIMARY_METRIC", "macro F1")
    ctx.setdefault("FRAMEWORK_NAME", "")
    ctx.setdefault("FRAMEWORK_RULES", "")
    ctx.setdefault("DATA_ROOT_VAR", "DATA_ROOT")
    ctx.setdefault("DATA_ROOT_DEFAULT", "/home/data/my_dataset")
    ctx.setdefault("SHARED_DATA_DIR", "/home/data/")
    ctx.setdefault("DATA_DESCRIPTION", "")
    ctx.setdefault("GPU_COUNT_PER_USER", "4")
    ctx.setdefault("DEGRADED_NODE_NAME", "")
    ctx.setdefault("DEGRADED_NODE_SCRATCH", "")
    ctx.setdefault("JUDGE_MODEL", "")
    ctx.setdefault("JUDGE_API_DEFAULT", "")
    ctx.setdefault("WANDB_PROJECT", "")

    return ctx


def render_text(content: str, ctx: dict[str, str]) -> str:
    """Render template text: resolve conditionals, then substitute placeholders."""
    # Process {{#IF KEY}} ... {{/IF KEY}} blocks
    def replace_if(match: re.Match) -> str:
        key = match.group(1)
        body = match.group(2)
        if ctx.get(key):
            return body
        return ""

    content = CONDITIONAL_BLOCK_RE.sub(replace_if, content)

    # Process {{#UNLESS KEY}} ... {{/UNLESS KEY}} blocks
    def replace_unless(match: re.Match) -> str:
        key = match.group(1)
        body = match.group(2)
        if not ctx.get(key):
            return body
        return ""

    content = UNLESS_BLOCK_RE.sub(replace_unless, content)

    # Substitute {{KEY}} placeholders
    def replace_placeholder(match: re.Match) -> str:
        key = match.group(1)
        return ctx.get(key, match.group(0))  # Leave unresolved if missing

    content = PLACEHOLDER_RE.sub(replace_placeholder, content)

    return content


def is_renderable(path: Path) -> bool:
    """Check if a file should have placeholders rendered."""
    if path.suffix in RENDERABLE_EXTENSIONS:
        return True
    if path.name in {".gitignore", ".gitkeep", "Makefile"}:
        return True
    return False


def copy_and_render(
    template_dir: Path,
    output_dir: Path,
    ctx: dict[str, str],
) -> list[str]:
    """Copy template tree to output, rendering placeholders in text files."""
    rendered_files: list[str] = []
    package_name = ctx["PACKAGE_NAME"]

    for src_path in sorted(template_dir.rglob("*")):
        if src_path.is_dir():
            continue

        # Compute relative path, replacing {{PACKAGE_NAME}} in directory names
        rel = src_path.relative_to(template_dir)
        rel_str = str(rel).replace("{{PACKAGE_NAME}}", package_name)
        dst_path = output_dir / rel_str

        # Create parent directories
        dst_path.parent.mkdir(parents=True, exist_ok=True)

        if is_renderable(src_path):
            content = src_path.read_text(encoding="utf-8")
            rendered = render_text(content, ctx)
            dst_path.write_text(rendered, encoding="utf-8")
            rendered_files.append(rel_str)
        else:
            shutil.copy2(src_path, dst_path)

    return rendered_files


def check_unresolved(output_dir: Path) -> list[tuple[str, list[str]]]:
    """Find any remaining unresolved {{PLACEHOLDER}} tokens."""
    issues: list[tuple[str, list[str]]] = []
    for path in sorted(output_dir.rglob("*")):
        if not path.is_file():
            continue
        if not is_renderable(path):
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue
        matches = PLACEHOLDER_RE.findall(content)
        if matches:
            rel = path.relative_to(output_dir)
            issues.append((str(rel), sorted(set(matches))))
    return issues


def print_post_init(output_dir: Path, ctx: dict[str, str]) -> None:
    """Print post-initialization instructions."""
    print(f"\n{'=' * 60}")
    print(f"  Project initialized at: {output_dir}")
    print(f"{'=' * 60}")
    print()
    print("Next steps:")
    print()
    print(f"  1. cd {output_dir}")
    print(f"  2. git init && git add -A && git commit -m 'Initial project scaffold'")
    print()
    print("  3. Set up Python environment:")
    print(f"     uv venv --python {ctx.get('PYTHON_VERSION', '3.11')}")
    print("     uv sync")
    print()
    print("  4. Copy global Claude files (optional but recommended):")
    print(f"     cp {output_dir}/global_claude_md/CLAUDE.md ~/.claude/CLAUDE.md")
    print("     # Review and customize the global rules for your cluster")
    print()
    print("  5. Review and customize:")
    print("     - CLAUDE.md        (project instructions for Claude Code)")
    print("     - docs/milestones.md")
    print("     - docs/research_strategy.md")
    print("     - jobs/PREAMBLE.sh (SLURM preamble for your cluster)")
    print()
    print("  6. Start your first Claude Code session!")
    print()


def main() -> None:
    """Entry point."""
    parser = argparse.ArgumentParser(
        description="Initialize a new research project from the agentic-research-template.",
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to a JSON config file (skips interactive prompts).",
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Output directory for the new project.",
    )
    args = parser.parse_args()

    output_dir = Path(args.output).resolve()

    if output_dir.exists() and any(output_dir.iterdir()):
        print(f"ERROR: Output directory is not empty: {output_dir}", file=sys.stderr)
        print("  Use an empty directory or a new path.", file=sys.stderr)
        sys.exit(1)

    # Gather configuration
    if args.config:
        print(f"Loading config from: {args.config}")
        ctx = gather_from_config(args.config)
    else:
        print("=== agentic-research-template initializer ===")
        print("Press Enter to accept defaults shown in [brackets].\n")
        ctx = gather_interactive()

    print(f"\nRendering project: {ctx['PROJECT_NAME']} -> {output_dir}")

    # Copy and render
    output_dir.mkdir(parents=True, exist_ok=True)
    rendered_files = copy_and_render(TEMPLATE_DIR, output_dir, ctx)

    # Move global_claude_md and global_memory to top level for easy access
    # (They're reference files, not part of the project tree)

    print(f"  Rendered {len(rendered_files)} files.")

    # Check for unresolved placeholders
    issues = check_unresolved(output_dir)
    if issues:
        print("\nWARNING: Unresolved placeholders found:")
        for filepath, keys in issues:
            print(f"  {filepath}: {', '.join(keys)}")
        print("  These may be intentional TODOs or missing config values.")

    print_post_init(output_dir, ctx)


if __name__ == "__main__":
    main()
