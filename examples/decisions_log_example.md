# Key Decisions Log — Example

This is an anonymized excerpt showing the format and level of detail expected.

---

## 2026-03-01

**Per-category analysis & label enrichment plan** — 9 low-performing categories (F1<0.27) account for 80%+ of macro F1 deficit. Root causes categorized: hierarchical overlap (subcategory ⊂ parent category), extreme rarity (<1% prevalence), subjective spectrum (borderline cases), modality limitations. Task pipeline already handles missing labels correctly (skips, not imputes). Proposed: negative mining from section templates, hierarchical label propagation, three-class formulation for RL. Ablation plan: 4 conditions (all missing→negative, section-aware negatives, hierarchy, combined). Council report: `docs/research_strategy/report_to_council/per_category_analysis.md`.

## 2026-02-28

**Explicit task type flags** — `--include-secondary-tasks` and `--no-primary-tasks` in config + CLI control which task types are generated during training. Evaluation always includes ALL task types regardless of training config, enabling cross-task generalization measurement. Replaced fragile auto-detection that silently loaded tasks based on file existence.

**Versioned label files** — 9 versioned files deployed to data root (labels v1/v2 × 3 splits, secondary v1 × 3 splits). All job scripts and Python defaults reference versioned filenames. Unversioned files removed.

**Quality gates for extraction pipeline** — Gate 1: `scripts/check_extraction.py` (login node, no API) detects name clusters (union-find, fuzzy matching at 0.82), attribute duplicates, bloated targets, leakage patterns. Gate 2: `scripts/validate_schema.py` (SLURM) computes coverage/agreement against GT labels with go/no-go thresholds.

## 2026-02-25

**Secondary task implemented** — `generate_secondary_tasks()` generates organ-level comparison branches (12 categories, ~60 templates, 50/50 polarity). Merged with primary task branches in collator. Feature bank stores secondary labels. Max sequence length bumped 768→1024 across all job scripts.

## 2026-02-23

**F1-based early stopping** — `eval_loss` is a blended metric that masks primary task F1 improvement. Switched to `--metric-for-best-model eval_macro_f1`.

**Resume-from-checkpoint support** — Added `--resume-from-checkpoint` to training script with `ignore_data_skip=True` (custom DataLoader incompatible with framework's skip sampler).
