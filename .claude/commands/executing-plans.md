# Executing Plans (Standalone)

Run the executing-plans skill to implement a written plan with batch execution.

**Important:** This command runs the skill in isolation WITHOUT automatically triggering next steps (finishing-branch, etc.).

## Input
$ARGUMENTS

## Instructions

Use the `executing-plans` skill to:
1. Load and critically review the plan
2. Raise any concerns before starting
3. Execute tasks in batches (default: 3 tasks)
4. Follow each step exactly as written
5. Report after each batch for feedback

Process:
1. Load plan → Review critically
2. Execute batch → Run verifications
3. Report → Wait for feedback
4. Continue or adjust based on feedback

**STOP after completing all plan tasks.** Do not automatically proceed to finishing-branch or documentation. Report completion and wait for further instructions.
