# CLAUDE.md — [Project Name]

<!-- TEMPLATE NOTE: This is a reference example. An AI agent reads this to understand
     the structure and conventions, then writes a project-specific version.
     Sections marked [CUSTOMIZE] need project-specific content.
     Sections marked [CONDITIONAL] should be included only if relevant. -->

## Project Overview

[CUSTOMIZE: One-paragraph project description. What it does, what domain, what approach.]

**Current phase:** Project setup complete. Initial scaffold generated. Ready for first research session.

**Branding:** Externally (README, papers, communication) this project is "[External Name]".

## Repository Structure

```
[package_name]/
├── pyproject.toml
├── CHANGELOG.md         # Session-by-session development log
├── src/[package_name]/
│   ├── config/          # Dataclass configs
│   ├── data/            # Dataset, collator, transforms, loader
│   ├── models/          # Encoders, adapters, model subclasses
│   ├── eval/            # Metrics, evaluation, extraction
│   └── utils/
├── scripts/             # Training, evaluation, export entry points
├── jobs/                # SLURM job scripts (the ONLY way to run GPU workloads)
├── tests/
├── data/                # Local data files (labels, schemas, splits)
├── results/             # Experiment outputs, logs, predictions
└── docs/                # Planning, strategy, experiment tracking
```

## Current Task (agent-updated each session)

- **Branch:** `main` — 0 tests passing
- **Working on:** Session 0: Project scaffold initialized. No code written yet.
- **Strategic context:** TODO — define initial research questions in `docs/research_strategy.md`
- **Key decisions:** See [`docs/decisions_log.md`](docs/decisions_log.md)
- **Base model:** [CUSTOMIZE: e.g., `Qwen/Qwen3-VL-8B-Instruct`] <!-- [CONDITIONAL: only if applicable] -->
- **Known issues:** None yet.
- **Experiment results:** See [`docs/experiment_results.md`](docs/experiment_results.md)
- **Data artifacts:** See [`docs/data_artifacts.md`](docs/data_artifacts.md)

## Agent Board

Multiple Claude Code agents may work on this repo concurrently. This board tracks who is doing what. **Each agent MUST read this section at session start and update it at session end (or when claiming/completing work).**

| Agent | Focus Area | Status | Current Work | Claimed Files/Dirs |
|-------|-----------|--------|-------------|-------------------|
| **A** | — | Idle | — | — |
| **B** | — | Idle | — | — |
| **C** | — | Idle | — | — |

**Rules:**
- Before modifying a file in another agent's claimed dirs, check if it conflicts. Shared files (`CLAUDE.md`, `docs/experiment_results.md`, `docs/decisions_log.md`) are always writable by any agent — use additive edits only (append, don't rewrite other agents' sections).
- If you need something from another agent's work, note the dependency here rather than blocking.
- When done with a workstream, update status to "Done" and remove claimed dirs.

## Experiment Queue

Full history and completed experiments in [`docs/experiment_results.md`](docs/experiment_results.md).

### Wave 0: Baseline Evaluation (TODO)

[CUSTOMIZE: Define your first set of experiments. Each wave should have:]
- Clear hypothesis
- Go/no-go gate with measurable threshold
- Expected outputs and where they land in `results/`

### Future Waves

See [`docs/experiment_results.md`](docs/experiment_results.md) § Experiment Queue for planned waves.

> This section is updated by the agent at the end of each session. See [CHANGELOG.md](CHANGELOG.md) for full history.

## Project Roadmap

