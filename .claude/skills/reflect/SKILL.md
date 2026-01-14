---
name: reflect
description: Capture lessons learned and improve processes after completing features. Use after finishing-branch, completing documentation, or when explicitly asked to reflect on work done. Triggers on "reflect", "lessons learned", "retrospective", "what went well", "improve process".
---

# Reflect

## Overview

Capture lessons learned, update documentation with discovered patterns, and improve processes for future work.

**Core principle:** Every completed feature teaches something. Capture it or lose it.

**Announce at start:** "I'm using the reflect skill to capture lessons learned from this work."

## When to Use

- After completing a feature (finishing-branch done)
- After documentation generation
- When explicitly asked to reflect
- After a difficult debugging session
- When discovering a new pattern worth documenting

## The Reflection Process

### Step 1: Gather Context

**Identify what was built:**
```
- Feature/fix name:
- Files changed:
- Patterns used:
- Challenges encountered:
```

### Step 2: Capture Lessons

**Answer these questions:**

```markdown
## What Went Well
- [List successes and smooth areas]

## What Was Challenging
- [List difficulties and friction points]

## What Would I Do Differently
- [List improvements for next time]

## New Patterns Discovered
- [List any new patterns or approaches found]
```

### Step 3: Update Documentation

**If new pattern discovered:**

1. Add to CLAUDE.md if project-wide pattern:
```markdown
## [Pattern Name]

**When to use:** [Conditions]

**Structure:**
\`\`\`typescript
// Template code
\`\`\`

**Example:**
\`\`\`typescript
// Real implementation from this feature
\`\`\`
```

2. Update relevant skill if skill-specific pattern

### Step 4: Process Improvements

**Consider updates to:**

| Area | What to Update |
|------|---------------|
| Skills | New skill or skill enhancement |
| CLAUDE.md | New project patterns |
| Checklists | Missing verification steps |
| Templates | Improved boilerplate |

## Quick Reflection Template

```markdown
# Reflection: [Feature Name]

**Date:** [Date]
**Duration:** [How long it took]

## Summary
[1-2 sentences about what was accomplished]

## Wins
- [Success 1]
- [Success 2]

## Challenges
- [Challenge 1] → [How resolved]
- [Challenge 2] → [How resolved]

## Learnings
- [Key learning 1]
- [Key learning 2]

## Process Updates
- [ ] Update CLAUDE.md with [pattern]
- [ ] Update [skill] with [improvement]
- [ ] Add to [checklist]

## For Next Time
- [Recommendation for future similar work]
```

## Common Reflection Categories

### Code Patterns
- New architectural patterns
- Better abstractions discovered
- Performance optimizations found

### Process Improvements
- Steps that should be automated
- Checks that were missing
- Order of operations that worked better

### Tool Usage
- Commands that were helpful
- Tool combinations that worked well
- New tools discovered

### Knowledge Gaps
- Documentation that was missing
- Concepts that needed research
- Areas requiring deeper understanding

## Red Flags - STOP and Reflect

These indicate a reflection is overdue:
- Same type of bug happening repeatedly
- Frequently looking up the same information
- Feeling like "we've done this before"
- Debugging sessions taking too long
- Repeated back-and-forth with similar issues

## Output Locations

| Output | Location |
|--------|----------|
| Project patterns | `CLAUDE.md` |
| Architecture decisions | `docs/adrs/ADR-NNNN.md` |
| Process improvements | Relevant skill file |
| Session notes | `docs/reflections/` (optional) |

---

## Next Steps

After reflection is complete, the workflow is DONE.

**This is the end of the standard flow.**

**Optional follow-ups:**
- `/requirements-analyst [new feature]` - Start a new feature from requirements.
- `/brainstorm [new idea]` - Explore a new idea for the project.
- `/skill-creator [improvement]` - Create or update a skill based on learnings.
