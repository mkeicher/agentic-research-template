# Milestones — [Project Name]

Detailed checklist for each milestone. Update status symbols as work progresses:
- ⬜ Not started
- 🔄 In progress
- ✅ Complete

---

## M0: Project Setup & Alignment ✅

- ✅ Repository structure created
- ✅ Dependencies configured in `pyproject.toml`
- ✅ `CLAUDE.md` initialized with project context
- ⬜ Cluster access verified (data paths, GPU allocation)
- ⬜ First `uv sync` on cluster
- ⬜ Baseline model can be loaded

## M1: Evaluation Pipeline ⬜

- ⬜ Define evaluation metrics (primary: [your metric])
- ⬜ Implement metric computation in `src/[package]/eval/`
- ⬜ Create evaluation script (`scripts/eval.py`)
- ⬜ Benchmark baseline model(s)
- ⬜ Evaluation results in `docs/experiment_results.md`
- ⬜ Tests for all metric functions

## M2: Initial Training & Ablations ⬜

- ⬜ Data loading pipeline implemented
- ⬜ Training script (`scripts/train.py`)
- ⬜ First training run completed
- ⬜ Ablation study defined
- ⬜ All ablation runs completed
- ⬜ Results documented in `docs/experiment_results.md`

## M3: Method Improvement ⬜

- ⬜ Core method designed (see `docs/research_strategy.md`)
- ⬜ Implementation complete
- ⬜ Comparison against baselines
- ⬜ Council review if results are surprising

## M4: Refinement & Analysis ⬜

- ⬜ Error analysis on failure cases
- ⬜ Targeted improvements based on error analysis
- ⬜ Final ablation sweep
- ⬜ Statistical significance tests

## M5: Paper & Validation ⬜

- ⬜ All result tables populated (`results/results_scaffold.md`)
- ⬜ Paper draft written
- ⬜ Figures generated
- ⬜ Submission
