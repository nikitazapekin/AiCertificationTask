# Coder Frontend (Standalone)

Run frontend implementation via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `coder-frontend`
- **description:** `Implement frontend feature`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Implement frontend features following component-based architecture.

PROCESS:
1. Understand existing component patterns
2. Plan component hierarchy
3. Implement with proper state management
4. Write tests for components
5. Check accessibility

PATTERNS TO FOLLOW:
- Component architecture (Container/Presentational)
- State management (useState, Context, React Query)
- Custom hooks for reusable logic
- Theme tokens for consistency

FILE NAMING: kebab-case.tsx, use-kebab-case.ts, *.spec.tsx

STOP after completing implementation. Do not proceed to code review or other skills.
```

**After sub-agent completes:** Report the implementation summary to the user.
