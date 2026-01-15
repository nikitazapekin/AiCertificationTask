# Coder Backend (Standalone)

Run backend implementation via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `coder`
- **description:** `Implement backend feature`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Implement backend features following layered architecture.

PROCESS:
1. Understand existing codebase patterns
2. Plan implementation (files to create/modify)
3. Implement following layered architecture
4. Write unit tests
5. Run lint and tests

LAYER PLACEMENT:
- Controller → Presentation layer
- Service → Business Logic layer
- Repository → Data Access layer
- DTO → Data Transfer
- Entity → Domain

DEPENDENCY RULES:
- ✅ Controller → Service → Repository
- ❌ Repository → Service, Service → Controller

STOP after completing implementation. Do not proceed to code review or other skills.
```

**After sub-agent completes:** Report the implementation summary to the user.
