# agentic-research-template

A project template for running applied research with Claude Code agents on SLURM/HPC clusters. Distilled from 80+ sessions of battle-tested patterns on a real research project.

**This is a methodology, not just scaffolding.** The template encodes workflows for session-based development, multi-agent coordination, AI council reviews, quality gates, structured experiment tracking, and mandatory documentation that actually stays current.

## Philosophy

1. **Session-based work.** Research happens in discrete sessions. Each session has a wrap-up protocol that updates docs, commits changes, and leaves a clean handover for the next session (or agent).

2. **Self-maintaining documentation.** `CLAUDE.md` is the single source of truth for agent context. The wrap-up protocol ensures it never goes stale. `CHANGELOG.md` is the institutional memory.

3. **AI Council for strategic decisions.** When results are surprising or approaches need to change, the council pattern uses multiple independent AI reviewers to prevent tunnel vision and create auditable decision trails.

4. **Quality gates over YOLO.** Pipelines have explicit go/no-go gates with measurable thresholds. SOPs document failure modes and remediation steps. HALT conditions prevent throwing good GPU-hours after bad.

5. **Results scaffold first.** Before writing code, define what paper tables you need to fill. Every script traces back to a result. If it doesn't serve a table, question whether it's needed now.

## Quick Start

```bash
# Clone the template
git clone https://github.com/matthias-k/agentic-research-template.git
cd agentic-research-template

# Initialize a new project (interactive)
python init.py --output ~/dev/my-research-project

# Or use a config file
python init.py --config init_config.example.json --output ~/dev/my-research-project

# Set up the new project
cd ~/dev/my-research-project
git init && git add -A && git commit -m "Initial scaffold"
uv venv --python 3.11 && uv sync
```

The initializer prompts for ~20 values (project name, data paths, cluster config, etc.) and renders all templates. No dependencies beyond Python stdlib.

### Post-Init Checklist

1. **Review and customize `CLAUDE.md`** — the core of the template. Adjust sections marked TODO.
2. **Copy global rules** — `global_claude_md/CLAUDE.md` → `~/.claude/CLAUDE.md` (optional but recommended for shared clusters).
3. **Set up SLURM preamble** — review `jobs/PREAMBLE.sh` for your cluster's specifics.
4. **Define your research strategy** — fill in `docs/research_strategy.md`.
5. **Map your paper** — sketch tables in `results/results_scaffold.md`.
6. **Start a Claude Code session** and begin working!

## Key Concepts

### CLAUDE.md — The Agent's Playbook

The generated `CLAUDE.md` contains:
- **Project Overview** — what the project is, current phase, branding
- **Current Task** — updated every session with branch, test count, blockers, next steps
- **Agent Board** — multi-agent coordination table (who is working on what)
- **Experiment Queue** — waves of experiments with hypotheses and gates
- **Project Roadmap** — milestone tracking synced with `docs/milestones.md`
- **Code Style & Philosophy** — universal principles for clean research code
- **Critical Rules** — git discipline, framework usage, anti-patterns
- **Workflow Protocol** — plan-first, incremental, lint+test before commit
- **Session Wrap-Up Protocol** — mandatory end-of-session documentation updates
- **Review Protocol** — self-review checklist + human gates
- **Cluster Handover Protocol** — SLURM standards and job script templates
- **Technical Environment** — models, metrics, GPU limits, login node rules
- **Testing Standards** — what to test, what to skip, naming conventions

### Agent Board

Track concurrent agents working on the same repo:

```markdown
| Agent | Focus Area | Status | Current Work | Claimed Files/Dirs |
|-------|-----------|--------|-------------|-------------------|
| A     | Eval      | Active | Implementing F1 metric | src/pkg/eval/ |
| B     | Training  | Active | SFT script | scripts/train.py |
```

Rules: don't modify another agent's claimed files without checking. Shared docs are append-only.

### AI Council Pattern

For research pivots, contradictory results, or architecture decisions:

1. **Pose the question** with all evidence
2. **Independent analyses** from 2-3 separate sessions
3. **Synthesis** in a new session with all analyses
4. **Alignment strategies** — testable proposals resolving disagreements
5. **Approved proposal** — user picks one
6. **Report to council** — post-implementation evidence report

