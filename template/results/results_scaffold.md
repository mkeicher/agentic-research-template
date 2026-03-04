# Results Scaffold — {{PROJECT_NAME}}

Maps paper tables/figures to code outputs. **Every piece of code should trace back to an entry here.**

## Table 1: Baseline Comparison

| Method | {{PRIMARY_METRIC}} | Notes |
|--------|-----|-------|
| *Baseline 1* | — | `results/baseline_1/` |
| *Baseline 2* | — | `results/baseline_2/` |
| *Ours* | — | `results/ours/` |

**Populated by:** Wave 0 (baseline eval) + Wave 2+ (training)
**Script:** `scripts/eval.py` (TODO)

## Table 2: Ablation Study

| Ablation | {{PRIMARY_METRIC}} | Delta | Notes |
|----------|-----|-------|-------|
| *Full method* | — | — | |
| *- Component A* | — | — | |
| *- Component B* | — | — | |

**Populated by:** Wave 1 (ablations)
**Script:** `scripts/eval.py` (TODO)

## Figure 1: Training Curves

**Source:** W&B export
**Script:** TODO

---

*Add more tables/figures as the paper takes shape. Each entry should specify which experiment wave populates it and which script generates the data.*
