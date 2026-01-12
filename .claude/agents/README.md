# Skill-Based Agents

This directory contains agent definitions for each skill in the project. Each agent is responsible **only** for executing its specific skill and does NOT orchestrate the overall workflow.

## Architecture

### Orchestrator vs Worker Agents

There are two types of agents:

1. **Orchestrator Agent** (`new-feature-orchestrator-agent.md`)
   - Manages the overall workflow
   - Calls other agents in sequence
   - Tracks phase completion
   - Decides which agent to call next

2. **Worker Agents** (all other agents)
   - Focus on a single skill
   - Do NOT call other agents
   - Return results to the orchestrator
   - Let the orchestrator decide next steps

### Key Principle: No Flow Interference

Worker agents must NOT:
- Call other skills directly
- Proceed to the next phase
- Make workflow decisions

Worker agents SHOULD:
- Execute their specific skill
- Return structured results
- Report blockers to the orchestrator

## Skill Flow

```
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 1: UNDERSTANDING                                          │
│ Requirements Analyst → Brainstorm → Pattern Discovery           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 2: PLANNING                                               │
│ Writing Plans → Architect → API Designer → Nx Workflow          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 3: EXECUTION                                              │
│ Executing Plans → Git Worktrees                                 │
│     ├── Frontend Branch                                         │
│     │   └── Design → Code → Review → Test → Debug → Finish      │
│     └── Backend Branch                                          │
│         └── Code → CQRS → Review → Test → Debug → Finish        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 4: FINALIZATION                                           │
│ Documentation Generator → Reflect                               │
└─────────────────────────────────────────────────────────────────┘
```

## Agent Categories

### Understanding Phase
| Agent | Skill | Purpose |
|-------|-------|---------|
| `requirements-analyst-agent` | requirements-analyst | Parse and decompose requirements |
| `brainstorming-agent` | brainstorming | Design through dialogue |
| `pattern-discovery-agent` | pattern-discovery | Find existing patterns |

### Planning Phase
| Agent | Skill | Purpose |
|-------|-------|---------|
| `writing-plans-agent` | writing-plans | Create implementation plans |
| `architect-agent` | architect | Architecture decisions |
| `api-designer-agent` | api-designer | REST API design |
| `executing-plans-agent` | executing-plans | Execute plan in batches |
| `using-git-worktrees-agent` | using-git-worktrees | Create isolated workspaces |
| `nx-workflow-agent` | nx-workflow | Nx monorepo commands |

### Backend Branch
| Agent | Skill | Purpose |
|-------|-------|---------|
| `coder-agent` | coder | Backend implementation |
| `cqrs-generator-agent` | cqrs-generator | Generate CQRS code |
| `review-cqrs-agent` | review-cqrs | Review CQRS compliance |

### Frontend Branch
| Agent | Skill | Purpose |
|-------|-------|---------|
| `frontend-design-agent` | frontend-design | UI/UX design |
| `coder-frontend-agent` | coder-frontend | Frontend implementation |

### Quality (Shared)
| Agent | Skill | Purpose |
|-------|-------|---------|
| `code-reviewer-agent` | code-reviewer | Code quality review |
| `test-generator-agent` | test-generator | Generate tests |
| `systematic-debugger-agent` | systematic-debugger | Root cause analysis |
| `verification-agent` | verification-before-completion | Verify claims with evidence |
| `finishing-branch-agent` | finishing-branch | Complete branch work |

### Finalization Phase
| Agent | Skill | Purpose |
|-------|-------|---------|
| `documentation-generator-agent` | documentation-generator | Generate docs |
| `reflect-agent` | reflect | Capture lessons learned |

### Utility
| Agent | Skill | Purpose |
|-------|-------|---------|
| `atlassian-skill-agent` | atlassian-skill | Jira/Confluence integration |
| `skill-creator-agent` | skill-creator | Create new skills |
| `new-feature-orchestrator-agent` | new-feature | **Orchestrate full workflow** |

## Usage

### Spawning an Agent

Use the Task tool with a prompt that references the agent definition:

```typescript
// Example: Spawn requirements analyst agent
Task({
  description: "Analyze requirements",
  prompt: `You are the Requirements Analyst Agent.

Follow the agent definition at: .claude/agents/requirements-analyst-agent.md

Task: Analyze the following requirements...

IMPORTANT:
- ONLY perform requirements analysis
- DO NOT proceed to design or implementation
- Return structured requirements document
`,
  subagent_type: "general-purpose"
});
```

### Orchestrating a Feature

Use the new-feature-orchestrator-agent to manage the full workflow:

```typescript
Task({
  description: "Implement new feature",
  prompt: `You are the New Feature Orchestrator Agent.

Follow the agent definition at: .claude/agents/new-feature-orchestrator-agent.md

Feature: [Feature description]

Orchestrate the complete workflow, calling appropriate agents in sequence.
`,
  subagent_type: "general-purpose"
});
```

## Agent Definition Structure

Each agent file contains:

1. **Role**: Single-sentence purpose
2. **Scope**: What the agent does
3. **Constraints**: What the agent does NOT do
4. **Input**: Expected inputs
5. **Output**: Expected outputs
6. **Skill Reference**: Path to SKILL.md
7. **Flow Position**: Where in the flow this agent operates

## Flow Enforcement

The skill flow is defined in:
`/home/illia/Node-ClaudeCode-template/.claude/skills/SKILL FLOW.md`

Key rules:
1. Only the orchestrator agent manages flow
2. Worker agents return results without proceeding
3. Phase gates must be verified before progressing
4. Blockers are reported, not worked around

## Adding New Agents

1. Create new skill in `.claude/skills/`
2. Create agent definition in `.claude/agents/`
3. Follow the agent template structure
4. Add constraints to prevent flow interference
5. Update this README with the new agent
