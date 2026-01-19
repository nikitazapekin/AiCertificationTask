# Claude Code Configuration

This directory contains skills, commands, agents, and hooks that extend Claude Code's capabilities for this project.

## Directory Structure

```
.claude/
├── agents/          # Agent definitions (execute skills in isolation)
├── commands/        # Slash commands (user-invocable shortcuts)
├── hooks/           # Shell commands triggered by events
├── skills/          # Detailed skill implementations
├── settings.json    # Team configuration (permissions, hooks)
└── settings.local.json  # Personal settings (gitignored)
```

## Architecture: Command -> Agent -> Skill

The system uses a **manual flow** where each command runs in isolation and suggests the next step. This keeps context clean and prevents hallucination.

```
User runs: /requirements-analyst [prompt]
              │
              ▼
    ┌─────────────────────┐
    │   Command Spawns    │
    │   Agent             │
    └─────────────────────┘
              │
              ▼
    ┌─────────────────────┐
    │   Agent Executes    │
    │   Skill             │
    └─────────────────────┘
              │
              ▼
    ┌─────────────────────┐
    │   Output with       │
    │   Context Summary   │
    │   + Next Steps      │
    └─────────────────────┘
```

**Key Benefits:**
- Each command runs in isolated context (prevents hallucination)
- Context summaries allow handoff to next command
- User controls the flow (no automatic chaining)
- Main conversation stays clean

## Quick Start

### Using Commands (Slash Commands)

Commands are shortcuts to invoke skills. Type `/` followed by the command name:

| Command                 | Description                                       |
| ----------------------- | ------------------------------------------------- |
| `/requirements-analyst` | Analyze and decompose requirements                |
| `/brainstorm`           | Explore ideas and create designs through dialogue |
| `/writing-plans`        | Create detailed implementation plans              |
| `/architect`            | System architecture decisions                     |
| `/api-designer`         | REST API design with Swagger                      |
| `/git-worktrees`        | Create isolated workspaces                        |
| `/coder`                | Implement backend features                        |
| `/coder-frontend`       | Implement frontend features                       |
| `/frontend-design`      | Create distinctive UI designs                     |
| `/code-reviewer`        | Code quality and best practices review            |
| `/test-generator`       | Generate unit, integration, and E2E tests         |
| `/debugger`             | Systematic debugging with root cause analysis     |
| `/finishing-branch`     | Complete branch work and merge/PR                 |
| `/verify`               | Verify claims with evidence before completion     |
| `/docs-generator`       | Generate project documentation                    |
| `/reflect`              | Capture lessons learned                           |
| `/project-generator`    | Scaffold new NestJS project structure             |
| `/atlassian`            | Jira/Confluence integration                       |
| `/skill-creator`        | Create new skills                                 |

**Example:**

```
/brainstorm user authentication with OAuth
```

### Context Handoff

Each command outputs a context summary. Pass this to the next command:

```
/brainstorm Design user authentication feature

[Agent completes and outputs context summary]

/writing-plans Based on auth design: JWT with refresh tokens,
  endpoints for login/logout/refresh, middleware for protected routes
```

## Skill Flow

See `skills/SKILL FLOW.md` for the complete visual diagram.

### Quick Reference: Next by Flow

| Current Command | Next by Flow | Why |
|-----------------|--------------|-----|
| `/requirements-analyst` | `/brainstorm` | Turn requirements into design |
| `/brainstorm` | `/writing-plans` | Create implementation tasks |
| `/writing-plans` | `/architect` | Review architecture |
| `/architect` | `/api-designer` | Design APIs |
| `/api-designer` | `/git-worktrees` | Create workspace |
| `/git-worktrees` | `/coder` or `/frontend-design` | Start coding |
| `/coder` | `/code-reviewer` | Review code |
| `/code-reviewer` | `/test-generator` | Generate tests |
| `/test-generator` | `/debugger` or `/finishing-branch` | Debug or finish |
| `/finishing-branch` | `/verify` | Verify before merge |
| `/verify` | `/docs-generator` | Document changes |
| `/docs-generator` | `/reflect` | Capture lessons |
| `/reflect` | (end) | Flow complete |

## Skills

Skills are detailed instruction sets that define how Claude performs specific tasks.

### Skill Categories

#### Understanding Phase

| Skill                  | Purpose                                                  |
| ---------------------- | -------------------------------------------------------- |
| `requirements-analyst` | Parse requirements from Confluence, decompose into tasks |
| `brainstorming`        | Explore ideas through dialogue, create designs           |

#### Planning Phase

| Skill                 | Purpose                              |
| --------------------- | ------------------------------------ |
| `architect`           | High-level architecture decisions    |
| `api-designer`        | REST API design, DTOs, Swagger docs  |
| `writing-plans`       | Create granular implementation plans |
| `using-git-worktrees` | Create isolated git worktrees        |

#### Implementation Phase

| Skill               | Purpose                                                |
| ------------------- | ------------------------------------------------------ |
| `coder`             | Backend implementation (Controller/Service/Repository) |
| `coder-frontend`    | Frontend implementation (React/Vue/Angular)            |
| `frontend-design`   | Create distinctive, production-grade UI                |
| `project-generator` | Generate NestJS project scaffolding                    |

#### Quality Phase

| Skill                            | Purpose                                    |
| -------------------------------- | ------------------------------------------ |
| `code-reviewer`                  | Code quality, security, performance review |
| `test-generator`                 | Generate comprehensive tests               |
| `systematic-debugger`            | Root cause analysis and debugging          |
| `verification-before-completion` | Verify claims with evidence                |

#### Finalization Phase

