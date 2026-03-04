# .context/ — Read-Only Reference

This directory contains reference materials for Claude Code sessions:

- Paper summaries and analysis
- External documentation (cluster, framework, API)
- Reference implementations from other projects
- Dataset documentation and schema descriptions

## Rules

- **Read-only.** Claude Code reads these for context but never modifies them.
- **Not imported.** Nothing in `.context/` is imported by project code.
- **Not tested.** Reference code here is for understanding, not execution.
- **Add liberally.** Any document that helps an AI agent understand the project context belongs here.

## What to Put Here

- Summaries of papers your project builds on
- Cluster documentation (hardware, SLURM config, available software)
- API documentation for external services
- Dataset READMEs and schema descriptions
- Code from v1 or predecessor projects (for reference, not reuse)
