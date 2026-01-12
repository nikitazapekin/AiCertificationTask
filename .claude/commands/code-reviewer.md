# Code Reviewer (Standalone)

Run the code-reviewer skill to review code for quality and issues.

**Important:** This command runs the skill in isolation WITHOUT automatically triggering next steps.

## Input
$ARGUMENTS

## Instructions

Use the `code-reviewer` skill to review:
1. Architecture compliance (layer placement, dependencies)
2. Code quality (naming, DRY, YAGNI, error handling)
3. TypeScript best practices (no `any`, explicit types)
4. Security (input validation, no secrets, SQL injection)
5. Performance (N+1 queries, indexing, async)
6. Testing (presence, edge cases, readability)

Output format:
```markdown
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
```

**STOP after completing review.** Do not automatically proceed to fixing issues or other skills.
