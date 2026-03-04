# Council Report: Task Reformulation Hypothesis — Empirical Results

**Date:** 2026-02-22
**Author:** Research Team (via Claude)
**Status:** Empirical evaluation complete. Hypothesis largely disproven.

---

## 1. Executive Summary

The council proposed that the binary VQA grounding task was "prior-dominated" and suggested three interventions: shuffled bitstring protocol, perceiver resampler, and contrastive A/B discrimination. After 15K-scale experiments, the hypothesis is largely wrong — simple binary VQA produces the strongest grounding signal when properly scaled. The bitstring task fails to generalize despite being "mathematically impossible to cheat."

---

## 2. The Council's Predictions vs. Reality

### Prediction 1: "Binary VQA is prior-dominated"

**Evidence at proposal time (1.5K training):**

| Metric | Value |
|--------|-------|
| Task F1 (real images) | 64.6% |
| Task F1 (shuffled images) | 59.7% |
| **Delta_ground** | **5.0%** |
| Gate (>15%) | **FAIL** |

This was correct for 1.5K training. The delta was small.

**Evidence after 15K training (this report):**

| Projector | F1 Real | F1 Shuffled | Delta_ground | Gate |
|-----------|---------|-------------|-------------|------|
| Linear | **63.0%** | 45.0% | **18.0%** | **PASS** |
| Cross-Attention | **59.8%** | 39.0% | **20.7%** | **PASS** |

**Verdict: DISPROVEN.** Binary VQA is NOT inherently prior-dominated. The 1.5K result was a data scaling issue, not a task design issue.

### Prediction 2: "Bitstring makes prior-based guessing impossible"

**Results (15K bitstring):**

| Metric | Value |
|--------|-------|
| Training token accuracy | 87.4% |
| Task F1 (real) | 14.0% |
| Task F1 (shuffled) | 5.3% |
| Delta_ground | 8.7% |
| Gate (>15%) | **FAIL** |

**Verdict: FAILED.** The bitstring task is learnable during training but does not generalize. The model collapses to a conservative prediction strategy.

---

## 3. Key Learnings

1. **Data scale solved the problem the council was trying to fix architecturally.** 10x more training data improved grounding delta from 5% to 18-21%.
2. **Making the task harder degraded grounding.** The bitstring's complexity prevented generalization.
3. **Implementation matters as much as design.** A post-hoc code audit revealed the contrastive smoke test had sampling bugs that limited pair diversity.

---

## 4. Recommendations

### Immediate Actions
1. Proceed with binary VQA as the grounding task
2. Scale to full training set (15K+ studies)
3. Drop bitstring approach entirely

### Future Investigation
- Test contrastive A/B at 15K scale with fixed sampling (fair comparison)
- Investigate per-finding performance gaps

### What to Abandon
- Shuffled bitstring protocol (fails to generalize)
- Architectural complexity for grounding (perceiver resampler adds cost without benefit)

---

## 5. Decision Required

**Recommended: Continue with binary VQA at 15K scale.** Evidence strongly supports this as the best grounding approach. Council's architectural interventions should be deprioritized in favor of data scaling and per-finding analysis.
