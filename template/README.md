# [Project Name]

[CUSTOMIZE: One-paragraph project description.]

## Setup

### Prerequisites
- Python 3.11+
- [uv](https://github.com/astral-sh/uv) for package management
- Access to SLURM cluster (for GPU workloads)

### Installation

```bash
git clone https://github.com/[username]/[repo].git
cd [repo]

uv venv --python 3.11
uv sync
uv sync --group dev
```

### Environment Variables

<!-- [CUSTOMIZE: List your project's env vars] -->
| Variable | Description | Default |
|----------|-------------|---------|
| `DATA_ROOT` | Root directory for dataset | `/path/to/data` |

## Usage

### Running Tests

```bash
uv run pytest tests/ -x -q
```

### Linting

```bash
uv run ruff check src/ tests/
uv run ruff format --check src/ tests/
```

### SLURM Jobs

All GPU workloads run via SLURM. Job scripts are in `jobs/`.

```bash
sbatch jobs/<script_name>.sh
squeue -u $USER
tail -f results/<job_output>.log
```

## Project Structure

```
├── src/[package]/       # Main package
│   ├── config/          # Configuration dataclasses
│   ├── data/            # Data loading and transforms
│   ├── models/          # Model definitions
│   ├── eval/            # Evaluation metrics
│   └── utils/           # Utilities
├── scripts/             # CLI entry points
├── jobs/                # SLURM job scripts
├── tests/               # Test suite
├── data/                # Local data files
├── results/             # Experiment outputs
└── docs/                # Documentation
```

## Roadmap

| # | Milestone | Status |
|---|-----------|--------|
| M0 | Project Setup | ✅ |
| M1 | Evaluation Pipeline | ⬜ |
| M2 | Initial Training | ⬜ |
| M3 | Method Improvement | ⬜ |
| M4 | Refinement | ⬜ |
| M5 | Paper | ⬜ |

## Development

This project uses [Claude Code](https://claude.com/claude-code) for AI-assisted development. See `CLAUDE.md` for project instructions and workflow protocols.

## License

MIT
