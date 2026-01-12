# Brainstorming (Standalone)

Run the brainstorming skill to explore ideas and create designs through dialogue.

**Important:** This command runs the skill in isolation WITHOUT automatically triggering next steps (writing-plans, using-git-worktrees, etc.).

## Input
$ARGUMENTS

## Instructions

Use the `brainstorming` skill to:
1. Understand the current project context
2. Ask questions one at a time to refine the idea
3. Explore 2-3 different approaches with trade-offs
4. Present design in small sections (200-300 words each)
5. Validate each section before continuing

Output a design document covering:
- Problem statement
- Proposed solution
- Architecture
- Data model
- Error handling
- Testing strategy

**STOP after completing the design.** Do not automatically proceed to writing-plans or implementation.
