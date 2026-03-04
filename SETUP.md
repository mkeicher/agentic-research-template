# Setup: Initialize a New Research Project

**This file is a prompt for Claude Code (or any AI coding agent).** Copy-paste the instructions below into a new Claude Code session to initialize your project.

---

## How to Use

1. Clone this template repo somewhere accessible:
   ```bash
   git clone https://github.com/mkeicher/agentic-research-template.git /tmp/agentic-research-template
   ```

2. Create your project directory:
   ```bash
   mkdir -p ~/dev/my-project && cd ~/dev/my-project && git init
   ```

3. Start a Claude Code session in your new project directory and paste the prompt below.

---

## Prompt

```
I'm initializing a new research project using the agentic-research-template.

The template is at: /tmp/agentic-research-template/

Please:

1. Read the template README.md to understand the methodology.

2. Read all files under template/ — these are reference templates showing the structure, conventions, and content patterns. DO NOT copy them literally or do mechanical placeholder substitution. Instead, use them as high-quality examples of what each file should contain, and write project-specific versions.

3. Ask me about my project. I need you to understand:
   - Project name and one-line description
   - What kind of research (ML, medical imaging, NLP, etc.)
   - Base model or framework I'm building on
   - Primary evaluation metric
   - Dataset location and structure
   - Cluster setup (SLURM node names, GPU count, any degraded nodes)
   - Whether I use W&B, an LLM judge API, or other services
   - My name and GitHub username

4. Based on my answers, create the full project structure by writing each file with content tailored to my specific project. Key files to create:
   - CLAUDE.md (the most important file — agent instructions specific to my project)
   - README.md
   - CHANGELOG.md (pre-populated with Session 0)
   - pyproject.toml
   - .gitignore
   - src/<package_name>/ with __init__.py files for config, data, models, eval, utils
   - tests/__init__.py and tests/conftest.py
   - jobs/PREAMBLE.sh (SLURM preamble for my cluster)
   - jobs/README_RUN.md
   - docs/ (milestones, research_strategy, experiment_results, decisions_log, data_artifacts, implementation_plan)
   - docs/templates/ (changelog_entry, handover, council_report, sop)
   - docs/research_strategy/README.md (AI council pattern)
   - results/results_scaffold.md
   - .context/README.md
   - data/.gitkeep, scripts/.gitkeep

5. Also generate (but don't install — just put in the project root for me to review):
   - global_claude_md/CLAUDE.md — global cluster rules for ~/.claude/CLAUDE.md
   - global_memory/MEMORY.md — initial agent memory file

6. Adapt intelligently:
   - If I don't use SLURM, skip jobs/ or adapt for my compute environment
   - If I don't use W&B, omit those sections
   - If I don't use a judge API, omit those sections
   - Rewrite research strategy sections to reflect my actual research domain
   - Adjust code style rules if I mention specific preferences

7. After creating all files, commit and print a summary of what was created.

Read the template files now and then ask me your questions.
```

---

## What the Agent Will Do

The agent reads the template files as **examples of good research project structure**, then asks you ~8-10 questions to understand your specific project. It writes all files from scratch, adapting content intelligently rather than doing mechanical find-and-replace.

This means:
- Sections irrelevant to your project are omitted entirely (not left as empty TODOs)
- Domain-specific language is used throughout (not generic placeholders)
- The agent can add project-specific sections the template doesn't anticipate
- Edge cases (no SLURM, no W&B, non-Python, etc.) are handled naturally

## Alternative: Gemini / Codex / Other Agents

The same approach works with any capable coding agent. The template files in `template/` are the reference — any agent that can read files and write new ones can do the initialization. Just adapt the prompt above for your agent's interface.
