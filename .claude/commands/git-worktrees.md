# Git Worktrees (Standalone)

Run the using-git-worktrees skill to create isolated git workspaces.

**Important:** This command runs the skill in isolation WITHOUT automatically triggering next steps (executing-plans, coder, etc.).

## Input
$ARGUMENTS

## Instructions

Use the `using-git-worktrees` skill to:
1. Check for existing worktree directories (.worktrees, worktrees)
2. Verify directory is in .gitignore
3. Create worktree with new branch
4. Run project setup (npm install, etc.)
5. Verify clean baseline with tests

Directory selection priority:
1. Check existing directories
2. Check CLAUDE.md preference
3. Ask user if neither found

Safety verification:
- Verify directory is gitignored before creating
- Add to .gitignore and commit if needed

**STOP after worktree is ready.** Do not automatically proceed to implementation. Report the worktree location and wait for further instructions.
