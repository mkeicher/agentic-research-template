#!/usr/bin/env bash
# =============================================================================
# SLURM Job Preamble — copy this block into every new job script in jobs/
#
# TEMPLATE NOTE: Customize the env var names, default paths, and optional
# sections (judge API, degraded node) for your specific project and cluster.
#
# SLURM compute nodes do NOT reliably inherit login-node environment variables.
# `source ~/.bashrc` is best-effort but may silently fail (non-interactive shell).
# All env vars that scripts depend on MUST have explicit fallback defaults.
# =============================================================================

set -euo pipefail

# Source user profile for env vars (best-effort).
source ~/.bashrc 2>/dev/null || true
export DATA_ROOT="${DATA_ROOT:-/path/to/data}"
# [CUSTOMIZE: Add your project's env vars with hardcoded defaults here]

# [CONDITIONAL: Include if using an LLM judge API]
# Judge API: use proxy URL file if running, else fall back to direct server.
# _PROXY_URL_FILE="${SLURM_SUBMIT_DIR:-$(pwd)}/results/vllm_proxy_url.txt"
# if [ -z "${JUDGE_API_BASE:-}" ] && [ -f "${_PROXY_URL_FILE}" ]; then
#     export JUDGE_API_BASE="$(cat "${_PROXY_URL_FILE}")"
# else
#     export JUDGE_API_BASE="${JUDGE_API_BASE:-http://localhost:8267/v1}"
# fi
# export JUDGE_API_KEY="${JUDGE_API_KEY:-EMPTY}"
# export JUDGE_MODEL="${JUDGE_MODEL:-qwen3-32b-awq}"

# === Environment setup ===
echo "=== Job started at $(date) ==="
echo "Git commit: $(git rev-parse HEAD 2>/dev/null || echo 'not a git repo')"
echo "Node: $(hostname)"
echo "GPU: $(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null || echo 'N/A')"
echo "DATA_ROOT: ${DATA_ROOT}"
echo "CUDA_VISIBLE_DEVICES: ${CUDA_VISIBLE_DEVICES:-not set}"
echo ""

# Activate UV environment.
cd "${SLURM_SUBMIT_DIR:-.}"
source .venv/bin/activate 2>/dev/null || eval "$(uv venv --activate)"

# Fix SSL cert verification for UV-managed Python (needed for model downloads).
export SSL_CERT_FILE="$(python -c 'import certifi; print(certifi.where())' 2>/dev/null || echo '')"

# [CONDITIONAL: Include if you have a degraded node with local scratch]
# === Degraded node scratch safety ===
# SCRATCH_DATA="/scratch/user/data"
# if [[ "$(hostname)" == degraded-node* ]]; then
#     echo "=== degraded node detected: using local scratch ==="
#     if [ ! -d "${SCRATCH_DATA}" ]; then
#         echo "ERROR: Scratch not set up. Set up scratch data first, then resubmit."
#         exit 1
#     fi
#     export DATA_ROOT="${SCRATCH_DATA}"
#     echo "DATA_ROOT redirected to: ${DATA_ROOT}"
# fi
