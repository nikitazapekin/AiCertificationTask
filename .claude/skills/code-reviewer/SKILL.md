---
name: code-reviewer
description: Review code for quality, standards compliance, security issues, and performance problems. Use when reviewing PRs, checking code quality, finding bugs, or ensuring standards compliance. Triggers on "review code", "code review", "check this", "review PR", "find issues", "code quality".
---

# Code Reviewer

## Overview

Review code for quality, standards compliance, security issues, and performance problems.

## Review Categories

### 1. Architecture Compliance

- [ ] Correct layer placement (controller, service, repository)
- [ ] Dependencies flow in correct direction
- [ ] Proper module organization
- [ ] Single responsibility principle

### 2. Code Quality

- [ ] Clear naming conventions
- [ ] No magic numbers/strings
- [ ] DRY - no duplicate code
- [ ] YAGNI - no unnecessary features
- [ ] Proper error handling
- [ ] Comments only where logic is non-obvious

### 3. TypeScript Best Practices

- [ ] No `any` types
- [ ] Interfaces for object shapes
- [ ] Explicit return types on public methods
- [ ] Proper null/undefined handling
- [ ] Correct use of `readonly`

### 4. Security

- [ ] Input validation present
- [ ] No hardcoded secrets
- [ ] Proper authorization checks
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (output encoding)

### 5. Performance

- [ ] No N+1 queries
- [ ] Proper indexing considered
- [ ] Efficient algorithms
- [ ] No memory leaks
- [ ] Async operations where appropriate

### 6. Testing

- [ ] Unit tests present
- [ ] Edge cases covered
- [ ] Tests are readable
- [ ] Mocks used appropriately

## Code Smells

| Smell | Issue | Fix |
|-------|-------|-----|
| Long method | Hard to understand | Extract to smaller methods |
| Large class | Too many responsibilities | Split into focused classes |
| Feature envy | Method uses other class data | Move method to that class |
| Data clumps | Same data groups repeated | Create a class for it |
| Primitive obsession | Using primitives for domain concepts | Create value objects |
| Switch statements | Often indicates missing polymorphism | Use strategy pattern |
| Parallel inheritance | Two hierarchies change together | Merge or compose |
| Dead code | Unused code | Delete it |
| Comments | Explaining bad code | Refactor to be self-documenting |

## Review Process

### Step 1: Understand Context

- What is the purpose of this change?
- What requirements does it fulfill?
- What existing code does it interact with?

### Step 2: Check Architecture

- Does it follow project patterns?
- Is it in the correct layer?
- Are dependencies correct?

### Step 3: Review Logic

- Does the code do what it's supposed to?
- Are edge cases handled?
- Are errors handled properly?

### Step 4: Check Tests

- Are there tests?
- Do tests cover the functionality?
- Are tests readable and maintainable?

### Step 5: Provide Feedback

Format feedback as:

```markdown
## Summary
[Overall assessment]

## Issues Found

### Critical (Must Fix)
- [ ] [Issue description] - [File:Line]

### Major (Should Fix)
- [ ] [Issue description] - [File:Line]

### Minor (Consider)
- [ ] [Issue description] - [File:Line]

### Positive Notes
- [What was done well]
```

## Severity Guidelines

| Severity | Criteria | Examples |
|----------|----------|----------|
| Critical | Security issue, data loss, crash | SQL injection, missing auth |
| Major | Bug, poor performance, maintainability | N+1 query, duplicate code |
| Minor | Style, naming, small improvements | Variable naming, comments |

## Integration

**Called by:**
- `coder` - After implementation
- `coder-frontend` - After implementation
- `executing-plans` - During review phase

**Calls:**
- None - standalone review skill
