# Verification Before Completion (Standalone)

Run verification via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `verification`
- **description:** `Verify work completion`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Verify work before claiming completion.

IRON LAW: NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE

THE GATE FUNCTION:
1. IDENTIFY: What command proves this claim?
2. RUN: Execute the FULL command (fresh, complete)
3. READ: Full output, check exit code, count failures
4. VERIFY: Does output confirm the claim?
5. ONLY THEN: Make the claim

VERIFICATION COMMANDS:
# Tests
npx nx test backend

# Lint
npx nx lint backend

# Build
npx nx build backend

# All
npx nx run-many -t test,lint,build

RED FLAGS:
- Using "should", "probably", "seems to"
- Expressing satisfaction before verification
- About to commit/push without verification
- Relying on partial verification

Run the command. Read the output. THEN claim the result.
```

**After sub-agent completes:** Report the verification results to the user.