See `docs/research_strategy/README.md` in the generated project.

### Quality Gates & SOPs

Pipelines have explicit checkpoints:

```markdown
**Gate 1: Data Quality**
- Metric: Coverage > 0.50, Agreement > 0.90
- Script: `scripts/check_quality.py`
- PASS → proceed to training
- FAIL → investigate and iterate
```

HALT conditions prevent runaway iteration. SOPs document the full pipeline with failure modes.

### Session Wrap-Up Protocol

At the end of every session, the agent must:

1. Run tests and linting (fix failures)
2. Commit pending work
3. Append to `CHANGELOG.md`
4. Update `CLAUDE.md` current task, agent board, roadmap
5. Update `docs/milestones.md`
6. Push to origin
7. Print session summary

This is enforced by the CLAUDE.md instructions — agents that skip steps get called out.

### Experiment Waves

Experiments are organized in numbered waves:

- **Wave 0:** Baseline evaluation
- **Wave 1:** Initial ablations
- **Wave 2+:** Iterative improvements

Each wave has a hypothesis, go/no-go gate, and maps to entries in `results/results_scaffold.md`.

## Directory Structure

```
agentic-research-template/
├── README.md                     # This file
├── LICENSE                       # MIT
├── init.py                       # Project initializer (stdlib only)
├── init_config.example.json      # Example config for non-interactive init
│
├── template/                     # Everything here gets copied + rendered
│   ├── CLAUDE.md                 # The core — agent instructions with {{PLACEHOLDERS}}
│   ├── README.md                 # Project README template
│   ├── CHANGELOG.md              # Pre-populated with Session 0
│   ├── pyproject.toml            # Python project config
│   ├── .gitignore
│   ├── global_claude_md/         # Template for ~/.claude/CLAUDE.md
│   ├── global_memory/            # Template for agent memory
│   ├── src/{{PACKAGE_NAME}}/     # Source package skeleton
│   ├── scripts/                  # CLI entry points
│   ├── tests/                    # Test infrastructure
│   ├── jobs/                     # SLURM templates (PREAMBLE.sh, handover)
│   ├── data/                     # Local data files
│   ├── results/                  # Results scaffold
│   ├── docs/                     # Full documentation framework
│   └── .context/                 # Read-only reference directory
│
└── examples/                     # Anonymized real-world examples
    ├── council_report_example.md
    ├── sop_example.md
    └── decisions_log_example.md
```

## Customization

### Adding Sections to CLAUDE.md

The template uses `{{PLACEHOLDER}}` syntax for simple substitution and `{{#IF KEY}} ... {{/IF KEY}}` for conditional blocks. To add new conditional sections:

1. Add a new key to the config (e.g., `"my_feature_enabled": true`)
2. Wrap content in `{{#IF MY_FEATURE_ENABLED}} ... {{/IF MY_FEATURE_ENABLED}}`
3. The block renders only if the key is truthy (non-empty string)

### Adapting for Non-SLURM Environments

The template assumes SLURM. For other environments:
- Replace `jobs/PREAMBLE.sh` with your job scheduler's equivalent
- Adjust "Login Node Rules" in CLAUDE.md
- Keep the handover protocol — it works for any remote execution pattern

### Scaling Agent Count

The Agent Board starts with 3 rows. For larger teams:
- Add rows as needed
- Consider splitting `CLAUDE.md` if it exceeds ~500 lines
- Use `docs/` for detailed agent-specific context

## What This Template Does NOT Do

- **No ML code.** This is infrastructure for organizing research, not a training framework.
- **No cloud abstractions.** SLURM-focused. Adapting to cloud is left to the user.
- **No CI/CD.** Research repos rarely need it. Add if your project does.
- **No data versioning.** Use `docs/data_artifacts.md` for manual tracking. Add DVC/etc. if needed.

## Credits

Distilled from the MerlinChat research project (80+ Claude Code sessions, 1200+ tests, 6 concurrent agents). The patterns emerged from real failures: stale docs, conflicting agents, wasted GPU-hours from unclear handovers, and strategic dead ends caught too late.

## License

MIT
