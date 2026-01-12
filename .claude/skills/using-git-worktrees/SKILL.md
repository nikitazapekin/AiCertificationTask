---
name: using-git-worktrees
description: Use when starting feature work that needs isolation from current workspace or before executing implementation plans - creates isolated git worktrees with smart directory selection and safety verification
---

# Using Git Worktrees

## Overview

Git worktrees create isolated workspaces sharing the same repository, allowing work on multiple branches simultaneously without switching.

**Core principle:** Systematic directory selection + safety verification = reliable isolation.

**Announce at start:** "I'm using the using-git-worktrees skill to set up an isolated workspace."

## Directory Selection Process

Follow this priority order:

### 1. Check Existing Directories

```bash
# Check in priority order
ls -d .worktrees 2>/dev/null     # Preferred (hidden)
ls -d worktrees 2>/dev/null      # Alternative
```

**If found:** Use that directory. If both exist, `.worktrees` wins.

### 2. Check CLAUDE.md

```bash
grep -i "worktree.*director" CLAUDE.md 2>/dev/null
```

**If preference specified:** Use it without asking.

### 3. Ask User

If no directory exists and no CLAUDE.md preference. **Use AskUserQuestion tool.**

```
No worktree directory found. Where should I create worktrees?

1. .worktrees/ (project-local, hidden)
2. ~/worktrees/<project-name>/ (global location)

Which would you prefer?
```

## Safety Verification

### For Project-Local Directories

**MUST verify directory is ignored before creating worktree:**

```bash
git check-ignore -q .worktrees 2>/dev/null
```

**If NOT ignored:**
1. Add to .gitignore
2. Commit the change
3. Proceed with worktree creation

## Creation Steps

### 1. Create Worktree

```bash
# Create worktree with new branch
git worktree add <path> -b <branch-name>
cd <path>
```

### 2. Run Project Setup

Auto-detect and run appropriate setup:

```bash
# Node.js
if [ -f package.json ]; then npm install; fi

# Rust
if [ -f Cargo.toml ]; then cargo build; fi

# Python
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Go
if [ -f go.mod ]; then go mod download; fi
```

### 3. Verify Clean Baseline

Run tests to ensure worktree starts clean:

```bash
npx nx test backend  # or appropriate test command
```

**If tests fail:** Report failures, ask whether to proceed or investigate. **Use AskUserQuestion tool.**

**If tests pass:** Report ready.

### 4. Report Location

```
Worktree ready at <full-path>
Tests passing (<N> tests, 0 failures)
Ready to implement <feature-name>
```

## Quick Reference

| Situation | Action |
|-----------|--------|
| `.worktrees/` exists | Use it (verify ignored) |
| `worktrees/` exists | Use it (verify ignored) |
| Both exist | Use `.worktrees/` |
| Neither exists | Check CLAUDE.md → Ask user (Use AskUserQuestion tool) |
| Directory not ignored | Add to .gitignore + commit |
| Tests fail during baseline | Report failures + ask (Use AskUserQuestion tool) |

## Common Mistakes

- **Skipping ignore verification** - Worktree contents get tracked
- **Assuming directory location** - Creates inconsistency
- **Proceeding with failing tests** - Can't distinguish new bugs from pre-existing

## Integration

**Called by:**
- `brainstorming` - When ready to implement
- `writing-plans` - For isolated development
- `executing-plans` - For parallel development

**Pairs with:**
- `finishing-branch` - Cleans up worktree after work complete
