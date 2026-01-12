# Claude Code Configuration

This directory contains skills, commands, agents, and hooks that extend Claude Code's capabilities for this project.

## Directory Structure

```
.claude/
├── agents/          # Agent definitions (workers + orchestrators)
├── commands/        # Slash commands (user-invocable shortcuts)
├── hooks/           # Shell commands triggered by events
├── skills/          # Detailed skill implementations
├── settings.json    # Team configuration (permissions, hooks)
└── settings.local.json  # Personal settings (gitignored)
```

## Quick Start

### Using Commands (Slash Commands)

Commands are shortcuts to invoke skills. Type `/` followed by the command name:

| Command | Description |
|---------|-------------|
| `/brainstorm` | Explore ideas and create designs through dialogue |
| `/new-feature` | Complete feature implementation workflow |
| `/coder` | Implement backend features |
| `/coder-frontend` | Implement frontend features |
| `/test-generator` | Generate unit, integration, and E2E tests |
| `/debugger` | Systematic debugging with root cause analysis |
| `/code-reviewer` | Code quality and best practices review |
| `/architect` | System architecture decisions |
| `/api-designer` | REST API design with Swagger |
| `/writing-plans` | Create detailed implementation plans |
| `/executing-plans` | Execute plans in batches |
| `/git-worktrees` | Create isolated workspaces |
| `/finishing-branch` | Complete branch work and merge/PR |
| `/verify` | Verify claims with evidence before completion |
| `/docs-generator` | Generate project documentation |
| `/reflect` | Capture lessons learned |
| `/project-generator` | Scaffold new NestJS project structure |
| `/requirements-analyst` | Analyze and decompose requirements |
| `/atlassian` | Jira/Confluence integration |
| `/skill-creator` | Create new skills |
| `/setup` | Development environment setup |
| `/review-cqrs` | CQRS pattern code review |
| `/frontend-design` | Create distinctive UI designs |

**Example:**
```
/brainstorm user authentication with OAuth
```

## Skills

Skills are detailed instruction sets that define how Claude performs specific tasks. Each skill contains:

- **SKILL.md**: Core instructions, templates, and workflows
- **Metadata**: Name, description, and trigger keywords

### Skill Categories

#### Understanding Phase
| Skill | Purpose |
|-------|---------|
| `requirements-analyst` | Parse requirements from Confluence, decompose into tasks |
| `brainstorming` | Explore ideas through dialogue, create designs |

#### Planning Phase
| Skill | Purpose |
|-------|---------|
| `architect` | High-level architecture decisions |
| `api-designer` | REST API design, DTOs, Swagger docs |
| `writing-plans` | Create granular implementation plans |
| `executing-plans` | Execute plans in batches with review |
| `using-git-worktrees` | Create isolated git worktrees |

#### Implementation Phase
| Skill | Purpose |
|-------|---------|
| `coder` | Backend implementation (Controller/Service/Repository) |
| `coder-frontend` | Frontend implementation (React/Vue/Angular) |
| `frontend-design` | Create distinctive, production-grade UI |
| `project-generator` | Generate NestJS project scaffolding |

#### Quality Phase
| Skill | Purpose |
|-------|---------|
| `code-reviewer` | Code quality, security, performance review |
| `test-generator` | Generate comprehensive tests |
| `systematic-debugger` | Root cause analysis and debugging |
| `verification-before-completion` | Verify claims with evidence |

#### Finalization Phase
| Skill | Purpose |
|-------|---------|
| `finishing-branch` | Complete branch work, create PR/merge |
| `documentation-generator` | Generate project documentation |
| `reflect` | Capture lessons learned, process improvements |

#### Utility
| Skill | Purpose |
|-------|---------|
| `atlassian-skill` | Jira/Confluence integration |
| `skill-creator` | Create new skills |
| `using-skills` | Meta-skill for finding and using skills |

### Skill Flow

```
Requirements Analyst → Brainstorm → Writing Plan
                                        ↓
                    Architect → API Designer → Executing Plans
                                                    ↓
                                          Git Worktrees
                                         /           \
                            Frontend Branch      Backend Branch
                                   ↓                    ↓
                            Frontend Design         Coder
                                   ↓                    ↓
                            Coder Frontend      Code Reviewer
                                   ↓                    ↓
                            Code Reviewer       Test Generator
                                   ↓                    ↓
                            Test Generator      Debugger
                                   ↓                    ↓
                            Debugger            Finishing Branch
                                   ↓                    ↓
                            Finishing Branch    Verification
                                   ↓                    ↓
                                   └──────┬────────────┘
                                          ↓
                                Documentation Generator
                                          ↓
                                       Reflect
```

## Agents

Agents are autonomous workers that execute specific skills. There are two types:

### 1. Orchestrator Agent
- **`new-feature-orchestrator-agent`**: Manages the complete feature workflow
- Calls worker agents in sequence
- Tracks phase completion
- Makes workflow decisions

### 2. Worker Agents
All other agents focus on a single skill:

