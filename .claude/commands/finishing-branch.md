# Finishing Branch (Standalone)

Run branch completion via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `finishing-branch`
- **description:** `Complete branch work`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Complete development work and integrate changes.

PROCESS:
1. Verify tests pass (test, lint, build)
2. Determine base branch
3. Present completion options
4. Execute chosen option
5. Cleanup worktree if applicable

OPTIONS TO PRESENT:
1. Merge back to base branch locally
2. Push and create a Pull Request
3. Keep the branch as-is (handle later)
4. Discard this work (requires confirmation)

NEVER:
- Proceed with failing tests
- Merge without verifying tests on result
- Delete work without confirmation
- Force-push without explicit request

STOP after completing the chosen option. Do not proceed to documentation or reflection.
```

**After sub-agent completes:** Report the completion status to the user.
