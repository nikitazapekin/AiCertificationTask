# Writing Plans (Standalone)

Run the writing-plans skill to create detailed implementation plans.

**Important:** This command runs the skill in isolation WITHOUT automatically triggering next steps (executing-plans, using-git-worktrees, etc.).

## Input
$ARGUMENTS

## Instructions

Use the `writing-plans` skill to:
1. Create comprehensive implementation plan
2. Break into bite-sized tasks (2-5 minutes each)
3. Include exact file paths for each task
4. Provide complete code snippets (not "add validation")
5. Include test commands with expected output

Save plan to: `docs/plans/YYYY-MM-DD-<feature-name>.md`

Each task should follow TDD:
1. Write the failing test
2. Run it to verify it fails
3. Implement minimal code
4. Run test to verify it passes
5. Commit

**STOP after saving the plan.** Do not automatically proceed to executing-plans or creating worktrees.
