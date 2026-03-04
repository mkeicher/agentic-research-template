# ~/.claude/CLAUDE.md — Global Cluster Rules

This file applies to ALL projects and sessions on this shared SLURM cluster.
These rules are NON-NEGOTIABLE and override any project-level instructions that conflict.

## Filesystem Boundaries

You are operating on a shared HPC cluster. Other users' work and system stability depend on you staying in your lane.

**Write only to:**
- The current repository working directory and its subdirectories
- `$HOME/.cache/` (UV, HuggingFace, pip caches)
- `$HOME/.local/` (user-local binaries)
- SLURM output logs in the repo's `results/` or `jobs/` directories

**Read-only (never write, rename, or delete):**
- `${{DATA_ROOT_VAR}}` and any shared dataset directories under `{{SHARED_DATA_DIR}}`
- Other users' home directories
- Anything outside `$HOME/`

**Never touch:**
- System directories: `/etc/`, `/usr/`, `/opt/`, `/var/`, `/boot/`
- Shell configs: `~/.bashrc`, `~/.bash_profile`, `~/.profile`, `~/.ssh/config`
- Shared temp directories: `/tmp/` (used by all users and SLURM)
- SLURM configuration files

## File Deletion Policy (CRITICAL)

**NEVER delete files without explicit user confirmation.**

Before ANY `rm`, `rm -r`, `unlink`, `shutil.rmtree`, `os.remove`, or equivalent:
1. List the exact files/directories that would be deleted
2. Show the full paths
3. State WHY the deletion is needed
4. **Wait for user approval before executing**

This applies even with `--dangerously-skip-permissions` enabled. Treat deletion as a manual approval gate regardless of autonomy settings.

The only exception: files created during the CURRENT session that are clearly temporary build artifacts (e.g., `__pycache__`, `.ruff_cache`, `*.pyc`). These may be cleaned up without asking.

## Package & Environment Rules

- **Only use `uv`** for package management. Never `pip install`, `conda`, `apt`, `yum`, or any system package manager.
- Never install packages globally or with `--system`.
- Never modify the system Python installation.
- Adding new dependencies means editing `pyproject.toml` and running `uv sync` — nothing else.

## Process & Resource Rules

- **Never run CPU/memory-intensive work on the login node.** Use `sbatch` or `srun` for anything beyond quick debugging (<30 seconds, <2GB RAM).
- Never start long-running background processes on the login node (servers, watchers, daemons).
- Never `kill`, `pkill`, or `killall` processes you didn't start in the current session.
- Never open network ports or bind to addresses on any node.

## SLURM Rules

- Only `scancel` jobs that you submitted in the current session. Never cancel other jobs.
- **Never interfere with jobs from other projects.** Jobs submitted under this user account from a different project/repo are off-limits — do not cancel, modify, requeue, or deprioritize them. Treat them as belonging to another user.
- Never modify SLURM configuration or queue settings.
- Right-size resource requests: don't request GPUs for CPU-only work.
- **Per-user GPU limit is typically {{GPU_COUNT_PER_USER}} GPUs.** Plan job submissions to stay within this cap.
- **Set generous SLURM time limits.** Re-running a timed-out job wastes far more time than a generous limit. Default to `--time=7-00:00:00` (7 days). Jobs terminate on completion or failure anyway; the user will manually cancel stuck jobs. Never try to fit multiple independent workloads into one job — submit them as separate parallel jobs instead.
- Always include `set -euo pipefail` in job scripts so failures are caught.

## Git Rules

- Only push to remotes already configured in the repo.
- Never force-push without explicit user instruction.
- Never rewrite history on shared branches (`main`) without explicit user instruction.
- Never modify `.git/config` to add remotes, change URLs, or alter hooks.

## When Uncertain

If a command could affect other users, the system, or data outside the repo: **stop and ask.** Do not guess. Do not rationalize. The cost of asking is seconds; the cost of a mistake can be hours of someone else's lost work.
