---
name: using-git-worktrees
description: Use when starting feature work that needs isolation from current workspace - creates isolated git worktrees for backend, frontend, or both for parallel development
---

# Using Git Worktrees

## Overview

Git worktrees create isolated workspaces sharing the same repository, allowing work on multiple branches simultaneously without switching. Supports parallel backend/frontend development with separate worktrees.

**Core principle:** Systematic directory selection + safety verification = reliable isolation.

**Announce at start:** "I'm using the using-git-worktrees skill to set up isolated workspace(s)."

## Step 1: Determine Worktree Type

**Ask user what worktrees to create. Use AskUserQuestion tool:**

```
What type of worktree(s) do you need?

1. Backend only - Single worktree for backend development
2. Frontend only - Single worktree for frontend development
3. Both (parallel) - Separate worktrees for backend and frontend

Which option?
```

**Branch naming convention:**
- Backend only: `feature/<name>`
- Frontend only: `feature/<name>`
- Both: `feature/<name>-backend` and `feature/<name>-frontend`

## Step 2: Directory Selection

Follow this priority order:

### 2.1. Check Existing Directories

```bash
# Check in priority order
ls -d .worktrees 2>/dev/null     # Preferred (hidden)
ls -d worktrees 2>/dev/null      # Alternative
```

**If found:** Use that directory. If both exist, `.worktrees` wins.

### 2.2. Check CLAUDE.md

```bash
grep -i "worktree.*director" CLAUDE.md 2>/dev/null
```

**If preference specified:** Use it without asking.

### 2.3. Ask User

If no directory exists and no CLAUDE.md preference. **Use AskUserQuestion tool.**

```
No worktree directory found. Where should I create worktrees?

1. .worktrees/ (project-local, hidden)
2. ~/worktrees/<project-name>/ (global location)

Which would you prefer?
```

## Step 3: Safety Verification

### For Project-Local Directories

**MUST verify directory is ignored before creating worktree:**

```bash
git check-ignore -q .worktrees 2>/dev/null
```

**If NOT ignored:**
1. Add to .gitignore
2. Commit the change
3. Proceed with worktree creation

## Step 4: Create Worktree(s)

### Single Worktree (Backend or Frontend)

```bash
# Create worktree with new branch
git worktree add <worktree-dir>/<feature-name> -b feature/<feature-name>
cd <worktree-dir>/<feature-name>
```

### Parallel Worktrees (Both Backend and Frontend)

```bash
# Create backend worktree
git worktree add <worktree-dir>/<feature-name>-backend -b feature/<feature-name>-backend

# Create frontend worktree
git worktree add <worktree-dir>/<feature-name>-frontend -b feature/<feature-name>-frontend
```

## Step 5: Run Project Setup (each worktree)

Auto-detect and run appropriate setup in each worktree:

```bash
# Node.js (monorepo)
if [ -f package.json ]; then npm install; fi

# Rust
if [ -f Cargo.toml ]; then cargo build; fi

# Python
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Go
if [ -f go.mod ]; then go mod download; fi
```

## Step 6: Verify Clean Baseline (each worktree)

Run tests to ensure worktree starts clean:

```bash
# For backend worktree
npx nx test backend

# For frontend worktree
npx nx test frontend
```

**If tests fail:** Report failures, ask whether to proceed or investigate. **Use AskUserQuestion tool.**

**If tests pass:** Report ready.

## Step 7: Report Location(s)

### Single Worktree

```
Worktree ready at <full-path>
Branch: feature/<feature-name>
Tests passing (<N> tests, 0 failures)
Ready to implement <feature-name>
```

### Parallel Worktrees

```
Worktrees ready for parallel development:

Backend:
  Path: <full-path-backend>
  Branch: feature/<feature-name>-backend
  Tests: passing (<N> tests)

Frontend:
  Path: <full-path-frontend>
  Branch: feature/<feature-name>-frontend
  Tests: passing (<N> tests)

Ready for parallel implementation of <feature-name>
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
| Parallel development needed | Create separate backend/frontend worktrees |

## Common Mistakes

- **Skipping ignore verification** - Worktree contents get tracked
- **Assuming directory location** - Creates inconsistency
- **Proceeding with failing tests** - Can't distinguish new bugs from pre-existing
- **Using single worktree for full-stack** - Limits parallel development

---

## Next Steps

After worktree(s) created and verified, STOP and present these options:

### For Single Backend Worktree

**Next by flow:** `/coder [context]` - Start backend implementation in the worktree.

**Alternatives:**
- `/code-reviewer [context]` - Review existing code before implementing.

### For Single Frontend Worktree

**Next by flow:** `/frontend-design [context]` - Design UI before frontend implementation.

**Alternatives:**
- `/coder-frontend [context]` - Start frontend implementation directly.

### For Parallel Worktrees (Both)

**Next by flow:** Start implementation in both worktrees:
- Backend: `/coder [context]` in the backend worktree
- Frontend: `/frontend-design [context]` or `/coder-frontend [context]` in the frontend worktree

**Note:** With parallel worktrees, you can work on backend and frontend independently and merge when both are complete.
