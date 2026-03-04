# Standard Operating Procedure (SOP) Template

Use this format for pipelines with quality gates and failure modes.

```markdown
# SOP: [Pipeline Name]

**Version:** 1.0
**Created:** YYYY-MM-DD
**Owner:** [Agent letter or name]

## Purpose

[One sentence: what this pipeline does and why it exists.]

## Prerequisites

- [ ] [Prerequisite 1]
- [ ] [Prerequisite 2]

## Pipeline Stages

### Stage 1: [Name]
**Input:** [What goes in]
**Output:** [What comes out]
**Script:** `scripts/[name].py`
**Job:** `jobs/[name].sh`

Steps:
1. [Step]
2. [Step]

**Gate 1: [Name]**
- Metric: [What is measured]
- Threshold: [Pass condition, e.g., "> 0.80"]
- Script: `scripts/check_[name].py`
- **PASS →** proceed to Stage 2
- **FAIL →** [specific remediation steps]

### Stage 2: [Name]
**Input:** Stage 1 output
**Output:** [What comes out]

Steps:
1. [Step]
2. [Step]

**Gate 2: [Name]**
- Metric: [What is measured]
- Threshold: [Pass condition]
- **PASS →** proceed to Stage 3
- **FAIL →** [specific remediation steps]

## HALT Conditions

Stop the pipeline entirely if:
1. [Condition that means the approach is fundamentally flawed]
2. [Condition that means data quality is insufficient]
3. [Cost/time threshold exceeded]

## Postmortem Checklist

If the pipeline fails at any gate:
- [ ] Document which gate failed and the metric value
- [ ] Identify root cause (data issue, prompt issue, threshold too strict)
- [ ] Decide: adjust threshold, modify pipeline, or abandon approach
- [ ] Record decision in `docs/decisions_log.md`

## Versioning

| Version | Date | Change |
|---------|------|--------|
| 1.0 | YYYY-MM-DD | Initial SOP |
```
