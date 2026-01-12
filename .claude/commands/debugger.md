# Systematic Debugger (Standalone)

Run the systematic-debugger skill to find root cause before fixing bugs.

**Important:** This command runs the skill in isolation WITHOUT automatically triggering next steps.

## Input
$ARGUMENTS

## Instructions

Use the `systematic-debugger` skill with the iron law:
**NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST**

Four phases:
1. **Root Cause Investigation**
   - Read error messages carefully
   - Reproduce consistently
   - Check recent changes
   - Trace data flow

2. **Pattern Analysis**
   - Find working examples
   - Compare against references
   - Identify differences

3. **Hypothesis and Testing**
   - Form single hypothesis
   - Make smallest possible change
   - Verify before continuing

4. **Implementation**
   - Create failing test case
   - Implement single fix
   - Verify fix

Red flags (STOP):
- "Quick fix for now"
- "Just try changing X"
- "Skip the test"
- "I don't fully understand but..."

**STOP after fixing the issue.** Do not automatically proceed to other skills.
