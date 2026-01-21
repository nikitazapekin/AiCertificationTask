# Skill Flow Reference

This document defines the recommended order of skills. Each skill stops after completion and suggests the next step - the user decides whether to continue.

## Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                     PHASE 1: UNDERSTANDING                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   /requirements-analyst ──────────► /brainstorm                     │
│   (parse & decompose)               (refine into design)            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     PHASE 2: PLANNING                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   /writing-plans ──────► /architect ──────► /api-designer           │
│   (granular tasks)       (decisions)        (REST design)           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     PHASE 3: EXECUTION                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   /project-generator (scaffold if new project)                      │
│         │                                                           │
│         ▼                                                           │
│   /git-worktrees (create isolated workspace)                        │
│         │                                                           │
│         ├─────────────────────┬─────────────────────┐               │
│         ▼                     ▼                     │               │
│   ┌───────────────┐    ┌───────────────┐            │               │
│   │ FRONTEND      │    │ BACKEND       │            │               │
│   ├───────────────┤    ├───────────────┤            │               │
│   │ /frontend-    │    │ /coder        │            │               │
│   │   design      │    │     │         │            │               │
│   │     │         │    │     ▼         │            │               │
│   │     ▼         │    │ /code-reviewer│            │               │
│   │ /coder-       │    │     │         │            │               │
│   │   frontend    │    │     ▼         │            │               │
│   │     │         │    │ /test-        │            │               │
│   │     ▼         │    │   generator   │            │               │
│   │ /code-reviewer│    │     │         │            │               │
│   │     │         │    │     ▼         │            │               │
│   │     ▼         │    │ /debugger     │            │               │
│   │ /test-        │    │  (if needed)  │            │               │
│   │   generator   │    │     │         │            │               │
│   │     │         │    │     ▼         │            │               │
│   │     ▼         │    │ /finishing-   │            │               │
│   │ /debugger     │    │   branch      │            │               │
│   │  (if needed)  │    └───────────────┘            │               │
│   │     │         │            │                    │               │
│   │     ▼         │            │                    │               │
│   │ /finishing-   │            │                    │               │
│   │   branch      │            │                    │               │
│   └───────────────┘            │                    │               │
│         │                      │                    │               │
│         └──────────────────────┴────────────────────┘               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     PHASE 4: FINALIZATION                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   /docs-generator ──────────────────► /reflect                      │
│   (update documentation)               (lessons learned)            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Quick Reference: Next by Flow

| Current Command         | Next by Flow                             | Why                                     |
| ----------------------- | ---------------------------------------- | --------------------------------------- |
| `/requirements-analyst` | `/brainstorm`                            | Turn requirements into design           |
| `/brainstorm`           | `/writing-plans`                         | Create implementation tasks from design |
| `/writing-plans`        | `/architect`                             | Review architecture for the plan        |
| `/architect`            | `/api-designer`                          | Design APIs based on architecture       |
| `/api-designer`         | `/project-generator` or `/git-worktrees` | Scaffold if new, then create workspace  |
| `/project-generator`    | `/git-worktrees`                         | Create isolated workspace for coding    |
| `/git-worktrees`        | `/coder` or `/frontend-design`           | Start implementation                    |
| `/frontend-design`      | `/coder-frontend`                        | Implement the designed UI               |
| `/coder-frontend`       | `/code-reviewer`                         | Review the frontend code                |
| `/coder`                | `/code-reviewer`                         | Review the backend code                 |
| `/code-reviewer`        | `/test-generator`                        | Generate tests for reviewed code        |
| `/test-generator`       | `/debugger` or `/finishing-branch`       | Debug failures or finish                |
| `/debugger`             | `/test-generator`                        | Re-run tests after fix                  |
| `/finishing-branch`     | `/docs-generator`                        | Document the changes                    |
| `/docs-generator`       | `/reflect`                               | Capture lessons learned                 |
| `/reflect`              | (end)                                    | Flow complete                           |

## When to Use project-generator

Use `/project-generator` only when you need to scaffold a new project:

| Situation                                | Use project-generator?               |
| ---------------------------------------- | ------------------------------------ |
| New project (backend, frontend, or both) | Yes, before `/git-worktrees`         |
| Adding feature to existing project       | No, skip to `/git-worktrees`         |
| New module in existing project           | No, `/coder` handles module creation |

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
→ /api-designer Design REST endpoints
→ /project-generator Scaffold backend + frontend
→ /git-worktrees Create workspace
→ /coder Implement backend features
→ /frontend-design Design UI
→ /coder-frontend Implement frontend
→ /code-reviewer Review all code
→ /test-generator Generate tests
→ /finishing-branch Complete feature
```

### New Backend Only

```
/brainstorm Design user management API
→ /architect Review architecture
→ /api-designer Design endpoints
→ /project-generator Scaffold backend
→ /git-worktrees Create workspace
→ /coder Implement features
→ /test-generator Generate tests
→ /finishing-branch Complete
```

### Adding Feature to Existing Project

```
/requirements-analyst Parse new feature spec
→ /brainstorm Design the feature
→ /git-worktrees Create workspace
→ /coder Implement feature
→ /code-reviewer Review code
→ /test-generator Generate tests
→ /finishing-branch Complete
```
