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
│   /writing-plans ─► /architect ─► /api-designer ─► /executing-plans │
│   (granular tasks)  (decisions)   (REST design)    (batch execute)  │
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
│   │  (if needed)  │    │     │         │            │               │
│   │     │         │    │     ▼         │            │               │
│   │     ▼         │    │ /verify       │            │               │
│   │ /finishing-   │    └───────────────┘            │               │
│   │   branch      │            │                    │               │
│   │     │         │            │                    │               │
│   │     ▼         │            │                    │               │
│   │ /verify       │            │                    │               │
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

| Current Command | Next by Flow | Why |
|-----------------|--------------|-----|
| `/requirements-analyst` | `/brainstorm` | Turn requirements into design |
| `/brainstorm` | `/writing-plans` | Create implementation tasks from design |
| `/writing-plans` | `/architect` | Review architecture for the plan |
| `/architect` | `/api-designer` | Design APIs based on architecture |
| `/api-designer` | `/executing-plans` | Start implementing the designed API |
| `/executing-plans` | `/git-worktrees` | Create isolated workspace for coding |
| `/git-worktrees` | `/coder` or `/frontend-design` | Start implementation |
| `/frontend-design` | `/coder-frontend` | Implement the designed UI |
| `/coder-frontend` | `/code-reviewer` | Review the frontend code |
| `/coder` | `/code-reviewer` | Review the backend code |
| `/code-reviewer` | `/test-generator` | Generate tests for reviewed code |
| `/test-generator` | `/debugger` or `/finishing-branch` | Debug failures or finish |
| `/debugger` | `/test-generator` | Re-run tests after fix |
| `/finishing-branch` | `/verify` | Verify before merge |
| `/verify` | `/docs-generator` | Document the changes |
| `/docs-generator` | `/reflect` | Capture lessons learned |
| `/reflect` | (end) | Flow complete |

## Utility Commands (No Fixed Flow Position)

| Command | When to Use |
|---------|-------------|
| `/atlassian` | Fetch requirements from Jira/Confluence |
| `/skill-creator` | Create a new skill |
| `/project-generator` | Scaffold a new project |

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
