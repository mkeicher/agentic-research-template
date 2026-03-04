# {{EXTERNAL_NAME}}

{{PROJECT_DESCRIPTION}}

## Setup

### Prerequisites
- Python {{PYTHON_VERSION}}+
- [uv](https://github.com/astral-sh/uv) for package management
- Access to SLURM cluster (for GPU workloads)

### Installation

```bash
# Clone the repository
git clone https://github.com/{{GITHUB_USERNAME}}/{{PACKAGE_NAME}}.git
cd {{PACKAGE_NAME}}

# Create virtual environment and install dependencies
uv venv --python {{PYTHON_VERSION}}
uv sync

# Install dev dependencies
uv sync --group dev
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `{{DATA_ROOT_VAR}}` | Root directory for dataset | `{{DATA_ROOT_DEFAULT}}` |
{{#IF WANDB_ENABLED}}
| `WANDB_PROJECT` | W&B project name | `{{WANDB_PROJECT}}` |
{{/IF WANDB_ENABLED}}

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
# Submit a job
sbatch jobs/<script_name>.sh

# Check job status
squeue -u $USER

# View output
tail -f results/<job_output>.log
```

## Project Structure

```
├── src/{{PACKAGE_NAME}}/    # Main package
│   ├── config/              # Configuration dataclasses
│   ├── data/                # Data loading and transforms
│   ├── models/              # Model definitions
│   ├── eval/                # Evaluation metrics
│   └── utils/               # Utilities
├── scripts/                 # CLI entry points
├── jobs/                    # SLURM job scripts
├── tests/                   # Test suite
├── data/                    # Local data files
├── results/                 # Experiment outputs
└── docs/                    # Documentation
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
