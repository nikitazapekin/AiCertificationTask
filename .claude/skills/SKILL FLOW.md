# Skill Flow Reference

This document defines the recommended order of skills. Each skill stops after completion and suggests the next step - the user decides whether to continue.

## Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│             PHASE 1: UNDERSTANDING (Temporary task docs)            │
│                        Output: tasks/TASK-N/                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   /requirements-analyst ──────────────────► /brainstorm              │
│   (requirements-analyst-requirements.md)   (brainstorming-design.md)│
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│             PHASE 2: PLANNING (Updates living specs)                │
│                        Output: specs/ + tasks/                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   /architect ──────► /api-designer ──► /frontend-design ──► /writing│
│   (architect-        (api-designer-    (frontend-design-    -plans │
│    architecture.md)   spec.md)          spec.md)      (writing-   │
│                                                  plans-plan.md)   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     PHASE 3: EXECUTION                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   /git-worktrees (create isolated workspace)                        │
│         │                                                           │
│         ├─────────────────────┬─────────────────────┐               │
│         ▼                     ▼                     │               │
│   ┌───────────────┐    ┌───────────────┐            │               │
│   │ FRONTEND      │    │ BACKEND       │            │               │
│   ├───────────────┤    ├───────────────┤            │               │
│   │ /coder-       │    │ /coder        │            │               │
│   │   frontend    │    │     │         │            │               │
│   │     │         │    │     ▼         │            │               │
│   │     ▼         │    │ /code-reviewer│            │               │
│   │ /code-reviewer│    │     │         │            │               │
│   │     │         │    │     ▼         │            │               │
│   │     ▼         │    │ /test-        │            │               │
│   │ /test-        │    │   generator   │            │               │
│   │   generator   │    │     │         │            │               │
│   │     │         │    │     ▼         │            │               │
│   │     ▼         │    │ /debugger     │            │               │
│   │ /debugger     │    │  (if needed)  │            │               │
│   │  (if needed)  │    │     │         │            │               │
│   │     │         │    │     ▼         │            │               │
│   │     ▼         │    │ /finishing-   │            │               │
│   │ /finishing-   │    │   branch      │            │               │
│   │   branch      │    └───────────────┘            │               │
│   └───────────────┘            │                    │               │
│         │                      │                    │               │
│         └──────────────────────┴────────────────────┘               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│             PHASE 4: FINALIZATION (Updates ongoing docs)            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   /changelog-generator ──► /docs-generator ──► /finishing-branch   │
│   (CHANGELOG.md)            (README, ADRs, etc)  (merge/PR/cleanup)│
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Quick Reference: Next by Flow

| Current Command         | Next by Flow                             | Why                                     |
| ----------------------- | ---------------------------------------- | --------------------------------------- |
| `/requirements-analyst` | `/brainstorm`                            | Turn requirements into design           |
| `/brainstorm`           | `/architect`                             | Review architecture for the design      |
| `/architect`            | `/api-designer`                          | Design APIs based on architecture       |
| `/api-designer`         | `/frontend-design`                       | Design UI based on API design           |
| `/frontend-design`      | `/writing-plans`                         | Create implementation tasks from specs  |
| `/writing-plans`        | `/git-worktrees`                         | Create isolated workspace               |
| `/git-worktrees`        | `/coder` or `/coder-frontend`            | Start implementation                    |
| `/coder-frontend`       | `/code-reviewer`                         | Review the frontend code                |
| `/coder`                | `/code-reviewer`                         | Review the backend code                 |
| `/code-reviewer`        | `/test-generator`                        | Generate tests for reviewed code        |
| `/test-generator`       | `/debugger` or `/changelog-generator`    | Debug failures or document changes      |
| `/debugger`             | `/test-generator`                        | Re-run tests after fix                  |
| `/changelog-generator`  | `/finishing-branch`                      | Complete the branch                     |
| `/finishing-branch`     | `/docs-generator`                        | Document the changes                    |
| `/docs-generator`       | `/finishing-branch` or (end)             | Complete workflow                       |

## Entry Points

Choose your starting point based on your situation:

| Situation                     | Start With                  |
| ----------------------------- | --------------------------- |
| Have requirements/specs       | `/requirements-analyst`     |
| Have an idea to explore       | `/brainstorm`               |
| Have a plan ready             | `/git-worktrees` → `/coder` |
| Existing project, add feature | `/git-worktrees` → `/coder` |
| Fix a bug                     | `/debugger`                 |

## Utility Commands (Any Time)

| Command          | When to Use                             |
| ---------------- | --------------------------------------- |
| `/atlassian`     | Fetch requirements from Jira/Confluence |
| `/skill-creator` | Create a new skill                      |

## How It Works

1. **User runs a command** (e.g., `/requirements-analyst [prompt]`)
2. **Command spawns an agent** that runs in isolation
3. **Agent executes the skill** following its instructions
4. **Agent stops and outputs:**
   - Context summary (what was done)
   - Next step suggestion by flow
   - Alternative suggestions
5. **User decides** whether to run the next command

## Context Handoff

Each command's output includes a context summary. Pass this to the next command:

```
/brainstorm Based on requirements analysis: [paste context summary]
```

This keeps the main conversation clean while preserving continuity.

## Example Flows

### New Full-Stack Project

```
/brainstorm Design e-commerce app
→ /architect Review architecture decisions
→ /writing-plans Create implementation tasks
→ /git-worktrees Create workspace
→ /coder Implement backend features
→ /coder-frontend Implement frontend
→ /code-reviewer Review all code
→ /test-generator Generate tests
→ /changelog-generator Document changes
→ /finishing-branch Complete feature
```

### New Backend Only

```
/brainstorm Design user management API
→ /architect Review architecture decisions
→ /writing-plans Create implementation tasks
→ /git-worktrees Create workspace
→ /coder Implement features
→ /test-generator Generate tests
→ /changelog-generator Document changes
→ /finishing-branch Complete
```

### Adding Feature to Existing Project

```
/requirements-analyst Parse new feature spec
→ /brainstorm Design the feature
→ /architect Review architecture
→ /writing-plans Create implementation tasks
→ /git-worktrees Create workspace
→ /coder Implement feature
→ /code-reviewer Review code
→ /test-generator Generate tests
→ /changelog-generator Document changes
→ /finishing-branch Complete
```
