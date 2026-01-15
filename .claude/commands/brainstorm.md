# Brainstorming (Standalone)

Run brainstorming via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `brainstorming`
- **description:** `Brainstorm design ideas`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Run brainstorming session to explore ideas and create designs through dialogue.

PROCESS:
1. Understand the current project context
2. Ask questions one at a time to refine the idea
3. Explore 2-3 different approaches with trade-offs
4. Present design in small sections (200-300 words each)
5. Validate each section before continuing

OUTPUT: Design document covering:
- Problem statement
- Proposed solution
- Architecture
- Data model
- Error handling
- Testing strategy

STOP after completing the design. Do not proceed to writing-plans or implementation.
```

**After sub-agent completes:** Report the design summary to the user.