High-level milestones. Detailed tracking in [Reference Documents](#reference-documents).

| # | Milestone | Status | Target | Key Deliverable |
|---|-----------|--------|--------|-----------------|
| M0 | Project Setup & Alignment | ✅ | Week 1 | Repo structure, dependencies, cluster access |
| M1 | Evaluation Pipeline | ⬜ | Weeks 2–4 | Benchmark baselines, define primary metric |
| M2 | Initial Training & Ablations | ⬜ | Weeks 4–8 | First training runs, ablation results |
| M3 | Method Improvement | ⬜ | Weeks 8–14 | Core method implementation |
| M4 | Refinement & Analysis | ⬜ | Weeks 14–20 | Ablations, error analysis, final method |
| M5 | Paper & Validation | ⬜ | Weeks 20–26 | Paper submission |

> **Rule:** When a milestone status changes, update BOTH this table AND `docs/milestones.md`.

## Code Style & Philosophy

- **Prefer composition over inheritance** (except where framework requires subclassing).
- **Favor explicit over clever.** No single-letter variables outside list comprehensions. No nested ternaries.
- **Functions should do one thing.** If a docstring needs "and" to describe the function, split it.
- **Return early, avoid deep nesting.** Guard clauses over nested if/else.
- **Dataclasses over dicts** for any structured data that crosses function boundaries.
- **Logging over print.** Use stdlib `logging` — never bare `print()` in library code.
- **Errors should be informative.** Custom exceptions with context, not `raise ValueError("bad input")`.
- **Naming matters.** Variables and functions should be self-documenting. If you need a comment to explain *what* a variable holds, rename it instead.

## Critical Rules

### Git Discipline
- **`main` is the development trunk.** Short-lived feature branches off `main`, merge back when done. No long-lived dev branches.
- **Push at session end** — always ask for confirmation first.
- Atomic commits. Run linting + tests before every commit. Do not commit broken code.

### [Framework Name] Usage
<!-- [CONDITIONAL: Include only if the project has a core framework with specific rules] -->
[CUSTOMIZE: e.g., "Prefer the official `merlin-vlm` package. Never reimplement the architecture from scratch."]

### Code Standards
- Python 3.11+. Type hints on all function signatures.
- Use `ruff` for linting and formatting (config in `pyproject.toml`).
- No hardcoded paths. All data paths via environment variable or CLI args.
- No monkey-patching. Proper subclassing only.
- Docstrings on all public functions (Google style).
- No use of `Any` type hints as a shortcut. Be specific.

### Anti-Patterns (Do NOT)
- Do not add `try/except: pass` or broad exception swallowing. Catch specific exceptions.
- Do not add dependencies without checking if existing deps already cover the need.
- Do not write "utility" grab-bag modules. Every module has a single clear purpose.
- Do not generate placeholder/stub implementations unless explicitly asked. Either implement fully or flag as `TODO:` with a clear description.
- Do not refactor code that isn't part of the current task without asking first.
- Do not chain multiple large changes without a checkpoint. Implement incrementally.
- Do not silently change function signatures or return types — these are API boundaries.

## Workflow Protocol

1. Before writing code, state the plan in 3–5 bullet points. Wait for approval.
2. Implement in small, testable increments. Commit after each working increment.
3. After completing a logical unit of work, run:
   - `uv run ruff check src/ tests/`
   - `uv run ruff format --check src/ tests/`
   - `uv run pytest tests/ -x -q`
4. Write a summary of changes before committing: what changed, why, what to verify.
5. Never chain multiple large changes without a checkpoint.

### Session Wrap-Up Protocol

When the user signals the session is ending ("wrap up", "end session", "that's it for today"), execute in order:

1. **Run tests and linting.** Fix failures before proceeding.
2. **Commit all pending work** with clear, atomic messages.
3. **Append a session entry to `CHANGELOG.md`** using the template in [`docs/templates/changelog_entry.md`](docs/templates/changelog_entry.md).
4. **Update project docs:**
   - `CLAUDE.md` → "Current Task" (branch, test count, what's done, blockers, next steps)
   - `CLAUDE.md` → "Agent Board" table (update your row's status and current work)
   - `CLAUDE.md` → "Project Roadmap" table if milestones changed
   - `docs/milestones.md` — flip completed items (⬜→✅), mark in-progress (🔄), add dates. Assess against actual codebase state.
   - `README.md` — sync Roadmap table. Update scripts/features if user-facing changes.
5. **Push to origin** (`git push`).
6. **Print a session summary** to chat.

**Do not skip steps. Do not ask "should I update the changelog?" — just do it.**
**Do not consider a session complete until docs are updated.**

## Review Protocol

### Self-Review (before every commit)
1. Does this change do exactly one thing? State it in one sentence.
2. Are all new public functions tested?
3. Does `ruff check` and `pytest` pass?
4. Any hardcoded values, broad excepts, or missing type hints?
5. Would the function signatures make sense to someone reading only the API?

### Human Review (at checkpoints)
Do not proceed past these without user approval:
- New module or subpackage creation
- Any change to public API signatures
- Metric implementations (correctness is critical)
- Anything touching data loading or preprocessing pipelines
- Before merging branches

## Cluster Handover Protocol

When a milestone needs GPU execution, create or update `jobs/README_RUN.md` with: summary, exact commands (copy-paste ready), expected output, expected runtime, specific sanity checks, known limitations, and what the results unlock. See [`docs/templates/handover.md`](docs/templates/handover.md) for the full template.

### SLURM Job Script Standards

Every job script in `jobs/` must have: descriptive filename, `#SBATCH` headers (name, output, GPU, time), git hash logging, env var logging, UV activation, output to `results/`, and `set -euo pipefail`.

**Required preamble:** Copy from [`jobs/PREAMBLE.sh`](jobs/PREAMBLE.sh) for every new SLURM script. The same pattern applies to inline `sbatch --wrap` commands.

**Critical rules:**
- **NEVER use `${VAR:?error}`** — use `${VAR:-default}` with hardcoded fallback. SLURM nodes don't inherit login shell.
- **NEVER rely on `~/.bashrc` alone** — always provide defaults.

## Technical Environment

<!-- [CUSTOMIZE: Fill in your specific setup] -->
**Base model:** [e.g., `Qwen/Qwen3-VL-8B-Instruct`]
**Primary metric:** [e.g., macro F1]
**Per-user GPU limit:** [e.g., 4] GPUs

**Execution environments:**
- **SLURM cluster:** All batch experiments via `sbatch`. Job scripts in `jobs/`.
- **Local dev:** Quick debugging, single-sample inference, tests.
- **CPU-only:** Tests and linting only.

**Do not verify environment setup.** Dependencies installed, data at `$DATA_ROOT`. UV is the sole package manager (`uv sync`). New dependencies → edit `pyproject.toml` + `uv sync`. See `README.md` for setup.

**Code portability:** Tests run on CPU with synthetic data. Never silently fail on CPU.

### Login Node Rules

Login nodes are shared. **All non-trivial compute → SLURM.**

**Allowed:** file inspection, git, `uv sync`/`ruff`/`pytest`, SLURM commands (`sbatch`/`squeue`/`sacct`/`scancel`), quick `python -c`, `curl`.
**Must use SLURM:** API calls, full dataset processing, GPU workloads, anything > ~2 minutes.

**Resource sizing:** `gpu:0` for CPU jobs · `gpu:1` only for model loading · `--cpus-per-task` matched to parallelism · `168:00:00` default time.

**Ad-hoc jobs** (without a permanent script):
```bash
sbatch --job-name=quick-task --output=results/quick_%j.log \
  --gres=gpu:0 --mem=16G --cpus-per-task=2 --time=168:00:00 \
  --partition=part-1 \
  --wrap='
source ~/.bashrc 2>/dev/null || true
export DATA_ROOT="${DATA_ROOT:-/path/to/data}"
cd '"$(pwd)"' && source .venv/bin/activate
export SSL_CERT_FILE="$(python -c "import certifi; print(certifi.where())" 2>/dev/null || echo "")"
python scripts/my_script.py ...
'
```

## Testing

Tests prevent regression across agentic sessions — they are the institutional memory of the project.

**Always test:** metric computations (scientific correctness non-negotiable), data loading/transforms (silent shape/dtype bugs), extraction/parsing logic (fragile), shared functions.
**Smoke tests fine for:** model wrapper forward passes, config loading, CLI parsing.
**Don't test:** visualization/plotting, one-off scripts, SLURM templates.

**Standards:** Arrange-Act-Assert · `pytest` fixtures, not setUp/tearDown · names: `test_<function>_<scenario>_<expected>` · mock external services (offline, <30s) · GPU code tested via mocked outputs and fixture predictions · `uv run pytest tests/ -x -q` before committing.

## Current Strategy

TODO — Define your research strategy in [`docs/research_strategy.md`](docs/research_strategy.md).

**Every piece of code should trace back to a table in [`results/results_scaffold.md`](results/results_scaffold.md).** If it doesn't serve a result, question whether it's needed now.

## Dataset

<!-- [CUSTOMIZE: Describe your dataset structure] -->
[Brief description of the dataset.]

Data at `$DATA_ROOT` (default: `/path/to/data`).

```
$DATA_ROOT/
├── ...                  # Add your data layout
```

### Data Loading Rules
- No hardcoded paths. All data paths via env var or CLI args.
- Use official train/val/test splits. Never reshuffle.

## Environment Variables

<!-- [CUSTOMIZE: List your project's env vars] -->
| Variable | Description | Default |
|----------|-------------|---------|
| `DATA_ROOT` | Root directory for dataset | `/path/to/data` |

<!-- [CONDITIONAL: Include if using judge API] -->
| `JUDGE_API_BASE` | LLM judge API endpoint | `http://localhost:8267/v1` |
| `JUDGE_MODEL` | Judge model name | `qwen3-32b-awq` |

<!-- [CONDITIONAL: Include if using W&B] -->
| `WANDB_PROJECT` | W&B project name | `my-project` |

**Shell expansion caveat (CRITICAL):** The Bash tool starts a fresh shell. Env vars may NOT expand. **Always use hardcoded paths in Bash tool calls.**

Env var references are fine in SLURM job scripts and Python code — just not in interactive Bash tool commands.

## W&B Experiment Tracking
<!-- [CONDITIONAL: Include only if using W&B] -->

| Project | Phase | Description |
|---------|-------|-------------|
| `my-project` | M1+ | All experiment runs |

## Documentation Standards
- **README.md** — single source of truth for setup, usage, project overview. Update with every feature.
- **CHANGELOG.md** — single source of truth for session history. Never skip an entry.
- Scripts in `scripts/` — `--help` CLI interface (argparse/typer) + docstring with purpose, example usage, expected I/O.
- Non-obvious design decisions — inline comments explaining *why*, not *what*.
- New metrics/models/features — update README.md usage section.

## Reference Documents

**Active planning (`docs/`):**
- [`decisions_log.md`](docs/decisions_log.md) — Chronological key decisions log
- [`experiment_results.md`](docs/experiment_results.md) — All experiment tables and queue
- [`data_artifacts.md`](docs/data_artifacts.md) — Versioned label files, embeddings, result directories
- [`milestones.md`](docs/milestones.md) — Phased milestone tracker (detailed checklist)
- [`implementation_plan.md`](docs/implementation_plan.md) — Full implementation plan (all phases)
- [`research_strategy.md`](docs/research_strategy.md) — Research questions and experiment design
- `docs/templates/` — Templates for changelog, handover, council reports, SOPs
- `docs/research_strategy/` — Council reports and alignment strategies

**Results:** [`results/results_scaffold.md`](results/results_scaffold.md) — paper tables, required output formats, phase mapping.

**Read-only reference (`.context/`):**
- Add external documentation, paper summaries, reference implementations here.
- These files are for agent context only — never modify them programmatically.
