# SOP: Attribute Schema Refinement Pipeline

**Version:** 2.2
**Created:** 2026-02-27
**Owner:** Agent B

## Purpose

Iteratively build and validate a structured attribute schema from unstructured text using LLM extraction, quality gates, and human-in-the-loop review.

## Prerequisites

- [ ] Seed schema exists (`data/schemas/seed_schema.json`)
- [ ] LLM judge API running (check `results/api_url.txt`)
- [ ] Meta-dev split available (100 stratified studies for fast iteration)

## Pipeline Stages

### Stage 1: Schema Assembly
**Input:** Raw ontology extraction outputs
**Output:** Unified seed schema with core + extended entries
**Script:** `scripts/assemble_schema.py`
**Job:** CPU-only (login node OK)

Steps:
1. Parse ontology extraction outputs
2. Deduplicate entries (fuzzy matching at 0.85 threshold)
3. Apply anti-presence blocklist (strip presence-type attributes)
4. Write `data/schemas/schema_v{N}.json`

### Stage 2: Delta Extraction (meta-dev)
**Input:** Schema v{N} + 100 meta-dev studies
**Output:** Proposed additions (new findings, new attributes, new targets)
**Script:** `scripts/extract_attributes.py --stage delta`
**Job:** `jobs/extract_delta.sh` (1 GPU, ~2h)

Steps:
1. For each study: extract attributes using current schema
2. Identify gaps: findings/attributes/targets not in schema
3. Aggregate additions with frequency counts
4. Write `results/extraction/additions.jsonl`

**Gate 1: Consolidation Quality**
- Metric: Duplicate cluster count, bloated targets, presence leakage
- Threshold: Zero duplicate clusters after dedup, zero presence attributes
- Script: `scripts/check_consolidation.py`
- **PASS →** proceed to Stage 3
- **FAIL →** fix dedup mapping, re-run consolidation, re-check

### Stage 3: Full Extraction (15K training)
**Input:** Schema v{N} (post-Gate 1) + full training set
**Output:** Extracted attributes for all training studies
**Script:** `scripts/extract_attributes.py --stage strict`
**Job:** `jobs/extract_full.sh` (1 GPU, ~24h)

Steps:
1. Extract using strict mode (no new findings/attributes allowed)
2. Checkpoint every 100 studies
3. Write `results/extraction/full_extraction.jsonl`

**Gate 2: Schema Validation**
- Metrics: Coverage (>0.50), Agreement (>0.90), Attribute Yield (>0.30)
- Script: `scripts/validate_schema.py`
- **PASS →** schema is production-ready
- **FAIL with coverage <0.50 →** iterate (back to Stage 2)
- **FAIL with agreement <0.90 →** investigate prompt quality

## HALT Conditions

Stop the pipeline entirely if:
1. Three consecutive iterations show no convergence (additions stay >5 per finding at freq ≥3)
2. Agreement drops below 0.80 (fundamental prompt/schema mismatch)
3. Coverage plateaus below 0.40 after two full iterations

## Postmortem Checklist

If the pipeline fails at any gate:
- [ ] Document which gate failed and the metric value
- [ ] Identify root cause (data issue, prompt issue, threshold too strict)
- [ ] Decide: adjust threshold, modify pipeline, or abandon approach
- [ ] Record decision in `docs/decisions_log.md`

## Versioning

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-02-27 | Initial SOP with Gate 1 + Gate 2 |
| 2.0 | 2026-02-28 | Added anti-presence blocklist, dedup mapping |
| 2.2 | 2026-03-01 | Curated dedup (fuzzy 0.90), 55 finding aliases, HALT conditions |