| Skill                     | Purpose                                       |
| ------------------------- | --------------------------------------------- |
| `finishing-branch`        | Complete branch work, create PR/merge         |
| `documentation-generator` | Generate project documentation                |
| `reflect`                 | Capture lessons learned, process improvements |

#### Utility

| Skill             | Purpose                     |
| ----------------- | --------------------------- |
| `atlassian-skill` | Jira/Confluence integration |
| `skill-creator`   | Create new skills           |

## Agents

Agents are workers that execute skills in isolation and return structured output.

### Agent Behavior

Every agent:
1. Uses the Skill tool to invoke its skill
2. Executes the skill completely
3. **STOPS** when done (no automatic chaining)
4. Provides:
   - **Context Summary**: 2-3 sentences of what was accomplished
   - **Next Steps**: Suggestions for next command

### Agent List

| Agent                           | Skill                          | Purpose                     |
| ------------------------------- | ------------------------------ | --------------------------- |
| `requirements-analyst-agent`    | requirements-analyst           | Parse requirements          |
| `brainstorming-agent`           | brainstorming                  | Design through dialogue     |
| `writing-plans-agent`           | writing-plans                  | Create implementation plans |
| `architect-agent`               | architect                      | Architecture decisions      |
| `api-designer-agent`            | api-designer                   | REST API design             |
| `using-git-worktrees-agent`     | using-git-worktrees            | Create isolated workspaces  |
| `coder-agent`                   | coder                          | Backend implementation      |
| `coder-frontend-agent`          | coder-frontend                 | Frontend implementation     |
| `frontend-design-agent`         | frontend-design                | UI/UX design                |
| `code-reviewer-agent`           | code-reviewer                  | Code quality review         |
| `test-generator-agent`          | test-generator                 | Generate tests              |
| `systematic-debugger-agent`     | systematic-debugger            | Root cause analysis         |
| `verification-agent`            | verification-before-completion | Verify claims               |
| `finishing-branch-agent`        | finishing-branch               | Complete branch work        |
| `documentation-generator-agent` | documentation-generator        | Generate docs               |
| `reflect-agent`                 | reflect                        | Capture lessons learned     |
| `atlassian-skill-agent`         | atlassian-skill                | Jira/Confluence             |
| `skill-creator-agent`           | skill-creator                  | Create new skills           |
| `project-generator-agent`       | project-generator              | Scaffold projects           |

### Key Principle: Stop After Completion

Agents must:
- Execute ONLY their specific skill
- STOP when done
- NOT chain to other skills automatically
- NOT make workflow decisions

The **user** decides the next step based on suggestions.

## Hooks

Hooks are shell commands that execute in response to Claude Code events.

### Configured Hooks

| Hook                      | Trigger                  | Purpose              |
| ------------------------- | ------------------------ | -------------------- |
| `SessionStart`            | Session begins           | Welcome message      |
| `Notification`            | Permission/input needed  | Desktop notification |
| `Stop`                    | Response completed       | Completion timestamp |
| `PreToolUse:Bash`         | Before bash command      | Visual feedback      |
| `PreToolUse:Edit\|Write`  | Before file modification | Alert message        |
| `PostToolUse:Write\|Edit` | After file saved         | Confirmation         |

### Hook Return Codes

| Code | Meaning                         |
| ---- | ------------------------------- |
| `0`  | Success, continue               |
| `1`  | Failure, but continue (warning) |
| `2`  | Failure, block operation        |

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

   ---

   ## Next Steps

   After skill is complete, STOP and present these options:

   **Next by flow:** `/next-command [context]` - Why use this.

   **Alternatives:**
   - `/alt-command [context]` - Why use this.
   ```

3. **Create command** (optional): `.claude/commands/<skill-name>.md`
4. **Create agent** (optional): `.claude/agents/<skill-name>-agent.md`

Use `/skill-creator` for guided skill creation.

## Usage Examples

### Start a New Feature

```
/requirements-analyst Parse the user story for payment processing
```

After completion, agent suggests: `/brainstorm [context]`

```
/brainstorm Based on requirements: payment processing for subscriptions,
  supports Stripe/PayPal, needs webhooks for status updates
```

### Implementation Session

```
/coder Implement the PaymentService with Stripe integration
```

After completion, agent suggests: `/code-reviewer [context]`

```
/code-reviewer Review the PaymentService implementation in
  src/payment/payment.service.ts
```

### Debugging Session

```
/debugger Fix authentication token refresh not working
```

### Generate Tests

```
/test-generator Generate tests for PaymentService
```

### Complete Feature

```
/finishing-branch Complete payment feature branch
```

## Best Practices

1. **Follow the flow** - Use suggested next steps
2. **Pass context** - Include context summaries when calling next command
3. **Use git worktrees** for isolated development
4. **Verify before claiming completion** - Run tests and build
5. **Review code** before merging
6. **Reflect** after completing features to improve process
7. **Keep skills focused** - One skill, one purpose

## Troubleshooting

### Skill not triggering?

- Check skill name matches exactly
- Verify SKILL.md frontmatter syntax
- Ensure skill directory exists

### Agent not stopping?

- Check agent constraints in agent file
- Verify skill has "Next Steps" section
- Report if agent chains automatically

### Context getting polluted?

- Use commands instead of asking directly
- Each command runs in isolated context
- Pass context summaries, not full history

## References

- [Claude Code Documentation](https://docs.anthropic.com/claude-code)
- [agents/README.md](agents/README.md) - Agent architecture details
- [hooks/README.md](hooks/README.md) - Hook configuration guide
- [skills/SKILL FLOW.md](skills/SKILL%20FLOW.md) - Skill flow diagram
