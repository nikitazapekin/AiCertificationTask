# Writing Plans (Standalone)

Run plan creation via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `writing-plans`
- **description:** `Create implementation plan`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Create detailed implementation plan with bite-sized tasks.

PROCESS:
1. Create comprehensive implementation plan
2. Break into bite-sized tasks (2-5 minutes each)
3. Include exact file paths for each task
4. Provide complete code snippets (not "add validation")
5. Include test commands with expected output

SAVE PLAN TO: docs/plans/YYYY-MM-DD-<feature-name>.md

Each task should follow TDD:
1. Write the failing test
2. Run it to verify it fails
3. Implement minimal code
4. Run test to verify it passes
5. Commit

STOP after saving the plan. Do not proceed to executing-plans or creating worktrees.
```

**After sub-agent completes:** Report the plan location to the user.
