# Implementation Plan — {{PROJECT_NAME}}

## Overview

TODO — Define the phased implementation plan for this project. Each phase should have:
- Clear objectives
- Go/no-go gates
- Expected deliverables
- Dependencies on previous phases

## Phase 1: Evaluation Pipeline

**Objective:** Establish reliable evaluation before any training.

**Deliverables:**
- [ ] Metric implementation with tests
- [ ] Baseline benchmark results
- [ ] Evaluation script with CLI

**Gate:** Baseline metrics are reproducible and match published numbers (if applicable).

## Phase 2: Training Infrastructure

**Objective:** End-to-end training pipeline.

**Deliverables:**
- [ ] Data loading with proper splits
- [ ] Training script with SLURM job
- [ ] First successful training run

**Gate:** Training loss decreases; eval metrics are reasonable.

## Phase 3: Core Method

**Objective:** Implement and validate the proposed method.

**Deliverables:**
- [ ] Method implementation
- [ ] Ablation study
- [ ] Comparison with baselines

**Gate:** Method meets or exceeds baseline on {{PRIMARY_METRIC}}.

## Phase 4: Refinement

**Objective:** Improve robustness and analyze failure modes.

## Phase 5: Paper

**Objective:** Write up results and submit.
