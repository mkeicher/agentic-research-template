# Cluster Claude Session — Quick Start Prompt

Copy-paste this into a new Claude Code session when you need to run GPU workloads on the cluster. It provides context so the agent can pick up where you left off.

---

```
I need to run GPU jobs on the cluster for {{PROJECT_NAME}}.

Current state:
- Branch: `main`
- See CLAUDE.md for full project context
- See jobs/README_RUN.md for the current handover

Tasks:
1. Check `jobs/README_RUN.md` for pending runs
2. Verify prerequisites (uv sync, data paths)
3. Submit jobs via `sbatch jobs/<script>.sh`
4. Monitor with `squeue -u $USER`
5. Check outputs in `results/`

Important:
- Never run GPU work on the login node
- GPU limit: {{GPU_COUNT_PER_USER}} per user
- Use `--time=7-00:00:00` for time limits
- Check `squeue` before submitting to stay within GPU cap
```
