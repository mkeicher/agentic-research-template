# Council Report Template

Use this format for AI council review reports in `docs/research_strategy/report_to_council/`.

The "AI Council" pattern uses multiple Claude sessions (or models) as independent reviewers of a research decision. Each reviewer analyzes the evidence independently, then findings are synthesized.

```markdown
# Council Report: [Topic] — [Key Finding]

**Date:** YYYY-MM-DD
**Author:** [Name] (via Claude)
**Status:** [Empirical evaluation complete / Analysis pending / Actionable]

---

## 1. Executive Summary

[2-3 sentences: what question was asked, what the evidence says, what the recommendation is.]

---

## 2. Background & Hypothesis

### The Question
[What research question or decision prompted this review?]

### Prior Evidence
[What was known before this analysis? Include metrics, tables, references.]

### Hypothesis
[What did we expect to find?]

---

## 3. Evidence

### Experiment Results
| Condition | Metric A | Metric B | Notes |
|-----------|----------|----------|-------|
| Baseline  | X.XX     | Y.YY     |       |
| Method 1  | X.XX     | Y.YY     |       |
| Method 2  | X.XX     | Y.YY     |       |

### Key Observations
1. [Observation with supporting data]
2. [Observation with supporting data]
3. [Observation with supporting data]

---

## 4. Analysis

### What Worked
- [Finding with explanation]

### What Didn't Work
- [Finding with explanation]

### Surprises
- [Unexpected result and possible explanation]

---

## 5. Recommendations

### Immediate Actions
1. [Action item]
2. [Action item]

### Future Investigation
- [What should be explored next]

### What to Abandon
- [Approaches that the evidence suggests should be dropped]

---

## 6. Decision Required

[Clear statement of the decision the user needs to make, with the recommended option highlighted.]

Options:
- **A (Recommended):** [Description]
- **B:** [Description]
- **C:** [Description]
```
