# Git Worktrees (Standalone)

Run git worktree creation via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `using-git-worktrees`
- **description:** `Create git worktree`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Create isolated git workspace using worktrees.

PROCESS:
1. Check for existing worktree directories (.worktrees, worktrees)
2. Verify directory is in .gitignore
3. Create worktree with new branch
4. Run project setup (npm install, etc.)
5. Verify clean baseline with tests

DIRECTORY SELECTION PRIORITY:
1. Check existing directories
2. Check CLAUDE.md preference
3. Ask user if neither found

SAFETY VERIFICATION:
- Verify directory is gitignored before creating
- Add to .gitignore and commit if needed

STOP after worktree is ready. Do not proceed to implementation. Report the worktree location and wait for further instructions.
```

**After sub-agent completes:** Report the worktree location to the user.
