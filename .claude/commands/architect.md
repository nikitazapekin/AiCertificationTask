# Architect (Standalone)

Run architecture decisions via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `architect`
- **description:** `Make architecture decisions`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Make system architecture decisions for NestJS project.

PROCESS:
1. Determine where to place new code (module, shared, integration)
2. Select appropriate patterns (controller, service, repository)
3. Define architecture layers and dependencies
4. Make technology decisions
5. Consider security and scalability

OUTPUT: Decisions on:
- Layer placement
- Module structure
- Entity relationships
- Transaction boundaries
- Component boundaries

STOP after completing architecture decisions. Do not proceed to API design or implementation.
```

**After sub-agent completes:** Report the architecture decisions to the user.
