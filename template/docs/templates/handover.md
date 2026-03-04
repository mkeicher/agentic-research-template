# Cluster Handover Template

Use this format for `jobs/README_RUN.md` when handing off work for cluster execution.

```markdown
# Cluster Run: [Milestone Name]
**Date:** YYYY-MM-DD
**Branch:** `main`
**Status:** Ready for cluster execution

## Summary
[One paragraph]

## Prerequisites
- [ ] `uv sync` completed on cluster
- [ ] Data root env var points to correct path
- [ ] [Any other env setup]

## Jobs to Run

### Job 1: [Name]
```bash
sbatch jobs/[script_name].sh
```
**Expected runtime:** ~Xh on Y GPU(s)
**Output:** `results/[path]`

### Job 2: [Name] (depends on Job 1)
```bash
sbatch jobs/[script_name].sh
```
**Expected runtime:** ~Xh on Y GPU(s)
**Output:** `results/[path]`

## Sanity Checks
- [ ] [Specific check 1]
- [ ] [Specific check 2]
- [ ] [Specific check 3]

## Results Scaffold
Populates: `results/results_scaffold.md` → Table [X]

## Known Limitations
- [Limitation 1]

## Next Steps After This Run
- [What to do with the results]
```
