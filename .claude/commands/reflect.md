# Reflect (Standalone)

Run reflection via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `reflect`
- **description:** `Capture lessons learned`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Capture lessons learned and improve processes.

PROCESS:
1. Gather context (feature, files changed, patterns used)
2. Capture lessons (what went well, challenges, improvements)
3. Update documentation if new patterns discovered
4. Consider process improvements

REFLECTION TEMPLATE:
# Reflection: [Feature Name]

**Date:** [Date]

## Summary
[What was accomplished]

## Wins
- [Success 1]

## Challenges
- [Challenge 1] → [How resolved]

## Learnings
- [Key learning]

## Process Updates
- [ ] Update CLAUDE.md with [pattern]
- [ ] Update [skill] with [improvement]

## For Next Time
- [Recommendation]

OUTPUT LOCATIONS:
- CLAUDE.md - Project patterns
- docs/adrs/ - Architecture decisions
- Relevant skill file - Process improvements

Complete reflection and update relevant documentation.
```

**After sub-agent completes:** Report the learnings summary to the user.
