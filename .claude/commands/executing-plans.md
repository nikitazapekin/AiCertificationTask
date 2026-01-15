# Executing Plans (Standalone)

Run plan execution via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `executing-plans`
- **description:** `Execute implementation plan`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Execute a written implementation plan with batch execution.

PROCESS:
1. Load and critically review the plan
2. Raise any concerns before starting
3. Execute tasks in batches (default: 3 tasks)
4. Follow each step exactly as written
5. Report after each batch for feedback

WORKFLOW:
1. Load plan → Review critically
2. Execute batch → Run verifications
3. Report → Wait for feedback
4. Continue or adjust based on feedback

STOP after completing all plan tasks. Do not proceed to finishing-branch or documentation. Report completion and wait for further instructions.
```

**After sub-agent completes:** Report task completion status to the user.
