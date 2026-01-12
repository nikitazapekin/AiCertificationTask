---
name: new-feature
description: Complete Feature Implementation Workflow - orchestrates the full feature development lifecycle from requirements to documentation. Use when implementing a new feature, adding functionality, or following structured development process. Triggers on "new feature", "implement feature", "add feature", "build feature".
---

# New Feature

## Overview

Orchestrate the complete feature implementation workflow from requirements to documentation.

**Core principle:** Follow the structured workflow. Skip nothing. Each phase has a purpose.

**Announce at start:** "I'm using the new-feature skill to orchestrate implementation of [feature name]."

## The Complete Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 1: UNDERSTANDING                       │
├─────────────────────────────────────────────────────────────────┤
│ Requirements Analyst → Brainstorm                               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 2: PLANNING                            │
├─────────────────────────────────────────────────────────────────┤
│ Writing Plans → Architect → API Designer                        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 3: EXECUTION                           │
├─────────────────────────────────────────────────────────────────┤
│ Executing Plans → Using Git Worktrees                           │
│                                                                 │
│ ┌─────────────────┐         ┌─────────────────┐                │
│ │ FRONTEND BRANCH │         │ BACKEND BRANCH  │                │
│ ├─────────────────┤         ├─────────────────┤                │
│ │ Frontend Design │         │ Coder           │                │
│ │ Coder Frontend  │         │ Code Reviewer   │                │
│ │ Code Reviewer   │         │ Test Generator  │                │
│ │ Test Generator  │         │ Systematic Debug│                │
│ │ Systematic Debug│         │ Finishing Branch│                │
│ │ Finishing Branch│         │ Verification    │                │
│ │ Verification    │         └─────────────────┘                │
│ └─────────────────┘                                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 4: FINALIZATION                        │
├─────────────────────────────────────────────────────────────────┤
│ Documentation Generator → Reflect                               │
└─────────────────────────────────────────────────────────────────┘
```

## Phase 1: Understanding

### Step 1.1: Requirements Analysis

**Use:** `requirements-analyst`

```
Input: User request, Confluence page, Jira ticket
Output: Structured requirements with acceptance criteria

Tasks:
1. Parse raw requirements
2. Decompose into actionable tasks
3. Identify acceptance criteria
4. Map to technical components
```

### Step 1.2: Brainstorming

**Use:** `brainstorming`

```
Input: Parsed requirements
Output: Design decisions, refined approach

Tasks:
1. Explore solution approaches
2. Identify trade-offs
3. Refine requirements with technical context
4. Document design decisions
```

## Phase 2: Planning

### Step 2.1: Writing Plans

**Use:** `writing-plans`

```
Input: Requirements, design
Output: Implementation plan with granular tasks

Tasks:
1. Create implementation plan
2. Break into parallel-safe tasks
3. Define success criteria per task
4. Identify dependencies
```

### Step 2.2: Architecture

**Use:** `architect`

```
Input: Implementation plan
Output: Architecture decisions

Tasks:
1. Review architecture implications
2. Make technology decisions
3. Define component boundaries
4. Document in ADR if significant
```

### Step 2.3: API Design

**Use:** `api-designer`

```
Input: Architecture decisions
Output: API specifications

Tasks:
1. Design REST endpoints
2. Create DTOs with validation
3. Add Swagger decorators
4. Generate Bruno collections
```

## Phase 3: Execution

### Step 3.1: Setup Execution

**Use:** `executing-plans`, `using-git-worktrees`

```
Tasks:
1. Create feature branch(es)
2. Set up worktrees if parallel work
3. Begin task execution
```

### Step 3.2: Frontend Branch (if applicable)

Execute in sequence:

| Skill | Purpose |
|-------|---------|
| `frontend-design` | UI/UX design |
| `coder-frontend` | Implement components |
| `code-reviewer` | Review code quality |
| `test-generator` | Create tests |
| `systematic-debugger` | Fix issues |
| `finishing-branch` | Complete branch |
| `verification-before-completion` | Verify all passing |

### Step 3.3: Backend Branch

Execute in sequence:

| Skill | Purpose |
|-------|---------|
| `coder` | Implement business logic |
| `code-reviewer` | Review code quality |
| `test-generator` | Create tests |
| `systematic-debugger` | Fix issues |
| `finishing-branch` | Complete branch |
| `verification-before-completion` | Verify all passing |

## Phase 4: Finalization

### Step 4.1: Documentation

**Use:** `documentation-generator`

```
Tasks:
1. Update/create README
2. Write ADRs if architectural decisions made
3. Update CHANGELOG
4. Add JSDoc for public APIs
5. Update CLAUDE.md with new patterns
```

### Step 4.2: Reflection

**Use:** `reflect`

```
Tasks:
1. Capture lessons learned
2. Update skills with improvements
3. Document new patterns
4. Note process improvements
```

## Quick Start Checklist

```markdown
## Feature: [Name]

### Phase 1: Understanding
- [ ] Requirements analyzed (requirements-analyst)
- [ ] Design brainstormed (brainstorming)

### Phase 2: Planning
- [ ] Plan written (writing-plans)
- [ ] Architecture reviewed (architect)
- [ ] APIs designed (api-designer)

### Phase 3: Execution
- [ ] Branches created (executing-plans)
- [ ] Frontend implemented (if applicable)
- [ ] Backend implemented
- [ ] Tests passing
- [ ] Code reviewed
- [ ] Branches finished (finishing-branch)

### Phase 4: Finalization
- [ ] Documentation updated (documentation-generator)
- [ ] Lessons captured (reflect)
```

## Skill Invocation Order

For a typical full-stack feature:

```
1.  requirements-analyst
2.  brainstorming
3.  writing-plans
4.  architect
5.  api-designer
6.  executing-plans
7.  using-git-worktrees

    [Parallel if applicable]
    Frontend:               Backend:
    8a. frontend-design     8b. coder
    9a. coder-frontend      9b. code-reviewer
    10a. code-reviewer      10b. test-generator
    11a. test-generator     11b. systematic-debugger
    12a. systematic-debugger 12b. finishing-branch
    13a. finishing-branch   13b. verification
    14a. verification

15. documentation-generator
16. reflect
```

## Phase Transitions

### Understanding → Planning
**Gate:** Clear requirements documented with acceptance criteria

### Planning → Execution
**Gate:** Plan approved, architecture decided, APIs designed

### Execution → Finalization
**Gate:** All tests pass, code reviewed, branches completed

### Finalization → Done
**Gate:** Documentation updated, reflection captured

## Red Flags - STOP

- Skipping requirements analysis
- Starting code before plan
- Missing tests
- Incomplete verification
- No documentation updates

## Integration

**Orchestrates:**
All skills in the workflow

**External integration:**
- `atlassian-skill` - Requirement tracking, status updates

**Key skills:**
- `verification-before-completion` - Enforced at every phase gate
- `systematic-debugger` - Called when issues arise
- `reflect` - Always at the end