| Agent | Skill | Purpose |
|-------|-------|---------|
| `brainstorming-agent` | brainstorming | Design through dialogue |
| `requirements-analyst-agent` | requirements-analyst | Parse requirements |
| `architect-agent` | architect | Architecture decisions |
| `api-designer-agent` | api-designer | REST API design |
| `writing-plans-agent` | writing-plans | Create implementation plans |
| `executing-plans-agent` | executing-plans | Execute plans |
| `using-git-worktrees-agent` | using-git-worktrees | Create isolated workspaces |
| `coder-agent` | coder | Backend implementation |
| `coder-frontend-agent` | coder-frontend | Frontend implementation |
| `frontend-design-agent` | frontend-design | UI/UX design |
| `code-reviewer-agent` | code-reviewer | Code quality review |
| `test-generator-agent` | test-generator | Generate tests |
| `systematic-debugger-agent` | systematic-debugger | Root cause analysis |
| `verification-agent` | verification-before-completion | Verify claims |
| `finishing-branch-agent` | finishing-branch | Complete branch work |
| `documentation-generator-agent` | documentation-generator | Generate docs |
| `reflect-agent` | reflect | Capture lessons learned |
| `atlassian-skill-agent` | atlassian-skill | Jira/Confluence |
| `skill-creator-agent` | skill-creator | Create new skills |
| `project-generator-agent` | project-generator | Scaffold projects |

### Key Principle: No Flow Interference

Worker agents must NOT:
- Call other skills directly
- Proceed to the next phase
- Make workflow decisions

Worker agents SHOULD:
- Execute their specific skill
- Return structured results
- Report blockers to the orchestrator

## Hooks

Hooks are shell commands that execute in response to Claude Code events.

### Configured Hooks

| Hook | Trigger | Purpose |
|------|---------|---------|
| `SessionStart` | Session begins | Welcome message |
| `Notification` | Permission/input needed | Desktop notification |
| `Stop` | Response completed | Completion timestamp |
| `PreToolUse:Bash` | Before bash command | Visual feedback |
| `PreToolUse:Edit\|Write` | Before file modification | Alert message |
| `PostToolUse:Write\|Edit` | After file saved | Confirmation |

### Hook Return Codes

| Code | Meaning |
|------|---------|
| `0` | Success, continue |
| `1` | Failure, but continue (warning) |
| `2` | Failure, block operation |

### Custom Hook Examples

**Auto-lint after file changes:**
```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [{
      "type": "command",
      "command": "bash -c 'FILE=$(echo \"$0\" | jq -r \".tool_input.file_path\"); npx eslint --fix \"$FILE\" 2>/dev/null || true'",
      "timeout": 15000
    }]
  }]
}
```

**Block .env modifications:**
```json
{
  "PreToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [{
      "type": "command",
      "command": "bash -c 'FILE=$(echo \"$0\" | jq -r \".tool_input.file_path\"); if [[ \"$FILE\" =~ \\.env ]]; then echo \"Cannot modify .env\" && exit 2; fi'",
      "timeout": 1000
    }]
  }]
}
```

See `hooks/README.md` for more examples.

## Settings

### Team Settings (`settings.json`)

Shared configuration committed to git:

```json
{
  "permissions": {
    "allow": ["Read(**)", "Edit(**)", "Bash(git:*)"],
    "deny": ["Read(.env)", "Bash(rm -rf:*)"]
  },
  "hooks": { ... }
}
```

### Personal Settings (`settings.local.json`)

Personal overrides (gitignored):
- Custom notifications
- Personal preferences
- Experimental features

## Creating New Skills

1. **Create skill directory**: `.claude/skills/<skill-name>/`
2. **Create SKILL.md** with frontmatter:
   ```markdown
   ---
   name: my-skill
   description: "What this skill does"
   ---

   # Skill Name

   ## Overview
   ...
   ```
3. **Create command** (optional): `.claude/commands/<skill-name>.md`
4. **Create agent** (optional): `.claude/agents/<skill-name>-agent.md`

Use `/skill-creator` for guided skill creation.

## Usage Examples

### Complete Feature Workflow
```
/new-feature user profile management
```

### Design-Only Session
```
/brainstorm payment processing integration
```

### Implementation Session
```
/coder implement user registration endpoint
```

### Debugging Session
```
/debugger fix authentication token refresh
```

### Review Code
```
/code-reviewer review src/auth/auth.service.ts
```

### Generate Tests
```
/test-generator generate tests for UserService
```

### Create Documentation
```
/docs-generator create API documentation
```

## Best Practices

1. **Start with brainstorming** for new features
2. **Use git worktrees** for isolated development
3. **Verify before claiming completion** - run tests and build
4. **Review code** before merging
5. **Reflect** after completing features to improve process
6. **Keep skills focused** - one skill, one purpose
7. **Document decisions** in design docs

## Troubleshooting

### Skill not triggering?
- Check skill name matches exactly
- Verify SKILL.md frontmatter syntax
- Ensure skill directory exists

### Hook failing?
- Test hook command manually
- Check timeout settings
- Review return codes

### Agent not executing?
- Verify agent file exists in `agents/`
- Check agent constraints match task
- Review flow position

## References

- [Claude Code Documentation](https://docs.anthropic.com/claude-code)
- [agents/README.md](agents/README.md) - Agent architecture details
- [hooks/README.md](hooks/README.md) - Hook configuration guide
- [skills/SKILL FLOW.md](skills/SKILL%20FLOW.md) - Skill flow diagram
