# Reflect (Standalone)

Run the reflect skill to capture lessons learned and improve processes.

**Important:** This command runs the skill in isolation.

## Input
$ARGUMENTS

## Instructions

Use the `reflect` skill to:
1. Gather context (feature, files changed, patterns used)
2. Capture lessons (what went well, challenges, improvements)
3. Update documentation if new patterns discovered
4. Consider process improvements

Reflection template:
```markdown
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
```

Output locations:
- `CLAUDE.md` - Project patterns
- `docs/adrs/` - Architecture decisions
- Relevant skill file - Process improvements

**Complete reflection and update relevant documentation.**
