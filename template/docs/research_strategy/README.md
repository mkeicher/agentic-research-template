# Research Strategy & AI Council Pattern

This directory contains strategic research documents, alignment proposals, and council reports.

## The AI Council Pattern

The "AI Council" is a structured process for making high-stakes research decisions using multiple AI perspectives. It prevents tunnel vision, catches blind spots, and creates an auditable decision trail.

### When to Use

- **Research pivots:** When evidence contradicts your current approach
- **Architecture decisions:** Choosing between fundamentally different methods
- **Contradictory results:** When experiments produce unexpected or conflicting outcomes
- **Resource allocation:** Deciding which experiments to prioritize with limited GPU time
- **Go/no-go gates:** When a pipeline stage fails and you need to decide whether to iterate or abandon

### The 6-Step Process

#### Step 1: Pose the Question
Write a clear problem statement with all relevant evidence (metrics, tables, observations). Include what you expected vs. what happened.

#### Step 2: Independent Analyses
Run 2-3 separate Claude Code sessions (or different models), each analyzing the same evidence independently. Give each session the problem statement but NOT each other's analyses.

Each reviewer should produce:
- Root cause analysis
- Proposed solutions (ranked)
- Risk assessment
- Confidence level

#### Step 3: Synthesis
In a new session, provide ALL reviewer analyses. Ask for:
- Points of agreement
- Points of disagreement and which evidence supports each
- Blind spots (what no reviewer considered)
- Synthesized recommendation

#### Step 4: Alignment Strategies
If reviewers disagree, create alignment proposals — concrete, testable plans that resolve the disagreement through experimentation rather than argument.

File naming: `proposal_[topic].md` in `alignment_strategies/`

#### Step 5: Approved Proposal
User reviews proposals and approves one (possibly with modifications). The approved proposal becomes the implementation plan.

#### Step 6: Report to Council
After implementation and evaluation, write a council report documenting:
- What was predicted vs. what happened
- Which reviewer was right (and why)
- Updated understanding
- Next decision point

File naming: `[topic]_[date].md` in `report_to_council/`

### Directory Structure

```
docs/research_strategy/
├── README.md                           # This file
├── alignment_strategies/               # Proposals for resolving disagreements
│   ├── proposal_[topic_a].md
│   └── proposal_[topic_b].md
└── report_to_council/                  # Post-implementation evidence reports
    ├── [topic_a]_YYYY-MM-DD.md
    └── [topic_b]_YYYY-MM-DD.md
```

### Tips

- **Be specific with evidence.** Include actual metrics, not just "it performed poorly."
- **Don't lead the witness.** Present facts, not your preferred conclusion.
- **Time-box reviews.** Each reviewer analysis should take 15-30 minutes, not hours.
- **Track prediction accuracy.** Over time, you'll learn which patterns of reasoning lead to correct predictions.
- **The council is advisory.** The human researcher makes the final call. The council prevents groupthink, not replaces judgment.
