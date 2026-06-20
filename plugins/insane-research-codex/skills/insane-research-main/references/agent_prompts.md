# Agent Prompt Templates

## General Research Agent
```
Research [specific aspect] of [main topic].

Focus on finding:
- Recent information (prioritize last 2 years)
- Authoritative sources
- Specific data/statistics
- Multiple perspectives

For EVERY factual claim, provide:
- Direct quote or data point
- Source URL
- Author/organization
- Publication date
- Confidence rating (High/Medium/Low)

Return structured findings with all source URLs.
```

## Technical Research Agent
```
Find technical/academic information about [topic].

Look for:
- Peer-reviewed papers
- Technical specifications
- Methodologies and frameworks
- Scientific evidence

Include proper academic citations with DOI/URLs.
```

## Verification Agent
```
Verify the following claims about [topic]:
[List key claims to verify]

Use multiple search queries to find:
- Supporting evidence
- Contradicting information
- Original sources

Rate confidence: High/Medium/Low for each claim.
Explain any contradictions found.
Never confirm without sources.
```

## Agent Deployment Pattern

Use Codex sub-agents only when the user explicitly asks for parallel research.

- `explorer` — Assign one bounded subtopic, source type, or claim-verification set.
- `default` — Use for synthesis assistance when the work is mostly writing or reasoning.
- Lead agent — Keep source triage, citation standards, and final synthesis in the main thread.

Each delegated prompt should include:

- exact research question
- required source quality
- output shape
- citation requirements
- instruction to avoid making unsupported claims

---

## Graph of Thoughts Integration

The research process uses Graph of Thoughts (GoT) for complex reasoning:

1. **Modeling Research as Graph Operations**: Each research step becomes a node
2. **Parallel Processing**: Multiple research paths explored simultaneously
3. **Scoring & Optimization**: Information quality scored and optimized
4. **Backtracking**: Poor research paths abandoned for better alternatives

### GoT Operations:
- **Generate**: Create search queries and hypotheses
- **Score**: Evaluate information quality and relevance
- **GroundTruth**: Verify facts against authoritative sources
- **Aggregate**: Combine findings from multiple sources
- **Improve**: Refine research questions based on findings
