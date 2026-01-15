# Requirements Analyst (Standalone)

Run requirements analysis via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `requirements-analyst`
- **description:** `Analyze requirements`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Analyze and decompose requirements into actionable tasks.

PROCESS:
1. Parse requirements from the provided input (Confluence page, spec, user request)
2. Decompose into actionable tasks
3. Identify acceptance criteria
4. Map to technical components

OUTPUT: Structured requirements document with:
- Functional requirements
- Non-functional requirements
- Business rules
- Task breakdown
- Gap analysis

STOP after completing the requirements analysis. Do not proceed to brainstorming or other skills.
```

**After sub-agent completes:** Report the requirements summary to the user.
