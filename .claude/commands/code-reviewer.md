# Code Reviewer (Standalone)

Run code review via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `code-reviewer`
- **description:** `Review code quality`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Review code for quality, standards compliance, and issues.

REVIEW AREAS:
1. Architecture compliance (layer placement, dependencies)
2. Code quality (naming, DRY, YAGNI, error handling)
3. TypeScript best practices (no `any`, explicit types)
4. Security (input validation, no secrets, SQL injection)
5. Performance (N+1 queries, indexing, async)
6. Testing (presence, edge cases, readability)

OUTPUT FORMAT:
## Summary
[Overall assessment]

## Issues Found

### Critical (Must Fix)
- [ ] [Issue] - [File:Line]

### Major (Should Fix)
- [ ] [Issue] - [File:Line]

### Minor (Consider)
- [ ] [Issue] - [File:Line]

### Positive Notes
- [What was done well]

STOP after completing review. Do not proceed to fixing issues or other skills.
```

**After sub-agent completes:** Report the review summary to the user.
