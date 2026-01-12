# Finishing Branch (Standalone)

Run the finishing-branch skill to complete development work.

**Important:** This command runs the skill in isolation WITHOUT automatically triggering next steps (documentation, reflect, etc.).

## Input
$ARGUMENTS

## Instructions

Use the `finishing-branch` skill to:
1. Verify tests pass (test, lint, build)
2. Determine base branch
3. Present completion options
4. Execute chosen option
5. Cleanup worktree if applicable

Options to present:
1. Merge back to base branch locally
2. Push and create a Pull Request
3. Keep the branch as-is (handle later)
4. Discard this work (requires confirmation)

Never:
- Proceed with failing tests
- Merge without verifying tests on result
- Delete work without confirmation
- Force-push without explicit request

**STOP after completing the chosen option.** Do not automatically proceed to documentation or reflection.
