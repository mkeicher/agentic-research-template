#!/usr/bin/env bash
# =============================================================================
# SLURM Job Preamble — copy this block into every new job script in jobs/
#
# SLURM compute nodes do NOT reliably inherit login-node environment variables.
# `source ~/.bashrc` is best-effort but may silently fail (non-interactive shell).
# All env vars that scripts depend on MUST have explicit fallback defaults.
# =============================================================================

set -euo pipefail

# Source user profile for env vars (best-effort).
source ~/.bashrc 2>/dev/null || true
export {{DATA_ROOT_VAR}}="${{{DATA_ROOT_VAR}}:-{{DATA_ROOT_DEFAULT}}}"
{{#IF JUDGE_API_ENABLED}}
# Judge API: use proxy URL file if running, else fall back to direct server.
_PROXY_URL_FILE="${SLURM_SUBMIT_DIR:-$(pwd)}/results/vllm_proxy_url.txt"
if [ -z "${JUDGE_API_BASE:-}" ] && [ -f "${_PROXY_URL_FILE}" ]; then
    export JUDGE_API_BASE="$(cat "${_PROXY_URL_FILE}")"
else
    export JUDGE_API_BASE="${JUDGE_API_BASE:-{{JUDGE_API_DEFAULT}}}"
fi
export JUDGE_API_KEY="${JUDGE_API_KEY:-EMPTY}"
export JUDGE_MODEL="${JUDGE_MODEL:-{{JUDGE_MODEL}}}"
export JUDGE_MAX_CONCURRENT="${JUDGE_MAX_CONCURRENT:-16}"
{{/IF JUDGE_API_ENABLED}}

# === Environment setup ===
echo "=== Job started at $(date) ==="
echo "Git commit: $(git rev-parse HEAD 2>/dev/null || echo 'not a git repo')"
echo "Node: $(hostname)"
echo "GPU: $(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null || echo 'N/A')"
echo "{{DATA_ROOT_VAR}}: ${{{DATA_ROOT_VAR}}}"
echo "CUDA_VISIBLE_DEVICES: ${CUDA_VISIBLE_DEVICES:-not set}"
echo ""

# Activate UV environment.
cd "${SLURM_SUBMIT_DIR:-.}"
source .venv/bin/activate 2>/dev/null || eval "$(uv venv --activate)"

# Fix SSL cert verification for UV-managed Python (needed for model downloads).
export SSL_CERT_FILE="$(python -c 'import certifi; print(certifi.where())' 2>/dev/null || echo '')"
{{#IF DEGRADED_NODE_ENABLED}}

# === Degraded node scratch safety ===
# {{DEGRADED_NODE_NAME}} has degraded NFS I/O. Redirect to local scratch if available.
SCRATCH_DATA="{{DEGRADED_NODE_SCRATCH}}"
if [[ "$(hostname)" == {{DEGRADED_NODE_NAME}}* ]]; then
    echo "=== {{DEGRADED_NODE_NAME}} detected: using local scratch ==="
    if [ ! -d "${SCRATCH_DATA}" ]; then
        echo "ERROR: Scratch not set up on {{DEGRADED_NODE_NAME}}."
        echo "Set up scratch data first, then resubmit this job."
        exit 1
    fi
    export {{DATA_ROOT_VAR}}="${SCRATCH_DATA}"
    echo "{{DATA_ROOT_VAR}} redirected to: ${{{DATA_ROOT_VAR}}}"
fi
{{/IF DEGRADED_NODE_ENABLED}}
