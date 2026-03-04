# agentic-research-template

A project template for running applied research with AI coding agents (Claude Code, Gemini, Codex) on SLURM/HPC clusters. Distilled from 80+ sessions of battle-tested patterns on a real research project.

**This is a methodology, not just scaffolding.** The template encodes workflows for session-based development, multi-agent coordination, AI council reviews, quality gates, structured experiment tracking, and mandatory documentation that actually stays current.

## Philosophy

1. **Session-based work.** Research happens in discrete sessions. Each session has a wrap-up protocol that updates docs, commits changes, and leaves a clean handover for the next session (or agent).

2. **Self-maintaining documentation.** `CLAUDE.md` is the single source of truth for agent context. The wrap-up protocol ensures it never goes stale. `CHANGELOG.md` is the institutional memory.

3. **AI Council for strategic decisions.** When results are surprising or approaches need to change, the council pattern uses multiple independent AI reviewers to prevent tunnel vision and create auditable decision trails.

4. **Quality gates over YOLO.** Pipelines have explicit go/no-go gates with measurable thresholds. SOPs document failure modes and remediation steps. HALT conditions prevent throwing good GPU-hours after bad.

5. **Results scaffold first.** Before writing code, define what paper tables you need to fill. Every script traces back to a result. If it doesn't serve a table, question whether it's needed now.

## Quick Start

The template is initialized by an AI agent — not a Python script. The agent reads the template files as examples, asks about your project, and writes tailored files.

### 1. Clone the template

```bash
git clone https://github.com/mkeicher/agentic-research-template.git /tmp/agentic-research-template
```

### 2. Create your project

```bash
mkdir -p ~/dev/my-project && cd ~/dev/my-project && git init
```

### 3. Start a Claude Code session and paste the setup prompt

Open Claude Code (or your preferred AI coding agent) in the new directory and paste the prompt from [`SETUP.md`](SETUP.md). The agent will:

1. Read all template files to understand the structure and conventions
2. Ask you ~8-10 questions about your project (name, domain, cluster setup, tools, etc.)
3. Write all project files with content tailored to your specific project
4. Commit the scaffold

**Why an agent instead of a script?** An agent can adapt intelligently — omitting irrelevant sections, rewriting for your domain, adding project-specific content the template doesn't anticipate. A mechanical `{{PLACEHOLDER}}` system can only do find-and-replace.

### 4. Post-setup checklist

1. Review `CLAUDE.md` — the most important file. Adjust as needed.
2. Copy `global_claude_md/CLAUDE.md` → `~/.claude/CLAUDE.md` (recommended for shared clusters)
3. Review `jobs/PREAMBLE.sh` for your cluster's specifics
4. Fill in `docs/research_strategy.md`
5. Sketch paper tables in `results/results_scaffold.md`
6. Start working!

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

See `docs/research_strategy/README.md` in the generated project, and `examples/council_report_example.md` for a real example.

### Quality Gates & SOPs

Pipelines have explicit checkpoints:

```markdown
**Gate 1: Data Quality**
- Metric: Coverage > 0.50, Agreement > 0.90
- Script: `scripts/check_quality.py`
- PASS → proceed to training
- FAIL → investigate and iterate
```

HALT conditions prevent runaway iteration. See `examples/sop_example.md`.

### Session Wrap-Up Protocol

At the end of every session, the agent must:

1. Run tests and linting (fix failures)
2. Commit pending work
3. Append to `CHANGELOG.md`
4. Update `CLAUDE.md` current task, agent board, roadmap
5. Update `docs/milestones.md`
6. Push to origin
7. Print session summary

### Experiment Waves

Experiments are organized in numbered waves:

- **Wave 0:** Baseline evaluation
- **Wave 1:** Initial ablations
- **Wave 2+:** Iterative improvements

Each wave has a hypothesis, go/no-go gate, and maps to entries in `results/results_scaffold.md`.

## Repository Structure

```
agentic-research-template/
├── README.md                     # This file
├── SETUP.md                      # Prompt for AI agent to initialize a new project
├── LICENSE                       # MIT
│
├── template/                     # Reference files the agent reads during setup
│   ├── CLAUDE.md                 # Agent instructions — the core template
│   ├── README.md                 # Project README reference
│   ├── CHANGELOG.md              # Pre-populated with Session 0
│   ├── pyproject.toml            # Python project config reference
│   ├── .gitignore
│   ├── global_claude_md/         # Reference for ~/.claude/CLAUDE.md
│   ├── global_memory/            # Reference for agent memory
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
    ├── council_report_example.md # AI council review with evidence tables
    ├── sop_example.md            # Pipeline SOP with quality gates
    └── decisions_log_example.md  # Chronological decision log
```

## Customization

### Using with Other AI Agents

The `SETUP.md` prompt is written for Claude Code but works with any capable coding agent (Gemini, Codex, Cursor, etc.). The template files in `template/` are plain markdown and Python — any agent that can read files and write new ones can do the initialization.

### Adapting for Non-SLURM Environments

The template assumes SLURM. For other environments:
- Replace `jobs/PREAMBLE.sh` with your job scheduler's equivalent
- Adjust "Login Node Rules" in CLAUDE.md
- Keep the handover protocol — it works for any remote execution pattern

### Scaling Agent Count

The Agent Board starts with 3 rows. Add rows as needed for larger teams. Consider splitting `CLAUDE.md` if it exceeds ~500 lines.

## What This Template Does NOT Do

- **No ML code.** This is infrastructure for organizing research, not a training framework.
- **No cloud abstractions.** SLURM-focused. Adapting to cloud is left to the user.
- **No CI/CD.** Research repos rarely need it. Add if your project does.
- **No data versioning.** Use `docs/data_artifacts.md` for manual tracking. Add DVC/etc. if needed.

## Credits

Distilled from the MerlinChat research project (80+ Claude Code sessions, 1200+ tests, 6 concurrent agents). The patterns emerged from real failures: stale docs, conflicting agents, wasted GPU-hours from unclear handovers, and strategic dead ends caught too late.

## License

MIT
