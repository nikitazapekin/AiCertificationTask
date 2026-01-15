# Systematic Debugger (Standalone)

Run debugging via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `systematic-debugger`
- **description:** `Debug issue`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Find root cause before fixing bugs.

IRON LAW: NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST

FOUR PHASES:

1. ROOT CAUSE INVESTIGATION
   - Read error messages carefully
   - Reproduce consistently
   - Check recent changes
   - Trace data flow

2. PATTERN ANALYSIS
   - Find working examples
   - Compare against references
   - Identify differences

3. HYPOTHESIS AND TESTING
   - Form single hypothesis
   - Make smallest possible change
   - Verify before continuing

4. IMPLEMENTATION
   - Create failing test case
   - Implement single fix
   - Verify fix

RED FLAGS (STOP):
- "Quick fix for now"
- "Just try changing X"
- "Skip the test"
- "I don't fully understand but..."

STOP after fixing the issue. Do not proceed to other skills.
```

**After sub-agent completes:** Report the fix and root cause to the user.
