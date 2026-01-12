---
name: using-skills
description: Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions
---

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance a skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill.

IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. This is not optional. You cannot rationalize your way out of this.
</EXTREMELY-IMPORTANT>

## How to Access Skills

**In Claude Code:** Use the `Skill` tool. When you invoke a skill, its content is loaded and presented to you—follow it directly. Never use the Read tool on skill files.

## The Rule

**Check for skills BEFORE ANY RESPONSE.** This includes clarifying questions. Even 1% chance means invoke the Skill tool first.

```
User message received
        │
        ▼
Might any skill apply? ──────────────────┐
        │                                │
        │ yes, even 1%                   │ definitely not
        ▼                                │
Invoke Skill tool                        │
        │                                │
        ▼                                │
Announce: "Using [skill] to [purpose]"   │
        │                                │
        ▼                                │
Has checklist? ──────────────────────────┤
        │                                │
        │ yes                            │ no
        ▼                                │
Create TodoWrite todo per item           │
        │                                │
        ▼                                │
Follow skill exactly ◄───────────────────┤
        │                                │
        ▼                                ▼
Respond (including clarifications) ◄─────┘
```

## Red Flags

These thoughts mean STOP—you're rationalizing:

| Thought | Reality |
|---------|---------|
| "This is just a simple question" | Questions are tasks. Check for skills. |
| "I need more context first" | Skill check comes BEFORE clarifying questions. |
| "Let me explore the codebase first" | Skills tell you HOW to explore. Check first. |
| "I can check git/files quickly" | Files lack conversation context. Check for skills. |
| "Let me gather information first" | Skills tell you HOW to gather information. |
| "This doesn't need a formal skill" | If a skill exists, use it. |
| "I remember this skill" | Skills evolve. Read current version. |
| "This doesn't count as a task" | Action = task. Check for skills. |
| "The skill is overkill" | Simple things become complex. Use it. |
| "I'll just do this one thing first" | Check BEFORE doing anything. |
| "This feels productive" | Undisciplined action wastes time. Skills prevent this. |

## Skill Priority

When multiple skills could apply, use this order:

1. **Process skills first** (systematic-debugger, requirements-analyst) - determine HOW to approach
2. **Architecture skills second** (architect, api-designer) - guide design decisions
3. **Implementation skills third** (coder, coder-frontend) - guide execution
4. **Review skills fourth** (code-reviewer) - validate work
5. **Documentation skills last** (documentation-generator, reflect) - document and learn

## The Flow

```
Requirements Analyst → Brainstorm → Writing Plans
                                          │
    ┌─────────────────────────────────────┘
    │
    ▼
Architect → API Designer → Executing Plans
                                │
         ┌──────────────────────┼──────────────────────┐
         │                      │                      │
         ▼                      ▼                      ▼
   Using Git Worktrees    (Parallel Tasks)      (Single Branch)
         │
    ┌────┴────┐
    │         │
    ▼         ▼
Frontend   Backend
Branch     Branch
    │         │
    └────┬────┘
         │
         ▼
Documentation Generator → Reflect
```

## Skill Categories

### Orchestration Skills (Multi-Step Workflows)

| Skill | When to Use |
|-------|-------------|
| `new-feature` | Building any new feature (orchestrates entire flow) |

### Requirements & Design Skills

| Skill | When to Use |
|-------|-------------|
| `requirements-analyst` | Analyzing requirements, parsing Confluence, decomposing tasks |
| `brainstorming` | Creative work, designing features, refining ideas |
| `writing-plans` | Creating detailed implementation plans |

### Architecture Skills

| Skill | When to Use |
|-------|-------------|
| `architect` | Design decisions, technology choices, scalability |
| `api-designer` | REST API design, DTOs, Swagger documentation |

### Execution Skills

| Skill | When to Use |
|-------|-------------|
| `executing-plans` | Running implementation plans with batch execution |
| `using-git-worktrees` | Creating isolated workspaces for parallel development |

### Frontend Branch Skills

| Skill | When to Use |
|-------|-------------|
| `frontend-design` | UI/UX design, component architecture |
| `coder-frontend` | Frontend implementation, React/Vue/Angular |

### Backend Branch Skills

| Skill | When to Use |
|-------|-------------|
| `coder` | Backend feature implementation, bug fixes |

### Quality Skills

| Skill | When to Use |
|-------|-------------|
| `test-generator` | Writing tests (unit, integration, e2e) |
| `code-reviewer` | Code quality analysis |
| `systematic-debugger` | Debugging, error analysis, root cause |
| `verification-before-completion` | Verify before claiming completion |

### Finalization Skills

| Skill | When to Use |
|-------|-------------|
| `finishing-branch` | Complete development work, merge/PR |

### Documentation & Learning Skills

| Skill | When to Use |
|-------|-------------|
| `documentation-generator` | READMEs, ADRs, changelogs |
| `reflect` | Lessons learned, process improvement |
| `skill-creator` | Creating new skills |

### Integration Skills

| Skill | When to Use |
|-------|-------------|
| `atlassian-skill` | Jira, Confluence, requirement tracking |

## Skill Types

**Rigid** (systematic-debugger, verification-before-completion): Follow exactly. Don't adapt away discipline.

**Flexible** (brainstorming, architect): Adapt principles to context.

The skill itself tells you which.

## Common Task → Skill Mappings

| User Request | Primary Skill | Secondary Skills |
|--------------|---------------|------------------|
| "Add feature X" | `new-feature` | (orchestrates all) |
| "Create endpoint" | `api-designer` | coder, test-generator |
| "Add entity" | `coder` | test-generator |
| "Fix bug" | `systematic-debugger` | coder, test-generator |
| "Review code" | `code-reviewer` | - |
| "Analyze requirements" | `requirements-analyst` | architect |
| "Write tests" | `test-generator` | - |
| "Design system" | `architect` | api-designer |
| "Build frontend" | `frontend-design` | coder-frontend |
| "Debug issue" | `systematic-debugger` | (standalone) |

## Verification

Before completing ANY task, verify:

- [ ] Checked for applicable skills BEFORE starting
- [ ] Invoked all relevant skills
- [ ] Followed skill instructions exactly
- [ ] Used TodoWrite for multi-step tasks
- [ ] Completed all checklist items from skills
- [ ] Documented any NEW patterns in CLAUDE.md (self-improving system)
